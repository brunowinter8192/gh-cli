# Discussion Indexing Probe — gastownhall/beads (2026-05-30)

**Script:** `dev/repo_indexing/fetch_discussions_probe.py`
**Repo:** `gastownhall/beads`
**Query:** `memory repo:gastownhall/beads`

## Search + Fetch

| Metric | Value |
|---|---|
| GraphQL search calls | 1 |
| `discussionCount` returned | 23 (full corpus — `memory` matched all 23 discussions) |
| Per-thread `get_discussion` calls | 23 |
| **Total GraphQL calls** | **24** |

Query note: `memory repo:gastownhall/beads` returned all 23 discussions beads has. The keyword provides relevance ranking but beads is a small, focused repo — every discussion touches the core memory/tracking concept at some level. No fallback needed; 23 < 30 cap, so the full corpus was fetched.

## KB Distribution

| Measure | Total | min | avg | median | max |
|---|---|---|---|---|---|
| Raw (pre-strip) | 122.0 KB | 0.23 KB | 5.30 KB | 3.53 KB | 22.24 KB |
| Stripped | 115.2 KB | 0.06 KB | 5.01 KB | 3.26 KB | 21.95 KB |
| Written MDs | 116.3 KB | 0.08 KB | 5.06 KB | 3.30 KB | 22.02 KB |

**Strip reduction: 5.6%** — much smaller than issues (issues strip removed ~30–40% via checklist boilerplate + metadata). Discussion format is mostly body text; metadata block (`**Category:**`, `**Author:**`, `**Created:**`, per-comment attributions) is a small fraction of total.

**vs issues baseline:** 30 issues ≈ 690 KB (~23 KB/MD avg). Discussions: 23 threads ≈ 116 KB (~5 KB/MD avg). Discussions are ~4.5x more compact per thread. Full beads discussion corpus fits in less than one average issue thread from a large repo.

## Structure Findings

| Category | Count |
|---|---|
| Q&A | 6 |
| Ideas | 6 |
| General | 6 |
| Announcements | 3 |
| Show and tell | 2 |

| Metric | Value |
|---|---|
| 0-comment threads | 9 / 23 (39%) |
| isAnswered (formal) | 0 / 23 |
| Upvotes range | 1–6 (avg 2.4) |
| Comments range | 0–17 (avg 2.1) |

**0-comment threads (39%):** predominantly Ideas category posts and early announcements. Bodies range from near-empty (#4166 "DIsable beads memory", 0.06 KB stripped — one-sentence request) to medium-length proposals. They still carry signal for RAG (the body text describes a feature request or usage question), but are thin.

**isAnswered = 0/23:** surprising for 6 Q&A threads. The Q&A discussions have comments with answers, but none were formally accepted (isAnswer flag set). Means the `### Accepted Answer` block will not appear in any beads thread. All substantive content lives in the comment thread.

**Upvote / engagement ceiling:** max 6 upvotes, avg 2.4. This is a low-traffic repo. Not a problem for indexing, but confirms a relevance floor based on community validation would be too aggressive for beads — it would cut legitimate threads with 1–2 upvotes.

## Structural Note: Accepted Answer Deduplication (flag for index_discussions)

`get_discussion` renders the accepted answer in **two places**: once in the `### Accepted Answer` section (from the `answer` field on the discussion) and once inside the comments list as the comment node with `isAnswer: true` tagged `[ANSWER]`. This is a duplication of the same body text. In the beads corpus it doesn't manifest (0 answered threads), but the future `index_discussions` wrapper should strip or deduplicate the comment-list copy of the accepted answer to avoid duplicate chunk embedding. The `### Accepted Answer` section (labeled, clearly bounded) is the keeper; the in-list copy should be dropped.

## Value Assessment

**Worth indexing: yes, with a minimal quality floor.**

The beads discussion corpus is small (23 threads, 116 KB total) but high-signal — every thread is about beads usage, design philosophy, integration patterns, or workflow questions. The subject matter directly answers "how does beads work / how should I use it" queries that a RAG agent would receive. This is the primary value proposition: discussions capture *why* and *how* reasoning that doesn't appear in code or issues.

Quality concerns:
- 9 zero-comment threads are thin but not noise — body text is on-topic. At 116 KB total, excluding them gains little.
- The two large threads (#3433 "The Agentic Covenant" at 22 KB, #1836 "Keep SQLite" at 15.5 KB) are substantive essays with extended comment threads. These are highest-value chunks.
- Low upvotes/comments reflect a small community, not irrelevant content.

**Recommended floor for `index_discussions`:** none needed for beads (all 23 threads worth indexing). For larger repos, `comment_count >= 1` would cut empty idea posts — apply if total N > 50 and 0-comment fraction > 40%.

**Separate `github_discussions` collection** (not merged into `github_issues`): confirmed. Discussion and issue content serve different query types; keeping them in separate collections allows targeted `--document` filtering and avoids cross-contamination in hybrid retrieval.
