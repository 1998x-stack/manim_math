"""高一上 004：仅验证逻辑/源码，无 Manim 图像依赖。"""
import runpy
import unittest
from pathlib import Path

LESSON_TEST = (Path(__file__).resolve().parents[1]
               / "高中/高一/第一学期/第一章-集合与命题"
               / "004四种命题及其关系/verify_four_propositions.py")


class Grade10FourPropositionsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.checks = runpy.run_path(str(LESSON_TEST), run_name="__lesson_ci__")

    def test_truth_table_and_counterexample(self):
        self.checks["test_logic"]()

    def test_scene_formula_and_structure(self):
        self.checks["test_source_contract"]()


if __name__ == "__main__":
    unittest.main()
