"""七年级无理数：对比有理数与无理数，证明 √2 不是有理数。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class Topic001无理数的概念Animation(Scene):
    """沿用既有 Scene 入口；小数近似不作为无理性的证明。"""

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
        author = self.fit(Text("上海初高中数学直通车 @emptyandcalm", font_size=18, color=GRAY_B))
        author.move_to(UP * 6.7)
        self.add(author)
        title = self.fit(Text("无理数的概念", font_size=48, color=GOLD)).move_to(UP * 5)
        prompt = self.fit(Text("所有无限小数都是无理数吗？", font_size=32)).move_to(UP * 1)
        self.play(Write(title), FadeIn(prompt), run_time=1.1)
        self.wait(1.7)
        self.play(FadeOut(VGroup(title, prompt)), run_time=0.5)

        self.show_example("有理数：有限小数", r"0.25=\frac{1}{4}",
                          "可以表示为两个整数的比", BLUE)
        self.show_example("有理数：无限循环小数", r"0.\overline{3}=\frac{1}{3}",
                          "无限小数也可能是有理数", BLUE)
        self.show_example("无理数：无限不循环小数", r"\sqrt{2}\approx1.41421356\ldots",
                          "小数近似值本身不能证明无理性", GREEN)
        self.show_example("无理数的另一个例子", r"\pi\approx3.14159265\ldots",
                          "圆周率是无理数；省略号不是证明", GREEN)

        heading = self.fit(Text("为什么根号 2 不是有理数？", font_size=32, color=YELLOW))
        heading.move_to(UP * 5.2)
        assumption = self.fit(Text("反设：p、q 是互素整数，且 q 不为 0", font_size=26))
        assumption.move_to(UP * 3.8)
        # 数学公式与中文说明分别用 MathTex/Text，避免默认 LaTeX 编译中文失败。
        formulas = (
            r"\sqrt{2}=\frac{p}{q}\ \Longrightarrow\ p^2=2q^2",
            r"2\mid p\ \Longrightarrow\ p=2k",
            r"q^2=2k^2\ \Longrightarrow\ 2\mid q",
            r"\gcd(p,q)\geq 2",
        )
        steps = VGroup(*(self.fit(MathTex(formula, font_size=34)) for formula in formulas))
        steps.arrange(DOWN, buff=0.55, aligned_edge=LEFT).move_to(UP * 0.1)
        conclusion = self.fit(Text("分子、分母均为偶数，与互素矛盾", font_size=26))
        conclusion.move_to(DOWN * 3.7)
        self.play(Write(heading), FadeIn(assumption), run_time=0.8)
        for step in steps:
            self.play(Write(step), run_time=1.0)
        self.play(FadeIn(conclusion), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(VGroup(heading, assumption, steps, conclusion)), run_time=0.5)

        summary = self.fit(Text("实数分为有理数与无理数", font_size=34, color=GOLD))
        summary.move_to(UP * 1.0)
        self.play(Write(summary), run_time=0.9)
        self.wait(2)
