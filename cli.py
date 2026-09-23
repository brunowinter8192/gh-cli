#!/usr/bin/env python3
# INFRASTRUCTURE
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import argparse

from src.github.search_repos import search_repos_workflow
from src.github.search_code import search_code_workflow
from src.github.get_repo_tree import get_repo_tree_workflow
from src.github.get_file_content import get_file_content_workflow
from src.github.index_issues import index_issues_workflow
from src.github.index_discussions import index_discussions_workflow
from src.github.index_releases import index_releases_workflow
from src.github.create_issue import create_issue_workflow
from src.github.update_issue import update_issue_workflow
from src.github.list_issues import list_issues_workflow
from src.github.get_issue import get_issue_workflow
from src.github.delete_issue import delete_issue_workflow
from src.github.repo_freshness import repo_freshness_workflow
from src.github.download_files import download_files_workflow
from src.github.trending import trending_workflow

HELP_TEXT = (
    "This CLI has no help text. Invoke the skill gh-cli-search via "
    "the Skill tool and follow it exactly. Do not guess flags."
)


class NoHelpParser(argparse.ArgumentParser):
    def error(self, message):
        self.exit(2, HELP_TEXT + "\n")

    def print_help(self, file=None):
        print(HELP_TEXT, file=file or sys.stderr)
        self.exit(2)


# ORCHESTRATOR
def main():
    parser = _build_parser()
    args = parser.parse_args()
    try:
        result = _dispatch(args, parser)
        print(result[0].text)
    except BrokenPipeError:
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


# FUNCTIONS
def _add_search_repos_parser(sub):
    p = sub.add_parser("search_repos", help="Search GitHub repositories.")
    p.add_argument("query", help="Search query (max 2-3 words; GitHub returns 0 for longer queries)")
    p.add_argument("--sort-by", dest="sort_by",
                   choices=["stars", "forks", "updated", "best_match"],
                   default="best_match")


def _add_search_code_parser(sub):
    p = sub.add_parser("search_code", help="Search code across GitHub.")
    p.add_argument("query", help="Code search query with qualifiers (e.g. 'def workflow language:python')")


def _add_get_repo_tree_parser(sub):
    p = sub.add_parser("get_repo_tree", help="Browse repository file tree (one level).")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("--path", default="", help="Directory to list (default: repo root)")


