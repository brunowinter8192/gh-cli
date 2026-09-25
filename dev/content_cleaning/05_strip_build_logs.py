#!/usr/bin/env python3

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

MIN_BLOCK_LINES = 10
SENSITIVITY_THRESHOLDS = [5, 8, 10, 15, 20, 30]



ERROR_RE = re.compile(r'error|fatal|traceback|exception|failed|warning', re.IGNORECASE)
TRACE_RE = re.compile(r'^\s*File "[^"]+", line \d+, in ')
BACKTRACE_RE = re.compile(r':\d+:\d+:.*0x[0-9a-fA-F]+ in ')

SIGNAL_PATTERNS = [
    re.compile(r'^\s*(running|creating|copying|writing|reading|installing|removing|deleting|'
               r'generating|skipping|cleaning|overriding|byte-compiling|moving)\s+\S'),
    re.compile(r"^Use '.*' instead of '.*' as the compiler$"),
    re.compile(r"^\s*building '.*' extension$"),
    re.compile(r'^\s*(Collecting|Downloading|Using cached|Requirement already satisfied|'
               r'Installing collected packages|Successfully installed|Successfully built|'
               r'Building wheel for|Building wheels for collected packages|'
               r'Installing build dependencies|Getting requirements to build wheel|'
               r'Preparing metadata|Installing backend dependencies|Stored in directory|'
               r'Created wheel for|Looking in indexes|Solving environment|'
               r'Collecting package metadata|Preparing transaction|Verifying transaction|'
               r'Executing transaction|Downloading and Extracting Packages|Channels:|'
               r'Platform:)\b'),
    re.compile(r'━{5,}'),
    re.compile(r'^## Package Plan ##$'),
    re.compile(r'^\s*The following (NEW )?packages will be (downloaded|INSTALLED):$'),
    re.compile(r'^\s*-\s+(conda-forge|defaults)\s*$'),
    re.compile(r'^\s*[\w.+-]+\s+(conda-forge|pkgs/main)[\w/.:+-]*::'),
    re.compile(r'^\s*\$\s+conda (activate|deactivate|update)'),
    re.compile(r'^\s*(Cloning into|remote:|Receiving objects|Resolving deltas|Updating files|'
               r'requesting all changes|adding changesets|adding manifests|adding file changes|'
               r'updating to branch)\b'),
    re.compile(r'^\d+ files updated, \d+ files (merged|removed)'),
    re.compile(r'^added \d+ changesets with \d+ changes to \d+ files'),
    re.compile(r"^\s*(/\S+/)?([a-zA-Z0-9_.-]*-)?(clang|gcc|g\+\+|cc1|cc)\s+-\S"),
    re.compile(r'^\s*\S+\.(c|cc|cpp|cxx|m|mm|h|hpp|hh):\d+:\d+:\s*note:'),
]


def _is_protected(line: str) -> bool:
    return bool(ERROR_RE.search(line) or TRACE_RE.search(line) or BACKTRACE_RE.search(line))


def _is_signal(line: str) -> bool:
    if _is_protected(line):
        return False
    return any(p.search(line) for p in SIGNAL_PATTERNS)


def _is_blank(line: str) -> bool:
    return line.strip() == ''


BRIDGE_GAP = 3


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



@dataclass
class Block:
    filename: str
    start_line: int
    end_line: int
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
    md_files = list_md_files(source_dir)
    results = measure_all(md_files, threshold)
    safety_ok, safety_total = assert_safety(results)
    report_path = write_dump_report(results)
    print_corpus_summary(md_files, results, report_path, safety_ok, safety_total)
    print_sensitivity(md_files)
    print_worst_file(md_files)
    if apply:
        reject_apply()


# FUNCTIONS

def list_md_files(source_dir: Path) -> list:
    md_files = sorted(source_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {source_dir}", file=sys.stderr)
        sys.exit(1)
    return md_files


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


NARROW_VOCAB_RE = re.compile(
    r'^\s*(copying|creating|running|writing|reading|installing|byte-compiling)\s+\S'
)


def measure_worst_file_coverage(md_files: list) -> dict:
    largest = max(md_files, key=lambda p: len(p.read_text(errors='replace')))
    text = largest.read_text(errors='replace')
    lines = text.splitlines()
    candidate_lines = [l for l in lines if l.strip() and not _is_protected(l)]
    narrow_hits = sum(1 for l in candidate_lines if NARROW_VOCAB_RE.match(l))
    full_hits = sum(1 for l in candidate_lines if _is_signal(l))
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


def write_dump(path: Path, results: list) -> None:
    o = []
    for fr in sorted(results, key=lambda x: x.filename):
        for b in fr.blocks:
            o.append(f"{b.filename}:{b.start_line}-{b.end_line}")
            o.append(b.text)
            o.append("")
    path.write_text('\n'.join(o))


def write_dump_report(results: list) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = REPORT_DIR / f"05_strip_build_logs_dryrun_{ts}.md"
    write_dump(report_path, results)
    return report_path


def print_corpus_summary(md_files: list, results: list, report_path: Path, safety_ok: bool, safety_total: int) -> None:
    total_blocks = sum(len(fr.blocks) for fr in results)
    total_lines = sum(b.length for fr in results for b in fr.blocks)
    total_chars = sum(fr.chars_removed for fr in results)
    print(f"report: {report_path}")
    print(f"files_scanned={len(md_files)} files_affected={len(results)} "
          f"blocks={total_blocks} lines_removed={total_lines} chars_removed={total_chars} "
          f"safety={'PASS' if safety_ok else 'FAIL'} ({safety_total} lines checked)")


def print_sensitivity(md_files: list) -> None:
    for row in measure_sensitivity(md_files):
        print(f"sensitivity threshold={row['threshold']}: "
              f"files_affected={row['files_affected']} blocks={row['blocks']} "
              f"lines_removed={row['lines_removed']} chars_removed={row['chars_removed']}")


def print_worst_file(md_files: list) -> None:
    wf = measure_worst_file_coverage(md_files)
    print(f"worst_file={wf['filename']} file_chars={wf['file_chars']} "
          f"candidate_lines={wf['candidate_lines']} narrow_hits={wf['narrow_hits']} "
          f"full_hits={wf['full_hits']} chars_removed={wf['chars_removed']}")


def reject_apply() -> None:
    raise RuntimeError("--apply is not enabled in this milestone (dry-run only).")


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
