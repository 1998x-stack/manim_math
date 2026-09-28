# A-Level P1 §1.3 — Mathematical contract

**Source and scope:** Cambridge International AS & A Level Mathematics, Pure Mathematics 1 (2018), §1.3, textbook page 10 (PDF page 22). Source sequence: state formula for `ax²+bx+c=0`, assume `a≠0`, derive by completing the square, substitute coefficients, present answers to requested significant figures. All animated examples, tiling and figure layout in this project are original rather than reproductions of textbook pages.

| Claim / visual | Assumptions and domain | Justification | Edge case / independent test |
| --- | --- | --- | --- |
| The quadratic formula `x=(-b±√(b²−4ac))/(2a)` solves `ax²+bx+c=0` over reals when `Δ≥0` | Real `a,b,c`; `a≠0`; `Δ=b²−4ac≥0` | Divide by `a`; add `(b/2a)²`; obtain `(x+b/2a)²=Δ/(4a²)`; taking both square-root branches yields the formula. `±√Δ/(2a)` is a valid *unordered* pair even if `a<0`. | `a=0` must be rejected; `Δ<0` has no real roots (complex roots are outside this animation). |
| Number of *distinct real* roots is 2, 1, or 0 according as `Δ>0`, `Δ=0`, or `Δ<0` | Real coefficients, `a≠0` | The square-root term is positive, zero, or nonreal respectively. | `Δ=0` is **one double root**, not two distinct x-intercepts. |
| Completing-square area model: `x²+2dx+d²=(x+d)²` | Illustrative tiling uses nonnegative *integer* x,d; x=d=2 in shot 3. | 2×2 block + two 2×2 strips + 2×2 corner = 4×4 square. General algebraic identity follows from expansion for all real x,d, not from this finite tiling alone. | Negative x/d cannot be represented by ordinary positive unit tiles. `test_geometry_tile_counts_and_domain`. |
| Original worked example `2x²−2x−1=0` has `Δ=12` and `x=(1±√3)/2` | Real x | Substitute a=2,b=−2,c=−1 and simplify `√12=2√3`. | Distinct real roots; x≈1.37 and x≈−0.366 (3 significant figures). `test_exact_example_claims`, `test_rounded_example_is_3sf`. |
| The graph of `y=2x²−2x−1` has vertex `(1/2,−3/2)` and x-intercepts at worked example roots | Real x | Complete square `2(x−1/2)²−3/2`; set y=0; graph plotted from the same coefficient model. | Both root x-values are in plotted x-range. `test_exact_example_claims`. |
| Discriminant family `(x−1)²−k=0` has `Δ=4k` | Real k, real x | Expand x²−2x+(1−k); roots 1±√k only for k≥0. | k=1: 2 roots; k=0: tangent, 1 double root; k=−1: 0 real roots. `test_root_count_and_repeated_root`. |
| Original practice `3x²+2x−2=0` has exact solutions `x=(-1±√7)/3` | Real x | Δ=4+24=28, `√28=2√7`. | `test_practice_radicals_and_residual`. |

**Geometry and graph boundaries:** The 4×4 tile diagram has only illustrative lengths; mathematical proof is independent of tiles. All three discriminant-state curves use a fixed nondegenerate plot interval `[-0.48,2.48]`, and each visible root marker is calculated from the current `k` tracker. Do not infer a general symbolic identity solely from one diagram or numeric sampling.

**Rounding:** Report surds before decimals; rounding is an approximation rather than an equality. The source textbook §1.3 also uses an example to three significant figures, but the example here is an original one.
