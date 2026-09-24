"""六年级下 · 相反数：数轴关于原点的对称与代数性质。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


def opposite(value):
    """任意有理数的相反数；特别地 opposite(0) == 0。"""
    return -value


class OppositeNumbers(Scene):
    """原场景入口不变；按“实例→数轴→定义→推广→零→总结”呈现。"""

    def construct(self):
        self.camera.background_color = "#141827"
        self.positive = "#76DDB0"
        self.negative = "#FFAF7E"
        self.zero_color = "#C4A2FF"
        self.muted = "#C4CDDE"
        self.header = Text("上海初高中数学直通车 @emptyandcalm",
                           font_size=21, color=self.muted).move_to(UP * 6.7)
        self.title = Text("相反数", font_size=41, color=YELLOW).move_to(UP * 5.65)
        self.add(self.header)
        self.play(Write(self.title), run_time=0.5)
        self.overlay = None
        self.axis = None
        self.scene_1_opening()
        self.scene_2_number_line()
        self.scene_3_definition()
        self.scene_4_more_examples()
        self.scene_5_special_case()
        self.scene_6_summary()

    def set_overlay(self, title, *objects):
        """只淡出本镜实际显示的对象，保留统一的顶栏与必要的数轴。"""
        if self.overlay is not None:
            self.play(FadeOut(self.overlay), run_time=0.35)
        next_title = Text(title, font_size=41, color=YELLOW).move_to(UP * 5.65)
        self.play(Transform(self.title, next_title), run_time=0.35)
        self.overlay = VGroup(*objects)

    def scene_1_opening(self):
        prompt = Text("3 与 -3 有什么关系？", font_size=34).move_to(UP * 4.1)
        numbers = VGroup(
            MathTex("3", font_size=84, color=self.positive),
            MathTex("-3", font_size=84, color=self.negative),
        ).arrange(RIGHT, buff=1.75).move_to(UP * 1.8)
        answer = Text("它们互为相反数", font_size=33, color=YELLOW)
        answer.move_to(DOWN * 1)
        self.set_overlay("相反数", prompt, numbers, answer)
        self.play(Write(prompt), FadeIn(numbers), run_time=0.9)
        self.wait(0.4)
        self.play(FadeIn(answer), run_time=0.5)
        self.wait(0.7)

    def scene_2_number_line(self):
        self.axis = NumberLine(x_range=[-5, 5, 1], length=7.1,
                               include_numbers=True, font_size=23,
                               include_tip=True, color=self.muted)
        self.axis.move_to(UP * 0.8)
        left = Dot(self.axis.n2p(-3), radius=0.12, color=self.negative)
        right = Dot(self.axis.n2p(3), radius=0.12, color=self.positive)
        zero = Dot(self.axis.n2p(0), radius=0.12, color=self.zero_color)
        left_label = MathTex("-3", color=self.negative, font_size=36)
        left_label.move_to(left.get_center() + UP * 0.65)
        right_label = MathTex("3", color=self.positive, font_size=36)
        right_label.move_to(right.get_center() + UP * 0.65)
        note = Text("距原点同样远，分别在原点两侧", font_size=28,
                    color=self.muted).move_to(DOWN * 1.6)
        pair = VGroup(left, right, zero, left_label, right_label)
        self.set_overlay("数轴上的相反数", pair, note)
        self.play(Create(self.axis), run_time=0.9)
        self.play(FadeIn(pair), run_time=0.6)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(0.8)

    def scene_3_definition(self):
        left_value, right_value = opposite(3), 3
        left = self.axis.n2p(left_value)
        right = self.axis.n2p(right_value)
        origin = self.axis.n2p(0)
        # 距离箭头放在数轴上方，避免与轴上的刻度重叠。
        left_arrow = DoubleArrow(origin + UP * 1.55, left + UP * 1.55,
                                 buff=0, tip_length=0.13, color=self.negative)
        right_arrow = DoubleArrow(origin + UP * 1.55, right + UP * 1.55,
                                  buff=0, tip_length=0.13, color=self.positive)
        left_distance = MathTex("3", color=self.negative, font_size=30)
        left_distance.move_to((origin + left) / 2 + UP * 2.05)
        right_distance = MathTex("3", color=self.positive, font_size=30)
        right_distance.move_to((origin + right) / 2 + UP * 2.05)
        definition = Text("在数轴上，两点关于原点对称", font_size=29)
        definition.move_to(DOWN * 2.1)
        rule = MathTex(r"a+(-a)=0", font_size=44, color=YELLOW)
        rule.move_to(DOWN * 3.4)
        self.set_overlay("相反数的定义", left_arrow, right_arrow,
                         left_distance, right_distance, definition, rule)
        self.play(GrowArrow(left_arrow), GrowArrow(right_arrow), run_time=0.9)
        self.play(FadeIn(left_distance), FadeIn(right_distance), run_time=0.4)
        self.play(Write(definition), Write(rule), run_time=0.9)
        self.wait(1)

    def scene_4_more_examples(self):
        examples = [(4, self.positive), (opposite(4), self.negative),
                    (1.5, self.positive), (opposite(1.5), self.negative)]
        marks = VGroup()
        for value, color in examples:
            dot = Dot(self.axis.n2p(value), radius=0.1, color=color)
            label = MathTex(f"{value:g}", font_size=30, color=color)
            label.move_to(dot.get_center() + UP * 0.7)
            marks.add(VGroup(dot, label))
        statement = MathTex(r"-(-a)=a", font_size=43)
        statement.move_to(DOWN * 2)
        note = Text("数轴上每个数都有唯一的相反数", font_size=28,
                    color=self.muted).move_to(DOWN * 3.3)
        self.set_overlay("相反数举例", marks, statement, note)
        self.play(LaggedStart(*[FadeIn(mark) for mark in marks], lag_ratio=0.22))
        self.play(Write(statement), FadeIn(note), run_time=0.8)
        self.wait(0.9)

    def scene_5_special_case(self):
        dot = Dot(self.axis.n2p(opposite(0)), radius=0.18, color=self.zero_color)
        text = Text("0 的相反数是 0", font_size=35,
                    color=self.zero_color).move_to(UP * 3.4)
        formula = MathTex(r"-(0)=0,\quad 0+0=0", font_size=39)
        formula.move_to(DOWN * 1.8)
        explanation = Text("原点关于自身对称，0 不分正负", font_size=27,
                           color=self.muted).move_to(DOWN * 3.1)
        self.set_overlay("零的相反数", dot, text, formula, explanation)
        self.play(FadeIn(dot, scale=1.3), FadeIn(text), run_time=0.7)
        self.play(Write(formula), FadeIn(explanation), run_time=0.8)
        self.wait(0.9)

    def scene_6_summary(self):
        if self.axis is not None:
            self.play(FadeOut(self.axis), run_time=0.35)
        facts = VGroup(
            Text("任意有理数 a 的相反数是 -a", font_size=30),
            Text("在数轴上关于原点对称", font_size=30),
            MathTex(r"a+(-a)=0", font_size=41),
            MathTex(r"-(-a)=a", font_size=41),
            Text("0 的相反数还是 0", font_size=30, color=self.zero_color),
        ).arrange(DOWN, buff=0.73).move_to(UP * 0.5)
        self.set_overlay("相反数总结", facts)
        self.play(LaggedStart(*[FadeIn(item, shift=RIGHT * 0.15)
                                for item in facts], lag_ratio=0.16))
        self.wait(1.2)
