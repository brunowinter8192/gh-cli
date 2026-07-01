# Token Resolution: zshrc-Canonical Pattern

## Problem

`gh-cli` calls inside a Claude Code session returned `401 Unauthorized` after rotating `GH_TOKEN` in `~/.zshrc` and starting a fresh CC session. `cat ~/.zshrc | grep GH_TOKEN` showed the new token clearly; the API call used a stale one.

Manifestation:
```
$ gh-cli get_repo_tree garrettj403 SciencePlots --depth 2
requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: ...
```

## Investigation

### Code Analysis

Claude Code does not source `~/.zshrc` per Bash call. At startup it captures a one-time shell snapshot at `~/.claude/shell-snapshots/snapshot-zsh-<id>.sh`; every Bash invocation sources that frozen snapshot:

```
/bin/zsh -c source /Users/.../snapshot-zsh-1779924332722-uml6ew.sh ... && eval '<command>'
```

`GH_TOKEN` in the snapshot is frozen at the moment the parent terminal tab launched CC. A token rotation in `~/.zshrc` after that point is invisible to all Bash calls in the session — even if CC was "reopened", as long as the parent tab was not itself reopened.

`src/github/client.py` resolved `GITHUB_TOKEN` purely from `os.environ`, inheriting the stale snapshot value.

### Verification

```
$ echo "${GH_TOKEN:0:4}...${GH_TOKEN: -4}"   # stale CC snapshot env
ghp_...8rOU
$ gh-cli get_repo garrettj403 SciencePlots    # uses zshrc value after fix
**garrettj403/SciencePlots** (8,909 stars)
...
```

Env shows stale token; API call succeeds — resolver reads `~/.zshrc` independent of the snapshot.

## Resolution

`_read_zshrc_token()` and `_resolve_token()` added to `client.py`. `GITHUB_TOKEN = _resolve_token()` runs at module-import time.

Resolution order:

1. `~/.zshrc` — last `export GH_TOKEN=...` line; defeats CC shell-snapshot staleness
2. `os.environ["GH_TOKEN"]` — explicit override, works in CI where zshrc is absent
3. `os.environ["GITHUB_TOKEN"]` — GitHub Actions / CI default

Regex tolerates `="..."`, `='...'`, and bare `=value` forms; skips comment lines; last definition wins (matches zsh top-to-bottom source order).

`graphql_client.py` imports `GITHUB_TOKEN` from `client.py` at module-import time and picks up the resolved value transparently.

## Trade-off

A user running `export GH_TOKEN=<test>` in a single shell to temporarily test a different token will find the `~/.zshrc` value overrides it silently. Acceptable: token rotation via zshrc is the dominant use case; the workaround is to temporarily edit zshrc, run, and revert.
