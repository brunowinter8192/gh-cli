
# INFRASTRUCTURE
import logging
import os
import re
import requests
from pathlib import Path

GITHUB_API_BASE = "https://api.github.com"
GITHUB_GRAPHQL = "https://api.github.com/graphql"

logger = logging.getLogger(__name__)

_ZSHRC_TOKEN_RE = re.compile(
    r'^\s*export\s+GH_TOKEN\s*=\s*["\']?([^"\'\s#]+)["\']?',
    re.MULTILINE,
)


# FUNCTIONS

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


def build_headers(accept: str = "application/vnd.github+json") -> dict:
    headers = {
        "Accept": accept,
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def graphql_query(query: str, variables: dict) -> dict:
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(
        GITHUB_GRAPHQL,
        headers=headers,
        json={"query": query, "variables": variables}
    )
    response.raise_for_status()
    data = response.json()
    if "errors" in data:
        raise Exception(f"GraphQL Error: {data['errors']}")
    return data["data"]
