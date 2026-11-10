"""Batch eight: eleven reviews resolved, ten unique Scenes, stable Gallery."""
import ast
import json
from pathlib import Path
import unittest
from assets.build_catalog import find_scene_py

ROOT = Path(__file__).resolve().parents[1]
LESSONS = json.loads(r'''{"001解决问题策略":{"topic":"小学/二年级/上册/第六章-整理与提高/001解决问题策略","keep":"001解决问题策略_animation.py","remove":"001_解决问题策略.py","scene":"Topic001解决问题策略Animation","id":"b0fc8bc977"},"001认识角":{"topic":"小学/二年级/上册/第四章-几何小实践/001认识角","keep":"001认识角_animation.py","remove":"001_认识角.py","scene":"Topic001认识角Animation","id":"cd9b10a67f"},"001东南西北":{"topic":"小学/二年级/上册/第五章-方向与位置/001东南西北","keep":"001东南西北_animation.py","remove":"001_东南西北.py","scene":"Topic001东南西北Animation","id":"9eec233a9d"},"001运算顺序":{"topic":"小学/二年级/下册/第一章-复习与提高/001运算顺序","keep":"001运算顺序_animation.py","remove":"001_运算顺序.py","scene":"Topic001运算顺序Animation","id":"07507656bc"},"001认识周长":{"topic":"小学/三年级/上册/第五章-几何小实践/001认识周长","keep":"001认识周长_animation.py","remove":"001_认识周长.py","scene":"Topic001认识周长Animation","id":"d4b142a89d"},"001复式条形统计图":{"topic":"小学/三年级/下册/第三章-统计/001复式条形统计图","keep":"001复式条形统计图_animation.py","remove":"001_复式条形统计图.py","scene":"Topic001复式条形统计图Animation","id":"d80e1f90d7"},"001单式折线统计图":{"topic":"小学/四年级/第二学期/第三章-统计/001单式折线统计图","keep":"001单式折线统计图_animation.py","remove":"001_单式折线统计图.py","scene":"Topic001单式折线统计图Animation","id":"9e41b9e477"},"002笔算除法(试商与调商)":{"topic":"小学/四年级/第一学期/第四章-数的运算——除数是两位数的除法/002笔算除法(试商与调商)","keep":"002_笔算除法.py","remove":"002_笔算除法(试商与调商).py","scene":"WrittenDivisionLesson","id":"d2811b7e28"},"001长方体":{"topic":"小学/一年级/上册/第三章-认识图形（一）/001长方体","keep":"001长方体_animation.py","remove":"001_长方体.py","scene":"Topic001长方体Animation","id":"5294b9fda1"},"001认识平面图形":{"topic":"小学/一年级/下册/第六章-几何小实践/001认识平面图形","keep":"001认识平面图形_animation.py","remove":"001_认识平面图形.py","scene":"Topic001认识平面图形Animation","id":"b4bba766e5"}}''')
ALIAS = "小学/五年级/第二学期/第三章-分数的意义和性质/001单位'1'"


def pure_math(lesson, function):
    d = LESSONS[lesson]
    path = ROOT / d["topic"] / d["keep"]
    tree = ast.parse(path.read_text(encoding="utf-8"))
    matches = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == function]
    assert len(matches) == 1
    namespace = {}
    exec(compile(ast.Module(body=matches, type_ignores=[]), str(path), "exec"), namespace)
    return namespace[function]


class BatchEightTests(unittest.TestCase):
    def test_single_scene_per_deduplicated_topic(self):
        for name, item in LESSONS.items():
            with self.subTest(name=name):
                folder = ROOT / item["topic"]
                self.assertFalse((folder / item["remove"]).exists())
                sources = [p.name for p in folder.glob("*.py")
                           if not p.name.startswith(("test_", "verify_", "__"))]
                self.assertEqual(sources, [item["keep"]])
                self.assertEqual(find_scene_py(folder), folder / item["keep"])
                content = (folder / item["keep"]).read_text(encoding="utf-8")
                self.assertNotIn("正在学习", content)
                self.assertNotIn("这是一个重要的数学概念", content)
                tree = ast.parse(content)
                scenes = [n.name for n in tree.body if isinstance(n, ast.ClassDef)
                          and any(isinstance(base, ast.Name) and base.id == "Scene" for base in n.bases)]
                self.assertEqual(scenes, [item["scene"]])

    def test_catalog_count_ids_and_video_paths(self):
        catalog = json.loads((ROOT / "assets/catalog.json").read_text(encoding="utf-8"))
        entries = [topic for level in catalog["levels"]
                   for grade in level.get("grades", [])
                   for semester in grade.get("semesters", [])
                   for chapter in semester.get("chapters", [])
                   for topic in chapter.get("topics", [])]
        self.assertEqual(len(entries), 534)
        by_id = {topic["id"]: topic for topic in entries}
        self.assertEqual(len(by_id), 534)
        for item in LESSONS.values():
            with self.subTest(id=item["id"]):
                topic = by_id[item["id"]]
                self.assertEqual(topic["pyFile"], item["topic"] + "/" + item["keep"])
                self.assertEqual(topic["videoFile"],
                                 item["topic"] + "/" + item["scene"] + "_finish.mp4")
                self.assertTrue(topic["hasVideo"])

    def test_remaining_mapping_is_reviewed_not_alternative_scenes(self):
        mapping = json.loads((ROOT / "catalog/primary-scene-overrides.json").read_text(encoding="utf-8"))
        self.assertEqual(len(mapping["topics"]), 16)
        self.assertTrue(all(t["status"] == "source-reviewed" for t in mapping["topics"]))
        alias = next(t for t in mapping["topics"] if t["topic"] == ALIAS)
        self.assertEqual(alias["scene_class"], "UnitOneLesson")
        bridge = (ROOT / ALIAS / "001单位_1__animation.py").read_text(encoding="utf-8")
        self.assertIn("run_path(", bridge)
        self.assertNotIn("def construct(", bridge)

    def test_math_models_for_rebuilt_courses(self):
        changes = pure_math("001单式折线统计图", "daily_changes")
        self.assertEqual(changes((18, 20, 19, 23, 25)), (2, -1, 4, 2))
        self.assertEqual(sum(changes((18, 20, 19, 23, 25))), 7)
        with self.assertRaises(ValueError):
            changes((18,))
        self.assertEqual(len(pure_math("001长方体", "opposite_face_pairs")()), 3)
        self.assertEqual(pure_math("001认识平面图形", "straight_side_counts")(),
                         {"长方形": 4, "正方形": 4, "三角形": 3, "圆": 0})


if __name__ == "__main__":
    unittest.main()
