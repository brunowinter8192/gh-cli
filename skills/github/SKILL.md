---
name: gh-search
description: GitHub API search and exploration tools
tools:
  - mcp__plugin_github-research_github__search_repos
  - mcp__plugin_github-research_github__search_code
  - mcp__plugin_github-research_github__get_repo
  - mcp__plugin_github-research_github__get_repo_tree
  - mcp__plugin_github-research_github__get_file_content
  - mcp__plugin_github-research_github__grep_file
  - mcp__plugin_github-research_github__grep_repo
  - mcp__plugin_github-research_github__search_items
  - mcp__plugin_github-research_github__get_issue
  - mcp__plugin_github-research_github__get_issue_comments
  - mcp__plugin_github-research_github__list_repo_prs
  - mcp__plugin_github-research_github__get_pr
  - mcp__plugin_github-research_github__get_pr_files
  - mcp__plugin_github-research_github__search_discussions
  - mcp__plugin_github-research_github__list_discussions
  - mcp__plugin_github-research_github__get_discussion
  - mcp__plugin_github-research_github__list_commits
  - mcp__plugin_github-research_github__compare_commits
  - mcp__plugin_github-research_github__list_releases
  - mcp__plugin_github-research_github__get_release
---

# GitHub MCP Tools — Search Strategy

## Navigation Rules

**1. DOCS first — always.**
Before opening data files or CSVs in any directory, check for README.md or DOCS.md in that directory (or parent). Well-documented repos explain which files are authoritative and what each subdirectory contains. Skipping DOCS leads to reading the wrong file.

**2. Ambiguous matches — check ALL before reporting.**
When multiple candidates exist (same filename in different paths, multiple subdirectories like `approach_1/` through `approach_4/`, different versions of the same data): check ALL of them BEFORE reporting any result to the user. Never report a mismatch after checking only one candidate when others remain unchecked. The correct workflow is:
1. Identify all candidates (parallel `get_file_content` or `grep_file` calls)
2. Compare each against the expected data
3. Report the full picture: which matches, which don't, and why

**Bad:** "v2/config.json doesn't match. Should I check the others?"
**Good:** "Found config.json in 3 locations. v1/ matches the expected data, v2/ and v3/ differ because [reasons]."

**3. When no candidate matches — show all to the user.**
If after checking ALL candidates none matches, present all findings with their full paths and let the user decide. One wrong assumption wastes more time than a few extra tool calls.

**4. Search Mode — targeted vs exploratory.**

Two fundamentally different search modes exist:

- **Targeted search** (user asked for specific data, verification, comparison):
  The user has context. Ask for path when genuinely ambiguous, but exhaust cheap self-serve options first:
  1. `get_repo_tree(pattern="*keyword*")` or `grep_repo` to locate files directly
  2. If file found but content doesn't match → **check same directory first** (`depth=1`) for variants (filtered, selected, final, summary...)
  3. If same directory has nothing → broaden scope one level up
  4. Only after 2-3 failed attempts → ask user
  Use existing context (beads, conversation history) as navigation hints.

- **Exploratory search** (discover trends, compare repos, survey landscape):
  The user has no specific target. Navigate freely with tools.
  Drill down via get_repo_tree, read READMEs, follow interesting leads.
  Example: "What are hot topics in Claude Code?" → Browse repos, read discussions.

**5. Filename search before content search.**
When looking for a specific example or report, search by the broadest known identifier in the filename FIRST (e.g., template name, query ID), not by specific content details (e.g., node IDs, exact values).
- `get_repo_tree(pattern="*Q8*", path="Predictions/")` → finds all Q8 reports in one call
- `grep_repo(pattern="13408", file_pattern="*.md")` → may miss due to `max_files` limit
Server enforces min 20 files for `grep_repo` regardless of `max_files` value.

**6. Truncation → spawn subagent.**
When `grep_repo` or `get_repo_tree` returns a truncation warning, do NOT repeat with same scope.
Instead: spawn a `github-search` subagent to search the truncated directory.
The subagent can independently narrow scope by drilling into subdirectories.
Example: `grep_repo(path="Dynamic")` truncated → spawn subagent:
"Search for value 48.5 in CSV files under Prediction_Methods/Dynamic/Runtime_Prediction.
Drill into subdirectories with depth=1 first, then grep_repo with narrow path."

