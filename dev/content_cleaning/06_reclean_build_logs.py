#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_SOURCE_DIR = Path(
    "/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli/"
    "data/documents/github_issues"
)
REPORT_DIR = Path(__file__).parent / "md"

MIN_BLOCK_LINES = 10
BRIDGE_GAP = 3

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


# ORCHESTRATOR

def reclean_workflow(source_dir: Path, apply: bool) -> None:
    md_files = sorted(source_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {source_dir}", file=sys.stderr)
        sys.exit(1)

    results = measure_all(md_files)
    assert_safety(results)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = REPORT_DIR / f"06_reclean_dryrun_{ts}.md"
    write_report(report_path, results, len(md_files))
    print(report_path)

    if apply:
        backup_dir = apply_changes(source_dir, results, ts)
        print(f"Backup: {backup_dir}")


# FUNCTIONS

def measure_all(md_files: list) -> list[dict]:
    results = []
    for fp in md_files:
        before = fp.read_text(errors='replace')
        lines = before.splitlines()
        blocks = _find_build_log_blocks(lines)
        after = strip_build_logs(before)
        gross_removed = sum(len('\n'.join(lines[s:e + 1])) + 1 for s, e in blocks)
        results.append({
            "filename": fp.name,
            "filepath": fp,
            "before": before,
            "after": after,
            "lines": lines,
            "blocks": blocks,
            "gross_chars_removed": gross_removed,
            "net_chars_removed": len(before) - len(after),
            "changed": after != before,
        })
    return results


def assert_safety(results: list[dict]) -> None:
    violations = []
    total_checked = 0
    for r in results:
        for start, end in r["blocks"]:
            for line in r["lines"][start:end + 1]:
                total_checked += 1
                if ERROR_RE.search(line):
                    violations.append((r["filename"], line))
    if violations:
        for fname, line in violations:
            print(f"SAFETY VIOLATION: {fname}: {line[:120]!r}", file=sys.stderr)
        print(f"ASSERTION FAIL: {len(violations)} violation(s) in {total_checked} removed lines "
              f"checked — refusing to write report or corpus.", file=sys.stderr)
        sys.exit(1)


def apply_changes(source_dir: Path, results: list[dict], ts: str) -> Path:
    backup_dir = source_dir.parent / f"{source_dir.name}_PRE_BUILDLOG_STRIP_BACKUP_{ts}"
    shutil.copytree(source_dir, backup_dir)
    for r in results:
        if r["changed"]:
            r["filepath"].write_text(r["after"], encoding="utf-8")
    return backup_dir


def write_report(path: Path, results: list[dict], total_files: int) -> None:
    changed = [r for r in results if r["changed"]]
    total_gross = sum(r["gross_chars_removed"] for r in results)
    total_net = sum(r["net_chars_removed"] for r in results)
    total_blocks = sum(len(r["blocks"]) for r in changed)

    o = [
        f"# Issue Build-Log Reclean Dry-Run Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\nCorpus: {total_files} files · `data/documents/github_issues/`",
        "\n## Summary\n",
        "| Metric | Value |",
        "|---|---|",
        f"| Files that would change | {len(changed)} / {total_files} |",
        f"| Total blocks removed | {total_blocks} |",
        f"| Total chars removed — gross (size of text cut out) | {total_gross:,} |",
        f"| Total chars removed — net (file shrinkage, placeholder written back) | {total_net:,} |",
        "\n## Safety Assertion\n",
        "- **No removed line contains an error indicator "
        "(`error`/`fatal`/`Traceback`/`Exception`/`failed`/`warning`, case-insensitive)**: PASS "
        "(checked above — a FAIL exits before this report is written)",
    ]

    if changed:
        o += [
            "\n## Per-File Results (changed files, sorted by gross chars removed)\n",
            "| File | Blocks | Gross chars removed | Net chars removed |",
            "|---|---|---|---|",
        ]
        for r in sorted(changed, key=lambda x: -x["gross_chars_removed"]):
            o.append(f"| `{r['filename']}` | {len(r['blocks'])} | "
                      f"{r['gross_chars_removed']:,} | {r['net_chars_removed']:,} |")

    unchanged = [r for r in results if not r["changed"]]
    o += [
        "\n## Unchanged Files\n",
        f"{len(unchanged)} files would not change.",
    ]

    path.write_text('\n'.join(o) + '\n')


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Re-clean existing issue MDs with strip_build_logs() — dry-run by default"
    )
    p.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    p.add_argument("--apply", action="store_true",
                    help="Overwrite files in place (creates timestamped backup first)")
    args = p.parse_args()
    reclean_workflow(args.source_dir, apply=args.apply)
