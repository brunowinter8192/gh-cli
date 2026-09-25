# dev/tool_design/

## Role
Smoke tests for individual tool-design decisions in `src/github/` (one script per design question). Backs `process-docs/tool_design/`.

## Public Interface
No package `__init__` — each script is a standalone, manually-run dev entry point.

## Flow
1. Run the script directly (no arguments).
2. `probe_large_file.py` drives `cli.py` as a subprocess per tier/case; `test_strict_access.py` runs offline strands in parallel processes.
3. Prints a pass/fail summary and writes a report MD to `md/`.

## Modules

### probe_large_file.py (130 LOC)

**Purpose:** Smoke test for `get_file_content`'s size-tier dispatch — CLI subprocess calls, no direct `src.` import.
**Reads:** live GitHub repos via `cli.py get_file_content` subprocess (tiers 1/2); a fake response dict via inline `python -c` subprocess (tier 3).
**Writes:** report MD to `md/probe_large_file_<timestamp>.md`; prints result summary + report path; non-zero exit on any failure.
**Called by:** run manually (dev entry point).
**Calls out:** none.

---

### test_strict_access.py (227 LOC)

**Purpose:** Offline check that the strict-access rework keeps observed payload shapes working (null repo, null language, no answer, nothing to index, env-only token).
**Reads:** nothing external; each strand runs in its own process with a temporary HOME and stubbed calls.
**Writes:** `md/test_strict_access.md` (full runs only); non-zero exit on any failed strand.
**Called by:** manual run only.
**Calls out:** none.

---

## State
None — each run is stateless; tier 2's downloaded file lands in `/tmp` as a side effect of exercising the tool under test, not script state.
