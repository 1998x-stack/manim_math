"""
数列的概念 - Manim 教学动画
Sequence Concept - Educational Animation

知识点: 高二数学 - 数列的概念
目标受众: 高中学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
1. 开场钩子 - 生活中的数列
2. 数列的定义
3. 数列与函数的关系
4. 数列的表示方法
5. 数列的分类
6. 前n项和
7. 总结关注
"""

from manim import *
import numpy as np


# ========== 全局配置 - TikTok 竖屏尺寸 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class SequenceConcept(Scene):
    """
    数列概念教学动画场景
    
    本动画通过视觉化展示帮助学生理解：
    1. 数列的本质 - 有序排列的数
    2. 数列作为函数的理解
    3. 数列的多种表示方法
    4. 数列的分类
    5. 前n项和的概念
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主要元素
        self.COLOR_SECONDARY = "#2ecc71"    # 绿色 - 次要元素
        self.COLOR_HIGHLIGHT = "#e74c3c"    # 红色 - 高亮强调
        self.COLOR_FORMULA = "#f39c12"      # 橙色 - 公式
        self.COLOR_AUXILIARY = "#95a5a6"    # 灰色 - 辅助线
        self.COLOR_SEQUENCE = "#9b59b6"     # 紫色 - 数列点
        
        # 初始化几何数据和配置
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()           # 0-6s
        self.scene_2_definition()        # 6-16s
        self.scene_3_as_function()       # 16-26s
        self.scene_4_representations()   # 26-45s
        self.scene_5_classifications()   # 45-58s
        self.scene_6_sum()               # 58-70s
        self.scene_7_summary()           # 70-85s
    
    def setup_geometry(self):
        """初始化所有数据和配置"""
        print("🔧 初始化几何数据...")
        
        # ===== 示例数列: aₙ = 2n =====
        self.example_sequence = [2, 4, 6, 8, 10, 12, 14, 16]
        self.sequence_indices = list(range(1, 9))  # n = 1, 2, ..., 8
        
        # ===== 坐标系配置 =====
        self.axes_x_range = [0, 9, 1]
        self.axes_y_range = [0, 18, 2]
        self.axes_width = 7.0
        self.axes_height = 4.5
        self.axes_offset = UP * 1.5
        
        # ===== 字体大小 =====
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        self.FONT_AUTHOR = 20
        
        # ===== 验证边界 =====
        self._verify_setup()
        
        print("✅ 几何数据初始化完成")
    
    def _verify_setup(self):
        """验证配置的合理性"""
        # 验证坐标系不会超出边界
        axes_left = self.axes_offset[0] - self.axes_width / 2
        axes_right = self.axes_offset[0] + self.axes_width / 2
        axes_bottom = self.axes_offset[1] - self.axes_height / 2
        axes_top = self.axes_offset[1] + self.axes_height / 2
        
        assert -4 <= axes_left <= 4, f"坐标系左边界超限: {axes_left}"
        assert -4 <= axes_right <= 4, f"坐标系右边界超限: {axes_right}"
        assert -7 <= axes_bottom <= 7, f"坐标系下边界超限: {axes_bottom}"
        assert -7 <= axes_top <= 7, f"坐标系上边界超限: {axes_top}"
        
        print("✓ 边界验证通过")
    
    # ========== Scene 1: 开场钩子 (0-6秒) ==========
    def scene_1_opening(self):
        """场景1: 吸引注意力，引出数列概念"""
        
        # 作者信息 (顶部，全程保留)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_AUTHOR,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "1, 2, 3, 5, 8, 13, 21...\n发现规律了吗?",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.0)
        self.wait(0.5)
        
        # 生活场景示例 - 楼层号
        floor_label = Text(
            "生活中的数列: 楼层号",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 3)
        
        # 楼层号码: 1F, 2F, 3F, 4F, 5F
        floor_numbers = VGroup(*[
            VGroup(
                Text(f"{i}", font="Arial", font_size=32, color=WHITE, weight=BOLD),
                Text("F", font="Arial", font_size=24, color=self.COLOR_AUXILIARY)
            ).arrange(RIGHT, buff=0.05)
            for i in range(1, 6)
        ]).arrange(RIGHT, buff=0.5).move_to(UP * 1.5)
        
        self.play(FadeIn(floor_label, shift=UP * 0.2), run_time=0.4)
        self.play(
            LaggedStart(*[
                FadeIn(floor, scale=0.8) for floor in floor_numbers
            ], lag_ratio=0.2),
            run_time=1.0
        )
        
        # 闪烁高亮
        for floor in floor_numbers:
            self.play(Flash(floor, color=self.COLOR_HIGHLIGHT, flash_radius=0.3), run_time=0.15)
        
        self.wait(0.5)
        
        # 引出数列概念
        concept_text = Text(
            "这就是数学中的——数列!",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(concept_text, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(floor_label),
            FadeOut(floor_numbers),
            FadeOut(concept_text),
            run_time=0.5
        )
    
    # ========== Scene 2: 数列的定义 (6-16秒) ==========
    def scene_2_definition(self):
        """场景2: 讲解数列的严格定义和记号"""
        
        # 标题
        title = Text(
            "数列的概念",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 定义文字
        definition = Text(
            "按照一定顺序排列的一列数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=WHITE
        ).move_to(UP * 4.8)
        
        self.play(Write(definition), run_time=0.8)
        self.wait(1.0)
        
        # 数列记号
        notation_label = Text(
            "记作:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 3.2)
        
        notation = MathTex(
            r"\{a_n\} = a_1, a_2, a_3, \ldots, a_n, \ldots",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(UP * 2.2)
        
        self.play(FadeIn(notation_label), run_time=0.3)
        self.play(Write(notation), run_time=1.0)
        self.wait(0.5)
        
        # 逐项说明
        explanations = VGroup(
            VGroup(
                MathTex(r"a_1", font_size=28, color=self.COLOR_HIGHLIGHT),
                Text(": 第1项", font="Noto Sans CJK SC", font_size=self.FONT_SMALL, color=WHITE)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"a_2", font_size=28, color=self.COLOR_HIGHLIGHT),
                Text(": 第2项", font="Noto Sans CJK SC", font_size=self.FONT_SMALL, color=WHITE)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"a_n", font_size=28, color=self.COLOR_HIGHLIGHT),
                Text(": 第n项 (通项)", font="Noto Sans CJK SC", font_size=self.FONT_SMALL, color=WHITE)
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(UP * 0.3)
        
        for i, exp in enumerate(explanations):
            self.play(FadeIn(exp, shift=RIGHT * 0.3), run_time=0.4)
            if i < len(explanations) - 1:
                self.wait(0.2)
        
        self.wait(1.0)
        
        # 通项公式
        general_term_label = Text(
            "通项公式:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 2.0)
        
        general_term = MathTex(
            r"a_n = f(n)",
            font_size=32,
            color=self.COLOR_FORMULA
        ).next_to(general_term_label, DOWN, buff=0.3)
        
        self.play(
            FadeIn(general_term_label),
            FadeIn(general_term, shift=UP * 0.2),
            run_time=0.6
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(notation_label),
            FadeOut(explanations),
            FadeOut(general_term_label),
            FadeOut(general_term),
            run_time=0.5
        )
        
        # 保留notation作为参考（移到顶部）
        self.notation_ref = notation.copy().scale(0.7).move_to(UP * 6.5)
        self.play(Transform(notation, self.notation_ref), run_time=0.4)
        self.remove(notation)
        self.add(self.notation_ref)
    
    # ========== Scene 3: 数列与函数 (16-26秒) ==========
    def scene_3_as_function(self):
        """场景3: 揭示数列的函数本质"""
        
        # 标题
        title = Text(
            "数列的函数本质",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 创建坐标系
        self.axes = Axes(
            x_range=self.axes_x_range,
            y_range=self.axes_y_range,
            x_length=self.axes_width,
            y_length=self.axes_height,
            axis_config={
                "include_numbers": True,
                "font_size": 18,
                "color": self.COLOR_AUXILIARY
            },
            tips=False
        ).move_to(self.axes_offset)
        
        # 坐标轴标签
        x_label = MathTex("n", font_size=24, color=WHITE).next_to(
            self.axes.x_axis.get_end(), RIGHT, buff=0.2
        )
        y_label = MathTex("a_n", font_size=24, color=WHITE).next_to(
            self.axes.y_axis.get_end(), UP, buff=0.2
        )
        
        self.play(Create(self.axes), run_time=1.0)
        self.play(FadeIn(x_label), FadeIn(y_label), run_time=0.4)
        
        # 说明文字
        explanation = Text(
            "定义在正整数集上的函数",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 4.5)
        
        mapping = MathTex(
            r"n \to a_n",
            font_size=28,
            color=self.COLOR_FORMULA
        ).next_to(explanation, DOWN, buff=0.3)
        
        self.play(FadeIn(explanation), FadeIn(mapping), run_time=0.6)
        self.wait(0.8)
        
        # 绘制数列点 (aₙ = 2n)
        self.sequence_dots = VGroup(*[
            Dot(
                self.axes.c2p(n, 2*n),
                color=self.COLOR_SEQUENCE,
                radius=0.08
            )
            for n in self.sequence_indices
        ])
        
        # 点标签
        dot_labels = VGroup(*[
            MathTex(f"({n},{2*n})", font_size=14, color=self.COLOR_AUXILIARY)
            .next_to(self.sequence_dots[i], UR, buff=0.08)
            for i, n in enumerate(self.sequence_indices)
        ])
        
        # 逐个绘制点
        self.play(
            LaggedStart(*[
                GrowFromCenter(dot) for dot in self.sequence_dots
            ], lag_ratio=0.15),
            run_time=2.0
        )
        
        # 显示部分标签（避免拥挤）
        selected_labels = VGroup(dot_labels[0], dot_labels[3], dot_labels[7])
        self.play(
            LaggedStart(*[
                FadeIn(label, scale=0.5) for label in selected_labels
            ], lag_ratio=0.2),
            run_time=0.8
        )
        
        # 箭头指示对应关系
        arrow_1 = Arrow(
            self.axes.c2p(1, 0) + DOWN * 0.3,
            self.axes.c2p(1, 2) + DOWN * 0.1,
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(Create(arrow_1), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(mapping),
            FadeOut(selected_labels),
            FadeOut(arrow_1),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(self.notation_ref),
            run_time=0.5
        )
        
        # 保留坐标系和点，用于下一场景
    
    # ========== Scene 4: 数列的表示方法 (26-45秒) ==========
    def scene_4_representations(self):
        """场景4: 介绍四种表示方法"""
        
        # 4.1 通项公式法 (26-31秒)
        self._show_general_formula()
        
        # 4.2 递推公式法 (31-36秒)
        self._show_recursive_formula()
        
        # 4.3 列表法 (36-40秒)
        self._show_table_method()
        
        # 4.4 图像法 (40-45秒)
        self._show_graph_method()
    
    def _show_general_formula(self):
        """4.1 通项公式法"""
        title = Text(
            "① 通项公式法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)
        
        # 公式
        formula = MathTex(
            r"a_n = 2n",
            font_size=36,
            color=self.COLOR_FORMULA
        ).move_to(UP * 5)
        
        self.play(Write(formula), run_time=0.6)
        
        # 验证几项
        verifications = VGroup(
            MathTex(r"a_1 = 2 \times 1 = 2", font_size=24, color=WHITE),
            MathTex(r"a_2 = 2 \times 2 = 4", font_size=24, color=WHITE),
            MathTex(r"a_5 = 2 \times 5 = 10", font_size=24, color=WHITE)
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 5)
        
        for ver in verifications:
            self.play(FadeIn(ver, shift=UP * 0.2), run_time=0.4)
        
        # 优点
        advantage = Text(
            "✓ 可直接计算任意项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(advantage), run_time=0.4)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(verifications),
            FadeOut(advantage),
            run_time=0.4
        )
    
    def _show_recursive_formula(self):
        """4.2 递推公式法"""
        title = Text(
            "② 递推公式法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)
        
        # 公式
        formula = VGroup(
            MathTex(r"a_1 = 2", font_size=32, color=self.COLOR_FORMULA),
            MathTex(r"a_n = a_{n-1} + 2", font_size=32, color=self.COLOR_FORMULA)
        ).arrange(DOWN, buff=0.3).move_to(UP * 4.8)
        
        self.play(Write(formula[0]), run_time=0.5)
        self.play(Write(formula[1]), run_time=0.6)
        
        # 递推动画
        numbers = VGroup(*[
            MathTex(str(val), font_size=32, color=WHITE)
            for val in [2, 4, 6, 8, 10]
        ]).arrange(RIGHT, buff=0.8).move_to(DOWN * 4.5)
        
        arrows = VGroup(*[
            Arrow(
                numbers[i].get_right(),
                numbers[i+1].get_left(),
                color=self.COLOR_HIGHLIGHT,
                buff=0.1,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.2
            )
            for i in range(4)
        ])
        
        plus_two = VGroup(*[
            MathTex("+2", font_size=20, color=self.COLOR_SECONDARY)
            .next_to(arrow, UP, buff=0.05)
            for arrow in arrows
        ])
        
        self.play(FadeIn(numbers[0]), run_time=0.3)
        
        for i in range(4):
            self.play(
                Create(arrows[i]),
                FadeIn(plus_two[i]),
                run_time=0.25
            )
            self.play(FadeIn(numbers[i+1], scale=0.8), run_time=0.25)
        
        # 特点
        feature = Text(
            "✓ 根据前项求后项",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(feature), run_time=0.4)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(numbers),
            FadeOut(arrows),
            FadeOut(plus_two),
            FadeOut(feature),
            run_time=0.4
        )
    
    def _show_table_method(self):
        """4.3 列表法"""
        title = Text(
            "③ 列表法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)
        
        # 创建表格
        # 表头
        n_header = Text("n", font="Arial", font_size=24, color=self.COLOR_AUXILIARY)
        an_header = MathTex("a_n", font_size=24, color=self.COLOR_AUXILIARY)
        
        # 数值
        n_values = VGroup(*[
            Text(str(i), font="Arial", font_size=22, color=WHITE)
            for i in range(1, 7)
        ])
        
        an_values = VGroup(*[
            Text(str(2*i), font="Arial", font_size=22, color=WHITE)
            for i in range(1, 7)
        ])
        
        # 省略号
        n_dots = Text("...", font="Arial", font_size=22, color=self.COLOR_AUXILIARY)
        an_dots = Text("...", font="Arial", font_size=22, color=self.COLOR_AUXILIARY)
        
        # 排列表格
        n_row = VGroup(n_header, *n_values, n_dots).arrange(RIGHT, buff=0.5)
        an_row = VGroup(an_header, *an_values, an_dots).arrange(RIGHT, buff=0.5)
        
        # 对齐
        for i in range(len(n_row)):
            an_row[i].align_to(n_row[i], LEFT)
        
        table = VGroup(n_row, an_row).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        
        # 分隔线
        line = Line(
            n_row.get_left() + LEFT * 0.2,
            n_row.get_right() + RIGHT * 0.2,
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        ).next_to(n_row, DOWN, buff=0.25)
        
        self.play(FadeIn(n_row), run_time=0.6)
        self.play(Create(line), run_time=0.3)
        self.play(FadeIn(an_row), run_time=0.6)
        
        # 特点
        feature = Text(
            "✓ 直观明了",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(feature), run_time=0.4)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(table),
            FadeOut(line),
            FadeOut(feature),
            run_time=0.4
        )
    
    def _show_graph_method(self):
        """4.4 图像法"""
        title = Text(
            "④ 图像法",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)
        
        # 坐标系和点已经存在，高亮它们
        self.play(
            self.sequence_dots.animate.set_color(self.COLOR_HIGHLIGHT).scale(1.3),
            run_time=0.6
        )
        
        # 用虚线连接各点（强调离散性）
        connecting_lines = VGroup(*[
            DashedLine(
                self.sequence_dots[i].get_center(),
                self.sequence_dots[i+1].get_center(),
                color=self.COLOR_AUXILIARY,
                dash_length=0.08,
                stroke_width=2
            )
            for i in range(len(self.sequence_dots) - 1)
        ])
        
        self.play(
            LaggedStart(*[
                Create(line) for line in connecting_lines
            ], lag_ratio=0.15),
            run_time=1.5
        )
        
        # 特点
        feature = Text(
            "✓ 看出变化趋势",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(feature), run_time=0.4)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(connecting_lines),
            FadeOut(feature),
            self.sequence_dots.animate.set_color(self.COLOR_SEQUENCE).scale(1/1.3),
            run_time=0.5
        )
    
    # ========== Scene 5: 数列的分类 (45-58秒) ==========
    def scene_5_classifications(self):
        """场景5: 展示数列的不同类型"""
        
        # 标题
        title = Text(
            "数列的分类",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 5.1 递增数列
        self._show_increasing_sequence(title)
        
        # 5.2 递减数列
        self._show_decreasing_sequence(title)
        
        # 5.3 常数列
        self._show_constant_sequence(title)
        
        # 5.4 周期数列
        self._show_periodic_sequence(title)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(self.axes),
            FadeOut(self.sequence_dots),
            run_time=0.5
        )
    
    def _show_increasing_sequence(self, title):
        """递增数列"""
        label = Text(
            "递增数列",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).next_to(title, DOWN, buff=0.4)
        
        # 2, 4, 6, 8, 10, 12, 14, 16 (已经是递增)
        increasing_dots = VGroup(*[
            Dot(
                self.axes.c2p(n, 2*n),
                color=self.COLOR_SEQUENCE,
                radius=0.08
            )
            for n in self.sequence_indices
        ])
        
        self.play(FadeIn(label), run_time=0.4)
        self.play(Transform(self.sequence_dots, increasing_dots), run_time=0.8)
        self.wait(0.6)
        self.play(FadeOut(label), run_time=0.3)
    
    def _show_decreasing_sequence(self, title):
        """递减数列"""
        label = Text(
            "递减数列",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).next_to(title, DOWN, buff=0.4)
        
        # 16, 14, 12, 10, 8, 6, 4, 2
        decreasing_dots = VGroup(*[
            Dot(
                self.axes.c2p(n, 18 - 2*n),
                color=self.COLOR_SEQUENCE,
                radius=0.08
            )
            for n in self.sequence_indices
        ])
        
        self.play(FadeIn(label), run_time=0.4)
        self.play(Transform(self.sequence_dots, decreasing_dots), run_time=0.8)
        self.wait(0.6)
        self.play(FadeOut(label), run_time=0.3)
    
    def _show_constant_sequence(self, title):
        """常数列"""
        label = Text(
            "常数列",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).next_to(title, DOWN, buff=0.4)
        
        # 8, 8, 8, 8, 8, 8, 8, 8
        constant_dots = VGroup(*[
            Dot(
                self.axes.c2p(n, 8),
                color=self.COLOR_SEQUENCE,
                radius=0.08
            )
            for n in self.sequence_indices
        ])
        
        self.play(FadeIn(label), run_time=0.4)
        self.play(Transform(self.sequence_dots, constant_dots), run_time=0.8)
        self.wait(0.6)
        self.play(FadeOut(label), run_time=0.3)
    
    def _show_periodic_sequence(self, title):
        """周期数列"""
        label = Text(
            "周期数列",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_SECONDARY
        ).next_to(title, DOWN, buff=0.4)
        
        # 周期为3: 4, 8, 12, 4, 8, 12, 4, 8
        periodic_values = [4, 8, 12, 4, 8, 12, 4, 8]
        periodic_dots = VGroup(*[
            Dot(
                self.axes.c2p(n, periodic_values[i]),
                color=self.COLOR_SEQUENCE,
                radius=0.08
            )
            for i, n in enumerate(self.sequence_indices)
        ])
        
        self.play(FadeIn(label), run_time=0.4)
        self.play(Transform(self.sequence_dots, periodic_dots), run_time=0.8)
        self.wait(0.8)
        self.play(FadeOut(label), run_time=0.3)
    
    # ========== Scene 6: 前n项和 (58-70秒) ==========
    def scene_6_sum(self):
        """场景6: 讲解前n项和的概念"""
        
        # 标题
        title = Text(
            "前n项和",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # Sₙ 定义
        sum_formula = MathTex(
            r"S_n = a_1 + a_2 + \cdots + a_n",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(UP * 4.8)
        
        self.play(Write(sum_formula), run_time=0.8)
        self.wait(0.8)
        
        # 示例：计算前5项和
        example_label = Text(
            "示例: 计算前5项和",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 3.5)
        
        # 数列
        sequence = MathTex(
            r"2, 4, 6, 8, 10",
            font_size=28,
            color=WHITE
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(example_label), run_time=0.4)
        self.play(Write(sequence), run_time=0.6)
        
        # 求和动画 - 数字飞入
        sum_equation = MathTex(
            r"S_5 = 2 + 4 + 6 + 8 + 10",
            font_size=28,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 1.0)
        
        self.play(TransformFromCopy(sequence, sum_equation), run_time=1.0)
        
        # 结果
        result = MathTex(
            r"= 30",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).next_to(sum_equation, RIGHT, buff=0.3)
        
        self.play(FadeIn(result, shift=LEFT * 0.3), run_time=0.6)
        self.wait(0.8)
        
        # 递推关系
        recursive_label = Text(
            "aₙ 与 Sₙ 的关系:",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=self.COLOR_AUXILIARY
        ).move_to(DOWN * 1.0)
        
        recursive_formula = MathTex(
            r"a_n = S_n - S_{n-1} \quad (n \geq 2)",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 2.0)
        
        special_case = MathTex(
            r"a_1 = S_1",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 3.2)
        
        self.play(FadeIn(recursive_label), run_time=0.4)
        self.play(Write(recursive_formula), run_time=0.8)
        self.wait(0.6)
        self.play(Write(special_case), run_time=0.6)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(sum_formula),
            FadeOut(example_label),
            FadeOut(sequence),
            FadeOut(sum_equation),
            FadeOut(result),
            FadeOut(recursive_label),
            FadeOut(recursive_formula),
            FadeOut(special_case),
            run_time=0.6
        )
    
    # ========== Scene 7: 总结 & 关注 (70-85秒) ==========
    def scene_7_summary(self):
        """场景7: 总结要点，引导关注"""
        
        # 总结标题
        summary_title = Text(
            "数列核心要点",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 创建知识点卡片
        cards_data = [
            ("定义", "有序排列的数", self.COLOR_PRIMARY),
            ("本质", "离散函数 n→aₙ", self.COLOR_SECONDARY),
            ("表示", "通项/递推/列表/图像", self.COLOR_FORMULA),
            ("分类", "递增/递减/常/周期", self.COLOR_SEQUENCE),
            ("求和", "Sₙ, aₙ=Sₙ-Sₙ₋₁", self.COLOR_HIGHLIGHT)
        ]
        
        cards = VGroup()
        for i, (key, value, color) in enumerate(cards_data):
            card = self._create_summary_card(key, value, color)
            card.move_to(UP * (3.5 - i * 1.0))
            cards.add(card)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            card.shift(LEFT * 8)  # 初始在左侧外
        
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 8), run_time=0.4)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        self.wait(0.8)
        
        # 清理卡片，准备结尾
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            run_time=0.5
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_AUXILIARY
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰 - 数字旋转
        numbers = VGroup(*[
            Text(str(i), font="Arial", font_size=40, color=self.COLOR_SECONDARY, weight=BOLD)
            for i in [1, 2, 3, 5, 8]
        ])
        
        # 围绕关注文字排列
        radius = 2.5
        for i, num in enumerate(numbers):
            angle = i * 2 * PI / len(numbers)
            num.move_to(follow_text.get_center() + radius * np.array([np.cos(angle), np.sin(angle), 0]))
        
        self.play(
            LaggedStart(*[
                FadeIn(num, scale=0.5) for num in numbers
            ], lag_ratio=0.15),
            run_time=0.8
        )
        
        self.play(Rotate(numbers, angle=PI/3, run_time=1.5))
        self.wait(0.8)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(numbers),
            run_time=1.0
        )
    
    def _create_summary_card(self, key, value, color):
        """创建总结卡片"""
        # 图标圆点
        icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 关键词
        key_text = Text(
            key,
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE,
            weight=BOLD
        )
        
        # 内容
        value_text = Text(
            value,
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_AUXILIARY
        )
        
        # 组合
        card = VGroup(icon, key_text, value_text).arrange(RIGHT, buff=0.25)
        
        return card


# ========== 运行命令 ==========
# manim -pql sequence_concept.py SequenceConcept  # 快速预览
# manim -qh sequence_concept.py SequenceConcept   # 高质量 (1080p)
# manim -qk sequence_concept.py SequenceConcept   # 4K质量