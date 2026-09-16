---
name: gh-cli-search
description: 
---

# GitHub Search — Skill

**Code und Repo-Inhalte laufen direkt über die CLI.**
Alles was INNERHALB eines Repos liegt, holst du mit `search_repos`, `search_code`, `get_repo_tree` und `get_file_content`. Das sind direkte `gh-cli`-Aufrufe, und du liest deren Ausgabe.

**Die Konversations- und Release-Schicht läuft über query-getriebene RAG-Indexierung.**
Bei Issues rufst du `gh-cli index_issues "<1-3 kw>" <owner/repo>` auf und danach `rag-cli search "<terms>" github_issues`. Bei Discussions rufst du `gh-cli index_discussions "<1-3 kw>" <owner/repo>` auf und danach `rag-cli search "<terms>" github_discussions`. Bei Releases rufst du `gh-cli index_releases <owner/repo>` auf und danach `rag-cli search "<feature>" github_releases`.

**`get_repo_tree` geht genau eine Ebene tief, du steigst also ab und dumpst nicht.**
Jeder Aufruf listet exakt eine Verzeichnisebene. Um tiefer zu kommen, rufst du erneut auf, mit `--path <subdir>` und einem Verzeichnisnamen aus der vorherigen Ausgabe. Es gibt keinen rekursiven Modus und keinen Voll-Baum, und es gibt auch keine Kürzung. Du läufst den Baum von oben nach unten ab, eine Ebene pro Aufruf.

**Verzeichnisse tragen kein Signal über Zeilen oder Größe.**
In der Auflistung zeigen `blob`-Einträge, also Dateien, die Felder `language`, `lines` und `size`. `tree`-Einträge, also Verzeichnisse, zeigen dort nur `-`. Um zu beurteilen was in einem Verzeichnis liegt, steigst du mit `--path` hinein. Eine Suche über Glob oder Namensmuster gibt es nicht. Um eine Datei zu finden, läufst du entweder zu ihr hin oder du nutzt `search_code` mit einem inhaltlichen Begriff.

**Pfade stammen ausschließlich aus vorheriger Tool-Ausgabe und werden nie selbst konstruiert.**
Nutze nur Repo-Pfade, die in der Ausgabe von `get_repo_tree` oder `get_file_content` aufgetaucht sind. Ein 404 bedeutet, dass der Pfad FALSCH ist, und dann rufst du `get_repo_tree` erneut auf, um den echten zu finden.

**`search_code` liefert null Treffer für Code, der EXISTIERT, und du kennst die Fälle.**
- Dateien über 350 KiB werden nicht indexiert.
- Leere Dateien, Binärdateien und Dateien ohne UTF-8 werden nicht indexiert.
- Eine Datei mit mehr als einer Zeile über 4096 Bytes ist ausgeschlossen.
- Zeilen über 1024 Zeichen werden abgeschnitten.
   - Ein Treffer hinter dem Abschneidepunkt ist unsichtbar.
- Ein Pfad-Vorfahre namens `external`, `third_party` oder `node_modules` löst den Ausschluss für Vendored- und Generated-Code aus.
   - Diese Heuristik hat bestätigte Fehlalarme auf eigenem Code.
- Datendateien wie CSV und TSV, laut Linguist mit `type: data`, werden nie indexiert.
   - Das Tool zeigt bei null Treffern eine NOTE für diesen Fall.
- Sehr große Repos sind unter Umständen gar nicht indexiert.
- Frische oder inaktive Repos warten auf eine Indexierung bei Bedarf.
- Durchsuchbar ist nur der Default-Branch.
- Identische Dateien über mehrere Repos hinweg werden über ihren SHA dedupliziert.

**Eskalation bei null Treffern: klone nach /tmp und greppe.**
- Eine Datei, die `get_repo_tree` auflistet und in der `search_code` nichts findet, beweist eine Lücke im Index und keine Abwesenheit.
- Klone das Repo flach und greppe über das ganze Repo, also `git clone --depth 1 https://github.com/<owner>/<repo> /tmp/<repo>` und danach `grep -rn`.
   - Bei einem riesigen Repo klonst du nur den relevanten Teilbaum, also `git clone --depth 1 --sparse ... && git -C /tmp/<repo> sparse-checkout set <subdir>`.
