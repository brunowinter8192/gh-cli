# INFRASTRUCTURE
import logging
import re
import subprocess
from pathlib import Path

from mcp.types import TextContent

from src.github.graphql_client import graphql_query
from src.github.get_discussion import get_discussion_workflow

logger = logging.getLogger(__name__)

RAG_ROOT    = Path("/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli")
RAG_DOC_DIR = RAG_ROOT / "data" / "documents" / "github_discussions"
COLLECTION  = "github_discussions"
DEFAULT_LIMIT = 30

FOOTER_LOOKAHEAD = 20
_BADGE_DOMAINS = frozenset([
    'shields.io/badge', 'camo.githubusercontent.com',
    'app.dosu.dev/response-feedback', 'go.dosu.dev',
])
GH_IMG_RE = re.compile(
    r'<img\s+width="\d+"\s+height="\d+"\s+alt="[^"]*"\s+'
    r'src="https://github\.com/user-attachments/assets/[a-f0-9-]+"[^>]*/?>',
    re.IGNORECASE,
)
ISSUE_HEADING_RE = re.compile(
    r'^### (?:🔎 Search before asking|🤖 Consult the online AI assistant)'
)

SEARCH_QUERY = """
query($query: String!, $first: Int!) {
  search(query: $query, type: DISCUSSION, first: $first) {
    discussionCount
    nodes {
      ... on Discussion {
        number
      }
    }
  }
}
"""


# ORCHESTRATOR

# Fetch GitHub discussions matching query + repo, write per-discussion MDs, index into RAG
def index_discussions_workflow(query: str, repo: str, limit: int = DEFAULT_LIMIT) -> list[TextContent]:
    logger.info("index_discussions query=%s repo=%s limit=%s", query, repo, limit)
    owner, repo_name = repo.split("/", 1)
    repo_basename = repo_name

    keywords = query.split()[:3]
    if not keywords:
        return [TextContent(type="text", text="Empty query — provide 1-3 keywords.")]
    total = 0
    numbers: list[int] = []
    kw_level = 0
    for k in range(len(keywords), 0, -1):
        sub_q = " ".join(keywords[:k])
        total, numbers = search_discussions_raw(sub_q, repo, limit)
        if total > 0:
            kw_level = k
            break
    if total == 0:
        return [TextContent(type="text", text=f"No discussions found for '{keywords[0]}' in {repo}.")]

    RAG_DOC_DIR.mkdir(parents=True, exist_ok=True)
    mds_written = 0
    for num in numbers:
        disc_text = get_discussion_workflow(owner, repo_name, num)[0].text
        clean, title = strip_discussion_noise(disc_text)
        md = build_discussion_md(num, title, clean)
        md = redact_tokens(md)
        (RAG_DOC_DIR / f"{repo_basename}__{num}.md").write_text(md, encoding="utf-8")
        mds_written += 1

    new_chunks = run_index()
    total_mds, total_chunks = get_collection_stats()

    fallback_note = (
        f" (fell back to {kw_level} keyword{'s' if kw_level != 1 else ''})"
        if kw_level < len(keywords) else ""
    )
    summary = (
        f"Indexed {mds_written} discussions from {repo}.\n"
        f"Query: '{query}'{fallback_note}\n"
        f"New chunks added this run: {new_chunks}\n"
        f"Collection now: {total_mds} MDs, {total_chunks} chunks total."
    )
    return [TextContent(type="text", text=summary)]


# FUNCTIONS

# Search discussions via GitHub GraphQL Search API; return (discussionCount, numbers[:limit])
def search_discussions_raw(query: str, repo: str, limit: int) -> tuple[int, list[int]]:
    scoped_query = f"{query} repo:{repo}"
    variables = {"query": scoped_query, "first": min(limit, 100)}
    data = graphql_query(SEARCH_QUERY, variables)
    search = data["search"]
    numbers = [n["number"] for n in search["nodes"] if n is not None][:limit]
    return search["discussionCount"], numbers


# Strip blockquote prefix for dosu marker detection
def _bare(line: str) -> str:
    return re.sub(r'^[\s>]+', '', line).strip()


# True if line is a dosu-feedback badge line (shields.io / camo / dosu domains)
def _is_badge_line(line: str) -> bool:
    c = _bare(line)
    has_badge = '[![' in c or c.startswith('<sup>How did I do?')
    has_dosu = any(x in c for x in _BADGE_DOMAINS)
    return has_badge and has_dosu


