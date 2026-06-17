# Discussion Indexing (index_discussions)

## Status Quo (IST)
- Tool `index_discussions` (`index_discussions_workflow()` in `src/github/index_discussions.py`), gh-cli subcommand: `index_discussions <query> <repo> [--limit 30]`.
- Query: hard-capped to 3 keywords (`query.split()[:3]`); 0-result fallback drops last keyword 3→2→1, then errors; empty/whitespace query → guard error.
- Search: `search_discussions_raw()` → GraphQL `search(query: "<kw> repo:<repo>", type: DISCUSSION, first: limit)`; returns `(discussionCount, numbers[:limit])`. `repo:` injection confirmed working (probe: `memory repo:gastownhall/beads` returned all 23 beads discussions).
- Fetch: in-process `get_discussion_workflow(owner, repo, num)` — one GraphQL call per thread (body + comments in natural chronological API order + accepted answer). `comment_limit=100` (API per-page max); no comment re-sorting.
- Strip: `strip_discussion_noise()` extracts title from `## ` line; drops metadata block (`**Category:**`, `**Author:**`, `**Created:**`, `**Upvotes:**`, `**Status:**`); deduplicates `[ANSWER]`-tagged comment by dropping the in-list copy and keeping the `### Accepted Answer` section. Also strips 6 noise classes: (1) `DOSU_FOOTER` — `<!-- Dosu Comment Footer -->` through first badge line within 20 lines (hard invariant: no threaded-reply `^\s*>\s*\*\*@` in block); (2) `DOSU_GREETING` — `<!-- Greeting -->` + next non-blank line; (3) `DOSU_ANSWER_MARKER` — inline `<!-- Answer -->` tag removed from line, surrounding text kept; (4) `GH_SCREENSHOT_IMG` — `<img … src="https://github.com/user-attachments/assets/…">` tags stripped entirely; (5) `FAILED_UPLOAD` — `![Uploading …]()` empty-URL markers; (6) `ISSUE_TEMPLATE_CHECKLIST` — `### 🔎 Search before asking` and `### 🤖 Consult the online AI assistant` headings + their `- [x]` checkbox lines, boundary: heading + checkboxes only (description section kept).
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

**Noise audit (2026-06-17):** `dev/discussion_cleaning/audit_discussion_noise.py` · report: `dev/discussion_cleaning/audit_reports/audit_20260617.md` · dataset: 78 MDs, `data/documents/github_discussions/`, opendatalab/MinerU + gastownhall/beads repos.

| Noise class | Files hit | Hits | Chars | Risk hits | Verdict |
|---|---|---|---|---|---|
| DOSU_FOOTER | 41 / 78 | 99 | 413,707 | 0 | SAFE TO STRIP |
| DOSU_GREETING | 17 / 78 | 17 | 1,813 | 0 | SAFE TO STRIP |
| DOSU_ANSWER_MARKER | 41 / 78 | 99 | 1,485 | 0 | SAFE TO STRIP |
| GH_SCREENSHOT_IMG | 13 / 78 | 15 | 2,066 | 0 | stripped (user decision) |
| FAILED_UPLOAD | 1 / 78 | 1 | 25 | 0 | SAFE TO STRIP |
| ISSUE_TEMPLATE_CHECKLIST | 3 / 78 | 6 | 1,836 | 0 | SAFE TO STRIP |

Root cause of 15/78 indexing failures: DOSU_FOOTER blocks contain base64-encoded SVG badge links (up to 6,299 chars without a space), which the char-based chunker emits as a single oversized chunk → embedding server HTTP 400 abort.

**Strip validation (2026-06-17):** `dev/discussion_cleaning/A_strip_validation.py` · report: `dev/discussion_cleaning/A_strip_validation_reports/validation_20260617_203934.md` · dataset: 78 MDs (applied new strip in-memory, read-only).

| Metric | Before | After |
|---|---|---|
| Corpus peak no-space run (chars) | 6,299 | 6,299 * |
| Files with run > 1,500 chars | 40 | 1 * |
| Total chars removed | — | 421,565 |
| Files changed | — | 78 / 78 |

*1 residual file (`MinerU__4820.md`): camo-proxied badge appears inside a `> ` blockquote 25 lines after the `<!-- Dosu Comment Footer -->` marker; FOOTER_LOOKAHEAD=20 stops at an earlier badge line (index 38), leaving the blockquoted badge (index 56) undetected. This edge case has no preceding marker at its location and falls outside the 6 audited classes.

## Recommendation (SOLL)
- **N=30 (Keep)** — mirrors `index_issues`; covers full beads corpus (23 < 30); appropriate cap for larger repos.
- **Query max-3 + fallback 3→2→1 (Keep)** — mirrors `index_issues`; GraphQL `search(type:DISCUSSION)` honors same qualifiers.
- **Dedup via index-dir content-hash (Keep)** — no wrapper-side fetch-skip; always overwrite → catches updated discussions.
- **6-class noise strip (Keep)** — audit shows all 6 classes SAFE TO STRIP (0 risk hits); validation shows 39/40 previously oversized files drop below 1,500-char threshold (421,565 chars removed). Residual: 1 file with blockquoted badge outside marker detection range — out of scope for current 6 classes.

## Offene Fragen
- Freshness / re-index cadence / purge policy for `github_discussions` (undefined, same open question as `github_issues`).
- Shared collection for all repos or per-repo collections? (same open question as `github_issues`).
- No floor currently applied (all 23 beads threads indexed). For large repos with >50 discussions and >40% zero-comment fraction, a `comment_count >= 1` floor may be appropriate.

## Quellen
- `decisions/OldThemes/repo_discussion_indexing/probe_beads_2026-05-30.md`
- `decisions/OldThemes/repo_discussion_indexing/feasibility.md`
