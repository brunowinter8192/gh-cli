# dev/issue_indexing/

## Purpose

Measurement probe for the issue-indexing pipeline: fetch GitHub issues matching a query and render them to a single MD, before any RAG indexing. First measurement step that informed `decisions/issue_indexing.md`.

## Scripts

### 01_fetch_repo_content.py (273 LOC)
**Purpose:** Fetch GitHub issues matching a query (issues-only, PRs dropped) and render to per-issue MDs. Self-contained: search logic inlined (token resolution + direct `requests`); content fetched via `cli.py` subprocess. Applies a noise filter to strip metadata/boilerplate. No RAG indexing.
**Usage:** `.venv/bin/python dev/issue_indexing/01_fetch_repo_content.py [--query Q] [--repo owner/repo] [--top-n N] [--out-dir DIR]`
**Flags:** `--query` (default `streaming`); `--repo` (default `anthropics/claude-code`); `--top-n` (default 100); `--out-dir`.
**Output:** per-issue MDs to `--out-dir`; measurement summary (issues fetched, MDs written, total KB) printed to stdout. Archived measurement outputs: `md/01_streaming_claude-code.md`, `md/01_streaming_issues_top100.md`.
