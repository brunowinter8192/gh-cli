# dev/content_cleaning/

## Role
Audit, validate, and re-clean the noise strip for `index_discussions` and `index_issues`. Backs `process-docs/content_cleaning/`, `process-docs/discussion_indexing/`, `process-docs/issue_indexing/`. Operates on the built MD corpora (`github_discussions/` and `github_issues/` doc dirs).

`fixtures/` holds synthetic issue MDs for `05_strip_build_logs.py`, in two groups. Fixtures `01`–`12`: content classes absent from the 844-file corpus that a detector could plausibly mistake for build-log noise, plus a positive control (`12`) and a real-log-ending-in-a-failure case (`04`) — these are pass/fail regression tests; expected result is zero removal on every one of them except `04` (partial — only the disposable log prefix) and `12` (full). Fixtures `13`–`17`: five adversarial cases invented specifically to defeat the detector (a human sentence inside a log run, a lowercase-prose run opening with a vocabulary verb, a remark between two log runs, a sentence opening with a bare anchor word). A stopword-based prose guard was built to pass all five, then reverted (see `process-docs/content_cleaning/`) because none of the five occur in the real corpus and the guard's measured cost — ~6,679 chars of genuine noise no longer removed, `ghostty__2210.md` dropped out of the affected set — was paid against an imagined risk, not an observed one. `13`–`17` are no longer pass/fail tests; they are kept as documentation of exposure this project knowingly accepts. Not real corpus data; never touched by any `--source-dir` default.

## Modules

### 01_audit_discussion_noise.py (350 LOC)

**Purpose:** Classify dosu-bot noise classes across the discussion MDs. Read-only — never modifies source files.
**Reads:** discussion MD corpus (default doc dir; `--source-dir PATH` override).
**Writes:** report MD to `md/01_audit_<date>.md`; prints the report path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 02_strip_validation.py (311 LOC)

**Purpose:** Validate `strip_discussion_noise()` on the 78-MD corpus. Read-only.
**Reads:** discussion MD corpus (`--source-dir PATH` override); verbatim inline copy of `src/github/discussion_cleaning.py` strip logic.
**Writes:** report MD to `md/02_validation_<timestamp>.md`; prints the report path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 03_reclean_discussions.py (286 LOC)

**Purpose:** Re-clean existing discussion MDs with `strip_noise()` — noise-only pass, safe on built MDs (does not touch `##` headings, metadata, attribution headers). Dry-run by default; `--apply` overwrites in place after a timestamped backup.
**Reads:** discussion MD corpus (`--source-dir PATH` override); verbatim inline copy of `src/github/discussion_cleaning.py` strip logic.
**Writes:** report MD to `md/03_reclean_dryrun_<timestamp>.md`; with `--apply`, overwrites corpus files (backup first); prints the report path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 04_reclean_issues.py (168 LOC)

**Purpose:** Re-clean existing issue MDs with `strip_generic_noise()` — image/data-URI/no-space pass only. Additive and safe on already-formatted MDs. Dry-run by default; `--apply` overwrites in place after a timestamped backup.
**Reads:** issue MD corpus (`--source-dir PATH` override); verbatim inline copy of `src/github/text_cleaning.py` strip logic.
**Writes:** report MD to `md/04_reclean_dryrun_<timestamp>.md`; with `--apply`, overwrites corpus files (backup first); prints the report path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

### 05_strip_build_logs.py (367 LOC)

**Purpose:** Detect build/install-tool log noise (setuptools/distutils output, pip/conda install output, compiler invocations + diagnostics, VCS clone output) in issue MDs and dry-run strip it via `strip_build_logs()`. This script itself stays dry-run only — `--apply` exists but is never exercised here; production re-cleaning of the existing corpus is `06_reclean_build_logs.py`. `strip_build_logs()` is an intentional verbatim copy of `src/github/text_cleaning.py`, which is wired into `index_issues.py` for future fetches. Source of truth: `src/github/text_cleaning.py`. Detection is vocabulary (`SIGNAL_PATTERNS`) + run-length threshold (`MIN_BLOCK_LINES`) + bounded bridge (`BRIDGE_GAP`) + hard error/traceback/backtrace exclusion — no prose guard (tried and reverted, see Gotchas).
**Reads:** issue MD corpus (`--source-dir PATH` override, also pointed at `fixtures/` for the regression suite).
**Writes:** dump MD to `md/05_strip_build_logs_dryrun_<timestamp>.md` (removed content only — one `<file>:<start>-<end>` identification line per block, then the verbatim removed text, nothing else); all measurement (corpus/sensitivity/vocabulary-coverage/safety-assertion numbers) goes to stdout, never into the artifact; prints the report path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 06_reclean_build_logs.py (307 LOC)

