# Skill-Beads — Konsolidierung (2026-04-26)

> ⚠️ **STALENESS BANNER**
> Diese Beads wurden 2026-04-26 gegen eine **21-Tool**-Oberfläche geschrieben.
> Prod ist jetzt **11 Tools** (Stand 2026-05-30, nach `index_discussions`-Merge).
> Vorschläge, die gelöschte Tools referenzieren, sind unten explizit markiert.
>
> Gelöschte Tools (Dateien aus `src/github/` entfernt): `search_items`, `list_commits`, `compare_commits`.
> Deregistriert als Subcommands (Dateien behalten, intern): `get_issue`, `get_issue_comments` → interne Helfer von `index_issues`; `get_discussion` → interner Helfer von `index_discussions`.
> Gelöschte Subcommands + Dateien: `search_discussions`, `list_discussions`.
>
> **github-6vg** ist am stärksten betroffen — seine Domänen-Tabelle basiert vollständig auf der alten Oberfläche.

---

## Thema 1 — Progressive Loading: SKILL.md → references/ (Bead github-3cl)

**Problem:** `SKILL.md` ist 656 Zeilen flat. Bei jeder Skill-Activation lädt Claude alles — auch wenn der Task nur ein `search_repos`-Lookup ist. Parameter-Reference (~250 Zeilen) und Output-Format-Regeln (~80 Zeilen) sind nicht task-relevant für simple Lookups.

**Vorbild:** `automazeio/ccpm` (5-Phasen-Architektur):
- `SKILL.md` (~80 Zeilen) — Tool-Inventar, Quick-Reference, Pointer auf `references/`
- `references/search-strategy.md`, `references/navigation.md`, `references/output-format.md`, `references/tool-reference.md`, `references/limitations.md`
- URL: https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md

**Vorschlag:** Split in:
- `SKILL.md` (~80 Zeilen) — Tool-Inventar, Quick-Reference, Pointer auf `references/`
- `references/search-strategy.md` — Tool-Selection, iteratives Refinement, Qualifiers
- `references/navigation.md` — DOCS-first, ambiguous-matches, search-mode rules
- `references/output-format.md` — FILE/EVIDENCE/VERDICT, Output Hygiene
- `references/tool-reference.md` — vollständige Parameter-Tabellen pro Tool
- `references/limitations.md` — Truncation, search_code data files, query limits

**Verifikation:** Skill-Activation lädt nur SKILL.md (kürzer); bei konkretem Task wird passendes references/-File explizit referenziert; Token-Einsparung pro Activation messbar.

**Staleness-Note:** Die Tool-Zahl hat sich von 18 auf 11 geändert. Der Split bleibt sinnvoll, aber das "18 Tools = 250 Zeilen Parameter-Reference" Argument ist schwächer — 11 Tools = geschätzte 150 Zeilen. Entscheidung noch angemessen, Ausmaß kleiner als angenommen.

**Status:** VERTAGT — Prod-Sync hat Priorität.

---

## Thema 2 — Description-Field Schärfen (Bead github-4xx)

**Problem:** Aktueller SKILL.md Frontmatter hat **kein `description:`-Feld** (leer — nur `name: github-search`). Claude entscheidet die Auto-Aktivierung anhand des `description`-Felds; fehlt es, wird die Skill zu zufällig aktiviert.

(Bead-Stand: der Bead beschreibt einen Stand mit `description: See ~/.claude/shared-rules/global/cli-skills.md` — diese Zeile existiert in der aktuellen Datei nicht mehr. Das macht das Problem nicht kleiner, sondern größer.)

**Vorbild:** `automazeio/ccpm` — ~600-Zeichen-Description mit: (1) konkreten Trigger-Sätzen, (2) expliziter Negativ-Liste, (3) Synonymen.

**Vorschlag (aus Bead, adaptiert für 11-Tool-Prod):**
```yaml
description: "GitHub remote research via gh-cli. Use when asked to find repos/projects,
  read remote files, search code patterns, browse issues/discussions, or check releases
  on GitHub. Do NOT use for: editing local files, running local git commands, searching
  local code (use Grep/Glob instead), or operations on the user's own GitHub account."
```

Trigger-Phrasen einbauen: "finde repos für X", "zeig mir wie X in Y implementiert ist", "was sind bekannte issues in Z", "index discussions von W für RAG". Negativ-Liste: lokal, `git commit`, `git push`, PR-Operationen auf eigenem Repo.

**Verifikation:** Description-Field aktualisiert; plugin-sync ausgeführt; Test-Sessions: Skill aktiviert sich bei Trigger-Phrasen, NICHT bei lokalen Operationen.

**Status:** JETZT (Etappe B Scope) — geringer Aufwand, hoher Klarheitsgewinn, kein Abhängigkeiten.

---

## Thema 3 — Domain-Split-Architektur: N Skills statt 1 (Bead github-6vg)

**Problem:** Eine monolithische `github-search` Skill mit allen Tools quer durch alle Domänen. Bei Aktivierung wird alles geladen.

**Vorbild:** `github/github-mcp-server` — 14 Toolsets (repos, issues, pull_requests, discussions, …), beim Server-Start aktivierbar/deaktivierbar via Flags. Agent lädt nur die Tools, die er braucht.
URLs: https://github.com/github/github-mcp-server/blob/main/pkg/github/tools.go, https://github.com/github/github-mcp-server/blob/main/docs/toolsets-and-icons.md

