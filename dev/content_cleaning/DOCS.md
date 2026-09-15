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

### 02_strip_validation.py (328 LOC)

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

### 05_strip_build_logs.py (374 LOC)

**Purpose:** Detect build/install-tool log noise (setuptools/distutils output, pip/conda install output, compiler invocations + diagnostics, VCS clone output) in issue MDs and dry-run strip it via `strip_build_logs()`. This script itself stays dry-run only — `--apply` exists but is never exercised here; production re-cleaning of the existing corpus is `06_reclean_build_logs.py`. `strip_build_logs()` is an intentional verbatim copy of `src/github/text_cleaning.py`, which is wired into `index_issues.py` for future fetches. Source of truth: `src/github/text_cleaning.py`. Detection is vocabulary (`SIGNAL_PATTERNS`) + run-length threshold (`MIN_BLOCK_LINES`) + bounded bridge (`BRIDGE_GAP`) + hard error/traceback/backtrace/**warning** exclusion (`warning` added 2026-09-05 — a warning is content, never noise; see `text_cleaning.py`'s DOCS.md entry) — no prose guard (tried and reverted, see Gotchas).
**Reads:** issue MD corpus (`--source-dir PATH` override, also pointed at `fixtures/` for the regression suite).
**Writes:** dump MD to `md/05_strip_build_logs_dryrun_<timestamp>.md` (removed content only — one `<file>:<start>-<end>` identification line per block, then the verbatim removed text, nothing else); all measurement (corpus/sensitivity/vocabulary-coverage/safety-assertion numbers) goes to stdout, never into the artifact; prints the report path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 06_reclean_build_logs.py (314 LOC)

**Purpose:** Re-clean existing issue MDs with `strip_build_logs()` — build/install-tool log noise pass, mirrors `04_reclean_issues.py`'s shape. Dry-run by default; `--apply` overwrites in place after a timestamped backup (the corpus is gitignored, so the backup is the only safety net); refuses to write anything — report or corpus — if the safety assertion fails. Applied once, 2026-08-28: 8 files changed, 56 blocks, gross 333,184 / net 331,055 chars removed — see `process-docs/content_cleaning/`. `warning` added to the hard exclusion 2026-09-05 (see `text_cleaning.py`'s DOCS.md entry); re-run dry-run against the pre-strip backup shows the fixed detector alone would now remove 8 files, 51 blocks, gross 310,370 chars — 352 lines of warning content across 5 of the 8 files are newly kept; see `process-docs/content_cleaning/` and `10_restore_build_log_files.py` for the restore of the live corpus.
**Reads:** issue MD corpus (`--source-dir PATH` override); verbatim inline copy of `src/github/text_cleaning.py` strip logic.
**Writes:** report MD to `md/06_reclean_dryrun_<timestamp>.md` with both gross (size of text cut out) and net (file shrinkage, accounting for the placeholder written back) chars-removed figures, labelled separately — never collapsed into one number; with `--apply`, backs up the full corpus first to `<source_dir>_PRE_BUILDLOG_STRIP_BACKUP_<timestamp>` (named so its purpose — the only surviving pre-strip record, since the existing corpus has no raw counterpart — is obvious without opening it; not disposable, do not delete), then overwrites only the changed corpus files; prints the report path and backup path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 07_reclean_migration_headers.py (279 LOC)

**Purpose:** Re-clean existing issue MDs — strip two junk classes left by the Bitbucket migration. Class F: the tracker-migration attribution header + rule, a bold `**[Original report](bitbucket_url) by NAME (...).**` line (issue body, first content) or `**Original comment by NAME (...).**` line (each migrated comment), always followed by a blank line then exactly 40 dashes. Class G: a whole comment (separator through body) whose body reduces to solely `Removing version: X (automated comment)` — a class-G comment always carries a nested class-F header, so `_find_all_blocks()` drops any class-F span fully contained inside a class-G span before combining, so per-class totals and the text splice never double-count. Combines the equivalent of `strip_noise`'s class-F branch and `strip_comments_noise`'s class-F + class-G branches into one pass over the whole already-assembled MD. Dry-run by default; `--apply` overwrites in place after a timestamped backup. Applied once, 2026-09-05: 7 files changed (`pyobjc__175/176/31/34/44/76/77.md`; `pyobjc__610.md`, a native GitHub issue, unaffected), 36 spans (31 F, 5 G — G set exactly `pyobjc__175/176/44/76/77.md`), 131 lines (93 F, 38 G), 7,942 chars (6,568 F, 1,374 G) — apply numbers confirmed identical to the approved dry-run; reindex done and recorded separately — see `process-docs/content_cleaning/`.
**Reads:** issue MD corpus (`--source-dir PATH` override); verbatim inline copy of `src/github/index_issues.py`'s class-F and class-G anchors + removal logic.
**Writes:** report MD to `md/07_reclean_dryrun_<timestamp>.md` — summary numbers split F/G, a per-file table split F/G, then the verbatim removed text for every span (one `<file>:<start>-<end> [F|G]` identification line per span, then the text, nothing else) so the whole removal can be read in full; with `--apply`, backs up the full corpus first to `<source_dir>_PRE_MIGRATION_NOISE_STRIP_BACKUP_<timestamp>` (not disposable, do not delete), then overwrites only the changed corpus files; prints the report path and backup path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 08_audit_debug_stream.py (341 LOC)

**Purpose:** Measure junk class B (DEBUG_STREAM — app debug/log lines pasted from a terminal, distinct from class A build/install output) on the issue MD corpus. Read-only — never modifies the corpus; no detector or strip, measurement + a written proposal only. Vocabulary (derived by reading real files, not the junk-class inventory's 3 examples alone): `ghostty_debug` (`^(debug|info|warning)\([a-zA-Z_]+\):`), `playwright_pw` (`^\s*pw:[a-z:]+`, also covers the `pw:browser` sub-shape), `loguru_narration` (loguru's `TIMESTAMP | LEVEL | module:func:line - msg` with LEVEL restricted to `TRACE/DEBUG/INFO/SUCCESS/WARNING` — ERROR/CRITICAL deliberately excluded, those are the retrieval target). Measures, per shape: files/lines/chars, repo clustering, run-length histogram (`_find_shape_runs`, a single-vocabulary simplification of `_find_build_log_blocks`'s bridging discipline). Also measures literal-repeat vs. normalized-fingerprint (`_normalize_fingerprint`: digits/hex/UUID/timestamp collapsed) repeats corpus-wide, and adjacency (windows 0/3/10 lines) between each vocabulary-matched line and a currently-protected line (`ERROR_RE`/`TRACE_RE`/`BACKTRACE_RE`, verbatim copy) vs. a proposed, measurement-only extension (`PROPOSED_CRASH_RE`: `panic:`/`Segmentation fault`/`SIG(ABRT|SEGV|ILL|BUS|FPE)`/`Aborted (core dumped)`; `PROPOSED_UNRESOLVED_FRAME_RE`: unresolved `???:?:?: 0x... in ???` backtrace frames) — found reading `ghostty__10406.md`/`ghostty__10379.md`, where real crash content matches none of the existing protected regexes. Measured on the 963-file corpus (2026-09-05): 55 files, 2,957 lines, 485,182 chars (6.64% of corpus) candidate across the 3 shapes; see `process-docs/content_cleaning/` for the full proposal, the non-B evidence, and the gate recommendation.
**Reads:** issue MD corpus (`--source-dir PATH` override).
**Writes:** report MD to `md/08_audit_<timestamp>.md` — per-shape file/line/chars/repo/run-length breakdown with per-file evidence lines, plus the literal-vs-fingerprint repeat comparison with top-delta files and their normalized examples; corpus-wide numbers (per-shape totals, repeat comparison, adjacency counts) go to stdout; prints the report path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 09_strip_debug_stream.py (310 LOC)

**Purpose:** Detect + dry-run strip junk class B (DEBUG_STREAM) from issue MDs — dry-run only, no `--apply`, shaped like `strip_build_logs` (vocabulary + run-length floor + per-line hard exclusion, block starts/ends only on a signal line) but deliberately has **no bridge** (gaps between same-shape runs are overwhelmingly genuinely protected error content or meaningful non-filler prose, never a harmless wrapped continuation — a bridge would routinely jump across real, protected error content). Vocabulary unchanged from `08_audit_debug_stream.py`. `MIN_RUN_LINES = 3` (raised from an initially-accepted 2 after the precision read of the first dry-run found two real signal lines — `signal=SIGBUS`/`signal=SIGTRAP` process-exit lines — sitting in exactly length-2 runs). Protected set: `ERROR_RE`/`TRACE_RE`/`BACKTRACE_RE` (existing) plus `CRASH_RE` (decided in, iteratively evidenced): `panic:`, `Segmentation fault`, `signal=SIG\w+`, `core dumped`, `#FailureMessage`, `Crash keys:`, `Received signal \d+`, `exitCode=\d{5,}` — each added on a specific corpus-found case across three precision-read iterations (SIGBUS/SIGTRAP process-exit lines; a 33-line qemu native crash too long for any floor to exclude; Chromium's own `#FailureMessage`/`Crash keys:` crash markers; macOS's `Received signal N NAME` handler; Windows NTSTATUS crash exit codes, confirmed by a maintainer comment in `playwright__37199.md` directly analyzing one such exit code). The unresolved-backtrace-frame pattern proposed in M1 (`???:?:?: 0x... in ???`) is decided **out** — zero corpus overlap with any B-vocabulary match. Accepted, documented residue: generic native Chromium backtrace frames (function names + hex addresses, e.g. `ChromeMain [0x...+N]`) still get removed as part of otherwise-legitimate blocks in 3 files (206 lines) — judged non-retrieval-value since the actual crash-type markers are separately protected and preserved. Final numbers (2026-09-05): 41 files, 144 blocks, 2,645 lines, 382,151 gross / 376,352 net chars, 5.23% of corpus. Safety assertion: PASS, 2,645 lines checked, 0 violations. See `process-docs/content_cleaning/` for the full iteration log, the precision-read findings, and the recall-check breakdown (410 surviving vocabulary-matched lines: 257 individually protected, 153 below the run-length floor — all read and judged safe).
**Reads:** issue MD corpus (`--source-dir PATH` override).
**Writes:** dump MD to `md/09_strip_debug_stream_dryrun_<timestamp>.md` (removed content only — one `<file>:<start>-<end> [shape]` identification line per block, then the verbatim removed text, nothing else); numbers (per-shape and total files/blocks/lines/gross+net chars/% corpus/safety) go to stdout, never into the artifact; prints the report path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

---

### 10_restore_build_log_files.py (400 LOC)

**Purpose:** Restore the 8 files the 2026-08-28 build-log strip touched to what they would be under the fixed, warning-protected `strip_build_logs()`: for each, PRE_BUILDLOG backup version → fixed `strip_build_logs()` → class F+G strip (verbatim copy of `07_reclean_migration_headers.py`'s logic, needed for the 3 pyobjc files, which predate the 2026-09-05 F/G milestone and so still carry that noise in the backup) → diff against the live file. Dry-run by default, never modifies anything. Diffing excludes placeholder lines (`_strip_placeholders`) from the comparison — a placeholder's wording/count is expected to change under the fix (fewer lines removed per block, or a block splitting around a newly-protected line), not "content" that could regress; only real, non-placeholder lines are checked, via `difflib.SequenceMatcher` opcodes (`insert` = expected lines added back, `delete`/`replace` = unexpected, must be empty). Dry-run result (2026-09-05): 5/8 files changed, 352 lines added back, **0 unexpected diffs** across all 8 files — confirmed by reading the added-back lines and cross-checking against the separate cost-measurement report. `--apply` backs up the live corpus dir to `<corpus>_PRE_WARNING_RESTORE_BACKUP_<timestamp>` then overwrites only the 8 files; refuses (exits non-zero) if any file shows an unexpected diff. Not yet applied — awaiting approval on the dry-run; see `process-docs/content_cleaning/`.
**Reads:** the PRE_BUILDLOG backup dir and the live issue MD corpus (fixed paths, no `--source-dir` override — this script is specific to the 8 named files).
**Writes:** report MD to `md/10_restore_dryrun_<timestamp>.md` — per-file table (changed/lines added back/unexpected diffs/placeholder counts) plus per-file verbatim added-back lines and any unexpected diff; with `--apply`, backs up the full live corpus first, then overwrites only the changed files among the 8; prints the report path and (if applied) backup path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only (`difflib`).

## Gotchas
- `03_reclean_discussions.py` and `02_strip_validation.py` contain intentional verbatim copies of `src/github/discussion_cleaning.py` (`strip_noise` + `_bare`, `_is_badge_line`, constants): the `block_dev_imports_src` hook forbids `from src.` in dev/. Duplication, not drift — update the copy when the source changes.
- `04_reclean_issues.py` contains an intentional verbatim copy of `src/github/text_cleaning.py` (`strip_generic_noise` + regexes). Source of truth: `src/github/text_cleaning.py`.
- `05_strip_build_logs.py` and `06_reclean_build_logs.py` both contain intentional verbatim copies of `src/github/text_cleaning.py`'s `strip_build_logs()` + everything it needs (`ERROR_RE`/`TRACE_RE`/`BACKTRACE_RE`, `SIGNAL_PATTERNS`, `_find_build_log_blocks`). Two independent copies, matching the existing `02`/`03` precedent for `discussion_cleaning.py` — update both when the source changes. `10_restore_build_log_files.py` carries a third copy of the same `strip_build_logs()` logic (post-warning-fix) plus an independent copy of `07_reclean_migration_headers.py`'s class-F/G logic — two verbatim copies in one file, update both halves when either source changes.
- `warning` was added to `ERROR_RE` 2026-09-05 (project premise: content and context have absolute priority, a warning is content, never noise) after `MinerU__1418.md`'s `"WARNING: magic-pdf 0.6.1 does not provide the extra 'full'"` was found bridged over by the pre-fix detector. Three `SIGNAL_PATTERNS` entries that only ever matched warning lines (`warning: no ... found matching`, `clang: warning:`, `N warnings generated`) were removed as dead weight; the compiler-diagnostic header entry was narrowed from `(warning|note):` to `note:` only. Verified byte-identical across all three copies (`text_cleaning.py`, `05`, `06`) for the shared `ERROR_RE`/`SIGNAL_PATTERNS` block. See `process-docs/content_cleaning/` for the corpus-wide cost measurement (352 lines newly kept across 5 of the 8 previously-stripped files) and the restore dry-run (`10_restore_build_log_files.py`).
- A stopword-density prose guard (`_is_prose_line`, a loose-gerund tier, `_is_bridge_blocked`) was built on top of this detector, then fully reverted in both dev copies and in `src/github/text_cleaning.py`. It was built to pass five adversarial fixtures (now `fixtures/13`–`17`) invented specifically to defeat the detector; a full read of 372,885 chars of removed corpus text found zero real instances of any of the five, and the guard's measured cost was real: ~6,679 chars of genuine noise no longer removed, `ghostty__2210.md` dropped out of the affected set, the module grew by ~180 lines, and the guard itself needed three separate collision fixes within one session (`-I`/`-i` compiler flags colliding with pronouns, a repeated flag substring colliding with stopword counting, `.so`/bare-gerund anchors colliding with real tool narration). This project's methodology strips against the real corpus, not against invented content — see `process-docs/content_cleaning/` for the full trail.
- `fixtures/13`–`17` document the accepted exposure left by the revert: a human sentence sandwiched inside a log run, a prose passage that opens with a vocabulary verb, a remark between two log runs, and a sentence opening with a bare anchor word (`Collecting`/`Downloading`) are all swallowed if they occur inside or adjacent to a genuine `MIN_BLOCK_LINES`-or-longer run. None of these five shapes has been observed in the 844-file corpus.
- `07_reclean_migration_headers.py` contains an intentional verbatim copy of `src/github/index_issues.py`'s class-F anchors (`MIGRATION_REPORT_RE`, `MIGRATION_COMMENT_RE`, `MIGRATION_RULE_RE`) and class-G anchors (`SEP_RE`, `AUTOMATED_COMMENT_RE`, `_is_automated_only_comment`), plus removal logic (`_find_migration_blocks` + `_find_automated_comment_blocks` + `_find_all_blocks` + `strip_migration_and_automated`, a `strip_build_logs`-shaped block-and-splice, no placeholder). Source of truth: `src/github/index_issues.py`. Unlike `strip_noise`/`strip_comments_noise`, this script runs both classes' removal on the whole already-built MD in one pass rather than on body/comments separately — safe because the anchor forms never occur outside their respective section and match nothing else observed in the corpus. Because src's `strip_comments_noise` is a line-state-machine (an `in_automated_block` flag short-circuits the nested class-F branch for lines inside a dropped comment) while this script is block-find-then-splice, `_find_all_blocks()` has to explicitly drop any class-F span nested inside a class-G span before combining — the state machine gets this for free from elif ordering, the block-based script does not, and skipping that step would double-list and double-splice the same lines.
