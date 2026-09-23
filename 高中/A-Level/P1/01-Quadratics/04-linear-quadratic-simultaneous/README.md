# A-Level Pure Mathematics 1 · 1.4 — Solving simultaneous equations

**Lesson:** one linear equation + one quadratic equation. **Scene:** `P1LinearQuadratic` in `lesson.py`. Placement in main repository: `高中/A-Level/P1/01-Quadratics/04-linear-quadratic-simultaneous/`.

Based on the user's Cambridge International AS & A Level Mathematics: Pure Mathematics 1 Coursebook (2018), §1.4, printed pp. 11–14 (PDF pp. 23–26). Original examples/animations are supplementary and not a reproduction of textbook pages or copyrighted exercises.

## Teaching sequence

Eight beats: introduction → graph with two common points → substitution and factorisation → recover y/check both equations → animated secant/tangent/no-intersection cases → circle as a general quadratic curve → common errors including vertical lines → independent practice.

The worked example is `y=x²−2x+1` with `y=x+1`: the solutions are `(0,1)` and `(3,4)`. A second example uses a circle `x²+y²=5` and the same line: `(-2,-1)`, `(1,2)`. The independent practice uses `y=x²−2x+2` and `y=2x−1`: `(1,1)` and `(3,5)`.

## Files and running

- `lesson.py`: original portrait 9:16 Manim Community scene, course label and sampled real-Mobject safety assertions.
- `math_model.py`: independent Fraction-based substitution, discriminant and common-coordinate model.
- `test_math.py`: 10 pure-Python unit tests including tangent, disjoint and conic cases.
- `math_spec.md`: claims, proof, edge cases and plot-domain contract.
- `storyboard.md`: per-beat visuals, animation lifecycle and honest verification states.

```bash
cd 高中/A-Level/P1/01-Quadratics/04-linear-quadratic-simultaneous
python -m unittest -v test_math.py
python -m py_compile lesson.py math_model.py test_math.py
python -m manim --version
python -m manim render --help  # verify width,height order in your installed version
python -m manim render -r 270,480 --fps 15 lesson.py P1LinearQuadratic
python -m manim render -r 1080,1920 --fps 30 lesson.py P1LinearQuadratic
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate -show_entries format=duration -of json PATH_TO_RENDERED_MP4
```

Manim CE, LaTeX and the `Noto Sans CJK SC` font (or an edited installed font) are needed for rendering. The original scene contains no narration/music. Do not republish as a verified MP4 before a real preview, representative frame inspection (especially tracker midframes and label placement) and `ffprobe` result. Runtime checks only cover the registered objects at explicit calls.
