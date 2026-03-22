# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)

MAX_COMMITS_DISPLAY = 20
MAX_FILES_DISPLAY = 30


# ORCHESTRATOR
def compare_commits_workflow(owner: str, repo: str, base: str, head: str) -> list[TextContent]:
    logger.info("compare_commits owner=%s repo=%s base=%s head=%s", owner, repo, base, head)
    raw_data = fetch_comparison(owner, repo, base, head)
    formatted = format_comparison(raw_data)
    return [TextContent(type="text", text=formatted)]


# FUNCTIONS

# Fetch comparison between two refs
def fetch_comparison(owner: str, repo: str, base: str, head: str) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/compare/{base}...{head}"
    logger.debug("Fetching from %s", url)
    response = requests.get(url, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format comparison for display
def format_comparison(data: dict) -> str:
    status = data.get("status", "unknown")
    ahead = data.get("ahead_by", 0)
    behind = data.get("behind_by", 0)
    total = data.get("total_commits", 0)
    files = data.get("files", [])
    commits = data.get("commits", [])

    base_sha = data.get("base_commit", {}).get("sha", "")[:7]
    head_sha = data.get("commits", [{}])[-1].get("sha", "")[:7] if commits else ""

    lines = []
    lines.append(f"# Comparison: {base_sha}...{head_sha}")
    lines.append(f"Status: {status} | Ahead by: {ahead} | Behind by: {behind}")
    lines.append(f"Total commits: {total} | Files changed: {len(files)}")
    lines.append("")

    if commits:
        lines.append("## Commits")
        for idx, c in enumerate(commits[:MAX_COMMITS_DISPLAY], 1):
            sha_short = c["sha"][:7]
            message = c["commit"]["message"].splitlines()[0][:80]
            lines.append(f"{idx}. {sha_short} — {message}")
        if len(commits) > MAX_COMMITS_DISPLAY:
            lines.append(f"   ... and {len(commits) - MAX_COMMITS_DISPLAY} more commits")
        lines.append("")

    if files:
        lines.append(f"## Files Changed ({len(files)})")
        status_icons = {"added": "A", "removed": "D", "modified": "M", "renamed": "R"}
        for f in files[:MAX_FILES_DISPLAY]:
            icon = status_icons.get(f["status"], f["status"][0].upper())
            name = f["filename"]
            if f["status"] == "renamed" and f.get("previous_filename"):
                name = f"{f['previous_filename']} -> {f['filename']}"
            lines.append(f"  [{icon}] {name} (+{f['additions']} -{f['deletions']})")
        if len(files) > MAX_FILES_DISPLAY:
            lines.append(f"  ... and {len(files) - MAX_FILES_DISPLAY} more files")

    return "\n".join(lines)
