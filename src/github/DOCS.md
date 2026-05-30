# src/github/

## Role

13 tool modules (9 visible REST, 2 internal REST helpers, 1 GraphQL internal helper, 1 RAG-indexing discussion module) plus 2 infrastructure modules. Each tool module follows INFRASTRUCTURE → ORCHESTRATOR → FUNCTIONS layout; the orchestrator (`<tool>_workflow()`) is the single entry point called by `cli.py` (or by `index_issues.py`/`index_discussions.py` for the internal helpers). Infrastructure modules provide shared auth and HTTP primitives. Touch this package when adding, modifying, or debugging a tool; the only coupling to the delivery layer is the `list[TextContent]` return contract.

## Public Interface

`__init__.py` is empty — no package-level exports. `cli.py` imports each tool directly: `from src.github.<module> import <module>_workflow`. No other callers outside `src/github/` exist except `grep_file.py`, `grep_repo.py` (cross-module internal imports documented per module below).

## Flow

1. `cli.py` calls `<tool>_workflow(params)`
2. Fetch function builds URL + headers, calls GitHub API (REST or GraphQL)
3. Format function parses raw JSON → human-readable text string
4. Workflow wraps string in `TextContent`, returns `list[TextContent]`

## Modules

### client.py (62 LOC)

**Purpose:** REST infrastructure — auth token resolution, API base URL, shared request headers.
**Reads:** `~/.zshrc` (last `export GH_TOKEN=` line via `_read_zshrc_token()`); `os.environ["GH_TOKEN"]`; `os.environ["GITHUB_TOKEN"]`. Resolves at module-import time.
**Writes:** exports `GITHUB_TOKEN` (str), `GITHUB_API_BASE` (str), `RESULTS_PER_PAGE` (int); `build_headers()` returns headers dict.
**Called by:** all 12 REST tool modules (import `build_headers`, `GITHUB_API_BASE`, `RESULTS_PER_PAGE`); `graphql_client.py` (imports `GITHUB_TOKEN`).
**Calls out:** stdlib only (`os`, `re`, `pathlib`).

---

### graphql_client.py (29 LOC)

**Purpose:** GraphQL infrastructure — single HTTP POST wrapper for GitHub GraphQL API v4.
**Reads:** `GITHUB_TOKEN` from `client.py`; accepts query string + variables dict from caller.
**Writes:** returns `data` dict from response; raises on HTTP errors or GraphQL `errors` key.
**Called by:** `get_discussion.py`, `index_discussions.py`.
**Calls out:** `requests`.

---

### search_repos.py (102 LOC)

**Purpose:** Search GitHub repositories by keyword using the Search Repositories API.
**Reads:** GitHub Search API (`/search/repositories`). Enforces `MAX_QUERY_WORDS=3` (long queries return 0 results from GitHub).
**Writes:** returns `list[TextContent]` — up to 20 repos with name, description, stars, forks, language, URL.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

---

### search_code.py (85 LOC)

**Purpose:** Search code across GitHub using the Code Search API with text-match metadata.
**Reads:** GitHub Search Code API (`/search/code`) with `text-match` accept header for code fragments.
**Writes:** returns `list[TextContent]` — up to 20 matches with file paths and code fragments. Appends NOTE when 0 results (GitHub does not index CSV/data files).
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

---

### get_repo.py (57 LOC)

**Purpose:** Retrieve repository metadata including topics and license.
**Reads:** GitHub Repos API (`/repos/{owner}/{repo}`).
**Writes:** returns `list[TextContent]` — stars, description, language, topics, license, open issues, default branch, URL.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

---

### get_repo_tree.py (164 LOC)

**Purpose:** Traverse repository file tree with depth limiting and glob-pattern file search.
**Reads:** GitHub Repos API (default branch), Git Trees API (`/git/trees`), Contents API (for sub-path SHA resolution).
**Writes:** returns `list[TextContent]` — directory/file listing (browse mode) or pattern matches (search mode). Warns when GitHub API tree is truncated (>100k entries) or output exceeds `MAX_TREE_CHARS`.
**Called by:** `cli.py`; `grep_repo.py` (imports `fetch_default_branch`, `get_tree_sha`, `fetch_tree`, `filter_by_pattern`).
**Calls out:** `requests`, `mcp.types`.

---

### get_file_content.py (104 LOC)

**Purpose:** Retrieve and decode file content from a repository with optional line range and metadata-only mode.
**Reads:** GitHub Contents API (`/contents/{path}`). Decodes base64 content.
**Writes:** returns `list[TextContent]` — file metadata + content (or metadata only); directory entry counts when path is a directory.
**Called by:** `cli.py`; `grep_file.py` (imports `fetch_file_content`, `decode_content`); `grep_repo.py` (imports `fetch_file_content`, `decode_content`).
**Calls out:** `requests`, `mcp.types`.

---

### grep_file.py (83 LOC)

