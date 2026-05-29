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
from src.github.grep_file import grep_file_workflow
from src.github.grep_repo import grep_repo_workflow
from src.github.search_items import search_items_workflow
from src.github.get_issue import get_issue_workflow
from src.github.get_issue_comments import get_issue_comments_workflow
from src.github.index_issues import index_issues_workflow
from src.github.get_repo import get_repo_workflow
from src.github.search_discussions import search_discussions_workflow
from src.github.list_discussions import list_discussions_workflow
from src.github.get_discussion import get_discussion_workflow
from src.github.list_commits import list_commits_workflow
from src.github.compare_commits import compare_commits_workflow
from src.github.list_releases import list_releases_workflow
from src.github.get_release import get_release_workflow


def main():
    parser = argparse.ArgumentParser(
        prog="cli.py",
        description="GitHub Research CLI — 18 tools for searching repos, code, issues, discussions, releases."
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
    p = sub.add_parser("get_repo_tree", help="Browse repository file tree.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("--path", default="", help="Subdirectory scope")
    p.add_argument("--depth", type=int, default=-1, help="Tree depth (-1=unlimited)")
    p.add_argument("--pattern", default="", help="Glob pattern for file search (e.g. '*.py')")

    # ── get_file_content ──────────────────────────────────────────────────────
    p = sub.add_parser("get_file_content", help="Read file from GitHub repo.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("path")
    p.add_argument("--metadata-only", dest="metadata_only", action="store_true", default=False)
    p.add_argument("--offset", type=int, default=0, help="Start reading from this line number")
    p.add_argument("--limit", type=int, default=0, help="Number of lines to return (0=all)")

    # ── grep_file ─────────────────────────────────────────────────────────────
    p = sub.add_parser("grep_file", help="Regex search within a single file.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("path")
    p.add_argument("pattern", help="Regex pattern")
    p.add_argument("--context-lines", dest="context_lines", type=int, default=0)
    p.add_argument("--max-matches", dest="max_matches", type=int, default=50)

    # ── grep_repo ─────────────────────────────────────────────────────────────
    p = sub.add_parser("grep_repo", help="Regex search across repo files.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("pattern", help="Regex pattern to search in file content")
    p.add_argument("--file-pattern", dest="file_pattern", default="*",
                   help="Glob pattern for file selection (e.g. '*.py')")
    p.add_argument("--path", default="", help="Subdirectory scope")
    p.add_argument("--max-files", dest="max_files", type=int, default=10,
                   help="Max files to search (server enforces min 20)")

    # ── search_items ──────────────────────────────────────────────────────────
    p = sub.add_parser("search_items", help="Search GitHub issues or PRs.")
    p.add_argument("query")
    p.add_argument("--type", dest="item_type", required=True,
                   choices=["issue", "pr"], help="Item type to search")
    p.add_argument("--sort-by", dest="sort_by",
                   choices=["comments", "reactions", "created", "updated", "best_match"],
                   default="best_match")

    # ── get_issue ─────────────────────────────────────────────────────────────
    p = sub.add_parser("get_issue", help="Read GitHub issue.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("issue_number", type=int)

    # ── get_issue_comments ────────────────────────────────────────────────────
    p = sub.add_parser("get_issue_comments", help="Read issue comments.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("issue_number", type=int)

    # ── index_issues ──────────────────────────────────────────────────────────
    p = sub.add_parser("index_issues", help="Fetch issues matching a query and index into RAG.")
    p.add_argument("query", help="Search keywords (max 3; most distinctive first)")
    p.add_argument("repo", help="Repository as owner/repo")
    p.add_argument("--limit", type=int, default=30,
                   help="Max issues to fetch and index (default 30)")

    # ── get_repo ──────────────────────────────────────────────────────────────
    p = sub.add_parser("get_repo", help="Read repository metadata.")
    p.add_argument("owner")
    p.add_argument("repo")

    # ── search_discussions ────────────────────────────────────────────────────
    p = sub.add_parser("search_discussions", help="Search GitHub discussions.")
    p.add_argument("query")
    p.add_argument("--first", type=int, default=10, help="Max results to return")

    # ── list_discussions ──────────────────────────────────────────────────────
    p = sub.add_parser("list_discussions", help="List repository discussions.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("--first", type=int, default=10)
    p.add_argument("--category", default=None, help="Filter by category slug")
    ans_group = p.add_mutually_exclusive_group()
    ans_group.add_argument("--answered", dest="answered", action="store_true", default=None,
                           help="Show only answered discussions")
    ans_group.add_argument("--not-answered", dest="answered", action="store_false",
                           help="Show only unanswered discussions")

    # ── get_discussion ────────────────────────────────────────────────────────
    p = sub.add_parser("get_discussion", help="Read discussion with comments.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("number", type=int)
    p.add_argument("--comment-limit", dest="comment_limit", type=int, default=50)
    p.add_argument("--comment-sort", dest="comment_sort",
                   choices=["upvotes", "chronological"], default="upvotes")

    # ── list_commits ──────────────────────────────────────────────────────────
    p = sub.add_parser("list_commits", help="List commit history.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("--sha", default="", help="Branch or commit SHA to start from")
    p.add_argument("--path", default="", help="Only commits touching this file path")
    p.add_argument("--author", default="", help="Filter by author login")
    p.add_argument("--per-page", dest="per_page", type=int, default=20)

    # ── compare_commits ───────────────────────────────────────────────────────
    p = sub.add_parser("compare_commits", help="Compare branches/tags/SHAs.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("base", help="Base branch, tag, or SHA")
    p.add_argument("head", help="Head branch, tag, or SHA")

    # ── list_releases ─────────────────────────────────────────────────────────
    p = sub.add_parser("list_releases", help="List repository releases.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("--per-page", dest="per_page", type=int, default=10)

    # ── get_release ───────────────────────────────────────────────────────────
    p = sub.add_parser("get_release", help="Read release notes.")
    p.add_argument("owner")
    p.add_argument("repo")
    p.add_argument("--tag", default=None,
                   help="Release tag (e.g. 'v2.0.0') — omit for latest release")

    # ── Dispatch ──────────────────────────────────────────────────────────────
    args = parser.parse_args()

    if args.cmd == "search_repos":
        result = search_repos_workflow(args.query, args.sort_by)

    elif args.cmd == "search_code":
        result = search_code_workflow(args.query)

    elif args.cmd == "get_repo_tree":
        result = get_repo_tree_workflow(args.owner, args.repo, args.path, args.depth, args.pattern)

    elif args.cmd == "get_file_content":
        result = get_file_content_workflow(
            args.owner, args.repo, args.path,
            args.metadata_only, args.offset, args.limit
        )

    elif args.cmd == "grep_file":
        result = grep_file_workflow(
            args.owner, args.repo, args.path,
            args.pattern, args.context_lines, args.max_matches
        )

    elif args.cmd == "grep_repo":
        result = grep_repo_workflow(
            args.owner, args.repo, args.pattern,
            args.file_pattern, args.path, args.max_files
        )

    elif args.cmd == "search_items":
        result = search_items_workflow(args.query, args.item_type, args.sort_by)

    elif args.cmd == "get_issue":
        result = get_issue_workflow(args.owner, args.repo, args.issue_number)

    elif args.cmd == "get_issue_comments":
        result = get_issue_comments_workflow(args.owner, args.repo, args.issue_number)

    elif args.cmd == "index_issues":
        result = index_issues_workflow(args.query, args.repo, args.limit)

    elif args.cmd == "get_repo":
        result = get_repo_workflow(args.owner, args.repo)

    elif args.cmd == "search_discussions":
        result = search_discussions_workflow(args.query, args.first)

    elif args.cmd == "list_discussions":
        result = list_discussions_workflow(
            args.owner, args.repo, args.first, args.category, args.answered
        )

    elif args.cmd == "get_discussion":
        result = get_discussion_workflow(
            args.owner, args.repo, args.number,
            args.comment_limit, args.comment_sort
        )

    elif args.cmd == "list_commits":
        result = list_commits_workflow(
            args.owner, args.repo, args.sha,
            args.path, args.author, args.per_page
        )

    elif args.cmd == "compare_commits":
        result = compare_commits_workflow(args.owner, args.repo, args.base, args.head)

    elif args.cmd == "list_releases":
        result = list_releases_workflow(args.owner, args.repo, args.per_page)

    elif args.cmd == "get_release":
        result = get_release_workflow(args.owner, args.repo, args.tag)

    else:
        parser.error(f"Unknown command: {args.cmd}")

    print(result[0].text)


if __name__ == "__main__":
    main()
