# INFRASTRUCTURE
import logging
import requests
from typing import Literal
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers
from src.github.repo_counts import fetch_repo_counts, format_count_line

logger = logging.getLogger(__name__)

SEARCH_REPOS_PER_PAGE = 30


# ORCHESTRATOR

def search_repos_workflow(
    query: str,
    sort_by: Literal["stars", "forks", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    logger.info("search_repos query=%s sort_by=%s", query, sort_by)
    keywords = query.split()[:3]
    if not keywords:
        return [TextContent(type="text", text="Empty query — provide 1-3 keywords.")]
    raw_response = None
    for k in range(len(keywords), 0, -1):
        sub_q = " ".join(keywords[:k])
        raw_response = fetch_repositories(sub_q, sort_by)
        if raw_response["total_count"] > 0:
            break
    if raw_response["total_count"] == 0:
        return [TextContent(type="text", text=f"No repositories found for '{keywords[0]}'.")]
    items = raw_response.get("items", [])
    repos = [tuple(r["full_name"].split("/", 1)) for r in items]
    counts = fetch_repo_counts(repos)
    return [TextContent(type="text", text=format_repo_results(items, counts))]


# FUNCTIONS

# Fetch repositories from GitHub Search API
def fetch_repositories(query: str, sort_by: str) -> dict:
    url = f"{GITHUB_API_BASE}/search/repositories"
    logger.debug("Fetching from %s", url)
    params = {"q": query, "per_page": SEARCH_REPOS_PER_PAGE, "order": "desc"}
    if sort_by != "best_match":
        params["sort"] = sort_by
    response = requests.get(url, params=params, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Emit one line per repo: full_name · ⭐stars · issues:N · discussions:M
def format_repo_results(items: list, counts: dict) -> str:
    lines = []
    for repo in items:
        full_name = repo["full_name"]
        stars = repo["stargazers_count"]
        lines.append(format_count_line(full_name, stars, counts.get(full_name)))
    return "\n".join(lines)
