# Search-Strategy Fallback — grep_repo false-negatives + escalation (2026-05-30)

## Problem

`grep_repo` can return "No matches" even when the pattern DOES exist in the repo — a silent false negative. Concluding "not present" from a single tool's empty result nearly led to a wrong research conclusion (that DockDoor had no space-move implementation).

## Case (2026-05-30)

Searching `ejbills/DockDoor` for the bridged space-move implementation (`SLSMoveWindowsToManagedSpace` / `SLSBridgedMoveWindowsToManagedSpaceOperation`):

| Tool | Call | Result |
|---|---|---|
| `grep_repo` (1st) | `ManagedSpace\|MoveWindows\|toSpace...` `*.swift` `max_files=25` | No matches (only 25/50 files searched — cap) |
| `grep_repo` (2nd) | same pattern, `max_files=50` | **No matches** (50/50 searched) |
| `search_code` | `ManagedSpace repo:ejbills/DockDoor` | **6 matches** → `DockDoor/Utilities/PrivateApis.swift` |
| `get_repo_tree` | `--pattern "*.swift"` filtered for api/space files | located adjacent files |

`grep_repo` searched all 50 matching files and STILL missed the hit that `search_code` returned immediately. The file (`PrivateApis.swift`) contained both searched symbols verbatim.

## Escalation strategy (codified in SKILL.md § Search-Failure Escalation)

On ANY 0 / "No matches":
1. `grep_repo` empty → `search_code "<term> repo:owner/repo"` (different index).
2. `search_code` empty → `get_repo_tree(pattern="*<keyword>*")` to find the file by NAME, then `get_file_content` / `grep_file` on the exact path.
3. Vary the term itself (synonym, shorter substring, casing) — never re-run the identical term in the identical tool.

Two different tools silent = evidence of absence. One tool silent = switch tools, don't conclude.

## Root cause (hypothesis, undiagnosed)

`grep_repo` likely fetches a bounded/default-branch file set or applies server-side content filtering that can miss files which `search_code`'s pre-built GitHub code index covers. Not fully diagnosed — the practical mitigation is the escalation chain above, not a grep_repo fix.
