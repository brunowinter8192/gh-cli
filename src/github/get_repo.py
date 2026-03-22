# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def get_repo_workflow(owner: str, repo: str) -> list[TextContent]:
    logger.info("get_repo owner=%s repo=%s", owner, repo)
    raw_data = fetch_repo(owner, repo)
    formatted = format_repo(raw_data)
    return [TextContent(type="text", text=formatted)]


# FUNCTIONS

# Fetch repository metadata from GitHub API
def fetch_repo(owner: str, repo: str) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    logger.debug("Fetching from %s", url)
    response = requests.get(url, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format repository metadata for display
def format_repo(data: dict) -> str:
    full_name = data.get("full_name", "")
    stars = data.get("stargazers_count", 0)
    description = data.get("description") or "No description"
    language = data.get("language") or "Unknown"
    topics = data.get("topics") or []
    license_info = data.get("license") or {}
    license_name = license_info.get("name", "None")
    updated = data.get("updated_at", "")[:10]
    open_issues = data.get("open_issues_count", 0)
    default_branch = data.get("default_branch", "main")
    url = data.get("html_url", "")

    topics_str = ", ".join(topics) if topics else "None"

    lines = [
        f"**{full_name}** ({stars:,} stars)",
        f"- Description: {description}",
        f"- Language: {language}",
        f"- Topics: {topics_str}",
        f"- License: {license_name}",
        f"- Updated: {updated}",
        f"- Open Issues: {open_issues}",
        f"- Default Branch: {default_branch}",
        f"- URL: {url}"
    ]

    return "\n".join(lines)
