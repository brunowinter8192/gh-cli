# trending command: scraping GitHub Trending (2026-09-24)

Process record for `gh-cli trending`. Code: `src/github/trending.py`. Offline test: `dev/trending/test_trending.py`.

## Constraint

GitHub has no API for Trending. The only source is the HTML page `https://github.com/trending`. The tool therefore scrapes and must fail loudly when the markup drifts.

## URL and parameters (verified live 2026-09-24)

| Want | URL |
|---|---|
| repos, all languages | `/trending?since=daily` |
| repos, one language | `/trending/python?since=weekly` (`c++` stays literal, `c#` becomes `c%23`) |
| developers | `/trending/developers[/<language>]?since=...` |
| spoken language | `?spoken_language_code=de` (repositories only) |

`since` is `daily` / `weekly` / `monthly`, shown as "today" / "this week" / "this month". Requests carry a custom User-Agent and a 10 s timeout. No GitHub token is sent.

## Observed markup

Repository entry: `<article class="Box-row">` with:
- `h2.h3 > a[href="/owner/name"]` (h1 in older markup, both accepted)
- `p` description, absent for some repos (observed: anthropics/financial-services)
- `span[itemprop=programmingLanguage]`
- `a[href$=/stargazers]` and `a[href$=/forks]`, text like `40,132`
- `span.float-sm-right`, text `12,590 stars this week`
- "Built by" avatar links (ignored)

Developer entry: `<article class="Box-row d-flex">` with the developer in `h1.h3 > a[href="/login"]` (text = display name, may be missing, e.g. Ikalus1988), plus a NESTED plain `<article>` for "Popular repo" (`h1.h4 > a[href="/owner/repo"]`, description in `div.f6.mt-1`). The parser tracks article nesting so the nested article does not end the entry.

Entry count varies: repos weekly returned 20, repos daily 17, developers 25. Hence no `--limit`: the tool returns everything the page shows.

## Parser choice

stdlib `html.parser.HTMLParser` (no new dependency, `requirements.txt` unchanged). `EntryCollector` records a flat list of nodes per entry (tag, attrs, classes, accumulated text, flags `nested` and `in_title`); extract functions query that list. Void tags (`img`, ...) and self-closing tags are not pushed on the open-node stack.

## Tripwire

Raise (CLI prints `Error: ...`, exit 1) on: zero entries; missing repo link, stars link, forks link; non-numeric counts; unrecognised period text; repo link not `owner/name`. Optional fields (description, language, period stars, developer popular repo) stay empty. Observed live: `--language nosuchlang123` returns a page with zero entries and hits the tripwire; `--developers --spoken de` is rejected before any fetch.

Note: `--spoken de` can legitimately return very few entries. Observed 1 entry with `+0 today` (public-ui/kolibri).

## Output format

```
Trending repositories · python · this month
1. debpalash/VoiceStudio · Python · stars:34816 · forks:4113 · +23275 this month
   <description, max 160 chars>
```
Developers: `1. henrygd (hank) · popular: henrygd/beszel` plus description line. No emoji (code standard), no "Built by".

## Test

`dev/trending/fixtures/*.html` are trimmed live pages (3 repo articles incl. one without description; 2 developer articles incl. one without display name), about 14 KB total instead of 700 KB. `python dev/trending/test_trending.py` needs no network and writes `dev/trending/md/test_trending.md`. It also checks the tripwires by mutating the fixture (removed `/stargazers`, changed period wording, empty page).

## Pitfalls

- The Python environment with `mcp` installed lives in the main checkout of gh-cli (hidden dot-directory for the virtualenv, see the `~/.local/bin/gh-cli` wrapper); system `python3` lacks `mcp`.
- zsh does not word-split unquoted variables; use `${=var}` when looping over argument strings.
- A pre-commit-style hook rejects any Bash command whose text mentions the virtualenv directory name plus a slash; write docs with the Write tool.
