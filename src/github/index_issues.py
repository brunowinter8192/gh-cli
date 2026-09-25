# INFRASTRUCTURE
import logging
import re
import subprocess
from pathlib import Path

import requests
from mcp.types import TextContent

from src.github.client import GITHUB_API_BASE, build_headers
from src.github.get_issue import get_issue_workflow
from src.github.get_issue_comments import get_issue_comments_workflow
from src.github.text_cleaning import strip_generic_noise, strip_build_logs
from src.github.raw_logging import log_raw_issue
from src.github.config import RAG_ROOT, DEFAULT_LIMIT

logger = logging.getLogger(__name__)

RAG_DOC_DIR = RAG_ROOT / "data" / "documents" / "github_issues"
COLLECTION  = "github_issues"

MIGRATION_REPORT_RE = re.compile(r'^\*\*\[Original report\]\([^)]*\) by .+\.\*\*$')
MIGRATION_COMMENT_RE = re.compile(r'^\*\*Original comment by .+\.\*\*$')
MIGRATION_RULE_RE = re.compile(r'^-{40}$')

AUTOMATED_COMMENT_RE = re.compile(r'^Removing version: .+ \(automated comment\)$')


# ORCHESTRATOR

def index_issues_workflow(query: str, repo: str, limit: int = DEFAULT_LIMIT) -> list[TextContent]:
    logger.info("index_issues query=%s repo=%s limit=%s", query, repo, limit)
    owner, repo_name = repo.split("/", 1)
    repo_basename = repo_name

    keywords = query.split()[:3]
    if not keywords:
        return [TextContent(type="text", text="Empty query — provide 1-3 keywords.")]

    total, numbers, kw_level = search_issues_with_fallback(keywords, repo, limit)
    if total == 0:
        return [TextContent(type="text", text=f"No issues found for '{keywords[0]}' in {repo}.")]

    RAG_DOC_DIR.mkdir(parents=True, exist_ok=True)
    mds_written = write_issue_mds(owner, repo_name, repo_basename, numbers)

    new_chunks = run_index()
    total_mds, total_chunks = get_collection_stats()

    summary = build_index_summary(
        mds_written, repo, query, kw_level, keywords, new_chunks, total_mds, total_chunks
    )
    return [TextContent(type="text", text=summary)]


# FUNCTIONS

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


def search_issues_with_fallback(keywords: list[str], repo: str, limit: int) -> tuple[int, list[int], int]:
    total = 0
    numbers: list[int] = []
    kw_level = 0
    for k in range(len(keywords), 0, -1):
        sub_q = " ".join(keywords[:k])
        total, numbers = search_raw(sub_q, repo, limit)
        if total > 0:
            kw_level = k
            break
    return total, numbers, kw_level


def write_one_issue_md(owner: str, repo_name: str, repo_basename: str, num: int) -> None:
    filename = f"{repo_basename}__{num}.md"
    issue_text = get_issue_workflow(owner, repo_name, num)[0].text
    comments_text = get_issue_comments_workflow(owner, repo_name, num)[0].text
    log_raw_issue(filename, issue_text, comments_text)

    clean, title = strip_noise(issue_text)
    clean = strip_generic_noise(clean)
    clean = strip_build_logs(clean)
    clean_comments = strip_comments_noise(comments_text)
    clean_comments = strip_generic_noise(clean_comments)
    clean_comments = strip_build_logs(clean_comments)
    md = build_issue_md(num, title, clean, clean_comments)
    (RAG_DOC_DIR / filename).write_text(md, encoding="utf-8")


def write_issue_mds(owner: str, repo_name: str, repo_basename: str, numbers: list[int]) -> int:
    mds_written = 0
    for num in numbers:
        write_one_issue_md(owner, repo_name, repo_basename, num)
        mds_written += 1
    return mds_written


