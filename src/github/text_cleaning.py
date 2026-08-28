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
# log, plus the max consecutive non-signal/non-blank/non-bridge-blocked filler lines bridged
# inside an open run (wrapped compiler diagnostic messages, source-context lines). A block only
# ever starts and ends ON a matched signal line, never on bridged filler. Values measured against
# the 844-file github_issues corpus; see process-docs/content_cleaning/.
MIN_BLOCK_LINES = 10
BRIDGE_GAP = 3

# Hard safety exclusion — a line matching any of these is NEVER classified as removable and NEVER
# bridged over. These are the retrieval target of the document (the actual failure).
ERROR_RE = re.compile(r'error|fatal|traceback|exception|failed', re.IGNORECASE)
# Python traceback frame ("File "...", line N, in func") and native/gdb backtrace frame
# ("path:line:col: 0xADDR in func") — protected even though they don't literally contain an
# error-indicator word. Without this, caret/underline diagnostic markers (below) can bridge
# straight across real traceback frames and delete the crash location. See process notes.
TRACE_RE = re.compile(r'^\s*File "[^"]+", line \d+, in ')
BACKTRACE_RE = re.compile(r':\d+:\d+:.*0x[0-9a-fA-F]+ in ')

# Human-language guard — protected on the same footing as error/traceback lines, for two
# reasons: (1) a prose line sandwiched inside a signal run must never be bridged over (it is not
# a wrapped diagnostic continuation, it is a person's sentence), and (2) a prose sentence that
# happens to start with a vocabulary verb ("running the tests locally is step one") must never be
# classified as signal in the first place. Tool output (distutils/pip/VCS/compiler lines) is
# terse and essentially never carries function words like "the", "is", "which" — ordinary English
# sentences do. A word-tokenized stopword count is a cheap, language-structure-based proxy for
# that distinction; it does not depend on the vocabulary regexes below, so it catches prose
# regardless of which verb it happens to open with.
#
# 'a' and 'i' are deliberately excluded even though they are common English words: '-I/path' and
# '-Iinclude/' are real compiler include flags (a bare "I" lands as its own token whenever the
# path starts with a non-word char), and single-letter macro/loop parameters named 'a' are
# common C ("#define ALIGN(v, a) ..."). Both would otherwise leak a spurious stopword hit from
# genuine tool/source output. No other word in this list is a plausible single/double-letter
# compiler flag or common short C identifier on its own.
_PROSE_STOPWORDS = frozenset({
    'an', 'the', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
    'do', 'does', 'did', 'me', 'my', 'we', 'our', 'you', 'your', 'he', 'she', 'it', 'its',
    'they', 'them', 'this', 'that', 'these', 'those', 'and', 'but', 'if', 'or', 'because', 'as',
    'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'into', 'through', 'during',
    'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'on', 'off', 'over',
    'under', 'again', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all',
    'any', 'both', 'each', 'more', 'most', 'other', 'some', 'such', 'no', 'not', 'only', 'own',
    'same', 'so', 'than', 'too', 'very', 'can', 'will', 'just', 'should', 'now', 'which', 'who',
    'whom',
})
_PROSE_MIN_STOPWORD_HITS = 2

