# Releases RAG — Design Rationale

## Use Cases

Two distinct use cases for release data:

1. **Single-latest-release inspection** — "what changed in the latest release?" Minor use case; `get_release` (REST, one call) adequately served it.
2. **Cross-release feature search** — "since when does /workflow exist?", "does our installed version have feature X?", "what releases mention dynamic workflows?" This is the real driver. No CLI-call model can serve it: the agent would have to page through O(100) releases manually, reading each body. RAG makes the entire release pool searchable in one query.

Use case 2 is the war-decisive concern. Two CLI tools for inspection are the wrong unit of work; a searchable index is the right one.

## Why RAG Over Two CLI Tools

`list_releases` (paginated list, body truncated to 300 chars) + `get_release` (single release by tag) require the agent to already know WHICH release it cares about. For feature-search (when did X appear?), the agent has no prior knowledge of the release tag — it would need to page through the list reading each entry. That is O(100) tool calls for a 100-release repo.

RAG collapses this to one `search_hybrid` call that returns the relevant release(s) by semantic similarity to the feature query.

## Per-Repo Collection Isolation

Collection name: `github_releases__{owner}__{repo}` (double underscore separates owner, repo, and kind; natural hyphens in repo name preserved). Per-repo collection = isolation by construction:

- Cross-repo dilution eliminated (anthropics/claude-code releases don't contaminate a search against another repo's releases).
- Different repos indexed independently; agent passes the explicit collection name — no ambiguity.
- Alternative considered and rejected: single `github_releases` collection with owner/repo as metadata filter. Rejected because: (1) `rag-cli search_hybrid` has no metadata-filter param; (2) per-repo isolation is sufficient and simpler.

## Clean-Before-Index Janitor

On every `index_releases` call: delete the RAG collection + rmtree the doc dir, then recreate both from scratch. Rationale: releases are append-only in practice (tags don't change bodies after publish), but there is no TTL or diff mechanism in the indexer. Wipe-and-reindex is the simplest correct strategy — idempotent, no stale-chunk risk, no partial-update edge cases. Cost: O(100) releases × ~1 chunk each = negligible reindex time.

## Endpoint Facts

- `GET /repos/{owner}/{repo}/releases` — returns full release objects including `body` (full changelog text, not truncated).
- `per_page` max: 100. No `sort` param — API always returns newest-first.
- Hard limit: 100 releases fetched (single call, no pagination). Rationale: cross-repo feature search is primarily useful on recent history; very old releases are low-signal noise. Revisit if a 100+ release repo becomes a use case.
- Assets excluded naturally: asset metadata is in the `assets` array, not in `body` — not written into the MD, not indexed.

## Noise-Strip Set (strip_release_noise)

Applied to every release body before writing the MD:

| Pattern | Why strip |
|---|---|
| `## What's Changed` header line | Section title adds no searchable content |
| `**Full Changelog**: <url>` lines | URL noise; not searchable feature content |
| `## New Contributors` section (header + `@user first contribution` lines until next `##`) | Contributor attribution is not feature content |
| `by @username in #1234` / `by @username in https://...` suffix on bullet lines | PR attribution noise; the feature description precedes it |

Claude Code release bodies are already clean (mostly feature bullet lists). Strip set is robustness for other repos.

## Downstream dependency

`index_releases_workflow()` (`index_releases.py`) is functionally blocked by a bug in `rag-cli delete`: the janitor calls `rag-cli delete --collection <name>` before re-indexing, but the current delete implementation leaves the `indexed_files` manifest intact. On the next `workflow.py index-dir` run, the indexer sees all files as already-hashed in the manifest and skips them — producing an empty collection. The wipe-and-reindex strategy only works correctly when delete also clears the manifest.

See `decisions/OldThemes/delete_manifest_orphans.md` in the rag-cli project for the full investigation and fix status.
