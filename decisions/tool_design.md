# Tool Design

## Status Quo (IST)

- 11 tools registered in `cli.py` (argparse subcommands); 9 are query/research tools, 2 (`index_issues`, `index_discussions`) are RAG-indexing commands (fetch + strip + write MDs + `workflow.py index-dir`)
- `get_issue`, `get_issue_comments` retained as internal helpers of `index_issues.py`; no subcommand (not CLI-accessible directly)
- `get_discussion` retained as internal helper of `index_discussions.py`; no subcommand (not CLI-accessible directly)
- `search_items`, `list_commits`, `compare_commits`, `search_discussions`, `list_discussions` removed from CLI surface; module files deleted from `src/github/`
- Query truncation: `search_repos` enforces `MAX_QUERY_WORDS=3` (GitHub Search returns 0 for long queries); `index_issues`/`index_discussions` cap at 3 keywords with 3→2→1 fallback
- Pagination: fixed `RESULTS_PER_PAGE=20` from `client.py`, no cursor-based pagination; `list_releases` exposes page-based pagination via `--page` param (GitHub `/releases` API supports `page` natively; `per_page` clamped to 100)
- `grep_repo` default `max_files=10`, caller can override
- `get_file_content` supports `offset`/`limit` for line-range reads and `metadata_only` mode
- `get_repo_tree` supports `depth` filtering and `pattern` glob matching

## Evidenz

No benchmarks run. Query truncation added after observing GitHub Search returning 0 results for multi-word queries.

## Recommendation (SOLL)

Pending — needs evaluation.

## Offene Fragen

- Is MAX_QUERY_WORDS=3 optimal or too aggressive?
- Should pagination be exposed as a tool parameter (page number)? → **Resolved for `list_releases`**: yes, page-based (`--page`). Other tools TBD.

## Quellen

None indexed.
