# gh-cli/ (root)

## Role
Argparse entry point for the GitHub Research CLI. `cli.py` registers 15 subcommands and routes each to a `<tool>_workflow()` in `src/github/`. Touch this file only to add/remove a subcommand or change dispatch/error-handling; tool logic lives in `src/github/`, not here.

## Public Interface
No package `__init__` — `cli.py` is a standalone script. Entry path: `~/.local/bin/gh-cli` wrapper → `python cli.py <cmd> [args]`; also loaded by Claude Code via the `gh-cli-search` skill through Bash.

## Flow
1. `gh-cli <cmd> [args]` → wrapper runs `python cli.py <cmd> [args]`.
2. `_build_parser()` parses args; `_dispatch()` routes to `<tool>_workflow(params)`.
3. Workflow returns `list[TextContent]`; `main()` prints `result[0].text` to stdout.
4. `BrokenPipeError` → devnull dup2 + exit 0; any other `Exception` → `Error: {e}` to stderr + exit 1.

## Modules

### cli.py (302 LOC)

**Purpose:** Argparse CLI entry — build parser (15 subparsers), dispatch to workflows, central error handling.
**Reads:** `sys.argv` (argparse); prepends its own dir to `sys.path` at import so `src.github.*` resolves from any cwd.
**Writes:** `result[0].text` to stdout; `Error: {e}` to stderr on failure; exit codes 0/1.
**Called by:** `~/.local/bin/gh-cli` wrapper; `gh-cli-search` skill via Bash.
**Calls out:** all 15 `<tool>_workflow` functions from `src.github.*`; stdlib `argparse`, `os`, `sys`.

## State
None — no module-level mutable state owned here; `main()` reads argv and dispatches, nothing persists between invocations.
