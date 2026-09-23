"""线段的相等、和、差、倍与分：中点 B 将 AC 等分。"""

from manim import *


class 线段相等与和差倍分Animation(Scene):
    """AB=BC 时，AC=AB+BC=2AB，BC=AC-AB。"""

    def construct(self):
        title = Text("线段的相等与和、差、倍、分", font_size=34)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))

        point_a, point_b, point_c = LEFT * 2.8 + UP, UP, RIGHT * 2.8 + UP
        base = Line(point_a, point_c, color=GRAY, stroke_width=3)
        ab = Line(point_a, point_b, color=BLUE, stroke_width=7)
        bc = Line(point_b, point_c, color=YELLOW, stroke_width=7)
        dots = VGroup(*[Dot(point, radius=0.10) for point in (point_a, point_b, point_c)])
        labels = VGroup(*[
            Text(name, font_size=28).next_to(dot, DOWN, buff=0.18)
            for name, dot in zip("ABC", dots)
        ])
        self.play(Create(base), FadeIn(dots), FadeIn(labels))
        self.play(Create(ab), Create(bc))

        explanation = Text("B 是 AC 的中点，两个小线段相等", font_size=26)
        explanation.next_to(labels, DOWN, buff=0.6)
        self.play(FadeIn(explanation))
        relations = VGroup(
            MathTex(r"AB=BC", font_size=39),
            MathTex(r"AC=AB+BC", font_size=39),
            MathTex(r"AC=2AB", font_size=39),
            MathTex(r"AB=\frac{AC}{2}", font_size=39),
            MathTex(r"BC=AC-AB", font_size=39),
        ).arrange(DOWN, buff=0.2)
        relations.next_to(explanation, DOWN, buff=0.38)
        self.play(LaggedStart(*(Write(item) for item in relations), lag_ratio=0.35))
        self.wait(2)
