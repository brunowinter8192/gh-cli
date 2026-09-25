# INFRASTRUCTURE
import logging
import re

from mcp.types import TextContent

from src.github.discussion_cleaning import strip_noise
from src.github.graphql_client import graphql_query
from src.github.get_discussion import get_discussion_workflow
from src.github.config import RAG_ROOT, DEFAULT_LIMIT
from src.github.query_common import (
    split_repo, extract_keywords, search_with_keyword_fallback,
    build_empty_query_message, build_no_hits_message,
)
from src.github.response import text_response
from src.github.rag_indexing import run_index, get_collection_stats, build_index_summary

logger = logging.getLogger(__name__)

RAG_DOC_DIR = RAG_ROOT / "data" / "documents" / "github_discussions"
COLLECTION  = "github_discussions"

SEARCH_QUERY = """
query($query: String!, $first: Int!) {
  search(query: $query, type: DISCUSSION, first: $first) {
    discussionCount
    nodes {
      ... on Discussion {
        number
      }
    }
  }
}
"""

METADATA_PREFIXES = (
    "**Category:**", "**Author:**", "**Created:**", "**Upvotes:**", "**Status:**",
)
ANSWER_COMMENT_HDR_RE = re.compile(
    r'^\*\*@\S+\*\* \(\d{4}-\d{2}-\d{2}\) - \d+ upvotes \[ANSWER\]$'
)
COMMENT_HDR_RE = re.compile(
    r'^\*\*@\S+\*\* \(\d{4}-\d{2}-\d{2}\) - \d+ upvotes'
)


# ORCHESTRATOR

def index_discussions_workflow(query: str, repo: str, limit: int = DEFAULT_LIMIT) -> list[TextContent]:
    logger.info("index_discussions query=%s repo=%s limit=%s", query, repo, limit)
    owner, repo_name = split_repo(repo)
    keywords = extract_keywords(query)
    if not keywords:
        return text_response(build_empty_query_message())

    total, numbers, kw_level = search_discussions_with_fallback(keywords, repo, limit)
    if total == 0:
        return text_response(build_no_hits_message("discussions", keywords[0], repo))

    mds_written = write_discussion_mds(owner, repo_name, numbers)

    new_chunks = run_index(COLLECTION)
    total_mds, total_chunks = get_collection_stats(COLLECTION, RAG_DOC_DIR)

    summary = build_index_summary(
        "discussions", mds_written, repo, query, kw_level, keywords, new_chunks, total_mds, total_chunks
    )
    return text_response(summary)


# FUNCTIONS

def search_discussions_with_fallback(keywords: list[str], repo: str, limit: int) -> tuple[int, list[int], int]:
    return search_with_keyword_fallback(keywords, lambda sub_query: search_discussions_raw(sub_query, repo, limit))


def search_discussions_raw(query: str, repo: str, limit: int) -> tuple[int, list[int]]:
    scoped_query = f"{query} repo:{repo}"
    variables = {"query": scoped_query, "first": min(limit, 100)}
    data = graphql_query(SEARCH_QUERY, variables)
    search = data["search"]
    numbers = [n["number"] for n in search["nodes"] if n is not None][:limit]
    return search["discussionCount"], numbers


def write_discussion_mds(owner: str, repo_name: str, numbers: list[int]) -> int:
    RAG_DOC_DIR.mkdir(parents=True, exist_ok=True)
    mds_written = 0
    for num in numbers:
        write_one_discussion_md(owner, repo_name, num)
        mds_written += 1
    return mds_written


def write_one_discussion_md(owner: str, repo_name: str, num: int) -> None:
    disc_text = get_discussion_workflow(owner, repo_name, num)[0].text
    clean, title = strip_discussion_noise(disc_text)
    md = build_discussion_md(num, title, clean)
    md = redact_tokens(md)
    (RAG_DOC_DIR / f"{repo_name}__{num}.md").write_text(md, encoding="utf-8")


def strip_discussion_noise(text: str) -> tuple[str, str]:
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


def build_discussion_md(disc_num: int, title: str, body_text: str) -> str:
    header = f"# {title}" if title else f"# Discussion #{disc_num}"
    return f"{header}\n\n{body_text}\n"


def redact_tokens(text: str) -> str:
    text = re.sub(r'ghp_[A-Za-z0-9]+', '[REDACTED]', text)
    text = re.sub(r'github_pat_[A-Za-z0-9_]+', '[REDACTED]', text)
    return text
