"""复数的概念：复数的代数形式与复平面中的坐标表示。"""

from manim import *


class 复数的概念Animation(Scene):
    """用具体的复数 z=2+i 解释 z=a+bi 与点 (a,b) 的对应关系。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("复数的概念", font_size=46).to_edge(UP, buff=0.6)
        definition = MathTex(
            r"z=a+bi,\quad a,b\in\mathbb{R}", font_size=36
        )
        imaginary_unit = MathTex(r"i^2=-1", font_size=34)
        statement = VGroup(definition, imaginary_unit).arrange(DOWN, buff=0.3)
        statement.next_to(title, DOWN, buff=0.45)

        # 坐标比例由 NumberPlane.c2p 统一转换，避免把数学坐标当作屏幕坐标。
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            background_line_style={"stroke_opacity": 0.3},
        ).move_to(DOWN * 0.6)
        x_label = MathTex(r"\operatorname{Re}", font_size=28)
        x_label.next_to(plane.c2p(3, 0), RIGHT, buff=0.12)
        y_label = MathTex(r"\operatorname{Im}", font_size=28)
        y_label.next_to(plane.c2p(0, 2), UP, buff=0.12)

        origin = plane.c2p(0, 0)
        endpoint = plane.c2p(2, 1)
        vector = Arrow(origin, endpoint, buff=0, color=YELLOW)
        point = Dot(endpoint, color=YELLOW)
        example = MathTex(r"z=2+i", font_size=32, color=YELLOW)
        example.next_to(point, RIGHT, buff=0.22)
        explanation = Text("实部是 2，虚部是 1，对应点 (2, 1)", font_size=24)
        explanation.to_edge(DOWN, buff=0.75)

        self.play(Write(title), Write(statement))
        self.play(Create(plane), FadeIn(x_label), FadeIn(y_label))
        self.play(GrowArrow(vector), FadeIn(point), Write(example))
        self.play(FadeIn(explanation))
        self.wait(2)
