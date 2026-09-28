# A-Level P1 §1.3 — The Quadratic Formula

Next lesson after §1.2 Completing the Square in `高中/A-Level/P1/01-Quadratics/`.

**Scene:** `P1QuadraticFormula` · **source:** `lesson.py` · **frame:** 9:16, no audio. This course is grounded in the user's Cambridge *Pure Mathematics 1* Coursebook (2018), §1.3, printed page 10 / PDF page 22. The derivation order and the need for `a≠0` follow that section; example coefficients, tiling, graph and practice are original teaching additions, not copies of textbook exercises.

## Learning sequence

9 shots: transition from factorisation; recap square completion; illustrative colored 4×4 area tiles; algebraic derivation; worked example `2x²−2x−1=0`; graph and two roots; live discriminant family (2, 1, 0 real roots); exact vs 3-significant-figure answers and cautions; original practice `3x²+2x−2=0`.

## Files

- `math_model.py`: pure standard-library Fraction-based model (no Manim dependency).
- `test_math.py`: 8 lesson-specific tests with normal, boundary, domain and degeneracy cases.
- `lesson.py`: original 9:16 Manim Community scene and fixed-state runtime safety checks.
- `math_spec.md`: mathematical assumptions, derivation and applicability notes.
- `storyboard.md`: claims, visual states, transitions and evidence checklist.

## Commands

From this folder, with Manim Community, TeX and CJK font available:

```bash
python -m unittest -v test_math.py
python -m py_compile lesson.py math_model.py test_math.py
python -m manim --version
python -m manim render --help  # check -r resolution ordering for installed version
python -m manim render -r 270,480 --fps 15 lesson.py P1QuadraticFormula
python -m manim render -r 1080,1920 --fps 30 lesson.py P1QuadraticFormula
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate -show_entries format=duration -of json PATH_TO_NEW_VIDEO.mp4
```

The `-r W,H` commands follow Manim Community's recent CLI convention; confirm using your installed version. For the specified production Skill, additionally run `python scripts/audit_scene.py /absolute/path/lesson.py --json` from its skill directory, plus real preview rendering, representative-frame inspection and actual output media probing. The built-in `checkpoint` only checks registered visible objects at explicitly called moments; it does not certify the full video or guarantee there is no overlap.

**Verification in creation environment:** 8 standard-library mathematical tests and Python syntax checks passed; `manim` package not installed, so no actual Scene render / frame review / mp4 was performed. The provided animation is **source code, not a verified finished video**. No external music, copyrighted textbook pages or media files are included.
