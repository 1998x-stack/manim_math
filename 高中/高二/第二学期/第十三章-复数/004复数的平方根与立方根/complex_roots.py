"""复数的平方根与立方根（高二）。

区分“方程的所有根”与单值根号；非零复数有三个不同的立方根，
零只有一个不同的根。旧视频需要重新渲染，不应视作本文件的验证结果。

预览：manim -pql complex_roots.py ComplexRoots
"""

import numpy as np
from manim import *


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG_COLOR = "#1a1a2e"
FONT = "PingFang SC"
UNIT_R = 2.0  # 画面长度；复数模长仍为 1
PLANE_CENTER = np.array([0.0, 1.0, 0.0])


def cube_root_point(k):
    """1 的第 k 个立方根在画面中的位置，k 仅取 0、1、2。"""
    if k not in (0, 1, 2):
        raise ValueError("k must be 0, 1 or 2")
    angle = 2 * np.pi * k / 3
    return PLANE_CENTER + UNIT_R * np.array(
        [np.cos(angle), np.sin(angle), 0.0]
    )


class ComplexRoots(Scene):
    """按概念、平方根、立方根、单位根及性质组织的竖屏场景。"""

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.watermark = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B,
        ).move_to(UP * 7.0)
        self.add(self.watermark)
        self.scene_0_hook()
        self.scene_1_sqrt_negative()
        self.scene_2_general_sqrt()
        self.scene_3_cube_root_formula()
        self.scene_4_cube_roots_visual()
        self.scene_5_omega_properties()
        self.scene_6_outro()

    def _card(self, heading, items):
        """短段落独立展示；MathTex 只接收 LaTeX，中文由 Text 渲染。"""
        title = Text(heading, font=FONT, font_size=38, color=YELLOW)
        title.move_to(UP * 5.6)
        rows = VGroup()
        for kind, content in items:
            if kind == "math":
                item = MathTex(content, font_size=37)
            elif kind == "text":
                item = Text(content, font=FONT, font_size=27)
            else:
                raise ValueError(f"unsupported card item: {kind}")
            if item.width > 7.8:
                item.scale_to_fit_width(7.8)
            rows.add(item)
        rows.arrange(DOWN, buff=0.6).move_to(UP * 0.3)
        self.play(Write(title), run_time=0.6)
        for row in rows:
            self.play(FadeIn(row), run_time=0.45)
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(rows), run_time=0.5)

    def scene_0_hook(self):
        self._card("复数的根", [
            ("text", "方程的全部解，与根号的单值记号不同"),
            ("math", r"w^2=-4\ \Longleftrightarrow\ w=\pm 2i"),
            ("math", r"(2i)^2=(-2i)^2=-4"),
        ])

    def scene_1_sqrt_negative(self):
        self._card("负数的平方根", [
            ("math", r"\sqrt{4}=2"),
            ("math", r"x^2=4\ \Longleftrightarrow\ x=\pm 2"),
            ("math", r"w^2=-a\ \Longleftrightarrow\ w=\pm\sqrt{a}\,i"),
            ("math", r"a>0"),
            ("text", "根号的单值记号，不等于列出方程的全部解"),
        ])

    def scene_2_general_sqrt(self):
        self._card("一般复数的平方根", [
            ("math", r"w^2=3+4i,\quad w=x+yi"),
            ("math", r"x^2-y^2=3,\quad 2xy=4"),
            ("math", r"(2+i)^2=3+4i"),
            ("math", r"w=2+i\quad\mathrm{or}\quad w=-2-i"),
            ("text", "两根互为相反数；不能把 x、y 的正负号独立组合"),
        ])

    def scene_3_cube_root_formula(self):
        self._card("复数的立方根", [
            ("math", r"z=r(\cos\theta+i\sin\theta),\quad r>0"),
            ("math", r"w_k=\sqrt[3]{r}\left(\cos\frac{\theta+2k\pi}{3}"
                     r"+i\sin\frac{\theta+2k\pi}{3}\right)"),
            ("math", r"k=0,1,2"),
            ("text", "非零复数有三个不同的立方根，相邻辐角相差 120°"),
            ("math", r"z=0\ \Longrightarrow\ w=0\quad\text{(only one distinct root)}"),
        ])

    def scene_4_cube_roots_visual(self):
        title = Text("1 的三个立方根", font=FONT, font_size=38, color=YELLOW)
        title.move_to(UP * 5.7)
        equation = MathTex(r"w^3=1", font_size=38).move_to(UP * 4.8)
        self.play(Write(title), Write(equation))

        # 显示比例 UNIT_R=2 对应复数模长 1，实际点位置由相同变换生成。
        plane = NumberPlane(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=6, y_length=6,
            background_line_style={"stroke_opacity": 0.25},
        ).move_to(PLANE_CENTER)
        center = plane.c2p(0, 0)
        circle = Circle(radius=UNIT_R, color=GRAY_B).move_to(center)
        self.play(Create(plane), Create(circle), run_time=1.0)

        roots = VGroup()
        colors = [GREEN, BLUE, RED]
        labels = [r"1", r"\omega", r"\omega^2"]
        for k in range(3):
            point = cube_root_point(k)
            # 数学坐标由复平面映射；避免把复数 (1,0) 误写为画面中心。
            dot = Dot(point, color=colors[k], radius=0.1)
            arrow = Arrow(center, point, buff=0, color=colors[k])
            label = MathTex(labels[k], font_size=32, color=colors[k])
            direction = RIGHT if k == 0 else LEFT
            label.next_to(dot, direction, buff=0.25)
            roots.add(dot, arrow, label)
            self.play(GrowArrow(arrow), FadeIn(dot), Write(label), run_time=0.7)

        info = MathTex(
            r"1+\omega+\omega^2=0,\quad |\omega|=1",
            font_size=33,
        ).move_to(DOWN * 4.2)
        note = Text("三个根在单位圆上，辐角间隔为 120°", font=FONT, font_size=26)
        note.move_to(DOWN * 5.0)
        self.play(Write(info), FadeIn(note))
        self.wait(1.5)
        self.play(
            FadeOut(title), FadeOut(equation), FadeOut(plane), FadeOut(circle),
            FadeOut(roots), FadeOut(info), FadeOut(note), run_time=0.6,
        )

    def scene_5_omega_properties(self):
        self._card("ω 的重要性质", [
            ("math", r"\omega=-\frac12+\frac{\sqrt3}{2}i"),
            ("math", r"\omega^3=1,\quad\omega\ne1"),
            ("math", r"1+\omega+\omega^2=0"),
            ("math", r"\omega^2=\overline{\omega}"),
        ])

    def scene_6_outro(self):
        self._card("知识回顾", [
            ("text", "平方根：先写方程，再求全部解"),
            ("text", "立方根：非零复数有三个不同根"),
            ("math", r"1,\ \omega,\ \omega^2"),
            ("text", "零的平方根和立方根都只有一个不同的值：0"),
        ])
