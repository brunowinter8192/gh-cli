#!/usr/bin/env python3
"""
Extract real gh-cli tool invocations and their results from Monitor_CC proxy logs.

Streams api_requests_*.jsonl files, collects Bash tool_use blocks whose command
contains 'gh-cli', deduplicates by tool_use id, pairs with tool_result blocks,
and writes one JSONL record per unique call.

Usage:
    ./venv/bin/python dev/ghcli_usage/extract_ghcli_calls.py
    ./venv/bin/python dev/ghcli_usage/extract_ghcli_calls.py --logs-dir /path/to/logs
    ./venv/bin/python dev/ghcli_usage/extract_ghcli_calls.py --max-result-chars 2000
"""

# INFRASTRUCTURE

import argparse
import json
import re
from collections import Counter
from pathlib import Path

MONITOR_CC_LOGS_DIR = '/Users/brunowinter2000/Documents/ai/Monitor_CC/src/logs'
DEFAULT_OUT_DIR = Path(__file__).parent


# ORCHESTRATOR

def extract_ghcli_calls_workflow(args):
    log_files = discover_log_files(args.logs_dir)
    all_records = []
    seen_ids = set()
    lines_total = 0
    prededup_total = 0
    for log_path in log_files:
        records, new_ids, lines, prededup = process_log_file(
            log_path, seen_ids, args.max_result_chars
        )
        all_records.extend(records)
        seen_ids = seen_ids | new_ids
        lines_total += lines
        prededup_total += prededup
    out_path = Path(args.out_dir) / 'ghcli_calls.jsonl'
    write_jsonl(all_records, out_path)
    print_stats(all_records, lines_total, prededup_total, len(log_files))


# FUNCTIONS

def discover_log_files(logs_dir):
    return sorted(Path(logs_dir).glob('api_requests_*.jsonl'))


def parse_project(fname):
    base = Path(fname).stem
    rest = base[len('api_requests_'):]
    m = re.match(r'^(.+)_(\d+)$', rest)
    if not m:
        return 'unknown'
    without_ts = m.group(1)
    if without_ts.startswith('worker_'):
        parts = without_ts.split('_', 2)
        return parts[2] if len(parts) > 2 else 'unknown'
    parts = without_ts.split('_', 1)
    return parts[1] if len(parts) > 1 else 'unknown'


def parse_raw_payload(obj):
    rp = obj.get('raw_payload', {})
    if isinstance(rp, str):
        try:
            rp = json.loads(rp)
        except json.JSONDecodeError:
            return {}
    return rp if isinstance(rp, dict) else {}


def ghcli_invocation_subcommand(command):
    """
    Return the gh-cli subcommand if 'command' actually invokes gh-cli as a shell command,
    else return None (filters out mentions in comments, echo strings, grep patterns, heredocs).

    A real invocation: 'gh-cli' appears at the start of a shell segment (after optional
    env-var assignments), not inside a comment line, grep argument, or heredoc body.
    """
    for line in command.split('\n'):
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        # Split on shell separators ; && || (not single | which is a pipe within a call)
        segments = re.split(r'\s*(?:&&|\|\||;)\s*', stripped)
        for seg in segments:
            seg = seg.strip()
            # Strip leading env-var assignments: [export] VARNAME=value
            seg = re.sub(r'^(?:(?:export\s+)?\w+=\S*\s+)+', '', seg).strip()
            if seg.startswith('gh-cli'):
                rest = seg[len('gh-cli'):].strip()
                tokens = rest.split()
                return tokens[0] if tokens else ''
    return None


def extract_tool_uses_and_results(messages, wanted_ids):
    """Walk message content blocks; return new tool_uses, results for known ids, prededup count."""
    tool_uses = {}
    tool_results = {}
    prededup = 0
    for msg in messages:
        content = msg.get('content')
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            btype = block.get('type')
            if btype == 'tool_use' and block.get('name') == 'Bash':
                cmd = block.get('input', {}).get('command', '')
                if 'gh-cli' not in cmd:
                    continue
                subcmd = ghcli_invocation_subcommand(cmd)
                if subcmd is None:
                    continue  # gh-cli only in comment/string/grep — not a real invocation
                tid = block.get('id', '')
                prededup += 1
                if tid not in wanted_ids and tid not in tool_uses:
                    tool_uses[tid] = {'command': cmd, 'subcommand': subcmd}
            elif btype == 'tool_result':
                tid = block.get('tool_use_id', '')
                if tid not in tool_results and (tid in wanted_ids or tid in tool_uses):
                    raw_content = block.get('content') or ''
                    if isinstance(raw_content, list):
                        raw_content = ' '.join(
                            b.get('text', '') if isinstance(b, dict) else str(b)
                            for b in raw_content
                        )
                    tool_results[tid] = {
                        'content': raw_content,
                        'is_error': block.get('is_error'),
                    }
    return tool_uses, tool_results, prededup


