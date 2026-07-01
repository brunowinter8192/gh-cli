# dev/repo_exploration/

## Problem

`gh-cli` has no "understand an unknown repo top-down" orientation flow. `get_repo_tree` (ls/find) and `get_file_content` (cat) exist, but there is no strategy for: what files matter, what the tech stack is, where the anchor documents live. This suite probes GitHub endpoints that may fill that gap.

Production code status quo: `get_repo_tree` uses a 3-REST-call chain (default-branch → SHA → `/git/trees?recursive`); `get_file_content` is `/contents/{path}` + base64 decode. See `decisions/tool_design.md` IST.

Open question under investigation: can a set of cheaper / higher-signal calls replace or augment the current approach for orientation tasks? Decision deferred to next session after probe results.

## Investigation

### Code Analysis

- `src/github/client.py` — token resolution (`_read_zshrc_token` / `_resolve_token`) + `build_headers()` copied verbatim into `probe_client.py` for dev/-self-containment (hook `block_dev_imports_src` forbids `from src.` in dev/ files — intentional duplication, not drift).
- `src/github/graphql_client.py` — `graphql_query(query, variables)` copied verbatim into `probe_client.py` for same reason.

### External Research

| Source | Result | Relevance |
|--------|--------|-----------|
| GitHub GraphQL: TreeEntry.lineCount / .language | ✅ | Per-entry language+lineCount — not available from REST `/git/trees` |

### Hypotheses

| Hypothesis | Status | Evidence |
|------------|--------|----------|
| GraphQL one-shot wins on token cost vs 3-REST chain | Unverified | lineCount+language per entry suggests higher signal density; measure next session |

## Scripts

**`probe_client.py`** — shared auth/HTTP infrastructure (verbatim copy of src/ auth for dev/-self-containment). Not a runnable probe.

**`probe_graphql_explore.py`** — Tree-only, depth=1. GraphQL one round-trip returns per-entry: name, type, language, lineCount, size. Repository metadata (description, primaryLanguage, languages) printed only for root expressions (path after ":" is empty, e.g. `"HEAD:"`); omitted for sub-path expressions to avoid repeated noise. If expression resolves to a Blob, prints a redirect message — does NOT read file content. Prints to stdout (console diagnostic tool); `md/` holds manually-captured probe output.
```
.venv/bin/python dev/repo_exploration/probe_graphql_explore.py <owner> <repo> [expression]
# expression examples: "HEAD:" (root, prints metadata), "HEAD:plugins/" (subtree, table only)
```
