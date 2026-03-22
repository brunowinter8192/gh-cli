# GitHub Research MCP Server

GitHub API tools for searching repos, code, issues, PRs, discussions.

## Sources

See [sources/sources.md](sources/sources.md).

## Pipeline Components

### API Layer

| Component | Implementation | Config |
|-----------|---------------|--------|
| **REST Client** | `src/github/client.py` — shared headers, auth | `GH_TOKEN` env var, `RESULTS_PER_PAGE=20` |
| **GraphQL Client** | `src/github/graphql_client.py` | Discussions API (no REST endpoint exists) |
| **Query Truncation** | `src/github/search_repos.py` | `MAX_QUERY_WORDS=3` (GitHub returns 0 for long queries) |

### Delivery

| Component | Implementation | Config |
|-----------|---------------|--------|
| **MCP Server** | `server.py` via FastMCP | 21 tools (20 REST, 1 GraphQL) |

### Key Files

| File | Purpose |
|------|---------|
| `server.py` | MCP server — tool definitions, delegates to src/github/ |
| `src/github/client.py` | Shared infrastructure — API base URL, auth headers, constants |
| `src/github/graphql_client.py` | GraphQL client for Discussions API |
| `src/github/DOCS.md` | Tool reference documentation |

## Project Structure

```
github/
├── server.py
├── requirements.txt
├── README.md                       → [Setup & External Docs](README.md)
├── decisions/
├── src/
│   └── github/                     → [DOCS.md](src/github/DOCS.md)
├── .claude-plugin/                 → Plugin distribution
```
