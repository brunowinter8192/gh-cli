# Tool Design

## Status Quo (IST)

- 21 MCP tools registered in `server.py`
- Query truncation: `search_repos` enforces MAX_QUERY_WORDS=3 (GitHub Search returns 0 for long queries)
- Pagination: Fixed `RESULTS_PER_PAGE=20` from `client.py`, no cursor-based pagination
- `grep_repo` default `max_files=10`, agent can override
- `get_file_content` supports `offset`/`limit` for line-range reads and `metadata_only` mode
- `get_repo_tree` supports `depth` filtering and `pattern` glob matching
- `get_discussion` supports `comment_sort` (upvotes vs chronological) and `comment_limit`
- Minimal tool docstrings (3-5 words) per server-pattern convention

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
