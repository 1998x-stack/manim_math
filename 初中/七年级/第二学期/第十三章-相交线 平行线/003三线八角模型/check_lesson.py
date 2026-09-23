"""三线八角专项纯数学回归：提取实际源码交点与角弧函数。"""
import ast
from math import atan2, degrees, isclose, pi
from pathlib import Path

source = Path(__file__).with_name('three_lines_eight_angles.py').read_text(encoding='utf-8')
tree = ast.parse(source)
scene = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'ThreeLinesEightAngles')
methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
assert {'setup_geometry','draw_lines','draw_angles','show_opening','show_construction',
        'show_corresponding_angles','show_alternate_angles','show_consecutive_angles',
        'show_summary','show_outro'} <= methods
model = [n for n in tree.body if isinstance(n, ast.FunctionDef)
         and n.name in ('intersect_horizontal', 'angle_sector')]
assert len(model) == 2
namespace = {'pi': pi}
exec(compile(ast.Module(body=model, type_ignores=[]), '<geometry>', 'exec'), namespace)
intersect = namespace['intersect_horizontal']
sector = namespace['angle_sector']
p = intersect((-2.0,-3.6),(2.2,4.8),2.0)
q = intersect((-2.0,-3.6),(2.2,4.8),-0.8)
assert all(isclose(a,b,abs_tol=1e-9) for a,b in zip(p,(0.8,2.0)))
assert all(isclose(a,b,abs_tol=1e-9) for a,b in zip(q,(-0.6,-0.8)))
assert isclose((p[0]-q[0])/(p[1]-q[1]),.5)
try:
    intersect((0,0),(2,0),2)
except ValueError:
    pass
else:
    raise AssertionError('parallel transversal must reject')
theta = atan2(2,1)
values = [degrees(sector(i,theta)[1]) for i in range(8)]
assert all(0 < value < 180 for value in values)
assert all(isclose(values[a-1], values[b-1])
           for a,b in ((1,5),(2,6),(3,7),(4,8),(3,5),(4,6)))
assert all(isclose(values[a-1]+values[b-1],180)
           for a,b in ((3,6),(4,5)))
# 标签的中线位于角弧中间，弧不会错画为补角或优角。
for i in range(8):
    start, span, midpoint = sector(i, theta)
    assert isclose(midpoint, start+span/2)
    assert span < pi
# 不允许把同位角/内错角的相等或同旁内角互补脱离平行条件。
assert '互补结论成立的前提：被截两条直线平行' in source
assert '只有在有平行条件时' in source
assert r'\text{与}' not in source
print('PASS: actual Scene, two intersections, eight minor sectors, 4 corresponding/2 alternate/2 consecutive pairs')
