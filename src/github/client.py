# INFRASTRUCTURE
import logging
import os

GITHUB_API_BASE = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "") or os.environ.get("GH_TOKEN", "")
RESULTS_PER_PAGE = 20

logger = logging.getLogger(__name__)


# FUNCTIONS

# Build headers with optional auth token
def build_headers(accept: str = "application/vnd.github+json") -> dict:
    logger.debug("Building headers accept=%s", accept)
    headers = {
        "Accept": accept,
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers
