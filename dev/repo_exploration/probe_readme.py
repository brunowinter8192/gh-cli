"""
Probe: GET /repos/{owner}/{repo}/readme  (and /readme/{dir} if dir given)

Demonstrates: GitHub returns the preferred README regardless of filename (README.md,
readme.rst, README.txt, etc.) without caller needing to guess the name.
Content is base64-encoded in the default JSON response.

Usage (from project root):
  .venv/bin/python dev/repo_exploration/probe_readme.py <owner> <repo> [dir]
"""
# INFRASTRUCTURE
import argparse
import base64
import requests
from probe_client import GITHUB_API_BASE, build_headers


# ORCHESTRATOR
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("owner")
    parser.add_argument("repo")
    parser.add_argument("dir", nargs="?", default=None,
                        help="Subdirectory to find README in (optional)")
    args = parser.parse_args()
    result = fetch_and_print(args.owner, args.repo, args.dir)
    print(result)


# FUNCTIONS

# Fetch README and return formatted string
def fetch_and_print(owner: str, repo: str, subdir: str | None) -> str:
    path = f"/repos/{owner}/{repo}/readme"
    if subdir:
        path += f"/{subdir}"
    response = requests.get(f"{GITHUB_API_BASE}{path}", headers=build_headers())
    response.raise_for_status()
    data = response.json()

    raw = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    lines = raw.splitlines()
    preview = "\n".join(lines[:40])
    truncated = f"\n... ({len(lines) - 40} more lines)" if len(lines) > 40 else ""

    return (
        f"name:  {data['name']}\n"
        f"path:  {data['path']}\n"
        f"size:  {data['size']} bytes  ({len(lines)} lines)\n"
        f"\n{preview}{truncated}"
    )


if __name__ == "__main__":
    main()
