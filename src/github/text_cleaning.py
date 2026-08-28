# INFRASTRUCTURE
import re

# Any HTML <img> tag (any attribute order/presence)
IMG_RE = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
# Any markdown image with non-empty URL: ![alt](url) — subsumes extension-specific and data-URI forms.
# Requires non-empty URL ([^)]+) to avoid matching ![]() used as literal code examples in prose.
MD_IMG_RE = re.compile(r'!\[[^\]]*\]\([^)]+\)', re.IGNORECASE)
# Bare base64 data-URI not inside markdown image syntax
DATA_URI_RE = re.compile(
    r'data:image/[^;]+;base64,[A-Za-z0-9+/=]+',
    re.IGNORECASE,
)

# --- build/install log noise (setuptools/distutils, pip/conda, VCS, compiler) ------------------
# Run-length threshold: minimum consecutive block length (lines) to qualify as a removable build
# log, plus the max consecutive non-signal/non-blank/non-protected filler lines bridged inside an
# open run (wrapped compiler diagnostic messages, source-context lines). A block only ever starts
# and ends ON a matched signal line, never on bridged filler. Values measured against the
# 844-file github_issues corpus; see process-docs/content_cleaning/.
MIN_BLOCK_LINES = 10
BRIDGE_GAP = 3

# Hard safety exclusion — a line matching any of these is NEVER classified as removable and NEVER
# bridged over. These are the retrieval target of the document (the actual failure).
ERROR_RE = re.compile(r'error|fatal|traceback|exception|failed', re.IGNORECASE)
# Python traceback frame ("File "...", line N, in func") and native/gdb backtrace frame
# ("path:line:col: 0xADDR in func") — protected even though they don't literally contain an
# error-indicator word. Without this, caret/underline diagnostic markers can bridge straight
# across real traceback frames and delete the crash location. See process notes.
TRACE_RE = re.compile(r'^\s*File "[^"]+", line \d+, in ')
BACKTRACE_RE = re.compile(r':\d+:\d+:.*0x[0-9a-fA-F]+ in ')

# Vocabulary: line-start / structural anchors for machine-generated build & install output.
# Deliberately loose (single verbs, generic phrases) — safety comes from the run-length gate in
# _find_build_log_blocks, not from vocabulary precision. See process-docs/content_cleaning/ for
# corpus-grep justification (these verbs also occur in ordinary prose, but never in long unbroken
# runs) and for why a stopword-based prose guard was tried on top of this vocabulary and reverted:
# it was built against five invented adversarial fixtures, not one instance of which occurs in
# the 844-file corpus, while it measurably cost real corpus coverage (~6,679 chars of genuine
# noise no longer removed) and roughly doubled this module's size and comment load.
SIGNAL_PATTERNS = [
    # distutils/setuptools verb lines (running install, creating build/, copying X -> Y, ...)
    re.compile(r'^\s*(running|creating|copying|writing|reading|installing|removing|deleting|'
               r'generating|skipping|cleaning|overriding|byte-compiling|moving)\s+\S'),
    re.compile(r"^\s*warning: no (directories|files|previously-included files) found matching"),
    re.compile(r"^Use '.*' instead of '.*' as the compiler$"),
    re.compile(r"^\s*building '.*' extension$"),
    # pip / conda package-manager output
    re.compile(r'^\s*(Collecting|Downloading|Using cached|Requirement already satisfied|'
               r'Installing collected packages|Successfully installed|Successfully built|'
               r'Building wheel for|Building wheels for collected packages|'
               r'Installing build dependencies|Getting requirements to build wheel|'
               r'Preparing metadata|Installing backend dependencies|Stored in directory|'
               r'Created wheel for|Looking in indexes|Solving environment|'
               r'Collecting package metadata|Preparing transaction|Verifying transaction|'
               r'Executing transaction|Downloading and Extracting Packages|Channels:|'
               r'Platform:)\b'),
    re.compile(r'━{5,}'),                                            # pip/conda progress bar
    re.compile(r'^## Package Plan ##$'),
    re.compile(r'^\s*The following (NEW )?packages will be (downloaded|INSTALLED):$'),
    re.compile(r'^\s*-\s+(conda-forge|defaults)\s*$'),
    re.compile(r'^\s*[\w.+-]+\s+(conda-forge|pkgs/main)[\w/.:+-]*::'),  # conda install spec row
    re.compile(r'^\s*\$\s+conda (activate|deactivate|update)'),
    # VCS clone/pull output (git/hg)
    re.compile(r'^\s*(Cloning into|remote:|Receiving objects|Resolving deltas|Updating files|'
               r'requesting all changes|adding changesets|adding manifests|adding file changes|'
               r'updating to branch)\b'),
    re.compile(r'^\d+ files updated, \d+ files (merged|removed)'),
    re.compile(r'^added \d+ changesets with \d+ changes to \d+ files'),
    # compiler invocation + diagnostics
    re.compile(r"^\s*(/\S+/)?([a-zA-Z0-9_.-]*-)?(clang|gcc|g\+\+|cc1|cc)\s+-\S"),
    re.compile(r'^\s*\S+\.(c|cc|cpp|cxx|m|mm|h|hpp|hh):\d+:\d+:\s*(warning|note):'),
    re.compile(r'^\d+ warnings? generated\.$'),
    re.compile(r'^\s*clang: warning:'),
]


