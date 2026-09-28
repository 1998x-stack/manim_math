"""Cambridge A-Level P1 §1.6 — extrema of a quadratic; silent original Manim CE scene.

From this folder: python -m manim render -r 270,480 --fps 15 lesson.py P1QuadraticExtrema
Real-render, font and frame QA are mandatory before publishing a video.
"""
from manim import *
from math_model import UP as UP_QUAD, DOWN, PRACTICE

config.frame_width = 9
config.frame_height = 16
BG = '#101724'
PANEL = '#1B2B40'
WHITE = '#F4F6FD'
MUTED = '#B5C5D8'
CYAN = '#64DED7'
GOLD = '#FFD879'
PINK = '#FF91A6'
GREEN = '#A2E7BD'
GRID = '#3B526B'
CJK = 'Noto Sans CJK SC'


def zh(content, size=26, color=WHITE):
    mob = Text(content, font=CJK, font_size=size, color=color)
    if mob.width > 7.5:
        mob.scale_to_fit_width(7.5)
    return mob


def tex(content, size=40, color=WHITE):
    mob = MathTex(content, font_size=size, color=color)
    if mob.width > 7.5:
        mob.scale_to_fit_width(7.5)
    return mob


def panel(height=1.35):
    return RoundedRectangle(width=7.6, height=height, corner_radius=.15,
                            fill_color=PANEL, fill_opacity=.95,
                            stroke_color=GRID, stroke_width=1.4)


def checkpoint(scene, **named):
    """Fixed-state identity/safe-bbox probe; NOT a rendered-frame review."""
    def descendants(item):
        yield item
        for sub in item.submobjects:
            yield from descendants(sub)
    shown = {id(item) for root in scene.mobjects for item in descendants(root)}
    for key, obj in named.items():
        if id(obj) not in shown and not (obj.submobjects and
                                           all(id(m) in shown for m in obj.submobjects)):
            raise AssertionError(f'{key}: absent from current Scene family')
        if (obj.get_left()[0] < -4 or obj.get_right()[0] > 4 or
                obj.get_bottom()[1] < -7 or obj.get_top()[1] > 7):
            raise AssertionError(f'{key}: outside 9:16 safe zone')


