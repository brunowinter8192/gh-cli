# Tool Design

## Status Quo (IST)

- 13 tools registered in `cli.py` (argparse subcommands); 6 are query/research tools (search_repos, search_code, get_repo_tree, get_file_content, list_releases, get_release), 2 (`index_issues`, `index_discussions`) are RAG-indexing commands, 3 are issue write commands (`create_issue`, `update_issue`, `delete_issue`), 2 are issue read commands (`list_issues`, `get_issue`)
- `get_issue` exposed as CLI subcommand (owner/repo/number → title/state/body); also called internally by `index_issues.py`
- `get_issue_comments` retained as internal-only helper of `index_issues.py`; no subcommand (not CLI-accessible directly)
- `get_discussion` retained as internal helper of `index_discussions.py`; no subcommand (not CLI-accessible directly)
- `grep_file`, `grep_repo` removed from surface; files deleted from `src/github/`. Client-side grep tools with no own GitHub API endpoint; `search_code` covers the research use-case
- `comment_issue` removed from surface; `src/github/comment_issue.py` deleted
- `get_repo` removed from surface; `src/github/get_repo.py` deleted — no use-case
- `search_items`, `list_commits`, `compare_commits`, `search_discussions`, `list_discussions` removed from CLI surface; module files deleted from `src/github/`
- Query truncation: `search_repos`, `index_issues`, `index_discussions` all cap at 3 keywords with 3→2→1 fallback (drop from back until `total_count > 0`; `search_repos` hard-truncate removed)
- Output: `search_repos` emits one line per repo (`full_name stars`, plain integer); `search_code` emits `full_name path` locator + full untruncated fragment(s) indented; decorative headers removed from both
- Pagination: `search_repos` uses `SEARCH_REPOS_PER_PAGE=30` (local constant in `search_repos.py`); `search_code` uses `SEARCH_CODE_PER_PAGE=30` (local constant in `search_code.py`); shared pagination constant removed from `client.py` (no remaining users); `list_releases` exposes page-based pagination via `--page` param (GitHub `/releases` API supports `page` natively; `per_page` clamped to 100)
- `get_file_content` supports `offset`/`limit` for line-range reads and `metadata_only` mode
- `get_repo_tree` supports `depth` filtering and `pattern` glob matching

## Evidenz

No benchmarks run. Query truncation added after observing GitHub Search returning 0 results for multi-word queries.

## Recommendation (SOLL)

Pending — needs evaluation.

## Offene Fragen

- Is 3-keyword cap optimal or too aggressive? → **Resolved for `search_repos`**: 3-word cap retained; hard-truncate replaced by 3→2→1 fallback so narrow trailing keywords no longer block results.
- Should pagination be exposed as a tool parameter (page number)? → **Resolved for `list_releases`**: yes, page-based (`--page`). Other tools TBD.

## Quellen

None indexed.