# FUNCTIONS

# Apply all generic noise subs to a single line; used by strip_generic_noise and per-line callers
def _strip_line(line: str) -> str:
    line = re.sub(IMG_RE, '', line)
    line = re.sub(MD_IMG_RE, '', line)
    line = re.sub(DATA_URI_RE, '', line)
    line = re.sub(r'!\[Uploading[^\]]*\]\(\)', '', line)
    line = re.sub(r'\S{1000,}', '', line)
    return line


# Strip generic image noise and long no-space runs from text
def strip_generic_noise(text: str) -> str:
    return '\n'.join(_strip_line(line) for line in text.splitlines())


# Hard-excluded: never signal, never bridgeable, always breaks a run.
def _is_protected(line: str) -> bool:
    return bool(ERROR_RE.search(line) or TRACE_RE.search(line) or BACKTRACE_RE.search(line))


# Line matches the build-log vocabulary and is not hard-excluded
def _is_signal(line: str) -> bool:
    if _is_protected(line):
        return False
    return any(p.search(line) for p in SIGNAL_PATTERNS)


def _is_blank(line: str) -> bool:
    return line.strip() == ''


# Group signal lines into removable (start, end) line-index spans (0-indexed, inclusive)
def _find_build_log_blocks(lines: list, threshold: int = MIN_BLOCK_LINES) -> list:
    n = len(lines)
    blocks = []
    i = 0
    while i < n:
        if not _is_signal(lines[i]):
            i += 1
            continue
        start = i
        end = i
        j = i + 1
        while j < n:
            if _is_protected(lines[j]):
                break
            if _is_signal(lines[j]):
                end = j
                j += 1
                continue
            if _is_blank(lines[j]):
                j += 1
                continue
            # bridge candidate: peek ahead up to BRIDGE_GAP non-signal/blank/protected lines
            k = j
            gap = 0
            while (k < n and gap < BRIDGE_GAP and not _is_signal(lines[k])
                   and not _is_blank(lines[k]) and not _is_protected(lines[k])):
                k += 1
                gap += 1
            if k < n and _is_signal(lines[k]):
                end = k
                j = k + 1
                continue
            break
        if end - start + 1 >= threshold:
            blocks.append((start, end))
        i = end + 1
    return blocks


def _placeholder(n_lines: int) -> str:
    return f"[build log output removed — {n_lines} lines]"


# Strip build/install-tool log noise (setuptools/distutils, pip/conda, VCS, compiler) from text
def strip_build_logs(text: str) -> str:
    lines = text.splitlines()
    blocks = _find_build_log_blocks(lines, MIN_BLOCK_LINES)
    if not blocks:
        return text
    out = []
    prev_end = -1
    for start, end in blocks:
        out.extend(lines[prev_end + 1:start])
        out.append(_placeholder(end - start + 1))
        prev_end = end
    out.extend(lines[prev_end + 1:])
    result = '\n'.join(out)
    if text.endswith('\n') and not result.endswith('\n'):
        result += '\n'
    return result
