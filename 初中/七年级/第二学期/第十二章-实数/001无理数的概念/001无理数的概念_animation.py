"""七年级无理数：对比有理数、无限不循环小数与平方根。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class Topic001无理数的概念Animation(Scene):
    """保留原有入口名，避免以近似小数冒充无理性的证明。"""

    def fit(self, mob):
        if mob.width > 7.5:
            mob.scale_to_fit_width(7.5)
        return mob

    def show_example(self, heading, formula, explanation, color=BLUE):
        heading_mob = self.fit(Text(heading, font_size=34, color=color)).move_to(UP * 5)
        expression = self.fit(MathTex(formula, font_size=47)).move_to(UP * 1.2)
        note = self.fit(Text(explanation, font_size=27, color=WHITE)).move_to(DOWN * 1.4)
        self.play(Write(heading_mob), run_time=0.7)
        self.play(Write(expression), run_time=1.1)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(VGroup(heading_mob, expression, note)), run_time=0.5)

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = Text("上海初高中数学直通车 @emptyandcalm", font_size=18, color=GRAY_B)
        self.fit(author).move_to(UP * 7.2)
        self.add(author)
        title = Text("无理数的概念", font_size=48, color=GOLD).move_to(UP * 5)
        prompt = self.fit(Text("所有无限小数都是无理数吗？", font_size=32)).move_to(UP * 1)
        self.play(Write(title), FadeIn(prompt), run_time=1.1)
        self.wait(1.7)
        self.play(FadeOut(VGroup(title, prompt)), run_time=0.5)

        self.show_example("有理数：有限小数", r"0.25=\frac14",
                          "可以写成两个整数的比", BLUE)
        self.show_example("有理数：无限循环小数", r"0.\overline{3}=\frac13",
                          "无限小数也可能是有理数", BLUE)
        self.show_example("无理数：无限不循环小数", r"\sqrt2\approx1.41421356\ldots",
                          "根号 2 不能写成两个整数的比", GREEN)
        self.show_example("无理数的另一个例子", r"\pi\approx3.14159265\ldots",
                          "省略号只表示近似展开，不是证明", GREEN)

        sec = Text("为什么根号 2 不是有理数？", font_size=32, color=YELLOW)
        self.fit(sec).move_to(UP * 5.1)
        lines = [
            r"\sqrt2=\frac pq\quad (p,q\text{互素})",
            r"p^2=2q^2\ \Longrightarrow\ p\text{为偶数}",
            r"p=2k\ \Longrightarrow\ q^2=2k^2",
            r"q\text{也为偶数，与互素矛盾}",
        ]
        # p、q 的中文字注释由 Text 呈现；只传可移植的 LaTeX 给 MathTex。
        lines = [
            r"\sqrt2=\frac pq", r"p^2=2q^2\ \Longrightarrow\ 2\mid p",
            r"p=2k\ \Longrightarrow\ q^2=2k^2",
            r"2\mid q\quad\text{(contradiction)}",
        ]
        steps = VGroup(*(self.fit(MathTex(s, font_size=35)) for s in lines))
        steps.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 0.5)
        note = self.fit(Text("假设最简分数，得到分子分母同为偶数，矛盾", font_size=24))
        note.move_to(DOWN * 3.3)
        self.play(Write(sec), run_time=0.6)
        for line in steps:
            self.play(Write(line), run_time=0.9)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.5)
        self.play(FadeOut(VGroup(sec, steps, note)), run_time=0.5)

        summary = self.fit(Text("实数 = 有理数 + 无理数", font_size=34, color=GOLD))
        summary.move_to(UP * 1.0)
        self.play(Write(summary), run_time=0.9)
        self.wait(2)
