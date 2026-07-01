# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
# From client.py: base API URL and header builder with auth token
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def get_issue_workflow(owner: str, repo: str, issue_number: int) -> list[TextContent]:
    logger.info("get_issue owner=%s repo=%s issue_number=%s", owner, repo, issue_number)
    raw_response = fetch_issue(owner, repo, issue_number)
    formatted_string = format_issue(raw_response, owner, repo)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Fetch single issue from GitHub API
def fetch_issue(owner: str, repo: str, issue_number: int) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues/{issue_number}"
    logger.debug("Fetching from %s", url)
    response = requests.get(url, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format issue for display
def format_issue(issue: dict, owner: str, repo: str) -> str:
    lines = []

    lines.append(f"# {issue['title']}")
    lines.append(f"State: {issue['state'].upper()} | #{issue['number']}")
    lines.append(f"Author: {issue['user']['login']}")
    lines.append(f"Created: {issue['created_at']} | Updated: {issue['updated_at']}")

    labels = ", ".join(l["name"] for l in issue.get("labels", []))
    if labels:
        lines.append(f"Labels: {labels}")

    lines.append(f"Comments: {issue['comments']}")
    lines.append(f"URL: {issue['html_url']}")

    lines.append("\n---\n")

    body = issue.get("body") or "(No description provided)"
    lines.append(body)

    return "\n".join(lines)
