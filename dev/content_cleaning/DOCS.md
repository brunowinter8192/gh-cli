# dev/content_cleaning/

## Role
Audit, validate, and re-clean the noise strip for `index_discussions` and `index_issues`. Backs `process-docs/content_cleaning/`, `process-docs/discussion_indexing/`, `process-docs/issue_indexing/`. Operates on the built MD corpora (`github_discussions/` and `github_issues/` doc dirs).

## Public Interface
No package `__init__` — each script is a standalone, manually-run dev entry point. None are imported by `src/` or by each other.

## Flow
1. Point `--source-dir` at a corpus (or use the script's default RAG doc dir).
2. Script measures or detects noise via a verbatim copy of the relevant `src/github/` strip logic.
3. Read-only scripts write a report MD; `--apply`-capable scripts default to dry-run and require the flag to overwrite the corpus.
4. Numbers-heavy measurement goes to stdout, never into the report artifact.

## Modules

### 01_audit_discussion_noise.py (341 LOC)

**Purpose:** Classify dosu-bot noise classes across the discussion MD corpus. Read-only.
**Reads:** discussion MD corpus (`--source-dir PATH` override).
**Writes:** report MD to `md/01_audit_<date>.md`; prints the report path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 02_strip_validation.py (319 LOC)

**Purpose:** Validate the discussion noise strip against the discussion MD corpus. Read-only.
**Reads:** discussion MD corpus (`--source-dir PATH` override); verbatim inline copy of `src/github/discussion_cleaning.py`'s strip logic.
**Writes:** report MD to `md/02_validation_<timestamp>.md`; prints the report path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 03_reclean_discussions.py (273 LOC)

**Purpose:** Re-clean existing discussion MDs with the discussion noise strip — noise-only pass, safe on built MDs. Dry-run by default.
**Reads:** discussion MD corpus (`--source-dir PATH` override); verbatim inline copy of `src/github/discussion_cleaning.py`'s strip logic.
**Writes:** report MD; with `--apply`, overwrites corpus files after a timestamped backup.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 04_reclean_issues.py (157 LOC)

**Purpose:** Re-clean existing issue MDs with the generic noise strip — image/data-URI/no-space pass only. Dry-run by default.
**Reads:** issue MD corpus (`--source-dir PATH` override); verbatim inline copy of `src/github/text_cleaning.py`'s strip logic.
**Writes:** report MD; with `--apply`, overwrites corpus files after a timestamped backup.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 05_strip_build_logs.py (305 LOC)

**Purpose:** Detect and dry-run strip build/install-tool log noise from issue MDs. Measurement and proposal only — no `--apply` exercised.
**Reads:** issue MD corpus (`--source-dir PATH` override, also pointed at `fixtures/` for the regression suite).
**Writes:** dump MD of removed content only; all measurement goes to stdout.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 06_reclean_build_logs.py (250 LOC)

**Purpose:** Re-clean existing issue MDs with the build-log strip — the production re-cleaning counterpart to `05`. Dry-run by default.
**Reads:** issue MD corpus (`--source-dir PATH` override); verbatim inline copy of `src/github/text_cleaning.py`'s strip logic.
**Writes:** report MD; with `--apply`, backs up the full corpus first, then overwrites only changed files.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 07_reclean_migration_headers.py (226 LOC)

**Purpose:** Re-clean existing issue MDs — strip the tracker-migration header (class F) and automated version-removal comments (class G) left by the Bitbucket migration. Dry-run by default.
**Reads:** issue MD corpus (`--source-dir PATH` override); verbatim inline copy of `src/github/index_issues.py`'s class-F/G anchors and removal logic.
**Writes:** report MD with per-class totals and verbatim removed spans; with `--apply`, backs up then overwrites changed files.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 08_audit_debug_stream.py (300 LOC)

**Purpose:** Measure junk class B (DEBUG_STREAM) on the issue MD corpus. Read-only — measurement and a written proposal only, no detector or strip.
**Reads:** issue MD corpus (`--source-dir PATH` override).
**Writes:** report MD with per-shape and repeat-comparison breakdowns; corpus-wide numbers to stdout.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 09_strip_debug_stream.py (226 LOC)

**Purpose:** Detect and dry-run strip junk class B (DEBUG_STREAM) from issue MDs. No `--apply`, never modifies the corpus.
**Reads:** issue MD corpus (`--source-dir PATH` override).
**Writes:** dump MD of removed content only; measurement to stdout.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 10_restore_build_log_files.py (373 LOC)

**Purpose:** Restore the 8 build-log-stripped files to what they would be under the fixed, warning-protected build-log strip. Dry-run by default, never modifies anything unless `--apply`.
**Reads:** the pre-buildlog backup dir and the live issue MD corpus (fixed set of 8 files, no `--source-dir` override).
**Writes:** report MD of per-file added-back lines and any unexpected diff; with `--apply`, backs up the live corpus then overwrites only the changed files.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only (`difflib`).

---

## State
None — each script reads its corpus fresh on every run; no shared state between scripts. A corpus backup created by an `--apply` run is the only persistent side effect, and is not disposable.
