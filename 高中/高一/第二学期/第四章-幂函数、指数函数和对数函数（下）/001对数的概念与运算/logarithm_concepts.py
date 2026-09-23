"""高一第二学期：对数的概念与运算（竖屏教学动画）。

运行：manim -ql logarithm_concepts.py LogarithmConcepts
数学约定：所有对数在实数范围内讨论；不能把近似小数写成精确等式。
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

AUTHOR_NAME = "上海初高中数学直通车"
AUTHOR_ID = "@emptyandcalm"
AUTHOR_FONT = "PingFang SC"
COLOR_PRIMARY = "#3498db"
COLOR_SECONDARY = "#e74c3c"
COLOR_FORMULA = "#2ecc71"
COLOR_EXPONENT = "#9b59b6"
COLOR_LOGARITHM = "#e67e22"


class LogarithmConcepts(Scene):
    """七镜：从指数式到对数，再到运算与换底。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = Text(
            f"{AUTHOR_NAME} {AUTHOR_ID}", font=AUTHOR_FONT,
            font_size=17, color=GRAY_B,
        ).move_to(DOWN * 6.7)
        self.add(self.author_info)
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_special_logs()
        self.scene_4_identities()
        self.scene_5_operations_part1()
        self.scene_6_operations_part2()
        self.scene_7_outro()
        self.play(FadeOut(self.author_info), run_time=0.4)

    @staticmethod
    def _formula(latex, size=29, color=WHITE):
        """数学公式不含中文；长公式按整对象缩放以留出竖屏边距。"""
        formula = MathTex(latex, font_size=size, color=color)
        if formula.width > 7.3:
            formula.scale_to_fit_width(7.3)
        return formula

    def _page(self, heading, cards, note):
        """每镜只淡出真实上屏的同一对象，避免淡出临时 VGroup 后残留。"""
        title = Text(heading, font=AUTHOR_FONT, font_size=35,
                     color=COLOR_PRIMARY).move_to(UP * 5.7)
        displayed = [title]
        self.play(Write(title), run_time=0.65)
        card_mobjects = VGroup()
        for label, formulas, color in cards:
            caption = Text(label, font=AUTHOR_FONT, font_size=23, color=color)
            lines = VGroup(*(self._formula(formula, size=26) for formula in formulas))
            lines.arrange(DOWN, buff=0.16)
            content = VGroup(caption, lines).arrange(DOWN, buff=0.19)
            border = SurroundingRectangle(content, buff=0.22,
                                          corner_radius=0.12, color=color,
                                          stroke_width=2)
            card_mobjects.add(VGroup(border, content))
        card_mobjects.arrange(DOWN, buff=0.36).move_to(DOWN * 0.15)
        # 章节中的四张单行卡片也必须位于作者栏与标题之间。
        if card_mobjects.height > 8.7:
            card_mobjects.scale_to_fit_height(8.7)
        if card_mobjects.width > 7.8:
            card_mobjects.scale_to_fit_width(7.8)
        for card in card_mobjects:
            self.play(FadeIn(card, shift=UP * 0.14), run_time=0.65)
            displayed.append(card)
        note_obj = Text(note, font=AUTHOR_FONT, font_size=19,
                        color=GRAY_A).move_to(DOWN * 5.5)
        if note_obj.width > 7.5:
            note_obj.scale_to_fit_width(7.5)
        self.play(FadeIn(note_obj), run_time=0.45)
        displayed.append(note_obj)
        self.wait(1.0)
        self.play(*(FadeOut(obj) for obj in displayed), run_time=0.55)

    def scene_1_opening(self):
        title = Text("2 的几次方等于 8？", font=AUTHOR_FONT,
                     font_size=35, color=WHITE).move_to(UP * 5.1)
        self.play(Write(title), run_time=0.7)
        bars = VGroup()
        for exponent in range(4):
            blocks = VGroup(*(
                Square(side_length=0.31, stroke_width=1,
                       color=COLOR_EXPONENT, fill_opacity=0.75)
                for _ in range(2 ** exponent)
            )).arrange(RIGHT, buff=0.06)
            label = self._formula(r"2^{%d}=%d" % (exponent, 2 ** exponent),
                                  size=25, color=COLOR_EXPONENT)
            bars.add(VGroup(label, blocks).arrange(RIGHT, buff=0.45))
        bars.arrange(DOWN, buff=0.48, aligned_edge=LEFT).move_to(UP * 1.0)
        for row in bars:
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.35)
        answer = self._formula(r"2^3=8\quad\Longleftrightarrow\quad\log_2 8=3",
                               size=31, color=YELLOW).move_to(DOWN * 3.1)
        explanation = Text("求指数 3，可以写成求对数", font=AUTHOR_FONT,
                           font_size=23, color=WHITE).next_to(answer, DOWN, buff=0.43)
        self.play(Write(answer), FadeIn(explanation), run_time=1.0)
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(bars), FadeOut(answer),
                  FadeOut(explanation), run_time=0.6)

    def scene_2_definition(self):
        self._page("对数的定义", [
            ("指数式与对数式互相转换", [
                r"a^x=N\quad\Longleftrightarrow\quad x=\log_a N",
                r"2^3=8\quad\Longleftrightarrow\quad\log_2 8=3",
            ], COLOR_LOGARITHM),
            ("底数 a、真数 N、对数 x", [
                r"a>0,\quad a\ne1,\quad N>0",
            ], COLOR_FORMULA),
        ], "条件不可省略：底数必须正且不等于 1，真数必须正")

    def scene_3_special_logs(self):
        self._page("两种特殊对数", [
            ("常用对数：底数是 10", [
                r"\lg N=\log_{10}N", r"\lg 100=2",
            ], COLOR_PRIMARY),
            ("自然对数：底数是 e", [
                r"\ln N=\log_e N", r"\ln e=1,\quad e\approx2.71828",
            ], COLOR_LOGARITHM),
        ], "两种对数的真数 N 都要大于 0")

    def scene_4_identities(self):
        self._page("对数恒等式", [
            ("指数与对数互相抵消", [
                r"a^{\log_a N}=N", r"2^{\log_2 8}=8",
            ], COLOR_FORMULA),
            ("反过来同样成立", [
                r"\log_a(a^t)=t\quad(t\in\mathbb{R})",
            ], COLOR_EXPONENT),
            ("两个常用特例", [
                r"\log_a 1=0,\qquad\log_a a=1",
            ], COLOR_LOGARITHM),
        ], "前提：a > 0 且 a 不等于 1；第一式还要求 N > 0")

    def scene_5_operations_part1(self):
        self._page("对数运算：乘与除", [
            ("乘积变加法", [
                r"\log_a(MN)=\log_a M+\log_a N",
                r"\log_2(4\cdot8)=2+3=5",
            ], COLOR_FORMULA),
            ("商变减法", [
                r"\log_a\left(\frac{M}{N}\right)=\log_a M-\log_a N",
                r"\log_2\left(\frac{8}{4}\right)=3-2=1",
            ], COLOR_SECONDARY),
        ], "两条法则均要求 M > 0、N > 0，且底数合法")

    def scene_6_operations_part2(self):
        self._page("幂运算与换底", [
            ("幂次提到对数前", [
                r"\log_a(M^t)=t\log_a M",
                r"\log_2(8^2)=2\log_2 8=6",
            ], COLOR_FORMULA),
            ("换成另一个合法的底 c", [
                r"\log_a b=\frac{\log_c b}{\log_c a}",
                r"\log_2 8=\frac{\lg 8}{\lg 2}=3",
            ], COLOR_LOGARITHM),
        ], "M、b > 0；a、c > 0 且均不等于 1；t 为实数")

    def scene_7_outro(self):
        self._page("本课四个要点", [
            ("定义", [r"a^x=N\ \Longleftrightarrow\ x=\log_a N"], COLOR_PRIMARY),
            ("恒等式", [r"a^{\log_a N}=N"], COLOR_FORMULA),
            ("乘积法则", [r"\log_a(MN)=\log_a M+\log_a N"], COLOR_SECONDARY),
            ("换底公式", [r"\log_a b=\frac{\log_c b}{\log_c a}"], COLOR_LOGARITHM),
        ], "每次应用公式，先检查底数和真数的取值条件")
