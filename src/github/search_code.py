# INFRASTRUCTURE
import logging
import requests
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, RESULTS_PER_PAGE, build_headers

logger = logging.getLogger(__name__)


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
        "per_page": RESULTS_PER_PAGE
    }
    response = requests.get(url, params=params, headers=build_headers("application/vnd.github.text-match+json"))
    response.raise_for_status()
    return response.json()


# Extract relevant fields from raw API response
def format_code_results(raw_response: dict) -> str:
    total = raw_response["total_count"]
    items = raw_response.get("items", [])

    lines = []
    lines.append(f"Found {total:,} code matches.\n")

    if not items:
        lines.append("No results to display.")
        lines.append("\nNOTE: GitHub Code Search does not index all file types. CSV, TSV, and other data files")
        lines.append("are not searchable. Use grep_file with a known file path, or grep_repo to search file")
        lines.append("content by pattern.")
        return "\n".join(lines)

    lines.append("Top Matches:\n")

    for idx, item in enumerate(items, 1):
        repo_info = item["repository"]
        owner = repo_info["owner"]["login"]
        repo_name = repo_info["name"]
        full_name = repo_info["full_name"]
        path = item["path"]
        url = item["html_url"]

        lines.append(f"{idx}. {full_name} - {path}")
        lines.append(f"   URL: {url}")

        if "text_matches" in item and item["text_matches"]:
            lines.append("   Code Fragments:")
            text_matches = extract_text_matches(item["text_matches"])
            for match in text_matches[:3]:
                fragment = match.get("fragment", "").strip()
                if fragment:
                    lines.append(f"     {fragment[:100]}...")

        lines.append("")

    return "\n".join(lines)


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
