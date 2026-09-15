# Milestone 1 — Function-Level Cohesion (2026-09-16)

Process record for the function-level LOC-reduction milestone: `cli.py::_build_parser`,
`cli.py::_dispatch`, `src/github/discussion_cleaning.py::strip_noise`,
`src/github/index_issues.py::index_issues_workflow`, and the two dev report writers
(`dev/content_cleaning/02_strip_validation.py::write_report`,
`dev/content_cleaning/08_audit_debug_stream.py::write_report`). No module split (all five files
stayed under 400 LOC); this was function-only extraction, no logic change.

## What changed, per file

- `cli.py` — `_build_parser` split into 14 `_add_<cmd>_parser(sub)` helpers, called from
  `_build_parser` in the exact original subcommand order (argparse renders `--help` in insertion
  order, so order preservation is load-bearing, not cosmetic — kept identical on purpose).
  `_dispatch` split into 14 `_dispatch_<cmd>(args)` handlers plus a `cmd -> handler` dict lookup in
  `_dispatch` itself. Every pre-existing `# ── <cmd> ──` banner comment moved with its code block,
  none added or removed.
- `src/github/discussion_cleaning.py::strip_noise` — the three skippable-block cases (DOSU_FOOTER,
  DOSU_GREETING, ISSUE_TEMPLATE_CHECKLIST) extracted into `_try_skip_dosu_footer`,
  `_try_skip_dosu_greeting`, `_try_skip_issue_template_checklist`, each `(lines, i, ...) -> int |
  None`. Main loop tries them in the original source order, first non-`None` wins, then falls
  through to the unchanged badge/footer-text/markerless-greeting/inline-sub tail.
- `src/github/index_issues.py::index_issues_workflow` — extracted `search_issues_with_fallback`
  (the 3→2→1 keyword loop), `write_one_issue_md` (fetch+raw-log+strip+build+write for one issue),
  `write_issue_mds` (loop over `write_one_issue_md`), `build_index_summary` (fallback-note +
  summary string). The orchestrator now only guards (empty query, zero results) and calls.
- Both dev `write_report` functions split into one `_render_<section>(...)` helper per report
  section, each returning a list of lines; `write_report` concatenates in the original order.

## LOC after (function bodies, via `ast` end_lineno - lineno + 1)

None of the six target functions or any newly extracted helper reaches 50 LOC. Largest post-split:
`index_issues_workflow` 23, `strip_noise` (discussion_cleaning) 40, `_dispatch` ~16,
`_build_parser` ~20, `08_audit_debug_stream.py::write_report` 13, `02_strip_validation.py::write_report` 7.
Two functions outside this milestone's target list sit close to the ceiling and are worth a future
agent's attention: `index_issues.py::strip_comments_noise` (47 LOC) and
`02_strip_validation.py::strip_noise`/`spot_check` (46/33) — none of these were in scope here, left
untouched per the milestone boundary.

## Verification method (why byte-identical / behavior-identical claims are trustworthy)

- **`cli.py` `--help`**: captured `python cli.py --help` and `python cli.py <cmd> --help` for all
  14 subcommands before and after, `diff -r` the two directories — empty diff. This is close to
  tautological given `NoHelpParser` intercepts all help/usage/error output with a fixed
  `HELP_TEXT` string regardless of the argparse tree shape, but the diff was still run and is
  attached as proof, not assumed.
- **`discussion_cleaning.strip_noise`**: loaded the pre-edit and post-edit file as two independent
  module objects via `importlib.util.spec_from_file_location` + `module_from_spec` +
  `spec.loader.exec_module`, ran both against all 131 real files in the local
  `.../rag-cli/data/documents/github_discussions/` corpus, diffed output strings — 0 mismatches.
  **Pitfall hit**: `spec_from_file_location` returns `None` (not an error — silently `None`,
  raising `AttributeError: 'NoneType' object has no attribute 'loader'` one line later) when the
  source path's extension isn't `.py` — a `.orig` backup copy failed silently until renamed to
  `.py`. If a future agent uses this load-two-module-versions pattern, keep the backup file's
  extension `.py`, not `.orig`/`.bak`/anything else.
- **`index_issues_workflow`**: no network/rag-cli available in this sandbox, so this one is proven
  differently: loaded both versions the same way, monkeypatched every dependency
  (`search_raw`, `get_issue_workflow`, `get_issue_comments_workflow`, `log_raw_issue`,
  `strip_noise`, `strip_generic_noise`, `strip_build_logs`, `strip_comments_noise`,
  `build_issue_md`, `run_index`, `get_collection_stats`) to fakes that both compute a deterministic
  result AND append a call-record tuple to a shared list, then ran both workflow versions with
  identical arguments (including a 3→2→1 fallback-triggering case, the empty-query guard, and the
  zero-results guard) and asserted the call-record lists are equal (they are — exact same calls,
  exact same order, exact same arguments) and the returned text and written MD files are equal
  (they are). This proves the extraction reproduces the exact same sequence of external calls with
  the exact same arguments, not just a plausible-looking one.
- **Dev report writers**: `datetime.now` is the only non-deterministic input, so both loaded
  modules had `mod.datetime` monkeypatched to a fixed-value subclass before calling `write_report`
  with identical synthetic fixtures; outputs compared with `==` (not eyeballed) — byte-identical
  for both `02_strip_validation.py` and `08_audit_debug_stream.py`. Also ran both scripts
  end-to-end against the real corpora post-refactor to confirm no runtime error; the generated
  report files from that smoke run were deleted afterward (no lasting value — same numbers as the
  pre-refactor run, not a new measurement, so nothing worth keeping in `dev/content_cleaning/md/`).

## Note recorded, not acted on (per instruction)

`dev/content_cleaning/02_strip_validation.py` and `03_reclean_discussions.py` each hold an
independent verbatim copy of `strip_noise` (+ `_bare`, `_is_badge_line`,
`_is_dosu_markerless_greeting`, `_is_dosu_footer_text_line`, and the four shared constants) — this
is the project's existing, documented convention (`block_dev_imports_src` hook forbids `from src.`
in `dev/`; see `src/github/DOCS.md` Gotchas and `dev/content_cleaning/DOCS.md` Gotchas). Diffed the
two copies directly (`FOOTER_LOOKAHEAD` through the end of `strip_noise`, byte comparison): **the
`strip_noise` function body and its four helpers are byte-identical between the two copies as of
2026-09-16.** The only differences between the two files in that region are copy-specific
surroundings unrelated to the noise-strip logic itself: `02` also carries `SPOT_CHECK_FILES`,
`SPOT_CHECK_PATTERNS`, and a `strip_discussion_noise` wrapper (needed for its validation role);
`03` does not (its role is a noise-only re-clean, deliberately not doing the discussion-format
pass — consistent with `dev/content_cleaning/DOCS.md`'s description of `03`). Neither copy was
touched by this milestone, and no unification was attempted — both stay exactly as found. A future
control-flow-focused pass is the right place to decide whether the two `strip_noise` copies (three,
counting `src/github/discussion_cleaning.py` itself) should ever be reduced to fewer independent
sources; this session did not evaluate that trade-off.

## Something worth knowing if you touch `cli.py` again

`_build_parser`'s subcommand order is not just readability — argparse's `--help` output lists
subcommands in the order `add_parser()` was called, so silently reordering the 14
`_add_<cmd>_parser(sub)` calls in `_build_parser` would produce a *different*, not just
differently-organized, `--help` output. Keep the call order matching the original file's
subcommand order if you ever add/remove/reorder a subcommand.
