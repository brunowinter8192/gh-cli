#!/usr/bin/env python3
import os
import sys

# Ensure src.github.* imports resolve regardless of working directory
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


# Build argparse parser with all 14 subcommands
def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cli.py",
        description="GitHub Research CLI — 14 tools for searching, browsing, and managing repos, code, issues, discussions, releases."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    # ── search_repos ──────────────────────────────────────────────────────────
    p = sub.add_parser("search_repos", help="Search GitHub repositories.")
    p.add_argument("query", help="Search query (max 2-3 words; GitHub returns 0 for longer queries)")
    p.add_argument("--sort-by", dest="sort_by",
                   choices=["stars", "forks", "updated", "best_match"],
                   default="best_match")

    # ── search_code ───────────────────────────────────────────────────────────
    p = sub.add_parser("search_code", help="Search code across GitHub.")
    p.add_argument("query", help="Code search query with qualifiers (e.g. 'def workflow language:python')")

    # ── get_repo_tree ─────────────────────────────────────────────────────────
    p = sub.add_parser("get_repo_tree", help="Browse repository file tree (one level).")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("--path", default="", help="Directory to list (default: repo root)")

    # ── get_file_content ──────────────────────────────────────────────────────
    p = sub.add_parser("get_file_content", help="Read file from GitHub repo.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("path")
    p.add_argument("--metadata-only", dest="metadata_only", action="store_true", default=False)
    p.add_argument("--offset", type=int, default=0, help="Start reading from this line number")
    p.add_argument("--limit", type=int, default=0, help="Number of lines to return (0=all)")

    # ── index_issues ──────────────────────────────────────────────────────────
    p = sub.add_parser("index_issues", help="Fetch issues matching a query and index into RAG.")
    p.add_argument("query", help="Search keywords (max 3; most distinctive first)")
    p.add_argument("repo", help="Repository as owner/repo")
    p.add_argument("--limit", type=int, default=30,
                   help="Max issues to fetch and index (default 30)")

    # ── index_discussions ─────────────────────────────────────────────────────
    p = sub.add_parser("index_discussions", help="Fetch discussions matching a query and index into RAG.")
    p.add_argument("query", help="Search keywords (max 3; most distinctive first)")
    p.add_argument("repo", help="Repository as owner/repo")
    p.add_argument("--limit", type=int, default=30,
                   help="Max discussions to fetch and index (default 30)")

    # ── index_releases ────────────────────────────────────────────────────────
    p = sub.add_parser("index_releases", help="Fetch all releases and index into RAG.")
    p.add_argument("repo", help="Repository as owner/repo")

    # ── create_issue ──────────────────────────────────────────────────────────
    p = sub.add_parser("create_issue", help="Create a new issue.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("title")
    p.add_argument("--body", default=None, help="Issue body (Markdown)")
    p.add_argument("--labels", default=None, help="Comma-separated label names")
    p.add_argument("--assignees", default=None, help="Comma-separated GitHub usernames")

    # ── update_issue ──────────────────────────────────────────────────────────
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

    # ── list_issues ───────────────────────────────────────────────────────────
    p = sub.add_parser("list_issues", help="List repository issues (default: open only).")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("--state", choices=["open", "closed", "all"], default="open",
                   help="Filter by state (default: open)")
    p.add_argument("--labels", default=None, help="Comma-separated label filter")
    p.add_argument("--limit", type=int, default=30, help="Max issues to return (default 30)")

    # ── get_issue ─────────────────────────────────────────────────────────────
    p = sub.add_parser("get_issue", help="Read a single issue (title, state, body).")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("number", type=int)

    # ── delete_issue ──────────────────────────────────────────────────────────
    p = sub.add_parser("delete_issue", help="Permanently delete an issue via GraphQL (irreversible).")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("number", type=int)
    p.add_argument("--confirm", action="store_true", default=False,
                   help="Required: actually perform the deletion (irreversible)")

    # ── repo_freshness ────────────────────────────────────────────────────────
    p = sub.add_parser("repo_freshness", help="Show how recently a repo was pushed to.")
    p.add_argument("owner")
    p.add_argument("repo")

    # ── download_files ────────────────────────────────────────────────────────
    p = sub.add_parser("download_files", help="Download specific repo files to a local directory.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("paths", nargs="+", help="One or more repo file paths to download")
    p.add_argument("--dest", default=".", help="Local destination directory (default: current dir)")

    return parser


# Dispatch parsed args to the matching workflow function
def _dispatch(args, parser):
    if args.cmd == "search_repos":
        return search_repos_workflow(args.query, args.sort_by)

    elif args.cmd == "search_code":
        return search_code_workflow(args.query)

    elif args.cmd == "get_repo_tree":
        return get_repo_tree_workflow(args.owner, args.repo, args.path)

    elif args.cmd == "get_file_content":
        return get_file_content_workflow(
            args.owner, args.repo, args.path,
            args.metadata_only, args.offset, args.limit
        )

    elif args.cmd == "index_issues":
        return index_issues_workflow(args.query, args.repo, args.limit)

    elif args.cmd == "index_discussions":
        return index_discussions_workflow(args.query, args.repo, args.limit)

    elif args.cmd == "index_releases":
        return index_releases_workflow(args.repo)

    elif args.cmd == "create_issue":
        labels = [l.strip() for l in args.labels.split(",")] if args.labels else None
        assignees = [a.strip() for a in args.assignees.split(",")] if args.assignees else None
        return create_issue_workflow(args.owner, args.repo, args.title, args.body, labels, assignees)

    elif args.cmd == "update_issue":
        labels = [l.strip() for l in args.labels.split(",")] if args.labels else None
        return update_issue_workflow(
            args.owner, args.repo, args.number,
            args.title, args.body, labels, args.state, args.state_reason
        )

    elif args.cmd == "list_issues":
        return list_issues_workflow(args.owner, args.repo, args.state, args.labels, args.limit)

    elif args.cmd == "get_issue":
        return get_issue_workflow(args.owner, args.repo, args.number)

    elif args.cmd == "delete_issue":
        return delete_issue_workflow(args.owner, args.repo, args.number, args.confirm)

    elif args.cmd == "repo_freshness":
        return repo_freshness_workflow(args.owner, args.repo)

    elif args.cmd == "download_files":
        return download_files_workflow(args.owner, args.repo, args.paths, args.dest)

    else:
        parser.error(f"Unknown command: {args.cmd}")


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


if __name__ == "__main__":
    main()
