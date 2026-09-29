"""Developer-only P26 record/closure audit; never launches a native host or model."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import collections
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import package_claude as common

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def data(path):
    return json.loads(read(path))

def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()

def git(*args):
    p = subprocess.run(["git", "-c", "safe.directory=" + ROOT.as_posix(),
                        "-c", "core.excludesFile=", *args], cwd=ROOT,
                       capture_output=True, text=True, encoding="utf-8")
    assert p.returncode == 0, (args, p.stdout, p.stderr)
    return p.stdout.strip()

def audit(checks):
    slugs = ("claude-cli", "claude-vscode", "codex-cli", "codex-ide", "copilot-cli", "copilot-vscode")
    cases = data("tests/live/cases.json")["cases"]
    assert [c["id"] for c in cases] == [f"LT-{n:02}" for n in range(1, 13)]
    p25 = data("tests/behavioral/evaluation/catalog.json")["cases"]
    p25ids = {c["id"] for c in p25}
    for case in cases:
        assert case["operator_input"] and case["expected"]["allowed"] and case["expected"]["forbidden"]
        assert set(case["fixture_cases"]) <= p25ids
    records = [data(f"docs/evidence/live/{s}.json") for s in slugs]
    flat = [c for r in records for c in r["checks"]]
    assert len(flat) == len({c["id"] for c in flat}) == 72
    assert collections.Counter(c["execution_status"] for c in flat) == {"PASS": 2, "NOT_RUN": 70}
    assert collections.Counter(c["evidence_status"] for c in flat) == {"VERIFIED": 2, "UNSUPPORTED": 12, "NOT_TESTED": 58}
    for record in records:
        assert record["screenshots"] == [] and record["model"] == "NOT_INVOKED"
        assert record["full_behavioral_suite"] == "NOT_TESTED"
        assert [c["protocol_case"] for c in record["checks"]] == [c["id"] for c in cases]
        for check in record["checks"]:
            for field in ("applicability", "method", "inspected_scope", "limitations", "baseline_relation"):
                assert check[field], (check["id"], field)
            assert check["evidence"] and all((ROOT / "docs/evidence/live" / p).is_file() for p in check["evidence"])
    checks.append({"id": "P26-A01", "status": "PASS", "observed": "72 independent records; 2 PASS, 70 NOT_RUN; expected cases separate"})

    first = data("docs/evidence/live/claude-native-attempt-01.json")
    claude = data("docs/evidence/live/claude-native-attempt-02.json")
    zip_run = data("docs/evidence/live/claude-zip-attempt-01.json")
    assert len(first["commands"]) == 2 and len(claude["commands"]) == 5
    assert [c["exit_code"] for c in claude["commands"]] == [0, 0, 1, 0, 0]
    assert "version: No version" in claude["commands"][1]["stdout"]
    assert "author: No author" in claude["commands"][1]["stdout"]
    expected_skills = {"architecture", "implement", "init", "memory", "requirement", "review", "security", "test"}
    for output in (claude["commands"][-1]["stdout"], zip_run["commands"][0]["stdout"]):
        found = re.search(r"Skills \(8\)\s+([^\n]+)", output)
        assert found and set(found[1].split(", ")) == expected_skills
        assert all(s in output for s in ("Agents (0)", "Hooks (0)", "MCP servers (0)", "LSP servers (0)"))
    assert claude["project_before"] == claude["project_after"]
    assert claude["payload_before"] == claude["payload_after"]
    assert zip_run["project_after"] == claude["project_after"]
    assert all(c["exit_code"] == 0 for c in zip_run["commands"])
    checks.append({"id": "P26-A02", "status": "PASS", "observed": "Claude actual normal acceptance, strict FAIL, eight metadata entries and preservation agree with reports"})

    install = data("docs/evidence/live/codex-native-attempt-01.json")
    life = data("docs/evidence/live/codex-lifecycle-attempt-01.json")
    assert all(c["exit_code"] == 0 for c in install["commands"] + life["commands"])
    added = json.loads(install["commands"][-1]["stdout"])
    assert added["pluginId"] == "kiyo-compass@kiyo-p26-disposable"
    assert added["version"] == life["native_reported_version"] == "1.0.0"
    assert "version" not in life["cached_manifest"] and life["product_version"] == "UNSET"
    assert life["cache_matches_distribution"] and not life["cache_exists_after_remove"]
    assert install["project_before"] == install["project_after"] == life["project_before"] == life["project_after"]
    assert len(life["cache_file_hashes"]) == 795 and len(life["cache_skill_files"]) == 8
    cache_check = json.loads(life["commands"][1]["stdout"])
    assert (cache_check["result"], cache_check["skills"], cache_check["local_links"]) == ("PASS", 8, 4956)
    assert cache_check["outside_read_probe"] == "DENIED"
    assert json.loads(life["commands"][3]["stdout"])["installed"] == []
    assert life["catalog_source_still_exists"] and life["native_model_sessions"] == 0
    checks.append({"id": "P26-A03", "status": "PASS", "observed": "Codex native install/cache/removal evidence consistent; fallback version separated; three project files preserved"})

    inventory = data("docs/evidence/packaging/artifact-inventory.json")
    assert len(inventory["inputs"]) == 112
    for path, digest in inventory["inputs"].items():
        assert sha(path) == digest, path
    for path, digest in inventory["tooling_sha256"].items():
        assert sha(path) == digest, path
    for package in inventory["packages"].values():
        assert sha("dist/archives/" + package["archive"]) == package["archive_sha256"]
    assert len(list((ROOT / "src/kiyo/skills").glob("*/SKILL.md"))) == 8
    previous = data("docs/evidence/behavioral/observations.json")
    assert previous["host_runs"] == 0 and len(previous["records"]) == 48
    assert all(c["result"] == "NOT_RUN" for c in previous["records"])
    checks.append({"id": "P26-A04", "status": "PASS", "observed": "112 product/overlay/license inputs, packaging tooling and 3 ZIP hashes unchanged; P25 remains 48 NOT_RUN"})

    files = [p for directory in ("docs", "src", "tests", "platforms", "dist")
             for p in (ROOT / directory).rglob("*.md")]
    texts = {}
    for p in files:
        text = p.read_text(encoding="utf-8")
        assert "\ufffd" not in text and "\x00" not in text, p
        assert not re.search(r"^(<<<<<<<|=======|>>>>>>>)", text, re.M), p
        common.reject_links(p)
        texts[p.resolve()] = text
    anchors = {p: {common.slug(m[1]) for m in re.finditer(r"^#{1,6}\s+(.+?)\s*$", t, re.M)}
               for p, t in texts.items()}
    count = 0
    for path, text in texts.items():
        base = path
        rel = path.relative_to(ROOT).as_posix()
        for target in ("claude", "codex", "copilot"):
            if rel == f"platforms/{target}/resources/activation.md":
                folder = "dist/claude" if target == "claude" else f"dist/{target}/kiyo-compass"
                base = (ROOT / folder / "skills/init/references" / target / "activation.md").resolve()
        body = re.sub(chr(96) * 3 + r"[\s\S]*?" + chr(96) * 3, "", text)
        for match in common.LINK.finditer(body):
            dest = match[1].strip().strip("<>")
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", dest):
                continue
            filename, _, anchor = dest.partition("#")
            target = (base.parent / filename).resolve() if filename else base
            assert target.is_relative_to(ROOT) and target.exists(), (rel, dest)
            assert not anchor or anchor in anchors.get(target, set()), (rel, dest, "anchor")
            count += 1
    checks.append({"id": "P26-A05", "status": "PASS", "observed": {"markdown_files": len(files), "local_links": count},
                   "limitations": "Inline link convention; external URLs not re-fetched; platform adapters rebased to installed form"})

    trace = read("docs/build/TRACEABILITY.md")
    rows = [[v.strip() for v in l.split("|")[1:-1]]
            for l in trace.splitlines() if re.match(r"^\| REQ-\d{3} \|", l)]
    ids = [f"REQ-{n:03}" for n in range(1, 81)]
    assert [r[0] for r in rows] == ids and all(len(r) == 10 and r[8] == "NOT_RUN" for r in rows)
    assert collections.Counter(r[7] for r in rows) == {"PARTIALLY_IMPLEMENTED": 79, "NOT_IMPLEMENTED": 1}
    assert re.findall(r"^## (REQ-\d{3})$", read("docs/build/REQUIREMENTS.md"), re.M) == ids
    assert trace.count("[P26 actual evidence]") == 30
    for name, prefix, total in (("OPEN-ISSUES", "ISS", 9), ("DECISIONS", "DEC", 4)):
        assert re.findall(r"^\| (" + prefix + r"-\d{3}) \|", read(f"docs/build/{name}.md"), re.M) == [f"{prefix}-{n:03}" for n in range(1, total + 1)]
    progress = read("docs/build/PROGRESS.md")
    assert "| 26 | Live Host Tests | DONE |" in progress
    assert "| 27 | Documentation | NOT_STARTED |" in progress
    assert "**Next: Prompt 27 Documentation**" in read("docs/build/HANDOFF.md")
    checks.append({"id": "P26-A06", "status": "PASS", "observed": "80 unique requirements/full NOT_RUN; 30 scoped trace additions; 9 issues/4 owner decisions retained; next27"})

    assert git("branch", "--show-current") == "main"
    assert git("rev-parse", "HEAD") == "cb4647c56c2ea0c711d9c35b861c0ad0fc76280a"
    assert not git("diff", "--cached", "--name-only")
    assert git("hash-object", "LICENSE") == "d2e60c5b160ed4f9ca096215e72efee5769936b1"
    modified = set(git("diff", "--name-only").splitlines())
    assert len(modified) == 12 and all(p.startswith(("docs/build/", "docs/compatibility/", "docs/research/")) for p in modified)
    new = set(git("ls-files", "--others", "--exclude-standard").splitlines())
    assert new and all(p.startswith(("docs/evidence/live/", "tests/live/", "docs/compatibility/live-")) for p in new)
    assert not (ROOT / "debug.log").exists()
    for name in (".kiyo", "AGENTS.md", "AGENTS.override.md", "CLAUDE.md", ".vscode", ".github"):
        assert not (ROOT / name).exists(), name
    git("diff", "--check")
    checks.append({"id": "P26-A07", "status": "PASS", "observed": {"modified_files": len(modified), "new_files": len(new), "diff_check": "PASS"},
                   "limitations": "Read-only closure audit; does not verify absent global/transient effects or agent behavior"})

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    assert not args.report.exists(), "Use a fresh evidence filename"
    report = {"layer": "offline_evidence_record_audit", "started_at": datetime.now(timezone.utc).isoformat(),
              "command": sys.orig_argv, "checks": [], "host_or_model_executions": 0,
              "inputs_sha256": {p.relative_to(ROOT).as_posix(): sha(p.relative_to(ROOT))
                                for p in sorted((ROOT / "docs/evidence/live").glob("*.json"))
                                if not p.name.startswith("record-audit-")},
              "audit_source_sha256": sha("tests/live/check_records.py"),
              "case_catalog_sha256": sha("tests/live/cases.json")}
    try:
        audit(report["checks"])
        report.update(result="PASS", exit_code=0)
    except Exception as error:
        report.update(result="FAIL", exit_code=1, failure=f"{type(error).__name__}: {error}")
    report["finished_at"] = datetime.now(timezone.utc).isoformat()
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(json.dumps(report, ensure_ascii=True, indent=2))
    return report["exit_code"]

if __name__ == "__main__":
    raise SystemExit(main())
