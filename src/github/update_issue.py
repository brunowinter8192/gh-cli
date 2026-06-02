# INFRASTRUCTURE
import logging
from mcp.types import TextContent
from src.github.client import request

logger = logging.getLogger(__name__)


# ORCHESTRATOR
def update_issue_workflow(
    owner: str,
    repo: str,
    number: int,
    title: str | None = None,
    body: str | None = None,
    labels: list[str] | None = None,
    state: str | None = None,
    state_reason: str | None = None,
) -> list[TextContent]:
    logger.info("update_issue owner=%s repo=%s number=%s", owner, repo, number)
    issue = patch_issue(owner, repo, number, title, body, labels, state, state_reason)
    text = format_updated(issue)
    return [TextContent(type="text", text=text)]


# FUNCTIONS

def patch_issue(
    owner: str,
    repo: str,
    number: int,
    title: str | None,
    body: str | None,
    labels: list[str] | None,
    state: str | None,
    state_reason: str | None,
) -> dict:
    payload: dict = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if labels is not None:
        payload["labels"] = labels
    if state is not None:
        payload["state"] = state
    if state_reason is not None:
        payload["state_reason"] = state_reason
    return request("PATCH", f"/repos/{owner}/{repo}/issues/{number}", json=payload)


def format_updated(issue: dict) -> str:
    return (
        f"Updated #{issue['number']} — \"{issue['title']}\" [{issue['state'].upper()}]\n"
        f"{issue['html_url']}"
    )
