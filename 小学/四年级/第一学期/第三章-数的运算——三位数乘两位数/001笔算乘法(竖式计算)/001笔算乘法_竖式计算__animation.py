"""兼容旧场景名，复用同目录的竖式乘法教学动画。

运行：manim -pql '001笔算乘法_竖式计算__animation.py' Topic001笔算乘法竖式计算Animation
"""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


_LESSON_FILE = Path(__file__).with_name("001_笔算乘法(竖式计算).py")
_spec = spec_from_file_location("grade4_column_multiplication_lesson", _LESSON_FILE)
if _spec is None or _spec.loader is None:
    raise ImportError(f"无法加载教学场景：{_LESSON_FILE}")
_lesson = module_from_spec(_spec)
_spec.loader.exec_module(_lesson)


class Topic001笔算乘法竖式计算Animation(_lesson.ColumnMultiplicationLesson):
    """旧入口与主入口显示完全相同的竖式过程，避免两套实现漂移。"""
