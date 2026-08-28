# Prose Guard Revert + Raw-Fetch Logging + Production Integration (2026-08-28)

Process record for three changes made together after production integration was approved and
merged: reverting the stopword-based prose guard from the build-log detector (both dev copies
and `src/github/text_cleaning.py`), adding a raw-fetch logging mechanism ahead of any strip, and
completing the re-clean dry-run check. No `--apply` was run and the RAG index was not touched.

## Why the prose guard was reverted

The guard (`_is_prose_line`, a loose-gerund vocabulary tier, `_is_bridge_blocked`) was built
across several rounds specifically to defeat five adversarial fixtures invented to probe the
detector: a human sentence sandwiched inside a log run, a prose passage opening with a loose
vocabulary verb, a remark between two log runs, and a sentence opening with a bare anchor word
(`Collecting`/`Downloading`). All five were synthetic — not one instance of any of them was found
in the 844-file `github_issues` corpus. A full manual read of every removed block in that corpus
(62 blocks, 361,245 chars, first line to last) had already been done as part of building the
detector, and it found zero swallowed human sentences before the guard existed.

The guard's cost, measured precisely rather than estimated: with the guard, the corpus dry-run
showed 7 files affected, 66 blocks, 326,505 chars removed (gross); without it, 8 files, 56
blocks, 333,184 chars. The difference — 6,679 chars of genuine build/install-tool noise — is
exactly the noise the guard prevented from being removed, and `ghostty__2210.md` dropped out of
the affected set entirely (its sole block was `Downloading separate debug info for ...` lines,
gdb's own symbol-fetch narration, caught by the guard's "Downloading" gate). Building the guard
also cost real engineering: the module grew from roughly 200 to over 260 lines, and the guard
itself needed three separate collision fixes within a single session — `-I`/`-i` compiler include
flags and single-letter C macro params colliding with the pronoun "I" and article "a", a repeated
flag substring (`-Wshorten-64-to-32`) colliding with stopword-occurrence counting, and the `.so`
shared-library extension plus real gdb/modelscope narration colliding with the bare-gerund gate.

This project's methodology (see the `content_cleaning` area's earlier entries) gates every strip
against the real corpus — grep the corpus, measure the cost, decide. The prose guard was gated
against invented content instead, and paid a real, measured price against a risk that, as of
2026-08-28, has zero observed instances. Reverted in full: `dev/content_cleaning/
05_strip_build_logs.py`, `dev/content_cleaning/06_reclean_build_logs.py`, and
`src/github/text_cleaning.py` are all back to vocabulary (`SIGNAL_PATTERNS`) + run-length
threshold (`MIN_BLOCK_LINES`) + bounded bridge (`BRIDGE_GAP`) + hard error/traceback/backtrace
exclusion (`ERROR_RE`/`TRACE_RE`/`BACKTRACE_RE`) — the same three files, byte-for-byte parity
checked against each other and against the pre-guard git history.

`dev/content_cleaning/fixtures/13`–`17` (the five adversarial cases) are kept, not deleted. They
no longer function as pass/fail regression tests — re-running the reverted detector against them
shows all five now get swallowed again, confirmed directly (`13`: the sandwiched sentence is
gone; `14`: the entire 14-line prose passage is gone; `16`: both log runs merge into one block
and the remark between them is gone; `17`: the sentence opening with "Downloading" is gone). They
now document, precisely, the exposure this project knowingly accepts: a human sentence adjacent
to or between genuine `MIN_BLOCK_LINES`-or-longer build-log runs can be swallowed if it does not
itself break the run.

## Raw-fetch logging

