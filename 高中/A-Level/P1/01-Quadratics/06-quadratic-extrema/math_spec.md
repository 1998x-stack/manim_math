# Math specification · P1 §1.6 Maximum and minimum values of a quadratic function

Source scope: *Cambridge International AS & A Level Mathematics: Pure Mathematics 1* (2018), §1.6, printed pp. 17–20 / PDF pp. 29–32. Source covers parabola orientation, vertex, symmetry axis, x/y intercepts, graph sketching, and completed-square form. All animation examples and labels here are newly written and are not reproduced textbook exercises.

| claim | assumptions / domain | mathematical justification | edge case / counterexample | model/test/visual |
|---|---|---|---|---|
| `f(x)=ax²+bx+c=a(x-h)²+k`, `h=-b/(2a)`, `k=c-b²/(4a)` | real coefficients, `a != 0`, `x in R` | expand and compare coefficients, or complete square | `a=0`: linear/constant, no parabolic vertex | `Quadratic.h`, `.k`, `.verify_vertex_identity`, shot 5 |
| parabola has global min `k` at `x=h` if `a>0` and global max `k` if `a<0` | real `x`, nonzero `a` | `(x-h)² >= 0`, multiply by sign of `a` | no global maximum for `a>0`, no global minimum for `a<0` on `R` | `.kind`, shots 1, 2, 6 |
| axis `x=h`; symmetric pairs `f(h-d)=f(h+d)` | real `h,d` | both are `ad²+k` | domain restriction may exclude symmetric mate | `.value`, tests, shots 3–4 |
| `f=x²-4x+1=(x-2)²-3`, vertex `(2,-3)`, `f(1)=f(3)=-2`, zeros `2±sqrt(3)`, y intercept `(0,1)` | real `x` | square completion and zero equation | roots labeled exactly, render dots from the same model's numeric roots | `UP`, `.roots()`, shots 2,4,7 |
| `g=-x²+6x-5=4-(x-3)²`, max 4 at x=3, zeros x=1,5, y intercept -5 | real `x` | completed square + substitution | do not confuse maximum value 4 with maximizer x=3 | `DOWN`, shot 6 |
| `f` on `[3,4]` has min -2 at x=3 and max 1 at x=4 | closed interval, same `f` as above | vertex `x=2` excluded; endpoint comparison | global vertex formula is not automatically constrained-interval answer | `.interval_extrema`, shot 8 |
| practice `q=-x²+4x+1=5-(x-2)²`, max 5 at x=2 | real `x` | square completion | for `a=0`, reject quadratic model | `PRACTICE`, shot 9 |

The transformed-graph segment in shot 3 is a visual demonstration of `y=(x-h)²+k` for tracker values; its vertex and symmetry line derive from the SAME trackers. Static graph roots and key point values come from `math_model.py`. Numeric tracing alone does not prove the general formulas; shot 5 presents the algebraic derivation. The restricted-domain shot is an ORIGINAL extension, not an assertion that the textbook §1.6 requires interval optimization.

Visualization contract: portrait logical 9×16; conservative safe bbox x ∈ [-4,4], y ∈ [-7,7]; course brand always visible; Chinese `Text`, formulas `MathTex`. No audio, third-party illustrations, or textbook page scans. A custom fixed-state `checkpoint` checks object presence and bbox only at explicit points; it does not replace the Skill runtime_probe, static AST audit, live render, or frame review.
