# SKILL.md Why-Removal — 2026-06-13

Principle reaffirmed: a skill states WHAT + HOW (tools, parameters, landmines, procedure) — NO rationale ("why X is so the way it is"). Rationale lives in `decisions/OldThemes/`. Tool-failure-modes (landmines) are NOT rationale and stay.

## Audit result

`skills/gh-cli-search/SKILL.md` (309 lines) was already largely why-free after the two prior slimming passes (580 → 457 → 345 → 309). Big design rationales had been externalized to `decisions/OldThemes/` (e.g. `search_code_compaction.md`, `release_indexing/redesign.md`). Only three pure-rationale fragments remained.

## Cuts

| Location | Removed fragment | Type |
|---|---|---|
| Two Access Patterns | "A few broad vector searches replace many fine-grained tool-calls." | efficiency rationale (HOW stands above it) |
| When to Stop → research task | "— alternatives matter" | begründung appended to the 3-query rule |
| When to Stop → research task | "— one result is not a comparison, it's a starting point" | begründung appended to do-not-stop |

The rules themselves ("Minimum 3 distinct queries before stopping", "Do NOT stop at first match") stay — only the trailing why was cut.

## Kept (landmines + procedure, NOT why)

- Gotchas, `repo:`-scoping consequences, release-collection wipe behavior, `search_code` CSV-skip, Search-Failure-Escalation — concrete tool-failure-modes (landmines), retained per the established skill rule.
- GOOD/BAD `search_repos` vs `search_code` examples and Iterative Refinement — procedure (the core HOW of a search skill), not rationale.
