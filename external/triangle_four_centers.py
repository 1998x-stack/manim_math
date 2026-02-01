"""
三角形四心教学动画 - Triangle Four Centers Animation
使用 Manim 创建的中学几何教学视频

内容: 外心、内心、重心、垂心的定义、构造和性质
目标观众: 初中/高中学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
  manim -pql triangle_four_centers.py TriangleFourCenters  # 快速预览
  manim -qh triangle_four_centers.py TriangleFourCenters   # 高质量
"""

from manim import *
import numpy as np


# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class GeometryCalculator:
    """几何计算工具类 - 所有几何计算的核心"""
    
    @staticmethod
    def circumcenter(A, B, C):
        """计算外心 - 三边垂直平分线交点"""
        ax, ay = A[0], A[1]
        bx, by = B[0], B[1]
        cx, cy = C[0], C[1]
        
        D = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        
        if abs(D) < 1e-10:
            return (A + B + C) / 3
        
        ux = ((ax**2 + ay**2) * (by - cy) + 
              (bx**2 + by**2) * (cy - ay) + 
              (cx**2 + cy**2) * (ay - by)) / D
        
        uy = ((ax**2 + ay**2) * (cx - bx) + 
              (bx**2 + by**2) * (ax - cx) + 
              (cx**2 + cy**2) * (bx - ax)) / D
        
        return np.array([ux, uy, 0])
    
    @staticmethod
    def incenter(A, B, C):
        """计算内心 - 加权平均"""
        a = np.linalg.norm(B - C)
        b = np.linalg.norm(C - A)
        c = np.linalg.norm(A - B)
        return (a * A + b * B + c * C) / (a + b + c)
    
    @staticmethod
    def centroid(A, B, C):
        """计算重心 - 简单平均"""
        return (A + B + C) / 3
    
    @staticmethod
    def orthocenter(A, B, C):
        """计算垂心 - 三条高线交点"""
        ax, ay = A[0], A[1]
        bx, by = B[0], B[1]
        cx, cy = C[0], C[1]
        
        det = (cy - by) * (ax - cx) - (bx - cx) * (cy - ay)
        
        if abs(det) < 1e-10:
            return GeometryCalculator.centroid(A, B, C)
        
        t1 = ((bx - ax) * (ax - cx) + (by - ay) * (ay - cy)) / det
        
        hx = ax + t1 * (cy - by)
        hy = ay + t1 * (bx - cx)
        
        return np.array([hx, hy, 0])
    
    @staticmethod
    def perpendicular_foot(point, line_start, line_end):
        """计算点到直线的垂足"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        t = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
        return line_start + t * line_vec
    
    @staticmethod
    def distance_point_to_line(point, line_start, line_end):
        """计算点到直线的距离"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        # 使用 2D 叉积
        cross_product = point_vec[0] * line_vec[1] - point_vec[1] * line_vec[0]
        return abs(cross_product) / np.linalg.norm(line_vec)


