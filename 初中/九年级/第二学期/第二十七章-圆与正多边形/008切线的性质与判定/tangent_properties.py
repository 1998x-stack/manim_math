"""切线的性质与判定：八段教学入口，统一复用经过数学验证的切线数据。

将冗余而可能出现不一致的切点计算集中到 tangent_math.py 和 tangent_theorems.py；
此课单独保留原 TangentProperties 类名及八个公开分镜方法。
"""
from manim import *
import numpy as np
from tangent_math import tangent_points, verify_tangent_geometry
from tangent_theorems import TangentTheorems

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TangentProperties(TangentTheorems, Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.O = np.array([0.0, 0.8, 0.0])
        self.r = 1.8
        self.T = self.O + self.r * RIGHT
        self.P = np.array([3.0, 2.5, 0.0])
        self.A, self.B = (
            np.array([*point, 0.0])
            for point in tangent_points(tuple(self.O[:2]), self.r, tuple(self.P[:2]))
        )
        self.length = verify_tangent_geometry(tuple(self.O[:2]), self.r, tuple(self.P[:2]))
        self.circle = Circle(radius=self.r, color=self.BLUE_CIRCLE, stroke_width=4).move_to(self.O)
        self.scene_1_opening()
        self.scene_2_tangent_property_intro()
        self.scene_3_perpendicular_proof()
        self.scene_4_tangent_criteria_intro()
        self.scene_5_tangent_criteria_demo()
        self.scene_6_tangent_length_intro()
        self.scene_7_tangent_length_proof()
        self.scene_8_summary_outro()

    def scene_2_tangent_property_intro(self):
        heading = self.headline("切线只有一个公共点")
        radius = Line(self.O, self.T, color=self.GREEN_RADIUS, stroke_width=3)
        line = Line(self.T + DOWN * 2.4, self.T + UP * 2.4,
                    color=self.RED_TANGENT, stroke_width=4)
        dot = Dot(self.T, color=YELLOW, radius=0.11)
        caption = Text("T 在圆上，也是直线与圆的唯一公共点", font="sans-serif",
                       font_size=23, color=GRAY_A).move_to(DOWN * 4.7)
        self.play(Write(heading), Create(radius))
        self.play(Create(line), FadeIn(dot), FadeIn(caption))
        self.wait(0.8)
        self.play(FadeOut(VGroup(heading, radius, line, dot, caption)))

    def scene_3_perpendicular_proof(self):
        # 以真实切点、半径、直角标记给出切线性质，不依赖角标签猜测。
        super().scene_2_tangent_property()

    def scene_4_tangent_criteria_intro(self):
        heading = self.headline("判定切线需要两个条件")
        premise_1 = Text("① 直线经过半径的外端点 T", font="sans-serif",
                         font_size=26).move_to(UP * 1.8)
        premise_2 = Text("② 直线与该半径垂直", font="sans-serif",
                         font_size=26).move_to(DOWN * 0.1)
        warning = Text("只有垂直或只有经过圆上一点，都不足以判定", font="sans-serif",
                       font_size=22, color=YELLOW).move_to(DOWN * 3.6)
        self.play(Write(heading), FadeIn(premise_1))
        self.play(FadeIn(premise_2), FadeIn(warning))
        self.wait(1.0)
        self.play(FadeOut(VGroup(heading, premise_1, premise_2, warning)))

    def scene_5_tangent_criteria_demo(self):
        super().scene_3_tangent_criterion()

    def scene_6_tangent_length_intro(self):
        super().scene_4_tangent_length_prep()

    def scene_7_tangent_length_proof(self):
        # 直角三角形 OAP 与 OBP 斜边 OP 公共，直角边 OA=OB；
        # 使用 RHS 全等而非仅以视觉等长代替证明。
        super().scene_5_tangent_length_theorem()

    def scene_8_summary_outro(self):
        super().scene_6_summary()
        super().scene_7_outro()


# manim -ql tangent_properties.py TangentProperties
