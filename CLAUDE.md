# GitHub Research MCP Server

GitHub API tools for searching repos, code, issues, PRs, discussions.

## Sources

| Source | Purpose |
|--------|---------|
| RAG Collection `APIEndpoints` | GitHub REST API (9 docs, 1141 chunks) |
| RAG Collection `GraphQL_GH` | GitHub GraphQL schema (1975 chunks) |
| endpoints.md | 47 REST API categories with [RAG] markers |

## Project Structure

```
github/
├── server.py
├── requirements.txt
├── README.md                       → [Setup & External Docs](README.md)
├── src/
│   └── github/                     → [DOCS.md](src/github/DOCS.md)
├── .claude-plugin/                 Plugin distribution (edit directly here)
```
