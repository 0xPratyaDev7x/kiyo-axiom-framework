"""Bounded developer packaging tests; no native client, install, network or project bootstrap."""
from pathlib import Path, PurePosixPath
import argparse
from datetime import datetime, timezone
import io
import json
import os
import platform
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import package_distributions as pack
import verify_payload as verify
from package_claude import require, sha, write_new_or_identical


def safe_extract(data, destination):
    require(not destination.exists(), "Extraction destination must be fresh")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        members = archive.infolist()
        names = [p.filename for p in members]
        require(len({p.casefold() for p in names}) == len(names), "Duplicate/case-colliding member")
        for item in members:
            parts = PurePosixPath(item.filename).parts
            require(item.filename.startswith("kiyo-axiom-framework/") and len(parts) > 1
                    and not item.filename.startswith("/") and "\\" not in item.filename
                    and ":" not in item.filename and all(p not in (".", "..") for p in parts)
                    and "//" not in item.filename, "Unsafe ZIP member")
            require(stat.S_IFMT(item.external_attr >> 16) == stat.S_IFREG,
                    "Non-regular ZIP member (including symlink)")
        destination.mkdir(parents=True)
        for item in members:
            target = destination / item.filename
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as handle:
                handle.write(archive.read(item))
    return destination / "kiyo-axiom-framework"


def rejects(fn, label):
    try:
        fn()
    except ValueError:
        return label
    raise AssertionError("Expected rejection: " + label)


