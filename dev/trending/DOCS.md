# dev/trending/

## Role
Offline test for the `trending` tool in `src/github/trending.py`, driven by saved HTML fixtures. Backs `process-docs/trending/`.

## Public Interface
No package `__init__` — `test_trending.py` is a standalone, manually-run script.

## Flow
1. Run `python dev/trending/test_trending.py` (no arguments, no network).
2. Script runs its independent strands in parallel threads (strand names as CLI args run a subset); each is fail-fast, the others keep running.
3. Writes per-strand PASS/FAIL report to `md/test_trending.md`; prints PASS or FAIL lines, non-zero exit on any failure.

## Modules

### test_trending.py (134 LOC)

**Purpose:** Deterministic check of `parse_trending`, `format_trending` and the tripwires against trimmed live-page fixtures.
**Reads:** `fixtures/trending_weekly.html`, `fixtures/trending_developers.html`, `fixtures/trending_single_star.html`.
**Writes:** `md/test_trending.md` (full runs only); non-zero exit on assertion failure.
**Called by:** manual run only.
**Calls out:** none.

---

### probe_optional_fields.py (74 LOC)

**Purpose:** Live probe counting which optional trending fields are actually absent across a page sample; evidence for which defaults are observed.
**Reads:** live `github.com/trending` pages via `src.github.trending`.
**Writes:** `md/probe_optional_fields.md`; prints the report path.
**Called by:** manual run only.
**Calls out:** none.

---

## State
None.
