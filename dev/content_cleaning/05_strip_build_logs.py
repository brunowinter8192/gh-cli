#!/usr/bin/env python3
# Detect + (dry-run) strip build/install-tool log noise from issue MDs (setuptools/distutils
# output, pip/conda install output, compiler invocations + diagnostics, VCS clone output).
# Read-only in this milestone — dry-run only, no --apply exercised, corpus never modified.
#
# strip_build_logs() below is written to be moved verbatim into src/github/text_cleaning.py in a
# later, separately approved step (stdlib-only, no dev-specific logic). Source of truth once
# merged: src/github/text_cleaning.py. dev/ may not import src/ (hook: block_dev_imports_src) —
# intentional duplication, not drift, per the convention in 03/04's DOCS.md entry.
#
# Usage: python3 dev/content_cleaning/05_strip_build_logs.py [--source-dir PATH] [--threshold N]

# INFRASTRUCTURE

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

DEFAULT_SOURCE_DIR = Path(
    "/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli/"
    "data/documents/github_issues"
)
REPORT_DIR = Path(__file__).parent / "md"

# Run-length threshold: minimum consecutive block length (lines) to qualify as a removable
# build log. See "Run-Length Sensitivity" in the generated report for the measurement behind
# this default.
MIN_BLOCK_LINES = 10
SENSITIVITY_THRESHOLDS = [5, 8, 10, 15, 20, 30]


# ============================================================================================
# --- verbatim copy candidate for src/github/text_cleaning.py (keep in sync once merged) -----
# stdlib-only (re). No dev-specific logic.

# Hard safety exclusion — a line matching any of these is NEVER classified as removable and
# NEVER bridged over. These are the retrieval target of the document (the actual failure).
ERROR_RE = re.compile(r'error|fatal|traceback|exception|failed', re.IGNORECASE)
# Python traceback frame ("File "...", line N, in func") and native/gdb backtrace frame
# ("path:line:col: 0xADDR in func") — protected even though they don't literally contain an
# error-indicator word. Without this, caret/underline diagnostic markers (below) can bridge
# straight across real traceback frames and delete the crash location. See process notes.
TRACE_RE = re.compile(r'^\s*File "[^"]+", line \d+, in ')
BACKTRACE_RE = re.compile(r':\d+:\d+:.*0x[0-9a-fA-F]+ in ')

# Vocabulary: line-start / structural anchors for machine-generated build & install output.
# Deliberately loose (single verbs, generic phrases) — safety comes from the run-length gate
# in _find_build_log_blocks, not from vocabulary precision. See report for corpus-grep
# justification (these verbs also occur in ordinary prose, but never in long unbroken runs).
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
    # pip-list-style two-column package/version table row (e.g. "numpy    2.1.1")
    re.compile(r'^[A-Za-z][\w.\-]*\s{2,}[\w.\-]+$'),
    re.compile(r'^Package\s+Version$'),
    re.compile(r'^-{5,}\s+-{5,}$'),
]


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


# Max consecutive non-signal, non-blank, non-protected lines bridged inside an open run (handles
# e.g. a compiler diagnostic's wrapped message / source-context lines between two matched header
# lines). A run only ever starts and ends ON a matched signal line, never on bridged filler.
BRIDGE_GAP = 3


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


# Strip build/install-tool log noise from the full text of one issue MD
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

# --- end verbatim copy candidate --------------------------------------------------------------
# ============================================================================================


@dataclass
class Block:
    filename: str
    start_line: int   # 1-indexed
    end_line: int      # 1-indexed
    length: int
    before: str
    first: str
    last: str
    after: str
    text: str


@dataclass
class FileResult:
    filename: str
    file_chars: int
    blocks: list = field(default_factory=list)
    chars_removed: int = 0


# ORCHESTRATOR

