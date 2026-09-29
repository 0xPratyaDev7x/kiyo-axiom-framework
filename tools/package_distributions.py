"""Developer-only deterministic archives; delegates native rendering to existing builders."""
from pathlib import Path, PurePosixPath
import argparse
import io
import json
import platform
import subprocess
import zipfile

import package_claude as claude
import package_codex as codex
import package_copilot as copilot
from package_claude import require, sha, read_input, reject_links, write_new_or_identical

BUILDERS = {"claude": claude, "codex": codex, "copilot": copilot}
CATALOG = "tools/packaging-inputs.json"
TOOLING = (CATALOG, "tools/package_distributions.py", "tools/package_claude.py",
           "tools/package_codex.py", "tools/package_copilot.py")


def inputs(root):
    catalog = json.loads(read_input(root, CATALOG))
    require(catalog["format"] == "kiyo-packaging-inputs-1", "Unknown input catalog")
    paths = catalog["sources"]
    require(paths == sorted(set(paths)), "Input allowlist must be unique and sorted")
    for p in paths:
        require(not PurePosixPath(p).is_absolute() and ".." not in p.split("/")
                and "\\" not in p and ":" not in p, "Unsafe input name")
        require(p == "LICENSE" or p.startswith("src/kiyo/") and p.endswith(".md")
                or p in {
                    "platforms/claude/.claude-plugin/plugin.json",
                    "platforms/codex/plugin.json", "platforms/copilot/plugin.json",
                    *[f"platforms/{t}/resources/activation.md" for t in BUILDERS]},
                f"Non-product input: {p}")
    # Enumerate names before reading any new product file; fail closed on unknown content.
    observed = set()
    for folder in (*claude.SHARED, "skills"):
        tree = root / "src/kiyo" / folder
        reject_links(tree)
        for p in tree.rglob("*"):
            reject_links(p)
            if p.is_file():
                observed.add(p.relative_to(root).as_posix())
    observed.add("src/kiyo/KIYO.md")
    require(observed == {p for p in paths if p.startswith("src/kiyo/")},
            "Product tree differs from reviewed input allowlist")
    return {p: read_input(root, p) for p in paths}


def archive_bytes(payload):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
        for path, data in sorted(payload.items()):
            # Fixed ZIP epoch is serialization metadata, NOT an observed build date.
            item = zipfile.ZipInfo("kiyo-compass/" + path, (1980, 1, 1, 0, 0, 0))
            item.create_system = 3
            item.external_attr = 0o100644 << 16
            item.compress_type = zipfile.ZIP_STORED
            archive.writestr(item, data)
    return stream.getvalue()


def parity_rows(source, records):
    import posixpath
    import re
    controls = re.findall(r"^\| (KIYO-[A-Z]+-\d{3}) \| \[[^\]]+\]\(([^)]+)\)",
                          source["src/kiyo/framework/control-index.md"].decode(), re.M)
    require(len(controls) == len({c[0] for c in controls}) == 68, "Review changed control inventory")
    definitions = [(key, posixpath.normpath("src/kiyo/framework/" + path.split("#")[0])
                    + ("#" + path.split("#", 1)[1] if "#" in path else "")) for key, path in controls]
    definitions += [("kiyo." + skill, f"src/kiyo/skills/{skill}/SKILL.md") for skill in claude.SKILLS]
    targets = {
        "claude-cli": ("claude", "Native discovery, file reads and host permissions", "Live loading/lifecycle NOT_TESTED"),
        "claude-vscode": ("claude", "Active Claude extension/workspace, file reads and host permissions", "Independent IDE loading NOT_TESTED"),
        "codex-cli": ("codex", "Native CLI discovery, AGENTS scope, file reads and host permissions", "Exact selector UNKNOWN; ingestion FAIL for owner fields; live NOT_TESTED"),
        "codex-ide": ("codex", "No selected native plugin route", "UNSUPPORTED native plugins; DEC-004; CLI content is not IDE support"),
        "copilot-cli": ("copilot", "Native CLI discovery, file reads and host permissions", "Exact selector/collisions UNKNOWN; live NOT_TESTED"),
        "copilot-vscode": ("copilot", "Active harness/extension, discovery settings, file reads and host permissions", "Independent loading/lifecycle NOT_TESTED"),
    }
    rows = []
    for target, (artifact, dependency, gap) in targets.items():
        outputs = records[artifact]["outputs"]
        for key, canonical in definitions:
            path = canonical.split("#")[0]
            represented = [p for p, row in outputs.items() if row["source"] == path]
            require(len(represented) == (1 if key.startswith("kiyo.") else 8),
                    "Control/skill missing from adapter: " + canonical)
            rows.append({
                "target": target, "control_or_skill": key, "canonical_rule": canonical,
                "adapter_representation": {"artifact": artifact, "paths": represented},
                "activation_requirement": "activation-matrix.md target " + target + "; "
                    + ("native route unsupported" if target == "codex-ide" else "E; P only for separately authorized project guidance"),
                "static_evidence": {"status": "PASS", "scope": "Candidate artifact content only",
                                    "canonical_sha256": sha(source[path]),
                                    "output_sha256": {p: outputs[p]["sha256"] for p in represented}},
                "behavioral_evidence": "NOT_RUN for packaged host behavior",
                "host_dependency": dependency, "gap": gap,
            })
    return rows


