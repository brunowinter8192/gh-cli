# SKILL.md Prod Adaptation — Scope for Stage B

Rewrite plan: SKILL.md 18-tool state → 11-tool prod state (2026-05-30).
Reference truth: `cli.py` (11 subcommands), `src/github/DOCS.md`.

---

## 1. Staleness audit (line refs against the current SKILL.md, 657 lines)

### 1.1 Wrong tool count / dead-tool references

| Line(s) | Problem | Fix |
|---|---|---|
| L.15 | `"Quick Reference — All 18 Tools"` | → `"All 11 Tools"` |
| L.34 | `gh-cli search_items ...` | remove (tool deleted) |
| L.35–36 | `gh-cli get_issue ...` / `get_issue_comments ...` | remove (internal helpers, no subcommand) |
| L.40–43 | `search_discussions`, `list_discussions`, `get_discussion` quick-ref | remove (deleted/internal) |
| L.46–48 | `list_commits`, `compare_commits` quick-ref | remove (deleted) |
| L.59 | `"Discussions ... planned, not yet built"` | fix: `index_discussions` is built; releases stay CLI-direct (no RAG) |
| L.98–100 | Table Issues & PRs: `search_items`, `get_issue`, `get_issue_comments` | remove; section → "RAG-Semantic" with `index_issues` + `index_discussions` |
| L.104–109 | Table Discussions: `search_discussions`, `list_discussions`, `get_discussion` | remove |
| L.114–118 | Table Commits & Releases: `list_commits`, `compare_commits` | remove; section → "Releases" with `list_releases`, `get_release` only |
| L.204–207 | Issue Investigation Workflow: `search_items` step 1 | remove; section pointless without search_items → either remove entirely or rewrite as "via RAG" |
| L.226–230 | Discussion Research Workflow: `search_discussions`, `list_discussions`, `get_discussion` | replace fully (see §2.3) |
| L.234–238 | Commit History Workflow | remove `list_commits`/`compare_commits`; keep only the release workflow |
| L.358–370 | Parameter Reference: `search_items` | remove |
| L.371–377 | Parameter Reference: `get_issue` / `get_issue_comments` | remove (internal helpers — no CLI access) |
| L.394–419 | Parameter Reference: `search_discussions`, `list_discussions`, `get_discussion` | remove (`get_discussion` internal, no CLI) |
| L.421–439 | Parameter Reference: `list_commits`, `compare_commits` | remove |
| L.465 | Search Qualifiers: `repo:owner/repo ... search_items` | remove `search_items` from applies-to |
| L.538 | "For PR results from search_items --type pr" | remove (whole sentence) |

### 1.2 Missing: `index_discussions` completely absent

- Not in Quick Reference
- Not in Tools by Category
- No query-engineering section
- No parameter-reference entry
- No tool-chaining workflow
- Two Access Patterns (L.58–59): only `index_issues` mentioned

### 1.3 Frontmatter

Current:
```yaml
---
name: github-search
---
```
Missing: `description:` (no field present — skill auto-activation not steerable).
Missing: `allowed-tools:` (no field — no tool constraint active).

---

## 2. Target structure after rewrite (11 tools)

### 2.1 Frontmatter (new)

```yaml
---
name: github-search
description: "GitHub remote research via gh-cli. Use when asked to find repos/projects,
  read remote files, search code patterns, browse or index issues/discussions, or check
  releases on GitHub. Trigger phrases: 'finde repos für X', 'zeig mir wie X in Y
  implementiert ist', 'was sind bekannte issues in Z', 'index discussions von W'.
  Do NOT use for: editing local files, local git commands (commit/push/checkout),
  searching local code (use Grep/Glob), operations on the user's own GitHub account."
allowed-tools: Bash
---
```

### 2.2 Quick Reference (11 tools)

```bash
# Discovery
gh-cli search_repos "fastapi" --sort-by stars
gh-cli search_code "def workflow language:python repo:owner/repo"
gh-cli get_repo anthropics claude-code

# Repository Exploration
gh-cli get_repo_tree anthropics claude-code --path src --depth 2 --pattern "*.py"
gh-cli get_file_content anthropics claude-code README.md
gh-cli get_file_content anthropics claude-code src/main.py --offset 100 --limit 50
gh-cli get_file_content anthropics claude-code src/ --metadata-only

# Content Search
gh-cli grep_file anthropics claude-code src/main.py "def run" --context-lines 3
gh-cli grep_repo anthropics claude-code "class.*Tool" --file-pattern "*.py" --path src

# RAG Indexing (Issues + Discussions)
gh-cli index_issues "streaming" anthropics/claude-code --limit 30
gh-cli index_discussions "memory" gastownhall/beads --limit 30

# Releases
gh-cli list_releases anthropics claude-code --per-page 5
gh-cli get_release anthropics claude-code --tag v2.0.0
gh-cli get_release anthropics claude-code  # latest
```

### 2.3 Tools by Category (new)

