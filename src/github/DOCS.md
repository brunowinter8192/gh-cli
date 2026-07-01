# src/github/

## Role

21 modules: 16 tool modules (14 visible CLI subcommands: 11 REST + 3 GraphQL; 1 internal REST helper `get_issue_comments`; 1 internal GraphQL helper `get_discussion`), 2 cleaning/utility modules (`text_cleaning`, `discussion_cleaning`), and 3 infrastructure modules (`client`, `graphql_client`, `repo_counts`). Each tool module follows INFRASTRUCTURE → ORCHESTRATOR → FUNCTIONS layout; the orchestrator (`<tool>_workflow()`) is the single entry point called by `cli.py` (or by `index_issues.py`/`index_discussions.py` for the internal helpers). Infrastructure modules provide shared auth and HTTP primitives. Touch this package when adding, modifying, or debugging a tool; the only coupling to the delivery layer is the `list[TextContent]` return contract.

## Public Interface

`__init__.py` is empty — no package-level exports. `cli.py` imports each tool directly: `from src.github.<module> import <module>_workflow`. Cross-module imports within `src/github/` are documented per module below.

## Flow

1. `cli.py` calls `<tool>_workflow(params)`
2. Fetch function builds URL + headers, calls GitHub API (REST or GraphQL)
3. Format function parses raw JSON → human-readable text string
4. Workflow wraps string in `TextContent`, returns `list[TextContent]`

## Modules

### client.py (70 LOC)

**Purpose:** REST infrastructure — auth token resolution, API base URL, shared request headers, generic HTTP helper.
**Reads:** `~/.zshrc` (last `export GH_TOKEN=` line via `_read_zshrc_token()`); `os.environ["GH_TOKEN"]`; `os.environ["GITHUB_TOKEN"]`. Resolves at module-import time.
**Writes:** exports `GITHUB_TOKEN` (str), `GITHUB_API_BASE` (str); `build_headers()` returns headers dict; `request(method, path, json, params)` executes any HTTP method and returns parsed JSON.
**Called by:** all 12 REST modules (11 visible subcommands + `get_issue_comments`; read modules import `build_headers`/`GITHUB_API_BASE`; write/list modules use `request()`); `graphql_client.py` (imports `GITHUB_TOKEN`); `repo_counts.py` (imports `GITHUB_TOKEN` transitively via `graphql_client.py`).
**Calls out:** `requests`; stdlib (`os`, `re`, `pathlib`).

---

### graphql_client.py (30 LOC)

**Purpose:** GraphQL infrastructure — single HTTP POST wrapper for GitHub GraphQL API v4.
**Reads:** `GITHUB_TOKEN` from `client.py`; accepts query string + variables dict from caller.
**Writes:** returns `data` dict from response; raises on HTTP errors or GraphQL `errors` key.
**Called by:** `repo_counts.py`, `get_discussion.py`, `index_discussions.py`, `delete_issue.py`, `get_repo_tree.py`.
**Calls out:** `requests`.

---

### repo_counts.py (51 LOC)

**Purpose:** Shared GraphQL enrichment helper — fetches star/issue/discussion counts for a list of repos in one batched aliased query.
**Reads:** GitHub GraphQL API via `graphql_query()` — `stargazerCount`, `issues{totalCount}`, `discussions{totalCount}`, `hasIssuesEnabled`, `hasDiscussionsEnabled` per repo; all repos in one HTTP call via field aliases (`r0`, `r1`, …).
**Writes:** `fetch_repo_counts(repos)` returns `{full_name: counts_dict | None}` (None when repo is deleted/renamed between search and enrichment); `format_count_line(full_name, stars, counts)` returns formatted string `"owner/repo · ⭐N · issues:N · discussions:M"` with `(off)` suffix when feature disabled.
**Called by:** `search_repos.py`, `search_code.py`.
**Calls out:** imports `graphql_query` from `graphql_client.py`.

---

### search_repos.py (59 LOC)

