# INFRASTRUCTURE
import logging
from mcp.types import TextContent
from src.github.graphql_client import graphql_query

logger = logging.getLogger(__name__)

SEARCH_QUERY = """
query($query: String!, $first: Int!) {
  search(query: $query, type: DISCUSSION, first: $first) {
    discussionCount
    nodes {
      ... on Discussion {
        number
        title
        bodyText
        repository { nameWithOwner }
        author { login }
        category { name emoji }
        comments { totalCount }
        upvoteCount
        isAnswered
        url
        createdAt
      }
    }
  }
}
"""


# ORCHESTRATOR
def search_discussions_workflow(query: str, first: int = 10) -> list[TextContent]:
    logger.info("search_discussions query=%s", query)
    raw_data = fetch_discussions(query, first)
    formatted = format_results(raw_data)
    return [TextContent(type="text", text=formatted)]


# FUNCTIONS

# Fetch discussions via GitHub GraphQL Search API
def fetch_discussions(query: str, first: int) -> dict:
    logger.debug("Fetching discussions query=%s", query)
    variables = {"query": query, "first": min(first, 100)}
    return graphql_query(SEARCH_QUERY, variables)


# Format search results for display
def format_results(data: dict) -> str:
    search = data["search"]
    total = search["discussionCount"]
    nodes = search["nodes"]

    lines = [f"## Discussions ({total} total)\n"]

    if not nodes:
        lines.append("No discussions found.")
        return "\n".join(lines)

    for idx, d in enumerate(nodes, 1):
        if d is None:
            continue
        category = d.get("category") or {}
        emoji = category.get("emoji", "")
        cat_name = category.get("name", "")
        author = (d.get("author") or {}).get("login", "unknown")
        repo = (d.get("repository") or {}).get("nameWithOwner", "")
        comments = (d.get("comments") or {}).get("totalCount", 0)
        answered = "Yes" if d.get("isAnswered") else "No"

        lines.append(f"{idx}. **{d['title']}** [{emoji} {cat_name}]")
        lines.append(f"   Repo: {repo}")
        lines.append(f"   Author: @{author} | Comments: {comments} | Upvotes: {d.get('upvoteCount', 0)}")
        lines.append(f"   Answered: {answered}")
        lines.append(f"   URL: {d.get('url', '')}")
        lines.append("")

    return "\n".join(lines)
