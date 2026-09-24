"""运行高一上 003 的本课独立数学和 Scene 静态回归（不导入 Manim）。"""
import runpy
import unittest
from pathlib import Path

LESSON_TEST = (Path(__file__).resolve().parents[1]
               / "高中/高一/第一学期/第一章-集合与命题"
               / "003集合的运算/verify_set_operations.py")


class Grade10SetOperationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.checks = runpy.run_path(str(LESSON_TEST), run_name="__lesson_ci__")

    def test_scene_data_and_geometry(self):
        self.checks["test_scene_model"]()

    def test_set_laws_and_boundary_cases(self):
        self.checks["test_general_laws"]()

    def test_scene_source_contract(self):
        self.checks["test_source_contract"]()


if __name__ == "__main__":
    unittest.main()
