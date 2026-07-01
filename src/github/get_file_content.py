# INFRASTRUCTURE
import logging
import re
import requests
import base64
from mcp.types import TextContent
# From client.py: base API URL and header builder with auth token
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)

# _SIZE_INLINE_MAX: GitHub Contents API inlines base64 content up to 1 MB
# _SIZE_API_MAX: GitHub API hard limit at 100 MB — beyond this, no download supported
_SIZE_INLINE_MAX = 1_048_576
_SIZE_API_MAX    = 104_857_600


# ORCHESTRATOR
def get_file_content_workflow(owner: str, repo: str, path: str, metadata_only: bool = False, offset: int = 0, limit: int = 0) -> list[TextContent]:
    logger.info("get_file_content owner=%s repo=%s path=%s", owner, repo, path)
    raw_response = fetch_file_content(owner, repo, path)

    if isinstance(raw_response, list):
        if metadata_only:
            return [TextContent(type="text", text=format_dir_metadata(raw_response, path))]
        raise ValueError(f"Path '{path}' is a directory, not a file. Use get_repo_tree or metadata_only=True.")

    if metadata_only:
        return [TextContent(type="text", text=format_metadata(raw_response))]

    size = raw_response.get("size", 0)
    if size > _SIZE_API_MAX:
        return [TextContent(type="text", text=format_toolarge_response(raw_response))]
    if size > _SIZE_INLINE_MAX:
        tmp = _tmp_path(owner, repo, path)
        _stream_download(raw_response["download_url"], tmp)
        return [TextContent(type="text", text=format_large_file_response(raw_response, tmp))]
    return [TextContent(type="text", text=format_file_response(raw_response, offset, limit))]


# FUNCTIONS

# Fetch file content from GitHub Contents API
def fetch_file_content(owner: str, repo: str, path: str) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"
    logger.debug("Fetching from %s", url)
    response = requests.get(url, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Build a collision-resistant /tmp path for a downloaded large file
def _tmp_path(owner: str, repo: str, path: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", path)
    return f"/tmp/gh-cli_{owner}_{repo}_{safe}"


# Stream-download url to dest_path; raises on HTTP or network error
def _stream_download(url: str, dest_path: str) -> None:
    resp = requests.get(url, stream=True, timeout=30)
    resp.raise_for_status()
    with open(dest_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=65536):
            f.write(chunk)


# Format response for files in the 1–100 MB tier (downloaded to /tmp)
def format_large_file_response(raw_response: dict, tmp_path: str) -> str:
    path = raw_response["path"]
    name = raw_response["name"]
    size = raw_response["size"]
    url  = raw_response["html_url"]

    lines = []
    lines.append(f"File: {path}")
    lines.append(f"Name: {name}")
    lines.append(f"Size: {size:,} bytes")
    lines.append(f"URL: {url}")
    lines.append("")
    lines.append("Note: file exceeds 1 MB — GitHub Contents API does not inline content above this limit.")
    lines.append(f"Downloaded to: {tmp_path}")
    lines.append("You can now read it locally with offset/limit (e.g. head, tail, or get_file_content with a local path tool).")
    return "\n".join(lines)


# Format response for files larger than 100 MB (GitHub API limit — no download possible)
def format_toolarge_response(raw_response: dict) -> str:
    path = raw_response["path"]
    name = raw_response["name"]
    size = raw_response["size"]
    url  = raw_response["html_url"]

    lines = []
    lines.append(f"File: {path}")
    lines.append(f"Name: {name}")
    lines.append(f"Size: {size:,} bytes")
    lines.append(f"URL: {url}")
    lines.append("")
    lines.append("Error: file exceeds 100 MB — the GitHub API does not support reading or downloading files above this limit.")
    lines.append("No content returned.")
    return "\n".join(lines)


# Format directory metadata from Contents API list response
def format_dir_metadata(raw_response: list, path: str) -> str:
    dirs = [e for e in raw_response if e["type"] == "dir"]
    files = [e for e in raw_response if e["type"] == "file"]
    lines = []
    lines.append(f"Path: {path}")
    lines.append(f"Type: dir")
    lines.append(f"Entries: {len(raw_response)} ({len(dirs)} dirs, {len(files)} files)")
    return "\n".join(lines)


# Format metadata without content decoding
def format_metadata(raw_response: dict) -> str:
    lines = []
    lines.append(f"File: {raw_response['path']}")
    lines.append(f"Name: {raw_response['name']}")
    lines.append(f"Size: {raw_response['size']:,} bytes")
    lines.append(f"Type: {raw_response.get('type', 'unknown')}")
    lines.append(f"SHA: {raw_response.get('sha', 'N/A')}")
    lines.append(f"URL: {raw_response.get('html_url', 'N/A')}")
    return "\n".join(lines)


# Decode base64 content and format response with optional line range
def format_file_response(raw_response: dict, offset: int = 0, limit: int = 0) -> str:
    if raw_response.get("type") != "file":
        raise ValueError(f"Path is not a file, got type: {raw_response.get('type')}")

    decoded_content = decode_content(raw_response)
    content_lines = decoded_content.split("\n")
    total_lines = len(content_lines)

    if limit > 0:
        content_lines = content_lines[offset:offset + limit]
    elif offset > 0:
        content_lines = content_lines[offset:]

    path = raw_response["path"]
    name = raw_response["name"]
    size = raw_response["size"]
    url = raw_response["html_url"]

    lines = []
    lines.append(f"File: {path}")
    lines.append(f"Name: {name}")
    lines.append(f"Size: {size:,} bytes")
    lines.append(f"Lines: {total_lines} total")
    if offset > 0 or limit > 0:
        shown = len(content_lines)
        lines.append(f"Showing: lines {offset + 1}-{offset + shown} of {total_lines}")
    lines.append(f"URL: {url}\n")
    lines.append("Content:")
    lines.append("=" * 60)
    lines.append("\n".join(content_lines))
    lines.append("=" * 60)

    return "\n".join(lines)


# Decode base64 file content to UTF-8 string
def decode_content(raw_response: dict) -> str:
    content = raw_response.get("content", "")
    encoding = raw_response.get("encoding", "")

    if encoding == "base64" and content:
        content_clean = content.replace("\n", "")
        return base64.b64decode(content_clean).decode("utf-8")
    return content
