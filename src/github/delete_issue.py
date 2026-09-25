# INFRASTRUCTURE
import logging
import sys
from mcp.types import TextContent
from src.github.client import request
from src.github.graphql_client import graphql_query
from src.github.response import text_response

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
    if not confirm:
        return text_response(build_dry_run_message(number, issue))
    warn_permanent_delete(number, issue)
    send_delete_mutation(issue)
    return text_response(build_deleted_message(number))


# FUNCTIONS

def fetch_issue_meta(owner: str, repo: str, number: int) -> dict:
    return request("GET", f"/repos/{owner}/{repo}/issues/{number}")


def build_dry_run_message(number: int, issue: dict) -> str:
    return (
        f"Would delete issue #{number}: \"{issue['title']}\"\n"
        f"{issue['html_url']}\n\n"
        "This is irreversible. Re-run with --confirm to actually delete."
    )


def warn_permanent_delete(number: int, issue: dict) -> None:
    print(
        f"WARNING: Permanently deleting issue #{number}: \"{issue['title']}\" — this cannot be undone.",
        file=sys.stderr,
    )


def send_delete_mutation(issue: dict) -> None:
    graphql_query(_DELETE_MUTATION, {"input": {"issueId": issue["node_id"]}})


def build_deleted_message(number: int) -> str:
    return f"Issue #{number} permanently deleted."
