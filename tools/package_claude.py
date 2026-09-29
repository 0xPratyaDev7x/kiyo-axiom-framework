"""Developer-only Claude static packager. No native execution or installation."""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import posixpath
import re
import subprocess

SKILLS = ("init", "requirement", "implement", "review", "test", "security", "architecture", "memory")
SHARED = ("framework", "governance", "agent-security", "workflows", "profiles", "templates")
SUFFIX = (
    "\n## Claude native guidance\n\n"
    "For Claude invocation or an authorized project bootstrap, read the conditional\n"
    "[Claude activation reference](./references/claude/activation.md).\n"
)
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def reject_links(path):
    for part in (path, *path.parents):
        if part.exists() or part.is_symlink():
            require(not part.is_symlink() and not (getattr(part.lstat(), "st_file_attributes", 0) & 1024),
                    f"Symlink/reparse point is not allowed: {part}")


def read_input(root, relative):
    path = root / relative
    reject_links(path)
    require(path.resolve().is_relative_to(root.resolve()) and path.is_file(),
            f"Missing or escaping input: {relative}")
    return path.read_bytes()


def make_payload(root):
    payload, provenance = {}, {}
    def add(destination, source, data=None, transform="byte-copy"):
        original = read_input(root, source)
        payload[destination] = original if data is None else data
        provenance[destination] = {"source": source, "source_sha256": sha(original),
                                   "transform": transform, "sha256": sha(payload[destination]),
                                   "bytes": len(payload[destination])}
    manifest_path = "platforms/claude/.claude-plugin/plugin.json"
    manifest = json.loads(read_input(root, manifest_path))
    require(set(manifest) == {"name", "description"}, "Unexpected manifest fields")
    require(manifest["name"] == "kiyo-axiom-framework" and isinstance(manifest["description"], str)
            and manifest["description"].strip(), "Unexpected working identity or description")
    add(".claude-plugin/plugin.json", manifest_path)
    add("LICENSE", "LICENSE")
    src = root / "src/kiyo"
    actual_skills = sorted(p.parent.name for p in (src / "skills").glob("*/SKILL.md"))
    require(actual_skills == sorted(SKILLS), "Expected exactly eight canonical skills")
    shared = [src / "KIYO.md"]
    for directory in SHARED:
        folder = src / directory
        reject_links(folder)
        require(folder.is_dir(), f"Missing shared tree: {directory}")
        for path in folder.rglob("*"):
            reject_links(path)
            if path.is_file():
                require(path.suffix == ".md", f"Non-Markdown shared input: {path}")
                shared.append(path)
    for skill in SKILLS:
        source = f"src/kiyo/skills/{skill}/SKILL.md"
        text = read_input(root, source).decode("utf-8").replace("\r\n", "\n")
        front = re.match(r"^---\nname: ([a-z-]+)\ndescription: ([^\n]+)\n---\n", text)
        require(front is not None and front[1] == skill, f"Unexpected canonical frontmatter: {skill}")
        def replace(match):
            dest = match[1]
            require(dest.startswith("../../"), f"Unexpected entry reference: {dest}")
            return match[0].replace("(" + dest + ")", "(./references/kiyo/" + dest[6:] + ")")
        rendered = LINK.sub(replace, text).rstrip() + "\n" + SUFFIX
        require(len(rendered.splitlines()) <= 250 and len(rendered.split()) <= 1200,
                f"Entry budget exceeded: {skill}")
        add(f"skills/{skill}/SKILL.md", source, rendered.encode("utf-8"),
            "entry LF normalization; local ../../ destinations -> ./references/kiyo/; conditional Claude link suffix")
        for path in sorted(shared):
            source = path.relative_to(root).as_posix()
            add(f"skills/{skill}/references/kiyo/{path.relative_to(src).as_posix()}", source)
        add(f"skills/{skill}/references/claude/activation.md", "platforms/claude/resources/activation.md")
    metrics = validate_payload(payload)
    return payload, provenance, metrics


def slug(text):
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    return re.sub(r"[^\w\- ]", "", text).replace(" ", "-")


