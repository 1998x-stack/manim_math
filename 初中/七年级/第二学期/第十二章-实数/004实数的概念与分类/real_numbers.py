"""七年级下册：实数及两种分类（1080×1920，保留 RealNumbersConcept）。"""
from manim import *
import math

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
RATIONAL = BLUE_C
IRRATIONAL = ORANGE
ACCENT = YELLOW


class RealNumbersConcept(Scene):
    def fit(self, mob, max_width=7.5):
        if mob.width > max_width:
            mob.scale_to_fit_width(max_width)
        return mob

    def heading(self, title):
        mob = self.fit(Text(title, font_size=38, color=GOLD)).move_to(UP * 5.8)
        self.play(Write(mob), run_time=0.6)
        return mob

    def note(self, text, y, color=WHITE, size=26):
        mob = self.fit(Text(text, font_size=size, color=color)).move_to(UP * y)
        self.play(FadeIn(mob), run_time=0.5)
        return mob

    def formula(self, tex, y, color=WHITE, size=38):
        mob = self.fit(MathTex(tex, font_size=size, color=color)).move_to(UP * y)
        self.play(Write(mob), run_time=0.7)
        return mob

    def clear_stage(self):
        visible = [m for m in self.mobjects if m is not self.author]
        if visible:
            self.play(FadeOut(VGroup(*visible)), run_time=0.4)

    def construct(self):
        self.camera.background_color = BG
        self.author = self.fit(
            Text("上海初高中数学直通车 @emptyandcalm", font_size=18, color=GRAY_B)
        ).move_to(UP * 6.75)
        self.add(self.author)
        self.scene_opening()
        self.scene_number_line()
        self.scene_classification_tree()
        self.scene_examples()
        self.scene_pos_neg_classification()
        self.scene_outro()

    def scene_opening(self):
        self.heading("哪些数属于实数？")
        numbers = VGroup(
            MathTex(r"\frac{1}{2}", color=RATIONAL, font_size=52),
            MathTex(r"\sqrt{2}", color=IRRATIONAL, font_size=52),
            MathTex(r"\pi", color=IRRATIONAL, font_size=52),
            MathTex(r"-3", color=RATIONAL, font_size=52),
            MathTex(r"0", color=RATIONAL, font_size=52),
        ).arrange_in_grid(rows=2, cols=3, buff=(0.9, 1.2)).move_to(UP * 1.1)
        self.play(LaggedStart(*(FadeIn(m) for m in numbers), lag_ratio=0.2), run_time=1.3)
        self.note("有理数和无理数共同构成实数", -2.6, ACCENT)
        self.wait(0.8)
        self.clear_stage()

    def scene_number_line(self):
        self.heading("实数与数轴一一对应")
        line = NumberLine(
            x_range=[-1, 4, 1], length=7.1, include_numbers=True,
            include_tip=True, color=GRAY_B, font_size=27,
        ).move_to(UP * 1.6)
        self.play(Create(line), run_time=0.9)
        # 数轴已有整数数字，仅为无理数添加点与上方标签。
        for value, name in ((math.sqrt(2), r"\sqrt{2}"), (math.pi, r"\pi")):
            dot = Dot(line.number_to_point(value), radius=0.095, color=IRRATIONAL)
            label = MathTex(name, font_size=31, color=IRRATIONAL)
            label.next_to(dot, UP, buff=0.35)
            self.play(FadeIn(dot), Write(label), run_time=0.55)
        self.note("根号 2 和圆周率也能在数轴上找到位置", -0.3, IRRATIONAL)
        self.note("小数近似只是定位辅助，不是无理性的证明", -1.5)
        self.note("每个实数对应一个点；每个点对应一个实数", -3.0, ACCENT)
        self.wait(1.0)
        self.clear_stage()

    def scene_classification_tree(self):
        self.heading("分类一：有理数与无理数")
        self.formula(r"\mathbb{R}=\mathbb{Q}\cup(\mathbb{R}\setminus\mathbb{Q})", 4.2, ACCENT, 33)
        left = RoundedRectangle(width=3.4, height=3.6, corner_radius=0.16,
                                color=RATIONAL, fill_opacity=0.08)
        right = RoundedRectangle(width=3.4, height=3.6, corner_radius=0.16,
                                 color=IRRATIONAL, fill_opacity=0.08)
        left.move_to(LEFT * 1.85 + UP * 0.5)
        right.move_to(RIGHT * 1.85 + UP * 0.5)
        self.play(Create(left), Create(right), run_time=0.6)
        rational_text = VGroup(
            Text("有理数", font_size=30, color=RATIONAL),
            Text("整数", font_size=24),
            Text("非整数有理数", font_size=24),
            MathTex(r"-2,\ 0,\ \frac{1}{3},\ 0.25", font_size=26, color=RATIONAL),
        ).arrange(DOWN, buff=0.35)
        self.fit(rational_text, 3.1).move_to(left.get_center())
        irrational_text = VGroup(
            Text("无理数", font_size=30, color=IRRATIONAL),
            Text("无限不循环小数", font_size=24),
            MathTex(r"\sqrt{2},\ \pi,\ -\sqrt{3}", font_size=30, color=IRRATIONAL),
        ).arrange(DOWN, buff=0.5)
        self.fit(irrational_text, 3.1).move_to(right.get_center())
        self.play(FadeIn(rational_text), FadeIn(irrational_text), run_time=0.9)
        self.note("两类互不重叠，合在一起就是全部实数", -3.0, ACCENT)
        self.wait(1.0)
        self.clear_stage()

    def scene_examples(self):
        self.heading("判断时先化简再分类")
        examples = (
            (r"\sqrt{4}=2", "有理数：正整数", RATIONAL),
            (r"0.\overline{3}=\frac{1}{3}", "有理数：无限循环小数", RATIONAL),
            (r"0.25=\frac{1}{4}", "有理数：有限小数", RATIONAL),
            (r"\sqrt{2}", "无理数：不能写成整数比", IRRATIONAL),
        )
        for i, (tex, description, color) in enumerate(examples):
            y = 4.2 - 2.1 * i
            self.formula(tex, y, color, 33)
            self.note(description, y - 0.75, color, 23)
        self.wait(0.9)
        self.clear_stage()

    def scene_pos_neg_classification(self):
        self.heading("分类二：正数、零、负数")
        groups = (
            ("正实数", r"\frac{1}{3},\ \sqrt{2},\ \pi", BLUE_C),
            ("零", r"0", PURPLE_C),
            ("负实数", r"-2,\ -\sqrt{3},\ -\pi", ORANGE),
        )
        for i, (text, tex, color) in enumerate(groups):
            y = 3.9 - i * 2.55
            self.note(text, y, color, 30)
            self.formula(tex, y - 0.85, color, 32)
        self.wait(1.0)
        self.clear_stage()

    def scene_outro(self):
        self.heading("两种分类，不能混淆")
        self.note("有理数和无理数：按表示方式分类", 4.0, RATIONAL)
        self.note("正实数、零、负实数：按符号分类", 2.5, IRRATIONAL)
        self.formula(r"\sqrt{4}=2\in\mathbb{Q}", 0.65, ACCENT)
        self.formula(r"\sqrt{2}\notin\mathbb{Q}", -0.7, IRRATIONAL)
        self.note("分类前要看清数值与条件", -2.5)
        self.wait(2)
