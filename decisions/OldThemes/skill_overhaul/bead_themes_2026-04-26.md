# Skill Beads — Consolidation (2026-04-26)

> ⚠️ **STALENESS BANNER**
> These beads were written 2026-04-26 against a **21-tool** surface.
> Prod is now **11 tools** (as of 2026-05-30, after the `index_discussions` merge).
> Proposals referencing deleted tools are explicitly marked below.
>
> Deleted tools (files removed from `src/github/`): `search_items`, `list_commits`, `compare_commits`.
> Deregistered as subcommands (files kept, internal): `get_issue`, `get_issue_comments` → internal helpers of `index_issues`; `get_discussion` → internal helper of `index_discussions`.
> Deleted subcommands + files: `search_discussions`, `list_discussions`.
>
> **github-6vg** is most affected — its domain table is based entirely on the old surface.

---

## Theme 1 — Progressive Loading: SKILL.md → references/ (Bead github-3cl)

**Problem:** `SKILL.md` is 656 lines flat. On every skill activation Claude loads everything — even when the task is just a `search_repos` lookup. Parameter reference (~250 lines) and output-format rules (~80 lines) are not task-relevant for simple lookups.

**Model:** `automazeio/ccpm` (5-phase architecture):
- `SKILL.md` (~80 lines) — tool inventory, quick reference, pointer to `references/`
- `references/search-strategy.md`, `references/navigation.md`, `references/output-format.md`, `references/tool-reference.md`, `references/limitations.md`
- URL: https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md

**Proposal:** split into:
- `SKILL.md` (~80 lines) — tool inventory, quick reference, pointer to `references/`
- `references/search-strategy.md` — tool selection, iterative refinement, qualifiers
- `references/navigation.md` — DOCS-first, ambiguous-matches, search-mode rules
- `references/output-format.md` — FILE/EVIDENCE/VERDICT, output hygiene
- `references/tool-reference.md` — complete parameter tables per tool
- `references/limitations.md` — truncation, search_code data files, query limits

**Verification:** skill activation loads only SKILL.md (shorter); on a concrete task the matching references/ file is referenced explicitly; token saving per activation measurable.

**Staleness note:** the tool count changed from 18 to 11. The split stays reasonable, but the "18 tools = 250 lines parameter reference" argument is weaker — 11 tools = an estimated 150 lines. Decision still appropriate, magnitude smaller than assumed.

**Status:** DEFERRED — prod sync has priority.

---

## Theme 2 — Sharpen the description field (Bead github-4xx)

**Problem:** the current SKILL.md frontmatter has **no `description:` field** (empty — only `name: github-search`). Claude decides auto-activation based on the `description` field; if it is missing, the skill activates too randomly.

(Bead state: the bead describes a state with `description: See ~/.claude/shared-rules/global/cli-skills.md` — this line no longer exists in the current file. That does not shrink the problem, it grows it.)

**Model:** `automazeio/ccpm` — ~600-character description with: (1) concrete trigger sentences, (2) explicit negative list, (3) synonyms.

**Proposal (from bead, adapted for 11-tool prod):**
```yaml
description: "GitHub remote research via gh-cli. Use when asked to find repos/projects,
  read remote files, search code patterns, browse issues/discussions, or check releases
  on GitHub. Do NOT use for: editing local files, running local git commands, searching
  local code (use Grep/Glob instead), or operations on the user's own GitHub account."
```

Build in trigger phrases: "finde repos für X", "zeig mir wie X in Y implementiert ist", "was sind bekannte issues in Z", "index discussions von W für RAG". Negative list: local, `git commit`, `git push`, PR operations on own repo.

**Verification:** description field updated; plugin-sync run; test sessions: skill activates on trigger phrases, NOT on local operations.

**Status:** NOW (Stage B scope) — low effort, high clarity gain, no dependencies.

---

## Theme 3 — Domain-split architecture: N skills instead of 1 (Bead github-6vg)

**Problem:** one monolithic `github-search` skill with all tools across all domains. On activation everything is loaded.

**Model:** `github/github-mcp-server` — 14 toolsets (repos, issues, pull_requests, discussions, …), enable/disable at server start via flags. The agent loads only the tools it needs.
URLs: https://github.com/github/github-mcp-server/blob/main/pkg/github/tools.go, https://github.com/github/github-mcp-server/blob/main/docs/toolsets-and-icons.md

