# INFRASTRUCTURE
import logging
import re
from mcp.types import TextContent
from src.github.get_repo_tree import fetch_default_branch, get_tree_sha, fetch_tree
from src.github.get_repo_tree import filter_by_pattern
from src.github.get_file_content import fetch_file_content, decode_content
from src.github.grep_file import search_lines

logger = logging.getLogger(__name__)

MAX_FILES = 10
MAX_MATCHES_PER_FILE = 3


# ORCHESTRATOR
def grep_repo_workflow(owner: str, repo: str, pattern: str, file_pattern: str = "*", path: str = "", max_files: int = MAX_FILES) -> list[TextContent]:
    """Regex search across repo files."""
    logger.info("grep_repo owner=%s repo=%s pattern=%s", owner, repo, pattern)
    max_files = max(max_files, 20)  # Floor: agent can go higher, never lower
    default_branch = fetch_default_branch(owner, repo)
    tree_sha = get_tree_sha(owner, repo, default_branch, path)
    raw_tree = fetch_tree(owner, repo, tree_sha, recursive=True)
    truncated = raw_tree.get("truncated", False)
    matching_files = filter_by_pattern(raw_tree, file_pattern)
    results = grep_matching_files(owner, repo, matching_files[:max_files], pattern, path)
    return [TextContent(type="text", text=format_grep_repo_results(results, pattern, file_pattern, path, len(matching_files), max_files, truncated))]


# FUNCTIONS

# Grep content of each matching file for regex pattern
def grep_matching_files(owner: str, repo: str, files: list[dict], pattern: str, base_path: str = "") -> list[dict]:
    results = []
    for file_item in files:
        file_path = f"{base_path}/{file_item['path']}" if base_path else file_item["path"]
        raw_response = fetch_file_content(owner, repo, file_path)
        if isinstance(raw_response, list):
            continue
        content = decode_content(raw_response)
        lines = content.split("\n")
        matches = search_lines(lines, pattern, 0, MAX_MATCHES_PER_FILE)
        results.append({"path": file_path, "matches": matches, "total_lines": len(lines)})
    return results


# Format grep results across multiple files
def format_grep_repo_results(results: list[dict], pattern: str, file_pattern: str, base_path: str, total_matching: int, max_files: int, truncated: bool) -> str:
    scope = base_path if base_path else "/"
    searched = len(results)
    output = []
    output.append(f"Search: \"{pattern}\" in {file_pattern} (scope: {scope})")
    output.append(f"Files searched: {searched}/{total_matching} matching files (max_files={max_files})\n")

    if truncated:
        output.append("WARNING: Repository tree was truncated by GitHub API. File list may be incomplete.")
        output.append("Use the 'path' parameter to narrow scope for complete results.\n")

    files_with_matches = [r for r in results if r["matches"]]
    files_without_matches = [r for r in results if not r["matches"]]

    if not files_with_matches:
        output.append("No matches found in any file.")
        return "\n".join(output)

    for result in files_with_matches:
        match_count = len(result["matches"])
        output.append(f"--- {result['path']} ({match_count} match{'es' if match_count != 1 else ''}) ---")
        for match in result["matches"]:
            line_num = match["match_line"] + 1
            line_text = match["lines"][match["match_line"] - match["start"]][1]
            output.append(f">  {line_num:>6}: {line_text}")
        output.append("")

    if files_without_matches:
        no_match_paths = [r["path"] for r in files_without_matches]
        output.append(f"No matches: {', '.join(no_match_paths)}")

    return "\n".join(output)
