# P1 1.1 / Solving quadratic equations by factorisation

- Target: portrait 9:16, logical 9×16, output target 1080×1920; safe region x∈[-4,4], y∈[-7,7]. Dark background; teal/gold/coral/green mathematical color key.
- Persistent identity: `header` / brand label 'A-Level | PURE MATHEMATICS 1 · P1'; `footer` / Chapter 1 §1.1. No copied exam-board artwork.
- Runtime class: `P1Factorisation`; caption-only (no audio included); timings are editorial approximations, not an audio sync promise.
- Math source: uploaded Cambridge P1 coursebook §1.1 on physical PDF pp. 15–18; the `x²−5x+6` video example and diagrams are original teaching expansions, not claims of being the textbook's examples.

| Shot | approx. | learning_fact / math claim | on-screen object IDs and lifecycle | transition/checkpoint |
|---|---:|---|---|---|
| 01 Opening | 7 s | Solve quadratic by splitting zero product into linear equations | `question`, `prompt`, `chips`: create; `header/footer`: keep | `question` inside safe bbox; fade out all content |
| 02 Area tiles | 14 s | For x≥3 a square minus width-2 strip and height-3 strip plus their overlap is `(x−2)(x−3)` | `whole`, `upper`, `right_strip`, `overlap`, `remain`, `identity`: create; then remove | area check for x=5, labeled overlap; all boxes within viewport |
| 03 Find pair | 11 s | Find integers −2,−3 using sum −5 / product +6; verify by expansion | `sum_pair`,`product_pair`,`candidate_factors`,`expansion`: create/remove | chosen factors multiply back to the given trinomial |
| 04 Zero product | 10 s | `A·B=0 ⇒ A=0 or B=0` | `orig`,`factors`,`branches`: create/remove | mutually exhaustive algebra branch highlighted |
| 05 Solve both factors | 10 s | `x−2=0` or `x−3=0` gives 2,3 | `two_branches`, `solution`: create/remove | actual solution boxed; no factor discarded |
| 06 Parabola | 13 s | polynomial zero values coincide with x-axis intersections | `axes`, `graph`, `root_markers`, `graph_formula`: create/remove | graph & markers from same f/roots and axes.c2p |
| 07 Error case | 10 s | dividing by possible zero factor loses root 2 | `avoid_cancel`, `counterexample`: create/remove | visually distinguish wrong omission from valid proof |
| 08 Practice | 10 s + read pause | first factor out 2 in `2x²−10x+12=0` | `practice_answer`: create/remove | solutions match example because scale factor nonzero |
| 09 Summary | 12 s | rearrange, factor, zero-product, check both roots | `closing_card`, `final_result`, `verified_roots`: create/keep | final note and source-appropriate P1 identifier |

## Object lifecycle

`self.chrome` persists across all shots. All other top-level content is cleared by `clear_content()` after each shot, except the final summary, which remains on screen through the end. No ReplacementTransform source/target ambiguity; the original question and follow-up panels are separate new objects intentionally.

## Verification boundaries

- Pure math test: `python test_math.py` (no Manim import).
- Syntax: `python -m py_compile lesson.py math_model.py test_math.py`.
- `assert_visible` checks registered on-screen **real Manim objects** at the end of each shot during actual rendering; this is not per-frame overlap or pacing inspection.
- AST production scanner: run upstream `scripts/audit_scene.py` if installed separately; not bundled here.
- Preview, final render, ffprobe, manual representative-frame review: only mark passed after actual execution in a Manim environment. There is no narration/music; audio review is not applicable.
