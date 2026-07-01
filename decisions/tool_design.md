# Tool Design

## Status Quo (IST)

- 14 tools registered in `cli.py` (argparse subcommands); 9 are research/query tools (search_repos, search_code, get_repo_tree, get_file_content, repo_freshness, download_files, index_issues, index_discussions, index_releases), 5 are issue-management commands (create_issue, update_issue, delete_issue, list_issues, get_issue)
- `get_issue` exposed as CLI subcommand (owner/repo/number → title/state/body); also called internally by `index_issues.py`
- `get_issue_comments` retained as internal-only helper of `index_issues.py`; no subcommand (not CLI-accessible directly)
- `get_discussion` retained as internal helper of `index_discussions.py`; no subcommand (not CLI-accessible directly)
- `grep_file`, `grep_repo` removed from surface; files deleted from `src/github/`. Client-side grep tools with no own GitHub API endpoint; `search_code` covers the research use-case
- `comment_issue` removed from surface (file deleted)
- `get_repo` removed from surface (file deleted) — no use-case
- `search_items`, `list_commits`, `compare_commits`, `search_discussions`, `list_discussions` removed from CLI surface; module files deleted from `src/github/`
- Query truncation: `search_repos`, `index_issues`, `index_discussions` all cap at 3 keywords with 3→2→1 fallback (drop from back until `total_count > 0`; `search_repos` hard-truncate removed)
- Output: `search_repos` emits one enriched line per repo (`full_name · ⭐stars · issues:N · discussions:M`; `(off)` appended when `hasIssuesEnabled`/`hasDiscussionsEnabled` false); stars from REST `stargazers_count`. `search_code` prepends a `## Repos (N unique)` summary block (same line format per unique repo; stars from GraphQL `stargazerCount` — REST /search/code returns only a minimal repo stub without star count) then the existing per-hit `full_name path` + fragment(s) output. Both tools call `fetch_repo_counts()` (`src/github/repo_counts.py`) after the REST search to enrich counts in a single batched aliased GraphQL call. Null-repo guard: if a repo's GraphQL node is `null` (deleted/renamed between search and enrichment), counts render as `issues:? · discussions:?`.
- Pagination: `search_repos` uses `SEARCH_REPOS_PER_PAGE=30` (local constant in `search_repos.py`); `search_code` uses `SEARCH_CODE_PER_PAGE=30` (local constant in `search_code.py`); shared pagination constant removed from `client.py` (no remaining users)
- `index_releases` per-repo RAG indexing: fixed single collection `github_releases` (wipe-per-index — janitor deletes collection + rmtrees `RAG_ROOT/data/documents/github_releases/` before refill, so only one repo's releases are present at a time); `GET /repos/{o}/{r}/releases?per_page=100` (hard 100, newest-first, no sort param); per-release MD written to `RAG_ROOT/data/documents/github_releases/`; `list_releases` and `get_release` removed
- `get_file_content` supports `offset`/`limit` for line-range reads and `metadata_only` mode; implementation: `GET /repos/{o}/{r}/contents/{path}` with three size tiers — ≤1 MB: base64 inline decode (offset/limit apply); 1–100 MB: stream `download_url` to `/tmp/gh-cli_{owner}_{repo}_{path}` via `requests` chunked streaming, return path (offset/limit do not apply — caller reads the /tmp file locally); >100 MB: return error (GitHub API hard limit, no download possible). `metadata_only` works for all sizes.
- `get_repo_tree` one-level directory traversal (depth=1 always); implementation: GraphQL one-shot (`repository.object(expression)` → `Tree.entries`); metadata block (description/primaryLanguage/languages) on root call only; `--path` is the single exposed param; no depth/pattern/blob-reading

## Evidenz

No benchmarks run. Query truncation added after observing GitHub Search returning 0 results for multi-word queries.

**GraphQL traversal probes** (`dev/repo_exploration/`):
- Script: `probe_graphql_explore.py` — GraphQL one-shot depth=1 tree traversal; production shape (tree-only, metadata-on-root, single expression param).
- Root call output: `md/graphql_explore.md` — metadata block + 17-entry root tree for `anthropics/claude-code`; one round-trip.
- Sub-path call output: `md/graphql_plugins.md` — tree-only (no metadata) for `HEAD:plugins/`; 14 entries, one round-trip.
- GraphQL schema (TreeEntry fields lineCount/language/size): gh-cli-reference: docs_github_com_en_graphql_reference_git.

**search_code content-term constraint** (confirmed via probe runs): `search_code` forwards qualifiers (filename:/extension:/path:/language:) but GitHub code search requires ≥1 free-text content term — a qualifier-only query is rejected. Pure name-only structural find (equivalent to `find -name`) is not achievable via `search_code`. Scope: default branch only, files <384KB, rate-limited to 10 req/min.

## Offene Fragen

- Should `list_issues` expose a `--page` parameter? Currently paginates internally; no `--page` param exposed.

## Quellen

None indexed.
