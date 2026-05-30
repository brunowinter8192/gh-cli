# SKILL.md Prod-Adaptation — Scope für Etappe B

Rewrite-Plan: SKILL.md 18-Tool-Stand → 11-Tool-Prod-Stand (2026-05-30).
Referenz-Wahrheit: `cli.py` (11 Subcommands), `src/github/DOCS.md`.

---

## 1. Staleness-Audit (Zeilen-Refs gegen aktuelle SKILL.md, 657 Zeilen)

### 1.1 Falsche Tool-Zahl / Dead-Tool-Referenzen

| Zeile(n) | Problem | Fix |
|---|---|---|
| Z.15 | `"Quick Reference — All 18 Tools"` | → `"All 11 Tools"` |
| Z.34 | `gh-cli search_items ...` | entfernen (Tool gelöscht) |
| Z.35–36 | `gh-cli get_issue ...` / `get_issue_comments ...` | entfernen (interne Helfer, kein Subcommand) |
| Z.40–43 | `search_discussions`, `list_discussions`, `get_discussion` Quick-Ref | entfernen (gelöscht/intern) |
| Z.46–48 | `list_commits`, `compare_commits` Quick-Ref | entfernen (gelöscht) |
| Z.59 | `"Discussions ... planned, not yet built"` | fix: `index_discussions` ist gebaut; releases bleiben CLI-direct (kein RAG) |
| Z.98–100 | Tabelle Issues & PRs: `search_items`, `get_issue`, `get_issue_comments` | entfernen; Sektion → "RAG-Semantic" mit `index_issues` + `index_discussions` |
| Z.104–109 | Tabelle Discussions: `search_discussions`, `list_discussions`, `get_discussion` | entfernen |
| Z.114–118 | Tabelle Commits & Releases: `list_commits`, `compare_commits` | entfernen; Sektion → "Releases" mit `list_releases`, `get_release` only |
| Z.204–207 | Issue Investigation Workflow: `search_items` Schritt 1 | entfernen; Sektion sinnlos ohne search_items → entweder ganz entfernen oder als "via RAG" umschreiben |
| Z.226–230 | Discussion Research Workflow: `search_discussions`, `list_discussions`, `get_discussion` | vollständig ersetzen (siehe §2.3) |
| Z.234–238 | Commit History Workflow | `list_commits`/`compare_commits` entfernen; nur Release-Workflow behalten |
| Z.358–370 | Parameter Reference: `search_items` | entfernen |
| Z.371–377 | Parameter Reference: `get_issue` / `get_issue_comments` | entfernen (interne Helfer — kein CLI-Zugriff) |
| Z.394–419 | Parameter Reference: `search_discussions`, `list_discussions`, `get_discussion` | entfernen (`get_discussion` intern, kein CLI) |
| Z.421–439 | Parameter Reference: `list_commits`, `compare_commits` | entfernen |
| Z.465 | Search Qualifiers: `repo:owner/repo ... search_items` | `search_items` aus Applies-to entfernen |
| Z.538 | "For PR results from search_items --type pr" | entfernen (ganzer Satz) |

### 1.2 Fehlendes: `index_discussions` komplett absent

- Nicht in Quick Reference
- Nicht in Tools by Category
- Kein Query-Engineering-Abschnitt
- Kein Parameter-Reference-Eintrag
- Kein Tool-Chaining-Workflow
- Two Access Patterns (Z.58–59): nur `index_issues` erwähnt

### 1.3 Frontmatter

Aktuell:
```yaml
---
name: github-search
---
```
Fehlend: `description:` (kein Feld vorhanden — Skill-Auto-Activation nicht steuerbar).
Fehlend: `allowed-tools:` (kein Feld — keine Tool-Constraint aktiv).

---

## 2. Ziel-Struktur nach Rewrite (11 Tools)

### 2.1 Frontmatter (neu)

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

### 2.2 Quick Reference (11 Tools)

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

### 2.3 Tools by Category (neu)

**Discovery:** `search_repos`, `search_code`, `get_repo`
**Repository Exploration:** `get_repo_tree`, `get_file_content`
**Content Search:** `grep_file`, `grep_repo`
**RAG-Semantic (Issues):** `index_issues`
**RAG-Semantic (Discussions):** `index_discussions`
**Releases:** `list_releases`, `get_release`

