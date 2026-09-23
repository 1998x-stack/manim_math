"""平行线判定专项回归：验证原本错误的同点邻补角不足以判定平行。"""
import ast
from math import atan2, cos, degrees, isclose, pi, radians, sin
from pathlib import Path

src = Path(__file__).with_name('parallel_lines.py').read_text(encoding='utf-8')
tree = ast.parse(src)
scene = next(node for node in tree.body if isinstance(node, ast.ClassDef)
             and node.name == 'ParallelLineDetermination')
scene_methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
assert {f'scene_{i}_{name}' for i,name in ((1,'opening'),(2,'diagram'),
    (3,'corresponding'),(4,'alternate'),(5,'cointerior'),(6,'summary'),(7,'outro'))} <= scene_methods
sector_ast = next(node for node in tree.body if isinstance(node, ast.FunctionDef)
                  and node.name == 'sector_spec')
namespace = {'pi': pi}
exec(compile(ast.Module(body=[sector_ast], type_ignores=[]), '<sectors>', 'exec'), namespace)
sector = namespace['sector_spec']
theta, tilt = atan2(2, 1), radians(15)
value = lambda index, delta: degrees(sector(index, theta, delta)[1])
# 先检验不平行场景：同一点的邻补角仍然互补，不能推出两线平行。
assert not isclose(sin(tilt), 0)
assert isclose(value(5,tilt) + value(6,tilt), 180)
assert isclose(value(1,tilt) - value(5,tilt), 15)
assert not isclose(value(4,tilt) + value(5,tilt), 180)
assert not isclose(value(3,tilt), value(5,tilt))
# 下方直线转至水平后：同位角、内错角及同旁内角三判据恰好满足。
assert isclose(sin(0),0)
assert isclose(value(1,0),value(5,0))
assert isclose(value(3,0),value(5,0))
assert isclose(value(4,0) + value(5,0), 180)
for delta in (0,tilt):
    for i in range(1,9):
        start, span, middle = sector(i,theta,delta)
        assert 0 < span < pi and isclose(middle,start+span/2)
assert r'\angle1=\angle2' not in src
assert r'\angle3=\angle4' not in src
assert '同一交点的邻补角' in src
assert '反例' in src
print('PASS: seven existing scenes, actual sector model, nonparallel counterexample, 3 valid criteria')
