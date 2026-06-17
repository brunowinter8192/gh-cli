#!/usr/bin/env python3
# Validate strip_discussion_noise() on the 78-MD corpus. Read-only — never writes source files.
# Intentional verbatim copy of src/github/discussion_cleaning.py strip_noise() (+ _bare,
# _is_badge_line, constants). dev/ may not import src/ (hook: block_dev_imports_src) —
# intentional duplication, not drift. Update if the source changes.
# strip_discussion_noise() is kept as a thin local wrapper (full version in index_discussions.py
# which pulls mcp — not importable in dev/).
# Usage: python3 dev/discussion_cleaning/A_strip_validation.py [--source-dir PATH]

# INFRASTRUCTURE

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

DEFAULT_SOURCE_DIR = Path(
    "/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli/"
    "data/documents/github_discussions"
)
REPORT_DIR = Path(__file__).parent / "A_strip_validation_reports"
THRESHOLD = 1500

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
GH_IMG_RE = re.compile(
    r'<img\s+width="\d+"\s+height="\d+"\s+alt="[^"]*"\s+'
    r'src="https://github\.com/user-attachments/assets/[a-f0-9-]+"[^>]*/?>',
    re.IGNORECASE,
)
MD_IMG_RE = re.compile(
    r'!\[[^\]]*\]\([^)]*\.(?:png|jpe?g|gif|svg|webp)(?:\?[^)]*)?\)',
    re.IGNORECASE,
)
ISSUE_HEADING_RE = re.compile(
    r'^### (?:🔎 Search before asking|🤖 Consult the online AI assistant)'
)
# ------------------------------------------------------------------

SPOT_CHECK_FILES = [
    "MinerU__2961.md",   # footer-heavy: 5+ footers, greeting, answer-markers, issue-template
    "MinerU__3304.md",   # footer + failed-upload
    "MinerU__3185.md",   # greeting + img
    "MinerU__4279.md",   # 2 img tags
]
SPOT_CHECK_PATTERNS = [
    (r'^\*\*@\w', "comment attribution headers"),
    (r'^\s*>\s*\*\*@', "threaded replies"),
    (r'### (?:Description|Accepted Answer|Body)', "content section headings"),
]


# ORCHESTRATOR

