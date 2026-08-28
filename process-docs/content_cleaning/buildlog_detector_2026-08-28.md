# Build/Install Log Detector — dry-run design + adversarial hardening (2026-08-28)

Process record for `dev/content_cleaning/05_strip_build_logs.py`: a dry-run-only detector for
build/install-tool log noise (setuptools/distutils output, pip/conda install output, compiler
invocations + diagnostics, VCS clone output) in the 844-file, 19-repo `github_issues` MD corpus.
No production integration in this milestone — `strip_build_logs()` is written to move verbatim
into `src/github/text_cleaning.py` later, separately approved. This file is the investigation
trail; the current shape of the detector lives in the module itself and in
`dev/content_cleaning/DOCS.md`.

## Detection mechanism

Three tiers, not one flat vocabulary list:
- `_LOOSE_VERB_RE` / `_LOOSE_GERUND_RE` — single common English words (`running`/`creating`/
  `copying`/... ; `Collecting`/`Downloading`) that can plausibly open a real sentence. Gated by
  a stopword-density prose check (`_is_prose_line`) before being accepted as signal.
- `SIGNAL_PATTERNS` — multi-word or digit/colon-anchored phrases (`Requirement already
  satisfied`, `file:line:col: warning:` headers, VCS summaries with embedded counts). Not
  prose-gated for signal classification — see "Per-anchor prose-gating cost" below for why.
- A run-length threshold (`MIN_BLOCK_LINES = 10` by default) plus a bounded bridge (`BRIDGE_GAP
  = 3`) that lets a run cross a small number of non-signal filler lines (wrapped compiler
  diagnostic messages, source-context lines). A block is only ever removed if it reaches the
  threshold; a block only ever starts and ends on a confirmed signal line, never on bridged
  filler.

Hard exclusions, applied everywhere (never signal, never bridged over, always break a run):
`error|fatal|traceback|exception|failed` (case-insensitive substring), a Python traceback frame
(`File "...", line N, in `), and a native/gdb backtrace frame (`path:line:col: 0xADDR in func`).

## Vocabulary determination