**7. Session context before new searches.**
Before making new tool calls, check if the referenced data was already read in this session. New claims often reference the same source files as previous ones (e.g., a later thesis section summarizing selection results you already verified). Re-reading known files wastes tool calls and risks misinterpreting which file to look for.

**Detection:** If the user references specific data (table, number, file, claim) → targeted.
If the user says "look around", "explore", "what's out there" → exploratory.

## Subagent Dispatch (github-search)

| Agent | subagent_type | Model | Output |
|-------|---------------|-------|--------|
| github-search | `github-search` | Haiku | FILE/VALUE/PATH per finding |

**Usage:** `Task(subagent_type="github-search", prompt="...")`

**Troubleshooting:** If `subagent_type` not found: run `/context` to check registered agents. If agent is missing, compare its frontmatter (`.claude/agents/<name>.md`) with a working agent — YAML indentation errors silently break registration.

**PROHIBITED:** Never use `subagent_type="general-purpose"` or other generic agents for GitHub repo searches. The `github-search` agent has dedicated instructions (`.claude/agents/github-search.md`) with MCP tool knowledge and the FILE/VALUE/EVIDENCE output format. Generic agents lack this context and produce unstructured output.

### Workflow: Dispatch First → Verify

**CRITICAL:** Always dispatch the sub FIRST. Do NOT start searching yourself — once you start, you tend to keep going instead of delegating.

**Exploratory Research = Subagent ALWAYS (NON-NEGOTIABLE):**
When the task is "find libraries/repos for X" or any broad landscape survey:
- ALWAYS dispatch github-search subagent — no exceptions
- The orchestrator NEVER makes own search_repos calls for exploratory searches
- Subagent does the broad search (multiple short queries), orchestrator verifies top results
- Doing it yourself leads to: too-specific queries, 0 results, 7+ iterations, wasted context
- Pattern: dispatch sub → sub returns candidates → you verify top 3-5 with get_repo/get_file_content

**Ecosystem/Landscape Searches — Breadth First (NON-NEGOTIABLE):**
When researching an entire ecosystem (e.g., "web crawling tools", "vector databases"):
- Dispatch 2+ parallel subagents with DIFFERENT search angles (e.g., one by technology, one by use case)
- Each agent runs 5-10 SHORT queries (2-3 words max), sorted by stars
- A single agent with narrow queries returns niche repos and misses the big players
- Minimum: 10 distinct queries across all agents to cover the landscape
- Example failure: "crawl4ai mcp" (narrow) → 2 repos. Fix: "web crawler python" + "website scraper" + "firecrawl" + "scrapy" → full ecosystem

**Subtask Limit (CRITICAL):**
- Maximum 3-4 subtasks per github-search dispatch
- If task requires 5+ subtasks: split into sequential dispatches (first known issues → then searches/exploration)
- Reason: Haiku context exhausts after ~15 large tool outputs — excess tasks get silently dropped

**1. Dispatch (subagent)**
- Dispatch immediately with all available session context (directory structure, file patterns, what to look for)
- Include known paths from earlier calls (Rule 7) — saves the sub redundant overview work
- Sub does the heavy searching: drilling into directories, reading DOCS, finding CSVs, extracting data
- Sub returns: file paths + concrete data (numbers, counts, content extracts)
- Sub either FINDS the data → you verify, or reports clearly WHAT was checked and WHY it didn't match → you build on that

**2. Verify (you)**
- Double-check critical findings with `get_file_content` or `grep_file`
- Never trust sub numbers blindly — spot-check at least the key claims
- Present verified results to user

**When to skip the sub (do it yourself):**
- Single file lookup where you know the exact path
- 1-2 targeted tool calls that will definitively answer the question
- Data you already have in session context (Rule 7)

**3. Iterate (when claims remain unverified)**
- After Verify, present results including NOT VERIFIED claims — this gives the user a chance to redirect
- When user confirms to continue: dispatch a SECOND sub with accumulated context (not manual search)
- Include everything you now know: verified file paths, directory listings, which files exist in relevant directories
- Each iteration narrows the search: first sub does broad search, second sub targets gaps

### When to Use

