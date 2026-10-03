"""Offline portability checks for the new public Performance skill on every target."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tests/static"))
import contracts  # noqa: E402
import package_distributions as pack  # noqa: E402
import package_codex_ide as ide  # noqa: E402


class PerformancePackage(unittest.TestCase):
    def test_performance_is_portable_with_its_resources_on_every_target(self):
        source = (ROOT / "src/kiyo/skills/performance/SKILL.md").read_text(encoding="utf-8")
        for target, builder in {**pack.BUILDERS, "codex-ide": ide}.items():
            with self.subTest(target=target):
                payload, _, metrics = builder.make_payload(ROOT)
                prefix = ".agents/skills/kiyo-performance/" if target == "codex-ide" else "skills/performance/"
                entry = payload[prefix + "SKILL.md"].decode()
                name = "kiyo-performance" if target == "codex-ide" else "performance"
                self.assertEqual(metrics["skills"], 9)
                self.assertTrue(entry.startswith(f"---\nname: {name}\n"))
                self.assertIn("**kiyo.performance**", entry)
                self.assertEqual(contracts.frontmatter({"entry": entry.encode()}, "entry")["description"],
                                 contracts.frontmatter({"entry": source.encode()}, "entry")["description"])
                # Check the folder alone: no sibling skill or source checkout is needed.
                isolated = {p: b for p, b in payload.items() if p.startswith(prefix)}
                self.assertGreater(contracts.links(isolated, packaged=True), 0)
                for resource in ("KIYO.md", "framework/bootstrap.md", "workflows/performance.md",
                                 "templates/reports/performance-report.md"):
                    canonical = (ROOT / "src/kiyo" / resource).read_bytes()
                    self.assertEqual(isolated[prefix + "references/kiyo/" + resource], canonical)
                adapter = payload[prefix + f"references/{'codex' if target == 'codex-ide' else target}/activation.md"]
                self.assertIn(b"| kiyo.performance |", adapter)


if __name__ == "__main__":
    unittest.main()
