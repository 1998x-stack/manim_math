"""Original 9:16 Manim CE lesson: A-Level P1 §1.5, quadratic in g(x).

Render: python -m manim render -r 270,480 --fps 15 lesson.py P1ComplexQuadratics
Requires Manim Community, LaTeX and an installed CJK font.
Model and all numerical example values are in math_model.py.
"""
from math import sqrt
from manim import *
from math_model import MAIN_T, MAIN_X, SURD_X, POWER_X, CHALLENGE_X, evaluate_transformed, preimages

config.frame_width, config.frame_height = 9, 16
BG, CARD, GRID = '#101724', '#1A2A3E', '#34516A'
INK, SUB = '#F0F5FC', '#AEC3D6'
TEAL, GOLD, GREEN, PINK = '#55DCD0', '#FFD36B', '#92E5B5', '#FF8C9A'
CJK = 'Noto Sans CJK SC'  # replace with available installed font if needed


def text(s, size=28, color=INK, max_w=7.5):
    m = Text(s, font=CJK, font_size=size, color=color)
    if m.width > max_w:
        m.scale_to_fit_width(max_w)
    return m


def formula(s, size=43, color=INK, max_w=7.5):
    m = MathTex(s, font_size=size, color=color)
    if m.width > max_w:
        m.scale_to_fit_width(max_w)
    return m


def panel(w=7.6, h=1.55):
    return RoundedRectangle(width=w, height=h, corner_radius=.15,
                            fill_color=CARD, fill_opacity=.96, stroke_color=GRID,
                            stroke_width=1.4)


def checkpoint(scene, **objects):
    """Scene-family membership and bbox safety at explicit moments only."""
    def family(obj):
        yield obj
        for child in obj.submobjects:
            yield from family(child)
    current = {id(o) for root in scene.mobjects for o in family(root)}
    for label, mob in objects.items():
        members = list(family(mob))
        if id(mob) not in current and not all(id(c) in current for c in members[1:]):
            raise AssertionError(f'{label}: missing from actual Scene family')
        if (mob.get_left()[0] < -4.05 or mob.get_right()[0] > 4.05 or
            mob.get_top()[1] > 7.05 or mob.get_bottom()[1] < -7.05):
            raise AssertionError(f'{label}: outside conservative safe zone')


