"""本课纯数学与源码回归（不调用 Manim，不冒充实渲染）。"""
import ast
from fractions import Fraction
from math import isclose, sqrt
from pathlib import Path

source = Path(__file__).with_name("real_number_ops.py").read_text(encoding="utf-8")
scene = [x for x in ast.parse(source).body if isinstance(x, ast.ClassDef)
         and x.name == "RealNumberOperations"]
assert len(scene) == 1
methods = {x.name for x in scene[0].body if isinstance(x, ast.FunctionDef)}
assert {"scene_opening", "scene_add_sub", "scene_mul_div", "scene_simplify",
        "scene_abs_value", "scene_laws", "scene_combined", "scene_outro"} <= methods
assert r"\sqrt{a^2b}=|a|\sqrt{b}" in source
assert r"\sqrt{a^2b}=a\sqrt{b}" not in source
assert "除法还要求 b 大于 0" in source
assert "根号内不同，不一定不能合并" in source

for a in (-3, -1, 0, 1, 3):
    for b in (0, Fraction(1, 4), 2, 7):
        assert isclose(sqrt(a * a * b), abs(a) * sqrt(b))
for a in (0, 2, 3, 12):
    for b in (0, 3, 5):
        assert isclose(sqrt(a) * sqrt(b), sqrt(a * b))
    for b in (1, 3, 5):
        assert isclose(sqrt(a) / sqrt(b), sqrt(a / b))
assert isclose(sqrt(2) + sqrt(8), 3 * sqrt(2))
assert sqrt(10) > 3 and sqrt(2) > 1
assert isclose((sqrt(3) + sqrt(2)) * (sqrt(3) - sqrt(2)), 1)
assert isclose(sqrt(2) * sqrt(8) + sqrt(3) * sqrt(3), 7)
print("PASS: 8 scenes, principal root sign, radicand and denominator domain, sample operations")
