# GitHub Tools

FastMCP server providing GitHub search and repository exploration tools.

## search_repos.py

**Purpose:** Search GitHub repositories using the Search API.
**Input:** query string with optional qualifiers, sort_by parameter
**Output:** Human-readable formatted text listing 20 repositories with metadata for direct tree/file access

### search_repos_workflow()
Main orchestrator that coordinates repository search. Calls fetch_repositories to get raw API data, then format_repo_results to extract relevant fields. Returns formatted text string with repository listings.

### fetch_repositories()
Performs HTTP GET request to GitHub Search Repositories API. Constructs URL with query parameters for search term, sort order, and pagination. Sets appropriate headers for API version. Returns raw JSON response.

### format_repo_results()
Transforms raw API response into human-readable text output. Extracts owner, repo name, full_name, description, stars, forks, language, updated_at, and html_url from each repository. Returns formatted text string listing repositories with descriptions, language, stats, and URLs.

## search_code.py

**Purpose:** Search code across GitHub using the Code Search API with text match metadata.
**Input:** query string with search terms and qualifiers
**Output:** Human-readable formatted text listing 20 code matches with repository info and code fragments

### search_code_workflow()
Main orchestrator that coordinates code search. Calls fetch_code_search with text-match header to get highlighted results, then format_code_results to structure the output. Returns formatted text string with code matches and snippets.

### fetch_code_search()
Performs HTTP GET request to GitHub Search Code API. Uses special Accept header to request text-match metadata which provides code fragments. Returns raw JSON response with embedded text_matches arrays.

### format_code_results()
Transforms raw API response into human-readable text output. When no results found, appends a NOTE about GitHub Code Search not indexing data file types (CSV, TSV), suggesting grep_file or grep_repo as alternatives. Extracts repository metadata (owner, repo, full_name, description, stars) and file information (path, file_name, html_url) for each match. Calls extract_text_matches to process code fragments. Returns formatted text string listing code matches with file paths and first three code fragments per match.

### extract_text_matches()
Processes text_matches array from API response. Filters for matches on content and path properties. Returns list of fragment objects showing where search terms appear in the code or file path.

## get_repo_tree.py

**Purpose:** Traverse repository structure with lazy loading to handle large repositories. Also supports file search by glob pattern.
**Input:** owner, repo name, optional path for sub-tree exploration, optional depth for tree depth limiting, optional pattern for file name search
**Output:** Human-readable formatted text showing tree structure (browse mode) or matching files (search mode)

### get_repo_tree_workflow()
Main orchestrator that coordinates tree retrieval. First fetches default branch name, then gets tree SHA for specified path. Two modes: when pattern is provided, always fetches recursive tree and filters by glob pattern using filter_by_pattern, returning matching files via format_matches. When no pattern, determines recursive mode based on depth parameter (depth=1 skips recursive API call), fetches tree and formats response with depth filtering and root-level prioritization. Returns formatted text string.

### fetch_default_branch()
Gets default branch name for repository by querying repository metadata. Returns branch name string (e.g., "main" or "master").

### get_tree_sha()
Resolves tree SHA for given path. For root path, fetches branch info to get commit tree SHA. For sub-paths, uses Contents API to get directory SHA. Raises ValueError if path is not a directory.

### fetch_tree()
Performs HTTP GET request to GitHub Git Trees API. Accepts recursive boolean parameter: when True passes recursive=true to API (returns all nested paths), when False returns only direct children of the tree SHA. Returns tree structure with items including path, type (blob/tree), size, and SHA. Response includes `truncated` boolean flag — when True, the tree exceeds GitHub API limits (~100k entries) and results are incomplete.

### format_tree_response()
Transforms raw tree into human-readable text output. Checks `truncated` flag from API response and prepends warning if tree was truncated by GitHub API. When depth > 0, filters items to only include paths with fewer than depth "/" separators. Sorts directories and files by path depth (root-level items first) to ensure shallow items are always visible within the 50-item display limit. Checks if formatted text exceeds MAX_TREE_CHARS (1000) and appends output truncation warning if needed. Two independent warnings: API truncation (incomplete data from GitHub) and output truncation (display limit exceeded). Returns formatted text string displaying directory path, directories list, and files list with sizes.

