"""
多面体概念教学动画 - Polyhedron Concepts Animation
使用 Manim 创建的高三立体几何教学视频

内容: 多面体定义、凸多面体、正多面体（5种）、欧拉公式
目标观众: 高三学生
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


class PolyhedronConcepts(ThreeDScene):
    """
    多面体概念教学动画场景 (3D)
    
    场景顺序:
    1. 开场引入
    2. 多面体定义
    3. 凸多面体
    4. 正多面体引入
    5. 正四面体详解
    6. 正六面体详解
    7. 正八面体详解
    8. 欧拉公式总结
    9. 五种正多面体全家福
    10. 结尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主要多面体
        self.COLOR_VERTEX = "#e74c3c"         # 红色 - 顶点
        self.COLOR_EDGE = "#f39c12"           # 橙色 - 棱
        self.COLOR_FACE = "#2ecc71"           # 绿色 - 面
        self.COLOR_FORMULA = "#9b59b6"        # 紫色 - 公式
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        
        # 设置初始相机角度
        self.set_camera_orientation(phi=70*DEGREES, theta=-45*DEGREES)
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.show_opening()
        self.show_polyhedron_definition()
        self.show_convex_polyhedron()
        self.show_regular_intro()
        self.show_tetrahedron()
        self.show_cube()
        self.show_octahedron()
        self.show_euler_formula()
        self.show_five_polyhedra()
        self.show_outro()
    
    def setup_geometry(self):
        """初始化所有3D几何对象和数据"""
        # ===== 正多面体尺寸 =====
        self.POLY_SIZE = 1.2
        
        # ===== 创建五种正多面体 =====
        self.tetrahedron = Tetrahedron(edge_length=self.POLY_SIZE)
        self.cube = Cube(side_length=self.POLY_SIZE)
        self.octahedron = Octahedron(edge_length=self.POLY_SIZE)
        self.dodecahedron = Dodecahedron(edge_length=self.POLY_SIZE * 0.7)
        self.icosahedron = Icosahedron(edge_length=self.POLY_SIZE * 0.8)
        
        # 设置颜色
        for poly in [self.tetrahedron, self.cube, self.octahedron, 
                     self.dodecahedron, self.icosahedron]:
            poly.set_color(self.COLOR_PRIMARY)
            poly.set_fill(self.COLOR_PRIMARY, opacity=0.3)
            poly.set_stroke(WHITE, width=2)
        
        # ===== 欧拉公式数据 =====
        self.euler_data = {
            "tetrahedron": {"V": 4, "E": 6, "F": 4},
            "cube": {"V": 8, "E": 12, "F": 6},
            "octahedron": {"V": 6, "E": 12, "F": 8},
            "dodecahedron": {"V": 20, "E": 30, "F": 12},
            "icosahedron": {"V": 12, "E": 30, "F": 20},
        }
        
        # ===== 验证欧拉公式 =====
        self.verify_euler_formula()
        
        print("✓ 几何数据初始化完成")
    
    def verify_euler_formula(self):
        """验证所有多面体满足欧拉公式 V - E + F = 2"""
        for name, data in self.euler_data.items():
            V, E, F = data["V"], data["E"], data["F"]
            result = V - E + F
            if result != 2:
                print(f"WARNING: {name} 不满足欧拉公式! V-E+F = {result}")
            else:
                print(f"✓ {name}: V={V}, E={E}, F={F}, V-E+F={result}")
    
    def show_opening(self):
        """场景1: 开场引入"""
        # ===== 作者信息 (2D固定层) =====
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B
        )
        # 使用 add_fixed_in_frame_mobjects 将2D文字固定在屏幕上
        self.add_fixed_in_frame_mobjects(self.author_info)
        self.author_info.to_edge(UP, buff=0.3)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # ===== 钩子问题 (2D) =====
        hook_text = Text(
            "世界上只有5种正多面体？",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        )
        self.add_fixed_in_frame_mobjects(hook_text)
        hook_text.move_to(UP * 2.8)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # ===== 旋转的正四面体 (3D) =====
        tetra_opening = self.tetrahedron.copy().scale(0.8)
        
        self.play(Create(tetra_opening), run_time=1.5)
        self.wait(0.3)
        
        # 开始环境旋转
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(1.5)
        self.stop_ambient_camera_rotation()
        
        # ===== 清理 =====
        self.play(
            FadeOut(hook_text),
            tetra_opening.animate.scale(0.3).move_to(UP * 2 + LEFT * 3),
            run_time=0.6
        )
        
        self.remove(tetra_opening)
    
    def show_polyhedron_definition(self):
        """场景2: 多面体定义"""
        # ===== 标题 (2D) =====
        title = Text(
            "多面体的定义",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        )
        self.add_fixed_in_frame_mobjects(title)
        title.move_to(UP * 2.2)
        
        self.play(Write(title), run_time=0.6)
        
        # ===== 创建示例多面体（三棱锥） =====
        # 使用自定义顶点创建简单三棱锥
        # 转换为 numpy 数组并缩放
        vertices_raw = [
            [0, 0, 0],           # 底面中心
            [1, 0, -0.5],        # 底面顶点1
            [-0.5, 0, -0.5],     # 底面顶点2
            [0, 1.2, 0],         # 顶点
        ]
        
        # 保存缩放后的顶点坐标（供后续使用）
        scale_factor = 1.3
        vertices_scaled = [np.array(v) * scale_factor for v in vertices_raw]
        
        # 定义面（顶点索引）
        faces = [
            [0, 1, 2],     # 底面
            [0, 1, 3],     # 侧面1
            [1, 2, 3],     # 侧面2
            [2, 0, 3],     # 侧面3
        ]
        
        poly_demo = Polyhedron(
            vertex_coords=vertices_raw,
            faces_list=faces
        ).scale(scale_factor)
        
        poly_demo.set_color(self.COLOR_PRIMARY)
        poly_demo.set_fill(self.COLOR_PRIMARY, opacity=0.2)
        poly_demo.set_stroke(WHITE, width=2)
        
        self.play(Create(poly_demo, lag_ratio=0.1), run_time=1.2)
        self.wait(0.3)
        
        # ===== 高亮面 =====
        # 使用保存的顶点坐标创建高亮面
        face_highlight = Polygon(
            vertices_scaled[0],
            vertices_scaled[1],
            vertices_scaled[2],
            color=self.COLOR_FACE,
            fill_opacity=0.5,
            stroke_width=4
        )
        
        face_label = Text("面", font="PingFang SC", font_size=24, color=self.COLOR_FACE)
        self.add_fixed_in_frame_mobjects(face_label)
        face_label.move_to(DOWN * 1.5 + LEFT * 2.5)
        
        face_def = Text(
            "平面多边形", 
            font="PingFang SC", 
            font_size=18, 
            color=GRAY_A
        )
        self.add_fixed_in_frame_mobjects(face_def)
        face_def.next_to(face_label, DOWN, buff=0.1)
        
        self.play(
            Create(face_highlight),
            FadeIn(face_label),
            FadeIn(face_def),
            run_time=0.8
        )
        self.wait(0.5)
        
        self.play(FadeOut(face_highlight), FadeOut(face_label), FadeOut(face_def))
        
        # ===== 高亮棱 =====
        # 使用保存的顶点坐标创建边
        edges_to_highlight = VGroup()
        edge_indices = [[0, 1], [1, 2], [2, 0], [0, 3]]  # 选择几条边
        
        for idx_pair in edge_indices:
            v1 = vertices_scaled[idx_pair[0]]
            v2 = vertices_scaled[idx_pair[1]]
            edge_line = Line3D(
                start=v1,
                end=v2,
                color=self.COLOR_EDGE,
                stroke_width=6
            )
            edges_to_highlight.add(edge_line)
        
        edge_label = Text("棱", font="PingFang SC", font_size=24, color=self.COLOR_EDGE)
        self.add_fixed_in_frame_mobjects(edge_label)
        edge_label.move_to(DOWN * 1.5)
        
        edge_def = Text(
            "相邻面的公共边", 
            font="PingFang SC", 
            font_size=18, 
            color=GRAY_A
        )
        self.add_fixed_in_frame_mobjects(edge_def)
        edge_def.next_to(edge_label, DOWN, buff=0.1)
        
        self.play(
            Create(edges_to_highlight, lag_ratio=0.2),
            FadeIn(edge_label),
            FadeIn(edge_def),
            run_time=1.0
        )
        self.wait(0.5)
        
        self.play(FadeOut(edges_to_highlight), FadeOut(edge_label), FadeOut(edge_def))
        
        # ===== 高亮顶点 =====
        # 使用保存的顶点坐标创建顶点标记
        vertices_dots = VGroup(*[
            Dot3D(point=v, radius=0.08, color=self.COLOR_VERTEX)
            for v in vertices_scaled
        ])
        
        vertex_label = Text("顶点", font="PingFang SC", font_size=24, color=self.COLOR_VERTEX)
        self.add_fixed_in_frame_mobjects(vertex_label)
        vertex_label.move_to(DOWN * 1.5 + RIGHT * 2.5)
        
        vertex_def = Text(
            "棱的公共点", 
            font="PingFang SC", 
            font_size=18, 
            color=GRAY_A
        )
        self.add_fixed_in_frame_mobjects(vertex_def)
        vertex_def.next_to(vertex_label, DOWN, buff=0.1)
        
        self.play(
            Create(vertices_dots, lag_ratio=0.15),
            FadeIn(vertex_label),
            FadeIn(vertex_def),
            run_time=1.0
        )
        self.wait(0.5)
        
        # ===== 完整定义 (2D) =====
        definition = Text(
            "多面体：由若干平面多边形围成",
            font="PingFang SC",
            font_size=20,
            color=GRAY_A
        )
        self.add_fixed_in_frame_mobjects(definition)
        definition.move_to(DOWN * 3.5)
        
        self.play(FadeIn(definition), run_time=0.8)
        self.wait(1.2)
        
        # ===== 清理 =====
        self.play(
            FadeOut(title),
            FadeOut(poly_demo),
            FadeOut(vertices_dots),
            FadeOut(vertex_label),
            FadeOut(vertex_def),
            FadeOut(definition),
            run_time=0.5
        )
    
    def show_convex_polyhedron(self):
        """场景3: 凸多面体"""
        # ===== 标题 =====
        title = Text(
            "凸多面体",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        )
        self.add_fixed_in_frame_mobjects(title)
        title.move_to(UP * 2.2)
        
        self.play(Write(title), run_time=0.6)
        
        # ===== 左侧：凸多面体（立方体） =====
        convex = self.cube.copy().scale(0.6).shift(LEFT * 2)
        
        convex_check = Text("✓", font_size=40, color=GREEN)
        self.add_fixed_in_frame_mobjects(convex_check)
        convex_check.move_to(DOWN * 1.8 + LEFT * 2)
        
        convex_label = Text("凸", font="PingFang SC", font_size=24, color=GREEN)
        self.add_fixed_in_frame_mobjects(convex_label)
        convex_label.next_to(convex_check, DOWN, buff=0.1)
        
        self.play(Create(convex), run_time=1.0)
        self.play(FadeIn(convex_check), FadeIn(convex_label), run_time=0.4)
        
        # ===== 右侧：非凸示意（星形） =====
        # 创建一个简单的非凸多面体示意（使用五角星轮廓）
        star_points_2d = [
            [np.cos(i * 2 * PI / 5), np.sin(i * 2 * PI / 5), 0]
            for i in range(5)
        ]
        
        # 交错连接形成星形
        star_path = [star_points_2d[i] for i in [0, 2, 4, 1, 3, 0]]
        
        non_convex = Polygon(*star_path, color=self.COLOR_PRIMARY, stroke_width=2)
        non_convex.set_fill(self.COLOR_PRIMARY, opacity=0.3)
        non_convex.scale(0.6).shift(RIGHT * 2)
        
        # 将2D多边形转为类3D显示
        non_convex.rotate(PI/6, axis=RIGHT)
        
        non_convex_cross = Text("✗", font_size=40, color=RED)
        self.add_fixed_in_frame_mobjects(non_convex_cross)
        non_convex_cross.move_to(DOWN * 1.8 + RIGHT * 2)
        
        non_convex_label = Text("非凸", font="PingFang SC", font_size=24, color=RED)
        self.add_fixed_in_frame_mobjects(non_convex_label)
        non_convex_label.next_to(non_convex_cross, DOWN, buff=0.1)
        
        self.play(Create(non_convex), run_time=1.0)
        self.play(FadeIn(non_convex_cross), FadeIn(non_convex_label), run_time=0.4)
        
        # ===== 判别标准说明 =====
        criterion = Text(
            "延展任一面，其余各面在同侧 → 凸",
            font="PingFang SC",
            font_size=18,
            color=GRAY_A
        )
        self.add_fixed_in_frame_mobjects(criterion)
        criterion.move_to(DOWN * 3.5)
        
        self.play(FadeIn(criterion), run_time=1.0)
        self.wait(1.5)
        
        # ===== 清理 =====
        self.play(
            FadeOut(title),
            FadeOut(convex),
            FadeOut(non_convex),
            FadeOut(convex_check),
            FadeOut(convex_label),
            FadeOut(non_convex_cross),
            FadeOut(non_convex_label),
            FadeOut(criterion),
            run_time=0.5
        )
    
    def show_regular_intro(self):
        """场景4: 正多面体引入"""
        # ===== 标题 =====
        title = Text(
            "正多面体",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        )
        self.add_fixed_in_frame_mobjects(title)
        title.move_to(UP * 2.5)
        
        self.play(Write(title), run_time=0.6)
        
        # ===== 定义条件 =====
        cond1 = Text(
            "① 各面都是全等的正多边形",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        )
        self.add_fixed_in_frame_mobjects(cond1)
        cond1.move_to(UP * 1.5)
        
        cond2 = Text(
            "② 各顶点的面数相同",
            font="PingFang SC",
            font_size=22,
            color=GRAY_A
        )
        self.add_fixed_in_frame_mobjects(cond2)
        cond2.move_to(UP * 0.9)
        
        self.play(FadeIn(cond1), run_time=0.5)
        self.play(FadeIn(cond2), run_time=0.5)
        
        # ===== 五个小图标 =====
        icons = VGroup()
        
        icon_polys = [
            self.tetrahedron.copy(),
            self.cube.copy(),
            self.octahedron.copy(),
            self.dodecahedron.copy(),
            self.icosahedron.copy(),
        ]
        
        for i, poly in enumerate(icon_polys):
            poly.scale(0.25)
            # 排列成一行
            x_pos = -2.5 + i * 1.3
            poly.move_to([x_pos, -0.5, 0])
            icons.add(poly)
        
        self.play(
            LaggedStart(*[Create(icon) for icon in icons], lag_ratio=0.2),
            run_time=1.5
        )
        
        # ===== 强调"仅有5种" =====
        emphasis = Text(
            "仅有5种！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        )
        self.add_fixed_in_frame_mobjects(emphasis)
        emphasis.move_to(DOWN * 2.5)
        
        self.play(
            Flash(emphasis, color=YELLOW, flash_radius=0.5),
            FadeIn(emphasis, scale=1.2),
            run_time=1.0
        )
        self.wait(1.2)
        
        # ===== 保留图标，移到顶部作为导航 =====
        # 缩小并移动
        icons_nav = VGroup(*[icon.copy() for icon in icons])
        for i, icon in enumerate(icons_nav):
            icon.scale(0.6)  # 进一步缩小
            x_pos = -3 + i * 1.5
            icon.target = icon.copy().move_to([x_pos, 3, 0])
        
        self.play(
            *[MoveToTarget(icon) for icon in icons_nav],
            FadeOut(title),
            FadeOut(cond1),
            FadeOut(cond2),
            FadeOut(emphasis),
            *[FadeOut(icon) for icon in icons],
            run_time=0.6
        )
        
        # 保存导航图标引用
        self.icons_nav = icons_nav
    
    def show_polyhedron_detail(self, poly_name, polyhedron, data):
        """
        通用函数：展示一个正多面体的详细信息
        
        参数:
            poly_name: 名称（中文）
            polyhedron: Manim 3D对象
            data: {"V": int, "E": int, "F": int}
        """
        V, E, F = data["V"], data["E"], data["F"]
        
        # ===== 名称 =====
        name_text = Text(
            poly_name,
            font="PingFang SC",
            font_size=32,
            color=WHITE
        )
        self.add_fixed_in_frame_mobjects(name_text)
        name_text.move_to(UP * 2.2)
        
        self.play(Write(name_text), run_time=0.5)
        
        # ===== 创建多面体 =====
        poly = polyhedron.copy().scale(0.9)
        
        self.play(Create(poly), run_time=1.2)
        
        # ===== 旋转展示 =====
        self.play(Rotate(poly, angle=2*PI/3, axis=UP, run_time=2.0))
        
        # ===== 数据标注区域（右侧，2D固定） =====
        data_box = VGroup()
        
        v_text = Text(f"V = {V}", font="PingFang SC", font_size=24, color=self.COLOR_VERTEX)
        e_text = Text(f"E = {E}", font="PingFang SC", font_size=24, color=self.COLOR_EDGE)
        f_text = Text(f"F = {F}", font="PingFang SC", font_size=24, color=self.COLOR_FACE)
        
        data_box.add(v_text, e_text, f_text)
        data_box.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.add_fixed_in_frame_mobjects(data_box)
        data_box.move_to(DOWN * 0.5 + RIGHT * 2.5)
        
        # ===== 顶点高亮 + 计数 =====
        # 使用多面体的角点作为顶点位置的近似
        # 对于内置的正多面体，使用启发式方法找顶点
        try:
            # 尝试获取边界框的关键点
            corners = []
            # 获取多面体的所有点
            all_points = poly.get_all_points()
            
            # 使用聚类方法找到顶点（基于点的密集程度）
            # 简化方法：使用多面体的极值点
            if len(all_points) > 0:
                # 找到x, y, z各方向的极值点
                unique_points = []
                tolerance = 0.1
                
                for point in all_points:
                    is_unique = True
                    for up in unique_points:
                        if np.linalg.norm(point - up) < tolerance:
                            is_unique = False
                            break
                    if is_unique:
                        unique_points.append(point)
                
                # 取前V个最分散的点作为顶点
                if len(unique_points) >= V:
                    corners = unique_points[:V]
                else:
                    corners = unique_points
            
            if len(corners) > 0:
                dots = VGroup(*[
                    Dot3D(point=v, radius=0.06, color=self.COLOR_VERTEX)
                    for v in corners[:V]
                ])
                
                self.play(
                    Create(dots, lag_ratio=0.08),
                    FadeIn(v_text),
                    run_time=1.0
                )
                self.wait(0.3)
            else:
                # 如果无法获取顶点，只显示计数
                self.play(FadeIn(v_text), run_time=0.5)
                dots = VGroup()  # 空组，避免后续错误
        except:
            # 降级方案：仅显示文字，不标注顶点
            self.play(FadeIn(v_text), run_time=0.5)
            dots = VGroup()
        
        # ===== 棱高亮（示意，不逐一） =====
        self.play(
            poly.animate.set_stroke(self.COLOR_EDGE, width=5),
            FadeIn(e_text),
            run_time=0.8
        )
        self.wait(0.3)
        self.play(poly.animate.set_stroke(WHITE, width=2))
        
        # ===== 面高亮 =====
        self.play(
            poly.animate.set_fill(self.COLOR_FACE, opacity=0.6),
            FadeIn(f_text),
            run_time=0.8
        )
        self.wait(0.3)
        
        # ===== 欧拉公式验证 =====
        euler_calc = MathTex(
            f"{V}", "-", f"{E}", "+", f"{F}", "=", "2",
            font_size=32
        )
        euler_calc[0].set_color(self.COLOR_VERTEX)
        euler_calc[2].set_color(self.COLOR_EDGE)
        euler_calc[4].set_color(self.COLOR_FACE)
        euler_calc[6].set_color(GREEN)
        
        self.add_fixed_in_frame_mobjects(euler_calc)
        euler_calc.move_to(DOWN * 3)
        
        checkmark = Text("✓", font_size=40, color=GREEN)
        self.add_fixed_in_frame_mobjects(checkmark)
        checkmark.next_to(euler_calc, RIGHT, buff=0.3)
        
        self.play(Write(euler_calc), run_time=1.0)
        self.play(FadeIn(checkmark, scale=1.5), run_time=0.5)
        
        self.wait(0.8)
        
        # ===== 清理 =====
        self.play(
            FadeOut(name_text),
            FadeOut(poly),
            FadeOut(dots),
            FadeOut(data_box),
            FadeOut(euler_calc),
            FadeOut(checkmark),
            run_time=0.4
        )
    
    def show_tetrahedron(self):
        """场景5: 正四面体详解"""
        self.show_polyhedron_detail(
            "正四面体",
            self.tetrahedron,
            self.euler_data["tetrahedron"]
        )
    
    def show_cube(self):
        """场景6: 正六面体（立方体）详解"""
        self.show_polyhedron_detail(
            "正六面体（立方体）",
            self.cube,
            self.euler_data["cube"]
        )
    
    def show_octahedron(self):
        """场景7: 正八面体详解"""
        self.show_polyhedron_detail(
            "正八面体",
            self.octahedron,
            self.euler_data["octahedron"]
        )
    
    def show_euler_formula(self):
        """场景8: 欧拉公式总结"""
        # ===== 大标题 =====
        title = Text(
            "欧拉公式",
            font="PingFang SC",
            font_size=40,
            color=GOLD
        )
        self.add_fixed_in_frame_mobjects(title)
        title.move_to(UP * 3)
        
        self.play(Write(title), run_time=0.8)
        
        # ===== 公式 =====
        formula = MathTex(
            r"V - E + F = 2",
            font_size=48,
            color=self.COLOR_FORMULA
        )
        self.add_fixed_in_frame_mobjects(formula)
        formula.move_to(UP * 1.8)
        
        self.play(Write(formula), run_time=1.2)
        
        # ===== 三个多面体并排 =====
        poly_group = VGroup(
            self.tetrahedron.copy().scale(0.4),
            self.cube.copy().scale(0.4),
            self.octahedron.copy().scale(0.4),
        )
        
        positions = [LEFT * 2.2, ORIGIN, RIGHT * 2.2]
        for poly, pos in zip(poly_group, positions):
            poly.move_to(pos + UP * 0.3)
        
        self.play(
            LaggedStart(*[Create(poly) for poly in poly_group], lag_ratio=0.3),
            run_time=1.5
        )
        
        # ===== 验证计算（2D文字） =====
        verifications = VGroup()
        
        data_list = [
            self.euler_data["tetrahedron"],
            self.euler_data["cube"],
            self.euler_data["octahedron"],
        ]
        
        for data, pos in zip(data_list, positions):
            V, E, F = data["V"], data["E"], data["F"]
            calc_text = Text(
                f"{V}-{E}+{F}=2",
                font="PingFang SC",
                font_size=18,
                color=GRAY_A
            )
            self.add_fixed_in_frame_mobjects(calc_text)
            calc_text.move_to(pos + DOWN * 1.2)
            verifications.add(calc_text)
        
        # 依次显示验证
        for i, calc in enumerate(verifications):
            self.play(Write(calc), run_time=0.8)
            self.wait(0.3)
        
        # ===== 统一结论 =====
        conclusion = Text(
            "对所有凸多面体成立！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        )
        self.add_fixed_in_frame_mobjects(conclusion)
        conclusion.move_to(DOWN * 3)
        
        self.play(
            Flash(conclusion, color=YELLOW),
            FadeIn(conclusion, shift=UP * 0.3),
            run_time=1.0
        )
        
        # ===== 高亮所有"=2" =====
        self.play(
            *[Indicate(calc[-2:]) for calc in verifications],
            Indicate(formula[-1]),
            run_time=1.0
        )
        
        self.wait(1.5)
        
        # ===== 清理 =====
        self.play(
            FadeOut(title),
            FadeOut(formula),
            *[FadeOut(poly) for poly in poly_group],
            FadeOut(verifications),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def show_five_polyhedra(self):
        """场景9: 五种正多面体全家福"""
        # ===== 标题 =====
        title = Text(
            "五种正多面体",
            font="PingFang SC",
            font_size=36,
            color=GOLD
        )
        self.add_fixed_in_frame_mobjects(title)
        title.move_to(UP * 3)
        
        self.play(Write(title), run_time=0.6)
        
        # ===== 五个多面体网格排列 =====
        # 布局: 第一行3个，第二行2个
        polys = [
            ("正四面体", self.tetrahedron.copy(), self.euler_data["tetrahedron"]),
            ("正六面体", self.cube.copy(), self.euler_data["cube"]),
            ("正八面体", self.octahedron.copy(), self.euler_data["octahedron"]),
            ("正十二面体", self.dodecahedron.copy(), self.euler_data["dodecahedron"]),
            ("正二十面体", self.icosahedron.copy(), self.euler_data["icosahedron"]),
        ]
        
        # 位置布局
        positions_row1 = [LEFT * 2.5, ORIGIN, RIGHT * 2.5]
        positions_row2 = [LEFT * 1.2, RIGHT * 1.2]
        all_positions = positions_row1 + positions_row2
        
        poly_objects = VGroup()
        labels = VGroup()
        
        for i, (name, poly, data) in enumerate(polys):
            # 缩放并定位
            poly.scale(0.35 if i < 3 else 0.3)
            
            y_offset = UP * 0.8 if i < 3 else DOWN * 1.2
            poly.move_to(all_positions[i] + y_offset)
            
            poly_objects.add(poly)
            
            # 名称标签 (2D)
            label = Text(name, font="PingFang SC", font_size=16, color=WHITE)
            self.add_fixed_in_frame_mobjects(label)
            label_y = 0.1 if i < 3 else -1.9
            label.move_to(all_positions[i] + UP * label_y)
            labels.add(label)
            
            # 数据标签 (2D)
            V, E, F = data["V"], data["E"], data["F"]
            data_text = Text(
                f"V={V} E={E} F={F}",
                font="PingFang SC",
                font_size=12,
                color=GRAY_A
            )
            self.add_fixed_in_frame_mobjects(data_text)
            data_y = -0.3 if i < 3 else -2.3
            data_text.move_to(all_positions[i] + UP * data_y)
            labels.add(data_text)
        
        # ===== 依次创建 =====
        self.play(
            LaggedStart(*[Create(poly) for poly in poly_objects], lag_ratio=0.3),
            run_time=2.5
        )
        
        # ===== 同步旋转展示 =====
        self.play(
            *[Rotate(poly, angle=PI, axis=UP) for poly in poly_objects],
            run_time=3.0,
            rate_func=smooth
        )
        
        # ===== 标签淡入 =====
        self.play(FadeIn(labels), run_time=1.0)
        
        self.wait(1.0)
        
        # ===== 清理 =====
        self.play(
            FadeOut(title),
            *[FadeOut(poly) for poly in poly_objects],
            FadeOut(labels),
            run_time=0.6
        )
    
    def show_outro(self):
        """场景10: 结尾关注"""
        # 停止相机旋转（如果有）
        self.stop_ambient_camera_rotation()
        
        # 重置相机到正面
        self.move_camera(phi=0, theta=-90*DEGREES, run_time=0.8)
        
        # ===== 作者信息放大 =====
        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        )
        self.add_fixed_in_frame_mobjects(author_large)
        author_large.move_to(UP * 1)
        
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=GRAY_B
        )
        self.add_fixed_in_frame_mobjects(author_id)
        author_id.move_to(ORIGIN)
        
        self.play(
            Transform(self.author_info, author_large),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # ===== 关注提示 =====
        follow_text = Text(
            "关注我，学更多立体几何！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        )
        self.add_fixed_in_frame_mobjects(follow_text)
        follow_text.move_to(DOWN * 1.2)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # ===== 装饰：旋转的小多面体 =====
        decorations = VGroup(
            self.tetrahedron.copy().scale(0.15),
            self.cube.copy().scale(0.15),
            self.octahedron.copy().scale(0.15),
            self.dodecahedron.copy().scale(0.12),
            self.icosahedron.copy().scale(0.12),
        )
        
        # 环绕排列
        radius = 2.5
        for i, deco in enumerate(decorations):
            angle = i * 2 * PI / 5
            x = radius * np.cos(angle)
            y = radius * np.sin(angle) - 1
            deco.move_to([x, y, 0])
        
        self.play(
            *[FadeIn(deco, scale=0.5) for deco in decorations],
            run_time=0.8
        )
        
        # 旋转装饰
        self.play(
            *[Rotate(deco, angle=2*PI, axis=UP) for deco in decorations],
            run_time=3.0,
            rate_func=linear
        )
        
        # ===== 全部淡出 =====
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            *[FadeOut(deco) for deco in decorations],
            run_time=1.0
        )


# ===== 渲染命令 =====
# 快速预览：manim -pql polyhedron_concepts.py PolyhedronConcepts
# 高质量：manim -qh polyhedron_concepts.py PolyhedronConcepts
# 4K：manim -qk polyhedron_concepts.py PolyhedronConcepts