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

## GraphQL one-shot (probe_graphql_explore) — KEPT (future)

**What it is:** GraphQL `repository{description, primaryLanguage, languages(first:10), object(expression)}` dispatched on Tree/Blob. One round-trip returns: repo description, primary language, full language breakdown (subsumes /languages), and per-entry name/type/language/lineCount for any subtree expression.

**Status:** Retained in `dev/repo_exploration/` as reference implementation. NOT promoted to a production tool yet — promotion deferred pending: (1) token-cost comparison vs current 3-REST chain (`get_repo_tree`), (2) design decision on what a production orientation tool should expose to the user. Hypothesis that GraphQL one-shot wins on signal density remains unverified (see DOCS.md Hypotheses).
