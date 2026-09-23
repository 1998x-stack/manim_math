"""y=A sin(ωx+φ)+B 的快速预览场景。

仅用于检查布局和图像变换，不替代完整场景的数学与渲染验收。
运行：manim -pql test_animation.py TestAsinAnimation
"""

from manim import *
import numpy as np


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TestAsinAnimation(Scene):
    def construct(self):
        self.camera.background_color = '#1a1a2e'

        title = Text(
            '函数 y=A sin(ωx+φ)+B 的图像与性质',
            font='PingFang SC', font_size=36, color=GOLD,
        ).scale_to_fit_width(8).to_edge(UP, buff=0.6)
        formula = MathTex(
            r'y=A\sin(\omega x+\varphi)+B', font_size=40,
        ).next_to(title, DOWN, buff=0.4)
        self.play(Write(title), run_time=0.7)
        self.play(Write(formula), run_time=0.7)

        axes = Axes(
            x_range=[-PI, PI, PI / 2],
            y_range=[-2.5, 2.5, 1],
            x_length=6.4,
            y_length=4.0,
            axis_config={'color': BLUE},
            tips=False,
        ).move_to(DOWN * 0.4)
        # 先安放坐标系再绘图，确保所有曲线共享同一个坐标映射。
        base_graph = axes.plot(np.sin, x_range=[-PI, PI], color=BLUE)
        transformed_graph = axes.plot(
            lambda x: 1.5 * np.sin(2 * x + PI / 4) + 0.5,
            x_range=[-PI, PI], color=RED,
        )
        self.play(Create(axes), Create(base_graph), run_time=1.2)
        self.wait(0.5)
        self.play(Transform(base_graph, transformed_graph), run_time=1.2)

        # 普通中文必须使用 Text；Tex/MathTex 只包含数学公式。
        # ω 为角频率而不是通常以 Hz 表示的频率。
        descriptions = VGroup(
            Text('A：振幅的绝对值 |A|', font='PingFang SC', font_size=22),
            Text('ω：角频率；周期 T=2π/|ω|', font='PingFang SC', font_size=22),
            Text('φ：初相；水平位移 -φ/ω', font='PingFang SC', font_size=22),
            Text('B：竖直平移', font='PingFang SC', font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        descriptions.scale_to_fit_width(min(descriptions.width, 7.8))
        descriptions.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(descriptions), run_time=0.7)
        self.wait(1)


if __name__ == '__main__':
    print('Run: manim -pql test_animation.py TestAsinAnimation')
