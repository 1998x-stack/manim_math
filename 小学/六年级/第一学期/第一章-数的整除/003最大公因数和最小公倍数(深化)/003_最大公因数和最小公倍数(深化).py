"""最大公因数和最小公倍数：用 12 与 18 的质因数分解示范。"""

from manim import *


class 最大公因数和最小公倍数深化Animation(Scene):
    """通过共同质因数及各质因数的最高次数求 GCD 和 LCM。"""

    def construct(self):
        title = Text("最大公因数与最小公倍数", font_size=37).to_edge(UP, buff=0.55)
        self.play(Write(title))

        factors = VGroup(
            MathTex(r"12=2^2\times3", font_size=43),
            MathTex(r"18=2\times3^2", font_size=43),
        ).arrange(DOWN, buff=0.38).move_to(UP * 1.55)
        self.play(LaggedStart(*(Write(item) for item in factors), lag_ratio=0.5))

        gcd_note = Text("共同的质因数，各取较少的次数", font_size=27, color=BLUE)
        gcd_expr = MathTex(r"\gcd(12,18)=2\times3=6", font_size=39)
        gcd_group = VGroup(gcd_note, gcd_expr).arrange(DOWN, buff=0.22)
        gcd_group.next_to(factors, DOWN, buff=0.65)
        self.play(FadeIn(gcd_note), Write(gcd_expr))
        self.wait(1)

        lcm_note = Text("出现的质因数，各取较多的次数", font_size=27, color=YELLOW)
        lcm_expr = MathTex(r"\operatorname{lcm}(12,18)=2^2\times3^2=36", font_size=37)
        lcm_group = VGroup(lcm_note, lcm_expr).arrange(DOWN, buff=0.22)
        lcm_group.next_to(gcd_group, DOWN, buff=0.55)
        self.play(FadeIn(lcm_note), Write(lcm_expr))

        check = MathTex(r"6\times36=12\times18", font_size=36, color=GREEN)
        check.next_to(lcm_group, DOWN, buff=0.65)
        self.play(Write(check))
        self.wait(2)
