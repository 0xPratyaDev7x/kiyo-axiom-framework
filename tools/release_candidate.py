"""Developer-only local release rehearsal. No host, install, signing or publishing."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import ast
import collections
import json
import platform
import re
import subprocess
import sys
import tempfile

import package_distributions as pack
import verify_payload
from package_claude import require, sha, reject_links

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests/packaging"))
from test_distributions import safe_extract

CODE = (*pack.TOOLING, "tools/verify_payload.py", "tools/release_candidate.py",
        "tests/packaging/test_distributions.py", "tests/static/contracts.py",
        "tests/static/test_contracts.py", "tests/release/test_release.py")
SUPPORT = ("docs/build/REQUIREMENTS.md", "docs/build/TRACEABILITY.md",
           "tests/behavioral/verification/scenarios.md",
           "tests/behavioral/agent-security/scenarios.md")
TARGETS = ("claude-cli", "claude-vscode", "codex-cli", "codex-ide",
           "copilot-cli", "copilot-vscode")
STAGES = ("Validate", "Package", "Inspect payload", "Run tests",
          "Artifact inventory", "Release-readiness report")


def now():
    return datetime.now(timezone.utc).isoformat()


def write(path, value):
    reject_links(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = value if isinstance(value, str) else json.dumps(value, indent=2, sort_keys=True) + "\n"
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def output_path(path):
    """Only a fresh direct child of this checkout's developer release directory."""
    path = path.absolute()
    reject_links(path)
    require(path.parent.resolve() == (ROOT / "dist/releases").resolve()
            and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", path.name),
            "Output must be a named direct child of dist/releases")
    require(not path.exists(), "Output already exists; preserve evidence and choose a fresh run")
    return path


def versions(manifests):
    require(manifests and {m.get("name") for m in manifests.values()} == {"kiyo-axiom-framework"},
            "Native identity mismatch")
    values = {path: m.get("version") for path, m in manifests.items()}
    require(all(v is None or isinstance(v, str) and v.strip() for v in values.values()),
            "Invalid version metadata")
    require(len(set(values.values())) == 1, "Mixed or inconsistent native versions")
    value = next(iter(values.values()))
    return {"status": "PASS", "values": values, "product_version": value or "UNSET",
            "scope": "Manifest identity/version equality; not semantic-version/schema or owner approval",
            "publication_version_gate": "OWNER_REQUIRED" if value is None else "OWNER_APPROVAL_UNVERIFIED"}


def snapshot():
    paths = set(CODE) | set(SUPPORT)
    paths.update(p.relative_to(ROOT).as_posix()
                 for p in (ROOT / "tests/static/fixtures").glob("*.json"))
    return {p: sha((ROOT / p).read_bytes()) for p in sorted(paths)}


def review_inventories(inputs):
    citations = {}
    for path, content in inputs.items():
        if path.endswith(".md"):
            for url in re.findall(r"\]\((https://[^)]+)\)", content.decode("utf-8")):
                citations.setdefault(url, []).append(path)
    imports = set()
    for path in CODE:
        if not path.endswith(".py"):
            continue
        tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(n.name.split(".")[0] for n in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".")[0])
    local = {Path(p).stem for p in CODE if p.endswith(".py")}
    external = sorted(imports - local - set(sys.stdlib_module_names))
    require(not external, "Unreviewed developer imports: " + ", ".join(external))
    dependencies = {
        "format": "kiyo-dependency-inventory-1", "formal_sbom": False,
        "payload_runtime_dependencies": [],
        "payload_executables_hooks_mcp": [],
        "developer": {"python": platform.python_version(), "python_packages_required": [],
                      "stdlib_imports": sorted(imports & set(sys.stdlib_module_names)),
                      "repository_modules": sorted(imports & local), "git": "See source-revision.json"},
        "host_prerequisites": "External native host/account/policy; not bundled runtime dependencies",
        "scope": list(CODE),
        "limitations": "Reviewed static imports/tooling; not an installed-machine inventory or formal SBOM"}
    attribution = {
        "format": "kiyo-attribution-inventory-1", "formal_sbom": False,
        "project_license": {"path": "LICENSE", "sha256": sha(inputs["LICENSE"]),
                            "observed_heading": inputs["LICENSE"].decode().splitlines()[0],
                            "publication_confirmation": "OWNER_REQUIRED"},
        "bundled_third_party_runtime_components": [],
        "third_party_reference_citations": [{"url": u, "canonical_files": sorted(set(ps)),
                                            "treatment": "Reference attribution, not vendored runtime"}
                                           for u, ps in sorted(citations.items())],
        "limitations": "No legal clearance or license grant inferred for external documents. "
                       "No external text fetched by pipeline; ISO full text is not bundled. "
                       "Human review of authored prose remains required."}
    return dependencies, attribution


