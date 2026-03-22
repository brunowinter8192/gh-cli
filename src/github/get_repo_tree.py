# INFRASTRUCTURE
import logging
import requests
from fnmatch import fnmatch
from os.path import basename
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)

MAX_TREE_CHARS = 1000
PATTERN_RESULTS_LIMIT = 50


# ORCHESTRATOR
def get_repo_tree_workflow(owner: str, repo: str, path: str = "", depth: int = -1, pattern: str = "") -> list[TextContent]:
    logger.info("get_repo_tree owner=%s repo=%s path=%s", owner, repo, path)
    default_branch = fetch_default_branch(owner, repo)
    tree_sha = get_tree_sha(owner, repo, default_branch, path)

    if pattern:
        raw_tree = fetch_tree(owner, repo, tree_sha, recursive=True)
        truncated = raw_tree.get("truncated", False)
        matches = filter_by_pattern(raw_tree, pattern)
        return [TextContent(type="text", text=format_matches(matches, pattern, path, truncated))]

    recursive = depth != 1
    raw_tree = fetch_tree(owner, repo, tree_sha, recursive)
    formatted_string = format_tree_response(raw_tree, path, depth)
    return [TextContent(type="text", text=formatted_string)]


# FUNCTIONS

# Get default branch name for repository
def fetch_default_branch(owner: str, repo: str) -> str:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    logger.debug("Fetching from %s", url)
    headers = build_headers()

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["default_branch"]


# Get tree SHA for specific path or root
def get_tree_sha(owner: str, repo: str, branch: str, path: str) -> str:
    if not path:
        url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/branches/{branch}"
        logger.debug("Fetching from %s", url)
        headers = build_headers()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()["commit"]["commit"]["tree"]["sha"]

    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"
    logger.debug("Fetching from %s", url)
    params = {"ref": branch}
    headers = build_headers("application/vnd.github.object+json")
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()
    if data.get("type") == "dir":
        return data["sha"]

    raise ValueError(f"Path '{path}' is not a directory")


# Fetch tree structure from GitHub Git Trees API
def fetch_tree(owner: str, repo: str, tree_sha: str, recursive: bool = True) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/git/trees/{tree_sha}"
    logger.debug("Fetching from %s", url)
    params = {"recursive": "true"} if recursive else {}
    headers = build_headers()

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


# Format tree response with depth filtering and root-level prioritization
def format_tree_response(raw_tree: dict, base_path: str, depth: int = -1) -> str:
    tree_items = raw_tree.get("tree", [])

    truncated = raw_tree.get("truncated", False)

    if not tree_items:
        lines = []
        lines.append(f"Directory: {base_path if base_path else '/'}\n")
        if truncated:
            lines.append("WARNING: Repository tree was truncated by GitHub API. Results may be incomplete.")
            lines.append("Use 'path' parameter to browse specific subdirectories or 'depth=1' for shallow listing.\n")
        lines.append("Empty directory.")
        return "\n".join(lines)

    if depth > 0:
        tree_items = [item for item in tree_items if item["path"].count("/") < depth]

    dirs = sorted(
        [item for item in tree_items if item["type"] == "tree"],
        key=lambda item: item["path"].count("/")
    )
    files = sorted(
        [item for item in tree_items if item["type"] == "blob"],
        key=lambda item: item["path"].count("/")
    )

    content_lines = []
    content_lines.append(f"Directories ({len(dirs)}):")
    for item in dirs[:50]:
        content_lines.append(f"  {item['path']}/")

    content_lines.append(f"\nFiles ({len(files)}):")
    for item in files[:50]:
        size = item.get("size", 0)
        content_lines.append(f"  {item['path']} ({size:,} bytes)")

    output_truncated = len("\n".join(content_lines)) > MAX_TREE_CHARS

    lines = []
    lines.append(f"Directory: {base_path if base_path else '/'}\n")

    if truncated:
        lines.append("WARNING: Repository tree was truncated by GitHub API. Results may be incomplete.")
        lines.append("Use 'path' parameter to browse specific subdirectories or 'depth=1' for shallow listing.\n")
    if output_truncated:
        lines.append(f"WARNING: Output truncated (>{MAX_TREE_CHARS} chars). Showing top 50 directories and 50 files.")
        lines.append("Use 'path' parameter or 'depth=1' to narrow results.\n")

    lines.extend(content_lines)
    return "\n".join(lines)


# Filter tree items by glob pattern against filename or full path
def filter_by_pattern(raw_tree: dict, pattern: str) -> list[dict]:
    items = [item for item in raw_tree.get("tree", []) if item["type"] == "blob"]
    has_slash = "/" in pattern
    return [
        item for item in items
        if fnmatch(item["path"] if has_slash else basename(item["path"]), pattern)
    ][:PATTERN_RESULTS_LIMIT]


# Format matching files as text output
def format_matches(matches: list[dict], pattern: str, base_path: str, truncated: bool = False) -> str:
    lines = []
    scope = base_path if base_path else "/"
    lines.append(f"Search: \"{pattern}\" in {scope}\n")

    if truncated:
        lines.append("WARNING: Repository tree was truncated by GitHub API. Results may be incomplete.")
        lines.append("Use the 'path' parameter to search within a specific directory for complete results.\n")

    if not matches:
        lines.append("No files found.")
        return "\n".join(lines)

    lines.append(f"Matches ({len(matches)}):")
    for item in matches:
        size = item.get("size", 0)
        lines.append(f"  {item['path']} ({size:,} bytes)")

    return "\n".join(lines)
