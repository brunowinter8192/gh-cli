# INFRASTRUCTURE
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))

from src.github.trending import format_trending, parse_trending, validate_options

FIXTURES = HERE / "fixtures"
REPORT = HERE / "md" / "test_trending.md"


# ORCHESTRATOR
def main():
    names = select_strands(sys.argv[1:])
    results = run_strands(names)
    write_report(results, len(names) == len(strand_table()))
    report_and_exit(results)


# FUNCTIONS
def strand_table():
    return dict([
        ("repositories", check_repositories),
        ("developers", check_developers),
        ("single_star", check_single_star),
        ("tripwires", check_tripwires),
    ])


def select_strands(requested):
    table = strand_table()
    unknown = [name for name in requested if name not in table]
    if unknown:
        raise SystemExit(f"unknown strand(s): {', '.join(unknown)}; available: {', '.join(table)}")
    return requested or list(table)


def run_strands(names):
    table = strand_table()
    with ThreadPoolExecutor(max_workers=len(names)) as pool:
        futures = [pool.submit(run_strand, name, table[name]) for name in names]
        return [f.result() for f in futures]


def run_strand(name, fn):
    try:
        return name, fn(), None
    except Exception as e:
        return name, None, f"{type(e).__name__}: {e}"


def write_report(results, is_full_run):
    if not is_full_run:
        return
    sections = [format_section(name, output, error) for name, output, error in results]
    REPORT.write_text("# test_trending\n\n" + "\n".join(sections))


def format_section(name, output, error):
    status = "FAIL" if error else "PASS"
    body = f"## {name}: {status}\n\n"
    if error:
        body += error + "\n"
    if output:
        body += "```\n" + output + "\n```\n"
    return body


def report_and_exit(results):
    failed = [name for name, _, error in results if error]
    for name in failed:
        print(f"FAIL {name}")
    if failed:
        sys.exit(1)
    print("PASS test_trending")


def check_repositories():
    html = (FIXTURES / "trending_weekly.html").read_text()
    items = parse_trending(html, False)
    assert len(items) == 3, len(items)
    first = items[0]
    assert first["full_name"] == "alibaba/open-code-review"
    assert first["language"] == "Go"
    assert first["stars"] == 40132 and first["forks"] == 2884
    assert first["period"] == (12590, "this week")
    assert first["description"].startswith("Secure, fast, efficient")
    no_description = items[2]
    assert no_description["full_name"] == "anthropics/financial-services"
    assert no_description["description"] == ""
    return format_trending(items, "go", "weekly", None, False)


def check_developers():
    html = (FIXTURES / "trending_developers.html").read_text()
    items = parse_trending(html, True)
    assert len(items) == 2, len(items)
    assert items[0]["login"] == "lidge-jun" and items[0]["name"] == "JUN"
    assert items[0]["repo"] == "lidge-jun/opencodex"
    assert items[0]["repo_description"].startswith("Universal provider proxy")
    return format_trending(items, None, "daily", None, True)


def check_single_star():
    html = (FIXTURES / "trending_single_star.html").read_text()
    items = parse_trending(html, False)
    assert len(items) == 1, len(items)
    assert items[0]["full_name"] == "nyldn/claude-octopus"
    assert items[0]["period"] == (1, "today"), items[0]["period"]
    return format_trending(items, "shell", "daily", None, False)


def raises(fn, needle):
    try:
        fn()
    except (RuntimeError, ValueError) as e:
        assert needle in str(e), str(e)
        return
    raise AssertionError(f"no error raised, expected '{needle}'")


def check_tripwires():
    raises(lambda: parse_trending("<html><body></body></html>", False), "0 entries")
    html = (FIXTURES / "trending_weekly.html").read_text()
    raises(lambda: parse_trending(html.replace("/stargazers", "/x"), False), "stars link not found")
    raises(lambda: parse_trending(html.replace("stars this week", "sterne"), False), "unrecognised")
    raises(lambda: validate_options("de", True), "--spoken")


if __name__ == "__main__":
    main()
