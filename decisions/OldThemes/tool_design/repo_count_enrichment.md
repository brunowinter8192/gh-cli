# Repo-Count Enrichment in search_repos / search_code (2026-06-11)

Process record for adding per-repo issue/discussion counts to the two discovery tools.

## Problem

Discussion/issue indexing is per-repo, but not every repo enables both. `anthropics/claude-code` has discussions DISABLED (issues only). Pre-enrichment, `search_repos` emitted `full_name stars` and `search_code` emitted `full_name path` — no signal which conversation layer a repo uses. An agent would blindly run `index_discussions` on claude-code and get "No discussions found" = wasted round. The fix: surface `issues:N · discussions:M` + an `(off)` marker at discovery time, so the agent routes to `index_issues` vs `index_discussions` on sight.

## API choice — REST insufficient, GraphQL required

- REST `/search/repositories` returns `open_issues_count` only: counts OPEN issues + OPEN PRs combined (GitHub treats PRs as issues), no closed, NO discussion count, no enabled flags. Insufficient.
- GraphQL `Repository` provides exactly the signal: `issues { totalCount }` (clean, excludes PRs), `discussions { totalCount }`, `hasIssuesEnabled`, `hasDiscussionsEnabled`, `stargazerCount`.
- Source: `gh-cli-reference` — `docs_github_com_en_graphql_reference_repos.md`, `docs_github_com_en_graphql_guides_using_the_graphql_api_for_discussions.md`.

## Architecture — REST search + batched GraphQL enrichment (chosen)

Kept the existing REST search; appended ONE batched aliased GraphQL call (`r0: repository(...) {...} r1: ...`) enriching the whole result set in a single request via `graphql_query()`. New shared helper `fetch_repo_counts()` + `format_count_line()` in `src/github/repo_counts.py`; both search tools call it.

**Rejected alternative:** migrate `search_repos` to GraphQL `search(type:REPOSITORY)` with counts inline (one call, no REST+GraphQL split). Rejected to preserve the REST search ranking/sort behavior (`sort_by` stars/forks/updated) — ranking stability valued over the marginal elegance of a single call. `search_code` has NO GraphQL equivalent (GitHub code search is REST-only), so REST + enrichment is forced there regardless; using the same pattern for both keeps one helper.

## Implementation findings

- **search_code stars source:** the REST `/search/code` repository stub does NOT include `stargazers_count` (confirmed via live probe). → `stargazerCount` is pulled from the GraphQL enrichment for search_code; `search_repos` keeps its REST `stargazers_count` (present there).
- **null-repo guard:** a repo listed in search results can return `null` from the `repository(...)` lookup (deleted/renamed between search and enrichment). `fetch_repo_counts()` maps null → `None`; rendered as `issues:? · discussions:?` rather than crashing.
- **Output:** `owner/repo · ⭐{stars} · issues:{n} · discussions:{m}`, `(off)` appended per feature when its enabled flag is false. `search_code` prepends a `## Repos (N unique)` summary block (repos deduped first-seen) before the per-hit output.

## Live verification (2026-06-11, merged dev)

- `search_repos "fastapi"` → 30 enriched lines, both `(off)` variants present (e.g. `zhanymkanov/fastapi-best-practices · ⭐17479 · issues:60 · discussions:0 (off)`).
- `search_code "... repo:anthropics/claude-code"` → `## Repos (1 unique)` + `anthropics/claude-code · ⭐131774 · issues:65172 · discussions:0 (off)` — motivating case confirmed.

## Quellen

- `gh-cli-reference`: `docs_github_com_en_graphql_reference_repos.md`, `docs_github_com_en_rest_repos_repos.md`, `docs_github_com_en_rest_issues_issues.md` (PR-as-issue note), `docs_github_com_en_graphql_guides_using_the_graphql_api_for_discussions.md`.
