# INFRASTRUCTURE
import logging
from mcp.types import TextContent
from src.github.client import request

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def comment_issue_workflow(owner: str, repo: str, number: int, body: str) -> list[TextContent]:
    logger.info("comment_issue owner=%s repo=%s number=%s", owner, repo, number)
    comment = post_comment(owner, repo, number, body)
    text = f"Comment added to issue #{number}\n{comment['html_url']}"
    return [TextContent(type="text", text=text)]


# FUNCTIONS

def post_comment(owner: str, repo: str, number: int, body: str) -> dict:
    return request(
        "POST",
        f"/repos/{owner}/{repo}/issues/{number}/comments",
        json={"body": body},
    )
