---
name: github-search
description: "GitHub remote research via gh-cli. Use when the user asks to find repos/projects ('finde repos für X', 'was gibt es zu Y'), read remote files ('lies das README von Z'), search code patterns ('zeig mir wie X in Y implementiert ist'), index and search issues or discussions ('index issues von X', 'index discussions von Y', 'bekannte issues in Z für RAG'), or look up releases on GitHub. Do NOT use for: editing local files, running local git commands, searching local code (use Grep/Glob instead), or operations on the user's own GitHub account."
allowed-tools: Bash
---

# GitHub Search — Skill

## CLI Invocation

All tools are invoked via the `gh-cli` wrapper (installed at `~/.local/bin/gh-cli`, in PATH):

```
gh-cli <cmd> [args]
```

### Quick Reference — All 11 Tools

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

# RAG Indexing (Issues + Discussions)
gh-cli index_issues "streaming" anthropics/claude-code --limit 30
gh-cli index_discussions "memory" gastownhall/beads --limit 30

# Releases
gh-cli list_releases anthropics claude-code --per-page 5
gh-cli get_release anthropics claude-code --tag v2.0.0
gh-cli get_release anthropics claude-code  # latest release
```

On error (import failure, missing GH_TOKEN, API error): the CLI prints to stderr and exits non-zero. Check `GH_TOKEN` env var is set.

## Two Access Patterns

- **Code & repo content → direct CLI.** Everything INSIDE a repo: `search_repos`, `search_code`, `get_repo`, `get_repo_tree`, `get_file_content`, `grep_file`, `grep_repo`. Release metadata: `list_releases`, `get_release`. Direct `gh-cli` calls — read the output.
- **The conversation layer → query-driven RAG indexing.** The discussion/text layer AROUND the code. Issues: `gh-cli index_issues "<1-3 kw>" <owner/repo>` → then `rag-cli search_hybrid "<terms>" github_issues`. Discussions: `gh-cli index_discussions "<1-3 kw>" <owner/repo>` → then `rag-cli search_hybrid "<terms>" github_discussions`. A few broad vector searches replace many fine-grained tool-calls. Releases stay CLI-direct (exact-artifact lookup, not fuzzy retrieval).

## Regex Patterns (grep_file / grep_repo)

Patterns are compiled with Python `re` — **NOT** POSIX ERE.

- Alternation: use bare `|`, never `\|`. POSIX-ERE `\|` matches a literal backslash-pipe in Python and returns zero matches silently.
- The CLI auto-normalizes `\|` → `|` and emits a warning, but writing the correct pattern first is faster.
- Good: `"MOUSE_WHEEL_UP|MOUSE_WHEEL_DOWN"`, `"def (run|start)"`
- Bad: `"MOUSE\|mouse\|button"` (escaped pipes; auto-corrected but wastes a call)

## Gotchas

- **Local paths as tool params → validation error.** `get_file_content`, `grep_file`, `grep_repo` take repo-relative `path` only (e.g., `src/main.py`). Claude Code writes tool results to `/Users/.../.claude/projects/.../tool-results/...` — those are local filesystem paths. Passing one as `path`, or omitting `owner`/`repo`, fails immediately.

- **Truncation warning → narrow scope, don't retry.** On any truncation warning: `get_repo_tree(path="<dir>", depth=1)` to find subdirectories, then `grep_repo(path=<subdir>)` per subdirectory. Retrying the same broad scope reproduces the truncation.

- **Filename pattern before content search.** `get_repo_tree(pattern="*keyword*", path="<dir>")` locates files in one call. `grep_repo` has a `max_files` cap (server min 20) — on large repos it silently misses files beyond the limit. Find candidates with tree pattern first, then grep on known paths.

## Query Engineering (index_issues / index_discussions)

- **MAX 3 keywords** (mandatory) — the wrapper hard-caps at 3; extra words are silently dropped before the search call.
- **Most distinctive keyword first** — the fallback loop drops from the back (3→2→1 keywords). If the 3-keyword query returns 0 results, it retries with 2, then 1. A nonsense or overly-narrow last keyword won't block the run; an overly-narrow *first* keyword will error.
- **Indexing runs in the BACKGROUND — never poll for completion.** `index_issues` / `index_discussions` dispatch the fetch+embed job and return immediately with a background task ID. On completion you are NOTIFIED automatically. Do NOT `tail` the task output file, do NOT re-check status, do NOT loop/sleep waiting. Fire the index command, then either do other work or go idle — run the `rag-cli search_hybrid` step only AFTER the completion notification arrives. Polling the index output is a rule violation (wasted tool calls + context).
- **After indexing, search via RAG:**
  ```
  gh-cli index_issues "streaming" anthropics/claude-code --limit 30
  rag-cli search_hybrid "streaming context window tool_use" github_issues

  gh-cli index_discussions "memory" gastownhall/beads --limit 30
  rag-cli search_hybrid "memory tracking workflow" github_discussions
  ```
- **Re-run = re-index** — always overwrites MDs and re-indexes. Items with new comments get re-chunked automatically (RAG `index-dir` skips unchanged content-hash).

**index_discussions only:**
- **repo: injection automatic** — `index_discussions` scopes search to the target repo; no cross-repo search.
- **Accepted-answer threading** — accepted answers appear in `### Accepted Answer` block; duplicate in-list `[ANSWER]` tag is stripped automatically during indexing.

