# One-File Skill Principle + Slimming Cut-Log

## Decision: One-File Skill — Progressive Loading REJECTED

**Context:** During skill architecture review, a `references/` split was considered — entry file with core rules + separate sub-files loaded on demand (e.g., `references/parameter_tables.md`, `references/query_engineering.md`).

**Decision:** Single-file skill, no progressive loading. The deferred progressive-loading idea (formerly tracked as Bead github-3cl) is superseded.

**Rationale — why progressive loading loses:**

Progressive loading forces the agent to:
1. **Recognize** it must load more context — requires a meta-rule in the entry file ("load X when doing Y")
2. **Spend an extra tool-call** per sub-file loaded — tool-call cost is non-trivial when the skill is used for fast lookup
3. **Carry an incomplete mental model** until the sub-file loads — the agent may draw wrong conclusions or spin in a "what do I need to load next?" loop

Net result: more total context consumed for a *less complete* skill at execution time. The only saving is in the subset of sessions where some sub-files are genuinely never needed — but the github-search skill has 11 tools that all see regular use; there is no "almost-never-needed" sub-file that saves meaningful context.

**Simplicity principle:** one file loads, one file is current, one file can be audited. When the entry file is complete and self-contained, the agent is fully informed from the first invocation. The expensive failure mode is under-information (agent guesses wrong, wastes tool-calls, misses tools), not over-explanation.

**Consequence for future changes:** adding content to the skill = one file to edit. No sync between entry file and sub-files, no risk of a sub-file diverging from the entry file's assumptions.

---

## Slimming Cut-Log — 2026-05-30

Skill reduced from 580 → ~457 lines. Every cut is either pure duplication or foreign-domain bleed. No tool information removed.

### Governing principle

Two permitted cut types only:
- **Duplication** — the same information stated 2–3×. Removing it loses zero information.
- **Foreign-domain bleed** — instructions copied from a specific private data-verification / ML-prediction repo. This content does NOT apply to general public GitHub repos and actively misleads agents working in general contexts.

NEVER cut legitimate tool information. Parameter Reference tables, all 11 tool descriptions, example calls: untouched.

### CUT 1 — Tools by Category (38 lines removed)

Section contained five per-category tables (Discovery / Repository Exploration / Content Search / RAG-Semantic / Releases), each mapping tool name → one-sentence purpose. Pure duplication: Quick Reference (all 11 tools with example calls) + Parameter Reference (full param tables per tool) already cover this. Zero unique information in the tables.

### CUT 2 — search_repos 3-word limit: 3 occurrences → 1

The same rule ("max 2-3 words, API returns 0 for 4+ word queries") appeared in:
- Tool Selection section (one-line bullet)
- Dedicated NON-NEGOTIABLE block in Search Strategy (WRONG/RIGHT examples)
- Known Limitations (`search_repos — query length limit` sub-section)

Consolidation: NON-NEGOTIABLE block kept (most complete version, with WRONG/RIGHT examples). Before removing the Known Limitations entry, its unique sub-point ("server auto-truncates to 3 words with CLI warning") was folded into the NON-NEGOTIABLE block. One-line Tool Selection bullet removed (covered by the NON-NEGOTIABLE block). Known Limitations entry removed.

### CUT 3 — Merge Query Engineering sections (6 lines saved)

`## Query Engineering (index_issues)` and `## Query Engineering (index_discussions)` were near-identical. Shared rules (MAX 3 keywords, distinctive-first, 3→2→1 fallback, re-run = re-index) stated twice word-for-word. Merged into `## Query Engineering (index_issues / index_discussions)`: shared rules once, discussion-specific deltas (`repo:` injection automatic, accepted-answer threading) in a clearly labelled `**index_discussions only:**` block. Both RAG example code blocks preserved.

### CUT 4 — Guidelines section (30 lines removed)

Three sub-points, all foreign-domain bleed:
- **DOCS first** — duplicate of Navigation Rule 1 (already present)
- **Thoroughness over efficiency** — framed for a data-verification repo ("summary/comparison files", "read even if not explicitly asked"); wrong default for general public repos where reading blind wastes API quota
- **DATA, not plans** — used `FILE/VALUE/EVIDENCE` output format, `mean_mre;0.2173...` handoff example, `path/to/file.csv` artifacts — 100% data-verification task framing
- Four trailing bullets (iterate / chain / be specific / be honest) — covered by When to Stop, Tool Chaining Workflows, Repo-Scoped Search respectively

### CUT 5 — Report Format + Output Requirements: data-verification variants (35 lines removed)

**Report Format:** Removed `### For Data Verification` format block (`FILE/LINES/VALUE/EVIDENCE/VERDICT blocks` code example with `get_repo_tree(...) → found X directories` Search Process template). Edited "Right:" example to remove the `FILE: / VALUE: / EVIDENCE: blocks` reference — that's data-verification-specific output format, not a general GitHub search output. Kept: `### For Repo Discovery` format block.

