#!/usr/bin/env python3
# Measure junk class B (DEBUG_STREAM — app debug/log lines pasted from a terminal, NOT
# build/install output, which is class A / strip_build_logs) on the current github_issues corpus.
# Read-only: never modifies the corpus, never writes anything but its own report. No detector, no
# strip — this milestone is measurement + a written proposal only.
#
# Vocabulary (derived by reading real corpus files, not from the inventory's 3 examples alone —
# see process-docs/content_cleaning/):
#   - ghostty_debug:    ^(debug|info|warning)\([a-zA-Z_]+\):        e.g. "debug(app): mailbox message=redraw_surface"
#   - playwright_pw:    ^\s*pw:[a-z:]+                              e.g. "pw:channel:event {", "pw:browser [pid=N][out] ..."
#   - loguru_narration: TIMESTAMP | LEVEL | module:func:line - msg, LEVEL in {TRACE,DEBUG,INFO,SUCCESS,WARNING}
#                       ERROR/CRITICAL levels deliberately excluded — those are the retrieval target.
#
# Protection baseline (verbatim copy of src/github/text_cleaning.py's hard exclusions — the
# "currently protected" set) plus a PROPOSED, measurement-only extension found while reading
# ghostty__10406.md/ghostty__10379.md: real crash indicators (panic/segfault/SIG*/aborted, and
# unresolved "???:?:?:" backtrace frames) that match none of ERROR_RE/TRACE_RE/BACKTRACE_RE. The
# proposed regexes are never wired into any strip; whether they belong in text_cleaning.py is a
# later decision made on this milestone's dump, per the process this area's earlier work follows.
#
# Usage: python3 dev/content_cleaning/08_audit_debug_stream.py [--source-dir PATH]

# INFRASTRUCTURE

import argparse
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

DEFAULT_SOURCE_DIR = Path(
    "/Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli/"
    "data/documents/github_issues"
)
REPORT_DIR = Path(__file__).parent / "md"

# Minimum occurrence count for a line (literal or normalized) to count as "repeated" — matches the
# inventory's cross-cutting "J" detector threshold.
REPEAT_THRESHOLD = 5
# Adjacency windows (lines) checked around each candidate for a protected line nearby.
ADJACENCY_WINDOWS = [0, 3, 10]

# --- verbatim copy of src/github/text_cleaning.py's hard exclusions ("currently protected") -----
ERROR_RE = re.compile(r'error|fatal|traceback|exception|failed', re.IGNORECASE)
TRACE_RE = re.compile(r'^\s*File "[^"]+", line \d+, in ')
BACKTRACE_RE = re.compile(r':\d+:\d+:.*0x[0-9a-fA-F]+ in ')

# --- proposed additional protection — measurement-only, not wired into any strip ----------------
# Found reading ghostty__10406.md (line 615: "Segmentation fault at address 0x...", followed by
# unresolved "???:?:?: 0x... in ??? (lib.so)" frames) and ghostty__10379.md (line 606: "thread
# 34041 panic: ..." sitting one line after the last debug(app) narration line, zero-line gap).
# None of these match ERROR_RE/TRACE_RE/BACKTRACE_RE.
PROPOSED_CRASH_RE = re.compile(
    r'panic:|Segmentation fault|SIG(ABRT|SEGV|ILL|BUS|FPE)\b|Aborted \(core dumped\)',
    re.IGNORECASE,
)
PROPOSED_UNRESOLVED_FRAME_RE = re.compile(r'^\?\?\?:\?:\?:.*0x[0-9a-fA-F]+ in ')

# --- candidate class-B vocabulary -----------------------------------------------------------
SHAPES = {
    "ghostty_debug": re.compile(r'^(debug|info|warning)\([a-zA-Z_]+\):'),
    "playwright_pw": re.compile(r'^\s*pw:[a-z:]+'),
    "loguru_narration": re.compile(
        r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+ \| (TRACE|DEBUG|INFO|SUCCESS|WARNING)\s*\|'
    ),
}

# --- fingerprint normalization: numbers, hex addresses, UUIDs, timestamps -> placeholders -------
_UUID_RE = re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', re.IGNORECASE)
_HEX_RE = re.compile(r'0x[0-9a-fA-F]+')
_TIMESTAMP_RE = re.compile(r'\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(\.\d+)?')
_NUM_RE = re.compile(r'\d+')


@dataclass
class FileResult:
    filename: str
    repo: str
    file_chars: int
    shape_lines: dict = field(default_factory=dict)       # shape -> matched line count
    shape_chars: dict = field(default_factory=dict)       # shape -> matched char count
    shape_runs: dict = field(default_factory=dict)        # shape -> list[(start,end) 0-idx]
    literal_repeats: dict = field(default_factory=dict)   # line -> count (>=threshold)
    fingerprint_repeats: dict = field(default_factory=dict)  # norm -> (count, example_line)


# FUNCTIONS

# True if line matches any of the existing, currently-shipped hard exclusions
def _is_protected_existing(line: str) -> bool:
    return bool(ERROR_RE.search(line) or TRACE_RE.search(line) or BACKTRACE_RE.search(line))


