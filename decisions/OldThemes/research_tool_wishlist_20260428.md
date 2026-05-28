# Research Tool Wishlist — 2026-04-28

Reflexion nach zwei Recherche-Runs:
- Run 1: API-Latency Issues in `anthropics/claude-code` (~15 Tool-Calls)
- Run 2: Claude Code Source Leaks + Binary Extract für Env-Var-Mapping (~46 Tool-Calls)
Total: ~61 Tool-Calls. Ziel dieser Notiz: was war Reibung, was wäre die ideale Tool-Suite.

---

## 1. Recherche-Anatomie

### Run 1 — GH Issues

| Kategorie | Calls | Redundant |
|---|---|---|
| `search_items` | 3 | 1 (dritte Query brachte nur bereits gesehene Issues) |
| `get_issue` (body lesen) | 6 | 0 |
| `get_issue_comments` | 5 | 0 |
| Grep auf Comment-Output | 2 | 0 |
| **Total** | **16** | **1** |

### Run 2 — Source Code + Binary

| Kategorie | Calls | Redundant |
|---|---|---|
| `search_repos` | 1 | 0 |
| `get_repo_tree` | 5 | 1 (wzf1997 utils/ — kein Treffer) |
| `get_file_content` (docs) | 4 | 0 |
| `grep_file` auf TS-Files | 4 | 2 (keine Matches weil Post-v2.1.88 Env-Vars) |
| `grep_repo` auf TS-Files | 4 | 3 (alle no-match, gleicher Grund) |
| npm tarball Kette | 9 | 4 (strings-Flood → zwei Persisted-Outputs → zweimal grep) |
| INSIGHTS.md search + reads | 4 | 0 |
| `get_issue_comments` #33949 + greps | 3 | 0 |
| alanisme model-routing read | 3 | 0 |
| **Total** | **37** | **10** |

**Gesamtbilanz:** ~61 Calls, ~10 eindeutig redundant, weitere ~8 low-yield (Calls die Treffer lieferten, aber den Output nicht wert waren).

---

## 2. Top-Frictions

### Friction 1 — `get_issue_comments` Pagination-Blindheit

**Was passierte:** Issue #26224 hat 90 Comments. `get_issue_comments` lieferte 30 zurück — still at March 13, obwohl das Issue am 2026-04-27 geupdated wurde. Die neuesten 60 Comments (April) waren komplett unsichtbar. Ich sah den letzten Anthropic-Staff-Response (catherinewu, Feb 23) und konnte nicht sagen: gibt es danach noch was? Hatte ich alle Infos?

**Kosten:** Falsches Confidence-Niveau. Ich hätte "letzter Staff-Response Feb 23, kein Follow-up" als gesichert reported — war aber nur "kein Follow-up in den ersten 30 der 90 Comments sichtbar."

**Fehlendes:** Offset/Limit für Comments, OR: `--sort created_desc` (neueste zuerst), OR: `--filter-author-association MEMBER` um direkt auf Staff-Comments zu springen.

---

### Friction 2 — NPM-Binary-Extract als 9-Call-Kette

**Was passierte:**
```
npm view → (tarball URL)
curl wrapper package → tar list → cat cli-wrapper.cjs  [4 calls, Wrapper-Only]
npm view platform pkg → (URL)
curl darwin binary (205MB!) → tar extract → ls
strings /tmp/package/claude  → FLOOD → Persisted (1MB)
grep auf Persisted → NOCH FLOOD → zweites Persisted (610KB)
grep -a mit anderem Pattern → noch zu breit
grep -oa "CLAUDE_[A-Z_]*"  ← dieser Call war der eigentlich nützliche
```

9 Calls, ~300MB lokaler Download, zwei Riesige Persisted-Outputs die im Context hingen, nur um `grep -oa "CLAUDE_[A-Z_]*"` auf einem Binary auszuführen. Der gesamte Overhead existiert weil kein Tool "gib mir alle Strings aus einem npm-Binary die auf Pattern X matchen" kann — ohne lokalen Download.

**Kosten:** ~4 echte Waste-Calls + 2 Persisted-Outputs die den Context belasteten.

---

### Friction 3 — Post-v2.1.88 Env-Vars in Source-Code nicht findbar

**Was passierte:** Die decompilierten Source-Code-Repos (wzf1997, thepono1, by-oneself) basieren alle auf dem v2.1.88 Source-Map-Leak. Die interessantesten neuen Env-Vars (`CLAUDE_SLOW_FIRST_BYTE_MS`, `CLAUDE_ENABLE_BYTE_WATCHDOG`, `CLAUDE_CODE_RETRY_WATCHDOG`, `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS`) wurden nach dem Leak hinzugefügt. Ich habe 7 `grep_repo` / `grep_file` Calls auf TS-Files gemacht, alle mit 0 Matches — bis ich realisierte: die Vars sind nur im Compiled Binary.

