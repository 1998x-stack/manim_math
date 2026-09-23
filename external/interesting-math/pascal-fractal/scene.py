"""先用双亲连线展示杨辉三角递推，再以奇偶三角形展示有限自相似。

Render: manim external/interesting-math/pascal-fractal/scene.py PascalFractalScene
"""
from math import comb
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
FONT = "Noto Sans CJK SC"
BACKGROUND = "#101827"


def pascal_row(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return [comb(n, k) for k in range(n + 1)]


def parity_row(n):
    return [value % 2 for value in pascal_row(n)]


class PascalFractalScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        self.add(Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                      font_size=17, color=GREY_B).move_to(UP * 7))
        title = Text("杨辉三角形里有分形？", font=FONT,
                     font_size=35).move_to(UP * 6.3)
        lead = Text("每个内部数字，等于正上方两个数字的和", font=FONT,
                    font_size=24).move_to(UP * 5.15)
        self.play(Write(title), FadeIn(lead))

        # Explicit parent-to-child construction: the 2 has two visible 1 parents.
        numbers = VGroup()
        centers = {}
        for n in range(5):
            for k, value in enumerate(pascal_row(n)):
                point = np.array([(k-n/2)*1.05, 4.1-n*0.72, 0])
                centers[(n, k)] = point
                badge = Circle(radius=0.27, color=TEAL_C if value % 2 else GREY_B,
                               stroke_width=2, fill_color=BACKGROUND,
                               fill_opacity=1).move_to(point)
                numeral = MathTex(str(value), font_size=28,
                                  color=WHITE if value % 2 else GREY_B).move_to(point)
                numbers.add(VGroup(badge, numeral))
        links = VGroup()
        for n in range(2, 5):
            for k in range(1, n):
                for parent in (k-1, k):
                    links.add(Line(centers[(n-1, parent)], centers[(n, k)],
                                   color=BLUE_D, stroke_width=2))
        self.play(Create(links), LaggedStart(*[FadeIn(node) for node in numbers],
                                                   lag_ratio=0.05), run_time=2.2)
        parent_formula = MathTex(r"1+1=2\quad\Rightarrow\quad 2\equiv0\pmod2",
                                 font_size=34).move_to(DOWN*0.15)
        self.play(Write(parent_formula))
        self.wait(0.6)
        self.play(FadeOut(numbers), FadeOut(links), FadeOut(parent_formula),
                  Transform(lead, Text("把奇数画成亮三角形，偶数画成暗三角形",
                                       font=FONT, font_size=24).move_to(UP*5.15)))

        # A fixed grid keeps old rows in place and makes the 16/32-row nesting visible.
        rows = []
        for n in range(32):
            cells = VGroup(*[
                RegularPolygon(n=3, radius=0.088, color=TEAL_C if odd else GREY_D,
                               stroke_width=0,
                               fill_color=TEAL_C if odd else GREY_D,
                               fill_opacity=1 if odd else 0.28)
                .move_to(np.array([(k-n/2)*0.20, 4.10-n*0.20, 0]))
                for k, odd in enumerate(parity_row(n))
            ])
            rows.append(cells)
        stage = Text("前 8 行", font=FONT, font_size=25).move_to(DOWN*3.0)
        self.play(FadeIn(stage), LaggedStart(*[FadeIn(r) for r in rows[:8]],
                                             lag_ratio=0.11), run_time=1.8)
        for first, last, text in ((8, 16, "前 16 行"), (16, 32, "前 32 行")):
            self.play(FadeIn(VGroup(*rows[first:last])),
                      Transform(stage, Text(text, font=FONT,
                                            font_size=25).move_to(DOWN*3.0)),
                      run_time=1.6)
            self.wait(0.3)

        # At power-of-two row boundaries, the nonzero mod-2 entries form
        # three translated copies of the previous 16-row pattern.
        outlines = VGroup(
            Polygon([0, 4.10, 0], [-1.5, 1.10, 0], [1.5, 1.10, 0],
                    color=YELLOW, stroke_width=2, fill_opacity=0),
            Polygon([-1.6, 0.90, 0], [-3.1, -2.10, 0], [-0.1, -2.10, 0],
                    color=YELLOW, stroke_width=2, fill_opacity=0),
            Polygon([1.6, 0.90, 0], [0.1, -2.10, 0], [3.1, -2.10, 0],
                    color=YELLOW, stroke_width=2, fill_opacity=0),
        )
        explanation = Text("三个缩小的奇偶图案，组成更大的三角形",
                           font=FONT, font_size=24, color=YELLOW).move_to(DOWN*4.25)
        recurrence = MathTex(r"\binom nk\equiv\binom{n-1}{k-1}+\binom{n-1}{k}\pmod2",
                             font_size=30).move_to(DOWN*5.35)
        self.play(Create(outlines), FadeIn(explanation), Write(recurrence),
                  run_time=2)
        self.wait(2)
