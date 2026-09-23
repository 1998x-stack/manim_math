"""六年级上册：分解素因数（竖屏 9:16）。

预览：manim -ql prime_factorization.py PrimeFactorization
正式渲染：manim -qh prime_factorization.py PrimeFactorization
短除法行、显示公式和验算均由同一组数据生成；渲染和画面检查仍需单独执行。
"""

from manim import *


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PrimeFactorization(Scene):
    PRIMARY = "#3498db"
    PRIME = "#e74c3c"
    COMPOSITE = "#2ecc71"
    HIGHLIGHT = "#f39c12"
    DIVISOR = "#9b59b6"

    @staticmethod
    def prime_factors(number):
        """正整数 number>=2 的素因数，含重数，按非降序返回。"""
        if not isinstance(number, int) or isinstance(number, bool) or number < 2:
            raise ValueError("number 必须是至少为 2 的整数")
        current, divisor = number, 2
        result = []
        while divisor * divisor <= current:
            while current % divisor == 0:
                result.append(divisor)
                current //= divisor
            divisor += 1
        if current > 1:
            result.append(current)
        return tuple(result)

    @staticmethod
    def short_division_steps(number):
        """输出 (被除数, 素除数, 整数商)，最后一行整数商为 1。"""
        factors = PrimeFactorization.prime_factors(number)
        rows, current = [], number
        for factor in factors:
            quotient, remainder = divmod(current, factor)
            if remainder != 0:
                raise ArithmeticError("短除法的商必须是整数")
            rows.append((current, factor, quotient))
            current = quotient
        if current != 1:
            raise ArithmeticError("短除法必须在商为 1 时结束")
        return tuple(rows)

    def text(self, text, size=30, color=WHITE):
        label = Text(text, font_size=size, color=color)
        if label.width > 7.8:
            label.scale_to_fit_width(7.8)
        return label

    def math(self, latex, size=40, color=WHITE):
        label = MathTex(latex, font_size=size, color=color)
        if label.width > 7.8:
            label.scale_to_fit_width(7.8)
        return label

    def clear_stage(self, *objects):
        self.play(*(FadeOut(obj) for obj in objects), run_time=0.5)

    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self.author_info = self.text("上海初高中数学直通车 @emptyandcalm", 20, GRAY_B)
        self.author_info.move_to(UP * 7.15)
        self.play(FadeIn(self.author_info), run_time=0.4)
        self.show_opening()
        self.show_prime_composite()
        self.show_definition()
        self.show_division_30()
        self.show_division_60()
        self.show_summary()

    def show_opening(self):
        title = self.text("30 可以分成哪些数相乘？", 38, self.HIGHLIGHT)
        title.move_to(UP * 5.4)
        examples = VGroup(*(
            self.math(expr, 37)
            for expr in (r"1\times30", r"2\times15", r"3\times10", r"5\times6")
        )).arrange(DOWN, buff=0.5).move_to(UP * 2.25)
        target = self.math(r"30=2\times3\times5", 45, self.PRIME)
        target.move_to(DOWN * 1.9)
        remark = self.text("继续拆分，直到每个因数都是素数", 28, YELLOW)
        remark.move_to(DOWN * 3.1)
        self.play(Write(title), FadeIn(examples), run_time=1.1)
        self.play(Write(target), FadeIn(remark), run_time=0.9)
        self.wait(0.8)
        self.clear_stage(title, examples, target, remark)

    def show_prime_composite(self):
        title = self.text("先辨认素数与合数", 40, self.PRIMARY).move_to(UP * 5.4)
        prime = self.text("素数：大于 1，恰有两个正因数", 30, self.PRIME)
        prime.move_to(UP * 3.65)
        prime_examples = self.math(r"2,3,5,7,11,13,\ldots", 38, self.PRIME)
        prime_examples.move_to(UP * 2.25)
        composite = self.text("合数：大于 1，至少有三个正因数", 30, self.COMPOSITE)
        composite.move_to(UP * 0.5)
        composite_examples = self.math(r"4,6,8,9,10,12,\ldots", 38, self.COMPOSITE)
        composite_examples.move_to(DOWN * 0.8)
        exception = self.text("1 既不是素数也不是合数", 29, YELLOW)
        exception.move_to(DOWN * 2.9)
        self.play(Write(title), FadeIn(prime), run_time=0.8)
        self.play(Write(prime_examples), run_time=0.6)
        self.play(FadeIn(composite), Write(composite_examples), run_time=0.9)
        self.play(FadeIn(exception), run_time=0.5)
        self.wait(0.7)
        self.clear_stage(title, prime, prime_examples, composite, composite_examples, exception)

    def show_definition(self):
        title = self.text("什么是分解素因数？", 40, self.PRIMARY).move_to(UP * 5.4)
        definition = self.text("把合数写成素数乘积的形式", 32)
        definition.move_to(UP * 3.75)
        formula = self.math(r"30=2\times3\times5", 50, self.HIGHLIGHT)
        formula.move_to(UP * 1.7)
        individual = VGroup(*(
            self.math(fr"{p}\text{{ 是素数}}", 31, self.PRIME)
            for p in self.prime_factors(30)
        )).arrange(DOWN, buff=0.42).move_to(DOWN * 0.7)
        uniqueness = self.text("不计因数的顺序，素因数分解唯一", 28, YELLOW)
        uniqueness.move_to(DOWN * 3.7)
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        self.play(Write(formula), run_time=0.7)
        self.play(FadeIn(individual), run_time=0.7)
        self.play(FadeIn(uniqueness), run_time=0.6)
        self.wait(0.8)
        self.clear_stage(title, definition, formula, individual, uniqueness)

    def draw_short_division(self, number, title_text):
        """同一分解数据逐行构造左侧素因数及右侧连续整数商。"""
        rows = self.short_division_steps(number)
        factors = self.prime_factors(number)
        title = self.text(title_text, 40, self.DIVISOR).move_to(UP * 5.4)
        prompt = self.text("每次用素数整除，商写在下一行", 27)
        prompt.move_to(UP * 4.25)
        self.play(Write(title), FadeIn(prompt), run_time=0.8)
        current_numbers = VGroup(self.math(str(number), 41).move_to((0.6, 3.1, 0)))
        divisors, strokes, row_notes = VGroup(), VGroup(), VGroup()
        self.play(FadeIn(current_numbers[0]), run_time=0.4)
        for index, (dividend, divisor, quotient) in enumerate(rows):
            y = 3.1 - index * 0.8
            left = self.math(str(divisor), 38, self.DIVISOR).move_to((-0.9, y, 0))
            hline = Line((-1.45, y - 0.39, 0), (1.35, y - 0.39, 0),
                         stroke_width=2, color=GRAY_B)
            vline = Line((-0.15, y + 0.30, 0), (-0.15, y - 0.39, 0),
                         stroke_width=2, color=GRAY_B)
            next_number = self.math(str(quotient), 40,
                                    self.HIGHLIGHT if quotient == 1 else WHITE)
            next_number.move_to((0.6, y - 0.8, 0))
            # 被除数由上一行出现的同一 MathTex 对象呈现。
            divisors.add(left)
            strokes.add(hline, vline)
            current_numbers.add(next_number)
            self.play(FadeIn(left), Create(hline), Create(vline),
                      FadeIn(next_number), run_time=0.65)
        end_note = self.text("商为 1，短除法结束", 27, self.HIGHLIGHT)
        end_note.move_to(DOWN * 1.65)
        result_tex = str(number) + "=" + "\\times".join(str(p) for p in factors)
        product = self.math(result_tex, 40, self.HIGHLIGHT).move_to(DOWN * 2.85)
        # 检查每个短除法行均满足 被除数=素因数×整数商。
        verification_tex = r"\quad ".join(
            fr"{dividend}={divisor}\times{quotient}"
            for dividend, divisor, quotient in rows
        )
        verification = self.math(verification_tex, 27, GRAY_A)
        verification.move_to(DOWN * 4)
        self.play(FadeIn(end_note), Write(product), run_time=0.8)
        self.play(FadeIn(verification), run_time=0.6)
        self.wait(1)
        self.clear_stage(title, prompt, current_numbers, divisors, strokes,
                         row_notes, end_note, product, verification)

    def show_division_30(self):
        self.draw_short_division(30, "短除法：30")

    def show_division_60(self):
        self.draw_short_division(60, "短除法：60")
        result = self.math(r"60=2^2\times3\times5", 44, self.HIGHLIGHT)
        result.move_to(UP * 1.8)
        description = self.text("相同素因数可合并成指数形式", 28)
        description.move_to(DOWN * 0.2)
        self.play(Write(result), FadeIn(description), run_time=0.9)
        self.wait(0.9)
        self.clear_stage(result, description)

    def show_summary(self):
        title = self.text("短除法步骤", 40, self.PRIMARY).move_to(UP * 5.4)
        steps = VGroup(
            self.text("① 从最小素数 2 开始尝试", 28),
            self.text("② 能整除就除，并写下这个素因数", 28),
            self.text("③ 对所得的商继续分解", 28),
            self.text("④ 商为 1 时停止", 28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.76).move_to(UP * 1.45)
        example = self.math(r"60=2^2\times3\times5", 43, self.HIGHLIGHT)
        example.move_to(DOWN * 2.55)
        reminder = self.text("合数分解为素数乘积，不计顺序结果唯一", 26)
        reminder.move_to(DOWN * 4)
        self.play(Write(title), run_time=0.7)
        for step in steps:
            self.play(FadeIn(step), run_time=0.5)
        self.play(Write(example), FadeIn(reminder), run_time=0.9)
        self.wait(0.9)
        self.clear_stage(title, steps, example, reminder, self.author_info)
