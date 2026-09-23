"""整式方程课程纯数学回归；以 AST 提取模型，无需安装 Manim。"""
import ast
from math import copysign, isfinite
from pathlib import Path

path = Path(__file__).with_name("integral_equation_animation.py")
source = path.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(path))
namespace = {"isfinite": isfinite, "copysign": copysign}
for name in ("polynomial_value", "factor_roots", "real_cube_root"):
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name)
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(path), "exec"), namespace)
poly = namespace["polynomial_value"]
roots = namespace["factor_roots"]
cube = namespace["real_cube_root"]


def run():
    assert any(isinstance(node, ast.ClassDef) and node.name == "IntegralEquation"
               for node in tree.body)
    for index, ending in enumerate(("hook", "definition", "core_idea", "example",
                                    "zero_product", "cube_type", "outro"), start=1):
        assert f"def scene{index}_{ending}(" in source
    assert roots(2) == (-2.0, 0.0, 2.0)
    assert roots(-2) == (-2.0, 0.0, 2.0)
    assert roots(0) == (0.0,)  # 三个因子都为 x 时，只有一个互异解
    for root in roots(2):
        assert poly(root) == 0
        assert root ** 3 - 4 * root == 0
    for x in (-5, -3, -1, 1, 3, 5):
        assert poly(x) == x**3 - 4*x
        assert poly(x) != 0
    for a in (-27, -8, -1, 0, 1, 8, 27, 64):
        answer = cube(a)
        assert abs(answer**3 - a) < 1e-10, (a, answer)
        # 三次幂严格递增，只有一条实数解分支。
        assert (answer + 1)**3 > a and (answer - 1)**3 < a
    assert 2**2 == (-2)**2 == 4  # 反例：偶次方程不能套用唯一根结论
    for bad in (float("nan"), float("inf"), float("-inf")):
        for fn in (poly, roots, cube):
            try:
                fn(bad)
            except ValueError:
                pass
            else:
                raise AssertionError((fn.__name__, bad))
    print("PASS: seven scenes, factorization, 3 real roots, repeated zero, cubic roots and invalid inputs")


if __name__ == "__main__":
    run()
