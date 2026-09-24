"""对顶角与邻补角专项几何/源码回归：无 Manim 依赖。"""
import ast
from math import cos, degrees, isclose, pi, radians, sin, tau
from pathlib import Path

source = Path(__file__).with_name('vertical_and_adjacent_angles.py').read_text(encoding='utf-8')
tree = ast.parse(source)
scene = [node for node in tree.body if isinstance(node, ast.ClassDef)
         and node.name == 'VerticalAndAdjacentAngles']
assert len(scene) == 1
methods = {node.name for node in scene[0].body if isinstance(node, ast.FunctionDef)}
assert {'setup_geometry', 'verify_geometry', 'draw_sector', 'show_opening',
        'show_intersecting_lines', 'show_vertical_angles', 'show_adjacent_angles',
        'show_numerical_example', 'show_summary', 'show_outro'} <= methods
sweep_node = next(node for node in tree.body if isinstance(node, ast.FunctionDef)
                  and node.name == 'signed_short_sweep')
namespace = {'PI': pi, 'TAU': tau}
exec(compile(ast.Module(body=[sweep_node], type_ignores=[]), '<sweep>', 'exec'), namespace)
short_sweep = namespace['signed_short_sweep']
angles = tuple(radians(deg) for deg in (30, -40, 210, 140))
sweeps = [short_sweep(angles[i], angles[(i + 1) % 4]) for i in range(4)]
values = [abs(degrees(s)) for s in sweeps]
assert all(-pi < s < 0 for s in sweeps), sweeps
assert all(isclose(value, expect, abs_tol=1e-9)
           for value, expect in zip(values, (70, 110, 70, 110)))
assert isclose(values[0], values[2]) and isclose(values[1], values[3])
assert isclose(values[0] + values[1], 180)
# 实际渲染的标签方位使用同一有向弧的中间角，不是优角中点。
expected_mid = (-5, -95, 175, 85)
for i, degree in enumerate(expected_mid):
    midpoint = angles[i] + sweeps[i] / 2
    assert isclose(cos(midpoint), cos(radians(degree)), abs_tol=1e-9)
    assert isclose(sin(midpoint), sin(radians(degree)), abs_tol=1e-9)
    end = angles[i] + sweeps[i]
    assert isclose(sin(end), sin(angles[(i + 1) % 4]), abs_tol=1e-9)
    assert isclose(cos(end), cos(angles[(i + 1) % 4]), abs_tol=1e-9)
assert '同角互补' not in source
assert '邻补角互补' in source
assert 'angle=sweep' in source
print('PASS: Scene entry, seven scenes, short signed arcs, labels, vertical & supplementary angles')
