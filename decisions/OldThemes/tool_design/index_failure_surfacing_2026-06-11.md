# Index-failure surfacing — loud error, no retry (2026-06-11)

Cross-tool decision for `index_issues` / `index_discussions` / `index_releases`: how a failed `rag-cli index` (or `rag-cli delete`) subprocess is handled.

## Problem (silent failure)

- All three `run_index()` functions: on `result.returncode != 0` they logged a `logger.warning` and returned `0`. The user-facing summary then read `New chunks added: 0` / `Collection now: N MDs, 0 chunks total` — indistinguishable from a successful no-op. The per-thread MDs were already on disk, but nothing was indexed, and the agent saw apparent success.
- Observed live: a concurrent `list_documents` on `searxng_crypto` held the rag lock → `Error: rag busy` → index swallowed → empty collection reported as success.
- `index_releases.janitor_clean()` was worse: it discarded the `rag-cli delete` returncode entirely AND `rmtree`'d the doc dir regardless. On a busy delete-failure the old collection survived but the doc dir was wiped + refilled → `run_index()` then indexed the new repo's MDs INTO the old collection = mixed-repo data, undetected. It also lacked `text=True` (stderr was bytes).

## Decision (user-directed)

- **Raise a loud error. NO retry, NO backoff.** Retry was explicitly rejected: rag-cli is always running, manual re-index once the server is free is trivial, and the only unacceptable behavior is silent-fail-while-indexing-nothing.
- **`RuntimeError`, not an Error-`TextContent`.** `cli.py` has no try/except around workflow calls, so an unhandled `raise` propagates → traceback on stderr + exit 1 → the agent sees the failure unambiguously. An Error-`TextContent` would give exit 0 and be counted as success — the exact silent-success failure mode we are removing.

## Implementation

- All three `run_index()`: on non-zero exit → `raise RuntimeError(...)`. Message distinguishes busy/locked (`any(w in stderr.lower() for w in ("busy","locked","in use"))`) from a generic failure, names the recovery command `rag-cli index --collection <COLLECTION>` (MDs are already staged), and appends `stderr[:300]`.
- `index_releases.janitor_clean()`: added `text=True`; returncode-check + `raise` placed **before** the `shutil.rmtree(doc_dir)` — so a busy delete-failure leaves the old state fully intact (old collection AND old MDs), never a half-wiped state.

## Verification

- **Happy path — live:** `gh-cli index_discussions "memory" gastownhall/beads` on merged dev → exit 0, unchanged MDs skipped, `github_discussions` intact at 96 chunks, no spurious raise.
- **Error path — code-verified:** a busy DB cannot be forced on demand; the logic is a trivial returncode-check → raise (high confidence by read).

## Scope note

IST captured in `decisions/issue_indexing.md` + `decisions/discussion_indexing.md`. `index_releases` has no dedicated decision file — its janitor/run_index error behavior lives in code + `src/github/DOCS.md`. Same commit also corrected a stale IST line in both decision files: the index mechanism was documented as `RAG/venv/bin/python workflow.py index-dir` but the code uses `rag-cli index --collection <X>` (the historical Evidenz-baseline line in `issue_indexing.md` was left as-is — it describes a past run with the old mechanism).
