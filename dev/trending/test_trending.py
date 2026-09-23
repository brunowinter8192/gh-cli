import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))

from src.github.trending import format_trending, parse_trending, validate_options

FIXTURES = HERE / "fixtures"
REPORT = HERE / "md" / "test_trending.md"


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


def main():
    repo_output = check_repositories()
    dev_output = check_developers()
    check_tripwires()
    REPORT.write_text(
        "# test_trending\n\nAll checks passed.\n\n## repositories\n\n```\n"
        + repo_output + "\n```\n\n## developers\n\n```\n" + dev_output + "\n```\n"
    )
    print("PASS test_trending")


if __name__ == "__main__":
    main()
