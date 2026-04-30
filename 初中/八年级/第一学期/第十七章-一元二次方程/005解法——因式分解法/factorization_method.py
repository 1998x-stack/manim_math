"""
一元二次方程 - 因式分解法教学动画
Quadratic Equation - Factorization Method Teaching Animation

使用 Manim 创建的初中数学教学视频
内容: 用因式分解法解一元二次方程
目标观众: 八年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

执行命令:
manim -pql factorization_method.py FactorizationMethod  # 快速预览
manim -qh factorization_method.py FactorizationMethod   # 高质量
"""

from manim import *
import numpy as np


# ===== 全局配置 - TikTok 竖屏尺寸 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class FactorizationMethod(Scene):
    """
    因式分解法教学动画场景
    
    教学流程:
    1. 开场钩子 - 引起兴趣
    2. 零因式定理 - 理论基础
    3. 因式分解步骤 - 操作演示
    4. 应用定理求解 - 得出答案
    5. 验证答案 - 巩固理解
    6. 方法总结 - 强化记忆
    7. 片尾关注 - 引导互动
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主公式
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 关键步骤
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 高亮
        self.COLOR_SUCCESS = "#2ecc71"      # 绿色 - 答案
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助
        
        # 字体配置
        self.FONT_CHINESE = "PingFang SC"  # 或 "SimHei"
        self.AUTHOR_NAME = "上海初高中数学直通车"
        self.AUTHOR_ID = "@emptyandcalm"
        
        # 执行动画序列
        self.show_opening()
        self.show_zero_product_theorem()
        self.show_factorization_steps()
        self.show_apply_theorem()
        self.show_verification()
        self.show_summary()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息 (顶部)
        self.author_info = Text(
            f"{self.AUTHOR_NAME} {self.AUTHOR_ID}",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题 - 大字抓眼球
        hook = Text(
            "3秒解方程？",
            font=self.FONT_CHINESE,
            font_size=52,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook, run_time=0.6))
        self.wait(0.3)
        
        # 方程式从中心展开
        self.equation = MathTex(
            r"x^2 - 5x + 6 = 0",
            font_size=48,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 3)
        
        self.play(GrowFromCenter(self.equation, run_time=0.8))
        self.play(
            Flash(self.equation, color=self.COLOR_HIGHLIGHT, flash_radius=0.6),
            run_time=0.5
        )
        self.wait(0.5)
        
        # 提示文字
        hint = Text(
            "用因式分解法, 超简单!",
            font=self.FONT_CHINESE,
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(hint),
            run_time=0.4
        )
    
    def show_zero_product_theorem(self):
        """场景2: 零因式定理 (5-12秒)"""
        # 标题
        title = Text(
            "零因式定理",
            font=self.FONT_CHINESE,
            font_size=40,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 6)
        
        subtitle = Text(
            "这是关键!",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 核心公式
        ab_formula = MathTex(
            r"ab = 0",
            font_size=56,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(ab_formula, scale=1.2), run_time=0.7)
        
        # 箭头
        arrow = Arrow(
            start=UP * 2.8,
            end=UP * 1.5,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1,
            stroke_width=6
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 推论
        conclusion = MathTex(
            r"a = 0",
            r"\text{ or }",
            r"b = 0",
            font_size=48
        ).move_to(UP * 0.8)
        conclusion[0].set_color(self.COLOR_SECONDARY)
        conclusion[2].set_color(self.COLOR_SECONDARY)
        
        self.play(Write(conclusion), run_time=1.0)
        self.wait(0.5)
        
        # 示例闪烁强化理解
        example_1 = MathTex(
            r"2 \times 0 = 0",
            font_size=32,
            color=GRAY_A
        ).move_to(DOWN * 0.5 + LEFT * 2)
        
        example_2 = MathTex(
            r"0 \times 5 = 0",
            font_size=32,
            color=GRAY_A
        ).move_to(DOWN * 0.5 + RIGHT * 2)
        
        self.play(
            FadeIn(example_1, shift=RIGHT * 0.3),
            FadeIn(example_2, shift=LEFT * 0.3),
            run_time=0.6
        )
        
        for _ in range(2):
            self.play(
                example_1.animate.set_color(self.COLOR_HIGHLIGHT),
                example_2.animate.set_color(self.COLOR_HIGHLIGHT),
                run_time=0.3
            )
            self.play(
                example_1.animate.set_color(GRAY_A),
                example_2.animate.set_color(GRAY_A),
                run_time=0.3
            )
        
        # 重点框
        key_box = SurroundingRectangle(
            conclusion,
            color=self.COLOR_HIGHLIGHT,
            buff=0.3,
            corner_radius=0.1
        )
        
        self.play(Create(key_box), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(ab_formula),
            FadeOut(arrow),
            FadeOut(conclusion),
            FadeOut(example_1),
            FadeOut(example_2),
            FadeOut(key_box),
            run_time=0.6
        )
    
    def show_factorization_steps(self):
        """场景3: 因式分解步骤 (12-25秒)"""
        # 方程移至顶部
        self.play(
            self.equation.animate.move_to(UP * 6).scale(0.8),
            run_time=0.8
        )
        
        # 步骤标题
        step_title = Text(
            "步骤1: 因式分解",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.7)
        
        # 分解思路
        hint_text = Text(
            "找两个数: 和=-5, 积=6",
            font=self.FONT_CHINESE,
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(hint_text), run_time=0.6)
        self.wait(0.5)
        
        # 展示分解: -5 = -2 + (-3)
        decompose_sum = MathTex(
            r"-5 = -2 + (-3)",
            font_size=32,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 2.8)
        
        self.play(Write(decompose_sum), run_time=0.8)
        
        # 展示: 6 = 2 × 3
        decompose_prod = MathTex(
            r"6 = 2 \times 3",
            font_size=32,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 2.0)
        
        self.play(Write(decompose_prod), run_time=0.8)
        self.wait(0.5)
        
        # 十字相乘辅助网格
        grid_title = Text(
            "十字相乘:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 1.0 + LEFT * 2.5)
        
        # 简化的十字相乘示意图
        cross_lines = VGroup(
            Line(UP * 0.5 + LEFT * 1.5, DOWN * 0.5 + RIGHT * 1.5, color=self.COLOR_AUXILIARY),
            Line(UP * 0.5 + RIGHT * 1.5, DOWN * 0.5 + LEFT * 1.5, color=self.COLOR_AUXILIARY)
        ).move_to(UP * 0.3)
        
        num_1 = MathTex(r"1", font_size=28).move_to(UP * 0.6 + LEFT * 1.5)
        num_minus2 = MathTex(r"-2", font_size=28, color=self.COLOR_SECONDARY).move_to(UP * 0.6 + RIGHT * 1.5)
        num_x = MathTex(r"1", font_size=28).move_to(DOWN * 0.6 + LEFT * 1.5)
        num_minus3 = MathTex(r"-3", font_size=28, color=self.COLOR_SECONDARY).move_to(DOWN * 0.6 + RIGHT * 1.5)
        
        cross_group = VGroup(grid_title, cross_lines, num_1, num_minus2, num_x, num_minus3)
        
        self.play(FadeIn(cross_group), run_time=1.0)
        
        # 高亮 -2 和 -3
        self.play(
            Flash(num_minus2, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            Flash(num_minus3, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
            run_time=0.6
        )
        self.wait(0.5)
        
        # 指向因式分解结果的箭头
        result_arrow = Arrow(
            start=DOWN * 1.2,
            end=DOWN * 2.0,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        self.play(GrowArrow(result_arrow), run_time=0.5)
        
        # 因式分解后的形式
        factored = MathTex(
            r"(x-2)(x-3) = 0",
            font_size=52,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 2.8)
        
        self.play(Write(factored), run_time=1.2)
        self.play(
            Flash(factored, color=self.COLOR_SUCCESS, flash_radius=0.8),
            run_time=0.5
        )
        self.wait(1.0)
        
        # 清理中间步骤
        self.play(
            FadeOut(step_title),
            FadeOut(hint_text),
            FadeOut(decompose_sum),
            FadeOut(decompose_prod),
            FadeOut(cross_group),
            FadeOut(result_arrow),
            FadeOut(self.equation),
            run_time=0.6
        )
        
        # 保存因式分解结果，移至合适位置
        self.factored_eq = factored
        self.play(
            self.factored_eq.animate.move_to(UP * 5),
            run_time=0.6
        )
    
    def show_apply_theorem(self):
        """场景4: 应用零因式定理求解 (25-35秒)"""
        # 步骤标题
        step_title = Text(
            "步骤2: 令因式为0",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 3.8)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.7)
        
        # 回顾定理（小字提示）
        recall = Text(
            "根据 ab=0 → a=0 或 b=0",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 3.0)
        
        self.play(FadeIn(recall), run_time=0.5)
        self.wait(0.5)
        
        # 标记两个因式
        factor_1 = MathTex(r"x-2", font_size=42, color=self.COLOR_SECONDARY).move_to(UP * 1.8 + LEFT * 2)
        factor_2 = MathTex(r"x-3", font_size=42, color=self.COLOR_SECONDARY).move_to(UP * 1.8 + RIGHT * 2)
        
        box_1 = SurroundingRectangle(factor_1, color=self.COLOR_SECONDARY, buff=0.15)
        box_2 = SurroundingRectangle(factor_2, color=self.COLOR_SECONDARY, buff=0.15)
        
        self.play(
            TransformFromCopy(self.factored_eq, factor_1),
            Create(box_1),
            run_time=0.7
        )
        self.play(
            TransformFromCopy(self.factored_eq, factor_2),
            Create(box_2),
            run_time=0.7
        )
        self.wait(0.3)
        
        # 提示文字
        hint = Text(
            "分别令它们等于0:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 0.8)
        
        self.play(FadeIn(hint), run_time=0.5)
        
        # 分支1: x - 2 = 0
        branch_1_eq = MathTex(
            r"x - 2 = 0",
            font_size=38
        ).move_to(DOWN * 0.2 + LEFT * 2.2)
        
        self.play(Write(branch_1_eq), run_time=0.6)
        
        # 求解1
        arrow_1 = MathTex(r"\Downarrow", font_size=32).next_to(branch_1_eq, DOWN, buff=0.2)
        solution_1 = MathTex(
            r"x = 2",
            font_size=42,
            color=self.COLOR_SUCCESS
        ).next_to(arrow_1, DOWN, buff=0.2)
        
        self.play(FadeIn(arrow_1), run_time=0.3)
        self.play(Write(solution_1), run_time=0.6)
        self.play(Flash(solution_1, color=self.COLOR_SUCCESS), run_time=0.4)
        self.wait(0.3)
        
        # 分支2: x - 3 = 0
        branch_2_eq = MathTex(
            r"x - 3 = 0",
            font_size=38
        ).move_to(DOWN * 0.2 + RIGHT * 2.2)
        
        self.play(Write(branch_2_eq), run_time=0.6)
        
        # 求解2
        arrow_2 = MathTex(r"\Downarrow", font_size=32).next_to(branch_2_eq, DOWN, buff=0.2)
        solution_2 = MathTex(
            r"x = 3",
            font_size=42,
            color=self.COLOR_SUCCESS
        ).next_to(arrow_2, DOWN, buff=0.2)
        
        self.play(FadeIn(arrow_2), run_time=0.3)
        self.play(Write(solution_2), run_time=0.6)
        self.play(Flash(solution_2, color=self.COLOR_SUCCESS), run_time=0.4)
        self.wait(0.5)
        
        # 汇总答案
        final_answer = MathTex(
            r"x_1 = 2, \quad x_2 = 3",
            font_size=48,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 4.5)
        
        answer_box = SurroundingRectangle(
            final_answer,
            color=self.COLOR_SUCCESS,
            buff=0.3,
            corner_radius=0.15
        )
        
        self.play(
            TransformFromCopy(VGroup(solution_1, solution_2), final_answer),
            run_time=0.8
        )
        self.play(Create(answer_box), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(recall),
            FadeOut(factor_1),
            FadeOut(factor_2),
            FadeOut(box_1),
            FadeOut(box_2),
            FadeOut(hint),
            FadeOut(branch_1_eq),
            FadeOut(branch_2_eq),
            FadeOut(arrow_1),
            FadeOut(arrow_2),
            FadeOut(solution_1),
            FadeOut(solution_2),
            FadeOut(self.factored_eq),
            run_time=0.6
        )
        
        # 保存最终答案
        self.final_answer = VGroup(final_answer, answer_box)
        self.play(
            self.final_answer.animate.move_to(UP * 5.5).scale(0.85),
            run_time=0.6
        )
    
    def show_verification(self):
        """场景5: 验证答案 (35-45秒)"""
        # 步骤标题
        step_title = Text(
            "步骤3: 验证",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 4.2)
        
        self.play(FadeIn(step_title, shift=DOWN * 0.2), run_time=0.7)
        
        # 原方程（小字提示）
        original = MathTex(
            r"x^2 - 5x + 6 = 0",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 3.4)
        
        self.play(FadeIn(original), run_time=0.5)
        
        # 验证 x = 2
        verify_label_1 = Text(
            "代入 x = 2:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2.3 + LEFT * 3)
        
        self.play(FadeIn(verify_label_1), run_time=0.5)
        
        verify_1_step1 = MathTex(
            r"2^2 - 5 \times 2 + 6",
            font_size=32
        ).move_to(UP * 1.5)
        
        self.play(Write(verify_1_step1), run_time=0.8)
        
        verify_1_step2 = MathTex(
            r"= 4 - 10 + 6",
            font_size=32
        ).move_to(UP * 0.8)
        
        self.play(Write(verify_1_step2), run_time=0.6)
        
        verify_1_step3 = MathTex(
            r"= 0",
            font_size=36,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 0.1)
        
        checkmark_1 = MathTex(
            r"\checkmark",
            font_size=48,
            color=self.COLOR_SUCCESS
        ).next_to(verify_1_step3, RIGHT, buff=0.3)
        
        self.play(Write(verify_1_step3), run_time=0.6)
        self.play(FadeIn(checkmark_1, scale=1.5), run_time=0.4)
        self.wait(0.5)
        
        # 验证 x = 3
        verify_label_2 = Text(
            "代入 x = 3:",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 0.8 + LEFT * 3)
        
        self.play(FadeIn(verify_label_2), run_time=0.5)
        
        verify_2_step1 = MathTex(
            r"3^2 - 5 \times 3 + 6",
            font_size=32
        ).move_to(DOWN * 1.6)
        
        self.play(Write(verify_2_step1), run_time=0.8)
        
        verify_2_step2 = MathTex(
            r"= 9 - 15 + 6",
            font_size=32
        ).move_to(DOWN * 2.3)
        
        self.play(Write(verify_2_step2), run_time=0.6)
        
        verify_2_step3 = MathTex(
            r"= 0",
            font_size=36,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 3.0)
        
        checkmark_2 = MathTex(
            r"\checkmark",
            font_size=48,
            color=self.COLOR_SUCCESS
        ).next_to(verify_2_step3, RIGHT, buff=0.3)
        
        self.play(Write(verify_2_step3), run_time=0.6)
        self.play(FadeIn(checkmark_2, scale=1.5), run_time=0.4)
        
        # 验证通过提示
        pass_text = Text(
            "验证通过! 答案正确!",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_SUCCESS,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(pass_text, shift=UP * 0.3, scale=1.2), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(step_title),
            FadeOut(original),
            FadeOut(verify_label_1),
            FadeOut(verify_label_2),
            FadeOut(verify_1_step1),
            FadeOut(verify_1_step2),
            FadeOut(verify_1_step3),
            FadeOut(checkmark_1),
            FadeOut(verify_2_step1),
            FadeOut(verify_2_step2),
            FadeOut(verify_2_step3),
            FadeOut(checkmark_2),
            FadeOut(pass_text),
            FadeOut(self.final_answer),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景6: 方法总结 (45-55秒)"""
        # 标题
        title = Text(
            "因式分解法 - 三步走",
            font=self.FONT_CHINESE,
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建步骤卡片
        card_1 = self.create_step_card(
            "1️⃣ 因式分解",
            "将方程左边化为两个因式乘积",
            UP * 4.2
        )
        
        card_2 = self.create_step_card(
            "2️⃣ 令因式为0",
            "分别令每个因式等于0",
            UP * 2.2
        )
        
        card_3 = self.create_step_card(
            "3️⃣ 求解验证",
            "解出x的值, 代入验证",
            UP * 0.2
        )
        
        # 卡片依次滑入
        for card in [card_1, card_2, card_3]:
            card.shift(LEFT * 10)  # 初始位置在左侧外
        
        self.play(card_1.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card_2.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.3)
        self.play(card_3.animate.shift(RIGHT * 10), run_time=0.6)
        self.wait(0.5)
        
        # 适用条件强调
        condition = Text(
            "⚡ 适用条件: 左边容易因式分解时最快!",
            font=self.FONT_CHINESE,
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(condition, shift=UP * 0.3), run_time=0.6)
        
        # 更多示例快速闪烁
        examples_label = Text(
            "更多例子:",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 3.8)
        
        example_eqs = VGroup(
            MathTex(r"x^2 - 4 = 0", font_size=24, color=GRAY_A),
            MathTex(r"x^2 + 3x - 10 = 0", font_size=24, color=GRAY_A),
            MathTex(r"2x^2 - 5x - 3 = 0", font_size=24, color=GRAY_A)
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 4.8)
        
        self.play(FadeIn(examples_label), run_time=0.4)
        self.play(FadeIn(example_eqs, shift=UP * 0.2), run_time=0.6)
        
        # 闪烁示例
        for _ in range(2):
            self.play(
                example_eqs.animate.set_color(self.COLOR_HIGHLIGHT),
                run_time=0.3
            )
            self.play(
                example_eqs.animate.set_color(GRAY_A),
                run_time=0.3
            )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card_1),
            FadeOut(card_2),
            FadeOut(card_3),
            FadeOut(condition),
            FadeOut(examples_label),
            FadeOut(example_eqs),
            run_time=0.6
        )
    
    def create_step_card(self, step_title, content, position):
        """创建步骤卡片"""
        # 标题
        title_text = Text(
            step_title,
            font=self.FONT_CHINESE,
            font_size=28,
            color=WHITE,
            weight=BOLD
        )
        
        # 内容
        content_text = Text(
            content,
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_A
        )
        
        # 组合卡片
        card = VGroup(title_text, content_text).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        
        # 背景矩形
        bg_rect = SurroundingRectangle(
            card,
            color=self.COLOR_PRIMARY,
            fill_color="#2c3e50",
            fill_opacity=0.3,
            buff=0.3,
            corner_radius=0.15
        )
        
        card_group = VGroup(bg_rect, card)
        card_group.move_to(position)
        
        return card_group
    
    def show_outro(self):
        """场景7: 片尾关注 (55-65秒)"""
        # 作者信息放大居中
        author_name = Text(
            self.AUTHOR_NAME,
            font=self.FONT_CHINESE,
            font_size=42,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            self.AUTHOR_ID,
            font=self.FONT_CHINESE,
            font_size=34,
            color=GRAY_B
        ).move_to(UP * 1.0)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 数学更简单!",
            font=self.FONT_CHINESE,
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 0.5)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 装饰 - 数学符号环绕
        symbols = VGroup(
            MathTex(r"+", font_size=36, color=self.COLOR_PRIMARY),
            MathTex(r"-", font_size=36, color=self.COLOR_SECONDARY),
            MathTex(r"\times", font_size=36, color=self.COLOR_SUCCESS),
            MathTex(r"\div", font_size=36, color=GOLD),
            MathTex(r"=", font_size=36, color=self.COLOR_HIGHLIGHT),
            MathTex(r"x^2", font_size=28, color=self.COLOR_PRIMARY)
        )
        
        # 环形排列
        radius = 2.5
        for i, symbol in enumerate(symbols):
            angle = i * TAU / len(symbols)
            symbol.move_to(follow_text.get_center() + radius * np.array([np.cos(angle), np.sin(angle), 0]))
        
        self.play(
            *[FadeIn(sym, scale=0.5) for sym in symbols],
            run_time=0.6
        )
        self.play(Rotate(symbols, angle=TAU/3, about_point=follow_text.get_center()), run_time=1.5)
        
        # 下期预告
        preview = Text(
            "下期预告: 配方法解方程",
            font=self.FONT_CHINESE,
            font_size=26,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(preview, shift=UP * 0.2), run_time=0.6)
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(symbols),
            FadeOut(preview),
            run_time=1.0
        )


# ===== 运行说明 =====
"""
命令行执行:

# 快速预览 (低质量, 用于调试)
manim -pql factorization_method.py FactorizationMethod

# 中等质量
manim -pqm factorization_method.py FactorizationMethod

# 高质量 (1080p, 用于发布)
manim -pqh factorization_method.py FactorizationMethod

# 4K质量 (最高质量)
manim -pqk factorization_method.py FactorizationMethod

参数说明:
-p : 预览 (渲染完成后自动播放)
-q : 质量 (l=低, m=中, h=高, k=4K)
"""