class TriangleFourCenters(Scene):
    """
    三角形四心教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 外心 (Circumcenter)
    3. 内心 (Incenter)
    4. 重心 (Centroid)
    5. 垂心 (Orthocenter)
    6. 四心汇总
    7. 欧拉线彩蛋
    8. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_CIRCUMCENTER = "#e74c3c"  # 红色 - 外心
        self.COLOR_INCENTER = "#3498db"      # 蓝色 - 内心
        self.COLOR_CENTROID = "#2ecc71"      # 绿色 - 重心
        self.COLOR_ORTHOCENTER = "#f39c12"   # 橙色 - 垂心
        self.COLOR_TRIANGLE = WHITE
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_HIGHLIGHT = YELLOW
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_circumcenter()
        self.show_incenter()
        self.show_centroid()
        self.show_orthocenter()
        self.show_summary()
        self.show_euler_line()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化三角形和所有几何元素"""
        # 基准三角形顶点 (使用斜三角形便于展示所有四心)
        self.A = np.array([-2.5, 1.5, 0])
        self.B = np.array([2.5, -0.5, 0])
        self.C = np.array([-1.0, -2.5, 0])
        
        # 缩放和偏移
        self.SCALE = 0.9
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
        
        # 预计算四心
        calc = GeometryCalculator
        self.circumcenter = calc.circumcenter(self.A, self.B, self.C)
        self.incenter = calc.incenter(self.A, self.B, self.C)
        self.centroid = calc.centroid(self.A, self.B, self.C)
        self.orthocenter = calc.orthocenter(self.A, self.B, self.C)
        
        # 创建三角形对象
        self.triangle = Polygon(self.A, self.B, self.C, 
                                color=self.COLOR_TRIANGLE, 
                                stroke_width=3)
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部,贯穿全片)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "一个三角形有几个特殊中心?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 三角形创建
        self.play(Create(self.triangle), run_time=1.0)
        
        # 四个神秘闪烁点
        centers = [
            self.circumcenter,
            self.incenter,
            self.centroid,
            self.orthocenter
        ]
        
        dots = VGroup(*[
            Dot(center, radius=0.08, color=YELLOW)
            for center in centers
        ])
        
        for dot in dots:
            self.play(FadeIn(dot, scale=0.5), run_time=0.2)
        
        # 提示文字
        hint = Text(
            "答案是: 四个!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(hint),
            FadeOut(dots),
            run_time=0.5
        )
    
    def show_circumcenter(self):
        """场景2: 外心 - 垂直平分线交点"""
        # 标题
        title = Text(
            "外心 Circumcenter",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_CIRCUMCENTER
        ).move_to(UP * 5.5)
        
        definition = Text(
            "三边垂直平分线的交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # AB的垂直平分线
        ab_line = Line(self.A, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(ab_line), run_time=0.5)
        
        m_ab_dot = Dot(self.M_AB, color=self.COLOR_AUXILIARY, radius=0.06)
        m_ab_label = Text("M", font="Noto Sans CJK SC", font_size=20).next_to(m_ab_dot, UP, buff=0.1)
        
        self.play(FadeIn(m_ab_dot), FadeIn(m_ab_label), run_time=0.4)
        
        # 垂直方向
        dir_AB = self.B - self.A
        perp_AB = np.array([-dir_AB[1], dir_AB[0], 0])
        perp_AB_normalized = perp_AB / np.linalg.norm(perp_AB)
        
        extension_length = 3.0
        perp_line_1 = DashedLine(
            self.M_AB - perp_AB_normalized * extension_length,
            self.M_AB + perp_AB_normalized * extension_length,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        explain_1 = Text(
            "垂直平分线: 过中点且垂直",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Create(perp_line_1), FadeIn(explain_1), run_time=0.8)
        self.play(ab_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        
        # BC的垂直平分线
        bc_line = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(bc_line), run_time=0.5)
        
        m_bc_dot = Dot(self.M_BC, color=self.COLOR_AUXILIARY, radius=0.06)
        self.play(FadeIn(m_bc_dot), run_time=0.3)
        
        dir_BC = self.C - self.B
        perp_BC = np.array([-dir_BC[1], dir_BC[0], 0])
        perp_BC_normalized = perp_BC / np.linalg.norm(perp_BC)
        
        perp_line_2 = DashedLine(
            self.M_BC - perp_BC_normalized * extension_length,
            self.M_BC + perp_BC_normalized * extension_length,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(perp_line_2), run_time=0.8)
        self.play(bc_line.animate.set_color(self.COLOR_TRIANGLE), FadeOut(explain_1), run_time=0.3)
        self.play(FadeOut(ab_line), FadeOut(bc_line), run_time=0.2)
        
        # 外心O
        o_dot = Dot(self.circumcenter, color=self.COLOR_CIRCUMCENTER, radius=0.12)
        o_label = Text("O", font="Noto Sans CJK SC", font_size=24, 
                      color=self.COLOR_CIRCUMCENTER).next_to(o_dot, RIGHT, buff=0.15)
        o_label_2 = Text("外心", font="Noto Sans CJK SC", font_size=18, 
                        color=self.COLOR_CIRCUMCENTER).next_to(o_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(o_dot, scale=0.5), run_time=0.5)
        self.play(Flash(o_dot, color=self.COLOR_CIRCUMCENTER, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(o_label), FadeIn(o_label_2), run_time=0.4)
        
        # 外接圆
        radius = np.linalg.norm(self.circumcenter - self.A)
        circumcircle = Circle(
            radius=radius,
            color=self.COLOR_CIRCUMCENTER,
            stroke_width=2
        ).move_to(self.circumcenter)
        
        self.play(Create(circumcircle), run_time=1.5)
        
        # 半径
        radii = VGroup(
            DashedLine(self.circumcenter, self.A, color=self.COLOR_AUXILIARY, dash_length=0.08),
            DashedLine(self.circumcenter, self.B, color=self.COLOR_AUXILIARY, dash_length=0.08),
            DashedLine(self.circumcenter, self.C, color=self.COLOR_AUXILIARY, dash_length=0.08)
        )
        
        self.play(Create(radii), run_time=0.8)
        
        property_text = Text(
            "到三顶点距离相等",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(property_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(perp_line_1),
            FadeOut(perp_line_2),
            FadeOut(m_ab_dot),
            FadeOut(m_ab_label),
            FadeOut(m_bc_dot),
            FadeOut(circumcircle),
            FadeOut(radii),
            FadeOut(property_text),
            FadeOut(o_label),
            FadeOut(o_label_2),
            run_time=0.6
        )
        
        # 保留外心点但变小
        self.o_small = Dot(self.circumcenter, color=self.COLOR_CIRCUMCENTER, 
                          radius=0.05, fill_opacity=0.5)
        self.play(Transform(o_dot, self.o_small), run_time=0.3)
        self.remove(o_dot)
        self.add(self.o_small)
    
    def show_incenter(self):
        """场景3: 内心 - 角平分线交点"""
        title = Text(
            "内心 Incenter",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_INCENTER
        ).move_to(UP * 5.5)
        
        definition = Text(
            "三条角平分线的交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # 角A的角平分线 - 使用角平分线定理计算交点
        t = self.c / (self.b + self.c)
        D_point = self.B + t * (self.C - self.B)
        
        angle_bisector_1 = DashedLine(
            self.A,
            D_point,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        explain_1 = Text(
            "角平分线: 平分角度",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Create(angle_bisector_1), FadeIn(explain_1), run_time=1.0)
        
        # 角B的角平分线
        t = self.a / (self.a + self.c)
        E_point = self.C + t * (self.A - self.C)
        
        angle_bisector_2 = DashedLine(
            self.B,
            E_point,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(angle_bisector_2), FadeOut(explain_1), run_time=0.8)
        
        # 内心I
        i_dot = Dot(self.incenter, color=self.COLOR_INCENTER, radius=0.12)
        i_label = Text("I", font="Noto Sans CJK SC", font_size=24, 
                      color=self.COLOR_INCENTER).next_to(i_dot, RIGHT, buff=0.15)
        i_label_2 = Text("内心", font="Noto Sans CJK SC", font_size=18, 
                        color=self.COLOR_INCENTER).next_to(i_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(i_dot, scale=0.5), run_time=0.5)
        self.play(Flash(i_dot, color=self.COLOR_INCENTER, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(i_label), FadeIn(i_label_2), run_time=0.4)
        
        # 内切圆
        calc = GeometryCalculator
        inradius = calc.distance_point_to_line(self.incenter, self.B, self.C)
        
        incircle = Circle(
            radius=inradius,
            color=self.COLOR_INCENTER,
            stroke_width=2
        ).move_to(self.incenter)
        
        self.play(Create(incircle), run_time=1.5)
        
        # 到三边的垂线
        foot_BC = calc.perpendicular_foot(self.incenter, self.B, self.C)
        foot_CA = calc.perpendicular_foot(self.incenter, self.C, self.A)
        foot_AB = calc.perpendicular_foot(self.incenter, self.A, self.B)
        
        perpendiculars = VGroup(
            DashedLine(self.incenter, foot_BC, color=self.COLOR_AUXILIARY, dash_length=0.08),
            DashedLine(self.incenter, foot_CA, color=self.COLOR_AUXILIARY, dash_length=0.08),
            DashedLine(self.incenter, foot_AB, color=self.COLOR_AUXILIARY, dash_length=0.08)
        )
        
        self.play(Create(perpendiculars), run_time=0.8)
        
        property_text = Text(
            "到三边距离相等",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(property_text), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(angle_bisector_1),
            FadeOut(angle_bisector_2),
            FadeOut(incircle),
            FadeOut(perpendiculars),
            FadeOut(property_text),
            FadeOut(i_label),
            FadeOut(i_label_2),
            run_time=0.6
        )
        
        self.i_small = Dot(self.incenter, color=self.COLOR_INCENTER, 
                          radius=0.05, fill_opacity=0.5)
        self.play(Transform(i_dot, self.i_small), run_time=0.3)
        self.remove(i_dot)
        self.add(self.i_small)
    
    def show_centroid(self):
        """场景4: 重心 - 中线交点"""
        title = Text(
            "重心 Centroid",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_CENTROID
        ).move_to(UP * 5.5)
        
        definition = Text(
            "三条中线的交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        # 中线AM
        m_bc_dot = Dot(self.M_BC, color=self.COLOR_AUXILIARY, radius=0.06)
        m_bc_label = Text("M", font="Noto Sans CJK SC", font_size=20).next_to(m_bc_dot, DOWN, buff=0.1)
        
        self.play(FadeIn(m_bc_dot), FadeIn(m_bc_label), run_time=0.4)
        
        median_1 = Line(self.A, self.M_BC, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        explain_1 = Text(
            "中线: 顶点到对边中点",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Create(median_1), FadeIn(explain_1), run_time=1.0)
        
        # 中线BN
        m_ca_dot = Dot(self.M_CA, color=self.COLOR_AUXILIARY, radius=0.06)
        self.play(FadeIn(m_ca_dot), run_time=0.3)
        
        median_2 = Line(self.B, self.M_CA, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        self.play(Create(median_2), FadeOut(explain_1), run_time=0.8)
        
        # 重心G
        g_dot = Dot(self.centroid, color=self.COLOR_CENTROID, radius=0.12)
        g_label = Text("G", font="Noto Sans CJK SC", font_size=24, 
                      color=self.COLOR_CENTROID).next_to(g_dot, RIGHT, buff=0.15)
        g_label_2 = Text("重心", font="Noto Sans CJK SC", font_size=18, 
                        color=self.COLOR_CENTROID).next_to(g_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(g_dot, scale=0.5), run_time=0.5)
        self.play(Flash(g_dot, color=self.COLOR_CENTROID, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(g_label), FadeIn(g_label_2), run_time=0.4)
        
        # 2:1比例标注
        property_text = Text(
            "重心分中线为 2:1",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        property_text_2 = Text(
            "物理重心 (平衡点)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 6)
        
        self.play(
            FadeIn(property_text),
            FadeIn(property_text_2),
            run_time=1.0
        )
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(median_1),
            FadeOut(median_2),
            FadeOut(m_bc_dot),
            FadeOut(m_bc_label),
            FadeOut(m_ca_dot),
            FadeOut(property_text),
            FadeOut(property_text_2),
            FadeOut(g_label),
            FadeOut(g_label_2),
            run_time=0.6
        )
        
        self.g_small = Dot(self.centroid, color=self.COLOR_CENTROID, 
                          radius=0.05, fill_opacity=0.5)
        self.play(Transform(g_dot, self.g_small), run_time=0.3)
        self.remove(g_dot)
        self.add(self.g_small)
    
    def show_orthocenter(self):
        """场景5: 垂心 - 高线交点"""
        title = Text(
            "垂心 Orthocenter",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_ORTHOCENTER
        ).move_to(UP * 5.5)
        
        definition = Text(
            "三条高线的交点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.8)
        
        self.play(Write(title), FadeIn(definition), run_time=0.8)
        
        calc = GeometryCalculator
        
        # 从A到BC的高
        bc_line = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(bc_line), run_time=0.5)
        
        foot_D = calc.perpendicular_foot(self.A, self.B, self.C)
        altitude_1 = DashedLine(self.A, foot_D, color=self.COLOR_AUXILIARY, dash_length=0.1)
        
        # 直角标记
        right_angle_1 = self.create_right_angle_mark(foot_D, self.A, self.B, size=0.15)
        
        explain_1 = Text(
            "高线: 顶点到对边的垂线",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(Create(altitude_1), FadeIn(right_angle_1), FadeIn(explain_1), run_time=1.0)
        self.play(bc_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        
        # 从B到CA的高
        ca_line = Line(self.C, self.A, color=self.COLOR_HIGHLIGHT, stroke_width=4)
        self.play(Create(ca_line), FadeOut(bc_line), run_time=0.5)
        
        foot_E = calc.perpendicular_foot(self.B, self.C, self.A)
        altitude_2 = DashedLine(self.B, foot_E, color=self.COLOR_AUXILIARY, dash_length=0.1)
        
        right_angle_2 = self.create_right_angle_mark(foot_E, self.B, self.C, size=0.15)
        
        self.play(Create(altitude_2), FadeIn(right_angle_2), FadeOut(explain_1), run_time=0.8)
        self.play(ca_line.animate.set_color(self.COLOR_TRIANGLE), run_time=0.3)
        self.play(FadeOut(ca_line), run_time=0.2)
        
        # 垂心H
        h_dot = Dot(self.orthocenter, color=self.COLOR_ORTHOCENTER, radius=0.12)
        h_label = Text("H", font="Noto Sans CJK SC", font_size=24, 
                      color=self.COLOR_ORTHOCENTER).next_to(h_dot, RIGHT, buff=0.15)
        h_label_2 = Text("垂心", font="Noto Sans CJK SC", font_size=18, 
                        color=self.COLOR_ORTHOCENTER).next_to(h_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(h_dot, scale=0.5), run_time=0.5)
        self.play(Flash(h_dot, color=self.COLOR_ORTHOCENTER, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(h_label), FadeIn(h_label_2), run_time=0.4)
        
        # 第三条高
        foot_F = calc.perpendicular_foot(self.C, self.A, self.B)
        altitude_3 = DashedLine(self.C, foot_F, color=self.COLOR_AUXILIARY, dash_length=0.1)
        
        property_text = Text(
            "三条高线共点!",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(Create(altitude_3), FadeIn(property_text), run_time=1.0)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(altitude_1),
            FadeOut(altitude_2),
            FadeOut(altitude_3),
            FadeOut(right_angle_1),
            FadeOut(right_angle_2),
            FadeOut(property_text),
            FadeOut(h_label),
            FadeOut(h_label_2),
            run_time=0.6
        )
        
        self.h_small = Dot(self.orthocenter, color=self.COLOR_ORTHOCENTER, 
                          radius=0.05, fill_opacity=0.5)
        self.play(Transform(h_dot, self.h_small), run_time=0.3)
        self.remove(h_dot)
        self.add(self.h_small)
    
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
    
    def show_summary(self):
        """场景6: 四心汇总"""
        # 三角形缩小并移动
        triangle_small = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_TRIANGLE,
            stroke_width=2
        ).scale(0.6).move_to(UP * 3)
        
        # 重新计算缩放后的四心位置
        scale_factor = 0.6
        center_offset = UP * 3
        
        o_pos = (self.circumcenter - self.OFFSET) * scale_factor + center_offset
        i_pos = (self.incenter - self.OFFSET) * scale_factor + center_offset
        g_pos = (self.centroid - self.OFFSET) * scale_factor + center_offset
        h_pos = (self.orthocenter - self.OFFSET) * scale_factor + center_offset
        
        self.play(
            Transform(self.triangle, triangle_small),
            self.o_small.animate.move_to(o_pos).scale(2).set_opacity(1),
            self.i_small.animate.move_to(i_pos).scale(2).set_opacity(1),
            self.g_small.animate.move_to(g_pos).scale(2).set_opacity(1),
            self.h_small.animate.move_to(h_pos).scale(2).set_opacity(1),
            run_time=1.0
        )
        
        # 标注四心
        o_label = Text("O", font="Noto Sans CJK SC", font_size=18, 
                      color=self.COLOR_CIRCUMCENTER).next_to(self.o_small, RIGHT, buff=0.08)
        i_label = Text("I", font="Noto Sans CJK SC", font_size=18, 
                      color=self.COLOR_INCENTER).next_to(self.i_small, LEFT, buff=0.08)
        g_label = Text("G", font="Noto Sans CJK SC", font_size=18, 
                      color=self.COLOR_CENTROID).next_to(self.g_small, DOWN, buff=0.08)
        h_label = Text("H", font="Noto Sans CJK SC", font_size=18, 
                      color=self.COLOR_ORTHOCENTER).next_to(self.h_small, UP, buff=0.08)
        
        self.play(
            Flash(self.o_small, color=self.COLOR_CIRCUMCENTER),
            Flash(self.i_small, color=self.COLOR_INCENTER),
            Flash(self.g_small, color=self.COLOR_CENTROID),
            Flash(self.h_small, color=self.COLOR_ORTHOCENTER),
            run_time=0.8
        )
        
        self.play(
            FadeIn(o_label),
            FadeIn(i_label),
            FadeIn(g_label),
            FadeIn(h_label),
            run_time=0.5
        )
        
        # 四心特性卡片
        cards = VGroup()
        
        card_1 = self.create_center_card(
            "外心", "垂直平分线交点, 外接圆圆心",
            self.COLOR_CIRCUMCENTER, UP * 1
        )
        cards.add(card_1)
        
        card_2 = self.create_center_card(
            "内心", "角平分线交点, 内切圆圆心",
            self.COLOR_INCENTER, ORIGIN
        )
        cards.add(card_2)
        
        card_3 = self.create_center_card(
            "重心", "中线交点, 物理重心, 2:1比例",
            self.COLOR_CENTROID, DOWN * 1
        )
        cards.add(card_3)
        
        card_4 = self.create_center_card(
            "垂心", "高线交点",
            self.COLOR_ORTHOCENTER, DOWN * 2
        )
        cards.add(card_4)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.4)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 重点提示
        highlight = Text(
            "掌握四心, 轻松解题!",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(highlight, shift=UP * 0.3), run_time=0.6)
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(self.triangle),
            FadeOut(self.o_small),
            FadeOut(self.i_small),
            FadeOut(self.g_small),
            FadeOut(self.h_small),
            FadeOut(o_label),
            FadeOut(i_label),
            FadeOut(g_label),
            FadeOut(h_label),
            FadeOut(cards),
            FadeOut(highlight),
            run_time=0.6
        )
    
    def create_center_card(self, title, content, color, position, font_size_content=18):
        """创建四心特性卡片"""
        icon = Circle(radius=0.2, fill_color=color, fill_opacity=1, stroke_width=0)
        
        title_text = Text(
            title,
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        
        content_text = Text(
            content,
            font="Noto Sans CJK SC",
            font_size=font_size_content,
            color=GRAY_A
        )
        
        card = VGroup(icon, title_text, content_text).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        card.shift(LEFT * 10)
        
        return card
    
    def show_euler_line(self):
        """场景7: 欧拉线彩蛋"""
        # 重新设置几何
        self.triangle = Polygon(self.A, self.B, self.C, 
                               color=self.COLOR_TRIANGLE, 
                               stroke_width=3)
        
        self.o_small = Dot(self.circumcenter, color=self.COLOR_CIRCUMCENTER, radius=0.10)
        self.g_small = Dot(self.centroid, color=self.COLOR_CENTROID, radius=0.10)
        self.h_small = Dot(self.orthocenter, color=self.COLOR_ORTHOCENTER, radius=0.10)
        
        o_label = Text("O", font="Noto Sans CJK SC", font_size=20, 
                      color=self.COLOR_CIRCUMCENTER).next_to(self.o_small, RIGHT, buff=0.1)
        g_label = Text("G", font="Noto Sans CJK SC", font_size=20, 
                      color=self.COLOR_CENTROID).next_to(self.g_small, DOWN, buff=0.1)
        h_label = Text("H", font="Noto Sans CJK SC", font_size=20, 
                      color=self.COLOR_ORTHOCENTER).next_to(self.h_small, LEFT, buff=0.1)
        
        self.play(
            FadeIn(self.triangle),
            FadeIn(self.o_small),
            FadeIn(self.g_small),
            FadeIn(self.h_small),
            FadeIn(o_label),
            FadeIn(g_label),
            FadeIn(h_label),
            run_time=0.5
        )
        
        # 欧拉线
        euler_line = DashedLine(
            self.circumcenter - (self.orthocenter - self.circumcenter) * 0.2,
            self.orthocenter + (self.orthocenter - self.circumcenter) * 0.2,
            color=GOLD,
            dash_length=0.1,
            stroke_width=3
        )
        
        title = Text(
            "欧拉线",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        ).move_to(UP * 5.5)
        
        explanation = Text(
            "外心、重心、垂心共线!",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        formula = MathTex(
            r"OG : GH = 1 : 2",
            color=YELLOW,
            font_size=36
        ).move_to(DOWN * 5)
        
        self.play(Write(title), run_time=0.6)
        self.play(Create(euler_line), run_time=1.0)
        self.play(FadeIn(explanation), run_time=0.5)
        self.play(Write(formula), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(self.triangle),
            FadeOut(self.o_small),
            FadeOut(self.g_small),
            FadeOut(self.h_small),
            FadeOut(o_label),
            FadeOut(g_label),
            FadeOut(h_label),
            FadeOut(euler_line),
            FadeOut(title),
            FadeOut(explanation),
            FadeOut(formula),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景8: 片尾关注"""
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
            "关注我, 学更多几何技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 小三角形装饰
        triangles = VGroup(*[
            Polygon(ORIGIN, RIGHT * 0.3, UP * 0.3, 
                   color=GOLD, fill_opacity=0.8)
            .scale(0.5)
            .move_to(follow_text.get_center() + 2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.6
        )
        self.play(Rotate(triangles, angle=PI, run_time=1.5))
        
        # 四心图标快闪
        icon_size = 0.3
        icons = VGroup(
            Circle(radius=icon_size, color=self.COLOR_CIRCUMCENTER, fill_opacity=0.8).shift(LEFT * 2),
            Circle(radius=icon_size, color=self.COLOR_INCENTER, fill_opacity=0.8).shift(LEFT * 1),
            Circle(radius=icon_size, color=self.COLOR_CENTROID, fill_opacity=0.8),
            Circle(radius=icon_size, color=self.COLOR_ORTHOCENTER, fill_opacity=0.8).shift(RIGHT * 1)
        ).move_to(DOWN * 2.5)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.wait(1)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            FadeOut(icons),
            run_time=1.0
        )