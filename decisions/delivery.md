# Delivery Architecture

## Status Quo (IST)

- **Entry point:** `cli.py` — argparse CLI, 16 subcommands (233 LOC)
- **Wrapper:** `~/.local/bin/gh-cli` → invokes `python cli.py`; installed externally; in PATH
- **Plugin:** skills-only — `.claude-plugin/plugin.json` `"skills": ["./skills/github-search/"]`; no MCP server, no `"tools"` key
- **Skill:** `skills/gh-cli-search/SKILL.md` — CC skill loaded by the plugin; drives `gh-cli` calls via Bash; frontmatter: `description` (trigger phrases + negativ-liste for auto-activation), `allowed-tools: Bash` (constraint: no Read/Edit/Glob during GitHub-research activation)
- **Return contract:** all 16 visible `<tool>_workflow()` functions return `list[TextContent]`; `print(result[0].text)` in `cli.py` `main()` dispatch; `get_issue_comments_workflow` internal-only helper of `index_issues.py` (no CLI subcommand); `get_discussion_workflow` internal-only helper of `index_discussions.py` (no CLI subcommand)
- **REST tools:** 14 visible subcommands + `get_issue_comments` (internal-only) = 15 REST modules; all via `build_headers()` (`src/github/client.py`) — `GITHUB_API_BASE`, auth, `RESULTS_PER_PAGE=20`
- **GraphQL tools:** 2 visible subcommands (`index_discussions`, `delete_issue`) + `get_discussion` (internal-only) = 3 GraphQL modules; all via `graphql_query()` (`src/github/graphql_client.py`). `search_discussions`, `list_discussions` removed (files deleted).
- **Infra (not tools):** `client.py`, `graphql_client.py`

## Evidenz

From code:
- `print(result[0].text)` in `cli.py` `main()` — TextContent contract enforced at dispatch layer
- `search_repos_workflow()` → `list[TextContent]` return annotation (representative; all 16 visible workflows carry this type, confirmed via `from mcp.types import TextContent` in each module)
- `.claude-plugin/plugin.json`: `"skills": ["./skills/github-search/"]` only — no server or tools key
- `_resolve_token()` in `client.py` — zshrc-first token resolution active at module-import time

## Recommendation (SOLL)

Keep (no change needed).

## Offene Fragen

None.

## Quellen

None indexed.
