# Repo Exploration — Phase B Verdicts

## /community/profile — REJECTED

**What it is:** `GET /repos/{o}/{r}/community/profile` — GitHub community health metric. Returns an integer health percentage, repo description, updated_at, and a files-map listing presence/absence of: code_of_conduct, contributing, issue_template, license, pull_request_template, readme.

**Why rejected:**

1. **Wrong family.** Health metric, not orientation tool. The endpoint measures community governance completeness (CoC, contributing guide, templates) — none of which maps to "what is this repo, where is the code, what is the tech stack."

2. **Unreliable files-map.** The `license` field uses GitHub licensee detection (SPDX / known FOSS licenses). Proprietary or custom licenses are not detected → field reports `absent` even when a LICENSE file exists. Confirmed on `anthropics/claude-code`: tree contains `LICENSE.md`, community/profile reports `license: absent`. Any orientation logic relying on the files-map will silently misclassify repos with non-FOSS licenses.

3. **Only orientation-relevant field is `readme`.** That is already covered by `GET /repos/{o}/{r}/readme` (probe_readme.py / `get_file_content`) with full content and path resolution. No additive signal.

**dev/ script:** `dev/repo_exploration/probe_community.py` (deleted). Raw output archived in `dev/repo_exploration/raw_results/community.md` (deleted).
