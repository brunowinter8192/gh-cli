# src/github/

## Role

17 tool modules (14 REST, 3 GraphQL) plus 2 infrastructure modules. Each tool module follows INFRASTRUCTURE → ORCHESTRATOR → FUNCTIONS layout; the orchestrator (`<tool>_workflow()`) is the single entry point called by `cli.py`. Infrastructure modules provide shared auth and HTTP primitives. Touch this package when adding, modifying, or debugging a tool; the only coupling to the delivery layer is the `list[TextContent]` return contract.

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
**Called by:** all 14 REST tool modules (import `build_headers`, `GITHUB_API_BASE`, `RESULTS_PER_PAGE`); `graphql_client.py` (imports `GITHUB_TOKEN`).
**Calls out:** stdlib only (`os`, `re`, `pathlib`).

---

### graphql_client.py (29 LOC)

**Purpose:** GraphQL infrastructure — single HTTP POST wrapper for GitHub GraphQL API v4.
**Reads:** `GITHUB_TOKEN` from `client.py`; accepts query string + variables dict from caller.
**Writes:** returns `data` dict from response; raises on HTTP errors or GraphQL `errors` key.
**Called by:** `search_discussions.py`, `list_discussions.py`, `get_discussion.py`.
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

### search_items.py (92 LOC)

**Purpose:** Search GitHub issues or PRs using the Search Issues API with type qualifier.
**Reads:** GitHub Search Issues API (`/search/issues`) with `is:issue` or `is:pr` qualifier injected.
**Writes:** returns `list[TextContent]` — up to 20 items with number, title, state (MERGED detection for PRs), author, labels, URL.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

---

### get_issue.py (53 LOC)

**Purpose:** Retrieve full issue details including body.
**Reads:** GitHub Issues API (`/issues/{number}`).
**Writes:** returns `list[TextContent]` — title, state, author, dates, labels, comment count, body.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

---

### get_issue_comments.py (51 LOC)

**Purpose:** Retrieve all comments on a GitHub issue.
**Reads:** GitHub Issue Comments API (`/issues/{number}/comments`).
**Writes:** returns `list[TextContent]` — comment count, each comment with author, date, body.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

---

### list_commits.py (64 LOC)

**Purpose:** List commits in a repository with optional filters for branch, file path, and author.
**Reads:** GitHub Commits API (`/commits`) with optional `sha`, `path`, `author`, `per_page` params.
**Writes:** returns `list[TextContent]` — short SHA, commit message (first line), author, date, URL per commit.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

---

### compare_commits.py (72 LOC)

**Purpose:** Compare two branches, tags, or SHAs showing commits and file changes between them.
**Reads:** GitHub Compare API (`/compare/{base}...{head}`).
**Writes:** returns `list[TextContent]` — status, ahead/behind counts, commit list (max 20), files changed (max 30) with status icons and diff stats.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

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

### search_discussions.py (79 LOC)

**Purpose:** Search GitHub Discussions across all repositories using GraphQL Search API.
**Reads:** GitHub GraphQL API via `graphql_query()` (`graphql_client.py`) — `search(type: DISCUSSION)`.
**Writes:** returns `list[TextContent]` — discussion count, title, category, repository, author, comment count, upvotes, answered status, URL.
**Called by:** `cli.py`.
**Calls out:** `mcp.types`; imports from `graphql_client.py`.

---

### list_discussions.py (127 LOC)

**Purpose:** List discussions in a specific repository with optional category and answered filters.
**Reads:** GitHub GraphQL API via `graphql_query()` — repository discussions ordered by UPDATED_AT DESC; optionally queries `discussionCategories` to resolve category slug to ID.
**Writes:** returns `list[TextContent]` — title, category, author, comment count, upvotes, answered status, update date, discussion number.
**Called by:** `cli.py`.
**Calls out:** `mcp.types`; imports from `graphql_client.py`.

---

### get_discussion.py (139 LOC)

**Purpose:** Retrieve a full discussion with comments, accepted answer, and configurable comment sort.
**Reads:** GitHub GraphQL API via `graphql_query()` — discussion by number with body, answer, comments, and nested replies.
**Writes:** returns `list[TextContent]` — title, category, author, upvotes, body, accepted answer section, sorted/limited comments with `[ANSWER]` tag.
**Called by:** `cli.py`.
**Calls out:** `mcp.types`; imports from `graphql_client.py`.
