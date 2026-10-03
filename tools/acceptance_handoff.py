"""Developer-only P30 final handoff audit; no host, network, install or publication."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse
import hashlib
import json
import re
import subprocess
import sys
import zipfile
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "dist/releases/p30-run-01"
BASE = "f5a6b3b428eb4e7096e0620a52ee7ccdd2fbace4"
SKILLS = ("init", "requirement", "implement", "review", "test", "security", "architecture", "memory", "performance")
CASE_PREFIX = dict(zip(SKILLS, ("INIT", "REQ", "IMPL", "REV", "TEST", "SEC", "ARCH", "MEM", "PERF")))
TARGETS = ("claude-cli", "claude-vscode", "codex-cli", "codex-ide", "copilot-cli", "copilot-vscode")
DOCS = ("docs/build/FINAL-ACCEPTANCE.md", "docs/build/PROGRESS.md",
        "docs/build/HANDOFF.md", "docs/build/OPEN-ISSUES.md",
        "docs/build/TRACEABILITY.md", "docs/build/BASELINE.md",
        "docs/build/DECISIONS.md", "docs/research/SOURCES.md",
        "docs/release/publication-runbook.md", "docs/release/owner-actions.md",
        "docs/release/submission-checklists.md",
        "docs/evidence/acceptance/validation-report.md", "README.md")


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(blob):
    return hashlib.sha256(blob).hexdigest()


def need(value, message):
    if not value:
        raise ValueError(message)


def read(path):
    return json.loads((ROOT / path).read_bytes())


def exact_file(path):
    need(path.resolve().is_relative_to(ROOT.resolve()), "Reference escapes checkout")
    cursor = ROOT
    for part in path.relative_to(ROOT).parts:
        need(part in {p.name for p in cursor.iterdir()}, "Missing/case-mismatched reference: " + str(path))
        cursor /= part
        need(not cursor.is_symlink() and not (getattr(cursor.lstat(), "st_file_attributes", 0) & 1024),
             "Symlink/reparse reference")
    need(path.is_file(), "Expected file reference: " + str(path))


def dump(path, value):
    with path.open("x", encoding="utf-8", newline="\n") as output:
        json.dump(value, output, indent=2, ensure_ascii=False)
        output.write("\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    destination = args.output.absolute()
    need(destination.parent.resolve() == (ROOT / "docs/evidence/acceptance").resolve(),
         "Use a fresh direct child of docs/evidence/acceptance")
    need(not destination.exists(), "Keep existing evidence; choose a fresh output")
    destination.mkdir(parents=True)
    report = {"format": "kiyo-final-acceptance-checks-1", "command": sys.orig_argv,
              "started_utc": now(), "checks": [], "commands": [],
              "limitations": "Offline artifact/document/record checks; no behavioral, portal or host execution."}

    def check(key, method):
        row = {"id": key, "started_utc": now()}
        try:
            row.update(status="PASS", observed=method())
        except Exception as error:
            row.update(status="FAIL", error=f"{type(error).__name__}: {error}")
            raise
        finally:
            row["finished_utc"] = now()
            report["checks"].append(row)

    def git(*argv):
        command = ["git", "-c", "safe.directory=" + ROOT.as_posix(), "-c", "core.excludesFile=", *argv]
        result = subprocess.run(command, cwd=ROOT, capture_output=True)
        report["commands"].append({"argv": command, "exit_code": result.returncode,
                                  "stdout": result.stdout.decode("utf-8", "replace"),
                                  "stderr": result.stderr.decode("utf-8", "replace")})
        need(result.returncode == 0, "Git read failed")
        return result.stdout

    inventory = {"format": "kiyo-final-handoff-1", "candidate": "p30-run-01",
                 "product_version": "UNSET", "artifact_status": "DEVELOPMENT_UNRELEASED",
                 "source_revision": BASE, "readiness": {
                     "CONTENT_READY": "YES for authored static Core/Skills/Policies/Templates only",
                     "PACKAGE_VALIDATED": "WITH_LIMITATIONS: PKG-08 Windows 1314",
                     "HOST_VERIFIED": False, "PUBLISHING_READY": False, "PUBLISHED": False},
                 "signature": "NOT_SIGNED", "provenance_attestation": "NOT_ATTESTED"}
    try:
        source = read("dist/releases/p30-run-01/source-revision.json")
        pipeline = read("dist/releases/p30-run-01/pipeline.json")
        content = read("dist/releases/p30-run-01/artifact-inventory.json")
        ledger = read("docs/build/requirement-audit.json")
        catalog = read("tests/behavioral/evaluation/catalog.json")
        behavior = read("docs/evidence/behavioral/observations.json")

        def baseline():
            need(git("rev-parse", "HEAD").decode().strip() == BASE == source["head"], "Changed base revision")
            need(not git("diff", "--cached", "--name-only").strip(), "Unexpected staged changes")
            for path, digest in content["inputs"].items():
                need(sha((ROOT / path).read_bytes()) == digest, "Changed product input: " + path)
            for path, digest in source["developer_and_contract_sha256"].items():
                if path != "docs/build/TRACEABILITY.md":
                    need(sha((ROOT / path).read_bytes()) == digest, "Changed pipeline input: " + path)
            changed = git("diff", "--name-only", BASE).decode().splitlines()
            need(set(changed) <= set(DOCS), "Unscoped tracked edit")
            # Git stores normalized text while the Windows checkout has CRLF.
            # Exact worktree-byte preservation is checked in content inputs above.
            need(git("show", BASE + ":LICENSE").replace(b"\r\n", b"\n") ==
                 (ROOT / "LICENSE").read_bytes().replace(b"\r\n", b"\n"), "LICENSE content changed")
            need(not (ROOT / ".kiyo").exists(), "Unexpected project memory initialization")
            inventory["documentation_sha256"] = {p: sha((ROOT / p).read_bytes()) for p in DOCS}
            return {"head": BASE, "preserved_product_inputs": len(content["inputs"]), "tracked_changes": changed,
                    "memory_impact": "NONE", "trace_snapshot_note": "Final trace prose postdates pipeline; criteria and product unchanged"}
        check("FA-01-baseline-preservation", baseline)

        def packages():
            need(pipeline["exit_code"] == 0, "Pipeline failed")
            need([(x["name"], x["status"]) for x in pipeline["stages"]] == [
                (n, "PASS") for n in ("Validate", "Package", "Inspect payload", "Run tests",
                                      "Artifact inventory", "Release-readiness report")], "Incomplete pipeline")
            need(pipeline["package_status"] == "PACKAGE_VALIDATED_WITH_LIMITATIONS", "Package scope changed")
            need([x["id"] for x in pipeline["blocked_checks"]] == ["PKG-08"], "Unexpected blocked checks")
            need(content == read("dist/releases/p30-run-01/repeat-inventory.json"), "Repeat inventory differs")
            old = read("dist/releases/p29-run-02/artifact-inventory.json")
            need(content["inputs"] == old["inputs"], "Changed historical product")
            entries = {}
            sums = []
            for target, item in content["packages"].items():
                archive = RUN / "archives" / item["archive"]
                blob = archive.read_bytes()
                need(sha(blob) == item["archive_sha256"] == old["packages"][target]["archive_sha256"],
                     "Archive digest changed")
                need(blob == (RUN / "reproducibility" / item["archive"]).read_bytes(), "Repeat bytes differ")
                with zipfile.ZipFile(archive) as zipped:
                    files = {n.removeprefix("kiyo-axiom-framework/"): zipped.read(n) for n in zipped.namelist()}
                need({p: sha(b) for p, b in files.items()} ==
                     {p: r["sha256"] for p, r in item["outputs"].items()}, "Member inventory mismatch")
                need(sorted(p.split("/")[1] for p in files if re.fullmatch(r"skills/[^/]+/SKILL.md", p))
                     == sorted(SKILLS), "Public Skill inventory mismatch")
                metadata = {p: json.loads(b) for p, b in files.items() if p.endswith("plugin.json")}
                need(all(m.get("version") is None and m["name"] == "kiyo-axiom-framework" for m in metadata.values()),
                     "Invented identity/version")
                entries[target] = {"path": archive.relative_to(ROOT).as_posix(), "sha256": sha(blob),
                                   "bytes": len(blob), "files": len(files), "skills": list(SKILLS),
                                   "root_readme_present": "README.md" in files}
                sums.append(sha(blob) + "  " + entries[target]["path"])
            inventory["artifacts"] = entries
            inventory["channel_preflight"] = {
                "GAP30-01": {"claude_root_readme": entries["claude"]["root_readme_present"],
                             "claude_files": entries["claude"]["files"], "documented_reviewer_threshold": 512,
                             "result": "MISSING_README_AND_REVIEWER_THRESHOLD_EXCEEDED",
                             "scope": "Local comparison with PUB30-03, not portal rejection"},
                "GAP30-02": {"result": "OWNER INPUT REQUIRED", "scope": "PUB30-07 route applicability inference"}}
            (destination / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8")
            return entries
        check("FA-02-actual-artifacts", packages)

        def requirements():
            expected = [f"REQ-{n:03}" for n in range(1, 81)]
            text = (ROOT / "docs/build/REQUIREMENTS.md").read_text(encoding="utf-8")
            trace = (ROOT / "docs/build/TRACEABILITY.md").read_text(encoding="utf-8")
            need(re.findall(r"^## (REQ-\d{3})$", text, re.M) == expected, "Registry omission")
            need(re.findall(r"^\| (REQ-\d{3}) \|", trace, re.M) == expected, "Trace omission")
            need([r["id"] for r in ledger["requirements"]] == expected, "Ledger omission")
            rows = []
            for row in ledger["requirements"]:
                need(row["verification_status"] == "NOT_RUN", "Full acceptance promoted")
                files = row["implementing_files"]
                for path in files:
                    exact_file(ROOT / path)
                representations = {}
                for target, item in content["packages"].items():
                    representations[target] = [{"canonical": v["source"], "member": p,
                                                 "transform": v["transform"], "sha256": v["sha256"]}
                        for p, v in item["outputs"].items() if v["source"] in files]
                rows.append({"id": row["id"], "skill_or_procedure": row["skills_and_shared_procedures"],
                    "implementing_files": files, "package_representations": representations,
                    "non_payload_files": [p for p in files if p not in content["inputs"]],
                    "implementation_status": row["implementation_status"], "full_verification": "NOT_RUN",
                    "behavioral_cases": row["behavioral_cases"], "actual_evidence": row["actual_evidence"],
                    "gaps": row["gap_ids"], "scope": "Only direct source/output mappings; docs/tools intentionally outside payload"})
            inventory["requirements"] = rows
            inventory["skill_chains"] = [{"logical_id": "kiyo." + s, "canonical": f"src/kiyo/skills/{s}/SKILL.md",
                "package_entry": f"skills/{s}/SKILL.md",
                "core": f"skills/{s}/references/kiyo/KIYO.md",
                "behavioral_cases": [c["id"] for c in catalog["cases"] if c["id"].startswith("BEH-" + CASE_PREFIX[s] + "-")],
                "behavioral_status": "NOT_RUN"} for s in SKILLS]
            need(all(len(s["behavioral_cases"]) == 4 for s in inventory["skill_chains"]), "Missing Skill cases")
            return {"requirements": len(rows), "implementation": dict(Counter(r["implementation_status"] for r in rows)),
                    "full_verification": "80 NOT_RUN"}
        check("FA-03-requirement-chain", requirements)

        def evidence():
            static = read("dist/releases/p30-run-01/evidence/static.json")
            release = read("dist/releases/p30-run-01/evidence/release-tests.json")
            need(static["tests_run"] == 37 and all(r["status"] == "PASS" for r in static["checks"]), "Static result gap")
            need(release["tests_run"] == 10 and release["exit_code"] == 0, "Release regression gap")
            need(behavior["host_runs"] == 0 and len(behavior["records"]) == 48
                 and all(r["result"] == "NOT_RUN" for r in behavior["records"]), "Behavior silently promoted")
            live = {t: read("docs/evidence/live/" + t + ".json") for t in TARGETS}
            checks = [r for d in live.values() for r in d["checks"]]
            counts = dict(Counter(r["execution_status"] for r in checks))
            need(len(checks) == 72 and counts == {"NOT_RUN": 70, "PASS": 2}, "Live result scope changed")
            inventory["evidence"] = {"pipeline": "dist/releases/p30-run-01/pipeline.json",
                "static_pass": 37, "release_regressions_pass": 10, "behavioral_not_run": 48,
                "live_checks": counts,
                "targets": {t: {"host_version": d["host_version"], "scope": d["scope_summary"],
                    "full_behavioral_suite": d["full_behavioral_suite"], "evidence": "docs/evidence/live/" + t + ".json"}
                    for t, d in live.items()}}
            need(pipeline["publication_status"] == "NOT_PUBLISHED"
                 and pipeline["publication_readiness"] == "BLOCKED"
                 and pipeline["signature"] == "NOT_SIGNED", "Release gate changed")
            return inventory["evidence"]
        check("FA-04-evidence-separation", evidence)

        def references():
            count = 0
            for name in DOCS:
                path = ROOT / name
                exact_file(path)
                body = path.read_text(encoding="utf-8")
                body = re.sub(r"(?ms)^(`{3}|~{3}).*?^\1[^\n]*$", "", body)
                for match in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", body):
                    link = unquote(match[1].strip().strip("<>"))
                    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", link):
                        continue
                    file, _, anchor = link.partition("#")
                    target = (path.parent / file).resolve() if file else path
                    # These exact outputs are written by this invocation after the
                    # reference check; do not require a previous fabricated report.
                    if target in {destination / "checks.json", destination / "handoff-inventory.json"}:
                        need(not anchor, "Unexpected self-report anchor")
                        count += 1
                        continue
                    exact_file(target)
                    if anchor and target.suffix == ".md":
                        headings = re.findall(r"^#{1,6}\s+(.+?)\s*$", target.read_text(encoding="utf-8"), re.M)
                        slugs = {re.sub(r"[^\w\- ]", "", re.sub(r"<[^>]+>", "", h).strip().lower()).replace(" ", "-") for h in headings}
                        need(anchor in slugs, "Missing anchor: " + name + " -> " + link)
                    count += 1
            return {"markdown_documents": len(DOCS), "local_links": count,
                    "scope": "Inline links/headings in delivery docs; current output locators checked structurally before creation; external sources separately researched"}
        check("FA-05-delivery-references", references)
        inventory["recorded_utc"] = now()
        dump(destination / "handoff-inventory.json", inventory)
        report["exit_code"] = 0
    except Exception as error:
        report.update(exit_code=1, failure=f"{type(error).__name__}: {error}")
    report["finished_utc"] = now()
    report["script_sha256"] = sha(Path(__file__).read_bytes())
    dump(destination / "checks.json", report)
    print(json.dumps({"output": str(destination), "exit_code": report["exit_code"],
                      "checks": [(r["id"], r["status"]) for r in report["checks"]]}))
    return report["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())

