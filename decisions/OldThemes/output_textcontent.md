# Output Contract: list[TextContent]

Two sequential output bugs in late 2025 drove the current workflow return type. Both occurred in the original FastMCP server era and the fix survives the CLI migration.

## Problem

Two distinct symptoms, same session (2025-11-18):

1. **JSON double-encoding:** Tool output appeared as JSON-escaped gibberish — `{"result":"{\n  \"total_count\": 119429,\n  \"items\": [\n ..."}`. Context7 MCP displayed clean formatted text; GitHub MCP did not.

2. **Literal `\n` rendering:** After fixing (1), all tools displayed literal `\n` escape sequences instead of line breaks — `"Found 39,530 repositories...\n\nTop Results:\n\n1. firecrawl"` — single-line strings visible in Claude Code.

## Investigation

### Code Analysis

**Bug 1 — double-encoding:** Format functions returned `json.dumps(result, indent=2)`. FastMCP wraps tool return values in a JSON protocol layer when serializing for MCP. Serializing an already-JSON string produces a second JSON encoding: inner quotes become `\"`, newlines become `\n`. Fix: replaced `json.dumps()` with human-readable text formatters across the four initial modules (`search_repos.py`, `search_code.py`, `get_file_content.py`, `get_repo_tree.py`). Removed `import json` from all four.

**Bug 2 — newline rendering:** After fix 1, workflow functions returned plain `str`. Claude Code v2.0.22+ introduced an undocumented breaking change: when FastMCP tools return primitive `str`, FastMCP generates both a `content` array (TextContent blocks, where newlines render correctly) AND a `structuredContent` JSON object. CC v2.0.22+ prioritizes `structuredContent` for display, rendering the JSON representation with escaped `\n` sequences.

### External Research

| Source | Result | Relevance |
|--------|--------|-----------|
| anthropics/claude-code#9962 | Found ✅ | Confirmed CC v2.0.22+ `structuredContent` priority as breaking change |

## Resolution

All `<tool>_workflow()` functions return `list[TextContent]` (imported from `mcp.types`). Wrapping in `TextContent` prevents FastMCP from generating `structuredContent`, forcing CC to use only the `content` array where newlines render correctly.

## Current Status

The `list[TextContent]` contract survives the MCP → CLI migration. `cli.py` dispatches with `print(result[0].text)` (line 272). The `mcp` package remains in `requirements.txt` exclusively for this import — no MCP server is running. All 20 workflow functions in `src/github/` carry `-> list[TextContent]` return annotations.
