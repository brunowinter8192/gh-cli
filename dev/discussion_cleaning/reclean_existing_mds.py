#!/usr/bin/env python3
# Re-clean 78 existing discussion MDs using strip_noise() — noise-only pass, safe on built MDs.
# strip_noise does NOT touch ## headings, metadata lines, or comment attribution headers;
# it only removes dosu footers/greetings, img tags, failed uploads, checklist blocks, badge lines,
# and caps no-space runs >= 1000 chars.
# Intentional verbatim copy of src/github/discussion_cleaning.py strip_noise() (+ _bare,
# _is_badge_line, constants). dev/ may not import src/ (hook: block_dev_imports_src) —
# intentional duplication, not drift. Update if the source changes.
# Dry-run by default (no writes). Use --apply to overwrite files (creates timestamped backup first).
# Usage: python3 dev/discussion_cleaning/reclean_existing_mds.py [--apply] [--source-dir PATH]

# INFRASTRUCTURE

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_SOURCE_DIR = Path(
    "/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli/"
    "data/documents/github_discussions"
)
REPORT_DIR = Path(__file__).parent / "reclean_reports"
NO_SPACE_LIMIT = 1000

# --- verbatim copy of src/github/discussion_cleaning.py (keep in sync) ---
FOOTER_LOOKAHEAD = 20
_BADGE_DOMAINS = frozenset([
    'shields.io/badge', 'camo.githubusercontent.com',
    'app.dosu.dev/response-feedback', 'go.dosu.dev',
])
_FOOTER_TEXT_PHRASES = (
    'To reply, just mention',
    'Docs are dead. Just use',
    'Share context across your team and agents. Try',
)
GH_IMG_RE = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
MD_IMG_RE = re.compile(r'!\[[^\]]*\]\([^)]+\)', re.IGNORECASE)
ISSUE_HEADING_RE = re.compile(
    r'^### (?:🔎 Search before asking|🤖 Consult the online AI assistant)'
)
# --------------------------------------------------------------------------------------------


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
    report_path = REPORT_DIR / f"reclean_dryrun_{ts}.md"
    write_report(report_path, results, len(md_files))
    print(report_path)

    if apply:
        backup_dir = apply_changes(source_dir, results, ts)
        changed_count = sum(1 for r in results if r["changed"])
        total_removed = sum(r["chars_removed"] for r in results)
        corpus_after_peak = max(r["after_max"] for r in results)
        h2_ok = all(r["before_h2"] == r["after_h2"] for r in results)
        print(f"Backup: {backup_dir}")
        print(f"Files changed: {changed_count} / {len(results)}")
        print(f"Total chars removed: {total_removed:,}")
        print(f"Corpus peak no-space run after: {corpus_after_peak} (must be <{NO_SPACE_LIMIT}): {'OK' if corpus_after_peak < NO_SPACE_LIMIT else 'FAIL'}")
        print(f"## heading count preserved: {'OK' if h2_ok else 'FAIL'}")
        print_sample(results)


# FUNCTIONS

def _bare(line: str) -> str:
    return re.sub(r'^[\s>]+', '', line).strip()


def _is_badge_line(line: str) -> bool:
    c = _bare(line)
    has_badge = '[![' in c or c.startswith('<sup>How did I do?')
    has_dosu = any(x in c for x in _BADGE_DOMAINS)
    return has_badge and has_dosu


def _is_dosu_markerless_greeting(line: str) -> bool:
    stripped = re.sub(r'^[\s>_*]+', '', line.replace('&nbsp;', ' ')).strip()
    if not (stripped.startswith('Hi @') or stripped.startswith('你好@') or stripped.startswith('你好 @')):
        return False
    if 'Dosu' not in line:
        return False
    return ('helping' in line and 'team' in line) or ('帮助' in line and '团队' in line)


def _is_dosu_footer_text_line(line: str) -> bool:
    stripped = re.sub(r'^[\s>_*]+', '', line).strip()
    has_dosu_ref = 'Dosu' in line or '@dosu' in line
    for phrase in _FOOTER_TEXT_PHRASES:
        if stripped.startswith(phrase) and has_dosu_ref:
            return True
    if '回复时只需提及' in line and '@dosu' in line:
        return True
    if '已经过时' in line and ('Dosu' in line or 'dosu.dev' in line):
        return True
    return False


def strip_noise(text: str) -> str:
    lines = text.splitlines()
    i = 0
    out = []
    while i < len(lines):
        line = lines[i]
        bare = _bare(line)
        if bare == '<!-- Dosu Comment Footer -->':
            badge_idx = next(
                (j for j in range(i + 1, min(i + FOOTER_LOOKAHEAD, len(lines)))
                 if _is_badge_line(lines[j])), None
            )
            if badge_idx is not None:
                block = lines[i:badge_idx + 1]
                if not any(re.search(r'^\s*>\s*\*\*@', l) for l in block):
                    i = badge_idx + 1
                    continue
        if bare == '<!-- Greeting -->':
            greet_idx = next(
                (j for j in range(i + 1, min(i + 5, len(lines))) if lines[j].strip()), None
            )
            if greet_idx is not None:
                i = greet_idx + 1
                continue
        if ISSUE_HEADING_RE.match(line.strip()):
            j = i + 1
            while j < len(lines) and (lines[j].strip().startswith('- [') or not lines[j].strip()):
                j += 1
            i = j
            continue
        if _is_badge_line(line):
            i += 1
            continue
        if _is_dosu_footer_text_line(line):
            i += 1
            continue
        if _is_dosu_markerless_greeting(line):
            i += 1
            continue
        line = re.sub(r'<!--\s*(?:Answer|Greeting)\s*-->', '', line)
        line = re.sub(GH_IMG_RE, '', line)
        line = re.sub(MD_IMG_RE, '', line)
        line = re.sub(r'\S{1000,}', '', line)
        out.append(line)
        i += 1
    return "\n".join(out)


