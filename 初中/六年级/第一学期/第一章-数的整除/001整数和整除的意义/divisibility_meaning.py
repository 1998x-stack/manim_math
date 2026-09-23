"""六年级上册：整数和整除的意义（9:16 竖屏）。

预览：manim -ql divisibility_meaning.py DivisibilityMeaning
正式渲染：manim -qh divisibility_meaning.py DivisibilityMeaning
数学规则见同目录 verify_divisibility.py；渲染后仍需逐镜检查字体和边界。
"""

from manim import *


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class DivisibilityMeaning(Scene):
    """以同一批方块解释平均分组、整除及因数和倍数。"""

    BLUE_MAIN = "#3498db"
    GREEN_OK = "#2ecc71"
    RED_NO = "#e74c3c"
    PURPLE_FACTOR = "#9b59b6"
    ORANGE_MULTIPLE = "#f39c12"
    GROUP_COLORS = ("#9b59b6", "#e74c3c", "#3498db", "#2ecc71", "#f39c12")

    def chinese(self, value, size=30, color=WHITE):
        """中文与数学公式分开：Text 使用运行环境可用的 CJK 字体。"""
        label = Text(value, font_size=size, color=color)
        if label.width > 7.8:
            label.scale_to_fit_width(7.8)
        return label

    def formula(self, latex, size=36, color=WHITE):
        expression = MathTex(latex, font_size=size, color=color)
        if expression.width > 7.8:
            expression.scale_to_fit_width(7.8)
        return expression

    def stage(self, *objects):
        """只清理本镜实际使用的屏上对象；顶端署名保留。"""
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.5)

    def make_squares(self):
        """按行生成十二个同一身份的方块，分组时只移动这些对象。"""
        squares = VGroup()
        for row in range(3):
            for col in range(4):
                square = Square(
                    side_length=0.34,
                    stroke_color=WHITE,
                    stroke_width=1.5,
                    fill_color=self.BLUE_MAIN,
                    fill_opacity=0.85,
                ).move_to(((col - 1.5) * 0.48, 3.0 - row * 0.48, 0))
                squares.add(square)
        return squares

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = self.chinese(
            "上海初高中数学直通车 @emptyandcalm", 20, GRAY_B
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_info), run_time=0.4)
        self.show_opening()
        self.show_concept()
        self.show_example_divisible()
        self.show_example_not_divisible()
        self.show_factor_multiple()
        self.show_notation()
        self.show_outro()

    def show_opening(self):
        title = self.chinese("12 个苹果怎样平均分？", 40, YELLOW).move_to(UP * 5.3)
        scenario = self.chinese("平均分给 3 个同学", 32).move_to(UP * 3.2)
        question = self.chinese("每人能分到几个？", 30, self.BLUE_MAIN).move_to(UP)
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(scenario), FadeIn(question), run_time=0.8)
        self.wait(0.9)
        self.stage(title, scenario, question)

    def show_concept(self):
        title = self.chinese("什么是整除？", 42, self.BLUE_MAIN).move_to(UP * 5.5)
        premise = self.chinese("a、b 都是整数，且 b 不为 0", 29).move_to(UP * 3.7)
        identity = self.formula(r"a=bq,\quad q\in\mathbb{Z}", 45, YELLOW).move_to(UP * 1.9)
        meaning = self.chinese("如果存在这样的整数 q，就说 b 整除 a", 28).move_to(UP * 0.3)
        remainder = self.chinese("等价说法：整数除法的余数为 0", 27, self.GREEN_OK).move_to(DOWN * 1.25)
        notation = self.formula(r"b\mid a", 55, self.GREEN_OK).move_to(DOWN * 3)
        self.play(Write(title), FadeIn(premise), run_time=0.9)
        self.play(Write(identity), run_time=0.9)
        self.play(FadeIn(meaning), FadeIn(remainder), run_time=0.9)
        self.play(Write(notation), run_time=0.6)
        self.wait(1)
        self.stage(title, premise, identity, meaning, remainder, notation)

    def show_example_divisible(self):
        title = self.formula(r"12\div 3=\,?", 48).move_to(UP * 5.4)
        squares = self.make_squares()
        prompt = self.chinese("12 个方块，平均分成 3 组", 29, YELLOW).move_to(UP * 0.7)
        self.play(Write(title), FadeIn(squares), run_time=1.1)
        self.play(FadeIn(prompt), run_time=0.5)
        # 三组各四个；遍历真实方块引用，不创建替身。
        moves = []
        for index, square in enumerate(squares):
            group, within = divmod(index, 4)
            x = (-2.4, 0, 2.4)[group] + (within % 2 - 0.5) * 0.46
            y = 3.0 + (0.5 - within // 2) * 0.46
            moves.append(square.animate.move_to((x, y, 0)).set_fill(
                self.GROUP_COLORS[group], opacity=0.85
            ))
        self.play(*moves, run_time=1.5)
        labels = VGroup(*(
            self.chinese("4", 34, self.GROUP_COLORS[index]).move_to((x, 1.9, 0))
            for index, x in enumerate((-2.4, 0, 2.4))
        ))
        answer = self.formula(r"12=3\times4", 42).move_to(DOWN * 0.55)
        result = self.chinese("每组 4 个，余数为 0：能整除", 30, self.GREEN_OK).move_to(DOWN * 2)
        self.play(FadeIn(labels), Write(answer), run_time=0.8)
        self.play(FadeOut(prompt), FadeIn(result), run_time=0.7)
        self.wait(1)
        self.stage(title, squares, labels, answer, result)

    def show_example_not_divisible(self):
        title = self.formula(r"12\div 5=\,?", 48).move_to(UP * 5.4)
        squares = self.make_squares()
        prompt = self.chinese("尝试平均分成 5 组", 29, YELLOW).move_to(UP * 0.7)
        self.play(Write(title), FadeIn(squares), run_time=1.1)
        self.play(FadeIn(prompt), run_time=0.5)
        moves = []
        xs = (-3.0, -1.5, 0, 1.5, 3.0)
        for index, square in enumerate(squares):
            if index < 10:
                group, within = divmod(index, 2)
                target = (xs[group], 2.9 - within * 0.48, 0)
                moves.append(square.animate.move_to(target).set_fill(
                    self.GROUP_COLORS[group], opacity=0.85
                ))
            else:
                # 原来的最后两个方块就是余下的两个，没有新增或丢失对象。
                target = ((index - 10.5) * 0.55, 1.3, 0)
                moves.append(square.animate.move_to(target).set_fill(self.RED_NO, opacity=0.85))
        self.play(*moves, run_time=1.5)
        labels = VGroup(*(
            self.chinese("2", 27, self.GROUP_COLORS[index]).move_to((x, 1.75, 0))
            for index, x in enumerate(xs)
        ))
        leftover = self.chinese("剩余 2 个", 27, self.RED_NO).move_to((0, 0.55, 0))
        identity = self.formula(r"12=5\times2+2", 41).move_to(DOWN * 0.9)
        conclusion = self.chinese("余数是 2，不是 0：不能整除", 29, self.RED_NO).move_to(DOWN * 2.4)
        self.play(FadeIn(labels), FadeIn(leftover), FadeOut(prompt), run_time=0.7)
        self.play(Write(identity), FadeIn(conclusion), run_time=0.9)
        self.wait(1)
        self.stage(title, squares, labels, leftover, identity, conclusion)

    def show_factor_multiple(self):
        title = self.chinese("因数与倍数", 42, self.BLUE_MAIN).move_to(UP * 5.4)
        identity = self.formula(r"12=3\times4", 46).move_to(UP * 3.6)
        factor = self.chinese("3 和 4 是 12 的因数", 32, self.PURPLE_FACTOR).move_to(UP * 1.6)
        multiple = self.chinese("12 是 3 和 4 的倍数", 32, self.ORANGE_MULTIPLE).move_to(ORIGIN)
        scope = self.chinese("这里讨论正整数的因数与倍数", 27, GRAY_A).move_to(DOWN * 1.8)
        fact = self.chinese("在正整数范围内：因数 ≤ 对应倍数", 28, YELLOW).move_to(DOWN * 3.1)
        self.play(Write(title), Write(identity), run_time=0.9)
        self.play(FadeIn(factor), FadeIn(multiple), run_time=0.9)
        self.play(FadeIn(scope), FadeIn(fact), run_time=0.8)
        self.wait(1)
        self.stage(title, identity, factor, multiple, scope, fact)

    def show_notation(self):
        title = self.chinese("整除的符号", 42, self.BLUE_MAIN).move_to(UP * 5.4)
        symbol = self.formula(r"b\mid a", 60, YELLOW).move_to(UP * 3.4)
        meaning = self.chinese("读作：b 整除 a；表示 a 能被 b 整除", 28).move_to(UP * 1.7)
        yes = self.formula(r"3\mid12", 43, self.GREEN_OK).move_to(ORIGIN)
        yes_explain = self.chinese("因为 12 = 3 × 4", 28).move_to(DOWN * 1)
        no = self.formula(r"5\nmid12", 43, self.RED_NO).move_to(DOWN * 2.4)
        no_explain = self.chinese("因为 12 = 5 × 2 + 2", 28).move_to(DOWN * 3.4)
        self.play(Write(title), Write(symbol), run_time=0.9)
        self.play(FadeIn(meaning), run_time=0.5)
        self.play(Write(yes), FadeIn(yes_explain), run_time=0.8)
        self.play(Write(no), FadeIn(no_explain), run_time=0.8)
        self.wait(1)
        self.stage(title, symbol, meaning, yes, yes_explain, no, no_explain)

    def show_outro(self):
        title = self.chinese("本课总结", 42, YELLOW).move_to(UP * 5.4)
        summary = VGroup(
            self.chinese("a、b 为整数，b 不等于 0", 29),
            self.formula(r"b\mid a\iff a=bq,\ q\in\mathbb{Z}", 37),
            self.chinese("整除时，整数除法的余数为 0", 29, self.GREEN_OK),
            self.chinese("正整数的因数与倍数相互对应", 29, self.ORANGE_MULTIPLE),
        ).arrange(DOWN, buff=0.65).move_to(UP * 1.5)
        signature = self.chinese("上海初高中数学直通车", 32).move_to(DOWN * 3.1)
        author_id = self.chinese("@emptyandcalm", 27, GRAY_B).move_to(DOWN * 4.1)
        self.play(Write(title), FadeIn(summary), run_time=1.2)
        self.wait(1.3)
        self.play(FadeIn(signature), FadeIn(author_id), run_time=0.6)
        self.wait(0.7)
        self.stage(title, summary, signature, author_id, self.author_info)


class TestDivisibility(Scene):
    """独立的轻量演示入口；不冒充完整教学片的验证结果。"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.add(MathTex(r"12=3\times4,\quad 3\mid12"))