def validate_payload(payload):
    require(set(p.split("/")[0] for p in payload) == {".claude-plugin", "skills", "LICENSE"},
            "Unexpected payload root")
    manifest = json.loads(payload[".claude-plugin/plugin.json"])
    require(set(manifest) == {"name", "description"} and manifest["name"] == "kiyo-axiom-framework",
            "Unsupported manifest mutation")
    entries = sorted(p.split("/")[1] for p in payload if re.fullmatch(r"skills/[^/]+/SKILL.md", p))
    require(entries == sorted(SKILLS), "Missing/extra entry")
    texts, anchors = {}, {}
    for path, data in payload.items():
        require(not path.startswith("/") and ".." not in Path(path).parts, "Unsafe output path")
        require(path == "LICENSE" or path == ".claude-plugin/plugin.json" or
                (path.startswith("skills/") and path.endswith(".md")), f"Prohibited component: {path}")
        if path.endswith(".md"):
            text = data.decode("utf-8").replace("\r\n", "\n")
            require(not re.search(r"[A-Z]:[/\\]|file://|/Users/|/home/|~[/\\]", text),
                    f"Absolute/home resource path: {path}")
            texts[path] = text
            anchors[path] = {slug(m[1]) for m in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.M)}
    links = 0
    for path, text in texts.items():
        scope = "/".join(path.split("/")[:2]) + "/"
        without_fences = re.sub(chr(96)*3 + r"[\s\S]*?" + chr(96)*3, "", text)
        for match in LINK.finditer(without_fences):
            dest = match[1].strip().strip("<>")
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", dest):
                require(dest.startswith("https://"), f"Unexpected resource scheme: {path}")
                continue
            file, _, anchor = dest.partition("#")
            target = posixpath.normpath(posixpath.join(posixpath.dirname(path), file)) if file else path
            require(target.startswith(scope) and target in payload,
                    f"Missing/escaping/case-mismatched reference: {path} -> {dest}")
            if anchor:
                require(anchor in anchors.get(target, set()), f"Missing anchor: {path} -> {dest}")
            links += 1
    bootstrap = texts["skills/init/references/kiyo/KIYO.md"]
    bootstrap += texts["skills/init/references/kiyo/framework/bootstrap.md"]
    require(len(bootstrap.splitlines()) <= 120 and len(bootstrap.split()) <= 600, "Bootstrap budget")
    return {"files": len(payload), "skills": len(entries), "local_links": links,
            "bytes": sum(map(len, payload.values())),
            "payload_digest": sha("\n".join(p + " " + sha(b) for p, b in sorted(payload.items())).encode())}


def write_new_or_identical(output, payload):
    output = Path(output).absolute()
    reject_links(output)
    if output.exists():
        require(output.is_dir(), f"Output is not a directory: {output}")
        existing = {}
        for path in output.rglob("*"):
            reject_links(path)
            if path.is_file():
                existing[path.relative_to(output).as_posix()] = path.read_bytes()
        if existing:
            require(existing == payload, "Existing output differs; refusing overwrite. Choose a new output.")
            return False
    output.mkdir(parents=True, exist_ok=True)
    for relative, data in sorted(payload.items()):
        path = output / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as handle:
            handle.write(data)
    return True


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=root / "dist/claude")
    parser.add_argument("--inventory", type=Path, default=root / "docs/evidence/claude/package-inventory.json")
    args = parser.parse_args()
    output = args.output.absolute()
    inventory = args.inventory.absolute()
    reject_links(output)
    reject_links(inventory)
    require(not inventory.resolve().is_relative_to(output.resolve()), "Inventory must stay outside payload")
    require(not output.resolve().is_relative_to((root / "src").resolve()), "Output cannot be source")
    require(not output.resolve().is_relative_to((root / "platforms").resolve()), "Output cannot be overlay")
    payload, provenance, metrics = make_payload(root)
    # Git revision is observed provenance, not proof that new input bytes were committed.
    command = ["git", "-c", "safe.directory=" + root.as_posix(), "-c", "core.excludesFile=", "-C", str(root)]
    git = subprocess.run(command + ["rev-parse", "HEAD"], capture_output=True, text=True, check=True)
    record = {"format": "kiyo-claude-source-inventory-1", "artifact_status": "DEVELOPMENT_UNRELEASED",
              "source_git_head": git.stdout.strip(), "revision_scope": "Base commit; input hashes describe actual worktree bytes.",
              "python": platform.python_version(), "metrics": metrics,
              "sources": sorted({row["source"] for row in provenance.values()}), "outputs": provenance}
    record_bytes = (json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if inventory.exists():
        require(inventory.read_bytes() == record_bytes, "Existing inventory differs; choose a new inventory.")
    changed = write_new_or_identical(output, payload)
    if not inventory.exists():
        inventory.parent.mkdir(parents=True, exist_ok=True)
        with inventory.open("xb") as handle:
            handle.write(record_bytes)
    print(json.dumps({"result": "PASS", "output_created": changed,
                      "shared_per_skill": len([p for p in payload if p.startswith("skills/init/references/kiyo/")]),
                      **metrics}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error))
