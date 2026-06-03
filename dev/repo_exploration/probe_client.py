# Intentional verbatim copy of src/github/client.py (token resolution + build_headers)
# and src/github/graphql_client.py (graphql_query) for dev/-self-containment.
# dev/ probes may not import from src/ (hook: block_dev_imports_src). Update this file
# if the source changes materially (token resolution logic, API base URL).

# INFRASTRUCTURE
import logging
import os
import re
import requests
from pathlib import Path

GITHUB_API_BASE = "https://api.github.com"
GITHUB_GRAPHQL = "https://api.github.com/graphql"

logger = logging.getLogger(__name__)

# Matches: export GH_TOKEN=value | export GH_TOKEN="value" | export GH_TOKEN='value'
# Ignores leading `#` comments. Last assignment wins (mimics zsh source order).
_ZSHRC_TOKEN_RE = re.compile(
    r'^\s*export\s+GH_TOKEN\s*=\s*["\']?([^"\'\s#]+)["\']?',
    re.MULTILINE,
)


# FUNCTIONS

# Parse ~/.zshrc for the last `export GH_TOKEN=...` line.
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


# Resolve in canonical order: zshrc wins, then env GH_TOKEN, then env GITHUB_TOKEN.
def _resolve_token() -> str:
    return (
        _read_zshrc_token()
        or os.environ.get("GH_TOKEN", "")
        or os.environ.get("GITHUB_TOKEN", "")
    )


GITHUB_TOKEN = _resolve_token()


# Build headers with optional auth token
def build_headers(accept: str = "application/vnd.github+json") -> dict:
    headers = {
        "Accept": accept,
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


# Execute GraphQL query against GitHub API
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
