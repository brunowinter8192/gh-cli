# INFRASTRUCTURE
import logging
import re
import subprocess
from pathlib import Path

from src.github.config import RAG_CLI, RAG_ROOT
from src.github.query_common import build_fallback_note

logger = logging.getLogger(__name__)


# FUNCTIONS

def run_index(collection: str) -> int:
    result = subprocess.run(
        [str(RAG_CLI), "index", "--collection", collection],
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


def parse_chunk_count(stdout: str) -> int:
    if "Nothing to index." in stdout:
        logger.info("rag-cli index: nothing to index, all files unchanged")
        return 0
    m = re.search(r"Done: \d+ files indexed \((\d+) chunks\)", stdout)
    if m is None:
        raise RuntimeError(f"Unrecognised rag-cli index output: {stdout[-300:]}")
    return int(m.group(1))


def get_collection_stats(collection: str, doc_dir: Path) -> tuple[int, int]:
    md_count = len(list(doc_dir.glob("*.md")))
    result = subprocess.run(
        [str(RAG_CLI), "list_collections"],
        capture_output=True, text=True, cwd=str(RAG_ROOT),
    )
    m = re.search(rf"{re.escape(collection)}\s*\((\d+) chunks\)", result.stdout)
    if m is None:
        raise RuntimeError(f"Collection {collection} not found in rag-cli list_collections output: {result.stdout[-300:]}")
    return md_count, int(m.group(1))


def build_index_summary(
    noun: str, mds_written: int, repo: str, query: str, kw_level: int, keywords: list[str],
    new_chunks: int, total_mds: int, total_chunks: int,
) -> str:
    return (
        f"Indexed {mds_written} {noun} from {repo}.\n"
        f"Query: '{query}'{build_fallback_note(kw_level, keywords)}\n"
        f"New chunks added this run: {new_chunks}\n"
        f"Collection now: {total_mds} MDs, {total_chunks} chunks total."
    )
