# github-search SKILL Evaluation — 2026-04-25

Documented from a live research session in Monitor_CC. 8 gh-cli calls for mitmproxy/textual/glances issues. Comparison benchmark: the `tool-use` skill (`/Users/brunowinter2000/Documents/ai/Meta/blank/skills/tool-use/SKILL.md`), which sets the quality bar.

> **Note:** originally planned as a bead in `.beads/`, but the bead system in MCP/github is currently in a broken state (Dolt DB "github" not found, init fails). If the repo runs again, adopt this file 1:1 as the bead description.

Three levers addressed separately.

## 1. Lean Call — shorter / more intuitive Bash invocations

Already good: the `gh-cli <verb> <positional> [--flags]` structure is consistent with git/gh, easy to learn.

Suboptimal:

- `search_repos` query limit (max 2-3 words) is mentioned in SKILL.md, but the sense of WHEN to pivot does not come across. "high memory" returned 0, "DataTable scroll" returned 68. A keyword strategy like "for issue search: use 'X leak' / 'X bug' / 'slow X' as default lead keywords instead of 'high X' / 'too much X'" would be concrete.
- The `repo:owner/repo` qualifier must be passed on EVERY `search_code`/`search_items`, otherwise the search goes global. Default behavior could be reversed: from the current repo path, gh-cli could auto-append it, with an override flag for cross-repo.
- Combo verbs would be handy: `gh-cli read_issue <owner> <repo> <num>` as a shortcut for `get_issue` + `get_issue_comments` in one call with combined output (body + comments with clear separators). Two calls today, could be one.

## 2. Smart wrappers / configurables for repo traversal

Observed today: the research needed 5 sequential steps (search_items → identify top hit → get_issue → get_issue_comments → reading). Not a skill bug, but optimization potential.

Concrete wrapper ideas:
- `gh-cli explore_issue <owner> <repo> <num>`: emits issue + ALL comments (capped) + all PRs referencing the issue in one structured file. One tool call instead of three.
- `gh-cli explore_repo <owner> <repo> --topic memory`: get_repo + get_repo_tree (depth=2) + grep_repo for the topic pattern + first 3 hits in one file. Architecture quick-overview in one step.
- `gh-cli compare_issues <owner1>/<repo1>#N <owner2>/<repo2>#M`: read two issues in parallel with side-by-side output for "do they suffer from the same X?".
- Cross-repo `search_items`: one query against multiple repos in one call (e.g. `--repos "Textualize/textual,nicolargo/glances,mitmproxy/mitmproxy"`). Manually sequential today → upgraded to one call.

No user search yet: when you know mhils builds interesting things, the entry point is missing. `gh-cli get_user_repos mhils --top 10 --sort stars` would be valuable.

Discussion search is global, not repo-scoped: `list_discussions <owner> <repo>` exists, but `search_discussions` has no `repo:` qualifier. Asymmetric to search_items.

## 3. Noise-free output

What works very well in gh-cli (quality bar):
- `=== response ===` header and `--- Comment N ---` delimiter — parser-friendly with sed/grep/head
- Result limits are chosen conservatively (top 20 issues, top 30 comments default) — prevents huge dumps
- Empty-result handling explicit: "Found 0 issues matching your query." instead of silent fail

Suboptimal:
- get_issue body contains original markdown incl. image links (`![mitmdump_rss](https://user-images.githubusercontent.com/...)`) and original whitespace. For issues with many embedded images / large code blocks, output tokens could explode. An optional `--strip-images` or `--text-only` flag would help.
- search_items output contains a redundant `[get_issue: owner=... repo=... issue_number=N]` hint per hit. Nice-to-have for AI/Claude (shows next tool call), but as raw text output for a human skim-reader it is noise. Optional `--for-human` flag that omits the hints.
- `get_issue_comments` lists ALL comments chronologically — for issues with 30+ comments and much discussion, the top-by-upvotes are more valuable. `get_discussion` already has `--comment-sort upvotes`, but `get_issue_comments` does not. Consistency missing.
- `get_repo` output is well formatted (description, language, topics, stars, license) but the topics list is a comma list on one line. With 10+ topics this becomes a very long line. Optional multi-line wrap.

## 4. SKILL.md structure — gap to tool-use

### Frontmatter description
- tool-use: "Tool-call hygiene. Reduces call-waste through concrete anti-patterns and preferred alternatives. Covers token efficiency, verbose output, tool selection, and per-tool behavior reference."
- github-search: "See ~/.claude/shared-rules/global/cli-skills.md"

Browsing `~/.claude/skills/`, you cannot tell what github-search does without opening the full SKILL.md. → a one-sentence own description is missing.

### Hard Rules up front
tool-use has 7 hard-numbered rules with dated concrete-failure anchors. github-search has its rules scattered across several sections (Search Strategy / Navigation Rules / Path Integrity / Output Hygiene). A consolidated top section "Hard Rules" would be valuable. Concrete candidates:
- "Repo-scoped: ALWAYS add `repo:owner/repo` to search_code/search_items"
- "search_repos query: max 2-3 words"
- "Path Integrity: only paths from previous get_repo_tree output"
- "Always redirect get_issue_comments to /tmp file if >5 comments"
- "search_items empty-result: never retry same query, pivot keywords"
- "Local paths NEVER as `path` parameter"

### Concrete failures with date
tool-use has "Concrete failure (2026-04-23): ..." anchors per rule. github-search has WRONG/RIGHT examples but no session-dated anchors. The dated-anchor pattern makes rules "tangible" — they are not abstract but born from real pain.

### Decision tree visualized
tool-use's heredoc decision flow (Case 1/2/3) is designed as a visual 4-step flow. github-search's `search_repos` vs `search_code` logic is described textually, would benefit from a decision-tree visualization.

### Output Hygiene promotion
"NEVER use local paths as tool parameters" sits in github-search under "Output Hygiene" at the end. Due to its criticality (instant fail) it belongs at the very front as Hard Rule #1.

## 5. Feature gaps (wishlist)

- `search_users` / `get_user_repos`: user entry point missing entirely
- `get_repo_languages`: language-percentage breakdown
- `grep_repo --include-history`: match pattern in deleted lines too
- Cross-repo `search_items` with multi-repo filter
- Discussion search repo-scoped
- `explore_*` combo verbs for frequent sequences (issue + comments in one call)
- Output flags: `--strip-images`, `--for-human`, `--comment-sort upvotes` for `get_issue_comments`

## 6. Skill-test methodology for the future

A live research session is the best stress test for a skill. Recommendation: on every skill update, run a mini research task alongside ("find 3 repos with X pattern, read the most relevant issue thread, summarize") and observe where the skill holder stumbles. Exactly those stumbles are the spots where the SKILL.md must become clearer.

## 7. Concrete Source

Research detail notes (what we found, not the skill eval) are in `/Users/brunowinter2000/Documents/ai/Monitor_CC/sources/RAM_research_2026-04-25.md`. Content: gh-cli was called 8 times for mitmproxy #4456, textual #6381, glances #1447 + helper calls. Output was clean enough / parser-friendly for sed/grep, all calls succeeded except one (textual + "high memory" zero-result, pivoted to other keywords).
