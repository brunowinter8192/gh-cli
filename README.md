# GitHub Research

GitHub API tools for Claude Code — search repos, code, issues, PRs, discussions, and explore any repository.

## Features

- **Full GitHub Search** — repos, code snippets, issues, PRs, and discussions in one plugin
- **Repository Exploration** — browse file trees, read files, grep content without cloning
- **PR & Commit Analysis** — inspect diffs, changed files, commit history, branch comparisons
- **Release Tracking** — list releases and read changelogs
- **Autonomous Research Agent** — dispatches multi-tool GitHub investigations automatically

## Quick Start

```
/plugin marketplace add brunowinter8192/claude-plugins
/plugin install github-research
# Restart session
```

## Prerequisites

- Python 3.10+
- `GH_TOKEN` environment variable (optional, recommended — see Setup)

## Setup

**Plugin install** (Quick Start above) handles everything automatically.

**GitHub Token (recommended):**

```bash
# Add to ~/.zshrc or ~/.bashrc
export GH_TOKEN="ghp_your_token_here"
```

Without a token the plugin works on public repos at 60 requests/hour. With a token: 5000 requests/hour.

**Manual install** (without plugin system):

```json
{
  "mcpServers": {
    "github": {
      "command": "uvx",
      "args": ["--with", "requests", "fastmcp", "run", "/absolute/path/to/server.py"],
      "env": { "GITHUB_TOKEN": "${GH_TOKEN}" }
    }
  }
}
```

## Usage

### MCP Tools

| Tool | What it does | When to use |
|------|-------------|-------------|
| `search_repos` | Find repositories by topic, language, keyword | Discover projects or alternatives |
| `search_code` | Find code patterns across GitHub | Find implementation examples |
| `search_items` | Search issues or PRs across GitHub | Track bugs, feature requests, merged changes |
| `search_discussions` | Find discussions across GitHub | Community Q&A, design decisions |
| `get_repo` | Repository metadata, topics, stats | Quick overview before diving in |
| `get_repo_tree` | Browse file structure with optional filtering | Understand project layout |
| `get_file_content` | Read file content with pagination | Read source files |
| `grep_file` | Regex search within a single file | Find specific code in a known file |
| `grep_repo` | Regex search across all repo files | Find patterns when `search_code` returns nothing |
| `get_issue` / `get_issue_comments` | Issue details and full discussion thread | Understand a reported bug or request |
| `list_repo_prs` | List PRs with state and sort filters | See what's merged, open, or in review |
| `get_pr` / `get_pr_files` | PR details and list of changed files | Review a specific pull request |
| `list_commits` / `compare_commits` | Commit history or diff between branches/tags | Track changes over time |
| `list_releases` / `get_release` | Releases with changelogs | Check latest version or release notes |
| `list_discussions` / `get_discussion` | Discussions in a specific repo | Read community conversations |

### Skills & Commands

- **`/github-research:agent-github-search`** — Tool reference and usage workflows for the GitHub search agent. Activate when doing multi-step research.

### Agents

- **`github-search`** — Autonomous deep-research specialist. Chains multiple tools to investigate repos, compare libraries, or trace issues. Dispatch for complex multi-tool tasks; use direct tool calls for single lookups.

## Workflows

**Researching a library:**
`search_repos` → `get_repo` for stats → `get_repo_tree` to understand structure → `get_file_content` or `grep_repo` to read implementation details.

**Investigating an issue:**
`search_items` (or known issue number) → `get_issue` → `get_issue_comments` for full discussion → `list_repo_prs` to find the fix → `get_pr_files` to see what changed.

**Comparing implementations:**
Dispatch the `github-search` agent with a research question — it searches, reads, and compares across repos automatically.

## Troubleshooting

<details>
<summary>Rate limit exceeded</summary>

Without a token GitHub allows ~60 requests/hour. Set `GH_TOKEN` in your shell and restart:

```bash
export GH_TOKEN="ghp_your_token_here"
```

Authenticated requests get 5000/hour.
</details>

<details>
<summary>search_code returns empty results</summary>

GitHub code search has indexing limitations — not all repos or files are indexed. Fallbacks:

1. Use `grep_repo` on a known repo to search file content directly
2. Use `get_repo_tree` + `get_file_content` to read files manually
3. Try shorter, more specific queries (GitHub truncates long queries internally)
</details>

<details>
<summary>Tools not available after install</summary>

Restart your Claude Code session after installing the plugin. MCP servers are loaded at session start.
</details>

## License

MIT
