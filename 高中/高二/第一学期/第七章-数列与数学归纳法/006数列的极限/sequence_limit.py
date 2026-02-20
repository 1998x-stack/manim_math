"""
数列的极限教学动画 - Sequence Limit Teaching Animation
使用 Manim 0.19.2 创建的高二数学教学视频

内容: 数列极限的定义、收敛与发散、重要极限
目标观众: 高二学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ==================== 全局配置 ====================

# TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ==================== 主场景类 ====================

class SequenceLimit(Scene):
    """
    数列极限教学动画主场景
    
    场景顺序:
    1. 开场钩子 (5-6秒)
    2. 极限定义 (15-18秒)
    3. 收敛与发散 (12-15秒)
    4. 重要极限1 - lim(1/n)=0 (15-18秒)
    5. 重要极限2 - lim(1+1/n)^n=e (20-25秒)
    6. 极限运算法则 (12-15秒)
    7. 总结与关注 (10-12秒)
    
    总时长: 约90-110秒
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_LIMIT = "#e74c3c"         # 红色 - 极限值
        self.COLOR_SEQUENCE = "#3498db"      # 蓝色 - 数列点
        self.COLOR_CONVERGE = "#2ecc71"      # 绿色 - 收敛
        self.COLOR_DIVERGE = "#e67e22"       # 橙色 - 发散
        self.COLOR_EPSILON = "#9b59b6"       # 紫色 - ε邻域
        self.COLOR_E = "#f39c12"             # 金色 - 自然常数e
        
        # 字体大小
        self.FONT_SIZES = {
            "title": 36,
            "subtitle": 28,
            "body": 22,
            "label": 20,
            "formula": 26,
            "small": 18,
        }
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_convergence_vs_divergence()
        self.scene_4_limit_1_n()
        self.scene_5_limit_e()
        self.scene_6_operations()
        self.scene_7_summary()
    
    # ==================== Scene 1: 开场钩子 ====================
    
    def scene_1_opening(self):
        """开场钩子 - 引出极限概念"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子标题
        hook_title = Text(
            "无限接近的奥秘",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_title), run_time=0.7)
        
        # 数字序列
        number_seq = VGroup(
            MathTex("0.9", font_size=self.FONT_SIZES["subtitle"]),
            MathTex("0.99", font_size=self.FONT_SIZES["subtitle"]),
            MathTex("0.999", font_size=self.FONT_SIZES["subtitle"]),
            MathTex("0.9999", font_size=self.FONT_SIZES["subtitle"]),
            MathTex(r"\cdots", font_size=self.FONT_SIZES["subtitle"]),
        ).arrange(RIGHT, buff=0.4).move_to(UP * 3.5)
        
        self.play(Write(number_seq), run_time=1.5)
        
        # 问号
        question = Text(
            "接近什么？",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_LIMIT
        ).move_to(UP * 2)
        
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        
        # 箭头和目标数字
        arrow = Arrow(
            number_seq.get_bottom(),
            UP * 0.5,
            color=self.COLOR_LIMIT,
            stroke_width=6
        )
        
        target_number = MathTex(
            "1",
            font_size=self.FONT_SIZES["title"] + 10,
            color=self.COLOR_LIMIT
        ).move_to(ORIGIN)
        
        self.play(GrowArrow(arrow), run_time=0.6)
        self.play(
            FadeIn(target_number, scale=1.5),
            Flash(target_number, color=self.COLOR_LIMIT, flash_radius=0.8),
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_title),
            FadeOut(number_seq),
            FadeOut(question),
            FadeOut(arrow),
            FadeOut(target_number),
            run_time=0.5
        )
    
    # ==================== Scene 2: 极限定义 ====================
    
    def scene_2_definition(self):
        """极限定义和可视化"""
        # 标题
        title = Text(
            "数列的极限",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 定义文字
        definition = Text(
            "当n无限增大时，aₙ无限接近常数A",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=WHITE
        ).move_to(UP * 5)
        
        self.play(FadeIn(definition, shift=DOWN * 0.2), run_time=0.9)
        
        # 极限公式
        limit_formula = MathTex(
            r"\lim_{n \to \infty} a_n = A",
            font_size=self.FONT_SIZES["formula"] + 2,
            color=self.COLOR_LIMIT
        ).move_to(UP * 3.8)
        
        self.play(Write(limit_formula), run_time=1.0)
        
        self.wait(0.5)
        
        # 创建坐标系（示例：aₙ = 1/n）
        axes = Axes(
            x_range=[0, 12, 2],
            y_range=[0, 1.3, 0.2],
            x_length=5.5,
            y_length=4.5,
            axis_config={
                "include_numbers": True,
                "font_size": 16,
            },
            tips=False
        ).move_to(DOWN * 0.5)
        
        # 轴标签
        x_label = MathTex("n", font_size=self.FONT_SIZES["body"]).next_to(axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex("a_n", font_size=self.FONT_SIZES["body"]).next_to(axes.y_axis, UP, buff=0.2)
        
        self.play(Create(axes), run_time=1.0)
        self.play(Write(x_label), Write(y_label), run_time=0.5)
        
        # 极限线 y=0
        limit_line = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(12, 0),
            color=self.COLOR_LIMIT,
            stroke_width=3,
            dash_length=0.1
        )
        
        limit_label = MathTex(
            "A = 0",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_LIMIT
        ).next_to(axes.c2p(11, 0), UR, buff=0.15)
        
        self.play(Create(limit_line), run_time=0.7)
        self.play(FadeIn(limit_label), run_time=0.4)
        
        # 数列点 aₙ = 1/n
        n_values = range(1, 11)
        dots = VGroup()
        
        for n in n_values:
            an = 1/n
            dot = Dot(
                axes.c2p(n, an),
                radius=0.06,
                color=self.COLOR_SEQUENCE,
                fill_opacity=1
            )
            dots.add(dot)
        
        # 点依次出现
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots], lag_ratio=0.15),
            run_time=2.0
        )
        
        self.wait(0.8)
        
        # ε邻域
        epsilon = 0.25
        epsilon_rect = Rectangle(
            width=axes.x_axis.get_length(),
            height=2 * epsilon,  # Height is simply 2*epsilon
            color=self.COLOR_EPSILON,
            fill_opacity=0.2,
            stroke_width=0
        ).move_to(axes.c2p(6, epsilon))
        
        epsilon_note = Text(
            "ε邻域：最终所有点都在此范围内",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_EPSILON
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(epsilon_rect), run_time=0.7)
        self.play(FadeIn(epsilon_note, shift=UP * 0.2), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(definition),
            FadeOut(epsilon_rect),
            FadeOut(epsilon_note),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(limit_line),
            FadeOut(limit_label),
            FadeOut(dots),
            title.animate.scale(0.5).move_to(UP * 7 + LEFT * 2.5),
            limit_formula.animate.scale(0.6).move_to(UP * 6.5),
            run_time=0.6
        )
        
        # 保留
        self.limit_formula_ref = limit_formula
        self.title_ref = title
    
    # ==================== Scene 3: 收敛与发散 ====================
    
    def scene_3_convergence_vs_divergence(self):
        """收敛与发散对比"""
        # 标题
        title = Text(
            "收敛 vs 发散",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 左侧：收敛数列
        axes_left = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 2.5, 0.5],
            x_length=3.2,
            y_length=3.5,
            axis_config={"font_size": 14},
            tips=False
        ).move_to(LEFT * 2.2 + UP * 2)
        
        label_left = Text(
            "收敛",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_CONVERGE,
            weight=BOLD
        ).next_to(axes_left, UP, buff=0.3)
        
        self.play(Create(axes_left), FadeIn(label_left), run_time=0.8)
        
        # 右侧：发散数列
        axes_right = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 11, 2],
            x_length=3.2,
            y_length=3.5,
            axis_config={"font_size": 14},
            tips=False
        ).move_to(RIGHT * 2.2 + UP * 2)
        
        label_right = Text(
            "发散",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_DIVERGE,
            weight=BOLD
        ).next_to(axes_right, UP, buff=0.3)
        
        self.play(Create(axes_right), FadeIn(label_right), run_time=0.8)
        
        # 左侧数列点：aₙ = 1 + 1/n → 1
        dots_left = VGroup()
        for n in range(1, 10):
            an = 1 + 1/n
            dot = Dot(
                axes_left.c2p(n, an),
                radius=0.05,
                color=self.COLOR_CONVERGE,
                fill_opacity=1
            )
            dots_left.add(dot)
        
        # 极限线
        limit_line_left = DashedLine(
            axes_left.c2p(0, 1),
            axes_left.c2p(10, 1),
            color=self.COLOR_CONVERGE,
            stroke_width=2,
            dash_length=0.08
        )
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots_left], lag_ratio=0.12),
            run_time=1.5
        )
        self.play(Create(limit_line_left), run_time=0.6)
        
        # 收敛说明
        converge_check = MathTex(
            r"\checkmark",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_CONVERGE
        ).next_to(label_left, RIGHT, buff=0.2)
        
        self.play(FadeIn(converge_check, scale=1.3), run_time=0.5)
        
        # 右侧数列点：aₙ = n → ∞
        dots_right = VGroup()
        for n in range(1, 10):
            an = n
            dot = Dot(
                axes_right.c2p(n, an),
                radius=0.05,
                color=self.COLOR_DIVERGE,
                fill_opacity=1
            )
            dots_right.add(dot)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots_right], lag_ratio=0.12),
            run_time=1.5
        )
        
        # 向上箭头
        arrow_up = Arrow(
            axes_right.c2p(8, 8),
            axes_right.c2p(8, 10.5),
            color=self.COLOR_DIVERGE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(GrowArrow(arrow_up), run_time=0.6)
        
        # 发散标记
        diverge_cross = MathTex(
            r"\times",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_DIVERGE
        ).next_to(label_right, RIGHT, buff=0.2)
        
        self.play(FadeIn(diverge_cross, scale=1.3), run_time=0.5)
        
        # 对比说明
        comparison = VGroup(
            Text("收敛：极限存在", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["body"] - 2, color=self.COLOR_CONVERGE),
            Text("发散：极限不存在", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["body"] - 2, color=self.COLOR_DIVERGE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(DOWN * 2)
        
        self.play(FadeIn(comparison, shift=UP * 0.2), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axes_left),
            FadeOut(axes_right),
            FadeOut(label_left),
            FadeOut(label_right),
            FadeOut(dots_left),
            FadeOut(dots_right),
            FadeOut(limit_line_left),
            FadeOut(arrow_up),
            FadeOut(converge_check),
            FadeOut(diverge_cross),
            FadeOut(comparison),
            run_time=0.6
        )
    
    # ==================== Scene 4: 重要极限1 ====================
    
    def scene_4_limit_1_n(self):
        """重要极限：lim(1/n)=0"""
        # 标题
        title = Text(
            "重要极限①",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_LIMIT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 公式
        formula = MathTex(
            r"\lim_{n \to \infty} \frac{1}{n} = 0",
            font_size=self.FONT_SIZES["formula"] + 2,
            color=self.COLOR_LIMIT
        ).move_to(UP * 5)
        
        self.play(Write(formula), run_time=1.0)
        
        # 强调
        self.play(
            formula.animate.scale(1.15),
            Flash(formula, color=self.COLOR_LIMIT),
            run_time=0.6
        )
        
        self.wait(0.5)
        
        # 坐标系
        axes = Axes(
            x_range=[0, 20, 5],
            y_range=[0, 1.2, 0.2],
            x_length=6,
            y_length=4.5,
            axis_config={
                "include_numbers": True,
                "font_size": 16,
            },
            tips=False
        ).move_to(DOWN * 0.5)
        
        x_label = MathTex("n", font_size=self.FONT_SIZES["body"]).next_to(axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex(r"\frac{1}{n}", font_size=self.FONT_SIZES["body"]).next_to(axes.y_axis, UP, buff=0.2)
        
        self.play(Create(axes), run_time=0.8)
        self.play(Write(x_label), Write(y_label), run_time=0.4)
        
        # 极限线 y=0
        limit_line = DashedLine(
            axes.c2p(0, 0),
            axes.c2p(20, 0),
            color=self.COLOR_LIMIT,
            stroke_width=3,
            dash_length=0.1
        )
        
        self.play(Create(limit_line), run_time=0.6)
        
        # 数列点（前10个）
        dots_1 = VGroup()
        for n in range(1, 11):
            an = 1/n
            dot = Dot(
                axes.c2p(n, an),
                radius=0.06,
                color=self.COLOR_SEQUENCE,
                fill_opacity=1
            )
            dots_1.add(dot)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots_1], lag_ratio=0.15),
            run_time=2.0
        )
        
        # 数值表格
        table_data = [
            ["n", "1", "5", "10", "100"],
            ["1/n", "1.0", "0.2", "0.1", "0.01"]
        ]
        
        table = MobjectTable(
            [[Text(cell, font="Noto Sans CJK SC", font_size=14) for cell in row] for row in table_data],
            include_outer_lines=True,
            line_config={"stroke_width": 1}
        ).scale(0.6).move_to(DOWN * 5)
        
        self.play(Create(table), run_time=1.2)
        
        self.wait(1.0)
        
        # 后续点（加速）
        dots_2 = VGroup()
        for n in range(11, 21):
            an = 1/n
            dot = Dot(
                axes.c2p(n, an),
                radius=0.05,
                color=self.COLOR_SEQUENCE,
                fill_opacity=0.8
            )
            dots_2.add(dot)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots_2], lag_ratio=0.08),
            run_time=1.2
        )
        
        # 箭头指向0
        arrow_to_zero = Arrow(
            axes.c2p(15, 0.3),
            axes.c2p(18, 0.05),
            color=self.COLOR_LIMIT,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(GrowArrow(arrow_to_zero), run_time=0.6)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(table),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(limit_line),
            FadeOut(dots_1),
            FadeOut(dots_2),
            FadeOut(arrow_to_zero),
            title.animate.scale(0.5).move_to(DOWN * 6.5 + LEFT * 2),
            formula.animate.scale(1/1.15).scale(0.55).move_to(DOWN * 6 + LEFT * 2),
            run_time=0.6
        )
        
        # 保留
        self.formula_1n_ref = formula
        self.title_1n_ref = title
    
    # ==================== Scene 5: 重要极限2 ====================
    
    def scene_5_limit_e(self):
        """重要极限：lim(1+1/n)^n=e"""
        # 标题
        title = Text(
            "重要极限②",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=self.COLOR_E,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 公式
        formula = MathTex(
            r"\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e",
            font_size=self.FONT_SIZES["formula"],
            color=self.COLOR_E
        ).move_to(UP * 5)
        
        self.play(Write(formula), run_time=1.2)
        
        # e的值
        e_value = MathTex(
            r"e \approx 2.71828\cdots",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).next_to(formula, DOWN, buff=0.3)
        
        self.play(FadeIn(e_value, shift=DOWN * 0.2), run_time=0.6)
        
        # 强调
        self.play(
            formula.animate.scale(1.1),
            Flash(formula, color=self.COLOR_E),
            run_time=0.6
        )
        
        self.wait(0.5)
        
        # 坐标系
        axes = Axes(
            x_range=[0, 50, 10],
            y_range=[0, 3.5, 0.5],
            x_length=6,
            y_length=4.5,
            axis_config={
                "include_numbers": True,
                "font_size": 16,
            },
            tips=False
        ).move_to(DOWN * 0.8)
        
        x_label = MathTex("n", font_size=self.FONT_SIZES["body"]).next_to(axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex(r"\left(1+\frac{1}{n}\right)^n", font_size=18).next_to(axes.y_axis, UP, buff=0.2)
        
        self.play(Create(axes), run_time=0.9)
        self.play(Write(x_label), Write(y_label), run_time=0.5)
        
        # e参考线
        e_line = DashedLine(
            axes.c2p(0, np.e),
            axes.c2p(50, np.e),
            color=self.COLOR_E,
            stroke_width=3,
            dash_length=0.1
        )
        
        e_label = MathTex(
            "e",
            font_size=self.FONT_SIZES["body"],
            color=self.COLOR_E
        ).next_to(axes.c2p(48, np.e), UR, buff=0.1)
        
        self.play(Create(e_line), FadeIn(e_label), run_time=0.7)
        
        # 数列点（前10个）
        dots_1 = VGroup()
        for n in range(1, 11):
            an = (1 + 1/n)**n
            dot = Dot(
                axes.c2p(n, an),
                radius=0.06,
                color=self.COLOR_SEQUENCE,
                fill_opacity=1
            )
            dots_1.add(dot)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots_1], lag_ratio=0.15),
            run_time=2.5
        )
        
        # 数值表格
        table_data = [
            ["n", "1", "5", "10", "50"],
            [r"(1+\frac{1}{n})^n", "2.0", "2.49", "2.59", "2.69"]
        ]
        
        table = MobjectTable(
            [[MathTex(cell, font_size=14) if "/" in cell or "^" in cell else Text(cell, font="Noto Sans CJK SC", font_size=14) for cell in row] for row in table_data],
            include_outer_lines=True,
            line_config={"stroke_width": 1}
        ).scale(0.55).move_to(DOWN * 5.5)
        
        self.play(Create(table), run_time=1.5)
        
        self.wait(1.0)
        
        # 后续点（加速，接近e）
        dots_2 = VGroup()
        for n in [15, 20, 30, 40, 50]:
            an = (1 + 1/n)**n
            dot = Dot(
                axes.c2p(n, an),
                radius=0.05,
                color=self.COLOR_SEQUENCE,
                fill_opacity=0.8
            )
            dots_2.add(dot)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots_2], lag_ratio=0.2),
            run_time=1.5
        )
        
        # 闪烁e线
        self.play(
            Indicate(e_line, scale_factor=1.05, color=self.COLOR_E),
            run_time=0.8
        )
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(e_value),
            FadeOut(table),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(e_line),
            FadeOut(e_label),
            FadeOut(dots_1),
            FadeOut(dots_2),
            title.animate.scale(0.5).move_to(DOWN * 6.5 + RIGHT * 2),
            formula.animate.scale(1/1.1).scale(0.5).move_to(DOWN * 6 + RIGHT * 2),
            run_time=0.6
        )
        
        # 保留
        self.formula_e_ref = formula
        self.title_e_ref = title
    
    # ==================== Scene 6: 极限运算法则 ====================
    
    def scene_6_operations(self):
        """极限运算法则"""
        # 标题
        title = Text(
            "极限运算法则",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 法则
        rules = VGroup(
            MathTex(r"\lim(a_n \pm b_n) = \lim a_n \pm \lim b_n", font_size=self.FONT_SIZES["body"] - 2),
            MathTex(r"\lim(a_n \cdot b_n) = \lim a_n \cdot \lim b_n", font_size=self.FONT_SIZES["body"] - 2),
            MathTex(r"\lim\frac{a_n}{b_n} = \frac{\lim a_n}{\lim b_n}", font_size=self.FONT_SIZES["body"] - 2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(UP * 3.5)
        
        # 依次显示
        for rule in rules:
            self.play(FadeIn(rule, shift=RIGHT * 0.3), run_time=0.7)
            self.wait(0.3)
        
        # 条件标注
        condition = Text(
            "(lim bₙ ≠ 0)",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["small"],
            color=self.COLOR_LIMIT
        ).next_to(rules[2], RIGHT, buff=0.3)
        
        self.play(FadeIn(condition), run_time=0.4)
        
        # 示例
        example_title = Text(
            "示例：",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["body"],
            color=GRAY_A
        ).move_to(UP * 0.8 + LEFT * 3.5)
        
        example_problem = MathTex(
            r"\lim_{n \to \infty} \frac{2n + 1}{n}",
            font_size=self.FONT_SIZES["body"]
        ).next_to(example_title, RIGHT, buff=0.3)
        
        self.play(Write(example_title), Write(example_problem), run_time=0.8)
        
        # 步骤
        steps = VGroup(
            MathTex(r"= \lim_{n \to \infty} \left(2 + \frac{1}{n}\right)", font_size=self.FONT_SIZES["body"] - 2),
            MathTex(r"= \lim_{n \to \infty} 2 + \lim_{n \to \infty} \frac{1}{n}", font_size=self.FONT_SIZES["body"] - 2),
            MathTex(r"= 2 + 0 = 2", font_size=self.FONT_SIZES["body"] - 2, color=self.COLOR_CONVERGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(DOWN * 1.5)
        
        for step in steps:
            self.play(Write(step), run_time=0.9)
            self.wait(0.5)
        
        # 框选答案
        answer_box = SurroundingRectangle(
            steps[2],
            color=self.COLOR_CONVERGE,
            buff=0.15,
            corner_radius=0.1
        )
        
        self.play(Create(answer_box), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rules),
            FadeOut(condition),
            FadeOut(example_title),
            FadeOut(example_problem),
            FadeOut(steps),
            FadeOut(answer_box),
            run_time=0.6
        )
    
    # ==================== Scene 7: 总结与关注 ====================
    
    def scene_7_summary(self):
        """总结与关注"""
        # 标题
        title = Text(
            "数列极限要点",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 要点
        points = VGroup(
            Text("• 极限：n→∞时aₙ接近常数A", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["body"] - 2, color=WHITE),
            Text("• 收敛/发散：极限存在/不存在", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["body"] - 2, color=WHITE),
            Text("• 重要极限：1/n→0, (1+1/n)ⁿ→e", font="Noto Sans CJK SC", font_size=self.FONT_SIZES["body"] - 2, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).move_to(UP * 3.5)
        
        for point in points:
            self.play(FadeIn(point, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        
        # 公式卡片
        card_1 = VGroup(
            MathTex(r"\lim_{n \to \infty} \frac{1}{n} = 0", font_size=20, color=self.COLOR_LIMIT),
            Rectangle(height=0.6, width=3.5, color=self.COLOR_LIMIT, stroke_width=2)
        )
        card_1[1].move_to(card_1[0])
        card_1.move_to(UP * 1)
        
        card_2 = VGroup(
            MathTex(r"\lim_{n \to \infty} \left(1+\frac{1}{n}\right)^n = e", font_size=18, color=self.COLOR_E),
            Rectangle(height=0.6, width=4, color=self.COLOR_E, stroke_width=2)
        )
        card_2[1].move_to(card_2[0])
        card_2.next_to(card_1, DOWN, buff=0.4)
        
        self.play(FadeIn(card_1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(card_2, shift=UP * 0.2), run_time=0.6)
        
        self.wait(0.8)
        
        # 清理参考
        refs_to_clear = [
            self.limit_formula_ref if hasattr(self, 'limit_formula_ref') else None,
            self.title_ref if hasattr(self, 'title_ref') else None,
            self.formula_1n_ref if hasattr(self, 'formula_1n_ref') else None,
            self.title_1n_ref if hasattr(self, 'title_1n_ref') else None,
            self.formula_e_ref if hasattr(self, 'formula_e_ref') else None,
            self.title_e_ref if hasattr(self, 'title_e_ref') else None,
        ]
        refs_to_clear = [r for r in refs_to_clear if r is not None]
        
        self.play(
            FadeOut(title),
            FadeOut(points),
            FadeOut(card_1),
            FadeOut(card_2),
            *[FadeOut(ref) for ref in refs_to_clear],
            run_time=0.5
        )
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["title"],
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 1)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=GRAY_B
        ).next_to(author_large, DOWN, buff=0.3)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，掌握极限技巧！",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SIZES["subtitle"],
            color=self.COLOR_LIMIT,
            weight=BOLD
        ).move_to(DOWN * 2)
        
        self.play(
            FadeIn(follow_text, shift=UP * 0.3, scale=1.1),
            run_time=0.6
        )
        
        # 点赞图标
        like_icon = Star(
            color=self.COLOR_LIMIT,
            fill_opacity=0.8,
            stroke_width=2
        ).scale(0.6).move_to(DOWN * 4)
        
        self.play(
            FadeIn(like_icon, scale=0.5),
            run_time=0.4
        )
        
        self.play(
            Flash(like_icon, color=self.COLOR_LIMIT, flash_radius=0.5),
            like_icon.animate.scale(1.3),
            run_time=0.5
        )
        
        self.play(like_icon.animate.scale(1/1.3), run_time=0.3)
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(like_icon),
            run_time=1.0
        )


# ==================== 渲染入口 ====================

if __name__ == "__main__":
    # 使用以下命令渲染:
    # 快速预览: manim -pql sequence_limit.py SequenceLimit
    # 高质量: manim -qh sequence_limit.py SequenceLimit
    # 4K质量: manim -qk sequence_limit.py SequenceLimit
    pass