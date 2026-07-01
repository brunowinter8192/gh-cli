# dev/discussion_cleaning/

## Purpose

Audit + validate + re-clean the dosu-bot noise strip for `index_discussions`. Backs `decisions/content_cleaning.md` / `decisions/discussion_indexing.md`. Operates on the built discussion MD corpus (rag-cli `github_discussions` doc dir).

## Scripts

### audit_discussion_noise.py (350 LOC)
**Purpose:** Classify noise classes across the discussion MDs. Read-only — never modifies source files.
**Usage:** `python3 dev/discussion_cleaning/audit_discussion_noise.py [--source-dir PATH]`
**Output:** report MD to `audit_reports/audit_<date>.md`; prints the report path.

### A_strip_validation.py (311 LOC)
**Purpose:** Validate `strip_discussion_noise()` on the 78-MD corpus. Read-only.
**Usage:** `python3 dev/discussion_cleaning/A_strip_validation.py [--source-dir PATH]`
**Output:** report MD to `A_strip_validation_reports/validation_<timestamp>.md`.

### reclean_existing_mds.py (295 LOC)
**Purpose:** Re-clean existing discussion MDs with `strip_noise()` — noise-only pass, safe on built MDs (does not touch `##` headings, metadata, attribution headers). Dry-run by default.
**Usage:** `python3 dev/discussion_cleaning/reclean_existing_mds.py [--apply] [--source-dir PATH]`
**Flags:** `--apply` overwrites files in place (timestamped backup first); `--source-dir PATH`.
**Output:** report MD to `reclean_reports/reclean_dryrun_<timestamp>.md` (or apply report).

## Gotchas

- Intentional verbatim copy of `src/github/discussion_cleaning.py` (`strip_noise` + `_bare`, `_is_badge_line`, constants): the `block_dev_imports_src` hook forbids `from src.` in dev/. Duplication, not drift — update the copy when the source changes.
