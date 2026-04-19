# INFRASTRUCTURE
import logging
import re
from mcp.types import TextContent
from src.github.get_file_content import fetch_file_content, decode_content

logger = logging.getLogger(__name__)

MAX_MATCHES = 50


# ORCHESTRATOR
def grep_file_workflow(owner: str, repo: str, path: str, pattern: str, context_lines: int = 0, max_matches: int = MAX_MATCHES) -> list[TextContent]:
    logger.info("grep_file owner=%s repo=%s path=%s pattern=%s", owner, repo, path, pattern)
    pattern, warning = normalize_pattern(pattern)
    raw_response = fetch_file_content(owner, repo, path)

    if isinstance(raw_response, list):
        raise ValueError(f"Path '{path}' is a directory, not a file.")

    content = decode_content(raw_response)
    lines = content.split("\n")
    matches = search_lines(lines, pattern, context_lines, max_matches)
    return [TextContent(type="text", text=format_grep_response(matches, path, pattern, len(lines), warning))]


# FUNCTIONS

# Normalize POSIX-ERE escapes to Python re syntax. Returns (pattern, warning_or_None).
def normalize_pattern(pattern: str) -> tuple[str, str | None]:
    if r'\|' in pattern:
        fixed = pattern.replace(r'\|', '|')
        return fixed, (
            f"Pattern contained POSIX-ERE '\\|' — auto-normalized to Python '|' for alternation. "
            f"Original: {pattern!r}  →  Used: {fixed!r}. Use bare '|' in future queries."
        )
    return pattern, None


# Find lines matching regex pattern with optional context
def search_lines(lines: list[str], pattern: str, context_lines: int, max_matches: int) -> list[dict]:
    compiled = re.compile(pattern)
    match_indices = [i for i, line in enumerate(lines) if compiled.search(line)]

    if not match_indices:
        return []

    results = []
    for idx in match_indices[:max_matches]:
        start = max(0, idx - context_lines)
        end = min(len(lines), idx + context_lines + 1)
        results.append({
            "match_line": idx,
            "start": start,
            "end": end,
            "lines": [(i, lines[i]) for i in range(start, end)]
        })

    return results


# Format grep results as text output
def format_grep_response(matches: list[dict], path: str, pattern: str, total_lines: int, warning: str | None = None) -> str:
    output = []
    if warning:
        output.append(f"Note: {warning}\n")
    output.append(f"File: {path} ({total_lines:,} lines)")
    output.append(f"Pattern: \"{pattern}\"")

    if not matches:
        output.append("\nNo matches found.")
        return "\n".join(output)

    output.append(f"Matches: {len(matches)}\n")

    for match in matches:
        for line_num, line_text in match["lines"]:
            marker = ">" if line_num == match["match_line"] else " "
            output.append(f"{marker} {line_num + 1:>6}: {line_text}")
        if match != matches[-1]:
            output.append("  ---")

    return "\n".join(output)
