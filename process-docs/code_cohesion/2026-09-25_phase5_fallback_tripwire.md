# Phase 5: fallback and tripwire (src/, cli.py)

## Decision rule applied
Observed-only. A field being nullable in the GitHub schema is not an observation. Observation = occurrence in a dev/ report, a process-docs entry, a fixture, the indexed corpora under rag-cli/data/documents, or a live probe recorded in a dev/ report. Boolean `or` conditions, valid empty results, "no language filter" as input and HTMLParser `None` for valueless attributes stay structural.

## Observed (kept, made traceable)
| Where | Evidence | Trace |
|---|---|---|
| token chain zshrc -> GH_TOKEN -> GITHUB_TOKEN | tool_design token_resolution entry | logger.info names the source, never the token |
| null repo in repo_counts | tool_design repo_count_enrichment entry | logger.warning names the repo |
| issue body null | 2 files in github_issues corpus contain "(No description provided)" | logger.info with issue number |
| rag-cli "Nothing to index." | rag-cli src/rag/index_cmd.py; unchanged-MD re-runs | logger.info, returns 0 |
| tree entry language null, lineCount null | dev/repo_exploration/md/01_graphql_explore.md and 01_graphql_plugins.md show "-" | visible in output ("-") |
| trending repo without description | fixture (anthropics/financial-services), live probe 10 of 522 | logger.info |
| trending developer without popular repo / popular repo description | live probe 5 and 34 of 654 | logger.info |
| download_files per-path failures | tool_design download_files entry | logger.warning plus Failed report |
| raw_logging swallow | content_cleaning revert_and_raw_logging entry (verified with unwritable path) | already logger.warning, unchanged |
| BrokenPipe in cli.py, `except Exception` in cli.py | milestone2 salvage; the latter is the abort-and-report path | unchanged |

## Not observed, now strict (raise instead of default)
Discussion author/category/answer author/createdAt/upvoteCount/body/comments/nodes/replies (no `@unknown` or `@ghost` in the 264 discussion MDs), release tag_name/published_at/body (30 releases, none empty, none untagged), repo description and primaryLanguage in get_repo_tree (only the one described repo ever seen; null raises RuntimeError via require_present), tree entry size, file size/type/sha/html_url/content/encoding, non-base64 encoding, `labels`, comment body, `items`, text_matches fragment/property/text_matches key, repo_counts fields, GraphQL error message, empty GitHub token (raises at request time; import stays lazy because trending needs no token), unparseable rag-cli output, missing collection in list_collections, trending language and period stars (probe: 522 of 522 present). `shutil.rmtree(ignore_errors=True)` replaced by an exists() check.

## Live findings
1. Live probe 2026-09-25 (60 pages): trending shows the period text `1 star today` (singular). PERIOD_RE only knows the plural, so the existing tripwire raises "period stars ... unrecognised" on daily shell and daily markdown pages. Observed markup, pre-existing, NOT fixed in this phase (behaviour change, out of scope). Successor: extend PERIOD_RE to accept `star|stars`.
2. Live E2E after the change: get_issue, get_discussion (5 beads threads), search_repos, search_code (4 queries, strict text_matches held), get_repo_tree root and sub path, get_file_content, repo_freshness, list_issues, trending (repos, developers), download_files, get_collection_stats of all three collections: no strict-access failure. A repo with a null description was not found live, so that path is untested live.

## Pitfalls
- No logging config exists anywhere: only WARNING and above reach stderr. info lines are invisible unless logging is enabled.
- `d["x"]` does not raise on a JSON null. Only follow-up operations ([:10], .strip(), ["login"], join) raise. Where a null would print silently (repo description, primaryLanguage) require_present raises explicitly.
- parse_chunk_count / get_collection_stats exist as three copies (issues, discussions, releases); left duplicated, cohesion is out of scope here.

## Tests
dev/tool_design/test_strict_access.py: 8 strands in separate processes (tokens need their own HOME and env). Deliberate break of one assertion: that strand FAIL, other 7 PASS, exit 1, restored. dev/trending/test_trending.py unchanged and passing.

## Follow-up after review (2026-09-25)
Corrections to the sections above:
1. get_repo_tree root description: the probe observed repositories without a description (10 of 522 trending entries), so a missing description is an observed condition, not an unseen shape. It is now a logged fallback: `(none)` in the output plus `logger.info`. The statement above that a null description raises via require_present is superseded; require_present remains only for primaryLanguage (never observed missing). New strand `tree_repo_without_description` in dev/tool_design/test_strict_access.py.
2. Trending "1 star today": PERIOD_RE now accepts `stars?`. Fixture dev/trending/fixtures/trending_single_star.html is one real article (nyldn/claude-octopus, daily shell page 2026-09-25) with the hydro attributes and svgs stripped, 2680 bytes. Strand `single_star` in test_trending.py. Proven: with the old regex the strand FAILs and the other three PASS; with the new regex all PASS. Live runs of trending daily for shell, markdown and all languages exit 0 (previously the first two raised).