Das Problem: ich wusste das Nicht-Vorhandensein nicht vorab. Jeder Null-Return cost einen Call und Context.

**Fehlendes:** Eine Versions-Awareness — "welche Vars gibt es in v2.1.88 vs. v2.1.121" — oder ein Tool das direkt auf dem Binary arbeitet statt auf der Source.

---

### Friction 4 — Cross-Query Issue-Dedup fehlt

**Was passierte:** Ich habe 3 `search_items`-Queries gemacht. Issues #25979, #26224, #49500 tauchten in MEHREREN Queries auf. Ich musste manuell tracked welche ich schon gelesen hatte. Bei Issue #33949 war ich mir nicht sicher ob ich ihn in Run 1 schon gesehen hatte (war als Dupe-Ref in #49500 erwähnt, aber nicht direkt in meinen Search-Results).

**Kosten:** Cognitive Overhead, keine echten Waste-Calls — aber erhöht das Risiko einen Issue doppelt zu lesen.

**Fehlendes:** Session-level Issue-Dedup im Search-Tool. "Habe ich #33949 diese Session schon gelesen?" sollte das Tool wissen.

---

### Friction 5 — Staff-Comment-Suche als Post-Processing statt Filter

**Was passierte:** Um Anthropic-Staff-Responses zu finden musste ich immer erst alle Comments holen, dann lokal greppen nach `catherinewu`, `MEMBER`, `staff`, `acknowledged`. Das ist fragil (Staff-Namen hard-coded, `MEMBER` erscheint auch in anderen Kontexten) und kostet einen extra Grep-Call pro Issue.

**Fehlendes:** `get_issue_comments --filter-author-association MEMBER,OWNER` würde direkt alle Staff-Responses zurückgeben — 1 Call statt 2.

---

## 3. Wishlist

### W1 — `gh_issue_comments_paginated` (Friction 1)

**Was es tut:** Erweiterung von `get_issue_comments` um:
- `offset: int` + `limit: int` für echte Pagination
- `sort_by: "created" | "created_desc"` — default `created_desc` würde die NEUESTEN Comments zuerst liefern (für "gibt es neue Staff-Responses?" ist das was man will)
- `filter_author_association: "MEMBER" | "OWNER" | "CONTRIBUTOR"` — liefert nur Comments von Anthropic-Mitarbeitern

**Interface:**
```python
get_issue_comments(owner, repo, issue_number,
    sort_by="created_desc",
    filter_author_association="MEMBER",
    limit=10)
```

**Speedup:** Für den "hat Anthropic reagiert?" Use-Case: 1 Call statt 2, und korrekt auch bei 90-Comment-Issues.

---

### W2 — `npm_binary_strings_extract` (Friction 2, der größte Gewinn)

**Was es tut:** Server-seitig: lädt npm Package (any platform variant), extrahiert Binary, führt `strings` + Pattern-Filter aus. Kein lokaler Download nötig.

**Interface:**
```python
npm_binary_strings_extract(
    package="@anthropic-ai/claude-code-darwin-arm64",
    version="latest",           # oder "2.1.121"
    pattern="CLAUDE_[A-Z_]+",  # regex, wird als grep -oaE angewendet
    deduplicate=True,
    sort=True
)
# → ["CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS", "CLAUDE_ENABLE_BYTE_WATCHDOG", ...]
```

**Intern:** Cached Binary zwischen Calls (205MB Binary, gleiche Version → kein Re-Download). Pattern-Matching auf Serverseite, zurück kommen nur die Matches.

**Speedup:** 9 Calls → 1 Call. ~300MB Download entfällt. Keine Persisted-Output-Floods.

**Realisierbarkeit:** Mittlerer Aufwand. Braucht einen Service der npm-Packages cached und strings-extraction als API anbietet. Alternativ: ein lokales Tool das beim ersten Aufruf cached (`~/.cache/npm-strings/`). Mit existierender Tech (Node + npm API) in 2-3h baubar.

---

### W3 — `gh_cross_repo_search` (Friction 3)

**Was es tut:** Statt N separate `grep_repo`-Calls — ein Call mit einer Repo-Liste. Führt die Suche parallel aus und aggregiert Ergebnisse mit Repo-Attribution.