**Purpose:** Search GitHub repositories by keyword using the Search Repositories API; enrich results with per-repo issue/discussion counts.
**Reads:** GitHub Search API (`/search/repositories`); `SEARCH_REPOS_PER_PAGE=30` (local); 3→2→1 keyword fallback (drops trailing keywords until `total_count > 0`). Stars from REST `stargazers_count`. Issue/discussion counts + enabled flags from `fetch_repo_counts()` (single batched GraphQL call).
**Writes:** returns `list[TextContent]` — one enriched line per repo: `full_name · ⭐stars · issues:N · discussions:M`; up to 30 results.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`; imports from `repo_counts.py`.

---

### search_code.py (85 LOC)

**Purpose:** Search code across GitHub using the Code Search API with text-match metadata; prepends per-repo issue/discussion summary.
**Reads:** GitHub Search Code API (`/search/code`) with `text-match` accept header; `SEARCH_CODE_PER_PAGE=30` (local); up to 3 full untruncated fragments per match. Stars + issue/discussion counts from `fetch_repo_counts()` (single batched GraphQL call on unique repos; REST /search/code returns only a minimal repo stub without star count).
**Writes:** returns `list[TextContent]` — `## Repos (N unique)` summary block (one enriched line per unique repo) followed by per-hit `full_name path` + fragment(s); single-line note on 0 results.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`; imports from `repo_counts.py`.

---

### get_repo_tree.py (114 LOC)

**Purpose:** One-level directory traversal of a repository tree via GraphQL one-shot. depth=1 always; tree-only (no blob reading).
**Reads:** GitHub GraphQL API (`repository.object(expression)` → `Tree.entries`); per-entry fields: name, type, language, lineCount, size. Metadata block (description/primaryLanguage/languages) on root expression only.
**Writes:** returns `list[TextContent]` — metadata block (root only) + tree table; or blob-redirect message; or null-path message.
**Called by:** `cli.py`.
**Calls out:** `mcp.types`; imports `graphql_query` from `graphql_client.py`.

---

### get_file_content.py (168 LOC)

**Purpose:** Retrieve file content from a repository with optional line range and metadata-only mode. Handles three size tiers transparently: ≤1 MB (base64 inline), 1–100 MB (stream to `/tmp`), >100 MB (error).
**Reads:** GitHub Contents API (`/contents/{path}`). Tier dispatch on `size` field: ≤1 MB decodes base64 inline (offset/limit apply); 1–100 MB streams `download_url` to `/tmp/gh-cli_{owner}_{repo}_{path}` via chunked `requests` download (timeout=30 s), returns `/tmp` path for local reading; >100 MB returns an explicit error (GitHub API hard limit).
**Writes:** returns `list[TextContent]` — file metadata + content or /tmp path or error; directory entry counts when path is a directory.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

---

### get_issue.py (50 LOC)

**Purpose:** Retrieve full issue details including body.
**Reads:** GitHub Issues API (`/issues/{number}`).
**Writes:** returns `list[TextContent]` — title, state, author, dates, labels, comment count, body.
**Called by:** `cli.py` (direct CLI subcommand: `gh-cli get_issue owner repo number`); `index_issues.py` (imports `get_issue_workflow` for RAG fetch).
**Calls out:** `requests`, `mcp.types`.

---

### download_files.py (73 LOC)

**Purpose:** Download one or more specific repo files to a local directory — binary-safe, per-path failure isolation (one failure does not abort remaining paths). Flat write: `<dest>/<basename(path)>`.
**Reads:** GitHub Contents API via imported `fetch_file_content()` from `get_file_content.py` — returns dict (file) or list (directory); streams raw bytes via imported `_stream_download(download_url, dest_path)`; validates against imported `_SIZE_API_MAX` (100 MB limit). Failure cases: directory response, `download_url` is None (submodule/symlink), size > 100 MB, HTTP error (404 etc.).
**Writes:** binary files to `<dest>/<basename>` (os.makedirs exist_ok=True before loop); returns `list[TextContent]` — per-path Written (path → dest_path, bytes) and Failed (path → reason) report.
**Called by:** `cli.py` (direct CLI subcommand: `gh-cli download_files owner repo path [path ...] --dest <dir>`).
**Calls out:** `mcp.types`; imports `fetch_file_content`, `_stream_download`, `_SIZE_API_MAX` from `get_file_content.py`; stdlib `os`.

---

### repo_freshness.py (44 LOC)

**Purpose:** Fetch repo metadata and report push freshness — `pushed_at` (last branch push), relative age in whole days, `updated_at`, `created_at`.
**Reads:** GitHub REST API (`GET /repos/{owner}/{repo}`) — fields `full_name`, `pushed_at`, `updated_at`, `created_at`.
**Writes:** returns `list[TextContent]` — `full_name`, pushed timestamp + `(pushed N day(s) ago)` relative age, updated timestamp, created timestamp.
**Called by:** `cli.py` (direct CLI subcommand: `gh-cli repo_freshness owner repo`).
**Calls out:** `requests`, `mcp.types`; stdlib `datetime`.

---

### get_issue_comments.py (51 LOC)

