"""
圆的基本概念 - Circle Basic Concepts Animation
使用 Manim 创建的六年级数学教学视频

内容: 圆心、半径、直径、弦、弧等基本概念
目标观众: 六年级学生
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


class CircleBasicConcepts(Scene):
    """
    圆的基本概念教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 圆的定义
    3. 圆心 O
    4. 半径 r
    5. 直径 d
    6. 弦和弧
    7. 对称性
    8. 总结回顾
    9. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主圆
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 圆心
        self.COLOR_RADIUS = "#2ecc71"         # 绿色 - 半径
        self.COLOR_DIAMETER = "#f39c12"       # 橙色 - 直径
        self.COLOR_CHORD = "#9b59b6"          # 紫色 - 弦
        self.COLOR_ARC = "#1abc9c"            # 青色 - 弧
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_circle_definition()
        self.show_center()
        self.show_radius()
        self.show_diameter()
        self.show_chord_and_arc()
        self.show_symmetry()
        self.show_summary()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化圆和所有几何元素"""
        # 主圆参数
        self.O = ORIGIN + UP * 0.5  # 圆心位置
        self.radius = 2.5  # 半径
        
        # 创建主圆（但不添加到场景）
        self.main_circle = Circle(
            radius=self.radius,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).move_to(self.O)
        
        # 圆心点
        self.center_dot = Dot(
            self.O,
            color=self.COLOR_SECONDARY,
            radius=0.1
        )
        
        # 预计算常用点
        # 半径端点（右侧）
        self.P_right = self.O + RIGHT * self.radius
        
        # 直径端点
        self.D1 = self.O + LEFT * self.radius
        self.D2 = self.O + RIGHT * self.radius
        
        # 弦端点（60度和120度）
        angle1 = PI / 3  # 60度
        angle2 = 2 * PI / 3  # 120度
        self.C1 = self.O + self.radius * np.array([np.cos(angle1), np.sin(angle1), 0])
        self.C2 = self.O + self.radius * np.array([np.cos(angle2), np.sin(angle2), 0])
        
        # 弧端点（45度和135度）
        arc_angle1 = PI / 4  # 45度
        arc_angle2 = 3 * PI / 4  # 135度
        self.A1 = self.O + self.radius * np.array([np.cos(arc_angle1), np.sin(arc_angle1), 0])
        self.A2 = self.O + self.radius * np.array([np.cos(arc_angle2), np.sin(arc_angle2), 0])
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "你知道圆有多少个特殊点吗？",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 多个小圆闪现
        small_circles = VGroup(*[
            Circle(radius=0.3, color=self.COLOR_PRIMARY, stroke_width=2)
            .move_to(UP * 2 + RIGHT * i * 1.2 + DOWN * (i % 2) * 0.5)
            for i in range(-2, 3)
        ])
        
        self.play(
            *[Create(c) for c in small_circles],
            run_time=1.0
        )
        
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(small_circles),
            run_time=0.5
        )
    
    def show_circle_definition(self):
        """场景2: 圆的定义"""
        # 标题
        title = Text(
            "什么是圆？",
            font="Noto Sans CJK SC",
            font_size=42,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 圆心点出现
        self.play(FadeIn(self.center_dot, scale=0.5), run_time=0.4)
        self.play(Flash(self.center_dot, color=self.COLOR_SECONDARY), run_time=0.3)
        
        # 半径线段旋转绘制圆
        radius_line = Line(
            self.O,
            self.O + RIGHT * self.radius,
            color=self.COLOR_RADIUS,
            stroke_width=3
        )
        
        # 使用 ValueTracker 来实现旋转绘制
        angle_tracker = ValueTracker(0)
        
        rotating_line = always_redraw(
            lambda: Line(
                self.O,
                self.O + self.radius * np.array([
                    np.cos(angle_tracker.get_value()),
                    np.sin(angle_tracker.get_value()),
                    0
                ]),
                color=self.COLOR_RADIUS,
                stroke_width=3
            )
        )
        
        self.add(rotating_line)
        
        # 同时旋转和创建圆
        self.play(
            angle_tracker.animate.set_value(2 * PI),
            Create(self.main_circle),
            run_time=2.0,
            rate_func=linear
        )
        
        self.remove(rotating_line)
        
        # 定义文字
        definition = Text(
            "到定点距离等于定长的点的集合",
            font="Noto Sans CJK SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 4.5)
        
        self.play(Write(definition), run_time=1.5)
        
        # 公式
        formula = MathTex(
            r"\{ P \mid |PO| = r \}",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.5)
        
        self.play(Write(formula), run_time=1.0)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            run_time=0.5
        )
        
        # 公式移到顶部
        self.play(
            formula.animate.scale(0.7).move_to(UP * 6.5),
            run_time=0.6
        )
        
        # 保存公式引用以便后续清理
        self.formula_ref = formula
    
    def show_center(self):
        """场景3: 圆心 O"""
        # 标题
        title = Text(
            "圆心 O",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_SECONDARY
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 圆心放大闪烁
        self.play(
            self.center_dot.animate.scale(1.5),
            Flash(self.center_dot, color=self.COLOR_SECONDARY, flash_radius=0.5),
            run_time=0.6
        )
        
        self.play(self.center_dot.animate.scale(1/1.5), run_time=0.3)
        
        # 标签
        label_O = Text(
            "O",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_SECONDARY
        ).next_to(self.center_dot, DOWN + RIGHT, buff=0.15)
        
        self.play(FadeIn(label_O), run_time=0.4)
        
        # 说明
        explanation = Text(
            "圆心是圆的中心点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(Write(explanation), run_time=1.0)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            run_time=0.5
        )
        
        # 保存标签引用
        self.label_O = label_O
    
    def show_radius(self):
        """场景4: 半径 r"""
        # 标题
        title = Text(
            "半径 r",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_RADIUS
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 第一条半径
        radius_1 = Line(
            self.O,
            self.P_right,
            color=self.COLOR_RADIUS,
            stroke_width=4
        )
        
        self.play(Create(radius_1), run_time=0.6)
        
        # 端点和标签
        point_P = Dot(self.P_right, color=self.COLOR_RADIUS, radius=0.08)
        label_P = Text(
            "P",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_RADIUS
        ).next_to(point_P, RIGHT, buff=0.1)
        
        self.play(
            FadeIn(point_P),
            FadeIn(label_P),
            run_time=0.4
        )
        
        # 多条半径依次出现
        angles = [PI/6, PI/2, 7*PI/6, -PI/3]
        radius_lines = VGroup()
        
        for angle in angles:
            end_point = self.O + self.radius * np.array([np.cos(angle), np.sin(angle), 0])
            r_line = Line(
                self.O,
                end_point,
                color=self.COLOR_RADIUS,
                stroke_width=2,
                stroke_opacity=0.5
            )
            radius_lines.add(r_line)
        
        self.play(
            *[Create(line) for line in radius_lines],
            run_time=1.2
        )
        
        # 说明
        explanation = Text(
            "半径：圆心到圆上任意点的距离",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Write(explanation), run_time=1.0)
        
        # 公式
        formula_r = MathTex(
            r"r = |PO|",
            font_size=32,
            color=self.COLOR_RADIUS
        ).move_to(DOWN * 5)
        
        self.play(Write(formula_r), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(formula_r),
            FadeOut(radius_lines),
            FadeOut(point_P),
            FadeOut(label_P),
            run_time=0.6
        )
        
        # 保留一条半径线
        self.radius_1 = radius_1
    
    def show_diameter(self):
        """场景5: 直径 d"""
        # 标题
        title = Text(
            "直径 d",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_DIAMETER
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 清除半径线
        self.play(FadeOut(self.radius_1), run_time=0.3)
        
        # 直径线段
        diameter = Line(
            self.D1,
            self.D2,
            color=self.COLOR_DIAMETER,
            stroke_width=4
        )
        
        self.play(Create(diameter), run_time=0.8)
        
        # 端点标注
        point_A = Dot(self.D1, color=self.COLOR_DIAMETER, radius=0.08)
        point_B = Dot(self.D2, color=self.COLOR_DIAMETER, radius=0.08)
        label_A = Text("A", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_DIAMETER).next_to(point_A, LEFT, buff=0.1)
        label_B = Text("B", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_DIAMETER).next_to(point_B, RIGHT, buff=0.1)
        
        self.play(
            FadeIn(point_A),
            FadeIn(point_B),
            FadeIn(label_A),
            FadeIn(label_B),
            run_time=0.4
        )
        
        # 说明
        explanation = Text(
            "直径：通过圆心的弦",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Write(explanation), run_time=1.0)
        
        # 公式
        formula_d = MathTex(
            r"d = 2r",
            font_size=36,
            color=self.COLOR_DIAMETER
        ).move_to(DOWN * 5)
        
        self.play(Write(formula_d), run_time=0.8)
        
        # 演示 2r
        two_radii = VGroup(
            Line(self.O, self.D1, color=self.COLOR_RADIUS, stroke_width=3),
            Line(self.O, self.D2, color=self.COLOR_RADIUS, stroke_width=3)
        )
        
        brace_left = Brace(Line(self.D1, self.O), direction=DOWN, buff=0.1, color=self.COLOR_RADIUS)
        brace_right = Brace(Line(self.O, self.D2), direction=DOWN, buff=0.1, color=self.COLOR_RADIUS)
        label_r1 = Text("r", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_RADIUS).next_to(brace_left, DOWN, buff=0.05)
        label_r2 = Text("r", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_RADIUS).next_to(brace_right, DOWN, buff=0.05)
        
        self.play(
            Create(two_radii),
            FadeIn(brace_left),
            FadeIn(brace_right),
            FadeIn(label_r1),
            FadeIn(label_r2),
            run_time=0.6
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(formula_d),
            FadeOut(diameter),
            FadeOut(point_A),
            FadeOut(point_B),
            FadeOut(label_A),
            FadeOut(label_B),
            FadeOut(two_radii),
            FadeOut(brace_left),
            FadeOut(brace_right),
            FadeOut(label_r1),
            FadeOut(label_r2),
            run_time=0.6
        )
    
    def show_chord_and_arc(self):
        """场景6: 弦和弧"""
        # 标题
        title = Text(
            "弦和弧",
            font="Noto Sans CJK SC",
            font_size=38,
            color=self.COLOR_CHORD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 弦线段
        chord = Line(
            self.C1,
            self.C2,
            color=self.COLOR_CHORD,
            stroke_width=4
        )
        
        self.play(Create(chord), run_time=0.6)
        
        # 端点标注
        point_C = Dot(self.C1, color=self.COLOR_CHORD, radius=0.08)
        point_D = Dot(self.C2, color=self.COLOR_CHORD, radius=0.08)
        label_C = Text("C", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_CHORD).next_to(point_C, RIGHT + DOWN, buff=0.1)
        label_D = Text("D", font="Noto Sans CJK SC", font_size=24, color=self.COLOR_CHORD).next_to(point_D, LEFT + DOWN, buff=0.1)
        
        self.play(
            FadeIn(point_C),
            FadeIn(point_D),
            FadeIn(label_C),
            FadeIn(label_D),
            run_time=0.4
        )
        
        # 弦说明
        chord_explanation = Text(
            "弦：连接圆上两点的线段",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        self.play(Write(chord_explanation), run_time=1.0)
        
        # 弧高亮
        # 计算弧的起始和结束角度
        angle_C = np.arctan2(self.C1[1] - self.O[1], self.C1[0] - self.O[0])
        angle_D = np.arctan2(self.C2[1] - self.O[1], self.C2[0] - self.O[0])
        
        arc = Arc(
            radius=self.radius,
            start_angle=angle_C,
            angle=angle_D - angle_C,
            color=self.COLOR_ARC,
            stroke_width=6
        ).move_arc_center_to(self.O)
        
        self.play(Create(arc), run_time=0.8)
        
        # 弧说明
        arc_explanation = Text(
            "弧：圆上两点之间的曲线部分",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(Write(arc_explanation), run_time=1.0)
        
        # 直径对比（最长的弦）
        diameter_compare = Line(
            self.D1,
            self.D2,
            color=self.COLOR_DIAMETER,
            stroke_width=3
        )
        
        compare_text = Text(
            "直径是最长的弦",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(
            Create(diameter_compare),
            FadeIn(compare_text),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(chord),
            FadeOut(point_C),
            FadeOut(point_D),
            FadeOut(label_C),
            FadeOut(label_D),
            FadeOut(chord_explanation),
            FadeOut(arc),
            FadeOut(arc_explanation),
            FadeOut(diameter_compare),
            FadeOut(compare_text),
            run_time=0.6
        )
    
    def show_symmetry(self):
        """场景7: 圆的对称性"""
        # 标题
        title = Text(
            "圆的对称性",
            font="Noto Sans CJK SC",
            font_size=38,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title), run_time=0.4)
        
        # 第一条对称轴（竖直）
        axis_1 = DashedLine(
            self.O + UP * self.radius,
            self.O + DOWN * self.radius,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(axis_1), run_time=0.6)
        
        # 圆沿轴翻转动画（使用半圆演示）
        left_semicircle = Arc(
            radius=self.radius,
            start_angle=PI/2,
            angle=PI,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4
        ).move_arc_center_to(self.O)
        
        right_semicircle = Arc(
            radius=self.radius,
            start_angle=-PI/2,
            angle=PI,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=4,
            stroke_opacity=0.3
        ).move_arc_center_to(self.O)
        
        self.play(
            Create(left_semicircle),
            Create(right_semicircle),
            run_time=0.6
        )
        
        # 翻转动画
        self.play(
            Rotate(left_semicircle, angle=PI, axis=UP, about_point=self.O),
            run_time=1.2
        )
        
        self.play(
            FadeOut(left_semicircle),
            FadeOut(right_semicircle),
            run_time=0.3
        )
        
        # 多条对称轴旋转出现
        num_axes = 8
        symmetry_axes = VGroup()
        
        for i in range(num_axes):
            angle = i * PI / num_axes
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            axis = DashedLine(
                self.O - direction * self.radius,
                self.O + direction * self.radius,
                color=self.COLOR_AUXILIARY,
                dash_length=0.08,
                stroke_opacity=0.6
            )
            symmetry_axes.add(axis)
        
        self.play(
            Create(symmetry_axes),
            Rotate(symmetry_axes, angle=PI/4, about_point=self.O),
            run_time=1.5
        )
        
        # 说明
        explanation = Text(
            "任何直径所在直线都是对称轴",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(Write(explanation), run_time=1.2)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(axis_1),
            FadeOut(symmetry_axes),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景8: 总结回顾"""
        # 标题
        title = Text(
            "圆的基本要素",
            font="Noto Sans CJK SC",
            font_size=42,
            color=GOLD
        ).move_to(UP * 6.5)
        
        self.play(FadeIn(title), run_time=0.5)
        
        # 清除之前的公式引用
        if hasattr(self, 'formula_ref'):
            self.play(FadeOut(self.formula_ref), run_time=0.3)
        
        # 圆缩小移到上方
        self.play(
            self.main_circle.animate.scale(0.6).move_to(UP * 3),
            self.center_dot.animate.scale(0.6).move_to(UP * 3),
            self.label_O.animate.scale(0.8).move_to(UP * 3 + DOWN * 0.15 + RIGHT * 0.15),
            run_time=0.8
        )
        
        # 5个要素卡片
        cards_data = [
            ("圆心 O", "圆的中心点，记作O", self.COLOR_SECONDARY, UP * 1.2),
            ("半径 r", "圆心到圆上任意点的距离", self.COLOR_RADIUS, UP * 0.3),
            ("直径 d", "通过圆心的弦，d = 2r", self.COLOR_DIAMETER, DOWN * 0.6),
            ("弦", "连接圆上两点的线段", self.COLOR_CHORD, DOWN * 1.5),
            ("弧", "圆上两点之间的曲线部分", self.COLOR_ARC, DOWN * 2.4),
        ]
        
        cards = VGroup()
        
        for name, desc, color, pos in cards_data:
            # 图标圆
            icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
            
            # 名称
            name_text = Text(
                name,
                font="Noto Sans CJK SC",
                font_size=22,
                color=WHITE,
                weight=BOLD
            )
            
            # 描述
            desc_text = Text(
                desc,
                font="Noto Sans CJK SC",
                font_size=16,
                color=GRAY_A
            )
            
            # 组合
            card = VGroup(icon, name_text, desc_text).arrange(RIGHT, buff=0.2)
            card.move_to(pos)
            
            # 初始位置在左侧外
            card.shift(LEFT * 10)
            
            cards.add(card)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(
                card.animate.shift(RIGHT * 10),
                run_time=0.4
            )
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 重点提示
        highlight_text = Text(
            "掌握这些要素，圆就不再神秘！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(highlight_text, shift=UP * 0.3), run_time=0.6)
        
        self.wait(2.5)
        
        # 清理所有元素
        self.play(
            FadeOut(title),
            FadeOut(self.main_circle),
            FadeOut(self.center_dot),
            FadeOut(self.label_O),
            FadeOut(cards),
            FadeOut(highlight_text),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景9: 片尾关注"""
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=44,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        
        # ID出现
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        
        # 关注文字
        follow_text = Text(
            "关注我，学更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 圆形装饰
        circles_deco = VGroup(*[
            Circle(
                radius=0.25,
                color=self.COLOR_PRIMARY,
                fill_opacity=0.6,
                stroke_width=2
            ).move_to(
                follow_text.get_center() + 
                1.8 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0])
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(c, scale=0.5) for c in circles_deco],
            run_time=0.6
        )
        
        self.play(
            Rotate(circles_deco, angle=PI, about_point=follow_text.get_center()),
            run_time=1.5
        )
        
        self.wait(0.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles_deco),
            run_time=1.0
        )


# 运行命令:
# manim -pql circle_basic_concepts.py CircleBasicConcepts  # 快速预览
# manim -qh circle_basic_concepts.py CircleBasicConcepts   # 高质量渲染