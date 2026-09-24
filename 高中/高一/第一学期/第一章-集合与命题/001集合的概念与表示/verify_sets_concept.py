"""不导入 Manim 的集合课数学/静态回归：python verify_sets_concept.py。"""

import ast
from pathlib import Path

SOURCE = Path(__file__).with_name("sets_concept.py")


def verify():
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
    elements = next(
        ast.literal_eval(node.value)
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "DISPLAYED_ELEMENTS"
                for target in node.targets)
    )
    A = set(elements)
    assert elements == (1, 2, 3, 4, 5), "集合模型或画面元素有变化，须同步审核公式"
    assert len(A) == len(elements), "集合内不可将重复对象计为不同元素"
    assert 3 in A and 6 not in A, "隶属关系与画面不一致"
    assert {1, 2, 2, 3, 4, 5} == A, "互异性例子有误"
    assert {5, 3, 1, 4, 2} == A, "无序性例子有误"
    assert {x for x in range(-10, 11) if isinstance(x, int) and 1 <= x <= 5} == A
    assert all(1 <= x <= 5 for x in A), "描述法与列举法不一致"
    classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    assert any(node.name == "SetsConceptAnimation" for node in classes), "场景入口被意外更名"
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "play":
            assert not any(isinstance(arg, ast.Call) and isinstance(arg.func, ast.Attribute)
                           and arg.func.attr == "play" for arg in node.args), "禁止嵌套 self.play"
    print("PASS: 集合模型、两种表示、隶属关系、入口及嵌套动画静态检查")


if __name__ == "__main__":
    verify()
