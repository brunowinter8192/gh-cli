# MCP to CLI Migration

## Context

The project originally ran as a FastMCP server (`server.py`), exposing 21 tools via the MCP protocol. Claude Code sessions accessed them through MCP tool registration. Tool docstrings followed a 3-5 word server-pattern convention imposed by FastMCP.

## Rationale

Three drivers for the migration:

**Testability.** The CLI is directly invokable: `python cli.py <cmd> [args]` or `gh-cli <cmd> [args]`. No MCP session, no protocol negotiation, no running CC instance required. Any tool call can be smoke-tested from a plain shell.

**Maintainability.** FastMCP dispatch adds a protocol indirection layer that provides no semantic value for this use case. GitHub API tools have no state, no streaming, and no side effects that require MCP's tool-call model. Argparse CLI is standard Python with no framework dependency for dispatch logic.

**CC hooks make MCP unnecessary.** With the `gh-cli` wrapper and `github-search` skill, Claude Code sessions invoke tools via plain Bash calls. The skill layer delivers the same capability ("Claude can call GitHub research tools") at lower complexity. No MCP server process, no socket lifecycle, no registration overhead.

## Result

- `server.py` replaced by `cli.py` (argparse, 20 subcommands). The old docs cited 21 — that count was stale; tool consolidation happened in earlier commits (e.g. fb2d265 "Consolidate MCP tools: 19 → 17 via merge-first", 37807a3 "migrate github-research from MCP to pure CLI"), not during this documentation session.
- Plugin changed from MCP-server to skills-only: `.claude-plugin/plugin.json` sets `"skills": ["./skills/github-search/"]` with no `"server"` key
- Tool docstrings replaced by argparse `help=` strings
- `mcp` package retained in `requirements.txt`: all `<tool>_workflow()` functions still return `list[TextContent]` for the newline-rendering fix (see `decisions/OldThemes/output_textcontent.md`)

Current delivery state documented in `decisions/delivery.md`.