**Output Requirements:** Removed intro (`"Every finding MUST include FILE path + concrete evidence"` — the "caller who will verify your findings" framing is data-verification specific), and the full `### Data Verification Output` section (`FILE: Prediction_Methods/Hybrid_1/Datasets/Baseline_SVM/approach_3/patterns_filtered.csv`, `LINES: 74 total (line 1 = header → 73 data rows)`, `VERDICT: MISMATCH (expected 72, found 73)`). Kept: `### Repo Discovery Output` (owner/repo format, key file paths, Good/Bad examples with `qdrant/mcp-server-qdrant`).

### CUT 6 — Known Limitations: "Searching for Values in Data Files" (6 lines removed)

Sub-section explained that percentages stored as decimals (6.74% → 0.06741992) cause `search_code` to return 0 results, and recommended `grep_repo` on CSV files by column name. This is a data-verification-specific search pattern for private ML datasets, irrelevant to general GitHub repos. Removed.

Retained three operational tool-behavior bullets: `get_repo_tree` truncation → use `path` param; `search_code` skips CSV/data files → use `grep_repo`; `grep_repo` min 20 files enforcement.

### CUT 7 — Foreign example strings in Navigation Rules + Path Integrity (line edits)

Replaced domain-specific example strings with GitHub-general equivalents:
- `multiple subdirectories like \`approach_1/\` through \`approach_4/\`, different versions of the same data` → `multiple subdirectories, different versions`
- `get_repo_tree(pattern="*Q8*", path="Predictions/")` → `get_repo_tree(pattern="*v2*", path="docs/")`
- `grep_repo(pattern="13408", file_pattern="*.md")` → `grep_repo(pattern="def.*Handler", file_pattern="*.py")`
- `Baseline_SVM/approach_3/` → `src/server/handlers/`
- `Datasets/approach_3/` ... `Datasets/Baseline_SVM/approach_3/` → `src/handlers/` ... `src/server/handlers/`

The underlying rules (DOCS-first, ambiguous-matches, path-integrity 404 rule, pre-call check, filename-search-before-content-search) are preserved unchanged.

---

## Slimming Cut-Log — Pass 2 (output/navigation overhead) — 2026-05-30

Skill reduced from 459 → ~345 lines. Governing principle: a skill describes its TOOLS (capabilities, parameters, landmines). Output templates and navigation discipline are either the caller's responsibility or generic agent competence — they do not belong in tool documentation. EXCEPTION: any rule that describes a concrete tool failure mode (wrong arg type → error, retry pattern → truncation, search order → silent misses) is a tool landmine and stays, extracted into `## Gotchas`.

### CUT A — `## Navigation Rules` (60 lines)

Six numbered rules (DOCS-first, ambiguous-matches, check-all, search-mode, filename-before-content, session-context) + three subsections (Truncation Handling, Reading Priority, Result Limits). These are general research discipline, not github-tool behavior. An agent that doesn't know to check all candidates before reporting isn't missing tool knowledge; it's missing general reasoning skill.

**Landmines extracted before removal:**
- `### Truncation Handling` → Gotcha 2 (tool behavior: truncation warning means narrow scope, specific API pattern `get_repo_tree(path=<dir>, depth=1)`)
- Bullet 5 (filename before content search) → Gotcha 3 (tool constraint: `grep_repo` `max_files` cap silently misses files on large repos)

### CUT B — `## Report Format` (19 lines)

"End with a structured report, not narration" + `### For Repo Discovery` output template. Generic agent output discipline, not a tool capability or failure mode. Zero tool-specific information.

### CUT C — `## Output Requirements` + `### Repo Discovery Output` (26 lines)

Cosmetic output format for repo discovery results (`owner/repo`, Key Files, Good/Bad example with `qdrant/mcp-server-qdrant`). Caller decides output format; the skill's job is to get the data. After removing `### Repo Discovery Output`, the `## Output Requirements` header was empty → also removed.

### CUT D — `## Output Hygiene` (18 lines)

Three blocks: "NEVER include local paths in output" (cosmetic output rule), "ONLY GitHub references" (cosmetic), "NEVER use local paths as tool parameters" (tool landmine). First two are output cosmetics. Third is a real tool failure mode.

**Landmine extracted before removal:**
- `**NEVER use local paths as tool parameters**` → Gotcha 1 (tool behavior: `get_file_content`/`grep_file`/`grep_repo` require repo-relative `path`; CC tool-result files at `/Users/.../.claude/projects/.../tool-results/...` cause immediate validation errors)

### ADD — `## Gotchas` section (9 lines)

Three tool-landmine bullets, placed after `## Regex Patterns` (groups the two tool-landmine sections near the top):

1. **Local paths as tool params → validation error** — `get_file_content`, `grep_file`, `grep_repo` take repo-relative path only. CC tool-result local paths → guaranteed validation error.
2. **Truncation warning → narrow scope, don't retry** — use `get_repo_tree(path="<dir>", depth=1)` + `grep_repo(path=<subdir>)`. Retrying same broad scope reproduces the truncation.
3. **Filename pattern before content search** — `get_repo_tree(pattern="*keyword*")` locates files in one call; `grep_repo` `max_files` cap silently misses files on large repos.
