"""
二次函数与一元二次方程的关系
Quadratic Function and Equation Relationship Animation

内容: 判别式Δ与抛物线交点个数的关系
目标观众: 九年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ==================== 全局配置 ====================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class QuadraticEquationRelation(Scene):
    """
    二次函数与一元二次方程关系教学动画
    
    场景顺序:
    1. 开场钩子
    2. 建立坐标系
    3. Δ>0 两个交点
    4. Δ=0 一个交点
    5. Δ<0 无交点
    6. 三种情况对比
    7. 判别式公式强化
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 初始化配色方案
        self.setup_colors()
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 验证几何计算
        self.verify_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_setup_axes()
        self.scene_3_delta_positive()
        self.scene_4_delta_zero()
        self.scene_5_delta_negative()
        self.scene_6_comparison()
        self.scene_7_formula_emphasis()
        self.scene_8_outro()
    
    def setup_colors(self):
        """初始化颜色配置"""
        self.COLOR_PARABOLA = "#e74c3c"        # 红色 - 抛物线
        self.COLOR_X_AXIS = "#3498db"          # 蓝色 - x轴
        self.COLOR_INTERSECTION = "#2ecc71"    # 绿色 - 交点
        self.COLOR_DISCRIMINANT = "#f39c12"    # 橙色 - 判别式
        self.COLOR_EQUATION = GOLD             # 金色 - 方程
        self.COLOR_HIGHLIGHT = YELLOW          # 黄色 - 强调
        self.COLOR_AUXILIARY = GRAY_B          # 灰色 - 辅助
    
    def setup_geometry(self):
        """统一初始化所有几何数据"""
        # ========== 情况1: Δ>0, 两个交点 ==========
        # 方程: y = x² - 4x + 3 = (x-1)(x-3)
        self.a1 = 1.0
        self.b1 = -4.0
        self.c1 = 3.0
        self.func_two = lambda x: self.a1 * x**2 + self.b1 * x + self.c1
        self.root1_1 = 1.0  # 第一个根
        self.root1_2 = 3.0  # 第二个根
        self.delta1 = self.b1**2 - 4*self.a1*self.c1  # = 16-12 = 4
        
        # ========== 情况2: Δ=0, 一个交点 ==========
        # 方程: y = x² - 4x + 4 = (x-2)²
        self.a2 = 1.0
        self.b2 = -4.0
        self.c2 = 4.0
        self.func_one = lambda x: (x - 2.0)**2
        self.root2 = 2.0  # 重根
        self.delta2 = self.b2**2 - 4*self.a2*self.c2  # = 16-16 = 0
        
        # ========== 情况3: Δ<0, 无交点 ==========
        # 方程: y = x² - 2x + 3
        self.a3 = 1.0
        self.b3 = -2.0
        self.c3 = 3.0
        self.func_none = lambda x: self.a3 * x**2 + self.b3 * x + self.c3
        self.delta3 = self.b3**2 - 4*self.a3*self.c3  # = 4-12 = -8
        
        # 计算顶点（用于情况3）
        self.h3 = -self.b3 / (2 * self.a3)  # x = 1
        self.k3 = self.func_none(self.h3)    # y = 2
        
        # ========== 坐标系配置 ==========
        self.axes_config = {
            'x_range': [-1, 5, 1],
            'y_range': [-2, 5, 1],
            'x_length': 7,
            'y_length': 10,
            'axis_config': {
                'include_numbers': True,
                'font_size': 18,
                'color': WHITE,
                'numbers_to_exclude': [0]
            }
        }
        
        # 坐标系偏移
        self.axes_offset = DOWN * 1
    
    def verify_geometry(self):
        """验证几何计算正确性"""
        epsilon = 1e-10
        
        # 验证情况1: 两个根
        assert abs(self.func_two(self.root1_1)) < epsilon, f"根1验证失败: f({self.root1_1}) = {self.func_two(self.root1_1)}"
        assert abs(self.func_two(self.root1_2)) < epsilon, f"根2验证失败: f({self.root1_2}) = {self.func_two(self.root1_2)}"
        assert self.delta1 == 4 and self.delta1 > 0, "判别式1错误"
        
        # 验证情况2: 重根
        assert abs(self.func_one(self.root2)) < epsilon, f"重根验证失败: f({self.root2}) = {self.func_one(self.root2)}"
        assert self.delta2 == 0, "判别式2错误"
        
        # 验证情况3: 无实根
        assert self.delta3 == -8 and self.delta3 < 0, "判别式3错误"
        # 验证抛物线在x轴上方
        assert self.k3 > 0, "顶点应在x轴上方"
        # 验证最小值大于0（无交点）
        min_val = self.func_none(self.h3)
        assert min_val > 0, "最小值应大于0"
        
        print("✓ 几何验证通过")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息（顶部，贯穿全片）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "抛物线与x轴的交点\n藏着什么秘密?",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD,
            line_spacing=1.2
        ).move_to(UP * 4.5)
        
        self.play(Write(hook_question), run_time=0.8)
        self.wait(0.5)
        
        # 三条抛物线快速闪现（预览）
        # 创建临时小坐标系
        temp_axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-2, 5, 1],
            x_length=5,
            y_length=6,
            axis_config={'stroke_width': 1, 'include_numbers': False}
        ).move_to(DOWN * 0.5)
        
        # 三条抛物线
        preview_1 = temp_axes.plot(self.func_two, x_range=[0, 4], color=self.COLOR_PARABOLA, stroke_width=3)
        preview_2 = temp_axes.plot(self.func_one, x_range=[0, 4], color=self.COLOR_PARABOLA, stroke_width=3)
        preview_3 = temp_axes.plot(self.func_none, x_range=[0, 4], color=self.COLOR_PARABOLA, stroke_width=3)
        
        # 快速切换展示
        self.play(FadeIn(temp_axes, preview_1), run_time=0.4)
        self.wait(0.3)
        self.play(Transform(preview_1, preview_2), run_time=0.4)
        self.wait(0.3)
        self.play(Transform(preview_1, preview_3), run_time=0.4)
        self.wait(0.3)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(temp_axes),
            FadeOut(preview_1),
            run_time=0.4
        )
    
    def scene_2_setup_axes(self):
        """场景2: 建立坐标系 (5-12秒)"""
        # 创建坐标系
        self.axes = Axes(**self.axes_config).shift(self.axes_offset)
        
        # 原点标签
        origin_label = MathTex("O", font_size=20, color=WHITE).next_to(
            self.axes.c2p(0, 0), DL, buff=0.15
        )
        
        # 标题
        title = Text(
            "二次函数 ↔ 一元二次方程",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_EQUATION
        ).move_to(UP * 6)
        
        # 坐标系动画
        self.play(Create(self.axes), run_time=1.2)
        self.play(FadeIn(origin_label), run_time=0.3)
        self.wait(0.2)
        
        # x轴强调
        x_axis_highlight = self.axes.get_x_axis().copy().set_color(self.COLOR_X_AXIS).set_stroke(width=6)
        self.play(
            Create(x_axis_highlight),
            Flash(x_axis_highlight, color=self.COLOR_X_AXIS, flash_radius=0.5),
            run_time=0.6
        )
        self.play(FadeOut(x_axis_highlight), run_time=0.3)
        
        # 标题出现
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.3)
        
        # 核心概念
        concept = Text(
            "交点横坐标 = 方程的根",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(Write(concept), run_time=0.8)
        self.wait(1.5)
        
        # 清理标题和概念
        self.play(
            FadeOut(title),
            FadeOut(concept),
            run_time=0.4
        )
        
        # 保存引用
        self.origin_label = origin_label
    
    def scene_3_delta_positive(self):
        """场景3: Δ>0 两个交点 (12-30秒)"""
        # 方程显示
        equation_tex = MathTex(
            r"y = x^2 - 4x + 3",
            font_size=28,
            color=self.COLOR_EQUATION
        ).move_to(UP * 5.8)
        
        equation_factored = MathTex(
            r"y = (x-1)(x-3)",
            font_size=28,
            color=self.COLOR_EQUATION
        ).move_to(UP * 5.8)
        
        self.play(Write(equation_tex), run_time=0.8)
        self.wait(0.3)
        
        # 抛物线
        parabola_two = self.axes.plot(
            self.func_two,
            x_range=[-0.5, 4.5],
            color=self.COLOR_PARABOLA,
            stroke_width=4
        )
        
        self.play(Create(parabola_two), run_time=1.5)
        self.wait(0.3)
        
        # 交点1
        intersection1_pos = self.axes.c2p(self.root1_1, 0)
        dot1 = Dot(intersection1_pos, color=self.COLOR_INTERSECTION, radius=0.12)
        label1 = MathTex("x_1=1", font_size=22, color=self.COLOR_INTERSECTION).next_to(dot1, DOWN, buff=0.3)
        
        self.play(
            FadeIn(dot1, scale=0.5),
            Flash(dot1, color=self.COLOR_INTERSECTION, flash_radius=0.3),
            run_time=0.6
        )
        self.play(Write(label1), run_time=0.5)
        self.wait(0.3)
        
        # 交点2
        intersection2_pos = self.axes.c2p(self.root1_2, 0)
        dot2 = Dot(intersection2_pos, color=self.COLOR_INTERSECTION, radius=0.12)
        label2 = MathTex("x_2=3", font_size=22, color=self.COLOR_INTERSECTION).next_to(dot2, DOWN, buff=0.3)
        
        self.play(
            FadeIn(dot2, scale=0.5),
            Flash(dot2, color=self.COLOR_INTERSECTION, flash_radius=0.3),
            run_time=0.6
        )
        self.play(Write(label2), run_time=0.5)
        self.wait(0.5)
        
        # 因式分解形式
        self.play(TransformMatchingTex(equation_tex, equation_factored), run_time=0.8)
        self.wait(0.4)
        
        # 判别式计算
        delta_title = Text(
            "判别式 Δ",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_DISCRIMINANT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(delta_title, shift=UP * 0.2), run_time=0.5)
        
        # 计算步骤
        delta_calc_1 = MathTex(
            r"\Delta = b^2 - 4ac",
            font_size=22,
            color=self.COLOR_DISCRIMINANT
        ).move_to(DOWN * 5.3)
        
        delta_calc_2 = MathTex(
            r"= (-4)^2 - 4(1)(3)",
            font_size=22,
            color=self.COLOR_DISCRIMINANT
        ).move_to(DOWN * 5.9)
        
        delta_calc_3 = MathTex(
            r"= 16 - 12 = 4",
            font_size=22,
            color=self.COLOR_DISCRIMINANT
        ).move_to(DOWN * 6.5)
        
        self.play(Write(delta_calc_1), run_time=0.5)
        self.play(Write(delta_calc_2), run_time=0.5)
        self.play(Write(delta_calc_3), run_time=0.5)
        self.wait(0.3)
        
        # 结论
        conclusion_1 = Text(
            "Δ > 0 → 两个交点",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 7.3)
        
        self.play(
            FadeIn(conclusion_1, scale=1.1),
            Flash(conclusion_1, color=YELLOW, flash_radius=0.5),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 垂直虚线强调横坐标
        vline1 = DashedLine(
            self.axes.c2p(self.root1_1, self.func_two(self.root1_1)),
            intersection1_pos,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        vline2 = DashedLine(
            self.axes.c2p(self.root1_2, self.func_two(self.root1_2)),
            intersection2_pos,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        # 注意：抛物线最低点在y=-1，不在x轴上
        actual_dot1_pos = self.axes.c2p(self.root1_1, self.func_two(self.root1_1))
        actual_dot2_pos = self.axes.c2p(self.root1_2, self.func_two(self.root1_2))
        
        # 从抛物线上的点到x轴的垂线
        vline1_correct = DashedLine(
            intersection1_pos + UP * 0.1,  # 稍微延长一点
            intersection1_pos + DOWN * 0.1,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        vline2_correct = DashedLine(
            intersection2_pos + UP * 0.1,
            intersection2_pos + DOWN * 0.1,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3
        )
        
        self.play(
            Create(vline1_correct),
            Create(vline2_correct),
            run_time=0.6
        )
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(delta_title),
            FadeOut(delta_calc_1),
            FadeOut(delta_calc_2),
            FadeOut(delta_calc_3),
            FadeOut(conclusion_1),
            FadeOut(vline1_correct),
            FadeOut(vline2_correct),
            FadeOut(equation_factored),
            FadeOut(parabola_two),
            FadeOut(dot1),
            FadeOut(dot2),
            FadeOut(label1),
            FadeOut(label2),
            run_time=0.5
        )
    
    def scene_4_delta_zero(self):
        """场景4: Δ=0 一个交点 (30-48秒)"""
        # 方程显示
        equation_tex = MathTex(
            r"y = x^2 - 4x + 4",
            font_size=28,
            color=self.COLOR_EQUATION
        ).move_to(UP * 5.8)
        
        equation_perfect = MathTex(
            r"y = (x-2)^2",
            font_size=28,
            color=self.COLOR_EQUATION
        ).move_to(UP * 5.8)
        
        self.play(Write(equation_tex), run_time=0.8)
        self.wait(0.3)
        
        # 完全平方强调
        self.play(TransformMatchingTex(equation_tex, equation_perfect), run_time=0.8)
        self.wait(0.4)
        
        # 抛物线
        parabola_one = self.axes.plot(
            self.func_one,
            x_range=[0, 4],
            color=self.COLOR_PARABOLA,
            stroke_width=4
        )
        
        self.play(Create(parabola_one), run_time=1.5)
        self.wait(0.3)
        
        # 切点（重根）
        tangent_pos = self.axes.c2p(self.root2, 0)
        dot_tangent = Dot(tangent_pos, color=self.COLOR_INTERSECTION, radius=0.12)
        
        # 双圆圈标记重根
        double_circle = Circle(radius=0.2, color=self.COLOR_INTERSECTION, stroke_width=2).move_to(tangent_pos)
        
        self.play(
            FadeIn(dot_tangent, scale=0.5),
            Flash(dot_tangent, color=self.COLOR_INTERSECTION, flash_radius=0.3),
            run_time=0.6
        )
        self.play(Create(double_circle), run_time=0.4)
        
        # 标签
        label_tangent = MathTex(
            r"x_1 = x_2 = 2",
            font_size=22,
            color=self.COLOR_INTERSECTION
        ).next_to(tangent_pos, DOWN, buff=0.5)
        
        label_double_root = Text(
            "(重根)",
            font="PingFang SC",
            font_size=18,
            color=self.COLOR_INTERSECTION
        ).next_to(label_tangent, DOWN, buff=0.1)
        
        self.play(Write(label_tangent), run_time=0.6)
        self.play(FadeIn(label_double_root), run_time=0.3)
        self.wait(0.4)
        
        # 判别式计算
        delta_title = Text(
            "判别式 Δ",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_DISCRIMINANT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(delta_title, shift=UP * 0.2), run_time=0.5)
        
        delta_calc = MathTex(
            r"\Delta = (-4)^2 - 4(1)(4) = 0",
            font_size=22,
            color=self.COLOR_DISCRIMINANT
        ).move_to(DOWN * 5.3)
        
        self.play(Write(delta_calc), run_time=1.0)
        self.wait(0.3)
        
        # 结论
        conclusion_2 = Text(
            "Δ = 0 → 一个交点",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 6.3)
        
        self.play(
            FadeIn(conclusion_2, scale=1.1),
            Flash(conclusion_2, color=YELLOW, flash_radius=0.5),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 顶点在x轴上标注
        vertex_note = Text(
            "顶点在x轴上",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 7.1)
        
        self.play(FadeIn(vertex_note, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # x轴相切动画
        tangent_line = Line(
            self.axes.c2p(1, 0),
            self.axes.c2p(3, 0),
            color=self.COLOR_X_AXIS,
            stroke_width=6
        )
        self.play(Create(tangent_line), run_time=0.6)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(delta_title),
            FadeOut(delta_calc),
            FadeOut(conclusion_2),
            FadeOut(vertex_note),
            FadeOut(tangent_line),
            FadeOut(equation_perfect),
            FadeOut(parabola_one),
            FadeOut(dot_tangent),
            FadeOut(double_circle),
            FadeOut(label_tangent),
            FadeOut(label_double_root),
            run_time=0.5
        )
    
    def scene_5_delta_negative(self):
        """场景5: Δ<0 无交点 (48-63秒)"""
        # 方程显示
        equation_tex = MathTex(
            r"y = x^2 - 2x + 3",
            font_size=28,
            color=self.COLOR_EQUATION
        ).move_to(UP * 5.8)
        
        self.play(Write(equation_tex), run_time=0.8)
        self.wait(0.3)
        
        # 抛物线
        parabola_none = self.axes.plot(
            self.func_none,
            x_range=[-0.5, 2.5],
            color=self.COLOR_PARABOLA,
            stroke_width=4
        )
        
        self.play(Create(parabola_none), run_time=1.5)
        self.wait(0.3)
        
        # x轴闪烁强调
        x_axis_flash = self.axes.get_x_axis().copy().set_color(self.COLOR_X_AXIS).set_stroke(width=6)
        self.play(
            Flash(x_axis_flash, color=self.COLOR_X_AXIS, flash_radius=0.5),
            run_time=0.6
        )
        
        # 从顶点到x轴的距离线
        vertex_pos = self.axes.c2p(self.h3, self.k3)
        vertex_proj = self.axes.c2p(self.h3, 0)
        
        distance_line = DashedLine(
            vertex_pos,
            vertex_proj,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08
        )
        
        self.play(Create(distance_line), run_time=0.6)
        self.wait(0.3)
        
        # 无交点标记
        no_intersection = Text(
            "✗ 无交点",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).next_to(distance_line, RIGHT, buff=0.3)
        
        self.play(FadeIn(no_intersection), run_time=0.4)
        self.wait(0.4)
        
        # 判别式计算
        delta_title = Text(
            "判别式 Δ",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_DISCRIMINANT,
            weight=BOLD
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(delta_title, shift=UP * 0.2), run_time=0.5)
        
        delta_calc = MathTex(
            r"\Delta = (-2)^2 - 4(1)(3) = -8",
            font_size=22,
            color=self.COLOR_DISCRIMINANT
        ).move_to(DOWN * 5.3)
        
        self.play(Write(delta_calc), run_time=1.0)
        self.wait(0.3)
        
        # 结论
        conclusion_3 = Text(
            "Δ < 0 → 无交点",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 6.3)
        
        self.play(
            FadeIn(conclusion_3, scale=1.1),
            Flash(conclusion_3, color=YELLOW, flash_radius=0.5),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 说明
        no_real_roots = Text(
            "无实数根",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 7.1)
        
        self.play(FadeIn(no_real_roots), run_time=0.5)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(delta_title),
            FadeOut(delta_calc),
            FadeOut(conclusion_3),
            FadeOut(no_real_roots),
            FadeOut(distance_line),
            FadeOut(no_intersection),
            FadeOut(equation_tex),
            FadeOut(parabola_none),
            run_time=0.5
        )
    
    def scene_6_comparison(self):
        """场景6: 三种情况对比 (63-75秒)"""
        # 清空坐标系内容
        self.play(
            FadeOut(self.axes),
            FadeOut(self.origin_label),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "三种情况对比",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.4)
        self.wait(0.3)
        
        # 创建三个小坐标系
        small_axes_config = {
            'x_range': [-1, 5, 2],
            'y_range': [-2, 5, 2],
            'x_length': 2,
            'y_length': 2.5,
            'axis_config': {
                'include_numbers': False,
                'stroke_width': 1.5,
                'color': WHITE
            }
        }
        
        axes_left = Axes(**small_axes_config).move_to(LEFT * 2.5 + UP * 3.5)
        axes_center = Axes(**small_axes_config).move_to(UP * 3.5)
        axes_right = Axes(**small_axes_config).move_to(RIGHT * 2.5 + UP * 3.5)
        
        # 三条抛物线
        para_left = axes_left.plot(self.func_two, x_range=[0, 4], color=self.COLOR_PARABOLA, stroke_width=2.5)
        para_center = axes_center.plot(self.func_one, x_range=[0, 4], color=self.COLOR_PARABOLA, stroke_width=2.5)
        para_right = axes_right.plot(self.func_none, x_range=[0, 2.5], color=self.COLOR_PARABOLA, stroke_width=2.5)
        
        # 交点
        dot_left_1 = Dot(axes_left.c2p(1, 0), color=self.COLOR_INTERSECTION, radius=0.06)
        dot_left_2 = Dot(axes_left.c2p(3, 0), color=self.COLOR_INTERSECTION, radius=0.06)
        dot_center = Dot(axes_center.c2p(2, 0), color=self.COLOR_INTERSECTION, radius=0.06)
        
        # 并排显示
        self.play(
            FadeIn(axes_left, para_left, dot_left_1, dot_left_2),
            FadeIn(axes_center, para_center, dot_center),
            FadeIn(axes_right, para_right),
            run_time=1.0
        )
        self.wait(0.5)
        
        # Δ值标注
        delta_left = MathTex(r"\Delta > 0", font_size=20, color=self.COLOR_DISCRIMINANT).next_to(axes_left, DOWN, buff=0.3)
        delta_center = MathTex(r"\Delta = 0", font_size=20, color=self.COLOR_DISCRIMINANT).next_to(axes_center, DOWN, buff=0.3)
        delta_right = MathTex(r"\Delta < 0", font_size=20, color=self.COLOR_DISCRIMINANT).next_to(axes_right, DOWN, buff=0.3)
        
        self.play(
            Write(delta_left),
            Write(delta_center),
            Write(delta_right),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 对比表格
        table_data = [
            ["两个交点", "一个交点", "无交点"],
            ["两个不等实根", "两个相等实根", "无实根"],
            ["x₁ ≠ x₂", "x₁ = x₂", "-"]
        ]
        
        row_y_positions = [1.2, 0, -1.2]
        
        for row_idx, row_data in enumerate(table_data):
            y_pos = row_y_positions[row_idx]
            
            cell_left = Text(row_data[0], font="PingFang SC", font_size=18, color=WHITE).move_to(LEFT * 2.5 + UP * y_pos)
            cell_center = Text(row_data[1], font="PingFang SC", font_size=18, color=WHITE).move_to(UP * y_pos)
            
            if row_data[2] == "-":
                cell_right = Text(row_data[2], font="PingFang SC", font_size=18, color=GRAY_B).move_to(RIGHT * 2.5 + UP * y_pos)
            else:
                cell_right = Text(row_data[2], font="PingFang SC", font_size=18, color=WHITE).move_to(RIGHT * 2.5 + UP * y_pos)
            
            self.play(
                FadeIn(cell_left, shift=RIGHT * 0.3),
                FadeIn(cell_center, shift=RIGHT * 0.3),
                FadeIn(cell_right, shift=RIGHT * 0.3),
                run_time=0.6
            )
            self.wait(0.4)
        
        # 整体闪烁强调
        all_elements = VGroup(
            axes_left, para_left, dot_left_1, dot_left_2, delta_left,
            axes_center, para_center, dot_center, delta_center,
            axes_right, para_right, delta_right
        )
        
        self.play(
            Flash(all_elements, color=YELLOW, flash_radius=1.5),
            run_time=0.8
        )
        self.wait(2.0)
        
        # 清理
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != self.author_info], run_time=0.5)
    
    def scene_7_formula_emphasis(self):
        """场景7: 判别式公式强化 (75-82秒)"""
        # 判别式公式大字显示
        delta_formula = MathTex(
            r"\Delta = b^2 - 4ac",
            font_size=52,
            color=self.COLOR_DISCRIMINANT
        ).move_to(UP * 2)
        
        self.play(GrowFromCenter(delta_formula), run_time=0.8)
        self.wait(0.3)
        
        # 多次闪烁强调
        for _ in range(2):
            self.play(
                Flash(delta_formula, color=YELLOW, flash_radius=0.8),
                run_time=0.4
            )
            self.wait(0.2)
        
        # 三种情况图标
        icon_positive = VGroup(
            MathTex(r"\Delta > 0", font_size=24, color=self.COLOR_DISCRIMINANT),
            MathTex(r"\Downarrow", font_size=20),
            Text("2个交点", font="PingFang SC", font_size=20)
        ).arrange(DOWN, buff=0.15).move_to(LEFT * 2.5 + DOWN * 1.5)
        
        icon_zero = VGroup(
            MathTex(r"\Delta = 0", font_size=24, color=self.COLOR_DISCRIMINANT),
            MathTex(r"\Downarrow", font_size=20),
            Text("1个交点", font="PingFang SC", font_size=20)
        ).arrange(DOWN, buff=0.15).move_to(DOWN * 1.5)
        
        icon_negative = VGroup(
            MathTex(r"\Delta < 0", font_size=24, color=self.COLOR_DISCRIMINANT),
            MathTex(r"\Downarrow", font_size=20),
            Text("0个交点", font="PingFang SC", font_size=20)
        ).arrange(DOWN, buff=0.15).move_to(RIGHT * 2.5 + DOWN * 1.5)
        
        icons = VGroup(icon_positive, icon_zero, icon_negative)
        
        self.play(
            FadeIn(icon_positive, shift=UP * 0.5),
            FadeIn(icon_zero, shift=UP * 0.5),
            FadeIn(icon_negative, shift=UP * 0.5),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 关键提示
        reminder = Text(
            "记住判别式!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 5)
        
        self.play(
            FadeIn(reminder, scale=1.2),
            Flash(reminder, color=YELLOW, flash_radius=0.5),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(delta_formula),
            FadeOut(icons),
            FadeOut(reminder),
            run_time=0.5
        )
    
    def scene_8_outro(self):
        """场景8: 片尾关注 (82-90秒)"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=GRAY_B
        ).move_to(UP * 0.8)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        
        # 关注引导
        follow_text = Text(
            "关注我，轻松学二次函数!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 0.5)
        
        self.play(
            Write(follow_text),
            Flash(follow_text, color=YELLOW, flash_radius=0.5),
            run_time=0.7
        )
        
        # 装饰抛物线（代表三种情况）
        decorative_axes = Axes(
            x_range=[-1, 3, 1],
            y_range=[-1, 2, 1],
            x_length=1.2,
            y_length=1.2,
            axis_config={'stroke_width': 0}
        )
        
        colors = [self.COLOR_PARABOLA, self.COLOR_DISCRIMINANT, self.COLOR_INTERSECTION]
        
        decorative_parabolas = VGroup()
        for i, color in enumerate(colors):
            small_para = decorative_axes.plot(lambda x: 0.5 * (x-1)**2, x_range=[0, 2], color=color, stroke_width=3)
            angle = i * 2 * PI / 3
            position = 2 * np.array([np.cos(angle), np.sin(angle), 0]) + DOWN * 2.5
            para_group = VGroup(decorative_axes.copy(), small_para).move_to(position)
            decorative_parabolas.add(para_group)
        
        self.play(*[FadeIn(p, scale=0.5) for p in decorative_parabolas], run_time=0.5)
        self.play(Rotate(decorative_parabolas, angle=PI, run_time=1.5))
        
        # 闪烁强调
        self.play(
            Flash(follow_text, color=YELLOW, flash_radius=0.5),
            run_time=0.4
        )
        self.wait(1.2)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorative_parabolas),
            run_time=1.0
        )


# ==================== 运行命令 ====================
# 快速预览:
#   manim -pql quadratic_equation_relation.py QuadraticEquationRelation
#
# 高质量渲染:
#   manim -qh quadratic_equation_relation.py QuadraticEquationRelation
#
# 4K质量:
#   manim -qk quadratic_equation_relation.py QuadraticEquationRelation