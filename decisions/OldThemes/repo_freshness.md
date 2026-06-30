# repo_freshness — freshness signal: emission site

Process record for the `repo_freshness` tool. Final state lives in `decisions/tool_design.md`.

## Problem

`search_repos` output carries no last-activity date. Repo freshness had to be inferred from sort rank + copyright year in source files, never read from a hard timestamp — despite `--sort-by updated` ranking on exactly that field.

Available timestamps (all from `GET /repos/{owner}/{repo}`, ISO-8601 UTC):

| Field | Meaning | Use |
|---|---|---|
| `pushed_at` | last commit push to any branch | core "code still moving" signal |
| `updated_at` | last change to repo record (push, star, settings, release...) | noisier |
| `created_at` | repo creation | context |

Chosen core signal: `pushed_at`.

## Options for emission site

| Option | Shape | Verdict |
|---|---|---|
| A | add `pushed_at` to each `search_repos` result line (original framing) | rejected — overloads the discovery-list output with a per-repo date; freshness check is a distinct, on-demand use-case, not a search concern |
| B | standalone `repo_freshness` tool, run on one repo | chosen — single `GET /repos/{owner}/{repo}` call, no search/GraphQL enrichment; clean separation: discovery vs freshness-check |

## Decision

Standalone tool `repo_freshness owner repo`. Output: `full_name`, `pushed_at` + relative age ("pushed X days ago", computed `datetime.now(timezone.utc) - pushed_at`), plus `updated_at` / `created_at` as context. Single REST call, mirrors `get_issue` module structure. Purpose surfaced in `skills/gh-cli-search`: judge how current a repo is → how much to trust it on shifting foundations.
