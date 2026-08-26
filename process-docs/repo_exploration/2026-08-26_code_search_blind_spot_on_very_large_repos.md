# `search_code` blind spot on very large repos — download + local grep as the missing rung (2026-08-26)

Continues the `repo_exploration` area. That area's prior entries mapped the orientation tools
(`get_repo_tree`, `get_file_content`) against their local-filesystem analogues and rejected the
endpoints that added no signal. This entry records a case where the `grep` analogue itself —
`search_code` — silently returns nothing on a repo it cannot index, and where the escalation
ladder documented in the `gh-cli-search` skill runs out before the answer is reached.

## What happened

Target: `mozilla/gecko-dev`, looking for the macOS window-activation call in Gecko's Cocoa widget
layer. Two `search_code` calls with distinct, highly specific terms:

- `makeKeyAndOrderFront repo:mozilla/gecko-dev path:widget/cocoa` → 0 results.
- `nsCocoaWindow::Resize repo:mozilla/gecko-dev` → 0 results.

Both terms are verifiably present in the repo. After downloading the single file, a local grep
found `makeKeyAndOrderFront` at 6 distinct call sites and `nsCocoaWindow::Resize` at lines 6153
and 6159 of `widget/cocoa/nsCocoaWindow.mm`. The zero-result answers were therefore not a phrasing
problem and no reformulation would have fixed them.

`get_repo_tree mozilla gecko-dev --path widget/cocoa` worked normally in the same session and
returned the full 120-entry directory listing with per-file line counts. The repo is fully
reachable over GraphQL; only GitHub's code-search index is missing for it. GitHub does not index
every repo for code search, and `gecko-dev` is a multi-million-commit mirror of a non-git upstream —
exactly the profile where the index is absent.

## The gap in the escalation ladder

The `gh-cli-search` skill's rule reads: `search_code` empty → traverse with `get_repo_tree` and read
the exact path with `get_file_content`; only two different tools both returning nothing counts as
absence. Followed literally, that ladder leads to reading an 8191-line, 282 KB source file through
`get_file_content` in offset windows, without knowing which window holds the answer. That is the
worst case the area's own "recursive full-tree dump = anti-pattern" reasoning was written against,
applied to a file instead of a tree.

## What actually resolved it, in two calls

1. `download_files mozilla gecko-dev widget/cocoa/nsCocoaWindow.mm --dest /tmp/gecko` — 282,273
   bytes on disk, one call, no clone, no RAG.
2. A local `grep -n` with the five candidate symbols alternated in one pattern, then a single `sed`
   over the four resulting line ranges.

Total cost: two calls plus one targeted read, against an unbounded number of blind offset windows.
The downloaded file is a throwaway under `/tmp`, so nothing persists and no collection is polluted.

A full `git clone` was considered and rejected: `gecko-dev` is several GB even shallow, and the
question needed exactly one file. Cloning becomes the better option only when the search itself is
repo-wide — when the file is unknown, not just its contents.

## Reading

`download_files` already exists and is documented, but it sits in the command table as a
file-delivery utility rather than as a step in the search ladder. The behavioral gap is that
nothing tells a caller facing an unindexed repo to reach for it. The candidate fix is a third rung
in the escalation rule — download the file (or the directory) and grep it locally — placed before
"two tools returning nothing counts as absence", together with a named trigger: a repo large enough
that GitHub's code-search index is plausibly absent, recognizable by `search_code` returning zero
for a term that a `get_repo_tree` listing shows must exist.
