#!/usr/bin/env python3

# INFRASTRUCTURE

import argparse
import difflib
import re
import shutil
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

BACKUP_DIR = Path(
    "/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli/"
    "data/documents/github_issues_PRE_BUILDLOG_STRIP_BACKUP_20260828_230949"
)
LIVE_DIR = Path(
    "/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli/"
    "data/documents/github_issues"
)
REPORT_DIR = Path(__file__).parent / "md"

FILE_BASENAMES = [
    "MinerU__1418", "MinerU__2262", "MinerU__826", "curl_cffi__74",
    "ghostty__2210", "pyobjc__175", "pyobjc__176", "pyobjc__34",
]

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

MIGRATION_REPORT_RE = re.compile(r'^\*\*\[Original report\]\([^)]*\) by .+\.\*\*$')
MIGRATION_COMMENT_RE = re.compile(r'^\*\*Original comment by .+\.\*\*$')
MIGRATION_RULE_RE = re.compile(r'^-{40}$')
SEP_RE = re.compile(r'^--- Comment \d+ ---$')
AUTOMATED_COMMENT_RE = re.compile(r'^Removing version: .+ \(automated comment\)$')


def _find_migration_blocks(lines: list) -> list:
    n = len(lines)
    blocks = []
    i = 0
    while i < n:
        line = lines[i]
        if ((MIGRATION_REPORT_RE.match(line) or MIGRATION_COMMENT_RE.match(line))
                and i + 2 < n and lines[i + 1].strip() == ''
                and MIGRATION_RULE_RE.match(lines[i + 2])):
            blocks.append((i, i + 2))
            i += 3
            continue
        i += 1
    return blocks


def _is_automated_only_comment(block: list) -> bool:
    content = []
    i = 0
    n = len(block)
    while i < n:
        line = block[i]
        if line.strip() == '' or line.startswith('Author:') or line.startswith('Date:'):
            i += 1
            continue
        if (MIGRATION_COMMENT_RE.match(line) and i + 2 < n
                and block[i + 1].strip() == '' and MIGRATION_RULE_RE.match(block[i + 2])):
            i += 3
            continue
        content.append(line)
        i += 1
    return len(content) == 1 and bool(AUTOMATED_COMMENT_RE.match(content[0]))


def _find_automated_comment_blocks(lines: list) -> list:
    n = len(lines)
    blocks = []
    i = 0
    while i < n:
        if SEP_RE.match(lines[i]):
            end_idx = next((j for j in range(i + 1, n) if SEP_RE.match(lines[j])), n)
            if _is_automated_only_comment(lines[i + 1:end_idx]):
                blocks.append((i, end_idx - 1))
                i = end_idx
                continue
        i += 1
    return blocks


def _find_all_blocks(lines: list) -> list:
    g_blocks = _find_automated_comment_blocks(lines)
    f_blocks_raw = _find_migration_blocks(lines)
    f_blocks = [
        b for b in f_blocks_raw
        if not any(g[0] <= b[0] and b[1] <= g[1] for g in g_blocks)
    ]
    tagged = [(s, e, 'F') for s, e in f_blocks] + [(s, e, 'G') for s, e in g_blocks]
    return sorted(tagged)


def strip_migration_and_automated(text: str) -> str:
    lines = text.splitlines()
    blocks = _find_all_blocks(lines)
    if not blocks:
        return text
    out = []
    prev_end = -1
    for start, end, _cls in blocks:
        out.extend(lines[prev_end + 1:start])
        prev_end = end
    out.extend(lines[prev_end + 1:])
    result = '\n'.join(out)
    if text.endswith('\n') and not result.endswith('\n'):
        result += '\n'
    return result

PLACEHOLDER_RE = re.compile(r'^\[build log output removed — \d+ lines\]$')


@dataclass
class FileResult:
    filename: str
    reconstructed: str
    live_text: str
    added_back: list = field(default_factory=list)
    unexpected: list = field(default_factory=list)
    placeholders_before: int = 0
    placeholders_after: int = 0
    changed: bool = False


# FUNCTIONS

def _strip_placeholders(lines: list) -> list:
    return [l for l in lines if not PLACEHOLDER_RE.match(l)]


