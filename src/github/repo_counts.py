# INFRASTRUCTURE
import logging
# From graphql_client.py: execute GraphQL query against GitHub API
from src.github.graphql_client import graphql_query

logger = logging.getLogger(__name__)


# FUNCTIONS

# Batch-fetch star/issue/discussion counts for multiple repos in one aliased GraphQL call
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
            result[f"{owner}/{name}"] = None
            continue
        result[f"{owner}/{name}"] = {
            "stars": node.get("stargazerCount", 0),
            "issues": (node.get("issues") or {}).get("totalCount", 0),
            "discussions": (node.get("discussions") or {}).get("totalCount", 0),
            "hasIssuesEnabled": node.get("hasIssuesEnabled", True),
            "hasDiscussionsEnabled": node.get("hasDiscussionsEnabled", True),
        }
    return result


# Format one repo summary line; counts=None when repo is deleted/renamed between search and enrichment
def format_count_line(full_name: str, stars: int, counts) -> str:
    if counts is None:
        return f"{full_name} · ⭐{stars} · issues:? · discussions:?"
    issues_n = counts.get("issues", 0)
    disc_n = counts.get("discussions", 0)
    issues_str = f"issues:{issues_n}" if counts.get("hasIssuesEnabled", True) else f"issues:{issues_n} (off)"
    disc_str = f"discussions:{disc_n}" if counts.get("hasDiscussionsEnabled", True) else f"discussions:{disc_n} (off)"
    return f"{full_name} · ⭐{stars} · {issues_str} · {disc_str}"