def package_status(stages, blocked):
    # The optional Windows symlink probe never disappears into an exit-zero summary.
    if (tuple(s.get("name") for s in stages) != STAGES
            or any(s.get("status") != "PASS" for s in stages)):
        return "PACKAGE_NOT_VALIDATED"
    return "PACKAGE_VALIDATED_WITH_LIMITATIONS" if blocked else "PACKAGE_VALIDATED"


class Pipeline:
    def __init__(self, output):
        self.output = output
        self.commands = []
        self.stages = []

    def command(self, argv):
        row = {"argv": [str(a) for a in argv], "cwd": str(ROOT), "started_utc": now()}
        self.commands.append(row)
        try:
            run = subprocess.run(row["argv"], cwd=ROOT, capture_output=True,
                                 text=True, encoding="utf-8", errors="replace")
            row.update(exit_code=run.returncode, stdout=run.stdout, stderr=run.stderr)
        except OSError as error:
            row.update(exit_code=None, stdout="", stderr=str(error))
            raise
        finally:
            row["finished_utc"] = now()
        require(row["exit_code"] == 0, f"Command failed: {row['argv']}; see pipeline.json")
        return row["stdout"].strip()

    def git(self, *args):
        return self.command(["git", "-c", "safe.directory=" + ROOT.as_posix(),
                             "-c", "core.excludesFile=", *args])

    def stage(self, name, action):
        row = {"name": name, "status": "NOT_RUN", "started_utc": now()}
        self.stages.append(row)
        print("Stage: " + name, flush=True)
        try:
            row["observed"] = action()
            row["status"] = "PASS"
        except Exception as error:
            row.update(status="FAIL", error=f"{type(error).__name__}: {error}")
            raise
        finally:
            row["finished_utc"] = now()


