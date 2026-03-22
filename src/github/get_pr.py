# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def get_pr_workflow(owner: str, repo: str, pull_number: int) -> list[TextContent]:
    logger.info("get_pr owner=%s repo=%s pull_number=%s", owner, repo, pull_number)
    raw_response = fetch_pr(owner, repo, pull_number)
    formatted_string = format_pr(raw_response, owner, repo)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Fetch single PR from GitHub API
def fetch_pr(owner: str, repo: str, pull_number: int) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls/{pull_number}"
    logger.debug("Fetching from %s", url)
    response = requests.get(url, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format PR for display
def format_pr(pr: dict, owner: str, repo: str) -> str:
    lines = []

    state = pr["state"].upper()
    if pr.get("merged_at"):
        state = "MERGED"

    lines.append(f"# {pr['title']}")
    lines.append(f"State: {state} | #{pr['number']}")
    lines.append(f"Author: {pr['user']['login']}")
    lines.append(f"Branch: {pr['head']['ref']} -> {pr['base']['ref']}")
    lines.append(f"Created: {pr['created_at']} | Updated: {pr['updated_at']}")

    if pr.get("merged_at"):
        lines.append(f"Merged: {pr['merged_at']} by {pr.get('merged_by', {}).get('login', 'unknown')}")

    labels = ", ".join(l["name"] for l in pr.get("labels", []))
    if labels:
        lines.append(f"Labels: {labels}")

    lines.append(f"Commits: {pr.get('commits', 0)} | Additions: +{pr.get('additions', 0)} | Deletions: -{pr.get('deletions', 0)}")
    lines.append(f"Changed Files: {pr.get('changed_files', 0)}")
    lines.append(f"Mergeable: {pr.get('mergeable', 'unknown')}")
    lines.append(f"URL: {pr['html_url']}")

    lines.append(f"\n[get_pr_files: owner=\"{owner}\" repo=\"{repo}\" pull_number={pr['number']}]")

    lines.append("\n---\n")

    body = pr.get("body") or "(No description provided)"
    lines.append(body)

    return "\n".join(lines)
