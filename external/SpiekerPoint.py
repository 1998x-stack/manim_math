"""
斯皮克点 (Spieker Point) 数学教学动画
使用 Manim 创建的竖屏短视频

内容: 斯皮克点的定义、构造、性质和几何意义
目标观众: 高中生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心概念:
1. 斯皮克点 = 中点三角形的内心
2. 斯皮克圆 = 中点三角形的内切圆  
3. 物理意义 = 周长的重心 (铁丝框的质心)
4. 关系: Sp = (G + Na) / 2
"""

from manim import *
import numpy as np


# ============================================================================
# 全局配置 - TikTok 竖屏尺寸
# ============================================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ============================================================================
# 几何计算工具类
# ============================================================================
class GeometryCalculator:
    """精确几何计算工具 - 所有计算必须使用此类"""
    
    @staticmethod
    def midpoint(P1, P2):
        """计算中点"""
        return (P1 + P2) / 2
    
    @staticmethod
    def incenter(A, B, C):
        """
        计算三角形内心
        使用加权平均公式: I = (a*A + b*B + c*C) / (a + b + c)
        其中 a = |BC|, b = |CA|, c = |AB|
        """
        a = np.linalg.norm(B - C)  # BC边长
        b = np.linalg.norm(C - A)  # CA边长
        c = np.linalg.norm(A - B)  # AB边长
        return (a * A + b * B + c * C) / (a + b + c)
    
    @staticmethod
    def centroid(A, B, C):
        """计算重心 - 简单平均"""
        return (A + B + C) / 3
    
    @staticmethod
    def distance_point_to_line(point, line_start, line_end):
        """计算点到直线的距离 - 使用叉积"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        cross_product = np.cross(point_vec[:2], line_vec[:2])
        return np.abs(cross_product) / np.linalg.norm(line_vec)
    
    @staticmethod
    def perpendicular_foot(point, line_start, line_end):
        """计算点到直线的垂足"""
        line_vec = line_end - line_start
        point_vec = point - line_start
        t = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
        return line_start + t * line_vec
    
    @staticmethod
    def nagel_point(A, B, C):
        """
        计算奈格尔点
        公式: Na = (s-a)*A + (s-b)*B + (s-c)*C / (s-a + s-b + s-c)
        其中 s = (a+b+c)/2 是半周长
        简化: Na = ((b+c-a)*A + (c+a-b)*B + (a+b-c)*C) / (a+b+c)
        """
        a = np.linalg.norm(B - C)
        b = np.linalg.norm(C - A)
        c = np.linalg.norm(A - B)
        
        weight_A = b + c - a
        weight_B = c + a - b
        weight_C = a + b - c
        
        total_weight = weight_A + weight_B + weight_C
        
        return (weight_A * A + weight_B * B + weight_C * C) / total_weight


# ============================================================================
# 主场景类
# ============================================================================
class SpiekerPointScene(Scene):
    """
    斯皮克点教学动画主场景
    
    场景顺序:
    1. 开场钩子
    2. 中点三角形构造
    3. 斯皮克点定义
    4. 斯皮克圆
    5. 周长重心
    6. 与重心、奈格尔点关系
    7. 重心坐标表示
    8. 总结与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_PRIMARY = "#3498db"        # 蓝色 - 主三角形
        self.COLOR_MEDIAL = "#e74c3c"         # 红色 - 中点三角形
        self.COLOR_SPIEKER = "#f39c12"        # 橙色 - 斯皮克点
        self.COLOR_INCIRCLE = "#2ecc71"       # 绿色 - 斯皮克圆
        self.COLOR_CENTROID = "#9b59b6"       # 紫色 - 重心
        self.COLOR_NAGEL = "#e67e22"          # 橙红 - 奈格尔点
        self.COLOR_HIGHLIGHT = YELLOW
        self.COLOR_AUXILIARY = GRAY_B
        self.COLOR_CONSTRUCTION = "#95a5a6"   # 灰色 - 辅助线
        
        # 初始化所有几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_medial_triangle()
        self.scene_3_spieker_definition()
        self.scene_4_spieker_circle()
        self.scene_5_perimeter_centroid()
        self.scene_6_centroid_nagel_relation()
        self.scene_7_barycentric_coordinates()
        self.scene_8_summary()
    
    def setup_geometry(self):
        """
        【核心】统一初始化所有几何数据
        所有坐标在此精确计算，后续场景只引用
        """
        print("=" * 60)
        print("初始化几何数据...")
        
        # ========== 基准参数 ==========
        self.SCALE = 1.1
        self.OFFSET = UP * 1.5
        
        # ========== 主三角形顶点 (使用斜三角形) ==========
        self.A = np.array([-2.5, 1.2, 0]) * self.SCALE + self.OFFSET
        self.B = np.array([2.8, -0.8, 0]) * self.SCALE + self.OFFSET
        self.C = np.array([-0.8, -2.2, 0]) * self.SCALE + self.OFFSET
        
        # ========== 边长 ==========
        self.a = np.linalg.norm(self.B - self.C)  # BC
        self.b = np.linalg.norm(self.C - self.A)  # CA
        self.c = np.linalg.norm(self.A - self.B)  # AB
        
        print(f"边长: a(BC)={self.a:.4f}, b(CA)={self.b:.4f}, c(AB)={self.c:.4f}")
        
        # ========== 中点三角形顶点 ==========
        self.D = GeometryCalculator.midpoint(self.B, self.C)  # BC中点
        self.E = GeometryCalculator.midpoint(self.C, self.A)  # CA中点
        self.F = GeometryCalculator.midpoint(self.A, self.B)  # AB中点
        
        print(f"中点: D={self.D[:2]}, E={self.E[:2]}, F={self.F[:2]}")
        
        # ========== 中点三角形边长 ==========
        self.d_ef = np.linalg.norm(self.F - self.E)  # EF
        self.d_fd = np.linalg.norm(self.D - self.F)  # FD
        self.d_de = np.linalg.norm(self.E - self.D)  # DE
        
        # ========== 斯皮克点 (中点三角形的内心) ==========
        self.Sp = GeometryCalculator.incenter(self.D, self.E, self.F)
        
        print(f"斯皮克点 Sp = {self.Sp[:2]}")
        
        # ========== 斯皮克圆半径 (中点三角形的内切圆半径) ==========
        self.spieker_radius = GeometryCalculator.distance_point_to_line(
            self.Sp, self.E, self.F
        )
        
        print(f"斯皮克圆半径 r = {self.spieker_radius:.4f}")
        
        # ========== 重心 ==========
        self.G = GeometryCalculator.centroid(self.A, self.B, self.C)
        
        print(f"重心 G = {self.G[:2]}")
        
        # ========== 奈格尔点 ==========
        self.Na = GeometryCalculator.nagel_point(self.A, self.B, self.C)
        
        print(f"奈格尔点 Na = {self.Na[:2]}")
        
        # ========== 验证几何关系 ==========
        self.verify_geometry()
        
        # ========== 创建三角形对象 (不添加到场景) ==========
        self.triangle_ABC = Polygon(
            self.A, self.B, self.C,
            color=self.COLOR_PRIMARY,
            stroke_width=3,
            fill_opacity=0.1,
            fill_color=self.COLOR_PRIMARY
        )
        
        self.medial_triangle_DEF = Polygon(
            self.D, self.E, self.F,
            color=self.COLOR_MEDIAL,
            stroke_width=3,
            fill_opacity=0.15,
            fill_color=self.COLOR_MEDIAL
        )
        
        print("几何数据初始化完成!")
        print("=" * 60)
    
    def verify_geometry(self):
        """验证所有几何计算的正确性"""
        epsilon = 1e-6
        errors = []
        
        print("\n【验证几何关系】")
        
        # ===== 1. 验证斯皮克点到中点三角形三边距离相等 =====
        dist_to_EF = GeometryCalculator.distance_point_to_line(self.Sp, self.E, self.F)
        dist_to_FD = GeometryCalculator.distance_point_to_line(self.Sp, self.F, self.D)
        dist_to_DE = GeometryCalculator.distance_point_to_line(self.Sp, self.D, self.E)
        
        print(f"  Sp到EF距离: {dist_to_EF:.6f}")
        print(f"  Sp到FD距离: {dist_to_FD:.6f}")
        print(f"  Sp到DE距离: {dist_to_DE:.6f}")
        
        if abs(dist_to_EF - dist_to_FD) > epsilon:
            errors.append(f"斯皮克点错误: 到EF={dist_to_EF:.6f}, 到FD={dist_to_FD:.6f}")
        if abs(dist_to_FD - dist_to_DE) > epsilon:
            errors.append(f"斯皮克点错误: 到FD={dist_to_FD:.6f}, 到DE={dist_to_DE:.6f}")
        
        # ===== 2. 验证 Sp = (G + Na) / 2 =====
        midpoint_G_Na = (self.G + self.Na) / 2
        diff = np.linalg.norm(self.Sp - midpoint_G_Na)
        
        print(f"  Sp = {self.Sp[:2]}")
        print(f"  (G+Na)/2 = {midpoint_G_Na[:2]}")
        print(f"  差值: {diff:.6f}")
        
        if diff > epsilon:
            errors.append(f"中点关系错误: ||Sp - (G+Na)/2|| = {diff:.6f}")
        
        # ===== 3. 验证中点三角形边长 = 原三角形边长 × 0.5 =====
        # EF 应该平行于 AB 且长度为 AB/2
        ratio_EF_AB = self.d_ef / self.c
        ratio_FD_BC = self.d_fd / self.a
        ratio_DE_CA = self.d_de / self.b
        
        print(f"  EF/AB = {ratio_EF_AB:.6f} (理论值 0.5)")
        print(f"  FD/BC = {ratio_FD_BC:.6f} (理论值 0.5)")
        print(f"  DE/CA = {ratio_DE_CA:.6f} (理论值 0.5)")
        
        if abs(ratio_EF_AB - 0.5) > epsilon:
            errors.append(f"中点三角形边长错误: EF/AB = {ratio_EF_AB:.6f}")
        
        # ===== 输出结果 =====
        if errors:
            print("\n❌ 几何验证失败:")
            for e in errors:
                print(f"  - {e}")
            raise ValueError("几何验证失败！请检查计算")
        else:
            print("\n✓ 几何验证通过!")
    
    # ========================================================================
    # Scene 1: 开场钩子 (0-5秒)
    # ========================================================================
    def scene_1_opening(self):
        """场景1: 开场 - 吸引注意力"""
        print("\n【Scene 1: 开场钩子】")
        
        # 作者信息 (顶部)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "周长的重心在哪里?",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        
        # 主三角形创建
        self.play(Create(self.triangle_ABC), run_time=1.0)
        
        # 中点三角形淡入
        medial_preview = self.medial_triangle_DEF.copy().set_opacity(0.5)
        self.play(Create(medial_preview, run_time=0.8))
        
        # 斯皮克点闪烁
        sp_preview = Dot(self.Sp, color=self.COLOR_SPIEKER, radius=0.1)
        self.play(FadeIn(sp_preview, scale=0.5), run_time=0.5)
        self.play(
            Flash(sp_preview, color=self.COLOR_SPIEKER, flash_radius=0.3),
            run_time=0.4
        )
        
        # 提示文字
        hint = Text(
            "答案藏在中点三角形里...",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(hint),
            FadeOut(sp_preview),
            FadeOut(medial_preview),
            self.triangle_ABC.animate.set_opacity(0.3),
            run_time=0.5
        )
    
    # ========================================================================
    # Scene 2: 中点三角形构造 (5-12秒)
    # ========================================================================
    def scene_2_medial_triangle(self):
        """场景2: 中点三角形的定义和构造"""
        print("\n【Scene 2: 中点三角形构造】")
        
        # 标题
        title = Text(
            "中点三角形",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_MEDIAL
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "Medial Triangle",
            font_size=24,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.6)
        
        # 恢复三角形透明度
        self.play(self.triangle_ABC.animate.set_opacity(1.0), run_time=0.3)
        
        # 边BC高亮 -> 中点D
        bc_edge = Line(self.B, self.C, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(bc_edge), run_time=0.4)
        
        dot_D = Dot(self.D, color=self.COLOR_MEDIAL, radius=0.08)
        label_D = Text("D", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(
            dot_D, DOWN, buff=0.1
        )
        
        self.play(
            FadeIn(dot_D, scale=0.5),
            Write(label_D),
            run_time=0.5
        )
        self.play(bc_edge.animate.set_color(self.COLOR_PRIMARY), run_time=0.2)
        
        # 边CA高亮 -> 中点E
        ca_edge = Line(self.C, self.A, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(ca_edge), FadeOut(bc_edge), run_time=0.4)
        
        dot_E = Dot(self.E, color=self.COLOR_MEDIAL, radius=0.08)
        label_E = Text("E", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(
            dot_E, LEFT, buff=0.1
        )
        
        self.play(
            FadeIn(dot_E, scale=0.5),
            Write(label_E),
            run_time=0.5
        )
        self.play(ca_edge.animate.set_color(self.COLOR_PRIMARY), run_time=0.2)
        
        # 边AB高亮 -> 中点F
        ab_edge = Line(self.A, self.B, color=self.COLOR_HIGHLIGHT, stroke_width=6)
        self.play(Create(ab_edge), FadeOut(ca_edge), run_time=0.4)
        
        dot_F = Dot(self.F, color=self.COLOR_MEDIAL, radius=0.08)
        label_F = Text("F", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(
            dot_F, UP, buff=0.1
        )
        
        self.play(
            FadeIn(dot_F, scale=0.5),
            Write(label_F),
            run_time=0.5
        )
        self.play(ab_edge.animate.set_color(self.COLOR_PRIMARY), run_time=0.2)
        self.play(FadeOut(ab_edge), run_time=0.2)
        
        # 连接中点形成中点三角形
        self.play(Create(self.medial_triangle_DEF), run_time=1.2)
        
        # 定义说明
        definition = Text(
            "连接三边中点形成的三角形",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(definition), run_time=0.5)
        self.wait(1.4)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(definition),
            run_time=0.5
        )
        
        # 保留元素
        self.midpoint_dots = VGroup(dot_D, dot_E, dot_F)
        self.midpoint_labels = VGroup(label_D, label_E, label_F)
    
    # ========================================================================
    # Scene 3: 斯皮克点定义 (12-20秒)
    # ========================================================================
    def scene_3_spieker_definition(self):
        """场景3: 斯皮克点 - 中点三角形的内心"""
        print("\n【Scene 3: 斯皮克点定义】")
        
        # 标题
        title = Text(
            "斯皮克点",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_SPIEKER
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "Spieker Point",
            font_size=24,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 定义
        definition = Text(
            "中点三角形 △DEF 的内心",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(definition), run_time=0.5)
        
        # 原三角形变灰
        self.play(
            self.triangle_ABC.animate.set_opacity(0.2),
            run_time=0.4
        )
        
        # 中点三角形高亮
        self.play(
            self.medial_triangle_DEF.animate.set_stroke(width=4).set_color(self.COLOR_MEDIAL),
            run_time=0.4
        )
        
        # 角D的角平分线
        # 计算角平分线方向
        vec_DE = (self.E - self.D) / np.linalg.norm(self.E - self.D)
        vec_DF = (self.F - self.D) / np.linalg.norm(self.F - self.D)
        bisector_D_dir = vec_DE + vec_DF
        bisector_D_dir_normalized = bisector_D_dir / np.linalg.norm(bisector_D_dir)
        
        # 找到角平分线与对边的交点
        # 使用角平分线定理
        t = self.d_de / (self.d_de + self.d_fd)
        intersection_D = self.E + t * (self.F - self.E)
        
        bisector_1 = DashedLine(
            self.D,
            intersection_D,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        explain_1 = Text(
            "作角平分线...",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(Create(bisector_1), FadeIn(explain_1), run_time=1.0)
        
        # 角E的角平分线
        vec_EF = (self.F - self.E) / np.linalg.norm(self.F - self.E)
        vec_ED = (self.D - self.E) / np.linalg.norm(self.D - self.E)
        bisector_E_dir = vec_EF + vec_ED
        bisector_E_dir_normalized = bisector_E_dir / np.linalg.norm(bisector_E_dir)
        
        t = self.d_ef / (self.d_ef + self.d_de)
        intersection_E = self.F + t * (self.D - self.F)
        
        bisector_2 = DashedLine(
            self.E,
            intersection_E,
            color=self.COLOR_AUXILIARY,
            dash_length=0.1
        )
        
        self.play(Create(bisector_2), FadeOut(explain_1), run_time=0.8)
        
        # 斯皮克点出现
        sp_dot = Dot(self.Sp, color=self.COLOR_SPIEKER, radius=0.12)
        sp_label = Text(
            "Sp",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_SPIEKER
        ).next_to(sp_dot, RIGHT, buff=0.15)
        
        sp_label_2 = Text(
            "斯皮克点",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_SPIEKER
        ).next_to(sp_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(FadeIn(sp_dot, scale=0.5), run_time=0.5)
        self.play(Flash(sp_dot, color=self.COLOR_SPIEKER, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(sp_label), FadeIn(sp_label_2), run_time=0.4)
        
        # 核心概念
        core_concept = Text(
            "三条角平分线交于一点",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(core_concept), run_time=0.6)
        self.wait(1.4)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(definition),
            FadeOut(bisector_1),
            FadeOut(bisector_2),
            FadeOut(core_concept),
            FadeOut(sp_label_2),
            self.triangle_ABC.animate.set_opacity(1.0),
            run_time=0.6
        )
        
        # 保留元素
        self.sp_dot = sp_dot
        self.sp_label = sp_label
    
    # ========================================================================
    # Scene 4: 斯皮克圆 (20-28秒)
    # ========================================================================
    def scene_4_spieker_circle(self):
        """场景4: 斯皮克圆 - 中点三角形的内切圆"""
        print("\n【Scene 4: 斯皮克圆】")
        
        # 标题
        title = Text(
            "斯皮克圆",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_INCIRCLE
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "Spieker Circle",
            font_size=24,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.5)
        
        # 从Sp到三边的垂线
        foot_EF = GeometryCalculator.perpendicular_foot(self.Sp, self.E, self.F)
        foot_FD = GeometryCalculator.perpendicular_foot(self.Sp, self.F, self.D)
        foot_DE = GeometryCalculator.perpendicular_foot(self.Sp, self.D, self.E)
        
        perp_EF = DashedLine(self.Sp, foot_EF, color=self.COLOR_AUXILIARY, dash_length=0.08)
        perp_FD = DashedLine(self.Sp, foot_FD, color=self.COLOR_AUXILIARY, dash_length=0.08)
        perp_DE = DashedLine(self.Sp, foot_DE, color=self.COLOR_AUXILIARY, dash_length=0.08)
        
        # 直角标记
        right_angle_1 = self.create_right_angle_mark(foot_EF, self.Sp, self.E, size=0.12)
        right_angle_2 = self.create_right_angle_mark(foot_FD, self.Sp, self.F, size=0.12)
        right_angle_3 = self.create_right_angle_mark(foot_DE, self.Sp, self.D, size=0.12)
        
        self.play(
            Create(perp_EF),
            FadeIn(right_angle_1),
            run_time=0.8
        )
        
        self.play(
            Create(perp_FD),
            FadeIn(right_angle_2),
            run_time=0.8
        )
        
        self.play(
            Create(perp_DE),
            FadeIn(right_angle_3),
            run_time=0.8
        )
        
        # 说明文字
        equal_dist_text = Text(
            "到三边距离相等",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(equal_dist_text), run_time=0.5)
        
        # 绘制斯皮克圆
        spieker_circle = Circle(
            radius=self.spieker_radius,
            color=self.COLOR_INCIRCLE,
            stroke_width=2.5
        ).move_to(self.Sp)
        
        self.play(Create(spieker_circle), run_time=1.5)
        
        # 圆标签
        circle_label = Text(
            "斯皮克圆",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_INCIRCLE
        ).next_to(spieker_circle, RIGHT, buff=0.2)
        
        self.play(Write(circle_label), run_time=0.5)
        
        # 性质说明
        property_text = Text(
            "中点三角形的内切圆",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(property_text), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(perp_EF),
            FadeOut(perp_FD),
            FadeOut(perp_DE),
            FadeOut(right_angle_1),
            FadeOut(right_angle_2),
            FadeOut(right_angle_3),
            FadeOut(equal_dist_text),
            FadeOut(circle_label),
            FadeOut(property_text),
            spieker_circle.animate.set_opacity(0.3),
            run_time=0.6
        )
        
        # 保留元素
        self.spieker_circle = spieker_circle
    
    def create_right_angle_mark(self, corner, point1, point2, size=0.15):
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
    
    # ========================================================================
    # Scene 5: 周长重心 (28-38秒)
    # ========================================================================
    def scene_5_perimeter_centroid(self):
        """场景5: 斯皮克点的物理意义 - 周长重心"""
        print("\n【Scene 5: 周长重心】")
        
        # 淡出中点三角形和斯皮克圆
        self.play(
            FadeOut(self.medial_triangle_DEF),
            FadeOut(self.spieker_circle),
            FadeOut(self.midpoint_dots),
            FadeOut(self.midpoint_labels),
            run_time=0.5
        )
        
        # 标题
        title = Text(
            "周长重心",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.COLOR_SPIEKER
        ).move_to(UP * 5.5)
        
        subtitle = Text(
            "Perimeter Centroid",
            font_size=24,
            color=GRAY_A
        ).next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), FadeIn(subtitle), run_time=0.8)
        
        # 说明
        definition = Text(
            "如果三角形是均匀铁丝框...",
            font="Noto Sans CJK SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(definition), run_time=0.5)
        
        # 三角形边加粗模拟框架
        self.play(
            self.triangle_ABC.animate.set_stroke(width=8),
            run_time=0.6
        )
        
        # 填充变透明
        self.play(
            self.triangle_ABC.animate.set_fill(opacity=0),
            run_time=0.4
        )
        
        # 框架说明
        frame_text = Text(
            "只有边, 没有面",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(frame_text), run_time=0.5)
        
        # 斯皮克点闪烁
        self.play(Flash(self.sp_dot, color=self.COLOR_SPIEKER, flash_radius=0.4), run_time=0.5)
        
        # 平衡点动画 - 三角形微晃
        original_pos = self.triangle_ABC.get_center()
        
        self.play(
            Indicate(self.sp_dot, scale_factor=1.3),
            self.triangle_ABC.animate.rotate(0.05, about_point=self.Sp),
            run_time=0.6
        )
        self.play(
            self.triangle_ABC.animate.rotate(-0.1, about_point=self.Sp),
            run_time=0.6
        )
        self.play(
            self.triangle_ABC.animate.rotate(0.05, about_point=self.Sp),
            run_time=0.6
        )
        
        # 对比: 重心G
        g_dot = Dot(self.G, color=self.COLOR_CENTROID, radius=0.10)
        g_label = Text(
            "G",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_CENTROID
        ).next_to(g_dot, DOWN, buff=0.1)
        
        g_label_2 = Text(
            "重心",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_CENTROID
        ).next_to(g_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(
            FadeIn(g_dot, scale=0.5),
            Write(g_label),
            FadeIn(g_label_2),
            run_time=0.6
        )
        
        # 对比说明
        comparison_text = VGroup(
            Text("面积重心", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_CENTROID),
            Text(" vs ", font_size=20, color=GRAY_A),
            Text("周长重心", font="Noto Sans CJK SC", font_size=20, color=self.COLOR_SPIEKER)
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.5)
        
        self.play(FadeIn(comparison_text), run_time=0.6)
        
        # 核心结论
        core_text = Text(
            "斯皮克点 = 周长的质心!",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(core_text, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)
        
        # 恢复填充
        self.play(
            self.triangle_ABC.animate.set_fill(opacity=0.1).set_stroke(width=3),
            run_time=0.4
        )
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(definition),
            FadeOut(frame_text),
            FadeOut(comparison_text),
            FadeOut(core_text),
            FadeOut(g_label_2),
            run_time=0.6
        )
        
        # 保留元素
        self.g_dot = g_dot
        self.g_label = g_label
    
    # ========================================================================
    # Scene 6: 与重心、奈格尔点关系 (38-48秒)
    # ========================================================================
    def scene_6_centroid_nagel_relation(self):
        """场景6: Sp = (G + Na) / 2 的关系"""
        print("\n【Scene 6: 重心与奈格尔点关系】")
        
        # 标题
        title = Text(
            "三点共线关系",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 重心G强调
        self.play(
            self.g_dot.animate.scale(2.5).set_opacity(1),
            run_time=0.5
        )
        
        # 奈格尔点Na出现
        na_dot = Dot(self.Na, color=self.COLOR_NAGEL, radius=0.10)
        na_label = Text(
            "Na",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_NAGEL
        ).next_to(na_dot, UP, buff=0.1)
        
        na_label_2 = Text(
            "奈格尔点",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.COLOR_NAGEL
        ).next_to(na_label, DOWN, buff=0.05, aligned_edge=LEFT)
        
        self.play(
            FadeIn(na_dot, scale=0.5),
            Write(na_label),
            FadeIn(na_label_2),
            run_time=0.8
        )
        
        # 简短说明Na
        na_brief = Text(
            "(与旁切圆相关的点)",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B
        ).move_to(DOWN * 4.5)
        
        self.play(FadeIn(na_brief), run_time=0.5)
        self.play(FadeOut(na_brief), run_time=0.3)
        
        # 连线G-Na
        line_G_Na = Line(self.G, self.Na, color=GRAY_B, stroke_width=2)
        
        self.play(Create(line_G_Na), run_time=0.8)
        
        # Sp强调
        self.play(Indicate(self.sp_dot, scale_factor=1.4), run_time=0.6)
        
        # 中点标记
        midpoint_mark = VGroup(
            Line(
                self.Sp + UP * 0.15 + LEFT * 0.1,
                self.Sp + UP * 0.15 + RIGHT * 0.1,
                color=YELLOW,
                stroke_width=3
            ),
            Line(
                self.Sp + DOWN * 0.15 + LEFT * 0.1,
                self.Sp + DOWN * 0.15 + RIGHT * 0.1,
                color=YELLOW,
                stroke_width=3
            )
        )
        
        self.play(Create(midpoint_mark), run_time=0.5)
        
        # 公式展示
        formula = MathTex(
            r"Sp = \frac{G + Na}{2}",
            font_size=40,
            color=WHITE
        ).move_to(DOWN * 5)
        
        self.play(Write(formula), run_time=1.2)
        
        # 验证动画 - 距离检查
        dist_G_Sp = np.linalg.norm(self.Sp - self.G)
        dist_Sp_Na = np.linalg.norm(self.Na - self.Sp)
        
        brace_1 = Brace(Line(self.G, self.Sp), direction=LEFT, buff=0.1, color=YELLOW)
        brace_2 = Brace(Line(self.Sp, self.Na), direction=RIGHT, buff=0.1, color=YELLOW)
        
        self.play(
            FadeIn(brace_1),
            FadeIn(brace_2),
            run_time=1.5
        )
        
        # 结论
        conclusion = Text(
            "斯皮克点是重心与奈格尔点的中点!",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 6.5)
        
        self.play(FadeIn(conclusion), run_time=0.6)
        self.wait(1.8)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line_G_Na),
            FadeOut(formula),
            FadeOut(conclusion),
            FadeOut(midpoint_mark),
            FadeOut(brace_1),
            FadeOut(brace_2),
            FadeOut(na_dot),
            FadeOut(na_label),
            FadeOut(na_label_2),
            self.g_dot.animate.scale(0.4).set_opacity(0.5),
            run_time=0.6
        )
    
    # ========================================================================
    # Scene 7: 重心坐标表示 (48-56秒)
    # ========================================================================
    def scene_7_barycentric_coordinates(self):
        """场景7: 斯皮克点的数学表达"""
        print("\n【Scene 7: 重心坐标表示】")
        
        # 标题
        title = Text(
            "数学表达",
            font="Noto Sans CJK SC",
            font_size=36,
            color=GOLD
        ).move_to(UP * 5.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 边长标注
        label_a = MathTex("a", font_size=24, color=YELLOW).move_to(
            (self.B + self.C) / 2 + DOWN * 0.3
        )
        label_b = MathTex("b", font_size=24, color=YELLOW).move_to(
            (self.C + self.A) / 2 + LEFT * 0.3
        )
        label_c = MathTex("c", font_size=24, color=YELLOW).move_to(
            (self.A + self.B) / 2 + UP * 0.3
        )
        
        side_labels = VGroup(label_a, label_b, label_c)
        
        self.play(FadeIn(side_labels), run_time=0.8)
        
        # 重心坐标公式
        formula_bary = MathTex(
            r"Sp = (b+c : c+a : a+b)",
            font_size=32,
            color=WHITE
        ).move_to(UP * 3.5)
        
        self.play(Write(formula_bary), run_time=1.2)
        
        # 解释
        explain_1 = Text(
            "重心坐标表示",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).next_to(formula_bary, DOWN, buff=0.3)
        
        self.play(FadeIn(explain_1), run_time=0.5)
        
        # 三线坐标
        formula_trilinear = MathTex(
            r"Sp = (bc : ca : ab)",
            font_size=32,
            color=WHITE
        ).move_to(UP * 1.5)
        
        self.play(Write(formula_trilinear), run_time=1.0)
        
        explain_2 = Text(
            "三线坐标表示",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).next_to(formula_trilinear, DOWN, buff=0.3)
        
        self.play(FadeIn(explain_2), run_time=0.5)
        
        # 对比内心
        incenter_formula = MathTex(
            r"I = (a : b : c)",
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 1)
        
        incenter_label = Text(
            "内心 (对比)",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B
        ).next_to(incenter_formula, DOWN, buff=0.2)
        
        self.play(
            FadeIn(incenter_formula),
            FadeIn(incenter_label),
            run_time=0.8
        )
        
        # 总结说明
        comparison = Text(
            "边长的对称组合",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(comparison), run_time=0.6)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(formula_bary),
            FadeOut(formula_trilinear),
            FadeOut(side_labels),
            FadeOut(explain_1),
            FadeOut(explain_2),
            FadeOut(incenter_formula),
            FadeOut(incenter_label),
            FadeOut(comparison),
            run_time=0.6
        )
    
    # ========================================================================
    # Scene 8: 总结与片尾 (56-75秒)
    # ========================================================================
    def scene_8_summary(self):
        """场景8: 总结核心概念"""
        print("\n【Scene 8: 总结与片尾】")
        
        # 淡出所有几何
        self.play(
            FadeOut(self.triangle_ABC),
            FadeOut(self.sp_dot),
            FadeOut(self.sp_label),
            FadeOut(self.g_dot),
            FadeOut(self.g_label),
            run_time=0.6
        )
        
        # 总结标题
        summary_title = Text(
            "斯皮克点 - 核心要点",
            font="Noto Sans CJK SC",
            font_size=40,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 6)
        
        self.play(Write(summary_title), run_time=0.8)
        
        # 核心要点卡片
        cards = VGroup()
        
        # 要点1
        card_1 = self.create_summary_card(
            "✓ 定义: 中点三角形的内心",
            self.COLOR_MEDIAL,
            UP * 3.5
        )
        cards.add(card_1)
        
        # 要点2
        card_2 = self.create_summary_card(
            "✓ 几何: 斯皮克圆圆心",
            self.COLOR_INCIRCLE,
            UP * 2
        )
        cards.add(card_2)
        
        # 要点3
        card_3 = self.create_summary_card(
            "✓ 物理: 周长的质心",
            self.COLOR_SPIEKER,
            UP * 0.5
        )
        cards.add(card_3)
        
        # 要点4
        card_4 = self.create_summary_card(
            "✓ 关系: Sp = (G+Na)/2",
            self.COLOR_CENTROID,
            DOWN * 1
        )
        cards.add(card_4)
        
        # 卡片依次滑入
        for i, card in enumerate(cards):
            self.play(card.animate.shift(RIGHT * 0), run_time=0.6)
            if i < len(cards) - 1:
                self.wait(0.2)
        
        # 应用场景
        applications = Text(
            "在三角形周长相关问题中有重要作用",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A
        ).move_to(DOWN * 3)
        
        self.play(FadeIn(applications), run_time=0.8)
        self.wait(2.5)
        
        # 淡出要点
        self.play(
            FadeOut(summary_title),
            FadeOut(cards),
            FadeOut(applications),
            run_time=0.6
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 1.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        
        # ID显示
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 探索更多几何奥秘!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.8)
        
        # 装饰 - 小圆点
        icons = VGroup(*[
            Dot(
                follow_text.get_center() + 2.5 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]),
                color=[self.COLOR_MEDIAL, self.COLOR_INCIRCLE, self.COLOR_SPIEKER,
                       self.COLOR_CENTROID, self.COLOR_NAGEL, GOLD][i],
                radius=0.12,
                fill_opacity=0.8
            )
            for i in range(6)
        ])
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in icons],
            run_time=1.5
        )
        
        self.play(Rotate(icons, angle=PI, run_time=1.5))
        
        # 小图标快闪
        self.play(
            *[Flash(icon, flash_radius=0.2) for icon in icons],
            run_time=1.0
        )
        
        self.wait(2.0)
        
        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(icons),
            run_time=1.0
        )
        
        print("\n【动画制作完成!】")
    
    def create_summary_card(self, text, color, position):
        """创建总结卡片"""
        # 图标圆
        icon = Circle(radius=0.15, fill_color=color, fill_opacity=1, stroke_width=0)
        
        # 文本
        content = Text(
            text,
            font="Noto Sans CJK SC",
            font_size=24,
            color=WHITE
        )
        
        # 组合
        card = VGroup(icon, content).arrange(RIGHT, buff=0.3)
        card.move_to(position)
        
        # 初始位置在左侧外
        card.shift(LEFT * 10)
        
        return card


# ============================================================================
# 渲染命令说明
# ============================================================================
"""
渲染命令:

# 快速预览 (480p 15fps)
manim -pql spieker_point_animation.py SpiekerPointScene

# 中等质量 (720p 30fps)
manim -pqm spieker_point_animation.py SpiekerPointScene

# 高质量 (1080p 60fps) - 推荐用于发布
manim -pqh spieker_point_animation.py SpiekerPointScene

# 4K质量 (2160p 60fps) - 最高质量
manim -pqk spieker_point_animation.py SpiekerPointScene

# GIF输出
manim -pql --format gif spieker_point_animation.py SpiekerPointScene

参数说明:
-p: 渲染后自动播放
-q: 质量 (l=low, m=medium, h=high, k=4k)
--format: 输出格式 (默认mp4)
"""