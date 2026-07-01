# API Strategy (REST vs GraphQL)

## Status Quo (IST)

- **REST API v3** via `build_headers()` (`client.py`): `search_repos`, `search_code`, `get_file_content`, `index_issues`, `index_releases`, `repo_freshness`, `create_issue`, `update_issue`, `list_issues`, `get_issue`, plus internal helper `get_issue_comments` (of `index_issues.py`). `download_files` is REST via `get_file_content`'s fetch. `delete_issue` resolves the issue `node_id` via a REST GET first.
- **GraphQL API v4** via `graphql_query()` (`graphql_client.py`):
  - `get_repo_tree` (`get_repo_tree.py`) — one-shot depth=1 tree with per-entry language / lineCount / size (replaces the former 3-REST recursive chain)
  - `index_discussions` (`index_discussions.py`) — repo-scoped `search(type: DISCUSSION)` in `search_discussions_raw()`; per-thread fetch via `get_discussion_workflow()` (also GraphQL). GraphQL-only — no REST Discussions endpoint exists.
  - `repo_counts` (`repo_counts.py`) — batched aliased query fetching `stargazerCount`, `issues{totalCount}`, `discussions{totalCount}`, `hasIssuesEnabled`, `hasDiscussionsEnabled` per repo in one HTTP call; layered on `search_repos.py`/`search_code.py` REST results
  - `delete_issue` (`delete_issue.py`) — `deleteIssue` mutation (GraphQL-only), after the REST node_id GET
  - `get_discussion` — single discussion with threaded comments; internal-only helper of `index_discussions.py`, no CLI subcommand
- `search_discussions`, `list_discussions`, `list_releases`, `get_release`, `grep_file`, `grep_repo` removed from surface; files deleted from `src/github/`.
- Split rule: REST for repos / code / issues / releases / file fetch; GraphQL where REST has no endpoint (Discussions), where a mutation requires it (`deleteIssue`), or where one round-trip beats a REST chain (`get_repo_tree` tree+metadata, `repo_counts` batched enrichment).

## Evidenz

No benchmarks run. Architecture follows GitHub API availability — Discussions API is GraphQL-only; `deleteIssue` mutation is GraphQL-only.

## Offene Fragen

- Rate limit differences between REST and GraphQL for heavy usage patterns?

## Quellen

None indexed.
