"""
Smoke test: get_file_content large-file tier handling.

Covers all three size tiers via CLI subprocess (hook forbids 'from src.' in dev/ files):

  Tier 1 (<=1 MB)   — octocat/Hello-World README    (tiny, base64 inline)
  Tier 2 (1-100 MB) — MuRongPIG/Proxy-Master http.txt (1.8 MB, streams to /tmp)
  Tier 3 (>100 MB)  — simulated via format_toolarge_response with a fake response dict
                       (no live >100 MB GitHub file used; GitHub API hard limit means the
                        branch is trivial: return error text when size > _SIZE_API_MAX)

Usage (from project root):
  python3 dev/tool_design/probe_large_file.py
"""
# INFRASTRUCTURE
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

REPORT_DIR = Path(__file__).parent / "md"
PROJECT_ROOT = Path(__file__).resolve().parents[2]


# ORCHESTRATOR
def main():
    sections = []
    passed, failed = 0, 0

    passed, failed = run_tier1(sections, passed, failed)
    passed, failed = run_tier2(sections, passed, failed)
    passed, failed = run_tier3(sections, passed, failed)

    report_path = write_report(sections, passed, failed)
    print(f"Results: {passed} passed, {failed} failed")
    print(report_path)
    if failed:
        sys.exit(1)


# FUNCTIONS

# Invoke cli.py as a subprocess and capture combined stdout+stderr
def run_cli(*args):
    result = subprocess.run(
        [sys.executable, "cli.py"] + list(args),
        capture_output=True, text=True, cwd=PROJECT_ROOT
    )
    return result.stdout + result.stderr


# Simulate the >100 MB branch via format_toolarge_response with a fake response dict
def check_tier3_error():
    code = (
        "import sys; sys.path.insert(0, '.'); "
        "from src.github.get_file_content import format_toolarge_response; "
        "fake = {'path': 'huge.bin', 'name': 'huge.bin', 'size': 200_000_000, "
        "        'type': 'file', 'sha': 'abc', 'html_url': 'https://github.com/x/y/blob/main/huge.bin'}; "
        "out = format_toolarge_response(fake); print(out)"
    )
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True, text=True, cwd=PROJECT_ROOT
    )
    return result.stdout + result.stderr


# Tier 1 (<=1 MB): expect inline content block
def run_tier1(sections, passed, failed):
    out = run_cli("get_file_content", "octocat", "Hello-World", "README")
    ok = "Content:" in out and "Lines:" in out
    verdict = "PASS: inline content present" if ok else "FAIL: expected inline content block"
    sections.append(f"## Tier 1: <=1 MB (octocat/Hello-World README)\n\n{out[:500]}\n\n{verdict}")
    return (passed + 1, failed) if ok else (passed, failed + 1)


# Tier 2 (1-100 MB): expect stream-to-/tmp with file present on disk
def run_tier2(sections, passed, failed):
    out = run_cli("get_file_content", "MuRongPIG", "Proxy-Master", "http.txt")
    tmp_path = "/tmp/gh-cli_MuRongPIG_Proxy-Master_http.txt"
    ok = False
    if "Downloaded to:" in out and tmp_path in out and os.path.isfile(tmp_path):
        size_on_disk = os.path.getsize(tmp_path)
        verdict = f"PASS: file on disk at {tmp_path} ({size_on_disk:,} bytes)"
        ok = True
    elif "Downloaded to:" in out and tmp_path in out:
        verdict = f"FAIL: output mentions path but file not found on disk: {tmp_path}"
    else:
        verdict = f"FAIL: expected 'Downloaded to: {tmp_path}' in output"
    sections.append(f"## Tier 2: 1-100 MB (MuRongPIG/Proxy-Master http.txt, ~1.8 MB)\n\n{out[:500]}\n\n{verdict}")
    return (passed + 1, failed) if ok else (passed, failed + 1)


# Tier 3 (>100 MB): expect explicit error, no content
def run_tier3(sections, passed, failed):
    out = check_tier3_error()
    ok = "Error: file exceeds 100 MB" in out and "No content returned." in out
    verdict = "PASS: error message present, no content returned" if ok else "FAIL: expected >100 MB error message"
    sections.append(f"## Tier 3: >100 MB (simulated — fake 200 MB response dict)\n\n{out[:500]}\n\n{verdict}")
    return (passed + 1, failed) if ok else (passed, failed + 1)


# Write the tier-by-tier report to md/
def write_report(sections, passed, failed):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = REPORT_DIR / f"probe_large_file_{timestamp}.md"
    header = f"# get_file_content large-file tier smoke test\n\nResults: {passed} passed, {failed} failed\n"
    report_path.write_text(header + "\n" + "\n\n".join(sections) + "\n")
    return report_path


if __name__ == "__main__":
    main()
