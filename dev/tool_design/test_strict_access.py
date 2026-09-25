# INFRASTRUCTURE
import base64
import os
import sys
import tempfile
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPORT = HERE / "md" / "test_strict_access.md"


# ORCHESTRATOR
def main():
    names = select_strands(sys.argv[1:])
    results = run_strands(names)
    write_report(results, len(names) == len(strand_table()))
    report_and_exit(results)


# FUNCTIONS
def strand_table():
    return dict([
        ("token_env_fallback", check_token_env_fallback),
        ("token_empty_raises", check_token_empty_raises),
        ("repo_counts_null_repo", check_repo_counts_null_repo),
        ("parse_chunk_count", check_parse_chunk_count),
        ("issue_body_null", check_issue_body_null),
        ("tree_null_language_and_linecount", check_tree_null_language_and_linecount),
        ("discussion_without_answer", check_discussion_without_answer),
        ("empty_base64_file", check_empty_base64_file),
        ("tree_repo_without_description", check_tree_repo_without_description),
        ("search_repos_fallback_note", check_search_repos_fallback_note),
    ])


def select_strands(requested):
    table = strand_table()
    unknown = [name for name in requested if name not in table]
    if unknown:
        raise SystemExit(f"unknown strand(s): {', '.join(unknown)}; available: {', '.join(table)}")
    return requested or list(table)


def run_strands(names):
    table = strand_table()
    context = multiprocessing.get_context("spawn")
    with ProcessPoolExecutor(max_workers=len(names), mp_context=context, max_tasks_per_child=1) as pool:
        futures = [(name, pool.submit(table[name])) for name in names]
        return [collect(name, future) for name, future in futures]


def collect(name, future):
    try:
        future.result()
        return name, None
    except Exception as e:
        return name, f"{type(e).__name__}: {e}"


def write_report(results, is_full_run):
    if not is_full_run:
        return
    lines = ["# test_strict_access", ""]
    for name, error in results:
        lines.append(f"- {name}: {'FAIL ' + error if error else 'PASS'}")
    REPORT.write_text("\n".join(lines) + "\n")


def report_and_exit(results):
    failed = [name for name, error in results if error]
    for name in failed:
        print(f"FAIL {name}")
    if failed:
        sys.exit(1)
    print("PASS test_strict_access")


def prepare_import(home_token_env):
    sys.path.insert(0, str(ROOT))
    home = tempfile.mkdtemp()
    os.environ["HOME"] = home
    os.environ.pop("GH_TOKEN", None)
    os.environ.pop("GITHUB_TOKEN", None)
    os.environ.update(home_token_env)


def check_token_env_fallback():
    prepare_import({"GITHUB_TOKEN": "ghp_test"})
    from src.github.client import build_headers, require_token
    assert require_token() == "ghp_test"
    assert build_headers()["Authorization"] == "Bearer ghp_test"


def check_token_empty_raises():
    prepare_import({})
    from src.github.client import build_headers
    from src.github.graphql_client import graphql_query
    for call in (build_headers, lambda: graphql_query("query { x }", {})):
        try:
            call()
        except RuntimeError as e:
            assert "No GitHub token" in str(e), str(e)
        else:
            raise AssertionError("no error raised for empty token")


def check_repo_counts_null_repo():
    prepare_import({})
    import src.github.repo_counts as rc
    full = {
        "stargazerCount": 131774,
        "issues": {"totalCount": 65172},
        "discussions": {"totalCount": 0},
        "hasIssuesEnabled": True,
        "hasDiscussionsEnabled": False,
    }
    rc.graphql_query = lambda query, variables: {"r0": None, "r1": full}
    counts = rc.fetch_repo_counts([("gone", "repo"), ("anthropics", "claude-code")])
    assert counts["gone/repo"] is None
    assert rc.format_count_line("gone/repo", 1, None) == "gone/repo · stars:1 · issues:? · discussions:?"
    line = rc.format_count_line("anthropics/claude-code", 131774, counts["anthropics/claude-code"])
    assert line == "anthropics/claude-code · stars:131774 · issues:65172 · discussions:0 (off)", line


def check_parse_chunk_count():
    sys.path.insert(0, str(ROOT))
    from src.github.rag_indexing import parse_chunk_count
    assert parse_chunk_count("\nNothing to index.\n") == 0
    assert parse_chunk_count("\nDone: 2 files indexed (17 chunks), 5 skipped, 0 adopted") == 17
    try:
        parse_chunk_count("something else")
    except RuntimeError as e:
        assert "Unrecognised" in str(e)
    else:
        raise AssertionError("no error raised for unknown output")


