# Storyboard · A-Level Pure Mathematics 1 §1.6

**Source and scope:** Cambridge P1 Coursebook (2018), §1.6, printed pp.17–20; original examples and explanations in `math_spec.md`. **Format:** 9:16, bilingual on-screen labeling, silent. **Goal:** see why the coefficient's sign determines the extremum, calculate the vertex/axis, sketch graph with intercepts, handle domain limits.

| Shot / estimated time | learning_fact / claim | data -> visual objects / transitions | check |
|---|---|---|---|
| 1 / 7 s | coefficient sign changes up/down opening | original formula cards and arrows, persistent course header | distinguish max from min; label placement |
| 2 / 10 s | `f=x²-4x+1=(x-2)²-3`; square nonnegative | sequential MathTex, conclusion panel | algebra verified by model; screen readability |
| 3 / 9 s | parabola `y=(x-h)²+k` follows `(h,k)` | `h,k` trackers -> graph, vertex, dashed axis via same values; start h=k=0, end h=2,k=-3 | initial / final explicit checkpoints; intermediate requires real render inspection |
| 4 / 9 s | `f(1)=f(3)=-2`, vertex (2,-3), axis x=2 | model -> Axes.plot and symmetric dots, dashed axis | x/y conversion by Axes.c2p; no mismatched labels |
| 5 / 11 s | `h=-b/(2a)`, `k=c-b²/(4a)` | algebraic completion sequence & sign rule | `a≠0`, exact identities tests |
| 6 / 9 s | `g=4-(x-3)²`: max 4 at x=3 | model -> graph, vertex, two zeros, symmetry axis | zero positions (1,5); curve visible at endpoints |
| 7 / 10 s | sketch `f`: vertex, y-intercept, exact x-intercepts | model-derived roots -> dots, exact symbolic label, y-dot | numerical dots match exact text and graph |
| 8 / 10 s | `f` on [3,4] has min -2 and max 1 | full curve muted, restricted segment highlighted, endpoints model | vertex x=2 excluded; finite endpoints only |
| 9 / 12 s | practice `q=5-(x-2)²`, max 5 at x=2 | question -> pause -> formula, vertex, maximum | check via PRACTICE; answer appears only after pause |

Lifecycle: `brand_objects` create once / retain all shots. Each shot's title, graphs, points, labels and panels are created during that shot and removed via `clear_shot` before the next. Shot 3's live `graph`, `vertex` and `symmetry` remain as the same scene objects while trackers change; no `ReplacementTransform` references are reused. Shot 3's `Transform(start, finish)` retains **start** as the on-screen object. The graph/point/axis are explicitly registered for beginning and ending checks; intermediary position correctness must be reviewed in actual frames.

## Validation evidence

| layer | status | required evidence |
|---|---|---|
| math claims / unit tests | pass | run 12 tests in `test_math.py` |
| Python syntax | pass | `python -m py_compile` |
| skill AST audit | not_run | requires access to `scripts/audit_scene.py` from the repo's Skill |
| actual Manim runtime checkpoints | blocked | Manim package not present here |
| preview & formal render | blocked | Manim package not present here |
| frame / font / TeX inspection | not_run | requires new rendered media |
| ffprobe & audio review | not_run | no rendered MP4; intended audio is none |
