"""相遇问题：两人相向而行，距离以速度和缩短。"""
from fractions import Fraction
from manim import *

config.frame_width = 9
config.frame_height = 16
BG = "#101827"
FONT = "Noto Sans CJK SC"


def encounter_time(distance: int, speed_a: int, speed_b: int) -> Fraction:
    if any(type(v) is not int for v in (distance, speed_a, speed_b)):
        raise ValueError("integer data required")
    if distance <= 0 or speed_a < 0 or speed_b < 0 or speed_a + speed_b == 0:
        raise ValueError("invalid distance or speeds")
    return Fraction(distance, speed_a + speed_b)


class EncounterScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        distance, speed_a, speed_b = 200, 60, 40
        hours = encounter_time(distance, speed_a, speed_b)
        assert hours == 2
        title = Text("相遇问题：速度和", font=FONT, font_size=36).move_to(UP * 6.2)
        question = Text("相距 200 千米，相向而行，多久相遇？", font=FONT, font_size=27).move_to(UP * 4.9)
        self.play(Write(title), FadeIn(question))
        track = Line([-3.2, 1.0, 0], [3.2, 1.0, 0], color=WHITE)
        start_a, start_b = np.array([-3.0, 1.0, 0]), np.array([3.0, 1.0, 0])
        meet = np.array([0.6, 1.0, 0])  # 比例 60:40，甲行 120 千米，占总程的 60%。
        a = Dot(start_a, radius=.19, color=BLUE_B)
        b = Dot(start_b, radius=.19, color=YELLOW)
        label_a = Text("甲：60 千米/时", font=FONT, font_size=26, color=BLUE_B).move_to([-2.1, 2.2, 0])
        label_b = Text("乙：40 千米/时", font=FONT, font_size=26, color=YELLOW).move_to([2.1, 3.0, 0])
        self.play(Create(track), FadeIn(a, b), FadeIn(label_a, label_b))
        shrinking = MathTex(r"200-(60+40)t", font_size=36).move_to(DOWN * 1.1)
        self.play(Write(shrinking))
        self.play(a.animate.move_to(meet), b.animate.move_to(meet), run_time=3, rate_func=linear)
        meeting = Dot(meet, radius=.23, color=GREEN_B)
        self.play(FadeOut(a, b), FadeIn(meeting))
        formula = MathTex(r"t=\frac{200}{60+40}=2", font_size=40, color=YELLOW).move_to(DOWN * 3.2)
        note = Text("两人合起来每小时走 100 千米", font=FONT, font_size=28).move_to(DOWN * 4.65)
        self.play(Write(formula), FadeIn(note))
        self.wait(2)
