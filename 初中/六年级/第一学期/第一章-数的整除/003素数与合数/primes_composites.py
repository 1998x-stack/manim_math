"""六年级上：素数与合数（9:16 竖屏）。

manim -ql primes_composites.py PrimesComposites
manim -qh primes_composites.py PrimesComposites

素数、合数、数字 1 的颜色和数量均由同一组数学函数计算。
"""

from manim import *
import math
import numpy as np


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PrimesComposites(Scene):
    PRIME = "#2ecc71"
    COMPOSITE = "#e74c3c"
    SPECIAL = "#f39c12"
    FACTOR = "#9b59b6"
    PRIMARY = "#3498db"
    DEFAULT = "#515b6a"

    @staticmethod
    def is_prime(number):
        """只接受整数；0、1、负整数不是素数。"""
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError("number 必须是整数")
        if number < 2:
            return False
        for divisor in range(2, math.isqrt(number) + 1):
            if number % divisor == 0:
                return False
        return True

    @staticmethod
    def get_factors(number):
        """正整数的全部正因数，按从小到大排列。"""
        if not isinstance(number, int) or isinstance(number, bool) or number <= 0:
            raise ValueError("只计算正整数的正因数")
        return tuple(i for i in range(1, number + 1) if number % i == 0)

    def classify(self, number):
        if not isinstance(number, int) or isinstance(number, bool) or number < 1:
            raise ValueError("分类对象必须是正整数")
        if number == 1:
            return "special"
        return "prime" if self.is_prime(number) else "composite"

    def text(self, content, size=30, color=WHITE):
        label = Text(content, font_size=size, color=color)
        if label.width > 7.8:
            label.scale_to_fit_width(7.8)
        return label

    def formula(self, expression, size=40, color=WHITE):
        label = MathTex(expression, font_size=size, color=color)
        if label.width > 7.8:
            label.scale_to_fit_width(7.8)
        return label

    def create_number_circle(self, number, color, radius=0.36, font_size=27):
        """背景圆与数字文字分开；后续只修改 circle[0] 的填充颜色。"""
        circle = Circle(radius=radius, stroke_color=WHITE, stroke_width=1.5,
                        fill_color=color, fill_opacity=0.90)
        numeral = self.text(str(number), font_size, WHITE).move_to(circle.get_center())
        return VGroup(circle, numeral)

    def create_factor_display(self, number, factors, center_pos, center_color, orbit=1.15):
        """中心、因数节点和线共用同一数学数据，无临时替身。"""
        center = self.create_number_circle(number, center_color, radius=0.52, font_size=31)
        center.move_to(center_pos)
        nodes, lines = VGroup(), VGroup()
        for index, factor in enumerate(factors):
            angle = PI / 2 + 2 * PI * index / len(factors)
            pos = center_pos + np.array([orbit * np.cos(angle), orbit * np.sin(angle), 0])
            node = self.create_number_circle(factor, self.FACTOR, radius=0.28, font_size=20)
            node.move_to(pos)
            nodes.add(node)
            lines.add(Line(center.get_center(), node.get_center(), color=GRAY_B,
                           stroke_width=2))
        return VGroup(lines, center, nodes)

    def finish(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.5)

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = self.text("上海初高中数学直通车 @emptyandcalm", 20, GRAY_B)
        self.author_info.move_to(UP * 7.15)
        self.play(FadeIn(self.author_info), run_time=0.4)
        self.show_opening()
        self.show_factors_review()
        self.show_prime_definition()
        self.show_composite_definition()
        self.show_special_cases()
        self.show_classification()
        self.show_outro()

    def show_opening(self):
        title = self.text("这些数字有什么不同？", 39, YELLOW).move_to(UP * 5.4)
        examples = ((2, 3, 5, 7, 11), (4, 6, 8, 9, 10))
        rows = VGroup()
        for values, y in zip(examples, (3.4, 1.65)):
            row = VGroup(*(
                self.create_number_circle(n, self.PRIME if self.is_prime(n) else self.COMPOSITE)
                for n in values
            )).arrange(RIGHT, buff=0.28).move_to((0, y, 0))
            rows.add(row)
        question = self.text("从正因数的数量寻找规律", 29, self.PRIMARY).move_to(DOWN * 0.7)
        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(rows), run_time=0.9)
        self.play(FadeIn(question), run_time=0.5)
        self.wait(0.8)
        self.finish(title, rows, question)

    def show_factors_review(self):
        title = self.text("回顾：一个数的正因数", 38, self.PRIMARY).move_to(UP * 5.3)
        description = self.text("6 的正因数是 1、2、3、6", 30).move_to(UP * 3.75)
        factors = self.get_factors(6)
        display = self.create_factor_display(6, factors, np.array([0, 0.7, 0]), self.PRIMARY)
        count = self.text(f"一共有 {len(factors)} 个正因数", 31, YELLOW).move_to(DOWN * 2.3)
        self.play(Write(title), FadeIn(description), run_time=0.8)
        self.play(FadeIn(display), run_time=1)
        self.play(FadeIn(count), run_time=0.5)
        self.wait(0.8)
        self.finish(title, description, display, count)

    def show_prime_definition(self):
        title = self.text("素数（质数）", 42, self.PRIME).move_to(UP * 5.4)
        definition = self.text("大于 1，且恰有两个正因数", 30).move_to(UP * 4)
        factors = self.get_factors(7)
        display = self.create_factor_display(7, factors, np.array([0, 1.0, 0]), self.PRIME)
        detail = self.text("7 的正因数只有 1 和 7", 30, YELLOW).move_to(DOWN * 1.2)
        conclusion = self.text("所以 7 是素数", 34, self.PRIME).move_to(DOWN * 2.5)
        more = self.text("其他例子：2、3、5、11、13、17、19", 27, GRAY_A).move_to(DOWN * 4)
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        self.play(FadeIn(display), run_time=0.8)
        self.play(FadeIn(detail), FadeIn(conclusion), run_time=0.8)
        self.play(FadeIn(more), run_time=0.5)
        self.wait(0.8)
        self.finish(title, definition, display, detail, conclusion, more)

    def show_composite_definition(self):
        title = self.text("合数", 42, self.COMPOSITE).move_to(UP * 5.4)
        definition = self.text("大于 1，且至少有三个正因数", 30).move_to(UP * 4)
        factors = self.get_factors(6)
        display = self.create_factor_display(6, factors, np.array([0, 1, 0]), self.COMPOSITE)
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        self.play(FadeIn(display), run_time=0.8)
        # 只修改已出现的两枚因数节点的背景；不同时在同一对象上执行 FadeIn 和 animate。
        highlights = [index for index, factor in enumerate(factors) if factor not in (1, 6)]
        self.play(*(
            display[2][index][0].animate.set_fill(self.SPECIAL, opacity=0.9)
            for index in highlights
        ), run_time=0.6)
        detail = self.text("6 除了 1 和 6，还有正因数 2、3", 29, YELLOW).move_to(DOWN * 1.45)
        conclusion = self.text("所以 6 是合数", 34, self.COMPOSITE).move_to(DOWN * 2.8)
        self.play(FadeIn(detail), FadeIn(conclusion), run_time=0.8)
        self.wait(0.9)
        self.finish(title, definition, display, detail, conclusion)

    def show_special_cases(self):
        title = self.text("特殊情况：1 和 2", 40, YELLOW).move_to(UP * 5.4)
        one = self.create_factor_display(1, self.get_factors(1),
                                         np.array([-2, 2.1, 0]), self.SPECIAL, orbit=0.94)
        two = self.create_factor_display(2, self.get_factors(2),
                                         np.array([2, 2.1, 0]), self.PRIME, orbit=0.94)
        one_note = self.text("1 只有一个正因数", 26, self.SPECIAL).move_to((-2, -0.4, 0))
        one_fact = self.text("既不是素数也不是合数", 24, self.SPECIAL).move_to((-2, -1.35, 0))
        two_note = self.text("2 只有两个正因数", 26, self.PRIME).move_to((2, -0.4, 0))
        two_fact = self.text("最小且唯一的偶素数", 24, self.PRIME).move_to((2, -1.35, 0))
        parity = self.text("偶数大于 2 时，除 1 和本身外还可被 2 整除", 26)
        parity.move_to(DOWN * 3.2)
        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(one), FadeIn(two), run_time=0.8)
        self.play(FadeIn(one_note), FadeIn(one_fact),
                  FadeIn(two_note), FadeIn(two_fact), run_time=0.9)
        self.play(FadeIn(parity), run_time=0.6)
        self.wait(0.9)
        self.finish(title, one, two, one_note, one_fact, two_note, two_fact, parity)

    def show_classification(self):
        title = self.text("1—20 的分类", 42, self.PRIMARY).move_to(UP * 5.4)
        numbers = tuple(range(1, 21))
        nodes = VGroup()
        for index, n in enumerate(numbers):
            row, col = divmod(index, 5)
            nodes.add(self.create_number_circle(n, self.DEFAULT, radius=0.34, font_size=24)
                      .move_to(((col - 2) * 1.25, 3.3 - row * 1.12, 0)))
        self.play(Write(title), FadeIn(nodes), run_time=1.1)
        # 数字标签固定为白色，只为真实圆形背景着色。
        classifications = {n: self.classify(n) for n in numbers}
        color_map = {"prime": self.PRIME, "composite": self.COMPOSITE,
                     "special": self.SPECIAL}
        for category in ("special", "prime", "composite"):
            indices = [n - 1 for n in numbers if classifications[n] == category]
            self.play(*(nodes[i][0].animate.set_fill(color_map[category], opacity=0.9)
                        for i in indices), run_time=0.8)
        primes = tuple(n for n in numbers if classifications[n] == "prime")
        composites = tuple(n for n in numbers if classifications[n] == "composite")
        special = tuple(n for n in numbers if classifications[n] == "special")
        counts = VGroup(
            self.text(f"素数 {len(primes)} 个", 29, self.PRIME),
            self.text(f"合数 {len(composites)} 个", 29, self.COMPOSITE),
            self.text(f"特殊的 1：{len(special)} 个", 28, self.SPECIAL),
        ).arrange(DOWN, buff=0.55).move_to(DOWN * 2.9)
        self.play(FadeIn(counts), run_time=0.7)
        self.wait(1)
        self.finish(title, nodes, counts)

    def show_outro(self):
        title = self.text("本课总结", 42, YELLOW).move_to(UP * 5.4)
        points = VGroup(
            self.text("素数：大于 1，恰有两个正因数", 30, self.PRIME),
            self.text("合数：大于 1，至少有三个正因数", 30, self.COMPOSITE),
            self.text("1 既不是素数也不是合数", 30, self.SPECIAL),
            self.text("2 是唯一的偶素数", 30, self.PRIME),
        ).arrange(DOWN, buff=0.65).move_to(UP * 1.25)
        signature = self.text("上海初高中数学直通车", 31).move_to(DOWN * 3.2)
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(points), run_time=1)
        self.play(FadeIn(signature), run_time=0.6)
        self.wait(1)
        self.finish(title, points, signature, self.author_info)


class TestPrimesComposites(Scene):
    """独立轻量预览入口。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.add(MathTex(r"7\text{ is prime},\quad 6=2\times3"))
