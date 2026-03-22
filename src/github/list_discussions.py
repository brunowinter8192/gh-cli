# INFRASTRUCTURE
import logging
from mcp.types import TextContent
from src.github.graphql_client import graphql_query

logger = logging.getLogger(__name__)

CATEGORIES_QUERY = """
query($owner: String!, $repo: String!) {
  repository(owner: $owner, name: $repo) {
    discussionCategories(first: 20) {
      nodes {
        id
        name
        slug
        emoji
      }
    }
  }
}
"""

LIST_QUERY = """
query($owner: String!, $repo: String!, $first: Int!, $answered: Boolean, $categoryId: ID) {
  repository(owner: $owner, name: $repo) {
    discussions(
      first: $first,
      orderBy: {field: UPDATED_AT, direction: DESC},
      answered: $answered,
      categoryId: $categoryId
    ) {
      nodes {
        number
        title
        category { name emoji slug }
        author { login }
        comments { totalCount }
        upvoteCount
        isAnswered
        url
        createdAt
        updatedAt
      }
    }
  }
}
"""


# ORCHESTRATOR
def list_discussions_workflow(
    owner: str,
    repo: str,
    first: int = 10,
    category: str | None = None,
    answered: bool | None = None
) -> list[TextContent]:
    logger.info("list_discussions owner=%s repo=%s", owner, repo)
    category_id = None
    if category:
        category_id = lookup_category_id(owner, repo, category)

    raw_data = fetch_discussions(owner, repo, first, category_id, answered)
    formatted = format_results(owner, repo, raw_data)
    return [TextContent(type="text", text=formatted)]


# FUNCTIONS

# Lookup category ID by slug
def lookup_category_id(owner: str, repo: str, slug: str) -> str | None:
    logger.debug("Fetching categories owner=%s repo=%s", owner, repo)
    variables = {"owner": owner, "repo": repo}
    data = graphql_query(CATEGORIES_QUERY, variables)
    categories = data["repository"]["discussionCategories"]["nodes"]

    for cat in categories:
        if cat["slug"] == slug:
            return cat["id"]
    return None


# Fetch discussions from repository
def fetch_discussions(
    owner: str,
    repo: str,
    first: int,
    category_id: str | None,
    answered: bool | None
) -> dict:
    logger.debug("Fetching discussions owner=%s repo=%s", owner, repo)
    variables = {
        "owner": owner,
        "repo": repo,
        "first": min(first, 100),
        "categoryId": category_id,
        "answered": answered
    }
    return graphql_query(LIST_QUERY, variables)


# Format discussions list for display
def format_results(owner: str, repo: str, data: dict) -> str:
    nodes = data["repository"]["discussions"]["nodes"]

    lines = [f"## Discussions in {owner}/{repo}\n"]

    if not nodes:
        lines.append("No discussions found.")
        return "\n".join(lines)

    for idx, d in enumerate(nodes, 1):
        category = d.get("category") or {}
        emoji = category.get("emoji", "")
        cat_name = category.get("name", "")
        author = (d.get("author") or {}).get("login", "unknown")
        comments = (d.get("comments") or {}).get("totalCount", 0)
        answered = "Yes" if d.get("isAnswered") else "No"
        updated = d.get("updatedAt", "")[:10]

        lines.append(f"{idx}. **{d['title']}** [{emoji} {cat_name}]")
        lines.append(f"   Author: @{author} | Comments: {comments} | Upvotes: {d.get('upvoteCount', 0)}")
        lines.append(f"   Answered: {answered} | Updated: {updated}")
        lines.append(f"   ID: #{d['number']}")
        lines.append("")

    return "\n".join(lines)
