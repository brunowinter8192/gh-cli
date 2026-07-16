# Issue Management Surface — Rationale

Captures the two surface changes made to `cli.py` issue commands: removal of `comment_issue` and promotion of `get_issue` from internal helper to CLI subcommand.

## comment_issue removed

`comment_issue_workflow` (`src/github/comment_issue.py`, now deleted) posted a comment body to `/repos/{owner}/{repo}/issues/{number}/comments`.

**Why removed:** Opus's issue workflow exclusively uses `update_issue` to maintain a body-based Source-Inventory (structured sections rewritten via PATCH on the issue body). Comments are never written as part of this workflow — they are a different artifact (append-only thread) that serves neither read-modify-write nor structured tracking. The tool had no active caller post-workflow-adoption and was dead surface area. Leaving it registered creates confusion (AI might reach for `comment_issue` when `update_issue` is the correct tool) and adds noise to the CLI help output.

## get_issue promoted to CLI subcommand

`get_issue_workflow` (`src/github/get_issue.py`) retrieves a full issue: title, state, author, dates, labels, comment count, body. It existed solely as an internal helper called by `index_issues.py` during RAG indexing — there was no `get_issue` CLI subcommand.

**Why promoted:** The read-modify-write pattern for issue bodies requires reading the current body before writing a replacement. Without `gh-cli get_issue`, this meant either calling the GitHub REST API directly or using `index_issues` (which does far more: fetches many issues, strips noise, writes MDs, runs RAG indexing). Having `get_issue` as a proper subcommand gives a precise single-issue reader with no side effects. The three-arg shape (owner/repo/number) mirrors `update_issue`, `delete_issue`, and `list_issues` exactly — zero friction.

**get_issue_comments remains internal:** `get_issue_comments_workflow` is kept as an internal-only helper of `index_issues.py`. It is NOT a CLI subcommand. The `[get_issue_comments: ...]` hint line that `format_issue()` previously appended to output (when `issue['comments'] > 0`) has been removed: it appeared in CLI output as if it were a callable CLI tool, misleading users. `index_issues.py` called `get_issue_comments_workflow` directly regardless of the hint; the corresponding `HINT_RE` filter in `strip_noise()` was dead code after the hint was removed and was cleaned up.
