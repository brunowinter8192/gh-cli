# INFRASTRUCTURE
import logging
from mcp.types import TextContent
# From graphql_client.py: execute GraphQL query against GitHub API
from src.github.graphql_client import graphql_query

logger = logging.getLogger(__name__)

DISCUSSION_QUERY = """
query($owner: String!, $repo: String!, $number: Int!, $commentLimit: Int!) {
  repository(owner: $owner, name: $repo) {
    discussion(number: $number) {
      title
      body
      author { login }
      category { name emoji isAnswerable }
      upvoteCount
      createdAt
      updatedAt
      isAnswered
      answer {
        body
        author { login }
        createdAt
        upvoteCount
        url
      }
      comments(first: $commentLimit) {
        totalCount
        nodes {
          body
          author { login }
          createdAt
          isAnswer
          upvoteCount
          url
          replies(first: 5) {
            nodes {
              body
              author { login }
              createdAt
              upvoteCount
            }
          }
        }
      }
    }
  }
}
"""


# ORCHESTRATOR
def get_discussion_workflow(
    owner: str,
    repo: str,
    number: int,
    comment_limit: int = 100
) -> list[TextContent]:
    logger.info("get_discussion owner=%s repo=%s number=%s", owner, repo, number)
    raw_data = fetch_discussion(owner, repo, number, comment_limit)
    formatted = format_discussion(raw_data, comment_limit)
    return [TextContent(type="text", text=formatted)]


# FUNCTIONS

# Fetch single discussion with comments
def fetch_discussion(owner: str, repo: str, number: int, comment_limit: int) -> dict:
    logger.debug("Fetching discussion owner=%s repo=%s number=%s", owner, repo, number)
    variables = {
        "owner": owner,
        "repo": repo,
        "number": number,
        "commentLimit": min(comment_limit, 100)
    }
    return graphql_query(DISCUSSION_QUERY, variables)


# Format discussion for display
def format_discussion(data: dict, comment_limit: int) -> str:
    d = data["repository"]["discussion"]
    if not d:
        return "Discussion not found."

    category = d.get("category") or {}
    author = (d.get("author") or {}).get("login", "unknown")
    answered_status = "Answered" if d.get("isAnswered") else "Open"

    lines = [
        f"## {d['title']}\n",
        f"**Category:** {category.get('emoji', '')} {category.get('name', '')}",
        f"**Author:** @{author}",
        f"**Created:** {d.get('createdAt', '')[:10]}",
        f"**Upvotes:** {d.get('upvoteCount', 0)}",
        f"**Status:** {answered_status}\n",
        "### Body",
        d.get("body", ""),
        "\n---\n"
    ]

    answer = d.get("answer")
    if answer:
        ans_author = (answer.get("author") or {}).get("login", "unknown")
        lines.append("### Accepted Answer")
        lines.append(f"**@{ans_author}** ({answer.get('createdAt', '')[:10]}) - {answer.get('upvoteCount', 0)} upvotes")
        lines.append(answer.get("body", ""))
        lines.append("\n---\n")

    comments_data = d.get("comments") or {}
    total_comments = comments_data.get("totalCount", 0)
    comments = (comments_data.get("nodes") or [])[:comment_limit]

    lines.append(f"### Comments ({total_comments} total, showing {len(comments)})\n")

    for c in comments:
        c_author = (c.get("author") or {}).get("login", "unknown")
        is_answer = " [ANSWER]" if c.get("isAnswer") else ""
        lines.append(f"**@{c_author}** ({c.get('createdAt', '')[:10]}) - {c.get('upvoteCount', 0)} upvotes{is_answer}")
        lines.append(c.get("body", ""))

        replies = (c.get("replies") or {}).get("nodes") or []
        for r in replies:
            r_author = (r.get("author") or {}).get("login", "unknown")
            lines.append(f"  > **@{r_author}**: {r.get('body', '')} ({r.get('upvoteCount', 0)} upvotes)")

        lines.append("")

    return "\n".join(lines)
