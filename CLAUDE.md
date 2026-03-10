# CLAUDE.MD - MCP Server Engineering Reference

## PROJECT

- **GitHub Repo:** `brunowinter8192/github-MCP`
- **Bugs:** GitHub Issues (`gh issue create --repo brunowinter8192/github-MCP`)

---

## General

- NO emojis in production code, READMEs, DOCS.md, logs
- ALWAYS keep script console output concise
- `endpoints.md` lists all 47 GitHub REST API categories with `[RAG]` markers for those available via vector search

### Plugin Distribution

`.claude-plugin/` is the plugin distribution folder (tracked in git). Edit files directly here.

New tools MUST be registered in 5 places: `server.py`, `.claude-plugin/skills/github/SKILL.md`, `.claude-plugin/agents/github-search.md`, `src/github/DOCS.md`, `README.md`

### Testing

**CRITICAL:** Test MCP tools by calling them directly via MCP tool calls, NOT via Python import.

**RIGHT:**
```
mcp__github__get_repo_tree(owner="anthropics", repo="claude-code", depth=1)
```

**WRONG:**
```bash
source .venv/bin/activate && python -c "from src.github.get_repo_tree import ..."
```

**Rules:**
- The MCP server runs as a separate process - there is no local venv to activate
- Always use `mcp__github__<tool_name>(...)` to verify tool behavior
- Test both default parameters and new/changed parameters
- **After code changes:** MCP server must be restarted before tool calls reflect changes. Ask user to restart (`/mcp` in Claude Code) before running verification tests
- **Plugin-based project:** When no `.mcp.json` exists (project uses plugin distribution), test via curl against GitHub API directly. The API response shapes are identical to what the MCP module processes. Use `debug/test_endpoints.sh` pattern for reproducible verification with markdown output.

---

## server.py (MCP Entry Point)

**Purpose:** MCP server exposing tools to Claude Code. Only imports and tool definitions.

```python
# INFRASTRUCTURE
from typing import Literal
from fastmcp import FastMCP
from dotenv import load_dotenv
from mcp.types import TextContent

load_dotenv()

from src.github.search_repos import search_repos_workflow
from src.github.get_file_content import get_file_content_workflow

mcp = FastMCP("GitHub")


# TOOLS

@mcp.tool
def search_repos(
    query: str,
    sort_by: Literal["stars", "forks", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    """Search GitHub repositories. Use when user wants to find projects, libraries, or frameworks."""
    return search_repos_workflow(query, sort_by)


@mcp.tool
def get_file_content(owner: str, repo: str, path: str) -> list[TextContent]:
    """Get file content from a repository. Use after browsing repo tree to read specific files."""
    return get_file_content_workflow(owner, repo, path)


if __name__ == "__main__":
    mcp.run()
```

**Rules:**
- NO business logic in server.py
- Each tool delegates to module orchestrator
- Literal for enum-like choices
- Returns list[TextContent] for MCP compatibility
- **Merge-First:** Before adding a new tool, check if an existing tool can absorb the functionality via an additional parameter. Fewer tools = less context overhead for the model. Only create a separate tool when the use case, API endpoint, or output format is fundamentally different.

---

## MODULE PATTERN (src/github/tool_name.py)

**CRITICAL:** Each module follows INFRASTRUCTURE -> ORCHESTRATOR -> FUNCTIONS

### Starter Pattern (1-3 modules)

For small MCPs, define constants directly in each module:

```python
# INFRASTRUCTURE
import os
import requests
from mcp.types import TextContent

API_BASE = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
RESULTS_LIMIT = 20


# ORCHESTRATOR
def search_repos_workflow(query: str, sort_by: str) -> list[TextContent]:
    raw_data = search_repos_api(query, sort_by)
    return format_response(raw_data)


# FUNCTIONS

# Call GitHub search API
def search_repos_api(query: str, sort_by: str) -> dict:
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    params = {"q": query, "sort": sort_by, "per_page": RESULTS_LIMIT}
    response = requests.get(f"{API_BASE}/search/repositories", headers=headers, params=params)
    response.raise_for_status()
    return response.json()


# Format API response for MCP output
def format_response(data: dict) -> list[TextContent]:
    items = data.get("items", [])
    lines = [f"{r['full_name']} ({r['stargazers_count']} stars)" for r in items]
    return [TextContent(type="text", text="\n".join(lines))]
```

### Scaled Pattern (4+ modules)

For larger MCPs, extract shared infrastructure to `client.py`:

**client.py:**
```python
# INFRASTRUCTURE
import os

GITHUB_API_BASE = "https://api.github.com"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
RESULTS_PER_PAGE = 20


# FUNCTIONS

# Build headers with optional auth token
def build_headers(accept: str = "application/vnd.github+json") -> dict:
    headers = {
        "Accept": accept,
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers
```

**Module using client.py:**
```python
# INFRASTRUCTURE
import requests
from mcp.types import TextContent
from src.github.client import GITHUB_API_BASE, RESULTS_PER_PAGE, build_headers


# ORCHESTRATOR
def search_repos_workflow(query: str, sort_by: str) -> list[TextContent]:
    raw_data = fetch_repositories(query, sort_by)
    return [TextContent(type="text", text=format_response(raw_data))]


# FUNCTIONS

# Fetch repositories from GitHub Search API
def fetch_repositories(query: str, sort_by: str) -> dict:
    url = f"{GITHUB_API_BASE}/search/repositories"
    params = {"q": query, "per_page": RESULTS_PER_PAGE}
    response = requests.get(url, params=params, headers=build_headers())
    response.raise_for_status()
    return response.json()
```

