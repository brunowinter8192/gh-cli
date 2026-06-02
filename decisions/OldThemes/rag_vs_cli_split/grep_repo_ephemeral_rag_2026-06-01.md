# grep_repo Failure + Ephemeral-RAG for Aggregated Search (2026-06-01)

Continuation of `tool_surface_2026-05-30.md`. The 2026-05-30 split kept `search_repos`/`search_code`/`grep_repo` as CLI-direct. This file revisits that, triggered by `grep_repo` being the weakest tool on the surface + the persisted-output (po) → bad-agent-grep failure pattern.

## Trigger

- `grep_repo` = weakest link. Silent false negatives (`search_strategy_fallback.md` DockDoor case). Candidate for removal.
- po problem: aggregated-search output too large → proxy persists to tmp + strips preview → agent greps the tmp file → content-greps for prose/metadata are garbage (`description`/`language` dumps, no value). This is a RULE problem (agent behavior on po), not a hook problem. The proxy preview-strip works correctly.

## grep_repo Code-Level Diagnosis (corrects the "undiagnosed" hypothesis)

`search_strategy_fallback.md` called the DockDoor false-negative "undiagnosed" and hypothesized "server-side content filtering". **Wrong — the cause is client-side, visible in code.**

`grep_repo_workflow()` (`grep_repo.py`) rebuilds grep from parts: `fetch_default_branch` → `get_tree_sha` → `fetch_tree(recursive=True)` → `filter_by_pattern` → per-file `fetch_file_content` (Contents API) → base64 decode → `re` over lines.

Two hard, code-visible failure sources:

1. **50-file cap before max_files.** `filter_by_pattern()` (`get_repo_tree.py`) truncates candidates at `PATTERN_RESULTS_LIMIT = 50` BEFORE `grep_repo_workflow` applies `matching_files[:max_files]`. Order: cap-to-50 THEN slice-to-max_files. Repo with >50 matching files → files beyond the 50th (tree order) are invisible, and the agent CANNOT recover by raising `max_files` (the cap already fired). DockDoor report "50/50 searched" with `max_files=50` = exactly this cap. `PrivateApis.swift` lay beyond the first 50 `.swift` files.
2. **Contents-API 1 MB limit.** `fetch_file_content()` uses `/contents/{path}`, which returns base64 only for files ≤1 MB. Larger files → empty content → `decode_content` returns `""` → silent no-match. Second independent cause if `PrivateApis.swift` was large.

Plus: `re.compile(pattern)` no flags — case-sensitive, no MULTILINE.

**Architecture comparison (the killer point):** `grep_repo` = N+2 sequential REST calls (branch + tree + N file downloads, each full base64). `search_code` = ONE call against GitHub's prebuilt code index, ranked, with `text_matches` fragments, no 50-cap. DockDoor: `search_code` returned 6 hits immediately; `grep_repo` returned none after 50 downloads. `grep_repo` is a worse client-side reimplementation of what GitHub does server-side.

## Tool Categorization (identity-known split from 2026-05-30)

**Intra-repo — identity known → CLI direct (keep):** `get_repo`, `get_repo_tree`, `get_file_content`, `grep_file`, `list_releases`, `get_release`. Plus `grep_repo` as a BROKEN borderline (repo known, but over-files-aggregated output + the failures above).

**Aggregated search — identity unknown → ephemeral-RAG candidate:** `search_repos`, `search_code`. The only two fuzzy-query→candidate-set tools. Exactly the ones that produce the po the agent then mis-greps. `search_repos` has `MAX_OUTPUT_CHARS = 80_000` hardcoded; 20 verbose entries breach it.

**Already RAG (persistent, unchanged):** `index_issues` → `github_issues`, `index_discussions` → `github_discussions`.

**Internal helpers (no subcommand):** `get_issue`, `get_issue_comments`, `get_discussion`.

## Ephemeral-RAG Proposal (user direction)

Aggregated searches (`search_repos`, `search_code`) → index results into RAG, agent semantic-searches instead of grepping a po. BUT different logic from the persistent issue/discussion collections: **non-persistent, 24h TTL** — DB cleaned 24h after content written. Distinct from `github_issues`/`github_discussions`.

## Assessment (Opus, pre-API-docs)

**grep_repo: replace/demote, don't fix.** Even repaired (drop 50-cap, Blobs-API for >1 MB, `re.IGNORECASE`), it stays N+2 sequential calls vs `search_code`'s single indexed call — correct-but-slow, never better on indexed file types. Only residual niche: file types GitHub Code Search does NOT index (CSV/TSV/data) — narrow. DockDoor evidence: `grep_repo` actively misleads. Proposed: `search_code` (with `repo:`) becomes primary "does pattern X exist in repo", `grep_file` stays for known file, `grep_repo` removed or shrunk to data-file niche.

**Ephemeral-RAG: two independent po-fixes, decide deliberately.**
- *Lean output* (simple): `search_repos` → one line per repo (full_name, stars, 1-line desc, url). At the current 20-result cap, no po, no RAG needed. Sufficient on its own.
- *Ephemeral RAG, 24h TTL* (heavy): worth it ONLY if we lift the 20-result cap to index large candidate pools (100+) and semantic-narrow. Real capability gain, not just po-avoidance.
- The real question is therefore NOT "RAG yes/no" but "do we want result-sets bigger than 20?" — gated on whether GitHub pagination makes big pools cheap.

## Open Questions (all gated on GitHub API-docs research)

- Does GitHub Search pagination make large result-sets (>20) cheap, or is it rate-limit-prohibitive? (`search_repos`/`search_code` currently fixed `RESULTS_PER_PAGE=20`, no cursor pagination.)
- `search_code` `repo:` qualifier coverage + rate limits + which file types it skips → determines `grep_repo`'s true residual niche.
- Do native GitHub endpoints (REST/GraphQL) already solve our problems? We only know the endpoints currently wired. GitHub has many more.
- Where do the GitHub API docs live? No `github_reference`/`gh_reference` collection exists yet (only `github-docs`, `github_issues`, `github_discussions`) → must crawl + index.

## Decision Status

PENDING — gated on GitHub API-docs research. Plan: crawl GitHub API docs (web-research skill / crawling workflow) → MDs to `RAG/data/documents/gh_reference` → index into `gh_reference` collection (likely needs creation) → decide grep_repo replace-vs-fix + ephemeral-RAG-vs-lean-output against real endpoint capabilities.

## Evidence Sources

- Code: `grep_repo.py`, `grep_file.py`, `get_repo_tree.py` (`filter_by_pattern`, `PATTERN_RESULTS_LIMIT=50`), `get_file_content.py` (`fetch_file_content` Contents API), `search_code.py`, `search_repos.py` (`MAX_OUTPUT_CHARS=80_000`), `client.py` (`RESULTS_PER_PAGE=20`).
- Prior: `decisions/OldThemes/rag_vs_cli_split/tool_surface_2026-05-30.md`, `decisions/OldThemes/search_strategy_fallback.md` (DockDoor case), `decisions/tool_design.md`.
- Usage evidence (not yet run): `dev/ghcli_usage/extract_ghcli_calls.py` (extracts real gh-cli calls from Monitor_CC proxy logs).
