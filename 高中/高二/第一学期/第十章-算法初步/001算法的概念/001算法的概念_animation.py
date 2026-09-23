"""高二《算法的概念》：用 1 到 n 的求和展示输入、步骤、终止及输出。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

FONT = "PingFang SC"
BG = "#1a1a2e"


class Topic001算法的概念Animation(Scene):
    """保留原有 Scene 入口，删除无数学内容的通用占位演示。"""

    def construct(self):
        self.camera.background_color = BG
        watermark = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B,
        ).move_to(UP * 7.0)
        self.add(watermark)
        self.show_definition()
        self.show_five_properties()
        self.show_example()
        self.show_summary()

    def show_card(self, heading, lines):
        title = Text(heading, font=FONT, font_size=39, color=YELLOW)
        title.move_to(UP * 5.5)
        content = VGroup(*[
            Text(line, font=FONT, font_size=27, color=WHITE)
            for line in lines
        ])
        for row in content:
            if row.width > 7.8:
                row.scale_to_fit_width(7.8)
        content.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        content.move_to(UP * 0.2)
        self.play(Write(title))
        for row in content:
            self.play(FadeIn(row, shift=UP * 0.1), run_time=0.45)
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(content), run_time=0.5)

    def show_definition(self):
        self.show_card("什么是算法？", [
            "针对一类问题，给出明确且有限的步骤。",
            "同样的输入，按同样规则执行。",
            "例如：求从 1 到 n 的整数和。",
        ])

    def show_five_properties(self):
        self.show_card("算法的基本特征", [
            "输入：确定一个正整数 n。",
            "确定性：每一步没有歧义。",
            "可行性：加法和比较都能执行。",
            "有穷性：循环恰好执行 n 次。",
            "输出：得到一个确定的整数和。",
        ])

    def show_example(self):
        title = Text("一个完整的算法", font=FONT, font_size=38, color=YELLOW)
        title.move_to(UP * 5.5)
        target = MathTex(r"S=1+2+\cdots+n,\quad n\in\mathbb{Z}_{>0}", font_size=35)
        target.move_to(UP * 4.45)
        self.play(Write(title), Write(target))

        steps = [
            "输入 n；设 S=0，k=1。",
            "若 k≤n，执行 S=S+k。",
            "令 k=k+1，返回条件判断。",
            "若 k>n，输出 S，结束。",
        ]
        pseudocode = VGroup(*[
            Text(step, font=FONT, font_size=26) for step in steps
        ])
        pseudocode.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 1.7)
        for row in pseudocode:
            if row.width > 7.8:
                row.scale_to_fit_width(7.8)
            self.play(FadeIn(row), run_time=0.4)
        self.wait(0.7)
        self.play(FadeOut(pseudocode))

        input_label = Text("示例输入：n=4", font=FONT, font_size=28, color=BLUE)
        input_label.move_to(UP * 1.8)
        self.play(Write(input_label))
        traces = [(1, 1), (2, 3), (3, 6), (4, 10)]
        trace_mob = None
        for k, total in traces:
            next_trace = MathTex(
                rf"k={k},\quad S={total}", font_size=36, color=GREEN
            ).move_to(ORIGIN)
            if trace_mob is None:
                self.play(Write(next_trace), run_time=0.45)
            else:
                self.play(ReplacementTransform(trace_mob, next_trace), run_time=0.45)
            trace_mob = next_trace
        output = Text("下一次 k=5>4，循环结束；输出 10", font=FONT, font_size=25)
        output.move_to(DOWN * 1.2)
        self.play(FadeIn(output))
        self.wait(1.2)
        self.play(*[
            FadeOut(obj) for obj in [title, target, input_label, trace_mob, output]
        ])

    def show_summary(self):
        self.show_card("小结", [
            "明确输入 → 按规则执行 → 有限步结束。",
            "本例 n=4，四次累加后输出 10。",
            "流程图与伪代码可以描述同一算法。",
        ])
