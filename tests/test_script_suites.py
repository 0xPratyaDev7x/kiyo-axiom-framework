"""Pytest entry for the argparse-based static and packaging suites.

tests/static/test_contracts.py and tests/packaging/test_distributions.py are report-writing
scripts, so pytest does not collect them on its own. These wrappers run each against a fresh
temporary build and report path, keeping `python -m pytest tests` a complete gate.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    return subprocess.run([sys.executable, "-B", *map(str, args)], cwd=ROOT,
                          capture_output=True, text=True, encoding="utf-8", errors="replace")


def detail(result):
    return (result.stdout[-2000:] + "\n" + result.stderr[-2000:]).strip()


def test_static_contracts(tmp_path):
    archives, inventory, report = tmp_path / "archives", tmp_path / "inventory.json", tmp_path / "static.json"
    build = run("tools/package_distributions.py", "--output", archives, "--inventory", inventory)
    assert build.returncode == 0, detail(build)
    result = run("tests/static/test_contracts.py", "--inventory", inventory,
                 "--archives", archives, "--report", report)
    assert result.returncode == 0, detail(result)
    data = json.loads(report.read_text(encoding="utf-8"))
    assert data["failures"] == 0 and data["errors"] == 0 and data["tests_run"] > 0


def test_packaging_distributions(tmp_path):
    report = tmp_path / "packaging.json"
    result = run("tests/packaging/test_distributions.py", "--report", report)
    assert result.returncode == 0, detail(result)
    checks = json.loads(report.read_text(encoding="utf-8"))["checks"]
    # BLOCKED marks an environment limit (e.g. Windows symlink privilege), never a pass.
    assert checks and all(c["status"] in {"PASS", "BLOCKED"} for c in checks), checks
    assert any(c["status"] == "PASS" for c in checks)
