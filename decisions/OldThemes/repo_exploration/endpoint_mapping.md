# Repo Exploration — Endpoint Mapping (Phase A: Probe Build)

## The Gap

Structural repo exploration = "understand an unknown repo top-down": what files exist, what the tech stack is, where the anchor documents (README, CONTRIBUTING, LICENSE) live, which directory is the entry point. This is distinct from grep (`search_code` — find a known pattern) and distinct from targeted file reads (`get_file_content`).

Local-FS analogy:

| Tool | FS analogy |
|---|---|
| `search_repos` | `find / -name '*.git'` |
| `search_code` | `grep -r` |
| `get_repo_tree` | `ls` / `tree` / `find -name` |
| `get_file_content` | `cat` / `head` |
| **missing** | **`file` / `wc -l` / `stat` per entry; no orientation strategy** |

The gap: no documented orientation strategy, and the current tools give raw FS primitives without the signal layer (language per file, anchor doc locations, tech stack summary).

## Current Baseline (Production)

`get_repo_tree` uses a 3-REST-call chain:
1. `GET /repos/{owner}/{repo}` → default branch name
2. `GET /repos/{owner}/{repo}/branches/{branch}` or `/contents/{path}` → tree SHA
3. `GET /git/trees/{sha}?recursive=1` → full file list

Browse mode = ls. Pattern mode = find -name. No per-entry language or line count.

`get_file_content` = `GET /contents/{path}`, base64-decode, offset/limit slicing. One file per call.

## Candidate Endpoints

| Endpoint | API | Returns | Maps to use-case | Probe |
|---|---|---|---|---|
| `GET /repos/{o}/{r}/readme[/{dir}]` | REST | Preferred README regardless of filename (base64 JSON; raw via `vnd.github.raw+json`) | Anchor #1 "what is this repo" — no filename guessing | `probe_readme.py` |
| `GET /repos/{o}/{r}/languages` | REST | Language→bytes breakdown | Tech-stack orientation in one call | `probe_languages.py` |
| `GET /repos/{o}/{r}/community/profile` | REST | Health%, description, files-map (README/LICENSE/CONTRIBUTING/CoC/templates presence+paths) | Anchor-file map in one call | `probe_community.py` |
| `GET /contents/{path}` with `Accept: application/vnd.github.object+json` | REST | Directory as `entries` array (consistent object format) | Cleaner dir listing (alternative to git/trees chain) | note only |
| GraphQL `repository.object(expression)` → Tree | GraphQL | `entries{name, type, path, extension, language{name}, lineCount, size}` | Structure WITH language+lineCount per entry — one call | `probe_graphql_explore.py` |
| GraphQL `…on Blob { text, byteSize, isBinary }` | GraphQL | File content (UTF-8) directly | Read file in same query as tree inspection | `probe_graphql_explore.py` |
| GraphQL `Repository{ description, primaryLanguage, languages }` | GraphQL | Repo metadata + language ranking | Orientation metadata in same round-trip | `probe_graphql_explore.py` |

## Investigation Plan

**Phase A (this session):** Build `dev/repo_exploration/` probes — `probe_readme.py`, `probe_languages.py`, `probe_community.py`, `probe_graphql_explore.py` + shared `probe_client.py` (self-contained auth copy). Sanity-run each once to verify they hit the real API without errors.

**Phase B (next session):** Run all probes against one well-known repo (e.g. `fastapi/fastapi`) and compare:
- Output quality: how much orientation signal per call?
- Token cost: chars returned vs current get_repo_tree output for the same repo?
- GraphQL one-shot vs 3-REST chain: round-trips, response size, field richness?

**Decision point after Phase B:** choose among:
- (a) Add a REST `get_readme` tool and/or `get_languages` tool (small, clear use-case)
- (b) Rework `get_repo_tree` as a GraphQL one-shot (dev/-vs-src/ rule: stays in dev/ until verified)
- (c) Skill-only strategy: no new tool surface, just document the orientation workflow (note: `get_repo` was removed for no use-case — additions must earn it)

## Open Questions

- Does the GraphQL one-shot (single call: description + languages + tree entries with lineCount/language) win on output quality AND token cost vs the current 3-REST chain? Measure in Phase B.
- How does `/readme` behave on repos with no README, or repos with multiple README variants (`README.md` + `README.rst`)? Test in Phase B.
- Is `/community/profile` `files` map reliably populated (paths vs just presence flags)? Check in Phase B.
- Is adding tool surface justified? The user removed `get_repo` for no use-case — any new tool must demonstrate a concrete orientation benefit that skill guidance alone cannot provide.

## Quellen

- `gh-cli-reference: docs_github_com_en_rest_repos_contents` (readme, contents endpoints)
- `gh-cli-reference: docs_github_com_en_rest_metrics_community` (community/profile endpoint)
- `gh-cli-reference: docs_github_com_en_graphql_reference_git` (Tree/Blob/TreeEntry fields)
- `gh-cli-reference: docs_github_com_en_graphql_reference_repos` (Repository fields, languages)
