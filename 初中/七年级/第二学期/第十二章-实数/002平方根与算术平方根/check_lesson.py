"""平方根课专项回归：纯标准库，不冒充 Manim 实际渲染。"""
import ast
import math
from pathlib import Path

source = Path(__file__).with_name("sqrt_concept.py").read_text(encoding="utf-8")
tree = ast.parse(source)
scene = [node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "SquareRootConcept"]
assert len(scene) == 1, "existing entrypoint must remain"
method_names = {node.name for node in scene[0].body if isinstance(node, ast.FunctionDef)}
assert {"scene_opening", "scene_definition", "scene_three_cases", "scene_arithmetic_sqrt",
        "scene_key_formula", "scene_practice", "scene_outro"} <= method_names

# MathTex 字面量必须是纯 ASCII LaTeX；中文另用 Text。
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "MathTex":
        for arg in node.args:
            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                assert arg.value.isascii(), (node.lineno, arg.value)

# 禁止把 sqrt(4) 写成 ±2，或笼统声称 0 有两个不同的平方根。
assert r"\sqrt{4}=\pm2" not in source
assert "正数有两个不同的平方根，零只有一个" in source
assert r"\sqrt{9}=3" in source
assert r"\sqrt{a^2}=|a|" in source

for a in (0.0, 0.25, 4.0, 9.0, 36.0):
    arithmetic = math.sqrt(a)
    assert arithmetic >= 0
    assert math.isclose(arithmetic * arithmetic, a)
    roots = {arithmetic, -arithmetic}
    assert len(roots) == (1 if a == 0 else 2)
for x in (-7.0, -3.0, -0.1, 0.0, 0.1, 3.0, 7.0):
    assert math.isclose(math.sqrt(x * x), abs(x))
assert all(x * x >= 0 for x in (-4, -2, 0, 2, 4))
print("PASS: Scene entry, seven scenes, MathTex literals, zero/negative domain, |a| cases")
