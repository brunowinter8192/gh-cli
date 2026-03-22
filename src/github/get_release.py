# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def get_release_workflow(owner: str, repo: str, tag: str | None = None) -> list[TextContent]:
    logger.info("get_release owner=%s repo=%s tag=%s", owner, repo, tag)
    raw = fetch_release(owner, repo, tag)
    formatted = format_release(raw, owner, repo)
    return [TextContent(type="text", text=formatted)]


# FUNCTIONS

# Fetch single release: latest or by tag
def fetch_release(owner: str, repo: str, tag: str | None) -> dict:
    if tag:
        url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases/tags/{tag}"
    else:
        url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases/latest"
    logger.debug("Fetching from %s", url)
    response = requests.get(url, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Format release with full body for display
def format_release(r: dict, owner: str, repo: str) -> str:
    tag = r.get("tag_name", "")
    name = r.get("name", "") or tag
    published = (r.get("published_at") or "")[:10]
    prerelease = "Pre-release" if r.get("prerelease") else "Release"
    url = r.get("html_url", "")
    assets = r.get("assets", [])

    lines = []
    lines.append(f"# {name} ({tag})")
    lines.append(f"{owner}/{repo} | {prerelease} | Published: {published}")
    lines.append(f"URL: {url}")
    lines.append("")

    body = (r.get("body") or "").strip()
    if body:
        lines.append(body)
    else:
        lines.append("No release notes.")

    if assets:
        lines.append("")
        lines.append(f"## Assets ({len(assets)})")
        for a in assets:
            size_mb = a.get("size", 0) / (1024 * 1024)
            downloads = a.get("download_count", 0)
            lines.append(f"- {a['name']} ({size_mb:.1f} MB, {downloads} downloads)")

    return "\n".join(lines)
