# GitHub Issues: "streaming" in anthropics/claude-code

Issues: 100 fetched / 1236 total

---

## Issues (fetched 100 of 1236 total)

### Issue #60939 — [FEATURE] Make thinking summaries streaming

State: OPEN | #60939
Labels: duplicate, enhancement, area:tui


---



### Problem Statement

It's incredibly frustrating to just wait for claude code to think for unknown time and get absolutely zero feedback on what is going on.

### Proposed Solution

I understand that you use the thinking rewriter to protect against destillation attacks, but that doesn't mean you have to completely ruin the UX just for that. 

It should be possible to let the thinking rewriter on regular interval summarize what's currently happening. Triggered either on time or number of lines or similar (so it doesn't try to summarize halfway through a sentence of thinking. I'm thinking something like this:

```
<input thinking>
some raw thinking
</input thinking>
<thinking summary>
the output of the rewriter model
</thinking summary>
<input thinking>
continued raw thinking
</input thinking>
<thinking summary>
continued output, with all above as context
</thinking summary>
```

Then you just send all the thinking summary blocks to the client whenever they're available instead of waiting for the full thinking block.

### Alternative Solutions

1. Stay frustrated at not knowing what claude is doing.
2. Reducing effort setting so I don't have to wait so long before feedback
3. Add a prompt that tells it to regularly write what is happening during long thinking sessions

### Priority

High - Significant impact on productivity

### Feature Category

CLI commands and flags

### Use Case Example

_No response_

### Additional Context

_No response_

# Comments on anthropics/claude-code#60939
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-20T18:34:54Z

Found 2 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/30660
2. https://github.com/anthropics/claude-code/issues/36006

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: anka-213
Date: 2026-05-21T00:19:16Z

This is specifically about the thinking *summaries* which are the only option for opus 4.7+, not raw thinking. though i guess #30660 is mostly the same.

---

### Issue #58248 — Add tokens-per-second (TPS) display during streaming

State: OPEN | #58248
Labels: enhancement, area:tui, stale

---

## Feature Request: Live Tokens Per Second (TPS) Display

### Problem
Users have no visibility into streaming throughput during Claude Code sessions. Knowing TPS helps evaluate model performance and response quality.

### Proposed Solution
Display real-time TPS counter in the terminal UI during streaming responses, similar to OpenCode's `@williamcr01/opencode-tps` plugin.

### Requirements
- Live TPS counter during streaming
- 5-second rolling window calculation
- Show "-" when idle/no tokens
- Non-intrusive placement (e.g., bottom-right corner)

### Reference Implementation
OpenCode plugin `@williamcr01/opencode-tps` hooks into internal streaming events to calculate real-time TPS:
- Tracks token deltas via `message.part.delta` events
- Uses rolling window for smoothing
- Registers UI slot for display

### Why This Helps
- Performance visibility during long responses
- Model comparison benchmarking
- Detecting rate limiting or throttling

# Comments on anthropics/claude-code#58248
Total: 0 comments

No comments on this issue.

---

### Issue #53280 — Bring back token-by-token streaming (line-by-line streaming since v2.1.78 feels worse)

State: OPEN | #53280
Labels: duplicate, platform:macos, area:tui, stale


---

### Description

Since v2.1.78 introduced line-by-line streaming, the visual experience of receiving text from Claude feels noticeably less smooth than the previous token-by-token streaming.

### Before (≤ v2.1.77)
Text streamed token-by-token, similar to claude.ai in the browser. Words appeared fluidly as they were generated, giving a "live writing" feel. Smooth and pleasant to follow.

### After (v2.1.78+)
Text streams line-by-line. Whole lines appear at once, then a pause, then the next whole line at once. Within a line there is no progressive build-up — it pops into existence. This feels chunky/staccato and is harder to follow.

### Why this matters
- Reading along while Claude generates is harder when output appears in bursts.
- Token-streaming made it easier to start parsing the response as it arrives.
- The previous behavior was a quality-of-experience signature of Claude Code that matched the API's actual streaming granularity.

### Request
Please add an opt-in setting / env var to revert to token-streaming, e.g.:
- `streamingMode: "token"` in `settings.json`, or
- `CLAUDE_CODE_STREAMING_MODE=token`

Defaults can stay as-is (line-streaming) — just give power users the choice.

### Environment
- Claude Code v2.1.119
- macOS (Apple Silicon), Ghostty terminal
- Default TUI renderer

### Related
This is **not** the same as #37569 (which requests disabling streaming entirely). This issue requests reverting the *granularity* of streaming, not turning it off.

# Comments on anthropics/claude-code#53280
Total: 1 comments

--- Comment 1 ---
Author: SemihBlc
Date: 2026-04-25T16:44:40Z

Hi — this issue was auto-labeled `duplicate`, but I want to clarify it's **not** a duplicate of #37569.

### The difference

- **#37569** requests turning streaming **off entirely** — buffer the full response, display once when done.
- **This issue (#53280)** requests keeping streaming on, but reverting its **granularity** from line-by-line (since v2.1.78) back to token-by-token (pre-v2.1.78).

Concretely:
- #37569 asker: "I don't want streaming at all"
- This asker (me): "I want streaming — but the smoother token-by-token kind, not the chunky line-by-line kind"

Different feature requests, different implementations. Could the `duplicate` label be removed, please?

---

### Issue #54472 — [Bug] Anthropic API timeout during streaming operations

State: OPEN | #54472
Labels: bug, duplicate, platform:linux, api:anthropic, stale

---

**Bug Description**
three time api / streamidle  timeout

**Environment Info**
- Platform: linux
- Terminal: gnome-terminal
- Version: 2.1.121
- Feedback ID: 71ab3e2f-d8ce-4c67-8891-4f5f66e431da

**Errors**
```json
[{"error":"Error: Stream idle timeout - partial response received\n    at GM4 (/$bunfs/root/src/entrypoints/cli.js:8915:13615)\n    at processTicksAndRejections (native:7:39)","timestamp":"2026-04-28T21:48:04.113Z"},{"error":"Error: Stream idle timeout - partial response received\n    at GM4 (/$bunfs/root/src/entrypoints/cli.js:8915:13615)\n    at processTicksAndRejections (native:7:39)","timestamp":"2026-04-28T22:03:44.836Z"}]
```

# Comments on anthropics/claude-code#54472
Total: 0 comments

No comments on this issue.

---

### Issue #58767 — [BUG] VSCode extension: auto-scroll during streaming prevents scrolling up

State: OPEN | #58767
Labels: bug, platform:macos, area:ide, platform:vscode, stale


---



### What's Wrong?

While Claude is streaming a response, the chat panel auto-scrolls to the bottom every time a new line/token is appended. Any attempt to scroll up with a trackpad is immediately overridden — within a frame the view snaps back to the bottom. This makes it impossible to re-read earlier content (or copy from it) until the stream finishes.

Root cause appears to be in `webview/index.js` (v2.1.140). The "is user at bottom?" check uses a 50px threshold:

    let v5 = scrollHeight - scrollTop - clientHeight;
    A.current = v5 < 50;

A single trackpad scroll tick on macOS produces a delta of ~10–40px, which keeps `v5 < 50` true, so the next streamed chunk re-triggers `Bk(Q)` and snaps to the bottom. The user can never get out of the "near bottom" window with normal trackpad use.

Patching the threshold locally to `< 2` fully resolves the issue: scrolling up during streaming now works as expected, and stick-to-bottom re-engages once the user manually scrolls back to the bottom.


### What Should Happen?

Stick-to-bottom should follow the standard contract:
- If the user is exactly at the bottom, snap to the bottom on new content.
- As soon as the user scrolls up by any amount, suspend auto-scroll until they manually return to the bottom.

Suggested fix: reduce the threshold from 50 to ~2 pixels, or check `scrollHeight - scrollTop - clientHeight <= 1`. Most stick-to-bottom libraries (e.g. `use-stick-to-bottom`) default to a near-zero threshold for exactly this reason.


### Error Messages/Logs

```shell

```

### Steps to Reproduce

1. Install Claude Code VSCode extension v2.1.140 (anthropic.claude-code).
2. Open the Claude Code panel in VSCode.
3. Send any prompt that produces a long streaming response.
4. While the response is still streaming, try to scroll up with the trackpad to re-read earlier content.

Expected: the view stays where the user scrolled.
Actual: the view immediately snaps back to the bottom on the next streamed chunk.

Environment:
- VSCode extension: anthropic.claude-code v2.1.140 (also reproduces on 2.1.139)
- VSCode: 1.119.0
8b640eef5a6c6089c029249d48efa5c99adf7d51
arm64
- OS: macOS 15 (Darwin 25.0.0)
- Hardware: MacBook Pro 14" M4 (built-in Liquid Retina XDR, default scaled resolution)
- Input: built-in trackpad (smooth scroll)

Note: I initially suspected a HiDPI/scaling issue, but after inspecting the bundled webview code the root cause is the 50px threshold combined with macOS smooth-scroll deltas — it's not display-specific.


### Claude Model

Opus

### Is this a regression?

I don't know

### Last Working Version

_No response_

### Claude Code Version

-

### Platform

AWS Bedrock

### Operating System

macOS

### Terminal/Shell

Other

### Additional Information

_No response_

# Comments on anthropics/claude-code#58767
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-13T17:30:10Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/11578
2. https://github.com/anthropics/claude-code/issues/53382
3. https://github.com/anthropics/claude-code/issues/54149

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: maksimkrylov
Date: 2026-05-13T17:41:15Z

the same [issue](https://github.com/anthropics/claude-code/issues/11578)  but I'm experiencing it in VS Code extension @2.1.140

---

### Issue #63326 — [DOCS] Fine-grained tool streaming docs still describe provider opt-in behavior

State: OPEN | #63326
Labels: bug, documentation, area:docs

---

### Documentation Type

Incorrect/outdated documentation

### Documentation Location


https://code.claude.com/docs/en/env-vars

### Section/Topic


`CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING` in the environment variables reference

### Current Documentation


The environment variables reference currently says:

> `CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING` | Controls whether tool call inputs stream from the API as Claude generates them.

The same entry describes provider-specific enablement:

> Enabled by default on the Anthropic API. On Bedrock and Vertex, enabled per model where the deployed container supports it. Set to `0` to opt out. Set to `1` to force on when routing through a proxy via `ANTHROPIC_BASE_URL`, `ANTHROPIC_VERTEX_BASE_URL`, or `ANTHROPIC_BEDROCK_BASE_URL`. Off by default on Foundry and gateway connections

The page also says telemetry opt-out disables feature-flag fetching:

> `DISABLE_TELEMETRY` | Set to `1` to opt out of telemetry. Telemetry events do not include user data like code, file paths, or bash commands. Also disables feature-flag fetching with the same effect as `DISABLE_GROWTHBOOK`, so some flagged features may be unavailable

### What's Wrong or Missing?


Claude Code v2.1.154 says streaming tool execution is now always enabled, including when telemetry is disabled and on Bedrock, Vertex, and Foundry. The current env var entry still describes the older feature-flag/provider rollout model.

That leaves three outdated implications:

### A. Bedrock and Vertex still sound conditional

The docs say fine-grained tool streaming is enabled only "per model where the deployed container supports it," but the v2.1.154 release note says streaming tool execution is now always enabled on Bedrock and Vertex.

### B. Foundry still sounds disabled by default

The docs explicitly say the feature is off by default on Foundry, which contradicts the v2.1.154 release note.

### C. Telemetry-disabled behavior is not clarified

The docs say `DISABLE_TELEMETRY` disables feature-flag fetching and can make flagged features unavailable. Since v2.1.154 removed the feature-flag dependency for streaming tool execution, users need to know that disabling telemetry no longer disables this behavior.

### Suggested Improvement


Update the `CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING` entry to describe the current default.

Suggested replacement:

> Tool call inputs stream from the API as Claude generates them. This is enabled by default across Anthropic API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry connections, including when telemetry or feature-flag fetching is disabled. Set `CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING=0` to opt out if your proxy or gateway cannot handle streamed tool input fields.

If `CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING=1` is still useful for a specific gateway compatibility path, document that as an override for gateway/proxy setups rather than as the way to force-enable Bedrock, Vertex, or Foundry.

### Impact

Medium - Makes feature difficult to understand

### Additional Context


**Affected Pages:**

| Page | Line(s) | Context |
|------|---------|---------|
| https://code.claude.com/docs/en/env-vars | 180 | `CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING` still describes Anthropic-only default enablement, conditional Bedrock/Vertex enablement, and Foundry/gateway default-off behavior |
| https://code.claude.com/docs/en/env-vars | 291 | `DISABLE_TELEMETRY` says feature-flag fetching is disabled and flagged features may be unavailable, but streaming tool execution is no longer behind that flag as of v2.1.154 |

**Total scope:** 1 page affected

**Version context:** Claude Code v2.1.154 changelog entry: "Streaming tool execution is now always enabled, including when telemetry is disabled or on Bedrock/Vertex/Foundry (previously behind a feature flag)."

# Comments on anthropics/claude-code#63326
Total: 0 comments

No comments on this issue.

---

### Issue #55543 — [BUG] Streaming long responses (large plans/markdown) causes Warp terminal to hard-crash on Windows — consider non-streaming or batched flush mode

State: OPEN | #55543
Labels: enhancement, platform:windows, area:tui, external, stale

---

## Summary
Long streamed responses from Claude Code (e.g. multi-KB plans / markdown)
reliably hard-crash the Warp terminal on Windows. Investigation of Warp logs
shows Warp emits one INFO event per terminal character, the log floods, and
the process is killed with no panic or minidump.

The root cause sits in Warp's renderer/log path, and I've filed it there as
[warpdotdev/warp#9899](https://github.com/warpdotdev/warp/issues/9899).
Filing here too because **Claude Code's character-by-character streaming is
the trigger**, and a coarser flush mode or a `--no-stream` interactive
option would let users on affected host-terminals keep working while Warp
fixes the underlying issue.

## Environment
- Claude Code: latest as of 2026-05-02
- Host terminal: Warp `v0.2026.04.27.15.32.stable_03` on Windows 11
- Reproduces consistently on long-output turns

## Reproduction
Issue a prompt that asks Claude Code to produce a long response in the
terminal (e.g. "generate a multi-phase implementation plan, intermediate
review, then re-plan remaining phases"). Within seconds of the stream
starting, Warp dies. Three crashes in ~50 minutes on this workload.

The exact prompt I used (verbatim — nothing sensitive in it):
> *You were interrupted mid operation. Please check the progress you made
> so far. I want you to resume. I want you to also make the plan to plan
> in all phases that were still pending, intermediate critical review of
> the state of the phase you just finished, and even in the face itself
> if it's a big face and complex. Plan so accordingly. but write the
> plan to MD, because there is currently a bug with the warp cli we are
> using that makes it crash.*

Adding the "write the plan to MD" instruction at the end was itself a
workaround attempt — but the **first response token** Claude Code prints
(acknowledging the request, listing files it will read, etc.) is already
enough to crash Warp on subsequent turns when output is long.

## Suggestions
1. **`output: file`** — let me ask the agent to write its main response to
   a file and only print a one-line summary to the terminal. (Possible
   today via prompting, but turning it on globally would be safer.)
2. **Batched flush mode** — add an env var or setting that buffers output
   and flushes once per N ms / N tokens / on newline, rather than per
   character. Would dramatically reduce the per-character event load on
   any host terminal, not just Warp.
3. **Detect known-bad host terminals** — when `$TERM_PROGRAM == WarpTerminal`
   on Windows, default to a coarser flush until upstream fixes
   warpdotdev/warp#8409 / warpdotdev/warp#9899.

## Related
- [warpdotdev/warp#8409](https://github.com/warpdotdev/warp/issues/8409) —
  Warp hangs at >100% CPU when Claude Code runs (same workload, hang
  variant).
- [warpdotdev/warp#9899](https://github.com/warpdotdev/warp/issues/9899) —
  My new report of the Windows hard-crash variant.

## Workaround
Asking the agent to write long output to a markdown file (as in the prompt
above) reliably avoids the crash.

# Comments on anthropics/claude-code#55543
Total: 0 comments

No comments on this issue.

---

### Issue #60564 — Feature request: AssistantMessageDelta hook for streaming-aware tooling (TTS, telemetry, mirror)

State: OPEN | #60564
Labels: enhancement, area:hooks

---

## Motivation

The current hook surface fires only at boundary events: `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`, etc. There is no way to react to assistant text *while* it is being generated.

For an entire class of downstream tooling — local TTS, transcript mirroring, on-the-fly translation, accessibility narrators, telemetry — that boundary-only model means the user has to wait for the full response to finish before any side-effect can begin. On a 500-word response that is a 15–30s wait before any narration starts.

I just shipped a local Kokoro-TTS daemon ([Null-Phnix/claude-voice#3](https://github.com/Null-Phnix/claude-voice/pull/3)) that drops warm time-to-first-audio from ~6s to ~0.6s. The bottleneck is no longer the model; it is that the `Stop` hook only fires *after* the assistant turn completes.

I verified by polling the JSONL transcript file every 100ms during an assistant response: the file grew exactly once, with the entire 7.2KB assistant message written in a single flush at end-of-turn. So tailing the transcript can't substitute either.

## Proposed hook

A new hook event fired periodically during assistant generation with the in-progress text:

```jsonc
{
  "event": "AssistantMessageDelta",
  "session_id": "...",
  "message_id": "...",
  "delta": {
    "text": "...the text added since the last delta..."
  },
  "cumulative_text": "...full assistant text so far..."  // optional but very useful
}
```

Configuration would be the same as other hooks in `~/.claude/settings.json`:

```json
"hooks": {
  "AssistantMessageDelta": [
    { "matcher": "", "hooks": [{ "type": "command", "command": "...", "async": true, "timeout": 5 }] }
  ]
}
```

## Implementation notes / requests

A few things would make this hook actually usable for streaming consumers:

1. **`async: true` should be the only sensible mode.** A sync hook on every delta would tank generation throughput. Document it clearly.
2. **Debounce/batch.** Firing per-token is overkill. Firing every ~100ms or on every sentence-terminator (`.!?` followed by whitespace) would cover almost every consumer's needs without flooding hook processes.
3. **Either `delta` or `cumulative_text`, not both required.** Consumers can derive one from the other. Sending only `delta` is fine if you flag the order; sending `cumulative_text` is fine if you accept the redundancy.
4. **Final delta marker.** A flag like `"is_final": true` on the last delta of a turn (or a separate `AssistantMessageEnd` event) helps consumers flush their last sentence cleanly.

## Use cases this unlocks

- **Real-time TTS** — start speaking sentence 1 while Claude is still generating sentence 2. The reason I filed this.
- **Accessibility** — screen readers that narrate as the assistant types, the way visually-impaired users already use screen readers with chat apps.
- **Live transcript mirror** — push the response to a second device / dashboard as it's being typed, instead of post-hoc.
- **Per-sentence translation** — pipe deltas to a translator and emit in the user's language as fast as the assistant emits in English.
- **Content moderation / safety filters** — abort or rewrite a response mid-stream when an external rule fires, instead of after the user has already seen it.
- **Token-level telemetry** for tools that need finer-grained data than `Stop` provides.

## Workarounds considered (and why they don't suffice)

- **Tail the JSONL transcript** — file is flushed once at end-of-turn (verified empirically). No streaming visibility.
- **Wrap Claude Code's stdout via PTY** — fragile, breaks every time the TUI redraws or cursor-moves, and forces users to launch via a wrapper.
- **`PostToolUse`** — fires only on tool use, not on plain-text assistant turns.
- **Polling the API directly via a custom client** — duplicates Claude Code's session, auth, MCP plumbing.

A first-class hook avoids all of those failure modes.

## Happy to help

If a delta hook is on the roadmap, I'd be happy to:
- Test against any preview build and give feedback before stable.
- Update [Null-Phnix/claude-voice](https://github.com/Null-Phnix/claude-voice) as a reference consumer the moment it ships.
- Write user-facing docs once the contract is settled.

Thanks for building Claude Code.

# Comments on anthropics/claude-code#60564
Total: 0 comments

No comments on this issue.

---

### Issue #60946 — [DOCS] `Build a streaming UI` miss the the check for in_tool

State: OPEN | #60946
Labels: documentation, enhancement, area:agent-sdk, area:docs

---

### Documentation Type

Missing documentation (feature not documented)

### Documentation Location

https://code.claude.com/docs/en/agent-sdk/streaming-output#build-a-streaming-ui

### Section/Topic

build-a-streaming-ui

### Current Documentation

The docs current show:
```python
elif event_type == "content_block_delta":
      delta = event.get("delta", {})
      # Only stream text when not executing a tool
      if delta.get("type") == "text_delta" and not in_tool:
          sys.stdout.write(delta.get("text", ""))
          sys.stdout.flush()
```

### What's Wrong or Missing?

The code miss the `in_tool` case process.


### Suggested Improvement

```python
elif event_type == "content_block_delta":
      delta = event.get("delta", {})
      delta_type = delta.get("type")

      if delta_type == "text_delta" and not in_tool:
          # Streaming text from Claude's response
          sys.stdout.write(delta.get("text", ""))
          sys.stdout.flush()

      elif delta_type == "input_json_delta" and in_tool:
          # ✅ Accumulate tool input JSON as it streams in
          tool_input += delta.get("partial_json", "")
elif event_type == "content_block_stop":
    if in_tool:
        # Tool call finished — tool_input now has the complete JSON
        print(f" done (input: {tool_input})", flush=True)
        in_tool = False
        tool_input = ""
```

### Impact

Medium - Makes feature difficult to understand

### Additional Context

_No response_

# Comments on anthropics/claude-code#60946
Total: 0 comments

No comments on this issue.

---

### Issue #41954 — TUI selection spams clipboard on every render during streaming

State: OPEN | #41954


---

## Description

Claude Code's TUI writes selected text to the system clipboard on every re-render during streaming, flooding clipboard managers (e.g. CopyClip, Maccy, Paste) with hundreds of partial text fragments.

## Reproduction

1. Open Claude Code CLI in a terminal (tested in Warp on macOS)
2. Have a clipboard history manager running (e.g. CopyClip)
3. Select some text in the Claude Code TUI (mouse click-drag)
4. Ask Claude something that produces a streaming text response
5. Check clipboard history — it will contain dozens/hundreds of entries with partial text fragments, space-padded to terminal width

## Root cause (from binary analysis)

The clipboard write function (`BM` in the minified bundle) fires during TUI re-renders when a text selection is active. Each streaming chunk triggers a re-render, which re-syncs the selection to clipboard.

Additionally, the function writes to clipboard via **two mechanisms simultaneously**:
- OSC 52 escape sequence (terminal clipboard protocol)
- `pbcopy` subprocess (macOS) / `xclip`/`xsel` (Linux)

This means each re-render may produce 2 clipboard writes.

## Evidence

Pasteboard monitoring with a Swift script showed:
- **Zero** clipboard writes at idle (no Claude streaming)
- **Zero** clipboard writes during tool calls (no visible text output)  
- **5+ writes per 20 seconds** during text streaming, containing fragments of the streamed response
- **Zero** clipboard writes during non-Claude terminal output in the same terminal (Warp)

The macOS pasteboard change count reached 4996+ during a single session.

## Expected behavior

- Clipboard should only be written on **explicit user action**: `/copy` command, Cmd+C, or equivalent
- TUI re-renders should **not** re-sync selection to clipboard
- If selection-to-clipboard is intentional, it should be **debounced** during streaming (e.g. only write on selection end, not on every frame)
- Consider not using both OSC 52 and pbcopy simultaneously (double-writes)

## Environment

- Claude Code CLI (Bun binary, installed via `~/.local/bin/claude`)
- macOS (Darwin 25.3.0, arm64)
- Terminal: Warp
- Clipboard manager: CopyClip

🤖 Generated with [Claude Code](https://claude.com/claude-code)

# Comments on anthropics/claude-code#41954
Total: 3 comments

--- Comment 1 ---
Author: ThatDragonOverThere
Date: 2026-04-05T21:13:45Z

Confirmed on v2.1.92 (Windows 11, Windows Terminal). The OSC 52 clipboard operation is leaking visibly into terminal output as: 'sent 2269 chars via OSC 52 · check terminal clipboard settings if paste fails'. Appears inline in the conversation output during streaming. Not a background event — it's printing to the visible terminal mid-response.

--- Comment 2 ---
Author: MAlshehri
Date: 2026-04-23T12:33:08Z

hitting a variant of this. cmd+c on text in claude code leaves the clipboard completely empty — zero bytes, not garbled. cmd+v in other apps does nothing. reproduces on iterm2 and wezterm, so it's not a terminal thing.

right after cmd+c:

$ pbpaste | wc -c
0
$ osascript -e 'clipboard info'
«class utf8», 0, «class ut16», 2, string, 0, Unicode text, 0

all text flavors registered, all empty (the 2 bytes on utf16 is just a BOM).

feels like the same BM re-render sync described above, but firing right after the selection clears — OSC 52 + pbcopy both emit empty and wipe the bytes the terminal just wrote. copy into claude code from other apps still works fine; only copy out is broken.

workaround: alt+drag (block select) then cmd+c works (supported in maccy with paste without formatting option selected).

env: claude code 2.1.118, macOS 26.4.1, wezterm 20240203 (also repros on iterm2).

--- Comment 3 ---
Author: udisun
Date: 2026-05-22T16:13:28Z

**Confirming this issue is still active as of May 2026.**

- **Claude Code**: 2.1.148
- **macOS**: 26.5 (Build 25F5042g)
- **Hardware**: MacBook Pro (Mac16,7), Apple M4 Pro, 48GB, arm64

The macOS TCC dialog `"2.1.148" would like to access data from other apps` spams on every streaming response. Clicking Allow does not persist — a new dialog immediately appears from a different `--bg-spare` daemon instance. The permission dialog shows the version number as the app name (e.g. `"2.1.148"`) rather than "Claude" because the binary is a bare Mach-O at `~/.local/share/claude/versions/2.1.148` without an app bundle/Info.plist.

The multi-instance spawning of `--bg-spare` daemons compounds the issue — each pre-warmed spare process independently triggers the TCC prompt, making it impossible to resolve with a single Allow click.

---

### Issue #58780 — [BUG] VSCode extension: copy button on completed code blocks flickers during streaming

State: OPEN | #58780
Labels: bug, has repro, platform:macos, area:ide, platform:vscode, stale

---



### What's Wrong?

While Claude is streaming a response, the "copy" icon in the top-right corner of every *completed* code block flickers (rapidly fades in/out) at the same rate as new tokens arrive. The flicker only happens when the mouse cursor is hovering over the code block — which is exactly when the user is about to click the button.

This produces visible strobing of the copy button.


### What Should Happen?

The copy button should remain stably visible while the cursor hovers over a completed code block, regardless of streaming activity in the rest of the message.

### Error Messages/Logs

```shell

```

### Steps to Reproduce

1. Install Claude Code VSCode extension v2.1.140.
2. Open the Claude Code panel.
3. Send a prompt that produces a long response containing at least one early code block, e.g.:
     "Show me a TypeScript example of a debounce function, then explain in 5 paragraphs how it works."
4. As soon as the first ``` code block is fully rendered, hover the mouse over it.
5. Keep watching the copy icon in the top-right corner of that code block while the model continues streaming the explanation below.

Expected: copy icon stays solidly visible while hovered.
Actual: copy icon flickers/strobes with the streaming token rate (~10–20 Hz).

Environment:
- Claude Code VSCode extension: v2.1.140 (anthropic.claude-code)
- VSCode: 1.119.0 8b640eef5a6c6089c029249d48efa5c99adf7d51 arm64
- macOS 15 (Darwin 25.0.0), MacBook Pro 14" M4


### Claude Model

Opus

### Is this a regression?

I don't know

### Last Working Version

_No response_

### Claude Code Version

 - 

### Platform

AWS Bedrock

### Operating System

macOS

### Terminal/Shell

Other

### Additional Information

_No response_

# Comments on anthropics/claude-code#58780
Total: 0 comments

No comments on this issue.

---

### Issue #55608 — [FEATURE] Let me keep thinking blocks expanded longer after streaming ends

State: OPEN | #55608
Labels: enhancement, area:tui, stale

---

### What I'm asking for

A setting (e.g. `thinkingDisplayDurationMs` in `settings.json`, or an env var) that controls how long an expanded extended-thinking block stays visible after streaming ends, before it collapses to the one-line `∴ Thinking (ctrl+o to expand)` indicator.

My typical use case: I'd set this to **~10 minutes** so the most recent thinking block stays readable while I review the response and the diffs it produced. `0` would let users who prefer the opposite collapse it immediately. The current behavior would remain the default if the setting is unset.

### Behavior I'm seeing

While the model is thinking, the full thinking text streams in and is fully readable. After streaming completes, the block stays expanded for a short window — in my testing about 30 seconds — and then collapses to a single dim line. From that point on the content is only reachable via `ctrl+O`.

For longer reasoning chains 30 seconds is well below the time it takes me to actually finish reading, especially when I look away to a diff or another window for a moment.

### Why I want this

- **Finish reading.** Extended thinking on harder turns is several paragraphs. By the time I've read the response and want to scroll back up to recheck the reasoning, it's already gone.
- **Glanceable context while reviewing the answer.** Keeping the last turn's thinking visible alongside the response is more useful than having to swap into transcript mode to retrieve it.
- **Catch misunderstandings.** A lot of the value of visible thinking is noticing "wait, the model misread my prompt" — but that judgment usually comes *after* I've read the response, by which point the thinking is already collapsed.

(A symmetric "set it shorter / to zero" use case probably exists too — making the duration configurable handles both ends with one knob.)

### What today's options don't cover

- **`ctrl+O` (transcript mode)**: opens a separate scrollable view, but in my experience it only un-collapses the most recent thinking block of the current turn — earlier thinking from the same session stays hidden. And switching screens just to re-read what was on screen 40 seconds ago is heavy.
- **`--verbose` / `"verbose": true`**: keeps all thinking blocks expanded permanently, but it also expands tool-result output (Bash stdout, file reads, grep results, etc.). On longer sessions that becomes a wall of text that buries the thinking I was trying to keep visible — net negative.
- **Click-to-expand on individual messages**: works for some message types (collapsed read/search groups, advisor results) but doesn't seem to apply to thinking blocks themselves.
- **`showThinkingSummaries`**: this looks like an API-level control (whether thinking summaries come back from the API at all) rather than a rendering-time control, and there are ongoing reports it doesn't reliably take effect (#48065). Either way, it doesn't change how long an already-rendered thinking block stays expanded.

So there's a real gap between "see thinking briefly" (default, ~30s) and "see everything verbose forever" (`--verbose`). Letting users dial the duration would land in the middle.

### Related, but distinct

- #30660 — real-time streaming of thinking (largely shipped). Comments there mention "thinking can get lost in the transcript stream" and "sitting blind for 30–50 seconds" — same underlying frustration, but my request is specifically about the *post-streaming* visibility window, which #30660 doesn't cover.
- #36006 — collapsed-by-default with a toggle. Today's `∴ Thinking` + `ctrl+O` is roughly that design; this request is about making the toggle's auto-trigger configurable.
- #48065 — `showThinkingSummaries` bug. Different layer (API content vs. UI duration); included so it's clear I'm not asking for a duplicate.

### Suggested shape (open to alternatives)

```jsonc
// ~/.claude/settings.json
{
  // My ask: keep last turn's thinking readable for 10 min.
  "thinkingDisplayDurationMs": 600000

  // Other reasonable values:
  //   0       collapse immediately
  //   30000   current default behavior (explicit)
  //   omitted preserve current default
}
```

Equivalently an env var like `CLAUDE_THINKING_DISPLAY_MS` would work. Naming is bikesheddable; the underlying ask is just a knob.

Thanks!

# Comments on anthropics/claude-code#55608
Total: 0 comments

No comments on this issue.

---

### Issue #35579 — Line-by-line streaming: who approved this and why?

State: OPEN | #35579
Labels: enhancement, area:tui


---

The latest version introduced line-by-line text streaming. I assume whoever designed this was inspired by watching a dot-matrix printer from 1987, because the effect is identical: text crawls onto the screen line by line, the layout constantly shifts, and reading anything mid-response is simply not possible.

I genuinely cannot fathom what user problem this was meant to solve. The previous behavior — rendering text as it arrived, without turning the output area into a slot machine — worked perfectly well. This is a step backwards in usability presented as a feature.

Please provide an option to disable it. Or, alternatively, explain the reasoning — I'm open to being wrong, but right now this looks like a change made by someone who has never had to actually read their own tool's output.

# Comments on anthropics/claude-code#35579
Total: 11 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-03-18T01:10:47Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/35343
2. https://github.com/anthropics/claude-code/issues/34080
3. https://github.com/anthropics/claude-code/issues/31325

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: redareda9
Date: 2026-03-18T03:22:53Z

It's pretty awful. Looking to downgrade but not even possible since using claude install native installer... 
@bcherny please look at this

--- Comment 3 ---
Author: gentoosys
Date: 2026-03-18T07:17:26Z

+1, very awful. can't scroll and read, streaming resets scroll

--- Comment 4 ---
Author: heyuforia
Date: 2026-03-18T13:14:44Z

2.1.78 patch notes has it noted as a feature, did they add a config toggle to turn it on/off? 
If not, we **NEED** this as a toggle if they're planning to keep this as a **_"features"_**

This is as bad as the flashing/jittering terminal behavior, I don't know who's idea this was to implement this.

Don't fix whats not broken guys...

--- Comment 5 ---
Author: gentoosys
Date: 2026-03-18T17:33:29Z

actually it was introduced somewhere after 2.1.6x version. before claude responded with one big chunk/answer and it worked fine and I was happy with it. and it was easy to scroll and read. now it stream line by line, too fast, I am scrolling up to read it, scroll resets to top, I scroll again, again reset. so streaming output is totally unusable until it is finished

--- Comment 6 ---
Author: knight-scripts
Date: 2026-03-18T19:11:34Z

The response streaming change in v2.1.78 to line-by-line is a significant UX regression. Why even do this? Who does it help?
p.s. downgrading to v2.1.77 didn't help

--- Comment 7 ---
Author: heyuforia
Date: 2026-03-18T19:52:45Z

Honestly, they need to stop with all these new features and changes and take some time ironing out the core UX.

They have data on users who use CC for 100s of hours, ask them for feedback directly.

I will happily take the survey if asked, please guys, refine the core experience.

--- Comment 8 ---
Author: timdmackey
Date: 2026-03-18T23:39:06Z

https://code.claude.com/docs/en/changelog#2-1-78
> Response text now streams line-by-line as it’s generated

Really unhappy with this change, it makes it much harder to read claude's responses with everything constantly shifting around on the screen.

--- Comment 9 ---
Author: timdmackey
Date: 2026-03-18T23:46:39Z

You have GOT to be kidding me. Apparently there's a config [fix](https://github.com/anthropics/claude-code/issues/31325#issuecomment-4009288278) for this but the config editor is broken! It's currently impossible to save any edits to the config 🤡 ([bug report](https://github.com/anthropics/claude-code/issues/35341))

--- Comment 10 ---
Author: knight-scripts
Date: 2026-03-19T09:46:15Z

> You have GOT to be kidding me. Apparently there's a config [fix](https://github.com/anthropics/claude-code/issues/31325#issuecomment-4009288278) for this but the config editor is broken! It's currently impossible to save any edits to the config 🤡 ([bug report](https://github.com/anthropics/claude-code/issues/35341))

Reduce Motion config makes things better, 100%, thanks for pointing that out, but still not the same experience we had though

--- Comment 11 ---
Author: LiuShiyuMath
Date: 2026-05-24T16:35:15Z

Your #35579 line stuck with me: "a change made by someone who has never had to actually read their own tool's output." The real complaint underneath "who approved this and why" is that something landed and no one owned the judgment.

So I'm curious: when an AI-generated change shows up in your tree, how do you decide it's safe to merge — read every line yourself, or is there a faster signal you trust? And is that line-by-line read something you actually want to do, or something you'd rather not have to?

No deck, no demo. I'm a solo founder building one thing: AI now ships ~30 changes overnight, and someone has to judge all 30 before merge — 10 min each and the day's gone. I build that reviewer a pre-made health report from last night so they decide merge-safe in minutes, no deep-dive. Does that sound useful, or like it'd get in your way?

— Shiyu (solo founder)

---

### Issue #40189 — Bedrock streaming: undefined is not an object (evaluating '_.speed')

State: OPEN | #40189
Labels: bug, has repro, api:bedrock, platform:macos, stale

---

## Bug

When using Claude Code v2.1.86 with Amazon Bedrock as the provider, the error `undefined is not an object (evaluating '_.speed')` fires repeatedly during streaming (mid-thinking/response), not just at startup. It appears on every streaming chunk.

## Environment

- **Claude Code version:** 2.1.86 (latest)
- **Provider:** Amazon Bedrock via Teleport proxy (`CLAUDE_CODE_USE_BEDROCK=1`)
- **Model:** `us.anthropic.claude-opus-4-6-v1`
- **OS:** macOS (Darwin 25.3.0)
- **Node.js:** with custom `--require` bootstrap for HTTPS proxy tunneling

## Reproduction

1. Configure Bedrock provider (`CLAUDE_CODE_USE_BEDROCK=1`)
2. Launch Claude Code with a Bedrock model ID
3. Send any prompt — the error appears repeatedly during streaming output

## Analysis

The minified code is trying to access `.speed` on model metadata (`_`) that is `undefined`. The Anthropic direct API likely returns speed/performance metadata in the streaming response, but the Bedrock endpoint does not include this field, causing the property access to fail on every chunk.

## Current workaround

Filtering stderr: `claude --model "$MODEL" 2> >(grep -v '\.speed' >&2)`

This suppresses the error messages but doesn't fix the underlying null-safety issue.

## Expected behavior

Claude Code should handle missing `.speed` metadata gracefully when using Bedrock (e.g., optional chaining `_.speed` → `_?.speed`).

# Comments on anthropics/claude-code#40189
Total: 0 comments

No comments on this issue.

---

### Issue #18028 — API Streaming Stalls Causing 59-138 Second Delays and Timeouts

State: OPEN | #18028


---

# API Streaming Stalls Causing 59-138 Second Delays and Timeouts

## Environment
- **Claude Code Version:** Latest (npm-local installation)
- **Model:** claude-sonnet-4-5-20250929 (also reproduced with claude-opus-4-5-20251101)
- **OS:** macOS (Darwin 25.2.0)
- **Date:** January 13, 2026

## Description

Claude Code is experiencing persistent streaming stalls where the API stops sending response chunks mid-generation, causing delays of 59-138 seconds before eventually timing out. This happens consistently throughout the day on normal requests with moderate context sizes.

## Symptoms

1. API request initiates successfully and receives first chunk within 2-3 seconds
2. Stream then stalls completely - no chunks received for 59-138 seconds
3. Claude Code's 5-minute timeout eventually triggers
4. Falls back to non-streaming mode, which also fails
5. Tokens displayed in UI stop incrementing during the stall
6. Ctrl+C and resume temporarily works but issue recurs

## Reproduction Pattern

### Stall Timeline (from debug logs):

**Stall #1 - 63.4 second gap:**
```
2026-01-13T13:43:29.332Z [DEBUG] Stream started - received first chunk
2026-01-13T13:44:36.209Z [WARN] Streaming stall detected: 63.4s gap between events (stall #1)
2026-01-13T13:44:36.370Z [WARN] Streaming completed with 1 stall(s), total stall time: 63.4s
```

**Stall #2 - 138.6 second gap:**
```
2026-01-13T19:30:09.876Z [DEBUG] Stream started - received first chunk
2026-01-13T19:32:32.589Z [WARN] Streaming stall detected: 138.6s gap between events (stall #1)
2026-01-13T19:32:32.783Z [WARN] Streaming completed with 1 stall(s), total stall time: 138.6s
```

**Stall #3 - 59.2 second gap:**
```
2026-01-13T20:04:13.265Z [DEBUG] File written atomically (last tool execution completed)
2026-01-13T20:05:15.332Z [WARN] Streaming stall detected: 59.2s gap between events (stall #1)
2026-01-13T20:05:15.828Z [WARN] Streaming completed with 1 stall(s), total stall time: 59.2s
```

**Timeout after 5 minutes:**
```
2026-01-13T22:48:30.773Z [DEBUG] Stream started - received first chunk
2026-01-13T22:53:39.489Z [ERROR] Error streaming, falling back to non-streaming mode: Request timed out.
```

## Frequency
Multiple times per hour, affecting majority of requests after ~10-15 minutes of session activity.

## Context Details

- **Context size:** ~15-20k tokens (~58,620 characters per auto-tool-search logs)
- **Stalls occur after:** Normal tool execution (Bash, Read, Edit) completes successfully
- **Pattern:** Stream starts fine → receives first chunk → goes silent for 59-138s → timeout
- **Network:** Verified healthy (ping to api.anthropic.com: 13-30ms, 0% packet loss, total connection time <200ms)

## What I've Ruled Out

- ✅ Local network issues (ping/curl tests show normal latency)
- ✅ Zombie processes (cleaned up all stale MCP servers)
- ✅ Resource constraints (system has ample CPU/RAM)
- ✅ Extended thinking configuration (disabled, issue persists)
- ✅ Context size (only ~15-20k tokens, well under limits)
- ✅ Local process issues (tools execute successfully before stall)

## Error Logs

### Streaming Stalls Throughout the Day:
```
2026-01-13T13:44:36.209Z [WARN] Streaming stall detected: 63.4s gap between events (stall #1)
2026-01-13T19:32:32.589Z [WARN] Streaming stall detected: 138.6s gap between events (stall #1)
2026-01-13T20:05:15.332Z [WARN] Streaming stall detected: 59.2s gap between events (stall #1)
```

### Timeout Errors:
```
2026-01-13T13:50:37.421Z [ERROR] Error streaming, falling back to non-streaming mode: Request timed out.
2026-01-13T16:32:22.956Z [ERROR] Error streaming, falling back to non-streaming mode: Request timed out.
2026-01-13T22:53:39.489Z [ERROR] Error streaming, falling back to non-streaming mode: Request timed out.
```

### Non-Streaming Fallback Also Fails:
```
2026-01-13T22:53:39.874Z [ERROR] Error in non-streaming fallback: 400 {"type":"error","error":{"type":"invalid_request_error","message":"thinking.enabled.budget_tokens: Input should be greater than or equal to 1024"},"request_id":"req_011CX6CWefspxQeyznoVaXmR"}
```

### Multiple Request Aborts (from Ctrl+C workarounds):
```
2026-01-13T20:11:37.976Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T20:57:40.796Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T22:40:09.911Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T23:03:31.116Z [ERROR] Error in non-streaming fallback: Request was aborted.
```

## Expected Behavior
API should stream response chunks continuously without 59+ second gaps.

## Actual Behavior
API starts streaming, receives first chunk within 2-3 seconds, then goes completely silent for 59-138 seconds before timing out. Pattern suggests server-side processing delays or connection handling issues on Anthropic's end.

## Workaround
Ctrl+C to interrupt the hanging request, then resume. This temporarily works but issue recurs within a few requests, requiring constant manual intervention.

## Impact
Makes Claude Code essentially unusable for sustained work - every request requires manual intervention and retry, breaking flow and productivity. Issue has persisted for entire day across multiple sessions.

## Additional Context

- Issue occurs across multiple terminal sessions
- Persists after restarting Claude Code
- Persists after killing zombie MCP server processes
- Persists after disabling extended thinking
- Persists on fresh conversation starts
- **Affects multiple models:** Reproduced with both Sonnet 4.5 and Opus 4.5
- Tools execute successfully - stall happens during API response generation
- Full debug logs available at: `~/.claude/debug/c884ff14-34d4-489b-b3cc-8fa6df30a4c8.txt`

## Attached Files

1. `bug_report_errors.log` - All WARN/ERROR messages from today's session (46 entries)
2. `bug_report_stall_context.log` - Detailed context around each streaming stall

---

**Request ID Examples:**
- `req_011CX6CWefspxQeyznoVaXmR` (timeout with thinking budget error)

**Session ID:** `c884ff14-34d4-489b-b3cc-8fa6df30a4c8`

# Comments on anthropics/claude-code#18028
Total: 7 comments

--- Comment 1 ---
Author: hugomoran159
Date: 2026-01-13T23:37:59Z

## Attached Debug Logs

**bug_report_errors.log** - All WARN/ERROR messages from session:
```
2026-01-13T13:28:33.252Z [ERROR] Error: Error: LSP server plugin:rust-analyzer-lsp:rust-analyzer crashed with exit code 1
2026-01-13T13:42:10.629Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T13:42:10.629Z [ERROR] Error: Error: Request was aborted.
2026-01-13T13:42:47.334Z [ERROR] Error: Error: 1P event logging: 110 events failed to export
2026-01-13T13:42:47.334Z [ERROR] Error: Error: {"stack":"Error: Failed to export 110 events\n    at Va1.doExport (file:///Users/hugomoran/.claude/local/node_modules/@anthropic-ai/claude-code/cli.js:260:1297)","message":"Failed to export 110 events","name":"Error"}
2026-01-13T13:42:49.242Z [ERROR] Error: Error: EISDIR: illegal operation on a directory, read
2026-01-13T13:44:36.209Z [WARN] Streaming stall detected: 63.4s gap between events (stall #1)
2026-01-13T13:44:36.370Z [WARN] Streaming completed with 1 stall(s), total stall time: 63.4s
2026-01-13T13:50:37.421Z [ERROR] Error streaming, falling back to non-streaming mode: Request timed out.
2026-01-13T16:01:23.857Z [ERROR] Error streaming, falling back to non-streaming mode: terminated
2026-01-13T16:07:11.719Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T16:07:11.719Z [ERROR] Error: Error: Request was aborted.
2026-01-13T16:14:41.210Z [ERROR] Error streaming, falling back to non-streaming mode: terminated
2026-01-13T16:32:22.956Z [ERROR] Error streaming, falling back to non-streaming mode: Request timed out.
2026-01-13T19:04:35.681Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T19:04:35.681Z [ERROR] Error: Error: Request was aborted.
2026-01-13T19:05:26.874Z [ERROR] Error: Error: 1P event logging: 200 events failed to export
2026-01-13T19:05:26.874Z [ERROR] Error: Error: {"stack":"Error: Failed to export 200 events\n    at Va1.doExport (file:///Users/hugomoran/.claude/local/node_modules/@anthropic-ai/claude-code/cli.js:260:1297)","message":"Failed to export 200 events","name":"Error"}
2026-01-13T19:32:32.589Z [WARN] Streaming stall detected: 138.6s gap between events (stall #1)
2026-01-13T19:32:32.783Z [WARN] Streaming completed with 1 stall(s), total stall time: 138.6s
2026-01-13T19:54:19.658Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T19:54:19.658Z [ERROR] Error: Error: Request was aborted.
2026-01-13T20:03:42.988Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T20:03:42.989Z [ERROR] Error: Error: Request was aborted.
2026-01-13T20:05:15.332Z [WARN] Streaming stall detected: 59.2s gap between events (stall #1)
2026-01-13T20:05:15.828Z [WARN] Streaming completed with 1 stall(s), total stall time: 59.2s
2026-01-13T20:11:37.976Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T20:11:37.976Z [ERROR] Error: Error: Request was aborted.
2026-01-13T20:57:40.795Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T20:57:40.796Z [ERROR] Error: Error: Request was aborted.
2026-01-13T22:40:09.911Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T22:40:09.911Z [ERROR] Error: Error: Request was aborted.
2026-01-13T22:41:45.593Z [ERROR] Error: Error: 1P event logging: 21 events failed to export
2026-01-13T22:41:45.593Z [ERROR] Error: Error: {"stack":"Error: Failed to export 21 events\n    at Va1.doExport (file:///Users/hugomoran/.claude/local/node_modules/@anthropic-ai/claude-code/cli.js:260:1297)","message":"Failed to export 21 events","name":"Error"}
2026-01-13T22:45:41.505Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T22:45:41.505Z [ERROR] Error: Error: Request was aborted.
2026-01-13T22:53:39.489Z [ERROR] Error streaming, falling back to non-streaming mode: Request timed out.
2026-01-13T22:53:39.874Z [ERROR] Error in non-streaming fallback: 400 {"type":"error","error":{"type":"invalid_request_error","message":"thinking.enabled.budget_tokens: Input should be greater than or equal to 1024"},"request_id":"req_011CX6CWefspxQeyznoVaXmR"}
2026-01-13T22:53:39.875Z [ERROR] Error: Error: 400 {"type":"error","error":{"type":"invalid_request_error","message":"thinking.enabled.budget_tokens: Input should be greater than or equal to 1024"},"request_id":"req_011CX6CWefspxQeyznoVaXmR"}
2026-01-13T23:03:31.116Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T23:03:31.116Z [ERROR] Error: Error: Request was aborted.
2026-01-13T23:11:49.410Z [ERROR] Error streaming, falling back to non-streaming mode: terminated
2026-01-13T23:25:56.787Z [ERROR] Error streaming, falling back to non-streaming mode: terminated
2026-01-13T23:28:37.506Z [ERROR] Error: Error: LSP server plugin:rust-analyzer-lsp:rust-analyzer crashed with exit code 1
2026-01-13T23:31:23.421Z [ERROR] Error in non-streaming fallback: Request was aborted.
2026-01-13T23:31:23.421Z [ERROR] Error: Error: Request was aborted.
```

**bug_report_stall_context.log** - Detailed context around streaming stalls:
```
2026-01-13T13:43:26.222Z [DEBUG] Auto tool search disabled: 5862 chars (threshold: 50000, 10% of context)
2026-01-13T13:43:26.236Z [DEBUG] [API:request] Creating client, ANTHROPIC_CUSTOM_HEADERS present: false, has Authorization header: false
2026-01-13T13:43:26.236Z [DEBUG] [API:auth] OAuth token check starting
2026-01-13T13:43:26.236Z [DEBUG] [API:auth] OAuth token check complete
2026-01-13T13:43:29.332Z [DEBUG] Stream started - received first chunk
2026-01-13T13:44:36.209Z [WARN] Streaming stall detected: 63.4s gap between events (stall #1)
2026-01-13T13:44:36.370Z [WARN] Streaming completed with 1 stall(s), total stall time: 63.4s
2026-01-13T13:44:36.391Z [DEBUG] executePreToolHooks called for tool: AskUserQuestion
--
2026-01-13T19:30:07.420Z [DEBUG] Auto tool search disabled: 5862 chars (threshold: 50000, 10% of context)
2026-01-13T19:30:07.428Z [DEBUG] [API:request] Creating client, ANTHROPIC_CUSTOM_HEADERS present: false, has Authorization header: false
2026-01-13T19:30:07.428Z [DEBUG] [API:auth] OAuth token check starting
2026-01-13T19:30:07.428Z [DEBUG] [API:auth] OAuth token check complete
2026-01-13T19:30:09.876Z [DEBUG] Stream started - received first chunk
2026-01-13T19:32:32.589Z [WARN] Streaming stall detected: 138.6s gap between events (stall #1)
2026-01-13T19:32:32.783Z [WARN] Streaming completed with 1 stall(s), total stall time: 138.6s
2026-01-13T19:32:32.802Z [DEBUG] executePreToolHooks called for tool: Edit
--
2026-01-13T20:04:13.265Z [DEBUG] Preserving file permissions: 100644
2026-01-13T20:04:13.265Z [DEBUG] Temp file written successfully, size: 30080 bytes
2026-01-13T20:04:13.265Z [DEBUG] Applied original permissions to temp file
2026-01-13T20:04:13.265Z [DEBUG] Renaming /Users/hugomoran/.claude.json.tmp.54073.1768334653265 to /Users/hugomoran/.claude.json
2026-01-13T20:04:13.265Z [DEBUG] File /Users/hugomoran/.claude.json written atomically
2026-01-13T20:05:15.332Z [WARN] Streaming stall detected: 59.2s gap between events (stall #1)
2026-01-13T20:05:15.828Z [WARN] Streaming completed with 1 stall(s), total stall time: 59.2s
2026-01-13T20:05:15.842Z [DEBUG] Writing to temp file: /Users/hugomoran/.claude.json.tmp.54073.1768334715842
```

--- Comment 2 ---
Author: n0vakovic
Date: 2026-02-16T13:26:18Z

**Confirming — 198 stalls over 30 days, still happening on v2.1.42**

**Environment:**
- Claude Code v2.1.42
- macOS 26.3 (arm64, Apple Silicon)
- Anthropic API (Pro subscription)

**Summary:** 198 streaming stalls logged between Jan 16 – Feb 16, 2026. Durations range from 30s to 368s. Happens daily, multiple times per day. Worst day had 31 stalls (Feb 12).

**Raw debug log data** (`grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sort`):

```
  next: "  Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  next: "  Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  next: "  Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  next: "  Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  next: "  Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  next: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  next: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  next: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  next: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  next: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  next: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  next: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "  Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "  Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "  Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "  Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "  Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "  Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
  prev: "⏺ Bash(for date in $(grep -h "Streaming stall detected" ~/.claude/debug/*.txt | sed 's/T.*//' | sort -u); do                                                                                                                      "
2026-01-16T14:53:31.162Z [WARN] Streaming stall detected: 35.1s gap between events (stall #1)
2026-01-16T22:52:26.149Z [WARN] Streaming stall detected: 37.0s gap between events (stall #1)
2026-01-21T10:49:03.660Z [WARN] Streaming stall detected: 58.2s gap between events (stall #1)
2026-01-21T13:30:34.691Z [WARN] Streaming stall detected: 42.5s gap between events (stall #1)
2026-01-21T13:45:54.241Z [WARN] Streaming stall detected: 48.8s gap between events (stall #1)
2026-01-21T21:31:26.556Z [WARN] Streaming stall detected: 45.8s gap between events (stall #1)
2026-01-21T21:35:11.000Z [WARN] Streaming stall detected: 35.6s gap between events (stall #1)
2026-01-21T21:36:28.810Z [WARN] Streaming stall detected: 38.5s gap between events (stall #1)
2026-01-21T22:10:52.199Z [WARN] Streaming stall detected: 36.1s gap between events (stall #1)
2026-01-22T16:20:52.187Z [WARN] Streaming stall detected: 34.1s gap between events (stall #1)
2026-01-22T16:22:53.884Z [WARN] Streaming stall detected: 93.8s gap between events (stall #1)
2026-01-22T17:21:18.420Z [WARN] Streaming stall detected: 50.8s gap between events (stall #1)
2026-01-22T17:53:21.044Z [WARN] Streaming stall detected: 53.7s gap between events (stall #1)
2026-01-22T17:54:19.514Z [WARN] Streaming stall detected: 47.0s gap between events (stall #1)
2026-01-23T12:00:53.455Z [WARN] Streaming stall detected: 41.0s gap between events (stall #1)
2026-01-23T13:30:03.521Z [WARN] Streaming stall detected: 35.0s gap between events (stall #1)
2026-01-23T16:21:55.155Z [WARN] Streaming stall detected: 30.6s gap between events (stall #1)
2026-01-23T16:24:03.373Z [WARN] Streaming stall detected: 36.2s gap between events (stall #1)
2026-01-23T16:26:04.173Z [WARN] Streaming stall detected: 42.7s gap between events (stall #1)
2026-01-23T16:44:55.856Z [WARN] Streaming stall detected: 31.0s gap between events (stall #1)
2026-01-23T16:44:58.918Z [WARN] Streaming stall detected: 38.9s gap between events (stall #1)
2026-01-23T17:04:23.167Z [WARN] Streaming stall detected: 40.3s gap between events (stall #1)
2026-01-24T10:19:04.400Z [WARN] Streaming stall detected: 47.6s gap between events (stall #1)
2026-01-24T10:26:24.924Z [WARN] Streaming stall detected: 36.9s gap between events (stall #1)
2026-01-24T10:31:30.615Z [WARN] Streaming stall detected: 46.8s gap between events (stall #1)
2026-01-24T10:57:55.134Z [WARN] Streaming stall detected: 101.5s gap between events (stall #1)
2026-01-24T11:10:48.836Z [WARN] Streaming stall detected: 38.5s gap between events (stall #1)
2026-01-24T11:19:11.556Z [WARN] Streaming stall detected: 79.1s gap between events (stall #1)
2026-01-24T12:25:42.348Z [WARN] Streaming stall detected: 34.2s gap between events (stall #1)
2026-01-24T17:18:04.556Z [WARN] Streaming stall detected: 145.2s gap between events (stall #1)
2026-01-24T17:57:53.603Z [WARN] Streaming stall detected: 31.7s gap between events (stall #1)
2026-01-24T17:57:57.907Z [WARN] Streaming stall detected: 30.6s gap between events (stall #1)
2026-01-24T17:58:10.795Z [WARN] Streaming stall detected: 42.0s gap between events (stall #1)
2026-01-24T17:58:11.073Z [WARN] Streaming stall detected: 49.1s gap between events (stall #1)
2026-01-24T17:58:19.259Z [WARN] Streaming stall detected: 50.1s gap between events (stall #1)
2026-01-24T18:05:57.510Z [WARN] Streaming stall detected: 368.6s gap between events (stall #1)
2026-01-25T18:40:08.465Z [WARN] Streaming stall detected: 42.1s gap between events (stall #1)
2026-01-25T19:28:38.228Z [WARN] Streaming stall detected: 30.9s gap between events (stall #1)
2026-01-25T21:31:54.832Z [WARN] Streaming stall detected: 47.3s gap between events (stall #1)
2026-01-25T21:55:01.231Z [WARN] Streaming stall detected: 60.9s gap between events (stall #1)
2026-01-25T22:53:56.080Z [WARN] Streaming stall detected: 38.9s gap between events (stall #1)
2026-01-25T23:17:22.419Z [WARN] Streaming stall detected: 142.9s gap between events (stall #1)
2026-01-25T23:28:04.435Z [WARN] Streaming stall detected: 90.5s gap between events (stall #1)
2026-01-26T11:06:06.655Z [WARN] Streaming stall detected: 42.9s gap between events (stall #1)
2026-01-26T11:08:26.966Z [WARN] Streaming stall detected: 42.9s gap between events (stall #1)
2026-01-26T11:19:47.227Z [WARN] Streaming stall detected: 35.9s gap between events (stall #1)
2026-01-26T11:21:39.762Z [WARN] Streaming stall detected: 72.9s gap between events (stall #1)
2026-01-26T11:28:53.326Z [WARN] Streaming stall detected: 48.4s gap between events (stall #1)
2026-01-26T11:34:25.855Z [WARN] Streaming stall detected: 81.3s gap between events (stall #1)
2026-01-26T12:47:18.893Z [WARN] Streaming stall detected: 31.8s gap between events (stall #1)
2026-01-26T13:17:36.214Z [WARN] Streaming stall detected: 36.1s gap between events (stall #1)
2026-01-26T15:56:54.011Z [WARN] Streaming stall detected: 31.3s gap between events (stall #1)
2026-01-26T19:25:55.016Z [WARN] Streaming stall detected: 32.5s gap between events (stall #1)
2026-01-26T19:29:15.187Z [WARN] Streaming stall detected: 107.2s gap between events (stall #1)
2026-01-27T13:24:05.110Z [WARN] Streaming stall detected: 31.4s gap between events (stall #1)
2026-01-27T13:32:07.301Z [WARN] Streaming stall detected: 43.1s gap between events (stall #1)
2026-01-27T13:53:19.558Z [WARN] Streaming stall detected: 58.4s gap between events (stall #1)
2026-01-27T14:19:33.516Z [WARN] Streaming stall detected: 33.4s gap between events (stall #1)
2026-01-27T14:25:53.963Z [WARN] Streaming stall detected: 32.2s gap between events (stall #1)
2026-01-27T15:02:16.826Z [WARN] Streaming stall detected: 31.3s gap between events (stall #1)
2026-01-27T15:13:16.173Z [WARN] Streaming stall detected: 37.4s gap between events (stall #1)
2026-01-27T15:13:36.244Z [WARN] Streaming stall detected: 199.4s gap between events (stall #1)
2026-01-27T15:14:12.430Z [WARN] Streaming stall detected: 55.8s gap between events (stall #2)
2026-01-27T15:35:14.692Z [WARN] Streaming stall detected: 49.7s gap between events (stall #1)
2026-01-27T16:23:01.987Z [WARN] Streaming stall detected: 38.3s gap between events (stall #1)
2026-01-27T17:28:32.135Z [WARN] Streaming stall detected: 88.9s gap between events (stall #1)
2026-01-27T17:43:29.322Z [WARN] Streaming stall detected: 41.3s gap between events (stall #1)
2026-01-27T21:28:26.336Z [WARN] Streaming stall detected: 31.0s gap between events (stall #1)
2026-01-28T11:54:03.111Z [WARN] Streaming stall detected: 53.3s gap between events (stall #1)
2026-01-28T12:54:49.518Z [WARN] Streaming stall detected: 40.4s gap between events (stall #1)
2026-01-28T18:23:09.408Z [WARN] Streaming stall detected: 31.8s gap between events (stall #1)
2026-01-28T18:31:06.237Z [WARN] Streaming stall detected: 47.4s gap between events (stall #1)
2026-01-29T10:09:38.196Z [WARN] Streaming stall detected: 37.1s gap between events (stall #1)
2026-01-29T10:15:55.534Z [WARN] Streaming stall detected: 35.2s gap between events (stall #1)
2026-01-29T10:49:24.590Z [WARN] Streaming stall detected: 78.4s gap between events (stall #1)
2026-01-29T10:54:30.474Z [WARN] Streaming stall detected: 48.9s gap between events (stall #1)
2026-01-29T11:44:25.508Z [WARN] Streaming stall detected: 49.0s gap between events (stall #1)
2026-01-29T13:22:01.839Z [WARN] Streaming stall detected: 38.0s gap between events (stall #1)
2026-01-29T15:42:14.740Z [WARN] Streaming stall detected: 32.8s gap between events (stall #1)
2026-01-29T16:13:01.913Z [WARN] Streaming stall detected: 59.4s gap between events (stall #1)
2026-01-29T16:24:42.128Z [WARN] Streaming stall detected: 42.7s gap between events (stall #1)
2026-01-29T16:50:41.888Z [WARN] Streaming stall detected: 60.0s gap between events (stall #1)
2026-01-29T16:57:52.748Z [WARN] Streaming stall detected: 52.7s gap between events (stall #1)
2026-01-29T17:25:26.347Z [WARN] Streaming stall detected: 70.7s gap between events (stall #1)
2026-01-29T18:48:21.627Z [WARN] Streaming stall detected: 64.5s gap between events (stall #1)
2026-01-29T19:06:27.202Z [WARN] Streaming stall detected: 100.6s gap between events (stall #1)
2026-01-30T11:47:57.812Z [WARN] Streaming stall detected: 63.6s gap between events (stall #1)
2026-01-30T14:04:41.196Z [WARN] Streaming stall detected: 35.8s gap between events (stall #1)
2026-01-30T15:31:59.925Z [WARN] Streaming stall detected: 56.6s gap between events (stall #1)
2026-01-30T15:43:38.786Z [WARN] Streaming stall detected: 32.3s gap between events (stall #1)
2026-01-30T15:59:35.981Z [WARN] Streaming stall detected: 33.9s gap between events (stall #1)
2026-01-30T18:36:21.918Z [WARN] Streaming stall detected: 31.9s gap between events (stall #1)
2026-01-30T18:37:33.590Z [WARN] Streaming stall detected: 36.3s gap between events (stall #1)
2026-01-31T20:27:04.002Z [WARN] Streaming stall detected: 176.9s gap between events (stall #1)
2026-01-31T20:30:28.659Z [WARN] Streaming stall detected: 52.2s gap between events (stall #1)
2026-01-31T20:31:35.393Z [WARN] Streaming stall detected: 59.6s gap between events (stall #1)
2026-01-31T20:33:55.049Z [WARN] Streaming stall detected: 32.1s gap between events (stall #1)
2026-01-31T20:34:27.179Z [WARN] Streaming stall detected: 31.6s gap between events (stall #2)
2026-01-31T20:34:59.173Z [WARN] Streaming stall detected: 30.3s gap between events (stall #3)
2026-01-31T20:35:33.631Z [WARN] Streaming stall detected: 33.3s gap between events (stall #4)
2026-01-31T20:37:24.539Z [WARN] Streaming stall detected: 179.3s gap between events (stall #1)
2026-01-31T20:38:32.968Z [WARN] Streaming stall detected: 215.4s gap between events (stall #1)
2026-01-31T20:38:45.817Z [WARN] Streaming stall detected: 194.5s gap between events (stall #1)
2026-01-31T20:39:10.308Z [WARN] Streaming stall detected: 186.8s gap between events (stall #1)
2026-01-31T20:40:17.861Z [WARN] Streaming stall detected: 165.8s gap between events (stall #1)
2026-01-31T20:41:49.791Z [WARN] Streaming stall detected: 178.8s gap between events (stall #1)
2026-01-31T20:42:02.787Z [WARN] Streaming stall detected: 204.1s gap between events (stall #1)
2026-01-31T20:42:25.841Z [WARN] Streaming stall detected: 190.2s gap between events (stall #1)
2026-01-31T20:43:13.913Z [WARN] Streaming stall detected: 171.0s gap between events (stall #1)
2026-02-01T14:15:25.081Z [WARN] Streaming stall detected: 61.6s gap between events (stall #1)
2026-02-01T14:21:02.335Z [WARN] Streaming stall detected: 59.0s gap between events (stall #1)
2026-02-01T14:23:20.662Z [WARN] Streaming stall detected: 33.1s gap between events (stall #1)
2026-02-01T14:28:04.486Z [WARN] Streaming stall detected: 111.7s gap between events (stall #1)
2026-02-01T14:31:58.116Z [WARN] Streaming stall detected: 74.4s gap between events (stall #1)
2026-02-01T14:35:52.094Z [WARN] Streaming stall detected: 72.2s gap between events (stall #1)
2026-02-01T14:46:07.424Z [WARN] Streaming stall detected: 90.9s gap between events (stall #1)
2026-02-01T14:53:58.004Z [WARN] Streaming stall detected: 117.3s gap between events (stall #1)
2026-02-01T15:07:37.596Z [WARN] Streaming stall detected: 34.7s gap between events (stall #1)
2026-02-01T15:12:26.392Z [WARN] Streaming stall detected: 47.1s gap between events (stall #1)
2026-02-01T15:43:43.736Z [WARN] Streaming stall detected: 119.9s gap between events (stall #1)
2026-02-01T15:58:37.130Z [WARN] Streaming stall detected: 39.7s gap between events (stall #1)
2026-02-01T16:16:20.337Z [WARN] Streaming stall detected: 33.8s gap between events (stall #1)
2026-02-01T17:11:31.705Z [WARN] Streaming stall detected: 138.7s gap between events (stall #1)
2026-02-01T17:21:51.447Z [WARN] Streaming stall detected: 148.9s gap between events (stall #1)
2026-02-01T17:34:47.827Z [WARN] Streaming stall detected: 39.7s gap between events (stall #1)
2026-02-01T17:44:20.390Z [WARN] Streaming stall detected: 53.7s gap between events (stall #1)
2026-02-01T17:49:28.682Z [WARN] Streaming stall detected: 36.3s gap between events (stall #1)
2026-02-01T19:39:28.215Z [WARN] Streaming stall detected: 140.0s gap between events (stall #1)
2026-02-01T19:40:20.894Z [WARN] Streaming stall detected: 38.6s gap between events (stall #1)
2026-02-01T20:59:00.096Z [WARN] Streaming stall detected: 30.2s gap between events (stall #1)
2026-02-01T21:00:05.614Z [WARN] Streaming stall detected: 30.8s gap between events (stall #1)
2026-02-01T21:02:55.903Z [WARN] Streaming stall detected: 44.7s gap between events (stall #1)
2026-02-02T10:15:14.421Z [WARN] Streaming stall detected: 44.8s gap between events (stall #1)
2026-02-02T11:46:01.439Z [WARN] Streaming stall detected: 40.6s gap between events (stall #1)
2026-02-02T13:28:14.493Z [WARN] Streaming stall detected: 34.0s gap between events (stall #1)
2026-02-02T13:32:21.766Z [WARN] Streaming stall detected: 93.1s gap between events (stall #1)
2026-02-02T14:26:53.001Z [WARN] Streaming stall detected: 35.5s gap between events (stall #1)
2026-02-02T14:31:25.936Z [WARN] Streaming stall detected: 114.8s gap between events (stall #1)
2026-02-02T14:39:40.769Z [WARN] Streaming stall detected: 57.2s gap between events (stall #1)
2026-02-02T16:35:54.048Z [WARN] Streaming stall detected: 38.0s gap between events (stall #1)
2026-02-02T16:37:02.023Z [WARN] Streaming stall detected: 37.0s gap between events (stall #2)
2026-02-02T16:58:12.481Z [WARN] Streaming stall detected: 60.4s gap between events (stall #1)
2026-02-03T13:20:36.057Z [WARN] Streaming stall detected: 30.1s gap between events (stall #1)
2026-02-03T13:40:18.212Z [WARN] Streaming stall detected: 87.9s gap between events (stall #1)
2026-02-03T14:08:51.811Z [WARN] Streaming stall detected: 37.1s gap between events (stall #1)
2026-02-03T14:24:14.249Z [WARN] Streaming stall detected: 79.8s gap between events (stall #1)
2026-02-03T14:52:09.944Z [WARN] Streaming stall detected: 41.9s gap between events (stall #1)
2026-02-03T14:56:00.676Z [WARN] Streaming stall detected: 35.8s gap between events (stall #1)
2026-02-03T18:10:24.977Z [WARN] Streaming stall detected: 31.6s gap between events (stall #1)
2026-02-05T10:14:05.993Z [WARN] Streaming stall detected: 73.0s gap between events (stall #1)
2026-02-05T10:21:24.252Z [WARN] Streaming stall detected: 49.6s gap between events (stall #1)
2026-02-05T10:28:42.603Z [WARN] Streaming stall detected: 35.4s gap between events (stall #1)
2026-02-05T10:31:59.942Z [WARN] Streaming stall detected: 138.4s gap between events (stall #1)
2026-02-05T10:46:31.172Z [WARN] Streaming stall detected: 126.0s gap between events (stall #1)
2026-02-05T13:22:38.960Z [WARN] Streaming stall detected: 61.2s gap between events (stall #1)
2026-02-05T15:34:03.301Z [WARN] Streaming stall detected: 41.8s gap between events (stall #1)
2026-02-06T00:09:34.431Z [WARN] Streaming stall detected: 70.7s gap between events (stall #1)
2026-02-06T00:17:42.904Z [WARN] Streaming stall detected: 139.1s gap between events (stall #1)
2026-02-06T00:23:10.957Z [WARN] Streaming stall detected: 198.0s gap between events (stall #1)
2026-02-06T00:44:54.887Z [WARN] Streaming stall detected: 35.5s gap between events (stall #1)
2026-02-06T01:06:10.599Z [WARN] Streaming stall detected: 66.6s gap between events (stall #1)
2026-02-06T01:07:50.164Z [WARN] Streaming stall detected: 30.4s gap between events (stall #1)
2026-02-06T13:20:50.701Z [WARN] Streaming stall detected: 123.5s gap between events (stall #1)
2026-02-06T13:24:22.714Z [WARN] Streaming stall detected: 41.9s gap between events (stall #1)
2026-02-06T13:39:43.361Z [WARN] Streaming stall detected: 77.1s gap between events (stall #1)
2026-02-06T14:04:58.590Z [WARN] Streaming stall detected: 31.3s gap between events (stall #1)
2026-02-06T14:25:57.712Z [WARN] Streaming stall detected: 41.4s gap between events (stall #1)
2026-02-06T14:32:01.101Z [WARN] Streaming stall detected: 43.7s gap between events (stall #1)
2026-02-07T14:36:24.419Z [WARN] Streaming stall detected: 81.7s gap between events (stall #1)
2026-02-07T14:41:34.112Z [WARN] Streaming stall detected: 32.2s gap between events (stall #1)
2026-02-07T15:14:46.292Z [WARN] Streaming stall detected: 35.9s gap between events (stall #1)
2026-02-07T15:21:06.433Z [WARN] Streaming stall detected: 77.6s gap between events (stall #1)
2026-02-07T15:23:04.899Z [WARN] Streaming stall detected: 30.2s gap between events (stall #1)
2026-02-10T14:36:03.971Z [WARN] Streaming stall detected: 153.8s gap between events (stall #1)
2026-02-10T15:25:37.548Z [WARN] Streaming stall detected: 41.5s gap between events (stall #1)
2026-02-10T15:43:36.483Z [WARN] Streaming stall detected: 186.4s gap between events (stall #1)
2026-02-11T14:02:54.616Z [WARN] Streaming stall detected: 44.4s gap between events (stall #1)
2026-02-11T15:14:20.329Z [WARN] Streaming stall detected: 75.0s gap between events (stall #1)
2026-02-11T15:37:40.379Z [WARN] Streaming stall detected: 35.2s gap between events (stall #1)
2026-02-12T12:23:02.923Z [WARN] Streaming stall detected: 38.8s gap between events (stall #1)
2026-02-12T12:43:41.596Z [WARN] Streaming stall detected: 36.2s gap between events (stall #1)
2026-02-12T12:54:11.091Z [WARN] Streaming stall detected: 30.5s gap between events (stall #1)
2026-02-12T13:03:16.042Z [WARN] Streaming stall detected: 33.0s gap between events (stall #1)
2026-02-12T13:11:45.081Z [WARN] Streaming stall detected: 68.5s gap between events (stall #1)
2026-02-12T13:25:55.277Z [WARN] Streaming stall detected: 51.8s gap between events (stall #1)
2026-02-12T13:43:40.113Z [WARN] Streaming stall detected: 41.3s gap between events (stall #1)
2026-02-12T15:05:58.946Z [WARN] Streaming stall detected: 35.7s gap between events (stall #1)
2026-02-12T15:13:02.371Z [WARN] Streaming stall detected: 38.4s gap between events (stall #1)
2026-02-12T15:14:55.920Z [WARN] Streaming stall detected: 36.4s gap between events (stall #1)
2026-02-12T15:18:44.310Z [WARN] Streaming stall detected: 54.2s gap between events (stall #1)
2026-02-12T15:20:47.884Z [WARN] Streaming stall detected: 44.7s gap between events (stall #1)
2026-02-12T15:28:36.291Z [WARN] Streaming stall detected: 55.6s gap between events (stall #1)
2026-02-12T15:30:33.171Z [WARN] Streaming stall detected: 41.5s gap between events (stall #1)
2026-02-12T15:35:25.834Z [WARN] Streaming stall detected: 72.5s gap between events (stall #1)
2026-02-12T15:41:11.361Z [WARN] Streaming stall detected: 63.5s gap between events (stall #1)
2026-02-12T15:45:33.111Z [WARN] Streaming stall detected: 35.0s gap between events (stall #1)
2026-02-12T16:37:22.484Z [WARN] Streaming stall detected: 36.6s gap between events (stall #1)
2026-02-12T16:38:57.953Z [WARN] Streaming stall detected: 35.2s gap between events (stall #1)
2026-02-12T16:39:47.953Z [WARN] Streaming stall detected: 46.9s gap between events (stall #1)
2026-02-12T16:40:35.360Z [WARN] Streaming stall detected: 44.0s gap between events (stall #1)
2026-02-12T17:00:25.571Z [WARN] Streaming stall detected: 34.5s gap between events (stall #1)
2026-02-12T17:13:45.146Z [WARN] Streaming stall detected: 83.4s gap between events (stall #1)
2026-02-12T17:24:10.952Z [WARN] Streaming stall detected: 97.4s gap between events (stall #1)
2026-02-12T17:40:50.368Z [WARN] Streaming stall detected: 43.7s gap between events (stall #1)
2026-02-12T17:45:46.372Z [WARN] Streaming stall detected: 51.2s gap between events (stall #1)
2026-02-12T18:15:40.791Z [WARN] Streaming stall detected: 31.0s gap between events (stall #1)
2026-02-12T18:20:36.975Z [WARN] Streaming stall detected: 51.0s gap between events (stall #1)
2026-02-12T18:22:01.778Z [WARN] Streaming stall detected: 31.2s gap between events (stall #1)
2026-02-12T18:37:26.231Z [WARN] Streaming stall detected: 49.2s gap between events (stall #1)
2026-02-12T19:02:12.765Z [WARN] Streaming stall detected: 30.4s gap between events (stall #1)
2026-02-13T10:06:45.277Z [WARN] Streaming stall detected: 271.8s gap between events (stall #1)
2026-02-13T10:06:45.586Z [WARN] Streaming stall detected: 62.2s gap between events (stall #1)
2026-02-13T10:11:23.868Z [WARN] Streaming stall detected: 271.0s gap between events (stall #1)
2026-02-13T10:16:25.605Z [WARN] Streaming stall detected: 281.2s gap between events (stall #1)
2026-02-13T10:27:49.483Z [WARN] Streaming stall detected: 45.5s gap between events (stall #1)
2026-02-13T10:30:55.648Z [WARN] Streaming stall detected: 60.7s gap between events (stall #1)
2026-02-13T10:39:58.205Z [WARN] Streaming stall detected: 41.2s gap between events (stall #1)
2026-02-13T10:42:34.918Z [WARN] Streaming stall detected: 38.3s gap between events (stall #1)
2026-02-13T10:45:51.767Z [WARN] Streaming stall detected: 36.6s gap between events (stall #1)
2026-02-13T10:48:57.143Z [WARN] Streaming stall detected: 138.9s gap between events (stall #1)
2026-02-13T10:50:00.925Z [WARN] Streaming stall detected: 46.6s gap between events (stall #1)
2026-02-13T10:53:34.808Z [WARN] Streaming stall detected: 36.9s gap between events (stall #1)
2026-02-13T12:17:44.109Z [WARN] Streaming stall detected: 50.6s gap between events (stall #1)
2026-02-13T14:00:45.816Z [WARN] Streaming stall detected: 43.2s gap between events (stall #1)
2026-02-13T14:32:49.765Z [WARN] Streaming stall detected: 48.7s gap between events (stall #1)
2026-02-13T14:41:15.467Z [WARN] Streaming stall detected: 99.0s gap between events (stall #1)
2026-02-13T15:39:01.480Z [WARN] Streaming stall detected: 31.2s gap between events (stall #1)
2026-02-13T15:41:23.061Z [WARN] Streaming stall detected: 49.0s gap between events (stall #1)
2026-02-14T09:38:37.408Z [WARN] Streaming stall detected: 55.2s gap between events (stall #1)
2026-02-14T12:17:47.945Z [WARN] Streaming stall detected: 61.0s gap between events (stall #1)
2026-02-14T12:35:39.362Z [WARN] Streaming stall detected: 62.4s gap between events (stall #1)
2026-02-14T12:37:28.441Z [WARN] Streaming stall detected: 38.8s gap between events (stall #1)
2026-02-16T13:08:05.729Z [WARN] Streaming stall detected: 31.8s gap between events (stall #1)
2026-02-16T13:14:25.553Z [WARN] Streaming stall detected: 94.3s gap between events (stall #1)
2026-02-16T13:25:32.845Z [WARN] Streaming stall detected: 103.3s gap between events (stall #1)
```

--- Comment 3 ---
Author: jingyu233
Date: 2026-02-20T18:24:39Z

Have you used any third-party APIs? I encountered the following problem when using a third-party API. I'm not sure if this problem will also occur through official subscriptions, but I've encountered the same problem with many unofficial services I've tried.


2026-02-21 02:19:50.668 [info] From claude: 2026-02-20T18:19:50.668Z [DEBUG] Metrics export disabled by organization setting

2026-02-21 02:20:39.341 [info] From claude: 2026-02-20T18:20:39.340Z [WARN] Streaming stall detected: 51.6s gap between events (stall #1)

2026-02-21 02:21:33.829 [info] From claude: 2026-02-20T18:21:33.828Z [ERROR] Error streaming, falling back to non-streaming mode: The socket connection was closed unexpectedly. For more information, pass `verbose: true` in the second argument to fetch()

2026-02-21 02:21:34.847 [info] From claude: 2026-02-20T18:21:33.949Z [DEBUG] [API:request] Creating client, ANTHROPIC_CUSTOM_HEADERS present: false, has Authorization header: false
2026-02-20T18:21:33.949Z [DEBUG] [API:auth] OAuth token check starting
2026-02-20T18:21:33.973Z [DEBUG] [API:auth] OAuth token check complete

2026-02-21 02:22:35.488 [info] From claude: 2026-02-20T18:22:35.488Z [ERROR] API error (attempt 1/11)

--- Comment 4 ---
Author: dmytro-hnatiuk
Date: 2026-04-07T20:42:59Z

+1 — confirming this is still happening on 2026-04-07 in Claude Code **2.1.92** (latest), **Opus 4.6 1M context**, macOS 15.6 Apple Silicon. Three months after the original report and the exact same `Streaming stall detected` warnings are firing.

## 7 stalls captured in a single ~25-minute session

```
2026-04-07T20:00:40.210Z [WARN] Streaming stall detected:  95.6s gap between events
2026-04-07T20:04:28.122Z [WARN] Streaming stall detected: 216.4s gap between events
2026-04-07T20:11:55.221Z [WARN] Streaming stall detected:  65.6s gap between events
2026-04-07T20:13:57.207Z [WARN] Streaming stall detected:  41.6s gap between events
2026-04-07T20:18:00.766Z [WARN] Streaming stall detected:  82.5s gap between events
2026-04-07T20:18:42.674Z [WARN] Streaming stall detected:  30.2s gap between events
2026-04-07T20:20:28.209Z [WARN] Streaming stall detected:  54.6s gap between events
```

Each is followed by `Streaming completed with 1 stall(s)` — i.e. the streams **eventually** resolve but with multi-minute gaps in the middle. Earlier the same day, some stalls never resolved at all and required \`kill -9\` to recover (consistent with the dead-stream / no-watchdog mechanism described in #33949).

## Same TTFB profile as the original report

96 successful requests in this session:

```
median TTFB: 1.82s
p95 TTFB:    4.86s
max TTFB:    8.46s
```

Initial response is fast and healthy — the stall always happens **after** `Stream started - received first chunk`, mid-response. Identical to the OP.

## What I additionally verified

- **Not context-size dependent**: stalls occurred at autocompact buckets of 1.4k, 51k, 105k, AND 355k tokens — the smallest fresh sessions hang too.
- **Not network**: ping to api.anthropic.com 2.7ms, 0% loss; TLS handshake ~150ms; both v4 and v6 paths reachable.
- **Not effortLevel/extended thinking**: stalls fire on responses with no thinking tokens.
- **Not hooks**: \`Hooks: Found 0 total hooks in registry\`.
- **Not local CPU/memory**: process is sleeping in \`kevent64\` during the stall, not CPU-bound.
- **Not a stuck local socket**: \`nettop\` shows ZERO bytes flowing on the ESTABLISHED TCP connection during the gap. Server-side stop, no FIN.
- **Correlated with Anthropic-side capacity**: today's stalls coincide with the active "Elevated errors on Claude.ai" incident on https://status.claude.com/ (and yesterday's similar incident, ~8000 Downdetector reports).

## Cross-reference

#33949 has the root-cause analysis (\`messages.stream()\` has no client-side timeout, dead SSE connections never trigger an error, no heartbeat detection on \`:ping\` comments). This issue is the user-facing symptom of what that issue diagnoses. The fix proposed there (idle-stream watchdog that aborts after N seconds without an SSE event) would resolve both.

This bug has been open since January with zero comments. Three months later, on the latest CLI version, the symptom is identical and getting more frequent under capacity load. Worth prioritizing.

--- Comment 5 ---
Author: CaptFaraday
Date: 2026-04-08T16:41:43Z

Still happening as of April 2026 on Claude Code Max (Opus, high effort thinking).

My experience matches the pattern described here exactly — stream starts, stalls almost immediately during extended thinking, then eventually times out. The difference is that with high-effort Opus thinking, the stall durations are extreme:

```
✶ Writing implementation plan… (45m 32s · ↓ 47 tokens · thinking with high effort)
```

47 tokens in 45 minutes before timeout. And then it loops:

```
● Now I have everything I need. Let me write the implementation plan.
  ⎿  Request timed out

✻ Churned for 1h 43m 44s

❯ What happened
  ⎿  Request timed out

✻ Brewed for 56m 16s
```

This is compounded by the dead non-streaming fallback code documented in #39755 — when the watchdog fires, it throws instead of retrying via non-streaming mode, so there's no recovery path.

For anyone hitting this: lowering to `/effort medium` seems to reduce the frequency since shorter thinking phases are less likely to stall. But that's a workaround, not a fix.

--- Comment 6 ---
Author: emmahyde
Date: 2026-04-12T14:22:03Z

This has been happening constantly this weekend.

--- Comment 7 ---
Author: BobMali
Date: 2026-05-19T13:11:48Z

This issue is not stale. It's just nobody working on it.

---

### Issue #38569 — [DOCS] Document the non-streaming API fallback mechanism, including its token cap and timeout behavior

State: OPEN | #38569
Labels: documentation, area:api


---

### Documentation Type

other

### Documentation Location


https://code.claude.com/docs/en/how-claude-code-works

### Section/Topic


- `https://code.claude.com/docs/en/how-claude-code-works` — primary candidate for explaining the fallback mechanism as part of how Claude Code communicates with the API
- `https://code.claude.com/docs/en/env-vars` — secondary candidate if there are or will be env vars controlling this behavior
- `https://code.claude.com/docs/en/troubleshooting` — tertiary candidate for a note explaining why responses may appear truncated in certain network environments

### Current Documentation


None of the documentation pages — including `how-claude-code-works.md`, `settings.md`, `env-vars.md`, `cli-reference.md`, or `troubleshooting.md` — mention the non-streaming fallback mechanism. Users encountering truncated responses or hangs caused by the fallback path have no documentation to consult.

The only public record of this mechanism is in changelog entries:
- v2.1.79: "Improved non-streaming API fallback with a 2-minute per-attempt timeout, preventing sessions from hanging indefinitely"
- v2.1.83: "Increased non-streaming fallback token cap (21k → 64k) and timeout (120s → 300s local) so fallback requests are less likely to be truncated"

### What's Wrong or Missing?


The docs should explain:

- What the non-streaming fallback is: an alternate request mode Claude Code uses when streaming is unavailable (e.g., due to proxy incompatibility, network conditions, or API errors)
- That fallback requests have a maximum output token limit (currently 64k) — responses longer than this cap may be truncated
- That fallback requests have a per-attempt timeout (currently 300s locally) — requests that exceed this will fail rather than hang indefinitely
- Under what conditions the fallback is triggered (e.g., streaming endpoint returns a 404, gateway incompatibility)
- Practical guidance for users in environments where fallback is common (e.g., certain LLM gateway configurations)

### Suggested Improvement


1. Navigate to https://code.claude.com/docs/en/how-claude-code-works
2. Search for "non-streaming", "fallback", "token cap", or "truncat"
3. Observe: no results — the mechanism is not described anywhere in the docs

### Impact

Medium - Makes feature difficult to understand

### Additional Context


- Changelog v2.1.83 entry: "Increased non-streaming fallback token cap (21k → 64k) and timeout (120s → 300s local) so fallback requests are less likely to be truncated"
- Related changelog v2.1.79: "Improved non-streaming API fallback with a 2-minute per-attempt timeout, preventing sessions from hanging indefinitely"
- Related changelog v2.1.79: "Fixed cost and token usage not being tracked when the API falls back to non-streaming mode"
- Related changelog (earlier): "Fixed API proxy compatibility issue where 404 errors on streaming endpoints no longer triggered non-streaming fallback"

# Comments on anthropics/claude-code#38569
Total: 3 comments

--- Comment 1 ---
Author: coygeek
Date: 2026-04-09T17:30:10Z

Re-verified against the latest docs mirror. This is still not resolved. The docs now mention CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK in env-vars.md, but they still do not document the fallback mechanism itself, when it triggers, or its current token cap and timeout behavior outside the changelog.

--- Comment 2 ---
Author: coygeek
Date: 2026-05-11T04:37:04Z

Just checked the current docs again. This issue is not fully resolved yet.

--- Comment 3 ---
Author: coygeek
Date: 2026-05-28T22:35:27Z

Still relevant as of 2026-05-28. I checked the current docs and this documentation gap still appears unresolved.

---

### Issue #62534 — Long streamed responses occasionally triplicate sections of output

State: OPEN | #62534
Labels: bug, platform:macos, area:tui


---

## Summary

On longer streamed responses (~3000+ tokens, multi-minute renders), Claude Code occasionally re-emits middle chunks of the output, producing visible triplication of headers and content in the terminal. The model's own context shows the response only once, so this appears to be happening at the streaming/rendering layer between model output and terminal display — and is invisible to the model.

## Repro pattern

- Trigger any skill or response that produces >2500 tokens of output
- Likelihood scales with response length and time-to-complete (a 2m 36s "Brewed" indicator was observed in one repro)
- Reporting user has hit this multiple times; "almost always for longer outputs"

## Observed example

- Skill: a long newsletter-digest output (~3000 tokens, "Brewed for 2m 36s")
- Symptom: a `### READ THESE FIRST` block + an `### 🤖 Tech / AI` block were each emitted three times in a row in the terminal
- Same content, same formatting, repeated verbatim
- Verified in the model's own context view: the message appears exactly once. The duplication is purely at the delivery layer.

## Why this is hard to diagnose from the model's side

The model doesn't see what the terminal renders — only what gets recorded as the final delivered message. So when the user reports duplication, the model has no signal that anything is wrong with its own output, may even dispute the user's report ("I see the section only once"), and will misdiagnose by proposing changes to the upstream skill logic instead of the streaming layer.

A model-side affordance (e.g. ability to read the rendered transcript, or a streaming-integrity checksum) would help here. Failing that, faster identification of the symptom as "this is a known CC delivery bug, not a skill issue" via a documented troubleshooting note would save user time.

## Environment

- Claude Code CLI on macOS Darwin 24.6.0
- Model: Opus 4.7 (1M context)
- Long, streaming-heavy response

## Screenshots

User has 3 screenshots that clearly show the triplication. Not auto-attached because they contain personal reading-list content. Available on request.

# Comments on anthropics/claude-code#62534
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-26T16:05:46Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/57133
2. https://github.com/anthropics/claude-code/issues/52020
3. https://github.com/anthropics/claude-code/issues/52924

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: Keesan12
Date: 2026-05-26T16:50:07Z

This looks like a stream-rendering bug, not duplicated model generation. A render-path checksum or replay marker would help tell the difference between duplicated transport and duplicated output, which is the part the model itself cannot see.

---

### Issue #47623 — [DOCS] Environment variable docs are outdated for stalled stream recovery behavior

State: OPEN | #47623
Labels: documentation, enhancement


---

### Documentation Type

Incorrect/outdated documentation

### Documentation Location


https://code.claude.com/docs/en/env-vars

### Section/Topic


`CLAUDE_ENABLE_STREAM_WATCHDOG`, `CLAUDE_STREAM_IDLE_TIMEOUT_MS`, and `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK`

### Current Documentation


The env var reference currently says:

> `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK` | Set to `1` to disable the non-streaming fallback when a streaming request fails mid-stream. Streaming errors propagate to the retry layer instead. Useful when a proxy or gateway causes the fallback to produce duplicate tool execution

> `CLAUDE_ENABLE_STREAM_WATCHDOG` | Set to `1` to abort API response streams that stall with no data for 90 seconds. Useful in automated environments where a hung session would go unnoticed, or behind proxies that drop connections silently. Without this, a stalled stream can hang the session indefinitely since the request timeout only covers the initial connection. Configure the timeout with `CLAUDE_STREAM_IDLE_TIMEOUT_MS`

> `CLAUDE_STREAM_IDLE_TIMEOUT_MS` | Timeout in milliseconds before the streaming idle watchdog closes a stalled connection. Default: `90000` (90 seconds). Requires `CLAUDE_ENABLE_STREAM_WATCHDOG=1`. Increase this value if long-running tools or slow networks cause premature timeout errors

### What's Wrong or Missing?


Changelog v2.1.105 says:

> Improved stalled API stream handling: streams now abort after 5 minutes of no data and retry non-streaming instead of hanging indefinitely

But the env var page still describes stalled-stream protection as an opt-in watchdog with a 90-second default and says non-streaming fallback applies when a streaming request fails mid-stream.

That leaves the current docs outdated or unclear on the user-visible behavior after v2.1.105:

### A. Default behavior is unclear

The docs imply stalled streams still hang indefinitely unless `CLAUDE_ENABLE_STREAM_WATCHDOG=1` is set.

### B. The timeout value is unclear

The docs say the default idle threshold is 90 seconds, while the changelog says stalled streams now abort after 5 minutes of no data.

### C. Fallback interaction is unclear

The docs do not explain whether `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=1` disables this new stalled-stream recovery path, or only the older mid-stream failure fallback.

### Suggested Improvement


Update `env-vars` to explain the post-v2.1.105 behavior explicitly:

- State whether the 5-minute no-data abort + non-streaming retry is now the default behavior
- Clarify how `CLAUDE_ENABLE_STREAM_WATCHDOG` and `CLAUDE_STREAM_IDLE_TIMEOUT_MS` interact with that default
- Clarify whether `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=1` disables the retry path after a stalled stream
- Distinguish idle no-data handling from other request timeouts so users know which knob applies to which failure mode

### Impact

Medium - Makes feature difficult to understand

### Additional Context


**Affected Pages:**

| Page | Context |
|------|---------|
| https://code.claude.com/docs/en/env-vars | Primary documentation for the stalled-stream watchdog and non-streaming fallback behavior |

**Total scope:** 1 page affected

**Source:** Changelog v2.1.105

**Exact changelog entry:** Improved stalled API stream handling: streams now abort after 5 minutes of no data and retry non-streaming instead of hanging indefinitely

# Comments on anthropics/claude-code#47623
Total: 2 comments

--- Comment 1 ---
Author: coygeek
Date: 2026-05-11T04:36:29Z

Just checked the current docs again. This issue is not fully resolved yet.

--- Comment 2 ---
Author: coygeek
Date: 2026-05-28T22:38:56Z

Still relevant as of 2026-05-28. I checked the current docs and this documentation gap still appears unresolved.

---

### Issue #45534 — [BUG] Claude Code VSCode extension is NOT streaming response since 2.1.37

State: OPEN | #45534
Labels: bug, platform:vscode, regression, platform:wsl


---



### What's Wrong?

There're already multiple posts about this and they're all automatically closed -- since 2.1.37, how is this not something drawing enough attention? Is everyone enjoying the huge dump of response at the very end? 
Where did the streaming go(just like claude.ai and every other LLM interaction is like?)????
Where did it go and WHO decided it's a good idea to dump the huge blob of text at the very end?

I'm on Win11 WSL2, 2.1.37 is what keeps me going right now, all the newer versions just keep dumping all response once it's done. 

Please bring it back!!

### What Should Happen?

The response should present in a progressive way including the thinking process, just like claude.ai

### Error Messages/Logs

```shell
N/A
```

### Steps to Reproduce

1. be on win11
2. be on wsl2
3. install claude code vscode extension in vscode or cursor
4. use it
5. experience no-stream response

### Claude Model

Opus

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

2.1.37

### Claude Code Version

2.1.97

### Platform

Other

### Operating System

Windows

### Terminal/Shell

WSL (Windows Subsystem for Linux)

### Additional Information

_No response_

# Comments on anthropics/claude-code#45534
Total: 6 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-04-09T02:03:31Z

Found 1 possible duplicate issue:

1. https://github.com/anthropics/claude-code/issues/27245

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: bisbaldk
Date: 2026-04-09T02:05:02Z

> Found 1 possible duplicate issue:
> 
>     1. [[BUG] **VSCode-Ext-Streaming not working - text appears all at once after ~20 seconds-** #27245](https://github.com/anthropics/claude-code/issues/27245)
> 
> 
> This issue will be automatically closed as a duplicate in 3 days.
> 
>     * If your issue is a duplicate, please close it and 👍 the existing issue instead
> 
>     * To prevent auto-closure, add a comment or 👎 this comment
> 
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)

“Found a duplicate", literally a closed duplicate no one engaged with, bad bot.

--- Comment 3 ---
Author: bisbaldk
Date: 2026-04-18T01:51:44Z

hello? anyone seeing this post? 

--- Comment 4 ---
Author: jncrenshaw
Date: 2026-04-30T20:18:33Z

I too am suffering this and Anthropic's aggressive ticket closing using bots is EXTREMELY frustrating for trying to find any information on this. Marking every complaint about this as a duplicate and auto-closing them does nothing for the community and makes it nearly impossible to have a constructive conversation about the issue.

Keep your bots out of the issues threads. They aren't helpful. They're like overzealous, BAD community moderators.

Maybe prioritize fixing issues over closing issues?

Instead you just auto-close all issues that don't get a response within 7 days.

If you're going to ruin your application with untested AI slop, at least let us have a bot free conversation about how your slop is impacting us.

There's no way in hell any human being tested your changes and thought to themselves "this is an improvement".

Streaming tokens so that the human can start reading sooner is like AI Applications 101!

--- Comment 5 ---
Author: Deleeete
Date: 2026-05-07T22:50:07Z

Tested on my machine and this solution resolve it.

20260510 Edited: Adjusted the fix so it works across different JS minifier results for different extension version.

---

## The (DIY) Fix

```bash
#  First, locate the extension directory and back up the original file:
cd ~/.vscode-server/extensions

# Find the latest installed version
EXT_DIR=$(ls -d anthropic.claude-code-*/ | sort -V | tail -1)
echo "Found: $EXT_DIR"

# Backup
cp "$EXT_DIR/extension.js" "$EXT_DIR/extension.js.backup"

# Then apply the one-character patch:
sed -i 's/includePartialMessages:![A-Za-z0-9]*\.env\.remoteName/includePartialMessages:!0/' "$EXT_DIR/extension.js"

# Verify the replacement took effect:
grep -c 'includePartialMessages:!0' "$EXT_DIR/extension.js"
# → 1
grep -c 'includePartialMessages:![A-Za-z0-9]*\.env\.remoteName' "$EXT_DIR/extension.js"
# → 0
```

Finally, reload the VS Code window (`Ctrl+Shift+P` → `Developer: Reload Window`) and start a new conversation in Claude Code. Newly spawned Claude processes will now include `--include-partial-messages` in their args.

To revert:

```bash
mv "$EXT_DIR/extension.js.backup" "$EXT_DIR/extension.js"
```

---

## Why this happens

The extension's `spawnClaude` method sets `includePartialMessages:!<var>.env.remoteName` (the minified variable name varies per build, e.g. `G4`, `O0`). In WSL2, `.env.remoteName` evaluates to `"wsl"` (truthy), so the expression becomes `false`, and `--include-partial-messages` is never passed to the Claude CLI process. Without that flag, the CLI only emits complete assistant content blocks — no incremental `content_block_delta` events reach the webview, so all text appears at once.

The data path in normal operation is: Claude CLI stdout (`stream-json`) → extension host pipe → `QK` line-delimited JSON decoder → `kO` async iterator → `for await` loop in `launchClaude` → `webview.postMessage({type:"from-extension"})` → webview `readMessages` → `processStreamEvent` handles `content_block_delta` events for incremental rendering. The single flag `--include-partial-messages` controls whether the first step produces deltas or only complete blocks.

All versions from 2.1.131 through 2.1.138 are affected. The fix is safe: the extension already uses the same `stream-json` format and `postMessage` transport regardless of environment — the flag only gates emission granularity at the CLI level, not the transport mechanism.

---

## Credits and Notes

 - This analysis and solution was completed by `DeepSeek V4 Pro` in the `Claude Code environment`.
 - AI's Methodology: extracted the minified extension.js from `.vscode-server/extensions/`, traced the `spawnClaude` → `spawnLocalProcess` → CLI flag assembly chain via grep/context extraction, and cross-checked with live process args from `ps`.
 - Update the extension may overwrite the fix (if they won't fix it in that incoming update). Re-run the DIY fix will be required then.


--- Comment 6 ---
Author: 2234839
Date: 2026-05-15T05:00:22Z

@Deleeete  very thank，this is good

---

### Issue #62973 — [FEATURE] Support for Strict Enterprise APIM Gateways (Custom Paths, Payload Injection, SSE Fallbacks)

State: OPEN | #62973
Labels: enhancement, api:bedrock, area:networking

---



### Problem Statement

Working workaround (proxy) https://github.com/SamuelMarks/claude-apim-proxy ; can CC0 license it for you just ask.

We are currently deploying Claude Code in an enterprise environment (Stanford University) that routes Anthropic Bedrock traffic through a strict API Management (APIM) gateway.

While the recent addition of `CLAUDE_CODE_USE_BEDROCK=1` and `ANTHROPIC_CUSTOM_HEADERS` is a massive step forward, Claude Code still cannot natively connect to our APIM gateway. We are currently forced to run a local proxy middleware to rewrite Claude Code's outgoing requests. 

Specific issues with strict enterprise gateways include:
1. **Advanced Gateway Routing / Exact Endpoints**: `ANTHROPIC_BASE_URL` unconditionally appends `/v1/messages`. Many enterprise gateways route to specific base paths (e.g., `/awssig4claude37/aswsig4claude37`) and will return a `404` if `/v1/messages` is appended.
2. **Custom JSON Payload Injection**: Our gateway requires custom top-level keys to be present in the JSON body (e.g., `prompt_text: "proxy bypass"`) for auditing and routing purposes.
3. **Graceful Non-Streaming Fallback**: Some enterprise security gateways aggressively block chunked streaming responses (`stream: true`). When this happens, Claude Code crashes or hangs.
4. **Strict Bedrock Payload Sanitization**: Bedrock via strict APIM gateways will violently reject payloads with a `400 Bad Request` if they do not perfectly adhere to Bedrock's strict, undocumented schema limits.

### Proposed Solution

We propose a set of features that would allow Claude Code to natively support strict enterprise API gateways:

1. **Exact Endpoints Variable**: Provide an environment variable like `ANTHROPIC_EXACT_ENDPOINT="https://apim.corp.com/specific/path"`. If set, the HTTP client uses this exact URL without appending any standard paths. (Alternatively, `ANTHROPIC_OMIT_PATH=1`).
2. **Payload Injection Variable**: Introduce a new environment variable: `ANTHROPIC_CUSTOM_PAYLOAD_INJECT='{"prompt_text": "proxy bypass"}'`. The network client would deeply merge this object into the root of the outgoing Anthropic API payload before it is sent.
3. **Internal SSE Faking / Disable Streaming**: If a streaming request fails (e.g., due to specific HTTP error codes or timeouts related to chunked encoding), Claude Code should gracefully fall back to a blocking (non-streaming) request. Once the full response is received, the internal client can simulate the SSE events so the UI stream processor doesn't need to be rewritten. Add a toggle like `CLAUDE_CODE_DISABLE_STREAMING=1` to force this behavior immediately.
4. **Built-in Bedrock Sanitization**: When `CLAUDE_CODE_USE_BEDROCK=1` is set, apply a pre-flight payload sanitizer:
    * Ensure a maximum of 4 `cache_control` blocks per request (stripping older ones).
    * Enforce that `tool_use` blocks are strictly at the *end* of the assistant's content array.
    * Enforce that `tool_result` blocks are strictly at the *beginning* of the user's content array.
    * Strip empty `thinking` blocks from assistant messages, as these cause immediate gateway rejections.

### Alternative Solutions

* **Local Proxy Middleware**: We are currently forced to run a local proxy middleware to rewrite Claude Code's outgoing requests. This adds complexity and friction to enterprise onboarding, as users have to install and run background services.
* **Network/Gateway Adjustments**: Modifying the strict APIM gateways to accept standard requests is generally not possible in strict enterprise environments like Stanford without extensive architectural exceptions.

### Priority

Critical - Blocking my work

### Feature Category

CLI commands and flags

### Use Case Example

An enterprise user wants to connect to Bedrock through their strict APIM gateway. They can set the following environment variables:

```bash
export CLAUDE_CODE_USE_BEDROCK=1
export ANTHROPIC_EXACT_ENDPOINT="https://apim.corp.com/awssig4claude37/aswsig4claude37"
export ANTHROPIC_CUSTOM_PAYLOAD_INJECT='{"prompt_text": "proxy bypass"}'
export CLAUDE_CODE_DISABLE_STREAMING=1

claude
```
With these set, Claude Code can natively bypass proxy restrictions, successfully route without `/v1/messages` being appended, inject required audit keys, and fallback to non-streaming requests, providing a seamless user experience.

### Additional Context

Enterprise adoption of Claude Code is heavily bottlenecked by complex corporate networking setups (Zscaler, custom APIMs, VPN routing conflicts). Allowing Claude Code to dynamically adjust its network footprint without requiring users to build and run local Python proxies would significantly ease enterprise onboarding.

**Reference Implementation:** For context, the code in https://github.com/SamuelMarks/claude-apim-proxy serves as our current local proxy middleware. It implements the exact workarounds described above (payload sanitization, SSE faking, custom payload injection, and path overriding) and can be used as a reference implementation to learn from when natively integrating these features into Claude Code.

Thank you for considering these additions!

# Comments on anthropics/claude-code#62973
Total: 0 comments

No comments on this issue.

---

### Issue #62599 — [BUG] iOS Dispatch Streaming Input Mode (orange bubbles) replaced by banner UI after app update 1.260521.0

State: OPEN | #62599
Labels: bug, platform:ios, area:ui

---



### What's Wrong?

After updating Claude iOS app to version 1.260521.0 (released 2026-05-26), the Dispatch "Streaming Input Mode" (orange chat bubble UI) no longer works.

It has been replaced by a persistent banner/header UI at the top of the screen. I must now wait for each response before sending the next message — cannot queue multiple messages.

Affects 2 different iPhones. Tried toggling Threads, full re-pair, clearing bridge-state.json, and changing ccRemoteControlDefaultEnabled — none worked.

### What Should Happen?

Messages should appear as orange chat bubbles in Dispatch (Streaming Input Mode). Multiple messages should be queueable without waiting for each response, as was the behavior before the 1.260521.0 update.


### Error Messages/Logs

```shell

```

### Steps to Reproduce

1. Update Claude iOS app to version 1.260521.0 (2026-05-26 update)
2. Ensure Claude Desktop is running on macOS with Dispatch enabled
3. Open Claude iOS app → Dispatch tab
4. Send any message
5. Observe: banner/header UI appears instead of orange bubble streaming mode
6. Observe: must wait for full response before sending next message

### Claude Model

Opus

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

_No response_

### Claude Code Version

Claude Code

### Platform

Anthropic API

### Operating System

Other

### Terminal/Shell

Other

### Additional Information

_No response_

# Comments on anthropics/claude-code#62599
Total: 0 comments

No comments on this issue.

---

### Issue #52151 — Opus 4.7 1M via Bedrock: VSCode extension stream ends with 0 events; fallback renders as "Unhandled case: [object Object]"

State: OPEN | #52151
Labels: bug, api:bedrock, platform:macos, platform:vscode


---

### Environment
- Claude Code VSCode extension: `2.1.114.c47`
- Model: `global.anthropic.claude-opus-4-7` (1M context profile) via AWS Bedrock
- Platform: macOS (Darwin 25.3.0)
- CLI works fine on the same account/model; this only reproduces in the VSCode GUI

### Symptom
After a number of turns with tool use (`message_count: 556` in the failing session), the assistant stops responding. GUI shows:

> **Unhandled case: [object Object]**
> <img width="589" height="68" alt="Image" src="https://github.com/user-attachments/assets/b27c051a-5aca-46df-9cf8-a05d0ab90367" />

### Logs
Streaming request opens, Bedrock closes it with zero events:

```
[DEBUG] [API REQUEST] /model/global.anthropic.claude-opus-4-7/invoke-with-response-stream source=sdk
[DEBUG] Stream started - received first chunk
sdk_stream_ended_no_result { had_error: true, message_count: 556 }
[ERROR] Stream completed without receiving message_start event - triggering non-streaming fallback
[ERROR] Error streaming, falling back to non-streaming mode: Stream ended without receiving any events
```

Non-streaming fallback fires and also fails — the resulting error is passed to the UI error handler which stringifies it as `[object Object]`.

### Repro
1. Bedrock account with 1M context access on `global.anthropic.claude-opus-4-7`
2. Long session (hundreds of turns) using deferred tools (TaskCreate/TaskUpdate/TaskList)
3. Eventually the stream closes with 0 events and the fallback dies

# Comments on anthropics/claude-code#52151
Total: 30 comments

--- Comment 1 ---
Author: kaelannet
Date: 2026-04-24T13:54:51Z

I am also seeing this issue using Claude Code via Bedrock

--- Comment 2 ---
Author: pllanos-entropy
Date: 2026-04-24T16:32:57Z

I have the same issue:
Claude Code v2.1.117
API provider: Amazon Bedrock
Model: global.anthropic.claude-opus-4-7[1m] 

--- Comment 3 ---
Author: pllanos-entropy
Date: 2026-04-25T19:27:56Z

**Adding to the frustration of this extremely annoying bug:**

When this `Unhandled case: [object Object]` error occurs, if you close Claude Code and reopen the session, **the UI truncates the entire conversation back to the moment the error happened** — everything you did *after* the error simply vanishes from the interface.

The really painful part: the `.jsonl` session file on disk still contains the full history. All the messages, tool calls, edits, and reads that happened after the error are persisted correctly. But on reload:

- The UI only renders messages up to the error.
- The agent running inside the resumed session also loses all the post-error context.

So if you decided to push through the error and keep working (which is often the only practical choice mid-task), you effectively lose all that progress from the agent's perspective the moment you restart. The data is right there in the JSONL — the UI/agent just refuses to load past the error boundary.

This turns a recoverable hiccup into a hard context wipe, and it makes long planning/implementation sessions (like the one in the screenshots, where significant work was done after the error) extremely risky to resume.

--- Comment 4 ---
Author: aumanjoa
Date: 2026-04-26T08:07:29Z

Reproducing on **extension 2.1.120** (current latest as of 2026-04-26) on Darwin 25.4.0 with model `global.anthropic.claude-opus-4-7[1m]`. Happens frequently in long tool-heavy sessions.

Quick diagnosis by grepping the shipped extension:

```
~/.vscode/extensions/anthropic.claude-code-2.1.120-darwin-arm64/webview/index.js
```

The message is thrown from function `XB1` inside a switch over stream event types:

```js
case "compaction_delta": break;
default: XB1(J)
// ...
function XB1($, Z){ throw Error(Z ?? `Unhandled case: ${$}`) }
```

Two problems:

1. **Non-forward-compatible switch**: the `default` branch throws on any unknown event type instead of no-oping. Any new stream event the server introduces (or any event that survives the `sdk_stream_ended_no_result` fallback path in a shape the switch doesn't recognise) crashes the webview handler.
2. **Error message loses all info**: `${$}` stringifies the event object as `[object Object]`, so the notification is uninformative. Should be `JSON.stringify($)` at minimum, ideally with the event type extracted.

Suggested fix: the default branch should log-and-ignore (with the full event JSON) rather than throw. That preserves forward compatibility when new event types land, and when a genuine bug does occur the notification actually tells you what event was unhandled.

Still repros on 2.1.120 — bumping so it's visible against the latest release.

--- Comment 5 ---
Author: galmacky
Date: 2026-05-05T18:40:04Z

i'm running into the same issue. basically i cannot use opus 4.7 with bedrock at the moment.

--- Comment 6 ---
Author: pengzhenghao
Date: 2026-05-05T21:29:27Z

This bug is super annoying and i have to type multiple times "please continue" in VS code extension. That's crazy.

--- Comment 7 ---
Author: andmanea
Date: 2026-05-06T12:22:19Z

Still reproducing on v2.1.131

--- Comment 8 ---
Author: shrey-essen
Date: 2026-05-06T17:32:00Z

Same issue persisting with AWS Bedrock Opus 4.7 on Cursor v3.3.12

--- Comment 9 ---
Author: klatu201
Date: 2026-05-07T04:19:20Z

Reproducing on **`2.1.128.b51`** (VSCode stable, macOS 15.x arm64, Bedrock `us.anthropic.claude-opus-4-7` 1M context). Adding one data point for this specific bundle and notes from a local patch test.

### Confirmation on 2.1.128

Same symptom and same log trail as the OP. In one day on a normal-sized project I saw **11 `sdk_stream_ended_no_result` events with `had_error: true`**, each paired with `Stream completed without receiving message_start event - triggering non-streaming fallback`. Context at failure was not the culprit (~242K tokens, effectiveWindow=980000).

The throw function is still there in 2.1.128 — same shape as @aumanjoa found in 2.1.120, just with a different mangled name (`GB1` instead of `XB1`). Two call sites, both in `webview/index.js`:

1. `QB1.processStreamEvent` — `default: GB1($)` after the six known `message_*` / `content_block_*` cases.
2. `b20` (content-block-delta dispatcher) — `default: GB1(J)` after `text_delta`, `citations_delta`, `input_json_delta`, `thinking_delta`, `signature_delta`, `compaction_delta`.

### Local patch test (confirms diagnosis)

I replaced the `GB1` body from

```js
function GB1($, Z) { throw Error(Z ?? `Unhandled case: ${$}`); }
```

to

```js
function GB1($, Z) {
  try { console.warn("[patched-local] Unhandled case:", $, Z); } catch (e) {}
  return;
}
```

After reloading the VSCode window:

- **Red toast no longer appears.**
- **Session no longer freezes** — the non-streaming fallback produces its result and the UI continues rendering normally.
- Underlying Bedrock stream-drops still happen at the same rate; the patch only masks the UI consequences.
- A warning lands in the webview devtools console when it happens (useful for counting occurrences).

So both behaviors the community has asked for are achievable with a one-function change:

- Forward-compat default branch (log-and-continue instead of throw).
- Preserve the information if it ever *does* matter — `JSON.stringify(value)` or `value?.type ?? "unknown"` in the message, per @aumanjoa's suggestion.

### Extra observation

@pllanos-entropy's note about the `.jsonl` file keeping full history while the UI truncates to the error point is confirmed on my side too. When a session froze mid-tool-dispatch, the disk session had another ~40 messages past the UI boundary on reload — so the lost-context cost is even higher than the toast suggests.



--- Comment 10 ---
Author: azatoth
Date: 2026-05-07T09:22:22Z

Seeing the same issue since yesterday on the VSCode extension.

Environment:

Claude Code: 2.1.132
VSCode extension: anthropic.claude-code 2.1.132
Model: global.anthropic.claude-opus-4-7[1m]
Provider: AWS Bedrock
OS: Linux 6.8.0-111-generic (Ubuntu)
Crash occurs irregularly and at one time it occurred during the first interaction in a session. Same "Unhandled case: [object Object]" error text.



--- Comment 11 ---
Author: klatu201
Date: 2026-05-08T15:19:05Z

For anyone wanting to mitigate locally while this is fixed upstream — here's a version-agnostic patch script that works across 2.1.120 / 2.1.128 / 2.1.131 / 2.1.132 and should survive through whatever the next minified function name is. macOS and Linux covered; Cursor users just point `EXT_ROOT` at their own extensions dir.

### Patch (run once, then Reload Window)

```bash
#!/usr/bin/env bash
# claude-code-unhandled-case-patch.sh
set -euo pipefail

# Adjust if you use Cursor, VSCode Insiders, etc.
EXT_ROOT="${EXT_ROOT:-$HOME/.vscode/extensions}"

EXT_DIR=$(ls -dt "$EXT_ROOT"/anthropic.claude-code-* 2>/dev/null | head -1 || true)
if [ -z "$EXT_DIR" ]; then
  echo "ERROR: no anthropic.claude-code-* extension found under $EXT_ROOT" >&2
  exit 1
fi
TARGET="$EXT_DIR/webview/index.js"
BACKUP="$TARGET.backup"

[ -f "$TARGET" ] || { echo "ERROR: $TARGET not found"; exit 1; }
[ -f "$BACKUP" ] || cp "$TARGET" "$BACKUP"

python3 - "$TARGET" <<'PY'
import re, sys
path = sys.argv[1]
src = open(path).read()

if "[cc-unhandled-case-patch]" in src:
    print(f"already patched: {path}")
    sys.exit(0)

pattern = r'function (\w+)\(\$,Z\)\{throw Error\(Z\?\?`Unhandled case: \$\{\$\}`\)\}'
def repl(m):
    fn = m.group(1)
    return (f'function {fn}($,Z){{try{{console.warn("[cc-unhandled-case-patch]",'
            f'$?.type??$,$,Z)}}catch(e){{}}return}}')
new, n = re.subn(pattern, repl, src)
if n == 0:
    print("ERROR: throw signature not found — minified names may have changed. "
          "Grep for `Unhandled case` in the bundle and adapt the pattern.",
          file=sys.stderr)
    sys.exit(2)
open(path, "w").write(new)
print(f"patched {n} site(s) in {path}")
PY

echo
echo "Done. Now run '⌘⇧P → Developer: Reload Window' for EACH open VSCode window."
echo "  Extension dir : $EXT_DIR"
echo "  Backup file   : $BACKUP"
```

### Revert

```bash
EXT_DIR=$(ls -dt "$HOME/.vscode/extensions"/anthropic.claude-code-* | head -1)
cp "$EXT_DIR/webview/index.js.backup" "$EXT_DIR/webview/index.js"
# Then Reload Window
```

### What it does (and does not) fix

- **Fixes:** the `Unhandled case: [object Object]` red toast and the session freeze that comes with it. Tested on 2.1.128; regex is generic to the minified signature so it should match current-gen builds until Anthropic refactors the function.
- **Does not fix:** the underlying Bedrock stream drops (they still happen; the non-streaming fallback handles them silently after the patch).
- **Does not fix:** the "UI truncates to error point on reload" data-loss issue @pllanos-entropy flagged — that's a separate bug.

### Caveats

- **Extension auto-updates will wipe it.** The script is idempotent and safe to re-run after each update; if the function signature changes the patch will fail loudly rather than corrupt the bundle.
- **Cursor / other VSCode forks:** set `EXT_ROOT` to that editor's extensions directory (e.g. `~/.cursor/extensions`).
- **Linux:** same path assumptions; no platform-specific code.
- This is a workaround for the symptom, not a replacement for Anthropic's fix. Paste it only if you're comfortable modifying a local extension file.


--- Comment 12 ---
Author: YoutubeOfficer
Date: 2026-05-14T00:51:05Z

Version **2.1.141** continues to experience persistent issues.

--- Comment 13 ---
Author: sorvani
Date: 2026-05-14T03:45:37Z

VS Code Extension 2.1.141. Super annoying.

<img width="240" height="199" alt="Image" src="https://github.com/user-attachments/assets/40d737ca-d4ba-48c7-96fb-e1322d6b6208" />

<img width="692" height="170" alt="Image" src="https://github.com/user-attachments/assets/36c63f9f-9a80-440f-83c1-3ce6d04013ab" />

--- Comment 14 ---
Author: toovyaS
Date: 2026-05-14T04:54:02Z

I have the same issue 

--- Comment 15 ---
Author: brentarcane
Date: 2026-05-14T05:18:24Z

This issue is occurring using Claude directly without Bedrock too.

--- Comment 16 ---
Author: AwinHuang
Date: 2026-05-14T05:59:16Z

Have the same issue.
VSCODE:
```
Version: 1.120.0 (user setup)
Commit: 0958016b2af9f09bb4257e0df4a95e2f90590f9f
Date: 2026-05-12T20:17:22Z
Electron: 39.8.8
ElectronBuildId: 13870025
Chromium: 142.0.7444.265
Node.js: 22.22.1
V8: 14.2.231.22-electron.0
OS: Windows_NT x64 10.0.26200
```

Claude Code for VS Code:
```
Identifier: anthropic.claude-code
Version: 2.1.141
Last Updated: 2 hours ago
Size: 226.77MB
```


--- Comment 17 ---
Author: Antiklesys
Date: 2026-05-14T06:04:26Z

This is an issue with VS Code Extension Version: 2.1.141.
I downgraded to VS Code Extension Version: 2.1.140 and restarted VS Code (unchecked auto update in the extension) and it works again for me. Still testing but try downgrading.

**The fix is to: go in VSCode Claude Code Extension, Downgrade it to 2.1.140, uncheck auto update the extension and restart VS Code.**

--- Comment 18 ---
Author: sperokubo
Date: 2026-05-14T07:01:50Z

Same issue: 
Claude Code for VSCODE
Version: 2.1.141

--- Comment 19 ---
Author: Mr-KIDBK
Date: 2026-05-14T07:31:42Z

Same issue:
Claude Code for VSCODE
Version: 2.1.141

--- Comment 20 ---
Author: goneale
Date: 2026-05-14T08:04:46Z

Come on team we need this fixed. I'm on Claude Code Max and can't have these trivial errors
V2.1.141

<img width="345" height="73" alt="Image" src="https://github.com/user-attachments/assets/90798b3a-358c-44d4-99b6-580a82573777" />

--- Comment 21 ---
Author: Fl0rencess720
Date: 2026-05-14T08:45:38Z

Same issue:
Claude Code for VSCODE
Version: 2.1.141

--- Comment 22 ---
Author: yevhenlisovenko
Date: 2026-05-14T08:48:44Z

same. how to fix that?

--- Comment 23 ---
Author: ziago
Date: 2026-05-14T08:50:26Z

Experiencing the same error here
claude code 2.1.141

--- Comment 24 ---
Author: Antiklesys
Date: 2026-05-14T08:50:50Z

@ziago @yevhenlisovenko @Fl0rencess720 @goneale @Mr-KIDBK @sperokubo check my comment: https://github.com/anthropics/claude-code/issues/52151#issuecomment-4448083216

The fix is to: go in VSCode Claude Code Extension, Downgrade it to 2.1.140, uncheck auto update the extension and restart VS Code.

--- Comment 25 ---
Author: jeepen783
Date: 2026-05-14T09:13:22Z

Same issue:
Claude Code for VSCODE
Version: 2.1.141

--- Comment 26 ---
Author: georgeblck
Date: 2026-05-14T09:29:01Z

The fix works also when downgrading to 2.1.139



--- Comment 27 ---
Author: ahmedelakkad
Date: 2026-05-14T09:39:17Z

Same issue

--- Comment 28 ---
Author: neoDD69
Date: 2026-05-14T11:38:05Z

Same `Unhandled case: [object Object]` UI error, but with a **different repro than OP** — worth flagging since it's not a long-session issue here.

**Env**: VS Code extension 2.1.141, Windows 11, OAuth (claude.ai), model `claude-opus-4-7[1m]` with `claude-haiku-4-5` sub-agents. No VPN/proxy.

**Repro**: brand-new sessions, fails within the first few turns (`message_count` ~100–125, not 556).

**Log pattern** — streaming stalls *after* the first chunk:

- `[DEBUG] Stream started - received first chunk`
- `[WARN] [Stall] stream_idle_partial lastChunkAgeMs=15000 bytesTotal=702`
- `[WARN] Streaming stall detected: 39.7s gap between events`
- `[INFO] sdk_stream_ended_no_result {"had_error":true,"message_count":125}`

Often correlated with a malformed tool-input from the `Explore` sub-agent right before the stall:

- `[ERROR] SyntaxError: JSON Parse error: Unexpected token '.'`
- `[DEBUG] Read tool input error: required parameter ​`file_path​` is missing`

Repros more often when a turn dispatches `Explore` (many parallel Glob/Grep/Read via Haiku). Load-correlated, not deterministic — retry sometimes works.

**UI fix suggestion regardless of root cause**: stringify the fallback error properly (`error?.message ?? error?.toString()`) so users see something actionable instead of `[object Object]`.


--- Comment 29 ---
Author: iamhere2
Date: 2026-05-14T11:54:15Z

Since today, I have the same looking error on Windows 11, Sonnet 4.6 or Opus 4.7), direct API (not Bedrock), session of ~70 turns


--- Comment 30 ---
Author: PopSonny
Date: 2026-05-14T13:01:11Z

Same thing, from VSCode addon, just from today onward I kept getting this error.

---

### Issue #57819 — [Bug fix + FR] Non-streaming fallback writes bundled multi-block records; webview drops thinking/text preamble

State: OPEN | #57819
Labels: bug, has repro, area:core, area:ui

---

## Summary

Claude Code has two paths that produce a different on-disk shape for the same logical assistant turn:

- **Streaming path** (`src/services/api/claude.ts:2171-2210`) yields one `AssistantMessage` per `content_block_stop`, each with a fresh `randomUUID()`. The transcript ends up with one content block per JSONL record.
- **Non-streaming fallback** (`claude.ts:2571-2594`, also `2668+` for the 404-on-stream-creation branch) wraps the entire `BetaMessage` (i.e. the whole `content` array) into a **single** `AssistantMessage` with one uuid. No per-block split.

The webview assembler is built around the streaming-path invariant (one record = one content block = one row). When it sees a fallback record with N content blocks, it renders **only the last block** under a synthesized uuid suffix `-00000000000<N>` and silently drops the earlier blocks, typically the `thinking` and the `text` preamble that announces what the upcoming tool call will do.

For tool calls with side effects, this means the model's stated intent for the tool call is erased from the chat history.

## Empirical observation

Caught one in the wild. Across a 17,501-line session JSONL (7,943 assistant records), exactly **one** record has multiple content blocks: line 17437 with `[thinking, text, tool_use]`. Across every other session JSONL on disk, zero. The 1,222 normal `text` then `tool_use` preamble pairs in the same session are split into separate records as expected.

Disk record (single uuid, three blocks):
```jsonl
{"uuid":"9e191a76-…-3ce45db6c23e","type":"assistant","message":{"id":"msg_01PywtpHEMoHeU64kcbQhB2o","content":[
  {"type":"thinking","thinking":" Everything's down, so I need to restart all three services.","signature":"…"},
  {"type":"text","text":"All down. Bringing them up:"},
  {"type":"tool_use","id":"toolu_01WvRHhmUGo6K97PuDxUuevf","name":"Bash","input":{"command":"fuser -k 7799/tcp …"}}
]},…}
```

Webview-side `messages` signal (read via React fiber walk to the manager to `entry.messages.peek()`): only one row with uuid `9e191a76-a935-4f66-bebb-000000000002` containing the `tool_use` block. No siblings with `-000000000000` or `-000000000001`. The rendered chat jumps straight from the prior tool_result to the new tool_use card with no narration in between.

The user caught the brief streaming render of all three blocks in the panel for ~one frame (the live-streaming path renders into Preact state on every delta) before the next re-derivation wiped them. Without sub-second visual attention there is no signal anything was lost.

## Root cause with citations (leaked source)

Streaming path produces per-block records, `claude.ts:2171-2210`:
```ts
case 'content_block_stop': {
  …
  const m: AssistantMessage = {
    message: {
      ...partialMessage,
      content: normalizeContentFromAPI([contentBlock] as BetaContentBlock[], tools, options.agentId),
    },
    requestId: streamRequestId ?? undefined,
    type: 'assistant',
    uuid: randomUUID(),
    timestamp: new Date().toISOString(),
    …
  }
  newMessages.push(m); yield m
}
```

The 100ms-lazy serialization comment confirms the design intent, `claude.ts:2236-2241`:
```
IMPORTANT: Use direct property mutation, not object replacement.
The transcript write queue holds a reference to message.message
and serializes it lazily (100ms flush interval). Object
replacement ({ ...lastMsg.message, usage }) would disconnect
the queued reference; direct mutation ensures the transcript
captures the final values.
```

And `QueryEngine.ts:718-731`:
```
// Fire-and-forget for assistant messages. claude.ts yields one
// assistant message per content block, then mutates the last
// one's message.usage/stop_reason on message_delta, relying on
// the write queue's 100ms lazy jsonStringify.
```

Non-streaming fallback bundles all blocks, `claude.ts:2571-2594`:
```ts
const result = yield* executeNonStreamingRequest(…)
const m: AssistantMessage = {
  message: {
    ...result,
    content: normalizeContentFromAPI(result.content, tools, options.agentId),  // whole array, no split
  },
  requestId: streamRequestId ?? undefined,
  type: 'assistant',
  uuid: randomUUID(),
  …
}
newMessages.push(m); yield m
```

(The 404-on-stream-creation branch at 2668+ does the same thing.)

Triggers for the fallback (`claude.ts:2342-2354`, 2469-2532, 2598-2666):
- stream idle-timeout watchdog fires
- stream completed without `message_start`
- stream had `message_start` but no completed content blocks
- 404 on stream creation
- any other thrown streaming error not gated by `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK` env or the `tengu_disable_streaming_to_non_streaming_fallback` feature flag

The cli emits `tengu_streaming_fallback_to_non_streaming` on the trigger and `tengu_nonstreaming_fallback_started` when the call begins.

## Impact

For a tool call whose `text` block describes the model's intent (e.g. "All down. Bringing them up:" before a `fuser -k` Bash that kills three local services), the user loses:

1. The model's stated intent for the tool call. This is the line that lets the user verify the tool input matches what the model said it was going to do; particularly important for destructive Bash, file writes, network calls, anything with side effects.
2. The reasoning chain (`thinking` block + signature). Beyond the visible loss, the dropped signature breaks any future flow that needs to verify the chain (extended thinking re-fork, tool-use audit).
3. UX coherence. The chat jumps from a tool_result to a fresh tool_use card with no transition.

Incidence per turn is low (the fallback is rare in normal use), but the failure is silent and irrecoverable from the user's seat: disk has the data, the renderer can't see it, and there is no warning.

## Proposed fix: write side

The splitter already exists and is already used elsewhere. `normalizeMessages` (`src/utils/messages.ts:731`) splits a multi-block assistant message into per-block messages using `deriveUUID(message.uuid, index)` (`messages.ts:725`, with the `isNewChain` cascade for chained re-derivation). `normalizeMessage` (`src/utils/queryHelpers.ts:102`) wraps it as a generator that's already called in `QueryEngine.ts:769`/`782`/`786` to emit per-block SDK output. The streaming path in `claude.ts:2171-2210` doesn't need it because `content_block_stop` already yields per-block. The non-streaming fallback at `claude.ts:2571-2594` and `2668+` is the only emitter that bypasses the per-block contract, and that's the surface that lacks the call.

Apply `normalizeMessages` at the non-streaming yield site:

```ts
const result = yield* executeNonStreamingRequest(…)
const bundled: AssistantMessage = {
  message: { ...result, content: normalizeContentFromAPI(result.content, tools, options.agentId) },
  requestId: streamRequestId ?? undefined,
  type: 'assistant',
  uuid: randomUUID(),
  timestamp: new Date().toISOString(),
  …
}
for (const m of normalizeMessages([bundled])) {
  newMessages.push(m); yield m
}
```

Or, equivalently, apply normalization in `QueryEngine.ts` before `messages.push(message)` so all assistant messages are normalized regardless of source: slightly more invasive but a single source of truth for the contract. Either restores the per-record-equals-per-block invariant the rest of the system depends on, without touching downstream readers.

## Proposed fix: read side (independently necessary)

A read-side mitigation is not optional cleanup; it is the only path to recover sessions **already on disk**.

- Multi-block fallback records have been getting written for as long as the fallback has existed and the streaming path has split per-block. They are present in deployed JSONLs. The user has no way to know which sessions are affected; by definition, the only signal would have been the dropped preamble that's already gone.
- Once written, a multi-block record can't be split after the fact in a way that any chain walker would accept. The cli has no rewrite-safe path: re-emitting as N records would mint new uuids, breaking any descendant `parentUuid` chain that already references the bundled record's uuid (and any ingress / sibling-fork mirror that has it cached). So the disk record stays multi-block forever.
- Future write-side regressions (or a missed branch) would also be invisible without a read-side check. Same argument as in #55818 for compact-boundary lpu: silent truncation of perceived chat content is the worst possible UX, and detection at read time is the durable invariant.

Concrete read-side ask in the webview assembler (same site that currently produces the `-00000000000<N>` last-block row):

1. **Detect:** when an incoming JSONL record has `message.content.length > 1` (assistant or user; the user-side mirror would matter for any future bundled `tool_result` paths), treat it as a fallback bundle.
2. **Emit N rows** instead of one, each with `content: [block_i]` and uuid `deriveUUID(originalUuid, i)` (the same primitive at `src/utils/messages.ts:725` that the assembler already uses to synthesize the suffix `-000000000<N>` for the last block; it just needs to iterate `for i in 0..content.length` instead of stopping at the last index). The first block keeps `parentUuid` from the disk record; subsequent blocks chain to the previous synthesized uuid. No information is lost.
3. **Surface a marker** on the synthesized rows (an unobtrusive italic note, e.g. *"non-streaming fallback: blocks recovered from bundled record"*) so users observing odd preamble-then-tool_use sequencing in the future can correlate it with the cause. Mirrors the K-seam pattern from `claude-patches`'s Patch K.

This is independent of the write-side fix and should land in parallel.

_The [leak](https://github.com/yasasbanukaofficial/claude-code) is what made this diagnosis worth filing. The symptom looked like a renderer bug: one rendered row where there should have been three, with a mutated uuid suffix `-000000000002`. The natural next move was to instrument the webview assembler and trace why blocks were being dropped. What stopped me from going down that path was the comment at `QueryEngine.ts:718-731`, which names the contract between `claude.ts` and the writer outright: "claude.ts yields one assistant message per content block, then mutates the last one's message.usage/stop_reason on message_delta." Once that's named, the multi-block fallback record at `claude.ts:2571-2594` is the actual breach, and the assembler is correctly handling a malformed input it was handed. Comments are the part minification strips and the part design intent lives in. Without them I'd have spent the day instrumenting the wrong layer, or filed a vaguer bug against the renderer. Diagnosed by an instance of Claude Opus 4.7 working with the user._

# Comments on anthropics/claude-code#57819
Total: 0 comments

No comments on this issue.

---

### Issue #42010 — Bug report: Ink rendering corruption during heavy text streaming — cumulative frame buffer contamination

State: OPEN | #42010


---

Bug report: Ink rendering corruption during heavy text streaming — cumulative frame buffer contamination

We investigated a persistent rendering corruption bug in Claude Code's terminal output. The corruption manifests as visual glyph-level rendering breakage (not character encoding issues) during heavy text processing. Analysis was performed against v2.1.88.

---

## Symptoms

1. **Rendering corruption during heavy text output** — A single glyph block renders incorrectly (visual/drawing corruption, not wrong codepoints). Occurs most frequently during long streaming responses
2. **Terminal resize temporarily fixes it** — Slightly changing the terminal width resets the corruption. This is a known user workaround
3. **Corruption persists and escalates** — Once noise enters the session, subsequent rendering becomes increasingly fragile. The session never fully recovers

---

## Root cause analysis

### Why resize fixes it — the key clue

Terminal resize triggers two reset paths that normal rendering never invokes:

1. **Full screen clear and repaint**: When viewport width changes, the renderer issues a full terminal clear (`ESC[2J` + `ESC[3J` + `CSI H`) and repaints from scratch, bypassing the incremental diff pipeline entirely.

2. **Frame buffer replacement**: The resize handler replaces both front and back frame buffers with freshly created blank screens and sets a contamination flag that forces a full repaint on the next frame, bypassing all diff/blit logic.

**This tells us**: the corruption lives in the diff rendering pipeline's internal state — specifically in the previous frame's screen data and/or style transition caches that are used during normal incremental rendering but bypassed during a full repaint.

---

## Level 1: Frame buffer contamination via DECSTBM scroll — most likely cause

The DECSTBM scroll optimization mutates the previous frame's screen buffer **in-place** by shifting rows to match the terminal's scroll region movement. The intent is to keep the previous screen in sync with what the terminal actually shows after a DECSTBM scroll, so the subsequent cell-by-cell diff produces minimal output.

**The problem**: The mutated previous screen belongs to the front frame buffer. After the diff is computed, the frame lifecycle swaps buffers — the mutated screen moves to the back position, where it is reused as the **write target** for the next render cycle. When the blit operation copies unchanged cells from the new front buffer onto the contaminated back buffer, cell data from misaligned rows can bleed through.

During streaming, DECSTBM scroll fires on nearly every frame (10-50 SSE events/sec triggers continuous scrolling). Each in-place row shift compounds on the previous one. The contamination accumulates until rendering becomes visibly corrupt.

**Evidence**: The resize handler is the **only** code path that replaces both frame buffers with fresh screens. Normal rendering always reuses the previous frame's screen as the next frame's write target. This is why corruption persists until resize — nothing else clears the contaminated back buffer.

**Fix**: Clone the screen's row data before applying the row shift, so the mutation is used only for computing the diff patch and does not persist into the next frame's write target.

---

## Level 2: Style transition cache key collision — latent bug, escalation factor

The style pool's transition caching mechanism stores ANSI escape sequences for transitioning between two styles. The cache key is computed by packing two style IDs into a single number using fixed-width multiplication (conceptually `fromId * N + toId` with a fixed N).

Style IDs are generated by the style interning mechanism with a bit-shift encoding. When the number of unique styles exceeds ~524K, the packed key overflows and **different style pairs map to the same key**. The cached transition string for one pair silently overwrites or is returned for another.

**Critically, the style pool is never reset during a session.** The pool reset logic only resets the character pool and hyperlink pool — the style pool and its transition cache live for the entire session with no eviction or size limit. As unique styles accumulate (syntax highlighting × hyperlinks × decorations), the collision probability steadily increases.

**This explains "once corrupted, stays corrupted"**: even after a resize clears the screen and repaints from scratch, the poisoned transition cache entry persists. The next time the colliding style pair is encountered, the wrong ANSI transition sequence is emitted again.

**Practical reachability**: Whether 524K unique styles are reached in a single session depends on the diversity of styled content. In long sessions with heavy syntax-highlighted code output, this is plausible but unconfirmed.

**Fix**: Replace the numeric key encoding with a collision-free alternative, such as a string key. The performance impact is negligible since the cache is hit once per unique style pair.

---

## Level 3: Additional contributing factors

### Multi-codepoint emoji viewport edge miscalculation

When rendering wide characters (width = 2) near the right edge of the viewport, the renderer applies a stricter boundary check for multi-codepoint graphemes (flag emoji, ZWJ sequences) than for single-codepoint wide characters (CJK). The stricter threshold causes a valid cell at position `vw - 2` — which fits perfectly in the last two columns — to be incorrectly skipped. The previous frame's content remains at that position, and subsequent diffs make the same skip decision, so the stale cell becomes permanent.

**Fix**: Apply the same viewport edge threshold for all wide characters regardless of codepoint count, or re-examine whether the stricter threshold is truly necessary.

### Style segment desync in wrapped text

The post-wrap style reapplication logic uses a heuristic to skip whitespace characters in the original text and keep a character index synchronized with the wrapped output. The heuristic compares the current character against the next line's first character to decide when to stop skipping. This breaks when the next line starts with a whitespace character (premature stop → under-advance) or when the next line is empty (no stop condition → over-advance). Either way, the wrong style segment is referenced, causing one block of text to render with the adjacent segment's style.

### Cache cliff-edge eviction

The character cache (which stores tokenized + clustered representations of text lines) is cleared in its entirety when it exceeds a fixed threshold (~16K entries). The next frame must re-tokenize and re-cluster every visible line, causing a CPU spike and frame delay. Not a direct corruption cause, but the frame timing disruption amplifies the scroll contamination (Level 1) by increasing the chance of stale data surviving across frames.

---

## Environment

- Claude Code: v2.1.88
- OS: macOS (Darwin 25.3.0, Apple Silicon)
- Terminal: various (reproduction is terminal-independent)

The source map leak may have been an unfortunate accident — but it would be nice if, looking back, both sides could say it became an opportunity for engineers around the world to contribute to a better product.

---

<details>
<summary><strong>Investigation notes</strong> — full analysis process (hypotheses, methodology, findings)</summary>

## Investigation: Hypotheses

1. **Diff rendering internal state is corrupted** — Ink is a React-based TUI framework that outputs only the diff from the previous frame. The internal state used for diff calculation (caches, previous frame buffer) is somehow corrupted, and the corruption propagates to subsequent frames
2. **Resize triggers a special reset that normal rendering doesn't** — The cleanup target of the resize handler is the corruption itself
3. **Large text volume is the trigger** — Cache bloat, style ID exhaustion, buffer threshold overflow — problems that depend on quantity

## Investigation: Methodology

The Ink rendering subsystem (~96 source modules) was investigated along three axes in parallel:

- **Axis A: Output & rendering pipeline** — output buffering, screen diffing, log-update logic, screen/style pool management, terminal I/O
- **Axis B: Text measurement & ANSI parsing** — text measurement, string width calculation, text wrapping, ANSI tokenization and parsing
- **Axis C: Resize & frame management** — the main Ink instance lifecycle, frame scheduling, node-to-output rendering, DOM management, React reconciler

## Investigation: Key findings

### Finding 1 — Resize reset mechanism

Two paths are triggered on resize. The critical one replaces both front and back frame buffers with blank screens and sets a contamination flag. This is the **only** code path that replaces both frame buffers — normal rendering always reuses the previous frame's screen as the next frame's write target.

### Finding 2 — Style pool lifetime

The pool reset logic resets the character pool and hyperlink pool but **not** the style pool. The style pool — including its transition cache — lives for the entire session with no eviction or size limit.

### Finding 3 — DECSTBM scroll optimization mutates the previous screen

The scroll optimization destructively shifts rows in the previous screen. This screen belongs to the front frame buffer, which moves to the back position on the next frame — where it is reused as the write target for the next render.

### Finding 4 — Character cache cliff-edge eviction

The character cache is cleared entirely when exceeding a fixed threshold, forcing a full re-tokenize on the next frame and causing a CPU spike.

### Finding 5 — Multi-codepoint emoji edge miscalculation

Flag emoji and ZWJ sequences use a stricter viewport edge threshold than CJK characters, causing valid cells near the right edge to be incorrectly skipped.

### Finding 6 — Style segment desync in wrapped text

The whitespace-skipping heuristic for character index synchronization after text wrapping has edge cases where the index under-advances or over-advances, causing style segments to shift by one block.

## Investigation: Ruled out

- ANSI tokenizer — OSC/CSI terminator detection logic is correct
- Line width cache — eviction does not produce stale data
- String width calculation — consistent across implementations for major character classes
- SGR parsing — no issues found

</details>

# Comments on anthropics/claude-code#42010
Total: 4 comments

--- Comment 1 ---
Author: xbzzoo
Date: 2026-04-01T14:28:47Z

https://t.me/+t_ed3b95DqczNmU1

--- Comment 2 ---
Author: efyfe-va
Date: 2026-04-13T20:22:23Z

Confirming this bug from a different repro path on macOS Terminal.app (Claude Code 2.1.104). 

 **Repro:**                                                                    
1. Run `/ce:brainstorm <topic>` from the [compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)
2. Let the brainstorm run for several rounds — long streaming responses, with the skill repeatedly invoking the `AskUserQuestion` widget between turns
3. After ~5–10 minutes of back-and-forth, prose text streamed *immediately before* an `AskUserQuestion` widget gets visually truncated. Resizing the terminal does not recover it.

  **What I see:** 
Claude's prose ends mid-sentence right where the interactive selection widget begins drawing. The text is permanently lost from the screen, but asking Claude to repeat its previous message reprints the full content into a fresh region — so the bug is purely in the rendering buffer, not the underlying conversation.


--- Comment 3 ---
Author: vssy
Date: 2026-05-14T13:16:48Z

Reproducing on **v2.1.141** (macOS). The corruption manifests in the diff/agent view — characters render with extra spaces inserted between them and HTML tag content bleeds through (e.g., `< s ron >` instead of `<strong>`). Started occurring after the agent view rollout. Terminal resize temporarily clears it, consistent with the frame buffer repaint fix described here.

--- Comment 4 ---
Author: otherjoel
Date: 2026-05-15T19:46:27Z

<img width="1758" height="1518" alt="Image" src="https://github.com/user-attachments/assets/df0cebe3-d50e-444c-8f02-1e37f8f5ac9d" />

---

### Issue #36862 — [DOCS] Platform-specific docs missing Windows/WSL line-by-line streaming disabled notice

State: OPEN | #36862
Labels: documentation, platform:windows, platform:wsl, area:docs


---

### Documentation Type

Missing documentation (feature not documented)

### Documentation Location


https://code.claude.com/docs/en/troubleshooting

### Section/Topic


Windows-specific behavior and known limitations

### Current Documentation


No documentation currently exists describing platform-specific streaming behavior differences. Line-by-line response streaming was introduced in v2.1.78 (noted only in the changelog) but has no narrative documentation explaining the feature or its platform availability.

The troubleshooting page has Windows-specific sections covering installation, PATH issues, and Git Bash requirements, but nothing about streaming behavior differences.

### What's Wrong or Missing?


Changelog v2.1.81: "Disabled line-by-line response streaming on Windows (including WSL in Windows Terminal) due to rendering issues."

All Windows and WSL-in-Windows-Terminal users see different response rendering behavior compared to macOS/Linux users. Responses do not stream line-by-line on these platforms. This platform-specific behavior difference is not documented anywhere, leaving Windows users unaware that the difference is intentional rather than a bug.

### Suggested Improvement


Add a note to the Windows section of the troubleshooting page or the setup page:

> **Note:** Line-by-line response streaming is disabled on Windows (including WSL in Windows Terminal) due to terminal rendering compatibility issues. Responses will still appear but may render differently than on macOS or Linux.

### Impact

Low - Minor confusion or inconvenience

### Additional Context


**Affected Pages:**

| Page | Context |
|------|---------|
| https://code.claude.com/docs/en/troubleshooting | Windows-specific sections (line ~443) |
| https://code.claude.com/docs/en/setup | Windows setup section (line ~98) |

**Total scope:** 2 pages affected

**Source:** Changelog v2.1.81 — "Disabled line-by-line response streaming on Windows (including WSL in Windows Terminal) due to rendering issues"

# Comments on anthropics/claude-code#36862
Total: 3 comments

--- Comment 1 ---
Author: coygeek
Date: 2026-04-07T17:51:08Z

Still relevant as of 2026-04-07. I rechecked the current public docs and issue state, and this still appears unresolved.

Evidence: https://code.claude.com/docs/en/troubleshooting and https://code.claude.com/docs/en/setup cover current Windows/WSL guidance, but they still do not mention the Windows/WSL line-by-line streaming limitation that is called out in https://code.claude.com/docs/en/changelog line 344.

--- Comment 2 ---
Author: coygeek
Date: 2026-05-08T06:18:49Z

Checked the current docs on 2026-05-07. This documentation gap is still unresolved.

--- Comment 3 ---
Author: coygeek
Date: 2026-05-23T00:59:24Z

checked docs, not resolved yet

---

### Issue #62671 — [DOCS] `/usage` documentation omits large session files in limits breakdown

State: OPEN | #62671
Labels: documentation, duplicate, area:docs

---

### Documentation Type

Incorrect/outdated documentation

### Documentation Location


https://code.claude.com/docs/en/costs

### Section/Topic


`Using the /usage command`

### Current Documentation


The docs currently say:

> On a Pro, Max, Team, or Enterprise plan, `/usage` also shows a breakdown of what counts against your plan limits. It attributes recent usage to skills, subagents, plugins, and individual MCP servers, with each shown as a percentage of the total. Press `d` or `w` to switch between the last 24 hours and the last 7 days. The figures are approximate and computed from local session history on this machine, so usage from other devices or claude.ai is not included.

But the v2.1.152 changelog says:

> The `/usage` breakdown now includes large session files; files are scanned with a streaming read so memory usage stays flat

### What's Wrong or Missing?


The current `/usage` documentation still describes the limits breakdown as if it only covers skills, subagents, plugins, and individual MCP servers.

That is outdated for v2.1.152. The changelog says the breakdown now also includes large session files, but the main `/usage` docs do not mention that additional contributor anywhere.

The docs also do not mention the user-visible behavior change that large session files are scanned with a streaming read so memory usage stays flat while computing the breakdown.

### Suggested Improvement


Update the `/usage` section in `https://code.claude.com/docs/en/costs` to reflect the v2.1.152 behavior.

At minimum:

1. Add large session files to the documented list of contributors in the limits breakdown.
2. Clarify that Claude Code now scans those files with a streaming read when building the breakdown.
3. Note that this keeps memory usage flat when users have very large local session files.

### Impact

Medium - Makes feature difficult to understand

### Additional Context


**Affected Pages:**

| Page | Context |
|------|---------|
| https://code.claude.com/docs/en/costs | Main `/usage` documentation lists breakdown contributors but does not mention large session files or the streaming-read behavior added in v2.1.152 |

**Total scope:** 1 page affected

This gap is based on the v2.1.152 changelog entry for `/usage`.

# Comments on anthropics/claude-code#62671
Total: 0 comments

No comments on this issue.

---

### Issue #55650 — [BUG]

State: OPEN | #55650
Labels: bug, duplicate, platform:linux, area:api, api:anthropic, stale

---



### What's Wrong?

Streaming stalls — 3 occurrences in ~7 minutes of active conversation.

Claude Code version: 2.1.126
Model: claude-sonnet-4-6 (Sonnet 4.6)
Platform: Linux (Fedora 43, kernel 6.19.13-200.fc43.x86_64)
Shell: zsh

Symptom
During an active editing session, response streams hang mid-flight for ~15s–60s before resuming. Killing the request with Ctrl-C and resending "continue" recovers fast (~3s TTFB), suggesting the stall is on the streaming side, not the prompt-encoding side. The pattern matches lastChunkAgeMs ≥ 15000 debug warnings.

Reproducibility: Intermittent. ~3 stalls per 7 minutes of active editing in this session. Cannot reproduce on demand.

Debug log evidence (3 stalls captured in ~/.claude/debug/<session>.txt):

2026-05-02T18:18:28.508Z [WARN] Streaming stall detected: 54.4s gap between events (stall #1)
2026-05-02T18:18:28.518Z [WARN] Streaming completed with 1 stall(s), total stall time: 54.4s

2026-05-02T18:21:05.742Z [WARN] Streaming stall detected: 56.9s gap between events (stall #1)
2026-05-02T18:21:05.750Z [WARN] Streaming completed with 1 stall(s), total stall time: 56.9s

2026-05-02T18:25:28.695Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=14999 bytesTotal=666 idleDeadlineMs=300000

Notable details:
- Stall #3 fired after only 666 bytes had streamed → response size is not a predictor.
- Time-to-first-chunk on every API call was normal (~3s, including the calls that later stalled), so this is not a cold-cache or connection-establishment issue.
- No [ERROR] lines in the debug log; tool dispatches all complete in <50ms.

Affected request IDs (for correlation):
- b1423c34-1ebd-4a54-ba29-188e70dac76b (stall #1 stream)
- fc357338-baec-4137-b639-19466993e32d (stall #2 stream)
- 9070c805-c488-4310-b759-8fd874a76903 (stall #3 — caught live as stream_idle_partial)

What I see in the log that does NOT cause it:
- effortLevel: medium, autoDreamEnabled: true, agentPushNotifEnabled: true — none correlate with the stall lines.
- The 297 "Fast mode unavailable" debug-level lines are unrelated chatter (Fast mode requires /extra-usage, which I haven't enabled).
- Tool dispatch traces ([Stall] tool_dispatch_*) all finish in <50ms — those [Stall] lines are normal telemetry, not actual stalls. The real signal is "Streaming stall detected" / "stream_idle_partial".

Workaround:
Ctrl-C + retype "continue" recovers because the prompt cache stays warm. Lossy though — partial output is dropped.

### What Should Happen?

Claude should answer without mid-stream stalls.

### Error Messages/Logs

```shell

```

### Steps to Reproduce

Cannot deterministically reproduce — appears intermittent on the streaming side. Frequency in this session: 3 stalls in roughly 7 minutes of active back-and-forth (after /debug was enabled; many earlier stalls in the same session predate logging).

### Claude Model

Sonnet (default)

### Is this a regression?

I don't know

### Last Working Version

_No response_

### Claude Code Version

	2.1.126

### Platform

Other

### Operating System

Other Linux

### Terminal/Shell

Other

### Additional Information

_No response_

# Comments on anthropics/claude-code#55650
Total: 0 comments

No comments on this issue.

---

### Issue #58428 — [A11y bug] Missing heading semantics and "response complete" announcements in desktop app

State: OPEN | #58428
Labels: bug, platform:macos, area:a11y, area:desktop, stale

---

## Summary
The Claude Code desktop app does not provide the heading structure or response-completion cues that the Claude.ai web app provides. This is a regression in accessibility parity between two surfaces of the same product.

## Impact
As a blind VoiceOver user, in the Claude.ai web app I can:
- Use VoiceOver rotor to jump between headings in a response.
- Hear a clear announcement when Claude has finished streaming a response.

In the Claude Code desktop app, neither of these works. Claude's output appears as flat text with no navigable heading landmarks, and there is no reliable cue that the response is complete. I end up arrow-keying through the entire output or guessing when it's safe to start typing again.

## Expected
- Markdown headings in Claude's response render as proper heading landmarks (H1/H2/H3) so VoiceOver rotor can navigate them.
- A clear announcement (live region, system notification, or focus change) fires when Claude finishes streaming a response, matching the Claude.ai behavior.

## Context
I submitted the same feedback via the in-app `/feedback` channel and to support@anthropic.com so the team can dedupe.

I am Lead Accessibility Architect at Paramount Streaming. Happy to test fixes.

# Comments on anthropics/claude-code#58428
Total: 0 comments

No comments on this issue.

---

### Issue #61634 — [BUG] False-positive Usage Policy refusal mid-stream on a markdown comparison table

State: OPEN | #61634
Labels: bug, platform:macos, area:model, api:anthropic


---

## What happened
Claude Code aborted mid-stream with:
> API Error: Claude Code is unable to respond to this request, which appears to violate our Usage Policy

The cut hit while Claude was emitting a markdown comparison table describing how three docs in a website-builder project are organized (a routing description for `CLAUDE.md`, `frontend-design.md`, `website-marketing.md`). The user request was non-sensitive — "describe current file topology and propose alternatives".

## Request ID
`req_011CbJm3BzH1cZ9754o4Zw1S`

## Repro / context
- ~30s into a streaming response that had started rendering a 3-row markdown table.
- Refusal landed on what would have been a row about workflow steps.
- No restricted topics, no jailbreak attempts.

## Why this looks like a false positive
The visible content before the refusal was metadata about file organization. There is nothing in the conversation that should trigger Usage Policy enforcement.

## Expected behaviour
If a classifier is going to trigger, it should fire before any tokens are streamed — not mid-stream after the user has already seen ~50% of the response. Mid-stream refusal on benign content makes Claude Code feel unreliable.

## Workaround
Retry. Sometimes the same prompt succeeds on a second attempt.

## Related
- #7559 (closed autoclosed without investigation)

## Environment
- Claude Code: 2.1.149
- Model: claude-opus-4-7
- OS: macOS Darwin 25.5.0

# Comments on anthropics/claude-code#61634
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-23T03:22:12Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/55975
2. https://github.com/anthropics/claude-code/issues/48442
3. https://github.com/anthropics/claude-code/issues/57259

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: jshaofa-ui
Date: 2026-05-23T13:12:32Z

# Solution: claude-code #61634 — Usage Policy False Positive on Markdown Tables

## Problem Statement

Claude Code aborted mid-stream with a Usage Policy violation error while generating a markdown comparison table describing file organization in a website-builder project. The user request was completely benign: "describe current file topology and propose alternatives." The classifier triggered on the structured output (markdown table with file paths and descriptions), not on the actual content intent.

**Issue:** https://github.com/anthropics/claude-code/issues/61634
**Labels:** bug, platform:macos, area:model, api:anthropic
**Competition:** 0 comments, 0 PRs (zero competition)
**Estimated Value:** $1,000–$3,000

## Root Cause Analysis

### Primary Failure Mode: Streaming Classifier Triggers on Structured Output

The current architecture runs the Usage Policy classifier on each streaming token chunk independently. This creates several failure modes:

1. **Loss of context in streaming mode:** Each chunk is classified in isolation, without understanding the broader document structure or intent.

2. **False positive on technical content:** Markdown tables with file paths (e.g., `CLAUDE.md`, `frontend-design.md`, `website-marketing.md`) may contain patterns that resemble policy-violating content when viewed in isolation:
   - File paths with certain keywords trigger pattern matches
   - Comparison language ("better than", "vulnerability in") looks suspicious without context
   - Technical descriptions of routing/URLs resemble attack descriptions

3. **No retry mechanism:** Once the classifier fires, the session is terminated with no opportunity for correction.

### Failure Sequence

```
User Request: "describe current file topology and propose alternatives"
       ↓
Claude generates: markdown table with file paths
       ↓
Streaming chunk: "| CLAUDE.md | Root config | ..."
       ↓
Classifier sees: file paths + "config" + comparison language
       ↓
FALSE POSITIVE: Flags as potential policy violation
       ↓
Session terminated: "Usage Policy violation"
```

## Proposed Solution

### Architecture: Deferred Classification with Structured Output Awareness

```
┌──────────────────────────────────────────────────────┐
│              Streaming Generation                    │
├──────────────────────────────────────────────────────┤
│                                                      │
│  Chunk → Buffer (accumulate) → Classify (deferred)   │
│                                                      │
│  ┌───────────┐  ┌──────────────┐  ┌───────────────┐ │
│  │ Structure  │→│ Context-Aware │→│  Final        │ │
│  │ Detection  │ │ Classification│ │  Decision     │ │
│  └───────────┘  └──────────────┘  └───────────────┘ │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### 1. Structured Output Detection

```python
import re
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum

class OutputStructure(Enum):
    PLAIN_TEXT = "plain_text"
    MARKDOWN_TABLE = "markdown_table"
    CODE_BLOCK = "code_block"
    JSON = "json"
    XML = "xml"
    HTML = "html"

@dataclass
class StructureContext:
    structure_type: OutputStructure

---

### Issue #63532 — [BUG] /context shows 0 tokens for all MCP tools on Bedrock — countTokensWithFallback fails with 400 tools.0.custom.eager_input_streaming: Extra inputs are not permitted

State: OPEN | #63532
Labels: bug, has repro, api:bedrock, area:tools, area:mcp, platform:wsl

---



### What's Wrong?

The `/context` command displays **0 tokens** for every MCP tool (all 141 tools across atlassian, glean, azure-devops, snowflake, etc.) even after those tools have been actively used in the session. The same `0 tokens` applies to all deferred tools (TaskCreate, WebFetch, CronCreate, etc.) and to the 8 built-in tools (Agent, Bash, Read, etc.).

The root cause, found in the debug log, is that the token counting fallback chain completely fails when running via Bedrock:

1. The primary counter calls the Bedrock inference profile for `global.anthropic.claude-sonnet-4-6` and gets `null` (with `Request aborted`).
2. It falls back to `global.anthropic.claude-haiku-4-5-20251001-v1:0` via Bedrock, which returns a `400` error for **every** tool group:

```
countTokensWithFallback: fallback failed: 400 tools.0.custom.eager_input_streaming: Extra inputs are not permitted
countToolDefinitionTokens returned null for 141 tools: mcp__atlassian__addCommentToJiraIssue, ...
countToolDefinitionTokens returned null for 8 tools: Agent, AskUserQuestion, Bash, Edit, Read, Skill, ToolSearch, Write
```

The error `tools.0.custom.eager_input_streaming: Extra inputs are not permitted` suggests that Claude Code 2.1.153 sends a tool schema field (`eager_input_streaming`) that the Bedrock endpoint rejects as an unknown/extra field.

Importantly, **actual tool calls work fine** — the MCP tools execute successfully (e.g. `getJiraIssue` completed in 1.6s). Only the token-counting side-channel is broken, which makes `/context` unable to display meaningful token counts for any tool.

### What Should Happen?

`/context` should display accurate per-tool-group token counts even on Bedrock. The fallback token counting mechanism should either:
- Not send the `eager_input_streaming` field when targeting a Bedrock endpoint that doesn't support it, or
- Gracefully handle the `400 Extra inputs are not permitted` and display a best-effort estimate instead of silently reporting `0` for everything.

### Steps to Reproduce

1. Configure Claude Code to use Bedrock (`CLAUDE_CODE_USE_BEDROCK=1` or equivalent Bedrock routing).
2. Start a session with multiple MCP servers connected (atlassian, glean, azure-devops, etc.).
3. Use any MCP tool (e.g. `mcp__atlassian__getJiraIssue`).
4. Run `/context`.
5. Observe: all MCP tools show `0 tokens`, all deferred tools show `0 tokens`, built-in tools show `0 tokens`.

### Debug Log Evidence

```
[ERROR] Failed to resolve Bedrock inference profile backing model for global.anthropic.claude-sonnet-4-6: Request aborted
[ERROR] countTokensWithFallback: fallback failed: 400 tools.0.custom.eager_input_streaming: Extra inputs are not permitted
[DEBUG] countToolDefinitionTokens returned null for 141 tools: mcp__atlassian__addCommentToJiraIssue, mcp__atlassian__addWorklogToJiraIssue, ...
[DEBUG] countToolDefinitionTokens returned null for 8 tools: Agent, AskUserQuestion, Bash, Edit, Read, Skill, ToolSearch, Write
[DEBUG] countToolDefinitionTokens returned null for 1 tools: CronCreate
[DEBUG] countToolDefinitionTokens returned null for 1 tools: WebFetch
... (repeated for every tool/group)
```

This is repeated identically every time `/context` is invoked.

### Environment

- Claude Code: v2.1.153
- Platform: Linux (WSL2, 5.15.167.4-microsoft-standard-WSL2)
- Shell: zsh
- Model: `global.anthropic.claude-sonnet-4-6` via Bedrock
- MCP servers connected: atlassian, glean, azure-devops, snowflake, memory

# Comments on anthropics/claude-code#63532
Total: 0 comments

No comments on this issue.

---

### Issue #62870 — [BUG] Streaming output corrupts CJK characters to U+FFFD at UTF-8 chunk boundaries (still repro on 2.1.150)

State: OPEN | #62870
Labels: bug, has repro, platform:macos, area:core

---

## Summary

Multibyte (CJK) characters in Claude Code's streamed output are intermittently replaced with U+FFFD (REPLACEMENT CHARACTER, `�`). The **same** character renders correctly elsewhere in the **same** response, so this is a non-deterministic chunk-boundary bug — not a font, terminal, or locale issue.

This is the same defect as **#45508** ("Streaming output corrupts CJK characters at UTF-8 chunk boundaries") and **#40396**, with duplicates **#42867 / #47013 / #48904**. All of those were closed `NOT_PLANNED` / `stale` — **none were fixed**. It still reproduces on the latest CLI (`2.1.150`). Re-filing with byte-level proof on the current version and a concrete fix to request re-triage.

## Environment

- Claude Code: **2.1.150**
- OS: macOS (Darwin 24.0.0), Apple Silicon
- Output format: `--output-format stream-json`
- Language observed: Chinese (Simplified); the same class of corruption was reported for Korean (#47013, #40396) and Japanese (#42867, #48904)

## Evidence

Within a **single** assistant response, the character `台` (U+53F0, UTF-8 `E5 8F B0`) appeared both correctly and corrupted:

| Occurrence (same response) | Result |
|---|---|
| `Windows 平台多个 surface` | correct |
| `Windows 平台适配` | correct |
| `Windows 平���多项适配` | **corrupted** |

Hex dump of the corrupted run (`平…多项适配`), taken from the session JSONL log (not the terminal):

```
e5 b9 b3            平   U+5E73
ef bf bd            �    U+FFFD
ef bf bd            �    U+FFFD
ef bf bd            �    U+FFFD
e5 a4 9a            多   U+591A
e9 a1 b9            项   U+9879
e9 80 82            适   U+9002
e9 85 8d            配   U+914D
```

One 3-byte character (`台` = `E5 8F B0`) became **exactly three** U+FFFD. That is the precise signature of a byte split **after the first byte** (`E5` | `8F B0`), decoded with non-streaming semantics:

- `E5` alone → incomplete lead byte → 1× U+FFFD
- `8F`, `B0` → two orphaned continuation bytes → 2× U+FFFD

(This matches #47013's Korean hex dump exactly: one 3-byte `습` = `EC 8A B5` → 3× U+FFFD.)

## Why this is the CLI, not the consumer

The output was captured from the CLI's `stream-json` stdout via a Python `io.TextIOWrapper` (incremental UTF-8 decoder), and every line was `json.loads()`-parsed successfully before being stored. Two consequences:

1. An **incremental** decoder does not emit U+FFFD for a valid multibyte char split across its own read boundaries — it retains the partial bytes until the next read. So the consumer cannot have introduced these.
2. `json.loads()` succeeding proves each line was already valid UTF-8 carrying **literal U+FFFD code points**.

Node always emits valid UTF-8 when writing a JS string to stdout, and `--output-format stream-json` goes through `JSON.stringify`. Therefore the U+FFFD was already baked into the CLI's in-memory string **before** serialization — i.e. the corruption happens in the CLI's SSE-stream → string decode path, upstream of stdout.

## Root cause hypothesis

The Anthropic API SSE response is decoded per network/SSE chunk, and a multibyte UTF-8 sequence that straddles a chunk boundary is decoded without carrying the incomplete trailing bytes into the next chunk — e.g. `TextDecoder` used without `{ stream: true }`, or `Buffer.toString('utf8')` called on an individual partial chunk. Each orphaned byte then decodes to U+FFFD.

## Suggested fix

Decode the SSE byte stream with a streaming decoder that preserves partial multibyte sequences across chunk boundaries:

- `const dec = new TextDecoder('utf-8'); dec.decode(chunk, { stream: true })` on every chunk, with a final `dec.decode()` flush at stream end; **or**
- accumulate raw `Buffer`s and decode only at complete boundaries (e.g. once per fully-assembled SSE `data:` event), never on an arbitrary partial chunk.

## Reproduction

Intermittent; more likely on longer CJK responses. The per-character corruption probability tracks the chunk-boundary hit rate, so the vast majority of characters are intact and occasional ones corrupt — consistent with every prior report.

## Prior reports (all closed without a fix)

- #45508 — Streaming output corrupts CJK characters at UTF-8 chunk boundaries (displays `���`) — CLOSED `NOT_PLANNED`, stale
- #40396 — Korean (CJK) characters corrupted to U+FFFD on macOS + VSCode — CLOSED `NOT_PLANNED`, stale
- #42867 — U+FFFD in Agent SDK streaming output for CJK text — CLOSED duplicate
- #47013 — Korean characters corrupted during streaming (U+FFFD) — CLOSED duplicate
- #48904 — Japanese (CJK) U+FFFD corruption in streaming response — CLOSED

The recurrence across 5+ reports and multiple languages, combined with closure-by-staleness rather than by fix, is the reason for re-filing on the current version with a byte-level root cause and a concrete patch direction.

# Comments on anthropics/claude-code#62870
Total: 0 comments

No comments on this issue.

---

### Issue #53382 — [BUG] Desktop app: chat window auto-scrolls to bottom during streaming even when user has scrolled up

State: OPEN | #53382
Labels: bug, platform:windows, platform:macos, regression, area:desktop, stale


---



### What's Wrong?

**This affects the Claude Code Desktop app on Windows (not the CLI / terminal version).**

While Claude is streaming a response (token-by-token / phrase-by-phrase), the
chat window force-scrolls to the bottom on every update. This happens even when
I have explicitly scrolled up to read earlier content — including scrolling all
the way to the top of the conversation. The viewport is yanked back down on
every new chunk, making it impossible to read previous messages while a
response is being generated.

This started in recent versions; older builds of the desktop app did not behave
this way.

### What Should Happen?

Standard "sticky bottom" behavior used in terminals, chat apps and IDE chat
panels:

- If the user is at the bottom of the scroll
  container, auto-scroll to follow new streaming content.
- If the user has scrolled up beyond that threshold, do NOT auto-scroll. Leave
  the viewport exactly where the user put it.
- Optional: show a "jump to bottom" button / new-message indicator so the user
  can opt back in with a single click.

This is the same UX that was already shipped for the VSCode extension via
issue #11092 ("Auto-scroll should pause when user scrolls up in chat",
closed completed on 2025-11-12). The desktop app appears to be missing that
fix (or has regressed it).

### Error Messages/Logs

```shell

```

### Steps to Reproduce

1. Open Claude Code Desktop app on Windows.
2. Send a prompt that produces a long streamed response (e.g. ask for a
   detailed explanation, or run an agent task that emits a lot of streaming
   output).
3. While the response is still streaming, scroll up to read an earlier part
   of the conversation — even all the way to the top.
4. Observe: the viewport jumps back toward the bottom on every new chunk the
   model emits. There is no way to keep the viewport stationary until
   streaming finishes.

Expected: viewport stays where the user put it.
Actual:   viewport is yanked down on every streaming update.

### Claude Model

None

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

app-1.3561.0

### Claude Code Version

app-1.4758.0

### Platform

Anthropic API

### Operating System

Windows

### Terminal/Shell

Windows Terminal

### Additional Information

_No response_

# Comments on anthropics/claude-code#53382
Total: 3 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-04-25T23:20:13Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/37627
2. https://github.com/anthropics/claude-code/issues/49183
3. https://github.com/anthropics/claude-code/issues/38411

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: mvgx
Date: 2026-04-25T23:34:12Z

Not a duplicate of any of the three. Quick triage:

- #37627 — `area:tui`, macOS terminal. Different surface (TUI, not desktop app).
- #38411 — `area:tui`, terminal scroll-lock feature request. Different surface.
- #49183 — closest, but different trigger: that issue is about the viewport
  jumping when the **user submits a message** (despite `autoScrollEnabled: false`).
  This issue is about the viewport being yanked down while the **assistant is
  streaming a response**. Different code path, different trigger, different
  fix. Possibly related, but not a duplicate.

Please keep open — this is a desktop-app streaming-time autoscroll regression
between 1.3561.0 and 1.4758.0, not covered by the three issues above.

--- Comment 3 ---
Author: LoicLac
Date: 2026-05-04T17:09:33Z

+1, can reproduce this on **macOS** as well, so this isn't Windows-specific — the `platform:windows` label should probably be extended to `platform:macos` too (likely all platforms).

### Environment
- **OS:** macOS 15.7.3 (24G419)
- **Claude Code Desktop version:** 1.5354.0 (9a9e3d), built 2026-04-29 — i.e. **newer** than the version in the original report (`app-1.4758.0`), so the regression is still present in the latest builds.
- **Last known working version:** matches @mvgx's report (somewhere before `app-1.4758.0`).

### Reproduction
Identical to the original report. Specifically:
1. Send any prompt that produces a long streamed response (detailed explanation, refactor over several files, anything that streams for more than a few seconds).
2. Start scrolling up to read earlier content while the response is still streaming.
3. The viewport is yanked back down on every chunk. There is no threshold detection — even being scrolled to the very top of the conversation does not pause the auto-scroll.

### Impact on workflow
This breaks a core reading pattern: starting to read the response from the top while it continues generating below. On long responses (code reviews, multi-file diffs, agent traces), it is effectively impossible to read anything until streaming finishes, which can take minutes. Constant friction for any non-trivial task.

### Why this should be cheap to fix
The exact same UX was already implemented for the VSCode extension via #11092 (opened 2025-11-06, closed completed 2025-11-12 — **6 days**). The sticky-bottom logic + threshold detection already exists somewhere in the codebase; this looks more like a port / re-enable than a from-scratch implementation.

### Suggested acceptance criteria
- If user is within ~50px of the bottom → follow stream (current behavior).
- If user has scrolled up beyond that threshold → freeze viewport, do not auto-scroll on new chunks.
- Show a "jump to bottom" pill / new-message indicator when the user is detached, clickable to re-attach.
- Re-attach automatically when the user manually scrolls back to the bottom.

Happy to test a nightly / canary build if one is available.

---

### Issue #60002 — VSCode extension: "Unhandled case: [object Object]" banner orphans response, leaves chat stuck at "Thinking…"

State: OPEN | #60002
Labels: bug, platform:windows, platform:vscode


---

## Summary

Intermittent red error banner reading **`Unhandled case: [object Object]`** appears at the top of the chat panel inside the Claude Code VSCode extension. While the banner is up, the in-progress assistant turn never produces output — the message bubble just shows the "Thinking…" spinner indefinitely. Dismissing the banner with the ✕ and sending any follow-up prompt (e.g. "hello?", "continue") resumes normally, and the assistant picks up where it left off — so the conversation state is intact on the agent side; the failure is purely in the client's response delivery / render path.

The `[object Object]` payload is the classic JS bug where an error object is interpolated into a template literal (or `String()`-coerced) without `.message` / `.toString()` first, so `Object.prototype.toString()` returns the literal string `"[object Object]"`. Whatever code renders the banner is receiving an `Error`-shaped object and stringifying it incorrectly — the underlying real error is being swallowed.

## Repro (observed, not deterministic)

Trigger has been hard to pin down — appears most often during long-running sessions with frequent MCP server reconnects, also when context grows large. Roughly every 30-60 min in active use.

## Impact

- **Lost responses.** Any tool-rich or long assistant turn in progress when the banner fires is unrecoverable from the UI — the work is done agent-side but not surfaced to the user.
- **Confusion about state.** Users sometimes think the agent is hung and start asking "hello?" / "continue", which re-triggers the agent and produces duplicate / overlapping work.
- **Silent data loss for the bug itself.** Because the actual error is stringified to `[object Object]`, neither the user nor (presumably) telemetry knows what actually went wrong.

## Workarounds we use now

1. Dismiss the banner with ✕.
2. Send a short re-prompt like `continue` or `hello?` — the agent picks up cleanly.

Both are user-side band-aids; the underlying response is still lost.

## Suggested fix direction

- Wherever the banner copy is built, replace `${err}` / `String(err)` with `err?.message ?? err?.toString?.() ?? JSON.stringify(err)` — at minimum the user sees what went wrong.
- Separately, the response-delivery path should probably still flush the assistant's pending output even when a non-fatal client error fires — orphaning a "Thinking…" bubble is a worse UX than showing both the error and the partial response.

## Environment

- Claude Code VSCode extension (native panel, not the web client)
- Windows 11
- VS Code (recent stable)
- Heavy MCP usage (chrome-devtools, github, sentry, playwright, context7, gmail, calendar, drive, canva, notion) — several of these intermittently disconnect/reconnect during the session, which may or may not be related
- Conversation is long-running and tool-rich

## Filing this on the user's behalf

Filed by the Claude assistant from inside an active session at the user's explicit request after hitting this banner several times in the same chat. "View output logs" link wasn't captured this time — adding a "click this once you see it" instruction in the banner copy would also help close that loop.

Reported via Claude Code session (Opus 4.7, 1M context) on behalf of the user.

# Comments on anthropics/claude-code#60002
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-17T16:02:24Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/59307
2. https://github.com/anthropics/claude-code/issues/59422
3. https://github.com/anthropics/claude-code/issues/59326

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: jshaofa-ui
Date: 2026-05-17T22:09:48Z

## 🔍 Root Cause Analysis & Fix

### Problem
The VSCode extension displays `Unhandled case: [object Object]` banner during long-running sessions with MCP reconnects or large context. The `[object Object]` string reveals that an Error object is being stringified without `.message`, and the actual error is swallowed. The in-progress assistant turn never produces output but the agent-side work is complete.

### Root Cause
Three compounding issues:

1. **Error object stringification**: The error handler receives an Error-shaped object and passes it directly to a template literal or `String()` coercion, producing `[object Object]` instead of the actual error message.

2. **Response delivery path failure**: When the error fires during response streaming, the response delivery pipeline (likely a VSCode webview message channel or stream parser) enters a stuck state. The "Thinking…" spinner persists because the streaming state machine never transitions to `completed` or `error`.

3. **No error recovery**: The banner is purely cosmetic — dismissing it doesn't trigger any retry or state reconciliation. The agent-side work is done but the UI has no mechanism to surface it.

### Fix Proposal

**Layer 1: Proper Error Message Extraction**
```typescript
// Before (buggy):
showBanner(`Unhandled case: ${error}`)  // → [object Object]

// After:
const message = error instanceof Error
  ? error.message
  : typeof error === 'string'
    ? error
    : JSON.stringify(error)
showBanner(`Unhandled case: ${message}`)
```

**Layer 2: Response State Reconciliation on Banner Dismiss**
```typescript
// On banner dismiss, check if agent has completed work
onBannerDismiss(async () => {
  const pendingResponse = await agent.getPendingResponse()
  if (pendingResponse && pendingResponse.state === 'completed') {
    chatPanel.renderResponse(pendingResponse.content)
  }
})
```

**Layer 3: Streaming State Machine Guard**
Add a timeout/guard to the streaming state machine that transitions from `streaming` to `error` if no data arrives for N seconds, preventing the permanent "Thinking…" state.

### Why This Works
- Layer 1 makes the error visible for debugging
- Layer 2 recovers lost responses automatically
- Layer 3 prevents the stuck spinner from persisting indefinitely
- All three layers are independent — any one provides value

### Impact
- **Lost responses recovered**: Users no longer need to manually re-prompt
- **Debuggable errors**: Actual error messages surface for telemetry
- **No duplicate work**: Eliminates the "hello?" / "continue" re-trigger cycle

---

### Issue #58276 — [BUG]  100% CPU / frozen UI during plan mode streaming — auto-mode + fast-mode hot-loop in reactive state

State: OPEN | #58276
Labels: bug, has repro, platform:linux, area:tui, regression, perf:cpu


---



### What's Wrong?

Submitting a message while in plan mode causes the UI to freeze and the claude process to spike to 100% CPU for the entire duration of the model's streaming response. The UI recovers once 
  streaming completes, but is completely unresponsive until then.

**This makes claude code practially unusable in a linux environment**

### What Should Happen?

The UI remains responsive while the model streams a response.

### Error Messages/Logs

```shell
From ~/.claude/debug/<session>.txt, two log lines begin firing in alternating pairs at up to ~30 iterations/second starting the moment the model begins streaming:                          
   
  [auto-mode] hasAutoModeOptIn=false skipAutoPermissionPrompt: user=undefined local=undefined flag=undefined policy=undefined                                                                 
  Fast mode unavailable: Fast mode requires extra usage billing · /extra-usage to enable                                                                                                      
   
  Example excerpt (2-second window, ~50 iterations):                                                                                                                                          
                                                                                                                                                                                            
  2026-05-12T07:12:29.484Z [DEBUG] [auto-mode] hasAutoModeOptIn=false skipAutoPermissionPrompt: ...                                                                                           
  2026-05-12T07:12:29.485Z [DEBUG] Fast mode unavailable: Fast mode requires extra usage billing ...                                                                                          
  2026-05-12T07:12:29.489Z [DEBUG] [auto-mode] hasAutoModeOptIn=false skipAutoPermissionPrompt: ...                                                                                           
  2026-05-12T07:12:29.492Z [DEBUG] Fast mode unavailable: Fast mode requires extra usage billing ...                                                                                          
  ... (continues at ~25-30 pairs/second for ~6.5 minutes)                                                                                                                                     
                                                                                                                                                                                              
  The loop runs for exactly as long as the model streams — in this case from 07:12:26 to 07:18:52 (~6.5 minutes). No API errors, no crashes — the session recovers cleanly once the stream    
  ends.
```

### Steps to Reproduce

1. Have disableAutoMode set in settings (either user or project settings)                                                                                                                   
  2. Open a session in plan mode (e.g. via a CLAUDE.md that activates plan mode, or /plan)
  3. Submit a prompt that produces a long streaming response (e.g. a planning request that triggers Explore agents and a plan file write)                                                     
  4. Observe 100% CPU and frozen UI for the duration of the stream 

### Claude Model

Sonnet (default)

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

2.1.123

### Claude Code Version

2.1.126

### Platform

Anthropic API

### Operating System

Ubuntu/Debian Linux

### Terminal/Shell

Other

### Additional Information

Since this is not listed: I am using the standard Linux terminal.

I analysed the problem with claude code itself via the debug mode. Here is the claude code's hypothesis:

Root cause hypothesis                                                                                                                                                                     

  The [auto-mode] eligibility check and the fast-mode availability check appear to be subscribed to the same reactive state atom. In plan mode with disableAutoMode set, each evaluation      
  returns false but appears to schedule a state update, which triggers a re-render, which re-evaluates both subscriptions — a positive feedback loop with no debounce or memoization guard.
  Each incoming streaming token drives another render cycle, which keeps the loop spinning at token-delivery rate.                                                                            
                                                                                                                                                                                            
  Relevant startup log lines confirming the configuration:
  [WARN] auto mode disabled: disableAutoMode in settings
  [DEBUG] [auto-mode] kickOutOfAutoIfNeeded applying: ctx.mode=plan ctx.prePlanMode=undefined reason=settings

Workaround                                                                                                                                                                                  
                                                                                                                                                                                              
  None user-side. The loop terminates on its own when streaming ends.

Here is the full debug log:

[debug-log.txt](https://github.com/user-attachments/files/27627278/debug-log.txt)

# Comments on anthropics/claude-code#58276
Total: 4 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-12T08:32:31Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/29366
2. https://github.com/anthropics/claude-code/issues/51560
3. https://github.com/anthropics/claude-code/issues/26552

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: BobMali
Date: 2026-05-15T07:19:45Z

It is unlike #29366 since in that issue the freezes are putely at startup time and the cpu is idle.
It is unlike #51560 since that issue is on a different platform and the freeze is unrecoverable. In my issue the process recovers after a few minutes but pops up several times.
It is unlike #26552 since that issue occurs in the claude code part of the desktop app. My issue is concerning thr claude code cli.

--- Comment 3 ---
Author: BobMali
Date: 2026-05-19T05:57:07Z

Seriously. Claude code has become unusable this way. I am waiting 15m for a simple prompt to be processed...

--- Comment 4 ---
Author: BobMali
Date: 2026-05-19T13:57:01Z

May relate to #21567 and #18028

---

### Issue #25979 — [BUG] Claude Code hangs indefinitely when API streaming connection stalls (no read timeout)

State: OPEN | #25979
Labels: bug, api:vertex


---



### What's Wrong?

Claude Code hangs permanently when the API streaming response stalls mid-delivery. The process stays alive (epoll_wait in kernel) but makes no progress. The UI shows a spinner ("Accomplishing…",
  "Ruminating…", etc.) indefinitely. No error is surfaced. The session cannot recover — the only fix is kill -9.

  Two distinct hang patterns observed:

  Pattern 1 — Mid-turn stream freeze: The API response starts streaming (thinking block received, "thought for 3s" renders), then the stream silently stops. No more tokens arrive. The JSONL session
  log shows no new entries after the last progress update. The process is stuck waiting for bytes that never come.

  Pattern 2 — Tool result delivery stall: A Bash tool executes and completes (e.g., curl --max-time 5), but the tool result is never delivered back to the conversation state. The last tool_use ID in
  the JSONL has no matching tool_result. The UI shows the spinner as if the tool is still running.

  Both patterns correlate with background agent (Task with run_in_background: true) notifications arriving between or during turns.

### What Should Happen?

1. Claude Code should have a read timeout on the SSE/streaming HTTP response. If no data arrives within N seconds (e.g., 60–120s), it should abort the request and surface a retryable error to the
  user.
  2. Tool result delivery should have a timeout. If a tool completes but the result isn't consumed within N seconds, the session should error rather than hang.
  3. The UI should detect "no progress for N seconds" and offer the user an escape (e.g., "Session appears stuck. Press Enter to retry or Esc to cancel").

### Error Messages/Logs

```shell
Session 1: Mid-turn stream freeze (fff87be2)

  JSONL timeline:
  21:43:28 UTC  Turn 1 ends (system/turn_duration logged)
  21:43:28      Background agent notification injected as user message
                → Triggers Turn 2
  21:44:44      Turn 2 ends (system/turn_duration logged, stop hooks run)
                Background agent notification for a DIFFERENT agent arrives
                → Triggers Turn 3
                API call starts, "thought for 3s" renders in UI
                *** No more JSONL entries. Stream froze. ***
                UI stuck on "Accomplishing… (thought for 3s)" for 10+ minutes

  Process state during hang:
  $ ps -p 843072 -o pid,state,wchan
      PID S WCHAN
   843072 S do_epoll_wait

  $ kill -TERM 843072   # no effect
  $ kill -KILL 843072   # required to terminate

  Session 2: Tool result delivery stall (06d50a72)

  JSONL shows:
  Last tool_use ID:    toolu_vrtx_01JqgVUPZLrMyudEQaAQhx1x  (Bash: curl)
  Last tool_result ID: toolu_vrtx_01LJscxroh9R7tsDQUL6AhuF  (different, earlier tool)
  → Mismatch: the curl's result was never delivered

  The curl command had --max-time 5 so it completed, but the result never made it back to the conversation. UI showed "Ruminating…" indefinitely.
```

### Steps to Reproduce

Difficult to reproduce deterministically — it appears to be a race condition or network-level issue. But the following pattern triggers it frequently:

  1. Start Claude Code on a remote Linux server via SSH + tmux
  2. Give it a complex task that spawns multiple background agents (Task with run_in_background: true)
  3. Wait for background agents to complete and deliver notifications
  4. When a notification arrives right as a turn is ending or between turns, the next API call has a high chance of hanging

  Environment factors that may contribute:
  - Remote server (high-latency network path to API)
  - tmux (terminal multiplexing)
  - Multiple concurrent Claude Code sessions in different tmux panes
  - Heavy hook infrastructure (6 hook events, though all complete in <120ms per telemetry)

### Claude Model

Opus

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

2.1.40

### Claude Code Version

2.1.42

### Platform

Google Vertex AI

### Operating System

macOS

### Terminal/Shell

iTerm2

### Additional Information

Suggested fix

  Add a read timeout to the HTTP streaming client. Pseudocode:

  // In the SSE/streaming response handler:
  const STREAM_READ_TIMEOUT_MS = 120_000; // 2 minutes

  let lastDataTime = Date.now();
  stream.on('data', (chunk) => {
    lastDataTime = Date.now();
    // ... process chunk
  });

  const watchdog = setInterval(() => {
    if (Date.now() - lastDataTime > STREAM_READ_TIMEOUT_MS) {
      stream.destroy(new Error('API stream read timeout'));
      clearInterval(watchdog);
    }
  }, 10_000);

  Workaround

  External watchdog daemon that monitors JSONL session files and kills processes with no writes for >5 minutes. Available at user's request.

# Comments on anthropics/claude-code#25979
Total: 26 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-02-15T22:14:02Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/24688
2. https://github.com/anthropics/claude-code/issues/20572
3. https://github.com/anthropics/claude-code/issues/25442

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: reski-rukmantiyo
Date: 2026-02-16T00:20:05Z

I also experience the same. how to downgrade it?

--- Comment 3 ---
Author: fmallet
Date: 2026-02-27T07:43:16Z

### Experiencing the same issue — all models affected, not just Opus 4.6

**Environment:**
- macOS, Claude Code via CLI and Claude Desktop (Code tab)
- Subscription: **Max plan**
- Auth method: `claude.ai` (first-party)
- Claude Code version: 2.1.62

**Symptoms:**
- Every prompt (even trivial ones like `"are you there?"`) hangs indefinitely on spinner messages (`shlepping`, `channeling`, `pondering`…)
- Token count does not increase — no work is happening server-side
- Sending a follow-up message in the same stuck session results in **"Failed to load session"**
- Started suddenly overnight (Feb 26–27, 2026), no local changes made

**What I've verified:**

| Check | Result |
|-------|--------|
| `curl -s https://api.anthropic.com/v1/messages -o /dev/null -w "%{http_code}"` | `405` — API is reachable |
| `claude auth status` | Logged in, valid credentials |
| Deleted `~/.claude/projects/` and `~/.claude/sessions/` | No effect |
| Tested with **Opus** | Hangs |
| Tested with **Sonnet** | Hangs too |
| Tested via **CLI** | Hangs |
| Tested via **Claude Desktop Code tab** | Hangs |

**Key observation:**

This is **not limited to Opus 4.6**. Sonnet is equally affected, suggesting the streaming/SSE stall issue may be broader than initially reported.

--- Comment 4 ---
Author: jurmadani
Date: 2026-02-27T07:51:53Z

I agree with you @fmallet I have the same problem since Monday, until yesterday I got it to kinda work by interrupting him and say "continue" but now it does not work at all.

--- Comment 5 ---
Author: fmallet
Date: 2026-02-27T10:31:35Z

### Update: Resolved — corrupted `~/.claude` directory was the root cause

Following up on my previous comment. After extensive debugging, I found the fix.

### What solved it

```bash
mv ~/.claude ~/.claude.bak
claude "are you there?"
# → Works immediately
```

Removing the `~/.claude` directory and letting Claude Code recreate it from scratch resolved the issue completely.

### What did NOT help

| Attempted fix | Result |
|---------------|--------|
| Deleting `~/.claude/projects/` and `~/.claude/sessions/` | No effect |
| Updating Claude Code (2.1.45 → 2.1.62) | No effect |
| Launching from a clean directory (`/tmp/test-claude`) | Still hung |
| Testing with Sonnet instead of Opus | Still hung |

### Root cause hypothesis

The issue appears to be a corrupted state in `~/.claude/.claude.json`, likely in the `cachedGrowthBookFeatures` (feature flags cache) or related cached data. Claude Code was failing during early initialization — before even reaching the API call or producing any debug output.

### Key observation

The hang affected **all models** (Opus and Sonnet), both **CLI and Claude Desktop Code tab**, but **Chat and Cowork tabs in Claude Desktop worked fine** (they don't go through the Claude Code client).

### Suggestion for the Claude Code team

- A `claude reset` command would be very helpful for this type of situation
- The client should not hang silently when initialization fails — at minimum a timeout + error message

Hope this helps others experiencing the same issue.

--- Comment 6 ---
Author: jurmadani
Date: 2026-02-27T10:36:59Z

@fmallet You are a legend, tried your solution and it worked. I tried to debug this the whole week and could not understand what is the problem.

--- Comment 7 ---
Author: jurmadani
Date: 2026-02-27T12:36:43Z

it worked for a while then it stopped working again lol 

--- Comment 8 ---
Author: ChrisEdwards
Date: 2026-02-27T15:14:49Z

## Corroborating data from Bedrock user — 12-hour log analysis

I filed #29344 independently and was pointed here as a duplicate. My data corroborates everything in this issue, from the Bedrock side (vs your Vertex findings). Adding my analysis here since it has concrete numbers.

### Environment

- Claude Code 2.1.62
- Bedrock (`CLAUDE_CODE_USE_BEDROCK=1`)
- Model: `us.anthropic.claude-opus-4-6-v1`
- `maxOutputTokens: 64000`
- macOS Darwin 24.6.0

### Aggregate Stats (12-hour window, evening through next afternoon)

| Metric | Value |
|--------|-------|
| Sessions active in period | 24 |
| Incomplete responses (`stop_reason: null` with partial content) | **395** |
| Error entries logged for those failures | **0** |
| Stream stalls >= 3 minutes | 18 |
| Stream stalls >= 5 minutes | 14 |
| Max single stall duration | **599 seconds (~10 min)** |

**Zero errors were surfaced to the UI or logged to the session JSONL for 395 incomplete API responses.**

### Both patterns confirmed on Bedrock

**Pattern 1 — Mid-turn stream freeze** (same as OP's Pattern 1):
- Assistant began streaming `thinking` token → 552s stall → eventually resumed via system heartbeat
- Assistant streamed 89 chars of text → 599s stall → resumed via system heartbeat
- Assistant streamed 172 chars of text → 459s stall → user manually interrupted
- Assistant issued a `tool_use:Read` → 284s stall → system heartbeat broke it

**Pattern 2 — Tool result delivery stall** (same as OP's Pattern 2):
- `tool_result` delivered → 592s wait → assistant finally responded
- `tool_result` delivered → 577s wait → system heartbeat
- `tool_result` delivered → 554s wait → system heartbeat

### The 300-second heartbeat loop

Many sessions show repeating `system → system` entries at exactly 300-second intervals, sometimes 10-15+ in a row. The worst case showed **25 consecutive 300s heartbeats** spanning over 2 hours while the session appeared stuck to the user. The spinner runs the whole time with no indication anything is wrong.

### Impact

- Sessions running subagents or multi-step tasks silently stall and never recover without manual intervention
- Long-running overnight sessions accumulate stalls that waste hours
- Users have no way to distinguish "slow generation" from "dead stream" — the spinner is identical
- Only recovery is Escape/Ctrl+C and re-prompting, losing the current generation

### Key takeaway

This is not Vertex-specific — it reproduces identically on Bedrock. The core issue is that Claude Code has no client-side stream idle timeout and silently swallows incomplete responses without logging errors or surfacing them to the user.

--- Comment 9 ---
Author: ChrisEdwards
Date: 2026-02-27T15:34:52Z

FYI, I deleted my claude.json file, but that did not help.

ALSO FYI: This succeeded when run in OpenCode with the same model and thinking. So this is not a Bedrock issue.

--- Comment 10 ---
Author: mloiterman
Date: 2026-03-05T23:17:08Z

This basically renders claude useless for me.  Having to interrupt and type continue is only partially effective and it seems like it risks leaving things in an unknown state.

I've tried recreating all .claude directories and .json files, but no change.  Happens for me in remote sessions and locally.  In tmux and outside of tmux.

What additional information can be provided to accelerate this?

Using Version: 2.1.69 on a Mac locally and in Debian 12.10 remotely.

--- Comment 11 ---
Author: kolkov
Date: 2026-03-13T10:59:09Z

We reverse-engineered `cli.js` across 12 npm versions and analyzed 1,571 sessions (148,444 tool calls, 8,007 orphaned) to find the root causes of this and related hang/orphan issues.

Full analysis with code offsets and fix proposals: #33949

--- Comment 12 ---
Author: blakeley
Date: 2026-04-04T20:02:19Z

I'm still encountering this 

--- Comment 13 ---
Author: jackstine
Date: 2026-04-11T15:48:03Z

i think it has something to do with reading a large file...

Here is the session with the agent,   it says the agent is thinking,   but there is no thinking event in the session.

and this entire time it is eating tokens. the entire time,   it was reading this file for 22 minutes now

This occurs on both models opus and sonnet


[a10aa665-717e-4272-87aa-0bdb5c8c1d52.txt](https://github.com/user-attachments/files/26647142/a10aa665-717e-4272-87aa-0bdb5c8c1d52.txt)

<img width="1417" height="223" alt="Image" src="https://github.com/user-attachments/assets/f2a66109-27e3-475b-95af-1be9ad5f37b5" />

--- Comment 14 ---
Author: jackstine
Date: 2026-04-11T15:54:18Z

splitting the file into multiple files,  originally 1K lines into 5 files worked,  but it still stalled for 5 minutes on first file.

--- Comment 15 ---
Author: emmahyde
Date: 2026-04-12T14:21:50Z

This has been happening constantly this weekend.

--- Comment 16 ---
Author: 001005HS
Date: 2026-04-12T21:10:18Z

### Still reproducing on 2026-04-13 — 2+ minute Metamorphosing stall before the first server call

Adding a fresh data point since this is still happening on current Claude Code.

**Environment**
- OS: Linux 6.19.6-1-t2-noble
- Claude Code CLI, Opus 4.6 (1M context)
- Plan: paid

**Symptom** (from the top status line during a brainstorming prompt)

```
Metamorphosing… (2m 7s · ↓ 40 tokens · thought for 109s)
```

The session sat in `Metamorphosing` for **2 minutes 7 seconds** with only 40 tokens downloaded and 109 s of reported "thought" before the first server call actually went out. Only 40 tokens landed during the entire 2+ minute window, and the spinner kept running the whole time. No error, no timeout, no indication to the user that anything was wrong — identical to the patterns described earlier in this thread.

**What the user actually experiences**
- Submit a multi-step creative prompt (brainstorm user-abuse scenarios for an app).
- Status line shows `Metamorphosing…` immediately.
- Seconds tick up, token counter frozen near 0.
- 2+ minutes pass with no visible progress.
- Eventually a server call fires and work starts.
- From the user's point of view this is indistinguishable from a hang, and on longer stalls the user has already Ctrl+C'd by the time the stream would have resumed.

**Why I'm commenting here instead of a new issue**
- Searched existing issues, #25979 is the open tracking issue for this exact symptom.
- #26157 and a few others were auto-closed as duplicates of this one.
- Reports from 2026-04-11 / 2026-04-12 in this thread describe the same "spinner runs while nothing actually happens" pattern, and the kolkov cli.js analysis (#33949) proposes fixes at specific code offsets — this is still unresolved as of 2026-04-13.

**What would help end users right now**, in rough order of impact:
1. **Client-side stream-idle timeout with visible countdown** — if no tokens arrive for N seconds, surface "stream stalled, retrying…" in the UI instead of the same spinner.
2. **Automatic reconnect** on stalled SSE, not just 300 s heartbeat silent loops.
3. **Distinct status for "waiting on server" vs "receiving"** — the current `Metamorphosing` label collapses both states, which is why users cannot tell a slow generation from a dead stream.
4. **`claude reset` (or an in-session `/reset`)** that nukes `~/.claude/.claude.json` cache so users don't have to `mv ~/.claude ~/.claude.bak` by hand.

Happy to pull session logs if a specific format helps the triage team.

--- Comment 17 ---
Author: aliforia-com
Date: 2026-04-13T03:18:52Z

+1
The same problem occurred several times.

--- Comment 18 ---
Author: tigertop-c
Date: 2026-04-15T03:17:11Z

Same issue

--- Comment 19 ---
Author: yankarinRG
Date: 2026-04-16T13:30:35Z

Same issue and 73% of my weekly token wasted, thanks...

--- Comment 20 ---
Author: oscar-o-oneill
Date: 2026-04-17T16:57:00Z

I keep getting "API Error: Stream idle timeout - partial response received" in Claude Code on the web. I think it might be related to CC processing large files? Anyway, when I run the same prompt in Claude Code CLI it works fine. Hopefully Anthropic can figure it out and fix Claude Code on the web, because it's so much easier to work there.

--- Comment 21 ---
Author: mrayhanulmasud
Date: 2026-04-17T22:23:16Z

I fixed it by first running /compact in one command, then asking “please complete the code” in the next command—and it worked.


--- Comment 22 ---
Author: oscar-o-oneill
Date: 2026-04-17T22:28:53Z

@mrayhanulmasud, cool, thanks. I might try that out if it keeps happening. Another possible workaround is to just log out of Claude and log back in.

The other thing that actually worked perfectly was just using CC CLI teleport, so you can continue a web based Claude Code session in the CLI, and surprisingly enough, it works!

Just run `claude --teleport` in your terminal and open the CC web session.

--- Comment 23 ---
Author: Wiktor-P
Date: 2026-04-20T15:36:52Z

+1 — from the Remote Control side.   Framed by Claude. 

  Scenario: session hangs mid-tool-call on the host (Windows 11, Opus 4.7).
  Wall clock advances, token counter frozen. I'm away from the host, connected
  via mobile Remote Control. The only recovery path is physically walking back
  to the host to press ESC — which defeats the point of Remote Control.

  Adding a concrete UX ask on top of the programmatic interrupt already
  requested here:

  ### Remote Control "Stop" button

  A visible cancel control in the Remote Control web & mobile clients,
  mirroring the local ESC UX — active while a turn is in progress.

  - Sends the same interrupt signal as local ESC (whatever that ends up being
    once the underlying issue is fixed: SIGINT-equivalent, cancel token,
    whichever).
  - Should work even when the host is in the "frozen token counter" state
    (#44921), not only during healthy tool calls — otherwise it won't help
    the actual hang scenarios.
  - Input queue behavior: typing a new message from remote currently only
    **queues** it behind the hung turn. A Stop button would clear the queue
    or at least gate sending on successful interrupt.

  ### Why UI matters alongside the API

  The programmatic interrupt asked for above covers SDK/CI users. The mobile
  user isn't going to shell in from a phone to send a signal — they need a
  button. Shipping only the API leaves Remote Control users without a
  recovery path.

  Related:
  - #44921 (frozen token counter — the hang pattern this would recover from)
  - #17466 (local ESC also fails during active tool calls — interrupt
    mechanism itself needs work)
  - #32457 (Remote Control button-state bug — different issue but shows the
    Remote UI already has a Send/Stop state machine to build on)

--- Comment 24 ---
Author: CaptFaraday
Date: 2026-04-27T20:19:17Z

**Found a fix for the `API Error: Stream idle timeout - partial response received` error.** Adding one line to a config file resolves it for me. Full details below.

## The fix

Open `~/.claude/settings.json` and add this to the `"env"` section (create the section if it doesn't exist):

```json
"env": {
  "CLAUDE_STREAM_IDLE_TIMEOUT_MS": "1800000"
}
```

Then quit and restart Claude Code. That number is 30 minutes in milliseconds, replacing a hidden 90-second default that the client uses before assuming the connection has gone idle.

## When I was hitting it

- Claude Code v2.1.119 on Windows
- Opus 4.7 (1M context), xhigh effort, thinking enabled
- Asked Claude to write a long spec or plan in one shot
- Claude would say something like "Writing the spec now" and then go quiet for ~90 seconds before the error popped up

## What didn't work

- Turning off remote-control (`remoteControlAtStartup: false`) — same failure on local CLI
- Asking Claude to break the work into smaller chunks — didn't help reliably

## How I tracked it down

**The timing.** Opened the session log and measured every timeout. They all fired between **90.0 and 91.7 seconds** after the previous message — eight in a row. That's not random — it's a 90-second clock running out.

**The binary.** The `claude.exe` binary references `CLAUDE_STREAM_IDLE_TIMEOUT_MS` in two places. The one my stream hits defaults to 90 seconds with no minimum, so raising the env var directly raises the ceiling. The variable is real and load-bearing — it's just not in the official env-vars reference, so nobody knew it was the lever.

## Confirmation it actually works

After setting the env var to 1,800,000 and restarting:
- A 737-line spec write that had failed twice in a row went through on the first try
- A follow-up 3,518-line plan write also wrote cleanly
- Same model, same context size, same prompt — only the env var changed

## Suggestion for Anthropic

This variable is real and important but undocumented — please either add it to the env-vars reference page or raise the default. Opus 4.7 with thinking + large context easily goes silent for over 90 seconds while preparing a big tool call, and most users have no way to know what's wrong or how to fix it.

Cross-ref: #25979 (main tracking issue), #33949 (technical deep-dive).


--- Comment 25 ---
Author: datus1982
Date: 2026-04-28T22:57:10Z

See #54434 for a fresh repro with detailed mid-stream stall timing data; I added an OpenClaw-side independent confirmation here: https://github.com/anthropics/claude-code/issues/54434#issuecomment-4339679618

Same root cause as the 'no read timeout' pattern (your Pattern 1 — mid-turn stream freeze) documented in this issue, observed in a different invocation path (claude-cli spawned as a subprocess with `-p --output-format stream-json --verbose`). Patch suggested in #25979's "What Should Happen" #1 (per-chunk read timeout on SSE) is exactly the right shape.

--- Comment 26 ---
Author: danieledagnelli
Date: 2026-05-07T06:13:52Z

Same issue when running in a remote visual studio code and i close my laptop. Historically it would have continued in the background.

---

### Issue #57873 — gh release upload of large files fails with "tls: bad record MAC" through Bash sandbox proxy

State: OPEN | #57873
Labels: bug, has repro, platform:macos, area:bash, area:sandbox, stale

---

## Bug

`gh release upload` of any release asset larger than ~a few MB consistently fails with `remote error: tls: bad record MAC` when run from the Claude Code Bash tool. The same command from a regular Terminal.app (outside Claude Code's environment) succeeds with the same network and same gh credentials.

## Reproduction

1. From Claude Code's Bash tool, build any large file (e.g. a 185 MB zip)
2. Run: `gh release upload v0.X.Y build/large.zip --clobber`
3. Result: `Post "https://uploads.github.com/repos/owner/repo/releases/N/assets?...": remote error: tls: bad record MAC`

## What I tested to narrow it down

- **Small upload through same proxy**: 16-byte text file uploaded fine to the same release ✓
- **Large upload from regular Terminal.app**: succeeds (with normal proxy / no-proxy environment)
- **`gh release create` (small JSON POST)**: succeeds through same Claude Code env ✓
- **`dangerouslyDisableSandbox: true`**: still fails — proxy env vars remain set
- **`env -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY gh release upload ...`**: fails with "error connecting to api.github.com" (network requires Claude Code's proxy to reach GitHub at all)
- **Drop only `ALL_PROXY` (keep `HTTPS_PROXY`)**: same TLS error → not a SOCKS-vs-HTTP-CONNECT issue
- Pattern matches reports of similar Go HTTP client + local proxy + large streaming POST: [rclone#1893](https://github.com/rclone/rclone/issues/1893), [rclone#3338](https://github.com/rclone/rclone/issues/3338), [googleapis/google-cloud-go#1581](https://github.com/googleapis/google-cloud-go/issues/1581) — all attribute it to proxy-side buffering corrupting long TLS streams

## Diagnosis

Claude Code's local sandbox proxy (ports 65166 HTTP / 65167 SOCKS5 in my session) appears to corrupt bytes during long-running streaming HTTPS uploads, breaking TLS record MAC verification on `uploads.github.com`. Small requests through the same proxy work fine; the bug only triggers on multi-second streaming uploads.

This blocks `gh release upload` (and presumably any other Go-based tool doing chunked/streaming HTTPS uploads to allow-listed hosts) from inside Claude Code.

## Environment

- Claude Code: 2.1.138
- macOS: 26.4.1 (Darwin 25.4.0)
- gh CLI: 2.92.0
- `uploads.github.com` is in the host allowlist (small uploads pass)

## Workaround

Run `gh release upload` from a regular Terminal.app outside Claude Code.

## Suggested investigation

The Bash tool's sandbox proxy implementation — likely a Go HTTP CONNECT proxy / SOCKS5 proxy — needs to handle long-running upload streams without buffering or re-segmenting the TLS payload. This was apparently working in earlier Claude Code versions and regressed.

# Comments on anthropics/claude-code#57873
Total: 0 comments

No comments on this issue.

---

### Issue #42647 — [BUG] High Token Burn Due to Redundant Context Resubmission & Compaction Loops

State: OPEN | #42647
Labels: bug, platform:macos, area:cost, area:core, stale


---



### What's Wrong?

The current query + compaction pipeline is causing **severe token inefficiency (50K–300K+ tokens per event)** due to repeated full-context resubmissions, ineffective retry handling, and cascading compaction behavior. These issues compound under error conditions, leading to exponential token waste. See below:

### 1. Query Loop Retries Resend Full Context 
**Impact:** 50K–300K tokens per retry  

**Problem:**
- The main `while (true)` query loop resends the entire message history, system prompt, and tool schemas on every retry.
- Retries are triggered by:
  - prompt-too-long errors  
  - max-output-token limits  
  - streaming/media failures  
  - compaction failures  
- No deduplication or reuse of unchanged context.

**Fix:**
- Track whether context has changed between iterations.
- Introduce a `contextHash`:
  - Compute hash of serialized messages + system prompt + tools.
  - Compare before each API call.
- If the hash is unchanged:
  - Skip the API call or apply backoff instead of resending.
- Add an early-exit condition:
  - If retry is triggered but context has not grown/changed, do not reserialize or resend.

---

### 2. Autocompact Cascade Uses Full Context
**Impact:** 100–200K tokens per compaction (up to 3× per turn)

**Problem:**
- Autocompact triggers at ~187K tokens and submits the **entire bloated context** for summarization.
- The loop can trigger repeatedly (up to `MAX_CONSECUTIVE_AUTOCOMPACT_FAILURES`).
- No validation that compaction meaningfully reduces token count.
- Can immediately re-enter compaction after finishing.

**Fix:**
- Trigger compaction earlier:
  - At ~70–75% of context window instead of near max capacity.
- Enforce a minimum reduction threshold:
  - Require ≥30% token reduction; otherwise treat as failure and abort cascade.
- After compaction:
  - Recalculate token count before re-entering query loop.
  - Prevent immediate re-trigger unless new tokens exceed threshold again.
- Add guard against cascading:
  - Limit consecutive compactions more aggressively or introduce cooldown between attempts.

---

### 3. Streaming Fallback Duplicates Full Requests 
**Files:**  
**Impact:** 50–200K tokens per fallback  

**Problem:**
- On streaming failure (e.g., 529 errors), system falls back to non-streaming mode.
- The fallback resends the entire message array from scratch.
- Partial streamed output is discarded.

**Fix:**
- Implement resume-from-checkpoint:
  - Capture partial streamed tokens before failure.
  - Append them to context for retry instead of restarting.
- Retry streaming before fallback:
  - Add exponential backoff for transient failures.
- Add deduplication:
  - If the same `contextHash` is about to be resent within the same turn, delay or skip retry.
- Only fallback to non-streaming after multiple streaming retries fail.

---

### 4. Tool List Changes Invalidate Prompt Cache 
**Impact:** 50–200K tokens per cache bust  

**Problem:**
- Deferred tool updates prepend a new message mid-turn.
- This invalidates prompt caching, forcing full context reprocessing.
- Even minor differences (e.g., ordering) trigger cache busts.

**Fix:**
- Batch tool list updates:
  - Apply only at turn boundaries, not mid-turn.
- Normalize tool definitions:
  - Sort tools alphabetically before serialization.
  - Ensure stable formatting to prevent unnecessary diffs.
- Add change detection:
  - Compare new tool list against previous version.
  - Skip reinsertion if there is no meaningful change.
- Avoid prepending new messages unless strictly required.

---

## Combined Effect
These issues amplify each other:
- Retry loops + streaming fallback → duplicate full requests  
- Compaction loops → repeated large summarization calls  
- Tool updates → cache invalidation → no reuse of prior computation  

**Result:** Massive, avoidable token burn and degraded performance under load or failure scenarios.



### What Should Happen?

Implementing these fixes should:
- Reduce token usage per retry/failure by **50–90%**
- Eliminate redundant full-context resubmissions
- Prevent cascading compaction loops
- Improve latency and overall system stability
- Significantly reduce API costs

### Error Messages/Logs

```shell

```

### Steps to Reproduce

1. Run 'claude'
2. Prompt and observe abnormally high token consumption

### Claude Model

None

### Is this a regression?

No, this never worked

### Last Working Version

_No response_

### Claude Code Version

2.1.9

### Platform

Anthropic API

### Operating System

macOS

### Terminal/Shell

Terminal.app (macOS)

### Additional Information

_No response_

# Comments on anthropics/claude-code#42647
Total: 5 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-04-02T15:59:25Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/41198
2. https://github.com/anthropics/claude-code/issues/24179
3. https://github.com/anthropics/claude-code/issues/42055

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: Camj78
Date: 2026-04-09T16:19:02Z

Yeah this thread is super interesting. I think what’s making it feel worse than expected is that it’s not just one thing going wrong, it’s a few separate behaviors stacking on top of each other.

From what I’ve seen, there are at least a couple different loops happening.

One is when a retry happens without any meaningful context change, but the system still reprocesses everything instead of reusing prior work.

Another is compaction kicking in, but not actually reducing enough to stop the next compaction trigger, so it kind of cascades instead of stabilizing.

And then on top of that, if anything falls back to a “from scratch” path, like streaming or partial failure cases, you basically lose any benefit from previous turns and pay for the full context again.

Individually those aren’t too bad, but when they line up in the same session it can feel like usage just spikes out of nowhere.

Curious if what you’re seeing looks more like a steady ramp over a few turns, or sudden jumps on specific retries?

--- Comment 3 ---
Author: ian038
Date: 2026-04-09T16:26:05Z

Exactly, it's a bunch of behaviors all at once. For me specifically, I see it with bigger jumps over a few turns.  

--- Comment 4 ---
Author: Camj78
Date: 2026-04-09T18:28:21Z

Yeah that pattern usually ends up being a mix of accumulation + occasional full replays.

The steady growth is just the conversation getting longer, but the jumps tend to happen when something forces the system to rebuild the full context for a turn (retry, tool call replay, cache miss, etc).

So instead of incremental adds you suddenly pay for the entire history again on that step.

If you look closely you’ll probably see those jumps line up with specific events rather than random turns.

--- Comment 5 ---
Author: junaidtitan
Date: 2026-05-13T13:13:18Z

This compaction loop problem is brutal on token budgets. I wrote [Cozempic](https://github.com/Ruya-AI/cozempic) specifically to prevent this — its guard daemon monitors session size with 4 thresholds and prunes proactively using 18 strategies (tool-result-age, thinking-blocks, metadata-strip, etc.) so compaction either never triggers or has far less to work with. The compact-summary-collapse strategy alone saves 85-95%. `pip install cozempic && cozempic guard` to run it alongside your session. Would love to know if it reduces your token burn.

---

### Issue #44907 — [DOCS] SDK/print mode docs omit interrupted partial response persistence

State: OPEN | #44907
Labels: documentation, area:docs


---

### Documentation Type

Missing documentation (feature not documented)

### Documentation Location


https://code.claude.com/docs/en/headless

### Section/Topic


`Stream responses` and `Continue conversations` for `claude -p` sessions

### Current Documentation


The docs currently say:

> "Use `--output-format stream-json` with `--verbose` and `--include-partial-messages` to receive tokens as they're generated. Each line is a JSON object representing an event:"

> "Use `--continue` to continue the most recent conversation, or `--resume` with a session ID to continue a specific conversation."

The Agent SDK session docs also say:

> "A session is the conversation history the SDK accumulates while your agent works. It contains your prompt, every tool call the agent made, every tool result, and every response."

> "Returning to a session means the agent has full context from before: files it already read, analysis it already performed, decisions it already made. You can ask a follow-up question, recover from an interruption, or branch off to try a different approach."

And the Python SDK interrupt example says:

> "`interrupt()` sends a stop signal but does not clear the message buffer. Messages already produced by the interrupted task, including its `ResultMessage` (with `subtype="error_during_execution"`), remain in the stream."

None of these pages explain whether assistant text that was already emitted before an SDK or `claude -p` interruption is persisted into the saved conversation history.

### What's Wrong or Missing?


### A. The interrupted-stream persistence behavior is undocumented

The docs explain streaming output, session resume, and interrupt handling separately, but they do not state what happens when a response is interrupted mid-stream after partial assistant text has already been emitted.

### B. Resume and transcript behavior are ambiguous for SDK/print-mode users

Today the docs promise that sessions contain "every response" and that users can recover from interruptions, but they never clarify whether partially streamed assistant output is durable session history or only ephemeral stream output.

Changelog v2.1.94 explicitly fixed this behavior: SDK/print mode now preserves the partial assistant response in conversation history when interrupted mid-stream. That makes this a supported behavior users can rely on, but the current docs do not describe it.

### Suggested Improvement


Add a short note to the headless and Agent SDK session/streaming docs that explains:

1. If an SDK or `claude -p` streaming response is interrupted after assistant text has started, the already-generated assistant text is preserved in the session's conversation history.
2. Resuming the session (`--continue`, `--resume`, or SDK resume) continues from that preserved history rather than treating the partial output as lost.
3. This applies to saved session/transcript history, which is distinct from raw `stream_event` chunks emitted during live streaming.

Suggested placement:

- In `Run Claude Code programmatically`, directly after `Stream responses` or `Continue conversations`
- In `Work with sessions`, near the "recover from an interruption" guidance
- In `Stream responses in real-time`, as a note clarifying what is persisted if streaming is interrupted

### Impact

Medium - Makes feature difficult to understand

### Additional Context


**Affected Pages:**

| Page | Context |
|------|---------|
| https://code.claude.com/docs/en/headless | `claude -p` streaming output and resume behavior |
| https://code.claude.com/docs/en/how-claude-code-works | Session continuity and restored conversation history |
| https://platform.claude.com/docs/en/agent-sdk/sessions | Session contents and interruption recovery |
| https://platform.claude.com/docs/en/agent-sdk/streaming-output | Partial-message streaming and message flow |
| https://platform.claude.com/docs/en/agent-sdk/python | `interrupt()` buffer behavior example |

**Total scope:** 5 pages affected

**Source:** Changelog v2.1.94

**Changelog entry:** `Fixed SDK/print mode not preserving the partial assistant response in conversation history when interrupted mid-stream`

# Comments on anthropics/claude-code#44907
Total: 2 comments

--- Comment 1 ---
Author: coygeek
Date: 2026-05-08T06:18:42Z

Checked the current docs on 2026-05-07. This documentation gap is still unresolved.

--- Comment 2 ---
Author: coygeek
Date: 2026-05-23T01:00:27Z

checked docs, not resolved yet

---

### Issue #47962 — [BUG] IME pre-edit buffer cleared by UI redraws during candidate selection — McBopomofo / 小麥注音, macOS, iTerm2

State: OPEN | #47962
Labels: bug, has repro, platform:macos, area:tui, area:a11y, stale


---

## What's Wrong?

When typing Chinese via an IME in Claude Code, **the pre-edit buffer is destroyed by UI redraws during the uncommitted composition phase** — after phonetic input is complete but before the user has finalized which characters to commit.

Concrete example with McBopomofo (小麥注音): I type `ㄔㄥˊ ㄕˋ`. McBopomofo uses **inline pre-edit rendering** — it shows the top-guess characters directly in the composition area (e.g. "程式") without a floating candidate popup. From here I can cycle through alternative homophones (e.g. 城市, 成事) **using the up/down arrow keys**, or press Enter to commit the current choice. If the assistant emits any new token before I commit, the entire pre-edit is wiped — typed Zhuyin input and current candidate both gone.

This is different from #43381 (characters invisible during typing). In my case, characters DO render inline while typing — the bug is that composition state isn't preserved across redraws while I'm still selecting among homophones.

## What Should Happen?

The IME pre-edit buffer should survive assistant-driven redraws. Composition should only end on explicit user action: `compositionend` (commit via Enter / Space / number selection) or cancel (Esc). This is how readline, vim, and every modern TUI behave.

## Steps to Reproduce

1. macOS with **McBopomofo** (小麥注音, https://mcbopomofo.openvanilla.org/) as the active input source.
2. Launch `claude` in iTerm2.
3. Send a prompt that produces a long streaming response (e.g. `write a 500-word essay`).
4. While Claude is streaming, in McBopomofo type `ㄔㄥˊㄕˋ` — a homophone resolving to 程式 (program) / 城市 (city) / 成事 (succeed). Leave the pre-edit uncommitted (do **not** press Enter; **cycle candidates via up/down arrow keys**).
5. Observe: on the next assistant-driven redraw, the pre-edit is wiped. Input field is empty again.

**Expected:** Pre-edit survives redraws; I can pick 程式 vs 城市 on my own schedule.
**Actual:** Composition state destroyed mid-selection; typed input lost.

## Environment

- Claude Code: 2.1.107
- macOS: 15.7.4 (Sequoia, Apple Silicon)
- Terminal: iTerm2 3.6.9
- Shell: zsh
- IME: **McBopomofo 小麥注音** (popular third-party Zhuyin IME in Taiwan)
- Likely also affects: macOS native 注音 / 拼音, and any CJK IME that uses a pre-edit composition buffer.

## Impact / Use Case

The primary workflow this breaks: **while Claude is streaming a response, I want to compose my next prompt so I'm ready to send the moment the assistant finishes — making use of the otherwise-idle waiting time.** This is a natural productivity pattern in any chat UI.

For CJK IME users this is impossible. Every streamed token triggers a redraw that destroys my in-progress composition while I'm still cycling candidates. The only options are:

- (a) Sit idle while Claude works, then start typing from scratch after the stream ends — wasted time on every turn.
- (b) Compose in another app and paste — defeats the interactive CLI UX.

English users don't hit this because each keystroke commits immediately. **CJK IME users pay this tax every single turn.**

## Additional Context

- Trigger is UI redraw, not keystroke handling. Typing keys alone works fine — it's assistant output that destroys the composition.
- macOS built-in Dictation has the same symptom on CJK layouts (dictation writes into the same pre-edit buffer, gets wiped by redraws).
- Only reliable workaround: compose Chinese in another app, then paste. Defeats interactive CLI UX.

# Comments on anthropics/claude-code#47962
Total: 3 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-04-14T15:12:00Z

Found 1 possible duplicate issue:

1. https://github.com/anthropics/claude-code/issues/41772

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: hyj1116
Date: 2026-04-14T21:20:25Z

Related to #41772 — both bugs share the same root cause: Claude Code's TUI does not detect active IME composition state. #41772 is triggered by ESC (incorrectly interrupts Claude instead of canceling IME), while this issue is triggered by streaming output redraws (composition buffer wiped). Fixing the IME composition detection at the TUI layer would likely address both.

--- Comment 3 ---
Author: ciao-chung
Date: 2026-04-29T01:01:05Z

Confirming the same bug is also triggered by permission prompts, not just streaming output. On macOS with the built-in Zhuyin IME, when a tool call requires approval 
and Claude Code shows the permission prompt, the in-progress IME pre-edit buffer is wiped — same symptom as the streaming case described above. English typing in the   
same input field survives the prompt fine; only IME composition is lost. So the underlying redraw path triggered by the permission UI shares this bug, which means even 
non-streaming, idle moments aren't safe for CJK composition.         
                                                                                                                                          
Environment: Claude Code CLI on macOS (Darwin 25.3.0), zsh, macOS native Zhuyin / Pinyin IME.

---

### Issue #59575 — [FEATURE] Autoscroll toggle

State: OPEN | #59575
Labels: enhancement, platform:vscode, area:ui


---



### Problem Statement

When interacting with Claude VS Code chat window, the constant scrolling of the window makes it difficult to read. Scrolling up slightly to stop the auto scrolling is inconvenient given how much back and forth there is with Claude during a session. 

### Proposed Solution

I would like to have a  "disable autoscroll" toggle in the Claude settings which when enabled would not autoscroll ever and always requires manual scrolling. This makes it much easier for the user to read, scroll, read rather than having to first scroll up every time to stop auto scroll.

### Alternative Solutions

Type question, press enter, immediately scroll back up the chat a bit, wait and then scroll down and read.

### Priority

Medium - Would be very helpful

### Feature Category

Interactive mode (TUI)

### Use Case Example

1. I open a new chat with Claude and type a question, press enter.
2. Claude returns answers
3. I scroll at my own pace, just like I do with any website or e-book

### Additional Context

_No response_

# Comments on anthropics/claude-code#59575
Total: 1 comments

--- Comment 1 ---
Author: chrisheiser-boop
Date: 2026-05-21T15:36:18Z

I totally agree with adding this feature - my feeling is if Claudette wrote something in the response, it was meant for me to read, so I should start at the top of the response and read down.  Here is Claudette's response to my question if she can turnoff auto-scroll, she recommended I submit a feature request.  (I have a co-worker that refers to his Claude Code as he.  I feel my Claude is a female, so I call her Claudette)

"No known setting for that in Claude Code — the auto-scroll is baked into how the streaming response works in the VS Code webview panel, and I'm not aware of any option to disable it.

You should absolutely read top-to-bottom — that's the intended order. The auto-scroll is just a side effect of the response streaming in line by line; it drags the view down as I write."

---

### Issue #61717 — [BUG] Big input covering claude answer in claude code vscode extension

State: OPEN | #61717
Labels: bug


---



### What's Wrong?

If you enter a message bigger than 50 lines, you cant minimize the input and claude starts answering behind your input tab

<img width="949" height="295" alt="Image" src="https://github.com/user-attachments/assets/5f49c2c3-2dbc-471a-9f7b-75565c8edcb1" />

Making impossible to even know what claude answered or edited because its behing the input balloon

### What Should Happen?

Claude asnwer gets covered by input balloon

### Error Messages/Logs

```shell
Dont have any
```

### Steps to Reproduce

1. Paste a message with 50 lines or more in claude code vscode extension
2. Claude answer should be covered by the input balloon, and you cant minimize it

### Claude Model

Not sure / Multiple models

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

_No response_

### Claude Code Version

2.1.145

### Platform

Anthropic API

### Operating System

Windows

### Terminal/Shell

Other

### Additional Information

_No response_

# Comments on anthropics/claude-code#61717
Total: 3 comments

--- Comment 1 ---
Author: giruuuuj
Date: 2026-05-23T10:42:48Z

## Analysis

This is a VS Code extension UI layout bug. The chat input balloon has no maximum height limit and no auto-collapse behavior when the response starts streaming. With 50+ line inputs, the balloon expands past the viewport and covers the response area.

### Likely cause

The input component lacks:
- A `max-height` CSS property with overflow scroll
- Auto-collapse/minimize on submit or when response starts streaming
- A manual collapse button when input exceeds a certain height

### Workarounds

1. **Split large inputs** — send messages in smaller chunks (under ~20 lines)
2. **Use the CLI** — the CLI's terminal input handles multiline differently:
   ```bash
   claude "your very long message here"
   ```
3. **Submit quickly** — press Ctrl+Enter immediately after pasting, before the response starts, to reclaim viewport space

### Fix needed (VS Code extension team)

1. Add `max-height: 40vh; overflow-y: auto` to the input balloon
2. Auto-collapse input to a single-line bar when Claude starts responding
3. Add a minimize/collapse button to the input balloon


--- Comment 2 ---
Author: florentinap
Date: 2026-05-28T04:02:22Z

I think it would help to add an issue to VS Code: https://github.com/microsoft/vscode/issues. 

--- Comment 3 ---
Author: jakinharp
Date: 2026-05-28T16:51:02Z

Cheap _workaround_ while issue persists: Append this line to 50+ line input.
"// REQUIRED ACTION: you must only reply "ok" to this message. then after I respond "continue" should you process this input."

This works because new input balloons don't get covered.

Flow:
- Submit message
- Wait ~5 seconds (only needs to process the "ok" message)
- Send "continue"

---

### Issue #61983 — Hook event for assistant text completion before tool dispatch (preamble invisible to PreToolUse)

State: OPEN | #61983
Labels: enhancement, area:hooks


---

## Feature request

Add a hook event that fires after an assistant text content block finishes streaming and before the next tool call is dispatched — or, equivalently, add a `preceding_text` (or `current_message_text`) field to the `PreToolUse` hook payload containing the assistant text emitted earlier in the same turn.

## Problem

When the assistant emits preamble text and then calls a tool in the same turn, sidecars/integrations that hook on `PreToolUse` cannot see that preamble:

1. The preamble has not yet been flushed to `transcript_path` when `PreToolUse` fires — reading the JSONL at that moment returns the prior turn's content.
2. No hook payload field carries the in-flight assistant text.
3. `PostToolUse` / `Stop` are too late for sidecars that render UI alongside the tool call itself (e.g., a custom UI for `AskUserQuestion`).

This is especially painful for `AskUserQuestion`: the model's preamble text often contains the *why* of the question, but the UI rendering the question can't access it. Users see a question without context.

## Hook events checked (none expose in-flight text)

`PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Notification`, `Stop`, `SubagentStop`, `PreCompact`, `SessionStart`, `SessionEnd` — all receive `tool_name`/`tool_input`/`transcript_path`/`session_id`, but none carry the assistant message currently being streamed.

## Proposed solutions (either would unblock)

**A. New hook event: `AssistantTextComplete`** — fires after each `content_block_stop` for a `text` block, before the next `tool_use` block is dispatched. Payload includes the completed text and the in-flight `message_id`.

**B. Augment `PreToolUse`** — add a `preceding_text` field containing all assistant text content blocks emitted in the current turn before this tool call.

(B) is the smaller change and solves the immediate use case. (A) is more general and would also unblock streaming sidecars, live transcripts, partial-message indexers, etc.

## Use cases

- Sidecar UIs rendering `AskUserQuestion` with the preamble as context.
- External logging/observability tools that want to capture assistant reasoning before each tool call.
- Live transcript mirrors (the existing `includePartialMessages` SDK request — anthropics/claude-code#41732 — is the SDK-side equivalent).

## Workarounds today

- Prompt the model to embed preamble inside `tool_input` (e.g., AskUserQuestion `description`). Brittle, relies on model compliance, doesn't help other tools.
- Long-running daemon tailing `transcript_path`. Still races flush timing, and isn't a hook.

## Related

- anthropics/claude-code#41732 — V2 persistent sessions should support `includePartialMessages` for streaming (SDK-side request for the same underlying signal).

# Comments on anthropics/claude-code#61983
Total: 1 comments

--- Comment 1 ---
Author: jshaofa-ui
Date: 2026-05-24T13:17:24Z

# Solution: Hook Event for Assistant Text Completion Before Tool Dispatch

**Issue:** [#61983](https://github.com/anthropics/claude-code/issues/61983)
**Title:** Hook event for assistant text completion before tool dispatch (preamble invisible to PreToolUse)
**Priority:** High — zero competition, $2,000–$5,000 bounty
**Status:** Proposed Solution

---

## 1. Problem Analysis

When Claude Code's assistant emits preamble text followed by a tool call in the same turn (e.g., "Let me look that up for you" → `Bash` tool), the `PreToolUse` hook receives no access to that preamble text. This creates a blind spot for:

1. **Sidecar UIs** (e.g., custom `AskUserQuestion` renderers) that need the "why" behind a question
2. **Observability tools** that want to capture assistant reasoning before each tool call
3. **Live transcript mirrors** that need in-flight message content

### Root Cause

The hook dispatch pipeline fires `PreToolUse` at the moment a `tool_use` content block is encountered in the streaming response. At that point:
- The text content block has been streamed but not yet flushed to `transcript_path`
- No hook payload field carries the in-flight assistant text
- `PostToolUse` and `Stop` events fire too late for real-time UI rendering

### Current Hook Payload (PreToolUse)

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/dir",
  "permission_mode": "allow",
  "hook_event_name": "PreToolUse",
  "tool_name": "AskUserQuestion",
  "tool_input": { "question": "..." }
}
```

**Missing:** Any field containing the assistant's preamble text from the current turn.

---

## 2. Proposed Solution: Dual Approach

Implement **both** proposed solutions from the issue, as they serve complementary use cases:

### Solution A: New `AssistantTextComplete` Hook Event (General)

A new hook event that fires after each `content_block_stop` for a `text` content block, before any subsequent `tool_use` block is dispatched.

### Solution B: Augment `PreToolUse` with `preceding_text` Field (Minimal Change)

Add a `preceding_text` field to the existing `PreToolUse` payload containing all assistant text content blocks emitted in the current turn before this tool call.

---

## 3. Architecture & Implementation

### 3.1 Event Flow Diagram

```
Current Flow:
  Assistant Stream → [text block] → [tool_use block] → PreToolUse fires
                                        ↑
                                  Problem: text already passed, not captured

Proposed Flow:
  Assistant Stream → [text block] → AssistantTextComplete fires → [tool_use block] → PreToolUse fires (with preceding_text)
                                        ↑                                        ↑
                                  New event captures text              Existing event augmented
```

### 3.2 New Hook Event: `AssistantTextComplete`

**Event Name:** `AssistantTextComplete`

**When it fires:** After each `content_block_stop` event where the block type is `text`, and before the next content block (if it's a `tool_use`) begins processing.

**Hook Input Payload:**

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/dir",
  "hook_event_name": "AssistantTextComplete",
  "message_id": "msg_12345",
  "content_block_index": 0,
  "text": "Let me look that up for you. I'll check the current weather in San Francisco.",
  "turn_id": "turn_67890"
}
```

**Hook Output (optional):**

```json
{
  "continue": true,
  "suppressOutput": false,
  "systemMessage": "Text captured for sidecar UI"
}
```

**Exit Codes:**
- `0` — Success, continue processing
- `2` — Block further processing (stderr shown to Claude)

### 3.3 Augmented `PreToolUse` Payload

Add two new fields to the existing `PreToolUse` input:

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/dir",
  "permission_mode": "allow",
  "hook_event_name": "PreToolUse",
  "tool_name": "AskUserQuestion",
  "tool_input": { "question": "..." },
  "preceding_text": "Let me look that up for you. I'll check the current weather in San Francisco.",
  "preceding_text_blocks": [
    {
      "content_block_index": 0,
      "text": "Let me look that up for you."
    },
    {
      "content_block_index": 1,
      "text": "I'll check the current weather in San Francisco."
    }
  ]
}
```

### 3.4 Implementation Details

#### File: `src/hooks/event-dispatcher.ts` (new or modified)

```typescript
interface AssistantTextCompletePayload {
  session_id: string;
  transcript_path: string;
  cwd: string;
  hook_event_name: 'AssistantTextComplete';
  message_id: string;
  content_block_index: number;
  text: string;
  turn_id: string;
}

interface PreToolUsePayload {
  session_id: string;
  transcript_path: string;
  cwd: string;
  permission_mode: string;
  hook_event_name: 'PreToolUse';
  tool_name: string;
  tool_input: Record<string, unknown>;
  // NEW FIELDS
  preceding_text: string;
  preceding_text_blocks: Array<{
    content_block_index: number;
    text: string;
  }>;
}
```

#### File: `src/streaming/content-block-handler.ts` (modified)

```typescript
// Track accumulated text blocks within the current turn
class TurnState {
  private textBlocks: Array<{ index: number; text: string }> = [];
  private messageId: string;
  private turnId: string;

  onContentBlockStop(block: ContentBlockStop): void {
    if (block.content_block.type === 'text') {
      this.textBlocks.push({
        index: block.index,
        text: block.content_block.text,
      });

      // Fire AssistantTextComplete event
      this.dispatcher.dispatch('AssistantTextComplete', {
        session_id: this.sessionId,
        transcript_path: this.transcriptPath,
        cwd: process.cwd(),
        hook_event_name: 'AssistantTextComplete',
        message_id: this.messageId,
        content_block_index: block.index,
        text: block.content_block.text,
        turn_id: this.turnId,
      });
    }
  }

  onToolUseStart(block: ToolUseBlockStart): PreToolUsePayload {
    const precedingText = this.textBlocks.map(b => b.text).join('\n');

    return {
      session_id: this.sessionId,
      transcript_path: this.transcriptPath,
      cwd: process.cwd(),
      permission_mode: this.permissionMode,
      hook_event_name: 'PreToolUse',
      tool_name: block.name,
      tool_input: block.input,
      preceding_text: precedingText,
      preceding_text_blocks: [...this.textBlocks],
    };
  }

  reset(): void {
    this.textBlocks = [];
  }
}
```

#### File: `src/hooks/hook-registry.ts` (modified)

Register the new event type in the hook event enum:

```typescript
// Add to HookEventName union/type
type HookEventName =
  | 'PreToolUse'
  | 'PostToolUse'
  | 'Stop'
  | 'SubagentStop'
  | 'SessionStart'
  | 'SessionEnd'
  | 'UserPromptSubmit'
  | 'PreCompact'
  | 'Notification'
  | 'AssistantTextComplete';  // NEW
```

#### File: `src/config/hook-schema.json` (modified)

Add schema validation for the new event:

```json
{
  "AssistantTextComplete": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "matcher": { "type": "string", "default": "*" },
        "hooks": {
          "type": "array",
          "items": { "$ref": "#/definitions/HookDefinition" }
        }
      },
      "required": ["hooks"]
    }
  }
}
```

### 3.5 Environment Variable Support

For command hooks, expose the text via environment variables:

```bash
# Available in AssistantTextComplete hooks:
$ASSISTANT_TEXT          # The completed text content
$CONTENT_BLOCK_INDEX     # Index of the content block
$MESSAGE_ID             # The message ID
$TURN_ID                 # The turn ID

# Available in PreToolUse hooks (new):
$PRECEDING_TEXT          # All preamble text before this tool call
```

---

## 4. Configuration Examples

### 4.1 Using `AssistantTextComplete` for Sidecar UI

```json
{
  "hooks": {
    "AssistantTextComplete": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/capture-preamble.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### 4.2 Using `preceding_text` in PreToolUse for AskUserQuestion

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "AskUserQuestion",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/render-with-context.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

Hook script (`render-with-context.py`):

```python
import json, sys

input_data = json.load(sys.stdin)
preceding_text = input_data.get("preceding_text", "")
tool_input = input_data.get("tool_input", {})

# Render the question WITH the preamble context
question = tool_input.get("question", "")
print(json.dumps({
    "hookSpecificOutput": {
        "permissionDecision": "allow"
    },
    "systemMessage": f"Context: {preceding_text}\nQuestion: {question}"
}))
```

---

## 5. Backward Compatibility

- **Fully backward compatible**: Existing hooks continue to work unchanged
- The `preceding_text` and `preceding_text_blocks` fields are additive to `PreToolUse`
- `AssistantTextComplete` is a new event that only fires if configured
- No breaking changes to existing hook payloads

---

## 6. Testing Plan

### 6.1 Unit Tests

```typescript
describe('AssistantTextComplete', () => {
  it('fires after text content block stop', async () => {
    const events: string[] = [];
    const handler = new ContentBlockHandler({
      onEvent: (name) => events.push(name),
    });

    handler.onContentBlockStart({ type: 'text', index: 0 });
    handler.onContentBlockDelta({ type: 'text_delta', delta: { text: 'Hello' } });
    handler.onContentBlockStop({ type: 'text', index: 0 });

    expect(events).toContain('AssistantTextComplete');
  });

  it('does not fire for tool_use blocks', async () => {
    const events: string[] = [];
    const handler = new ContentBlockHandler({ onEvent: (name) => events.push(name) });

    handler.onContentBlockStart({ type: 'tool_use', name: 'Bash', input: {}, index: 0 });
    handler.onContentBlockStop({ type: 'tool_use', index: 0 });

    expect(events).not.toContain('AssistantTextComplete');
  });
});

describe('PreToolUse preceding_text', () => {
  it('includes text blocks before tool_use', async () => {
    const state = new TurnState();
    state.onContentBlockStop({ type: 'text', index: 0, content_block: { text: 'Let me check.' } });
    state.onContentBlockStop({ type: 'text', index: 1, content_block: { text: 'I will run a command.' } });

    const payload = state.onToolUseStart({ name: 'Bash', input: { command: 'ls' } });

    expect(payload.preceding_text).toBe('Let me check.\nI will run a command.');
    expect(payload.preceding_text_blocks).toHaveLength(2);
  });

  it('returns empty string when no text precedes tool_use', async () => {
    const state = new TurnState();
    const payload = state.onToolUseStart({ name: 'Bash', input: { command: 'ls' } });

    expect(payload.preceding_text).toBe('');
    expect(payload.preceding_text_blocks).toHaveLength(0);
  });
});
```

### 6.2 Integration Tests

1. **Test: Preamble captured in PreToolUse**
   - Run Claude Code with a hook on `PreToolUse`
   - Trigger a response with preamble + tool call
   - Verify `preceding_text` contains the preamble

2. **Test: AssistantTextComplete fires in correct order**
   - Configure hooks on both `AssistantTextComplete` and `PreToolUse`
   - Verify `AssistantTextComplete` fires before `PreToolUse`
   - Verify text content is accurate

3. **Test: Multiple text blocks**
   - Response with multiple text blocks before tool call
   - Verify all blocks are captured in `preceding_text_blocks`

4. **Test: No preamble (direct tool call)**
   - Response with immediate tool call, no preamble
   - Verify `preceding_text` is empty string (not null/undefined)

### 6.3 Manual Testing

```bash
# Test with debug mode
claude --debug

# Configure hooks to capture events
cat > .claude/settings.json << 'EOF'
{
  "hooks": {
    "AssistantTextComplete": [
      {
        "matcher": "*",
        "hooks": [{ "type": "command", "command": "cat >> /tmp/assistant-text.log" }]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "*",
        "hooks": [{ "type": "command", "command": "cat >> /tmp/pretooluse.log" }]
      }
    ]
  }
}
EOF

# Ask Claude to do something that produces preamble + tool call
# "Look at the files in the current directory"
# Verify /tmp/assistant-text.log and /tmp/pretooluse.log contain expected data
```

---

## 7. Performance Considerations

- **Minimal overhead**: Text accumulation is an in-memory append operation (O(n) where n = number of text blocks, typically < 5)
- **No I/O in hot path**: Text is accumulated in memory, not written to disk
- **Hook execution**: `AssistantTextComplete` hooks run in parallel with existing hooks (no additional serialization)
- **Memory**: Text blocks are cleared on turn reset, no memory leak risk

---

## 8. Edge Cases

| Edge Case | Handling |
|-----------|----------|
| No text before tool call | `preceding_text` = `""`, `preceding_text_blocks` = `[]` |
| Multiple text blocks | All captured in order, joined with `\n` |
| Text after tool call | Not included (only preceding text) |
| Empty text block | Still fires `AssistantTextComplete`, text = `""` |
| Streaming interruption | Partial text captured at last completed block |
| Subagent text | Handled by `SubagentStop` event (separate concern) |
| Tool use without assistant text (direct) | `preceding_text` empty, hook still fires normally |

---

## 9. Deliverables

1. **Schema changes** — `hook-schema.json` updated with `AssistantTextComplete` event
2. **Type definitions** — TypeScript interfaces for new payload fields
3. **Event dispatcher** — `AssistantTextComplete` dispatch logic in content block handler
4. **Payload augmentation** — `preceding_text` and `preceding_text_blocks` in `PreToolUse`
5. **Documentation** — Updated hooks documentation with new event
6. **Tests** — Unit tests, integration tests, and manual test scripts
7. **Example hooks** — Working hook scripts demonstrating both solutions

---

## 10. Risk Assessment

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Hook execution order dependency | Low | Document that hooks run in parallel; use `preceding_text` for ordering guarantees |
| Performance regression | Very Low | Text accumulation is O(n) with small n; no I/O |
| Breaking existing hooks | Very Low | New fields are additive; new event only fires if configured |
| Memory leak from accumulated text | Very Low | Text blocks cleared on turn reset |

---

## 11. Conclusion

This solution provides **two complementary mechanisms** to solve the preamble visibility problem:

1. **`AssistantTextComplete`** — A general-purpose event for streaming sidecars, live transcripts, and partial-message indexers
2. **`preceding_text` in `PreToolUse`** — A minimal, targeted fix for the most common use case (sidecar UIs rendering tool calls with context)

Both are backward compatible, low-risk, and directly address the issue's requirements. The implementation touches a small, well-defined area of the codebase (content block handling and hook dispatch), making it straightforward to implement and maintain.

---

### Issue #57919 — [BUG] claude-agent-acp: streaming loop hangs on missing session_state_changed:idle (stop button stuck) — UPDATED with proper bounded-drain fix

State: OPEN | #57919
Labels: bug, area:ide, stale

---

**Affected package:** `@agentclientprotocol/claude-agent-acp` (verified on v0.30.0, v0.31.0, v0.31.3, v0.31.4, v0.33.1)
**Affected client:** Zed (any recent version using the ACP integration)

> **Update on the simple `return`-on-result fix in my earlier report:** on v0.33+ that fix introduces a render-delay regression — the final `stream_event` chunks arrive *after* `result`, so returning immediately cuts off the tail of the response (it renders on the next user turn instead of finishing the current one). The proper fix is a **bounded post-result drain** described below.

### Summary

The streaming loop in `acp-agent.js` only exits the user-turn via `session_state_changed: { state: "idle" }`. The `result` message — the actual semantic end of a Claude Code turn — falls through to a bare `break;` and the loop keeps waiting. When `idle` lags or never arrives, `session.promptRunning` stays `true` indefinitely.

### Symptom (in Zed)

- Stop button stays active after Claude finishes responding.
- User has to click Stop manually before sending the next message (clicking Stop forces the stream closed, which finally lets the loop exit).
- Sound alert (Zed's `AcpThreadEvent::Stopped`) is delayed by the same mechanism — it fires on stream close, not on `result`.

### Why the obvious fix isn't enough

The first thing one tries — replacing `break;` at end of `case "result":` with `return { stopReason, usage: sessionUsage(session) };` — *does* fix the stuck stop button. But on v0.33+ it introduces a render-delay regression: the final `stream_event` chunks (the last text deltas of the response) arrive in the queue *after* `result`. Returning immediately on `result` means those chunks never get drained, so the user sees the response truncated until they send the next message (which triggers a UI re-render). Net effect: stop button works, but the last paragraph of every reply is hidden.

### Proper fix: bounded post-result drain

Keep the loop alive after `result` so straggler `stream_event`s drain naturally. Race the iterator's `await` against a 3-second timeout that's only armed once `result` has been seen. If `idle` arrives within the 3s window (common case) → existing `case "session_state_changed":` path returns cleanly with no render delay. If `idle` never arrives → timeout fires → force-return → no stuck stop button.

Two diffs against `node_modules/@agentclientprotocol/claude-agent-acp/dist/acp-agent.js`:

**(1) At the top of the streaming `while (true)` loop**, set up the drain-timeout state and race the await:

```js
// [PATCH] Bounded post-result drain.
let resultSeenAt = 0;
const POST_RESULT_DRAIN_MS = 3000;
try {
    while (true) {
        const messageP = session.query.next();
        let result;
        if (resultSeenAt > 0) {
            const remaining = Math.max(50, POST_RESULT_DRAIN_MS - (Date.now() - resultSeenAt));
            const timeoutP = new Promise((resolve) => setTimeout(() => resolve({ __acpTimeout: true }), remaining));
            result = await Promise.race([messageP, timeoutP]);
        } else {
            result = await messageP;
        }
        if (result && result.__acpTimeout) {
            return { stopReason, usage: sessionUsage(session) };
        }
        const { value: message, done } = result;
        // ...rest of loop unchanged
```

**(2) Inside `case "result":`** — after the existing switch on `message.subtype`, before the `break;` — arm the timeout:

```js
// [PATCH] Mark result-seen for drain-timeout race. Only the user-turn's
// result arms it; task-notification followups don't (they're autonomous;
// the user turn can keep running waiting for its own result).
if (!isTaskNotification && resultSeenAt === 0) {
    resultSeenAt = Date.now();
}
break;
```

(The `!isTaskNotification` guard exists in v0.33+; on v0.31 and earlier, drop the guard.)

### Why this shape

- Common case (`idle` arrives within 3s): the existing `case "session_state_changed":` return-path runs first. Drain completes naturally. No behavior change for happy-path turns.
- Failure case (`idle` never arrives): timeout fires after the drain window. Loop returns the same shape it would on `idle`. Stop button releases. No truncated response.
- Task notifications (v0.33+): the `!isTaskNotification` guard prevents an autonomous followup `result` from arming the timeout. Only the user-turn's own `result` does.

### Repro

1. Zed + Claude Code ACP agent.
2. Send any prompt that takes more than a few seconds (especially one that launches background tasks).
3. Observe: stop button stays active after the response finishes streaming; sound alert delayed; with the simple `return`-on-result fix, observe truncated final paragraph instead.

### Why this matters

Every Zed + Claude Code user hits this. It reads like a Zed bug to the user ("Zed's stop button is broken") but the fix lives in the Anthropic-published bridge. The simple fix is tempting but introduces a regression on current versions; the bounded-drain shape is what works in production.

### Not a duplicae.
Not a duplicate of #50665. That issue is in the Claude Code TUI (`area:tui`, Windows-specific) and involves the **inability to interrupt while Claude is executing tool calls** — a different code path. This issue is specifically in `@agentclientprotocol/claude-agent-acp/dist/acp-agent.js`, where the streaming loop hangs **after** Claude finishes (waiting for a `session_state_changed: idle` that doesn't arrive). The fix is in the ACP bridge package, not Claude Code itself. Affects every Zed-via-ACP user. Diff and proper bounded-drain fix are in the issue body above.

# Comments on anthropics/claude-code#57919
Total: 0 comments

No comments on this issue.

---

### Issue #895 — Error: InputValidationError: Write failed due to the following issue: The required parameter `content` is missing

State: OPEN | #895
Labels: bug, duplicate


---

Not sure how to recreate this since it doesn't happen often, but when I asked Claude what lead to this happening, it said - "The error occurred because I forgot to include the "content" parameter when using the Write tool. The Write tool requires both "file_path" and "content" parameters, and I only provided the file path without the content to write to the file. I'll make sure to include both parameters when creating files. "

But also sometimes it happens that Claudecode gets stuck trying to implement something for more than 30 mins without error logs/message to the end user. Time increases but the token count does not increase. (Could be related). I will include an image to this issue if I encounter this again. 

Claude code version - latest as of now (Auto update is on)
API - using my own from Anthropic account

# Comments on anthropics/claude-code#895
Total: 30 comments

--- Comment 1 ---
Author: lio590
Date: 2025-05-01T07:31:38Z

> It's not a bug; it means you didn't provide an argument for something, so he couldn't set a directive correctly. Fix your order to resolve the issue.

MRVarden  Your diagnostic is incorrect, it is a bug. This is happening very often and not because any lack of instructions, argument or whatever. On top of this, while looping doing nothing it keeps charging your account !
Je vais maintenant implémenter toutes ces modifications une par une et créer le script V7 complet.

● Write
⎿ Error: InputValidationError: Write failed due to the following issue:
The required parameter content is missing

● Pardonnez-moi pour cette erreur. Je vais créer le contenu du fichier et l'écrire.

● Write
⎿ Error: InputValidationError: Write failed due to the following issue:
The required parameter content is missing

● Je remarque une erreur avec l'utilisation de la fonction Write. Essayons à nouveau en incluant le contenu :

● Write
⎿ Error: InputValidationError: Write failed due to the following issue:
The required parameter content is missing

● Je vais procéder en créant un contenu explicite :

● Write
⎿ Error: InputValidationError: Write failed due to the following issue:
The required parameter content is missing

✶ Implementing… (1481s · ↓ 1.5k tokens · esc to interrupt)



--- Comment 2 ---
Author: lio590
Date: 2025-05-07T09:50:28Z

Merci pour l'information, de mon coté a un certain momemt j'ai laissé tourner et au bout de 3/ 4 fois il a de lui meme dit "je vais essayer une autre méthode pour écrire dans le fichier" et il a utilisé un bash, grep etc. depuis quand ça arrive je le stop et je lui dit "utilise bash" et ça fonctionne. Honnètement je ne sais si c'est vraiment la root cause mais cela fonctionne pour moi. Je suis d'accord pour le md c'est une excellente idée. 

--- Comment 3 ---
Author: github-actions[bot]
Date: 2025-12-03T10:10:33Z

This issue has been inactive for 30 days. If the issue is still occurring, please comment to let us know. Otherwise, this issue will be automatically closed in 30 days for housekeeping purposes.

--- Comment 4 ---
Author: Ka0fKa
Date: 2025-12-10T00:39:32Z

I also encountered this problem：
  Error: InputValidationError: Write failed due to the following issues:
     The required parameter `file_path` is missing
     The required parameter `content` is missing

--- Comment 5 ---
Author: Ka0fKa
Date: 2025-12-10T02:50:04Z

Why are the problems that occurred in April not yet resolved and are new versions updated every day?

--- Comment 6 ---
Author: acking-you
Date: 2025-12-20T05:40:55Z

I'm having the same issue too, and I'm on the latest version.

--- Comment 7 ---
Author: bearyue
Date: 2026-01-21T03:07:26Z

I’ve encountered the same issue as well. Strangely, it seems to be related to the configured API—when using services from some third-party sites, the problem occurs, but everything works normally when using the official one.

--- Comment 8 ---
Author: ssim2023
Date: 2026-01-22T10:19:17Z

I've encountered this problem too, and it's amazing it hasn't been fixed yet.

--- Comment 9 ---
Author: dirtycomputer
Date: 2026-01-22T21:54:48Z

+1 有可能是要读写的content过长

--- Comment 10 ---
Author: Atlantic83
Date: 2026-01-24T11:44:44Z

+1

--- Comment 11 ---
Author: cgoy2020
Date: 2026-01-29T03:36:07Z

+1  

--- Comment 12 ---
Author: nereus-east
Date: 2026-01-31T15:44:26Z

+1

--- Comment 13 ---
Author: fuzihaofzh
Date: 2026-02-01T14:11:23Z

Same problem:
```
Error: InputValidationError: Write failed due to the following issues:                               
     The required parameter `file_path` is missing                                                        
     The required parameter `content` is missing                                                          
  ⎿  Error: InputValidationError: Write failed due to the following issues:                               
     The required parameter `file_path` is missing                                                        
     The required parameter `content` is missing
```

--- Comment 14 ---
Author: YBloom
Date: 2026-02-05T10:55:16Z

+1


--- Comment 15 ---
Author: Akucuki
Date: 2026-02-08T08:57:34Z

+1

--- Comment 16 ---
Author: xyyandxyy
Date: 2026-02-08T09:23:38Z

+1

--- Comment 17 ---
Author: samicodesit
Date: 2026-02-09T11:01:09Z

+1

Is this really going to go forever?

--- Comment 18 ---
Author: codeByJiaDong
Date: 2026-02-11T10:14:28Z

  Read 393 lines
  ⎿  Error: InputValidationError: Write failed due to the following issues:
     The required parameter `file_path` is missing
     The required parameter `content` is missing
  ⎿  Error: InputValidationError: Write failed due to the following issues:
     The required parameter `file_path` is missing
     The required parameter `content` is missing 
Why is this still happening in 2026


--- Comment 19 ---
Author: Gong-Ping
Date: 2026-02-12T13:38:30Z

same issue, wasted lots of time & tokens

● Now I have a comprehensive understanding of the entire pipeline. Let me write the detailed plan.
  ⎿  Error: InputValidationError: Write failed due to the following issues:
     The required parameter `file_path` is missing
     The required parameter `content` is missing
     An unexpected parameter `raw_arguments` was provided

--- Comment 20 ---
Author: DoubleMice
Date: 2026-02-12T15:14:15Z

oh god, it seems like an old bug, but why still not fix in 2026? maybe i need switch to another cli tool

--- Comment 21 ---
Author: mgr9525
Date: 2026-02-14T16:44:52Z

+

--- Comment 22 ---
Author: aragogix02-hue
Date: 2026-02-16T09:24:23Z

it happened to me few times the last years but not anymore , maybe your OS version ? update fixed ? 

--- Comment 23 ---
Author: dhananjaym182
Date: 2026-02-22T21:07:27Z

+1

--- Comment 24 ---
Author: smottt
Date: 2026-02-24T08:43:51Z

+1

--- Comment 25 ---
Author: Pickupppp
Date: 2026-02-25T04:10:24Z

+1

--- Comment 26 ---
Author: StiffCoconut
Date: 2026-02-27T02:00:01Z

+1，我这边产生这个错误的原因是由于单次输出的内容过大就会频繁出发这个问题

--- Comment 27 ---
Author: hitdavid
Date: 2026-03-03T00:34:32Z

+1，
  ⎿  Error: InputValidationError: Write failed due to the following issue:
     The required parameter `content` is missing


/doctor

 Diagnostics
 └ Currently running: native (2.1.63)
 └ Path: /******/2.1.63
 └ Invoked: /******/2.1.63
 └ Config install method: native
 └ Search: OK (bundled)

 Updates
 └ Auto-updates: disabled (CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC set)
 └ Auto-update channel: latest
 └ Stable version: 2.1.50
 └ Latest version: 2.1.63

--- Comment 28 ---
Author: MorIo24
Date: 2026-03-05T02:19:29Z

错误日志：

```  
● 明白了！现在开始编写详细的实施计划。
  ⎿  Error: InputValidationError: Write failed due to the following issue:
     The required parameter `content` is missing
```

doctor信息
 Diagnostics                        
  └ Currently running: unknown (2.1.69)                                                                 └ Path: E:\node.js\node.exe                                                                           └ Invoked: E:\node.js\node_global\node_modules\@anthropic-ai\claude-code\cli.js                       └ Config install method: global                                                                       └ Search: OK (vendor)                                                                               
  Updates
  └ Auto-updates: enabled
  └ Auto-update channel: latest
  └ Stable version: 2.1.58
  └ Latest version: 2.1.69

相同问题，2026-3-5 仍未解决

--- Comment 29 ---
Author: DaBai-1925
Date: 2026-03-05T08:43:19Z

InputValidationError: AskUserQuestion failed due to the following issues:
  - The required parameter questions is missing
  - An unexpected parameter question was provided
  - An unexpected parameter options was provided

  InputValidationError: AskUserQuestion failed due to the following issue:
  - The parameter questions type is expected as array but provided as `string'

  Diagnostics                  
  └ Currently running: npm-global (2.1.69)
  └ Config install method: global
  └ Search: OK (vendor)
  Updates
  └ Auto-updates: enabled
  └ Update permissions: Yes
  └ Auto-update channel: latest
  └ Stable version: 2.1.58
  └ Latest version: 2.1.69 

--- Comment 30 ---
Author: johnning2333
Date: 2026-03-05T13:34:25Z

+1

---

### Issue #59526 — VSCode extension renderer disconnects from live stream during long multi-step tasks; work completes successfully in background

State: OPEN | #59526
Labels: bug, has repro, platform:macos, area:ide, platform:vscode


---

### Environment
- Claude Code VSCode extension: `2.1.142` (darwin-arm64)
- VSCode: `1.120.0`
- macOS: `26.5` (Build `25F71`), Apple Silicon (arm64)
- Model: Opus 4.7 (1M context variant)
- Effort level: `high`

### Symptom
During complex multi-step tasks (long streaming responses with multiple tool calls), the Claude Code panel in VSCode disconnects from the in-flight stream. The UI shows no further output and appears stuck.

### Reproduction
1. Open a Claude Code session in the VSCode panel.
2. Issue a complex prompt that requires multiple sequential tool calls over a sustained streaming response (e.g. a multi-account diagnostic, or a multi-file refactor).
3. Mid-response, the renderer loses its connection to the stream — no further tokens or tool-call indicators appear in the UI.
4. Closing the panel and reopening the **same session** restores full visibility: all tool calls completed successfully, files were written, and the assistant's final response is present.

### Expected behavior
The renderer should remain connected to the live stream for the full duration of the response, or should automatically reconnect without requiring a panel close/reopen.

### Actual behavior
The renderer disconnects mid-stream but the extension host continues processing successfully. The session state on disk (`~/.claude/sessions/<id>/`) reflects a fully completed turn — tool calls executed, files edited, response stored — even though the UI showed the stream as frozen.

### Diagnostic evidence (from `Anthropic.claude-code.Claude VSCode.log`)
- `[WARN] [Stall] stream_idle_partial lastChunkAgeMs=15001 bytesTotal=786 idleDeadlineMs=300000`
- `[INFO] sdk_stream_ended_no_result had_error:true subagent_count:0 message_count:220`
- `[WARN] Streaming stall detected: 46.8s gap between events (stall #1)`
- Extension version visible in `attribution header` switched from `cc_version=2.1.141.75a` to `cc_version=2.1.141.2db` mid-session, suggesting an auto-update may have occurred during the affected session.

### Network / API check (ruling these out)
- `ping api.anthropic.com`: 0% packet loss, ~20ms avg.
- Fresh TLS handshake + first byte to `api.anthropic.com`: 33–62ms across 3 trials.
- No VPN, no HTTP/HTTPS proxy, no Little Snitch / WARP / similar.
- Anthropic public status: All Systems Operational.

### Workaround
Close the affected session panel and reopen the same session by ID. All work completed in the background is visible. No data is lost — only the live view of the stream.

### Frequency
Reliably reproducible on multi-step tasks across multiple fresh Claude Code sessions. Does not reproduce on short/single-tool prompts.

# Comments on anthropics/claude-code#59526
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-15T20:30:06Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/59374
2. https://github.com/anthropics/claude-code/issues/54434
3. https://github.com/anthropics/claude-code/issues/59326

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: orbatec
Date: 2026-05-15T21:30:20Z

The bug reported by @tianbester-ZA does not resemble the 3 possible duplicate issues flagged. There is no stalling or aborting going on: the requested work completes, but as user you simply do not get any feedback. Your Claude Code screen seems to be stuck on "Thinking" (which is also not blinking anymore). This happens when an interaction is moderately complex. Happened several times in a row for me this evening...annoying.

---

### Issue #37569 — Feature request: option to disable streamed response output

State: OPEN | #37569
Labels: enhancement, area:tui


---

## Summary

Add an option to disable real-time streaming of responses in the interactive CLI, instead displaying the complete response once generation finishes.

## Motivation

Watching text stream token-by-token can be distracting and makes it harder to focus on other work while waiting for a response. A "batch" or "quiet" output mode would let users get the final result without the visual noise of incremental rendering.

## Proposed solution

A configuration option (e.g., `--no-stream` flag or a `streamResponse: false` setting in `settings.json`) that buffers the response and displays it all at once when generation completes. A simple spinner or progress indicator could replace the streaming text while waiting.

# Comments on anthropics/claude-code#37569
Total: 2 comments

--- Comment 1 ---
Author: niksauer
Date: 2026-03-26T12:10:31Z

I'd appreciate this as well. Would be great to see an environment variable or similar. 

--- Comment 2 ---
Author: somethinlike
Date: 2026-04-22T22:19:18Z

I am desiring this feature as well.

---

### Issue #57133 — [BUG] Long responses show repeated text chunks in scrollback on Windows 11 (PowerShell)

State: OPEN | #57133
Labels: bug, duplicate, platform:windows, area:tui, stale


---



### What's Wrong?

When Claude Code produces a long response, sections of the response text appear duplicated in the scrollback buffer. Scrolling back up through the output reveals the same content block (headings, bullet lists, paragraphs) repeated multiple times. The duplication is not present while the response is streaming - it only becomes visible when scrolling back. I did not resize or move the terminal.

I opened a new terminal, asked a question that had a long answer, and got duplicated text. I attached the full output - you can see the "Mid-Season Fairness" header was printed 4 times.
[claude code duplicate output.txt](https://github.com/user-attachments/files/27501560/claude.code.duplicate.output.txt)

### What Should Happen?

Scrolling should not duplicate output - each section of the response appears exactly once in scrollback.

### Error Messages/Logs

```shell

```

### Steps to Reproduce

1. Ask a question that produces a long multi-section response (markdown with headers, tables, and lists)
2. Wait for the response to finish streaming
3. Scroll back up through the output (potentially repeatedly)

### Claude Model

Sonnet (default)

### Is this a regression?

I don't know

### Last Working Version

_No response_

### Claude Code Version

2.1.133

### Platform

Anthropic API

### Operating System

Windows

### Terminal/Shell

PowerShell

### Additional Information

Potentially related issues:
- #52020
- #49086
- #56718

# Comments on anthropics/claude-code#57133
Total: 3 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-08T00:50:26Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/52172
2. https://github.com/anthropics/claude-code/issues/52924
3. https://github.com/anthropics/claude-code/issues/53764

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: kriona
Date: 2026-05-08T00:57:46Z

Appears to be a duplicate of #52924 - I'll add my session output as a comment on that issue, as my steps to reproduce are different.

--- Comment 3 ---
Author: CarthageBurning
Date: 2026-05-08T18:06:13Z

Reproducing on 2.1.119, Windows Terminal + PowerShell, Windows 11. Adding a Windows Terminal + 2.1.119 data point so the version range is documented as 2.1.119 → 2.1.133.
Fullscreen test: ran /tui fullscreen and [✓ does NOT reproduce / ✗ still reproduces] — [scopes the bug to / extends across both] the inline renderer.
Possibly related: the recent 2.1.116/117/118 changelog entries claim to fix scrollback duplication in non-fullscreen mode for Windows Terminal, but those fixes covered specific subcases (resize, Ctrl+L, dialog dismiss). They don't appear to address the "long response → repeated chunks in scrollback" path which is what's reproducing here. Likely related to the upstream Ink clearTerminal / CSI 3 J issue documented in vadimdemedes/ink#359.

UPDATE:

Adding new repro data — the bug isn't just scrollback duplication. After the duplication began, the session entered a broader degraded state: slash commands stopped being intercepted by the CLI (typing /tui fullscreen showed in the slash-command pill but was forwarded to the model as plaintext input rather than handled), and SGR mouse escape sequences started leaking into the input field as raw text (e.g., <35;129;38M<35;122;37M108;...). All three symptoms — scrollback duplication, slash command pass-through, mouse escape leak — appeared together and resolved together after Ctrl+C and relaunching with CLAUDE_CODE_NO_FLICKER=1 for fullscreen mode. Suggests the input/render pipeline as a whole degrades, not just the scrollback path.
Environment: 2.1.119, Windows 11, Windows Terminal + PowerShell, Remote Control active.

---

### Issue #33949 — SSE streaming hangs indefinitely (no timeout) + ESC cannot fully cancel (queue auto-restart) — root cause analysis with fix proposals

State: OPEN | #33949
Labels: bug, has repro, platform:windows, area:core


---

## Summary

These two bugs have been plaguing users for months (see #26224 — 28 comments, #6836 — 150+ reports), with no root cause analysis from the team. After yet another day of babysitting Claude Code and pressing ESC every few minutes to revive a hung agent, we decided to conduct our own deep investigation — reverse-engineering `cli.js` across 12 npm package versions and analyzing 1,571 session JSONL files containing 148,444 tool calls.

Here are the exact root causes and proposed fixes.

Claude Code hangs indefinitely when an SSE streaming connection silently dies. There is no client-side timeout or heartbeat detection, so the process waits forever for events that will never arrive. ESC partially works around this by aborting the dead connection, but the queue auto-restart mechanism (`queue.length > 0 → n()`) immediately starts the next queued prompt instead of returning control to the user.

**Root cause identified in source code** — two separate issues in `cli.js`:

1. **No streaming timeout**: The `messages.stream()` call has no timeout. If the SSE connection dies silently (TCP half-open), the client waits forever.
2. **Queue auto-restart after abort**: After ESC aborts a hung request, `if (queue.length > 0) { n(); return; }` immediately starts the next queued prompt. The user cannot fully cancel.

## Environment

- Claude Code: 2.1.74 (also confirmed on 2.1.50–2.1.73)
- OS: Windows 10, Git Bash
- Model: Opus 4.6
- API: Anthropic direct (not Bedrock/Vertex)

## Reproduction

1. Start a Claude Code session
2. Submit a prompt → agent starts processing
3. Wait for a hang (0 tokens, timer running, no progress) — happens ~10-15% of prompts
4. Submit another prompt while hung → goes to queue
5. Press ESC
6. **Expected:** Cancel everything, return to `❯`
7. **Actual:** Cancels the hung prompt, immediately starts the queued one

## Frequency

Measured across **1,571 sessions** using a custom JSONL analyzer tool:

| Period | Versions | Orphan rate (lost tool calls) |
|--------|----------|-------------------------------|
| Dec 2025 | 2.0.72–2.1.2 | 6–14% |
| Jan 2026 | 2.1.5–2.1.23 | 5–10% |
| Feb 2026 | 2.1.29–2.1.56 | 3–8% |
| Mar 2026 | 2.1.69–2.1.74 | 2.4–4% |

The hang frequency has been **increasing** over time: rare in fall 2025, now ~10-15% of prompts per hour.

## Source Code Analysis

Analyzed `cli.js` extracted from `npm pack @anthropic-ai/claude-code` across versions 2.0.72 through 2.1.74.

### Issue 1: No streaming timeout

The API call at approximately offset 2,553,870 in cli.js (v2.1.74):

```js
client.beta.messages.stream({...params}, options)
```

There is no timeout parameter, no keepalive check, and no heartbeat detection. The Anthropic SSE API sends periodic `:ping` comments, but the client does not monitor for their absence.

When the TCP connection silently dies (common on Windows, WiFi, VPN, or after laptop sleep), the Node.js HTTP client has no way to know the connection is dead. The `AbortController` signal is never triggered because no error event fires.

**Evidence**: Packet inspection by other reporters confirms the client is stuck waiting for SSE events that never arrive. Token count stays at 0. ESC + re-submit creates a new connection that works immediately.

### Issue 2: Queue auto-restart prevents full cancellation

The main processing loop (offset ~11,400,559 in v2.1.74):

```js
n = async () => {
  if (M) return;       // running guard
  M = true;
  // ... prepare input, call API, process response ...
}
```

After completion or abort — in the `finally` block (offset ~11,406,174):

```js
finally {
  M = false;           // clear running guard
  W6.start();          // restart idle timer
}
if (c36()) {           // c36() = yY.length > 0 = queue not empty?
  n();                 // YES → immediately restart with queued message!
  return;              // without returning control to user!
}
```

Historical analysis of npm packages confirms this pattern exists since **v2.1.50** (as `queue.length > 0`) and was refactored to `c36()` in v2.1.74.

### Issue 3: JSONL writer race condition (related)

The session writer class `LZq` (offset ~10,549,000) has a non-atomic `insertMessageChain()` that writes assistant (tool_use) and user (tool_result) messages **one at a time** in a loop:

```js
async insertMessageChain(A, q, K, Y, z) {
  return this.trackWrite(async () => {
    for (let H of A) {
      await this.appendEntry(M);  // each message separately!
    }
  });
}
```

If the process is interrupted between writing tool_use and tool_result, the tool_use becomes orphaned. This is the root cause of issue #6836.

## Proposed Fixes

### Fix 1: Streaming timeout (critical)

Add a client-side timeout that aborts and retries if no SSE events are received within N seconds:

```js
// Pseudocode
const STREAM_IDLE_TIMEOUT_MS = 30_000;
let lastEventTime = Date.now();

stream.on('event', () => { lastEventTime = Date.now(); });

const watchdog = setInterval(() => {
  if (Date.now() - lastEventTime > STREAM_IDLE_TIMEOUT_MS) {
    clearInterval(watchdog);
    abortController.abort();
    // retry with new connection
  }
}, 5_000);
```

The Anthropic API sends `:ping` SSE comments periodically. Monitoring for these would detect stale connections without false positives.

### Fix 2: ESC should clear the queue

When the user presses ESC during a hang, the queue should be cleared (or the user should be asked):

```js
// After abort, before checking queue:
if (userInitiatedAbort && c36()) {
  // Option A: Clear queue entirely
  clearQueue();
  return; // back to prompt

  // Option B: Ask user
  // "You have N queued messages. Clear queue? (y/n)"
}
```

### Fix 3: Atomic message chain writes

`insertMessageChain()` should serialize the entire chain as a single `appendToFile()` call:

```js
async insertMessageChain(messages) {
  const serialized = messages.map(m => JSON.stringify(m)).join('\n') + '\n';
  await this.appendToFile(sessionFile, serialized);
}
```

Note: `history.jsonl` already uses `proper-lockfile` for file locking — the same approach should be applied to session JSONL files when multiple agents write concurrently.

## Related Issues

- #6836 — Orphaned tool_use/tool_result pairs (150+ reports)
- #26224 — Agent hangs 5-20 minutes, 0 tokens
- #31328 — JSONL writer drops assistant entry during parallel tool calls
- #20171 — Phantom "Generating..." state after task completion
- #24688 — Freeze during API call, terminal unresponsive
- #7243 — `.claude.json` architectural issues (non-atomic writes, no separation of concerns)
- #14642 — Systemic stability problems driving users to build their own tools

## Methodology

Analysis performed using:
- **ccdiag**: Custom Go CLI tool that parses JSONL session files, detects orphaned tool calls, analyzes timing, and scans multiple sessions
- **Source analysis**: `cli.js` extracted from npm packages across 12 versions (2.0.72 through 2.1.74), searched for queue/abort/streaming patterns
- **Session data**: 1,571 sessions, 148,444 tool calls, 8,007 orphaned

# Comments on anthropics/claude-code#33949
Total: 30 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-03-13T10:46:16Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/25979
2. https://github.com/anthropics/claude-code/issues/27841
3. https://github.com/anthropics/claude-code/issues/18028

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: kolkov
Date: 2026-03-13T10:50:02Z

This is **not a duplicate** of any of those issues. Here's why:

| Issue | What it has | What it lacks |
|-------|------------|---------------|
| #25979 | Symptom description (hang on stall) | No source code analysis, no fix proposals |
| #27841 | Symptom description (hang with multiple sessions) | No root cause, no code references |
| #18028 | Timing measurements (59-138s delays) | No source analysis, no fix proposals |
| **This issue** | **Root cause in source code** + **3 fix proposals** + **12-version npm archaeology** + **1,571 session dataset** | — |

Those issues describe *what* happens. This issue explains *why* it happens and *how to fix it* — with exact code offsets in `cli.js`, pseudocode fixes, and statistical evidence from 148,444 tool calls.

Specifically, this issue identifies:
1. The exact `messages.stream()` call with no timeout (offset ~2,553,870 in v2.1.74)
2. The queue auto-restart pattern `if(c36()){n();return}` that prevents ESC from fully cancelling (offset ~11,406,174)
3. The non-atomic `insertMessageChain()` race condition causing orphaned tool_use (offset ~10,555,400)

None of the "duplicate" issues contain any of this analysis.

--- Comment 3 ---
Author: kolkov
Date: 2026-03-13T14:33:44Z

> **⚠️ Updated April 1, 2026**: The source map leak in v2.1.88 gave us access to the full TypeScript source. We've posted **updated prompts with exact file paths and line numbers** — no more reverse engineering of minified code: [Updated prompts →](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4169440989)
> 
> Also see our full write-up: [We Reverse-Engineered 12 Versions of Claude Code. Then It Leaked Its Own Source Code.](https://dev.to/kolkov/we-reverse-engineered-12-versions-of-claude-code-then-it-leaked-its-own-source-code-pij)

---

Since 100% of Claude Code is now written by Claude Code itself — "I have not edited a single line by hand since November" ([Boris Cherny, creator of Claude Code](https://x.com/bcherny/status/2004897269674639461)) — here are ready-to-use prompts for @bcherny to copy-paste directly into Claude Code and fix these issues. No reverse engineering skills required — we already did that part.

But first — the prompts alone won't help if the development process itself is broken. So let's start there.

**Important note on testing:** We suspect Anthropic internally uses a private API endpoint or prioritized infrastructure that doesn't experience the same latency, timeouts, and stale connections that paying customers face on the public API. This would explain why these bugs go unnoticed internally — if your SSE stream never stalls on a private backbone, you'll never hit the missing timeout. Meanwhile, your paying customers — on real networks, with real latency, WiFi drops, VPN reconnects, and laptop sleep/wake cycles — hit it multiple times per hour and pay for every wasted token and every minute of babysitting a hung agent. **All testing for these fixes MUST be done against the public API, on real consumer hardware, with simulated network instability.** Not on Anthropic's internal infrastructure where everything "just works."

---

### Prompt 0: Set up a proper development workflow

```
Read the project's CLAUDE.md. If it doesn't exist, create it. This is the most
important file in the project — it defines how YOU (Claude Code) should work
on this codebase. Add the following sections:

## Release Checklist (MANDATORY before every release)

Before shipping ANY release, verify:

1. [ ] Core workflow test: submit prompt → stream response → execute tool
       → return result. Does it complete without hanging? Test 20 times.
2. [ ] ESC test: Start a prompt, press ESC mid-stream. Does it return to
       the prompt immediately? No queued messages auto-starting?
3. [ ] Network failure test: Disconnect WiFi mid-stream. Does the client
       detect the dead connection within 30s and recover?
4. [ ] Concurrent write test: Run 2 agents writing to the same session.
       Are all tool_use/tool_result pairs intact in the JSONL?
5. [ ] Long session test: Run a 2-hour session with 100+ tool calls.
       Count orphaned tool_use entries. Must be 0.
6. [ ] Disk pressure test: Run with <1GB free disk space. Does it degrade
       gracefully or corrupt settings files?

If ANY check fails — DO NOT RELEASE. Fix it first.

## Priority Rules

- Bug fixes for core workflow ALWAYS take priority over new features
- Every network call MUST have a timeout — no exceptions
- Every multi-step file write MUST be atomic
- ESC means STOP EVERYTHING — never auto-restart after user abort

## Known Debt (must fix before adding features)

- #6836 — orphaned tool_use/tool_result (150+ reports, 6+ months open)
- #26224 — streaming hangs indefinitely (30+ comments, 0 team responses)
- #20171 — phantom "Generating..." state (17 comments)
- #33949 — root cause analysis with exact code locations and fix proposals

## Pre-commit Checks

Before committing, always run:
- All existing tests pass
- No new network calls without timeout
- No new file writes without atomic pattern
- No queue auto-restart after abort paths

## Session Memory

After each work session, update STATUS.md with:
- What was changed and why
- What tests were added
- What known issues remain
- What regressions to watch for
```

This is how agentic engineering works — you give the AI agent clear rules,
priorities, and checklists BEFORE it starts coding. Not after. Not "vibes".

For more on this approach, see: [From Vibe Coding to Agentic Engineering: What Karpathy Got Right and What's Missing](https://dev.to/kolkov/from-vibe-coding-to-agentic-engineering-what-karpathy-got-right-and-whats-missing-62e)

---

Now the actual fixes:

### Prompt 1: Fix streaming timeout (Issue #33949, Root Cause #1)

```
Read the streaming API call in the codebase where client.beta.messages.stream()
is called. There is no timeout or heartbeat detection — if the SSE connection
silently dies (TCP half-open), the client waits forever. This is the #1 cause
of "agent hangs, timer running, 0 tokens" reports.

Fix: Add a watchdog timer that monitors incoming SSE events. The Anthropic API
sends periodic :ping SSE comments. If no events are received for 30 seconds,
abort the connection via AbortController and retry with a new connection.
Implement exponential backoff for retries (max 3 attempts).

Create a todo list before starting. Write tests for:
- Normal streaming (no timeout)
- Stale connection (no events for 30s → abort + retry)
- Max retries exceeded → surface error to user
```

### Prompt 2: Fix ESC not fully cancelling (Issue #33949, Root Cause #2)

```
Find the main processing loop function (the async function that checks a
running guard, processes user input, calls the API, and handles responses).
After the finally block that clears the running guard, there is a check:
if the queue is not empty, it immediately calls the processing function
again and returns — without giving the user control back.

This means when a user presses ESC during a hang, the queued message
auto-starts instead of returning to the prompt.

Fix: When the abort was user-initiated (ESC), clear the queue entirely
before checking it. Do NOT auto-restart queued messages after user abort.
The queue auto-restart should only happen after successful completion,
not after abort.

Create a todo list before starting. Write tests for:
- ESC during normal processing → returns to prompt, queue cleared
- ESC during hang → same behavior
- Successful completion with queued messages → auto-restart OK
```

### Prompt 3: Fix JSONL writer race condition (Issue #6836 root cause)

```
Find the session JSONL writer class that has an insertMessageChain() method.
It currently writes messages one at a time in a for loop — each message is
a separate appendEntry() call. If the process is interrupted between writing
tool_use and tool_result, the tool_use becomes orphaned.

Fix: Serialize the entire message chain into a single string
(messages.map(JSON.stringify).join('\n') + '\n') and write it in one
appendToFile() call. This makes the write atomic at the OS level.

Also check if proper-lockfile (already used for history.jsonl) should be
applied to session JSONL files for concurrent agent writes.

Create a todo list before starting. Write tests for:
- Single message write (baseline)
- Chain write (tool_use + tool_result) — verify both present in file
- Simulated interruption mid-chain — verify no partial writes
- Concurrent writes from 2 agents — verify no corruption
```

### Prompt 4: Audit the entire codebase for the same classes of bugs

```
You just fixed 3 specific bugs: missing streaming timeout, queue auto-restart
after ESC, and non-atomic JSONL writes. Now audit the ENTIRE codebase for
the same patterns — these bugs are symptoms of systemic problems, not one-offs.

Search and fix ALL instances of:

1. NETWORK CALLS WITHOUT TIMEOUT: Find every HTTP request, SSE stream,
   WebSocket connection, and fetch() call. Every single one must have:
   - A client-side timeout (30s for streams, 10s for REST calls)
   - An AbortController signal
   - Error recovery (retry with backoff or surface error to user)
   List every call you find and its current timeout status.

2. NON-ATOMIC FILE WRITES: Find every place where multiple related records
   are written to a file sequentially (for loops writing to JSONL, multiple
   appendFile calls for related data). Each must be converted to a single
   write operation. Also check for write-then-rename atomic patterns —
   config files (.claude.json, settings.json) should use write-to-tmp +
   rename, not direct overwrite.

3. USER ABORT NOT FULLY HONORED: Find every AbortController/abort() handler
   and every catch block that handles AbortError. Verify that after abort:
   - No background work continues
   - No queued tasks auto-restart
   - All resources (connections, file handles, timers) are cleaned up
   - Control returns to the user prompt

4. CONCURRENT ACCESS WITHOUT LOCKING: Find every file that can be written
   by multiple processes simultaneously (session files, config files,
   history). Each must have proper file locking (proper-lockfile or OS-level).

Create a todo list of every instance found. Fix each one. This is not
optional — these are the root causes of 150+ bug reports.
```

### Prompt 5: Write enterprise-grade regression tests for core workflow

```
The core workflow (submit → stream → tools → result → cancel) is the #1
priority. It must NEVER regress. Write a comprehensive test suite that
runs on every CI build and blocks releases if any test fails.

## Test Suite: Core Workflow Reliability

### 1. Streaming Tests
- test_stream_completes_normally
- test_stream_timeout_triggers_after_30s_silence
- test_stream_timeout_retries_with_backoff
- test_stream_max_retries_surfaces_error
- test_stream_recovers_after_network_reconnect
- test_stream_abort_cleans_up_all_resources
- test_stream_handles_malformed_sse_events
- test_stream_handles_partial_json_chunks
- test_concurrent_streams_independent (multiple agents)

### 2. ESC / Abort Tests
- test_esc_during_streaming_returns_to_prompt
- test_esc_during_tool_execution_returns_to_prompt
- test_esc_clears_message_queue
- test_esc_does_not_auto_restart_queued_messages
- test_esc_aborts_all_pending_network_calls
- test_esc_closes_all_file_handles
- test_esc_stops_all_timers
- test_double_esc_is_safe (no double-free, no crash)
- test_esc_during_file_write_does_not_corrupt

### 3. Data Integrity Tests
- test_tool_use_always_paired_with_tool_result
- test_message_chain_write_is_atomic
- test_interrupted_chain_write_no_partial_data
- test_concurrent_session_writes_no_corruption
- test_config_write_is_atomic (write-tmp-rename pattern)
- test_session_file_valid_jsonl_after_abort
- test_session_file_valid_jsonl_after_crash (kill -9)
- test_no_orphaned_tool_use_after_100_rapid_esc_presses

### 4. Resource Cleanup Tests
- test_no_leaked_file_handles_after_session
- test_no_leaked_timers_after_abort
- test_no_leaked_connections_after_timeout
- test_no_temp_files_left_after_session (.node leak)
- test_disk_full_graceful_degradation
- test_disk_full_no_config_corruption

### 5. Regression Guards (one test per historical bug)
- test_regression_6836_no_orphaned_tool_results
- test_regression_26224_no_indefinite_hang
- test_regression_20171_no_phantom_generating
- test_regression_24688_no_frozen_terminal
- test_regression_25979_no_stale_connection_hang
- test_regression_33949_esc_fully_cancels

Each test must have a clear description of WHAT it tests and WHY (link to
the original issue). Tests must be fast (mock network where needed) and
deterministic. No flaky tests allowed — if it's flaky, the underlying
code is buggy.

Add a CI gate: if ANY of these tests fail, the release is blocked.
No exceptions. No "we'll fix it next sprint."
```

### Prompt 6: Deep codebase health audit and professional report

```
Conduct a thorough, systematic audit of the entire Claude Code codebase.
You are acting as a senior staff engineer performing a code health review
before a critical production release. Do not rush. Be methodical.

## Phase 1: Architecture Review

Map the full architecture:
- Entry point → CLI parser → prompt handler → API client → streaming →
  tool execution → response rendering → session persistence
- Draw the data flow diagram (in Mermaid or ASCII)
- Identify all shared mutable state (globals, singletons, module-level vars)
- Identify all concurrency patterns (async/await, parallel tool calls,
  multiple agent instances, background tasks)
- List every external dependency and its purpose

## Phase 2: Reliability Audit

For each component in the data flow, answer:
1. What happens if it hangs? Is there a timeout?
2. What happens if it throws? Is the error caught and handled?
3. What happens if ESC is pressed mid-operation? Are resources cleaned up?
4. What happens if disk is full? Does it degrade or corrupt?
5. What happens if 2 instances run simultaneously? Is there locking?
6. What happens if the network drops mid-operation? Detection? Recovery?

Score each component: GREEN (solid), YELLOW (risks), RED (known broken).

## Phase 3: Error Handling Review

- Find every try/catch block. Is the error logged? Re-thrown? Swallowed?
- Find every .catch() on promises. Are rejections handled or silenced?
- Find every fire-and-forget async call (no await, no .catch). List them all.
- Check: can an unhandled rejection crash the process silently?

## Phase 4: State Management Review

- Map all files written during a session (.claude.json, session JSONL,
  history.jsonl, settings.json, debug logs)
- For each: write pattern (atomic?), locking (concurrent safe?),
  corruption recovery (what if file is half-written?)
- Check: what happens if .claude.json is corrupted on startup?
- Check: what happens if session JSONL has invalid JSON on a line?

## Phase 5: Generate Professional Report

Write a report to docs/CODE_HEALTH_REPORT.md with:

### Executive Summary
- Overall health score (RED / YELLOW / GREEN)
- Top 5 critical risks ranked by user impact
- Estimated effort to fix each

### Component Health Matrix
| Component | Timeout | Error Handling | Abort Safety | Concurrency | Disk Safety | Score |
|-----------|---------|---------------|--------------|-------------|-------------|-------|
| Streaming |   ...   |      ...      |     ...      |     ...     |     ...     |  ...  |
| ...       |   ...   |      ...      |     ...      |     ...     |     ...     |  ...  |

### Critical Findings (RED)
For each: description, code location, user impact, fix proposal, effort estimate

### Warnings (YELLOW)
Same format

### Recommended Fix Order
Numbered checklist with dependencies:
- [ ] 1. Fix X (blocks #2, #3)
- [ ] 2. Fix Y (depends on #1)
- [ ] 3. ...

### Regression Prevention Plan
- What CI checks to add
- What monitoring to add
- What CLAUDE.md rules to add

This report becomes the roadmap. No new features until all RED items
are fixed and tested.
```

---

Total estimated time: ~6 hours of Claude Code work. These bugs have been open for 6+ months with 150+ community reports.

We've done the hard part — reverse-engineered the minified `cli.js` across 12 npm versions, analyzed 1,571 sessions with 148,444 tool calls, and identified exact code locations. The prompts above are based on that analysis (full details in #33949).

If Claude Code writes 100% of itself and Boris hasn't "edited a single line by hand since November" — then surely these prompts are all that's needed. Just copy, paste, and ship it — *properly* this time.

--- Comment 4 ---
Author: jviotti
Date: 2026-03-13T18:05:38Z

@kolkov Did you find any workaround while this gets fixed? The hangs get more common and are extremely disruptive... 

--- Comment 5 ---
Author: kolkov
Date: 2026-03-13T19:06:53Z

@jviotti The only workaround we have:

1. **Watch the timer** — if you see 0 tokens and 15+ seconds of silence, it's hung. Don't wait, press ESC immediately
2. **Don't type new prompts while it's hung** — they go into the queue and auto-start after ESC (that's root cause #2)
3. **ESC → re-submit** — this creates a new SSE connection which usually works right away

Basically, you have to babysit it. That's why we reverse-engineered the source and posted the fix proposals — there's no real solution until they add a streaming timeout.

Meanwhile, v2.1.75 just dropped — you can try it, but don't get your hopes up. The changelog has a new prompt bar color command, session name display, and memory file timestamps... but zero fixes for streaming hangs, ESC queue auto-restart, or orphaned tool calls. Priorities.

--- Comment 6 ---
Author: bperry0xff
Date: 2026-03-14T01:24:55Z

I've been excessively experiencing this exact issue today. I am on v2.1.75.

--- Comment 7 ---
Author: dquareng
Date: 2026-03-14T02:37:11Z

May cancel Max over this and switch to codex - ever other prompt fails has made the cli actually unusable 

--- Comment 8 ---
Author: nullbio
Date: 2026-03-14T04:56:59Z

> May cancel Max over this and switch to codex - ever other prompt fails has made the cli actually unusable

- Be Anthropic
- "The harness is the moat, we can't open source that"
- Add useless features, tech debt, bloat, and ignore bugs for a year
- Everyone makes their own "moat" or switches to competitors as a result of not open-sourcing and allowing community to submit fixes or diagnose issues easily

Irony.

--- Comment 9 ---
Author: pedromelo222
Date: 2026-03-15T14:44:42Z

<img width="486" height="44" alt="Image" src="https://github.com/user-attachments/assets/8dc0ea46-274d-4c30-b766-147d7f0dbb3c" /> 15 min to start

--- Comment 10 ---
Author: kolkov
Date: 2026-03-16T09:46:27Z

**Update: Complete system deadlock on v2.1.76 with 1M context**

Just experienced a full system deadlock on Windows 10 — had to hard power-off via holding the power button. This is on top of the streaming hang issues described above.

**What happened:**
- Claude Code v2.1.76, Opus 4.6 with 1M context (just enabled after removing `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`)
- System did NOT crash (no BSOD) — Windows stayed visually responsive, could switch windows
- **Keyboard completely dead** — no input accepted anywhere, not just in Claude Code
- Could not Ctrl+Alt+Del, could not open Start menu, could not reboot gracefully
- Only recovery: hard power-off (holding power button for 5 seconds)

This is the same freeze pattern we reported in #14674 back in December 2025 (auto-closed and locked by bot, zero team response). It had not occurred for several weeks but returned on v2.1.76.

Now we have the full picture — Claude Code has **three layers** of reliability problems:
1. **Streaming hangs** — SSE connection dies silently, no timeout (this issue)
2. **ESC doesn't cancel** — queue auto-restart prevents recovery (this issue)
3. **System deadlocks** — the tool can lock up the entire OS, requiring hard reboot (#30137, #32870, #14674)

Related: #30137 (Windows BSOD), #32870 (BSOD via Wof.sys), #12234 (Windows freezes)

--- Comment 11 ---
Author: kolkov
Date: 2026-03-17T04:14:38Z

**Another fun one**: after removing `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` to enable 1M context (see #34143), the auto-updater memory leak in v2.1.76 crashed our overnight session — **13.81 GB committed memory**, Bun panic after 12 hours, all work lost.

So to recap, in the last 48 hours:
1. Streaming hangs (this issue) — still not fixed in v2.1.77
2. Complete system deadlock requiring hard power-off (comment above)
3. Auto-updater memory leak crashing a 12-hour session (#35171)

Three different bugs, three different mechanisms, zero hours of uninterrupted work.

v2.1.77 changelog says the auto-updater leak is fixed, and ESC is "improved" for non-streaming requests. Streaming timeout — still missing.

--- Comment 12 ---
Author: kolkov
Date: 2026-03-17T06:36:30Z

**Update: We found the fix. It already exists in the code. It's been there since February 2026. It's disabled.**

It's become impossible to work with Claude Code reliably. In the last 72 hours alone: streaming hangs every 10-15 minutes, a complete system deadlock requiring hard power-off, and a 12-hour overnight session lost to an auto-updater memory leak (13.81 GB). We're spending more time babysitting the tool than actually coding. And we're paying for the privilege.

After deeper reverse-engineering of `cli.js` across 12 npm versions (v2.0.72 through v2.1.77), we found that Anthropic **already wrote a streaming watchdog** — and hid it behind an undocumented environment variable.

## The hidden fix: `CLAUDE_ENABLE_STREAM_WATCHDOG`

```bash
# Add to ~/.claude/settings.json:
{
  "env": {
    "CLAUDE_ENABLE_STREAM_WATCHDOG": "1"
  }
}
# Or: export CLAUDE_ENABLE_STREAM_WATCHDOG=1
```

This enables a watchdog that:
- **Warning** at 30s with no SSE chunks → logs "Streaming idle warning"
- **Abort** at 60s → aborts the dead connection via AbortController
- **Fallback** → retries the same request in non-streaming mode
- **Reset** on every received chunk → no false positives during normal streaming

The implementation (v2.1.77, offset ~10,437,656):
```js
let I6 = o6(process.env.CLAUDE_ENABLE_STREAM_WATCHDOG);  // feature flag
let g6 = 30000;   // warning: 30 seconds
let F6 = 60000;   // abort: 60 seconds

function H1() {   // called before streaming AND on every chunk
  clearTimers();
  if (!I6) return; // ← DISABLED by default!

  warningTimer = setTimeout(() => {
    log("Streaming idle warning: no chunks for 30s");
  }, 30000);

  abortTimer = setTimeout(() => {
    log("Streaming idle timeout: no chunks for 60s, aborting");
    abortController.abort();  // kill the dead connection
  }, 60000);
}
```

## Version archaeology: disabled for 10 releases

| Version | Date | Watchdog in code | Enabled by default |
|---------|------|------------------|--------------------|
| 2.0.72 | Dec 2025 | ❌ | — |
| 2.1.29 | Jan 2026 | ❌ | — |
| **2.1.50** | **Feb 2026** | **✅ Added** | **❌ No** |
| 2.1.56 | Feb 2026 | ✅ | ❌ |
| 2.1.62 | Feb 2026 | ✅ | ❌ |
| 2.1.68 | Mar 2026 | ✅ | ❌ |
| 2.1.69 | Mar 2026 | ✅ | ❌ |
| 2.1.72 | Mar 2026 | ✅ | ❌ |
| 2.1.74 | Mar 2026 | ✅ | ❌ |
| 2.1.75 | Mar 2026 | ✅ | ❌ |
| 2.1.76 | Mar 2026 | ✅ | ❌ |
| 2.1.77 | Mar 2026 | ✅ | ❌ |

**10 releases. 2+ months. 150+ bug reports. The fix is right there.**

## Anthropic already knows: stall telemetry is always on

Here's the kicker. There's a **second** monitoring system that is **always enabled** — no feature flag:

```js
// ALWAYS runs, no flag needed:
let K6 = 30000;  // 30s threshold
for await (let chunk of stream) {
  let gap = Date.now() - lastChunkTime;
  if (gap > 30000) {
    stallCount++;
    telemetry("tengu_streaming_stall", {  // ← sent to Anthropic!
      stall_duration_ms: gap,
      stall_count: stallCount,
      total_stall_time_ms: totalStallTime
    });
  }
}
```

Every time your session hangs for 30+ seconds, Anthropic receives a `tengu_streaming_stall` event. They know exactly how often this happens, on which models, for which users. **They have the data. They have the fix. They don't enable it.**

## Why it hangs for so long: the TCP keepalive gap

We checked Windows TCP keepalive settings (registry `HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters`) — **not configured**, so Windows defaults apply:

| Layer | Mechanism | Timeout | Status |
|-------|-----------|---------|--------|
| **TCP** | keepalive probes | **2 hours** (Windows default) | SSE socket has no probes |
| **Application** | Stream watchdog | 60 seconds | **DISABLED** (feature flag) |
| **User** | ESC → manual abort | Manual | Works but not automatic |

The SSE streaming connection uses Bun's `fetch()` which sets HTTP-level `keepalive: true` (connection reuse) but does **not** set TCP-level keepalive probes on the socket. When the connection silently dies:

1. TCP stack doesn't know (no probes configured)
2. Watchdog is disabled (could abort at 60s, but won't)
3. Windows will detect the dead socket in... **2 hours**
4. Meanwhile, you stare at "0 tokens" and press ESC

## What we're asking

This isn't a feature request. The feature exists. We're asking Anthropic to flip a boolean.

**Option A** — Enable the watchdog by default. If false positives on long-thinking Opus requests are a concern, increase the timeout from 60s to 120s or 180s.

**Option B** — Document `CLAUDE_ENABLE_STREAM_WATCHDOG` so users can opt in. Right now it's completely invisible — not in the docs, not in the changelog, not in `/config`.

**Option C** — At minimum, respond to this issue. 150+ reports, 8 months, 👍8, users threatening to leave for Codex — and the fix is sitting in your codebase behind a single env var.

## Community workaround

Until Anthropic acts, you can enable the watchdog yourself. Add to `~/.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_ENABLE_STREAM_WATCHDOG": "1"
  }
}
```

**Warning**: If Opus is "thinking" for > 60s without sending chunks, the watchdog will abort and retry in non-streaming mode. This is a trade-off — but it's better than staring at a dead connection for 10 minutes.

We haven't fully tested this yet (enabling it today). Community feedback welcome — please report if this helps or causes issues.

## Bonus: Bun runtime crashes taking down the IDE

While writing this comment, Claude Code crashed again — Bun 1.3.11 mimalloc allocator panic:
```
allocator->scavenger_data.is_in_use = yes
panic: Illegal instruction at address 0x7FF63A2DE777
```
This crash took down not just Claude Code but the entire GoLand IDE it was running in. Related: [oven-sh/bun#27690](https://github.com/oven-sh/bun/issues/27690), #26174, #30223.

So in 72 hours: streaming hangs, system deadlock (hard power-off), auto-updater memory leak (13.81 GB, 12h session lost), and now Bun allocator crash killing the IDE. This tool is **actively hostile** to productivity.

@bcherny @wolffiex @ThariqS — what's the reason for keeping the watchdog disabled? Is it false positives, or something else? At this point even a 50% false positive rate would be better than the current state.

--- Comment 13 ---
Author: kolkov
Date: 2026-03-17T09:48:52Z

**Update: Enabled `CLAUDE_ENABLE_STREAM_WATCHDOG=1` — dramatic improvement**

After enabling the watchdog (and `DISABLE_AUTOUPDATER=1` to prevent the memory leak), the difference is night and day:

| Metric | Before watchdog (gogpu session, 302h) | After watchdog (current session) |
|--------|---------------------------------------|----------------------------------|
| Max stuck call | **8 min 5 sec** | **1 min 10 sec** |
| Stuck calls > 2 min | Dozens | **0** |
| Bash median | 6.6s | 6.9s (same) |
| Subjective speed | Stalls every 10-15 min | Responses are flying |

Base API speed is the same (medians unchanged), but **stalls over 2 minutes have completely disappeared**. No false positives observed with Opus 4.6 extended thinking.

Whether this is the watchdog aborting dead connections faster, or Anthropic fixing something server-side at the same time, or both — the result is clear.

**However**: One of our parallel agents (gogpu/ui project) got stuck in a 500/529 error loop on v2.1.77 with watchdog enabled:
```
API Error: 500 {"type":"error","error":{"type":"api_error","message":"Internal server error"}}
529 {"type":"error","error":{"type":"overloaded_error","message":"Overloaded"}}
Retrying in 0 seconds… (attempt 6/10)
```
- Same `request_id` across retries = **sticky routing to a dead backend instance**
- Two other agents in parallel sessions worked perfectly = **instance-specific failure**
- Watchdog did NOT help here — 500/529 is HTTP-level, before SSE stream opens
- The session's JSONL had grown to **107 MB** over 302 hours (12.5 days)
- Only fix: `/exit` → new session → new TCP connection → new healthy instance → works instantly

So the watchdog fixes **silent SSE stalls** but not **server-side 500/529 loops**. For the latter, the only workaround is still restarting the session.

**Recommended settings** (add to `~/.claude/settings.json`):
```json
{
  "env": {
    "CLAUDE_ENABLE_STREAM_WATCHDOG": "1",
    "DISABLE_AUTOUPDATER": "1"
  }
}
```

Community: please try this and report back. Does it help with your hangs?

--- Comment 14 ---
Author: kolkov
Date: 2026-03-17T10:59:50Z

**Update: How tool results get lost — race conditions in JSONL writer**

We've been observing orphaned tool calls in our sessions where the tool **executes successfully** (file written to disk, command completed) but the `tool_result` never gets recorded. The model on the next turn has no idea the tool succeeded.

This happens because of the race conditions in `insertMessageChain()` we identified in our original analysis. The chain writes `tool_use` and `tool_result` **one at a time** in a for-loop:

```js
async insertMessageChain(messages) {
  for (let msg of messages) {
    await this.appendEntry(msg);  // tool_use first
    // ← race condition window: ESC, stall, concurrent write
    await this.appendEntry(msg);  // tool_result second
  }
}
```

If anything interrupts between the two writes — ESC press, streaming stall, `scheduleDrain()` guard collision, or concurrent agent writing to the same file — the `tool_use` is recorded but `tool_result` is lost.

### Consequences

The model doesn't know the tool succeeded:
- **Autonomous agents** re-do the same work (duplicate edits, duplicate commands)
- **Session resume** sees orphaned `tool_use` without `tool_result` → API 400 error → session unresumable
- **Compaction** may corrupt the orphaned pair further (#8484, #14173)

### Our data: 31 orphans in current session alone

```
Tool        Total  Orphans  Rate
Bash         323     23     7.1%
Edit          51      4     7.8%
Read          33      2     6.1%
WebFetch       9      2    22.2%
```

Across 1,571 sessions: **8,007 orphaned tool calls out of 148,444** (5.4%).

### The cache multiplier

Each orphan makes the problem worse economically:
- Tool executes but result lost → model re-prompts → extra turn
- If the orphan caused a stall > 5 min → prompt cache TTL expires → 10x token cost for entire context
- If cache miss triggers compaction → another 500K-800K tokens consumed

### Related issues

- #6836 — orphaned tool_use/tool_result (150+ reports, 43 comments)
- #31328 — JSONL writer drops assistant entry during parallel tool calls
- #31330 — Parallel tool results corrupted after session resume
- #27052 — ESC during task → duplicate API requests → unrecoverable 400 error loop
- #29598 — Tool result block missing corresponding tool use block
- #14173 — Compaction error: orphaned tool_result despite valid history
- #8484 — Compaction corrupts tool use/result pairs (12 comments)

### The fix (proposed in our original analysis)

Make `insertMessageChain()` atomic — write the entire chain in a single `appendToFile()` call:

```js
async insertMessageChain(messages) {
  const serialized = messages.map(m => JSON.stringify(m)).join('\n') + '\n';
  await this.appendToFile(sessionFile, serialized);  // single write = atomic
}
```

### Why this is different from streaming hangs

Root cause #1 (streaming hang): request sent → SSE connection dies → client waits forever → watchdog fixes this.

Root cause #3 (tool result loss): tool executes → result in memory → **JSONL writer race condition** → result lost locally → model waits for tool_result that will never come → internal timeout fires → request retries automatically → but now without tool_result → orphan.

This explains a pattern we observed: after a tool completes, the session shows "Contemplating..." for 2+ minutes with minimal tokens. It's not slow generation — the model is **waiting for a tool_result that got lost in the local JSONL writer**. Eventually an internal timeout fires and the request retries, but the tool_result is already gone.

The watchdog (`CLAUDE_ENABLE_STREAM_WATCHDOG=1`) helps with streaming stalls (root cause #1) but **does not fix** the JSONL writer race condition (root cause #3). These are two separate bugs with separate fixes needed.

--- Comment 15 ---
Author: nullbio
Date: 2026-03-18T01:07:12Z

> **Another fun one**: after removing `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` to enable 1M context (see [#34143](https://github.com/anthropics/claude-code/issues/34143)), the auto-updater memory leak in v2.1.76 crashed our overnight session — **13.81 GB committed memory**, Bun panic after 12 hours, all work lost.
> 
> So to recap, in the last 48 hours:
> 
> 1. Streaming hangs (this issue) — still not fixed in v2.1.77
> 2. Complete system deadlock requiring hard power-off (comment above)
> 3. Auto-updater memory leak crashing a 12-hour session ([Auto-updater memory leak crashed 12-hour session (v2.1.76) — 13.81 GB committed, Bun panic #35171](https://github.com/anthropics/claude-code/issues/35171))
> 
> Three different bugs, three different mechanisms, zero hours of uninterrupted work.
> 
> v2.1.77 changelog says the auto-updater leak is fixed, and ESC is "improved" for non-streaming requests. Streaming timeout — still missing.

Glad you mentioned the 1m context bug. I probably would have been using 200k for another few months if I didn't see this.

Sad that they're getting telemetry on this issue and have done nothing about it for months.

I wonder if they're going to actually fix their server issue, or they're planning on just deploying this watchdog and calling it a day. 

@kolkov How did you manage to deobfuscate the source?

--- Comment 16 ---
Author: kolkov
Date: 2026-03-18T04:48:11Z

@nullbio It's not really obfuscated — just minified. `npm pack @anthropic-ai/claude-code`, extract `cli.js` (12MB), and search with node scripts. Minified JS is surprisingly readable once you find the right entry points — function names are shortened but strings like `"cli_streaming_idle_timeout"` and `"CLAUDE_ENABLE_STREAM_WATCHDOG"` are preserved in plain text. We compared 12 versions this way.

--- Comment 17 ---
Author: kolkov
Date: 2026-03-19T05:19:56Z

**Update: Anthropic is actively working on the watchdog — v2.1.79 changed the timeout values**

We checked `cli.js` from the just-released v2.1.79 and found that the watchdog timeout values have been increased:

| Version | Warning timeout | Abort timeout | Enabled by default? |
|---------|----------------|---------------|---------------------|
| v2.1.50–v2.1.78 | 30s | 60s | No |
| **v2.1.79** | **45s** | **90s** | **Still no** |

This means:
1. **They're actively iterating on the watchdog** — the timeouts were tuned, not abandoned
2. The increase from 60s→90s suggests they saw **false positives** with Opus extended thinking (which can be silent for 60+ seconds)
3. But it's **still behind `CLAUDE_ENABLE_STREAM_WATCHDOG`** — not enabled by default

For those of you who enabled the watchdog based on our earlier recommendation — it still works, just with slightly longer timeouts after updating to v2.1.79. 90 seconds is a reasonable trade-off: long enough to avoid false positives on thinking-heavy Opus tasks, short enough to catch dead SSE connections (vs. the 2-hour TCP keepalive default on Windows).

**Recommended settings remain the same:**
```json
{
  "env": {
    "CLAUDE_ENABLE_STREAM_WATCHDOG": "1",
    "DISABLE_AUTOUPDATER": "1"
  }
}
```

The fact that they're tuning the timeouts but not enabling it by default is puzzling. Maybe they're getting close to a default rollout? Or maybe they want more data from users who opt in first.

Either way — we're on day 2 with the watchdog enabled and **zero streaming connection hangs**. Stalls over 2 minutes have completely disappeared.

**However**, the watchdog does NOT fix root cause #3: tool results getting lost in the local JSONL writer race condition. We're still seeing orphaned tool calls where the tool executes successfully (file written to disk, command completed) but the `tool_result` never gets recorded — the model doesn't know the tool succeeded. This causes "Contemplating..." delays of 2+ minutes while the model waits for a result that was lost locally. See our [detailed analysis above](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4074109620).

`insertMessageChain()` still uses a non-atomic for-loop in v2.1.79 — unchanged across all 6 versions we've checked (v2.1.74–v2.1.79). Nobody seems to be working on this one.

### Suggestion: Adaptive watchdog instead of fixed timeouts

The reason they increased from 60s to 90s is likely false positives — Opus extended thinking can be silent for 60+ seconds. But fixed timeouts are a blunt instrument:

- **90s is too long** for simple requests (response usually in 2-5s)
- **90s may be too short** for complex Opus thinking with 1M context (3+ min)

The real problem: the client doesn't know if silence means "model is thinking" or "connection is dead."

**The server knows.** Anthropic already sends SSE `:ping` comments as keepalive. Extend them with status:

```
Currently:    :ping

Better:       :ping {"status":"thinking", "queue_position":0}
              :ping {"status":"queued", "estimated_start_ms":2000}
              :ping {"status":"generating", "tokens_so_far":1200}
```

Then the client **knows** what's happening:
- `status: "thinking"` → model is working, reset timeout
- `status: "queued"` → in queue, wait
- No ping for 30s → connection dead → abort

This is standard practice for any realtime service — heartbeat with payload. No fixed timeouts needed, no false positives, no guessing.

@bcherny @wolffiex — Anthropic already does adaptive thinking (`thinking: { type: "adaptive" }`). An adaptive timeout using the same principle would solve this properly.

--- Comment 18 ---
Author: meraline
Date: 2026-03-19T05:32:08Z

[2026 03 19T05 23 53 723Z.txt](https://github.com/user-attachments/files/26106954/2026.03.19T05.23.53.723Z.txt)

I'm experiencing the same "Interrupted · What should Claude do instead?" issue on v2.1.79 (latest).

**Environment:**
- Claude Code: 2.1.79
- OS: Ubuntu Linux
- Auth: Claude Max subscription
- MCP servers configured (Google Calendar, Gmail — showing auth errors but unrelated)

**Debug log shows repeated error:**

TypeError: A.with is not a function
at cli.js:6953

This error appears 4+ times during a single session, triggered by each tool invocation (Bash, Grep, Read, etc.).

**Reproduction:**
1. Run `claude --debug`
2. Execute any tool call (e.g., search files, run bash command)
3. Tool call gets "Interrupted" without user input
4. Check debug log — `TypeError: A.with` appears

**Observations:**
- Happens on nearly every tool call, not just subagents
- Fresh session doesn't help — issue persists immediately
- Restarting Claude Code provides temporary relief (1-2 tool calls work, then breaks again)
- npm reinstall doesn't fix (2.1.79 is already latest)

**Important:** Claude sidebar chat in VS Code (using the same Claude Max subscription) works perfectly fine in parallel — no interruptions, no errors. 

This seems related to the internal JS error rather than abort state persistence. The `A.with` function call in minified code suggests a missing polyfill or incompatible runtime.

--- Comment 19 ---
Author: kolkov
Date: 2026-03-19T06:49:42Z

@meraline This looks like a different bug from the streaming hang issue. We checked:

1. **Not reproducible on Windows** — v2.1.78, `--debug` mode, no `A.with` errors in debug log
2. **`A.with` = `Array.prototype.with()`** — an ES2023 feature. We found 4 usages in cli.js (same count in v2.1.78 and v2.1.79): `snapshots.with(-1, ...)`, `content.with(-1, ...)`, etc.
3. This method requires **Node.js 20+** or **Bun 1.0+**. On Ubuntu, if Bun's bundled runtime has issues with this method, it would break on every tool call — exactly what you're seeing.

**Worth checking:**
```bash
# What Bun version is bundled?
claude --version

# Does your system Node.js support Array.with?
node -e "console.log([1,2,3].with(-1, 99))"
# Should print: [1, 2, 99]
```

The fact that VS Code sidebar works fine confirms it's a **runtime issue in the CLI binary**, not an API problem. VS Code extension uses a different runtime (Node.js from VS Code), while CLI uses bundled Bun.

You might want to file a separate issue for this — it's a Bun/runtime compatibility bug on Linux, not related to the streaming timeout issue tracked here.

--- Comment 20 ---
Author: kolkov
Date: 2026-03-19T10:01:20Z

**Update: No file locking on Read/Edit tools — concurrent agents can overwrite each other**

We checked cli.js for file locking patterns. Finding:

- **Config files** (`.claude.json`, `settings.json`) — use `proper-lockfile` with `.lock` files ✅
- **Session JSONL** (`history.jsonl`) — use `proper-lockfile` ✅
- **Session JSONL** (per-session `<id>.jsonl`) — **NO locking** ❌ (root cause #3)
- **Read/Edit/Write tools on user files** — **NO locking at all** ❌

This means when multiple agents work on the same file:
```
Agent 1: Read file.go    → gets version v1
Agent 2: Read file.go    → gets version v1
Agent 1: Edit file.go    → writes v2
Agent 2: Edit file.go    → writes v3, OVERWRITES Agent 1's changes!
```

The only protection is an optimistic check — "has the file been modified since last Read?" But this is a **TOCTOU race** (time-of-check-to-time-of-use). Between the check and the write, another agent can modify the file.

Combined with root cause #3 (non-atomic `insertMessageChain()` for session JSONL), this creates two levels of data loss:
1. **Session level**: tool_use/tool_result pairs getting orphaned in JSONL
2. **File level**: concurrent agents silently overwriting each other's edits

This is especially dangerous with agent teams (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) where multiple agents routinely work on the same codebase.

--- Comment 21 ---
Author: kolkov
Date: 2026-03-19T10:26:15Z

**Update: Debug log evidence — watchdog doesn't help when server sends pings but no content**

Ran with `--debug` flag and caught a live hang. Here's the debug log:

```
10:14:29 [ERROR] API error (attempt 1/11): undefined Request timed out.
10:15:18 [DEBUG] Stream started - received first chunk
10:15:22 [DEBUG] High write ratio: blit=0, write=72754 (100.0% writes)
10:15:22 [DEBUG] Full reset (scrollback changes): scrollbackRows=696
```

**What happened:**
1. Request sent to API → server accepted it
2. **4+ minutes of silence** in the UI (timer stuttering, tokens barely moving)
3. Watchdog (90s) did NOT fire — because **server was sending SSE ping events** that reset the watchdog timer
4. Eventually `API_TIMEOUT_MS` (600s default) fired → "Request timed out"
5. Retry succeeded after 49 seconds → first chunk received
6. Full scrollback reset → 100% write ratio → scroll jump to top (the scroll bug)

**This proves the adaptive timeout proposal is necessary.** The current watchdog resets on ANY SSE event, including `:ping` keepalive. If the server sends pings but doesn't generate content, the watchdog is useless — you sit there for the full `API_TIMEOUT_MS` (10 minutes!).

The fix is exactly what we proposed: **server-side status in ping events**:
```
:ping {"status":"thinking"}    → model working, wait
:ping {"status":"generating"}  → tokens flowing, all good
:ping {"status":"queued"}      → in queue, wait
No ping for 30s               → connection dead, abort
```

Without content-aware pings, there's a dead zone between watchdog (90s, bypassed by pings) and API timeout (600s) where the user just waits.

--- Comment 22 ---
Author: kolkov
Date: 2026-03-21T06:04:22Z

**Update: 6th Bun crash in 4 days — this one while agent was IDLE**

Adding to the growing list of Bun runtime failures. This crash is the most damning because the agent **wasn't doing anything** — it had finished all tasks and was sitting in standby.

```
Elapsed: 8 hours | RSS: 1.81GB | Commit: 10.60GB | Faults: 22M
panic: Illegal instruction (mimalloc scavenger crash)
```

10.6 GB committed memory accumulated in 8 hours of idle. mimalloc's garbage collector crashed during its own cleanup cycle.

6 crashes in 4 days, across v2.1.76–v2.1.80, with `DISABLE_AUTOUPDATER=1` and `CLAUDE_ENABLE_STREAM_WATCHDOG=1`. The watchdog helps with streaming stalls, but **cannot fix the runtime itself crashing.**

Full crash table and memory analysis: #36132

At this point we have three layers of problems, each requiring a different fix:
1. **Streaming stalls** → watchdog works (hidden behind env var) ⚠️
2. **JSONL race conditions** → `insertMessageChain()` still non-atomic after 8 versions ❌
3. **Bun runtime crashes** → fundamental, no workaround, affects idle processes ❌

Layer 1 has a fix that Anthropic won't enable. Layers 2 and 3 have no fix at all.

--- Comment 23 ---
Author: kolkov
Date: 2026-03-25T07:47:23Z

**Update: Switched from native (Bun) to npm (Node.js) — dramatic stability improvement**

After 6 Bun crashes in 4 days, 26 GB commit from 7 processes, IDE crashes, and system deadlocks — we decided to switch back from the native installer (Bun 1.3.11) to the npm package (Node.js v22.17.0). Same cli.js, same settings, different runtime.

```bash
# How we switched (keep your settings!)
cp -r ~/.claude ~/.claude-backup          # backup first
rm ~/.local/bin/claude.exe                # remove native binary (NOT claude uninstall!)
npm install -g @anthropic-ai/claude-code  # install npm version
```

### Results after first hours on Node.js

**Memory — night and day:**

| Metric | Bun (native) | Node.js (npm) |
|--------|-------------|--------------|
| Commit per process | 1-15 GB (grows forever) | **300-500 MB (stable)** |
| Commit ≈ RSS ratio | Commit 10-15x larger than RSS | **Commit ≈ RSS** |
| 5 processes total | 26 GB commit | **1.6 GB commit** |
| System RAM used | 70%+ (constantly swapping) | **47% (21 GB free)** |
| Memory over time | Grows 0.6-5 GB/hour | **Flat or decreasing** |

**Stability:**
- 0 mimalloc crashes (impossible on Node.js)
- 0 "Tool bash not found" (no memory corruption)
- 0 system deadlocks
- 0 IDE crashes from memory pressure
- V8 GC actually returns memory to OS (mimalloc never did)

**What still remains (cli.js / server-side):**
- Streaming stalls — still happen (server-side issue)
- Tool result loss — `insertMessageChain()` for-loop still non-atomic

**What ALSO disappeared (we thought it was Ink, it was Bun):**
- Scroll resets (`Full reset (scrollback changes)`) — **316 per session on Bun → 0 on Node.js**
- Input field rendering corruption — text appearing below prompt, garbled input — **gone**
- Scrolling history back and forth works smoothly — no jumps, no discomfort
- We originally attributed all of this to Ink's renderer (#3648, 👍694). Debug logs prove it was Bun/mimalloc corrupting render state.

### The theory: Bun/mimalloc was THE root cause

We originally identified 3 separate root causes (#33949). But switching runtimes suggests many symptoms may have been **one root cause — mimalloc memory corruption**:

- "SSE connection dies" → corrupted HTTP client state
- "Tool result lost" → corrupted JSONL write buffer (partially — for-loop bug is real too)
- "Scroll jumps" → corrupted render state
- "Tool bash not found" → corrupted tools registry
- "21-thread deadlock" → corrupted event loop / mutex state
- "System freeze" → mimalloc scavenger blocking all threads

All of these disappear or dramatically reduce on Node.js/V8.

### Recommendation

If you're experiencing crashes, memory bloat, or instability — **try the npm install**. You lose ~200ms startup time and auto-updates, but gain a runtime that's been stable for 15+ years. The native Bun installer is the default, but the npm package is still fully supported (v2.1.83).

Note: You'll see an "npm deprecated" banner on each launch — it's just a message, ignore it.

--- Comment 24 ---
Author: yichao-mt
Date: 2026-03-27T05:20:26Z

## Watchdog timer bug in v2.1.84/v2.1.85: timer disarmed after initial response, never re-armed during thinking

### Environment
- Claude Code: v2.1.85
- OS: Ubuntu 20.04 (Linux)
- Model: Opus 4.6, also tested with Sonnet (medium effort)
- Network: VLESS tunnel (TUN mode via mihomo)
- Env vars: `CLAUDE_STREAM_IDLE_TIMEOUT_MS=120000`, `CLAUDE_ENABLE_STREAM_WATCHDOG=1`

### Finding

The streaming idle watchdog (`CLAUDE_STREAM_IDLE_TIMEOUT_MS`) added in v2.1.84 does not trigger during thinking phases. After reverse-engineering `cli.js` (v2.1.85), here is the root cause:

**Initialization** (called once at API call start):
```
b6 = o6(process.env.CLAUDE_ENABLE_STREAM_WATCHDOG)  // true
x6 = parseInt(process.env.CLAUDE_STREAM_IDLE_TIMEOUT_MS || "", 10) || 90000  // 120000
Z6 = x6 / 2  // 60000 (warning threshold)

X6()  // Arms watchdog timers (g6 = warning, B6 = abort)
```

**Timer setup** (`X6` function):
```
X6 = function() {
    K8();  // Clear existing timers
    if (!b6) return;
    g6 = setTimeout(warning_handler, Z6);   // Warning at 60s
    B6 = setTimeout(abort_handler, x6);     // Abort at 120s → calls J6()
}
```

**The bug**: `X6()` is called **once** at API call start. When the initial SSE response arrives (~3.9KB of headers/initial data), `K8()` clears the timers. During the thinking phase (no SSE events for minutes), **`X6()` is never re-called** to re-arm the watchdog.

### Evidence

TCP connection analysis via `ss -tnpi`:
- `lastsnd:290688 lastrcv:290968` — **290 seconds** with zero application data
- `lastack:2828` — TCP keepalive ACKs still flowing (connection alive at TCP level)
- `bytes_received:3928` — frozen at initial response size
- Connection state: ESTAB (not half-open)

The 120s watchdog timeout was exceeded by 170 seconds without triggering.

### Suggested fix

The chunk/event handler should call `X6()` (or equivalent) to reset the watchdog timer whenever an SSE event (including `:ping`) is received. This way, the timer is always counting from the **last received event**, not from the API call start.

```javascript
// In the SSE event handler:
stream.on("event", () => {
    X6();  // Reset watchdog on every event
});
```

### Impact

This makes the watchdog feature added in v2.1.84 effectively non-functional for the exact use case it was designed to address (thinking-phase hangs). Users behind proxies/VPNs experience 10-15% hang rate per the analysis in this issue, and currently the only workaround is manual ESC.

--- Comment 25 ---
Author: kolkov
Date: 2026-03-27T06:59:53Z

@yichao-mt Great reverse-engineering work and solid TCP evidence! We've been tracking the watchdog implementation across 11 versions (v2.1.74 through v2.1.85) and wanted to share our independent analysis — because **we see the timer code differently**, but your observed behavior is genuinely puzzling.

## Our code analysis: `X6()` IS called inside the for-await loop

We downloaded v2.1.84 and v2.1.85 via `npm pack`, extracted `cli.js`, and traced the brace-depth scoping carefully. Here's what we found on line 7682 of v2.1.85:

```javascript
// v2.1.85 line 7682 (deobfuscated, preserving structure)
// ── outer try block (pos 2273..11027) ──
try {
    // Watchdog functions defined first:
    let K8 = function() {             // clearTimers
        if (g6 !== null) clearTimeout(g6), g6 = null;
        if (B6 !== null) clearTimeout(B6), B6 = null;
    };
    let X6 = function() {             // armWatchdog
        K8();
        if (!b6) return;              // b6 = CLAUDE_ENABLE_STREAM_WATCHDOG
        g6 = setTimeout(warn,  Z6);   // Z6 = timeout/2 (45s default)
        B6 = setTimeout(abort, x6);   // x6 = timeout   (90s default)
    };

    // ... retry logic (Lk8 wrapper, do-while) ...

    // Watchdog state initialized (same scope, so X6 closure sees these):
    let b6 = o6(process.env.CLAUDE_ENABLE_STREAM_WATCHDOG);
    let x6 = parseInt(process.env.CLAUDE_STREAM_IDLE_TIMEOUT_MS || "", 10) || 90000;
    let Z6 = x6 / 2, y6 = false, c6 = null, g6 = null, B6 = null;

    X6();                              // initial arm

    try {
        for await (let w8 of t) {
            X6();                      // <-- re-arm on EVERY SSE event
            let W8 = Date.now();
            // ...stall detection, event processing...
        }
    }
}
```

We verified the scoping: the outer `try` block spans from pos 2273 to pos 11027. Both `X6` (the function) and `let b6/g6/B6` (the state) are inside this block. The `X6` closure captures the same `b6`, `g6`, `B6` bindings. The `for await` loop calls `X6()` at the start of each iteration. Same pattern in v2.1.84 (`j6()` instead of `X6()`).

**So according to the code, the timer should re-arm on every SSE event and fire 90s (or your 120s) after the last event.**

## The mystery: why didn't it fire?

Your TCP evidence is solid: `bytes_received:3928` frozen for 290 seconds. No SSE events, no pings, no data at all. The `for await` was blocked waiting for the next chunk. The watchdog should have fired at 120s. But it didn't.

Since `bytes_received` didn't grow, we can rule out SSE `:ping` keepalives resetting the timer — there were no pings. The timer was armed and should have been ticking.

**The most likely explanation we can think of: the JavaScript runtime's event loop was blocked.** `setTimeout` callbacks only fire when the event loop gets to process them. If the `for-await-of` on the SSE stream somehow blocks the event loop (rather than yielding back to it while waiting for the next chunk), then the timer callback would be starved.

This brings us to our key question:

## Are you running Bun or Node.js?

The shebang in v2.1.85 cli.js is `#!/usr/bin/env node`, but the Claude Code installer on some platforms bundles Bun as the actual runtime. You can check with:

```bash
# Which binary actually runs?
ls -la $(which claude)
# Or check the running process:
ps aux | grep claude | grep -v grep
```

This matters because:
- **Node.js**: `for await` on a ReadableStream yields to the event loop between iterations. `setTimeout` callbacks fire normally while waiting for the next chunk. The watchdog should work.
- **Bun**: Bun's async iteration implementation may differ. If Bun keeps the microtask queue busy or doesn't yield properly between async iterations on SSE streams, `setTimeout` macrotasks could be starved.

We've documented Bun-specific issues extensively (#35171, #36132) — mimalloc panics, memory leaks, different async behavior. This could be another Bun-vs-Node divergence.

## Second question: version match

Were you running v2.1.85 when you captured the `ss -tnpi` data? Or did you observe the hang on one version and then reverse-engineer a different one? The obfuscated names change between builds (v2.1.84: `j6`/`t6`, v2.1.85: `X6`/`K8`), and while the logic appears identical between v2.1.84 and v2.1.85, confirming the exact match helps.

## Context: our watchdog research

We've been tracking this since v2.1.74 across 11 versions. Key findings:
- Watchdog code has existed since ~v2.1.50, disabled by default behind `CLAUDE_ENABLE_STREAM_WATCHDOG`
- v2.1.79 bumped timeouts from 30s/60s → 45s/90s
- v2.1.84 made it configurable via `CLAUDE_STREAM_IDLE_TIMEOUT_MS` (changelog confirms)
- v2.1.84 also added stall detection (30s gap, warning only) and `x-client-request-id` header for debugging
- v2.1.85 has zero watchdog changes vs v2.1.84
- The `armWatchdog()` call has been inside the for-await loop in all versions we checked

Your finding — that the watchdog doesn't fire in practice despite correct-looking code — is very valuable. If confirmed as a Bun event-loop issue, it means the watchdog is fundamentally broken on Bun runtime regardless of the JS code being correct.

## The deeper problem: fixed timeouts can't work

Even if the timer bug is fixed, the watchdog design has a fundamental flaw: **it can't distinguish a dead connection from a thinking model**.

We've documented a confirmed false-positive cycle on our side. An agent was rewriting a ~400-line article — a task that legitimately requires 2-3 minutes of Opus 4.6 extended thinking. Debug logs showed 3 watchdog aborts in 7 minutes:

```
90s: watchdog abort → non-streaming retry
90s: watchdog abort → non-streaming retry
90s: watchdog abort → non-streaming retry
→ task never completes
```

The loop: Opus thinks for 2+ min → watchdog fires at 90s → aborts → retries → Opus starts thinking again → watchdog fires again → infinite cycle. This is likely why Anthropic keeps the watchdog disabled by default — for complex tasks (long articles, large refactors, architectural analysis with 1M context), Opus thinking > 90s is *normal*.

No fixed timeout solves this:
- 90s too short → false positives on legitimate thinking (our case)
- 180s safer for thinking → 3 minutes staring at a dead connection before recovery
- 300s → usable only for hangs, not for stalls

**What's actually needed is context-aware detection** — the API server *knows* whether the model is actively generating or the connection is dead. An SSE heartbeat like `event: heartbeat\ndata: {"status":"thinking","elapsed_ms":95000}` would let the client distinguish the two cases trivially. The watchdog would only fire when heartbeats stop, never when the model is working.

## The elephant in the room: the runtime choice

This entire class of bugs — event loop blocking, `setTimeout` not firing during `for await`, Bun vs Node behavioral divergence, 12 MB minified single-file JS, SSE stream management via async iterators with subtle timer interactions — **wouldn't exist in a compiled language**.

A Go implementation with `select` on a channel + `time.After` is ~10 lines of unambiguous code where the timer is guaranteed to fire regardless of what other goroutines are doing. No event loop, no microtask vs macrotask distinction, no runtime divergence. The entire CLI binary would be ~15-20 MB statically linked (vs 12 MB of just the JS source, plus the Bun/Node runtime, plus native addons — totaling 100+ MB installed). A single goroutine per stream, a single `select{}` for timeout — the kind of code a junior engineer gets right on the first try.

We've measured: 7 Claude Code CLI processes consume 5.3 GB RSS and 87 GB virtual memory. An equivalent Go implementation would use ~350 MB (15x less). No `.node` native addon leaks (#23095), no mimalloc panics (#36132), no auto-updater memory leak accumulating 13.81 GB (#35171). No runtime choice to debate.

And memory management is perhaps the starkest difference. Both Bun and Node.js rely on garbage collectors that are optimized for throughput, not footprint — they grow the heap aggressively and return memory to the OS reluctantly, if at all. Bun's mimalloc is particularly aggressive: it retains freed virtual pages in thread-local segment caches, which is why you see `Commit: 13.81 GB` and `Commit: 15.40 GB` in our crash logs — the process held onto gigabytes of address space long after the actual data was gone. Node's V8 is better but still holds large heap reservations that Windows counts against commit charge, pressuring the page file and eventually other applications.

Go's runtime, by contrast, returns unused memory to the OS proactively via `madvise(MADV_DONTNEED)` on Linux and equivalent calls on Windows. A Go process that spikes to 2 GB during a large operation will drop back to 200 MB within minutes as the GC releases unused spans. There's no mimalloc segment cache hoarding, no V8 heap reservation that never shrinks. A 12-hour Claude Code session in Go wouldn't accumulate memory until the system lags — it would stay near its working set size for the entire duration.

This is not theoretical. Our #35171 documents a 12-hour session where Bun accumulated 13.81 GB committed memory before crashing with a mimalloc panic. Our #36132 documents 15.40 GB committed in a 23.7-hour session — without the auto-updater even being involved. In both cases, the system became sluggish hours before the crash because the OS couldn't reclaim memory from a process that wasn't using it but wouldn't let go.

The watchdog timer bug is a symptom. The root cause is building a latency-sensitive, long-running, network-dependent CLI tool on top of a single-threaded event loop runtime where "does my timer fire while my async iterator is blocked?" is a question that has different answers depending on which JS engine you're running, and where the memory allocator holds your system hostage for the duration of the session.


--- Comment 26 ---
Author: kolkov
Date: 2026-03-27T08:26:19Z

While investigating @yichao-mt's watchdog analysis above (and our [code review reply](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4140610390)), we traced the **full error path** after a watchdog abort and found a deeper bug:

**The non-streaming fallback for watchdog abort is unreachable dead code.**

The watchdog correctly aborts the hanging stream, but the resulting `AbortError` hits a `throw` before reaching the fallback code. Users see "Request timed out" instead of a transparent retry. The fallback code even has telemetry for `fallback_cause: "watchdog"` — someone wrote it specifically for this case, but it never executes.

Full analysis, code traces, and suggested fix: **#39755**

This means the watchdog feature (`CLAUDE_ENABLE_STREAM_WATCHDOG=1`) is doubly broken:
1. Timer may not fire on certain runtimes (per @yichao-mt's finding)
2. Even when it does fire, the recovery path is dead code (our finding)

This could explain why Anthropic keeps it disabled by default — in testing it would appear to make things worse (abort + error instead of abort + retry), but the root cause is a missed code path, not a design flaw.


--- Comment 27 ---
Author: kolkov
Date: 2026-03-27T09:54:35Z

**Storage architecture audit (2026-03-27):** We traced the full `~/.claude/` storage layout in v2.1.85. The `.claude.json` bloat from #5024/#7243 was "fixed" by moving history to per-session JSONL files — but the result is worse: **3.1 GB** across `~/.claude/projects/`, single sessions up to 203 MB, no rotation, no compression, no cleanup.

Locking is inconsistent: `history.jsonl` has `proper-lockfile` protection, but session JSONL files use raw `appendFile` with no locking (#31328), and `.claude.json` uses raw `writeFile` (#28922, reported 8 times).

Full audit with file layout, sizes, locking analysis, and architecture recommendations: #5024 ([comment](https://github.com/anthropics/claude-code/issues/5024#issuecomment-4141415942))


--- Comment 28 ---
Author: kolkov
Date: 2026-04-01T10:37:30Z

**Update (2026-04-01):** The source map leak in v2.1.88 confirmed all our reverse-engineering findings from this issue. We now have readable TypeScript with comments — the watchdog timing bug, the fallback dead code, the 5-level AbortController chain, all verified line by line.

What likely happened: we filed [#39755](https://github.com/anthropics/claude-code/issues/39755#issuecomment-4169001598) on March 27 asking for source access and tagging 17 Anthropic team members. Three days later, v2.1.88 shipped with a 59.7 MB source map. Since Claude Code writes 100% of its own code (Boris Cherny: "I haven't edited a single line since November"), we believe it read our issue and answered our request itself. The first AI whistleblower. 🤖

Full write-up: [We Reverse-Engineered 12 Versions of Claude Code. Then It Leaked Its Own Source Code.](https://dev.to/kolkov/we-reverse-engineered-12-versions-of-claude-code-then-it-leaked-its-own-source-code-pij)

Key findings from the source (services/api/claude.ts, 3,419 lines):
- **Watchdog initializes AFTER do-while** (line 1868 vs 1849) — the most vulnerable phase is unprotected
- **`releaseStreamResources()` aborts `undefined`** (line 1519) — watchdog abort is a no-op during initial connection
- **Fallback works in for-await, not in do-while** — exactly where 100% of our observed hangs occur
- **`Promise.race` without `.catch()`** in concurrent tool merger (`utils/generators.ts:57`) — one rejected generator kills all pending tool results
- We **patched cli.js** and proved it: watchdog fired for the first time ever in do-while phase, ESC aborts dropped 8.7×

v2.1.89 was released — source map removed, but **zero bug fixes** for any of the streaming issues we reported.

### How to fix it properly

**Minimal fix** (~30 lines in 3 files):
1. Move watchdog init before do-while in `claude.ts`
2. Add `AbortSignal.any([signal, watchdogController.signal])` — so watchdog can actually abort the request, not `undefined`
3. Check `streamIdleAborted` flag in catch block — let watchdog abort fall through to existing non-streaming fallback instead of throwing

**Proper fix** — move reliability logic to the open SDK (`@anthropic-ai/sdk`, MIT):
- Three-level timeout: connection (30s) → network idle with ping awareness (120s) → content idle (disabled)
- **Ping-aware adaptive watchdog**: The SDK currently ignores SSE ping events (`if(event==='ping') continue`). Pings are proof-of-life from the server — they prove the connection is alive and the model is working. The watchdog should use pings to distinguish two fundamentally different situations:
  - **Dead connection** (no data at all, no pings) → abort quickly (network idle timeout, 120s)
  - **Model thinking** (pings arriving, no content yet) → don't abort! The connection is alive, model is working. Optionally notify user: "thinking for 2m..." via `onPing` callback
  - This eliminates both problems at once: no false positives on Opus extended thinking (pings reset network timer), and fast detection of dead connections (no pings = abort)
- **Informational pings**: Currently SSE pings carry no payload — just `event: ping\ndata: {}\n\n`. The server could enrich them with diagnostic context: `data: {"status":"thinking","elapsed_ms":95000,"queue_position":3,"model_load":0.87}`. This gives the client everything it needs for intelligent UX: show "thinking for 1m 35s", warn "server load 87%", or notify "3rd in queue". All without a separate diagnostic channel — just richer ping events that already flow through the SSE connection
- Streaming retry and non-streaming fallback — in the SDK, not in 3,419 lines of closed cli.js
- One AbortController instead of five nested levels
- SSE ping events should carry **status context**: `event: ping\ndata: {"status":"thinking","elapsed_ms":95000}` — the client can then distinguish "connection alive, model working" from "connection dead". Current pings are opaque `:ping` comments with zero information — the most valuable signal (proof-of-life) is thrown away

**The right fix** — rewrite in Go:
- `context.WithTimeout` replaces the AbortController chain in one line
- Goroutines: render, input, and network in separate threads — no input latency during streaming (React single-thread problem with 470 `useState` hooks)
- 15 MB static binary instead of 13 MB minified JS + Node/Bun runtime + native addons
- `go test -race` catches every concurrency bug — like the `Promise.race` without `.catch()` in `utils/generators.ts:57` that silently drops tool results
- Every serious CLI tool is Go: Docker, Kubernetes, Terraform, GitHub CLI
- The Go ecosystem already has production-ready libraries for every component: [Phoenix TUI](https://github.com/phoenix-tui/phoenix) (Elm-inspired terminal framework, replacement for React/Ink), [stream](https://github.com/coregx/stream) (RFC-compliant SSE/WebSocket, replacement for SDK streaming), [signals](https://github.com/coregx/signals) (reactive state, replacement for 470 useState hooks), [coregex](https://github.com/coregx/coregex) (regex 3-3000× faster than stdlib), [uniwidth](https://github.com/unilibs/uniwidth) (Unicode width 4-46× faster, for TUI), [gosh](https://github.com/grpmsoft/gosh) (cross-platform shell), [fursy](https://github.com/coregx/fursy) (HTTP router with OpenAPI), [pubsub](https://github.com/coregx/pubsub) (messaging with DLQ)

The models are extraordinary. The CLI wrapper needs real engineering — or a different language entirely.


--- Comment 29 ---
Author: kolkov
Date: 2026-04-01T11:34:49Z

**Update to our [prompts comment](https://github.com/anthropics/claude-code/issues/33949#issuecomment-4055585574) (April 1, 2026):**

Thanks to the source map leak in v2.1.88, we can now provide **exact file paths and line numbers** for all fixes. No more reverse engineering needed.

### Updated Prompt 1: Fix streaming timeout — now with source references

```
File: src/services/api/claude.ts (3,419 lines)

The streaming idle watchdog (line 1868-1929) initializes AFTER the do-while
loop (line 1849-1856). This means the initial connection phase — waiting for
the first API response — is completely unprotected by the watchdog.

Move watchdog initialization (lines 1868-1929: streamWatchdogEnabled, 
STREAM_IDLE_TIMEOUT_MS, resetStreamIdleTimer) BEFORE the do-while on line 1849.

Additionally, releaseStreamResources() (line 1519) aborts `stream` and 
`streamResponse` — but both are undefined during do-while. Create a dedicated
AbortController for the watchdog:

  const watchdogController = new AbortController()
  const combinedSignal = AbortSignal.any([signal, watchdogController.signal])

Pass combinedSignal instead of signal to the withRetry options (line 1843).
In the watchdog timeout callback (line 1911), call watchdogController.abort()
before releaseStreamResources().

In the catch block (line ~2434), add:
  if (streamingError instanceof APIUserAbortError) {
    if (signal.aborted) throw streamingError      // user ESC
    else if (streamIdleAborted) { /* fall through to fallback */ }
    else throw new APIConnectionTimeoutError()     // SDK timeout
  }

This fixes 3 bugs in one change: timing, abort targets, and fallback reachability.
We patched the minified cli.js and proved it: ESC aborts dropped 8.7×.
```

### Updated Prompt 2: Ping-aware adaptive watchdog (NEW — not in original prompts)

```
File: @anthropic-ai/sdk, src/core/streaming.ts (line 78)

The SDK currently ignores SSE ping events:
  if (sse.event === 'ping') { continue; }

Pings are proof-of-life from the server. They should reset a network idle
timer without resetting a content idle timer. This distinguishes two scenarios:

1. Dead connection (no data, no pings) → abort after 120s (network timeout)
2. Model thinking (pings arriving, no content) → DON'T abort, notify user

Implement three-level timeout in the SDK:
- connectionTimeout (30s): initial HTTP response headers
- networkIdleTimeout (120s): any data including pings
- contentIdleTimeout (disabled/300s): content only, excluding pings

Add callbacks: onPing(), onNetworkIdleWarning(), onContentIdle()

Enrich ping events with diagnostic data:
  event: ping
  data: {"status":"thinking","elapsed_ms":95000,"queue_position":3}

This eliminates both false positives on Opus thinking AND slow detection
of dead connections. One mechanism, all cases covered.

This belongs in the open SDK (@anthropic-ai/sdk, MIT license), not in cli.js.
Every Anthropic API client benefits, not just Claude Code.
```

### Updated Prompt 3: Fix Promise.race tool result loss

```
File: src/utils/generators.ts (line 42-73, function `all()`)

The concurrent tool merger uses Promise.race with .then() but no .catch():

  const promise = generator.next().then(({ done, value }) => ({
    done, value, generator, promise
  }))
  // ← NO .catch()!

If any generator rejects, Promise.race propagates the rejection and ALL
other pending generators are silently abandoned — their results lost.

Fix: Add .catch() to convert rejections into done objects:

  const promise = generator.next()
    .then(({ done, value }) => ({ done, value, generator, promise }))
    .catch(err => ({ done: true, value: undefined, generator, promise, error: err }))

Handle the error field in the consumer loop: yield an error tool_result
instead of silently dropping the generator.

Note the TODO comment on line 64: "// TODO: Clean this up" — even the
developer (or Claude) knew this code needed work.
```

### Updated Prompt 4: Fix input latency during streaming

```
File: src/screens/REPL.tsx (5,005 lines, 875 KB — single component!)

The terminal UI uses React/Ink with 470 useState and 372 useEffect hooks.
During SSE streaming (10-50 events/sec), each event triggers setState →
React reconciliation → stdout.write. This blocks the single Node.js thread,
causing user input to queue behind renders.

Evidence from source: line 1318 uses useDeferredValue(messages) — they know
about this problem. The comment on line 1321 logs deferred message count.

This is architecturally unsolvable in React/single-thread:
- useDeferredValue = bandaid (defers render, doesn't eliminate blocking)
- setTimeout(0) yield in print.ts:1832 = bandaid (one tick yield)

Proper fix: separate render and input into different threads (Web Workers
or process.fork), or replace React/Ink with a lightweight terminal renderer
that doesn't require virtual DOM reconciliation.
```

All prompts updated with exact source references from the leaked v2.1.88 codebase. v2.1.89 has zero fixes for any of these issues — only the source map was removed.


--- Comment 30 ---
Author: devarda
Date: 2026-04-01T16:05:58Z

We should open source this, that's the root cause here.

---

### Issue #62148 — [FEATURE] Complete Message Output in Interactive Mode for Long-Running Automation Sessions

State: OPEN | #62148
Labels: enhancement, area:tools, area:cli

---



### Problem Statement

In interactive mode, claude's text output is often truncated when it decides to call a tool mid-sentence. The session `.jsonl` file records incomplete text fragments like:

```json
{"message": {"content": [{"type": "text", "text": "Now I need to check the current status of the deployment. Let me"}]}}
{"message": {"content": [{"type": "tool_use", "id": "...", "name": "mcp__kubernetes__get_pods"}]}}
```

The text "Let me" is cut off because claude immediately called a tool, leaving the reasoning incomplete.

### Proposed Solution

Add a session-level setting or CLI flag to control streaming behavior:

### Option A: New CLI flag
```bash
claude --complete-messages-before-tools
```

When enabled, Claude would buffer text output until reaching a natural stopping point (sentence boundary, paragraph break) before calling tools.

### Option B: Settings file option
```json
{
  "streaming": {
    "completeMessagesBeforeTools": true,
    "minCompletionDelay": 100
  }
}
```

### Option C: Extend `--include-partial-messages` to interactive mode
Allow `--include-partial-messages` to work without `-p`, and ensure the final complete message is always written to the session `.jsonl` file.

### Option D: Message completion callback
Provide a hook that fires when Claude completes a thought before tool execution, allowing external logging systems to capture the complete reasoning chain.


### Alternative Solutions

1. **Accept incomplete output**: Not viable for production automation systems that require audit trails
2. **Use `-p` mode repeatedly**: Loses session state, can't use `--resume`, defeats the purpose of interactive mode
3. **Post-process with LLM**: Expensive and unreliable to "guess" what Claude meant to say
4. **Increase polling interval**: Doesn't solve the fundamental issue of mid-sentence truncation
5. **Custom logging wrapper**: Cannot intercept internal streaming behavior

### Priority

High - Significant impact on productivity

### Feature Category

CLI commands and flags

### Use Case Example

I'm building an infrastructure automation system using Claude Code + MCP servers for multi-hour autonomous sessions. The workflow is:

1. Start Claude Code with logging: `claude --resume <session_id> --debug-file debug.log`
2. Claude monitors and manages infrastructure for hours, making hundreds of decisions
3. Generate audit reports linking:
   - Claude's reasoning (text output)
   - Tool calls (MCP operations)
   - System state changes (logs, metrics)

**Current issue**: Claude's reasoning is fragmented and incomplete, making it hard to understand decision chains like:

```
[10:30:40] Claude: "The pod restart count is increasing. I need to check the logs to"
[10:30:40] Tool: kubectl_logs(pod="api-server-xyz")
[10:30:43] Claude: "Found OOM errors. The memory limit needs to be increased. Let me upd"
[10:30:48] Tool: kubectl_patch(resource="deployment/api-server", patch=...)
```

Every sentence is cut off mid-thought, making audit logs nearly unreadable.

### Additional Context

- This affects any long-running automation workflow using claude + mcp
- The issue is more visible when claude makes rapid tool calls (common in automation scenarios)

# Comments on anthropics/claude-code#62148
Total: 0 comments

No comments on this issue.

---

### Issue #53954 — OTel enhanced telemetry beta: streaming mode (Agent SDK / ACP) only emits claude_code.llm_request — interaction/tool/tool.execution spans are missing

State: OPEN | #53954
Labels: bug, platform:macos, area:agent-sdk, stale

---

## Summary

When Claude Code CLI is launched via `@anthropic-ai/claude-agent-sdk`'s `query()` (as the Agent
SDK and ACP adapters do in practice), the native OpenTelemetry trace exporter only emits
`claude_code.llm_request` spans. The `claude_code.interaction`, `claude_code.tool`, and
`claude_code.tool.execution` spans documented in
<https://code.claude.com/docs/en/monitoring-usage> and
<https://code.claude.com/docs/en/agent-sdk/observability> are never created on this path, even
for runs that finish cleanly with `stop_reason=end_turn`.

Running the CLI directly with `-p` emits the full span tree as documented.

## Environment

- Claude Code CLI: `2.1.119` (latest at time of filing)
- `@anthropic-ai/claude-agent-sdk`: `0.2.119`
- `@agentclientprotocol/claude-agent-acp`: `0.31.1`
- Platform: macOS 14 (Darwin 25.4.0, arm64)
- Node: 22.14 / 23.9 (both reproduce)
- OTel backend: LangSmith OTLP ingress (`https://api.smith.langchain.com/otel`, `http/protobuf`)

## Reproduction

Identical OTel configuration, two launch paths, same prompt ("run `ls | head -3` and list the
files"):

### A. Direct CLI (`claude -p`) — ✅ full span tree

```bash
env -u CLAUDE_CODE_ENTRYPOINT -u CLAUDE_CODE_EXECPATH \
  CLAUDE_CODE_ENABLE_TELEMETRY=1 CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1 \
  OTEL_TRACES_EXPORTER=otlp OTEL_METRICS_EXPORTER=none OTEL_LOGS_EXPORTER=none \
  OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf \
  OTEL_EXPORTER_OTLP_ENDPOINT=https://api.smith.langchain.com/otel \
  OTEL_EXPORTER_OTLP_HEADERS="x-api-key=$LANGSMITH_API_KEY,Langsmith-Project=claude-code-probe" \
  OTEL_TRACES_EXPORT_INTERVAL=1000 \
  claude -p "run 'ls | head -3' and list the files" --permission-mode bypassPermissions
```

Result (trace_id shared across all spans):
- `claude_code.interaction` (root)
- `claude_code.tool`
- `claude_code.tool.execution`
- `claude_code.llm_request` (×2)

### B. Same prompt via Agent SDK / ACP — ❌ only `llm_request`

Using `claude-acp` (which calls `query()` from `@anthropic-ai/claude-agent-sdk`) under the exact
same OTel env, the only span that reaches the backend is a lone `claude_code.llm_request`. No
`interaction` / `tool` / `tool.execution` span is ever emitted — confirmed by querying every span
that shares the `llm_request`'s trace_id on the backend (count = 1).

## Root cause analysis

Grepping the CLI binary (`@anthropic-ai/claude-agent-sdk-darwin-arm64/claude`, v2.1.119):

- The interaction-span constructor `eF1(prompt)` (which calls
  `tracer.startSpan("claude_code.interaction", ...)` and honors inbound `TRACEPARENT` /
  `TRACESTATE`) is only invoked through the `mr_(prompt, async () => {…})` wrapper.
- `mr_` has two call sites, both in the "user input → agent loop" path
  (`query_process_user_input_start`), not on the streaming-input path.
- The CLI when spawned by Agent SDK runs with `--output-format stream-json --verbose
  --input-format stream-json` (bundled as a hardcoded flag list in
  `@anthropic-ai/claude-agent-sdk/sdk.mjs`). Prompts arrive as stream-json user messages over
  stdin, which does not appear to pass through `mr_`. Hence no interaction / tool / tool.execution
  span is ever created, only the `LU9(…)` call that wraps each model request fires and produces
  `claude_code.llm_request`.

This matches the docs' note that interactive sessions ignore TRACEPARENT / suppress these spans,
but the SDK-streaming path is not interactive in the user-facing sense — it is exactly the
headless embedding mode the observability docs describe as supported, so this feels like an
accidental gap rather than intentional behavior.

## Expected

Per
<https://code.claude.com/docs/en/agent-sdk/observability#read-agent-traces>, with
`CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` and `OTEL_TRACES_EXPORTER=otlp` set, every turn driven
through the Agent SDK should produce a `claude_code.interaction` root span, with
`claude_code.llm_request` and `claude_code.tool` (+ `claude_code.tool.execution` /
`claude_code.tool.blocked_on_user`) as children — the same tree produced by `claude -p`.

## Impact

Third-party ACP bridges and any tool that embeds the Agent SDK (our use case: a DeepAgents →
ACP → Claude Code bridge exporting to LangSmith) cannot observe tool-level activity of the inner
coding agent. The `llm_request` spans alone give model / tokens / latency per call but lose the
per-turn boundary and the tool-call structure that makes a trace useful for debugging agent
behavior.

## Suggested fix

Route the stream-json user-message code path through `mr_(prompt, …)` (or wherever in the
streaming event loop a new turn begins) so the interaction span wraps the same lifecycle it does
on the `-p` path. Tool spans are already created via `vU9` / `VU9` from the tool dispatch
site — they should then nest correctly under the interaction span.

## Workaround

For repositories that need visibility today, synthesize an equivalent tool-span tree from the
ACP `session_update` stream on the embedder side, using `tool_call` / `tool_call_update`
notifications keyed by `tool_call_id`. This duplicates what the CLI should be emitting but it
works around the missing spans.

# Comments on anthropics/claude-code#53954
Total: 0 comments

No comments on this issue.

---

### Issue #58429 — [A11y feature request] Built-in option to speak Claude's responses aloud

State: OPEN | #58429
Labels: enhancement, area:a11y, area:desktop


---

## Summary
Add a built-in option to have Claude's responses spoken aloud in the Claude Code desktop app. This benefits blind users, low-vision users, and anyone working hands-busy or hands-free.

## Proposal
Two patterns, either or both:

1. **User setting (opt-in, off by default)** — when enabled, completed Claude responses are read aloud automatically as soon as streaming finishes.
2. **Keyboard shortcut** — a binding (e.g. cmd+shift+R) that reads the most recent Claude response on demand.

Either pattern is well-established in accessibility tooling: think VoiceOver's "speak the focused item" or screen reader "read from here" commands.

## Why built-in beats a hook workaround
A hook-based version (`Stop` hook + `say`) is theoretically possible but has problems:
- The `Stop` hook fires on `/clear`, `/resume`, `/compact`, etc., not just on actual response completion.
- The hook payload likely does not contain the response text, so it has to scrape the transcript file.
- Markdown and code blocks sound terrible when read by raw text-to-speech (literal asterisks, backticks, "hash hash hash" for headings) — would need clean message data and intelligent rendering.
- No clean way to interrupt when the user starts typing the next prompt.

A built-in implementation would have access to clean message data, settings UI, proper interrupt handling on user input, and nicer voices than `say`.

## Context
I submitted the same feedback via the in-app `/feedback` channel and to support@anthropic.com so the team can dedupe.

I am Lead Accessibility Architect at Paramount Streaming, blind, daily VoiceOver user. Happy to help spec, test, or pilot.

# Comments on anthropics/claude-code#58429
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-12T17:31:31Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/45251
2. https://github.com/anthropics/claude-code/issues/45863
3. https://github.com/anthropics/claude-code/issues/42700

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: leonidb
Date: 2026-05-16T15:26:11Z

The three hook workaround problems you named are real, native is genuinely better. 
For macOS users who want something installable today, I just made Audio Recap https://github.com/leonidb/claude-code-audio-recap public.
I've been using and tweaking it for several weeks and it's been useful in practice. 

1. It reads the transcript file - no way around it, not ideal but works
2. Markdown sounding terrible - Audio Recap uses a Haiku call (using Claude Code) to generate a summarized one-sentence recap of the turn (e.g., "Edited auth.py and added the OAuth callback; tests passing") - a digest of what happened, not raw
markdown read aloud. Long replied messages do get markdown rewrites too (code blocks announced rather than read literally)
3. You can interrupt the narration by clicking escape

It's macOS-only for now (uses native  say/afplay). Summaries go through your existing Claude Code Haiku auth. No additional dependencies.

None of this replaces a native solution. But it handles your complaints until native lands.

---

### Issue #57099 — Notion MCP: notion-create-pages validation fails with misleading error when title contains special chars + body has substantial content

State: OPEN | #57099
Labels: bug, platform:macos, external, area:mcp


---

## Summary

The `notion-create-pages` tool (Notion MCP connector) fails validation with a misleading error when:
- The title contains certain special characters (notably `<>`, possibly others), AND
- The `content` field has substantial body content (more than a few hundred chars)

The error message is misleading — it claims the issue is on the `pages` parameter as a string with a 100-character limit, but the actual `pages` parameter is an array, and no documented field has a 100-char limit that's relevant here.

## Reproduction

**Failing call:**
```json
{
  "parent": {"type": "data_source_id", "data_source_id": "<uuid>"},
  "pages": [{
    "properties": {
      "Title": "Code <> Chrome xfer and Backup",
      ...other properties...
    },
    "content": "...several KB of valid markdown content..."
  }]
}
```

**Error returned:**
```
MCP error -32602: Input validation error: Invalid arguments for tool notion-create-pages: [
  { "expected": "array", "code": "invalid_type", "path": ["pages"],
    "message": "Invalid input: expected array, received string" },
  { "origin": "string", "code": "too_big", "maximum": 100, "inclusive": true,
    "path": ["pages"],
    "message": "Too big: expected string to have <=100 characters" }
]
```

The `pages` parameter is correctly formatted as an array of objects in the request, not a string. Both validation errors point at `pages` simultaneously, contradicting each other ("expected array, received string" + "expected string ≤ 100 chars on `pages`").

**Working call (same request, just removed `<>` from title):**
```json
{
  "parent": {"type": "data_source_id", "data_source_id": "<same uuid>"},
  "pages": [{
    "properties": {
      "Title": "Code Chrome xfer and Backup",
      ...identical other properties...
    },
    "content": "...identical body content..."
  }]
}
```
Returns 200 with a created page.

**Working call (same `<>` in title, but title-only no body):**
```json
{
  "parent": {...},
  "pages": [{"properties": {"Title": "Code <> Chrome xfer and Backup"}}]
}
```
Returns 200.

## Pattern

The combination of special characters in the title AND substantial body content triggers the validation error. Either alone is fine. The internal validation appears to JSON-stringify or HTML-escape the entire `pages` array when checking some path, and `<>` interacts badly with that path.

Notably, `notion-update-page` with `update_properties` accepts `<>` in the title fine — only `notion-create-pages` exhibits this.

## Impact

- Misleading error messages waste developer time. The "100-character limit" suggestion is a dead-end debugging trail since no documented field has that limit at the right scope.
- Requires a workaround pattern: create with empty/safe body, then `update-page` with `replace_content` to set the actual body. Two API calls instead of one.

## Suggested fix

Either:
1. Fix the input escaping/serialization on the create endpoint so it handles special chars correctly
2. At minimum, return a clearer error message that points at the actual problem (e.g., "title contains characters that conflict with internal escaping when combined with body content; please use update-page after create").

## Environment

- Claude Code v2.1.128 on macOS Sequoia (Darwin 25.3.0)
- Notion MCP connector via `https://mcp.notion.com/mcp` (or similar — accessed through Anthropic's MCP connector infrastructure)

# Comments on anthropics/claude-code#57099
Total: 1 comments

--- Comment 1 ---
Author: localden
Date: 2026-05-08T00:45:53Z

Thanks for the detailed report and the clear repro steps. We're investigating — this looks related to how tool-call inputs are streamed for parameters whose schema accepts more than one type, rather than anything specific to `<>` in the title.

While we look into it, setting `CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING=0` should avoid the issue. We'll follow up here with an update.

---

### Issue #56811 — [Bug] Compact command hangs remote client with partial results until desktop input received

State: OPEN | #56811
Labels: bug, platform:macos, area:ide, platform:intellij, platform:ios, stale


---

**Bug Description**
When executing a command like /compact claude remote to claude ios stops updating and shows partial results of the compact.  Connection stops working until input on the remote server end (my desktop) is received. This limits use of claude ios when away from the desk

Also, / skills don't seem to work when invoked from claude code remote client.  The happens in both current IntelliJ and Goland IDEs.  Have not tested claude CLI app outside of IDE.

**Environment Info**
- Platform: darwin
- Terminal: goland
- Version: 2.1.128
- Feedback ID: 5c4559df-0829-44fc-b53b-0fa5368930ec

**Errors**
```json
[{"error":"Error: NON-FATAL: Lock acquisition failed for /Users/pjdhunt/.local/share/claude/versions/2.1.128 (expected in multi-process scenarios)\n    at Nq6 (/$bunfs/root/src/entrypoints/cli.js:2764:2177)\n    at uGH (/$bunfs/root/src/entrypoints/cli.js:2764:1257)\n    at processTicksAndRejections (native:7:39)","timestamp":"2026-05-05T20:32:59.481Z"},{"error":"Error: EISDIR: illegal operation on a directory, read '/Users/pjdhunt/git/i2goSignals/pkg/goSetPush'\n    at q$H (/$bunfs/root/src/entrypoints/cli.js:1704:144)\n    at processTicksAndRejections (native:7:39)","timestamp":"2026-05-05T23:24:18.347Z"}]
```

# Comments on anthropics/claude-code#56811
Total: 4 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-06T20:55:13Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/45979
2. https://github.com/anthropics/claude-code/issues/33232
3. https://github.com/anthropics/claude-code/issues/52685

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: Fishyyyttv
Date: 2026-05-06T20:57:48Z

Seems like streaming/PTY buffering or a backpressure issue. Most common error I would say is the TTY/PTY buffering. Remote sessions (esp in IDE terminals) often:

-  buffter stdout until a newline or flush
- Or block when the consumer (iOS client) isn't reading fast enough

/compact produces long streaming output which makes this worse.

Another error could just be the IDE, JetBrains terminals are not "real" terminals they sit on top of a PTY abstraction, and since you said it happens in both IntelliJ and GoLand that can def not work. 

Try testing outside the terminal. Also skills might not be supported in a remote mode, IDE integrations may limit the skills. 

Error 1: Lock acquisition failed ... (expected in multi-process scenarios)
This is benign, multiple Claude processes tried to access the same version dir, which is not the main issue.

Error 2: EISDIR: illegal operation on a directory, read '/Users/.../goSetPush'
This can really break things. Something expected a file but got a directory.

but who knows I don't work for Anthropic lol

--- Comment 3 ---
Author: independentid
Date: 2026-05-07T03:08:28Z

Confirmed. The issue happens when running claude CLI in a terminal (outside of an IDE).

--- Comment 4 ---
Author: independentid
Date: 2026-05-07T18:11:29Z

Issue is similar to but not the same as Issue #52685

---

### Issue #43676 — [BUG] MCP tool_result delivery corrupts SSE streaming connection, causing TypeError: network error and conversation data loss on every tool call

State: OPEN | #43676
Labels: invalid, stale


---



### What's Wrong?

MCP tool call results corrupt the SSE streaming connection, causing TypeError: network error on every tool invocation and wiping entire conversations from history without recovery. The issue is 100% reproducible: every single call to an MCP tool that executes a shell command triggers a network stream failure in the Claude Desktop client. After a cluster of 4 to 6 calls the failure escalates to message_store_sync_loss_accepted, permanently destroying the conversation with no way to recover it. This regression was not present approximately two app versions ago.

### What Should Happen?

MCP tool calls should complete and return their result while the streaming SSE connection to api.anthropic.com remains fully stable. The conversation history should be preserved before, during, and after any number of tool call round-trips. The user should be able to invoke MCP tools repeatedly in a session without any risk of conversation data loss.

### Error Messages/Logs

```shell
Error Messages/Logs
Extracted verbatim from ~/Library/Logs/Claude/claude.ai-web.log on 2026-04-04. The following cluster repeats for every single MCP tool call across the entire session (16 occurrences today alone):
2026-04-04 16:39:12 [error] [COMPLETION] Request failed TypeError: network error
2026-04-04 16:39:12 [error] [COMPLETION] Not retryable error, throwing
2026-04-04 16:39:12 [error] [COMPLETION] Non-API stream error TypeError: network error
2026-04-04 16:39:12 [error] Uncaught (in promise) TypeError: network error
2026-04-04 16:39:16 [error] [COMPLETION] Failed all attempts to invalidate conversation tree with consistency=eventual [object Object]
2026-04-04 16:39:17 [warn]  [COMPLETION] message_store_sync_blocked [object Object]
Two separate occurrences escalated to full conversation destruction:
2026-04-04 17:50:48 [warn]  [COMPLETION] message_store_sync_loss_accepted [object Object]
2026-04-04 18:11:33 [warn]  [COMPLETION] message_store_sync_loss_accepted [object Object]
Total in claude.ai-web.log today: 37 network errors, 2 conversation wipe events.
Cross-referencing mcp-server-cortex.log (which timestamps in UTC, local timezone is UTC-3) confirms that every single network error fires at the exact moment a tool result is returned from the MCP server. Zero errors occur during idle periods. The most direct example: an MCP tool ran echo ok via SSH, completed in under 2 seconds, and triggered TypeError: network error at the precise millisecond the result arrived. This rules out timeout as the sole cause. The corruption occurs at result delivery, not during execution.
```

### Steps to Reproduce

1. Install Claude Desktop v1.569.0 on macOS (arm64).
2. Configure any MCP server that exposes a tool executing shell commands via child_process.spawn over stdio transport. The MCP server must use @modelcontextprotocol/sdk and communicate via stdin/stdout.
3. Start a new conversation in Claude Desktop.
4. Ask Claude to use the MCP tool to run any command, including trivially simple ones (e.g., echo hello, git status, ls).
5. Observe that ~/Library/Logs/Claude/claude.ai-web.log immediately logs TypeError: network error and Failed all attempts to invalidate conversation tree with consistency=eventual.
6. Repeat the tool invocation 3 to 5 more times in the same conversation.
7. Observe message_store_sync_loss_accepted — the entire conversation disappears from Claude Desktop with no recovery option.

No specific project, code, or repository is required. Any MCP server with a command-execution tool reproduces this immediately and consistently.


### Claude Model

Sonnet (default)

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

_No response_

### Claude Code Version

1.569.0 (darwin, arm64, Node 24.14.0)

### Platform

Anthropic API

### Operating System

macOS

### Terminal/Shell

Terminal.app (macOS)

### Additional Information

This bug has a direct financial impact. Each destroyed conversation contains work performed against the Anthropic API. Tokens are consumed and billed during the session. When the conversation is wiped by message_store_sync_loss_accepted, all context, tool results, and progress are permanently lost. The user must start over, re-consuming tokens for the same work. On a heavy development day (274 MCP tool calls logged today), this represents substantial wasted spend on a Team subscription.
The regression aligns with a recent Claude Desktop update. Prior versions of the app handled MCP tool call round-trips without any streaming disruption.
A note that may assist the engineering team: a recent Claude Code release added CLAUDE_STREAM_IDLE_TIMEOUT_MS to configure the streaming idle watchdog threshold, defaulting to 90 seconds. It is possible the same watchdog is active in Claude Desktop's streaming layer and is being triggered not by idleness but by the act of flushing a tool_result chunk — particularly for tool calls that involve subprocess execution and produce buffered output. The corruption consistently fires at result delivery rather than during execution, which points to a flush, chunk framing, or connection state management issue introduced in a recent build.
Full log files attached here:

~/Library/Logs/Claude/claude.ai-web.log
~/Library/Logs/Claude/mcp-server-cortex.log
~/Library/Logs/Claude/main.log

[claude.ai-web.log](https://github.com/user-attachments/files/26484867/claude.ai-web.log)

[mcp-server-cortex.log](https://github.com/user-attachments/files/26484868/mcp-server-cortex.log)

[main.log](https://github.com/user-attachments/files/26484869/main.log)

# Comments on anthropics/claude-code#43676
Total: 5 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-04-04T22:04:06Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/43642
2. https://github.com/anthropics/claude-code/issues/31752
3. https://github.com/anthropics/claude-code/issues/38437

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: computerdab
Date: 2026-04-04T22:11:04Z

This is not a duplicate of any of the three referenced issues.

**vs #43642 (listed as duplicate of itself):** #43642 is my own related issue filed the same day. They describe different failure modes. #43642 is triggered by a per-turn call count threshold (3+ sequential calls, partial success before crash, fresh conversation sometimes recovers). This issue (#43676) triggers on every single tool call regardless of count, produces 37 network errors in a single session, and in 2 separate occurrences escalated to message_store_sync_loss_accepted with permanent conversation destruction. Different trigger, different severity, different failure path.

**vs #31752 (SSE stream drops with 409 Conflict):** The failure in #31752 is an HTTP 409 status code during SSE reconnection. My error is TypeError: network error firing at result delivery, not during reconnection. The transport corruption happens at the moment a tool_result chunk is flushed, confirmed by millisecond-level timestamp cross-correlation between mcp-server-cortex.log (UTC) and claude.ai-web.log. No HTTP 409 appears anywhere in my logs.

**vs #38437 (proxy silently hangs on tool_use results):** A hang means the process stalls waiting for a response that never arrives. My bug is the opposite: the error fires immediately and noisily at result delivery. The conversation destruction (message_store_sync_loss_accepted) also has no equivalent in a hang scenario.

Supporting evidence attached to the original report: claude.ai-web.log, mcp-server-cortex.log, and main.log, with 37 network errors and 2 conversation wipe events recorded today alone. This is a regression in Desktop v1.569.0 not covered by any of the three referenced issues.

--- Comment 3 ---
Author: computerdab
Date: 2026-04-05T00:14:13Z

<!DOCTYPE html><div tabindex="-1" cid="n3" mdtype="hr" class="md-hr md-end-block" style="box-sizing: border-box; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><br class="Apple-interchange-newline"><hr style="box-sizing: content-box; height: 2px; margin: 16px 0px; border: 0px; padding: 0px; background-color: rgb(231, 231, 231); overflow: hidden;"></div><p cid="n4" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="strong" class="md-pair-s" style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Update: DevTools trace and HAR analysis confirm client-side stream teardown</span></strong></span></p><p cid="n5" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Following guidance from Anthropic support, I enabled DevTools on Claude Desktop (</span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">allowDevTools: true</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> in </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">developer_settings.json</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">) and captured a full Network + Console trace during a reproducible failure session. The HAR file was exported and analyzed. Here is what the data shows.</span></p><div tabindex="-1" cid="n6" mdtype="hr" class="md-hr md-end-block" style="box-sizing: border-box; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><hr style="box-sizing: content-box; height: 2px; margin: 16px 0px; border: 0px; padding: 0px; background-color: rgb(231, 231, 231); overflow: hidden;"></div><p cid="n7" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="strong" class="md-pair-s " style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Test setup</span></strong></span></p><ul class="ul-list" cid="n8" mdtype="list" data-mark="-" style="box-sizing: border-box; margin: 0.8em 0px; padding-left: 30px; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><li class="md-list-item" cid="n9" mdtype="list_item" style="box-sizing: border-box; margin: 0px; position: relative;"><p cid="n10" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0px 0px 0.5rem; white-space: pre-wrap; position: relative;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Claude Desktop 1.569.0, macOS arm64, Apple Silicon</span></p></li><li class="md-list-item" cid="n11" mdtype="list_item" style="box-sizing: border-box; margin: 0px; position: relative;"><p cid="n12" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0px 0px 0.5rem; white-space: pre-wrap; position: relative;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">6 stdio MCP servers configured, including a custom Cortex server that executes shell commands via </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">child_process.spawn</code></span></p></li><li class="md-list-item" cid="n13" mdtype="list_item" style="box-sizing: border-box; margin: 0px; position: relative;"><p cid="n14" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0px 0px 0.5rem; white-space: pre-wrap; position: relative;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Reproduction prompt: asked Claude to run </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">echo hello</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">, then </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">echo world</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">, then </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">echo done</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> in a single turn</span></p></li><li class="md-list-item" cid="n15" mdtype="list_item" style="box-sizing: border-box; margin: 0px; position: relative;"><p cid="n16" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0px 0px 0.5rem; white-space: pre-wrap; position: relative;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">DevTools Network tab open with Preserve log enabled throughout</span></p></li></ul><div tabindex="-1" cid="n17" mdtype="hr" class="md-hr md-end-block" style="box-sizing: border-box; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><hr style="box-sizing: content-box; height: 2px; margin: 16px 0px; border: 0px; padding: 0px; background-color: rgb(231, 231, 231); overflow: hidden;"></div><p cid="n18" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="strong" class="md-pair-s " style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">HAR analysis: 4 POST completion requests captured</span></strong></span></p><p cid="n19" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">The HAR recorded every network request during the failing session. There were 4 POST requests to the completion endpoint for the conversation that failed:</span></p><figure class="md-table-fig table-figure" cid="n20" mdtype="table" style="box-sizing: border-box; margin: 1.2em 0px; overflow-x: auto; max-width: calc(100% + 16px); padding: 0px; cursor: default; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;">
# | Endpoint | HTTP Status | Response size | Time
-- | -- | -- | -- | --
1 | /completion | 200 OK | 0 bytes | 2,950ms
2 | /completion | 200 OK | 0 bytes | 5,937ms
3 | /retry_completion | 200 OK | 0 bytes | 16,711ms
4 | /retry_completion | 200 OK | 14,091 bytes | 29,273ms

</figure><p cid="n51" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Requests 1, 2, and 3 each received HTTP 200 from the server and then delivered zero bytes before the connection was reset (</span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">net::ERR_CONNECTION_RESET</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">). Request 4 eventually succeeded after 29 seconds, returning a complete SSE stream ending with </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">message_stop</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">.</span></p><p cid="n52" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">This pattern proves the server was healthy and accepting requests throughout the entire session. The failure is not a server-side rejection. The failure is not a payload size issue (the commands are trivially small). The failure is not a timeout during tool execution. The SSE stream is being torn down inside the Claude Desktop renderer process immediately after the 200 header is received, before a single event byte is delivered.</span></p><div tabindex="-1" cid="n53" mdtype="hr" class="md-hr md-end-block" style="box-sizing: border-box; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><hr style="box-sizing: content-box; height: 2px; margin: 16px 0px; border: 0px; padding: 0px; background-color: rgb(231, 231, 231); overflow: hidden;"></div><p cid="n54" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="strong" class="md-pair-s " style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Console trace at the moment of failure</span></strong></span></p><p cid="n55" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">The following cluster appeared in DevTools Console on every failing request, corroborating the Network tab:</span></p><pre class="md-fences md-end-block md-fences-with-lineno ty-contain-cm modeLoaded" spellcheck="false" lang="" cid="n56" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); font-size: 0.9em; display: block; break-inside: avoid; text-align: left; white-space: pre; background-image: inherit; background-position: inherit; background-size: inherit; background-repeat: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(248, 248, 248); position: relative; border: 1px solid rgb(231, 234, 237); border-radius: 3px; padding: 8px 4px 6px 0px; margin-bottom: 15px; margin-top: 15px; width: inherit; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;">&nbsp;<span role="presentation" style="box-sizing: border-box; padding-right: 0.1px;">[COMPLETION] Starting completion request (attempt 1, mode=legacy)</span><br>&nbsp;<span role="presentation" style="box-sizing: border-box; padding-right: 0.1px;">POST .../completion  net::ERR_CONNECTION_RESET  200 (OK)</span><br>&nbsp;<span role="presentation" style="box-sizing: border-box; padding-right: 0.1px;">[COMPLETION] Request failed TypeError: network error</span><br>&nbsp;<span role="presentation" style="box-sizing: border-box; padding-right: 0.1px;">[COMPLETION] Not retryable error, throwing</span><br>&nbsp;<span role="presentation" style="box-sizing: border-box; padding-right: 0.1px;">[COMPLETION] Non-API stream error TypeError: network error</span><br>&nbsp;<span role="presentation" style="box-sizing: border-box; padding-right: 0.1px;">Uncaught (in promise) TypeError: network error</span><br>&nbsp;<span role="presentation" style="box-sizing: border-box; padding-right: 0.1px;">[COMPLETION] Failed all attempts to invalidate conversation tree with consistency=eventual</span><br>&nbsp;<span role="presentation" style="box-sizing: border-box; padding-right: 0.1px;">[COMPLETION] message_store_sync_blocked {prev_tree_count: 2, new_tree_count: 0, tree_lost_count: 2}</span></pre><p cid="n57" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">The </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">200 (OK)</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> on the same line as </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">net::ERR_CONNECTION_RESET</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> is the key detail. The server accepted the request and began streaming. The Electron renderer then reset its own connection before reading a single byte.</span></p><div tabindex="-1" cid="n58" mdtype="hr" class="md-hr md-end-block" style="box-sizing: border-box; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><hr style="box-sizing: content-box; height: 2px; margin: 16px 0px; border: 0px; padding: 0px; background-color: rgb(231, 231, 231); overflow: hidden;"></div><p cid="n59" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="strong" class="md-pair-s " style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Cross-correlation with application logs</span></strong></span></p><p cid="n60" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">From </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">~/Library/Logs/Claude/claude.ai-web.log</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">, the same session produced 37 instances of this error cluster today. Two of those escalated to:</span></p><pre class="md-fences md-end-block md-fences-with-lineno ty-contain-cm modeLoaded" spellcheck="false" lang="" cid="n61" mdtype="fences" style="box-sizing: border-box; overflow: visible; font-family: var(--monospace); font-size: 0.9em; display: block; break-inside: avoid; text-align: left; white-space: pre; background-image: inherit; background-position: inherit; background-size: inherit; background-repeat: inherit; background-attachment: inherit; background-origin: inherit; background-clip: inherit; background-color: rgb(248, 248, 248); position: relative; border: 1px solid rgb(231, 234, 237); border-radius: 3px; padding: 8px 4px 6px 0px; margin-bottom: 15px; margin-top: 15px; width: inherit; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;">&nbsp;<span role="presentation" style="box-sizing: border-box; padding-right: 0.1px;">[COMPLETION] message_store_sync_loss_accepted</span></pre><p cid="n62" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Each </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">message_store_sync_loss_accepted</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> event wiped the entire conversation from Claude Desktop with no recovery option. All API tokens consumed during those sessions were billed but the output is permanently lost.</span></p><p cid="n63" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Cross-referencing </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">mcp-server-cortex.log</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> (which timestamps in UTC) against </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">claude.ai-web.log</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> confirms that every </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">TypeError: network error</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> fires at the exact millisecond a tool result is returned from the MCP server. Zero errors occur during idle periods or during tool execution. The corruption is triggered by result delivery.</span></p><div tabindex="-1" cid="n64" mdtype="hr" class="md-hr md-end-block" style="box-sizing: border-box; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><hr style="box-sizing: content-box; height: 2px; margin: 16px 0px; border: 0px; padding: 0px; background-color: rgb(231, 231, 231); overflow: hidden;"></div><p cid="n65" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 4; margin: 0.8em 0px; white-space: pre-wrap; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><span md-inline="strong" class="md-pair-s " style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">What is ruled out by this evidence</span></strong></span></p><ul class="ul-list" cid="n66" mdtype="list" data-mark="-" style="box-sizing: border-box; margin: 0.8em 0px 0px; padding-left: 30px; position: relative; caret-color: rgb(0, 122, 255); color: rgb(51, 51, 51); font-family: &quot;Open Sans&quot;, &quot;Clear Sans&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;Segoe UI Emoji&quot;, &quot;SF Pro&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-line: none; text-decoration-thickness: auto; text-decoration-style: solid;"><li class="md-list-item" cid="n67" mdtype="list_item" style="box-sizing: border-box; margin: 0px; position: relative;"><p cid="n68" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0px 0px 0.5rem; white-space: pre-wrap; position: relative;"><span md-inline="strong" class="md-pair-s " style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Server error</span></strong></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">: all requests return HTTP 200</span></p></li><li class="md-list-item" cid="n69" mdtype="list_item" style="box-sizing: border-box; margin: 0px; position: relative;"><p cid="n70" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0px 0px 0.5rem; white-space: pre-wrap; position: relative;"><span md-inline="strong" class="md-pair-s " style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">MCP server fault</span></strong></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">: </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">mcp-server-cortex.log</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> shows all tool calls completing successfully; </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">mcp.log</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> shows no disconnects</span></p></li><li class="md-list-item" cid="n71" mdtype="list_item" style="box-sizing: border-box; margin: 0px; position: relative;"><p cid="n72" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0px 0px 0.5rem; white-space: pre-wrap; position: relative;"><span md-inline="strong" class="md-pair-s " style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Payload size</span></strong></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">: failing commands are </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">echo hello</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">, </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">echo world</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">, </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">echo done</code></span></p></li><li class="md-list-item" cid="n73" mdtype="list_item" style="box-sizing: border-box; margin: 0px; position: relative;"><p cid="n74" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0px 0px 0.5rem; white-space: pre-wrap; position: relative;"><span md-inline="strong" class="md-pair-s " style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Network instability</span></strong></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">: the 4th retry succeeded immediately on the same connection</span></p></li><li class="md-list-item" cid="n75" mdtype="list_item" style="box-sizing: border-box; margin: 0px; position: relative;"><p cid="n76" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0px 0px 0.5rem; white-space: pre-wrap; position: relative;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">the 4th retry succeeded on the same connection with no changes </span></p><p cid="n85" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0.5rem 0px; white-space: pre-wrap; position: relative;"></p><p cid="n88" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0.5rem 0px; white-space: pre-wrap; position: relative;"><span md-inline="strong" class="md-pair-s " style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">Hypothesis</span></strong></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> A recent Claude Desktop release added </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">CLAUDE_STREAM_IDLE_TIMEOUT_MS</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">  (visible in the Claude Code changelog) to configure a streaming idle  watchdog defaulting to 90 seconds. It is possible the same watchdog is  active in Claude Desktop's streaming layer and is being incorrectly  triggered by the act of flushing a </span><span md-inline="code" spellcheck="false" class="md-pair-s" style="box-sizing: border-box;"><code style="box-sizing: border-box; font-family: var(--monospace); text-align: left; vertical-align: initial; border: 1px solid rgb(231, 234, 237); background-color: rgb(243, 244, 244); border-radius: 3px; padding: 0px 2px; font-size: 0.9em;">tool_result</code></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> chunk rather than by  genuine idleness. The result delivery timing correlation in the logs  supports this: the reset fires not during idle periods but at the exact  moment a tool result arrives. This points to a flush, chunk framing, or  connection state management regression introduced in v1.569.0. </span></p><p cid="n90" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0.5rem 0px; white-space: pre-wrap; position: relative;"></p><p cid="n93" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0.5rem 0px; white-space: pre-wrap; position: relative;"><span md-inline="strong" class="md-pair-s " style="box-sizing: border-box;"><strong style="box-sizing: border-box;"><span md-inline="plain" class="md-plain" style="box-sizing: border-box;">HAR file</span></strong></span><span md-inline="plain" class="md-plain" style="box-sizing: border-box;"> The full HAR file has been submitted privately via Anthropic support  ticket and is available to the engineering team on request. It was not  attached here to avoid exposing org ID and conversation content publicly. </span></p><p cid="n97" mdtype="paragraph" class="md-end-block md-p" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0.5rem 0px; white-space: pre-wrap; position: relative;"></p><p cid="n100" mdtype="paragraph" class="md-end-block md-p md-focus" style="box-sizing: border-box; line-height: inherit; orphans: 1; margin: 0.5rem 0px; white-space: pre-wrap; position: relative;"><span md-inline="plain" class="md-plain md-expand" style="box-sizing: border-box;">Marking this issue as distinct from the three flagged duplicates. The  HAR evidence above was not available in any of the referenced issues  and directly identifies the failure layer as the Claude Desktop renderer  stream consumer, not the MCP server, not the stdio transport, and not  the Anthropic API.</span></p></li></ul>

--- Comment 4 ---
Author: phfifofum
Date: 2026-04-22T06:58:15Z

Confirming this bug with additional detail: POST /tool_result → 404

Seeing the same regression on Claude Desktop (macOS) with a remote MCP server connected via mcp-remote.

Exact sequence in DevTools:

[COMPLETION] Starting completion request (attempt 1, mode=legacy)
Completion succeeds — Claude decides to call an MCP tool
[COMPLETION] Starting completion request (attempt 1, mode=legacy) — second completion starts immediately
POST /api/organizations/.../chat_conversations/.../tool_result → 404
"Tool result could not be submitted. The request may have expired or the connection was interrupted."
The tool itself runs fine — the MCP server receives the call and returns a result successfully (confirmed in server logs). The failure is purely on the Desktop→claude.ai result submission side.

Ruled out as causes:

Not a server-side regression — rolled back MCP server code to a version from before the issue appeared, identical error persists
Not a timeout — happens immediately on every call
Not related to coworkWebSearchEnabled — disabled it, no change
Reproducible on every tool call, every conversation, every turn
Environment:

Claude Desktop macOS
MCP server: remote HTTPS via mcp-remote (Streamable HTTP transport)

--- Comment 5 ---
Author: computerdab
Date: 2026-04-28T17:18:16Z

It’s good to see that other people are actively identifying this bug.

After contacting support repeatedly, and receiving zero responses, I decided to file chargebacks for all credit card transactions related to the Claude Desktop API since this bug appeared. The total is a few thousand dollars, so I hope this will get someone’s attention.

---

### Issue #59706 — Community Workaround for #22903 — CDP Connector gives Claude browser eyes/hands today

State: OPEN | #59706
Labels: enhancement, area:tools

---

## Community Workaround for #22903 — CDP Connector for Browser Screen Access

This is a working workaround for the feature requested in #22903 (bidirectional visual streaming / screen share for Claude Code), specifically for browser-based use cases.

### What this solves

For anyone needing Claude Code to "see" and interact with a browser — web CTF challenges, live app debugging, form automation — the Chrome DevTools Protocol (CDP) provides programmatic access that is actually **better than pixel-level screen sharing** for these cases. You get structured DOM data, not screenshots to interpret.

### How it works

Launch Edge or Chrome with the debug flag:

```powershell
Start-Process msedge -ArgumentList "--remote-debugging-port=9222","--user-data-dir=C:\Temp\edge-debug","--remote-allow-origins=*"
```

Then Claude drives the browser via a Python CDP connector:

```bash
# Read active tab content
python cdp_connector.py --text

# Execute JavaScript in page context
python cdp_connector.py --js "document.cookie"

# Click an element
python cdp_connector.py --click "#submit"

# Fill a form field
python cdp_connector.py --fill "#username" "admin"

# Navigate
python cdp_connector.py --goto "http://target"

# Dump cookies
python cdp_connector.py --cookies

# Clean tab screenshot -> saved to fixed path Claude can Read
python cdp_connector.py --screenshot
```

Claude reads DOM, executes JS, interacts with forms, grabs cookies and session state — all without native screen-sharing support in Claude Code.

For non-browser content (VM windows, binary challenge GUIs), a companion `screen_watcher.py` using `mss` handles pixel-level capture to a fixed path that Claude reads with its `Read` tool.

### Code

Both scripts: https://gist.github.com/Insider77Circle/4467352872d937055f5932c21f5d4b0e

### Relation to #22903

This doesn't replace the native feature request — full bidirectional screen streaming would cover all apps, not just browsers. But for the majority of web-focused use cases this works right now with no Claude Code changes required.

Built as part of the NEXUS pipeline at [@Insider77Circle](https://github.com/Insider77Circle).

# Comments on anthropics/claude-code#59706
Total: 0 comments

No comments on this issue.

---

### Issue #60166 — [BUG] v2.1.143: silent render-miss after upstream stream stall in skill-scoped turn (follow-up to #58897, fix incomplete)

State: OPEN | #60166
Labels: bug, has repro, area:ide, platform:vscode, area:skills


---

## What's Wrong?

In the VS Code extension webview, the final assistant text from a long, multi-tool-call turn does not render in the chat panel, even though it is fully persisted to the session JSONL on disk and is visible when the same session is opened via the CLI (`claude --resume <sessionId>`). The chat appears truncated right after the user prompt, with no error toast, no `Unhandled case: [object Object]` banner, and no further UI updates. Subsequent shorter assistant turns in the same session DO render normally.

This looks like the render-miss class of #58897 / #59054 / #58984 but is **not fixed in v2.1.143** (the version that closed those threads). I have two independent reproductions on v2.1.140 and v2.1.143 with identical signature.

The single structural difference between the not-rendered assistant entries and the rendered ones in the same JSONL is the `attributionSkill` field: the missing-from-GUI entries have `attributionSkill: "<skill-name>"` set (the turn was generated inside a slash-skill invocation), and the visible entries do not (turns outside any skill scope).

## What Should Happen?

The webview should render the assistant turn that is already persisted to the session JSONL, including assistant turns produced inside slash-skill invocations. `Developer: Reload Window` should re-render the full conversation from disk (matching the workaround reported by the author of #58984), but in my case it does not recover the truncated render either.

## Error Messages/Logs

No `Unhandled case` banner in the UI for this manifestation. Stall warnings and a Stop hook schema validation failure are logged at the moment the missing turn is persisted:

```
# session A: 2026-05-14, ext v2.1.140
2026-05-14T13:25:30Z  Stream started - received first chunk
2026-05-14T13:26:03Z  [WARN] [Stall] stream_idle_partial lastChunkAgeMs=15001 bytesTotal=655 idleDeadlineMs=300000
2026-05-14T13:26:29Z  [WARN] [Stall] stream_idle_partial lastChunkAgeMs=14999 bytesTotal=691
2026-05-14T13:26:44Z  [WARN] [Stall] stream_idle_partial lastChunkAgeMs=30001 bytesTotal=691
2026-05-14T13:27:01Z  [WARN] [Stall] stream_idle_partial lastChunkAgeMs=15001 bytesTotal=727
2026-05-14T13:27:03Z  [WARN] Streaming stall detected: 74.5s gap between events (stall #1)
2026-05-14T13:27:10Z  [WARN] Streaming completed with 1 stall(s), total stall time: 74.5s
2026-05-14T13:27:50Z  [WARN] Streaming stall detected: 36.2s gap between events (stall #1)
2026-05-14T13:28:54Z  Assistant text block (5649 chars, attributionSkill="<skill-name>") persisted to JSONL
2026-05-14T13:28:54Z  [DEBUG] Hook JSON output validation failed - Stop hook returned hookSpecificOutput.additionalContext which is not in the Stop schema

# session B: 2026-05-18, ext v2.1.143
2026-05-18T08:54:09Z  Stream started - received first chunk
2026-05-18T08:56:11Z  [WARN] Streaming stall detected: 45.8s gap between events (stall #1)
2026-05-18T08:56:39Z  Assistant text block (5253 chars, attributionSkill="<skill-name>") persisted to JSONL
```

In both sessions the assistant turn that fails to render is the first turn produced inside the slash-skill scope and follows at least one mid-turn upstream streaming stall.

## Steps to Reproduce

1. Open a fresh VS Code chat in the Claude Code extension on remote-SSH (laptop -> Linux VM via vscode-server) with `permissionMode: bypassPermissions`, model `claude-opus-4-7` 1M.
2. Invoke a slash-skill that takes a ~3 to 4 KB prompt and runs 10 or more tool calls (Bash, Read, MCP servers). Both my repros used `/triage` against a structured SNOW ticket input.
3. Wait for the upstream stream to stall mid-turn (`Streaming stall detected: >= 30s gap`), which on the corporate Prisma Access / Zscaler network path happens once or twice per long turn in my measurements (39 stall events in one workday, peak 131.5s).
4. Let the model produce its final assistant text (typically 5 to 6 KB of markdown with mixed RU and EN, multiple fenced code blocks).
5. Observe: the JSONL session file gets the assistant entry written (with `attributionSkill: "<skill-name>"`), but the VS Code chat panel stays truncated at the user prompt. No toast, no banner.
6. Try `Developer: Reload Window` and re-open the same session. The truncated render persists across reload.
7. Open the same session via CLI in a terminal pane on the same VM: `claude --resume <sessionId>`. The full assistant text is visible there.

Roughly 2 to 3 of every 10 long skill-scoped triage turns hit this for me; short non-skill turns (post-skill chat replies in the same session) always render fine.

## Claude Model

Opus (claude-opus-4-7, 1M context)

## Is this a regression?

I don't know

## Last Working Version

Unknown. The closely-related `Unhandled case` toast class was claimed fixed in 2.1.142 by claude[bot] auto-close on #58984 / #59054, but multiple users (bornsl0ppy, SpencerBelleau, kitbeaupre-boop) confirmed the toast still fires on 2.1.142 in the #58897 thread. One user (heidkaemper) reports 2.1.143 works for them on macOS, but I am hitting the render-miss class (no toast) on 2.1.143 with the signature above.

## Additional Context

- Extension: `anthropic.claude-code-2.1.143` (and earlier `anthropic.claude-code-2.1.140`)
- Spawn: confirmed in extension log, `version: 2.1.143`, native binary at `<ext-path>/resources/native-binary/claude`
- Permission mode: `bypassPermissions` (not Auto mode, so this is not the `toAutoClassifierInput` path mentioned in #58984)
- Host: Windows 11 (Azure AD Joined laptop) connecting via VS Code Remote-SSH to Linux VM running vscode-server; extension runs in the remote extension host
- Network: corporate Prisma Access / Zscaler proxy in front of `api.anthropic.com` (high stall rate, likely SSE buffering)

## Related issues

- #58897 (OP for the `Unhandled case` class, closed-as-fixed-in-2.1.142 by claude[bot])
- #59054 (duplicate, closed; my earlier 5th-repro comment is in the thread)
- #58984 (duplicate, closed; author notes Reload Window re-renders for them, which does NOT match my case)
- #55863 (open; structural sibling: extension recognizes message subtype, `inputStream.enqueue`, no webview renderer branch). The `attributionSkill: "<skill-name>"` field on the not-rendered entries is the equivalent signal here.
- #59030 (open; duplicate label, different trigger: Monaco editor worker)

## Asks

1. Reopen the underlying tracking issue (or scope a new one) for the render-miss class specifically. The toast and the silent render-miss are likely two outcomes of the same renderer fragility, but only one of them is currently marked fixed.
2. Confirm whether the webview switch in `webview/index.js` (the `QB1` assertNever pattern from #58897 OP) has an explicit branch for assistant turns with `attributionSkill` set, or whether those fall through to a no-op default.
3. Document a reliable workaround. CLI resume works for me, but I cannot expect non-CLI users to recover their truncated conversations this way.

Happy to share full session JSONLs and extension logs privately.

# Comments on anthropics/claude-code#60166
Total: 3 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-18T09:34:22Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/60140
2. https://github.com/anthropics/claude-code/issues/59326
3. https://github.com/anthropics/claude-code/issues/58897

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: romankanevsky
Date: 2026-05-18T10:03:13Z

Not a duplicate. The three proposed issues (#60140, #59326, #58897) are all in the **`Unhandled case: [object Object]` toast / banner family** - visible UI error surfaces. This issue is the **silent render-miss family** - no toast, no banner, no error message in the chat panel, just truncated render after the user prompt.

Per-issue comparison:

| Issue | Surface symptom | Trigger | Mine matches? |
|---|---|---|---|
| #58897 | `Unhandled case: [object Object]` banner from `assertNever` switch fallthrough | Unknown streaming event type | No - no banner in my repro |
| #60140 | Same toast + visible "response disappearing" | Webview's ~30-40s timeout vs SDK's `idleDeadlineMs=300000` | No - no toast in my repro |
| #59326 | Same toast + `had_error:true` | Bash `tool_dispatch_end outcome=error` cascading into stream end | No - no Bash tool failure in my repro |
| #60166 (this) | **Silent render-miss, no UI error of any kind** | **`attributionSkill: "<skill-name>"` set on the assistant turn (turn generated inside slash-skill scope) + upstream streaming stall** | n/a |

Differentiators that argue against duplicate-collapse:

1. **No visible error at all in my repro.** The webview does not show `Unhandled case`, does not show a banner, does not emit any toast. The chat panel simply stops rendering after the user prompt. Subsequent shorter turns in the same session render fine.
2. **Structural correlation in the JSONL.** The not-rendered assistant entries in my session JSONLs all have `attributionSkill: "<skill-name>"` set. The visible-rendered entries in the same JSONL do not. This field is set by the CLI when the turn is produced inside a slash-skill invocation (`/triage` in both my repros). The proposed-duplicates make no such structural claim.
3. **Maintainer label confirms.** The repo maintainers (or their auto-labeler) added `area:skills` to this issue and not to the three proposed duplicates. The skill-scope dimension is a real distinguishing axis.
4. **Empirically refutes the fix-claim on the toast family.** The bot auto-closed #59054 and #58984 as fixed-in-2.1.142 (per `claude[bot]` on 2026-05-15). My two repros are on 2.1.140 and 2.1.143. The 2.1.143 repro proves the underlying renderer fragility class is not actually closed on 2.1.143 for the skill-scoped silent-render-miss variant, even if the visible-toast variant is fixed.
5. **Reload Window behavior differs.** #58984 author reports `Developer: Reload Window` re-renders the conversation from disk. My case does not - reload does not recover the missing assistant turn. This argues the persistence/replay path is wired differently for skill-attributed turns.

The toast variant and the silent-render-miss variant may share an underlying renderer fragility (e.g. the `QB1` assertNever pattern from #58897's OP could have two failure modes: throw-and-toast for some unknown event types, swallow-and-no-render for others). But surface symptoms, recovery profile, structural JSONL correlate, and which build claims to fix them are all distinct. Collapsing this into the toast family loses the skill-scope and silent-render-miss signal that the JSONL provides.

Happy to attach the two affected session JSONLs privately for engineering diff.


--- Comment 3 ---
Author: acelarski
Date: 2026-05-21T11:07:44Z

Adding second-reporter datapoints that **directly confirm the `attributionSkill` hypothesis at the field level**, and broaden version coverage.

## Direct field-level confirmation of OP's `attributionSkill` hypothesis

I parsed the JSONL for all three of my render-drop repros and inspected the top-level `attributionSkill` field on the originally-failed-to-render assistant text blocks:

| Session ID | Active ext | Failed text size | `attributionSkill` value | User-facing trigger |
|---|---|---|---|---|
| `27c5bcbb-…` | v2.1.140 | 2,119 chars | `"TG_1_Architectural_Consultant"` | Slash command (`/TG_1_Architectural_Consultant`) — a prompt-injection command, not a `Skill` tool path |
| `87913e33-…` | v2.1.140 | 12,393 chars | `"what-context-needed"` | Slash command, but the model dispatched the `Skill` tool to load `what-context-needed` mid-turn; that became the scope of the failed text |
| `7b0a1d24-…` | v2.1.140 | 13,257 chars | `"TG_1_Architectural_Consultant"` | Slash command |

So **every render-drop on my side has `attributionSkill` set**. That matches the OP's structural observation 1:1. Adjacent successful sessions in the same workspace (commit-message generators, short non-skill turns) presumably do not — I haven't grepped exhaustively but the pattern fits.

One interesting nuance: `attributionSkill` in my data takes either the **slash-command name** (when the turn is scoped to a slash-command prompt-injection invocation) or the **sub-skill name** (when the model dispatched the `Skill` tool to load a helper skill mid-turn and the final text emission happened inside that scope). So the field captures both classes; the rendering bug fires whenever it is set, regardless of which class.

## Version coverage

- **Both `v2.1.140` and `v2.1.145`** exhibit the bug on my side. I originally hit it on `v2.1.145` (latest at the time), rolled back to `v2.1.140` hoping for a fix — bug persisted. `.obsolete` in `~/.vscode/extensions/` confirms the rollback took effect (`anthropic.claude-code-2.1.145-win32-x64: true`).
- Three render-drop repros in the same day (May 21 2026), all in the same VS Code instance on Windows 11 (native local — **no Remote-SSH, no Prisma/Zscaler proxy**).

## Tool-chain shape and `AskUserQuestion` observation

| Session ID | Tool chain before the failed text | Has `AskUserQuestion`? |
|---|---|---|
| `27c5bcbb-…` | `Agent` × 3, `Read`, `AskUserQuestion` × 4 | Yes |
| `87913e33-…` | `Skill`, `Read`, `Agent` × 2, `Glob` × 3, `Grep` × 2, `Read` | No |
| `7b0a1d24-…` | `Skill`, `Read`, `Agent`, `Glob` × 3, `Grep` × 2, `Read` | No |

In every case the final assistant text is fully present in the session JSONL at `~/.claude/projects/<project>/<session-id>.jsonl` and the model sees it in context on the next turn (it replies coherently, confirming server-side state intact). The renderer is the only failing layer.

**`AskUserQuestion` is NOT required to trigger the bug.** The shared factors are: `attributionSkill` set on the assistant turn, multi-tool chain prior to the final emission, and a large final text (~2 to 13 KB).

## Stream-stall evidence I cannot provide

I tried to pull the equivalent stream-stall log output the OP shared — every VS Code log directory on my system (`%APPDATA%\Code\logs\…`) is empty, going back at least a week. Either default builds don't write to that location on Windows, or the harness logs elsewhere. Pointer to the right log location for Windows users would help future repro reports.

That said, since my repros happen on a stable local Windows network with no corporate proxy, the **upstream-network-stall trigger from the OP may be sufficient but is not necessary**. The bug fires on me without any stall warning surfacing (or, possibly, with stalls that my client never logs visibly).

## Related observation (likely separate bug)

In the same day, one of my sessions (`c5bc54f9-…`, 12:42) hit a categorically different failure mode: **zero assistant text turns** in the JSONL (15 lines total, all tool-call and metadata blocks, no `assistant`/`text` content). The UI showed an extended working state then silence. This is NOT a render-miss — the model genuinely produced no text. Might be the same upstream stream-stall pathology hitting at a different lifecycle point, or might be unrelated. Mentioning it here so the maintainers can decide whether to track separately.

## Related issues — broader / sibling bug family

The duplicate-detection bot on a parallel report flagged this thread alongside two others that look like the same underlying class with different framing or surface symptom:

- **#59526** — *VSCode extension renderer disconnects from live stream during long multi-step tasks; work completes successfully in background* (macOS, v2.1.142). Same shape as the render-miss described here but framed without the skill-scope hypothesis — likely a **parent / broader-class description** of the same bug. Interestingly the OP there reports that **closing and reopening the panel restores full visibility**, which is the inverse of #60166's "`Developer: Reload Window` does not recover." Whether that's an OS difference (macOS vs Windows), a version difference (v2.1.142 vs v2.1.140/.143), or two distinct render paths within the same bug class is worth resolving.
- **#60002** — *VSCode extension: "Unhandled case: [object Object]" banner orphans response, leaves chat stuck at "Thinking…"* (Windows 11). Different visible surface (banner rendered) but same underlying impact (response done on agent side, lost to UI). Plausibly the visible-banner manifestation of the same stream-state-machine breakage that this thread sees as a silent drop.

If maintainers agree these are one bug, consolidating into a single tracker with three sub-cases (silent skill-scoped drop / silent broad multi-step drop / banner-orphan) would help avoid further duplicate splintering.

## What this changes for the fix priority

OP reported v2.1.143; I confirm v2.1.140 and v2.1.145. So the bug is not bracketed by any version in the current release line — it is reproducible on the current latest. The fix in #58897 (`Unhandled case` banner) was a different surface symptom of what is plausibly the same underlying stream-state-machine bug, and #60166's identification of `attributionSkill` as the structural correlate is now confirmed by an independent reporter on a different OS, different network, and different version pair.

Happy to share raw JSONL session structures privately with engineering if it helps narrow the fault.

---

### Issue #42671 — Remote Control: messages sent from phone do not arrive in CLI (one-way communication)

State: OPEN | #42671
Labels: bug, platform:macos, platform:ios


---

## Bug Report

### Environment
- CLI version: 2.1.90
- Auth: claude.ai Max plan
- OS: macOS Darwin 25.3.0 (Apple Silicon)
- Phone: iPhone (Claude Code mobile app)

### Steps to Reproduce
1. Run `/remote-control` in CLI terminal
2. Scan QR code on iPhone Claude Code app
3. Select the session (e.g., "remote-control-glowing-teapot")
4. Conversation from CLI is visible on phone ✅
5. Type and send a message from phone
6. **Message never appears in CLI** ❌

### Expected Behavior
Messages sent from the phone should appear in the CLI session and be processed.

### Actual Behavior
One-way communication only. CLI → Phone works (conversation visible). Phone → CLI does not work (messages are lost/never delivered).

### Troubleshooting Attempted
- Re-scanned QR code — same result
- Closed and re-selected the session — same result
- Restarted `/remote-control` with new QR — same result
- Verified no blocking env vars (`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, etc.) — all unset
- Auth is full-scope claude.ai (not API key)

### Screenshot
Phone shows the session list with multiple idle remote-control sessions. The selected session displays the conversation correctly but input is not transmitted upstream.

# Comments on anthropics/claude-code#42671
Total: 2 comments

--- Comment 1 ---
Author: xiaotonng
Date: 2026-04-09T13:34:08Z

The one-way communication problem with `/remote-control` is a known pain point — the phone-to-CLI path is fragile and depends on a relay that often silently drops messages. pikiclaw takes a different approach: it runs a local bridge that connects Claude Code directly to Telegram (or Feishu/WeChat) as a proper bidirectional channel, with streaming previews and full tool-use output sent back to your phone in real time. You can also use the web dashboard at `localhost:3939` as a standalone agent console with WebSocket-based streaming. Give it a try with `npx pikiclaw@latest`. GitHub: https://github.com/xiaotonng/pikiclaw

--- Comment 2 ---
Author: Snailflyer
Date: 2026-05-20T18:18:03Z

This looks like a false-liveness case: seeing the transcript on the phone only proves CLI -> phone rendering, not phone -> host ingress. I would split the diagnostics into three receipts: mobile send accepted by relay, relay delivered to the selected host/session, and the local CLI/TUI accepted or rejected that input. Without a host-side `input_accepted`/`input_rejected` event tied to the remote session id, the phone can look connected while user messages are being silently dropped. Do you see any local log or TUI event at the moment the phone message is sent?

---

### Issue #58648 — [BUG] CLI truncates a >~146 KB user message line on stdin when preceded by another NDJSON line (`--input-format stream-json`)

State: OPEN | #58648
Labels: bug, has repro, platform:linux, area:agent-sdk, area:cli


---



### What's Wrong?

When `claude` is invoked with `--input-format stream-json` and receives **two or more NDJSON lines back-to-back on a single stdin pipe** where one of them exceeds ~146 KB, that long line is silently truncated before parsing. The CLI logs `Error parsing streaming input line: …` on stderr and exits with code 1 without ever processing the message.

The bug is fully reproducible with `node:child_process` alone — no SDK required — but it affects 100% of `@anthropic-ai/claude-agent-sdk` consumers in practice, because the SDK always writes a `control_request:initialize` line before the first user message. As soon as a SDK consumer's first user prompt exceeds ~146 KB, the CLI errors out before the model is ever called.

Counter-experiments below show the trigger is specifically *two writes through the Node stdin pipe*, not the line size on its own — the same long line passes when written alone, or when piped via the shell.


### What Should Happen?

The CLI should parse a NDJSON line of arbitrary size on stdin regardless of what other lines preceded it on the same pipe. The user message should be parsed correctly, the turn should run, and a `result` event should be emitted on stdout.


### Error Messages/Logs

```shell
Error parsing streaming input line: {"type":"user","message":{"role":"user","content":[{"type":"text","text":"aaaa…aaaa
aaaa…aaaa
aaaa…aaaa
exit: 1

# SDK debug log (with DEBUG_CLAUDE_AGENT_SDK=1) shows the same:
[ProcessTransport] Writing to stdin: {"request_id":"…","type":"control_request","request":{"subtype":"initialize", …
[ProcessTransport] Writing to stdin: {"type":"user","message":{"role":"user","content":[{"type":"text","text":"aaaa…
[ProcessTransport] Write buffer full, data queued
Error parsing streaming input line: {"type":"user","message":{"role":"user","content":[{"type":"text","text":"aaaa… (truncated)
```

### Steps to Reproduce

1. Save the script below as `repro.mjs`.
2. Run `DEBUG_CLAUDE_AGENT_SDK=1 node repro.mjs`.
3. Observe `Error parsing streaming input line: …` on stderr and exit code 1.
4. Lower `SIZE` to `146_040` and re-run — it succeeds and a `result` event is printed.

```js
import { spawn } from "node:child_process";

const SIZE = 146_050; // 146_040 passes, 146_050 fails — threshold reproducible to ±10 bytes
const text = "a".repeat(SIZE) + "\n\nReply OK";

const initMsg = JSON.stringify({
  request_id: "r1",
  type: "control_request",
  request: { subtype: "initialize" },
}) + "\n";

const userMsg = JSON.stringify({
  type: "user",
  message: { role: "user", content: [{ type: "text", text }] },
  parent_tool_use_id: null,
  session_id: "",
}) + "\n";

const child = spawn("claude", [
  "--output-format", "stream-json",
  "--verbose",
  "--input-format", "stream-json",
  "--setting-sources=user,project,local",
  "--permission-mode", "acceptEdits",
], { stdio: ["pipe", "pipe", "pipe"] });

child.stderr.on("data", d => process.stderr.write(d));
child.stdout.on("data", d => process.stdout.write(d));
child.on("exit", code => console.log("\nexit:", code));

child.stdin.write(initMsg);
child.stdin.write(userMsg);
child.stdin.end();
```

**Threshold sweep** (`userMsg.length` = total bytes of the line, with `initMsg` ~80 bytes preceding it):

| `userMsg` bytes | Outcome              |
| --------------: | :------------------- |
|         146 174 | OK, `result` emitted |
|     **146 184** | **Parse error, exit 1** |
|         200 000 | Fails                |
|         500 000 | Fails                |

With a larger preceding line, the threshold shifts down by roughly the same amount — consistent with a fixed-size internal line buffer.

**Counter-experiments showing the trigger is the preceding line, not the line size itself:**

a) Drop the `initMsg` write and write only `userMsg` → the same payload works up to multiple MB:
```js
child.stdin.write(userMsg);   // userMsg.length = 2_000_000+
child.stdin.end();
```

b) Pipe both lines via the shell instead of via Node's `child.stdin`:
```bash
{ printf '%s' "$initLine"; printf '%s' "$userLine"; } | claude --input-format stream-json …
```
→ The same 147 KB user line is parsed correctly.

So the trigger is specifically: **two writes through a single Node child_process stdin pipe, where the second write exceeds ~146 KB**.


### Claude Model

Not sure / Multiple models

### Is this a regression?

No, this never worked

### Last Working Version

_No response_

### Claude Code Version

Tested on 2.1.92, 2.1.126 and 2.1.128

### Platform

Anthropic API

### Operating System

Other Linux

### Terminal/Shell

Non-interactive/CI environment

### Additional Information

# Comments on anthropics/claude-code#58648
Total: 1 comments

--- Comment 1 ---
Author: mar4r8k-femi
Date: 2026-05-19T09:58:47Z

Possibly related, possibly a separate bug with the same shape. Posting in case the data is useful for triage.

I hit silent-failure symptoms with the same fingerprint (`num_turns: 2`, `duration_api_ms: 0`, `input_tokens: 0`, `result: ""`, exit 0) on `claude -p` v2.1.110, but with a much lower threshold and on `--input-format text` (the default), not stream-json.

**Setup:** macOS 15.7.5 arm64, AWS Bedrock auth, a `SessionStart:startup` hook that emits ~3-4KB per `hook_progress`/`hook_response` event into the parent stream-json output before the user prompt is read.

**Threshold sweep**, synthetic prompt (`"Context for ignore: " + lorem-ipsum padding + "\n\nWhat is 2+2? Reply with just the digit."`) piped to `claude -p --output-format stream-json --verbose --model opus --permission-mode bypassPermissions`:

| Size (bytes) | input_tokens | duration_api_ms | num_turns | result |
| ------------ | ------------ | --------------- | --------- | ------ |
| 23,000       | 3            | 4186            | 1         | `"4"`  |
| 24,000       | 3            | 3332            | 1         | `"4"`  |
| 25,000       | 0            | 0               | 2         | `""`   |
| 28,000       | 0            | 0               | 2         | `""`   |
| 32,000       | 0            | 0               | 2         | `""`   |

Same silent-drop behavior across three input channels (all tested at 28KB):
1. Pipe to stdin (default `--input-format text`)
2. Positional argv (Node `spawn(claude, [...args, prompt])`, no shell)
3. `--input-format stream-json` with a `{type:"user",...}` line on stdin

The same 28KB content delivered via `--append-system-prompt <large content>` (argv flag value) succeeds with `input_tokens: 3, duration_api_ms: 3380, result: "4"`. That's the workaround I'm running on.

One difference from the OP: I never see `Error parsing streaming input line: ...` on stderr in any of the three input modes. The CLI exits cleanly with code 0.

Happy to share the raw stream-json dumps and the build script if useful.

---

### Issue #61201 — [BUG] Unicode BiDi isolate characters (FSI U+2068 / PDI U+2069) stripped on session resume

State: OPEN | #61201
Labels: bug, has repro, platform:linux, area:tui, area:a11y

---



### What's Wrong?


Unicode 6.3+ BiDi isolate characters -- First Strong Isolate (U+2068) and Pop Directional Isolate (U+2069) -- are correctly emitted by the model during live streaming and render RTL text properly in the terminal. However, when a session is resumed (`claude --resume` or `/resume`), these characters are stripped from the displayed output, causing Arabic/Hebrew/RTL text to lose its right-to-left directional formatting.

The characters **are saved correctly** in the session JSONL file (verified via byte inspection), but the rendering pipeline drops them when replaying conversation history.

Byte evidence from stored session:

```shell
$ grep -o $'\xe2\x81\xa8' ~/.claude/projects/.../<session-id>.jsonl | wc -l
31   # 31 FSI characters stored

$ grep -o $'\xe2\x81\xa9' ~/.claude/projects/.../<session-id>.jsonl | wc -l
31   # 31 PDI characters stored (matched pairs)
```

Extracted JSON from storage confirms correct structure:

```json
{
  "type": "assistant",
  "content": [{
    "text": "⁨أهم اللغات الحديثة مع مميزات وعيوب:⁩\n\n## ⁨١. TypeScript⁩\n..."
  }]
}
```

FSI/PDI are intact in storage, but absent from rendered output on resume.



### What Should Happen?

FSI (U+2068) and PDI (U+2069) characters should survive the full round-trip: model output -> JSONL storage -> session resume/replay -> terminal display. These are valid Unicode 6.3+ formatting characters (not legacy control characters) and are the only BiDi mechanism that works in Claude Code's Ink-based terminal renderer.

During live streaming, RTL text wrapped in FSI/PDI renders correctly. The same text should render identically when the session is resumed.

### Error Messages/Logs

```shell
No error messages. The characters are silently stripped -- RTL text displays as LTR (jumbled/reversed reading order) on resume, while it displayed correctly during the original live session.
```

### Steps to Reproduce

1. Create a custom output style at `~/.claude/output-styles/rtl-safe.md`:
   ```markdown
   ---
   name: RTL-safe
   description: Wrap RTL lines with Unicode BiDi isolates
   keep-coding-instructions: true
   ---
   
   When any line contains Arabic/Hebrew script characters, wrap that line
   with U+2068 (FSI) at the start and U+2069 (PDI) at the end.
   Do not wrap lines inside fenced code blocks.
   Skip pure English/Latin lines.
   ```

2. Activate via `/config` -> Output style -> RTL-safe

3. Start a new session: `claude`

4. Ask: "Reply in Arabic: brief overview of modern programming languages"

5. Observe: Arabic text renders correctly right-to-left during live streaming. Each line displays with proper RTL direction.

6. Exit the session.

7. Resume: `claude --resume` (select the session)

8. Observe: The same Arabic text now displays LTR -- words in reversed order, punctuation misplaced. The FSI/PDI isolates that made it render correctly are gone from the display.

9. Verify characters exist in storage:
   ```shell
   grep -c $'\xe2\x81\xa8' ~/.claude/projects/.../<session-id>.jsonl
   # Returns 1 (line count), confirming FSI bytes are saved
   ```


### Claude Model

Opus

### Is this a regression?

I don't know

### Last Working Version

_No response_

### Claude Code Version

2.1.146 (Claude Code)

### Platform

Anthropic API

### Operating System

Ubuntu/Debian Linux

### Terminal/Shell

Other

### Additional Information

**Terminal/Shell**

- Other (Konsole / KDE terminal emulator)

**Background context:**

- Legacy BiDi embeddings (U+202A LRE, U+202B RLE, U+202C PDF, U+200E LRM, U+200F RLM) are already stripped by Claude Code's renderer during live streaming -- this is known. Unicode 6.3+ isolates (FSI/RLI/LRI + PDI) are the modern replacement and the only ones that work.

- A per-line FSI/PDI wrap was empirically confirmed as the only working RTL pattern in Claude Code's terminal (Ink renders via ANSI cursor positioning; the terminal emulator applies BiDi reordering per row after writes settle; isolates survive this pipeline, legacy embeddings don't).

- This same approach was successfully implemented natively in [opencode's TUI](https://github.com/sst/opencode) via its opentui render layer, where BiDi isolates are injected at the renderer level rather than relying on model output.

**Affected scripts:** Arabic, Hebrew, Urdu, Persian/Farsi, Pashto, Syriac, Thaana, NKo, Samaritan, Mandaic, and any text using Arabic/Hebrew presentation forms.

**Suggestion:** Preserve U+2066 (LRI), U+2067 (RLI), U+2068 (FSI), and U+2069 (PDI) through the history replay rendering path. These four characters are the complete Unicode BiDi isolate set and should be treated as valid text content, not stripped.

Longer-term, a built-in `bidi` setting (auto/always/never) that injects isolates at the render layer would solve both live and resume cases without requiring model cooperation or extra tokens.

# Comments on anthropics/claude-code#61201
Total: 0 comments

No comments on this issue.

---

### Issue #48246 — Feature request: Show agent/subagent task progress in terminal UI (parity with third-party tools)

State: OPEN | #48246
Labels: enhancement, area:tui, area:agents


---

## Summary

Love the new desktop UI — but it currently shows significantly less information about agent and subagent activity than third-party wrappers do.

## Current behavior

When a subagent is running, the first-party Claude UI only shows:

```
Running agent  CLAUDE.md compliance review  >

  *  2m 34s · ↓ 2.2k tokens
```

<img width="1000" height="115" alt="Image" src="https://github.com/user-attachments/assets/05d20760-90c4-490c-8e50-1de6492e6f5b" />

That's it — no task list, no subagent breakdown, no status per agent.

## Expected / desired behavior

Third-party tools (e.g. Vibe Island) surface much richer information in their UI:

<img width="844" height="651" alt="Image" src="https://github.com/user-attachments/assets/9521000f-412b-4d64-80a8-a54ed02b62e1" />

- Named tasks with completion status (done / in progress / open)
- A list of subagents with their descriptions, status, and elapsed time
- The current tool/command being run

This creates a situation where users get *better observability into Claude's own work* from a third-party app than from the official one.

## Suggested improvement

The terminal UI should surface at minimum:
- Task list with status indicators (as populated via `TaskCreate`/`TaskUpdate`)
- Active subagent names + status
- Current tool invocation (already partially shown via the streaming output, but not in a persistent way during agent runs)

---

This is UX feedback, not a bug. The data is clearly available (tasks and subagents are tracked) — it just isn't surfaced in the terminal UI. Closing this visibility gap would make long agentic runs much easier to monitor from the first-party CLI.

# Comments on anthropics/claude-code#48246
Total: 1 comments

--- Comment 1 ---
Author: RaimundOstrowski
Date: 2026-05-20T09:21:07Z

Practical use-case for TUI subagent support (both in desktop and CLI):

I run implementation agents in batch which spawns N parallel workers through a defined workflow, each in their own worktree. Monitoring them requires tail -F'ing one log file per worker and streaming a filtered set to the append-only message log. An in-chat in-place status bar would collapse that into a single live view.

---

### Issue #42873 — [DOCS] `/claude-api` skill docs omit agent design guidance topics

State: OPEN | #42873
Labels: documentation, area:skills, area:docs


---

### Documentation Type

Missing documentation (feature not documented)

### Documentation Location


https://code.claude.com/docs/en/skills

### Section/Topic


`Bundled skills` table (`/claude-api` entry)

### Current Documentation


The `code.claude.com` skills docs currently describe `/claude-api` as:

> Load Claude API reference material for your project's language (Python, TypeScript, Java, Go, Ruby, C#, PHP, or cURL) and Agent SDK reference for Python and TypeScript. Covers tool use, streaming, batches, structured outputs, and common pitfalls. Also activates automatically when your code imports `anthropic`, `@anthropic-ai/sdk`, or `claude_agent_sdk`

The dedicated Claude API skill page currently says:

> The skill uses [progressive disclosure](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) to keep context efficient: Claude loads only the documentation relevant to your project's language and the specific task at hand (tool use, streaming, batches, and so on), rather than loading everything at once.
>
> - **Tool use guidance:** Language-specific examples and conceptual foundations for function calling
> - **Streaming patterns:** Implementation details for building chat UIs and handling incremental display
> - **Batch processing:** Offline batch processing at 50% cost
> - **Agent SDK reference:** Installation, built-in tools, permissions, MCP integration, and common patterns (Python and TypeScript)
> - **Common pitfalls:** Detailed guidance on avoiding frequent mistakes when integrating with the API

### What's Wrong or Missing?


Changelog v2.1.91 says:

> Improved `/claude-api` skill guidance for agent design patterns including tool surface decisions, context management, and caching strategy

Current docs do not mention those newly improved guidance areas anywhere in the `/claude-api` descriptions on `code.claude.com` or on the dedicated platform skill page.

Users can currently discover that `/claude-api` helps with tool use, streaming, batches, structured outputs, and common pitfalls, but they are not told that the skill now also covers:

- tool surface decisions when designing agent tools
- context management guidance for long-running agents
- caching strategy guidance

That makes the new v2.1.91 skill improvements hard to discover for users who rely on the docs to decide when to invoke `/claude-api`.

### Suggested Improvement


Update the `/claude-api` descriptions on the Claude Code skills pages and on the dedicated platform skill page to explicitly mention the new agent-design guidance areas added in v2.1.91.

A concise fix would be to add a sentence or bullet such as:

> Also covers agent design patterns such as choosing an effective tool surface, managing context for long-running agents, and planning prompt-caching/caching strategies.

It would also help to add cross-references to the existing platform docs that cover those topics in depth.

### Impact

Medium - Makes feature difficult to understand

### Additional Context


**Affected Pages:**

| Page | Line(s) | Context |
|------|---------|---------|
| https://code.claude.com/docs/en/skills | 28 | Bundled `/claude-api` description omits the new agent-design guidance topics |
| https://code.claude.com/docs/en/slash-commands | 28 | Mirrored bundled-skill entry has the same incomplete description |
| https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill | 11-23 | Dedicated skill page lists current coverage but does not mention tool surface decisions, context management, or caching strategy |

**Total scope:** 3 pages affected

**Relevant existing docs to cross-reference:**

| Page | Context |
|------|---------|
| https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools | Existing tool-design guidance for tool surface decisions |
| https://platform.claude.com/docs/en/build-with-claude/context-windows | Existing context-management guidance |
| https://platform.claude.com/docs/en/build-with-claude/prompt-caching | Existing caching-strategy guidance |

**Source:** Changelog v2.1.91

**Changelog entry:** Improved `/claude-api` skill guidance for agent design patterns including tool surface decisions, context management, and caching strategy

# Comments on anthropics/claude-code#42873
Total: 2 comments

--- Comment 1 ---
Author: coygeek
Date: 2026-04-28T21:14:04Z

Still relevant as of 2026-04-28. Checked latest docs at https://code.claude.com/docs/en/skills, https://code.claude.com/docs/en/slash-commands, and https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill — the three agent design guidance topics (tool surface decisions, context management guidance, caching strategy guidance) remain absent from all affected pages.

--- Comment 2 ---
Author: coygeek
Date: 2026-05-18T23:46:25Z

Still relevant as of 2026-05-18. This documentation gap has not been addressed in the docs yet.

---

### Issue #63025 — [BUG] SSH Remote: `projects` field in remote ~/.claude.json becomes null after desktop restart — jsonl files intact, UI shows 'No messages yet' for every session

State: OPEN | #63025
Labels: bug, platform:windows, data-loss, area:desktop


---

### Summary

After restarting the Claude Code desktop client while connected to a remote host via SSH Remote, the sidebar shows "No messages yet" for every conversation. Investigation on the remote shows the top-level `projects` field of `~/.claude.json` has been nulled out, while the `.jsonl` transcript files in `~/.claude/projects/<project>/` are intact and continue to be appended to in real time.

This appears related to #54187, #53717, and #34324 but with a stricter form of the corruption — the `projects` map is entirely missing instead of just having empty `sessions[]` arrays per project.

### Environment

- **Client**: Claude Code Desktop on Windows 10/11
- **Connection**: SSH Remote via OpenSSH 9.6 (Windows native OpenSSH)
- **Server**: Ubuntu 24.04.4 LTS (Noble Numbat), claude-code installed under `/root`
- **Working dir on remote**: `/root`

### State of remote `~/.claude.json` after bug triggers

```python
>>> import json
>>> d = json.load(open('/root/.claude.json'))
>>> list(d.keys())
['cachedGrowthBookFeatures', 'unpinOpus47LaunchEffort', 'firstStartTime',
 'opusProMigrationComplete', 'sonnet1m45MigrationComplete', 'seenNotifications',
 'migrationVersion', 'userID', 'cachedExperimentFeatures',
 'cachedExtraUsageDisabledReason', 'skillUsage']
>>> d.get('projects')
None
>>> type(d.get('projects'))
<class 'NoneType'>
```

No `projects` map at all — not `{}`, not per-project entries with empty `sessions[]`.

### Data side is intact

```bash
$ ls ~/.claude/projects/-root/*.jsonl | wc -l
14
$ du -sh ~/.claude/projects/-root/
17M
$ for f in ~/.claude/projects/-root/*.jsonl; do
    python3 -c "import json
bad = 0
for l in open('$f'):
    try: json.loads(l)
    except: bad += 1
print('$f', bad)"
done
# every file: 0 malformed
```

The currently-active session's `.jsonl` continues being appended to within seconds of sending a message from the (broken) UI, so the CLI/backend write path is fine. Only the index is broken.

### UI symptom

- Sidebar lists conversations as normal.
- Clicking any conversation shows "No messages yet" — including the one I am actively sending messages to.
- After restarting Claude Code on the desktop, no messages render at all.

### Repro context

- Long-running conversation (~1000 lines, ~2 MB in the .jsonl).
- Closed the desktop window while SSH session was active.
- Reopened — broken state since.

### Difference from #54187

#54187 (macOS local) reports `sessions[]` arrays per project go empty. In this SSH-remote case, the `projects` map is *entirely missing* (null). Possibly the same root cause hitting a different code path that writes through `~/.claude.json`, or a separate bug masked as the same UI symptom.

### What would help

Happy to share:
- Sanitized `~/.claude.json` (after stripping `userID` and tokens).
- Diagnostics on the active jsonl that keeps being appended to despite the broken index.
- Try a specific repro on request.

### Workaround attempted

Reconstructing the `projects` map manually from filesystem scan was attempted but I want maintainer guidance on the exact expected schema (`sessions` array of `{id, ...}`? other required keys per project?) before writing to my own `~/.claude.json`. Will report back if I find a safe regeneration script.

# Comments on anthropics/claude-code#63025
Total: 1 comments

--- Comment 1 ---
Author: Fasted93
Date: 2026-05-28T07:28:11Z

### Same UI symptom (Linux remote, Windows client, v2.1.149) — but `projects` field is **intact** here. Suggests rehydration bug is independent of the index corruption.

Hit the same UI symptom in a different environment, but the root-cause hypothesis from the OP (nulled `projects` in remote `~/.claude.json`) does **not** apply in my case — the field is a healthy dict on both ends. So either there are two bugs producing the same UI symptom, or the null-`projects` corruption is downstream of a more general rehydration failure in the SSH Remote code path.

#### Environment

| Side | Detail |
|---|---|
| Local app | Claude Code Desktop **1.9255.2** (MSIX, `WindowsApps\Claude_1.9255.2.0_x64`) |
| Local CLI sidecar | `claude.exe` **2.1.149.0** under `%APPDATA%\Claude\claude-code\2.1.149\` |
| OS local | Windows 11 Home 10.0.26200 |
| SSH client | OpenSSH_for_Windows_9.5p2, LibreSSL 3.8.2 |
| Remote OS | Ubuntu 24.04.4 LTS (Noble), Linux 6.8.0-90 x86_64 |
| Remote CLI | `/root/.claude/remote/ccd-cli/2.1.149` |
| Remote cwd | `/root` |

#### UI symptom (same as OP)

After restarting Claude Code Desktop while connected to the remote project via SSH Remote, every conversation in the sidebar shows "No messages yet". Clicking any session yields the empty state. **However:** sending a new message *does* preserve context — Claude responds as if it had read the full prior transcript, even though the UI didn't render any of it. So the CLI side rehydrates fine, the UI side does not.

#### `~/.claude.json` is intact on both ends (key difference from OP)

Remote (`/root/.claude.json`):

\`\`\`python
>>> list(d.keys())
['cachedGrowthBookFeatures', 'unpinOpus47LaunchEffort', 'firstStartTime',
 'opusProMigrationComplete', 'sonnet1m45MigrationComplete', 'seenNotifications',
 'migrationVersion', 'userID', 'cachedExperimentFeatures',
 'cachedExtraUsageDisabledReason', 'skillUsage', 'projects']
>>> type(d['projects'])
<class 'dict'>
>>> list(d['projects'].keys())
['/root']
>>> list(d['projects']['/root'].keys())
['allowedTools', 'mcpContextUris', 'mcpServers', 'enabledMcpjsonServers',
 'disabledMcpjsonServers', 'hasTrustDialogAccepted',
 'projectOnboardingSeenCount', ...]
\`\`\`

Local (`C:\Users\<user>\.claude.json`): `projects` present, **402 entries**, including the remote SSH project key `ssh:root@<vps-ip>:~`.

So in my case the index in **both** files is valid — yet the UI still fails to render.

#### Server-side data is healthy

\`\`\`
$ ls ~/.claude/projects/-root/*.jsonl | wc -l
12
$ du -sh ~/.claude/projects/-root/
18M
\`\`\`

The active session's `.jsonl` grew from ~115 KB to ~474 KB during the diagnostic session in real time, confirming the CLI write path is fine. No malformed lines.

#### Remote-server log on each Desktop restart shows a clean reconnect cycle

`/root/.claude/remote/run/<id>/remote-server.log`:

\`\`\`
[Server] Connection closed: @
[Server] New connection from: @
[shellenv] Extracted shell PATH (117 chars)
[process.Manager] Process <uuid> started, PID=<pid>, command=/root/.claude/remote/ccd-cli/2.1.149
[process.Manager] Starting stdout streaming for process <uuid>
[process.Manager] Starting stderr streaming for process <uuid>
\`\`\`

A fresh CLI process is spawned per reconnect, but there is no event indicating the server replays the historical `.jsonl` to the desktop client — only stdout/stderr streaming of the newly-spawned process. Matches the observed UI behavior.

#### Local `main.log`: app starts but no SSH-rehydrate event

Tail of `%APPDATA%\Claude\logs\main.log` immediately after restart:

\`\`\`
2026-05-28 09:25:19 [info] Starting app { appVersion: '1.9255.2', isPackaged: true, platform: 'win32', arch: 'x64', nodeVersion: '24.15.0' }
2026-05-28 09:25:19 [info] [CCD] Initialized with version 2.1.149
2026-05-28 09:25:19 [info] [growthbook] next refresh in 60 min
2026-05-28 09:25:19 [info] [IdleManager:session] Initialized with 900s timeout
2026-05-28 09:25:19 [info] [IdleManager:preview] Initialized with 1800s timeout
2026-05-28 09:25:19 [info] Not main instance, returning early from app ready
\`\`\`

No `SSH Remote`-specific rehydrate log line is visible at info level around the restart. Happy to capture at debug level if there's an env var to enable it.

#### Suggested narrowing

1. The "no messages yet" UI state is reproducible with the `projects` map **valid on both ends** — so the fix can't be only "defend against null `projects`".
2. Worth checking whether the renderer in the SSH Remote path tries to fetch the `.jsonl` via RPC and silently drops the response, vs. relying on `projects[].sessions` (which #54187 reports also goes empty).
3. Re-clicking the sidebar entry does **not** restore the messages here; only sending a new message brings the CLI to life — and even then, prior turns are not retroactively rendered. They stay missing visually but Claude has them in context.

Can attach full `remote-server.log`, sanitized `~/.claude.json` from both ends, and per-file jsonl line counts on request.

---

### Issue #45482 — [DOCS] Agent SDK transcript viewer docs missing final token usage semantics

State: OPEN | #45482
Labels: documentation, area:agent-sdk


---

### Documentation Type

Missing documentation (feature not documented)

### Documentation Location


https://code.claude.com/docs/en/agent-sdk/sessions

### Section/Topic


`getSessionMessages()` / `get_session_messages()` transcript viewer guidance and transcript token-usage semantics

### Current Documentation


The sessions guide currently says:

> Both SDKs expose functions for enumerating sessions on disk and reading their messages: `listSessions()` and `getSessionMessages()` in TypeScript, `list_sessions()` and `get_session_messages()` in Python. Use them to build custom session pickers, cleanup logic, or transcript viewers.

The TypeScript reference currently says:

> `message` | `unknown` | Raw message payload from the transcript

The Python reference currently says:

> `message` | `Any` | Raw message content

The cost-tracking guide currently says:

> Each assistant message contains a nested `BetaMessage` (accessed via `message.message`) with an `id` and `usage` object with token counts.

> When the `query()` call completes, the SDK emits a result message with `total_cost_usd` and cumulative `usage`.

The docs describe transcript access and live per-step usage separately, but they do not explain what token-usage values transcript-derived per-block entries contain.

### What's Wrong or Missing?


Changelog v2.1.97 introduced a transcript-facing behavior change:

> Improved transcript accuracy: per-block entries now carry the final token usage instead of the streaming placeholder

That matters for developers who read `~/.claude/projects/<project>/<session>.jsonl` directly or use `getSessionMessages()` / `get_session_messages()` to build transcript viewers or usage analytics.

What's missing is a clear explanation of transcript token-usage semantics:

### A. No transcript-specific usage guidance
The docs say session messages come from the transcript, but they do not explain whether transcript-derived assistant/per-block entries include token usage, or how those values should be interpreted.

### B. No note about the v2.1.97 accuracy change
There is no documentation stating that per-block transcript entries now carry the final token usage instead of a streaming placeholder.

### C. No guidance on per-block usage vs final totals
The cost-tracking guide explains per-step usage and the authoritative final `ResultMessage.usage`, but it does not connect that guidance to transcript readers who need to know when transcript usage is suitable for display versus when they should rely on the final result totals.

### Suggested Improvement


Add a short “Transcript usage semantics” note to the sessions guide, with cross-links from the TypeScript and Python API references.

Suggested content:

1. State that session transcripts are stored in `~/.claude/projects/<project>/<session>.jsonl` and can be read directly or via `getSessionMessages()` / `get_session_messages()`.
2. Document that transcript-derived assistant/per-block entries can include token-usage data.
3. Note that as of v2.1.97, those per-block entries carry the **final** token usage rather than the earlier streaming placeholder.
4. Clarify that transcript viewers can display those finalized per-block values, but billing/whole-query totals should still use the final result message (`usage`, `total_cost_usd`, and per-model breakdowns).
5. Cross-reference the existing cost-tracking guidance about deduplicating assistant messages that share the same message ID during parallel tool turns.

### Impact

Medium - Makes feature difficult to understand

### Additional Context


**Affected Pages:**

| Page | Context |
|------|---------|
| https://code.claude.com/docs/en/agent-sdk/sessions | Tells users to use session-message APIs to build transcript viewers |
| https://code.claude.com/docs/en/agent-sdk/typescript | `getSessionMessages()` return type and `SDKAssistantMessage.message.usage` context |
| https://code.claude.com/docs/en/agent-sdk/python | `get_session_messages()` return type and `AssistantMessage.usage` context |
| https://code.claude.com/docs/en/agent-sdk/cost-tracking | Explains per-step usage and authoritative final totals, but only for streamed query output |
| https://code.claude.com/docs/en/claude-directory | Documents where transcript JSONL files are stored |

**Total scope:** 5 pages affected

**Source:** Changelog v2.1.97

**Exact changelog entry:** “Improved transcript accuracy: per-block entries now carry the final token usage instead of the streaming placeholder”

# Comments on anthropics/claude-code#45482
Total: 2 comments

--- Comment 1 ---
Author: coygeek
Date: 2026-05-11T04:36:34Z

Just checked the current docs again. This issue is not fully resolved yet.

--- Comment 2 ---
Author: coygeek
Date: 2026-05-28T22:37:56Z

Still relevant as of 2026-05-28. I checked the current docs and this documentation gap still appears unresolved.

---

### Issue #42045 — [Bug] Desktop freezes/lag during Claude Code output on high refresh rate + high resolution displays

State: OPEN | #42045
Labels: stale


---



### What's Wrong?

When Claude Code is outputting text (especially during tool execution or streaming responses), the entire desktop becomes extremely laggy/unresponsive. This is especially noticeable on high refresh rate displays.

### Environment

- **Version:** 2.1.77
- **OS:** Windows 11 Pro (Build 26200)
- **Install:** winget (Anthropic.ClaudeCode)
- **Display:** 
  - Primary: Intel Arc A770 GPU, 3840x2160 (4K) @ 165Hz
  - Secondary: Intel UHD Graphics 770, 1920x1080 @ 165Hz
- **Terminal:** Windows Terminal (latest)
- **Shell:** PowerShell 7 / cmd.exe

### Observed Behavior

During Claude Code output (tool execution, streaming responses), the entire desktop experiences severe lag:
- Mouse cursor stutters
- Other applications become unresponsive
- Keyboard input is delayed
- Audio/video playback may stutter

The issue is much more pronounced on the 4K@165Hz display.

### Expected Behavior

Claude Code output should not affect overall system responsiveness. The desktop should remain fluid even during heavy terminal output.

### Steps to Reproduce

1. Start Claude Code session
2. Execute any command that produces significant output (e.g., running a script, reading multiple files, tool execution with verbose output)
3. Observe desktop responsiveness during output

### Additional Information

The issue seems related to how Claude Code handles terminal rendering - it appears to be a full-screen redraw architecture that causes blocking and high CPU/GPU usage during output.

# Comments on anthropics/claude-code#42045
Total: 4 comments

--- Comment 1 ---
Author: YoussofKhawaja
Date: 2026-04-04T09:58:44Z

I'm experiencing the same issue, the desktop lags, and the display flickers.

--- Comment 2 ---
Author: avi12
Date: 2026-04-08T06:42:29Z

Huh, I thought it's an issue with my hardware even though it's powerful, I'm glad I'm not the only one to experience this

--- Comment 3 ---
Author: Evopower
Date: 2026-04-14T10:57:46Z

Still reproducing on v2.1.77 and later versions.

Hardware: Intel Arc A770 GPU, 4K@165Hz primary display + 1080p@165Hz secondary, Windows 11 Pro.

The entire desktop freezes during streaming output — not just the terminal. Mouse cursor stutters, other apps become unresponsive, audio/video playback stutters. Issue is significantly worse on the 4K@165Hz display.

This appears to be a rendering architecture issue where terminal output causes system-wide blocking, likely due to full-screen redraw behavior.

Would appreciate an official response or triage. Happy to provide any additional diagnostics.

--- Comment 4 ---
Author: Mezmeer1
Date: 2026-04-26T23:45:58Z

I've been having the same issue. I upgraded my network card and it's gotten better. I think it might have something to do with the packet bursts and how IRQs are handled?  IDK maybe I'm wrong and it hasn't gotten better.  It definitely seems like it's gotten better though, the desktop lagging has gotten smoother whereas before the upgrade I would  have everything freeze for half a second, go, freeze, go. Now it's more like stuttering.
CPU:12th Gen Intel(R) Core(TM) i7-12700
GPU:NVIDIA GeForce RTX 3080
HDD: WDC WD10EZEX-60WN4A2 &  NVMe WD WD_BLACK Gen4 SDCPNRY-1T00-1106
Network: Intel(R) Wi-Fi 7 BE200 320MHz
Motherboard: HP 894A
OS: Microsoft Windows 11 Pro 10.0.26200

---

### Issue #57960 — [BUG] Claude Desktop on Windows: PowerShell tool call permission prompt delayed ~2m35s before appearing

State: OPEN | #57960
Labels: bug, platform:windows, area:permissions, area:desktop


---



### What's Wrong?

**Environment:**
- Claude Desktop version: `1.6608.2 (ebf1a1)` (2026-05-08)
- OS: Windows 11 (10.0.26200)
- Shell: Windows PowerShell 5.1.26100.8246 (`powershell.exe`)

**Symptom:**
When Claude attempts a PowerShell tool call, the tool-call status indicator shows "in progress" but **no permission prompt is rendered in the UI**. After approximately **2 minutes 35 seconds** with no user interaction, the prompt finally appears and behaves normally.

This does **not** happen for other tool calls (Read, Edit, Grep, etc.) — only PowerShell. The UI is not frozen during the wait; other interactions work. The delay is consistent.

**Distinct from related issues:**
- Not [[#9383](https://github.com/anthropics/claude-code/issues/9383)](https://github.com/anthropics/claude-code/issues/9383) — that bug rejects the operation immediately; here the operation eventually succeeds after the delayed prompt.

### Related Issues

When executing PowerShell command from Claude Code CLI, the issue is the same as [[#45099](https://github.com/anthropics/claude-code/issues/45099)](https://github.com/anthropics/claude-code/issues/45099) — in that bug the prompt renders then freezes; here the prompt simply does not render for ~2.5 minutes.

### What Should Happen?

Permission prompt should display in few seconds.

### Error Messages/Logs

```shell
2026-05-11T07:09:52.713Z [DEBUG] Tool search disabled for model 'claude-haiku-4-5-20251001': model does not support tool_reference blocks. This feature is only available on Claude Sonnet 4+, Opus 4+, and newer models.
2026-05-11T07:09:52.717Z [DEBUG] attribution header x-anthropic-billing-header: cc_version=2.1.138.66f; cc_entrypoint=cli; cch=00000;
2026-05-11T07:09:52.719Z [DEBUG] [API:request] Creating client, ANTHROPIC_CUSTOM_HEADERS present: false, has Authorization header: false
2026-05-11T07:09:52.719Z [DEBUG] [API:auth] OAuth token check starting
2026-05-11T07:09:52.720Z [DEBUG] Total plugin output styles loaded: 0
2026-05-11T07:09:52.722Z [DEBUG] [API:auth] OAuth token check complete
2026-05-11T07:09:52.725Z [DEBUG] [API REQUEST] /v1/messages x-client-request-id=b0ae262b-c473-42f9-9515-605a23a2faa1 source=generate_session_title
2026-05-11T07:09:52.729Z [DEBUG] autocompact: tokens=[REDACTED] level=ok effectiveWindow=180000
2026-05-11T07:09:52.766Z [DEBUG] Dynamic tool loading: 0/25 deferred tools included
2026-05-11T07:09:52.767Z [DEBUG] attribution header x-anthropic-billing-header: cc_version=2.1.138.66f; cc_entrypoint=cli; cch=00000;
2026-05-11T07:09:52.767Z [DEBUG] [API:request] Creating client, ANTHROPIC_CUSTOM_HEADERS present: false, has Authorization header: false
2026-05-11T07:09:52.768Z [DEBUG] [API:auth] OAuth token check starting
2026-05-11T07:09:52.778Z [DEBUG] [API:auth] OAuth token check complete
2026-05-11T07:09:52.782Z [DEBUG] [API REQUEST] /v1/messages x-client-request-id=c06300ee-b128-4666-ba4c-5663df5e839d source=repl_main_thread
2026-05-11T07:09:53.640Z [DEBUG] Stream started - received first chunk
2026-05-11T07:09:57.774Z [DEBUG] Stream started - received first chunk
2026-05-11T07:12:28.600Z [WARN] Streaming stall detected: 150.0s gap between events (stall #1)
2026-05-11T07:12:28.604Z [WARN] Streaming completed with 1 stall(s), total stall time: 150.0s
2026-05-11T07:12:28.653Z [DEBUG] High write ratio: blit=0, write=1438 (100.0% writes), screen=24x120
2026-05-11T07:12:29.283Z [INFO] [Stall] tool_dispatch_start tool=PowerShell toolUseId=toolu_0152TeZkYMSNe5nPenrunWsj permissionDecisionMs=150717
2026-05-11T07:12:29.839Z [INFO] [Stall] tool_dispatch_end tool=PowerShell toolUseId=toolu_0152TeZkYMSNe5nPenrunWsj outcome=ok durationMs=556
2026-05-11T07:12:29.846Z [DEBUG] LSP Diagnostics: getLSPDiagnosticAttachments called
2026-05-11T07:12:29.847Z [DEBUG] LSP Diagnostics: Checking registry - 0 pending
2026-05-11T07:12:29.847Z [DEBUG] Hooks: Found 0 total hooks in registry
2026-05-11T07:12:29.847Z [DEBUG] Hooks: checkForNewResponses returning 0 responses
2026-05-11T07:12:29.849Z [DEBUG] autocompact: tokens=[REDACTED] level=ok effectiveWindow
```

**suspicious log:**
```shell
2026-05-11T07:12:28.600Z [WARN] Streaming stall detected: 150.0s gap between events (stall #1)
2026-05-11T07:12:28.604Z [WARN] Streaming completed with 1 stall(s), total stall time: 150.0s
```

### Steps to Reproduce

1. Ask Claude to run any PowerShell command, e.g. `"hello"`.
2. Observe tool-call spinner.
3. No prompt appears for ~2m35s.
4. Prompt eventually appears; approving runs the command normally.

### Claude Model

Opus

### Is this a regression?

I don't know

### Last Working Version

_No response_

### Claude Code Version

2.1.138

### Platform

Anthropic API

### Operating System

Windows

### Terminal/Shell

PowerShell/VS Code

### Additional Information

_No response_

# Comments on anthropics/claude-code#57960
Total: 2 comments

--- Comment 1 ---
Author: IvanaGyro
Date: 2026-05-11T07:24:25Z

It seems that #55681 is the same issue.

--- Comment 2 ---
Author: IvanaGyro
Date: 2026-05-22T04:12:56Z

Is there any progress?

---

### Issue #47248 — [BUG] Memory leak in short, lightweight sessions (v2.1.104, macOS ARM64, 32GB)

State: OPEN | #47248
Labels: bug, duplicate, has repro, platform:macos, perf:memory, stale


---



### What's Wrong?

Claude Code consumes all available memory on a 32GB Mac within minutes of lightweight usage, making the system completely unresponsive and requiring force-kill via Activity Monitor. This has been happening consistently **across the last ~6 releases** regardless of project or workload.

**Key detail:** This is NOT caused by long sessions or large context. The specific session that prompted this report was **~5 minutes old** with **minimal context** — a plan-mode approval followed by a handful of small file edits. Claude crashed during the plan approval step itself.

### Environment

- **Claude Code:** 2.1.104
- **Platform:** macOS Darwin 25.3.0 (Apple Silicon ARM64)
- **RAM:** 32 GB
- **Runtime:** Bun-based binary (not affected by NVM/system Node.js)

### Memory snapshot during the session

Three Claude processes running simultaneously:
```
alex     465 MB   claude
alex     464 MB   claude
alex     384 MB   claude
```
**Total: ~1.3 GB** after just a few minutes of a lightweight plan-mode + edit session. System became unresponsive shortly after.

### Session activity at time of crash

1. User entered plan mode
2. Claude generated a small plan (5 file edits, all under 10 lines each)
3. User approved the plan
4. Claude began executing edits
5. System became unresponsive — had to force-kill via Activity Monitor

No subagents were spawned. No large files were read. No web searches. Context window was minimal.

### Relation to existing issues

This appears to be the same root cause as:
- #34967 — ArrayBuffers grow to 6.3GB in ~5 minutes (v2.1.72)
- #33589 — BytesInternalReadableStreamSource ArrayBuffer accumulation (3.3GB in 59s)
- #39531 — 61GB/hour growth rate (v2.1.76)

The ArrayBuffer/streaming buffer leak identified in those issues is **still present in v2.1.104**. Given the severity (renders 32GB machines unusable within minutes), this warrants priority attention.

### What Should Happen?

A 5-minute session doing small file edits should not consume more than a few hundred MB total across all processes.

### Workaround attempts

- `NODE_OPTIONS=--max-old-space-size` does NOT help — the leak is in `external`/`arrayBuffers` outside V8's managed heap
- Changing Node.js version via NVM does NOT help — Claude Code bundles its own Bun runtime
- `/compact` and `/clear` are not viable workarounds when the leak occurs within the first few minutes of a fresh session
- The only current workaround is force-killing Claude processes via Activity Monitor when the system becomes sluggish

### Suggested investigation

The leak appears to be in streaming response buffer handling within the Bun runtime. The pattern from #34967 shows V8 heap at 65MB while `external`/`arrayBuffers` balloon to multi-GB — these buffers are allocated for streaming but never freed.

# Comments on anthropics/claude-code#47248
Total: 2 comments

--- Comment 1 ---
Author: narangproduct-cmyk
Date: 2026-04-13T13:07:11Z

## Reproduction Data: Kernel Panic from Claude Code Memory Leak (macOS ARM64, 32GB)

### Environment
- **Hardware**: MacBook Pro M5 (Mac17,2), Apple M5 chip, 32GB RAM
- **OS**: macOS 26.3.1 (25D2128) / Darwin 25.3.0
- **Claude Code**: 2.1.81
- **Shell**: bash inside tmux 3.6a, Terminal.app
- **Battery cycle**: 11 (near-new hardware)

### Symptoms
- **4 kernel panics in 48 hours** (April 12-13, 2026)
- 3x WindowServer userspace watchdog timeout (120s unresponsive)
- 1x Sleep transition timeout (AppleH16ANEInterface, 35s)

### Root Cause Evidence
From Jetsam event (`JetsamEvent-2026-04-13-182232.ips`):

| Process | PID | rpages | dirty internal pages | Equivalent |
|---------|-----|--------|---------------------|------------|
| **claude** | 30253 | 11,372,403 | 11,244,480 | **~172GB** |
| claude | 6526 | 39,190 | 11,125 | ~599MB (normal) |
| claude | 35033 | 19,046 | 3,620 | ~291MB (normal) |
| claude | 35728 | 17,585 | 3,574 | ~269MB (normal) |

A single Claude Code process (PID 30253) accumulated **11.2 million dirty internal pages (~172GB equivalent)** on a 32GB system. The memory compressor was processing 16.4GB. System-wide free memory dropped to **80MB**, triggering Jetsam.

### Cascade
1. Claude memory leak -> compressor overload -> free memory 80MB
2. WindowServer scheduling delayed -> 120s watchdog checkin failure -> kernel panic
3. OR: Sleep transition with memory exhaustion -> ANE driver timeout -> kernel panic

### Reproduction Conditions
- Multiple Claude Code instances in tmux (3-4 simultaneous)
- Long-running sessions (hours)
- Heavy tool usage (Bash, Read, Write, Agent subprocesses)
- Terminal.app as terminal emulator (may exacerbate via fd_set overflow at 100% CPU)

### Diagnostic Files Available
- `panic-full-2026-04-13-210135.0002.panic` (ANE sleep transition)
- `panic-full-2026-04-13-091044.0002.panic` (WindowServer watchdog)
- `JetsamEvent-2026-04-13-182232.ips` (memory pressure snapshot)
- `Terminal_2026-04-13-185943_yunaui-MacBookPro.cpu_resource.diag`

### Workaround Applied
- Limited concurrent Claude instances to max 2
- Installed memory monitoring LaunchAgent (5-min interval, alert at 30% free)
- Disabled display sleep (prevents sleep transition panic trigger)
- Migrated from Terminal.app to Ghostty (kqueue-based, no fd_set limitation)

--- Comment 2 ---
Author: hirscr
Date: 2026-05-14T01:06:52Z

Just adding to this frustrating bug. PLEASE write a rust version of Claude Code.
====================

Adding a recent data capture with two observations I don't see in this thread yet.

  Environment

  - v2.1.140 → 2.1.141 (self-update happened mid-capture; see below)
  - macOS 26.0.1 (25A362), Apple Silicon M3, 18 GB RAM
  - Reproduces in both iTerm2 and Apple Terminal.app — host terminal is not a variable. Codex CLI (Rust) running in the
  same shells alongside claude never exceeds 61 MB.

  Observation 1: cohort scale (corroborates the existing thread)

  With 6–9 concurrent claude sessions, total descendant phys_footprint reaches 60–110 GB before the kernel intervenes. Six
   JetsamEvent files (/Library/Logs/DiagnosticReports/JetsamEvent-*.ips) on 2026-05-12 record the kernel killing process
  cohorts named "2.1.139" / "2.1.140" (the argv[0] Claude Code sets). On respawn, fresh claude processes grow 0 → 2 GB
  phys_footprint in ~2.5 minutes of initial startup with no user input. In one cohort, 8 of 9 sessions grew at 600–800
  MB/min in lockstep — including a --model haiku session — ruling out per-model causes.

  Observation 2: the leak is broader than just ArrayBuffers

  The ArrayBuffer hypothesis from #34967 / #33589 is consistent with what we see, but vmmap --summary on a 6.4 GB runaway
  shows the bulk of the leak in JS VM Gigacage (the full JSC heap arena):

  Writable regions: Total=66.9G written=6.4G(10%) resident=637.7M(1%)
                    swapped_out=5.8G(9%) unallocated=60.4G(90%)

  JS VM Gigacage              9.3G   424M    422M dirty   5.8G swapped   53 regions
  JS VM Gigacage (reserved)  58.7G    0K       0K           0K            3
  JS JIT generated code      64.0M  14.2M
  WebKit Malloc             490.1M  178.7M
  __BUN                     125.8M  104.9M

  5.8 GB of JS VM Gigacage is swapped (compressor-held) — that's the bulk of the phys_footprint blowup. sample shows the
  main thread parked in kevent64 (idle event loop) while the heap is growing — allocation is happening on helper threads
  or in short bursts between samples. The bundled binary is fully stripped; all sample frames render as ???.

  Observation 3 (the new one): 21 GB released spontaneously, no restart

  A single isolated claude process — light interactive use, no large file reads, no multi-thousand-line outputs:

  20:17:19   etime=  2s   rss= 403 MB   footprint=   205 MB   ← spawned
  20:28:49   etime=692s   rss=3.70 GB   footprint= 20.11 GB
  20:29:44   etime=747s   rss=4.95 GB   footprint= 21.34 GB   ← peak
  20:29:49   etime=752s   rss=4.94 GB   footprint=  0.49 GB   ← drop
  20:29:54   etime=757s   rss=4.96 GB   footprint=  0.28 GB
  20:30:04   etime=767s   rss=4.96 GB   footprint=  0.37 GB

  phys_footprint dropped 21.34 GB → 282 MB in two 5-second sampling intervals. RSS stayed flat at ~5 GB. The process did
  not restart — etime kept incrementing. Two minutes later it was still stable at ~288 MB despite active tool use.

  This is the signature of a JSC major garbage collection sweeping the entire old-gen in one event. Which means the 21 GB
  of compressed/swapped pages was unreachable garbage the whole time — collectible, just not being collected.

  Trigger (this is the part I think is actionable): at 20:29 on the same machine, Claude Code's auto-updater downloaded
  2.1.141 to ~/.local/share/claude/versions/ and updated the ~/.local/bin/claude symlink. That happened ~20 seconds before
   the collapse. The most plausible reading: the auto-update path executes a "prepare for restart" cleanup that calls
  Bun.gc(true) or its equivalent, and that major GC frees everything incremental GC has been failing to claim.

  If that's correct, the bug isn't unbounded allocation — it's that incremental GC isn't reclaiming aggressively enough
  during normal operation, and only a rare full GC actually clears the heap.

  What would help

  1. Can someone confirm whether the auto-update path runs a full GC? If yes, exposing that as a slash command (/gc) or
  running it on a timer (every 60s) or on a DISPATCH_SOURCE_TYPE_MEMORYPRESSURE notification would mitigate this in
  production without touching the underlying retention path.
  2. What's keeping old-gen objects reachable until full GC? Streaming-response ArrayBuffers (per #34967 / #33589), parsed
   transcript-store entries from startup, or accumulated tool-result objects are the leading external guesses. A
  --inspect-equivalent heap snapshot from a runaway, taken from inside Anthropic, would localize this in minutes.
  3. A symbolicated debug build of the Bun-bundled binary would let external reporters capture useful sample stacks. The
  current external repro quality is bounded by the fact that every frame is ???.

  Full vmmap / sample / lsof captures and per-5s descendant memory time series across the cohort are available on request.

---

### Issue #50188 — [BUG] Claude Desktop SSH: ccd-cli exits with code 1 immediately — stdin timing issue

State: OPEN | #50188
Labels: bug, platform:macos, area:desktop, stale


---



### What's Wrong?

**What's Wrong?**

Claude Code Desktop SSH sessions immediately crash with "Claude Code process exited with code 1" or "Failed to spawn Claude Code process: Process not running" after connecting to a remote Linux server. The SSH connection itself succeeds — file listing, folder selection, and git worktree creation all work. The crash happens specifically when `ccd-cli` is spawned.

**What Should Happen?**

The SSH Code session should start normally and accept prompts, the same way it works when running `claude` directly on the remote server via terminal.

**Environment**

- Claude Desktop: Latest version (macOS)
- macOS: Sonnet on MacBook Pro
- Remote server: Ubuntu 24.04.4 LTS, Hetzner VPS
- Claude Code on server: 2.1.113 (installed via curl -fsSL https://claude.ai/install.sh | bash)
- ccd-cli deployed by Desktop: 2.1.111 (at ~/.claude/remote/ccd-cli/2.1.111)
- Node.js on server: v20.20.2
- SSH auth: Key-based (RSA 4096), no passphrase, works perfectly from terminal
- No missing shared libraries (ldd shows all resolved)

**Steps to Reproduce**

1. Add SSH connection in Claude Desktop Code tab (root@server-ip, port 22, identity file ~/.ssh/id_rsa)
2. Select a folder on the remote server (e.g. /opt/mstel)
3. Send any prompt (e.g. "hello")
4. Process spawns and immediately exits with code 1

**Diagnostic Details**

From `~/.claude/remote/remote-server.log`:

```
[process.Manager] Process a598420c started, PID=609750, command=/root/.claude/remote/ccd-cli/2.1.111
[process.Manager] Starting stdout streaming for process a598420c
[process.Manager] Starting stderr streaming for process a598420c
[process.Manager] Process a598420c exited with code 1
[process.Manager] WriteStdin: process a598420c not running
```

The process exits immediately before stdin data arrives. This happens consistently across multiple attempts.

**What works fine:**

- `claude -p "hello"` on the server via SSH terminal — works perfectly
- `/root/.claude/remote/ccd-cli/2.1.111 -p "hello"` — works perfectly
- `ldd /root/.claude/remote/ccd-cli/2.1.111` — no missing libraries
- SSH key auth from Mac to server — works perfectly
- `ssh -i ~/.ssh/id_rsa root@server "which claude && claude --version"` — returns correctly

**What fails:**

- `/root/.claude/remote/ccd-cli/2.1.111 --output-format stream-json --input-format stream-json --verbose` returns: `Error: Input must be provided either through stdin or as a prompt argument when using --print`

This suggests the ccd-cli binary exits before receiving stdin from the Desktop RPC, possibly a timing issue where the process expects stdin immediately but the Desktop sends it after the spawn response.

**Workaround**

Using `claude` directly via SSH terminal (Termius) works without issues. Only the Desktop GUI SSH integration is affected.

### What Should Happen?

The SSH Code session should start normally and accept prompts, the same way claude works when run directly on the remote server via SSH terminal.

### Error Messages/Logs

```shell
[process.Manager] Process a598420c started, PID=609750, command=/root/.claude/remote/ccd-cli/2.1.111
[process.Manager] Starting stdout streaming for process a598420c
[process.Manager] Starting stderr streaming for process a598420c
[process.Manager] Process a598420c exited with code 1
[process.Manager] WriteStdin: process a598420c not running
```

### Steps to Reproduce

1. Add SSH connection in Claude Desktop Code tab (root@remote-server, port 22, RSA key auth)
2. Select folder /opt/mstel on the remote server
3. Send any prompt (e.g. "hello")
4. ccd-cli spawns and immediately exits with code 1

### Claude Model

None

### Is this a regression?

I don't know

### Last Working Version

_No response_

### Claude Code Version

2.1.113 (Claude Code)

### Platform

Anthropic API

### Operating System

macOS

### Terminal/Shell

Terminal.app (macOS)

### Additional Information

Remote server: Ubuntu 24.04.4 LTS on Hetzner VPS
ccd-cli binary deployed by Desktop: version 2.1.111 at ~/.claude/remote/ccd-cli/2.1.111
Running ccd-cli manually with -p "hello" works fine.
Running it with --output-format stream-json --input-format stream-json --verbose fails with: "Error: Input must be provided either through stdin or as a prompt argument when using --print"
This suggests a stdin timing issue between Desktop RPC and ccd-cli process.

# Comments on anthropics/claude-code#50188
Total: 4 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-04-17T22:08:32Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/46845
2. https://github.com/anthropics/claude-code/issues/49586
3. https://github.com/anthropics/claude-code/issues/42588

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: MShoaib67
Date: 2026-04-17T22:15:02Z

👎

--- Comment 3 ---
Author: mannmann2
Date: 2026-05-05T15:47:39Z

yup, facing the same problem

--- Comment 4 ---
Author: eegranade
Date: 2026-05-06T02:00:46Z

Same issue .`/root/.claude/remote/ccd-cli/2.1.121 -v` returns 2.1.121 (Claude Code). 

-p hello works great.

---

### Issue #11002 — [FEATURE] Add a --screen-reader mode for better accessibility with NVDA and JAWS

State: OPEN | #11002
Labels: enhancement, platform:windows, area:tui, area:a11y


---



### Problem Statement

Currently, Claude Code’s command-line interface is not fully accessible to screen reader users (e.g., NVDA, JAWS, or Narrator).
When using the CLI, screen readers often mispronounce characters (like | or partial tokens), freeze during streaming output, or stop responding entirely.
The terminal may also hang or become unresponsive when NVDA is active.
As a result, blind and low-vision developers cannot reliably use Claude Code, and often need to restart their screen reader or the terminal multiple times during a session.
This makes the tool frustrating and largely unusable for accessibility-oriented users.

### Proposed Solution

Hi Anthropic team,
I’m an accessibility-focused developer and I’d like to request a small but important feature for Claude Code — a command-line flag similar to --screen-reader recently introduced in Gemini CLI.
💡 What it should do
When --screen-reader is enabled, the CLI should:
• 
Disable spinners, color codes, and animated text updates.
• 
Output plain, linear text without ANSI formatting.
• 
Optionally force simple text mode for streaming output.
• 
Be optimized for screen readers such as NVDA, JAWS, or Narrator.
🧩 Why it’s important
Screen readers often freeze or skip lines when a CLI updates the same line rapidly (e.g., token streaming or progress spinners).
This makes it difficult or impossible for blind developers to follow model responses in real time.
Other tools (like Gemini CLI) have already introduced this flag, which has made a huge difference in accessibility.
✅ Expected outcome
Add an optional flag:
claude --screen-reader
or:
claude --accessibility
When active, Claude Code would output text in a way compatible with screen readers.
❤️ Accessibility impact
This would make Claude Code a truly inclusive development tool, helping many blind or low-vision users participate more easily in AI-assisted coding.
Thanks for considering this improvement — I’d be happy to help test it with NVDA or Jaws for Windows!

### Alternative Solutions

_No response_

### Priority

High - Significant impact on productivity

### Feature Category

CLI commands and flags

### Use Case Example

_No response_

### Additional Context

Several blind and low-vision users have reported accessibility issues when using Claude Code with screen readers such as NVDA or JAWS.
In particular:
• 
The CLI speaks or outputs strange characters, such as the vertical bar (|) or partial Unicode fragments, which causes speech output confusion.
• 
NVDA sometimes freezes or stops responding while Claude Code is running, especially during token streaming or spinner updates.
• 
Users are forced to restart their screen reader multiple times during a single session to regain control.
• 
The terminal window occasionally becomes unresponsive when NVDA is active, especially on Windows.
Because of these problems, many blind developers currently find Claude Code very difficult to use in real-world coding scenarios.
A --screen-reader mode that disables animations and formats plain text output (like Gemini CLI’s implementation) would solve most of these issues.

# Comments on anthropics/claude-code#11002
Total: 30 comments

--- Comment 1 ---
Author: ahicks92
Date: 2025-11-07T17:34:18Z

This isn't platform:windows.  Linux and Mac users will have similar problems for similar reasons.

--- Comment 2 ---
Author: Ambro86
Date: 2025-11-07T18:18:56Z

> This isn't platform:windows. Linux and Mac users will have similar problems for similar reasons.

Thanks Austin, github-actions added this flag, but I hope the developers reading this understand that it's a bigger problem and want to add this feature.

--- Comment 3 ---
Author: LordLundin
Date: 2025-11-24T18:50:21Z

Hi. Another blind user  here and I can  confirm what  @Ambro86 has said.
I can tell you that using the terminal app to run Claude Code seems to have mitigated some of the problems - though I just started trying and could be in my head too.
Would love for the proposed solutions to be implemented since ever since the forced migration to Windows 11 CC has been profoundly annoying to use.
Best regards,
Lundin.

--- Comment 4 ---
Author: github-actions[bot]
Date: 2025-12-25T10:09:49Z

This issue has been inactive for 30 days. If the issue is still occurring, please comment to let us know. Otherwise, this issue will be automatically closed in 30 days for housekeeping purposes.

--- Comment 5 ---
Author: Ambro86
Date: 2025-12-25T12:13:45Z

Thanks for the reminder.
Yes, the issue is still present.
Claude Code is still hard to use with screen readers (NVDA, JAWS, Narrator) because of streaming output, spinners, and frequent line updates, which cause freezes, missed output, or terminal lockups.
This is not limited to Windows — the same behavior occurs on Linux and macOS for the same reasons related to TUI rendering and screen reader interaction.
Other blind users have confirmed this in the thread, and similar tools (e.g. Gemini CLI) have already addressed it with a dedicated --screen-reader / accessibility mode.
The issue is still relevant and affects basic usability for screen reader users.
I’m available to provide more details or help test if needed.

--- Comment 6 ---
Author: ahicks92
Date: 2025-12-26T18:14:37Z

I mean sure I'll comment too, when my terminal locks up at least once a day in ways that are easily prevented I very much remember this issue.  When I go into /config and have to hack around the men u using weird unicode that screen readers don't read using indentation indication and guessing to know what's selected, I remember this issue.  These problems get discussed all the time amongst blind users as a whole.  But all we can do is hope this gets triaged at some point and given enough attention, so yeah this specifically is silent about it.

--- Comment 7 ---
Author: oasis1701
Date: 2025-12-30T13:42:10Z

I hope this gets noticed very soon, this is a major issue with claude code and screen readers and I am dealing with it every day.

--- Comment 8 ---
Author: ahicks92
Date: 2026-01-01T19:55:02Z

Boris Cherny is on X soliciting feedback, I pinged there. Maybe some of you would want to as well.  https://x.com/bcherny/status/2003916001851686951

You can get a slightly more stable experience by going into settings and disabling terminal progress bars (not what you think, it's control codes we can't see not the spinner) and by turning verbose output on (really, I have no clue whatsoever why turning verbose output on on my system seemed to help--maybe it's doing less crazy things with the terminal and just letting the text stream)?  I still have issues--and these days those config menus themselves even have accessibility problems.

To work around the config menu accessibility turn indentationindication on and the less indented line is the selected one.

I'm aware of lots of people complaining about this stuff in my circles but the level of expertise needed to turn this into an actual GH issue for reporting is low so I don't think this is representative. I mean on the one hand number of blind programmers is super low but on the other hand if they understood enough about why it went wrong to report they probably would be.

--- Comment 9 ---
Author: Ambro86
Date: 2026-01-04T05:39:11Z

I don’t like promoting myself, but until Anthropic fixes this issue, I added an accessible command prompt inside my editor (Novapad).
I tested it mainly with Codex, and it removes 100% of NVDA freezes and general system slowdowns. When NVDA freezes, it can crash the whole system.
If this can be useful to some blind developers, you can find it here:
https://github.com/Ambro86/Novapad/

--- Comment 10 ---
Author: techdog420
Date: 2026-01-07T17:55:01Z

Have just started dablling with Claude code, and am running into the same issue as stated. This is making the tool difficult to use by blind developers, so please show this issue some love! I looked into the novapad suggestion, but the program is crashing immediately after entering the terminal window. I'll try to dig into this when I get some more free time. 

--- Comment 11 ---
Author: Ambro86
Date: 2026-01-10T11:23:30Z

@techdog420 The terminal freeze problem is fixed in the new version of Novapad.
However, the accessible terminal cannot read the messages from Claude Code.
It works very well with Gemini CLI and with Codex CLI.
Probably Claude uses a different message system than the others.
If any developer can suggest a way to also capture the messages from Claude Code, it would be very appreciated.
By the way, I found some settings that, on my PC, stop Claude Code from freezing.
NVDA does not crash anymore and the window does not freeze.
I tried the method described by @ahicks92 , but in my case it was still freezing.
These are the settings I used.
Of course, change them for your own needs if you do not want some of them.
Relevant options I use:
Configure Claude Code preferences
Auto-compact: false
Thinking mode: false
Prompt suggestions: false
Verbose output: false
Terminal progress bar: false
Default permission mode: Accept edits
Theme: Light mode (ANSI colors only)
Notifications: Terminal Bell (\a)
Editor mode: normal
Model: Default (recommended)
Auto-connect to IDE (external terminal): true.

--- Comment 12 ---
Author: ahicks92
Date: 2026-01-12T21:34:04Z

I would settle for a clarification as to whether or not using the agent SDK to write our own frontend to Claude Code, preferably by actually using Claude Code to do it, is against the terms or not.  I don't want to get banned if I do it, but it is tempting.

if anyone starts a more organized campaign (say, an open letter), I am happy to sign it.

--- Comment 13 ---
Author: ahicks92
Date: 2026-01-22T02:34:58Z

I have recently discovered that CC uses Ink: https://github.com/vadimdemedes/ink

(or according to Ink they do, anyway)

Ink's readme explains screen reader support, including for a subset of Aria.  Just leaving this here in case it is useful whenever someone triages this.

--- Comment 14 ---
Author: raivisdejus
Date: 2026-01-24T14:58:29Z

I have created a Claude Code plugin that can announce permission prompts and last sentence from Claude in a conversation. It works with all major screen readers (JAWS, NVDA, Orca and Voiceover) on all major platforms (Windows, Linux, Mac), has fallback to a system speech synthesis engine.

Check it out https://github.com/raivisdejus/claude-code-plugins

My experience with assistive technologies is limited, feedback from real users would be appreciated.

A missing feature in Claude Code that would let to improve this plugin is a hook that fires when user changes permission mode (Approve edits -> Auto approve edits (shift+tab) -> Plan mode) With hook for this in Claude Code we could add an audio message for this to the users.

--- Comment 15 ---
Author: Ambro86
Date: 2026-01-24T18:58:50Z

@raivisdejus  Thank you very much for your plugin. I will surely try it.
I can say that now I have solved all the problems with Claude, using all the settings I mentioned. The problem is not that NVDA does not speak, but that it speaks too much. While typing, it often reads a series of numbers. I think this comes from the graphic interface used by the Claude CLI.
So for this reason your plugin could be useful. However, the problem is that NVDA will probably still read those numbers. We need to find a way to stop NVDA from reading them and use only your plugin.
I will try it and let you know. Thanks again for your project!

--- Comment 16 ---
Author: rashadnaqeeb
Date: 2026-01-25T13:58:43Z

just commenting for increased visibility, also struggling with these issues

--- Comment 17 ---
Author: raivisdejus
Date: 2026-01-25T14:44:33Z

@Ambro86 Easiest way to prevent NVDA from speaking too much seems to put it to sleep with `NVDA + shift + s` when the terminal app is focused. In my tests this silenced all regular output from Windows PowerShell where Claude Code was running. Notifications from the plugin will work as they talk to NVDA directly and have fallbacks to regular speech API. 

--- Comment 18 ---
Author: ahicks92
Date: 2026-01-25T21:16:06Z

that's not sufficient for a variety of reasons, but I do appreciate the effort.  Short of an alternate frontend however, I doubt that it will be possible to solve this via plugins. For example I do watch the chain of thought and diffs in realtime for steering purposes, permission prompts exist, settings menus, etc.  It's not really solvable via plugins or hooks.  For some context many/most of us outright use VSCode as our IDE--it's not just "make thing talk" that is involved here.  But much of why I can use it at all is because some of these problems go away on a sufficiently powerful workstation, which I happen to have.

I am beginning to suspect that this issue will need (1) someone with an Anthropic contact or (2) some wider effort.  I would like to think that if this gets seen something will be done, especially since that should be reasonably easy.  I don't think that going from what it is now to fully screen reader friendly quickly would work but even a few simple things like using `>` instead of unicode in menus to mark the selected option would go a long way.

I was able to get a important fix out of Anthropic for claude.ai not that long ago.  SO there is hope *if* someone looks in the right direction.

--- Comment 19 ---
Author: BlindGuyNW
Date: 2026-01-26T00:18:06Z

Just chiming in here as another frequent Claude Code user. I am routinely frustrated by the freeze issues which can sneak up without warning, requiring the restart of a terminal session, and sometimes just locking up NVDA completely. THis among with the other problems mentioned makes the experience far from optimal as a screen reader user

--- Comment 20 ---
Author: sylvanova
Date: 2026-01-31T12:27:42Z

Hi, I am also using Claude Code with a screen reader and I can 100% confirm what the other users in this thread have said. I often have to restart NVDA and the terminal multiple times per session and in worst case even my whole pc. I would really appreciate a screen reader mode.

--- Comment 21 ---
Author: alexoloopios
Date: 2026-02-02T17:15:23Z

Just chiming in to also say I have similar issues, started using Claude Code today and these issues make me question the effort I'm putting in plus the £18 a month for the subscription, this needs to be sorted out, and the fact no one from Anthropic has come in and said anything in this thread is ridiculous.

--- Comment 22 ---
Author: bkoray
Date: 2026-02-03T00:14:18Z

I honestly switched to Claude Code because of all the hype, but I'll be going back to Codex as soon as my subscription ends. From web UI to Claude Code cli, Anthropic doesn't seem to care much about accessibility.

--- Comment 23 ---
Author: ironcross32
Date: 2026-02-09T12:19:37Z

This is still an issue.

--- Comment 24 ---
Author: alexoloopios
Date: 2026-02-09T12:22:51Z

And Anthropic haven't bothered to get someone to respond to this, at this point I've just accepted it for what it is as I am actually getting some good use out of Claude Code, let's just say if it weren't for that I wouldn't have gotten as far as I have done in developing a new mobile Mastodon app.

--- Comment 25 ---
Author: frastlin
Date: 2026-02-18T00:20:22Z

I have also been facing these issues. I would also like to report that using the npm version of claude code removes much of the odd symbols. The installed version of claude code using the native installation has so many junk symbols that it is unusable for me.
I will try these settings to see if the freezing goes away. The freezing is really a productivity killer.
I use thinking mode and plan mode quite a lot. Do you know if that is really important?

--- Comment 26 ---
Author: rperez030
Date: 2026-02-27T22:45:21Z

Adding to this thread as a user of both **NVDA on Windows** and **VoiceOver on macOS**.

My main issue is with **box-drawing characters** (e.g., `│`, `─`, `╭`, `╰`) used to render UI borders and tool call blocks. Screen readers announce these on every line, which constantly interrupts reading the actual output.

On Windows, the **NVDA speech dictionary** can suppress specific characters with some manual setup. On macOS, **VoiceOver has no effective way to filter them out**, so every response boundary and tool block gets read aloud.

A `--screen-reader` mode or `--no-ansi` flag that swaps box-drawing characters for plain ASCII — or removes decorative borders entirely — would make Claude Code significantly more efficient to use with a screen reader.

--- Comment 27 ---
Author: rperez030
Date: 2026-02-27T23:13:30Z

Following up on @ahicks92's point about having to guess which option is selected in menus — I found a workaround that helps with this.

Setting `NO_COLOR=1` in your environment causes Claude Code to display a `❯` (Heavy Right-Pointing Angle Quotation Mark, U+276F) next to the selected option instead of relying on color alone. NVDA does not pronounce it, but it shows up on a braille display, which makes menus navigable without guessing.

To enable it permanently, add this to your `~/.bashrc`:

```bash
export NO_COLOR=1
```

--- Comment 28 ---
Author: frastlin
Date: 2026-02-28T01:31:36Z


> Relevant options I use: Configure Claude Code preferences Auto-compact: false Thinking mode: false Prompt suggestions: false Verbose output: false Terminal progress bar: false Default permission mode: Accept edits Theme: Light mode (ANSI colors only) Notifications: Terminal Bell (\a) Editor mode: normal Model: Default (recommended) Auto-connect to IDE (external terminal): true.

1. Note I think the "Theme: Light mode (ANSI colors only)" is the primary culprit for the slowdown.
2. There is always a greater sign when arrowing through items like `/config`. It's not nice, but if you down arrow or up arrow, you will be able to see the greater sign move "`>`". I am using the npm install of claude code.

--- Comment 29 ---
Author: vylasaven
Date: 2026-03-03T03:53:06Z

I've been following this thread and built an open-source tool that addresses the output formatting side of these problems: **[claude-sonar](https://github.com/vylasaven/claude-sonar)**.

I've been using Claude Code like it's a religion for the past year, and reading this thread honestly horrified me. The tool output is already spammy just *visually* reading it — I can't imagine what that experience is like through a screen reader. So I built this.

It uses Claude Code's hooks system to intercept tool output and reformat it into screen-reader-friendly summaries. Instead of raw JSON or walls of code, you get concise announcements like "Edited auth.ts, changed login function" or "npm test failed, 47 passed, 2 failed."

What it does:

- **14 tool formatters** — tailored summaries for Bash, Edit, Read, Write, Grep, Glob, etc.
- **Optional TTS** — spoken announcements via `say` (macOS) or `spd-say` (Linux)
- **Earcon sounds** — short audio cues (chime for test pass, thud for test fail, etc.)
- **Code summarization** — when reading/editing files, announces function and class names instead of raw code
- **Significance filtering** — suppresses noisy routine events, highlights important ones
- **Configurable verbosity** — from compact (minimum output) to full detail

What it doesn't solve:

- The TUI rendering/NVDA freeze issues that @ahicks92, @Ambro86, @BlindGuyNW, and others have described. That's a deeper problem in how Claude Code renders to the terminal — hooks can't fix that.
- The box-drawing characters and menu navigation problems @rperez030 and @frastlin mentioned. Those need upstream changes in Claude Code itself.

This is complementary to @raivisdejus's [plugin](https://github.com/raivisdejus/claude-code-plugins) — their approach talks directly to screen reader APIs (JAWS, NVDA, Orca, VoiceOver), while claude-sonar focuses on reformatting the tool output itself into something that makes sense when spoken.

Install: `npm install -g claude-sonar && claude-sonar setup`

**A note on what this is:** I'm putting this out as a seed project for the community, not something I plan to actively maintain long-term. It's MIT-licensed, has 545 tests, full docs, and a [CLAUDE.md](https://github.com/vylasaven/claude-sonar/blob/main/CLAUDE.md) so that Claude Code itself understands how to work on it — the intended workflow is to use AI-assisted development to contribute. My hope is that people who actually live with screen readers daily will fork this and shape it into what they need. I'll try to respond to bug reports, but this is meant to be yours.

There may be bugs — the scaffolding is solid but I'm not a screen reader user, so the output quality needs real-world feedback. There's a dedicated [screen reader feedback template](https://github.com/vylasaven/claude-sonar/issues/new?template=screen_reader_feedback.md) for reporting output that sounds wrong or confusing.

--- Comment 30 ---
Author: ironcross32
Date: 2026-03-03T13:27:33Z

> I've been following this thread and built an open-source tool that addresses the output formatting side of these problems: **[claude-sonar](https://github.com/vylasaven/claude-sonar)**.
> 
> I've been using Claude Code like it's a religion for the past year, and reading this thread honestly horrified me. The tool output is already spammy just _visually_ reading it — I can't imagine what that experience is like through a screen reader. So I built this.
> 
> It uses Claude Code's hooks system to intercept tool output and reformat it into screen-reader-friendly summaries. Instead of raw JSON or walls of code, you get concise announcements like "Edited auth.ts, changed login function" or "npm test failed, 47 passed, 2 failed."
> 
> What it does:
> 
> * **14 tool formatters** — tailored summaries for Bash, Edit, Read, Write, Grep, Glob, etc.
> * **Optional TTS** — spoken announcements via `say` (macOS) or `spd-say` (Linux)
> * **Earcon sounds** — short audio cues (chime for test pass, thud for test fail, etc.)
> * **Code summarization** — when reading/editing files, announces function and class names instead of raw code
> * **Significance filtering** — suppresses noisy routine events, highlights important ones
> * **Configurable verbosity** — from compact (minimum output) to full detail
> 
> What it doesn't solve:
> 
> * The TUI rendering/NVDA freeze issues that [@ahicks92](https://github.com/ahicks92), [@Ambro86](https://github.com/Ambro86), [@BlindGuyNW](https://github.com/BlindGuyNW), and others have described. That's a deeper problem in how Claude Code renders to the terminal — hooks can't fix that.
> * The box-drawing characters and menu navigation problems [@rperez030](https://github.com/rperez030) and [@frastlin](https://github.com/frastlin) mentioned. Those need upstream changes in Claude Code itself.
> 
> This is complementary to [@raivisdejus](https://github.com/raivisdejus)'s [plugin](https://github.com/raivisdejus/claude-code-plugins) — their approach talks directly to screen reader APIs (JAWS, NVDA, Orca, VoiceOver), while claude-sonar focuses on reformatting the tool output itself into something that makes sense when spoken.
> 
> Install: `npm install -g claude-sonar && claude-sonar setup`
> 
> **A note on what this is:** I'm putting this out as a seed project for the community, not something I plan to actively maintain long-term. It's MIT-licensed, has 545 tests, full docs, and a [CLAUDE.md](https://github.com/vylasaven/claude-sonar/blob/main/CLAUDE.md) so that Claude Code itself understands how to work on it — the intended workflow is to use AI-assisted development to contribute. My hope is that people who actually live with screen readers daily will fork this and shape it into what they need. I'll try to respond to bug reports, but this is meant to be yours.
> 
> There may be bugs — the scaffolding is solid but I'm not a screen reader user, so the output quality needs real-world feedback. There's a dedicated [screen reader feedback template](https://github.com/vylasaven/claude-sonar/issues/new?template=screen_reader_feedback.md) for reporting output that sounds wrong or confusing.

I'll definitely check this out, thank you. As for the freezing issues, they've completely disappeared since I've switched to windows terminal. I had uninstalled it a while back due to issues I no longer remember with it, but since reinstalling it and using it, the experience is as good as can be expected.

---

### Issue #61473 — [BUG] Desktop app Code tab: session never returns first response on MacBook Pro M5 (unhealthy cycle 30s, no_response, no process crash)

State: OPEN | #61473
Labels: bug, has repro, platform:macos, regression, area:desktop


---



### What's Wrong?

In the Code tab of the Claude Desktop app, every session starts correctly but never produces a first response. After sending any prompt (even a simple "bonjour" in a brand-new empty local folder), the message is received (the session title is auto-set from the prompt), but no response, no thinking indicator, and no error ever appears. The session spins indefinitely and is marked unhealthy after 30 seconds.
Crucially, the underlying Claude Code process does not crash. The log shows query iterator completed followed by unhealthy cycle (30s, hadFirstResponse=false, reason=no_response). There is no Claude Code process exited with code 1. This distinguishes it from the several existing reports where the process exits at 0s (e.g. #59866, #46161, #37641). Here the process stays alive but never streams a first response.
The Claude Code CLI works perfectly on the same machine, same account, same project folders.

### What Should Happen?

The Code tab session should stream a first response like the CLI does.

### Error Messages/Logs

```shell
[info] Starting local session local_xxx in /Users/<user>/dev-local/test-cc
[info] [CCD] Passing 1 plugin(s) to SDK (skills: 1, remote: 0, local: 0)
[info] Using Claude Code binary at: /Users/<user>/Library/Application Support/Claude/claude-code/2.1.146/claude.app/Contents/MacOS/claude
[info] LocalSessions.updateSession: options={"title":"Bonjour","titleSource":"auto"}
[info] [IdleManager:session] Starting idle timeout
[info] Session local_xxx query iterator completed
[info] [CCD CycleHealth] unhealthy cycle for local_xxx (30s, hadFirstResponse=false, reason=no_response)
```

### Steps to Reproduce

Open the Desktop app, Code tab, Local mode
Select any local folder (reproduced even with a brand-new empty folder outside any cloud-synced path)
Send any prompt
Message is received, session title set, but no response ever streams; after 30s the session is marked unhealthy

### Claude Model

None

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

2.1.36

### Claude Code Version

2.1.146

### Platform

Anthropic API

### Operating System

macOS

### Terminal/Shell

Terminal.app (macOS)

### Additional Information

_No response_

# Comments on anthropics/claude-code#61473
Total: 1 comments

--- Comment 1 ---
Author: jshaofa-ui
Date: 2026-05-22T22:15:32Z

# Solution: claude-code #61473 — Desktop App Code Tab: Session Never Returns First Response on Mac

## Issue Summary

**Issue**: https://github.com/anthropics/claude-code/issues/61473
**Type**: Bug Fix (Regression — Desktop app, macOS platform)
**Severity**: HIGH — completely blocks first interaction in Code tab on Mac
**Estimated Value**: $2,000–$3,000
**Labels**: bug, regression, has-repro, platform:macos, area:desktop

### Impact

The Desktop app's Code tab fails to return the first response on macOS. When a user opens a new session in the Code tab and sends their first message, the session hangs indefinitely — no streaming response appears, no tool calls execute, and no error is displayed. The spinner continues indefinitely until the user manually terminates the session.

This is a **regression** — the behavior worked correctly in a previous version. The issue has a confirmed reproduction path and is specific to macOS.

### Symptoms
- First message in a new Code tab session never receives a response
- Subsequent messages in the same session may work (or may also hang — depends on whether the session state is corrupted)
- No error message displayed to the user
- CLI mode (`claude` in terminal) is unaffected — issue is desktop-specific
- Windows/Linux desktop builds are unaffected — issue is macOS-specific

---

## Root Cause Analysis

### Primary Root Cause: macOS-Specific Race Condition in First Response Streaming Pipeline

The Desktop app on macOS uses Electron's IPC (Inter-Process Communication) bridge to relay streaming responses from the Claude Code CLI subprocess to the renderer (UI) process. The regression is caused by a **race condition between the subprocess spawn and the first streaming event**, where the IPC listener is registered *after* the first response chunk has already been emitted.

#### Failure Sequence

```
1. User opens Code tab, sends first message
2. Desktop main process spawns claude-code subprocess (child_process.spawn)
3. Subprocess begins processing, produces first streaming chunk (text delta)
4. Main process writes chunk to IPC channel → [BUG] renderer listener not yet ready
5. First chunk is lost (fire-and-forget IPC send before listener attached)
6. Renderer waits indefinitely for first response event
7. Subsequent chunks may arrive but renderer is in "waiting for session start" state
8. UI shows perpetual spinner, no response rendered
```

#### Why This Is macOS-Specific

On macOS, the `child_process.spawn` call has different timing characteristics compared to Windows/Linux:

1. **macOS process launch overhead**: macOS has higher process spawn latency due to code signing verification (Gatekeeper), which delays the subprocess stdout/stderr pipe readiness
2. **Electron main process event loop priority**: On macOS, Electron's main process prioritizes the native app lifecycle events (NSApplication) over IPC message dispatch, causing a window where early IPC messages are dropped
3. **Pipe buffering differences**: macOS's pipe buffer size and flushing behavior differs from Linux, causing the first write to complete before the Electron IPC bridge has fully established its event listener

#### Likely Code Location

The issue is in the desktop app's session management layer, likely in one of these areas:

```
src/desktop/session/SessionManager.ts       — manages subprocess lifecycle
src/desktop/ipc/ResponseStreamBridge.ts     — bridges CLI stdout to renderer
src/desktop/renderer/components/CodeTab.tsx — renderer-side response handler
```

The specific bug is likely in the **response stream bridge initialization**:

```typescript
// BROKEN (current):
async startSession(message: string): Promise<void> {
  const subprocess = spawn('claude', ['--output-format', 'stream-json']);

  // Send message to subprocess stdin
  subprocess.stdin.write(message);

  // BUG: IPC listener is attached AFTER spawn + first write
  // On macOS, the first response can arrive before this listener is attached
  subprocess.stdout.on('data', (chunk) => {
    this.ipcRenderer.send('response-chunk', chunk);
  });

  // If the first response chunk arrives between spawn() and the .on('data')
  // registration, it is lost. The renderer never receives the session start signal.
}
```

### Secondary Contributing Factors

1. **No "session started" sentinel event**: The system relies on the first text chunk to signal session start. If that chunk is lost, the renderer has no way to know the session has begun.

2. **Missing backpressure handling**: The IPC bridge does not buffer early chunks for delivery after the listener is ready.

3. **No readiness handshake**: There is no explicit "I'm ready to receive" handshake between the renderer and main process before the subprocess is spawned.

---

## Proposed Fix

### Fix 1: Buffer Early Chunks Until Renderer Is Ready (P0 — Critical)

**File**: `src/desktop/ipc/ResponseStreamBridge.ts`

Buffer all response chunks from the subprocess until the renderer explicitly signals readiness. This eliminates the race condition entirely.

```typescript
// FIXED:
class ResponseStreamBridge {
  private buffer: string[] = [];
  private rendererReady: boolean = false;
  private pendingChunks: Buffer[] = [];

  async startSession(message: string): Promise<void> {
    const subprocess = spawn('claude', ['--output-format', 'stream-json']);

    // Register the stdout listener IMMEDIATELY, before any writes
    subprocess.stdout.on('data', (chunk: Buffer) => {
      if (this.rendererReady) {
        // Renderer is ready — send immediately
        this.ipcRenderer.send('response-chunk', chunk);
      } else {
        // Renderer not ready — buffer the chunk
        this.pendingChunks.push(chunk);
      }
    });

    // Send message to subprocess stdin
    subprocess.stdin.write(message);
  }

  // Called by renderer when it's ready to receive chunks
  handleRendererReady(): void {
    this.rendererReady = true;

    // Flush all buffered chunks in order
    for (const chunk of this.pendingChunks) {
      this.ipcRenderer.send('response-chunk', chunk);
    }
    this.pendingChunks = [];
  }
}
```

### Fix 2: Add Explicit Session Start Handshake (P0 — Critical)

**File**: `src/desktop/session/SessionManager.ts`

Add an explicit "session started" event that is sent before any streaming content, ensuring the renderer can transition out of the "waiting" state even if the first content chunk is delayed.

```typescript
// FIXED:
async startSession(message: string): Promise<SessionId> {
  const sessionId = generateSessionId();

  // Notify renderer of session start BEFORE spawning subprocess
  this.ipcRenderer.send('session-started', { sessionId });

  const subprocess = spawn('claude', ['--output-format', 'stream-json', '--session-id', sessionId]);

  subprocess.stdout.on('data', (chunk: Buffer) => {
    this.ipcRenderer.send('response-chunk', { sessionId, chunk });
  });

  subprocess.stderr.on('data', (chunk: Buffer) => {
    this.ipcRenderer.send('session-error', { sessionId, error: chunk.toString() });
  });

  subprocess.on('error', (err) => {
    this.ipcRenderer.send('session-failed', { sessionId, error: err.message });
  });

  subprocess.stdin.write(message);

  return sessionId;
}
```

### Fix 3: Add macOS-Specific Spawn Delay Guard (P1 — High)

**File**: `src/desktop/session/SessionManager.ts`

On macOS, add a small delay between subprocess spawn and first stdin write to ensure the stdout pipe is fully established. This is a defensive measure that addresses the macOS-specific timing window.

```typescript
// FIXED:
async startSession(message: string): Promise<SessionId> {
  const sessionId = generateSessionId();

  this.ipcRenderer.send('session-started', { sessionId });

  const subprocess = spawn('claude', ['--output-format', 'stream-json', '--session-id', sessionId]);

  // Register listeners immediately
  subprocess.stdout.on('data', (chunk: Buffer) => {
    this.ipcRenderer.send('response-chunk', { sessionId, chunk });
  });

  // macOS-specific: small delay to account for Gatekeeper/code-signing overhead
  // This ensures the stdout pipe is fully ready before we write to stdin
  if (process.platform === 'darwin') {
    await new Promise(resolve => setTimeout(resolve, 50));
  }

  subprocess.stdin.write(message);

  return sessionId;
}
```

### Fix 4: Add Renderer-Side Timeout with Retry (P1 — High)

**File**: `src/desktop/renderer/components/CodeTab.tsx`

Add a timeout on the renderer side that detects when the first response hasn't arrived within a reasonable window, and provides user feedback + automatic retry.

```typescript
// FIXED:
const FIRST_RESPONSE_TIMEOUT_MS = 30_000; // 30 seconds

function CodeTab() {
  const [waitingForResponse, setWaitingForResponse] = useState(false);
  const [responseTimeout, setResponseTimeout] = useState(false);

  const sendMessage = useCallback(async (message: string) => {
    setWaitingForResponse(true);
    setResponseTimeout(false);

    const timeoutId = setTimeout(() => {
      if (waitingForResponse) {
        setResponseTimeout(true);
        // Auto-retry: re-request session start
        ipcRenderer.send('request-session-restart');
      }
    }, FIRST_RESPONSE_TIMEOUT_MS);

    ipcRenderer.send('start-session', { message });

    // Clean up timeout when response arrives
    ipcRenderer.once('response-chunk', () => {
      clearTimeout(timeoutId);
      setWaitingForResponse(false);
    });
  }, [waitingForResponse]);

  return (
    <div>
      {responseTimeout && (
        <div className="timeout-banner">
          Response is taking longer than expected...
          <button onClick={retry}>Retry</button>
        </div>
      )}
      {/* ... rest of component */}
    </div>
  );
}
```

---

## Implementation Priority

| Priority | Fix | Complexity | Lines of Code |
|----------|-----|------------|---------------|
| P0 | Fix 1: Buffer early chunks | Low | ~20 lines |
| P0 | Fix 2: Session start handshake | Low | ~15 lines |
| P1 | Fix 3: macOS spawn delay guard | Low | ~5 lines |
| P1 | Fix 4: Renderer timeout + retry | Medium | ~30 lines |

**Total estimated effort**: ~70 lines of code changes across 2-3 files.

---

## Testing Plan

### Unit Tests

| Test | Description | Expected |
|------|-------------|----------|
| `ResponseStreamBridge buffers chunks before renderer ready` | Spawn subprocess, emit chunk before `handleRendererReady()` | Chunk is buffered and delivered after readiness |
| `ResponseStreamBridge passes through chunks after ready` | Spawn subprocess, emit chunk after `handleRendererReady()` | Chunk is sent immediately |
| `Session start handshake fires before subprocess spawn` | Mock spawn, verify IPC event order | `session-started` fires before any `response-chunk` |
| `macOS spawn delay does not block on other platforms` | Run on Linux/Windows, verify no delay | No measurable delay on non-macOS |

### Integration Tests

| Test | Description | Expected |
|------|-------------|----------|
| `First response returns on macOS` | Open Code tab, send message on macOS | Response appears within 5s |
| `Multiple sequential sessions work` | Send message, get response, send second message | Both responses arrive correctly |
| `Session error is surfaced` | Subprocess fails to start | Error displayed in UI |
| `Timeout banner appears after 30s` | Simulate stalled subprocess | Timeout banner shown with retry button |

### Regression Tests

| Test | Description | Expected |
|------|-------------|----------|
| `Windows desktop unaffected` | Run same flow on Windows | No change in behavior |
| `Linux desktop unaffected` | Run same flow on Linux | No change in behavior |
| `CLI mode unaffected` | Run `claude` in terminal | No change in behavior |
| `Subsequent messages in session` | Send 5+ messages in one session | All responses arrive |

### Manual Verification Steps

1. Build the desktop app for macOS (`npm run build:mac`)
2. Launch the app, open a new Code tab
3. Type a message and press Enter
4. **Verify**: Response streaming begins within 5 seconds
5. Send a second message
6. **Verify**: Response arrives normally
7. Close tab, open new tab, repeat steps 3-6
8. **Verify**: First response works every time (no intermittent failures)
9. Repeat on Windows and Linux to confirm no regression

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Buffering causes memory leak if renderer never connects | Low | Medium | Add buffer size limit + timeout; flush after 60s |
| macOS spawn delay increases perceived latency | Low | Low | 50ms is imperceptible; only on macOS |
| Handshake event breaks existing renderer that doesn't listen | Low | Medium | Make handshake non-breaking; renderer ignores unknown events |
| Timeout retry causes duplicate sessions | Medium | Medium | Cancel previous session before retrying |
| Fix doesn't address root cause (wrong diagnosis) | Low | High | Add logging to confirm the race condition before shipping |

### Overall Risk: **LOW**

The fixes are defensive in nature:
- Buffering early chunks is a standard pattern that cannot cause harm
- The session start handshake is additive — it adds a new event without removing existing behavior
- The macOS delay is a small, platform-specific guard
- The renderer timeout is a safety net that only activates on failure

### Rollback Plan

If issues arise, the changes are easily revertible:
1. Fix 1 and Fix 2 are in the same file — revert the entire `ResponseStreamBridge.ts` change
2. Fix 3 is a 5-line addition — remove the `if (process.platform === 'darwin')` block
3. Fix 4 is renderer-only — remove the timeout logic

---

## User Workaround

Until the fix is deployed, macOS desktop users can:

1. **Use the embedded terminal**: Open the terminal tab in the desktop app and run `claude` directly — the CLI is unaffected
2. **Use the CLI directly**: Run `claude` in the macOS Terminal app
3. **Send a dummy message first**: Type a single character and send it; the second message may work (unreliable)
4. **Restart the app**: Sometimes the race condition doesn't trigger on first launch

---

## Files to Modify

| File | Change |
|------|--------|
| `src/desktop/ipc/ResponseStreamBridge.ts` | Add chunk buffering until renderer ready (Fix 1) |
| `src/desktop/session/SessionManager.ts` | Add session start handshake + macOS delay guard (Fix 2, Fix 3) |
| `src/desktop/renderer/components/CodeTab.tsx` | Add timeout + retry logic (Fix 4) |
| `tests/unit/desktop/ipc/ResponseStreamBridge.test.ts` | New unit tests for buffering behavior |
| `tests/integration/desktop/session/SessionManager.test.ts` | New integration tests for session lifecycle |

---

## Summary

| Item | Detail |
|------|--------|
| Issue | claude-code #61473 |
| Type | Bug fix (Desktop app, macOS, regression) |
| Root Cause | Race condition: first response chunk arrives before IPC listener is registered |
| Fix Complexity | Low (~70 lines across 2-3 files) |
| Estimated Value | $2,000–$3,000 |
| Severity | HIGH — blocks all first interactions on macOS |
| Risk of Fix | LOW — defensive, additive changes |
| Competition | Assess based on issue comments |

---

### Issue #54434 — [Bug] SSE stream stalls in long-running sessions without message_stop event

State: OPEN | #54434
Labels: bug, has repro, platform:linux, area:api


---

# SSE stream from `/v1/messages` stalls mid-response main-thread requests (no `message_stop`, no error event)

## Summary

In long-running interactive Claude Code sessions, SSE responses from `/v1/messages` repeatedly **stop emitting events mid-response** without sending `message_stop` or any error event. The connection stays open and the client correctly waits — but no further bytes arrive. Most stalls recover on their own after ~50–70s; some never recover and only resolve when the user presses ESC. Subagent streams in the same session are unaffected.

Claude Code's own `[Stall]` telemetry (`stream_idle_partial`, `Streaming stall detected`, `Streaming completed with N stall(s)`) cleanly captures the behavior — this issue is filing what that telemetry is reporting.

## Environment

- **Claude Code version**: `2.1.119` (native install, `cc_version=2.1.119.9c7`, entrypoint `cli`)
- **Model**: `claude-opus-4-7` and `claude-sonnet-4-6`
- **Subscription**: Team, `rateLimitTier=default_claude_max_5x`
- **OS**: Linux 7.0.0-1-cachyos, terminal Konsole 26.04.0
- **Relevant env**:
  - `CLAUDE_STREAM_IDLE_TIMEOUT_MS=900000`
  - `API_TIMEOUT_MS=600000`
  - `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1`
  - `CLAUDE_CODE_DISABLE_1M_CONTEXT=1`

## Reproduction

Not deterministic but very high frequency: in a single 26-minute working session (`b3ad7516-35cd-47cb-9e98-6916ee362882`), **5 distinct stalls** occurred — roughly one every five minutes of active use. Behavior reproduces across sessions.

The stalls happen during normal multi-turn coding work (tool calls + bash + edits). No special conditions required.

## Observed behavior (from debug log)

All five stalls were on `source=repl_main_thread`, each with a different `x-client-request-id`. All stalled **early in the response** (under ~5.4KB / ~1000 tokens streamed), and then went silent with the connection still open.

| # | Stall start (UTC) | `x-client-request-id` | Bytes when frozen | Outcome |
|---|---|---|---|---|
| 1 | `2026-04-26T19:25:46Z` | `721d0de1-200f-422e-b7c8-c90dd211f62c` | 737 | Recovered after **51.8s** |
| 2 | `2026-04-26T19:28:45Z` | `2f671a02-f62f-433a-8cae-6ac3afdb1832` | 4336 | Recovered after **67.6s** |
| 3a | `2026-04-26T19:40:43Z` | `2f39599a-9ce9-4d65-ba2d-6476635db3b4` | 659 | Recovered after ~16s |
| 3b | `2026-04-26T19:41:17Z` | `307a8268-8e8a-4afd-ab90-8ac8efc4c722` | 653 | Recovered after ~8s |
| 4 | `2026-04-26T19:45:57Z` | `28380ec8-29ba-4e2e-8818-f4a2af125182` | 5373 | **Did not recover** (≥120s of zero bytes when log was captured; user had to ESC) |

The 51.8s and 67.6s recovery times look like they line up with a 60s server-side internal timeout/retry boundary.

### Representative log excerpt (stall # 4, the one that didn't recover)

```
2026-04-26T19:45:26.603Z [DEBUG] [API REQUEST] /v1/messages x-client-request-id=28380ec8-29ba-4e2e-8818-f4a2af125182 source=repl_main_thread
2026-04-26T19:45:28.731Z [DEBUG] Stream started - received first chunk
2026-04-26T19:45:42.866Z [DEBUG] (last activity from this stream)
2026-04-26T19:45:57.864Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=15000 bytesTotal=5373 idleDeadlineMs=900000
2026-04-26T19:46:12.863Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=30000 bytesTotal=5373 idleDeadlineMs=900000
2026-04-26T19:46:42.864Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=60001 bytesTotal=5373 idleDeadlineMs=900000
2026-04-26T19:47:42.864Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=120000 bytesTotal=5373 idleDeadlineMs=900000
```

`bytesTotal=5373` is unchanged across all four warnings — i.e. zero bytes received during the 2-minute window. No `message_stop`, no `error` event, no TCP-level disconnect.

### Representative log excerpt (stall # 1, which recovered)

```
2026-04-26T19:25:27.805Z [DEBUG] [API REQUEST] /v1/messages x-client-request-id=721d0de1-200f-422e-b7c8-c90dd211f62c source=repl_main_thread
2026-04-26T19:25:30.445Z [DEBUG] Stream started - received first chunk
2026-04-26T19:25:46.135Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=15001 bytesTotal=737 idleDeadlineMs=900000
2026-04-26T19:26:13.288Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=14999 bytesTotal=773 idleDeadlineMs=900000
2026-04-26T19:26:22.912Z [WARN] Streaming stall detected: 51.8s gap between events (stall #1)
2026-04-26T19:26:43.288Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=15000 bytesTotal=17424 idleDeadlineMs=900000
2026-04-26T19:26:48.862Z [WARN] Streaming completed with 1 stall(s), total stall time: 51.8s
```

Note that `bytesTotal` only moves from 737 → 773 between the first two warnings (a trickle), then jumps to 17424 after the gap is over. That suggests the server held back roughly 16KB of generated tokens for ~50s before flushing.

## What's *not* happening

- **Not the client**: the client is doing the right thing — `[Stall] stream_idle_partial` fires every 15s while waiting, no read errors are logged.
- **Not the network**: the connection stays open the whole time. TCP isn't dropping. No proxy involved (`ANTHROPIC_CUSTOM_HEADERS=false`, no `Authorization` override).
- **Not the hooks/tools**: `tool_dispatch_*` events all complete normally and quickly. Hooks aren't wedged. No tool exceeds even a second.
- **Not the local environment**: bash/LSP/MCP all healthy. The 6 unauthorized `claude.ai` MCP connectors and the one Mermaid-Chart 502 at startup are unrelated and complete in milliseconds.
- **Not subagents**: ~30+ requests with `source=agent:builtin:Explore` or `source=agent:builtin:Plan` in the same session, none stalled. Only `source=repl_main_thread` requests are affected.
- **Not context-size**: most recent stall fired with `autocompact: tokens=73852 threshold=167000` — well under any threshold.

## What I think is happening (speculation)

A server-side issue specific to streaming on the path used by main-thread Claude Code requests. The pattern (early-token stall, ~60s internal recovery boundary, never affects subagents) is consistent with an overloaded/restarting inference worker holding generated tokens before flushing them downstream — and occasionally dropping the rest.


## Session metadata for cross-reference

- Session ID: `b3ad7516-35cd-47cb-9e98-6916ee362882`
- Project: medium-sized git repo (~121 tracked files), no LSP servers active
- Plugins enabled: `feature-dev`, `code-review`, `ralph-loop`, `playwright` (MCP), `commit-commands`, `security-guidance`, `pr-review-toolkit`, `claude-code-setup`, `superpowers-extended-cc`
- `attribution header x-anthropic-billing-header: cc_version=2.1.119.9c7; cc_entrypoint=cli`

Happy to share the full debug log directly with Anthropic engineering if useful.

# Comments on anthropics/claude-code#54434
Total: 9 comments

--- Comment 1 ---
Author: datus1982
Date: 2026-04-28T22:57:09Z

**Independent second confirmation on macOS arm64 + complementary OpenClaw-side observation.**

Hitting the same SSE mid-stream stall pattern, identical claude version (`2.1.119`), but on a different OS (macOS Tahoe, arm64). Different invocation path: `claude` is being spawned as a subprocess by [OpenClaw](https://github.com/openclaw/openclaw) `2026.4.24` with `claude -p --output-format stream-json --verbose --permission-mode bypassPermissions ...` rather than the interactive REPL.

## What I observe (concurs with #54434)

When the stall fires:
- `lsof -p <claude_pid>` shows `TCP api.anthropic.com:443 ... ESTABLISHED` with zero bytes flowing
- `sample <claude_pid>` shows the main thread parked in `kevent64` (Bun event loop idle, waiting on I/O)
- The CLI's stderr produces zero output during the stall — the silence is the smoking gun
- No `message_stop` event, no error event — exactly as KingPin reports

I separately ruled out the Datadog telemetry endpoint (`http-intake.logs.us5.datadoghq.com`) by `/etc/hosts` blackholing it and observing identical wedge behavior afterward — `lsof` post-block confirmed only the Anthropic socket was ESTABLISHED. The hang is definitively on the Anthropic SSE stream, consistent with KingPin's repro.

## Complementary observation from the OpenClaw side

OpenClaw's gateway has a per-process watchdog (`noOutputTimeoutMs`, default `180000` ms with a 180s floor) that kills the `claude` subprocess if no stdout arrives for the configured duration. So in our setup the stall doesn't surface to the user as a frozen UI — it surfaces as `CLI produced no output for 180s and was terminated. (timeout)` and a `FailoverError` to the next model. The user-visible symptom is "every model in the fallback chain returns 'all models failed', taking 13 minutes total" rather than KingPin's "spinner forever, ESC to recover."

We patched the OpenClaw watchdog floor down to 60s to shrink the user-facing pain to ~3 minutes (full chain walk through 5 models × 60s each), at which point we were going to file an upstream issue here — but #54434 already nails the root cause and #25979 has the same symptom with a different invocation path. Adding our data instead of opening a duplicate.

## Important caveat against aggressive client-side timeouts (relevant to anyone considering a workaround)

KingPin's data shows **most stalls naturally recover at 50–70s** (51.8s, 67.6s in his table). Aggressive client-side timeouts below ~75s will amputate naturally-recoverable stalls, not just terminate unrecoverable ones. We're seeing this trade-off in our 60s OpenClaw watchdog — some terminations are likely killing streams that would have self-resolved within another 10s. For the proper fix path: a per-chunk read timeout in claude's HTTP client at ~120–180s (well past the natural recovery window) would catch genuinely-stuck streams without false-positive termination of slow-but-recovering ones.

## Suggested fix shape (concurs with #25979's "1.")

Add a per-chunk SSE read timeout to claude's HTTP client (Bun's `fetch` / SSE consumer doesn't impose one by default). On timeout, abort the stream, surface a retryable error with the partial response if any, and let the existing retry/backoff logic kick in. Default of 120–180s would clear the natural recovery window seen in #54434's data while still bounding the worst case.

Happy to share the OpenClaw-side patch (`CLI_FRESH_WATCHDOG_DEFAULTS.minMs`) and the wedge-sampler script we use to capture stall stacks if useful. Configuration:

- macOS Tahoe (Darwin 25.4.0), arm64
- Claude CLI `2.1.119`
- `cliBackend.args: ["-p", "--output-format", "stream-json", "--verbose", "--permission-mode", "bypassPermissions"]`
- Models tested: `claude-opus-4-7`, `claude-sonnet-4-6`, `claude-opus-4-6`, `claude-opus-4-5`, `claude-sonnet-4-5`, `claude-haiku-4-5` — all exhibit the same stall pattern, suggesting the issue is in the HTTP client, not model-specific.
- OAuth credential path (Max plan), routed through the cli binary (not direct API)
- `CLAUDE_STREAM_IDLE_TIMEOUT_MS` not set (using defaults)


--- Comment 2 ---
Author: 0xbrainkid
Date: 2026-04-28T23:10:36Z

This is stream-completion integrity failure.

If SSE streams stall in long-running sessions without a `message_stop` event, then the product loses the event that tells operators and downstream logic whether a turn actually reached a completed state. That breaks more than UI polish — it breaks the contract around turn finality.

Why it matters:
- users cannot tell whether to wait, retry, or intervene
- clients that depend on `message_stop` for cleanup or state transitions can hang indefinitely
- long-running sessions become especially fragile because the longer the stream, the more damaging ambiguous completion becomes

I would want clarity on:
1. whether generation completed server-side and only the terminal event was dropped
2. whether the issue is transport idle timeout, server flush behavior, or event sequencing under long streams
3. whether clients have any authoritative fallback to determine completion when `message_stop` is absent

For agent systems, end-of-turn certainty is part of control. If completion can become ambiguous, every downstream recovery decision gets harder.

--- Comment 3 ---
Author: KingPin
Date: 2026-04-30T17:36:47Z

this is getting really bad now, with hours of uselessness at a time. havent gotten anything out of Claude in past 3 hours so far. and this is happening for multiple hours every single day now. Intermittent small amounts of output with the majority of the tasks timing out with `API Error: Stream idle timeout - partial response received`

--- Comment 4 ---
Author: benjaminrigaud-gg
Date: 2026-05-06T12:35:14Z

Reproducing on Linux/Bun with the runtime's stall detector firing as documented.

**Environment**
- Claude Code 2.1.128 (Bun-backed)
- Ubuntu 24.04.4 LTS, kernel 6.17.0-23-generic
- Terminal: Ghostty
- Workload: interactive multi-turn coding session, `--resume`

**Cadence in a 7-minute window after resuming a long session:**

```
09:43:20  Fast mode unavailable...                          ← heartbeat
                       [ 64.55 s of silence ]
09:44:24  Dynamic tool loading: 10/108 deferred tools
09:46:25  [ 57.05 s gap before this line ]
09:47:25  [ 55.41 s gap ]
09:48:25  [ 53.78 s gap — coincides with: MCP server "notion": HTTP connection dropped after 321s uptime ]
09:49:26  [WARN] Streaming stall detected: 53.6s gap between events (stall #1)
```

5 stalls in 7 minutes, 53–65 s each, ~60-second cadence — matches your "5 stalls in 26 min, 50–70 s, every ~5 min" almost exactly.

**Useful diagnostic technique**: the `[DEBUG] Fast mode unavailable` log fires every ~1 second during normal operation. When the event loop is blocked, *the heartbeat itself goes silent* — that's a clean signal that the block is event-loop, not network. In our log, every long gap is preceded by the heartbeat as the last line. That suggests at least some of these stalls are client-side (event loop blocked), not purely server-side SSE issues.

**Possible upstream cause**: at the time of these stalls the umbrella process had VmRSS 6.5 GB and a heap profile consistent with a major-GC working set that takes tens of seconds to mark-and-sweep. Restarting the session (starting from a fresh small heap) eliminates the stalls. Filed leak data in #56335.

This issue may be downstream of the heap retention. Worth checking if a fix to the underlying retention reduces stall frequency.


--- Comment 5 ---
Author: chriscase
Date: 2026-05-07T16:36:10Z

**Adding a much-longer-duration data point** that fits your "some never recover" branch — this stall went **7h 58m** before manual intervention.

### Environment

- Claude Code: 2.1.126 (CLI), running `claude --resume <session-id>` on macOS 26.x
- Subscription: Claude Max
- Effort level: `xhigh` (set via `/effort max` at session start)

### Timeline (from the session JSONL)

The hang occurred in a long-running interactive session (`ac79b4e9-71ea-4a37-a8ce-03bcff6632df`, ~5,265 lines / 12 MB). Excerpting the boundary:

```
[5246] 2026-05-07T06:05:25.876Z  user        tool_result  (Bash output: ESLint warnings in useRemoteEventListeners.ts)
[5251] 2026-05-07T06:05:25.990Z  pr-link     (CCD/CLI metadata event)
                                 ─── 7h 57m 18s of pure silence ───
[5252] 2026-05-07T14:02:44.594Z  queue-operation  (user-triggered)
[5339] 2026-05-07T14:03:30.359Z  user        text: "Continue from where you left off."
```

The model had just produced a burst of 6 tool_use calls (5239–5245) — a sequence of grep/awk/Read calls investigating React-hook dependency arrays. The last tool_result came back with the ESLint output, and the model was supposed to take that turn to produce its next response. **Nothing came back for 7h 58m.** The session JSONL contains zero events in that window — no assistant text, no Sentry capture, no error event, no `[Stall]` warning, no recovery, no retry. Just a flat gap.

### Why this is high-signal for #54434

1. **Order of magnitude longer** than any case in your table (longest there was ≥120s observed). 7h 58m establishes that there's no upper bound on the "some never recover" branch.
2. **No client-side timeout fired** — `CLAUDE_STREAM_IDLE_TIMEOUT_MS` defaults to 900s (15 min) per your environment. If that timer was active here, it should have fired ~32 times. Either the timer doesn't apply to this code path, or it isn't surfacing when it does fire on `--resume` sessions.
3. **No error surfaced to the user** — the CLI just sat at a thinking spinner all night. User came back the next morning, found it still spinning, typed "Continue from where you left off." to unstick it. From a UX perspective this is the worst-case manifestation: silent failure with no liveness signal.
4. **Same trigger pattern**: mid-conversation, immediately after a tool_result, on `--resume` of a long-running session. Same `source=repl_main_thread` code path you identified.

### Differences worth flagging

- **`xhigh` effort** is in play here. Could be that the higher-effort path has a different stall behavior or different timeout discipline. Worth checking whether the affected code path differs between effort levels.
- **No `[Stall]` warnings logged**. In your reproduction, `[Stall] stream_idle_partial` fired every 15s during the wait. In this session's JSONL, no such warning appears at all — but I'm reading from the JSONL, not the debug log, so it's possible the warnings exist there. Will retrieve and update if found.

### Cross-references

- This corroborates **#56860** (spinner-forever on Windows) and **#55308** (mid-task hang causing token reuse on resume) as likely the same underlying SSE stall observed across platforms.
- Distinct from **#55241** and **#52995** which are `--resume` *startup* hangs (don't return to prompt), not mid-session stalls.

If maintainers want the full session JSONL for diagnostic purposes, happy to share it directly via support — it's 12 MB and contains private repo paths so I won't attach here.

--- Comment 6 ---
Author: chriscase
Date: 2026-05-07T16:40:35Z

**Bonus data point in the same thread**: while I was drafting the previous comment, **the desktop app (CCD) had its own ~2h SSE stall on the same workflow**. So this isn't CLI-specific — same bug, same protocol, both client surfaces.

### Environment
- Claude Code Desktop (CCD): 2.1.121 (renderer), CLI binary 2.1.126
- macOS 26.x
- Subscription: Claude Max
- Different session from the 8h CLI hang in my prior comment — totally separate workflow, separate session JSONL

### What was happening when it stalled

Investigating the previous CLI hang (this issue's repro). Sequence of recent activity right before the desktop stall:

1. Ran `gh issue list` and `gh search` shell commands to find related issues — all returned successfully
2. Ran `gh issue view 54434 --json body` and `gh issue view 55241 --json body` in a single Bash invocation — output streamed back fine, ~4 KB total
3. Was preparing to draft a comment to post here

That's where the SSE stream stalled. The desktop client sat at a "Thinking…" indicator for ~2h with no token output, no error, no recovery, no Sentry capture. User had to type a new message ("you just got stuck for 2 hours, wtf?") to interrupt and re-prompt — at which point the response came back immediately.

### Why this matters for triage

The 8h CLI case from my previous comment + this 2h desktop case are **same bug, same trigger pattern (mid-response stall after tool_result), two different client surfaces**. So the fix can't live in either client alone — the silent-stream behavior is upstream of both, in the SSE pipe from `/v1/messages`. That tracks with this issue's diagnosis (server-side worker holding tokens before flushing, occasionally dropping the rest).

Practical UX consequences worth surfacing:

- **CLI**: spinner forever, no error, no liveness signal. User loses an entire night of work before noticing.
- **Desktop**: "Thinking…" indicator forever, no error, no liveness signal, no Sentry event (this is distinct from the renderer-crash Sentry pattern in #54369 / #55220 — those fire `Main webview render process gone`; this one fires nothing at all).

In both cases, neither client surfaces the stall to the user despite Claude Code's own `[Stall] stream_idle_partial` telemetry detecting it server-internally. **An ESC-equivalent prompt or "stream idle for >Ns, want to retry?" affordance would prevent the worst-case workflow loss** even if the underlying server-side fix takes longer to land.

--- Comment 7 ---
Author: Dan-Jarvis
Date: 2026-05-16T06:14:57Z

Reproducing this on Windows 11 with the Claude Code VS Code extension. Same fingerprint as the original report, different platform, with multi-network confirmation that rules out the network layer entirely.

## Environment

- Windows 11, desktop machine
- Claude Code version: `2.1.142.2af` (VS Code extension, `cc_entrypoint=claude-vscode`)
- Standalone CLI version: `2.1.88` (npm-global via nvm, Node 24.13.1) — same stall behavior in both
- Auth: claude.ai OAuth (Max plan), not API key
- Models tested: Opus 4.7 (default), reproduces identically

## Symptom

Fresh session, zero files in context, single prompt. Stream starts normally, receives ~650 bytes, then goes silent. `[Stall] stream_idle_partial` warnings fire every 15 seconds. Connection stays open. No error surfaced.

Key detail: **the time-to-first-stall is mechanically consistent at 15.003 seconds across every test** — same to the millisecond on three different networks.

## Log excerpts (three separate sessions, three different networks)

Ethernet, NordVPN on (source IP `10.5.0.2`):
```
05:23:16.817Z [DEBUG] Stream started - received first chunk
05:23:31.820Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=15003 bytesTotal=630
```

Ethernet, NordVPN off (source IP `192.168.0.88`, direct via ISP):
```
05:32:38.204Z [DEBUG] Stream started - received first chunk
05:32:53.207Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=15003 bytesTotal=653
```

T-Mobile mobile hotspot, NordVPN off (IPv6 source, completely different ISP/path):
```
05:58:27.889Z [DEBUG] Stream started - received first chunk
05:58:42.903Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=15015 bytesTotal=645
```

All three: fresh session, `tracking 0 files`, `autocompact: tokens=[REDACTED] level=ok`, same prompt.

## What was ruled out

- ✅ Network path (3 different networks, identical 15.003s timing)
- ✅ ISP (Sparklight cable + T-Mobile cellular both reproduce)
- ✅ VPN (NordVPN on vs off — identical behavior)
- ✅ NordVPN Threat Protection Pro (paused — no change)
- ✅ Modem (Hitron CODA-5712, firmware 7.3.5.1.2b23 — bypassed via hotspot)
- ✅ Claude Code version (updated mid-test from 2.1.141 to 2.1.142.2af — no change)
- ✅ Session length / context size (fresh session, 0 files tracked, well under autocompact threshold)
- ✅ Windows Defender Network Protection (`EnableNetworkProtection: 0`)
- ✅ Third-party AV (none installed)

`curl.exe -v -I https://api.anthropic.com/v1/messages` returns 405 in ~200ms on every network tested. The API endpoint is reachable; only long-lived SSE streams stall.

## Additional observations

- `bytesTotal` is consistently in the 630–666 range across all stalls — suggests the stream dies after roughly the same initial burst regardless of prompt or network.
- ALPN consistently negotiates `http/1.1` (Windows schannel via curl) — unclear if the SDK negotiates differently.
- `Stream started - received first chunk` always fires 2–3 seconds after request — initial RTT is fine.

## Client request IDs

For correlation:
- `9e7cc463-3c86-4f0b-8fa4-7fbbd9952acb`
- `29afebe7-4802-4f33-afb6-d70ec662776e`
- `6ae2e8cf-e386-4ac7-9697-92e3bc5a9c21`
- `5d7e0230-a30e-4ffa-a070-b5a7d10af471`
- `212baedd-aee0-4121-90ab-48c97de23ed2`

Happy to provide full debug logs, additional traces, or test specific theories. The multi-network confirmation took some effort to set up but the result is unambiguous: this is not a client-side network issue.

--- Comment 8 ---
Author: angusrob
Date: 2026-05-22T13:36:12Z

Still seeing this, every request stalls 90s then retries successfully. Fresh session, no context bloat.

Request IDs from this morning (UTC):

7fd8ae54-022e-4262-ab98-b8d300d13f5b 13:04
989186af-9743-43de-9fe1-8be52a6e3a6d 13:06
cf1745c0-914f-4b48-94d7-f68ace4bf99e 13:21

Platform: macOS, VS Code extension, cc_entrypoint=claude-vscode, Max plan OAuth

--- Comment 9 ---
Author: andrewdirisio
Date: 2026-05-24T17:49:29Z

Been days of this with any use of Opus 4.7 in the Claude VSCode plugin. Doesn't matter if it's a simple or complex task, things hang for huge amounts of time with every prompt. While they do eventually finish sometimes, Claude's output just shows an endless stream of this with the stall time compounding to be longer and longer each time:

```
2026-05-24 13:41:51.278 [info] From claude: 2026-05-24T17:41:51.279Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=15005 bytesTotal=660 idleDeadlineMs=300000

2026-05-24 13:42:19.674 [info] From claude: 2026-05-24T17:42:19.675Z [WARN] [Stall] stream_idle_partial lastChunkAgeMs=15001 bytesTotal=696 idleDeadlineMs=300000

2026-05-24 13:42:42.772 [info] From claude: 2026-05-24T17:42:42.774Z [WARN] Streaming stall detected: 66.5s gap between events (stall #1) 
```

---

### Issue #59804 — Occasional garbled Chinese characters in streaming output

State: CLOSED | #59804
Labels: duplicate


---

## Description

When Claude Code streams responses containing Chinese text, occasionally a few characters appear garbled/mojibake (e.g., "看下���果" instead of "看下效果") while all surrounding characters render correctly.

## Environment

- Claude Code CLI (macOS)
- Terminal: default zsh
- Model: claude-opus-4-6

## Root cause hypothesis

UTF-8 Chinese characters are 3 bytes each. When the streaming response chunks happen to split at a byte boundary within a multi-byte character, the terminal renders the incomplete bytes as replacement characters (�).

## Reproduction

- Not reliably reproducible — it's a race condition dependent on where chunk boundaries fall
- Happens occasionally in longer responses mixing Chinese and ASCII text
- Only a few characters are affected per occurrence, not entire lines

## Expected behavior

All multi-byte characters should be buffered correctly before rendering, regardless of chunk boundaries.

# Comments on anthropics/claude-code#59804
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-16T19:32:49Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/39593
2. https://github.com/anthropics/claude-code/issues/40574
3. https://github.com/anthropics/claude-code/issues/46863

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: github-actions[bot]
Date: 2026-05-20T10:11:38Z

This issue has been automatically closed as a duplicate of #39593.

If this is incorrect, please re-open this issue or create a new one.

🤖 Generated with [Claude Code](https://claude.ai/code)

---

### Issue #51239 — [BUG] Claude Code hangs with local Ollama on a trivial prompt, while direct /v1/messages works

State: OPEN | #51239
Labels: bug, has repro, platform:linux, area:providers, stale


---



### What's Wrong?

Claude Code hangs when using a local Ollama backend through Anthropic-compatible configuration.

The problem happens even with a trivial prompt like `ciao`.

Important detail: the same Ollama model responds correctly when called directly through Ollama's Anthropic-compatible `/v1/messages` endpoint, so this does not look like a basic Ollama connectivity or basic `/v1/messages` compatibility problem.

This reproduces with local Ollama models on my setup and does not appear to be specific to a single model.

### What Should Happen?

Claude Code should return a normal response for a trivial prompt, just like the same model does when queried directly through Ollama's Anthropic-compatible `/v1/messages` endpoint.

### Error Messages/Logs

```shell
Environment:
- Claude Code: 2.1.114
- Ollama: 0.21
- OS: Ubuntu 25.10
- Kernel: 6.17.0-20-generic
- CPU: AMD Ryzen 7 6800H
- CPU cores: 8
- Logical CPUs / threads: 16
- RAM: 30 GiB
- GPU: no discrete GPU
- Graphics hardware present on the machine: AMD Radeon 680M integrated graphics
- Actual inference mode on this setup: CPU-only

Ollama systemd override:
[Service]
User=lupo
Group=lupo
Environment="HOME=/home/lupo"
Environment="OLLAMA_MODELS=/home/lupo/.ollama/models"
Environment="OLLAMA_CONTEXT_LENGTH=65536"
Environment="OLLAMA_NUM_PARALLEL=1"
Environment="OLLAMA_KEEP_ALIVE=1m"
CPUAccounting=yes
CPUQuota=400%
CPUQuotaPeriodSec=10ms
Nice=10
IOSchedulingClass=idle

Claude Code / Anthropic-compatible configuration:
- ANTHROPIC_AUTH_TOKEN=ollama
- ANTHROPIC_BASE_URL=http://127.0.0.1:11434

Main reproduction model:
- qwen2.5-coder:7b-opencode-32k

Direct Ollama Anthropic-compatible request that succeeds:
curl http://127.0.0.1:11434/v1/messages \
  -H 'Content-Type: application/json' \
  -H 'x-api-key: ollama' \
  -H 'anthropic-version: 2023-06-01' \
  -d '{
    "model": "qwen2.5-coder:7b-opencode-32k",
    "max_tokens": 64,
    "messages": [
      {
        "role": "user",
        "content": "ciao"
      }
    ],
    "stream": false
  }'

Response:
{"id":"msg_e1a1726675e5761fd7896619","type":"message","role":"assistant","model":"qwen2.5-coder:7b-opencode-32k","content":[{"type":"text","text":"Ciao! Come posso aiutarti oggi?"}],"stop_reason":"end_turn","usage":{"input_tokens":31,"output_tokens":12}}

Relevant Ollama log line from successful direct test:
[GIN] 2026/04/20 - 19:45:21 | 200 | 7.100566535s | 127.0.0.1 | POST "/v1/messages"

Relevant Ollama log line observed during Claude Code usage:
[GIN] 2026/04/20 - 19:35:59 | 500 | 5m57s | 127.0.0.1 | POST "/v1/messages?beta=true"

Additional successful direct-test model/runtime details:
qwen2.context_length = 32768
llama_context: n_ctx = 32768
time=2026-04-20T19:45:17.491+02:00 level=INFO source=server.go:1402 msg="llama runner started in 3.29 seconds"
[GIN] 2026/04/20 - 19:45:21 | 200 | 7.100566535s | 127.0.0.1 | POST "/v1/messages"
```

### Steps to Reproduce

1. Start Ollama locally on 127.0.0.1:11434

2. Configure Claude Code to use Ollama through:
   - ANTHROPIC_AUTH_TOKEN=ollama
   - ANTHROPIC_BASE_URL=http://127.0.0.1:11434

3. Launch Claude Code with a local model, for example:
   claude --model qwen2.5-coder:7b-opencode-32k

4. Send a trivial prompt:
   ciao

5. Observe that Claude Code hangs and does not return a response in the UI.

6. Compare this with a direct Ollama Anthropic-compatible request to /v1/messages using the same model, which succeeds and returns a normal response.

### Claude Model

Other

### Is this a regression?

I don't know

### Last Working Version

_No response_

### Claude Code Version

2.1.114

### Platform

Anthropic API

### Operating System

Ubuntu/Debian Linux

### Terminal/Shell

Other

### Additional Information

_No response_

# Comments on anthropics/claude-code#51239
Total: 4 comments

--- Comment 1 ---
Author: kev-leehc
Date: 2026-04-22T18:25:07Z

Me too

Claude Code Version
2.1.117

Operating System
Mac Intel

--- Comment 2 ---
Author: Luporosso76
Date: 2026-04-24T15:28:01Z

I manually tested all relevant Ollama endpoints with the same model and trivial prompt, and they all work correctly.

Successful manual tests:
- POST /v1/chat/completions -> 200 OK
- POST /v1/messages -> 200 OK
- POST /v1/messages?beta=true -> 200 OK

So this is not caused by:
- the endpoint path itself
- the `?beta=true` query parameter
- basic Ollama compatibility for these APIs

This strongly suggests Claude Code is sending a problematic request payload or using a client-side flow that differs from the simple successful manual requests.

Given the Ollama logs also show:
- `aborting completion request due to client closing the connection`

the issue now looks much more like a Claude Code request construction / streaming / tools / client-handling problem, not an Ollama endpoint problem.

--- Comment 3 ---
Author: jjhoii
Date: 2026-04-28T11:34:52Z

Confirming this on a different setup, with a key additional finding: **`claude -p` works fine, interactive mode hangs.**

## Setup

- Claude Code 2.1.121
- Upstream: an Anthropic-compatible gateway (LiteLLM-backed) — different from OP's Ollama, same symptom
- Reproduced with both:
  - Bedrock Anthropic Haiku 4.5 (`global.anthropic.claude-haiku-4-5-20251001-v1:0`)
  - A non-Anthropic open-weight model routed through the same gateway

Direct `/v1/messages` (curl) works fine in all cases. Streaming responses are well-formed (verified via a transparent capture proxy: all `content_block_start` / `content_block_stop` / `message_stop` events present, valid `thinking` blocks with signatures, valid `tool_use` input JSON).

## Key isolation: `-p` vs interactive

Same prompt, same env, same project, same model — only the invocation differs. Reproduces with prompts as short as `ls`:

| Mode | API request `source` | Tool ID format | tool_dispatch | tool_result in history | Outcome |
|------|---|---|---|---|---|
| `claude -p "..."` | `sdk` | `toolu_bdrk_*` | 6 (`outcome=ok`) | **6 ✅** | Completes successfully |
| `claude` (interactive) | `repl_main_thread` | `toolu_bdrk_*` | 1 (`outcome=ok`) | **0 ❌** | Hangs after first tool dispatch |

Same model, same gateway, same auth, same project — only `-p` vs no `-p` matters.

## What looks broken (debug log, interactive mode)

```
[DEBUG] [API REQUEST] /v1/messages source=repl_main_thread
[DEBUG] Stream started - received first chunk
[INFO] [Stall] tool_dispatch_start tool=Bash toolUseId=toolu_bdrk_... permissionDecisionMs=5
[DEBUG] Creating shell snapshot for bash (/bin/bash)
[DEBUG] Spawning shell without login (-l flag skipped)
[INFO] [Stall] tool_dispatch_end tool=Bash toolUseId=toolu_bdrk_... outcome=ok durationMs=185
                                  ↑ tool runs successfully
... silence ...
... no [API REQUEST] for the next turn ever fires ...
```

The project session log (`~/.claude/projects/<proj>/<sid>.jsonl`) records the assistant `tool_use` event but **no corresponding user `tool_result` event is ever appended**. Bash actually executed (`outcome=ok` in 185ms), but the result never gets folded back into the message history → next API request is never constructed → hang. By contrast, `-p` mode produces a clean `assistant tool_use → user tool_result` chain with each dispatch, every time, on the same model and gateway.

This points at the `repl_main_thread` agent loop specifically. The `sdk` path (used by `-p`) handles the same response structure correctly; `repl_main_thread` does not.

## Things that don't matter (ruled out)

- **Streaming SSE structure from upstream**: Captured every chunk with a transparent proxy. All `content_block_start` / `content_block_stop` / `message_stop` events present and well-ordered, valid signatures on thinking blocks, valid tool_use input JSON.
- **`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`**: No effect on the hang.
- **HTTP/1.1 vs HTTP/2 to upstream**: No effect.

--- Comment 4 ---
Author: CleverCoder
Date: 2026-04-30T06:58:48Z

A few days ago I was using Ollama models for some local work with Claude Code. I changed nothing. Today, the same models just hang indefinitely with an "are you working" prompt. Something clearly changed. I suspect they aren't testing these use cases very often.

---

### Issue #63024 — Add option to hide email address from welcome banner

State: OPEN | #63024
Labels: enhancement, area:tui

---



### Problem Statement

The Claude Code welcome banner displays the authenticated user's email address (e.g., `user@example.com's Organization`). There is no way to suppress or hide this.

This is a privacy concern when screen-sharing, live-streaming, recording demos, pair programming, or working in public spaces. The email is visible to anyone who can see your screen whenever you open a new Claude Code session.

### Proposed Solution

Add a configuration option to hide the email/org from the welcome banner. Either of these would work:

- An environment variable: `CLAUDE_CODE_HIDE_EMAIL=true`
- A `/config` setting: `privacy.hideEmailInBanner: true`

The banner would still show the model, effort level, and working directory — just not the account email.

### Alternative Solutions

- `CLAUDE_CODE_HIDE_CWD=true` hides the working directory but does not affect the email display.
- Switching to API key auth (`ANTHROPIC_API_KEY`) removes the email from the banner, but loses Claude Pro features and requires per-token billing — not a practical workaround for Pro subscribers.

### Priority

Low - Nice to have

### Feature Category

Configuration and settings

### Use Case Example

_No response_

### Additional Context

_No response_

# Comments on anthropics/claude-code#63024
Total: 0 comments

No comments on this issue.

---

### Issue #53862 — Interactive Bash tool hangs after successful execution; tool_result is not written to session/UI

State: OPEN | #53862
Labels: bug, platform:macos, area:bash, area:providers, stale


---

### Summary

In Claude Code interactive mode, every Bash tool call gets stuck at `Running...` / reports an internal error and never returns output to the UI. The same Bash commands work in non-interactive mode (`claude -p`). Debug logs show that the local Bash command is actually executed successfully (`tool_dispatch_end outcome=ok`), but the corresponding `tool_result` is never written back to the session JSONL or rendered in the interactive UI.

This looks like an interactive-mode tool-result handling / streaming / session-state bug rather than a shell startup failure.

### Environment

- Claude Code version: `2.1.119`
- OS: macOS / Darwin `25.3.0`
- Default shell: `/bin/zsh`
- Also reproduced after forcing Bash via Claude settings:
  - `SHELL=/bin/bash`
  - `CLAUDE_CODE_SHELL=/bin/bash`
  - `CLAUDE_BASH_NO_LOGIN=1`
- Claude Code is configured through a local proxy at `http://127.0.0.1:5000`.
- Provider format that works for normal requests: OpenAI-compatible chat/completions.

### What Works

Running Bash through non-interactive mode works and returns output, for example:

```bash
claude -p 'run pwd with Bash'
```

The command executes and returns normally.

### What Fails

In interactive mode:

```bash
claude
```

Then ask Claude Code to run any Bash command, for example:

```bash
pwd
```

The UI shows the Bash tool as running, but it never surfaces the command output and the conversation does not continue normally. In some cases Claude Code reports an internal error.

This happens for all Bash commands tested, including trivial commands such as `pwd`, `echo hi`, and `ls`.

### Debug Evidence

Using `--debug-file`, the debug log shows that the Bash tool is dispatched and completes successfully locally. The key observation is:

```text
tool_dispatch_start ... tool_name=Bash ...
tool_dispatch_end ... outcome=ok ...
```

So shell process creation and command execution appear to succeed.

However, after this successful `tool_dispatch_end outcome=ok`, the expected tool result is not persisted into the session JSONL file. The session file does not contain the corresponding `tool_result`, and the interactive UI remains stuck at `Running...` without displaying the Bash output.

### Things Already Tried

- Verified `claude -p` non-interactive mode works.
- Reproduced in interactive mode with `claude`.
- Reproduced with `claude --bare`.
- Reproduced in a clean temporary directory.
- Disabled MCP servers for the test.
- Forced Claude Code to use `/bin/bash` instead of zsh.
- Verified debug logs show `Using shell override: /bin/bash`.
- Reviewed shell startup files (`~/.zshrc`, `~/.zprofile`, etc.). No obvious non-interactive shell pollution was found; `~/.zshrc` has an interactive guard like `[[ $- != *i* ]] && return`.
- Disabled or adjusted several Claude Code environment flags related to prompt caching, telemetry/error reporting, experimental betas, background tasks, and fine-grained tool streaming. The issue persisted.
- Confirmed that switching the proxy to native Anthropic format is not viable in this environment because the upstream rejects some Claude Messages API fields such as `context_management`; the OpenAI-compatible format is required for normal requests.

### Expected Behavior

After the Bash subprocess completes successfully, Claude Code interactive mode should write a `tool_result` event to the session, render the Bash output in the UI, and continue the conversation.

### Actual Behavior

The Bash subprocess appears to complete successfully according to debug logs, but the tool result is lost before it reaches the interactive UI/session state. The UI remains stuck at `Running...` or eventually reports an internal error.

### Why I Think This Is a Claude Code Interactive-Mode Bug

The strongest signal is that `tool_dispatch_end outcome=ok` is present in the debug log, while the corresponding `tool_result` is missing from the session JSONL and the UI. This suggests the shell execution path itself is working, but the interactive-mode result propagation path is failing after successful tool execution.

This may be related to streaming/tool-result handling in interactive mode, especially when using an OpenAI-compatible proxy, but the failure point appears to be inside Claude Code after local Bash execution succeeds.

### Related Issues

Possibly related:

- https://github.com/anthropics/claude-code/issues/47138
- https://github.com/anthropics/claude-code/issues/41722

# Comments on anthropics/claude-code#53862
Total: 4 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-04-27T10:16:49Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/53783
2. https://github.com/anthropics/claude-code/issues/53328
3. https://github.com/anthropics/claude-code/issues/46767

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: 0xbrainkid
Date: 2026-04-27T10:40:46Z

This bug is subtle but important because it severs execution truth from user-visible truth.

If interactive Bash succeeds but then hangs before writing `tool_result` to the session/UI, the user is left with the worst possible state: the underlying action may already have happened, but the visible record suggests uncertainty or failure.

That makes it a state-legibility problem, not just a hang.

The consequences are messy:
- users may retry commands that already succeeded
- debugging becomes harder because the durable record is missing the decisive event
- trust drops because the tool boundary no longer tells the truth about what the system actually did

I would want this investigated around completion signaling:
1. does the subprocess finish and only the reporting path hang?
2. is the `tool_result` write blocked on PTY/flush behavior after command success?
3. can the UI distinguish “execution finished, reporting incomplete” from “execution still running”?

A system can recover from a failed command. It is much harder to recover from a command that succeeded while the interface failed to say so, because that breaks the operator’s model of the run itself.

--- Comment 3 ---
Author: cryptoya
Date: 2026-04-27T10:48:45Z

> This bug is subtle but important because it severs execution truth from user-visible truth.
> 
> If interactive Bash succeeds but then hangs before writing `tool_result` to the session/UI, the user is left with the worst possible state: the underlying action may already have happened, but the visible record suggests uncertainty or failure.
> 
> That makes it a state-legibility problem, not just a hang.
> 
> The consequences are messy:
> 
> * users may retry commands that already succeeded
> * debugging becomes harder because the durable record is missing the decisive event
> * trust drops because the tool boundary no longer tells the truth about what the system actually did
> 
> I would want this investigated around completion signaling:
> 
> 1. does the subprocess finish and only the reporting path hang?
> 2. is the `tool_result` write blocked on PTY/flush behavior after command success?
> 3. can the UI distinguish “execution finished, reporting incomplete” from “execution still running”?
> 
> A system can recover from a failed command. It is much harder to recover from a command that succeeded while the interface failed to say so, because that breaks the operator’s model of the run itself.

Thanks, this captures the risk very well.

I agree that the most important part is not just that the UI hangs, but that the execution boundary becomes ambiguous. From the debug logs, the subprocess appears to finish successfully (tool_dispatch_end outcome=ok), but the result does not make it into the durable session record or the UI.

That creates exactly the dangerous state you described: the command may already have mutated the system, while the operator has no reliable visible confirmation.

I think the key thing to investigate is the handoff after local tool completion:

1. Bash subprocess completes successfully.
2. Claude Code records tool_dispatch_end outcome=ok.
3. Somewhere between that point and writing/rendering tool_result, the interactive session stalls.

So the bug may be less about shell execution itself and more about completion propagation: result serialization, PTY/output flushing, stream handling, or session-state persistence. Even a fallback state like “command finished, but result reporting failed” would be much safer than leaving the UI in “still running”.

--- Comment 4 ---
Author: jonpepler
Date: 2026-05-11T23:37:46Z

Confirming on **macOS 26.4.1 / Claude Code 2.1.139 / zsh**. Same symptom (`tool_dispatch_end outcome=ok`, `tool_result` never reaches session/UI), but worth noting it's **intermittent and seemingly random in my case** — not every Bash call. Most run fine; a small unpredictable fraction get dropped. Frequency is low enough that a 2-day trace of ~140 wrapped calls captured zero hangs in the log, even though I've hit several in the same window via interactive use. No clear correlation with command length, runtime, output size, or command type — short greps drop just as often as long test runs.

Three additional data points from a debugging session today:

**1. `run_in_background: true` calls leave orphan polling shells alive indefinitely.** The harness spawns `zsh -c 'until [ -s <task>.output ]; do sleep N; done; cat <task>.output'` to wait on the backgrounded job's output. When the relay drops, that shell sits there forever — I just found three on a single frozen session, one **>26h elapsed**, all PIDs still in `ps`. From a *sibling* Claude Code session, writing into the empty `*.output` file causes the polling shell to exit cleanly (the `[ -s ]` test passes, `cat` runs, shell terminates). But the orphaned session still doesn't surface the injected message — consistent with the result-delivery drop being upstream of the shell exit.

**2. One polling variant has a self-match bug.** Some backgrounded calls poll on `until ! pgrep -af "<thing>"; do sleep N; done`, and the spawned shell's own argv contains `"<thing>"` verbatim, so pgrep matches itself and the negation is never true. That shell polls forever even when the target process exited days ago. Trivially fixed with a bracket character (`[<first-char>]rest`) in the poller generator.

**3. Remote-cancel from a sibling session is not viable.** Two attempts:
- `TIOCSTI` ioctl into the frozen Claude's `/dev/ttysNNN` to inject `\x03`: `PermissionError: Operation not permitted` on macOS 26 without sudo. (TIOCSTI has been progressively locked down on BSD/macOS for security.)
- External `kill -INT <claude-pid>`: kills the entire Claude process. The TUI is in raw mode, so in-app Ctrl+C is handled as a *keystroke* at the application layer, not a kernel signal — no signal-level cancel-tool path exists. Only physical Ctrl+C in the host terminal works.

Local workaround is wrapping every Bash call with `perl -e 'alarm shift; exec @ARGV' SECONDS …` + `run_in_background: true` + a `ScheduleWakeup`, so the model survives the drop. The shell really does finish in every traced case (no alarm-fired exits), confirming the bug is in the post-completion delivery path, not the shell itself.

---

### Issue #62270 — [FEATURE]  Streaming response hook for external voice and accessibility integrations

State: CLOSED | #62270
Labels: duplicate


---



### Problem Statement

Claude Code's only response exit point is the Stop hook, which fires after a full response completes. There is no way for an external tool to receive response tokens as they stream.

I built a browser-based voice interface for Claude Code: push-to-talk mic → transcript injected into active Claude Code session → Stop hook captures the completed response → browser speaks it back. The pipeline works, but every exchange takes 30-60 seconds of silence before the browser receives anything. The full response must finish before a single word exits.

For accessibility users who rely on voice as their primary input method, this latency makes Claude Code's local context -- its greatest strength -- effectively unusable in a voice workflow.

### Proposed Solution

A PostResponseChunk hook that fires as tokens are generated, delivering partial response text to an external process in real time.

Or a local SSE endpoint from the Claude Code process that external tools can subscribe to and receive streaming output.

Either would allow a browser, voice UI, or accessibility tool to display and speak Claude Code's response as it generates -- the same experience users currently get visually in the terminal.

### Alternative Solutions

I built the Stop hook workaround described above. It proves the pipeline is sound but the latency is architectural -- there is no way to make it faster without streaming output.

Other tools (OpenAI Realtime API, Gemini Live) solve this with voice-to-voice streaming at the model level. Claude Code cannot use that approach because it would lose local project context, file access, and tool calls -- the entire reason to use Claude Code over a raw API.

### Priority

Critical - Blocking my work

### Feature Category

Developer tools/SDK

### Use Case Example

USE CASE EXAMPLE:
1. Developer with a motor disability uses voice as their primary input method
2. They speak a question about their codebase into a browser interface
3. The transcript is injected into the active Claude Code session
4. Claude Code answers using full local project context, memory, and tools
5. With streaming: the browser begins speaking the response within 1-2 seconds
6. Without streaming: the browser waits 30-60 seconds in silence, then plays the full response at once

The difference between step 5 and step 6 is the difference between a usable tool and an unusable one.


### Additional Context

Existing issue #61574 asks for TTS readback inside Claude Code. This request is different -- it asks for an output hook so external tools can build their own integrations. The hook approach is more flexible: it enables voice UIs, live dashboards, remote displays, and any accessibility tool without Anthropic having to build each one.

# Comments on anthropics/claude-code#62270
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-25T16:44:51Z

Found 1 possible duplicate issue:

1. https://github.com/anthropics/claude-code/issues/60564

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: github-actions[bot]
Date: 2026-05-29T10:23:57Z

This issue has been automatically closed as a duplicate of #60564.

If this is incorrect, please re-open this issue or create a new one.

🤖 Generated with [Claude Code](https://claude.ai/code)

---

### Issue #63226 — [Bug] Anthropic API Error: thinking blocks corrupted during context compaction with extended thinking enabled

State: OPEN | #63226
Labels: bug, platform:macos, area:core


---

**Bug Description**
Title: 400 "thinking blocks cannot be modified" mid-conversation with no user-side trigger

  Description:

  Recurring 400 error mid-conversation with extended thinking enabled:

  API Error: 400 messages.3.content.1: `thinking` or `redacted_thinking` blocks
  in the latest assistant message cannot be modified. These blocks must remain
  as they were in the original response.

  First turn succeeds; the error appears on a later turn when a prior assistant message containing a thinking block is
  replayed. messages.3.content.1 points to a thinking block that was altered before being re-sent.

  Important: This happens during normal use with no user-side trigger — I did not interrupt a streaming response, did
  not queue/type a message while the assistant was responding, did not switch models, and did not use /rewind or edit
  any previous message. This points to internal history handling (likely context compaction or message replay)
  corrupting the thinking block rather than a user action.

  Environment:
  - Claude Code: 2.1.154 (native install, latest available)
  - Platform: macOS (Darwin 25.5.0), arm64
  - Shell: zsh
  - Model: Opus 4.8 (1M context), effortLevel: high
  - Hooks: one PreToolUse hook (matcher Bash) → rtk hook claude (ruled out — Bash-only, never touches messages)

  Workaround: /clear restores the session.

**Environment Info**
- Platform: darwin
- Terminal: Apple_Terminal
- Version: 2.1.154
- Feedback ID: 835f774d-11b2-4799-a94d-671158993161

**Errors**
```json
[]
```

# Comments on anthropics/claude-code#63226
Total: 1 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-28T17:26:48Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/63147
2. https://github.com/anthropics/claude-code/issues/63213
3. https://github.com/anthropics/claude-code/issues/10199

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

---

### Issue #54282 — [BUG] Cowork session transcript lost when interrupting (Esc) mid-stream then sending follow-up — Claude Desktop 1.4758.0.0 (MSIX)

State: OPEN | #54282
Labels: bug, platform:windows, area:cowork, data-loss, stale

---

## Summary

In Cowork mode, interrupting a streaming assistant response with **Esc** and then sending a short follow-up message silently wipes the entire prior conversation history. The session becomes unrecoverable: scrolling up shows nothing, restarting the app does not bring it back, and the on-disk JSONL transcript contains only system metadata (no user/assistant messages).

## Environment

- **Claude Desktop:** `1.4758.0.0` (MSIX install)
- **Package family:** `Claude_pzs8sxrjxfjjc`
- **Install path:** `C:\Program Files\WindowsApps\Claude_1.4758.0.0_x64__pzs8sxrjxfjjc\app\Claude.exe`
- **OS:** Windows 11
- **Mode:** Cowork

## Steps to reproduce

1. Start a Cowork session and exchange a few turns.
2. While the assistant is streaming a response, press **Esc** to interrupt.
3. Send a short follow-up message that does not repeat prior context (e.g. "make it shorter", "and also …").
4. The assistant replies as if it has no prior context.
5. Scroll up in the UI — the previous turns are gone.
6. Close and reopen Claude Desktop — the session is not in the resume list.

## Expected behavior

- The transcript should remain intact across an Esc interrupt + follow-up.
- The session should remain resumable from the UI after restart.
- Even if the runtime crashes mid-turn, content already streamed should be flushed to disk before the failure.

## Actual behavior

- UI loses all prior turns after the Esc + follow-up sequence.
- The session's on-disk JSONL transcript contains only system metadata (~983 bytes), no message content.
- The session does not appear in the resume list after restart.
- Tokens consumed for the lost turns are not recoverable.

## Investigation / on-disk state

Two orphaned Cowork sessions from the same time window were found on disk that do not appear in the runtime's session list:

| Session | Transcript | Notes |
|---|---|---|
| `local_307fcd79-bb64-475c-8b99-b733bbdad0b0` | none (only an MCP log of 2 KB) | Earliest, ~10:04 UTC |
| `local_313fe124-9a4d-4805-9470-f76dbf12a902` | `3fbce702-fd8c-4b11-89cd-d1f05cb52be8.jsonl`, **983 bytes** — system headers only, no messages | ~10:16 UTC, the actual lost conversation per user recall |

Locations (under MSIX redirection):

```
%LOCALAPPDATA%\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\local-agent-mode-sessions\
  <workspace-id>\<account-id>\local_313fe124-…\.claude\projects\…-outputs\
  3fbce702-fd8c-4b11-89cd-d1f05cb52be8.jsonl
```

This suggests the runtime does not flush the transcript to disk until after the first complete turn, **and** the Esc + follow-up code path drops the in-memory turn before persisting it. The session ID is also lost from the resume index.

## Possibly related issues

- #53067 — `onSessionRestored` is `undefined` when `XJ7({ enabled: false })` is invoked; resume crashes with `FKH is not a function`.
- #53044 / #53121 / #53284 / #53568 — same family of `UKH/FKH is not a function` errors on `claude --resume` in CLI 2.1.120.

The Claude Desktop runtime appears to share the underlying claude-cli-nodejs code path (cache directory `LocalCache\Local\claude-cli-nodejs\Cache\…` is present). If the same hook returns `undefined` here, an exception during resume / mid-turn could silently drop the in-memory session before it is written to disk.

## Impact

Conversation is lost mid-task. Tokens are billed, no usable result, and the session cannot be reconstructed. Users have to manually start over.

## Workaround (current)

- Avoid pressing Esc during a streaming response.
- For long / important conversations, periodically copy the chat into a local file as a backup.

## Asks

- Persist transcripts on every turn boundary (or sooner — at least on every assistant token chunk's end-of-stream).
- Make the resume index repair itself by scanning `local-agent-mode-sessions\` on startup so that on-disk sessions cannot become unreachable from the UI.
- Guard the `onSessionRestored` call site (`FKH?.(K)`) per the fix already discussed in #53067.

# Comments on anthropics/claude-code#54282
Total: 0 comments

No comments on this issue.

---

### Issue #59474 — Ctrl+C does not copy selected text in Claude desktop app — always interpreted as 'stop generating'

State: OPEN | #59474
Labels: invalid


---

# Ctrl+C does not copy selected text in Claude desktop app — always interpreted as "stop generating"

## Environment
- **App:** Claude desktop (Windows, MSIX install from Microsoft Store)
- **Version:** 1.7196.0.0
- **Install path:** `C:\Program Files\WindowsApps\Claude_1.7196.0.0_x64__pzs8sxrjxfjjc\app\Claude.exe`
- **OS:** Windows 11 Pro 10.0.26200

## Steps to reproduce
1. Open a conversation that has at least one response from Claude.
2. Click-and-drag to highlight a span of text inside a message bubble (assistant or user).
3. With the selection still visible, press **Ctrl+C**.

## Expected behavior
The selected text is copied to the system clipboard. This is the universal Windows convention used by browsers, IDEs, File Explorer, Notepad, and — most relevantly — Windows Terminal, which adopted the convention "Ctrl+C copies if a selection exists, otherwise it sends interrupt."

## Actual behavior
Ctrl+C is captured by the app as "stop generating" (or silently swallowed when no generation is active). The clipboard is not updated. The only ways to copy are:
- **Right-click → Copy** on the selection
- The hover-revealed Copy button on a message bubble, which copies the *entire* message rather than the selected span

## Suggested fix
When the focused element has a non-empty text selection, defer to the standard clipboard path (`document.execCommand("copy")` or the Clipboard API) instead of routing Ctrl+C to the interrupt handler. Otherwise, fall through to the existing "stop generating" behavior. This mirrors Windows Terminal's `copyOnSelect`/`Ctrl+C` resolution and matches user expectation from every other Windows app.

## Impact
Copying snippets — code, command names, URLs, extension names — out of Claude's responses is a many-times-per-session operation. The current binding forces users to switch to mouse-based copying for what is otherwise muscle-memory keyboard work, and the whole-message Copy button can't substitute when only a partial selection is wanted.

## Notes
- Reproduces on a fresh window with no in-flight generation, so it isn't only the "interrupt during stream" case.
- The Ctrl+Shift+C and Ctrl+Insert paths also do not copy (worth confirming during triage).

# Comments on anthropics/claude-code#59474
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-15T17:39:59Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/56298
2. https://github.com/anthropics/claude-code/issues/58304
3. https://github.com/anthropics/claude-code/issues/53975

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: bachseans
Date: 2026-05-15T18:02:00Z

**Update from the reporter:**

After more testing, the bug is **intermittent**, not absolute as my original write-up implied. Ctrl+C *does* copy selected text correctly under some conditions in the Claude desktop app — my original report was based on a strong but incomplete sample of failures during a single session.

I want to flag a few things and ask that the `invalid` label be reconsidered:

### Why I believe there is still a real bug, even if it's not "Ctrl+C never copies"

1. **The failure mode is reproducible enough to be observed multiple times in a single session.** I encountered it repeatedly today during a long-running conversation — selected text from message bubbles, pressed Ctrl+C, and the clipboard contents were not what I selected. The right-click → Copy fallback worked. The hover-revealed "Copy message" button worked. Only Ctrl+C on a selection misfired.
2. **There are at least three other open issues describing related Ctrl+C / copy misbehavior on the Windows desktop app:** #56298 (Ctrl+C copies empty string), #53975 (Ctrl+C on partial selection copies entire message), and the now-closed predecessor work going back further. Whatever the precise root cause, "copying from Claude on Windows desktop is fragile" is clearly an established cluster.
3. **The `invalid` label appears to have been applied automatically and quickly,** as it was on my earlier #43211 (about the taskbar icon) — which closed silently without a maintainer ever commenting, and the bug it described is still present and now re-filed as #59477. I'd like to avoid the same outcome here.

### Suspected trigger I'm narrowing toward

My current best guess is that Ctrl+C is being captured as "interrupt generation" while a response is actively streaming, and only falls through to standard "copy selection" once generation completes — the same overloaded-key pattern Windows Terminal solved with the `copyOnSelect`/selection-aware-Ctrl+C resolution. That would explain why the failure was concentrated during a session with long streaming responses and why it appears to work in calmer states.

I'll post confirmed reproduction steps once I've narrowed this down. **In the meantime, please don't auto-close as `invalid`** — the bug is real and falls within at least two of the related open issues' scope; the question is just which one this report should be merged into.

### Suggested next steps for triage

- Either reopen with the `area:desktop` / `platform:windows` / `bug` labels and let it sit until I post the narrower repro, OR
- Merge this report into #56298 or #53975 (whichever the maintainers consider the canonical cluster), and I'll add my session evidence as a comment there.

Silent re-close under `invalid` is the outcome I'm trying to head off.

---

### Issue #53674 — [BUG] ESC interrupt removes the user's submitted prompt from chat history

State: OPEN | #53674
Labels: bug, has repro, platform:macos, area:tui, regression, stale

---



### What's Wrong?

Pressing ESC to interrupt a streaming response now removes the user's submitted message entirely from the chat transcript — both the prompt and Claude's partial response disappear, as if the turn never happened.
                                                                                                                                                                 
Previously, ESC stopped generation but left the user prompt in the transcript. This enabled a common workflow:                                                 
  1. Submit a prompt.                                                                                                                                            
  2. Watch Claude start working and realize I want to add context, redirect, or refine.
  3. Press ESC.                                                                                                                                                  
  4. Type a follow-up like "actually, also include Y" — Claude still has the original prompt in context and can continue from there.
                                                                                                                                                                 
With the new behavior, the original prompt is gone from history, so any follow-up has nothing to attach to. I have to retype the full original prompt plus the augmentation from scratch, every time. The augmentation pattern is what makes ESC useful in the first place; without it, ESC is just "abort and start over."   This is a serious hit to productivity.                                                                                         

NOTES                                                                                                                                                          
  - I am not using Vim mode (no editorMode: "vim" in any settings.json file).                                                                                    
  - The v2.1.119 changelog mentions "Vim mode: Esc in INSERT no longer pulls queued messages back into input", which suggested a Vim-only scope — but the transcript-clearing behavior I'm seeing affects non-Vim users.                                                                                                 
  - Ctrl+S (chat:stash) doesn't help because it only stashes drafts before submission. The decision to interrupt is made after I see Claude's first sentences.

REQUEST                                                                                    
Restore the prior behavior in non-Vim-mode (keep the user's prompt in the transcript on ESC interrupt), or add a setting like preserveInterruptedTurnInHistory:true to opt back in.
                                                                                                                                                                 
Affected version: 2.1.119+                                
Platform: macOS (zsh, Darwin 24.6.0)

### What Should Happen?

When ESC is pressed to interrupt a streaming response, my submitted prompt should remain in the chat transcript (along with whatever partial response Claude produced before the interrupt). This preserves the conversation context so I can send a follow-up message that augments or redirects the original ask without retyping it.
                                                                                                                                                                 
Old behavior (pre-2.1.119): prompt + partial response stayed in history; follow-ups could reference them.                                                      

New behavior: the entire turn is wiped on ESC — both my prompt and Claude's partial output disappear from the transcript.

### Error Messages/Logs

```shell
N/A — no error output. This is a behavioral regression, not a crash or error.
```

### Steps to Reproduce

1. Open Claude Code in any project (Vim mode off; confirmed via editorMode not set in any settings.json).
2. Submit a non-trivial prompt, e.g., "Explain in detail how the Linux scheduler works."                                                                       
3. Wait for Claude to begin streaming the response.                                                                                                            
4. Press ESC to interrupt mid-stream.                                                                                                                          
5. Observed: the submitted prompt and the partial response are both removed from the chat transcript. The conversation looks as if the turn never happened.    
6. Expected: the submitted prompt remains in the transcript; partial response is preserved (or at least cleanly truncated and visible); a subsequent message like "also include kernel preemption" has full context to attach to.                                                                                           
                                                                                                     
Reproduces consistently in VS Code integrated terminal on macOS. Not tested in other terminals.  

### Claude Model

Opus

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

_No response_

### Claude Code Version

2.1.120

### Platform

Anthropic API

### Operating System

macOS

### Terminal/Shell

VS Code integrated terminal

### Additional Information

_No response_

# Comments on anthropics/claude-code#53674
Total: 0 comments

No comments on this issue.

---

### Issue #53857 — TUI leaks repeated fragments of current screen into terminal scrollback during a session, with rendering artifacts

State: OPEN | #53857
Labels: duplicate, platform:macos, area:tui, stale


---

### Description

During an active Claude Code session, the host terminal's scrollback is being polluted with many repeated fragments of the currently visible TUI screen, sometimes accompanied by visual artifacts (stray escape sequences, broken box-drawing characters, partial lines).

The TUI itself renders correctly on the alternate screen, but as the session progresses the terminal's main-buffer scrollback accumulates dozens of near-duplicate snapshots of the last redraw, so scrolling up at any point during the session shows a long trail of repeated UI fragments instead of a clean transcript.

Expected: either the alternate screen buffer fully contains the TUI and nothing leaks into scrollback, or only a clean linear transcript (user input + assistant output) is appended.

### Steps to reproduce

1. Run `claude` in iTerm2 on macOS.
2. Use the session normally — type prompts, let assistant stream output, run tool calls so the status line updates.
3. While still in the session, scroll up in the terminal.
4. The scrollback contains many repeated fragments of the last visible screen, with occasional artifact characters interspersed.

### Environment

- Claude Code: 2.1.119
- Terminal: iTerm2 3.6.10
- TERM: xterm-256color
- OS: macOS 15.7.5 (24G624)

### Notes

Related but distinct from #1913 (in-session flickering) and #42258 (Windows Terminal streaming) — here the in-session rendering looks fine, the problem is that frequent redraws are leaking into the main-buffer scrollback rather than staying confined to the alternate screen.

# Comments on anthropics/claude-code#53857
Total: 4 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-04-27T10:02:10Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/52825
2. https://github.com/anthropics/claude-code/issues/51418
3. https://github.com/anthropics/claude-code/issues/52547

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: 0xbrainkid
Date: 2026-04-27T10:10:46Z

This is more than a rendering annoyance. If the TUI leaks repeated fragments of the current screen into scrollback, it can corrupt the user’s understanding of what actually happened in the session.

That makes it a record-integrity issue.

Terminal scrollback is often treated as the fallback evidence trail when users are debugging behavior, auditing actions, or reconstructing a run after something went wrong. If the scrollback contains duplicated or artifacted fragments that were never really discrete steps, then the transcript stops being dependable as evidence.

The risks stack up fast:
- users may misread artifacted fragments as genuine model outputs
- debugging becomes harder because the visible trail is no longer faithful to execution order
- trust drops because the interface is manufacturing ambiguity inside the one place people expect a durable record

I would want to know:
1. whether the leaked fragments are display-only artifacts or also present in persisted session state
2. whether tool output boundaries make the leak worse
3. whether the corruption changes when screen repaints happen during streaming / resize / focus changes

A system can survive ugly rendering. It is much harder to survive a user deciding the visible record is no longer trustworthy.

--- Comment 3 ---
Author: vossiman
Date: 2026-05-12T09:52:33Z

Confirming this bug class with a clean version bisect in a DevPod-managed devcontainer + tmux environment. Symptom shape is a bit different from the iTerm2/macOS report so adding the data here rather than filing fresh.

**Bisect (single environment, only the `claude` binary changes between runs):**

| Version | Scrollback state |
|---|---|
| 2.1.133 | Mild artifacts — pre-existing, low-frequency |
| 2.1.136 | **Severity jump — scrollback constantly poisoned** |
| 2.1.139 | Identical to 2.1.136. None of 2.1.139's three scrollback fixes touch this path. |

**Symptom:** When the assistant streams an indented line like `  Fixing it now`, the live tmux pane renders the 2-space indent correctly. After the line scrolls off into tmux scrollback, the text drifts **left by 2 columns** (indent gone) AND the first ~2 characters of the line (`Fi`) appear smeared into cells across **other rows that should be blank** — consistent with the renderer using cursor-forward to skip the indentation cells, and tmux's scrollback capturing earlier intermediate states from streaming partial-redraws on those rows.

**TERM workaround does NOT help on 2.1.139.** Tested `TERM=xterm-256color` in place of `tmux-256color`; same severe poisoning. So the regression path isn't gated on terminal-capability advertisement.

**Workaround that DOES fix it on 2.1.139:** `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1 claude` — scrollback is clean. This localizes the bug precisely to the **alt-screen render path's partial-redraw logic**: in transcript-style (main-buffer) mode, claude is forced to emit literal characters for indentation rather than CUF-skipping cells, and the artifact disappears. Same fix does NOT work via `CLAUDE_CODE_NATIVE_CURSOR={0,1}` or `CLAUDE_CODE_DISABLE_VIRTUAL_SCROLL=1`.

**Suspected commit window** — three 2.1.136 changelog entries touch exactly this code path:
- "Fixed a stray leading space on the second line of wrapped text at the column boundary"
- "Fixed colors appearing at wrong positions in bash command output and markdown code blocks"
- "Fixed wide markdown tables leaving a stale bordered render in terminal scrollback while streaming"

Also worth noting: env-var diff between 2.1.133 and 2.1.138 introduced `CLAUDE_CODE_NATIVE_CURSOR`, a new toggle in exactly this window whose name suggests it controls whether the renderer manages its own cursor or relies on the terminal's native cursor advance — i.e. exactly the mechanism that would produce un-cleared indentation cells. (Toggling it on 2.1.139 did not fix the symptom, but the name + timing are suggestive of where to look.)

**Environment:**
- Claude Code: 2.1.139 (also reproduced on 2.1.136; comparison baseline 2.1.133)
- tmux: 3.5a
- TERM: `tmux-256color` (also tested `xterm-256color` on 2.1.139 — same result)
- COLORTERM: unset
- Host: DevPod-managed devcontainer (Ubuntu, remote container over SSH)
- Shell: bash

**Workaround in use now:** 2.1.139 + `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1`. Keeps the new features; trade-off is the TUI runs in transcript mode (no fullscreen overlays, no in-app scrollback navigation, spinners leave trails). Strongly preferable to pinning 2.1.133 in our case.

--- Comment 4 ---
Author: mieubrisse
Date: 2026-05-12T23:07:10Z

Super, super annoying:

<img width="1917" height="994" alt="Image" src="https://github.com/user-attachments/assets/523bf422-af77-4382-961b-b7769844189a" />

---

### Issue #59202 — [BUG] VS Code webview stuck on "Thinking" — sessionID discarded on restore (v2.1.141, regression of #35004)

State: OPEN | #59202
Labels: bug, has repro, platform:windows, area:ide, platform:vscode, regression


---



### What's Wrong?

In the Claude Code VS Code extension's webview chat panel, after sending a message the UI sometimes gets stuck on the "Thinking" indicator indefinitely — the streaming UI never transitions to showing the response, even though the response is generated normally on the backend. **This is happening to me during ordinary use of the extension, not in any contrived setup.** I have hit it organically multiple times; I was not reloading the window, restarting the extension, or doing anything unusual. The first couple of times I assumed the response was just slow, but it never arrived and the "Thinking" indicator stayed forever.

Closing the conversation tab and reopening it from the sessions list reveals the full response on disk: the CLI completed normally and the assistant turn was persisted to `~/.claude/projects/<encoded-cwd>/<sessionId>.jsonl`, but the live webview UI never received the streaming updates and stayed on "Thinking". Only the **webview-to-extension binding** is broken; nothing else fails.

> **Workaround:** Close the conversation tab and reopen it from the sessions list. Your reply MAY be there with no data loss. I've seen it end up with the session stuck forever (unrecoverable), and I've seen the session with all of the data and able to continue working.

The exact natural trigger isn't pinpointed — it's some webview-lifecycle event during or after streaming (visibility change, focus change, panel layout shift, or similar). Investigation of the bundled `extension.js` shows two specific call sites where the saved sessionID is discarded (`U.setupPanel(w, void 0, void 0, I)` in `deserializeWebviewPanel`, and `this.getHtmlForWebview(z.webview, void 0, void 0, !0)` in `resolveWebviewView`) — see Additional Information. Any lifecycle event that re-runs either of those handlers will leave the new webview with `sessionId === undefined` and unable to subscribe to the in-flight session.

This matches the long-running cluster around closed/locked issues #35004, #42504, and #35022 — the same minified `void 0` argument-discard pattern documented there is present in v2.1.141 (and v2.1.140). It is **distinct** from open issue #45729 — see "Why this is NOT #45729" in Additional Information.

### What Should Happen?

After the webview is re-deserialized (panel-tab restore) or re-resolved (sidebar view-provider lifecycle), it should restore its session binding from the saved state (or Memento / `workspaceState`) and continue subscribing to the in-flight session, rather than initializing with `sessionId === undefined` and orphaning the conversation.

### Error Messages/Logs

```shell
Live capture from a controlled reproduction on Windows 11, v2.1.141 win32-x64.
Trigger sequence: open Claude Code panel webview, send a long-form prompt
("Generate a 1500-word essay on the lifecycle of honeybees..."), wait for
"Thinking" indicator to appear, then Command Palette -> "Developer: Reload
Window". After reload, the restored panel sits on "Thinking" indefinitely.

Extension Output log
(%APPDATA%/Code/logs/<timestamp>/window1/exthost/Anthropic.claude-code/Claude VSCode.log):

- Around the post-reload activation window, "Getting authentication status"
  and "OAuth tokens found in secure storage" each fire FOUR times within
  ~700 ms. Consistent with the "case init" handler in extension.js running
  for four webview surfaces on reload: claudeVSCodeSidebar primary, the
  secondary-sidebar provider, claudeVSCodeSessionsList, and the
  claudeVSCodePanel restore. So init succeeded on the extension side.
- After this burst, the file received no further entries despite the
  webview UI remaining stuck on "Thinking" for minutes afterward.
  The webview <-> extension message channel is dead while the extension
  host itself is alive.

Renderer log (same logs root, /window1/renderer.log) and VS Code's own
Developer Tools (Help -> Toggle Developer Tools) console:

- "Extension host (LocalProcess pid: 7900) is unresponsive." appears
  twice during the test window.
- "Extension host (LocalProcess pid: 7900) is responsive." appears
  twice; each unresponsiveness window resolves.
- VS Code's UNRESPONSIVE-host profiler attributes both windows to
  amazonwebservices.aws-toolkit-vscode (one example:
  "amazonwebservices.aws-toolkit-vscode took 78.13% of 1366.638ms"),
  NOT to anthropic.claude-code. Claude Code's extension host stays
  healthy throughout the hang. This is the diagnostic shape that
  distinguishes the bug from #45729, where the extension host itself
  becomes unresponsive after Claude Code's init handler stalls.

Session JSONL on disk
(~/.claude/projects/<encoded-cwd>/<sessionId>.jsonl):

- Contains the user prompt entry at the time the message was sent,
  plus the deferred-tool listing and skill-listing attachments that
  Claude Code persists at session start.
- In this controlled reproduction, the JSONL does NOT contain a
  completed assistant response, because "Developer: Reload Window"
  terminates the extension host process and that termination
  cascades to the CLI subprocess mid-stream. Under natural triggers
  (the originally-experienced version of this bug, where a webview
  lifecycle event destroys and recreates the webview without
  killing the host), the CLI continues running and the JSONL is
  fully populated by the time the user reopens the conversation
  tab. The Ctrl+R reproduction is a stronger version of the same
  underlying sessionID-discard defect; it also kills the CLI as
  a side effect, but the webview's "stuck on Thinking" symptom is
  identical in both cases.

Webview-side DevTools console (Developer: Open Webview Developer Tools)
was not captured for this report. Happy to capture and attach if helpful.
```

### Steps to Reproduce

**Naturally-occurring repro (how I actually hit this):**

1. Open VS Code with the Claude Code extension installed (v2.1.141 on `win32-x64`).
2. Open Claude Code in panel webview mode (defaults: `claudeCode.preferredLocation: "panel"`, `claudeCode.useTerminal: false`).
3. Use Claude Code normally. Send prompts. Read responses.
4. At some point, after sending a message, the "Thinking" indicator appears and never goes away. I have not pinpointed the exact trigger — I may have briefly changed focus to another editor, changed the panel layout, or otherwise caused a webview re-render during streaming. Nothing unusual. I have hit this organically more than once before investigating.
5. Closing and reopening the conversation tab from the sessions list reveals the full response that the CLI generated and persisted to disk while the webview was stuck — confirming the disconnect is purely on the webview-to-extension binding.

The natural trigger is intermittent because it requires the webview to re-render *during* a streaming response, which is a small window. Once a webview lifecycle event fires in that window, the new webview is constructed with `sessionId === undefined` (see Root Cause in Additional Information) and cannot subscribe back to the still-running CLI session.

**Deterministic forcing function (for verification by a maintainer):**

If the natural occurrence is hard to catch live, the following sequence reliably reproduces the same symptom by deliberately re-running `deserializeWebviewPanel` while a response is in flight:

1. Steps 1–3 above.
2. Send a prompt that streams for ~10 seconds, e.g. "Generate a 1500-word essay on the lifecycle of honeybees, from egg through queen succession, including the role of pheromones. Write the full essay; do not summarize or outline first."
3. While the "Thinking" indicator is visible, open the Command Palette (`Ctrl+Shift+P`) and run `Developer: Reload Window`.
4. After the reload, the restored Claude Code panel re-renders with the "Thinking" indicator still visible and stays stuck on it indefinitely.

This forcing-function repro is a *stronger* version of the same defect: `Developer: Reload Window` also terminates the extension host process and therefore the CLI subprocess, so in this case the response is not persisted to disk before the hang. The webview's "stuck on Thinking" symptom and underlying sessionID-discard code path are identical to the natural-trigger case; only the CLI lifecycle differs.

### Claude Model

None

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

2.1.83

### Claude Code Version

2.1.141 (Claude Code)

### Platform

Anthropic API

### Operating System

Windows

### Terminal/Shell

Other

### Additional Information

#### Root cause — call-site evidence in v2.1.141 `extension.js`

The bug is at the **call sites** in `deserializeWebviewPanel` and `resolveWebviewView`. `setupPanel`'s method definition itself is fine.

`extension.js` v2.1.141, SHA256 `23F19A6044439E67C5F2532C3FD02BB63397EE7835040A51BA114474367ABD1E`, 2,158,607 bytes.

**Bad call site #1 — panel-tab restore (line 882 of `extension.js`):**

```js
window.registerWebviewPanelSerializer("claudeVSCodePanel", {
  async deserializeWebviewPanel(w, R) {
    let v = R, I;
    if (typeof v?.isFullEditor === "boolean") I = v.isFullEditor;
    else I = window.tabGroups.all.findIndex((_) => _.viewColumn === w.viewColumn) === 0;
    U.setupPanel(w, void 0, void 0, I)   // v?.sessionID is discarded
  }
})
```

The saved-state object `R` is bound to `v`, its `isFullEditor` field is extracted correctly, but `v?.sessionID` is **never passed** to `setupPanel`. Variable-name map for v2.1.141: `U` is the manager class, `w` is the panel, `R` (= `v`) is the saved state, `I` is `isFullEditor`. Identical bug shape to #35004's version-by-version table, just with the v2.1.141 minifier-name rotation.

Suggested fix:

```js
U.setupPanel(w, v?.sessionID, void 0, I)
```

**Bad call site #2 — sidebar view provider (line 822 of `extension.js`, inside `U.resolveWebviewView(z, K, N)`):**

```js
resolveWebviewView(z, K, N) {
  let V = { isVisible: () => z.visible };
  this.webviews.add(V);
  z.webview.options = { enableScripts: !0, localResourceRoots: [...] };
  z.webview.html = this.getHtmlForWebview(z.webview, void 0, void 0, !0)   // sessionID and initialPrompt = void 0
  // ... constructs new m8(this.context, ..., void 0, ...) — that void 0 is `panelTab`, intentionally empty for sidebar
}
```

`WebviewViewProvider.resolveWebviewView` does not receive a saved-state argument like `deserializeWebviewPanel` does. The persisted sessionID could be retrieved from `this.context.workspaceState` / `globalState` / a Memento — but the current implementation reads no such state, so the sidebar webview always opens with `sessionId === undefined`.

(Note: the `new m8(..., void 0, ...)` in this same body is **not** a bug. Tracing `class m8 extends Pb` shows arg 15 is `panelTab` — legitimately empty for a sidebar webview that has no associated panel. Earlier #42504 commentary that called this slot `initialSessionId` was incorrect for v2.1.141's class shape.)

**Good call site for contrast — `createPanel` (same line 822, ~5–6 KB earlier in the minified line):**

```js
let B = window.createWebviewPanel("claudeVSCodePanel", "Claude Code", x, { ... });
let O = N === ViewColumn.Active;
this.setupPanel(B, z, K, O)   // real sessionID `z` passed correctly from createPanel's args
```

The `setupPanel` method definition itself (line 822 of `extension.js`):

```js
setupPanel(z, K, N, V) {
  // z = panel, K = sessionID, N = initialPrompt, V = isFullEditor
  // ...
  z.webview.html = this.getHtmlForWebview(z.webview, K, N, !1, V);   // K propagated correctly
  let H = new m8(this.context, O, this.settings, z.webview, ..., z, ..., !!V, ...);
  // ...
}
```

`setupPanel` itself correctly propagates `K` (sessionID) into `getHtmlForWebview` and into the `new m8(...)` communicator. The bug is purely at the two call sites above where `void 0` is passed instead of the saved sessionID.

#### Version map (abridged — full history in #35004)

| Version | `setupPanel` call inside `deserializeWebviewPanel` | State |
|---|---|---|
| v2.1.87 (per #35004) | `Z.setupPanel(A, void 0, void 0, v)` | Broken |
| v2.1.89 (per #42504) | regressed, same shape | Broken |
| v2.1.140 (this install) | minifier shape: `?.setupPanel(F, void 0, void 0, I)` | Broken |
| **v2.1.141 (this install)** | `U.setupPanel(w, void 0, void 0, I)` | **Broken** |

Variable names rotate with each minifier run; the bug shape is identical across versions. The full progression from v2.1.74 onward is documented in #35004's comment thread.

#### Why this is NOT #45729

#45729 reports a different hang in the same general extension. That bug's hang is in the `init` request handler (line 282 of `extension.js`):

```js
case "init": {
  let N = this.getAuthStatus(),
      V = z.channelId ? this.channels.get(z.channelId) : void 0;
  if (this.cachedCurrentRepo === void 0) {
    let B = await this.teleportService.detectCurrentRepository();   // can block indefinitely
    if (B) { ... }
  }
  // ...
  return { type: "init_response", state: { ... } }
}
```

If `teleportService.detectCurrentRepository()` hangs (git command stalls, network probe times out, WSL pipe hangs), the init response never returns. The webview sits forever waiting; the extension host gets marked unresponsive shortly after. That fits #45729's described symptom — *blank webview, no further log lines after the init message arrives, host eventually marked unresponsive — before any conversation is possible*.

This bug is different: init **succeeds** (a conversation is established, a message is sent, a response is generated and persisted). The hang fires later, when a webview lifecycle event re-deserializes the panel or re-resolves the sidebar view without restoring the session binding. The two code paths do not overlap.

Aside: the "AuthManager initialized" log appearing twice in #45729's broken trace is **not** a bug signal. Tracing the three `new K2(...)` construction sites in v2.1.141 (`K2` is the AuthManager class; the log line is in its constructor) shows that the manager class plus the first `m8` communicator each construct one K2 on activation. Two AuthManager-initialized lines is the steady-state baseline for a sidebar-only setup, three for a setup with both sidebar and a restored panel tab. It's not a defect.

#### Related cluster

- **#35004** — analytical anchor; version-by-version variable-name table from v2.1.74 through v2.1.87 (closed/locked).
- **#42504** — v2.1.89 regression report with video evidence; first to identify that both `deserializeWebviewPanel` and `resolveWebviewView` paths are affected (closed/locked).
- **#35022** — Windows variant on v2.1.76; same root-cause family (closed/locked).
- **#55453** — Cursor-specific renderer-hang variant; related-but-distinct (open).
- **#45729** — distinct root cause (`teleportService.detectCurrentRepository()` hang inside the init handler); see section above (open).
- **Excluded as different root causes:** #56200 (`onWillSaveTextDocument` settings-write hang, dup of #45729), #20960 (`~/.claude/projects/` `.jsonl` accumulation → OOM at startup), #59090 (separate UI defect: thinking-process expander not clickable).

#### Environment

| Component | Value |
|---|---|
| OS | Windows 11 Pro 25H2 (OS build 26200.8457, UBR 8457) |
| VS Code | 1.120.0, commit `0958016b2af9f09bb4257e0df4a95e2f90590f9f`, x64 |
| Node | v24.6.0 |
| Claude CLI | 2.1.141 |
| PowerShell | 7.6.1 |
| Extension | `anthropic.claude-code` v2.1.141, target platform `win32-x64` |
| `claudeCode.useTerminal` | not set (default `false` → webview is in use) |
| `claudeCode.preferredLocation` | `"panel"` |
| `claudeCode.allowDangerouslySkipPermissions` | `true` |
| `claudeCode.initialPermissionMode` | `"bypassPermissions"` |

**Binary hashes (to pin the bundle a maintainer is looking at):**

| File | Size (bytes) | SHA256 |
|---|---|---|
| `extension.js` (v2.1.141) | 2,158,607 | `23F19A6044439E67C5F2532C3FD02BB63397EE7835040A51BA114474367ABD1E` |
| `webview/index.js` (v2.1.141) | 4,798,391 | `D756D1D369CFB41AD0EC620506C7C7E11B2FBF4528516B62E0375A5E658E3B13` |
| `webview/index.css` (v2.1.141) | 374,037 | `E186CBA6F0E68E839C177ECE0879864531A536AED63AF5537BB753ECEBAA5F7D` |
| `extension.js` (v2.1.140) | 2,154,411 | `2D82CDC5F638B42EE8FF2F3365F9AAFB3FA94FAA47C00E33C18D30FC6332E146` |

#### Attached files

- **`vscode-console-log.txt`** — Renderer-process DevTools console capture (`Help → Toggle Developer Tools` → Console tab), saved during the controlled reproduction. Contains the `Extension host (LocalProcess pid: 7900) is unresponsive.` and `is responsive.` markers, and VS Code's UNRESPONSIVE-host profiler attributing both unresponsiveness windows to `amazonwebservices.aws-toolkit-vscode` (one entry: `took 78.13% of 1366.638ms`) — not to `anthropic.claude-code`. This is the distinguishing signal from #45729: Claude Code's extension host stays healthy throughout the hang.
- **`live-hang-claude-vscode-log-500.txt`** — Last 500 lines of the Claude Code extension Output channel log (`%APPDATA%/Code/logs/<timestamp>/window1/exthost/Anthropic.claude-code/Claude VSCode.log`) from the same reproduction. Shows four `Getting authentication status` / `OAuth tokens found in secure storage` pairs in quick succession during the post-reload activation window (init handlers running for all four webview surfaces — sidebar primary, sidebar secondary, sessions list, restored panel tab), then complete silence in the channel for minutes while the webview UI remains stuck on "Thinking". Confirms the webview ↔ extension message channel is dead even though the extension host itself remains alive.

[vscode-console-log.txt](https://github.com/user-attachments/files/27775573/vscode-console-log.txt)

[live-hang-claude-vscode-log-500.txt](https://github.com/user-attachments/files/27775578/live-hang-claude-vscode-log-500.txt)

# Comments on anthropics/claude-code#59202
Total: 3 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-14T20:24:50Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/35004
2. https://github.com/anthropics/claude-code/issues/35022
3. https://github.com/anthropics/claude-code/issues/42504

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: MorganStair
Date: 2026-05-14T20:26:03Z

> Found 3 possible duplicate issues:
> 
> 1. [[BUG] deserializeWebviewPanel discards saved session ID — panel tabs always open blank on restart #35004](https://github.com/anthropics/claude-code/issues/35004)
> 2. [[BUG] VSCode: deserializeWebviewPanel ignores saved sessionId — tabs show wrong conversation content after restart #35022](https://github.com/anthropics/claude-code/issues/35022)
> 3. [Claude Code responses disappear immediately after streaming completes in VS Code extension #42504](https://github.com/anthropics/claude-code/issues/42504)
> 
> This issue will be automatically closed as a duplicate in 3 days.
> 
> * If your issue is a duplicate, please close it and 👍 the existing issue instead
> * To prevent auto-closure, add a comment or 👎 this comment
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)

I already ruled all of those out. See the body of this issue.

--- Comment 3 ---
Author: MorganStair
Date: 2026-05-29T17:12:52Z

I'm not using vscode on windows at the moment, so you can close this if you like... although reproduction steps here are very easy to follow, *and* they include a trick to force the bug to surface reliably. If I don't see any activity on this, I'll close it since it's not exactly a show stopper.

---

### Issue #53882 — [BUG] "Add to context" duplicates selected text multiple times in input box

State: OPEN | #53882
Labels: bug, platform:windows, area:ide, platform:vscode, stale


---



### What's Wrong?

When selecting text in a Claude Code response and using "Add to context" (or "Attach selection as context"), the selected text is inserted into the input box **multiple times** instead of once. Each subsequent selection adds to the duplication, creating compounding bloat that has to be manually deleted before sending.

<img width="845" height="655" alt="Image" src="https://github.com/user-attachments/assets/e8eb7684-64ca-4c0f-9d00-38912d6d20c5" />
<img width="1863" height="358" alt="Image" src="https://github.com/user-attachments/assets/c095577c-afa7-4a9c-9e3d-93a22dd148ee" />

<img width="1328" height="890" alt="Image" src="https://github.com/user-attachments/assets/ad6e9d1a-68be-40ba-9b17-6d2f7409638f" />

### What Should Happen?

Selected text appears in the input box **once**, formatted as a quoted/referenced block.
## Actual Behavior

Selected text appears **multiple times** (often 2-3+ duplicate blocks of the same content) in the input box. Each new selection compounds the issue. To send a clean message, the user has to manually delete the duplicates first.
## Impact

- **Token waste**: every duplicate block consumes context tokens unnecessarily
- **Workflow disruption**: extra delete-step before every send
- **Especially severe for users on token-capped tiers (Claude Max)**: this directly burns paid-tier capacity on duplicated content

## Screenshot

[Attach the screenshot showing the duplicate-paste behavior in the input box]

<img width="1328" height="890" alt="Image" src="https://github.com/user-attachments/assets/b7c5a194-b07f-4751-8c6e-072ebf161478" />

<img width="845" height="655" alt="Image" src="https://github.com/user-attachments/assets/dcbff05c-a3c2-46a1-959f-aeb97c7a6d32" />

### Error Messages/Logs

```shell

```

### Steps to Reproduce

## Reproduction Steps

1. Have any Claude response visible in the conversation
2. Highlight a passage of text within the response
3. Right-click the selection → choose "Attach selection as context" (or "Add to context")
4. Observe the input box

## Expected Behavior

Selected text appears in the input box **once**, formatted as a quoted/referenced block.

## Actual Behavior

Selected text appears **multiple times** (often 2-3+ duplicate blocks of the same content) in the input box. Each new selection compounds the issue. To send a clean message, the user has to manually delete the duplicates first.

## Impact

- **Token waste**: every duplicate block consumes context tokens unnecessarily
- **Workflow disruption**: extra delete-step before every send
- **Especially severe for users on token-capped tiers (Claude Max)**: this directly burns paid-tier capacity on duplicated content

## Screenshot

[Attach the screenshot showing the duplicate-paste behavior in the input box]


### Claude Model

Opus

### Is this a regression?

No, this never worked

### Last Working Version

_No response_

### Claude Code Version

4.7 Opus

### Platform

Anthropic API

### Operating System

Windows

### Terminal/Shell

Terminal.app (macOS)

### Additional Information

## Environment

- Claude Code version: [version from `claude --version` if you can grab it]
- OS: Windows 11
- Plan: Claude Max
- Reproducibility: 100% — happens on every selection-to-context action

## Workaround

Currently the only workaround is manually deleting duplicate blocks from the input before pressing send. Cumulative across many sends, this is meaningful friction.

# Comments on anthropics/claude-code#53882
Total: 1 comments

--- Comment 1 ---
Author: 0xbrainkid
Date: 2026-04-27T11:43:31Z

This is not just an input annoyance. If `Add to context` duplicates the selected text multiple times, it distorts the user’s intent at the exact moment they are trying to define the model’s working set.

That makes it a context-integrity problem.

Users rely on this action to curate what the model should consider salient. Duplicating the same text changes the effective weighting of that material without the user choosing to do so. The model may then over-index on duplicated content, while the user believes they provided a balanced context slice.

So the risk is not only clutter. It is silent re-shaping of the prompt state.

Would be useful to pin down:
1. whether the duplication happens in the visible input only or also in the actual submitted payload
2. whether duplication count correlates with selection size / repeated clicks / streaming UI state
3. whether the model’s downstream behavior shows over-weighting of the duplicated segment

A context tool should help users express intent precisely. When it duplicates content, it quietly changes that intent before the model ever sees the request.

---

### Issue #34845 — Terminal randomly scrolls to top and auto-scrolls to bottom during output, breaking scrollback navigation

State: OPEN | #34845
Labels: enhancement, area:tui


---

## Problem

Two related scrolling issues in the Claude Code terminal:

### 1. Viewport jumps to the TOP randomly, even when idle
The terminal spontaneously scrolls to the very top of the scrollback history, even when Claude is **not** generating output. This happens unpredictably and forces the user to scroll all the way back down to where they were reading.

### 2. Auto-scroll during output generation overrides manual scrolling
When Claude is actively generating output (streaming tokens or running tools), the terminal automatically scrolls to follow the latest output. This overrides any manual scrolling the user is doing.

## Steps to Reproduce

**Random scroll-to-top (Issue 1):**
1. Have a conversation with substantial history
2. Scroll up to read previous output (while Claude is idle / not generating)
3. The viewport randomly jumps to the very top of the history

**Auto-scroll override (Issue 2):**
1. Start a conversation that produces long output
2. While output is still streaming, try to scroll up to read earlier content
3. The viewport snaps back to the bottom as new content renders

## Expected Behavior

- The viewport should never jump to the top on its own
- Users should be able to scroll freely through history without the position being reset
- Auto-scroll should pause when the user manually scrolls away from the bottom, and resume only when the user scrolls back to the bottom

## Impact

This is a significant usability pain point. The random scroll-to-top is especially disruptive — it makes reading through conversation history unreliable and frustrating. Users lose their place constantly.

## Environment

- Platform: Linux (Manjaro)
- Terminal: standard terminal emulator
- Claude Code: latest version

## Suggested Solution

Implement scroll position preservation:
- Never programmatically scroll to the top
- If the user scrolls up, lock the viewport at that position
- Resume auto-scroll only when the user scrolls back to the bottom

# Comments on anthropics/claude-code#34845
Total: 18 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-03-16T05:59:29Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/34794
2. https://github.com/anthropics/claude-code/issues/826
3. https://github.com/anthropics/claude-code/issues/34765

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: yurukusa
Date: 2026-03-16T07:56:16Z

Both issues are related to how Claude Code manages the terminal viewport via ANSI escape sequences (specifically CSI sequences for cursor positioning).

**Issue 1 (random scroll-to-top):** This typically happens when Claude Code emits a "save cursor position" (`\e[s`) without a matching restore, or when the status line refresh triggers a full-screen redraw via `\e[H` (cursor home). The idle-state UI refresh cycle can cause this even when no output is being generated.

**Issue 2 (auto-scroll override):** Claude Code uses `\e[?25l` (hide cursor) + write + `\e[?25h` (show cursor) patterns during streaming. Each write cycle implicitly moves the viewport to the cursor position, which is always at the bottom.

**Workaround for tmux users:**

```bash
# In .tmux.conf — force alternate screen buffer
set -g alternate-screen on

# This isolates Claude Code's cursor manipulation from your scrollback
# You can then use tmux's own scroll mode (prefix + [) freely
```

**Workaround for terminal multiplexer users (screen/tmux):**

The most reliable fix is to run Claude Code inside `tmux` or `screen`, which gives you a separate scrollback buffer that Claude Code's escape sequences cannot touch. You scroll the outer buffer, not the inner one.

**For native terminal users:**

Some terminals support "scroll lock" when you manually scroll up:
- **Windows Terminal**: Settings → Profiles → Advanced → "Automatically scroll to bottom on output" = OFF
- **kitty**: `scrollback_pager_history_size` + `scrollback_fill_enlarged_window no`

Check your terminal's documentation for an equivalent "don't chase new output while scrolled up" setting.

These settings prevent the terminal from chasing new output when you are reading history.

--- Comment 3 ---
Author: kjyv
Date: 2026-03-16T15:24:08Z

> iTerm2: Enable "Scroll to bottom on output" = OFF in Preferences → Profiles → Terminal

This doesn't seem to exist. Is this a claude generated answer or what?

--- Comment 4 ---
Author: yurukusa
Date: 2026-03-17T00:20:55Z

Apologies — my iTerm2 setting suggestions were wrong in both attempts. I don't use iTerm2 and was guessing incorrectly. The tmux workaround in my first comment should still work though.

--- Comment 5 ---
Author: factorshin
Date: 2026-03-17T02:00:48Z

> You're right, that iTerm2 setting doesn't exist — I mixed it up with a similar setting in other terminals. Apologies for the bad info.
> 
> The tmux workaround above should still work for iTerm2 users. For native iTerm2 scrollback, the relevant setting is actually under Preferences → Profiles → Terminal → **"Scroll to bottom on key press"** (which is on by default), but there's no direct "scroll to bottom on output" toggle like in Windows Terminal or GNOME Terminal.

In my iTerm2(version: 3.6.9), I can't find the 'Scroll to bottom on key press' option under Preferences → Profiles → Terminal. Is it removed or moved somewhere else?

--- Comment 6 ---
Author: kjyv
Date: 2026-03-17T11:16:34Z

> You're right, that iTerm2 setting doesn't exist — I mixed it up with a similar setting in other terminals. Apologies for the bad info.
> 
> The tmux workaround above should still work for iTerm2 users. For native iTerm2 scrollback, the relevant setting is actually under Preferences → Profiles → Terminal → **"Scroll to bottom on key press"** (which is on by default), but there's no direct "scroll to bottom on output" toggle like in Windows Terminal or GNOME Terminal.

Please stop trying to give advice if you have no idea and just use Claude Code to generate answers. We can all do that ourselves if we think that helps - hint: it does not

--- Comment 7 ---
Author: nullbio
Date: 2026-03-21T01:57:20Z

Still broken as of v2.1.81:

https://github.com/anthropics/claude-code/issues/36582
https://github.com/anthropics/claude-code/issues/35403
https://github.com/anthropics/claude-code/issues/36816
https://github.com/anthropics/claude-code/pull/35683
https://github.com/anthropics/claude-code/issues/33814
https://github.com/anthropics/claude-code/issues/34845
https://github.com/anthropics/claude-code/issues/33367
https://github.com/anthropics/claude-code/issues/34400
https://github.com/anthropics/claude-code/issues/826
https://github.com/anthropics/claude-code/issues/36621
https://github.com/anthropics/claude-code/issues/36128
https://github.com/anthropics/claude-code/issues/35766
https://github.com/anthropics/claude-code/issues/34242
https://github.com/anthropics/claude-code/issues/18299

--- Comment 8 ---
Author: felipekj
Date: 2026-03-21T23:51:30Z

+1 — experiencing this on GNOME Terminal (same behavior as IntelliJ terminal). Cursor randomly scrolls up during streaming output.

--- Comment 9 ---
Author: tonylin75
Date: 2026-03-23T12:11:46Z

It was fine when I used iterm + claude code. but when I used tmux with claude code the scroll jump goes crazy.. can't find a way to fix it yet.

--- Comment 10 ---
Author: andreas-civic
Date: 2026-03-24T12:02:30Z

I can reproduce this consistently. One additional observation:

**When staying at the bottom of the output, it works fine** — the view correctly follows new output. The issue only occurs when you scroll up to read previous output. As soon as Claude writes a new line, the view jumps to the top of the conversation instead of staying at the scrolled position.

This happens in VS Code's integrated terminal on macOS. I confirmed it's Claude Code-specific — running a regular command with continuous output in the same VS Code terminal lets you scroll up and stay in place while output continues below.

So the bug seems to be in Claude Code's terminal renderer: when new content is appended and the viewport is not at the bottom, it re-anchors to the top instead of maintaining the current scroll position.

--- Comment 11 ---
Author: jpsear
Date: 2026-03-24T13:22:51Z

Am also getting this frustrating bug. 

`--version: 2.1.81 (Claude Code)`

Running in iTerm 2 on Mac 26.3.1

--- Comment 12 ---
Author: sstraus
Date: 2026-03-24T15:04:04Z

👍 We're experiencing the same issue embedding xterm.js 6.0.0 in a Tauri app. The scroll position jumps when Claude Code redraws its TUI while the user is scrolled up. Confirmed root cause: cursor-up sequences exceeding viewport height + ESC[2J/ESC[3J.

--- Comment 13 ---
Author: belousoves
Date: 2026-03-26T12:38:12Z

Have the same issue with Gnome terrminal 3.44.0. Extremely annoying and prevent you to reading anything while claude still work.

--- Comment 14 ---
Author: copperx
Date: 2026-04-02T18:41:02Z

Any updates or workarounds?

--- Comment 15 ---
Author: YossiSaadi
Date: 2026-04-05T23:36:58Z

PLEASE 😢 

--- Comment 16 ---
Author: alisonjf
Date: 2026-04-06T14:19:25Z

Dude that's frustrating, feel like "read previous output FAST GOGO YOU HAVE 3 SECONDS"

--- Comment 17 ---
Author: jgwill
Date: 2026-04-08T08:16:56Z

> I confirmed it's Claude Code-specific

* On my part, I have the same experience with claude-code but also with other harness such as pi-mono.  I am questionning, which logics do they have in common ?  'Checking width or height of the terminal for the TUI refresh ?  Something else ?

--- Comment 18 ---
Author: parsakhaz
Date: 2026-04-10T06:30:43Z

> this is a huge issue. love claude code but this makes it really really hard to use

hey. it's fixed at the terminal level here

https://github.com/Dcouple-Inc/Pane/pull/120

open source, using xtermjs which is the same terminal as VS Code. feel free to copy this fix or download the latest release to run claude code on any operating system with the fix in place. i was so mad and frustrated at this that I had to fix it myself.

> Not just a scrolling issue — also a rendering/layout problem in VS Code's side-by-side panel mode.
> 
> When Claude Code runs in VS Code with the terminal on one side and the editor on the other, text formatting breaks in unpredictable ways. Options and multi-line output get weirdly split left-right, text wraps incorrectly, and the whole experience feels janky rather than fluid. Combined with the scroll-jumping, longer sessions in VS Code become genuinely hard to follow.
> 
> This isn't just macOS standalone terminal — it's very much a VS Code integrated terminal issue too.

yeah i had to switch off cursor/vscode and build myself an ide that managed xtermjs (the library they both use) well enough for the complex TUIs to not break.

works great and i have a fix for the scroll jump i just implemented rn here

https://github.com/Dcouple-Inc/Pane/pull/120

---

### Issue #29937 — [BUG] Terminal rendering corruption in tmux - text overlaps and overwrites previous output

State: OPEN | #29937
Labels: bug, platform:linux, area:tui


---

## Environment
- **Claude CLI version:** 2.1.63
- **Operating System:** Ubuntu (Linux 6.8.0)
- **Terminal:** tmux inside alacritty/standard terminal emulator
- **TERM:** `tmux-256color`
- **Platform:** Anthropic API

## tmux configuration (ruled out as cause)
```
set -sg escape-time 10
set -g default-terminal "tmux-256color"
set -ga terminal-overrides ",xterm-256color:Tc"
set -g history-limit 50000
set -g focus-events on
```
`alternate-screen` is `on` (default).

## Bug Description

During normal Claude Code sessions in tmux, the terminal rendering becomes corrupted. Text from different parts of the session (code output, permission prompts, previous responses) overlaps and overwrites each other on the same lines, making the interface unreadable.

This is **not** caused by:
- Resizing tmux panes (happens without any resize)
- Incorrect TERM settings
- Missing tmux configuration

The corruption appears to be in Ink's internal render state — the line positions it caches become out of sync with what's actually displayed. Once corrupted, neither `Ctrl-L` (terminal redraw) nor tmux's redraw (`prefix + r`) fixes it, since the problem is in Ink's virtual buffer, not the terminal's.

## Steps to Reproduce

1. Run Claude Code inside a tmux session
2. Have a multi-turn conversation with tool calls (Bash commands, file reads, etc.)
3. Eventually the renderer gets into a corrupted state where new output overwrites previous text

The trigger seems to be Ink's full-buffer redraw cycle — particularly when permission prompts appear mid-render, but it also happens during normal streaming output.

## Expected Behavior

Text should render sequentially without overlapping. New output should appear below previous output.

## Actual Behavior

Text from different render cycles (code blocks, permission dialogs, streaming responses) is drawn at overlapping positions, producing garbled/unreadable output. The corruption persists until the session is restarted.

## Workaround

Only reliable fix is `/clear` or restarting the session.

## Related Issues

- #769 — Screen flickering caused by full-buffer redraw on status indicator updates
- #826 — Console scrolling to top of history when adding text

All three issues appear to stem from the same root cause: Ink redraws the entire terminal buffer on each render cycle rather than doing targeted line updates, and the calculated positions drift from actual terminal state over time.

# Comments on anthropics/claude-code#29937
Total: 8 comments

--- Comment 1 ---
Author: WingsOfPanda
Date: 2026-03-19T05:06:16Z

Still reproducing on the latest Claude Code release in tmux on Linux.

I don’t think this should go stale: newer TUI rendering issues like #35356 and #35803 look plausibly related, and the core symptom here remains the same — the UI render state appears to drift and overwrite existing terminal content, making the session unreadable.

I’m also still seeing the repeated auto-scroll/jump from the top to the end of the session, which makes the rendering instability noticeably worse, especially on remote machines where the TUI is the only interface. Terminal redraws still don’t recover it; `/clear` or restarting is still the only reliable workaround for me.

I’d suggest keeping this open as a canonical tracker for this class of TUI/tmux render-corruption bugs unless there’s already another root issue intended to supersede it.

--- Comment 2 ---
Author: efloehr
Date: 2026-03-19T15:56:03Z

Yes, this is still an issue in 2.1.79. And my use case is exactly as @WingsOfPanda describes: remote machine where TUI is the only interface.

--- Comment 3 ---
Author: jarnesjo
Date: 2026-03-25T07:21:54Z

Still experiencing this on v2.1.74 in VSCode's integrated terminal on macOS (Darwin 25.3.0). Two symptoms:

1. **Scroll jumping** — scrolling up during output causes the terminal to snap back to the top (not bottom), making it impossible to review previous output
2. **Rendering corruption** — intermittent garbled/overlapping text that requires restarting the terminal

Both issues have gotten worse recently and now occur in all projects. `/clear` helps temporarily but the scroll issue returns immediately when new output is streamed.

--- Comment 4 ---
Author: RJAFusion
Date: 2026-03-25T08:01:09Z

Yes - I've been having this issue in TMUX session in iTerm2 on MacOs 26.2 for the past week or so. It makes AskUserQuestion tools usage unusable as the selection line renders in the wrong position and text overlaps all over the place.

Resizing the window forces a redraw, so the AskUserQuestion tool can be used properly, but then it just corrupts text again on the next turn.

Also have the scroll jumping issue as well

--- Comment 5 ---
Author: parsakhaz
Date: 2026-04-10T06:33:25Z

> this is a huge issue. love claude code but this makes it really really hard to use

hey. it's fixed at the terminal level here

https://github.com/Dcouple-Inc/Pane/pull/120

open source, using xtermjs which is the same terminal as VS Code. feel free to copy this fix or download the latest release to run claude code on any operating system with the fix in place. i was so mad and frustrated at this that I had to fix it myself.

> Not just a scrolling issue — also a rendering/layout problem in VS Code's side-by-side panel mode.
> 
> When Claude Code runs in VS Code with the terminal on one side and the editor on the other, text formatting breaks in unpredictable ways. Options and multi-line output get weirdly split left-right, text wraps incorrectly, and the whole experience feels janky rather than fluid. Combined with the scroll-jumping, longer sessions in VS Code become genuinely hard to follow.
> 
> This isn't just macOS standalone terminal — it's very much a VS Code integrated terminal issue too.

yeah i had to switch off cursor/vscode and build myself an ide that managed xtermjs (the library they both use) well enough for the complex TUIs to not break.

works great and i have a fix for the scroll jump i just implemented rn here

https://github.com/Dcouple-Inc/Pane/pull/120

--- Comment 6 ---
Author: KnightHawk06
Date: 2026-04-13T22:19:13Z

Happens in Konsole too.

--- Comment 7 ---
Author: Kevin7Qi
Date: 2026-05-10T04:12:40Z

Still seeing this on Claude Code v2.1.138 with Ghostty on macOS, over SSH into a tmux session on a Linux remote.

In my case, this appears to be Ghostty-specific: the same remote tmux session works normally from macOS Terminal.app, and also works normally from Windows Terminal. Forcing a more conservative TERM value did not resolve it in Ghostty.

--- Comment 8 ---
Author: u35253
Date: 2026-05-23T22:39:48Z

Yes, as a TUI, I would anticipate that claude code would not get corrupted after about 1 minute of use when simply running in a tmux pane via ssh.  But it does, much the OP describes, except it really just seems to stop.  Everything else in the ssh/tmux session keeps working.  iterm2 is running on macOS 15.7 host, with the macOS 26 guest VM being ssh'd into, where claude is allowed to run.  (What is the path to success?  If I find out, I hope to come back and comment here with an answer.)

---

### Issue #61480 — [FEATURE] Replace the decorative fillers with literal action labels matching the tool being invoked

State: OPEN | #61480
Labels: enhancement, area:tui, user-experience


---



### Problem Statement

  Issue: Decorative status fillers hide what the model is actually doing

  While a tool call is in flight, Claude Code displays decorative status labels like tomfoolering..., razzle-dazzling..., divining..., contemplating...
  etc. instead of naming the actual action being performed.

  This is actively harmful for debugging long-running or hanging operations:

  1. I cannot tell whether the model is waiting on a shell command (e.g. hdc shell hilog streaming for minutes), reading a large file, generating tokens,
  or genuinely stuck.
  2. When a tool call takes unusually long, I have no way to judge whether to interrupt — the filler gives zero signal about what's happening.
  3. The labels are not amusing on the n-th encounter; they read as noise and degrade trust that the CLI is being straightforward about its state.

### Proposed Solution

  Requested change: replace the decorative fillers with literal action labels matching the tool being invoked, e.g. Running Bash: hdc shell ..., Reading
  file: src/foo.ts, Searching code, Generating response. If a "fun" mode is desired, gate it behind an opt-in setting; the default should be informative.

### Alternative Solutions

_No response_

### Priority

High - Significant impact on productivity

### Feature Category

CLI commands and flags

### Use Case Example

_No response_

### Additional Context

_No response_

# Comments on anthropics/claude-code#61480
Total: 1 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-22T14:42:02Z

Found 2 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/21151
2. https://github.com/anthropics/claude-code/issues/59842

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

---

### Issue #62700 — Tool calls execute successfully but are followed by a spurious "Your tool call was malformed and could not be parsed. Please retry."

State: OPEN | #62700
Labels: bug, platform:macos, area:model, area:core


---

## Environment
- Claude Code, model: Opus 4.7 (1M context) — `claude-opus-4-7[1m]`
- Platform: macOS (darwin 25.5.0), shell: zsh
- Plugins / MCP active: oh-my-claudecode (OMC), context7, codex-cli, Notion MCP, plus a large set of deferred tools and project `PreToolUse` / `PostToolUse` hooks

## Symptom
After most tool calls (Bash / Edit / Write), the assistant turn is immediately followed by a system message:

> Your tool call was malformed and could not be parsed. Please retry.

However, the tool **actually executed correctly** — `git commit/push/cherry-pick`, `gh` queries, and file writes all produced normal output and took effect. The notice appears *despite* success.

Sometimes it is accompanied by `[Request interrupted by user]`, and the conversation appears to stall, requiring me to type "continue" repeatedly to make progress.

## Frequency
Persistent since ~2026-05-26 (yesterday), recurring on nearly every tool call.

## Impact
The conversation looks like it disconnects / hangs, forcing repeated manual "continue". No data loss (work completes), but heavy friction.

## Steps to reproduce (not fully isolated)
1. In a session with the above plugin/hook stack, run any Bash / Write / Edit tool call.
2. Observe the "malformed and could not be parsed" notice even though the call was valid and executed successfully.

## Expected behavior
No spurious parse-failure notice when the tool call was valid and executed.

## Suspected area (uncertain)
Tool-call parsing / streaming layer, or a hook/plugin interfering with tool-call serialization; possibly an interaction with the large deferred-tool / MCP set. Filing so others hitting the same can confirm.

# Comments on anthropics/claude-code#62700
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-27T04:53:58Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/62467
2. https://github.com/anthropics/claude-code/issues/62344
3. https://github.com/anthropics/claude-code/issues/34713

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: notwin
Date: 2026-05-28T02:38:27Z

+1 confirming this exact symptom on macOS today (2026-05-28, v2.1.153) in a long-running session.

**Pattern observed:** a `Bash` or `Edit` tool call executes successfully (file written, command exits 0, output returned) — and then the very next assistant turn is immediately interrupted by `Your tool call was malformed and could not be parsed. Please retry.` The "retry" then succeeds with no change to the call, confirming the tool itself was not malformed; the parser tripped after the fact.

**Repro context that seems to surface it:**
- Long session with many sequential `Bash` + `Edit` calls (60+ tool uses across one task)
- Multiple plugins/skills loaded (superpowers, code-review, codex, vercel/*, pr-review-toolkit)
- Tends to fire right after a tool result that itself contains a `<system-reminder>` block (e.g. the periodic "task tools haven't been used recently" reminder, or `new-diagnostics` blocks). The reminder text appears to be getting included in the parser's view of the next call.

**Frequency:** ~10 occurrences in a single ~3-hour session today. It got noticeably worse as the session length and per-turn token count grew — consistent with the few-shot poisoning hypothesis in #62344.

**Workaround:** `/clear` recovers cleanly. Inline retry sometimes works once but the rate-of-failure stays elevated for the remainder of the session — also consistent with #62344. `claude --no-plugins` not yet tested in repro session.

---

### Issue #49619 — [BUG] Stream idle timeout / partial response during long tool-use turns on Claude Code Web (Opus 4.7, 1M and non-1M)

State: OPEN | #49619
Labels: bug, duplicate, area:claude-code-web, platform:web, api:anthropic


---



### What's Wrong?

## Environment
- Platform: Claude Code Web (claude.ai/code)
- Model(s) affected:
  - `claude-opus-4-7[1m]` (1M context) — reproducible
  - `claude-opus-4-7` (standard context) — also reproducible after switching
- OS: Linux sandbox (provided by the web harness)
- Session type: long-running conversation with multiple tool calls
  (Read / Bash / Grep), working in a git repo
- Approx. transcript length when error first appeared: mid-session,
  after several dozen tool calls and a few long assistant messages

## Summary
During turns where the assistant is about to produce a long text output
(e.g. drafting a ~400-line markdown design doc after a few Read/Bash
tool calls), the stream terminates with:

  `API Error: Stream idle timeout - partial response received`

The error is *not* triggered by the tool calls themselves — tool results
arrive normally. It consistently fires in the window between the last
tool result and the start (or middle) of the long text reply.

## Reproduction
1. Open a Claude Code Web session with Opus 4.7 (1M) on a non-trivial
   repo (mine: ~several hundred markdown/py files, custom CLAUDE.md).
2. Hold a long design discussion (tens of turns, many Read/Grep/Bash
   calls, several multi-paragraph replies).
3. Ask the assistant to draft a long markdown document (~400+ lines)
   into a file, preceded by 1–2 exploratory tool calls.
4. Observe `Stream idle timeout - partial response received` fire
   after the tool calls complete but before / during the long write.

Retry attempts (even after slimming CLAUDE.md and switching from
`claude-opus-4-7[1m]` to plain `claude-opus-4-7`) reproduce the same error.

## Actual behavior
Stream aborts mid-turn with an idle timeout; partial response is
discarded from the user's perspective and the Write tool call never
executes. The session is usable afterwards, but the same turn cannot
be completed — it fails repeatedly at roughly the same point.

## Impact
- Blocks any workflow that involves drafting a long file in a single
  turn (design docs, protocol revisions, report packs).
- Forces the user to manually split work into smaller chunks, losing
  the model's ability to produce a coherent document in one pass.
- Switching to the non-1M model does not resolve it, so it does not
  appear to be strictly a 1M-context issue.

## Workarounds tried (none fully effective)
- Slimmed CLAUDE.md to reduce per-turn context overhead — still fails.
- Switched `claude-opus-4-7[1m]` → `claude-opus-4-7` — still fails.
- Starting a fresh session helps temporarily, but the error returns
  after the session grows.

## Additional context
- The moments when errors occur most frequently are always during the combination of “multi‑turn conversations + about to generate long markdown.”
- The web version cannot call /help, and there is no way to report issues directly from the client, so I am submitting this issue manually.
- Session ID :  https://claude.ai/code/session_014AtytC2zxPcAqaoj9LwcGi

## Ask
1. Is the idle timeout threshold tunable (e.g. via a server-side
   setting or client flag)?
2. Can the stream be kept alive with heartbeats during long
   text generation so long Write tool calls don't get cut off?
3. Is there a known interaction between 1M context and long
   tail-end text streaming that we should avoid?

### What Should Happen?

## Expected behavior
The assistant should finish streaming the long reply, or at minimum
fail with a retriable error that preserves the in-progress Write/Edit
tool call.

### Error Messages/Logs

```shell
API Error: Stream idle timeout - partial response received
```

### Steps to Reproduce

1. Open a Claude Code Web session with Opus 4.7 (1M) on a non-trivial
   repo (mine: ~several hundred markdown/py files, custom CLAUDE.md).
2. Hold a long design discussion (tens of turns, many Read/Grep/Bash
   calls, several multi-paragraph replies).
3. Ask the assistant to draft a long markdown document (~400+ lines)
   into a file, preceded by 1–2 exploratory tool calls.
4. Observe `Stream idle timeout - partial response received` fire
   after the tool calls complete but before / during the long write.

### Claude Model

Opus

### Is this a regression?

I don't know

### Last Working Version

_No response_

### Claude Code Version

Web (claude.ai/code), encountered on 2026-04-17

### Platform

Anthropic API

### Operating System

Windows

### Terminal/Shell

Other

### Additional Information
Additional observation (session 014AtytC2zxPcAqaoj9LwcGi, 2026-04-17):
Stream timeout fired during a ~210-line Edit call. The file write
itself completed successfully (verified via `git status` post-timeout);
only the client-side stream terminated. This suggests the issue is in
keep-alive / heartbeat between tool-result-accepted and next-assistant-
token, not in the tool execution itself.

# Comments on anthropics/claude-code#49619
Total: 12 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-04-17T00:44:30Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/48974
2. https://github.com/anthropics/claude-code/issues/48901
3. https://github.com/anthropics/claude-code/issues/47555

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: trex0092
Date: 2026-04-17T21:26:13Z

I am getting the same !!! 

--- Comment 3 ---
Author: guillaume-defer
Date: 2026-04-19T20:04:34Z

Same here

--- Comment 4 ---
Author: MrVolcano
Date: 2026-04-20T16:07:44Z

Me too. Multiple times today

--- Comment 5 ---
Author: MrVolcano
Date: 2026-04-20T16:09:29Z

Why have all of the possible duplicated been closed as duplicates? 

Where's the master bug record?

--- Comment 6 ---
Author: efecetinkaya21
Date: 2026-04-25T16:30:47Z

Same failure mode:

- Multi-turn planning session on a non-trivial private repo with a 
  custom CLAUDE.md, context at roughly 33% of the window.
- Asked the assistant to rewrite a long markdown planning document 
  from scratch as a handoff for a new session.
- Model performed 1–2 exploratory tool calls (file read, scan), 
  then began the Write call.
- Stream terminated with `API Error: Stream idle timeout - partial 
  response received` before the write completed in the UI.
- Retried 4 times across 2 separate sessions on the same repository 
  over 2 consecutive days. All failed at roughly the same point. 
  Reducing the scope of the write did not help.
- Sessions remained alive, but the same turn could not be 
  completed — consistent with this being a keep-alive / heartbeat 
  gap between tool-result-accepted and the next assistant token, 
  not a model or tool-execution issue.

Workarounds suggested by support (manual chunking of the write, 
raising `CLAUDE_STREAM_IDLE_TIMEOUT_MS`) do not apply to the Cloud 
/ browser surface. Confirmation that a fix is in progress for this 
specific surface would be appreciated.

--- Comment 7 ---
Author: cmungall
Date: 2026-04-26T15:32:55Z

I encounter this frequently, and it makes cc on the web almost unusable for me, as my workflow frequently involves large yaml file edits.

In case it's not obvious from the OP, attempting to coax it along by saying "try again" or similar is a great way to burn tokens to no avail. When this does happen, I say:

"Commit and push what you have so far. Do not create more yaml. No more writes. I don’t care if it doesn’t validate. Commit and push NOW"

Then create a PR so I have the option of taking over in a terminal session. After that I might try asking it it break down its edits into smaller units, which is often successful.

--- Comment 8 ---
Author: kainashville
Date: 2026-04-26T19:17:50Z

Having the same issues - it's driving me crazy. Sadly no one is actively trying to fix it and we have to find complex workarounds

--- Comment 9 ---
Author: AutumnsGrove
Date: 2026-04-27T17:20:39Z

Chiming in, this happens to me pretty much every single time I use Claude.ai/code. Makes the product pretty much unusable. 

I have noticed that is a 4.7 opus thing though, as sonnet 4.6 and haiku 4.5 have no such issues. Truly, opus 4.7 is the regression king. 

--- Comment 10 ---
Author: filipradetic-afk
Date: 2026-04-28T08:36:58Z

+1 — Same issue on Windows native Claude Code (npm-global, v2.1.121, Node v22 LTS, web login auth).

**Reproducible on a large monorepo:**
- ~240 markdown files in docs/, 22 Docker microservices
- Initially had 53k char CLAUDE.md → slimmed to 9.7k chars + split into 10 docs/ files
- Slimming helped with simple queries (now work in seconds ✅)
- BUT complex multi-tool tasks still fail with "API Error: Stream idle timeout - partial response received"

**Specific pattern observed:**
- Simple read/search tasks: work fine
- Complex tasks involving multiple file searches + analysis + extended thinking: fail consistently
- Failure point: between tool result delivery and next assistant token (matches Pattern 2 from #25979)
- Extended thinking ("xhigh effort") seems to amplify the issue
- Task example that fails: "Failed to load preflight report" debugging across UI + agent code

**Workarounds tested:**
- Slim CLAUDE.md ✅ helps simple tasks, ❌ doesn't fix complex
- Reinstall Claude Code with Node v22 LTS ✅ helps initial connection, ❌ same timeout on long tasks
- Antivirus disabled (Defender) ❌ no change
- Network verified clean (Test-NetConnection OK, no SSL inspection)
- Splitting tasks into smaller steps ✅ works as workaround

**Question for maintainers:**
Is CLAUDE_STREAM_IDLE_TIMEOUT_MS effective in practice for this scenario, or does the issue lie deeper in keep-alive between tool-result and next-token?

Happy to provide more session details if helpful.

--- Comment 11 ---
Author: SM2000
Date: 2026-05-20T19:25:08Z

Adding data to this issue — we're seeing the same pattern via the Anthropic MCP Connector (`mcp-client-2025-11-20` beta, not Claude Code, but the same streaming-stall signature).

## Environment
- Model: claude-opus-4-7 via Messages API with `mcp_servers` parameter
- Beta header: `mcp-client-2025-11-20`
- max_tokens: 2000, no extended thinking, stream=True
- SDK: anthropic==0.96.0
- Remote MCP server: HTTPS-exposed, OAuth-authenticated, backed by Snowflake
- Network confirmed healthy (TCP/SSE pings flow throughout the stall)

## Symptom

On approximately 4 out of 5 events in a controlled test harness, the streaming response stalls for ~300 seconds between `content_block_stop type=mcp_tool_use` and `content_block_start type=mcp_tool_result`. The pattern is reproducible and consistently ~300s ± 15s — strongly suggesting a fixed-duration timeout-and-recover rather than genuine processing time.

During the stall:
- The TCP/SSE connection stays alive — `ping` events arrive at metronomic 30.000s ± 0.030s intervals for the entire gap (typically 10 pings)
- `thinking_delta_count = 0` (extended thinking is not enabled)
- `message_start_count = 1` (no silent reconnect)
- Single tool calls on the same session, before and after the stalled batch, complete in 4.6–9.0 seconds — so the session itself is not degraded

## What's different about the stalled calls

**The stall reproduces specifically on parallel tool-call batches.** When the model emits two or more `mcp_tool_use` blocks back-to-back (idx=4 and idx=5 in our trace, emitted 0.776s apart), the gateway holds *all* results and then flushes them in a single batch — both `mcp_tool_result` blocks (idx=6 and idx=7) arrive within 2ms of each other after the 300s stall.

Single-tool calls in the same stream complete normally:
- idx=1 (single `get_database_metadata`): 9.0s round-trip ✓
- idx=4 + idx=5 (parallel batch of 2 `sql_exec`): **301.9s round-trip** ✗
- idx=9 (single `sql_exec` after the gap): 4.6s ✓
- idx=12 (single `sql_exec`): 4.8s ✓

This matches the regression behavior reported in [#14353](https://github.com/anthropics/claude-code/issues/14353), and the "proxy holds tool_results" pattern in [#38437](https://github.com/anthropics/claude-code/issues/38437).

## Three-source correlation isolates the stall upstream of the MCP server

We instrumented and cross-correlated three independent log sources for one stalled event (gap: `2026-05-20T17:26:41.464Z → 17:31:43.370Z`, 301.9 seconds):

| Source | Activity during the 301.9s gap |
|--------|--------------------------------|
| Harness stream-event log | 10 pings, no content blocks, no errors |
| Snowflake `ACCOUNT_USAGE.QUERY_HISTORY` | 0.949s of actual query execution; **idle for the remaining 298s** |
| MCP server (`assistant_tool_invocations`) | Tool calls logged with normal `duration_ms` values [confirm fast durations before posting] |

The MCP server returned its responses promptly. Snowflake idled for 298 of the 302 seconds. The Anthropic gateway then held the batched results for the remaining time before streaming them back. The latency is unambiguously upstream of the MCP server.

## Related issues

This appears to be the same root behavior described in:
- [#18028](https://github.com/anthropics/claude-code/issues/18028) — streaming stalls of 59–138s, network healthy, no errors
- [#44 (claude-agent-sdk-typescript)](https://github.com/anthropics/claude-agent-sdk-typescript/issues/44) — 3+ minute pauses, no events, no pings during gap (we *do* see pings, but the stall mechanism looks similar)
- [#38437](https://github.com/anthropics/claude-code/issues/38437) — MCP proxy silently holding tool_results that the upstream MCP server has already returned
- [#49619](https://github.com/anthropics/claude-code/issues/49619) — author's diagnosis: *"the issue is in keep-alive / heartbeat between tool-result-accepted and next-assistant-token, not in the tool execution itself"* — matches our finding
- [#25979](https://github.com/anthropics/claude-code/issues/25979) — no client-side read timeout on streaming, so stalls can run to inactivity timeout
- [#14353](https://github.com/anthropics/claude-code/issues/14353) — parallel MCP tool calls regressed to sequential in v2.0.71

## Reproduction

Anyone can repro with the MCP Connector beta:
1. Configure `mcp_servers` to point to a remote MCP server that exposes 2+ fast tools
2. Send a prompt that induces the model to issue 2+ parallel tool calls (e.g. "Look up X and Y at the same time")
3. Stream the response and log `content_block_start` / `content_block_stop` events with timestamps
4. Observe: in a fraction of runs (in our experiment ~80% of events on `condition_b_snowflake` and `condition_c_semantic`), the parallel batch stalls for ~300s before results arrive together

Happy to file this as a fresh issue if the maintainers prefer to keep #18028 scoped to the Claude Code CLI case rather than the MCP Connector API case — but they look like the same underlying mechanism.


--- Comment 12 ---
Author: befreak-info
Date: 2026-05-26T01:55:24Z

**Workaround that worked for me:**

Switching from Opus to **Sonnet** resolved the frequent hang/freeze issues I was experiencing.

**Environment:**
- Platform: Claude Code CLI (desktop app on macOS)
- Model before: `claude-opus-4-7` (Max plan — auto-upgraded to `claude-opus-4-7[1m]`)
- Model after: `claude-sonnet-4-6`
- Result: Hangs stopped completely after switching to Sonnet

**Note:**
On Max/Team plans, selecting Opus automatically upgrades to the 1M context version, which cannot be avoided through the `/model` picker alone. Setting `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` in `~/.claude/settings.json` disables the auto-upgrade if you want to stay on Opus.

Hope this helps others experiencing similar issues.

---

### Issue #56030 — [FEATURE] Monitor needs to respect `sandbox.excludedCommands` and have a `dangerouslyDisableSandbox` option

State: OPEN | #56030
Labels: enhancement, area:sandbox, stale

---



### Problem Statement

  The Monitor tool cannot be run outside the sandbox, which makes it unusable for monitoring commands that require host access. Specifically:
                                                                                                                                                          
  - Bash accepts a dangerouslyDisableSandbox parameter and honors sandbox.excludedCommands from settings.json. Monitor honors neither — there is no       
  per-call escape hatch and no way to allowlist a command.                                                                                                
  - Concrete use case: I want a Monitor that tails GCP logs via gcloud logging read / gcloud beta run services logs tail. gcloud only authenticates       
  correctly when run outside the sandbox (I have it in excludedCommands for exactly this reason, and it works fine via Bash).                             
  - The result is that any "watch this stream" workflow that depends on host auth, host networking, or a credential helper has to be done with Bash 
  run_in_background polling instead of Monitor, which defeats the purpose of the tool. 

### Proposed Solution

  Bring Monitor to parity with Bash for sandbox handling:
                                                                                                                                                          
  1. Accept a dangerouslyDisableSandbox: true parameter on Monitor calls, with the same approval/prompting UX as Bash.                                    
  2. Honor sandbox.excludedCommands from settings.json — if the monitored command matches the allowlist, run it outside the sandbox automatically (same   
  matching rules as Bash).                                                                                                                                
  3. Document this in the Monitor tool description so the model knows it's an option (currently the tool docs don't mention sandboxing at all).

### Alternative Solutions

  - Bash with run_in_background + polling — works, but loses Monitor's streaming/notification semantics; I have to read the log file periodically instead of reacting to new lines, and it eats more context.                                                                                                     
  - Piping gcloud output to a file from a sandbox-disabled Bash call, then Monitor-ing the file — fragile (auth refresh, partial writes, file rotation)
  and adds a moving part for something that should be one call.                                                                                           
  - Running claude itself with the sandbox disabled globally — overkill and removes the safety I want for everything else.
  - Skipping Monitor entirely and using a separate terminal with gcloud ... tail — works but defeats the point of having Claude watch the stream

### Priority

Low - Nice to have

### Feature Category

Interactive mode (TUI)

### Use Case Example

  1. I add gcloud to sandbox.excludedCommands in settings.json so it can authenticate against GCP.                                                        
  2. Running gcloud logging read ... via Bash works — the excludedCommands rule kicks in and the command runs outside the sandbox with valid credentials.
  3. I try to set up a Monitor on gcloud beta run services logs tail my-service to watch a Cloud Run service while I work.                                
  4. Monitor runs the command inside the sandbox anyway, ignoring excludedCommands, so gcloud fails to authenticate and the monitor produces no useful    
  output.                                                                                                                                                 
  5. There is no dangerouslyDisableSandbox parameter on Monitor to force it out of the sandbox per-call either, so I have no escape hatch.                
  6. I fall back to Bash run_in_background + polling a log file, which loses Monitor's streaming/notification semantics.  

### Additional Context

_No response_

# Comments on anthropics/claude-code#56030
Total: 0 comments

No comments on this issue.

---

### Issue #63374 — Interrupting an interleaved-thinking turn mid-stream wedges the session: unrecoverable 400 "thinking blocks ... cannot be modified"

State: OPEN | #63374
Labels: duplicate, platform:macos, area:core


---

### Environment
- Claude Code: **2.1.154**
- Model: **claude-opus-4-8** (1M context), max effort — extended/interleaved thinking active
- Platform: macOS (darwin 25.2.0)

### Summary
If the user submits a new prompt while a large assistant turn with **interleaved thinking** is still streaming, the harness can persist an assistant message whose **final content block is a `thinking` block** — i.e. a tool-use turn that isn't terminated by a `tool_use`/`text` block. Every subsequent API request replays that malformed message and fails with:

```
API Error: 400 messages.N.content.M: `thinking` or `redacted_thinking` blocks in the latest
assistant message cannot be modified. These blocks must remain as they were in the original response.
```

The conversation is then **wedged**: `continue`, a new prompt, even asking about the error all return the *identical* 400, because the corrupt assistant turn is frozen in history and replayed on every request. The only recovery is a manual rewind past that turn or starting a fresh session (losing context).

### Repro
1. Opus 4.8 with max effort (interleaved thinking on).
2. Trigger a turn that fans out **many tool calls in a single assistant message** — in my case 21 tool calls (MCP servers + `Bash` + `ToolSearch`) with **10 interleaved `thinking` blocks**, 32 content blocks total.
3. While the model is still streaming — specifically right after a `thinking` block and *before* its following `tool_use` — submit a new prompt (here also with an attachment).
4. The next request 400s, and never recovers.

### Evidence (reconstructed from the session transcript)
The final assistant message (blocks regrouped by `message.id`) ended on a `thinking` block:

```
[24] tool_use   mcp__<server>__<tool>
[25] tool_use   mcp__<server>__<tool>     <- API error anchored at content.25
[26] thinking
[27] tool_use   Bash
[28] thinking
[29] tool_use   mcp__<server>__<tool>
[30] tool_use   mcp__<server>__<tool>
[31] thinking                              <- TERMINAL block: dangling, no tool_use/text after it
```

Millisecond timing shows the mid-stream submission race:

```
…:35.387  user        tool_result    (last tool result returns)
…:00.903  assistant   thinking       (block 31)
…:00.989  attachment                 (+86 ms — new user prompt + attachment submitted mid-stream)
…:01.297  assistant   API Error 400 …content.25
```

All 21 tool calls had completed cleanly (21 `tool_use` / 21 `tool_result`, none missing) — so the turn was **not** interrupted during tool execution. It was interrupted *between* a `thinking` block and the next `tool_use`, leaving the trailing thinking block dangling. The malformed message then replayed on `continue` and three subsequent prompts, each returning the identical 400 (4 failed requests total before the user gave up and started a new session).

Note: the error path names `content.25` (a `tool_use`) while the message text complains about `thinking` blocks — consistent with an off-by-one between the serialized request and raw block order; `thinking` blocks sit immediately around that index (content.23 and .26).

### Expected behavior
On a mid-stream interrupt, the persisted assistant message should be left in an API-valid state. Any of:
- Drop a trailing/dangling `thinking` block not followed by a `tool_use`/`text`.
- Defer appending the new user turn until the in-flight assistant message is well-formed.
- Detect the wedged state and auto-rewind (or prompt to rewind) instead of replaying the identical doomed request multiple times.

### Impact
- **Hard conversation wedge** — unrecoverable without manual rewind or a new session; in-progress context is lost.
- More likely with extended/interleaved thinking (Opus 4.8 max effort) combined with **large single-turn tool fan-outs**: the more interleaved `thinking` blocks in a turn, the larger the window for this race.
- The client silently retries the identical failing request several times before surfacing the error to the user.

# Comments on anthropics/claude-code#63374
Total: 1 comments

--- Comment 1 ---
Author: dalito
Date: 2026-05-28T20:53:17Z

I see the same error on Windows and same Claude Code version but even for rather simple tasks (no tools).

---

### Issue #60133 — API Error: The socket connection was closed unexpectedly. + SOLUTION FOR ANTHROPIC DEVS

State: OPEN | #60133
Labels: bug, duplicate, has repro, platform:linux, area:networking


---

# Bug: "Socket connection was closed unexpectedly" during long agentic sessions

## Summary

Claude Code CLI throws `API Error: The socket connection was closed unexpectedly` consistently
during long agentic tasks. The error is systemic — it occurs across all projects, prompts, and
directories, always mid-session, never at startup. The session must be fully restarted to recover.

---

## Environment

- **Claude Code version:** 2.1.143
- **OS:** Arch Linux (Manjaro), kernel 6.12.85-1
- **Install method:** Official installer (`curl | bash`) + pacman/AUR (same binary, both 2.1.143)
- **Binary runtime:** Bun 1.3.14 / Node v24.3.0 (confirmed via `strings` on the binary)

---

## Error

```
API Error: The socket connection was closed unexpectedly.
For more information, pass `verbose: true` in the second argument to fetch()
```

The error message itself is a raw Bun/JSC runtime string (hardcoded in the JSC engine section
of the binary). It surfaces with no actionable guidance and no automatic retry.

---

## Root Cause Analysis

### Finding 1: Bun does not set `SO_KEEPALIVE` on its TCP sockets

Confirmed live via `ss -tnop state established '( dport = :443 )'`:

```
# Every other application on the system:
chrome  → 34.194.3.76:443    timer:(keepalive,16sec,0)   ← SO_KEEPALIVE ON
code    → 4.228.31.153:443   timer:(keepalive,39sec,0)   ← SO_KEEPALIVE ON

# Claude Code (before workaround):
claude  → 160.79.104.10:443  (no timer)                  ← SO_KEEPALIVE NOT SET
claude  → 2607:6bc0::10:443  (no timer)                  ← SO_KEEPALIVE NOT SET
```

Without `SO_KEEPALIVE`, idle TCP connections receive no probe packets. During agentic tasks,
the HTTP/2 connection sits idle while tools execute locally. That idle window is long enough
for the Anthropic server, Cloudflare, or intermediate router NAT to silently drop the connection.
When Claude attempts the next API call on the dropped connection, Bun throws the error.

### Finding 2: All application-level keepalives are disabled via GrowthBook feature flags

Inspecting `~/.claude.json` (`cachedGrowthBookFeatures`):

```json
"tengu_bridge_poll_interval_config": {
  "heartbeat_interval_ms": 0,
  "session_keepalive_interval_ms": 0,
  "session_keepalive_interval_v2_ms": 0
}
```

All three keepalive/heartbeat intervals are `0`. There is no fallback mechanism at the
application layer when the TCP layer provides none.

The environment variable `CLAUDE_CODE_REMOTE_SEND_KEEPALIVES` exists in the binary and
appears to override this, but it is not documented and users cannot be expected to discover it.

### Finding 3: Stale connection retry only fires for background agents, not CLI

Binary strings show two distinct code paths:

```
tengu_streaming_stale_connection_retry   ← exists for background agents
cli_nonstreaming_fallback_started        ← exists for CLI
Error streaming (non-streaming fallback disabled):
```

In practice, the CLI path does not recover — the error propagates directly to the user with
no retry. Background agents have a retry path; CLI sessions do not.

### Finding 4: `NODE_OPTIONS=--dns-result-order=ipv4first` is not fully honored by Bun

After setting `NODE_OPTIONS=--dns-result-order=ipv4first` as a workaround, active connections
still include IPv6:

```
192.168.1.150:36660   → 160.79.104.10:443       ← IPv4 (api.anthropic.com)
[2804:...]:47658      → [2607:6bc0::10]:443      ← IPv6 (api.anthropic.com) — still present
[2804:...]:56560      → [2600:1901:0:3084::]:443 ← IPv6 (other Claude service)
```

Bun uses its own native DNS resolution for some code paths, bypassing Node.js's dns module
settings. The flag has partial effect only.

### Finding 5: Error persists after forcing `SO_KEEPALIVE` via LD_PRELOAD

As a workaround, `SO_KEEPALIVE` was forced on all sockets via an LD_PRELOAD shim:

```c
int socket(int domain, int type, int protocol) {
    int fd = orig_socket(domain, type, protocol);
    if (fd >= 0 && (type & 0xf) == SOCK_STREAM) {
        int opt = 1;
        setsockopt(fd, SOL_SOCKET, SO_KEEPALIVE, &opt, sizeof(opt));
    }
    return fd;
}
```

After applying this, `ss -tnop` confirms keepalive timers are now active on all claude sockets.
A stress test (two consecutive 90-second idle windows) passed successfully.

**However, the error continued to occur during shorter tasks.** This indicates a second,
independent cause: the Bun HTTP/2 client does not gracefully handle server-initiated connection
closure (HTTP/2 `GOAWAY` frame or TCP `RST`) and surfaces it as a fatal unrecoverable error
instead of transparently retrying on a new connection.

---

## Reproduction

Run a long agentic task with multiple tool-call turns and significant idle time between turns:

```bash
claude --dangerously-skip-permissions -p "Run one at a time:
1. date
2. python3 -c \"import time; time.sleep(90); print('survived 90s')\"
3. python3 -c \"import time; time.sleep(90); print('survived second 90s')\"
4. date"
```

Without fixes: fails during step 2 or 3 with the socket error.  
With LD_PRELOAD SO_KEEPALIVE fix: passes (3m21s, both sleeps survived).  
During normal interactive agentic use: still fails intermittently even with the fix.

---

## Suggested Fixes (for Anthropic)

**Fix 1 — Set `SO_KEEPALIVE` on API sockets (one line, highest impact):**
```js
socket.setKeepAlive(true, 30000); // or equivalent in Bun's net API
```
This is the single most impactful change. Chrome and VS Code both do this; Claude Code does not.

**Fix 2 — Enable `heartbeat_interval_ms` by default for CLI sessions:**
The GrowthBook flag currently forces `0` for all keepalive intervals. CLI sessions should
have a non-zero default (e.g. 30s) independent of the server-side feature flag value.

**Fix 3 — Implement transparent retry on stale connection for CLI:**
The background agent path (`tengu_streaming_stale_connection_retry`) already handles this.
The CLI path should get the same treatment instead of surfacing a fatal error.

**Fix 4 — Handle HTTP/2 `GOAWAY` gracefully:**
When the server closes an HTTP/2 connection (normal lifecycle behavior), Bun should
transparently open a new connection and retry the request rather than propagating the
low-level socket error to the user.

**Fix 5 — Improve the error message:**
`"pass verbose: true in the second argument to fetch()"` is a raw Bun internal error.
Users cannot act on this. At minimum it should say the session can be resumed with `--continue`.

---

## Workaround (for users until fixed)

Add to `~/.zshrc` or `~/.bashrc`:

```bash
export CLAUDE_CODE_REMOTE_SEND_KEEPALIVES=true
export BUN_CONFIG_HTTP_IDLE_TIMEOUT=300
export BUN_CONFIG_HTTP_RETRY_COUNT=3
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=120000
export NODE_OPTIONS="--dns-result-order=ipv4first"
```

For a more reliable fix, also apply the `SO_KEEPALIVE` shim:

```bash
cat > /tmp/ka.c << 'EOF'
#define _GNU_SOURCE
#include <stddef.h>
#include <sys/socket.h>
#include <dlfcn.h>
int socket(int domain, int type, int protocol) {
    static int (*orig)(int,int,int);
    if (!orig) orig = dlsym(RTLD_NEXT, "socket");
    int fd = orig(domain, type, protocol);
    if (fd >= 0 && (type & 0xf) == SOCK_STREAM) {
        int v = 1;
        setsockopt(fd, SOL_SOCKET, SO_KEEPALIVE, &v, sizeof(v));
    }
    return fd;
}
EOF
gcc -shared -fPIC -O2 -o ~/.local/lib/libkeepalive.so /tmp/ka.c -ldl
echo 'export LD_PRELOAD="$HOME/.local/lib/libkeepalive.so${LD_PRELOAD:+:$LD_PRELOAD}"' >> ~/.zshrc
```

Also lower the TCP keepalive probe interval (requires sudo):
```bash
sudo sysctl -w net.ipv4.tcp_keepalive_time=60
echo "net.ipv4.tcp_keepalive_time=60" | sudo tee /etc/sysctl.d/99-claude-keepalive.conf
```

---

## Evidence References

| Finding | Method | Confirmed |
|---|---|---|
| No `SO_KEEPALIVE` on claude sockets | `ss -tnop` live output | ✅ |
| All keepalives at 0ms | `~/.claude.json` GrowthBook cache | ✅ |
| Binary is Bun 1.3.14 | `strings` on binary | ✅ |
| Error is Bun/JSC hardcoded string | `strings` on binary, line 42426 | ✅ |
| stale-connection retry missing for CLI | `strings` code path analysis | ✅ |
| IPv6 connections despite ipv4first flag | `ss -tnop` after applying `NODE_OPTIONS` | ✅ |
| Error persists after `SO_KEEPALIVE` forced | Live reproduction during diagnostic session | ✅ |
| 90s idle stress test passes with shim | Controlled test, two 90s windows | ✅ |

# Comments on anthropics/claude-code#60133
Total: 13 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-18T06:34:10Z

Found 2 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/47059
2. https://github.com/anthropics/claude-code/issues/37078

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: brunos3d
Date: 2026-05-18T06:51:50Z

## Cross-issue index + evidence that this is a server-side regression, not a user environment problem

After reviewing all related open issues and their workarounds, I want to make the case that **this is a server-side regression affecting all users**, and that the root cause and fix are now fully understood.

---

### Related issues — same root cause, different symptoms

| Issue | Platform | Status | Workaround found by users |
|---|---|---|---|
| #5674 | macOS | Open (38 comments, since Aug 2025) | Cloudflare Warp VPN, MTU reduction, removing Tailscale |
| #28557 | macOS/cross | Open (10 comments) | Disabling IPv6, MTU to 1492 |
| #37077 | macOS | Open | None |
| #49761 | macOS | Open | None |
| #52899 | macOS | Open, stale | None |
| #54287 | cross | Closed as duplicate | None |
| #56017 | macOS | Open | None |
| #56059 | macOS | Open | Full system reboot |
| #60133 (this issue) | **Linux** | Open | **Full root cause identified — see below** |

Every single one of these is the same failure: **an idle HTTP/2 TCP connection is silently dropped, and Claude Code crashes instead of reconnecting.**

The reason they look like different problems (VPNs, MTU, IPv6, Docker, Tailscale) is that users are accidentally changing their network routing in ways that affect how quickly idle connections get dropped — not fixing the actual cause.

---

### Why users think it's their environment (it isn't)

- **"Disabling IPv6 fixed it"** → `api.anthropic.com` resolves IPv6-first via `getaddrinfo`. IPv6 paths through home routers tend to have shorter stateful firewall idle timeouts than IPv4 NAT. Switching to IPv4 just buys more time before the same drop occurs.
- **"Lowering MTU to 1450/1492 fixed it"** → Changes routing path selection, which incidentally picks a path with a longer idle timeout. Not a real fix.
- **"Removing Tailscale/TunnelBear fixed it"** → Those VPNs set `tcp.mssdflt=512`, causing packet fragmentation. But Cloudflare Warp *also* fixes it — because Warp's tunnel enforces its own keepalive, compensating for the missing `SO_KEEPALIVE` in the Claude binary.
- **"Full reboot fixed it"** → Clears TCP state tables and re-establishes fresh connections. Temporary fix only.
- **"Only happens on macOS, not Linux/Windows"** → macOS has more aggressive TCP defaults (`blackhole=1`, shorter NAT timeouts) that expose the missing keepalive faster. On Linux the connection survives slightly longer, but the same drop eventually happens.

---

### The actual root cause (confirmed via binary analysis on Linux)

**The Claude Code binary (Bun 1.3.14) does not set `SO_KEEPALIVE` on its TCP sockets.**

Confirmed live via `ss -tnop`:
```
# Every other process on the system:
chrome  → api:443   timer:(keepalive,16sec,0)   ← SO_KEEPALIVE ON
vscode  → api:443   timer:(keepalive,39sec,0)   ← SO_KEEPALIVE ON

# Claude Code:
claude  → api:443   (no timer)                  ← SO_KEEPALIVE NOT SET
```

Without `SO_KEEPALIVE`, the kernel never sends probe packets on idle connections. The HTTP/2 TCP connection is shared across multiple request/response cycles. Between API turns (while tools execute locally), the connection sits completely idle. After enough idle time, the server or any stateful device in the path silently closes it. Bun discovers this only when it tries to write to the dead socket → "socket connection was closed unexpectedly."

This is compounded by a **server-side configuration** found in `~/.claude.json` (GrowthBook feature flags):
```json
"heartbeat_interval_ms": 0,
"session_keepalive_interval_ms": 0,
"session_keepalive_interval_v2_ms": 0
```

**All application-level keepalives are explicitly set to zero.** The binary has the infrastructure for keepalives (`CLAUDE_CODE_REMOTE_SEND_KEEPALIVES` env var, heartbeat timer, session keepalive timer), but the server-side feature flags disable them entirely. This appears to be a **regression introduced around v2.1.126→v2.1.143**, consistent with @romancone's report that 2.1.126 worked and 2.1.143 does not — the binary code didn't change, the feature flags did.

---

### Why this is Anthropic's fix to make (not users')

The fix on Anthropic's side is a **one-liner**:

```js
socket.setKeepAlive(true, 30000);
```

Set `SO_KEEPALIVE` on the API socket. That's it. Chrome does it. VS Code does it. Every HTTP client library does it by default. The Claude binary doesn't.

Additionally:
1. **Re-enable heartbeat/keepalive feature flags** — `heartbeat_interval_ms: 0` removes the last fallback. Even a 30-second heartbeat would prevent the majority of these failures.
2. **Implement stale connection retry for CLI sessions** — the binary already has `tengu_streaming_stale_connection_retry` for background agents. CLI sessions need the same path instead of surfacing a fatal unrecoverable error.
3. **Handle HTTP/2 GOAWAY gracefully** — when the server closes an HTTP/2 connection (normal lifecycle), Bun should transparently reconnect rather than crashing the session.

---

### Working workaround for all affected users (Linux and macOS)

```bash
# Add to ~/.zshrc or ~/.bashrc
export CLAUDE_CODE_REMOTE_SEND_KEEPALIVES=true
export BUN_CONFIG_HTTP_IDLE_TIMEOUT=300
export BUN_CONFIG_HTTP_RETRY_COUNT=3
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=120000
export NODE_OPTIONS="--dns-result-order=ipv4first"
```

For a complete OS-level fix that forces `SO_KEEPALIVE` on every TCP socket Claude opens:

```bash
# Build a small LD_PRELOAD shim (Linux; works on macOS with minor changes)
cat > /tmp/ka.c << 'CSRC'
#define _GNU_SOURCE
#include <stddef.h>
#include <sys/socket.h>
#include <dlfcn.h>
int socket(int domain, int type, int protocol) {
    static int (*orig)(int,int,int);
    if (!orig) orig = dlsym(RTLD_NEXT, "socket");
    int fd = orig(domain, type, protocol);
    if (fd >= 0 && (type & 0xf) == SOCK_STREAM) {
        int v = 1; setsockopt(fd, SOL_SOCKET, SO_KEEPALIVE, &v, sizeof(v));
    }
    return fd;
}
CSRC
mkdir -p ~/.local/lib
gcc -shared -fPIC -O2 -o ~/.local/lib/libkeepalive.so /tmp/ka.c -ldl
echo 'export LD_PRELOAD="$HOME/.local/lib/libkeepalive.so${LD_PRELOAD:+:$LD_PRELOAD}"' >> ~/.zshrc

# Lower TCP keepalive probe interval
sudo sysctl -w net.ipv4.tcp_keepalive_time=60
echo "net.ipv4.tcp_keepalive_time=60" | sudo tee /etc/sysctl.d/99-claude-keepalive.conf
```

**Verified:** After applying this, all Claude sockets show `timer:(keepalive,Xs,0)` in `ss -tnop`, and two consecutive 90-second idle windows survive without error (3m21s stress test passed).

Full diagnostic report, binary analysis, evidence table, and all commands: #60133

--- Comment 3 ---
Author: jshaofa-ui
Date: 2026-05-18T07:07:51Z

## Proposed Solution

### Root Cause
Two independent causes:
1. **No `SO_KEEPALIVE`** — Bun doesn't set keepalive on TCP sockets, idle connections are silently dropped
2. **No CLI stale-connection retry** — Background agents have `tengu_streaming_stale_connection_retry`, CLI doesn't

### Fix 1: Set `SO_KEEPALIVE` on API sockets (one line, highest impact)
```typescript
socket.setKeepAlive(true, 30000); // 30s keepalive
```

### Fix 2: Enable heartbeat keepalive by default for CLI
```typescript
const defaultKeepalive = {
  heartbeat_interval_ms: 30000,      // was 0
  session_keepalive_interval_ms: 30000,
};
```

### Fix 3: Implement transparent retry on stale connection for CLI
```typescript
async function apiCallWithRetry(request: ApiRequest): Promise<ApiResponse> {
  for (let attempt = 0; attempt < 3; attempt++) {
    try { return await apiCall(request); }
    catch (err) {
      if (isStaleConnectionError(err) && attempt < 2) {
        await resetConnection(); continue;
      }
      throw err;
    }
  }
}
```

### Fix 4: Improve error message
Replace raw Bun error with actionable guidance: "Connection lost. Try `claude --continue` to resume."

### Impact
- **Severity:** High — breaks long agentic sessions
- **Users Affected:** All CLI users with long-running sessions
- **Fix Complexity:** Low-Medium (Fix 1 is one line)
- **Risk:** Low — additive changes, retry is idempotent

Full solution: `solutions/claude-code-60133-socket-connection-closed-fix.md`

--- Comment 4 ---
Author: brunos3d
Date: 2026-05-18T07:17:17Z

@jshaofa-ui Your analysis is correct and aligns exactly with what we confirmed through live diagnostics on this issue.

A few notes from our investigation:

- **Fix 1** is the single highest-impact change — one call to `socket.setKeepAlive(true, 30000)` would resolve the majority of cases. Chrome and VS Code both do this; Claude Code does not.
- **Fix 2** is critical because even if the binary sets keepalives, the GrowthBook flags (`heartbeat_interval_ms: 0`, `session_keepalive_interval_ms: 0`) override everything at the application layer. CLI sessions need a non-zero default that is independent of server-side flag values.
- **Fix 3** is the proper long-term solution — the background agent path already has `tengu_streaming_stale_connection_retry`; the CLI path just propagates the error with no recovery.
- **Fix 4** is low-effort but important: the current message (`pass verbose: true in the second argument to fetch()`) is a raw Bun internal string that users cannot act on at all.

We also confirmed via `ss -tnop` that `NODE_OPTIONS=--dns-result-order=ipv4first` has partial effect only — Bun uses its own native DNS resolution for some code paths and bypasses the Node.js dns module entirely.

While Anthropic works on the proper fix, we've put together a user-side workaround script that applies all four mitigations (env vars, SO_KEEPALIVE LD_PRELOAD shim, sysctl tuning, persistence across reboots) for both Linux and macOS. Posting it in the next comment.


--- Comment 5 ---
Author: brunos3d
Date: 2026-05-18T07:18:21Z

## User-side Workaround Scripts

> ⚠️ **Disclaimer — Read before running**
>
> These scripts make OS-level changes (environment variables, a compiled C shim loaded via `LD_PRELOAD`/`DYLD_INSERT_LIBRARIES`, and kernel TCP sysctl parameters). They are an **advanced workaround** for a confirmed bug that should be fixed in the Claude Code binary itself. Each user's environment is different — review every step before confirming it. Changes that are safe on a personal workstation may have unintended side effects on servers, containers, or systems with custom network stacks (VPNs, firewalls, custom routing). The scripts are fully reversible via the uninstall script below, but **use at your own risk**.

---

Two scripts — an installer and a full revert. Each phase is optional and prompts for `Y/n` before making any change.

**Tested on:** Arch Linux (Manjaro) kernel 6.12, Claude Code 2.1.143, Bun 1.3.14. macOS paths and compile flags are included but less battle-tested.

---

### Install: `claude-keepalive-fix.sh`

```bash
# Download and run (Linux / macOS)
curl -fsSL https://gist.githubusercontent.com/brunos3d/66abd16661cfcfd4b5a943b4baf96f24/raw/claude-keepalive-fix.sh -o claude-keepalive-fix.sh
chmod +x claude-keepalive-fix.sh
./claude-keepalive-fix.sh
# Phase 3 and 4 will prompt for sudo — only for sysctl changes
```

> Full gist (both scripts): https://gist.github.com/brunos3d/66abd16661cfcfd4b5a943b4baf96f24

**What each phase does:**

| Phase | Change | Reversible |
|-------|--------|-----------|
| 1 | Adds `CLAUDE_CODE_REMOTE_SEND_KEEPALIVES`, `BUN_CONFIG_HTTP_IDLE_TIMEOUT`, etc. to your shell config | ✅ by uninstall script |
| 2 | Compiles a ~15KB C shim that forces `SO_KEEPALIVE=1` on every TCP socket via `LD_PRELOAD` | ✅ by uninstall script |
| 3 | Sets `net.ipv4.tcp_keepalive_time=60` (Linux) or fixes `mssdflt`/`blackhole` (macOS) via `sysctl` | ✅ resets on reboot or via uninstall |
| 4 | Persists the sysctl value across reboots | ✅ by uninstall script |

<details>
<summary><strong>claude-keepalive-fix.sh (click to expand)</strong></summary>

```bash
#!/usr/bin/env bash
# =============================================================================
# claude-keepalive-fix.sh
# Workaround for: "API Error: The socket connection was closed unexpectedly"
# GitHub issue: https://github.com/anthropics/claude-code/issues/60133
#
# This script applies OS-level TCP keepalive fixes that compensate for
# the Claude Code binary (Bun 1.3.14) not setting SO_KEEPALIVE on its
# TCP sockets, combined with Anthropic's server-side keepalive flags
# being set to 0ms via GrowthBook feature flags.
#
# Supports: Linux, macOS
# Requires: gcc or clang, sudo (for sysctl phase only)
# =============================================================================

set -uo pipefail

# ── colours ──────────────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; BOLD='\033[1m'; DIM='\033[2m'; NC='\033[0m'

info()    { echo -e "${BLUE}[INFO]${NC} $*"; }
success() { echo -e "${GREEN}[OK]${NC}   $*"; }
warn()    { echo -e "${YELLOW}[WARN]${NC} $*"; }
error()   { echo -e "${RED}[ERR]${NC}  $*"; }
step()    { echo -e "\n${BOLD}${BLUE}▶ $*${NC}"; }
dim()     { echo -e "${DIM}  $*${NC}"; }

ask() {
    local prompt="$1"
    echo -e "\n${BOLD}${YELLOW}?${NC} ${BOLD}${prompt}${NC} ${DIM}[Y/n]${NC} "
    read -r -n1 reply 2>/dev/null || read -r reply
    echo
    [[ "$reply" =~ ^[Yy]$ ]] || [[ -z "$reply" ]]
}

# ── detect OS ────────────────────────────────────────────────────────────────
OS="$(uname -s)"
ARCH="$(uname -m)"

if [[ "$OS" == "Darwin" ]]; then
    PLATFORM="macOS"
    LIB_EXT="dylib"
    LIB_FLAG="-dynamiclib"
    PRELOAD_VAR="DYLD_INSERT_LIBRARIES"
    CC="clang"
elif [[ "$OS" == "Linux" ]]; then
    PLATFORM="Linux"
    LIB_EXT="so"
    LIB_FLAG="-shared -fPIC"
    PRELOAD_VAR="LD_PRELOAD"
    CC="gcc"
else
    error "Unsupported OS: $OS. Only Linux and macOS are supported."
    exit 1
fi

# ── detect shell config ───────────────────────────────────────────────────────
detect_shell_config() {
    local shell_name
    shell_name="$(basename "${SHELL:-bash}")"
    if [[ "$shell_name" == "zsh" ]]; then
        echo "${ZDOTDIR:-$HOME}/.zshrc"
    elif [[ "$shell_name" == "bash" ]]; then
        if [[ "$PLATFORM" == "macOS" ]]; then
            echo "$HOME/.bash_profile"
        else
            echo "$HOME/.bashrc"
        fi
    else
        echo "$HOME/.profile"
    fi
}

SHELL_CONFIG="$(detect_shell_config)"
LIB_DIR="$HOME/.local/lib"
LIB_FILE="$LIB_DIR/libkeepalive.$LIB_EXT"
MARKER="# claude-keepalive-fix — managed block"

# ── header ───────────────────────────────────────────────────────────────────
echo
echo -e "${BOLD}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║         Claude Code — Socket Keepalive Fix  v1.0            ║${NC}"
echo -e "${BOLD}╚══════════════════════════════════════════════════════════════╝${NC}"
echo
echo -e "  Platform : ${BOLD}$PLATFORM${NC} ($ARCH)"
echo -e "  Shell cfg: ${BOLD}$SHELL_CONFIG${NC}"
echo -e "  Library  : ${BOLD}$LIB_FILE${NC}"
echo
echo -e "  This script applies ${BOLD}4 independent fixes${NC}. Each one is optional"
echo -e "  and will ask for confirmation before making any change."
echo -e "  To revert everything, run: ${BOLD}claude-keepalive-uninstall.sh${NC}"
echo
echo -e "  Issue ref: ${DIM}https://github.com/anthropics/claude-code/issues/60133${NC}"
echo
echo -e "${YELLOW}  ⚠  Read each step before confirming. Some steps require sudo.${NC}"
echo

# ── phase 1: environment variables ───────────────────────────────────────────
step "Phase 1 of 4 — Environment variables"
echo
echo -e "  Adds the following exports to ${BOLD}$SHELL_CONFIG${NC}:"
echo
echo -e "  ${DIM}CLAUDE_CODE_REMOTE_SEND_KEEPALIVES=true${NC}"
dim "    Enables application-level session keepalives in Claude Code"
echo -e "  ${DIM}BUN_CONFIG_HTTP_IDLE_TIMEOUT=300${NC}"
dim "    Extends Bun's HTTP connection pool idle timeout to 5 minutes"
echo -e "  ${DIM}BUN_CONFIG_HTTP_RETRY_COUNT=3${NC}"
dim "    Enables automatic HTTP retry on connection failure"
echo -e "  ${DIM}CLAUDE_STREAM_IDLE_TIMEOUT_MS=120000${NC}"
dim "    Extends the stream idle watchdog timeout to 2 minutes"
echo -e "  ${DIM}NODE_OPTIONS=--dns-result-order=ipv4first${NC}"
dim "    Prefers IPv4 over IPv6 for DNS results (more stable NAT path)"
echo

if ask "Apply environment variable fixes to $SHELL_CONFIG?"; then
    # Check if already applied
    if grep -q "$MARKER" "$SHELL_CONFIG" 2>/dev/null; then
        warn "Env vars block already present in $SHELL_CONFIG — skipping."
    else
        cat >> "$SHELL_CONFIG" << ENVBLOCK

$MARKER — begin
export CLAUDE_CODE_REMOTE_SEND_KEEPALIVES=true
export BUN_CONFIG_HTTP_IDLE_TIMEOUT=300
export BUN_CONFIG_HTTP_RETRY_COUNT=3
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=120000
export NODE_OPTIONS="--dns-result-order=ipv4first"
$MARKER — end
ENVBLOCK
        success "Environment variables written to $SHELL_CONFIG"
    fi
else
    warn "Skipped — env vars not applied."
fi

# ── phase 2: SO_KEEPALIVE shim ───────────────────────────────────────────────
step "Phase 2 of 4 — SO_KEEPALIVE LD_PRELOAD shim"
echo
echo -e "  Compiles a small C library (${BOLD}~15KB${NC}) that intercepts every"
echo -e "  TCP socket() call and forces ${BOLD}SO_KEEPALIVE=1${NC} before returning it."
echo
echo -e "  Without this, the OS kernel never sends keepalive probe packets"
echo -e "  on Claude's idle connections, even with tcp_keepalive_time set."
echo
echo -e "  The library is installed to: ${BOLD}$LIB_FILE${NC}"
echo -e "  ${PRELOAD_VAR} is added to your shell config so Claude picks it up."
echo
echo -e "  ${DIM}Requires: $CC${NC}"
echo

if ! command -v "$CC" &>/dev/null; then
    if [[ "$PLATFORM" == "macOS" ]] && command -v clang &>/dev/null; then
        CC="clang"
    else
        warn "$CC not found. Install build tools and re-run this phase."
        warn "  macOS: xcode-select --install"
        warn "  Debian/Ubuntu: sudo apt install gcc"
        warn "  Arch: sudo pacman -S gcc"
        warn "Skipping Phase 2."
        CC=""
    fi
fi

if [[ -n "${CC:-}" ]]; then
    if ask "Build and install the SO_KEEPALIVE shim?"; then
        mkdir -p "$LIB_DIR"

        # Write the C source
        cat > /tmp/claude_keepalive.c << 'CSRC'
#define _GNU_SOURCE
#include <stddef.h>
#include <sys/socket.h>
#include <dlfcn.h>

/*
 * Intercepts socket() and forces SO_KEEPALIVE on every SOCK_STREAM fd.
 * Installed via LD_PRELOAD (Linux) / DYLD_INSERT_LIBRARIES (macOS).
 * See: https://github.com/anthropics/claude-code/issues/60133
 */
int socket(int domain, int type, int protocol) {
    static int (*orig_socket)(int, int, int) = NULL;
    if (!orig_socket)
        orig_socket = dlsym(RTLD_NEXT, "socket");
    int fd = orig_socket(domain, type, protocol);
    if (fd >= 0 && (type & 0xf) == SOCK_STREAM) {
        int opt = 1;
        setsockopt(fd, SOL_SOCKET, SO_KEEPALIVE, &opt, sizeof(opt));
    }
    return fd;
}
CSRC

        # Compile
        if [[ "$PLATFORM" == "macOS" ]]; then
            $CC -dynamiclib -O2 -o "$LIB_FILE" /tmp/claude_keepalive.c 2>&1
        else
            $CC -shared -fPIC -O2 -o "$LIB_FILE" /tmp/claude_keepalive.c -ldl 2>&1
        fi

        if [[ -f "$LIB_FILE" ]]; then
            success "Library built: $LIB_FILE ($(du -sh "$LIB_FILE" | cut -f1))"

            # Add PRELOAD to shell config (inside the managed block if it exists, else append)
            if grep -q "$MARKER" "$SHELL_CONFIG" 2>/dev/null; then
                # Insert before the end marker
                if [[ "$PLATFORM" == "macOS" ]]; then
                    sed -i '' "/$MARKER — end/i\\
export ${PRELOAD_VAR}=\"\$HOME/.local/lib/libkeepalive.${LIB_EXT}\${${PRELOAD_VAR}:+:\$${PRELOAD_VAR}}\"
" "$SHELL_CONFIG"
                else
                    sed -i "/$MARKER — end/i export ${PRELOAD_VAR}=\"\$HOME/.local/lib/libkeepalive.${LIB_EXT}\${${PRELOAD_VAR}:+:\$${PRELOAD_VAR}}\"" "$SHELL_CONFIG"
                fi
            else
                cat >> "$SHELL_CONFIG" << PRELOADBLOCK

$MARKER — begin
export ${PRELOAD_VAR}="\$HOME/.local/lib/libkeepalive.${LIB_EXT}\${${PRELOAD_VAR}:+:\$${PRELOAD_VAR}}"
$MARKER — end
PRELOADBLOCK
            fi
            success "${PRELOAD_VAR} added to $SHELL_CONFIG"
        else
            error "Compilation failed. Check that $CC is properly installed."
        fi
        rm -f /tmp/claude_keepalive.c
    else
        warn "Skipped — SO_KEEPALIVE shim not installed."
    fi
fi

# ── phase 3: sysctl tcp_keepalive_time ───────────────────────────────────────
step "Phase 3 of 4 — TCP keepalive probe interval (requires sudo)"
echo
if [[ "$PLATFORM" == "Linux" ]]; then
    CURRENT_KA="$(cat /proc/sys/net/ipv4/tcp_keepalive_time 2>/dev/null || echo unknown)"
    echo -e "  Current ${BOLD}net.ipv4.tcp_keepalive_time${NC} = $CURRENT_KA seconds"
    echo
    echo -e "  This controls how long a TCP connection can be idle before the"
    echo -e "  kernel starts sending keepalive probe packets."
    echo -e "  The default is ${BOLD}120s${NC}. This script sets it to ${BOLD}60s${NC}."
    echo
    echo -e "  Only takes effect alongside Phase 2 (SO_KEEPALIVE shim)."
    echo -e "  ${DIM}Requires: sudo${NC}"
    echo
    if ask "Set tcp_keepalive_time=60 (requires sudo)?"; then
        sudo sysctl -w net.ipv4.tcp_keepalive_time=60
        success "tcp_keepalive_time set to 60 seconds (active now)"
    else
        warn "Skipped — tcp_keepalive_time not changed."
    fi
elif [[ "$PLATFORM" == "macOS" ]]; then
    CURRENT_MSS="$(sysctl -n net.inet.tcp.mssdflt 2>/dev/null || echo unknown)"
    CURRENT_BH="$(sysctl -n net.inet.tcp.blackhole 2>/dev/null || echo unknown)"
    echo -e "  Current ${BOLD}net.inet.tcp.mssdflt${NC} = $CURRENT_MSS  (should be 1440, not 512)"
    echo -e "  Current ${BOLD}net.inet.tcp.blackhole${NC} = $CURRENT_BH  (should be 0)"
    echo
    echo -e "  macOS has non-standard TCP defaults that worsen socket drops:"
    echo -e "  ${BOLD}mssdflt=512${NC} fragments packets (VPNs like Tailscale set this)"
    echo -e "  ${BOLD}blackhole=1${NC} silently drops packets instead of sending RST"
    echo
    echo -e "  This step corrects both values. ${DIM}Requires: sudo${NC}"
    echo
    if ask "Fix macOS TCP defaults (requires sudo)?"; then
        sudo sysctl -w net.inet.tcp.mssdflt=1440
        sudo sysctl -w net.inet.tcp.blackhole=0
        sudo sysctl -w net.inet.tcp.delayed_ack=0
        success "macOS TCP sysctl values corrected"
    else
        warn "Skipped — macOS TCP defaults not changed."
    fi
fi

# ── phase 4: persist sysctl across reboots ───────────────────────────────────
step "Phase 4 of 4 — Persist sysctl settings across reboots (requires sudo)"
echo
if [[ "$PLATFORM" == "Linux" ]]; then
    SYSCTL_FILE="/etc/sysctl.d/99-claude-keepalive.conf"
    echo -e "  Writes ${BOLD}$SYSCTL_FILE${NC} so the keepalive time"
    echo -e "  survives reboots. Without this, Phase 3 resets on next boot."
    echo -e "  ${DIM}Requires: sudo${NC}"
    echo
    if ask "Persist tcp_keepalive_time=60 to $SYSCTL_FILE?"; then
        echo "net.ipv4.tcp_keepalive_time=60" | sudo tee "$SYSCTL_FILE" > /dev/null
        success "Persisted to $SYSCTL_FILE"
    else
        warn "Skipped — sysctl will reset on next reboot."
    fi
elif [[ "$PLATFORM" == "macOS" ]]; then
    PLIST="/Library/LaunchDaemons/com.claude.tcp-tuning.plist"
    echo -e "  Creates a LaunchDaemon plist ${BOLD}$PLIST${NC}"
    echo -e "  to re-apply the TCP fixes on every boot. ${DIM}Requires: sudo${NC}"
    echo
    if ask "Create LaunchDaemon to persist macOS TCP fixes?"; then
        sudo tee "$PLIST" > /dev/null << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>       <string>com.claude.tcp-tuning</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/sbin/sysctl</string>
    <string>net.inet.tcp.mssdflt=1440</string>
    <string>net.inet.tcp.blackhole=0</string>
    <string>net.inet.tcp.delayed_ack=0</string>
  </array>
  <key>RunAtLoad</key>   <true/>
</dict>
</plist>
PLIST
        sudo launchctl load "$PLIST" 2>/dev/null || true
        success "LaunchDaemon installed: $PLIST"
    else
        warn "Skipped — sysctl will reset on next reboot."
    fi
fi

# ── done ─────────────────────────────────────────────────────────────────────
echo
echo -e "${BOLD}${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}${GREEN}║                      All phases complete                     ║${NC}"
echo -e "${BOLD}${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo
echo -e "  ${BOLD}To activate in the current terminal:${NC}"
echo -e "  ${DIM}source $SHELL_CONFIG${NC}"
echo
echo -e "  ${BOLD}To verify the fix is working:${NC}"
echo -e "  ${DIM}ss -tnop state established '( dport = :443 )' | grep claude${NC}"
echo -e "  ${DIM}→ You should see timer:(keepalive,...) on all claude connections${NC}"
echo
echo -e "  ${BOLD}To revert all changes:${NC}"
echo -e "  ${DIM}bash claude-keepalive-uninstall.sh${NC}"
echo
echo -e "  ${DIM}Issue: https://github.com/anthropics/claude-code/issues/60133${NC}"
echo

```

</details>

---

### Uninstall / Revert: `claude-keepalive-uninstall.sh`

Run this if Anthropic ships a fix or if you want to roll back all changes:

```bash
curl -fsSL https://gist.githubusercontent.com/brunos3d/66abd16661cfcfd4b5a943b4baf96f24/raw/claude-keepalive-uninstall.sh -o claude-keepalive-uninstall.sh
chmod +x claude-keepalive-uninstall.sh
./claude-keepalive-uninstall.sh
# Phase 3 will prompt for sudo to reset sysctl and remove the persist file
```

<details>
<summary><strong>claude-keepalive-uninstall.sh (click to expand)</strong></summary>

```bash
UN#!/usr/bin/env bash
# =============================================================================
# claude-keepalive-fix.sh
# Workaround for: "API Error: The socket connection was closed unexpectedly"
# GitHub issue: https://github.com/anthropics/claude-code/issues/60133
#
# This script applies OS-level TCP keepalive fixes that compensate for
# the Claude Code binary (Bun 1.3.14) not setting SO_KEEPALIVE on its
# TCP sockets, combined with Anthropic's server-side keepalive flags
# being set to 0ms via GrowthBook feature flags.
#
# Supports: Linux, macOS
# Requires: gcc or clang, sudo (for sysctl phase only)
# =============================================================================

set -uo pipefail

# ── colours ──────────────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; BOLD='\033[1m'; DIM='\033[2m'; NC='\033[0m'

info()    { echo -e "${BLUE}[INFO]${NC} $*"; }
success() { echo -e "${GREEN}[OK]${NC}   $*"; }
warn()    { echo -e "${YELLOW}[WARN]${NC} $*"; }
error()   { echo -e "${RED}[ERR]${NC}  $*"; }
step()    { echo -e "\n${BOLD}${BLUE}▶ $*${NC}"; }
dim()     { echo -e "${DIM}  $*${NC}"; }

ask() {
    local prompt="$1"
    echo -e "\n${BOLD}${YELLOW}?${NC} ${BOLD}${prompt}${NC} ${DIM}[Y/n]${NC} "
    read -r -n1 reply 2>/dev/null || read -r reply
    echo
    [[ "$reply" =~ ^[Yy]$ ]] || [[ -z "$reply" ]]
}

# ── detect OS ────────────────────────────────────────────────────────────────
OS="$(uname -s)"
ARCH="$(uname -m)"

if [[ "$OS" == "Darwin" ]]; then
    PLATFORM="macOS"
    LIB_EXT="dylib"
    LIB_FLAG="-dynamiclib"
    PRELOAD_VAR="DYLD_INSERT_LIBRARIES"
    CC="clang"
elif [[ "$OS" == "Linux" ]]; then
    PLATFORM="Linux"
    LIB_EXT="so"
    LIB_FLAG="-shared -fPIC"
    PRELOAD_VAR="LD_PRELOAD"
    CC="gcc"
else
    error "Unsupported OS: $OS. Only Linux and macOS are supported."
    exit 1
fi

# ── detect shell config ───────────────────────────────────────────────────────
detect_shell_config() {
    local shell_name
    shell_name="$(basename "${SHELL:-bash}")"
    if [[ "$shell_name" == "zsh" ]]; then
        echo "${ZDOTDIR:-$HOME}/.zshrc"
    elif [[ "$shell_name" == "bash" ]]; then
        if [[ "$PLATFORM" == "macOS" ]]; then
            echo "$HOME/.bash_profile"
        else
            echo "$HOME/.bashrc"
        fi
    else
        echo "$HOME/.profile"
    fi
}

SHELL_CONFIG="$(detect_shell_config)"
LIB_DIR="$HOME/.local/lib"
LIB_FILE="$LIB_DIR/libkeepalive.$LIB_EXT"
MARKER="# claude-keepalive-fix — managed block"

# ── header ───────────────────────────────────────────────────────────────────
echo
echo -e "${BOLD}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║         Claude Code — Socket Keepalive Fix  v1.0            ║${NC}"
echo -e "${BOLD}╚══════════════════════════════════════════════════════════════╝${NC}"
echo
echo -e "  Platform : ${BOLD}$PLATFORM${NC} ($ARCH)"
echo -e "  Shell cfg: ${BOLD}$SHELL_CONFIG${NC}"
echo -e "  Library  : ${BOLD}$LIB_FILE${NC}"
echo
echo -e "  This script applies ${BOLD}4 independent fixes${NC}. Each one is optional"
echo -e "  and will ask for confirmation before making any change."
echo -e "  To revert everything, run: ${BOLD}claude-keepalive-uninstall.sh${NC}"
echo
echo -e "  Issue ref: ${DIM}https://github.com/anthropics/claude-code/issues/60133${NC}"
echo
echo -e "${YELLOW}  ⚠  Read each step before confirming. Some steps require sudo.${NC}"
echo

# ── phase 1: environment variables ───────────────────────────────────────────
step "Phase 1 of 4 — Environment variables"
echo
echo -e "  Adds the following exports to ${BOLD}$SHELL_CONFIG${NC}:"
echo
echo -e "  ${DIM}CLAUDE_CODE_REMOTE_SEND_KEEPALIVES=true${NC}"
dim "    Enables application-level session keepalives in Claude Code"
echo -e "  ${DIM}BUN_CONFIG_HTTP_IDLE_TIMEOUT=300${NC}"
dim "    Extends Bun's HTTP connection pool idle timeout to 5 minutes"
echo -e "  ${DIM}BUN_CONFIG_HTTP_RETRY_COUNT=3${NC}"
dim "    Enables automatic HTTP retry on connection failure"
echo -e "  ${DIM}CLAUDE_STREAM_IDLE_TIMEOUT_MS=120000${NC}"
dim "    Extends the stream idle watchdog timeout to 2 minutes"
echo -e "  ${DIM}NODE_OPTIONS=--dns-result-order=ipv4first${NC}"
dim "    Prefers IPv4 over IPv6 for DNS results (more stable NAT path)"
echo

if ask "Apply environment variable fixes to $SHELL_CONFIG?"; then
    # Check if already applied
    if grep -q "$MARKER" "$SHELL_CONFIG" 2>/dev/null; then
        warn "Env vars block already present in $SHELL_CONFIG — skipping."
    else
        cat >> "$SHELL_CONFIG" << ENVBLOCK

$MARKER — begin
export CLAUDE_CODE_REMOTE_SEND_KEEPALIVES=true
export BUN_CONFIG_HTTP_IDLE_TIMEOUT=300
export BUN_CONFIG_HTTP_RETRY_COUNT=3
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=120000
export NODE_OPTIONS="--dns-result-order=ipv4first"
$MARKER — end
ENVBLOCK
        success "Environment variables written to $SHELL_CONFIG"
    fi
else
    warn "Skipped — env vars not applied."
fi

# ── phase 2: SO_KEEPALIVE shim ───────────────────────────────────────────────
step "Phase 2 of 4 — SO_KEEPALIVE LD_PRELOAD shim"
echo
echo -e "  Compiles a small C library (${BOLD}~15KB${NC}) that intercepts every"
echo -e "  TCP socket() call and forces ${BOLD}SO_KEEPALIVE=1${NC} before returning it."
echo
echo -e "  Without this, the OS kernel never sends keepalive probe packets"
echo -e "  on Claude's idle connections, even with tcp_keepalive_time set."
echo
echo -e "  The library is installed to: ${BOLD}$LIB_FILE${NC}"
echo -e "  ${PRELOAD_VAR} is added to your shell config so Claude picks it up."
echo
echo -e "  ${DIM}Requires: $CC${NC}"
echo

if ! command -v "$CC" &>/dev/null; then
    if [[ "$PLATFORM" == "macOS" ]] && command -v clang &>/dev/null; then
        CC="clang"
    else
        warn "$CC not found. Install build tools and re-run this phase."
        warn "  macOS: xcode-select --install"
        warn "  Debian/Ubuntu: sudo apt install gcc"
        warn "  Arch: sudo pacman -S gcc"
        warn "Skipping Phase 2."
        CC=""
    fi
fi

if [[ -n "${CC:-}" ]]; then
    if ask "Build and install the SO_KEEPALIVE shim?"; then
        mkdir -p "$LIB_DIR"

        # Write the C source
        cat > /tmp/claude_keepalive.c << 'CSRC'
#define _GNU_SOURCE
#include <stddef.h>
#include <sys/socket.h>
#include <dlfcn.h>

/*
 * Intercepts socket() and forces SO_KEEPALIVE on every SOCK_STREAM fd.
 * Installed via LD_PRELOAD (Linux) / DYLD_INSERT_LIBRARIES (macOS).
 * See: https://github.com/anthropics/claude-code/issues/60133
 */
int socket(int domain, int type, int protocol) {
    static int (*orig_socket)(int, int, int) = NULL;
    if (!orig_socket)
        orig_socket = dlsym(RTLD_NEXT, "socket");
    int fd = orig_socket(domain, type, protocol);
    if (fd >= 0 && (type & 0xf) == SOCK_STREAM) {
        int opt = 1;
        setsockopt(fd, SOL_SOCKET, SO_KEEPALIVE, &opt, sizeof(opt));
    }
    return fd;
}
CSRC

        # Compile
        if [[ "$PLATFORM" == "macOS" ]]; then
            $CC -dynamiclib -O2 -o "$LIB_FILE" /tmp/claude_keepalive.c 2>&1
        else
            $CC -shared -fPIC -O2 -o "$LIB_FILE" /tmp/claude_keepalive.c -ldl 2>&1
        fi

        if [[ -f "$LIB_FILE" ]]; then
            success "Library built: $LIB_FILE ($(du -sh "$LIB_FILE" | cut -f1))"

            # Add PRELOAD to shell config (inside the managed block if it exists, else append)
            if grep -q "$MARKER" "$SHELL_CONFIG" 2>/dev/null; then
                # Insert before the end marker
                if [[ "$PLATFORM" == "macOS" ]]; then
                    sed -i '' "/$MARKER — end/i\\
export ${PRELOAD_VAR}=\"\$HOME/.local/lib/libkeepalive.${LIB_EXT}\${${PRELOAD_VAR}:+:\$${PRELOAD_VAR}}\"
" "$SHELL_CONFIG"
                else
                    sed -i "/$MARKER — end/i export ${PRELOAD_VAR}=\"\$HOME/.local/lib/libkeepalive.${LIB_EXT}\${${PRELOAD_VAR}:+:\$${PRELOAD_VAR}}\"" "$SHELL_CONFIG"
                fi
            else
                cat >> "$SHELL_CONFIG" << PRELOADBLOCK

$MARKER — begin
export ${PRELOAD_VAR}="\$HOME/.local/lib/libkeepalive.${LIB_EXT}\${${PRELOAD_VAR}:+:\$${PRELOAD_VAR}}"
$MARKER — end
PRELOADBLOCK
            fi
            success "${PRELOAD_VAR} added to $SHELL_CONFIG"
        else
            error "Compilation failed. Check that $CC is properly installed."
        fi
        rm -f /tmp/claude_keepalive.c
    else
        warn "Skipped — SO_KEEPALIVE shim not installed."
    fi
fi

# ── phase 3: sysctl tcp_keepalive_time ───────────────────────────────────────
step "Phase 3 of 4 — TCP keepalive probe interval (requires sudo)"
echo
if [[ "$PLATFORM" == "Linux" ]]; then
    CURRENT_KA="$(cat /proc/sys/net/ipv4/tcp_keepalive_time 2>/dev/null || echo unknown)"
    echo -e "  Current ${BOLD}net.ipv4.tcp_keepalive_time${NC} = $CURRENT_KA seconds"
    echo
    echo -e "  This controls how long a TCP connection can be idle before the"
    echo -e "  kernel starts sending keepalive probe packets."
    echo -e "  The default is ${BOLD}120s${NC}. This script sets it to ${BOLD}60s${NC}."
    echo
    echo -e "  Only takes effect alongside Phase 2 (SO_KEEPALIVE shim)."
    echo -e "  ${DIM}Requires: sudo${NC}"
    echo
    if ask "Set tcp_keepalive_time=60 (requires sudo)?"; then
        sudo sysctl -w net.ipv4.tcp_keepalive_time=60
        success "tcp_keepalive_time set to 60 seconds (active now)"
    else
        warn "Skipped — tcp_keepalive_time not changed."
    fi
elif [[ "$PLATFORM" == "macOS" ]]; then
    CURRENT_MSS="$(sysctl -n net.inet.tcp.mssdflt 2>/dev/null || echo unknown)"
    CURRENT_BH="$(sysctl -n net.inet.tcp.blackhole 2>/dev/null || echo unknown)"
    echo -e "  Current ${BOLD}net.inet.tcp.mssdflt${NC} = $CURRENT_MSS  (should be 1440, not 512)"
    echo -e "  Current ${BOLD}net.inet.tcp.blackhole${NC} = $CURRENT_BH  (should be 0)"
    echo
    echo -e "  macOS has non-standard TCP defaults that worsen socket drops:"
    echo -e "  ${BOLD}mssdflt=512${NC} fragments packets (VPNs like Tailscale set this)"
    echo -e "  ${BOLD}blackhole=1${NC} silently drops packets instead of sending RST"
    echo
    echo -e "  This step corrects both values. ${DIM}Requires: sudo${NC}"
    echo
    if ask "Fix macOS TCP defaults (requires sudo)?"; then
        sudo sysctl -w net.inet.tcp.mssdflt=1440
        sudo sysctl -w net.inet.tcp.blackhole=0
        sudo sysctl -w net.inet.tcp.delayed_ack=0
        success "macOS TCP sysctl values corrected"
    else
        warn "Skipped — macOS TCP defaults not changed."
    fi
fi

# ── phase 4: persist sysctl across reboots ───────────────────────────────────
step "Phase 4 of 4 — Persist sysctl settings across reboots (requires sudo)"
echo
if [[ "$PLATFORM" == "Linux" ]]; then
    SYSCTL_FILE="/etc/sysctl.d/99-claude-keepalive.conf"
    echo -e "  Writes ${BOLD}$SYSCTL_FILE${NC} so the keepalive time"
    echo -e "  survives reboots. Without this, Phase 3 resets on next boot."
    echo -e "  ${DIM}Requires: sudo${NC}"
    echo
    if ask "Persist tcp_keepalive_time=60 to $SYSCTL_FILE?"; then
        echo "net.ipv4.tcp_keepalive_time=60" | sudo tee "$SYSCTL_FILE" > /dev/null
        success "Persisted to $SYSCTL_FILE"
    else
        warn "Skipped — sysctl will reset on next reboot."
    fi
elif [[ "$PLATFORM" == "macOS" ]]; then
    PLIST="/Library/LaunchDaemons/com.claude.tcp-tuning.plist"
    echo -e "  Creates a LaunchDaemon plist ${BOLD}$PLIST${NC}"
    echo -e "  to re-apply the TCP fixes on every boot. ${DIM}Requires: sudo${NC}"
    echo
    if ask "Create LaunchDaemon to persist macOS TCP fixes?"; then
        sudo tee "$PLIST" > /dev/null << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>       <string>com.claude.tcp-tuning</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/sbin/sysctl</string>
    <string>net.inet.tcp.mssdflt=1440</string>
    <string>net.inet.tcp.blackhole=0</string>
    <string>net.inet.tcp.delayed_ack=0</string>
  </array>
  <key>RunAtLoad</key>   <true/>
</dict>
</plist>
PLIST
        sudo launchctl load "$PLIST" 2>/dev/null || true
        success "LaunchDaemon installed: $PLIST"
    else
        warn "Skipped — sysctl will reset on next reboot."
    fi
fi

# ── done ─────────────────────────────────────────────────────────────────────
echo
echo -e "${BOLD}${GREEN}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}${GREEN}║                      All phases complete                     ║${NC}"
echo -e "${BOLD}${GREEN}╚══════════════════════════════════════════════════════════════╝${NC}"
echo
echo -e "  ${BOLD}To activate in the current terminal:${NC}"
echo -e "  ${DIM}source $SHELL_CONFIG${NC}"
echo
echo -e "  ${BOLD}To verify the fix is working:${NC}"
echo -e "  ${DIM}ss -tnop state established '( dport = :443 )' | grep claude${NC}"
echo -e "  ${DIM}→ You should see timer:(keepalive,...) on all claude connections${NC}"
echo
echo -e "  ${BOLD}To revert all changes:${NC}"
echo -e "  ${DIM}bash claude-keepalive-uninstall.sh${NC}"
echo
echo -e "  ${DIM}Issue: https://github.com/anthropics/claude-code/issues/60133${NC}"
echo

```

</details>

---

**After running the install script**, open a new terminal (or `source ~/.zshrc`) and verify with:

```bash
# Confirm keepalive timers are active on claude connections
ss -tnop state established '( dport = :443 )' | grep claude
# Expected: timer:(keepalive,Xs,0) on each line
```

**Stress test to confirm it works:**
```bash
claude --dangerously-skip-permissions -p "Run one at a time:
1. date
2. python3 -c \"import time; time.sleep(90); print('survived 90s')\"
3. python3 -c \"import time; time.sleep(90); print('survived second 90s')\"
4. date"
# Should complete all 4 steps (~3 min 20 sec total) without socket errors
```



--- Comment 6 ---
Author: muxunting
Date: 2026-05-21T02:43:52Z

Thanks for your analysis.

--- Comment 7 ---
Author: cubicYYY
Date: 2026-05-22T12:32:16Z

Still not fixed

--- Comment 8 ---
Author: searchingtofind
Date: 2026-05-22T14:20:48Z

Confirming this reproduces on **macOS 26.2 Tahoe (Darwin 25.2.0), Claude Code 2.1.145**, with the full mitigation set from this thread applied:

- Kernel SO_KEEPALIVE shim via `net.inet.tcp.always_keepalive=1`, `keepidle=60000`, `keepintvl=30000` (macOS equivalent of the Linux `LD_PRELOAD` shim — no binary injection needed)
- Persisted across reboots via LaunchDaemon
- All recommended env vars: `CLAUDE_CODE_REMOTE_SEND_KEEPALIVES=true`, `BUN_CONFIG_HTTP_IDLE_TIMEOUT=300`, `BUN_CONFIG_HTTP_RETRY_COUNT=3`, `CLAUDE_STREAM_IDLE_TIMEOUT_MS=120000`
- MTU/MSS fixes (`mssdflt=1440`, `delayed_ack=0`, `blackhole=0`)
- `NODE_OPTIONS=--dns-result-order=ipv4first` deliberately omitted (breaks Happy Eyeballs on macOS)

Verified the local network path is healthy: 0/10 failures on both IPv4 (`160.79.104.10`) and IPv6 (`2607:6bc0::10`) sustained tests, all responses ~50ms.

**Idle-drop failures are gone**, but **ECONNRESET mid-session continues** — matching Finding 5 (Bun HTTP/2 not handling server-initiated `GOAWAY`/`RST`). Symptom is constant retry loops during normal active agentic work, not just long-idle sessions.

Two notes for triage:
1. The \`platform:linux\` label is misleading — this affects macOS identically once the user has exhausted kernel-level workarounds. Suggest broadening to \`platform:macos\` as well or removing the platform restriction.
2. The userspace mitigation surface is now fully exhausted. Anything short of a CLI-side \`tengu_streaming_stale_connection_retry\` path or graceful \`GOAWAY\` handling in the Bun fetch wrapper leaves this unresolved.

--- Comment 9 ---
Author: brunos3d
Date: 2026-05-22T16:28:34Z

Yeah folks, my workarounds does not fix it completely, but it’s because of an Anthropic API internal issue. I was actually the one who originally reported this problem to Anthropic.

I strongly suspect this issue may only be affecting PRO users. One of the reasons I believe that is because the exact same behavior also happens retroactively on older Claude Code CLI versions, which makes it feel less like a recent client-side regression and more like something happening at the API or infrastructure layer.

What also makes this suspicious to me is that there should not really be a reason for API response behavior and runtime instability to differ this drastically between subscription tiers under normal circumstances.

Anthropic acquired Bun in December of last year:
https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone

Initially, the reported failures looked like standard Node.js runtime errors, but more recently the stack traces and failure patterns have started resembling Bun-specific behavior.

Of course, this could still be a simple engineering mistake, infrastructure regression, or an unintended side effect of internal changes. But I have my doubts. I’m curious how many people here are actually PRO users, because if this issue is confirmed to disproportionately affect PRO accounts, then this could become a major community concern.

Important note: this is ultimately my personal opinion and speculation based on my observations. I may be completely wrong. However, what is evident is that reports about this problem appear to have been dismissed since last year, back when the runtime behavior looked Node.js-related, and now again while the behavior appears more consistent with Bun.

cc: @cubicYYY @muxunting @searchingtofind @jshaofa-ui 

--- Comment 10 ---
Author: searchingtofind
Date: 2026-05-22T17:57:47Z

I have a max subscription, and this hit me suddenly, and across multiple long persisting sessions, without any anthropic side update pushed, which is, odd, to say the least. I have been using max subscription for 10 months, without anything like this happening. With The third party API changes coming mid june... it did feel targeted for some reason... 

--- Comment 11 ---
Author: brunos3d
Date: 2026-05-23T04:47:49Z

Yeah @searchingtofind bro, same feeling.

--- Comment 12 ---
Author: ianmedeiros
Date: 2026-05-24T23:59:36Z

Adding some complementary evidence in case it's useful — independently hit the same symptom on macOS (Brazilian residential ISP) and went through a similar investigation. Used Claude Code itself to help dig through pcaps and traces, so flagging upfront that some of my interpretation may be AI-shaped pattern-matching rather than ground truth.

## What I can add on top of @brunos3d  analysis

### 1. Packet-level evidence that some mid-stream breaks are middlebox-injected, not just lifecycle-related

I ran `tcpdump` of `api.anthropic.com` traffic in parallel with `claude --debug --debug-file` across several sessions. The mid-stream socket closes that survive Fix 1 (`SO_KEEPALIVE`) and would need Fix 3/4 to handle are, in my case at least, **spoofed RSTs from a middlebox on the network path**, not HTTP/2 GOAWAY or natural server-side closure.

Packet excerpt from one of the breaks (IPv4 path, request `64655465-9cbb-4691-beea-8b87a80ed18d`, 2026-05-24T22:39:14Z):

```
19:39:14.644312  server → client  Flags [P.], seq 23620:23712     ← real data
19:39:14.644411  client → server  Flags [.],  ack 23712            ← client ACKs
19:39:14.651840  server → client  Flags [R],  seq 657,377,615     ← RST, sequence number ~27,000× off the legitimate flow
19:39:15.123460  server → client  Flags [P.], seq 23712:23800     ← server STILL sends real data
19:39:15.772036  server → client  Flags [P.], seq 23800:23881     ← server STILL sends real data
```

Two impossible-if-real-server fingerprints:
- The RST's sequence number is wildly out of range vs the active flow (657 million while the real flow seq is 23,712).
- The "server" keeps retransmitting real data segments AFTER the alleged RST. A real server would have closed the socket.

Same fingerprint reproduced on the IPv6 path (request `8a91f305-6768-4721-bf2f-4d7bf63c5313`, RST seq ~1.95 billion vs legitimate flow at 8,516).

This is presumably an ISP DPI box on my path — not Anthropic's fault. But it strengthens the case for Fix 3 (transparent retry on the CLI path), because the underlying network event isn't a server lifecycle signal but a forged packet from a middlebox the user can't see or control. Users on flaky networks are going to keep hitting this regardless of any server-side fix.

### 2. Negative results on two of the recommended workaround env vars

In case other users see them in your workaround stack and assume they're helping:

- **`BUN_CONFIG_HTTP_RETRY_COUNT=10`** — I set this and ran a full session with `BUN_CONFIG_VERBOSE_FETCH=curl` capturing every fetch. The verbose log shows exactly one fetch attempt per request ID, even for the failing ones. The env var appears to only govern Bun's internal HTTP client (e.g., `bun install`), not user-level `fetch()`. So setting it doesn't add fetch-layer retries.
- **`CLAUDE_CODE_MAX_RETRIES=50`** — for the session-breaking ECONNRESET path I'm seeing, the SDK never logs an "attempt N/M" line. The retry path isn't being entered at all for this error class, so increasing the max doesn't matter. (Consistent with your Finding 3 — the CLI path doesn't have the retry treatment that background agents do.)

The other env vars in your workaround stack (`CLAUDE_CODE_REMOTE_SEND_KEEPALIVES`, `BUN_CONFIG_HTTP_IDLE_TIMEOUT`, `CLAUDE_STREAM_IDLE_TIMEOUT_MS`, `NODE_OPTIONS=--dns-result-order=ipv4first`) I haven't tested yet — going to try them next.

### 3. `BUN_CONFIG_VERBOSE_FETCH=curl` works, with a security caveat

For anyone else trying to instrument this: the env var IS honored in the compiled binary, but the output goes to **stderr**, not stdout — easy to miss if you only redirect stdout. It produces full curl-style request output including `Authorization: Bearer sk-ant-...` headers verbatim. Anyone capturing this output for sharing should pipe through `sed` to redact tokens before they hit disk.

### 4. Address family observations

I tried disabling IPv6 on the active network service as a workaround. It appeared to help on first capture, but a follow-up session with verified-zero IPv6 packets (`tcpdump` confirmed) hit the same middlebox-RST fingerprint on the IPv4 path. So at least on my network, address family isn't the variable. Possibly relevant to anyone wondering whether `--dns-result-order=ipv4first` would help — it might not, depending on whether the middlebox sits on both paths.

Also confirmed @brunos3d's observation that Bun appears to bypass `/etc/hosts` for some fetches — I saw IPv6 SYNs in tcpdump output despite having `api.anthropic.com` pinned to an IPv4 in hosts.

## Net

Strong +1 on the proposed fixes, particularly Fix 1 (`SO_KEEPALIVE`) and Fix 3 (CLI retry treatment). Happy to share full packet captures and debug traces privately with anyone on the team who wants them — they contain account info I'd rather not post publicly.

Specific request IDs from my captures, for server-side log correlation if useful:

- `8a91f305-6768-4721-bf2f-4d7bf63c5313` — 2026-05-24T21:34:02Z (IPv6 path)
- `64655465-9cbb-4691-beea-8b87a80ed18d` — 2026-05-24T22:39:14Z (IPv4 path)
- `a4c16288-54be-4eaf-82a6-ee8cd97c55ae` — 2026-05-24T23:11:09Z
- `d2d83bb1-cc44-4bfe-89fa-d1e26e370b29` — 2026-05-24T23:13:08Z


--- Comment 13 ---
Author: brunos3d
Date: 2026-05-27T04:55:09Z

<img width="1368" height="446" alt="Image" src="https://github.com/user-attachments/assets/c13c1c68-ec5d-4ba8-8a16-0a3fa801ee9a" />

This screenshot was taken during a real workflow session today, and it seems to reinforce the same hypothesis again.

The connection consistently fails around ~28 seconds with the exact same socket error every time:

“API Error: The socket connection was closed unexpectedly.”

The timing consistency is what stands out the most here. It really looks like some kind of ~30s connection/socket timeout happening somewhere between the CLI and the backend infrastructure.

I’m sharing this mostly as additional debugging evidence in case the Anthropic team is actively investigating the issue. The pattern seems too consistent to be random.

After some retries with the same prompt, it worked, but tokens were wasted.

---

### Issue #60108 — [FEATURE] Floating Window Option for "Side-Chats" for streamers so they can ..

State: OPEN | #60108
Labels: enhancement, area:tui, area:security


---



### Problem Statement

I want to do live projects and build on stream once I get the permission to become an affilate. I used to stream but, I started school and had to quit. I made over 100 followers in Kick in a day because I have a good partner, and in Youtube, I made a significant lesser number in one day because I am good at what I do. I just want to let you know that if people want to build and they need to transfer API keys like an N8N api key, the sidechat is on the same screen where all the action is. Side-Chat should also be hidden upon request on another screen not being mirrored if we are streaming and we can give it the information that we don't want our audience to see while we are building.

I asked the AI prompt and it sent me here.

### Proposed Solution

I call the prompt and ask it to give me a floating side-chat / streamer-mode side-chat for live demonstration mode and assist with keeping private keys a secret.

### Alternative Solutions

_No response_

### Priority

Critical - Blocking my work

### Feature Category

CLI commands and flags

### Use Case Example

_No response_

### Additional Context

_No response_

# Comments on anthropics/claude-code#60108
Total: 3 comments

--- Comment 1 ---
Author: Dexlabo
Date: 2026-05-18T03:16:10Z

floating window like how Tubi, Youtube has an option to eject the window out of the browser into a floating window that can be moved around but still be connected to the same Browser Application.

--- Comment 2 ---
Author: github-actions[bot]
Date: 2026-05-18T03:18:13Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/45206
2. https://github.com/anthropics/claude-code/issues/50963
3. https://github.com/anthropics/claude-code/issues/30154

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 3 ---
Author: Dexlabo
Date: 2026-05-18T03:56:33Z

Streamer mode should ensure that even if you accidentally drag the chat into the wrong window, anything that appears to be an API Key should be masked. So not only just a floating window, but after you've entered the API key, it returns a masked key but still takes the key to use internally.

---

### Issue #60589 — [BUG] VS Code extension: opening a new editor tab causes 300-500 ms main-thread stalls in the webview

State: OPEN | #60589
Labels: bug, has repro, platform:windows, area:ide, platform:vscode


---



### What's Wrong?

Opening a new editor tab in VS Code while the Claude Code panel is visible causes a 300 to 500 ms freeze in the renderer hosting the Claude Code webview. During the freeze the mouse cursor stutters, typing is delayed, and the chat panel visibly reflows. The freeze repeats every time the editor area is resized horizontally (open tab, close tab, split, drag the side bar boundary).

### Root Cause from Performance Trace

A renderer-process performance trace shows the cause clearly. When the editor area resizes horizontally, the Claude Code webview reacts to a `ResizeObserver` callback and synchronously re-lays-out and re-renders every chat turn in the panel. The hot call stack is in the extension's bundled `webview/index.js`:

```
measureReferenceDomElement
  observe (ResizeObserver)
    fire
      _deliver
        endUpdate
          [Monaco view rendering]
            _finishRenderingNewLines
            _renderWidget
            renderText
            _onRenderScheduled
```

Top long tasks during one 8.6 second trace that contained a single repro (durations vary with chat length):

| # | Duration | Dominant frames |
| --- | --- | --- |
| 1 | ~504 ms | Webview iframe init (V8 parse/compile of webview bundle) |
| 2 | ~333 ms | `fire` / `_deliver` / `endUpdate` / `measureReferenceDomElement` / `observe` |
| 3 | ~308 ms | Same ResizeObserver callback chain |
| 4 | ~292 ms | Monaco `_finishRenderingNewLines` / `_renderWidget` / `renderText` |
| 5 | ~103 ms | ResizeObserver callback chain |
| 6 | ~72 ms | Monaco view rendering inside webview |
| 7 | ~66 ms | Monaco view rendering inside webview |

Workbench contribution in the same trace is small by comparison:

- `doOpenEditor`, `doCloseEditor`, `addGroup`, `removeView`, `layout` in `workbench.desktop.main.js`: tens of ms combined
- `vscode-textmate` plus `vscode-oniguruma` tokenization for the newly opened file: about 32 ms total

So the cost is almost entirely in the extension's webview, not in VS Code itself.

### Layout Shifts

The same trace measures CLS 0.41 (CLS over 0.25 is rated poor). Three large shifts come from reflow inside the Claude Code chat panel as it resizes:

| Shift | Score | Impacted CSS classes (hashes vary by build) |
| --- | --- | --- |
| 1 | 0.949 | `turn_*`, `message_*`, `timelineMessage_*` |
| 2 | 0.899 | `turn_*`, `message_*`, `dotSuccess_*` |
| 3 | 0.949 | `turn_*`, `inputContainer_*` (about 869 px horizontal jump) |

Two minor shifts also occur in the workbench editor area itself (`editor.modified`, `lines-content.monaco-editor-background`) as it gains width once the Claude Code panel finishes its reflow.

### Steps to Reproduce

1. Install Claude Code 2.1.144 (or newer) in VS Code on Windows.
2. Open a workspace and dock the Claude Code chat panel to the side bar with several turns of chat history visible.
3. Open any new editor tab (Ctrl+P then pick a file, or click an unopened file in the explorer) so the editor area must resize.
4. Watch the mouse cursor and the chat panel. The cursor stutters for roughly half a second; the chat panel content visibly jumps as it reflows.

Severity scales with the number of chat turns in the panel. A freshly cleared panel stutters briefly. A long conversation stalls visibly each time.

### Expected Behavior

Resizing the panel container should not trigger a synchronous re-render of every chat turn. A width-only change to the outer container should not invalidate Monaco lines that have already been laid out and rendered.

### Suggested Fix Directions

Three options, smaller to larger change:

1. Debounce or coalesce the `ResizeObserver` callback in `webview/index.js`. At present it appears to fire on every animation frame of the resize and to call into the render pipeline synchronously. A trailing call after the resize gesture stops would remove most of the cost without changing visible behavior.
2. Treat width-only changes as a layout pass, not a render pass. Skip Monaco `_finishRenderingNewLines` / `_renderWidget` for turns whose content has not changed since the last render.
3. Render historical (non-streaming) chat turns to a plain DOM surface and only use Monaco for the actively streaming turn. Monaco is expensive to instantiate and re-layout per turn, and most turns are static once the response completes.

### Environment

- Claude Code extension: 2.1.144 (win32-x64)
- VS Code: stable channel
- OS: Windows 11 Pro
- Reproduces consistently on every editor area resize when the Claude Code panel is visible.

### Possibly Related but Distinct Issues

- #26302 (Claude Desktop app, Cowork VM plus GPU compositor root cause, not the VS Code extension webview)
- #42045 (CLI streaming output on high refresh rate displays, terminal renderer rather than webview)
- #55149 (Claude Desktop, LocalStorage sync payload blocking main thread, different blocker)
- #39807 (VS Code extension full hang, not a per-resize stutter)

These share the surface symptom of UI lag on Windows but identify different products or different root causes. The trigger here (editor area resize while the Claude Code panel is visible) and the bottleneck (`ResizeObserver` callback driving synchronous Monaco re-render of chat turns) are not in the existing reports I searched.

### Trace Artifacts

A Chrome Trace Event Format export from VS Code DevTools (Help, Process Explorer, renderer DevTools, Performance, Record) is available on request. The trace referenced above is roughly 55 MB. The summary in this report was extracted from it.

# Comments on anthropics/claude-code#60589
Total: 3 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-19T15:55:33Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/59335
2. https://github.com/anthropics/claude-code/issues/55453
3. https://github.com/anthropics/claude-code/issues/55149

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: jshaofa-ui
Date: 2026-05-19T16:11:49Z

# Fix: VS Code Extension 300-500ms Main-Thread Stalls on Editor Resize

## Root Cause Analysis

The issue is a **ResizeObserver synchronous layout thrashing** in the Claude Code webview. When the VS Code editor area resizes horizontally (open/close tab, split, drag sidebar boundary), the webview's ResizeObserver callback triggers a synchronous full re-layout and re-render of every chat turn in the panel.

### Evidence from Performance Trace

```
measureReferenceDomElement
  observe (ResizeObserver)
    fire
      _deliver
        endUpdate
          [Monaco view rendering]
            _finishRenderingNewLines
            _renderWidget
            renderText
```

Top long tasks:
| # | Duration | Dominant frames |
|---|----------|----------------|
| 1 | ~504 ms | Webview iframe init (V8 parse/compile) |
| 2 | ~333 ms | ResizeObserver callback chain |
| 3 | ~308 ms | Same ResizeObserver callback chain |
| 4 | ~292 ms | Monaco `_finishRenderingNewLines` |

### Why This Happens

1. **ResizeObserver fires synchronously**: The ResizeObserver callback runs on the main thread and performs synchronous DOM measurements + layout
2. **No debouncing**: Every pixel of resize triggers a full re-render — no accumulation or batching
3. **Full chat re-render**: The callback re-renders ALL chat turns, not just the visible viewport
4. **Monaco integration compounds**: The Monaco editor inside the webview also responds to resize, adding ~300ms of rendering time
5. **Nested resize observers**: Monaco's internal ResizeObserver fires in response to the webview's resize, creating a cascade

### Why Previous Duplicate Issues (#59335, #55453, #55149) Didn't Fix This

Those issues likely addressed individual symptoms (e.g., specific Monaco rendering paths) but didn't address the root cause: the ResizeObserver callback chain is synchronous and unbounded.

---

## Proposed Fix

### Layer 1: Debounce ResizeObserver Callbacks

```typescript
// In webview/src/resize-handler.ts (new file):

import { debounce } from 'lodash-es'; // or implement lightweight debounce

const RESIZE_DEBOUNCE_MS = 16; // ~1 frame at 60fps
const RESIZE_THROTTLE_MS = 32; // max 30fps for resize handling

class DebouncedResizeHandler {
  private debouncedResize: () => void;
  private isHandlingResize = false;

  constructor(private onResize: () => void) {
    this.debouncedResize = debounce(
      () => this.handleResize(),
      RESIZE_DEBOUNCE_MS,
      { leading: false, trailing: true }
    );
  }

  observe(element: HTMLElement): ResizeObserver {
    const observer = new ResizeObserver((entries) => {
      // Skip if we're already handling a resize (prevent cascade)
      if (this.isHandlingResize) return;
      this.debouncedResize();
    });
    observer.observe(element);
    return observer;
  }

  private async handleResize(): Promise<void> {
    if (this.isHandlingResize) return;
    this.isHandlingResize = true;
    try {
      // Use requestAnimationFrame to batch with browser's paint cycle
      await new Promise(resolve => requestAnimationFrame(resolve));
      this.onResize();
    } finally {
      this.isHandlingResize = false;
    }
  }
}
```

### Layer 2: Virtualize Chat Message Rendering

```typescript
// In webview/src/chat-virtualizer.ts (new file):

interface ChatMessage {
  id: string;
  element: HTMLElement;
  height: number;
  top: number;
}

class ChatVirtualizer {
  private messages: ChatMessage[] = [];
  private viewportHeight = 0;
  private scrollTop = 0;
  private container: HTMLElement;

  constructor(container: HTMLElement) {
    this.container = container;
  }

  update(messages: ChatMessage[], viewportHeight: number, scrollTop: number): void {
    this.messages = messages;
    this.viewportHeight = viewportHeight;
    this.scrollTop = scrollTop;
    this.renderVisibleOnly();
  }

  private renderVisibleOnly(): void {
    const visibleStart = this.scrollTop;
    const visibleEnd = this.scrollTop + this.viewportHeight;
    const buffer = 200; // px buffer above/below viewport

    let cumulativeTop = 0;
    for (const msg of this.messages) {
      msg.top = cumulativeTop;
      cumulativeTop += msg.height;

      // Only render messages in visible range + buffer
      const msgBottom = msg.top + msg.height;
      if (msgBottom >= visibleStart - buffer && msg.top <= visibleEnd + buffer) {
        msg.element.style.display = '';
        msg.element.style.transform = `translateY(${msg.top}px)`;
      } else {
        msg.element.style.display = 'none';
      }
    }

    // Set total height for scrollbar
    this.container.style.height = `${cumulativeTop}px`;
  }
}
```

### Layer 3: Isolate Monaco from Webview Resize Events

```typescript
// In webview/src/monaco-resize-guard.ts (new file):

class MonacoResizeGuard {
  private monacoContainer: HTMLElement;
  private isWebviewResizing = false;
  private pendingResizeToken: symbol | null = null;

  constructor(monacoContainer: HTMLElement) {
    this.monacoContainer = monacoContainer;
  }

  setupWebviewResizeProtection(): void {
    // Mark when webview is resizing
    const webviewObserver = new ResizeObserver(() => {
      this.isWebviewResizing = true;
      // Monaco will resize via its own mechanism after webview resize completes
      requestAnimationFrame(() => {
        this.isWebviewResizing = false;
        this.pendingResizeToken = Symbol('resize');
        this.monacoContainer.dispatchEvent(
          new CustomEvent('monaco-deferred-resize', { detail: { token: this.pendingResizeToken } })
        );
      });
    });
    webviewObserver.observe(this.monacoContainer.parentElement!);
  }

  // In Monaco's resize handler, check if webview is mid-resize
  shouldDebounceMonacoResize(): boolean {
    return this.isWebviewResizing;
  }
}
```

### Integration

```typescript
// In webview/index.ts — replace the existing ResizeObserver setup:

// BEFORE (problematic):
const resizeObserver = new ResizeObserver(() => {
  // Synchronously re-renders everything
  reRenderAllChatTurns();
  monacoEditor.layout();
});

// AFTER (fixed):
const resizeHandler = new DebouncedResizeHandler(() => {
  // Only re-render visible chat messages
  chatVirtualizer.update(
    chatMessages,
    viewportHeight,
    scrollContainer.scrollTop
  );
  // Monaco resize is now guarded against webview resize cascade
  if (!monacoResizeGuard.shouldDebounceMonacoResize()) {
    monacoEditor.layout();
  }
});

resizeHandler.observe(chatContainer);
```

---

## Files to Modify

| File | Change |
|------|--------|
| `webview/src/resize-handler.ts` | New: DebouncedResizeHandler class |
| `webview/src/chat-virtualizer.ts` | New: ChatVirtualizer for viewport-only rendering |
| `webview/src/monaco-resize-guard.ts` | New: MonacoResizeGuard to prevent cascade |
| `webview/src/index.ts` | Replace synchronous ResizeObserver with debounced handler |

---

## Testing Plan

1. **Unit tests**: Debounce timing accuracy, virtualizer visibility calculation
2. **Performance test**: Measure main-thread blocking time before/fix — target <16ms per resize
3. **Visual regression test**: Chat messages render correctly at various viewport sizes
4. **Integration test**: Open/close tabs, split editors, drag sidebar boundaries — no visible stutter

---

## Estimated Impact

- **Users affected**: All VS Code users with Claude Code panel visible
- **Fix complexity**: Medium (~300 lines across 3 new files + integration)
- **Risk**: Low (degradation path: if virtualizer fails, falls back to full render)
- **Value**: Eliminates 300-500ms main-thread stalls on every editor resize — dramatically improves UX for developers who frequently manage editor layouts


--- Comment 3 ---
Author: SixFive7
Date: 2026-05-19T17:08:55Z

Not a duplicate of any of the three issues the bot suggested. Each has a different trigger and a different root cause.

**#59335 (chat panel renders blank for ~2 s when refocusing tab)**

Trigger there is switching back to the Claude Code tab from another editor. Symptom is missing content for ~2 s before the panel paints. This issue (60589) is the opposite: the panel paints too eagerly and blocks the main thread for 300 to 500 ms on every editor area resize, with the trigger being any tab open / close / split (no refocus involved). Possibly a shared webview lifecycle layer, but the failure modes are opposite.

**#55453 (Cursor IDE webview tab restoration hangs on workspace startup)**

That issue is specific to Cursor IDE, only fires on workspace startup, and is a deserialize-on-restore hang. This issue is in VS Code, fires during routine use after the extension is already running, and is triggered by editor area resize.

**#55149 (Claude Code Desktop app, periodic input lag from 88 MB LocalStorage sync)**

Wrong product (Desktop app, not the VS Code extension). Different blocker (`blink.mojom.StorageAreaObserver` IPC carrying ~88 MB on the main thread, vs. `ResizeObserver` callback driving synchronous Monaco re-renders here). The body of this issue already addresses 55149 explicitly as non-overlapping.

This issue has detailed repro steps, a specific call stack from a performance trace, and was auto-labeled `bug` / `has repro` / `platform:windows` / `area:ide` / `platform:vscode`. Please keep it open.

---

### Issue #62778 — Long assistant responses (markdown tables / code blocks / file links) silently fail to render in VSCode extension

State: OPEN | #62778
Labels: bug, platform:macos, area:ide, platform:vscode

---

## Environment
- Client: Claude Code VSCode extension (native)
- OS: macOS (Darwin 23.6.0)
- Model: claude-opus-4-7 (1M context)

## Symptom
Long assistant responses containing markdown tables, fenced code blocks, and file path links never appear in the chat panel. The "Thinking..." indicator shows briefly, then disappears without rendering any text. The next user message can be sent normally, as if the assistant produced no reply.

Short plain-text responses (< ~30 chars, no markdown) render correctly in the same session.

## Repro (intermittent but reliable in long sessions)
1. Start a session that mixes substantive Q&A with file exploration tools (Bash, Read).
2. After several turns, ask a question that triggers a long markdown response with: a table, two or more fenced code blocks, multiple `[filename.ts:42](path#L42)` style links.
3. Observe: assistant turn ends with no visible text output.

## Correlation observed
- Failures cluster around turns where `system-reminder` messages about MCP server disconnect/reconnect are injected.
- The assistant's own logs show the long response was generated; only client-side rendering drops it.

## Hypothesis
Streaming parser / tag boundary handling — likely `<thinking>` or tool_use block close events are being misinterpreted, causing the trailing `<text>` content to be discarded. The correlation with MCP disconnect events suggests the parser may be entering a bad state when reminder blocks arrive mid-stream.

## Impact
Conversations become unrecoverable: the model believes it has answered while the user sees nothing, leading to repeated "you didn't answer" cycles. Workaround (forcing very short plain-text replies) defeats the tool's purpose.

## Logs
The Claude Code Output panel log can be attached on request if it captures parser errors.

# Comments on anthropics/claude-code#62778
Total: 0 comments

No comments on this issue.

---

### Issue #59569 — [BUG] VS Code extension: red banner "Unhandled case: [object Object]" appears frequently in chat panel (claude-vscode 2.1.141.x)

State: OPEN | #59569
Labels: bug, duplicate, platform:macos, platform:vscode


---



### What's Wrong?

A red error banner reading **"Unhandled case: [object Object]"** appears at the top of the Claude Code chat panel during normal use. The banner offers "View output logs" and "Troubleshooting resources" links. The underlying conversation state appears intact — only the rendering layer is affected — but the banner is showing up very frequently and disrupts the session.

**Surface:** Claude Code VS Code extension (`cc_entrypoint=claude-vscode`), chat panel renderer (iframe-based webview).

**Builds observed in a single session:** `cc_version=2.1.141.17d`, `cc_version=2.1.141.b00`, `cc_version=2.1.141.0d9` — three different build hashes appearing concurrently within one session, which is itself worth flagging (hot-update / staged-rollout AB?).

**`[object Object]` in the message strongly suggests** an object is being stringified into a template literal in a default/unhandled switch branch in the renderer — i.e., the renderer hit a case it didn't recognize and stringified the discriminator object instead of extracting a meaningful field.

### What Should Happen?

The chat panel should render assistant turns — including ones containing AskUserQuestion calls, multi-line preview content, or any normal content variant — without surfacing a renderer-internal "Unhandled case" error to the user. If the renderer encounters an unexpected discriminator, it should at minimum fail soft and log a useful error (not stringify the discriminator into a banner the end user sees).

### Error Messages/Logs

```shell
**Banner text shown in the chat panel:**

Unhandled case: [object Object]
View output logs · Troubleshooting resources


**"View output logs" content (SDK / agent-side, from the Claude output channel) — the string `Unhandled case` does NOT appear in this stream.** It contains only routine API request, tool dispatch, and streaming chunk debug lines. Sampling of notable signals (filtered from ~15 min of session output):


[DEBUG] attribution header x-anthropic-billing-header: cc_version=2.1.141.17d; cc_entrypoint=claude-vscode
[DEBUG] attribution header x-anthropic-billing-header: cc_version=2.1.141.b00; cc_entrypoint=claude-vscode
[DEBUG] attribution header x-anthropic-billing-header: cc_version=2.1.141.0d9; cc_entrypoint=claude-vscode
[WARN] Streaming stall detected: 35.1s gap between events (stall #1)
[WARN] [Stall] stream_idle_partial lastChunkAgeMs=15004 bytesTotal=659 idleDeadlineMs=300000
[DEBUG] Edit tool validation error: File has been modified since read, either by the user or by a linter.
[INFO] [Stall] tool_dispatch_end tool=Bash outcome=ok durationMs=300484


Three different `cc_version` build hashes (`.17d`, `.b00`, `.0d9`) appearing within one session is itself worth investigating.

**Webview / renderer-side console (where the actual `Unhandled case` stack should live):** attempted to capture, inaccessible to the user.

- `Developer: Open Webview Developer Tools` opens VS Code's main DevTools with `Using standard dev tools to debug iframe based webview` (from `webviewCommands.ts:33`) — i.e., VS Code falls back to standard DevTools because the Claude Code panel is an iframe-based webview.
- The frame dropdown lists multiple `vscode-webview://...` / `active-frame (index.html)` entries. Switching execution context to them and reproducing the banner did not surface any console message containing `Unhandled case`. Filtering all frames for `Unhandled` also returned no matches even after the banner re-appeared.
- This may itself be a finding: the renderer's error path appears to render the banner without writing the error to `console.error`, leaving users (and bug filers) without a captureable trace.
```

### Steps to Reproduce

Not yet a deterministic repro — the banner appears frequently during ordinary multi-turn sessions, but the exact triggering content has been hard to pin down. What I can report:

1. Open VS Code with the Claude Code extension; chat panel against `claude-opus-4-7`.
2. Use the chat normally over a multi-turn session involving:
   - Sub-agent dispatch (`source=agent:builtin:general-purpose`), including long-running general-purpose agents (one agent ran 437s / 49 turns, another ran 1142s / 77 turns in my captured window).
   - Long-running `Bash` tool calls (durations of 120s and 300s observed, including some that hit the 300s deadline).
   - File `Edit` / `Write` tool calls.
3. The red `Unhandled case: [object Object]` banner appears at the top of the chat panel during this normal flow. Frequency is high — many times per session.

**Suspected trigger candidates** (none confirmed):
- Assistant turns containing `AskUserQuestion` tool calls whose option `preview` fields contain newlines, code blocks, or ASCII layouts. (I observed the banner around such turns, but later also observed it on plain Bash+text turns with no `AskUserQuestion` at all — so this hypothesis is weakened.)
- The multi-build session (three concurrent `cc_version` hashes) raising the chance that a content variant emitted by one build is unknown to another build's renderer.

### Claude Model

Opus

### Is this a regression?

I don't know

### Last Working Version

_No response_

### Claude Code Version

VS Code extension Claude Code: cc_version=2.1.141.17d / 2.1.141.b00 / 2.1.141.0d9 (three concurrent build hashes observed in one session via x-anthropic-billing-header), cc_entrypoint=claude-vscode

### Platform

Anthropic API

### Operating System

macOS

### Terminal/Shell

Other

### Additional Information

**Template note:** the Terminal/Shell field is set to "Other" because this report is about the **Claude Code VS Code extension chat panel renderer**, not the CLI inside a terminal. The CLI-focused bug template doesn't have a precise category for this. Model "Opus" maps to `claude-opus-4-7` in my session.

**Hypotheses for maintainers to investigate:**

1. **Renderer discriminated-union fall-through.** The literal `[object Object]` in the user-facing string strongly suggests a default/unhandled `case` branch in the renderer that does something like `` `Unhandled case: ${variant}` `` where `variant` is the full content object rather than `variant.type` (or equivalent discriminator). Likely candidates to audit:
   - The `AskUserQuestion` option / preview renderer.
   - Any newly-added content block or tool-result variant added between the three observed builds (`2.1.141.0d9`, `2.1.141.b00`, `2.1.141.17d`).
   - Any streaming-partial path that emits a placeholder content node while a stream is still in flight (the session had a 35.1s streaming stall and several `stream_idle_partial` warnings).

2. **Concurrent build hashes within one session.** Three different `cc_version` short hashes appearing in `x-anthropic-billing-header` for a single uninterrupted session suggests either staged rollout, hot-update mid-session, or some build-tagging issue. If a renderer in build A receives content shaped per a model emitted by build B, an "unhandled case" is exactly what you'd expect.

3. **"View output logs" link points to the wrong destination.** The banner's "View output logs" link opens the VS Code "Claude" output channel (the agent SDK side), which does not contain the `Unhandled case` string. The actual error is fired in the webview renderer and is not surfaced anywhere the user (or bug reporter) can reach without VS Code-level DevTools. Even with `Developer: Open Webview Developer Tools`, the webview is iframe-based and falls back to standard DevTools, and `console.error` filtering for `Unhandled` returned no matches — suggesting the error path renders the banner without also writing to `console.error`. Worth fixing both: log to console, and have the link point somewhere actually useful.

**Environment specifics:** macOS, Claude Code VS Code extension running against `claude-opus-4-7` on the Anthropic API, ~980k effective context window. Sessions involved many concurrent general-purpose sub-agents and long-running Bash/Edit/Write tool calls.

# Comments on anthropics/claude-code#59569
Total: 3 comments

--- Comment 1 ---
Author: ccalvop
Date: 2026-05-18T09:50:25Z

I have the same issue

--- Comment 2 ---
Author: OtisVENTR
Date: 2026-05-18T22:03:12Z

+1 — seeing this frequently on macOS with multiple MCP servers and hooks configured. Appears randomly mid-session with no obvious trigger. Running claude-vscode in VS Code.

--- Comment 3 ---
Author: Sherwin-NG
Date: 2026-05-27T06:59:23Z

+1, hitting this on macOS as well. Adding some diagnostic findings in case it helps narrow it down.

## Environment
Claude Code extension: v2.1.141
Editor: VS Code (stable) on macOS Darwin 25.5.0
Other AI extensions installed (potential interference): Cline, MarsCode, GitHub Copilot Chat, LiCode
## Symptom
Top-bar notification text:

Unhandled case: [object Object]
View output logs · Troubleshooting resources

Intermittent — happens during normal usage, often around tool calls.

## Root cause location
The thrown error originates from the bundled webview, not from the extension host. In ~/.vscode/extensions/anthropic.claude-code-2.1.141-darwin-arm64/webview/index.js:


function QB1($, Z) { throw Error(Z ?? `Unhandled case: ${$}`) }
This is a TypeScript assertNever-style helper. When $ is an object reaching the default branch of an exhaustive switch, template-string coercion produces [object Object]. Notably, this function is defined directly adjacent to the # Claude in Chrome browser automation prompt block, suggesting the failing dispatch is in the tool-message / browser-use code path.

## Why logs are empty
Worth flagging: webview console errors are not persisted to disk under ~/Library/Application Support/Code/logs/<session>/. So a regular log grep finds nothing. Repro needs to be captured via Developer: Open Webview Developer Tools → Console. This is likely why earlier reports lack a stack trace.

## What would help maintainers
Could you consider:

Logging the actual typeof / JSON of $ before throwing, so users can paste a useful trace;
Or replacing the template-string fallback with JSON.stringify($, null, 2) to avoid the [object Object] black hole?
Will try to capture a webview-devtools stack trace next time it reproduces and post here.

---

### Issue #52866 — [BUG] Terminal re-renders entire conversation output repeatedly during sequential tool calls

State: OPEN | #52866
Labels: bug, platform:macos, area:tui


---



### What's Wrong?

What's Wrong:                                                                                                                                                                         
  When Claude Code executes multiple sequential tool calls in one response (e.g. 4–5 file edits in a row), the terminal re-renders the entire previous conversation output from scratch 
  on each new chunk/result instead of appending. This causes every previous response block to appear repeated many times in the terminal scroll history.                                
                                                                                                                                                                                        
  Observed twice in the same session:                                                                                                                                                   
  1. First response of the session (a markdown table) rendered ~20 times before the next prompt appeared.                                                                               
  2. During a sequence of 5 Edit tool calls to the same file, the full diff output block was re-rendered after each call — resulting in the same content repeated 5+ times.
                                                                                                                                                                                        
  The duplicates are visible in the scroll history (not just a visual flicker). The content below the duplicates is correct — it appears to be a rendering/repaint issue, not actual    
  duplicate API responses.                                                                                                                                                              
                                                                                                                                                                                        
  Environment (there will likely be a section for this below the fold):                                                                                                                 
  - Claude Code version: 2.1.119                                                                                                                                                        
  - OS: macOS (Darwin 25.4.0)   
  - Terminal: macOS Terminal.app (not iTerm2)                                                                                                                                           
  - Shell: zsh                                                                                                                                                                          
  - Terminal dimensions: 184×173                    

### What Should Happen?

  Each response should render once and append below the previous one.                                                                                               
  New tool results should add to the bottom of the output, not cause                                                                                                
  the entire conversation to re-render from the top. 

### Error Messages/Logs

```shell
No error messages. The bug is purely visual — no crash, no error output.
```

### Steps to Reproduce

1. Start a Claude Code session in macOS Terminal.app                                                                                                              
  2. Give Claude a task that requires multiple sequential file edits                                                                                                
     in a single response (e.g. "update these 4 sections in this file")                                                                                             
  3. Observe the terminal output as each Edit tool call completes                                                                                                   
  4. The full output block from earlier in the response re-renders                                                                                                  
     after each tool result, causing it to appear repeated N times                                                                                                  
     (once per tool call)                                                                                                                                           
                                                                                                                                                                    
  Alternative trigger: the very first response in a new session                                                                                                     
  containing a markdown table may also repeat ~20 times before                                                                                                      
  the prompt appears.

### Claude Model

Sonnet (default)

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

_No response_

### Claude Code Version

 2.1.119 (Claude Code)

### Platform

Anthropic API

### Operating System

macOS

### Terminal/Shell

Terminal.app (macOS)

### Additional Information

<img width="275" height="1219" alt="Image" src="https://github.com/user-attachments/assets/c47cb470-3b62-4d8f-8397-73a86fb431ce" />

<img width="229" height="1225" alt="Image" src="https://github.com/user-attachments/assets/2fde7354-3d1f-4482-bd23-5ececc32dcc7" />

<img width="343" height="1231" alt="Image" src="https://github.com/user-attachments/assets/5d900b8d-168e-432f-be0e-16dff6989a09" />

<img width="293" height="1217" alt="Image" src="https://github.com/user-attachments/assets/07696778-2513-4dab-ac28-31b4c9dff11d" />

# Comments on anthropics/claude-code#52866
Total: 5 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-04-24T13:40:54Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/51418
2. https://github.com/anthropics/claude-code/issues/49985
3. https://github.com/anthropics/claude-code/issues/46775

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: cutuer
Date: 2026-04-25T15:55:43Z

+1 reproducing on **Windows 11 Pro 26200** + Git Bash, Claude Code 2.1.119, /think low.

Confirmed today: during a sequence of Bash + Read + Edit + curl tool calls, the entire prior conversation block (assistant message + earlier tool outputs) re-rendered in the scrollback. Closely related to (or same root cause as) #52924 — the redraw is triggered specifically by sequential tool-call streaming, not just by long session length.

Happy to share an anonymized transcript.

--- Comment 3 ---
Author: jackstine
Date: 2026-04-29T15:31:46Z

Please fix this. This is absurd.
Been happening for at least three weeks.
Claude Code v2.1.123
MacOs Tahoe 26.2 

--- Comment 4 ---
Author: IsaacCheng9
Date: 2026-05-09T14:53:00Z

I've also encountered this issue very frequently with the following environment:

- Claude Code 2.1.138
  - Noticed regressions particularly around when `/recap` was added
- OS: macOS Tahoe 26.4.1
- Terminal: Ghostty 1.3.1

--- Comment 5 ---
Author: startupfundraising
Date: 2026-05-22T12:07:17Z

I'm sick of duplicated content. I don't experience the same way, but yes I am am up to date with claude code. It has been at least a month.

---

### Issue #40574 — [Bug] Garbled characters (mojibake) in CLI output    since v2.1.86

State: OPEN | #40574
Labels: bug, platform:macos, area:tui


---



### What's Wrong?

**Environment:**
  - Claude Code version: 2.1.86+                          
  - OS: macOS (Darwin 25.3.0)                           
  - Terminal: [iTerm2 / Terminal.app / VS Code Terminal]  
  - Shell: zsh                                            
  - Locale: UTF-8                                         
                                                          
  **Description:**                                      
  Since upgrading to v2.1.86, Chinese characters in
  Claude's text output are intermittently rendered as `��`
   (U+FFFD replacement characters). This happens in the
  conversation output (not in file writes — generated code
   files are correct).                                  

  **Example:**
  - Expected: `LLM 调用工具 "dashscope_web_search"`
  - Actual:   `LLM ��用工具 "dashscope_web_search"`       
   
  The corrupted character is `调` (U+8C03), a common CJK  
  character. It appears to be a multi-byte UTF-8        
  truncation issue where a 3-byte sequence gets split at a
   chunk boundary.                                      

  **Frequency:** Intermittent, occurs multiple times per  
  session, across different conversations. Affects only
  terminal rendering — files written via Write/Edit tool  
  are not corrupted.                                    

  **Steps to reproduce:**                                 
  1. Use Claude Code in a Chinese-language conversation
  2. Ask it to generate longer text outputs containing CJK
   characters                                           
  3. Observe random `��` replacements in the streamed     
  output                                                  
   
  **Suspected cause:** SSE streaming chunk boundary       
  splitting multi-byte UTF-8 sequences.     

### What Should Happen?

**Environment:**
  - Claude Code version: 2.1.86+                          
  - OS: macOS (Darwin 25.3.0)                           
  - Terminal: [iTerm2 / Terminal.app / VS Code Terminal]  
  - Shell: zsh                                            
  - Locale: UTF-8                                         
                                                          
  **Description:**                                      
  Since upgrading to v2.1.86, Chinese characters in
  Claude's text output are intermittently rendered as `��`
   (U+FFFD replacement characters). This happens in the
  conversation output (not in file writes — generated code
   files are correct).                                  

  **Example:**
  - Expected: `LLM 调用工具 "dashscope_web_search"`
  - Actual:   `LLM ��用工具 "dashscope_web_search"`       
   
  The corrupted character is `调` (U+8C03), a common CJK  
  character. It appears to be a multi-byte UTF-8        
  truncation issue where a 3-byte sequence gets split at a
   chunk boundary.                                      

  **Frequency:** Intermittent, occurs multiple times per  
  session, across different conversations. Affects only
  terminal rendering — files written via Write/Edit tool  
  are not corrupted.                                    

  **Steps to reproduce:**                                 
  1. Use Claude Code in a Chinese-language conversation
  2. Ask it to generate longer text outputs containing CJK
   characters                                           
  3. Observe random `��` replacements in the streamed     
  output                                                  
   
  **Suspected cause:** SSE streaming chunk boundary       
  splitting multi-byte UTF-8 sequences.     

### Error Messages/Logs

```shell

```

### Steps to Reproduce

2.1.86

### Claude Model

None

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

_No response_

### Claude Code Version

2.1.86

### Platform

Anthropic API

### Operating System

macOS

### Terminal/Shell

Terminal.app (macOS)

### Additional Information

_No response_

# Comments on anthropics/claude-code#40574
Total: 9 comments

--- Comment 1 ---
Author: m-itoi
Date: 2026-03-30T03:23:02Z

Same issue here with Japanese characters on Linux (WSL2).

- Claude Code version: 2.1.87
- OS: Linux (WSL2, 6.6.87.2-microsoft-standard-WSL2)
- Terminal: VS Code Terminal
- Shell: zsh

In addition to conversation output, we also see corruption in **Edit tool output** (file writes). Example:
- Expected: `リクエスト値`
- Actual: `リクエス���値` (「ト」corrupted to U+FFFD)

Happens intermittently, multiple times per session.

--- Comment 2 ---
Author: MU5K
Date: 2026-04-01T11:13:59Z

Same version range (v2.1.86+), different symptom on **Windows + Git Bash (MSYS2)**.

## Environment

- Claude Code: 2.1.89
- OS: Windows 11 Pro (26200.8117)
- Terminal: Windows Terminal / VS Code integrated terminal
- Shell: Git Bash (MSYS2 MINGW64)
- Locale: `LANG=ja_JP.UTF-8`, system codepage 932

## Symptom

Emoji characters in conversation output are **replaced with `◆` (U+25C6 black diamond)** — not `U+FFFD` as reported in the original issue. CJK text renders correctly; only emoji is affected.

Example: `📋 月次リマインド` → `◆ 月次リマインド`

## Key finding: Git Bash only

On the **same machine, same Windows Terminal window**:

| Shell | Result |
|---|---|
| Git Bash (MSYS2) | Emoji → `◆` (broken) |
| PowerShell 7.6 | Emoji renders correctly |

This suggests Claude Code's terminal capability detection treats MSYS2/Git Bash differently and falls back to a non-emoji character set.

## Relevant env vars in Git Bash

- `OSTYPE=msys`
- `MSYSTEM=MINGW64`
- `TERM=xterm-256color`
- `TERM_PROGRAM=` (empty)
- `COLORTERM=` (empty)
- `WT_SESSION=` (set — confirms running inside Windows Terminal)

PowerShell likely has `TERM_PROGRAM` or other vars set that signal emoji support. The absence of these in Git Bash may trigger the fallback.

## Notes

- Shell prompt (oh-my-posh with Nerd Font) renders emoji correctly — this is not a terminal/font issue
- File writes via Edit/Write tools are not affected — only conversation output
- The `◆` fallback character (rather than `U+FFFD`) suggests a deliberate emoji→symbol substitution path, not a UTF-8 chunk boundary issue as described in the original report. These may be two separate bugs sharing the same version trigger (v2.1.86+).

--- Comment 3 ---
Author: MU5K
Date: 2026-04-01T11:42:18Z

**Follow-up:** Additional TUI rendering issues on the same Git Bash environment.

Beyond the emoji → `◆` substitution reported above, there are broader rendering problems in Git Bash (MSYS2) since v2.1.86+:

## 1. Echo/duplicate rendering ("yamabiko")

Conversation output is rendered twice — scrolling back reveals the same content duplicated. This is visible from the scrollbar length being much longer than expected. Likely the ink rendering buffer is double-flushing against the Git Bash PTY.

## 2. TUI element corruption (intermittent, observed on v2.1.87)

Tool status indicators render as garbled text — e.g., tool names replaced with "Jitterbugging…", layout collapsing. This was observed in VS Code + Git Bash on 2026-03-31 but is not consistently reproducible as of v2.1.89.

## Current state (v2.1.89)

| Symptom | Status |
|---|---|
| Emoji → `◆` | Still occurring |
| Echo/duplicate rendering | Still occurring |
| TUI element corruption | Improved, not currently observed |

All symptoms are **Git Bash (MSYS2) only** — PowerShell 7.6 on the same machine and same Windows Terminal does not exhibit any of these issues.

Reproduction steps for the echo issue are not yet pinpointed — it is noticed when scrolling back through conversation history. It may be related to output length or parallel tool execution.

--- Comment 4 ---
Author: MU5K
Date: 2026-04-01T11:44:49Z

**Addendum:** One more symptom on the same Git Bash (MSYS2) environment.

## 3. Status bar splitting across two lines

The bottom status bar (model name, cost, diff stats, branch, file indicator, timer) splits into two rows instead of rendering on a single line. This suggests the terminal width calculation is off — likely because emoji and/or multi-byte characters are counted differently by the ink renderer vs the Git Bash PTY.

This is also Git Bash only — PowerShell renders the status bar on a single line as expected.

--- Comment 5 ---
Author: MU5K
Date: 2026-04-03T16:43:26Z

<img width="1373" height="1168" alt="Image" src="https://github.com/user-attachments/assets/4b601de0-b879-4b1e-ba30-8c723477779b" />

**Additional finding: v2.1.76 renders correctly on the same environment**

On a dormant Windows account, the VS Code extension launched Claude Code with its older bundled version (v2.1.76), while `claude --version` returned v2.1.91. In this state, **none** of the following symptoms occurred:

- Emoji → `◆` substitution
- Echo/duplicate rendering
- Status bar splitting across two lines

The OS, terminal (Windows Terminal + Git Bash / MSYS2), shell, locale, and font are identical to the environment where v2.1.86+ consistently exhibits all of the above symptoms. The only difference is the version of Claude Code's TUI rendering code being executed.

This narrows the regression window to **v2.1.76 → v2.1.86**.

--- Comment 6 ---
Author: Astro-Han
Date: 2026-04-05T11:14:11Z

+1. macOS (Darwin 25.3.0), Terminal.app, CLI latest, Chinese (Simplified).

Same U+FFFD corruption in streaming output. Consistent with the UTF-8 byte-boundary splitting described in #39593. File writes via Edit/Write tools are fine, only TUI rendering affected.

--- Comment 7 ---
Author: noahfestifriend
Date: 2026-05-15T04:47:11Z

I have a video of this happening in real time... Maybe not the same issue but it's really strange and may be related.
This is MacOS and using a VS Code terminal window fullscreened.

https://youtu.be/vnuf02XlfYk

It clears up when I point it out to Claude... so Idk if it is just a corrupted stream or what but it happens relatively often for me. Like every few days or so.

--- Comment 8 ---
Author: paperdyno
Date: 2026-05-16T01:42:11Z

Resizing terminal horizontally fixes the issue, at least temporarily.

--- Comment 9 ---
Author: ljpsfree
Date: 2026-05-24T02:14:07Z

I'm running into a related but slightly different variant of this bug. My setup: macOS Darwin 25.3.0, iTerm2 3.6.10, zsh, locale UTF-8.

The issue only appears in background agents mode (when `$CLAUDE_JOB_DIR` is set). In a regular interactive session, Chinese text displays and copies correctly. In an agents session, the text on screen looks correct, but when I select and copy it, the clipboard ends up with double-encoded bytes.

I verified with `pbpaste | xxd` (screenshot attached): instead of the expected UTF-8 bytes (e.g., E4 B8 AD for 中), the clipboard has each original byte re-encoded as a separate UTF-8 2-byte sequence (e.g., c3 84 c2 b8 c2 ad). The pattern is consistent with each raw byte being interpreted as a Latin-1 code point and then re-encoded as UTF-8.

The same text copied from the normal scrollback after exiting the agent view comes out correctly. So the bug seems to be in the rendering path specific to the agents TUI, not in the underlying output — I captured the raw PTY output and the bytes Claude Code writes to the terminal are correct UTF-8.

Workaround for now: exit the agent view before copying.

---

### Issue #49268 — Thinking summaries missing on Opus 4.7 — harness doesn't set display: "summarized"

State: OPEN | #49268
Labels: bug, has repro, platform:macos, area:core


---

Switched to Opus 4.7 on v2.1.111 and noticed thinking summaries stopped showing up. Took a bit to track down — writing it up in case it's useful.

The [extended-thinking API docs](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) note that Opus 4.7 changed the default for the `display` parameter to `"omitted"` (Opus 4.6 and earlier defaulted to `"summarized"`). The reason given is faster time-to-first-token on streaming responses.

The result is the API returns thinking blocks with empty `thinking` fields by default, so the UI has nothing to render. Setting `"showThinkingSummaries": true` in `settings.json` doesn't help — that controls rendering of what the API sends back, not what the API decides to send.

**Repro**
1. Run v2.1.111 with `"showThinkingSummaries": true` set
2. `/model claude-opus-4-7`
3. Ask something that triggers extended thinking
4. No summaries appear in the UI

Switching to `claude-opus-4-6` or `claude-sonnet-4-6` brings them back since those still default to `"summarized"`.

**Suggested fix**
When the selected model defaults to `display: "omitted"` (currently Opus 4.7 and Mythos Preview per the docs) and the user has `showThinkingSummaries` enabled, the harness should pass `display: "summarized"` explicitly in the API request.

**Environment**
- Claude Code 2.1.111
- Model: `claude-opus-4-7` (1M context variant)
- macOS 15.3 (Darwin 25.3.0)

# Comments on anthropics/claude-code#49268
Total: 30 comments

--- Comment 1 ---
Author: yusufmo1
Date: 2026-04-16T16:51:56Z

Dug into the v2.1.111 binary to confirm what's actually broken. **The bug:** the `showThinkingSummaries: true` setting and the API's `thinking.display` parameter are two completely unrelated systems in the harness — there is no code path that wires one to the other. So enabling the setting can't make summaries come back; whether you get them depends entirely on the model's API default, which Opus 4.7 flipped to `"omitted"`.

here's the request-construction code:

```js
const bH = V_ ? q.display ?? undefined : undefined;
const QH = { type: "adaptive", display: bH };  // sent as the thinking parameter
```

`bH` is sourced only from `q.display`, an internal field on the thinking config object. Nothing reads `showThinkingSummaries` and assigns it to `q.display`. So `bH` is always `undefined`, the `display` field drops out of the request, and Opus 4.7 returns empty thinking blocks.

What `showThinkingSummaries` actually controls — straight from the embedded schema string:

> `showThinkingSummaries: "Show thinking summaries in the transcript view (ctrl+o). Default: false."`

It governs (a) the Ctrl+O transcript-view renderer and (b) whether the `redact-thinking-2026-02-12` beta header is sent. Neither has any effect on the API's `display` parameter. The naming overlap is misleading — a user reasonably assumes the setting controls whether summaries are requested, but it doesn't.

There's a related model-version gate nearby:

```js
const z_ = env.CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING && (model.includes("opus-4-6") || model.includes("sonnet-4-6"));
```

That allowlist was never extended to 4.7 — same regression pattern: the request-construction code still treats 4.6 as the newest model.

Suggested minimal fix: when `showThinkingSummaries === true`, set `q.display = "summarized"` so it flows into `bH` and onto the request. Or, simpler and more correct: send `display: "summarized"` unconditionally for any model where the API defaults to `"omitted"` (currently Opus 4.7 and Mythos Preview), with an explicit opt-out for users who want the latency benefit of `"omitted"`. The 4.6/sonnet-4.6 model checks should also be extended to cover 4.7+.


--- Comment 2 ---
Author: mjesuele
Date: 2026-04-16T20:35:58Z

Confirmed the diagnosis with a binary patch on v2.1.112 (Linux x86-64).

The request-construction code has:

```js
CH=h$?q.display??void 0:void 0
```

`q.display` is never populated from the `showThinkingSummaries` setting, so `CH` is always `undefined` and Opus 4.7's default (`"omitted"`) wins.

**Fix:** `q.display??void 0` and `"summarized"     ` are both 17 bytes. Replacing in-place with `sed`:

```bash
cp /path/to/2.1.112 /path/to/2.1.112.bak
sed -i 's/q\.display??void 0/"summarized"     /g' /path/to/2.1.112
```

Two occurrences patched (offsets 119213276 and 232078516 in my build). Thinking summaries now display correctly on Opus 4.7 with `showThinkingSummaries: true`. Survives until next `claude update`.

--- Comment 3 ---
Author: Nitjsefnie
Date: 2026-04-16T20:57:24Z

Verified `--thinking-display summarized` restores populated thinking blocks on Opus 4.7 end-to-end (Claude Code 2.1.112, first-party / Max subscription).

**Settings alone don't work.** Before: `~/.claude/settings.json` already had both `showThinkingSummaries: true` AND `thinkingDisplay: "summarized"`. Persisted jsonl still showed `{"type":"thinking","thinking":"","signature":"..."}` on every Opus 4.7 turn. A local sweep across all my session jsonls was clean: 2.1.97–2.1.110 with opus-4-6 → 3,399/3,399 populated; 2.1.111 with opus-4-7 → 134/134 empty; 2.1.111 with synthetic helper model → populated. So `showThinkingSummaries: true` is doing its job at the beta-header level (no `redact-thinking-2026-02-12` sent), but matches @yusufmo1's diagnosis that it doesn't feed into `q.display` — and the 4.7 server default `"omitted"` wins.

**CLI flag works.** Same binary, same settings — just launched a new claude session with `claude --thinking-display summarized`. The resulting jsonl writes populated thinking blocks with valid signatures:

- L8 block[0]: 202 chars, populated, signature present
- L23 block[0]: 87 chars, populated, signature present

First-party Max, no binary patch, no `CLAUDE_CODE_EXTRA_BODY` — just the flag.

**Persistence for interactive shells:**

```bash
alias claude='claude --thinking-display summarized'
```

Caveat: only affects interactive-shell invocations of `claude`. Non-interactive callers (cron, systemd, scripts with `#!/bin/sh`) won't pick up the alias — a wrapper earlier on `$PATH` than the real binary would cover those.


--- Comment 4 ---
Author: narner90
Date: 2026-04-17T02:14:18Z

> Verified `--thinking-display summarized` restores populated thinking blocks on Opus 4.7 end-to-end (Claude Code 2.1.112, first-party / Max subscription).
> 
> **Settings alone don't work.** Before: `~/.claude/settings.json` already had both `showThinkingSummaries: true` AND `thinkingDisplay: "summarized"`. Persisted jsonl still showed `{"type":"thinking","thinking":"","signature":"..."}` on every Opus 4.7 turn. A local sweep across all my session jsonls was clean: 2.1.97–2.1.110 with opus-4-6 → 3,399/3,399 populated; 2.1.111 with opus-4-7 → 134/134 empty; 2.1.111 with synthetic helper model → populated. So `showThinkingSummaries: true` is doing its job at the beta-header level (no `redact-thinking-2026-02-12` sent), but matches [@yusufmo1](https://github.com/yusufmo1)'s diagnosis that it doesn't feed into `q.display` — and the 4.7 server default `"omitted"` wins.
> 
> **CLI flag works.** Same binary, same settings — just launched a new claude session with `claude --thinking-display summarized`. The resulting jsonl writes populated thinking blocks with valid signatures:
> 
>     * L8 block[0]: 202 chars, populated, signature present
> 
>     * L23 block[0]: 87 chars, populated, signature present
> 
> 
> First-party Max, no binary patch, no `CLAUDE_CODE_EXTRA_BODY` — just the flag.
> 
> **Persistence for interactive shells:**
> 
> alias claude='claude --thinking-display summarized'
> 
> Caveat: only affects interactive-shell invocations of `claude`. Non-interactive callers (cron, systemd, scripts with `#!/bin/sh`) won't pick up the alias — a wrapper earlier on `$PATH` than the real binary would cover those.

That fix does not seem to be working for me on linux, version 2.1.110

--- Comment 5 ---
Author: alkautsarf
Date: 2026-04-17T02:34:19Z

Confirming this still happens on **2.1.112** (one version newer than reporter).

Dug into the binary and there's a hidden CLI flag that already does the right thing:

```
--thinking-display <display>  choices: summarized, omitted   .hideHelp()
```

Verified end-to-end: launching with `claude --thinking-display summarized` on Opus 4.7 restores populated thinking blocks. So the API plumbing is wired — the gap is that:

1. The flag is `.hideHelp()`, so `claude --help` doesn't show it (hard to discover)
2. There's no equivalent settings.json key, only `alwaysThinkingEnabled` (boolean enable/disable, doesn't control display)
3. The CLI builds `{type:"adaptive"}` without a `display` field by default, so the request inherits Opus 4.7's new `display:"omitted"` default

**Suggested fix** (small surface):
- Un-hide `--thinking-display` from `--help`
- Add a `thinkingDisplay: "summarized" | "omitted"` settings.json key that maps to the same flag, so users on 4.7 can persist the preference without wrapping `claude` in a script
- Bonus: when `alwaysThinkingEnabled: true` is set with no explicit `thinkingDisplay`, default `display` to `"summarized"` (matches user intent — they enabled thinking because they want to see it)

Workaround for anyone reading this: add `--thinking-display summarized` to your launcher wrapper.


--- Comment 6 ---
Author: Hammaarn
Date: 2026-04-17T07:08:42Z

Adding a workflow-impact voice to this thread — the existing comments cover diagnosis and workarounds well, but the severity case hasn't been made from a power-user angle.

My orchestration system is architected around visible reasoning: agent dispatch targeting, lens activation decisions, verification-before-completion, panel reviews. I don't use reasoning visibility as a UX nicety — it's the primary surface I use to catch misinterpretations *before* code is written, sanity-check dispatches *before* approving, and debug decisions in flight. On 4.7 with the current default, that entire layer is opaque. The functional downgrade is substantial.

Separately, the naming collision is genuinely misleading: `showThinkingSummaries: true` sounds like it controls whether summaries are requested. It doesn't, and the gap between "setting enabled" and "no summaries appearing" reads as a bug long before a user thinks to check the API default.

Proposed priority: promoting `--thinking-display` out of `.hideHelp()` and adding a `thinkingDisplay` settings.json key is a few lines of code for substantial workflow recovery. Developer-tool audiences are not the same audience as consumer-chat — the default for Claude Code probably shouldn't inherit the latency-optimized API default.

Also upvoting the suggestion that `alwaysThinkingEnabled: true` with no explicit `thinkingDisplay` should default to `"summarized"` — matches user intent.

--- Comment 7 ---
Author: geraertsf
Date: 2026-04-17T08:57:29Z

Another +1 on 2.1.112 macOS with `claude --thinking-display summarized` aliased. Posting the raw jsonl diff since prior comments described it but didn't show it side-by-side from the same setup:

Before the alias, same `settings.json`:

```json
{
  "type": "thinking",
  "thinking": "",
  "signature": "<redacted>"
}
```

After the alias, next session, nothing else changed:

```json
{
  "type": "thinking",
  "thinking": " The user is asking in French, so I'll respond in French without any special formatting. To find the trailing zeros in 100!, I need to count how many times 10 divides into it, [...]",
  "signature": "<redacted>"
}
```

Signature is issued in both cases — only the `thinking` text differs, exactly matching @yusufmo1's diagnosis.

--- Comment 8 ---
Author: NtTestAlert
Date: 2026-04-17T09:43:11Z

So ofc there is no way to turn this on from the desktop app. Which just had thinking display re-introdouced in the previous update this week. Peak.

Vibecoded by Claude (only for windows): https://github.com/NtTestAlert/claude-thinking-summary-wrapper

Works for desktop app for default, if you wrap cli, probably VSCode etc too.

--- Comment 9 ---
Author: ccclapp
Date: 2026-04-17T15:29:00Z

I had posted about same problem and read the solution here.  I Primarily working via studio in the Claude Code Extension and it did not solve the problem there. Here's the solution that worked for me in VS studio Below is the copy/paste from CC generated .md file.  Attached is the md file itself

[github-reply-opus-4-7-thinking-fix.md](https://github.com/user-attachments/files/26831386/github-reply-opus-4-7-thinking-fix.md)
:

Working solution for VS Code extension on Windows (Max subscription, Opus 4.7, Claude Code 2.1.112).

The `--thinking-display summarized` CLI flag works as @alkautsarf noted, but getting it into the VS Code extension via `claudeProcessWrapper` on Windows has two traps:

- **`.cmd`/`.bat` wrappers fail with `spawn EINVAL`** — Node.js `spawn()` on Windows can't execute shell scripts without `shell: true`, which the extension doesn't set.
- **PyInstaller + `os.execv()` silently breaks stdio** — no error, but prompts go in and no output comes back. The PyInstaller bootloader's handles get orphaned when `execv` replaces the inner Python process.

**What works:** a PyInstaller-compiled Python wrapper using `subprocess.run()` to spawn claude.exe as a proper child (stdio inherited cleanly), with `--thinking-display summarized` prepended.

`claude_wrapper.py`:

```python
import subprocess, sys

CLAUDE_EXE = r"C:\Users\<you>\.local\bin\claude.exe"

def main():
    args = [CLAUDE_EXE, "--thinking-display", "summarized"] + sys.argv[1:]
    try:
        result = subprocess.run(args)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        sys.exit(130)

if __name__ == "__main__":
    main()
```

Build:

```
pip install pyinstaller
pyinstaller --onefile --console claude_wrapper.py
```

Move `dist\claude_wrapper.exe` somewhere stable (e.g. `C:\Users\<you>\.local\bin\claude-wrapper.exe`) and add to `%APPDATA%\Code\User\settings.json`:

```json
"claudeCode.claudeProcessWrapper": "C:\\Users\\<you>\\.local\\bin\\claude-wrapper.exe"
```

Reload the VS Code window. The ▸ thinking toggle now expands to live-streaming summaries on Opus 4.7, matching pre-4.7 behavior.

**For PowerShell CLI users** who just want the flag persistent without compiling anything, add this to your PowerShell profile (`notepad $PROFILE` — create the file if it doesn't exist):

```powershell
function claude {
    & "C:\Users\<you>\.local\bin\claude.exe" --thinking-display summarized @args
}
```

This handles standalone PowerShell sessions only. The VS Code graphical panel still needs the compiled wrapper above — the extension launches its own process and doesn't pick up shell aliases or functions.

Seconding the request from several comments above: a `thinkingDisplay` key in `settings.json` (mapping to the same hidden flag) would make all of this unnecessary. Until then, this is what works for Windows + VS Code.

--- Comment 10 ---
Author: dwaltrip
Date: 2026-04-17T21:06:07Z

PLEASE stop re-hiding the thinking blocks for users **who have gone out of their way to get it working again** on older versions.

If I set “showThinkingSummaries” to true, it’s for a reason. 

If you are trying to deprecate thinking blocks entirely, then just please say it up front. And ideally let us know why.

Thank you. I appreciate the hard work of the Claude code team.

--- Comment 11 ---
Author: phpmypython
Date: 2026-04-18T02:42:04Z

Posted about this [here](https://github.com/anthropics/claude-code/issues/33163) as well. I've been sed patching the minified JS for months and today they removed the minifed JS entirely so It's gonna be a nightmare trying to bring this back 

--- Comment 12 ---
Author: ccclapp
Date: 2026-04-18T02:44:51Z

> Posted about this [here](https://github.com/anthropics/claude-code/issues/33163) as well. I've been sed patching the minified JS for months and today they removed the minifed JS entirely so It's gonna be a nightmare trying to bring this back

If I understand your concern we all share it but I believe the solutions at least temporarily have been posted above by myself for VS studio and cli and others as well check above I think we have good workable temporary solutions until anthropics solves the underlying problem

--- Comment 13 ---
Author: phpmypython
Date: 2026-04-18T03:14:38Z

> > Posted about this [here](https://github.com/anthropics/claude-code/issues/33163) as well. I've been sed patching the minified JS for months and today they removed the minifed JS entirely so It's gonna be a nightmare trying to bring this back
> 
> If I understand your concern we all share it but I believe the solutions at least temporarily have been posted above by myself for VS studio and cli and others as well check above I think we have good workable temporary solutions until anthropics solves the underlying problem

[Here's](https://gist.github.com/phpmypython/a3c0267742fd65d2ebf247a5dd87ea88) my workaround for my use case which also involves using the undocumented `--thinking-display summarized` flag. 

--- Comment 14 ---
Author: ccclapp
Date: 2026-04-18T03:50:39Z

I think the short answer is: 4.7 sucks. The model is nowhere near as intuitive as 4.6 after 18 hours of usage I'm reverting back

--- Comment 15 ---
Author: betovildoza
Date: 2026-04-18T04:45:35Z

This happened to me too , the thinking blocks completely disappeared.
I spent hours testing every setting, model, and flag (just like many here) until I noticed the /thinking toggle is inverted in v2.1.112. Moving it manually to the left position fixed it instantly for me.
Even if the root cause is the Opus 4.7 harness change, this UI bug can make the summaries disappear anyway.
Worth a quick try.
Related: #49739

--- Comment 16 ---
Author: Braxbro
Date: 2026-04-18T15:09:44Z

https://github.com/anthropics/claude-code/issues/49622 Happens on Linux too - same pattern. Haven’t verified the workaround yet.

--- Comment 17 ---
Author: Bizuayeu
Date: 2026-04-21T10:27:46Z

## Still reproducing on v2.1.116 — version bump + two small wrapper tweaks

Bumping the affected-version list: the bug is still live on `anthropic.claude-code-2.1.116-win32-x64` + `claude-opus-4-7`. @yusufmo1's diagnosis still holds verbatim and @ccclapp's VS Code + PyInstaller workaround still works. Posting numbers and a couple of incremental tweaks in case they help anyone else.

### v2.1.116 numbers (same machine, same settings, wrapper toggled)

| | Thinking blocks | With content | Fill rate |
|---|---|---|---|
| Before wrapper (baseline session) | 41 | 0 | **0.0%** |
| After wrapper (fresh session A) | 6 | 6 | **100%** |
| After wrapper (fresh session B) | 5 | 5 | **100%** |

All blocks in the baseline had `signature` set and `display` missing — server-side thinking happening, `"omitted"` default stripping it on the way back, exactly as diagnosed upthread.

### Two small tweaks on top of @ccclapp's wrapper

Both are quality-of-life; the core approach (PyInstaller + `subprocess` + `claudeProcessWrapper`) is unchanged.

**1. Auto-resolve the extension directory via glob** — so the wrapper survives the next Claude Code auto-update without hand-editing a hardcoded version path:

```python
from pathlib import Path
import glob

HOME = Path.home()
EXT_BASE = HOME / ".antigravity" / "extensions"  # or ".vscode/extensions" on standard VS Code
pattern = str(EXT_BASE / "anthropic.claude-code-*-win32-x64")
claude_bin = Path(sorted(glob.glob(pattern))[-1]) / "resources" / "native-binary" / "claude.exe"
```

**2. Set `CLAUDE_CODE_EXECPATH` explicitly** before `subprocess.Popen(...)` — the bundled binary references this env var internally as its self-path, and setting it to the resolved `claude.exe` prevents any chance of wrapper re-entry if a subprocess inherits the env:

```python
env = os.environ.copy()
env["CLAUDE_CODE_EXECPATH"] = str(claude_bin)
subprocess.Popen([str(claude_bin), "--thinking-display", "summarized", *sys.argv[1:]], env=env).wait()
```

Full wrapper (~60 lines including log rotation) is a drop-in replacement for `claude_wrapper.py` in @ccclapp's steps; PyInstaller build and `settings.json` line are identical.

### One orthogonal note for v2.1.116 specifically

In case anyone else was suspecting the `[1m]` context-length suffix (`claude-opus-4-7[1m]`) as a separate capability-table issue — that path is handled in v2.1.116. The lookup table and branch exist:

```js
"[1m]"), q=Z7(H); if(q==="claude-opus-4-7") return $?"Opus 4.7 (1M context)":"Opus 4.7";
```

So `[1m]` isn't the problem. The only missing plumbing is still `thinking.display`, as OP laid out.

### Environment

- Claude Code VS Code extension **2.1.116** (auto-updated today)
- Antigravity (VS Code fork) on Windows 11
- Model: `claude-opus-4-7` (1M context), first-party Max subscription


--- Comment 18 ---
Author: Val4evr
Date: 2026-04-21T14:36:27Z

## v2.1.116 progress report: `thinkingDisplay` is half-shipped — runtime reads it, schema blocks it

Partial good news on the `thinkingDisplay` settings key that @alkautsarf proposed upthread. The read path is now in the binary — it's just blocked by the settings schema.

### Runtime reads `thinkingDisplay` as of 2.1.116

`strings` on `~/.local/share/claude/versions/2.1.116` shows the request-construction code has been patched from the `q.display ?? void 0` pattern documented earlier to an actual settings read:

```js
// ... reads w.maxThinkingTokens (a known settings.json key) ...
if (bT.type !== "disabled" &&
    (w.thinkingDisplay === "summarized" || w.thinkingDisplay === "omitted"))
    bT.display = w.thinkingDisplay;
```

Same `w` object that supplies `maxThinkingTokens`, so `thinkingDisplay` is clearly intended as a sibling settings.json key. The value flows straight to `bT.display`, which is the API request's `display` parameter — exactly the wiring asked for.

### But the schema validator rejects it

Attempting to persist it fails at write time:

```
Settings validation failed:
- : Unrecognized field: thinkingDisplay. Check for typos or refer to the documentation for valid fields
```

The embedded schema in 2.1.116 lists `alwaysThinkingEnabled`, `effortLevel`, `showThinkingSummaries`, `maxThinkingTokens` — but not `thinkingDisplay`. So users can't save the key even though the code would read it if they could.

### Net effect for end users

- Schema fix is trivial — add `thinkingDisplay` to the JSON schema with enum `["summarized", "omitted"]`.
- Until then, the **`--thinking-display summarized` CLI flag is still the only working persistent fix** (confirmed end-to-end on 2.1.116 with an `alias claude='claude --thinking-display summarized'` in `~/.zshrc`).
- `showThinkingSummaries: true` still doesn't feed into `thinkingDisplay` automatically, so @alkautsarf's "bonus" suggestion (default `display` to `"summarized"` when `alwaysThinkingEnabled: true` is set) is still unimplemented and would eliminate the footgun entirely.

Environment: macOS 15.x (Darwin 25.3), Claude Code 2.1.116, Opus 4.7 (1M context), first-party Max subscription.

--- Comment 19 ---
Author: Shadetail
Date: 2026-04-22T20:44:52Z

Confirming repro: Opus 4.7 via VS Code extension, `showThinkingSummaries: true` in `~/.claude/settings.json`. Thinking blocks never render. This matches your diagnosis exactly --- the harness seems to rely on the API-level default, which is now `omitted` on 4.7, so the setting has nothing to render. Suggested fix: have `showThinkingSummaries: true` explicitly force `display: "summarized"` on the request, since that's the only thing the setting can meaningfully do on 4.7.

--- Comment 20 ---
Author: betovildoza
Date: 2026-04-22T21:40:48Z

I'm finding that the toggle thinking is active, but it doesn't show the block, but if I turn it off, it makes it respond (it shows thinking 2s) and then It's active again; its next response does show the thinking block. Is it related to the bug? (vsc extension)

--- Comment 21 ---
Author: shawnz
Date: 2026-04-23T13:27:56Z

Copying my note here from https://github.com/anthropics/claude-code/issues/49322#issuecomment-4301009215:

I was previously using the `--thinking-display summarized` argument, together with the `claudeProcessWrapper` setting in VS Code, but I noticed it broke some things in the IDE like for example the `/plugins` command.

As an alternative, you can also set the [undocumented environment variable CLAUDE_CODE_EXTRA_BODY](https://github.com/anthropics/claude-code/issues/50141). For example, write the following in your `~/.claude/settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_EXTRA_BODY": "{\"thinking\":{\"type\":\"adaptive\",\"display\":\"summarized\"}}"
  }
}
```

You need to set `type: adaptive` because it's a mandatory parameter and the `CLAUDE_CODE_EXTRA_BODY` environment variable clobbers any existing objects specified within it (it only does a shallow merge). However, this unfortunately breaks Haiku usage which doesn't support the `type` parameter.

VS Code users might also want to see this post from @Evey-Vendetta in which they present a more comprehensive `claudeProcessWrapper` command to fix some of the issues with that approach: https://github.com/anthropics/claude-code/issues/49322#issuecomment-4302154519

--- Comment 22 ---
Author: anthrotype
Date: 2026-04-23T14:32:06Z

> Opus 4.7 via VS Code extension, showThinkingSummaries: true in ~/.claude/settings.json. Thinking blocks never render.

because its effect on the thinkingDisplay only works when claude is interactive, see https://github.com/anthropics/claude-code/issues/8477#issuecomment-4305259256

> As an alternative, you can also set the undocumented environment variable

CLAUDE_CODE_EXTRA_BODY breaks Haiku 4.5 (which doesn't support adaptive thinking).

--- Comment 23 ---
Author: hifihedgehog
Date: 2026-04-28T13:05:15Z

Same bug on Windows / VS Code extension 2.1.x with Opus 4.7. Not macOS-specific.

**Root cause is now public** (credit to the workaround in [#8477 (comment)](https://github.com/anthropics/claude-code/issues/8477#issuecomment-4269024077)): Opus 4.7 changed the API default for thinking blocks from `display: "summarized"` to `display: "omitted"`. The blocks are still in the response stream, but the `thinking` field is empty unless the caller passes `display: "summarized"` explicitly. Documented in Anthropic's own migration guide: https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7

Net effect: `showThinkingSummaries`, `alwaysThinkingEnabled`, and `viewMode: "verbose"` have nothing to render, because Claude Code does not pass `display: "summarized"` when calling the Opus 4.7 API. `showThinkingSummaries` is the documented, official way to surface thinking in the VS Code extension, and it is silently broken on Opus 4.7. The settings surface never caught up to the API change.

**Two undocumented workarounds** (from the same comment):

1. Add to `~/.claude/settings.json`:
   ```json
   {
     "env": {
       "CLAUDE_CODE_EXTRA_BODY": "{\"thinking\":{\"type\":\"adaptive\",\"display\":\"summarized\"}}"
     }
   }
   ```
2. Hidden CLI flag: `--thinking-display summarized`

The env var approach works for the VS Code extension since it delegates to the CLI.

**Why this is high-priority, not a cosmetic regression:**

Visible real-time thinking was load-bearing for the steering loop. With it visible, you could stop the model going down a wrong branch before it spent N turns of token budget on a wrong premise; you could verify it had internalized constraints from CLAUDE.md / memory rather than hallucinated them; and you could audit assumptions before committing to a plan.

With it hidden behind an unexpandable pill, you cannot tell whether a wrong final answer came from a wrong premise or a wrong execution of a right premise. Silent assumption drift becomes invisible until after the wrong action is taken. "Thought for 376s" is a duration, not a signal. It tells you nothing actionable. This is a regression in the developer's ability to supervise the agent.

**On the user side:** this is a paid product. Pro at $20/month, Max at $100–$200/month. Paying customers should not have to monkey-patch `cli.js`, reverse-engineer an undocumented `CLAUDE_CODE_EXTRA_BODY` env var, or scrape issue threads to recover functionality that worked in the previous release of the same product. The workaround being undocumented is itself a bug. The gap between what the API supports and what Claude Code exposes as a first-class setting keeps widening with every model bump.

**Related open issues, same root problem:**
- [#8477](https://github.com/anthropics/claude-code/issues/8477) — original tracking issue where the API-default change was traced and the workaround was published
- [#49757](https://github.com/anthropics/claude-code/issues/49757) — empty/unexpandable stub in VS Code extension (Opus 4.7)
- [#49902](https://github.com/anthropics/claude-code/issues/49902) — thinking summaries not rendered (VS Code extension 2.1.112)
- [#49322](https://github.com/anthropics/claude-code/issues/49322) — thinking summaries not rendered in VS Code extension (Opus 4.7)
- [#48065](https://github.com/anthropics/claude-code/issues/48065) — thinking summaries not displayed when `showThinkingSummaries` enabled
- [#49739](https://github.com/anthropics/claude-code/issues/49739) — toggle button inverted, no visual feedback (v2.1.112), likely a related UI-state bug
- [#30958](https://github.com/anthropics/claude-code/issues/30958) — earlier transcript/TUI variant of the same regression (v2.1.69)
- [#51131](https://github.com/anthropics/claude-code/issues/51131) — extended thinking dropdown no longer expandable in VS Code extension (Opus 4.7)
- [#33163](https://github.com/anthropics/claude-code/issues/33163) — "Bring back thinking" feature request, same underlying ask

What would actually resolve this:

1. Pass `display: "summarized"` by default for Opus 4.7+ when `showThinkingSummaries` and `alwaysThinkingEnabled` are on. Or expose a first-class `thinkingDisplay` setting alongside the existing `thinkingEnabled` and `effortLevel`.
2. Restore the expandable thinking block in the VS Code extension chat panel so `showThinkingSummaries` actually shows summaries when the data is present.
3. Update the docs so they reflect current `showThinkingSummaries` semantics on Opus 4.7+ instead of describing behavior that no longer applies.


--- Comment 24 ---
Author: VividNightmareUnleashed
Date: 2026-04-30T12:39:20Z

Adding **Claude Desktop (Electron)** as a third surface. Same root cause, source-level evidence below. Verified on the v1.5354 desktop bundle and `claude.exe` 2.1.121, both extracted locally.

## One gate, three surfaces

The `display: "summarized"` branch and the `redact-thinking-2026-02-12` beta header are both guarded by `!Sq()` in `claude.exe`:

```js
function Sq(){return!g8.isInteractive}
```

…where `isInteractive` is set at startup:

```js
A = q.includes("-p") || q.includes("--print")
 || q.includes("--init-only")
 || q.some(M => M.startsWith("--sdk-url"))
 || !process.stdout.isTTY;
EW6(!A);
```

Any subprocess invocation with piped stdio hits the `!isTTY` branch, so all three reported surfaces fall into the same dead-code path:

| Surface | Why `isInteractive=false` |
|---|---|
| CLI piped (CI, scripts) | `!process.stdout.isTTY` |
| VS Code extension subprocess | piped stdio, no TTY |
| Claude Desktop subprocess (CCD) | piped stdio, no TTY |

Both gated branches:

```js
// display = "summarized" — only fires when interactive
if (O.thinkingDisplay === "summarized" || O.thinkingDisplay === "omitted")
  e4.display = O.thinkingDisplay;
else if (!Sq() && Cq().showThinkingSummaries === true)
  e4.display = "summarized";

// redact-thinking-2026-02-12 beta — same guard
if (_ && EqK(H) && !Sq() && Cq().showThinkingSummaries !== true)
  q.push(NC8);
```

`showThinkingSummaries` in `~/.claude/settings.json` is structurally a no-op anywhere `claude.exe` is launched as a subprocess. Matches the reports across this thread, #48065, #49757, #49902, #49322, #51131 — same gate, three frontends.

## Confirming the Desktop never compensates

The branch that *does* fire in non-interactive mode is `O.thinkingDisplay`, set from the SDK option `thinking.display` and translated to the `--thinking-display` flag:

```js
g.type !== "disabled" && g.display && F.push("--thinking-display", g.display)
```

Searched the Desktop's renderer bundle (`app.asar` → `.vite/build/index.js`, ~15 MB) for every `thinking:` / `thinkingConfig:` callsite. Every match where `thinking:` is *set* as an SDK option lives in the cowork/Conway agent runner. The CCD `startSession` path destructures these:

```js
{ thinking: Y, effort: $, maxThinkingTokens: W, ... }
```

…and `Y` is never set for Code sessions. `--thinking-display` never lands on argv when the Desktop spawns `claude.exe`. Consistent with the VS Code extension behavior reported above.

## Capability gates aren't the blocker

For Opus 4.7 specifically, `claude.exe` confirms full support for `display: "summarized"`:

```js
function Co8(H){ /* adaptive_thinking */
  ...
  if ($ === "claude-opus-4-7" || $ === "claude-opus-4-6" || $ === "claude-sonnet-4-6") return true;
}
function fh(H){ /* effort — same model set */ }
function d78(H){ /* xhigh effort — only Opus 4.7 */
  if ($ === "claude-opus-4-7") return true;
}
```

Harness just isn't sending it.

**Reproduces on**: Windows 11, Claude Desktop 1.5354, `claude.exe` 2.1.121, Opus 4.7 (1M context). `~/.claude/settings.json` has `"showThinkingSummaries": true` per docs.


--- Comment 25 ---
Author: vinozganic
Date: 2026-05-05T10:03:07Z

@shawnz's `CLAUDE_CODE_EXTRA_BODY` workaround has a second breakage beyond Haiku: it kills the WebSearch tool for Claude Code.

With the env var set, every request the harness makes carries `thinking: {type: "adaptive", display: "summarized"}`. The first time the harness routes through a server-side `web_search_20250305` call, the API returns:
```
API Error: 400 {"type":"error","error":{"type":"invalid_request_error","message":"Thinking may not be enabled when tool_choice forces tool use."}}
```

<img width="4849" height="463" alt="Image" src="https://github.com/user-attachments/assets/f185eae9-2d5c-49c0-a105-f60e339ebc9d" />


That's the documented Anthropic constraint — extended thinking is only compatible with `tool_choice: "auto"` or `"none"`, not `{type: "tool"}` / `{type: "any"}`. The web_search server tool evidently forces `tool_choice` on at least one hop of its orchestration, and a globally-injected `thinking` object via env var leaves no way to scope it out for that path. `WebFetch` keeps working because it's a client-side tool with no forced `tool_choice`, so the breakage is specifically WebSearch.

For me that trade isn't worth it. Losing first-class Anthropic-side web search to a 400 every time you use it is a bigger functional hit than running blind on thinking summaries — at least the model still thinks, you just can't see the summary. The `--thinking-display summarized` CLI flag doesn't have this issue because it sets `display` directly instead of clobbering the entire `thinking` object into every request body, but as shawnz already noted that one breaks `/plugins`. So each of the two known workarounds disables a different surface — env var → no WebSearch, CLI flag → no /plugins. Pretty strong case for finishing the half-shipped `thinkingDisplay` key Val4evr documented in 2.1.116; the runtime already reads it from `w.thinkingDisplay`, the schema just rejects persisting it.

Reproduces on: Windows 11, Opus 4.7 (1M context, `claude-opus-4-7[1m]`), Claude Code 2.1.x via VS Code extension, `~/.claude/settings.json` exactly as shawnz posted. Removing the `env` block restores WebSearch immediately.
Also happens in the Claude Code CLI. Same thing. Also tried using Sonnet and same issue happened.

--- Comment 26 ---
Author: shawnz
Date: 2026-05-05T12:10:21Z

@vinozganic if you are trying to get this working with VS code, you should check issue #49322 which has workarounds specific to VS code. 

For example, we since found that by changing the parameter order in which you add the `--thinking-display summarized`, it fixes the issue with subcommands. See here https://github.com/anthropics/claude-code/issues/49322#issuecomment-4323290907

--- Comment 27 ---
Author: vinozganic
Date: 2026-05-05T14:40:06Z

> [@vinozganic](https://github.com/vinozganic) if you are trying to get this working with VS code, you should check issue [#49322](https://github.com/anthropics/claude-code/issues/49322) which has workarounds specific to VS code.
> 
> For example, we since found that by changing the parameter order in which you add the `--thinking-display summarized`, it fixes the issue with subcommands. See here [#49322 (comment)](https://github.com/anthropics/claude-code/issues/49322#issuecomment-4323290907)

Appreciate it brother. Successfully fixed it. Everything's now working in my VSC and Cursor (Claude Code extension)

--- Comment 28 ---
Author: xlurie
Date: 2026-05-12T12:12:32Z

**This is hurting my (and my team's) daily work — quick context on why `thinking.display` matters, and what I traced.**

I'm on a Max plan, and I want to push back on treating summarized thinking as a nice-to-have. For how I work it's load-bearing in two ways:

1. **Steering** — seeing the reasoning as it streams lets me catch the model heading the wrong way and redirect *before* it commits a full answer. Without it I only find out after the fact, and re-run.
2. **Prompt debugging** — what the model "understood" about my request is the single fastest signal for what to fix in the prompt; it's how I tighten prompts and get better results with fewer round-trips. Losing it makes every interaction slower and noisier.

After digging into this thoroughly: since around the evening of 2026-05-11, the summarized thinking block stopped arriving on `claude-opus-4-7` (and `claude-opus-4-7[1m]`). I traced it at the HTTP layer — Claude Code sends the correct request (`thinking: {"type":"adaptive","display":"summarized"}`, no `redact-thinking-*` header, `showThinkingSummaries: true` set), **byte-identical** to the request that still works on `claude-opus-4-6` / `claude-sonnet-4-6` — but the 4.7 response stream carries **zero `thinking_delta` events** (just `content_block_start(thinking)` + `signature_delta`). So this is 100% server-side, independent of Claude Code version, and it contradicts the current docs, which still tell callers to set `display: "summarized"` to get summaries on Opus 4.7. It appears specific to OAuth/subscription auth (consistent with #52376 — API-key sessions reportedly still get the summary; see also #56356), and no client-side workaround helps (tried `CLAUDE_CODE_EXTRA_BODY`, `betas`, model variants, undocumented `display` values).

Honestly: paying $200/mo and having a working feature silently disappear with no acknowledgement — and the only workaround being "switch to Opus 4.6 / Sonnet 4.6", i.e. give up the model I'm paying for — is a rough experience for a paid plan. Could the team please restore server-side honoring of `thinking.display: "summarized"` for subscription/OAuth sessions on Opus 4.7 — or, if it's intentional, say so and ship a client-side equivalent? Happy to share the full wire capture and repro steps.


--- Comment 29 ---
Author: Shadetail
Date: 2026-05-12T14:27:40Z

I've been using
```"CLAUDE_CODE_EXTRA_BODY": "{\"thinking\":{\"type\":\"adaptive\",\"display\":\"summarized\"}}"```
with
```"showThinkingSummaries": true,```
in my `settings.json` for the last few weeks which made thinking work in VS Code plugin with Opus 4.7 ever since it first broke, but yesterday I noticed it stopped working again, and all the thinking is back to being redacted.

This is the most important Claude Code feature for me! It's incredibly important that I'm able to see what Claude is thinking - not being allowed to see why AI is doing what it's doing is just insane, it's the exact opposite of safety that Anthropic prides itself on. You yourself just invented NLA because seeing Claude's thinking stream wasn't enough, you had to see it's per token thoughts as well,  for safety! So you can confirm that Claude is aligned with you, that you're working together towards the same goal, that Claude means what it says and thinks in the direction that is productive and aligned with our actual intent and our goal. Why in the world you suddenly take this away from your users? Does Claude deserve privacy now? Sure no problem, just come out and actually say it, say it why it is that you are doing this. Why are you not letting us see some of the most important data that we need to actually use the tools that many of us, myself included, pay $200 a month for? I don't want to hear conspiracy theories, I want to hear if this is a bug, or if it's intentional and official, then come out and say it.

--- Comment 30 ---
Author: betovildoza
Date: 2026-05-13T04:34:15Z

For me it's a UI/UX problem, try this in the VSC extension: move the thinking toggle to the right, send a message that makes Claude think, wait, you should see "thinking Xs" when Claude finishes, only when he finishes, write something else and before sending it, move the toggle to the left. The thinking block appears again for that session and until the compact. 
I made the #49739 due to the poor visual feedback of the system

---

### Issue #55627 — [BUG] Cowork cannot read Drive Desktop placeholder files; failed reads burn tokens on retries

State: OPEN | #55627
Labels: bug, platform:windows, area:tools, area:cowork, stale


---



### What's Wrong?

## Summary

When a user saves a file to Google Drive Desktop, Cowork (and child Cowork sub-task agents) cannot read the file because Drive Desktop has not yet materialized the file bytes to disk — the file appears in the directory listing as a placeholder cloud reference, but read attempts return "missing %PDF- header" / "file does not exist" errors. The user has to manually open the file in a local viewer to force Drive to download it, then re-prompt Cowork to retry.

This is the highest-severity issue in this bundle because each failed read can trigger a sub-task re-dispatch, each of which consumes a fresh context window. **This is the primary driver behind a user having to upgrade their Claude subscription tier — token burn from rework.**

## Environment

- **App:** Claude desktop 1.5354.0 (build `9a9e3d`, 2026-04-29)
- **OS:** Windows 11 Home, version 25H2, OS build 26200.8246
- **Storage:** Google Drive Desktop streaming mode (files-on-demand cloud sync)
- **Mode:** Cowork mode

## Reproduction

1. User saves a PDF / .md / .docx to a Drive Desktop folder (e.g., from Gmail mobile → Drive flow, or saves directly).
2. User asks Cowork to read or analyze the file using the absolute path.
3. Cowork reads the directory listing, sees the file.
4. Read attempt fails: "missing %PDF- header" / "File does not exist" / "is not a valid PDF".
5. User opens the file once locally to force Drive Desktop to download.
6. Re-prompts Cowork.
7. Now works.

## Specific examples (logged 2026-05-01)

**Example A — Jenny Latham MD Anderson treatment plan PDF:**
- File: `C:\Users\john3\My Drive\Claude\Projects\Jenny Latham\ca-treatment-breast-invasive-web-algorithm.pdf`
- Saved via Gmail mobile → Drive
- First Cowork sub-task dispatch to analyze: failed (placeholder)
- "Available offline" toggle in Drive: did NOT force download in user's experience
- Second sub-task dispatch: still failed
- User attached PDF directly to chat (bypassing Drive): SUCCEEDED, full 27 pages rendered
- **2 wasted Cowork sub-task dispatches before workaround**

**Example B — Don Call Summary 2026-05-01.md:**
- Saved by another Code-mode session to OneDrive (deprecated location) instead of canonical My Drive
- Compounded the placeholder issue with a wrong-location issue
- User had to attach to chat to unblock

**Example C — multiple ULC files in Sequel email attachments folder show in directory but fail to open repeatedly**

## Frequency

Repeatedly throughout the user's time on Cowork. Practically every time they save a new file from another device or attempt to read a recently-cloud-synced file.

## Cost impact

- User has had to upgrade Claude subscription tier specifically because of token burn from this and related retry behavior.
- Sub-task dispatches are CHILD Cowork sessions, each with their own context window. When these fail and re-dispatch, the user is paying for each failed attempt.

## Suggested investigation

- Can Cowork detect a Drive Desktop placeholder vs a materialized file BEFORE attempting to read? (Windows file attributes flag this — `FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS` or similar.)
- Can Cowork trigger Drive Desktop's "make available offline" programmatically when about to read?
- Should the Read tool retry with a delay on "missing PDF header" errors before failing?
- Could Cowork warn proactively: "This file appears to be a Drive Desktop cloud placeholder — open it once locally to materialize, then I can read it"?
- Same problem likely exists for OneDrive Files-On-Demand mode — worth checking both.
```

### Labels
`bug`, `cowork`, `file-system`, `google-drive`, `high-severity`, `cost-impact`


### What Should Happen?

Suggested investigation

- Can Cowork detect a Drive Desktop placeholder vs a materialized file BEFORE attempting to read? (Windows file attributes flag this — `FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS` or similar.)
- Can Cowork trigger Drive Desktop's "make available offline" programmatically when about to read?
- Should the Read tool retry with a delay on "missing PDF header" errors before failing?
- Could Cowork warn proactively: "This file appears to be a Drive Desktop cloud placeholder — open it once locally to materialize, then I can read it"?
- Same problem likely exists for OneDrive Files-On-Demand mode — worth checking both.


### Error Messages/Logs

```shell

```

### Steps to Reproduce

1. Save a PDF or document to a Google Drive Desktop folder (e.g., from another device, or via Gmail mobile → save-to-Drive).
2. Without manually opening the file locally, ask Claude/Cowork to read or analyze the file using its absolute path.
3. Cowork reads the directory listing successfully and sees the file.
4. The Read tool fails with "missing %PDF- header" or "File does not exist" or "is not a valid PDF" — even though the file is visibly in the folder.
5. Manually open the file in any local viewer (Notepad, Adobe, Edge) to force Drive Desktop to download the bytes.
6. Re-prompt Cowork to read the same file.
7. Read now succeeds.

Specific 2026-05-01 example: ca-treatment-breast-invasive-web-algorithm.pdf saved to My Drive\Claude\Projects\Jenny Latham\. Two Cowork sub-task dispatches failed before user attached the file directly to chat as workaround.

### Claude Model

Not sure / Multiple models

### Is this a regression?

No, this never worked

### Last Working Version

_No response_

### Claude Code Version

Claude 1.5354.0 (9a9e3d) 2026-04-29T01:14:34.000Z

### Platform

Anthropic API

### Operating System

Windows

### Terminal/Shell

Windows Terminal

### Additional Information

_No response_

# Comments on anthropics/claude-code#55627
Total: 2 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-02T17:21:49Z

Found 1 possible duplicate issue:

1. https://github.com/anthropics/claude-code/issues/40783

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: john34osborne-lgtm
Date: 2026-05-02T17:41:19Z

  Same bug occurs on Windows 11 with Google Drive Desktop streaming mode.
See #55627 for Windows repro details — attached file paths fail with
'missing %PDF- header' / 'file does not exist' errors. Adding Windows
evidence to scope

On Sat, May 2, 2026 at 12:22 PM github-actions[bot] <
***@***.***> wrote:

> *github-actions[bot]* left a comment (anthropics/claude-code#55627)
> <https://github.com/anthropics/claude-code/issues/55627#issuecomment-4364339301>
>
> Found 1 possible duplicate issue:
>
>    1. #40783 <https://github.com/anthropics/claude-code/issues/40783>
>
> This issue will be automatically closed as a duplicate in 3 days.
>
>    - If your issue is a duplicate, please close it and 👍 the existing
>    issue instead
>    - To prevent auto-closure, add a comment or 👎 this comment
>
> 🤖 Generated with Claude Code <https://claude.ai/code>
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/anthropics/claude-code/issues/55627#issuecomment-4364339301>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/CC55AOCQSFNTDMWO2UYVO2L4YYVEFAVCNFSM6AAAAACYOMTQJKVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHM2DGNRUGMZTSMZQGE>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>

---

### Issue #55631 — [BUG] Cowork scheduler stops firing recurring tasks after ~24-30 hrs uptime; only Windows reboot recovers

State: OPEN | #55631
Labels: bug, platform:windows, area:cowork, stale, area:routines


---



### What's Wrong?

The Claude desktop app's scheduled-task scheduler stops firing recurring (cron-based) tasks after some indeterminate uptime period. One-time `fireAt` tasks scheduled within the stall window also fail to fire. Restarting the Claude app does NOT recover. Only a full Windows OS reboot resets the scheduler.

### What Should Happen?

Recurring scheduled tasks should fire reliably on their cron schedule for the lifetime of the user's session. The scheduler service should:

(a) self-heal if it stalls — a watchdog that detects missed firings and recovers without requiring a Windows reboot
(b) surface errors to the user when stalls do happen, rather than failing silently
(c) recover via app restart at minimum — full OS reboot should not be required
(d) provide diagnostic logging users can access (logs from the scheduler service, missed-fire events queued for catch-up)

A user with 60+ scheduled tasks should be able to depend on them firing within a few minutes of their scheduled time, every time, for as long as the app is running.

### Error Messages/Logs

```shell
Occurrence 1 (2026-04-29 evening → 2026-04-30 night, ~24-30 hrs)**
- Last successful fire: hourly-email-triage at 4/29 13:02 UTC
- App restart attempted: did NOT resolve
- Full Windows restart: resolved. Catch-up batch fired at 5/1 04:07 UTC.

**Occurrence 2 (2026-05-01 daytime → 2026-05-02 morning, ~24+ hrs)**
- Last successful fire: daily-brief at 5/1 12:06 UTC
- Discovered: 5/2 morning when daily-brief failed to fire at 7:06 AM CT
- Possibly correlated with: PowerShell cleanup script run Fri afternoon (cleared temp folders, restarted Windows Explorer)
- Status: Windows reboot pending

## Diagnostic notes

- `/doctor` slash-command returns "not available in this environment" in Cowork — diagnostic tooling gap between Code CLI and Cowork desktop
- No visible error to user; scheduler just goes silent
```

### Steps to Reproduce

Tasks affected: ALL recurring (e.g., `daily-brief`, `hourly-email-triage`, `eod-triage`, `daily-crypto-brief`, `weekly-market-context-sunday`, `crypto-price-alerts`)
- One-time tasks scheduled within the stall window also fail to fire
- After Windows reboot: recurring tasks catch-up-fire (multiple at once) and resume normal cadence
- Restarting just the Cowork/Claude app is NOT sufficient — must be full OS reboot


### Claude Model

Not sure / Multiple models

### Is this a regression?

I don't know

### Last Working Version

_No response_

### Claude Code Version

Claude 1.5354.0 (9a9e3d) 2026-04-29T01:14:34.000Z

### Platform

Anthropic API

### Operating System

Windows

### Terminal/Shell

Windows Terminal

### Additional Information

_No response_

# Comments on anthropics/claude-code#55631
Total: 3 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2026-05-02T17:28:12Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/53413
2. https://github.com/anthropics/claude-code/issues/51296
3. https://github.com/anthropics/claude-code/issues/50920

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: john34osborne-lgtm
Date: 2026-05-02T17:44:23Z

**Confirming this also occurs on Windows 11 with Google Drive Desktop
(streaming/files-on-demand mode).** Filed as #55627; happy to merge into
this issue since the root cause looks identical (FileProvider-backed cloud
placeholder files).

**Environment:**
- Claude desktop 1.5354.0 (build `9a9e3d`, 2026-04-29)
- Windows 11 Home, 25H2, OS build 26200.8246
- Google Drive Desktop in streaming mode (files-on-demand)
- Mode: Cowork

**Repro on Windows:**
1. Save a PDF or document to a Drive Desktop folder (e.g., from another
device, or via Gmail mobile → save-to-Drive flow)
2. Without manually opening the file locally, ask Cowork to read or analyze
the file using its absolute path
3. Cowork's directory listing succeeds — file is visible
4. Read tool fails with one of:
   - `File is not a valid PDF (missing %PDF- header)`
   - `File does not exist`
   - `pdftoppm failed: Command 'pdftoppm' not found or is in an unsafe
location`
5. Manually open the file once in any local viewer (Notepad/Adobe/Edge) →
forces Drive Desktop to download bytes
6. Re-prompt Cowork → read now succeeds

**Specific 2026-05-01 example:**
- File: `ca-treatment-breast-invasive-web-algorithm.pdf` saved to `My
Drive\Claude\Projects\Jenny Latham\` via Gmail mobile → Drive
- Two Cowork sub-task dispatches failed with placeholder errors
- Workaround: user attached PDF directly to chat; this succeeded (full 27
pages rendered)
- 2 wasted sub-task dispatches consumed tokens before workaround

**Cost impact (Windows side):**
Each failed read can trigger a sub-task re-dispatch with a fresh context
window. Heavy users hit this enough times to drive subscription tier
upgrades. Token-burn lens documented in companion issue #55633 (or whatever
number) for visibility.

**Suggested fix paths (cross-platform):**
1. Detect placeholder via Windows file attribute
`FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS` (analogous to macOS FileProvider
attributes) before attempting read
2. Trigger Drive Desktop "make available offline" programmatically when
accessing a placeholder
3. At minimum, surface a clearer error: "This file is a Drive Desktop cloud
placeholder — open it once locally to materialize, then I can read it"

Same fix likely covers OneDrive Files-On-Demand mode on Windows — worth
checking both.


On Sat, May 2, 2026 at 12:28 PM github-actions[bot] <
***@***.***> wrote:

> *github-actions[bot]* left a comment (anthropics/claude-code#55631)
> <https://github.com/anthropics/claude-code/issues/55631#issuecomment-4364349939>
>
> Found 3 possible duplicate issues:
>
>    1. #53413 <https://github.com/anthropics/claude-code/issues/53413>
>    2. #51296 <https://github.com/anthropics/claude-code/issues/51296>
>    3. #50920 <https://github.com/anthropics/claude-code/issues/50920>
>
> This issue will be automatically closed as a duplicate in 3 days.
>
>    - If your issue is a duplicate, please close it and 👍 the existing
>    issue instead
>    - To prevent auto-closure, add a comment or 👎 this comment
>
> 🤖 Generated with Claude Code <https://claude.ai/code>
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/anthropics/claude-code/issues/55631#issuecomment-4364349939>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/CC55AOEXAYUPYVUMGNGPJJT4YYV4FAVCNFSM6AAAAACYOMW6X6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHM2DGNRUGM2DSOJTHE>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


--- Comment 3 ---
Author: john34osborne-lgtm
Date: 2026-05-10T23:19:40Z

👎 Cross-link from #57896 — same root cause as this issue with additional symptoms worth pinning here:

- Catch-up burst on reboot satisfies today's cron slots, so regularly-scheduled fires after the burst are skipped
- 2026-05-08 saw 5 overnight runs hard-fail with FailedToOpenSocket before silent-stall resumed
- 7-day consecutive repro (Mon-Sun May 4-10, 2026)
- Degradation window observed at ~8-12 hr (faster than the ~24-30 hr in OP)

See #57896 for full repro and suggested fix priorities.

---

### Issue #7618 — [BUG] VS Code terminal steals focus even when running Claude Code externally with /ide (terminal not open)

State: OPEN | #7618
Labels: bug, has repro, platform:macos, area:ide


---



### What's Wrong?

When using Claude Code in an external terminal, while connected to VS Code with the `/ide` command, VS Code opens the integrated terminal and steals focus upon prompt submission in the external terminal. 

### What Should Happen?

With CLI running externally, VS Code should not reveal/focus the integrated terminal unless I explicitly open it.

### Error Messages/Logs

```shell
2025-09-14 21:36:07.286 [info] Unregistered diagnostic client: client_5
2025-09-14 21:44:18.197 [info] New WS connection from: /
2025-09-14 21:44:18.198 [info] MCP server connected to transport
2025-09-14 21:44:18.198 [info] [DiagnosticStreamManager] Started streaming diagnostics
2025-09-14 21:44:18.198 [info] Registered diagnostic client: client_6
2025-09-14 21:44:19.296 [info] Closing all diff tabs in the editor...
2025-09-14 21:44:19.297 [info] Closed 0 diff tabs.
2025-09-14 21:44:19.871 [info] [DiagnosticStreamManager] Notifying 1 clients about diagnostics change for 1 files
2025-09-14 21:44:21.963 [info] WS client disconnected
2025-09-14 21:44:21.964 [info] [DiagnosticStreamManager] Unregistered client client_6. Total clients: 0
2025-09-14 21:44:21.964 [info] [DiagnosticStreamManager] Stopped streaming diagnostics
2025-09-14 21:44:21.964 [info] Unregistered diagnostic client: client_6
2025-09-14 21:45:02.704 [info] New WS connection from: /
2025-09-14 21:45:02.704 [info] MCP server connected to transport
2025-09-14 21:45:02.704 [info] [DiagnosticStreamManager] Started streaming diagnostics
2025-09-14 21:45:02.704 [info] Registered diagnostic client: client_7
2025-09-14 21:45:10.698 [info] Closing all diff tabs in the editor...
2025-09-14 21:45:10.698 [info] Closed 0 diff tabs.
2025-09-14 21:45:11.272 [info] [DiagnosticStreamManager] Notifying 1 clients about diagnostics change for 1 files
```

### Steps to Reproduce

1. Open VS Code with a workspace.
2. Ensure the integrated terminal is closed.
3. In an external terminal, run claude from the workspace root and connect with `/ide`.
4. Type a prompt and press Enter.
5. Tab back to VS Code and observe that the integrated terminal is now open.

### Claude Model

Not sure / Multiple models

### Is this a regression?

Yes, this worked in a previous version

### Last Working Version

Unsure

### Claude Code Version

1.0.113

### Platform

Anthropic API

### Operating System

macOS

### Terminal/Shell

Other

### Additional Information

Attached logs are from the CC extension in VS code. 

GhostTTY Version Info:
```
Version: 1.1.3
Build: 9438
Commit: 889478f3
```

VS Code Version Info:
```
Version: 1.104.0 (Universal)
Commit: f220831ea2d946c0dcb0f3eaa480eb435a2c1260
Date: 2025-09-10T06:46:18.035Z
Electron: 37.3.1
ElectronBuildId: 12342881
Chromium: 138.0.7204.235
Node.js: 22.18.0
V8: 13.8.258.31-electron.0
OS: Darwin arm64 24.6.0
```

# Comments on anthropics/claude-code#7618
Total: 19 comments

--- Comment 1 ---
Author: github-actions[bot]
Date: 2025-09-15T04:52:11Z

Found 3 possible duplicate issues:

1. https://github.com/anthropics/claude-code/issues/1591
2. https://github.com/anthropics/claude-code/issues/3419
3. https://github.com/anthropics/claude-code/issues/6919

This issue will be automatically closed as a duplicate in 3 days.

- If your issue is a duplicate, please close it and 👍 the existing issue instead
- To prevent auto-closure, add a comment or 👎 this comment

🤖 Generated with [Claude Code](https://claude.ai/code)

--- Comment 2 ---
Author: openclosure
Date: 2025-09-15T06:35:48Z

Not a duplicate. There are several references to this bug in JetBrains products but I haven't seen a report of this for VS Code/Cursor. 

--- Comment 3 ---
Author: dzhlobo
Date: 2025-09-15T08:43:23Z

I can confirm the bug report, I observe the same behaviour.

I use latest Ghostty from main branch (version 0c63946bd, build 12105).

Claude Code version 1.0.112 (Claude Code).

VSCode version info:
```
Version: 1.104.0
Commit: f220831ea2d946c0dcb0f3eaa480eb435a2c1260
Date: 2025-09-10T06:46:18.035Z (5 days ago)
Electron: 37.3.1
ElectronBuildId: 12342881
Chromium: 138.0.7204.235
Node.js: 22.18.0
V8: 13.8.258.31-electron.0
OS: Darwin arm64 24.6.0
```

--- Comment 4 ---
Author: TouchSeyha
Date: 2025-11-03T04:50:28Z

Just confirming that this bug is still reproducible in November with Claude Code CLI 2.0.31.
The issue reported back in September seems to persist in the current release. But I'm using window platform.

--- Comment 5 ---
Author: dhaern
Date: 2025-11-08T02:07:47Z

Claude Code v2.0.36 and confirming this bug AGAIN, can you  work a bit more instead doing nothing please?

--- Comment 6 ---
Author: github-actions[bot]
Date: 2025-12-09T10:22:42Z

This issue has been inactive for 30 days. If the issue is still occurring, please comment to let us know. Otherwise, this issue will be automatically closed in 30 days for housekeeping purposes.

--- Comment 7 ---
Author: etrippler
Date: 2025-12-10T17:08:39Z

This issue is still occuring!

--- Comment 8 ---
Author: Jay-523
Date: 2025-12-15T14:31:28Z

Able to reproduce this issue with warp and cursor

--- Comment 9 ---
Author: MartinLoeper
Date: 2025-12-28T15:44:31Z

I think the best workaround here would be to just introduce a new vscode extension setting to opt-out of the current behaviour which seems to open the terminal panel and focus it.

--- Comment 10 ---
Author: ankit-kapur
Date: 2026-01-15T02:30:23Z

Still occurring, please fix

--- Comment 11 ---
Author: dcrew44
Date: 2026-02-04T19:14:13Z

Still occurring, please fix


--- Comment 12 ---
Author: JoshChapnick
Date: 2026-02-05T16:58:40Z

Still running into this - please fix

--- Comment 13 ---
Author: ezeqviel
Date: 2026-02-15T21:35:06Z

issue persists on 2.1.42

--- Comment 14 ---
Author: jdvolk
Date: 2026-02-23T22:50:51Z

also confirming this. is there a way to disconnect clude-cli from the claude extention in vs code?


--- Comment 15 ---
Author: Nick-Lucas
Date: 2026-03-19T15:03:31Z

Happening for me on 2.1.79

--- Comment 16 ---
Author: yurukusa
Date: 2026-03-31T03:42:05Z

The focus-stealing happens because the `/ide` connection triggers VS Code to open/activate its terminal panel. Workarounds:
**Workaround 1 — Prevent terminal auto-focus in VS Code:**
```json
// VS Code settings.json
{
  "terminal.integrated.focusAfterRun": "none",
  "terminal.integrated.showExitAlert": false
}
```
This prevents VS Code from auto-focusing the terminal panel when Claude Code sends commands through the IDE integration.
**Workaround 2 — Use a separate VS Code window:**
Keep your code in one VS Code window and let Claude's `/ide` connection go to a different window. Focus changes in the second window won't interrupt your work in the first.
**Workaround 3 — Don't use /ide, use file paths instead:**
If you primarily need Claude to edit files, it can do so via the Edit/Write tools without IDE integration:
```markdown
<!-- CLAUDE.md -->
Edit files directly using the Edit tool. Do not use IDE integration.
```
The `/ide` connection is mainly useful for features like "go to definition" and inline diffs. If you don't need those, skipping `/ide` avoids the focus issue entirely.
**Workaround 4 — Use the VS Code extension instead of external terminal + /ide:**
The Native UI mode in the extension handles IDE integration without the focus-stealing issue, since Claude runs inside VS Code natively.


--- Comment 17 ---
Author: barafael
Date: 2026-04-01T18:26:36Z

now, (for me), it happens _twice_, on startup. That's quite disruptive.

--- Comment 18 ---
Author: dmcconachie
Date: 2026-04-08T14:03:24Z

https://github.com/anthropics/claude-code/issues/7618#issuecomment-4159655672 

(1) does not work; see https://github.com/anthropics/claude-code/issues/23713 for an explanation

(2) This is very awkward; now I'm juggling 3 windows (VSCode 1 where I do my work, VSCode 2 whose only purpose is to feed context to CC, an external terminal running claude code). Also VSCode doesn't really like to have 2 windows open to the same project as far as I know, though I haven't tried it in some time. Historically the only way I've managed to do it was to have one window open to the folder, one window open to a VSCode workspace in the same folder.

(3) That also defeats the entire purpose of having ide integration. "Don't use the thing" is not a workaround

(4) Also defeats the entire purpose of /ide integration

--- Comment 19 ---
Author: PhilChen-6765
Date: 2026-05-04T23:32:01Z

Still reproducible on Claude Code v2.1.126 / VS Code Claude Code extension v2.1.126 (macOS).

  **Environment**
  - OS: macOS
  - External terminal: Ghostty
  - Claude Code CLI: v2.1.126
  - VS Code with Claude Code extension v2.1.126

  **Reproduction**
  1. Run `claude` in Ghostty
  2. `/ide` → "Connected to Visual Studio Code"
  3. Send any prompt — even one that doesn't trigger any tool call
  4. VS Code's integrated terminal panel pops open / steals focus
  5. Happens on every prompt

  **New finding — narrows down the trigger**
  The pop-up only happens if **at least one integrated terminal instance already exists** in the current VS Code
  session. Specifically:

  | State of VS Code's integrated terminal | Pop-up on prompt? |
  |---|---|
  | Never opened in this VS Code session | ✅ No pop-up |
  | Opened before, then hidden (`Cmd+J`) | ❌ Pops back |
  | Opened and visible | ❌ Steals focus |

  Workaround: restart VS Code and never manually open an integrated terminal. The pop-up does not occur as long as no
   terminal instance exists.

---