- **Data verification in known repos** — Sub finds the specific CSV/file, extracts the numbers
- **Multi-directory search** — Task spans 3+ directories in a repo
- **API truncation** — Large repo tree gets truncated, sub can narrow scope independently
- Finding repos by topic/technology
- Searching code patterns across GitHub
- Comparing multiple repos for a use case
- Investigating issues/PRs in unknown repos

### When NOT to Use

- Single file lookup where you know the exact path
- Simple targeted search where 1-2 tool calls suffice
- You already have the file content and just need to read it
- **Quick Fact Lookup** (stars, description, open issue count, latest PR): Do it yourself with `get_repo` + `search_items`. Dispatching a sub for 2 direct API calls adds latency with no benefit.

### How to Prompt

**BAD:**
- "Find the data in this repo" (no context, no structure info)
- "Search vector databases" (no scope)

**GOOD — include overview context + enforce output format:**
```
Repo: brunowinter8192/PostgresRuntimeEval
Directory structure (from my overview):
- Prediction_Methods/Hybrid_2/Data_Generation/ has 01_patterns.csv
- Prediction_Methods/Hybrid_2/Runtime_Prediction/Pattern_Selection/Error/ has Baseline/ and Epsilon/

Task: Find how many patterns were SELECTED (not total) and their length range.
Look for selected_patterns.csv or selection_summary.csv in Error/Epsilon/.

Output format (MANDATORY — use EXACTLY this for every finding):
FILE: <full repo path>
VALUE: <extracted number or data>
EVIDENCE: <relevant line from file>
```

**Template (data verification):**
```
Repo: [OWNER]/[REPO]
Context: [directory structure from your overview]

Verify these claims:
1. [Claim with specific number]
2. [Claim with specific range]

For each claim, report in this EXACT format:
FILE: <full repo path to source file>
LINES: <total lines in file, noting if line 1 is header>
VALUE: <actual value found>
EVIDENCE: <copy the relevant line(s) from the file>
VERDICT: MATCH / MISMATCH (expected X, found Y)
```

**Template (exploration):**
```
Research [TOPIC] on GitHub.

Focus on:
1. [Specific aspect 1]
2. [Specific aspect 2]

For each repo found:
- Name, stars, description
- Key implementation files (paths!)
- [Specific evaluation criteria]
```

**Truncation Template:**
```
Search for [VALUE/PATTERN] in [REPO] under [TRUNCATED_PATH].

Strategy:
1. get_repo_tree(path="[TRUNCATED_PATH]", depth=1) to discover subdirectories
2. grep_repo with narrow path on each subdirectory
3. Report all matches with full file paths
```

### After Agent Returns

**Agent = Scout, not Authority**

**Expected output format (per finding):**
```
FILE: Prediction_Methods/Hybrid_1/Datasets/Baseline_SVM/approach_3/patterns_filtered.csv
LINES: 74 total (line 1 = header, line 74 = empty trailing newline)
VALUE: 72 patterns
EVIDENCE: pattern_hash;pattern_string;pattern_length;operator_count;occurrence_count (header, line 1)
VERDICT: MATCH (expected 72, found 72)
```

**If agent returns text summaries without FILE/VALUE/EVIDENCE → output is unusable.**
Re-prompt with: "Your output lacked file paths. Re-run and use EXACTLY this format for every finding: FILE: / VALUE: / EVIDENCE:"

**You MUST:**
1. Spot-check at least 1 critical FILE path with `get_file_content`
2. Verify at least 1 VALUE by reading the actual file
3. Never present agent numbers to user without verification
4. **Count CSV rows yourself** — agent line counts are unreliable:
   - Line 1 = header? → subtract 1
   - Trailing newline? → last "line" is empty → subtract 1
   - Read the LAST lines of the file (`offset` near end) to check if final line is empty
   - Example: API says "74 lines" → could be 72 data rows (1 header + 72 data + 1 empty)

**Verification checklist:**
- [ ] Agent provided concrete file paths (not just summaries)
- [ ] Key file paths exist (not hallucinated)
- [ ] Critical numbers match when you spot-check
- [ ] CSV row count verified: read last lines, check for header + trailing newline