def build_index_summary(
    mds_written: int, repo: str, query: str, kw_level: int, keywords: list[str],
    new_chunks: int, total_mds: int, total_chunks: int,
) -> str:
    fallback_note = (
        f" (fell back to {kw_level} keyword{'s' if kw_level != 1 else ''})"
        if kw_level < len(keywords) else ""
    )
    return (
        f"Indexed {mds_written} issues from {repo}.\n"
        f"Query: '{query}'{fallback_note}\n"
        f"New chunks added this run: {new_chunks}\n"
        f"Collection now: {total_mds} MDs, {total_chunks} chunks total."
    )


def strip_noise(text: str) -> tuple[str, str]:
    METADATA_PREFIXES = (
        "Updated:", "Branch:",
        "Commits:", "Changed Files:", "Mergeable:", "URL:", "Comments:",
    )
    CHECKBOX_RE = re.compile(r'^\s*-\s*\[[ xX]\]')

    title = ""
    title_extracted = False
    out = []
    lines = text.splitlines()
    skip_until = -1

    for i, line in enumerate(lines):
        if i <= skip_until:
            continue
        if not title_extracted and line.startswith("# "):
            title = line[2:].strip()
            title_extracted = True
            continue
        if (MIGRATION_REPORT_RE.match(line) and i + 2 < len(lines)
                and lines[i + 1].strip() == '' and MIGRATION_RULE_RE.match(lines[i + 2])):
            skip_until = i + 2
            continue
        if any(line.startswith(p) for p in METADATA_PREFIXES):
            continue
        if line.strip() == "### Preflight Checklist":
            continue
        if CHECKBOX_RE.match(line):
            continue
        out.append(line)

    return "\n".join(out), title


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


def strip_comments_noise(comments_text: str) -> str:
    SEP_RE = re.compile(r'^--- Comment \d+ ---$')
    lines = comments_text.split('\n')
    out = []
    in_bot_block = False
    in_automated_block = False
    skip_until = -1

    for i, line in enumerate(lines):
        if i <= skip_until:
            continue
        if SEP_RE.match(line):
            author_line = ''
            for j in range(i + 1, min(i + 4, len(lines))):
                if lines[j].startswith('Author:'):
                    author_line = lines[j]
                    break
            if '[bot] (' in author_line:
                in_bot_block = True
                in_automated_block = False
            else:
                in_bot_block = False
                end_idx = next(
                    (j for j in range(i + 1, len(lines)) if SEP_RE.match(lines[j])), len(lines)
                )
                in_automated_block = _is_automated_only_comment(lines[i + 1:end_idx])
                if not in_automated_block:
                    out.append(line)
        elif in_bot_block:
            continue
        elif in_automated_block:
            continue
        elif (MIGRATION_COMMENT_RE.match(line) and i + 2 < len(lines)
                and lines[i + 1].strip() == '' and MIGRATION_RULE_RE.match(lines[i + 2])):
            skip_until = i + 2
            continue
        elif line.startswith('> '):
            continue
        else:
            out.append(line)

    return '\n'.join(out)


def build_issue_md(issue_num: int, title: str, issue_text: str, comments_text: str) -> str:
    header = f"# {title}" if title else f"# Issue #{issue_num}"
    return f"{header}\n\n{issue_text}\n\n{comments_text}\n"


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


def parse_chunk_count(stdout: str) -> int:
    if "Nothing to index." in stdout:
        logger.info("rag-cli index: nothing to index, all files unchanged")
        return 0
    m = re.search(r"Done: \d+ files indexed \((\d+) chunks\)", stdout)
    if m is None:
        raise RuntimeError(f"Unrecognised rag-cli index output: {stdout[-300:]}")
    return int(m.group(1))


def get_collection_stats() -> tuple[int, int]:
    md_count = len(list(RAG_DOC_DIR.glob("*.md")))
    rag_cli = Path.home() / ".local" / "bin" / "rag-cli"
    result = subprocess.run(
        [str(rag_cli), "list_collections"],
        capture_output=True, text=True, cwd=str(RAG_ROOT),
    )
    m = re.search(r"github_issues\s*\((\d+) chunks\)", result.stdout)
    if m is None:
        raise RuntimeError(f"Collection github_issues not found in rag-cli list_collections output: {result.stdout[-300:]}")
    return md_count, int(m.group(1))
