# dev/trending/

## Role
Offline test for the `trending` tool in `src/github/trending.py`, driven by saved HTML fixtures. Backs `process-docs/trending/`.

## Public Interface
No package `__init__` — `test_trending.py` is a standalone, manually-run script.

## Flow
1. Run `python dev/trending/test_trending.py` (no arguments, no network).
2. Script parses the fixtures in `fixtures/` and checks fields plus tripwire errors.
3. Prints PASS and writes the formatted output to `md/test_trending.md`.

## Modules

### test_trending.py (68 LOC)

**Purpose:** Deterministic check of `parse_trending`, `format_trending` and the tripwires against trimmed live-page fixtures.
**Reads:** `fixtures/trending_weekly.html`, `fixtures/trending_developers.html`.
**Writes:** `md/test_trending.md`; exit code 1 on assertion failure.
**Called by:** manual run only.
**Calls out:** `src.github.trending`.

---

## State
None.
