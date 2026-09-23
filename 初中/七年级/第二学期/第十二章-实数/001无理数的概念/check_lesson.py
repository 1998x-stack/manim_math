"""本课纯 Python 数学与源码回归；不依赖 Manim，也不代替视频渲染。"""
import ast
from fractions import Fraction
from math import gcd, isclose, pi, sqrt
from pathlib import Path

path = Path(__file__).with_name("001无理数的概念_animation.py")
tree = ast.parse(path.read_text(encoding="utf-8"))
scenes = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
assert scenes == ["Topic001无理数的概念Animation"]

# 仅审计本课确实会送入 MathTex 的字面量与证明公式序列。
strings = []
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "MathTex":
        for arg in node.args:
            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                strings.append(arg.value)
    if isinstance(node, ast.Assign) and any(
        isinstance(target, ast.Name) and target.id == "formulas" for target in node.targets
    ):
        strings += [value.value for value in node.value.elts if isinstance(value, ast.Constant)]
assert len(strings) == 4
assert all(all(ord(character) < 128 for character in expression) for expression in strings)
assert all("\\text{" not in expression for expression in strings)

assert Fraction(1, 4) == Fraction("0.25")
assert Fraction(1, 3) * 3 == 1
assert isclose(sqrt(2), 1.41421356, abs_tol=1e-8)
assert isclose(pi, 3.14159265, abs_tol=1e-8)

# 有限范围仅检验反证法用到的奇偶命题，绝非用枚举证明 √2 无理。
for n in range(-200, 201):
    if n * n % 2 == 0:
        assert n % 2 == 0
for p in range(-40, 41):
    for q in range(-40, 41):
        if q != 0 and p * p == 2 * q * q:
            assert gcd(p, q) >= 2
print("PASS: scene name, MathTex ASCII, rational examples, parity regression")
