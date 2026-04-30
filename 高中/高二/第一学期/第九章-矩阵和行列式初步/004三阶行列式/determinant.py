"""
三阶行列式 - Third-Order Determinant Animation
使用 Manim 创建的高中数学教学视频

内容: 对角线法则（沙路法则）、三阶行列式计算
目标观众: 高二学生
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


class ThirdOrderDeterminant(Scene):
    """
    三阶行列式教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 行列式定义
    3. 对角线法则介绍
    4. 主对角线计算
    5. 副对角线计算
    6. 完整公式与示例
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"       # 蓝色
        self.COLOR_SECONDARY = "#e74c3c"     # 红色
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色
        self.COLOR_POSITIVE = "#2ecc71"      # 绿色 - 正项
        self.COLOR_NEGATIVE = "#e74c3c"      # 红色 - 负项
        self.COLOR_AUXILIARY = GRAY_B        # 灰色
        self.COLOR_MATRIX = WHITE            # 白色
        
        # 字体配置
        self.FONT = "PingFang SC"
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_diagonal_rule()
        self.show_main_diagonals()
        self.show_anti_diagonals()
        self.show_example()
        self.show_outro()
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子文字
        hook1 = Text(
            "九个数字，一个规则",
            font=self.FONT,
            font_size=40,
            color=WHITE
        ).move_to(UP * 5.5)
        
        hook2 = Text(
            "计算出一个神奇的值！",
            font=self.FONT,
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)
        
        self.play(Write(hook1), run_time=0.8)
        self.play(FadeIn(hook2, shift=UP * 0.3), run_time=0.6)
        
        # 创建3×3矩阵轮廓
        matrix_outline = Rectangle(
            width=3.5,
            height=3.5,
            stroke_color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(UP * 0.5)
        
        self.play(Create(matrix_outline), run_time=1.0)
        
        # 矩阵元素（符号）
        matrix_elements = self.create_symbolic_matrix().move_to(UP * 0.5)
        
        self.play(FadeIn(matrix_elements), run_time=1.0)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook1),
            FadeOut(hook2),
            FadeOut(matrix_outline),
            run_time=0.5
        )
        
        # 保存矩阵引用
        self.symbolic_matrix = matrix_elements
    
    def create_symbolic_matrix(self):
        """创建符号矩阵"""
        # 使用 MathTex 创建矩阵元素
        elements = VGroup()
        
        labels = [
            ["a_1", "b_1", "c_1"],
            ["a_2", "b_2", "c_2"],
            ["a_3", "b_3", "c_3"]
        ]
        
        for i in range(3):
            for j in range(3):
                elem = MathTex(
                    labels[i][j],
                    font_size=32,
                    color=self.COLOR_MATRIX
                )
                # 计算位置
                x_pos = (j - 1) * 1.0
                y_pos = (1 - i) * 1.0
                elem.move_to(np.array([x_pos, y_pos, 0]))
                elements.add(elem)
        
        return elements
    
    def show_definition(self):
        """场景2: 行列式定义"""
        # 标题
        title = Text(
            "三阶行列式",
            font=self.FONT,
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 移动矩阵到合适位置
        self.play(
            self.symbolic_matrix.animate.move_to(UP * 2),
            run_time=0.8
        )
        
        # 添加行列式符号（两条竖线）
        left_line = Line(
            UP * 3.5 + LEFT * 1.8,
            UP * 0.5 + LEFT * 1.8,
            stroke_width=3,
            color=self.COLOR_PRIMARY
        )
        
        right_line = Line(
            UP * 3.5 + RIGHT * 1.8,
            UP * 0.5 + RIGHT * 1.8,
            stroke_width=3,
            color=self.COLOR_PRIMARY
        )
        
        self.play(
            Create(left_line),
            Create(right_line),
            run_time=0.5
        )
        
        # 说明文字
        explanation = Text(
            "由9个数按特定规则计算出一个数值",
            font=self.FONT,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(explanation), run_time=0.8)
        
        # 公式预览
        formula_preview = MathTex(
            r"|A| = a_1b_2c_3 + b_1c_2a_3 + c_1a_2b_3",
            font_size=20
        ).move_to(DOWN * 2.5)
        
        formula_preview2 = MathTex(
            r"- c_1b_2a_3 - b_1a_2c_3 - a_1c_2b_3",
            font_size=20
        ).move_to(DOWN * 3.2)
        
        self.play(
            FadeIn(formula_preview, shift=UP * 0.2),
            FadeIn(formula_preview2, shift=UP * 0.2),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 保存标题引用
        self.title = title
        
        # 清理
        self.play(
            FadeOut(explanation),
            FadeOut(formula_preview),
            FadeOut(formula_preview2),
            FadeOut(left_line),
            FadeOut(right_line),
            run_time=0.5
        )
    
    def show_diagonal_rule(self):
        """场景3: 对角线法则介绍"""
        # 副标题
        subtitle = Text(
            "对角线法则（沙路法则）",
            font=self.FONT,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(subtitle), run_time=0.8)
        
        # 扩展矩阵：重复前两列
        extended_matrix = self.create_extended_matrix().move_to(UP * 2)
        
        explanation1 = Text(
            "重复前两列，便于计算",
            font=self.FONT,
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        
        self.play(
            Transform(self.symbolic_matrix, extended_matrix),
            FadeIn(explanation1),
            run_time=1.0
        )
        
        self.wait(0.8)
        self.play(FadeOut(explanation1), run_time=0.3)
        
        # 标记主对角线（绿色）
        main_diag_label = Text(
            "主对角线（正项）",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_POSITIVE
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(main_diag_label), run_time=0.5)
        
        # 创建三条主对角线箭头
        main_arrows = VGroup()
        for i in range(3):
            arrow = self.create_diagonal_arrow(
                start_col=i,
                start_row=0,
                direction=1,  # 向右下
                color=self.COLOR_POSITIVE
            )
            main_arrows.add(arrow)
        
        self.play(
            *[Create(arrow) for arrow in main_arrows],
            run_time=1.5
        )
        
        self.wait(0.5)
        self.play(FadeOut(main_diag_label), run_time=0.3)
        
        # 标记副对角线（红色）
        anti_diag_label = Text(
            "副对角线（负项）",
            font=self.FONT,
            font_size=22,
            color=self.COLOR_NEGATIVE
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(anti_diag_label), run_time=0.5)
        
        # 创建三条副对角线箭头
        anti_arrows = VGroup()
        for i in range(3):
            arrow = self.create_diagonal_arrow(
                start_col=2+i,
                start_row=0,
                direction=-1,  # 向左下
                color=self.COLOR_NEGATIVE
            )
            anti_arrows.add(arrow)
        
        self.play(
            *[Create(arrow) for arrow in anti_arrows],
            run_time=1.5
        )
        
        self.wait(0.5)
        
        # 规则说明
        rule = Text(
            "主对角线乘积之和 - 副对角线乘积之和",
            font=self.FONT,
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        self.play(
            Transform(anti_diag_label, rule),
            run_time=0.8
        )
        
        self.wait(1.4)
        
        # 保存引用
        self.main_arrows = main_arrows
        self.anti_arrows = anti_arrows
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(anti_diag_label),
            run_time=0.5
        )
    
    def create_extended_matrix(self):
        """创建扩展矩阵（5列）"""
        elements = VGroup()
        
        labels = [
            ["a_1", "b_1", "c_1", "a_1", "b_1"],
            ["a_2", "b_2", "c_2", "a_2", "b_2"],
            ["a_3", "b_3", "c_3", "a_3", "b_3"]
        ]
        
        for i in range(3):
            for j in range(5):
                elem = MathTex(
                    labels[i][j],
                    font_size=28,
                    color=self.COLOR_MATRIX if j < 3 else GRAY_C
                )
                # 计算位置
                x_pos = (j - 2) * 0.8
                y_pos = (1 - i) * 1.0
                elem.move_to(np.array([x_pos, y_pos, 0]))
                elements.add(elem)
        
        return elements
    
    def create_diagonal_arrow(self, start_col, start_row, direction, color):
        """
        创建对角线箭头
        direction: 1 = 右下, -1 = 左下
        """
        # 计算起点和终点位置
        start_x = (start_col - 2) * 0.8
        start_y = (1 - start_row) * 1.0
        
        end_x = start_x + direction * 2 * 0.8
        end_y = start_y - 2 * 1.0
        
        start_point = np.array([start_x, start_y, 0]) + UP * 2
        end_point = np.array([end_x, end_y, 0]) + UP * 2
        
        arrow = Arrow(
            start_point + UP * 0.3,
            end_point + DOWN * 0.3,
            color=color,
            stroke_width=4,
            buff=0.1,
            tip_length=0.2
        )
        
        return arrow
    
    def show_main_diagonals(self):
        """场景4: 主对角线计算"""
        # 计算区域（右侧）
        calc_area = VGroup()
        calc_y = UP * 3
        
        # 对角线1: a₁b₂c₃
        self.play(
            self.main_arrows[0].animate.set_stroke(width=6),
            run_time=0.8
        )
        
        term1 = MathTex(r"a_1 b_2 c_3", font_size=26, color=self.COLOR_POSITIVE)
        term1.move_to(RIGHT * 2.5 + calc_y)
        
        self.play(Write(term1), run_time=1.0)
        calc_area.add(term1)
        
        self.play(
            self.main_arrows[0].animate.set_stroke(width=4),
            run_time=0.3
        )
        self.wait(0.5)
        
        # 对角线2: b₁c₂a₃
        self.play(
            self.main_arrows[1].animate.set_stroke(width=6),
            run_time=0.8
        )
        
        plus1 = MathTex(r"+", font_size=26, color=WHITE)
        plus1.next_to(term1, DOWN, buff=0.3, aligned_edge=LEFT)
        
        term2 = MathTex(r"b_1 c_2 a_3", font_size=26, color=self.COLOR_POSITIVE)
        term2.next_to(plus1, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(plus1),
            Write(term2),
            run_time=1.0
        )
        calc_area.add(plus1, term2)
        
        self.play(
            self.main_arrows[1].animate.set_stroke(width=4),
            run_time=0.3
        )
        self.wait(0.5)
        
        # 对角线3: c₁a₂b₃
        self.play(
            self.main_arrows[2].animate.set_stroke(width=6),
            run_time=0.8
        )
        
        plus2 = MathTex(r"+", font_size=26, color=WHITE)
        plus2.next_to(term2, DOWN, buff=0.3, aligned_edge=LEFT)
        
        term3 = MathTex(r"c_1 a_2 b_3", font_size=26, color=self.COLOR_POSITIVE)
        term3.next_to(plus2, RIGHT, buff=0.2)
        
        self.play(
            FadeIn(plus2),
            Write(term3),
            run_time=1.0
        )
        calc_area.add(plus2, term3)
        
        self.play(
            self.main_arrows[2].animate.set_stroke(width=4),
            run_time=0.3
        )
        self.wait(0.5)
        
        # 框选正项和
        positive_box = SurroundingRectangle(
            calc_area,
            color=self.COLOR_POSITIVE,
            buff=0.15,
            stroke_width=2
        )
        
        positive_label = Text(
            "正项和",
            font=self.FONT,
            font_size=20,
            color=self.COLOR_POSITIVE
        ).next_to(positive_box, RIGHT, buff=0.2)
        
        self.play(
            Create(positive_box),
            FadeIn(positive_label),
            run_time=0.8
        )
        
        self.wait(1.8)
        
        # 保存引用
        self.positive_terms = VGroup(calc_area, positive_box, positive_label)
        
        # 向上移动
        self.play(
            self.positive_terms.animate.shift(UP * 0.5),
            run_time=0.5
        )
    
    def show_anti_diagonals(self):
        """场景5: 副对角线计算"""
        # 计算区域（右侧，负项）
        calc_area = VGroup()
        calc_y = UP * 0.5
        
        # 对角线1: -c₁b₂a₃
        self.play(
            self.anti_arrows[0].animate.set_stroke(width=6),
            run_time=0.8
        )
        
        term1 = MathTex(r"- c_1 b_2 a_3", font_size=26, color=self.COLOR_NEGATIVE)
        term1.move_to(RIGHT * 2.5 + calc_y)
        
        self.play(Write(term1), run_time=1.0)
        calc_area.add(term1)
        
        self.play(
            self.anti_arrows[0].animate.set_stroke(width=4),
            run_time=0.3
        )
        self.wait(0.5)
        
        # 对角线2: -b₁a₂c₃
        self.play(
            self.anti_arrows[1].animate.set_stroke(width=6),
            run_time=0.8
        )
        
        term2 = MathTex(r"- b_1 a_2 c_3", font_size=26, color=self.COLOR_NEGATIVE)
        term2.next_to(term1, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(term2), run_time=1.0)
        calc_area.add(term2)
        
        self.play(
            self.anti_arrows[1].animate.set_stroke(width=4),
            run_time=0.3
        )
        self.wait(0.5)
        
        # 对角线3: -a₁c₂b₃
        self.play(
            self.anti_arrows[2].animate.set_stroke(width=6),
            run_time=0.8
        )
        
        term3 = MathTex(r"- a_1 c_2 b_3", font_size=26, color=self.COLOR_NEGATIVE)
        term3.next_to(term2, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(term3), run_time=1.0)
        calc_area.add(term3)
        
        self.play(
            self.anti_arrows[2].animate.set_stroke(width=4),
            run_time=0.3
        )
        self.wait(0.5)
        
        # 框选负项和
        negative_box = SurroundingRectangle(
            calc_area,
            color=self.COLOR_NEGATIVE,
            buff=0.15,
            stroke_width=2
        )
        
        negative_label = Text(
            "负项和",
            font=self.FONT,
            font_size=20,
            color=self.COLOR_NEGATIVE
        ).next_to(negative_box, RIGHT, buff=0.2)
        
        self.play(
            Create(negative_box),
            FadeIn(negative_label),
            run_time=0.8
        )
        
        self.wait(1.8)
        
        # 保存引用
        self.negative_terms = VGroup(calc_area, negative_box, negative_label)
    
    def show_example(self):
        """场景6: 完整公式与示例"""
        # 清理对角线和扩展矩阵
        self.play(
            FadeOut(self.symbolic_matrix),
            FadeOut(self.main_arrows),
            FadeOut(self.anti_arrows),
            FadeOut(self.positive_terms),
            FadeOut(self.negative_terms),
            run_time=0.6
        )
        
        # 完整公式
        formula = MathTex(
            r"|A| = ",
            r"a_1b_2c_3 + b_1c_2a_3 + c_1a_2b_3",
            r"\\",
            r"- c_1b_2a_3 - b_1a_2c_3 - a_1c_2b_3",
            font_size=20
        ).move_to(UP * 3.5)
        
        formula[1].set_color(self.COLOR_POSITIVE)
        formula[3].set_color(self.COLOR_NEGATIVE)
        
        self.play(Write(formula), run_time=1.2)
        
        flash_rect = SurroundingRectangle(
            formula,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        self.play(ShowPassingFlash(flash_rect, time_width=0.5), run_time=0.5)
        
        self.wait(0.8)
        
        # 具体数值示例
        example_label = Text(
            "数值示例:",
            font=self.FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 2 + LEFT * 2.5)
        
        self.play(FadeIn(example_label), run_time=0.5)
        
        # 数值矩阵
        numeric_matrix = self.create_numeric_matrix().move_to(UP * 0.5 + LEFT * 2.5)
        
        self.play(FadeIn(numeric_matrix), run_time=0.8)
        
        # 计算过程
        calc_steps = VGroup()
        
        # 主对角线
        step1 = MathTex(r"2 \times 5 \times 9 = 90", font_size=22, color=self.COLOR_POSITIVE)
        step1.move_to(UP * 1.5 + RIGHT * 2)
        calc_steps.add(step1)
        self.play(Write(step1), run_time=1.5)
        
        step2 = MathTex(r"1 \times 6 \times 8 = 48", font_size=22, color=self.COLOR_POSITIVE)
        step2.next_to(step1, DOWN, buff=0.3, aligned_edge=LEFT)
        calc_steps.add(step2)
        self.play(Write(step2), run_time=1.5)
        
        step3 = MathTex(r"3 \times 4 \times 7 = 84", font_size=22, color=self.COLOR_POSITIVE)
        step3.next_to(step2, DOWN, buff=0.3, aligned_edge=LEFT)
        calc_steps.add(step3)
        self.play(Write(step3), run_time=1.5)
        
        sum_positive = MathTex(r"90 + 48 + 84 = 222", font_size=24, color=self.COLOR_POSITIVE)
        sum_positive.next_to(step3, DOWN, buff=0.5, aligned_edge=LEFT)
        calc_steps.add(sum_positive)
        self.play(Write(sum_positive), run_time=1.0)
        
        # 副对角线
        step4 = MathTex(r"3 \times 5 \times 7 = 105", font_size=22, color=self.COLOR_NEGATIVE)
        step4.next_to(sum_positive, DOWN, buff=0.5, aligned_edge=LEFT)
        calc_steps.add(step4)
        self.play(Write(step4), run_time=1.5)
        
        step5 = MathTex(r"1 \times 4 \times 9 = 36", font_size=22, color=self.COLOR_NEGATIVE)
        step5.next_to(step4, DOWN, buff=0.3, aligned_edge=LEFT)
        calc_steps.add(step5)
        self.play(Write(step5), run_time=1.5)
        
        step6 = MathTex(r"2 \times 6 \times 8 = 96", font_size=22, color=self.COLOR_NEGATIVE)
        step6.next_to(step5, DOWN, buff=0.3, aligned_edge=LEFT)
        calc_steps.add(step6)
        self.play(Write(step6), run_time=1.5)
        
        sum_negative = MathTex(r"105 + 36 + 96 = 237", font_size=24, color=self.COLOR_NEGATIVE)
        sum_negative.next_to(step6, DOWN, buff=0.5, aligned_edge=LEFT)
        calc_steps.add(sum_negative)
        self.play(Write(sum_negative), run_time=1.0)
        
        # 最终结果
        final_result = MathTex(
            r"|A| = 222 - 237 = -15",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(Write(final_result), run_time=1.2)
        self.play(
            Flash(final_result, color=self.COLOR_HIGHLIGHT, flash_radius=0.5),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(formula),
            FadeOut(example_label),
            FadeOut(numeric_matrix),
            FadeOut(calc_steps),
            run_time=0.6
        )
        
        # 移动结果到中心
        self.play(
            final_result.animate.move_to(ORIGIN),
            run_time=0.5
        )
        self.play(FadeOut(final_result), run_time=0.3)
    
    def create_numeric_matrix(self):
        """创建数值矩阵"""
        elements = VGroup()
        
        values = [
            ["2", "1", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        
        for i in range(3):
            for j in range(3):
                elem = MathTex(
                    values[i][j],
                    font_size=32,
                    color=self.COLOR_MATRIX
                )
                x_pos = (j - 1) * 0.8
                y_pos = (1 - i) * 0.8
                elem.move_to(np.array([x_pos, y_pos, 0]))
                elements.add(elem)
        
        # 添加矩阵符号
        left_line = Line(
            UP * 1.3 + LEFT * 1.5,
            DOWN * 1.3 + LEFT * 1.5,
            stroke_width=3,
            color=self.COLOR_PRIMARY
        )
        
        right_line = Line(
            UP * 1.3 + RIGHT * 1.5,
            DOWN * 1.3 + RIGHT * 1.5,
            stroke_width=3,
            color=self.COLOR_PRIMARY
        )
        
        return VGroup(elements, left_line, right_line)
    
    def show_outro(self):
        """场景7: 总结与片尾"""
        # 要点卡片
        card1 = self.create_summary_card(
            "对角线法则",
            "简单快速计算三阶行列式",
            self.COLOR_POSITIVE,
            UP * 2
        )
        
        card2 = self.create_summary_card(
            "记忆口诀",
            "主对角线正，副对角线负",
            self.COLOR_NEGATIVE,
            UP * 0.5
        )
        
        card3 = self.create_summary_card(
            "重要应用",
            "解三元一次方程组",
            self.COLOR_PRIMARY,
            DOWN * 1
        )
        
        cards = VGroup(card1, card2, card3)
        
        # 卡片滑入
        for card in cards:
            card.shift(LEFT * 10)
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)
        
        self.wait(1.0)
        
        # 清理
        self.play(FadeOut(cards), FadeOut(self.title), run_time=0.5)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT,
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT,
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(Transform(self.author_info, author_name), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow = Text(
            "关注我，学更多数学技巧！",
            font=self.FONT,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 矩阵装饰图标
        matrix_icons = VGroup(*[
            Rectangle(width=0.3, height=0.3, color=c, fill_opacity=0.8)
            for c in [self.COLOR_POSITIVE, self.COLOR_NEGATIVE, self.COLOR_PRIMARY]
        ]).arrange(RIGHT, buff=0.3).move_to(DOWN * 2)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in matrix_icons], run_time=0.6)
        self.play(matrix_icons.animate.scale(1.2), run_time=0.5)
        self.play(matrix_icons.animate.scale(1/1.2), run_time=0.5)
        
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(matrix_icons),
            run_time=1.0
        )
    
    def create_summary_card(self, title_text, subtitle_text, color, position):
        """创建总结卡片"""
        # 图标
        icon = Square(side_length=0.3, fill_color=color, fill_opacity=0.8, stroke_width=0)
        
        # 文字
        title = Text(title_text, font=self.FONT, font_size=26, color=WHITE)
        subtitle = Text(subtitle_text, font=self.FONT, font_size=18, color=GRAY_A)
        
        text_group = VGroup(title, subtitle).arrange(DOWN, buff=0.12)
        
        card = VGroup(icon, text_group).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        return card


# 运行命令示例:
# manim -pql determinant.py ThirdOrderDeterminant  # 快速预览
# manim -qh determinant.py ThirdOrderDeterminant   # 高质量输出