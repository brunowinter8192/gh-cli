# Discussion comment order + limit — natural chronological, limit 100 (2026-06-11)

Supersedes the upvote-resort behavior in `get_discussion.py` (the internal fetch helper of `index_discussions`).

## Superseded (removed this session)

- `comment_sort: Literal["upvotes","chronological"] = "upvotes"` parameter on `get_discussion_workflow()`.
- `sort_comments()` — Python-side re-sort of fetched comments by `upvoteCount` desc (active under the "upvotes" default).
- `comment_limit` default = 50.

## Current (IST → see `decisions/discussion_indexing.md`)

- No `comment_sort`; comments render in the **natural chronological order** the GitHub API returns.
- `comment_limit` default = **100**.

## Rationale

- For RAG indexing, comment ORDER is irrelevant to the embedding — every comment is chunked + embedded regardless of sequence, so re-sorting buys nothing for retrieval.
- The upvote re-sort actively DESTROYED the natural conversation chain (question → answer → follow-up), which is the one thing worth preserving in the indexed text. Net negative → removed.
- `comment_sort` as a config knob therefore has no RAG use-case → dropped, not just defaulted.

## Comment-coverage / sampling note

- `Discussion.comments` connection has NO `orderBy` (unlike issue comments which expose `IssueCommentOrder`) — the API returns comments in creation order; `comments(first:N)` caps at 100 per page. Source: `gh-cli-reference` → `docs_github_com_en_graphql_guides_using_the_graphql_api_for_discussions.md`.
- Old behavior fetched the first-50-chronological window, THEN upvote-sorted that window — so a high-upvote comment at position >50 was never seen. Raising 50→100 = the API per-page max without pagination → full coverage for all but very large threads.
- Threads >100 comments still truncate. Pagination (`after` cursor) deferred — not worth it without a concrete repo where it bites. The upvote-info per comment is still shown (`{upvoteCount} upvotes`), just not used to reorder.

## Pre-existing robustness gap observed (NOT this scope)

`index_discussions` / `index_issues` do not retry/wait on RAG lock contention: when the rag DB was busy (a concurrent `list_documents` on `searxng_crypto`), the index step exited non-zero and the tool reported `New chunks added: 0` / `0 chunks total` while the per-thread MDs were already written to disk. Recovered by re-running `rag-cli index --collection github_discussions` (24 files → 96 chunks). Pre-existing pattern, not introduced here — candidate for a future lock-retry in the index step.
