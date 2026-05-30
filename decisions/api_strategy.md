# API Strategy (REST vs GraphQL)

## Status Quo (IST)

- 11 modules use GitHub REST API v3 via `build_headers()` (`client.py`): 9 visible subcommands + `get_issue`, `get_issue_comments` (internal-only helpers of `index_issues.py`)
- 2 tools use GitHub GraphQL API v4 via `graphql_query()` (`graphql_client.py`):
  - `index_discussions` (`index_discussions.py`) — calls `graphql_query` directly for repo-scoped `search(type: DISCUSSION)` in `search_discussions_raw()`; delegates per-thread fetch to `get_discussion_workflow()` (also GraphQL)
  - `get_discussion` — single discussion with threaded comments + upvote sorting; internal-only helper of `index_discussions.py`, no CLI subcommand
- `search_discussions`, `list_discussions` removed from surface; files deleted from `src/github/`
- GraphQL used exclusively for Discussions (no REST endpoint exists)
- REST used for repos, code, issues (via `index_issues`), releases; commit tools (`list_commits`, `compare_commits`) and PR/issue search (`search_items`) removed from surface

## Evidenz

No benchmarks run. Architecture follows GitHub API availability — Discussions API is GraphQL-only.

## Recommendation (SOLL)

Pending — needs evaluation.

## Offene Fragen

- Should file-tree operations (get_repo_tree) use GraphQL for more efficient single-request fetches?
- Rate limit differences between REST and GraphQL for heavy usage patterns?

## Quellen

None indexed.
