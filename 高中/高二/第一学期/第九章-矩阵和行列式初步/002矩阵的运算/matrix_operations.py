"""
矩阵的运算 - Matrix Operations
使用 Manim 创建的高中数学教学视频

内容: 矩阵加法、数乘、矩阵乘法、运算性质
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

from manim import TexTemplate
config.tex_template = TexTemplate()
config.tex_template.add_to_preamble(r"\usepackage[UTF8, fontset=adobe]{ctex}")


class MatrixOperations(Scene):
    """
    矩阵运算教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 矩阵加法
    3. 数乘
    4. 矩阵乘法引入
    5. 矩阵乘法详细计算
    6. 矩阵乘法完整示例
    7. 交换律不成立
    8. 其他性质与总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 矩阵A
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 矩阵B
        self.COLOR_RESULT = "#2ecc71"       # 绿色 - 结果
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_MULTIPLY = "#9b59b6"      # 紫色 - 乘法
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        
        # 初始化全局元素
        self.setup_globals()
        
        # 执行动画序列
        self.show_opening()
        self.show_addition()
        self.show_scalar_multiplication()
        self.show_multiplication_intro()
        self.show_multiplication_detail()
        self.show_multiplication_complete()
        self.show_non_commutative()
        self.show_properties_summary()
    
    def setup_globals(self):
        """初始化全局配置和常驻元素"""
        # 作者信息 (持续显示)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.add(self.author_info)
        
        # 标准位置
        self.MATRIX_CENTER = UP * 2
        self.TITLE_POS = UP * 6
        self.EXPLAIN_POS = DOWN * 4.5
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 钩子问题
        hook = Text(
            "矩阵如何计算?",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.TITLE_POS)
        
        self.play(Write(hook), run_time=1.0)
        self.wait(0.3)
        
        # 三种运算符号
        add_symbol = MathTex("+", font_size=60, color=self.COLOR_PRIMARY).move_to(LEFT * 2.5 + UP * 2)
        scalar_symbol = MathTex("k \\cdot", font_size=60, color=self.COLOR_SECONDARY).move_to(UP * 2)
        mult_symbol = MathTex("\\times", font_size=60, color=self.COLOR_MULTIPLY).move_to(RIGHT * 2.5 + UP * 2)
        
        symbols = VGroup(add_symbol, scalar_symbol, mult_symbol)
        
        for symbol in symbols:
            self.play(FadeIn(symbol, scale=1.2), run_time=0.4)
        
        # 过渡文字
        transition = Text(
            "三种基本运算",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_RESULT
        ).move_to(self.EXPLAIN_POS)
        
        self.play(FadeIn(transition, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(symbols),
            FadeOut(transition),
            run_time=0.5
        )
    
    def show_addition(self):
        """场景2: 矩阵加法"""
        # 标题
        title = Text(
            "矩阵加法",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.7)
        
        # 矩阵 A
        matrix_A = Matrix(
            [["1", "2"], ["3", "4"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28},
            h_buff=0.8,
            v_buff=0.6
        ).move_to(LEFT * 2.5 + UP * 2)
        matrix_A.set_color(self.COLOR_PRIMARY)
        
        label_A = MathTex("A =", font_size=28).next_to(matrix_A, LEFT, buff=0.3)
        
        # 矩阵 B
        matrix_B = Matrix(
            [["5", "6"], ["7", "8"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28},
            h_buff=0.8,
            v_buff=0.6
        ).move_to(RIGHT * 2.5 + UP * 2)
        matrix_B.set_color(self.COLOR_SECONDARY)
        
        label_B = MathTex("B =", font_size=28).next_to(matrix_B, LEFT, buff=0.3)
        
        # 加号
        plus = MathTex("+", font_size=40).move_to(UP * 2)
        
        self.play(
            Write(label_A),
            Create(matrix_A),
            run_time=0.8
        )
        self.play(Write(plus), run_time=0.3)
        self.play(
            Write(label_B),
            Create(matrix_B),
            run_time=0.8
        )
        
        # 高亮对应元素相加
        for i in range(4):
            self.play(
                Indicate(matrix_A.get_entries()[i], color=self.COLOR_HIGHLIGHT),
                Indicate(matrix_B.get_entries()[i], color=self.COLOR_HIGHLIGHT),
                run_time=0.3
            )
        
        # 结果矩阵
        matrix_C = Matrix(
            [["6", "8"], ["10", "12"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28},
            h_buff=0.8,
            v_buff=0.6
        ).move_to(DOWN * 0.5)
        matrix_C.set_color(self.COLOR_RESULT)
        
        equal = MathTex("=", font_size=40).next_to(matrix_C, LEFT, buff=0.5)
        
        self.play(
            Write(equal),
            Create(matrix_C),
            run_time=1.0
        )
        
        # 说明
        explain = Text(
            "对应元素相加",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(self.EXPLAIN_POS)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.5)  # 延长等待
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(label_A),
            FadeOut(matrix_A),
            FadeOut(plus),
            FadeOut(label_B),
            FadeOut(matrix_B),
            FadeOut(equal),
            FadeOut(matrix_C),
            FadeOut(explain),
            run_time=0.5
        )
    
    def show_scalar_multiplication(self):
        """场景3: 数乘"""
        # 标题
        title = Text(
            "数乘",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.7)
        
        # 常数
        scalar = MathTex("2", font_size=40, color=self.COLOR_SECONDARY).move_to(LEFT * 2.5 + UP * 2)
        
        # 矩阵 A
        matrix_A = Matrix(
            [["1", "2"], ["3", "4"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28},
            h_buff=0.8,
            v_buff=0.6
        ).move_to(LEFT * 0.5 + UP * 2)
        matrix_A.set_color(self.COLOR_PRIMARY)
        
        self.play(Write(scalar), Create(matrix_A), run_time=1.0)
        
        # 逐个元素乘以2
        highlights = []
        for i in range(4):
            self.play(
                Indicate(matrix_A.get_entries()[i], color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
                run_time=0.3
            )
        
        # 结果矩阵
        matrix_result = Matrix(
            [["2", "4"], ["6", "8"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28},
            h_buff=0.8,
            v_buff=0.6
        ).move_to(DOWN * 0.5)
        matrix_result.set_color(self.COLOR_RESULT)
        
        equal = MathTex("=", font_size=40).next_to(matrix_result, LEFT, buff=0.5)
        
        self.play(
            Write(equal),
            Create(matrix_result),
            run_time=1.0
        )
        
        # 说明
        explain = Text(
            "每个元素乘以常数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(self.EXPLAIN_POS)
        
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(1.3)  # 延长等待
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(scalar),
            FadeOut(matrix_A),
            FadeOut(equal),
            FadeOut(matrix_result),
            FadeOut(explain),
            run_time=0.5
        )
    
    def show_multiplication_intro(self):
        """场景4: 矩阵乘法引入"""
        # 标题 - 强调重点
        title = Text(
            "矩阵乘法 (重点)",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MULTIPLY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.8)
        
        # 矩阵 A (2×3)
        matrix_A = Matrix(
            [["1", "2", "3"], ["4", "5", "6"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 24},
            h_buff=0.7,
            v_buff=0.5
        ).move_to(LEFT * 2 + UP * 2.5)
        matrix_A.set_color(self.COLOR_PRIMARY)
        
        label_A = MathTex("A_{2 \\times 3} =", font_size=24).next_to(matrix_A, LEFT, buff=0.3)
        dim_A = Text("2×3", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_PRIMARY).next_to(matrix_A, DOWN, buff=0.3)
        
        # 矩阵 B (3×2)
        matrix_B = Matrix(
            [["7", "8"], ["9", "10"], ["11", "12"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 24},
            h_buff=0.7,
            v_buff=0.5
        ).move_to(RIGHT * 2 + UP * 2.5)
        matrix_B.set_color(self.COLOR_SECONDARY)
        
        label_B = MathTex("B_{3 \\times 2} =", font_size=24).next_to(matrix_B, LEFT, buff=0.3)
        dim_B = Text("3×2", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_SECONDARY).next_to(matrix_B, DOWN, buff=0.3)
        
        self.play(
            Write(label_A),
            Create(matrix_A),
            FadeIn(dim_A),
            run_time=1.0
        )
        self.play(
            Write(label_B),
            Create(matrix_B),
            FadeIn(dim_B),
            run_time=1.0
        )
        
        # 维度匹配说明
        condition = Text(
            "A的列数 = B的行数",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.5)
        
        # 连接3和3
        arrow1 = Arrow(
            dim_A.get_right() + LEFT * 0.3,
            condition.get_top() + UP * 0.1,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        arrow2 = Arrow(
            dim_B.get_left() + RIGHT * 0.3,
            condition.get_top() + UP * 0.1,
            color=self.COLOR_HIGHLIGHT,
            buff=0.1
        )
        
        self.play(
            FadeIn(condition, shift=DOWN * 0.2),
            Create(arrow1),
            Create(arrow2),
            run_time=0.8
        )
        self.wait(0.8)
        
        # 结果维度
        result_dim = Text(
            "结果: 2×2 矩阵",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(result_dim, scale=1.1), run_time=0.6)
        self.wait(1.3)  # 延长等待
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(label_A),
            FadeOut(matrix_A),
            FadeOut(dim_A),
            FadeOut(label_B),
            FadeOut(matrix_B),
            FadeOut(dim_B),
            FadeOut(condition),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(result_dim),
            run_time=0.5
        )
    
    def show_multiplication_detail(self):
        """场景5: 矩阵乘法详细计算 - 计算第一个元素"""
        # 标题
        title = Text(
            "如何计算 c₁₁?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_MULTIPLY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.7)
        
        # 简化的矩阵用于演示
        # A (2×3)
        matrix_A = Matrix(
            [["a_{11}", "a_{12}", "a_{13}"], ["a_{21}", "a_{22}", "a_{23}"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 20},
            h_buff=0.9,
            v_buff=0.5
        ).move_to(LEFT * 2.5 + UP * 3.5)
        matrix_A.set_color(self.COLOR_PRIMARY)
        
        # B (3×2)
        matrix_B = Matrix(
            [["b_{11}", "b_{12}"], ["b_{21}", "b_{22}"], ["b_{31}", "b_{32}"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 20},
            h_buff=0.9,
            v_buff=0.5
        ).move_to(RIGHT * 2.5 + UP * 3.5)
        matrix_B.set_color(self.COLOR_SECONDARY)
        
        self.play(Create(matrix_A), Create(matrix_B), run_time=1.0)
        
        # 高亮第1行和第1列
        row_rect = SurroundingRectangle(
            VGroup(*matrix_A.get_entries()[0:3]),
            color=self.COLOR_PRIMARY,
            buff=0.1
        )
        
        col_rect = SurroundingRectangle(
            VGroup(matrix_B.get_entries()[0], matrix_B.get_entries()[2], matrix_B.get_entries()[4]),
            color=self.COLOR_SECONDARY,
            buff=0.1
        )
        
        self.play(Create(row_rect), run_time=0.5)
        self.play(Create(col_rect), run_time=0.5)
        
        # 说明
        explain1 = Text(
            "取A的第1行",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_PRIMARY
        ).move_to(LEFT * 2.5 + UP * 1.8)
        
        explain2 = Text(
            "取B的第1列",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_SECONDARY
        ).move_to(RIGHT * 2.5 + UP * 1.8)
        
        self.play(FadeIn(explain1), FadeIn(explain2), run_time=0.5)
        self.wait(0.5)
        
        # 计算过程
        calc_title = Text(
            "对应元素相乘，再求和:",
            font="Noto Sans CJK SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 1)
        
        self.play(FadeIn(calc_title), run_time=0.5)
        
        # 分步显示乘积
        product1 = MathTex("a_{11} \\times b_{11}", font_size=24, color=self.COLOR_MULTIPLY).move_to(UP * 0.2)
        product2 = MathTex("a_{12} \\times b_{21}", font_size=24, color=self.COLOR_MULTIPLY).next_to(product1, DOWN, buff=0.3)
        product3 = MathTex("a_{13} \\times b_{31}", font_size=24, color=self.COLOR_MULTIPLY).next_to(product2, DOWN, buff=0.3)
        
        self.play(Write(product1), run_time=0.7)
        self.play(Write(product2), run_time=0.7)
        self.play(Write(product3), run_time=0.7)
        
        # 求和
        plus1 = MathTex("+", font_size=20).move_to(product1.get_right() + RIGHT * 0.3 + DOWN * 0.15)
        plus2 = MathTex("+", font_size=20).move_to(product2.get_right() + RIGHT * 0.3 + DOWN * 0.15)
        
        self.play(Write(plus1), Write(plus2), run_time=0.4)
        
        # Brace 标注求和
        products_group = VGroup(product1, product2, product3)
        brace = Brace(products_group, LEFT, color=self.COLOR_RESULT)
        brace_text = Text("求和", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_RESULT).next_to(brace, LEFT, buff=0.1)
        
        self.play(GrowFromCenter(brace), FadeIn(brace_text), run_time=0.6)
        self.wait(0.5)
        
        # 最终结果
        result = MathTex(
            "c_{11} = a_{11}b_{11} + a_{12}b_{21} + a_{13}b_{31}",
            font_size=22,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 2.5)
        
        self.play(Write(result), run_time=1.2)
        self.wait(2.0)  # 延长等待，让学生理解
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(matrix_A),
            FadeOut(matrix_B),
            FadeOut(row_rect),
            FadeOut(col_rect),
            FadeOut(explain1),
            FadeOut(explain2),
            FadeOut(calc_title),
            FadeOut(products_group),
            FadeOut(plus1),
            FadeOut(plus2),
            FadeOut(brace),
            FadeOut(brace_text),
            FadeOut(result),
            run_time=0.6
        )
    
    def show_multiplication_complete(self):
        """场景6: 矩阵乘法完整示例"""
        # 标题
        title = Text(
            "完整计算",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_MULTIPLY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.6)
        
        # 具体数值的矩阵
        matrix_A = Matrix(
            [["1", "2", "3"], ["4", "5", "6"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 24},
            h_buff=0.7,
            v_buff=0.5
        ).move_to(LEFT * 2 + UP * 3)
        matrix_A.set_color(self.COLOR_PRIMARY)
        
        matrix_B = Matrix(
            [["7", "8"], ["9", "10"], ["11", "12"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 24},
            h_buff=0.7,
            v_buff=0.5
        ).move_to(RIGHT * 2 + UP * 3)
        matrix_B.set_color(self.COLOR_SECONDARY)
        
        times = MathTex("\\times", font_size=32).move_to(UP * 3)
        
        self.play(Create(matrix_A), Write(times), Create(matrix_B), run_time=1.0)
        
        # 提示"同理计算其他元素"
        hint = Text(
            "同理计算其他元素...",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 1.5)
        
        self.play(FadeIn(hint), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(hint), run_time=0.3)
        
        # 快速闪烁计算过程（简化）
        # c11 = 1*7 + 2*9 + 3*11 = 58
        # c12 = 1*8 + 2*10 + 3*12 = 64
        # c21 = 4*7 + 5*9 + 6*11 = 139
        # c22 = 4*8 + 5*10 + 6*12 = 154
        
        calc_labels = [
            "c₁₁ = 58",
            "c₁₂ = 64",
            "c₂₁ = 139",
            "c₂₂ = 154"
        ]
        
        positions = [
            UP * 1 + LEFT * 1,
            UP * 1 + RIGHT * 1,
            UP * 0 + LEFT * 1,
            UP * 0 + RIGHT * 1
        ]
        
        for i, (label_text, pos) in enumerate(zip(calc_labels, positions)):
            label = Text(label_text, font="Noto Sans CJK SC", font_size=22, color=self.COLOR_RESULT).move_to(pos)
            self.play(FadeIn(label, scale=1.2), run_time=0.6)
            if i < 3:
                self.wait(0.3)
        
        self.wait(0.8)
        
        # 最终结果矩阵
        result_matrix = Matrix(
            [["58", "64"], ["139", "154"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28},
            h_buff=0.8,
            v_buff=0.6
        ).move_to(DOWN * 2)
        result_matrix.set_color(self.COLOR_RESULT)
        
        equal = MathTex("=", font_size=40).next_to(result_matrix, LEFT, buff=0.5)
        
        self.play(
            Write(equal),
            Create(result_matrix),
            run_time=1.2
        )
        self.wait(2.0)  # 延长等待
        
        # 清理（保留结果矩阵用于下一场景对比）
        self.play(
            FadeOut(title),
            FadeOut(matrix_A),
            FadeOut(times),
            FadeOut(matrix_B),
            FadeOut(VGroup(*[self.mobjects[i] for i in range(len(self.mobjects)) if isinstance(self.mobjects[i], Text) and "c₁" in str(self.mobjects[i]) or "c₂" in str(self.mobjects[i])])),
            run_time=0.5
        )
        
        # 将结果保存为属性供下一场景使用
        self.ab_result = VGroup(equal, result_matrix)
    
    def show_non_commutative(self):
        """场景7: 交换律不成立"""
        # 标题 - 警示
        title = Text(
            "注意: AB ≠ BA",
            font="Noto Sans CJK SC",
            font_size=36,
            color=RED
        ).move_to(self.TITLE_POS)
        
        # 警告图标
        warning = Text("⚠️", font_size=40).next_to(title, LEFT, buff=0.3)
        
        self.play(
            Write(title),
            FadeIn(warning, scale=1.5),
            run_time=0.8
        )
        
        # AB 的结果（从上一场景移动）
        if hasattr(self, 'ab_result'):
            ab_label = Text("AB =", font="Noto Sans CJK SC", font_size=24).next_to(self.ab_result, LEFT, buff=0.3)
            
            self.play(
                self.ab_result.animate.scale(0.7).move_to(UP * 2.5),
                FadeIn(ab_label),
                run_time=0.8
            )
        else:
            # 备用：直接创建
            ab_result = Matrix(
                [["58", "64"], ["139", "154"]],
                left_bracket="[",
                right_bracket="]",
                element_to_mobject_config={"font_size": 20}
            ).scale(0.7).move_to(UP * 2.5)
            ab_result.set_color(self.COLOR_RESULT)
            ab_label = Text("AB =", font="Noto Sans CJK SC", font_size=24).next_to(ab_result, LEFT, buff=0.3)
            self.play(Create(ab_result), FadeIn(ab_label), run_time=0.8)
        
        # BA 的结果（注意：B是3×2，A是2×3，BA是3×3）
        ba_result = Matrix(
            [["39", "54", "69"], ["49", "68", "87"], ["59", "82", "105"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 18},
            h_buff=0.6,
            v_buff=0.4
        ).scale(0.6).move_to(UP * 0.5)
        ba_result.set_color(self.COLOR_SECONDARY)
        
        ba_label = Text("BA =", font="Noto Sans CJK SC", font_size=24).next_to(ba_result, LEFT, buff=0.3)
        
        self.play(
            FadeIn(ba_label),
            Create(ba_result),
            run_time=1.0
        )
        
        # 不等号
        not_equal = MathTex("\\neq", font_size=50, color=RED).move_to(UP * 1.5 + RIGHT * 3)
        self.play(Write(not_equal), run_time=0.5)
        
        # 叉号强调
        cross = Text("✗", font_size=60, color=RED).next_to(not_equal, RIGHT, buff=0.3)
        self.play(FadeIn(cross, scale=1.5), run_time=0.4)
        
        # 原因说明
        reason = Text(
            "维度不同 & 计算顺序不同",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(reason), run_time=0.7)
        self.wait(2.0)  # 延长等待，强调重点
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(warning),
            FadeOut(self.ab_result if hasattr(self, 'ab_result') else ab_result),
            FadeOut(ab_label),
            FadeOut(ba_result),
            FadeOut(ba_label),
            FadeOut(not_equal),
            FadeOut(cross),
            FadeOut(reason),
            run_time=0.6
        )
    
    def show_properties_summary(self):
        """场景8: 其他性质与总结"""
        # 标题
        title = Text(
            "重要性质",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.7)
        
        # 性质列表
        properties = VGroup()
        
        # 结合律
        prop1 = MathTex("(AB)C = A(BC)", font_size=26, color=WHITE).move_to(UP * 3.5)
        prop1_label = Text("结合律", font="Noto Sans CJK SC", font_size=20, color=GRAY_A).next_to(prop1, LEFT, buff=0.5)
        properties.add(VGroup(prop1_label, prop1))
        
        # 分配律
        prop2 = MathTex("A(B + C) = AB + AC", font_size=26, color=WHITE).move_to(UP * 2.5)
        prop2_label = Text("分配律", font="Noto Sans CJK SC", font_size=20, color=GRAY_A).next_to(prop2, LEFT, buff=0.5)
        properties.add(VGroup(prop2_label, prop2))
        
        # 单位矩阵
        prop3 = MathTex("EA = AE = A", font_size=26, color=self.COLOR_RESULT).move_to(UP * 1.5)
        prop3_label = Text("单位矩阵", font="Noto Sans CJK SC", font_size=20, color=GRAY_A).next_to(prop3, LEFT, buff=0.5)
        properties.add(VGroup(prop3_label, prop3))
        
        # 零矩阵
        prop4 = MathTex("A \\cdot O = O", font_size=26, color=GRAY).move_to(UP * 0.5)
        prop4_label = Text("零矩阵", font="Noto Sans CJK SC", font_size=20, color=GRAY_A).next_to(prop4, LEFT, buff=0.5)
        properties.add(VGroup(prop4_label, prop4))
        
        # 依次显示
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT * 0.3), run_time=0.8)
            self.wait(0.4)
        
        # 三种运算回顾
        summary_title = Text(
            "三种运算回顾",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 运算图标
        add_icon = MathTex("+", font_size=40, color=self.COLOR_PRIMARY).move_to(DOWN * 2 + LEFT * 2)
        add_label = Text("加法", font="Noto Sans CJK SC", font_size=18).next_to(add_icon, DOWN, buff=0.2)
        
        scalar_icon = MathTex("k\\cdot", font_size=40, color=self.COLOR_SECONDARY).move_to(DOWN * 2)
        scalar_label = Text("数乘", font="Noto Sans CJK SC", font_size=18).next_to(scalar_icon, DOWN, buff=0.2)
        
        mult_icon = MathTex("\\times", font_size=40, color=self.COLOR_MULTIPLY).move_to(DOWN * 2 + RIGHT * 2)
        mult_label = Text("乘法", font="Noto Sans CJK SC", font_size=18).next_to(mult_icon, DOWN, buff=0.2)
        
        icons = VGroup(
            VGroup(add_icon, add_label),
            VGroup(scalar_icon, scalar_label),
            VGroup(mult_icon, mult_label)
        )
        
        for icon in icons:
            self.play(FadeIn(icon, scale=1.2), run_time=0.4)
        
        self.wait(1.0)
        
        # 片尾关注
        outro = Text(
            "关注我, 学更多矩阵技巧!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_RESULT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(outro, shift=UP * 0.3), run_time=0.6)
        
        # 装饰
        stars = VGroup(*[
            Text("★", font_size=30, color=GOLD).move_to(
                outro.get_center() + 1.8 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(star, scale=0.5) for star in stars],
            run_time=0.5
        )
        self.play(Rotate(stars, angle=PI/3, run_time=1.0))
        
        self.wait(2.0)  # 延长片尾等待
        
        # 全部淡出
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.0
        )


# 运行命令:
# manim -pql matrix_operations.py MatrixOperations  # 快速预览
# manim -qh matrix_operations.py MatrixOperations   # 高质量 1080p
# manim -qk matrix_operations.py MatrixOperations   # 4K质量