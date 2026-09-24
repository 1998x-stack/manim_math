"""充分/必要/充要条件课的纯 Python 模型与源码回归。

python verify_conditions_scene.py；不会导入 Manim，也不表示渲染已完成。
"""
import ast
from math import hypot
from pathlib import Path

SOURCE = Path(__file__).with_name("sufficient_necessary_conditions.py")
source = SOURCE.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(SOURCE))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def find_value(scope, name):
    for stmt in scope.body:
        if isinstance(stmt, ast.Assign):
            if any(isinstance(t, ast.Name) and t.id == name for t in stmt.targets):
                if isinstance(stmt.value, ast.Call):
                    require(len(stmt.value.args) == 1, f"{name} 坐标无法校验")
                    return ast.literal_eval(stmt.value.args[0])
                return ast.literal_eval(stmt.value)
    raise AssertionError(f"Scene 数学常量 {name} 缺失")


def test_math():
    constants = {name: find_value(tree, name) for name in
                 ("SAMPLE_P_BOUND", "SAMPLE_Q_BOUND", "SAMPLE_COUNTEREXAMPLE",
                  "EQUIVALENT_BOUND")}
    namespace = dict(constants)
    funcs = ast.Module(body=[node for node in tree.body
                             if isinstance(node, ast.FunctionDef) and
                             node.name in ("p_condition", "q_condition", "r_condition", "s_condition")],
                       type_ignores=[])
    exec(compile(funcs, str(SOURCE), "exec"), namespace)
    p, q, r, s = (namespace[key] for key in
                   ("p_condition", "q_condition", "r_condition", "s_condition"))
    samples = (-10, -2, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.00001, 3, 10)
    for x in samples:
        require(not p(x) or q(x), f"{x}: p 应推出 q")
        require(r(x) == s(x), f"{x}: r 与 s 应等价")
    x = constants["SAMPLE_COUNTEREXAMPLE"]
    require(x == 1 and q(x) and not p(x), "x=1 应反驳 q 对 p 的充分性")
    require(not p(2) and not q(0), "不等式端点须是严格不等号")
    require(not r(-1) and not r(1) and r(0), "等价条件的边界错误")
    print("PASS: p⇒q、q 不充分、r⇔s 和开区间端点")


def test_geometry_and_scene():
    scene = next(cls for cls in tree.body if isinstance(cls, ast.ClassDef)
                 and cls.name == "SufficientNecessaryConditions")
    p_center = find_value(scene, "CENTER_P")
    q_center = find_value(scene, "CENTER_Q")
    r_p, r_q = find_value(scene, "RADIUS_P"), find_value(scene, "RADIUS_Q")
    distance = hypot(p_center[0] - q_center[0], p_center[1] - q_center[1])
    require(distance + r_p < r_q, "充分/必要图中 P 必须严格包含于 Q")
    require(r_q < 3.8 and p_center != q_center,
            "真包含图不能误画成 P=Q，也不能溢出水平安全区")
    require(find_value(scene, "RADIUS_EQUAL") > 0,
            "充要示意图需要正半径")
    methods = {m.name for m in scene.body if isinstance(m, ast.FunctionDef)}
    require({"show_opening", "show_sufficient_condition", "show_necessary_condition",
             "show_equivalent_condition", "show_summary"} <= methods,
            "须保留原有五个 Scene 环节")
    compile(source, str(SOURCE), "exec")
    for node in ast.walk(scene):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "play":
            require(not any(isinstance(inner, ast.Call)
                            and isinstance(inner.func, ast.Attribute)
                            and inner.func.attr == "play"
                            for arg in node.args for inner in ast.walk(arg)),
                    "禁止嵌套 self.play")
    print("PASS: 真包含圆几何、不同等价示例、Scene 入口和语法")


if __name__ == "__main__":
    test_math()
    test_geometry_and_scene()
    print("PASS: 已运行的纯 Python 回归全部通过；字体/TeX/媒体另须验收")