**Verification tool selection (CRITICAL):**
When verifying whether a parameter/function/class exists:
- Agent cited a specific FILE → use `grep_file` on THAT file. Direct hit, no false negatives.
- Agent cited no specific file → use `grep_repo` with `file_pattern="*.py"`. Server enforces min 20 files; set higher for repos with 50+ files.
- NEVER conclude "doesn't exist" from a `grep_repo` with low max_files — that's a sampling error, not a verification.

**Verification scope transparency (CRITICAL):**
When reporting results to user, ALWAYS separate:
```
VERIFIED (data matches source file):
- [list what you actually checked against which file]

NOT VERIFIED (not in this data source):
- [list claims you could NOT verify from the file you read]
- [state which file/data would be needed]
```
Never say "MATCH" for claims you didn't actually verify. If thesis shows derived data (pattern labels, computed metrics, visualizations) and you only checked raw data — that is a PARTIAL verification. Say so explicitly.

### Known Pitfalls (Haiku)

1. **Missing Paths** — Agent may forget file paths. Fix: Explicitly ask "Include full file paths for every finding"
2. **Wrong Counts** — Agent may miscount CSV rows or confuse total vs filtered. Fix: Always spot-check counts yourself
3. **Format Drift** — Agent uses own format instead of requested. Fix: Say "Use EXACTLY this format:" with template
4. **Local Path Leak** — Agent may include local filesystem paths. Fix: Verify output contains only GitHub paths
5. **Plan Instead of Data** — Agent returns a "plan" or "strategy" with directory structure but never actually reads files. Fix: When agent output contains NO concrete FILE/VALUE/EVIDENCE entries and instead describes what it WOULD do, immediately dispatch a follow-up sub with:
   - The directory structure the first sub discovered (reuse its work)
   - Explicit instruction: "Read the actual files. Do NOT return a plan. Return FILE/VALUE/EVIDENCE for each finding."
   - Narrower scope targeting the specific files identified by the first sub
   - This is especially common with Haiku on large repos — it maps structure but runs out of turns before reading data
6. **Parameter Confusion** — Agent puts path value into repo field (e.g., `get_file_content(owner="X", repo="CLAUDE.md")` instead of `path="CLAUDE.md"`). Fix: Verify agent output has all 3 required params: owner, repo, path

## Tool Selection

| Goal | Primary Tool | Secondary |
|------|--------------|-----------|
| Find projects by topic | search_repos | get_repo |
| Find code patterns | search_code | get_file_content |
| Understand structure | get_repo_tree | get_file_content |
| Compare projects | search_repos | get_file_content (README) |
| Find Q&A/help | search_discussions | get_discussion |
| Community insights | list_discussions | get_discussion |

## Reading Priority (per repository)

1. **README.md** - Overview, features, usage
2. **package.json / pyproject.toml** - Dependencies, metadata
3. **docs/ or examples/** - Usage patterns
4. **src/** - Only if critical to answer question

## Result Limits

**search_repos / search_code:**
- Fetch: Top 10-15 results
- Read in depth: Top 3-5
- Skim rest: Only for outliers

**Files per repo:**
- Max 3-4 files (README + key sources)
- Use get_repo_tree first to identify critical files

## Known Limitations

**`get_repo_tree` — truncation warning on large repos (Issue #1):**
- GitHub Git Trees API truncates at ~100k entries
- Tool now warns when `truncated=true` in API response
- **Workaround:** Use `path` parameter to narrow search scope — smaller subtree avoids truncation

**`search_code` — does not index CSV/data files (Issue #2):**
- GitHub Code Search skips `type: data` files (CSV, TSV, etc. per GitHub Linguist)
- Tool output hints to use `grep_repo` when 0 results
- **Fallback:** `grep_repo(pattern="search_term", file_pattern="*.csv", path="subdir")`

**`search_repos` — query length limit (Issue #3):**
- Server auto-truncates queries to 3 words with warning in output
- When exploring a broad topic: run MULTIPLE short queries, not ONE long query
- Use `sort_by` parameter (stars, updated) to filter, not more query words

## Searching for Values

When searching for numeric values in CSVs or data files:
- **Stored format ≠ display format:** 6.74% is stored as `0.06741992...`
- `search_code("6.74")` → 0 results. `search_code("0.0674")` → may also fail (CSV not indexed)
- **Strategy:** Search for the column/metric name (e.g., `overall_mre`) instead of the value itself
- **Best approach for data files:** `grep_repo` to search content across matching files
