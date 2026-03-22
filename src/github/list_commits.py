# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, RESULTS_PER_PAGE, build_headers

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def list_commits_workflow(
    owner: str,
    repo: str,
    sha: str = "",
    path: str = "",
    author: str = "",
    per_page: int = RESULTS_PER_PAGE
) -> list[TextContent]:
    logger.info("list_commits owner=%s repo=%s", owner, repo)
    raw_data = fetch_commits(owner, repo, sha, path, author, per_page)
    formatted = format_commits(raw_data, owner, repo)
    return [TextContent(type="text", text=formatted)]


# FUNCTIONS

# Fetch commits from repository
def fetch_commits(owner: str, repo: str, sha: str, path: str, author: str, per_page: int) -> list:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/commits"
    logger.debug("Fetching from %s", url)
    params = {"per_page": per_page}
    if sha:
        params["sha"] = sha
    if path:
        params["path"] = path
    if author:
        params["author"] = author
    response = requests.get(url, params=params, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format commit list for display
def format_commits(commits: list, owner: str, repo: str) -> str:
    lines = []
    lines.append(f"# Commits in {owner}/{repo}")
    lines.append(f"Showing {len(commits)} commits\n")

    if not commits:
        lines.append("No commits found.")
        return "\n".join(lines)

    for idx, c in enumerate(commits, 1):
        sha_short = c["sha"][:7]
        message = c["commit"]["message"].splitlines()[0][:80]
        author_name = c["commit"]["author"]["name"]
        date = c["commit"]["author"]["date"][:10]

        lines.append(f"{idx}. {sha_short} — {message}")
        lines.append(f"   Author: {author_name} | Date: {date}")
        lines.append(f"   URL: {c['html_url']}")
        lines.append("")

    return "\n".join(lines)
