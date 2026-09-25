# INFRASTRUCTURE
import os
import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

REPORT_DIR = Path(__file__).parent / "md"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
TIER2_TMP_PATH = "/tmp/gh-cli_MuRongPIG_Proxy-Master_http.txt"


# ORCHESTRATOR
def main():
    names = select_strands(sys.argv[1:])
    results = run_strands(names)
    report_path = write_report(results)
    print_summary(results, report_path)
    exit_on_failure(results)


# FUNCTIONS
def strand_table():
    return {
        "tier1": run_tier1,
        "tier2": run_tier2,
        "tier3": run_tier3,
    }


def select_strands(requested):
    table = strand_table()
    unknown = [name for name in requested if name not in table]
    if unknown:
        raise SystemExit(f"unknown strand(s): {', '.join(unknown)}; available: {', '.join(table)}")
    return requested or list(table)


def run_strands(names):
    table = strand_table()
    with ThreadPoolExecutor(max_workers=len(names)) as pool:
        futures = [pool.submit(run_strand, table[name]) for name in names]
        return [future.result() for future in futures]


def run_strand(fn):
    try:
        return fn()
    except Exception as e:
        return False, f"## Strand error\n\n{type(e).__name__}: {e}"


def run_cli(*args):
    result = subprocess.run(
        [sys.executable, "cli.py"] + list(args),
        capture_output=True, text=True, cwd=PROJECT_ROOT
    )
    return result.stdout + result.stderr


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


def run_tier1():
    out = run_cli("get_file_content", "octocat", "Hello-World", "README")
    ok = "Content:" in out and "Lines:" in out
    verdict = "PASS: inline content present" if ok else "FAIL: expected inline content block"
    return ok, f"## Tier 1: <=1 MB (octocat/Hello-World README)\n\n{out[:500]}\n\n{verdict}"


def run_tier2():
    if os.path.isfile(TIER2_TMP_PATH):
        os.remove(TIER2_TMP_PATH)
    out = run_cli("get_file_content", "MuRongPIG", "Proxy-Master", "http.txt")
    ok = False
    if "Downloaded to:" in out and TIER2_TMP_PATH in out and os.path.isfile(TIER2_TMP_PATH):
        size_on_disk = os.path.getsize(TIER2_TMP_PATH)
        verdict = f"PASS: file on disk at {TIER2_TMP_PATH} ({size_on_disk:,} bytes)"
        ok = True
    elif "Downloaded to:" in out and TIER2_TMP_PATH in out:
        verdict = f"FAIL: output mentions path but file not found on disk: {TIER2_TMP_PATH}"
    else:
        verdict = f"FAIL: expected 'Downloaded to: {TIER2_TMP_PATH}' in output"
    return ok, f"## Tier 2: 1-100 MB (MuRongPIG/Proxy-Master http.txt, ~1.8 MB)\n\n{out[:500]}\n\n{verdict}"


def run_tier3():
    out = check_tier3_error()
    ok = "Error: file exceeds 100 MB" in out and "No content returned." in out
    verdict = "PASS: error message present, no content returned" if ok else "FAIL: expected >100 MB error message"
    return ok, f"## Tier 3: >100 MB (simulated — fake 200 MB response dict)\n\n{out[:500]}\n\n{verdict}"


def write_report(results):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = REPORT_DIR / f"probe_large_file_{timestamp}.md"
    passed = sum(1 for ok, _ in results if ok)
    failed = len(results) - passed
    header = f"# get_file_content large-file tier smoke test\n\nResults: {passed} passed, {failed} failed\n"
    report_path.write_text(header + "\n" + "\n\n".join(section for _, section in results) + "\n")
    return report_path


def print_summary(results, report_path):
    passed = sum(1 for ok, _ in results if ok)
    print(f"Results: {passed} passed, {len(results) - passed} failed")
    print(report_path)


def exit_on_failure(results):
    if any(not ok for ok, _ in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
