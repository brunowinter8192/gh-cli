# grep_file + grep_repo Removal

`grep_file.py` and `grep_repo.py` removed from `src/github/` and from the CLI surface. This closes the grep_repo replace-vs-fix question as REMOVE.

## What they were

- `grep_file`: fetched a single file via `get_file_content.fetch_file_content()`, then applied Python `re` pattern matching over the decoded lines. No own GitHub API endpoint — pure client-side regex over a `get_file_content` fetch.
- `grep_repo`: fetched the repo tree via `get_repo_tree` helpers (`fetch_default_branch`, `get_tree_sha`, `fetch_tree`, `filter_by_pattern`), then iterated matching files with `get_file_content.fetch_file_content()` + `grep_file.search_lines()`. No own GitHub API endpoint. A manual crawl composed from two other tools' internals.

## Why removed

**No own endpoint.** Both tools are client-side composites wrapping helpers from `get_repo_tree.py` and `get_file_content.py`. The real GitHub search capability is `search_code` (server-side indexed full-text search). Keeping grep_file/grep_repo as CLI commands implied parity with search_code — they are not; they fetch content first, then grep locally.

**search_code supersedes for the research use-case.** The skill's purpose is foreign-repo research. For "find this pattern in repo X", `search_code "pattern repo:owner/repo"` hits GitHub's pre-built index in one API call and returns ranked results with file paths. grep_repo fetches tree + N files + greps locally — more API calls, slower, and has a known false-negative failure mode (returned "No matches" with 50/50 files searched while search_code found 6 hits for the identical term in the same repo, confirmed 2026-05-30).

**Dead helper check.** After deletion: `fetch_file_content` and `decode_content` (from `get_file_content.py`) remain active — used by `get_file_content_workflow` itself. `fetch_default_branch`, `get_tree_sha`, `fetch_tree`, `filter_by_pattern` (from `get_repo_tree.py`) remain active — used by `get_repo_tree_workflow` itself. Zero orphaned helpers.

**Stale output text cleaned.** `search_code.py` NOTE text that recommended `grep_file`/`grep_repo` as a fallback updated to `get_file_content`.
