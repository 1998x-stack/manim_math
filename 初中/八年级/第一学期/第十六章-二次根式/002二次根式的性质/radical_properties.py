"""二次根式的性质：八年级第一学期，第十六章。

manim -pql radical_properties.py QuadraticRadicalProperties
保留原 Scene 入口、七段教学顺序与 9:16 画幅。旧视频不由此脚本覆盖。
"""

import math
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def root_then_square(value):
    """(√a)² 仅在实数域 a >= 0 时定义；供独立数学测试调用。"""
    if not math.isfinite(value) or value < 0:
        raise ValueError("被开方数须为有限的非负实数")
    return math.sqrt(value) ** 2


def square_then_root(value):
    """√(a²) = |a|，对任意有限实数均成立。"""
    if not math.isfinite(value):
        raise ValueError("示例输入须为有限实数")
    return abs(value)


class QuadraticRadicalProperties(Scene):
    BG = "#1a1a2e"
    CYAN = "#00ced1"
    CORAL = "#ff827a"
    GREEN = "#4cd6a0"
    GOLD = "#ffd166"
    MUTED = "#b4bfd2"
    PANEL = "#16213e"

    def construct(self):
        self.camera.background_color = self.BG
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC", font_size=18, color=self.MUTED,
        ).move_to(UP * 6.65)
        self.add(self.author_info)
        self.scene_1_hook()
        self.scene_2_review()
        self.scene_3_prop1()
        self.scene_4_prop2_trap()
        self.scene_5_prop2_full()
        self.scene_6_pitfall()
        self.scene_7_summary()

    def _title(self, text, color=None):
        title = Text(text, font="PingFang SC", font_size=38,
                     color=color or self.GOLD).move_to(UP * 5.8)
        if title.width > 7.8:
            title.scale_to_fit_width(7.8)
        return title

    def _panel(self, center_y, height, *objects, border=None):
        bg = RoundedRectangle(
            corner_radius=0.25, width=7.7, height=height,
            fill_color=self.PANEL, fill_opacity=0.94,
            stroke_color=border or self.MUTED, stroke_width=2,
        ).move_to(UP * center_y)
        content = VGroup(*objects)
        content.move_to(bg.get_center())
        if content.width > 7.1:
            content.scale_to_fit_width(7.1)
        if content.height > height - 0.25:
            content.scale_to_fit_height(height - 0.25)
        return VGroup(bg, content)

    def _clear(self):
        # 只淡出实际在画面中的顶层对象，且每个对象只生成一个动画。
        active = [mob for mob in list(self.mobjects) if mob is not self.author_info]
        if active:
            self.play(*[FadeOut(mob) for mob in active], run_time=0.4)

    def scene_1_hook(self):
        title = self._title("先平方再开方，会得到原数吗？")
        question = MathTex(r"\sqrt{(-3)^2}=\ ?", font_size=65,
                           color=self.GOLD).move_to(UP * 3.6)
        guess = Text("先独立想一想：答案是 -3 还是 3？",
                     font="PingFang SC", font_size=27,
                     color=self.MUTED).move_to(UP * 1.9)
        result = MathTex(r"\sqrt{(-3)^2}=\sqrt9=3", font_size=47,
                         color=self.GREEN).move_to(ORIGIN)
        note = Text("算术平方根取非负值", font="PingFang SC",
                    font_size=28, color=self.CORAL).move_to(DOWN * 1.2)
        self.play(Write(title), Write(question), run_time=0.9)
        self.play(FadeIn(guess), run_time=0.4)
        self.wait(0.8)
        self.play(Write(result), FadeIn(note), run_time=0.8)
        self.wait(1.0)
        self._clear()

    def scene_2_review(self):
        title = self._title("回顾：二次根式的定义")
        definition = self._panel(
            3.5, 2.2,
            MathTex(r"\sqrt a\quad(a\geq0)", font_size=53, color=self.CYAN),
            border=self.CYAN,
        )
        condition = Text("实数范围内，被开方数必须非负。",
                         font="PingFang SC", font_size=28,
                         color=self.MUTED).move_to(UP * 1.4)
        property1 = self._panel(
            -0.4, 1.5,
            MathTex(r"(\sqrt a)^2=a\quad(a\geq0)", font_size=42,
                    color=self.CYAN), border=self.CYAN,
        )
        property2 = self._panel(
            -2.6, 1.5,
            MathTex(r"\sqrt{a^2}=|a|\quad(a\in\mathbb R)",
                    font_size=42, color=self.CORAL), border=self.CORAL,
        )
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        self.play(FadeIn(condition), run_time=0.5)
        self.play(FadeIn(property1), FadeIn(property2), run_time=0.8)
        self.wait(1.0)
        self._clear()

    def scene_3_prop1(self):
        title = self._title("性质一：先开根，再平方", self.CYAN)
        rule = self._panel(
            3.9, 1.65,
            MathTex(r"(\sqrt a)^2=a\quad(a\geq0)", font_size=44,
                    color=self.CYAN), border=self.CYAN,
        )
        steps = self._panel(
            1.5, 1.8,
            MathTex(r"(\sqrt9)^2=3^2=9", font_size=49, color=WHITE),
            border=self.GREEN,
        )
        other = self._panel(
            -0.8, 1.8,
            MathTex(r"(\sqrt5)^2=5", font_size=52, color=self.GREEN),
            border=self.GREEN,
        )
        guard = Text("条件 a ≥ 0 不能省略；√(-9) 在实数中无意义。",
                     font="PingFang SC", font_size=25,
                     color=self.GOLD).move_to(DOWN * 3.0)
        if guard.width > 7.8:
            guard.scale_to_fit_width(7.8)
        self.play(Write(title), FadeIn(rule), run_time=0.8)
        self.play(FadeIn(steps), FadeIn(other), run_time=0.8)
        self.play(FadeIn(guard), run_time=0.5)
        self.wait(1.2)
        self._clear()

    def scene_4_prop2_trap(self):
        title = self._title("性质二：不能直接去掉平方", self.CORAL)
        candidate = self._panel(
            3.9, 1.65,
            MathTex(r"\sqrt{a^2}\stackrel{?}{=}a", font_size=55,
                    color=self.GOLD), border=self.GOLD,
        )
        positive = self._panel(
            1.5, 1.8,
            MathTex(r"a=3:\quad\sqrt{3^2}=3=a", font_size=40,
                    color=self.GREEN), border=self.GREEN,
        )
        negative = self._panel(
            -0.8, 1.8,
            MathTex(r"a=-3:\quad\sqrt{(-3)^2}=3\ne-3", font_size=37,
                    color=self.CORAL), border=self.CORAL,
        )
        conclusion = Text("一个反例就足以否定“对所有实数成立”。",
                          font="PingFang SC", font_size=26,
                          color=self.GOLD).move_to(DOWN * 3.1)
        self.play(Write(title), FadeIn(candidate), run_time=0.8)
        self.play(FadeIn(positive), run_time=0.6)
        self.play(FadeIn(negative), FadeIn(conclusion), run_time=0.7)
        self.wait(1.3)
        self._clear()

    def scene_5_prop2_full(self):
        title = self._title("性质二：绝对值与数轴", self.CORAL)
        rule = MathTex(r"\sqrt{a^2}=|a|\quad(a\in\mathbb R)",
                       font_size=48, color=self.GOLD).move_to(UP * 4.8)
        line = NumberLine(x_range=[-4, 4, 1], length=7.0,
                          include_numbers=True, font_size=25).move_to(UP * 2.7)
        zero = line.n2p(0)
        negative = line.n2p(-3)
        positive = line.n2p(3)
        left_distance = Line(zero, negative, color=self.CORAL, stroke_width=7)
        right_distance = Line(zero, positive, color=self.GREEN, stroke_width=7)
        left_dot = Dot(negative, color=self.CORAL, radius=0.10)
        right_dot = Dot(positive, color=self.GREEN, radius=0.10)
        left_label = MathTex(r"a=-3", font_size=26,
                             color=self.CORAL).next_to(left_dot, UP, buff=0.25)
        right_label = MathTex(r"a=3", font_size=26,
                              color=self.GREEN).next_to(right_dot, UP, buff=0.25)
        explanation = Text("到 0 的距离相同，绝对值都是 3",
                           font="PingFang SC", font_size=27,
                           color=self.MUTED).move_to(UP * 1.5)
        pos_case = self._panel(
            -0.4, 1.65,
            MathTex(r"a\geq0:\quad\sqrt{a^2}=a", font_size=40,
                    color=self.GREEN), border=self.GREEN,
        )
        neg_case = self._panel(
            -2.8, 1.65,
            MathTex(r"a<0:\quad\sqrt{a^2}=-a>0", font_size=40,
                    color=self.CORAL), border=self.CORAL,
        )
        self.play(Write(title), Write(rule), run_time=0.8)
        self.play(Create(line), run_time=0.5)
        self.play(Create(left_distance), Create(right_distance),
                  FadeIn(left_dot), FadeIn(right_dot),
                  FadeIn(left_label), FadeIn(right_label), run_time=0.8)
        self.play(FadeIn(explanation), run_time=0.4)
        self.play(FadeIn(pos_case), FadeIn(neg_case), run_time=0.7)
        self.wait(1.3)
        self._clear()

    def scene_6_pitfall(self):
        title = self._title("判断正误：算术平方根不为负", self.CORAL)
        examples = (
            (r"\sqrt{(-5)^2}=-5", False),
            (r"\sqrt{(-5)^2}=5", True),
            (r"\sqrt{(-2)^2}=|-2|=2", True),
            (r"\sqrt4=-2", False),
        )
        self.play(Write(title), run_time=0.5)
        for index, (formula, valid) in enumerate(examples):
            # 用实际数值判定，确保屏上结论与符号一致；不将列表作为单个动画。
            expected = (square_then_root(-5), square_then_root(-5),
                        square_then_root(-2), math.sqrt(4))[index]
            written = (-5, 5, 2, -2)[index]
            assert (math.isclose(expected, written)) is valid
            answer = Text("正确" if valid else "错误", font="PingFang SC",
                          font_size=25, color=self.GREEN if valid else self.CORAL)
            tex = MathTex(formula, font_size=37, color=WHITE)
            content = VGroup(tex, answer).arrange(RIGHT, buff=0.45)
            card = self._panel(3.9 - index * 1.8, 1.4, content,
                               border=self.GREEN if valid else self.CORAL)
            self.play(FadeIn(card), run_time=0.45)
        self.wait(1.3)
        self._clear()

    def scene_7_summary(self):
        title = self._title("两条性质，条件不同")
        first = self._panel(
            3.8, 2.0,
            MathTex(r"(\sqrt a)^2=a\quad(a\geq0)", font_size=43,
                    color=self.CYAN), border=self.CYAN,
        )
        second = self._panel(
            1.0, 2.0,
            MathTex(r"\sqrt{a^2}=|a|\quad(a\in\mathbb R)",
                    font_size=43, color=self.CORAL), border=self.CORAL,
        )
        final_note = Text("开平方的结果非负；负数先取绝对值。",
                          font="PingFang SC", font_size=29,
                          color=self.GOLD).move_to(DOWN * 2.0)
        self.play(Write(title), FadeIn(first), run_time=0.7)
        self.play(FadeIn(second), FadeIn(final_note), run_time=0.8)
        self.wait(1.5)
        self._clear()
        self.play(FadeOut(self.author_info), run_time=0.35)
