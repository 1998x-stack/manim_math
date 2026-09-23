"""二次根式的乘除法：八年级第一学期，第十六章。

manim -pql radical_mul_div.py RadicalMultDiv
保留原有 11 段 Scene 方法、1080×1920 竖屏、作者水印。
"""

import math
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def root_product(a, b):
    """√a·√b=√(ab)，在实数范围内要求 a≥0,b≥0。"""
    if not math.isfinite(a) or not math.isfinite(b) or a < 0 or b < 0:
        raise ValueError("乘法的被开方数须非负且有限")
    return math.sqrt(a) * math.sqrt(b)


def root_quotient(a, b):
    """√a/√b=√(a/b)，在实数范围内要求 a≥0,b>0。"""
    if not math.isfinite(a) or not math.isfinite(b) or a < 0 or b <= 0:
        raise ValueError("分子非负且分母的被开方数须为正")
    return math.sqrt(a) / math.sqrt(b)


def rationalize(numerator, radicand):
    """n/√a = n√a/a；示例要求分母非零且 a>0。"""
    if not math.isfinite(numerator) or not math.isfinite(radicand) or radicand <= 0:
        raise ValueError("分母的被开方数须为有限正数")
    return numerator * math.sqrt(radicand) / radicand


class RadicalMultDiv(Scene):
    BG = "#1a1a2e"
    TITLE = "#f9ca24"
    CYAN = "#57cad3"
    VIOLET = "#b4a1fa"
    GREEN = "#8bdf9f"
    CORAL = "#f58989"
    MUTED = "#c0cad9"
    PANEL = "#16213e"

    def construct(self):
        self.camera.background_color = self.BG
        self.author = Text("上海初高中数学直通车 @emptyandcalm",
                           font="PingFang SC", font_size=18,
                           color=self.MUTED).move_to(UP * 6.6)
        self.add(self.author)
        self.scene_opening()
        self.scene_mul_formula()
        self.scene_mul_ex1()
        self.scene_mul_ex2()
        self.scene_div_formula()
        self.scene_div_ex1()
        self.scene_rationalize_intro()
        self.scene_rationalize_ex()
        self.scene_quick_practice()
        self.scene_summary()
        self.scene_outro()

    def _title(self, text):
        title = Text(text, font="PingFang SC", font_size=39,
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
        stroke = color or self.CYAN
        bg = RoundedRectangle(corner_radius=0.25, width=7.7,
                              height=height, stroke_color=stroke,
                              stroke_width=2, fill_color=self.PANEL,
                              fill_opacity=0.92).move_to(UP * y)
        body = content if isinstance(content, VGroup) else VGroup(content)
        body.move_to(bg.get_center())
        if body.width > 7.05:
            body.scale_to_fit_width(7.05)
        if body.height > height - 0.24:
            body.scale_to_fit_height(height - 0.24)
        return VGroup(bg, body)

    def _clear(self):
        active = [mob for mob in list(self.mobjects) if mob is not self.author]
        if active:
            self.play(*[FadeOut(mob) for mob in active], run_time=0.4)

    def scene_opening(self):
        title = self._title("根号能直接相乘、相除吗？")
        product = self._card(3.7, 1.9,
                             MathTex(r"\sqrt3\cdot\sqrt5=\sqrt{15}",
                                     font_size=49, color=self.CYAN), self.CYAN)
        quotient = self._card(1.0, 1.9,
                              MathTex(r"\sqrt{12}\div\sqrt3=2", font_size=49,
                                      color=self.VIOLET), self.VIOLET)
        note = self._note("必须先检查被开方数与分母的取值条件", -1.4,
                          self.TITLE)
        self.play(Write(title), FadeIn(product), run_time=0.8)
        self.play(FadeIn(quotient), FadeIn(note), run_time=0.8)
        self.wait(1.0)
        self._clear()

    def scene_mul_formula(self):
        title = self._title("乘法公式：根号内相乘")
        rule = self._card(3.7, 1.9,
                          MathTex(r"\sqrt a\cdot\sqrt b=\sqrt{ab}",
                                  font_size=50, color=self.CYAN), self.CYAN)
        guard = self._note("适用条件：a ≥ 0，b ≥ 0", 2.0, self.TITLE)
        example = self._card(0.0, 1.9,
                             MathTex(r"\sqrt3\cdot\sqrt5=\sqrt{15}",
                                     font_size=47, color=self.GREEN), self.GREEN)
        edge = self._card(-2.6, 1.5,
                          MathTex(r"\sqrt0\cdot\sqrt5=0", font_size=48,
                                  color=self.VIOLET), self.VIOLET)
        self.play(Write(title), FadeIn(rule), run_time=0.8)
        self.play(FadeIn(guard), FadeIn(example), run_time=0.7)
        self.play(FadeIn(edge), run_time=0.5)
        self.wait(1.0)
        self._clear()

    def scene_mul_ex1(self):
        title = self._title("例题一：√3 × √5")
        assert math.isclose(root_product(3, 5), math.sqrt(15))
        source = self._card(3.7, 1.8,
                            MathTex(r"\sqrt3\cdot\sqrt5", font_size=56,
                                    color=WHITE), self.CYAN)
        middle = self._card(1.15, 1.8,
                            MathTex(r"\sqrt{3\cdot5}", font_size=56,
                                    color=self.TITLE), self.TITLE)
        result = self._card(-1.4, 1.8,
                            MathTex(r"\sqrt{15}", font_size=62,
                                    color=self.GREEN), self.GREEN)
        note = self._note("15 没有大于 1 的平方因数，结果已是最简", -3.5)
        self.play(Write(title), FadeIn(source), run_time=0.8)
        self.play(FadeIn(middle), FadeIn(result), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_mul_ex2(self):
        title = self._title("例题二：乘完记得化简")
        problem = self._card(3.7, 1.8,
                             MathTex(r"\sqrt2\cdot\sqrt8=\sqrt{16}=4",
                                     font_size=48, color=self.GREEN), self.GREEN)
        hint = self._note("用长方形理解：长 × 宽 = 面积", 2.25, self.CYAN)
        # √8/√2=2，示意矩形宽高比精确为 2:1；长度的单位缩放一致。
        rectangle = Rectangle(width=3.8, height=1.9, color=self.CYAN,
                              fill_color=self.CYAN, fill_opacity=0.16,
                              stroke_width=3).move_to(DOWN * 0.1)
        width_label = MathTex(r"\sqrt8", font_size=31,
                              color=self.TITLE).next_to(rectangle, DOWN, buff=0.14)
        height_label = MathTex(r"\sqrt2", font_size=31,
                               color=self.TITLE).next_to(rectangle, LEFT, buff=0.15)
        area_label = self._note("面积 = 4", -0.1, self.GREEN)
        after = self._card(-3.05, 1.6,
                           MathTex(r"\sqrt2\cdot2\sqrt2=4", font_size=49,
                                   color=self.GREEN), self.GREEN)
        assert math.isclose(root_product(2, 8), 4)
        assert math.isclose(3.8 / 1.9, math.sqrt(8) / math.sqrt(2))
        self.play(Write(title), FadeIn(problem), FadeIn(hint), run_time=0.8)
        self.play(Create(rectangle), FadeIn(width_label), FadeIn(height_label),
                  FadeIn(area_label), run_time=0.8)
        self.play(FadeIn(after), run_time=0.5)
        self.wait(1.0)
        self._clear()

    def scene_div_formula(self):
        title = self._title("除法公式：分母不能为零")
        rule = self._card(3.7, 1.9,
                          MathTex(r"\frac{\sqrt a}{\sqrt b}=\sqrt{\frac ab}",
                                  font_size=49, color=self.VIOLET), self.VIOLET)
        guard = self._note("适用条件：a ≥ 0，b > 0", 2.0, self.TITLE)
        example = self._card(0.0, 1.9,
                             MathTex(r"\frac{\sqrt{12}}{\sqrt3}=\sqrt4=2",
                                     font_size=45, color=self.GREEN), self.GREEN)
        warning = self._note("b = 0 时分母为 0，运算无意义", -2.7, self.CORAL)
        self.play(Write(title), FadeIn(rule), run_time=0.8)
        self.play(FadeIn(guard), FadeIn(example), run_time=0.7)
        self.play(FadeIn(warning), run_time=0.5)
        self.wait(1.0)
        self._clear()

    def scene_div_ex1(self):
        title = self._title("例题三：√12 ÷ √3")
        assert math.isclose(root_quotient(12, 3), 2)
        source = self._card(3.7, 1.8,
                            MathTex(r"\frac{\sqrt{12}}{\sqrt3}",
                                    font_size=55, color=WHITE), self.VIOLET)
        middle = self._card(1.15, 1.8,
                            MathTex(r"\sqrt{\frac{12}{3}}=\sqrt4",
                                    font_size=51, color=self.TITLE), self.TITLE)
        result = self._card(-1.4, 1.8,
                            MathTex(r"=2", font_size=62,
                                    color=self.GREEN), self.GREEN)
        note = self._note("先开方后作商，或先作商再开方，结果相同", -3.5)
        self.play(Write(title), FadeIn(source), run_time=0.8)
        self.play(FadeIn(middle), FadeIn(result), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_rationalize_intro(self):
        title = self._title("分母有理化：乘以 1，不改变数值")
        source = self._card(3.7, 1.85,
                            MathTex(r"\frac1{\sqrt3}", font_size=60,
                                    color=self.CORAL), self.CORAL)
        fraction_one = self._card(1.15, 1.85,
                                  MathTex(r"\frac{\sqrt3}{\sqrt3}=1",
                                          font_size=52, color=self.TITLE), self.TITLE)
        result = self._card(-1.4, 1.85,
                            MathTex(r"\frac1{\sqrt3}=\frac{\sqrt3}{3}",
                                    font_size=47, color=self.GREEN), self.GREEN)
        note = self._note("通用式：a > 0 时，1/√a = √a/a", -3.55)
        assert math.isclose(rationalize(1, 3), 1 / math.sqrt(3))
        self.play(Write(title), FadeIn(source), run_time=0.8)
        self.play(FadeIn(fraction_one), FadeIn(result), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_rationalize_ex(self):
        title = self._title("例题四：把 6/√3 化到最简")
        source = self._card(3.7, 1.9,
                            MathTex(r"\frac6{\sqrt3}", font_size=58,
                                    color=WHITE), self.CYAN)
        middle = self._card(1.1, 1.9,
                            MathTex(r"\frac{6\sqrt3}{\sqrt3\cdot\sqrt3}",
                                    font_size=50, color=self.TITLE), self.TITLE)
        answer = self._card(-1.5, 1.9,
                            MathTex(r"\frac{6\sqrt3}3=2\sqrt3", font_size=52,
                                    color=self.GREEN), self.GREEN)
        note = self._note("每一步都分子、分母同乘 √3，不能只乘分母", -3.5)
        assert math.isclose(rationalize(6, 3), 2 * math.sqrt(3))
        self.play(Write(title), FadeIn(source), run_time=0.8)
        self.play(FadeIn(middle), FadeIn(answer), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()

    def scene_quick_practice(self):
        title = self._title("快速练习：判断值和定义域")
        examples = (
            (r"\sqrt2\cdot\sqrt8=4", "乘法：正确", True),
            (r"\frac{\sqrt{12}}{\sqrt3}=2", "除法：正确", True),
            (r"\frac1{\sqrt3}=\frac{\sqrt3}3", "有理化：正确", True),
            (r"\frac{\sqrt5}{\sqrt0}", "分母为 0：无意义", False),
        )
        assert math.isclose(root_product(2, 8), 4)
        assert math.isclose(root_quotient(12, 3), 2)
        assert math.isclose(rationalize(1, 3), math.sqrt(3) / 3)
        self.play(Write(title), run_time=0.5)
        for index, (tex, label, valid) in enumerate(examples):
            formula = MathTex(tex, font_size=40, color=WHITE)
            explanation = self._note(label, 0, self.GREEN if valid else self.CORAL)
            content = VGroup(formula, explanation).arrange(DOWN, buff=0.16)
            card = self._card(4.5 - 1.85 * index, 1.55, content,
                              self.GREEN if valid else self.CORAL)
            self.play(FadeIn(card), run_time=0.45)
        self.wait(1.0)
        self._clear()

    def scene_summary(self):
        title = self._title("总结：先判断条件，再使用公式")
        product = self._card(3.75, 1.9,
                             MathTex(r"\sqrt a\cdot\sqrt b=\sqrt{ab}",
                                     font_size=49, color=self.CYAN), self.CYAN)
        product_domain = self._note("乘法：a ≥ 0，b ≥ 0", 2.25)
        quotient = self._card(0.6, 1.9,
                              MathTex(r"\frac{\sqrt a}{\sqrt b}=\sqrt{\frac ab}",
                                      font_size=45, color=self.VIOLET), self.VIOLET)
        quotient_domain = self._note("除法：a ≥ 0，b > 0", -0.85)
        rationalization = self._card(-2.75, 1.65,
                                     MathTex(r"\frac1{\sqrt a}=\frac{\sqrt a}a\quad(a>0)",
                                             font_size=43, color=self.GREEN),
                                     self.GREEN)
        self.play(Write(title), FadeIn(product), FadeIn(product_domain),
                  run_time=0.8)
        self.play(FadeIn(quotient), FadeIn(quotient_domain), run_time=0.8)
        self.play(FadeIn(rationalization), run_time=0.5)
        self.wait(1.2)
        self._clear()

    def scene_outro(self):
        title = self._title("乘除法的核心：条件与化简")
        result = MathTex(r"\frac6{\sqrt3}=2\sqrt3", font_size=52,
                         color=self.GREEN).move_to(UP * 2.7)
        note = self._note("分母不能为零；最终结果注意化到最简", 0.8,
                          self.TITLE)
        self.play(Write(title), Write(result), run_time=0.8)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)
        self._clear()
        self.play(FadeOut(self.author), run_time=0.35)
