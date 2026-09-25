# gh-cli/ (root)

## Role
Argparse entry point for the GitHub Research CLI. `cli.py` registers one subcommand per tool and routes each to a `<tool>_workflow()` in `src/github/`. Touch this file only to add/remove a subcommand or change dispatch/error-handling; tool logic lives in `src/github/`, not here.

## Public Interface
No package `__init__` — `cli.py` is a standalone script. Entry path: `~/.local/bin/gh-cli` wrapper → `python cli.py <cmd> [args]`; also loaded by Claude Code via the `gh-cli-search` skill through Bash.

## Flow
1. `gh-cli <cmd> [args]` → wrapper runs `python cli.py <cmd> [args]`.
2. Args are parsed, then routed to the matching `<tool>_workflow`.
3. Workflow returns `list[TextContent]`; the entry point prints `result[0].text` to stdout.
4. `BrokenPipeError` is swallowed silently; any other `Exception` → `Error: {e}` to stderr + non-zero exit.

## Modules

### cli.py (306 LOC)

**Purpose:** Argparse CLI entry — build parser (one subparser per tool), dispatch to workflows, central error handling.
**Reads:** `sys.argv` (argparse); prepends its own dir to `sys.path` at import so `src.github.*` resolves from any cwd.
**Writes:** `result[0].text` to stdout; `Error: {e}` to stderr on failure; non-zero exit on failure.
**Called by:** `~/.local/bin/gh-cli` wrapper; `gh-cli-search` skill via Bash.
**Calls out:** none.

## State
None — no module-level mutable state owned here; nothing persists between invocations.