**Purpose:** Retrieve all comments on a GitHub issue.
**Reads:** GitHub Issue Comments API (`/issues/{number}/comments`).
**Writes:** returns `list[TextContent]` — comment count, each comment with author, date, body.
**Called by:** `index_issues.py` (imports `get_issue_comments_workflow`). Internal-only helper — no CLI subcommand.
**Calls out:** `requests`, `mcp.types`.

---

### index_issues.py (196 LOC)

**Purpose:** Fetch GitHub issues matching a query, strip noise, write per-issue MDs, and index into the `github_issues` RAG collection. Keyword-fallback loop (3→2→1) ensures a non-empty result set.
**Reads:** GitHub Search Issues API + `get_issue_workflow` + `get_issue_comments_workflow` in-process; globs `RAG_DOC_DIR/*.md` for MD count; `rag-cli list_collections` for chunk total.
**Writes:** per-issue MDs to `RAG_DOC_DIR` as `<repo_basename>__<num>.md` (overwrite); invokes `rag-cli index` via subprocess; raises `RuntimeError` on non-zero exit (busy/locked detected via stderr, message includes recovery command); returns `list[TextContent]` summary.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`; imports from `get_issue.py`, `get_issue_comments.py`, `text_cleaning.py` (`strip_generic_noise` applied additively after `strip_noise`/`strip_comments_noise`).

---

### index_releases.py (151 LOC)

**Purpose:** Fetch up to 100 releases (newest-first) for a repo, write per-release MDs with noise stripped, and index into the fixed `github_releases` RAG collection. Clean-before-index janitor: delete collection + rmtree doc dir before each run (idempotent).
**Reads:** `GET /repos/{o}/{r}/releases?per_page=100`; globs doc dir for MD count; `rag-cli list_collections` for chunk total.
**Writes:** per-release MDs to `RAG_ROOT/data/documents/github_releases/` as `<tag>.md` (fixed collection, not per-repo path); invokes `rag-cli index` via subprocess; raises `RuntimeError` on non-zero exit from either `delete` (janitor) or `index` — raise is before rmtree so old state stays intact on busy; returns `list[TextContent]` summary with follow-up `rag-cli search_hybrid` command.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`, `shutil`, `subprocess`.

---

### create_issue.py (45 LOC)

**Purpose:** Create a new issue in a repository.
**Reads:** nothing beyond auth.
**Writes:** POST `/repos/{owner}/{repo}/issues` with title, optional body/labels/assignees; returns `list[TextContent]` — issue number + html_url.
**Called by:** `cli.py`.
**Calls out:** `client.request()`, `mcp.types`.

---

### update_issue.py (56 LOC)

**Purpose:** Update an existing issue's title, body, labels, or state (close / reopen).
**Reads:** nothing beyond auth.
**Writes:** PATCH `/repos/{owner}/{repo}/issues/{number}` with only the fields explicitly provided; returns `list[TextContent]` — updated number, title, state, url.
**Called by:** `cli.py`.
**Calls out:** `client.request()`, `mcp.types`.

---

### list_issues.py (64 LOC)

**Purpose:** List repository issues with state filter (default: open). Filters out pull-request entries returned by the REST endpoint.
**Reads:** GET `/repos/{owner}/{repo}/issues` — paginates until `limit` real issues collected.
**Writes:** returns `list[TextContent]` — one line per issue: number, state, title, labels.
**Called by:** `cli.py`.
**Calls out:** `client.request()`, `mcp.types`.

---

### delete_issue.py (47 LOC)

**Purpose:** Permanently delete an issue via the GitHub GraphQL `deleteIssue` mutation. Without `--confirm`, prints what would be deleted and exits safely. With `--confirm`, prints an irreversible-warning to stderr, resolves `node_id` via REST GET, then executes the mutation.
**Reads:** GET `/repos/{owner}/{repo}/issues/{number}` for `node_id` and title.
**Writes:** GraphQL `deleteIssue` mutation (only when `--confirm` passed); returns `list[TextContent]` — dry-run notice or deletion confirmation.
**Called by:** `cli.py`.
**Calls out:** `client.request()`, `graphql_client.graphql_query()`, `mcp.types`.

---

### get_discussion.py (128 LOC)

**Purpose:** Retrieve a full discussion with comments and accepted answer in natural chronological order. Internal-only fetch helper for `index_discussions.py`.
**Reads:** GitHub GraphQL API via `graphql_query()` — discussion by number with body, answer, comments (chronological, up to 100), and nested replies.
**Writes:** returns `list[TextContent]` — title, category, author, upvotes, body, accepted answer section, comments with `[ANSWER]` tag; `comment_limit` default 100 (API per-page max); no re-sorting.
**Called by:** `index_discussions.py` (imports `get_discussion_workflow`). Internal-only helper — no CLI subcommand.
**Calls out:** `mcp.types`; imports from `graphql_client.py`.

