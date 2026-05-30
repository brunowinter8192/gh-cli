# Delivery Architecture

## Status Quo (IST)

- **Entry point:** `cli.py` — argparse CLI, 11 subcommands (`search_repos` … `get_release`)
- **Wrapper:** `~/.local/bin/gh-cli` → invokes `python cli.py`; installed externally; in PATH
- **Plugin:** skills-only — `.claude-plugin/plugin.json` `"skills": ["./skills/github-search/"]`; no MCP server, no `"tools"` key
- **Skill:** `skills/github-search/SKILL.md` — CC skill loaded by the plugin; drives `gh-cli` calls via Bash
- **Return contract:** all 11 visible `<tool>_workflow()` functions return `list[TextContent]`; `print(result[0].text)` in `cli.py` `main()` dispatch; `get_issue_workflow` + `get_issue_comments_workflow` internal-only helpers of `index_issues.py`; `get_discussion_workflow` internal-only helper of `index_discussions.py`
- **REST tools:** 9 visible subcommands + `get_issue`, `get_issue_comments` (internal-only); all via `build_headers()` (`src/github/client.py`) — `GITHUB_API_BASE`, auth, `RESULTS_PER_PAGE=20`
- **GraphQL tools:** `graphql_query()` (`src/github/graphql_client.py`) — Discussions API (no REST endpoint exists); `index_discussions.py` uses GraphQL directly for `search(type:DISCUSSION)` + delegates to `get_discussion_workflow()`. `search_discussions`, `list_discussions` removed (files deleted).

## Evidenz

From code:
- `print(result[0].text)` in `cli.py` `main()` — TextContent contract enforced at dispatch layer
- `search_repos_workflow()` → `list[TextContent]` return annotation (representative; all 11 visible workflows carry this type, confirmed via `from mcp.types import TextContent` in each module)
- `.claude-plugin/plugin.json`: `"skills": ["./skills/github-search/"]` only — no server or tools key
- `_resolve_token()` in `client.py` — zshrc-first token resolution active at module-import time

## Recommendation (SOLL)

Keep (no change needed).

## Offene Fragen

None.

## Quellen

None indexed.
