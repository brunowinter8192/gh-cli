# INFRASTRUCTURE
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_LOG_DIR = _REPO_ROOT / "logs" / "raw_issues"
MANIFEST_PATH = RAW_LOG_DIR / "_manifest.jsonl"

CLEANING_VERSION = "2026-09-05-keep-attribution"


# FUNCTIONS

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
