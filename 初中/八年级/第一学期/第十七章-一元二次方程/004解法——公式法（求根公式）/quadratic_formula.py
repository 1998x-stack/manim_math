"""
求根公式（公式法）- Manim 教学动画
Quadratic Formula for Solving Quadratic Equations

目标受众: 八年级学生
视频格式: TikTok 竖屏 (1080×1920)
时长: 65-80秒

作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ==================== 全局配置 ====================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class QuadraticFormula(Scene):
    """
    求根公式教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 介绍求根公式
    3. 判别式详解
    4. 使用步骤
    5. 实例演示1 - x² + 5x + 6 = 0
    6. 实例演示2 - 2x² + 5x - 3 = 0
    7. 总结与关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主公式
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 判别式
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助
        self.COLOR_SUCCESS = "#2ecc71"        # 绿色 - 正确答案
        self.COLOR_WARNING = "#f39c12"        # 橙色 - 警告
        
        # 字体配置
        self.FONT_CHINESE = "Noto Sans CJK SC"
        self.FONT_SIZE_TITLE = 38
        self.FONT_SIZE_SUBTITLE = 28
        self.FONT_SIZE_BODY = 24
        self.FONT_SIZE_SMALL = 20
        self.FONT_SIZE_FORMULA = 30
        
        # 执行动画序列
        self.show_opening()
        self.show_formula_introduction()
        self.show_discriminant()
        self.show_steps()
        self.show_example_1()
        self.show_example_2()
        self.show_summary()
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息 (顶部固定)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子方程
        hook_equation = MathTex(
            r"2x^2 + 5x - 3 = 0",
            font_size=52,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4)
        
        question_text = Text(
            "怎么解？",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=WHITE
        ).next_to(hook_equation, DOWN, buff=0.5)
        
        self.play(Write(hook_equation), run_time=1.0)
        self.play(FadeIn(question_text, shift=UP * 0.2), run_time=0.5)
        
        # 问号动画
        question_mark = Text(
            "?",
            font=self.FONT_CHINESE,
            font_size=60,
            color=self.COLOR_HIGHLIGHT
        ).move_to(RIGHT * 2.5 + UP * 3)
        
        self.play(FadeIn(question_mark, scale=0.5), run_time=0.4)
        self.play(Flash(question_mark, color=self.COLOR_HIGHLIGHT, flash_radius=0.4), run_time=0.4)
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_equation),
            FadeOut(question_text),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def show_formula_introduction(self):
        """场景2: 介绍求根公式 (5-15秒)"""
        # 标题
        title = Text(
            "求根公式（公式法）",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6)
        
        subtitle = Text(
            "Quadratic Formula",
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A,
            slant=ITALIC
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 标准形式
        standard_form = MathTex(
            r"ax^2 + bx + c = 0",
            font_size=self.FONT_SIZE_FORMULA,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(standard_form), run_time=0.8)
        self.wait(0.4)
        
        # 核心公式框
        formula_box = RoundedRectangle(
            width=7.0,
            height=1.8,
            corner_radius=0.15,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_to(UP * 2.8)
        
        self.play(Create(formula_box), run_time=0.6)
        
        # 求根公式
        formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=self.FONT_SIZE_FORMULA + 6,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2.8)
        
        self.play(Write(formula), run_time=1.5)
        self.wait(0.5)
        
        # 条件框
        condition_box = RoundedRectangle(
            width=4.5,
            height=1.2,
            corner_radius=0.1,
            color=self.COLOR_WARNING,
            fill_opacity=0.1
        ).move_to(UP * 1.0)
        
        condition_label = Text(
            "使用条件:",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=GRAY_A
        ).next_to(condition_box, UP, buff=0.15)
        
        condition_text = VGroup(
            MathTex(r"a \neq 0", font_size=self.FONT_SIZE_BODY, color=self.COLOR_WARNING),
            MathTex(r"b^2 - 4ac \geq 0", font_size=self.FONT_SIZE_BODY, color=self.COLOR_WARNING)
        ).arrange(DOWN, buff=0.2).move_to(condition_box.get_center())
        
        self.play(
            FadeIn(condition_box),
            FadeIn(condition_label),
            run_time=0.5
        )
        self.play(Write(condition_text), run_time=0.8)
        
        # 强调 a≠0
        self.play(
            Indicate(condition_text[0], scale_factor=1.2, color=self.COLOR_WARNING),
            run_time=0.6
        )
        self.wait(0.5)
        
        # 公式闪烁
        self.play(
            Flash(VGroup(formula_box, formula), color=self.COLOR_PRIMARY, flash_radius=0.5),
            run_time=0.6
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(standard_form),
            FadeOut(formula_box),
            FadeOut(formula),
            FadeOut(condition_box),
            FadeOut(condition_label),
            FadeOut(condition_text),
            run_time=0.6
        )
    
    def show_discriminant(self):
        """场景3: 判别式详解 (15-25秒)"""
        # 标题
        discriminant_title = Text(
            "判别式 Δ（Delta）",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(discriminant_title), run_time=0.8)
        
        # 判别式定义
        delta_definition = MathTex(
            r"\Delta = {{ b^2 - 4ac }}",
            font_size=self.FONT_SIZE_FORMULA + 4,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 4.8)
        
        self.play(Write(delta_definition), run_time=1.0)
        
        # 高亮根号内部分
        sqrt_part = delta_definition.get_part_by_tex(r"b^2 - 4ac")
        self.play(
            Indicate(sqrt_part, scale_factor=1.15, color=self.COLOR_HIGHLIGHT),
            run_time=0.7
        )
        self.wait(0.4)
        
        # 三种情况
        cases_y_start = 3.0
        case_spacing = 1.8
        
        # 情况1: Δ > 0
        case1_box = self.create_case_box(
            condition=r"\Delta > 0",
            result="两个不等实根",
            color=self.COLOR_SUCCESS,
            position=UP * cases_y_start
        )
        
        self.play(FadeIn(case1_box, shift=LEFT * 0.5), run_time=0.5)
        self.wait(0.3)
        
        # 情况2: Δ = 0
        case2_box = self.create_case_box(
            condition=r"\Delta = 0",
            result="两个相等实根",
            color=self.COLOR_WARNING,
            position=UP * (cases_y_start - case_spacing)
        )
        
        self.play(FadeIn(case2_box, shift=LEFT * 0.5), run_time=0.5)
        self.wait(0.3)
        
        # 情况3: Δ < 0
        case3_box = self.create_case_box(
            condition=r"\Delta < 0",
            result="无实数根",
            color=GRAY,
            position=UP * (cases_y_start - 2 * case_spacing)
        )
        
        self.play(FadeIn(case3_box, shift=LEFT * 0.5), run_time=0.5)
        self.wait(0.5)
        
        # 整体闪烁
        all_cases = VGroup(case1_box, case2_box, case3_box)
        self.play(
            Flash(all_cases, color=self.COLOR_SECONDARY, flash_radius=0.4),
            run_time=0.6
        )
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(discriminant_title),
            FadeOut(delta_definition),
            FadeOut(all_cases),
            run_time=0.6
        )
    
    def create_case_box(self, condition, result, color, position):
        """创建判别式情况框"""
        box = RoundedRectangle(
            width=6.5,
            height=0.8,
            corner_radius=0.1,
            color=color,
            fill_opacity=0.1,
            stroke_width=2
        ).move_to(position)
        
        condition_tex = MathTex(
            condition,
            font_size=self.FONT_SIZE_BODY,
            color=color
        ).move_to(box.get_center() + LEFT * 1.8)
        
        arrow = Arrow(
            start=ORIGIN,
            end=RIGHT * 0.6,
            color=color,
            stroke_width=3,
            buff=0
        ).move_to(box.get_center() + LEFT * 0.3)
        
        result_text = Text(
            result,
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SMALL,
            color=color
        ).move_to(box.get_center() + RIGHT * 1.5)
        
        return VGroup(box, condition_tex, arrow, result_text)
    
    def show_steps(self):
        """场景4: 使用步骤 (25-35秒)"""
        # 标题
        steps_title = Text(
            "使用步骤",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(steps_title), run_time=0.7)
        
        # 步骤卡片
        step1 = self.create_step_card(
            number="1",
            content="确定 a, b, c 的值",
            position=UP * 4.0
        )
        
        step2 = self.create_step_card(
            number="2",
            content="计算判别式 Δ = b²-4ac",
            position=UP * 2.5
        )
        
        step3 = self.create_step_card(
            number="3",
            content="代入公式计算",
            position=UP * 1.0
        )
        
        step4 = self.create_step_card(
            number="4",
            content="化简得出答案",
            position=DOWN * 0.5
        )
        
        # 依次滑入
        for step in [step1, step2, step3, step4]:
            self.play(FadeIn(step, shift=RIGHT * 0.5), run_time=0.5)
            self.wait(0.2)
        
        all_steps = VGroup(step1, step2, step3, step4)
        self.play(
            Flash(all_steps, color=self.COLOR_PRIMARY, flash_radius=0.4),
            run_time=0.6
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(steps_title),
            FadeOut(all_steps),
            run_time=0.6
        )
    
    def create_step_card(self, number, content, position):
        """创建步骤卡片"""
        # 编号圆
        circle = Circle(
            radius=0.25,
            color=self.COLOR_PRIMARY,
            fill_opacity=1,
            stroke_width=0
        )
        
        number_text = Text(
            number,
            font=self.FONT_CHINESE,
            font_size=22,
            color=WHITE,
            weight=BOLD
        ).move_to(circle.get_center())
        
        number_group = VGroup(circle, number_text)
        
        # 内容文字
        content_text = Text(
            content,
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=WHITE
        )
        
        # 组合
        card = VGroup(number_group, content_text).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def show_example_1(self):
        """场景5: 实例演示1 - x² + 5x + 6 = 0 (35-48秒)"""
        # 例题标签
        example_label = Text(
            "例题 1",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(example_label), run_time=0.5)
        
        # 方程
        equation = MathTex(
            r"x^2 + 5x + 6 = 0",
            font_size=self.FONT_SIZE_FORMULA + 2,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(equation), run_time=0.8)
        self.wait(0.3)
        
        # 识别系数
        coefficients = MathTex(
            r"a = {{ 1 }}, \quad b = {{ 5 }}, \quad c = {{ 6 }}",
            font_size=self.FONT_SIZE_BODY,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(coefficients), run_time=0.8)
        
        # 逐个高亮系数
        a_value = coefficients.get_part_by_tex("1")
        b_value = coefficients.get_part_by_tex("5")
        c_value = coefficients.get_part_by_tex("6")
        
        for value in [a_value, b_value, c_value]:
            self.play(Indicate(value, scale_factor=1.2, color=self.COLOR_HIGHLIGHT), run_time=0.4)
        
        self.wait(0.3)
        
        # 计算判别式
        delta_label = Text(
            "计算 Δ:",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(UP * 3.3)
        
        delta_calc = MathTex(
            r"\Delta = 5^2 - 4 \times 1 \times 6 = 25 - 24 = {{ 1 }}",
            font_size=self.FONT_SIZE_BODY,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 2.6)
        
        self.play(FadeIn(delta_label, shift=DOWN * 0.2), run_time=0.3)
        self.play(Write(delta_calc), run_time=1.0)
        
        # 高亮结果
        delta_result = delta_calc.get_part_by_tex("1")
        self.play(Indicate(delta_result, scale_factor=1.3, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        self.wait(0.3)
        
        # 代入公式
        substitution = MathTex(
            r"x = \frac{-5 \pm \sqrt{1}}{2 \times 1}",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 1.3)
        
        self.play(Write(substitution), run_time=1.0)
        self.wait(0.4)
        
        # 简化
        simplified = MathTex(
            r"x = \frac{-5 \pm 1}{2}",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 0.2)
        
        self.play(TransformMatchingTex(substitution.copy(), simplified), run_time=1.0)
        self.wait(0.3)
        
        # 最终答案
        answers = MathTex(
            r"x_1 = -2, \quad x_2 = -3",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 1.2)
        
        self.play(Write(answers), run_time=0.8)
        
        # 答案框
        answer_rect = SurroundingRectangle(
            answers,
            color=self.COLOR_SUCCESS,
            buff=0.25,
            corner_radius=0.1
        )
        
        self.play(Create(answer_rect), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(example_label),
            FadeOut(equation),
            FadeOut(coefficients),
            FadeOut(delta_label),
            FadeOut(delta_calc),
            FadeOut(substitution),
            FadeOut(simplified),
            FadeOut(answers),
            FadeOut(answer_rect),
            run_time=0.6
        )
    
    def show_example_2(self):
        """场景6: 实例演示2 - 2x² + 5x - 3 = 0 (48-60秒)"""
        # 例题标签
        example_label = Text(
            "例题 2",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_SUBTITLE,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(example_label), run_time=0.5)
        
        # 方程
        equation = MathTex(
            r"2x^2 + 5x - 3 = 0",
            font_size=self.FONT_SIZE_FORMULA + 2,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(equation), run_time=0.8)
        self.wait(0.3)
        
        # 识别系数
        coefficients = MathTex(
            r"a = {{ 2 }}, \quad b = {{ 5 }}, \quad c = {{ -3 }}",
            font_size=self.FONT_SIZE_BODY,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(coefficients), run_time=0.8)
        
        # 高亮所有系数
        self.play(
            Indicate(coefficients, scale_factor=1.1, color=self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        self.wait(0.3)
        
        # 计算判别式
        delta_label = Text(
            "计算 Δ:",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY,
            color=GRAY_A
        ).move_to(UP * 3.3)
        
        delta_calc = MathTex(
            r"\Delta = 5^2 - 4 \times 2 \times (-3) = 25 + 24 = {{ 49 }}",
            font_size=self.FONT_SIZE_BODY - 2,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 2.6)
        
        self.play(FadeIn(delta_label, shift=DOWN * 0.2), run_time=0.3)
        self.play(Write(delta_calc), run_time=1.0)
        
        # 高亮结果
        delta_result = delta_calc.get_part_by_tex("49")
        self.play(Indicate(delta_result, scale_factor=1.3, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        self.wait(0.3)
        
        # 代入公式
        substitution = MathTex(
            r"x = \frac{-5 \pm \sqrt{49}}{2 \times 2}",
            font_size=self.FONT_SIZE_FORMULA - 2,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 1.3)
        
        self.play(Write(substitution), run_time=1.0)
        self.wait(0.4)
        
        # 计算根号
        sqrt_step = MathTex(
            r"x = \frac{-5 \pm 7}{4}",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 0.2)
        
        self.play(TransformMatchingTex(substitution.copy(), sqrt_step), run_time=1.0)
        self.wait(0.3)
        
        # 最终答案
        answers = MathTex(
            r"x_1 = \frac{1}{2}, \quad x_2 = -3",
            font_size=self.FONT_SIZE_FORMULA,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 1.2)
        
        self.play(Write(answers), run_time=0.8)
        
        # 答案框
        answer_rect = SurroundingRectangle(
            answers,
            color=self.COLOR_SUCCESS,
            buff=0.25,
            corner_radius=0.1
        )
        
        self.play(Create(answer_rect), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(example_label),
            FadeOut(equation),
            FadeOut(coefficients),
            FadeOut(delta_label),
            FadeOut(delta_calc),
            FadeOut(substitution),
            FadeOut(sqrt_step),
            FadeOut(answers),
            FadeOut(answer_rect),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结与关注 (60-80秒)"""
        # 总结标题
        summary_title = Text(
            "总结要点",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_TITLE,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 公式回顾
        formula_recap = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=self.FONT_SIZE_FORMULA + 2,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 4.5)
        
        self.play(Write(formula_recap), run_time=1.0)
        self.wait(0.5)
        
        # 要点1
        point1 = VGroup(
            Circle(radius=0.12, color=self.COLOR_PRIMARY, fill_opacity=1),
            Text(
                "先算判别式 Δ = b²-4ac",
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_BODY - 2,
                color=WHITE
            ).shift(RIGHT * 1.5)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.8)
        point1.shift(LEFT * 10)
        
        # 要点2
        point2 = VGroup(
            Circle(radius=0.12, color=self.COLOR_PRIMARY, fill_opacity=1),
            Text(
                "Δ ≥ 0 才有实数根",
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_BODY - 2,
                color=WHITE
            ).shift(RIGHT * 1.5)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1.5)
        point2.shift(LEFT * 10)
        
        # 要点3
        point3 = VGroup(
            Circle(radius=0.12, color=self.COLOR_PRIMARY, fill_opacity=1),
            Text(
                "记住 ± 号，两个解",
                font=self.FONT_CHINESE,
                font_size=self.FONT_SIZE_BODY - 2,
                color=WHITE
            ).shift(RIGHT * 1.5)
        ).arrange(RIGHT, buff=0.3).move_to(UP * 0.2)
        point3.shift(LEFT * 10)
        
        # 依次滑入
        self.play(point1.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(point2.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(point3.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.5)
        
        # 整体闪烁
        all_points = VGroup(point1, point2, point3)
        self.play(
            Flash(all_points, color=self.COLOR_PRIMARY, flash_radius=0.5),
            run_time=0.6
        )
        self.wait(0.8)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font=self.FONT_CHINESE,
            font_size=34,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 2.5)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=26,
            color=GRAY_B
        ).next_to(author_large, DOWN, buff=0.3)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        
        # 关注文字
        follow_text = Text(
            "关注我, 掌握更多解题方法!",
            font=self.FONT_CHINESE,
            font_size=self.FONT_SIZE_BODY + 2,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.8)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 装饰元素
        decorations = VGroup(*[
            Circle(
                radius=0.18,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.6
            ).move_to(
                follow_text.get_center() + 2.8 * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0])
            )
            for i in range(8)
        ])
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        self.play(
            Rotate(decorations, angle=PI, run_time=1.5)
        )
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(formula_recap),
            FadeOut(all_points),
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


# ==================== 渲染命令 ====================
"""
快速预览 (480p):
manim -pql quadratic_formula.py QuadraticFormula

高质量渲染 (1080p) - 推荐:
manim -qh quadratic_formula.py QuadraticFormula

4K质量 (2160p):
manim -qk quadratic_formula.py QuadraticFormula

GIF格式:
manim -pql --format gif quadratic_formula.py QuadraticFormula
"""