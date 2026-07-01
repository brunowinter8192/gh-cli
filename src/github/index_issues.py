# INFRASTRUCTURE
import logging
import re
import subprocess
from pathlib import Path

import requests
from mcp.types import TextContent

# From client.py: base API URL and header builder with auth token
from src.github.client import GITHUB_API_BASE, build_headers
# From get_issue.py: fetch and format a single GitHub issue
from src.github.get_issue import get_issue_workflow
# From get_issue_comments.py: fetch and format comments for a single issue
from src.github.get_issue_comments import get_issue_comments_workflow
# From text_cleaning.py: generic image/data-URI/no-space strips (additive, after issue-specific strips)
from src.github.text_cleaning import strip_generic_noise

logger = logging.getLogger(__name__)

RAG_ROOT    = Path("/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli")
RAG_DOC_DIR = RAG_ROOT / "data" / "documents" / "github_issues"
COLLECTION  = "github_issues"
DEFAULT_LIMIT = 30


# ORCHESTRATOR

# Fetch GitHub issues matching query + repo, write per-issue MDs, index into RAG
def index_issues_workflow(query: str, repo: str, limit: int = DEFAULT_LIMIT) -> list[TextContent]:
    logger.info("index_issues query=%s repo=%s limit=%s", query, repo, limit)
    owner, repo_name = repo.split("/", 1)
    repo_basename = repo_name

    keywords = query.split()[:3]
    if not keywords:
        return [TextContent(type="text", text="Empty query — provide 1-3 keywords.")]
    total = 0
    numbers: list[int] = []
    kw_level = 0
    for k in range(len(keywords), 0, -1):
        sub_q = " ".join(keywords[:k])
        total, numbers = search_raw(sub_q, repo, limit)
        if total > 0:
            kw_level = k
            break
    if total == 0:
        return [TextContent(type="text", text=f"No issues found for '{keywords[0]}' in {repo}.")]

    RAG_DOC_DIR.mkdir(parents=True, exist_ok=True)
    mds_written = 0
    for num in numbers:
        issue_text = get_issue_workflow(owner, repo_name, num)[0].text
        clean, title = strip_noise(issue_text)
        clean = strip_generic_noise(clean)
        comments_text = get_issue_comments_workflow(owner, repo_name, num)[0].text
        clean_comments = strip_comments_noise(comments_text)
        clean_comments = strip_generic_noise(clean_comments)
        md = build_issue_md(num, title, clean, clean_comments)
        (RAG_DOC_DIR / f"{repo_basename}__{num}.md").write_text(md, encoding="utf-8")
        mds_written += 1

    new_chunks = run_index()
    total_mds, total_chunks = get_collection_stats()

    fallback_note = (
        f" (fell back to {kw_level} keyword{'s' if kw_level != 1 else ''})"
        if kw_level < len(keywords) else ""
    )
    summary = (
        f"Indexed {mds_written} issues from {repo}.\n"
        f"Query: '{query}'{fallback_note}\n"
        f"New chunks added this run: {new_chunks}\n"
        f"Collection now: {total_mds} MDs, {total_chunks} chunks total."
    )
    return [TextContent(type="text", text=summary)]


# FUNCTIONS

# Search issues via GitHub Search Issues API; return (total_count, numbers[:limit])
def search_raw(query: str, repo: str, limit: int) -> tuple[int, list[int]]:
    built_query = f"{query} repo:{repo} is:issue"
    params = {"q": built_query, "per_page": min(limit, 100), "order": "desc"}
    response = requests.get(
        f"{GITHUB_API_BASE}/search/issues",
        params=params,
        headers=build_headers(),
    )
    response.raise_for_status()
    raw = response.json()
    numbers = [item["number"] for item in raw["items"][:limit]]
    return raw["total_count"], numbers


# Strip indexing noise from a formatted issue text; return (filtered_text, extracted_title)
def strip_noise(text: str) -> tuple[str, str]:
    METADATA_PREFIXES = (
        "Author:", "Created:", "Updated:", "Branch:",
        "Commits:", "Changed Files:", "Mergeable:", "URL:", "Comments:",
    )
    CHECKBOX_RE = re.compile(r'^\s*-\s*\[[ xX]\]')

    title = ""
    title_extracted = False
    out = []

    for line in text.splitlines():
        if not title_extracted and line.startswith("# "):
            title = line[2:].strip()
            title_extracted = True
            continue
        if any(line.startswith(p) for p in METADATA_PREFIXES):
            continue
        if line.strip() == "### Preflight Checklist":
            continue
        if CHECKBOX_RE.match(line):
            continue
        out.append(line)

    return "\n".join(out), title


# Clean comments text: drop bot comments, strip Author/Date metadata, strip quoted-reply lines
def strip_comments_noise(comments_text: str) -> str:
    SEP_RE = re.compile(r'^--- Comment \d+ ---$')
    lines = comments_text.split('\n')
    out = []
    in_bot_block = False

    for i, line in enumerate(lines):
        if SEP_RE.match(line):
            author_line = ''
            for j in range(i + 1, min(i + 4, len(lines))):
                if lines[j].startswith('Author:'):
                    author_line = lines[j]
                    break
            if author_line.rstrip().endswith('[bot]'):
                in_bot_block = True
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


# Render one issue as a standalone MD with H1 title
def build_issue_md(issue_num: int, title: str, issue_text: str, comments_text: str) -> str:
    header = f"# {title}" if title else f"# Issue #{issue_num}"
    return f"{header}\n\n{issue_text}\n\n{comments_text}\n"


# Run rag-cli index (incremental); return new chunk count from stdout
def run_index() -> int:
    rag_cli = Path.home() / ".local" / "bin" / "rag-cli"
    result = subprocess.run(
        [str(rag_cli), "index", "--collection", COLLECTION],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        busy = any(w in stderr.lower() for w in ("busy", "locked", "in use"))
        reason = "RAG server busy or DB locked" if busy else f"rag-cli index failed (exit {result.returncode})"
        raise RuntimeError(
            f"{reason} — MDs are staged, run manually when server is free: "
            f"rag-cli index --collection {COLLECTION}\nDetails: {stderr[:300]}"
        )
    return parse_chunk_count(result.stdout)


# Parse new chunk count from rag-cli index stdout
def parse_chunk_count(stdout: str) -> int:
    m = re.search(r"Done: \d+ files indexed \((\d+) chunks\)", stdout)
    return int(m.group(1)) if m else 0


# Return (md_count, total_chunks) for github_issues collection
def get_collection_stats() -> tuple[int, int]:
    md_count = len(list(RAG_DOC_DIR.glob("*.md")))
    rag_cli = Path.home() / ".local" / "bin" / "rag-cli"
    try:
        result = subprocess.run(
            [str(rag_cli), "list_collections"],
            capture_output=True, text=True, cwd=str(RAG_ROOT),
        )
        m = re.search(r"github_issues\s*\((\d+) chunks\)", result.stdout)
        total_chunks = int(m.group(1)) if m else 0
    except Exception as exc:
        logger.warning("index_issues: rag-cli list_collections failed: %s", exc)
        total_chunks = 0
    return md_count, total_chunks
