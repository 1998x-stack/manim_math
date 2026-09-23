"""实数分类与源码回归：标准库验证离散示例，不代替数学证明或渲染。"""
import ast
import math
from fractions import Fraction
from pathlib import Path

src = Path(__file__).with_name("real_numbers.py").read_text(encoding="utf-8")
tree = ast.parse(src)
scene = [node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "RealNumbersConcept"]
assert len(scene) == 1
methods = {node.name for node in scene[0].body if isinstance(node, ast.FunctionDef)}
assert {"scene_opening", "scene_number_line", "scene_classification_tree",
        "scene_examples", "scene_pos_neg_classification", "scene_outro"} <= methods
assert r"\sqrt{4}=2" in src
assert r"0.\overline{3}=\frac{1}{3}" in src
assert "非整数有理数" in src
assert "0.333\\ldots" not in src
assert "include_numbers=True" in src

for a, b in ((1, 3), (1, 4), (2, 3), (-5, 2)):
    q = Fraction(a, b)
    assert q.denominator != 0
assert Fraction("0.25") == Fraction(1, 4)
assert 3 * Fraction(1, 3) == 1
assert math.isclose(math.sqrt(2), 1.4142135623730951)
assert math.sqrt(4) == 2
assert all(x > 0 for x in (Fraction(1, 3), math.sqrt(2), math.pi))
assert all(x < 0 for x in (-2, -math.sqrt(3), -math.pi))
print("PASS: Scene entry, six scenes, sqrt(4), recurring/fixed decimals, sign classes")
