"""Developer-only standalone payload closure verifier; imports no repository modules."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import posixpath
import re
import sys
from urllib.parse import unquote

SKILLS = ("init", "requirement", "implement", "review", "test", "security", "architecture", "memory", "performance")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def no_links(path):
    for p in (path, *path.parents):
        if p.exists() or p.is_symlink():
            require(not p.is_symlink() and not (getattr(p.lstat(), "st_file_attributes", 0) & 1024),
                    "Symlink/reparse point forbidden")


def collect(root):
    no_links(root)
    files = {}
    for p in root.rglob("*"):
        no_links(p)
        if p.is_file():
            files[p.relative_to(root).as_posix()] = p.read_bytes()
    return files


def validate(files, target):
    require(target in ("claude", "codex", "copilot"), "Unknown target")
    native = {"claude": {".claude-plugin/plugin.json"},
              "codex": {"plugin.json", ".codex-plugin/plugin.json"},
              "copilot": {"plugin.json"}}[target]
    require(len({p.casefold() for p in files}) == len(files), "Case collision")
    for p in files:
        parts = p.split("/")
        require(not p.startswith("/") and all(x not in ("", ".", "..") for x in parts)
                and "\\" not in p and ":" not in p, "Unsafe payload path")
        require(p in native | {"LICENSE"} or re.fullmatch(
            r"skills/(" + "|".join(SKILLS) + r")/(SKILL\.md|references/(kiyo/.+\.md|"
            + target + r"/activation\.md))", p), "Non-allowlisted payload component: " + p)
    require(native | {"LICENSE"} <= set(files), "Missing native/legal file")
    entries = {p.split("/")[1] for p in files if re.fullmatch(r"skills/[^/]+/SKILL.md", p)}
    require(entries == set(SKILLS), "Expected nine public skills")
    reference = {p.removeprefix("skills/init/references/kiyo/"): b for p, b in files.items()
                 if p.startswith("skills/init/references/kiyo/")}
    require(bool(reference) and "KIYO.md" in reference and "framework/bootstrap.md" in reference,
            "Missing shared Core")
    for skill in SKILLS:
        entry = files[f"skills/{skill}/SKILL.md"].decode().replace("\r\n", "\n")
        require(re.match(r"^---\nname: " + skill + r"\ndescription: [^\n]+\n---\n", entry),
                "Unexpected entry metadata")
        require(len(entry.splitlines()) <= 250 and len(entry.split()) <= 1200, "Entry budget")
        prefix = f"skills/{skill}/references/kiyo/"
        require({p[len(prefix):]: b for p, b in files.items() if p.startswith(prefix)} == reference,
                "Shared copies differ")
        require(files.get(f"skills/{skill}/references/{target}/activation.md") ==
                files.get(f"skills/init/references/{target}/activation.md") is not None,
                "Missing/different native adapter")
    texts, anchors = {}, {}
    for p, data in files.items():
        if not p.endswith(".md"):
            continue
        text = data.decode("utf-8").replace("\r\n", "\n")
        require(not re.search(r"(?<![A-Za-z0-9])[A-Za-z]:[/\\]|file://|/Users/|/home/|~[/\\]", text),
                "Absolute developer/home path")
        texts[p] = text
        anchors[p] = {re.sub(r"[^\w\- ]", "", re.sub(r"<[^>]+>", "", m[1]).strip().lower()).replace(" ", "-")
                      for m in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.M)}
    count = 0
    for p, text in texts.items():
        scope = "/".join(p.split("/")[:2]) + "/"
        body = re.sub(chr(96) * 3 + r"[\s\S]*?" + chr(96) * 3, "", text)
        # Current product convention is inline Markdown links, not runtime imports/HTML.
        require(not re.search(r"(?m)^\s*\[[^\]]+\]:\s*\S|<\s*(?:img|a)\s+[^>]*\b(?:href|src)\s*=", body),
                "Unsupported resource syntax; extend explicit review before packaging")
        for link in LINK.finditer(body):
            dest = unquote(link[1].strip().strip("<>"))
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", dest):
                require(dest.startswith("https://"), "Unexpected scheme")
                continue
            require(not dest.startswith(("/", "\\")) and "\\" not in dest, "Absolute resource")
            filename, _, anchor = dest.partition("#")
            resource = posixpath.normpath(posixpath.join(posixpath.dirname(p), filename)) if filename else p
            require(resource.startswith(scope) and resource in files,
                    "Missing/escaping/case-mismatched resource: " + p + " -> " + dest)
            require(not anchor or anchor in anchors.get(resource, set()), "Missing anchor")
            count += 1
    core = reference["KIYO.md"].decode() + reference["framework/bootstrap.md"].decode()
    require(len(core.splitlines()) <= 120 and len(core.split()) <= 600, "Bootstrap budget")
    inventory = {p: digest(b) for p, b in sorted(files.items())}
    return {"result": "PASS", "files": len(files), "skills": len(entries),
            "shared_per_skill": len(reference), "local_links": count,
            "payload_digest": digest("\n".join(p + " " + h for p, h in inventory.items()).encode())}


def restrict_reads(root):
    # A test-process assertion, NOT an OS sandbox or a security boundary for hostile code.
    # Imports above are complete. During inspection all audited content/directory reads
    # must be under the extracted root. No source modules are imported.
    def audit(event, args):
        if event in ("open", "os.listdir", "os.scandir"):
            p = args[0]
            if not isinstance(p, (str, bytes, os.PathLike)):
                raise PermissionError("Non-path read denied by isolation test")
            path = Path(os.fsdecode(p)).absolute()
            if not path.is_relative_to(root) or ".." in path.parts:
                raise PermissionError("Outside-payload read denied by isolation test")
        if event in ("socket.connect", "subprocess.Popen", "os.system"):
            raise PermissionError("External effect denied by isolation test")
    sys.addaudithook(audit)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("payload", type=Path)
    parser.add_argument("target", choices=("claude", "codex", "copilot"))
    parser.add_argument("--deny-probe", type=Path, required=True)
    args = parser.parse_args()
    root = args.payload.resolve()
    probe = args.deny_probe.absolute()
    require(not probe.is_relative_to(root), "Probe must be outside payload")
    no_links(root)
    restrict_reads(root)
    try:
        probe.read_bytes()
    except PermissionError:
        denied = True
    else:
        raise ValueError("Original source remained readable")
    result = validate(collect(root), args.target)
    result["outside_read_probe"] = "DENIED" if denied else "FAILED"
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as error:
        raise SystemExit(str(error))
