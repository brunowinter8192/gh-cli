# Repo Exploration (get_repo_tree)

## Status Quo (IST)

- `get_repo_tree` = GraphQL one-shot, depth=1 directory traversal (`src/github/get_repo_tree.py`, via `graphql_client.graphql_query`). Subcommand: `get_repo_tree <owner> <repo> [--path P]`; `get_repo_tree_workflow(owner, repo, path="")`.
- Per-entry fields: name, type, language, lineCount, size. Metadata block (description / primaryLanguage / languages) emitted ONLY on ROOT expression (empty path); sub-path calls return the tree table only (no repeated-description noise).
- TREE-ONLY: no blob/file reading — `get_file_content` remains the reader (`Blob.text` lacks offset/limit). depth=1 always; descend by re-calling with a deeper `--path`.
- Recursive find-by-name (former pattern mode) dropped: `search_code` requires ≥1 free-text content term, so pure name-only structural find is not forwarded — non-need for top-down exploration.
- Agent-exposed param = path/expression only; all other knobs hidden in the wrapper.

## Evidenz

- Recursive full-tree dump = anti-pattern for live exploration (huge token cost, mostly noise). One-level traversal with per-entry signal shows where substance is and where to descend. GraphQL delivers tree + language + lineCount + repo metadata in one round-trip vs the old 3-REST chain (default-branch → SHA → `/git/trees?recursive`). → `decisions/OldThemes/repo_exploration/phaseB_results.md`, `endpoint_mapping.md`; dev probes `dev/repo_exploration/probe_graphql_explore.py`, raw `dev/repo_exploration/raw_results/graphql_explore.md` (root) + `graphql_plugins.md` (sub-path).
- Rejected exploration endpoints: `/community/profile` (health metric, not orientation; `license` field uses licensee detection → reports `absent` for non-FOSS, confirmed on `anthropics/claude-code` where `LICENSE.md` exists but is reported absent), `/readme` (marginal over `get_file_content` once filename is known), `/languages` (subsumed by GraphQL `languages` field). → `phaseB_results.md`.

## Offene Fragen

- depth≥2 traversal deferred; v1 is pure one-level — add only if it proves too blind.

## Quellen

- gh-cli-reference: `docs_github_com_en_graphql_reference_git` (Tree / Blob / TreeEntry fields)
- gh-cli-reference: `docs_github_com_en_graphql_reference_repos` (Repository fields, languages)
- gh-cli-reference: `docs_github_com_en_rest_repos_contents` (readme, contents endpoints)
- gh-cli-reference: `docs_github_com_en_rest_metrics_community` (community/profile endpoint)
