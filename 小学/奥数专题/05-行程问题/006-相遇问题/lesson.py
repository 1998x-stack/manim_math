"""相遇问题：带真实路程比例的线段图；动态显示已走路程和剩余间距。"""
from fractions import Fraction
from manim import *

config.frame_width, config.frame_height = 9, 16
BG, FONT = "#101827", "Noto Sans CJK SC"


def encounter_time(distance: int, speed_a: int, speed_b: int) -> Fraction:
    if any(type(v) is not int for v in (distance, speed_a, speed_b)):
        raise ValueError("integer data required")
    if distance <= 0 or speed_a < 0 or speed_b < 0 or speed_a + speed_b == 0:
        raise ValueError("invalid distance or speeds")
    return Fraction(distance, speed_a + speed_b)


class EncounterScene(Scene):
    def construct(self):
        self.camera.background_color = BG
        distance, va, vb = 200, 60, 40
        duration = encounter_time(distance, va, vb)
        assert duration == 2
        title = Text("相遇问题：线段被两人同时缩短", font=FONT, font_size=33).move_to(UP * 6.24)
        question = Text("相距 200 千米，甲每时 60，乙每时 40", font=FONT, font_size=27).move_to(UP * 5.08)
        self.play(Write(title), FadeIn(question))
        start_x, end_x, y = -3., 3., 1.5
        scale = (end_x - start_x) / distance
        t = ValueTracker(0.)
        x_a = lambda: start_x + va * t.get_value() * scale
        x_b = lambda: end_x - vb * t.get_value() * scale
        road = Line([start_x, y, 0], [end_x, y, 0], color=GREY_B, stroke_width=4)
        ticks = VGroup()
        for km in range(0, 201, 40):
            x = start_x + km * scale
            ticks.add(Line([x, y-.10, 0], [x, y+.10, 0], color=GREY_A))
            ticks.add(MathTex(str(km), font_size=23).move_to([x, y-.37, 0]))
        a = always_redraw(lambda: Dot([x_a(), y, 0], radius=.17, color=BLUE_B))
        b = always_redraw(lambda: Dot([x_b(), y, 0], radius=.17, color=YELLOW))
        traveled_a = always_redraw(lambda: Line([start_x, y, 0], [x_a(), y, 0], color=BLUE_B, stroke_width=9))
        traveled_b = always_redraw(lambda: Line([x_b(), y, 0], [end_x, y, 0], color=YELLOW, stroke_width=9))
        gap = always_redraw(lambda: Line([x_a(), y, 0], [x_b(), y, 0], color=GREEN_B, stroke_width=5))
        la = Text("甲 60 千米/时", font=FONT, font_size=27, color=BLUE_B).move_to([-2.05, 3.02, 0])
        lb = Text("乙 40 千米/时", font=FONT, font_size=27, color=YELLOW).move_to([2.05, 3.02, 0])
        self.play(Create(road), FadeIn(ticks), FadeIn(a, b, la, lb))
        self.add(traveled_a, traveled_b, gap, a, b)

        time_caption = Text("已过时间（小时）", font=FONT, font_size=27).move_to([-1.8, -.15, 0])
        time_value = DecimalNumber(0, num_decimal_places=1, font_size=36, color=BLUE_B).move_to([1.55, -.15, 0])
        time_value.add_updater(lambda m: m.set_value(t.get_value()))
        gap_caption = Text("两人还相距（千米）", font=FONT, font_size=27).move_to([-1.8, -1.08, 0])
        gap_value = DecimalNumber(distance, num_decimal_places=0, font_size=36, color=GREEN_B).move_to([1.55, -1.08, 0])
        gap_value.add_updater(lambda m: m.set_value(max(0, distance-(va+vb)*t.get_value())))
        self.play(FadeIn(time_caption, gap_caption, time_value, gap_value))
        self.play(t.animate.set_value(1.), run_time=2, rate_func=linear)
        halfway = MathTex(r"200-(60+40)\times1=100", font_size=33).move_to(DOWN * 2.40)
        self.play(Write(halfway))
        self.play(t.animate.set_value(2.), run_time=2, rate_func=linear)
        meet_x = start_x + 120 * scale
        assert abs(meet_x - (end_x - 80 * scale)) < 1e-9
        mark = Dot([meet_x, y, 0], color=GREEN_B, radius=.22)
        self.play(FadeIn(mark), FadeOut(halfway))
        proof = MathTex(r"120+80=200", font_size=37).move_to(DOWN * 2.52)
        answer = MathTex(r"t=\frac{200}{60+40}=2", font_size=39, color=YELLOW).move_to(DOWN * 3.76)
        principle = Text("每小时合走 100 千米，2 小时走完 200 千米", font=FONT, font_size=25).move_to(DOWN * 5.15)
        self.play(Write(proof), Write(answer), FadeIn(principle))
        self.wait(2)
        time_value.clear_updaters()
        gap_value.clear_updaters()
