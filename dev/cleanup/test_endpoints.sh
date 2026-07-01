#!/bin/bash
# Test GitHub REST API endpoints for new MCP tools
# Output: Markdown format for verification
# Usage: ./debug/test_endpoints.sh > debug/test_results.md

REPO_OWNER="anthropics"
REPO_NAME="claude-code"
TOKEN="${GH_TOKEN:-${GITHUB_TOKEN:-}}"

if [ -z "$TOKEN" ]; then
    echo "ERROR: No GitHub token found. Set GH_TOKEN or GITHUB_TOKEN."
    exit 1
fi

AUTH_HEADER="Authorization: Bearer $TOKEN"
API_HEADER="X-GitHub-Api-Version: 2022-11-28"
ACCEPT="Accept: application/vnd.github+json"

echo "# GitHub API Endpoint Verification"
echo ""
echo "Repo: ${REPO_OWNER}/${REPO_NAME}"
echo "Date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""

# --- 1. GET Topics ---
echo "## 1. GET /repos/{owner}/{repo}/topics"
echo ""
echo "\`\`\`"
echo "GET /repos/${REPO_OWNER}/${REPO_NAME}/topics"
echo "\`\`\`"
echo ""

TOPICS=$(curl -s \
    -H "$AUTH_HEADER" \
    -H "$API_HEADER" \
    -H "$ACCEPT" \
    "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/topics")

echo "**Response:**"
echo ""
echo "\`\`\`json"
echo "$TOPICS" | python3 -m json.tool 2>/dev/null || echo "$TOPICS"
echo "\`\`\`"
echo ""

# --- 2. GET Topics (own repo, to show PUT would work) ---
echo "## 2. GET Topics (own repo - brunowinter8192/github-MCP)"
echo ""
echo "Shows current topics. PUT would replace these."
echo ""

OWN_TOPICS=$(curl -s \
    -H "$AUTH_HEADER" \
    -H "$API_HEADER" \
    -H "$ACCEPT" \
    "https://api.github.com/repos/brunowinter8192/github-MCP/topics")

echo "**Response:**"
echo ""
echo "\`\`\`json"
echo "$OWN_TOPICS" | python3 -m json.tool 2>/dev/null || echo "$OWN_TOPICS"
echo "\`\`\`"
echo ""
echo "**PUT endpoint:** \`PUT /repos/{owner}/{repo}/topics\` with body \`{\"names\": [\"topic1\", \"topic2\"]}\`"
echo ""

# --- 3. GET Commits ---
echo "## 3. GET /repos/{owner}/{repo}/commits"
echo ""
echo "\`\`\`"
echo "GET /repos/${REPO_OWNER}/${REPO_NAME}/commits?per_page=3"
echo "\`\`\`"
echo ""

COMMITS=$(curl -s \
    -H "$AUTH_HEADER" \
    -H "$API_HEADER" \
    -H "$ACCEPT" \
    "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/commits?per_page=3")

echo "**Response (first 3 commits, key fields):**"
echo ""
echo "\`\`\`json"
echo "$COMMITS" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for c in data[:3]:
    print(json.dumps({
        'sha': c['sha'][:7],
        'message': c['commit']['message'].split('\n')[0][:80],
        'author': c['commit']['author']['name'],
        'date': c['commit']['author']['date'],
        'url': c['html_url']
    }, indent=2))
    print('---')
" 2>/dev/null || echo "$COMMITS"
echo "\`\`\`"
echo ""

# --- 3b. GET Commits with filters ---
echo "### 3b. Commits with path filter"
echo ""
echo "\`\`\`"
echo "GET /repos/${REPO_OWNER}/${REPO_NAME}/commits?per_page=2&path=README.md"
echo "\`\`\`"
echo ""

COMMITS_PATH=$(curl -s \
    -H "$AUTH_HEADER" \
    -H "$API_HEADER" \
    -H "$ACCEPT" \
    "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/commits?per_page=2&path=README.md")

echo "**Response (commits touching README.md):**"
echo ""
echo "\`\`\`json"
echo "$COMMITS_PATH" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for c in data[:2]:
    print(json.dumps({
        'sha': c['sha'][:7],
        'message': c['commit']['message'].split('\n')[0][:80],
        'date': c['commit']['author']['date']
    }, indent=2))
    print('---')
" 2>/dev/null || echo "$COMMITS_PATH"
echo "\`\`\`"
echo ""

# --- 4. GET Compare ---
echo "## 4. GET /repos/{owner}/{repo}/compare/{base}...{head}"
echo ""
echo "\`\`\`"
echo "GET /repos/${REPO_OWNER}/${REPO_NAME}/compare/main~5...main"
echo "\`\`\`"
echo ""

