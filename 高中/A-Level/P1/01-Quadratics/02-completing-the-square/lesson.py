"""A-Level P1 §1.2 — Completing the square, original Manim CE lesson.

9:16 logical portrait; silent caption-paced scenes. Manim/LaTeX/CJK font required.
python -m manim render -r 270,480 --fps 15 lesson.py P1CompletingTheSquare
python -m manim render -r 1080,1920 --fps 30 lesson.py P1CompletingTheSquare

The geometric 5x5 picture uses x=2 ONLY. The algebraic identity holds for
all real x. The text does not reproduce Cambridge textbook worked examples.
"""
from manim import *
from math_model import (completed_square, square_completion_tiles,
                        solve_example_via_square, parabola_vertex_and_roots)

config.frame_width = 9
config.frame_height = 16
BG = '#101724'
PANEL = '#1B2A3C'
INK = '#EDF4FC'
MUTED = '#A6BCD3'
TEAL = '#53DCD3'
GOLD = '#FFD06B'
PINK = '#FF8295'
GREEN = '#8BE3AE'
GRID = '#35536D'
FONT = 'Noto Sans CJK SC'  # replace with an installed CJK font if required


def cn(text, size=29, color=INK):
    obj = Text(text, font=FONT, font_size=size, color=color)
    if obj.width > 7.62:
        obj.scale_to_fit_width(7.62)
    return obj


def tex(expr, size=40, color=INK):
    obj = MathTex(expr, font_size=size, color=color)
    if obj.width > 7.62:
        obj.scale_to_fit_width(7.62)
    return obj


def panel(w=7.72, h=2.2):
    return RoundedRectangle(corner_radius=.16, width=w, height=h,
                            fill_color=PANEL, fill_opacity=.95,
                            stroke_color=GRID, stroke_width=1.5)


def checkpoint(scene, **objects):
    """Visible Mobject and portrait-safe-box checks at settled keyframes only."""
    def family(m):
        yield m
        for child in m.submobjects:
            yield from family(child)
    visible = {id(item) for root in scene.mobjects for item in family(root)}
    for name, mob in objects.items():
        # Layout wrappers may contain individually animated visible Mobjects.
        shown = id(mob) in visible or (bool(mob.submobjects) and
                    all(id(child) in visible for child in mob.submobjects))
        if not shown:
            raise AssertionError(f'{name}: not part of the displayed scene')
        if (mob.get_left()[0] < -4.02 or mob.get_right()[0] > 4.02 or
                mob.get_bottom()[1] < -7.02 or mob.get_top()[1] > 7.02):
            raise AssertionError(f'{name}: outside 9:16 title/formula safe bounds')


