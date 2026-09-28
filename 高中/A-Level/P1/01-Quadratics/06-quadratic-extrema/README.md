# A-Level P1 §1.6 — Maximum and minimum values of a quadratic function

**Scene:** `P1QuadraticExtrema` in `lesson.py`. Original Manim Community 9:16 silent lesson with a persistent `A-Level / PURE MATHEMATICS 1 / P1` header. It follows the user's Cambridge *Pure Mathematics 1* (2018) §1.6, printed pp.17–20 / PDF pp.29–32, but uses new examples/figures rather than copying textbook pages.

The nine shots explain sign of a, completed-square vertex form, a live translated parabola and symmetry axis, symmetric points, general vertex formula, concave-down maximum, graph sketch with x/y intercepts, a restricted interval (explicit original extension), and independent practice.

## Files

- `lesson.py`: the animation. Chinese is `Text` using a configurable CJK font, mathematical expressions are `MathTex`.
- `math_model.py`: exact `fractions.Fraction` calculations of vertex, extrema, symmetry, discriminant and interval endpoints; no Manim dependency.
- `test_math.py`: 12 standalone tests for normal, boundary, degeneracy and restricted-domain cases.
- `math_spec.md`: every mathematical claim, domain, proof, and edge case.
- `storyboard.md`: shot-by-shot model-to-visual mapping and explicit verification status.

## Run

Install Manim Community, a working LaTeX toolchain, and a Chinese font (default `Noto Sans CJK SC` may need replacing in `lesson.py`). From this directory:

```bash
python -m unittest -v test_math.py
python -m py_compile lesson.py math_model.py test_math.py
python -m manim --version
python -m manim render --help
python -m manim render -r 270,480 --fps 15 lesson.py P1QuadraticExtrema
python -m manim render -r 1080,1920 --fps 30 lesson.py P1QuadraticExtrema
```

Check CLI resolution order in the **installed** Manim version. Run the repo Skill's `scripts/audit_scene.py` against `lesson.py`; use its runtime probe for additional scene-level identity and bbox checks. After rendering, inspect opening, tracking midpoint/end, both graph-sketch scenes, restricted interval and answer reveal. Verify real output dimensions, duration, frame rate and audio with `ffprobe`; never label unrendered code a finished video.

**Preparation evidence:** mathematics tests and syntax checked locally. Manim absent in preparation environment: no successful Scene execution, TeX compilation, video render, frame review or final MP4. No copyrighted textbook scans, third-party music, or finished video in this package.
