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
    content = path.read_text(encoding="utf-8", errors="replace")
    matches = _ZSHRC_TOKEN_RE.findall(content)
    return matches[-1] if matches else ""


def _read_env_token(name: str) -> str:
    return os.environ.get(name, "")


def _resolve_token() -> str:
    sources = (
        ("zshrc", _read_zshrc_token),
        ("GH_TOKEN", lambda: _read_env_token("GH_TOKEN")),
        ("GITHUB_TOKEN", lambda: _read_env_token("GITHUB_TOKEN")),
    )
    for name, read in sources:
        token = read()
        if token:
            logger.info("Token resolved from %s", name)
            return token
    return ""


GITHUB_TOKEN = _resolve_token()


# FUNCTIONS

def require_token() -> str:
    if not GITHUB_TOKEN:
        raise RuntimeError("No GitHub token found in ~/.zshrc, GH_TOKEN or GITHUB_TOKEN")
    return GITHUB_TOKEN


def build_headers(accept: str = "application/vnd.github+json") -> dict:
    logger.debug("Building headers accept=%s", accept)
    headers = {
        "Accept": accept,
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": f"Bearer {require_token()}",
    }
    return headers


def request(method: str, path: str, json: dict | None = None, params: dict | None = None) -> dict:
    url = f"{GITHUB_API_BASE}{path}"
    logger.debug("%s %s", method, url)
    response = requests.request(method, url, headers=build_headers(), json=json, params=params)
    response.raise_for_status()
    return response.json()
