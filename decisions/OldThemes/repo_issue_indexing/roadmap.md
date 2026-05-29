# Repo Issue Indexing — Roadmap & Findings

Process documentation for the planned "index a repo's issues into RAG" capability. Not yet in prod.

## Idea

Reddit-style query-driven indexing applied to GitHub. One query pulls the most relevant GitHub issues for a repo, renders per-issue MDs, dedups, indexes into RAG. The agent then does a few broad vector searches instead of many fine-grained tool calls. Reference mechanic: `index_subreddits_workflow()` in `src/reddit/index_subreddits.py` (Reddit project) — sub → repo mapping.

Conceptual frame: a GitHub **issue** ≈ a Reddit **post** (discussion layer → index it). PRs/code ≈ the code layer (live exploration tools, not indexed).

## Scope decisions

- **Issues only.** PRs dropped from the index. Rationale: for closed-product / public-issue-tracker repos (e.g. `anthropics/claude-code`) external PRs are rarely merged = low signal (the heaviest PR in the probe was a community Rust-rewrite, 2022 files, never to be merged). Empirical: across 97 extracted real gh-cli invocations, `get_pr` / `get_pr_files` / `list_repo_prs` = 0 calls.
- Discussions / Commits / Releases: deferred, not in the first index.
- PR **tools** in the CLI (`list_repo_prs`, `get_pr`, `get_pr_files`): DECIDED — remove from the CLI entirely (never used: 0 calls; out of the index anyway). Executed in the feature-build block; on removal, `tool_design.md` / `api_strategy.md` / `delivery.md` IST drop from 20→17 tools, 17→14 REST.

## Empirical findings (this session — `anthropics/claude-code`, query "streaming")

- `total_count`: issues 1236, PRs 10. One-word query already swamps issues; relevance-capping is mandatory (cannot index 1236).
- GitHub Search API limits (verified): max **100 results per call** (`per_page` cap); only the **first 1000** retrievable (page 11 → `422 "Only the first 1000 search results are available"`). Even "all" caps at 1000.
- Rate limits (verified via `/rate_limit`): **core** (REST `get_issue`/`get_issue_comments`) = 5000/hour; **search** (`search_items`) = 30/minute. Each issue costs 2 core calls. Top-100 = 1 search + 200 core ≈ 4% of the hourly core budget. Search is never the bottleneck; content-fetch is the volume driver.
- Sort: `search_items` default `best_match` (GitHub relevance). Top-N by relevance carries the signal; the tail (rank ~300+) are tangential "streaming" mentions, low value.
- KB baseline (top-100 issues, **pre-cleanup**): 888.6 KB total; per-issue min 0.89 / avg 8.88 / median 4.96 / max 80.81 KB. **Comments dominate: 531.8 KB (60%)** vs bodies 344.4 KB.

## Cleanup filter (`dev/repo_indexing/fetch_repo_content.py`)

- `strip_noise()` (issue body): strips metadata lines (Author/Created/Updated/Branch/Commits/Changed-Files/Mergeable/URL/Comments-count), tool-hint lines `[get_...]`, Preflight-Checklist + checkbox boilerplate; folds the duplicate title into the anchor. Removed only 2.2% — metadata is small.
- `strip_comments_noise()` (comments — the 60% bulk): drops entire **bot comments** (Author ends `[bot]`, e.g. github-actions duplicate-detector), strips per-comment `Author:`/`Date:`, strips `> ` quote-reply lines. Low-content/length-based dropping deferred (false-positive risk: a short comment may be a precise staff fix).

## Staging (up to the indexing threshold)

- Per-issue MDs written to `RAG/data/documents/github_issues/` named `<repo-basename>__<num>.md` (mirrors `reddit_posts/<sub>__<id>.md`). Collection name `github_issues`.
- Chunking + indexing use RAG's config **1:1** — no custom chunking. Command (verified): `cd RAG && venv/bin/python workflow.py index-dir --input data/documents/github_issues`. Indexing is triggered **jointly**, not auto-run by the staging step.
- **Status (end of this session):** 100 cleaned per-issue MDs staged in `RAG/data/documents/github_issues/` (1.0 MB; total 830.6 KB, down from 888.6 pre-cleanup −6.5%; comments 531.8 → 476.3 KB after `strip_comments_noise`; bodies unchanged 344.4 KB). At the indexing threshold. **Indexing NOT yet run** — the `index-dir` trigger + the indexing-time baseline (which decides N) is pending the feature-build session.

## Security finding & redaction precondition (this session)

The `streaming` extraction surfaced a token leak. Past sessions used inline `export GH_TOKEN="…" ; gh-cli …` (a workaround for the CC shell-snapshot staleness — see `token_resolution.md`). The Monitor_CC proxy logged those command lines; the extractor copied them verbatim into `ghcli_calls.jsonl`, which then carried the **live** `ghp_…` token (== current zshrc token) plus an old `github_pat_…`. GitHub push-protection blocked the push — the token never reached the remote.

Resolution this session: `dev/` is now gitignored (never public); local `main` was reset to the clean origin state and only the public roadmap pushed; the token-bearing commit (`ghcli_calls.jsonl`) stays on the local `dev` branch only.

PRECONDITIONS for the feature-build before ANY push:
- The extractor (`extract_ghcli_calls.py`) and the fetch/index wrapper MUST redact token patterns (`ghp_…`, `github_pat_…`) before writing any MD/JSONL artifact.
- The exposed live `ghp_…` token should be rotated (it sat in shell-history + proxy-logs + a local commit).

## Prod wrapper (target)

New gh-cli command: user gives a query (+ repo) → top-N relevant issues pulled → saved as per-issue MDs → dedup against already-indexed (Reddit-style: post-id/number + title-hash) → RAG index. The agent's job is pure **query engineering**.

Skill update required: document the new command + query-engineering guidance — single-word-leaning queries (more keywords → fewer hits), and a 0-result fallback that drops keywords 5→4→3→2→1.

## Open questions

- **N (issues per query):** derive from the indexing-time baseline (pending — first action of the feature-build session). Trade-off: latency (2 core calls + embed per issue) vs completeness vs noise down the relevance ranking. The batch is sized by the call budget, not by gut feeling; the natural unit is one search call = 100 candidates.
- **Sleep between calls:** DECIDED — no sleeps in the prod wrapper. The secondary rate-limit was never actually encountered this session (zero 403s); we do not pre-emptively defend against limits we have not hit. (The dev probe still carries 0.5s sleeps — harmless; removed when the wrapper is built.)
- **Freshness / re-index / purge policy:** issues are mutable and grow; snapshot vs re-index cadence + purge schedule undefined.