# True under the existing exclusions OR the proposed, measurement-only extension
def _is_protected_proposed(line: str) -> bool:
    return (_is_protected_existing(line) or bool(PROPOSED_CRASH_RE.search(line))
            or bool(PROPOSED_UNRESOLVED_FRAME_RE.match(line)))


# Replace UUIDs, hex addresses, timestamps, and bare digit runs with placeholders
def _normalize_fingerprint(line: str) -> str:
    l = _UUID_RE.sub('<UUID>', line)
    l = _HEX_RE.sub('<HEX>', l)
    l = _TIMESTAMP_RE.sub('<TS>', l)
    l = _NUM_RE.sub('<N>', l)
    return l


# Group shape-matched lines (that are not currently/proposed protected, per protected_fn) into
# maximal (start, end) runs, 0-indexed inclusive; blank lines bridge a run but never extend or
# confirm it alone — mirrors _find_build_log_blocks's bridging discipline at single-vocabulary scale
def _find_shape_runs(lines: list, shape_re: "re.Pattern", protected_fn) -> list:
    def is_signal(line: str) -> bool:
        return bool(shape_re.match(line)) and not protected_fn(line)

    n = len(lines)
    runs = []
    i = 0
    while i < n:
        if not is_signal(lines[i]):
            i += 1
            continue
        start = i
        end = i
        j = i + 1
        while j < n:
            if is_signal(lines[j]):
                end = j
                j += 1
                continue
            if lines[j].strip() == '':
                j += 1
                continue
            break
        runs.append((start, end))
        i = end + 1
    return runs


# Bucket run lengths for the report's histogram
def _run_length_bucket(length: int) -> str:
    if length <= 2:
        return "1-2"
    if length <= 5:
        return "3-5"
    if length <= 9:
        return "6-9"
    if length <= 19:
        return "10-19"
    if length <= 49:
        return "20-49"
    return "50+"


# Count of shape-matched lines with a protected line within +/-window (0 = the line itself)
def _adjacency_count(lines: list, shape_re: "re.Pattern", protected_fn, window: int) -> int:
    n = len(lines)
    count = 0
    for i, line in enumerate(lines):
        if not shape_re.match(line):
            continue
        lo, hi = max(0, i - window), min(n - 1, i + window)
        if any(protected_fn(lines[j]) for j in range(lo, hi + 1)):
            count += 1
    return count


# Measure everything for one file: per-shape lines/chars/runs, literal repeats, fingerprint repeats
def measure_file(fp: Path) -> FileResult:
    text = fp.read_text(errors='replace')
    lines = text.splitlines()
    repo = fp.name.split('__')[0]
    fr = FileResult(filename=fp.name, repo=repo, file_chars=len(text))

    for shape_name, shape_re in SHAPES.items():
        matched = [l for l in lines if shape_re.match(l)]
        if matched:
            fr.shape_lines[shape_name] = len(matched)
            fr.shape_chars[shape_name] = sum(len(l) + 1 for l in matched)
            fr.shape_runs[shape_name] = _find_shape_runs(lines, shape_re, _is_protected_existing)

    literal_c = Counter(l for l in lines if l.strip())
    fr.literal_repeats = {l: n for l, n in literal_c.items() if n >= REPEAT_THRESHOLD}

    fp_c = Counter()
    fp_example = {}
    for l in lines:
        if not l.strip():
            continue
        norm = _normalize_fingerprint(l)
        fp_c[norm] += 1
        fp_example.setdefault(norm, l)
    fr.fingerprint_repeats = {
        norm: (n, fp_example[norm]) for norm, n in fp_c.items() if n >= REPEAT_THRESHOLD
    }

    return fr


def measure_all(md_files: list) -> list:
    return [measure_file(fp) for fp in md_files]


# Corpus-wide adjacency numbers (existing vs. existing+proposed protection), for the stdout summary
def measure_adjacency(md_files: list) -> dict:
    rows = {}
    for shape_name, shape_re in SHAPES.items():
        rows[shape_name] = {}
        for window in ADJACENCY_WINDOWS:
            existing_total = 0
            proposed_total = 0
            for fp in md_files:
                lines = fp.read_text(errors='replace').splitlines()
                existing_total += _adjacency_count(lines, shape_re, _is_protected_existing, window)
                proposed_total += _adjacency_count(lines, shape_re, _is_protected_proposed, window)
            rows[shape_name][window] = (existing_total, proposed_total)
    return rows


