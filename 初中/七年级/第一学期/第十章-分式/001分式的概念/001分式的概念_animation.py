"""七年级分式的概念：分母含字母、分母禁值、分式为零的条件。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class Topic001分式的概念Animation(Scene):
    """保留旧场景名称，同时替换没有数学内容的通用动画模板。"""

    def fit(self, mob):
        if mob.width > 7.5:
            mob.scale_to_fit_width(7.5)
        return mob

    def show_rule(self, heading, expression, explanation, color=BLUE):
        heading_mob = self.fit(Text(heading, font_size=34, color=color)).move_to(UP * 4.9)
        formula = self.fit(MathTex(expression, font_size=46)).move_to(UP * 1.4)
        note = self.fit(Text(explanation, font_size=27, color=WHITE)).move_to(DOWN * 1.3)
        self.play(Write(heading_mob), run_time=0.7)
        self.play(Write(formula), run_time=1.1)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.8)
        self.play(FadeOut(VGroup(heading_mob, formula, note)), run_time=0.5)

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        author = Text("上海初高中数学直通车 @emptyandcalm", font_size=18, color=GRAY_B)
        self.fit(author).move_to(UP * 7.2)
        self.add(author)
        title = Text("分式的概念", font_size=48, color=GOLD).move_to(UP * 5.1)
        question = self.fit(MathTex(r"\frac{x+1}{x-2}", font_size=58)).move_to(UP * 1.2)
        self.play(Write(title), Write(question), run_time=1.3)
        self.wait(1.3)
        self.play(FadeOut(VGroup(title, question)), run_time=0.5)

        self.show_rule("什么是分式？", r"\frac{A}{B}",
                       "A、B 是整式，分母 B 含有字母", BLUE)
        self.show_rule("分式有意义的条件", r"B\neq 0",
                       "分母不能为零；代入前先找禁值", ORANGE)
        self.show_rule("实例：先排除分母为零", r"\frac{x+1}{x-2},\quad x\neq 2",
                       "当 x=2 时分母为 0，分式无意义", YELLOW)
        self.show_rule("分式的值为零", r"\frac{A}{B}=0\;\Longleftrightarrow\;A=0,\ B\neq 0",
                       "分子为零，而且分母仍不能为零", GREEN)
        self.show_rule("例题：求分式值为零时的 x", r"\frac{x-1}{x+2}=0\;\Longrightarrow\;x=1",
                       "检验：代入 x=1 后分母为 3，不为零", GREEN)

        summary = self.fit(Text("先看分母，再看分子，最后检验", font_size=32, color=GOLD))
        summary.move_to(UP * 2)
        check = self.fit(MathTex(r"x=1:\quad \frac{1-1}{1+2}=0", font_size=43))
        check.move_to(DOWN * 0.4)
        self.play(Write(summary), Write(check), run_time=1.2)
        self.wait(2)
