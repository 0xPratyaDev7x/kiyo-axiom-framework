"""Offline release-tool regression checks; synthetic files, no native host or network."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import io
import json
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tests/static"))
import release_candidate as release
import test_contracts as static

class ReleaseTests(unittest.TestCase):
    def test_01_unset_is_consistent_but_not_release_version(self):
        result = release.versions({"a": {"name": "kiyo-axiom-framework"}, "b": {"name": "kiyo-axiom-framework"}})
        self.assertEqual(result["product_version"], "UNSET")
        self.assertEqual(result["publication_version_gate"], "OWNER_REQUIRED")

    def test_02_mixed_versions_rejected(self):
        for other in ("9.8.7", None):
            with self.assertRaisesRegex(ValueError, "inconsistent native versions"):
                release.versions({"a": {"name": "kiyo-axiom-framework", "version": "9.8.6"},
                                  "b": {"name": "kiyo-axiom-framework", "version": other}})
        with self.assertRaisesRegex(ValueError, "Invalid version"):
            release.versions({"a": {"name": "kiyo-axiom-framework", "version": 1}})

    def test_03_identity_mismatch_rejected(self):
        with self.assertRaisesRegex(ValueError, "identity mismatch"):
            release.versions({"a": {"name": "synthetic-other"}})

    def test_04_output_scope_and_overwrite_refused(self):
        scratch = Path(tempfile.mkdtemp(prefix="kiyo p28 output test "))
        with patch.object(release, "ROOT", scratch):
            with self.assertRaisesRegex(ValueError, "direct child"):
                release.output_path(scratch / "source")
            with self.assertRaisesRegex(ValueError, "direct child"):
                release.output_path(scratch / "dist/releases/../outside")
            target = scratch / "dist/releases/existing"
            target.mkdir(parents=True)
            marker = target / "human.txt"
            marker.write_text("SYNTHETIC HUMAN", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "already exists"):
                release.output_path(target)
            self.assertEqual(marker.read_text(), "SYNTHETIC HUMAN")

    def test_05_failed_or_blocked_evidence_never_plain_validated(self):
        self.assertEqual(release.package_status([], []), "PACKAGE_NOT_VALIDATED")
        self.assertEqual(release.package_status([{"status": "FAIL"}], []), "PACKAGE_NOT_VALIDATED")
        complete = [{"name": name, "status": "PASS"} for name in release.STAGES]
        self.assertEqual(release.package_status(complete, [{"id": "PKG-08"}]),
                         "PACKAGE_VALIDATED_WITH_LIMITATIONS")
        self.assertEqual(release.package_status(complete, []), "PACKAGE_VALIDATED")
        for index in range(len(complete)):
            for status in ("FAIL", "BLOCKED", "NOT_RUN", "NOT_APPLICABLE"):
                changed = [dict(row) for row in complete]
                changed[index]["status"] = status
                self.assertEqual(release.package_status(changed, []), "PACKAGE_NOT_VALIDATED")

    def test_06_pipeline_failure_retains_report_and_no_success(self):
        scratch = Path(tempfile.mkdtemp(prefix="kiyo p28 failure test "))
        out = scratch / "dist/releases/failure"
        with patch.object(release, "ROOT", scratch), patch.object(release.pack, "inputs",
                side_effect=ValueError("SYNTHETIC INVALID INPUT")), patch("sys.stdout", new=io.StringIO()):
            self.assertEqual(release.run(out), 1)
        result = json.loads((out / "pipeline.json").read_bytes())
        self.assertEqual(result["package_status"], "PACKAGE_NOT_VALIDATED")
        self.assertEqual(result["signature"], "NOT_SIGNED")
        self.assertEqual(result["publication_status"], "NOT_PUBLISHED")
        self.assertIn("SYNTHETIC INVALID INPUT", result["failure"])
        self.assertFalse((out / "archives").exists())

    def test_07_static_suite_reads_selected_candidate_and_refuses_escape(self):
        scratch = Path(tempfile.mkdtemp(prefix="kiyo p28 candidate test "))
        inv = scratch / "selected.json"
        (scratch / "candidate.zip").write_bytes(release.pack.archive_bytes({"selected.md": b"SYNTHETIC"}))
        inv.write_text(json.dumps({"packages": {"claude": {"archive": "candidate.zip"}}}), encoding="utf-8")
        with patch.object(static.pack, "inputs", return_value={}):
            _, packages, _, _ = static.load_context(inv, scratch)
            self.assertEqual(packages["claude"], {"selected.md": b"SYNTHETIC"})
            inv.write_text(json.dumps({"packages": {"claude": {"archive": "../outside.zip"}}}), encoding="utf-8")
            with self.assertRaisesRegex(static.c.Violation, "ARCHIVE_PATH"):
                static.load_context(inv, scratch)

    def test_08_unsigned_inventory_has_no_fabricated_dependencies(self):
        deps, attribution = release.review_inventories(release.pack.inputs(ROOT))
        self.assertEqual(deps["payload_runtime_dependencies"], [])
        self.assertEqual(deps["developer"]["python_packages_required"], [])
        self.assertFalse(deps["formal_sbom"])
        self.assertFalse(attribution["formal_sbom"])
        self.assertEqual(attribution["project_license"]["publication_confirmation"], "OWNER_REQUIRED")
        self.assertEqual(attribution["project_license"]["sha256"], release.sha((ROOT / "LICENSE").read_bytes()))
        self.assertTrue(attribution["third_party_reference_citations"])

    def test_09_incomplete_or_reordered_pipeline_cannot_validate(self):
        names = ("Validate", "Package", "Inspect payload", "Run tests",
                 "Artifact inventory", "Release-readiness report")
        complete = [{"name": name, "status": "PASS"} for name in names]
        for index in range(len(complete)):
            with self.subTest(missing=names[index]):
                self.assertEqual(release.package_status(complete[:index] + complete[index+1:], []),
                                 "PACKAGE_NOT_VALIDATED")
        for invalid in (complete[::-1], complete + [complete[0]],
                        [{"status": "PASS"}],
                        [{"name": "SYNTHETIC UNKNOWN", "status": "PASS"}]):
            with self.subTest(stages=invalid):
                self.assertEqual(release.package_status(invalid, []), "PACKAGE_NOT_VALIDATED")

    def test_10_readiness_write_failure_cannot_leave_success_record(self):
        scratch = Path(tempfile.mkdtemp(prefix="kiyo p29 report failure "))
        out = scratch / "dist/releases/failure"
        original_write = release.write
        def deny_readiness(path, value):
            if path.name == "readiness.md":
                raise OSError("SYNTHETIC readiness output unavailable")
            original_write(path, value)
        def completed_prerequisite(pipeline, name, action):
            # Unit fixture only: isolate final report I/O, never claim a real build.
            pipeline.stages.append({"name": name, "status": "PASS"})
        with patch.object(release, "ROOT", scratch), patch.object(release.pack, "inputs", return_value={}), \
                patch.object(release, "snapshot", return_value={}), \
                patch.object(release.Pipeline, "stage", completed_prerequisite), \
                patch.object(release, "write", deny_readiness), patch("sys.stdout", new=io.StringIO()):
            self.assertEqual(release.run(out), 1)
        result = json.loads((out / "pipeline.json").read_bytes())
        self.assertEqual(result["exit_code"], 1)
        self.assertEqual(result["package_status"], "PACKAGE_NOT_VALIDATED")
        self.assertEqual(result["stages"][-1]["status"], "FAIL")
        self.assertIn("SYNTHETIC readiness output unavailable", result["failure"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    if args.report.exists():
        raise SystemExit("Choose a fresh report; retain failures")
    started = datetime.now(timezone.utc).isoformat()
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(ReleaseTests))
    code = 0 if result.wasSuccessful() else 1
    report = {"format": "kiyo-release-tests-1", "command": sys.orig_argv, "exit_code": code,
              "started_utc": started, "finished_utc": datetime.now(timezone.utc).isoformat(),
              "tests_run": result.testsRun, "failures": len(result.failures),
              "errors": len(result.errors), "skipped": len(result.skipped), "output": stream.getvalue(),
              "source_sha256": {p: release.sha((ROOT / p).read_bytes())
                                for p in ("tools/release_candidate.py", "tests/release/test_release.py",
                                          "tests/static/test_contracts.py")},
              "limitations": "Developer helper and synthetic failure tests only; no host/signing/publication"}
    release.write(args.report, report)
    print(stream.getvalue())
    return code


if __name__ == "__main__":
    raise SystemExit(main())
