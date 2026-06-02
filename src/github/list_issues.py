# INFRASTRUCTURE
import logging
from mcp.types import TextContent
from src.github.client import request

logger = logging.getLogger(__name__)

_PER_PAGE = 100


# ORCHESTRATOR
def list_issues_workflow(
    owner: str,
    repo: str,
    state: str = "open",
    labels: str | None = None,
    limit: int = 30,
) -> list[TextContent]:
    logger.info("list_issues owner=%s repo=%s state=%s", owner, repo, state)
    issues = fetch_issues(owner, repo, state, labels, limit)
    text = format_issues(issues, owner, repo, state)
    return [TextContent(type="text", text=text)]


# FUNCTIONS

def fetch_issues(
    owner: str,
    repo: str,
    state: str,
    labels: str | None,
    limit: int,
) -> list[dict]:
    params: dict = {"state": state, "per_page": min(limit, _PER_PAGE)}
    if labels:
        params["labels"] = labels

    issues = []
    page = 1
    while len(issues) < limit:
        params["page"] = page
        page_data = request("GET", f"/repos/{owner}/{repo}/issues", params=params)
        if not page_data:
            break
        # REST list also returns PRs — filter them out
        real_issues = [i for i in page_data if "pull_request" not in i]
        issues.extend(real_issues)
        if len(page_data) < params["per_page"]:
            break
        page += 1

    return issues[:limit]


def format_issues(issues: list[dict], owner: str, repo: str, state: str) -> str:
    if not issues:
        return f"No {state} issues found in {owner}/{repo}."

    lines = [f"{owner}/{repo} — {state.upper()} issues ({len(issues)} shown)\n"]
    for issue in issues:
        labels = ", ".join(lbl["name"] for lbl in issue.get("labels", []))
        label_str = f"  [{labels}]" if labels else ""
        lines.append(f"#{issue['number']:>4}  [{issue['state'].upper()}]  {issue['title']}{label_str}")
    return "\n".join(lines)
