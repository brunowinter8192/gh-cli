# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
# From client.py: base API URL and header builder with auth token
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)

COMMENTS_PER_PAGE = 30


# ORCHESTRATOR
def get_issue_comments_workflow(owner: str, repo: str, issue_number: int) -> list[TextContent]:
    logger.info("get_issue_comments owner=%s repo=%s issue_number=%s", owner, repo, issue_number)
    raw_response = fetch_comments(owner, repo, issue_number)
    formatted_string = format_comments(raw_response, owner, repo, issue_number)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Fetch comments from GitHub API
def fetch_comments(owner: str, repo: str, issue_number: int) -> list:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues/{issue_number}/comments"
    logger.debug("Fetching from %s", url)
    params = {"per_page": COMMENTS_PER_PAGE}
    response = requests.get(url, params=params, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format comments for display
def format_comments(comments: list, owner: str, repo: str, issue_number: int) -> str:
    lines = []

    lines.append(f"# Comments on {owner}/{repo}#{issue_number}")
    lines.append(f"Total: {len(comments)} comments\n")

    if not comments:
        lines.append("No comments on this issue.")
        return "\n".join(lines)

    for idx, comment in enumerate(comments, 1):
        lines.append(f"--- Comment {idx} ---")
        lines.append(f"Author: {comment['user']['login']}")
        lines.append(f"Date: {comment['created_at']}")
        lines.append("")
        lines.append(comment.get("body") or "(Empty comment)")
        lines.append("")

    return "\n".join(lines)
