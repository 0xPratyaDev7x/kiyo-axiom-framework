"""Developer-only Copilot static packager; no install or consumer runtime."""
from pathlib import Path
import argparse
import json
import platform
import posixpath
import re
import subprocess
import sys

sys.dont_write_bytecode = True
# Only common file/hash helpers; no Claude manifest or payload construction.
from package_claude import (
    SKILLS, SHARED, LINK, require, sha, reject_links, read_input,
    write_new_or_identical, slug,
)

SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
SUFFIX = (
    "\n## Copilot native guidance\n\n"
    "For Copilot invocation or an authorized project bootstrap, read the conditional\n"
    "[Copilot activation reference](./references/copilot/activation.md).\n"
)


def validate_manifest(manifest):
    # CP22-01/07/10 establish this closed, skills-only subset for both targets.
    # This local subset check is not a host parser or a full operational validator.
    require(isinstance(manifest, dict) and set(manifest) == {"$schema", "name", "description"},
            "Unexpected portable manifest fields")
    require(manifest["$schema"] == SCHEMA, "Unsupported selected schema")
    name = manifest["name"]
    require(isinstance(name, str) and 1 <= len(name) <= 64
            and re.fullmatch(r"(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?", name),
            "Invalid portable name")
    require(name == "kiyo-compass", "Unexpected working identity")
    require(isinstance(manifest["description"], str) and manifest["description"].strip(),
            "Missing development description")


def make_payload(root):
    payload, provenance = {}, {}
    def add(destination, source, data=None, transform="byte-copy"):
        original = read_input(root, source)
        require(destination not in payload, f"Duplicate destination: {destination}")
        payload[destination] = original if data is None else data
        provenance[destination] = {"source": source, "source_sha256": sha(original),
                                   "transform": transform, "sha256": sha(payload[destination]),
                                   "bytes": len(payload[destination])}
    manifest_path = "platforms/copilot/plugin.json"
    validate_manifest(json.loads(read_input(root, manifest_path)))
    add("plugin.json", manifest_path)
    add("LICENSE", "LICENSE")
    src = root / "src/kiyo"
    require(sorted(p.parent.name for p in (src / "skills").glob("*/SKILL.md")) == sorted(SKILLS),
            "Expected exactly eight canonical entries")
    shared = [src / "KIYO.md"]
    for directory in SHARED:
        folder = src / directory
        reject_links(folder)
        require(folder.is_dir(), f"Missing shared folder: {directory}")
        for path in folder.rglob("*"):
            reject_links(path)
            if path.is_file():
                require(path.suffix == ".md", f"Non-Markdown shared resource: {path}")
                shared.append(path)
    for skill in SKILLS:
        source = f"src/kiyo/skills/{skill}/SKILL.md"
        text = read_input(root, source).decode("utf-8").replace("\r\n", "\n")
        front = re.match(r"^---\nname: ([a-z-]+)\ndescription: ([^\n]+)\n---\n", text)
        require(front is not None and front[1] == skill and len(front[1]) <= 64
                and 0 < len(front[2]) <= 1024, f"Invalid name/description: {skill}")
        def replace(match):
            dest = match[1]
            require(dest.startswith("../../"), f"Unexpected entry reference: {dest}")
            return match[0].replace("(" + dest + ")", "(./references/kiyo/" + dest[6:] + ")")
        rendered = LINK.sub(replace, text).rstrip() + "\n" + SUFFIX
        require(len(rendered.splitlines()) <= 250 and len(rendered.split()) <= 1200,
                f"Entry budget exceeded: {skill}")
        add(f"skills/{skill}/SKILL.md", source, rendered.encode("utf-8"),
            "entry LF normalization; ../../ destinations -> ./references/kiyo/; conditional Copilot link suffix")
        for path in sorted(shared):
            add(f"skills/{skill}/references/kiyo/{path.relative_to(src).as_posix()}",
                path.relative_to(root).as_posix())
        add(f"skills/{skill}/references/copilot/activation.md", "platforms/copilot/resources/activation.md")
    return payload, provenance, validate_payload(payload)