**Interface:**
```python
gh_cross_repo_search(
    repos=["wzf1997/claude-code-source",
           "thepono1/claude-code-source",
           "alanisme/claude-code-decompiled"],
    pattern="STREAM_IDLE_TIMEOUT|STREAM_WATCHDOG",
    file_pattern="*.ts",
    max_results_per_repo=5
)
# → {"wzf1997/...": [], "thepono1/...": [...], "alanisme/...": [...]}
```

**Speedup:** 4 Calls → 1 Call. Besonders wertvoll wenn man nicht weiß welches Repo die gesuchten Files hat.

**Realisierbarkeit:** Leicht — das github-search CLI macht schon `grep_repo` auf einzelne Repos. Ein Wrapper der N parallele Calls macht und merged: 1h Aufwand.

---

### W4 — `gh_issue_search_with_context` (Friction 4 + 5)

**Was es tut:** Kombination aus `search_items` + `get_issue` + `get_issue_comments --filter MEMBER` in einem einzigen Call. Für jeden gefundenen Issue: Body + Staff-Comments in einem einzigen Response-Objekt.

**Interface:**
```python
gh_issue_search_with_context(
    query="slow streaming repo:anthropics/claude-code",
    type="issue",
    sort_by="updated",
    include_body=True,
    include_staff_comments=True,   # filtert nach MEMBER/OWNER/CONTRIBUTOR
    max_issues=5,
    max_comments_per_issue=3      # top 3 Staff-Comments
)
```

**Speedup:** Für "finde relevante Issues + check ob Anthropic reagiert hat": heute ~12 Calls (3 search + 6 get_issue + 5 get_comments + 2 grep) → 1-2 Calls.

**Realisierbarkeit:** Mittlerer Aufwand. Erfordert GitHub API Batching + client-side Filtering auf author_association. Mit dem bestehenden github-search CLI als Basis: 3-4h.

---

### W5 — Session-Dedup für Issues (Friction 4)

**Was es tut:** Das Tool tracked welche Issue-Nummern in dieser Session bereits gelesen wurden. In `search_items`-Results werden bereits-gelesene Issues markiert oder gefiltert.

**Interface:** Automatisch im Hintergrund. `search_items` returns: `already_read: true` für Issues die `get_issue` already called. Optional: `--exclude-already-read` flag.

**Speedup:** Kein direkter Call-Saving, aber verhindert Doppel-Reads und spart Cognitive Load beim Planen.

**Realisierbarkeit:** Leicht — in-memory Set im CLI-Prozess, kein Persistenz nötig.

---

### W6 — `npm_version_diff_vars` (Friction 3, Phantasie)

**Was es tut:** Gegeben zwei Package-Versionen — diff die enthaltenen String-Literals (Env-Var-Namen, Feature-Flag-Namen, Error-Messages). Zeigt was NEU hinzugekommen ist, was entfernt wurde.

**Interface:**
```python
npm_version_diff_vars(
    package="@anthropic-ai/claude-code-darwin-arm64",
    from_version="2.1.88",
    to_version="2.1.121",
    pattern="CLAUDE_[A-Z_]+"
)
# → {
#   "added": ["CLAUDE_SLOW_FIRST_BYTE_MS", "CLAUDE_ENABLE_BYTE_WATCHDOG", ...],
#   "removed": [],
#   "unchanged": ["CLAUDE_STREAM_IDLE_TIMEOUT_MS", ...]
# }
```

**Use Case:** Hätte in 1 Call erklärt warum die Source-Code-Repos (v2.1.88) die neuen Vars nicht haben. Hätte auch direkt die "post-leak additions" identifiziert ohne Binary-Download.

**Realisierbarkeit:** Mittlerer Aufwand. Braucht einen npm-Binary-Cache mit Multi-Version-Support. Mit der Binary-Strings-Infrastruktur aus W2 als Basis: +2-3h.

---

### W7 — `gh_issue_timeline` (Phantasie, aber wertvoll)

**Was es tut:** Statt Body + Comments getrennt — eine einzige Timeline-View eines Issues: alle Events in chronologischer Reihenfolge (body, comments, label changes, closes/reopens, cross-references), gefiltert nach Relevanz.

**Interface:**
```python
gh_issue_timeline(
    owner, repo, issue_number,
    filter_events=["comment", "labeled", "closed"],
    filter_author_associations=["MEMBER", "OWNER"],  # optional
    max_events=20,
    sort="desc"  # neueste zuerst
)
```

**Use Case:** Für "was ist der aktuelle Stand dieser Issue?" in einem Call: letzter Staff-Comment, letztes Label, ob sie geschlossen wurde, alles in einer Response.