**Original proposal (5 focused skills):**

| Skill | Tools (original, 2026-04-26) |
|---|---|
| `github-discovery` | search_repos, get_repo, search_code |
| `github-content` | get_repo_tree, get_file_content, grep_file, grep_repo |
| `github-issues-prs` | ~~search_items~~, ~~get_issue~~, ~~get_issue_comments~~, ~~list_repo_prs~~, ~~get_pr~~, ~~get_pr_files~~ |
| `github-discussions` | ~~search_discussions~~, ~~list_discussions~~, ~~get_discussion~~ |
| `github-history` | ~~list_commits~~, ~~compare_commits~~, list_releases, get_release |

> ⚠️ **Heavily outdated.** Struck-through tools are deleted or internal. The proposal in its original form is no longer implementable.

**Updated state (11 tools, after index_discussions):**

| Skill | Tools (prod 2026-05-30) |
|---|---|
| `github-discovery` | search_repos, get_repo, search_code |
| `github-content` | get_repo_tree, get_file_content, grep_file, grep_repo |
| `github-rag` | index_issues, index_discussions |
| `github-releases` | list_releases, get_release |

Trade-offs unchanged: PRO = smaller SKILL.md per skill, clearer auto-activation. CON = tool-chaining across domains (e.g. search_code → grep_repo → index_issues) more complicated; 4 plugin-source files instead of 1.

**Status:** DEFERRED — a multi-skill architecture is a decision of its own magnitude, NOT implementable in passing. Prod sync first. Open question: can Claude have multiple skills active at once? (still unresolved).

---

## Theme 4 — allowed-tools: Bash frontmatter (Bead github-chm)

**Problem:** no `allowed-tools` field in the frontmatter. With an active skill the agent could theoretically apply Read/Edit/Glob to local files too — which for `github-search` is never sensible (we read GitHub remote, not local).

**Model:** `myuon/agent-skills` (`skills/gh/SKILL.md`):
```yaml
allowed-tools: Bash
```
URL: https://github.com/myuon/agent-skills/blob/main/skills/gh/SKILL.md

**Proposal:** extend the frontmatter with `allowed-tools: Bash`.

**Caveat:** first check whether `allowed-tools: Bash` collides with the workflow (e.g. if the agent would need to read local configs in between). If yes: `allowed-tools: Bash, Read` or similar. Currently: gh-cli returns everything via stdout; no Read/Edit on local files needed during GitHub research.

**Verification:** frontmatter extended; plugin-sync run; in test session: skill active → Read tool call blocked.

**Status:** NOW (Stage B scope) — 1-line edit, no risk when no local-read need exists.

---

## Theme 5 — Pre-baked scripts for discovery patterns (Bead github-i1v)

**Problem:** recurring research patterns require 2-4 CLI calls + manual sorting/filtering. Tool-call-intensive, context-budget-heavy.

**Models:**
- `majiayu000/claude-skill-registry` — `scripts/gh_profile.sh`, `scripts/gh_repos.sh` with `--limit` flag. URL: https://github.com/majiayu000/claude-skill-registry/blob/main/skills/development/github-info/SKILL.md
- `automazeio/ccpm` — Script-First rule: for deterministic read-and-report operations ALWAYS a script instead of a manual tool sequence. URL: https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md

**Proposal:** `skills/github-search/scripts/` with:
- `top_trending.sh <query> [--limit N]` — search_repos + sort=stars + take N
- `repo_overview.sh <owner/repo>` — get_repo + get_repo_tree depth=1 + README
- ~~`find_issues.sh <owner/repo> --label <label>`~~ — search_items removed
- ~~`find_prs_touching.sh <owner/repo> <file_path>`~~ — PR tools removed
- ~~`compare_releases.sh <owner/repo> <tag1> <tag2>`~~ — compare_commits removed

> ⚠️ Three of the 5 script proposals reference deleted tools. `top_trending.sh` and `repo_overview.sh` are still implementable. Possibly add: `index_and_search.sh <query> <owner/repo>` as a wrapper for `index_discussions` + `rag-cli search_hybrid`.

**Status:** DEFERRED — useful, but downstream. Prod sync first, then scripts as an addition.
