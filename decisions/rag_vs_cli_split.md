# RAG-vs-CLI Split (retrieval-mode surface)

## Status Quo (IST)

Two retrieval modes on the gh-cli surface. Split criterion = whether artifact identity is known BEFORE the call, not data type.

- **RAG-semantic (identity unknown, fuzzy query → candidate set):** `index_issues` → `github_issues`, `index_discussions` → `github_discussions`, `index_releases` → `github_releases`. Each fetches, strips noise, writes per-item MDs, indexes into a persistent RAG collection; agent queries via `rag-cli search_hybrid`.
- **CLI-direct (identity known → exact lookup):** `search_repos`, `search_code`, `get_repo_tree`, `get_file_content`, `repo_freshness`, `download_files`, plus issue-management (`create_issue`, `update_issue`, `list_issues`, `get_issue`, `delete_issue`).
- `grep_file` + `grep_repo` REMOVED (files deleted from `src/github/`, deregistered from CLI). Both were client-side composites over `get_repo_tree`/`get_file_content` helpers — no own GitHub endpoint. `search_code` (server-side indexed full-text) supersedes them for foreign-repo pattern search.

## Evidenz

- `grep_repo` code-level failure modes (client-side, not "server-side filtering"): `filter_by_pattern` caps candidates at 50 BEFORE the `max_files` slice → files past the 50th invisible, unrecoverable by raising `max_files`; Contents-API 1 MB limit → large files silent no-match; `re.compile` no flags (case-sensitive). DockDoor case (2026-05-30): `search_code` 6 hits immediately, `grep_repo` 0 after 50 downloads. `grep_repo` = N+2 sequential REST calls vs `search_code` single indexed call. → `decisions/OldThemes/rag_vs_cli_split/grep_removal_2026-06-02.md`, `grep_repo_ephemeral_rag_2026-06-01.md`.
- Two-mode split rationale + release/commit/raw-issue-primitive removals; usage sample of 97 CLI invocations showed 0 calls to `list_commits`/`compare_commits`. → `decisions/OldThemes/rag_vs_cli_split/tool_surface_2026-05-30.md`.

## Offene Fragen

- Ephemeral-RAG (24h TTL) for aggregated searches (`search_repos`/`search_code`) — proposed, NOT built. Worth it only if result-sets larger than the current fixed cap are wanted; gated on GitHub Search pagination cost.
- Residual niche for local grep: file types GitHub Code Search does not index (CSV/TSV/data) — currently uncovered after grep removal.