def max_no_space_run(text: str) -> int:
    tokens = re.findall(r'\S+', text)
    return max((len(t) for t in tokens), default=0)


def count_h2_headings(text: str) -> int:
    return sum(1 for line in text.splitlines() if re.match(r'^## ', line))


def measure_all(md_files: list) -> list[dict]:
    results = []
    for fp in md_files:
        before = fp.read_text(errors='replace')
        after = strip_noise(before)
        # Preserve original trailing whitespace form for writes (don't introduce whitespace diffs).
        if before.endswith('\n') and not after.endswith('\n'):
            after += '\n'
        # Changed only when content differs beyond trailing whitespace (ignore \n vs \n\n endings).
        results.append({
            "filename": fp.name,
            "filepath": fp,
            "before": before,
            "after": after,
            "before_max": max_no_space_run(before),
            "after_max": max_no_space_run(after),
            "before_h2": count_h2_headings(before),
            "after_h2": count_h2_headings(after),
            "chars_removed": len(before) - len(after),
            "changed": after.rstrip() != before.rstrip(),
        })
    return results


def assert_safety(results: list[dict]) -> None:
    failures_ns = [r for r in results if r["after_max"] >= NO_SPACE_LIMIT]
    if failures_ns:
        for r in failures_ns:
            print(
                f"ASSERTION FAIL no-space: {r['filename']}: after_max={r['after_max']} >= {NO_SPACE_LIMIT}",
                file=sys.stderr,
            )
        sys.exit(1)

    failures_h2 = [r for r in results if r["before_h2"] != r["after_h2"]]
    if failures_h2:
        for r in failures_h2:
            print(
                f"ASSERTION FAIL h2-heading: {r['filename']}: before={r['before_h2']} after={r['after_h2']}",
                file=sys.stderr,
            )
        sys.exit(1)


def apply_changes(source_dir: Path, results: list[dict], ts: str) -> Path:
    backup_dir = source_dir.parent / f"{source_dir.name}_backup_{ts}"
    shutil.copytree(source_dir, backup_dir)
    for r in results:
        if r["changed"]:
            r["filepath"].write_text(r["after"], encoding="utf-8")
    return backup_dir


def print_sample(results: list[dict]) -> None:
    footer_files = [r for r in results if r["changed"] and "<!-- Dosu Comment Footer -->" in r["before"]]
    if not footer_files:
        return
    sample = sorted(footer_files, key=lambda x: -x["chars_removed"])[0]
    before_lines = sample["before"].splitlines()
    after_lines = sample["after"].splitlines()
    footer_idx = next((i for i, l in enumerate(before_lines) if "<!-- Dosu Comment Footer -->" in l), None)
    if footer_idx is None:
        return
    start = max(0, footer_idx - 1)
    end = min(len(before_lines), footer_idx + 8)
    print(f"\nSample — {sample['filename']} (before, lines {start+1}-{end}):")
    for line in before_lines[start:end]:
        print(f"  {line[:120]}")
    print(f"\nSample — {sample['filename']} (after, same region):")
    for line in after_lines[start:min(start + 4, len(after_lines))]:
        print(f"  {line[:120]}")


def write_report(path: Path, results: list[dict], total_files: int) -> None:
    changed = [r for r in results if r["changed"]]
    corpus_before_peak = max(r["before_max"] for r in results)
    corpus_after_peak = max(r["after_max"] for r in results)
    total_removed = sum(r["chars_removed"] for r in results)
    h2_ok = all(r["before_h2"] == r["after_h2"] for r in results)
    ns_ok = corpus_after_peak < NO_SPACE_LIMIT

    o = [
        f"# Reclean Dry-Run Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\nCorpus: {total_files} files · `data/documents/github_discussions/`",
        "\n## Summary\n",
        "| Metric | Value |",
        "|---|---|",
        f"| Files that would change | {len(changed)} / {total_files} |",
        f"| Total chars removed | {total_removed:,} |",
        f"| Corpus peak no-space run — before | {corpus_before_peak:,} |",
        f"| Corpus peak no-space run — after  | {corpus_after_peak:,} |",
        "\n## Safety Assertions\n",
        f"- **max no-space run < {NO_SPACE_LIMIT} for ALL files after**: {'✅ PASS' if ns_ok else '❌ FAIL'}",
        f"- **`## ` heading count identical before/after (all files)**: {'✅ PASS' if h2_ok else '❌ FAIL'}",
    ]

    if changed:
        o += [
            "\n## Per-File Results (changed files, sorted by chars removed)\n",
            "| File | Before max | After max | Chars removed | H2 Δ |",
            "|---|---|---|---|---|",
        ]
        for r in sorted(changed, key=lambda x: -x["chars_removed"]):
            h2_flag = "✅" if r["before_h2"] == r["after_h2"] else f"❌ {r['before_h2']}→{r['after_h2']}"
            o.append(
                f"| `{r['filename']}` | {r['before_max']:,} | {r['after_max']:,} "
                f"| {r['chars_removed']:,} | {h2_flag} |"
            )

    unchanged = [r for r in results if not r["changed"]]
    o += [
        f"\n## Unchanged Files\n",
        f"{len(unchanged)} files would not change.",
    ]

    path.write_text('\n'.join(o) + '\n')


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Re-clean existing discussion MDs with strip_noise() — dry-run by default"
    )
    p.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    p.add_argument("--apply", action="store_true", help="Overwrite files in place (creates timestamped backup first)")
    args = p.parse_args()
    reclean_workflow(args.source_dir, apply=args.apply)
