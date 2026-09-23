"""余角、补角、对顶角：和的条件与相交直线的对顶角相等。"""

from manim import *


class 余角补角对顶角Animation(Scene):
    """直观展示互余、互补，以及相交直线形成的对顶角。"""

    def construct(self):
        title = Text("余角、补角、对顶角", font_size=39).to_edge(UP, buff=0.5)
        self.play(Write(title))

        a = LEFT * 2 + DOWN * 0.65 + UP * 1.8
        b = LEFT * 2 + UP * 0.65 + UP * 1.8
        c = RIGHT * 2 + UP * 0.65 + UP * 1.8
        d = RIGHT * 2 + DOWN * 0.65 + UP * 1.8
        o = UP * 1.8
        crossing = VGroup(Line(a, c, color=BLUE), Line(b, d, color=YELLOW))
        endpoints = VGroup(*[Dot(p, radius=0.07) for p in (a, b, c, d, o)])
        names = VGroup(*[
            Text(name, font_size=22).next_to(point, direction, buff=0.1)
            for name, point, direction in (
                ("A", a, DOWN), ("B", b, UP), ("C", c, UP),
                ("D", d, DOWN), ("O", o, DOWN),
            )
        ])
        self.play(Create(crossing), FadeIn(endpoints), FadeIn(names))

        facts = VGroup(
            VGroup(Text("余角：两个角的和是 90°", font_size=25),
                   MathTex(r"30^\circ+60^\circ=90^\circ", font_size=35)),
            VGroup(Text("补角：两个角的和是 180°", font_size=25),
                   MathTex(r"110^\circ+70^\circ=180^\circ", font_size=35)),
            VGroup(Text("对顶角：两条直线相交，所成对顶角相等", font_size=24),
                   MathTex(r"\angle AOB=\angle COD", font_size=35)),
        )
        for fact in facts:
            fact.arrange(DOWN, buff=0.1)
        facts.arrange(DOWN, buff=0.24).move_to(DOWN * 1.75)
        self.play(LaggedStart(*(FadeIn(fact) for fact in facts), lag_ratio=0.4))
        self.wait(2)
