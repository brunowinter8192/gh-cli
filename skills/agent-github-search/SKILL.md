---
name: agent-github-search
description: GitHub MCP tool reference for search agents
---

# GitHub MCP Tools — Reference

## Tools by Category

### Discovery

| Tool | Purpose |
|------|---------|
| search_repos | Find repositories by topic, technology, or keyword |
| search_code | Find code patterns or usage examples across GitHub |
| get_repo | Read repository metadata (stars, topics, license) |

### Repository Exploration

| Tool | Purpose |
|------|---------|
| get_repo_tree | Browse directory structure, search files by glob pattern |
| get_file_content | Read file content, metadata, or directory listing |

### Content Search

| Tool | Purpose |
|------|---------|
| grep_file | Search within a single file by regex |
| grep_repo | Search across multiple files in a repo by regex + file glob |

### Issues & PRs

| Tool | Purpose |
|------|---------|
| search_items | Find issues or PRs across GitHub |
| get_issue | Read full issue with body |
| get_issue_comments | Read issue discussion thread |
| list_repo_prs | List PRs in a repository |
| get_pr | Read full PR with body and stats |
| get_pr_files | List changed files in a PR |

### Discussions

| Tool | Purpose |
|------|---------|
| search_discussions | Find discussions across GitHub |
| list_discussions | Browse discussions in a specific repo |
| get_discussion | Read full discussion with comments |

### Commits & Releases

| Tool | Purpose |
|------|---------|
| list_commits | Browse commit history, find when a file changed |
| compare_commits | See diff between two branches, tags, or SHAs |
| list_releases | List all releases with changelogs |
| get_release | Read full release notes for a specific tag |

## Parameter Reference

### search_repos

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| query | str | required | Search query with GitHub qualifiers (e.g., "fastapi stars:>1000") |
| sort_by | stars/forks/updated/best_match | best_match | Sort order |

### search_code

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| query | str | required | Code search with qualifiers (e.g., "def workflow language:python") |

### get_repo_tree

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| path | str | "" | Subdirectory scope (reduces truncation risk) |
| depth | int | -1 | Tree depth limit (-1=unlimited, 1=direct children only) |
| pattern | str | "" | Glob pattern for file search (e.g., "\*config\*", "\*.py") |

### get_file_content

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| path | str | required | File or directory path |
| metadata_only | bool | False | Return only metadata (no content download) |
| offset | int | 0 | Start reading from this line number |
| limit | int | 0 | Number of lines to return (0=all) |

### grep_file

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| path | str | required | File path to search |
| pattern | str | required | Regex pattern |
| context_lines | int | 0 | Lines of context around matches |
| max_matches | int | 50 | Maximum matches to return |

### grep_repo

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| pattern | str | required | Regex pattern to search in file content |
| file_pattern | str | "\*" | Glob pattern for file selection |
| path | str | "" | Subdirectory scope (narrows search, avoids truncation) |
| max_files | int | 10 | Max files to search (server enforces min 20) |

### search_items

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| query | str | required | Search query with qualifiers |
| type | "issue"/"pr" | required | Item type to search |
| sort_by | comments/reactions/created/updated/best_match | best_match | Sort order |

**Empty result handling:** Response < 100 chars = 0 results found.
- The topic does NOT exist in that repo as an issue/PR — do NOT retry with synonyms on the same repo
- NEVER repeat the exact same query in the same session
- Pivot immediately: use `search_code`, `grep_repo`, or read the relevant docs file directly

### get_issue / get_issue_comments

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| issue_number | int | required | Issue number |

### list_repo_prs

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| state | open/closed/all | open | PR state filter |
| sort_by | created/updated/popularity/long-running | created | Sort order |

### get_pr / get_pr_files

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| pull_number | int | required | PR number |

### get_repo

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |

### search_discussions

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| query | str | required | Search query |
| first | int | 10 | Max results to return |

### list_discussions

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| first | int | 10 | Max results |
| category | str/null | null | Filter by category slug |
| answered | bool/null | null | Filter by answered status |

### get_discussion

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| number | int | required | Discussion number |
| comment_limit | int | 50 | Max comments to return |
| comment_sort | upvotes/chronological | upvotes | Comment sort order |

### list_commits

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| sha | str | "" | Branch or commit SHA to start from |
| path | str | "" | Only commits touching this file path |
| author | str | "" | Filter by author login |
| per_page | int | 20 | Number of commits to return |

### compare_commits

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| base | str | required | Base branch, tag, or SHA |
| head | str | required | Head branch, tag, or SHA |

### list_releases

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| per_page | int | 10 | Number of releases to return |

### get_release

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| tag | str/null | null | Release tag (e.g., "v2.0.0") — omit for latest release |

## Search Qualifiers

GitHub search supports qualifiers in query strings:

| Qualifier | Example | Applies to |
|-----------|---------|------------|
| language:X | "fastapi language:python" | search_repos, search_code |
| stars:>N | "mcp stars:>100" | search_repos |
| repo:owner/repo | "error repo:anthropics/claude-code" | search_code, search_items |
| is:open/closed/merged | "bug is:open" | search_items |
| topic:X | "topic:mcp-server" | search_repos |

## Known Limitations

**get_repo_tree — truncation on large repos:**
- GitHub Git Trees API truncates at ~100k entries
- Tool warns when `truncated=true` in API response
- **Workaround:** Use `path` parameter to narrow scope

**search_code — does not index CSV/data files:**
- GitHub Code Search skips `type: data` files (CSV, TSV, etc. per GitHub Linguist)
- Tool shows NOTE when 0 results
- **Fallback:** Use `grep_repo` for data file content search

**grep_repo — max_files limit:**
- Server enforces min 20 files regardless of `max_files` value
- For repos with 50+ matching files, set `max_files` higher explicitly

## Searching for Values in Data Files

When searching for numeric values in CSVs:
- **Stored format != display format:** 6.74% is stored as `0.06741992...`
- `search_code("6.74")` → 0 results (CSV not indexed)
- **Strategy:** Search for column/metric name instead of value
- **Best approach:** `grep_repo(pattern="column_name", file_pattern="*.csv", path="subdir")`