**Discovery:** `search_repos`, `search_code`, `get_repo`
**Repository Exploration:** `get_repo_tree`, `get_file_content`
**Content Search:** `grep_file`, `grep_repo`
**RAG-Semantic (Issues):** `index_issues`
**RAG-Semantic (Discussions):** `index_discussions`
**Releases:** `list_releases`, `get_release`

### 2.4 Two Access Patterns (update)

- **Code & repo content → direct CLI.** `search_repos`, `search_code`, `get_repo`, `get_repo_tree`, `get_file_content`, `grep_file`, `grep_repo`, `list_releases`, `get_release`. Direct `gh-cli` calls.
- **Conversation/discussion layer → query-driven RAG indexing.** Issues: `index_issues "<kw>" <owner/repo>` → `rag-cli search_hybrid "<terms>" github_issues`. Discussions: `index_discussions "<kw>" <owner/repo>` → `rag-cli search_hybrid "<terms>" github_discussions`. A few broad vector searches replace many fine-grained tool-calls. Releases stay CLI-direct (exact-artifact lookup, not fuzzy retrieval).

(Remove "planned, not yet built".)

### 2.5 Query Engineering — index_discussions (NEW, mirrors index_issues)

```
## Query Engineering (index_discussions)
- MAX 3 keywords — same cap as index_issues; extra words dropped silently.
- Most distinctive keyword first — fallback loop 3→2→1 drops from the back.
- repo: injection automatic — index_discussions scopes to the target repo; no cross-repo search.
- After indexing, search via RAG:
    gh-cli index_discussions "memory" gastownhall/beads --limit 30
    rag-cli search_hybrid "memory tracking workflow" github_discussions
- Re-run = re-index — always overwrites MDs; index-dir skips unchanged content-hash.
- isAnswered threading: accepted answers appear in ### Accepted Answer block; duplicate
  in-list [ANSWER] tag is stripped automatically during indexing.
```

### 2.6 Tool Chaining — Discussion Research (NEW, replaces old 3-tool chain)

```
### Discussion Research
1. index_discussions "<1-3 kw>" owner/repo [--limit N]
   → fetches top-N discussions by relevance, strips noise, writes MDs to github_discussions/
2. rag-cli search_hybrid "<terms>" github_discussions
   → broad vector search across all indexed threads (replaces many get_discussion calls)
```

### 2.7 Tool Chaining — Issue Investigation (update)

Remove `search_items` step. The workflow now starts at `index_issues`:
```
### Issue Investigation
1. index_issues "<1-3 kw>" owner/repo [--limit 30]
2. rag-cli search_hybrid "<error or symptom terms>" github_issues
```

(The old `search_items → get_issue → get_issue_comments` chain is gone. The 3-step fine-grained lookup no longer has a CLI path; RAG replaces it.)

### 2.8 Parameter Reference — index_discussions (NEW)

| Parameter | Type | Default | Description |
|---|---|---|---|
| query | str | required | Search keywords (max 3; most distinctive first) |
| repo | str | required | Repository as owner/repo |
| --limit | int | 30 | Max discussions to fetch and index |

### 2.9 Commits & Releases section

Remove `list_commits` / `compare_commits` (deleted). Keep `list_releases` + `get_release` under the renamed section "Releases". Remove the "Commit History & Version Analysis" workflow; leave the "Release Lookup" workflow.

---

## 3. Scope cut for Stage B

### NOW (prod sync — Stage B)

| Item | Source | Change |
|---|---|---|
| 18→11 tool count | prod reality | quick-ref + all tables + section headers |
| 5 dead tools out | prod reality | all refs removed (see §1.1 audit) |
| `index_discussions` in | prod reality | QR + category table + query-eng section + chaining workflow + param ref |
| Two Access Patterns fix | prod reality | remove "not yet built"; add discussions; releases stay CLI-direct |
| `get_issue`/`get_issue_comments` demotion | prod reality | remove from user-facing param ref + tables (internal helpers, no subcommand) |
| Frontmatter `description:` | bead github-4xx | new field with trigger phrases + negative list |
| Frontmatter `allowed-tools: Bash` | bead github-chm | new field |
| Issue Investigation workflow | prod reality | `search_items` step removed |

### DEFERRED (not Stage B)

| Item | Source | Why deferred |
|---|---|---|
| Progressive loading: SKILL.md → references/ | bead github-3cl | architecture decision; SKILL.md is 11-tool-clean only after prod sync — then a split evaluation pays off |
| Domain split: N skills | bead github-6vg | own decision; multi-skill question (active simultaneously?) unresolved |
| Pre-baked scripts | bead github-i1v | downstream; prod-clean first, then scripts |

---

## 4. LOC estimate after rewrite

Removed: ~180 lines (5 dead tool blocks in QR + tables + workflows + param ref).
Added: ~40 lines (`index_discussions` QR + table + QE section + workflow + param ref + frontmatter).
Net: 657 − 180 + 40 ≈ **517 lines** (−21%). No split yet (DEFERRED).