### filter_by_pattern()
Filters tree items (blobs only) using fnmatch. When pattern contains "/" matches against full path, otherwise matches against basename only. Returns up to PATTERN_RESULTS_LIMIT (50) matching items. Used by pattern search mode and by grep_repo module.

### format_matches()
Transforms matched items into human-readable text output. Accepts optional `truncated` flag — when True, prepends warning that results may be incomplete due to GitHub API tree truncation. Displays search pattern, scope, match count, and each file with path and size in bytes.

## get_file_content.py

**Purpose:** Retrieve and decode file content from GitHub repositories, with optional line range and metadata-only mode.
**Input:** owner, repo name, file path, optional metadata_only flag, optional offset/limit for line range
**Output:** Human-readable formatted text displaying file content with metadata, or metadata only when metadata_only=True

### get_file_content_workflow()
Main orchestrator that coordinates file retrieval. Accepts metadata_only (default False), offset (default 0), and limit (default 0) parameters. Checks if API response is a list (directory) or dict (file). For directories: returns format_dir_metadata when metadata_only=True, raises ValueError otherwise. For files: selects format_metadata (metadata only) or format_file_response (content with optional line range). Returns formatted text string.

### fetch_file_content()
Performs HTTP GET request to GitHub Contents API for specific file path. Returns raw JSON response: dict for files (base64-encoded content and metadata), list for directories (array of entry dicts with name, path, size, type, sha, html_url).

### format_dir_metadata()
Formats directory metadata from Contents API list response. Counts entries by type (dirs vs files). Returns formatted text with path, type, and entry counts. Used when metadata_only=True on a directory path.

### format_metadata()
Extracts only metadata fields from file API response: path, name, size, type, sha, html_url. No base64 decoding. Use for existence checks or size queries without downloading content.

### format_file_response()
Validates response type is "file" (not directory). Calls decode_content to get UTF-8 string, then applies optional offset/limit line range. Always shows total line count in metadata. When offset or limit are set, shows which lines are being returned. Raises ValueError if path is not a file. Returns formatted text string displaying file metadata (name, path, size, lines info, URL) followed by separator and content.

### decode_content()
Decodes base64 file content to UTF-8 string after removing newlines from base64 string. Returns raw content string if encoding is not base64. Shared by format_file_response and grep_file module.

## grep_repo.py

**Purpose:** Search file content across a repository by file name pattern. Combines get_repo_tree's filter_by_pattern (find files by glob) + grep_file logic (search content by regex).
**Input:** owner, repo name, regex pattern, file glob pattern, optional path scope, max_files limit
**Output:** Human-readable formatted text listing matches per file with line numbers

### grep_repo_workflow()
Main orchestrator that coordinates repo-wide content search. Reuses fetch_default_branch, get_tree_sha, fetch_tree, and filter_by_pattern from get_repo_tree module. For each matching file (up to max_files), fetches content and searches with regex using search_lines from grep_file. Includes truncation warning if tree was truncated. Returns formatted text string with per-file match results.

### grep_matching_files()
Iterates over matching file list, fetches each file via fetch_file_content + decode_content, then runs search_lines with the regex pattern. Skips directories. Returns list of result dicts with path, matches, and total_lines per file.

### format_grep_repo_results()
Transforms per-file match results into human-readable text output. Shows search parameters, file count, truncation warning if applicable, then per-file match details with line numbers. Lists files without matches at the end.

## grep_file.py

**Purpose:** Search file content by regex pattern, returning only matching lines with optional context.
**Input:** owner, repo name, file path, regex pattern, optional context_lines, optional max_matches
**Output:** Human-readable formatted text listing matching lines with line numbers

### grep_file_workflow()
Main orchestrator that coordinates file grep. Calls fetch_file_content and decode_content from get_file_content module. Splits content into lines, searches with regex, and formats results. Raises ValueError if path is a directory. Returns formatted text string with matching lines.

### search_lines()
Finds lines matching compiled regex pattern. Collects match indices, then builds result dicts with match line index and context range (start/end based on context_lines parameter). Returns up to max_matches results, each containing line numbers and text for the match and surrounding context lines.

