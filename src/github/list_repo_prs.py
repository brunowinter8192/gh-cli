# INFRASTRUCTURE
import logging
import requests
from typing import Literal
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, RESULTS_PER_PAGE, build_headers

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def list_repo_prs_workflow(
    owner: str,
    repo: str,
    state: Literal["open", "closed", "all"] = "open",
    sort_by: Literal["created", "updated", "popularity", "long-running"] = "created"
) -> list[TextContent]:
    logger.info("list_repo_prs owner=%s repo=%s", owner, repo)
    raw_response = fetch_repo_prs(owner, repo, state, sort_by)
    formatted_string = format_pr_list(raw_response, owner, repo)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Fetch PRs from repository
def fetch_repo_prs(owner: str, repo: str, state: str, sort_by: str) -> list:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls"
    logger.debug("Fetching from %s", url)
    params = {
        "state": state,
        "sort": sort_by,
        "direction": "desc",
        "per_page": RESULTS_PER_PAGE
    }
    response = requests.get(url, params=params, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format PR list for display
def format_pr_list(prs: list, owner: str, repo: str) -> str:
    lines = []
    lines.append(f"# Pull Requests in {owner}/{repo}")
    lines.append(f"Showing {len(prs)} PRs\n")

    if not prs:
        lines.append("No pull requests found.")
        return "\n".join(lines)

    for idx, pr in enumerate(prs, 1):
        state = pr["state"].upper()
        if pr.get("merged_at"):
            state = "MERGED"

        lines.append(f"{idx}. [{state}] {pr['title']}")
        lines.append(f"   #{pr['number']} | Author: {pr['user']['login']}")
        lines.append(f"   Branch: {pr['head']['ref']} -> {pr['base']['ref']}")
        lines.append(f"   Created: {pr['created_at']}")

        labels = ", ".join(l["name"] for l in pr.get("labels", []))
        if labels:
            lines.append(f"   Labels: {labels}")

        lines.append(f"   URL: {pr['html_url']}")
        lines.append(f"   [get_pr: owner=\"{owner}\" repo=\"{repo}\" pull_number={pr['number']}]")
        lines.append("")

    return "\n".join(lines)
