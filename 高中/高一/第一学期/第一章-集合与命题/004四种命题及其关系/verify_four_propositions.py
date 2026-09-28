"""四种命题课的独立数学和源码测试；不导入 Manim。

python verify_four_propositions.py
"""
import ast
from pathlib import Path

SOURCE = Path(__file__).with_name("four_propositions.py")
source = SOURCE.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(SOURCE))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def assigned(scope, name):
    for node in scope.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                return ast.literal_eval(node.value)
    raise AssertionError(f"未发现常量 {name}")


def test_logic():
    definitions = ast.Module(body=[node for node in tree.body
                                   if isinstance(node, ast.FunctionDef)
                                   and node.name in {"implies", "proposition_values"}],
                             type_ignores=[])
    namespace = {}
    exec(compile(definitions, str(SOURCE), "exec"), namespace)
    proposition_values = namespace["proposition_values"]
    implies = namespace["implies"]
    for p in (False, True):
        for q in (False, True):
            original, converse, inverse, contrapositive = proposition_values(p, q)
            require(original == contrapositive, "原命题与逆否命题应等价")
            require(converse == inverse, "逆命题与否命题应等价")
            require(original == implies(p, q), "原命题真值计算错误")
            require(converse == implies(q, p), "逆命题真值计算错误")
    require(proposition_values(False, True) == (True, False, False, True),
            "逆命题和否命题不总与原命题等价")
    example = assigned(tree, "EXAMPLE_COUNTEREXAMPLE")
    require(example == 2, "应使用 n=2 作为两个非等价命题的反例")
    for n in range(-100, 101):
        p, q = n % 4 == 0, n % 2 == 0
        original, converse, inverse, contra = proposition_values(p, q)
        require(original and contra, f"整数 n={n} 不满足原/逆否命题")
        if n == example:
            require(not converse and not inverse, "n=2 应反驳逆命题和否命题")
    print("PASS: 全部四行真值及 201 个整数样本，反例 n=2")


def test_source_contract():
    compile(source, str(SOURCE), "exec")
    scene = next(node for node in tree.body if isinstance(node, ast.ClassDef)
                 and node.name == "FourPropositions")
    specs = assigned(scene, "SPECS")
    require([row[0] for row in specs] == ["原命题", "逆命题", "否命题", "逆否命题"],
            "四卡标签顺序不正确")
    require([row[1] for row in specs] == [r"p\to q", r"q\to p",
                                       r"\neg p\to\neg q", r"\neg q\to\neg p"],
            "四种命题的条件与结论或 TeX 转义不正确")
    require(assigned(tree, "EXAMPLE_DOMAIN") == r"n\in\mathbb{Z}",
            "必须明确整数论域")
    methods = {node.name for node in scene.body if isinstance(node, ast.FunctionDef)}
    require({"show_opening", "show_what_is_proposition", "show_original",
             "show_converse", "show_inverse", "show_contrapositive",
             "show_relationship_diagram", "show_equivalence", "show_outro"} <= methods,
            "原九镜教学顺序必须保留")
    for node in ast.walk(scene):
        if not isinstance(node, ast.Call):
            continue
        if isinstance(node.func, ast.Name) and node.func.id in {"Tex", "MathTex"}:
            for arg in node.args:
                if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                    require(not any("\u3400" <= ch <= "\u9fff" for ch in arg.value),
                            "中文须用 Text，不能直接放入默认 MathTex")
        if isinstance(node.func, ast.Attribute) and node.func.attr == "play":
            require(not any(isinstance(inner, ast.Call)
                            and isinstance(inner.func, ast.Attribute)
                            and inner.func.attr == "play"
                            for arg in node.args for inner in ast.walk(arg)),
                    "禁止嵌套 self.play")
    print("PASS: Scene 类、九镜、实际公式 TeX 和关键静态规则")


if __name__ == "__main__":
    test_logic()
    test_source_contract()
    print("PASS: 已执行的纯 Python 回归通过；Manim 渲染仍需单独验收")
