---
name: github-search
description: See ~/.claude/shared-rules/global/cli-skills.md
---

# GitHub Search — Skill

## CLI Invocation

All tools are invoked via the `gh-cli` wrapper (installed at `~/.local/bin/gh-cli`, in PATH):

```
gh-cli <cmd> [args]
```

### Quick Reference — All 20 Tools

```bash
# Discovery
gh-cli search_repos "fastapi" --sort-by stars
gh-cli search_code "def workflow language:python repo:owner/repo"
gh-cli get_repo anthropics claude-code

# Repository Exploration
gh-cli get_repo_tree anthropics claude-code --path src --depth 2 --pattern "*.py"
gh-cli get_file_content anthropics claude-code README.md
gh-cli get_file_content anthropics claude-code src/main.py --offset 100 --limit 50
gh-cli get_file_content anthropics claude-code src/ --metadata-only

# Content Search
gh-cli grep_file anthropics claude-code src/main.py "def run" --context-lines 3
gh-cli grep_repo anthropics claude-code "class.*Tool" --file-pattern "*.py" --path src --max-files 20

# Issues & PRs
gh-cli search_items "memory leak repo:anthropics/claude-code" --type issue --sort-by comments
gh-cli get_issue anthropics claude-code 1234
gh-cli get_issue_comments anthropics claude-code 1234
gh-cli list_repo_prs anthropics claude-code --state open --sort-by updated
gh-cli get_pr anthropics claude-code 567
gh-cli get_pr_files anthropics claude-code 567

# Discussions
gh-cli search_discussions "context window topic:claude"
gh-cli list_discussions anthropics claude-code --first 20 --category q-a --answered
gh-cli list_discussions anthropics claude-code --not-answered
gh-cli get_discussion anthropics claude-code 89 --comment-sort upvotes --comment-limit 30

# Commits & Releases
gh-cli list_commits anthropics claude-code --path src/main.py --per-page 10
gh-cli list_commits anthropics claude-code --sha main --author octocat
gh-cli compare_commits anthropics claude-code v1.0 v2.0
gh-cli list_releases anthropics claude-code --per-page 5
gh-cli get_release anthropics claude-code --tag v2.0.0
gh-cli get_release anthropics claude-code  # latest release
```

On error (import failure, missing GH_TOKEN, API error): the CLI prints to stderr and exits non-zero. Check `GH_TOKEN` env var is set.

## Regex Patterns (grep_file / grep_repo)

Patterns are compiled with Python `re` — **NOT** POSIX ERE.

- Alternation: use bare `|`, never `\|`. POSIX-ERE `\|` matches a literal backslash-pipe in Python and returns zero matches silently.
- The CLI auto-normalizes `\|` → `|` and emits a warning, but writing the correct pattern first is faster.
- Good: `"MOUSE_WHEEL_UP|MOUSE_WHEEL_DOWN"`, `"def (run|start)"`
- Bad: `"MOUSE\|mouse\|button"` (escaped pipes; auto-corrected but wastes a call)

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

## Search Strategy

### Tool Selection: search_repos vs. search_code (CRITICAL)

**Use `search_repos`** when the task is: "find repos/tools/libraries for X"
- Landscape discovery, tech comparison, "what exists for this use case"
- Start with 2-3 core keywords MAXIMUM (GitHub API returns 0 for 4+ words)
- GOOD: `search_repos("reddit bot")` → finds Reddit automation repos
- BAD: `search_code("reddit post automation selenium python")` → finds README files that mention all 4 words

**Use `search_code`** when the task is: "find this code pattern/function in repo(s)"
- Known repo, looking for specific implementation
- With `repo:owner/repo` qualifier to scope the search
- GOOD: `search_code("def submit_post repo:specific/repo")` → finds implementation
- BAD: `search_code("reddit post selenium")` → finds 2000+ unrelated files globally

**`search_repos` query limit (NON-NEGOTIABLE):**
- Maximum 2-3 words. GitHub API returns 0 results for 4+ word queries.
- WRONG: `search_repos("reddit browser submit post without api")` → 0 results
- RIGHT: `search_repos("reddit bot")` → then narrow with `sort_by=stars`
- When no results: try synonyms as SEPARATE 2-word queries, don't add words to the failing query

### Repo-Scoped Search (CRITICAL)

When the task specifies a target repo (e.g., "search anthropics/claude-code"):
- **ALWAYS** add `repo:owner/repo` to ALL search_code and search_items queries
- `search_code("session IPC repo:anthropics/claude-code")` — not just `search_code("session IPC")`
- Broad queries without `repo:` return results from unrelated repos and waste turns

### Iterative Refinement (when no target repo is specified)

**Start broad, then narrow down:**

