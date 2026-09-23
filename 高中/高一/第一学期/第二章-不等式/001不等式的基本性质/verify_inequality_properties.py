"""不等式的六项性质：从真实 Scene 常量读取数轴示例的纯 Python 回归。

运行：python verify_inequality_properties.py；不导入 Manim，不代表已经渲染。
"""
import ast
from pathlib import Path

SOURCE = Path(__file__).with_name("inequality_properties_full.py")
source = SOURCE.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(SOURCE))


def require(condition, reason):
    if not condition:
        raise AssertionError(reason)


def assigned(name):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == name for t in node.targets
        ):
            return ast.literal_eval(node.value)
    raise AssertionError(f"缺少真实 Scene 数据 {name}")


def test_scene_examples():
    cases = assigned("NUMBER_LINE_CASES")
    require(set(cases) == {"symmetry", "transitivity", "addition", "positive", "negative"},
            "数轴案例和五种性质必须一一对应")
    compare = {">": lambda a, b: a > b, "<": lambda a, b: a < b}
    for key, (before, after, start_op, end_op) in cases.items():
        require(len(before) == len(after) == 2, f"{key}: 每根数轴都须显示两个元素")
        require(all(-6 <= n <= 6 for n in (*before, *after)),
                f"{key}: 有元素超出真实 NumberLine 的范围")
        require(compare[start_op](*before) and compare[end_op](*after),
                f"{key}: 数轴实际数据与不等号不一致")
    a, b = cases["symmetry"][:2]
    require(a == b[::-1] and cases["symmetry"][2:] == (">", "<"),
            "对称性必须交换两侧数字与符号")
    a, b = cases["transitivity"][:2]
    require(a[0] == b[0] and a[0] > a[1] > b[1], "传递性条件或结论有误")
    a, b = cases["addition"][:2]
    require(a[0] - b[0] == a[1] - b[1] == 2,
            "同加 -2 两侧必须使用相同增量")
    a, b = cases["positive"][:2]
    require(b == tuple(2 * value for value in a) and b[0] > b[1],
            "乘以正数 2 时不等号不能翻转")
    a, b = cases["negative"][:2]
    require(b == tuple(-2 * value for value in a) and b[0] < b[1],
            "乘以负数 -2 时不等号必须翻转")
    print("PASS: 五组上下数轴的真实数字、符号、变换与画面范围")


def test_general_properties():
    domain = range(-8, 9)
    for a in domain:
        for b in domain:
            if a <= b:
                continue
            require(b < a, "对称性错误")
            for c in domain:
                require(a + c > b + c, "加法不等式错误")
                if c > 0:
                    require(a * c > b * c, "乘正数不等式错误")
                elif c < 0:
                    require(a * c < b * c, "乘负数不等式错误")
                else:
                    require(a * c == b * c, "乘 0 后不能保留严格不等号")
                if b > c:
                    require(a > c, "传递性错误")
            if b > 0:
                require(a * a > b * b, "正数平方不等式错误")
    require((-3 < -2) and ((-3) ** 2 > (-2) ** 2),
            "应有平方无法一般保序的负数反例")
    sides = assigned("SQUARE_SIDES")
    require(sides == (3, 2) and sides[0] ** 2 == 9 and sides[1] ** 2 == 4,
            "面积方格与平方公式 3²=9、2²=4 必须一致")
    unit = assigned("SQUARE_UNIT")
    require(0 < unit < 1, "单位方格边长须一致且为正")
    print("PASS: 全部六项性质及 c<0、c=0、平方正数前提的边界回归")


def test_source_contract():
    compile(source, str(SOURCE), "exec")
    scene = next(node for node in tree.body if isinstance(node, ast.ClassDef)
                 and node.name == "InequalityPropertiesFull")
    methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
    expected = {"show_opening", "show_summary", "show_outro"} | {
        f"show_property_{number}" for number in range(1, 7)
    }
    require(expected <= methods, "须保留所有六项性质及原 Scene 九镜入口")
    for node in ast.walk(scene):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ("MathTex", "Tex"):
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        require(not any("\u3400" <= ch <= "\u9fff" for ch in arg.value),
                                "中文数学混排须用 Text 而非默认 MathTex")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "play":
            require(not any(isinstance(sub, ast.Call) and
                            isinstance(sub.func, ast.Attribute) and sub.func.attr == "play"
                            for arg in node.args for sub in ast.walk(arg)),
                    "禁止嵌套 self.play")
    print("PASS: Scene 入口、语法与关键静态动画用法")


if __name__ == "__main__":
    test_scene_examples()
    test_general_properties()
    test_source_contract()
    print("PASS: 已运行的纯 Python 测试通过；实际视频另须渲染验收")
