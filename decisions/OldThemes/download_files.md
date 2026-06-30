# download_files — file-to-disk download tool

Process record for the `download_files` tool. Final state lives in `decisions/tool_design.md`.

## Problem

`get_file_content` surfaces a file's content into the assistant's context only — no disk write. Missing capability: pull 1-2 specific files from a repo onto disk, no clone, no RAG index. Use case (orchestrator → worker): download external reference file(s) into a worker's worktree → worker READS them → not committed/merged → vanish with the worktree.

## Design decisions

| Topic | Options | Chosen | Reason |
|---|---|---|---|
| Download path | (a) tiered base64-decode (≤1 MB) + stream (>1 MB) like get_file_content; (b) unified `_stream_download` for ALL sizes via `download_url` | (b) | base64 path `.decode("utf-8")` breaks binary files; `download_url` present for every file in Contents API response; one binary-safe path |
| Target layout | flat `<dest>/<basename>` vs preserve repo-relative path | flat | matches "1-2 specific files" use case; collision risk on same-basename accepted |
| Multi-path error handling | fail-fast vs per-path report | per-path report | one bad path (404 / dir / oversize) must not abort the good downloads; written + failed listed separately |
| Code reuse | reimplement vs import from get_file_content | import `fetch_file_content`, `_stream_download`, `_SIZE_API_MAX` | no duplication; existing fetch already carries `raise_for_status()` (404 → per-path exception) |

## Per-path rules

dir (list response) → FAILED; `download_url` None (submodule/symlink) → FAILED; `size` > 100 MB → FAILED; else stream raw bytes to `<dest>/<basename>`. `os.makedirs(dest, exist_ok=True)` once before the loop.

## Tool shape

`download_files owner repo path [path ...] --dest <dir>` (--dest default "."). Returns per-path report (written paths + bytes, failed paths + reason). Surfaced in `skills/gh-cli-search` with the worker-reference use case.
