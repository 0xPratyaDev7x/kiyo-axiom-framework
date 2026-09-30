"""Developer-only Codex packaging from canonical content; no native execution."""
from pathlib import Path
import argparse
import json
import platform
import posixpath
import re
import subprocess
import sys

sys.dont_write_bytecode = True
# Reuse only audited filesystem/hash helpers, not Claude schema or payload creation.
from package_claude import (
    SKILLS, SHARED, LINK, require, sha, reject_links, read_input,
    write_new_or_identical, slug, require_release_metadata,
)

SUFFIX = (
    "\n## Codex native guidance\n\n"
    "For Codex invocation or an authorized project bootstrap, read the conditional\n"
    "[Codex activation reference](./references/codex/activation.md).\n"
)
SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"


def compatibility_manifest(portable):
    return {
        "name": portable["name"],
        "version": portable["version"],
        "description": portable["description"],
        "author": portable["author"],
        "skills": "./skills/",
        "interface": portable["extensions"]["com.openai"]["interface"],
    }


def validate_manifests(portable, compatibility):
    require(set(portable) == {"$schema", "name", "version", "description", "author", "extensions"},
            "Unexpected portable manifest fields")
    require_release_metadata(portable)
    require(portable["$schema"] == SCHEMA and portable["name"] == "kiyo-axiom-framework",
            "Unexpected schema or working identity")
    require(isinstance(portable["description"], str) and portable["description"].strip(),
            "Description is required for this artifact")
    require(set(portable["extensions"]) == {"com.openai"}
            and set(portable["extensions"]["com.openai"]) == {"interface"},
            "Only the OpenAI presentation extension is allowed")
    interface = portable["extensions"]["com.openai"]["interface"]
    require(set(interface) == {"displayName", "shortDescription", "longDescription",
                              "category", "capabilities", "defaultPrompt"},
            "Unexpected presentation fields")
    for field in ("displayName", "shortDescription", "longDescription", "category"):
        require(isinstance(interface[field], str) and interface[field].strip(),
                f"Invalid interface.{field}")
    require(len(interface["displayName"]) <= 30 and len(interface["shortDescription"]) <= 30,
            "Presentation text budget")
    require(interface["category"] == "Productivity" and interface["capabilities"] == [],
            "Unexpected development presentation")
    prompts = interface["defaultPrompt"]
    require(isinstance(prompts, list) and 1 <= len(prompts) <= 3
            and all(isinstance(p, str) and 0 < len(p) <= 128 and "\n" not in p for p in prompts),
            "Invalid starter prompts")
    require(compatibility == compatibility_manifest(portable),
            "Compatibility manifest diverges from portable input")
    # Submission still needs an owner-supplied interface.developerName.
    # This is a selected-field development check, not public-ingestion validation.


def make_payload(root):
    payload, provenance = {}, {}
    def add(destination, source, data=None, transform="byte-copy"):
        original = read_input(root, source)
        payload[destination] = original if data is None else data
        provenance[destination] = {"source": source, "source_sha256": sha(original),
                                   "transform": transform, "sha256": sha(payload[destination]),
                                   "bytes": len(payload[destination])}
    source_manifest = "platforms/codex/plugin.json"
    portable = json.loads(read_input(root, source_manifest))
    compatibility = compatibility_manifest(portable)
    validate_manifests(portable, compatibility)
    add("plugin.json", source_manifest)
    add(".codex-plugin/plugin.json", source_manifest,
        (json.dumps(compatibility, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
        "derive Codex compatibility identity/interface and explicit ./skills/ from portable input")
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
        require(front is not None and front[1] == skill, f"Unexpected frontmatter: {skill}")
        def replace(match):
            dest = match[1]
            require(dest.startswith("../../"), f"Unexpected entry reference: {dest}")
            return match[0].replace("(" + dest + ")", "(./references/kiyo/" + dest[6:] + ")")
        rendered = LINK.sub(replace, text).rstrip() + "\n" + SUFFIX
        require(len(rendered.splitlines()) <= 250 and len(rendered.split()) <= 1200,
                f"Entry budget exceeded: {skill}")
        add(f"skills/{skill}/SKILL.md", source, rendered.encode("utf-8"),
            "entry LF normalization; ../../ destinations -> ./references/kiyo/; conditional Codex link suffix")
        for path in sorted(shared):
            add(f"skills/{skill}/references/kiyo/{path.relative_to(src).as_posix()}",
                path.relative_to(root).as_posix())
        add(f"skills/{skill}/references/codex/activation.md", "platforms/codex/resources/activation.md")
    return payload, provenance, validate_payload(payload)


def validate_payload(payload):
    require(set(p.split("/")[0] for p in payload) == {"plugin.json", ".codex-plugin", "skills", "LICENSE"},
            "Unexpected payload root")
    validate_manifests(json.loads(payload["plugin.json"]), json.loads(payload[".codex-plugin/plugin.json"]))
    entries = sorted(p.split("/")[1] for p in payload if re.fullmatch(r"skills/[^/]+/SKILL.md", p))
    require(entries == sorted(SKILLS), "Missing/extra public entry")
    texts, anchors = {}, {}
    for path, data in payload.items():
        require(not path.startswith("/") and ".." not in Path(path).parts, "Unsafe output path")
        require(path in {"plugin.json", ".codex-plugin/plugin.json", "LICENSE"}
                or (path.startswith("skills/") and path.endswith(".md")), f"Prohibited component: {path}")
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
    parser.add_argument("--output", type=Path, default=root / "dist/codex/kiyo-axiom-framework")
    parser.add_argument("--inventory", type=Path, default=root / "docs/evidence/codex/package-inventory.json")
    args = parser.parse_args()
    output, inventory = args.output.absolute(), args.inventory.absolute()
    reject_links(output)
    reject_links(inventory)
    require(output.name == "kiyo-axiom-framework", "Outer plugin folder must match working manifest name")
    require(not inventory.resolve().is_relative_to(output.resolve()), "Inventory must be outside payload")
    for tree in ("src", "platforms"):
        require(not output.resolve().is_relative_to((root / tree).resolve()), "Output cannot be source/overlay")
    payload, provenance, metrics = make_payload(root)
    command = ["git", "-c", "safe.directory=" + root.as_posix(), "-c", "core.excludesFile=", "-C", str(root)]
    base = subprocess.run(command + ["rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    tooling = {p: sha(read_input(root, p)) for p in ("tools/package_codex.py", "tools/package_claude.py")}
    record = {"format": "kiyo-codex-source-inventory-1", "artifact_status": "DEVELOPMENT_UNRELEASED",
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
