# INFRASTRUCTURE
import logging
import sys
from mcp.types import TextContent
from src.github.client import request
from src.github.graphql_client import graphql_query

logger = logging.getLogger(__name__)

_DELETE_MUTATION = """
mutation DeleteIssue($input: DeleteIssueInput!) {
  deleteIssue(input: $input) {
    repository {
      name
    }
  }
}
"""


# ORCHESTRATOR
def delete_issue_workflow(owner: str, repo: str, number: int, confirm: bool) -> list[TextContent]:
    logger.info("delete_issue owner=%s repo=%s number=%s confirm=%s", owner, repo, number, confirm)
    issue = fetch_issue_meta(owner, repo, number)
    title = issue["title"]
    node_id = issue["node_id"]

    if not confirm:
        text = (
            f"Would delete issue #{number}: \"{title}\"\n"
            f"{issue['html_url']}\n\n"
            "This is irreversible. Re-run with --confirm to actually delete."
        )
        return [TextContent(type="text", text=text)]

    print(
        f"WARNING: Permanently deleting issue #{number}: \"{title}\" — this cannot be undone.",
        file=sys.stderr,
    )
    graphql_query(_DELETE_MUTATION, {"input": {"issueId": node_id}})
    return [TextContent(type="text", text=f"Issue #{number} permanently deleted.")]


# FUNCTIONS

def fetch_issue_meta(owner: str, repo: str, number: int) -> dict:
    return request("GET", f"/repos/{owner}/{repo}/issues/{number}")
