"""精确演示三等分换边、每代新增的正三角形及周长/面积递推。

Render: manim external/interesting-math/koch-snowflake/scene.py KochSnowflakeScene
"""
from math import cos, pi, sin, sqrt
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
FONT = "Noto Sans CJK SC"
BACKGROUND = "#101827"


def initial_triangle():
    """逆时针顶点；每条有向边的右侧为雪花外侧。"""
    return [complex(cos(pi/2 + 2*pi*k/3), sin(pi/2 + 2*pi*k/3))
            for k in range(3)]


def koch_step(points):
    if len(points) < 3:
        raise ValueError("expected a closed polygon with at least three vertices")
    result = []
    outward = complex(0.5, -sqrt(3)/2)
    for idx, start in enumerate(points):
        end = points[(idx+1) % len(points)]
        segment = (end-start)/3
        result.extend((start, start+segment,
                       start+segment+segment*outward,
                       start+2*segment))
    return result


def added_triangles(points):
    """每条旧边新增的真实等边三角形顶点（共享新轮廓的顶点）。"""
    if len(points) < 3:
        raise ValueError("expected a closed polygon with at least three vertices")
    outward = complex(0.5, -sqrt(3)/2)
    triangles = []
    for idx, start in enumerate(points):
        seg = (points[(idx+1) % len(points)] - start)/3
        left = start+seg
        triangles.append((left, left+seg*outward, start+2*seg))
    return triangles


def perimeter_ratio(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return (4/3)**n


def area_ratio(n):
    """第 n 代面积 / 初始正三角形面积。"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return 1 + sum((1/3)*(4/9)**j for j in range(n))


class KochSnowflakeScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        self.add(Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                      font_size=17, color=GREY_B).move_to(UP * 7))
        title = Text("无限周长，有限面积？", font=FONT,
                     font_size=35).move_to(UP * 6.3)
        lead = Text("先看一条边：三等分，中段向外搭等边三角形",
                    font=FONT, font_size=23).move_to(UP * 5.25)

        # The inset uses an actual equilateral bump: height = sqrt(3)/2 * base.
        y = 3.65
        a, b, c, d = (np.array([x, y, 0]) for x in (-1.5, -0.5, 0.5, 1.5))
        peak = np.array([0, y+sqrt(3)/2, 0])
        thirds = VGroup(*[Dot(p, radius=0.055, color=WHITE)
                          for p in (a, b, c, d)])
        old_middle = DashedLine(b, c, color=GREY_B)
        replacement = VGroup(Line(a, b, color=TEAL_C, stroke_width=4),
                             Line(b, peak, color=YELLOW, stroke_width=4),
                             Line(peak, c, color=YELLOW, stroke_width=4),
                             Line(c, d, color=TEAL_C, stroke_width=4))
        local_area = Polygon(b, peak, c, color=YELLOW,
                             fill_color=YELLOW, fill_opacity=0.22,
                             stroke_width=0)
        self.play(Write(title), FadeIn(lead), FadeIn(thirds),
                  Create(Line(a, d, color=GREY_B)))
        self.play(Create(old_middle), FadeIn(local_area), Create(replacement))
        self.wait(0.5)

        def to_scene(z):
            return np.array([2.32*z.real, 2.32*z.imag+0.35, 0])

        def outline(vertices):
            coords = [to_scene(z) for z in vertices]
            return VMobject().set_points_as_corners(coords+[coords[0]]).set_stroke(
                color=TEAL_C, width=3)

        points = initial_triangle()
        snowflake = outline(points)
        iteration = Text("第 0 次：3 条边", font=FONT,
                         font_size=26).move_to(DOWN*3.35)
        perimeter = MathTex(r"P_n/P_0=(4/3)^n", font_size=33).move_to(DOWN*4.25)
        area_name = MathTex(r"A_n/A_0\approx", font_size=34).move_to([-0.65,-5.15,0])
        area_value = DecimalNumber(1, num_decimal_places=3,
                                   font_size=33, color=YELLOW).next_to(area_name, RIGHT)
        self.play(Create(snowflake), FadeIn(iteration), Write(perimeter),
                  Write(area_name), FadeIn(area_value))
        for n in range(1, 5):
            previous = points
            points = koch_step(previous)
            next_label = Text(f"第 {n} 次：{len(points)} 条边", font=FONT,
                              font_size=26).move_to(DOWN*3.35)
            # Highlight actual newly added regions only for readable early levels.
            bumps = VGroup()
            if n <= 3:
                bumps = VGroup(*[
                    Polygon(*[to_scene(vertex) for vertex in triangle],
                            color=YELLOW, fill_color=YELLOW,
                            fill_opacity=0.28, stroke_width=0.8)
                    for triangle in added_triangles(previous)
                ])
            animations = [Transform(snowflake, outline(points)),
                          Transform(iteration, next_label),
                          area_value.animate.set_value(area_ratio(n))]
            if n <= 3:
                animations.append(FadeIn(bumps))
            self.play(*animations, run_time=1.9)
            self.wait(0.45)
            if n <= 3:
                self.play(FadeOut(bumps), run_time=0.3)
        result = MathTex(r"P_n\to\infty,\quad A_n\to\frac85 A_0",
                         font_size=39, color=YELLOW).move_to(DOWN*6.3)
        self.play(Write(result))
        self.wait(2)
