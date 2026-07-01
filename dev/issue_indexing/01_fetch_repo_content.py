#!/usr/bin/env python3
# Measurement probe: fetch GitHub issues matching a query and render to a single MD file.
# Issues-only (PRs dropped — low signal for closed products with public trackers).
# Self-contained: search logic inlined (token resolution + direct requests); content via cli.py subprocess.
# Applies a noise filter to strip metadata/boilerplate from item sections before writing.
# No RAG indexing — first measurement step only.

# INFRASTRUCTURE
import argparse
import os
import re
import statistics
import subprocess
import sys
import time
from pathlib import Path

import requests

GITHUB_API_BASE = "https://api.github.com"
RESULTS_PER_PAGE = 100  # search API max per call; our natural batch unit

RAG_DOC_DIR = Path("/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/MCP/RAG/data/documents/github_issues")

_ZSHRC_TOKEN_RE = re.compile(
    r'^\s*export\s+GH_TOKEN\s*=\s*["\']?([^"\'\s#]+)["\']?',
    re.MULTILINE,
)
_CLI = Path(__file__).resolve().parents[2] / "cli.py"
_PY = sys.executable


def _read_zshrc_token() -> str:
    path = Path.home() / ".zshrc"
    if not path.is_file():
        return ""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    matches = _ZSHRC_TOKEN_RE.findall(content)
    return matches[-1] if matches else ""


def _resolve_token() -> str:
    return (
        _read_zshrc_token()
        or os.environ.get("GH_TOKEN", "")
        or os.environ.get("GITHUB_TOKEN", "")
    )


GITHUB_TOKEN = _resolve_token()


