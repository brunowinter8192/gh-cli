# Research Tool Wishlist — 2026-04-28

Reflection after two research runs:
- Run 1: API-latency issues in `anthropics/claude-code` (~15 tool calls)
- Run 2: Claude Code source leaks + binary extract for env-var mapping (~46 tool calls)
Total: ~61 tool calls. Goal of this note: what was friction, what would the ideal tool suite be.

---

## 1. Research anatomy

### Run 1 — GH issues

| Category | Calls | Redundant |
|---|---|---|
| `search_items` | 3 | 1 (third query only returned already-seen issues) |
| `get_issue` (read body) | 6 | 0 |
| `get_issue_comments` | 5 | 0 |
| Grep on comment output | 2 | 0 |
| **Total** | **16** | **1** |

### Run 2 — source code + binary

| Category | Calls | Redundant |
|---|---|---|
| `search_repos` | 1 | 0 |
| `get_repo_tree` | 5 | 1 (wzf1997 utils/ — no hit) |
| `get_file_content` (docs) | 4 | 0 |
| `grep_file` on TS files | 4 | 2 (no matches because post-v2.1.88 env vars) |
| `grep_repo` on TS files | 4 | 3 (all no-match, same reason) |
| npm tarball chain | 9 | 4 (strings flood → two persisted outputs → grep twice) |
| INSIGHTS.md search + reads | 4 | 0 |
| `get_issue_comments` #33949 + greps | 3 | 0 |
| alanisme model-routing read | 3 | 0 |
| **Total** | **37** | **10** |

**Overall tally:** ~61 calls, ~10 clearly redundant, another ~8 low-yield (calls that returned hits but were not worth the output).

---

## 2. Top frictions

### Friction 1 — `get_issue_comments` pagination blindness

**What happened:** issue #26224 has 90 comments. `get_issue_comments` returned 30 — still at March 13, although the issue was updated 2026-04-27. The newest 60 comments (April) were completely invisible. I saw the last Anthropic-staff response (catherinewu, Feb 23) and could not say: is there anything after it? Did I have all the info?

**Cost:** wrong confidence level. I would have reported "last staff response Feb 23, no follow-up" as certain — but it was only "no follow-up visible in the first 30 of the 90 comments."

**Missing:** offset/limit for comments, OR: `--sort created_desc` (newest first), OR: `--filter-author-association MEMBER` to jump directly to staff comments.

---

### Friction 2 — NPM binary extract as a 9-call chain

**What happened:**
```
npm view → (tarball URL)
curl wrapper package → tar list → cat cli-wrapper.cjs  [4 calls, wrapper-only]
npm view platform pkg → (URL)
curl darwin binary (205MB!) → tar extract → ls
strings /tmp/package/claude  → FLOOD → persisted (1MB)
grep on persisted → STILL FLOOD → second persisted (610KB)
grep -a with another pattern → still too broad
grep -oa "CLAUDE_[A-Z_]*"  ← this call was the actually useful one
```

9 calls, ~300MB local download, two huge persisted outputs hanging in context, just to run `grep -oa "CLAUDE_[A-Z_]*"` on a binary. The entire overhead exists because no tool can "give me all strings from an npm binary matching pattern X" — without a local download.

**Cost:** ~4 real waste calls + 2 persisted outputs burdening the context.

---

### Friction 3 — post-v2.1.88 env vars not findable in source code

**What happened:** the decompiled source-code repos (wzf1997, thepono1, by-oneself) are all based on the v2.1.88 source-map leak. The most interesting new env vars (`CLAUDE_SLOW_FIRST_BYTE_MS`, `CLAUDE_ENABLE_BYTE_WATCHDOG`, `CLAUDE_CODE_RETRY_WATCHDOG`, `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS`) were added after the leak. I made 7 `grep_repo` / `grep_file` calls on TS files, all with 0 matches — until I realized: the vars are only in the compiled binary.

The problem: I did not know the non-existence in advance. Every null return cost a call and context.

**Missing:** a version awareness — "which vars exist in v2.1.88 vs. v2.1.121" — or a tool that works directly on the binary instead of the source.

---

### Friction 4 — cross-query issue dedup missing

**What happened:** I made 3 `search_items` queries. Issues #25979, #26224, #49500 appeared in MULTIPLE queries. I had to manually track which ones I had already read. For issue #33949 I was not sure whether I had already seen it in Run 1 (it was mentioned as a dupe-ref in #49500, but not directly in my search results).

