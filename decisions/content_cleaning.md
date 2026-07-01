# Content Cleaning (RAG-index noise stripping)

## Status Quo (IST)

Noise-stripping shared across the RAG-indexing pipelines (`index_discussions`, `index_issues`) so future fetches auto-clean before MD write.

- `src/github/text_cleaning.py` — generic primitives: `strip_generic_noise(text)` (any `<img …>` tag, any `![…](url)` markdown-image, base64 data-URI, failed-upload `![Uploading…]()`, 1000-char no-space safety net). Used by BOTH `index_discussions` and `index_issues`.
- `src/github/discussion_cleaning.py` — dosu-bot-specific: `strip_noise(text)` (footer/greeting/answer markers, standalone badge lines, markerless greetings, footer-text taglines incl. blockquoted/email + CN variants). Used by `index_discussions`.
- `index_issues` additionally drops whole bot comments (author ends `[bot]`) → dosu footers/badges never reach issue MDs.
- Image regexes loosened to `<img\b[^>]*>` (any tag) + `![…](…)` with non-empty URL (any markdown image) — content-safe (images carry no searchable text).

## Evidenz

- Trigger: `rag-cli index github_discussions` aborted — a 2405-token chunk exceeded the 2048 embed context (HTTP 400); root = dosu-bot shields.io/camo badge runs (2000–6299 chars, no spaces) the char-recursive chunker cannot split. Every text-phrase strip gated by corpus-grep (phrase never in user prose) + dual anchor (exact phrase + dosu/brand token). Deliberate non-strips: email-quote headers (发件人/主题) where the header IS the question, user-quoted greetings, `![]()` syntax examples in code spans. → `decisions/OldThemes/content_cleaning/buildout_2026-06-17.md`.
- Results: discussions 63/78 → 78/78 indexed (15 silent embed-400 failures eliminated), peak no-space run 6299 → 457, ~431k chars removed; issues peak 3137 → 784, 18/103 files re-cleaned. Content integrity verified (SHA256 byte-identity over 78-file corpus, citation links + `##` headings + Q/A intact, 0 content lost). → `dev/discussion_cleaning/` (`audit_discussion_noise.py`, `A_strip_validation.py`, `reclean_existing_mds.py` + reports), `dev/issue_cleaning/reclean_issues.py`.

## Offene Fragen

- Accepted residual: email-quote header remnants left in 1 discussion file (stripping the email structure would destroy the quoted answer content).