def reconstruct_and_diff(filename: str) -> FileResult:
    backup_text = (BACKUP_DIR / filename).read_text(errors='replace')
    live_text = (LIVE_DIR / filename).read_text(errors='replace')

    reconstructed = strip_build_logs(backup_text)
    reconstructed = strip_migration_and_automated(reconstructed)

    live_lines = live_text.splitlines()
    recon_lines = reconstructed.splitlines()
    live_content = _strip_placeholders(live_lines)
    recon_content = _strip_placeholders(recon_lines)

    sm = difflib.SequenceMatcher(None, live_content, recon_content)
    added_back = []
    unexpected = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        elif tag == 'insert':
            added_back.extend(recon_content[j1:j2])
        else:
            unexpected.append((tag, live_content[i1:i2], recon_content[j1:j2]))

    return FileResult(
        filename=filename,
        reconstructed=reconstructed,
        live_text=live_text,
        added_back=added_back,
        unexpected=unexpected,
        placeholders_before=sum(1 for l in live_lines if PLACEHOLDER_RE.match(l)),
        placeholders_after=sum(1 for l in recon_lines if PLACEHOLDER_RE.match(l)),
        changed=reconstructed != live_text,
    )


def measure_all() -> list:
    return [reconstruct_and_diff(f"{name}.md") for name in FILE_BASENAMES]


def write_report(path: Path, results: list) -> None:
    o = [
        f"# Build-Log Warning-Protection Restore Dry-Run — "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\nBackup source: `{BACKUP_DIR}`",
        f"Live target: `{LIVE_DIR}`",
        "\n## Summary\n",
        "| File | Changed | Lines added back | Unexpected diffs | Placeholders before/after |",
        "|---|---|---|---|---|",
    ]
    for r in results:
        o.append(f"| `{r.filename}` | {r.changed} | {len(r.added_back)} | "
                  f"{len(r.unexpected)} | {r.placeholders_before}/{r.placeholders_after} |")

    any_unexpected = any(r.unexpected for r in results)
    o += [
        "\n## Safety Check\n",
        f"- **No unexpected differences (only newly-protected lines added back)**: "
        f"{'FAIL — see below, --apply will refuse' if any_unexpected else 'PASS'}",
    ]

    o += ["\n## Per-File Detail\n"]
    for r in results:
        o.append(f"### {r.filename}\n")
        if r.added_back:
            o.append("Lines added back (verbatim):\n")
            for l in r.added_back:
                o.append(f"    {l}")
            o.append("")
        else:
            o.append("No lines added back.\n")
        if r.unexpected:
            o.append("**UNEXPECTED DIFFERENCES:**\n")
            for tag, live_chunk, recon_chunk in r.unexpected:
                o.append(f"- tag={tag}")
                o.append(f"  live: {live_chunk}")
                o.append(f"  reconstructed: {recon_chunk}")
            o.append("")

    path.write_text('\n'.join(o) + '\n')


def apply_changes(results: list, ts: str) -> Path:
    backup_dir = LIVE_DIR.parent / f"{LIVE_DIR.name}_PRE_WARNING_RESTORE_BACKUP_{ts}"
    shutil.copytree(LIVE_DIR, backup_dir)
    for r in results:
        if r.changed:
            (LIVE_DIR / r.filename).write_text(r.reconstructed, encoding="utf-8")
    return backup_dir


# ORCHESTRATOR

def restore_workflow(apply: bool) -> None:
    results = measure_all()

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = REPORT_DIR / f"10_restore_dryrun_{ts}.md"
    write_report(report_path, results)
    print(f"report: {report_path}")

    changed = [r for r in results if r.changed]
    total_added_back = sum(len(r.added_back) for r in results)
    total_unexpected = sum(len(r.unexpected) for r in results)
    print(f"files_changed={len(changed)}/{len(results)} lines_added_back={total_added_back} "
          f"unexpected_diffs={total_unexpected}")

    if total_unexpected:
        print("UNEXPECTED DIFFERENCES FOUND — refusing to apply, see report", file=sys.stderr)
        for r in results:
            if r.unexpected:
                print(f"  {r.filename}: {len(r.unexpected)} unexpected diff span(s)",
                      file=sys.stderr)
        if apply:
            sys.exit(1)
        return

    if apply:
        backup_dir = apply_changes(results, ts)
        print(f"Backup: {backup_dir}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Restore the 8 build-log-stripped files under the fixed, warning-protected "
                    "strip_build_logs() — dry-run by default"
    )
    p.add_argument("--apply", action="store_true",
                    help="Overwrite the 8 live files (creates a full-corpus backup first)")
    args = p.parse_args()
    restore_workflow(apply=args.apply)