def validate_payload(payload):
    require(set(p.split("/")[0] for p in payload) == {"plugin.json", "skills", "LICENSE"},
            "Unexpected payload root")
    validate_manifest(json.loads(payload["plugin.json"]))
    entries = sorted(p.split("/")[1] for p in payload if re.fullmatch(r"skills/[^/]+/SKILL.md", p))
    require(entries == sorted(SKILLS), "Missing/extra public entry")
    texts, anchors = {}, {}
    for path, data in payload.items():
        require(not path.startswith("/") and ".." not in Path(path).parts, "Unsafe output path")
        require(path in {"plugin.json", "LICENSE"} or
                (path.startswith("skills/") and path.endswith(".md")), f"Prohibited component: {path}")
        if path.endswith(".md"):
            text = data.decode("utf-8").replace("\r\n", "\n")
            require(not re.search(r"[A-Z]:[/\\]|file://|/Users/|/home/|~[/\\]", text),
                    f"Absolute/home resource locator: {path}")
            texts[path] = text
            anchors[path] = {slug(m[1]) for m in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.M)}
    links = 0
    for path, text in texts.items():
        scope = "/".join(path.split("/")[:2]) + "/"
        text = re.sub(chr(96)*3 + r"[\s\S]*?" + chr(96)*3, "", text)
        for match in LINK.finditer(text):
            dest = match[1].strip().strip("<>")
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", dest):
                require(dest.startswith("https://"), f"Unexpected resource scheme: {path}")
                continue
            file, _, anchor = dest.partition("#")
            target = posixpath.normpath(posixpath.join(posixpath.dirname(path), file)) if file else path
            require(target.startswith(scope) and target in payload, f"Missing/escaping reference: {path} -> {dest}")
            if anchor:
                require(anchor in anchors.get(target, set()), f"Missing anchor: {path} -> {dest}")
            links += 1
    bootstrap = texts["skills/init/references/kiyo/KIYO.md"] + texts["skills/init/references/kiyo/framework/bootstrap.md"]
    require(len(bootstrap.splitlines()) <= 120 and len(bootstrap.split()) <= 600, "Bootstrap budget")
    return {"files": len(payload), "skills": len(entries), "local_links": links,
            "bytes": sum(map(len, payload.values())),
            "payload_digest": sha("\n".join(p + " " + sha(b) for p, b in sorted(payload.items())).encode())}


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=root / "dist/copilot/kiyo-compass")
    parser.add_argument("--inventory", type=Path, default=root / "docs/evidence/copilot/package-inventory.json")
    args = parser.parse_args()
    output, inventory = args.output.absolute(), args.inventory.absolute()
    reject_links(output)
    reject_links(inventory)
    require(output.name == "kiyo-compass", "Outer plugin folder must match working identity")
    require(not inventory.resolve().is_relative_to(output.resolve()), "Inventory must be outside payload")
    for tree in ("src", "platforms"):
        require(not output.resolve().is_relative_to((root / tree).resolve()), "Output cannot be source/overlay")
    payload, provenance, metrics = make_payload(root)
    command = ["git", "-c", "safe.directory=" + root.as_posix(), "-c", "core.excludesFile=", "-C", str(root)]
    base = subprocess.run(command + ["rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    tooling = {p: sha(read_input(root, p)) for p in ("tools/package_copilot.py", "tools/package_claude.py")}
    record = {"format": "kiyo-copilot-source-inventory-1", "artifact_status": "DEVELOPMENT_UNRELEASED",
              "targets": ["GitHub Copilot CLI", "GitHub Copilot VS Code"],
              "source_git_head": base, "revision_scope": "Base commit; input hashes describe actual worktree bytes.",
              "python": platform.python_version(), "tooling_sha256": tooling, "metrics": metrics,
              "sources": sorted({row["source"] for row in provenance.values()}), "outputs": provenance}
    encoded = (json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if inventory.exists():
        require(inventory.read_bytes() == encoded, "Existing inventory differs; choose a new inventory.")
    changed = write_new_or_identical(output, payload)
    if not inventory.exists():
        inventory.parent.mkdir(parents=True, exist_ok=True)
        with inventory.open("xb") as handle:
            handle.write(encoded)
    print(json.dumps({"result": "PASS", "output_created": changed,
                      "shared_per_skill": len([p for p in payload if p.startswith("skills/init/references/kiyo/")]),
                      **metrics}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error))
