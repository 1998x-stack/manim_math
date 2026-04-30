"""
椭圆中点弦问题 - Ellipse Chord Midpoint Animation
使用点差法求解椭圆中点弦的斜率

内容: 点差法推导椭圆中点弦斜率公式
目标观众: 高中学生
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


class EllipseChordMidpoint(Scene):
    """
    椭圆中点弦教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 问题设定
    3. 点差法介绍
    4. 代数推导
    5. 得到斜率公式
    6. 几何验证
    7. 特殊情况
    8. 总结
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_ELLIPSE = "#3498db"       # 蓝色 - 椭圆
        self.COLOR_CHORD = "#e74c3c"         # 红色 - 弦AB
        self.COLOR_MIDPOINT = "#f39c12"      # 橙色 - 中点M
        self.COLOR_SLOPE_LINE = "#2ecc71"    # 绿色 - 斜率线
        self.COLOR_FORMULA = "#9b59b6"       # 紫色 - 公式
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_problem_setup()
        self.show_point_difference_method()
        self.show_algebraic_derivation()
        self.show_slope_formula()
        self.show_geometric_verification()
        self.show_special_cases()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化椭圆和所有几何元素"""
        # ========== 椭圆参数 ==========
        self.a = 4.0  # 长半轴
        self.b = 2.0  # 短半轴
        
        # ========== 缩放和偏移 ==========
        self.ELLIPSE_SCALE = 0.7
        self.ELLIPSE_OFFSET = UP * 1.0
        
        # ========== 精确计算的坐标 (来自 verify_geometry.py) ==========
        # 原始坐标
        self.x0_orig = 1.5
        self.y0_orig = 0.8
        
        self.x1_orig = 3.940408
        self.y1_orig = -0.343941
        
        self.x2_orig = -0.940408
        self.y2_orig = 1.943941
        
        # Manim使用的坐标 (缩放后)
        self.A = np.array([2.758286, 0.759241, 0.000000])
        self.B = np.array([-0.658286, 2.360759, 0.000000])
        self.M = np.array([1.050000, 1.560000, 0.000000])
        
        # 斜率
        self.k = -0.468750
        
        # ========== 椭圆对象 ==========
        self.ellipse_width = 2 * self.a * self.ELLIPSE_SCALE
        self.ellipse_height = 2 * self.b * self.ELLIPSE_SCALE
        
        # 验证几何关系
        self.verify_geometry()
        
        print("✓ 几何初始化完成")
    
    def verify_geometry(self):
        """验证几何关系的正确性"""
        epsilon = 1e-6
        
        # 验证中点
        midpoint_calc = (self.A + self.B) / 2
        dist = np.linalg.norm(midpoint_calc - self.M)
        
        if dist > epsilon:
            print(f"WARNING: 中点计算误差 = {dist:.6f}")
        
        # 验证斜率
        if abs(self.B[0] - self.A[0]) > epsilon:
            k_calc = (self.B[1] - self.A[1]) / (self.B[0] - self.A[0])
            k_error = abs(k_calc - self.k)
            
            if k_error > epsilon:
                print(f"WARNING: 斜率计算误差 = {k_error:.6f}")
    
    def show_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子主标题
        hook_main = Text(
            "椭圆的中点弦",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        # 钩子副标题
        hook_sub = Text(
            "已知中点M，弦AB的斜率是多少?",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 5.2)
        
        self.play(Write(hook_main), run_time=1.0)
        self.play(FadeIn(hook_sub), run_time=0.4)
        
        # 椭圆淡入
        ellipse = Ellipse(
            width=self.ellipse_width,
            height=self.ellipse_height,
            color=self.COLOR_ELLIPSE,
            stroke_width=3
        ).move_to(self.ELLIPSE_OFFSET)
        
        self.play(Create(ellipse), run_time=1.2)
        
        # 中点M闪现
        dot_M = Dot(self.M, color=self.COLOR_MIDPOINT, radius=0.12)
        label_M = MathTex("M", font_size=24, color=self.COLOR_MIDPOINT).next_to(dot_M, UR, buff=0.15)
        
        self.play(
            FadeIn(dot_M, scale=0.5),
            Flash(dot_M, color=self.COLOR_MIDPOINT, flash_radius=0.3),
            run_time=0.5
        )
        self.play(Write(label_M), run_time=0.3)
        
        # 弦AB绘制
        chord_AB = Line(self.A, self.B, color=self.COLOR_CHORD, stroke_width=4)
        self.play(Create(chord_AB), run_time=0.8)
        
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(hook_main),
            FadeOut(hook_sub),
            run_time=0.5
        )
        
        # 保存对象供后续使用
        self.ellipse = ellipse
        self.chord_AB = chord_AB
        self.dot_M = dot_M
        self.label_M = label_M
    
    def show_problem_setup(self):
        """场景2: 问题设定 (5-12秒)"""
        # 椭圆方程
        ellipse_eq = MathTex(
            r"\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1",
            font_size=32,
            color=self.COLOR_ELLIPSE
        ).move_to(UP * 5.5)
        
        self.play(Write(ellipse_eq), run_time=0.8)
        
        # 添加端点
        dot_A = Dot(self.A, color=self.COLOR_CHORD, radius=0.10)
        label_A = MathTex("A", font_size=22, color=self.COLOR_CHORD).next_to(dot_A, UL, buff=0.1)
        
        dot_B = Dot(self.B, color=self.COLOR_CHORD, radius=0.10)
        label_B = MathTex("B", font_size=22, color=self.COLOR_CHORD).next_to(dot_B, DR, buff=0.1)
        
        # 条件1: A在椭圆上
        cond_1 = VGroup(
            Text("条件1: ", font="PingFang SC", font_size=24, color=GRAY_A),
            MathTex(r"A(x_1, y_1)", font_size=24, color=self.COLOR_CHORD),
            Text(" 在椭圆上", font="PingFang SC", font_size=24, color=GRAY_A)
        ).arrange(RIGHT, buff=0.1).move_to(UP * 4.5 + LEFT * 2)
        
        self.play(FadeIn(cond_1, shift=UP * 0.2), run_time=0.5)
        self.play(
            FadeIn(dot_A, scale=0.5),
            Flash(dot_A, color=self.COLOR_CHORD),
            Write(label_A),
            run_time=0.4
        )
        
        # 条件2: B在椭圆上
        cond_2 = VGroup(
            Text("条件2: ", font="PingFang SC", font_size=24, color=GRAY_A),
            MathTex(r"B(x_2, y_2)", font_size=24, color=self.COLOR_CHORD),
            Text(" 在椭圆上", font="PingFang SC", font_size=24, color=GRAY_A)
        ).arrange(RIGHT, buff=0.1).move_to(UP * 3.8 + LEFT * 2)
        
        self.play(FadeIn(cond_2, shift=UP * 0.2), run_time=0.5)
        self.play(
            FadeIn(dot_B, scale=0.5),
            Flash(dot_B, color=self.COLOR_CHORD),
            Write(label_B),
            run_time=0.4
        )
        
        # 条件3: M是中点
        cond_3 = VGroup(
            Text("条件3: ", font="PingFang SC", font_size=24, color=GRAY_A),
            MathTex(r"M(x_0, y_0)", font_size=24, color=self.COLOR_MIDPOINT),
            Text(" 是中点", font="PingFang SC", font_size=24, color=GRAY_A)
        ).arrange(RIGHT, buff=0.1).move_to(UP * 3.1 + LEFT * 2)
        
        self.play(FadeIn(cond_3, shift=UP * 0.2), run_time=0.5)
        
        # 中点关系动画
        dashed_MA = DashedLine(self.M, self.A, color=self.COLOR_AUXILIARY, dash_length=0.08)
        dashed_MB = DashedLine(self.M, self.B, color=self.COLOR_AUXILIARY, dash_length=0.08)
        
        self.play(
            Create(dashed_MA),
            Create(dashed_MB),
            run_time=0.6
        )
        
        # 目标框
        goal_box = VGroup(
            Text("求: 弦AB的斜率", font="PingFang SC", font_size=28, color=self.COLOR_HIGHLIGHT),
            MathTex(r"k = ?", font_size=32, color=self.COLOR_SLOPE_LINE)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 5)
        
        self.play(FadeIn(goal_box, shift=DOWN * 0.3), run_time=0.6)
        
        self.wait(2.7)
        
        # 清理
        self.play(
            FadeOut(ellipse_eq),
            FadeOut(cond_1),
            FadeOut(cond_2),
            FadeOut(cond_3),
            FadeOut(goal_box),
            FadeOut(dashed_MA),
            FadeOut(dashed_MB),
            run_time=0.6
        )
        
        # 保存对象
        self.dot_A = dot_A
        self.dot_B = dot_B
        self.label_A = label_A
        self.label_B = label_B
    
    def show_point_difference_method(self):
        """场景3: 点差法介绍 (12-20秒)"""
        # 标题
        title_method = Text(
            "点差法",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_FORMULA
        ).move_to(UP * 6.5)
        
        # 核心思想
        idea_text = Text(
            "两点都在椭圆上 → 两式相减 → 得到关系",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 5.8)
        
        self.play(Write(title_method), run_time=0.6)
        self.play(FadeIn(idea_text, shift=UP * 0.2), run_time=0.8)
        
        # 方程1: A在椭圆上
        eq_A = MathTex(
            r"\frac{x_1^2}{a^2} + \frac{y_1^2}{b^2} = 1",
            font_size=30,
            color=self.COLOR_CHORD
        ).move_to(UP * 4.5)
        
        self.play(Write(eq_A), run_time=1.0)
        self.play(Indicate(self.dot_A), run_time=0.4)
        
        # 方程2: B在椭圆上
        eq_B = MathTex(
            r"\frac{x_2^2}{a^2} + \frac{y_2^2}{b^2} = 1",
            font_size=30,
            color=self.COLOR_CHORD
        ).move_to(UP * 3.5)
        
        self.play(Write(eq_B), run_time=1.0)
        self.play(Indicate(self.dot_B), run_time=0.4)
        
        # 减号
        minus_sign = MathTex(
            r"-",
            font_size=40,
            color=YELLOW
        ).move_to(UP * 4.0 + LEFT * 3.5)
        
        self.play(FadeIn(minus_sign), run_time=0.3)
        
        # 提示
        subtract_hint = Text(
            "两式相减",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(subtract_hint, shift=DOWN * 0.2), run_time=0.5)
        
        self.wait(3.0)
        
        # 清理
        self.play(
            FadeOut(title_method),
            FadeOut(idea_text),
            FadeOut(subtract_hint),
            run_time=0.4
        )
        
        # 保存对象
        self.eq_A = eq_A
        self.eq_B = eq_B
        self.minus_sign = minus_sign
    
    def show_algebraic_derivation(self):
        """场景4: 代数推导 (20-32秒)"""
        # 清除前面方程
        self.play(
            FadeOut(self.eq_A),
            FadeOut(self.eq_B),
            FadeOut(self.minus_sign),
            run_time=0.4
        )
        
        # 相减结果
        subtract_result = MathTex(
            r"\frac{x_1^2 - x_2^2}{a^2} + \frac{y_1^2 - y_2^2}{b^2} = 0",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(Write(subtract_result), run_time=1.2)
        self.wait(1.0)
        
        # 因式分解提示
        factor_hint = Text(
            "因式分解",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)
        
        self.play(FadeIn(factor_hint), run_time=0.5)
        
        # 因式分解结果
        factored = MathTex(
            r"\frac{(x_1 - x_2)(x_1 + x_2)}{a^2} + \frac{(y_1 - y_2)(y_1 + y_2)}{b^2} = 0",
            font_size=26,
            color=self.COLOR_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(
            TransformMatchingTex(subtract_result, factored),
            FadeOut(factor_hint),
            run_time=1.5
        )
        
        self.wait(1.2)
        
        # 中点公式提示
        midpoint_hint = Text(
            "利用中点坐标关系",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.play(FadeIn(midpoint_hint), run_time=0.6)
        
        # 中点公式
        midpoint_formulas = VGroup(
            MathTex(r"x_1 + x_2 = 2x_0", font_size=24),
            MathTex(r"y_1 + y_2 = 2y_0", font_size=24)
        ).arrange(RIGHT, buff=0.8).move_to(UP * 1.8)
        
        self.play(Write(midpoint_formulas), run_time=1.0)
        
        # 代入中点后
        with_midpoint = MathTex(
            r"\frac{2x_0(x_1 - x_2)}{a^2} + \frac{2y_0(y_1 - y_2)}{b^2} = 0",
            font_size=26,
            color=self.COLOR_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(
            TransformMatchingTex(factored, with_midpoint),
            FadeOut(midpoint_hint),
            run_time=1.5
        )
        
        self.wait(3.1)
        
        # 清理
        self.play(
            FadeOut(midpoint_formulas),
            run_time=0.4
        )
        
        # 保存对象
        self.with_midpoint = with_midpoint
    
    def show_slope_formula(self):
        """场景5: 得到斜率公式 (32-42秒)"""
        # 斜率定义
        slope_def = MathTex(
            r"k = \frac{y_1 - y_2}{x_1 - x_2}",
            font_size=28,
            color=self.COLOR_SLOPE_LINE
        ).move_to(UP * 3.0)
        
        self.play(FadeIn(slope_def), run_time=0.6)
        self.wait(0.8)
        
        # 提示
        divide_hint = Text(
            "两边同时除以 (x₁ - x₂)",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 2.0)
        
        self.play(Write(divide_hint), run_time=0.8)
        
        # 整理后的式子
        rearranged = MathTex(
            r"\frac{x_0}{a^2} + \frac{y_0}{b^2} \cdot k = 0",
            font_size=28,
            color=self.COLOR_FORMULA
        ).move_to(UP * 4.5)
        
        self.play(
            TransformMatchingTex(self.with_midpoint, rearranged),
            FadeOut(divide_hint),
            run_time=1.5
        )
        
        self.wait(1.0)
        
        # 最终公式
        final_formula_content = VGroup(
            Text("中点弦斜率公式:", font="PingFang SC", font_size=28, color=self.COLOR_HIGHLIGHT),
            MathTex(
                r"k = -\frac{b^2 x_0}{a^2 y_0}",
                font_size=36,
                color=self.COLOR_SLOPE_LINE
            )
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 4.5)
        
        # 边框
        formula_rect = SurroundingRectangle(
            final_formula_content,
            color=YELLOW,
            buff=0.3,
            stroke_width=3
        )
        
        final_formula_box = VGroup(final_formula_content, formula_rect)
        
        self.play(FadeIn(final_formula_box, shift=UP * 0.3), run_time=1.0)
        self.play(Circumscribe(final_formula_box, color=YELLOW), run_time=1.0)
        
        self.wait(3.3)
        
        # 清理
        self.play(
            FadeOut(slope_def),
            FadeOut(rearranged),
            run_time=0.6
        )
        
        # 保存对象
        self.final_formula_box = final_formula_box
    
    def show_geometric_verification(self):
        """场景6: 几何验证 (42-54秒)"""
        # 公式移到左上角
        self.play(
            self.final_formula_box.animate.scale(0.6).to_corner(UL, buff=0.3),
            run_time=0.8
        )
        
        # 验证说明
        verify_text = Text(
            "几何验证",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(verify_text), run_time=0.5)
        
        # 计算过程 (使用实际数值)
        calc_steps = VGroup(
            MathTex(r"k = -\frac{2^2 \times 1.5}{4^2 \times 0.8}", font_size=26),
            MathTex(r"k = -\frac{6}{12.8}", font_size=26),
            MathTex(r"k \approx -0.469", font_size=26)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(UP * 3.5 + LEFT * 1.5)
        
        for i, step in enumerate(calc_steps):
            self.play(Write(step), run_time=0.5)
        
        # k值
        k_value = MathTex(
            r"k \approx -0.469",
            font_size=30,
            color=self.COLOR_SLOPE_LINE
        ).move_to(UP * 1.8)
        
        self.play(Write(k_value), run_time=0.6)
        
        # 绘制斜率线 (通过M，斜率为k)
        slope_angle = np.arctan(self.k)
        slope_line_length = 3.0
        
        slope_line = Line(
            self.M + LEFT * slope_line_length / 2,
            self.M + RIGHT * slope_line_length / 2,
            color=self.COLOR_SLOPE_LINE,
            stroke_width=3
        ).rotate(slope_angle, about_point=self.M)
        
        self.play(Create(slope_line), run_time=1.2)
        self.play(slope_line.animate.scale(1.5, about_point=self.M), run_time=0.8)
        
        # 验证提示
        check_text = Text(
            "用两点坐标验证:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(check_text), run_time=0.5)
        
        # 两点斜率
        two_point_slope = MathTex(
            r"k = \frac{y_2 - y_1}{x_2 - x_1} \approx -0.469",
            font_size=26,
            color=self.COLOR_SLOPE_LINE
        ).move_to(DOWN * 4.5)
        
        self.play(Write(two_point_slope), run_time=1.2)
        
        # 结果一致动画
        self.play(
            k_value.animate.move_to(DOWN * 5.5 + LEFT * 1.5),
            two_point_slope.animate.move_to(DOWN * 5.5 + RIGHT * 1.5),
            run_time=0.8
        )
        
        # 成功标记
        checkmark = Text(
            "✓ 验证成功!",
            font="PingFang SC",
            font_size=32,
            color=GREEN
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(checkmark), run_time=0.4)
        
        self.wait(3.7)
        
        # 清理
        self.play(
            FadeOut(verify_text),
            FadeOut(calc_steps),
            FadeOut(k_value),
            FadeOut(check_text),
            FadeOut(two_point_slope),
            FadeOut(checkmark),
            FadeOut(slope_line),
            run_time=0.6
        )
    
    def show_special_cases(self):
        """场景7: 特殊情况 (54-70秒)"""
        # 清理图形
        self.play(
            FadeOut(self.ellipse),
            FadeOut(self.chord_AB),
            FadeOut(self.dot_A),
            FadeOut(self.dot_B),
            FadeOut(self.dot_M),
            FadeOut(self.label_A),
            FadeOut(self.label_B),
            FadeOut(self.label_M),
            run_time=0.5
        )
        
        # 标题
        special_title = Text(
            "特殊情况",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(special_title), run_time=0.6)
        
        # 情况1: y₀ = 0
        card_1 = VGroup(
            Text("情况1: ", font="PingFang SC", font_size=24, color=YELLOW),
            MathTex(r"y_0 = 0", font_size=24),
            Text(" → 弦垂直于x轴", font="PingFang SC", font_size=20, color=GRAY_A)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 5.0 + LEFT * 10)
        
        self.play(card_1.animate.shift(RIGHT * 10), run_time=0.8)
        
        # 图示1
        small_ellipse_1 = Ellipse(
            width=1.5, height=0.8, color=self.COLOR_ELLIPSE, stroke_width=2
        ).move_to(UP * 4.5 + RIGHT * 2.5)
        
        vertical_chord = Line(
            UP * 4.9 + RIGHT * 2.5,
            UP * 4.1 + RIGHT * 2.5,
            color=self.COLOR_CHORD,
            stroke_width=3
        )
        
        self.play(
            Create(small_ellipse_1),
            Create(vertical_chord),
            run_time=1.5
        )
        
        # 情况2: x₀ = 0
        card_2 = VGroup(
            Text("情况2: ", font="PingFang SC", font_size=24, color=YELLOW),
            MathTex(r"x_0 = 0", font_size=24),
            Text(" → 弦平行于x轴", font="PingFang SC", font_size=20, color=GRAY_A)
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.5 + LEFT * 10)
        
        self.play(card_2.animate.shift(RIGHT * 10), run_time=0.8)
        
        # 图示2
        small_ellipse_2 = Ellipse(
            width=1.5, height=0.8, color=self.COLOR_ELLIPSE, stroke_width=2
        ).move_to(UP * 3.0 + RIGHT * 2.5)
        
        horizontal_chord = Line(
            UP * 3.0 + RIGHT * 2.0,
            UP * 3.0 + RIGHT * 3.0,
            color=self.COLOR_CHORD,
            stroke_width=3
        )
        
        self.play(
            Create(small_ellipse_2),
            Create(horizontal_chord),
            run_time=1.5
        )
        
        # 情况3: M在椭圆上
        card_3 = VGroup(
            Text("情况3: M在椭圆上 → 切线斜率", font="PingFang SC", font_size=20, color=GRAY_A)
        ).move_to(UP * 2.0 + LEFT * 10)
        
        self.play(card_3.animate.shift(RIGHT * 10), run_time=0.8)
        
        # 图示3
        small_ellipse_3 = Ellipse(
            width=1.5, height=0.8, color=self.COLOR_ELLIPSE, stroke_width=2
        ).move_to(UP * 1.5 + RIGHT * 2.5)
        
        tangent_point = np.array([3.25, 1.5, 0])
        tangent_line = Line(
            tangent_point + UP * 0.5 + LEFT * 0.3,
            tangent_point + DOWN * 0.5 + RIGHT * 0.3,
            color=self.COLOR_SLOPE_LINE,
            stroke_width=3
        )
        
        self.play(
            Create(small_ellipse_3),
            Create(tangent_line),
            run_time=1.5
        )
        
        # 汇总
        summary_text = Text(
            "公式适用于: M在椭圆内部, y₀≠0",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(summary_text), run_time=0.8)
        
        self.wait(7.2)
        
        # 清理
        self.play(
            FadeOut(card_1),
            FadeOut(card_2),
            FadeOut(card_3),
            FadeOut(small_ellipse_1),
            FadeOut(small_ellipse_2),
            FadeOut(small_ellipse_3),
            FadeOut(vertical_chord),
            FadeOut(horizontal_chord),
            FadeOut(tangent_line),
            FadeOut(summary_text),
            run_time=0.6
        )
        
        # 保存标题
        self.special_title = special_title
    
    def show_summary(self):
        """场景8: 总结 (70-90秒)"""
        # 标题变换
        summary_title = Text(
            "核心总结",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(Transform(self.special_title, summary_title), run_time=0.6)
        
        # 大号公式回到中央
        big_formula = MathTex(
            r"k = -\frac{b^2 x_0}{a^2 y_0}",
            font_size=48,
            color=self.COLOR_SLOPE_LINE
        ).move_to(UP * 4.5)
        
        big_rect = SurroundingRectangle(
            big_formula,
            color=YELLOW,
            buff=0.4,
            stroke_width=4
        )
        
        big_formula_group = VGroup(big_formula, big_rect)
        
        self.play(
            Transform(self.final_formula_box, big_formula_group),
            run_time=1.0
        )
        
        # 三要点卡片
        point_1 = Text("✓ 点差法: 两式相减", font="PingFang SC", font_size=24, color=GRAY_A).move_to(UP * 2.5)
        point_2 = Text("✓ 利用中点坐标关系", font="PingFang SC", font_size=24, color=GRAY_A).move_to(UP * 1.5)
        point_3 = Text("✓ 适用于椭圆/双曲线/抛物线", font="PingFang SC", font_size=24, color=GRAY_A).move_to(UP * 0.5)
        
        for point in [point_1, point_2, point_3]:
            self.play(FadeIn(point, shift=RIGHT * 0.5), run_time=0.6)
        
        # 装饰动画
        decorations = VGroup(*[
            Ellipse(width=0.6, height=0.4, color=self.COLOR_ELLIPSE, fill_opacity=0.3)
            .move_to(UP * 0.5 + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(FadeIn(decorations), run_time=1.0)
        
        # 应用场景
        application_text = Text(
            "应用: 求弦方程、弦长、对称问题",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.0)
        
        self.play(FadeIn(application_text), run_time=1.0)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 3.0)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(DOWN * 4.0)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 掌握更多解题技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰旋转
        self.play(Rotate(decorations, angle=PI, run_time=2.0))
        
        self.wait(10.7)


# 运行命令:
# manim -pql ellipse_chord_midpoint.py EllipseChordMidpoint  # 快速预览
# manim -qh ellipse_chord_midpoint.py EllipseChordMidpoint   # 高质量渲染