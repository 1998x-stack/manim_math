"""独立验证 002 的真实源码常量、子集公式与示意圆布局。"""

import ast
from itertools import combinations
from math import hypot
from pathlib import Path

SOURCE = Path(__file__).with_name("set_relations.py")


def class_attribute(tree, name):
    scene = next(n for n in tree.body if isinstance(n, ast.ClassDef)
                 and n.name == "SetRelationsAnimation")
    value = next(n.value for n in scene.body if isinstance(n, ast.Assign)
                 and any(isinstance(t, ast.Name) and t.id == name for t in n.targets))
    if isinstance(value, ast.Call) and isinstance(value.func, ast.Attribute) and value.func.attr == "array":
        return ast.literal_eval(value.args[0])
    return ast.literal_eval(value)


def main():
    source = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(source)
    data = {target.id: ast.literal_eval(node.value)
            for node in tree.body if isinstance(node, ast.Assign)
            for target in node.targets if isinstance(target, ast.Name)
            and target.id in {"A_MEMBERS", "B_MEMBERS"}}
    a, b = set(data["A_MEMBERS"]), set(data["B_MEMBERS"])
    assert a == {1, 2, 3} and b == {1, 2, 3, 4, 5}
    assert a < b and a <= b and a != b and not b <= a
    subsets = [set(group) for k in range(len(a) + 1) for group in combinations(sorted(a), k)]
    assert len(subsets) == 2 ** len(a) == 8
    assert len([s for s in subsets if s < a]) == 2 ** len(a) - 1 == 7
    assert subsets[-1] == a, "最后一张卡片必须是 A，自身不是其真子集"
    assert all(set() <= s for s in subsets)
    assert not set() < set()
    center_a, center_b = (class_attribute(tree, f"CENTER_{key}") for key in ("A", "B"))
    radius_a, radius_b = (class_attribute(tree, f"RADIUS_{key}") for key in ("A", "B"))
    assert hypot(center_a[0] - center_b[0], center_a[1] - center_b[1]) + radius_a < radius_b
    assert all(abs(c[0]) + r < 4 and abs(c[1]) + r < 7
               for c, r in [(center_a, radius_a), (center_b, radius_b)])
    assert "C=\\{1,2,3\\}" in source and "D=\\{3,2,1\\}" in source
    print("PASS: 源码集合常量、8/7 子集计数、空集边界、Venn 圆包含关系")


if __name__ == "__main__":
    main()
