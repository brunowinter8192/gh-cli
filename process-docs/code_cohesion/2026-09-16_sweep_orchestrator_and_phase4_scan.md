# Refactor sweep, orchestrator record and the Phase 4 control-flow scan (2026-09-16)

Orchestrator half of an `iterative-dev-refactor` run over this whole project. Phases 1 to 3 were
executed and merged. Phase 4 was scanned and deliberately NOT acted on — the list at the bottom is
the handover.

The per-milestone worker entries are `milestone1_function_loc.md` and `milestone2_comment_purge.md`
in this same folder. This entry holds what only the orchestrator saw.

## Starting state, measured

39 Python modules, 5813 lines. Not one module was over the 400-LOC ceiling — this project was the
only one of the four in this sweep with zero oversized modules. Six functions sat at or above the
50-LOC ceiling, one of them at or above 100:

- `cli.py::_build_parser` 108 LOC, hard target
- `dev/content_cleaning/02_strip_validation.py::write_report` 62
- `src/github/discussion_cleaning.py::strip_noise` 60
- `dev/content_cleaning/08_audit_debug_stream.py::write_report` 57
- `cli.py::_dispatch` 54
- `src/github/index_issues.py::index_issues_workflow` 52

After Phase 1: zero functions at or above 50, largest at 40.

`_build_parser` was cut into one `_add_<cmd>_parser` helper per subcommand, fourteen of them, and
`_dispatch` into a name-to-handler dict with one `_dispatch_<cmd>` per subcommand. The argparse tree
shape is unchanged, which is what makes the `--help` output structurally identical rather than
merely identical-in-testing; it was still diffed for the top-level parser and all fourteen
subcommands, empty diff both before and after Phase 2.

## Phase 2, the comment purge, in numbers

652 hits across 37 files: 650 comments and 2 docstrings. This was by far the densest of the four
projects in the sweep, and four dev scripts carried between 46 and 88 comment lines each, nearly all
of it in single large header blocks recording detector-threshold derivations.

643 were deleted as already covered by the owning `DOCS.md` or by an existing process-docs entry,
and only 9 carried substance that existed nowhere else.

That ratio was checked, not taken on trust. The largest single block was the 88-line header of
`dev/content_cleaning/09_strip_debug_stream.py`, which recorded why `MIN_RUN_LINES` was raised from
2 to 3 and named the two corpus cases that forced it — `playwright__31950.md:236` with
`signal=SIGBUS` and `playwright__14689.md:75` with `signal=SIGTRAP`. Both cases, and the floor
decision, are carried verbatim by `process-docs/content_cleaning/debug_stream_detector_2026-09-05.md`
at lines 29 and 44 to 46. The deletion was honest.

Five `DOCS.md` were rewritten to the Role / Public Interface / Flow / Modules / State format, with
all 37 module headings cross-checked against the real `wc -l`.

## The one place where deleting a docstring would have changed behaviour

`dev/repo_exploration/01_probe_graphql_explore.py` passed its module docstring to argparse as
`description=__doc__`. Deleting the docstring would have silently emptied the `--help` description.
The text was preserved as a literal string argument instead, and `--help` was verified byte-identical.

This is the class of hazard to look for before any comment purge: `__doc__` read at runtime. Grep
for `__doc__` before deleting anything.

## Phase 3

Every `DOCS.md` was already under the 400-line split threshold, the largest at 265 lines, so no
directory needed splitting into unit subfolders. `docs-drift-check` reported zero findings in all
three categories on the first run, before and after the sweep.

## What the sweep deliberately did NOT do

`strip_noise` exists three times in this repository. The real one is
`src/github/discussion_cleaning.py`, whose only importer is `src/github/index_discussions.py`.
`dev/content_cleaning/02_strip_validation.py` and `dev/content_cleaning/03_reclean_discussions.py`
each hold an independent verbatim copy, because a hook in this project forbids dev scripts from
importing src. The copies were confirmed byte-identical to each other in the shared logic and left
untouched. Whether that hook rule should keep buying triplication is a control-flow question, not a
size question.

`_read_zshrc_token` exists twice, in `src/github/client.py` and `dev/repo_exploration/probe_client.py`,
for the same reason.

## Phase 4 candidate list, scanned and not classified

An AST pass over every `except` handler in the project, classified by what the handler does. Only
six handlers produce output and one only logs, which makes this the cleanest of the four projects in
the sweep by a wide margin. Two handlers re-raise or exit and are tripwires, which stay.

- `src/github/index_issues.py:279`, `src/github/index_discussions.py:190` and
  `src/github/index_releases.py:149`, all in a function named `get_collection_stats`, all
  `except Exception`.
- `src/github/client.py:32` and `dev/repo_exploration/probe_client.py:35`, both in
  `_read_zshrc_token`, both `except OSError`.
- `src/github/download_files.py:30` in `_download_paths`, `except Exception`.
- `src/github/raw_logging.py:46` in `log_raw_issue`, `except Exception`, log-only.

The `get_collection_stats` triple is the finding worth carrying forward. All three shell out to
`rag-cli list_collections`, regex the chunk count out of stdout, and differ only in which collection
name the regex matches — `index_releases.py` takes the collection as a parameter, the other two
hardcode `github_issues` and `github_discussions`. A fourth copy of the same helper, with the same
swallow-and-return handler, lives in the reddit-cli project at
`src/reddit/index_subreddits.py:212`. That is four copies of one helper across two repositories,
each independently swallowing whatever went wrong with the subprocess.

## Method notes for a successor

Main scanned, workers fixed. Every number above came from an AST walk run at orchestration level.

For a comment purge the strong check is AST equality, not behaviour sampling: parse each file before
and after, strip docstrings from both trees, compare the dumps. An identical tree means the compiled
bytecode cannot differ for any input. In this project 35 of 37 files were AST-identical; the two
exceptions were the `__doc__` case above and `cli.py`, where `main()` moved position to satisfy the
section-marker order. Both were disclosed by the worker before the diff was read, which is the
behaviour to expect.

Behaviour was additionally proven at corpus scale rather than on fixtures: `strip_noise` over all
131 real discussion files and `strip_generic_noise` and `strip_build_logs` over roughly 550 real
issue files, zero mismatches each. When a real corpus is on disk, use it.