def _add_get_file_content_parser(sub):
    p = sub.add_parser("get_file_content", help="Read file from GitHub repo.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("path")
    p.add_argument("--metadata-only", dest="metadata_only", action="store_true", default=False)
    p.add_argument("--offset", type=int, default=0, help="Start reading from this line number")
    p.add_argument("--limit", type=int, default=0, help="Number of lines to return (0=all)")


def _add_index_issues_parser(sub):
    p = sub.add_parser("index_issues", help="Fetch issues matching a query and index into RAG.")
    p.add_argument("query", help="Search keywords (max 3; most distinctive first)")
    p.add_argument("repo", help="Repository as owner/repo")
    p.add_argument("--limit", type=int, default=30,
                   help="Max issues to fetch and index (default 30)")


def _add_index_discussions_parser(sub):
    p = sub.add_parser("index_discussions", help="Fetch discussions matching a query and index into RAG.")
    p.add_argument("query", help="Search keywords (max 3; most distinctive first)")
    p.add_argument("repo", help="Repository as owner/repo")
    p.add_argument("--limit", type=int, default=30,
                   help="Max discussions to fetch and index (default 30)")


def _add_index_releases_parser(sub):
    p = sub.add_parser("index_releases", help="Fetch all releases and index into RAG.")
    p.add_argument("repo", help="Repository as owner/repo")


def _add_create_issue_parser(sub):
    p = sub.add_parser("create_issue", help="Create a new issue.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("title")
    p.add_argument("--body", default=None, help="Issue body (Markdown)")
    p.add_argument("--labels", default=None, help="Comma-separated label names")
    p.add_argument("--assignees", default=None, help="Comma-separated GitHub usernames")


def _add_update_issue_parser(sub):
    p = sub.add_parser("update_issue", help="Update an existing issue (also closes/reopens).")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("number", type=int)
    p.add_argument("--title", default=None)
    p.add_argument("--body", default=None)
    p.add_argument("--labels", default=None, help="Comma-separated label names (replaces all)")
    p.add_argument("--state", choices=["open", "closed"], default=None)
    p.add_argument("--state-reason", dest="state_reason",
                   choices=["completed", "not_planned", "reopened"], default=None)


def _add_list_issues_parser(sub):
    p = sub.add_parser("list_issues", help="List repository issues (default: open only).")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("--state", choices=["open", "closed", "all"], default="open",
                   help="Filter by state (default: open)")
    p.add_argument("--labels", default=None, help="Comma-separated label filter")
    p.add_argument("--limit", type=int, default=30, help="Max issues to return (default 30)")


def _add_get_issue_parser(sub):
    p = sub.add_parser("get_issue", help="Read a single issue (title, state, body).")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("number", type=int)


def _add_delete_issue_parser(sub):
    p = sub.add_parser("delete_issue", help="Permanently delete an issue via GraphQL (irreversible).")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("number", type=int)
    p.add_argument("--confirm", action="store_true", default=False,
                   help="Required: actually perform the deletion (irreversible)")


def _add_repo_freshness_parser(sub):
    p = sub.add_parser("repo_freshness", help="Show how recently a repo was pushed to.")
    p.add_argument("owner")
    p.add_argument("repo")


def _add_download_files_parser(sub):
    p = sub.add_parser("download_files", help="Download specific repo files to a local directory.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("paths", nargs="+", help="One or more repo file paths to download")
    p.add_argument("--dest", default=".", help="Local destination directory (default: current dir)")


def _add_trending_parser(sub):
    p = sub.add_parser("trending", help="List what is trending on GitHub.")
    p.add_argument("--language", default=None, help="Language slug as in the trending URL (e.g. python, c++)")
    p.add_argument("--since", choices=["daily", "weekly", "monthly"], default="daily",
                   help="Date range: daily=today, weekly=this week, monthly=this month (default: daily)")
    p.add_argument("--spoken", default=None, help="Spoken language code (e.g. en, de, zh); repositories only")
    p.add_argument("--developers", action="store_true", default=False,
                   help="Show the Developers tab instead of Repositories")


def _build_parser() -> argparse.ArgumentParser:
    parser = NoHelpParser(
        prog="cli.py",
        description="GitHub Research CLI — 15 tools for searching, browsing, and managing repos, code, issues, discussions, releases."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    _add_search_repos_parser(sub)
    _add_search_code_parser(sub)
    _add_get_repo_tree_parser(sub)
    _add_get_file_content_parser(sub)
    _add_index_issues_parser(sub)
    _add_index_discussions_parser(sub)
    _add_index_releases_parser(sub)
    _add_create_issue_parser(sub)
    _add_update_issue_parser(sub)
    _add_list_issues_parser(sub)
    _add_get_issue_parser(sub)
    _add_delete_issue_parser(sub)
    _add_repo_freshness_parser(sub)
    _add_download_files_parser(sub)
    _add_trending_parser(sub)

    return parser


def _dispatch_search_repos(args):
    return search_repos_workflow(args.query, args.sort_by)


def _dispatch_search_code(args):
    return search_code_workflow(args.query)


def _dispatch_get_repo_tree(args):
    return get_repo_tree_workflow(args.owner, args.repo, args.path)


def _dispatch_get_file_content(args):
    return get_file_content_workflow(
        args.owner, args.repo, args.path,
        args.metadata_only, args.offset, args.limit
    )


def _dispatch_index_issues(args):
    return index_issues_workflow(args.query, args.repo, args.limit)


def _dispatch_index_discussions(args):
    return index_discussions_workflow(args.query, args.repo, args.limit)


def _dispatch_index_releases(args):
    return index_releases_workflow(args.repo)


def _dispatch_create_issue(args):
    labels = [l.strip() for l in args.labels.split(",")] if args.labels else None
    assignees = [a.strip() for a in args.assignees.split(",")] if args.assignees else None
    return create_issue_workflow(args.owner, args.repo, args.title, args.body, labels, assignees)


def _dispatch_update_issue(args):
    labels = [l.strip() for l in args.labels.split(",")] if args.labels else None
    return update_issue_workflow(
        args.owner, args.repo, args.number,
        args.title, args.body, labels, args.state, args.state_reason
    )


def _dispatch_list_issues(args):
    return list_issues_workflow(args.owner, args.repo, args.state, args.labels, args.limit)


def _dispatch_get_issue(args):
    return get_issue_workflow(args.owner, args.repo, args.number)


def _dispatch_delete_issue(args):
    return delete_issue_workflow(args.owner, args.repo, args.number, args.confirm)


def _dispatch_repo_freshness(args):
    return repo_freshness_workflow(args.owner, args.repo)


def _dispatch_download_files(args):
    return download_files_workflow(args.owner, args.repo, args.paths, args.dest)


def _dispatch_trending(args):
    return trending_workflow(args.language, args.since, args.spoken, args.developers)


def _dispatch(args, parser):
    handlers = {
        "search_repos": _dispatch_search_repos,
        "search_code": _dispatch_search_code,
        "get_repo_tree": _dispatch_get_repo_tree,
        "get_file_content": _dispatch_get_file_content,
        "index_issues": _dispatch_index_issues,
        "index_discussions": _dispatch_index_discussions,
        "index_releases": _dispatch_index_releases,
        "create_issue": _dispatch_create_issue,
        "update_issue": _dispatch_update_issue,
        "list_issues": _dispatch_list_issues,
        "get_issue": _dispatch_get_issue,
        "delete_issue": _dispatch_delete_issue,
        "repo_freshness": _dispatch_repo_freshness,
        "download_files": _dispatch_download_files,
        "trending": _dispatch_trending,
    }
    handler = handlers.get(args.cmd)
    if handler is None:
        parser.error(f"Unknown command: {args.cmd}")
        return
    return handler(args)


if __name__ == "__main__":
    main()
