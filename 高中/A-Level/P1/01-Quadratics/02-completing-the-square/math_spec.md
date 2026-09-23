# Mathematical contract — A-Level P1 §1.2 Completing the square

Basis: Cambridge International AS & A Level Mathematics, Pure Mathematics 1 (2018), §1.2 (printed pp. 6–9; PDF pp. 18–21). The coursebook introduces reverse expansion of a perfect square, first factoring a non-unit leading coefficient, solving quadratics including surd answers, and matching coefficients. Our animation uses **original examples** rather than reproducing textbook worked examples.

## Claims, domains and proof

1. **Universal identity:** for real `a,b,c,x`, `a != 0`, `ax²+bx+c = a(x+b/(2a))² + c - b²/(4a)`. Expand the right side: `ax²+bx+b²/(4a)+c-b²/(4a)`. No division by zero allowed. The special case `x²+6x+5=(x+3)²-4` holds for all real `x`.
2. **Exact solutions:** for real `x`, `x²+6x+5=0 ⇔ (x+3)²=4 ⇔ x+3=±2 ⇔ x=-5 or -1`. Both roots satisfy the original equation. **Do not drop the minus square-root branch.**
3. **Literal tile diagram:** at the single illustrative value `x=2`, base 2×2 has 4 cells, two 2×3 strips have 6 cells each, 3×3 corner has 5 filled cells and 4 unfilled cells. Hence 21 filled cells = 25 total minus 4 unfilled. Diagram is an illustration at positive integral dimensions; it is NOT a proof that the rectangle decomposition remains a physical area argument for negative `x`. The algebraic identity is universal via expansion.
4. **Graph:** `y=(x+3)²-4` has vertex `(-3,-4)` and axis `x=-3`, global minimum `-4` over real numbers; its x-intercepts are `-5` and `-1`. The plotted curve uses the identical polynomial in the real plotting interval `[-6,0]`; numerical screen sampling is only illustrative.
5. **Non-monic case:** `2x²-8x+3=2(x-2)²-5`, so the factor `2` multiplies `-4` before adding 3. More generally `a(x-h)²+k` has global minimum `k` if `a>0`, maximum `k` if `a<0`, for `x∈R`. This is an extension using original examples; do not misrepresent as a reproduction of §1.2 examples.
6. **Zero-real-root case:** for real `x`, `x²+2x+5=(x+1)²+4>0`, so the equation `x²+2x+5=0` has no **real** solution (not “no solution” in the complex numbers).
7. **Practice:** `x²-4x-1=0 ⇔ (x-2)²=5 ⇔ x=2±√5`. Both real answers retained in exact radical form.

## Tests and uncertainty

Independent pure-Python `test_math.py` checks the stated identities on negative/integer/fractional samples, a non-unit and negative leading coefficient, invalid `a=0`, literal tile counts/invalid dimensions, roots and vertex, and a positive-definite example. Those finite tests are regression evidence; proof is the expansion and square non-negativity above. Runtime layout, final video, TeX compilation, font coverage, subtitle timing and audio are **not verified** until actual Manim render and frame inspection.