**Ursprünglicher Vorschlag (5 fokussierte Skills):**

| Skill | Tools (original, 2026-04-26) |
|---|---|
| `github-discovery` | search_repos, get_repo, search_code |
| `github-content` | get_repo_tree, get_file_content, grep_file, grep_repo |
| `github-issues-prs` | ~~search_items~~, ~~get_issue~~, ~~get_issue_comments~~, ~~list_repo_prs~~, ~~get_pr~~, ~~get_pr_files~~ |
| `github-discussions` | ~~search_discussions~~, ~~list_discussions~~, ~~get_discussion~~ |
| `github-history` | ~~list_commits~~, ~~compare_commits~~, list_releases, get_release |

> ⚠️ **Stark veraltet.** Durchgestrichene Tools sind gelöscht oder intern. Der Vorschlag in seiner ursprünglichen Form ist nicht mehr umsetzbar.

**Aktualisierter Stand (11 Tools, nach index_discussions):**

| Skill | Tools (prod 2026-05-30) |
|---|---|
| `github-discovery` | search_repos, get_repo, search_code |
| `github-content` | get_repo_tree, get_file_content, grep_file, grep_repo |
| `github-rag` | index_issues, index_discussions |
| `github-releases` | list_releases, get_release |

Trade-offs unverändert: PRO = kleinere SKILL.md pro Skill, klarere Auto-Activation. CONTRA = Tool-Chaining über Domänen (z.B. search_code → grep_repo → index_issues) komplizierter; 4 Plugin-Source-Files statt 1.

**Status:** VERTAGT — Multi-Skill-Architektur ist eine Entscheidung eigener Größenordnung, NICHT im Vorbeigehen umsetzbar. Prod-Sync zuerst. Offene Frage: kann Claude mehrere Skills gleichzeitig aktiv haben? (noch ungeklärt).

---

## Thema 4 — allowed-tools: Bash Frontmatter (Bead github-chm)

**Problem:** Kein `allowed-tools`-Feld im Frontmatter. Damit kann der Agent bei aktiver Skill theoretisch auch Read/Edit/Glob auf lokale Files anwenden — was bei `github-search` nie sinnvoll ist (wir lesen GitHub remote, nicht lokal).

**Vorbild:** `myuon/agent-skills` (`skills/gh/SKILL.md`):
```yaml
allowed-tools: Bash
```
URL: https://github.com/myuon/agent-skills/blob/main/skills/gh/SKILL.md

**Vorschlag:** Frontmatter um `allowed-tools: Bash` erweitern.

**Caveat:** Vorher prüfen, ob `allowed-tools: Bash` mit dem Workflow kollidiert (z.B. wenn der Agent zwischendurch lokale Configs lesen müsste). Falls ja: `allowed-tools: Bash, Read` oder ähnlich. Aktuell: gh-cli gibt alles über stdout zurück; kein Read/Edit auf lokale Files nötig während GitHub-Recherche.

**Verifikation:** Frontmatter erweitert; plugin-sync ausgeführt; In Test-Session: Skill aktiv → Read-Tool-Call geblockt.

**Status:** JETZT (Etappe B Scope) — 1-Zeilen-Edit, kein Risiko wenn kein lokales-Read-Bedarf vorhanden.

---

## Thema 5 — Pre-baked Scripts für Discovery-Patterns (Bead github-i1v)

**Problem:** Wiederkehrende Research-Patterns erfordern 2-4 CLI-Calls + manuelles Sortieren/Filtern. Tool-Call-intensiv, Context-budget-belastend.

**Vorbilder:**
- `majiayu000/claude-skill-registry` — `scripts/gh_profile.sh`, `scripts/gh_repos.sh` mit `--limit` Flag. URL: https://github.com/majiayu000/claude-skill-registry/blob/main/skills/development/github-info/SKILL.md
- `automazeio/ccpm` — Script-First-Rule: für deterministische read-and-report Operationen IMMER Script statt manuelle Tool-Sequenz. URL: https://github.com/automazeio/ccpm/blob/main/skill/ccpm/SKILL.md

**Vorschlag:** `skills/github-search/scripts/` mit:
- `top_trending.sh <query> [--limit N]` — search_repos + sort=stars + take N
- `repo_overview.sh <owner/repo>` — get_repo + get_repo_tree depth=1 + README
- ~~`find_issues.sh <owner/repo> --label <label>`~~ — search_items entfernt
- ~~`find_prs_touching.sh <owner/repo> <file_path>`~~ — PR-Tools entfernt
- ~~`compare_releases.sh <owner/repo> <tag1> <tag2>`~~ — compare_commits entfernt

> ⚠️ Drei der 5 Script-Vorschläge referenzieren gelöschte Tools. `top_trending.sh` und `repo_overview.sh` sind noch umsetzbar. Möglicherweise ergänzen: `index_and_search.sh <query> <owner/repo>` als Wrapper für `index_discussions` + `rag-cli search_hybrid`.

**Status:** VERTAGT — nützlich, aber nachgelagert. Erst Prod-Sync, dann Scripts als Ergänzung.
