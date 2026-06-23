# get_file_content — large files (>1MB) — 2026-06-23

## Problem

`get_file_content` returned empty content (no error, "Lines: 1 total") for any file >1MB. Root: `fetch_file_content` uses the Contents API (`/repos/{o}/{r}/contents/{path}`), which inlines base64 only ≤1MB; larger files return `content=""` / `encoding="none"`. `decode_content` only decoded `encoding=="base64"`, else fell through to `return content` (empty) SILENTLY. offset/limit applied AFTER decode → operated on the empty string. Repro: `MuRongPIG/Proxy-Master/http.txt` (1.8MB) → empty.

## Investigation — GitHub API size tiers + NO partial read

From `gh-cli-reference` (GitHub REST docs):
- Contents API: ≤1MB full base64 inline; **1–100MB** retrievable only via `raw` media type or the response's `download_url` (raw.githubusercontent.com, no 1MB cap); **>100MB** not supported by the endpoint at all.
- Git Blobs API: base64, caps at **100MB**.
- **NO GitHub API supports partial / range reads** — no byte-range or line-range parameter on Contents API, Blobs API, raw media type, or GraphQL Blob (`isTruncated` is server-decided, not controllable). Confirmed across all four. → a head/partial read cannot come from the API.

## Decision — three-tier dispatch + delegate partial-read to local FS

In `get_file_content_workflow`, dispatch on Contents-API `size` (response carries `size` + `download_url` even for >1MB):
- **≤1MB:** unchanged — base64 inline, offset/limit apply.
- **1–100MB:** stream `download_url` to `/tmp/gh-cli_{owner}_{repo}_{path}` (requests stream + iter_content, timeout=30, never hold in memory), return the /tmp path + size + hint. offset/limit do NOT apply here — the caller reads the /tmp file with its OWN Read tool.
- **>100MB:** explicit error, no download.
- Never silently return empty.

**Why download-to-tmp (not `raw` media type inline):** the partial-read GitHub can't do, the LOCAL filesystem can — once on disk, the Read tool gives offset/limit/head for free, and big content stays OUT of the agent context (vs `raw` inline which floods context).

IST: `decisions/tool_design.md` (`get_file_content` line) + `src/github/DOCS.md`. Implementation: `src/github/get_file_content.py` (104→168 LOC). Smoke: `dev/repo_exploration/probe_large_file.py` (3 tiers, 3/3). Live-verified: 1.8MB http.txt → /tmp path, head readable locally.

## Sources

- `gh-cli-reference`: `docs_github_com_en_rest_repos_contents.md` (size tiers, raw/object media types, download_url), `docs_github_com_en_rest_git_blobs.md` (100MB cap), `docs_github_com_en_graphql_reference_git.md` (Blob.isTruncated/text — no range param).
