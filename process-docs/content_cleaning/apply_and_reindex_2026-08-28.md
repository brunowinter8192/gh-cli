# Build-Log Re-Clean Apply + Reindex (2026-08-28)

Process record for the one and only `--apply` run of `dev/content_cleaning/06_reclean_build_logs.py`
against the live `github_issues` corpus, and the reindex that followed. This is the corpus's
first-ever build-log strip; the dry-run numbers behind the decision to apply live in
`process-docs/content_cleaning/revert_and_raw_logging_2026-08-28.md`.

## File apply — before/after, parallel-write check

Recorded immediately before starting: **873 files**, newest mtime `2026-08-28 21:30:34.044777`
(`claude-code__87340.md` — a leftover from an earlier, unrelated parallel session's
`index_issues` run, already accounted for in the file-count baseline).

`06_reclean_build_logs.py --apply` ran. Backup created at
`data/documents/github_issues_PRE_BUILDLOG_STRIP_BACKUP_20260828_230949` — confirmed to exist and
hold the full pre-strip corpus (873 files) before any file was overwritten. This backup is
deliberately not a disposable safety net: the corpus's 873 MDs have no raw counterpart (raw
logging only covers fetches from this same session onward), so this directory is the only
surviving record of their pre-build-log-strip state, and the naming says so. Do not delete it.

Recorded immediately after: **873 files** (unchanged — the re-clean only overwrites, never
adds/removes), newest mtime `2026-08-28 23:09:50.364697` (`pyobjc__34.md`). Every file with an
mtime inside the apply's write window (`>= 23:09:50`) was enumerated: exactly 8, all within the
same millisecond burst (`23:09:50.363`–`.364697`) — `MinerU__1418.md`, `MinerU__2262.md`,
`MinerU__826.md`, `curl_cffi__74.md`, `ghostty__2210.md`, `pyobjc__175.md`, `pyobjc__176.md`,
`pyobjc__34.md`. No extra files, no count drift. No parallel write landed on the corpus during
this specific window.

## Reindex — a self-inflicted overlap, not a mystery third party

Per-document chunk counts were queried directly against the Postgres `documents` table
(`SELECT document, COUNT(*) ... GROUP BY document`) rather than through the CLI, for precision.

**Before reindex:** total 5,060 chunks. Per file: `MinerU__1418.md`=19, `MinerU__2262.md`=53,
`MinerU__826.md`=40, `curl_cffi__74.md`=47, `ghostty__2210.md`=56, `pyobjc__175.md`=43,
`pyobjc__176.md`=47, `pyobjc__34.md`=154.

The reindex command hit a `lock busy` error on the first attempt — an unrelated `update_docs` run
from another session, on a different collection, already holding the lock. After it cleared, two
client-side attempts reported as "timed out" (one after 0s due to a timeout value I passed in the
wrong unit, one after the tool's 2-minute default). A third attempt, given a generous explicit
timeout, completed and printed a full summary: `Found 873 markdown files`, `Skipped (hash
unchanged): 869`, `To index: 4` — naming only `ghostty__2210.md`, `pyobjc__175.md`,
`pyobjc__176.md`, `pyobjc__34.md`.

That is inconsistent with only 4 files having changed on disk — 8 were rewritten. The
after-query (below) shows all 8 with reduced chunk counts, not just the 4 named. The most
parsimonious explanation, and the one I believe is correct: a client-side "timeout" from this
tool does not necessarily mean the underlying `rag-cli index` subprocess was killed — the first
or second attempt most likely kept running to completion server-side while I, having no way to
distinguish "still running" from "failed," retried. That earlier run's own hash-check would have
already indexed `MinerU__1418.md`, `MinerU__2262.md`, `MinerU__826.md`, and `curl_cffi__74.md`
(alphabetically/discovery-order earlier) by the time the run I actually watched complete started,
leaving it only the remaining 4. I checked `status` (`Lock: FREE`) before the final attempt but
not between the first two — that gap is the process lapse. Not confirmed as fact, since I have no
direct visibility into a background process I didn't watch, but it is the explanation the
evidence supports, and I am not asserting a parallel session where the numbers are just as
consistent with my own overlap.

**After reindex:** total 4,846 chunks (**-214**). Per file: `MinerU__1418.md`=1,
`MinerU__2262.md`=5, `MinerU__826.md`=9, `curl_cffi__74.md`=44, `ghostty__2210.md`=55,
`pyobjc__175.md`=13, `pyobjc__176.md`=10, `pyobjc__34.md`=108. Two consecutive queries five
seconds apart returned identical numbers — the state had settled, nothing was still in flight.

## Verdict: stale chunks are deleted, not accumulated

Three independent pieces of evidence, all pointing the same way:

1. **Direct log evidence.** For 3 of the 4 files the completed run actually processed, it printed
   `Deleted N existing chunks for github_issues/<file>` immediately before indexing the
   replacement chunks — and N matches my own pre-reindex count exactly: `Deleted 43 ...
   pyobjc__175.md` (my count: 43), `Deleted 47 ... pyobjc__176.md` (47), `Deleted 154 ...
   pyobjc__34.md` (154). This is the indexer naming its own delete-then-insert behavior.
2. **Every one of the 8 files dropped**, and the size of each drop tracks that file's known
   gross-chars-removed share from the approved dry-run (e.g. `MinerU__2262.md` had ~94% of its
   chars removed and drops from 53→5 chunks; `curl_cffi__74.md` had ~6% removed and drops only
   47→44; `ghostty__2210.md` had ~1% removed and drops only 56→55). Accumulation would show flat
   or rising counts, not counts tracking the fraction of content actually cut.
3. **The collection total fell**, 5,060→4,846. Stale chunks piling up next to fresh ones can only
   ever raise or hold a collection's total steady; a fall of 214 is only possible if old rows for
   the changed documents were removed.

One loose end, stated rather than smoothed over: `ghostty__2210.md`'s processing in the run I
watched did not print a `Deleted N` line before `Indexed 55/55 chunks`, unlike the other three.
Its count still went cleanly 56→55 with no accumulation, so the *outcome* is unaffected — but I
cannot say with certainty whether the delete happened in the run I watched (silently) or in the
earlier, presumably-still-running attempt from immediately before it. Reported as an open
question, not resolved by assumption.

## Result

The corpus's first build-log strip is live: 8 files changed, 333,184 gross / 331,055 net chars
removed from the corpus (figures from the approved dry-run, unchanged by the apply since
detection was not re-run — the apply only executes what the dry-run already measured and
reported), 214 chunks net removed from the `github_issues` collection (5,060 → 4,846).
Backup preserved at `github_issues_PRE_BUILDLOG_STRIP_BACKUP_20260828_230949` as the sole
remaining record of the pre-strip corpus.

## Process lesson

Treat a client-side command timeout against a locking, stateful CLI as "unknown," not "failed."
Check `status` (lock state) before every retry, not just the last one, and prefer a longer
timeout up front over a retry loop when the operation is a single-writer, lock-guarded pipeline
step against shared state.
