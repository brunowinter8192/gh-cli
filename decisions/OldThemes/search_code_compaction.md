# search_code Compaction — Rationale

## Why the fragment is KEPT and UNTRUNCATED

`search_code` is a file-locator tool: the user wants to know which file/path contains a pattern AND see the matching snippet. The fragment IS the signal — it provides immediate context (is this the right implementation? is the function signature what I expect?) without a follow-up `get_file_content` call. Truncating at 100 chars destroyed that signal for fragments of typical length (observed range: 59–914 chars in live probes; the 839- and 914-char fragments were completely opaque at 100 chars).

Showing the full fragment per file replaces a two-step (search → read) with one. The 30-result output at typical fragment lengths (~200–900 chars average across multiple fragments) stays well within any context budget.

## Why no fallback loop (unlike search_repos)

`search_code` uses qualifier-based scoping (`repo:`, `language:`) — 0 results means the pattern genuinely isn't present, not that the query was too long. A fallback loop that drops qualifiers would search broader scope than the user intended, returning unrelated files. The hard GitHub Code Search constraint (must include at least one free-text term) is a query-validity rule, not a length issue. No fallback needed.

## Why only `repo:` and `language:` in the skill nudge

The GitHub Code Search qualifier surface includes `org:`, `user:`, `in:file`, `in:path`, boolean operators (AND/OR/NOT), `path:`, `extension:`, `size:`, and `filename:`. The vast majority of gh-cli use-cases are: (a) "find this function/pattern in a specific repo" (`repo:`) and (b) "narrow by language" (`language:`). The remaining qualifiers are either redundant for these cases or introduce edge-cases that confuse rather than help. Deliberately omitting them keeps the nudge scannable and opinionated. A user who needs `org:` can discover it from GitHub docs; a user following the skill nudge should get useful results on first try.

## Why `RESULTS_PER_PAGE` was removed from client.py

`RESULTS_PER_PAGE=20` was defined as a shared constant in `client.py`. After `search_repos` moved to `SEARCH_REPOS_PER_PAGE=30` (local) in the previous session, `search_code` was the sole remaining consumer. Removing it from `search_code.py` and replacing with `SEARCH_CODE_PER_PAGE=30` (local) left `RESULTS_PER_PAGE` with zero remaining users across `src/`. A dead export in the shared client is misleading — it implies something reads it, and it inflates the client's apparent interface. Removed from `client.py` entirely.

## Observed fragment lengths (live probe, 2026-06-03)

Query: `def workflow language:python repo:anthropics/claude-code`

| File | Fragment | Chars |
|---|---|---|
| review_api.py | `def cap_diff_for_prompt(...)` | 59 |
| review_api.py | IaC/CI/ALLOWLIST rules block | 839 |
| patterns.py | `github_actions_workflow` dict entry | 116 |
| patterns.py | `pack_rule_bitmask` docstring | 203 |
| llm.py | false-positive exclusions block | 914 |

The 100-char cap rendered the 839- and 914-char fragments as ~11% visible. All five fragments are fully readable in the new format.

## per_page = 30

Consistent with `search_repos` (same session). GitHub Code Search API supports `per_page` up to 100; total accessible results hard-capped at 1 000. 30 is a practical sweet-spot for discovery — broad enough to surface cross-file pattern matches, small enough to stay cheap even with full fragments.
