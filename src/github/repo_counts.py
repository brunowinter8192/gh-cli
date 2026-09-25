# INFRASTRUCTURE
import logging
from src.github.graphql_client import graphql_query

logger = logging.getLogger(__name__)


# FUNCTIONS

def fetch_repo_counts(repos: list) -> dict:
    if not repos:
        return {}
    fields = (
        "stargazerCount "
        "issues { totalCount } "
        "discussions { totalCount } "
        "hasIssuesEnabled "
        "hasDiscussionsEnabled"
    )
    parts = [
        f'r{i}: repository(owner: "{owner}", name: "{name}") {{ {fields} }}'
        for i, (owner, name) in enumerate(repos)
    ]
    query = "query { " + " ".join(parts) + " }"
    data = graphql_query(query, {})
    result = {}
    for i, (owner, name) in enumerate(repos):
        node = data.get(f"r{i}")
        if node is None:
            logger.warning("repo_counts: %s/%s returned null, counts unavailable", owner, name)
            result[f"{owner}/{name}"] = None
            continue
        result[f"{owner}/{name}"] = {
            "stars": node["stargazerCount"],
            "issues": node["issues"]["totalCount"],
            "discussions": node["discussions"]["totalCount"],
            "hasIssuesEnabled": node["hasIssuesEnabled"],
            "hasDiscussionsEnabled": node["hasDiscussionsEnabled"],
        }
    return result


def format_count_line(full_name: str, stars: int, counts) -> str:
    if counts is None:
        return f"{full_name} · ⭐{stars} · issues:? · discussions:?"
    issues_n = counts["issues"]
    disc_n = counts["discussions"]
    issues_str = f"issues:{issues_n}" if counts["hasIssuesEnabled"] else f"issues:{issues_n} (off)"
    disc_str = f"discussions:{disc_n}" if counts["hasDiscussionsEnabled"] else f"discussions:{disc_n} (off)"
    return f"{full_name} · ⭐{stars} · {issues_str} · {disc_str}"