def strip_build_logs_workflow(source_dir: Path, threshold: int, apply: bool) -> None:
    md_files = sorted(source_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {source_dir}", file=sys.stderr)
        sys.exit(1)

    results = measure_all(md_files, threshold)
    safety_ok, safety_total = assert_safety(results)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = REPORT_DIR / f"05_strip_build_logs_dryrun_{ts}.md"
    write_dump(report_path, results)

    # All measurement/summary output goes to stdout (for the calling agent's chat message),
    # never into the artifact itself — the artifact is the removed content, nothing else.
    total_blocks = sum(len(fr.blocks) for fr in results)
    total_lines = sum(b.length for fr in results for b in fr.blocks)
    total_chars = sum(fr.chars_removed for fr in results)
    print(f"report: {report_path}")
    print(f"files_scanned={len(md_files)} files_affected={len(results)} "
          f"blocks={total_blocks} lines_removed={total_lines} chars_removed={total_chars} "
          f"safety={'PASS' if safety_ok else 'FAIL'} ({safety_total} lines checked)")
    for row in measure_sensitivity(md_files):
        print(f"sensitivity threshold={row['threshold']}: "
              f"files_affected={row['files_affected']} blocks={row['blocks']} "
              f"lines_removed={row['lines_removed']} chars_removed={row['chars_removed']}")
    wf = measure_worst_file_coverage(md_files)
    print(f"worst_file={wf['filename']} file_chars={wf['file_chars']} "
          f"candidate_lines={wf['candidate_lines']} narrow_hits={wf['narrow_hits']} "
          f"full_hits={wf['full_hits']} chars_removed={wf['chars_removed']}")

    if apply:
        # Not exercised in this milestone (negative scope: no --apply run). Present only for
        # convention-parity with 04_reclean_issues.py; production integration is a later step.
        raise RuntimeError("--apply is not enabled in this milestone (dry-run only).")


# FUNCTIONS

# Compute per-file block detail (context lines + full removed text) at the given threshold
def measure_all(md_files: list, threshold: int) -> list:
    results = []
    for fp in md_files:
        text = fp.read_text(errors='replace')
        lines = text.splitlines()
        blocks = _find_build_log_blocks(lines, threshold)
        fr = FileResult(filename=fp.name, file_chars=len(text))
        for start, end in blocks:
            block_text = '\n'.join(lines[start:end + 1])
            fr.blocks.append(Block(
                filename=fp.name,
                start_line=start + 1,
                end_line=end + 1,
                length=end - start + 1,
                before=lines[start - 1] if start > 0 else "",
                first=lines[start],
                last=lines[end],
                after=lines[end + 1] if end + 1 < len(lines) else "",
                text=block_text,
            ))
            fr.chars_removed += len(block_text) + 1
        if fr.blocks:
            results.append(fr)
    return results


# Explicit assertion: no removed line contains an error indicator. Returns (pass, lines_checked).
def assert_safety(results: list) -> tuple:
    violations = 0
    total_lines = 0
    for fr in results:
        for b in fr.blocks:
            for line in b.text.split('\n'):
                total_lines += 1
                if ERROR_RE.search(line):
                    violations += 1
                    print(f"SAFETY VIOLATION: {fr.filename} L{b.start_line}-{b.end_line}: "
                          f"{line[:120]!r}", file=sys.stderr)
    return violations == 0, total_lines


# Narrow 7-verb baseline vocabulary (setuptools verbs only) — used only to re-measure the
# prior "34% of the worst file" coverage claim against the actual corpus, not part of detection.
NARROW_VOCAB_RE = re.compile(
    r'^\s*(copying|creating|running|writing|reading|installing|byte-compiling)\s+\S'
)


# Re-measure narrow-vocab vs. full-vocab vs. final-detector coverage on the corpus's largest
# file, for the report's vocabulary section. Computed fresh each run (no hardcoded numbers).
def measure_worst_file_coverage(md_files: list) -> dict:
    largest = max(md_files, key=lambda p: len(p.read_text(errors='replace')))
    text = largest.read_text(errors='replace')
    lines = text.splitlines()
    candidate_lines = [l for l in lines if l.strip() and not _is_protected(l)]
    narrow_hits = sum(1 for l in candidate_lines if NARROW_VOCAB_RE.match(l))
    full_hits = sum(1 for l in candidate_lines if _is_signal(l) or any(
        p.search(l) for p in SIGNAL_PATTERNS))
    blocks = _find_build_log_blocks(lines, MIN_BLOCK_LINES)
    chars_removed = sum(sum(len(lines[i]) + 1 for i in range(s, e + 1)) for s, e in blocks)
    return {
        "filename": largest.name,
        "file_chars": len(text),
        "candidate_lines": len(candidate_lines),
        "narrow_hits": narrow_hits,
        "full_hits": full_hits,
        "chars_removed": chars_removed,
    }


# Sweep MIN_BLOCK_LINES across SENSITIVITY_THRESHOLDS for the report's sensitivity table
def measure_sensitivity(md_files: list) -> list:
    rows = []
    for threshold in SENSITIVITY_THRESHOLDS:
        files_affected = 0
        total_blocks = 0
        total_lines = 0
        total_chars = 0
        for fp in md_files:
            text = fp.read_text(errors='replace')
            lines = text.splitlines()
            blocks = _find_build_log_blocks(lines, threshold)
            if blocks:
                files_affected += 1
                total_blocks += len(blocks)
                for start, end in blocks:
                    total_lines += end - start + 1
                    total_chars += sum(len(l) + 1 for l in lines[start:end + 1])
        rows.append({
            "threshold": threshold,
            "files_affected": files_affected,
            "blocks": total_blocks,
            "lines_removed": total_lines,
            "chars_removed": total_chars,
        })
    return rows


# Write the dump: nothing but the removed content. One identification line per block (source
# file + line range, nothing else on that line), then the removed text verbatim and unmodified,
# then the next block. No summary, no tables, no vocabulary discussion, no context lines, no
# per-block commentary. All measurement belongs in the caller's chat output, not in this file.
def write_dump(path: Path, results: list) -> None:
    o = []
    for fr in sorted(results, key=lambda x: x.filename):
        for b in fr.blocks:
            o.append(f"{b.filename}:{b.start_line}-{b.end_line}")
            o.append(b.text)
            o.append("")
    path.write_text('\n'.join(o))


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Detect + dry-run strip build/install log noise from issue MDs"
    )
    p.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    p.add_argument("--threshold", type=int, default=MIN_BLOCK_LINES,
                    help="minimum block length (lines) to qualify as removable")
    p.add_argument("--apply", action="store_true",
                    help="NOT enabled in this milestone — dry-run only")
    args = p.parse_args()
    strip_build_logs_workflow(args.source_dir, args.threshold, apply=args.apply)
