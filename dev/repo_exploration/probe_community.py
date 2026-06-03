"""
Probe: GET /repos/{owner}/{repo}/community/profile

Demonstrates: community health score + a map of which standard anchor files exist
(README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, issue template, PR template) and
their paths — all in one call.

Usage (from project root):
  .venv/bin/python dev/repo_exploration/probe_community.py <owner> <repo>
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

# Fetch community profile and return formatted string
def fetch_and_print(owner: str, repo: str) -> str:
    response = requests.get(
        f"{GITHUB_API_BASE}/repos/{owner}/{repo}/community/profile",
        headers=build_headers()
    )
    response.raise_for_status()
    data = response.json()

    lines = []
    lines.append(f"health:      {data.get('health_percentage', '?')}%")
    lines.append(f"description: {data.get('description') or '(none)'}")
    lines.append(f"updated_at:  {data.get('updated_at', '?')}")
    lines.append("")
    lines.append("files:")

    for key, val in sorted((data.get("files") or {}).items()):
        if val is None:
            lines.append(f"  {key:<30} absent")
        else:
            location = val.get("path") or val.get("url") or "(present)"
            lines.append(f"  {key:<30} {location}")

    return "\n".join(lines)


if __name__ == "__main__":
    main()
