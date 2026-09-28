"""A-Level Pure Mathematics 1 §1.4: one linear + one quadratic equation.

Original, silent Manim Community 9:16 scene; eight teaching beats, persistent P1 mark.
From this directory: python -m manim render -r 270,480 --fps 15 lesson.py P1LinearQuadratic
Requires Manim CE, a working TeX installation and Noto Sans CJK SC.
"""
from math import cos, sin, sqrt
from manim import *
from math_model import (MAIN_CURVE, MAIN_LINE, TANGENT, MISSED,
                        PRACTICE_CURVE, PRACTICE_LINE,
                        discriminant, intersections, circle_line_points)

config.frame_width = 9
config.frame_height = 16
BG, PANEL, INK = '#101724', '#1A2A3E', '#F0F5FC'
TEAL, GOLD, PINK, GREEN = '#55DCD0', '#FFD36B', '#FF8C9A', '#92E5B5'
GRID, MUTED = '#36536A', '#AFC2D5'
FONT = 'Noto Sans CJK SC'


def cn(value, size=29, color=INK):
    out = Text(value, font=FONT, font_size=size, color=color)
    if out.width > 7.48:
        out.scale_to_fit_width(7.48)
    return out


def eq(value, size=40, color=INK):
    out = MathTex(value, font_size=size, color=color)
    if out.width > 7.48:
        out.scale_to_fit_width(7.48)
    return out


def panel(height=1.4):
    return RoundedRectangle(width=7.65, height=height, corner_radius=.13,
                            fill_color=PANEL, fill_opacity=.93,
                            stroke_color=GRID, stroke_width=1.5)


def checkpoint(scene, **objects):
    """Inspect real registered objects at explicit frames; not a whole-video guarantee."""
    def family(obj):
        yield obj
        for sub in obj.submobjects:
            yield from family(sub)
    present = {id(obj) for root in scene.mobjects for obj in family(root)}
    for name, mob in objects.items():
        if id(mob) not in present and not (
                mob.submobjects and all(id(sub) in present for sub in mob.submobjects)):
            raise AssertionError(f'{name}: object not in current Scene family')
        if (mob.get_left()[0] < -4.01 or mob.get_right()[0] > 4.01 or
                mob.get_bottom()[1] < -7.01 or mob.get_top()[1] > 7.01):
            raise AssertionError(f'{name}: outside portrait safe area')