**Cost:** cognitive overhead, no real waste calls — but raises the risk of reading an issue twice.

**Missing:** session-level issue dedup in the search tool. "Have I already read #33949 this session?" is something the tool should know.

---

### Friction 5 — staff-comment search as post-processing instead of a filter

**What happened:** to find Anthropic-staff responses I always had to first fetch all comments, then grep locally for `catherinewu`, `MEMBER`, `staff`, `acknowledged`. That is fragile (staff names hard-coded, `MEMBER` also appears in other contexts) and costs an extra grep call per issue.

**Missing:** `get_issue_comments --filter-author-association MEMBER,OWNER` would directly return all staff responses — 1 call instead of 2.

---

## 3. Wishlist

### W1 — `gh_issue_comments_paginated` (Friction 1)

**What it does:** extends `get_issue_comments` with:
- `offset: int` + `limit: int` for real pagination
- `sort_by: "created" | "created_desc"` — default `created_desc` would return the NEWEST comments first (for "are there new staff responses?" that is what you want)
- `filter_author_association: "MEMBER" | "OWNER" | "CONTRIBUTOR"` — returns only comments from Anthropic staff

**Interface:**
```python
get_issue_comments(owner, repo, issue_number,
    sort_by="created_desc",
    filter_author_association="MEMBER",
    limit=10)
```

**Speedup:** for the "did Anthropic react?" use-case: 1 call instead of 2, and correct even on 90-comment issues.

---

### W2 — `npm_binary_strings_extract` (Friction 2, the biggest win)

**What it does:** server-side: downloads the npm package (any platform variant), extracts the binary, runs `strings` + pattern filter. No local download needed.

**Interface:**
```python
npm_binary_strings_extract(
    package="@anthropic-ai/claude-code-darwin-arm64",
    version="latest",           # or "2.1.121"
    pattern="CLAUDE_[A-Z_]+",  # regex, applied as grep -oaE
    deduplicate=True,
    sort=True
)
# → ["CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS", "CLAUDE_ENABLE_BYTE_WATCHDOG", ...]
```

**Internal:** caches the binary between calls (205MB binary, same version → no re-download). Pattern matching server-side, only the matches come back.

**Speedup:** 9 calls → 1 call. ~300MB download eliminated. No persisted-output floods.

**Feasibility:** medium effort. Needs a service that caches npm packages and offers strings-extraction as an API. Alternatively: a local tool that caches on first call (`~/.cache/npm-strings/`). Buildable in 2-3h with existing tech (Node + npm API).

---

### W3 — `gh_cross_repo_search` (Friction 3)

**What it does:** instead of N separate `grep_repo` calls — one call with a repo list. Runs the search in parallel and aggregates results with repo attribution.

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

**Speedup:** 4 calls → 1 call. Especially valuable when you do not know which repo has the sought files.

**Feasibility:** easy — the github-search CLI already does `grep_repo` on single repos. A wrapper that makes N parallel calls and merges: 1h effort.

---

### W4 — `gh_issue_search_with_context` (Friction 4 + 5)

**What it does:** combination of `search_items` + `get_issue` + `get_issue_comments --filter MEMBER` in a single call. For each found issue: body + staff comments in a single response object.

**Interface:**
```python
gh_issue_search_with_context(
    query="slow streaming repo:anthropics/claude-code",
    type="issue",
    sort_by="updated",
    include_body=True,
    include_staff_comments=True,   # filters by MEMBER/OWNER/CONTRIBUTOR
    max_issues=5,
    max_comments_per_issue=3      # top 3 staff comments
)
```

**Speedup:** for "find relevant issues + check whether Anthropic reacted": today ~12 calls (3 search + 6 get_issue + 5 get_comments + 2 grep) → 1-2 calls.

**Feasibility:** medium effort. Requires GitHub API batching + client-side filtering on author_association. With the existing github-search CLI as a base: 3-4h.

---

### W5 — session dedup for issues (Friction 4)

**What it does:** the tool tracks which issue numbers were already read this session. In `search_items` results, already-read issues are marked or filtered.

**Interface:** automatic in the background. `search_items` returns: `already_read: true` for issues where `get_issue` was already called. Optional: `--exclude-already-read` flag.

**Speedup:** no direct call saving, but prevents double reads and saves cognitive load during planning.

**Feasibility:** easy — in-memory set in the CLI process, no persistence needed.

---

### W6 — `npm_version_diff_vars` (Friction 3, fantasy)

