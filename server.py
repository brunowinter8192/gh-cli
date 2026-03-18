# INFRASTRUCTURE
from typing import Literal
from fastmcp import FastMCP
from mcp.types import TextContent

from src.github.search_repos import search_repos_workflow
from src.github.search_code import search_code_workflow
from src.github.get_repo_tree import get_repo_tree_workflow
from src.github.get_file_content import get_file_content_workflow
from src.github.grep_file import grep_file_workflow
from src.github.grep_repo import grep_repo_workflow
from src.github.search_items import search_items_workflow
from src.github.get_issue import get_issue_workflow
from src.github.get_issue_comments import get_issue_comments_workflow
from src.github.list_repo_prs import list_repo_prs_workflow
from src.github.get_pr import get_pr_workflow
from src.github.get_pr_files import get_pr_files_workflow
from src.github.get_repo import get_repo_workflow
from src.github.search_discussions import search_discussions_workflow
from src.github.list_discussions import list_discussions_workflow
from src.github.get_discussion import get_discussion_workflow
from src.github.list_commits import list_commits_workflow
from src.github.compare_commits import compare_commits_workflow
from src.github.list_releases import list_releases_workflow
from src.github.get_release import get_release_workflow

mcp = FastMCP("GitHub")


# TOOLS

@mcp.tool
def search_repos(
    query: str,
    sort_by: Literal["stars", "forks", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    """Search GitHub repositories."""
    return search_repos_workflow(query, sort_by)


@mcp.tool
def search_code(query: str) -> list[TextContent]:
    """Search code across GitHub."""
    return search_code_workflow(query)


@mcp.tool
def get_repo_tree(owner: str, repo: str, path: str = "", depth: int = -1, pattern: str = "") -> list[TextContent]:
    """Browse repository file tree."""
    return get_repo_tree_workflow(owner, repo, path, depth, pattern)


@mcp.tool
def get_file_content(owner: str, repo: str, path: str, metadata_only: bool = False, offset: int = 0, limit: int = 0) -> list[TextContent]:
    """Read file from GitHub repo."""
    return get_file_content_workflow(owner, repo, path, metadata_only, offset, limit)


@mcp.tool
def grep_file(owner: str, repo: str, path: str, pattern: str, context_lines: int = 0, max_matches: int = 50) -> list[TextContent]:
    """Regex search within a file."""
    return grep_file_workflow(owner, repo, path, pattern, context_lines, max_matches)


@mcp.tool
def grep_repo(owner: str, repo: str, pattern: str, file_pattern: str = "*", path: str = "", max_files: int = 10) -> list[TextContent]:
    """Regex search across repo files."""
    return grep_repo_workflow(owner, repo, pattern, file_pattern, path, max_files)


@mcp.tool
def search_items(
    query: str,
    type: Literal["issue", "pr"],
    sort_by: Literal["comments", "reactions", "created", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    """Search GitHub issues or PRs."""
    return search_items_workflow(query, type, sort_by)


@mcp.tool
def get_issue(owner: str, repo: str, issue_number: int) -> list[TextContent]:
    """Read GitHub issue."""
    return get_issue_workflow(owner, repo, issue_number)


@mcp.tool
def get_issue_comments(owner: str, repo: str, issue_number: int) -> list[TextContent]:
    """Read issue comments."""
    return get_issue_comments_workflow(owner, repo, issue_number)


@mcp.tool
def list_repo_prs(
    owner: str,
    repo: str,
    state: Literal["open", "closed", "all"] = "open",
    sort_by: Literal["created", "updated", "popularity", "long-running"] = "created"
) -> list[TextContent]:
    """List repository PRs."""
    return list_repo_prs_workflow(owner, repo, state, sort_by)


@mcp.tool
def get_pr(owner: str, repo: str, pull_number: int) -> list[TextContent]:
    """Read pull request details."""
    return get_pr_workflow(owner, repo, pull_number)


@mcp.tool
def get_pr_files(owner: str, repo: str, pull_number: int) -> list[TextContent]:
    """List files changed in a PR."""
    return get_pr_files_workflow(owner, repo, pull_number)


@mcp.tool
def get_repo(owner: str, repo: str) -> list[TextContent]:
    """Read repository metadata."""
    return get_repo_workflow(owner, repo)


@mcp.tool
def search_discussions(query: str, first: int = 10) -> list[TextContent]:
    """Search GitHub discussions."""
    return search_discussions_workflow(query, first)


@mcp.tool
def list_discussions(
    owner: str,
    repo: str,
    first: int = 10,
    category: str | None = None,
    answered: bool | None = None
) -> list[TextContent]:
    """List repository discussions."""
    return list_discussions_workflow(owner, repo, first, category, answered)


@mcp.tool
def get_discussion(
    owner: str,
    repo: str,
    number: int,
    comment_limit: int = 50,
    comment_sort: Literal["upvotes", "chronological"] = "upvotes"
) -> list[TextContent]:
    """Read discussion with comments."""
    return get_discussion_workflow(owner, repo, number, comment_limit, comment_sort)


@mcp.tool
def list_commits(
    owner: str,
    repo: str,
    sha: str = "",
    path: str = "",
    author: str = "",
    per_page: int = 20
) -> list[TextContent]:
    """List commit history."""
    return list_commits_workflow(owner, repo, sha, path, author, per_page)


@mcp.tool
def compare_commits(
    owner: str,
    repo: str,
    base: str,
    head: str
) -> list[TextContent]:
    """Compare branches/tags/SHAs."""
    return compare_commits_workflow(owner, repo, base, head)


@mcp.tool
def list_releases(
    owner: str,
    repo: str,
    per_page: int = 10
) -> list[TextContent]:
    """List repository releases."""
    return list_releases_workflow(owner, repo, per_page)


@mcp.tool
def get_release(
    owner: str,
    repo: str,
    tag: str | None = None
) -> list[TextContent]:
    """Read release notes."""
    return get_release_workflow(owner, repo, tag)


if __name__ == "__main__":
    mcp.run()
