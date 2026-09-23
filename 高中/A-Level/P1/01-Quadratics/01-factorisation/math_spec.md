# P1 1.1 Mathematical specification / 数学契约

- Course identification: **A-Level | Pure Mathematics 1 (P1)**, Chapter 1, §1.1.
- Textbook basis: user-supplied Cambridge *Pure Mathematics 1 Coursebook* (2018), physical PDF pp. 15–18 (printed pp. 3–6). The book's §1.1 reinforces factorisation, rearrangement to `ax²+bx+c=0`, the zero-product rule and checking solutions. The video uses a separately created example `x²−5x+6=0`, not an exact reproduction of textbook worked examples.
- Audience: learner with elementary polynomial expansion, integers and linear equations.
- Domain: solve the example over **real numbers**; the integer-pair search is an example method, not a universal method for all real quadratics.

| claim | assumptions/domain | justification | edge case/counterexample | executable check |
|---|---|---|---|---|
| `x²−5x+6 = (x−2)(x−3)` | all real x | distributivity: `x²−3x−2x+6` | identity remains true for x<3 even though rectangular-strip diagram ceases to be literal | `test_math.py`, coefficients and sample x |
| Area model: `x²−2x−3x+6=(x−2)(x−3)` | literal geometric strips only for x≥3 | remove width-2 and height-3 strips from square of side x; add overlap `2×3` once | negative strip lengths for x<3; don't use diagram as geometric proof there | `square_partition`, boundary x=3 and counterexamples x<3 |
| `(x−2)(x−3)=0 ⇒ x=2 or x=3` | x real, ordinary multiplication | zero-product property in integral domain ℝ | do not divide by x−2; at x=2 it equals zero | roots/check_solutions and explicit x=2 substitution |
| Graph of y=(x−2)(x−3) crosses x axis at 2,3 | Cartesian graph of continuous polynomial | f(x)=0 iff a graph point has y=0 | axis is a visualization, not a substitute for algebraic reasoning | roots, vertex value -1/4, sample signs |
| `2x²−10x+12=0` has the same roots | 2≠0 | divide whole equation by 2, then apply identical factorisation | zero coefficient division not permitted | expansion test plus plug roots |

Visuals: original area partition for `x=5`; graph derived directly from `math_model.f`; zero-product branches; original exercise; common invalid cancellation warning.
No copyrighted textbook diagram, external brand mark or third-party audio is included. 'A-Level · P1' is a text course identifier, not a reproduction of an awarding body's logo.
