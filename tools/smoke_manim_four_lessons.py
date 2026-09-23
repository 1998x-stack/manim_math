#!/usr/bin/env python3
"""Four real-course, no-Manim smoke checks. Does not claim video/visual acceptance."""
from __future__ import annotations

import ast
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/source/manim-video-production/scripts"
AREA_ROOT = ROOT / "小学/五年级/第一学期/第五章-几何小实践"
TRIG = ROOT / "高中/高一/第二学期/第六章-三角函数/003函数y=Asin(ωx+φ)的图像与性质"
PROB = ROOT / "初中/八年级/第二学期/第二十三章-概率初步/004频率与概率的关系"
COURSES = (
    ("equal_area", AREA_ROOT / "005等面积法-同底等高", "lesson.py", "EqualAreaMovingApex", "test_area_model.py", True),
    ("butterfly", AREA_ROOT / "006等面积法-梯形蝴蝶模型", "lesson.py", "TrapezoidButterflyArea", "test_area_model.py", True),
    ("trigonometry", TRIG, "003_函数y=Asin(ωx+φ)的图像与性质.py", "TrigonometricTransform", "verify_geometry.py", False),
    ("probability", PROB, "probability_frequency.py", "ProbabilityFrequency", None, False),
)


def probability_math_test() -> None:
    """Evaluate only the project's pure sampling function; never import Manim."""
    import numpy as np

    source = (PROB / "probability_frequency.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                 and node.name == "simulate_frequencies"]
    assert len(functions) == 1, "course's pure sampling function missing"
    module = ast.Module(body=functions, type_ignores=[])
    namespace = {"np": np}
    exec(compile(module, str(PROB / "probability_frequency.py"), "exec"), namespace)
    simulate = namespace["simulate_frequencies"]
    # Independently check model output, reproducibility, edge probabilities and no global RNG pollution.
    previous = np.random.get_state()
    flips, freq = simulate(1000, seed=42)
    assert np.array_equal(flips, simulate(1000, seed=42)[0])
    assert np.array_equal(freq, np.cumsum(flips) / np.arange(1, 1001))
    assert len(freq) == 1000 and np.all((freq >= 0) & (freq <= 1))
    assert np.array_equal(simulate(20, probability=0)[0], np.zeros(20))
    assert np.array_equal(simulate(20, probability=1)[0], np.ones(20))
    after = np.random.get_state()
    assert previous[0] == after[0] and np.array_equal(previous[1], after[1])
    assert previous[2:] == after[2:]
    for bad_n in (0, -1, 0.5):
        try:
            simulate(bad_n)
        except ValueError:
            pass
        else:
            raise AssertionError(f"invalid sample count accepted: {bad_n}")
    for bad_p in (-0.1, 1.1, float("nan")):
        try:
            simulate(10, probability=bad_p)
        except ValueError:
            pass
        else:
            raise AssertionError(f"invalid probability accepted: {bad_p}")
    print("PASS probability: 1000 trials, reproducibility, cumulative frequency, RNG isolation, edge cases")


def main() -> int:
    failures = []
    with tempfile.TemporaryDirectory(prefix="manim-course-smoke-") as work:
        for name, folder, script, scene, math_test, has_spec in COURSES:
            command = [sys.executable, str(SKILL / "production_check.py"),
                       str(folder / script), scene, "--out-dir", work]
            if math_test:
                command.extend(["--math-test", str(folder / math_test)])
            elif name == "probability":
                command.extend(["--math-test", str(Path(__file__).resolve()), "--probability-test"])
            result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
            # --probability-test has to be a separate stand-alone call, not a value passed to production_check.
            if name == "probability":
                command = [sys.executable, str(SKILL / "production_check.py"),
                           str(folder / script), scene, "--out-dir", work]
                result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
            try:
                report = json.loads(result.stdout)
                checks = report["checks"]
                valid = (result.returncode == 0 and report["status"] == "partial"
                         and checks["syntax"]["status"] == "pass"
                         and checks["ast"]["status"] == "pass"
                         and checks["manim_render"]["status"] == "not_run")
                if math_test:
                    valid = valid and checks["math_test"]["status"] == "pass"
                if not valid:
                    failures.append(f"{name}: production gate failed: {report}")
                print(f"{name}: syntax={checks['syntax']['status']} ast={checks['ast']['status']} "
                      f"math={checks['math_test']['status']} render={checks['manim_render']['status']} "
                      f"overall={report['status']}")
            except (ValueError, KeyError) as exc:
                failures.append(f"{name}: invalid report {exc}: {result.stdout} {result.stderr}")
            if has_spec:
                spec = subprocess.run([sys.executable, str(SKILL / "verify_geometry.py"),
                                       str(folder / "geometry_spec.json")],
                                      capture_output=True, text=True, encoding="utf-8")
                print(f"{name}: geometry_spec={'pass' if spec.returncode == 0 else 'fail'}")
                if spec.returncode:
                    failures.append(f"{name}: {spec.stdout} {spec.stderr}")
        try:
            probability_math_test()
        except Exception as exc:
            failures.append(f"probability math: {type(exc).__name__}: {exc}")
    if failures:
        for failure in failures:
            print("FAIL", failure, file=sys.stderr)
        return 1
    print("PASS: four course source/math smoke checks; actual Manim rendering NOT RUN")
    return 0


if __name__ == "__main__":
    if "--probability-test" in sys.argv:
        probability_math_test()
    else:
        sys.exit(main())
