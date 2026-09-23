"""与实际二次不等式 Scene 数学常量关联的纯 Python 回归。

python verify_quadratic_inequality_scene.py；不导入 Manim，不代表视频已渲染。
"""
import ast
from math import sqrt
from pathlib import Path

SOURCE = Path(__file__).with_name("quadratic_inequality.py")
source = SOURCE.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(SOURCE))


def require(condition, reason):
    if not condition:
        raise AssertionError(reason)


def constant(name):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise AssertionError(f"实际脚本常量缺失：{name}")


def math_functions():
    selected = ast.Module(body=[node for node in tree.body
                                if isinstance(node, ast.FunctionDef) and node.name in
                                ("quadratic", "analyze_quadratic", "positive_solution")],
                          type_ignores=[])
    scope = {"sqrt": sqrt}
    exec(compile(selected, str(SOURCE), "exec"), scope)
    return (scope[key] for key in ("quadratic", "analyze_quadratic", "positive_solution"))


def test_primary_example_and_graph():
    f, analyze, positive = math_functions()
    a, b, c = constant("EXAMPLE_COEFFICIENTS")
    delta, roots = analyze(a, b, c)
    require((a, b, c) == (1, -3, 2) and delta == 1 and roots == (1.0, 2.0),
            "主例系数、判别式或根与屏幕不一致")
    require(f(a, b, c, roots[0]) == f(a, b, c, roots[1]) == 0,
            "实际图像必须通过两个显示的零点")
    require(f(a, b, c, 1.5) < 0 and f(a, b, c, 0) > 0 and f(a, b, c, 3) > 0,
            "两侧为正、中间为负与画面着色不一致")
    for x in (roots[0], roots[1]):
        require(not positive(a, b, c, x), "严格 >0 不能包含两个零点")
    low, high = constant("GRAPH_X_RANGE")
    ymin, ymax = constant("GRAPH_Y_RANGE")
    require(low < 1 < 2 < high, "两个实根必须位于曲线显示范围内部")
    require(ymin < f(a, b, c, 1.5), "抛物线顶点应在画面内")
    for i in range(301):
        x = low + (high - low) * i / 300
        require(ymin < f(a, b, c, x) < ymax,
                f"主抛物线 x={x} 的函数值超出显示坐标轴 y_range")
        if x < 1 or x > 2:
            require(positive(a, b, c, x), "两零点外严格正值区域错误")
        elif 1 < x < 2:
            require(not positive(a, b, c, x), "两零点内负值区域错误")
    print("PASS: 主例判别式、1/2 两根、严格解集和整个绘图范围采样")


def test_discriminant_and_sign():
    f, analyze, positive = math_functions()
    require(constant("DISCRIMINANT_CASES") ==
            ((1, 0, -1), (1, 0, 0), (1, 0, 1)),
            "三张图必须严格分别展示 Δ>0、Δ=0、Δ<0 的不同函数")
    for coeffs in constant("DISCRIMINANT_CASES"):
        a, b, c = coeffs
        delta, roots = analyze(a, b, c)
        if c == -1:
            require(delta > 0 and roots == (-1.0, 1.0), "双根例子错误")
            require(all(positive(a, b, c, x) == (abs(x) > 1)
                        for x in (-2, -1, -0.5, 0, 0.5, 1, 2)),
                    "Δ>0、a>0 的严格解集必须在两根外侧")
        elif c == 0:
            require(delta == 0 and roots == (0.0,), "重根例子错误")
            require(all(positive(a, b, c, x) == (x != 0)
                        for x in (-2, -1, 0, 1, 2)), "Δ=0 时必须排除重根")
        else:
            require(delta < 0 and roots == () and
                    all(positive(a, b, c, x) for x in (-3, -1, 0, 1, 3)),
                    "Δ<0 且 a>0 时全部实数均为解")
    neg_delta, neg_roots = analyze(-1, 0, 1)
    require(neg_delta > 0 and neg_roots == (-1.0, 1.0),
            "a<0 时应按数值大小重新排序根")
    require(positive(-1, 0, 1, 0) and not positive(-1, 0, 1, 2),
            "a<0 时 >0 解集转至两根之间")
    require(not positive(-1, 0, -1, x=0), "a<0、Δ<0 时不可能 >0")
    try:
        analyze(0, 2, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("必须拒绝 a=0 的非二次退化输入")
    print("PASS: Δ 三分法、a<0 对照、重根/零点和 a=0 退化输入")


def test_scene_source():
    compile(source, str(SOURCE), "exec")
    scene = next(node for node in tree.body if isinstance(node, ast.ClassDef)
                 and node.name == "QuadraticInequality")
    methods = {item.name for item in scene.body if isinstance(item, ast.FunctionDef)}
    require({"show_opening", "show_transformation", "show_coordinate_system",
             "show_parabola", "show_roots", "show_regions", "show_three_cases",
             "show_outro", "setup_mathematics", "verify_mathematics"} <= methods,
            "需要保留原八镜入口及实际根与顶点校验")
    for node in ast.walk(scene):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "play":
            require(not any(isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute)
                            and sub.func.attr == "play"
                            for arg in node.args for sub in ast.walk(arg)),
                    "禁止嵌套 self.play")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("Tex", "MathTex"):
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    require(not any("\u3400" <= char <= "\u9fff" for char in arg.value),
                            "默认 TeX 不应包含中文")
    print("PASS: 原八镜入口、Python 语法和关键 Manim AST 约束")


if __name__ == "__main__":
    test_primary_example_and_graph()
    test_discriminant_and_sign()
    test_scene_source()
    print("PASS: 本课纯 Python 回归通过；真实图像需另行渲染验收")
