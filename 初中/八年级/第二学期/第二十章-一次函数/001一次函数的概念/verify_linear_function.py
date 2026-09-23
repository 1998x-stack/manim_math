"""无需安装 Manim 的一次函数数学回归：python verify_linear_function.py。"""

import ast
from pathlib import Path

SOURCE = Path(__file__).with_name("linear_function_concept.py")
tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
# 仅提取数学纯函数，避免验证阶段加载图形/字体/TeX 环境。
namespace = {}
for name in ("linear_value", "visible_interval"):
    assert name in functions, f"missing mathematical model: {name}"
    module = ast.Module(body=[functions[name]], type_ignores=[])
    exec(compile(module, str(SOURCE), "exec"), namespace)

value = namespace["linear_value"]
interval = namespace["visible_interval"]


def rejects(call):
    try:
        call()
    except ValueError:
        return
    raise AssertionError("invalid mathematical input must raise ValueError")


def test_math():
    assert value(2, 0, 0) == 0
    assert value(2, 1, 0) == 1
    assert value(2, 1, 1) == 3
    assert value(-1, 2, 1) == 1
    rejects(lambda: value(0, 1, 2))
    rejects(lambda: interval(0, 1, -3, 3, -3, 3))
    rejects(lambda: interval(1, 0, 1, 1, -3, 3))
    rejects(lambda: interval(1, 0, -3, 3, 2, 2))
    rejects(lambda: interval(1, 10, -3, 3, -3, 3))

    cases = [
        (2, 0, -1, 1),     # 正比例函数
        (2, 1, -1, 1),     # 向上平移一个单位后的整个图像仍可见
        (1, 1, -3, 2),
        (-1, 2, -1, 3),
        (0.5, -1, -3, 3),
        (-2, 0, -1.5, 1.5),
    ]
    for k, b, expected_start, expected_end in cases:
        lo, hi = interval(k, b, -3 if (k, b) != (2, 0) and (k, b) != (2, 1) else -1,
                          3 if (k, b) != (2, 0) and (k, b) != (2, 1) else 1,
                          -3, 3)
        assert (lo, hi) == (expected_start, expected_end), (k, b, lo, hi)
        assert lo < hi
        for x in (lo, (lo + hi) / 2, hi):
            assert -3 - 1e-9 <= value(k, b, x) <= 3 + 1e-9
    print("PASS: function values, domain boundaries, invalid inputs and six displayed graphs")


if __name__ == "__main__":
    test_math()
