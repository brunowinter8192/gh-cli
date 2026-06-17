# Issue Indexing (index_issues)

## Status Quo (IST)
- Tool `index_issues` (`index_issues_workflow()` in `src/github/index_issues.py`), gh-cli subcommand: `index_issues <query> <repo> [--limit 30]`.
- Query: hard-capped to 3 keywords (`query.split()[:3]`); 0-result fallback drops last keyword 3→2→1, then errors; empty/whitespace query → guard error.
- Search: `search_raw()` → `GET /search/issues?q="<kw> repo:<repo> is:issue"`, `per_page=min(limit,100)`, relevance order; returns top-`limit` issue numbers.
- Fetch: in-process `get_issue_workflow` + `get_issue_comments_workflow`; `strip_noise` (drops title/metadata/checklist) + `strip_comments_noise` (drops bot comments, Author/Date, quote lines) then `strip_generic_noise` (from `src/github/text_cleaning.py`) applied additively to both body and comments — removes `<img\b[^>]*>` HTML image tags, `!\[[^\]]*\]\([^)]+\)` markdown images (non-empty URL), `data:image/...;base64,...` bare data-URIs, `!\[Uploading...\]\(\)` failed uploads, and any `\S{1000,}` no-space run; per-issue MD `<repo_basename>__<num>.md` → `RAG/data/documents/github_issues/` (overwrite, no fetch-skip).
- Index: `rag-cli index --collection github_issues` via subprocess (synchronous). Dedup by content-hash (skip unchanged, re-index changed). Failure (non-zero exit) raises `RuntimeError` — busy/locked detected via stderr keywords, message includes manual recovery command (`rag-cli index --collection github_issues`); never silent.
- `DEFAULT_LIMIT = 30`. No sleeps. Auth via `build_headers` header (no token in artifacts).
- Retrieval of indexed issues: `rag-cli search_hybrid "<terms>" github_issues`.

## Evidenz
Indexing baseline (this session — `workflow.py index-dir` on 100 staged `anthropics/claude-code` "streaming" issues, embedding-8b; raw log `/tmp/gh_index.log`, one-off run not a persisted dev/ report):
- 100 issues → 606 chunks (avg 6.06/issue); real 706s (~11.8 min), user 4.4s → embedding-server-bound (~7s/issue, ~1.16s/chunk). 0 skipped, 0 adopted.
- Fetch: 2 core calls/issue; 200 for 100 = ~4% of 5000/hr core budget. Embedding dominates; search never the bottleneck.
- Dedup idempotent: post-build smoke `--limit 1` on an unchanged issue → 0 new chunks.

**Issue corpus re-clean (2026-06-18) — strip_generic_noise pass:** `dev/issue_cleaning/reclean_issues.py --apply` · report: `dev/issue_cleaning/reclean_reports/reclean_dryrun_20260618_002830.md` · dataset: 103 MDs, `data/documents/github_issues/`. Backup: `github_issues_backup_20260618_002830`.

| Metric | Value |
|---|---|
| Files changed | 18 / 103 |
| Total chars removed | 16,015 |
| Corpus peak no-space run — before | 3,137 |
| Corpus peak no-space run — after | 784 ✅ |
| `<img>` tag survivors (live corpus) | 0 ✅ |
| Markdown image survivors | 0 ✅ |
| No-space runs > 1000 (live corpus) | 0 ✅ |

Noise breakdown: 38 `<img>` tags (mix of `width+height+alt+src` and `width+alt+src` variants — both caught by `<img\b[^>]*>`), 12 markdown images (`![image](github.com/.../assets/<uuid>)` without file extension — caught by `[^)]+` broad pattern), 2 Cloudflare/Datadome opaque cookie blobs >1000 chars (stripped by `\S{1000,}` net in patchright__76 and curl_cffi__463). False-positive guard: `[^)]+` (non-empty URL) prevents matching literal `![]()` code examples in prose (confirmed in MinerU__4986 discussion corpus). Real issue text (EN/CN descriptions, error messages, code blocks, stack traces) intact across all 18 changed files.

## Recommendation (SOLL)
- **N=30 (Keep)** — default `--limit`, coverage-based (top-30 relevance carries the signal). PENDING eval: "rank 31-100 adds no marginal insight" is unmeasured — a recall eval (index top-100, representative queries, check if any answer comes from rank 31-100) would confirm.
- **Query max-3 + fallback 3→2→1 (Keep)** — robust regardless of GitHub issue-search AND/OR semantics. Pending: empirical check of multi-word issue-search semantics.
- **Dedup via index-dir content-hash (Keep)** — no wrapper-side dedup.

## Offene Fragen
- Wrapper's internal index-dir is synchronous (blocks ~N×7s for large N) — async/background variant for big N?
- Freshness / re-index cadence / purge policy for github_issues (undefined).
- Shared `github_issues` collection for all repos, or per-repo collections?

## Quellen
- `decisions/OldThemes/repo_issue_indexing/roadmap.md`, `decisions/OldThemes/repo_issue_indexing/wrapper_build.md`
