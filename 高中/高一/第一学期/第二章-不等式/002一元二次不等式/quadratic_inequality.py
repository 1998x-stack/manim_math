"""一元二次不等式：根、图像正负区与解集由同一函数数据驱动。

预览：manim -ql quadratic_inequality.py QuadraticInequality
原视频和音轨不随源代码更新；需独立执行真实视频渲染验收。
"""
from math import sqrt

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# 整片主例：f(x)=(x-1)(x-2)，严格不等式不包含两个根。
EXAMPLE_COEFFICIENTS = (1, -3, 2)
GRAPH_X_RANGE = (-0.4, 3.4)
GRAPH_Y_RANGE = (-0.75, 3.8)
# 判别式总结的三个例子均为开口向上的不同函数。
DISCRIMINANT_CASES = ((1, 0, -1), (1, 0, 0), (1, 0, 1))


def quadratic(a, b, c, x):
    return a * x * x + b * x + c


def analyze_quadratic(a, b, c):
    """返回 (判别式, 从小到大的实根)，拒绝退化为一次函数的输入。"""
    if a == 0:
        raise ValueError("一元二次不等式的二次项系数 a 不能为 0")
    delta = b * b - 4 * a * c
    if delta < 0:
        roots = ()
    elif delta == 0:
        roots = (-b / (2 * a),)
    else:
        step = sqrt(delta)
        roots = tuple(sorted(((-b - step) / (2 * a),
                              (-b + step) / (2 * a))))
    return delta, roots


def positive_solution(a, b, c, x):
    """用于数学回归的真值定义；等号根处严格大于零为假。"""
    return quadratic(a, b, c, x) > 0


