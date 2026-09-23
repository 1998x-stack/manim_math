"""在仓库现有 unittest CI 中检查两节等面积法课程，无需安装 Manim。"""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "小学" / "五年级" / "第一学期" / "第五章-几何小实践"
LESSONS = ("005等面积法-同底等高", "006等面积法-梯形蝴蝶模型")


class PrimaryEqualAreaLessonTests(unittest.TestCase):
    def test_lesson_math_regressions(self):
        for lesson in LESSONS:
            with self.subTest(lesson=lesson):
                directory = CHAPTER / lesson
                result = subprocess.run(
                    [sys.executable, "-m", "unittest", "discover", "-s", str(directory),
                     "-p", "test_area_model.py", "-v"],
                    cwd=ROOT, capture_output=True, text=True, check=False,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_python_syntax_without_manim_dependency(self):
        for lesson in LESSONS:
            with self.subTest(lesson=lesson):
                directory = CHAPTER / lesson
                result = subprocess.run(
                    [sys.executable, "-m", "py_compile",
                     str(directory / "lesson.py"), str(directory / "area_model.py"),
                     str(directory / "test_area_model.py")],
                    cwd=ROOT, capture_output=True, text=True, check=False,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