class P1QuadraticExtrema(Scene):
    """9 teaching beats: vertex, axis, coefficients, transformations, graph, domain."""

    def construct(self):
        self.camera.background_color = BG
        assert (UP_QUAD.h, UP_QUAD.k, DOWN.h, DOWN.k) == (2, -3, 3, 4)
        self.brand()
        self.introduction()
        self.square_recap()
        self.moving_parabola()
        self.symmetry_and_intercepts()
        self.general_formula()
        self.maximum_example()
        self.graph_sketch()
        self.restricted_domain()
        self.practice()

    def brand(self):
        pill = RoundedRectangle(width=1.8, height=.53, corner_radius=.14,
                                fill_color=CYAN, fill_opacity=1, stroke_width=0)
        tag = zh('A-Level', 24, BG).move_to(pill)
        track = zh('PURE MATHEMATICS 1 / P1', 18).next_to(pill, RIGHT, buff=.18)
        head = VGroup(pill, tag, track).move_to((0, 6.52, 0))
        rule = Line((-3.7, 6.12, 0), (3.7, 6.12, 0), color=GRID)
        foot = zh('CHAPTER 1  /  1.6 MAXIMUM & MINIMUM', 17, MUTED)
        foot.move_to((0, -6.56, 0))
        self.brand_objects = VGroup(head, rule, foot)
        self.add(self.brand_objects)
        checkpoint(self, header=head, footer=foot)

    def clear_shot(self):
        visible = [m for m in self.mobjects if m is not self.brand_objects]
        if visible:
            self.play(*[FadeOut(m) for m in visible], run_time=.42)

    def heading(self, chinese, english):
        title = zh(chinese, 32).move_to((0, 5.45, 0))
        subtitle = zh(english, 19, MUTED).move_to((0, 4.89, 0))
        self.play(FadeIn(title, shift=.12*UP), FadeIn(subtitle), run_time=.5)
        checkpoint(self, title=title, subtitle=subtitle)
        return title

    def axis(self, xr, yr, width=6.65, height=5.05, pos=(0, .65, 0)):
        ax = Axes(x_range=[xr[0], xr[1], 1], y_range=[yr[0], yr[1], 1],
                  x_length=width, y_length=height,
                  axis_config={'color': MUTED, 'stroke_width': 1.45},
                  tips=False).move_to(pos)
        return ax

    def introduction(self):
        self.heading('为什么抛物线存在最高点或最低点？', 'Maximum and minimum values of a quadratic')
        left = tex(r'y=x^2', 48, CYAN).move_to((0, 3, 0))
        right = tex(r'y=-x^2', 48, GOLD).move_to((0, 1.7, 0))
        arrow_l = Arrow((-1.7, 1.9, 0), (-1.7, .65, 0), color=CYAN, buff=.06)
        arrow_r = Arrow((1.7, .35, 0), (1.7, 1.55, 0), color=GOLD, buff=.06)
        note = zh('正的二次项系数向上开口；负的向下开口。', 26).move_to((0, -1, 0))
        card = panel(1.35).move_to((0, -3.0, 0))
        goal = zh('寻找顶点、对称轴及函数的极值', 28, GREEN).move_to(card)
        self.play(Write(left), GrowArrow(arrow_l), run_time=.75)
        self.play(Write(right), GrowArrow(arrow_r), run_time=.75)
        self.play(FadeIn(note), FadeIn(card), FadeIn(goal))
        checkpoint(self, left=left, right=right, goal=goal)
        self.wait(1.4)
        self.clear_shot()

    def square_recap(self):
        self.heading('回顾配方法：把函数写成顶点式', 'From standard form to vertex form')
        lines = [
            tex(r'f(x)=x^2-4x+1', 47),
            tex(r'= (x^2-4x+4)-3', 39),
            tex(r'=(x-2)^2-3', 51, CYAN),
        ]
        for expr, y in zip(lines, (3.0, 1.35, -.32)):
            expr.move_to((0, y, 0))
            self.play(Write(expr), run_time=.8)
        card = panel(1.6).move_to((0, -3.0, 0))
        text = zh('平方项 ≥ 0，所以最低值为 −3。', 26, GREEN).move_to(card)
        self.play(FadeIn(card), FadeIn(text))
        checkpoint(self, formulas=VGroup(*lines), takeaway=text)
        self.wait(1.7)
        self.clear_shot()

    def moving_parabola(self):
        self.heading('平移抛物线：顶点如何随图像移动？', 'Track horizontal and vertical shifts')
        axes = self.axis((0, 3.2), (-4, 11), width=6.55, height=5.1, pos=(0, .6, 0))
        h, k = ValueTracker(0), ValueTracker(0)
        f = lambda x: (x-h.get_value())**2+k.get_value()
        graph = always_redraw(lambda: axes.plot(f, x_range=[0, 3.2], color=CYAN,
                                                  stroke_width=5))
        vertex = always_redraw(lambda: Dot(axes.c2p(h.get_value(), k.get_value()),
                                            radius=.085, color=GOLD))
        symmetry = always_redraw(lambda: DashedLine(
            axes.c2p(h.get_value(), -3.5), axes.c2p(h.get_value(), 10.5),
            color=GOLD, dash_length=.15, stroke_width=1.6))
        self.play(Create(axes), Create(graph), FadeIn(vertex), FadeIn(symmetry), run_time=1)
        start = tex(r'(h,k)=(0,0)', 39, GOLD).move_to((0, -3.2, 0))
        self.play(FadeIn(start))
        checkpoint(self, axes=axes, graph=graph, vertex=vertex, axis=symmetry, label=start)
        self.wait(.65)
        self.play(h.animate.set_value(2), run_time=2.1)
        self.play(k.animate.set_value(-3), run_time=2.0)
        finish = tex(r'(h,k)=(2,-3)', 40, GREEN).move_to(start)
        self.play(Transform(start, finish), run_time=.6)
        checkpoint(self, graph=graph, vertex=vertex, axis=symmetry, label=start)
        assert (h.get_value(), k.get_value()) == (float(UP_QUAD.h), float(UP_QUAD.k))
        self.wait(1.3)
        self.clear_shot()

    def symmetry_and_intercepts(self):
        self.heading('顶点、对称轴与对称的两点', 'Every parabola is symmetric about its vertex')
        axes = self.axis((-1, 5), (-4, 8), pos=(0, 1.05, 0))
        graph = axes.plot(lambda x: float(UP_QUAD.value(x)), x_range=[-.65, 4.65],
                          color=CYAN, stroke_width=5)
        v = Dot(axes.c2p(float(UP_QUAD.h), float(UP_QUAD.k)), color=GOLD, radius=.09)
        axis = DashedLine(axes.c2p(2, -3.6), axes.c2p(2, 6.2), color=GOLD)
        p = Dot(axes.c2p(1, float(UP_QUAD.value(1))), color=GREEN)
        q = Dot(axes.c2p(3, float(UP_QUAD.value(3))), color=GREEN)
        pair = tex(r'f(1)=f(3)=-2', 33, GREEN).move_to((0, -3.55, 0))
        axis_label = tex(r'x=2', 33, GOLD).move_to((2.85, 3.9, 0))
        self.play(Create(axes), Create(graph), FadeIn(v), Create(axis), run_time=1.3)
        self.play(FadeIn(p), FadeIn(q), Write(pair), FadeIn(axis_label))
        checkpoint(self, axes=axes, curve=graph, vertex=v, axis=axis,
                   left=p, right=q, eq=pair, axis_label=axis_label)
        self.wait(1.5)
        self.clear_shot()

    def general_formula(self):
        self.heading('用系数直接求顶点坐标', 'The general vertex formula')
        formulas = [
            tex(r'f(x)=ax^2+bx+c\quad(a\ne0)', 39),
            tex(r'=a\left(x+\frac{b}{2a}\right)^2+c-\frac{b^2}{4a}', 35, CYAN),
            tex(r'h=-\frac{b}{2a}', 47, GOLD),
            tex(r'k=f(h)=c-\frac{b^2}{4a}', 41, GREEN),
        ]
        for formula, y in zip(formulas, (3.15, 1.6, -.25, -1.72)):
            formula.move_to((0, y, 0))
            self.play(Write(formula), run_time=1.0)
        card = panel(1.05).move_to((0, -4.0, 0))
        reminder = zh('a > 0 取最小值；a < 0 取最大值', 26).move_to(card)
        self.play(FadeIn(card), FadeIn(reminder))
        checkpoint(self, equations=VGroup(*formulas), reminder=reminder)
        self.wait(1.6)
        self.clear_shot()

    def maximum_example(self):
        self.heading('开口向下：寻找最高点', 'A negative leading coefficient gives a maximum')
        formula = tex(r'g(x)=-x^2+6x-5=4-(x-3)^2', 34, GOLD).move_to((0, 3.98, 0))
        axes = self.axis((-1, 7), (-6, 6), pos=(0, .6, 0))
        graph = axes.plot(lambda x: float(DOWN.value(x)), x_range=[0, 6.15],
                          color=GOLD, stroke_width=5)
        vertex = Dot(axes.c2p(float(DOWN.h), float(DOWN.k)), color=PINK, radius=.09)
        axline = DashedLine(axes.c2p(3, -5.6), axes.c2p(3, 5.5), color=PINK)
        roots = VGroup(*[Dot(axes.c2p(x, 0), color=GREEN, radius=.075)
                         for x in DOWN.roots()])
        ans = tex(r'\max g(x)=4\quad\text{at }x=3', 34, GREEN).move_to((0, -3.5, 0))
        self.play(Write(formula), Create(axes))
        self.play(Create(graph), FadeIn(vertex), Create(axline), FadeIn(roots), run_time=1.2)
        self.play(Write(ans))
        checkpoint(self, formula=formula, axes=axes, curve=graph, vertex=vertex,
                   line=axline, intercepts=roots, answer=ans)
        self.wait(1.6)
        self.clear_shot()

    def graph_sketch(self):
        self.heading('作图时标注顶点与坐标轴交点', 'Graph sketch: vertex, axis and intercepts')
        axes = self.axis((-1, 5), (-4, 8), pos=(0, 1.0, 0))
        graph = axes.plot(lambda x: float(UP_QUAD.value(x)), x_range=[-.65, 4.65],
                          color=CYAN, stroke_width=5)
        vertex = Dot(axes.c2p(2, -3), color=GOLD)
        xdots = VGroup(*[Dot(axes.c2p(x, 0), radius=.08, color=GREEN)
                         for x in UP_QUAD.roots()])
        ydot = Dot(axes.c2p(0, 1), radius=.08, color=PINK)
        formula = tex(r'f(x)=(x-2)^2-3', 40).move_to((0, 4.12, 0))
        labels = VGroup(tex(r'(2,-3)', 32, GOLD),
                        tex(r'x=2\pm\sqrt3', 31, GREEN),
                        tex(r'(0,1)', 31, PINK))
        labels[0].move_to((1.68, -3.02, 0))
        labels[1].move_to((0, -4.15, 0))
        labels[2].move_to((-2.75, 3.05, 0))
        self.play(Create(axes), Write(formula), Create(graph), run_time=1.2)
        self.play(FadeIn(vertex), FadeIn(xdots), FadeIn(ydot), *[FadeIn(m) for m in labels])
        checkpoint(self, graph=graph, dots=xdots, ydot=ydot, vertex=vertex,
                   labels=labels, formula=formula)
        self.wait(1.8)
        self.clear_shot()

    def restricted_domain(self):
        self.heading('注意定义域：顶点未必是区间最值点', 'Extrema on a restricted interval')
        bounds = UP_QUAD.interval_extrema(3, 4)
        assert bounds['min'] == (-2, 3) and bounds['max'] == (1, 4)
        axes = self.axis((0, 5), (-4, 4), pos=(0, 1.0, 0))
        faint = axes.plot(lambda x: float(UP_QUAD.value(x)), x_range=[0, 4.7],
                          color=MUTED, stroke_opacity=.38)
        segment = axes.plot(lambda x: float(UP_QUAD.value(x)), x_range=[3, 4],
                            color=CYAN, stroke_width=7)
        ends = VGroup(Dot(axes.c2p(3, -2), color=GREEN),
                      Dot(axes.c2p(4, 1), color=GOLD))
        restriction = tex(r'3\le x\le4', 42).move_to((0, 3.9, 0))
        verdict = tex(r'\min f=-2\ (x=3),\quad\max f=1\ (x=4)',
                      31, GREEN).move_to((0, -3.6, 0))
        reminder = zh('整条抛物线的顶点 x=2 不在此区间内。', 24, MUTED)
        reminder.move_to((0, -4.55, 0))
        self.play(Write(restriction), Create(axes), Create(faint))
        self.play(Create(segment), FadeIn(ends))
        self.play(Write(verdict), FadeIn(reminder))
        checkpoint(self, plot=segment, endpoints=ends, restriction=restriction,
                   answer=verdict, note=reminder)
        self.wait(1.7)
        self.clear_shot()

    def practice(self):
        self.heading('独立练习：求最大值并写出顶点', 'Your turn: identify the maximum and vertex')
        question = tex(r'q(x)=-x^2+4x+1', 49, GOLD).move_to((0, 3.15, 0))
        prompt = zh('暂停思考：用配方法求 q 的最大值。', 28).move_to((0, 1.45, 0))
        self.play(Write(question), FadeIn(prompt))
        self.wait(2.8)
        steps = [
            tex(r'q(x)=5-(x-2)^2', 44, CYAN),
            tex(r'\text{vertex }(2,5)', 41, GOLD),
            tex(r'\boxed{\max q(x)=5\ \text{at }x=2}', 40, GREEN),
        ]
        for mob, y in zip(steps, (.12, -1.25, -2.8)):
            mob.move_to((0, y, 0))
            self.play(Write(mob), run_time=.85)
        summary = zh('配方 → 顶点 → 对称轴 → 最值 → 截距核对', 24, MUTED)
        summary.move_to((0, -4.45, 0))
        self.play(FadeIn(summary))
        checkpoint(self, question=question, answer=VGroup(*steps), summary=summary)
        self.wait(2.0)
