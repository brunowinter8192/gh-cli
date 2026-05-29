# Repo Discussion Indexing — Feasibility (initial assessment, 2026-05-30)

Scoping for extending the index_issues methodology to GitHub Discussions. Not built. Initial feasibility grounding for the discussion-indexing work.

## Goal
Same query → top-N relevant discussion threads (repo-scoped) → per-thread MD → RAG index. Mirrors index_issues; one query feeds both. Agent then vector-searches instead of many fine-grained discussion tool-calls.

## Usage-model frame
gh-cli **direct** = code + repo search (content INSIDE a repo). RAG-**indexing** = the discussion/issue layer "around" the code. Issues done (index_issues); discussions next; commits/releases deferred (3rd block).

## Feasibility gate (must clear before building)
- Discussions are PER-REPO; many repos have NONE (incl. anthropics/claude-code) → need a repo with active discussions as test target.
- Confirm discussion content is worth indexing (vs per-repo sparsity).

## Current prod state (3 GraphQL tools, via graphql_client.py)
- `search_discussions(query, first)` — GLOBAL: GraphQL `search(query, type: DISCUSSION, first)` (`search_discussions.py:10`). NO repo scope in current impl; returns repo per hit.
- `list_discussions(owner, repo, --category, --answered)` — repo-scoped, ordered UPDATED_AT DESC. Not relevance-ranked.
- `get_discussion(owner, repo, number, --comment-limit, --comment-sort)` — full thread: body + threaded comments + accepted answer (`[ANSWER]` tag) in ONE call. Better than issues' two-call fetch.

## Key finding: repo-scoping likely trivial (VERIFY)
GitHub GraphQL `search(query:...)` honors the same qualifiers as issue search. Injecting `repo:owner/name` into the query string — `search(query: "repo:owner/name <terms>", type: DISCUSSION)` — should scope discussion search to a repo, exactly as `search_raw` does for issues (`<kw> repo:X is:issue`). MUST VERIFY empirically; this is the build's crux. If it works, the wrapper builds the repo-scoped query itself; the global `search_discussions` tool need not change.

## Pipeline mapping (vs issues)
- Search: repo-scoped discussion search (via `repo:` injection) → top-N discussion numbers. [verify]
- Fetch: `get_discussion` = body+comments+answer in ONE call (vs issues' 2). Simpler.
- MD + index + dedup: identical to index_issues (per-thread MD, index-dir content-hash).
Endpoint-wise we likely already have what's needed (repo-scoped search + get_discussion).

## Open questions
- Does `search(type:DISCUSSION)` honor `repo:`? (verify — feasibility crux)
- Test repo with discussions? (method: search_discussions global hits expose which repos have them; or known large OSS repos with Discussions enabled)
- N for discussions (mirror 30, or different)? Noise-stripping for get_discussion's output format (differs from get_issue)?
- Same `github_issues` collection or separate `github_discussions`?
