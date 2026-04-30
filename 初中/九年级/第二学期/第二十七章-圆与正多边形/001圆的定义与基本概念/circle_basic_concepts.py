"""
圆的定义与基本概念 - Circle Definition and Basic Concepts
使用 Manim 创建的九年级几何教学视频

内容: 圆的定义、圆心、半径、直径、弦、弧（优弧、劣弧）
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


class CircleBasicConcepts(Scene):
    """
    圆的基本概念教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 圆的定义
    3. 半径
    4. 直径
    5. 弦
    6. 弧
    7. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCLE = "#3498db"       # 蓝色 - 主圆
        self.COLOR_RADIUS = "#e74c3c"       # 红色 - 半径
        self.COLOR_DIAMETER = "#f39c12"     # 橙色 - 直径
        self.COLOR_CHORD = "#2ecc71"        # 绿色 - 弦
        self.COLOR_ARC = "#9b59b6"          # 紫色 - 弧
        self.COLOR_CENTER = "#e74c3c"       # 红色 - 圆心
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_definition()
        self.show_radius()
        self.show_diameter()
        self.show_chord()
        self.show_arc()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化圆及所有几何元素"""
        # 圆心位置和半径
        self.O = ORIGIN + UP * 1.0
        self.radius = 2.0
        
        # 缩放因子（确保在安全边界内）
        self.SCALE = 0.9
        self.radius = self.radius * self.SCALE
        
        # 圆上的关键点 - 精确计算
        self.A = self.O + self.radius * RIGHT          # 0度
        self.D = self.O + self.radius * LEFT           # 180度
        self.B = self.point_on_circle(60)              # 60度
        self.C = self.point_on_circle(150)             # 150度
        
        # 验证几何关系
        self.verify_geometry()
        
        print("✓ 几何初始化完成")
    
    def point_on_circle(self, angle_deg):
        """在圆上生成精确的点"""
        angle_rad = angle_deg * DEGREES
        return self.O + self.radius * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证所有点都在圆上
        points = [self.A, self.B, self.C, self.D]
        for i, point in enumerate(points):
            dist = np.linalg.norm(point - self.O)
            if abs(dist - self.radius) > epsilon:
                print(f"WARNING: 点{i}不在圆上! 距离: {dist:.6f}, 半径: {self.radius:.6f}")
        
        # 验证直径长度
        diameter_length = np.linalg.norm(self.A - self.D)
        expected_diameter = 2 * self.radius
        if abs(diameter_length - expected_diameter) > epsilon:
            print(f"WARNING: 直径长度错误! 实际: {diameter_length:.6f}, 期望: {expected_diameter:.6f}")
        
        # 验证直径通过圆心
        midpoint = (self.A + self.D) / 2
        dist_to_center = np.linalg.norm(midpoint - self.O)
        if dist_to_center > epsilon:
            print(f"WARNING: 直径不通过圆心! 距离: {dist_to_center:.6f}")
        
        print("✓ 几何验证通过")
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "为什么车轮是圆的？",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 简单的圆形轮廓
        circle_outline = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=4
        ).move_to(self.O)
        
        self.play(Create(circle_outline), run_time=1.0)
        
        # 旋转动画（暗示车轮）
        self.play(Rotate(circle_outline, PI, run_time=1.0))
        
        self.wait(0.5)
        
        # 清理
        self.play(FadeOut(hook_text), run_time=0.4)
        
        # 保留circle_outline，将在下一场景转换
        self.circle_outline = circle_outline
    
    def show_definition(self):
        """场景2: 圆的定义"""
        # 标题
        title = Text(
            "圆的定义",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 圆心点出现
        self.center_dot = Dot(self.O, color=self.COLOR_CENTER, radius=0.12)
        center_label = Text(
            "O",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_CENTER
        ).next_to(self.center_dot, DOWN, buff=0.15)
        
        self.play(FadeIn(self.center_dot, scale=0.5), run_time=0.3)
        self.play(FadeIn(center_label), run_time=0.3)
        
        # 第一条半径生长
        radius_1 = Line(self.O, self.A, color=self.COLOR_RADIUS, stroke_width=3)
        self.play(GrowFromCenter(radius_1), run_time=0.5)
        
        # 半径标注"r"
        radius_label = MathTex("r", font_size=28, color=self.COLOR_RADIUS).next_to(
            radius_1.get_center(), UP, buff=0.1
        )
        self.play(FadeIn(radius_label), run_time=0.3)
        
        self.wait(0.3)
        
        # 多条半径依次出现（8条）
        angles = [45, 90, 135, 180, 225, 270, 315]
        radii = VGroup(*[
            Line(self.O, self.point_on_circle(angle), color=self.COLOR_RADIUS, stroke_width=2)
            for angle in angles
        ])
        
        self.play(
            AnimationGroup(*[Create(r) for r in radii], lag_ratio=0.15),
            run_time=1.0
        )
        
        self.wait(0.3)
        
        # 圆周轨迹描绘
        self.circle = Circle(
            radius=self.radius,
            color=self.COLOR_CIRCLE,
            stroke_width=4
        ).move_to(self.O)
        
        self.play(
            Transform(self.circle_outline, self.circle),
            run_time=1.5
        )
        
        # 定义公式
        definition_formula = MathTex(
            r"\{P \mid |PO| = r\}",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4)
        
        definition_text = Text(
            "到定点O距离等于定长r的所有点",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(
            FadeIn(definition_formula, shift=UP * 0.3),
            FadeIn(definition_text, shift=UP * 0.3),
            run_time=0.6
        )
        
        # 强调"等距"
        self.play(
            Indicate(VGroup(*radii, radius_1), color=self.COLOR_HIGHLIGHT),
            Flash(self.center_dot, color=self.COLOR_CENTER, flash_radius=0.4),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(radii),
            FadeOut(radius_1),
            FadeOut(radius_label),
            FadeOut(definition_formula),
            FadeOut(definition_text),
            FadeOut(title),
            FadeOut(center_label),
            run_time=0.6
        )
        
        # 保留circle_outline (已转换为circle), center_dot
    
    def show_radius(self):
        """场景3: 半径"""
        # 小标题
        subtitle = Text(
            "半径 Radius",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_RADIUS
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 创建3-4条不同角度的半径
        angles = [0, 75, 160, 270]
        radius_group = VGroup(*[
            Line(self.O, self.point_on_circle(angle), color=self.COLOR_RADIUS, stroke_width=3)
            for angle in angles
        ])
        
        self.play(
            AnimationGroup(*[Create(r) for r in radius_group], lag_ratio=0.2),
            run_time=1.0
        )
        
        # 半径闪烁高亮
        self.play(
            Indicate(radius_group, color=self.COLOR_HIGHLIGHT, scale_factor=1.1),
            run_time=0.7
        )
        
        # 显示公式
        radius_formula = MathTex(
            r"r = |PO|",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(radius_formula), run_time=0.4)
        
        # 说明文字
        explanation_text = Text(
            "连接圆心与圆上任意一点的线段",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation_text), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(radius_group),
            FadeOut(radius_formula),
            FadeOut(explanation_text),
            run_time=0.6
        )
    
    def show_diameter(self):
        """场景4: 直径"""
        # 小标题
        subtitle = Text(
            "直径 Diameter",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_DIAMETER
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 创建两条半径（将合并为直径）
        radius_OA = Line(self.O, self.A, color=self.COLOR_RADIUS, stroke_width=3)
        radius_OD = Line(self.O, self.D, color=self.COLOR_RADIUS, stroke_width=3)
        
        self.play(
            Create(radius_OA),
            Create(radius_OD),
            run_time=0.8
        )
        
        self.wait(0.3)
        
        # 两条半径变色为橙色并合并为直径
        diameter_line = Line(self.A, self.D, color=self.COLOR_DIAMETER, stroke_width=5)
        
        self.play(
            Transform(VGroup(radius_OA, radius_OD), diameter_line),
            run_time=0.6
        )
        
        # 端点标注A和D
        point_A_label = Text("A", font="PingFang SC", font_size=20, color=WHITE).next_to(
            self.A, RIGHT, buff=0.15
        )
        point_D_label = Text("D", font="PingFang SC", font_size=20, color=WHITE).next_to(
            self.D, LEFT, buff=0.15
        )
        
        dot_A = Dot(self.A, color=WHITE, radius=0.06)
        dot_D = Dot(self.D, color=WHITE, radius=0.06)
        
        self.play(
            FadeIn(dot_A),
            FadeIn(dot_D),
            FadeIn(point_A_label),
            FadeIn(point_D_label),
            run_time=0.5
        )
        
        # 直径标注"d"
        diameter_label = MathTex("d", font_size=28, color=self.COLOR_DIAMETER).next_to(
            diameter_line.get_center(), UP, buff=0.2
        )
        self.play(FadeIn(diameter_label), run_time=0.3)
        
        # 公式d=2r
        formula = MathTex(
            r"d = 2r",
            font_size=32,
            color=WHITE
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(formula), run_time=0.5)
        
        # 说明文字
        explanation = Text(
            "通过圆心的弦，圆中最长的弦",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(radius_OA),
            FadeOut(radius_OD),
            FadeOut(diameter_label),
            FadeOut(dot_A),
            FadeOut(dot_D),
            FadeOut(point_A_label),
            FadeOut(point_D_label),
            FadeOut(formula),
            FadeOut(explanation),
            run_time=0.6
        )
    
    def show_chord(self):
        """场景5: 弦"""
        # 小标题
        subtitle = Text(
            "弦 Chord",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_CHORD
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 点B和C出现在圆上
        dot_B = Dot(self.B, color=WHITE, radius=0.08)
        dot_C = Dot(self.C, color=WHITE, radius=0.08)
        
        self.play(
            FadeIn(dot_B, scale=0.5),
            FadeIn(dot_C, scale=0.5),
            run_time=0.6
        )
        
        # 弦BC生长
        chord_BC = Line(self.B, self.C, color=self.COLOR_CHORD, stroke_width=4)
        self.play(GrowFromCenter(chord_BC), run_time=0.6)
        
        # 点标注
        label_B = Text("B", font="PingFang SC", font_size=20, color=WHITE).next_to(
            self.B, UR, buff=0.1
        )
        label_C = Text("C", font="PingFang SC", font_size=20, color=WHITE).next_to(
            self.C, UL, buff=0.1
        )
        
        self.play(
            FadeIn(label_B),
            FadeIn(label_C),
            run_time=0.4
        )
        
        # 弦高亮
        self.play(
            Indicate(chord_BC, color=self.COLOR_HIGHLIGHT, scale_factor=1.05),
            run_time=0.7
        )
        
        # 创建另一条弦（对比）
        point_E = self.point_on_circle(240)
        point_F = self.point_on_circle(330)
        chord_2 = Line(point_E, point_F, color=self.COLOR_CHORD, stroke_width=3, stroke_opacity=0.6)
        
        self.play(Create(chord_2), run_time=0.6)
        
        self.wait(0.4)
        
        # 直径重新出现（虚线）用于对比
        diameter_dashed = DashedLine(
            self.A, self.D,
            color=self.COLOR_DIAMETER,
            dash_length=0.1,
            stroke_width=3
        )
        
        self.play(Create(diameter_dashed), run_time=0.6)
        
        # 对比文字
        comparison_text = Text(
            "直径是特殊的弦（最长）",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        explanation = Text(
            "连接圆上任意两点的线段",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(
            FadeIn(comparison_text),
            FadeIn(explanation),
            run_time=0.6
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(chord_BC),
            FadeOut(chord_2),
            FadeOut(diameter_dashed),
            FadeOut(dot_B),
            FadeOut(dot_C),
            FadeOut(label_B),
            FadeOut(label_C),
            FadeOut(comparison_text),
            FadeOut(explanation),
            run_time=0.6
        )
        
        # 重新创建dot_B和dot_C用于下一场景
        self.dot_B = Dot(self.B, color=WHITE, radius=0.08)
        self.dot_C = Dot(self.C, color=WHITE, radius=0.08)
        self.add(self.dot_B, self.dot_C)
    
    def show_arc(self):
        """场景6: 弧"""
        # 小标题
        subtitle = Text(
            "弧 Arc",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_ARC
        ).move_to(UP * 5.5)
        
        self.play(Write(subtitle), run_time=0.6)
        
        # 点B和C闪烁
        self.play(
            Indicate(self.dot_B, color=self.COLOR_HIGHLIGHT),
            Indicate(self.dot_C, color=self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        
        # 计算B和C的角度
        angle_B = np.arctan2(self.B[1] - self.O[1], self.B[0] - self.O[0])
        angle_C = np.arctan2(self.C[1] - self.O[1], self.C[0] - self.O[0])
        
        # 确保劣弧角度正确（从B到C逆时针）
        if angle_C < angle_B:
            angle_C += 2 * PI
        
        minor_arc_angle = angle_C - angle_B
        
        # 劣弧BC描绘（较短的弧）
        minor_arc = Arc(
            radius=self.radius,
            start_angle=angle_B,
            angle=minor_arc_angle,
            color=self.COLOR_ARC,
            stroke_width=6
        ).move_to(self.O)
        
        self.play(Create(minor_arc), run_time=1.0)
        
        # 劣弧标注
        # 计算弧的中点位置
        mid_angle = angle_B + minor_arc_angle / 2
        arc_mid_point = self.O + (self.radius + 0.4) * np.array([np.cos(mid_angle), np.sin(mid_angle), 0])
        
        minor_arc_label = MathTex(
            r"\overset{\frown}{BC}",
            font_size=24,
            color=self.COLOR_ARC
        ).move_to(arc_mid_point)
        
        self.play(FadeIn(minor_arc_label), run_time=0.4)
        
        # 说明："劣弧（小于半圆）"
        minor_arc_explanation = Text(
            "劣弧（小于半圆）",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(minor_arc_explanation), run_time=0.5)
        
        self.wait(1.0)
        
        # 优弧BC描绘（较长的弧，虚线）
        major_arc_angle = 2 * PI - minor_arc_angle
        
        major_arc = Arc(
            radius=self.radius,
            start_angle=angle_C,
            angle=major_arc_angle,
            color=self.COLOR_ARC,
            stroke_width=4
        ).move_to(self.O)
        
        # 转换为虚线
        major_arc = DashedVMobject(major_arc, num_dashes=30)
        
        self.play(Create(major_arc), run_time=1.5)
        
        # 优弧标注
        major_mid_angle = angle_C + major_arc_angle / 2
        major_arc_mid_point = self.O + (self.radius + 0.4) * np.array([np.cos(major_mid_angle), np.sin(major_mid_angle), 0])
        
        major_arc_label = MathTex(
            r"\overset{\frown}{BAC}",
            font_size=24,
            color=self.COLOR_ARC
        ).move_to(major_arc_mid_point)
        
        self.play(FadeIn(major_arc_label), run_time=0.4)
        
        # 说明："优弧（大于半圆）"
        major_arc_explanation = Text(
            "优弧（大于半圆）",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(major_arc_explanation), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(subtitle),
            FadeOut(minor_arc),
            FadeOut(major_arc),
            FadeOut(minor_arc_label),
            FadeOut(major_arc_label),
            FadeOut(minor_arc_explanation),
            FadeOut(major_arc_explanation),
            FadeOut(self.dot_B),
            FadeOut(self.dot_C),
            run_time=0.6
        )
    
    def show_summary(self):
        """场景7: 总结与片尾"""
        # 圆缩小并移到上方
        circle_small = Circle(
            radius=self.radius * 0.5,
            color=self.COLOR_CIRCLE,
            stroke_width=3
        ).move_to(UP * 4.5)
        
        center_dot_small = Dot(UP * 4.5, color=self.COLOR_CENTER, radius=0.06)
        
        self.play(
            Transform(self.circle_outline, circle_small),
            Transform(self.center_dot, center_dot_small),
            run_time=1.0
        )
        
        # 知识卡片（5个概念）
        cards = VGroup()
        
        # 圆心卡片
        card_1 = self.create_knowledge_card(
            "圆心",
            "定点O",
            self.COLOR_CENTER,
            UP * 2.5
        )
        cards.add(card_1)
        
        # 半径卡片
        card_2 = self.create_knowledge_card(
            "半径",
            "r = |PO|",
            self.COLOR_RADIUS,
            UP * 1.3
        )
        cards.add(card_2)
        
        # 直径卡片
        card_3 = self.create_knowledge_card(
            "直径",
            "d = 2r，通过圆心",
            self.COLOR_DIAMETER,
            UP * 0.1
        )
        cards.add(card_3)
        
        # 弦卡片
        card_4 = self.create_knowledge_card(
            "弦",
            "连接圆上两点",
            self.COLOR_CHORD,
            DOWN * 1.1
        )
        cards.add(card_4)
        
        # 弧卡片
        card_5 = self.create_knowledge_card(
            "弧",
            "圆上两点间的部分",
            self.COLOR_ARC,
            DOWN * 2.3
        )
        cards.add(card_5)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.4)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        self.wait(0.8)
        
        # 总结文字
        summary_text = Text(
            "掌握圆的基本元素\n开启几何新篇章！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=1.2
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(summary_text, shift=UP * 0.3, scale=1.05), run_time=0.6)
        
        self.wait(1.0)
        
        # 清理并准备片尾
        self.play(
            FadeOut(self.circle_outline),
            FadeOut(self.center_dot),
            FadeOut(cards),
            FadeOut(summary_text),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
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
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我，学更多几何技巧！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小圆形装饰
        circles = VGroup(*[
            Circle(radius=0.15, color=self.COLOR_CIRCLE, fill_opacity=0.8)
            .move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(circ, scale=0.5) for circ in circles],
            run_time=0.6
        )
        self.play(Rotate(circles, angle=PI, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(circles),
            run_time=1.0
        )
    
    def create_knowledge_card(self, title, content, color, position):
        """创建知识卡片"""
        # 图标圆
        icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=24,
            color=WHITE
        )
        
        # 内容
        content_text = Text(
            content,
            font="PingFang SC",
            font_size=18,
            color=GRAY_A
        )
        
        # 组合
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card


# 运行命令:
# manim -pql circle_basic_concepts.py CircleBasicConcepts  # 快速预览
# manim -qh circle_basic_concepts.py CircleBasicConcepts   # 高质量渲染