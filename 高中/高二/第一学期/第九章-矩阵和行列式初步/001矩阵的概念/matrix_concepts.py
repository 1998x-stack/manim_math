"""
矩阵的概念 - Matrix Concepts
使用 Manim 创建的高中数学教学视频

内容: 矩阵定义、行矩阵、列矩阵、方阵、零矩阵、单位矩阵、矩阵相等
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


class MatrixConcepts(Scene):
    """
    矩阵概念教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 矩阵的定义
    3. 行矩阵
    4. 列矩阵
    5. 方阵
    6. 零矩阵
    7. 单位矩阵
    8. 矩阵相等与总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要矩阵
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 强调元素
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_SPECIAL = "#2ecc71"       # 绿色 - 特殊矩阵
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        
        # 初始化全局元素
        self.setup_globals()
        
        # 执行动画序列
        self.show_opening()
        self.show_matrix_definition()
        self.show_row_matrix()
        self.show_column_matrix()
        self.show_square_matrix()
        self.show_zero_matrix()
        self.show_unit_matrix()
        self.show_equality_and_summary()
    
    def setup_globals(self):
        """初始化全局配置和常驻元素"""
        # 作者信息 (持续显示)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.add(self.author_info)
        
        # 矩阵显示的标准位置
        self.MATRIX_CENTER = UP * 2
        self.TITLE_POS = UP * 6
        self.EXPLAIN_POS = DOWN * 4.5
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 钩子问题
        hook = Text(
            "如何存储表格数据?",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.TITLE_POS)
        
        self.play(Write(hook), run_time=1.0)
        self.wait(0.5)
        
        # 简单数据表格
        table_data = [
            ["90", "85", "92"],
            ["88", "91", "87"]
        ]
        
        table = Table(
            table_data,
            include_outer_lines=True,
            line_config={"stroke_width": 2, "color": self.COLOR_PRIMARY}
        ).scale(0.6).move_to(UP * 2)
        
        # 标签
        row_labels = VGroup(
            Text("小明", font="PingFang SC", font_size=20).next_to(table.get_rows()[0], LEFT, buff=0.3),
            Text("小红", font="PingFang SC", font_size=20).next_to(table.get_rows()[1], LEFT, buff=0.3)
        )
        
        col_labels = VGroup(
            Text("数学", font="PingFang SC", font_size=20).next_to(table.get_columns()[0], UP, buff=0.3),
            Text("英语", font="PingFang SC", font_size=20).next_to(table.get_columns()[1], UP, buff=0.3),
            Text("物理", font="PingFang SC", font_size=20).next_to(table.get_columns()[2], UP, buff=0.3)
        )
        
        self.play(Create(table), run_time=1.2)
        self.play(
            FadeIn(row_labels, shift=RIGHT * 0.2),
            FadeIn(col_labels, shift=DOWN * 0.2),
            run_time=0.8
        )
        
        # 闪烁效果
        self.play(
            Flash(table, color=self.COLOR_HIGHLIGHT, flash_radius=1.0),
            run_time=0.5
        )
        
        # 过渡文字
        transition = Text(
            "矩阵来帮忙!",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_SPECIAL
        ).move_to(self.EXPLAIN_POS)
        
        self.play(FadeIn(transition, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)  # 延长等待时间
        
        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(table),
            FadeOut(row_labels),
            FadeOut(col_labels),
            FadeOut(transition),
            run_time=0.6
        )
    
    def show_matrix_definition(self):
        """场景2: 矩阵的定义"""
        # 标题
        title = Text(
            "矩阵的定义",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建一般矩阵 (3×4)
        matrix_array = [
            ["a_{11}", "a_{12}", "a_{13}", "a_{14}"],
            ["a_{21}", "a_{22}", "a_{23}", "a_{24}"],
            ["a_{31}", "a_{32}", "a_{33}", "a_{34}"]
        ]
        
        matrix = Matrix(
            matrix_array,
            left_bracket="(",
            right_bracket=")",
            element_to_mobject_config={"font_size": 24},
            h_buff=1.2,
            v_buff=0.8
        ).move_to(self.MATRIX_CENTER)
        
        matrix.set_color(self.COLOR_PRIMARY)
        
        self.play(Create(matrix), run_time=2.0)
        self.wait(0.5)
        
        # 高亮某个元素
        highlight_element = matrix.get_entries()[6]  # a_{23}
        self.play(
            Indicate(highlight_element, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            run_time=0.8
        )
        
        # 元素说明
        element_label = MathTex(
            r"a_{ij}",
            font_size=32,
            color=self.COLOR_SECONDARY
        ).next_to(matrix, RIGHT, buff=0.8)
        
        element_explain = Text(
            "第i行第j列的元素",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).next_to(element_label, DOWN, buff=0.2)
        
        self.play(
            FadeIn(element_label, shift=LEFT * 0.3),
            FadeIn(element_explain),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 行列标注
        row_brace = Brace(matrix, LEFT, color=self.COLOR_SECONDARY)
        row_label = Text("m行", font="PingFang SC", font_size=22, color=self.COLOR_SECONDARY).next_to(row_brace, LEFT, buff=0.2)
        
        col_brace = Brace(matrix, UP, color=self.COLOR_SECONDARY)
        col_label = Text("n列", font="PingFang SC", font_size=22, color=self.COLOR_SECONDARY).next_to(col_brace, UP, buff=0.2)
        
        self.play(
            GrowFromCenter(row_brace),
            FadeIn(row_label),
            run_time=0.6
        )
        self.play(
            GrowFromCenter(col_brace),
            FadeIn(col_label),
            run_time=0.6
        )
        
        # 记号
        notation = MathTex(
            r"A = (a_{ij})_{m \times n}",
            font_size=32,
            color=WHITE
        ).move_to(self.EXPLAIN_POS)
        
        self.play(Write(notation), run_time=1.0)
        
        # 说明
        explain = Text(
            "m×n 表示 m 行 n 列",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).next_to(notation, DOWN, buff=0.3)
        
        self.play(FadeIn(explain), run_time=0.6)
        self.wait(2.0)  # 延长等待，让学生理解核心概念
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(matrix),
            FadeOut(element_label),
            FadeOut(element_explain),
            FadeOut(row_brace),
            FadeOut(row_label),
            FadeOut(col_brace),
            FadeOut(col_label),
            FadeOut(notation),
            FadeOut(explain),
            run_time=0.6
        )
    
    def show_row_matrix(self):
        """场景3: 行矩阵"""
        # 标题
        title = Text(
            "行矩阵 (1×n)",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SPECIAL
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.8)
        
        # 行矩阵示例
        row_matrix = Matrix(
            [["1", "2", "3", "4"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32},
            h_buff=1.0
        ).move_to(self.MATRIX_CENTER)
        
        row_matrix.set_color(self.COLOR_SPECIAL)
        
        self.play(Create(row_matrix), run_time=1.0)
        
        # 维度标注
        dimension = Text(
            "1行4列",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SECONDARY
        ).next_to(row_matrix, DOWN, buff=0.8)
        
        self.play(FadeIn(dimension, shift=UP * 0.2), run_time=0.5)
        
        # 特点高亮
        highlight = Text(
            "只有 1 行",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.EXPLAIN_POS)
        
        self.play(FadeIn(highlight, scale=1.1), run_time=0.6)
        self.wait(0.5)
        
        # 应用说明
        application = Text(
            "常用于表示: 向量、坐标、数据序列",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).next_to(highlight, DOWN, buff=0.3)
        
        self.play(FadeIn(application), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(row_matrix),
            FadeOut(dimension),
            FadeOut(highlight),
            FadeOut(application),
            run_time=0.6
        )
    
    def show_column_matrix(self):
        """场景4: 列矩阵"""
        # 标题
        title = Text(
            "列矩阵 (m×1)",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SPECIAL
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.8)
        
        # 列矩阵示例
        col_matrix = Matrix(
            [["5"], ["6"], ["7"], ["8"]],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 32},
            v_buff=0.6
        ).move_to(self.MATRIX_CENTER)
        
        col_matrix.set_color(self.COLOR_SPECIAL)
        
        self.play(Create(col_matrix), run_time=1.0)
        
        # 维度标注
        dimension = Text(
            "4行1列",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SECONDARY
        ).next_to(col_matrix, RIGHT, buff=0.8)
        
        self.play(FadeIn(dimension, shift=LEFT * 0.2), run_time=0.5)
        
        # 特点高亮
        highlight = Text(
            "只有 1 列",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.EXPLAIN_POS)
        
        self.play(FadeIn(highlight, scale=1.1), run_time=0.6)
        self.wait(0.5)
        
        # 对比说明
        compare = Text(
            "行矩阵的转置",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).next_to(highlight, DOWN, buff=0.3)
        
        self.play(FadeIn(compare), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(col_matrix),
            FadeOut(dimension),
            FadeOut(highlight),
            FadeOut(compare),
            run_time=0.6
        )
    
    def show_square_matrix(self):
        """场景5: 方阵"""
        # 标题
        title = Text(
            "方阵 (n×n)",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.8)
        
        # 方阵示例
        square_matrix = Matrix(
            [
                ["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"]
            ],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28},
            h_buff=0.9,
            v_buff=0.7
        ).move_to(self.MATRIX_CENTER)
        
        square_matrix.set_color(self.COLOR_PRIMARY)
        
        self.play(Create(square_matrix), run_time=1.2)
        
        # 维度标注
        dimension = Text(
            "3行3列 (行数 = 列数)",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_SECONDARY
        ).next_to(square_matrix, DOWN, buff=0.8)
        
        self.play(FadeIn(dimension, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)
        
        # 主对角线高亮
        diagonal_elements = [
            square_matrix.get_entries()[0],  # 1
            square_matrix.get_entries()[4],  # 5
            square_matrix.get_entries()[8]   # 9
        ]
        
        for elem in diagonal_elements:
            self.play(
                Indicate(elem, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
                run_time=0.3
            )
        
        # 对角线说明
        diagonal_label = Text(
            "主对角线",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.EXPLAIN_POS)
        
        diagonal_explain = Text(
            "从左上到右下的元素",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).next_to(diagonal_label, DOWN, buff=0.2)
        
        self.play(
            FadeIn(diagonal_label, scale=1.1),
            FadeIn(diagonal_explain),
            run_time=0.8
        )
        self.wait(2.0)  # 延长等待
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(square_matrix),
            FadeOut(dimension),
            FadeOut(diagonal_label),
            FadeOut(diagonal_explain),
            run_time=0.6
        )
    
    def show_zero_matrix(self):
        """场景6: 零矩阵"""
        # 标题
        title = Text(
            "零矩阵",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SECONDARY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.8)
        
        # 先创建普通矩阵
        normal_matrix = Matrix(
            [
                ["a", "b", "c"],
                ["d", "e", "f"]
            ],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28},
            h_buff=0.9,
            v_buff=0.7
        ).move_to(self.MATRIX_CENTER)
        
        self.play(Create(normal_matrix), run_time=0.8)
        self.wait(0.3)
        
        # 变换为零矩阵
        zero_matrix = Matrix(
            [
                ["0", "0", "0"],
                ["0", "0", "0"]
            ],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28},
            h_buff=0.9,
            v_buff=0.7
        ).move_to(self.MATRIX_CENTER)
        
        zero_matrix.set_color(self.COLOR_SECONDARY)
        
        self.play(Transform(normal_matrix, zero_matrix), run_time=1.2)
        self.wait(0.5)
        
        # 特点强调
        feature = Text(
            "所有元素都是 0",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(self.EXPLAIN_POS)
        
        self.play(FadeIn(feature, scale=1.1), run_time=0.6)
        
        # 记号
        notation = MathTex(
            r"O",
            font_size=32,
            color=WHITE
        ).next_to(feature, DOWN, buff=0.4)
        
        notation_text = Text(
            " 或 ",
            font="PingFang SC",
            font_size=28,
            color=WHITE
        ).next_to(notation, RIGHT, buff=0.1)
        
        notation_zero = MathTex(
            r"0",
            font_size=32,
            color=WHITE
        ).next_to(notation_text, RIGHT, buff=0.1)
        
        notation_group = VGroup(notation, notation_text, notation_zero)
        
        self.play(Write(notation_group), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(normal_matrix),
            FadeOut(feature),
            FadeOut(notation_group),
            run_time=0.6
        )
    
    def show_unit_matrix(self):
        """场景7: 单位矩阵"""
        # 标题
        title = Text(
            "单位矩阵 E",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_SPECIAL
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.8)
        
        # 单位矩阵
        unit_matrix = Matrix(
            [
                ["1", "0", "0"],
                ["0", "1", "0"],
                ["0", "0", "1"]
            ],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28},
            h_buff=0.9,
            v_buff=0.7
        ).move_to(self.MATRIX_CENTER)
        
        self.play(Create(unit_matrix), run_time=1.2)
        self.wait(0.5)
        
        # 主对角线为1闪烁
        diagonal_ones = [
            unit_matrix.get_entries()[0],  # 第一个1
            unit_matrix.get_entries()[4],  # 第二个1
            unit_matrix.get_entries()[8]   # 第三个1
        ]
        
        for elem in diagonal_ones:
            elem.set_color(self.COLOR_SPECIAL)
            self.play(
                Flash(elem, color=self.COLOR_HIGHLIGHT, flash_radius=0.3),
                run_time=0.4
            )
        
        # 其余元素变灰
        other_entries = [unit_matrix.get_entries()[i] for i in [1, 2, 3, 5, 6, 7]]
        self.play(
            *[entry.animate.set_color(GRAY) for entry in other_entries],
            run_time=0.6
        )
        
        # 特点说明
        feature1 = Text(
            "主对角线为 1",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_SPECIAL
        ).move_to(self.EXPLAIN_POS + UP * 0.5)
        
        feature2 = Text(
            "其余元素为 0",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).next_to(feature1, DOWN, buff=0.3)
        
        self.play(
            FadeIn(feature1, shift=UP * 0.2),
            FadeIn(feature2, shift=UP * 0.2),
            run_time=0.8
        )
        
        # 重要性提示
        important = Text(
            "矩阵运算中的 \"1\"",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).next_to(feature2, DOWN, buff=0.5)
        
        self.play(FadeIn(important, scale=1.1), run_time=0.6)
        self.wait(2.0)  # 延长等待，强调重要性
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(unit_matrix),
            FadeOut(feature1),
            FadeOut(feature2),
            FadeOut(important),
            run_time=0.6
        )
    
    def show_equality_and_summary(self):
        """场景8: 矩阵相等与总结"""
        # 标题
        title = Text(
            "矩阵相等",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(self.TITLE_POS)
        
        self.play(Write(title), run_time=0.8)
        
        # 两个矩阵
        matrix_A = Matrix(
            [
                ["1", "2"],
                ["3", "4"]
            ],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28}
        ).move_to(UP * 3 + LEFT * 2)
        
        matrix_B = Matrix(
            [
                ["1", "2"],
                ["3", "4"]
            ],
            left_bracket="[",
            right_bracket="]",
            element_to_mobject_config={"font_size": 28}
        ).move_to(UP * 3 + RIGHT * 2)
        
        label_A = MathTex("A =", font_size=32).next_to(matrix_A, LEFT, buff=0.3)
        label_B = MathTex("B =", font_size=32).next_to(matrix_B, LEFT, buff=0.3)
        
        self.play(
            Write(label_A),
            Create(matrix_A),
            run_time=0.8
        )
        self.play(
            Write(label_B),
            Create(matrix_B),
            run_time=0.8
        )
        
        # 等号
        equal_sign = MathTex("=", font_size=48, color=self.COLOR_HIGHLIGHT).move_to(UP * 3)
        self.play(Write(equal_sign), run_time=0.4)
        
        # 条件1: 同型
        condition1 = Text(
            "条件1: 同型矩阵 (行列数相同)",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).move_to(UP * 1)
        
        self.play(FadeIn(condition1, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)
        
        # 条件2: 对应元素相等
        condition2 = Text(
            "条件2: 对应位置元素相等",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).next_to(condition1, DOWN, buff=0.4)
        
        self.play(FadeIn(condition2, shift=UP * 0.2), run_time=0.8)
        
        # 逐个对应元素闪烁
        for i in range(4):
            self.play(
                Indicate(matrix_A.get_entries()[i], color=self.COLOR_HIGHLIGHT),
                Indicate(matrix_B.get_entries()[i], color=self.COLOR_HIGHLIGHT),
                run_time=0.3
            )
        
        self.wait(1.0)
        
        # 缩小到顶部
        all_equality = VGroup(label_A, matrix_A, equal_sign, matrix_B, label_B, condition1, condition2)
        self.play(
            all_equality.animate.scale(0.5).move_to(UP * 5.5),
            FadeOut(title),
            run_time=0.8
        )
        
        # 五种矩阵快速回顾
        summary_title = Text(
            "矩阵的五种基本形式",
            font="PingFang SC",
            font_size=32,
            color=GOLD
        ).move_to(UP * 3.5)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 创建五个小图标
        icons = VGroup()
        
        # 行矩阵图标
        icon1 = Matrix(
            [["\\square", "\\square", "\\square"]],
            element_to_mobject_config={"font_size": 16},
            h_buff=0.3
        ).scale(0.5)
        label1 = Text("行矩阵", font="PingFang SC", font_size=16).next_to(icon1, DOWN, buff=0.1)
        group1 = VGroup(icon1, label1)
        
        # 列矩阵图标
        icon2 = Matrix(
            [["\\square"], ["\\square"], ["\\square"]],
            element_to_mobject_config={"font_size": 16},
            v_buff=0.3
        ).scale(0.5)
        label2 = Text("列矩阵", font="PingFang SC", font_size=16).next_to(icon2, DOWN, buff=0.1)
        group2 = VGroup(icon2, label2)
        
        # 方阵图标
        icon3 = Matrix(
            [["\\square", "\\square"], ["\\square", "\\square"]],
            element_to_mobject_config={"font_size": 16},
            h_buff=0.3,
            v_buff=0.3
        ).scale(0.5)
        label3 = Text("方阵", font="PingFang SC", font_size=16).next_to(icon3, DOWN, buff=0.1)
        group3 = VGroup(icon3, label3)
        
        # 零矩阵图标
        icon4 = Matrix(
            [["0", "0"], ["0", "0"]],
            element_to_mobject_config={"font_size": 16},
            h_buff=0.3,
            v_buff=0.3
        ).scale(0.5)
        label4 = Text("零矩阵", font="PingFang SC", font_size=16).next_to(icon4, DOWN, buff=0.1)
        group4 = VGroup(icon4, label4)
        
        # 单位矩阵图标
        icon5 = Matrix(
            [["1", "0"], ["0", "1"]],
            element_to_mobject_config={"font_size": 16},
            h_buff=0.3,
            v_buff=0.3
        ).scale(0.5)
        label5 = Text("单位矩阵", font="PingFang SC", font_size=16).next_to(icon5, DOWN, buff=0.1)
        group5 = VGroup(icon5, label5)
        
        icons = VGroup(group1, group2, group3, group4, group5).arrange(RIGHT, buff=0.6).move_to(UP * 1.5)
        
        # 依次闪现
        for icon_group in icons:
            self.play(FadeIn(icon_group, scale=0.8), run_time=0.4)
        
        self.wait(1.5)  # 延长等待
        
        # 关键提示
        key_point = Text(
            "掌握这五种, 解题更轻松!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(key_point, scale=1.1), run_time=0.6)
        self.wait(1.0)
        
        # 片尾关注
        outro_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_SPECIAL
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(outro_text, shift=UP * 0.3), run_time=0.6)
        
        # 装饰元素
        decorations = VGroup(*[
            Square(side_length=0.2, color=GOLD, fill_opacity=0.8)
            .move_to(outro_text.get_center() + 1.5 * np.array([np.cos(i * PI / 4), np.sin(i * PI / 4), 0]))
            for i in range(8)
        ])
        
        self.play(
            *[FadeIn(deco, scale=0.5) for deco in decorations],
            run_time=0.6
        )
        self.play(Rotate(decorations, angle=PI / 2, run_time=1.2))
        
        self.wait(2.0)  # 延长最后的停留时间
        
        # 全部淡出
        self.play(
            FadeOut(all_equality),
            FadeOut(summary_title),
            FadeOut(icons),
            FadeOut(key_point),
            FadeOut(outro_text),
            FadeOut(decorations),
            FadeOut(self.author_info),
            run_time=1.0
        )


# 运行命令:
# manim -pql matrix_concepts.py MatrixConcepts  # 快速预览
# manim -qh matrix_concepts.py MatrixConcepts   # 高质量 1080p
# manim -qk matrix_concepts.py MatrixConcepts   # 4K质量