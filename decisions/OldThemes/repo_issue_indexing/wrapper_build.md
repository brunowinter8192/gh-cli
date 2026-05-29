# index_issues Wrapper — Build & Decisions (2026-05-30)

Build session crystallizing the issues-indexing roadmap (`roadmap.md`) into prod. This file = what was decided + built.

## Built
`index_issues` tool (`index_issues_workflow(query, repo, limit=30)` in `src/github/index_issues.py`). New gh-cli subcommand → tool count 17→18 (15 REST, 3 GraphQL). Wired in `cli.py`; documented in `skills/github-search/SKILL.md`. Commits 658f550 (feat) + 6ffa408 (empty-query guard) + d646f82 (recap), merged e157a63.

Flow: query → max-3-keyword repo-scoped search → top-N issue numbers → in-process `get_issue_workflow` + `get_issue_comments_workflow` → `strip_noise`/`strip_comments_noise` → per-issue MD `<repo>__<num>.md` → `RAG/data/documents/github_issues/` → subprocess `workflow.py index-dir`. No sleeps. Header-auth.

## Decisions

### N = 30 (default `--limit`)
Rationale: COVERAGE, not latency (user: 11min for 100 is acceptable). Top-30 by GitHub relevance carries the signal; rank 31-100 adds no marginal insight. Flag-overridable. "31-100 adds nothing" is plausible but UNMEASURED — see `decisions/issue_indexing.md` SOLL.

### Query engineering: max 3 keywords, fallback 3→2→1
- Skill mandates MAX 3 keywords; wrapper hard-caps `query.split()[:3]`.
- Most DISTINCTIVE keyword FIRST — fallback drops from the back, so the first keyword survives longest.
- 0 results → drop last keyword, retry. All-zero at k=1 → error. Empty query → guard.
- Refines the roadmap's "5→4→3→2→1" to 3→2→1 (max is 3, not 5).

### Dedup: index-dir content-hash, always-overwrite (divergence from Reddit)
RAG `index-dir` dedups by MD content-hash (`indexed_files` table → skip unchanged, adopt complete-untracked, re-index changed). The wrapper does NOT implement fetch-level skip — Reddit's `read_existing_state`/`filter_against_existing` was deliberately NOT copied. Always fetch top-N + overwrite → an issue with new comments → changed content-hash → re-indexed. Reddit's fetch-skip (net-new only) misses updates; for issues we catch them. Cost: re-fetch unchanged issues (2 core calls each), negligible vs 5000/hr.

### Noise stripping: current filters sufficient
Sampled #33949 (prose) + #60133 (shell/code + evidence tables): residual content is SIGNAL (fix instructions, repro, tables), not noise. Confirms roadmap's decision NOT to length-strip (would remove signal). Minor unstripped residue (`# Comments on …#N` header, `--- Comment N ---` separators) judged not worth the false-positive risk. No smarter filter built.

## Reuse
`client.build_headers`, `get_issue_workflow`, `get_issue_comments_workflow` (in-process, no subprocess/sleeps) + ports `strip_noise`/`strip_comments_noise`/`build_issue_md`/`search_raw` from probe `dev/repo_indexing/fetch_repo_content.py`. `run_index`/`parse_chunk_count`/`get_collection_stats` mirror `index_subreddits.py` (Reddit).

## Verified (Opus, post-merge on dev)
`cli.py --help` → 18 subcommands; empty-query guard; nonsense keyword → no-issues error; `index_issues "streaming" anthropics/claude-code --limit 1` → end-to-end, 0 new chunks (idempotent hash-skip of already-indexed issue).

## Aside: splade fix (RAG)
Indexing surfaced splade starting during index-dir. Root cause: `splade` preset `required_for: ["search","index"]` in RAG `server_utils.py`, but indexing is dense-only (sparse stays NULL) and no search/fusion path uses splade (only `backfill-splade`). Fixed → `required_for: []`. See RAG `decisions/OldThemes/splade_server_scope.md`. Also: Monitor_CC hook `block_unauthorized_background.py` whitelisted `workflow.py index-dir` so explicit background runs aren't force-flipped to foreground.
