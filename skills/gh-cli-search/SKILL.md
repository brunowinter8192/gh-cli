---
name: gh-cli-search
description: 
---

# GitHub Search — Skill

**Alles, was INNERHALB eines Repos liegt, holst du direkt über die CLI.**
- Die Commands dafür sind `search_repos`, `search_code`, `get_repo_tree` und `get_file_content`.
- Du liest deren Ausgabe direkt, es gibt keinen Umweg über RAG.

**Issues, Discussions und Releases laufen über RAG, erst indexieren, dann suchen.**
- Issues: `index_issues`, danach `rag-cli search "<terms>" github_issues`.
- Discussions: `index_discussions`, danach `rag-cli search "<terms>" github_discussions`.
- Releases: `index_releases`, danach `rag-cli search "<feature>" github_releases`.
- `rag-cli search` auf diesen Collections läuft erst, nachdem du in dieser Session indexiert hast.

**`get_repo_tree` geht genau eine Ebene tief, du steigst also ab und dumpst nicht.**
- Jeder Aufruf listet exakt eine Verzeichnisebene.
- Tiefer kommst du mit `--path <subdir>` und einem Verzeichnisnamen aus der vorherigen Ausgabe.
- Es gibt keinen rekursiven Modus, keinen Voll-Baum und keine Kürzung.

**Verzeichnisse tragen kein Signal über Zeilen oder Größe.**
- `blob`-Einträge, also Dateien, zeigen `lang`, `lines` und `size`.
- `tree`-Einträge, also Verzeichnisse, zeigen dort nur `-`.
- Was in einem Verzeichnis liegt, erfährst du nur, indem du mit `--path` hineinsteigst.
- Eine Suche über Glob oder Namensmuster gibt es nicht.
   - Eine Datei findest du, indem du zu ihr hinläufst oder `search_code` mit einem inhaltlichen Begriff nutzt.

**Pfade stammen ausschließlich aus vorheriger Tool-Ausgabe und werden nie selbst konstruiert.**
- Gültig sind nur Pfade aus der Ausgabe von `get_repo_tree` oder `get_file_content`.
- Ein 404 heißt, der Pfad ist FALSCH, dann rufst du `get_repo_tree` erneut auf und suchst den echten.

**`search_code` liefert null Treffer für Code, der EXISTIERT, und du kennst die Fälle.**
- Dateien über 350 KiB werden nicht indexiert.
- Leere Dateien, Binärdateien und Dateien ohne UTF-8 werden nicht indexiert.
- Eine Datei mit mehr als einer Zeile über 4096 Bytes ist ausgeschlossen.
- Zeilen über 1024 Zeichen werden abgeschnitten.
   - Ein Treffer hinter dem Abschneidepunkt ist unsichtbar.
- Ein Pfad-Vorfahre namens `external`, `third_party` oder `node_modules` löst den Ausschluss für Vendored- und Generated-Code aus.
   - Diese Heuristik hat bestätigte Fehlalarme auf eigenem Code.
- Datendateien wie CSV und TSV, laut Linguist mit `type: data`, werden nie indexiert.
- Sehr große Repos sind unter Umständen gar nicht indexiert.
- Frische oder inaktive Repos warten auf eine Indexierung bei Bedarf.
- Durchsuchbar ist nur der Default-Branch.
- Identische Dateien über mehrere Repos hinweg werden über ihren SHA dedupliziert.

**Bei null Treffern eskalierst du: klone nach /tmp und greppe.**
- Eine Datei, die `get_repo_tree` auflistet und in der `search_code` nichts findet, beweist eine Lücke im Index und keine Abwesenheit.
- Klone flach und greppe über das ganze Repo: `git clone --depth 1 https://github.com/<owner>/<repo> /tmp/<repo>`, danach `grep -rn`.
   - Bei einem riesigen Repo klonst du nur den Teilbaum: `git clone --depth 1 --sparse ... && git -C /tmp/<repo> sparse-checkout set <subdir>`.
- Blättere niemals blind mit `get_file_content --offset` durch eine große Datei.

**MAXIMAL 3 Keywords, mit Rückfall von 3 auf 2 auf 1.**
- Das gilt identisch für `search_repos`, `index_issues` und `index_discussions`.
- Der Wrapper deckelt hart bei 3, zusätzliche Wörter fallen vor dem Suchaufruf still weg.
- Liefert die Query null Treffer, wirft der Rückfall das hinterste Keyword weg und sucht erneut.
   - Das markanteste Keyword steht deshalb vorne.

**Ein Fehler landet auf stderr und endet mit einem Exit-Code ungleich null.**
- Ursachen sind ein fehlgeschlagener Import, ein fehlendes `GH_TOKEN` oder ein API-Fehler wie 404.
- Prüfe dann zuerst, ob die Umgebungsvariable `GH_TOKEN` gesetzt ist.

## Commands