---

### text_cleaning.py (30 LOC)

**Purpose:** Generic text noise-strip primitives shared across issue and discussion cleaning. No mcp dependency. Exports `strip_generic_noise(text) -> str` (full-text entry point) and `_strip_line(line) -> str` (per-line helper). Also exports regexes: `IMG_RE` (any HTML `<img\b[^>]*>` tag), `MD_IMG_RE` (any markdown image with non-empty URL `!\[[^\]]*\]\([^)]+\)` — non-empty URL required to avoid matching literal `![]()` code examples in prose), `DATA_URI_RE` (bare base64 data-URIs not inside markdown syntax). Strip order: IMG → MD_IMG → DATA_URI → FAILED_UPLOAD (`!\[Uploading...\]\(\)` empty-URL form, explicit since not subsumed by MD_IMG_RE) → `\S{1000,}` no-space net.
**Reads:** nothing — pure text transform.
**Writes:** returns cleaned string (never mutates argument).
**Called by:** `discussion_cleaning.py` (imports `strip_generic_noise`); `index_issues.py` (imports `strip_generic_noise`, applied additively to body + comments after issue-specific strips).
**Calls out:** stdlib only (`re`).

---

### discussion_cleaning.py (121 LOC)

**Purpose:** Dosu-specific noise-strip module — no mcp dependency. Exports `strip_noise(text) -> str`: 12 sub-categories — DOSU_FOOTER block, DOSU_GREETING 2-line standalone, ISSUE_TEMPLATE_CHECKLIST block, STANDALONE_BADGE_LINE, DOSU_FOOTER_TEXT (blockquoted/email-rendered prose: `'To reply, just mention'` / `'Docs are dead.'` / `'Share context…'` + dosu ref; Chinese: `回复时只需提及` / `已经过时`), DOSU_MARKERLESS_GREETING (`_is_dosu_markerless_greeting()`: after `^[\s>_*]+` + `&nbsp;→space` strip, line starts with `Hi @` / `你好@` / `你好 @` AND contains `Dosu` AND contains `helping`+`team` or `帮助`+`团队`; user-quoted attribution blocks preserved), DOSU_ANSWER_MARKER inline sub, DOSU_GREETING_INLINE sub (`<!-- Answer|Greeting -->` unified); generic image+no-space strips delegated to `strip_generic_noise()` from `text_cleaning.py`. Private helpers `_bare()`, `_is_badge_line()`, `_is_dosu_footer_text_line()`, `_is_dosu_markerless_greeting()` and constants (`FOOTER_LOOKAHEAD`, `_BADGE_DOMAINS`, `_FOOTER_TEXT_PHRASES`, `ISSUE_HEADING_RE`). Safe on raw `get_discussion` output and already-built MDs (does not touch `## ` headings, attribution headers, or metadata lines).
**Reads:** nothing — pure text transform.
**Writes:** returns cleaned string (never mutates argument).
**Called by:** `index_discussions.py` (imports `strip_noise`). Dev copies: `dev/content_cleaning/03_reclean_discussions.py`, `dev/content_cleaning/02_strip_validation.py` (verbatim inline copies — hook `block_dev_imports_src` prevents direct import).
**Calls out:** stdlib only (`re`); imports `strip_generic_noise` from `text_cleaning.py`.

---

### index_discussions.py (190 LOC)

**Purpose:** Fetch GitHub discussions matching a query, strip noise, redact tokens, write per-discussion MDs, and index into the `github_discussions` RAG collection. Keyword-fallback loop (3→2→1). `strip_discussion_noise(text) -> (str, title)` — calls imported `strip_noise()` then applies format logic (title extraction, metadata drop, `[ANSWER]` dedup) on raw `get_discussion` output.
**Reads:** GitHub GraphQL Search API (repo-scoped `search(type:DISCUSSION)`) + `get_discussion_workflow()` in-process; globs `RAG_DOC_DIR/*.md` for MD count; `rag-cli list_collections` for chunk total.
**Writes:** per-discussion MDs to `RAG_DOC_DIR` as `<repo_basename>__<num>.md` (overwrite); invokes `rag-cli index` via subprocess; raises `RuntimeError` on non-zero exit (busy/locked detected via stderr, message includes recovery command); returns `list[TextContent]` summary.
**Called by:** `cli.py`.
**Calls out:** `mcp.types`; imports from `discussion_cleaning.py`, `graphql_client.py`, `get_discussion.py`.
