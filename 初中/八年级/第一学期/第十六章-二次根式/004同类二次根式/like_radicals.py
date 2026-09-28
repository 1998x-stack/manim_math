"""同类二次根式：八年级第一学期，第十六章。

manim -pql like_radicals.py LikeRadicals
保留原十段教学顺序、Scene 入口、9:16 画幅与作者水印。
"""

import math
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def normalized_term(coefficient, radicand):
    """整数系数 × √(非负整数) → (根号外系数, 无平方因数的被开方数)。"""
    if type(coefficient) is not int or type(radicand) is not int or radicand < 0:
        raise ValueError("本课示例要求整数系数和非负整数被开方数")
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


def collect_like_terms(terms):
    """必须先约为最简根式，再按被开方数合并；只返回非零项。"""
    groups = {}
    for coefficient, radicand in terms:
        outside, inside = normalized_term(coefficient, radicand)
        if outside:
            groups[inside] = groups.get(inside, 0) + outside
    return {inside: coeff for inside, coeff in sorted(groups.items()) if coeff}


class LikeRadicals(Scene):
    BG = "#1a1a2e"
    TITLE = "#f9ca24"
    CYAN = "#57c8d2"
    GREEN = "#89dc9c"
    CORAL = "#f18a8a"
    MUTED = "#bfcbda"
    PANEL = "#16213e"

    def construct(self):
        self.camera.background_color = self.BG
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font="PingFang SC", font_size=18,
                           color=self.MUTED).move_to(UP * 6.6)
        self.add(self.author)
        self.scene_opening()
        self.scene_definition()
        self.scene_check_method()
        self.scene_merge_rule()
        self.scene_example_basic()
        self.scene_example_advanced()
        self.scene_counter_example()
        self.scene_quick_judge()
        self.scene_summary()
        self.scene_outro()

    def _title(self, text):
        title = Text(text, font="PingFang SC", font_size=38,
                     color=self.TITLE).move_to(UP * 5.8)
        if title.width > 7.8:
            title.scale_to_fit_width(7.8)
        return title

    def _note(self, text, y, color=None):
        note = Text(text, font="PingFang SC", font_size=26,
                    color=color or self.MUTED).move_to(UP * y)
        if note.width > 7.6:
            note.scale_to_fit_width(7.6)
        return note

    def _card(self, y, height, content, color=None):
        border = color or self.CYAN
        bg = RoundedRectangle(corner_radius=0.25, width=7.7,
                              height=height, stroke_color=border,
                              stroke_width=2, fill_color=self.PANEL,
                              fill_opacity=0.92).move_to(UP * y)
        body = content if isinstance(content, VGroup) else VGroup(content)
        body.move_to(bg.get_center())
        if body.width > 7.05:
            body.scale_to_fit_width(7.05)
        if body.height > height - 0.22:
            body.scale_to_fit_height(height - 0.22)
        return VGroup(bg, body)

    def _clear(self):
        active = [mob for mob in list(self.mobjects) if mob is not self.author]
        if active:
            self.play(*[FadeOut(mob) for mob in active], run_time=0.4)

    def scene_opening(self):
        title = self._title("下面哪一组可以合并？")
        left = self._card(3.75, 1.9,
                          MathTex(r"2\sqrt3+5\sqrt3", font_size=47,
                                  color=self.GREEN), self.GREEN)
        right = self._card(1.2, 1.9,
                           MathTex(r"\sqrt2+\sqrt3", font_size=47,
                                   color=self.CORAL), self.CORAL)
        answer = self._note("先化成最简根式，再比较根号内的数", -1.0, self.TITLE)
        verdict = MathTex(r"2\sqrt3+5\sqrt3=7\sqrt3", font_size=48,
                          color=self.GREEN).move_to(DOWN * 2.4)
        self.play(Write(title), FadeIn(left), run_time=0.8)
        self.play(FadeIn(right), run_time=0.6)
        self.play(FadeIn(answer), Write(verdict), run_time=0.7)
        self.wait(1.0)
        self._clear()

    def scene_definition(self):
        title = self._title("什么叫同类二次根式？")
        definition = self._card(
            3.7, 2.0,
            self._note("各自化到最简后，被开方数相同的根式属于同类", 0,
                       self.CYAN), self.CYAN,
        )
        same = self._card(
            1.15, 1.7,
            MathTex(r"\sqrt{12}=2\sqrt3,\quad\sqrt3", font_size=43,
                    color=self.GREEN), self.GREEN,
        )
        different = self._card(
            -1.4, 1.7,
            MathTex(r"\sqrt2,\quad\sqrt3", font_size=48,
                    color=self.CORAL), self.CORAL,
        )
        note = self._note("系数可以不同，关键是最简形式的被开方数", -3.4)
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        self.play(FadeIn(same), FadeIn(different), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_check_method(self):
        title = self._title("判断前，先分别化简")
        step1 = self._card(3.75, 1.7,
                           MathTex(r"\sqrt{12}=2\sqrt3", font_size=51,
                                   color=self.CYAN), self.CYAN)
        step2 = self._card(1.25, 1.7,
                           MathTex(r"\sqrt3=1\sqrt3", font_size=51,
                                   color=self.GREEN), self.GREEN)
        step3 = self._card(-1.25, 1.7,
                           MathTex(r"2\sqrt3+\sqrt3=3\sqrt3",
                                   font_size=48, color=self.TITLE), self.TITLE)
        assert collect_like_terms(((1, 12), (1, 3))) == {3: 3}
        note = self._note("原式根号内的 12 与 3 不同，化简后却同类", -3.4)
        self.play(Write(title), FadeIn(step1), run_time=0.7)
        self.play(FadeIn(step2), FadeIn(step3), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_merge_rule(self):
        title = self._title("合并：只加减根号外的系数")
        rule = self._card(
            3.6, 2.0,
            MathTex(r"m\sqrt r+n\sqrt r=(m+n)\sqrt r",
                    font_size=42, color=self.CYAN), self.CYAN,
        )
        condition = self._note("适用于同一被开方数 r ≥ 0 的根式", 2.1)
        example = self._card(
            -0.1, 1.95,
            MathTex(r"(2+5)\sqrt3=7\sqrt3", font_size=50,
                    color=self.GREEN), self.GREEN,
        )
        warning = self._note("若根号内不同，应先化简；仍不同则不按此法则合并", -2.3,
                             self.TITLE)
        self.play(Write(title), FadeIn(rule), run_time=0.7)
        self.play(FadeIn(condition), FadeIn(example), run_time=0.7)
        self.play(FadeIn(warning), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_example_basic(self):
        title = self._title("例题一：2√3 + 5√3")
        first = self._card(3.7, 1.8,
                           MathTex(r"2\sqrt3+5\sqrt3", font_size=50,
                                   color=WHITE), self.CYAN)
        step = self._card(1.15, 1.8,
                          MathTex(r"(2+5)\sqrt3", font_size=53,
                                  color=self.TITLE), self.TITLE)
        last = self._card(-1.4, 1.8,
                          MathTex(r"7\sqrt3", font_size=59,
                                  color=self.GREEN), self.GREEN)
        # 两组同类根式的系数 2 和 5，用同样宽度的小单元表示。
        tiles = VGroup(*[
            RoundedRectangle(corner_radius=0.08, width=0.75, height=0.38,
                             fill_color=self.CYAN if i < 2 else self.GREEN,
                             fill_opacity=0.9, stroke_width=0)
            for i in range(7)
        ]).arrange(RIGHT, buff=0.12).move_to(DOWN * 3.3)
        assert collect_like_terms(((2, 3), (5, 3))) == {3: 7}
        self.play(Write(title), FadeIn(first), run_time=0.7)
        self.play(FadeIn(step), FadeIn(last), run_time=0.7)
        self.play(FadeIn(tiles), run_time=0.5)
        self.wait(1.0)
        self._clear()

    def scene_example_advanced(self):
        title = self._title("例题二：先化简再合并")
        first = self._card(3.7, 1.8,
                           MathTex(r"\sqrt{12}+\sqrt3", font_size=54,
                                   color=WHITE), self.CYAN)
        second = self._card(1.15, 1.8,
                            MathTex(r"2\sqrt3+\sqrt3", font_size=54,
                                    color=self.TITLE), self.TITLE)
        third = self._card(-1.4, 1.8,
                           MathTex(r"(2+1)\sqrt3=3\sqrt3", font_size=48,
                                   color=self.GREEN), self.GREEN)
        assert collect_like_terms(((1, 12), (1, 3))) == {3: 3}
        note = self._note("可合并的依据：两项化成最简后都是 √3", -3.4)
        self.play(Write(title), FadeIn(first), run_time=0.7)
        self.play(FadeIn(second), FadeIn(third), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_counter_example(self):
        title = self._title("反例：不能直接相加被开方数")
        wrong = self._card(3.7, 1.8,
                           MathTex(r"\sqrt2+\sqrt3\ne\sqrt5", font_size=52,
                                   color=self.CORAL), self.CORAL)
        proof = self._card(
            1.0, 2.0,
            MathTex(r"(\sqrt2+\sqrt3)^2=5+2\sqrt6>5",
                    font_size=42, color=self.TITLE), self.TITLE,
        )
        outcome = self._card(-1.7, 1.7,
                             MathTex(r"\sqrt2+\sqrt3", font_size=54,
                                     color=self.GREEN), self.GREEN)
        note = self._note("两项最简后被开方数不同，不能按同类项法则合并", -3.5)
        assert collect_like_terms(((1, 2), (1, 3))) == {2: 1, 3: 1}
        self.play(Write(title), FadeIn(wrong), run_time=0.8)
        self.play(FadeIn(proof), FadeIn(outcome), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_quick_judge(self):
        title = self._title("四题判断：化简后是否同类？")
        rows = (
            (r"3\sqrt5+2\sqrt5=5\sqrt5", True),
            (r"\sqrt8+\sqrt2=3\sqrt2", True),
            (r"\sqrt3-\sqrt7", False),
            (r"4\sqrt6-\sqrt6=3\sqrt6", True),
        )
        checks = (
            collect_like_terms(((3, 5), (2, 5))) == {5: 5},
            collect_like_terms(((1, 8), (1, 2))) == {2: 3},
            len(collect_like_terms(((1, 3), (-1, 7)))) > 1,
            collect_like_terms(((4, 6), (-1, 6))) == {6: 3},
        )
        assert all(checks)
        self.play(Write(title), run_time=0.5)
        for index, (formula, valid) in enumerate(rows):
            status = self._note("同类，可以合并" if valid else "非同类，保留两项",
                                0, self.GREEN if valid else self.CORAL)
            latex = MathTex(formula, font_size=40, color=WHITE)
            content = VGroup(latex, status).arrange(DOWN, buff=0.17)
            card = self._card(4.5 - 1.85 * index, 1.55, content,
                              self.GREEN if valid else self.CORAL)
            self.play(FadeIn(card), run_time=0.45)
        self.wait(1.0)
        self._clear()

    def scene_summary(self):
        title = self._title("总结：同类必须先化到最简")
        rule = self._card(
            3.75, 1.85,
            self._note("最简二次根式的被开方数相同，才是同类", 0,
                       self.CYAN), self.CYAN,
        )
        basic = self._card(1.1, 1.8,
                           MathTex(r"2\sqrt3+5\sqrt3=7\sqrt3",
                                   font_size=45, color=self.GREEN), self.GREEN)
        advanced = self._card(-1.5, 1.8,
                              MathTex(r"\sqrt{12}+\sqrt3=3\sqrt3",
                                      font_size=45, color=self.TITLE), self.TITLE)
        note = self._note("√2 与 √3 已最简但不同类，不能直接合并", -3.5)
        self.play(Write(title), FadeIn(rule), run_time=0.7)
        self.play(FadeIn(basic), FadeIn(advanced), run_time=0.7)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_outro(self):
        title = self._title("先化简 → 再比较 → 才合并")
        formula = MathTex(r"\sqrt{12}+\sqrt3=3\sqrt3", font_size=51,
                          color=self.GREEN).move_to(UP * 2.7)
        note = self._note("记住：被开方数不同不等于不能先化简", 0.8, self.TITLE)
        self.play(Write(title), Write(formula), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()
        self.play(FadeOut(self.author), run_time=0.35)
