"""八年级上配方法：原入口 CompletingTheSquare。预览：manim -pql completing_the_square.py CompletingTheSquare。"""
import math
from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def complete_parameters(a, b, c):
    """ax²+bx+c=0 化为 (x+s)²=t，须 a≠0。"""
    if not all(math.isfinite(v) for v in (a, b, c)) or a == 0:
        raise ValueError("二次项非零且各系数有限")
    s = b / (2 * a)
    return s, s*s - c/a


def complete_roots(a, b, c):
    s, t = complete_parameters(a, b, c)
    if t < 0:
        return ()
    if t == 0:
        return (-s,)
    return (-s-math.sqrt(t), -s+math.sqrt(t))


def area_tiles(x, addend, scale):
    """四块面积 x²、xk、xk、k²，使用同一长度比例。"""
    if not all(math.isfinite(v) and v > 0 for v in (x, addend, scale)):
        raise ValueError("面积示例中所有长度、比例须为正")
    return x*scale, addend*scale, (x*x, x*addend, x*addend, addend*addend)


class CompletingTheSquare(Scene):
    GOLD = "#f9ca24"
    CYAN = "#55cad5"
    RED = "#f48b88"
    GREEN = "#87dda0"
    PURPLE = "#b29cf4"
    MUTED = "#c2ccda"
    PANEL = "#16213e"

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = Text("上海初高中数学直通车 @emptyandcalm",
                                font="PingFang SC", font_size=18,
                                color=self.MUTED).move_to(UP*6.6)
        self.add(self.author_info)
        self.show_opening()
        self.show_perfect_square_review()
        self.show_geometry_visualization()
        self.show_method_steps()
        self.show_example_1()
        self.show_example_2()
        self.show_applications()
        self.show_summary()

    def title(self, value):
        text = Text(value, font="PingFang SC", font_size=39,
                    color=self.GOLD).move_to(UP*5.8)
        if text.width > 7.8:
            text.scale_to_fit_width(7.8)
        return text

    def note(self, value, y, color=None):
        text = Text(value, font="PingFang SC", font_size=26,
                    color=color or self.MUTED).move_to(UP*y)
        if text.width > 7.6:
            text.scale_to_fit_width(7.6)
        return text

    def card(self, y, height, content, color=None):
        border = color or self.CYAN
        frame = RoundedRectangle(corner_radius=.25, width=7.7, height=height,
                                 stroke_color=border, stroke_width=2,
                                 fill_color=self.PANEL, fill_opacity=.92).move_to(UP*y)
        body = content if isinstance(content, VGroup) else VGroup(content)
        body.move_to(frame)
        if body.width > 7.05:
            body.scale_to_fit_width(7.05)
        if body.height > height-.24:
            body.scale_to_fit_height(height-.24)
        return VGroup(frame, body)

    def clear_lesson(self):
        active = [m for m in list(self.mobjects) if m is not self.author_info]
        if active:
            self.play(*[FadeOut(m) for m in active], run_time=.4)

    def show_opening(self):
        heading = self.title("x² + 6x + 5 = 0，怎样配方？")
        before = self.card(3.7, 1.8, MathTex(r"x^2+6x+5=0", font_size=52))
        after = self.card(1.1, 1.8, MathTex(r"x^2+6x=-5", font_size=55), self.GOLD)
        explanation = self.note("一次项系数的一半是 3，两边需要同时加 9", -1.5)
        self.play(Write(heading), FadeIn(before), run_time=.8)
        self.play(FadeIn(after), FadeIn(explanation), run_time=.8)
        self.wait(1)
        self.clear_lesson()

    def show_perfect_square_review(self):
        heading = self.title("回顾：完全平方公式")
        rule = self.card(3.7, 1.8,
                         MathTex(r"(a+b)^2=a^2+2ab+b^2", font_size=48), self.CYAN)
        example = self.card(1.1, 1.8,
                            MathTex(r"(x+3)^2=x^2+6x+9", font_size=48), self.GREEN)
        self.play(Write(heading), FadeIn(rule), run_time=.8)
        self.play(FadeIn(example), FadeIn(self.note("6x=2·x·3，缺少的正方形面积是 9", -1.6)), run_time=.8)
        self.wait(1)
        self.clear_lesson()

    def show_geometry_visualization(self):
        heading = self.title("面积拼图：x² + 6x + 9")
        hint = self.note("示例取 x = 2，边长 2 与 3 使用同一缩放比例", 4.4)
        x_side, k_side, areas = area_tiles(2, 3, .67)
        x_square = Square(side_length=x_side, color=self.CYAN,
                          fill_color=self.CYAN, fill_opacity=.25).move_to(UP*1.35+LEFT*.9)
        right_strip = Rectangle(width=k_side, height=x_side, color=self.RED,
                                fill_color=self.RED, fill_opacity=.27).next_to(x_square, RIGHT, buff=0)
        bottom_strip = Rectangle(width=x_side, height=k_side, color=self.RED,
                                 fill_color=self.RED, fill_opacity=.27).next_to(x_square, DOWN, buff=0)
        missing_square = Square(side_length=k_side, color=self.PURPLE,
                                fill_color=self.PURPLE, fill_opacity=.38).next_to(right_strip, DOWN, buff=0)
        tiles = (x_square, right_strip, bottom_strip, missing_square)
        labels = tuple(MathTex(s, font_size=33).move_to(shape)
                       for s, shape in zip((r"x^2", r"3x", r"3x", r"9"), tiles))
        outline = SurroundingRectangle(VGroup(*tiles), color=self.GREEN, buff=.05)
        formula = MathTex(r"x^2+3x+3x+9=(x+3)^2", font_size=42,
                          color=self.GREEN).move_to(DOWN*2.85)
        limitation = self.note("正长度才能这样画；代数恒等式对任意实数 x 成立", -4.1)
        assert areas == (4, 6, 6, 9) and sum(areas) == 25
        assert math.isclose(right_strip.width, k_side)
        assert math.isclose(bottom_strip.height, k_side)
        self.play(Write(heading), FadeIn(hint), run_time=.7)
        self.play(FadeIn(x_square), Write(labels[0]), run_time=.5)
        self.play(FadeIn(right_strip), FadeIn(bottom_strip),
                  Write(labels[1]), Write(labels[2]), run_time=.8)
        self.play(FadeIn(missing_square), Write(labels[3]), Create(outline), run_time=.8)
        self.play(Write(formula), FadeIn(limitation), run_time=.8)
        self.wait(1)
        self.clear_lesson()

    def show_method_steps(self):
        heading = self.title("配方法：四个步骤")
        steps = (("① 二次项系数先化为 1", self.CYAN),
                 ("② 移常数项到右边", self.PURPLE),
                 ("③ 两边加一次项系数一半的平方", self.GOLD),
                 ("④ 化为平方后检查右侧正负", self.GREEN))
        self.play(Write(heading), run_time=.5)
        for i, (label, color) in enumerate(steps):
            self.play(FadeIn(self.card(4.4-1.9*i, 1.55,
                                       self.note(label, 0, color), color)), run_time=.5)
        self.wait(1)
        self.clear_lesson()

    def show_example_1(self):
        heading = self.title("例题一：x² + 6x + 5 = 0")
        steps = ((r"x^2+6x=-5", self.CYAN),
                 (r"x^2+6x+9=-5+9", self.GOLD),
                 (r"(x+3)^2=4\quad\Rightarrow\quad x+3=\pm2", self.PURPLE),
                 (r"x=-3\pm2:\quad x=-5,-1", self.GREEN))
        shift, rhs = complete_parameters(1, 6, 5)
        roots = complete_roots(1, 6, 5)
        assert (shift, rhs) == (3, 4) and roots == (-5, -1)
        assert all(x*x+6*x+5 == 0 for x in roots)
        self.play(Write(heading), run_time=.5)
        for i, (formula, color) in enumerate(steps):
            self.play(FadeIn(self.card(3.8-2.3*i, 1.65,
                                       MathTex(formula, font_size=45), color)), run_time=.55)
        self.wait(1.1)
        self.clear_lesson()

    def show_example_2(self):
        heading = self.title("例题二：二次项系数不为 1")
        steps = ((r"2x^2-8x+3=0", self.CYAN),
                 (r"x^2-4x=-\frac32", self.GOLD),
                 (r"(x-2)^2=\frac52", self.PURPLE),
                 (r"x=2\pm\sqrt{\frac52}", self.GREEN))
        shift, rhs = complete_parameters(2, -8, 3)
        roots = complete_roots(2, -8, 3)
        assert math.isclose(shift, -2) and math.isclose(rhs, 2.5)
        assert len(roots) == 2
        assert all(math.isclose(2*x*x-8*x+3, 0, abs_tol=1e-12) for x in roots)
        self.play(Write(heading), run_time=.5)
        for i, (formula, color) in enumerate(steps):
            self.play(FadeIn(self.card(3.8-2.3*i, 1.65,
                                       MathTex(formula, font_size=48), color)), run_time=.55)
        self.play(FadeIn(self.note("两边加 4，得到 (x-2)² = 5/2", -5)), run_time=.45)
        self.wait(1.1)
        self.clear_lesson()

    def show_applications(self):
        heading = self.title("配方法还能读出二次函数的顶点")
        formula = self.card(3.7, 1.9,
                            MathTex(r"y=x^2+6x+5=(x+3)^2-4", font_size=45), self.GREEN)
        vertex = self.card(1.1, 1.8,
                           MathTex(r"(-3,-4)", font_size=54), self.CYAN)
        explanation = self.note("开口向上，顶点处达到最小值 -4", -1.5)
        self.play(Write(heading), FadeIn(formula), run_time=.8)
        self.play(FadeIn(vertex), FadeIn(explanation), run_time=.8)
        self.wait(1)
        self.clear_lesson()

    def show_summary(self):
        heading = self.title("总结：配成平方，再检查正负")
        general = self.card(3.7, 1.85,
                            MathTex(r"(x+\frac p2)^2=(\frac p2)^2-q",
                                    font_size=43), self.CYAN)
        note = self.note("先把原方程化为 x² + px + q = 0", 2.2)
        two = self.card(.65, 1.85,
                        MathTex(r"n>0:\quad x=-m\pm\sqrt n", font_size=47), self.GREEN)
        edge = self.note("配成 (x+m)²=n 后：n=0 一解，n<0 无实数解", -1.6)
        self.play(Write(heading), FadeIn(general), FadeIn(note), run_time=.8)
        self.play(FadeIn(two), FadeIn(edge), run_time=.8)
        self.wait(1.1)
        self.clear_lesson()
        self.play(FadeOut(self.author_info), run_time=.35)