### format_grep_response()
Transforms match results into human-readable text output. Displays file path, total line count, pattern, and match count. Each match shows line number and content, with ">" marker on the actual match line and " " on context lines. Context groups separated by "---".

## search_items.py

**Purpose:** Search GitHub issues or pull requests using the Search Issues API with type parameter.
**Input:** query string with optional qualifiers, type ("issue" or "pr"), sort_by parameter
**Output:** Human-readable formatted text listing 20 items with metadata for direct access

### search_items_workflow()
Main orchestrator that coordinates item search. Builds query with is:issue or is:pr qualifier based on type parameter, calls fetch_items to get raw API data, then format_item_results to extract relevant fields. Returns formatted text string with item listings.

### build_query()
Adds is:issue or is:pr qualifier to search query based on type parameter. Handles edge cases: replaces conflicting qualifiers, preserves explicit qualifiers. Returns modified query string.

### fetch_items()
Performs HTTP GET request to GitHub Search Issues API. Constructs URL with query parameters for search term, sort order, and pagination. Returns raw JSON response.

### format_item_results()
Transforms raw API response into human-readable text output. Extracts repository info, item number, title, state, author, comments count, labels, and URL. For PRs: detects MERGED state via pull_request.merged_at field. Appends type-specific tool hints (get_issue or get_pr) for direct access.

## get_issue.py

**Purpose:** Retrieve full issue details including body content.
**Input:** owner, repo name, issue_number
**Output:** Human-readable formatted text displaying issue with title, metadata, and full body

### get_issue_workflow()
Main orchestrator that coordinates single issue retrieval. Calls fetch_issue to get raw API data, then format_issue to structure the output. Returns formatted text string with complete issue details.

### fetch_issue()
Performs HTTP GET request to GitHub Issues API for specific issue number. Returns raw JSON response containing full issue data including body.

### format_issue()
Transforms raw API response into human-readable text output. Displays title, state, author, dates, labels, comments count, and URL. Includes hint for get_issue_comments if comments exist. Appends full issue body after separator.

## get_issue_comments.py

**Purpose:** Retrieve all comments on a GitHub issue.
**Input:** owner, repo name, issue_number
**Output:** Human-readable formatted text listing all comments with author and content

### get_issue_comments_workflow()
Main orchestrator that coordinates comments retrieval. Calls fetch_comments to get raw API data, then format_comments to structure the output. Returns formatted text string with all comments.

### fetch_comments()
Performs HTTP GET request to GitHub Issue Comments API. Returns array of comment objects with user, body, and created_at fields.

### format_comments()
Transforms raw API response into human-readable text output. Lists total comment count, then each comment with author, date, and full body. Returns formatted text string displaying discussion thread.

## list_repo_prs.py

**Purpose:** List pull requests in a specific repository using the Pulls API.
**Input:** owner, repo name, state filter, sort_by parameter
**Output:** Human-readable formatted text listing PRs in the repository with branch info

### list_repo_prs_workflow()
Main orchestrator that coordinates repository PR listing. Calls fetch_repo_prs to get raw API data, then format_pr_list to structure the output. Returns formatted text string with PR list.

### fetch_repo_prs()
Performs HTTP GET request to GitHub Pulls API for repository. Applies state and sort filters. Returns array of PR objects.

### format_pr_list()
Transforms raw API response into human-readable text output. Displays PR number, title, state, author, source and target branches, creation date, labels, and URL. Includes tool hints for get_pr access.

## get_pr.py

**Purpose:** Retrieve full pull request details including body content and statistics.
**Input:** owner, repo name, pull_number
**Output:** Human-readable formatted text displaying PR with title, metadata, stats, and full body

### get_pr_workflow()
Main orchestrator that coordinates single PR retrieval. Calls fetch_pr to get raw API data, then format_pr to structure the output. Returns formatted text string with complete PR details.

### fetch_pr()
Performs HTTP GET request to GitHub Pulls API for specific PR number. Returns raw JSON response containing full PR data including body, commits, additions, deletions.

