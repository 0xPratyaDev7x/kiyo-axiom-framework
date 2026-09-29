"""Developer-only checks for the Codex IDE standalone-skill package; no host execution."""
from pathlib import Path
import sys
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import package_codex as codex  # noqa: E402
import package_codex_ide as ide  # noqa: E402
from package_claude import SKILLS  # noqa: E402


class CodexIdePackage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload, cls.provenance, cls.metrics = ide.make_payload(ROOT)
        cls.cli, _, _ = codex.make_payload(ROOT)

    def test_deterministic(self):
        self.assertEqual(ide.make_payload(ROOT)[0], self.payload)

    def test_standalone_layout_without_plugin_manifest(self):
        self.assertEqual(self.metrics["skills"], 8)
        roots = {p.split("/")[0] for p in self.payload}
        self.assertEqual(roots, {".agents", "LICENSE"})
        for skill in SKILLS:
            entry = self.payload[f".agents/skills/kiyo-{skill}/SKILL.md"].decode()
            self.assertTrue(entry.startswith(f"---\nname: kiyo-{skill}\ndescription: "))

    def test_content_matches_cli_except_name_and_adapter(self):
        adapter = (ROOT / ide.ADAPTER).read_bytes()
        for path, data in self.payload.items():
            if path == "LICENSE":
                self.assertEqual(data, self.cli["LICENSE"])
                continue
            skill, rest = path[len(".agents/skills/kiyo-"):].split("/", 1)
            original = self.cli[f"skills/{skill}/{rest}"]
            if rest == "references/codex/activation.md":
                self.assertEqual(data, adapter)
            elif rest == "SKILL.md":
                self.assertEqual(data.replace(f"name: kiyo-{skill}\n".encode(), f"name: {skill}\n".encode(), 1),
                                 original)
            else:
                self.assertEqual(data, original)
        self.assertEqual(len(self.payload), len(self.cli) - 2)

    def test_committed_dist_matches_build(self):
        dist = ROOT / "dist/codex-ide"
        lf = lambda data: data.replace(b"\r\n", b"\n")  # Checkout line endings are not content.
        on_disk = {p.relative_to(dist).as_posix(): lf(p.read_bytes()) for p in dist.rglob("*") if p.is_file()}
        self.assertEqual(on_disk, {p: lf(b) for p, b in self.payload.items()},
                         "Rebuild with python -B tools/package_codex_ide.py")


if __name__ == "__main__":
    unittest.main()
