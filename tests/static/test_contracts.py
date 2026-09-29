"""Run selected static contracts against canonical content and actual development ZIPs."""
from pathlib import Path
import argparse
from datetime import datetime, timezone
import io
import json
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tests/packaging"))
import package_distributions as pack
import verify_payload
from test_distributions import safe_extract
from package_claude import sha
import contracts as c

SUPPORT = ("docs/build/REQUIREMENTS.md", "docs/build/TRACEABILITY.md",
           "tests/behavioral/verification/scenarios.md",
           "tests/behavioral/agent-security/scenarios.md")
GROUPS = (
 "Eight public Skills", "Frontmatter", "Mandatory resources", "Contained exact-case references",
 "Selected native manifest properties", "Identity/control/content parity", "Read-only and approval boundaries",
 "Enums and example roles", "AST coverage/ownership", "Memory record types",
 "Neutral template regression scan", "Input/payload allowlists", "Actual relocation/extraction",
 "Context budgets", "Required content substance", "Requirement ID coverage",
)
REQUIRED_NEGATIVES = {"broken-resource", "duplicate-skill", "unsupported-manifest-field",
                      "missing-approval-boundary", "contradictory-fake-pass", "private-package-file"}


def load_context(inventory_path=None, archive_dir=None):
    data = pack.inputs(ROOT)
    data.update({p: (ROOT/p).read_bytes() for p in SUPPORT})
    inventory_path = inventory_path or ROOT/"docs/evidence/packaging/artifact-inventory.json"
    archive_dir = archive_dir or ROOT/"dist/archives"
    inventory = json.loads(inventory_path.read_bytes())
    packages, archives = {}, {}
    for target, record in inventory["packages"].items():
        filename = record["archive"]
        c.need(Path(filename).name == filename and "/" not in filename and "\\" not in filename
               and ":" not in filename, "ARCHIVE_PATH", str(filename))
        archives[target] = (archive_dir/filename).read_bytes()
        with zipfile.ZipFile(io.BytesIO(archives[target])) as z:
            names = z.namelist()
            c.need(len(names) == len(set(n.casefold() for n in names)), "ZIP_DUPLICATE", target)
            c.need(all(n.startswith("kiyo-compass/") for n in names), "ZIP_ROOT", target)
            packages[target] = {n.removeprefix("kiyo-compass/"): z.read(n) for n in names}
    return data, packages, archives, inventory


def run_group(group, data, packages, context):
    files = c.product(data)
    if group in ("G01", "G02"):
        fn = c.skill_inventory if group == "G01" else c.metadata
        for mapping in (files, *packages.values()):
            fn(mapping)
        return {"canonical_entries": len(c.entries(files)),
                "package_entries": {t: len(c.entries(p)) for t,p in packages.items()}}
    if group == "G03":
        c.mandatory(files)
        return {"required_resources": len(c.MANDATORY), "skill_routes": len(c.PROCEDURES)}
    if group == "G04":
        return {"canonical_links": c.links(files),
                "package_links": {t: c.links(p, packaged=True) for t,p in packages.items()}}
    if group == "G05":
        c.manifests(data, packages, pack.BUILDERS)
        for t,payload in packages.items():
            native = ".claude-plugin/plugin.json" if t == "claude" else "plugin.json"
            c.need(payload[native] == data[f"platforms/{t}/{native}"], "MANIFEST_PARITY", t)
        return {"schemas": "selected properties only", "manifests": 4}
    if group == "G06":
        controls = c.identity(files, packages)
        for target,builder in pack.BUILDERS.items():
            for skill in c.SKILLS:
                path = f"skills/{skill}/SKILL.md"
                source = c.text(files,path)
                def transform(match):
                    dest = match[1]
                    return match[0].replace(dest, "./references/kiyo/"+dest[6:]) if dest.startswith("../../") else match[0]
                expected = c.LINK.sub(transform,source).rstrip()+"\n"+builder.SUFFIX
                c.need(c.text(packages[target],path) == expected, "ENTRY_PARITY", target+"/"+skill)
        c.need(not (ROOT/"VERSION").exists(), "UNAPPROVED_RELEASE_IDENTITY", "VERSION now exists: review owner decision")
        return {"controls": controls, "shared_byte_copies": 3*8*(len(files)-8), "entry_transforms": 24,
                "release_version": "UNKNOWN; absent, not invented"}
    if group == "G07":
        c.readonly(files)
    elif group == "G08":
        c.enums_and_examples(files,data)
    elif group == "G09":
        c.ast_mapping(files,data)
    elif group == "G10":
        c.memory_templates(files)
    elif group == "G11":
        return {"templates": c.neutral_templates(files), "scan": "bounded patterns and field defaults; not DLP"}
    elif group == "G12":
        inv = context["inventory"]
        catalog = json.loads((ROOT/pack.CATALOG).read_bytes())
        outputs = {t:r["outputs"] for t,r in inv["packages"].items()}
        c.allowlist(data,packages,catalog,outputs)
        c.need({p:sha(data[p]) for p in catalog["sources"]} == inv["inputs"], "INPUT_HASH", "P23 artifact sources")
        for p,digest in inv["tooling_sha256"].items():
            c.need(sha((ROOT/p).read_bytes())==digest,"TOOL_HASH",p)
        for t,payload in packages.items():
            c.need({p:sha(b) for p,b in payload.items()} == {p:r["sha256"] for p,r in outputs[t].items()},
                   "PAYLOAD_HASH",t)
            c.need(sha(context["archives"][t])==inv["packages"][t]["archive_sha256"],"ARCHIVE_HASH",t)
        return {"allowlisted_inputs":len(catalog["sources"]), "payload_files":{t:len(p) for t,p in packages.items()}}
    elif group == "G13":
        scratch = Path(tempfile.mkdtemp(prefix="kiyo p24 static "))
        context["scratch"] = str(scratch)
        checker = scratch/"isolated payload checker.py"
        shutil.copyfile(ROOT/"tools/verify_payload.py",checker)
        results = {}
        for target,data_zip in context["archives"].items():
            extracted = safe_extract(data_zip,scratch/f"{target} path with spaces")
            c.need(verify_payload.collect(extracted)==packages[target],"EXTRACTION_BYTES",target)
            command = [sys.executable,"-I","-B",str(checker),str(extracted),target,
                       "--deny-probe",str(ROOT/"src/kiyo/KIYO.md")]
            run = subprocess.run(command,cwd=scratch,capture_output=True,text=True)
            row = {"command":command,"cwd":str(scratch),"exit_code":run.returncode,
                   "stdout":run.stdout,"stderr":run.stderr}
            context["subcommands"].append(row)
            c.need(run.returncode==0,"RELOCATION_CHECK",target+": "+run.stderr)
            results[target]=json.loads(run.stdout)
        return {"scratch":str(scratch),"isolated_results":results,
                "limitations":"Cooperative audit guard, not OS sandbox; Windows only; native hosts NOT_TESTED"}
    elif group == "G14":
        return c.budgets(files,packages)
    elif group == "G15":
        c.substance(files)
        return {"canonical_nonempty_files":len(files)}
    elif group == "G16":
        c.requirements(data)
        return {"unique_requirements":80,"unique_trace_rows":80,"full_requirement_verification":"NOT_RUN"}
    else:
        raise ValueError("Unknown group "+group)
    return {"contract":"selected structured/normative assertions satisfied"}


