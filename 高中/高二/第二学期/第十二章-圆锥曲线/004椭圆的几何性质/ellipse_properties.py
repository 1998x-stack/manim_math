"""
椭圆的几何性质动画 - Ellipse Geometric Properties Animation
使用 Manim 创建的高中几何教学视频

内容: 离心率、准线、通径、焦半径、对称性
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


class EllipseProperties(Scene):
    """
    椭圆几何性质教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 范围与对称性
    3. 离心率概念
    4. 离心率的影响
    5. 准线的定义
    6. 焦半径公式
    7. 通径
    8. 性质总结
    9. 片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#e74c3c"      # 红色 - 椭圆
        self.COLOR_FOCUS = "#f39c12"        # 橙色 - 焦点
        self.COLOR_DIRECTRIX = "#9b59b6"    # 紫色 - 准线
        self.COLOR_LATUS = "#16a085"        # 青绿 - 通径
        self.COLOR_HIGHLIGHT = YELLOW        # 高亮色
        self.COLOR_AUXILIARY = GRAY_B        # 辅助线
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_range_symmetry()
        self.show_eccentricity_concept()
        self.show_eccentricity_effect()
        self.show_directrix()
        self.show_focal_radius()
        self.show_latus_rectum()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化椭圆和所有几何元素"""
        # 椭圆参数
        self.a = 3.0  # 长半轴
        self.b = 2.0  # 短半轴
        self.c = np.sqrt(self.a**2 - self.b**2)  # 半焦距
        self.e = self.c / self.a  # 离心率
        
        # 准线位置
        self.directrix_x = self.a**2 / self.c
        
        # 通径长度
        self.latus_length = 2 * self.b**2 / self.a
        
        # 缩放因子
        self.SCALE = 0.65
        self.OFFSET = UP * 1.0
        
        # 坐标系配置
        self.axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            x_length=8 * self.SCALE,
            y_length=5 * self.SCALE,
            axis_config={
                "include_numbers": False,
                "stroke_color": GRAY_B,
                "stroke_width": 2
            }
        ).move_to(self.OFFSET)
        
        # 坐标轴标签
        self.x_label = MathTex("x", font_size=24, color=GRAY_A).next_to(
            self.axes.x_axis.get_end(), RIGHT, buff=0.1
        )
        self.y_label = MathTex("y", font_size=24, color=GRAY_A).next_to(
            self.axes.y_axis.get_end(), UP, buff=0.1
        )
        
        # 焦点位置
        self.F1 = self.axes.c2p(-self.c, 0)
        self.F2 = self.axes.c2p(self.c, 0)
        
        # 顶点位置
        self.A1 = self.axes.c2p(-self.a, 0)
        self.A2 = self.axes.c2p(self.a, 0)
        self.B1 = self.axes.c2p(0, -self.b)
        self.B2 = self.axes.c2p(0, self.b)
        
        # 验证几何关系
        self.verify_geometry()
        
        print("✓ 几何数据初始化完成")
        print(f"  a = {self.a}, b = {self.b}, c = {self.c:.4f}")
        print(f"  e = {self.e:.4f}")
        print(f"  准线 x = ±{self.directrix_x:.4f}")
        print(f"  通径 = {self.latus_length:.4f}")
    
    def verify_geometry(self):
        """验证几何关系"""
        epsilon = 1e-6
        
        # 验证 a² = b² + c²
        if abs(self.a**2 - (self.b**2 + self.c**2)) > epsilon:
            raise ValueError("关系错误: a² ≠ b² + c²")
        
        # 验证离心率范围
        if not (0 < self.e < 1):
            raise ValueError(f"离心率错误: e = {self.e} 不在 (0, 1) 范围内")
        
        print("✓ 几何关系验证通过")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook = Text(
            "椭圆有哪些神奇的性质？",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook), run_time=1.0)
        
        # 创建坐标系和椭圆
        axes_group = VGroup(self.axes, self.x_label, self.y_label)
        self.play(Create(axes_group), run_time=0.8)
        
        self.ellipse = Ellipse(
            width=2 * self.a * self.axes.x_axis.unit_size,
            height=2 * self.b * self.axes.y_axis.unit_size,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.axes.c2p(0, 0))
        
        self.play(Create(self.ellipse), run_time=1.5)
        self.wait(0.5)
        
        # 清理钩子
        self.play(FadeOut(hook), run_time=0.4)
    
    def show_range_symmetry(self):
        """场景2: 范围与对称性"""
        # 标题
        title = Text(
            "范围与对称性",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 边界矩形
        boundary_rect = Rectangle(
            width=2 * self.a * self.axes.x_axis.unit_size,
            height=2 * self.b * self.axes.y_axis.unit_size,
            color=self.COLOR_AUXILIARY,
            stroke_width=2
        ).move_to(self.axes.c2p(0, 0))
        
        self.play(Create(boundary_rect), run_time=1.0)
        
        # 范围标注
        range_x = MathTex(
            r"-a \leq x \leq a",
            font_size=22,
            color=WHITE
        ).move_to(DOWN * 4)
        
        range_y = MathTex(
            r"-b \leq y \leq b",
            font_size=22,
            color=WHITE
        ).next_to(range_x, DOWN, buff=0.2)
        
        self.play(FadeIn(range_x), FadeIn(range_y), run_time=0.8)
        
        # 对称性演示 - 创建测试点
        test_point = Dot(self.axes.c2p(2, 1.3), color=YELLOW, radius=0.06)
        self.play(FadeIn(test_point, scale=0.5), run_time=0.5)
        
        # x轴对称
        mirror_x = Dot(self.axes.c2p(2, -1.3), color=YELLOW, radius=0.06)
        self.play(FadeIn(mirror_x), run_time=0.5)
        self.wait(0.5)
        
        # y轴对称
        mirror_y = Dot(self.axes.c2p(-2, 1.3), color=YELLOW, radius=0.06)
        self.play(FadeIn(mirror_y), run_time=0.5)
        
        # 原点对称
        mirror_o = Dot(self.axes.c2p(-2, -1.3), color=YELLOW, radius=0.06)
        self.play(FadeIn(mirror_o), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(boundary_rect),
            FadeOut(range_x),
            FadeOut(range_y),
            FadeOut(test_point),
            FadeOut(mirror_x),
            FadeOut(mirror_y),
            FadeOut(mirror_o),
            run_time=0.6
        )
    
    def show_eccentricity_concept(self):
        """场景3: 离心率概念"""
        # 标题
        title = Text(
            "离心率",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 公式
        formula = MathTex(
            r"e = \frac{c}{a}",
            font_size=32,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(formula), run_time=1.0)
        
        # 焦点标记
        f1_dot = Dot(self.F1, color=self.COLOR_FOCUS, radius=0.08)
        f2_dot = Dot(self.F2, color=self.COLOR_FOCUS, radius=0.08)
        
        f1_label = MathTex("F_1", font_size=20, color=self.COLOR_FOCUS).next_to(
            f1_dot, DOWN, buff=0.1
        )
        f2_label = MathTex("F_2", font_size=20, color=self.COLOR_FOCUS).next_to(
            f2_dot, DOWN, buff=0.1
        )
        
        self.play(
            FadeIn(f1_dot, scale=0.5),
            FadeIn(f1_label),
            FadeIn(f2_dot, scale=0.5),
            FadeIn(f2_label),
            run_time=1.2
        )
        
        # c 标注
        c_line = Line(self.F1, self.F2, color=self.COLOR_FOCUS, stroke_width=3)
        c_brace = Brace(c_line, direction=DOWN, buff=0.3, color=self.COLOR_FOCUS)
        c_label = MathTex("2c", font_size=22, color=self.COLOR_FOCUS).next_to(
            c_brace, DOWN, buff=0.05
        )
        
        self.play(Create(c_line), FadeIn(c_brace), FadeIn(c_label), run_time=1.0)
        
        # a 标注
        a_line = Line(self.axes.c2p(0, 0), self.A2, color=self.COLOR_PRIMARY, stroke_width=3)
        a_label = MathTex("a", font_size=22, color=self.COLOR_PRIMARY).next_to(
            a_line.get_center(), UP, buff=0.1
        )
        
        self.play(Create(a_line), FadeIn(a_label), run_time=0.8)
        
        # e 值计算
        e_value = MathTex(
            f"e = \\frac{{{self.c:.3f}}}{{{self.a}}} \\approx {self.e:.3f}",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        
        self.play(Write(e_value), run_time=1.2)
        
        # 范围说明
        range_text = MathTex(
            r"0 < e < 1",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(range_text), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(c_line),
            FadeOut(c_brace),
            FadeOut(c_label),
            FadeOut(a_line),
            FadeOut(a_label),
            FadeOut(e_value),
            FadeOut(range_text),
            run_time=0.6
        )
        
        # 保存焦点
        self.f1_dot = f1_dot
        self.f1_label = f1_label
        self.f2_dot = f2_dot
        self.f2_label = f2_label
    
    def show_eccentricity_effect(self):
        """场景4: 离心率的影响"""
        # 标题
        title = Text(
            "离心率的影响",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 原始椭圆淡化
        self.play(self.ellipse.animate.set_stroke(opacity=0.3), run_time=0.4)
        
        # e → 1 (椭圆变扁)
        text_flat = Text(
            "e 接近 1，椭圆越扁",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        # 创建扁椭圆
        flat_ellipse = Ellipse(
            width=2 * self.a * self.axes.x_axis.unit_size,
            height=2 * 0.7 * self.axes.y_axis.unit_size,  # b变小
            color=YELLOW,
            stroke_width=3
        ).move_to(self.axes.c2p(0, 0))
        
        self.play(Create(flat_ellipse), FadeIn(text_flat), run_time=1.5)
        self.wait(1.0)
        
        # 恢复
        self.play(FadeOut(flat_ellipse), FadeOut(text_flat), run_time=0.5)
        
        # e → 0 (椭圆变圆)
        text_round = Text(
            "e 接近 0，椭圆越圆",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        # 创建圆椭圆
        round_ellipse = Ellipse(
            width=2 * self.a * self.axes.x_axis.unit_size,
            height=2 * 2.8 * self.axes.y_axis.unit_size,  # b接近a
            color=YELLOW,
            stroke_width=3
        ).move_to(self.axes.c2p(0, 0))
        
        self.play(Create(round_ellipse), FadeIn(text_round), run_time=1.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(round_ellipse),
            FadeOut(text_round),
            FadeOut(title),
            run_time=0.5
        )
        
        # 恢复原椭圆
        self.play(self.ellipse.animate.set_stroke(opacity=1.0), run_time=0.3)
        
        # 极限说明
        limit_text = Text(
            "e=0时为圆，e=1时退化为线段",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(limit_text, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(limit_text), run_time=0.4)
    
    def show_directrix(self):
        """场景5: 准线的定义"""
        # 标题
        title = Text(
            "准线",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_DIRECTRIX
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 公式
        formula = MathTex(
            r"x = \pm \frac{a^2}{c}",
            font_size=30,
            color=WHITE
        ).move_to(UP * 4.7)
        
        self.play(Write(formula), run_time=1.0)
        
        # 右准线
        directrix_right = DashedLine(
            self.axes.c2p(self.directrix_x, -4),
            self.axes.c2p(self.directrix_x, 4),
            color=self.COLOR_DIRECTRIX,
            stroke_width=3,
            dash_length=0.1
        )
        
        # 左准线
        directrix_left = DashedLine(
            self.axes.c2p(-self.directrix_x, -4),
            self.axes.c2p(-self.directrix_x, 4),
            color=self.COLOR_DIRECTRIX,
            stroke_width=3,
            dash_length=0.1
        )
        
        self.play(Create(directrix_right), run_time=0.7)
        self.play(Create(directrix_left), run_time=0.7)
        
        # 准线标注
        d_label_r = MathTex(
            r"x = \frac{a^2}{c}",
            font_size=20,
            color=self.COLOR_DIRECTRIX
        ).next_to(directrix_right, UP, buff=0.1)
        
        d_label_l = MathTex(
            r"x = -\frac{a^2}{c}",
            font_size=20,
            color=self.COLOR_DIRECTRIX
        ).next_to(directrix_left, UP, buff=0.1)
        
        self.play(FadeIn(d_label_r), FadeIn(d_label_l), run_time=0.8)
        
        # 数值计算
        calculation = MathTex(
            f"\\frac{{{self.a**2}}}{{{self.c:.3f}}} \\approx {self.directrix_x:.2f}",
            font_size=24,
            color=YELLOW
        ).move_to(DOWN * 4)
        
        self.play(Write(calculation), run_time=1.0)
        
        # 焦点到准线距离标注
        distance_line = DashedLine(
            self.F2,
            self.axes.c2p(self.directrix_x, 0),
            color=self.COLOR_AUXILIARY,
            stroke_width=2,
            dash_length=0.08
        )
        
        self.play(Create(distance_line), run_time=0.8)
        
        distance_value = self.directrix_x - self.c
        distance_label = MathTex(
            f"{distance_value:.2f}",
            font_size=20,
            color=YELLOW
        ).next_to(distance_line.get_center(), DOWN, buff=0.1)
        
        self.play(FadeIn(distance_label), run_time=0.6)
        
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(d_label_r),
            FadeOut(d_label_l),
            FadeOut(calculation),
            FadeOut(distance_line),
            FadeOut(distance_label),
            run_time=0.6
        )
        
        # 保存准线
        self.directrix_right = directrix_right
        self.directrix_left = directrix_left
    
    def show_focal_radius(self):
        """场景6: 焦半径公式"""
        # 标题
        title = Text(
            "焦半径",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 椭圆上一点P (取第一象限)
        t = np.pi / 4
        x_p = self.a * np.cos(t)
        y_p = self.b * np.sin(t)
        point_P = Dot(self.axes.c2p(x_p, y_p), color=YELLOW, radius=0.08)
        p_label = Text("P", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(
            point_P, UP + RIGHT, buff=0.1
        )
        
        self.play(FadeIn(point_P, scale=0.5), FadeIn(p_label), run_time=0.6)
        
        # 连线 PF1, PF2
        line_pf1 = Line(point_P.get_center(), self.F1, color=self.COLOR_AUXILIARY, stroke_width=2)
        line_pf2 = Line(point_P.get_center(), self.F2, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        self.play(Create(line_pf1), run_time=0.6)
        self.play(Create(line_pf2), run_time=0.6)
        
        # 公式1
        formula1 = MathTex(
            r"|PF_1| = a + ex_0",
            font_size=26,
            color=WHITE
        ).move_to(UP * 3.8)
        
        self.play(Write(formula1), run_time=1.0)
        
        # 公式2
        formula2 = MathTex(
            r"|PF_2| = a - ex_0",
            font_size=26,
            color=WHITE
        ).move_to(UP * 3.2)
        
        self.play(Write(formula2), run_time=1.0)
        
        # x0标注
        x0_line = DashedLine(
            self.axes.c2p(x_p, 0),
            point_P.get_center(),
            color=GRAY_A,
            stroke_width=1.5,
            dash_length=0.06
        )
        
        x0_label = MathTex(
            "x_0",
            font_size=20,
            color=GRAY_A
        ).next_to(self.axes.c2p(x_p, 0), DOWN, buff=0.1)
        
        self.play(Create(x0_line), FadeIn(x0_label), run_time=0.8)
        
        # 数值验证
        r1 = self.a + self.e * x_p
        r2 = self.a - self.e * x_p
        
        verification = Text(
            f"|PF₁|+|PF₂| = {r1:.2f}+{r2:.2f} = {r1+r2:.2f} = 2a",
            font="Noto Sans CJK SC",
            font_size=20,
            color=YELLOW
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(verification, shift=UP * 0.2), run_time=1.0)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(point_P),
            FadeOut(p_label),
            FadeOut(line_pf1),
            FadeOut(line_pf2),
            FadeOut(formula1),
            FadeOut(formula2),
            FadeOut(x0_line),
            FadeOut(x0_label),
            FadeOut(verification),
            run_time=0.6
        )
    
    def show_latus_rectum(self):
        """场景7: 通径"""
        # 标题
        title = Text(
            "通径",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_LATUS
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 定义文字
        definition = Text(
            "过焦点垂直于长轴的弦",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(FadeIn(definition), run_time=0.9)
        
        # 计算通径端点
        # 过右焦点F2(c, 0)，垂直于x轴，代入椭圆方程
        # c²/a² + y²/b² = 1
        # y² = b²(1 - c²/a²) = b²(a² - c²)/a² = b⁴/a²
        # y = ±b²/a
        y_latus = self.b**2 / self.a
        
        p1 = self.axes.c2p(self.c, y_latus)
        p2 = self.axes.c2p(self.c, -y_latus)
        
        # 通径
        latus_rectum = Line(p1, p2, color=self.COLOR_LATUS, stroke_width=4)
        
        self.play(Create(latus_rectum), run_time=1.0)
        
        # 端点标注
        p1_dot = Dot(p1, color=self.COLOR_LATUS, radius=0.06)
        p2_dot = Dot(p2, color=self.COLOR_LATUS, radius=0.06)
        
        self.play(FadeIn(p1_dot), FadeIn(p2_dot), run_time=0.5)
        
        # 公式
        formula = MathTex(
            r"\text{长度} = \frac{2b^2}{a}",
            font_size=28,
            color=WHITE,
            tex_template=TexTemplateLibrary.ctex
        ).move_to(UP * 3.5)
        
        self.play(Write(formula), run_time=1.5)
        
        # 数值计算
        calculation = MathTex(
            f"= \\frac{{2 \\times {self.b**2}}}{{{self.a}}} \\approx {self.latus_length:.2f}",
            font_size=24,
            color=YELLOW
        ).move_to(DOWN * 4)
        
        self.play(Write(calculation), run_time=1.0)
        
        # 长度标注
        brace = Brace(latus_rectum, direction=RIGHT, buff=0.1, color=self.COLOR_LATUS)
        brace_label = MathTex(
            f"{self.latus_length:.2f}",
            font_size=20,
            color=self.COLOR_LATUS
        ).next_to(brace, RIGHT, buff=0.05)
        
        self.play(FadeIn(brace), FadeIn(brace_label), run_time=1.0)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(latus_rectum),
            FadeOut(p1_dot),
            FadeOut(p2_dot),
            FadeOut(formula),
            FadeOut(calculation),
            FadeOut(brace),
            FadeOut(brace_label),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景8: 性质总结"""
        # 清空场景
        self.play(
            FadeOut(self.ellipse),
            FadeOut(self.f1_dot),
            FadeOut(self.f1_label),
            FadeOut(self.f2_dot),
            FadeOut(self.f2_label),
            FadeOut(self.directrix_right),
            FadeOut(self.directrix_left),
            FadeOut(self.axes),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            run_time=0.5
        )
        
        # 总结标题
        summary_title = Text(
            "椭圆的几何性质",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 2.5)
        
        self.play(Write(summary_title), run_time=0.5)
        
        # 5个性质卡片
        card1 = self.create_property_card(
            "对称性",
            "关于x轴、y轴、原点对称",
            self.COLOR_PRIMARY,
            UP * 1.2
        )
        
        card2 = self.create_property_card(
            "离心率",
            "e = c/a (0 < e < 1)",
            self.COLOR_FOCUS,
            UP * 0.3
        )
        
        card3 = self.create_property_card(
            "准线",
            "x = ±a²/c",
            self.COLOR_DIRECTRIX,
            DOWN * 0.6
        )
        
        card4 = self.create_property_card(
            "通径",
            "长度 = 2b²/a",
            self.COLOR_LATUS,
            DOWN * 1.5
        )
        
        card5 = self.create_property_card(
            "焦半径",
            "|PF₁|=a+ex₀, |PF₂|=a-ex₀",
            YELLOW,
            DOWN * 2.4
        )
        
        cards = VGroup(card1, card2, card3, card4, card5)
        
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.5)
            if i < len(cards) - 1:
                self.wait(0.3)
        
        self.wait(4.0)
        
        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            run_time=0.5
        )
    
    def create_property_card(self, title, content, color, position):
        """创建性质卡片"""
        # 图标
        icon = Ellipse(
            width=0.4,
            height=0.25,
            fill_color=color,
            fill_opacity=0.8,
            stroke_width=0
        )
        
        # 标题
        title_text = Text(
            title,
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card
    
    def show_outro(self):
        """场景9: 片尾"""
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 掌握更多数学知识!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰椭圆
        ellipses = VGroup(*[
            Ellipse(
                width=0.6,
                height=0.4,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.5,
                stroke_width=2
            ).move_to(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(ellipse, scale=0.5) for ellipse in ellipses],
            run_time=0.8,
            lag_ratio=0.1
        )
        
        self.play(Rotate(ellipses, angle=PI, run_time=1.5))
        self.wait(0.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(ellipses),
            run_time=1.0
        )


# 运行命令:
# manim -pql ellipse_properties.py EllipseProperties  # 快速预览
# manim -qh ellipse_properties.py EllipseProperties   # 高质量渲染