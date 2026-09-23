"""七年级：整式的加减法（Manim Community Edition，9:16）。

保留历史 Scene 名称和媒体路径；只用 MathTex 排版数学公式，中文交给 Text。
运行：manim -pql 003_整式的加减法.py 整式的加减法Animation
"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class 整式的加减法Animation(Scene):
    """通过正负号去括号、同类项归并和减法例题讲解整式加减。"""

    def fit_width(self, mob, max_width=7.6):
        """把长公式限制在竖屏安全宽度内，不放大短公式。"""
        if mob.width > max_width:
            mob.scale_to_fit_width(max_width)
        return mob

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font_size=18, color=GRAY_B,
        ).move_to(UP * 7.2)
        self.add(self.author)
        self.opening()
        self.bracket_rule("正号去括号", r"+(a+b)", r"a+b", "括号前是正号：各项符号不变", GREEN)
        self.bracket_rule("负号去括号", r"-(a+b)", r"-a-b", "括号前是负号：括号内每一项都变号", ORANGE)
        self.addition_example()
        self.subtraction_example()
        self.common_error()
        self.summary()

    def opening(self):
        title = Text("整式的加减法", font_size=48, color=WHITE).move_to(UP * 5.5)
        question = self.fit_width(MathTex(r"(2x+3)-(x-1)=\,?", font_size=48))
        question.move_to(UP * 1.5)
        hint = Text("减去一个多项式，括号内的符号怎么办？", font_size=27, color=YELLOW)
        self.fit_width(hint).move_to(DOWN * 0.2)
        self.play(Write(title), run_time=0.9)
        self.play(Write(question), FadeIn(hint), run_time=1.2)
        self.wait(1.3)
        self.play(FadeOut(VGroup(title, question, hint)), run_time=0.5)

    def bracket_rule(self, heading, left_tex, right_tex, explanation, accent):
        title = Text(heading, font_size=38, color=accent).move_to(UP * 5.3)
        left = MathTex(left_tex, font_size=46)
        equal = MathTex("=", font_size=46)
        right = MathTex(right_tex, font_size=46, color=accent)
        formula = self.fit_width(VGroup(left, equal, right).arrange(RIGHT, buff=0.32))
        formula.move_to(UP * 1.3)
        note = self.fit_width(Text(explanation, font_size=26, color=WHITE))
        note.move_to(DOWN * 1.3)
        self.play(Write(title), run_time=0.65)
        self.play(Write(left), run_time=0.85)
        self.play(Circumscribe(left, color=accent), run_time=0.9)
        self.play(Write(equal), Write(right), run_time=1.1)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, formula, note)), run_time=0.55)

    def addition_example(self):
        title = Text("先练习加法：去括号并合并同类项", font_size=30).move_to(UP * 5.3)
        self.fit_width(title)
        lines = [
            r"(2x+3)+(x-1)",
            r"=2x+3+x-1",
            r"=(2x+x)+(3-1)",
            r"=3x+2",
        ]
        steps = VGroup(*(self.fit_width(MathTex(s, font_size=39)) for s in lines))
        steps.arrange(DOWN, buff=0.48, aligned_edge=LEFT).move_to(UP * 0.9)
        self.play(Write(title), run_time=0.7)
        for step in steps:
            self.play(Write(step), run_time=1.1)
            self.wait(0.45)
        self.play(Circumscribe(steps[-1], color=GREEN), run_time=0.8)
        self.wait(1.0)
        self.play(FadeOut(VGroup(title, steps)), run_time=0.55)

    def subtraction_example(self):
        title = Text("减法例题：先变号，再合并", font_size=32).move_to(UP * 5.3)
        lines = [
            r"(2x+3)-(x-1)",
            r"=2x+3-x+1",
            r"=(2x-x)+(3+1)",
            r"=x+4",
        ]
        steps = VGroup(*(self.fit_width(MathTex(s, font_size=41)) for s in lines))
        steps.arrange(DOWN, buff=0.52, aligned_edge=LEFT).move_to(UP * 1.1)
        note = self.fit_width(Text("减号作用于括号里的每一项，包括 -1", font_size=25, color=YELLOW))
        note.move_to(DOWN * 3.35)
        self.play(Write(title), run_time=0.7)
        self.play(Write(steps[0]), run_time=1.0)
        self.play(FadeIn(note), run_time=0.65)
        for step in steps[1:]:
            self.play(Write(step), run_time=1.25)
            self.wait(0.85)
        self.play(Circumscribe(steps[-1], color=GREEN), run_time=0.9)
        self.wait(1.3)
        self.play(FadeOut(VGroup(title, steps, note)), run_time=0.55)

    def common_error(self):
        title = Text("易错提醒：不能只给第一项变号", font_size=30, color=ORANGE)
        self.fit_width(title).move_to(UP * 5.3)
        wrong = self.fit_width(MathTex(r"-(x-1)\neq -x-1", font_size=41, color=RED))
        right = self.fit_width(MathTex(r"-(x-1)=-x+1", font_size=41, color=GREEN))
        wrong.move_to(UP * 1.9)
        right.move_to(DOWN * 0.4)
        note = Text("减号乘括号中的每一项", font_size=27).move_to(DOWN * 2.5)
        self.play(Write(title), run_time=0.7)
        self.play(Write(wrong), run_time=1.1)
        self.play(Write(right), run_time=1.1)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, wrong, right, note)), run_time=0.55)

    def summary(self):
        title = Text("整式加减：去括号 → 合并同类项", font_size=30, color=YELLOW)
        self.fit_width(title).move_to(UP * 4.2)
        answer = self.fit_width(MathTex(r"(2x+3)-(x-1)=x+4", font_size=42))
        answer.move_to(UP * 1.2)
        reminder = Text("括号前是负号，里面每一项都变号", font_size=27)
        self.fit_width(reminder).move_to(DOWN * 1.2)
        self.play(Write(title), run_time=0.7)
        self.play(Write(answer), run_time=1.1)
        self.play(FadeIn(reminder), run_time=0.7)
        self.wait(2)
