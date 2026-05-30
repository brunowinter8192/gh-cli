# CLI Surface Cleanup — Two-Mode Strategy (2026-05-30)

## Strategic Frame

Two retrieval modes define the post-cleanup surface:

**RAG (semantic):** fuzzy corpus where exact identity is unknown. You have keywords; you want the set of documents that best match. Issues fit: a bug report is one document in a sea of similar reports. `index_issues` fetches, strips noise, writes per-issue MDs, and indexes — one command covers discovery + storage. The future `index_discussions` mirrors this pattern exactly.

**CLI-direct (exact lookup):** exact artifact when you already know what you want. Repo discovery (you have a query, you want THE repo), in-repo source work (you have the owner/repo/path), releases (you want THIS tag or latest). Precision is the value; chunked fuzzy retrieval would degrade it.

The split is not about data type — it is about whether identity is known before the call.

## Why Releases Stay CLI-Direct (Reversal of Earlier Direction)

Earlier planning included changelogs/releases in the RAG-indexing track. This was reversed:

- A release is a **versioned, exact artifact**. The question is always "give me v2.0.0 changelog" or "give me the latest release" — identity is known.
- `list_releases` provides the version index (tags, dates, preview); `get_release` returns the full body. Two calls cover the complete use case.
- RAG indexing would fragment the changelog Markdown into fixed-size chunks and return fuzzy partial matches against a query. For a changelog this is strictly worse: you either get too much (irrelevant versions) or too little (truncated chunk mid-entry). The exact artifact is better served by exact retrieval.

## Why Commit Tools Were Removed

`list_commits` + `compare_commits` removed entirely (files deleted):

- Real-usage sample of 97 CLI invocations: 0 calls to either tool.
- Same rationale as the earlier PR-tool removal: commit history is a development-artifact surface, not a research surface. When you need diff context, you're in the repo already; when you're researching, you want issues, releases, or source — not commit SHAs.
- No internal pipeline depends on them; deletion is clean.

## Why Raw Issue Primitives Left the User Surface

`search_items` deleted (file + subcommand): `index_issues` already does its own search (the `search_raw()` function) as the first step of indexing. Exposing `search_items` as a direct subcommand duplicated the search surface without adding value — results go nowhere without the indexing pipeline.

`get_issue` + `get_issue_comments` deregistered as subcommands, **files kept**: `index_issues.py` imports both workflows directly (`get_issue_workflow`, `get_issue_comments_workflow`) to fetch each issue's body and comments during the indexing loop. Deleting the files would break the pipeline. They become internal-only helpers — same pattern `get_discussion` will follow when `index_discussions` is built.

## Current and Planned Surface

**After this block — 13 visible subcommands:**

| Group | Tools |
|---|---|
| Repo discovery | `search_repos`, `get_repo` |
| In-repo source | `search_code`, `get_repo_tree`, `get_file_content`, `grep_file`, `grep_repo` |
| Releases | `list_releases`, `get_release` |
| RAG-semantic | `index_issues` |
| Discussions (interim) | `search_discussions`, `list_discussions`, `get_discussion` |

The 3 discussion subcommands remain only because `index_discussions` does not yet exist. They are the sole discussion access path in this interim state.

**Planned final surface — 11 visible subcommands:**

The next block builds `index_discussions`. When it lands:
- `search_discussions`, `list_discussions` are deregistered (deleted from cli.py subcommands).
- `get_discussion` is deregistered as a subcommand but **kept as file** — it becomes `index_discussions.py`'s internal fetch helper, mirroring how `get_issue` serves `index_issues`.
- `index_discussions` is registered as the 11th subcommand.

Final taxonomy (11):

| Group | Tools |
|---|---|
| Repo discovery | `search_repos`, `get_repo` |
| In-repo source | `search_code`, `get_repo_tree`, `get_file_content`, `grep_file`, `grep_repo` |
| Releases | `list_releases`, `get_release` |
| RAG-semantic | `index_issues`, `index_discussions` |
