"""
约分与最简分数 - Reducing Fractions and Simplest Form Animation
使用 Manim 创建的六年级数学教学视频

内容: 约分的概念、最大公因数、最简分数的判断
目标观众: 六年级学生
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


class ReducingFractions(Scene):
    """
    约分与最简分数教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引出问题
    2. 引入概念 - 什么是约分
    3. 找公因数 - 演示约分过程
    4. 最简分数 - 定义和判断
    5. 快速练习 - 巩固理解
    6. 总结技巧 - 约分三步法
    7. 片尾关注 - 作者信息
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要分数
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调/高亮
        self.COLOR_HIGHLIGHT = YELLOW       # 黄色 - 关键步骤
        self.COLOR_AUXILIARY = GRAY_B       # 灰色 - 辅助说明
        self.COLOR_SUCCESS = "#2ecc71"      # 绿色 - 成功/最简分数
        self.COLOR_DIVISOR = "#f39c12"      # 橙色 - 公因数
        
        # 执行动画序列
        self.show_opening()
        self.show_concept()
        self.show_finding_gcd()
        self.show_simplest_fraction()
        self.show_quick_practice()
        self.show_summary()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息 (顶部水印, 全程保留)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "这两个分数相等吗?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 第一个分数: 12/18
        frac_1 = MathTex(
            r"\frac{12}{18}",
            font_size=56,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2 + LEFT * 2.5)
        
        self.play(Write(frac_1), run_time=0.7)
        
        # 疑问符号
        question = Text(
            "?",
            font="PingFang SC",
            font_size=60,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 2)
        
        self.play(FadeIn(question, scale=1.3), run_time=0.4)
        
        # 第二个分数: 2/3
        frac_2 = MathTex(
            r"\frac{2}{3}",
            font_size=56,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 2 + RIGHT * 2.5)
        
        self.play(Write(frac_2), run_time=0.7)
        
        # 等号闪烁提示
        equal_sign = MathTex(
            "=",
            font_size=56,
            color=YELLOW
        ).move_to(UP * 2)
        
        self.play(
            Transform(question, equal_sign),
            run_time=0.5
        )
        self.play(Flash(question, color=YELLOW, flash_radius=0.5), run_time=0.4)
        self.wait(0.5)
        
        # 答案揭晓
        answer = Text(
            "答案: 相等! 但需要约分",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # 清理准备进入下一场景
        self.play(
            FadeOut(hook_text),
            FadeOut(question),
            FadeOut(answer),
            frac_1.animate.move_to(UP * 4 + LEFT * 2),
            frac_2.animate.move_to(UP * 4 + RIGHT * 2),
            run_time=0.8
        )
        
        # 保存引用供后续使用
        self.frac_original = frac_1
        self.frac_simplified = frac_2
    
    def show_concept(self):
        """场景2: 引入概念 (5-12秒)"""
        # 标题
        title = Text(
            "约分",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 定义
        definition = Text(
            "把分数化简的过程",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(FadeIn(definition, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.8)
        
        # 分数基本性质 - 使用组合方式避免中文进入MathTex
        property_label = Text(
            "分数基本性质:",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        property_formula = MathTex(
            r"\frac{a}{b} = \frac{a \div c}{b \div c}",
            font_size=32,
            color=self.COLOR_PRIMARY
        )
        
        property_note = Text(
            "(c ≠ 0)",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        )
        
        property_group = VGroup(property_label, property_formula, property_note).arrange(RIGHT, buff=0.3).move_to(UP * 3.5)
        
        self.play(Write(property_group), run_time=1.2)
        
        # 框选强调
        highlight_box = SurroundingRectangle(
            property_formula,
            color=self.COLOR_HIGHLIGHT,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(Create(highlight_box), run_time=0.6)
        
        # 说明文字
        explanation = Text(
            "分子分母同时除以相同的数\n分数大小不变",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A,
            line_spacing=1.2
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(explanation, shift=UP * 0.2), run_time=0.6)
        self.wait(1.8)  # 难点停留
        
        # 清理
        self.play(
            FadeOut(definition),
            FadeOut(property_group),
            FadeOut(highlight_box),
            FadeOut(explanation),
            title.animate.scale(0.6).move_to(UP * 7 + LEFT * 3),
            run_time=0.7
        )
        
        self.title_yuefen = title
    
    def show_finding_gcd(self):
        """场景3: 找公因数 (12-25秒)"""
        # 将原分数移动放大到中心
        self.play(
            self.frac_original.animate.scale(1.3).move_to(UP * 4),
            self.frac_simplified.animate.fade(0.7),
            run_time=0.6
        )
        
        # 提示文字
        hint = Text(
            "第一步: 找公因数",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(hint, shift=DOWN * 0.2), run_time=0.5)
        
        # === 子场景3.1: 列举因数 ===
        # 12的因数
        factors_12_label = Text(
            "12的因数:",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 2.5 + LEFT * 2.5)
        
        factors_12 = MathTex(
            "1, 2, 3, 4, 6, 12",
            font_size=24,
            color=GRAY_A
        ).next_to(factors_12_label, DOWN, buff=0.2)
        
        self.play(
            Write(factors_12_label),
            Write(factors_12),
            run_time=1.0
        )
        
        # 18的因数
        factors_18_label = Text(
            "18的因数:",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 2.5 + RIGHT * 2.5)
        
        factors_18 = MathTex(
            "1, 2, 3, 6, 9, 18",
            font_size=24,
            color=GRAY_A
        ).next_to(factors_18_label, DOWN, buff=0.2)
        
        self.play(
            Write(factors_18_label),
            Write(factors_18),
            run_time=1.0
        )
        
        # 标记公因数 - 手动高亮特定位置
        # 为了简化，我们创建新的高亮版本
        common_factors_label = Text(
            "公因数:",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_DIVISOR,
            weight=BOLD
        ).move_to(UP * 0.5)
        
        common_factors = MathTex(
            "1, 2, 3, 6",
            font_size=28,
            color=self.COLOR_DIVISOR
        ).next_to(common_factors_label, DOWN, buff=0.2)
        
        self.play(
            FadeIn(common_factors_label, shift=UP * 0.2),
            Write(common_factors),
            run_time=1.0
        )
        
        self.wait(0.8)
        
        # === 子场景3.2: 强调最大公因数 ===
        self.play(
            FadeOut(factors_12_label),
            FadeOut(factors_12),
            FadeOut(factors_18_label),
            FadeOut(factors_18),
            run_time=0.5
        )
        
        # 最大公因数
        gcd_label = Text(
            "最大公因数 (GCD):",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SECONDARY,
            weight=BOLD
        ).move_to(UP * 1.5)
        
        gcd_value = MathTex(
            "6",
            font_size=56,
            color=self.COLOR_SECONDARY
        ).next_to(gcd_label, DOWN, buff=0.3)
        
        gcd_box = SurroundingRectangle(
            gcd_value,
            color=self.COLOR_SECONDARY,
            buff=0.2,
            corner_radius=0.15
        )
        
        self.play(
            FadeOut(common_factors_label),
            FadeOut(common_factors),
            FadeIn(gcd_label, shift=DOWN * 0.2),
            run_time=0.4
        )
        
        self.play(
            Write(gcd_value),
            Create(gcd_box),
            run_time=0.6
        )
        
        self.play(Flash(gcd_value, color=self.COLOR_SECONDARY, flash_radius=0.6), run_time=0.5)
        
        # 提示
        tip = Text(
            "用最大公因数, 一步到位!",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)
        
        # === 子场景3.3: 执行约分 ===
        self.play(
            FadeOut(hint),
            FadeOut(gcd_label),
            FadeOut(gcd_box),
            FadeOut(tip),
            run_time=0.5
        )
        
        # 第二步提示
        step2_hint = Text(
            "第二步: 分子分母同时除以6",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(step2_hint, shift=DOWN * 0.2), run_time=0.5)
        
        # 显示除法过程
        division_process = MathTex(
            r"\frac{12 \div 6}{18 \div 6}",
            font_size=48,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 2.5)
        
        self.play(
            self.frac_original.animate.move_to(UP * 4 + LEFT * 2.5),
            gcd_value.animate.scale(0.6).move_to(UP * 1.8),
            run_time=0.5
        )
        
        # 箭头指向除法过程
        arrow_to_process = Arrow(
            self.frac_original.get_right() + RIGHT * 0.3,
            division_process.get_left() + LEFT * 0.3,
            color=self.COLOR_DIVISOR,
            buff=0.1,
            stroke_width=4
        )
        
        self.play(
            GrowArrow(arrow_to_process),
            Write(division_process),
            run_time=0.8
        )
        
        # 计算结果
        result = MathTex(
            r"\frac{2}{3}",
            font_size=56,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 2.5 + RIGHT * 2.8)
        
        arrow_to_result = Arrow(
            division_process.get_right() + RIGHT * 0.2,
            result.get_left() + LEFT * 0.2,
            color=self.COLOR_SUCCESS,
            buff=0.1,
            stroke_width=4
        )
        
        self.play(
            GrowArrow(arrow_to_result),
            run_time=0.5
        )
        
        self.play(
            Write(result),
            run_time=0.7
        )
        
        # 成功庆祝
        success_text = Text(
            "约分成功! ✓",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_SUCCESS,
            weight=BOLD
        ).move_to(UP * 0.5)
        
        self.play(
            Flash(result, color=self.COLOR_SUCCESS, flash_radius=0.8),
            FadeIn(success_text, scale=1.2),
            run_time=0.8
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(step2_hint),
            FadeOut(gcd_value),
            FadeOut(arrow_to_process),
            FadeOut(division_process),
            FadeOut(arrow_to_result),
            FadeOut(success_text),
            FadeOut(self.frac_original),
            result.animate.scale(0.8).move_to(UP * 4),
            run_time=0.7
        )
        
        self.result_fraction = result
    
    def show_simplest_fraction(self):
        """场景4: 最简分数 (25-35秒)"""
        # 标题
        title = Text(
            "最简分数",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_SUCCESS,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 定义1
        definition1 = Text(
            "分子和分母只有公因数 1",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(FadeIn(definition1, shift=DOWN * 0.2), run_time=0.5)
        
        # 定义2
        definition2 = Text(
            "即: 分子分母互素",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.6)
        
        self.play(FadeIn(definition2, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.8)
        
        # 数学表达
        math_condition = MathTex(
            r"\text{gcd}(a, b) = 1",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 3.2)
        
        self.play(Write(math_condition), run_time=0.8)
        self.wait(1.0)
        
        # === 示例对比 ===
        # 正例: 2/3
        example_correct = VGroup(
            MathTex(r"\frac{2}{3}", font_size=40, color=self.COLOR_SUCCESS),
            Text("✓ 最简", font="PingFang SC", font_size=22, color=self.COLOR_SUCCESS),
            MathTex(r"\text{gcd}(2, 3) = 1", font_size=20, color=GRAY_A)
        ).arrange(DOWN, buff=0.25).move_to(UP * 1 + LEFT * 2.5)
        
        self.play(FadeIn(example_correct, shift=RIGHT * 0.3), run_time=0.7)
        
        # 反例: 12/18
        example_incorrect = VGroup(
            MathTex(r"\frac{12}{18}", font_size=40, color=self.COLOR_SECONDARY),
            Text("✗ 非最简", font="PingFang SC", font_size=22, color=self.COLOR_SECONDARY),
            MathTex(r"\text{gcd}(12, 18) = 6", font_size=20, color=GRAY_A)
        ).arrange(DOWN, buff=0.25).move_to(UP * 1 + RIGHT * 2.5)
        
        self.play(FadeIn(example_incorrect, shift=LEFT * 0.3), run_time=0.7)
        
        self.wait(1.5)
        
        # 对比动画 - 强调差异
        comparison_box_correct = SurroundingRectangle(
            example_correct,
            color=self.COLOR_SUCCESS,
            buff=0.15,
            corner_radius=0.1
        )
        
        comparison_box_incorrect = SurroundingRectangle(
            example_incorrect,
            color=self.COLOR_SECONDARY,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(
            Create(comparison_box_correct),
            Create(comparison_box_incorrect),
            run_time=0.8
        )
        
        self.wait(1.5)  # 难点停留
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition1),
            FadeOut(definition2),
            FadeOut(math_condition),
            FadeOut(example_correct),
            FadeOut(example_incorrect),
            FadeOut(comparison_box_correct),
            FadeOut(comparison_box_incorrect),
            FadeOut(self.result_fraction),
            FadeOut(self.frac_simplified),
            run_time=0.7
        )
    
    def show_quick_practice(self):
        """场景5: 快速练习 (35-50秒)"""
        practice_title = Text(
            "快速练习",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(practice_title), run_time=0.5)
        
        # === 练习1: 24/36 ===
        self.practice_example(
            "24", "36", "12", "2", "3",
            position=UP * 3.5
        )
        
        # === 练习2: 15/25 ===
        self.practice_example(
            "15", "25", "5", "3", "5",
            position=UP * 1
        )
        
        # === 练习3: 7/9 (已是最简) ===
        problem_3 = MathTex(
            r"\frac{7}{9}",
            font_size=40,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 1.5 + LEFT * 3)
        
        self.play(Write(problem_3), run_time=0.5)
        
        # 检查GCD
        check_gcd = MathTex(
            r"\text{gcd}(7, 9) = ?",
            font_size=28,
            color=GRAY_A
        ).next_to(problem_3, RIGHT, buff=0.5)
        
        self.play(Write(check_gcd), run_time=0.5)
        self.wait(0.5)
        
        # 结论
        gcd_result = MathTex(
            "1",
            font_size=36,
            color=self.COLOR_SUCCESS
        ).move_to(check_gcd.get_right() + RIGHT * 0.5)
        
        self.play(
            FadeOut(check_gcd),
            FadeIn(gcd_result, scale=1.2),
            run_time=0.5
        )
        
        # 判断
        conclusion = Text(
            "已是最简! ✓",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SUCCESS,
            weight=BOLD
        ).next_to(problem_3, DOWN, buff=0.4)
        
        self.play(
            FadeIn(conclusion, shift=UP * 0.2),
            Flash(problem_3, color=self.COLOR_SUCCESS),
            run_time=0.7
        )
        
        self.wait(1.0)
        
        # 清理所有练习
        self.play(
            FadeOut(practice_title),
            *[FadeOut(mob) for mob in self.mobjects if mob != self.author_info and mob != self.title_yuefen],
            run_time=0.6
        )
    
    def practice_example(self, num, den, gcd, result_num, result_den, position):
        """练习示例的辅助函数"""
        # 题目分数
        problem = MathTex(
            rf"\frac{{{num}}}{{{den}}}",
            font_size=40,
            color=self.COLOR_PRIMARY
        ).move_to(position + LEFT * 3)
        
        self.play(Write(problem), run_time=0.5)
        
        # GCD闪现
        gcd_text = MathTex(
            rf"\text{{gcd}} = {gcd}",
            font_size=24,
            color=self.COLOR_DIVISOR
        ).next_to(problem, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(gcd_text, scale=1.2),
            Flash(gcd_text, color=self.COLOR_DIVISOR),
            run_time=0.6
        )
        
        # 约分过程
        process = MathTex(
            rf"\frac{{{num} \div {gcd}}}{{{den} \div {gcd}}}",
            font_size=32,
            color=GRAY_A
        ).next_to(problem, RIGHT, buff=1.5)
        
        arrow1 = Arrow(
            problem.get_right() + RIGHT * 0.15,
            process.get_left() + LEFT * 0.15,
            buff=0,
            color=GRAY_B,
            stroke_width=3
        )
        
        self.play(
            FadeOut(gcd_text),
            GrowArrow(arrow1),
            Write(process),
            run_time=0.7
        )
        
        # 结果
        result = MathTex(
            rf"\frac{{{result_num}}}{{{result_den}}}",
            font_size=40,
            color=self.COLOR_SUCCESS
        ).next_to(process, RIGHT, buff=0.8)
        
        arrow2 = Arrow(
            process.get_right() + RIGHT * 0.15,
            result.get_left() + LEFT * 0.15,
            buff=0,
            color=self.COLOR_SUCCESS,
            stroke_width=3
        )
        
        self.play(
            GrowArrow(arrow2),
            Write(result),
            run_time=0.6
        )
        
        # 验证
        check = Text(
            "✓",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_SUCCESS
        ).next_to(result, RIGHT, buff=0.3)
        
        self.play(FadeIn(check, scale=1.3), run_time=0.4)
        self.wait(0.8)
    
    def show_summary(self):
        """场景6: 总结技巧 (50-60秒)"""
        # 标题
        title = Text(
            "约分三步法",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.7)
        
        # 步骤卡片
        step1 = self.create_step_card(
            "①",
            "找最大公因数 (GCD)",
            self.COLOR_DIVISOR,
            UP * 3.5
        )
        
        step2 = self.create_step_card(
            "②",
            "分子分母同时除以GCD",
            self.COLOR_PRIMARY,
            UP * 1.5
        )
        
        step3 = self.create_step_card(
            "③",
            "验证 gcd = 1 (最简)",
            self.COLOR_SUCCESS,
            DOWN * 0.5
        )
        
        # 依次滑入
        steps = [step1, step2, step3]
        for i, step in enumerate(steps):
            step.shift(LEFT * 10)  # 初始位置在左侧外
            self.play(step.animate.shift(RIGHT * 10), run_time=0.6)
            if i < len(steps) - 1:
                self.wait(0.3)
        
        self.wait(0.8)
        
        # 关键提示
        key_tip = Text(
            "用最大公因数, 一步到位!",
            font="PingFang SC",
            font_size=30,
            color=YELLOW,
            weight=BOLD
        ).move_to(DOWN * 3.5)
        
        tip_box = SurroundingRectangle(
            key_tip,
            color=YELLOW,
            buff=0.2,
            corner_radius=0.15,
            stroke_width=3
        )
        
        self.play(
            FadeIn(key_tip, shift=UP * 0.3),
            Create(tip_box),
            run_time=0.7
        )
        
        # 全部闪烁强调
        self.play(
            Flash(step1, color=self.COLOR_DIVISOR),
            Flash(step2, color=self.COLOR_PRIMARY),
            Flash(step3, color=self.COLOR_SUCCESS),
            Flash(key_tip, color=YELLOW),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(step3),
            FadeOut(key_tip),
            FadeOut(tip_box),
            run_time=0.7
        )
    
    def create_step_card(self, number, text, color, position):
        """创建步骤卡片"""
        # 编号圆圈
        circle = Circle(
            radius=0.35,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        number_text = Text(
            number,
            font="PingFang SC",
            font_size=28,
            color=WHITE,
            weight=BOLD
        ).move_to(circle.get_center())
        
        # 步骤文字
        step_text = Text(
            text,
            font="PingFang SC",
            font_size=26,
            color=WHITE
        )
        
        # 组合
        card = VGroup(circle, number_text, step_text).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        return card
    
    def show_outro(self):
        """场景7: 片尾关注 (60-75秒)"""
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=44,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2.5)
        
        self.play(
            FadeOut(self.title_yuefen),
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        
        # ID显示
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=36,
            color=GRAY_B
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 0.2)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.7)
        
        # 分数图标装饰 (6个围绕)
        fractions = [
            r"\frac{1}{2}", r"\frac{2}{3}", r"\frac{3}{4}",
            r"\frac{4}{5}", r"\frac{5}{6}", r"\frac{6}{7}"
        ]
        
        icons = VGroup()
        for i, frac in enumerate(fractions):
            angle = i * PI / 3
            icon = MathTex(
                frac,
                font_size=28,
                color=[self.COLOR_PRIMARY, self.COLOR_SUCCESS, self.COLOR_DIVISOR][i % 3]
            ).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(angle), np.sin(angle), 0])
            )
            icons.add(icon)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            run_time=0.8
        )
        
        # 旋转动画
        self.play(Rotate(icons, angle=PI, run_time=2.0))
        
        # 示例快闪回顾
        flashback = VGroup(
            MathTex(r"\frac{12}{18}", font_size=32, color=self.COLOR_PRIMARY),
            MathTex(r"\rightarrow", font_size=32, color=YELLOW),
            MathTex(r"\frac{2}{3}", font_size=32, color=self.COLOR_SUCCESS)
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 2)
        
        self.play(FadeIn(flashback, shift=UP * 0.3), run_time=0.6)
        self.play(Flash(flashback, color=YELLOW), run_time=0.5)
        
        self.wait(2.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            FadeOut(flashback),
            run_time=1.2
        )


# 运行命令:
# manim -pql reducing_fractions.py ReducingFractions  # 快速预览 (480p 15fps)
# manim -qm reducing_fractions.py ReducingFractions  # 中等质量 (720p 30fps)
# manim -qh reducing_fractions.py ReducingFractions  # 高质量 (1080p 60fps)