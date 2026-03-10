# GitHub Research Plugin

GitHub API tools for Claude Code - search repos, code, issues, PRs, discussions.

## Installation

### As Plugin (recommended)

In a Claude Code session:

```
/plugin marketplace add brunowinter8192/claude-plugins
/plugin install github-research
```

Restart the session after installation.

### Manual (.mcp.json)

Add to your project's `.mcp.json` (all paths must be absolute):

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

### GitHub Token (optional)

Set `GH_TOKEN` in your shell for authenticated access (higher rate limits):

```bash
# Add to ~/.zshrc or ~/.bashrc
export GH_TOKEN="ghp_your_token_here"
```

Without a token, tools work but hit GitHub's unauthenticated rate limit (~60 req/hour).

## Plugin Components

| Component | Name | Description |
|-----------|------|-------------|
| **Skill** | `/github-research:gh-search` | Tool usage context and workflows |
| **MCP Server** | `github` | 21 GitHub API tools |
| **Subagent** | `github-search` | Deep research specialist |

## MCP Tools

### search_repos

Find repositories by topic, language, or keyword.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | required | Search query with GitHub qualifiers (e.g., `"fastapi stars:>1000"`) |
| `sort_by` | `"stars"` / `"forks"` / `"updated"` / `"best_match"` | `"best_match"` | Sort order |

### search_code

Find code snippets and implementation patterns across GitHub.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | required | Code search query |

### get_repo

Get repository metadata including topics, license, and stats.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |

### get_repo_tree

Browse repository file structure with optional filtering.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `path` | string | `""` | Subdirectory path |
| `depth` | int | `-1` | Tree depth (`-1` = full) |
| `pattern` | string | `""` | Glob filter (e.g., `"*.py"`) |

### get_file_content

Read file content with optional pagination for large files.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `path` | string | required | File path |
| `metadata_only` | bool | `false` | Return only metadata |
| `offset` | int | `0` | Start line (pagination) |
| `limit` | int | `0` | Max lines (`0` = all) |

### grep_file

Search file content by regex pattern without downloading entire file.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `path` | string | required | File path |
| `pattern` | string | required | Regex pattern |
| `context_lines` | int | `0` | Lines before/after match |
| `max_matches` | int | `50` | Max results |

### grep_repo

Search file content across repo by file pattern. Fallback when `search_code` fails on data files.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `pattern` | string | required | Regex pattern |
| `file_pattern` | string | `"*.csv"` | File glob filter |
| `path` | string | `""` | Subdirectory scope |
| `max_files` | int | `10` | Max files to search |

### search_items

Find issues or PRs across GitHub.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | required | Search query |
| `type` | `"issue"` / `"pr"` | required | Item type |
| `sort_by` | `"comments"` / `"reactions"` / `"created"` / `"updated"` / `"best_match"` | `"best_match"` | Sort order |

### get_issue / get_issue_comments

Get issue details or discussion thread.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `issue_number` | int | required | Issue number |

### list_repo_prs

List pull requests in a repository.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `state` | `"open"` / `"closed"` / `"all"` | `"open"` | PR state filter |
| `sort_by` | `"created"` / `"updated"` / `"popularity"` / `"long-running"` | `"created"` | Sort order |

### get_pr / get_pr_files

Get PR details or list changed files.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `pull_number` | int | required | PR number |

### list_commits

Browse commit history with optional filters.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `sha` | string | `""` | Branch or SHA to start from |
| `path` | string | `""` | Only commits touching this file |
| `author` | string | `""` | Filter by author (username or email) |
| `per_page` | int | `20` | Number of results |

### compare_commits

Compare two branches, tags, or SHAs.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `base` | string | required | Base branch, tag, or SHA |
| `head` | string | required | Head branch, tag, or SHA |

### list_releases

List releases with version tags and changelogs.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `per_page` | int | `10` | Number of results |

### get_release

Get a single release with full release notes. Without tag returns latest release.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `tag` | string | `null` | Version tag (e.g., `"v2.1.72"`). Omit for latest |

### search_discussions

Find discussions across GitHub.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | required | Search query |
| `first` | int | `10` | Number of results |

### list_discussions

Browse discussions in a specific repository.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `first` | int | `10` | Number of results |
| `category` | string | `null` | Filter by category |
| `answered` | bool | `null` | Filter by answered status |

### get_discussion

Read full discussion with comments.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `owner` | string | required | Repository owner |
| `repo` | string | required | Repository name |
| `number` | int | required | Discussion number |
| `comment_limit` | int | `50` | Max comments |
| `comment_sort` | `"upvotes"` / `"chronological"` | `"upvotes"` | Comment sort order |

## Component Details

### Skill

- **Trigger:** `ghs` in prompt
- **Manual:** `/github-research:gh-search`
- **Content:** Tool context, workflows, when-to-use guidance

### MCP Server

- 20 read-only GitHub API tools
- **Required for private repos:** Set `GITHUB_TOKEN` or `GH_TOKEN` as system env var
- Without token: public repos only, lower rate limits

### Subagent

- **Type:** `github-search`
- **Use for:** Complex multi-tool research, comparing repos
- **Skip for:** Single tool calls, known owner/repo

## Directory Structure

```
github/
├── .claude-plugin/           # Plugin distribution
│   ├── plugin.json           # Plugin metadata
│   ├── marketplace.json      # Marketplace entry
│   ├── .mcp.json             # MCP server config
│   ├── skills/github/SKILL.md
│   └── agents/github-search.md
├── server.py                 # MCP entry point
└── src/github/               # Tool implementations
    └── DOCS.md
```

## Documentation

| Doc | Content |
|-----|---------|
| `src/github/DOCS.md` | Tool implementation details |
| `.claude-plugin/skills/github/SKILL.md` | Tool usage guide |
| `.claude-plugin/agents/github-search.md` | Subagent instructions |

## Development

Local testing without installation:

```bash
claude --plugin-dir ./github
```
