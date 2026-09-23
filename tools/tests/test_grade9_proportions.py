"""九年级《比例线段》数学/源码回归；无需安装 Manim。

运行：python tools/tests/test_grade9_proportions.py
"""

import ast
import math
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE = REPO_ROOT / "初中/九年级/第一学期/第二十四章-相似三角形/001比例线段/proportional_segments.py"
TEXT = SOURCE.read_text(encoding="utf-8")
TREE = ast.parse(TEXT, filename=str(SOURCE))


def math_functions():
    """仅提取纯数学函数，不执行 Scene 或加载 Manim。"""
    functions = [node for node in TREE.body if isinstance(node, ast.FunctionDef)
                 and node.name in {"valid_proportion", "proportional_mean"}]
    assert len(functions) == 2, "纯数学函数缺失"
    namespace = {"math": math}
    module = ast.fix_missing_locations(ast.Module(body=functions, type_ignores=[]))
    exec(compile(module, str(SOURCE), "exec"), namespace)
    return namespace["valid_proportion"], namespace["proportional_mean"]


def run_checks():
    compile(TEXT, str(SOURCE), "exec")
    valid, mean = math_functions()
    assert valid(2, 3, 4, 6)
    assert valid(4, 6, 2, 3)
    assert valid(20, 30, 40, 60)
    assert not valid(2, 3, 4, 5)
    assert not valid(1, 0, 2, 3)
    assert not valid(1, 2, 3, 0)
    assert not valid(-2, 3, -4, 6)
    assert not valid(math.inf, 2, 4, 6)
    assert not valid(math.nan, 2, 4, 6)
    # 比较交叉乘积时使用固定绝对误差，会把微小但不等的比例误判为相等。
    assert not valid(1e-9, 1e-9, 2e-9, 1e-9)
    assert valid(1e308, 1e308, 1e-308, 1e-308)
    assert not valid(1e-308, 1e308, 2e-308, 1e308)
    assert math.isclose(mean(2, 8), 4)
    assert math.isclose(mean(3, 12), 6)
    assert valid(2, mean(2, 8), mean(2, 8), 8)
    for a, c in ((0, 8), (-1, 8), (2, math.inf), (math.nan, 3)):
        try:
            mean(a, c)
        except ValueError:
            pass
        else:
            raise AssertionError("比例中项非法输入未被拒绝")
    a, b, c, d = 2, 3, 4, 6
    assert b > 0 and d > 0 and b + d > 0
    assert math.isclose((a + b) / b, (c + d) / d)
    assert math.isclose((a + c) / (b + d), a / b)

    scene_classes = [node for node in TREE.body if isinstance(node, ast.ClassDef)
                     and node.name == "ProportionalSegments"]
    assert len(scene_classes) == 1, "原 Scene 入口被修改"
    for node in ast.walk(TREE):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "MathTex":
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    assert not any("\u4e00" <= char <= "\u9fff" for char in arg.value), "中文进入 MathTex"
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "play":
            for arg in node.args:
                assert not (isinstance(arg, ast.Call) and isinstance(arg.func, ast.Attribute)
                            and arg.func.attr == "play"), "嵌套 play"
    print("PASS: syntax, ordinary/tiny/extreme ratios, boundary conditions, Scene entry and AST checks")


if __name__ == "__main__":
    run_checks()
