"""六年级：正比例的比值判断、关系式、图像与应用。"""

from manim import *

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

BG = "#131a30"
BLUE_ACCENT = "#60a5fa"
GOLD = "#fbbf24"
GREEN_ACCENT = "#34d399"


def direct_proportion_rate(points):
    """判断数据点能否满足 y=kx 且 k!=0，返回精确 k，否则返回 None。

    (0,0) 是允许的数据点，但 y/x 在 x=0 时不能计算。
    """
    from fractions import Fraction

    values = tuple(points)
    if len(values) < 2:
        raise ValueError("至少需要两个数据点")
    rate = None
    for pair in values:
        if not isinstance(pair, (tuple, list)) or len(pair) != 2:
            raise ValueError("每个数据点须有两个坐标")
        x, y = pair
        if type(x) is not int or type(y) is not int:
            raise ValueError("只接受整数数据点")
        if x == 0:
            if y != 0:
                return None
            continue
        candidate = Fraction(y, x)
        if candidate == 0:
            return None
        if rate is None:
            rate = candidate
        elif candidate != rate:
            return None
    return rate


class Topic001正比例Animation(Scene):
    """用相同速度下的路程/时间表格、图像和反例解释正比例。"""

    def construct(self):
        assert direct_proportion_rate([(1, 2), (2, 4), (3, 6)]) == 2
        assert direct_proportion_rate([(1, 2), (2, 5)]) is None
        self.camera.background_color = BG
        self.watermark = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font_size=17, color=GRAY_B
        ).move_to(UP * 7)
        self.add(self.watermark)
        self.opening()
        self.table_and_formula()
        self.graph()
        self.counterexample_and_summary()

    def transition(self):
        self.play(*[
            FadeOut(mob) for mob in list(self.mobjects) if mob is not self.watermark
        ], run_time=0.35)

    def heading(self, words):
        title = Text(words, font_size=36, color=GOLD).move_to(UP * 5.6)
        self.play(Write(title))
        return title

    def opening(self):
        title = Text("什么叫正比例？", font_size=46).move_to(UP * 3.5)
        question = Text("时间增加，路程按固定速度增长", font_size=28)
        question.move_to(UP * 1)
        self.play(Write(title), FadeIn(question))
        hint = Text("关键：相对应两个量的比值不变", font_size=28, color=GREEN_ACCENT)
        hint.move_to(DOWN * 1.5)
        self.play(Write(hint))
        self.wait(0.7)
        self.transition()

    def table_and_formula(self):
        self.heading("数据表与比值")
        heading = VGroup(
            Text("时间 x", font_size=27, color=BLUE_ACCENT),
            Text("路程 y", font_size=27, color=GREEN_ACCENT),
            Text("y÷x", font_size=27, color=GOLD),
        ).arrange(RIGHT, buff=0.8).move_to(UP * 3.6)
        self.play(FadeIn(heading))
        rows = VGroup()
        for x, y in [(1, 2), (2, 4), (3, 6)]:
            cells = VGroup(*[
                Text(value, font_size=30)
                for value in (str(x), str(y), str(y // x))
            ]).arrange(RIGHT, buff=1.6)
            rows.add(cells)
        rows.arrange(DOWN, buff=0.5).move_to(UP * 1)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.4)
        rule = MathTex(r"\frac{y}{x}=k,\quad y=kx", font_size=43, color=GOLD)
        rule.move_to(DOWN * 2.3)
        caution = Text("只在 x 不为 0 时计算比值", font_size=24, color=BLUE_ACCENT)
        caution.move_to(DOWN * 3.5)
        self.play(Write(rule), FadeIn(caution))
        self.wait(0.9)
        self.transition()

    def graph(self):
        self.heading("图像经过原点")
        axes = Axes(
            x_range=[0, 4, 1], y_range=[0, 8, 2],
            x_length=4.9, y_length=4.6,
            tips=False, axis_config={"include_numbers": True}
        ).move_to(DOWN * 0.5)
        graph = axes.plot(lambda x: 2 * x, x_range=[0, 3.4], color=GREEN_ACCENT)
        dots = VGroup(*[
            Dot(axes.c2p(x, 2 * x), radius=0.10, color=GOLD)
            for x in (1, 2, 3)
        ])
        self.play(Create(axes), Create(graph), run_time=1.2)
        self.play(FadeIn(dots))
        label = MathTex(r"y=2x", font_size=46, color=GOLD)
        label.move_to(UP * 3.4)
        self.play(Write(label))
        note = Text("非负量的实际图像：从原点出发的射线", font_size=24)
        note.move_to(DOWN * 4.3)
        self.play(FadeIn(note))
        self.wait(0.8)
        self.transition()

    def counterexample_and_summary(self):
        self.heading("判断是否成正比例")
        data = VGroup(
            MathTex(r"(1,2),\quad(2,5)", font_size=42),
            MathTex(r"\frac{2}{1}\ne\frac{5}{2}", font_size=42, color=GOLD),
            Text("比值变化，所以不成正比例", font_size=27, color=WHITE),
        ).arrange(DOWN, buff=0.7).move_to(UP * 1)
        for item in data:
            self.play(Write(item), run_time=0.6)
        conclusion = Text("关键是比值一定，而不是都在增加", font_size=26, color=GREEN_ACCENT)
        conclusion.move_to(DOWN * 3.2)
        self.play(FadeIn(conclusion))
        self.wait(1)
