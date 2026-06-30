---
name: gh-cli-search
description: "GitHub remote research via gh-cli. Use when the user asks to find repos/projects ('finde repos für X', 'was gibt es zu Y'), read remote files ('lies das README von Z'), search code patterns ('zeig mir wie X in Y implementiert ist'), index and search issues or discussions ('index issues von X', 'index discussions von Y', 'bekannte issues in Z für RAG'), look up releases on GitHub, or check how recently a repo was pushed to to judge how current/trustworthy it is ('wie aktuell ist repo X', 'wann wurde Y zuletzt gepusht', 'ist Z noch maintained'). Do NOT use for: editing local files, running local git commands, searching local code (use Grep/Glob instead), or operations on the user's own GitHub account."
allowed-tools: Bash
---

# GitHub Search — Skill

## CLI Invocation

All tools are invoked via the `gh-cli` wrapper (installed at `~/.local/bin/gh-cli`, in PATH):

```
gh-cli <cmd> [args]
```

### Quick Reference — All 7 Tools

```bash
# Discovery
gh-cli search_repos "fastapi" --sort-by stars
gh-cli search_code "def workflow language:python repo:owner/repo"

# Repository Exploration — one level at a time (NOT recursive)
gh-cli get_repo_tree anthropics claude-code             # root listing + repo metadata
gh-cli get_repo_tree anthropics claude-code --path src  # descend into a subdirectory
gh-cli get_file_content anthropics claude-code README.md
gh-cli get_file_content anthropics claude-code src/main.py --offset 100 --limit 50
gh-cli get_file_content anthropics claude-code src/ --metadata-only

# Repository Freshness — how recently a repo was pushed to (judge how current/trustworthy it is)
gh-cli repo_freshness anthropics claude-code   # pushed_at + "pushed N days ago" + updated_at/created_at

# RAG Indexing (Issues + Discussions + Releases)
gh-cli index_issues "streaming" anthropics/claude-code --limit 30
gh-cli index_discussions "memory" gastownhall/beads --limit 30
gh-cli index_releases anthropics/claude-code   # index last 100 releases, then RAG-search
```

On error (import failure, missing GH_TOKEN, API error): the CLI prints to stderr and exits non-zero. Check `GH_TOKEN` env var is set.

## Two Access Patterns

- **Code & repo content → direct CLI.** Everything INSIDE a repo: `search_repos`, `search_code`, `get_repo_tree`, `get_file_content`. Direct `gh-cli` calls — read the output.
- **The conversation & release layer → query-driven RAG indexing.** The text layer AROUND the code. Issues: `gh-cli index_issues "<1-3 kw>" <owner/repo>` → then `rag-cli search_hybrid "<terms>" github_issues`. Discussions: `gh-cli index_discussions "<1-3 kw>" <owner/repo>` → then `rag-cli search_hybrid "<terms>" github_discussions`. Releases: `gh-cli index_releases <owner/repo>` → then `rag-cli search_hybrid "<feature>" github_releases`.

## Gotchas

- **Local paths as tool params → validation error.** `get_file_content` takes a repo-relative `path` only (e.g., `src/main.py`). Claude Code writes tool results to `/Users/.../.claude/projects/.../tool-results/...` — those are local filesystem paths. Passing one as `path`, or omitting `owner`/`repo`, fails immediately.

- **`get_repo_tree` is one level deep — descend, don't dump.** Each call lists exactly one directory level. To go deeper, call again with `--path <subdir>` using a directory name from the previous output. There is no recursive/full-tree mode and no truncation — you walk the tree top-down, one level per call.

- **Directories carry no line/size signal.** In the listing, `blob` (file) entries show `language`, `lines`, and `size`; `tree` (directory) entries show `-`. To judge what is inside a directory, descend into it with `--path`. There is no glob/name-pattern search — to find a file you either traverse to it or use `search_code` with a content term.

## Query Engineering (index_issues / index_discussions)

**Execution (task-level):**
- **≥2 passes per problem** — one concrete (exact symptom: error string / signal code) plus one broader (component / feature / area). Both accumulate into the same collection; further angles optional, the broad pass is mandatory.
- **Index before search** — run `rag-cli search_hybrid` on `github_issues` / `github_discussions` only after indexing in this session. Index first, then search.

