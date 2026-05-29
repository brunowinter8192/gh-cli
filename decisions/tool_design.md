# Tool Design

## Status Quo (IST)

- 18 tools registered in `cli.py` (argparse subcommands); 17 are query/research tools, 1 (`index_issues`) is a RAG-indexing command (fetch + strip + write MDs + `workflow.py index-dir`)
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
- Should `search_items` (issues + PRs) be split into separate tools?

## Quellen

None indexed.
