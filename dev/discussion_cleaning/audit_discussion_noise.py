#!/usr/bin/env python3
# Audit noise classes in GitHub discussion MDs. Read-only — never modifies source files.
# Usage: python3 dev/discussion_cleaning/audit_discussion_noise.py [--source-dir PATH]

# INFRASTRUCTURE

import argparse, re, sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple

DEFAULT_SOURCE_DIR = Path(
    "/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli/"
    "data/documents/github_discussions"
)
REPORT_DIR = Path(__file__).parent / "audit_reports"
FOOTER_LOOKAHEAD = 20
SAMPLE_N = 5
CONTEXT_N = 2


@dataclass
class Hit:
    filename: str
    start_line: int
    end_line: int
    text: str
    before: str = ""
    after: str = ""
    content_risk: bool = False
    notes: str = ""


@dataclass
class Class:
    name: str
    detection: str
    verdict: str
    files: int = 0
    hits: int = 0
    chars: int = 0
    alnum: int = 0
    prose_alnum: int = 0
    risk_hits: int = 0
    all_hits: List[Hit] = field(default_factory=list)


# ORCHESTRATOR

def audit_discussion_noise_workflow(source_dir: Path) -> None:
    md_files = sorted(source_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {source_dir}", file=sys.stderr)
        sys.exit(1)
    classes = [
        audit_dosu_footer(md_files),
        audit_dosu_greeting(md_files),
        _audit_token_class(md_files, Class(
            name="DOSU_ANSWER_MARKER",
            detection="<!-- Answer --> HTML comment token — strip tag only, not surrounding text.",
            verdict="SAFE TO STRIP",
        ), re.compile(r'<!--\s*Answer\s*-->')),
        audit_gh_screenshot_img(md_files),
        _audit_token_class(md_files, Class(
            name="FAILED_UPLOAD",
            detection=r"![Uploading <filename>…]() — empty URL, image never uploaded.",
            verdict="SAFE TO STRIP",
        ), re.compile(r'!\[Uploading[^\]]*\]\(\)')),
        audit_issue_template(md_files),
    ]
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / f"audit_{datetime.now().strftime('%Y%m%d')}.md"
    write_report(report_path, classes, len(md_files))
    print(report_path)


# FUNCTIONS

def _strip_bq(line: str) -> str:
    return re.sub(r'^[\s>]+', '', line).strip()

def _is_badge_line(line: str) -> bool:
    c = _strip_bq(line)
    has_badge = '[![' in c or c.startswith('<sup>How did I do?')
    has_dosu = any(x in c for x in [
        'shields.io/badge', 'camo.githubusercontent.com',
        'app.dosu.dev/response-feedback', 'go.dosu.dev',
    ])
    return has_badge and has_dosu

def _impact(text: str) -> Tuple[int, int, int]:
    alnum = sum(c.isalnum() for c in text)
    s = re.sub(r'https?://\S+', '', text)
    s = re.sub(r'data%3A\S*', '', s)
    s = re.sub(r'(%[0-9A-Fa-f]{2})+\S*', '', s)
    return len(text), alnum, sum(c.isalnum() for c in s)

def _ctx(lines: list, start: int, end: int) -> Tuple[str, str]:
    before = ''.join(lines[max(0, start - CONTEXT_N):start]).rstrip()
    after = ''.join(lines[end + 1:min(len(lines), end + 1 + CONTEXT_N)]).lstrip()
    return before, after

def _add_hit(cls: Class, h: Hit, tc: int, al: int, pr: int, risk: bool = False) -> None:
    cls.all_hits.append(h)
    cls.hits += 1
    cls.chars += tc
    cls.alnum += al
    cls.prose_alnum += pr
    if risk:
        cls.risk_hits += 1


# Detect dosu footer block: <!-- Dosu Comment Footer --> through badge line (HARD INVARIANT: no > **@ in range)
def audit_dosu_footer(md_files: list) -> Class:
    cls = Class(
        name="DOSU_FOOTER",
        detection=(
            "<!-- Dosu Comment Footer --> … badge line (shields.io/camo [![…](…)](…) or <sup>How did I do?</sup>). "
            "HARD INVARIANT: matched range must contain no threaded-reply (> **@) line."
        ),
        verdict="SAFE TO STRIP",
    )
    files_hit: set = set()
    for fp in md_files:
        lines = fp.read_text(errors='replace').splitlines(keepends=True)
        i = 0
        while i < len(lines):
            if _strip_bq(lines[i]) == '<!-- Dosu Comment Footer -->':
                badge_idx: Optional[int] = next(
                    (j for j in range(i + 1, min(i + FOOTER_LOOKAHEAD, len(lines)))
                     if _is_badge_line(lines[j])), None
                )
                if badge_idx is not None:
                    block = lines[i:badge_idx + 1]
                    text = ''.join(block)
                    threaded = [l for l in block if re.search(r'^\s*>\s*\*\*@', l)]
                    risk = len(threaded) > 0
                    tc, al, pr = _impact(text)
                    before, after = _ctx(lines, i, badge_idx)
                    _add_hit(cls, Hit(
                        filename=fp.name, start_line=i + 1, end_line=badge_idx + 1,
                        text=text, before=before, after=after, content_risk=risk,
                        notes=(
                            "INVARIANT BREACH — threaded replies in range: "
                            + repr([l.rstrip()[:80] for l in threaded])
                        ) if risk else "",
                    ), tc, al, pr, risk)
                    files_hit.add(fp.name)
                    i = badge_idx + 1
                    continue
            i += 1
    cls.files = len(files_hit)
    return cls


# Detect dosu greeting: <!-- Greeting --> + next non-blank line (2-line boundary, no overrun)
def audit_dosu_greeting(md_files: list) -> Class:
    cls = Class(
        name="DOSU_GREETING",
        detection="<!-- Greeting --> + next non-blank line. Boundary: exactly 2 lines (marker + greeting text).",
        verdict="SAFE TO STRIP",
    )
    files_hit: set = set()
    for fp in md_files:
        lines = fp.read_text(errors='replace').splitlines(keepends=True)
        for i, line in enumerate(lines):
            if _strip_bq(line) == '<!-- Greeting -->':
                greet_idx = next(
                    (j for j in range(i + 1, min(i + 5, len(lines))) if lines[j].strip()), None
                )
                if greet_idx is None:
                    continue
                greet_text = lines[greet_idx].strip()
                is_template = any(x in greet_text for x in ["I'm", "I am", "Dosu"])
                text = lines[i] + lines[greet_idx]
                tc, al, pr = _impact(text)
                before, after = _ctx(lines, i, greet_idx)
                _add_hit(cls, Hit(
                    filename=fp.name, start_line=i + 1, end_line=greet_idx + 1,
                    text=text, before=before, after=after,
                    content_risk=not is_template,
                    notes="" if is_template else f"Unexpected greeting: {greet_text[:80]}",
                ), tc, al, pr, not is_template)
                files_hit.add(fp.name)
    cls.files = len(files_hit)
    return cls


# Generic single-token regex class detector (for DOSU_ANSWER_MARKER and FAILED_UPLOAD)
def _audit_token_class(md_files: list, cls: Class, pat: re.Pattern) -> Class:
    files_hit: set = set()
    for fp in md_files:
        text = fp.read_text(errors='replace')
        hits = list(pat.finditer(text))
        if not hits:
            continue
        lines = text.splitlines(keepends=True)
        for h in hits:
            tc, al, pr = _impact(h.group())
            lineno = text[:h.start()].count('\n')
            before, after = _ctx(lines, lineno, lineno)
            if len(cls.all_hits) < SAMPLE_N * 3:
                cls.all_hits.append(Hit(
                    filename=fp.name, start_line=lineno + 1, end_line=lineno + 1,
                    text=h.group(), before=before, after=after,
                ))
            cls.hits += 1; cls.chars += tc; cls.alnum += al; cls.prose_alnum += pr
        files_hit.add(fp.name)
    cls.files = len(files_hit)
    return cls


# Detect user-uploaded screenshot img tags — ALL hits shown for alt-text classification
def audit_gh_screenshot_img(md_files: list) -> Class:
    cls = Class(
        name="GH_SCREENSHOT_IMG",
        detection=(
            '<img width="N" height="M" alt="…" src="https://github.com/user-attachments/assets/UUID"> '
            "— all hits shown for alt-text content-risk classification."
        ),
        verdict="NEEDS-DECISION",
    )
    pat = re.compile(
        r'<img\s+width="\d+"\s+height="\d+"\s+alt="([^"]*?)"\s+'
        r'src="https://github\.com/user-attachments/assets/[a-f0-9-]+"[^>]*/?>',
        re.IGNORECASE,
    )
    files_hit: set = set()
    for fp in md_files:
        text = fp.read_text(errors='replace')
        hits = list(pat.finditer(text))
        if not hits:
            continue
        lines = text.splitlines(keepends=True)
        for h in hits:
            alt = h.group(1)
            tc, al, pr = _impact(h.group())
            lineno = text[:h.start()].count('\n')
            before, after = _ctx(lines, lineno, lineno)
            _add_hit(cls, Hit(
                filename=fp.name, start_line=lineno + 1, end_line=lineno + 1,
                text=h.group()[:120] + ("…" if len(h.group()) > 120 else ""),
                before=before, after=after, notes=f'alt="{alt}"',
            ), tc, al, pr)
        files_hit.add(fp.name)
    cls.files = len(files_hit)
    return cls


# Detect MinerU issue-template boilerplate sections
def audit_issue_template(md_files: list) -> Class:
    cls = Class(
        name="ISSUE_TEMPLATE_CHECKLIST",
        detection=(
            "### 🔎 Search before asking … and ### 🤖 Consult the online AI assistant … "
            "headings + their - [x] checkbox lines. Boundary: heading + checkboxes only."
        ),
        verdict="SAFE TO STRIP",
    )
    heading_pat = re.compile(r'^### (?:🔎 Search before asking|🤖 Consult the online AI assistant)')
    files_hit: set = set()
    for fp in md_files:
        lines = fp.read_text(errors='replace').splitlines(keepends=True)
        i = 0
        while i < len(lines):
            if heading_pat.match(lines[i].strip()):
                start = i
                j = i + 1
                while j < len(lines) and (lines[j].strip().startswith('- [') or not lines[j].strip()):
                    j += 1
                end = j - 1
                while end > start and not lines[end].strip():
                    end -= 1
                text = ''.join(lines[start:end + 1])
                non_tmpl = [
                    l.rstrip() for l in lines[start:end + 1]
                    if l.strip() and not l.strip().startswith('###') and not l.strip().startswith('- [')
                ]
                risk = len(non_tmpl) > 0
                tc, al, pr = _impact(text)
                before, after = _ctx(lines, start, end)
                _add_hit(cls, Hit(
                    filename=fp.name, start_line=start + 1, end_line=end + 1,
                    text=text, before=before, after=after, content_risk=risk,
                    notes=f"non-template lines: {non_tmpl}" if risk else "",
                ), tc, al, pr, risk)
                files_hit.add(fp.name)
                i = end + 1
            else:
                i += 1
    cls.files = len(files_hit)
    return cls


# Format a single hit as a list of markdown lines
def _fmt_hit(h: Hit, idx: int, max_text: int = 400) -> List[str]:
    o = [f"\n**Hit {idx} — `{h.filename}` L{h.start_line}–{h.end_line}**"]
    if h.content_risk:
        o.append(f"\n⚠️ CONTENT_RISK — {h.notes}")
    elif h.notes:
        o.append(f"\n*{h.notes}*")
    if h.before:
        o.append(f"\n```\n… (before)\n{h.before}\n```")
    trunc = h.text if len(h.text) <= max_text else h.text[:max_text] + f"\n… [{len(h.text)} chars total]"
    o.append(f"\n```\n[MATCH]\n{trunc}[/MATCH]\n```")
    if h.after:
        o.append(f"\n```\n{h.after}\n… (after)\n```")
    return o


# Write the audit report MD
def write_report(path: Path, classes: list, total_files: int) -> None:
    o: List[str] = [
        f"# Discussion Noise Audit — {datetime.now().strftime('%Y-%m-%d')}",
        f"\nCorpus: {total_files} files · `data/documents/github_discussions/`",
        "\n## Summary\n",
        "| Class | Files | Hits | Chars | Alnum | Prose Alnum | Risk Hits | Verdict |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for cls in classes:
        o.append(
            f"| {cls.name} | {cls.files} | {cls.hits} | {cls.chars:,} | "
            f"{cls.alnum:,} | {cls.prose_alnum:,} | {cls.risk_hits} | {cls.verdict} |"
        )
    for cls in classes:
        o += [f"\n---\n\n## {cls.name}\n",
              f"**Detection:** {cls.detection}\n",
              f"**Verdict: {cls.verdict}**\n",
              f"- Files hit: {cls.files} / {total_files}",
              f"- Total hits: {cls.hits}",
              f"- Chars matched: {cls.chars:,}",
              f"- Alnum in match: {cls.alnum:,}",
              f"- Prose alnum (excl. URLs/base64): {cls.prose_alnum:,}"]
        if cls.risk_hits:
            o.append(f"- **⚠️ CONTENT_RISK hits: {cls.risk_hits}** — details in samples")
        show = cls.all_hits if cls.name == "GH_SCREENSHOT_IMG" else cls.all_hits[:SAMPLE_N]
        if show:
            label = f"all {len(show)}" if cls.name == "GH_SCREENSHOT_IMG" else f"{len(show)} of {cls.hits}"
            o.append(f"\n### Samples ({label} hits)\n")
            for idx, h in enumerate(show, 1):
                o.extend(_fmt_hit(h, idx))
    path.write_text('\n'.join(o) + '\n')


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Audit noise classes in discussion MDs (read-only)")
    p.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    args = p.parse_args()
    audit_discussion_noise_workflow(args.source_dir)
