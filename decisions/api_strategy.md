# API Strategy (REST vs GraphQL)

## Status Quo (IST)

- 13 modules use GitHub REST API v3 via `build_headers()` (`client.py`): 12 visible subcommands (search_repos, search_code, get_repo_tree, get_file_content, index_issues, get_repo, list_releases, get_release, create_issue, update_issue, list_issues, get_issue) + `get_issue_comments` (internal-only helper of `index_issues.py`)
- 3 modules use GitHub GraphQL API v4 via `graphql_query()` (`graphql_client.py`):
  - `index_discussions` (`index_discussions.py`) — calls `graphql_query` directly for repo-scoped `search(type: DISCUSSION)` in `search_discussions_raw()`; delegates per-thread fetch to `get_discussion_workflow()` (also GraphQL)
  - `delete_issue` (`delete_issue.py`) — resolves `node_id` via REST GET, then executes GraphQL `deleteIssue` mutation
  - `get_discussion` — single discussion with threaded comments + upvote sorting; internal-only helper of `index_discussions.py`, no CLI subcommand
- `search_discussions`, `list_discussions`, `grep_file`, `grep_repo` removed from surface; files deleted from `src/github/`
- GraphQL used for Discussions (no REST endpoint exists) and issue deletion (GraphQL mutation required)
- REST used for repos, code, issues, releases

## Evidenz

No benchmarks run. Architecture follows GitHub API availability — Discussions API is GraphQL-only; `deleteIssue` mutation is GraphQL-only.

## Recommendation (SOLL)

Pending — needs evaluation.

## Offene Fragen

- Should file-tree operations (get_repo_tree) use GraphQL for more efficient single-request fetches?
- Rate limit differences between REST and GraphQL for heavy usage patterns?

## Quellen

None indexed.
