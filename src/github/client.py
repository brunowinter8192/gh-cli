# INFRASTRUCTURE
import logging
import os
import re
import requests
from pathlib import Path

GITHUB_API_BASE = "https://api.github.com"

logger = logging.getLogger(__name__)


_ZSHRC_TOKEN_RE = re.compile(
    r'^\s*export\s+GH_TOKEN\s*=\s*["\']?([^"\'\s#]+)["\']?',
    re.MULTILINE,
)


def _read_zshrc_token() -> str:
    path = Path.home() / ".zshrc"
    if not path.is_file():
        return ""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    matches = _ZSHRC_TOKEN_RE.findall(content)
    return matches[-1] if matches else ""


def _resolve_token() -> str:
    return (
        _read_zshrc_token()
        or os.environ.get("GH_TOKEN", "")
        or os.environ.get("GITHUB_TOKEN", "")
    )


GITHUB_TOKEN = _resolve_token()


# FUNCTIONS

def build_headers(accept: str = "application/vnd.github+json") -> dict:
    logger.debug("Building headers accept=%s", accept)
    headers = {
        "Accept": accept,
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def request(method: str, path: str, json: dict | None = None, params: dict | None = None) -> dict:
    url = f"{GITHUB_API_BASE}{path}"
    logger.debug("%s %s", method, url)
    response = requests.request(method, url, headers=build_headers(), json=json, params=params)
    response.raise_for_status()
    return response.json()
