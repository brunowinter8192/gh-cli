# dev/repo_exploration/

## Role
Probe + smoke-test suite for the repo-orientation tools. Validated the GraphQL one-shot depth=1 tree traversal now in `get_repo_tree` (production shape: tree-only, metadata-on-root, single expression param) and the three-tier size handling in `get_file_content`. Backs `process-docs/repo_exploration/` and `process-docs/tool_design/`.

## Modules

### probe_client.py (79 LOC)

**Purpose:** Shared auth/HTTP infrastructure — verbatim copy of `src/github` token resolution (`_read_zshrc_token`/`_resolve_token`/`build_headers`) and `graphql_query()` for dev/-self-containment. Not a runnable probe.
**Reads:** `~/.zshrc` / env for the GitHub token.
**Writes:** exports headers + `graphql_query()` to the other probes.
**Called by:** `01_probe_graphql_explore.py` (imports auth helpers).
**Calls out:** `requests`; stdlib.

---

### 01_probe_graphql_explore.py (141 LOC)

**Purpose:** GraphQL one-shot depth=1 tree traversal — per-entry name/type/language/lineCount/size; repository metadata (description/primaryLanguage/languages) printed only for root expressions (`HEAD:`), omitted for sub-paths. Blob expression → redirect message, no file read.
**Reads:** GitHub GraphQL API via `probe_client.py`; args `<owner> <repo> [expression]`.
**Writes:** prints to stdout; report MD to `md/01_graphql_explore.md` (root call) or `md/01_graphql_plugins.md` (sub-path call).
**Called by:** run manually (dev entry point).
**Calls out:** imports auth from `probe_client.py`.

---

### probe_large_file.py (101 LOC)

**Purpose:** Smoke test for `get_file_content` three-tier size handling — Tier 1 (≤1 MB base64 inline, octocat/Hello-World README), Tier 2 (1–100 MB stream to /tmp, MuRongPIG/Proxy-Master http.txt), Tier 3 (>100 MB error, simulated via `format_toolarge_response` on a fake 200 MB dict). Invokes `cli.py` via subprocess (hook forbids `from src.` in dev/).
**Reads:** live GitHub via `cli.py get_file_content`; `/tmp/gh-cli_MuRongPIG_Proxy-Master_http.txt` on disk to verify the Tier-2 download.
**Writes:** prints per-tier PASS/FAIL to stdout; exits 1 on any failure.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib `subprocess`, `os`, `sys`.

## Gotchas
- `probe_client.py` is a verbatim copy of `src/github` auth (`block_dev_imports_src` hook forbids `from src.` in dev/) — update it when the source auth changes (duplication, not drift).
