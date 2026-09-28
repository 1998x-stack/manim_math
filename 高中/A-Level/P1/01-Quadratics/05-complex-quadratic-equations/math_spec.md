# Mathematics specification — P1 §1.5

**Source boundary:** Cambridge International AS & A Level Mathematics, Pure Mathematics 1 (2018), §1.5, printed pp. 15–16 (PDF pp. 27–28), introduces equations quadratic in a function of x, such as even powers, radicals and exponentials. This project's figures, text, worked equations and challenges are original supplemental material, not textbook excerpts. This specification is not a claim that the textbook requires every supplemental visualization.

## Mathematical claim / assumptions / proof / edge / executable test

| Claim | Assumptions and domain | Justification and representative edge case | Test |
| --- | --- | --- | --- |
| `A*g(x)^2 + B*g(x) + C=0` becomes `A*t^2+B*t+C=0` with `t=g(x)` | `A != 0`, real x in domain of g | Substitution is an equivalence only if each solved t is mapped back through g on its actual range. Arbitrary roots t are **not** automatically valid x. | `test_main_four_roots`, `test_negative_t_not_in_range_of_square` |
| `x^4-5x^2+4=0` has x roots `-2,-1,1,2` | `x` real, `t=x^2>=0` | `t^2-5t+4=(t-1)(t-4)`. Both t roots 1 and 4 are in [0,∞). Each positive t has exactly two real preimages ±sqrt(t). All four give residual zero. | `test_main_intermediate_roots`, `test_main_four_roots` |
| x² maps t=0 to exactly one root x=0, positive t to two, negative t to none | real x | Square nonnegativity and unique nonnegative square root; repeated t roots do not multiply distinct x roots. | `test_zero_has_one_preimage`, `test_repeated_root_has_two_preimages_not_four` |
| Graph `y=x^4-5x^2+4` crosses x-axis at these four roots | shown domain x in [-2.15,2.15], y from -3 to 5.3 | The plot uses the identical model function as the unit tests, x-intercept dots at returned roots, not independently hard-coded alternate formulas. Axis viewport includes all plotted values in chosen interval. The plot numerically illustrates but is not proof. | `test_main_four_roots` + actual preview frame inspection pending |
| `x-5sqrt(x)+6=0` has x=4 or 9 | real `x>=0`, `t=sqrt(x)>=0` | `(t-2)(t-3)=0`, then x=t²; both satisfy the original. Negative t must be rejected. | `test_sqrt_example_and_original_equation` |
| `3^(2x)-10*3^x+9=0` has x=0 or 2 | real x, `t=3^x>0` | `(t-1)(t-9)=0`, `3^x=1,9`; roots x=0,2. t=0 and negative t are impossible. | `test_power_example_and_range` |
| `x^4-x²-6=0` has x=±sqrt(3) only | `t=x²>=0` | t=3 or -2; reject -2. The unrejected solutions satisfy original. | `test_practice_filters_negative_intermediate_root` |
| Independent challenge `x⁴-10x²+9=0` has ±1 and ±3 | real x | t=1 or 9, both positive; all four returned solutions checked in the original equation. | `test_new_independent_challenge` |

`quadratic_roots` handles no real t roots, zero discriminant and rejects zero leading coefficient; floating point tolerance is for numerical display/test support, not symbolic proof. During rendering, actual Manim Mobject positions, TeX/CJK font, animation-time state and frame bounds must still be inspected; static tests cannot certify any of these.
