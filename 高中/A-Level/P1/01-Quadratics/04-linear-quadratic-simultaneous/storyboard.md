# A-Level P1 §1.4 — Teaching storyboard

- **Reference:** user's Cambridge P1 (2018), §1.4, printed pp. 11–14 (PDF pp. 23–26). Includes an original parabola/line example, dynamic discriminant, original circle example and practice.
- **Audience/prerequisites:** P1 students familiar with linear equations, quadratics, §1.1 factorisation and §1.3 discriminant.
- **Scene:** `P1LinearQuadratic`, 9:16, muted dark board; fixed A-Level / PURE MATHEMATICS 1 / P1 branding, Chinese Text + mathematical MathTex only; silent, estimated ~90–120 seconds with pauses, not rigid timing.
- **Object data lineage:** every plotted common point is computed by `math_model.intersections` or `circle_line_points`, transformed by the current `Axes.c2p`; equations and labels use the same coefficients. Explicit static scene checkpoints do not cover every moving frame.

| Beat | learning_fact / mathematical claim | Visual objects and state transitions | Checkpoint / estimated time |
|---|---|---|---|
| 01 Introduction | Common solution means same ordered pair satisfies both equations. | Persistent brand stays; two color-coded cards/equations created; arrows converge on `(x,y)` question, then clear. | Equations/prompt visible; 9–12 s. |
| 02 Graph | Main line and parabola meet at `(0,1)` and `(3,4)`. | Axes → teal parabola → gold line → two green dots and paired labels; all coordinates from same model; clear. | Graph, points, labels register within safe zone; 12–15 s. |
| 03 Substitution | `x²−2x+1=x+1 → x²−3x=0 → x=0 or 3`. | Progressive stacked MathTex derivation; hold on factorisation; clear. | Valid equation in every row; 11–14 s. |
| 04 Back-substitution | y=1 for x=0 and y=4 for x=3; verify original quadratic. | Two side-by-side cards; result framed as ordered pairs; explicit original-curve check; clear. | Checks correspond to same branches; 10–13 s. |
| 05 Dynamic intersections | k=1 / −5/4 / −2 ⇒ 2 / 1 / 0 real intersections for same parabola. | Fixed Axes and curve; `ValueTracker` drives `always_redraw` line and dots from one model. Labels change **only after** each motion stops. | Static states k=1, −5/4, −2: discriminants 9,0,−3. Review midframes for geometry/overlap; 14–18 s. |
| 06 General quadratic curve | x²+y²=5 and y=x+1 produce 2 common points. | Equal-scale axes; accurately mapped parametric circle, line, dots; eliminate y, display solution pairs; clear. | (-2,-1) and (1,2), original equalities checked by math test; 12–16 s. |
| 07 Common errors | Return `(x,y)`, check both original equations, treat vertical line separately. | Four distinct textual+math cards; no speculative points; clear. | All cards within portrait safe region; 9–11 s. |
| 08 Practice & recap | `x²−2x+2=2x−1` gives `(1,1)` and `(3,5)`. | Student pause → substitute → factor → reveal two pairs; final takeaway; clear while brand persists. | Independent test + end frame visibility; 12–15 s. |

## Object lifetime and checks

Persistent brand created once and excluded from `wipe()`. Transient equation groups, axes, graphs, dots, labels and cards created per beat and faded with the same current object references. The sweep's dynamic `moving_line` and `moving_points` stay visible throughout sweep and are removed before the next beat. `ReplacementTransform(label, current)` updates the label variable to the current visible object. Mathematical model is independent of Scene; animated samples are **illustrative**, while algebra establishes the general statements.

| Validation layer | Status here | Evidence / next step |
|---|---|---|
| Math claims | pass | 10 independent pure-Python tests, plus algebraic derivations in `math_spec.md`. |
| Python syntax | pass | `python -m py_compile lesson.py math_model.py test_math.py`. |
| Skill AST audit | not_run | Execute `scripts/audit_scene.py` in the original Skill directory when available. |
| Runtime checkpoints | not_run | Embedded checks exist, but require a real Manim render. |
| Geometry JSON | N/A | Function coordinate graph, not a standalone geometry specification. |
| Manim render / font / LaTeX | not_run | Manim package unavailable in creation environment. |
| Frame review / ffprobe / audio | not_run | No video rendered; original scene is silent. |
