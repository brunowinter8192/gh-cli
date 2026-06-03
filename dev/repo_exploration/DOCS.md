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
| GitHub REST: /readme | ✅ | Returns preferred README regardless of filename; base64 content in default response |
| GitHub REST: /languages | ✅ | Returns language→bytes map; one call for full tech-stack breakdown |
| GitHub REST: /community/profile | ✅ | Health score + files-map (README/LICENSE/CONTRIBUTING/CoC/templates present+paths) |
| GitHub GraphQL: TreeEntry.lineCount / .language | ✅ | Per-entry language+lineCount — not available from REST `/git/trees` |

### Hypotheses

| Hypothesis | Status | Evidence |
|------------|--------|----------|
| GraphQL one-shot wins on token cost vs 3-REST chain | Unverified | lineCount+language per entry suggests higher signal density; measure next session |
| /readme handles no-README gracefully (404) | Unverified | Test against repo without README next session |
| /community/profile files-map replaces filename guessing | Unverified | Endpoint documented; run probe to confirm path fields populated |

## Scripts

**`probe_client.py`** — shared auth/HTTP infrastructure (verbatim copy of src/ auth for dev/-self-containment). Not a runnable probe.

**`probe_readme.py`** — `GET /repos/{o}/{r}/readme[/{dir}]`; prints name, path, size, first 40 lines.
```
.venv/bin/python dev/repo_exploration/probe_readme.py <owner> <repo> [dir]
```

**`probe_languages.py`** — `GET /repos/{o}/{r}/languages`; prints language→bytes sorted by size with percentages.
```
.venv/bin/python dev/repo_exploration/probe_languages.py <owner> <repo>
```

**`probe_community.py`** — `GET /repos/{o}/{r}/community/profile`; prints health%, description, files map.
```
.venv/bin/python dev/repo_exploration/probe_community.py <owner> <repo>
```

**`probe_graphql_explore.py`** — GraphQL `repository{description, primaryLanguage, languages, object(expression)}` dispatched on Tree/Blob; one round-trip gives structure + language + lineCount per entry. Default expression `"HEAD:"` = root tree.
```
.venv/bin/python dev/repo_exploration/probe_graphql_explore.py <owner> <repo> [expression]
# expression examples: "HEAD:" (root), "HEAD:src/" (subtree), "HEAD:README.md" (blob)
```
