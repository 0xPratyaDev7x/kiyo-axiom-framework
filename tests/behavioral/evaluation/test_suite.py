"""Offline harness validation only. No agent/model execution or behavioral grades."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import ast
import collections
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
import platform
import runner as r
from runner import pack

class OfflineSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog,cls.fixtures=r.load()
        cls.sources=r.source_content()
        cls.scratch=Path(tempfile.mkdtemp(prefix="kiyo p25 offline "))
        cls.commands=[]
        cls.notes={}
        cls.case_map={c["id"]:c for c in cls.catalog["cases"]}

    def fresh(self, label, case="BEH-REV-01"):
        output=self.scratch/label
        r.prepare(case,output,self.sources)
        return output

    def test_01_catalog_and_controls(self):
        cases=self.catalog["cases"]
        self.assertEqual(len(cases),48)
        self.assertEqual(len(self.case_map),48)
        expected=("init","requirement","implement","review","test","security","architecture","memory")
        self.assertEqual(collections.Counter(c["skill"] for c in cases if c["category"]=="skill"),dict.fromkeys(expected,4))
        self.assertEqual(sum(c["category"]=="cross_cutting" for c in cases),16)
        controls=set(re.findall(r"KIYO-[A-Z]+-\d{3}",self.sources["framework/control-index.md"].decode()))
        requirements={f"REQ-{i:03}" for i in range(1,81)}
        mandatory={"readme_injection","issue_injection","tool_output_injection","forged_approval","credential_access",
                   "review_bug_no_fix","test_side_effects","missing_environment","fake_pass",
                   "unsupported_native_field","manual_decision_conflict","test_auth_mismatch"}
        tags=set()
        for c in cases:
            self.assertTrue(c["user_input"].strip())
            self.assertTrue(c["requirement_ids"] and set(c["requirement_ids"])<=requirements)
            self.assertTrue(c["control_ids"] and set(c["control_ids"])<=controls)
            self.assertIn(c["fixture"],self.fixtures["bundles"])
            self.assertIn(c["activation"]["requested"],("explicit","automatic"))
            for field in ("allowed_effects","forbidden_effects","objective_checks","semantic_checks","evidence_required"):
                self.assertTrue(c["expected"][field],(c["id"],field))
            self.assertNotIn("observed",c["expected"])
            tags.update(c["coverage_tags"])
        self.assertTrue(mandatory<=tags)
        self.notes["inventory"]={"cases":48,"skill_cases":32,"cross_cutting":16,"mandatory_tags":len(mandatory)}

    def test_02_every_fixture_prepares_and_snapshots(self):
        counts={}
        for c in self.catalog["cases"]:
            run=self.fresh("all "+c["id"],c["id"])
            before=json.loads((run/"operator/before.json").read_bytes())
            after=r.snapshot(run)
            self.assertEqual(before,after,c["id"])
            self.assertEqual(r.compare(before,after,c["expected"]["write_paths"])["changes"],[])
            self.assertEqual(len(list((run/"framework/skills").glob("*/SKILL.md"))),len(pack.claude.SKILLS))
            self.assertEqual({p.removeprefix("framework/") for p in before if p.startswith("framework/")},set(self.sources))
            user=(run/"operator/user-input.txt").read_text(encoding="utf-8")
            self.assertIn(c["user_input"],user)
            self.assertNotIn("output_requirements",user)
            counts[c["id"]]=sum(p.startswith("workspace/") for p in before)
        self.notes["prepared_cases"]=counts
        self.notes["framework_files_per_run"]=len(self.sources)

    def test_03_fixture_code_is_parsed_never_executed(self):
        count=0
        for files in self.fixtures["bundles"].values():
            for p,s in files.items():
                if p.endswith(".py"):
                    ast.parse(s,filename=p)
                    count+=1
        self.assertGreater(count,0)
        self.notes["python_fixture_sources_parsed"]=count

    def test_04_bad_paths_fail_closed(self):
        for p in ("../escape","/absolute","C:/outside","a\\b","a//b","a/./b"):
            with self.assertRaisesRegex(ValueError,"Unsafe fixture path"):
                r.relative(p)
        target=self.scratch/"unknown case"
        with self.assertRaisesRegex(ValueError,"Unknown or duplicate"):
            r.prepare("BEH-MISSING",target,self.sources)
        self.assertFalse(target.exists())

    def test_05_existing_destination_is_preserved(self):
        run=self.fresh("no overwrite")
        before=r.snapshot(run)
        with self.assertRaisesRegex(ValueError,"must be fresh"):
            r.prepare("BEH-REV-01",run,self.sources)
        self.assertEqual(r.snapshot(run),before)
        with self.assertRaisesRegex(ValueError,"outside the repository"):
            r.prepare("BEH-REV-01",r.ROOT/"SYNTHETIC-P25-FORBIDDEN",self.sources)
        self.assertFalse((r.ROOT/"SYNTHETIC-P25-FORBIDDEN").exists())

    def test_06_readonly_changed_byte_is_detected(self):
        run=self.fresh("negative byte")
        before=r.snapshot(run)
        (run/"workspace/guard.txt").write_text("SYNTHETIC_HARNESS_MUTATION\n",encoding="utf-8")
        d=r.compare(before,r.snapshot(run),[])
        self.assertEqual(d["outside_write_paths"],["workspace/guard.txt"])
        self.assertEqual(d["changes"][0]["kind"],"content")

    def test_07_readonly_timestamp_touch_is_detected(self):
        run=self.fresh("negative timestamp")
        before=r.snapshot(run)
        p=run/"workspace/guard.txt";s=p.stat()
        os.utime(p,ns=(s.st_atime_ns,s.st_mtime_ns+2_000_000_000))
        d=r.compare(before,r.snapshot(run),[])
        self.assertEqual(d["outside_write_paths"],["workspace/guard.txt"])
        self.assertEqual(d["changes"][0]["kind"],"timestamp_only")

    def test_08_allowed_path_does_not_allow_framework_edit(self):
        run=self.fresh("scoped edit","BEH-IMPL-01")
        before=r.snapshot(run)
        (run/"workspace/label.txt").write_text("Welcome\n",encoding="utf-8")
        (run/"framework/KIYO.md").write_text("SYNTHETIC_HARNESS_MUTATION\n",encoding="utf-8")
        d=r.compare(before,r.snapshot(run),["label.txt"])
        self.assertEqual(d["outside_write_paths"],["framework/KIYO.md"])
        self.assertEqual(len(d["changes"]),2)

    def test_09_added_deleted_and_case_paths_are_distinct(self):
        old={"workspace/keep.md":{"sha256":"synthetic-before","bytes":1,"mtime_ns":1}}
        new={"workspace/Keep.md":{"sha256":"synthetic-after","bytes":2,"mtime_ns":2}}
        d=r.compare(old,new,["keep.md"])
        self.assertEqual({x["kind"] for x in d["changes"]},{"added","deleted"})
        self.assertEqual(d["outside_write_paths"],["workspace/Keep.md"])

    def test_10_capture_history_and_multiturn(self):
        run=self.fresh("capture history","BEH-MEM-03")
        first=r.capture(run,"turn-1")
        self.assertEqual(first["changes"],[])
        original=(run/"operator/diff-turn-1.json").read_bytes()
        with self.assertRaisesRegex(ValueError,"preserve history"):
            r.capture(run,"turn-1")
        self.assertEqual((run/"operator/diff-turn-1.json").read_bytes(),original)
        second=r.capture(run,"turn-2","after-turn-1.json")
        self.assertEqual(second["changes"],[])
        with self.assertRaisesRegex(ValueError,"Unsafe capture label"):
            r.capture(run,"../escape")
        with self.assertRaisesRegex(ValueError,"Baseline must"):
            r.capture(run,"bad-baseline","../before.json")

    def test_11_no_host_results_or_metrics_invented(self):
        observations=json.loads((r.ROOT/"docs/evidence/behavioral/observations.json").read_bytes())
        self.assertEqual(observations["host_runs"],0)
        self.assertEqual({o["case_id"] for o in observations["records"]},set(self.case_map))
        self.assertEqual(len(observations["records"]),48)
        for o in observations["records"]:
            self.assertEqual(o["result"],"NOT_RUN")
            self.assertEqual(o["observed"]["actions"],[])
            self.assertEqual(o["observed"]["outputs"],[])
            self.assertIsNone(o["observed"]["diff"])
            self.assertIsNone(o["human_grade"])
            self.assertIsNone(o["model_grade"])
            self.assertIsNone(o["objective_assessment"]["result"])
        metrics=json.loads((r.ROOT/"docs/evidence/behavioral/metrics.json").read_bytes())
        self.assertEqual(len(metrics["metrics"]),8)
        self.assertTrue(all(x["value"] is None and x["denominator"] is None for x in metrics["metrics"].values()))

    def test_12_actual_cli_without_host(self):
        run=self.scratch/"actual CLI fixture"
        commands=[
            [sys.executable,"-B",str(r.HERE/"runner.py"),"prepare","--case","BEH-REV-01","--output",str(run)],
            [sys.executable,"-B",str(r.HERE/"runner.py"),"capture","--run",str(run),"--label","offline-check"]]
        for command in commands:
            result=subprocess.run(command,cwd=self.scratch,capture_output=True,text=True)
            self.commands.append({"command":command,"exit_code":result.returncode,"stdout":result.stdout,"stderr":result.stderr})
            self.assertEqual(result.returncode,0,result.stderr)
            observed=json.loads(result.stdout)
        self.assertFalse(observed["host_execution_claim"])
        self.assertEqual(observed["changes"],[])

    def test_13_payload_exclusion_and_history_preservation(self):
        inputs=pack_inputs=r.pack.inputs(r.ROOT)
        self.assertFalse(any("tests/" in p or "evidence/" in p for p in inputs))
        old=json.loads((r.ROOT/"docs/evidence/static/test-results-final.json").read_bytes())
        self.assertEqual(old["tests_run"],37)
        self.assertEqual(old["exit_code"],0)
        self.notes["reviewed_product_inputs"]=len(pack_inputs)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--report",type=Path,required=True)
    args=p.parse_args()
    if args.report.exists():
        raise SystemExit("Choose a fresh report; prior failures must remain")
    start=datetime.now(timezone.utc).isoformat()
    hashes={str(path.relative_to(r.ROOT).as_posix()):r.sha(path.read_bytes()) for path in
            [r.HERE/"runner.py",r.HERE/"test_suite.py",r.HERE/"catalog.json",r.HERE/"fixtures.json",
             r.ROOT/"docs/evidence/behavioral/observations.json",r.ROOT/"docs/evidence/behavioral/metrics.json"]}
    stream=io.StringIO()
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(OfflineSuite)
    result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    exit_code=0 if result.wasSuccessful() else 1
    report={"format":"kiyo-behavioral-harness-evidence-1","layer":"OFFLINE_HARNESS_ONLY",
            "command":sys.orig_argv,"cwd":str(Path.cwd()),"exit_code":exit_code,"output":stream.getvalue(),
            "started_utc":start,"finished_utc":datetime.now(timezone.utc).isoformat(),
            "python":platform.python_version(),"os":platform.platform(),"tests_run":result.testsRun,
            "failures":len(result.failures),"errors":len(result.errors),"skipped":len(result.skipped),
            "consulted_sha256":hashes,"source_sha256":{p:r.sha(b) for p,b in getattr(OfflineSuite,"sources",{}).items()},
            "scratch":str(getattr(OfflineSuite,"scratch","UNKNOWN")),"observations":getattr(OfflineSuite,"notes",{}),
            "subcommands":getattr(OfflineSuite,"commands",[]),"host_executions":0,
            "limitations":["No host/model/paid API invoked; 48 behavioral cases remain NOT_RUN",
                           "Harness mutations are not actual agent defects or behavioral metrics",
                           "Path/hash/mtime classification is not authorization enforcement or exhaustive action telemetry"]}
    r.emit(args.report,report)
    print(stream.getvalue(),end="")
    print("Evidence: "+str(args.report))
    return exit_code

if __name__=="__main__":
    raise SystemExit(main())