**When to scale:** Refactor to client.py when you have 4+ modules with duplicated constants/headers.

**Note:** `client.py` is a utility module (no ORCHESTRATOR section). It only has INFRASTRUCTURE + FUNCTIONS because it's imported by other modules, not called from server.py.

**Section definitions:**

**INFRASTRUCTURE:**
- Imports and constants (or imports from client.py)
- Module-specific constants stay local (e.g., MAX_PATCH_PREVIEW)
- NO functions
- NO logic

**ORCHESTRATOR:**
- ONE function (named: tool_name_workflow)
- Called by server.py tool definition
- Calls internal functions in sequence
- No business logic (only function composition + protocol wrapping)

**FUNCTIONS:**
- Ordered by call sequence
- One responsibility each
- Function header comment (one line describing WHAT)
- NO comments inside function bodies (only header comments + section markers)
- Type hints: RECOMMENDED but optional
- When combining functions from multiple modules: verify path conventions are compatible (e.g., Trees API returns paths relative to subtree scope, Contents API requires full repo-relative paths)

---

## TOOL PARAMETER DESIGN

**CRITICAL:** Keep tool definitions lean. Documentation belongs in SKILL.md.

### Lean Tools + Skill Pattern

Tool definitions stay minimal to save context tokens. Detailed descriptions go in SKILL.md.

**server.py (lean):**
```python
@mcp.tool
def search_repos(
    query: str,
    sort_by: Literal["stars", "forks", "updated", "best_match"] = "best_match"
) -> list[TextContent]:
    """Search repos. Use to find projects, libraries, or frameworks."""
    return search_repos_workflow(query, sort_by)
```

**SKILL.md (detailed):**
```markdown
### search_repos
| Parameter | Description |
|-----------|-------------|
| query | Search query with GitHub qualifiers (e.g., "fastapi stars:>1000") |
| sort_by | Sort by: stars (popularity), forks, updated, best_match (relevance) |
```

**Rules:**
- NO `Annotated[str, Field(description="...")]` in tool definitions
- Docstring: One sentence (what + when)
- Parameter details: Only in SKILL.md

---

## TOOL OUTPUT DESIGN

**CRITICAL:** Output must be list[TextContent] for MCP compatibility

```python
from mcp.types import TextContent

def format_response(data: dict) -> list[TextContent]:
    text = format_as_string(data)
    return [TextContent(type="text", text=text)]
```

**Principles:**
- Always return list[TextContent]
- Human-readable text format
- Include relevant metadata (stars, dates, etc.)

---

## ERROR HANDLING

**Fail-Fast:** Let exceptions fly. No try-catch that silently swallows errors affecting business logic. Script must fail if it cannot fulfill its purpose.

**ALLOWED:**
- Retry logic with exponential backoff
- Graceful degradation with explicit logging
- Resource cleanup (connections)

**PROHIBITED:**
- Silently swallowing errors
- Generic `except Exception: pass`
- Hiding failures that affect business logic

```python
response = requests.get(url, headers=headers)
response.raise_for_status()  # Raises on 4xx/5xx
return response.json()
```

FastMCP handles exceptions and communicates errors to client.

---

## DOCUMENTATION STRUCTURE

### Hierarchy

```
github/
├── README.md                 # User docs (install, components, usage)
├── .claude-plugin/
│   ├── skills/.../SKILL.md   # Tool usage guide (for Claude)
│   └── agents/...md          # Subagent instructions (for Claude)
└── src/github/
    └── DOCS.md               # Implementation docs (for developers)
```

**Principles:**
- README = What users need to know
- SKILL.md = What Claude needs to use tools
- DOCS.md = What developers need to modify code

**File Organization:**
- NO test files in root (ONLY in debug/ folders - root or per-module)
- NO debug/ or logs/ folders in version control (MUST be in .gitignore)

---

## CLAUDE CODE INTEGRATION (.mcp.json)

**CRITICAL:** Each MCP server needs .mcp.json for Claude Code registration.

```json
{
  "mcpServers": {
    "github": {
      "command": "/absolute/path/to/venv/bin/fastmcp",
      "args": ["run", "/absolute/path/to/server.py"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Rules:**
- ALL paths MUST be absolute (no relative paths)
- NO cwd field (unreliable in Claude Code)
- Use ${VAR_NAME} syntax for secrets

---

## NAMING CONVENTIONS

**server.py:** Always named server.py
**Domain folder:** src/github/
**Shared client:** src/github/client.py (for scaled pattern)
**Modules:** src/github/search_repos.py, src/github/get_issue.py
**Package markers:** src/__init__.py and src/github/__init__.py
**Orchestrator function:** tool_name_workflow()
**MCP tool function:** @mcp.tool def tool_name()

---

## RAG COLLECTIONS

| Collection | Content |
|------------|---------|
| `APIEndpoints` | GitHub REST API documentation (9 docs, 1141 chunks) |
| `GraphQL_GH` | GitHub GraphQL API schema and docs (1975 chunks) |

### APIEndpoints Documents

| Document | Chunks | API Category |
|----------|--------|--------------|
| Repos.md | 451 | Repositories |
| PullRequests.md | 180 | Pull requests |
| Code_Scanning.md | 153 | Code scanning |
| issues.md | 128 | Issues |
| SearchDocs.md | 79 | Search |
| Commits.md | 88 | Commits |
| Releases.md | 53 | Releases |
| trees.md | 5 | Git database |
| Maekdown.md | 4 | Markdown |

Use `collection="APIEndpoints"` for REST API searches, `collection="GraphQL_GH"` for GraphQL schema searches.

