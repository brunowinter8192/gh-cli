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

MIN_RUN_LINES = 3

ERROR_RE = re.compile(r'error|fatal|traceback|exception|failed', re.IGNORECASE)
TRACE_RE = re.compile(r'^\s*File "[^"]+", line \d+, in ')
BACKTRACE_RE = re.compile(r':\d+:\d+:.*0x[0-9a-fA-F]+ in ')

CRASH_RE = re.compile(
    r'panic:|Segmentation fault|signal=SIG\w+|core dumped|#FailureMessage|Crash keys:|'
    r'Received signal \d+|exitCode=\d{5,}',
    re.IGNORECASE,
)

SHAPES = {
    "ghostty_debug": re.compile(r'^(debug|info|warning)\([a-zA-Z_]+\):'),
    "playwright_pw": re.compile(r'^\s*pw:[a-z:]+'),
    "loguru_narration": re.compile(
        r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+ \| (TRACE|DEBUG|INFO|SUCCESS|WARNING)\s*\|'
    ),
}


@dataclass
class Block:
    filename: str
    shape: str
    start_line: int
    end_line: int
    length: int
    text: str


@dataclass
class FileResult:
    filename: str
    filepath: Path
    file_chars: int
    blocks: list = field(default_factory=list)
    gross_chars_removed: int = 0
    net_chars_removed: int = 0
    changed: bool = False


# ORCHESTRATOR

def strip_debug_stream_workflow(source_dir: Path) -> None:
    md_files = list_md_files(source_dir)
    results = measure_all(md_files)
    total_checked = assert_safety(results)
    report_path = write_dump_report(results)
    print(f"report: {report_path}")
    print_corpus_summary(md_files, results, total_checked)
    print_shape_summaries(results)


# FUNCTIONS

def list_md_files(source_dir: Path) -> list:
    md_files = sorted(source_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {source_dir}", file=sys.stderr)
        sys.exit(1)
    return md_files


def _is_protected(line: str) -> bool:
    return bool(ERROR_RE.search(line) or TRACE_RE.search(line) or BACKTRACE_RE.search(line)
                or CRASH_RE.search(line))


def _find_shape_blocks(lines: list, shape_re: "re.Pattern") -> list:
    def is_signal(line: str) -> bool:
        return bool(shape_re.match(line)) and not _is_protected(line)

    n = len(lines)
    blocks = []
    i = 0
    while i < n:
        if not is_signal(lines[i]):
            i += 1
            continue
        start = i
        end = i
        j = i + 1
        while j < n:
            if is_signal(lines[j]):
                end = j
                j += 1
                continue
            if lines[j].strip() == '':
                j += 1
                continue
            break
        if end - start + 1 >= MIN_RUN_LINES:
            blocks.append((start, end))
        i = end + 1
    return blocks


def _find_all_blocks(lines: list) -> list:
    all_blocks = []
    for shape_name, shape_re in SHAPES.items():
        for start, end in _find_shape_blocks(lines, shape_re):
            all_blocks.append((start, end, shape_name))
    return sorted(all_blocks)


def _placeholder(n_lines: int) -> str:
    return f"[debug-stream output removed — {n_lines} lines]"


def strip_debug_stream(text: str) -> str:
    lines = text.splitlines()
    blocks = _find_all_blocks(lines)
    if not blocks:
        return text
    out = []
    prev_end = -1
    for start, end, _shape in blocks:
        out.extend(lines[prev_end + 1:start])
        out.append(_placeholder(end - start + 1))
        prev_end = end
    out.extend(lines[prev_end + 1:])
    result = '\n'.join(out)
    if text.endswith('\n') and not result.endswith('\n'):
        result += '\n'
    return result


def measure_all(md_files: list) -> list:
    results = []
    for fp in md_files:
        before = fp.read_text(errors='replace')
        lines = before.splitlines()
        blocks_idx = _find_all_blocks(lines)
        after = strip_debug_stream(before)
        blocks = []
        gross = 0
        for start, end, shape_name in blocks_idx:
            block_text = '\n'.join(lines[start:end + 1])
            blocks.append(Block(
                filename=fp.name, shape=shape_name,
                start_line=start + 1, end_line=end + 1,
                length=end - start + 1, text=block_text,
            ))
            gross += len(block_text) + 1
        results.append(FileResult(
            filename=fp.name, filepath=fp, file_chars=len(before),
            blocks=blocks, gross_chars_removed=gross,
            net_chars_removed=len(before) - len(after),
            changed=after != before,
        ))
    return results


def assert_safety(results: list) -> int:
    violations = []
    total_checked = 0
    for fr in results:
        for b in fr.blocks:
            for line in b.text.split('\n'):
                total_checked += 1
                if _is_protected(line):
                    violations.append((fr.filename, line))
    if violations:
        for fname, line in violations:
            print(f"SAFETY VIOLATION: {fname}: {line[:120]!r}", file=sys.stderr)
        print(f"ASSERTION FAIL: {len(violations)} violation(s) in {total_checked} removed lines "
              f"checked — refusing to write report.", file=sys.stderr)
        sys.exit(1)
    return total_checked


def write_dump(path: Path, results: list) -> None:
    o = []
    for fr in sorted(results, key=lambda x: x.filename):
        for b in fr.blocks:
            o.append(f"{b.filename}:{b.start_line}-{b.end_line} [{b.shape}]")
            o.append(b.text)
            o.append("")
    path.write_text('\n'.join(o))


def write_dump_report(results: list) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = REPORT_DIR / f"09_strip_debug_stream_dryrun_{ts}.md"
    write_dump(report_path, results)
    return report_path


def print_corpus_summary(md_files: list, results: list, total_checked: int) -> None:
    changed = [fr for fr in results if fr.changed]
    total_blocks = sum(len(fr.blocks) for fr in results)
    total_lines = sum(b.length for fr in results for b in fr.blocks)
    total_gross = sum(fr.gross_chars_removed for fr in results)
    total_net = sum(fr.net_chars_removed for fr in results)
    total_corpus_chars = sum(fr.file_chars for fr in results)
    pct = 100 * total_gross / total_corpus_chars if total_corpus_chars else 0
    print(f"files_scanned={len(md_files)} files_affected={len(changed)} blocks={total_blocks} "
          f"lines_removed={total_lines} gross_chars_removed={total_gross} "
          f"net_chars_removed={total_net} pct_corpus={pct:.2f}% "
          f"safety=PASS ({total_checked} lines checked)")


def print_shape_summaries(results: list) -> None:
    for shape_name in SHAPES:
        shape_blocks = [b for fr in results for b in fr.blocks if b.shape == shape_name]
        shape_files = {b.filename for b in shape_blocks}
        shape_lines = sum(b.length for b in shape_blocks)
        shape_chars = sum(len(b.text) + 1 for b in shape_blocks)
        print(f"shape={shape_name} files={len(shape_files)} blocks={len(shape_blocks)} "
              f"lines={shape_lines} chars={shape_chars}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Detect + dry-run strip junk class B (DEBUG_STREAM) from issue MDs — "
                    "dry-run only, no --apply"
    )
    p.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    args = p.parse_args()
    strip_debug_stream_workflow(args.source_dir)
