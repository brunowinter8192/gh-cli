# github-search SKILL Evaluation — 2026-04-25

Aus einer Live-Recherche-Session in Monitor_CC dokumentiert. 8 gh-cli Calls für mitmproxy/textual/glances issues. Vergleichs-Vorbild: `tool-use` Skill (`/Users/brunowinter2000/Documents/ai/Meta/blank/skills/tool-use/SKILL.md`) der das Quality-Niveau setzt.

> **Hinweis:** Ursprünglich als Bead in `.beads/` geplant, aber das Bead-System in MCP/github ist gerade in einem broken state (Dolt-DB "github" wird nicht gefunden, init scheitert). Wenn du das Repo wieder zum Laufen bekommst, dieses File 1:1 als Bead-Description übernehmen.

Drei Stellschrauben separat angegangen.

## 1. Lean Call — kürzere/intuitivere Bash-Invocations

Was schon gut ist: `gh-cli <verb> <positional> [--flags]` Struktur ist konsistent zu git/gh, einfach zu lernen.

Was suboptimal ist:

- `search_repos` query-limit (max 2-3 words) ist im SKILL.md erwähnt aber das Gefühl wann man pivoten muss kommt nicht rüber. „high memory" returned 0, „DataTable scroll" returned 68. Eine Keyword-Strategie wie „Bei Issue-Search: 'X leak' / 'X bug' / 'slow X' als Standard-Lead-Keywords statt 'high X' / 'too much X'" wäre konkret.
- `repo:owner/repo` qualifier muss bei JEDEM `search_code`/`search_items` mitgegeben werden, sonst geht die Suche global. Default-Behavior könnte umgekehrt sein: aus dem aktuellen Repo-Pfad heraus könnte gh-cli automatisch ergänzen, mit Override-Flag für Cross-Repo.
- Combo-Verbs wären praktisch: `gh-cli read_issue <owner> <repo> <num>` als Shortcut für `get_issue` + `get_issue_comments` in einem Call mit kombiniertem Output (Body + Comments mit klaren Trennern). Heute zwei Calls, könnte einer sein.

## 2. Intelligente Wrapper / Configurables für Repo-Traversal

Heute beobachtet: die Recherche brauchte 5 sequenzielle Steps (search_items → top hit identifizieren → get_issue → get_issue_comments → reading). Kein Skill-Bug aber Optimierungs-Potenzial.

Konkrete Wrapper-Ideen:
- `gh-cli explore_issue <owner> <repo> <num>`: gibt Issue + ALLE Comments (capped) + alle PRs die das Issue referenzieren in einem strukturierten File aus. Eine Tool-Call statt drei.
- `gh-cli explore_repo <owner> <repo> --topic memory`: get_repo + get_repo_tree (depth=2) + grep_repo für Topic-Pattern + erste 3 hits in einem File. Architektur-Schnellüberblick in einem Schritt.
- `gh-cli compare_issues <owner1>/<repo1>#N <owner2>/<repo2>#M`: zwei Issues parallel lesen mit Side-by-Side-Output für „leiden gleich an X?".
- Cross-repo `search_items`: ein Query gegen mehrere Repos in einem Call (z.B. `--repos "Textualize/textual,nicolargo/glances,mitmproxy/mitmproxy"`). Heute manuell sequenziell → aufgewertet auf einen Call.

Kein User-Search bisher: wenn man weiß dass mhils interessante Sachen baut, fehlt der Einstiegspunkt. `gh-cli get_user_repos mhils --top 10 --sort stars` wäre wertvoll.

Diskussions-Search ist global, kein Repo-scoped: `list_discussions <owner> <repo>` existiert, aber `search_discussions` hat kein `repo:` qualifier. Asymmetrisch zu search_items.

## 3. Noise-freier Output

Was bei gh-cli sehr gut funktioniert (Quality-Bar):
- `=== response ===` Header und `--- Comment N ---` Delimiter — parser-friendly mit sed/grep/head
- Result-Limits sind konservativ gewählt (top 20 issues, top 30 comments default) — verhindert riesige Dumps
- Empty-result handling explizit: „Found 0 issues matching your query." statt silent fail

