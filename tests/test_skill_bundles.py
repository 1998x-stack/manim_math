"""Regression tests for independently runnable, stdlib-only skill bundles."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills/source"
AGENTS = (".codex", ".opencode", ".claude")
SCRIPTS = {
    "prompt-to-scene": "extract_problem.py",
    "math-specification": "check_contract.py",
    "manim-scene": "discover_scene.py",
    "geometry-precision": "check_triangle.py",
    "chinese-vertical-layout": "scan_mathtex.py",
    "catalog-and-taxonomy": "check_catalog.py",
    "render-and-publish": "check_manifest.py",
    "safe-repository-migration": "check_moves.py",
}


class SkillBundles(unittest.TestCase):
    def run_script(self, skill, *args):
        return subprocess.run([sys.executable, str(SOURCE / skill / "scripts" / SCRIPTS[skill]), *map(str, args)], cwd=ROOT, text=True, capture_output=True, check=False)

    def test_complete_mirrors_and_local_navigation(self):
        for skill, script in SCRIPTS.items():
            base = SOURCE / skill
            manifest = (base / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn(f"name: {skill}\n", manifest)
            self.assertIn("description:", manifest)
            self.assertIn(f"scripts/{script}", manifest)
            self.assertTrue(list((base / "references").glob("*.md")))
            self.assertEqual(self.run_script(skill, "--help").returncode, 0)
            for agent in AGENTS:
                for path in base.rglob("*"):
                    if path.is_file():
                        self.assertEqual(path.read_bytes(), (ROOT / agent / "skills" / skill / path.relative_to(base)).read_bytes())

    def test_prompt_extraction_is_data_only(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "prompt.md"
            path.write_text('<problem>{"知识点":"数一数"}</problem>', encoding="utf-8")
            result = self.run_script("prompt-to-scene", path)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["problem"]["知识点"], "数一数")
            path.write_text('<problem>{"a":1}</problem><problem>{"a":2}</problem>', encoding="utf-8")
            self.assertEqual(self.run_script("prompt-to-scene", path).returncode, 1)

    def test_math_contract_needs_explicit_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "math.json"
            data = {"claim": "a=a", "domain": "real a", "givens": [], "derivation": [], "counterexamples": [], "tests": [], "proof_status": "verified_by_proof", "evidence": []}
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertEqual(self.run_script("math-specification", path).returncode, 1)
            data["evidence"] = ["identity"]
            path.write_text(json.dumps(data), encoding="utf-8")
            self.assertEqual(self.run_script("math-specification", path).returncode, 0)

    def test_scene_ignores_helper_and_flags_multiple(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "scene.py"
            path.write_text('from manim import Scene\nclass Helper: pass\nclass Lesson(Scene): pass\n', encoding="utf-8")
            result = self.run_script("manim-scene", path)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["candidates"], ["Lesson"])
            path.write_text('from manim import Scene\nclass One(Scene): pass\nclass Two(Scene): pass\n', encoding="utf-8")
            self.assertEqual(json.loads(self.run_script("manim-scene", path).stdout)["status"], "needs_review")

    def test_geometry_collinear_rejected(self):
        result = self.run_script("geometry-precision", "--points", "0,0;4,0;0,3")
        self.assertEqual(result.returncode, 0, result.stderr)
        ox, oy = json.loads(result.stdout)["circumcenter"]
        self.assertAlmostEqual(ox, 2)
        self.assertAlmostEqual(oy, 1.5)
        self.assertEqual(self.run_script("geometry-precision", "--points", "0,0;1,1;2,2").returncode, 1)

    def test_formula_literal_scan(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "scene.py"
            path.write_text('x = MathTex("中文")\n', encoding="utf-8")
            self.assertEqual(self.run_script("chinese-vertical-layout", path).returncode, 1)
            path.write_text('x = MathTex(r"a^2+b^2=c^2")\n', encoding="utf-8")
            self.assertEqual(self.run_script("chinese-vertical-layout", path).returncode, 0)

    def test_catalog_duplicate_and_manifest_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            catalog = Path(directory) / "catalog.json"
            topic = {"id": "x", "number": "1", "name": "topic", "docstring": "", "pyFile": "x.py", "videoFile": None, "hasVideo": False}
            data = {"levels": [{"grades": [{"semesters": [{"chapters": [{"topics": [topic]}]}]}]}]}
            catalog.write_text(json.dumps(data), encoding="utf-8")
            self.assertEqual(self.run_script("catalog-and-taxonomy", catalog).returncode, 0)
            data["levels"][0]["grades"][0]["semesters"][0]["chapters"][0]["topics"].append(dict(topic))
            catalog.write_text(json.dumps(data), encoding="utf-8")
            self.assertEqual(self.run_script("catalog-and-taxonomy", catalog).returncode, 1)
            manifest = Path(directory) / "media.json"
            manifest.write_text(json.dumps({"scene_id": "s", "source_video": "one.mp4", "final_video": "one.mp4", "license_status": "unknown", "render_status": "not_run", "visual_status": "not_run"}), encoding="utf-8")
            self.assertEqual(self.run_script("render-and-publish", manifest).returncode, 1)

    def test_migration_rejects_traversal_and_existing_target(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "old.md").write_text("original", encoding="utf-8")
            (root / "dest.md").write_text("destination", encoding="utf-8")
            plan = root / "moves.json"
            plan.write_text(json.dumps({"moves": [{"from": "old.md", "to": "../escape.md"}]}), encoding="utf-8")
            self.assertEqual(self.run_script("safe-repository-migration", plan, "--root", root).returncode, 1)
            plan.write_text(json.dumps({"moves": [{"from": "old.md", "to": "dest.md"}]}), encoding="utf-8")
            self.assertEqual(self.run_script("safe-repository-migration", plan, "--root", root).returncode, 1)


if __name__ == "__main__":
    unittest.main()
