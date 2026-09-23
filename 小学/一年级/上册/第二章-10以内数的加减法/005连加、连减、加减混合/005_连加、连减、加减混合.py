"""一年级连加、连减、加减混合：保持从左到右依次计算。

原 Scene 类名中使用了中文顿号「、」，不是合法 Python 标识符，
文件无法导入。本次修正为连加连减加减混合Animation。
渲染：manim -pql '005_连加、连减、加减混合.py' 连加连减加减混合Animation
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT = "PingFang SC"


def calculate_steps(first, second, third, first_op, second_op):
    """返回两步运算结果；本课约束中间数量和最终数量均为 0～10。"""
    if any(type(value) is not int or not 0 <= value <= 10
           for value in (first, second, third)):
        raise ValueError("每个数量必须是 0～10 的整数")
    if first_op not in ("+", "-") or second_op not in ("+", "-"):
        raise ValueError("本课仅支持加法和减法")
    middle = first + second if first_op == "+" else first - second
    final = middle + third if second_op == "+" else middle - third
    if not 0 <= middle <= 10 or not 0 <= final <= 10:
        raise ValueError("本课中间数量和结果必须在 0～10 内")
    return middle, final


class 连加连减加减混合Animation(Scene):
    """三个例题：2+3+1、5-2-1、5+2-3；每步同步展示物体数量。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=19, color=GRAY_B,
        ).move_to(UP * 7.2)
        title = Text("连加、连减、加减混合", font=FONT, font_size=39,
                     color=YELLOW).move_to(UP * 6)
        self.add(author)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)
        self.play(FadeOut(title), run_time=0.4)

        self.show_example(2, 3, 1, "+", "+", "连加：一个一个加进去")
        self.show_example(5, 2, 1, "-", "-", "连减：一个一个拿走")
        self.show_example(5, 2, 3, "+", "-", "加减混合：先加再减")

        takeaway = Text("从左往右，一步一步算", font=FONT,
                        font_size=40, color=YELLOW).move_to(UP * 1)
        self.play(Write(takeaway), run_time=1)
        self.wait(2)

    @staticmethod
    def make_counters(amount):
        """一个圆点对应一个物体；零时明确显示空集合文字。"""
        if amount == 0:
            return Text("没有圆点（0个）", font=FONT, font_size=27,
                        color=WHITE).move_to(UP * 0.5)
        dots = VGroup(*[
            Dot(radius=0.19, color=BLUE_B) for _ in range(amount)
        ]).arrange_in_grid(rows=2 if amount > 5 else 1, buff=0.3)
        return dots.move_to(UP * 0.5)

    def show_example(self, first, second, third, op1, op2, caption):
        middle, final = calculate_steps(first, second, third, op1, op2)
        heading = Text(caption, font=FONT, font_size=32,
                       color=YELLOW).move_to(UP * 5.1)
        expression = MathTex(
            f"{first}{op1}{second}{op2}{third}={final}", font_size=66,
        ).move_to(UP * 3.6)
        hint = Text("先算前两个数", font=FONT, font_size=30,
                    color=WHITE).move_to(DOWN * 2.2)
        counters = self.make_counters(first)
        self.play(FadeIn(heading), Write(expression), FadeIn(counters), run_time=0.9)
        self.wait(0.8)

        middle_counters = self.make_counters(middle)
        first_result = MathTex(
            f"{first}{op1}{second}={middle}", font_size=54,
        ).move_to(DOWN * 3.2)
        self.play(ReplacementTransform(counters, middle_counters),
                  FadeIn(hint), Write(first_result), run_time=0.9)
        self.wait(1.0)

        final_counters = self.make_counters(final)
        second_hint = Text("再算第三个数", font=FONT, font_size=30,
                           color=WHITE).move_to(DOWN * 2.2)
        final_result = MathTex(
            f"{middle}{op2}{third}={final}", font_size=54,
        ).move_to(DOWN * 3.2)
        self.play(ReplacementTransform(middle_counters, final_counters),
                  ReplacementTransform(hint, second_hint),
                  ReplacementTransform(first_result, final_result), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(VGroup(heading, expression, final_counters,
                                 second_hint, final_result)), run_time=0.7)
