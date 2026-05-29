# API Strategy (REST vs GraphQL)

## Status Quo (IST)

- 15 tools use GitHub REST API v3 via `build_headers()` (`client.py`)
- 3 tools use GitHub GraphQL API v4 via `graphql_query()` (`graphql_client.py`):
  - `search_discussions` — GraphQL Search for discussions
  - `list_discussions` — Repository discussions listing with optional category filter
  - `get_discussion` — Single discussion with threaded comments + upvote sorting
- `lookup_category_id()` in `list_discussions.py` is an internal helper, not a separate tool
- GraphQL used exclusively for Discussions (no REST endpoint exists)
- REST used for everything else (repos, code, issues, commits, releases); `search_items --type pr` searches PRs via the Issues Search API — no dedicated PR-fetch tools remain

## Evidenz

No benchmarks run. Architecture follows GitHub API availability — Discussions API is GraphQL-only.

## Recommendation (SOLL)

Pending — needs evaluation.

## Offene Fragen

- Should file-tree operations (get_repo_tree) use GraphQL for more efficient single-request fetches?
- Rate limit differences between REST and GraphQL for heavy usage patterns?

## Quellen

None indexed.
