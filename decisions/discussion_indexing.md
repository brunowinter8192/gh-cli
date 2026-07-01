# Discussion Indexing (index_discussions)

## Status Quo (IST)
- Tool `index_discussions` (`index_discussions_workflow()` in `src/github/index_discussions.py`), gh-cli subcommand: `index_discussions <query> <repo> [--limit 30]`.
- Query: hard-capped to 3 keywords (`query.split()[:3]`); 0-result fallback drops last keyword 3→2→1, then errors; empty/whitespace query → guard error.
- Search: `search_discussions_raw()` → GraphQL `search(query: "<kw> repo:<repo>", type: DISCUSSION, first: limit)`; returns `(discussionCount, numbers[:limit])`. `repo:` injection confirmed working (probe: `memory repo:gastownhall/beads` returned all 23 beads discussions).
- Fetch: in-process `get_discussion_workflow(owner, repo, num)` — one GraphQL call per thread (body + comments in natural chronological API order + accepted answer). `comment_limit=100` (API per-page max); no comment re-sorting.
- Strip: `strip_noise()` (in `src/github/discussion_cleaning.py`, imported by `index_discussions.py`) — pure noise pass, mcp-free; strips 12 noise classes + 1 safety pass: (1) `DOSU_FOOTER` — `<!-- Dosu Comment Footer -->` through first badge line within 20 lines (hard invariant: no threaded-reply `^\s*>\s*\*\*@` in block); (2) `DOSU_GREETING` — `<!-- Greeting -->` standalone line + next non-blank line; (3) `ISSUE_TEMPLATE_CHECKLIST` — `### 🔎 Search before asking` and `### 🤖 Consult the online AI assistant` headings + their `- [x]` checkbox lines; (4) STANDALONE BADGE LINE — any line where `_is_badge_line()` is True (catches markerless/blockquoted/orphaned dosu badges without a preceding footer marker); (5) `DOSU_FOOTER_TEXT` — blockquoted/email-rendered dosu footer prose (no HTML marker, no badge): line stripped of leading `>_* ` starts with one of `'To reply, just mention'` / `'Docs are dead. Just use'` / `'Share context across your team and agents. Try'` AND line contains `@dosu` or `dosu.dev`; Chinese variants: `回复时只需提及` + `@dosu`, or `已经过时` + `Dosu`/`dosu.dev`; (6) `DOSU_MARKERLESS_GREETING` — marker-less dosu greeting (email-rendered, no `<!-- Greeting -->` present): `_is_dosu_markerless_greeting()` — after `re.sub(r'^[\s>_*]+', '', line.replace('&nbsp;', ' '))`, line starts with `Hi @` / `你好@` / `你好 @` AND contains `Dosu` AND contains (`helping`+`team`) or (`帮助`+`团队`); user-quoted attribution blocks preserved because their stripped form starts with `@user**:`, not `Hi @` / `你好@`; (7) `DOSU_ANSWER_MARKER` — inline `<!-- Answer -->` sub; (8) `DOSU_GREETING_INLINE` — inline `<!-- Greeting -->` sub (catches `> **@dosubot**: <!-- Greeting -->` threading pattern; `<!-- Answer|Greeting -->` unified regex); (9) `GH_SCREENSHOT_IMG` — `<img … github.com/user-attachments/assets/…>` tags entirely; (10) `FAILED_UPLOAD` — `![Uploading …]()` empty-URL markers; (11) `MD_IMG` — `![alt](url.png|jpg|gif|svg|webp)` markdown images by file extension (`MD_IMG_RE`); (12) `no-space safety net` — `re.sub(r'\S{1000,}', '', line)` last, after all other subs. Hard invariant: no kept line contains a `\S{1000,}` run. `strip_discussion_noise()` (in `index_discussions.py`) — calls `strip_noise()` then applies format logic: title extraction (`## ` line → H1 via `build_discussion_md`), metadata drop (`**Category:**` etc.), `[ANSWER]` dedup (drops in-list copy, keeps `### Accepted Answer` section).
- Redaction: `redact_tokens()` applied to final MD string — patterns `ghp_[A-Za-z0-9]+` and `github_pat_[A-Za-z0-9_]+` → `[REDACTED]`.
- Output: per-thread MD `<repo_basename>__<num>.md` → `RAG/data/documents/github_discussions/` (overwrite).
- Index: `rag-cli index --collection github_discussions` via subprocess (synchronous). Dedup by content-hash (skip unchanged, re-index changed). Failure (non-zero exit) raises `RuntimeError` — busy/locked detected via stderr keywords, message includes manual recovery command (`rag-cli index --collection github_discussions`); never silent.
- `DEFAULT_LIMIT = 30`. Auth via `graphql_query()` (`graphql_client.py`) → `build_headers()` (no token in artifacts).
- `get_discussion_workflow()` signature: `(owner, repo, number, comment_limit=100)` — `comment_sort` removed; comments rendered in natural chronological order (GitHub GraphQL `comments(first:N)` returns creation-order); `comments(first: $commentLimit)` cap is `min(comment_limit, 100)` (API per-page max).
- Retrieval of indexed discussions: `rag-cli search_hybrid "<terms>" github_discussions`.

## Evidenz

