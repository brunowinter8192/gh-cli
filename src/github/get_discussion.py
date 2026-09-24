# INFRASTRUCTURE
import logging
from mcp.types import TextContent
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

def fetch_discussion(owner: str, repo: str, number: int, comment_limit: int) -> dict:
    logger.debug("Fetching discussion owner=%s repo=%s number=%s", owner, repo, number)
    variables = {
        "owner": owner,
        "repo": repo,
        "number": number,
        "commentLimit": min(comment_limit, 100)
    }
    return graphql_query(DISCUSSION_QUERY, variables)


def format_discussion(data: dict, comment_limit: int) -> str:
    d = data["repository"]["discussion"]
    if not d:
        return "Discussion not found."

    category = d["category"]
    author = d["author"]["login"]
    answered_status = "Answered" if d["isAnswered"] else "Open"

    lines = [
        f"## {d['title']}\n",
        f"**Category:** {category['emoji']} {category['name']}",
        f"**Author:** @{author}",
        f"**Created:** {d['createdAt'][:10]}",
        f"**Upvotes:** {d['upvoteCount']}",
        f"**Status:** {answered_status}\n",
        "### Body",
        d["body"],
        "\n---\n"
    ]

    answer = d["answer"]
    if answer:
        ans_author = answer["author"]["login"]
        lines.append("### Accepted Answer")
        lines.append(f"**@{ans_author}** ({answer['createdAt'][:10]}) - {answer['upvoteCount']} upvotes")
        lines.append(answer["body"])
        lines.append("\n---\n")

    comments_data = d["comments"]
    total_comments = comments_data["totalCount"]
    comments = comments_data["nodes"][:comment_limit]

    lines.append(f"### Comments ({total_comments} total, showing {len(comments)})\n")

    for c in comments:
        c_author = c["author"]["login"]
        is_answer = " [ANSWER]" if c["isAnswer"] else ""
        lines.append(f"**@{c_author}** ({c['createdAt'][:10]}) - {c['upvoteCount']} upvotes{is_answer}")
        lines.append(c["body"])

        replies = c["replies"]["nodes"]
        for r in replies:
            r_author = r["author"]["login"]
            lines.append(f"  > **@{r_author}**: {r['body']} ({r['upvoteCount']} upvotes)")

        lines.append("")

    return "\n".join(lines)
