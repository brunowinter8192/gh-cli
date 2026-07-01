# dev/issue_cleaning/

## Purpose

Re-clean the existing issue MD corpus with the generic noise strip. Backs `decisions/content_cleaning.md` / `decisions/issue_indexing.md`.

## Scripts

### reclean_issues.py (175 LOC)
**Purpose:** Re-clean existing issue MDs with `strip_generic_noise()` — image / data-URI / no-space pass only. Additive and safe on already-formatted MDs (built with `strip_noise` + `strip_comments_noise`). Dry-run by default.
**Usage:** `python3 dev/issue_cleaning/reclean_issues.py [--apply] [--source-dir PATH]`
**Flags:** `--apply` overwrites files in place (timestamped backup first); `--source-dir PATH`.
**Output:** report MD to `reclean_reports/reclean_dryrun_<timestamp>.md` (or apply report).

## Gotchas

- Intentional verbatim copy of `src/github/text_cleaning.py` (`strip_generic_noise` + regexes): the `block_dev_imports_src` hook forbids `from src.` in dev/. Duplication, not drift — source of truth is `src/github/text_cleaning.py`; update the copy when it changes.
