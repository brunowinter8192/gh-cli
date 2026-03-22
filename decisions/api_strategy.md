# API Strategy (REST vs GraphQL)

## Status Quo (IST)

- 20 tools use GitHub REST API v3 via `client.py` (requests + `build_headers()`)
- 4 tools use GitHub GraphQL API v4 via `graphql_client.py`:
  - `search_discussions` — GraphQL Search for discussions
  - `list_discussions` — Repository discussions listing with category filter
  - `get_discussion` — Single discussion with threaded comments + upvote sorting
  - `list_discussions` category lookup — resolves category slug to ID
- GraphQL used exclusively for Discussions (no REST endpoint exists)
- REST used for everything else (repos, code, issues, PRs, commits, releases)

## Evidenz

No benchmarks run. Architecture follows GitHub API availability — Discussions API is GraphQL-only.

## Recommendation (SOLL)

Pending — needs evaluation.

## Offene Fragen

- Should file-tree operations (get_repo_tree) use GraphQL for more efficient single-request fetches?
- Rate limit differences between REST and GraphQL for heavy usage patterns?

## Quellen

None indexed.
