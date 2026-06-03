# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)

SEARCH_CODE_PER_PAGE = 30


# ORCHESTRATOR
def search_code_workflow(query: str) -> list[TextContent]:
    logger.info("search_code query=%s", query)
    raw_response = fetch_code_search(query)
    formatted_string = format_code_results(raw_response)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Fetch code search results with text match metadata
def fetch_code_search(query: str) -> dict:
    url = f"{GITHUB_API_BASE}/search/code"
    logger.debug("Fetching from %s", url)
    params = {
        "q": query,
        "per_page": SEARCH_CODE_PER_PAGE
    }
    response = requests.get(url, params=params, headers=build_headers("application/vnd.github.text-match+json"))
    response.raise_for_status()
    return response.json()


# Emit locator line (full_name path) then full fragments indented
def format_code_results(raw_response: dict) -> str:
    items = raw_response.get("items", [])

    if not items:
        return "No results. Note: GitHub Code Search does not index CSV/data files — use get_file_content for known paths."

    lines = []
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
