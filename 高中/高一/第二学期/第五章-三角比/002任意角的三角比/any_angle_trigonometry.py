"""
任意角的三角比教学动画 - Trigonometric Ratios of Any Angle
使用 Manim 创建的高中三角函数教学视频

内容: 单位圆上任意角的三角函数定义，各象限符号规律
目标观众: 高一学生 (第二学期)
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


class AnyAngleTrigonometry(Scene):
    """
    任意角三角比教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 单位圆与坐标定义
    3. 第一象限 - 锐角回顾
    4. 第二象限 - 钝角扩展
    5. 第三象限
    6. 第四象限
    7. 象限符号口诀
    8. 旋转演示动画
    9. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_Q1 = "#3498db"        # 蓝色 - 第一象限
        self.COLOR_Q2 = "#e74c3c"        # 红色 - 第二象限
        self.COLOR_Q3 = "#9b59b6"        # 紫色 - 第三象限
        self.COLOR_Q4 = "#2ecc71"        # 绿色 - 第四象限
        self.COLOR_HIGHLIGHT = YELLOW    # 黄色 - 强调
        self.COLOR_POSITIVE = "#2ecc71"  # 绿色 - 正值
        self.COLOR_NEGATIVE = "#e74c3c"  # 红色 - 负值
        self.COLOR_CIRCLE = WHITE        # 白色 - 单位圆
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_unit_circle_definition()
        self.show_quadrant_1()
        self.show_quadrant_2()
        self.show_quadrant_3()
        self.show_quadrant_4()
        self.show_sign_rule_mnemonic()
        self.show_rotation_demo()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有几何元素的精确坐标"""
        # 基准参数
        self.OFFSET = UP * 1.5
        self.RADIUS = 2.0
        
        # 单位圆圆心
        self.center = self.OFFSET
        
        # 四个象限的示例角度
        self.angle_Q1 = PI / 6        # 30度
        self.angle_Q2 = 5 * PI / 6    # 150度
        self.angle_Q3 = 7 * PI / 6    # 210度
        self.angle_Q4 = 11 * PI / 6   # 330度
        
        # 计算各象限的点
        self.P_Q1 = self.center + self.RADIUS * np.array([
            np.cos(self.angle_Q1),
            np.sin(self.angle_Q1),
            0
        ])
        
        self.P_Q2 = self.center + self.RADIUS * np.array([
            np.cos(self.angle_Q2),
            np.sin(self.angle_Q2),
            0
        ])
        
        self.P_Q3 = self.center + self.RADIUS * np.array([
            np.cos(self.angle_Q3),
            np.sin(self.angle_Q3),
            0
        ])
        
        self.P_Q4 = self.center + self.RADIUS * np.array([
            np.cos(self.angle_Q4),
            np.sin(self.angle_Q4),
            0
        ])
        
        # 验证几何
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证点在圆上
        points = [self.P_Q1, self.P_Q2, self.P_Q3, self.P_Q4]
        for i, point in enumerate(points, 1):
            dist = np.linalg.norm(point - self.center)
            assert abs(dist - self.RADIUS) < epsilon, f"点Q{i}不在圆上: {dist}"
        
        print("✓ 几何验证通过")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_line1 = Text(
            "锐角的 sin、cos、tan 你会算",
            font="PingFang SC",
            font_size=34,
            color=WHITE
        ).move_to(UP * 2.5)
        
        hook_line2 = Text(
            "那钝角、负角呢?",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.2)
        
        self.play(Write(hook_line1), run_time=1.0)
        self.wait(0.5)
        self.play(Write(hook_line2), run_time=1.0)
        
        # 展示不同角度的例子
        angles_group = VGroup()
        
        angle_120 = MathTex(r"120^\circ", font_size=36, color=self.COLOR_Q2).move_to(ORIGIN + LEFT * 2)
        angle_neg30 = MathTex(r"-30^\circ", font_size=36, color=self.COLOR_Q4).move_to(ORIGIN + RIGHT * 2)
        angle_225 = MathTex(r"225^\circ", font_size=36, color=self.COLOR_Q3).move_to(DOWN * 1.2)
        
        angles_group = VGroup(angle_120, angle_neg30, angle_225)
        
        self.play(FadeIn(angles_group, scale=0.8), run_time=0.8)
        self.play(
            Indicate(angle_120, color=self.COLOR_Q2),
            Indicate(angle_neg30, color=self.COLOR_Q4),
            Indicate(angle_225, color=self.COLOR_Q3),
            run_time=1.0,
            lag_ratio=0.3
        )
        
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(angles_group),
            run_time=0.5
        )
    
    def show_unit_circle_definition(self):
        """场景2: 单位圆与坐标定义"""
        # 标题
        title = Text(
            "单位圆上的三角函数",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 坐标轴
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=5,
            y_length=5,
            axis_config={
                "color": GRAY_B,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
                "include_numbers": False
            }
        ).move_to(self.center)
        
        # 坐标轴标签
        x_label = MathTex("x", font_size=24, color=GRAY_A).next_to(
            axes.x_axis.get_end(), DOWN, buff=0.2
        )
        y_label = MathTex("y", font_size=24, color=GRAY_A).next_to(
            axes.y_axis.get_end(), LEFT, buff=0.2
        )
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1.2)
        
        # 单位圆
        circle = Circle(
            radius=self.RADIUS,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.center)
        
        circle_label = Text(
            "单位圆",
            font="PingFang SC",
            font_size=22,
            color=WHITE
        ).next_to(circle, UR, buff=0.1)
        
        self.play(Create(circle), run_time=1.5)
        self.play(FadeIn(circle_label, shift=DOWN * 0.2), run_time=0.5)
        
        self.wait(0.8)
        
        # 定义说明
        definition = Text(
            "设角α的终边与单位圆交于点 P(x, y)",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(definition, shift=UP * 0.3), run_time=0.8)
        
        # 三角函数定义
        formulas = VGroup(
            MathTex(r"\sin\alpha = y", font_size=30, color=WHITE),
            MathTex(r"\cos\alpha = x", font_size=30, color=WHITE),
            MathTex(r"\tan\alpha = \frac{y}{x}", font_size=30, color=WHITE)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to(DOWN * 6)
        
        for formula in formulas:
            self.play(Write(formula), run_time=0.8)
            self.wait(0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(circle_label),
            FadeOut(definition),
            FadeOut(formulas),
            run_time=0.5
        )
        
        # 保存元素
        self.axes = axes
        self.x_label = x_label
        self.y_label = y_label
        self.circle = circle
    
    def show_quadrant_1(self):
        """场景3: 第一象限 - 锐角回顾"""
        # 标题
        title = Text(
            "第一象限 (0° < α < 90°)",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_Q1
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 象限标识
        quadrant_bg = Polygon(
            self.center,
            self.center + RIGHT * 2.5,
            self.center + RIGHT * 2.5 + UP * 2.5,
            self.center + UP * 2.5,
            fill_color=self.COLOR_Q1,
            fill_opacity=0.15,
            stroke_width=0
        )
        
        self.play(FadeIn(quadrant_bg), run_time=0.5)
        
        # 角度和点
        angle_arc = Arc(
            radius=0.6,
            start_angle=0,
            angle=self.angle_Q1,
            arc_center=self.center,
            color=self.COLOR_Q1,
            stroke_width=3
        )
        
        angle_label = MathTex(r"\alpha", font_size=24, color=self.COLOR_Q1).move_to(
            self.center + np.array([0.8, 0.25, 0])
        )
        
        self.play(Create(angle_arc), Write(angle_label), run_time=0.8)
        
        # 终边
        terminal_line = Line(
            self.center,
            self.P_Q1,
            color=self.COLOR_Q1,
            stroke_width=3
        )
        
        self.play(Create(terminal_line), run_time=0.6)
        
        # 点P
        dot_P = Dot(self.P_Q1, color=self.COLOR_Q1, radius=0.1)
        label_P = MathTex(r"P(x, y)", font_size=24, color=WHITE).next_to(dot_P, UR, buff=0.15)
        
        self.play(FadeIn(dot_P, scale=0.5), Write(label_P), run_time=0.5)
        
        # 投影线
        x_proj_point = self.center + np.array([self.P_Q1[0] - self.center[0], 0, 0])
        y_proj_point = self.center + np.array([0, self.P_Q1[1] - self.center[1], 0])
        
        proj_x = DashedLine(
            self.P_Q1,
            x_proj_point,
            color=self.COLOR_CIRCLE,  # Fixed: COLOR_AUXILIARY was not defined
            dash_length=0.08
        )
        
        proj_y = DashedLine(
            self.P_Q1,
            y_proj_point,
            color=self.COLOR_CIRCLE,  # Fixed: COLOR_AUXILIARY was not defined
            dash_length=0.08
        )
        
        self.play(Create(proj_x), Create(proj_y), run_time=0.8)
        
        # 坐标值标注
        x_value = np.cos(self.angle_Q1)
        y_value = np.sin(self.angle_Q1)
        
        # 替换Brace为简单的线条和括号
        x_brace_start = x_proj_point
        x_brace_end = self.center
        x_brace = VGroup(
            Line(x_brace_start + DOWN*0.1, x_brace_start + DOWN*0.2),  # 小竖线
            Line(x_brace_start + DOWN*0.2, x_brace_end + DOWN*0.2),   # 横线
            Line(x_brace_end + DOWN*0.2, x_brace_end + DOWN*0.1),   # 右竖线
        ).set_color(self.COLOR_Q1)
        
        y_brace_start = self.P_Q1
        y_brace_end = y_proj_point
        y_brace = VGroup(
            Line(y_brace_start + RIGHT*0.1, y_brace_start + RIGHT*0.2),  # 小竖线
            Line(y_brace_start + RIGHT*0.2, y_brace_end + RIGHT*0.2), # 横线
            Line(y_brace_end + RIGHT*0.2, y_brace_end + RIGHT*0.1),   # 右竖线
        ).set_color(self.COLOR_Q1)
        
        x_label_val = MathTex(f"x > 0", font_size=22, color=self.COLOR_POSITIVE).next_to(x_brace, DOWN, buff=0.1)
        y_label_val = MathTex(f"y > 0", font_size=22, color=self.COLOR_POSITIVE).next_to(y_brace, RIGHT, buff=0.1)
        
        self.play(
            FadeIn(x_brace), Write(x_label_val),
            FadeIn(y_brace), Write(y_label_val),
            run_time=1.0
        )
        
        # 结论
        conclusion = VGroup(
            Text("x > 0, y > 0", font="PingFang SC", font_size=26, color=self.COLOR_POSITIVE),
            MathTex(r"\sin\alpha > 0,\ \cos\alpha > 0,\ \tan\alpha > 0", font_size=26, color=self.COLOR_POSITIVE)
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 5.5)
        
        conclusion[0].set_color(WHITE)
        conclusion[1][0:5].set_color(self.COLOR_POSITIVE)  # sin α > 0
        conclusion[1][6:11].set_color(self.COLOR_POSITIVE)  # cos α > 0
        conclusion[1][12:17].set_color(self.COLOR_POSITIVE)  # tan α > 0
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=1.0)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(quadrant_bg),
            FadeOut(angle_arc),
            FadeOut(angle_label),
            FadeOut(terminal_line),
            FadeOut(dot_P),
            FadeOut(label_P),
            FadeOut(proj_x),
            FadeOut(proj_y),
            FadeOut(x_brace),
            FadeOut(x_label_val),
            FadeOut(y_brace),
            FadeOut(y_label_val),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_quadrant_2(self):
        """场景4: 第二象限"""
        # 标题
        title = Text(
            "第二象限 (90° < α < 180°)",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_Q2
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 象限背景
        quadrant_bg = Polygon(
            self.center,
            self.center + LEFT * 2.5,
            self.center + LEFT * 2.5 + UP * 2.5,
            self.center + UP * 2.5,
            fill_color=self.COLOR_Q2,
            fill_opacity=0.15,
            stroke_width=0
        )
        
        self.play(FadeIn(quadrant_bg), run_time=0.5)
        
        # 角度
        angle_arc = Arc(
            radius=0.6,
            start_angle=0,
            angle=self.angle_Q2,
            arc_center=self.center,
            color=self.COLOR_Q2,
            stroke_width=3
        )
        
        angle_label = MathTex(r"\alpha", font_size=24, color=self.COLOR_Q2).move_to(
            self.center + np.array([-0.8, 0.25, 0])
        )
        
        self.play(Create(angle_arc), Write(angle_label), run_time=0.8)
        
        # 终边和点
        terminal_line = Line(self.center, self.P_Q2, color=self.COLOR_Q2, stroke_width=3)
        dot_P = Dot(self.P_Q2, color=self.COLOR_Q2, radius=0.1)
        label_P = MathTex(r"P(x, y)", font_size=24, color=WHITE).next_to(dot_P, UL, buff=0.15)
        
        self.play(Create(terminal_line), run_time=0.6)
        self.play(FadeIn(dot_P, scale=0.5), Write(label_P), run_time=0.5)
        
        # 投影
        x_proj_point = self.center + np.array([self.P_Q2[0] - self.center[0], 0, 0])
        
        proj_x = DashedLine(self.P_Q2, x_proj_point, color=self.COLOR_CIRCLE, dash_length=0.08)
        proj_y = DashedLine(
            self.P_Q2,
            self.center + np.array([0, self.P_Q2[1] - self.center[1], 0]),
            color=self.COLOR_CIRCLE,
            dash_length=0.08
        )
        
        self.play(Create(proj_x), Create(proj_y), run_time=0.8)
        
        # 符号标注
        x_label = MathTex("x < 0", font_size=24, color=self.COLOR_NEGATIVE).next_to(
            x_proj_point, DOWN, buff=0.3
        )
        y_label = MathTex("y > 0", font_size=24, color=self.COLOR_POSITIVE).next_to(
            self.center + np.array([0, self.P_Q2[1] - self.center[1], 0]),
            LEFT, buff=0.3
        )
        
        self.play(Write(x_label), Write(y_label), run_time=0.8)
        
        # 结论
        conclusion = VGroup(
            Text("x < 0, y > 0", font="PingFang SC", font_size=26, color=WHITE),
            MathTex(
                r"\sin\alpha ", r"> 0,\ ",
                r"\cos\alpha ", r"< 0,\ ",
                r"\tan\alpha ", r"< 0",
                font_size=26
            )
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 5.5)
        
        # 设置颜色
        conclusion[1][0:2].set_color(self.COLOR_POSITIVE)  # sin α > 0
        conclusion[1][3:5].set_color(self.COLOR_NEGATIVE)  # cos α < 0
        conclusion[1][6:8].set_color(self.COLOR_NEGATIVE)  # tan α < 0
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=1.0)
        
        # 重点提示
        hint = Text(
            "只有 sin 为正!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7)
        
        self.play(FadeIn(hint, scale=1.2), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, quadrant_bg, angle_arc, angle_label,
                terminal_line, dot_P, label_P, proj_x, proj_y,
                x_label, y_label, conclusion, hint
            )),
            run_time=0.6
        )
    
    def show_quadrant_3(self):
        """场景5: 第三象限"""
        # 标题
        title = Text(
            "第三象限 (180° < α < 270°)",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_Q3
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 象限背景
        quadrant_bg = Polygon(
            self.center,
            self.center + LEFT * 2.5,
            self.center + LEFT * 2.5 + DOWN * 2.5,
            self.center + DOWN * 2.5,
            fill_color=self.COLOR_Q3,
            fill_opacity=0.15,
            stroke_width=0
        )
        
        self.play(FadeIn(quadrant_bg), run_time=0.5)
        
        # 角度
        angle_arc = Arc(
            radius=0.6,
            start_angle=0,
            angle=self.angle_Q3,
            arc_center=self.center,
            color=self.COLOR_Q3,
            stroke_width=3
        )
        
        angle_label = MathTex(r"\alpha", font_size=24, color=self.COLOR_Q3).move_to(
            self.center + np.array([-0.8, -0.25, 0])
        )
        
        self.play(Create(angle_arc), Write(angle_label), run_time=0.8)
        
        # 终边和点
        terminal_line = Line(self.center, self.P_Q3, color=self.COLOR_Q3, stroke_width=3)
        dot_P = Dot(self.P_Q3, color=self.COLOR_Q3, radius=0.1)
        label_P = MathTex(r"P(x, y)", font_size=24, color=WHITE).next_to(dot_P, DL, buff=0.15)
        
        self.play(Create(terminal_line), FadeIn(dot_P, scale=0.5), Write(label_P), run_time=0.8)
        
        # 投影
        x_proj_point = self.center + np.array([self.P_Q3[0] - self.center[0], 0, 0])
        
        proj_x = DashedLine(self.P_Q3, x_proj_point, color=self.COLOR_CIRCLE, dash_length=0.08)
        proj_y = DashedLine(
            self.P_Q3,
            self.center + np.array([0, self.P_Q3[1] - self.center[1], 0]),
            color=self.COLOR_CIRCLE,
            dash_length=0.08
        )
        
        self.play(Create(proj_x), Create(proj_y), run_time=0.8)
        
        # 符号标注
        x_label = MathTex("x < 0", font_size=24, color=self.COLOR_NEGATIVE).next_to(
            x_proj_point, UP, buff=0.3
        )
        y_label = MathTex("y < 0", font_size=24, color=self.COLOR_NEGATIVE).next_to(
            self.center + np.array([0, self.P_Q3[1] - self.center[1], 0]),
            LEFT, buff=0.3
        )
        
        self.play(Write(x_label), Write(y_label), run_time=0.8)
        
        # 结论
        conclusion = VGroup(
            Text("x < 0, y < 0", font="PingFang SC", font_size=26, color=WHITE),
            MathTex(
                r"\sin\alpha ", r"< 0,\ ",
                r"\cos\alpha ", r"< 0,\ ",
                r"\tan\alpha ", r"> 0",
                font_size=26
            )
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 5.5)
        
        # 设置颜色
        conclusion[1][0:2].set_color(self.COLOR_NEGATIVE)  # sin α < 0
        conclusion[1][3:5].set_color(self.COLOR_NEGATIVE)  # cos α < 0
        conclusion[1][6:8].set_color(self.COLOR_POSITIVE)  # tan α > 0
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=1.0)
        
        # 重点提示
        hint = Text(
            "只有 tan 为正!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7)
        
        self.play(FadeIn(hint, scale=1.2), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, quadrant_bg, angle_arc, angle_label,
                terminal_line, dot_P, label_P, proj_x, proj_y,
                x_label, y_label, conclusion, hint
            )),
            run_time=0.6
        )
    
    def show_quadrant_4(self):
        """场景6: 第四象限"""
        # 标题
        title = Text(
            "第四象限 (270° < α < 360°)",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_Q4
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 象限背景
        quadrant_bg = Polygon(
            self.center,
            self.center + RIGHT * 2.5,
            self.center + RIGHT * 2.5 + DOWN * 2.5,
            self.center + DOWN * 2.5,
            fill_color=self.COLOR_Q4,
            fill_opacity=0.15,
            stroke_width=0
        )
        
        self.play(FadeIn(quadrant_bg), run_time=0.5)
        
        # 角度
        angle_arc = Arc(
            radius=0.6,
            start_angle=0,
            angle=self.angle_Q4,
            arc_center=self.center,
            color=self.COLOR_Q4,
            stroke_width=3
        )
        
        angle_label = MathTex(r"\alpha", font_size=24, color=self.COLOR_Q4).move_to(
            self.center + np.array([0.8, -0.25, 0])
        )
        
        self.play(Create(angle_arc), Write(angle_label), run_time=0.8)
        
        # 终边和点
        terminal_line = Line(self.center, self.P_Q4, color=self.COLOR_Q4, stroke_width=3)
        dot_P = Dot(self.P_Q4, color=self.COLOR_Q4, radius=0.1)
        label_P = MathTex(r"P(x, y)", font_size=24, color=WHITE).next_to(dot_P, DR, buff=0.15)
        
        self.play(Create(terminal_line), FadeIn(dot_P, scale=0.5), Write(label_P), run_time=0.8)
        
        # 投影
        x_proj_point = self.center + np.array([self.P_Q4[0] - self.center[0], 0, 0])
        
        proj_x = DashedLine(self.P_Q4, x_proj_point, color=self.COLOR_CIRCLE, dash_length=0.08)
        proj_y = DashedLine(
            self.P_Q4,
            self.center + np.array([0, self.P_Q4[1] - self.center[1], 0]),
            color=self.COLOR_CIRCLE,
            dash_length=0.08
        )
        
        self.play(Create(proj_x), Create(proj_y), run_time=0.8)
        
        # 符号标注
        x_label = MathTex("x > 0", font_size=24, color=self.COLOR_POSITIVE).next_to(
            x_proj_point, UP, buff=0.3
        )
        y_label = MathTex("y < 0", font_size=24, color=self.COLOR_NEGATIVE).next_to(
            self.center + np.array([0, self.P_Q4[1] - self.center[1], 0]),
            RIGHT, buff=0.3
        )
        
        self.play(Write(x_label), Write(y_label), run_time=0.8)
        
        # 结论
        conclusion = VGroup(
            Text("x > 0, y < 0", font="PingFang SC", font_size=26, color=WHITE),
            MathTex(
                r"\sin\alpha ", r"< 0,\ ",
                r"\cos\alpha ", r"> 0,\ ",
                r"\tan\alpha ", r"< 0",
                font_size=26
            )
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 5.5)
        
        # 设置颜色
        conclusion[1][0:2].set_color(self.COLOR_NEGATIVE)  # sin α < 0
        conclusion[1][3:5].set_color(self.COLOR_POSITIVE)  # cos α > 0
        conclusion[1][6:8].set_color(self.COLOR_NEGATIVE)  # tan α < 0
        
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=1.0)
        
        # 重点提示
        hint = Text(
            "只有 cos 为正!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7)
        
        self.play(FadeIn(hint, scale=1.2), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(VGroup(
                title, quadrant_bg, angle_arc, angle_label,
                terminal_line, dot_P, label_P, proj_x, proj_y,
                x_label, y_label, conclusion, hint
            )),
            run_time=0.6
        )
    
    def show_sign_rule_mnemonic(self):
        """场景7: 象限符号口诀"""
        # 清空圆和轴（暂时）
        self.play(
            self.circle.animate.set_stroke(opacity=0.3),
            self.axes.animate.set_stroke(opacity=0.3),
            self.x_label.animate.set_opacity(0.3),
            self.y_label.animate.set_opacity(0.3),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "记忆口诀",
            font="PingFang SC",
            font_size=42,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 口诀
        mnemonic = Text(
            "一全二正弦三正切四余弦",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 4.5)
        
        self.play(Write(mnemonic, run_time=2.0))
        self.wait(1.0)
        
        # 详细说明卡片
        cards = VGroup()
        
        card_1 = self.create_quadrant_card(
            "一",
            "全部为正",
            "sin > 0, cos > 0, tan > 0",
            self.COLOR_Q1,
            UP * 2.5
        )
        
        card_2 = self.create_quadrant_card(
            "二",
            "正弦为正",
            "sin > 0, cos < 0, tan < 0",
            self.COLOR_Q2,
            UP * 0.8
        )
        
        card_3 = self.create_quadrant_card(
            "三",
            "正切为正",
            "sin < 0, cos < 0, tan > 0",
            self.COLOR_Q3,
            DOWN * 0.9
        )
        
        card_4 = self.create_quadrant_card(
            "四",
            "余弦为正",
            "sin < 0, cos > 0, tan < 0",
            self.COLOR_Q4,
            DOWN * 2.6
        )
        
        cards.add(card_1, card_2, card_3, card_4)
        
        # 逐个显示卡片
        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.5), run_time=0.5)
            self.wait(0.4)
        
        self.wait(2.0)
        
        # 强调口诀
        self.play(
            mnemonic.animate.scale(1.2).set_color(GOLD),
            run_time=0.8
        )
        self.play(
            mnemonic.animate.scale(1/1.2),
            run_time=0.5
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(mnemonic),
            FadeOut(cards),
            self.circle.animate.set_stroke(opacity=1),
            self.axes.animate.set_stroke(opacity=1),
            self.x_label.animate.set_opacity(1),
            self.y_label.animate.set_opacity(1),
            run_time=0.6
        )
    
    def create_quadrant_card(self, quadrant_num, title_text, formula_text, color, position):
        """创建象限符号卡片"""
        # 象限标记
        quadrant_label = Text(
            f"第{quadrant_num}象限",
            font="PingFang SC",
            font_size=24,
            color=color,
            weight=BOLD
        )
        
        # 说明
        title = Text(
            title_text,
            font="PingFang SC",
            font_size=22,
            color=WHITE
        )
        
        # 公式
        formula = Text(
            formula_text,
            font="PingFang SC",
            font_size=18,
            color=GRAY_A
        )
        
        # 色标
        color_bar = Rectangle(
            width=0.15,
            height=0.8,
            fill_color=color,
            fill_opacity=1,
            stroke_width=0
        )
        
        # 内容组合
        content = VGroup(quadrant_label, title, formula).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        
        # 完整卡片
        card = VGroup(color_bar, content).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        return card
    
    def show_rotation_demo(self):
        """场景8: 旋转演示动画 (简化版避免复杂路径问题)"""
        # 标题
        title = Text(
            "角度旋转演示",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.6)
        
        # 显示单位圆和坐标轴
        unit_circle = Circle(
            radius=self.RADIUS,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(self.center)
        
        axes = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False, "stroke_width": 2}
        ).move_to(self.center)
        
        self.play(Create(axes), run_time=0.8)
        self.play(Create(unit_circle), run_time=0.8)
        
        # 静态示例 - 显示几个关键角度的三角比
        key_angles = [PI/6, PI/4, PI/3, PI/2, 2*PI/3, 3*PI/4, 5*PI/6, PI]
        colors = [BLUE, GREEN, YELLOW, RED, PURPLE, ORANGE, MAROON, TEAL]
        
        # 逐步展示关键角度
        for i, angle in enumerate(key_angles):
            # 计算点坐标
            point = self.center + self.RADIUS * np.array([
                np.cos(angle),
                np.sin(angle),
                0
            ])
            
            # 绘制从中心到该点的线
            radial_line = Line(self.center, point, color=colors[i % len(colors)], stroke_width=3)
            
            # 绘制点
            dot = Dot(point, color=colors[i % len(colors)], radius=0.1)
            
            # 添加角度标签
            angle_label = MathTex(f"{int(angle*180/PI)}°", font_size=20, color=colors[i % len(colors)]).next_to(point, UR, buff=0.1)
            
            # 添加三角比值标签
            sin_val = np.sin(angle)
            cos_val = np.cos(angle)
            ratio_labels = MathTex(
                f"sin={sin_val:.2f}", f"cos={cos_val:.2f}",
                font_size=16, color=colors[i % len(colors)]).next_to(dot, DR, buff=0.1)
            
            self.play(
                Create(radial_line),
                FadeIn(dot),
                Write(angle_label),
                Write(ratio_labels),
                run_time=0.6
            )
        
        
        # 总结文本
        summary = Text(
            "随着角度变化，三角比也在周期性变化",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(DOWN * 5)
        
        self.play(Write(summary), run_time=1.0)
        
        # 等待一下
        self.wait(1.5)
        
        # 清理 - 淡出演示元素
        self.play(
            FadeOut(title),
            FadeOut(summary),
            run_time=0.8
        )
    def show_outro(self):
        """场景9: 片尾关注"""
        # 淡出圆和坐标系
        self.play(
            FadeOut(self.circle),
            FadeOut(self.axes),
            FadeOut(self.x_label),
            FadeOut(self.y_label),
            run_time=0.5
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 2)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 1)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，轻松学三角!",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 口诀重复
        mnemonic = Text(
            "一全二正弦三正切四余弦",
            font="PingFang SC",
            font_size=28,
            color=GOLD
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(mnemonic, scale=1.2), run_time=0.8)
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(mnemonic),
            run_time=1.0
        )


# 运行命令:
# manim -pql any_angle_trigonometry.py AnyAngleTrigonometry  # 快速预览
# manim -qh any_angle_trigonometry.py AnyAngleTrigonometry   # 高质量 1080p
# manim -qk any_angle_trigonometry.py AnyAngleTrigonometry   # 4K质量