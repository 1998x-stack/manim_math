"""Check real lesson's pure sampling function without importing Manim."""
import ast
from pathlib import Path
import numpy as np

source = Path(__file__).resolve().parent.parent / "初中/八年级/第二学期/第二十三章-概率初步/004频率与概率的关系/probability_frequency.py"
tree = ast.parse(source.read_text(encoding="utf-8"))
functions = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "simulate_frequencies"]
assert len(functions) == 1, "simulate_frequencies missing or duplicate"
namespace = {"np": np}
exec(compile(ast.Module(body=functions, type_ignores=[]), str(source), "exec"), namespace)
simulate = namespace["simulate_frequencies"]
state_before = np.random.get_state()
flips, frequencies = simulate(1000, seed=42)
assert np.array_equal(flips, simulate(1000, seed=42)[0])
assert np.array_equal(frequencies, np.cumsum(flips) / np.arange(1, 1001))
assert np.all((0 <= frequencies) & (frequencies <= 1))
assert np.array_equal(simulate(20, probability=0)[0], np.zeros(20))
assert np.array_equal(simulate(20, probability=1)[0], np.ones(20))
state_after = np.random.get_state()
assert state_before[0] == state_after[0] and np.array_equal(state_before[1], state_after[1])
assert state_before[2:] == state_after[2:]
for n in (0, -1, 0.5):
    try:
        simulate(n)
    except ValueError:
        pass
    else:
        raise AssertionError(f"accepted invalid sample count {n}")
for p in (-0.1, 1.1, float("nan")):
    try:
        simulate(10, probability=p)
    except ValueError:
        pass
    else:
        raise AssertionError(f"accepted invalid probability {p}")
print("PASS probability model: reproducibility, counts, frequency, RNG isolation, boundaries")