def process_log_file(log_path, seen_ids, max_result_chars):
    fname = log_path.name
    project = parse_project(fname)
    file_tool_uses = {}
    file_tool_results = {}
    lines_scanned = 0
    prededup_total = 0

    with open(log_path, encoding='utf-8', errors='replace') as f:
        for line in f:
            lines_scanned += 1
            if 'gh-cli' not in line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            ts = obj.get('timestamp', '')
            rp = parse_raw_payload(obj)
            messages = rp.get('messages', [])
            all_wanted = seen_ids | set(file_tool_uses.keys())
            new_tu, new_tr, prededup = extract_tool_uses_and_results(messages, all_wanted)
            prededup_total += prededup
            for tid, info in new_tu.items():
                file_tool_uses[tid] = {**info, 'timestamp': ts, 'log': fname, 'project': project}
            for tid, result in new_tr.items():
                if tid not in file_tool_results:
                    file_tool_results[tid] = result

    records = [
        build_record(tid, tu_info, file_tool_results.get(tid, {}), max_result_chars)
        for tid, tu_info in file_tool_uses.items()
    ]
    return records, set(file_tool_uses.keys()), lines_scanned, prededup_total


# extract_subcommand is superseded by ghcli_invocation_subcommand (line-aware, used at parse time)


def is_found_zero(text):
    if not text:
        return False
    lower = text.lower()
    return 'found 0' in lower or 'no results' in lower


def build_record(tid, tu_info, tr_info, max_result_chars):
    command = tu_info.get('command', '')
    result_text = tr_info.get('content', '') or ''
    if max_result_chars > 0:
        result_text = result_text[:max_result_chars]
    is_error = tr_info.get('is_error')
    return {
        'tool_use_id': tid,
        'session_log': tu_info.get('log', ''),
        'project': tu_info.get('project', ''),
        'timestamp': tu_info.get('timestamp', ''),
        'command': command,
        'subcommand': tu_info.get('subcommand', ''),
        'result_text': result_text,
        'result_chars': len(result_text),
        'is_error': bool(is_error) if is_error is not None else False,
        'found_zero': is_found_zero(result_text),
    }


def write_jsonl(records, out_path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    print(f"Wrote {len(records)} records → {out_path}", flush=True)


def print_stats(records, lines_total, prededup_total, files_count):
    print(f"\n=== EXTRACTION STATS ===")
    print(f"Files scanned:            {files_count}")
    print(f"Lines scanned:            {lines_total:,}")
    print(f"Pre-dedup gh-cli hits:    {prededup_total:,}")
    print(f"Unique gh-cli calls:      {len(records)}")

    subcmd_counts = Counter(r['subcommand'] for r in records)
    print(f"\nSubcommand distribution:")
    for cmd, cnt in subcmd_counts.most_common():
        print(f"  {cnt:3d}  {cmd or '(empty)'}")

    project_counts = Counter(r['project'] for r in records)
    print(f"\nProject distribution:")
    for proj, cnt in project_counts.most_common():
        print(f"  {cnt:3d}  {proj}")

    error_count = sum(1 for r in records if r['is_error'])
    found_zero_count = sum(1 for r in records if r['found_zero'])
    no_result_count = sum(1 for r in records if not r['result_text'])
    print(f"\nError count:              {error_count}")
    print(f"Found-zero count:         {found_zero_count}")
    print(f"No result (unpaired):     {no_result_count}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Extract gh-cli calls from Monitor_CC proxy logs.'
    )
    parser.add_argument(
        '--logs-dir', default=MONITOR_CC_LOGS_DIR,
        help='Directory containing api_requests_*.jsonl files'
    )
    parser.add_argument(
        '--out-dir', default=str(DEFAULT_OUT_DIR),
        help='Output directory for ghcli_calls.jsonl'
    )
    parser.add_argument(
        '--max-result-chars', type=int, default=0,
        help='Truncate result_text to N chars (0 = full)'
    )
    args = parser.parse_args()
    extract_ghcli_calls_workflow(args)
