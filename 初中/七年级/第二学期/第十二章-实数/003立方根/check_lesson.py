"""立方根专项数学/源码回归；不依赖 Manim。"""
import ast
import math
from pathlib import Path

source = Path(__file__).with_name("cube_root.py").read_text(encoding="utf-8")
scene = [node for node in ast.parse(source).body
         if isinstance(node, ast.ClassDef) and node.name == "CubeRootConcept"]
assert len(scene) == 1
methods = {node.name for node in scene[0].body if isinstance(node, ast.FunctionDef)}
assert {"scene_opening", "scene_definition", "scene_three_cases", "scene_practice",
        "scene_comparison", "scene_outro"} <= methods
assert "负数立方根是代数中的数，不代表负的几何体积" in source
assert r"\sqrt[3]{-8}=-2" in source
assert r"\sqrt[3]{a^3}=a" in source

# 样例回归：奇次根是实数且符号随被开方数；不能以有限样本代替一般证明。
for x in (-11, -3, -2, -0.5, 0, 0.5, 2, 3, 11):
    a = x ** 3
    cbrt = math.copysign(abs(a) ** (1 / 3), a)
    assert math.isclose(cbrt, x, abs_tol=1e-9)
    assert math.isclose((-x) ** 3, -a)
    if a != 0:
        assert math.copysign(1, cbrt) == math.copysign(1, a)
assert all(x * x != -8 for x in range(-10, 11))
print("PASS: Scene entry, 6 scenes, signed cube roots, negative-volume distinction")