class P1ComplexQuadratics(Scene):
    """Nine teaching beats; exact roots and graphic positions share the pure model."""

    def construct(self):
        self.camera.background_color = BG
        assert MAIN_T == (1., 4.) and MAIN_X == (-2., -1., 1., 2.)
        assert SURD_X == (4., 9.) and abs(POWER_X[1]-2) < 1e-10
        assert CHALLENGE_X == (-3., -1., 1., 3.)
        self.chrome()
        self.intro()
        self.substitution_machine()
        self.solve_auxiliary()
        self.inverse_map()
        self.quartic_graph()
        self.radical_case()
        self.exponential_case()
        self.domain_warning()
        self.practice_and_summary()

    def chrome(self):
        badge = RoundedRectangle(width=1.8, height=.54, corner_radius=.13,
                                 fill_color=TEAL, fill_opacity=1, stroke_width=0)
        label = text('A-Level', 25, BG).move_to(badge)
        title = text('PURE MATHEMATICS 1  /  P1', 19)
        title.next_to(badge, RIGHT, buff=.2)
        header = VGroup(badge, label, title).move_to((0, 6.56, 0))
        separator = Line((-3.8, 6.13, 0), (3.8, 6.13, 0), color=GRID)
        footer = text('CHAPTER 1  /  1.5 COMPLEX QUADRATIC EQUATIONS', 17, SUB)
        footer.move_to((0, -6.62, 0))
        self.chrome_mobs = VGroup(header, separator, footer)
        self.add(self.chrome_mobs)
        checkpoint(self, header=header, footer=footer)

    def wipe(self):
        old = [o for o in self.mobjects if o is not self.chrome_mobs]
        if old:
            self.play(*[FadeOut(o) for o in old], run_time=.43)

    def heading(self, zh, en):
        a = text(zh, 34).move_to((0, 5.44, 0))
        b = text(en, 21, SUB).move_to((0, 4.89, 0))
        self.play(FadeIn(a, shift=.10*UP), FadeIn(b), run_time=.55)
        return a, b

    def show_stack(self, lines, colors=None, start=3.0, step=1.23, size=42):
        mobs = []
        for i, line in enumerate(lines):
            item = formula(line, size, (colors[i] if colors else INK)).move_to((0, start-i*step, 0))
            self.play(Write(item), run_time=.75)
            mobs.append(item)
        return VGroup(*mobs)

    def intro(self):
        self.heading('看起来是四次，为什么还能用二次方法？', 'Quadratic in a function of x')
        big = formula(r'x^4-5x^2+4=0', 59, GOLD).move_to((0, 2.65, 0))
        frame = panel(h=1.6).move_to((0, -.05, 0))
        hint = formula(r'x^4=(x^2)^2', 47, TEAL).move_to(frame)
        note = text('把重复出现的结构视作一个新变量。', 28).move_to((0, -2.0, 0))
        self.play(Write(big), run_time=1.1)
        self.play(FadeIn(frame), Write(hint), run_time=.9)
        self.play(FadeIn(note), run_time=.5)
        checkpoint(self, big=big, hint=hint, note=note)
        self.wait(1.5)
        self.wipe()

    def substitution_machine(self):
        self.heading('两层运算：先换元，再回代', 'A two-stage function machine')
        x = formula(r'x', 53, TEAL).move_to((-2.9, 2.35, 0))
        t = formula(r't=x^2', 45, GOLD).move_to((0, 2.35, 0))
        p = formula(r't^2-5t+4', 45, GREEN).move_to((2.6, 2.35, 0))
        ar1 = Arrow((-2.35, 2.35, 0), (-1.21, 2.35, 0), color=TEAL, buff=.08)
        ar2 = Arrow((.88, 2.35, 0), (1.48, 2.35, 0), color=GREEN, buff=.06)
        self.play(FadeIn(x), GrowArrow(ar1), FadeIn(t), run_time=.8)
        self.play(GrowArrow(ar2), FadeIn(p), run_time=.8)
        card = panel(h=2.2).move_to((0, -.75, 0))
        identity = formula(r'(x^2)^2-5(x^2)+4=0', 45).move_to((0, -.55, 0))
        simpler = formula(r't^2-5t+4=0', 46, GOLD).move_to((0, -1.48, 0))
        self.play(FadeIn(card), Write(identity), run_time=.8)
        self.play(Write(simpler), run_time=.8)
        rule = text('换元只改写方程，还必须检查 t 的可取值。', 25, SUB)
        rule.move_to((0, -3.25, 0))
        self.play(FadeIn(rule), run_time=.5)
        checkpoint(self, flow=VGroup(x,t,p), algebra=VGroup(identity,simpler), rule=rule)
        self.wait(1.4)
        self.wipe()

    def solve_auxiliary(self):
        self.heading('第一关：先解关于 t 的二次方程', 'Solve the auxiliary quadratic')
        lines = self.show_stack([
            r't^2-5t+4=0', r'(t-1)(t-4)=0', r't=1\quad\mathrm{or}\quad t=4'
        ], [INK, TEAL, GOLD], start=3.35, step=1.27, size=51)
        rec = panel(h=1.6).move_to((0, -2.18, 0))
        info = formula(r't=x^2\geq 0', 45, GREEN).move_to(rec)
        self.play(FadeIn(rec), Write(info), run_time=.75)
        checkpoint(self, steps=lines, domain=info)
        self.wait(1.5)
        self.wipe()

    def inverse_map(self):
        self.heading('第二关：每个 t 对应哪些 x？', 'The inverse-image diagram for t = x squared')
        number = NumberLine(x_range=[-2.5, 2.5, .5], length=6.85,
                            include_numbers=False, color=SUB).move_to((0, .15, 0))
        labels = VGroup(*[formula(str(k), 26).move_to(number.n2p(k)+.5*DOWN)
                          for k in (-2, -1, 0, 1, 2)])
        central = formula(r't=x^2', 44, TEAL).move_to((0, 3.34, 0))
        value = ValueTracker(1.)
        left = always_redraw(lambda: Dot(number.n2p(-sqrt(value.get_value())), radius=.13, color=PINK))
        right = always_redraw(lambda: Dot(number.n2p(sqrt(value.get_value())), radius=.13, color=GREEN))
        pair_1 = formula(r't=1\ \longrightarrow\ x=\pm1', 40).move_to((0, -2.45, 0))
        pair_4 = formula(r't=4\ \longrightarrow\ x=\pm2', 40, GOLD).move_to((0, -3.42, 0))
        self.play(Write(central), Create(number), FadeIn(labels), run_time=.9)
        self.add(left, right)
        self.play(Write(pair_1), run_time=.8)
        checkpoint(self, line=number, spots=VGroup(left,right), first=pair_1)
        self.play(value.animate.set_value(4.), run_time=1.5)
        self.play(Write(pair_4), run_time=.7)
        checkpoint(self, line=number, spots=VGroup(left,right), second=pair_4)
        self.wait(1.15)
        self.wipe()

    def quartic_graph(self):
        self.heading('图像检验：四个实根 = 四个 x 轴交点', 'Graph the original quartic, not the t-quadratic')
        ax = Axes(x_range=[-2.4, 2.4, 1], y_range=[-3, 5.3, 1],
                  x_length=6.8, y_length=5.75,
                  axis_config={'include_tip': False, 'color': SUB}).move_to((0, -.15, 0))
        f = lambda z: evaluate_transformed(z, 1, -5, 4, 'square')
        curve = ax.plot(f, x_range=[-2.15, 2.15, .02], color=TEAL, stroke_width=4)
        points = VGroup(*[Dot(ax.c2p(x, 0), radius=.095, color=GOLD) for x in MAIN_X])
        root_labels = VGroup(*[formula(s, 25, GOLD).move_to(ax.c2p(x, -.53))
                              for x,s in zip(MAIN_X, ('-2','-1','1','2'))])
        name = formula(r'y=x^4-5x^2+4', 37, TEAL).move_to((0, 3.73, 0))
        conclusion = formula(r'x=-2,-1,1,2', 40, GREEN).move_to((0, -4.20, 0))
        self.play(Create(ax), Write(name), run_time=.85)
        self.play(Create(curve), run_time=2.)
        self.play(FadeIn(points), FadeIn(root_labels), Write(conclusion), run_time=1.05)
        checkpoint(self, graph=VGroup(ax,curve,points,root_labels), equation=name, roots=conclusion)
        self.wait(1.6)
        self.wipe()

    def radical_case(self):
        self.heading('不只 x²：含根式的二次型方程', 'A quadratic in square root of x')
        steps = self.show_stack([
            r'x-5\sqrt{x}+6=0', r't=\sqrt{x}\ \Rightarrow\ t\geq0',
            r't^2-5t+6=0', r'(t-2)(t-3)=0',
            r't=2,3\ \Rightarrow\ x=4,9'
        ], [INK, GOLD, INK, TEAL, GREEN], start=3.52, step=1.14, size=41)
        checkpoint(self, steps=steps)
        self.wait(1.55)
        self.wipe()

    def exponential_case(self):
        self.heading('同一个结构：指数也可以换元', 'A quadratic in 3 to the power of x')
        steps = self.show_stack([
            r'3^{2x}-10\cdot3^x+9=0',
            r't=3^x\ \Rightarrow\ t>0',
            r't^2-10t+9=0',
            r'(t-1)(t-9)=0',
            r'3^x=1,9\ \Rightarrow\ x=0,2'
        ], [INK, GOLD, INK, TEAL, GREEN], start=3.50, step=1.14, size=40)
        checkpoint(self, steps=steps)
        self.wait(1.45)
        self.wipe()

    def domain_warning(self):
        self.heading('关键陷阱：t 的解不一定能回代', 'The range of g(x) matters')
        card1 = panel(h=2.75).move_to((0, 1.38, 0))
        ex = formula(r'x^4-x^2-6=0', 46).move_to((0, 2.25, 0))
        roots = formula(r't^2-t-6=0\Rightarrow t=3,-2', 37, GOLD).move_to((0, 1.32, 0))
        domain = formula(r't=x^2\geq0\Rightarrow t=-2\text{\ is\ invalid}', 33, PINK)
        domain.move_to((0, .37, 0))
        result = formula(r'x=\pm\sqrt3', 49, GREEN).move_to((0, -2.2, 0))
        note = text('零也需要单独检查：若 t=0，则只得到 x=0。', 26, SUB)
        note.move_to((0, -3.60, 0))
        self.play(FadeIn(card1), Write(ex), run_time=.7)
        self.play(Write(roots), Write(domain), run_time=1.3)
        self.play(Write(result), FadeIn(note), run_time=.8)
        checkpoint(self, equation=ex, rejected=domain, answer=result, note=note)
        self.wait(1.5)
        self.wipe()

    def practice_and_summary(self):
        self.heading('独立练习 · 三步形成稳定的方法', 'Try, check, then summarise')
        task = formula(r'x^4-10x^2+9=0', 48, GOLD).move_to((0, 3.25, 0))
        prompt = text('暂停思考：先设 t，再求 t，最后回代 x。', 26).move_to((0, 2.25, 0))
        self.play(Write(task), FadeIn(prompt), run_time=.8)
        self.wait(2.4)
        summary = panel(h=3.4).move_to((0, -.65, 0))
        rows = VGroup(
            formula(r'1.\ t=g(x)', 41, TEAL),
            formula(r'2.\ at^2+bt+c=0', 41, GOLD),
            formula(r'3.\ g(x)=t\ \text{and check the domain}', 33, GREEN),
        ).arrange(DOWN, buff=.65).move_to((0, -.55, 0))
        self.play(FadeIn(summary), run_time=.5)
        for r in rows:
            self.play(Write(r), run_time=.65)
        final = formula(r'\boxed{x=-3,-1,1,3}', 44, GREEN).move_to((0, -4.45, 0))
        self.play(Write(final), run_time=.85)
        checkpoint(self, task=task, rules=rows, answer=final)
        self.wait(2)