# Strip indexing noise from formatted discussion text; return (filtered_text, extracted_title)
def strip_discussion_noise(text: str) -> tuple[str, str]:
    METADATA_PREFIXES = (
        "**Category:**", "**Author:**", "**Created:**", "**Upvotes:**", "**Status:**",
    )
    ANSWER_COMMENT_HDR_RE = re.compile(
        r'^\*\*@\S+\*\* \(\d{4}-\d{2}-\d{2}\) - \d+ upvotes \[ANSWER\]$'
    )
    COMMENT_HDR_RE = re.compile(
        r'^\*\*@\S+\*\* \(\d{4}-\d{2}-\d{2}\) - \d+ upvotes'
    )

    title = ""
    title_extracted = False
    in_answer_comment = False
    out = []

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        bare = _bare(line)

        # (1) DOSU_FOOTER: strip <!-- Dosu Comment Footer --> ... badge line (incl.)
        if bare == '<!-- Dosu Comment Footer -->':
            badge_idx = next(
                (j for j in range(i + 1, min(i + FOOTER_LOOKAHEAD, len(lines)))
                 if _is_badge_line(lines[j])), None
            )
            if badge_idx is not None:
                block = lines[i:badge_idx + 1]
                if not any(re.search(r'^\s*>\s*\*\*@', l) for l in block):
                    i = badge_idx + 1
                    continue

        # (2) DOSU_GREETING: strip <!-- Greeting --> + next non-blank line
        if bare == '<!-- Greeting -->':
            greet_idx = next(
                (j for j in range(i + 1, min(i + 5, len(lines))) if lines[j].strip()), None
            )
            if greet_idx is not None:
                i = greet_idx + 1
                continue

        # (3) ISSUE_TEMPLATE_CHECKLIST: strip heading + consecutive checkbox/blank lines
        if ISSUE_HEADING_RE.match(line.strip()):
            j = i + 1
            while j < len(lines) and (lines[j].strip().startswith('- [') or not lines[j].strip()):
                j += 1
            i = j
            continue

        # (4) STANDALONE BADGE LINE: markerless/blockquoted/orphaned dosu badges
        #     (_is_badge_line already _bare()s the > prefix; catches quoted footer copies)
        if _is_badge_line(line):
            i += 1
            continue

        # (5) [ANSWER] comment dedup (existing behavior, unchanged)
        if ANSWER_COMMENT_HDR_RE.match(line):
            in_answer_comment = True
            i += 1
            continue
        if in_answer_comment:
            if COMMENT_HDR_RE.match(line) or line.startswith("### "):
                in_answer_comment = False
                out.append(line)
            i += 1
            continue

        # (6) Title extraction: get_discussion emits "## title", promote to H1 via build_discussion_md
        if not title_extracted and line.startswith("## "):
            title = line[3:].strip()
            title_extracted = True
            i += 1
            continue

        # (7) Metadata block drop
        if any(line.startswith(p) for p in METADATA_PREFIXES):
            i += 1
            continue

        # (8) Inline subs: DOSU_ANSWER_MARKER, GH_SCREENSHOT_IMG, FAILED_UPLOAD
        line = re.sub(r'<!--\s*Answer\s*-->', '', line)
        line = re.sub(GH_IMG_RE, '', line)
        line = re.sub(r'!\[Uploading[^\]]*\]\(\)', '', line)

        # (9) No-space safety net: remove any run of >= 1000 non-whitespace chars
        #     (URL blobs, base64, camo-proxied badge markup — never natural language)
        line = re.sub(r'\S{1000,}', '', line)

        out.append(line)
        i += 1

    return "\n".join(out), title


# Redact GitHub tokens before writing MDs to disk
def redact_tokens(text: str) -> str:
    text = re.sub(r'ghp_[A-Za-z0-9]+', '[REDACTED]', text)
    text = re.sub(r'github_pat_[A-Za-z0-9_]+', '[REDACTED]', text)
    return text


# Render one discussion as a standalone MD with H1 title
def build_discussion_md(disc_num: int, title: str, body_text: str) -> str:
    header = f"# {title}" if title else f"# Discussion #{disc_num}"
    return f"{header}\n\n{body_text}\n"


# Run rag-cli index (incremental); return new chunk count from stdout
def run_index() -> int:
    rag_cli = Path.home() / ".local" / "bin" / "rag-cli"
    result = subprocess.run(
        [str(rag_cli), "index", "--collection", COLLECTION],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip()
        busy = any(w in stderr.lower() for w in ("busy", "locked", "in use"))
        reason = "RAG server busy or DB locked" if busy else f"rag-cli index failed (exit {result.returncode})"
        raise RuntimeError(
            f"{reason} — MDs are staged, run manually when server is free: "
            f"rag-cli index --collection {COLLECTION}\nDetails: {stderr[:300]}"
        )
    return parse_chunk_count(result.stdout)


# Parse new chunk count from rag-cli index stdout
def parse_chunk_count(stdout: str) -> int:
    m = re.search(r"Done: \d+ files indexed \((\d+) chunks\)", stdout)
    return int(m.group(1)) if m else 0


# Return (md_count, total_chunks) for github_discussions collection
def get_collection_stats() -> tuple[int, int]:
    md_count = len(list(RAG_DOC_DIR.glob("*.md")))
    rag_cli = Path.home() / ".local" / "bin" / "rag-cli"
    try:
        result = subprocess.run(
            [str(rag_cli), "list_collections"],
            capture_output=True, text=True, cwd=str(RAG_ROOT),
        )
        m = re.search(r"github_discussions\s*\((\d+) chunks\)", result.stdout)
        total_chunks = int(m.group(1)) if m else 0
    except Exception as exc:
        logger.warning("index_discussions: rag-cli list_collections failed: %s", exc)
        total_chunks = 0
    return md_count, total_chunks
