# API Strategy (REST vs GraphQL)

## Status Quo (IST)

- 12 modules use GitHub REST API v3 via `build_headers()` (`client.py`): 10 visible subcommands + `get_issue`, `get_issue_comments` (internal-only helpers of `index_issues.py`)
- 3 tools use GitHub GraphQL API v4 via `graphql_query()` (`graphql_client.py`):
  - `search_discussions` — GraphQL Search for discussions
  - `list_discussions` — Repository discussions listing with optional category filter
  - `get_discussion` — Single discussion with threaded comments + upvote sorting
- `lookup_category_id()` in `list_discussions.py` is an internal helper, not a separate tool
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
