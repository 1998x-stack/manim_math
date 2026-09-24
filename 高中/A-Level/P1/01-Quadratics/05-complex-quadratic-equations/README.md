# A-Level Pure Mathematics 1 — 1.5 Solving more complex quadratic equations

**Lesson type:** equations that become quadratic after setting `t=g(x)`; **Scene:** `P1ComplexQuadratics` in `lesson.py`; **format:** silent Manim Community portrait 9:16. Continues the P1 Chapter 1 sequence; source topic is Cambridge International AS & A Level Mathematics, Pure Mathematics 1 (2018), §1.5, printed pp. 15–16 (PDF pp. 27–28). Equations and drawings here are original teaching additions, not copies of source pages or exercises.

## Teaching sequence

Nine beats: recognise `x^4=(x²)^2` → two-stage substitution → factor the auxiliary t quadratic → animated inverse-image numberline → quartic graph and four intercepts → radical substitution → exponential substitution → reject impossible auxiliary roots → independent challenge and recap. Visible equations distinguish the intermediate t roots from original x roots; the original function and its intercepts use the same tested pure-Python model.

## Files

- `lesson.py`: original Manim CE source; permanent A-Level/P1 emblem, 9 teaching beats, scene-level bbox/identity checks.
- `math_model.py`: reusable pure-Python root, domain and original-equation evaluation functions (Manim-independent).
- `test_math.py`: 11 unit tests for normal, zero, repeated, no-real, domain and invalid-leading-coefficient cases.
- `math_spec.md`: assumptions, reasoning, counterexamples/edge conditions and test mapping.
- `storyboard.md`: claim → model → visible object → inspection checklist.

## Local commands (from the topic folder)

```bash
python -m unittest -v test_math.py
python -m py_compile lesson.py math_model.py test_math.py
python -m manim --version
python -m manim render --help # confirm -r width,height convention for your installed version
python -m manim render -r 270,480 --fps 15 lesson.py P1ComplexQuadratics
python -m manim render -r 1080,1920 --fps 30 lesson.py P1ComplexQuadratics
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate -show_entries format=duration -of json PATH_TO_NEW_VIDEO.mp4
```

Needs Manim Community Edition, a functional LaTeX environment and a local CJK font (`Noto Sans CJK SC` or update `CJK`). From the repository's `.codex/skills/manim-video-production` folder additionally run `python scripts/audit_scene.py /absolute/path/to/lesson.py --json` and resolve `ERROR`s. Perform a true low-quality render and inspect opening, variable-tracker intermediate positions, all equations, plot/roots and final frame before publishing a video. The Python `checkpoint` verifies only registered actual scene objects at calls, not a whole animation.

**Status:** Python mathematical tests, syntax/static checks can be run without Manim. No rendered video is bundled or claimed; runtime/render/representative-frame/media checks must be performed where Manim is available. No copyrighted textbook images/third-party media/music included.
