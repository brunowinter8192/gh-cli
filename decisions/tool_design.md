# Tool Design

## Status Quo (IST)

- 13 tools registered in `cli.py` (argparse subcommands); 12 are query/research tools, 1 (`index_issues`) is a RAG-indexing command (fetch + strip + write MDs + `workflow.py index-dir`)
- `get_issue`, `get_issue_comments` retained as internal helpers of `index_issues.py`; no subcommand (not CLI-accessible directly)
- `search_items`, `list_commits`, `compare_commits` removed from CLI surface; module files deleted from `src/github/`
- Query truncation: `search_repos` enforces `MAX_QUERY_WORDS=3` (GitHub Search returns 0 for long queries)
- Pagination: fixed `RESULTS_PER_PAGE=20` from `client.py`, no cursor-based pagination
- `grep_repo` default `max_files=10`, caller can override
- `get_file_content` supports `offset`/`limit` for line-range reads and `metadata_only` mode
- `get_repo_tree` supports `depth` filtering and `pattern` glob matching
- `get_discussion` supports `comment_sort` (upvotes vs chronological) and `comment_limit`

## Evidenz

No benchmarks run. Query truncation added after observing GitHub Search returning 0 results for multi-word queries.

## Recommendation (SOLL)

Pending — needs evaluation.

## Offene Fragen

- Is MAX_QUERY_WORDS=3 optimal or too aggressive?
- Should pagination be exposed as a tool parameter (page number)?

## Quellen

None indexed.
