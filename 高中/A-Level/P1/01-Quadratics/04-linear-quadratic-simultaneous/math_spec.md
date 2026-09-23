# Mathematical contract — Cambridge P1 §1.4

**Primary source:** user's Cambridge International AS & A Level Mathematics: Pure Mathematics 1 Coursebook (2018), §1.4, printed pp. 11–12 (PDF pp. 23–24); practice problems follow on printed pp. 13–14. Source covers solving one linear and one quadratic equation by substitution; a solution is a common intersection (an ordered pair). It also notes that the substitution method extends beyond parabola graphs to general quadratic curves. **All examples and graph designs in this package are original**, not reproduced textbook exercises.

## Claims, assumptions, domains and verification

| Claim / visual | Assumptions, domain and justification | Edge case / test |
|---|---|---|
| A pair `(x,y)` is a solution iff it satisfies both equations | Both are real-variable equations. At a graphical intersection, y-values agree at the same x; in algebra, substitute the linear equation into the quadratic, then back-substitute. | `test_both_equations_checked`; x alone is not the full answer. |
| `y=x²−2x+1` and `y=x+1` meet at `(0,1)` and `(3,4)` | Equal y implies `x²−3x=x(x−3)=0`; back-substitution yields the two ordered pairs. | `test_elimination`, `test_two_exact_points`. |
| For `y=x²−2x+1` and `y=x+k`, discriminant is `5+4k` | Substitution yields `x²−3x+(1−k)=0`. Real intersections number 2 / 1 / 0 according to discriminant >0 / =0 / <0. | k=1: `(0,1),(3,4)`; k=−5/4: `(3/2,1/4)`; k=−2: no real intersection; `test_line_sweep_classification`. Do **not** label intermediate animation frames with endpoints' k values. |
| A line and a circle may also be solved using substitution | `x²+y²=5` and `y=x+1` yield `2x²+2x−4=0`, hence x=−2 or 1, points `(−2,−1)` and `(1,2)`. `r²=5>0`. | `test_circle_conic`, `test_domain_errors`. Plot via actual `Axes.c2p`, with equal x/y axis scale to draw a true circle. |
| Original practice `y=x²−2x+2`, `y=2x−1` has solutions `(1,1)` and `(3,5)` | Substitute to get `x²−4x+3=0=(x−1)(x−3)`. | `test_practice` plus direct substitution. |
| Real points with nonsquare discriminants may be approximated numerically | Float values used only for the geometric graph / nonperfect discriminant calculations; an exact root is preserved as a Fraction when possible. | `test_non_square_discriminant`; finite numerical tests do not constitute an algebraic proof. |

## Layout / geometry contract

Main parabola axes span x∈[−1,4], y∈[−3.5,9]; visible main curve samples only x∈[−.75,3.75], so y remains ∈[0,7.57]. Line family x∈[−.75,3.75], k∈[−2,1], so line y remains ∈[−2.75,4.75]. All highlighted dots and dynamic graphs derive from the same `math_model.py` dataset and the same `Axes.c2p` transform. Circle graph uses equal screen-units-per-coordinate for both axes. Registered visible objects must fit x∈[−4,4], y∈[−7,7] at explicit checkpoints; inspect intermediate frames separately.

**Limits:** A vertical line (`x=constant`) cannot be written as `y=mx+k`; solve by substituting the known x instead. More general conics can require discriminant/domain checks. Any squared rearrangement must be verified in the original equations. No textbook page images or audio are included.
