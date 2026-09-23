# INFRASTRUCTURE
import logging
import re
from html.parser import HTMLParser
from urllib.parse import quote

import requests
from mcp.types import TextContent

logger = logging.getLogger(__name__)

TRENDING_BASE_URL = "https://github.com/trending"
TRENDING_USER_AGENT = "gh-cli-trending/1.0"
TRENDING_TIMEOUT_SECONDS = 10
DESCRIPTION_MAX_CHARS = 160
SINCE_LABELS = {"daily": "today", "weekly": "this week", "monthly": "this month"}
VOID_TAGS = {"img", "br", "hr", "input", "meta", "link", "source", "wbr"}
PERIOD_RE = re.compile(r"^([\d,]+) stars (today|this week|this month)$")
NUMBER_RE = re.compile(r"^\d[\d,]*$")


# ORCHESTRATOR

def trending_workflow(
    language: str | None,
    since: str,
    spoken: str | None,
    developers: bool,
) -> list[TextContent]:
    logger.info("trending language=%s since=%s spoken=%s developers=%s", language, since, spoken, developers)
    validate_options(spoken, developers)
    html = fetch_trending_html(language, since, spoken, developers)
    items = parse_trending(html, developers)
    return [TextContent(type="text", text=format_trending(items, language, since, spoken, developers))]


# FUNCTIONS

def validate_options(spoken: str | None, developers: bool) -> None:
    if spoken and developers:
        raise ValueError("--spoken applies to repositories only, not to --developers")


def build_trending_url(language: str | None, developers: bool) -> str:
    url = TRENDING_BASE_URL
    if developers:
        url += "/developers"
    if language:
        url += "/" + quote(language.strip().lower(), safe="+")
    return url


