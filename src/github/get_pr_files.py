# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)

FILES_PER_PAGE = 100
MAX_PATCH_PREVIEW = 500


# ORCHESTRATOR
def get_pr_files_workflow(owner: str, repo: str, pull_number: int) -> list[TextContent]:
    logger.info("get_pr_files owner=%s repo=%s pull_number=%s", owner, repo, pull_number)
    raw_response = fetch_pr_files(owner, repo, pull_number)
    formatted_string = format_pr_files(raw_response, owner, repo, pull_number)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Fetch PR files from GitHub API
def fetch_pr_files(owner: str, repo: str, pull_number: int) -> list:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls/{pull_number}/files"
    logger.debug("Fetching from %s", url)
    params = {"per_page": FILES_PER_PAGE}
    response = requests.get(url, params=params, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format PR files for display
def format_pr_files(files: list, owner: str, repo: str, pull_number: int) -> str:
    lines = []

    total_additions = sum(f.get("additions", 0) for f in files)
    total_deletions = sum(f.get("deletions", 0) for f in files)

    lines.append(f"# Files Changed in {owner}/{repo}#{pull_number}")
    lines.append(f"Total: {len(files)} files | +{total_additions} additions | -{total_deletions} deletions\n")

    if not files:
        lines.append("No files changed in this PR.")
        return "\n".join(lines)

    for f in files:
        status_icon = {"added": "+", "removed": "-", "modified": "M", "renamed": "R"}.get(f["status"], "?")
        lines.append(f"[{status_icon}] {f['filename']}")
        lines.append(f"    +{f.get('additions', 0)} -{f.get('deletions', 0)} | Status: {f['status']}")

        if f.get("previous_filename"):
            lines.append(f"    Renamed from: {f['previous_filename']}")

        patch = f.get("patch", "")
        if patch:
            preview = patch[:MAX_PATCH_PREVIEW]
            if len(patch) > MAX_PATCH_PREVIEW:
                preview += "\n    ... (truncated)"
            lines.append(f"    Preview:\n    {preview.replace(chr(10), chr(10) + '    ')}")

        lines.append("")

    return "\n".join(lines)
