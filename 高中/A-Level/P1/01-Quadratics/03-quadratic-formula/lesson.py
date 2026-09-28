"""A-Level P1 §1.3 — The quadratic formula, original silent Manim CE lesson.

Portrait 9:16. Use `Text` for CJK and `MathTex` for mathematics.
    python -m manim render -r 270,480 --fps 15 lesson.py P1QuadraticFormula
    python -m manim render -r 1080,1920 --fps 30 lesson.py P1QuadraticFormula

Model: `math_model.py`. Geometric tiling uses x=d=2 as an illustration ONLY.
It does not prove the general algebraic identity for all real x.
"""
from math import sqrt
from manim import *
from math_model import EXAMPLE, PRACTICE, Quadratic, area_square_model, discriminant_family

config.frame_width = 9
config.frame_height = 16
BG = '#101724'
PANEL = '#1A2A3E'
INK = '#F0F5FC'
MUTED = '#AFC2D5'
TEAL = '#55DCD0'
GOLD = '#FFD36B'
PINK = '#FF8C9A'
GREEN = '#92E5B5'
GRID = '#36536A'
FONT = 'Noto Sans CJK SC'  # replace with locally installed CJK font if needed


def cn(text, size=29, color=INK):
    m = Text(text, font=FONT, font_size=size, color=color)
    if m.width > 7.55:
        m.scale_to_fit_width(7.55)
    return m


def eq(latex, size=40, color=INK):
    m = MathTex(latex, font_size=size, color=color)
    if m.width > 7.55:
        m.scale_to_fit_width(7.55)
    return m


def card(width=7.65, height=1.6):
    return RoundedRectangle(width=width, height=height, corner_radius=.15,
                            fill_color=PANEL, fill_opacity=.95,
                            stroke_color=GRID, stroke_width=1.5)


def checkpoint(scene, **objects):
    """Registered real Mobject identity + conservative bbox at this instant only."""
    def family(m):
        yield m
        for child in m.submobjects:
            yield from family(child)
    visible = {id(m) for root in scene.mobjects for m in family(root)}
    for name, mob in objects.items():
        if id(mob) not in visible and not (mob.submobjects and
                all(id(child) in visible for child in mob.submobjects)):
            raise AssertionError(f'{name}: not visible in scene family')
        if (mob.get_left()[0] < -4.03 or mob.get_right()[0] > 4.03 or
                mob.get_bottom()[1] < -7.03 or mob.get_top()[1] > 7.03):
            raise AssertionError(f'{name}: outside portrait safe zone')


