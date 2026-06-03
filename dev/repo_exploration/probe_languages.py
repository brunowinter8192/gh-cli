"""
Probe: GET /repos/{owner}/{repo}/languages

Demonstrates: language byte breakdown — each language mapped to the number of bytes
of code GitHub detected. Useful for tech-stack orientation in one call.

Usage (from project root):
  .venv/bin/python dev/repo_exploration/probe_languages.py <owner> <repo>
"""
# INFRASTRUCTURE
import argparse
import requests
from probe_client import GITHUB_API_BASE, build_headers


# ORCHESTRATOR
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("owner")
    parser.add_argument("repo")
    args = parser.parse_args()
    print(fetch_and_print(args.owner, args.repo))


# FUNCTIONS

# Fetch language breakdown and return formatted string
def fetch_and_print(owner: str, repo: str) -> str:
    response = requests.get(
        f"{GITHUB_API_BASE}/repos/{owner}/{repo}/languages",
        headers=build_headers()
    )
    response.raise_for_status()
    data = response.json()

    if not data:
        return "No language data returned (repo may be empty or undetected)."

    total = sum(data.values())
    lines = []
    for lang, nbytes in sorted(data.items(), key=lambda x: x[1], reverse=True):
        pct = nbytes / total * 100
        lines.append(f"  {lang:<20} {nbytes:>10,} bytes  ({pct:.1f}%)")
    lines.append(f"\n  total: {total:,} bytes")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