# First get a recent SHA to compare against
RECENT_SHAS=$(curl -s \
    -H "$AUTH_HEADER" \
    -H "$API_HEADER" \
    -H "$ACCEPT" \
    "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/commits?per_page=6")

BASE_SHA=$(echo "$RECENT_SHAS" | python3 -c "import sys,json; data=json.load(sys.stdin); print(data[5]['sha'])" 2>/dev/null)
HEAD_SHA=$(echo "$RECENT_SHAS" | python3 -c "import sys,json; data=json.load(sys.stdin); print(data[0]['sha'])" 2>/dev/null)

if [ -n "$BASE_SHA" ] && [ -n "$HEAD_SHA" ]; then
    COMPARE=$(curl -s \
        -H "$AUTH_HEADER" \
        -H "$API_HEADER" \
        -H "$ACCEPT" \
        "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/compare/${BASE_SHA}...${HEAD_SHA}")

    echo "**Comparing:** \`${BASE_SHA:0:7}...${HEAD_SHA:0:7}\`"
    echo ""
    echo "**Response (summary):**"
    echo ""
    echo "\`\`\`json"
    echo "$COMPARE" | python3 -c "
import sys, json
data = json.load(sys.stdin)
summary = {
    'status': data.get('status'),
    'ahead_by': data.get('ahead_by'),
    'behind_by': data.get('behind_by'),
    'total_commits': data.get('total_commits'),
    'files_changed': len(data.get('files', [])),
    'commits': [
        {'sha': c['sha'][:7], 'message': c['commit']['message'].split(chr(10))[0][:60]}
        for c in data.get('commits', [])[:5]
    ],
    'files_sample': [
        {'filename': f['filename'], 'status': f['status'], 'additions': f['additions'], 'deletions': f['deletions']}
        for f in data.get('files', [])[:5]
    ]
}
print(json.dumps(summary, indent=2))
" 2>/dev/null || echo "$COMPARE" | head -50
    echo "\`\`\`"
else
    echo "**ERROR:** Could not fetch SHAs for comparison"
fi
echo ""

# --- 5. GET Releases ---
echo "## 5. GET /repos/{owner}/{repo}/releases"
echo ""
echo "\`\`\`"
echo "GET /repos/${REPO_OWNER}/${REPO_NAME}/releases?per_page=3"
echo "\`\`\`"
echo ""

RELEASES=$(curl -s \
    -H "$AUTH_HEADER" \
    -H "$API_HEADER" \
    -H "$ACCEPT" \
    "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/releases?per_page=3")

echo "**Response (first 3 releases, key fields):**"
echo ""
echo "\`\`\`json"
echo "$RELEASES" | python3 -c "
import sys, json
data = json.load(sys.stdin)
if isinstance(data, list):
    for r in data[:3]:
        print(json.dumps({
            'tag_name': r.get('tag_name'),
            'name': r.get('name', '')[:80],
            'published_at': r.get('published_at'),
            'prerelease': r.get('prerelease'),
            'draft': r.get('draft'),
            'assets_count': len(r.get('assets', [])),
            'body_preview': (r.get('body') or '')[:200] + '...' if r.get('body') and len(r.get('body',''))>200 else r.get('body',''),
            'html_url': r.get('html_url')
        }, indent=2))
        print('---')
else:
    print(json.dumps(data, indent=2))
" 2>/dev/null || echo "$RELEASES"
echo "\`\`\`"
echo ""

# --- Summary ---
echo "## Summary"
echo ""
echo "| Endpoint | Status | Notes |"
echo "|----------|--------|-------|"

# Check each response
echo "$TOPICS" | python3 -c "import sys,json; d=json.load(sys.stdin); print('| GET topics | OK |', len(d.get('names',[])), 'topics |') if 'names' in d else print('| GET topics | ERROR |', d.get('message','') ,'|')" 2>/dev/null
echo "$COMMITS" | python3 -c "import sys,json; d=json.load(sys.stdin); print('| GET commits | OK |', len(d), 'commits returned |') if isinstance(d,list) else print('| GET commits | ERROR |', d.get('message',''), '|')" 2>/dev/null
if [ -n "$BASE_SHA" ]; then
    echo "$COMPARE" | python3 -c "import sys,json; d=json.load(sys.stdin); print('| GET compare | OK |', d.get('total_commits',0), 'commits,', len(d.get('files',[])), 'files |') if 'total_commits' in d else print('| GET compare | ERROR |', d.get('message',''), '|')" 2>/dev/null
fi
echo "$RELEASES" | python3 -c "import sys,json; d=json.load(sys.stdin); print('| GET releases | OK |', len(d), 'releases returned |') if isinstance(d,list) else print('| GET releases | ERROR |', d.get('message',''), '|')" 2>/dev/null
