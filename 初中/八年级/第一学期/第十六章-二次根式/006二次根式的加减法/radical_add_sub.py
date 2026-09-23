"""二次根式加减法：八年级第一学期，第十六章。

manim -pql radical_add_sub.py RadicalAddSub
保持原有十段教学方法、Scene 类名、9:16 比例、作者水印。
"""

import math
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def normalized_term(coefficient, radicand):
    """把整数系数的二次根式化最简，保留系数的正负号。"""
    if type(coefficient) is not int or type(radicand) is not int or radicand < 0:
        raise ValueError("本课要求整数系数和非负整数被开方数")
    if coefficient == 0 or radicand == 0:
        return 0, 1
    outside, inside, divisor = coefficient, radicand, 2
    while divisor * divisor <= inside:
        square = divisor * divisor
        while inside % square == 0:
            outside *= divisor
            inside //= square
        divisor += 1
    return outside, inside


def add_subtract_radicals(terms):
    """接收带符号项 (coeff,radicand)，按最简被开方数分组并消去零项。"""
    grouped = {}
    for coeff, radicand in terms:
        outside, inside = normalized_term(coeff, radicand)
        if outside:
            grouped[inside] = grouped.get(inside, 0) + outside
    return {inside: coeff for inside, coeff in sorted(grouped.items()) if coeff}


