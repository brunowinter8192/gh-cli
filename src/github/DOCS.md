# src/github/

## Role
GitHub API tool implementations behind `cli.py`'s 15 subcommands, plus the cleaning/utility and infrastructure modules they share. Each tool's `<tool>_workflow()` is its single entry point, returning `list[TextContent]`. Touch this package to add, modify, or debug a tool; infrastructure/cleaning modules are shared, not tool-specific.

## Public Interface
`__init__.py` is empty — no package-level exports. `cli.py` imports each tool directly: `from src.github.<module> import <module>_workflow`. Cross-module imports within `src/github/` are documented per module below.

## Flow
1. `cli.py` calls `<tool>_workflow(params)`
2. Fetch function builds URL + headers, calls GitHub API (REST or GraphQL)
3. Format function parses raw JSON → human-readable text string
4. Workflow wraps string in `TextContent`, returns `list[TextContent]`

## Modules

### config.py (5 LOC)

**Purpose:** Shared RAG-side constants used across the three index modules.
**Reads:** nothing — pure constants.
**Writes:** exports the shared constants.
**Called by:** `index_issues.py`, `index_discussions.py`, `index_releases.py`.
**Calls out:** stdlib (`pathlib`).

---

### client.py (60 LOC)

**Purpose:** REST infrastructure — auth token resolution, API base URL, shared request headers, generic HTTP helper.
**Reads:** `~/.zshrc` and GitHub token env vars, resolved at module-import time.
**Writes:** exports the token, API base URL, header builder and request helper.
**Called by:** all REST tool modules; `graphql_client.py` (imports the token); `repo_counts.py` (transitively).
**Calls out:** `requests`; stdlib (`os`, `re`, `pathlib`).

---

### graphql_client.py (29 LOC)

**Purpose:** GraphQL infrastructure — single HTTP POST wrapper for GitHub GraphQL API v4.
**Reads:** the token from `client.py`; query string + variables from caller.
**Writes:** returns response `data` dict; raises on HTTP errors or GraphQL `errors` key.
**Called by:** `repo_counts.py`, `get_discussion.py`, `index_discussions.py`, `delete_issue.py`, `get_repo_tree.py`.
**Calls out:** `requests`.

---

### repo_counts.py (49 LOC)

**Purpose:** Shared GraphQL enrichment helper — batch star/issue/discussion counts for a list of repos in one call.
**Reads:** GitHub GraphQL API via `graphql_client.py`.
**Writes:** returns a counts dict and a formatted summary line.
**Called by:** `search_repos.py`, `search_code.py`.
**Calls out:** `graphql_client.py`.

---

### search_repos.py (57 LOC)

**Purpose:** Search GitHub repositories by keyword; enrich results with per-repo issue/discussion counts.
**Reads:** GitHub Search Repositories API; keyword fallback on zero results.
**Writes:** returns `list[TextContent]` — one enriched line per repo.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`; `repo_counts.py`.

---

### search_code.py (81 LOC)

**Purpose:** Search code across GitHub with text-match metadata; prepends a per-repo issue/discussion summary.
**Reads:** GitHub Search Code API.
**Writes:** returns `list[TextContent]` — repo summary block plus per-hit fragments.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`; `repo_counts.py`.

---

### get_repo_tree.py (111 LOC)

**Purpose:** One-level directory traversal of a repository tree via a GraphQL one-shot query.
**Reads:** GitHub GraphQL API (`repository.object(expression)`).
**Writes:** returns `list[TextContent]` — metadata block (root only) plus tree table, or a redirect/error message.
**Called by:** `cli.py`.
**Calls out:** `mcp.types`; `graphql_client.py`.

---

### get_file_content.py (159 LOC)

**Purpose:** Retrieve file content with optional line range and metadata-only mode across three file-size tiers.
**Reads:** GitHub Contents API.
**Writes:** returns `list[TextContent]` — inline content, a streamed `/tmp` path, or an error, depending on size.
**Called by:** `cli.py`; `download_files.py` (imports its fetch/stream helpers).
**Calls out:** `requests`, `mcp.types`.

---

### get_issue.py (48 LOC)

**Purpose:** Retrieve full issue details including body.
**Reads:** GitHub Issues API.
**Writes:** returns `list[TextContent]`.
**Called by:** `cli.py`; `index_issues.py` (imports the workflow).
**Calls out:** `requests`, `mcp.types`.

---

### download_files.py (71 LOC)

**Purpose:** Download one or more repo files to a local directory, binary-safe, per-path failure isolation.
**Reads:** GitHub Contents API via `get_file_content.py` helpers.
**Writes:** files to `<dest>/<basename>`; returns `list[TextContent]` written/failed report.
**Called by:** `cli.py`.
**Calls out:** `mcp.types`; `get_file_content.py`.

---

### repo_freshness.py (42 LOC)

