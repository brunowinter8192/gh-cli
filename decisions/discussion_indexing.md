# Discussion Indexing (index_discussions)

## Status Quo (IST)
- Tool `index_discussions` (`index_discussions_workflow()` in `src/github/index_discussions.py`), gh-cli subcommand: `index_discussions <query> <repo> [--limit 30]`.
- Query: hard-capped to 3 keywords (`query.split()[:3]`); 0-result fallback drops last keyword 3→2→1, then errors; empty/whitespace query → guard error.
- Search: `search_discussions_raw()` → GraphQL `search(query: "<kw> repo:<repo>", type: DISCUSSION, first: limit)`; returns `(discussionCount, numbers[:limit])`. `repo:` injection confirmed working (probe: `memory repo:gastownhall/beads` returned all 23 beads discussions).
- Fetch: in-process `get_discussion_workflow(owner, repo, num)` — one GraphQL call per thread (body + comments in natural chronological API order + accepted answer). `comment_limit=100` (API per-page max); no comment re-sorting.
- Strip: `strip_discussion_noise()` extracts title from `## ` line; drops metadata block (`**Category:**`, `**Author:**`, `**Created:**`, `**Upvotes:**`, `**Status:**`); deduplicates `[ANSWER]`-tagged comment by dropping the in-list copy and keeping the `### Accepted Answer` section.
- Redaction: `redact_tokens()` applied to final MD string — patterns `ghp_[A-Za-z0-9]+` and `github_pat_[A-Za-z0-9_]+` → `[REDACTED]`.
- Output: per-thread MD `<repo_basename>__<num>.md` → `RAG/data/documents/github_discussions/` (overwrite).
- Index: `rag-cli index --collection github_discussions` via subprocess (synchronous). Dedup by content-hash (skip unchanged, re-index changed). Failure (non-zero exit) raises `RuntimeError` — busy/locked detected via stderr keywords, message includes manual recovery command (`rag-cli index --collection github_discussions`); never silent.
- `DEFAULT_LIMIT = 30`. Auth via `graphql_query()` (`graphql_client.py`) → `build_headers()` (no token in artifacts).
- `get_discussion_workflow()` signature: `(owner, repo, number, comment_limit=100)` — `comment_sort` removed; comments rendered in natural chronological order (GitHub GraphQL `comments(first:N)` returns creation-order); `comments(first: $commentLimit)` cap is `min(comment_limit, 100)` (API per-page max).
- Retrieval of indexed discussions: `rag-cli search_hybrid "<terms>" github_discussions`.

## Evidenz

Probe on `gastownhall/beads` (2026-05-30). Report: `decisions/OldThemes/repo_discussion_indexing/probe_beads_2026-05-30.md`. Dataset: 23 discussions, full corpus.

| Metric | Value |
|---|---|
| GraphQL search calls | 1 |
| `discussionCount` returned | 23 |
| Per-thread `get_discussion` calls | 23 |
| Total GraphQL calls | 24 |
| Raw size | 122.0 KB |
| Stripped size | 115.2 KB |
| Written MDs | 116.3 KB |
| Strip reduction | 5.6% |
| isAnswered threads | 0 / 23 |

Strip is much smaller than issues (~30–40%) — discussion format is mostly body text; the metadata block stripped per thread is a small fraction. The `[ANSWER]` dedup path (0 triggered in beads) is implemented for correctness on repos with answered threads.

Separate `github_discussions` collection (not merged into `github_issues`): confirmed. Discussion and issue content serve different query types; separate collections allow targeted retrieval.

## Recommendation (SOLL)
- **N=30 (Keep)** — mirrors `index_issues`; covers full beads corpus (23 < 30); appropriate cap for larger repos.
- **Query max-3 + fallback 3→2→1 (Keep)** — mirrors `index_issues`; GraphQL `search(type:DISCUSSION)` honors same qualifiers.
- **Dedup via index-dir content-hash (Keep)** — no wrapper-side fetch-skip; always overwrite → catches updated discussions.

## Offene Fragen
- Freshness / re-index cadence / purge policy for `github_discussions` (undefined, same open question as `github_issues`).
- Shared collection for all repos or per-repo collections? (same open question as `github_issues`).
- No floor currently applied (all 23 beads threads indexed). For large repos with >50 discussions and >40% zero-comment fraction, a `comment_count >= 1` floor may be appropriate.

## Quellen
- `decisions/OldThemes/repo_discussion_indexing/probe_beads_2026-05-30.md`
- `decisions/OldThemes/repo_discussion_indexing/feasibility.md`
