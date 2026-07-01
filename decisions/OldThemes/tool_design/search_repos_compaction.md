# search_repos Compaction — Rationale

## Why one-line `full_name stars`

The primary consumer of `search_repos` results is the traversal chain: `search_repos` → `get_repo` / `get_repo_tree` → `get_file_content`. The only field needed to enter that chain is `owner/repo` (`full_name`). Star count is the single useful signal for prioritising which repos to read next (a proxy for community adoption / maintenance health). Every other field in the old 6-line block (description, forks, language, topics, license, open_issues, URL) is redundant: description is returned by `get_repo`; URL is derivable from full_name; forks/language/topics are noise for the discovery use-case.

Token density: 30 one-liners ≈ 600 chars vs the old 20 × 6-line format ≈ 3 600 chars — a 6× reduction for a larger result set.

## Why per_page=30, scoped to search_repos only

`RESULTS_PER_PAGE=20` in `client.py` is a shared constant used by `search_code.py`. Changing it would silently raise `search_code` pagination as a side-effect — a different tool with different cost/benefit tradeoffs. Introducing `SEARCH_REPOS_PER_PAGE=30` in `search_repos.py` keeps the scoping explicit: search_repos gets 30 compact lines; search_code stays at 20 richer results.

The GitHub Search Repositories API supports `per_page` up to 100. The API hard-caps total accessible results at 1 000 (pages beyond that return empty). 30 is a practical sweet-spot: broad enough to surface niche alternatives, small enough to stay well under the output budget even before compact formatting.

## Why the index_issues 3→2→1 fallback instead of hard-truncate

The old `enforce_query_length` hard-truncated to 3 words and emitted a warning, but made no search attempt with the truncated query — it was merely a guard. Users had to manually retry with shorter queries. The `index_issues` fallback (`index_issues_workflow` lines 31–44) already proved the pattern works: take first 3 words, retry down to 1, stop at first non-zero `total_count`. Mirroring it in `search_repos` makes the two tools consistent and removes the manual retry burden. `enforce_query_length` and the `MAX_QUERY_WORDS` / `MAX_OUTPUT_CHARS` constants were deleted.

The `MAX_OUTPUT_CHARS=80_000` guard became moot: 30 × ~40-char lines ≈ 1 200 chars, well inside any budget.

## Why sort defaults to `best_match` (not `stars`)

GitHub's `best_match` applies a multi-factor relevance ranking that considers text match score, repo activity, star count, and fork count together. Defaulting to `sort=stars` discards relevance: a query for "fastapi oauth2" would surface generic mega-popular repos that happen to contain those words over purpose-built libraries. `best_match` is GitHub's own recommendation for discovery queries. Users who want star-ranked results can pass `--sort-by stars` explicitly.

## API surface note

The GitHub Search Repositories REST endpoint (`GET /search/repositories`) exposes 5 query parameters: `q`, `sort`, `order`, `per_page`, `page`. The `search_repos` wrapper currently exposes only `q` (as `query`) and `sort` (as `sort_by`). `order` is fixed to `desc`; `per_page` is fixed to 30 (local constant); `page` is not exposed (no cursor pagination). This is intentional — exposing `per_page` and `page` as CLI params is deferred until a concrete need arises.
