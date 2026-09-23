"""认识周长的简短示例；完整课程见同目录 001认识周长_animation.py。"""

from manim import *


class PerimeterIntroductionPreview(Scene):
    """用沿封闭图形的边界描画解释周长，不将中文传入 MathTex。"""

    def construct(self):
        title = Text("认识周长", font_size=42).to_edge(UP)
        self.play(Write(title))

        outline = Rectangle(width=3.6, height=2.2, color=BLUE).move_to(UP * 0.4)
        self.play(Create(outline), run_time=2)
        explanation = Text("封闭图形一周边线的长度叫周长", font_size=30).next_to(
            outline, DOWN, buff=0.65
        )
        self.play(Indicate(outline, color=YELLOW), Write(explanation))
        self.wait(1)
