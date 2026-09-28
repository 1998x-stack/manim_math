"""函数零点与严格/非严格不等式回归；独立于 manim。"""
import ast
from math import isfinite
from pathlib import Path

path = Path(__file__).with_name("linear_function_equation_inequality.py")
source = path.read_text(encoding="utf-8")
tree = ast.parse(source, filename=str(path))
namespace = {"isfinite": isfinite}
for name in ("zero_of", "relation_holds", "visible_interval"):
    function = next(node for node in tree.body
                    if isinstance(node, ast.FunctionDef) and node.name == name)
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(path), "exec"), namespace)
root_of = namespace["zero_of"]
holds = namespace["relation_holds"]
interval = namespace["visible_interval"]


def run():
    assert any(isinstance(n, ast.ClassDef) and n.name == "LinearFunctionEquationInequality"
               for n in tree.body)
    for method in ("show_opening", "setup_coordinate_system", "show_equation_solution",
                   "show_inequality_positive", "show_inequality_negative", "show_summary",
                   "show_example", "show_outro"):
        assert f"def {method}(" in source
    assert root_of(2, -3) == 1.5
    assert holds(2, -3, 1.5, "=")
    assert not holds(2, -3, 1.5, ">") and not holds(2, -3, 1.5, "<")
    assert holds(2, -3, 1.5, ">=") and holds(2, -3, 1.5, "<=")
    for k, b in ((2, -3), (-2, 3), (1, 0), (-1, 0), (3, -4)):
        root = root_of(k, b)
        assert abs(k * root + b) < 1e-12
        for x in (root - 1, root + 1):
            y = k * x + b
            assert holds(k, b, x, ">") == (y > 0)
            assert holds(k, b, x, "<") == (y < 0)
            assert holds(k, b, x, ">=") == (y >= 0)
            assert holds(k, b, x, "<=") == (y <= 0)
            assert not holds(k, b, x, "=")
        left, right = interval(k, b)
        assert -1 < left < right < 4
        for x in (left, (left + right) / 2, right):
            assert -5 < k * x + b < 5
    for invalid in ((0, 1), (float("nan"), 1), (2, float("inf"))):
        for function in (root_of, interval):
            try:
                function(*invalid)
            except ValueError:
                pass
            else:
                raise AssertionError((function.__name__, invalid))
    for relation in ("!=", "unknown"):
        try:
            holds(2, -3, 1.5, relation)
        except ValueError:
            pass
        else:
            raise AssertionError(relation)
    print("PASS: 8 scenes, 5 parameter sets, all sign relations, inclusive root, clipped endpoints")


if __name__ == "__main__":
    run()