Read `pyobjc__34/175/176.md`, `curl_cffi__74.md`, `MinerU__2262/1418.md` plus a full-corpus scan.
Re-measured a prior claim that a narrow 7-verb baseline (`copying/creating/running/writing/
reading/installing/byte-compiling`) covered 34% of the worst file's build log — could not
reproduce 34% from the narrow baseline alone (got 43.4% on a raw line-match basis against
`pyobjc__34.md`, the corpus's largest file at 198,266 chars); treated the original number as
unverifiable rather than ground truth. The full vocabulary matches 63.8% of that file's candidate
lines pre-gating; after run-length gating, final removal is 37.2% of the file's chars.

Sensitivity to `MIN_BLOCK_LINES` measured at 5/8/10/15/20/30 (values in the module and in each
generated report's stdout summary). 10 chosen as the production default: lower thresholds mostly
add short env-info/download-progress dumps of debatable retrieval value; higher thresholds start
dropping legitimately large pip/compiler blocks.

## Pip-list vocabulary — removed

An earlier iteration included a two-column package/version table row pattern (`^[A-Za-z][\w.\-]*
\s{2,}[\w.\-]+$` plus a `Package  Version` header and a dashed-underline row), on the theory that
a `pip list` dump is as disposable as `pip install` progress narration. A full manual read of
every removed block (all 62 blocks, 361,245 chars, first line to last) found one real cost: in
one file, a maintainer's
diagnostic conclusion ("looked at your dependency list, doesn't look like anything's missing")
directly referenced a table that would have been removed, and while the conclusion text itself
survived, the evidence underneath it would not have. Verdict: a package/version manifest is
structured *fact* (what was installed), not progress narration (what a tool did next) — nobody
searches for the latter, people do search for the former during a dependency-conflict
investigation. The whole category was dropped, not narrowed. Corpus effect: files affected
11 → 8, blocks 62 → 56, chars removed 361,245 → 333,184.

## The prose guard — five adversarial fixtures, iteratively hardening one mechanism

An independent adversarial pass (not corpus-derived — synthetic fixtures built specifically to
probe content classes absent from the 844-file sample) found two destructive mechanisms sharing
one root cause: `BRIDGE_GAP` bridged over *any* non-error filler line, including a human
sentence sandwiched inside a pasted log; and the loose-verb pattern had no defense against a
sentence that happened to open with one of its verbs.

Fix: `_is_prose_line()`, a stopword-density check (2+ *distinct* stopwords from a curated list
→ prose), used in two places — as a bridge-candidate blocker (`_is_bridge_blocked`, so a sentence
between two signal lines hard-stops the run exactly like an error line would) and as an
additional requirement on the loose verb/gerund patterns specifically (so "running the tests
locally is step one" is never classified as signal in the first place).

Two false-positive classes surfaced and were fixed during this work, both via full-corpus
regression testing, not the adversarial fixtures themselves:
- Naive `[A-Za-z']+` tokenization ignores digits, so `-I/path` (a real compiler include flag)
  fragments into a bare `I` (pronoun collision) and `i386`/`x86_64` do the same. Fixed with
  `\b...\b` word-boundary anchoring, which refuses to match inside a `\w` run containing digits.
- Counting stopword *occurrences* let a repeated flag substring (`-Wshorten-64-to-32` contributing
  a second `to` alongside a diagnostic's genuine `to`) hit the threshold on a duplicated word.
  Fixed by counting distinct stopwords via a set, not a running count.
- `a` and `i` are excluded from the stopword list entirely: single-letter C macro/loop params
  (`#define ALIGN(v, a) ...`) and the `-I`/`-i` flag pattern make them structurally collision-
  prone in a way multi-letter stopwords are not.

A fifth adversarial fixture closed a scope boundary flagged (not silently decided) after the
fourth: a sentence opening with a *bare anchor word* that lives in the un-prose-gated
`SIGNAL_PATTERNS` tier (`"Downloading the wheel by hand ... is the only thing that worked for
me."`) was still swallowed, because it never reached the prose check at all.

## Per-anchor prose-gating cost (full 844-file corpus)

Measured, per individual anchor phrase, how many corpus lines currently matched by that anchor
would stop being removed if it were prose-gated:

| Anchor | Matched | Cost if gated | Decision |
|---|---|---|---|
| `Collecting` | 420 | 0 | Gated — free |
| `Downloading` | 292 | 16 (gdb debug-symbol fetch, modelscope model-download messages) | Gated anyway — same bare-word exposure as the fixture that found it |
| `Requirement already satisfied` | 302 | 300 | Left ungated |
| `file:line:col: warning/note:` diagnostic header | 105 | 8 | Left ungated |
| `The following packages will be downloaded:` | 4 | 4 | Left ungated |
| `Created wheel for` | 2 | 2 | Left ungated |
| `Use 'X' instead of 'Y' as the compiler` | 2 | 2 | Left ungated |
| `added N changesets with M changes to K files` | 1 | 1 | Left ungated |
| ~30 other anchors (VCS, conda spec rows, progress bars, digit-anchored summaries) | — | 0 | No decision needed either way |

Only `Collecting` and `Downloading` are bare single gerunds with no required continuation; every
other anchor requires a specific multi-word phrase or digit/colon structure, which is why they
stay ungated despite occasionally containing stopwords — the corpus-grep methodology from the
`content_cleaning` area's earlier work (a phrase this specific essentially never occurs in human
prose) still applies to them.

**Residual, accepted exposure**, stated explicitly rather than left implicit: a sentence
containing the *complete literal text* of an ungated `SIGNAL_PATTERNS` anchor (e.g. "Requirement
already satisfied", "Created wheel for", "Use '...' instead of '...' as the compiler", a
well-formed `file:line:col:` diagnostic header) would still be swallowed if it opened or extended
a run. Judged low-probability given how syntactically specific each phrase is, but not fixed.

## Fixtures — permanent regression suite

`dev/content_cleaning/fixtures/` (17 files): 12 covering content classes absent from the current
corpus that a detector could plausibly mistake for build-log noise (step-by-step instructions,
Dockerfiles/CI workflows, setup.py/CMake source with compiler flags, a log genuinely ending in
the issue's failure, a short maintainer fix sequence, non-package two-column tables, changelog
bullets, a non-English issue, a `pip list` dependency-conflict regression check, a raw install
script pasted as source, and a positive control that must still fire) plus 5 adversarial cases
(A–E) that found and fixed the prose-guard gaps above. Expected result, checked after every
change to the detector: zero removal on every fixture except the positive control and the
log-ending-in-failure case (where only the disposable log prefix is removed, never the failure).

## Results as of 2026-08-28

Full corpus: 7 files affected, 66 blocks, 3,331 lines removed, 326,505 chars removed. Safety
assertion (no removed line contains `error`/`fatal`/`Traceback`/`Exception`/`failed`):
3,331 lines checked, 0 violations. Same file set affected before and after the prose-guard work
(one file, `ghostty__2210.md`, dropped out as the accepted cost of gating `Downloading`).

## Artifacts

- `dev/content_cleaning/05_strip_build_logs.py` — the detector, structured as a verbatim-copy
  candidate for `src/github/text_cleaning.py`.
- `dev/content_cleaning/fixtures/` — the 17-file regression suite.
- `dev/content_cleaning/md/05_strip_build_logs_dryrun_<timestamp>.md` — dump artifacts (removed
  content only, no summary/commentary in the file; all measurement goes to stdout).
