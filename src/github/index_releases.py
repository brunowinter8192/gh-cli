# INFRASTRUCTURE
import logging
import re
import shutil
import subprocess
from pathlib import Path

import requests
from mcp.types import TextContent

from src.github.client import GITHUB_API_BASE, build_headers

logger = logging.getLogger(__name__)

RAG_ROOT   = Path("/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli")

COLLECTION = "github_releases"


# ORCHESTRATOR

# Fetch all releases for a repo, write per-release MDs, index into RAG
def index_releases_workflow(repo: str) -> list[TextContent]:
    logger.info("index_releases repo=%s", repo)
    owner, repo_name = repo.split("/", 1)
    collection = COLLECTION
    doc_dir = RAG_ROOT / "data" / "documents" / "github_releases"

    janitor_clean(collection, doc_dir)
    doc_dir.mkdir(parents=True)

    releases = fetch_releases(owner, repo_name)
    for r in releases:
        write_release_md(r, doc_dir)

    new_chunks = run_index(collection)
    total_mds, total_chunks = get_collection_stats(collection, doc_dir)

    summary = (
        f"Indexed {len(releases)} releases from {repo}.\n"
        f"New chunks added this run: {new_chunks}\n"
        f"Collection now: {total_mds} MDs, {total_chunks} chunks total.\n"
        f"\nTo search: rag-cli search_hybrid \"<your feature query>\" github_releases"
    )
    return [TextContent(type="text", text=summary)]


# FUNCTIONS

# Delete RAG collection and doc dir before re-indexing; raise before rmtree on failure so old state stays intact
def janitor_clean(collection: str, doc_dir: Path) -> None:
    rag_cli = Path.home() / ".local" / "bin" / "rag-cli"
    result = subprocess.run(
        [str(rag_cli), "delete", "--collection", collection],
        capture_output=True, text=True, cwd=str(RAG_ROOT),
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        busy = any(w in stderr.lower() for w in ("busy", "locked", "in use"))
        reason = "RAG server busy or DB locked" if busy else f"rag-cli delete failed (exit {result.returncode})"
        raise RuntimeError(
            f"{reason} — cannot wipe collection '{collection}' before re-index. "
            f"Details: {stderr[:300]}"
        )
    shutil.rmtree(doc_dir, ignore_errors=True)


# Fetch up to 100 releases newest-first from GitHub REST API
def fetch_releases(owner: str, repo: str) -> list:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases"
    response = requests.get(url, params={"per_page": 100}, headers=build_headers())
    response.raise_for_status()
    return response.json()


# Remove changelog boilerplate from release body
def strip_release_noise(body: str) -> str:
    out = []
    skip_section = False
    for line in body.splitlines():
        if re.match(r"^## New Contributors", line, re.IGNORECASE):
            skip_section = True
            continue
        if skip_section:
            if re.match(r"^##", line):
                skip_section = False
            else:
                continue
        if re.match(r"^## What.s [Cc]hanged", line, re.IGNORECASE):
            continue
        if re.match(r"^\*\*Full Changelog\*\*:", line):
            continue
        line = re.sub(r"\s+by @\S+ in (?:#\d+|https?://\S+)", "", line)
        out.append(line)
    return "\n".join(out).strip()


# Write one release as a standalone MD file
def write_release_md(r: dict, doc_dir: Path) -> None:
    tag = (r.get("tag_name") or "untagged").strip() or "untagged"
    published = (r.get("published_at") or "")[:10] or "unknown"
    body = strip_release_noise((r.get("body") or "").strip())
    md = f"# {tag} ({published})\n\n{body}\n"
    filename = sanitize_filename(tag) + ".md"
    (doc_dir / filename).write_text(md, encoding="utf-8")


# Replace filename-unsafe chars with hyphens
def sanitize_filename(tag: str) -> str:
    return re.sub(r'[/\\:*?"<>|]', "-", tag).strip("- ")


# Run rag-cli index (incremental); return new chunk count from stdout
def run_index(collection: str) -> int:
    rag_cli = Path.home() / ".local" / "bin" / "rag-cli"
    result = subprocess.run(
        [str(rag_cli), "index", "--collection", collection],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        busy = any(w in stderr.lower() for w in ("busy", "locked", "in use"))
        reason = "RAG server busy or DB locked" if busy else f"rag-cli index failed (exit {result.returncode})"
        raise RuntimeError(
            f"{reason} — MDs are staged, run manually when server is free: "
            f"rag-cli index --collection {collection}\nDetails: {stderr[:300]}"
        )
    return parse_chunk_count(result.stdout)


# Parse new chunk count from rag-cli index stdout
def parse_chunk_count(stdout: str) -> int:
    m = re.search(r"Done: \d+ files indexed \((\d+) chunks\)", stdout)
    return int(m.group(1)) if m else 0


# Return (md_count, total_chunks) for the releases collection
def get_collection_stats(collection: str, doc_dir: Path) -> tuple[int, int]:
    md_count = len(list(doc_dir.glob("*.md")))
    rag_cli = Path.home() / ".local" / "bin" / "rag-cli"
    try:
        result = subprocess.run(
            [str(rag_cli), "list_collections"],
            capture_output=True, text=True, cwd=str(RAG_ROOT),
        )
        m = re.search(rf"{re.escape(collection)}\s*\((\d+) chunks\)", result.stdout)
        total_chunks = int(m.group(1)) if m else 0
    except Exception as exc:
        logger.warning("index_releases: rag-cli list_collections failed: %s", exc)
        total_chunks = 0
    return md_count, total_chunks
