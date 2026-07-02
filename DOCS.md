# gh-cli/ (root)

## Role
Argparse entry point for the GitHub Research CLI. `cli.py` registers 14 subcommands and routes each to a `<tool>_workflow()` in `src/github/`. Touch this file only to add/remove a subcommand or change dispatch/error-handling; tool logic lives in `src/github/`, not here.

## Public Interface
No package `__init__` — `cli.py` is a standalone script. Entry path: `~/.local/bin/gh-cli` wrapper → `python cli.py <cmd> [args]`; also loaded by Claude Code via the `gh-cli-search` skill through Bash.

## Flow
1. `gh-cli <cmd> [args]` → wrapper runs `python cli.py <cmd> [args]`.
2. `_build_parser()` parses args; `_dispatch()` routes to `<tool>_workflow(params)`.
3. Workflow returns `list[TextContent]`; `main()` prints `result[0].text` to stdout.
4. `BrokenPipeError` → devnull dup2 + exit 0; any other `Exception` → `Error: {e}` to stderr + exit 1.

## Modules

### cli.py (209 LOC)

**Purpose:** Argparse CLI entry — build parser (14 subparsers), dispatch to workflows, central error handling.
**Reads:** `sys.argv` (argparse); prepends its own dir to `sys.path` at import so `src.github.*` resolves from any cwd.
**Writes:** `result[0].text` to stdout; `Error: {e}` to stderr on failure; exit codes 0/1.
**Called by:** `~/.local/bin/gh-cli` wrapper; `gh-cli-search` skill via Bash.
**Calls out:** all 14 `<tool>_workflow` functions from `src.github.*`; stdlib `argparse`, `os`, `sys`.

## Gotchas
- `sys.path.insert(0, ...)` at line 6 runs before the `src.github.*` imports — required so the CLI works regardless of invocation cwd. Do not reorder.
- `BrokenPipeError` is caught first and swallowed (devnull dup2 + exit 0) so `gh-cli ... | head` stays clean; `SystemExit`/`KeyboardInterrupt` pass through unhandled.
