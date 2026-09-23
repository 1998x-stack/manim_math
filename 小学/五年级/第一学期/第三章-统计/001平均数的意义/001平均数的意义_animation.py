"""《平均数的意义》的历史 Manim 场景入口。

保留原有类名供旧命令调用，但不再渲染与平均数无关的通用占位动画。
主课程及教学内容只在同目录的 001_平均数的意义.py 中维护。
"""

from pathlib import Path
from runpy import run_path


# 文件名不是合法的 Python 模块标识符，用文件路径加载，避免修改 sys.path。
AverageMeaningLesson = run_path(
    str(Path(__file__).with_name("001_平均数的意义.py"))
)["AverageMeaningLesson"]


class Topic001平均数的意义Animation(AverageMeaningLesson):
    """与历史命令兼容的场景类；动画实现复用主课程。"""
