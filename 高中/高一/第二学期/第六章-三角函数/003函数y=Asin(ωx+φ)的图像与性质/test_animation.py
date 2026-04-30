"""
Test script to run a quick preview of the y=Asin(ωx+φ) animation.
This creates a shortened version for quick testing purposes.
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TestAsinAnimation(Scene):
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 简化版测试动画
        title = Text(
            "函数y=Asin(ωx+φ)的图像与性质",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).to_edge(UP)

        formula = MathTex(
            "y = A \\sin(\\omega x + \\varphi) + B",
            font_size=40
        ).next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(formula))

        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
            x_axis_config={
                "numbers_to_include": np.arange(-3, 4, 1),
            },
            y_axis_config={
                "numbers_to_include": np.arange(-2, 3, 1),
            },
        ).scale(0.8)

        # 基础正弦函数
        base_graph = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[-3, 3])

        # 变换后的函数 (A=1.5, ω=2, φ=π/4, B=0.5)
        transformed_graph = axes.plot(
            lambda x: 1.5 * np.sin(2*x + np.pi/4) + 0.5,
            color=RED,
            x_range=[-3, 3]
        )

        axes_and_base = VGroup(axes, base_graph)
        axes_and_base.move_to(ORIGIN)

        self.play(Create(axes_and_base))
        self.wait(1)

        # 演示变换
        self.play(Transform(base_graph, transformed_graph))
        self.wait(2)

        # 参数说明
        param_text = VGroup(
            Tex("A: 振幅 (Amplitude)", color=YELLOW),
            Tex("$\\omega$: 频率 (Frequency)", color=YELLOW),
            Tex("$\\varphi$: 相位 (Phase)", color=YELLOW),
            Tex("B: 垂直平移 (Vertical Shift)", color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(DOWN).shift(UP * 0.5)

        self.play(Write(param_text))
        self.wait(3)


if __name__ == "__main__":
    # For testing purposes
    print("Test script ready. Run with: manim -pql test_animation.py TestAsinAnimation")