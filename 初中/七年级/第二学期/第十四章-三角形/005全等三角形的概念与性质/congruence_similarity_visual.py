"""全等与相似：刚体运动保持边长，缩放只保持角和边比。"""
import numpy as np
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#101827"


def colored_triangle(offset):
    a = np.array([-1.1, -0.8, 0.0]) + offset
    b = np.array([1.1, -0.8, 0.0]) + offset
    c = np.array([-0.35, 1.2, 0.0]) + offset
    return VGroup(
        Polygon(a, b, c, stroke_color=WHITE, stroke_width=3,
                fill_color=BLUE, fill_opacity=0.08),
        Line(a, b, color=YELLOW, stroke_width=7),
        Line(b, c, color=GREEN, stroke_width=7),
        Line(c, a, color=ORANGE, stroke_width=7),
    )


class CongruenceSimilarityVisual(Scene):
    """Render: manim -pql congruence_similarity_visual.py CongruenceSimilarityVisual"""

    def construct(self):
        title = Text("全等 vs 相似", font_size=46).to_edge(UP, buff=1.0)
        left = colored_triangle(LEFT * 1.65)
        right = colored_triangle(RIGHT * 1.65)
        label_left = MathTex(r"\triangle ABC", font_size=38).move_to(
            LEFT * 1.75 + DOWN * 2.2)
        label_right = MathTex(r"\triangle A'B'C'", font_size=38).move_to(
            RIGHT * 1.75 + DOWN * 2.2)
        self.play(Write(title), FadeIn(left), FadeIn(right),
                  FadeIn(label_left), FadeIn(label_right))
        statement = MathTex(r"AB=A'B',\quad BC=B'C',\quad CA=C'A'",
                            font_size=34).move_to(DOWN * 3.5)
        self.play(Write(statement))
        self.play(Rotate(right, angle=PI / 3,
                         about_point=RIGHT * 1.65), run_time=2)
        self.wait(0.5)
        rigid = VGroup(Text("平移与旋转不改变形状和大小", font_size=30),
                       MathTex(r"\triangle ABC\cong\triangle A'B'C'",
                               font_size=39))
        rigid.arrange(DOWN, buff=0.35).move_to(DOWN * 4.8)
        self.play(FadeIn(rigid))
        self.wait(1)
        self.play(FadeOut(statement), FadeOut(rigid))
        valid_tests = VGroup(
            Text("SSS：三边分别相等", font_size=29),
            Text("SAS：两边及其夹角分别相等", font_size=29),
            Text("ASA：两角及其夹边分别相等", font_size=29),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 4.6)
        self.play(FadeIn(valid_tests))
        self.wait(1)
        self.play(FadeOut(valid_tests))

        # Scale about the right figure's center; the left figure is unchanged.
        self.play(right.animate.scale(1.35, about_point=RIGHT * 1.65),
                  run_time=2)
        similarity = VGroup(
            Text("对应角相等、对应边成比例：相似不一定全等", font_size=29),
            MathTex(r"\frac{A'B'}{AB}=\frac{B'C'}{BC}=\frac{C'A'}{CA}=k",
                    font_size=38),
            MathTex(r"k=1.35\ne1", font_size=38, color=YELLOW),
            Text("AA：两个对应角相等即可判定相似", font_size=28),
        ).arrange(DOWN, buff=0.38).move_to(DOWN * 4.6)
        self.play(FadeIn(similarity))
        self.wait(2)