### format_pr()
Transforms raw API response into human-readable text output. Displays title, state (including MERGED detection), author, branches, dates, merge info, labels, commit count, additions, deletions, changed files count, and mergeable status. Includes hint for get_pr_files. Appends full PR body after separator.

## get_pr_files.py

**Purpose:** Retrieve list of files changed in a pull request.
**Input:** owner, repo name, pull_number
**Output:** Human-readable formatted text listing all changed files with diff statistics

### get_pr_files_workflow()
Main orchestrator that coordinates PR files retrieval. Calls fetch_pr_files to get raw API data, then format_pr_files to structure the output. Returns formatted text string with file list.

### fetch_pr_files()
Performs HTTP GET request to GitHub Pulls Files API. Returns array of file objects with filename, status, additions, deletions, and patch.

### format_pr_files()
Transforms raw API response into human-readable text output. Calculates total additions and deletions. Lists each file with status icon, filename, change counts, and truncated patch preview. Shows renamed files with previous filename.

## list_commits.py

**Purpose:** List commits in a repository with optional filters for branch, path, and author.
**Input:** owner, repo name, optional sha (branch/SHA to start from), path (file filter), author, per_page
**Output:** Human-readable formatted text listing commits with SHA, message, author, date, and URL

### list_commits_workflow()
Main orchestrator that coordinates commit listing. Calls fetch_commits to get raw API data, then format_commits to structure the output. Returns formatted text string with commit listings.

### fetch_commits()
Performs HTTP GET request to GitHub Commits API for repository. Constructs URL with optional query parameters: sha (starting point), path (file filter), author (username/email filter), per_page (pagination). Skips empty string parameters. Returns array of commit objects.

### format_commits()
Transforms raw API response into human-readable text output. Extracts short SHA (7 chars), first line of commit message (max 80 chars), author name, date, and URL for each commit. Returns formatted text string listing commits.

## compare_commits.py

**Purpose:** Compare two branches, tags, or SHAs showing commits and file changes between them.
**Input:** owner, repo name, base ref, head ref
**Output:** Human-readable formatted text with comparison summary, commit list, and files changed with diff stats

### compare_commits_workflow()
Main orchestrator that coordinates commit comparison. Calls fetch_comparison to get raw API data, then format_comparison to structure the output. Returns formatted text string with comparison details.

### fetch_comparison()
Performs HTTP GET request to GitHub Compare API using {base}...{head} path format. Accepts branch names, tag names, or commit SHAs. Returns comparison object with status, ahead_by, behind_by, commits array, and files array.

### format_comparison()
Transforms raw API response into human-readable text output. Shows comparison summary (status, ahead/behind counts, total commits, files changed). Lists commits with short SHA and first message line (max 20 displayed). Lists files with status icon ([A]dded, [D]eleted, [M]odified, [R]enamed), filename, and addition/deletion counts (max 30 displayed). Shows renamed files with previous filename.

## list_releases.py

**Purpose:** List releases in a repository with version tags and changelogs.
**Input:** owner, repo name, per_page
**Output:** Human-readable formatted text listing releases with tag, name, date, changelog preview, and URL

### list_releases_workflow()
Main orchestrator that coordinates release listing. Calls fetch_releases to get raw API data, then format_releases to structure the output. Returns formatted text string with release listings.

### fetch_releases()
Performs HTTP GET request to GitHub Releases API for repository. Applies per_page pagination parameter. Returns array of release objects.

### format_releases()
Transforms raw API response into human-readable text output. Extracts tag_name, name, published date, prerelease flag, draft flag, assets count, and URL for each release. Includes changelog body preview truncated to 300 characters, collapsed to single line. Skips changelog line when body is empty.

## get_release.py

**Purpose:** Retrieve a single release with full release notes body. Supports latest release or specific tag.
**Input:** owner, repo name, optional tag
**Output:** Human-readable formatted text with release metadata and full Markdown body

### get_release_workflow()
Main orchestrator that coordinates single release retrieval. Calls fetch_release to get raw API data, then format_release to structure the output. Returns formatted text string with complete release details.

### fetch_release()
Performs HTTP GET request to GitHub Releases API. When tag is None, uses `/releases/latest` endpoint (most recent non-prerelease, non-draft release). When tag is provided, uses `/releases/tags/{tag}` endpoint. Returns raw JSON response containing full release data including body.

