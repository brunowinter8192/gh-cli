# INFRASTRUCTURE
import logging
import requests
import base64
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)


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
    return [TextContent(type="text", text=format_file_response(raw_response, offset, limit))]


# FUNCTIONS

# Fetch file content from GitHub Contents API
def fetch_file_content(owner: str, repo: str, path: str) -> dict:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/contents/{path}"
    logger.debug("Fetching from %s", url)
    response = requests.get(url, headers=build_headers())
    response.raise_for_status()
    return response.json()


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
