"""
锐角三角比的定义 - Trigonometric Ratios Definition Animation
使用 Manim 创建的九年级数学教学视频

内容: 正弦、余弦、正切的定义及不变性
目标观众: 九年级学生
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


class TrigonometricRatios(Scene):
    """
    锐角三角比教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 认识三条边
    3. 正弦 sinA 的定义
    4. 余弦 cosA 的定义
    5. 正切 tanA 的定义
    6. 三角比的不变性
    7. 公式总结
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_TRIANGLE = WHITE
        self.COLOR_OPPOSITE = "#e74c3c"       # 红色 - 对边
        self.COLOR_ADJACENT = "#3498db"       # 蓝色 - 邻边
        self.COLOR_HYPOTENUSE = "#2ecc71"     # 绿色 - 斜边
        self.COLOR_ANGLE = "#f39c12"          # 橙色 - 锐角
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_FORMULA = "#9b59b6"        # 紫色 - 公式
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_three_sides()
        self.show_sine_definition()
        self.show_cosine_definition()
        self.show_tangent_definition()
        self.show_invariance()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化直角三角形和所有几何数据"""
        # ===== 基准参数 =====
        self.angle_A_value = 35 * DEGREES  # 锐角A约35度
        self.adjacent_length = 3.0         # 邻边CB长度
        
        # ===== 精确计算对边和斜边 =====
        # 使用三角函数精确计算
        self.opposite_length = self.adjacent_length * np.tan(self.angle_A_value)
        self.hypotenuse_length = self.adjacent_length / np.cos(self.angle_A_value)
        
        # ===== 定义三角形顶点 =====
        # C为直角顶点，放在原点
        # B在C的右侧（邻边）
        # A在B的上方（构成直角三角形）
        
        self.SCALE = 0.85
        self.OFFSET = UP * 0.5
        
        # 原始坐标
        self.C_base = np.array([0, 0, 0])
        self.B_base = self.C_base + self.adjacent_length * RIGHT
        self.A_base = self.B_base + self.opposite_length * UP
        
        # 应用缩放和偏移
        self.C = self.C_base * self.SCALE + self.OFFSET
        self.B = self.B_base * self.SCALE + self.OFFSET
        self.A = self.A_base * self.SCALE + self.OFFSET
        
        # ===== 计算实际长度（用于显示）=====
        self.opposite = np.linalg.norm(self.A - self.B)
        self.adjacent = np.linalg.norm(self.B - self.C)
        self.hypotenuse = np.linalg.norm(self.A - self.C)
        
        # ===== 计算三角比值 =====
        self.sin_A = self.opposite / self.hypotenuse
        self.cos_A = self.adjacent / self.hypotenuse
        self.tan_A = self.opposite / self.adjacent
        
        # ===== 验证几何关系 =====
        self.verify_geometry()
        
        # ===== 创建基本图形对象（但不添加到场景）=====
        self.triangle = Polygon(
            self.C, self.B, self.A,
            color=self.COLOR_TRIANGLE,
            stroke_width=3
        )
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证勾股定理: a² + b² = c²
        pythagorean_check = self.opposite**2 + self.adjacent**2
        hypotenuse_squared = self.hypotenuse**2
        
        if abs(pythagorean_check - hypotenuse_squared) > epsilon:
            print(f"WARNING: 勾股定理验证失败!")
            print(f"  a² + b² = {pythagorean_check:.6f}")
            print(f"  c² = {hypotenuse_squared:.6f}")
        
        # 验证角C是否为直角
        vec_CA = self.A - self.C
        vec_CB = self.B - self.C
        dot_product = np.dot(vec_CA[:2], vec_CB[:2])
        
        if abs(dot_product) > epsilon:
            print(f"WARNING: 角C不是直角! 点积 = {dot_product:.6f}")
        
        # 验证三角比计算
        sin_check = np.sin(self.angle_A_value)
        if abs(self.sin_A - sin_check) > 0.01:
            print(f"WARNING: sin值计算偏差: {self.sin_A:.4f} vs {sin_check:.4f}")
        
        print("✓ 几何验证完成")
        print(f"  对边: {self.opposite:.3f}")
        print(f"  邻边: {self.adjacent:.3f}")
        print(f"  斜边: {self.hypotenuse:.3f}")
        print(f"  sin A: {self.sin_A:.3f}")
        print(f"  cos A: {self.cos_A:.3f}")
        print(f"  tan A: {self.tan_A:.3f}")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_question = Text(
            "如何用边长表示角的大小?",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_question), run_time=1.2)
        
        # 创建直角三角形
        self.play(Create(self.triangle), run_time=1.0)
        
        # 标注顶点
        label_A = MathTex("A", font_size=28, color=WHITE).next_to(self.A, UR, buff=0.15)
        label_B = MathTex("B", font_size=28, color=WHITE).next_to(self.B, DR, buff=0.15)
        label_C = MathTex("C", font_size=28, color=WHITE).next_to(self.C, DL, buff=0.15)
        
        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C),
            run_time=0.8
        )
        
        # 角A闪烁
        angle_A_arc = Angle.from_three_points(
            self.B, self.A, self.C,
            radius=0.4,
            color=self.COLOR_ANGLE,
            other_angle=False
        )
        
        self.play(
            Create(angle_A_arc),
            Flash(angle_A_arc, color=self.COLOR_ANGLE, flash_radius=0.5),
            run_time=0.8
        )
        
        hint_text = Text(
            "锐角三角比",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_question),
            FadeOut(hint_text),
            FadeOut(angle_A_arc),
            run_time=0.5
        )
        
        # 保存标签供后续使用
        self.label_A = label_A
        self.label_B = label_B
        self.label_C = label_C
    
    def show_three_sides(self):
        """场景2: 认识三条边"""
        # 标题
        title = Text(
            "认识直角三角形的三条边",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建直角标记
        right_angle_mark = RightAngle(
            Line(self.C, self.B),
            Line(self.C, self.A),
            length=0.25,
            color=YELLOW,
            quadrant=(-1, -1)
        )
        
        self.play(Create(right_angle_mark), run_time=0.5)
        
        # 角A标记
        angle_A = Angle.from_three_points(
            self.B, self.A, self.C,
            radius=0.35,
            color=self.COLOR_ANGLE
        )
        
        angle_label = MathTex(r"\angle A", font_size=24, color=self.COLOR_ANGLE).next_to(
            angle_A, DOWN + LEFT, buff=0.1
        )
        
        self.play(Create(angle_A), Write(angle_label), run_time=0.5)
        self.wait(0.3)
        
        # === 介绍斜边 ===
        hyp_line = Line(self.C, self.A, color=self.COLOR_HYPOTENUSE, stroke_width=6)
        
        hyp_label_cn = Text("斜边", font="PingFang SC", font_size=22, color=self.COLOR_HYPOTENUSE)
        hyp_label_math = MathTex("c", font_size=24, color=self.COLOR_HYPOTENUSE)
        hyp_label = VGroup(hyp_label_cn, hyp_label_math).arrange(RIGHT, buff=0.15)
        hyp_label.move_to(self.C + (self.A - self.C) * 0.5 + LEFT * 0.6)
        
        hyp_explain = Text(
            "直角的对边",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(
            Create(hyp_line),
            run_time=0.5
        )
        self.play(
            Write(hyp_label),
            FadeIn(hyp_explain),
            run_time=0.8
        )
        self.wait(1.0)
        self.play(FadeOut(hyp_explain), run_time=0.3)
        
        # === 介绍对边 ===
        opp_line = Line(self.B, self.A, color=self.COLOR_OPPOSITE, stroke_width=6)
        
        opp_label_cn = Text("对边", font="PingFang SC", font_size=22, color=self.COLOR_OPPOSITE)
        opp_label_math = MathTex("a", font_size=24, color=self.COLOR_OPPOSITE)
        opp_label = VGroup(opp_label_cn, opp_label_math).arrange(RIGHT, buff=0.15)
        
        opp_brace = Brace(Line(self.B, self.A), direction=RIGHT, buff=0.1, color=self.COLOR_OPPOSITE)
        opp_label.next_to(opp_brace, RIGHT, buff=0.1)
        
        opp_explain = Text(
            "角A的对边",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(Create(opp_line), run_time=0.5)
        self.play(
            Create(opp_brace),
            Write(opp_label),
            FadeIn(opp_explain),
            run_time=0.8
        )
        self.wait(1.0)
        self.play(FadeOut(opp_explain), run_time=0.3)
        
        # === 介绍邻边 ===
        adj_line = Line(self.C, self.B, color=self.COLOR_ADJACENT, stroke_width=6)
        
        adj_label_cn = Text("邻边", font="PingFang SC", font_size=22, color=self.COLOR_ADJACENT)
        adj_label_math = MathTex("b", font_size=24, color=self.COLOR_ADJACENT)
        adj_label = VGroup(adj_label_cn, adj_label_math).arrange(RIGHT, buff=0.15)
        
        adj_brace = Brace(Line(self.C, self.B), direction=DOWN, buff=0.1, color=self.COLOR_ADJACENT)
        adj_label.next_to(adj_brace, DOWN, buff=0.1)
        
        adj_explain = Text(
            "角A的邻边",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(Create(adj_line), run_time=0.5)
        self.play(
            Create(adj_brace),
            Write(adj_label),
            FadeIn(adj_explain),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(adj_explain),
            FadeOut(opp_brace),
            FadeOut(adj_brace),
            run_time=0.5
        )
        
        # 将彩色线段替换原三角形的边
        self.play(
            FadeOut(self.triangle),
            run_time=0.3
        )
        
        # 保存元素供后续使用
        self.right_angle_mark = right_angle_mark
        self.angle_A = angle_A
        self.angle_label = angle_label
        self.hyp_line = hyp_line
        self.opp_line = opp_line
        self.adj_line = adj_line
        self.hyp_label = hyp_label
        self.opp_label = opp_label
        self.adj_label = adj_label
        
        # 创建三角形组（彩色边）
        self.colored_triangle = VGroup(hyp_line, opp_line, adj_line)
    
    def show_sine_definition(self):
        """场景3: 正弦 sinA 的定义"""
        # 标题
        title_cn = Text("正弦", font="PingFang SC", font_size=36, color=self.COLOR_FORMULA)
        title_en = MathTex(r"\text{sine}", font_size=32, color=GRAY_A)
        title = VGroup(title_cn, title_en).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义文字
        definition = Text(
            "对边与斜边的比值",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(definition), run_time=0.5)
        
        # 公式推导
        formula_pos = UP * 1.5
        
        # sin A =
        sin_symbol = MathTex(r"\sin A =", font_size=36, color=self.COLOR_FORMULA).move_to(formula_pos + LEFT * 2)
        
        self.play(Write(sin_symbol), run_time=0.8)
        
        # 对边高亮
        self.play(
            Flash(self.opp_line, color=self.COLOR_OPPOSITE, flash_radius=0.5),
            self.opp_label.animate.set_color(YELLOW).scale(1.2),
            run_time=0.5
        )
        
        # 分数：对边/斜边
        numerator_cn = Text("对边", font="PingFang SC", font_size=24, color=self.COLOR_OPPOSITE)
        fraction_line = Line(LEFT * 0.6, RIGHT * 0.6, color=WHITE, stroke_width=2)
        denominator_cn = Text("斜边", font="PingFang SC", font_size=24, color=self.COLOR_HYPOTENUSE)
        
        fraction = VGroup(
            numerator_cn,
            fraction_line,
            denominator_cn
        ).arrange(DOWN, buff=0.15).next_to(sin_symbol, RIGHT, buff=0.3)
        
        self.play(Write(numerator_cn), run_time=0.5)
        self.play(Create(fraction_line), run_time=0.3)
        
        # 斜边高亮
        self.play(
            Flash(self.hyp_line, color=self.COLOR_HYPOTENUSE, flash_radius=0.5),
            self.hyp_label.animate.set_color(YELLOW).scale(1.2),
            run_time=0.5
        )
        
        self.play(Write(denominator_cn), run_time=0.5)
        
        # 恢复标签颜色
        self.play(
            self.opp_label.animate.set_color(self.COLOR_OPPOSITE).scale(1/1.2),
            self.hyp_label.animate.set_color(self.COLOR_HYPOTENUSE).scale(1/1.2),
            run_time=0.3
        )
        
        # 箭头指向数值
        arrow = Arrow(
            fraction.get_bottom() + DOWN * 0.3,
            fraction.get_bottom() + DOWN * 1.0,
            color=self.COLOR_FORMULA,
            buff=0.1,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 数值公式
        numerical = MathTex(
            r"\sin A = \frac{" + f"{self.opposite:.1f}" + r"}{" + f"{self.hypotenuse:.1f}" + r"}",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 1.5)
        
        self.play(Write(numerical), run_time=0.8)
        
        # 计算结果
        equals = MathTex(r"\approx", font_size=32, color=WHITE).next_to(numerical, RIGHT, buff=0.3)
        result = DecimalNumber(
            self.sin_A,
            num_decimal_places=3,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).next_to(equals, RIGHT, buff=0.3)
        
        self.play(Write(equals), Write(result), run_time=0.8)
        self.play(Flash(result, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.5)
        self.wait(1.5)
        
        # 清理大部分元素，保留核心公式
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(arrow),
            FadeOut(numerical),
            FadeOut(equals),
            FadeOut(result),
            FadeOut(fraction),
            run_time=0.5
        )
        
        # 将sin公式移到左上角作为参考
        sin_ref = MathTex(
            r"\sin A = \frac{a}{c}",
            font_size=24,
            color=self.COLOR_FORMULA
        ).move_to(LEFT * 3 + UP * 6.5)
        
        self.play(Transform(sin_symbol, sin_ref), run_time=0.5)
        self.remove(sin_symbol)
        self.add(sin_ref)
        
        self.sin_ref = sin_ref
    
    def show_cosine_definition(self):
        """场景4: 余弦 cosA 的定义"""
        # 标题
        title_cn = Text("余弦", font="PingFang SC", font_size=36, color=self.COLOR_FORMULA)
        title_en = MathTex(r"\text{cosine}", font_size=32, color=GRAY_A)
        title = VGroup(title_cn, title_en).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义文字
        definition = Text(
            "邻边与斜边的比值",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(definition), run_time=0.5)
        
        # 公式
        cos_symbol = MathTex(r"\cos A =", font_size=36, color=self.COLOR_FORMULA).move_to(UP * 1.5 + LEFT * 2)
        
        self.play(Write(cos_symbol), run_time=0.8)
        
        # 邻边高亮
        self.play(
            Flash(self.adj_line, color=self.COLOR_ADJACENT, flash_radius=0.5),
            self.adj_label.animate.set_color(YELLOW).scale(1.2),
            run_time=0.5
        )
        
        # 分数：邻边/斜边
        numerator_cn = Text("邻边", font="PingFang SC", font_size=24, color=self.COLOR_ADJACENT)
        fraction_line = Line(LEFT * 0.6, RIGHT * 0.6, color=WHITE, stroke_width=2)
        denominator_cn = Text("斜边", font="PingFang SC", font_size=24, color=self.COLOR_HYPOTENUSE)
        
        fraction = VGroup(
            numerator_cn,
            fraction_line,
            denominator_cn
        ).arrange(DOWN, buff=0.15).next_to(cos_symbol, RIGHT, buff=0.3)
        
        self.play(Write(numerator_cn), run_time=0.5)
        self.play(Create(fraction_line), run_time=0.3)
        
        # 斜边高亮
        self.play(
            Flash(self.hyp_line, color=self.COLOR_HYPOTENUSE, flash_radius=0.5),
            self.hyp_label.animate.set_color(YELLOW).scale(1.2),
            run_time=0.5
        )
        
        self.play(Write(denominator_cn), run_time=0.5)
        
        # 恢复颜色
        self.play(
            self.adj_label.animate.set_color(self.COLOR_ADJACENT).scale(1/1.2),
            self.hyp_label.animate.set_color(self.COLOR_HYPOTENUSE).scale(1/1.2),
            run_time=0.3
        )
        
        # 数值计算
        numerical = MathTex(
            r"\cos A = \frac{" + f"{self.adjacent:.1f}" + r"}{" + f"{self.hypotenuse:.1f}" + r"}",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 1.5)
        
        self.play(Write(numerical), run_time=0.8)
        
        equals = MathTex(r"\approx", font_size=32, color=WHITE).next_to(numerical, RIGHT, buff=0.3)
        result = DecimalNumber(
            self.cos_A,
            num_decimal_places=3,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).next_to(equals, RIGHT, buff=0.3)
        
        self.play(Write(equals), Write(result), run_time=0.8)
        self.play(Flash(result, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(numerical),
            FadeOut(equals),
            FadeOut(result),
            FadeOut(fraction),
            run_time=0.5
        )
        
        # cos公式移到参考位置
        cos_ref = MathTex(
            r"\cos A = \frac{b}{c}",
            font_size=24,
            color=self.COLOR_FORMULA
        ).move_to(ORIGIN + UP * 6.5)
        
        self.play(Transform(cos_symbol, cos_ref), run_time=0.5)
        self.remove(cos_symbol)
        self.add(cos_ref)
        
        self.cos_ref = cos_ref
    
    def show_tangent_definition(self):
        """场景5: 正切 tanA 的定义"""
        # 标题
        title_cn = Text("正切", font="PingFang SC", font_size=36, color=self.COLOR_FORMULA)
        title_en = MathTex(r"\text{tangent}", font_size=32, color=GRAY_A)
        title = VGroup(title_cn, title_en).arrange(RIGHT, buff=0.3).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 定义文字
        definition = Text(
            "对边与邻边的比值",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(definition), run_time=0.5)
        
        # 公式
        tan_symbol = MathTex(r"\tan A =", font_size=36, color=self.COLOR_FORMULA).move_to(UP * 1.5 + LEFT * 2)
        
        self.play(Write(tan_symbol), run_time=0.8)
        
        # 对边高亮
        self.play(
            Flash(self.opp_line, color=self.COLOR_OPPOSITE, flash_radius=0.5),
            run_time=0.5
        )
        
        # 分数：对边/邻边
        numerator_cn = Text("对边", font="PingFang SC", font_size=24, color=self.COLOR_OPPOSITE)
        fraction_line = Line(LEFT * 0.6, RIGHT * 0.6, color=WHITE, stroke_width=2)
        denominator_cn = Text("邻边", font="PingFang SC", font_size=24, color=self.COLOR_ADJACENT)
        
        fraction = VGroup(
            numerator_cn,
            fraction_line,
            denominator_cn
        ).arrange(DOWN, buff=0.15).next_to(tan_symbol, RIGHT, buff=0.3)
        
        self.play(Write(numerator_cn), run_time=0.5)
        self.play(Create(fraction_line), run_time=0.3)
        
        # 邻边高亮
        self.play(
            Flash(self.adj_line, color=self.COLOR_ADJACENT, flash_radius=0.5),
            run_time=0.5
        )
        
        self.play(Write(denominator_cn), run_time=0.5)
        
        # 数值计算
        numerical = MathTex(
            r"\tan A = \frac{" + f"{self.opposite:.1f}" + r"}{" + f"{self.adjacent:.1f}" + r"}",
            font_size=32,
            color=self.COLOR_FORMULA
        ).move_to(DOWN * 1.0)
        
        self.play(Write(numerical), run_time=0.8)
        
        equals = MathTex(r"\approx", font_size=32, color=WHITE).next_to(numerical, RIGHT, buff=0.3)
        result = DecimalNumber(
            self.tan_A,
            num_decimal_places=3,
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).next_to(equals, RIGHT, buff=0.3)
        
        self.play(Write(equals), Write(result), run_time=0.8)
        self.play(Flash(result, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.5)
        self.wait(0.8)
        
        # 关系式: tan A = sin A / cos A
        relation_title = Text(
            "重要关系:",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        relation = MathTex(
            r"\tan A = \frac{\sin A}{\cos A}",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).next_to(relation_title, DOWN, buff=0.3)
        
        self.play(FadeIn(relation_title), run_time=0.4)
        self.play(Write(relation), run_time=1.0)
        self.play(Flash(relation, color=self.COLOR_HIGHLIGHT, flash_radius=0.6), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(numerical),
            FadeOut(equals),
            FadeOut(result),
            FadeOut(fraction),
            FadeOut(relation_title),
            FadeOut(relation),
            run_time=0.5
        )
        
        # tan公式移到参考位置
        tan_ref = MathTex(
            r"\tan A = \frac{a}{b}",
            font_size=24,
            color=self.COLOR_FORMULA
        ).move_to(RIGHT * 3 + UP * 6.5)
        
        self.play(Transform(tan_symbol, tan_ref), run_time=0.5)
        self.remove(tan_symbol)
        self.add(tan_ref)
        
        self.tan_ref = tan_ref
    
    def show_invariance(self):
        """场景6: 三角比的不变性"""
        # 标题
        title = Text(
            "三角比只与角度有关!",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=1.0)
        
        # 移动并缩小当前三角形到左侧
        scale_small = 0.5
        pos_small = LEFT * 2.5 + UP * 1.5
        
        triangle_small = VGroup(
            self.colored_triangle,
            self.label_A,
            self.label_B,
            self.label_C,
            self.right_angle_mark,
            self.angle_A,
            self.angle_label,
            self.hyp_label,
            self.opp_label,
            self.adj_label
        )
        
        self.play(
            triangle_small.animate.scale(scale_small).move_to(pos_small),
            run_time=1.0
        )
        
        # 创建大三角形（相似）
        scale_large = 1.2
        pos_large = RIGHT * 2.0 + UP * 1.5
        
        # 计算大三角形的顶点
        C_large = self.C_base * scale_large
        B_large = self.B_base * scale_large
        A_large = self.A_base * scale_large
        
        # 应用位置偏移
        offset_large = pos_large
        C_large = C_large + offset_large
        B_large = B_large + offset_large
        A_large = A_large + offset_large
        
        # 创建大三角形的边
        hyp_large = Line(C_large, A_large, color=self.COLOR_HYPOTENUSE, stroke_width=6)
        opp_large = Line(B_large, A_large, color=self.COLOR_OPPOSITE, stroke_width=6)
        adj_large = Line(C_large, B_large, color=self.COLOR_ADJACENT, stroke_width=6)
        
        triangle_large = VGroup(hyp_large, opp_large, adj_large)
        
        self.play(Create(triangle_large), run_time=1.0)
        
        # 标注"角A相同"
        same_angle = Text(
            "∠A 相同",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_ANGLE
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(same_angle, scale=1.1), run_time=0.5)
        self.wait(0.5)
        
        # 对比表格
        table_bg = Rectangle(
            width=7,
            height=2.5,
            color=GRAY_B,
            stroke_width=2,
            fill_opacity=0.1
        ).move_to(DOWN * 1.5)
        
        self.play(Create(table_bg), run_time=0.5)
        
        # 表格内容
        header_small = Text("小三角形", font="PingFang SC", font_size=20, color=WHITE).move_to(LEFT * 2 + DOWN * 0.5)
        header_large = Text("大三角形", font="PingFang SC", font_size=20, color=WHITE).move_to(RIGHT * 2 + DOWN * 0.5)
        
        self.play(Write(header_small), Write(header_large), run_time=0.5)
        
        # sin值
        sin_small = MathTex(r"\sin A \approx", f"{self.sin_A:.3f}", font_size=22).move_to(LEFT * 2 + DOWN * 1.3)
        sin_large = MathTex(r"\sin A \approx", f"{self.sin_A:.3f}", font_size=22).move_to(RIGHT * 2 + DOWN * 1.3)
        sin_small[1].set_color(self.COLOR_HIGHLIGHT)
        sin_large[1].set_color(self.COLOR_HIGHLIGHT)
        
        self.play(Write(sin_small), Write(sin_large), run_time=0.8)
        
        equals_1 = MathTex(r"=", font_size=28, color=GREEN).move_to(DOWN * 1.3)
        self.play(Write(equals_1), Flash(equals_1, color=GREEN), run_time=0.5)
        
        # cos值
        cos_small = MathTex(r"\cos A \approx", f"{self.cos_A:.3f}", font_size=22).move_to(LEFT * 2 + DOWN * 2.0)
        cos_large = MathTex(r"\cos A \approx", f"{self.cos_A:.3f}", font_size=22).move_to(RIGHT * 2 + DOWN * 2.0)
        cos_small[1].set_color(self.COLOR_HIGHLIGHT)
        cos_large[1].set_color(self.COLOR_HIGHLIGHT)
        
        self.play(Write(cos_small), Write(cos_large), run_time=0.8)
        
        equals_2 = MathTex(r"=", font_size=28, color=GREEN).move_to(DOWN * 2.0)
        self.play(Write(equals_2), run_time=0.3)
        
        # tan值
        tan_small = MathTex(r"\tan A \approx", f"{self.tan_A:.3f}", font_size=22).move_to(LEFT * 2 + DOWN * 2.7)
        tan_large = MathTex(r"\tan A \approx", f"{self.tan_A:.3f}", font_size=22).move_to(RIGHT * 2 + DOWN * 2.7)
        tan_small[1].set_color(self.COLOR_HIGHLIGHT)
        tan_large[1].set_color(self.COLOR_HIGHLIGHT)
        
        self.play(Write(tan_small), Write(tan_large), run_time=0.8)
        
        equals_3 = MathTex(r"=", font_size=28, color=GREEN).move_to(DOWN * 2.7)
        self.play(Write(equals_3), run_time=0.3)
        
        # 结论
        conclusion = Text(
            "三角比的值与三角形大小无关!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(conclusion, scale=1.2), run_time=0.8)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(triangle_small),
            FadeOut(triangle_large),
            FadeOut(same_angle),
            FadeOut(table_bg),
            FadeOut(header_small),
            FadeOut(header_large),
            FadeOut(sin_small),
            FadeOut(sin_large),
            FadeOut(cos_small),
            FadeOut(cos_large),
            FadeOut(tan_small),
            FadeOut(tan_large),
            FadeOut(equals_1),
            FadeOut(equals_2),
            FadeOut(equals_3),
            FadeOut(conclusion),
            FadeOut(self.sin_ref),
            FadeOut(self.cos_ref),
            FadeOut(self.tan_ref),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 公式总结"""
        # 标题
        title = Text(
            "三角比公式总结",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 创建三个公式卡片
        card_1 = self.create_formula_card(
            r"\sin A = \frac{a}{c}",
            "对边/斜边",
            self.COLOR_OPPOSITE,
            UP * 3
        )
        
        card_2 = self.create_formula_card(
            r"\cos A = \frac{b}{c}",
            "邻边/斜边",
            self.COLOR_ADJACENT,
            UP * 1
        )
        
        card_3 = self.create_formula_card(
            r"\tan A = \frac{a}{b}",
            "对边/邻边",
            self.COLOR_FORMULA,
            DOWN * 1
        )
        
        # 卡片依次滑入
        self.play(card_1.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(0.3)
        self.play(card_2.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(0.3)
        self.play(card_3.animate.shift(RIGHT * 0), run_time=0.6)
        self.wait(1.0)
        
        # 记忆口诀
        mnemonic = Text(
            "记住: 只与角度有关，与大小无关!",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(FadeIn(mnemonic, shift=UP * 0.3), run_time=0.6)
        
        # 小三角形示意图
        mini_triangle = Polygon(
            ORIGIN,
            RIGHT * 0.8,
            RIGHT * 0.8 + UP * 0.6,
            color=WHITE,
            stroke_width=2
        ).move_to(DOWN * 5.5)
        
        self.play(Create(mini_triangle), run_time=0.5)
        
        # 标注a, b, c
        a_label = MathTex("a", font_size=18, color=self.COLOR_OPPOSITE).next_to(
            Line(mini_triangle.get_vertices()[1], mini_triangle.get_vertices()[2]),
            RIGHT,
            buff=0.05
        )
        b_label = MathTex("b", font_size=18, color=self.COLOR_ADJACENT).next_to(
            Line(mini_triangle.get_vertices()[0], mini_triangle.get_vertices()[1]),
            DOWN,
            buff=0.05
        )
        c_label = MathTex("c", font_size=18, color=self.COLOR_HYPOTENUSE).next_to(
            Line(mini_triangle.get_vertices()[0], mini_triangle.get_vertices()[2]),
            LEFT,
            buff=0.05
        )
        
        self.play(
            Write(a_label),
            Write(b_label),
            Write(c_label),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(card_1),
            FadeOut(card_2),
            FadeOut(card_3),
            FadeOut(mnemonic),
            FadeOut(mini_triangle),
            FadeOut(a_label),
            FadeOut(b_label),
            FadeOut(c_label),
            run_time=0.6
        )
    
    def create_formula_card(self, formula, description, color, position):
        """创建公式卡片"""
        # 图标圆
        icon = Circle(radius=0.25, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 公式
        formula_tex = MathTex(formula, font_size=28, color=WHITE)
        
        # 描述
        desc_text = Text(
            description,
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, formula_tex, desc_text).arrange(RIGHT, buff=0.4)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def show_outro(self):
        """场景8: 片尾关注"""
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰三角形
        triangles = VGroup(*[
            Polygon(
                ORIGIN,
                RIGHT * 0.3,
                UP * 0.3,
                color=self.COLOR_FORMULA,
                fill_opacity=0.8
            )
            .scale(0.5)
            .move_to(follow_text.get_center() + 2 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.6
        )
        self.play(Rotate(triangles, angle=PI, run_time=1.5))
        
        # 公式图标
        icon_size = 0.3
        icons = VGroup(
            Circle(radius=icon_size, color=self.COLOR_OPPOSITE, fill_opacity=0.8).shift(LEFT * 1.5),
            Circle(radius=icon_size, color=self.COLOR_ADJACENT, fill_opacity=0.8),
            Circle(radius=icon_size, color=self.COLOR_HYPOTENUSE, fill_opacity=0.8).shift(RIGHT * 1.5)
        ).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.wait(1.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            FadeOut(icons),
            run_time=1.0
        )


# 运行命令:
# manim -pql trigonometric_ratios.py TrigonometricRatios  # 快速预览
# manim -qh trigonometric_ratios.py TrigonometricRatios   # 高质量渲染