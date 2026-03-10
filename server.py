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
    """Search repos. Use when user wants to find projects, libraries, or frameworks."""
    return search_repos_workflow(query, sort_by)


@mcp.tool
def search_code(query: str) -> list[TextContent]:
    """Search code. Use to find implementation patterns or usage examples across GitHub."""
    return search_code_workflow(query)


@mcp.tool
def get_repo_tree(owner: str, repo: str, path: str = "", depth: int = -1, pattern: str = "") -> list[TextContent]:
    """Get repo tree. Use to browse repository structure before reading specific files."""
    return get_repo_tree_workflow(owner, repo, path, depth, pattern)


@mcp.tool
def get_file_content(owner: str, repo: str, path: str, metadata_only: bool = False, offset: int = 0, limit: int = 0) -> list[TextContent]:
    """Get file content. Use after browsing repo tree to read specific files."""
    return get_file_content_workflow(owner, repo, path, metadata_only, offset, limit)


@mcp.tool
def grep_file(owner: str, repo: str, path: str, pattern: str, context_lines: int = 0, max_matches: int = 50) -> list[TextContent]:
    """Search file content by regex pattern. Use to find specific lines without downloading entire file."""
    return grep_file_workflow(owner, repo, path, pattern, context_lines, max_matches)


@mcp.tool
def grep_repo(owner: str, repo: str, pattern: str, file_pattern: str = "*.csv", path: str = "", max_files: int = 10) -> list[TextContent]:
    """Search file content across repo by file pattern. Use when search_code fails on data files."""
    return grep_repo_workflow(owner, repo, pattern, file_pattern, path, max_files)


@mcp.tool
def search_items(
    query: str,
    type: Literal["issue", "pr"],
    sort_by: Literal["comments", "reactions", "created", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    """Search issues or PRs. Use to find bug reports, feature requests, or code changes."""
    return search_items_workflow(query, type, sort_by)


@mcp.tool
def get_issue(owner: str, repo: str, issue_number: int) -> list[TextContent]:
    """Get issue. Use to read full issue details including description."""
    return get_issue_workflow(owner, repo, issue_number)


@mcp.tool
def get_issue_comments(owner: str, repo: str, issue_number: int) -> list[TextContent]:
    """Get issue comments. Use to read the discussion thread on an issue."""
    return get_issue_comments_workflow(owner, repo, issue_number)


@mcp.tool
def list_repo_prs(
    owner: str,
    repo: str,
    state: Literal["open", "closed", "all"] = "open",
    sort_by: Literal["created", "updated", "popularity", "long-running"] = "created"
) -> list[TextContent]:
    """List repo PRs. Use to see recent activity or pending changes in a repository."""
    return list_repo_prs_workflow(owner, repo, state, sort_by)


@mcp.tool
def get_pr(owner: str, repo: str, pull_number: int) -> list[TextContent]:
    """Get PR. Use to read PR details including description and merge status."""
    return get_pr_workflow(owner, repo, pull_number)


@mcp.tool
def get_pr_files(owner: str, repo: str, pull_number: int) -> list[TextContent]:
    """Get PR files. Use to see which files were changed in a pull request."""
    return get_pr_files_workflow(owner, repo, pull_number)


@mcp.tool
def get_repo(owner: str, repo: str) -> list[TextContent]:
    """Get repo metadata. Use to read repository details including topics and license."""
    return get_repo_workflow(owner, repo)


@mcp.tool
def search_discussions(query: str, first: int = 10) -> list[TextContent]:
    """Search discussions. Use to find Q&A, ideas, or community conversations across GitHub."""
    return search_discussions_workflow(query, first)


@mcp.tool
def list_discussions(
    owner: str,
    repo: str,
    first: int = 10,
    category: str | None = None,
    answered: bool | None = None
) -> list[TextContent]:
    """List repo discussions. Use to browse discussions in a specific repository."""
    return list_discussions_workflow(owner, repo, first, category, answered)


@mcp.tool
def get_discussion(
    owner: str,
    repo: str,
    number: int,
    comment_limit: int = 50,
    comment_sort: Literal["upvotes", "chronological"] = "upvotes"
) -> list[TextContent]:
    """Get discussion. Use to read full discussion with comments sorted by upvotes."""
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
    """List commits. Use to browse commit history or find when changes were introduced."""
    return list_commits_workflow(owner, repo, sha, path, author, per_page)


@mcp.tool
def compare_commits(
    owner: str,
    repo: str,
    base: str,
    head: str
) -> list[TextContent]:
    """Compare two branches, tags, or SHAs. Use to see changes between versions."""
    return compare_commits_workflow(owner, repo, base, head)


@mcp.tool
def list_releases(
    owner: str,
    repo: str,
    per_page: int = 10
) -> list[TextContent]:
    """List releases. Use to find versions, changelogs, or breaking changes."""
    return list_releases_workflow(owner, repo, per_page)


@mcp.tool
def get_release(
    owner: str,
    repo: str,
    tag: str | None = None
) -> list[TextContent]:
    """Get release with full notes. Use to read changelogs or check what changed in a version."""
    return get_release_workflow(owner, repo, tag)


if __name__ == "__main__":
    mcp.run()
