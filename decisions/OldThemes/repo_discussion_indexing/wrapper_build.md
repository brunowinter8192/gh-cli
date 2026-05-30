# index_discussions Wrapper — Build & Decisions (2026-05-30)

Port session implementing the discussion-indexing wrapper whose design was converged by the probe (`probe_beads_2026-05-30.md`). Mirrors `index_issues` throughout; this file documents what was decided + built.

## Built

`index_discussions` tool (`index_discussions_workflow(query, repo, limit=30)` in `src/github/index_discussions.py`). New gh-cli subcommand — surface collapsed 13→11 simultaneously (`search_discussions`, `list_discussions`, `get_discussion` deregistered). Wired in `cli.py`.

Flow: query → max-3-keyword repo-scoped GraphQL search → top-N discussion numbers → in-process `get_discussion_workflow()` → `strip_discussion_noise()` + `redact_tokens()` → per-discussion MD `<repo>__<num>.md` → `RAG/data/documents/github_discussions/` → subprocess `workflow.py index-dir`. No sleeps.

## Search Lift

`search_discussions.py`'s `SEARCH_QUERY` (GraphQL `search(type: DISCUSSION)`) lifted into `index_discussions.py` as a local constant, trimmed to `discussionCount` + `number` only (the display fields from the original `search_discussions` tool are not needed). `search_discussions_raw()` injects `repo:{repo}` into the query string — identical pattern to `search_raw()` in `index_issues.py` (`{kw} repo:{owner/name} is:issue`). Probe confirmed `repo:` scoping works on `search(type:DISCUSSION)`.

`search_discussions.py` and `list_discussions.py` files deleted. `get_discussion.py` retained — becomes internal-only helper of `index_discussions.py`, mirroring how `get_issue.py` serves `index_issues.py`.

## Strip Implementation

`strip_discussion_noise()` processes `get_discussion_workflow()` output line-by-line:

1. **Title extraction** — `get_discussion` emits `## {title}` (H2, not H1). Detected with `line.startswith("## ")`, title extracted as `line[3:].strip()`, line dropped from body. `build_discussion_md()` promotes to `# {title}` (H1 in final MD).

2. **Metadata block** — drops lines with prefixes `**Category:**`, `**Author:**`, `**Created:**`, `**Upvotes:**`, `**Status:**`. These 5 lines are the per-discussion metadata block emitted before `### Body`.

3. **[ANSWER] dedup** — `get_discussion` renders the accepted answer in two places: `### Accepted Answer` section (keeper) and as a comment-list entry tagged `[ANSWER]` (duplicate). State machine: `ANSWER_COMMENT_HDR_RE` (`**@\S+** (YYYY-MM-DD) - N upvotes [ANSWER]`) detects the duplicate; `in_answer_comment = True` skips the header + body + replies until `COMMENT_HDR_RE` or `### ` line (next comment or section). EOF terminates naturally (loop ends while `in_answer_comment=True` — no residual append). Exact timestamp+upvotes pattern prevents false-match on inline `**@mention**` body text.

4. **Redaction** — `redact_tokens()` applied to final MD string: `ghp_[A-Za-z0-9]+` and `github_pat_[A-Za-z0-9_]+` → `[REDACTED]`.

## CLI Surface — 13 → 11

Deregistered: `search_discussions`, `list_discussions`, `get_discussion`.
Added: `index_discussions`.
Rationale crystallized in `decisions/OldThemes/rag_vs_cli_split/tool_surface_2026-05-30.md` — the 3 discussion primitives existed only because `index_discussions` didn't yet. Once the RAG-indexing command covers the semantic-retrieval use case, the individual primitives have no standalone value on the CLI surface.

## Constants vs index_issues

| Constant | index_issues | index_discussions |
|---|---|---|
| RAG_DOC_DIR | `RAG/data/documents/github_issues` | `RAG/data/documents/github_discussions` |
| COLLECTION | `github_issues` | `github_discussions` |
| DEFAULT_LIMIT | 30 | 30 |
| Search method | `GET /search/issues` (REST) | `graphql_query(SEARCH_QUERY)` (GraphQL) |
| Fetch | `get_issue_workflow` + `get_issue_comments_workflow` (2 calls/thread) | `get_discussion_workflow` (1 call/thread) |

Discussion fetch is simpler than issues — one GraphQL call returns body + comments + answer together.

## Probe Baseline

23 beads threads, 116 KB written, 5.6% strip reduction. `isAnswered = 0/23` — dedup path not triggered for this corpus but implemented correctly. Full numbers in `probe_beads_2026-05-30.md`.