**Purpose:** Re-clean existing issue MDs with `strip_build_logs()` — build/install-tool log noise pass, mirrors `04_reclean_issues.py`'s shape. Dry-run by default; `--apply` overwrites in place after a timestamped backup (the corpus is gitignored, so the backup is the only safety net); refuses to write anything — report or corpus — if the safety assertion fails. Applied once, 2026-08-28: 8 files changed, 56 blocks, gross 333,184 / net 331,055 chars removed — see `process-docs/content_cleaning/`.
**Reads:** issue MD corpus (`--source-dir PATH` override); verbatim inline copy of `src/github/text_cleaning.py` strip logic.
**Writes:** report MD to `md/06_reclean_dryrun_<timestamp>.md` with both gross (size of text cut out) and net (file shrinkage, accounting for the placeholder written back) chars-removed figures, labelled separately — never collapsed into one number; with `--apply`, backs up the full corpus first to `<source_dir>_PRE_BUILDLOG_STRIP_BACKUP_<timestamp>` (named so its purpose — the only surviving pre-strip record, since the existing corpus has no raw counterpart — is obvious without opening it; not disposable, do not delete), then overwrites only the changed corpus files; prints the report path and backup path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

## Gotchas
- `03_reclean_discussions.py` and `02_strip_validation.py` contain intentional verbatim copies of `src/github/discussion_cleaning.py` (`strip_noise` + `_bare`, `_is_badge_line`, constants): the `block_dev_imports_src` hook forbids `from src.` in dev/. Duplication, not drift — update the copy when the source changes.
- `04_reclean_issues.py` contains an intentional verbatim copy of `src/github/text_cleaning.py` (`strip_generic_noise` + regexes). Source of truth: `src/github/text_cleaning.py`.
- `05_strip_build_logs.py` and `06_reclean_build_logs.py` both contain intentional verbatim copies of `src/github/text_cleaning.py`'s `strip_build_logs()` + everything it needs (`ERROR_RE`/`TRACE_RE`/`BACKTRACE_RE`, `SIGNAL_PATTERNS`, `_find_build_log_blocks`). Two independent copies, matching the existing `02`/`03` precedent for `discussion_cleaning.py` — update both when the source changes.
- A stopword-density prose guard (`_is_prose_line`, a loose-gerund tier, `_is_bridge_blocked`) was built on top of this detector, then fully reverted in both dev copies and in `src/github/text_cleaning.py`. It was built to pass five adversarial fixtures (now `fixtures/13`–`17`) invented specifically to defeat the detector; a full read of 372,885 chars of removed corpus text found zero real instances of any of the five, and the guard's measured cost was real: ~6,679 chars of genuine noise no longer removed, `ghostty__2210.md` dropped out of the affected set, the module grew by ~180 lines, and the guard itself needed three separate collision fixes within one session (`-I`/`-i` compiler flags colliding with pronouns, a repeated flag substring colliding with stopword counting, `.so`/bare-gerund anchors colliding with real tool narration). This project's methodology strips against the real corpus, not against invented content — see `process-docs/content_cleaning/` for the full trail.
- `fixtures/13`–`17` document the accepted exposure left by the revert: a human sentence sandwiched inside a log run, a prose passage that opens with a vocabulary verb, a remark between two log runs, and a sentence opening with a bare anchor word (`Collecting`/`Downloading`) are all swallowed if they occur inside or adjacent to a genuine `MIN_BLOCK_LINES`-or-longer run. None of these five shapes has been observed in the 844-file corpus.
