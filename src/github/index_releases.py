# INFRASTRUCTURE
import logging
import re
import shutil
import subprocess
from pathlib import Path

import requests
from mcp.types import TextContent

from src.github.client import GITHUB_API_BASE, build_headers
from src.github.config import RAG_ROOT, RAG_CLI
from src.github.query_common import split_repo
from src.github.response import text_response
from src.github.rag_indexing import run_index, get_collection_stats

logger = logging.getLogger(__name__)

COLLECTION = "github_releases"
DOC_DIR = RAG_ROOT / "data" / "documents" / "github_releases"


# ORCHESTRATOR

def index_releases_workflow(repo: str) -> list[TextContent]:
    logger.info("index_releases repo=%s", repo)
    owner, repo_name = split_repo(repo)

    janitor_clean(COLLECTION, DOC_DIR)
    create_doc_dir(DOC_DIR)
    releases = fetch_releases(owner, repo_name)
    write_release_mds(releases, DOC_DIR)

    new_chunks = run_index(COLLECTION)
    total_mds, total_chunks = get_collection_stats(COLLECTION, DOC_DIR)

    summary = build_releases_summary(len(releases), repo, new_chunks, total_mds, total_chunks)
    return text_response(summary)


# FUNCTIONS

def janitor_clean(collection: str, doc_dir: Path) -> None:
    result = subprocess.run(
        [str(RAG_CLI), "delete", "--collection", collection],
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
    if doc_dir.exists():
        shutil.rmtree(doc_dir)


def create_doc_dir(doc_dir: Path) -> None:
    doc_dir.mkdir(parents=True)


def fetch_releases(owner: str, repo: str) -> list:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases"
    response = requests.get(url, params={"per_page": 100}, headers=build_headers())
    response.raise_for_status()
    return response.json()


def write_release_mds(releases: list, doc_dir: Path) -> None:
    for r in releases:
        write_release_md(r, doc_dir)


def write_release_md(r: dict, doc_dir: Path) -> None:
    tag = r["tag_name"].strip()
    published = r["published_at"][:10]
    body = strip_release_noise(r["body"].strip())
    md = f"# {tag} ({published})\n\n{body}\n"
    filename = sanitize_filename(tag) + ".md"
    (doc_dir / filename).write_text(md, encoding="utf-8")


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


def sanitize_filename(tag: str) -> str:
    return re.sub(r'[/\\:*?"<>|]', "-", tag).strip("- ")


def build_releases_summary(release_count: int, repo: str, new_chunks: int, total_mds: int, total_chunks: int) -> str:
    return (
        f"Indexed {release_count} releases from {repo}.\n"
        f"New chunks added this run: {new_chunks}\n"
        f"Collection now: {total_mds} MDs, {total_chunks} chunks total.\n"
        f"\nNewest release: rag-cli list_documents github_releases, then rag-cli expand_chunks github_releases <newest-release>.md 0 --after 2\n"
        f"Since when feature X exists: rag-cli search \"<feature>\" github_releases"
    )
