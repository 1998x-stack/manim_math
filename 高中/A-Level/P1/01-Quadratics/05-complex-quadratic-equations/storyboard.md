# Storyboard — P1 §1.5 (original 9:16 animation)

Nine distinct silent lesson beats. Persistent header: `A-Level / PURE MATHEMATICS 1 / P1` and footer: §1.5. Source of numerical facts is `math_model.py`; each MathTex string is an algebraic expression, Chinese captions are separate Manim Text objects. `chrome_mobs` survives all wipes; nonchrome objects are removed at the next transition.

| Beat | Learning fact / claim | Screen object / creation-update-removal | Checkpoint, visual inspection |
| --- | --- | --- | --- |
| 1. Hook | `x⁴=(x²)²` exposes a hidden quadratic | gold quartic equation; teal equivalent fourth-power shape, callout | complete heading, equation, callout within safe portrait area |
| 2. Two-stage map | `x→t=x²→t²−5t+4`; t must lie in range | x/t/p formulas, arrows, derivation card, domain note | arrows not crossing formula glyphs, main text legible |
| 3. Solve t | `t²−5t+4=0` gives t=1 or4, and t≥0 | sequential MathTex rows, range card | show both t roots, domain not visually detached |
| 4. Inverse-image map | t=1 ↔ x=±1; t=4 ↔ x=±2 | numberline, two updater dots driven by same `ValueTracker`, sequential t labels | t=1 initial & t=4 end checkpoints; **preview midframes still needed** |
| 5. Original quartic graph | four x-axis intersections at main-model roots | plotted quartic by `evaluate_transformed`, dots by `MAIN_X` from model, zero labels | plot range correct, four point-label pairings, check all crossings and intersections, no cropped vertex |
| 6. Radical | t=sqrt(x)≥0; x=4,9 | sequential equation rows | ensure `sqrt` domain and x=t² both shown |
| 7. Exponential | t=3^x>0; x=0,2 | sequential equation rows | ensure t positive and both x valid |
| 8. Domain pitfall | even-power t=-2 must be rejected; t=0 single preimage | bad auxiliary root highlighted pink; green final ±sqrt3; zero caveat | all domain constraints visible simultaneously |
| 9. Independent challenge | x⁴−10x²+9=0 has ±1,±3 | new question with thinking pause, method card, boxed answer | check answer matches question not prior worked example |

**Evidence ledger:** pure math tests and py_compile are run locally; Manim runtime, official Skill AST audit script, real render, frame review, ffprobe and audio check are unavailable/not run in the creation environment. The built-in `checkpoint` checks actual scene-family membership and bboxes only at explicitly called instants. It cannot validate animated in-between frames or text overlaps. No third-party audio or textbook page images are shipped.
