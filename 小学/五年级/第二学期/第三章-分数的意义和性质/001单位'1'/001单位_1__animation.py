"""《单位“1”》的历史 Manim 场景入口。

保留原有类名供旧命令调用；完整教学场景只在 001_单位'1'.py 中维护。
"""

from pathlib import Path
from runpy import run_path


UnitOneLesson = run_path(
    str(Path(__file__).with_name("001_单位'1'.py"))
)["UnitOneLesson"]


class Topic001单位1Animation(UnitOneLesson):
    """兼容历史渲染命令的场景，避免输出无关占位动画。"""