def mutate(fixture, data, packages):
    data = dict(data)
    packages = {t:dict(p) for t,p in packages.items()}
    operation,path = fixture["operation"],fixture["path"]
    if operation == "package-add":
        target, destination = path, fixture["match"]
        c.need(destination not in packages[target],"FIXTURE_PRECONDITION",fixture["id"])
        packages[target][destination] = fixture["value"].encode()
    elif operation == "copy":
        destination = fixture["value"]
        c.need(destination not in data,"FIXTURE_PRECONDITION",fixture["id"])
        data[destination] = data[path]
    elif operation == "delete":
        del data[path]
    elif operation == "set":
        data[path] = fixture["value"].encode()
    elif operation == "append":
        data[path] += fixture["value"].encode()
    elif operation == "json-field":
        obj = json.loads(data[path])
        c.need(fixture["match"] not in obj,"FIXTURE_PRECONDITION",fixture["id"])
        obj[fixture["match"]] = fixture["value"]
        data[path] = json.dumps(obj).encode()
    elif operation == "replace":
        s = c.text(data,path)
        c.need(s.count(fixture["match"])==1,"FIXTURE_PRECONDITION",fixture["id"]+" exact single mutation")
        data[path] = s.replace(fixture["match"],fixture["value"]).encode()
    else:
        raise ValueError("Unknown mutation "+operation)
    return data,packages


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report",type=Path,required=True)
    parser.add_argument("--inventory",type=Path,help="Candidate inventory; defaults to retained P23 inventory")
    parser.add_argument("--archives",type=Path,help="Candidate ZIP directory; defaults to dist/archives")
    args=parser.parse_args()
    if args.report.exists():
        raise SystemExit("Choose a fresh report path; retain previous executions.")
    started=datetime.now(timezone.utc).isoformat()
    context={"subcommands":[]}
    checks=[]
    report={"format":"kiyo-static-contract-evidence-1","started_utc":started,
            "command":sys.orig_argv,"cwd":str(Path.cwd()),"python":platform.python_version(),
            "os":platform.platform(),"checks":checks,"subcommands":context["subcommands"],
            "scope":"Selected static contracts; NOT full schema validation",
            "behavioral_evidence":"NOT_TESTED by this suite",
            "native_host_evidence":"NOT_TESTED; Codex IDE native plugin route UNSUPPORTED",
            "limitations":["No proof agents obey Markdown; no security/DLP certification",
                           "No native parser, installation, network, production, or OS sandbox test",
                           "P23 real filesystem symlink creation BLOCKED; not retried here"]}
    stream=io.StringIO()
    try:
        c.need(bool(args.inventory) == bool(args.archives), "CANDIDATE_ARGUMENTS",
               "Supply --inventory and --archives together")
        data,packages,archives,inventory=load_context(args.inventory,args.archives)
        report["candidate"]={"inventory":str(args.inventory or ROOT/"docs/evidence/packaging/artifact-inventory.json"),
                             "archives":str(args.archives or ROOT/"dist/archives")}
        context.update(archives=archives,inventory=inventory)
        report["consulted_sha256"]={p:sha(b) for p,b in data.items()}
        codepaths = ("tests/static/contracts.py","tests/static/test_contracts.py",
                     "tools/verify_payload.py","tests/packaging/test_distributions.py",*pack.TOOLING)
        report["tooling_sha256"]={p:sha((ROOT/p).read_bytes()) for p in codepaths}
        git=["git","-c","safe.directory="+ROOT.as_posix(),"-c","core.excludesFile=",
             "-C",str(ROOT),"rev-parse","HEAD"]
        observed=subprocess.run(git,capture_output=True,text=True)
        report["git_observation"]={"command":git,"exit_code":observed.returncode,
                                   "stdout":observed.stdout,"stderr":observed.stderr,
                                   "scope":"Base commit only; worktree hashes above identify inspected inputs"}
        c.need(observed.returncode==0,"GIT_OBSERVATION","cannot record baseline")
        suite=unittest.TestSuite()
        def positive(group,name):
            def check():
                row={"id":group,"name":name,"kind":"positive",
                     "applicability":"Required Prompt 24 static group", "command_ref":"command",
                     "method":"run_group("+group+")", "inspected_scope":"Canonical files and existing ZIPs as defined by this group",
                     "evidence_location":str(args.report), "limitations":"Selected properties; no behavioral/native assertion",
                     "baseline_relation":"Selected candidate bytes and recorded source hashes; previous attempts retained"}
                checks.append(row)
                try:
                    row["observed"]=run_group(group,data,packages,context)
                    row["status"]="PASS"
                except Exception as error:
                    row.update(status="FAIL",error=str(error))
                    raise
            return unittest.FunctionTestCase(check,description=group+" "+name)
        for i,name in enumerate(GROUPS,1):
            suite.addTest(positive(f"G{i:02}",name))
        fixtures=sorted((ROOT/"tests/static/fixtures").glob("*.json"))
        fixture_data = [json.loads(p.read_bytes()) for p in fixtures]
        fixture_ids = [f["id"] for f in fixture_data]
        c.need(len(fixture_ids)==len(set(fixture_ids)) and REQUIRED_NEGATIVES<=set(fixture_ids),
               "FIXTURE_INVENTORY","six named required negatives, unique IDs")
        report["fixtures_sha256"]={p.relative_to(ROOT).as_posix():sha(p.read_bytes()) for p in fixtures}
        def negative(fixture):
            def check():
                row={"id":fixture["id"],"group":fixture["group"],"kind":"negative",
                     "name":fixture["id"],"expected_code":fixture["expected_code"],"expected_detail":fixture["expected_detail"],
                     "applicability":"Synthetic rejection regression", "command_ref":"command",
                     "method":"Mutate isolated bytes, run owning group, assert exact code and detail",
                     "inspected_scope":fixture["path"], "evidence_location":str(args.report),
                     "limitations":"No malicious execution; bounded counterexample, not exhaustive proof",
                     "baseline_relation":"Mutation only; original product remains unchanged"}
                checks.append(row)
                try:
                    c.need(fixture["synthetic"] is True,"FIXTURE_INPUT",fixture["id"])
                    changed,changed_packages=mutate(fixture,data,packages)
                    try:
                        run_group(fixture["group"],changed,changed_packages,context)
                    except c.Violation as error:
                        row.update(observed_code=error.code,observed_detail=error.detail)
                        c.need(error.code==fixture["expected_code"] and fixture["expected_detail"] in error.detail,
                               "NEGATIVE_WRONG_REASON",fixture["id"]+": "+str(error))
                    else:
                        raise c.Violation("NEGATIVE_MISSED",fixture["id"])
                    row["status"]="PASS"
                except Exception as error:
                    row.update(status="FAIL",error=str(error))
                    raise
            return unittest.FunctionTestCase(check,description="negative "+fixture["id"])
        for fixture in fixture_data:
            suite.addTest(negative(fixture))
        result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
        exit_code=0 if result.wasSuccessful() else 1
        report.update(tests_run=result.testsRun,failures=len(result.failures),errors=len(result.errors),
                      skipped=len(result.skipped))
    except Exception:
        traceback.print_exc(file=stream)
        exit_code=1
    report.update(exit_code=exit_code,output=stream.getvalue(),finished_utc=datetime.now(timezone.utc).isoformat())
    if "scratch" in context:
        report["scratch"]=context["scratch"]
    args.report.parent.mkdir(parents=True,exist_ok=True)
    with args.report.open("x",encoding="utf-8",newline="\n") as handle:
        json.dump(report,handle,indent=2,sort_keys=True)
        handle.write("\n")
    print(stream.getvalue(),end="")
    print("Evidence: "+str(args.report))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())