class P1QuadraticFormula(Scene):
    """Nine shots: from completing square to general formula, graph and practice."""

    def construct(self):
        self.camera.background_color = BG
        assert EXAMPLE.delta == 12 and EXAMPLE.axis == .5
        assert PRACTICE.delta == 28
        self.chrome()
        self.hook()
        self.square_recap()
        self.area_visual()
        self.derive_formula()
        self.worked_example()
        self.parabola_roots()
        self.discriminant_visual()
        self.precision_and_boundaries()
        self.practice_and_summary()

    def chrome(self):
        pill = RoundedRectangle(width=1.79, height=.55, corner_radius=.13,
                                fill_color=TEAL, fill_opacity=1, stroke_width=0)
        name = cn('A-Level', 26, BG).move_to(pill)
        course = cn('PURE MATHEMATICS 1 / P1', 19).next_to(pill, RIGHT, buff=.18)
        header = VGroup(pill, name, course).move_to((0, 6.58, 0))
        rule = Line((-3.82, 6.12, 0), (3.82, 6.12, 0), color=GRID)
        footer = cn('CHAPTER 1  /  1.3 THE QUADRATIC FORMULA', 18, MUTED)
        footer.move_to((0, -6.62, 0))
        self.chrome_mobs = VGroup(header, rule, footer)
        self.add(self.chrome_mobs)
        checkpoint(self, header=header, footer=footer)

    def wipe(self):
        moving = [m for m in self.mobjects if m is not self.chrome_mobs]
        if moving:
            self.play(*[FadeOut(m) for m in moving], run_time=.48)

    def heading(self, zh, en):
        h = cn(zh, 34).move_to((0, 5.40, 0))
        s = cn(en, 21, MUTED).move_to((0, 4.86, 0))
        self.play(FadeIn(h, shift=.12*UP), FadeIn(s), run_time=.6)
        return h, s

    def hook(self):
        self.heading('每个二次方程，都能因式分解吗？', 'From factorisation to a universal formula')
        old = eq(r'(x-2)(x-3)=0', 52).move_to((0, 2.68, 0))
        fresh = eq(r'2x^2-2x-1=0', 54, GOLD).move_to((0, .9, 0))
        arrow = Arrow((0, 2.07, 0), (0, 1.49, 0), color=TEAL, buff=.05)
        frame = card(height=1.6).move_to((0, -2.1, 0))
        text = cn('配方法能推导出对所有 a ≠ 0 通用的求根公式', 24)
        text.move_to(frame)
        self.play(Write(old), run_time=.85)
        self.play(GrowArrow(arrow), Write(fresh), run_time=1.05)
        self.play(FadeIn(frame), FadeIn(text), run_time=.6)
        checkpoint(self, old=old, new=fresh, note=text)
        self.wait(1.9)
        self.wipe()

    def square_recap(self):
        self.heading('回顾 1.2：如何补成一个完整的平方', 'Complete the square before solving')
        rows = [
            eq(r'x^2+2dx+d^2=(x+d)^2', 37, TEAL),
            eq(r'x^2+2dx=(x+d)^2-d^2', 39),
            eq(r'x^2+4x=(x+2)^2-4', 43, GREEN),
        ]
        positions = [3.30, 1.95, .57]
        for mob, y in zip(rows, positions):
            mob.move_to((0, y, 0))
            self.play(Write(mob), run_time=.88)
        box = card(height=1.6).move_to((0, -2.25, 0))
        note = cn('先补平方，再保持原式的值不变。', 28).move_to(box)
        self.play(FadeIn(box), FadeIn(note), run_time=.55)
        checkpoint(self, identities=VGroup(*rows), note=note)
        self.wait(1.6)
        self.wipe()

    def area_visual(self):
        self.heading('几何直观：补上角落里的四个小方格', 'A numerical area model: x = 2, d = 2')
        data = area_square_model(2, 2)
        assert (data['base'], data['strips'], data['corner'], data['whole']) == (4, 8, 4, 16)
        side = .92
        groups = {'base': VGroup(), 'strips': VGroup(), 'corner': VGroup()}
        for row in range(4):
            for col in range(4):
                kind = ('base' if col < 2 and row < 2 else
                        'corner' if col >= 2 and row >= 2 else 'strips')
                color = {'base': TEAL, 'strips': GOLD, 'corner': GREEN}[kind]
                sq = Square(side_length=side, stroke_color=GRID,
                            stroke_width=1.7, fill_color=color, fill_opacity=.83)
                sq.move_to(((col-1.5)*side, .60+(row-1.5)*side, 0))
                groups[kind].add(sq)
        base, strips, corner = (groups[k] for k in ('base', 'strips', 'corner'))
        labels = VGroup(eq(r'x^2=4', 28, TEAL), eq(r'2dx=8', 28, GOLD),
                        eq(r'd^2=4', 28, GREEN)).arrange(RIGHT, buff=.32)
        labels.move_to((0, 3.48, 0))
        count = eq(r'4+8+4=16=(2+2)^2', 40).move_to((0, -2.78, 0))
        note = cn('彩色面积是一次数值示例；通用恒等式由代数展开保证。', 23, MUTED)
        note.move_to((0, -4.10, 0))
        self.play(FadeIn(labels), FadeIn(base), run_time=.8)
        self.play(FadeIn(strips), run_time=.7)
        self.play(FadeIn(corner), run_time=.7)
        self.play(Write(count), FadeIn(note), run_time=1.0)
        checkpoint(self, cells=VGroup(base, strips, corner), labels=labels,
                   area=count, caveat=note)
        self.wait(2)
        self.wipe()

    def derive_formula(self):
        self.heading('用配方法推导一般求根公式', 'General derivation, assuming a is nonzero')
        steps = [
            (r'ax^2+bx+c=0\qquad(a\ne0)', INK),
            (r'x^2+\frac ba x=-\frac ca', INK),
            (r'\left(x+\frac{b}{2a}\right)^2=\frac{b^2-4ac}{4a^2}', TEAL),
            (r'x+\frac{b}{2a}=\pm\frac{\sqrt{b^2-4ac}}{2a}', GOLD),
            (r'\boxed{x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}}', GREEN),
        ]
        formulae = VGroup()
        for i, (latex, color) in enumerate(steps):
            f = eq(latex, 37 if i < 4 else 41, color)
            f.move_to((0, 3.75 - i*1.57, 0))
            formulae.add(f)
            self.play(Write(f), run_time=1.05)
            self.wait(.55)
        note = cn('实数求根时，根号内必须非负；± 表示两种符号。', 23, MUTED)
        note.move_to((0, -4.63, 0))
        self.play(FadeIn(note), run_time=.45)
        checkpoint(self, derivation=formulae, condition=note)
        self.wait(2.1)
        self.wipe()

    def worked_example(self):
        self.heading('例题：识别 a、b、c 并逐项代入', 'An original non-integer-root example')
        source = eq(r'2x^2-2x-1=0', 51).move_to((0, 3.75, 0))
        coeffs = eq(r'a=2,\quad b=-2,\quad c=-1', 36, GOLD).move_to((0, 2.55, 0))
        d = eq(r'\Delta=b^2-4ac=4+8=12', 39, TEAL).move_to((0, 1.25, 0))
        raw = eq(r'x=\frac{2\pm\sqrt{12}}{4}', 48).move_to((0, -.25, 0))
        simplified = eq(r'\boxed{x=\frac{1\pm\sqrt{3}}{2}}', 49, GREEN)
        simplified.move_to((0, -2.03, 0))
        note = cn('代入时特别注意 b = −2 和 c = −1 的负号。', 24, MUTED)
        note.move_to((0, -4.20, 0))
        for mob in (source, coeffs, d, raw, simplified):
            self.play(Write(mob), run_time=.85)
        self.play(FadeIn(note), run_time=.38)
        checkpoint(self, original=source, coefficients=coeffs, delta=d,
                   substitution=raw, exact_answer=simplified, note=note)
        self.wait(2.0)
        self.wipe()

    def parabola_roots(self):
        self.heading('两个代数解，就是抛物线的两个零点', 'Exact algebra and geometric intersections agree')
        axes = Axes(x_range=[-1, 2, .5], y_range=[-2, 3, 1],
                    x_length=6.52, y_length=4.25, tips=False,
                    axis_config={'color': MUTED, 'include_numbers': True,
                                 'font_size': 18, 'stroke_width': 1.3})
        axes.move_to((0, .87, 0))
        graph = axes.plot(lambda x: 2*x*x-2*x-1,
                          x_range=[-.85, 1.85, .025], color=TEAL, stroke_width=5)
        low, high = EXAMPLE.real_roots()
        root_dots = VGroup(Dot(axes.c2p(low, 0), color=GOLD, radius=.085),
                           Dot(axes.c2p(high, 0), color=GOLD, radius=.085))
        vertex = Dot(axes.c2p(.5, -1.5), color=PINK, radius=.075)
        axis = DashedLine(axes.c2p(.5, -2), axes.c2p(.5, 2.6),
                          color=PINK, dash_length=.12, stroke_width=2)
        label = eq(r'\left(\frac12,-\frac32\right)', 27, PINK)
        label.move_to(axes.c2p(1.04, -1.54))
        root_note = eq(r'x_1=\frac{1-\sqrt3}{2},\qquad x_2=\frac{1+\sqrt3}{2}',
                       36, GREEN).move_to((0, -3.75, 0))
        expl = cn('顶点对称轴是 x = 1/2；两零点在对称轴两侧。', 23, MUTED)
        expl.move_to((0, -4.80, 0))
        self.play(Create(axes), Create(graph), run_time=1.5)
        self.play(Create(axis), FadeIn(vertex), FadeIn(label), run_time=.85)
        self.play(FadeIn(root_dots), Write(root_note), run_time=1.1)
        self.play(FadeIn(expl), run_time=.48)
        checkpoint(self, axes=axes, parabola=graph, zeros=root_dots,
                   vertex=vertex, symmetry=axis, answer=root_note)
        self.wait(2)
        self.wipe()

    def discriminant_visual(self):
        self.heading('判别式控制抛物线与 x 轴相交的次数', 'Discriminant = b² − 4ac')
        axes = Axes(x_range=[-.5, 2.5, .5], y_range=[-2, 3.5, 1],
                    x_length=6.45, y_length=4.14, tips=False,
                    axis_config={'color': MUTED, 'include_numbers': True,
                                 'font_size': 17, 'stroke_width': 1.3})
        axes.move_to((0, .90, 0))
        k = ValueTracker(1.)
        graph = always_redraw(lambda: axes.plot(
            lambda x: (x-1)**2 - k.get_value(), x_range=[-.48, 2.48, .03],
            color=TEAL, stroke_width=4.5))
        def current_dots():
            kval = k.get_value()
            if kval < -1e-5:
                return VGroup()
            xvalues = ([1-sqrt(kval), 1+sqrt(kval)] if kval > 1e-5
                       else [1.])
            return VGroup(*[Dot(axes.c2p(x, 0), color=GOLD, radius=.083)
                            for x in xvalues])
        dots = always_redraw(current_dots)
        statement = eq(r'k=1,\quad\Delta=4>0:\quad 2\ \mathrm{roots}', 32, GREEN)
        statement.move_to((0, -3.42, 0))
        footer = cn('当 a = 1, b = −2, c = 1 − k 时，判别式 Δ = 4k', 21, MUTED)
        footer.move_to((0, -4.54, 0))
        self.play(Create(axes), FadeIn(graph), FadeIn(dots), run_time=1.25)
        self.play(Write(statement), FadeIn(footer), run_time=.75)
        checkpoint(self, axes=axes, moving_curve=graph, moving_roots=dots,
                   status=statement, family_rule=footer)
        self.wait(1.2)
        self.play(k.animate.set_value(0), run_time=1.9)
        state0 = eq(r'k=0,\quad\Delta=0:\quad 1\ \mathrm{double\ root}', 30, GOLD)
        state0.move_to(statement)
        self.play(Transform(statement, state0), run_time=.55)
        assert discriminant_family(0).real_root_count == 1
        checkpoint(self, axes=axes, tangent_curve=graph, tangent_root=dots, status=statement)
        self.wait(1.2)
        self.play(k.animate.set_value(-1), run_time=1.85)
        state1 = eq(r'k=-1,\quad\Delta=-4<0:\quad 0\ \mathrm{real\ roots}', 30, PINK)
        state1.move_to(statement)
        self.play(Transform(statement, state1), run_time=.55)
        assert discriminant_family(-1).real_root_count == 0
        checkpoint(self, axes=axes, no_real_curve=graph, status=statement)
        self.wait(1.6)
        self.wipe()

    def precision_and_boundaries(self):
        self.heading('精确值、有效数字与适用条件', 'Exact radicals, 3 significant figures, a ≠ 0')
        exact = eq(r'x=\frac{1\pm\sqrt3}{2}', 47, GREEN).move_to((0, 3.26, 0))
        approx = eq(r'x\approx 1.37\ \mathrm{or}\ -0.366\quad (3\ \mathrm{s.f.})',
                    37, GOLD).move_to((0, 1.86, 0))
        self.play(Write(exact), Write(approx), run_time=1.35)
        conditions = [
            (r'a\ne 0', '否则方程不再是二次方程'),
            (r'\Delta\ge 0', '这是存在实数根的条件'),
            (r'\pm', '求根时两个符号都要考虑'),
        ]
        cards = VGroup()
        for i, (latex, text) in enumerate(conditions):
            bg = card(height=.93)
            m = eq(latex, 30, (TEAL, GOLD, PINK)[i])
            label = cn(text, 22)
            row = VGroup(m, label).arrange(RIGHT, buff=.36)
            row.move_to(bg)
            grouped = VGroup(bg, row)
            grouped.move_to((0, .12-1.25*i, 0))
            cards.add(grouped)
            self.play(FadeIn(grouped), run_time=.55)
        checkpoint(self, exact=exact, approx=approx, cautions=cards)
        self.wait(1.8)
        self.wipe()

    def practice_and_summary(self):
        self.heading('课堂练习：独立代入，然后核对答案', 'Try: 3x² + 2x − 2 = 0')
        problem = eq(r'3x^2+2x-2=0', 51).move_to((0, 3.62, 0))
        prompt = cn('先暂停视频，计算 a、b、c 与判别式。', 24, MUTED)
        prompt.move_to((0, 2.63, 0))
        self.play(Write(problem), FadeIn(prompt), run_time=.85)
        self.wait(3)
        d = eq(r'\Delta=2^2-4(3)(-2)=28', 39, TEAL).move_to((0, 1.25, 0))
        work = eq(r'x=\frac{-2\pm\sqrt{28}}6', 42).move_to((0, -.25, 0))
        answer = eq(r'\boxed{x=\frac{-1\pm\sqrt7}{3}}', 47, GREEN)
        answer.move_to((0, -1.84, 0))
        summary = card(height=1.35).move_to((0, -4.12, 0))
        message = cn('化为标准式 → 认清符号 → 计算 Δ → 代入并化简', 23)
        message.move_to(summary)
        for mob in (d, work, answer):
            self.play(Write(mob), run_time=.92)
        self.play(FadeIn(summary), FadeIn(message), run_time=.6)
        checkpoint(self, practice=problem, discriminant=d, working=work,
                   answer=answer, conclusion=message)
        self.wait(2.4)