There was no way to re-evaluate this trade-off, or any future filter change, against real
before/after data — the moment `strip_build_logs()` (or any strip) runs, the original text is
gone, and the only evidence available was inventing new fixtures each time. `src/github/
raw_logging.py` (`log_raw_issue`) fixes that going forward: for every issue fetched by
`index_issues_workflow`, the raw issue body and raw comments text — exactly as
`get_issue_workflow`/`get_issue_comments_workflow` returned them, before `strip_noise`,
`strip_comments_noise`, `strip_generic_noise`, or `strip_build_logs` touch anything — are written
to `logs/raw_issues/<repo_basename>__<num>.md`, the same filename the cleaned MD gets in
`RAG_DOC_DIR`, so the two diff directly by name. `logs/` sits at the gh-cli repo root (computed
relative to `raw_logging.py`'s own path, not hardcoded), entirely outside the RAG documents tree
(a different project on disk) and covered by the existing `logs/`/`*.log` `.gitignore` entries.

A companion `logs/raw_issues/_manifest.jsonl` gets one appended JSON line per fetch (`file`,
`fetched_at`, `cleaning_version`), where `cleaning_version` is a manually-bumped string constant
in `raw_logging.py` (`CLEANING_VERSION`, currently `"2026-08-28-no-prose-guard"`). Without this,
a raw/cleaned diff found months from now would be uninterpretable — the filter keeps changing
underneath the corpus, and nothing else on disk records which version produced which cleaned
file. Bumping this constant is now part of changing any strip in the pipeline.

`log_raw_issue` never raises: a write failure (permission, disk full, whatever) is caught broadly,
logged via `logger.warning`, and the fetch continues — verified directly by pointing it at an
unwritable path and confirming no exception propagates. This is a deliberate, documented
exception to the project's normal fail-fast rule: a missing raw log is a future-evidence loss,
not a correctness problem for the current fetch, so it must never block indexing.

**No backfill.** The 844 (now 873, corpus grows with ongoing use) already-cleaned MDs in
`github_issues` have no raw counterpart and cannot get one — the original API responses were
never persisted before this change, and there is no way to reconstruct them. Raw logging starts
covering fetches from this change forward only. This is stated plainly rather than implied
otherwise.

## Where strip_build_logs sits in the pipeline, and why

`index_issues_workflow` strips the issue body and the comments blob **separately** — each gets
its own `strip_noise`/`strip_generic_noise`/`strip_build_logs` (or `strip_comments_noise`/
`strip_generic_noise`/`strip_build_logs`) call — rather than assembling the full MD first and
stripping once. This was chosen with an explicit boundary-spanning check: `build_issue_md()`
always separates body and comments with a blank line, then `# Comments on ...` / `Total: N
comments`, then another blank line before `--- Comment 1 ---`, and each `--- Comment N ---`
separator between two comments is itself immediately bounded by blank lines. The bridge mechanism
in `_find_build_log_blocks` can never skip across a blank line to reach a line it has not
confirmed is signal (a candidate bridge span that lands on a blank line always fails the "is the
line at the far end actually signal" check, regardless of remaining gap budget). Verified
empirically as well as by inspection: running `strip_build_logs` on the two pieces separately and
concatenating produced an identical placeholder count to running it once on the fully assembled
text, for a real corpus file (`MinerU__2262.md`, 10 blocks either way). Separate processing is
therefore behaviorally equivalent to assembled processing for this corpus's structure, while
being the smaller, more consistent change (matches how `strip_generic_noise` was already applied
per-piece before this milestone).

## Dry-run numbers, post-revert (2026-08-28)

Corpus: 873 files (grew from 844 during this session via ordinary use, unrelated to this work).
`06_reclean_build_logs.py --source-dir <corpus>` (dry-run, no `--apply`):

- Files that would change: **8 / 873**
- Blocks: **56**
- Chars removed, gross (size of text cut out): **333,184**
- Chars removed, net (file shrinkage, accounting for the placeholder written back in each
  block's place): **331,055**

Both numbers are correct measurements of different things and neither supersedes the other:
gross is what a reader would have seen removed; net is what the file on disk actually shrinks by.
The 8 affected files match the pre-guard measurement exactly (`MinerU__2262.md`, `pyobjc__34.md`,
`pyobjc__176.md`, `pyobjc__175.md`, `MinerU__826.md`, `MinerU__1418.md`, `curl_cffi__74.md`,
`ghostty__2210.md`). Safety assertion: PASS, 0 violations, confirmed by a clean (no stderr output,
exit 0) run in addition to the report's own PASS line. No `--apply` was run; the corpus was not
modified; the RAG index was not touched.

## Artifacts

- `src/github/text_cleaning.py`, `dev/content_cleaning/05_strip_build_logs.py`,
  `dev/content_cleaning/06_reclean_build_logs.py` — reverted detector, verbatim-parity checked.
- `src/github/raw_logging.py` — new module, wired into `src/github/index_issues.py`.
- `dev/content_cleaning/fixtures/13`–`17` — kept as documented accepted exposure, no longer
  pass/fail tests.
- `dev/content_cleaning/md/06_reclean_dryrun_2026*.md` — the dry-run report behind the numbers
  above.
