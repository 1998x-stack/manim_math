"""
三角形的基本概念 - Triangle Basic Concepts
使用 Manim 创建的中学几何教学视频

内容: 三角形定义、基本元素(顶点/边/角)、按边分类、按角分类
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


class GeometryCalculator:
    """几何计算工具类 - 所有计算必须使用此类"""
    
    @staticmethod
    def midpoint(P1, P2):
        """计算中点"""
        return (P1 + P2) / 2
    
    @staticmethod
    def angle_at_vertex(A, B, C):
        """
        计算∠ABC的角度（弧度）
        B是顶点
        """
        BA = A - B
        BC = C - B
        cos_angle = np.dot(BA, BC) / (np.linalg.norm(BA) * np.linalg.norm(BC))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        return np.arccos(cos_angle)
    
    @staticmethod
    def perpendicular_foot(point, line_start, line_end):
        """计算点到直线的垂足"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        t = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
        return line_start + t * line_vec


class TriangleBasics(Scene):
    """
    三角形基本概念教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 三角形定义
    3. 三角形的基本元素
    4. 按边分类
    5. 按角分类
    6. 知识总结
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主三角形
        self.COLOR_VERTEX = "#e74c3c"         # 红色 - 顶点
        self.COLOR_EDGE = "#2ecc71"           # 绿色 - 边
        self.COLOR_ANGLE = "#f39c12"          # 橙色 - 角
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助
        self.COLOR_LABEL = WHITE              # 白色 - 标签
        self.COLOR_EQUAL_SIDE = "#9b59b6"     # 紫色 - 相等边
        self.COLOR_RIGHT_ANGLE = "#e74c3c"    # 红色 - 直角
        
        # 初始化所有几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_elements()
        self.scene_4_classification_by_sides()
        self.scene_5_classification_by_angles()
        self.scene_6_summary()
        self.scene_7_outro()
    
    def setup_geometry(self):
        """初始化所有几何数据 - 统一计算"""
        # 缩放和偏移
        self.SCALE = 0.9
        self.OFFSET = UP * 1.5
        
        # ========== 主三角形 (一般三角形) ==========
        self.A = np.array([-2.5, 0, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([2.5, -1, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([0, 2.5, 0]) * self.SCALE + self.OFFSET
        
        # 边长
        self.a = np.linalg.norm(self.B - self.C)  # BC
        self.b = np.linalg.norm(self.C - self.A)  # CA
        self.c = np.linalg.norm(self.A - self.B)  # AB
        
        # 角度 (弧度)
        self.angle_A = GeometryCalculator.angle_at_vertex(self.C, self.A, self.B)
        self.angle_B = GeometryCalculator.angle_at_vertex(self.A, self.B, self.C)
        self.angle_C = GeometryCalculator.angle_at_vertex(self.B, self.C, self.A)
        
        # ========== 等腰三角形 ==========
        self.A_iso = np.array([0, 2, 0]) * self.SCALE + self.OFFSET
        self.B_iso = np.array([-1.5, -1, 0]) * self.SCALE + self.OFFSET
        self.C_iso = np.array([1.5, -1, 0]) * self.SCALE + self.OFFSET
        
        # ========== 等边三角形 ==========
        eq_side = 3 * self.SCALE
        self.A_eq = np.array([0, eq_side * np.sqrt(3)/2, 0]) + self.OFFSET
        self.B_eq = np.array([-eq_side/2, 0, 0]) + self.OFFSET
        self.C_eq = np.array([eq_side/2, 0, 0]) + self.OFFSET
        
        # ========== 直角三角形 ==========
        self.A_rt = np.array([-2, -1, 0]) * self.SCALE + self.OFFSET
        self.B_rt = np.array([2, -1, 0]) * self.SCALE + self.OFFSET
        self.C_rt = np.array([2, 2, 0]) * self.SCALE + self.OFFSET
        
        # ========== 锐角三角形 (接近等边但不完全相等) ==========
        self.A_acute = np.array([0, 2.2, 0]) * self.SCALE + self.OFFSET
        self.B_acute = np.array([-2, -0.8, 0]) * self.SCALE + self.OFFSET
        self.C_acute = np.array([1.8, -1, 0]) * self.SCALE + self.OFFSET
        
        # ========== 钝角三角形 (角C是钝角 ~106°) ==========
        self.A_obtuse = np.array([-2, -1, 0]) * self.SCALE + self.OFFSET
        self.B_obtuse = np.array([2, -1, 0]) * self.SCALE + self.OFFSET
        self.C_obtuse = np.array([0.2, 0.5, 0]) * self.SCALE + self.OFFSET
        
        # 验证几何关系
        self.verify_geometry()
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证主三角形角度和
        angle_sum = self.angle_A + self.angle_B + self.angle_C
        if abs(angle_sum - np.pi) > epsilon:
            print(f"WARNING: 主三角形角度和错误! {np.degrees(angle_sum):.2f}° ≠ 180°")
        
        # 验证等腰三角形
        side_AB_iso = np.linalg.norm(self.B_iso - self.A_iso)
        side_AC_iso = np.linalg.norm(self.C_iso - self.A_iso)
        if abs(side_AB_iso - side_AC_iso) > epsilon:
            print(f"WARNING: 等腰三角形边长不相等! AB={side_AB_iso:.4f}, AC={side_AC_iso:.4f}")
        
        # 验证等边三角形
        side_AB_eq = np.linalg.norm(self.B_eq - self.A_eq)
        side_BC_eq = np.linalg.norm(self.C_eq - self.B_eq)
        side_CA_eq = np.linalg.norm(self.A_eq - self.C_eq)
        if not (abs(side_AB_eq - side_BC_eq) < epsilon and abs(side_BC_eq - side_CA_eq) < epsilon):
            print(f"WARNING: 等边三角形边长不相等!")
        
        # 验证直角三角形
        vec_BA = self.A_rt - self.B_rt
        vec_BC = self.C_rt - self.B_rt
        dot_product = np.dot(vec_BA[:2], vec_BC[:2])
        if abs(dot_product) > epsilon:
            print(f"WARNING: 直角三角形不垂直! 点积={dot_product:.6f}")
        
        print("✓ 几何验证完成")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
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
            "三角形，你真的了解吗？",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 三角形轮廓闪现
        triangle_outline = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        )
        
        self.play(Create(triangle_outline), run_time=0.6)
        
        # 三角形闪烁
        for _ in range(3):
            self.play(Flash(triangle_outline, color=self.COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.2)
        
        self.wait(0.5)
        
        # 清理
        self.play(FadeOut(hook_text), run_time=0.4)
        
        # 三角形变虚线
        triangle_dashed = DashedVMobject(triangle_outline, num_dashes=20)
        self.play(Transform(triangle_outline, triangle_dashed), run_time=0.3)
        self.remove(triangle_outline)
        self.triangle_outline = triangle_dashed
    
    def scene_2_definition(self):
        """场景2: 三角形定义 (5-12秒)"""
        # 标题
        title = Text(
            "什么是三角形？",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 5.5)
        
        definition = Text(
            "由三条线段首尾顺次相接围成的封闭图形",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.4)
        self.play(Write(definition), run_time=1.0)
        
        # 清空画布
        self.play(FadeOut(self.triangle_outline), run_time=0.3)
        
        # 动态构造: 顶点
        dot_A = Dot(self.A, color=self.COLOR_VERTEX, radius=0.1)
        dot_B = Dot(self.B, color=self.COLOR_VERTEX, radius=0.1)
        dot_C = Dot(self.C, color=self.COLOR_VERTEX, radius=0.1)
        
        self.play(FadeIn(dot_A, scale=0.5), run_time=0.3)
        self.play(FadeIn(dot_B, scale=0.5), run_time=0.3)
        self.play(FadeIn(dot_C, scale=0.5), run_time=0.3)
        
        # 连线
        edge_AB = Line(self.A, self.B, color=self.COLOR_PRIMARY, stroke_width=3)
        edge_BC = Line(self.B, self.C, color=self.COLOR_PRIMARY, stroke_width=3)
        edge_CA = Line(self.C, self.A, color=self.COLOR_PRIMARY, stroke_width=3)
        
        self.play(Create(edge_AB), run_time=0.5)
        self.play(Create(edge_BC), run_time=0.5)
        self.play(Create(edge_CA), run_time=0.5)
        
        # 形成封闭图形高亮
        triangle = Polygon(self.A, self.B, self.C, color=self.COLOR_PRIMARY, stroke_width=3)
        self.play(Indicate(triangle, color=self.COLOR_HIGHLIGHT), run_time=0.5)
        
        # 标注顶点
        label_A = Text("A", font="PingFang SC", font_size=24, color=WHITE).next_to(dot_A, DOWN + LEFT, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=24, color=WHITE).next_to(dot_B, DOWN + RIGHT, buff=0.15)
        label_C = Text("C", font="PingFang SC", font_size=24, color=WHITE).next_to(dot_C, UP, buff=0.15)
        
        self.play(Write(label_A), Write(label_B), Write(label_C), run_time=0.5)
        
        # 说明文字
        explain_text = Text(
            "记作 △ABC",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain_text), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(explain_text),
            run_time=0.4
        )
        
        # 保留元素
        self.triangle = triangle
        self.dots = VGroup(dot_A, dot_B, dot_C)
        self.labels = VGroup(label_A, label_B, label_C)
        self.edges = VGroup(edge_AB, edge_BC, edge_CA)
    
    def scene_3_elements(self):
        """场景3: 三角形的基本元素 (12-22秒)"""
        # 子场景3.1: 三个顶点
        title_vertex = Text(
            "三个顶点",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_VERTEX
        ).move_to(UP * 5.5)
        
        self.play(Write(title_vertex), run_time=0.5)
        
        # 顶点依次高亮
        for i, dot in enumerate(self.dots):
            self.play(
                dot.animate.scale(1.5).set_color(self.COLOR_VERTEX),
                run_time=0.5
            )
        
        self.play(
            Flash(self.dots[0], color=self.COLOR_VERTEX),
            Flash(self.dots[1], color=self.COLOR_VERTEX),
            Flash(self.dots[2], color=self.COLOR_VERTEX),
            run_time=0.5
        )
        
        # 恢复
        self.play(
            self.dots.animate.scale(1/1.5).set_color(self.COLOR_VERTEX),
            run_time=0.5
        )
        
        # 子场景3.2: 三条边
        title_edge = Text(
            "三条边",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_EDGE
        ).move_to(UP * 5.5)
        
        self.play(Transform(title_vertex, title_edge), run_time=0.5)
        
        # 边依次高亮并标注
        # 边AB (c)
        self.play(
            self.edges[0].animate.set_color(self.COLOR_EDGE).set_stroke(width=5),
            run_time=0.5
        )
        mid_AB = GeometryCalculator.midpoint(self.A, self.B)
        label_c = MathTex("c", font_size=24, color=WHITE).move_to(mid_AB + DOWN * 0.4)
        self.play(FadeIn(label_c), run_time=0.2)
        
        # 边BC (a)
        self.wait(0.2)
        self.play(
            self.edges[1].animate.set_color(self.COLOR_EDGE).set_stroke(width=5),
            run_time=0.5
        )
        mid_BC = GeometryCalculator.midpoint(self.B, self.C)
        label_a = MathTex("a", font_size=24, color=WHITE).move_to(mid_BC + RIGHT * 0.4)
        self.play(FadeIn(label_a), run_time=0.2)
        
        # 边CA (b)
        self.wait(0.2)
        self.play(
            self.edges[2].animate.set_color(self.COLOR_EDGE).set_stroke(width=5),
            run_time=0.5
        )
        mid_CA = GeometryCalculator.midpoint(self.C, self.A)
        label_b = MathTex("b", font_size=24, color=WHITE).move_to(mid_CA + LEFT * 0.4)
        self.play(FadeIn(label_b), run_time=0.2)
        
        # 说明对边关系
        edge_note = Text(
            "小写字母表示边，a对应顶点A的对边",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(edge_note), run_time=0.5)
        self.wait(0.6)
        
        # 边恢复原色
        self.play(
            self.edges.animate.set_color(self.COLOR_PRIMARY).set_stroke(width=3),
            FadeOut(edge_note),
            run_time=0.3
        )
        
        # 子场景3.3: 三个内角
        title_angle = Text(
            "三个内角",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_ANGLE
        ).move_to(UP * 5.5)
        
        self.play(Transform(title_vertex, title_angle), run_time=0.5)
        
        # 创建角度 - 使用 Angle.from_three_points
        # 角A: 从C到B (顶点A)
        angle_A = Angle.from_three_points(
            self.C, self.A, self.B,
            radius=0.5,
            color=self.COLOR_ANGLE,
            quadrant=(1, 1)
        )
        label_angle_A = MathTex(r"\angle A", font_size=20, color=WHITE).move_to(
            self.A + RIGHT * 0.8 + DOWN * 0.3
        )
        
        self.play(Create(angle_A), run_time=0.6)
        self.play(FadeIn(label_angle_A), run_time=0.2)
        
        # 角B: 从A到C (顶点B)
        angle_B = Angle.from_three_points(
            self.A, self.B, self.C,
            radius=0.5,
            color=self.COLOR_ANGLE,
            quadrant=(1, 1)
        )
        label_angle_B = MathTex(r"\angle B", font_size=20, color=WHITE).move_to(
            self.B + LEFT * 0.8 + DOWN * 0.3
        )
        
        self.play(Create(angle_B), run_time=0.6)
        self.play(FadeIn(label_angle_B), run_time=0.2)
        
        # 角C: 从B到A (顶点C)
        angle_C = Angle.from_three_points(
            self.B, self.C, self.A,
            radius=0.5,
            color=self.COLOR_ANGLE,
            quadrant=(1, 1)
        )
        label_angle_C = MathTex(r"\angle C", font_size=20, color=WHITE).move_to(
            self.C + UP * 0.6
        )
        
        self.play(Create(angle_C), run_time=0.6)
        self.play(FadeIn(label_angle_C), run_time=0.2)
        
        # 说明
        notation_text = Text(
            "△ABC 表示这个三角形",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(notation_text), run_time=0.5)
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(title_vertex),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(label_c),
            FadeOut(label_angle_A),
            FadeOut(label_angle_B),
            FadeOut(label_angle_C),
            FadeOut(notation_text),
            FadeOut(angle_A),
            FadeOut(angle_B),
            FadeOut(angle_C),
            run_time=0.4
        )
    
    def scene_4_classification_by_sides(self):
        """场景4: 按边分类 (22-35秒)"""
        # 主三角形缩小移到左上角
        small_triangle = VGroup(self.triangle, self.dots, self.labels, self.edges)
        self.play(
            small_triangle.animate.scale(0.4).to_corner(UL).shift(DOWN * 0.5),
            run_time=0.6
        )
        
        # 分类标题
        classification_title = Text(
            "三角形的分类 - 按边",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(classification_title), run_time=0.6)
        
        # 子场景4.1: 不等边三角形
        tri_scalene = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).scale(0.7).move_to(UP * 2)
        
        self.play(Create(tri_scalene), run_time=0.8)
        
        # 标注边长
        edge_info = Text(
            f"a={self.a:.1f}, b={self.b:.1f}, c={self.c:.1f}",
            font="PingFang SC",
            font_size=18,
            color=GRAY_A
        ).next_to(tri_scalene, DOWN, buff=0.3)
        
        label_scalene = Text(
            "不等边三角形",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_PRIMARY
        ).next_to(edge_info, DOWN, buff=0.2)
        
        explain_scalene = Text(
            "三条边长度都不相等",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).next_to(label_scalene, DOWN, buff=0.15)
        
        self.play(
            Write(edge_info),
            FadeIn(label_scalene),
            FadeIn(explain_scalene),
            run_time=0.8
        )
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(tri_scalene),
            FadeOut(edge_info),
            FadeOut(label_scalene),
            FadeOut(explain_scalene),
            run_time=0.3
        )
        
        # 子场景4.2: 等腰三角形
        tri_isosceles = Polygon(
            self.A_iso, self.B_iso, self.C_iso,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).scale(0.7).move_to(UP * 2)
        
        self.play(Create(tri_isosceles), run_time=0.8)
        
        # 标注相等的边
        edge_AB_iso = Line(
            tri_isosceles.get_vertices()[0],
            tri_isosceles.get_vertices()[1],
            color=self.COLOR_EQUAL_SIDE,
            stroke_width=5
        )
        edge_AC_iso = Line(
            tri_isosceles.get_vertices()[0],
            tri_isosceles.get_vertices()[2],
            color=self.COLOR_EQUAL_SIDE,
            stroke_width=5
        )
        
        self.play(
            Create(edge_AB_iso),
            Create(edge_AC_iso),
            run_time=0.7
        )
        
        # 相等标记 (短横线)
        mid_AB_iso = (tri_isosceles.get_vertices()[0] + tri_isosceles.get_vertices()[1]) / 2
        mid_AC_iso = (tri_isosceles.get_vertices()[0] + tri_isosceles.get_vertices()[2]) / 2
        
        # 计算垂直方向
        dir_AB = tri_isosceles.get_vertices()[1] - tri_isosceles.get_vertices()[0]
        perp_AB = np.array([-dir_AB[1], dir_AB[0], 0])
        perp_AB = perp_AB / np.linalg.norm(perp_AB) * 0.15
        
        dir_AC = tri_isosceles.get_vertices()[2] - tri_isosceles.get_vertices()[0]
        perp_AC = np.array([-dir_AC[1], dir_AC[0], 0])
        perp_AC = perp_AC / np.linalg.norm(perp_AC) * 0.15
        
        mark_AB = Line(
            mid_AB_iso - perp_AB,
            mid_AB_iso + perp_AB,
            color=WHITE,
            stroke_width=3
        )
        mark_AC = Line(
            mid_AC_iso - perp_AC,
            mid_AC_iso + perp_AC,
            color=WHITE,
            stroke_width=3
        )
        
        self.play(Create(mark_AB), Create(mark_AC), run_time=0.3)
        
        label_isosceles = Text(
            "等腰三角形",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_PRIMARY
        ).next_to(tri_isosceles, DOWN, buff=0.5)
        
        explain_isosceles = Text(
            "有两条边相等",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).next_to(label_isosceles, DOWN, buff=0.15)
        
        self.play(
            FadeIn(label_isosceles),
            FadeIn(explain_isosceles),
            run_time=0.5
        )
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(tri_isosceles),
            FadeOut(edge_AB_iso),
            FadeOut(edge_AC_iso),
            FadeOut(mark_AB),
            FadeOut(mark_AC),
            FadeOut(label_isosceles),
            FadeOut(explain_isosceles),
            run_time=0.3
        )
        
        # 子场景4.3: 等边三角形
        tri_equilateral = Polygon(
            self.A_eq, self.B_eq, self.C_eq,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).scale(0.6).move_to(UP * 2)
        
        self.play(Create(tri_equilateral), run_time=0.8)
        
        # 三边全部高亮
        edges_eq = VGroup(
            Line(tri_equilateral.get_vertices()[0], tri_equilateral.get_vertices()[1], color=self.COLOR_EQUAL_SIDE, stroke_width=5),
            Line(tri_equilateral.get_vertices()[1], tri_equilateral.get_vertices()[2], color=self.COLOR_EQUAL_SIDE, stroke_width=5),
            Line(tri_equilateral.get_vertices()[2], tri_equilateral.get_vertices()[0], color=self.COLOR_EQUAL_SIDE, stroke_width=5)
        )
        
        self.play(Create(edges_eq), run_time=0.7)
        
        # 三边相等标记 (每条边两道短横线)
        marks_eq = VGroup()
        for i in range(3):
            v1 = tri_equilateral.get_vertices()[i]
            v2 = tri_equilateral.get_vertices()[(i+1)%3]
            mid = (v1 + v2) / 2
            
            direction = v2 - v1
            perp = np.array([-direction[1], direction[0], 0])
            perp = perp / np.linalg.norm(perp) * 0.15
            
            # 两道短横线
            for offset in [-0.1, 0.1]:
                mark = Line(
                    mid + direction / np.linalg.norm(direction) * offset - perp,
                    mid + direction / np.linalg.norm(direction) * offset + perp,
                    color=WHITE,
                    stroke_width=3
                )
                marks_eq.add(mark)
        
        self.play(Create(marks_eq), run_time=0.3)
        
        label_equilateral = Text(
            "等边三角形",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_PRIMARY
        ).next_to(tri_equilateral, DOWN, buff=0.5)
        
        explain_equilateral = Text(
            "三条边都相等，三个角都是60°",
            font="PingFang SC",
            font_size=18,
            color=GRAY_B
        ).next_to(label_equilateral, DOWN, buff=0.15)
        
        self.play(
            FadeIn(label_equilateral),
            FadeIn(explain_equilateral),
            run_time=0.5
        )
        
        # 角度标注
        angle_labels_eq = VGroup(
            MathTex(r"60^\circ", font_size=18, color=self.COLOR_ANGLE).move_to(tri_equilateral.get_vertices()[0] + DOWN * 0.5),
            MathTex(r"60^\circ", font_size=18, color=self.COLOR_ANGLE).move_to(tri_equilateral.get_vertices()[1] + UP * 0.3 + LEFT * 0.3),
            MathTex(r"60^\circ", font_size=18, color=self.COLOR_ANGLE).move_to(tri_equilateral.get_vertices()[2] + UP * 0.3 + RIGHT * 0.3)
        )
        
        self.play(FadeIn(angle_labels_eq), run_time=0.5)
        self.wait(1.2)
        
        # 清理
        self.play(
            FadeOut(tri_equilateral),
            FadeOut(edges_eq),
            FadeOut(marks_eq),
            FadeOut(label_equilateral),
            FadeOut(explain_equilateral),
            FadeOut(angle_labels_eq),
            FadeOut(classification_title),
            FadeOut(small_triangle),
            run_time=0.5
        )
    
    def scene_5_classification_by_angles(self):
        """场景5: 按角分类 (35-48秒)"""
        # 分类标题
        classification_title2 = Text(
            "三角形的分类 - 按角",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6)
        
        self.play(Write(classification_title2), run_time=0.6)
        
        # 子场景5.1: 锐角三角形
        tri_acute = Polygon(
            self.A_acute, self.B_acute, self.C_acute,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).scale(0.7).move_to(UP * 2)
        
        self.play(Create(tri_acute), run_time=0.8)
        
        # 角度
        angle_A_acute = GeometryCalculator.angle_at_vertex(self.C_acute, self.A_acute, self.B_acute)
        angle_B_acute = GeometryCalculator.angle_at_vertex(self.A_acute, self.B_acute, self.C_acute)
        angle_C_acute = GeometryCalculator.angle_at_vertex(self.B_acute, self.C_acute, self.A_acute)
        
        # 标注角度
        angles_acute = VGroup(
            Angle.from_three_points(self.C_acute, self.A_acute, self.B_acute, radius=0.35, color=self.COLOR_ANGLE),
            Angle.from_three_points(self.A_acute, self.B_acute, self.C_acute, radius=0.35, color=self.COLOR_ANGLE),
            Angle.from_three_points(self.B_acute, self.C_acute, self.A_acute, radius=0.35, color=self.COLOR_ANGLE)
        ).scale(0.7).move_to(tri_acute.get_center())
        
        # 依次高亮
        for angle in angles_acute:
            self.play(Flash(angle, color=self.COLOR_ANGLE), run_time=0.35)
        
        angle_values = Text(
            f"{np.degrees(angle_A_acute):.0f}°, {np.degrees(angle_B_acute):.0f}°, {np.degrees(angle_C_acute):.0f}°",
            font="PingFang SC",
            font_size=18,
            color=GRAY_A
        ).next_to(tri_acute, DOWN, buff=0.3)
        
        label_acute = Text(
            "锐角三角形",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_PRIMARY
        ).next_to(angle_values, DOWN, buff=0.2)
        
        explain_acute = Text(
            "三个角都小于90°",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).next_to(label_acute, DOWN, buff=0.15)
        
        self.play(
            Write(angle_values),
            FadeIn(label_acute),
            FadeIn(explain_acute),
            run_time=0.8
        )
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(tri_acute),
            FadeOut(angles_acute),
            FadeOut(angle_values),
            FadeOut(label_acute),
            FadeOut(explain_acute),
            run_time=0.3
        )
        
        # 子场景5.2: 直角三角形
        tri_right = Polygon(
            self.A_rt, self.B_rt, self.C_rt,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).scale(0.7).move_to(UP * 2)
        
        self.play(Create(tri_right), run_time=0.8)
        
        # 直角标记
        # 创建直角 (B是直角顶点)
        line_BA = Line(tri_right.get_vertices()[1], tri_right.get_vertices()[0])
        line_BC = Line(tri_right.get_vertices()[1], tri_right.get_vertices()[2])
        
        right_angle_mark = RightAngle(
            line_BA, line_BC,
            length=0.25,
            color=self.COLOR_RIGHT_ANGLE,
            quadrant=(1, 1)
        ).scale(0.7).move_to(tri_right.get_vertices()[1])
        
        self.play(Create(right_angle_mark), run_time=0.7)
        
        # 高亮直角
        self.play(
            right_angle_mark.animate.set_color(self.COLOR_RIGHT_ANGLE),
            run_time=0.5
        )
        
        # 标注90°
        label_90 = MathTex(r"90^\circ", font_size=20, color=self.COLOR_RIGHT_ANGLE).next_to(
            tri_right.get_vertices()[1], UR, buff=0.4
        )
        
        self.play(FadeIn(label_90), run_time=0.5)
        
        label_right = Text(
            "直角三角形",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_PRIMARY
        ).next_to(tri_right, DOWN, buff=0.5)
        
        explain_right = Text(
            "有一个角等于90°",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).next_to(label_right, DOWN, buff=0.15)
        
        self.play(
            FadeIn(label_right),
            FadeIn(explain_right),
            run_time=0.5
        )
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(tri_right),
            FadeOut(right_angle_mark),
            FadeOut(label_90),
            FadeOut(label_right),
            FadeOut(explain_right),
            run_time=0.3
        )
        
        # 子场景5.3: 钝角三角形
        tri_obtuse = Polygon(
            self.A_obtuse, self.B_obtuse, self.C_obtuse,
            color=self.COLOR_PRIMARY,
            stroke_width=3
        ).scale(0.7).move_to(UP * 2)
        
        self.play(Create(tri_obtuse), run_time=0.8)
        
        # 钝角
        angle_C_obtuse = GeometryCalculator.angle_at_vertex(self.B_obtuse, self.C_obtuse, self.A_obtuse)
        
        # 钝角标记
        obtuse_angle = Angle.from_three_points(
            self.B_obtuse, self.C_obtuse, self.A_obtuse,
            radius=0.4,
            color=self.COLOR_ANGLE
        ).scale(0.7).move_to(tri_obtuse.get_center())
        
        self.play(Create(obtuse_angle), run_time=0.7)
        
        # 钝角高亮
        self.play(Indicate(obtuse_angle, color=self.COLOR_HIGHLIGHT, scale_factor=1.2), run_time=0.7)
        
        # 角度标注
        angle_value = Text(
            f"{np.degrees(angle_C_obtuse):.0f}°",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_ANGLE
        ).next_to(tri_obtuse.get_vertices()[2], LEFT, buff=0.3)
        
        self.play(FadeIn(angle_value), run_time=0.5)
        
        label_obtuse = Text(
            "钝角三角形",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_PRIMARY
        ).next_to(tri_obtuse, DOWN, buff=0.5)
        
        explain_obtuse = Text(
            "有一个角大于90°",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        ).next_to(label_obtuse, DOWN, buff=0.15)
        
        self.play(
            FadeIn(label_obtuse),
            FadeIn(explain_obtuse),
            run_time=0.5
        )
        self.wait(0.8)
        
        # 清理
        self.play(
            FadeOut(tri_obtuse),
            FadeOut(obtuse_angle),
            FadeOut(angle_value),
            FadeOut(label_obtuse),
            FadeOut(explain_obtuse),
            FadeOut(classification_title2),
            run_time=0.5
        )
    
    def scene_6_summary(self):
        """场景6: 知识总结 (48-58秒)"""
        # 总结标题
        summary_title = Text(
            "三角形分类总结",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.6)
        
        # 左侧: 按边分类
        left_title = Text(
            "按边分类",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_EDGE
        ).move_to(LEFT * 2.5 + UP * 4.5)
        
        self.play(FadeIn(left_title), run_time=0.4)
        
        # 左侧卡片
        cards_left = self.create_summary_cards([
            ("不等边", "三边都不等"),
            ("等腰", "两边相等"),
            ("等边", "三边相等")
        ], start_pos=LEFT * 2.5 + UP * 3)
        
        for i, card in enumerate(cards_left):
            card.shift(LEFT * 10)  # 初始在左侧外
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
        
        # 右侧: 按角分类
        right_title = Text(
            "按角分类",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_ANGLE
        ).move_to(RIGHT * 2.5 + UP * 4.5)
        
        self.play(FadeIn(right_title), run_time=0.4)
        
        # 右侧卡片
        cards_right = self.create_summary_cards([
            ("锐角", "三角<90°"),
            ("直角", "一角=90°"),
            ("钝角", "一角>90°")
        ], start_pos=RIGHT * 2.5 + UP * 3)
        
        for i, card in enumerate(cards_right):
            card.shift(RIGHT * 10)  # 初始在右侧外
            self.play(card.animate.shift(LEFT * 10), run_time=0.5)
        
        # 全部卡片闪烁
        all_cards = VGroup(*cards_left, *cards_right)
        self.play(Indicate(all_cards, color=self.COLOR_HIGHLIGHT), run_time=0.7)
        
        # 重点提示
        key_point = Text(
            "掌握这6种三角形，轻松解题！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(key_point, scale=1.1), run_time=0.6)
        self.wait(3.5)
        
        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(left_title),
            FadeOut(right_title),
            FadeOut(all_cards),
            FadeOut(key_point),
            run_time=0.6
        )
    
    def create_summary_cards(self, items, start_pos):
        """创建总结卡片"""
        cards = VGroup()
        
        for i, (name, description) in enumerate(items):
            # 卡片背景
            card_bg = RoundedRectangle(
                width=3.5,
                height=0.8,
                corner_radius=0.1,
                fill_color="#2c3e50",
                fill_opacity=0.8,
                stroke_width=2,
                stroke_color=self.COLOR_PRIMARY
            )
            
            # 名称
            name_text = Text(
                name,
                font="PingFang SC",
                font_size=22,
                color=WHITE
            )
            
            # 描述
            desc_text = Text(
                description,
                font="PingFang SC",
                font_size=16,
                color=GRAY_A
            )
            
            # 组合
            content = VGroup(name_text, desc_text).arrange(RIGHT, buff=0.3)
            card = VGroup(card_bg, content)
            card.move_to(start_pos + DOWN * i * 1.2)
            
            cards.add(card)
        
        return cards
    
    def scene_7_outro(self):
        """场景7: 片尾关注 (58-65秒)"""
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
            "关注我，学更多几何知识！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 六个小三角形装饰
        triangles = VGroup(*[
            Polygon(ORIGIN, RIGHT * 0.3, UP * 0.3, color=GOLD, fill_opacity=0.8)
            .scale(0.5)
            .move_to(follow_text.get_center() + 2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0]))
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(tri, scale=0.5) for tri in triangles],
            run_time=0.6
        )
        self.play(Rotate(triangles, angle=PI, run_time=1.5))
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(triangles),
            run_time=1.0
        )


# 运行命令:
# manim -pql triangle_basics.py TriangleBasics  # 快速预览
# manim -qh triangle_basics.py TriangleBasics   # 高质量