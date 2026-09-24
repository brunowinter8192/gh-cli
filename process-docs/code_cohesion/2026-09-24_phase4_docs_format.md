# Phase 4 Step 2: DOCS.md format

## Change
Removed all function-level and constant references from the root, dev/content_cleaning, dev/repo_exploration and src/github DOCS.md files (30 docs-drift-check findings), plus the same kind of names the tool did not flag (imported helper names in "Called by"). Deleted scripts/docs_drift_whitelist.txt (docs-drift-check has no whitelist mechanism any more).

## Salvage from src/github/DOCS.md
State paragraph before cutting: "client.py owns GITHUB_TOKEN (str, module-level), resolved once at import via _resolve_token(). Never mutated after import. Read by all REST modules via build_headers()/request() and by graphql_client.py directly (repo_counts.py transitively)." The ownership and never-mutated facts stay in DOCS.md in name-free form; the names are in client.py.

## Salvage from DOCS.md (root)
Flow: "_build_parser() parses args; _dispatch() routes to <tool>_workflow(params); main() prints result[0].text." Kept in name-free form.
