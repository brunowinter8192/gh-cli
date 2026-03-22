# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)

MAX_BODY_LENGTH = 300


# ORCHESTRATOR
def list_releases_workflow(owner: str, repo: str, per_page: int = 10) -> list[TextContent]:
    logger.info("list_releases owner=%s repo=%s", owner, repo)
    raw_data = fetch_releases(owner, repo, per_page)
    formatted = format_releases(raw_data, owner, repo)
    return [TextContent(type="text", text=formatted)]


# FUNCTIONS

# Fetch releases from repository
def fetch_releases(owner: str, repo: str, per_page: int) -> list:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases"
    logger.debug("Fetching from %s", url)
    params = {"per_page": per_page}
    response = requests.get(url, params=params, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format release list for display
def format_releases(releases: list, owner: str, repo: str) -> str:
    lines = []
    lines.append(f"# Releases in {owner}/{repo}")
    lines.append(f"Showing {len(releases)} releases\n")

    if not releases:
        lines.append("No releases found.")
        return "\n".join(lines)

    for idx, r in enumerate(releases, 1):
        tag = r.get("tag_name", "")
        name = r.get("name", "") or tag
        published = (r.get("published_at") or "")[:10]
        prerelease = "Yes" if r.get("prerelease") else "No"
        draft = "Yes" if r.get("draft") else "No"
        assets_count = len(r.get("assets", []))
        url = r.get("html_url", "")

        lines.append(f"{idx}. {tag} — {name}")
        lines.append(f"   Published: {published} | Prerelease: {prerelease} | Draft: {draft} | Assets: {assets_count}")

        body = (r.get("body") or "").strip()
        if body:
            body_preview = body[:MAX_BODY_LENGTH]
            if len(body) > MAX_BODY_LENGTH:
                body_preview += "..."
            body_oneline = " ".join(body_preview.splitlines())
            lines.append(f"   Changelog: {body_oneline}")

        lines.append(f"   URL: {url}")
        lines.append("")

    return "\n".join(lines)
