"""四年级：三位数乘两位数的竖式计算。

运行：manim -pql '001_笔算乘法(竖式计算).py' ColumnMultiplicationLesson
竖屏画幅由本课设置；使用 Manim Community Edition。
"""

from manim import *

# 必须在 Scene 初始化摄像机之前配置画幅，不能放在 construct() 中。
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

MULTIPLICAND = 123
MULTIPLIER = 45


def multiplication_steps(multiplicand: int, multiplier: int) -> tuple[int, int, int]:
    """返回个位部分积、十位部分积（已乘 10）及最终乘积。"""
    if (
        type(multiplicand) is not int
        or type(multiplier) is not int
        or not 100 <= multiplicand <= 999
        or not 10 <= multiplier <= 99
    ):
        raise ValueError("此课只接受三位数乘两位数的非负整数示例")
    units = multiplicand * (multiplier % 10)
    tens = multiplicand * (multiplier // 10) * 10
    return units, tens, units + tens


class ColumnMultiplicationLesson(Scene):
    """先对位，再求两个部分积，最后相加；第二行表示十位上的数。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        units, tens, answer = multiplication_steps(MULTIPLICAND, MULTIPLIER)
        unit_digit = MULTIPLIER % 10
        tens_digit = MULTIPLIER // 10

        title = Text("三位数乘两位数：竖式计算", font_size=43, color=YELLOW)
        title.scale_to_fit_width(7.9).move_to(UP * 6.2)
        prompt = Text("先算个位，再算十位，最后相加", font_size=29).move_to(UP * 4.7)
        question = Text(f"{MULTIPLICAND} × {MULTIPLIER} = ?", font_size=45).move_to(UP * 3.65)
        self.play(Write(title), FadeIn(prompt), Write(question))

        # 右端对齐：每个数的最右一位都位于个位列。
        number_font = "DejaVu Sans Mono"
        top = Text(str(MULTIPLICAND), font=number_font, font_size=66).move_to(
            UP * 2.25 + RIGHT * 1.0
        )
        multiplier = Text(str(MULTIPLIER), font=number_font, font_size=66)
        multiplier.move_to(UP * 1.45).align_to(top, RIGHT)
        sign = Text("×", font_size=58).next_to(multiplier, LEFT, buff=0.22)
        first_rule = Line(LEFT * 1.65, RIGHT * 1.65).move_to(UP * 0.95 + RIGHT * 0.5)
        self.play(Write(top), Write(multiplier), Write(sign), Create(first_rule))

        def digit_row(value: int, y: float, color):
            row = Text(str(value), font=number_font, font_size=61, color=color)
            row.move_to(UP * y).align_to(top, RIGHT)
            return row

        first = digit_row(units, 0.15, BLUE_B)
        second = digit_row(tens, -0.62, GREEN_B)
        second_rule = Line(LEFT * 1.65, RIGHT * 1.65).move_to(
            DOWN * 1.15 + RIGHT * 0.5
        )
        total = digit_row(answer, -2.0, YELLOW)

        first_hint = Text(
            f"个位：{unit_digit} × {MULTIPLICAND} = {units}", font_size=31, color=BLUE_B
        ).move_to(DOWN * 3.35)
        second_hint = Text(
            f"十位：{tens_digit}个十 × {MULTIPLICAND} = {tens}",
            font_size=29, color=GREEN_B
        ).move_to(DOWN * 3.35)
        second_hint.scale_to_fit_width(7.8)
        total_hint = Text(
            f"两个部分积相加：{units} + {tens} = {answer}",
            font_size=28, color=YELLOW
        ).move_to(DOWN * 3.35)
        total_hint.scale_to_fit_width(7.8)

        self.play(Write(first), FadeIn(first_hint))
        self.wait(0.7)
        self.play(Write(second), ReplacementTransform(first_hint, second_hint))
        self.wait(0.7)
        self.play(Create(second_rule), Write(total), ReplacementTransform(second_hint, total_hint))

        takeaway = Text("十位的部分积要向左错一位", font_size=30).move_to(DOWN * 4.65)
        takeaway.scale_to_fit_width(7.8)
        result = Text(f"答：{MULTIPLICAND} × {MULTIPLIER} = {answer}", font_size=36, color=YELLOW)
        result.scale_to_fit_width(7.8).move_to(DOWN * 5.65)
        self.play(FadeIn(takeaway), Write(result))
        self.wait(2)