def _render_shape_section(shape_name: str, results: list) -> list:
    affected = [r for r in results if r.shape_lines.get(shape_name)]
    total_lines = sum(r.shape_lines.get(shape_name, 0) for r in results)
    total_chars = sum(r.shape_chars.get(shape_name, 0) for r in results)
    by_repo = Counter()
    for r in affected:
        by_repo[r.repo] += r.shape_lines[shape_name]
    run_buckets = Counter()
    for r in affected:
        for start, end in r.shape_runs.get(shape_name, []):
            run_buckets[_run_length_bucket(end - start + 1)] += 1

    section = [
        f"\n## Shape: `{shape_name}`\n",
        f"Files: {len(affected)} · Lines: {total_lines} · Chars: {total_chars:,}",
        f"\nBy repo: {dict(by_repo)}",
        f"\nRun-length histogram (bucket -> run count): "
        f"{ {k: run_buckets[k] for k in ['1-2','3-5','6-9','10-19','20-49','50+'] if run_buckets[k]} }",
        "\n### Per-file evidence (top 15 by matched lines)\n",
    ]
    for r in sorted(affected, key=lambda x: -x.shape_lines[shape_name])[:15]:
        lines = (DEFAULT_SOURCE_DIR / r.filename).read_text(errors='replace').splitlines()
        example = next((l for l in lines if SHAPES[shape_name].match(l)), "")
        section.append(f"- `{r.filename}`: {r.shape_lines[shape_name]} lines, "
                  f"{len(r.shape_runs.get(shape_name, []))} run(s) — e.g. `{example[:140]}`")
    return section


def _render_repeat_comparison_section(results: list) -> list:
    section = ["\n## Literal-repeat vs. normalized-fingerprint repeats (corpus-wide)\n"]
    literal_files = [r for r in results if r.literal_repeats]
    fp_files = [r for r in results if r.fingerprint_repeats]
    literal_instances = sum(sum(r.literal_repeats.values()) for r in results)
    fp_instances = sum(sum(n for n, _ in r.fingerprint_repeats.values()) for r in results)
    section.append(f"Literal repeats (>= {REPEAT_THRESHOLD}x, exact line): {len(literal_files)} files, "
              f"{literal_instances} repeated-line instances.")
    section.append(f"Normalized-fingerprint repeats (>= {REPEAT_THRESHOLD}x, digits/hex/UUID/timestamp "
              f"collapsed): {len(fp_files)} files, {fp_instances} repeated-line instances.")
    section.append(f"Delta (instances the fingerprint measure surfaces that literal repeat misses): "
              f"{fp_instances - literal_instances}.")
    return section


def _render_fingerprint_delta_section(results: list) -> list:
    section = ["\n### Files where fingerprinting surfaces materially more than literal repeat\n"]
    for r in sorted(results, key=lambda x: -(sum(n for n, _ in x.fingerprint_repeats.values())
                                              - sum(x.literal_repeats.values())))[:15]:
        lit = sum(r.literal_repeats.values())
        fp = sum(n for n, _ in r.fingerprint_repeats.values())
        if fp - lit <= 0:
            continue
        section.append(f"- `{r.filename}`: literal={lit}, fingerprint={fp} (+{fp - lit})")
        top_fp = sorted(r.fingerprint_repeats.items(), key=lambda x: -x[1][0])[:2]
        for norm, (n, example) in top_fp:
            section.append(f"    {n}x normalized: `{norm[:120]}` — e.g. `{example[:120]}`")
    return section


def write_report(path: Path, results: list, total_files: int) -> None:
    o = [
        f"# Class B (DEBUG_STREAM) Audit Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\nCorpus: {total_files} files · `data/documents/github_issues/`",
    ]

    for shape_name in SHAPES:
        o += _render_shape_section(shape_name, results)

    o += _render_repeat_comparison_section(results)
    o += _render_fingerprint_delta_section(results)

    path.write_text('\n'.join(o) + '\n')


# ORCHESTRATOR

def audit_workflow(source_dir: Path) -> None:
    md_files = sorted(source_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {source_dir}", file=sys.stderr)
        sys.exit(1)

    results = measure_all(md_files)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = REPORT_DIR / f"08_audit_{ts}.md"
    write_report(report_path, results, len(md_files))
    print(f"report: {report_path}")

    for shape_name in SHAPES:
        affected = [r for r in results if r.shape_lines.get(shape_name)]
        total_lines = sum(r.shape_lines.get(shape_name, 0) for r in results)
        total_chars = sum(r.shape_chars.get(shape_name, 0) for r in results)
        total_chars_corpus = sum(r.file_chars for r in results)
        pct = 100 * total_chars / total_chars_corpus if total_chars_corpus else 0
        print(f"shape={shape_name} files={len(affected)} lines={total_lines} "
              f"chars={total_chars} pct_corpus={pct:.2f}%")

    literal_files = [r for r in results if r.literal_repeats]
    fp_files = [r for r in results if r.fingerprint_repeats]
    literal_instances = sum(sum(r.literal_repeats.values()) for r in results)
    fp_instances = sum(sum(n for n, _ in r.fingerprint_repeats.values()) for r in results)
    print(f"literal_repeats files={len(literal_files)} instances={literal_instances}")
    print(f"fingerprint_repeats files={len(fp_files)} instances={fp_instances} "
          f"delta={fp_instances - literal_instances}")

    adjacency = measure_adjacency(md_files)
    for shape_name, rows in adjacency.items():
        for window, (existing, proposed) in rows.items():
            print(f"adjacency shape={shape_name} window={window} "
                  f"protected_existing={existing} protected_existing+proposed={proposed}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Measure junk class B (DEBUG_STREAM) on the github_issues corpus — read-only"
    )
    p.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    args = p.parse_args()
    audit_workflow(args.source_dir)
