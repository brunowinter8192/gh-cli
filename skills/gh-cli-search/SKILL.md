---
name: gh-cli-search
description: 
---

# GitHub Search — Skill

**Code & repo content → direct CLI.**
Everything INSIDE a repo: `search_repos`, `search_code`, `get_repo_tree`, `get_file_content`. Direct `gh-cli` calls — read the output.

**The conversation & release layer → query-driven RAG indexing.**
Issues: `gh-cli index_issues "<1-3 kw>" <owner/repo>` → then `rag-cli search "<terms>" github_issues`. Discussions: `gh-cli index_discussions "<1-3 kw>" <owner/repo>` → then `rag-cli search "<terms>" github_discussions`. Releases: `gh-cli index_releases <owner/repo>` → then `rag-cli search "<feature>" github_releases`.

**`get_repo_tree` is one level deep — descend, don't dump.**
Each call lists exactly one directory level. To go deeper, call again with `--path <subdir>` using a directory name from the previous output. There is no recursive/full-tree mode and no truncation — you walk the tree top-down, one level per call.

**Directories carry no line/size signal.**
In the listing, `blob` (file) entries show `language`, `lines`, and `size`; `tree` (directory) entries show `-`. To judge what is inside a directory, descend into it with `--path`. There is no glob/name-pattern search — to find a file you either traverse to it or use `search_code` with a content term.

**Paths only from previous tool output — never constructed.**
Only use repo paths that appeared in `get_repo_tree` / `get_file_content` output. A 404 means the path is WRONG — re-run `get_repo_tree` to find the real one.

**search_code returns zero for code that EXISTS — know the cases.**
- Files over 350 KiB are not indexed.
- Empty files, binary files, and non-UTF-8 files are not indexed.
- A file with more than one line over 4096 bytes is excluded.
- Lines over 1024 characters are truncated.
   - A match beyond the truncation point is invisible.
- A path ancestor named `external`, `third_party`, or `node_modules` triggers the vendored/generated exclusion.
   - That heuristic has confirmed false positives on first-party code.
- Data files (CSV, TSV, per Linguist `type: data`) are never indexed.
   - The tool shows a NOTE on 0 results for this case.
- Very large repos may not be indexed at all.
- Fresh or inactive repos wait for on-demand indexing.
- Only the default branch is searchable.
- Identical files across repos are SHA-deduplicated.

**Zero-result escalation: clone to /tmp and grep.**
- A file listed by `get_repo_tree` where `search_code` found nothing proves an index gap, not absence.
- Shallow-clone the repo and grep repo-wide: `git clone --depth 1 https://github.com/<owner>/<repo> /tmp/<repo>` then `grep -rn`.
   - On a giant repo, clone only the relevant subtree: `git clone --depth 1 --sparse ... && git -C /tmp/<repo> sparse-checkout set <subdir>`.
- Never page through a large file with blind `get_file_content --offset` reads.

## Commands

| Command | Args | Does |
|---|---|---|
| search_repos | query (max 3 kw; qualifiers: stars:>N, topic:X) [--sort-by stars/forks/updated/best_match] | Find repos: landscape, "what exists for X" |
| search_code | query + qualifiers (repo:owner/repo, language:X) | Find code patterns; default branch only |
| get_repo_tree | owner repo [--path dir] | List ONE directory level; root call adds repo metadata |
| get_file_content | owner repo path [--offset N] [--limit N] [--metadata-only] | Read a repo file |
| repo_freshness | owner repo | pushed_at + age, updated_at/created_at — judge how current a repo is |
| download_files | owner repo path... [--dest dir] | Write repo files to local disk (no clone, no RAG) |
| index_issues | "query" owner/repo [--limit 30] | Fetch + index issues → RAG `github_issues` |
| index_discussions | "query" owner/repo [--limit 30] | Fetch + index discussions → RAG `github_discussions` |
| index_releases | owner/repo | Index last 100 releases → RAG `github_releases` (wipes + rebuilds) |

On error (import failure, missing GH_TOKEN, API error): the CLI prints to stderr and exits non-zero. Check `GH_TOKEN` env var is set.

## RAG Usage in gh-cli

**≥2 passes per problem.**
One concrete (exact symptom: error string / signal code) plus one broader (component / feature / area). Both accumulate into the same collection; further angles optional, the broad pass is mandatory.

**Index before search.**
Run `rag-cli search` on `github_issues` / `github_discussions` only after indexing in this session. Index first, then search.

**MAX 3 keywords, fallback 3→2→1.**
Mandatory; identical rule for `search_repos`, `index_issues`, `index_discussions` — the wrapper hard-caps at 3, extra words are silently dropped before the search call. Most distinctive keyword first: the fallback loop drops from the back (3→2→1), so if the 3-keyword query returns 0 it retries with 2, then 1.

**After indexing, search via RAG:**
  ```
  gh-cli index_issues "streaming" anthropics/claude-code --limit 30
  rag-cli search "streaming context window tool_use" github_issues

  gh-cli index_discussions "memory" gastownhall/beads --limit 30
  rag-cli search "memory tracking workflow" github_discussions
  ```

**Releases: recency questions → `read_document` from chunk 0, never vector search.**
After `index_releases`, answer "what is the latest release / how active is this package" by reading the newest indexed release directly: `rag-cli list_documents github_releases` → `rag-cli read_document github_releases <newest-release>.md 0 --after 2`. Vector search on `github_releases` is for "since when does feature X exist"; index your target repo immediately before searching — each run wipes and rebuilds the collection to that ONE repo.