def strip_validation_workflow(source_dir: Path) -> None:
    md_files = sorted(source_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {source_dir}", file=sys.stderr)
        sys.exit(1)

    results = measure_corpus(md_files)
    spot = spot_check(source_dir, SPOT_CHECK_FILES)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = REPORT_DIR / f"validation_{ts}.md"
    write_report(report_path, results, spot, len(md_files))
    print(report_path)


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
        line = re.sub(r'!\[Uploading[^\]]*\]\(\)', '', line)
        line = re.sub(MD_IMG_RE, '', line)
        line = re.sub(r'\S{1000,}', '', line)
        out.append(line)
        i += 1
    return "\n".join(out)


def strip_discussion_noise(text: str) -> tuple[str, str]:
    METADATA_PREFIXES = (
        "**Category:**", "**Author:**", "**Created:**", "**Upvotes:**", "**Status:**",
    )
    ANSWER_COMMENT_HDR_RE = re.compile(
        r'^\*\*@\S+\*\* \(\d{4}-\d{2}-\d{2}\) - \d+ upvotes \[ANSWER\]$'
    )
    COMMENT_HDR_RE = re.compile(
        r'^\*\*@\S+\*\* \(\d{4}-\d{2}-\d{2}\) - \d+ upvotes'
    )
    title = ""
    title_extracted = False
    in_answer_comment = False
    out = []
    for line in strip_noise(text).split('\n'):
        if ANSWER_COMMENT_HDR_RE.match(line):
            in_answer_comment = True
            continue
        if in_answer_comment:
            if COMMENT_HDR_RE.match(line) or line.startswith("### "):
                in_answer_comment = False
                out.append(line)
            continue
        if not title_extracted and line.startswith("## "):
            title = line[3:].strip()
            title_extracted = True
            continue
        if any(line.startswith(p) for p in METADATA_PREFIXES):
            continue
        out.append(line)
    return "\n".join(out), title


def max_no_space_run(text: str) -> int:
    tokens = re.findall(r'\S+', text)
    return max((len(t) for t in tokens), default=0)


def measure_corpus(md_files: list) -> list[dict]:
    results = []
    for fp in md_files:
        before = fp.read_text(errors='replace')
        after_text, _ = strip_discussion_noise(before)
        results.append({
            "filename": fp.name,
            "before_max": max_no_space_run(before),
            "after_max": max_no_space_run(after_text),
            "chars_removed": len(before) - len(after_text),
        })
    return results


def spot_check(source_dir: Path, filenames: list[str]) -> list[dict]:
    checks = []
    for fname in filenames:
        fp = source_dir / fname
        if not fp.exists():
            checks.append({"filename": fname, "found": False})
            continue
        before = fp.read_text(errors='replace')
        after_text, _ = strip_discussion_noise(before)
        pattern_counts = []
        for pat, label in SPOT_CHECK_PATTERNS:
            n_before = len(re.findall(pat, before, re.MULTILINE))
            n_after = len(re.findall(pat, after_text, re.MULTILINE))
            pattern_counts.append({
                "label": label,
                "before": n_before,
                "after": n_after,
                "ok": n_after >= n_before,
            })
        sample = [
            l for l in after_text.splitlines()
            if l.strip() and not l.startswith('#') and len(l.strip()) > 60
        ][:3]
        checks.append({
            "filename": fname,
            "found": True,
            "before_max": max_no_space_run(before),
            "after_max": max_no_space_run(after_text),
            "chars_removed": len(before) - len(after_text),
            "patterns": pattern_counts,
            "sample": sample,
        })
    return checks


def write_report(path: Path, results: list[dict], spot: list[dict], total_files: int) -> None:
    before_over = [r for r in results if r["before_max"] > THRESHOLD]
    after_over  = [r for r in results if r["after_max"]  > THRESHOLD]
    corpus_before_peak = max(r["before_max"] for r in results)
    corpus_after_peak  = max(r["after_max"]  for r in results)
    total_removed = sum(r["chars_removed"] for r in results)
    files_changed = sum(1 for r in results if r["chars_removed"] > 0)

    o = [
        f"# Strip Validation Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\nCorpus: {total_files} files · `data/documents/github_discussions/`",
        "\n## Summary\n",
        "| Metric | Before | After |",
        "|---|---|---|",
        f"| Corpus peak no-space run (chars) | {corpus_before_peak:,} | {corpus_after_peak:,} |",
        f"| Files with run > {THRESHOLD} chars | {len(before_over)} | {len(after_over)} |",
        f"| Total chars removed | — | {total_removed:,} |",
        f"| Files changed | — | {files_changed} / {total_files} |",
    ]

    pass_ok = len(after_over) == 0
    status = "✅ PASS" if pass_ok else f"❌ FAIL — {len(after_over)} file(s) still exceed {THRESHOLD} chars"
    o += [
        "\n## Pass Criterion\n",
        f"All {len(before_over)} files with no-space run > {THRESHOLD} chars must drop below threshold: **{status}**",
    ]
    if after_over:
        o.append("\n**Remaining offenders:**")
        for r in sorted(after_over, key=lambda x: -x["after_max"])[:10]:
            o.append(f"- `{r['filename']}`: {r['after_max']:,} chars")

    changed = sorted([r for r in results if r["chars_removed"] > 0], key=lambda x: -x["before_max"])
    o += [
        "\n## Per-File Results (changed files only)\n",
        "| File | Before max (chars) | After max (chars) | Chars removed |",
        "|---|---|---|---|",
    ]
    for r in changed:
        o.append(f"| `{r['filename']}` | {r['before_max']:,} | {r['after_max']:,} | {r['chars_removed']:,} |")

    o.append("\n## Content Preservation Spot-Check\n")
    for c in spot:
        if not c["found"]:
            o.append(f"\n### `{c['filename']}` — FILE NOT FOUND\n")
            continue
        o.append(f"\n### `{c['filename']}`\n")
        o.append(
            f"No-space run: {c['before_max']:,} → {c['after_max']:,} | "
            f"Chars removed: {c['chars_removed']:,}\n"
        )
        o.append("| Pattern | Before | After | Preserved |")
        o.append("|---|---|---|---|")
        for p in c["patterns"]:
            tick = "✅" if p["ok"] else "⚠️"
            o.append(f"| {p['label']} | {p['before']} | {p['after']} | {tick} |")
        if c["sample"]:
            o.append("\nSample lines from after-text (first 3 non-trivial):\n```")
            for line in c["sample"]:
                o.append(line[:120])
            o.append("```")

    path.write_text('\n'.join(o) + '\n')


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Validate strip_discussion_noise() on the MD corpus (read-only)")
    p.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    args = p.parse_args()
    strip_validation_workflow(args.source_dir)
