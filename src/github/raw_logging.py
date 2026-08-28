# INFRASTRUCTURE
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

# gh-cli repo root, computed relative to this file (src/github/raw_logging.py -> repo root) —
# NOT inside the RAG documents tree (that is a separate project, RAG_ROOT in config.py), so
# nothing written here is ever a candidate for indexing. Covered by the existing `logs/` /
# `*.log` entries in .gitignore.
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_LOG_DIR = _REPO_ROOT / "logs" / "raw_issues"
MANIFEST_PATH = RAW_LOG_DIR / "_manifest.jsonl"

# Bump this whenever the cleaning pipeline changes behavior (strip_noise, strip_comments_noise,
# strip_generic_noise, strip_build_logs, or their call order/site in index_issues.py). Recorded
# per fetch in the manifest so a raw/cleaned diff found months from now can be attributed to the
# filter version that actually produced the cleaned counterpart — without it the delta is
# uninterpretable, since the filter keeps changing underneath the corpus.
CLEANING_VERSION = "2026-08-28-no-prose-guard"


# FUNCTIONS

# Write the raw, unfiltered fetch text (issue body + comments, exactly as the fetch workflows
# returned them, before strip_noise/strip_comments_noise/strip_generic_noise/strip_build_logs
# touch anything) plus one manifest line recording which cleaning version will process it.
# filename matches the cleaned MD's filename exactly, so raw and cleaned diff by name. Never
# raises — a failed write warns and the caller continues indexing; there is no scenario where a
# missing raw log should block a fetch.
def log_raw_issue(filename: str, raw_issue_text: str, raw_comments_text: str) -> None:
    try:
        RAW_LOG_DIR.mkdir(parents=True, exist_ok=True)
        (RAW_LOG_DIR / filename).write_text(
            raw_issue_text + "\n\n" + raw_comments_text, encoding="utf-8"
        )
        entry = {
            "file": filename,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "cleaning_version": CLEANING_VERSION,
        }
        with MANIFEST_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as exc:
        logger.warning("raw_logging: failed to write raw log for %s: %s", filename, exc)
