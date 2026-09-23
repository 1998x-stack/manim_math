"""七年级下·平方根和算术平方根（竖屏教学版）。

保留 SquareRootConcept 入口和七段分镜；在实数范围内区分
“a 的平方根”与符号 sqrt(a)，尤其注意 a=0 和 a<0。
"""
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#1a1a2e"
ROOT = BLUE_C
ARITH = GREEN_C
WARNING = RED_C
HIGHLIGHT = YELLOW


class SquareRootConcept(Scene):
    """七段讲解，保持原有 Scene 类名供现有渲染命令使用。"""

    def fit(self, mob, max_width=7.5):
        if mob.width > max_width:
            mob.scale_to_fit_width(max_width)
        return mob

    def heading(self, name):
        title = self.fit(Text(name, font_size=39, color=GOLD)).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.65)
        return title

    def show_formula(self, formula, y, color=WHITE, size=40):
        mob = self.fit(MathTex(formula, font_size=size, color=color))
        mob.move_to(UP * y)
        self.play(Write(mob), run_time=0.7)
        return mob

    def show_note(self, text, y, color=WHITE, size=26):
        mob = self.fit(Text(text, font_size=size, color=color)).move_to(UP * y)
        self.play(FadeIn(mob), run_time=0.5)
        return mob

    def clear_stage(self):
        # 只对当前屏幕中的同一 Mobject 引用做 FadeOut。
        foreground = [mob for mob in self.mobjects if mob is not self.author_obj]
        if foreground:
            self.play(FadeOut(VGroup(*foreground)), run_time=0.45)

    def construct(self):
        self.camera.background_color = BG
        self.author_obj = self.fit(
            Text("上海初高中数学直通车 @emptyandcalm", font_size=18, color=GRAY_B)
        ).move_to(UP * 6.75)
        self.add(self.author_obj)
        self.scene_opening()
        self.scene_definition()
        self.scene_three_cases()
        self.scene_arithmetic_sqrt()
        self.scene_key_formula()
        self.scene_practice()
        self.scene_outro()

    def scene_opening(self):
        self.heading("面积为 9 的正方形")
        self.show_note("每小格面积为 1，边长有几个单位？", 4.7)
        cells = VGroup(*[
            Square(side_length=0.8, color=ROOT, fill_color=ROOT,
                   fill_opacity=0.16, stroke_width=2)
            for _ in range(9)
        ]).arrange_in_grid(rows=3, cols=3, buff=0).move_to(UP * 1.5)
        self.play(LaggedStart(*(FadeIn(c) for c in cells), lag_ratio=0.08), run_time=1.2)
        self.show_formula(r"3\times3=9", -1.0, HIGHLIGHT)
        self.show_note("几何中的边长必须非负，所以边长是 3", -2.2, ARITH)
        self.wait(0.8)
        self.clear_stage()

    def scene_definition(self):
        self.heading("什么是平方根？")
        self.show_note("如果一个数的平方等于 a，这个数就是 a 的平方根", 4.4)
        self.show_formula(r"x^2=a\quad (a\geq 0)", 2.7)
        self.show_formula(r"x=\pm\sqrt{a}", 1.3, HIGHLIGHT)
        self.show_formula(r"x^2=9\quad\Longrightarrow\quad x=\pm3", -0.4, ROOT)
        self.show_note("方程有两个解：3 和 -3；几何边长只取 3", -2.0, ARITH)
        self.show_note("注意：a=0 时，+0 与 -0 是同一个数", -3.2, HIGHLIGHT)
        self.wait(1.0)
        self.clear_stage()

    def scene_three_cases(self):
        self.heading("平方根的三种情况")
        cases = (
            (r"a>0:\quad x^2=4\Rightarrow x=\pm2", "两个不同的平方根", ROOT),
            (r"a=0:\quad x^2=0\Rightarrow x=0", "只有一个平方根：0", ARITH),
            (r"a<0:\quad x^2=-4", "没有实数解，即没有实数平方根", WARNING),
        )
        for i, (formula, description, color) in enumerate(cases):
            y = 3.8 - 2.5 * i
            self.show_formula(formula, y, color, 34)
            self.show_note(description, y - 0.8, color, 25)
        self.wait(1.1)
        self.clear_stage()

    def scene_arithmetic_sqrt(self):
        self.heading("算术平方根只取非负值")
        self.show_formula(r"\sqrt{9}=3\quad\neq\quad-3", 3.6, ARITH)
        self.show_note("9 的平方根是 -3 和 3", 2.25, ROOT)
        self.show_note("9 的算术平方根只有 3", 1.2, ARITH)
        self.show_formula(r"\sqrt{0}=0", -0.1, HIGHLIGHT)
        self.show_formula(r"\sqrt{a}\geq0\quad (a\geq0)", -1.5, ARITH)
        self.show_note("负数在实数范围内没有算术平方根", -3.1, WARNING)
        self.wait(1.0)
        self.clear_stage()

    def scene_key_formula(self):
        self.heading("为什么要用绝对值？")
        self.show_formula(r"\sqrt{a^2}=|a|\quad (a\in\mathbb{R})", 3.7, HIGHLIGHT)
        self.show_formula(r"a=3:\quad\sqrt{3^2}=3", 1.8, ARITH)
        self.show_formula(r"a=-3:\quad\sqrt{(-3)^2}=3", 0.3, ROOT)
        self.show_formula(r"|-3|=3\neq-3", -1.2, HIGHLIGHT)
        self.show_note("平方后再取算术平方根，结果总是非负", -2.9)
        self.wait(1.0)
        self.clear_stage()

    def scene_practice(self):
        self.heading("练一练：平方根还是算术平方根？")
        exercises = (
            (r"\sqrt{36}=6", ARITH),
            (r"x^2=36\ \Longrightarrow\ x=\pm6", ROOT),
            (r"\sqrt{(-7)^2}=7", ARITH),
            (r"\sqrt{\frac{9}{16}}=\frac{3}{4}", ARITH),
            (r"-\sqrt{0.25}=-0.5", ROOT),
        )
        for i, (formula, color) in enumerate(exercises):
            self.show_formula(formula, 4.1 - 1.6 * i, color, 34)
        self.wait(1.3)
        self.clear_stage()

    def scene_outro(self):
        self.heading("本节要点")
        self.show_note("正数有两个不同的平方根，零只有一个", 3.9, ROOT)
        self.show_note("负数没有实数平方根", 2.6, WARNING)
        self.show_formula(r"\sqrt{a}\geq0\quad (a\geq0)", 0.8, ARITH)
        self.show_formula(r"\sqrt{a^2}=|a|", -0.8, HIGHLIGHT)
        self.show_note("平方根是方程的解，根号表示非负的那个值", -2.5)
        self.wait(2)