class RadicalAddSub(Scene):
    BG = "#1a1a2e"
    TITLE = "#f9ca24"
    CYAN = "#58cbd6"
    VIOLET = "#b39efa"
    GREEN = "#87dc9b"
    CORAL = "#f28a8a"
    MUTED = "#bbc9d9"
    PANEL = "#16213e"

    def construct(self):
        self.camera.background_color = self.BG
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font="PingFang SC", font_size=18,
                           color=self.MUTED).move_to(UP * 6.6)
        self.add(self.author)
        self.scene_opening()
        self.scene_three_steps()
        self.scene_ex1_direct()
        self.scene_ex2_main()
        self.scene_ex3_subtract()
        self.scene_ex4_mixed()
        self.scene_cannot_merge()
        self.scene_quick_practice()
        self.scene_summary()
        self.scene_outro()

    def _title(self, message):
        text = Text(message, font="PingFang SC", font_size=39,
                    color=self.TITLE).move_to(UP * 5.8)
        if text.width > 7.8:
            text.scale_to_fit_width(7.8)
        return text

    def _note(self, message, y, color=None):
        text = Text(message, font="PingFang SC", font_size=26,
                    color=color or self.MUTED).move_to(UP * y)
        if text.width > 7.6:
            text.scale_to_fit_width(7.6)
        return text

    def _card(self, y, height, content, color=None):
        border = color or self.CYAN
        frame = RoundedRectangle(corner_radius=0.25, width=7.7, height=height,
                                 stroke_color=border, stroke_width=2,
                                 fill_color=self.PANEL, fill_opacity=0.92).move_to(UP * y)
        body = content if isinstance(content, VGroup) else VGroup(content)
        body.move_to(frame.get_center())
        if body.width > 7.05:
            body.scale_to_fit_width(7.05)
        if body.height > height - 0.24:
            body.scale_to_fit_height(height - 0.24)
        return VGroup(frame, body)

    def _clear(self):
        active = [mob for mob in list(self.mobjects) if mob is not self.author]
        if active:
            self.play(*[FadeOut(mob) for mob in active], run_time=0.4)

    def scene_opening(self):
        title = self._title("√8 + √18 等于多少？")
        problem = self._card(3.7, 1.85,
                             MathTex(r"\sqrt8+\sqrt{18}=\ ?", font_size=59,
                                     color=WHITE), self.CYAN)
        bad = self._card(1.1, 1.85,
                         MathTex(r"\sqrt8+\sqrt{18}\ne\sqrt{26}",
                                 font_size=47, color=self.CORAL), self.CORAL)
        answer = self._card(-1.5, 1.85,
                            MathTex(r"2\sqrt2+3\sqrt2=5\sqrt2",
                                    font_size=48, color=self.GREEN), self.GREEN)
        self.play(Write(title), FadeIn(problem), run_time=0.8)
        self.play(FadeIn(bad), run_time=0.6)
        self.play(FadeIn(answer), run_time=0.7)
        self.wait(1.0)
        self._clear()

    def scene_three_steps(self):
        title = self._title("根式加减：三步走")
        step1 = self._card(3.7, 1.8,
                           MathTex(r"\sqrt8=2\sqrt2,\ \sqrt{18}=3\sqrt2",
                                   font_size=42, color=self.CYAN), self.CYAN)
        step2 = self._card(1.1, 1.8,
                           self._note("分别化最简后，两个被开方数都是 2", 0,
                                      self.VIOLET), self.VIOLET)
        step3 = self._card(-1.5, 1.8,
                           MathTex(r"(2+3)\sqrt2=5\sqrt2", font_size=49,
                                   color=self.GREEN), self.GREEN)
        note = self._note("先化简 → 找同类 → 合并系数", -3.6, self.TITLE)
        self.play(Write(title), FadeIn(step1), run_time=0.8)
        self.play(FadeIn(step2), FadeIn(step3), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_ex1_direct(self):
        title = self._title("例题一：2√3 + 3√3")
        assert add_subtract_radicals(((2, 3), (3, 3))) == {3: 5}
        start = self._card(3.7, 1.8,
                           MathTex(r"2\sqrt3+3\sqrt3", font_size=56,
                                   color=WHITE), self.CYAN)
        result = self._card(1.1, 1.8,
                            MathTex(r"(2+3)\sqrt3=5\sqrt3",
                                    font_size=49, color=self.GREEN), self.GREEN)
        # 每个彩色方块代表 1 个 √3；五个方块与可见系数 2+3 一一对应。
        blocks = VGroup(*[
            RoundedRectangle(corner_radius=0.1, width=0.87, height=0.56,
                             fill_color=self.CYAN if index < 2 else self.GREEN,
                             fill_opacity=0.9, stroke_width=0)
            for index in range(5)
        ]).arrange(RIGHT, buff=0.14).move_to(DOWN * 1.8)
        note = self._note("两块加三块，得到五个同样的 √3 单元", -3.3)
        self.play(Write(title), FadeIn(start), run_time=0.8)
        self.play(FadeIn(result), run_time=0.5)
        self.play(FadeIn(blocks), FadeIn(note), run_time=0.7)
        self.wait(1.1)
        self._clear()

    def scene_ex2_main(self):
        title = self._title("例题二：√8 + √18")
        assert add_subtract_radicals(((1, 8), (1, 18))) == {2: 5}
        first = self._card(3.7, 1.8,
                           MathTex(r"\sqrt8+\sqrt{18}", font_size=56,
                                   color=WHITE), self.CYAN)
        second = self._card(1.1, 1.8,
                            MathTex(r"2\sqrt2+3\sqrt2", font_size=54,
                                    color=self.VIOLET), self.VIOLET)
        third = self._card(-1.5, 1.8,
                           MathTex(r"(2+3)\sqrt2=5\sqrt2", font_size=49,
                                   color=self.GREEN), self.GREEN)
        note = self._note("√8 与 √18 化简前不同，化简后同类", -3.5)
        self.play(Write(title), FadeIn(first), run_time=0.8)
        self.play(FadeIn(second), FadeIn(third), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.1)
        self._clear()

    def scene_ex3_subtract(self):
        title = self._title("例题三：√12 − √3")
        assert add_subtract_radicals(((1, 12), (-1, 3))) == {3: 1}
        first = self._card(3.7, 1.8,
                           MathTex(r"\sqrt{12}-\sqrt3", font_size=55,
                                   color=WHITE), self.CYAN)
        second = self._card(1.1, 1.8,
                            MathTex(r"2\sqrt3-1\sqrt3", font_size=50,
                                    color=self.VIOLET), self.VIOLET)
        third = self._card(-1.5, 1.8,
                           MathTex(r"(2-1)\sqrt3=\sqrt3", font_size=50,
                                   color=self.GREEN), self.GREEN)
        note = self._note("单独的 √3 系数是 1；减法不改变根号内的 3", -3.5)
        self.play(Write(title), FadeIn(first), run_time=0.8)
        self.play(FadeIn(second), FadeIn(third), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.1)
        self._clear()

    def scene_ex4_mixed(self):
        title = self._title("例题四：三项相加减")
        assert add_subtract_radicals(((1, 8), (1, 18), (-1, 2))) == {2: 4}
        first = self._card(3.7, 1.8,
                           MathTex(r"\sqrt8+\sqrt{18}-\sqrt2",
                                   font_size=52, color=WHITE), self.CYAN)
        second = self._card(1.1, 1.8,
                            MathTex(r"2\sqrt2+3\sqrt2-\sqrt2",
                                    font_size=47, color=self.VIOLET), self.VIOLET)
        third = self._card(-1.5, 1.8,
                           MathTex(r"(2+3-1)\sqrt2=4\sqrt2",
                                   font_size=46, color=self.GREEN), self.GREEN)
        note = self._note("合并时各项符号要原样带入：2 + 3 − 1 = 4", -3.5)
        self.play(Write(title), FadeIn(first), run_time=0.8)
        self.play(FadeIn(second), FadeIn(third), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.1)
        self._clear()

    def scene_cannot_merge(self):
        title = self._title("非同类根式不能按同类项合并")
        first = self._card(3.7, 1.8,
                           MathTex(r"\sqrt2+\sqrt3\ne\sqrt5",
                                   font_size=52, color=self.CORAL), self.CORAL)
        second = self._card(1.1, 1.8,
                            MathTex(r"(\sqrt2+\sqrt3)^2=5+2\sqrt6>5",
                                    font_size=40, color=self.TITLE), self.TITLE)
        third = self._card(-1.5, 1.8,
                           MathTex(r"\sqrt2+\sqrt3", font_size=60,
                                   color=self.GREEN), self.GREEN)
        note = self._note("先化最简；被开方数仍不同，就保留两项", -3.5)
        assert add_subtract_radicals(((1, 2), (1, 3))) == {2: 1, 3: 1}
        self.play(Write(title), FadeIn(first), run_time=0.8)
        self.play(FadeIn(second), FadeIn(third), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.1)
        self._clear()

    def scene_quick_practice(self):
        title = self._title("综合练习：先化简再算")
        questions = (
            (r"3\sqrt5+2\sqrt5=5\sqrt5", "直接合并", ((3, 5), (2, 5)), {5: 5}),
            (r"\sqrt{50}-\sqrt8=3\sqrt2", "先提取平方因数", ((1, 50), (-1, 8)), {2: 3}),
            (r"\sqrt{12}+\sqrt{27}=5\sqrt3", "最简后才同类", ((1, 12), (1, 27)), {3: 5}),
            (r"\sqrt3+\sqrt5", "非同类，保留两项", ((1, 3), (1, 5)), {3: 1, 5: 1}),
        )
        self.play(Write(title), run_time=0.5)
        for index, (formula, explanation, input_terms, expected) in enumerate(questions):
            assert add_subtract_radicals(input_terms) == expected
            content = VGroup(MathTex(formula, font_size=38, color=WHITE),
                             self._note(explanation, 0, self.GREEN)).arrange(DOWN, buff=0.18)
            card = self._card(4.5 - 1.85 * index, 1.55, content, self.GREEN)
            self.play(FadeIn(card), run_time=0.45)
        self.wait(1.1)
        self._clear()

    def scene_summary(self):
        title = self._title("总结：三步走，符号不丢")
        method = self._card(3.7, 1.8,
                            self._note("先化最简 → 找同类 → 加减根号外系数", 0,
                                       self.CYAN), self.CYAN)
        rule = self._card(1.1, 1.8,
                          MathTex(r"m\sqrt r\pm n\sqrt r=(m\pm n)\sqrt r",
                                  font_size=40, color=self.VIOLET), self.VIOLET)
        example = self._card(-1.5, 1.8,
                             MathTex(r"\sqrt8+\sqrt{18}-\sqrt2=4\sqrt2",
                                     font_size=43, color=self.GREEN), self.GREEN)
        note = self._note("非同类根式不能直接合并；负项系数要保留", -3.5)
        self.play(Write(title), FadeIn(method), run_time=0.8)
        self.play(FadeIn(rule), FadeIn(example), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_outro(self):
        title = self._title("根式加减，先化简再合并")
        formula = MathTex(r"\sqrt8+\sqrt{18}=5\sqrt2", font_size=52,
                          color=self.GREEN).move_to(UP * 2.6)
        note = self._note("算式可验证，画面结论才可靠", 0.8, self.TITLE)
        self.play(Write(title), Write(formula), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()
        self.play(FadeOut(self.author), run_time=0.35)