**Per-call keyword rules:**
- **MAX 3 keywords** (mandatory) — the wrapper hard-caps at 3; extra words are silently dropped before the search call.
- **Most distinctive keyword first** — the fallback loop drops from the back (3→2→1 keywords). If the 3-keyword query returns 0 results, it retries with 2, then 1. A nonsense or overly-narrow last keyword won't block the run; an overly-narrow *first* keyword will error.
- **Indexing is SYNCHRONOUS — the command blocks until done.** `index_issues` / `index_discussions` fetch, strip, write MDs, and run `rag-cli index` in-process; they return the summary directly when finished. Run `rag-cli search_hybrid` immediately after — no waiting, no polling, no notification needed.
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
- MAX 3 keywords — most distinctive first. Extra words are dropped before the search call.
- Automatic 3→2→1 fallback: if the 3-keyword query returns 0, it retries with 2 keywords, then 1. A narrow last keyword won't block the run; a narrow *first* keyword will.
- WRONG: `search_repos("reddit browser submit post without api")` → first 3 words used
- RIGHT: `search_repos("reddit bot")` → then narrow with `sort_by=stars`

### Repo-Scoped Search (CRITICAL)

When the task specifies a target repo (e.g., "search anthropics/claude-code"):
- **ALWAYS** add `repo:owner/repo` to ALL search_code queries
- `search_code("session IPC repo:anthropics/claude-code")` — not just `search_code("session IPC")`
- Broad queries without `repo:` return results from unrelated repos and waste turns

### Query Engineering (search_code)

- **Always include at least one free-text term** — a qualifier alone (e.g., `language:go`) is invalid; combine with a search term (e.g., `"http.Get language:go"`).
- **`repo:owner/repo`** — scope to a known repo (primary use). Without it, results span all of GitHub and signal drops sharply.
- **`language:LANG`** — filter by file language (e.g., `language:python`, `language:go`, `language:typescript`).
- Only the **default branch** is searched. Files >384KB are excluded.

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

### Deep Repository Exploration (top-down traversal)
```
1. search_repos "topic:mcp server" -> Find relevant repos (use ONLY when repo unknown)
   → If repo is already known (specified in task): skip search_repos, go directly to step 2
2. get_repo_tree owner, repo -> Root listing + repo metadata (description, languages)
   → Read the entries: blobs show language/lines/size, trees are descent points
3. get_repo_tree owner, repo --path src -> Descend into an interesting directory
   → Repeat --path for each level you want deeper (one level per call, never recursive)
4. get_file_content owner, repo, "README.md" -> Read an anchor file
5. get_file_content owner, repo, "src/main.py" -> Read implementation
```

**While traversing, identify and note for output:**
- Main source directory (often `src/`, `lib/`) — descend into it with `--path`
- Anchor files at root (`README.md`, `pyproject.toml`, `package.json`)
- Entry points (`main.py`, `server.py`, `__init__.py`) — the `lines` column flags the substantial files

### Issue Investigation (RAG)
≥2 passes, then one search.
```
1. index_issues "<concrete: exact error string / signal>" owner/repo [--limit 30]
2. index_issues "<broader: component / feature / area>" owner/repo [--limit 30]
3. rag-cli search_hybrid "<symptom or topic terms>" github_issues
   → broad vector search over the accumulated corpus (concrete + broad pass)
```

### Discussion Research (RAG)
≥2 passes, then one search.
```
1. index_discussions "<concrete: exact topic / symptom>" owner/repo [--limit 30]
2. index_discussions "<broader: component / feature / area>" owner/repo [--limit 30]
3. rag-cli search_hybrid "<terms>" github_discussions
   → broad vector search over the accumulated corpus (concrete + broad pass)
```

### Code Pattern Discovery
```
1. search_code "def workflow language:python" -> Find patterns
   → Note the file path from search results!
2. get_file_content owner, repo, path -> Read full implementation
3. get_repo_tree owner, repo, "src/" -> Understand context
```

### Release Feature Search (RAG)
```
1. index_releases owner/repo
   → fetches the last 100 releases (newest-first), strips changelog noise, writes MDs,
     and WIPES + rebuilds the single github_releases collection (clean-before-index)
2. rag-cli search_hybrid "<feature or slash-command>" github_releases
   → e.g. "dynamic workflows /workflows" → the release that introduced it + the version
```
Use this to answer "since when does feature X exist / does our version have it".
github_releases holds ONLY the last-indexed repo (each index wipes + refills it) — so
always run index_releases for your target repo immediately before searching.

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

