"""四种命题及其关系：固定论域、明确反例、用完整真值表展示等价性。

预览：manim -ql four_propositions.py FourPropositions
"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# 所有镜头使用同一个整数 n、同一组命题。
EXAMPLE_DOMAIN = r"n\in\mathbb{Z}"
EXAMPLE_P = r"n\in 4\mathbb{Z}"
EXAMPLE_Q = r"n\in 2\mathbb{Z}"
EXAMPLE_COUNTEREXAMPLE = 2


def implies(p, q):
    return (not p) or q


def proposition_values(p, q):
    """返回原、逆、否、逆否四种命题的真值。"""
    return (implies(p, q), implies(q, p),
            implies(not p, not q), implies(not q, not p))


class FourPropositions(Scene):
    FONT = "Noto Sans CJK SC"
    COLORS = ("#e74c3c", "#3498db", "#2ecc71", "#f39c12")
    COLOR_EQUIV = "#9b59b6"
    POSITIONS = ((-1.95, 2.20, 0), (1.95, 2.20, 0),
                 (-1.95, -1.50, 0), (1.95, -1.50, 0))
    SPECS = (
        ("原命题", r"p\to q", "4的倍数 ⇒ 偶数"),
        ("逆命题", r"q\to p", "偶数 ⇒ 4的倍数"),
        ("否命题", r"\neg p\to\neg q", "非4的倍数 ⇒ 非偶数"),
        ("逆否命题", r"\neg q\to\neg p", "非偶数 ⇒ 非4的倍数"),
    )

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = self._text("上海初高中数学直通车 @emptyandcalm", 19, GRAY_B)
        self.author_info.move_to(UP * 6.82)
        self.add(self.author_info)
        self.cards = [self._card(title, tex, description, color)
                      for (title, tex, description), color in zip(self.SPECS, self.COLORS)]
        self.show_opening()
        self.show_what_is_proposition()
        self.show_original()
        self.show_converse()
        self.show_inverse()
        self.show_contrapositive()
        self.show_relationship_diagram()
        self.show_equivalence()
        self.show_outro()

    def _text(self, value, size=27, color=WHITE):
        return Text(value, font=self.FONT, font_size=size, color=color)

    def _math(self, value, size=32, color=WHITE):
        obj = MathTex(value, font_size=size, color=color)
        if obj.width > 7.3:
            obj.scale_to_fit_width(7.3)
        return obj

    def _header(self, value, color=YELLOW):
        obj = self._text(value, 35, color).move_to(UP * 5.65)
        self.play(FadeIn(obj), run_time=0.45)
        return obj

    def _card(self, name, formula, caption, color):
        frame = RoundedRectangle(width=3.34, height=1.75, corner_radius=0.14,
                                 stroke_width=2, stroke_color=color)
        heading = self._text(name, 22, color).move_to(UP * 0.56)
        symbol = self._math(formula, 29).move_to(UP * 0.12)
        description = self._text(caption, 17, GRAY_A).move_to(DOWN * 0.52)
        if description.width > 3.12:
            description.scale_to_fit_width(3.12)
        return VGroup(frame, heading, symbol, description)

    def _show_card(self, index):
        self.cards[index].move_to(self.POSITIONS[index])
        self.play(FadeIn(self.cards[index]), run_time=0.65)

    def _example(self, note, latex, color):
        text = self._text(note, 24, color).move_to(DOWN * 4.42)
        if text.width > 7.35:
            text.scale_to_fit_width(7.35)
        formula = self._math(latex, 30, color).next_to(text, DOWN, buff=0.25)
        self.play(FadeIn(text), Write(formula), run_time=0.75)
        self.wait(0.7)
        self.play(FadeOut(text), FadeOut(formula), run_time=0.35)

    def show_opening(self):
        title = self._header("一个命题的四种形式")
        preview = VGroup(*[self._text(name, 25, color)
                           for (name, _, _), color in zip(self.SPECS, self.COLORS)])
        preview.arrange_in_grid(rows=2, cols=2, buff=(0.55, 0.8)).move_to(ORIGIN)
        self.play(FadeIn(preview), run_time=0.8)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(preview), run_time=0.4)

    def show_what_is_proposition(self):
        title = self._header("先固定论域和条件")
        line = self._text("命题是可以判断真假的陈述句", 27, GRAY_A).move_to(UP * 3.55)
        p = self._math("p:\;" + EXAMPLE_P, 35, self.COLORS[0]).move_to(UP * 2.00)
        q = self._math("q:\;" + EXAMPLE_Q, 35, self.COLORS[1]).move_to(UP * 0.72)
        domain = self._math(EXAMPLE_DOMAIN, 31, GRAY_A).move_to(DOWN * 0.76)
        note = self._text("以下四种形式始终使用同一个整数 n", 23, GRAY_A)
        note.move_to(DOWN * 2.35)
        self.play(FadeIn(line), Write(p), Write(q), Write(domain), run_time=1.35)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(0.6)
        self.play(*[FadeOut(obj) for obj in (title, line, p, q, domain, note)], run_time=0.5)

    def show_original(self):
        title = self._header("原命题：若 p，则 q", self.COLORS[0])
        self._show_card(0)
        self._example("4 的倍数一定是偶数：原命题为真", r"p\to q", self.COLORS[0])
        self.play(FadeOut(title), run_time=0.35)

    def show_converse(self):
        title = self._header("逆命题：交换条件与结论", self.COLORS[1])
        self._show_card(1)
        self._example("n=2 是偶数，但不是 4 的倍数", r"q\not\Rightarrow p", self.COLORS[1])
        self.play(FadeOut(title), run_time=0.35)

    def show_inverse(self):
        title = self._header("否命题：同时否定条件与结论", self.COLORS[2])
        self._show_card(2)
        self._example("n=2 不是 4 的倍数，却是偶数", r"\neg p\not\Rightarrow\neg q", self.COLORS[2])
        self.play(FadeOut(title), run_time=0.35)

    def show_contrapositive(self):
        title = self._header("逆否命题：交换并否定", self.COLORS[3])
        self._show_card(3)
        self._example("非偶数的整数不可能是 4 的倍数", r"\neg q\to\neg p", self.COLORS[3])
        self.play(FadeOut(title), run_time=0.35)

    def show_relationship_diagram(self):
        title = self._header("四种命题的变换关系")
        # 上下排保持原-逆、否-逆否；横向为互逆，纵向为互否。
        relations = VGroup(
            Line((-0.25, 2.2, 0), (0.25, 2.2, 0), color=GRAY_B),
            Line((-0.25, -1.5, 0), (0.25, -1.5, 0), color=GRAY_B),
            Line((-1.95, 1.27, 0), (-1.95, -0.55, 0), color=GRAY_B),
            Line((1.95, 1.27, 0), (1.95, -0.55, 0), color=GRAY_B),
        )
        labels = VGroup(
            self._text("互逆", 18, GRAY_B).move_to((0, 3.0, 0)),
            self._text("互逆", 18, GRAY_B).move_to((0, -2.5, 0)),
            self._text("互否", 18, GRAY_B).move_to((-1.38, 0.34, 0)),
            self._text("互否", 18, GRAY_B).move_to((2.52, 0.34, 0)),
        )
        self.play(Create(relations), FadeIn(labels), run_time=0.75)
        equivalences = VGroup(
            self._math(r"(p\to q)\iff(\neg q\to\neg p)", 27, self.COLOR_EQUIV),
            self._math(r"(q\to p)\iff(\neg p\to\neg q)", 27, self.COLOR_EQUIV),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 4.72)
        self.play(FadeIn(equivalences), run_time=0.65)
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(relations), FadeOut(labels),
                  FadeOut(equivalences), *[FadeOut(card) for card in self.cards], run_time=0.65)

    def show_equivalence(self):
        title = self._header("等价关系由真值表保证", self.COLOR_EQUIV)
        x_positions = (-3.20, -2.45, -1.15, 0.10, 1.35, 2.83)
        table = VGroup()
        for heading, x in zip(("p", "q", "原", "逆", "否", "逆否"), x_positions):
            table.add(self._text(heading, 25, YELLOW).move_to((x, 3.80, 0)))
        for row, (p, q) in enumerate(((False, False), (False, True),
                                      (True, False), (True, True))):
            values = (p, q) + proposition_values(p, q)
            for index, (value, x) in enumerate(zip(values, x_positions)):
                color = self.COLOR_EQUIV if index in (2, 5) else WHITE
                cell = self._text("真" if value else "假", 26, color)
                table.add(cell.move_to((x, 2.6 - row, 0)))
        note = self._text("原 ⇔ 逆否；逆 ⇔ 否（其他配对不保证等价）", 23, GRAY_A)
        note.move_to(DOWN * 3.0)
        if note.width > 7.35:
            note.scale_to_fit_width(7.35)
        self.play(FadeIn(table), run_time=0.9)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(1.1)
        self.play(FadeOut(title), FadeOut(table), FadeOut(note), run_time=0.6)

    def show_outro(self):
        summary = self._text("原与逆否等价，逆与否等价", 34, self.COLOR_EQUIV)
        summary.move_to(UP * 1.0)
        self.play(FadeIn(summary), run_time=0.55)
        self.wait(1.1)
        self.play(FadeOut(summary), FadeOut(self.author_info), run_time=0.6)
