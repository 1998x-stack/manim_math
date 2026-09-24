"""独立专项验证：从实际源码 AST 提取纯二维投影函数。"""
import ast
from math import hypot, isclose
from pathlib import Path

src = Path(__file__).with_name('perpendicular_lines.py').read_text(encoding='utf-8')
tree = ast.parse(src)
scene = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'PerpendicularLines')
methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
assert {'show_opening','show_definition','show_uniqueness','show_shortest_distance',
        'show_application','show_summary','show_outro','right_angle_mark','verify_geometry'} <= methods
pure_function = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                     and n.name == 'foot_of_perpendicular')
namespace = {}
exec(compile(ast.Module(body=[pure_function], type_ignores=[]), '<projection>', 'exec'), namespace)
foot = namespace['foot_of_perpendicular']
L0, L1 = (-3.5, 0), (3.5, 0)
P, A, B, Q = (-1.5, 2.5), (0.8, 0), (-3.2, 0), (1.8, 2.8)
H, K = foot(P, L0, L1), foot(Q, L0, L1)
assert all(isclose(v, e, abs_tol=1e-9) for actual, expected in ((H,(-1.5,0)), (K,(1.8,0))) for v,e in zip(actual, expected))
assert hypot(P[0]-H[0], P[1]-H[1]) < hypot(P[0]-A[0], P[1]-A[1])
assert hypot(P[0]-H[0], P[1]-H[1]) < hypot(P[0]-B[0], P[1]-B[1])
assert isclose(hypot(P[0]-H[0], P[1]-H[1]), 2.5)
# 斜线/负斜率、垂足在线段外、点在线上、直线方向颠倒。
for start, end, point, expected in [
    ((0,0),(2,2),(0,2),(1,1)), ((0,0),(2,-2),(0,-2),(1,-1)),
    ((0,0),(2,0),(5,3),(5,0)), ((0,0),(2,0),(1,0),(1,0)),
    ((2,2),(0,0),(0,2),(1,1)),
]:
    result = foot(point, start, end)
    assert all(isclose(a,b,abs_tol=1e-9) for a,b in zip(result,expected))
try:
    foot((1,2),(0,0),(0,0))
except ValueError:
    pass
else:
    raise AssertionError('degenerate line must be rejected')
assert 'WARNING: PH不垂直' not in src
assert 'self.H = np.array([*foot_of_perpendicular(' in src
print('PASS: original Scene and seven scenes, perpendicular projections, shortest distances, degenerate line')
