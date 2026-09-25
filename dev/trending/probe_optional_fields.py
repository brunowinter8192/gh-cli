# INFRASTRUCTURE
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))

from src.github.trending import PERIOD_RE, clean_text, collect_entries, fetch_trending_html, find_node

LANGUAGES = [None, "python", "rust", "javascript", "go", "c++", "shell", "html", "markdown", "jupyter-notebook"]
SINCES = ["daily", "weekly", "monthly"]
REPORT = HERE / "md" / "probe_optional_fields.md"


# ORCHESTRATOR
def main():
    combos = [(dev, since, lang) for dev in (False, True) for since in SINCES for lang in LANGUAGES]
    with ThreadPoolExecutor(max_workers=len(combos)) as pool:
        results = list(pool.map(probe_combo, combos))
    REPORT.write_text(build_report(results))
    print(REPORT)


# FUNCTIONS
def probe_combo(combo):
    developers, since, language = combo
    html = fetch_trending_html(language, since, None, developers)
    entries = collect_entries(html)
    return combo, [describe_entry(nodes, developers) for nodes in entries]


def describe_entry(nodes, developers):
    if developers:
        return {
            "popular_repo": find_node(nodes, lambda n: n["tag"] == "a" and n["nested"]) is not None,
            "popular_repo_description": find_node(nodes, lambda n: n["nested"] and n["tag"] == "div" and {"f6", "mt-1"} <= set(n["classes"])) is not None,
        }
    period = find_node(nodes, lambda n: "float-sm-right" in n["classes"])
    return {
        "description": find_node(nodes, lambda n: n["tag"] == "p") is not None,
        "language": find_node(nodes, lambda n: n["attrs"].get("itemprop") == "programmingLanguage") is not None,
        "period_node": period is not None,
        "period_text_unrecognised": clean_text(period["text"]) if period and not PERIOD_RE.match(clean_text(period["text"])) else None,
    }


def build_report(results):
    totals = {}
    unrecognised = set()
    entries_total = 0
    for (developers, _, _), entries in results:
        kind = "developers" if developers else "repositories"
        for entry in entries:
            entries_total += 1
            for field, value in entry.items():
                if field == "period_text_unrecognised":
                    if value:
                        unrecognised.add(value)
                    continue
                key = (kind, field)
                present, total = totals.get(key, (0, 0))
                totals[key] = (present + bool(value), total + 1)
    lines = [f"# probe_optional_fields ({date.today().isoformat()})", "", f"Pages: {len(results)}, entries: {entries_total}", "", "| kind | field | present | total |", "|---|---|---|---|"]
    for (kind, field), (present, total) in sorted(totals.items()):
        lines.append(f"| {kind} | {field} | {present} | {total} |")
    lines += ["", "Period texts not matching PERIOD_RE:", ""]
    lines += [f"- `{text}`" for text in sorted(unrecognised)] or ["- none"]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
