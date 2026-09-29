"""Developer-only Codex IDE standalone-skill packaging from canonical content; no native execution."""
from pathlib import Path
import argparse
import json
import platform
import posixpath
import re
import subprocess
import sys

sys.dont_write_bytecode = True
# Reuse the audited Codex entry rendering; only location, name and adapter differ.
import package_codex as codex
from package_claude import (
    SKILLS, LINK, require, sha, reject_links, read_input, write_new_or_identical, slug,
)

PREFIX = "kiyo-"
BASE = ".agents/skills/"
ADAPTER = "platforms/codex-ide/resources/activation.md"


def make_payload(root):
    rendered, codex_provenance, _ = codex.make_payload(root)
    adapter = read_input(root, ADAPTER)
    payload, provenance = {}, {}
    for path, data in rendered.items():
        row = dict(codex_provenance[path])
        if path in {"plugin.json", ".codex-plugin/plugin.json"}:
            continue  # The IDE extension loads standalone skills only; no plugin manifest.
        if path == "LICENSE":
            payload[path], provenance[path] = data, row
            continue
        require(path.startswith("skills/"), f"Unexpected Codex output: {path}")
        skill, rest = path[len("skills/"):].split("/", 1)
        dest = f"{BASE}{PREFIX}{skill}/{rest}"
        if rest == "SKILL.md":
            text = data.decode("utf-8")
            head = f"---\nname: {skill}\n"
            require(text.startswith(head), f"Unexpected frontmatter: {skill}")
            data = (f"---\nname: {PREFIX}{skill}\n" + text[len(head):]).encode("utf-8")
            row["transform"] += f"; standalone name {PREFIX}{skill}"
        elif rest == "references/codex/activation.md":
            data = adapter
            row = {"source": ADAPTER, "source_sha256": sha(adapter), "transform": "byte-copy"}
        row.update(sha256=sha(data), bytes=len(data))
        payload[dest], provenance[dest] = data, row
    return payload, provenance, validate_payload(payload)


def validate_payload(payload):
    names = {f"{PREFIX}{s}" for s in SKILLS}
    entries = set()
    texts, anchors = {}, {}
    for path, data in payload.items():
        require(not path.startswith("/") and ".." not in Path(path).parts, "Unsafe output path")
        if path == "LICENSE":
            continue
        match = re.fullmatch(r"\.agents/skills/([a-z-]+)/(SKILL\.md|references/(kiyo/.+|codex/activation)\.md)", path)
        require(match is not None and match[1] in names, f"Prohibited component: {path}")
        text = data.decode("utf-8").replace("\r\n", "\n")
        require(not re.search(r"[A-Z]:[/\\]|file://|/Users/|/home/|~[/\\]", text),
                f"Absolute/home resource locator: {path}")
        if match[2] == "SKILL.md":
            front = re.match(r"^---\nname: ([a-z-]+)\ndescription: ([^\n]+)\n---\n", text)
            require(front is not None and front[1] == match[1], f"Name/folder mismatch: {path}")
            require(len(text.splitlines()) <= 250 and len(text.split()) <= 1200, f"Entry budget: {path}")
            entries.add(match[1])
        texts[path] = text
        anchors[path] = {slug(m[1]) for m in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.M)}
    require(entries == names and "LICENSE" in payload, "Missing/extra standalone entry")
    links = 0
    for path, text in texts.items():
        scope = "/".join(path.split("/")[:3]) + "/"
        text = re.sub(chr(96)*3 + r"[\s\S]*?" + chr(96)*3, "", text)
        for match in LINK.finditer(text):
            dest = match[1].strip().strip("<>")
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", dest):
                require(dest.startswith("https://"), f"Unexpected resource scheme: {path}")
                continue
            file, _, anchor = dest.partition("#")
            target = posixpath.normpath(posixpath.join(posixpath.dirname(path), file)) if file else path
            # Each skill folder must stay self-contained so it can be copied alone.
            require(target.startswith(scope) and target in payload, f"Missing/escaping reference: {path} -> {dest}")
            if anchor:
                require(anchor in anchors.get(target, set()), f"Missing anchor: {path} -> {dest}")
            links += 1
    return {"files": len(payload), "skills": len(entries), "local_links": links,
            "bytes": sum(map(len, payload.values())),
            "payload_digest": sha("\n".join(p + " " + sha(b) for p, b in sorted(payload.items())).encode())}


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=root / "dist/codex-ide")
    parser.add_argument("--inventory", type=Path, default=root / "docs/evidence/codex-ide/package-inventory.json")
    args = parser.parse_args()
    output, inventory = args.output.absolute(), args.inventory.absolute()
    reject_links(output)
    reject_links(inventory)
    require(not inventory.resolve().is_relative_to(output.resolve()), "Inventory must be outside payload")
    for tree in ("src", "platforms"):
        require(not output.resolve().is_relative_to((root / tree).resolve()), "Output cannot be source/overlay")
    payload, provenance, metrics = make_payload(root)
    command = ["git", "-c", "safe.directory=" + root.as_posix(), "-c", "core.excludesFile=", "-C", str(root)]
    base = subprocess.run(command + ["rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    tooling = {p: sha(read_input(root, p)) for p in
               ("tools/package_codex_ide.py", "tools/package_codex.py", "tools/package_claude.py")}
    record = {"format": "kiyo-codex-ide-source-inventory-1", "artifact_status": "DEVELOPMENT_UNRELEASED",
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
    print(json.dumps({"result": "PASS", "output_created": changed, **metrics}, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error))
