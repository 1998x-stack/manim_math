"""集合运算 Scene 的纯 Python 数学、Venn 几何及源码回归。

运行：python verify_set_operations.py
不导入 Manim；不能代替实际 LaTeX/视频渲染或 Mobject 包围盒检查。
"""
from __future__ import annotations

import ast
from itertools import combinations
from math import hypot
from pathlib import Path


SOURCE = Path(__file__).with_name("set_operations.py")
TREE = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def assignment(scope, name):
    for statement in scope.body:
        if isinstance(statement, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name for target in statement.targets
        ):
            return statement.value
    raise AssertionError(f"缺少代码常量：{name}")


def literal(scope, name):
    return ast.literal_eval(assignment(scope, name))


def array(scope, name):
    node = assignment(scope, name)
    require(isinstance(node, ast.Call) and len(node.args) == 1,
            f"{name} 需要明确的坐标常量")
    return ast.literal_eval(node.args[0])


def test_scene_model():
    scene = next(node for node in TREE.body if isinstance(node, ast.ClassDef)
                 and node.name == "SetOperations")
    u, a, b = [set(literal(TREE, "ELEMENTS_" + suffix)) for suffix in ("U", "A", "B")]
    require(len(u) == 8 and a <= u and b <= u, "全集/子集定义错误")
    require(a & b == {3, 4}, "交集和动画内容不一致")
    require(a | b == {1, 2, 3, 4, 5, 6}, "并集和动画内容不一致")
    require(u - a == {5, 6, 7, 8}, "补集必须包括全集中 A 外的 5、6、7、8")
    require(u - (a & b) == {1, 2, 5, 6, 7, 8}, "综合题补集不正确")
    require(a - b == {1, 2}, "综合题交集不正确")
    centers = {key: array(scene, key) for key in
               ("CIRCLE_A_CENTER", "CIRCLE_B_CENTER", "UNIVERSAL_CENTER")}
    positions = literal(scene, "MARKER_POSITIONS")
    radius = literal(scene, "CIRCLE_RADIUS")
    width = literal(scene, "UNIVERSAL_WIDTH")
    height = literal(scene, "UNIVERSAL_HEIGHT")
    require(set(positions) == u, "屏幕元素必须与全集一一对应")
    for number, (x, y) in positions.items():
        p = (x, y)
        for letter, values in (("A", a), ("B", b)):
            center = centers[f"CIRCLE_{letter}_CENTER"]
            distance = hypot(p[0] - center[0], p[1] - center[1])
            require((distance < radius - 0.1) == (number in values),
                    f"数字 {number} 的圆内外位置与集合 {letter} 不一致")
        center_u = centers["UNIVERSAL_CENTER"]
        require(abs(x - center_u[0]) < width / 2 - 0.13
                and abs(y - center_u[1]) < height / 2 - 0.13,
                f"数字 {number} 不在全集矩形内部")
    scene_methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
    require({"show_opening", "show_intersection", "show_union", "show_complement",
             "show_properties_1", "show_properties_2", "show_example", "show_outro"}
            <= scene_methods, "必须保留原教学场景入口")
    print("PASS: 交、并、补与综合例题的实际集合常量及 8 个元素的圆内外关系")


def test_general_laws():
    for n in range(5):
        universe = set(range(n))
        all_subsets = [set(parts) for k in range(n + 1)
                       for parts in combinations(universe, k)]
        for a in all_subsets:
            require(a | (universe - a) == universe, "补集并集恒等式错误")
            require(a & (universe - a) == set(), "补集交集恒等式错误")
            require(universe - (universe - a) == a, "双重补集恒等式错误")
            require(a | set() == a and a & set() == set(), "空集运算错误")
            for b in all_subsets:
                require(universe - (a | b) == (universe - a) & (universe - b),
                        "德摩根律错误")
    print("PASS: 空集、全集及全部小型有限集合的补集性质")


def test_source_contract():
    compile(SOURCE.read_text(encoding="utf-8"), str(SOURCE), "exec")
    for node in ast.walk(TREE):
        if not isinstance(node, ast.Call):
            continue
        if isinstance(node.func, ast.Name) and node.func.id in {"Tex", "MathTex"}:
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    require(not any("\u3400" <= char <= "\u9fff" for char in arg.value),
                            "中文不得直接传入默认 MathTex/Tex")
        if isinstance(node.func, ast.Attribute) and node.func.attr == "play":
            require(not any(isinstance(inner, ast.Call)
                            and isinstance(inner.func, ast.Attribute)
                            and inner.func.attr == "play"
                            for arg in node.args for inner in ast.walk(arg)),
                    "不可嵌套调用 self.play")
    print("PASS: Python 语法、Scene 接口及关键 Manim 静态用法")


if __name__ == "__main__":
    test_scene_model()
    test_general_laws()
    test_source_contract()
    print("PASS: 已运行的纯 Python 测试全部通过；真实渲染尚未执行")
