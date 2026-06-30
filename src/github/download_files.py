# INFRASTRUCTURE
import logging
import os

from mcp.types import TextContent

from src.github.get_file_content import fetch_file_content, _stream_download, _SIZE_API_MAX

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def download_files_workflow(owner: str, repo: str, paths: list[str], dest: str) -> list[TextContent]:
    logger.info("download_files owner=%s repo=%s paths=%s dest=%s", owner, repo, paths, dest)
    os.makedirs(dest, exist_ok=True)
    written, failed = _download_paths(owner, repo, paths, dest)
    return [TextContent(type="text", text=format_download_report(written, failed, dest))]


# FUNCTIONS

# Fetch and stream each path; collect written and failed results
def _download_paths(owner: str, repo: str, paths: list[str], dest: str) -> tuple[list, list]:
    written = []
    failed = []
    for path in paths:
        try:
            raw = fetch_file_content(owner, repo, path)
        except Exception as e:
            failed.append((path, str(e)))
            continue

        if isinstance(raw, list):
            failed.append((path, "path is a directory"))
            continue

        download_url = raw.get("download_url")
        if download_url is None:
            failed.append((path, "no download_url (submodule or symlink)"))
            continue

        size = raw.get("size", 0)
        if size > _SIZE_API_MAX:
            failed.append((path, f"exceeds API limit ({size:,} bytes > 100 MB)"))
            continue

        dest_path = os.path.join(dest, os.path.basename(path))
        _stream_download(download_url, dest_path)
        written.append((path, dest_path, os.path.getsize(dest_path)))

    return written, failed


# Format per-path written/failed report
def format_download_report(written: list, failed: list, dest: str) -> str:
    lines = [f"Downloaded to: {os.path.abspath(dest)}/", ""]

    lines.append(f"Written ({len(written)}):")
    if written:
        for path, dest_path, size in written:
            lines.append(f"  {os.path.basename(path)} -> {dest_path} ({size:,} bytes)")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append(f"Failed ({len(failed)}):")
    if failed:
        for path, reason in failed:
            lines.append(f"  {path} — {reason}")
    else:
        lines.append("  (none)")

    return "\n".join(lines)
