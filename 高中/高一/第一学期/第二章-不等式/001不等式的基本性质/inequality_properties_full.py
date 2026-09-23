"""不等式的基本性质：每一步数轴数值、公式与数学条件均保持一致。

预览：manim -ql inequality_properties_full.py InequalityPropertiesFull
正式渲染、字体、TeX 及 Mobject 边界需在有依赖的环境单独验收。
"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# 上下两根数轴各展示同一对数字在操作前后的实际值。
# 每条记录：操作前两数、操作后两数、原不等号、最终不等号。
NUMBER_LINE_CASES = {
    "symmetry": ((3, 1), (1, 3), ">", "<"),
    "transitivity": ((4, 2), (4, -1), ">", ">"),
    "addition": ((3, 1), (1, -1), ">", ">"),
    "positive": ((2, 1), (4, 2), ">", ">"),
    "negative": ((2, 1), (-4, -2), ">", "<"),
}
SQUARE_SIDES = (3, 2)
SQUARE_UNIT = 0.61


class InequalityPropertiesFull(Scene):
    """保留开场、六项性质、总结、片尾共九个教学环节。"""

    FONT = "Noto Sans CJK SC"
    C_PRIMARY = "#3498db"
    C_SECONDARY = "#e74c3c"
    C_POSITIVE = "#2ecc71"
    C_NEGATIVE = "#e67e22"
    C_WARNING = "#f39c12"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = self._text("上海初高中数学直通车 @emptyandcalm", 18, GRAY_B)
        self.author_info.move_to(UP * 6.78)
        self.add(self.author_info)
        self.show_opening()
        self.show_property_1()
        self.show_property_2()
        self.show_property_3()
        self.show_property_4()
        self.show_property_5()
        self.show_property_6()
        self.show_summary()
        self.show_outro()

    def _text(self, content, size=26, color=WHITE):
        return Text(content, font=self.FONT, font_size=size, color=color)

    def _formula(self, content, size=36, color=WHITE, max_width=7.35):
        formula = MathTex(content, font_size=size, color=color)
        if formula.width > max_width:
            formula.scale_to_fit_width(max_width)
        return formula

    def _header(self, content, color=YELLOW):
        heading = self._text(content, 35, color).move_to(UP * 5.65)
        self.play(FadeIn(heading), run_time=0.5)
        return heading

    def _number_line(self, numbers, y):
        line = NumberLine(x_range=[-6, 6, 1], length=7.1, include_numbers=True,
                          font_size=18).move_to(UP * y)
        first, second = numbers
        dots = VGroup(Dot(line.n2p(first), radius=0.11, color=self.C_PRIMARY),
                      Dot(line.n2p(second), radius=0.11, color=self.C_SECONDARY))
        labels = VGroup(
            self._formula(str(first), 28, self.C_PRIMARY).next_to(dots[0], UP, buff=0.20),
            self._formula(str(second), 28, self.C_SECONDARY).next_to(dots[1], UP, buff=0.20),
        )
        return VGroup(line, dots, labels)

    def _show_case(self, key, heading, general_rule, top_example,
                   bottom_example, operation, conclusion, accent=None):
        before, after, before_sign, after_sign = NUMBER_LINE_CASES[key]
        if not (-6 <= min(*before, *after) and max(*before, *after) <= 6):
            raise ValueError("数轴样例超出设定的显示范围")
        compare = lambda values, sign: values[0] > values[1] if sign == ">" else values[0] < values[1]
        if not (compare(before, before_sign) and compare(after, after_sign)):
            raise ValueError("数字与屏幕不等号不一致")
        color = accent or self.C_PRIMARY
        title = self._header(heading, color)
        law = self._formula(general_rule, 30).move_to(UP * 4.6)
        self.play(Write(law), run_time=0.75)
        initial = self._number_line(before, 2.65)
        initial_formula = self._formula(top_example, 35).move_to(UP * 1.26)
        self.play(FadeIn(initial), Write(initial_formula), run_time=0.8)
        note = self._text(operation, 25, color).move_to(ORIGIN)
        self.play(FadeIn(note), run_time=0.42)
        final = self._number_line(after, -1.65)
        final_formula = self._formula(bottom_example, 35, color).move_to(DOWN * 3.08)
        self.play(FadeIn(final), Write(final_formula), run_time=0.82)
        explanation = self._text(conclusion, 23, GRAY_A).move_to(DOWN * 4.45)
        if explanation.width > 7.35:
            explanation.scale_to_fit_width(7.35)
        self.play(FadeIn(explanation), run_time=0.48)
        self.wait(0.7)
        self.play(*[FadeOut(m) for m in (title, law, initial, initial_formula,
                                         note, final, final_formula, explanation)],
                  run_time=0.55)

    def show_opening(self):
        title = self._header("不等式的六项基本性质")
        question = self._formula(r"3>1", 54, YELLOW).move_to(UP * 2.5)
        operation = self._text("两边同时乘以 -2，会发生什么？", 27, GRAY_A).move_to(ORIGIN)
        result = self._formula(r"-6<-2", 52, self.C_WARNING).move_to(DOWN * 2.5)
        self.play(Write(question), FadeIn(operation), run_time=0.8)
        self.play(Write(result), run_time=0.65)
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(question), FadeOut(operation),
                  FadeOut(result), run_time=0.55)

    def show_property_1(self):
        self._show_case(
            "symmetry", "性质一：对称性", r"a>b\iff b<a",
            r"3>1", r"1<3", "交换不等号两边的位置", "交换左右两端，不等号方向随之改变",
        )

    def show_property_2(self):
        self._show_case(
            "transitivity", "性质二：传递性", r"a>b,\ b>c\Longrightarrow a>c",
            r"4>2>-1", r"4>-1", "已知 4>2 且 2>-1", "两个相邻比较连接得出 4>-1",
        )

    def show_property_3(self):
        self._show_case(
            "addition", "性质三：两边同加", r"a>b\Longrightarrow a+c>b+c",
            r"3>1", r"1>-1", "两边同加 -2", "同加任意实数，方向保持不变",
        )

    def show_property_4(self):
        self._show_case(
            "positive", "性质四：乘以正数", r"a>b,\ c>0\Longrightarrow ac>bc",
            r"2>1", r"4>2", "两边同乘正数 2", "正数乘法保持大小关系",
            accent=self.C_POSITIVE,
        )

    def show_property_5(self):
        self._show_case(
            "negative", "性质五：乘以负数", r"a>b,\ c<0\Longrightarrow ac<bc",
            r"2>1", r"-4<-2", "两边同乘负数 -2", "注意：乘负数必须反转不等号！",
            accent=self.C_NEGATIVE,
        )

    def show_property_6(self):
        title = self._header("性质六：正数的平方", self.C_PRIMARY)
        condition = self._formula(r"a>b>0\Longrightarrow a^2>b^2", 34)
        condition.move_to(UP * 4.4)
        self.play(Write(condition), run_time=0.75)
        # 同一单位正方形拼成的 3x3 和 2x2 网格，显示面积恰好为 9、4。
        diagrams = VGroup()
        for n, center, color in ((SQUARE_SIDES[0], LEFT * 1.95 + UP * 1.20, self.C_PRIMARY),
                                 (SQUARE_SIDES[1], RIGHT * 1.95 + UP * 1.20, self.C_SECONDARY)):
            grid = VGroup(*[Square(side_length=SQUARE_UNIT, stroke_width=1.5,
                                   stroke_color=color, fill_color=color, fill_opacity=0.20)
                            for _ in range(n * n)])
            grid.arrange_in_grid(rows=n, cols=n, buff=0).move_to(center)
            label = self._formula(str(n), 31, color).next_to(grid, UP, buff=0.22)
            area = self._formula(f"{n}^2={n * n}", 37, color).next_to(grid, DOWN, buff=0.28)
            diagrams.add(VGroup(grid, label, area))
        self.play(FadeIn(diagrams), run_time=1.0)
        conclusion = self._formula(r"3^2=9>4=2^2", 39, self.C_POSITIVE)
        conclusion.move_to(DOWN * 2.20)
        self.play(Write(conclusion), run_time=0.7)
        warning = self._text("不能省略正数前提：-3<-2，但 9>4", 24, self.C_WARNING)
        warning.move_to(DOWN * 3.85)
        if warning.width > 7.35:
            warning.scale_to_fit_width(7.35)
        self.play(FadeIn(warning), run_time=0.55)
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(condition), FadeOut(diagrams),
                  FadeOut(conclusion), FadeOut(warning), run_time=0.60)

    def show_summary(self):
        title = self._header("六项性质：条件与方向")
        rows = (
            ("对称", r"a>b\iff b<a"),
            ("传递", r"a>b,\ b>c\Rightarrow a>c"),
            ("同加", r"a>b\Rightarrow a+c>b+c"),
            ("乘正数", r"a>b,\ c>0\Rightarrow ac>bc"),
            ("乘负数", r"a>b,\ c<0\Rightarrow ac<bc"),
            ("正数平方", r"a>b>0\Rightarrow a^2>b^2"),
        )
        cards = VGroup()
        for i, (label, tex) in enumerate(rows):
            color = self.C_NEGATIVE if i == 4 else WHITE
            border = RoundedRectangle(width=7.55, height=1.04, corner_radius=0.13,
                                      color=color, stroke_width=2)
            name = self._text(label, 22, color).move_to(LEFT * 2.64)
            formula = self._formula(tex, 26, color, max_width=4.8).move_to(RIGHT * 0.86)
            card = VGroup(border, name, formula).move_to(UP * (3.88 - 1.30 * i))
            cards.add(card)
            self.play(FadeIn(card), run_time=0.32)
        note = self._text("特别注意：c=0 时两边相等，不能保留严格不等号", 22, self.C_WARNING)
        note.move_to(DOWN * 4.7)
        if note.width > 7.35:
            note.scale_to_fit_width(7.35)
        self.play(FadeIn(note), run_time=0.45)
        self.wait(1.1)
        self.play(FadeOut(title), FadeOut(cards), FadeOut(note), run_time=0.62)

    def show_outro(self):
        title = self._text("先检查条件，再判断不等号方向", 32, YELLOW)
        title.move_to(UP * 1.0)
        self.play(FadeIn(title), run_time=0.55)
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(self.author_info), run_time=0.60)
