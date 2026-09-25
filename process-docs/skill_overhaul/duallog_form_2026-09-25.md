# gh-cli-search skill rewritten in the duallog skill's form (2026-09-25)

## What the user asked for

The user pointed at `iterative-dev/skills/iterative-dev-duallog/SKILL.md` and asked for `skills/gh-cli-search/SKILL.md` to follow exactly that form, after every gh-cli command had been executed once. Second instruction, after the first draft: the Output blocks must be **generic**, like the duallog skill's, showing the shape of the output and never a concrete repo from a test run.

## The target form (from the duallog skill)

- Core rules at the top: one bold sentence, then short bullets, no prose paragraphs.
- `## Commands` as a two-column table `Vorgang | Command`, the command with its full argument syntax.
- One `### <command>` section per command with `#### Input args` (one bullet per argument, em-dash, meaning) and `#### Output` (a fenced block, then bullets explaining the fields).
- Placeholders in angle brackets (`<owner>/<repo>`, `<N>`, `<path>`) inside Output blocks. Fixed literal messages that never vary (the zero-hit NOTE of `search_code`, the 404 line, `No repositories found for '<keyword>'.`) stay verbatim apart from their variable parts.

## How the outputs were obtained

Every command was run on 2026-09-25 (targets: psf/requests, gastownhall/beads, GitHub Trending), plus the RAG steps behind the index commands (`rag-cli search … github_issues --document '%requests%'`, `rag-cli list_documents github_releases --filter 2.34`, `rag-cli expand_chunks github_releases v2.34.2.md 0 --after 2`). The skill's Output blocks were then generalised from those real outputs. None of the test repos appears in the skill.

## Behaviour observed while running, now stated in the skill

- `search_code` prints `No results. Note: GitHub Code Search does not index CSV/data files — use get_file_content for known paths.` on **every** zero-hit result, also when no data file was involved (observed on a plain `def …` query against a code repo).
- `download_files` writes all files flat into `--dest`; the repo's directory structure is not rebuilt (`src/requests/__version__.py` and `README.md` both landed directly in the dest folder).
- `github_issues` and `github_discussions` accumulate across runs and repos, so a follow-up `rag-cli search` should be scoped with `--document '%<repo>%'`; issue documents are named `<repo>__<number>.md`.
- `search_repos` with a nonsense first keyword (`"zzqqxx jupyter notebook"`) ends the 3→2→1 fallback at the first keyword and prints `No repositories found for 'zzqqxx'.` — the fallback drops from the back, confirmed.
- `get_file_content` on a wrong path exits 1 with `Error: 404 Client Error: Not Found for url: https://api.github.com/repos/<owner>/<repo>/contents/<path>`.
- `repo_freshness`: `Pushed` is the code-activity signal, `Updated` also moves on stars/settings (GitHub API semantics, not tested separately).

## index_releases hint aligned with the skill (code change)

`src/github/index_releases.py build_releases_summary` ended with `To search: rag-cli search_hybrid "<your feature query>" github_releases`. That contradicted the skill, which answers "newest release" with `list_documents` + `expand_chunks` from chunk 0 and "since when does feature X exist" with a vector search. The user allowed this one code edit in the main session ("ausnahmsweise"). The summary now ends with two lines:

```
Newest release: rag-cli list_documents github_releases, then rag-cli expand_chunks github_releases <newest-release>.md 0 --after 2
Since when feature X exists: rag-cli search "<feature>" github_releases
```

Verified by running `gh-cli index_releases psf/requests` afterwards: the new lines appear. The `gh-cli` wrapper executes `cli.py` from this source repo directly, so the change is live without publishing; the skill text reaches the plugin cache only via `plugin-publish`.

Older process-docs in this area still name `rag-cli search_hybrid`; they describe the state at their date and were not edited.
