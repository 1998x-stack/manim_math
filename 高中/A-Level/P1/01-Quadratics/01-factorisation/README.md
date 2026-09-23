# A-Level P1 / 1.1 — Factorisation (Manim Community)

An original nine-shot portrait animation for **Pure Mathematics 1 (P1), Chapter 1 §1.1**, with bilingual captions, area decomposition, algebraic factoring, zero-product branches, a parabola, a cancellation counterexample and a practice question.

Files: `lesson.py` (class `P1Factorisation`), `math_model.py` (pure math model), `test_math.py` (independent lesson tests), `math_spec.md` (claims, assumptions and counterexamples), `storyboard.md` (shot-by-shot production plan).

## Prerequisites

Manim Community (not ManimGL), LaTeX / dvisvgm, Noto Sans CJK SC or edit the `FONT` constant. Ensure import works using `python -m manim --version`. The lesson is informed by Cambridge P1 §1.1 but uses original visuals and worked examples; the textbook itself is not included in this repository.

## Run

From **this** directory:

```bash
python test_math.py
python -m py_compile lesson.py math_model.py test_math.py
python -m manim --version
python -m manim render --help
python -m manim render -r 270,480 --fps 15 lesson.py P1Factorisation
python -m manim render -r 1080,1920 --fps 30 lesson.py P1Factorisation
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate -show_entries format=duration -of json <actual-mp4-path>
```

The script does not hardcode pixel width/height or add audio. After rendering, inspect the initial, middle, overlapping strips, graph labels, highlighted roots, and final frames for visual correctness. Do not publish an MP4 before a real render and media check.

**Source vs extension:** Cambridge P1 Chapter 1 §1.1 motivates rearranging to zero, factorising, applying the zero-product rule, and checking answers. The particular `x²−5x+6=0` example, geometric strip model, graph animation, mini-practice and layouts are original explanations. The diagram represents actual rectangular areas only for x≥3; the identity is valid for all real x.

**Current verification:** standalone mathematical checks and Python syntax compile passed in the source-preparation environment. Manim rendering, live Scene checkpoints, representative-frame review and final MP4/ffprobe verification have **not** been run; no video is committed.