**Purpose:** Regex search within a single file, returning matching lines with optional context.
**Reads:** file content via `fetch_file_content()` + `decode_content()` from `get_file_content.py`.
**Writes:** returns `list[TextContent]` — matching lines with line numbers, context lines marked with `>` / ` `.
**Called by:** `cli.py`; `grep_repo.py` (imports `search_lines`).
**Calls out:** `mcp.types`; imports from `get_file_content.py`.

---

### grep_repo.py (81 LOC)

**Purpose:** Regex search across multiple files in a repository, combining tree traversal with per-file content search.
**Reads:** repository tree via imports from `get_repo_tree.py`; file content via imports from `get_file_content.py`; regex matching via `search_lines` from `grep_file.py`.
**Writes:** returns `list[TextContent]` — per-file match results with line numbers; lists files without matches.
**Called by:** `cli.py`.
**Calls out:** `mcp.types`; imports from `get_repo_tree.py`, `get_file_content.py`, `grep_file.py`.

---

### get_issue.py (53 LOC)

**Purpose:** Retrieve full issue details including body.
**Reads:** GitHub Issues API (`/issues/{number}`).
**Writes:** returns `list[TextContent]` — title, state, author, dates, labels, comment count, body.
**Called by:** `index_issues.py` (imports `get_issue_workflow`). Internal-only helper — no CLI subcommand.
**Calls out:** `requests`, `mcp.types`.

---

### get_issue_comments.py (51 LOC)

**Purpose:** Retrieve all comments on a GitHub issue.
**Reads:** GitHub Issue Comments API (`/issues/{number}/comments`).
**Writes:** returns `list[TextContent]` — comment count, each comment with author, date, body.
**Called by:** `index_issues.py` (imports `get_issue_comments_workflow`). Internal-only helper — no CLI subcommand.
**Calls out:** `requests`, `mcp.types`.

---

### index_issues.py (190 LOC)

**Purpose:** Fetch GitHub issues matching a query, strip noise, write per-issue MDs, and index into the `github_issues` RAG collection. Keyword-fallback loop (3→2→1) ensures a non-empty result set.
**Reads:** GitHub Search Issues API + `get_issue_workflow` + `get_issue_comments_workflow` in-process; globs `RAG_DOC_DIR/*.md` for MD count; `rag-cli list_collections` for chunk total.
**Writes:** per-issue MDs to `RAG_DOC_DIR` as `<repo_basename>__<num>.md` (overwrite); invokes `workflow.py index-dir` via subprocess (RAG venv); returns `list[TextContent]` summary.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`; imports from `get_issue.py`, `get_issue_comments.py`.

---

### list_releases.py (65 LOC)

**Purpose:** List releases in a repository with version tags and changelog previews.
**Reads:** GitHub Releases API (`/releases`) with `per_page` param.
**Writes:** returns `list[TextContent]` — tag, name, date, prerelease/draft flags, asset count, 300-char changelog preview.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

---

### get_release.py (61 LOC)

**Purpose:** Retrieve a single release with full release notes. Supports latest or specific tag.
**Reads:** GitHub Releases API — `/releases/latest` (no tag) or `/releases/tags/{tag}`.
**Writes:** returns `list[TextContent]` — tag, name, date, prerelease status, full Markdown body, assets with sizes.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

---

### get_discussion.py (139 LOC)

**Purpose:** Retrieve a full discussion with comments, accepted answer, and configurable comment sort. Internal-only fetch helper for `index_discussions.py`.
**Reads:** GitHub GraphQL API via `graphql_query()` — discussion by number with body, answer, comments, and nested replies.
**Writes:** returns `list[TextContent]` — title, category, author, upvotes, body, accepted answer section, sorted/limited comments with `[ANSWER]` tag.
**Called by:** `index_discussions.py` (imports `get_discussion_workflow`). Internal-only helper — no CLI subcommand.
**Calls out:** `mcp.types`; imports from `graphql_client.py`.

---

### index_discussions.py (185 LOC)

**Purpose:** Fetch GitHub discussions matching a query, strip noise, redact tokens, write per-discussion MDs, and index into the `github_discussions` RAG collection. Keyword-fallback loop (3→2→1); Accepted-Answer dedup removes in-list `[ANSWER]` copy while keeping `### Accepted Answer` block.
**Reads:** GitHub GraphQL Search API (repo-scoped `search(type:DISCUSSION)`) + `get_discussion_workflow()` in-process; globs `RAG_DOC_DIR/*.md` for MD count; `rag-cli list_collections` for chunk total.
**Writes:** per-discussion MDs to `RAG_DOC_DIR` as `<repo_basename>__<num>.md` (overwrite); invokes `workflow.py index-dir` via subprocess (RAG venv); returns `list[TextContent]` summary.
**Called by:** `cli.py`.
**Calls out:** `mcp.types`; imports from `graphql_client.py`, `get_discussion.py`.
