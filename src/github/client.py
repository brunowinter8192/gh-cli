# INFRASTRUCTURE
import logging
import os
import re
from pathlib import Path

GITHUB_API_BASE = "https://api.github.com"
RESULTS_PER_PAGE = 20

logger = logging.getLogger(__name__)


# Parse ~/.zshrc for the last `export GH_TOKEN=...` line.
# CC's bash invocations source a frozen shell-snapshot (taken at CC start) instead of
# the live zshrc, so env-only resolution misses rotated tokens until the terminal tab
# is recreated. Reading zshrc directly at every gh-cli invocation makes the rotation
# in zshrc immediately effective without depending on the snapshot.
# Matches: export GH_TOKEN=value | export GH_TOKEN="value" | export GH_TOKEN='value'
# Ignores leading `#` comments. Last assignment wins (mimics zsh source order).
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


# Resolve in canonical order: zshrc wins (defeats stale CC shell-snapshot env),
# then env GH_TOKEN (explicit override), then env GITHUB_TOKEN (CI convention).
def _resolve_token() -> str:
    return (
        _read_zshrc_token()
        or os.environ.get("GH_TOKEN", "")
        or os.environ.get("GITHUB_TOKEN", "")
    )


GITHUB_TOKEN = _resolve_token()


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
