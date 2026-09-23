"""复平面几何：初始向量、旋转角、轨迹圆及有向坐标投影同步更新。

Render: manim external/interesting-math/complex-rotation/scene.py ComplexRotationScene
"""
from math import atan2, cos, pi, sin
from manim import *

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
FONT = "Noto Sans CJK SC"
BACKGROUND = "#101827"


def rotate_complex(z, theta):
    """乘以模为一的复数：保持长度并叠加转角。"""
    return z * complex(cos(theta), sin(theta))


class ComplexRotationScene(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        self.add(Text("上海初高中数学直通车 @emptyandcalm", font=FONT,
                      font_size=17, color=GREY_B).move_to(UP * 7))
        title = Text("复数乘法 = 平面旋转？", font=FONT,
                     font_size=34).move_to(UP * 6.3)
        hint = Text("灰色为原向量，黄色为乘法后的向量", font=FONT,
                    font_size=24).move_to(UP * 5.12)
        plane = NumberPlane(x_range=[-2, 2, 1], y_range=[-2, 2, 1],
                            x_length=6, y_length=6,
                            background_line_style={"stroke_opacity": 0.25})
        plane.move_to(UP * 0.55)
        z0 = complex(1.2, 0.5)
        theta = ValueTracker(0.0)
        origin = plane.c2p(0, 0)
        scale = plane.c2p(1, 0)[0] - origin[0]
        orbit = Circle(radius=abs(z0)*scale, color=BLUE_B,
                       stroke_opacity=0.75, stroke_width=2).move_to(origin)
        reference = Arrow(origin, plane.c2p(z0.real, z0.imag),
                          color=GREY_B, stroke_width=5, buff=0,
                          max_tip_length_to_length_ratio=0.14)

        def rotated():
            return rotate_complex(z0, theta.get_value())

        def endpoint():
            z = rotated()
            return plane.c2p(z.real, z.imag)

        vector = always_redraw(lambda: Arrow(
            origin, endpoint(), buff=0, color=YELLOW, stroke_width=6,
            max_tip_length_to_length_ratio=0.14))
        moving_point = always_redraw(lambda: Dot(endpoint(), color=YELLOW,
                                                  radius=0.08))
        foot = lambda: plane.c2p(rotated().real, 0)

        def projection():
            p = endpoint()
            f = foot()
            # Avoid a zero-length dashed line when the point crosses the real axis.
            components = VGroup(Line(origin, f, color=TEAL_C,
                                     stroke_width=4))
            if abs(p[1]-f[1]) > 0.025:
                components.add(DashedLine(f, p, color=TEAL_C,
                                           stroke_opacity=0.9))
            return components

        triangle = always_redraw(projection)
        arc = always_redraw(lambda: Arc(
            radius=0.76, start_angle=atan2(z0.imag, z0.real),
            angle=max(0.0001, theta.get_value()), arc_center=origin,
            color=YELLOW, stroke_width=3))
        angle_label = MathTex(r"\theta", color=YELLOW,
                              font_size=31).move_to([2.45, 3.65, 0])
        angle_value = DecimalNumber(0, num_decimal_places=2,
                                    font_size=29, color=YELLOW).next_to(
                                        angle_label, RIGHT, buff=0.12)
        angle_value.add_updater(lambda mob: mob.set_value(theta.get_value()/pi))
        angle_units = MathTex(r"\times\pi", color=YELLOW,
                              font_size=28).next_to(angle_value, RIGHT, buff=0.12)
        # All displayed signed projections are derived from the same z' as the dot.
        x_name = MathTex(r"x'=", font_size=34, color=TEAL_C).move_to([-2.7, -4.35, 0])
        x_value = DecimalNumber(z0.real, num_decimal_places=2,
                                font_size=33, color=TEAL_C).next_to(x_name, RIGHT)
        x_value.add_updater(lambda mob: mob.set_value(rotated().real))
        y_name = MathTex(r"y'=", font_size=34, color=TEAL_C).move_to([0.85, -4.35, 0])
        y_value = DecimalNumber(z0.imag, num_decimal_places=2,
                                font_size=33, color=TEAL_C).next_to(y_name, RIGHT)
        y_value.add_updater(lambda mob: mob.set_value(rotated().imag))
        equation = MathTex(r"z'=z(\cos\theta+i\sin\theta)",
                           font_size=37).move_to(DOWN*3.36)
        coordinate_rule = MathTex(
            r"x'=x\cos\theta-y\sin\theta,\quad"
            r"y'=x\sin\theta+y\cos\theta",
            font_size=28).move_to(DOWN*5.45)
        invariant = MathTex(r"|z'|=|z|", font_size=37,
                            color=YELLOW).move_to(DOWN*6.35)
        self.play(Write(title), FadeIn(hint), Create(plane), Create(orbit),
                  Create(reference), Write(equation), Write(coordinate_rule),
                  FadeIn(x_name), FadeIn(y_name), FadeIn(x_value),
                  FadeIn(y_value), FadeIn(angle_label),
                  FadeIn(angle_value), FadeIn(angle_units), FadeIn(invariant))
        self.add(triangle, arc, vector, moving_point)
        for target in (pi/2, pi, 3*pi/2, 2*pi):
            self.play(theta.animate.set_value(target), run_time=2,
                      rate_func=linear)
            self.wait(0.45)
        angle_value.clear_updaters()
        x_value.clear_updaters()
        y_value.clear_updaters()
        self.wait(1.5)
