"""无理方程的定义域、平方候选解和原式检验；不依赖 Manim。"""
import ast
from math import isclose, isfinite, sqrt
from pathlib import Path

path = Path(__file__).with_name("irrational_equation_animation.py")
source = path.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(path))
namespace = {"isfinite": isfinite, "isclose": isclose, "sqrt": sqrt}
for name in ("radical_defined", "necessary_sign_condition", "squared_residual",
             "original_residual", "validated_solutions"):
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    exec(compile(ast.Module(body=[fn], type_ignores=[]), str(path), "exec"), namespace)
defined = namespace["radical_defined"]
necessary = namespace["necessary_sign_condition"]
squared = namespace["squared_residual"]
original = namespace["original_residual"]
solutions = namespace["validated_solutions"]


def run():
    assert any(isinstance(n, ast.ClassDef) and n.name == "IrrationalEquation"
               for n in tree.body)
    for index, suffix in enumerate(("hook", "definition", "four_steps", "square_both_sides",
                                    "solve_quadratic", "verify", "outro"), 1):
        assert f"def scene{index}_{suffix}(" in source
    assert not defined(-0.50001) and defined(-0.5) and defined(0)
    assert not necessary(-0.5) and not necessary(0) and necessary(1)
    assert not necessary(-1) and necessary(4)
    assert squared(0) == squared(4) == 0
    for x in (-10, -0.5, 0, 1, 2, 3, 4, 10):
        assert squared(x) == x * (x - 4)
    assert original(0) == 2  # 根式在 0 有定义，但左侧 1、右侧 -1
    assert original(4) == 0  # 左侧 3、右侧 3
    assert solutions() == (4,)
    for x in (-1, -0.50001):
        try:
            original(x)
        except ValueError:
            pass
        else:
            raise AssertionError(f"根号内负数应拒绝: {x}")
    for bad in (float("nan"), float("inf"), float("-inf")):
        for fn in (defined, squared, original):
            try:
                fn(bad)
            except ValueError:
                pass
            else:
                raise AssertionError((fn.__name__, bad))
    print("PASS: seven scenes, radical/sign domain, squared candidates 0/4 and valid original root 4")


if __name__ == "__main__":
    run()