**Realisierbarkeit:** GitHub REST API hat `/issues/{id}/timeline` — dieser Endpoint existiert! Wäre mit dem bestehenden CLI-Framework in 2h integrierbar.

---

## 4. Realistic Subset

### Sofort baubar (< 2h, existierende Tech)

| Wishlist-Item | Aufwand | Was es braucht |
|---|---|---|
| W3 `gh_cross_repo_search` | 1h | Wrapper über existierenden `grep_repo` mit Parallelisierung |
| W5 Session-Dedup | 30min | In-memory Set im github-search CLI |
| `get_issue_comments --sort created_desc` | 1h | GitHub Comments API hat `since` + `page` Parameter, bereits exponiert |

### Mittlerer Aufwand (2-8h)

| Wishlist-Item | Aufwand | Hauptproblem |
|---|---|---|
| W2 `npm_binary_strings_extract` | 3-4h | npm-Binary-Download-Service + Caching-Layer |
| W4 `gh_issue_search_with_context` | 4-5h | Batching + rate-limit handling für N Issue-Reads |
| W1 `gh_issue_comments_paginated` | 2h | Einfache API-Extension, GitHub unterstützt Pagination |
| W7 `gh_issue_timeline` | 2h | GitHub `/timeline` Endpoint direkt wrappen |

### Phantasie / hoher Aufwand

| Wishlist-Item | Aufwand | Warum schwierig |
|---|---|---|
| W6 `npm_version_diff_vars` | 1-2 Tage | Multi-Version Binary Cache, Diff-Infrastruktur |
| Skill-Stacking (GH + Reddit + Web in 1 Call) | Tage | Fundamentale Änderung im Plugin-Routing |
| Strukturierte JSON-Outputs für nachgelagerte Verarbeitung | Tage | Würde alle Downstream-Tools (Monitor_CC Proxy-Display) betreffen |

---

## 5. Was gut funktioniert hat (Gegenpol)

Nicht alles war Friction. Folgendes war überraschend effizient:

**`alanisme/claude-code-decompiled` Struktur:** Das Repo hatte eine numerisch geordnete Dateiliste (`19-streaming-and-transport-layers.md`). Eines der seltenen Fälle wo ein Community-Repo so gut strukturiert ist dass `get_repo_tree` + 1 `get_file_content` direkt ans Ziel führt — ohne Exploration-Overhead.

**`grep -oa "CLAUDE_[A-Z_]*"` auf Binary:** Sobald ich den richtigen Pattern-Call gefunden hatte, war das Ergebnis (292 Env-Vars, sortiert, dedupliziert) in 1 Call hochwertig. Der Weg dorthin war teuer, das Ergebnis selbst war clean.

**`thepono1/INSIGHTS.md`:** 1572 Zeilen strukturierte Dokumentation aller Env-Vars, Feature-Flags, CLI-Optionen. Das Äquivalent von "jemand hat schon den ganzen Rechercheaufwand gemacht und in eine grep-bare Datei geschrieben." Eine Datei die als erste hätte gelesen werden sollen — ich habe sie erst nach 15 Source-Search-Calls gefunden.

→ **Meta-Lektion:** Bei Community-Research-Repos: IMMER zuerst README + INSIGHTS/SUMMARY-Files lesen. Erst dann in Source-Files graben. Die Community hat oft schon aggregiert was ich erst mühsam zusammensuchen muss.

**`search_items --sort-by updated`:** Sortierung nach `updated` statt `best_match` war die richtige Entscheidung für ein laufendes Problem. Aktive Issues (Apr 2026) waren sofort oben.

---

## 6. Meta-Observation: Die eigentliche Bottleneck

Die größte einzelne Ineffizienz war nicht ein fehlendes Tool — es war **fehlende Versions-Awareness**. Ich habe:
- 7 grep-Calls auf Source-Code-Repos (v2.1.88) für Env-Vars gemacht die erst in v2.1.121 existieren
- Nicht gewusst dass die Source-Map-Leak von v2.1.88 war und die gesuchten Vars post-Leak sind
- Das erst nach den Null-Results + Binary-Extract kombiniert

Ein Tool das beim ersten `search_repos "claude-code decompiled"` das Source-Versions-Datum zurückgibt ("based on v2.1.88, 2026-04-01") hätte mich sofort auf "v2.1.121 binary direkt checken" gesetzt — spart ~7 Calls.

Das ist eine Argument für einen `gh_repo_metadata_quick` Call der für jede Repo-Search auch "approximate source version" zurückgibt wenn erkennbar — statt das aus dem README manuell herauszulesen.