| Vorgang | Command |
|---|---|
| Repos finden, die Landschaft zu einem Thema abstecken | `search_repos <query> [--sort-by stars\|forks\|updated\|best_match]` |
| Code-Muster finden | `search_code <query>` |
| Eine Verzeichnisebene eines Repos listen | `get_repo_tree <owner> <repo> [--path dir]` |
| Eine Datei aus einem Repo lesen | `get_file_content <owner> <repo> <path> [--offset N] [--limit N] [--metadata-only]` |
| Die Aktualität eines Repos beurteilen | `repo_freshness <owner> <repo>` |
| Repo-Dateien auf die Platte schreiben, ohne Clone und ohne RAG | `download_files <owner> <repo> <path>... [--dest dir]` |
| GitHub Trending lesen | `trending [--language slug] [--since daily\|weekly\|monthly] [--spoken code] [--developers]` |
| Issues nach RAG indexieren | `index_issues "<query>" <owner/repo> [--limit N]` |
| Discussions nach RAG indexieren | `index_discussions "<query>" <owner/repo> [--limit N]` |
| Releases nach RAG indexieren | `index_releases <owner/repo>` |

### search_repos

#### Input args

- `query` — maximal 3 Keywords, dazu Qualifier wie `stars:>N` oder `topic:X`.
- `--sort-by` — `stars`, `forks`, `updated` oder `best_match`.

#### Output

```
<owner>/<repo> · stars:<N> · issues:<N> · discussions:<N>
<owner>/<repo> · stars:<N> · issues:<N> · discussions:0 (off)
```

- Eine Zeile pro Repo, bis zu 30 Zeilen.
- `discussions:0 (off)` heißt, das Repo hat Discussions abgeschaltet, `index_discussions` bringt dort nichts.
- Endet der Rückfall ohne Treffer, nennt die Ausgabe die letzte Query, also das vorderste Keyword:

```
No repositories found for '<keyword>'.
```

### search_code

#### Input args

- `query` — Suchbegriff plus Qualifier, also `repo:owner/repo` und `language:X`.
- Durchsucht wird nur der Default-Branch.

#### Output

```
## Repos (<N> unique)
<owner>/<repo> · stars:<N> · issues:<N> · discussions:<N>

<owner>/<repo> <path>
  <Trefferzeile mit Kontext>
  <Trefferzeile mit Kontext>

<owner>/<repo> <path>
  <Trefferzeile mit Kontext>
```

- Oben die Repos, in denen Treffer liegen, darunter ein Block pro Datei mit Repo, Pfad und den Trefferzeilen samt Kontext.
- Die Pfade aus diesen Blöcken sind gültige Eingaben für `get_file_content`.
- Bei null Treffern erscheint immer dieselbe Zeile, auch wenn gar keine Datendatei gemeint war:

```
No results. Note: GitHub Code Search does not index CSV/data files — use get_file_content for known paths.
```

### get_repo_tree

#### Input args

- `owner` und `repo` — das Ziel-Repo.
- `--path dir` — ein Verzeichnisname aus der vorherigen Ausgabe, ohne die Angabe wird der Root gelistet.

#### Output

```
description:     <Repo-Beschreibung>
primaryLanguage: <Sprache>
languages:       <Sprache> <N>%, <Sprache> <N>%

type: Tree

  name                                     type   lang               lines      size
  ----------------------------------------------------------------------------------
  <verzeichnis>                            tree   -                      -         0
  <datei>                                  blob   <Sprache>            <N>       <N>
```

- Nur der Root-Aufruf trägt die drei Metadaten-Zeilen `description`, `primaryLanguage` und `languages`.
- Ein Aufruf mit `--path` beginnt direkt mit `type: Tree`.
- `size` ist in Bytes.

### get_file_content

#### Input args

- `owner`, `repo` und `path` — `path` stammt aus `get_repo_tree` oder `search_code`.
- `--offset N` und `--limit N` — lesen einen Zeilenausschnitt, `--offset 10 --limit 15` liefert die Zeilen 11 bis 25.
- `--metadata-only` — liefert nur Größe, Typ, SHA und URL, ohne Inhalt.

#### Output

```
File: <path>
Name: <dateiname>
Size: <N> bytes
Lines: <N> total
Showing: lines <von>-<bis> of <N>
URL: https://github.com/<owner>/<repo>/blob/<branch>/<path>

Content:
============================================================
<Dateiinhalt>
============================================================
```

- `Showing` erscheint nur mit `--offset` oder `--limit`.
- Mit `--metadata-only`:

```
File: <path>
Name: <dateiname>
Size: <N> bytes
Type: file
SHA: <sha>
URL: https://github.com/<owner>/<repo>/blob/<branch>/<path>
```

- Ein falscher Pfad endet mit Exit-Code 1:

```
Error: 404 Client Error: Not Found for url: https://api.github.com/repos/<owner>/<repo>/contents/<path>
```

### repo_freshness

#### Input args

- `owner` und `repo` — das Ziel-Repo.

#### Output

```
<owner>/<repo>
Pushed:  <ISO-Zeitstempel>  (pushed <N> days ago)
Updated: <ISO-Zeitstempel>
Created: <ISO-Zeitstempel>
```