def fetch_trending_html(language: str | None, since: str, spoken: str | None, developers: bool) -> str:
    url = build_trending_url(language, developers)
    params = {"since": since}
    if spoken:
        params["spoken_language_code"] = spoken
    logger.debug("Fetching from %s params=%s", url, params)
    response = requests.get(
        url,
        params=params,
        headers={"User-Agent": TRENDING_USER_AGENT},
        timeout=TRENDING_TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    return response.text


def parse_trending(html: str, developers: bool) -> list[dict]:
    entries = collect_entries(html)
    if not entries:
        raise RuntimeError(
            "trending page yielded 0 entries: page markup changed, or unknown language / spoken code"
        )
    extract = extract_developer if developers else extract_repository
    return [extract(index, nodes) for index, nodes in enumerate(entries, start=1)]


def collect_entries(html: str) -> list[list[dict]]:
    collector = EntryCollector()
    collector.feed(html)
    collector.close()
    return collector.entries


class EntryCollector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.entries = []
        self.nodes = None
        self.open_nodes = []
        self.nested_articles = 0
        self.title_depth = 0

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        classes = (attr_map.get("class") or "").split()
        if self.nodes is None:
            if tag == "article" and "Box-row" in classes:
                self.nodes = []
                self.open_nodes = []
                self.nested_articles = 0
            return
        if tag == "article":
            self.nested_articles += 1
        if tag in VOID_TAGS:
            return
        node = {
            "tag": tag,
            "attrs": attr_map,
            "classes": classes,
            "nested": self.nested_articles > 0,
            "in_title": any(n["is_title"] for n in self.open_nodes),
            "is_title": tag in ("h1", "h2") and "h3" in classes,
            "text": "",
        }
        self.nodes.append(node)
        self.open_nodes.append(node)

    def handle_startendtag(self, tag, attrs):
        return

    def handle_endtag(self, tag):
        if self.nodes is None or tag in VOID_TAGS:
            return
        if tag == "article":
            if self.nested_articles > 0:
                self.nested_articles -= 1
            else:
                self.entries.append(self.nodes)
                self.nodes = None
                self.open_nodes = []
                return
        while self.open_nodes:
            closed = self.open_nodes.pop()
            if closed["tag"] == tag:
                break

    def handle_data(self, data):
        for node in self.open_nodes:
            node["text"] += data


def clean_text(text: str) -> str:
    return " ".join(text.split())


def find_node(nodes: list[dict], predicate) -> dict | None:
    for node in nodes:
        if predicate(node):
            return node
    return None


def require_node(nodes: list[dict], predicate, index: int, what: str) -> dict:
    node = find_node(nodes, predicate)
    if node is None:
        raise RuntimeError(f"trending entry {index}: {what} not found, page markup changed")
    return node


def parse_count(text: str, index: int, what: str) -> int:
    cleaned = clean_text(text)
    if not NUMBER_RE.match(cleaned):
        raise RuntimeError(f"trending entry {index}: {what} '{cleaned}' is not a number, page markup changed")
    return int(cleaned.replace(",", ""))


def parse_period_stars(nodes: list[dict], index: int) -> tuple[int, str] | None:
    node = find_node(nodes, lambda n: "float-sm-right" in n["classes"])
    if node is None:
        return None
    match = PERIOD_RE.match(clean_text(node["text"]))
    if match is None:
        raise RuntimeError(
            f"trending entry {index}: period stars '{clean_text(node['text'])}' unrecognised, page markup changed"
        )
    return int(match.group(1).replace(",", "")), match.group(2)


def extract_repository(index: int, nodes: list[dict]) -> dict:
    link = require_node(nodes, lambda n: n["tag"] == "a" and n["in_title"], index, "repo link")
    full_name = (link["attrs"].get("href") or "").strip("/")
    if full_name.count("/") != 1:
        raise RuntimeError(f"trending entry {index}: repo link '{full_name}' is not owner/name")
    stars = require_node(
        nodes, lambda n: n["tag"] == "a" and "stargazers" in (n["attrs"].get("href") or ""), index, "stars link"
    )
    forks = require_node(
        nodes,
        lambda n: n["tag"] == "a" and any(k in (n["attrs"].get("href") or "") for k in ("/forks", "network/members")),
        index,
        "forks link",
    )
    description = find_node(nodes, lambda n: n["tag"] == "p")
    language = find_node(nodes, lambda n: n["attrs"].get("itemprop") == "programmingLanguage")
    return {
        "rank": index,
        "full_name": full_name,
        "description": clean_text(description["text"]) if description else "",
        "language": clean_text(language["text"]) if language else "",
        "stars": parse_count(stars["text"], index, "stars"),
        "forks": parse_count(forks["text"], index, "forks"),
        "period": parse_period_stars(nodes, index),
    }


def extract_developer(index: int, nodes: list[dict]) -> dict:
    title = require_node(nodes, lambda n: n["is_title"] and not n["nested"], index, "developer heading")
    link = require_node(nodes, lambda n: n["tag"] == "a" and n["in_title"] and not n["nested"], index, "developer link")
    login = (link["attrs"].get("href") or "").strip("/")
    if not login or "/" in login:
        raise RuntimeError(f"trending entry {index}: developer link '{login}' is not a login")
    repo_link = find_node(
        nodes,
        lambda n: n["tag"] == "a" and n["nested"] and (n["attrs"].get("href") or "").strip("/").count("/") == 1,
    )
    repo_description = find_node(nodes, lambda n: n["nested"] and n["tag"] == "div" and {"f6", "mt-1"} <= set(n["classes"]))
    return {
        "rank": index,
        "login": login,
        "name": clean_text(title["text"]),
        "repo": (repo_link["attrs"]["href"].strip("/") if repo_link else ""),
        "repo_description": clean_text(repo_description["text"]) if repo_description else "",
    }


def truncate(text: str) -> str:
    if len(text) <= DESCRIPTION_MAX_CHARS:
        return text
    return text[: DESCRIPTION_MAX_CHARS - 3].rstrip() + "..."


def format_header(language: str | None, since: str, spoken: str | None, developers: bool) -> str:
    kind = "developers" if developers else "repositories"
    parts = [f"Trending {kind}", language or "all languages", SINCE_LABELS[since]]
    if spoken:
        parts.append(f"spoken:{spoken}")
    return " · ".join(parts)


def format_repository(item: dict) -> list[str]:
    fields = [f"{item['rank']}. {item['full_name']}"]
    if item["language"]:
        fields.append(item["language"])
    fields.append(f"stars:{item['stars']}")
    fields.append(f"forks:{item['forks']}")
    if item["period"]:
        gained, label = item["period"]
        fields.append(f"+{gained} {label}")
    lines = [" · ".join(fields)]
    if item["description"]:
        lines.append(f"   {truncate(item['description'])}")
    return lines


def format_developer(item: dict) -> list[str]:
    head = f"{item['rank']}. {item['login']}"
    if item["name"] and item["name"] != item["login"]:
        head += f" ({item['name']})"
    if item["repo"]:
        head += f" · popular: {item['repo']}"
    lines = [head]
    if item["repo_description"]:
        lines.append(f"   {truncate(item['repo_description'])}")
    return lines


def format_trending(items: list[dict], language: str | None, since: str, spoken: str | None, developers: bool) -> str:
    format_item = format_developer if developers else format_repository
    lines = [format_header(language, since, spoken, developers)]
    for item in items:
        lines.extend(format_item(item))
    return "\n".join(lines)
