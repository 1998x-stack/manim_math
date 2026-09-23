"""科赫雪花：四次可见递归，解析表达周长发散、面积收敛。

Render: manim -pql external/interesting-math/koch-snowflake/scene.py KochSnowflakeScene
"""
from math import cos, sin, pi, sqrt
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
FONT = "Noto Sans CJK SC"
BACKGROUND = "#101827"


def initial_triangle():
    """逆时针顶点；沿每条有向边向右侧（外侧）作凸起。"""
    return [complex(cos(pi / 2 + 2 * pi * k / 3),
                    sin(pi / 2 + 2 * pi * k / 3)) for k in range(3)]


def koch_step(points):
    if len(points) < 3:
        raise ValueError("expected a closed polygon with at least three vertices")
    result = []
    outward = complex(0.5, -sqrt(3) / 2)
    for idx, start in enumerate(points):
        end = points[(idx + 1) % len(points)]
        segment = (end - start) / 3
        result.extend((start, start + segment,
                       start + segment + segment * outward,
                       start + 2 * segment))
    return result


def perimeter_ratio(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return (4 / 3) ** n


def area_ratio(n):
    """雪花第 n 次迭代面积 / 初始正三角形面积。"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return 1 + sum((1 / 3) * (4 / 9) ** j for j in range(n))


class KochSnowflakeScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        title = Text("无限周长，有限面积？", font=FONT, font_size=35).move_to(UP * 6.4)
        lead = Text("每条边：三等分，中段向外凸起", font=FONT,
                    font_size=25).move_to(UP * 5.3)

        def outline(vertices):
            coords = [np.array([z.real * 2.35, z.imag * 2.35 + 0.35, 0])
                      for z in vertices]
            return VMobject().set_points_as_corners(coords + [coords[0]]).set_stroke(
                color=TEAL_C, width=3.0)

        points = initial_triangle()
        snowflake = outline(points)
        step = Text("第 0 次：正三角形", font=FONT, font_size=27).move_to(DOWN * 3.5)
        current = MathTex(r"P_0=P_0,\quad A_0=A_0", font_size=32).move_to(DOWN * 4.55)
        self.play(Write(title), FadeIn(lead), Create(snowflake), FadeIn(step), Write(current))
        for n in range(1, 5):
            points = koch_step(points)
            next_step = Text(f"第 {n} 次：{len(points)} 条边", font=FONT,
                             font_size=27).move_to(DOWN * 3.5)
            next_info = MathTex(
                rf"P_{n}/P_0=({{4}}/{{3}})^{{{n}}},\quad A_{n}/A_0\approx {area_ratio(n):.3f}",
                font_size=31).move_to(DOWN * 4.55)
            self.play(Transform(snowflake, outline(points)), Transform(step, next_step),
                      Transform(current, next_info), run_time=1.8)
            self.wait(0.4)
        result = MathTex(r"P_n\to\infty,\quad A_n\to\frac85 A_0",
                         font_size=41, color=YELLOW).move_to(DOWN * 6.0)
        self.play(Write(result))
        self.wait(2)