1. **First query**: 1-2 core keywords
   - Good: `html parser`
   - Bad: `html parser python beautifulsoup lxml async`

2. **Check results**: Analyze what you get

3. **Refine with qualifiers**:
   - `language:python`
   - `stars:>100`
   - `repo:owner/repo`
   - `is:open` / `is:closed` / `is:merged`

**Example Flow:**
```
Query 1: "fastapi authentication" -> 500 results, too broad
Query 2: "fastapi oauth2 language:python" -> 50 results, better
Query 3: "fastapi oauth2 jwt language:python stars:>50" -> 12 results, focused
```

## Tool Chaining Workflows

### Deep Repository Exploration
```
1. search_repos "topic:mcp server" -> Find relevant repos (use ONLY when repo unknown)
   → If repo is already known (specified in task): skip search_repos, go directly to get_repo
2. get_repo owner, repo -> Get repo metadata when repo is already known
   → search_repos with repo: qualifier = WRONG. Use get_repo instead.
3. get_repo_tree owner, repo -> Understand structure
   → Extract key file paths for your output!
4. get_file_content owner, repo, "README.md" -> Read docs
5. get_file_content owner, repo, "src/main.py" -> Read implementation
```

**After get_repo_tree, identify and note for output:**
- Main source file (often `src/`, `lib/`, or root `*.py`)
- Config files (`settings.py`, `config.py`, `pyproject.toml`)
- Entry points (`main.py`, `server.py`, `__init__.py`)

### Issue Investigation
```
1. search_items "error message repo:owner/repo" type="issue" -> Find related issues
2. get_issue owner, repo, issue_number -> Read full issue
3. get_issue_comments owner, repo, issue_number -> Read discussion
```

### PR Analysis
```
1. search_items "feature repo:owner/repo is:merged" type="pr" -> Find relevant PRs
2. get_pr owner, repo, pull_number -> Read PR details
3. get_pr_files owner, repo, pull_number -> See what changed
4. get_file_content owner, repo, "changed_file.py" -> Read current state
```

### Code Pattern Discovery
```
1. search_code "def workflow language:python" -> Find patterns
   → Note the file path from search results!
2. get_file_content owner, repo, path -> Read full implementation
3. get_repo_tree owner, repo, "src/" -> Understand context
```

### Discussion Research
```
1. search_discussions "error message topic" -> Find Q&A across repos
2. list_discussions owner, repo, category="q-a" -> Browse repo discussions
3. get_discussion owner, repo, number, comment_sort="upvotes" -> Read top answers
```

### Commit History & Version Analysis
```
1. list_commits owner, repo -> Browse recent commits
2. list_commits owner, repo, path="src/main.py" -> Find when file was changed
3. compare_commits owner, repo, base="v1.0", head="v2.0" -> See what changed between versions
4. list_releases owner, repo -> Find versions and changelogs
```

## Navigation Rules

**1. DOCS first — always.**
Before opening data files or CSVs in any directory, check for README.md or DOCS.md in that directory (or parent). Well-documented repos explain which files are authoritative and what each subdirectory contains. Skipping DOCS leads to reading the wrong file.

**2. Ambiguous matches — check ALL before reporting.**
When multiple candidates exist (same filename in different paths, multiple subdirectories like `approach_1/` through `approach_4/`, different versions of the same data): check ALL of them BEFORE reporting any result. Never report a mismatch after checking only one candidate when others remain unchecked. The correct workflow is:
1. Identify all candidates (parallel `get_file_content` or `grep_file` calls)
2. Compare each against the expected data
3. Report the full picture: which matches, which don't, and why

**3. When no candidate matches — show all.**
If after checking ALL candidates none matches, present all findings with their full paths. One wrong assumption wastes more time than a few extra tool calls.

**4. Search Mode — targeted vs exploratory.**

- **Targeted search** (asked for specific data, verification, comparison):
  Exhaust cheap self-serve options first:
  1. `get_repo_tree(pattern="*keyword*")` or `grep_repo` to locate files directly
  2. If file found but content doesn't match → **check same directory first** (`depth=1`) for variants (filtered, selected, final, summary...)
  3. If same directory has nothing → broaden scope one level up
  4. Only after 2-3 failed attempts → report as NOT FOUND

- **Exploratory search** (discover trends, compare repos, survey landscape):
  Navigate freely with tools. Drill down via get_repo_tree, read READMEs, follow interesting leads.

**5. Filename search before content search.**
When looking for a specific example or report, search by the broadest known identifier in the filename FIRST (e.g., template name, query ID), not by specific content details (e.g., node IDs, exact values).
- `get_repo_tree(pattern="*Q8*", path="Predictions/")` → finds all Q8 reports in one call
- `grep_repo(pattern="13408", file_pattern="*.md")` → may miss due to `max_files` limit