class P1CompletingTheSquare(Scene):
    """Eight instructional shots, with a persistent A-Level P1 marker."""

    def construct(self):
        self.camera.background_color = BG
        assert completed_square(1, 6, 5) == (1, 3, -4)
        assert completed_square(2, -8, 3) == (2, -2, -5)
        assert solve_example_via_square() == (-5, -1)
        self.chrome()
        self.opening()
        self.algebra_identity()
        self.area_tiles()
        self.complete_and_solve()
        self.parabola()
        self.non_monic()
        self.edge_cases()
        self.practice_and_recap()

    def chrome(self):
        brand = cn('A-Level', 27, BG)
        pill = RoundedRectangle(width=1.78, height=.57, corner_radius=.15,
                                fill_color=TEAL, fill_opacity=1, stroke_width=0)
        brand.move_to(pill)
        course = cn('PURE MATHEMATICS 1  /  P1', 21)
        course.next_to(pill, RIGHT, buff=.16)
        title = VGroup(pill, brand, course).move_to((0, 6.60, 0))
        line = Line((-3.78, 6.15, 0), (3.78, 6.15, 0), color=GRID)
        footer = cn('CHAPTER 1 / 1.2 COMPLETING THE SQUARE', 18, MUTED)
        footer.move_to((0, -6.60, 0))
        self.brand_group = VGroup(title, line, footer)
        self.add(self.brand_group)
        checkpoint(self, header=title, footer=footer)

    def wipe(self):
        elements = [obj for obj in self.mobjects if obj is not self.brand_group]
        if elements:
            self.play(*[FadeOut(obj) for obj in elements], run_time=.38)

    def heading(self, zh, en):
        title = cn(zh, 34).move_to((0, 5.40, 0))
        caption = cn(en, 21, MUTED).move_to((0, 4.85, 0))
        self.play(FadeIn(title, shift=.12 * UP), FadeIn(caption), run_time=.7)
        return title, caption

    def opening(self):
        self.heading('从二次式，找到一个完整的平方', 'Completing the square')
        start = tex(r'x^2+6x+5', 59).move_to((0, 2.55, 0))
        arrow = Arrow((0, 1.72, 0), (0, .85, 0), buff=.05,
                      color=TEAL, stroke_width=4)
        target = tex(r'(x+3)^2-4', 59, GREEN).move_to((0, -.15, 0))
        callout = panel(h=1.65).move_to((0, -2.25, 0))
        explanation = cn('把含 x 的部分合成一个平方', 27).move_to(callout)
        self.play(Write(start), run_time=.9)
        self.play(GrowArrow(arrow), Write(target), run_time=1.2)
        self.play(FadeIn(callout), FadeIn(explanation), run_time=.65)
        checkpoint(self, source=start, answer=target, message=explanation)
        self.wait(1.6)
        self.wipe()

    def algebra_identity(self):
        self.heading('为什么要加 9，再减 9？', 'Reverse the perfect-square expansion')
        identity = tex(r'(x+d)^2=x^2+2dx+d^2', 39).move_to((0, 3.45, 0))
        half = tex(r'2d=6\quad\Rightarrow\quad d=3', 39, GOLD).move_to((0, 1.96, 0))
        steps = [r'x^2+6x+5', r'=x^2+6x+9-9+5', r'=(x+3)^2-4']
        forms = VGroup(*[tex(s, 42, GREEN if i == 2 else INK)
                         for i, s in enumerate(steps)]).arrange(DOWN, buff=.50)
        forms.move_to((0, -.95, 0))
        hint = cn('补上的 9 必须再减去：原式的值不变。', 24, MUTED)
        hint.move_to((0, -4.15, 0))
        self.play(Write(identity), run_time=1.0)
        self.play(Write(half), run_time=.85)
        for item in forms:
            self.play(Write(item), run_time=.75)
        self.play(FadeIn(hint), run_time=.4)
        checkpoint(self, identity=identity, completed=forms, hint=hint)
        self.wait(1.5)
        self.wipe()

    def area_tiles(self):
        self.heading('用 25 个单位方格看见缺失的 4 格', 'Area model: x = 2, half-coefficient = 3')
        data = square_completion_tiles(2, 3, 5)
        assert data['whole'] == 25 and data['corner_missing'] == 4
        side = .74
        origin = (-1.85, -1.80)
        unit = lambda col, row: (origin[0]+(col+.5)*side,
                                 origin[1]+(row+.5)*side, 0)
        cells = VGroup()
        base = VGroup()
        strips = VGroup()
        corner = VGroup()
        missing = VGroup()
        for row in range(5):
            for col in range(5):
                if col < 2 and row < 2:
                    color, category = TEAL, base
                elif col < 2 or row < 2:
                    color, category = GOLD, strips
                else:
                    index = (row-2)*3 + (col-2)
                    color, category = (GREEN, corner) if index < 5 else (GRID, missing)
                sq = Square(side_length=side, stroke_width=1.7,
                            stroke_color=GRID if category is missing else INK,
                            fill_color=color,
                            fill_opacity=.12 if category is missing else .78)
                sq.move_to(unit(col, row))
                category.add(sq)
                cells.add(sq)
        diagram = VGroup(base, strips, corner, missing)
        diagram.move_to((0, .55, 0))
        legend = VGroup(tex(r'x^2=4', 25, TEAL),
                        tex(r'2(3x)=12', 25, GOLD),
                        tex(r'+5', 25, GREEN))
        legend.arrange(RIGHT, buff=.38).move_to((0, 3.10, 0))
        line1 = tex(r'4+6+6+5=21', 39).move_to((0, -3.12, 0))
        line2 = tex(r'21=25-4=5^2-2^2', 38, GREEN).move_to((0, -3.98, 0))
        caption = cn('彩色 21 格 + 空缺 4 格 = 边长 5 的正方形', 23, MUTED)
        caption.move_to((0, -5.10, 0))
        self.play(FadeIn(legend), run_time=.4)
        self.play(FadeIn(base), run_time=.5)
        self.play(FadeIn(strips), run_time=.55)
        self.play(FadeIn(corner), run_time=.55)
        self.play(FadeIn(missing), run_time=.55)
        self.play(Write(line1), Write(line2), run_time=1.1)
        self.play(FadeIn(caption), run_time=.45)
        checkpoint(self, base=base, strips=strips, filled_corner=corner,
                   missing_corner=missing, tile_legend=legend,
                   statement=line2, caption=caption)
        self.wait(1.8)
        self.wipe()

    def complete_and_solve(self):
        self.heading('配方之后，用平方解方程', 'Solve a quadratic by completing the square')
        lines = [r'x^2+6x+5=0', r'(x+3)^2-4=0',
                 r'(x+3)^2=4', r'x+3=\pm2',
                 r'x=-3\pm2', r'\boxed{x=-5\quad\text{or}\quad x=-1}']
        group = VGroup(*[tex(t, 40 if i < 5 else 41,
                                 GREEN if i == 5 else INK)
                         for i, t in enumerate(lines)]).arrange(DOWN, buff=.33)
        group.move_to((0, -.16, 0))
        tip = cn('开平方时保留正、负两种可能。', 25, GOLD).move_to((0, -4.47, 0))
        for line in group:
            self.play(Write(line), run_time=.64)
        self.play(FadeIn(tip), run_time=.35)
        checkpoint(self, steps=group, caution=tip)
        self.wait(1.8)
        self.wipe()

    def parabola(self):
        self.heading('平方形式直接读出顶点与最小值', 'Vertex form and the graph of the quadratic')
        axes = Axes(x_range=[-6, 0, 1], y_range=[-5, 6, 1],
                    x_length=6.9, y_length=4.5, tips=False,
                    axis_config={'color': MUTED, 'stroke_width': 1.5})
        axes.move_to((0, .20, 0))
        curve = axes.plot(lambda x: (x+3)**2-4, x_range=[-6, 0],
                          color=TEAL, stroke_width=4)
        vertex, roots = parabola_vertex_and_roots()
        vertex_dot = Dot(axes.c2p(*vertex), radius=.083, color=GOLD)
        root_dots = VGroup(*[Dot(axes.c2p(x, 0), radius=.075, color=GREEN)
                             for x in roots])
        symmetry = DashedLine(axes.c2p(-3,-5), axes.c2p(-3,6),
                              color=GOLD, dash_length=.12, stroke_width=1.8)
        v_label = tex(r'(-3,-4)', 28, GOLD).next_to(vertex_dot, DOWN, buff=.16)
        l_label = tex(r'-5', 27, GREEN).next_to(root_dots[0], UP, buff=.16)
        r_label = tex(r'-1', 27, GREEN).next_to(root_dots[1], UP, buff=.16)
        form = tex(r'y=(x+3)^2-4', 39, GREEN).move_to((0, -3.28, 0))
        note1 = cn('对称轴 x = -3；在 x = -3 处取得最小值 -4', 23, MUTED)
        note1.move_to((0, -4.30, 0))
        note2 = cn('两个零点正是方程的两个实数解。', 23)
        note2.move_to((0, -5.22, 0))
        self.play(Create(axes), run_time=.7)
        self.play(Create(curve), run_time=1.35)
        self.play(Create(symmetry), FadeIn(vertex_dot), FadeIn(v_label), run_time=.8)
        self.play(FadeIn(root_dots), FadeIn(l_label), FadeIn(r_label), run_time=.75)
        self.play(Write(form), FadeIn(note1), FadeIn(note2), run_time=1.05)
        checkpoint(self, axes=axes, graph=curve, vertex=v_label,
                   roots=root_dots, formula=form, meaning=note1)
        self.wait(1.9)
        self.wipe()

    def non_monic(self):
        self.heading('首项系数不是 1？先提取公因子', 'When a is not 1, factor it out first')
        eqs = [r'2x^2-8x+3', r'=2(x^2-4x)+3',
               r'=2\big[(x-2)^2-4\big]+3',
               r'=2(x-2)^2-5']
        rows = VGroup(*[tex(t, 42, GREEN if i == 3 else INK) for i,t in enumerate(eqs)])
        rows.arrange(DOWN, buff=.55).move_to((0, 1.07, 0))
        warning = panel(h=1.8).move_to((0, -3.26, 0))
        tip = cn('括号里的 -4，也要乘外面的 2。', 25, GOLD).move_to(warning)
        for row in rows:
            self.play(Write(row), run_time=.85)
        self.play(FadeIn(warning), FadeIn(tip), run_time=.65)
        checkpoint(self, calculation=rows, reminder=tip)
        self.wait(1.6)
        self.wipe()

    def edge_cases(self):
        self.heading('平方能告诉我们根是否存在', 'Real roots and the sign of the coefficient')
        p1 = panel(w=7.7, h=2.15).move_to((0, 2.12, 0))
        no_real = tex(r'x^2+2x+5=(x+1)^2+4>0', 35, PINK).move_to(p1)
        p2 = panel(w=7.7, h=2.10).move_to((0, -1.07, 0))
        negative = tex(r'-(x-1)^2+4\leq 4', 43, GOLD).move_to(p2)
        notes = VGroup(cn('第一式不可能等于 0：没有实数根。', 24),
                       cn('第二式在 x = 1 处取得最大值 4。', 24))
        notes[0].move_to((0,.45,0))
        notes[1].move_to((0,-2.76,0))
        self.play(FadeIn(p1), Write(no_real), run_time=.9)
        self.play(FadeIn(notes[0]), run_time=.4)
        self.play(FadeIn(p2), Write(negative), run_time=.9)
        self.play(FadeIn(notes[1]), run_time=.4)
        checkpoint(self, no_real_roots=no_real, maximum=negative, notes=notes)
        self.wait(1.5)
        self.wipe()

    def practice_and_recap(self):
        self.heading('试一试：完成一次独立配方', 'Pause and complete the square yourself')
        q = tex(r'x^2-4x-1=0', 53).move_to((0, 3.15, 0))
        prompt = cn('先取 -4 的一半，再平方补回。', 27, MUTED)
        prompt.move_to((0, 2.16, 0))
        self.play(Write(q), FadeIn(prompt), run_time=1.0)
        self.wait(2.0)
        steps = VGroup(tex(r'(x-2)^2-5=0', 43),
                       tex(r'(x-2)^2=5', 43),
                       tex(r'\boxed{x=2\pm\sqrt5}', 46, GREEN))
        steps.arrange(DOWN, buff=.57).move_to((0, -.77, 0))
        for s in steps:
            self.play(Write(s), run_time=.75)
        tip = cn('复盘：取半 → 平方 → 同加同减 → 解方程', 23, GOLD)
        tip.move_to((0, -4.70, 0))
        self.play(FadeIn(tip), run_time=.45)
        checkpoint(self, exercise=q, solution=steps, summary=tip)
        self.wait(2.0)
