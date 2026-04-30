"""
三角形的重要线段 - Triangle Important Segments Animation
使用 Manim 创建的七年级几何教学视频

内容: 中线、高线、角平分线的定义和性质
目标观众: 七年级学生
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


class TriangleImportantSegments(Scene):
    """
    三角形重要线段教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 中线 (Median)
    3. 高线 (Altitude)
    4. 角平分线 (Angle Bisector)
    5. 三线汇总对比
    6. 关键性质强化
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_MEDIAN = "#e74c3c"        # 红色 - 中线
        self.COLOR_ALTITUDE = "#3498db"      # 蓝色 - 高线
        self.COLOR_ANGLE_BISECTOR = "#2ecc71" # 绿色 - 角平分线
        self.COLOR_TRIANGLE = WHITE
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_HIGHLIGHT = YELLOW
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_median()
        self.show_altitude()
        self.show_angle_bisector()
        self.show_summary()
        self.show_properties()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化三角形和所有几何元素"""
        # 基准三角形顶点 (使用斜三角形便于展示所有线段)
        self.A = np.array([-2.5, 1.5, 0])
        self.B = np.array([2.5, -0.5, 0])
        self.C = np.array([-1.0, -2.5, 0])
        
        # 缩放和偏移
        self.SCALE = 0.85
        self.OFFSET = UP * 1.5
        
        # 应用变换
        self.A = self.A * self.SCALE + self.OFFSET
        self.B = self.B * self.SCALE + self.OFFSET
        self.C = self.C * self.SCALE + self.OFFSET
        
        # 计算边长
        self.a = np.linalg.norm(self.B - self.C)  # BC
        self.b = np.linalg.norm(self.C - self.A)  # CA
        self.c = np.linalg.norm(self.A - self.B)  # AB
        
        # 预计算所有中点
        self.M_AB = (self.A + self.B) / 2
        self.M_BC = (self.B + self.C) / 2
        self.M_CA = (self.C + self.A) / 2
        
        # 预计算重心
        self.centroid = (self.A + self.B + self.C) / 3
        
        # 预计算垂足
        self.foot_D = self.foot_of_perpendicular(self.A, self.B, self.C)
        self.foot_E = self.foot_of_perpendicular(self.B, self.C, self.A)
        self.foot_F = self.foot_of_perpendicular(self.C, self.A, self.B)
        
        # 预计算垂心
        self.orthocenter = self.calculate_orthocenter()
        
        # 预计算角平分线交点
        # 角平分线定理: BD/DC = AB/AC = c/b
        t_D = self.c / (self.b + self.c)
        self.point_D = self.B + t_D * (self.C - self.B)
        
        t_E = self.a / (self.a + self.c)
        self.point_E = self.C + t_E * (self.A - self.C)
        
        t_F = self.b / (self.a + self.b)
        self.point_F = self.A + t_F * (self.B - self.A)
        
        # 预计算内心
        self.incenter = (self.a * self.A + self.b * self.B + self.c * self.C) / (self.a + self.b + self.c)
        
        # 验证几何计算
        self.verify_geometry()
        
        # 创建三角形对象 (但不添加到场景)
        self.triangle = Polygon(self.A, self.B, self.C, color=self.COLOR_TRIANGLE, stroke_width=3)
    
    def foot_of_perpendicular(self, point, line_start, line_end):
        """计算点到直线的垂足"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        projection = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
        return line_start + projection * line_vec
    
    def calculate_orthocenter(self):
        """计算垂心 - 使用解析公式精确计算"""
        ax, ay = self.A[0], self.A[1]
        bx, by = self.B[0], self.B[1]
        cx, cy = self.C[0], self.C[1]
        
        # 从A到BC的高线方向: 垂直于BC
        # 从B到AC的高线方向: 垂直于AC
        
        # 高线1: A + t1*(cy-by, bx-cx)
        # 高线2: B + t2*(cy-ay, ax-cx)
        
        det = (cy - by) * (ax - cx) - (bx - cx) * (cy - ay)
        
        if abs(det) < 1e-10:
            # 退化情况
            return self.centroid
        
        t1 = ((bx - ax) * (ax - cx) + (by - ay) * (ay - cy)) / det
        
        hx = ax + t1 * (cy - by)
        hy = ay + t1 * (bx - cx)
        
        return np.array([hx, hy, 0])
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证中点
        assert np.linalg.norm(self.M_BC - (self.B + self.C) / 2) < epsilon, "BC中点计算错误"
        assert np.linalg.norm(self.M_CA - (self.C + self.A) / 2) < epsilon, "CA中点计算错误"
        assert np.linalg.norm(self.M_AB - (self.A + self.B) / 2) < epsilon, "AB中点计算错误"
        
        # 验证重心
        assert np.linalg.norm(self.centroid - (self.A + self.B + self.C) / 3) < epsilon, "重心计算错误"
        
        # 验证垂足的垂直性
        vec_AD = self.foot_D - self.A
        vec_BC = self.C - self.B
        dot_product_1 = np.dot(vec_AD[:2], vec_BC[:2])
        assert abs(dot_product_1) < epsilon, f"A到BC的垂直性错误: 点积={dot_product_1}"
        
        vec_BE = self.foot_E - self.B
        vec_CA = self.A - self.C
        dot_product_2 = np.dot(vec_BE[:2], vec_CA[:2])
        assert abs(dot_product_2) < epsilon, f"B到CA的垂直性错误: 点积={dot_product_2}"
        
        # 验证内心
        incenter_check = (self.a * self.A + self.b * self.B + self.c * self.C) / (self.a + self.b + self.c)
        assert np.linalg.norm(self.incenter - incenter_check) < epsilon, "内心计算错误"
        
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
        hook_text = Text(
            "三角形有哪些重要线段?",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 三角形淡入
        self.play(Create(self.triangle), run_time=1.0)
        
        # 顶点标签
        label_A = Text("A", font="PingFang SC", font_size=24, color=WHITE).next_to(self.A, UL, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=24, color=WHITE).next_to(self.B, UR, buff=0.15)
        label_C = Text("C", font="PingFang SC", font_size=24, color=WHITE).next_to(self.C, DOWN, buff=0.15)
        
        self.vertex_labels = VGroup(label_A, label_B, label_C)
        
        self.play(FadeIn(self.vertex_labels), run_time=0.4)
        self.wait(1.0)
        
        # 清理钩子
        self.play(FadeOut(hook_text), run_time=0.5)
    
    def show_median(self):
        """场景2: 中线 - 连接顶点与对边中点"""
        # 标题
        title = Text(
            "中线 Median",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_MEDIAN
        ).move_to(UP * 5.5)
        
        definition = Text(
            "连接顶点与对边中点的线段",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # Step 1: BC的中点和中线AM
        bc_line = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(bc_line), run_time=0.4)
        
        m_bc_dot = Dot(self.M_BC, color=self.COLOR_AUXILIARY, radius=0.06)
        m_bc_label = Text("M", font="PingFang SC", font_size=20, color=WHITE).next_to(m_bc_dot, DOWN, buff=0.1)
        
        self.play(FadeIn(m_bc_dot), FadeIn(m_bc_label), run_time=0.4)
        
        explain_1 = Text(
            "中点: 平分对边",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain_1), run_time=0.3)
        
        median_1 = Line(self.A, self.M_BC, color=self.COLOR_MEDIAN, stroke_width=2)
        
        self.play(Create(median_1), run_time=0.8)
        self.play(bc_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        self.play(FadeOut(explain_1), FadeOut(bc_line), run_time=0.2)
        
        # Step 2: CA的中点和中线BN
        ca_line = Line(self.C, self.A, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(ca_line), run_time=0.4)
        
        m_ca_dot = Dot(self.M_CA, color=self.COLOR_AUXILIARY, radius=0.06)
        m_ca_label = Text("N", font="PingFang SC", font_size=20, color=WHITE).next_to(m_ca_dot, LEFT, buff=0.1)
        
        self.play(FadeIn(m_ca_dot), FadeIn(m_ca_label), run_time=0.3)
        
        median_2 = Line(self.B, self.M_CA, color=self.COLOR_MEDIAN, stroke_width=2)
        
        self.play(Create(median_2), run_time=0.8)
        self.play(ca_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        self.play(FadeOut(ca_line), run_time=0.2)
        
        # Step 3: AB的中点和中线CP
        ab_line = Line(self.A, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(ab_line), run_time=0.4)
        
        m_ab_dot = Dot(self.M_AB, color=self.COLOR_AUXILIARY, radius=0.06)
        m_ab_label = Text("P", font="PingFang SC", font_size=20, color=WHITE).next_to(m_ab_dot, UP, buff=0.1)
        
        self.play(FadeIn(m_ab_dot), FadeIn(m_ab_label), run_time=0.3)
        
        median_3 = Line(self.C, self.M_AB, color=self.COLOR_MEDIAN, stroke_width=2)
        
        self.play(Create(median_3), run_time=0.8)
        self.play(ab_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        self.play(FadeOut(ab_line), run_time=0.2)
        
        # Step 4: 标记重心
        g_dot = Dot(self.centroid, color=self.COLOR_MEDIAN, radius=0.12)
        g_label = Text("G", font="PingFang SC", font_size=24, color=self.COLOR_MEDIAN).next_to(g_dot, RIGHT, buff=0.15)
        g_label_2 = Text("重心", font="PingFang SC", font_size=18, color=self.COLOR_MEDIAN).next_to(g_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(g_dot, scale=0.5), run_time=0.5)
        self.play(Flash(g_dot, color=self.COLOR_MEDIAN, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(g_label), FadeIn(g_label_2), run_time=0.4)
        
        property_text = Text(
            "三条中线交于重心",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(property_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.median_group = VGroup(median_1, median_2, median_3)
        self.median_midpoints = VGroup(m_bc_dot, m_ca_dot, m_ab_dot, m_bc_label, m_ca_label, m_ab_label)
        
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(property_text),
            FadeOut(g_label),
            FadeOut(g_label_2),
            run_time=0.6
        )
        
        # 保留重心点但变小
        self.g_small = Dot(self.centroid, color=self.COLOR_MEDIAN, radius=0.05, fill_opacity=0.5)
        self.play(Transform(g_dot, self.g_small), run_time=0.3)
        self.remove(g_dot)
        self.add(self.g_small)
        
        # 中线变灰虚线
        self.play(
            self.median_group.animate.set_color(GRAY_B).set_stroke(width=1.5),
            FadeOut(self.median_midpoints),
            run_time=0.4
        )
    
    def show_altitude(self):
        """场景3: 高线 - 从顶点到对边的垂线段"""
        # 清理中线
        self.play(FadeOut(self.median_group), run_time=0.4)
        
        # 标题
        title = Text(
            "高线 Altitude",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_ALTITUDE
        ).move_to(UP * 5.5)
        
        definition = Text(
            "从顶点向对边所在直线作的垂线段",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # Step 1: 从A到BC的高
        bc_line = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(bc_line), run_time=0.5)
        
        explain_1 = Text(
            "高线: 垂直于底边",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain_1), run_time=0.3)
        
        foot_d_dot = Dot(self.foot_D, color=self.COLOR_AUXILIARY, radius=0.06)
        
        self.play(FadeIn(foot_d_dot), run_time=0.3)
        
        altitude_1 = DashedLine(self.A, self.foot_D, color=self.COLOR_ALTITUDE, dash_length=0.1)
        
        self.play(Create(altitude_1), run_time=0.8)
        
        # 直角符号
        right_angle_1 = self.create_right_angle_mark(self.foot_D, self.A, self.B, size=0.15)
        
        self.play(FadeIn(right_angle_1), run_time=0.4)
        self.play(bc_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        self.play(FadeOut(explain_1), FadeOut(bc_line), run_time=0.2)
        
        # Step 2: 从B到CA的高
        ca_line = Line(self.C, self.A, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(ca_line), run_time=0.5)
        
        foot_e_dot = Dot(self.foot_E, color=self.COLOR_AUXILIARY, radius=0.06)
        
        self.play(FadeIn(foot_e_dot), run_time=0.3)
        
        altitude_2 = DashedLine(self.B, self.foot_E, color=self.COLOR_ALTITUDE, dash_length=0.1)
        
        self.play(Create(altitude_2), run_time=0.8)
        
        right_angle_2 = self.create_right_angle_mark(self.foot_E, self.B, self.C, size=0.15)
        
        self.play(FadeIn(right_angle_2), run_time=0.4)
        self.play(ca_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        self.play(FadeOut(ca_line), run_time=0.2)
        
        # Step 3: 从C到AB的高
        ab_line = Line(self.A, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(ab_line), run_time=0.5)
        
        foot_f_dot = Dot(self.foot_F, color=self.COLOR_AUXILIARY, radius=0.06)
        
        self.play(FadeIn(foot_f_dot), run_time=0.3)
        
        altitude_3 = DashedLine(self.C, self.foot_F, color=self.COLOR_ALTITUDE, dash_length=0.1)
        
        self.play(Create(altitude_3), run_time=0.8)
        
        right_angle_3 = self.create_right_angle_mark(self.foot_F, self.C, self.A, size=0.15)
        
        self.play(FadeIn(right_angle_3), run_time=0.4)
        self.play(ab_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        self.play(FadeOut(ab_line), run_time=0.2)
        
        # Step 4: 标记垂心
        h_dot = Dot(self.orthocenter, color=self.COLOR_ALTITUDE, radius=0.12)
        h_label = Text("H", font="PingFang SC", font_size=24, color=self.COLOR_ALTITUDE).next_to(h_dot, RIGHT, buff=0.15)
        h_label_2 = Text("垂心", font="PingFang SC", font_size=18, color=self.COLOR_ALTITUDE).next_to(h_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(h_dot, scale=0.5), run_time=0.5)
        self.play(Flash(h_dot, color=self.COLOR_ALTITUDE, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(h_label), FadeIn(h_label_2), run_time=0.4)
        
        property_text = Text(
            "三条高线交于垂心",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(property_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.altitude_group = VGroup(altitude_1, altitude_2, altitude_3)
        self.altitude_feet = VGroup(foot_d_dot, foot_e_dot, foot_f_dot)
        self.right_angles = VGroup(right_angle_1, right_angle_2, right_angle_3)
        
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(property_text),
            FadeOut(h_label),
            FadeOut(h_label_2),
            FadeOut(self.right_angles),
            run_time=0.6
        )
        
        # 保留垂心点但变小
        self.h_small = Dot(self.orthocenter, color=self.COLOR_ALTITUDE, radius=0.05, fill_opacity=0.5)
        self.play(Transform(h_dot, self.h_small), run_time=0.3)
        self.remove(h_dot)
        self.add(self.h_small)
        
        # 高线变灰虚线
        self.play(
            self.altitude_group.animate.set_color(GRAY_B).set_stroke(width=1.5),
            FadeOut(self.altitude_feet),
            run_time=0.4
        )
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.2):
        """创建直角标记"""
        vec1 = (point1 - corner)
        vec1 = vec1 / np.linalg.norm(vec1) * size
        vec2 = (point2 - corner)
        vec2 = vec2 / np.linalg.norm(vec2) * size
        
        square = Polygon(
            corner,
            corner + vec1,
            corner + vec1 + vec2,
            corner + vec2,
            color=YELLOW,
            stroke_width=1.5,
            fill_opacity=0
        )
        return square
    
    def show_angle_bisector(self):
        """场景4: 角平分线 - 平分角的线段"""
        # 清理高线
        self.play(FadeOut(self.altitude_group), run_time=0.4)
        
        # 标题
        title = Text(
            "角平分线 Angle Bisector",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_ANGLE_BISECTOR
        ).move_to(UP * 5.5)
        
        definition = Text(
            "角的平分线与对边的交点连成的线段",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # Step 1: 角A的角平分线
        explain_1 = Text(
            "平分角度",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(explain_1), run_time=0.3)
        
        # 高亮角A的两边
        ab_line = Line(self.A, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        ac_line = Line(self.A, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        
        self.play(Create(ab_line), Create(ac_line), run_time=0.5)
        
        # 角A的弧线 - 根据验证结果: 顺时针,使用 other_angle=True
        # 计算角弧方向
        vec_AB = self.B - self.A
        vec_AC = self.C - self.A
        cross_z = vec_AB[0] * vec_AC[1] - vec_AB[1] * vec_AC[0]
        # cross_z = -12.282500 < 0, 顺时针
        
        if cross_z > 0:
            # 逆时针
            angle_A_arc = Angle.from_three_points(self.B, self.A, self.C, radius=0.5, other_angle=False, color=YELLOW)
        else:
            # 顺时针 ← 实际情况
            angle_A_arc = Angle.from_three_points(self.B, self.A, self.C, radius=0.5, other_angle=True, color=YELLOW)
        
        self.play(Create(angle_A_arc), run_time=0.4)
        
        # 交点D
        point_d_dot = Dot(self.point_D, color=self.COLOR_AUXILIARY, radius=0.06)
        
        self.play(FadeIn(point_d_dot), run_time=0.3)
        
        # 角平分线AD
        bisector_1 = DashedLine(self.A, self.point_D, color=self.COLOR_ANGLE_BISECTOR, dash_length=0.1)
        
        self.play(Create(bisector_1), run_time=0.8)
        
        # 恢复颜色
        self.play(
            ab_line.animate.set_color(self.COLOR_TRIANGLE),
            ac_line.animate.set_color(self.COLOR_TRIANGLE),
            run_time=0.3
        )
        self.play(FadeOut(explain_1), FadeOut(angle_A_arc), FadeOut(ab_line), FadeOut(ac_line), run_time=0.2)
        
        # Step 2: 角B的角平分线
        ba_line = Line(self.B, self.A, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        bc_line = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        
        self.play(Create(ba_line), Create(bc_line), run_time=0.5)
        
        # 角B的弧线 - 根据验证结果: 逆时针,使用 other_angle=False
        vec_BA = self.A - self.B
        vec_BC = self.C - self.B
        cross_z_B = vec_BA[0] * vec_BC[1] - vec_BA[1] * vec_BC[0]
        # cross_z_B = 12.282500 > 0, 逆时针
        
        if cross_z_B > 0:
            # 逆时针 ← 实际情况
            angle_B_arc = Angle.from_three_points(self.A, self.B, self.C, radius=0.5, other_angle=False, color=YELLOW)
        else:
            # 顺时针
            angle_B_arc = Angle.from_three_points(self.A, self.B, self.C, radius=0.5, other_angle=True, color=YELLOW)
        
        self.play(Create(angle_B_arc), run_time=0.4)
        
        # 交点E
        point_e_dot = Dot(self.point_E, color=self.COLOR_AUXILIARY, radius=0.06)
        
        self.play(FadeIn(point_e_dot), run_time=0.3)
        
        # 角平分线BE
        bisector_2 = DashedLine(self.B, self.point_E, color=self.COLOR_ANGLE_BISECTOR, dash_length=0.1)
        
        self.play(Create(bisector_2), run_time=0.8)
        
        self.play(
            ba_line.animate.set_color(self.COLOR_TRIANGLE),
            bc_line.animate.set_color(self.COLOR_TRIANGLE),
            run_time=0.3
        )
        self.play(FadeOut(angle_B_arc), FadeOut(ba_line), FadeOut(bc_line), run_time=0.2)
        
        # Step 3: 角C的角平分线
        ca_line = Line(self.C, self.A, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        cb_line = Line(self.C, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        
        self.play(Create(ca_line), Create(cb_line), run_time=0.5)
        
        # 角C的弧线 - 根据验证结果: 顺时针,使用 other_angle=True
        vec_CA = self.A - self.C
        vec_CB = self.B - self.C
        cross_z_C = vec_CA[0] * vec_CB[1] - vec_CA[1] * vec_CB[0]
        # cross_z_C = -12.282500 < 0, 顺时针
        
        if cross_z_C > 0:
            # 逆时针
            angle_C_arc = Angle.from_three_points(self.A, self.C, self.B, radius=0.5, other_angle=False, color=YELLOW)
        else:
            # 顺时针 ← 实际情况
            angle_C_arc = Angle.from_three_points(self.A, self.C, self.B, radius=0.5, other_angle=True, color=YELLOW)
        
        self.play(Create(angle_C_arc), run_time=0.4)
        
        # 交点F
        point_f_dot = Dot(self.point_F, color=self.COLOR_AUXILIARY, radius=0.06)
        
        self.play(FadeIn(point_f_dot), run_time=0.3)
        
        # 角平分线CF
        bisector_3 = DashedLine(self.C, self.point_F, color=self.COLOR_ANGLE_BISECTOR, dash_length=0.1)
        
        self.play(Create(bisector_3), run_time=0.8)
        
        self.play(
            ca_line.animate.set_color(self.COLOR_TRIANGLE),
            cb_line.animate.set_color(self.COLOR_TRIANGLE),
            run_time=0.3
        )
        self.play(FadeOut(angle_C_arc), FadeOut(ca_line), FadeOut(cb_line), run_time=0.2)
        
        # Step 4: 标记内心
        i_dot = Dot(self.incenter, color=self.COLOR_ANGLE_BISECTOR, radius=0.12)
        i_label = Text("I", font="PingFang SC", font_size=24, color=self.COLOR_ANGLE_BISECTOR).next_to(i_dot, LEFT, buff=0.15)
        i_label_2 = Text("内心", font="PingFang SC", font_size=18, color=self.COLOR_ANGLE_BISECTOR).next_to(i_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(i_dot, scale=0.5), run_time=0.5)
        self.play(Flash(i_dot, color=self.COLOR_ANGLE_BISECTOR, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(i_label), FadeIn(i_label_2), run_time=0.4)
        
        property_text = Text(
            "三条角平分线交于内心",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(property_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.bisector_group = VGroup(bisector_1, bisector_2, bisector_3)
        self.bisector_points = VGroup(point_d_dot, point_e_dot, point_f_dot)
        
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(property_text),
            FadeOut(i_label),
            FadeOut(i_label_2),
            run_time=0.6
        )
        
        # 保留内心点但变小
        self.i_small = Dot(self.incenter, color=self.COLOR_ANGLE_BISECTOR, radius=0.05, fill_opacity=0.5)
        self.play(Transform(i_dot, self.i_small), run_time=0.3)
        self.remove(i_dot)
        self.add(self.i_small)
        
        # 角平分线变灰虚线
        self.play(
            self.bisector_group.animate.set_color(GRAY_B).set_stroke(width=1.5),
            FadeOut(self.bisector_points),
            run_time=0.4
        )
    
    def show_summary(self):
        """场景5: 三线汇总对比"""
        # 清理所有辅助线
        self.play(
            FadeOut(self.bisector_group),
            run_time=0.4
        )
        
        # 三角形缩放移动
        triangle_small = self.triangle.copy().scale(0.6).move_to(UP * 2.5)
        
        # 重新计算缩放后的坐标
        scale_factor = 0.6
        center_offset = UP * 2.5
        
        # 重新创建三条线段组
        A_new = (self.A - self.OFFSET) * scale_factor + center_offset
        B_new = (self.B - self.OFFSET) * scale_factor + center_offset
        C_new = (self.C - self.OFFSET) * scale_factor + center_offset
        
        M_BC_new = (self.M_BC - self.OFFSET) * scale_factor + center_offset
        M_CA_new = (self.M_CA - self.OFFSET) * scale_factor + center_offset
        M_AB_new = (self.M_AB - self.OFFSET) * scale_factor + center_offset
        
        foot_D_new = (self.foot_D - self.OFFSET) * scale_factor + center_offset
        foot_E_new = (self.foot_E - self.OFFSET) * scale_factor + center_offset
        foot_F_new = (self.foot_F - self.OFFSET) * scale_factor + center_offset
        
        point_D_new = (self.point_D - self.OFFSET) * scale_factor + center_offset
        point_E_new = (self.point_E - self.OFFSET) * scale_factor + center_offset
        point_F_new = (self.point_F - self.OFFSET) * scale_factor + center_offset
        
        g_pos = (self.centroid - self.OFFSET) * scale_factor + center_offset
        h_pos = (self.orthocenter - self.OFFSET) * scale_factor + center_offset
        i_pos = (self.incenter - self.OFFSET) * scale_factor + center_offset
        
        # 创建新的线段组
        median_group_new = VGroup(
            Line(A_new, M_BC_new, color=self.COLOR_MEDIAN, stroke_width=2),
            Line(B_new, M_CA_new, color=self.COLOR_MEDIAN, stroke_width=2),
            Line(C_new, M_AB_new, color=self.COLOR_MEDIAN, stroke_width=2)
        )
        
        altitude_group_new = VGroup(
            DashedLine(A_new, foot_D_new, color=self.COLOR_ALTITUDE, dash_length=0.08),
            DashedLine(B_new, foot_E_new, color=self.COLOR_ALTITUDE, dash_length=0.08),
            DashedLine(C_new, foot_F_new, color=self.COLOR_ALTITUDE, dash_length=0.08)
        )
        
        bisector_group_new = VGroup(
            DashedLine(A_new, point_D_new, color=self.COLOR_ANGLE_BISECTOR, dash_length=0.08),
            DashedLine(B_new, point_E_new, color=self.COLOR_ANGLE_BISECTOR, dash_length=0.08),
            DashedLine(C_new, point_F_new, color=self.COLOR_ANGLE_BISECTOR, dash_length=0.08)
        )
        
        # 动画: 三角形缩放移动
        self.play(
            Transform(self.triangle, triangle_small),
            self.vertex_labels.animate.scale(0.6).shift(UP * 2.5 - self.OFFSET),
            run_time=0.8
        )
        
        # 依次绘制三组线段
        self.play(Create(median_group_new, lag_ratio=0.3), run_time=1.0)
        self.play(
            self.g_small.animate.move_to(g_pos).scale(2).set_opacity(1),
            Flash(Dot(g_pos), color=self.COLOR_MEDIAN),
            run_time=0.5
        )
        
        self.play(Create(altitude_group_new, lag_ratio=0.3), run_time=1.0)
        self.play(
            self.h_small.animate.move_to(h_pos).scale(2).set_opacity(1),
            Flash(Dot(h_pos), color=self.COLOR_ALTITUDE),
            run_time=0.5
        )
        
        self.play(Create(bisector_group_new, lag_ratio=0.3), run_time=1.0)
        self.play(
            self.i_small.animate.move_to(i_pos).scale(2).set_opacity(1),
            Flash(Dot(i_pos), color=self.COLOR_ANGLE_BISECTOR),
            run_time=0.5
        )
        
        # 标注三个点
        g_label = Text("G", font="PingFang SC", font_size=18, color=self.COLOR_MEDIAN).next_to(self.g_small, DOWN, buff=0.08)
        h_label = Text("H", font="PingFang SC", font_size=18, color=self.COLOR_ALTITUDE).next_to(self.h_small, RIGHT, buff=0.08)
        i_label = Text("I", font="PingFang SC", font_size=18, color=self.COLOR_ANGLE_BISECTOR).next_to(self.i_small, LEFT, buff=0.08)
        
        self.play(
            FadeIn(g_label),
            FadeIn(h_label),
            FadeIn(i_label),
            run_time=0.5
        )
        
        # 对比卡片
        card_1 = self.create_summary_card(
            "中线",
            "顶点→对边中点, 交于重心G",
            self.COLOR_MEDIAN,
            DOWN * 0.5
        )
        
        card_2 = self.create_summary_card(
            "高线",
            "顶点→对边垂线, 交于垂心H",
            self.COLOR_ALTITUDE,
            DOWN * 1.8
        )
        
        card_3 = self.create_summary_card(
            "角平分线",
            "角平分→对边, 交于内心I",
            self.COLOR_ANGLE_BISECTOR,
            DOWN * 3.1
        )
        
        cards = VGroup(card_1, card_2, card_3)
        
        # 卡片从左侧滑入
        for card in cards:
            card.shift(LEFT * 10)
        
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(self.triangle),
            FadeOut(self.vertex_labels),
            FadeOut(median_group_new),
            FadeOut(altitude_group_new),
            FadeOut(bisector_group_new),
            FadeOut(self.g_small),
            FadeOut(self.h_small),
            FadeOut(self.i_small),
            FadeOut(g_label),
            FadeOut(h_label),
            FadeOut(i_label),
            FadeOut(cards),
            run_time=0.6
        )
    
    def create_summary_card(self, title, content, color, position):
        """创建对比卡片"""
        # 图标圆
        icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 标题
        title_text = Text(
            title,
            font="PingFang SC",
            font_size=22,
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
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.25)
        card.move_to(position)
        
        return card
    
    def show_properties(self):
        """场景6: 关键性质强化"""
        # 标题
        title = Text(
            "关键性质",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(title), run_time=0.6)
        
        # 性质列表
        property_1 = self.create_property_item(
            "1",
            "中线: 重心分中线为 2:1",
            UP * 3.5
        )
        
        property_2 = self.create_property_item(
            "2",
            "高线: 高线垂直于底边",
            UP * 2.2
        )
        
        property_3 = self.create_property_item(
            "3",
            "角平分线: 内心到三边距离相等",
            UP * 0.9
        )
        
        property_4 = self.create_property_item(
            "4",
            "共同特点: 三线共点",
            DOWN * 0.4
        )
        
        properties = VGroup(property_1, property_2, property_3, property_4)
        
        # 从左侧滑入
        for prop in properties:
            prop.shift(LEFT * 10)
        
        for i, prop in enumerate(properties):
            self.play(prop.animate.shift(RIGHT * 10), run_time=0.4)
            if i < len(properties) - 1:
                self.wait(0.2)
        
        # 重点提示
        highlight = Text(
            "记住这些性质, 轻松解题!",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(highlight, shift=UP * 0.3, scale=1.1), run_time=0.5)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(properties),
            FadeOut(highlight),
            run_time=0.6
        )
    
    def create_property_item(self, number, text, position):
        """创建性质条目"""
        # 编号圆
        number_circle = Circle(radius=0.25, fill_color=self.COLOR_HIGHLIGHT, fill_opacity=1, stroke_width=0)
        number_text = Text(number, font="PingFang SC", font_size=22, color=BLACK).move_to(number_circle.get_center())
        number_group = VGroup(number_circle, number_text)
        
        # 文字
        content = Text(
            text,
            font="PingFang SC",
            font_size=22,
            color=WHITE
        )
        
        # 组合
        item = VGroup(number_group, content).arrange(RIGHT, buff=0.4)
        item.move_to(position)
        
        return item
    
    def show_outro(self):
        """场景7: 片尾关注"""
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
            "关注我, 学更多几何技巧!",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 三角形装饰
        triangles = VGroup(*[
            Polygon(ORIGIN, RIGHT * 0.3, UP * 0.3, color=GOLD, fill_opacity=0.8)
            .scale(0.5)
            .move_to(follow_text.get_center() + 2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.5
        )
        self.play(Rotate(triangles, angle=PI, run_time=1.0))
        
        self.wait(0.8)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            run_time=0.8
        )


# 运行命令:
# manim -pql triangle_important_segments.py TriangleImportantSegments  # 快速预览
# manim -qh triangle_important_segments.py TriangleImportantSegments   # 高质量渲染