One directory level per call (GraphQL one-shot). Root call also returns repo metadata (description, primary language, language breakdown); sub-path calls return the listing only. Files are read with `get_file_content`, not this tool.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| path | str | "" | Directory to list (e.g. `src`, `plugins`). Empty = repo root. One level only — descend by calling again with the next subdirectory. |

### get_file_content

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |
| path | str | required | File or directory path |
| metadata_only | bool | False | Return only metadata (no content download) |
| offset | int | 0 | Start reading from this line number |
| limit | int | 0 | Number of lines to return (0=all) |

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

### index_releases

Fetches the last 100 releases (newest-first), strips changelog noise, and indexes them into the single RAG collection `github_releases`. Clean-before-index: each run WIPES and rebuilds `github_releases` with the given repo's releases — so the collection holds only ONE repo at a time (the last indexed) and is always fresh. Always index your target repo immediately before searching: `rag-cli search_hybrid "<feature>" github_releases`.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| repo | str | required | Repository as `owner/repo` |

### repo_freshness

Runs on a single repo (one REST call). Prints `pushed_at` (last commit push to any branch) with a relative age `(pushed N days ago)` computed from the current UTC time, plus `updated_at` and `created_at`. Use to judge how current a repo is and how much to trust it on shifting foundations (API behavior, framework conventions). `pushed_at` is the core signal; a large day-count = stale.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| owner | str | required | Repository owner |
| repo | str | required | Repository name |

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
- After `get_repo_tree`, note the `type` column: `tree` = directory, `blob` = file. NEVER pass a directory (`tree`) path to `get_file_content` — descend into it with `get_repo_tree --path` instead.

**Pre-call check (MANDATORY before EVERY `get_file_content` call):**
1. Did this exact path appear as a `blob` entry in a previous `get_repo_tree` output?
2. If YES → proceed.
3. If NO, or if the entry is a `tree` (directory) → use `get_repo_tree --path <dir>` to list it instead.
This check must be done every time, even for paths that "look like files".

## Known Limitations

**get_repo_tree — one level per call (by design):**
- Lists a single directory level; no recursive/full-tree dump and no truncation
- Directory (`tree`) entries carry no line/size signal — descend with `--path` to see inside
- To locate a file by name you cannot glob — traverse to it, or use `search_code` with a content term

**search_code — does not index CSV/data files:**
- GitHub Code Search skips `type: data` files (CSV, TSV, etc. per GitHub Linguist)
- Tool shows NOTE when 0 results
- **Fallback:** Use `get_file_content` to read a known file path directly

## Search-Failure Escalation (NON-NEGOTIABLE)

When ANY search (search_code, search_repos, RAG) returns 0 / "No matches", do NOT conclude "it isn't there" from a single tool. Escalate:

1. `search_code` empty → traverse with `get_repo_tree` (root, then `--path` into the likely directory) to find the file structurally, then `get_file_content` on the exact path. Note: `search_code` needs a free-text content term — a name/extension qualifier alone is rejected, so it cannot enumerate files by name.
2. Still empty → vary the term itself: synonym, shorter substring, different casing. Do NOT re-run the identical term in the identical tool (guessing).

Rule: only **two different tools** both returning nothing counts as evidence of absence. One tool's silence is not — it's a prompt to switch tools, not to give up.

## When to Stop

Task type determines stop criteria — identify which type you have before starting:

**Verification task** ("find file X", "check issue Y", "what does line Z say"):
- Found the specific answer → STOP immediately, synthesize
- One correct result = done. No need for alternatives.
- Anti-pattern: making exploratory calls after finding the answer

**Research / exploratory task** ("best library for X", "known issues with Y", "how do people solve Z"):
- Minimum 3 distinct queries before stopping
- Stop when 3-5 high-quality results found that together give a complete picture
- Stop after 3 queries with diminishing returns
- Do NOT stop at first match
- After finding 3+ repos: switch to READING (READMEs, key files) — no more searching

**Both types:**
- Stop when approaching token budget
- Max 2-3 files read per repo after discovery
