# Tool Design

## Status Quo (IST)

- 13 tools registered in `cli.py` (argparse subcommands); 6 are query/research tools (search_repos, search_code, get_repo_tree, get_file_content, list_releases, get_release), 2 (`index_issues`, `index_discussions`) are RAG-indexing commands, 3 are issue write commands (`create_issue`, `update_issue`, `delete_issue`), 2 are issue read commands (`list_issues`, `get_issue`)
- `get_issue` exposed as CLI subcommand (owner/repo/number → title/state/body); also called internally by `index_issues.py`
- `get_issue_comments` retained as internal-only helper of `index_issues.py`; no subcommand (not CLI-accessible directly)
- `get_discussion` retained as internal helper of `index_discussions.py`; no subcommand (not CLI-accessible directly)
- `grep_file`, `grep_repo` removed from surface; files deleted from `src/github/`. Client-side grep tools with no own GitHub API endpoint; `search_code` covers the research use-case
- `comment_issue` removed from surface (file deleted)
- `get_repo` removed from surface (file deleted) — no use-case
- `search_items`, `list_commits`, `compare_commits`, `search_discussions`, `list_discussions` removed from CLI surface; module files deleted from `src/github/`
- Query truncation: `search_repos`, `index_issues`, `index_discussions` all cap at 3 keywords with 3→2→1 fallback (drop from back until `total_count > 0`; `search_repos` hard-truncate removed)
- Output: `search_repos` emits one line per repo (`full_name stars`, plain integer); `search_code` emits `full_name path` locator + full untruncated fragment(s) indented; decorative headers removed from both
- Pagination: `search_repos` uses `SEARCH_REPOS_PER_PAGE=30` (local constant in `search_repos.py`); `search_code` uses `SEARCH_CODE_PER_PAGE=30` (local constant in `search_code.py`); shared pagination constant removed from `client.py` (no remaining users); `list_releases` exposes page-based pagination via `--page` param (GitHub `/releases` API supports `page` natively; `per_page` clamped to 100)
- `get_file_content` supports `offset`/`limit` for line-range reads and `metadata_only` mode; implementation: `GET /repos/{o}/{r}/contents/{path}` + base64 decode
- `get_repo_tree` supports `depth` filtering and `pattern` glob matching; implementation: 3-REST chain (default-branch → SHA → `GET /git/trees?recursive=1`) returning the full recursive tree in one payload

## Evidenz

No benchmarks run. Query truncation added after observing GitHub Search returning 0 results for multi-word queries.

**GraphQL traversal probes** (`dev/repo_exploration/`):
- Script: `probe_graphql_explore.py` — GraphQL one-shot depth=1 tree traversal; production shape (tree-only, metadata-on-root, single expression param).
- Root call output: `raw_results/graphql_explore.md` — metadata block + 17-entry root tree for `anthropics/claude-code`; one round-trip.
- Sub-path call output: `raw_results/graphql_plugins.md` — tree-only (no metadata) for `HEAD:plugins/`; 14 entries, one round-trip.
- GraphQL schema (TreeEntry fields lineCount/language/size): gh-cli-reference: docs_github_com_en_graphql_reference_git.

**search_code content-term constraint** (confirmed via probe runs): `search_code` forwards qualifiers (filename:/extension:/path:/language:) but GitHub code search requires ≥1 free-text content term — a qualifier-only query is rejected. Pure name-only structural find (equivalent to `find -name`) is not achievable via `search_code`. Scope: default branch only, files <384KB, rate-limited to 10 req/min.

## Recommendation (SOLL)

**Change — `get_repo_tree` → GraphQL one-level traversal tool:**
Replace `get_repo_tree` (3-REST recursive full-tree) with a GraphQL one-shot depth=1 directory-traversal tool. Shape: tree-only (no blob reading), depth=1 always, metadata block on root expression only, per-entry fields name/type/language/lineCount/size, single agent-exposed param (path/expression). `get_file_content` unchanged.

Recursive find-by-name (`get_repo_tree --pattern`) dropped — non-need (agent traverses structurally; `search_code` with a content term covers the remainder; pure name-only search is a GitHub API gap, not a tool gap).

Migration deferred: `src/` port + skill-description update for the traversal strategy are a separate green-lit step. IST remains reality until that step is complete.

## Offene Fragen

- Is 3-keyword cap optimal or too aggressive? → **Resolved for `search_repos`**: 3-word cap retained; hard-truncate replaced by 3→2→1 fallback so narrow trailing keywords no longer block results.
- Should pagination be exposed as a tool parameter (page number)? → **Resolved for `list_releases`**: yes, page-based (`--page`). Other tools TBD.

## Quellen

None indexed.
