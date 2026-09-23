"""单位复数乘法是旋转：图上位置来自同一数学函数。

Render: manim -pql external/interesting-math/complex-rotation/scene.py ComplexRotationScene
"""
from math import cos, sin, pi
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
FONT = "Noto Sans CJK SC"
BACKGROUND = "#101827"


def rotate_complex(z, theta):
    """将复数 z 乘以单位复数 cos(theta)+i sin(theta)。"""
    return z * complex(cos(theta), sin(theta))


class ComplexRotationScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        title = Text("复数乘法 = 平面旋转？", font=FONT, font_size=34).move_to(UP * 6.4)
        hint = Text("乘以单位复数：模不变，辐角增加", font=FONT,
                    font_size=25).move_to(UP * 5.2)
        plane = NumberPlane(x_range=[-2, 2, 1], y_range=[-2, 2, 1],
                            x_length=6.0, y_length=6.0,
                            background_line_style={"stroke_opacity": 0.25})
        plane.move_to(UP * 0.6)
        z0 = complex(1.2, 0.5)
        theta = ValueTracker(0.0)
        orbit = Circle(radius=abs(z0) * 1.5, color=GREY_B,
                       stroke_opacity=0.5).move_to(plane.c2p(0, 0))

        def endpoint():
            z = rotate_complex(z0, theta.get_value())
            return plane.c2p(z.real, z.imag)

        vector = always_redraw(lambda: Arrow(plane.c2p(0, 0), endpoint(),
                                             buff=0, color=TEAL_C, stroke_width=7))
        point = always_redraw(lambda: Dot(endpoint(), radius=0.09, color=YELLOW))
        projection = always_redraw(lambda: DashedLine(
            endpoint(), plane.c2p(rotate_complex(z0, theta.get_value()).real, 0),
            color=GREY_B, stroke_opacity=0.7))
        formula = MathTex(r"z'=z(\cos\theta+i\sin\theta)",
                          font_size=38).move_to(DOWN * 4.0)
        value_label = MathTex(r"\theta/\pi=", font_size=32).move_to([-0.7, -5.0, 0])
        value = DecimalNumber(0, num_decimal_places=2, font_size=32).next_to(value_label, RIGHT)
        value.add_updater(lambda m: m.set_value(theta.get_value() / pi))
        invariant = MathTex(r"|z'|=|z|", font_size=38,
                            color=TEAL_C).move_to(DOWN * 6.1)
        self.play(Write(title), FadeIn(hint), Create(plane), Create(orbit),
                  Write(formula), FadeIn(value_label), FadeIn(value), FadeIn(invariant))
        self.add(vector, point, projection)
        for angle in (pi / 2, pi, 3 * pi / 2, 2 * pi):
            self.play(theta.animate.set_value(angle), run_time=2, rate_func=linear)
            self.wait(0.3)
        value.clear_updaters()
        self.wait(1.5)
