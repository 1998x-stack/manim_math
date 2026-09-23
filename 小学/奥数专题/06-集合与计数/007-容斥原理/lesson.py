"""两集合容斥：合并时重叠部分只计一次。"""
from manim import *

config.frame_width = 9
config.frame_height = 16
BG = "#101827"
FONT = "Noto Sans CJK SC"


def union_count(a: int, b: int, both: int) -> int:
    if any(type(v) is not int for v in (a, b, both)):
        raise ValueError("integer counts required")
    if a < 0 or b < 0 or both < 0 or both > min(a, b):
        raise ValueError("invalid intersection count")
    return a + b - both


class InclusionExclusionScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        both, a_only, b_only = 4, 8, 6
        total = union_count(a_only + both, b_only + both, both)
        assert total == 18
        title = Text("容斥原理：别数两遍", font=FONT, font_size=36).move_to(UP * 6.2)
        question = Text("喜欢数学 12 人，科学 10 人，两者都喜欢 4 人", font=FONT, font_size=25).move_to(UP * 4.9)
        self.play(Write(title), FadeIn(question))
        left = Circle(radius=2.0, color=BLUE_B, fill_color=BLUE_D, fill_opacity=0.35).move_to([-1.25, 0.6, 0])
        right = Circle(radius=2.0, color=GREEN_B, fill_color=GREEN_D, fill_opacity=0.35).move_to([1.25, 0.6, 0])
        self.play(Create(left), Create(right))
        counts = VGroup(
            MathTex("8", font_size=50, color=BLUE_B).move_to([-2.30, 0.6, 0]),
            MathTex("4", font_size=50, color=YELLOW).move_to([0, 0.6, 0]),
            MathTex("6", font_size=50, color=GREEN_B).move_to([2.30, 0.6, 0]),
        )
        captions = VGroup(
            Text("仅数学", font=FONT, font_size=24).move_to([-2.35, -0.1, 0]),
            Text("两者都有", font=FONT, font_size=24).move_to([0, -0.1, 0]),
            Text("仅科学", font=FONT, font_size=24).move_to([2.35, -0.1, 0]),
        )
        self.play(LaggedStart(*(FadeIn(m) for m in counts), lag_ratio=.3), FadeIn(captions))
        wrong = MathTex(r"12+10=22", font_size=38, color=RED_B).move_to(DOWN * 3.0)
        self.play(Write(wrong))
        correction = Text("重复的 4 人要减去一次", font=FONT, font_size=29).move_to(DOWN * 3.95)
        self.play(FadeIn(correction), wrong.animate.set_opacity(.35))
        answer = MathTex(r"12+10-4=18", font_size=42, color=YELLOW).move_to(DOWN * 5.0)
        self.play(Write(answer))
        self.wait(2)
