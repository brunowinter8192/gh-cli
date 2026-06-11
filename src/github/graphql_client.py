# INFRASTRUCTURE
import logging
import requests
from src.github.client import GITHUB_TOKEN

GITHUB_GRAPHQL = "https://api.github.com/graphql"

logger = logging.getLogger(__name__)


# FUNCTIONS

# Execute GraphQL query against GitHub API
def graphql_query(query: str, variables: dict) -> dict:
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json"
    }
    logger.debug("Fetching from %s", GITHUB_GRAPHQL)
    response = requests.post(
        GITHUB_GRAPHQL,
        headers=headers,
        json={"query": query, "variables": variables}
    )
    response.raise_for_status()
    data = response.json()
    if "errors" in data:
        errors = data["errors"]
        raise Exception("GraphQL Error: " + "; ".join(e.get("message", str(e)) for e in errors))
    return data["data"]
