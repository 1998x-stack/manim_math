#!/usr/bin/env python3
"""Exercise production_check on four real courses without claiming render success."""
from __future__ import annotations

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
    ("trigonometry", TRIG, "003_函数y=Asin(ωx+φ)的图像与性质.py", "TrigonometricTransform", "verify_geometry.py", False),
    ("probability", PROB, "probability_frequency.py", "ProbabilityFrequency", "../../../../../tools/test_probability_frequency_model.py", False),
)


def main() -> int:
    failures = []
    with tempfile.TemporaryDirectory(prefix="manim-four-lessons-") as work:
        for name, folder, filename, scene, math_test, geometry in COURSES:
            test = ROOT / "tools/test_probability_frequency_model.py" if name == "probability" else folder / math_test
            command = [sys.executable, str(SKILL / "production_check.py"),
                       str(folder / filename), scene, "--math-test", str(test), "--out-dir", work]
            result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
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
                checked = subprocess.run([sys.executable, str(SKILL / "verify_geometry.py"),
                                          str(folder / "geometry_spec.json")],
                                         capture_output=True, text=True, encoding="utf-8")
                print(f"{name}: geometry_spec={'pass' if checked.returncode == 0 else 'fail'}")
                if checked.returncode:
                    failures.append(f"{name}: geometry check {checked.stdout} {checked.stderr}")
    for item in failures:
        print("FAIL: " + item, file=sys.stderr)
    if failures:
        return 1
    print("PASS four real-course syntax/AST/math gates; Manim render and visual review NOT RUN")
    return 0


if __name__ == "__main__":
    sys.exit(main())