def assemble(root):
    before = inputs(root)
    archives, records = {}, {}
    for target, builder in BUILDERS.items():
        payload, provenance, metrics = builder.make_payload(root)
        expected_sources = {p for p in before if not p.startswith("platforms/")
                            or p.startswith(f"platforms/{target}/")}
        require({v["source"] for v in provenance.values()} == expected_sources,
                f"Input coverage differs: {target}")
        for dest, row in provenance.items():
            require(row["source_sha256"] == sha(before[row["source"]]),
                    f"Input changed during rendering: {dest}")
            require(row["sha256"] == sha(payload[dest]), f"Output hash mismatch: {dest}")
            if row["transform"] == "byte-copy":
                require(payload[dest] == before[row["source"]], f"Copy differs: {dest}")
        filename = f"kiyo-compass-{target}-development.zip"
        archives[filename] = archive_bytes(payload)
        records[target] = {"archive": filename, "archive_sha256": sha(archives[filename]),
                           "archive_bytes": len(archives[filename]), "metrics": metrics,
                           "outputs": provenance}
    require(inputs(root) == before, "Inputs changed during build; discard candidate output")
    return archives, {"format": "kiyo-distribution-inventory-1",
                      "artifact_status": "DEVELOPMENT_UNRELEASED",
                      "inputs": {p: sha(b) for p, b in before.items()},
                      "packages": records, "parity": parity_rows(before, records)}


def write_inventory(path, encoded):
    reject_links(path)
    if path.exists():
        require(path.read_bytes() == encoded, "Existing inventory differs; choose a new path")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(encoded)


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=root / "dist/archives")
    parser.add_argument("--inventory", type=Path,
                        default=root / "docs/evidence/packaging/artifact-inventory.json")
    args = parser.parse_args()
    output, inventory = args.output.absolute(), args.inventory.absolute()
    reject_links(output)
    reject_links(inventory)
    for tree in ("src", "platforms", "tools", "tests"):
        require(not output.resolve().is_relative_to((root / tree).resolve()),
                "Archive output must not be inside authored inputs/tools/tests")
    require(not inventory.resolve().is_relative_to(output.resolve()), "Inventory belongs outside archives")
    archives, record = assemble(root)
    cmd = ["git", "-c", "safe.directory=" + root.as_posix(), "-c", "core.excludesFile=",
           "-C", str(root), "rev-parse", "HEAD"]
    record.update(source_git_head=subprocess.run(cmd, capture_output=True, text=True,
                                                check=True).stdout.strip(),
                  revision_scope="Base commit only; worktree input hashes are authoritative for these artifacts.",
                  python=platform.python_version(),
                  tooling_sha256={p: sha(read_input(root, p)) for p in TOOLING})
    encoded = (json.dumps(record, indent=2, sort_keys=True) + "\n").encode()
    if inventory.exists():
        require(inventory.read_bytes() == encoded, "Existing inventory differs; choose a new path")
    created = write_new_or_identical(output, archives)
    write_inventory(inventory, encoded)
    print(json.dumps({"result": "PASS", "output_created": created,
                      "packages": {t: {k: v for k, v in row.items() if k != "outputs"}
                                   for t, row in record["packages"].items()}}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error))
