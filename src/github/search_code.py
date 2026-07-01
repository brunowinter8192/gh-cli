# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
# From client.py: base API URL and header builder with auth token
from src.github.client import GITHUB_API_BASE, build_headers
# From repo_counts.py: batch-fetch star/issue/discussion counts, format per-repo summary line
from src.github.repo_counts import fetch_repo_counts, format_count_line

logger = logging.getLogger(__name__)

SEARCH_CODE_PER_PAGE = 30


# ORCHESTRATOR
def search_code_workflow(query: str) -> list[TextContent]:
    logger.info("search_code query=%s", query)
    raw_response = fetch_code_search(query)
    items = raw_response.get("items", [])
    if not items:
        return [TextContent(type="text", text="No results. Note: GitHub Code Search does not index CSV/data files — use get_file_content for known paths.")]
    repo_order = collect_unique_repos(items)
    repos = [tuple(fn.split("/", 1)) for fn in repo_order]
    counts = fetch_repo_counts(repos)
    formatted_string = format_code_results(items, repo_order, counts)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Fetch code search results with text match metadata
def fetch_code_search(query: str) -> dict:
    url = f"{GITHUB_API_BASE}/search/code"
    logger.debug("Fetching from %s", url)
    params = {"q": query, "per_page": SEARCH_CODE_PER_PAGE}
    response = requests.get(url, params=params, headers=build_headers("application/vnd.github.text-match+json"))
    response.raise_for_status()
    return response.json()


# Collect unique repo full_names from code hits, in first-seen order
def collect_unique_repos(items: list) -> list:
    seen = set()
    order = []
    for item in items:
        fn = item["repository"]["full_name"]
        if fn not in seen:
            seen.add(fn)
            order.append(fn)
    return order


# Emit repo summary block then per-hit locator + fragments
def format_code_results(items: list, repo_order: list, counts: dict) -> str:
    lines = []
    lines.append(f"## Repos ({len(repo_order)} unique)")
    for full_name in repo_order:
        c = counts.get(full_name)
        stars = c.get("stars", 0) if c else 0
        lines.append(format_count_line(full_name, stars, c))
    lines.append("")
    for item in items:
        full_name = item["repository"]["full_name"]
        path = item["path"]
        lines.append(f"{full_name} {path}")
        if item.get("text_matches"):
            text_matches = extract_text_matches(item["text_matches"])
            for match in text_matches[:3]:
                fragment = match.get("fragment", "").strip()
                if fragment:
                    for fline in fragment.splitlines():
                        lines.append(f"  {fline}")
                    lines.append("")
        lines.append("")
    return "\n".join(lines).rstrip()


# Extract code fragments from text match metadata
def extract_text_matches(matches: list) -> list:
    fragments = []
    for match in matches:
        if match.get("property") in ["content", "path"]:
            fragments.append({
                "fragment": match.get("fragment", ""),
                "property": match.get("property", "")
            })
    return fragments
