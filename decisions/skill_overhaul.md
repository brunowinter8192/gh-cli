# Skill Overhaul (gh-cli-search SKILL.md)

## Status Quo (IST)

- Single-file skill `skills/gh-cli-search/SKILL.md`. No progressive loading, no `references/` split.
- Content contract: WHAT + HOW only — tool inventory, parameter tables, landmines (tool-failure-modes), procedure. NO rationale ("why X is so"); rationale lives in `decisions/OldThemes/`.
- Landmines are NOT rationale and stay: `repo:`-scoping consequences, release-collection wipe behavior, `search_code` CSV-skip, search-failure escalation.

## Evidenz

- Progressive loading (`references/` sub-files loaded on demand) rejected: forces the agent to recognize it must load more, spend an extra tool-call per sub-file, and carry an incomplete mental model until load — net MORE context for a LESS complete skill; the 11-tool surface has no "almost-never-needed" sub-file. One file loads / is current / can be audited. → `decisions/OldThemes/skill_overhaul/one_file_principle_2026-05-30.md`.
- Why-removal audit: slimming passes 580 → 457 → 345 → 309 lines; big design rationales externalized to `decisions/OldThemes/`; only pure-rationale trailing clauses cut, the rules themselves kept. → `decisions/OldThemes/skill_overhaul/why_removal_2026-06-13.md`.
