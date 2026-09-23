"""竖屏整数与整除课：等分 12 个点，并用 13 个点演示余数反例。"""

from manim import *

# 保留该历史竖屏场景的输出比例；渲染时仍需检查字体与画面安全区。
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class Topic001整数与整除Animation(Scene):
    """被除数、除数与商为整数，余数为零时才构成整除。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        title = Text("整数与整除", font_size=48, color=YELLOW).move_to(UP * 5.4)
        intro = Text("12 个点，平均分成 3 组", font_size=30).move_to(UP * 3.8)
        self.play(Write(title), FadeIn(intro))

        groups = VGroup()
        for _ in range(3):
            dots = VGroup(*[Dot(radius=0.12, color=BLUE) for _ in range(4)])
            dots.arrange_in_grid(rows=2, cols=2, buff=(0.25, 0.25))
            groups.add(dots)
        groups.arrange(RIGHT, buff=0.65).move_to(UP * 1.7)
        self.play(LaggedStart(*(FadeIn(dot) for group in groups for dot in group),
                              lag_ratio=0.1))

        boxes = VGroup(*[
            SurroundingRectangle(group, color=YELLOW, buff=0.18)
            for group in groups
        ])
        self.play(*(Create(box) for box in boxes))
        division = MathTex(r"12\div3=4", font_size=52).move_to(DOWN * 0.3)
        note = Text("每组 4 个，没有剩余：余数是 0", font_size=29)
        note.next_to(division, DOWN, buff=0.38)
        self.play(Write(division), FadeIn(note))
        self.wait(1)

        extra_dot = Dot(radius=0.12, color=RED)
        extra_dot.next_to(groups, RIGHT, buff=0.8)
        extra_note = Text("多出 1 个点，不能再平均分给 3 组", font_size=28)
        extra_note.move_to(note)
        remainder = MathTex(r"13=3\times4+1", font_size=52).move_to(division)
        self.play(FadeIn(extra_dot), ReplacementTransform(division, remainder),
                  FadeOut(note), FadeIn(extra_note))
        self.wait(1)

        self.play(FadeOut(intro), FadeOut(extra_note))
        rules = VGroup(
            Text("12 能被 3 整除；3 能整除 12", font_size=29, color=GREEN),
            Text("13 除以 3 余 1，所以不能被 3 整除", font_size=27, color=YELLOW),
            Text("一般地：a、b、c 为整数，b≠0，a=b×c", font_size=25),
            Text("“能整除”和“能被整除”的方向不同", font_size=26),
        ).arrange(DOWN, buff=0.43).move_to(DOWN * 3.6)
        self.play(LaggedStart(*(FadeIn(line) for line in rules), lag_ratio=0.25))
        self.wait(3)
