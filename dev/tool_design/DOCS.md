# dev/tool_design/

## Purpose

Extract real-world gh-cli usage from Monitor_CC proxy logs to inform tool-design decisions (which tools are actually called, with what arguments, what results). Feeds `decisions/tool_design.md`.

## Scripts

### extract_ghcli_calls.py (259 LOC)
**Purpose:** Stream `api_requests_*.jsonl` proxy logs, collect Bash `tool_use` blocks whose command contains `gh-cli`, deduplicate by `tool_use` id, pair with `tool_result` blocks, write one JSONL record per unique call.
**Usage:**
```
.venv/bin/python dev/tool_design/extract_ghcli_calls.py
.venv/bin/python dev/tool_design/extract_ghcli_calls.py --logs-dir /path/to/logs
.venv/bin/python dev/tool_design/extract_ghcli_calls.py --max-result-chars 2000
```
**Flags:** `--logs-dir PATH` (proxy-log dir); `--max-result-chars N` (truncate paired result text).
**Output:** JSONL data extract to the out path; extraction stats printed to stdout.
