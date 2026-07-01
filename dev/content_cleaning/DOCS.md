# dev/content_cleaning/

## Purpose

Audit + validate + re-clean the noise strip for `index_discussions` and `index_issues`. Backs `decisions/content_cleaning.md`, `decisions/discussion_indexing.md`, `decisions/issue_indexing.md`. Operates on the built MD corpora (`github_discussions/` and `github_issues/` doc dirs).

## Scripts

### 01_audit_discussion_noise.py (350 LOC)
**Purpose:** Classify dosu-bot noise classes across the discussion MDs. Read-only — never modifies source files.
**Usage:** `python3 dev/content_cleaning/01_audit_discussion_noise.py [--source-dir PATH]`
**Output:** report MD to `md/01_audit_<date>.md`; prints the report path.

### 02_strip_validation.py (311 LOC)
**Purpose:** Validate `strip_discussion_noise()` on the 78-MD corpus. Read-only.
**Usage:** `python3 dev/content_cleaning/02_strip_validation.py [--source-dir PATH]`
**Output:** report MD to `md/02_validation_<timestamp>.md`; prints the report path.

### 03_reclean_discussions.py (286 LOC)
**Purpose:** Re-clean existing discussion MDs with `strip_noise()` — noise-only pass, safe on built MDs (does not touch `##` headings, metadata, attribution headers). Dry-run by default.
**Usage:** `python3 dev/content_cleaning/03_reclean_discussions.py [--apply] [--source-dir PATH]`
**Flags:** `--apply` overwrites files in place (timestamped backup first); `--source-dir PATH`.
**Output:** report MD to `md/03_reclean_dryrun_<timestamp>.md`; prints the report path.

### 04_reclean_issues.py (168 LOC)
**Purpose:** Re-clean existing issue MDs with `strip_generic_noise()` — image/data-URI/no-space pass only. Additive and safe on already-formatted MDs. Dry-run by default.
**Usage:** `python3 dev/content_cleaning/04_reclean_issues.py [--apply] [--source-dir PATH]`
**Flags:** `--apply` overwrites files in place (timestamped backup first); `--source-dir PATH`.
**Output:** report MD to `md/04_reclean_dryrun_<timestamp>.md`; prints the report path.

## Gotchas

- `03_reclean_discussions.py` and `02_strip_validation.py` contain intentional verbatim copies of `src/github/discussion_cleaning.py` (`strip_noise` + `_bare`, `_is_badge_line`, constants): the `block_dev_imports_src` hook forbids `from src.` in dev/. Duplication, not drift — update the copy when the source changes.
- `04_reclean_issues.py` contains an intentional verbatim copy of `src/github/text_cleaning.py` (`strip_generic_noise` + regexes). Source of truth: `src/github/text_cleaning.py`.
