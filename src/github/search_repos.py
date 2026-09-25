# INFRASTRUCTURE
import logging
import requests
from typing import Literal
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers
from src.github.repo_counts import fetch_repo_counts, format_count_line
from src.github.query_common import (
    extract_keywords, search_with_keyword_fallback,
    build_empty_query_message, build_no_hits_message, build_fallback_note,
)
from src.github.response import text_response

logger = logging.getLogger(__name__)

SEARCH_REPOS_PER_PAGE = 30


# ORCHESTRATOR

def search_repos_workflow(
    query: str,
    sort_by: Literal["stars", "forks", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    logger.info("search_repos query=%s sort_by=%s", query, sort_by)
    keywords = extract_keywords(query)
    if not keywords:
        return text_response(build_empty_query_message())
    total, raw_response, kw_level = search_repositories_with_fallback(keywords, sort_by)
    if total == 0:
        return text_response(build_no_hits_message("repositories", keywords[0]))
    items = raw_response["items"]
    counts = fetch_repo_counts(collect_repo_names(items))
    return text_response(format_repo_results(items, counts, kw_level, keywords))


# FUNCTIONS

def search_repositories_with_fallback(keywords: list[str], sort_by: str) -> tuple[int, dict, int]:
    def search(sub_query):
        raw_response = fetch_repositories(sub_query, sort_by)
        return raw_response["total_count"], raw_response
    return search_with_keyword_fallback(keywords, search)


def fetch_repositories(query: str, sort_by: str) -> dict:
    url = f"{GITHUB_API_BASE}/search/repositories"
    logger.debug("Fetching from %s", url)
    params = {"q": query, "per_page": SEARCH_REPOS_PER_PAGE, "order": "desc"}
    if sort_by != "best_match":
        params["sort"] = sort_by
    response = requests.get(url, params=params, headers=build_headers())
    response.raise_for_status()
    return response.json()


def collect_repo_names(items: list) -> list[tuple[str, str]]:
    return [tuple(r["full_name"].split("/", 1)) for r in items]


def format_repo_results(items: list, counts: dict, kw_level: int, keywords: list[str]) -> str:
    lines = []
    fallback_note = build_fallback_note(kw_level, keywords)
    if fallback_note:
        lines.append(f"Query: '{' '.join(keywords[:kw_level])}'{fallback_note}")
    for repo in items:
        full_name = repo["full_name"]
        stars = repo["stargazers_count"]
        lines.append(format_count_line(full_name, stars, counts[full_name]))
    return "\n".join(lines)
