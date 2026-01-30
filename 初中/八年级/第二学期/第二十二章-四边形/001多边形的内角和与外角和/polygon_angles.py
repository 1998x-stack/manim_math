"""
多边形的内角和与外角和 - Polygon Interior and Exterior Angles
使用 Manim 创建的八年级几何教学视频

内容: n边形内角和公式 (n-2)×180°, 外角和恒为360°
目标观众: 八年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np
from math import pi, cos, sin

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PolygonAngles(Scene):
    """
    多边形内角和与外角和教学动画场景
    
    场景顺序:
    1. 开场钩子
    2. 三角形引入
    3. 四边形分割
    4. 五边形分割
    5. 通用公式推导
    6. 外角和证明
    7. 总结与应用
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主图形
        self.COLOR_SECONDARY = "#e74c3c"      # 红色 - 内角
        self.COLOR_EXTERIOR = "#2ecc71"       # 绿色 - 外角
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助线
        self.COLOR_DIAGONAL = "#9b59b6"       # 紫色 - 对角线
        
        # 字体设置
        self.FONT_CHINESE = "Noto Sans CJK SC"
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_triangle()
        self.show_quadrilateral()
        self.show_pentagon()
        self.show_general_formula()
        self.show_exterior_angles()
        self.show_summary()
    
    def setup_geometry(self):
        """初始化所有多边形和几何元素"""
        # 基准参数
        self.POLYGON_RADIUS = 1.8
        self.MAIN_POSITION = UP * 1.5
        
        # 三角形顶点
        self.triangle_vertices = self.calculate_regular_polygon_vertices(3, self.POLYGON_RADIUS)
        
        # 四边形顶点
        self.square_vertices = self.calculate_regular_polygon_vertices(4, self.POLYGON_RADIUS)
        
        # 五边形顶点
        self.pentagon_vertices = self.calculate_regular_polygon_vertices(5, self.POLYGON_RADIUS)
        
        # 六边形顶点
        self.hexagon_vertices = self.calculate_regular_polygon_vertices(6, self.POLYGON_RADIUS)
        
        # 七边形顶点
        self.heptagon_vertices = self.calculate_regular_polygon_vertices(7, self.POLYGON_RADIUS)
        
        # 八边形顶点
        self.octagon_vertices = self.calculate_regular_polygon_vertices(8, self.POLYGON_RADIUS)
        
        print("✓ 几何初始化完成")
    
    def calculate_regular_polygon_vertices(self, n, radius, start_angle=PI/2):
        """
        计算正n边形的顶点坐标
        n: 边数
        radius: 外接圆半径
        start_angle: 起始角度（默认从顶部开始）
        """
        vertices = []
        for i in range(n):
            angle = start_angle + i * 2 * PI / n
            x = radius * cos(angle)
            y = radius * sin(angle)
            vertices.append(np.array([x, y, 0]))
        return vertices
    
    def show_opening(self):
        """场景1: 开场钩子"""
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "正五边形的内角和是多少?",
            font=self.FONT_CHINESE,
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(hook_text), run_time=1.2)
        
        # 多个多边形依次闪现
        shapes = VGroup()
        
        # 三角形
        triangle = Polygon(*self.triangle_vertices, color=self.COLOR_PRIMARY, stroke_width=3)
        triangle.scale(0.6).move_to(UP * 2)
        shapes.add(triangle)
        
        # 四边形
        square = Polygon(*self.square_vertices, color=self.COLOR_PRIMARY, stroke_width=3)
        square.scale(0.6).move_to(UP * 2)
        shapes.add(square)
        
        # 五边形
        pentagon = Polygon(*self.pentagon_vertices, color=self.COLOR_PRIMARY, stroke_width=3)
        pentagon.scale(0.6).move_to(UP * 2)
        shapes.add(pentagon)
        
        # 六边形
        hexagon = Polygon(*self.hexagon_vertices, color=self.COLOR_PRIMARY, stroke_width=3)
        hexagon.scale(0.6).move_to(UP * 2)
        shapes.add(hexagon)
        
        # 依次显示和隐藏
        for shape in shapes:
            self.play(FadeIn(shape, scale=0.8), run_time=0.4)
            self.play(FadeOut(shape, scale=1.2), run_time=0.4)
        
        # 问号跳动
        question_mark = Text("?", font_size=80, color=self.COLOR_HIGHLIGHT).move_to(UP * 2)
        self.play(FadeIn(question_mark, scale=0.5), run_time=0.3)
        self.play(Indicate(question_mark, scale_factor=1.3), run_time=0.6)
        
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(question_mark),
            run_time=0.5
        )
    
    def show_triangle(self):
        """场景2: 三角形引入"""
        # 标题
        title = Text(
            "从三角形开始",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 等边三角形
        triangle = Polygon(
            *self.triangle_vertices,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_to(self.MAIN_POSITION)
        
        self.play(Create(triangle), run_time=1.0)
        
        # 标记三个角
        angles = VGroup()
        angle_labels = VGroup()
        
        for i in range(3):
            # 计算角的位置
            vertex = triangle.get_vertices()[i]
            prev_vertex = triangle.get_vertices()[(i-1) % 3]
            next_vertex = triangle.get_vertices()[(i+1) % 3]
            
            # 创建角度弧
            angle_arc = self.create_angle_arc(vertex, prev_vertex, next_vertex, radius=0.3, color=self.COLOR_SECONDARY)
            angles.add(angle_arc)
            
            # 角度标签
            angle_center = vertex + (prev_vertex - vertex) * 0.15 + (next_vertex - vertex) * 0.15
            angle_center = angle_center / np.linalg.norm(angle_center - vertex) * 0.5 + vertex
            
            chinese_label = Text("60", font=self.FONT_CHINESE, font_size=20, color=WHITE)
            degree_symbol = MathTex(r"^\circ", font_size=20, color=WHITE)
            label_group = VGroup(chinese_label, degree_symbol).arrange(RIGHT, buff=0.05)
            label_group.move_to(angle_center)
            
            angle_labels.add(label_group)
        
        # 依次显示角度
        for angle, label in zip(angles, angle_labels):
            self.play(Create(angle), FadeIn(label), run_time=0.5)
        
        self.wait(0.3)
        
        # 公式
        formula_text = Text("60", font=self.FONT_CHINESE, font_size=28, color=WHITE)
        degree1 = MathTex(r"^\circ", font_size=28)
        plus1 = Text(" + 60", font=self.FONT_CHINESE, font_size=28, color=WHITE)
        degree2 = MathTex(r"^\circ", font_size=28)
        plus2 = Text(" + 60", font=self.FONT_CHINESE, font_size=28, color=WHITE)
        degree3 = MathTex(r"^\circ", font_size=28)
        equals = Text(" = 180", font=self.FONT_CHINESE, font_size=28, color=self.COLOR_HIGHLIGHT)
        degree4 = MathTex(r"^\circ", font_size=28, color=self.COLOR_HIGHLIGHT)
        
        formula = VGroup(
            formula_text, degree1, plus1, degree2, plus2, degree3, equals, degree4
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 3)
        
        self.play(Write(formula), run_time=1.5)
        self.play(Indicate(formula[-2:], scale_factor=1.2), run_time=0.8)
        
        self.wait(0.8)
        
        # 清理但保留小三角形
        small_triangle = triangle.copy().scale(0.3).move_to(UP * 6.5 + LEFT * 3)
        small_label = Text("3", font=self.FONT_CHINESE, font_size=16, color=GRAY_B).next_to(small_triangle, DOWN, buff=0.1)
        
        self.play(
            Transform(triangle, small_triangle),
            FadeOut(title),
            FadeOut(angles),
            FadeOut(angle_labels),
            FadeOut(formula),
            FadeIn(small_label),
            run_time=0.6
        )
        
        self.triangle_ref = VGroup(triangle, small_label)
    
    def create_angle_arc(self, vertex, point1, point2, radius=0.3, color=RED):
        """创建角度弧"""
        # 计算两个方向向量
        vec1 = point1 - vertex
        vec2 = point2 - vertex
        
        # 计算起始和结束角度
        angle1 = np.arctan2(vec1[1], vec1[0])
        angle2 = np.arctan2(vec2[1], vec2[0])
        
        # 确保逆时针方向
        if angle2 < angle1:
            angle2 += 2 * PI
        
        # 创建弧
        arc = Arc(
            radius=radius,
            start_angle=angle1,
            angle=angle2 - angle1,
            color=color,
            stroke_width=2
        ).move_arc_center_to(vertex)
        
        return arc
    
    def show_quadrilateral(self):
        """场景3: 四边形分割"""
        # 标题
        title = Text(
            "四边形的内角和",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 正方形
        square = Polygon(
            *self.square_vertices,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_to(self.MAIN_POSITION)
        
        self.play(Create(square), run_time=1.0)
        
        # 对角线
        vertices = square.get_vertices()
        diagonal = DashedLine(
            vertices[0], vertices[2],
            color=self.COLOR_DIAGONAL,
            dash_length=0.1,
            stroke_width=3
        )
        
        self.play(Create(diagonal), run_time=0.8)
        
        # 两个三角形分别闪烁
        triangle1_points = [vertices[0], vertices[1], vertices[2], vertices[0]]
        triangle1 = Polygon(*triangle1_points[:-1], color=self.COLOR_SECONDARY, fill_opacity=0.3, stroke_width=0)
        
        triangle2_points = [vertices[0], vertices[2], vertices[3], vertices[0]]
        triangle2 = Polygon(*triangle2_points[:-1], color=self.COLOR_EXTERIOR, fill_opacity=0.3, stroke_width=0)
        
        self.play(FadeIn(triangle1), run_time=0.4)
        self.play(FadeOut(triangle1), run_time=0.4)
        self.play(FadeIn(triangle2), run_time=0.4)
        self.play(FadeOut(triangle2), run_time=0.4)
        
        # 公式: 2 × 180° = 360°
        formula_parts = []
        formula_parts.append(Text("2", font=self.FONT_CHINESE, font_size=32, color=WHITE))
        formula_parts.append(MathTex(r"\times", font_size=32))
        formula_parts.append(Text("180", font=self.FONT_CHINESE, font_size=32, color=WHITE))
        formula_parts.append(MathTex(r"^\circ", font_size=32))
        formula_parts.append(Text(" = 360", font=self.FONT_CHINESE, font_size=32, color=self.COLOR_HIGHLIGHT))
        formula_parts.append(MathTex(r"^\circ", font_size=32, color=self.COLOR_HIGHLIGHT))
        
        formula = VGroup(*formula_parts).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.5)
        
        self.play(Write(formula), run_time=1.2)
        
        # 验证: 标记四个角
        explanation = Text(
            "正方形每个角90度",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理但保留小正方形
        small_square = square.copy().scale(0.3).move_to(UP * 6.5 + LEFT * 2)
        small_label = Text("4", font=self.FONT_CHINESE, font_size=16, color=GRAY_B).next_to(small_square, DOWN, buff=0.1)
        
        self.play(
            Transform(square, small_square),
            FadeOut(title),
            FadeOut(diagonal),
            FadeOut(formula),
            FadeOut(explanation),
            FadeIn(small_label),
            run_time=0.6
        )
        
        self.square_ref = VGroup(square, small_label)
    
    def show_pentagon(self):
        """场景4: 五边形分割"""
        # 标题
        title = Text(
            "五边形的内角和",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 正五边形
        pentagon = Polygon(
            *self.pentagon_vertices,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_to(self.MAIN_POSITION)
        
        self.play(Create(pentagon), run_time=1.0)
        
        # 顶点A标记
        vertices = pentagon.get_vertices()
        vertex_A = vertices[0]
        label_A = Text("A", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_HIGHLIGHT).next_to(vertex_A, UP, buff=0.2)
        
        self.play(FadeIn(label_A), run_time=0.4)
        
        # 从A引出对角线
        diagonals = VGroup()
        
        # A到C (顶点2)
        diagonal1 = DashedLine(
            vertices[0], vertices[2],
            color=self.COLOR_DIAGONAL,
            dash_length=0.1,
            stroke_width=3
        )
        diagonals.add(diagonal1)
        
        # A到D (顶点3)
        diagonal2 = DashedLine(
            vertices[0], vertices[3],
            color=self.COLOR_DIAGONAL,
            dash_length=0.1,
            stroke_width=3
        )
        diagonals.add(diagonal2)
        
        self.play(Create(diagonal1), run_time=0.6)
        self.wait(0.3)
        self.play(Create(diagonal2), run_time=0.6)
        
        # 三个三角形依次闪烁
        triangle1 = Polygon(vertices[0], vertices[1], vertices[2], color=self.COLOR_SECONDARY, fill_opacity=0.3, stroke_width=0)
        triangle2 = Polygon(vertices[0], vertices[2], vertices[3], color=self.COLOR_EXTERIOR, fill_opacity=0.3, stroke_width=0)
        triangle3 = Polygon(vertices[0], vertices[3], vertices[4], color=BLUE, fill_opacity=0.3, stroke_width=0)
        
        for tri in [triangle1, triangle2, triangle3]:
            self.play(FadeIn(tri), run_time=0.4)
            self.play(FadeOut(tri), run_time=0.3)
        
        # 公式: 3 × 180° = 540°
        formula_parts = []
        formula_parts.append(Text("3", font=self.FONT_CHINESE, font_size=32, color=WHITE))
        formula_parts.append(MathTex(r"\times", font_size=32))
        formula_parts.append(Text("180", font=self.FONT_CHINESE, font_size=32, color=WHITE))
        formula_parts.append(MathTex(r"^\circ", font_size=32))
        formula_parts.append(Text(" = 540", font=self.FONT_CHINESE, font_size=32, color=self.COLOR_HIGHLIGHT))
        formula_parts.append(MathTex(r"^\circ", font_size=32, color=self.COLOR_HIGHLIGHT))
        
        formula = VGroup(*formula_parts).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.5)
        
        self.play(Write(formula), run_time=1.2)
        
        # 关键观察
        observation = Text(
            "三角形数 = 边数 - 2",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(observation, shift=UP * 0.3), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        small_pentagon = pentagon.copy().scale(0.3).move_to(UP * 6.5 + LEFT * 1)
        small_label = Text("5", font=self.FONT_CHINESE, font_size=16, color=GRAY_B).next_to(small_pentagon, DOWN, buff=0.1)
        
        # 保留关键观察，移到顶部
        observation_top = observation.copy().scale(0.7).move_to(UP * 5.2)
        
        self.play(
            Transform(pentagon, small_pentagon),
            Transform(observation, observation_top),
            FadeOut(title),
            FadeOut(label_A),
            FadeOut(diagonals),
            FadeOut(formula),
            FadeIn(small_label),
            run_time=0.6
        )
        
        self.pentagon_ref = VGroup(pentagon, small_label)
        self.observation_ref = observation
    
    def show_general_formula(self):
        """场景5: 通用公式推导"""
        # 标题
        title = Text(
            "n边形内角和公式",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE
        ).move_to(UP * 6)
        
        self.play(
            FadeOut(self.observation_ref),
            FadeIn(title, shift=DOWN * 0.3),
            run_time=0.5
        )
        
        # 七边形
        heptagon = Polygon(
            *self.heptagon_vertices,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).move_to(self.MAIN_POSITION)
        
        self.play(Create(heptagon), run_time=1.0)
        
        # 从一个顶点引所有对角线
        vertices = heptagon.get_vertices()
        diagonals = VGroup()
        
        # 从顶点0到所有非相邻顶点
        for i in range(2, len(vertices) - 1):
            diagonal = DashedLine(
                vertices[0], vertices[i],
                color=self.COLOR_DIAGONAL,
                dash_length=0.08,
                stroke_width=2
            )
            diagonals.add(diagonal)
        
        self.play(
            *[Create(diag) for diag in diagonals],
            run_time=1.5,
            lag_ratio=0.2
        )
        
        # 三角形数量标注
        triangle_count = Text(
            "n - 2 个三角形",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(triangle_count, shift=UP * 0.3), run_time=0.8)
        
        self.wait(1.0)
        
        # 公式推导
        step1 = Text(
            "每个三角形内角和 = 180°",
            font=self.FONT_CHINESE,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(step1), run_time=0.8)
        self.wait(0.6)
        
        # 最终公式
        final_text = Text("内角和 = ", font=self.FONT_CHINESE, font_size=32, color=WHITE)
        final_formula = Text("(n-2)", font=self.FONT_CHINESE, font_size=32, color=self.COLOR_HIGHLIGHT)
        final_times = MathTex(r"\times", font_size=32)
        final_180 = Text("180", font=self.FONT_CHINESE, font_size=32, color=WHITE)
        final_degree = MathTex(r"^\circ", font_size=32)
        
        final = VGroup(
            final_text, final_formula, final_times, final_180, final_degree
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 6.5)
        
        self.play(
            FadeOut(step1),
            FadeOut(triangle_count),
            Write(final),
            run_time=1.5
        )
        
        # 框住公式强调
        box = SurroundingRectangle(final, color=self.COLOR_HIGHLIGHT, buff=0.15, stroke_width=3)
        self.play(Create(box), run_time=0.8)
        self.play(Indicate(VGroup(final, box), scale_factor=1.1), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理，保留公式到顶部
        formula_top = VGroup(final, box).copy().scale(0.65).move_to(UP * 5.5)
        
        self.play(
            Transform(VGroup(final, box), formula_top),
            FadeOut(title),
            FadeOut(heptagon),
            FadeOut(diagonals),
            run_time=0.6
        )
        
        self.interior_formula_ref = VGroup(final, box)
    
    def show_exterior_angles(self):
        """场景6: 外角和证明"""
        # 标题
        title = Text(
            "外角和的秘密",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE
        ).move_to(UP * 4)
        
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)
        
        # 五边形重新绘制
        pentagon = Polygon(
            *self.pentagon_vertices,
            color=self.COLOR_PRIMARY,
            stroke_width=4
        ).scale(0.9).move_to(UP * 0.5)
        
        self.play(Create(pentagon), run_time=1.0)
        
        vertices = pentagon.get_vertices()
        
        # 延长一条边示例
        side_start = vertices[0]
        side_end = vertices[1]
        extension_direction = (side_end - side_start) / np.linalg.norm(side_end - side_start)
        extension_point = side_end + extension_direction * 1.2
        
        extended_side = DashedLine(
            side_end, extension_point,
            color=self.COLOR_AUXILIARY,
            dash_length=0.08,
            stroke_width=2
        )
        
        self.play(Create(extended_side), run_time=0.6)
        
        # 标记外角
        # 外角是内角的补角
        prev_vertex = vertices[0]
        current_vertex = vertices[1]
        next_vertex = vertices[2]
        
        # 外角弧（从边的延长线到下一条边）
        exterior_arc = self.create_angle_arc(
            current_vertex,
            extension_point,
            next_vertex,
            radius=0.25,
            color=self.COLOR_EXTERIOR
        )
        
        self.play(Create(exterior_arc), run_time=0.6)
        
        # 说明文字
        explanation = Text(
            "外角 + 内角 = 180°",
            font=self.FONT_CHINESE,
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 2.5)
        
        self.play(FadeIn(explanation), run_time=0.5)
        
        self.wait(0.8)
        
        # 清理示例，准备展示所有外角
        self.play(
            FadeOut(extended_side),
            FadeOut(exterior_arc),
            FadeOut(explanation),
            run_time=0.4
        )
        
        # 创建所有外角
        exterior_angles = VGroup()
        
        for i in range(5):
            current = vertices[i]
            next_v = vertices[(i + 1) % 5]
            next_next = vertices[(i + 2) % 5]
            
            # 延长线方向
            edge_direction = (next_v - current) / np.linalg.norm(next_v - current)
            extension = next_v + edge_direction * 0.8
            
            # 外角弧
            ext_arc = self.create_angle_arc(
                next_v,
                extension,
                next_next,
                radius=0.2,
                color=self.COLOR_EXTERIOR
            )
            
            exterior_angles.add(ext_arc)
        
        # 依次显示外角
        for ext_angle in exterior_angles:
            self.play(Create(ext_angle), run_time=0.4)
        
        self.wait(0.5)
        
        # 外角"拆下"并移到中心拼成圆
        center = DOWN * 4
        circle_radius = 0.8
        
        # 创建扇形替代外角弧
        sectors = VGroup()
        angle_per_sector = 2 * PI / 5
        
        for i in range(5):
            sector = Sector(
                radius=circle_radius,
                start_angle=i * angle_per_sector,
                angle=angle_per_sector,
                color=self.COLOR_EXTERIOR,
                fill_opacity=0.6,
                stroke_width=2
            ).move_to(center)
            sectors.add(sector)
        
        # 动画：外角移动到扇形位置
        self.play(
            FadeOut(pentagon),
            *[ReplacementTransform(ext_angle, sector) for ext_angle, sector in zip(exterior_angles, sectors)],
            run_time=1.5
        )
        
        # 圆周标注
        circle_outline = Circle(radius=circle_radius, color=self.COLOR_EXTERIOR, stroke_width=3).move_to(center)
        self.play(Create(circle_outline), run_time=0.8)
        
        conclusion_text = Text("外角和 = ", font=self.FONT_CHINESE, font_size=32, color=WHITE)
        conclusion_value = Text("360", font=self.FONT_CHINESE, font_size=32, color=self.COLOR_HIGHLIGHT)
        conclusion_degree = MathTex(r"^\circ", font_size=32, color=self.COLOR_HIGHLIGHT)
        
        conclusion = VGroup(conclusion_text, conclusion_value, conclusion_degree).arrange(RIGHT, buff=0.1).move_to(DOWN * 6)
        
        self.play(Write(conclusion), run_time=1.2)
        
        # 强调
        self.play(
            Flash(VGroup(sectors, circle_outline), color=self.COLOR_EXTERIOR, flash_radius=1.2),
            Indicate(conclusion, scale_factor=1.2),
            run_time=1.0
        )
        
        # 重要说明
        note = Text(
            "与边数无关, 恒为360°!",
            font=self.FONT_CHINESE,
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7)
        
        self.play(FadeIn(note, shift=UP * 0.3), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(sectors),
            FadeOut(circle_outline),
            FadeOut(note),
            run_time=0.5
        )
        
        # 保留外角和公式到底部
        conclusion_bottom = conclusion.copy().scale(0.7).move_to(DOWN * 7)
        
        self.play(
            Transform(conclusion, conclusion_bottom),
            run_time=0.4
        )
        
        self.exterior_formula_ref = conclusion
    
    def show_summary(self):
        """场景7: 总结与应用"""
        # 标题
        title = Text(
            "公式总结",
            font=self.FONT_CHINESE,
            font_size=40,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 3)
        
        self.play(Write(title), run_time=0.8)
        
        # 公式卡片
        # 卡片1: 内角和
        card1_icon = Circle(radius=0.2, fill_color=self.COLOR_SECONDARY, fill_opacity=1, stroke_width=0)
        card1_title = Text("内角和", font=self.FONT_CHINESE, font_size=26, color=WHITE)
        card1_formula_text = Text("(n-2)", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_HIGHLIGHT)
        card1_times = MathTex(r"\times", font_size=24)
        card1_180 = Text("180", font=self.FONT_CHINESE, font_size=24, color=WHITE)
        card1_degree = MathTex(r"^\circ", font_size=24)
        card1_formula = VGroup(card1_formula_text, card1_times, card1_180, card1_degree).arrange(RIGHT, buff=0.05)
        card1 = VGroup(card1_icon, card1_title, card1_formula).arrange(RIGHT, buff=0.3).move_to(UP * 1.5)
        card1.shift(LEFT * 10)  # 初始位置在左侧外
        
        # 卡片2: 外角和
        card2_icon = Circle(radius=0.2, fill_color=self.COLOR_EXTERIOR, fill_opacity=1, stroke_width=0)
        card2_title = Text("外角和", font=self.FONT_CHINESE, font_size=26, color=WHITE)
        card2_value = Text("360", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_HIGHLIGHT)
        card2_degree = MathTex(r"^\circ", font_size=24, color=self.COLOR_HIGHLIGHT)
        card2_formula = VGroup(card2_value, card2_degree).arrange(RIGHT, buff=0.05)
        card2 = VGroup(card2_icon, card2_title, card2_formula).arrange(RIGHT, buff=0.3).move_to(UP * 0.3)
        card2.shift(LEFT * 10)
        
        # 卡片滑入
        self.play(card1.animate.shift(RIGHT * 10), run_time=0.6)
        self.play(card2.animate.shift(RIGHT * 10), run_time=0.6)
        
        self.wait(0.5)
        
        # 示例题目
        example_title = Text(
            "例题:",
            font=self.FONT_CHINESE,
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 1.5 + LEFT * 3)
        
        example_text = Text(
            "正八边形每个内角?",
            font=self.FONT_CHINESE,
            font_size=26,
            color=WHITE
        ).next_to(example_title, RIGHT, buff=0.2)
        
        self.play(FadeIn(VGroup(example_title, example_text)), run_time=0.8)
        
        # 计算步骤
        calc1_parts = []
        calc1_parts.append(Text("(8-2)", font=self.FONT_CHINESE, font_size=24, color=WHITE))
        calc1_parts.append(MathTex(r"\times", font_size=24))
        calc1_parts.append(Text("180", font=self.FONT_CHINESE, font_size=24, color=WHITE))
        calc1_parts.append(MathTex(r"^\circ", font_size=24))
        calc1_parts.append(MathTex(r"\div", font_size=24))
        calc1_parts.append(Text("8", font=self.FONT_CHINESE, font_size=24, color=WHITE))
        
        calc1 = VGroup(*calc1_parts).arrange(RIGHT, buff=0.1).move_to(DOWN * 3)
        
        self.play(Write(calc1), run_time=1.2)
        
        # 计算结果
        calc2_parts = []
        calc2_parts.append(Text("= 1080", font=self.FONT_CHINESE, font_size=24, color=WHITE))
        calc2_parts.append(MathTex(r"^\circ", font_size=24))
        calc2_parts.append(MathTex(r"\div", font_size=24))
        calc2_parts.append(Text("8 = 135", font=self.FONT_CHINESE, font_size=24, color=self.COLOR_HIGHLIGHT))
        calc2_parts.append(MathTex(r"^\circ", font_size=24, color=self.COLOR_HIGHLIGHT))
        
        calc2 = VGroup(*calc2_parts).arrange(RIGHT, buff=0.1).move_to(DOWN * 4)
        
        self.play(Write(calc2), run_time=1.2)
        
        # 答案强调
        answer_box = SurroundingRectangle(calc2[-2:], color=self.COLOR_HIGHLIGHT, buff=0.1, stroke_width=2)
        self.play(Create(answer_box), run_time=0.5)
        
        self.wait(1.0)
        
        # 清理示例
        self.play(
            FadeOut(VGroup(example_title, example_text)),
            FadeOut(calc1),
            FadeOut(calc2),
            FadeOut(answer_box),
            run_time=0.5
        )
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多几何技巧!",
            font=self.FONT_CHINESE,
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 2)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.8)
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font=self.FONT_CHINESE,
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 4)
        
        author_id = Text(
            "@emptyandcalm",
            font=self.FONT_CHINESE,
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 5)
        
        self.play(
            ReplacementTransform(self.author_info.copy(), author_name),
            FadeIn(author_id),
            run_time=0.8
        )
        
        # 装饰图案 - 小多边形
        decorations = VGroup()
        for i in range(6):
            angle = i * PI / 3
            pos = follow_text.get_center() + 2.5 * np.array([cos(angle), sin(angle), 0])
            
            if i % 3 == 0:
                deco = Polygon(*self.triangle_vertices, color=GOLD, fill_opacity=0.6, stroke_width=0)
            elif i % 3 == 1:
                deco = Polygon(*self.square_vertices, color=self.COLOR_PRIMARY, fill_opacity=0.6, stroke_width=0)
            else:
                deco = Polygon(*self.pentagon_vertices, color=self.COLOR_EXTERIOR, fill_opacity=0.6, stroke_width=0)
            
            deco.scale(0.15).move_to(pos)
            decorations.add(deco)
        
        self.play(
            *[FadeIn(deco, scale=0.5) for deco in decorations],
            run_time=0.8
        )
        
        self.play(Rotate(decorations, angle=PI/2, run_time=1.5))
        
        self.wait(1.5)
        
        # 全部淡出
        self.play(
            FadeOut(title),
            FadeOut(card1),
            FadeOut(card2),
            FadeOut(follow_text),
            FadeOut(author_name),
            FadeOut(author_id),
            FadeOut(decorations),
            FadeOut(self.author_info),
            FadeOut(self.interior_formula_ref),
            FadeOut(self.exterior_formula_ref),
            FadeOut(self.triangle_ref),
            FadeOut(self.square_ref),
            FadeOut(self.pentagon_ref),
            run_time=1.2
        )


# 渲染命令:
# manim -pql polygon_angles.py PolygonAngles  # 快速预览
# manim -qh polygon_angles.py PolygonAngles   # 高质量渲染