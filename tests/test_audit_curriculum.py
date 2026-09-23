"""No external dependencies or access to historical videos required."""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "audit_curriculum.py"
spec = importlib.util.spec_from_file_location("audit_curriculum", SCRIPT)
audit_module = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(audit_module)


class CurriculumAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.chapter = self.root / "小学" / "一年级" / "上册" / "第一章-认识数"

    def topic(self, name: str, *, problem: str = "数一数", scene: str = "class Counting(Scene):\n    def construct(self): pass\n") -> Path:
        directory = self.chapter / name
        directory.mkdir(parents=True)
        description = {"年级": "一年级", "学期": "上册", "章节": "第一章", "知识点": problem,
                       "数学公式": [], "相关知识点": [], "manim动画涉及元素": []}
        (directory / "description.json").write_text(json.dumps(description, ensure_ascii=False), encoding="utf-8")
        (directory / "prompt.md").write_text("Common instructions\n<problem>\n" + json.dumps(description, ensure_ascii=False)
                                              + "\n</problem>\nShared footer\n", encoding="utf-8")
        (directory / "storyboard.md").write_text("分镜", encoding="utf-8")
        (directory / "scene.py").write_text(scene, encoding="utf-8")
        return directory

    def test_template_reuse_does_not_erase_topic_specific_content(self):
        self.topic("001数一数")
        self.topic("002认识数字", problem="认识数字")
        result = audit_module.audit(self.root)
        self.assertEqual(result["topic_directory_count"], 2)
        self.assertEqual(len(result["shared_prompt_templates"]), 1)
        self.assertEqual(result["shared_prompt_templates"][0]["count"], 2)
        self.assertEqual(result["issue_counts"], {})
        self.assertNotEqual(result["records"][0]["prompt_sha256"], result["records"][1]["prompt_sha256"])

    def test_invalid_metadata_is_error_and_absence_is_warning(self):
        directory = self.topic("003损坏")
        (directory / "description.json").write_text("{", encoding="utf-8")
        (directory / "storyboard.md").unlink()
        result = audit_module.audit(self.root)
        self.assertEqual(result["issue_counts"]["invalid_description"], 1)
        self.assertEqual(result["issue_counts"]["missing_file"], 1)

    def test_prompt_description_mismatch_and_unparseable_problem(self):
        directory = self.topic("004不一致")
        (directory / "prompt.md").write_text('<problem>{"知识点": "其他内容"}</problem>', encoding="utf-8")
        result = audit_module.audit(self.root)
        self.assertEqual(result["issue_counts"]["prompt_description_mismatch"], 1)
        (directory / "prompt.md").write_text('<problem>{bad json}</problem>', encoding="utf-8")
        self.assertEqual(audit_module.audit(self.root)["issue_counts"]["invalid_problem_block"], 1)

    def test_scene_discovery_ignores_helper_class_and_surfaces_ambiguity(self):
        directory = self.topic("005多场景", scene="class Helper: pass\nclass A(Scene): pass\nclass B(ThreeDScene): pass\n")
        (directory / "renderA_finish.mp4").touch()
        (directory / "renderB_finish.mp4").touch()
        result = audit_module.audit(self.root)
        self.assertEqual(result["records"][0]["python_scene_candidates"], {"scene.py": ["A", "B"]})
        self.assertEqual(result["issue_counts"]["multiple_scene_candidates"], 1)
        self.assertEqual(result["issue_counts"]["multiple_final_videos"], 1)

    def test_cli_determinism_and_exit_codes(self):
        directory = self.topic("006未完成")
        self.assertEqual(audit_module.audit(self.root), audit_module.audit(self.root))
        self.assertEqual(audit_module.main(["--root", str(self.root), "--output", str(self.root / "report.json")]), 0)
        self.assertTrue((self.root / "report.json").is_file())
        (directory / "storyboard.md").unlink()
        self.assertEqual(audit_module.main(["--root", str(self.root), "--output", str(self.root / "report.json"), "--fail-on", "warning"]), 1)
        self.assertEqual(audit_module.main(["--root", str(self.root), "--output", str(self.root / "report.json"), "--fail-on", "error"]), 0)


if __name__ == "__main__":
    unittest.main()
