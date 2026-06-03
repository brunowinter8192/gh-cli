"""
Probe: GitHub GraphQL API — repository structure + metadata + content in one round-trip.

Query fetches:
  - repository.description, primaryLanguage, languages (top-10 by size)
  - repository.object(expression) dispatched on __typename:
      Tree  → entries{name, type, path, extension, lineCount, size, language}
      Blob  → text (UTF-8), byteSize, isBinary

Default expression "HEAD:" returns root tree. Pass a path for subtrees or files:
  HEAD:src/           → tree of src/ directory
  HEAD:README.md      → blob (file content)
  HEAD:src/main.py    → blob

Demonstrates: one GraphQL call gives structure WITH per-entry language+lineCount that
the REST Git Trees API (/git/trees?recursive) cannot provide.

Usage (from project root):
  .venv/bin/python dev/repo_exploration/probe_graphql_explore.py <owner> <repo> [expression]
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
          path
          extension
          lineCount
          size
          language {
            name
          }
        }
      }
      ... on Blob {
        text
        byteSize
        isBinary
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
    lines.append(f"type: {typename}")
    lines.append("")

    if typename == "Tree":
        lines.append(format_tree(obj.get("entries", [])))
    elif typename == "Blob":
        lines.append(format_blob(obj))

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


# Format blob content (first 40 lines or binary notice)
def format_blob(obj: dict) -> str:
    if obj.get("isBinary"):
        return f"(binary blob, {obj.get('byteSize', '?')} bytes)"
    text = obj.get("text") or ""
    content_lines = text.splitlines()
    preview = "\n".join(content_lines[:40])
    suffix = f"\n... ({len(content_lines) - 40} more lines)" if len(content_lines) > 40 else ""
    return f"{preview}{suffix}"


if __name__ == "__main__":
    main()
