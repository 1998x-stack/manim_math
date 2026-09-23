"""有理数的意义：能写成两个整数之比且分母非零的数。"""

from manim import *


class 有理数的意义Animation(Scene):
    """用整数和分数的例子说明有理数的统一表示。"""

    def construct(self):
        title = Text("有理数的意义", font_size=43).to_edge(UP, buff=0.55)
        self.play(Write(title))
        definition = Text("有理数能写成两个整数的比", font_size=31)
        definition.move_to(UP * 1.9)
        form = MathTex(r"\frac{p}{q},\quad p,q\in\mathbb{Z},\quad q\ne0", font_size=42)
        form.next_to(definition, DOWN, buff=0.45)
        self.play(FadeIn(definition), Write(form))

        examples = VGroup(
            Text("整数也可以表示成分母为 1 的分数", font_size=28),
            MathTex(r"-2=\frac{-2}{1},\qquad 0=\frac01", font_size=40),
            Text("分数可以表示正数，也可以表示负数", font_size=28),
            MathTex(r"\frac34,\qquad-\frac52", font_size=42),
        ).arrange(DOWN, buff=0.3)
        examples.next_to(form, DOWN, buff=0.6)
        self.play(LaggedStart(*(FadeIn(item) for item in examples), lag_ratio=0.4))
        self.wait(2)