- `Pushed` ist der letzte Push von Code, das ist das Maß für Aktivität.
- `Updated` ändert sich auch durch Sterne, Beschreibung oder Settings und sagt über Code nichts aus.

### download_files

#### Input args

- `owner` und `repo` — das Ziel-Repo.
- `path...` — ein oder mehrere Pfade aus `get_repo_tree`.
- `--dest dir` — der Zielordner auf der Platte.

#### Output

```
Downloaded to: <dest>/

Written (<N>):
  <dateiname> -> <dest>/<dateiname> (<N> bytes)

Failed (<N>):
  (none)
```

- Die Dateien landen flach im Zielordner, die Verzeichnisstruktur des Repos wird nicht nachgebaut.

### trending

#### Input args

- `--language slug` — eine Sprache wie `python`, ohne die Angabe alle Sprachen.
- `--since` — `daily`, `weekly` oder `monthly`, der Standard ist `daily`.
- `--spoken code` — ein Sprachcode wie `de`, gilt nur für Repos.
- `--developers` — liefert den Developers-Tab statt der Repos.

#### Output

```
Trending repositories · <sprache> · <zeitraum>
1. <owner>/<repo> · <Sprache> · stars:<N> · forks:<N> · +<N> <zeitraum>
   <Beschreibung>
```

- Gelesen wird die HTML-Seite github.com/trending, nicht die API.
- Die zweite Zeile eines Eintrags ist die Beschreibung, sie fehlt, wenn das Repo keine hat.
- Mit `--developers`:

```
Trending developers · <sprache> · <zeitraum>
1. <login> (<Name>) · popular: <owner>/<repo>
   <Beschreibung des Repos>
```

### index_issues

#### Input args

- `query` — 1 bis 3 Keywords, das markanteste vorne.
- `owner/repo` — das Ziel-Repo in einem Argument.
- `--limit N` — Anzahl der geholten Issues, der Standard ist 30.

#### Output

```
Indexed <N> issues from <owner>/<repo>.
Query: '<query>'
New chunks added this run: <N>
Collection now: <N> MDs, <N> chunks total.
```

- Die Collection `github_issues` wächst über alle Läufe und alle Repos an.
   - Grenze die Suche danach mit `--document '%<repo>%'` auf das Repo ein, die Dokumente heißen `<repo>__<nummer>.md`.
- Ein Treffer der Suche danach:

```
--- Result 1 (score: <score>) ---
Collection: github_issues | Document: <repo>__<nummer>.md | Chunk: <N>
# <Issue-Titel>

State: <OPEN|CLOSED> | #<nummer>
Author: <login> (<rolle>)
Created: <ISO-Zeitstempel> | Updated: <ISO-Zeitstempel>
```

### index_discussions

#### Input args

- `query` — 1 bis 3 Keywords, das markanteste vorne.
- `owner/repo` — das Ziel-Repo in einem Argument.
- `--limit N` — Anzahl der geholten Discussions, der Standard ist 30.

#### Output

```
Indexed <N> discussions from <owner>/<repo>.
Query: '<query>'
New chunks added this run: <N>
Collection now: <N> MDs, <N> chunks total.
```

- Die Collection `github_discussions` wächst wie `github_issues` über alle Läufe an.
- Zeigt `search_repos` für das Repo `discussions:0 (off)`, gibt es nichts zu indexieren.

### index_releases

#### Input args

- `owner/repo` — das Ziel-Repo in einem Argument.
- Geholt werden die letzten 100 Releases.

#### Output

```
Indexed <N> releases from <owner>/<repo>.
New chunks added this run: <N>
Collection now: <N> MDs, <N> chunks total.

To search: rag-cli search_hybrid "<your feature query>" github_releases
```

- Jeder Lauf leert `github_releases` und baut sie für dieses EINE Repo neu auf.
   - Indexiere deshalb unmittelbar vor der Suche.
- Die Frage nach dem neuesten Release beantwortest du mit `expand_chunks` ab Chunk 0, nie mit einer Vektorsuche.
   - Der Weg ist `rag-cli list_documents github_releases`, danach `rag-cli expand_chunks github_releases <newest-release>.md 0 --after 2`.
- Die Vektorsuche auf `github_releases` beantwortet die Frage, seit wann ein Feature X existiert.

## RAG-Nutzung

**Mindestens zwei Durchgänge pro Problem.**
- Der konkrete Durchgang nimmt das exakte Symptom, also den Fehlerstring oder den Signal-Code.
- Der breite Durchgang nimmt die Komponente, das Feature oder den Bereich.
- Beide sammeln sich in derselben Collection an.
- Weitere Blickwinkel sind optional, der breite Durchgang ist zwingend.

```
gh-cli index_issues "<symptom>" <owner/repo> --limit 30
rag-cli search "<exakter Fehlerstring>" github_issues --document '%<repo>%'
rag-cli search "<komponente feature bereich>" github_issues --document '%<repo>%'
```
