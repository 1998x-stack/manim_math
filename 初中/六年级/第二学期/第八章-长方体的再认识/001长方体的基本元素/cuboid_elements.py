"""
长方体的基本元素 - Manim 数学教学动画
Cuboid Elements - Educational Animation

知识点：长方体的顶点、棱、面及欧拉公式
年级：六年级第二学期
章节：第八章 - 长方体的再认识
作者：上海初高中数学直通车 @emptyandcalm

视频格式：TikTok 竖屏 (1080×1920)
时长：60-75秒
"""

from manim import *
import numpy as np


# ==================== 全局配置 ====================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CuboidElements(ThreeDScene):
    """
    长方体基本元素教学动画
    
    场景序列：
    1. 开场钩子
    2. 顶点讲解（8个）
    3. 棱讲解（12条）
    4. 面讲解（6个）
    5. 欧拉公式验证
    6. 特殊情况-正方体
    7. 片尾关注
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 初始化配色方案
        self.setup_colors()
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 设置3D摄像机
        self.set_camera_orientation(phi=70*DEGREES, theta=-45*DEGREES)
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_vertices()
        self.scene_3_edges()
        self.scene_4_faces()
        self.scene_5_euler_formula()
        self.scene_6_cube()
        self.scene_7_outro()
    
    def setup_colors(self):
        """配色方案"""
        # 长方体
        self.COLOR_CUBOID = "#3498db"      # 蓝色
        self.COLOR_FACE = "#e74c3c"        # 红色
        self.COLOR_EDGE = "#f39c12"        # 橙色
        self.COLOR_VERTEX = "#2ecc71"      # 绿色
        
        # 辅助
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_TEXT = WHITE
        
        # 作者
        self.AUTHOR_COLOR = GRAY_B
    
    def setup_geometry(self):
        """
        初始化长方体几何数据
        遵循约束法则：所有几何元素统一计算
        """
        # ========== 基准参数 ==========
        self.length = 3.0   # 长（x方向）
        self.width = 2.0    # 宽（y方向）
        self.height = 2.5   # 高（z方向）
        
        self.SCALE = 0.7    # 缩放以适配竖屏
        self.OFFSET = UP * 1.5
        
        # ========== 创建长方体（使用Prism）==========
        # Prism(dimensions=[width, height, depth])
        # 注意：Prism的参数顺序是 [宽, 高, 深]
        self.cuboid = Prism(
            dimensions=[self.width, self.height, self.length],
            fill_color=self.COLOR_CUBOID,
            fill_opacity=0.3,
            stroke_color=self.COLOR_CUBOID,
            stroke_width=2
        ).scale(self.SCALE).shift(self.OFFSET)
        
        # ========== 提取顶点坐标 ==========
        # Prism 会自动生成顶点，我们需要提取它们
        vertices = self.cuboid.get_vertices()
        
        # 长方体有8个顶点，按照特定顺序排列
        # 我们需要手动定义顶点位置以便精确控制
        l = self.length * self.SCALE / 2
        w = self.width * self.SCALE / 2
        h = self.height * self.SCALE / 2
        
        # 前面4个顶点（z为正）
        self.V0 = np.array([-w, -h, l]) + self.OFFSET  # 左下前
        self.V1 = np.array([w, -h, l]) + self.OFFSET   # 右下前
        self.V2 = np.array([w, h, l]) + self.OFFSET    # 右上前
        self.V3 = np.array([-w, h, l]) + self.OFFSET   # 左上前
        
        # 后面4个顶点（z为负）
        self.V4 = np.array([-w, -h, -l]) + self.OFFSET # 左下后
        self.V5 = np.array([w, -h, -l]) + self.OFFSET  # 右下后
        self.V6 = np.array([w, h, -l]) + self.OFFSET   # 右上后
        self.V7 = np.array([-w, h, -l]) + self.OFFSET  # 左上后
        
        self.vertices = [
            self.V0, self.V1, self.V2, self.V3,
            self.V4, self.V5, self.V6, self.V7
        ]
        
        # ========== 定义12条棱的分组 ==========
        # 长度方向（4条，平行于z轴）
        self.edges_length = [
            (self.V0, self.V4),  # 左下
            (self.V1, self.V5),  # 右下
            (self.V2, self.V6),  # 右上
            (self.V3, self.V7),  # 左上
        ]
        
        # 宽度方向（4条，平行于x轴）
        self.edges_width = [
            (self.V0, self.V1),  # 前下
            (self.V3, self.V2),  # 前上
            (self.V4, self.V5),  # 后下
            (self.V7, self.V6),  # 后上
        ]
        
        # 高度方向（4条，平行于y轴）
        self.edges_height = [
            (self.V0, self.V3),  # 左前
            (self.V1, self.V2),  # 右前
            (self.V4, self.V7),  # 左后
            (self.V5, self.V6),  # 右后
        ]
        
        # 所有12条棱
        self.all_edges = (
            self.edges_length + 
            self.edges_width + 
            self.edges_height
        )
        
        # ========== 定义6个面 ==========
        self.face_front = [self.V0, self.V1, self.V2, self.V3]  # 前
        self.face_back = [self.V4, self.V5, self.V6, self.V7]   # 后
        self.face_left = [self.V0, self.V3, self.V7, self.V4]   # 左
        self.face_right = [self.V1, self.V2, self.V6, self.V5]  # 右
        self.face_top = [self.V3, self.V2, self.V6, self.V7]    # 上
        self.face_bottom = [self.V0, self.V1, self.V5, self.V4] # 下
        
        self.all_faces = [
            self.face_front,
            self.face_back,
            self.face_left,
            self.face_right,
            self.face_top,
            self.face_bottom
        ]
        
        # ========== 欧拉公式数据 ==========
        self.num_vertices = 8
        self.num_edges = 12
        self.num_faces = 6
    
    def scene_1_opening(self):
        """
        场景1: 开场钩子 (0-4s)
        目的：抓住注意力，提出问题
        """
        # ===== 作者信息（常驻顶部）=====
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.AUTHOR_COLOR
        )
        # 固定在3D场景中需要使用 add_fixed_in_frame_mobjects
        self.author_info.to_edge(UP, buff=0.3)
        self.add_fixed_in_frame_mobjects(self.author_info)
        
        self.play(FadeIn(self.author_info, shift=DOWN*0.2), run_time=0.3)
        
        # ===== 钩子问题 =====
        hook_text = Text(
            "长方体有多少个元素？",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD
        )
        hook_text.move_to(UP * 6)
        self.add_fixed_in_frame_mobjects(hook_text)
        
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.3)
        
        # ===== 长方体创建 =====
        self.play(Create(self.cuboid), run_time=1.0)
        
        # ===== 旋转展示 =====
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(1.5)
        self.stop_ambient_camera_rotation()
        
        # 恢复初始角度
        self.move_camera(phi=70*DEGREES, theta=-45*DEGREES, run_time=0.5)
        
        self.wait(0.4)
        
        # ===== 清理 =====
        self.play(FadeOut(hook_text), run_time=0.5)
        self.remove(hook_text)
    
    def scene_2_vertices(self):
        """
        场景2: 顶点讲解 (4-14s)
        目的：识别并计数8个顶点
        """
        # ===== 标题和定义 =====
        title = Text(
            "顶点 Vertices",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_VERTEX
        )
        title.move_to(UP * 5.5)
        
        definition = Text(
            "长方体的角点",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        )
        definition.move_to(UP * 4.8)
        
        self.add_fixed_in_frame_mobjects(title, definition)
        
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(definition), run_time=0.3)
        self.wait(0.5)
        
        # ===== 创建顶点标记 =====
        # 前面4个顶点
        dots_front = VGroup(*[
            Dot3D(point=v, radius=0.12, color=self.COLOR_VERTEX)
            for v in [self.V0, self.V1, self.V2, self.V3]
        ])
        
        self.play(FadeIn(dots_front, scale=0.5), run_time=0.8)
        self.wait(0.5)
        
        # ===== 旋转显示后面 =====
        self.move_camera(theta=-135*DEGREES, run_time=1.0)
        self.wait(0.3)
        
        # 后面4个顶点
        dots_back = VGroup(*[
            Dot3D(point=v, radius=0.12, color=self.COLOR_VERTEX)
            for v in [self.V4, self.V5, self.V6, self.V7]
        ])
        
        self.play(FadeIn(dots_back, scale=0.5), run_time=0.8)
        self.wait(0.5)
        
        # 恢复视角
        self.move_camera(theta=-45*DEGREES, run_time=0.8)
        
        # ===== 计数动画 =====
        all_dots = VGroup(dots_front, dots_back)
        
        # 计数器
        counter = Integer(0, font_size=48, color=self.COLOR_VERTEX)
        counter.move_to(DOWN * 4)
        self.add_fixed_in_frame_mobjects(counter)
        
        # 逐个闪烁并计数
        for i in range(8):
            dot_index = i
            if i < 4:
                current_dot = dots_front[i]
            else:
                current_dot = dots_back[i-4]
            
            self.play(
                Flash(current_dot, color=self.COLOR_VERTEX, flash_radius=0.3),
                counter.animate.set_value(i+1),
                run_time=0.15
            )
            self.wait(0.05)
        
        # ===== 结论 =====
        conclusion = Text(
            "共 8 个顶点",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_VERTEX
        )
        conclusion.move_to(DOWN * 5)
        self.add_fixed_in_frame_mobjects(conclusion)
        
        self.play(FadeIn(conclusion, shift=UP*0.2), run_time=0.5)
        self.wait(0.5)
        
        # ===== 欧拉公式引入 =====
        formula_v = MathTex("V = 8", font_size=32, color=self.COLOR_VERTEX)
        formula_v.move_to(DOWN * 6)
        self.add_fixed_in_frame_mobjects(formula_v)
        
        hint = Text(
            "记住这个数字！",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        )
        hint.move_to(DOWN * 6.8)
        self.add_fixed_in_frame_mobjects(hint)
        
        self.play(Write(formula_v), run_time=0.5)
        self.play(FadeIn(hint), run_time=0.3)
        self.wait(1.5)
        
        # ===== 清理 =====
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(counter),
            FadeOut(conclusion),
            FadeOut(formula_v),
            FadeOut(hint),
            run_time=0.6
        )
        self.remove(title, definition, counter, conclusion, formula_v, hint)
        
        # 顶点变小但保留
        self.vertex_dots = VGroup(*[
            Dot3D(point=v, radius=0.05, color=self.COLOR_VERTEX, fill_opacity=0.5)
            for v in self.vertices
        ])
        self.play(
            FadeOut(all_dots),
            FadeIn(self.vertex_dots),
            run_time=0.3
        )
    
    def scene_3_edges(self):
        """
        场景3: 棱讲解 (14-28s)
        目的：识别12条棱，理解平行分组
        """
        # ===== 标题和定义 =====
        title = Text(
            "棱 Edges",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_EDGE
        )
        title.move_to(UP * 5.5)
        
        definition = Text(
            "连接顶点的线段",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        )
        definition.move_to(UP * 4.8)
        
        self.add_fixed_in_frame_mobjects(title, definition)
        
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(definition), run_time=0.3)
        self.wait(0.5)
        
        # 计数器
        counter = Integer(0, font_size=48, color=self.COLOR_EDGE)
        counter.move_to(DOWN * 4)
        self.add_fixed_in_frame_mobjects(counter)
        
        # ===== 长度方向的4条棱 =====
        explain_1 = Text(
            "长度方向（深度）",
            font="Noto Sans CJK SC",
            font_size=24,
            color=RED
        )
        explain_1.move_to(DOWN * 5)
        self.add_fixed_in_frame_mobjects(explain_1)
        
        self.play(FadeIn(explain_1), run_time=0.5)
        
        edges_length_lines = VGroup(*[
            Line3D(start=e[0], end=e[1], color=RED, stroke_width=6)
            for e in self.edges_length
        ])
        
        self.play(
            Create(edges_length_lines),
            counter.animate.set_value(4),
            run_time=1.0
        )
        self.wait(0.5)
        
        parallel_hint = Text(
            "互相平行且相等",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        )
        parallel_hint.move_to(DOWN * 6)
        self.add_fixed_in_frame_mobjects(parallel_hint)
        
        self.play(FadeIn(parallel_hint), run_time=0.4)
        self.wait(1.0)
        
        # ===== 宽度方向的4条棱 =====
        self.play(
            FadeOut(explain_1),
            FadeOut(parallel_hint),
            run_time=0.3
        )
        self.remove(explain_1, parallel_hint)
        
        explain_2 = Text(
            "宽度方向",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GREEN
        )
        explain_2.move_to(DOWN * 5)
        self.add_fixed_in_frame_mobjects(explain_2)
        
        self.play(
            FadeOut(edges_length_lines),
            FadeIn(explain_2),
            run_time=0.5
        )
        
        edges_width_lines = VGroup(*[
            Line3D(start=e[0], end=e[1], color=GREEN, stroke_width=6)
            for e in self.edges_width
        ])
        
        self.play(
            Create(edges_width_lines),
            counter.animate.set_value(8),
            run_time=1.0
        )
        self.wait(1.0)
        
        # ===== 高度方向的4条棱 =====
        self.play(FadeOut(explain_2), run_time=0.3)
        self.remove(explain_2)
        
        explain_3 = Text(
            "高度方向",
            font="Noto Sans CJK SC",
            font_size=24,
            color=BLUE
        )
        explain_3.move_to(DOWN * 5)
        self.add_fixed_in_frame_mobjects(explain_3)
        
        self.play(
            FadeOut(edges_width_lines),
            FadeIn(explain_3),
            run_time=0.5
        )
        
        edges_height_lines = VGroup(*[
            Line3D(start=e[0], end=e[1], color=BLUE, stroke_width=6)
            for e in self.edges_height
        ])
        
        self.play(
            Create(edges_height_lines),
            counter.animate.set_value(12),
            run_time=1.0
        )
        self.wait(0.8)
        
        # ===== 三组总结 =====
        self.play(FadeOut(explain_3), run_time=0.3)
        self.remove(explain_3)
        
        # 同时显示三组
        self.play(
            FadeIn(edges_length_lines),
            FadeIn(edges_width_lines),
            run_time=0.5
        )
        
        summary = Text(
            "3组，每组4条平行棱",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_EDGE
        )
        summary.move_to(DOWN * 5)
        self.add_fixed_in_frame_mobjects(summary)
        
        self.play(FadeIn(summary), run_time=0.5)
        self.wait(0.5)
        
        # 欧拉公式
        formula_e = MathTex("E = 12", font_size=32, color=self.COLOR_EDGE)
        formula_e.move_to(DOWN * 6)
        self.add_fixed_in_frame_mobjects(formula_e)
        
        self.play(Write(formula_e), run_time=0.5)
        self.wait(1.0)
        
        # ===== 清理 =====
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(counter),
            FadeOut(summary),
            FadeOut(formula_e),
            FadeOut(edges_length_lines),
            FadeOut(edges_width_lines),
            FadeOut(edges_height_lines),
            run_time=0.6
        )
        self.remove(
            title, definition, counter, summary, formula_e,
            edges_length_lines, edges_width_lines, edges_height_lines
        )
    
    def scene_4_faces(self):
        """
        场景4: 面讲解 (28-40s)
        目的：识别6个面，理解对面关系
        """
        # ===== 标题和定义 =====
        title = Text(
            "面 Faces",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_FACE
        )
        title.move_to(UP * 5.5)
        
        definition = Text(
            "由4条棱围成的平面",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        )
        definition.move_to(UP * 4.8)
        
        self.add_fixed_in_frame_mobjects(title, definition)
        
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(definition), run_time=0.3)
        self.wait(0.5)
        
        # 计数器
        counter = Integer(0, font_size=48, color=self.COLOR_FACE)
        counter.move_to(DOWN * 4)
        self.add_fixed_in_frame_mobjects(counter)
        
        # ===== 前后两个面 =====
        hint_1 = Text(
            "前后 2 个面",
            font="Noto Sans CJK SC",
            font_size=24,
            color=RED
        )
        hint_1.move_to(DOWN * 5)
        self.add_fixed_in_frame_mobjects(hint_1)
        
        # 前面
        face_front_poly = Polygon(
            *self.face_front,
            fill_color=RED,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.play(
            FadeIn(face_front_poly),
            FadeIn(hint_1),
            counter.animate.set_value(1),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 旋转显示后面
        self.move_camera(theta=-225*DEGREES, run_time=1.0)
        
        # 后面
        face_back_poly = Polygon(
            *self.face_back,
            fill_color=RED,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.play(
            FadeIn(face_back_poly),
            counter.animate.set_value(2),
            run_time=0.8
        )
        self.wait(0.5)
        
        # ===== 左右两个面 =====
        self.play(FadeOut(hint_1), run_time=0.3)
        self.remove(hint_1)
        
        hint_2 = Text(
            "左右 2 个面",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GREEN
        )
        hint_2.move_to(DOWN * 5)
        self.add_fixed_in_frame_mobjects(hint_2)
        
        self.move_camera(theta=-135*DEGREES, run_time=0.8)
        
        self.play(
            FadeOut(face_front_poly),
            FadeOut(face_back_poly),
            FadeIn(hint_2),
            run_time=0.5
        )
        
        # 左面
        face_left_poly = Polygon(
            *self.face_left,
            fill_color=GREEN,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.play(
            FadeIn(face_left_poly),
            counter.animate.set_value(3),
            run_time=0.8
        )
        self.wait(0.3)
        
        # 右面
        face_right_poly = Polygon(
            *self.face_right,
            fill_color=GREEN,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.play(
            FadeIn(face_right_poly),
            counter.animate.set_value(4),
            run_time=0.8
        )
        self.wait(0.5)
        
        # ===== 上下两个面 =====
        self.play(FadeOut(hint_2), run_time=0.3)
        self.remove(hint_2)
        
        hint_3 = Text(
            "上下 2 个面",
            font="Noto Sans CJK SC",
            font_size=24,
            color=BLUE
        )
        hint_3.move_to(DOWN * 5)
        self.add_fixed_in_frame_mobjects(hint_3)
        
        self.move_camera(phi=50*DEGREES, theta=-45*DEGREES, run_time=0.8)
        
        self.play(
            FadeOut(face_left_poly),
            FadeOut(face_right_poly),
            FadeIn(hint_3),
            run_time=0.5
        )
        
        # 上面
        face_top_poly = Polygon(
            *self.face_top,
            fill_color=BLUE,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.play(
            FadeIn(face_top_poly),
            counter.animate.set_value(5),
            run_time=0.8
        )
        self.wait(0.3)
        
        # 下面
        face_bottom_poly = Polygon(
            *self.face_bottom,
            fill_color=BLUE,
            fill_opacity=0.3,
            stroke_width=0
        )
        
        self.play(
            FadeIn(face_bottom_poly),
            counter.animate.set_value(6),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 恢复视角
        self.move_camera(phi=70*DEGREES, theta=-45*DEGREES, run_time=0.6)
        
        # ===== 对面关系 =====
        self.play(FadeOut(hint_3), run_time=0.3)
        self.remove(hint_3)
        
        opposite_hint = Text(
            "对面完全相同",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        )
        opposite_hint.move_to(DOWN * 5)
        self.add_fixed_in_frame_mobjects(opposite_hint)
        
        self.play(FadeIn(opposite_hint), run_time=0.5)
        self.wait(0.5)
        
        # 欧拉公式
        formula_f = MathTex("F = 6", font_size=32, color=self.COLOR_FACE)
        formula_f.move_to(DOWN * 6)
        self.add_fixed_in_frame_mobjects(formula_f)
        
        self.play(Write(formula_f), run_time=0.5)
        self.wait(0.5)
        
        # ===== 清理 =====
        self.play(
            FadeOut(title),
            FadeOut(definition),
            FadeOut(counter),
            FadeOut(opposite_hint),
            FadeOut(formula_f),
            FadeOut(face_top_poly),
            FadeOut(face_bottom_poly),
            run_time=0.6
        )
        self.remove(
            title, definition, counter, opposite_hint, formula_f,
            face_top_poly, face_bottom_poly
        )
    
    def scene_5_euler_formula(self):
        """
        场景5: 欧拉公式验证 (40-52s)
        目的：引入并验证欧拉公式 V - E + F = 2
        """
        # ===== 回顾标题 =====
        title = Text(
            "验证一个神奇的公式",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD
        )
        title.move_to(UP * 6)
        self.add_fixed_in_frame_mobjects(title)
        
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)
        
        # ===== 数据列表 =====
        data_v = MathTex("V = 8", font_size=28, color=self.COLOR_VERTEX)
        data_e = MathTex("E = 12", font_size=28, color=self.COLOR_EDGE)
        data_f = MathTex("F = 6", font_size=28, color=self.COLOR_FACE)
        
        data_group = VGroup(data_v, data_e, data_f).arrange(DOWN, buff=0.3)
        data_group.move_to(UP * 4.5)
        self.add_fixed_in_frame_mobjects(data_group)
        
        self.play(
            FadeIn(data_v, shift=RIGHT*0.3),
            run_time=0.4
        )
        self.wait(0.2)
        self.play(
            FadeIn(data_e, shift=RIGHT*0.3),
            run_time=0.4
        )
        self.wait(0.2)
        self.play(
            FadeIn(data_f, shift=RIGHT*0.3),
            run_time=0.4
        )
        self.wait(0.5)
        
        # 长方体旋转
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(1.0)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=70*DEGREES, theta=-45*DEGREES, run_time=0.5)
        
        # ===== 欧拉公式出现 =====
        formula_step1 = MathTex(
            "V - E + F = ?",
            font_size=36,
            color=WHITE
        )
        formula_step1.move_to(DOWN * 2)
        self.add_fixed_in_frame_mobjects(formula_step1)
        
        self.play(Write(formula_step1), run_time=0.8)
        self.wait(0.5)
        
        # ===== 代入数值 =====
        formula_step2 = MathTex(
            "8 - 12 + 6 = ?",
            font_size=36,
            color=WHITE
        )
        formula_step2.move_to(DOWN * 2)
        self.add_fixed_in_frame_mobjects(formula_step2)
        
        self.play(TransformMatchingTex(formula_step1, formula_step2), run_time=0.7)
        self.wait(0.5)
        
        # ===== 计算结果 =====
        formula_step3 = MathTex(
            "8 - 12 + 6 = 2",
            font_size=36,
            color=GOLD
        )
        formula_step3.move_to(DOWN * 2)
        self.add_fixed_in_frame_mobjects(formula_step3)
        
        self.play(
            TransformMatchingTex(formula_step2, formula_step3),
            run_time=0.6
        )
        self.play(
            Flash(formula_step3, color=GOLD, flash_radius=0.8),
            run_time=0.6
        )
        self.wait(0.5)
        
        # ===== 欧拉公式解释 =====
        self.play(FadeOut(title), run_time=0.3)
        self.remove(title)
        
        euler_title = Text(
            "欧拉公式",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        )
        euler_title.move_to(UP * 6)
        self.add_fixed_in_frame_mobjects(euler_title)
        
        explanation = Text(
            "适用于所有凸多面体！",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        )
        explanation.move_to(UP * 5.3)
        self.add_fixed_in_frame_mobjects(explanation)
        
        self.play(
            FadeIn(euler_title),
            FadeIn(explanation),
            run_time=0.6
        )
        self.wait(0.5)
        
        # ===== 神奇常数强调 =====
        emphasis = Text(
            "神奇的常数 2",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        )
        emphasis.move_to(DOWN * 3.5)
        self.add_fixed_in_frame_mobjects(emphasis)
        
        self.play(FadeIn(emphasis, scale=1.2), run_time=0.5)
        self.wait(1.0)
        
        # ===== 记忆卡片 =====
        self.play(
            FadeOut(data_group),
            FadeOut(formula_step3),
            FadeOut(euler_title),
            FadeOut(explanation),
            FadeOut(emphasis),
            run_time=0.5
        )
        self.remove(data_group, formula_step3, euler_title, explanation, emphasis)
        
        # 创建4张记忆卡片
        card_1 = self.create_memory_card("8个顶点", self.COLOR_VERTEX)
        card_2 = self.create_memory_card("12条棱 (3组×4)", self.COLOR_EDGE)
        card_3 = self.create_memory_card("6个面 (3对)", self.COLOR_FACE)
        card_4 = self.create_memory_card("V-E+F=2", GOLD)
        
        cards = VGroup(card_1, card_2, card_3, card_4).arrange(DOWN, buff=0.4)
        cards.move_to(ORIGIN)
        self.add_fixed_in_frame_mobjects(cards)
        
        for card in cards:
            card.shift(LEFT * 10)  # 初始在屏幕外
        
        # 依次滑入
        for card in cards:
            self.play(card.animate.shift(RIGHT * 10), run_time=0.4)
            self.wait(0.1)
        
        self.wait(1.0)
        
        # ===== 清理 =====
        self.play(FadeOut(cards), run_time=0.6)
        self.remove(cards)
    
    def create_memory_card(self, text, color):
        """创建记忆卡片"""
        # 图标
        icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 文字
        if "V-E+F" in text:
            label = MathTex(text, font_size=24, color=WHITE)
        else:
            label = Text(text, font="Noto Sans CJK SC", font_size=24, color=WHITE)
        
        # 组合
        card = VGroup(icon, label).arrange(RIGHT, buff=0.3)
        return card
    
    def scene_6_cube(self):
        """
        场景6: 特殊情况 - 正方体 (52-60s)
        目的：引出正方体是特殊的长方体
        """
        # ===== 标题 =====
        title = Text(
            "特殊的长方体",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        )
        title.move_to(UP * 6)
        self.add_fixed_in_frame_mobjects(title)
        
        self.play(Write(title), run_time=0.6)
        self.wait(0.5)
        
        # ===== 变形动画 =====
        # 创建正方体（边长取三者的平均值）
        avg_size = (self.length + self.width + self.height) / 3
        
        cube = Cube(
            side_length=avg_size * self.SCALE,
            fill_color=self.COLOR_CUBOID,
            fill_opacity=0.3,
            stroke_color=GOLD,
            stroke_width=3
        ).shift(self.OFFSET)
        
        hint = Text(
            "长宽高逐渐相等...",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        )
        hint.move_to(UP * 5.3)
        self.add_fixed_in_frame_mobjects(hint)
        
        self.play(FadeIn(hint), run_time=0.4)
        
        # 变形
        self.play(
            Transform(self.cuboid, cube),
            run_time=2.0,
            rate_func=smooth
        )
        
        self.play(FadeOut(hint), run_time=0.3)
        self.remove(hint)
        
        # ===== 正方体标注 =====
        cube_label = Text(
            "正方体",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GOLD
        )
        cube_label.move_to(UP * 5.3)
        self.add_fixed_in_frame_mobjects(cube_label)
        
        self.play(FadeIn(cube_label, scale=1.2), run_time=0.5)
        self.wait(0.5)
        
        # ===== 性质说明 =====
        property_1 = Text(
            "12条棱全部相等",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_EDGE
        )
        property_1.move_to(DOWN * 3)
        self.add_fixed_in_frame_mobjects(property_1)
        
        self.play(FadeIn(property_1), run_time=0.5)
        self.wait(0.5)
        
        property_2 = Text(
            "6个面都是正方形",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_FACE
        )
        property_2.move_to(DOWN * 4)
        self.add_fixed_in_frame_mobjects(property_2)
        
        self.play(FadeIn(property_2), run_time=0.5)
        self.wait(0.5)
        
        conclusion = Text(
            "正方体是特殊的长方体",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        )
        conclusion.move_to(DOWN * 5.5)
        self.add_fixed_in_frame_mobjects(conclusion)
        
        self.play(FadeIn(conclusion, scale=1.1), run_time=0.6)
        self.wait(1.0)
        
        # ===== 清理 =====
        self.play(
            FadeOut(title),
            FadeOut(cube_label),
            FadeOut(property_1),
            FadeOut(property_2),
            FadeOut(conclusion),
            FadeOut(self.vertex_dots),
            run_time=0.6
        )
        self.remove(
            title, cube_label, property_1, property_2, conclusion,
            self.vertex_dots
        )
    
    def scene_7_outro(self):
        """
        场景7: 片尾关注 (60-75s)
        目的：总结 + 关注引导
        """
        # ===== 快速回顾 =====
        # 长方体旋转
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(1.0)
        
        # 要点快闪
        point_1 = Text(
            "8个顶点 ●",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_VERTEX
        )
        point_1.move_to(UP * 3)
        self.add_fixed_in_frame_mobjects(point_1)
        
        self.play(FadeIn(point_1, shift=LEFT*0.3), run_time=0.5)
        self.wait(0.5)
        
        point_2 = Text(
            "12条棱 ━",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_EDGE
        )
        point_2.move_to(UP * 2)
        self.add_fixed_in_frame_mobjects(point_2)
        
        self.play(FadeIn(point_2, shift=LEFT*0.3), run_time=0.5)
        self.wait(0.5)
        
        point_3 = Text(
            "6个面 ▢",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_FACE
        )
        point_3.move_to(UP * 1)
        self.add_fixed_in_frame_mobjects(point_3)
        
        self.play(FadeIn(point_3, shift=LEFT*0.3), run_time=0.5)
        self.wait(0.5)
        
        point_4 = MathTex(
            "V - E + F = 2",
            font_size=32,
            color=GOLD
        )
        point_4.move_to(ORIGIN)
        self.add_fixed_in_frame_mobjects(point_4)
        
        self.play(Write(point_4), run_time=0.6)
        self.play(
            Flash(point_4, color=GOLD, flash_radius=0.6),
            run_time=0.5
        )
        self.wait(1.0)
        
        self.stop_ambient_camera_rotation()
        
        # ===== 作者信息放大 =====
        self.play(
            FadeOut(point_1),
            FadeOut(point_2),
            FadeOut(point_3),
            FadeOut(point_4),
            run_time=0.5
        )
        self.remove(point_1, point_2, point_3, point_4)
        
        # 作者名放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        )
        author_name.move_to(UP * 2)
        self.add_fixed_in_frame_mobjects(author_name)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        )
        author_id.move_to(UP * 1)
        self.add_fixed_in_frame_mobjects(author_id)
        
        self.play(FadeIn(author_id, shift=UP*0.3), run_time=0.5)
        self.wait(0.5)
        
        # ===== 关注提示 =====
        follow_text = Text(
            "关注我，学更多数学知识！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        )
        follow_text.move_to(DOWN * 1)
        self.add_fixed_in_frame_mobjects(follow_text)
        
        self.play(FadeIn(follow_text, shift=UP*0.3, scale=1.1), run_time=0.6)
        self.wait(0.5)
        
        # ===== 小长方体装饰 =====
        decorations = VGroup(*[
            Cube(side_length=0.3, fill_opacity=0.8, fill_color=GOLD)
            .move_to(follow_text.get_center() + 1.5 * np.array([
                np.cos(i * TAU / 6), 
                np.sin(i * TAU / 6), 
                0
            ]))
            for i in range(6)
        ])
        # 3D装饰需要添加到场景
        for dec in decorations:
            self.add(dec)
        
        self.play(
            *[FadeIn(dec, scale=0.5) for dec in decorations],
            run_time=0.6
        )
        
        # 旋转装饰
        self.play(
            Rotate(decorations, angle=PI, run_time=1.5)
        )
        
        # ===== 图标闪烁 =====
        icons = VGroup(
            Circle(radius=0.2, color=self.COLOR_VERTEX, fill_opacity=0.8).shift(LEFT*2 + DOWN*3),
            Circle(radius=0.2, color=self.COLOR_EDGE, fill_opacity=0.8).shift(LEFT*1 + DOWN*3),
            Circle(radius=0.2, color=self.COLOR_FACE, fill_opacity=0.8).shift(DOWN*3),
            Circle(radius=0.2, color=GOLD, fill_opacity=0.8).shift(RIGHT*1 + DOWN*3),
        )
        
        self.add_fixed_in_frame_mobjects(icons)
        
        self.play(*[FadeIn(icon, scale=0.5) for icon in icons], run_time=0.6)
        self.wait(0.5)
        
        # ===== 优雅结束 =====
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(2.0)
        self.stop_ambient_camera_rotation()
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            FadeOut(icons),
            FadeOut(self.cuboid),
            run_time=1.0
        )


# ==================== 主程序 ====================
if __name__ == "__main__":
    """
    渲染命令：
    
    # 快速预览（低质量）
    manim -pql cuboid_elements.py CuboidElements
    
    # 高质量（1080p）
    manim -qh cuboid_elements.py CuboidElements
    
    # 4K质量
    manim -qk cuboid_elements.py CuboidElements
    """
    pass