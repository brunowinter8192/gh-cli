# github/ — GitHub Research CLI

## Role

CLI tool delivering 14 GitHub commands: 9 read-only research commands (search, browse, issues, discussions, releases) plus 5 issue-management commands (3 write: create, update, delete; 2 read: list, get). `cli.py` is the argparse entry point; each subcommand delegates to a `<tool>_workflow()` function in `src/github/`. Delivered to Claude Code sessions via the `gh-cli` wrapper and `gh-cli-search` skill — invoked through Bash calls, no MCP protocol.

## Entry Points

- `cli.py` → 16 argparse subcommands; each imports `<tool>_workflow` from `src.github.<tool>`
- `~/.local/bin/gh-cli` wrapper → resolves to `python cli.py`; installed externally
- `skills/gh-cli-search/SKILL.md` → CC skill loaded by `.claude-plugin/plugin.json`; drives `gh-cli` calls from Claude Code sessions via Bash

## Directory Map

| Subdir | Role | LOC | Modules |
|--------|------|-----|---------|
| `src/github/` | Tool + infrastructure modules | ~1562 | 18 |
| `skills/gh-cli-search/` | CC skill config + Bash usage docs | — | 1 |
| `decisions/` | Pipeline decision records + OldThemes history | — | — |
| `dev/` | Legacy test artifacts | — | — |
| `.claude-plugin/` | Plugin metadata (skills-only) | — | 1 |

## Flow

1. `gh-cli <cmd> [args]` — wrapper invokes `python cli.py <cmd> [args]`
2. `cli.py` parses args, dispatches to `<tool>_workflow(params)`
3. Workflow calls fetch function — REST via `requests` + `build_headers()` / GraphQL via `graphql_query()`
4. Format function transforms raw API JSON to human-readable text
5. Workflow returns `list[TextContent]`
6. `cli.py` prints `result[0].text` to stdout; on any `Exception` → `Error: {str(e)}` to stderr + exit 1; `BrokenPipeError` → devnull dup2 + exit 0 (pipe-to-head stays clean)

## Shared State

| Owner | State | Who reads |
|-------|-------|-----------|
| `client.py` | `GITHUB_TOKEN` (str, module-level) — resolved once at import via `_resolve_token()` | all 13 REST modules (12 visible + `get_issue_comments`) via `build_headers()` / `request()`; `graphql_client.py` at import |

## Root-Level Files

| File | LOC | Why at root |
|------|-----|-------------|
| `cli.py` | 182 | Entry point — argparse dispatch for all 14 tools; central error handler (BrokenPipeError + Exception) |
| `requirements.txt` | 2 | Dependencies: `mcp` (TextContent type), `requests` |

## Subdir DOCS

- [src/github/DOCS.md](src/github/DOCS.md) — Module map for 16 tool modules + 2 infrastructure modules
