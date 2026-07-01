# Release Indexing (index_releases)

## Status Quo (IST)

- Tool `index_releases` (`index_releases_workflow(repo)` in `src/github/index_releases.py:23`), gh-cli subcommand: `index_releases <repo>`.
- Single fixed collection `github_releases` (`index_releases.py:17`), fixed doc dir `RAG_ROOT/data/documents/github_releases/` — regardless of repo. Agent always queries `rag-cli search_hybrid "<feature query>" github_releases`; no per-repo collection name.
- Clean-before-index janitor (`janitor_clean`, `index_releases.py:51`): `rag-cli delete --collection github_releases` + `rmtree` doc dir before every run → exactly one repo's releases present at a time. Raises BEFORE rmtree on delete failure (busy/lock) → old state preserved on failure.
- Fetch: `GET /repos/{owner}/{repo}/releases`, `per_page=100`, newest-first, single call, no pagination → hard cap 100 releases. Full `body` (untruncated changelog); assets excluded (in `assets` array, not `body`).
- `strip_release_noise` per body before MD write: `## What's Changed` header, `**Full Changelog**: <url>` lines, `## New Contributors` section, `by @user in #N`/URL PR-attribution suffixes.

## Evidenz

- Use-case driver = cross-release feature search ("since when does feature X exist?") — O(100) CLI calls collapse to one `search_hybrid`. Single-latest inspection (minor use-case) served by REST. Single fixed collection supersedes per-repo `github_releases__{owner}__{repo}` isolation (agent had to track per-repo names). Metadata-filter alternative rejected: `rag-cli search_hybrid` has no metadata-filter param → clean-before-index wipe is simpler. → `decisions/OldThemes/release_indexing/redesign.md`.

## Offene Fragen

- 100-release hard cap: revisit if a 100+ release repo becomes a use-case.
- Janitor correctness depends on `rag-cli delete` clearing the `indexed_files` manifest; if delete leaves the manifest, the next index skips all files as already-hashed → empty collection.
