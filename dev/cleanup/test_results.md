# GitHub API Endpoint Verification

Repo: anthropics/claude-code
Date: 2026-03-05T23:34:27Z

## 1. GET /repos/{owner}/{repo}/topics

```
GET /repos/anthropics/claude-code/topics
```

**Response:**

```json
{
    "names": []
}
```

## 2. GET Topics (own repo - brunowinter8192/github-MCP)

Shows current topics. PUT would replace these.

**Response:**

```json
{
    "names": []
}
```

**PUT endpoint:** `PUT /repos/{owner}/{repo}/topics` with body `{"names": ["topic1", "topic2"]}`

## 3. GET /repos/{owner}/{repo}/commits

```
GET /repos/anthropics/claude-code/commits?per_page=3
```

**Response (first 3 commits, key fields):**

```json
{
  "sha": "9582ad4",
  "message": "chore: Update CHANGELOG.md",
  "author": "GitHub Actions",
  "date": "2026-03-05T00:25:31Z",
  "url": "https://github.com/anthropics/claude-code/commit/9582ad480f687bbeaf0025852ac4f020b07f20bb"
}
---
{
  "sha": "0b3f7cb",
  "message": "chore: Update CHANGELOG.md",
  "author": "GitHub Actions",
  "date": "2026-03-04T10:10:30Z",
  "url": "https://github.com/anthropics/claude-code/commit/0b3f7cbbbd8c0e78c4bb63134ead608c555df5de"
}
---
{
  "sha": "a833523",
  "message": "chore: Update CHANGELOG.md",
  "author": "GitHub Actions",
  "date": "2026-03-04T02:23:29Z",
  "url": "https://github.com/anthropics/claude-code/commit/a8335230bc62baae60c8eb18ae77ab32123454bd"
}
---
```

### 3b. Commits with path filter

```
GET /repos/anthropics/claude-code/commits?per_page=2&path=README.md
```

**Response (commits touching README.md):**

```json
{
  "sha": "b640d94",
  "message": "docs: update installation instructions in README",
  "date": "2026-01-12T23:11:57Z"
}
---
{
  "sha": "24ad98a",
  "message": "docs: Fix links to Claude Code docs in README.",
  "date": "2026-01-06T14:47:41Z"
}
---
```

## 4. GET /repos/{owner}/{repo}/compare/{base}...{head}

```
GET /repos/anthropics/claude-code/compare/main~5...main
```

**Comparing:** `26a1334...9582ad4`

**Response (summary):**

```json
{
  "status": "ahead",
  "ahead_by": 5,
  "behind_by": 0,
  "total_commits": 5,
  "files_changed": 1,
  "commits": [
    {
      "sha": "38281cf",
      "message": "Merge pull request #30066 from anthropics/oct/gh-wrapper-imp"
    },
    {
      "sha": "9c63e98",
      "message": "chore: Update CHANGELOG.md"
    },
    {
      "sha": "a833523",
      "message": "chore: Update CHANGELOG.md"
    },
    {
      "sha": "0b3f7cb",
      "message": "chore: Update CHANGELOG.md"
    },
    {
      "sha": "9582ad4",
      "message": "chore: Update CHANGELOG.md"
    }
  ],
  "files_sample": [
    {
      "filename": "CHANGELOG.md",
      "status": "modified",
      "additions": 116,
      "deletions": 0
    }
  ]
}
```

## 5. GET /repos/{owner}/{repo}/releases

```
GET /repos/anthropics/claude-code/releases?per_page=3
```

**Response (first 3 releases, key fields):**

```json
{
  "tag_name": "v2.1.69",
  "name": "v2.1.69",
  "published_at": "2026-03-05T00:26:21Z",
  "prerelease": false,
  "draft": false,
  "assets_count": 0,
  "body_preview": "## What's changed\n\n- Added the `/claude-api` skill for building applications with the Claude API and Anthropic SDK\n- Added Ctrl+U on an empty bash prompt (`!`) to exit bash mode, matching `escape` and...",
  "html_url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.69"
}
---
{
  "tag_name": "v2.1.68",
  "name": "v2.1.68",
  "published_at": "2026-03-04T10:11:14Z",
  "prerelease": false,
  "draft": false,
  "assets_count": 0,
  "body_preview": "## What's changed\n\n- Opus 4.6 now defaults to medium effort for Max and Team subscribers. Medium effort works well for most tasks \u2014 it's the sweet spot between speed and thoroughness. You can change t...",
  "html_url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.68"
}
---
{
  "tag_name": "v2.1.66",
  "name": "v2.1.66",
  "published_at": "2026-03-04T01:19:19Z",
  "prerelease": false,
  "draft": false,
  "assets_count": 0,
  "body_preview": "\n",
  "html_url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.66"
}
---
```

## Summary

| Endpoint | Status | Notes |
|----------|--------|-------|
| GET topics | OK | 0 topics |
| GET commits | OK | 3 commits returned |
| GET compare | OK | 5 commits, 1 files |
| GET releases | OK | 3 releases returned |
