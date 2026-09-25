# INFRASTRUCTURE
import logging

MAX_KEYWORDS = 3

logger = logging.getLogger(__name__)


# FUNCTIONS

def build_empty_query_message() -> str:
    return "Empty query — provide 1-3 keywords."


def build_no_hits_message(subject: str, keyword: str, repo: str | None = None) -> str:
    scope = f" in {repo}" if repo else ""
    return f"No {subject} found for '{keyword}'{scope}."


def split_repo(repo: str) -> tuple[str, str]:
    owner, repo_name = repo.split("/", 1)
    return owner, repo_name


def extract_keywords(query: str) -> list[str]:
    return query.split()[:MAX_KEYWORDS]


def search_with_keyword_fallback(keywords: list[str], search) -> tuple[int, object, int]:
    total = 0
    payload = None
    for k in range(len(keywords), 0, -1):
        sub_query = " ".join(keywords[:k])
        total, payload = search(sub_query)
        if total > 0:
            if k < len(keywords):
                logger.info("Keyword fallback: '%s' produced the hits", sub_query)
            return total, payload, k
    return total, payload, 0


def build_fallback_note(kw_level: int, keywords: list[str]) -> str:
    if kw_level >= len(keywords):
        return ""
    return f" (fell back to {kw_level} keyword{'s' if kw_level != 1 else ''})"
