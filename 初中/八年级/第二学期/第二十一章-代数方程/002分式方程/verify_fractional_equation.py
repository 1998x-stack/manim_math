"""分式方程纯数学回归：区分禁值、整式候选值和原方程解。"""
import ast
from math import isfinite
from pathlib import Path

path = Path(__file__).with_name("fractional_equation_animation.py")
source = path.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(path))
namespace = {"isfinite": isfinite}
for name in ("lcd_value", "original_defined", "cleared_equation_residual",
             "original_equation_residual", "equation_solutions"):
    fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
    exec(compile(ast.Module(body=[fn], type_ignores=[]), str(path), "exec"), namespace)
lcd = namespace["lcd_value"]
defined = namespace["original_defined"]
cleared = namespace["cleared_equation_residual"]
residual = namespace["original_equation_residual"]
solutions = namespace["equation_solutions"]


def run():
    assert any(isinstance(n, ast.ClassDef) and n.name == "FractionalEquation"
               for n in tree.body)
    for index, name in enumerate(("hook", "definition", "four_steps", "remove_denom",
                                  "solve_integral", "verify_extraneous", "outro"), 1):
        assert f"def scene{index}_{name}(" in source
    assert lcd(1) == lcd(-1) == 0
    assert not defined(1) and not defined(-1)
    assert cleared(1) == 0
    assert cleared(-1) == -2  # 禁值 -1 不是本例的增根
    assert solutions() == ()
    for x in (-4, -3, -2, 0, 2, 3, 4):
        assert defined(x) and lcd(x) != 0
        assert abs(residual(x) * lcd(x) - cleared(x)) < 1e-10, x
        assert cleared(x) != 0 and residual(x) != 0
    for bad in (1, -1):
        try:
            residual(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"禁值不得代回原方程: {bad}")
    for bad in (float("nan"), float("inf"), float("-inf")):
        for fn in (lcd, cleared):
            try:
                fn(bad)
            except ValueError:
                pass
            else:
                raise AssertionError((fn.__name__, bad))
    # 对比另一道确有合法解的分式方程：1/(x-1)=2/(x+1) 得 x=3。
    assert 3 not in (-1, 1)
    assert 1 / (3 - 1) == 2 / (3 + 1)
    print("PASS: seven scenes, domain exclusions ±1, candidate x=1 rejected, no original solution")


if __name__ == "__main__":
    run()