- Blättere niemals blind mit `get_file_content --offset` durch eine große Datei.

## Commands

| Command | Argumente | Tut |
|---|---|---|
| search_repos | query (max 3 kw; Qualifier: stars:>N, topic:X) [--sort-by stars/forks/updated/best_match] | Repos finden, Landschaft abstecken, was existiert für X |
| search_code | query plus Qualifier (repo:owner/repo, language:X) | Code-Muster finden, nur auf dem Default-Branch |
| get_repo_tree | owner repo [--path dir] | EINE Verzeichnisebene listen, der Root-Aufruf ergänzt Repo-Metadaten |
| get_file_content | owner repo path [--offset N] [--limit N] [--metadata-only] | Eine Datei aus dem Repo lesen |
| repo_freshness | owner repo | pushed_at plus Alter, dazu updated_at und created_at, um die Aktualität zu beurteilen |
| download_files | owner repo path... [--dest dir] | Repo-Dateien auf die lokale Platte schreiben, ohne Clone und ohne RAG |
| index_issues | "query" owner/repo [--limit 30] | Issues holen und nach RAG `github_issues` indexieren |
| index_discussions | "query" owner/repo [--limit 30] | Discussions holen und nach RAG `github_discussions` indexieren |
| index_releases | owner/repo | Die letzten 100 Releases nach RAG `github_releases` indexieren, wobei die Collection geleert und neu aufgebaut wird |

Bei einem Fehler, also einem fehlgeschlagenen Import, einem fehlenden GH_TOKEN oder einem API-Fehler, schreibt die CLI auf stderr und endet mit einem Exit-Code ungleich null. Prüfe dann, ob die Umgebungsvariable `GH_TOKEN` gesetzt ist.

## RAG-Nutzung in gh-cli

**Mindestens zwei Durchgänge pro Problem.**
Ein Durchgang ist konkret und nimmt das exakte Symptom, also den Fehlerstring oder den Signal-Code. Der zweite ist breiter und nimmt die Komponente, das Feature oder den Bereich. Beide sammeln sich in derselben Collection an. Weitere Blickwinkel sind optional, der breite Durchgang ist zwingend.

**Indexieren kommt vor Suchen.**
Führe `rag-cli search` auf `github_issues` oder `github_discussions` erst aus, nachdem du in dieser Session indexiert hast. Also erst indexieren, dann suchen.

**MAXIMAL 3 Keywords, mit Rückfall von 3 auf 2 auf 1.**
Das ist zwingend und gilt identisch für `search_repos`, `index_issues` und `index_discussions`. Der Wrapper deckelt hart bei 3, zusätzliche Wörter fallen vor dem Suchaufruf still weg. Das markanteste Keyword steht vorne, denn die Rückfallschleife wirft von hinten weg. Liefert die Query mit 3 Keywords null Treffer, versucht sie es mit 2 und danach mit 1.

**Nach dem Indexieren suchst du über RAG:**
  ```
  gh-cli index_issues "streaming" anthropics/claude-code --limit 30
  rag-cli search "streaming context window tool_use" github_issues

  gh-cli index_discussions "memory" gastownhall/beads --limit 30
  rag-cli search "memory tracking workflow" github_discussions
  ```

**Bei Releases beantwortest du Aktualitätsfragen mit `read_document` ab Chunk 0, nie mit einer Vektorsuche.**
Nach `index_releases` beantwortest du die Frage nach dem neuesten Release oder der Aktivität eines Pakets, indem du das neueste indexierte Release direkt liest. Der Weg ist `rag-cli list_documents github_releases` und danach `rag-cli read_document github_releases <newest-release>.md 0 --after 2`. Die Vektorsuche auf `github_releases` beantwortet dagegen die Frage, seit wann ein Feature X existiert. Indexiere dein Ziel-Repo unmittelbar vor der Suche, denn jeder Lauf leert die Collection und baut sie auf dieses EINE Repo neu auf.