class QuadraticInequality(Scene):
    FONT = "Noto Sans CJK SC"
    COLOR_PARABOLA = "#3498db"
    COLOR_ROOT = "#e74c3c"
    COLOR_POSITIVE = "#2ecc71"
    COLOR_NEGATIVE = "#e67e22"
    COLOR_HIGHLIGHT = YELLOW
    COLOR_AUXILIARY = GRAY_B

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.setup_mathematics()
        self.author_info = self._text("上海初高中数学直通车 @emptyandcalm", 19, GRAY_B)
        self.author_info.move_to(UP * 6.82)
        self.add(self.author_info)
        self.show_opening()
        self.show_transformation()
        self.show_coordinate_system()
        self.show_parabola()
        self.show_roots()
        self.show_regions()
        self.show_three_cases()
        self.show_outro()

    def setup_mathematics(self):
        self.a, self.b, self.c = EXAMPLE_COEFFICIENTS
        self.delta, self.roots = analyze_quadratic(self.a, self.b, self.c)
        if len(self.roots) != 2:
            raise ValueError("主例必须有两个不等实根")
        self.x1, self.x2 = self.roots
        self.vertex_x = -self.b / (2 * self.a)
        self.vertex_y = self.parabola_func(self.vertex_x)
        self.verify_mathematics()

    def parabola_func(self, x):
        return quadratic(self.a, self.b, self.c, x)

    def verify_mathematics(self):
        if not (self.a > 0 and self.delta > 0 and
                abs(self.parabola_func(self.x1)) < 1e-8 and
                abs(self.parabola_func(self.x2)) < 1e-8 and
                self.x1 < self.vertex_x < self.x2 and self.vertex_y < 0):
            raise ValueError("例题根或抛物线数学数据错误")
        left, right = GRAPH_X_RANGE
        ymin, ymax = GRAPH_Y_RANGE
        if not (left < self.x1 < self.x2 < right and ymin < self.vertex_y):
            raise ValueError("根/顶点超出图域")
        for i in range(101):
            x = left + (right - left) * i / 100
            if not ymin < self.parabola_func(x) < ymax:
                raise ValueError("抛物线采样超出绘制坐标轴 y 范围")

    def _text(self, content, size=27, color=WHITE):
        return Text(content, font=self.FONT, font_size=size, color=color)

    def _formula(self, tex, size=34, color=WHITE):
        obj = MathTex(tex, font_size=size, color=color)
        if obj.width > 7.35:
            obj.scale_to_fit_width(7.35)
        return obj

    def _header(self, value, color=YELLOW):
        obj = self._text(value, 35, color).move_to(UP * 5.62)
        self.play(FadeIn(obj), run_time=0.50)
        return obj

    def show_opening(self):
        header = self._header("一元二次不等式怎么解？")
        question = MathTex(r"x^2-3x+2", ">", "0", font_size=48)
        question.move_to(UP * 2.3)
        self.play(Write(question), run_time=0.80)
        self.play(Indicate(question[1], color=self.COLOR_HIGHLIGHT), run_time=0.55)
        note = self._text("先找零点，再观察函数值的正负", 26, GRAY_A).move_to(ORIGIN)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(header), FadeOut(question), FadeOut(note), run_time=0.55)

    def show_transformation(self):
        header = self._header("把不等式转化为函数图像")
        f = self._formula(r"y=x^2-3x+2=(x-1)(x-2)", 38, self.COLOR_PARABOLA)
        f.move_to(UP * 2.6)
        condition = self._formula(r"f(x)>0", 43, self.COLOR_POSITIVE).move_to(UP * 0.45)
        note = self._text("对应抛物线位于 x 轴上方的横坐标", 24, GRAY_A)
        note.move_to(DOWN * 1.35)
        self.play(Write(f), run_time=0.8)
        self.play(Write(condition), FadeIn(note), run_time=0.75)
        self.wait(0.5)
        self.play(FadeOut(header), FadeOut(condition), FadeOut(note), run_time=0.45)
        self.function_label = f
        self.play(self.function_label.animate.scale(0.72).move_to(UP * 4.85),
                  run_time=0.5)

    def show_coordinate_system(self):
        # 严格使用已验证的绘制域：左右端点和整条曲线均在坐标轴内。
        self.axes = Axes(
            x_range=[GRAPH_X_RANGE[0], GRAPH_X_RANGE[1], 1],
            y_range=[GRAPH_Y_RANGE[0], GRAPH_Y_RANGE[1], 1],
            x_length=7.1, y_length=4.65,
            axis_config={"color": GRAY_B, "stroke_width": 2, "include_tip": False},
        ).move_to(UP * 0.83)
        labels = VGroup(*[
            self._formula(str(n), 22, GRAY_A).next_to(self.axes.c2p(n, 0), DOWN, buff=0.18)
            for n in (0, 1, 2, 3)
        ])
        self.axis_labels = labels
        self.play(Create(self.axes), FadeIn(labels), run_time=0.95)

    def show_parabola(self):
        self.parabola = self.axes.plot(
            self.parabola_func,
            x_range=[GRAPH_X_RANGE[0], GRAPH_X_RANGE[1]],
            color=self.COLOR_PARABOLA, stroke_width=4,
        )
        self.play(Create(self.parabola), run_time=1.2)
        note = self._text("a>0，图像开口向上", 24, GRAY_A).move_to(DOWN * 3.45)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(note), run_time=0.3)

    def show_roots(self):
        title = self._text("第一步：解方程，找零点", 26, self.COLOR_HIGHLIGHT)
        title.move_to(DOWN * 3.32)
        equation = self._formula(r"x^2-3x+2=0", 31).move_to(DOWN * 4.22)
        factored = self._formula(r"(x-1)(x-2)=0", 31).move_to(DOWN * 4.22)
        roots_formula = self._formula(r"x_1=1,\quad x_2=2", 32, self.COLOR_ROOT)
        roots_formula.move_to(DOWN * 5.20)
        self.play(FadeIn(title), Write(equation), run_time=0.75)
        self.play(ReplacementTransform(equation, factored), run_time=0.8)
        self.play(Write(roots_formula), run_time=0.6)
        self.root_group = VGroup()
        for root in self.roots:
            mark = Dot(self.axes.c2p(root, 0), radius=0.105, color=self.COLOR_ROOT)
            label = self._formula(str(int(root)), 24, self.COLOR_ROOT).next_to(
                mark, UP, buff=0.22)
            self.root_group.add(mark, label)
        self.play(FadeIn(self.root_group), run_time=0.60)
        self.wait(0.6)
        self.play(FadeOut(title), FadeOut(factored), FadeOut(roots_formula), run_time=0.5)

    def show_regions(self):
        # 严格不等式不能把根自身包含进解集；颜色只说明曲线在 x 轴哪侧。
        self.positive_areas = VGroup(
            self.axes.get_area(self.parabola, x_range=[GRAPH_X_RANGE[0], self.x1],
                               color=self.COLOR_POSITIVE, opacity=0.24),
            self.axes.get_area(self.parabola, x_range=[self.x2, GRAPH_X_RANGE[1]],
                               color=self.COLOR_POSITIVE, opacity=0.24),
        )
        self.negative_area = self.axes.get_area(
            self.parabola, x_range=[self.x1, self.x2],
            color=self.COLOR_NEGATIVE, opacity=0.24,
        )
        title = self._text("第二步：观察零点两侧的正负", 25, self.COLOR_HIGHLIGHT)
        title.move_to(DOWN * 3.33)
        self.play(FadeIn(title), FadeIn(self.positive_areas), run_time=0.83)
        self.play(FadeIn(self.negative_area), run_time=0.55)
        self.bring_to_front(self.axes, self.axis_labels, self.parabola, self.root_group)
        note = self._text("绿色：f(x)>0；橙色：f(x)<0", 22, GRAY_A)
        note.move_to(DOWN * 4.19)
        answer = self._formula(r"x\in(-\infty,1)\cup(2,+\infty)", 32,
                               self.COLOR_POSITIVE).move_to(DOWN * 5.20)
        endpoint = self._text("严格大于零，不包括 x=1 和 x=2", 22, GRAY_A)
        endpoint.move_to(DOWN * 6.0)
        self.play(FadeIn(note), Write(answer), run_time=0.85)
        self.play(FadeIn(endpoint), run_time=0.48)
        self.wait(0.75)
        self.play(*[FadeOut(m) for m in (title, note, answer, endpoint,
                                         self.positive_areas, self.negative_area)],
                  run_time=0.55)

    def _small_case(self, a, b, c, y, result, title):
        delta, roots = analyze_quadratic(a, b, c)
        axes = Axes(x_range=[-1.7, 1.7, 1], y_range=[-1.2, 3.3, 1],
                    x_length=3.05, y_length=1.47,
                    axis_config={"stroke_width": 1.5, "include_tip": False},
                    ).move_to((-1.82, y, 0))
        # x²+1 对应 Δ<0；绘制端点 |x|≤1.2，图像最高仅 2.44。
        domain = [-1.2, 1.2] if delta < 0 else [-1.45, 1.45]
        graph = axes.plot(lambda x: quadratic(a, b, c, x),
                          x_range=domain, color=self.COLOR_PARABOLA, stroke_width=2.5)
        points = VGroup(*[Dot(axes.c2p(root, 0), color=self.COLOR_ROOT, radius=0.055)
                          for root in roots])
        name = self._text(title, 23, self.COLOR_HIGHLIGHT).move_to((1.45, y + 0.33, 0))
        solution = self._formula(result, 24, self.COLOR_POSITIVE)
        if solution.width > 3.55:
            solution.scale_to_fit_width(3.55)
        solution.move_to((1.45, y - 0.31, 0))
        return VGroup(axes, graph, points, name, solution)

    def show_three_cases(self):
        self.play(FadeOut(self.axes), FadeOut(self.axis_labels),
                  FadeOut(self.parabola), FadeOut(self.root_group),
                  FadeOut(self.function_label), run_time=0.75)
        header = self._header("判别式决定实根情况")
        condition = self._formula(r"a>0,\quad ax^2+bx+c>0", 29, GRAY_A)
        condition.move_to(UP * 4.65)
        self.play(Write(condition), run_time=0.6)
        cases = VGroup(
            self._small_case(*DISCRIMINANT_CASES[0], 3.15,
                             r"x<-1\ \mathrm{or}\ x>1", "Δ>0：两个根"),
            self._small_case(*DISCRIMINANT_CASES[1], 0.0,
                             r"x\ne0", "Δ=0：一个重根"),
            self._small_case(*DISCRIMINANT_CASES[2], -3.0,
                             r"x\in\mathbb{R}", "Δ<0：无实根"),
        )
        for item in cases:
            self.play(FadeIn(item), run_time=0.6)
        note = self._text("若 a<0，须重新判断正负；不能照搬上述解集", 21, self.COLOR_NEGATIVE)
        note.move_to(DOWN * 5.08)
        if note.width > 7.35:
            note.scale_to_fit_width(7.35)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.85)
        self.play(FadeOut(header), FadeOut(condition), FadeOut(cases), FadeOut(note),
                  run_time=0.65)

    def show_outro(self):
        summary = self._text("求根 → 看开口 → 判正负 → 写解集", 30, YELLOW)
        summary.move_to(UP * 1.0)
        self.play(FadeIn(summary), run_time=0.5)
        self.wait(1.0)
        self.play(FadeOut(summary), FadeOut(self.author_info), run_time=0.6)
