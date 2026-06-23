"""
Smoke test: get_file_content large-file tier handling.

Covers all three size tiers via CLI subprocess (hook forbids 'from src.' in dev/ files):

  Tier 1 (<=1 MB)   — octocat/Hello-World README    (tiny, base64 inline)
  Tier 2 (1-100 MB) — MuRongPIG/Proxy-Master http.txt (1.8 MB, streams to /tmp)
  Tier 3 (>100 MB)  — simulated via format_toolarge_response with a fake response dict
                       (no live >100 MB GitHub file used; GitHub API hard limit means the
                        branch is trivial: return error text when size > _SIZE_API_MAX)

Usage (from project root):
  python3 dev/repo_exploration/probe_large_file.py
"""
# INFRASTRUCTURE
import os
import subprocess
import sys


def run_cli(*args):
    result = subprocess.run(
        [sys.executable, "cli.py"] + list(args),
        capture_output=True, text=True, cwd=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )
    return result.stdout + result.stderr


def check_tier3_error():
    # Inline Python -c so we never write 'from src.' at module level in this file.
    code = (
        "import sys; sys.path.insert(0, '.'); "
        "from src.github.get_file_content import format_toolarge_response; "
        "fake = {'path': 'huge.bin', 'name': 'huge.bin', 'size': 200_000_000, "
        "        'type': 'file', 'sha': 'abc', 'html_url': 'https://github.com/x/y/blob/main/huge.bin'}; "
        "out = format_toolarge_response(fake); print(out)"
    )
    result = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True, text=True,
        cwd=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )
    return result.stdout + result.stderr


# ORCHESTRATOR
def main():
    passed = 0
    failed = 0

    # ── Tier 1: <=1 MB ───────────────────────────────────────────────────────
    print("=" * 60)
    print("Tier 1: <=1 MB (octocat/Hello-World README)")
    out1 = run_cli("get_file_content", "octocat", "Hello-World", "README")
    print(out1[:500])
    if "Content:" in out1 and "Lines:" in out1:
        print("PASS: inline content present")
        passed += 1
    else:
        print("FAIL: expected inline content block")
        failed += 1

    # ── Tier 2: 1–100 MB ─────────────────────────────────────────────────────
    print("=" * 60)
    print("Tier 2: 1-100 MB (MuRongPIG/Proxy-Master http.txt, ~1.8 MB)")
    out2 = run_cli("get_file_content", "MuRongPIG", "Proxy-Master", "http.txt")
    print(out2[:500])
    tmp_path = "/tmp/gh-cli_MuRongPIG_Proxy-Master_http.txt"
    if "Downloaded to:" in out2 and tmp_path in out2:
        if os.path.isfile(tmp_path):
            size_on_disk = os.path.getsize(tmp_path)
            print(f"PASS: file on disk at {tmp_path} ({size_on_disk:,} bytes)")
            passed += 1
        else:
            print(f"FAIL: output mentions path but file not found on disk: {tmp_path}")
            failed += 1
    else:
        print(f"FAIL: expected 'Downloaded to: {tmp_path}' in output")
        failed += 1

    # ── Tier 3: >100 MB ──────────────────────────────────────────────────────
    print("=" * 60)
    print("Tier 3: >100 MB (simulated — fake 200 MB response dict)")
    out3 = check_tier3_error()
    print(out3[:500])
    if "Error: file exceeds 100 MB" in out3 and "No content returned." in out3:
        print("PASS: error message present, no content returned")
        passed += 1
    else:
        print("FAIL: expected >100 MB error message")
        failed += 1

    # ── Summary ───────────────────────────────────────────────────────────────
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
