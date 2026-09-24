"""高一上 005 的独立数学验证；不导入 Manim。"""
import runpy
import unittest
from pathlib import Path

LESSON_TEST = (Path(__file__).resolve().parents[1]
               / "高中/高一/第一学期/第一章-集合与命题"
               / "005充分条件与必要条件/verify_conditions_scene.py")


class Grade10ConditionsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.checks = runpy.run_path(str(LESSON_TEST), run_name="__lesson_ci__")

    def test_implication_and_equivalence_boundaries(self):
        self.checks["test_math"]()

    def test_venn_geometry_and_scene_contract(self):
        self.checks["test_geometry_and_scene"]()


if __name__ == "__main__":
    unittest.main()
