"""高一第二学期《对数函数》；七段教学场景，定义域与可见绘图区间分离。
运行：manim -ql logarithm_function.py LogarithmFunction
未经实际渲染，不得将静态审计认定为视频验收。
"""
from manim import *
import math

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
FONT = "Noto Sans CJK SC"
BACKGROUND = "#1a1a2e"
UP_COLOR = "#3498db"
DOWN_COLOR = "#e74c3c"
POINT_COLOR = "#2ecc71"
ASYMPTOTE_COLOR = "#f39c12"
AUTHOR = "上海初高中数学直通车 @emptyandcalm"


def cn(text, size=27, color=WHITE):
    return Text(text, font=FONT, font_size=size, color=color)


def fit(item, width=7.5):
    if item.width > width:
        item.scale_to_fit_width(width)
    return item


class LogarithmFunction(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        self.author_info = fit(cn(AUTHOR, 17, GRAY_B)).move_to(UP * 7.45)
        self.add(self.author_info)
        self.show_opening()
        self.show_definition()
        self.show_axes()
        self.show_case_a_greater_than_1()
        self.show_case_a_less_than_1()
        self.show_summary()
        self.show_outro()

    def _title(self, value):
        return fit(cn(value, 37, YELLOW)).move_to(UP * 6.4)

    def _clear(self, *items):
        self.play(*[FadeOut(item) for item in items], run_time=0.5)

    def show_opening(self):
        title = self._title("对数函数：底数改变，图像怎样变？")
        question = cn("指数函数的逆函数是什么？", 31).move_to(UP * 3.4)
        exp = MathTex(r"y=2^x", font_size=48, color=UP_COLOR).move_to(UP * 1.5)
        log = MathTex(r"y=\log_2 x", font_size=48, color=POINT_COLOR).move_to(DOWN * 0.5)
        note = cn("观察图像与底数的关系", 27, GRAY_A).move_to(DOWN * 3)
        self.play(Write(title), FadeIn(question), run_time=0.9)
        self.play(Write(exp), run_time=0.7)
        self.play(ReplacementTransform(exp.copy(), log), run_time=1.0)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.0)
        self._clear(title, question, exp, log, note)

    def show_definition(self):
        title = self._title("对数函数的定义")
        formula = MathTex(r"y=\log_a x", font_size=50, color=YELLOW).move_to(UP * 3.7)
        conditions = MathTex(r"a>0,\quad a\ne 1,\quad x>0", font_size=35).move_to(UP * 2)
        domain = MathTex(r"D=(0,+\infty)", font_size=37, color=POINT_COLOR).move_to(UP * 0.2)
        value_range = MathTex(r"R=\mathbb{R}", font_size=37, color=POINT_COLOR).move_to(DOWN * 1.3)
        invariant = MathTex(r"\log_a 1=0", font_size=37, color=UP_COLOR).move_to(DOWN * 3.2)
        note = cn("所有合法底数的图像都经过 (1,0)", 25).move_to(DOWN * 4.5)
        self.play(Write(title), Write(formula), run_time=0.9)
        self.play(Write(conditions), run_time=0.7)
        self.play(Write(domain), Write(value_range), run_time=0.9)
        self.play(Write(invariant), FadeIn(note), run_time=0.8)
        self.wait(1.0)
        self._clear(title, formula, conditions, domain, value_range, invariant, note)

    def show_axes(self):
        title = self._title("建立统一坐标系")
        self.axes = Axes(x_range=[0, 6, 1], y_range=[-3, 3, 1], x_length=6, y_length=6,
                         axis_config={"color": GRAY_B, "stroke_width": 2}, tips=False).move_to(DOWN * 0.3)
        self.fixed_point_dot = Dot(self.axes.c2p(1, 0), color=POINT_COLOR, radius=0.08)
        label = MathTex(r"(1,0)", font_size=26, color=POINT_COLOR).next_to(self.fixed_point_dot, UR, buff=0.2)
        self.asymptote_line = DashedLine(self.axes.c2p(0, -3), self.axes.c2p(0, 3),
                                        color=ASYMPTOTE_COLOR, dash_length=0.12)
        note = fit(cn("x=0 是垂直渐近线，不属于函数定义域", 24, ASYMPTOTE_COLOR))
        note.move_to(DOWN * 4.5)
        self.play(Write(title), Create(self.axes), run_time=1.1)
        self.play(Create(self.asymptote_line), run_time=0.6)
        self.play(FadeIn(self.fixed_point_dot), Write(label), FadeIn(note), run_time=0.8)
        self.wait(0.9)
        self._clear(title, label, note)

    def show_case_a_greater_than_1(self):
        title = self._title("当 a>1：严格递增")
        example = MathTex(r"y=\log_2 x", font_size=34, color=UP_COLOR).move_to(UP * 4.5)
        # log₂(1/8)=-3，log₂6<3，实际显示曲线不超出轴域。
        self.graph_increase = self.axes.plot(lambda x: math.log2(x), x_range=[0.125, 6],
                                             color=UP_COLOR, stroke_width=4)
        points = VGroup()
        for x, y, text in [(1, 0, r"(1,0)"), (2, 1, r"(2,1)"), (4, 2, r"(4,2)")]:
            dot = Dot(self.axes.c2p(x, y), radius=0.065, color=POINT_COLOR)
            label = MathTex(text, font_size=24).next_to(dot, UR, buff=0.12)
            points.add(dot, label)
        caption = cn("在定义域内，x 增大时函数值增大", 25, UP_COLOR).move_to(DOWN * 4.65)
        self.play(Write(title), Write(example), run_time=0.8)
        self.play(Create(self.graph_increase), run_time=1.4)
        self.play(*[FadeIn(obj) for obj in points], run_time=0.8)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(1.0)
        self._clear(title, example, points, caption)

    def show_case_a_less_than_1(self):
        title = self._title("当 0<a<1：严格递减")
        example = MathTex(r"y=\log_{1/2}x", font_size=34, color=DOWN_COLOR).move_to(UP * 4.5)
        # log_(1/2)(1/8)=3，log_(1/2)6>-3，两个分支都处于轴域。
        self.graph_decrease = self.axes.plot(lambda x: math.log(x) / math.log(0.5),
                                             x_range=[0.125, 6], color=DOWN_COLOR,
                                             stroke_width=4)
        points = VGroup()
        for x, y, text in [(1, 0, r"(1,0)"), (2, -1, r"(2,-1)"), (4, -2, r"(4,-2)")]:
            dot = Dot(self.axes.c2p(x, y), radius=0.065, color=POINT_COLOR)
            label = MathTex(text, font_size=24).next_to(dot, DR, buff=0.12)
            points.add(dot, label)
        comparison = MathTex(r"\log_{1/2}x=-\log_2x", font_size=34, color=YELLOW)
        fit(comparison).move_to(DOWN * 4.55)
        self.play(Write(title), Write(example), run_time=0.8)
        self.play(Create(self.graph_decrease), run_time=1.4)
        self.play(*[FadeIn(obj) for obj in points], run_time=0.8)
        self.play(Write(comparison), run_time=0.7)
        self.wait(1.1)
        self._clear(title, example, points, comparison)

    def show_summary(self):
        # 使用已显示的图像对象本身淡出，而非重新构造临时对象。
        self._clear(self.axes, self.asymptote_line, self.fixed_point_dot,
                    self.graph_increase, self.graph_decrease)
        title = self._title("对数函数 · 关键性质")
        lines = VGroup(
            MathTex(r"a>0,\ a\ne1,\ x>0", font_size=35),
            MathTex(r"D=(0,+\infty),\quad R=\mathbb R", font_size=33, color=POINT_COLOR),
            MathTex(r"\log_a1=0", font_size=37, color=YELLOW),
            cn("a>1：严格递增", 28, UP_COLOR),
            cn("0<a<1：严格递减", 28, DOWN_COLOR),
            cn("x=0 是垂直渐近线", 26, ASYMPTOTE_COLOR),
        ).arrange(DOWN, buff=0.52).move_to(UP * 0.3)
        self.play(Write(title), run_time=0.6)
        for line in lines:
            fit(line)
            self.play(FadeIn(line, shift=UP * 0.12), run_time=0.5)
        self.wait(1.0)
        self._clear(title, lines)

    def show_outro(self):
        title = self._title("图像对比，记住两种单调性")
        up = VGroup(MathTex(r"a>1", font_size=35, color=UP_COLOR),
                    cn("严格递增", 30, UP_COLOR)).arrange(RIGHT, buff=0.4).move_to(UP * 2.5)
        down = VGroup(MathTex(r"0<a<1", font_size=35, color=DOWN_COLOR),
                      cn("严格递减", 30, DOWN_COLOR)).arrange(RIGHT, buff=0.4).move_to(UP * 0.2)
        recap = cn("两种情形都经过 (1,0)", 31, POINT_COLOR).move_to(DOWN * 2)
        finish = cn("掌握图像，理解对数函数", 28, YELLOW).move_to(DOWN * 4)
        self.play(Write(title), FadeIn(up), run_time=0.8)
        self.play(FadeIn(down), FadeIn(recap), run_time=0.8)
        self.play(FadeIn(finish), run_time=0.7)
        self.wait(1.2)
        self._clear(title, up, down, recap, finish, self.author_info)
