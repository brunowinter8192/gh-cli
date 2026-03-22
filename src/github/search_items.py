# INFRASTRUCTURE
import logging
import requests
from typing import Literal
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, RESULTS_PER_PAGE, build_headers

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def search_items_workflow(
    query: str,
    type: Literal["issue", "pr"],
    sort_by: Literal["comments", "reactions", "created", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    logger.info("search_items query=%s type=%s", query, type)
    search_query = build_query(query, type)
    raw_response = fetch_items(search_query, sort_by)
    formatted_string = format_item_results(raw_response, type)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Build search query with is:issue or is:pr qualifier
def build_query(query: str, type: str) -> str:
    if type == "issue":
        if "is:pr" in query or "is:pull-request" in query:
            return query
        if "is:issue" not in query:
            return f"{query} is:issue"
        return query
    else:
        if "is:issue" in query:
            return query.replace("is:issue", "is:pr")
        if "is:pr" not in query and "is:pull-request" not in query:
            return f"{query} is:pr"
        return query


# Fetch items from GitHub Search Issues API
def fetch_items(query: str, sort_by: str) -> dict:
    url = f"{GITHUB_API_BASE}/search/issues"
    logger.debug("Fetching from %s", url)
    params = {"q": query, "per_page": RESULTS_PER_PAGE, "order": "desc"}
    if sort_by != "best_match":
        params["sort"] = sort_by
    response = requests.get(url, params=params, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format search results for display
def format_item_results(raw_response: dict, type: str) -> str:
    total = raw_response["total_count"]
    items = raw_response.get("items", [])
    resource_name = "issues" if type == "issue" else "pull requests"

    lines = []
    lines.append(f"Found {total:,} {resource_name} matching your query.\n")

    if not items:
        lines.append("No results to display.")
        return "\n".join(lines)

    lines.append("Top Results:\n")

    for idx, item in enumerate(items, 1):
        repo_url = item["repository_url"]
        repo_name = repo_url.split("/repos/")[1]
        owner, repo = repo_name.split("/")

        state = item["state"].upper()
        if type == "pr" and item.get("pull_request", {}).get("merged_at"):
            state = "MERGED"

        lines.append(f"{idx}. [{state}] {item['title']}")
        lines.append(f"   Repo: {repo_name} | #{item['number']}")
        lines.append(f"   Author: {item['user']['login']} | Comments: {item['comments']}")

        labels = ", ".join(l["name"] for l in item.get("labels", []))
        if labels:
            lines.append(f"   Labels: {labels}")

        lines.append(f"   URL: {item['html_url']}")

        if type == "issue":
            lines.append(f"   [get_issue: owner=\"{owner}\" repo=\"{repo}\" issue_number={item['number']}]")
        else:
            lines.append(f"   [get_pr: owner=\"{owner}\" repo=\"{repo}\" pull_number={item['number']}]")
        lines.append("")

    return "\n".join(lines)
