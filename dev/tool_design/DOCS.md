# dev/tool_design/

## Role
Smoke tests for individual tool-design decisions in `src/github/` (one script per design question). Backs `process-docs/tool_design/`.

## Modules

### probe_large_file.py (115 LOC)

**Purpose:** Smoke test for `get_file_content`'s three size-tier dispatch (<=1 MB inline, 1-100 MB stream-to-`/tmp`, >100 MB error) — CLI subprocess calls, no direct `src.` import.
**Reads:** live GitHub repos via `cli.py get_file_content` subprocess (Tier 1/2); `format_toolarge_response` via inline `python -c` subprocess with a fake response dict (Tier 3).
**Writes:** report MD to `md/probe_large_file_<timestamp>.md`; prints result summary + report path to stdout; exit code 1 on any failure.
**Called by:** run manually (dev entry point).
**Calls out:** stdlib (`subprocess`, `os`, `sys`) only.
