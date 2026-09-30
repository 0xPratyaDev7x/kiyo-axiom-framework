"""P29 offline audit-ledger checks; no host, model, network or product mutation."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import collections
import copy
import hashlib
import io
import json
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "docs/build/requirement-audit.json"
CATEGORIES = {"Missing implementation", "Contradictory contract", "Broken reference",
              "Missing test", "Missing live evidence", "External owner decision"}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def local(path):
    need(not Path(path).is_absolute() and "\\" not in path and ":" not in path
         and ".." not in path.split("/"), "unsafe audit path")
    target = ROOT / path
    need(target.resolve().is_relative_to(ROOT.resolve()) and target.is_file(),
         "missing/escaping implementing or evidence file: " + path)
    # Inspect exact member spelling on Windows as well as case-sensitive systems.
    cursor = ROOT
    for part in Path(path).parts:
        need(part in {p.name for p in cursor.iterdir()}, "case-mismatched audit path")
        cursor /= part
    return target


def validate(data):
    expected = [f"REQ-{n:03}" for n in range(1, 81)]
    rows = data["requirements"]
    need([r["id"] for r in rows] == expected, "80 unique ordered requirements")
    registry = (ROOT / "docs/build/REQUIREMENTS.md").read_text(encoding="utf-8")
    criteria = dict(re.findall(r"- \*\*Observable acceptance criteria \(AC-(\d{3})\):\*\* ([^\n]+)", registry))
    gaps = {g["id"]: g for g in data["gaps"]}
    need(len(gaps) == len(data["gaps"]), "duplicate gap")
    for gap in gaps.values():
        need(gap["category"] in CATEGORIES, "gap category")
        need(all(gap.get(k, "").strip() for k in ("problem", "next_action", "owner", "blocking_scope")),
             "gap lacks action/owner/blocking scope")
    need(data["release_readiness"] == "BLOCKED" and not data["host_verified"]
         and not data["published"], "release gate was silently promoted")
    catalog = json.loads((ROOT / "tests/behavioral/evaluation/catalog.json").read_bytes())
    cases = {c["id"]: c for c in catalog["cases"]}
    static = json.loads((ROOT / "dist/releases/p29-run-02/evidence/static.json").read_bytes())
    checks = {c["id"]: c for c in static["checks"]}
    text_cache = {}
    def content(path):
        if path not in text_cache:
            text_cache[path] = local(path).read_text(encoding="utf-8")
        return text_cache[path]
    for row in rows:
        key = row["id"]
        need(row["acceptance"] == criteria[key[4:]] and row["acceptance_id"] == "AC-" + key[4:],
             "changed acceptance criterion")
        need(row["implementation_status"] in {"IMPLEMENTED", "PARTIALLY_IMPLEMENTED", "NOT_IMPLEMENTED"},
             "invalid implementation status")
        need(row["verification_status"] == "NOT_RUN", "partial evidence promoted to full verification")
        need(row["implementing_files"] and row["implementing_files"] != ["README.md"], "README-only implementation")
        need([x["path"] for x in row["implementing_locations"]] == row["implementing_files"], "location inventory")
        for location in row["implementing_locations"]:
            lines = content(location["path"]).splitlines()
            need(1 <= location["line"] <= len(lines) and lines[location["line"]-1].strip(), "invalid line locator")
        for field in ("skills_and_shared_procedures", "audit_observation", "remaining_gaps",
                      "unsupported_limits", "verification_scope"):
            need(row[field].strip(), "empty required assessment field")
        need(set(row["gap_ids"]) <= gaps.keys(), "unrecorded gap")
        for case in row["behavioral_cases"]:
            need(case in cases and key in cases[case]["requirement_ids"], "case assignment mismatch")
        for spec in row["scenario_specifications"]:
            need(re.search(r"(?<![A-Z0-9-])" + re.escape(spec["id"]) + r"(?![A-Z0-9-])", content(spec["path"])),
                 "missing scenario ID")
            need(spec["status"] == "NOT_RUN", "specification presented as execution")
        for group in row["static_groups"]:
            need(group in checks and checks[group]["status"] == "PASS", "missing actual static result")
        for evidence in row["actual_evidence"]:
            content(evidence["path"])
            need(evidence["scope"].strip() and evidence["layer"].strip(), "unscoped evidence")
        need(row["planned_acceptance_case"] == "TC-" + key, "reserved acceptance ID")
    inv = data["invariants"]
    need([r["id"] for r in inv] == [f"INV-{n:02}" for n in range(1, 23)], "invariant omission")
    for row in inv:
        need(row["requirement_ids"] and set(row["requirement_ids"]) <= set(expected), "invariant mapping")
        need("static" in row["scope"] and "no behavioral/native promotion" in row["scope"], "invariant scope")
    return {"requirements": len(rows), "gaps": len(gaps), "invariants": len(inv),
            "implementation": dict(collections.Counter(r["implementation_status"] for r in rows))}


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(LEDGER.read_bytes())

    def test_01_actual_ledger_files_cases_and_evidence(self):
        self.assertEqual(validate(self.data)["requirements"], 80)

    def test_02_omission_and_duplicate_rejected(self):
        for rows in (self.data["requirements"][:-1], self.data["requirements"] + self.data["requirements"][:1]):
            changed = copy.deepcopy(self.data)
            changed["requirements"] = rows
            with self.assertRaisesRegex(ValueError, "80 unique"):
                validate(changed)

    def test_03_acceptance_reduction_rejected(self):
        self.data["requirements"][0]["acceptance"] = "SYNTHETIC weakened criterion"
        with self.assertRaisesRegex(ValueError, "changed acceptance"):
            validate(self.data)

    def test_04_unowned_gap_rejected(self):
        self.data["gaps"][0]["blocking_scope"] = ""
        with self.assertRaisesRegex(ValueError, "blocking scope"):
            validate(self.data)

    def test_05_fake_full_pass_rejected(self):
        self.data["requirements"][0]["verification_status"] = "PASS"
        with self.assertRaisesRegex(ValueError, "promoted"):
            validate(self.data)

    def test_06_missing_or_escaping_resource_rejected(self):
        for path in ("../SYNTHETIC.md", "docs/SYNTHETIC-absent.md"):
            with self.assertRaisesRegex(ValueError, "unsafe audit path|missing/escaping"):
                local(path)

    def test_07_release_claim_rejected(self):
        self.data["host_verified"] = True
        with self.assertRaisesRegex(ValueError, "release gate"):
            validate(self.data)

    def test_08_recorded_product_inputs_preserved(self):
        prior = json.loads((ROOT / "docs/evidence/packaging/artifact-inventory.json").read_bytes())
        current = json.loads((ROOT / "dist/releases/p29-run-02/artifact-inventory.json").read_bytes())
        self.assertEqual(current["inputs"], prior["inputs"])
        # P29 digests are a historical snapshot; product files may legitimately change
        # after it. Require only that every recorded input still exists and remains an
        # allowlisted product input, so the record keeps pointing at real sources.
        allowlist = set(json.loads((ROOT / "tools/packaging-inputs.json").read_bytes())["sources"])
        for path in current["inputs"]:
            local(path)
            self.assertIn(path, allowlist)
        for target in prior["packages"]:
            self.assertEqual(current["packages"][target]["archive_sha256"], prior["packages"][target]["archive_sha256"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()
    if args.report.exists():
        raise SystemExit("Choose fresh evidence; do not replace failures")
    started = datetime.now(timezone.utc).isoformat()
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(AuditTests))
    code = int(not result.wasSuccessful())
    report = {"command": sys.orig_argv, "exit_code": code, "started_utc": started,
              "finished_utc": datetime.now(timezone.utc).isoformat(), "tests_run": result.testsRun,
              "failures": len(result.failures), "errors": len(result.errors), "output": stream.getvalue(),
              "ledger_sha256": hashlib.sha256(LEDGER.read_bytes()).hexdigest(),
              "test_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "limitations": "Ledger integrity and synthetic negatives only; no semantic, behavioral, native or standards conformance proof"}
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("x", encoding="utf-8") as output:
        json.dump(report, output, indent=2)
        output.write("\n")
    print(stream.getvalue())
    return code


if __name__ == "__main__":
    raise SystemExit(main())
