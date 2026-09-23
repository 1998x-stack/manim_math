"""《等式的性质》历史场景入口。

保持旧类名，复用包含天平和非零除数条件的完整课程，避免通用占位视频。
"""

from pathlib import Path
from runpy import run_path


EqualityPropertyLesson = run_path(
    str(Path(__file__).with_name("003_等式的性质.py"))
)["EqualityPropertyLesson"]


class Topic003等式的性质Animation(EqualityPropertyLesson):
    """兼容旧渲染命令；教学内容与主场景保持一致。"""
