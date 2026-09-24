# INFRASTRUCTURE
import logging
from mcp.types import TextContent
from src.github.graphql_client import graphql_query

logger = logging.getLogger(__name__)

_QUERY = """
query ExploreRepo($owner: String!, $name: String!, $expression: String!) {
  repository(owner: $owner, name: $name) {
    description
    primaryLanguage {
      name
    }
    languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
      edges {
        size
        node {
          name
        }
      }
    }
    object(expression: $expression) {
      __typename
      ... on Tree {
        entries {
          name
          type
          lineCount
          size
          language {
            name
          }
        }
      }
    }
  }
}
""".strip()


# ORCHESTRATOR
def get_repo_tree_workflow(owner: str, repo: str, path: str = "") -> list[TextContent]:
    logger.info("get_repo_tree owner=%s repo=%s path=%s", owner, repo, path)
    text = fetch_and_format(owner, repo, path)
    return [TextContent(type="text", text=text)]


# FUNCTIONS

def build_expression(path: str) -> str:
    if not path:
        return "HEAD:"
    return "HEAD:" + path.strip("/") + "/"


def fetch_and_format(owner: str, repo: str, path: str) -> str:
    expression = build_expression(path)
    data = graphql_query(_QUERY, {"owner": owner, "name": repo, "expression": expression})
    repo_data = data["repository"]
    lines = []

    is_root = not path
    if is_root:
        lines.append(f"description:     {require_present(repo_data['description'], 'description')}")
        lines.append(f"primaryLanguage: {require_present(repo_data['primaryLanguage'], 'primaryLanguage')['name']}")
        lang_edges = repo_data["languages"]["edges"]
        if lang_edges:
            total_bytes = sum(e["size"] for e in lang_edges)
            lang_parts = [
                f"{e['node']['name']} {e['size'] / total_bytes * 100:.0f}%"
                for e in lang_edges
            ]
            lines.append(f"languages:       {', '.join(lang_parts)}")
        lines.append("")

    obj = repo_data["object"]
    if obj is None:
        lines.append("object: null — path not found or not accessible")
        return "\n".join(lines)

    typename = obj["__typename"]

    if typename == "Blob":
        lines.append(f"{path} is a file — use get_file_content to read it")
        return "\n".join(lines)

    lines.append(f"type: {typename}")
    lines.append("")
    lines.append(format_tree(obj["entries"]))

    return "\n".join(lines)


def require_present(value, field: str):
    if value is None:
        raise RuntimeError(f"get_repo_tree: {field} is null, payload shape not seen before")
    return value


def format_tree(entries: list) -> str:
    if not entries:
        return "(empty tree)"
    rows = []
    rows.append(f"  {'name':<40} {'type':<6} {'lang':<16} {'lines':>7} {'size':>9}")
    rows.append("  " + "-" * 82)
    for e in entries:
        lang = e["language"]["name"] if e["language"] else "-"
        lc = e["lineCount"]
        lines_str = str(lc) if lc is not None else "-"
        sz_str = f"{e['size']:,}"
        rows.append(
            f"  {e['name']:<40} {e['type']:<6} {lang:<16} {lines_str:>7} {sz_str:>9}"
        )
    return "\n".join(rows)