## Search Strategy

### Tool Selection: search_repos vs. search_code (CRITICAL)

**Use `search_repos`** when the task is: "find repos/tools/libraries for X"
- Landscape discovery, tech comparison, "what exists for this use case"
- GOOD: `search_repos("reddit bot")` → finds Reddit automation repos
- BAD: `search_code("reddit post automation selenium python")` → finds README files that mention all 4 words

**Use `search_code`** when the task is: "find this code pattern/function in repo(s)"
- Known repo, looking for specific implementation
- With `repo:owner/repo` qualifier to scope the search
- GOOD: `search_code("def submit_post repo:specific/repo")` → finds implementation
- BAD: `search_code("reddit post selenium")` → finds 2000+ unrelated files globally

**`search_repos` query limit (NON-NEGOTIABLE):**
- Maximum 2-3 words. 4+ word queries are auto-truncated to 3 (CLI warns) or return 0 results.
- WRONG: `search_repos("reddit browser submit post without api")` → 0 results
- RIGHT: `search_repos("reddit bot")` → then narrow with `sort_by=stars`
- When no results: try synonyms as SEPARATE 2-word queries, don't add words to the failing query

### Repo-Scoped Search (CRITICAL)

When the task specifies a target repo (e.g., "search anthropics/claude-code"):
- **ALWAYS** add `repo:owner/repo` to ALL search_code queries
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

### Issue Investigation (RAG)
```
1. index_issues "<1-3 kw>" owner/repo [--limit 30]
   → fetches top-N issues by relevance, strips noise, writes MDs, indexes into github_issues
2. rag-cli search_hybrid "<symptom or topic terms>" github_issues
   → broad vector search replaces many fine-grained issue tool-calls
```

### Discussion Research (RAG)
```
1. index_discussions "<1-3 kw>" owner/repo [--limit 30]
   → fetches top-N discussions by relevance, strips noise, writes MDs, indexes into github_discussions
2. rag-cli search_hybrid "<terms>" github_discussions
   → broad vector search across all indexed threads
```

### Code Pattern Discovery
```
1. search_code "def workflow language:python" -> Find patterns
   → Note the file path from search results!
2. get_file_content owner, repo, path -> Read full implementation
3. get_repo_tree owner, repo, "src/" -> Understand context
```

### Release Lookup
```
1. list_releases owner repo --per-page 5  -> Find versions and changelogs
2. list_releases owner repo --page 2      -> Releases 11-20 (page through history)
3. get_release owner repo --tag v2.0.0    -> Read specific release notes
4. get_release owner repo                 -> Read latest release
```

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

### index_issues

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| query | str | required | Search keywords (max 3; most distinctive first) |
| repo | str | required | Repository as owner/repo |
| --limit | int | 30 | Max issues to fetch and index |

### index_discussions

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| query | str | required | Search keywords (max 3; most distinctive first) |
| repo | str | required | Repository as owner/repo |
| --limit | int | 30 | Max discussions to fetch and index |

### get_repo

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |

### list_releases

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| per_page | int | 10 | Number of releases to return |
| --page | int | 1 | Page number (10 per page → page 2 = releases 11–20) |

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
| repo:owner/repo | "error repo:anthropics/claude-code" | search_code |
| topic:X | "topic:mcp-server" | search_repos |

## Path Integrity (CRITICAL)

**NEVER construct paths from memory or assumptions.**
- Only use paths that appeared in `get_repo_tree` or `get_file_content` output
- If `get_repo_tree` shows `src/server/handlers/` → use that EXACT path
- If a file read fails with 404 → the path is WRONG. Re-run `get_repo_tree` to find the correct path
- Do NOT skip intermediate directories (e.g., `src/handlers/` when actual path is `src/server/handlers/`)
- After `get_repo_tree`, note which entries are directories (trailing `/`) vs files. NEVER pass a directory path to `get_file_content` — use `get_repo_tree` to explore directories instead.

**Pre-call check (MANDATORY before EVERY `get_file_content` call):**
1. Did this exact path appear as a FILE entry (no trailing `/`) in a previous `get_repo_tree` output?
2. If YES → proceed.
3. If NO, or if path ends with `/` in tree output → use `get_repo_tree(path=<dir>, depth=1)` instead.
This check must be done every time, even for paths that "look like files".

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

**grep_repo can return "No matches" when matches DO exist (false negative).** Observed 2026-05-30: `grep_repo` returned "No matches" with 50/50 files searched on a file where `search_code "<term> repo:owner/repo"` found 6 hits — same repo, same term. A 0-result from one tool is NOT proof of absence.

## Search-Failure Escalation (NON-NEGOTIABLE)

When ANY search (search_code, grep_repo, search_repos, RAG) returns 0 / "No matches", do NOT conclude "it isn't there" from a single tool. Escalate:

1. `grep_repo` empty → `search_code "<term> repo:owner/repo"` (different index, catches what grep_repo silently misses).
2. `search_code` empty → `get_repo_tree(pattern="*<keyword>*", path="<dir>")` to locate the file by NAME, then `get_file_content` / `grep_file` on the exact path.
3. Still empty → vary the term itself: synonym, shorter substring, different casing. Do NOT re-run the identical term in the identical tool (guessing).

Rule: only **two different tools** both returning nothing counts as evidence of absence. One tool's silence is not — it's a prompt to switch tools, not to give up.

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
