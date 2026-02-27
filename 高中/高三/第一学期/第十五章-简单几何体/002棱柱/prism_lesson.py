"""
棱柱 (Prism) 教学动画
Manim 0.19.2 for TikTok vertical format (1080×1920)

内容: 棱柱的定义、分类、性质和计算公式
目标观众: 高三学生
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ========== 全局配置 - TikTok竖屏尺寸 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class PrismLesson(ThreeDScene):
    """
    棱柱教学动画场景
    
    场景顺序:
    1. 开场钩子 - 引入棱柱概念
    2. 棱柱定义 - 三要素说明
    3. 分类(按底面) - 三棱柱、四棱柱、五棱柱
    4. 分类(棱柱类型) - 直棱柱vs斜棱柱
    5. 正棱柱 - 定义和特征
    6. 体积和表面积公式 - 推导和计算
    7. 总结与片尾 - 要点回顾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"      # 蓝色 - 主棱柱
        self.COLOR_SECONDARY = "#e74c3c"    # 红色 - 高亮边
        self.COLOR_HIGHLIGHT = YELLOW        # 黄色 - 强调元素
        self.COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
        self.COLOR_BASE = "#2ecc71"         # 绿色 - 底面
        self.COLOR_LATERAL = "#9b59b6"      # 紫色 - 侧面
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 设置3D相机
        self.setup_camera()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_classification_by_base()
        self.scene_4_straight_vs_oblique()
        self.scene_5_regular_prism()
        self.scene_6_volume_and_surface_area()
        self.scene_7_summary()
    
    def setup_geometry(self):
        """初始化所有几何数据 - 精确计算"""
        
        # ========== 基础参数 ==========
        self.base_side = 2.0
        self.height = 3.0
        self.scale_factor = 0.7  # 整体缩放
        
        # ========== 三棱柱底面顶点（正三角形）==========
        self.A_bottom = np.array([-1.0, 0.0, 0.0])
        self.B_bottom = np.array([1.0, 0.0, 0.0])
        self.C_bottom = np.array([0.0, np.sqrt(3), 0.0])
        
        # ========== 三棱柱顶面顶点（直棱柱）==========
        self.A_top = self.A_bottom + np.array([0, 0, self.height])
        self.B_top = self.B_bottom + np.array([0, 0, self.height])
        self.C_top = self.C_bottom + np.array([0, 0, self.height])
        
        # ========== 斜棱柱顶面顶点 ==========
        tilt_angle = PI / 6  # 30度
        oblique_offset = self.height * np.tan(tilt_angle)
        
        self.A_top_oblique = self.A_bottom + np.array([oblique_offset, 0, self.height])
        self.B_top_oblique = self.B_bottom + np.array([oblique_offset, 0, self.height])
        self.C_top_oblique = self.C_bottom + np.array([oblique_offset, 0, self.height])
        
        # ========== 计算面积和体积 ==========
        self.base_area = (np.sqrt(3) / 4) * self.base_side**2
        self.volume = self.base_area * self.height
        self.perimeter = 3 * self.base_side
        self.lateral_area = self.perimeter * self.height
        self.surface_area = 2 * self.base_area + self.lateral_area
        
        # ========== 验证几何 ==========
        self.verify_geometry()
        
        print(f"✓ 几何初始化完成")
        print(f"  底面积: {self.base_area:.3f}")
        print(f"  体积: {self.volume:.3f}")
        print(f"  表面积: {self.surface_area:.3f}")
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证底面是等边三角形
        AB = np.linalg.norm(self.B_bottom - self.A_bottom)
        BC = np.linalg.norm(self.C_bottom - self.B_bottom)
        CA = np.linalg.norm(self.A_bottom - self.C_bottom)
        
        assert abs(AB - self.base_side) < epsilon, "底面边长AB错误"
        assert abs(BC - self.base_side) < epsilon, "底面边长BC错误"
        assert abs(CA - self.base_side) < epsilon, "底面边长CA错误"
        
        # 验证侧棱平行且相等
        edge1 = self.A_top - self.A_bottom
        edge2 = self.B_top - self.B_bottom
        edge3 = self.C_top - self.C_bottom
        
        assert np.allclose(edge1, edge2, atol=epsilon), "侧棱不平行"
        assert np.allclose(edge2, edge3, atol=epsilon), "侧棱不平行"
        
        print("✓ 几何验证通过")
    
    def setup_camera(self):
        """设置3D相机初始角度"""
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
    
    def create_prism(self, vertices_bottom, vertices_top, color=None):
        """
        创建棱柱3D对象
        
        Args:
            vertices_bottom: 底面顶点列表
            vertices_top: 顶面顶点列表
            color: 颜色
        """
        if color is None:
            color = self.COLOR_PRIMARY
        
        # 底面
        bottom_face = Polygon(
            *vertices_bottom,
            color=color,
            fill_opacity=0.3,
            stroke_width=2
        )
        
        # 顶面
        top_face = Polygon(
            *vertices_top,
            color=color,
            fill_opacity=0.3,
            stroke_width=2
        )
        
        # 侧棱
        n = len(vertices_bottom)
        edges = VGroup()
        for i in range(n):
            edge = Line3D(
                vertices_bottom[i],
                vertices_top[i],
                color=color,
                stroke_width=2
            )
            edges.add(edge)
        
        # 底面边
        bottom_edges = VGroup()
        for i in range(n):
            edge = Line3D(
                vertices_bottom[i],
                vertices_bottom[(i+1) % n],
                color=color,
                stroke_width=2
            )
            bottom_edges.add(edge)
        
        # 顶面边
        top_edges = VGroup()
        for i in range(n):
            edge = Line3D(
                vertices_top[i],
                vertices_top[(i+1) % n],
                color=color,
                stroke_width=2
            )
            top_edges.add(edge)
        
        # 组合
        prism = VGroup(bottom_face, top_face, edges, bottom_edges, top_edges)
        return prism
    
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        
        # 作者信息（固定在相机平面）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        )
        self.author_info.to_edge(UP, buff=0.3)
        self.author_info.set_opacity(0)          # 初始透明
        self.add_fixed_in_frame_mobjects(self.author_info)
        self.play(FadeIn(self.author_info), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "什么是棱柱?",
            font="Noto Sans CJK SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        )
        hook_text.move_to(UP * 2)
        hook_text.set_opacity(0)
        self.add_fixed_in_frame_mobjects(hook_text)
        self.play(FadeIn(hook_text), run_time=0.8)
        self.wait(0.5)
        
        # 创建主三棱柱
        vertices_bottom = [self.A_bottom, self.B_bottom, self.C_bottom]
        vertices_top = [self.A_top, self.B_top, self.C_top]
        
        self.main_prism = self.create_prism(
            vertices_bottom,
            vertices_top,
            color=self.COLOR_PRIMARY
        )
        self.main_prism.scale(self.scale_factor)
        self.main_prism.shift(DOWN * 0.5)
        
        self.play(Create(self.main_prism), run_time=1.5)
        self.wait(0.5)
        
        # 旋转展示
        self.play(
            Rotate(self.main_prism, angle=PI/3, axis=UP, run_time=2),
            self.camera.animate.set_phi(60 * DEGREES).set_theta(-30 * DEGREES),
            run_time=2
        )
        self.wait(0.5)
        
        # 清理
        self.play(FadeOut(hook_text), run_time=0.5)
        
        # 恢复相机
        self.play(
            self.camera.animate.set_phi(70 * DEGREES).set_theta(-45 * DEGREES),
            run_time=1
        )
    
    def scene_2_definition(self):
        """场景2: 棱柱定义 - 三要素"""
        
        # 标题
        title = Text(
            "棱柱的定义",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        )
        title.to_edge(UP, buff=1.5)
        title.set_opacity(0)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=0.6)
        self.wait(0.5)
        
        # 要素1: 两底面
        explain_1 = Text(
            "两底面: 平行且全等",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_BASE
        )
        explain_1.to_edge(DOWN, buff=3.5)
        explain_1.set_opacity(0)
        self.add_fixed_in_frame_mobjects(explain_1)
        
        # 高亮底面
        bottom_face = self.main_prism[0]
        top_face = self.main_prism[1]
        
        self.play(
            bottom_face.animate.set_color(self.COLOR_BASE).set_fill_opacity(0.6),
            top_face.animate.set_color(self.COLOR_BASE).set_fill_opacity(0.6),
            run_time=0.8
        )
        self.play(FadeIn(explain_1), run_time=0.5)
        self.wait(1.2)
        
        # 要素2: 侧面
        explain_2 = Text(
            "侧面: 平行四边形",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_LATERAL
        )
        explain_2.to_edge(DOWN, buff=2.5)
        explain_2.set_opacity(0)
        self.add_fixed_in_frame_mobjects(explain_2)
        
        # 创建侧面（示例：一个侧面）
        side_face_1 = Polygon(
            self.A_bottom * self.scale_factor + DOWN * 0.5,
            self.B_bottom * self.scale_factor + DOWN * 0.5,
            self.B_top * self.scale_factor + DOWN * 0.5,
            self.A_top * self.scale_factor + DOWN * 0.5,
            color=self.COLOR_LATERAL,
            fill_opacity=0.5,
            stroke_width=3
        )
        
        self.play(
            FadeOut(explain_1),
            bottom_face.animate.set_color(self.COLOR_PRIMARY).set_fill_opacity(0.3),
            top_face.animate.set_color(self.COLOR_PRIMARY).set_fill_opacity(0.3),
            run_time=0.4
        )
        
        self.play(
            FadeIn(side_face_1),
            FadeIn(explain_2),
            run_time=0.8
        )
        self.wait(1.2)
        
        # 要素3: 侧棱
        explain_3 = Text(
            "侧棱: 平行且相等",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SECONDARY
        )
        explain_3.to_edge(DOWN, buff=1.5)
        explain_3.set_opacity(0)
        self.add_fixed_in_frame_mobjects(explain_3)
        
        # 高亮侧棱
        edges = self.main_prism[2]
        
        self.play(
            FadeOut(explain_2),
            FadeOut(side_face_1),
            run_time=0.4
        )
        
        self.play(
            edges.animate.set_color(self.COLOR_SECONDARY).set_stroke_width(4),
            FadeIn(explain_3),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(explain_3),
            edges.animate.set_color(self.COLOR_PRIMARY).set_stroke_width(2),
            run_time=0.6
        )
    
    def scene_3_classification_by_base(self):
        """场景3: 按底面形状分类"""
        
        # 标题
        title = Text(
            "按底面形状分类",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        )
        title.to_edge(UP, buff=1.5)
        title.set_opacity(0)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=0.6)
        
        # 将主三棱柱移至左侧
        self.play(
            self.main_prism.animate.scale(0.6).shift(LEFT * 2.5 + UP * 0.5),
            run_time=0.8
        )
        
        # 创建四棱柱（正方形底）
        square_side = 1.5
        square_bottom = [
            np.array([-square_side/2, -square_side/2, 0]),
            np.array([square_side/2, -square_side/2, 0]),
            np.array([square_side/2, square_side/2, 0]),
            np.array([-square_side/2, square_side/2, 0])
        ]
        square_top = [v + np.array([0, 0, 2.5]) for v in square_bottom]
        
        quad_prism = self.create_prism(square_bottom, square_top, color="#e67e22")
        quad_prism.scale(0.35).shift(UP * 0.5)
        
        self.play(Create(quad_prism), run_time=1.0)
        
        # 创建五棱柱（正五边形底）
        n = 5
        penta_radius = 0.8
        penta_bottom = [
            np.array([penta_radius * np.cos(2*PI*i/n), 
                     penta_radius * np.sin(2*PI*i/n), 0])
            for i in range(n)
        ]
        penta_top = [v + np.array([0, 0, 2.5]) for v in penta_bottom]
        
        penta_prism = self.create_prism(penta_bottom, penta_top, color="#16a085")
        penta_prism.scale(0.35).shift(RIGHT * 2.5 + UP * 0.5)
        
        self.play(Create(penta_prism), run_time=1.0)
        
        # 标签
        label_tri = Text("三棱柱", font="Noto Sans CJK SC", font_size=18, color=WHITE)
        label_tri.move_to(LEFT * 3 + DOWN * 2)
        label_tri.set_opacity(0)
        self.add_fixed_in_frame_mobjects(label_tri)
        
        label_quad = Text("四棱柱", font="Noto Sans CJK SC", font_size=18, color=WHITE)
        label_quad.move_to(DOWN * 2)
        label_quad.set_opacity(0)
        self.add_fixed_in_frame_mobjects(label_quad)
        
        label_penta = Text("五棱柱", font="Noto Sans CJK SC", font_size=18, color=WHITE)
        label_penta.move_to(RIGHT * 3 + DOWN * 2)
        label_penta.set_opacity(0)
        self.add_fixed_in_frame_mobjects(label_penta)
        
        self.play(
            FadeIn(label_tri),
            FadeIn(label_quad),
            FadeIn(label_penta),
            run_time=0.6
        )
        
        # 公式
        formula = Text(
            "n棱柱: 底面为n边形",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        )
        formula.to_edge(DOWN, buff=1.5)
        formula.set_opacity(0)
        self.add_fixed_in_frame_mobjects(formula)
        
        self.play(FadeIn(formula), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(quad_prism),
            FadeOut(penta_prism),
            FadeOut(label_tri),
            FadeOut(label_quad),
            FadeOut(label_penta),
            FadeOut(formula),
            self.main_prism.animate.scale(1/0.6).shift(RIGHT * 2.5 + DOWN * 0.5),
            run_time=0.8
        )
    
    def scene_4_straight_vs_oblique(self):
        """场景4: 直棱柱vs斜棱柱"""
        
        # 标题
        title = Text(
            "直棱柱 vs 斜棱柱",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        )
        title.to_edge(UP, buff=1.5)
        title.set_opacity(0)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=0.6)
        
        # 直棱柱移至左侧
        self.play(
            self.main_prism.animate.scale(0.7).shift(LEFT * 2),
            run_time=0.8
        )
        
        # 创建斜棱柱
        vertices_bottom = [self.A_bottom, self.B_bottom, self.C_bottom]
        vertices_top_oblique = [self.A_top_oblique, self.B_top_oblique, self.C_top_oblique]
        
        oblique_prism = self.create_prism(
            vertices_bottom,
            vertices_top_oblique,
            color="#c0392b"
        )
        oblique_prism.scale(self.scale_factor * 0.7).shift(RIGHT * 2 + DOWN * 0.5)
        
        self.play(Create(oblique_prism), run_time=1.2)
        
        # 直棱柱标注
        label_straight = Text("直棱柱", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        label_straight.move_to(LEFT * 2.5 + DOWN * 3)
        label_straight.set_opacity(0)
        self.add_fixed_in_frame_mobjects(label_straight)
        
        explain_straight = Text(
            "侧棱⊥底面",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        )
        explain_straight.move_to(LEFT * 2.5 + DOWN * 3.8)
        explain_straight.set_opacity(0)
        self.add_fixed_in_frame_mobjects(explain_straight)
        
        # 斜棱柱标注
        label_oblique = Text("斜棱柱", font="Noto Sans CJK SC", font_size=20, color=WHITE)
        label_oblique.move_to(RIGHT * 2.5 + DOWN * 3)
        label_oblique.set_opacity(0)
        self.add_fixed_in_frame_mobjects(label_oblique)
        
        explain_oblique = Text(
            "侧棱与底面成角",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_A
        )
        explain_oblique.move_to(RIGHT * 2.5 + DOWN * 3.8)
        explain_oblique.set_opacity(0)
        self.add_fixed_in_frame_mobjects(explain_oblique)
        
        self.play(
            FadeIn(label_straight),
            FadeIn(explain_straight),
            FadeIn(label_oblique),
            FadeIn(explain_oblique),
            run_time=0.8
        )
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(oblique_prism),
            FadeOut(label_straight),
            FadeOut(explain_straight),
            FadeOut(label_oblique),
            FadeOut(explain_oblique),
            self.main_prism.animate.scale(1/0.7).shift(RIGHT * 2),
            run_time=0.8
        )
    
    def scene_5_regular_prism(self):
        """场景5: 正棱柱"""
        
        # 标题
        title = Text(
            "正棱柱",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        )
        title.to_edge(UP, buff=1.5)
        title.set_opacity(0)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=0.6)
        
        # 定义1
        definition_1 = Text(
            "底面是正多边形",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_BASE
        )
        definition_1.to_edge(DOWN, buff=3.5)
        definition_1.set_opacity(0)
        self.add_fixed_in_frame_mobjects(definition_1)
        
        # 高亮底面
        bottom_face = self.main_prism[0]
        
        self.play(
            bottom_face.animate.set_color(self.COLOR_BASE).set_fill_opacity(0.6),
            FadeIn(definition_1),
            run_time=0.8
        )
        self.wait(1.2)
        
        # 定义2
        definition_2 = Text(
            "侧棱垂直于底面",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SECONDARY
        )
        definition_2.to_edge(DOWN, buff=2.5)
        definition_2.set_opacity(0)
        self.add_fixed_in_frame_mobjects(definition_2)
        
        # 高亮侧棱
        edges = self.main_prism[2]
        
        self.play(
            FadeOut(definition_1),
            bottom_face.animate.set_color(self.COLOR_PRIMARY).set_fill_opacity(0.3),
            edges.animate.set_color(self.COLOR_SECONDARY).set_stroke_width(4),
            FadeIn(definition_2),
            run_time=0.8
        )
        self.wait(1.2)
        
        # 完整定义
        full_definition = Text(
            "正n棱柱 = 直棱柱 + 正n边形底",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        )
        full_definition.to_edge(DOWN, buff=1.5)
        full_definition.set_opacity(0)
        self.add_fixed_in_frame_mobjects(full_definition)
        
        self.play(
            FadeOut(definition_2),
            edges.animate.set_color(self.COLOR_PRIMARY).set_stroke_width(2),
            FadeIn(full_definition),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(full_definition),
            run_time=0.6
        )
    
    def scene_6_volume_and_surface_area(self):
        """场景6: 体积和表面积公式"""
        
        # 标题
        title = Text(
            "体积和表面积",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE
        )
        title.to_edge(UP, buff=1.5)
        title.set_opacity(0)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title), run_time=0.6)
        
        # 体积公式
        volume_title = Text(
            "体积公式:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        )
        volume_title.to_edge(DOWN, buff=5.5).shift(LEFT * 2)
        volume_title.set_opacity(0)
        self.add_fixed_in_frame_mobjects(volume_title)
        
        volume_formula = MathTex(
            r"V = S_{\text{底}} \cdot h",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        )
        volume_formula.next_to(volume_title, RIGHT, buff=0.5)
        volume_formula.set_opacity(0)
        self.add_fixed_in_frame_mobjects(volume_formula)
        
        self.play(
            FadeIn(volume_title),
            Write(volume_formula),
            run_time=1.0
        )
        
        # 数值示例
        volume_value = MathTex(
            rf"= {self.base_area:.2f} \times {self.height:.1f} = {self.volume:.2f}",
            font_size=24,
            color=GRAY_A
        )
        volume_value.next_to(volume_formula, DOWN, buff=0.3, aligned_edge=LEFT)
        volume_value.set_opacity(0)
        self.add_fixed_in_frame_mobjects(volume_value)
        
        self.play(FadeIn(volume_value), run_time=0.8)
        self.wait(1.5)
        
        # 表面积公式
        surface_title = Text(
            "表面积公式:",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        )
        surface_title.to_edge(DOWN, buff=3.5).shift(LEFT * 1.8)
        surface_title.set_opacity(0)
        self.add_fixed_in_frame_mobjects(surface_title)
        
        surface_formula = MathTex(
            r"S = 2S_{\text{底}} + S_{\text{侧}}",
            font_size=32,
            color=self.COLOR_HIGHLIGHT
        )
        surface_formula.next_to(surface_title, RIGHT, buff=0.5)
        surface_formula.set_opacity(0)
        self.add_fixed_in_frame_mobjects(surface_formula)
        
        self.play(
            FadeIn(surface_title),
            Write(surface_formula),
            run_time=1.0
        )
        
        # 侧面积公式
        lateral_formula = MathTex(
            r"S_{\text{侧}} = \text{周长} \cdot h",
            font_size=24,
            color=GRAY_A
        )
        lateral_formula.next_to(surface_formula, DOWN, buff=0.3, aligned_edge=LEFT)
        lateral_formula.set_opacity(0)
        self.add_fixed_in_frame_mobjects(lateral_formula)
        
        self.play(FadeIn(lateral_formula), run_time=0.8)
        
        # 数值示例
        surface_value = MathTex(
            rf"= 2 \times {self.base_area:.2f} + {self.lateral_area:.1f} = {self.surface_area:.2f}",
            font_size=20,
            color=GRAY_A
        )
        surface_value.next_to(lateral_formula, DOWN, buff=0.2, aligned_edge=LEFT)
        surface_value.set_opacity(0)
        self.add_fixed_in_frame_mobjects(surface_value)
        
        self.play(FadeIn(surface_value), run_time=0.8)
        self.wait(2.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(volume_title),
            FadeOut(volume_formula),
            FadeOut(volume_value),
            FadeOut(surface_title),
            FadeOut(surface_formula),
            FadeOut(lateral_formula),
            FadeOut(surface_value),
            run_time=0.6
        )
    
    def scene_7_summary(self):
        """场景7: 总结与片尾"""
        
        # 棱柱缩小移至左上
        self.play(
            self.main_prism.animate.scale(0.4).to_corner(UL, buff=0.8),
            run_time=1.0
        )
        
        # 相机正面视角
        self.play(
            self.camera.animate.set_phi(0 * DEGREES).set_theta(0 * DEGREES),
            run_time=1.5
        )
        
        # 要点卡片
        cards = VGroup()
        
        card_texts = [
            "两底面平行全等",
            "侧棱平行相等",
            r"$V = S_{\text{底}} \cdot h$",
            r"$S = 2S_{\text{底}} + S_{\text{侧}}$"
        ]
        
        card_colors = [
            self.COLOR_BASE,
            self.COLOR_SECONDARY,
            self.COLOR_HIGHLIGHT,
            GOLD
        ]
        
        for i, (text, color) in enumerate(zip(card_texts, card_colors)):
            # 检查是否包含数学公式
            if text.startswith(r"$"):
                # 使用MathTex
                content = MathTex(text[1:-1], font_size=22, color=WHITE)
            else:
                # 使用Text
                content = Text(text, font="Noto Sans CJK SC", font_size=22, color=WHITE)
            
            # 图标
            icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
            
            # 组合
            card = VGroup(icon, content).arrange(RIGHT, buff=0.4)
            card.move_to(UP * (1 - i * 1.2))
            card.shift(LEFT * 10)  # 初始在左侧外
            card.set_opacity(0)
            self.add_fixed_in_frame_mobjects(card)
            cards.add(card)
        
        # 卡片依次滑入
        for card in cards:
            card.set_opacity(1)
            self.play(card.animate.shift(RIGHT * 10), run_time=0.5)
            self.wait(0.3)
        
        self.wait(1.0)
        
        # 作者信息放大
        author_large = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        )
        author_large.move_to(DOWN * 3.5)
        author_large.set_opacity(0)
        self.add_fixed_in_frame_mobjects(author_large)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=26,
            color=GRAY_B
        )
        author_id.next_to(author_large, DOWN, buff=0.3)
        author_id.set_opacity(0)
        self.add_fixed_in_frame_mobjects(author_id)
        
        self.play(
            FadeOut(self.author_info),
            FadeIn(author_large),
            FadeIn(author_id),
            run_time=0.8
        )
        
        # 关注提示
        follow_text = Text(
            "关注获取更多立体几何技巧!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        )
        follow_text.next_to(author_id, DOWN, buff=0.8)
        follow_text.set_opacity(0)
        self.add_fixed_in_frame_mobjects(follow_text)
        
        self.play(FadeIn(follow_text), run_time=0.8)
        
        # 装饰图标
        icons = VGroup()
        for i in range(5):
            color = [self.COLOR_PRIMARY, self.COLOR_BASE, self.COLOR_HIGHLIGHT, 
                    self.COLOR_SECONDARY, self.COLOR_LATERAL][i]
            icon = Circle(radius=0.2, color=color, fill_opacity=0.8)
            icon.move_to(DOWN * 6 + (i - 2) * RIGHT * 1.2)
            icon.set_opacity(0)
            self.add_fixed_in_frame_mobjects(icon)
            icons.add(icon)
        
        self.play(*[FadeIn(icon) for icon in icons], run_time=0.6)
        self.wait(2.0)
        
        # 最终淡出
        self.play(
            *[FadeOut(mob) for mob in [cards, author_large, author_id, follow_text, icons, self.main_prism]],
            run_time=1.5
        )


# ========== 运行命令 ==========
# 快速预览:
# manim -pql prism_lesson.py PrismLesson
#
# 高质量渲染:
# manim -qh prism_lesson.py PrismLesson
#
# 4K质量:
# manim -qk prism_lesson.py PrismLesson