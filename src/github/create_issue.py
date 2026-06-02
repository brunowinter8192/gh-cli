# INFRASTRUCTURE
import logging
from mcp.types import TextContent
from src.github.client import request

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def create_issue_workflow(
    owner: str,
    repo: str,
    title: str,
    body: str | None = None,
    labels: list[str] | None = None,
    assignees: list[str] | None = None,
) -> list[TextContent]:
    logger.info("create_issue owner=%s repo=%s title=%s", owner, repo, title)
    issue = post_issue(owner, repo, title, body, labels, assignees)
    text = format_created(issue)
    return [TextContent(type="text", text=text)]


# FUNCTIONS

def post_issue(
    owner: str,
    repo: str,
    title: str,
    body: str | None,
    labels: list[str] | None,
    assignees: list[str] | None,
) -> dict:
    payload: dict = {"title": title}
    if body is not None:
        payload["body"] = body
    if labels:
        payload["labels"] = labels
    if assignees:
        payload["assignees"] = assignees
    return request("POST", f"/repos/{owner}/{repo}/issues", json=payload)


def format_created(issue: dict) -> str:
    return f"Created issue #{issue['number']}: {issue['title']}\n{issue['html_url']}"