Probe on `gastownhall/beads` (2026-05-30). Report: `decisions/OldThemes/discussion_indexing/probe_beads_2026-05-30.md`. Dataset: 23 discussions, full corpus.

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

**Strip validation v1 (2026-06-17, 6-class only):** `dev/discussion_cleaning/A_strip_validation_reports/validation_20260617_203934.md` — 39/40 files cleared; 1 residual (`MinerU__4820.md`, 6,299 chars): blockquoted camo badge 25 lines after marker, no marker at its local position.

**Strip validation v2 (2026-06-17, +badge-line strip +no-space net):** `dev/discussion_cleaning/A_strip_validation.py` · report: `dev/discussion_cleaning/A_strip_validation_reports/validation_20260617_205746.md` · dataset: 78 MDs (in-memory, read-only). Note: this validation runs `strip_discussion_noise()` (noise + format pass combined); the reclean script below runs `strip_noise()` only (noise pass only — preserves headings/metadata already dropped from built MDs).

| Metric | Before | After |
|---|---|---|
| Corpus peak no-space run (chars) | 6,299 | 457 |
| Files with run > 1,500 chars | 40 | 0 ✅ |
| Total chars removed | — | 430,624 |
| Files changed | — | 78 / 78 |

Content preservation (4 spot-check files): all comment attribution headers, threaded replies, and content section headings preserved at identical counts before/after.

**Reclean round 1 (2026-06-17):** `dev/discussion_cleaning/reclean_existing_mds.py --apply` · report: `dev/discussion_cleaning/reclean_reports/reclean_apply_20260617_213527.md` · dataset: 78 existing MDs (written before strip_noise existed). Backup: `github_discussions_backup_20260617_213527`.

| Metric | Value |
|---|---|
| Files changed (noise removed) | 44 / 78 |
| Files unchanged (no noise) | 34 / 78 |
| Total chars removed | 430,020 |
| Corpus peak no-space run after | 457 ✅ |
| `## ` heading count identical per file | ✅ PASS |

**Reclean round 2 (2026-06-17) — 3 new sub-categories (DOSU_FOOTER_TEXT, DOSU_GREETING_INLINE, MD_IMG):** `dev/discussion_cleaning/reclean_existing_mds.py --apply` · report: `dev/discussion_cleaning/reclean_reports/reclean_dryrun_20260617_224340.md` · dataset: same 78 MDs post round-1. Backup: `github_discussions_backup_20260617_224340`. Change-detection upgraded to `.rstrip()` comparison (eliminates trailing-whitespace-only rewrites).

| Metric | Value |
|---|---|
| Files changed | 4 / 78 (MinerU__4820, 4878, 4237, 3309) |
| Total chars removed | 702 |
| Corpus peak no-space run after | 457 ✅ |
| `## ` heading count identical per file | ✅ PASS |
| Citation links `[[N]](url)` in live corpus | 120 intact ✅ |
| MinerU__4878 `主题` question lines | 4 / 4 kept ✅ |

Per-file breakdown: MinerU__4820 (403 chars — Chinese DOSU_FOOTER_TEXT × 2, inline Greeting × 2); MinerU__4878 (121 chars — bare DOSU_FOOTER_TEXT); MinerU__4237 (94 chars — MD_IMG logo); MinerU__3309 (65 chars — blockquoted DOSU_FOOTER_TEXT).

**Reclean round 4 (2026-06-17) — DOSU_MARKERLESS_GREETING:** `dev/discussion_cleaning/reclean_existing_mds.py --apply` · report: `dev/discussion_cleaning/reclean_reports/reclean_dryrun_20260617_230019.md` · dataset: same 78 MDs post round-2. Backup: `github_discussions_backup_20260617_230019`.

| Metric | Value |
|---|---|
| Files changed | 4 / 78 (MinerU__5076, 5129, 4820, 4878) |
| Total chars removed | 349 |
| Corpus peak no-space run after | 457 ✅ |
| `## ` heading count identical per file | ✅ PASS |
| Standalone greeting residuals | 0 ✅ |
| Citation links `[[N]](url)` | 120 intact ✅ |
| MinerU__4878 `主题` question lines | 4 / 4 kept ✅ |

Per-file breakdown: MinerU__5076 (93 chars — `Hi @fancyerii! … helping the OpenDataLab team.`); MinerU__5129 (93 chars — `Hi @daisail0! … helping the OpenDataLab team.`); MinerU__4820 (86 chars — `Hi @mmMm128! … helping the MinerU team.`); MinerU__4878 (59 chars — `Hi @qyb320! I'm Dosu&nbsp;and I'm helping the MinerU team.` — `&nbsp;` normalization required). 2 user-quoted attribution lines in MinerU__3309 and MinerU__4820 correctly preserved (stripped form starts with `@user**:`, not `Hi @`).

## Offene Fragen
- Freshness / re-index cadence / purge policy for `github_discussions` (undefined, same open question as `github_issues`).
- Shared collection for all repos or per-repo collections? (same open question as `github_issues`).
- No floor currently applied (all 23 beads threads indexed). For large repos with >50 discussions and >40% zero-comment fraction, a `comment_count >= 1` floor may be appropriate.

## Quellen
- `decisions/OldThemes/discussion_indexing/probe_beads_2026-05-30.md`
- `decisions/OldThemes/discussion_indexing/feasibility.md`
