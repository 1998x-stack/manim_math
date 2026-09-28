"""七年级下册：立方根。保留原 CubeRootConcept 入口与六段分镜。

正方体仅用于正体积的几何引入；负数立方根用代数和数轴表示。
"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
POS = BLUE_C
NEG = ORANGE
ZERO = PURPLE_C
KEY = YELLOW


class CubeRootConcept(Scene):
    def fit(self, mob, width=7.5):
        if mob.width > width:
            mob.scale_to_fit_width(width)
        return mob

    def heading(self, title):
        mob = self.fit(Text(title, font_size=40, color=GOLD)).move_to(UP * 5.8)
        self.play(Write(mob), run_time=0.6)
        return mob

    def formula(self, latex, y, color=WHITE, size=38):
        mob = self.fit(MathTex(latex, font_size=size, color=color)).move_to(UP * y)
        self.play(Write(mob), run_time=0.65)
        return mob

    def note(self, description, y, color=WHITE, size=26):
        mob = self.fit(Text(description, font_size=size, color=color)).move_to(UP * y)
        self.play(FadeIn(mob), run_time=0.45)
        return mob

    def clear_stage(self):
        visible = [mob for mob in self.mobjects if mob is not self.author]
        if visible:
            self.play(FadeOut(VGroup(*visible)), run_time=0.4)

    def construct(self):
        self.camera.background_color = BG
        self.author = self.fit(
            Text("上海初高中数学直通车 @emptyandcalm", font_size=18, color=GRAY_B)
        ).move_to(UP * 6.75)
        self.add(self.author)
        self.scene_opening()
        self.scene_definition()
        self.scene_three_cases()
        self.scene_practice()
        self.scene_comparison()
        self.scene_outro()

    def scene_opening(self):
        self.heading("体积为 8 的正方体")
        self.note("边长为多少个单位？", 4.5)
        # 正体积的正方体二维投影；物理长度不用于表示负数。
        front = Square(side_length=2.25, color=POS, fill_opacity=0.15)
        top = Polygon(front.get_corner(UL), front.get_corner(UR),
                      front.get_corner(UR) + RIGHT * 0.65 + UP * 0.4,
                      front.get_corner(UL) + RIGHT * 0.65 + UP * 0.4,
                      color=POS, fill_opacity=0.25)
        right = Polygon(front.get_corner(DR), front.get_corner(UR),
                        front.get_corner(UR) + RIGHT * 0.65 + UP * 0.4,
                        front.get_corner(DR) + RIGHT * 0.65 + UP * 0.4,
                        color=POS, fill_opacity=0.3)
        cube = VGroup(front, top, right).move_to(UP * 1.7)
        self.play(Create(front), Create(top), Create(right), run_time=1.0)
        self.formula(r"V=2\times2\times2=8", -0.8, POS)
        self.note("几何边长是 2，不能是负数", -2.1, KEY)
        self.wait(0.8)
        self.clear_stage()

    def scene_definition(self):
        self.heading("什么是立方根？")
        self.note("若一个实数的立方等于 a，它就是 a 的立方根", 4.5)
        self.formula(r"x^3=a\quad\Longleftrightarrow\quad x=\sqrt[3]{a}", 2.8, KEY)
        self.formula(r"2^3=8\quad\Longrightarrow\quad\sqrt[3]{8}=2", 0.9, POS)
        self.formula(r"(-2)^3=-8\quad\Longrightarrow\quad\sqrt[3]{-8}=-2", -0.8, NEG)
        self.note("负数立方根是代数中的数，不代表负的几何体积", -2.7)
        self.wait(0.9)
        self.clear_stage()

    def scene_three_cases(self):
        self.heading("任意实数都有唯一立方根")
        cases = (
            (r"\sqrt[3]{8}=2", "正数的立方根是正数", POS),
            (r"\sqrt[3]{0}=0", "零的立方根是零", ZERO),
            (r"\sqrt[3]{-8}=-2", "负数的立方根是负数", NEG),
        )
        for i, (formula, text, color) in enumerate(cases):
            y = 3.9 - i * 2.4
            self.formula(formula, y, color, 37)
            self.note(text, y - 0.8, color)
        self.wait(0.9)
        self.clear_stage()

    def scene_practice(self):
        self.heading("计算立方根")
        exercises = (
            (r"\sqrt[3]{27}=3", POS),
            (r"\sqrt[3]{-27}=-3", NEG),
            (r"\sqrt[3]{\frac{1}{8}}=\frac{1}{2}", POS),
            (r"\sqrt[3]{-\frac{1}{8}}=-\frac{1}{2}", NEG),
            (r"\sqrt[3]{1000}=10", POS),
        )
        for i, (formula, color) in enumerate(exercises):
            self.formula(formula, 4.2 - i * 1.7, color, 37)
        self.wait(1.1)
        self.clear_stage()

    def scene_comparison(self):
        self.heading("平方根与立方根对比")
        self.note("在实数范围内，负数没有平方根", 4.2, NEG)
        self.formula(r"x^2=-8\quad (x\in\mathbb{R})", 2.6, NEG, 31)
        self.note("负数却有唯一的立方根", 0.95, POS)
        self.formula(r"x^3=-8\quad\Longrightarrow\quad x=-2", -0.6, POS)
        self.formula(r"\sqrt{(-2)^2}=2", -2.0, KEY)
        self.formula(r"\sqrt[3]{(-2)^3}=-2", -3.35, KEY)
        self.wait(1.0)
        self.clear_stage()

    def scene_outro(self):
        self.heading("本课总结")
        self.formula(r"\sqrt[3]{a^3}=a\quad (a\in\mathbb{R})", 3.9, KEY)
        self.note("每个实数都有唯一立方根", 2.15, POS)
        self.note("负数的立方根是负数，零的立方根是零", 0.9, NEG)
        self.formula(r"\sqrt[3]{-a}=-\sqrt[3]{a}", -0.7, KEY)
        self.note("别把立方根的正负号当作几何边长", -2.3)
        self.wait(1.8)
