"""7、8、9 的乘法口诀：算式、口诀与点阵数量逐条一致。"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

CHINESE_DIGITS = ("零", "一", "二", "三", "四", "五", "六", "七", "八", "九")


def chinese_number(value):
    """生成本课涉及的 1～81 的汉字数字，避免手写口诀与算式不一致。"""
    if not 1 <= value <= 81:
        raise ValueError("本课只使用 1～81 之间的正整数")
    if value < 10:
        return CHINESE_DIGITS[value]
    tens, ones = divmod(value, 10)
    return ("十" if tens == 1 else CHINESE_DIGITS[tens] + "十") + (
        CHINESE_DIGITS[ones] if ones else ""
    )


def multiplication_mnemonic(factor, multiplier):
    if not (7 <= factor <= 9 and 1 <= multiplier <= factor):
        raise ValueError("口诀范围应为 7～9 的乘法表")
    value = factor * multiplier
    prefix = CHINESE_DIGITS[multiplier] + CHINESE_DIGITS[factor]
    return prefix + ("得" if value < 10 else "") + chinese_number(value)


class MultiplyTableAnimation(Scene):
    """每条口诀只展示一组点阵；清理上一条，防止重复点阵堆积。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("7、8、9的乘法口诀", font_size=44, color=GOLD)
        title.move_to(UP * 6.2)
        self.play(Write(title))
        for factor in (7, 8, 9):
            self.show_table(factor)
        self.play(FadeOut(title))
        relation = VGroup(
            MathTex(r"7\times8=56", font_size=62),
            MathTex(r"56\div7=8", font_size=62),
            Text("乘法口诀也能帮助我们求商", font_size=27),
        ).arrange(DOWN, buff=0.7).move_to(ORIGIN)
        self.play(FadeIn(relation))
        self.wait(2)

    def show_table(self, factor):
        heading = Text(f"{factor}的乘法口诀", font_size=35, color=BLUE_B)
        heading.move_to(UP * 4.9)
        self.play(Write(heading))
        previous = None
        for multiplier in range(1, factor + 1):
            product = factor * multiplier
            assert product == len(range(factor * multiplier))
            equation = MathTex(
                rf"{multiplier}\times{factor}={product}", font_size=64
            ).move_to(UP * 3.45)
            mnemonic = Text(
                multiplication_mnemonic(factor, multiplier), font_size=34,
                color=YELLOW
            ).move_to(UP * 2.45)
            # multiplier 行，每行 factor 个点，实际数量恰好等于乘积。
            dots = VGroup(*[
                Dot(radius=0.095, color=BLUE_B).move_to([
                    (col - (factor - 1) / 2) * 0.42,
                    (row - (multiplier - 1) / 2) * 0.42,
                    0,
                ])
                for row in range(multiplier)
                for col in range(factor)
            ])
            assert len(dots) == product
            count = Text(
                f"{multiplier}组，每组{factor}个，共{product}个",
                font_size=26, color=GRAY_A
            ).move_to(DOWN * 3.25)
            current = VGroup(equation, mnemonic, dots, count)
            if previous is not None:
                self.play(FadeOut(previous), run_time=0.25)
            self.play(FadeIn(current), run_time=0.55)
            self.wait(0.4)
            previous = current
        if previous is not None:
            self.play(FadeOut(previous), FadeOut(heading), run_time=0.5)