def build_headers(accept: str = "application/vnd.github+json") -> dict:
    headers = {"Accept": accept, "X-GitHub-Api-Version": "2022-11-28"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


# ORCHESTRATOR

def fetch_repo_content_workflow(query: str, repo: str, top_n: int, out_dir: Path) -> None:
    owner, repo_name = repo.split("/", 1)
    repo_basename = repo_name

    total_issues, issue_numbers = search_raw(query, repo, top_n)

    issue_sections = fetch_issue_sections(owner, repo_name, issue_numbers)

    written = write_issue_files(issue_sections, repo_basename, out_dir)

    print_stats(
        total_issues,
        len(issue_sections),
        [(total, body, cmt) for _, _, total, body, cmt in issue_sections],
        written,
        out_dir,
    )


# FUNCTIONS

# Strip indexing noise from a formatted issue text; return (filtered_text, extracted_title).
# Applied only to the main issue text — comments are left unfiltered.
def strip_noise(text: str) -> tuple[str, str]:
    METADATA_PREFIXES = (
        "Author:", "Created:", "Updated:", "Branch:",
        "Commits:", "Changed Files:", "Mergeable:", "URL:", "Comments:",
    )
    HINT_RE = re.compile(r'^\[get_(?:issue_comments|pr_files):.*\]$')
    CHECKBOX_RE = re.compile(r'^\s*-\s*\[[ xX]\]')

    title = ""
    title_extracted = False
    out = []

    for line in text.splitlines():
        # Extract the standalone title from the first top-level heading in the metadata block
        if not title_extracted and line.startswith("# "):
            title = line[2:].strip()
            title_extracted = True
            continue
        # Strip metadata prefix lines
        if any(line.startswith(p) for p in METADATA_PREFIXES):
            continue
        # Strip tool-hint lines: [get_issue_comments: ...] / [get_pr_files: ...]
        if HINT_RE.match(line):
            continue
        # Strip Preflight Checklist heading
        if line.strip() == "### Preflight Checklist":
            continue
        # Strip task-checkbox lines (template boilerplate)
        if CHECKBOX_RE.match(line):
            continue
        out.append(line)

    return "\n".join(out), title


# Clean comments text: drop bot comments wholesale, strip Author:/Date: metadata, strip quoted-reply lines.
# Comment block format: '--- Comment N ---\nAuthor: X\nDate: Y\n\nbody'. Separator lines are kept for non-bot blocks.
def strip_comments_noise(comments_text: str) -> str:
    SEP_RE = re.compile(r'^--- Comment \d+ ---$')
    lines = comments_text.split('\n')
    out = []
    in_bot_block = False

    for i, line in enumerate(lines):
        if SEP_RE.match(line):
            # Look ahead (up to 3 lines) to find the Author: line for this block
            author_line = ''
            for j in range(i + 1, min(i + 4, len(lines))):
                if lines[j].startswith('Author:'):
                    author_line = lines[j]
                    break
            if author_line.rstrip().endswith('[bot]'):
                in_bot_block = True
                # Drop separator too — entire block is noise
            else:
                in_bot_block = False
                out.append(line)
        elif in_bot_block:
            continue
        elif line.startswith('Author:') or line.startswith('Date:'):
            continue
        elif line.startswith('> '):
            continue
        else:
            out.append(line)

    return '\n'.join(out)


# Search issues via GitHub Search Issues API; return (total_count, numbers[:top_n])
def search_raw(query: str, repo: str, top_n: int) -> tuple[int, list[int]]:
    built_query = f"{query} repo:{repo} is:issue"
    params = {"q": built_query, "per_page": RESULTS_PER_PAGE, "order": "desc"}
    response = requests.get(
        f"{GITHUB_API_BASE}/search/issues",
        params=params,
        headers=build_headers(),
    )
    response.raise_for_status()
    raw = response.json()
    numbers = [item["number"] for item in raw["items"][:top_n]]
    return raw["total_count"], numbers


# Run cli.py subcommand, return stdout text; raises on non-zero exit
def run_cli(*args: str) -> str:
    result = subprocess.run(
        [_PY, str(_CLI)] + list(args),
        capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()


# Fetch full content for issue numbers; return list of (issue_num, md_str, total_bytes, body_bytes, comments_bytes)
def fetch_issue_sections(owner: str, repo: str, numbers: list[int]) -> list[tuple[int, str, int, int, int]]:
    sections = []
    for num in numbers:
        raw_issue = run_cli("get_issue", owner, repo, str(num))
        issue_text, title = strip_noise(raw_issue)
        time.sleep(0.5)
        raw_comments = run_cli("get_issue_comments", owner, repo, str(num))
        comments_text = strip_comments_noise(raw_comments)
        time.sleep(0.5)
        md = build_issue_md(num, title, issue_text, comments_text)
        body_b = len(issue_text.encode("utf-8"))
        comments_b = len(comments_text.encode("utf-8"))
        sections.append((num, md, len(md.encode("utf-8")), body_b, comments_b))
    return sections


# Render one issue as a standalone MD with H1 title (RAG-friendly; mirrors Reddit build_markdown pattern)
def build_issue_md(issue_num: int, title: str, issue_text: str, comments_text: str) -> str:
    header = f"# {title}" if title else f"# Issue #{issue_num}"
    return f"{header}\n\n{issue_text}\n\n{comments_text}\n"


# Write per-issue MDs into out_dir; filename pattern: <repo_basename>__<issue_num>.md
# Returns list of (path, size_bytes) for stats
def write_issue_files(
    sections: list[tuple[int, str, int, int, int]],
    repo_basename: str,
    out_dir: Path,
) -> list[tuple[Path, int]]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for issue_num, md, _, _, _ in sections:
        fname = f"{repo_basename}__{issue_num}.md"
        path = out_dir / fname
        path.write_text(md, encoding="utf-8")
        written.append((path, len(md.encode("utf-8"))))
    return written


# Print fetch + per-issue size stats to stdout
def print_stats(
    total_issues: int,
    fetched_issues: int,
    issue_sizes: list[tuple[int, int, int]],   # (total, body, comments) per issue
    written: list[tuple[Path, int]],            # (path, bytes) per written file
    out_dir: Path,
) -> None:
    def kb(b: int) -> float:
        return b / 1024

    def fmt(b: int) -> str:
        return f"{kb(b):.2f}"

    def size_stats(totals: list[int]) -> str:
        if not totals:
            return "n/a"
        med = statistics.median(totals)
        return (
            f"min={fmt(min(totals))}kb  "
            f"avg={fmt(int(sum(totals) / len(totals)))}kb  "
            f"median={kb(med):.2f}kb  "
            f"max={fmt(max(totals))}kb"
        )

    issue_totals   = [t for t, _, _ in issue_sizes]
    issue_bodies   = [b for _, b, _ in issue_sizes]
    issue_comments = [c for _, _, c in issue_sizes]
    total_written_kb = sum(b for _, b in written) / 1024

    print(f"Issues : {fetched_issues:>3} fetched / {total_issues} total")
    print(f"Files  : {len(written)} MDs written → {out_dir}")
    print(f"Total  : {total_written_kb:.1f} KB across all per-issue MDs")
    print(f"Per-issue size : {size_stats(issue_totals)}")
    print()
    print("--- Bulk breakdown ---")
    print(f"Issue bodies   : {kb(sum(issue_bodies)):>7.1f} KB total  (avg {kb(int(sum(issue_bodies)/max(len(issue_bodies),1))):.1f}kb)")
    print(f"Issue comments : {kb(sum(issue_comments)):>7.1f} KB total  (avg {kb(int(sum(issue_comments)/max(len(issue_comments),1))):.1f}kb)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch GitHub issues matching a query in a repo → per-issue MD files."
    )
    parser.add_argument("--query", default="streaming")
    parser.add_argument("--repo", default="anthropics/claude-code")
    parser.add_argument("--top-n", dest="top_n", type=int, default=100)
    parser.add_argument("--out-dir", dest="out_dir", default=None)
    args = parser.parse_args()

    out_dir = Path(args.out_dir) if args.out_dir else RAG_DOC_DIR

    fetch_repo_content_workflow(args.query, args.repo, args.top_n, out_dir)
