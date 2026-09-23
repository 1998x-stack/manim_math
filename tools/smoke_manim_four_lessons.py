#!/usr/bin/env python3
"""Run source/math checks on four real courses; distinguish missing render from passing."""
from __future__ import annotations

import ast
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/source/manim-video-production/scripts"
AREAS = ROOT / "小学/五年级/第一学期/第五章-几何小实践"
TRIG = ROOT / "高中/高一/第二学期/第六章-三角函数/003函数y=Asin(ωx+φ)的图像与性质"
PROB = ROOT / "初中/八年级/第二学期/第二十三章-概率初步/004频率与概率的关系"
COURSES = (
    ("equal_area", AREAS / "005等面积法-同底等高", "lesson.py", "EqualAreaMovingApex", "test_area_model.py", True),
    ("butterfly", AREAS / "006等面积法-梯形蝴蝶模型", "lesson.py", "TrapezoidButterflyArea", "test_area_model.py", True),
    ("probability", PROB, "probability_frequency.py", "ProbabilityFrequency", "test_probability_frequency_model.py", False),
)


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")


def check_trigonometry() -> list[str]:
    """Actual Chinese Scene class currently cannot pass production_check's ASCII-only CLI gate."""
    failures = []
    source = TRIG / "003_函数y=Asin(ωx+φ)的图像与性质.py"
    actual_class = "函数yAsinωxφ的图像与性质"
    parsed = ast.parse(source.read_text(encoding="utf-8"))
    if not any(isinstance(node, ast.ClassDef) and node.name == actual_class for node in parsed.body):
        failures.append("trigonometry: true Unicode Scene class missing")
    for label, command in (
        ("syntax", [sys.executable, "-m", "py_compile", str(source)]),
        ("ast", [sys.executable, str(SKILL / "audit_scene.py"), str(source), "--json"]),
        ("math", [sys.executable, str(TRIG / "verify_geometry.py")]),
    ):
        result = run(command)
        if result.returncode:
            failures.append(f"trigonometry {label}: {result.stdout} {result.stderr}")
        elif label == "ast":
            payload = json.loads(result.stdout)
            print(f"trigonometry: ast=pass warnings={payload['warnings']}")
        else:
            print(f"trigonometry: {label}=pass")
    # Explicitly report, never treat an untested production gate or render as pass.
    print("trigonometry: production_gate=BLOCKED (existing ASCII-only Scene name validation); render=not_run")
    return failures


def main() -> int:
    failures = []
    with tempfile.TemporaryDirectory(prefix="manim-four-lessons-") as work:
        for name, folder, filename, scene, math_test, geometry in COURSES:
            test = ROOT / "tools/test_probability_frequency_model.py" if name == "probability" else folder / math_test
            command = [sys.executable, str(SKILL / "production_check.py"),
                       str(folder / filename), scene, "--math-test", str(test), "--out-dir", work]
            result = run(command)
            try:
                pointer = json.loads(result.stdout)
                report = json.loads(Path(pointer["report"]).read_text(encoding="utf-8"))
                checks = report["checks"]
                expected = {"syntax": "pass", "ast": "pass", "math_test": "pass",
                            "manim_render": "not_run", "frame_review": "not_run"}
                ok = (result.returncode == 0 and report["status"] == "partial" and
                      all(checks[item]["status"] == status for item, status in expected.items()))
                print(f"{name}: " + " ".join(f"{k}={checks[k]['status']}" for k in expected) +
                      f" overall={report['status']} AST_warnings={checks['ast'].get('warnings', 0)}")
                if not ok:
                    failures.append(f"{name}: gate mismatch: {report}")
            except (ValueError, KeyError, OSError) as exc:
                failures.append(f"{name}: report error {exc}; stdout={result.stdout}; stderr={result.stderr}")
            if geometry:
                checked = run([sys.executable, str(SKILL / "verify_geometry.py"),
                               str(folder / "geometry_spec.json")])
                print(f"{name}: geometry_spec={'pass' if checked.returncode == 0 else 'fail'}")
                if checked.returncode:
                    failures.append(f"{name}: geometry check {checked.stdout} {checked.stderr}")
        failures.extend(check_trigonometry())
    for item in failures:
        print("FAIL: " + item, file=sys.stderr)
    if failures:
        return 1
    print("PASS: four courses' syntax/AST/math and two geometry specs. "
          "Three production gates partial; Unicode Scene gate blocked; no Manim renders performed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
