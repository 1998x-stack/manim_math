"""六年级：不等式的三条性质，特别强调负数乘除与零因子。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#131a30"
BLUE_ACCENT = "#60a5fa"
GOLD = "#fbbf24"
RED_ACCENT = "#fb7185"
GREEN_ACCENT = "#34d399"


def transformed_inequality(a: int, b: int, offset: int = 0, factor: int = 1):
    """在 a>b 条件下先同加 offset 再同乘 factor，返回新两端及符号。"""
    if any(type(v) is not int for v in (a, b, offset, factor)) or a <= b:
        raise ValueError("要求整数 a>b；offset、factor 也须为整数")
    lhs = (a + offset) * factor
    rhs = (b + offset) * factor
    relation = ">" if lhs > rhs else "<" if lhs < rhs else "="
    return lhs, rhs, relation


class Topic003不等式及其性质Animation(Scene):
    """同一个不等式分别加数、乘正数、乘负数与乘零。"""

    def construct(self):
        assert transformed_inequality(5, 3, -2) == (3, 1, ">")
        assert transformed_inequality(5, 3, factor=2) == (10, 6, ">")
        assert transformed_inequality(5, 3, factor=-2) == (-10, -6, "<")
        assert transformed_inequality(5, 3, factor=0) == (0, 0, "=")
        self.camera.background_color = BG
        self.watermark = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font_size=17, color=GRAY_B
        ).move_to(UP * 7)
        self.add(self.watermark)
        self.opening()
        self.properties()
        self.warning()
        self.summary()

    def transition(self):
        self.play(
            *[FadeOut(item) for item in list(self.mobjects) if item is not self.watermark],
            run_time=0.35
        )

    def title(self, name):
        text = Text(name, font_size=37, color=GOLD).move_to(UP * 5.7)
        self.play(Write(text))
        return text

    def opening(self):
        title = Text("不等式及其性质", font_size=46).move_to(UP * 3.6)
        fact = MathTex(r"5>3", font_size=62, color=GOLD).move_to(UP * 1.6)
        subtitle = Text("两边做相同运算，方向会变吗？", font_size=29)
        subtitle.move_to(DOWN * 0.6)
        self.play(Write(title), Write(fact))
        self.play(FadeIn(subtitle))
        self.wait(0.8)
        self.transition()

    def properties(self):
        self.title("三条基本性质")
        original = MathTex(r"5>3", font_size=48, color=BLUE_ACCENT).move_to(UP * 4.2)
        self.play(Write(original))
        examples = [
            ("两边都减 2：方向不变", r"5-2>3-2", GREEN_ACCENT),
            ("两边都乘 2：方向不变", r"5\times 2>3\times 2", GREEN_ACCENT),
            ("两边都乘 -2：方向反转", r"5\times(-2)<3\times(-2)", RED_ACCENT),
        ]
        labels = VGroup()
        for message, expr, color in examples:
            text = Text(message, font_size=26, color=color)
            equation = MathTex(expr, font_size=38, color=WHITE)
            pair = VGroup(text, equation).arrange(DOWN, buff=0.13)
            labels.add(pair)
        labels.arrange(DOWN, buff=0.65).move_to(DOWN * 0.4)
        for pair in labels:
            self.play(FadeIn(pair[0]), Write(pair[1]), run_time=0.7)
            self.wait(0.25)
        self.wait(0.6)
        self.transition()

    def warning(self):
        self.title("注意：乘以 0")
        a = MathTex(r"5>3", font_size=55, color=GOLD).move_to(UP * 3)
        b = MathTex(r"5\times0=3\times0", font_size=46, color=RED_ACCENT)
        b.move_to(UP * 0.7)
        self.play(Write(a))
        self.play(Write(b))
        notes = VGroup(
            Text("乘以 0 后，两边相等", font_size=29),
            Text("不能继续写严格的大于号", font_size=29, color=RED_ACCENT),
        ).arrange(DOWN, buff=0.45).move_to(DOWN * 2.3)
        self.play(FadeIn(notes))
        self.wait(0.8)
        self.transition()

    def summary(self):
        self.title("记住符号的方向")
        notes = [
            ("同加或同减一个数", "不变", GREEN_ACCENT),
            ("同乘或同除一个正数", "不变", GREEN_ACCENT),
            ("同乘或同除一个负数", "反向", RED_ACCENT),
            ("同乘 0", "成为等式", GOLD),
        ]
        group = VGroup()
        for statement, result, color in notes:
            content = VGroup(
                Text(statement, font_size=25),
                Text(result, font_size=29, color=color),
            ).arrange(DOWN, buff=0.12)
            group.add(content)
        group.arrange(DOWN, buff=0.65).move_to(UP * 0.3)
        for row in group:
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.4)
        self.wait(1)