def check_issue_body_null():
    sys.path.insert(0, str(ROOT))
    from src.github.get_issue import format_issue
    issue = {
        "title": "t", "state": "open", "number": 7, "user": {"login": "u"},
        "author_association": "NONE", "created_at": "c", "updated_at": "u",
        "labels": [], "comments": 0, "html_url": "http://x", "body": None,
    }
    text = format_issue(issue, "o", "r")
    assert text.endswith("(No description provided)"), text
    assert "Labels:" not in text


def check_tree_null_language_and_linecount():
    sys.path.insert(0, str(ROOT))
    from src.github.get_repo_tree import format_tree
    entries = [
        {"name": "README.md", "type": "blob", "language": {"name": "Markdown"}, "lineCount": 77, "size": 6530},
        {"name": "plugins", "type": "tree", "language": None, "lineCount": None, "size": 0},
    ]
    rows = format_tree(entries).split("\n")
    assert rows[2].split() == ["README.md", "blob", "Markdown", "77", "6,530"], rows[2]
    assert rows[3].split() == ["plugins", "tree", "-", "-", "0"], rows[3]


def check_tree_repo_without_description():
    sys.path.insert(0, str(ROOT))
    import src.github.get_repo_tree as grt
    payload = {"repository": {
        "description": None,
        "primaryLanguage": {"name": "Go"},
        "languages": {"edges": [{"size": 10, "node": {"name": "Go"}}]},
        "object": {"__typename": "Tree", "entries": []},
    }}
    grt.graphql_query = lambda query, variables: payload
    text = grt.fetch_and_format("o", "r", "")
    assert "description:     (none)" in text, text
    assert "primaryLanguage: Go" in text


def check_search_repos_fallback_note():
    prepare_import({})
    import src.github.search_repos as sr
    payload = {"total_count": 1, "items": [{"full_name": "fastapi/fastapi", "stargazers_count": 5}]}
    empty = {"total_count": 0, "items": []}
    sr.fetch_repositories = lambda query, sort_by: payload if query == "fastapi" else empty
    sr.fetch_repo_counts = lambda repos: {"fastapi/fastapi": None}
    shortened = sr.search_repos_workflow("fastapi nonexistentzz")[0].text.split("\n")
    assert shortened[0] == "Query: 'fastapi' (fell back to 1 keyword)", shortened[0]
    assert shortened[1].startswith("fastapi/fastapi · stars:5"), shortened[1]
    direct = sr.search_repos_workflow("fastapi")[0].text
    assert not direct.startswith("Query:"), direct
    nothing = sr.search_repos_workflow("zzqq")[0].text
    assert nothing == "No repositories found for 'zzqq'.", nothing


def check_discussion_without_answer():
    sys.path.insert(0, str(ROOT))
    from src.github.get_discussion import format_discussion
    data = {"repository": {"discussion": {
        "title": "T", "body": "B", "author": {"login": "a"},
        "category": {"name": "Q&A", "emoji": "x", "isAnswerable": True},
        "upvoteCount": 1, "createdAt": "2026-06-01T00:00:00Z", "updatedAt": "2026-06-01T00:00:00Z",
        "isAnswered": False, "answer": None,
        "comments": {"totalCount": 1, "nodes": [{
            "body": "cb", "author": {"login": "c"}, "createdAt": "2026-06-02T00:00:00Z",
            "isAnswer": False, "upvoteCount": 0, "url": "u",
            "replies": {"nodes": [{"body": "rb", "author": {"login": "r"}, "createdAt": "2026-06-03T00:00:00Z", "upvoteCount": 0}]},
        }]},
    }}}
    text = format_discussion(data, 100)
    assert "**Status:** Open" in text
    assert "Accepted Answer" not in text
    assert "### Comments (1 total, showing 1)" in text
    assert "  > **@r**: rb (0 upvotes)" in text


def check_empty_base64_file():
    sys.path.insert(0, str(ROOT))
    from src.github.get_file_content import decode_content
    assert decode_content({"content": "", "encoding": "base64"}) == ""
    encoded = base64.b64encode(b"hello\nworld").decode()
    assert decode_content({"content": encoded, "encoding": "base64"}) == "hello\nworld"


if __name__ == "__main__":
    main()
