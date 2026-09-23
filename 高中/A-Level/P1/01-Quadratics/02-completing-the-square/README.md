# A-Level · Pure Mathematics 1 — 1.2 Completing the square

This is the second independent Manim Community lesson under Chapter 1 Quadratics. The persistent in-frame **A-Level / PURE MATHEMATICS 1 / P1** marker intentionally matches lesson 1.1.

## Course scope

The supplied Cambridge International AS & A Level Mathematics *Pure Mathematics 1 Coursebook* (2018), §1.2, introduces reverse perfect-square expansion, coefficient comparison, and solving quadratics (including exact radicals). Original lesson examples are `x²+6x+5=(x+3)²-4`, `2x²-8x+3=2(x-2)²-5`, the positive-definite case and `x²-4x-1=0` practice. No textbook page is embedded.

Eight instructional shots: introduction → reverse expansion → colored 5×5 tile completion (x=2) → quadratic solving with ± → roots and vertex on parabola → non-monic form → no-real-root/maximum contrast → practice and recap.

## Contents

- `lesson.py`: runnable `P1CompletingTheSquare` Manim Community `Scene`, 9:16 logic, no hard-coded pixel resolution and no audio.
- `math_model.py`: independent exact-fraction mathematics, zero-restricted model and deterministic geometric counts.
- `test_math.py`: lesson-specific tests with normal, fractional, invalid and exceptional cases.
- `math_spec.md`: assumptions, proofs and visualization limits.
- `storyboard.md`: sequence, object data source and test status.

## Usage

```bash
python -m unittest -v test_math.py
python -m py_compile lesson.py math_model.py test_math.py
python -m manim --version
python -m manim render --help
python -m manim render -r 270,480 --fps 15 lesson.py P1CompletingTheSquare
python -m manim render -r 1080,1920 --fps 30 lesson.py P1CompletingTheSquare
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate -show_entries format=duration -of json <actual-output.mp4>
```

Requires Manim Community, LaTeX, `ffprobe` for final inspection, and a CJK font (default `Noto Sans CJK SC` on the authoring machine; adjust `FONT` if absent). On-screen captions are silent and paced for individual reading. Review actual keyframes before using a production render. Source tests and syntax checks are NOT a substitute for TeX compilation or visual acceptance.