### format_release()
Transforms raw API response into human-readable text output. Displays tag, name, published date, prerelease status, and URL. Includes full release notes body as Markdown (no truncation). Lists assets with file size and download count when present.

## graphql_client.py

**Purpose:** Shared GraphQL client infrastructure for GitHub GraphQL API.
**Input:** GraphQL query string and variables dict
**Output:** Parsed JSON response data

### graphql_query()
Performs HTTP POST request to GitHub GraphQL API. Constructs Authorization header with Bearer token. Sends query and variables as JSON body. Raises exception on HTTP errors or GraphQL errors. Returns data field from response.

## get_repo.py

**Purpose:** Retrieve repository metadata including topics and license.
**Input:** owner, repo name
**Output:** Human-readable formatted text with repository details

### get_repo_workflow()
Main orchestrator that coordinates repository metadata retrieval. Calls fetch_repo to get raw API data, then format_repo to structure the output. Returns formatted text string with repository details.

### fetch_repo()
Performs HTTP GET request to GitHub Repos API for specific repository. Returns raw JSON response containing full repository metadata.

### format_repo()
Transforms raw API response into human-readable text output. Extracts full_name, stars, description, language, topics array, license name, updated date, open issues count, default branch, and URL. Returns formatted text string with repository overview.

## search_discussions.py

**Purpose:** Search GitHub Discussions across all repositories using GraphQL Search API.
**Input:** query string, first (limit)
**Output:** Human-readable formatted text listing discussions with metadata

### search_discussions_workflow()
Main orchestrator that coordinates discussion search. Calls fetch_discussions to query GraphQL API, then format_results to structure the output. Returns formatted text string with discussion listings.

### fetch_discussions()
Performs GraphQL query to GitHub Search API with type: DISCUSSION. Requests number, title, repository, author, category, comments count, upvotes, answered status, and URL. Returns raw GraphQL response data.

### format_results()
Transforms raw GraphQL response into human-readable text output. Lists total count and each discussion with title, category emoji, repository, author, comment count, upvotes, answered status, and URL.

## list_discussions.py

**Purpose:** List discussions in a specific repository using GraphQL Repository API.
**Input:** owner, repo name, first (limit), optional category slug, optional answered filter
**Output:** Human-readable formatted text listing discussions sorted by update date

### list_discussions_workflow()
Main orchestrator that coordinates repository discussion listing. Optionally calls lookup_category_id if category filter provided, then fetch_discussions for the list, then format_results to structure output. Returns formatted text string with discussion list.

### lookup_category_id()
Performs GraphQL query to get discussionCategories for repository. Matches provided slug against category slugs. Returns category ID string or None if not found.

### fetch_discussions()
Performs GraphQL query to repository discussions with orderBy UPDATED_AT DESC. Applies optional categoryId and answered filters. Returns raw GraphQL response data.

### format_results()
Transforms raw GraphQL response into human-readable text output. Lists each discussion with title, category, author, comments, upvotes, answered status, update date, and number.

## get_discussion.py

**Purpose:** Retrieve full discussion with comments using GraphQL Repository API.
**Input:** owner, repo name, discussion number, comment_limit, comment_sort
**Output:** Human-readable formatted text with discussion body, accepted answer, and top comments

### get_discussion_workflow()
Main orchestrator that coordinates single discussion retrieval. Calls fetch_discussion to get GraphQL data, then format_discussion to structure output with comment sorting. Returns formatted text string with complete discussion.

### fetch_discussion()
Performs GraphQL query for specific discussion number. Requests title, body, author, category, upvotes, dates, answered status, answer details, and comments with replies. Returns raw GraphQL response data.

### sort_comments()
Sorts comments array by upvoteCount descending if sort_by is "upvotes". Returns original order for "chronological". Applies limit after sorting.

### format_discussion()
Transforms raw GraphQL response into human-readable text output. Displays title, category, author, creation date, upvotes, and status. Shows body content, accepted answer section if present, and comments with nested replies. Marks accepted answer comments with [ANSWER] tag.
