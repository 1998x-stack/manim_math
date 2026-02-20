"""
韦达定理（根与系数的关系）- Vieta's Formulas
使用 Manim 创建的中学数学教学视频

内容: 一元二次方程的根与系数关系及其应用
目标观众: 八年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class VietaFormulas(Scene):
    """
    韦达定理教学动画
    
    场景顺序:
    1. 开场钩子
    2. 韦达定理介绍
    3. 公式推导（简化版）
    4. 例题1: 已知方程求和积
    5. 例题2: 已知两根求方程
    6. 例题3: 对称式计算
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主公式
        self.COLOR_ROOT_1 = "#e74c3c"         # 红色 - x₁
        self.COLOR_ROOT_2 = "#2ecc71"         # 绿色 - x₂
        self.COLOR_SUM = "#f39c12"            # 橙色 - 和式
        self.COLOR_PRODUCT = "#9b59b6"        # 紫色 - 积式
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        
        # 执行动画序列
        self.show_opening()
        self.show_vieta_intro()
        self.show_derivation()
        self.show_example_1()
        self.show_example_2()
        self.show_example_3()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 6.3)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "不解方程\n如何求两根之和与积?",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(UP * 4.8)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.3)
        
        # 方程出现
        equation = MathTex(
            r"x^2 - 5x + 6 = 0",
            font_size=44,
            color=WHITE
        ).move_to(UP * 2.8)
        
        self.play(Write(equation), run_time=0.8)
        
        # 问号闪烁
        question_mark = Text(
            "?",
            font_size=80,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(question_mark, scale=1.5), run_time=0.5)
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT), run_time=0.4)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(equation),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def show_vieta_intro(self):
        """场景2: 韦达定理介绍"""
        # 标题
        title = Text(
            "韦达定理",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 标准形式
        standard_form = MathTex(
            r"ax^2 + bx + c = 0",
            font_size=40
        ).move_to(UP * 4.5)
        
        constraint = MathTex(
            r"(a \neq 0)",
            font_size=32,
            color=self.COLOR_AUXILIARY
        ).next_to(standard_form, RIGHT, buff=0.3)
        
        self.play(Write(standard_form), run_time=0.8)
        self.play(FadeIn(constraint), run_time=0.4)
        
        # 两根标记
        root_text = Text(
            "若两根为：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 3.5 + LEFT * 2)
        
        root_labels = MathTex(
            r"x_1", r",", r"x_2",
            font_size=36
        ).next_to(root_text, RIGHT, buff=0.3)
        
        root_labels[0].set_color(self.COLOR_ROOT_1)
        root_labels[2].set_color(self.COLOR_ROOT_2)
        
        self.play(
            FadeIn(root_text),
            FadeIn(root_labels),
            run_time=0.8
        )
        self.wait(0.4)
        
        # 核心公式 - 和
        then_text = Text(
            "则有：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 2.3 + LEFT * 3)
        
        self.play(FadeIn(then_text), run_time=0.4)
        
        self.formula_sum = MathTex(
            r"x_1", r"+", r"x_2", r"=", r"-\frac{b}{a}",
            font_size=46
        ).move_to(UP * 1.5)
        
        self.formula_sum[0].set_color(self.COLOR_ROOT_1)
        self.formula_sum[2].set_color(self.COLOR_ROOT_2)
        self.formula_sum[4].set_color(self.COLOR_SUM)
        
        self.play(FadeIn(self.formula_sum, shift=UP * 0.3), run_time=1.0)
        
        # 核心公式 - 积
        self.formula_product = MathTex(
            r"x_1", r"\times", r"x_2", r"=", r"\frac{c}{a}",
            font_size=46
        ).move_to(UP * 0.3)
        
        self.formula_product[0].set_color(self.COLOR_ROOT_1)
        self.formula_product[2].set_color(self.COLOR_ROOT_2)
        self.formula_product[4].set_color(self.COLOR_PRODUCT)
        
        self.play(FadeIn(self.formula_product, shift=UP * 0.3), run_time=1.0)
        
        # 框选两个公式
        formulas_group = VGroup(self.formula_sum, self.formula_product)
        surrounding_box = SurroundingRectangle(
            formulas_group,
            color=self.COLOR_HIGHLIGHT,
            buff=0.4,
            stroke_width=3
        )
        
        self.play(Create(surrounding_box), run_time=1.0)
        self.wait(0.5)
        
        # 说明文字
        explanation = Text(
            "根与系数的关系",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 1.2)
        
        self.play(FadeIn(explanation), run_time=0.5)
        self.wait(1.0)
        
        # 清理并保留参考公式
        self.play(
            FadeOut(title),
            FadeOut(standard_form),
            FadeOut(constraint),
            FadeOut(root_text),
            FadeOut(root_labels),
            FadeOut(then_text),
            FadeOut(surrounding_box),
            FadeOut(explanation),
            run_time=0.6
        )
        
        # 将公式移到顶部作为参考
        self.reference_formulas = VGroup(
            self.formula_sum.copy(),
            self.formula_product.copy()
        ).arrange(DOWN, buff=0.15).scale(0.55).move_to(UP * 6 + LEFT * 1.5)
        
        self.play(
            Transform(self.formula_sum, self.reference_formulas[0]),
            Transform(self.formula_product, self.reference_formulas[1]),
            run_time=0.6
        )
        self.remove(self.formula_sum, self.formula_product)
        self.add(self.reference_formulas)
    
    def show_derivation(self):
        """场景3: 公式推导（简化版）"""
        # 副标题
        subtitle = Text(
            "公式推导",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5)
        
        self.play(Write(subtitle), run_time=0.5)
        
        # 求根公式
        quadratic_formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}",
            font_size=38
        ).move_to(UP * 4)
        
        self.play(Write(quadratic_formula), run_time=1.0)
        self.wait(0.5)
        
        # 两根表示
        root_1 = MathTex(
            r"x_1 = \frac{-b + \sqrt{b^2-4ac}}{2a}",
            font_size=34
        ).move_to(UP * 2.8)
        root_1[0][:2].set_color(self.COLOR_ROOT_1)
        
        root_2 = MathTex(
            r"x_2 = \frac{-b - \sqrt{b^2-4ac}}{2a}",
            font_size=34
        ).move_to(UP * 1.8)
        root_2[0][:2].set_color(self.COLOR_ROOT_2)
        
        self.play(
            TransformMatchingTex(quadratic_formula.copy(), root_1),
            run_time=1.0
        )
        self.play(
            FadeIn(root_2, shift=UP * 0.3),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 推导和
        sum_title = Text(
            "两根之和：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SUM
        ).move_to(UP * 0.5 + LEFT * 3)
        
        self.play(FadeIn(sum_title), run_time=0.4)
        
        sum_step1 = MathTex(
            r"x_1 + x_2 = \frac{-b+\sqrt{b^2-4ac}}{2a} + \frac{-b-\sqrt{b^2-4ac}}{2a}",
            font_size=28
        ).move_to(UP * 0)
        
        sum_step2 = MathTex(
            r"x_1 + x_2 = \frac{-2b}{2a}",
            font_size=32
        ).move_to(DOWN * 0.8)
        
        sum_step3 = MathTex(
            r"x_1 + x_2 = -\frac{b}{a}",
            font_size=36
        ).move_to(DOWN * 1.6)
        sum_step3[0][:2].set_color(self.COLOR_ROOT_1)
        sum_step3[0][3:5].set_color(self.COLOR_ROOT_2)
        sum_step3[0][6:].set_color(self.COLOR_SUM)
        
        self.play(Write(sum_step1), run_time=1.2)
        self.wait(0.3)
        self.play(TransformMatchingTex(sum_step1.copy(), sum_step2), run_time=1.0)
        self.wait(0.3)
        self.play(TransformMatchingTex(sum_step2.copy(), sum_step3), run_time=1.0)
        self.play(Indicate(sum_step3, color=self.COLOR_SUM), run_time=0.6)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(quadratic_formula),
            FadeOut(root_1),
            FadeOut(root_2),
            FadeOut(sum_title),
            FadeOut(sum_step1),
            FadeOut(sum_step2),
            FadeOut(sum_step3),
            run_time=0.6
        )
    
    def show_example_1(self):
        """场景4: 例题1 - 已知方程求和积"""
        # 副标题
        subtitle = Text(
            "例题1：求两根之和与积",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5)
        
        self.play(Write(subtitle), run_time=0.5)
        
        # 方程
        equation = MathTex(
            r"x^2", r"-", r"7x", r"+", r"12", r"=", r"0",
            font_size=44
        ).move_to(UP * 4)
        
        self.play(Write(equation), run_time=0.7)
        self.wait(0.3)
        
        # 标注系数
        brace_a = Brace(equation[0], DOWN, buff=0.1)
        label_a = MathTex(r"a=1", font_size=24).next_to(brace_a, DOWN, buff=0.1)
        
        brace_b = Brace(equation[2], DOWN, buff=0.1)
        label_b = MathTex(r"b=-7", font_size=24).next_to(brace_b, DOWN, buff=0.1)
        
        brace_c = Brace(equation[4], DOWN, buff=0.1)
        label_c = MathTex(r"c=12", font_size=24).next_to(brace_c, DOWN, buff=0.1)
        
        self.play(
            FadeIn(brace_a), FadeIn(label_a),
            FadeIn(brace_b), FadeIn(label_b),
            FadeIn(brace_c), FadeIn(label_c),
            run_time=1.2
        )
        self.wait(0.5)
        
        # 计算和
        sum_calc = VGroup(
            MathTex(r"x_1 + x_2 = -\frac{b}{a}", font_size=36),
            MathTex(r"= -\frac{(-7)}{1}", font_size=36),
            MathTex(r"= 7", font_size=40, color=self.COLOR_SUM)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(UP * 1.8)
        
        for step in sum_calc:
            self.play(Write(step), run_time=0.8)
        
        self.play(Indicate(sum_calc[2], color=self.COLOR_SUM), run_time=0.6)
        self.wait(0.5)
        
        # 计算积
        product_calc = VGroup(
            MathTex(r"x_1 \times x_2 = \frac{c}{a}", font_size=36),
            MathTex(r"= \frac{12}{1}", font_size=36),
            MathTex(r"= 12", font_size=40, color=self.COLOR_PRODUCT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(DOWN * 0.8)
        
        for step in product_calc:
            self.play(Write(step), run_time=0.8)
        
        self.play(Indicate(product_calc[2], color=self.COLOR_PRODUCT), run_time=0.6)
        self.wait(0.5)
        
        # 答案框
        answer = VGroup(
            Text("答：", font="Noto Sans CJK SC", font_size=self.FONT_BODY),
            MathTex(r"x_1 + x_2 = 7,\ x_1 \times x_2 = 12", font_size=32)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 3.5)
        
        answer_box = SurroundingRectangle(answer, color=YELLOW, buff=0.2)
        
        self.play(FadeIn(answer), Create(answer_box), run_time=0.8)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(equation),
            FadeOut(brace_a), FadeOut(label_a),
            FadeOut(brace_b), FadeOut(label_b),
            FadeOut(brace_c), FadeOut(label_c),
            FadeOut(sum_calc),
            FadeOut(product_calc),
            FadeOut(answer),
            FadeOut(answer_box),
            run_time=0.6
        )
    
    def show_example_2(self):
        """场景5: 例题2 - 已知两根求方程"""
        # 副标题
        subtitle = Text(
            "例题2：已知两根，求方程",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5)
        
        self.play(Write(subtitle), run_time=0.5)
        
        # 已知条件
        given = VGroup(
            Text("已知：", font="Noto Sans CJK SC", font_size=self.FONT_BODY),
            MathTex(r"x_1 = 3,\ x_2 = 4", font_size=36)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 4)
        
        given[1][0][:2].set_color(self.COLOR_ROOT_1)
        given[1][0][6:8].set_color(self.COLOR_ROOT_2)
        
        self.play(FadeIn(given), run_time=0.8)
        self.wait(0.3)
        
        # 计算和与积
        sum_calc = MathTex(
            r"x_1 + x_2 = 3 + 4 = 7",
            font_size=34
        ).move_to(UP * 2.8)
        sum_calc[0][:2].set_color(self.COLOR_ROOT_1)
        sum_calc[0][3:5].set_color(self.COLOR_ROOT_2)
        sum_calc[0][-1].set_color(self.COLOR_SUM)
        
        product_calc = MathTex(
            r"x_1 \times x_2 = 3 \times 4 = 12",
            font_size=34
        ).move_to(UP * 1.8)
        product_calc[0][:2].set_color(self.COLOR_ROOT_1)
        product_calc[0][3:5].set_color(self.COLOR_ROOT_2)
        product_calc[0][-2:].set_color(self.COLOR_PRODUCT)
        
        self.play(Write(sum_calc), run_time=1.0)
        self.wait(0.3)
        self.play(Write(product_calc), run_time=1.0)
        self.wait(0.5)
        
        # 反推公式
        reverse_title = Text(
            "构造方程：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5 + LEFT * 2.5)
        
        self.play(FadeIn(reverse_title), run_time=0.4)
        
        reverse_formula = MathTex(
            r"x^2 - (x_1+x_2)x + x_1 \times x_2 = 0",
            font_size=32
        ).move_to(UP * 0)
        
        self.play(Write(reverse_formula), run_time=1.2)
        self.wait(0.5)
        
        # 代入数值
        substitution = MathTex(
            r"x^2 - 7x + 12 = 0",
            font_size=40
        ).move_to(DOWN * 1.2)
        
        self.play(TransformMatchingTex(reverse_formula.copy(), substitution), run_time=1.0)
        
        # 答案框
        answer_box = SurroundingRectangle(substitution, color=YELLOW, buff=0.25)
        self.play(Create(answer_box), run_time=0.6)
        
        # 验证标记
        check_mark = Text(
            "✓",
            font_size=50,
            color=GREEN
        ).next_to(answer_box, RIGHT, buff=0.3)
        
        self.play(FadeIn(check_mark, scale=1.5), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(given),
            FadeOut(sum_calc),
            FadeOut(product_calc),
            FadeOut(reverse_title),
            FadeOut(reverse_formula),
            FadeOut(substitution),
            FadeOut(answer_box),
            FadeOut(check_mark),
            run_time=0.6
        )
    
    def show_example_3(self):
        """场景6: 例题3 - 对称式计算"""
        # 副标题
        subtitle = Text(
            "例题3：对称式计算",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5)
        
        self.play(Write(subtitle), run_time=0.5)
        
        # 方程
        equation = MathTex(
            r"x^2 - 5x + 3 = 0",
            font_size=40
        ).move_to(UP * 4.2)
        
        self.play(Write(equation), run_time=0.7)
        
        # 求解目标
        target = VGroup(
            Text("求：", font="Noto Sans CJK SC", font_size=self.FONT_BODY),
            MathTex(r"x_1^2 + x_2^2", font_size=38)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 3.2)
        
        target[1][0][:3].set_color(self.COLOR_ROOT_1)
        target[1][0][4:].set_color(self.COLOR_ROOT_2)
        
        self.play(FadeIn(target), run_time=0.7)
        self.wait(0.3)
        
        # 技巧公式
        trick_title = Text(
            "技巧：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2 + LEFT * 3)
        
        identity = MathTex(
            r"x_1^2 + x_2^2 = (x_1+x_2)^2 - 2x_1 x_2",
            font_size=34
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(trick_title), run_time=0.4)
        self.play(FadeIn(identity, shift=UP * 0.3), run_time=1.0)
        self.play(Indicate(identity, color=self.COLOR_HIGHLIGHT), run_time=0.8)
        self.wait(0.5)
        
        # 从韦达定理得到
        vieta_values = VGroup(
            MathTex(r"x_1 + x_2 = 5", font_size=32),
            MathTex(r"x_1 \times x_2 = 3", font_size=32)
        ).arrange(RIGHT, buff=1.5).move_to(UP * 0.3)
        
        vieta_values[0][0][:2].set_color(self.COLOR_ROOT_1)
        vieta_values[0][0][3:5].set_color(self.COLOR_ROOT_2)
        vieta_values[1][0][:2].set_color(self.COLOR_ROOT_1)
        vieta_values[1][0][3:5].set_color(self.COLOR_ROOT_2)
        
        self.play(Write(vieta_values), run_time=1.0)
        self.wait(0.5)
        
        # 代入计算
        substitution = MathTex(
            r"x_1^2 + x_2^2 = 5^2 - 2 \times 3",
            font_size=36
        ).move_to(DOWN * 1)
        
        self.play(TransformMatchingTex(identity.copy(), substitution), run_time=1.0)
        self.wait(0.3)
        
        calculation = MathTex(
            r"= 25 - 6",
            font_size=36
        ).move_to(DOWN * 1.8)
        
        self.play(Write(calculation), run_time=0.8)
        self.wait(0.3)
        
        final_answer = MathTex(
            r"= 19",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.8)
        
        self.play(Write(final_answer), run_time=0.8)
        self.play(
            Indicate(final_answer, color=YELLOW, scale_factor=1.2),
            run_time=0.8
        )
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(equation),
            FadeOut(target),
            FadeOut(trick_title),
            FadeOut(identity),
            FadeOut(vieta_values),
            FadeOut(substitution),
            FadeOut(calculation),
            FadeOut(final_answer),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结与片尾"""
        # 标题
        title = Text(
            "韦达定理总结",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 三个应用场景
        applications = VGroup(
            VGroup(
                Text("✓", font_size=40, color=GREEN),
                Text("求两根之和与积", font="Noto Sans CJK SC", font_size=26)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("✓", font_size=40, color=GREEN),
                Text("已知两根构造方程", font="Noto Sans CJK SC", font_size=26)
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("✓", font_size=40, color=GREEN),
                Text("计算对称式", font="Noto Sans CJK SC", font_size=26)
            ).arrange(RIGHT, buff=0.3)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).move_to(UP * 2.5)
        
        for app in applications:
            self.play(FadeIn(app, shift=UP * 0.2), run_time=0.6)
            self.wait(0.4)
        
        # 关键提示
        key_point = Text(
            "韦达定理 = 不解方程的神器",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(ORIGIN)
        
        self.play(FadeIn(key_point, shift=UP * 0.3, scale=1.1), run_time=0.8)
        self.wait(1.0)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=38,
            color=WHITE
        ).move_to(DOWN * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=30,
            color=GRAY_B
        ).move_to(DOWN * 2.8)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        
        # 装饰符号
        symbols = VGroup(
            MathTex(r"x_1", font_size=35, color=self.COLOR_ROOT_1),
            MathTex(r"x_2", font_size=35, color=self.COLOR_ROOT_2),
            MathTex(r"+", font_size=35, color=self.COLOR_SUM),
            MathTex(r"\times", font_size=35, color=self.COLOR_PRODUCT),
        ).arrange(RIGHT, buff=1).move_to(DOWN * 5.5)
        
        self.play(*[FadeIn(sym, scale=0.5) for sym in symbols], run_time=0.6)
        self.play(Rotate(symbols, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(title),
            FadeOut(applications),
            FadeOut(key_point),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(symbols),
            FadeOut(self.reference_formulas),
            run_time=1.0
        )


# 运行命令:
# manim -pql vieta_formulas.py VietaFormulas  # 快速预览
# manim -qh vieta_formulas.py VietaFormulas   # 高质量渲染