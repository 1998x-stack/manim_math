"""年、月、日的简短示例；完整课程见同目录 YearMonthDay。"""

from manim import *


class YearMonthDayPreview(Scene):
    """用中文 Text 呈现年月日知识点，避免把中文直接放入 MathTex。"""

    def construct(self):
        title = Text("年、月、日", font_size=42).to_edge(UP)
        self.play(Write(title))

        facts = VGroup(
            Text("1 年 = 12 个月", font_size=34),
            Text("大月：31 天；小月：30 天", font_size=30),
            Text("2 月：平年 28 天，闰年 29 天", font_size=28),
        ).arrange(DOWN, buff=0.65).move_to(ORIGIN)
        for fact in facts:
            self.play(Write(fact))
            self.wait(0.35)
        self.wait(1)
