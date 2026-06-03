# Repo Exploration — Phase B Verdicts

## /community/profile — REJECTED

**What it is:** `GET /repos/{o}/{r}/community/profile` — GitHub community health metric. Returns an integer health percentage, repo description, updated_at, and a files-map listing presence/absence of: code_of_conduct, contributing, issue_template, license, pull_request_template, readme.

**Why rejected:**

1. **Wrong family.** Health metric, not orientation tool. The endpoint measures community governance completeness (CoC, contributing guide, templates) — none of which maps to "what is this repo, where is the code, what is the tech stack."

2. **Unreliable files-map.** The `license` field uses GitHub licensee detection (SPDX / known FOSS licenses). Proprietary or custom licenses are not detected → field reports `absent` even when a LICENSE file exists. Confirmed on `anthropics/claude-code`: tree contains `LICENSE.md`, community/profile reports `license: absent`. Any orientation logic relying on the files-map will silently misclassify repos with non-FOSS licenses.

3. **Only orientation-relevant field is `readme`.** That is already covered by `GET /repos/{o}/{r}/readme` (probe_readme.py / `get_file_content`) with full content and path resolution. No additive signal.

**dev/ script:** `dev/repo_exploration/probe_community.py` (deleted). Raw output archived in `dev/repo_exploration/raw_results/community.md` (deleted).

## /readme — REJECTED

**What it is:** `GET /repos/{o}/{r}/readme[/{dir}]` — returns the preferred README for a repo or subdirectory (resolves non-standard filenames: `README.md`, `readme.md`, `README`, etc.); response includes name, path, size, base64 content.

**Why rejected:** Marginal over `get_file_content`. The only edge case it handles — non-standard README filename — is rare in practice, and the repo tree already surfaces the actual filename (visible via `probe_graphql_explore` / `get_repo_tree`). Once the filename is known, `get_file_content("README.md")` is equivalent. No standalone tool justified for a single low-frequency edge case.

**dev/ script:** `dev/repo_exploration/probe_readme.py` (deleted). Raw output archived in `dev/repo_exploration/raw_results/readme.md` (deleted).

## /languages — REJECTED

**What it is:** `GET /repos/{o}/{r}/languages` — returns a language→bytes map for the repo; one REST call, full tech-stack breakdown with byte counts.

**Why rejected:** Fully subsumed by `probe_graphql_explore`. The GraphQL query already includes `languages(first:10){nodes{name},totalSize}` and returns percentage breakdown inline on every call. Running a dedicated REST call to get language data that the GraphQL round-trip already delivers is pure redundancy — no additional signal, one extra HTTP request.

**dev/ script:** `dev/repo_exploration/probe_languages.py` (deleted). Raw output archived in `dev/repo_exploration/raw_results/languages.md` (deleted).

## DECISION: replace get_repo_tree with GraphQL one-level traversal

**Decision:** `get_repo_tree` (recursive full-tree, 3-REST chain: default-branch → SHA → `/git/trees?recursive`) is replaced by a GraphQL one-shot, depth=1 directory-traversal tool.

**Rationale:** For live top-down agent exploration, recursive full-tree dump is the anti-pattern — huge token cost, mostly noise, forces consuming the whole structure to find the relevant subtree. One-level traversal — point at a path, get that directory's entries, descend by re-applying the expression — is the right interaction model. Per-entry signal (language, lineCount, size) shows where substance is and where to descend.

**Tool shape:**
- TREE-ONLY: no blob/file reading. `get_file_content` stays the reader because `Blob.text` lacks offset/limit.
- depth=1 always.
- Metadata block (description/primaryLanguage/languages) only on ROOT expression (path after `:` is empty); sub-path calls return tree table only (removes repeated-description noise on traversal calls).
- Per-entry fields: name, type, language, lineCount, size.
- Agent-exposed param: ONLY the path/expression — all else hidden in the wrapper (CLI minimalism: do not overload the agent with knobs).

**Rejected knobs:**
- `isGenerated`: heuristic linguist flag, unreliable; hiding entries risks more than the noise it removes.
- `isTruncated` / `isBinary`: moot once blob-reading is dropped.
- depth≥2: deferred; v1 is pure one-level — add only if v1 proves too blind.

**Dropped capability — recursive find-by-name:** `get_repo_tree` pattern mode (find -name across whole tree) is dropped. `search_code` forwards qualifiers (filename:/extension:/path:) BUT GitHub code search requires ≥1 free-text CONTENT term — a language: or path: qualifier alone is rejected. Pure name-only structural find is impossible via `search_code`. Verdict: non-need for top-down exploration — the agent traverses structurally anyway and supplies a content term when it cares about content. No meaningful loss.

**Evidence:** `dev/repo_exploration/probe_graphql_explore.py` (production shape), `dev/repo_exploration/raw_results/graphql_explore.md` (root call, with metadata), `dev/repo_exploration/raw_results/graphql_plugins.md` (sub-path call, tree-only). GraphQL schema: gh-cli-reference: docs_github_com_en_graphql_reference_git.