# Vocabulary: line-start / structural anchors for machine-generated build & install output.
# Split into two tiers with different collision risk against ordinary prose:
#
# _LOOSE_VERB_RE / _LOOSE_GERUND_RE — a single common English word followed by arbitrary
# content, nothing else required. This is the shape that can open a real sentence ("running the
# tests locally is step one", "Downloading the wheel by hand ... is the only thing that worked"),
# so these alone are additionally gated by _is_prose_line() below. Measured per-anchor against
# the 844-file corpus before deciding which bare words belong here: "Collecting" costs 0 real
# lines when prose-gated (free), "Downloading" costs 16 (gdb debug-symbol-fetch messages,
# modelscope's "Downloading Model from X to Y") — gated anyway, because an ungated bare gerund is
# exactly the shape a person's sentence can wear.
#
# SIGNAL_PATTERNS — multi-word or structurally specific anchors (exact pip/conda/VCS strings,
# file:line:col diagnostic headers, "::" conda spec rows, digit-anchored VCS summaries). These
# follow the project's existing corpus-grep methodology (a phrase this specific essentially never
# occurs in human prose) and are NOT prose-gated for signal classification. Measured and left
# ungated on purpose: "Requirement already satisfied" costs ~300 lines, "Use 'X' instead of 'Y'
# as the compiler" costs 2, "Created wheel for" costs 2, "The following packages will be
# downloaded:" costs 4, "added N changesets with M changes to K files" costs 1, the
# file:line:col diagnostic header costs 8 — all genuine tool output, and all long/specific enough
# (or digit/colon-anchored) that a person coincidentally typing the exact phrase is not a
# realistic residual risk the way a bare gerund is. They remain subject to the prose gate like
# everything else when encountered as a BRIDGE candidate (see _is_bridge_blocked) — that check
# does not depend on which category a line would otherwise match.
_LOOSE_VERB_RE = re.compile(
    r'^\s*(running|creating|copying|writing|reading|installing|removing|deleting|'
    r'generating|skipping|cleaning|overriding|byte-compiling|moving)\s+\S'
)
_LOOSE_GERUND_RE = re.compile(r'^\s*(Collecting|Downloading)\b')
SIGNAL_PATTERNS = [
    re.compile(r"^\s*warning: no (directories|files|previously-included files) found matching"),
    re.compile(r"^Use '.*' instead of '.*' as the compiler$"),
    re.compile(r"^\s*building '.*' extension$"),
    # pip / conda package-manager output (bare "Collecting"/"Downloading" live in
    # _LOOSE_GERUND_RE instead — see comment above)
    re.compile(r'^\s*(Using cached|Requirement already satisfied|'
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


# A line reads as ordinary English prose (function-word density), not terse tool output.
# \b...\b (not a bare character class) matters: a flag token like "-Wshorten-64-to-32" or an
# arch name like "i386"/"x86_64" is one contiguous \w run, so a naive [A-Za-z']+ scan (which
# ignores digits) fragments it into spurious standalone words — "i386" yields a bare "i", which
# collides with the pronoun "I". Word-boundary anchors refuse to match inside a \w run that
# contains digits, so compiler flags stay non-words instead of leaking fake stopword hits.
# Counted as a SET, not a running count: a compiler diagnostic like
# "precision: 'long' to 'int' [-Wshorten-64-to-32]" contains the real preposition "to" plus a
# second "to" fragment from the flag name itself — two occurrences of the same word, which is not
# the density signature of a sentence. Genuine prose reliably uses 2+ *distinct* function words.
def _is_prose_line(line: str) -> bool:
    words = re.findall(r"\b[A-Za-z']+\b", line.lower())
    hits = {w for w in words if w in _PROSE_STOPWORDS}
    return len(hits) >= _PROSE_MIN_STOPWORD_HITS


# Hard-excluded: never signal, never bridgeable, always breaks a run. Error/traceback/backtrace
# only — NOT prose. Prose gating is scoped separately (see _is_signal and _is_bridge_blocked)
# because gating every anchored pattern here excluded ~300 genuine
# "Requirement already satisfied: X in Y (from Z)" pip lines during tuning.
def _is_protected(line: str) -> bool:
    return bool(ERROR_RE.search(line) or TRACE_RE.search(line) or BACKTRACE_RE.search(line))


# Line matches the build-log vocabulary and is not hard-excluded. The loose verb/gerund patterns
# are the ones ambiguous enough to open a real sentence, so they alone are also required to not
# read as prose; the multi-word/structural anchors in SIGNAL_PATTERNS are not (see comment above
# them).
def _is_signal(line: str) -> bool:
    if _is_protected(line):
        return False
    if any(p.search(line) for p in SIGNAL_PATTERNS):
        return True
    if _LOOSE_VERB_RE.search(line) or _LOOSE_GERUND_RE.search(line):
        return not _is_prose_line(line)
    return False


# A candidate bridge line (arbitrary filler between two confirmed signal lines) must never be
# bridged over if it is prose, regardless of which vocabulary category — if any — it resembles.
# Bridging exists for wrapped compiler diagnostics and source-context lines; a person's sentence
# sandwiched inside a log is neither, so it gets the same hard-stop treatment as an error line.
def _is_bridge_blocked(line: str) -> bool:
    return _is_protected(line) or _is_prose_line(line)


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
            # bridge candidate: peek ahead up to BRIDGE_GAP non-signal/blank/bridge-blocked lines
            k = j
            gap = 0
            while (k < n and gap < BRIDGE_GAP and not _is_signal(lines[k])
                   and not _is_blank(lines[k]) and not _is_bridge_blocked(lines[k])):
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
