"""
Probe: GitHub GraphQL API — repo tree traversal in one round-trip.

Tree-only, depth=1. Fetches per-entry: name, type, language, lineCount, size.
Repository metadata (description, primaryLanguage, languages) printed only for root
expressions (path component after ":" is empty, e.g. "HEAD:").
If expression resolves to a Blob, prints a redirect message — does NOT read content.

Usage (from project root):
  .venv/bin/python dev/repo_exploration/probe_graphql_explore.py <owner> <repo> [expression]
  # expression examples: "HEAD:" (root), "HEAD:plugins/" (subtree)
"""
# INFRASTRUCTURE
import argparse
from probe_client import graphql_query

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
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("owner")
    parser.add_argument("repo")
    parser.add_argument("expression", nargs="?", default="HEAD:",
                        help='Git expression (default: "HEAD:" = root tree)')
    args = parser.parse_args()
    print(fetch_and_print(args.owner, args.repo, args.expression))


# FUNCTIONS

# Execute GraphQL query and return formatted string
def fetch_and_print(owner: str, repo: str, expression: str) -> str:
    data = graphql_query(_QUERY, {"owner": owner, "name": repo, "expression": expression})
    repo_data = data["repository"]
    lines = []

    is_root = expression.split(":", 1)[1] == ""
    if is_root:
        lines.append(f"description:     {repo_data.get('description') or '(none)'}")
        primary = (repo_data.get("primaryLanguage") or {}).get("name", "(none)")
        lines.append(f"primaryLanguage: {primary}")
        lang_edges = (repo_data.get("languages") or {}).get("edges", [])
        if lang_edges:
            total_bytes = sum(e["size"] for e in lang_edges)
            lang_parts = [
                f"{e['node']['name']} {e['size'] / total_bytes * 100:.0f}%"
                for e in lang_edges
            ]
            lines.append(f"languages:       {', '.join(lang_parts)}")
        lines.append(f"expression:      {expression}")
        lines.append("")

    obj = repo_data.get("object")
    if obj is None:
        lines.append("object: null — path not found or not accessible")
        return "\n".join(lines)

    typename = obj.get("__typename")

    if typename == "Blob":
        lines.append(f"{expression} is a file — use get_file_content to read it")
        return "\n".join(lines)

    lines.append(f"type: {typename}")
    lines.append("")
    lines.append(format_tree(obj.get("entries", [])))

    return "\n".join(lines)


# Format tree entries as a table
def format_tree(entries: list) -> str:
    if not entries:
        return "(empty tree)"
    rows = []
    rows.append(f"  {'name':<40} {'type':<6} {'lang':<16} {'lines':>7} {'size':>9}")
    rows.append("  " + "-" * 82)
    for e in entries:
        lang = (e.get("language") or {}).get("name") or "-"
        lc = e.get("lineCount")
        lines_str = str(lc) if lc is not None else "-"
        sz = e.get("size")
        sz_str = f"{sz:,}" if sz is not None else "-"
        rows.append(
            f"  {e['name']:<40} {e['type']:<6} {lang:<16} {lines_str:>7} {sz_str:>9}"
        )
    return "\n".join(rows)


if __name__ == "__main__":
    main()