Was suboptimal ist:
- get_issue body enthält Original-Markdown inkl. Bilder-Links (`![mitmdump_rss](https://user-images.githubusercontent.com/...)`) und Original-Whitespace. Bei Issues mit vielen embedded images / large code blocks könnten die Output-Tokens explodieren. Optionaler `--strip-images` oder `--text-only` Flag wäre nützlich.
- search_items output enthält für jeden Hit einen redundanten `[get_issue: owner=... repo=... issue_number=N]` Hint. Nice-to-have für AI/Claude (zeigt next-tool-call), aber als rohe-Text-Ausgabe für menschliche Skim-Reader Noise. Optional `--for-human` Flag der die Hints ausspart.
- `get_issue_comments` listet ALLE Comments chronologisch — bei Issues mit 30+ Comments und viel Diskussion sind die top-by-upvotes wertvoller. `get_discussion` hat bereits `--comment-sort upvotes`, aber `get_issue_comments` nicht. Konsistenz fehlt.
- `get_repo` Output ist gut formatiert (Description, Language, Topics, Stars, License) aber Topics-Liste ist Komma-Liste auf einer Zeile. Bei 10+ Topics wird das eine sehr lange Zeile. Multi-line-Wrap optional.

## 4. SKILL.md Struktur — Gap zu tool-use

### Frontmatter description
- tool-use: „Tool-call hygiene. Reduces call-waste through concrete anti-patterns and preferred alternatives. Covers token efficiency, verbose output, tool selection, and per-tool behavior reference."
- github-search: „See ~/.claude/shared-rules/global/cli-skills.md"

Bei einem Browse durch `~/.claude/skills/` weiß man bei github-search nicht was es tut ohne die volle SKILL.md zu öffnen. → eigene Beschreibung in einem Satz fehlt.

### Hard Rules am Anfang
tool-use hat 7 hart nummerierte Rules mit datierten Concrete-Failure-Anker. github-search hat die Rules verstreut über mehrere Sections (Search Strategy / Navigation Rules / Path Integrity / Output Hygiene). Eine konsolidierte Top-Section „Hard Rules" wäre wertvoll. Konkrete Kandidaten:
- „Repo-scoped: ALWAYS add `repo:owner/repo` to search_code/search_items"
- „search_repos query: max 2-3 words"
- „Path Integrity: only paths from previous get_repo_tree output"
- „Always redirect get_issue_comments to /tmp file if >5 comments"
- „search_items empty-result: never retry same query, pivot keywords"
- „Local paths NEVER as `path` parameter"

### Concrete Failures mit Datum
tool-use hat „Concrete failure (2026-04-23): ..." Anker pro Rule. github-search hat WRONG/RIGHT-Beispiele aber keine Session-datierten Anker. Das datierte Anker-Pattern macht Rules „spürbar" — sie sind nicht abstrakt sondern aus echtem Schmerz entstanden.

### Decision-Tree visualisiert
tool-use's Heredoc-Decision-Flow (Case 1/2/3) ist als visueller 4-Step-Flow gestaltet. github-search's `search_repos` vs `search_code` Logik ist textuell beschrieben, würde von einem Decision-Tree-Visualization profitieren.

### Output Hygiene-Promotion
„NEVER use local paths as tool parameters" steht in github-search unter „Output Hygiene" am Ende. Wegen seiner Kritikalität (instant fail) gehört das nach ganz vorne als Hard Rule #1.

## 5. Feature-Lücken (Wunschliste)

- `search_users` / `get_user_repos`: User-Einstiegspunkt fehlt komplett
- `get_repo_languages`: language-percentage breakdown
- `grep_repo --include-history`: Pattern in deleted lines auch matchen
- Cross-repo `search_items` mit Multi-Repo-Filter
- Discussion-Search Repo-scoped
- `explore_*` Combo-Verbs für häufige Sequenzen (Issue + Comments in einem Call)
- Output-Flags: `--strip-images`, `--for-human`, `--comment-sort upvotes` für `get_issue_comments`

## 6. Skill-Test-Methodologie für die Zukunft

Eine Live-Recherche-Session ist der beste Härtetest für ein Skill. Empfehlung: bei jedem Skill-Update eine Mini-Recherche-Aufgabe mitlaufen lassen („finde 3 Repos mit X-Pattern, lies das relevanteste Issue-Thread, fasse zusammen") und beobachten wo der Skill-Holder stolpert. Genau diese Stolperer sind die Stellen wo die SKILL.md klarer werden muss.

## 7. Concrete Source

Recherche-Detail-Notes (das was wir gefunden haben, nicht die Skill-Eval) liegen in `/Users/brunowinter2000/Documents/ai/Monitor_CC/sources/RAM_research_2026-04-25.md`. Inhalt: gh-cli wurde 8 mal aufgerufen für mitmproxy #4456, textual #6381, glances #1447 + Helper-Calls. Output war sauber genug parser-friendly für sed/grep, alle Calls succeeded außer einer (textual + „high memory" zero-result, pivoted auf andere Keywords).