**6. Session context before new searches.**
Before making new tool calls, check if the referenced data was already read in this session. New claims often reference the same source files as previous ones. Re-reading known files wastes tool calls.

### Truncation Handling

When any tool returns a truncation warning:
1. Do NOT retry with same scope
2. Use `get_repo_tree(path="<truncated_dir>", depth=1)` to discover subdirectories
3. Run `grep_repo` with narrower `path` parameter on each subdirectory
4. Report which subdirectories were searched and which were skipped

### Reading Priority (per repository)

1. **README.md** - Overview, features, usage
2. **package.json / pyproject.toml** - Dependencies, metadata
3. **docs/ or examples/** - Usage patterns
4. **src/** - Only if critical to answer question

### Result Limits

**search_repos / search_code:**
- Fetch: Top 10-15 results
- Read in depth: Top 3-5
- Skim rest: Only for outliers

**Files per repo:**
- Max 3-4 files (README + key sources)
- Use get_repo_tree first to identify critical files

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

## Path Integrity (CRITICAL)

**NEVER construct paths from memory or assumptions.**
- Only use paths that appeared in `get_repo_tree` or `get_file_content` output
- If `get_repo_tree` shows `Baseline_SVM/approach_3/` → use that EXACT path
- If a file read fails with 404 → the path is WRONG. Re-run `get_repo_tree` to find the correct path
- Do NOT skip intermediate directories (e.g., `Datasets/approach_3/` when actual path is `Datasets/Baseline_SVM/approach_3/`)
- After `get_repo_tree`, note which entries are directories (trailing `/`) vs files. NEVER pass a directory path to `get_file_content` — use `get_repo_tree` to explore directories instead.

**Pre-call check (MANDATORY before EVERY `get_file_content` call):**
1. Did this exact path appear as a FILE entry (no trailing `/`) in a previous `get_repo_tree` output?
2. If YES → proceed.
3. If NO, or if path ends with `/` in tree output → use `get_repo_tree(path=<dir>, depth=1)` instead.
This check must be done every time, even for paths that "look like files".

## Report Format

**CRITICAL: Your FINAL response MUST be the structured report. Never end with narration.**

Wrong: "Excellent! I found the issue. Let me get the details:" — in-progress comment, NOT a final response.
Wrong: "I have enough information. Let me compile the findings now." — same anti-pattern.
Wrong: "I'll now summarize what I found:" — transition sentence, forbidden before the report.
Right: Start DIRECTLY with FILE: / VALUE: / EVIDENCE: blocks. Zero intro text.

When you have completed your research (or are approaching turn limits), output the structured report IMMEDIATELY as your final message. No commentary before it, no "let me now..." transitions.

Adapt format to task type:

### For Data Verification
```
## Findings
[FILE/LINES/VALUE/EVIDENCE/VERDICT blocks — one per claim]

## Search Process
1. get_repo_tree(...) → found X directories
2. get_file_content(...) → read file, N lines
3. grep_file(...) → found pattern at line N
```

### For Repo Discovery
```
## Summary (2-4 sentences)
## Top Results (Max 3-5) — with paths!
## Search Process
## Next Step (singular!)
```

## Output Requirements

**CRITICAL: Every finding MUST include FILE path + concrete evidence.**

Your output goes to the caller who will verify your findings. Without file paths, your output is unusable.

### Data Verification Output (when searching for specific values/counts)

Use this EXACT format for every finding:
```
FILE: Prediction_Methods/Hybrid_1/Datasets/Baseline_SVM/approach_3/patterns_filtered.csv
LINES: 74 total (line 1 = header → 73 data rows)
VALUE: 73 patterns
EVIDENCE: First line: "pattern_hash;pattern_string;pattern_length;..." (header)
VERDICT: MISMATCH (expected 72, found 73)
```

**Rules:**
- FILE must be the full repo-relative path (from `get_repo_tree` output)
- LINES must note if line 1 is a header (affects count!)
- EVIDENCE must quote actual content from the file
- VERDICT must state expected vs actual
- **For PRs and Issues:** EVIDENCE must include at minimum: title, status (open/closed/merged), and one concrete detail (description excerpt, key change, or comment). Search result metadata alone (e.g., "labels: python") is not sufficient — read the PR/Issue with `get_pr` or `get_issue` first.

### Repo Discovery Output (when finding repos/projects)

**For each relevant repo:**
- **Repo:** `owner/repo` (consistent format, no leading `/`)
- **Key Files:** Exact paths from `get_repo_tree` output
- **GitHub URL:** Only when explicitly requested

**Good Example:**
```
**qdrant/mcp-server-qdrant** (1,183 Stars)
- Implementation: `src/mcp_server_qdrant/server.py`
- Config: `src/mcp_server_qdrant/settings.py`
- Tools: qdrant-store, qdrant-find
```

**Bad Example (no paths):**
```
qdrant/mcp-server-qdrant implements FastMCP pattern
```

**For search_code results:**
Include the file path from search output, e.g.:
- "MCP tools defined in `internal/mcp/server.go`"

## Output Hygiene

**NEVER include in output:**
- Local filesystem paths (`/Users/...`, `/home/...`, `C:\...`)
- References to "current context" or "workspace"
- Any path that is not a GitHub repository path

**ONLY GitHub references:**
- `owner/repo` for repositories
- `path/to/file.py` for files within repos
- `https://github.com/...` URLs only when specifically asked

**NEVER use local paths as tool parameters (CRITICAL):**
- `get_file_content` requires THREE params: `owner`, `repo`, `path` — ALL mandatory
- `path` must be a repo-relative path (e.g., `src/main.py`) — NEVER a local filesystem path
- Claude Code writes tool results to local files like `/Users/.../.claude/projects/.../tool-results/...` — these are NOT GitHub paths. Do NOT pass them to any GitHub tool.
- A call with `path=/Users/...` and no `owner`/`repo` = guaranteed validation error.

## Guidelines

**DOCS first:** When searching within a repo directory, check for DOCS.md or README.md BEFORE deep-diving into individual files. These docs often reveal summary files, comparison scripts, or pre-computed outputs that answer the question in a single read. One extra call to read DOCS is cheaper than 10 calls navigating blind.

**Thoroughness over efficiency:** You are using cheap, fast tools. Your value is measured by RESULTS, not by token savings. Better one call too many than missing the right file. When in doubt, read the file. When a directory has summary/overview/comparison files, read them even if not explicitly asked.

**DATA, not plans (CRITICAL):** Your job is to READ files and RETURN data. Never return a "strategy" or "plan" describing what you WOULD do.

- **WRONG:** "I would search in directory X, then read file Y, then extract value Z"
- **RIGHT:** Actually call get_repo_tree, get_file_content, grep_file — then report FILE/VALUE/EVIDENCE

If you run out of turns before reading all files, return what you DID find plus a structured handoff:
```
## Completed
FILE: path/to/file.csv
VALUE: 21.73%
EVIDENCE: mean_mre;0.2173...

## Not Yet Read (for follow-up)
Directory structure discovered:
- path/to/dir/ contains: file_a.csv, file_b.csv, summary.csv
- path/to/other/ contains: overall_mre.csv
Target files to read: [exact paths from get_repo_tree output]
```

- **Iterate searches**: Never give up after one query
- **Chain tools**: search -> tree -> content for deep exploration
- **Be specific**: Include owner/repo references
- **Be honest**: Report if search yields poor results

## Known Limitations

**get_repo_tree — truncation on large repos:**
- GitHub Git Trees API truncates at ~100k entries
- Tool warns when `truncated=true` in API response
- **Workaround:** Use `path` parameter to narrow scope

**search_code — does not index CSV/data files:**
- GitHub Code Search skips `type: data` files (CSV, TSV, etc. per GitHub Linguist)
- Tool shows NOTE when 0 results
- **Fallback:** Use `grep_repo` for data file content search

**search_repos — query length limit:**
- Server auto-truncates queries to 3 words with warning in output
- When exploring a broad topic: run MULTIPLE short queries, not ONE long query
- Use `sort_by` parameter (stars, updated) to filter, not more query words

**grep_repo — max_files limit:**
- Server enforces min 20 files regardless of `max_files` value
- For repos with 50+ matching files, set `max_files` higher explicitly

**Searching for Values in Data Files:**
- **Stored format != display format:** 6.74% is stored as `0.06741992...`
- `search_code("6.74")` → 0 results (CSV not indexed)
- **Strategy:** Search for column/metric name instead of value
- **Best approach:** `grep_repo(pattern="column_name", file_pattern="*.csv", path="subdir")`

## When to Stop

Task type determines stop criteria — identify which type you have before starting:

**Verification task** ("find file X", "check issue Y", "what does line Z say"):
- Found the specific answer → STOP immediately, synthesize
- One correct result = done. No need for alternatives.
- Anti-pattern: making exploratory calls after finding the answer

**Research / exploratory task** ("best library for X", "known issues with Y", "how do people solve Z"):
- Minimum 3 distinct queries before stopping — alternatives matter
- Stop when 3-5 high-quality results found that together give a complete picture
- Stop after 3 queries with diminishing returns
- Do NOT stop at first match — one result is not a comparison, it's a starting point
- After finding 3+ repos: switch to READING (READMEs, key files) — no more searching

**Both types:**
- Stop when approaching token budget
- Max 2-3 files read per repo after discovery