**Purpose:** Fetch repo metadata and report push freshness (pushed/updated/created timestamps).
**Reads:** GitHub REST API (`GET /repos/{owner}/{repo}`).
**Writes:** returns `list[TextContent]`.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`.

---

### trending.py (274 LOC)

**Purpose:** List GitHub Trending repositories or developers by scraping the trending HTML page, with language, date-range and spoken-language filters.
**Reads:** `https://github.com/trending[/developers][/<language>]` HTML (no API exists); unauthenticated.
**Writes:** returns `list[TextContent]` — header line plus one entry per repo/developer; raises on zero entries or unmatched markup.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`; stdlib `html.parser`.

---

### get_issue_comments.py (49 LOC)

**Purpose:** Retrieve all comments on a GitHub issue.
**Reads:** GitHub Issue Comments API.
**Writes:** returns `list[TextContent]`.
**Called by:** `index_issues.py` (imports the workflow). Internal-only helper — no CLI subcommand.
**Calls out:** `requests`, `mcp.types`.

---

### index_issues.py (262 LOC)

**Purpose:** Fetch GitHub issues matching a query, strip noise, write per-issue MDs, and index into the `github_issues` RAG collection.
**Reads:** GitHub Search Issues API; the issue and comment workflows in-process; existing MD count; `rag-cli list_collections`.
**Writes:** per-issue MDs; raw pre-strip fetch log; invokes `rag-cli index`; returns `list[TextContent]` summary.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`; `get_issue.py`, `get_issue_comments.py`, `text_cleaning.py`, `raw_logging.py`, `config.py`.

---

### raw_logging.py (32 LOC)

**Purpose:** Write each issue's raw, unfiltered fetch text before any cleaning strip runs, paired by filename with the cleaned MD.
**Reads:** nothing — receives already-fetched raw text from its caller.
**Writes:** `logs/raw_issues/<file>.md` plus a manifest line; never raises on write failure.
**Called by:** `index_issues.py` .
**Calls out:** stdlib only (`json`, `logging`, `datetime`, `pathlib`).

---

### index_releases.py (141 LOC)

**Purpose:** Fetch releases for a repo, write per-release MDs, and index into the fixed `github_releases` RAG collection.
**Reads:** `GET /repos/{o}/{r}/releases`; existing MD count; `rag-cli list_collections`.
**Writes:** per-release MDs (collection wiped and rebuilt each run); invokes `rag-cli index`; returns `list[TextContent]`.
**Called by:** `cli.py`.
**Calls out:** `requests`, `mcp.types`, `shutil`, `subprocess`; `config.py`.

---

### create_issue.py (45 LOC)

**Purpose:** Create a new issue in a repository.
**Reads:** nothing beyond auth.
**Writes:** POST to the Issues API; returns `list[TextContent]`.
**Called by:** `cli.py`.
**Calls out:** `client.py`, `mcp.types`.

---

### update_issue.py (56 LOC)

**Purpose:** Update an existing issue's title, body, labels, or state.
**Reads:** nothing beyond auth.
**Writes:** PATCH to the Issues API; returns `list[TextContent]`.
**Called by:** `cli.py`.
**Calls out:** `client.py`, `mcp.types`.

---

### list_issues.py (63 LOC)

**Purpose:** List repository issues with a state filter, excluding pull requests returned by the REST endpoint.
**Reads:** `GET /repos/{owner}/{repo}/issues`, paginated.
**Writes:** returns `list[TextContent]`.
**Called by:** `cli.py`.
**Calls out:** `client.py`, `mcp.types`.

---

### delete_issue.py (47 LOC)

**Purpose:** Permanently delete an issue via the GraphQL `deleteIssue` mutation; dry-run notice without `--confirm`.
**Reads:** `GET /repos/{owner}/{repo}/issues/{number}` for `node_id`.
**Writes:** GraphQL mutation (only when confirmed); returns `list[TextContent]`.
**Called by:** `cli.py`.
**Calls out:** `client.py`, `graphql_client.py`, `mcp.types`.

---

### get_discussion.py (126 LOC)

**Purpose:** Retrieve a full discussion with comments and accepted answer in chronological order.
**Reads:** GitHub GraphQL API.
**Writes:** returns `list[TextContent]`.
**Called by:** `index_discussions.py` (imports the workflow). Internal-only helper — no CLI subcommand.
**Calls out:** `mcp.types`; `graphql_client.py`.

---

### text_cleaning.py (134 LOC)

**Purpose:** Generic text noise-strip primitives shared across issue and discussion cleaning, plus build/install-tool log detection.
**Reads:** nothing — pure text transform.
**Writes:** returns cleaned string (never mutates its argument).
**Called by:** `discussion_cleaning.py` (imports the generic strip); `index_issues.py` (imports the generic and build-log strips).
**Calls out:** stdlib only (`re`).

---

### discussion_cleaning.py (126 LOC)

**Purpose:** Dosu-bot noise-strip module for discussion text — footers, greetings, template checklists, badges.
**Reads:** nothing — pure text transform.
**Writes:** returns cleaned string (never mutates its argument).
**Called by:** `index_discussions.py` (imports the noise strip). Dev copies exist in `dev/content_cleaning/`.
**Calls out:** stdlib only (`re`); `text_cleaning.py`.

---

### index_discussions.py (177 LOC)

**Purpose:** Fetch GitHub discussions matching a query, strip noise, redact tokens, write per-discussion MDs, and index into the `github_discussions` RAG collection.
**Reads:** GitHub GraphQL Search API; the discussion workflow in-process; existing MD count; `rag-cli list_collections`.
**Writes:** per-discussion MDs; invokes `rag-cli index`; returns `list[TextContent]` summary.
**Called by:** `cli.py`.
**Calls out:** `mcp.types`; `discussion_cleaning.py`, `graphql_client.py`, `get_discussion.py`, `config.py`.

---

## State
`client.py` owns the GitHub token, resolved once at import and never mutated. Read by all REST modules through the client helpers and by `graphql_client.py` directly (`repo_counts.py` transitively). No other cross-module state.
