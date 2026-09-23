"""一元二次方程的概念：八年级第一学期，第十七章。

运行：manim -pql <本文件> 一元二次方程的概念Animation
保留原有 Scene 类名和竖屏尺寸，便于已有索引继续引用。
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class 一元二次方程的概念Animation(Scene):
    BG = "#1a1a2e"
    BLUE = "#3498db"
    GREEN = "#2ecc71"
    YELLOW = "#f1c40f"
    GRAY = "#95a5a6"
    FONT = "PingFang SC"

    def construct(self):
        self.camera.background_color = self.BG
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT, font_size=20, color=GRAY_B,
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_info), run_time=0.3)
        self.show_opening()
        self.show_definition()
        self.show_general_form()
        self.show_coefficient_explanation()
        self.show_comparison()
        self.show_summary()

    def _text(self, message, y, *, size=29, color=WHITE):
        """中文字幕使用 Text，而不是交给 LaTeX 编译。"""
        return Text(message, font=self.FONT, font_size=size, color=color).move_to(UP * y)

    def _formula(self, tex, y, *, size=42, color=WHITE):
        return MathTex(tex, font_size=size, color=color).move_to(UP * y)

    def _clear(self):
        """仅淡出实际存在的顶层对象；保留水印，不制造虚假的待删除对象。"""
        visible = [mob for mob in self.mobjects if mob is not self.author_info]
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.4)

    def show_opening(self):
        title = self._text("一元二次方程的概念", 5.4, size=44, color=self.YELLOW)
        subtitle = self._text("Quadratic Equation", 4.5, size=26, color=GRAY_A)
        self.play(Write(title), FadeIn(subtitle), run_time=0.9)
        self.wait(0.5)
        self._clear()

    def show_definition(self):
        title = self._text("什么是一元二次方程？", 5.7, size=36, color=self.YELLOW)
        definition = self._text(
            "整理后只含一个未知数，\n且最高次数是 2 的整式方程",
            3.7, size=29, color=self.BLUE,
        )
        example = self._formula(r"x^2-3x+2=0", 1.4, color=self.GREEN)
        notes = VGroup(
            self._text("一个未知数", 0, color=self.YELLOW),
            self._text("整式方程", 0, color=self.YELLOW),
            self._text("整理后次数为 2", 0, color=self.YELLOW),
        ).arrange(DOWN, buff=0.45).move_to(DOWN * 1.4)
        self.play(Write(title), Write(definition), run_time=1.0)
        self.play(Write(example), run_time=0.6)
        for note in notes:
            self.play(FadeIn(note), run_time=0.25)
        self.wait(0.6)
        self._clear()

    def show_general_form(self):
        title = self._text("一般形式", 5.7, size=38, color=self.YELLOW)
        terms = MathTex(
            r"ax^2", "+", r"bx", "+", "c", "=", "0",
            font_size=52, color=WHITE,
        ).move_to(UP * 3.8)
        condition = self._formula(r"a\ne 0", 2.9, color=self.YELLOW)
        self.play(Write(title), Write(terms), Write(condition), run_time=1.0)

        # 复用同一个矩形对象，在真实对象上做 ReplacementTransform。
        term_colors = (self.YELLOW, self.GREEN, self.GRAY)
        names = ("二次项", "一次项", "常数项")
        rectangle = SurroundingRectangle(terms[0], color=term_colors[0], buff=0.12)
        label = self._text(names[0], 1.5, size=29, color=term_colors[0])
        self.play(Create(rectangle), FadeIn(label), run_time=0.4)
        for index, target in enumerate((terms[2], terms[4]), start=1):
            next_rectangle = SurroundingRectangle(
                target, color=term_colors[index], buff=0.12,
            )
            next_label = self._text(names[index], 1.5, size=29, color=term_colors[index])
            self.play(
                ReplacementTransform(rectangle, next_rectangle),
                ReplacementTransform(label, next_label), run_time=0.45,
            )
            rectangle, label = next_rectangle, next_label
        self.wait(0.5)
        self._clear()

    def show_coefficient_explanation(self):
        title = self._text("系数有什么含义？", 5.7, size=37, color=self.YELLOW)
        formula = self._formula(r"ax^2+bx+c=0", 4.4, size=48)
        rows = (
            (r"a", "二次项系数", self.YELLOW),
            (r"b", "一次项系数", self.GREEN),
            (r"c", "常数项", self.GRAY),
        )
        labels = VGroup(*[
            VGroup(
                MathTex(symbol, color=color, font_size=40),
                Text(description, font=self.FONT, color=WHITE, font_size=28),
            ).arrange(RIGHT, buff=0.35)
            for symbol, description, color in rows
        ]).arrange(DOWN, buff=0.7).move_to(UP * 1.2)
        reminder = self._text("必须有 a ≠ 0，否则不是一元二次方程", -2.0,
                              size=25, color=self.YELLOW)
        self.play(Write(title), Write(formula), run_time=0.9)
        for label in labels:
            self.play(FadeIn(label), run_time=0.3)
        self.play(Write(reminder), run_time=0.6)
        self.wait(0.6)
        self._clear()

    def show_comparison(self):
        title = self._text("先整理，再判断次数", 5.7, size=36, color=self.YELLOW)
        examples = (
            (r"x(x+1)=0", "整理后为二次方程", self.GREEN),
            (r"x^2-x^2+x=0", "整理后为一次方程", self.BLUE),
            (r"x^3+x=0", "最高次数为 3", self.GRAY),
        )
        self.play(Write(title), run_time=0.5)
        for i, (tex, explanation, color) in enumerate(examples):
            y = 3.8 - 2.35 * i
            expression = self._formula(tex, y, size=38, color=color)
            comment = self._text(explanation, y - 0.68, size=25, color=WHITE)
            self.play(Write(expression), FadeIn(comment), run_time=0.6)
        self.wait(0.8)
        self._clear()

    def show_summary(self):
        title = self._text("总结", 5.7, size=42, color=self.YELLOW)
        formula = self._formula(r"ax^2+bx+c=0,\quad a\ne0", 3.8, size=40)
        principle = self._text("一个未知数 · 整式方程 · 整理后二次", 1.9,
                               size=27, color=self.GREEN)
        ending = self._text("记得先化简，再确认二次项系数！", -0.1,
                            size=28, color=self.YELLOW)
        self.play(Write(title), Write(formula), run_time=0.8)
        self.play(FadeIn(principle), FadeIn(ending), run_time=0.7)
        self.wait(1.5)
