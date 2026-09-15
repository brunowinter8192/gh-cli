# dev/repo_exploration/

## Role
Probe suite for the repo-orientation tools. Validated the GraphQL one-shot depth=1 tree traversal now in `get_repo_tree` (production shape: tree-only, metadata-on-root, single expression param). Backs `process-docs/repo_exploration/`.

## Public Interface
No package `__init__` — each script is a standalone, manually-run dev entry point.

## Flow
1. Run `01_probe_graphql_explore.py <owner> <repo> [expression]`.
2. Script authenticates via `probe_client.py`, issues one GraphQL query.
3. Prints the formatted result to stdout and writes a report MD to `md/`.

## Modules

### probe_client.py (69 LOC)

**Purpose:** Shared auth/HTTP infrastructure for dev/-self-containment — token resolution and `graphql_query()`. Not a runnable probe.
**Reads:** `~/.zshrc` / env for the GitHub token.
**Writes:** exports headers + `graphql_query()` to the other probes.
**Called by:** `01_probe_graphql_explore.py` (imports auth helpers).
**Calls out:** `requests`; stdlib.

---

### 01_probe_graphql_explore.py (128 LOC)

**Purpose:** GraphQL one-shot depth=1 tree traversal — per-entry name/type/language/lineCount/size, root-only repo metadata.
**Reads:** GitHub GraphQL API via `probe_client.py`; args `<owner> <repo> [expression]`.
**Writes:** prints to stdout; report MD to `md/01_graphql_explore.md` (root call) or `md/01_graphql_plugins.md` (sub-path call).
**Called by:** run manually (dev entry point).
**Calls out:** imports auth from `probe_client.py`.

---

## State
None — each probe run is stateless; `probe_client.py`'s resolved token lives only for the run's process lifetime.
