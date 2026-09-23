"""四种命题及其关系：同一组条件、反例和完整真值表。

预览：manim -ql four_propositions.py FourPropositions
视频及中文字体验收需要在实际 Manim + TeX 环境执行。
"""

from manim import *


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# 贯穿四种命题的同一个例子：论域始终是整数。
# p: n 是 4 的倍数；q: n 是偶数。n=2 是逆命题和否命题的反例。
EXAMPLE_DOMAIN = "n\\in\\mathbb{Z}"
EXAMPLE_P = "n\\in 4\\mathbb{Z}"
EXAMPLE_Q = "n\\in 2\\mathbb{Z}"
EXAMPLE_COUNTEREXAMPLE = 2


def implies(p, q):
    """仅用于生成屏幕真值表；不依赖 Manim。"""
    return (not p) or q


def proposition_values(p, q):
    """顺序：原、逆、否、逆否；两组配对的真值应始终相等。"""
    return (implies(p, q), implies(q, p),
            implies(not p, not q), implies(not q, not p))


class FourPropositions(Scene):
    FONT = "Noto Sans CJK SC"
    COLORS = ("#e74c3c", "#3498db", "#2ecc71", "#f39c12")
    COLOR_EQUIV = "#9b59b6"
    POSITION = ((-1.95, 2.25, 0), (1.95, 2.25, 0),
                (-1.95, -1.5, 0), (1.95, -1.5, 0))
    # 四框布局：原/逆位于上方，否/逆否位于下方。
    SPECS = (
        ("原命题", r"p\\rightarrow q", "4的倍数  ⇒  偶数"),
        ("逆命题", r"q\\rightarrow p", "偶数  ⇒  4的倍数"),
        ("否命题", r"\\neg p\\rightarrow\\neg q", "非4的倍数 ⇒ 非偶数"),
        ("逆否命题", r"\\neg q\\rightarrow\\neg p", "非偶数 ⇒ 非4的倍数"),
    )

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = self._text("上海初高中数学直通车 @emptyandcalm", 19, GRAY_B)
        self.author_info.move_to(UP * 6.8)
        self.add(self.author_info)
        self.cards = [self._card(*spec, color) for spec, color in zip(self.SPECS, self.COLORS)]
        self.show_opening()
        self.show_what_is_proposition()
        self.show_original()
        self.show_converse()
        self.show_inverse()
        self.show_contrapositive()
        self.show_relationship_diagram()
        self.show_equivalence()
        self.show_outro()

    def _text(self, content, size=27, color=WHITE):
        return Text(content, font=self.FONT, font_size=size, color=color)

    def _math(self, content, size=32, color=WHITE):
        result = MathTex(content, font_size=size, color=color)
        if result.width > 7.3:
            result.scale_to_fit_width(7.3)
        return result

    def _header(self, title, color=YELLOW):
        header = self._text(title, 36, color).move_to(UP * 5.63)
        self.play(FadeIn(header), run_time=0.48)
        return header

    def _card(self, title, formula, description, color):
        frame = RoundedRectangle(width=3.32, height=1.77, corner_radius=0.14,
                                 stroke_color=color, stroke_width=2)
        title_obj = self._text(title, 22, color).move_to(frame.get_center() + UP * 0.59)
        symbol = self._math(formula, 29).move_to(frame.get_center() + UP * 0.10)
        caption = self._text(description, 16, GRAY_A).move_to(frame.get_center() + DOWN * 0.52)
        if caption.width > 3.05:
            caption.scale_to_fit_width(3.05)
        return VGroup(frame, title_obj, symbol, caption)

    def _show_card(self, index):
        self.cards[index].move_to(self.POSITION[index])
        self.play(FadeIn(self.cards[index]), run_time=0.68)

    def _example(self, explanation, formula=None, color=WHITE):
        sentence = self._text(explanation, 24, color).move_to(DOWN * 4.45)
        if sentence.width > 7.4:
            sentence.scale_to_fit_width(7.4)
        self.play(FadeIn(sentence), run_time=0.55)
        if formula is None:
            self.wait(0.5)
            self.play(FadeOut(sentence), run_time=0.35)
            return
        example_formula = self._math(formula, 30, color).next_to(sentence, DOWN, buff=0.27)
        self.play(Write(example_formula), run_time=0.65)
        self.wait(0.65)
        self.play(FadeOut(sentence), FadeOut(example_formula), run_time=0.36)

    def show_opening(self):
        header = self._header("一个命题的四种形式")
        subtitles = VGroup(*[self._text(title, 25, color)
                             for (title, _, _), color in zip(self.SPECS, self.COLORS)])
        subtitles.arrange_in_grid(rows=2, cols=2, buff=(0.45, 0.7)).move_to(ORIGIN)
        self.play(FadeIn(subtitles), run_time=0.85)
        self.wait(0.45)
        self.play(FadeOut(header), FadeOut(subtitles), run_time=0.48)

    def show_what_is_proposition(self):
        header = self._header("先固定论域和条件")
        rule = self._text("命题是可以判断真假的陈述句", 28, GRAY_A).move_to(UP * 3.7)
        p = self._math(r"p:\;" + EXAMPLE_P, 34, self.COLORS[0]).move_to(UP * 2.0)
        q = self._math(r"q:\;" + EXAMPLE_Q, 34, self.COLORS[1]).move_to(UP * 0.75)
        domain = self._math(EXAMPLE_DOMAIN, 30, GRAY_A).move_to(DOWN * 0.8)
        note = self._text("以下四种命题始终使用同一个整数 n", 24, GRAY_A)
        note.move_to(DOWN * 2.4)
        self.play(FadeIn(rule), Write(p), Write(q), Write(domain), run_time=1.25)
        self.play(FadeIn(note), run_time=0.48)
        self.wait(0.6)
        self.play(*[FadeOut(m) for m in (header, rule, p, q, domain, note)], run_time=0.55)

    def show_original(self):
        header = self._header("原命题：若 p，则 q", self.COLORS[0])
        self._show_card(0)
        self._example("4 的倍数一定是偶数：原命题为真", r"p\\rightarrow q", self.COLORS[0])
        self.play(FadeOut(header), run_time=0.4)

    def show_converse(self):
        header = self._header("逆命题：交换条件与结论", self.COLORS[1])
        self._show_card(1)
        self._example("n=2 是偶数，但不是 4 的倍数", r"q\\not\\Rightarrow p", self.COLORS[1])
        self.play(FadeOut(header), run_time=0.4)

    def show_inverse(self):
        header = self._header("否命题：同时否定条件与结论", self.COLORS[2])
        self._show_card(2)
        self._example("n=2 不是 4 的倍数，却是偶数", r"\\neg p\\not\\Rightarrow\\neg q", self.COLORS[2])
        self.play(FadeOut(header), run_time=0.4)

    def show_contrapositive(self):
        header = self._header("逆否命题：交换并否定", self.COLORS[3])
        self._show_card(3)
        self._example("不是偶数的整数不可能是 4 的倍数", r"\\neg q\\rightarrow\\neg p", self.COLORS[3])
        self.play(FadeOut(header), run_time=0.4)

    def show_relationship_diagram(self):
        header = self._header("四种命题的变换关系")
        # 连线端点位于卡片间隙，不穿过命题文字。
        arrows = VGroup(
            DoubleArrow((-0.23, 2.25, 0), (0.23, 2.25, 0), buff=0, color=GRAY_B),
            DoubleArrow((-0.23, -1.5, 0), (0.23, -1.5, 0), buff=0, color=GRAY_B),
            DoubleArrow((-1.95, 1.30, 0), (-1.95, -0.53, 0), buff=0, color=GRAY_B),
            DoubleArrow((1.95, 1.30, 0), (1.95, -0.53, 0), buff=0, color=GRAY_B),
        )
        labels = VGroup(
            self._text("互逆", 18, GRAY_B).move_to((0, 3.05, 0)),
            self._text("互逆", 18, GRAY_B).move_to((0, -2.48, 0)),
            self._text("互否", 18, GRAY_B).move_to((-1.38, 0.4, 0)),
            self._text("互否", 18, GRAY_B).move_to((2.52, 0.4, 0)),
        )
        self.play(Create(arrows), FadeIn(labels), run_time=0.85)
        pairing = VGroup(
            self._math(r"(p\\to q)\\iff(\\neg q\\to\\neg p)", 26, self.COLOR_EQUIV),
            self._math(r"(q\\to p)\\iff(\\neg p\\to\\neg q)", 26, self.COLOR_EQUIV),
        ).arrange(DOWN, buff=0.26).move_to(DOWN * 4.75)
        self.play(FadeIn(pairing), run_time=0.72)
        self.wait(1.0)
        self.play(FadeOut(header), FadeOut(arrows), FadeOut(labels), FadeOut(pairing),
                  *[FadeOut(card) for card in self.cards], run_time=0.72)

    def show_equivalence(self):
        header = self._header("等价关系由真值表保证", self.COLOR_EQUIV)
        columns = ["p", "q", "原", "逆", "否", "逆否"]
        x_positions = (-3.25, -2.45, -1.15, 0.1, 1.35, 2.85)
        table = VGroup()
        for text, x in zip(columns, x_positions):
            table.add(self._text(text, 25, YELLOW).move_to((x, 3.85, 0)))
        for row, (p, q) in enumerate(((False, False), (False, True),
                                      (True, False), (True, True))):
            states = (p, q) + proposition_values(p, q)
            for state, x in zip(states, x_positions):
                cell = self._text("真" if state else "假", 26,
                                  self.COLOR_EQUIV if x in (-1.15, 2.85) else WHITE)
                cell.move_to((x, 2.65 - 1.0 * row, 0))
                table.add(cell)
        note = self._text("原 ⇔ 逆否；逆 ⇔ 否（其余不保证等价）", 23, GRAY_A)
        note.move_to(DOWN * 3.0)
        if note.width > 7.35:
            note.scale_to_fit_width(7.35)
        self.play(FadeIn(table), run_time=0.95)
        self.play(FadeIn(note), run_time=0.55)
        self.wait(1.2)
        self.play(FadeOut(header), FadeOut(table), FadeOut(note), run_time=0.6)

    def show_outro(self):
        summary = self._text("原与逆否等价，逆与否等价", 34, self.COLOR_EQUIV)
        summary.move_to(UP * 1.0)
        self.play(FadeIn(summary), run_time=0.55)
        self.wait(1.3)
        self.play(FadeOut(summary), FadeOut(self.author_info), run_time=0.6)
