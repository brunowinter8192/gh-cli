# INFRASTRUCTURE
import logging
from datetime import datetime, timezone

import requests
from mcp.types import TextContent

from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def repo_freshness_workflow(owner: str, repo: str) -> list[TextContent]:
    logger.info("repo_freshness owner=%s repo=%s", owner, repo)
    raw_response = fetch_repo_freshness(owner, repo)
    formatted_string = format_repo_freshness(raw_response)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Fetch repo metadata from GitHub API
def fetch_repo_freshness(owner: str, repo: str) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    logger.debug("Fetching from %s", url)
    response = requests.get(url, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format repo freshness for display
def format_repo_freshness(repo_data: dict) -> str:
    pushed_at = repo_data["pushed_at"]
    pushed_dt = datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
    days_ago = (datetime.now(timezone.utc) - pushed_dt).days

    lines = [
        repo_data["full_name"],
        f"Pushed:  {pushed_at}  (pushed {days_ago} day{'s' if days_ago != 1 else ''} ago)",
        f"Updated: {repo_data['updated_at']}",
        f"Created: {repo_data['created_at']}",
    ]
    return "\n".join(lines)