**What it does:** given two package versions — diff the contained string literals (env-var names, feature-flag names, error messages). Shows what is NEW, what was removed.

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

**Use case:** would have explained in 1 call why the source-code repos (v2.1.88) lack the new vars. Would also have directly identified the "post-leak additions" without a binary download.

**Feasibility:** medium effort. Needs an npm-binary cache with multi-version support. With the binary-strings infrastructure from W2 as a base: +2-3h.

---

### W7 — `gh_issue_timeline` (fantasy, but valuable)

**What it does:** instead of body + comments separately — a single timeline view of an issue: all events in chronological order (body, comments, label changes, closes/reopens, cross-references), filtered by relevance.

**Interface:**
```python
gh_issue_timeline(
    owner, repo, issue_number,
    filter_events=["comment", "labeled", "closed"],
    filter_author_associations=["MEMBER", "OWNER"],  # optional
    max_events=20,
    sort="desc"  # newest first
)
```

**Use case:** for "what is the current state of this issue?" in one call: last staff comment, last label, whether it was closed, all in one response.

**Feasibility:** GitHub REST API has `/issues/{id}/timeline` — this endpoint exists! Integrable with the existing CLI framework in 2h.

---

## 4. Realistic Subset

### Buildable now (< 2h, existing tech)

| Wishlist item | Effort | What it needs |
|---|---|---|
| W3 `gh_cross_repo_search` | 1h | wrapper over existing `grep_repo` with parallelization |
| W5 session dedup | 30min | in-memory set in the github-search CLI |
| `get_issue_comments --sort created_desc` | 1h | GitHub Comments API has `since` + `page` params, already exposed |

### Medium effort (2-8h)

| Wishlist item | Effort | Main problem |
|---|---|---|
| W2 `npm_binary_strings_extract` | 3-4h | npm-binary download service + caching layer |
| W4 `gh_issue_search_with_context` | 4-5h | batching + rate-limit handling for N issue reads |
| W1 `gh_issue_comments_paginated` | 2h | simple API extension, GitHub supports pagination |
| W7 `gh_issue_timeline` | 2h | wrap the GitHub `/timeline` endpoint directly |

### Fantasy / high effort

| Wishlist item | Effort | Why hard |
|---|---|---|
| W6 `npm_version_diff_vars` | 1-2 days | multi-version binary cache, diff infrastructure |
| Skill stacking (GH + Reddit + Web in 1 call) | days | fundamental change in plugin routing |
| Structured JSON outputs for downstream processing | days | would affect all downstream tools (Monitor_CC proxy display) |

---

## 5. What worked well (counterpoint)

Not everything was friction. The following was surprisingly efficient:

**`alanisme/claude-code-decompiled` structure:** the repo had a numerically ordered file list (`19-streaming-and-transport-layers.md`). One of the rare cases where a community repo is so well structured that `get_repo_tree` + 1 `get_file_content` leads straight to the target — without exploration overhead.

**`grep -oa "CLAUDE_[A-Z_]*"` on the binary:** once I found the right pattern call, the result (292 env vars, sorted, deduplicated) was high-quality in 1 call. The path there was expensive, the result itself was clean.

**`thepono1/INSIGHTS.md`:** 1572 lines of structured documentation of all env vars, feature flags, CLI options. The equivalent of "someone already did all the research work and wrote it into a grep-able file." A file that should have been read first — I found it only after 15 source-search calls.

→ **Meta-lesson:** for community-research repos: ALWAYS read README + INSIGHTS/SUMMARY files first. Only then dig into source files. The community has often already aggregated what I would otherwise painstakingly assemble.

**`search_items --sort-by updated`:** sorting by `updated` instead of `best_match` was the right decision for an ongoing problem. Active issues (Apr 2026) were immediately at the top.

---

## 6. Meta-observation: the real bottleneck

The single biggest inefficiency was not a missing tool — it was **missing version awareness**. I:
- made 7 grep calls on source-code repos (v2.1.88) for env vars that only exist in v2.1.121
- did not know the source-map leak was from v2.1.88 and the sought vars are post-leak
- pieced that together only after the null results + binary extract

A tool that on the first `search_repos "claude-code decompiled"` returns the source-version date ("based on v2.1.88, 2026-04-01") would have immediately set me to "check the v2.1.121 binary directly" — saving ~7 calls.

That is an argument for a `gh_repo_metadata_quick` call that for every repo search also returns "approximate source version" when detectable — instead of reading it manually out of the README.
