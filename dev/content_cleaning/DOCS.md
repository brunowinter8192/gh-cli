# dev/content_cleaning/

## Role
Audit, validate, and re-clean the noise strip for `index_discussions` and `index_issues`. Backs `process-docs/content_cleaning/`, `process-docs/discussion_indexing/`, `process-docs/issue_indexing/`. Operates on the built MD corpora (`github_discussions/` and `github_issues/` doc dirs).

`fixtures/` holds synthetic issue MDs used only by `05_strip_build_logs.py`'s adversarial regression suite — legitimate content shaped to plausibly trip the build-log detector, plus one positive control that must still fire. Not real corpus data; never touched by any `--source-dir` default.

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

### 05_strip_build_logs.py (450 LOC)

**Purpose:** Detect build/install-tool log noise (setuptools/distutils output, pip/conda install output, compiler invocations + diagnostics, VCS clone output) in issue MDs and dry-run strip it via `strip_build_logs()`. Read-only in the current milestone — dry-run only, `--apply` exists but is never exercised. `strip_build_logs()` is written to be moved verbatim into `src/github/text_cleaning.py` in a later, separately approved step.
**Reads:** issue MD corpus (`--source-dir PATH` override, also pointed at `fixtures/` for the regression suite).
**Writes:** dump MD to `md/05_strip_build_logs_dryrun_<timestamp>.md` (removed content only — one `<file>:<start>-<end>` identification line per block, then the verbatim removed text, nothing else); all measurement (corpus/sensitivity/vocabulary-coverage/safety-assertion numbers) goes to stdout, never into the artifact; prints the report path.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib only.

## Gotchas
- `03_reclean_discussions.py` and `02_strip_validation.py` contain intentional verbatim copies of `src/github/discussion_cleaning.py` (`strip_noise` + `_bare`, `_is_badge_line`, constants): the `block_dev_imports_src` hook forbids `from src.` in dev/. Duplication, not drift — update the copy when the source changes.
- `04_reclean_issues.py` contains an intentional verbatim copy of `src/github/text_cleaning.py` (`strip_generic_noise` + regexes). Source of truth: `src/github/text_cleaning.py`.
- `05_strip_build_logs.py`'s detection has three tiers, not one vocabulary list: `_LOOSE_VERB_RE`/`_LOOSE_GERUND_RE` (single common words — `running`/`creating`/`copying`/... and `Collecting`/`Downloading` — ambiguous enough to open a real sentence, so these alone are also required to fail `_is_prose_line()`) vs. `SIGNAL_PATTERNS` (multi-word or digit/colon-anchored phrases, e.g. "Requirement already satisfied", a `file:line:col: warning:` header — left un-prose-gated on purpose, since gating them cost ~300 genuine pip lines in testing). A bridge candidate (arbitrary filler between two confirmed signal lines) is prose-gated regardless of category via `_is_bridge_blocked()` — that's what stops a human sentence sandwiched inside a log run from being bridged over. See `process-docs/content_cleaning/` for the full per-anchor cost measurement and the adversarial-fixture trail behind this design.
- The prose guard's stopword tokenizer deliberately excludes single-letter words `a`/`i`: `-I/path` (compiler include flag) and single-letter C macro params (`#define ALIGN(v, a) ...`) collide with the pronoun "I" and article "a" respectively. Stopword hits are counted as a *set* (distinct words), not a running count — a compiler flag like `-Wshorten-64-to-32` can contribute a second, spurious `to` alongside a diagnostic message's genuine one.
- Residual, accepted exposure: a sentence containing the *complete, literal* text of an un-prose-gated `SIGNAL_PATTERNS` anchor (e.g. "Requirement already satisfied", "Created wheel for", "Use 'X' instead of 'Y' as the compiler") would still be swallowed. Judged low-risk (implausibly exact phrasing) but not fixed — flagged explicitly rather than silently decided.
