"""最简二次根式：八年级第一学期，第十六章。

运行：manim -pql simplest_radical.py SimplestRadical
保留原有九段分镜、9:16 比例、水印与 Scene 类名。
"""

import math
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def simplify_integer_radicand(value):
    """非负整数 n 的 √n = outside × √inside，inside 不含平方因数。"""
    if type(value) is not int or value < 0:
        raise ValueError("被开方数必须为非负整数")
    if value == 0:
        return 0, 1
    outside, inside, divisor = 1, value, 2
    while divisor * divisor <= inside:
        square = divisor * divisor
        while inside % square == 0:
            outside *= divisor
            inside //= square
        divisor += 1
    return outside, inside


def square_factor_root(a, b):
    """√(a²b)=|a|√b；实数 a、b 且 b≥0。"""
    if not math.isfinite(a) or not math.isfinite(b) or b < 0:
        raise ValueError("要求有限实数且 b≥0")
    return abs(a) * math.sqrt(b)


def quotient_root(a, b):
    """√(a/b)=√a/√b 的实数域条件为 a≥0 且 b>0。"""
    if not math.isfinite(a) or not math.isfinite(b) or a < 0 or b <= 0:
        raise ValueError("要求 a≥0 且 b>0")
    return math.sqrt(a / b)


class SimplestRadical(Scene):
    BG = "#1a1a2e"
    TITLE = "#f9ca24"
    GREEN = "#91dc87"
    CYAN = "#57ced4"
    CORAL = "#fa8684"
    MUTED = "#bac4d4"
    PANEL = "#16213e"

    def construct(self):
        self.camera.background_color = self.BG
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font="PingFang SC", font_size=18,
                           color=self.MUTED).move_to(UP * 6.6)
        self.add(self.author)
        self.scene_opening()
        self.scene_two_conditions()
        self.scene_method()
        self.scene_example1()
        self.scene_example2()
        self.scene_example3()
        self.scene_judge()
        self.scene_summary()
        self.scene_outro()

    def _title(self, text):
        title = Text(text, font="PingFang SC", font_size=39,
                     color=self.TITLE).move_to(UP * 5.75)
        if title.width > 7.8:
            title.scale_to_fit_width(7.8)
        return title

    def _card(self, y, height, content, color=None):
        border = color or self.CYAN
        frame = RoundedRectangle(
            corner_radius=0.25, width=7.7, height=height,
            fill_color=self.PANEL, fill_opacity=0.92,
            stroke_color=border, stroke_width=2,
        ).move_to(UP * y)
        body = content if isinstance(content, VGroup) else VGroup(content)
        body.move_to(frame.get_center())
        if body.width > 7.05:
            body.scale_to_fit_width(7.05)
        if body.height > height - 0.24:
            body.scale_to_fit_height(height - 0.24)
        return VGroup(frame, body)

    def _note(self, text, y, color=None):
        note = Text(text, font="PingFang SC", font_size=26,
                    color=color or self.MUTED).move_to(UP * y)
        if note.width > 7.6:
            note.scale_to_fit_width(7.6)
        return note

    def _clear(self):
        # 严格使用画面上同一对象；一轮 play 不为同一对象生成多份 FadeOut。
        visible = [mob for mob in list(self.mobjects) if mob is not self.author]
        if visible:
            self.play(*[FadeOut(mob) for mob in visible], run_time=0.4)

    def scene_opening(self):
        title = self._title("√12 和 2√3，哪一个最简？")
        left = self._card(3.6, 2.0,
                          MathTex(r"\sqrt{12}", font_size=65, color=self.CORAL),
                          self.CORAL)
        right = self._card(1.0, 2.0,
                           MathTex(r"2\sqrt3", font_size=65, color=self.GREEN),
                           self.GREEN)
        equality = MathTex(r"\sqrt{12}=2\sqrt3", font_size=52,
                           color=self.TITLE).move_to(DOWN * 1.6)
        explain = self._note("数值相等，但右边根号内已无完全平方因数", -3.0)
        self.play(Write(title), FadeIn(left), run_time=0.8)
        self.play(FadeIn(right), Write(equality), run_time=0.8)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.0)
        self._clear()

    def scene_two_conditions(self):
        title = self._title("最简二次根式的两个条件")
        first = self._card(
            3.7, 2.1,
            VGroup(self._note("① 被开方数不含分母", 0, self.CYAN),
                   MathTex(r"\sqrt{\frac34}=\frac{\sqrt3}{2}",
                           font_size=45, color=self.CYAN)).arrange(DOWN, buff=0.3),
            self.CYAN,
        )
        second = self._card(
            1.0, 2.1,
            VGroup(self._note("② 被开方数无可完全开方的因数或因式", 0, self.GREEN),
                   MathTex(r"\sqrt{12}=\sqrt{4\cdot3}=2\sqrt3",
                           font_size=43, color=self.GREEN)).arrange(DOWN, buff=0.3),
            self.GREEN,
        )
        note = self._note("有根号不等于已经化成最简形式", -1.5, self.TITLE)
        self.play(Write(title), FadeIn(first), run_time=0.8)
        self.play(FadeIn(second), FadeIn(note), run_time=0.8)
        self.wait(1.0)
        self._clear()

    def scene_method(self):
        title = self._title("提取完全平方因数")
        stage1 = self._card(3.7, 1.5,
                            MathTex(r"12=4\times3=2^2\times3",
                                    font_size=45, color=WHITE), self.CYAN)
        stage2 = self._card(1.3, 1.5,
                            MathTex(r"\sqrt{12}=\sqrt{2^2\times3}",
                                    font_size=44, color=self.TITLE), self.TITLE)
        stage3 = self._card(-1.1, 1.5,
                            MathTex(r"\sqrt{2^2\times3}=2\sqrt3",
                                    font_size=44, color=self.GREEN), self.GREEN)
        note = self._note("2² 从根号内移出时开方，根号内剩下 3", -3.4)
        self.play(Write(title), FadeIn(stage1), run_time=0.8)
        self.play(FadeIn(stage2), run_time=0.5)
        self.play(FadeIn(stage3), FadeIn(note), run_time=0.7)
        self.wait(1.1)
        self._clear()

    def scene_example1(self):
        title = self._title("例题一：化简 √12")
        outside, inside = simplify_integer_radicand(12)
        assert (outside, inside) == (2, 3)
        source = self._card(3.6, 1.7,
                            MathTex(r"\sqrt{12}", font_size=58, color=WHITE),
                            self.CYAN)
        factor = self._card(1.1, 1.7,
                            MathTex(r"\sqrt{4\times3}=\sqrt{2^2\times3}",
                                    font_size=44, color=self.TITLE), self.TITLE)
        answer = self._card(-1.4, 1.7,
                            MathTex(r"\sqrt{12}=2\sqrt3", font_size=51,
                                    color=self.GREEN), self.GREEN)
        note = self._note("结果仍含根号，但根号内的 3 已无法再开尽", -3.5)
        self.play(Write(title), FadeIn(source), run_time=0.8)
        self.play(FadeIn(factor), FadeIn(answer), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.1)
        self._clear()

    def scene_example2(self):
        title = self._title("例题二：含字母时先看正负")
        general = self._card(3.7, 1.8,
                             MathTex(r"\sqrt{a^2b}=|a|\sqrt b\quad(b\geq0)",
                                     font_size=42, color=self.TITLE), self.TITLE)
        positive = self._card(1.15, 1.8,
                              MathTex(r"a\geq0:\quad\sqrt{a^2b}=a\sqrt b",
                                      font_size=40, color=self.GREEN), self.GREEN)
        negative = self._card(-1.4, 1.8,
                              MathTex(r"a<0:\quad\sqrt{a^2b}=-a\sqrt b",
                                      font_size=40, color=self.CORAL), self.CORAL)
        example = self._note("例：a=-2，b=3 时，结果为 2√3，不是 -2√3", -3.4)
        assert math.isclose(square_factor_root(-2, 3), 2 * math.sqrt(3))
        self.play(Write(title), FadeIn(general), run_time=0.8)
        self.play(FadeIn(positive), FadeIn(negative), run_time=0.8)
        self.play(FadeIn(example), run_time=0.4)
        self.wait(1.1)
        self._clear()

    def scene_example3(self):
        title = self._title("例题三：根号内不能含分母")
        rule = self._card(3.65, 1.85,
                          MathTex(r"\sqrt{\frac ab}=\frac{\sqrt a}{\sqrt b}",
                                  font_size=48, color=self.CYAN), self.CYAN)
        domain = self._note("适用条件：a ≥ 0，b > 0", 2.1, self.TITLE)
        stages = self._card(
            0.1, 2.1,
            VGroup(MathTex(r"\sqrt{\frac34}=\frac{\sqrt3}{\sqrt4}",
                           font_size=43, color=WHITE),
                   MathTex(r"=\frac{\sqrt3}{2}", font_size=43,
                           color=self.GREEN)).arrange(DOWN, buff=0.27),
            self.GREEN,
        )
        warning = self._note("分母已是整数 2；若仍含根号，还需分母有理化", -2.4)
        assert math.isclose(quotient_root(3, 4), math.sqrt(3) / 2)
        self.play(Write(title), FadeIn(rule), run_time=0.8)
        self.play(FadeIn(domain), FadeIn(stages), run_time=0.8)
        self.play(FadeIn(warning), run_time=0.4)
        self.wait(1.1)
        self._clear()

    def scene_judge(self):
        title = self._title("判断：哪些式子已经最简？")
        checks = (
            (r"\sqrt3", "是：3 无平方因数", True),
            (r"\sqrt8", "否：√8 = 2√2", False),
            (r"\sqrt{\frac23}", "否：根号内含分母", False),
            (r"3\sqrt5", "是：5 无平方因数", True),
            (r"\sqrt{a^2}", "否：应化为 |a|", False),
        )
        self.play(Write(title), run_time=0.5)
        for i, (latex, reason, valid) in enumerate(checks):
            # 字母二次方的算术平方根必须取绝对值，不能默认为 a≥0。
            if i == 1:
                assert simplify_integer_radicand(8) == (2, 2)
            if i == 4:
                assert square_factor_root(-3, 1) == 3
            text = self._note(reason, 0, self.GREEN if valid else self.CORAL)
            formula = MathTex(latex, font_size=36, color=WHITE)
            content = VGroup(formula, text).arrange(RIGHT, buff=0.30)
            card = self._card(4.6 - i * 1.8, 1.45, content,
                              self.GREEN if valid else self.CORAL)
            self.play(FadeIn(card), run_time=0.45)
        self.wait(1.2)
        self._clear()

    def scene_summary(self):
        title = self._title("总结：先看定义域，再化简")
        first = self._card(
            3.7, 1.75,
            MathTex(r"\sqrt{12}=2\sqrt3", font_size=49,
                    color=self.GREEN), self.GREEN,
        )
        second = self._card(
            1.2, 1.75,
            MathTex(r"\sqrt{a^2b}=|a|\sqrt b\quad(b\geq0)",
                    font_size=41, color=self.TITLE), self.TITLE,
        )
        third = self._card(
            -1.3, 1.75,
            MathTex(r"\sqrt{\frac34}=\frac{\sqrt3}{2}",
                    font_size=47, color=self.CYAN), self.CYAN,
        )
        conditions = self._note("除去分母、提出平方因数；负数字母须保留绝对值", -3.6)
        self.play(Write(title), FadeIn(first), run_time=0.8)
        self.play(FadeIn(second), FadeIn(third), run_time=0.8)
        self.play(FadeIn(conditions), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_outro(self):
        title = self._title("最简二次根式：知识点回顾")
        formula = MathTex(r"\sqrt{12}=2\sqrt3", font_size=55,
                          color=self.GREEN).move_to(UP * 2.4)
        reminder = self._note("保持符号条件，化简结果才正确", 0.8, self.TITLE)
        self.play(Write(title), Write(formula), run_time=0.8)
        self.play(FadeIn(reminder), run_time=0.4)
        self.wait(1.0)
        self._clear()
        self.play(FadeOut(self.author), run_time=0.35)
