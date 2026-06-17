#!/usr/bin/env python3
# Re-clean existing issue MDs using strip_generic_noise() — image/data-URI/no-space pass only.
# The existing MDs were already built with strip_noise+strip_comments_noise (format logic done);
# this pass applies only the generic strips (IMG, MD_IMG, DATA_URI, \S{1000,} net) which are
# additive and safe on already-formatted MDs.
# Intentional verbatim copy of src/github/text_cleaning.py strip_generic_noise() (+ regexes).
# dev/ may not import src/ (hook: block_dev_imports_src) — intentional duplication, not drift.
# Update if the source changes. Source of truth: src/github/text_cleaning.py
# Dry-run by default (no writes). Use --apply to overwrite files (creates timestamped backup first).
# Usage: python3 dev/issue_cleaning/reclean_issues.py [--apply] [--source-dir PATH]

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
REPORT_DIR = Path(__file__).parent / "reclean_reports"
NO_SPACE_LIMIT = 1000

# --- verbatim copy of src/github/text_cleaning.py (keep in sync) ---
IMG_RE = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
MD_IMG_RE = re.compile(r'!\[[^\]]*\]\([^)]+\)', re.IGNORECASE)
DATA_URI_RE = re.compile(
    r'data:image/[^;]+;base64,[A-Za-z0-9+/=]+',
    re.IGNORECASE,
)


def _strip_line(line: str) -> str:
    line = re.sub(IMG_RE, '', line)
    line = re.sub(MD_IMG_RE, '', line)
    line = re.sub(DATA_URI_RE, '', line)
    line = re.sub(r'!\[Uploading[^\]]*\]\(\)', '', line)
    line = re.sub(r'\S{1000,}', '', line)
    return line


def strip_generic_noise(text: str) -> str:
    return '\n'.join(_strip_line(line) for line in text.splitlines())
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
        print(f"Backup: {backup_dir}")
        print(f"Files changed: {changed_count} / {len(results)}")
        print(f"Total chars removed: {total_removed:,}")
        print(f"Corpus peak no-space run after: {corpus_after_peak} (must be <{NO_SPACE_LIMIT}): {'OK' if corpus_after_peak < NO_SPACE_LIMIT else 'FAIL'}")


# FUNCTIONS

def max_no_space_run(text: str) -> int:
    tokens = re.findall(r'\S+', text)
    return max((len(t) for t in tokens), default=0)


def measure_all(md_files: list) -> list[dict]:
    results = []
    for fp in md_files:
        before = fp.read_text(errors='replace')
        after = strip_generic_noise(before)
        if before.endswith('\n') and not after.endswith('\n'):
            after += '\n'
        results.append({
            "filename": fp.name,
            "filepath": fp,
            "before": before,
            "after": after,
            "before_max": max_no_space_run(before),
            "after_max": max_no_space_run(after),
            "chars_removed": len(before) - len(after),
            "changed": after.rstrip() != before.rstrip(),
        })
    return results


def assert_safety(results: list[dict]) -> None:
    failures = [r for r in results if r["after_max"] >= NO_SPACE_LIMIT]
    if failures:
        for r in failures:
            print(
                f"ASSERTION FAIL no-space: {r['filename']}: after_max={r['after_max']} >= {NO_SPACE_LIMIT}",
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


def write_report(path: Path, results: list[dict], total_files: int) -> None:
    changed = [r for r in results if r["changed"]]
    corpus_before_peak = max(r["before_max"] for r in results)
    corpus_after_peak = max(r["after_max"] for r in results)
    total_removed = sum(r["chars_removed"] for r in results)
    ns_ok = corpus_after_peak < NO_SPACE_LIMIT

    o = [
        f"# Issue Reclean Dry-Run Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\nCorpus: {total_files} files · `data/documents/github_issues/`",
        "\n## Summary\n",
        "| Metric | Value |",
        "|---|---|",
        f"| Files that would change | {len(changed)} / {total_files} |",
        f"| Total chars removed | {total_removed:,} |",
        f"| Corpus peak no-space run — before | {corpus_before_peak:,} |",
        f"| Corpus peak no-space run — after  | {corpus_after_peak:,} |",
        "\n## Safety Assertion\n",
        f"- **max no-space run < {NO_SPACE_LIMIT} for ALL files after**: {'✅ PASS' if ns_ok else '❌ FAIL'}",
    ]

    if changed:
        o += [
            "\n## Per-File Results (changed files, sorted by chars removed)\n",
            "| File | Before max | After max | Chars removed |",
            "|---|---|---|---|",
        ]
        for r in sorted(changed, key=lambda x: -x["chars_removed"]):
            o.append(
                f"| `{r['filename']}` | {r['before_max']:,} | {r['after_max']:,} "
                f"| {r['chars_removed']:,} |"
            )

    unchanged = [r for r in results if not r["changed"]]
    o += [
        f"\n## Unchanged Files\n",
        f"{len(unchanged)} files would not change.",
    ]

    path.write_text('\n'.join(o) + '\n')


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Re-clean existing issue MDs with strip_generic_noise() — dry-run by default"
    )
    p.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    p.add_argument("--apply", action="store_true", help="Overwrite files in place (creates timestamped backup first)")
    args = p.parse_args()
    reclean_workflow(args.source_dir, apply=args.apply)