def run(output):
    output = output_path(output)
    output.mkdir(parents=True)
    pipeline = Pipeline(output)
    state = {"format": "kiyo-release-rehearsal-1", "started_utc": now(),
             "command": sys.orig_argv, "python": platform.python_version(), "os": platform.platform(),
             "commands": pipeline.commands, "stages": pipeline.stages, "blocked_checks": [],
             "host_status": {t: "UNSUPPORTED" if t == "codex-ide" else "NOT_TESTED" for t in TARGETS},
             "host_scope": "This pipeline launches no host. P26 partial evidence remains separate.",
             "signature": "NOT_SIGNED", "provenance_attestation": "NOT_ATTESTED",
             "publication_status": "NOT_PUBLISHED", "publication_readiness": "BLOCKED",
             "publication_blockers": ["Owner name/version/license/publisher/source/destination/approval unresolved",
                 "Native metadata/ingestion release failures retained",
                 "Independent host/behavior/activation/update acceptance incomplete",
                 "Human security/license review and disclosure contact not established"],
             "limitations": ["Selected static properties, not FULL SCHEMA VALIDATION",
                 "Checksums and local source records do not authenticate publisher or production state",
                 "No secret/DLP, host enforcement, behavioral or security guarantee"]}
    try:
        inputs = pack.inputs(ROOT)
        before = snapshot()
        def validate():
            state["source"] = {"head": pipeline.git("rev-parse", "HEAD"),
                               "branch": pipeline.git("branch", "--show-current"),
                               "git_version": pipeline.git("--version"),
                               "working_tree_porcelain": pipeline.git("status", "--porcelain=v1", "--untracked-files=normal"),
                               "input_sha256": {p: sha(b) for p, b in inputs.items()},
                               "developer_and_contract_sha256": before,
                               "scope": "Actual base plus current worktree input hashes; not a signed attestation"}
            write(output / "source-revision.json", state["source"])
            manifests = {p: json.loads(b) for p, b in inputs.items() if p.endswith("plugin.json")}
            manifests["derived:.codex-plugin/plugin.json"] = pack.codex.compatibility_manifest(
                manifests["platforms/codex/plugin.json"])
            state["version"] = versions(manifests)
            require(not (ROOT / "VERSION").exists(), "Unexpected VERSION; review canonical version authority")
            write(output / "version-consistency.json", state["version"])
            for builder in pack.BUILDERS.values():
                builder.make_payload(ROOT)
            return {"inputs": len(inputs), "version": state["version"]["product_version"],
                    "method": "Closed input/manifest/resource validation by existing native builders"}

        pipeline.stage("Validate", validate)

        def package():
            for directory, inventory in (("archives", "artifact-inventory.json"),
                                         ("reproducibility", "repeat-inventory.json")):
                pipeline.command([sys.executable, "-B", "tools/package_distributions.py",
                                  "--output", output / directory, "--inventory", output / inventory])
            a = json.loads((output / "artifact-inventory.json").read_bytes())
            b = json.loads((output / "repeat-inventory.json").read_bytes())
            require(a == b, "Two actual build inventories differ")
            for package in a["packages"].values():
                name = package["archive"]
                require((output / "archives" / name).read_bytes() ==
                        (output / "reproducibility" / name).read_bytes(), "Reproducibility failure: " + name)
            state["inventory"] = a
            return {"builds": 2, "inventories_equal": True, "archive_bytes_equal": True}

        pipeline.stage("Package", package)

        def inspect():
            scratch = Path(tempfile.mkdtemp(prefix="kiyo p28 release "))
            observed = {}
            for target, entry in state["inventory"]["packages"].items():
                blob = (output / "archives" / entry["archive"]).read_bytes()
                require(sha(blob) == entry["archive_sha256"], "Archive digest mismatch")
                extracted = safe_extract(blob, scratch / (target + " path with spaces"))
                payload = verify_payload.collect(extracted)
                require({p: sha(b) for p, b in payload.items()} ==
                        {p: r["sha256"] for p, r in entry["outputs"].items()}, "Extracted member mismatch")
                observed[target] = verify_payload.validate(payload, target)
            write(output / "payload-inspection.json", {"scratch": str(scratch), "targets": observed,
                  "scope": "Actual regular contained extraction, allowlist, nine Skills and relative references",
                  "limitation": "Static checker, not host loading or comprehensive secret scanning"})
            return observed

        pipeline.stage("Inspect payload", inspect)

        def tests():
            exits = {}
            for script, name, extra in (
                ("tests/static/test_contracts.py", "static.json",
                 ["--inventory", output / "artifact-inventory.json", "--archives", output / "archives"]),
                ("tests/packaging/test_distributions.py", "packaging.json", []),
                ("tests/release/test_release.py", "release-tests.json", [])):
                pipeline.command([sys.executable, "-B", script, "--report", output / "evidence" / name, *extra])
                exits[name] = pipeline.commands[-1]["exit_code"]
            reports = {p: json.loads((output / "evidence" / p).read_bytes())
                       for p in ("static.json", "packaging.json", "release-tests.json")}
            state["blocked_checks"] = [r for r in reports["packaging.json"]["checks"] if r["status"] == "BLOCKED"]
            require(all(r["id"] == "PKG-08" for r in state["blocked_checks"]), "Unexpected blocked required check")
            require(all(r["status"] in ("PASS", "BLOCKED") for r in reports["packaging.json"]["checks"]),
                    "Packaging check did not pass")
            return {p: {"status_counts": dict(collections.Counter(r["status"] for r in d.get("checks", []))),
                        "tests_run": d.get("tests_run"), "command_exit_code": exits[p],
                        "failures": d.get("failures"), "errors": d.get("errors"),
                        "note": "Packaging runner reports individual checks; inspect BLOCKED even on exit 0"}
                    for p, d in reports.items()}

        pipeline.stage("Run tests", tests)

        def inventory():
            require(pack.inputs(ROOT) == inputs and snapshot() == before,
                    "Inputs/tooling/contracts changed during release run; candidate not validated")
            require(pipeline.git("rev-parse", "HEAD") == state["source"]["head"], "HEAD changed during release run")
            dependencies, attribution = review_inventories(inputs)
            write(output / "dependency-inventory.json", dependencies)
            write(output / "attribution-inventory.json", attribution)
            previous = json.loads((ROOT / "docs/evidence/packaging/artifact-inventory.json").read_bytes())
            current = state["inventory"]["inputs"]
            changed = sorted(p for p in set(previous["inputs"]) | set(current)
                             if previous["inputs"].get(p) != current.get(p))
            write(output / "security-change-notes.json", {
                "baseline": "docs/evidence/packaging/artifact-inventory.json",
                "baseline_sha256": sha((ROOT / "docs/evidence/packaging/artifact-inventory.json").read_bytes()),
                "changed_product_inputs": changed,
                "review": "Compare changed instructions, metadata, resources, access/destinations and approvals",
                "ast_controls": ["KIYO-SEC-004", "KIYO-SEC-005", "KIYO-SEC-007", "KIYO-SEC-009"],
                "limitations": "No changed allowlisted bytes does not close prior native/behavior/security gaps"})
            sums = "".join(f"{entry['archive_sha256']}  archives/{entry['archive']}\n"
                           for entry in state["inventory"]["packages"].values())
            write(output / "SHA256SUMS", sums)
            return {"payload_runtime_dependencies": 0, "formal_sbom": False,
                    "changed_product_inputs": changed, "reference_citations": len(attribution["third_party_reference_citations"])}

        pipeline.stage("Artifact inventory", inventory)
        # Pipeline success cannot promote external approval, host tests or publication.
        pipeline.stage("Release-readiness report", lambda: {"publication": "BLOCKED", "signed": False,
                       "host_verified": False, "reason": "Independent evidence and owner gates retained"})
        state.update(exit_code=0, package_status=package_status(pipeline.stages, state["blocked_checks"]))
    except Exception as error:
        state.update(exit_code=1, package_status="PACKAGE_NOT_VALIDATED",
                     failure=f"{type(error).__name__}: {error}")
    state.pop("inventory", None)  # Full content/provenance is in its separate inventory.
    summary = ["# Local release readiness", "", "Generated developer evidence; not a release or publication.",
               "", f"- Package: **{state['package_status']}**",
               "- Host: **NOT_HOST_VERIFIED** (six statuses in pipeline.json)",
               "- Publication: **NOT_PUBLISHED / BLOCKED**",
               "- Signature: **NOT_SIGNED**; provenance attestation: **NOT_ATTESTED**",
               f"- Pipeline exit: {state['exit_code']}",
               "- Checksums identify bytes, not publisher identity.",
               "- Read pipeline.json for commands, results, failures and blocked checks.",
               "- Read artifact-inventory.json for per-file hashes and canonical provenance.",
               "- Read dependency-inventory.json / attribution-inventory.json; neither is a formal SBOM.",
               "", "Publication blockers:", *["- " + b for b in state["publication_blockers"]], ""]
    if "failure" in state:
        summary += ["Failure: " + state["failure"], ""]
    try:
        write(output / "readiness.md", "\n".join(summary))
    except (OSError, ValueError) as error:
        failure = f"Readiness output failed: {type(error).__name__}: {error}"
        state.update(exit_code=1, package_status="PACKAGE_NOT_VALIDATED",
                     failure=(state.get("failure", "") + "; " + failure).lstrip("; "))
        if pipeline.stages and pipeline.stages[-1]["name"] == "Release-readiness report":
            pipeline.stages[-1].update(status="FAIL", error=failure)
    if pipeline.stages and pipeline.stages[-1]["name"] == "Release-readiness report":
        pipeline.stages[-1]["finished_utc"] = now()
    state["finished_utc"] = now()
    # Persist success only after required report I/O has actually succeeded.
    write(output / "pipeline.json", state)
    print(json.dumps({"output": str(output), "package_status": state["package_status"],
                      "publication": state["publication_status"], "exit_code": state["exit_code"]}))
    return state["exit_code"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        return run(args.output)
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