### 2.4 Two Access Patterns (Update)

- **Code & repo content → direct CLI.** `search_repos`, `search_code`, `get_repo`, `get_repo_tree`, `get_file_content`, `grep_file`, `grep_repo`, `list_releases`, `get_release`. Direct `gh-cli` calls.
- **Conversation/discussion layer → query-driven RAG indexing.** Issues: `index_issues "<kw>" <owner/repo>` → `rag-cli search_hybrid "<terms>" github_issues`. Discussions: `index_discussions "<kw>" <owner/repo>` → `rag-cli search_hybrid "<terms>" github_discussions`. A few broad vector searches replace many fine-grained tool-calls. Releases stay CLI-direct (exact-artifact lookup, not fuzzy retrieval).

(Remove "planned, not yet built".)

### 2.5 Query Engineering — index_discussions (NEU, spiegelt index_issues)

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

### 2.6 Tool Chaining — Discussion Research (NEU ersetzt alte 3-Tool-Kette)

```
### Discussion Research
1. index_discussions "<1-3 kw>" owner/repo [--limit N]
   → fetches top-N discussions by relevance, strips noise, writes MDs to github_discussions/
2. rag-cli search_hybrid "<terms>" github_discussions
   → broad vector search across all indexed threads (replaces many get_discussion calls)
```

### 2.7 Tool Chaining — Issue Investigation (UPDATE)

Remove `search_items` step. The workflow now starts at `index_issues`:
```
### Issue Investigation
1. index_issues "<1-3 kw>" owner/repo [--limit 30]
2. rag-cli search_hybrid "<error or symptom terms>" github_issues
```

(The old `search_items → get_issue → get_issue_comments` chain is gone. The 3-step fine-grained lookup no longer has a CLI path; RAG replaces it.)

### 2.8 Parameter Reference — index_discussions (NEU)

| Parameter | Type | Default | Description |
|---|---|---|---|
| query | str | required | Search keywords (max 3; most distinctive first) |
| repo | str | required | Repository as owner/repo |
| --limit | int | 30 | Max discussions to fetch and index |

### 2.9 Commits & Releases Section

Remove `list_commits` / `compare_commits` (deleted). Keep `list_releases` + `get_release` under renamed section "Releases". Remove "Commit History & Version Analysis" workflow; leave "Release Lookup" workflow.

---

## 3. Scope-Cut für Etappe B

### JETZT (Prod-Sync — Etappe B)

| Item | Source | Change |
|---|---|---|
| 18→11 Tool-Zahl | prod reality | quick-ref + all tables + section headers |
| 5 dead tools raus | prod reality | all refs removed (see §1.1 audit) |
| `index_discussions` rein | prod reality | QR + category table + query-eng section + chaining workflow + param ref |
| Two Access Patterns fix | prod reality | remove "not yet built"; add discussions; releases stay CLI-direct |
| `get_issue`/`get_issue_comments`-Demotion | prod reality | remove from user-facing param ref + tables (internal helpers, no subcommand) |
| Frontmatter `description:` | bead github-4xx | new field with trigger phrases + negativ-liste |
| Frontmatter `allowed-tools: Bash` | bead github-chm | new field |
| Issue Investigation workflow | prod reality | `search_items` step removed |

### VERTAGT (nicht Etappe B)

| Item | Source | Warum vertagt |
|---|---|---|
| Progressive loading: SKILL.md → references/ | bead github-3cl | Architektur-Entscheidung; SKILL.md wird nach Prod-Sync erst 11-Tool-clean sein — dann lohnt Split-Evaluation |
| Domain-Split: N Skills | bead github-6vg | Eigene Entscheidung; Multi-Skill-Frage (gleichzeitig aktiv?) ungeklärt |
| Pre-baked Scripts | bead github-i1v | Nachgelagert; erst prod-clean, dann Scripts |

---

## 4. LOC-Schätzung nach Rewrite

Entfernt: ~180 Zeilen (5 tote Tool-Blöcke in QR + Tabellen + Workflows + ParamRef).
Hinzugefügt: ~40 Zeilen (`index_discussions` QR + Tabelle + QE-Sektion + Workflow + ParamRef + Frontmatter).
Net: 657 − 180 + 40 ≈ **517 Zeilen** (−21%). Noch kein Split (VERTAGT).