def snapshot(directory):
    return {p.relative_to(directory).as_posix(): (sha(p.read_bytes()), p.stat().st_mtime_ns)
            for p in directory.rglob("*") if p.is_file()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    require(not args.report.exists(), "Report already exists; choose a fresh report path")
    scratch = Path(tempfile.mkdtemp(prefix="kiyo p23 packaging "))
    checks = []
    def passed(case, result):
        checks.append({"id": case, "status": "PASS", "observed": result})

    # Two actual CLI builds, not simply hashing a cached artifact twice.
    records, runs = [], []
    for number in (1, 2):
        out = scratch / f"build {number}"
        inventory = scratch / f"inventory {number}.json"
        command = [sys.executable, "-B", str(ROOT / "tools/package_distributions.py"),
                   "--output", str(out), "--inventory", str(inventory)]
        run = subprocess.run(command, cwd=scratch, capture_output=True, text=True)
        require(run.returncode == 0, run.stderr or run.stdout)
        records.append(inventory.read_bytes())
        runs.append(out)
    require(records[0] == records[1], "Two build inventories differ")
    record = json.loads(records[0])
    require({p.name: p.read_bytes() for p in runs[0].iterdir()} ==
            {p.name: p.read_bytes() for p in runs[1].iterdir()}, "Two archive sets differ")
    passed("PKG-01", {"builds": 2, "inventories": "byte-identical", "archives": "byte-identical"})

    # Canonical/source parity is inspected outside the isolated checker.
    inputs = pack.inputs(ROOT)
    payloads = {}
    for target, row in record["packages"].items():
        data = (runs[0] / row["archive"]).read_bytes()
        extracted = safe_extract(data, scratch / f"fresh {target} path with spaces")
        files = verify.collect(extracted)
        payloads[target] = files
        require({p: sha(b) for p, b in files.items()} ==
                {p: v["sha256"] for p, v in row["outputs"].items()}, "Extracted inventory differs")
        previous = ROOT / ("dist/claude" if target == "claude" else f"dist/{target}/kiyo-axiom-framework")
        require(files == verify.collect(previous), "Existing generated distribution drift")
        for p, provenance in row["outputs"].items():
            original = inputs[provenance["source"]]
            if provenance["transform"] == "byte-copy":
                require(files[p] == original, "Canonical/overlay copy drift")
            elif p.endswith("/SKILL.md"):
                normalized = original.decode().replace("\r\n", "\n").rstrip() + "\n"
                rendered = files[p].decode()
                suffix = pack.BUILDERS[target].SUFFIX
                require(rendered.endswith(suffix), "Missing declared native suffix")
                restored = rendered[:-len(suffix)].replace("(./references/kiyo/", "(../../")
                require(restored == normalized, "Unapproved skill body transformation")
        # Copy only the standalone developer checker, never into the payload.
        checker = scratch / "standalone verifier.py"
        if not checker.exists():
            shutil.copyfile(ROOT / "tools/verify_payload.py", checker)
        command = [sys.executable, "-I", "-B", str(checker), str(extracted), target,
                   "--deny-probe", str(ROOT / "src/kiyo/KIYO.md")]
        run = subprocess.run(command, cwd=scratch, capture_output=True, text=True)
        require(run.returncode == 0, run.stderr or run.stdout)
        observed = json.loads(run.stdout)
        require(observed["payload_digest"] == row["metrics"]["payload_digest"], "Isolated digest differs")
        passed("PKG-02-" + target, observed)

    # Exact-case path lookup is independent of Windows filesystem case folding.
    sample = payloads["claude"]
    entry = "skills/init/SKILL.md"
    mutants = {}
    missing = dict(sample)
    del missing["skills/init/references/kiyo/KIYO.md"]
    mutants["missing-core"] = missing
    for label, before, after in (
        ("wrong-case", b"references/kiyo/KIYO.md", b"references/kiyo/kiyo.md"),
        ("escape", b"./references/kiyo/KIYO.md", b"../../../../outside.md"),
        ("encoded-escape", b"./references/kiyo/KIYO.md", b"%2e%2e/%2e%2e/outside.md"),
        ("absolute-developer-path", b"./references/kiyo/KIYO.md", b"C:/Users/SYNTHETIC/cache/KIYO.md"),
        ("unsupported-frontmatter", b"name: init", b"name: ninth"),
    ):
        changed = dict(sample)
        require(before in changed[entry], "Mutant source not found")
        changed[entry] = changed[entry].replace(before, after, 1)
        mutants[label] = changed
    for label, path in (("runtime", "run.py"), ("project-memory", ".kiyo/memory/project.md"),
                        ("build-log", "build.log"), ("fixture", "tests/fixture.md"),
                        ("credentials", ".env")):
        changed = dict(sample)
        changed[path] = b"SYNTHETIC EXCLUDED CONTENT"
        mutants[label] = changed
    changed = dict(sample)
    changed["skills/review/references/kiyo/KIYO.md"] += b"\nSYNTHETIC DRIFT\n"
    mutants["shared-drift"] = changed
    passed("PKG-03", [rejects(lambda f=f: verify.validate(f, "claude"), label)
                      for label, f in mutants.items()])

    endings = {}
    for target, files in payloads.items():
        for ending in ("LF", "CRLF"):
            variant = {p: b.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n" if ending == "CRLF" else b"\n")
                       if p.endswith(".md") else b for p, b in files.items()}
            path = safe_extract(pack.archive_bytes(variant), scratch / f"{target} {ending} extraction")
            command = [sys.executable, "-I", "-B", str(checker), str(path), target,
                       "--deny-probe", str(ROOT / "src/kiyo/KIYO.md")]
            run = subprocess.run(command, cwd=scratch, capture_output=True, text=True)
            require(run.returncode == 0, run.stderr or run.stdout)
            endings[target + "-" + ending] = json.loads(run.stdout)["local_links"]
    passed("PKG-04", endings)

    unsafe = []
    for label, filename, mode in (
        ("zip-traversal", "kiyo-axiom-framework/../../outside.md", 0o100644),
        ("zip-absolute", "/outside.md", 0o100644),
        ("zip-symlink", "kiyo-axiom-framework/link.md", 0o120777),
    ):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w") as z:
            item = zipfile.ZipInfo(filename)
            item.create_system = 3
            item.external_attr = mode << 16
            z.writestr(item, b"../../outside")
        unsafe.append(rejects(lambda: safe_extract(stream.getvalue(), scratch / label), label))
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w") as z:
        for name in ("kiyo-axiom-framework/A.md", "kiyo-axiom-framework/a.md"):
            item = zipfile.ZipInfo(name)
            item.external_attr = 0o100644 << 16
            z.writestr(item, b"SYNTHETIC")
    unsafe.append(rejects(lambda: safe_extract(stream.getvalue(), scratch / "zip-case"), "zip-case-collision"))
    passed("PKG-05", unsafe)

    # Synthetic source snapshot: actual secrets/memory are never read.
    fixture = scratch / "synthetic source"
    for p, b in {**inputs, pack.CATALOG: (ROOT / pack.CATALOG).read_bytes()}.items():
        file = fixture / p
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(b)
    for p in (".git/config", ".env", "credentials/key.txt", ".kiyo/memory/index.md",
              "private/notes.md", "build.log", "tests/fixture.md", "tools/generator.py",
              "node_modules/example.js"):
        file = fixture / p
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(b"SYNTHETIC EXCLUSION CANARY")
    archives, fixture_record = pack.assemble(fixture)
    require(archives == {p.name: p.read_bytes() for p in runs[0].iterdir()},
            "Excluded files affected output")
    (fixture / "src/kiyo/framework/private.md").write_bytes(b"SYNTHETIC UNREVIEWED")
    rejected = rejects(lambda: pack.assemble(fixture), "unknown-product-file")
    passed("PKG-06", {"excluded_canaries": 9, "output_unchanged": True, "unreviewed_file": rejected})

    # No-op output and refusal preserve human-edited outputs and unrelated user state.
    state = scratch / "user repository"
    for p in ("CLAUDE.md", "AGENTS.md", ".github/copilot-instructions.md",
              ".kiyo/memory/index.md", ".kiyo/policy.md"):
        file = state / p
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(b"SYNTHETIC HUMAN STATE\r\n")
    state_before = snapshot(state)
    before = snapshot(runs[0])
    require(write_new_or_identical(runs[0], archives) is False, "Identical build was not no-op")
    require(snapshot(runs[0]) == before, "No-op changed timestamps")
    changed_archive = dict(archives)
    changed_archive[next(iter(changed_archive))] += b"SYNTHETIC CHANGE"
    rejects(lambda: write_new_or_identical(runs[0], changed_archive), "existing-output-differs")
    require(snapshot(runs[0]) == before and snapshot(state) == state_before, "Existing state changed")
    passed("PKG-07", {"no_op": True, "timestamp_preserved": True, "overwrite_refused": True,
                      "user_state_unchanged": True, "native_update_uninstall": "NOT_RUN"})

    # Reparse behavior uses a real link if OS policy allows creation. ZIP links tested above.
    source = scratch / "symlink source"
    source.write_bytes(b"SYNTHETIC")
    link = scratch / "source symlink"
    try:
        link.symlink_to(source)
    except OSError as error:
        checks.append({"id": "PKG-08", "status": "BLOCKED",
                       "observed": {"reason": "OS denied local symlink creation",
                                    "winerror": getattr(error, "winerror", None)},
                       "limitation": "ZIP symlink rejection passed; real filesystem link test unavailable"})
    else:
        rejects(lambda: pack.reject_links(link), "source-symlink")
        passed("PKG-08", "Real filesystem source symlink rejected")

    # Check actual stored metadata, control inventory, templates and legal continuity.
    control_text = inputs["src/kiyo/framework/control-index.md"].decode()
    control_ids = __import__("re").findall(r"^\| (KIYO-[A-Z]+-\d{3}) \|", control_text, __import__("re").M)
    require(len(set(control_ids)) == len(control_ids) == 68, "Control inventory changed; review coverage")
    templates = [p for p in inputs if p.startswith("src/kiyo/templates/")]
    for data in archives.values():
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            require(all(i.date_time == (1980, 1, 1, 0, 0, 0) and i.compress_type == zipfile.ZIP_STORED
                        and i.external_attr >> 16 == 0o100644 for i in z.infolist()), "ZIP metadata drift")
    passed("PKG-09", {"controls": len(control_ids), "canonical_files": sum(p.startswith("src/kiyo/") for p in inputs),
                      "templates": len(templates), "public_skills_per_package": 8,
                      "archive_epoch": "fixed serialization value; not build date"})
    report = {"format": "kiyo-packaging-tests-1", "checked_at_utc": datetime.now(timezone.utc).isoformat(),
              "python": platform.python_version(), "os": platform.platform(),
              "source_git_head": record["source_git_head"],
              "tooling_sha256": {**record["tooling_sha256"],
                                "tools/verify_payload.py": sha((ROOT / "tools/verify_payload.py").read_bytes()),
                                "tests/packaging/test_distributions.py": sha(Path(__file__).read_bytes())},
              "checks": checks,
              "archives": {t: {k: v for k, v in row.items() if k != "outputs"}
                           for t, row in record["packages"].items()},
              "limitations": [
                  "Offline developer checks only; no native client or agent behavior was executed.",
                  "Audit hook restricts this cooperative verifier, not an OS sandbox or Kiyo enforcement.",
                  "Exact-case ZIP/resolver tests ran on Windows; native POSIX host execution NOT_RUN.",
                  "LF/CRLF variants test reference semantics; differing input bytes produce different digests.",
                  "Unsigned development artifacts; no owner release approval, no publication."
              ]}
    pack.write_inventory(args.report.absolute(), (json.dumps(report, indent=2, sort_keys=True) + "\n").encode())
    print(json.dumps({"checks": checks, "report": args.report.as_posix()}, indent=2))


if __name__ == "__main__":
    main()