class P1LinearQuadratic(Scene):
    """Eight beats: meaning, graph, elimination, checking, sweep, conic, pitfall, practice."""

    def construct(self):
        self.camera.background_color = BG
        assert intersections(MAIN_CURVE, MAIN_LINE) == ((0, 1), (3, 4))
        assert intersections(MAIN_CURVE, TANGENT) == ((1.5, .25),)
        assert len(intersections(MAIN_CURVE, MISSED)) == 0
        self.brand()
        self.introduction()
        self.graph_and_pairing()
        self.substitution()
        self.check_answers()
        self.sweep()
        self.circle_example()
        self.pitfalls()
        self.practice()

    def brand(self):
        pill = RoundedRectangle(width=1.8, height=.52, corner_radius=.13,
                                fill_color=TEAL, fill_opacity=1, stroke_width=0)
        tag = cn('A-Level', 25, BG).move_to(pill)
        title = cn('PURE MATHEMATICS 1 / P1', 19).next_to(pill, RIGHT, buff=.18)
        header = VGroup(pill, tag, title).move_to((0, 6.56, 0))
        rule = Line((-3.77, 6.12, 0), (3.77, 6.12, 0), color=GRID)
        footer = cn('CHAPTER 1  /  1.4 SIMULTANEOUS EQUATIONS', 18, MUTED)
        footer.move_to((0, -6.61, 0))
        self.fixed = VGroup(header, rule, footer)
        self.add(self.fixed)
        checkpoint(self, title=header, footer=footer)

    def wipe(self):
        old = [obj for obj in self.mobjects if obj is not self.fixed]
        if old:
            self.play(*[FadeOut(obj) for obj in old], run_time=.40)

    def heading(self, chinese, english):
        zh = cn(chinese, 32).move_to((0, 5.43, 0))
        en = cn(english, 20, MUTED).move_to((0, 4.91, 0))
        self.play(FadeIn(zh, shift=.12*UP), FadeIn(en), run_time=.55)
        checkpoint(self, heading=zh, translation=en)

    def main_axes(self):
        ax = Axes(x_range=[-1, 4, 1], y_range=[-3.5, 9, 2],
                  x_length=6.65, y_length=5.35, tips=False,
                  axis_config={'color': MUTED, 'stroke_width': 1.25,
                               'include_numbers': True, 'font_size': 17})
        ax.move_to((0, .23, 0))
        return ax

    def note(self, message, y=-4.23, color=MUTED):
        bar = panel(1.15).move_to((0, y, 0))
        text = cn(message, 24, color).move_to(bar)
        self.play(FadeIn(bar), FadeIn(text), run_time=.42)
        return VGroup(bar, text)

    def introduction(self):
        self.heading('1.4 一次方程与二次方程的联立', 'One linear equation + one quadratic equation')
        p = panel(2.55).move_to((0, 1.58, 0))
        e1 = eq(r'y=x^2-2x+1', 49, TEAL).move_to((0, 2.22, 0))
        e2 = eq(r'y=x+1', 49, GOLD).move_to((0, .96, 0))
        question = cn('什么样的 (x, y) 同时满足这两个方程？', 27)
        question.move_to((0, -1.15, 0))
        arrows = VGroup(Arrow((-2.1, -.04, 0), (-.4, -.64, 0), buff=.12, color=TEAL),
                        Arrow((2.1, -.04, 0), (.4, -.64, 0), buff=.12, color=GOLD))
        self.play(FadeIn(p), Write(e1), Write(e2), run_time=1.0)
        self.play(GrowArrow(arrows[0]), GrowArrow(arrows[1]), FadeIn(question), run_time=.75)
        self.note('一组解是一个有序数对，必须同时满足两式。', y=-3.0)
        checkpoint(self, equations=VGroup(e1, e2), prompt=question)
        self.wait(1.7)
        self.wipe()

    def graph_and_pairing(self):
        self.heading('先看图像：交点代表公共解', 'Intersections represent simultaneous solutions')
        ax = self.main_axes()
        curve = ax.plot(lambda x: float(MAIN_CURVE.at(x)),
                        x_range=[-.75, 3.75, .025], color=TEAL, stroke_width=4)
        line = ax.plot(lambda x: float(MAIN_LINE.at(x)),
                       x_range=[-.75, 3.75, .025], color=GOLD, stroke_width=4)
        dots = VGroup(*[Dot(ax.c2p(float(x), float(y)), radius=.075, color=GREEN)
                        for x, y in intersections(MAIN_CURVE, MAIN_LINE)])
        labels = VGroup(eq(r'A(0,1)', 31, GREEN), eq(r'B(3,4)', 31, GREEN))
        labels[0].next_to(dots[0], UL, buff=.12)
        labels[1].next_to(dots[1], UR, buff=.12)
        # Keep labels in the x/y coordinate frame; both dots come from math_model.
        legend = VGroup(eq(r'y=x^2-2x+1', 30, TEAL), eq(r'y=x+1', 30, GOLD))
        legend.arrange(DOWN, buff=.18).move_to((0, -3.36, 0))
        self.play(Create(ax), run_time=.75)
        self.play(Create(curve), Create(line), run_time=1.4)
        self.play(FadeIn(dots), FadeIn(labels), FadeIn(legend), run_time=.8)
        checkpoint(self, axes=ax, curve=curve, line=line, intersections=dots,
                   point_labels=labels, legend=legend)
        self.wait(2.0)
        self.wipe()

    def substitution(self):
        self.heading('代入消元：把两个方程变成一个', 'Substitute the linear equation into the quadratic')
        lines = [
            (r'x^2-2x+1=x+1', INK),
            (r'x^2-3x=0', TEAL),
            (r'x(x-3)=0', GOLD),
            (r'x=0\quad\text{or}\quad x=3', GREEN),
        ]
        rows = VGroup()
        for i, (latex, color) in enumerate(lines):
            obj = eq(latex, 46 if i != 3 else 42, color).move_to((0, 3.45-i*1.35, 0))
            self.play(Write(obj), run_time=.85)
            rows.add(obj)
            self.wait(.30)
        explanation = self.note('先消去 y，再用因式分解求 x 的值。', -3.34)
        checkpoint(self, derivation=rows, explanation=explanation)
        self.wait(1.7)
        self.wipe()

    def check_answers(self):
        self.heading('代回求 y：不能只写出 x 的解', 'Back-substitute and check both equations')
        left = panel(2.35).move_to((-1.85, 1.6, 0)).set_width(3.63, stretch=True)
        right = panel(2.35).move_to((1.85, 1.6, 0)).set_width(3.63, stretch=True)
        l1 = eq(r'x=0', 39, TEAL).move_to((-1.85, 2.23, 0))
        l2 = eq(r'y=0+1=1', 34).move_to((-1.85, 1.47, 0))
        r1 = eq(r'x=3', 39, GOLD).move_to((1.85, 2.23, 0))
        r2 = eq(r'y=3+1=4', 34).move_to((1.85, 1.47, 0))
        ans = eq(r'\boxed{(0,1)\quad\text{and}\quad(3,4)}', 42, GREEN)
        ans.move_to((0, -.58, 0))
        check = eq(r'0^2-2(0)+1=1\quad;\quad3^2-2(3)+1=4', 31)
        check.move_to((0, -2.13, 0))
        self.play(FadeIn(left), FadeIn(right), Write(l1), Write(r1), run_time=.7)
        self.play(Write(l2), Write(r2), run_time=.8)
        self.play(Write(ans), Write(check), run_time=1.1)
        self.note('把每个有序数对代回两个原方程检查。', -3.7)
        checkpoint(self, answers=ans, equality=check, first=l1, second=r1)
        self.wait(1.7)
        self.wipe()

    def sweep(self):
        self.heading('平移直线：为什么有时不是两个解？', 'Secant, tangent or no real intersection')
        ax = self.main_axes()
        curve = ax.plot(lambda x: float(MAIN_CURVE.at(x)),
                        x_range=[-.75, 3.75, .025], color=TEAL, stroke_width=4)
        intercept = ValueTracker(1.)
        moving_line = always_redraw(lambda: ax.plot(
            lambda x: x + intercept.get_value(), x_range=[-.75, 3.75, .025],
            color=GOLD, stroke_width=4))
        moving_points = always_redraw(lambda: VGroup(*[
            Dot(ax.c2p(float(x), float(y)), radius=.075, color=GREEN)
            for x, y in intersections(MAIN_CURVE,
                type(MAIN_LINE)(MAIN_LINE.m, intercept.get_value()))]))
        self.play(Create(ax), Create(curve), run_time=.8)
        self.add(moving_line, moving_points)
        cases = [(1.0, r'k=1,\ \Delta=9:\ 2\ \text{points}', 2),
                 (-1.25, r'k=-\frac54,\ \Delta=0:\ 1\ \text{point}', 1),
                 (-2.0, r'k=-2,\ \Delta=-3:\ 0\ \text{points}', 0)]
        label = None
        for idx, (k, latex, expected) in enumerate(cases):
            assert len(intersections(MAIN_CURVE, type(MAIN_LINE)(1, k))) == expected
            if idx:
                self.play(intercept.animate.set_value(k), run_time=1.65)
            current = eq(latex, 30, GREEN if expected else PINK)
            current.move_to((0, -3.42, 0))
            if label is None:
                self.play(Write(current), run_time=.48)
            else:
                self.play(ReplacementTransform(label, current), run_time=.5)
            label = current
            checkpoint(self, graph=curve, moving_line=moving_line, state=label)
            self.wait(1.05)
        self.note('固定抛物线，改变直线截距：交点数就是实数解数。', -4.75)
        self.wait(1.5)
        self.wipe()

    def circle_example(self):
        self.heading('拓展：二次方程也可以表示圆', 'The same substitution works for a circle')
        ax = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1],
                  x_length=5.22, y_length=5.22, tips=False,
                  axis_config={'color': MUTED, 'include_numbers': True,
                               'font_size': 17, 'stroke_width': 1.2})
        ax.move_to((0, 1.48, 0))
        radius = sqrt(5.)
        circle = ParametricFunction(
            lambda t: ax.c2p(radius*cos(t), radius*sin(t)),
            t_range=[0, TAU, .026], color=TEAL, stroke_width=4)
        line = ax.plot(lambda x: x+1, x_range=[-2.7, 1.7, .025],
                       color=GOLD, stroke_width=4)
        points = circle_line_points(5, MAIN_LINE)
        dots = VGroup(*[Dot(ax.c2p(float(x), float(y)), radius=.075, color=GREEN)
                        for x, y in points])
        e1 = eq(r'x^2+y^2=5,\quad y=x+1', 35)
        e1.move_to((0, -2.25, 0))
        e2 = eq(r'x^2+(x+1)^2=5', 35, TEAL).move_to((0, -3.23, 0))
        e3 = eq(r'\boxed{(-2,-1),\ (1,2)}', 38, GREEN).move_to((0, -4.38, 0))
        self.play(Create(ax), Create(circle), Create(line), run_time=1.15)
        self.play(FadeIn(dots), Write(e1), run_time=.85)
        self.play(Write(e2), Write(e3), run_time=1.2)
        checkpoint(self, axes=ax, circle=circle, line=line, dots=dots, result=e3)
        self.wait(2.1)
        self.wipe()

    def pitfalls(self):
        self.heading('常见错误：只算 x、漏检验或漏掉特殊情形', 'A root is not yet a coordinate pair')
        items = [
            ('先消元，再解二次方程。', r'x^2-3x=0', TEAL),
            ('每个 x 都要代回求对应的 y。', r'x=3\Rightarrow y=4', GOLD),
            ('两个原方程必须同时成立。', r'(3,4):\quad4=3+1', GREEN),
            ('若无法化为 y=mx+k，须改用另一种消元。', r'x=2\ \text{is a vertical line}', PINK),
        ]
        groups = VGroup()
        for i, (zh, latex, color) in enumerate(items):
            y = 3.42-2.04*i
            base = panel(1.66).move_to((0, y, 0))
            top = cn(zh, 24).move_to((0, y+.39, 0))
            bottom = eq(latex, 29, color).move_to((0, y-.33, 0))
            group = VGroup(base, top, bottom)
            self.play(FadeIn(group), run_time=.52)
            groups.add(group)
        checkpoint(self, tips=groups)
        self.wait(2.0)
        self.wipe()

    def practice(self):
        self.heading('试一试：独立完成一组新的联立方程', 'Practice, then reveal the ordered pairs')
        eqs = VGroup(eq(r'y=x^2-2x+2', 40, TEAL),
                     eq(r'y=2x-1', 40, GOLD)).arrange(DOWN, buff=.24)
        eqs.move_to((0, 3.3, 0))
        self.play(Write(eqs), run_time=.83)
        timer = cn('暂停画面：先消元，求 x，再代回求 y。', 25)
        timer.move_to((0, 1.5, 0))
        self.play(FadeIn(timer), run_time=.38)
        self.wait(2.3)
        steps = [r'x^2-4x+3=0', r'(x-1)(x-3)=0',
                 r'\boxed{(x,y)=(1,1)\ \text{or}\ (3,5)}']
        for i, latex in enumerate(steps):
            obj = eq(latex, 40 if i < 2 else 37, GREEN if i == 2 else INK)
            obj.move_to((0, .07-1.35*i, 0))
            self.play(Write(obj), run_time=.85)
            if i == 2:
                checkpoint(self, question=eqs, answer=obj)
            self.wait(.32)
        self.note('总结：联立方程的解是交点坐标，而非仅有 x 的取值。', -4.63)
        self.wait(2.1)
        self.wipe()
