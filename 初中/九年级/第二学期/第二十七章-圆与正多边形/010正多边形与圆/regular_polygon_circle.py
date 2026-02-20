"""
正多边形与圆 - 九年级数学教学动画
Regular Polygons and Circles - Grade 9 Math

知识点: 外接圆、中心、半径、边心距、中心角
格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np


# ========================
# 全局配置 - TikTok竖屏
# ========================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class RegularPolygonAndCircle(Scene):
    """
    正多边形与圆 - 教学动画
    场景:
    1. 开场钩子
    2. 认识四大要素（中心、半径、边心距、中心角）
    3. 中心角探索（不同正多边形对比）
    4. 正六边形特殊性质（边长=半径）
    5. 面积公式推导
    6. 总结 + 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # === 颜色方案 ===
        self.C_POLYGON  = "#4fc3f7"   # 浅蓝 - 正多边形
        self.C_CIRCLE   = "#ffb300"   # 金黄 - 外接圆
        self.C_CENTER   = "#ff4757"   # 红色 - 中心O
        self.C_RADIUS   = "#2ed573"   # 绿色 - 外接圆半径R
        self.C_APOTHEM  = "#fd79a8"   # 玫红 - 边心距r
        self.C_ANGLE    = "#a29bfe"   # 紫色 - 中心角
        self.C_SIDE     = "#ffeaa7"   # 淡黄 - 边长a
        self.C_TITLE    = GOLD
        self.C_TEXT     = "#dfe6e9"
        self.C_AUTHOR   = GRAY_B
        self.C_FORMULA  = WHITE
        self.C_HIGHLIGHT = YELLOW

        # === 初始化几何数据 ===
        self.setup_geometry()

        # === 执行各场景 ===
        self.scene_1_opening()
        self.scene_2_core_elements()
        self.scene_3_central_angle()
        self.scene_4_hexagon_special()
        self.scene_5_area_formula()
        self.scene_6_summary()

    # ============================================================
    # 几何数据初始化
    # ============================================================
    def setup_geometry(self):
        """统一初始化所有几何坐标，精确计算，不猜测"""

        # === 基准参数 ===
        self.R = 2.0           # 外接圆半径
        self.N = 6             # 默认正六边形
        self.CENTER = np.array([0.0, 1.2, 0.0])  # 图形中心（竖屏内容区偏上）

        # === 计算正六边形顶点 ===
        # 从正上方（90°）开始，逆时针
        self.hex_verts = self._calc_polygon_verts(self.N, self.R, self.CENTER, start_angle=np.pi/2)

        # === 计算正三角形顶点 ===
        self.tri_verts = self._calc_polygon_verts(3, self.R, self.CENTER, start_angle=np.pi/2)

        # === 计算正四边形顶点 ===
        self.sq_verts = self._calc_polygon_verts(4, self.R, self.CENTER, start_angle=np.pi/4)

        # === 派生几何量 ===
        # 正六边形
        self.hex_apothem = self.R * np.cos(np.pi / self.N)  # 边心距 = R*cos(π/n)
        self.hex_central_angle_deg = 360.0 / self.N         # 中心角 = 60°
        self.hex_side_len = np.linalg.norm(self.hex_verts[1] - self.hex_verts[0])  # 边长

        # 正六边形边的中点（第0条边：V0-V1）
        self.hex_edge0_mid = (self.hex_verts[0] + self.hex_verts[1]) / 2

        # 边心距终点（从中心到边中点）
        self.apothem_end = self.hex_edge0_mid

        # === 验证 ===
        self._verify()

    def _calc_polygon_verts(self, n, R, center, start_angle=np.pi/2):
        """计算正n边形的顶点坐标（精确）"""
        verts = []
        for k in range(n):
            angle = start_angle + 2 * np.pi * k / n
            x = center[0] + R * np.cos(angle)
            y = center[1] + R * np.sin(angle)
            verts.append(np.array([x, y, 0.0]))
        return verts

    def _verify(self):
        """验证几何计算正确性"""
        eps = 1e-8

        # 验证外接圆半径
        for v in self.hex_verts:
            d = np.linalg.norm(v - self.CENTER)
            assert abs(d - self.R) < eps, f"顶点距圆心 {d} ≠ R={self.R}"

        # 验证正六边形边长=半径
        side = np.linalg.norm(self.hex_verts[1] - self.hex_verts[0])
        assert abs(side - self.R) < eps, f"正六边形边长 {side} ≠ R={self.R}"

        # 验证边心距
        actual_apothem = np.linalg.norm(self.hex_edge0_mid - self.CENTER)
        assert abs(actual_apothem - self.hex_apothem) < eps, \
            f"边心距 {actual_apothem} ≠ {self.hex_apothem}"

        print("✓ 几何验证全部通过")

    # ============================================================
    # Scene 1: 开场钩子
    # ============================================================
    def scene_1_opening(self):
        # --- 作者信息（顶部）---
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color=self.C_AUTHOR
        ).move_to(UP * 7)

        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        # --- 标题 ---
        title = Text(
            "正多边形与圆",
            font="Noto Sans CJK SC",
            font_size=44,
            color=self.C_TITLE,
            weight=BOLD
        ).move_to(UP * 5.8)

        subtitle = Text(
            "它们之间藏着哪些秘密？",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.C_TEXT
        ).move_to(UP * 5.1)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)

        # --- 正六边形 + 外接圆 ---
        hex_poly = Polygon(
            *self.hex_verts,
            color=self.C_POLYGON,
            stroke_width=3.5
        )
        circ = Circle(radius=self.R, color=self.C_CIRCLE, stroke_width=2.5).move_to(self.CENTER)

        self.play(Create(hex_poly), run_time=1.2)
        self.play(Create(circ), run_time=1.0)

        # --- 钩子：为什么它们完美契合？---
        hook = Text(
            "为什么正六边形与圆如此完美？",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.C_HIGHLIGHT
        ).move_to(DOWN * 4.8)

        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.6)
        self.wait(1.0)

        # 保存引用
        self.hex_poly_main = hex_poly
        self.circ_main = circ

        # 清理钩子和标题（保留图形和作者信息）
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hook),
            run_time=0.5
        )

    # ============================================================
    # Scene 2: 认识四大要素
    # ============================================================
    def scene_2_core_elements(self):
        # --- 场景标题 ---
        sc_title = Text(
            "正多边形的重要元素",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.C_TITLE
        ).move_to(UP * 5.8)

        self.play(Write(sc_title), run_time=0.6)

        # ==== 1. 中心 O ====
        center_dot = Dot(self.CENTER, radius=0.12, color=self.C_CENTER, fill_opacity=1)
        center_label = Text("中心 O", font="Noto Sans CJK SC", font_size=22,
                           color=self.C_CENTER).next_to(center_dot, RIGHT, buff=0.15)

        self.play(FadeIn(center_dot, scale=0.3), run_time=0.5)
        self.play(Flash(center_dot, color=self.C_CENTER, flash_radius=0.3), run_time=0.4)
        self.play(FadeIn(center_label), run_time=0.4)
        self.wait(0.3)

        # ==== 2. 外接圆半径 R ====
        # 从中心到顶点V1（正上方）
        v_top = self.hex_verts[0]  # 顶点0（约在右上方）
        radius_line = Line(
            self.CENTER, v_top,
            color=self.C_RADIUS, stroke_width=3
        )

        # R 标签（线段中点旁边）
        r_mid = (np.array(self.CENTER) + np.array(v_top)) / 2
        r_label = MathTex("R", color=self.C_RADIUS, font_size=32).next_to(
            r_mid, LEFT, buff=0.15
        )
        r_desc = Text("外接圆半径", font="Noto Sans CJK SC", font_size=20,
                     color=self.C_RADIUS).move_to(DOWN * 3.8)

        self.play(Create(radius_line), run_time=0.8)
        self.play(FadeIn(r_label), FadeIn(r_desc), run_time=0.4)
        self.wait(0.4)

        # ==== 3. 边心距 r ====
        # 从中心到第0条边（V0-V5）的中点
        # 第0条边在右侧 V0-V5（根据我们的顶点排列）
        # 实际上让我们选更容易看到的边：V2-V3（左下）或者 V0-V1
        # 取 V4-V5 边（下方）的中点比较直观
        # 重新选择：选择最右侧的边 V0（右上）到 V5（右下）
        # 实际：V0=(1.73,2.2), V1=(0,3.2), V2=(-1.73,2.2), V3=(-1.73,0.2), V4=(0,-0.8), V5=(1.73,0.2)
        # 取 V0-V1 边（右上斜边）的中点 → 朝右上方，视觉上不够清晰
        # 用 V1-V2 边（上方横边）中点更好

        # 选用V1-V2（接近水平的上边）
        v1 = self.hex_verts[1]
        v2 = self.hex_verts[2]
        edge12_mid = (v1 + v2) / 2  # 上边中点

        apothem_line = DashedLine(
            self.CENTER, edge12_mid,
            color=self.C_APOTHEM, stroke_width=2.5, dash_length=0.12
        )

        # r 标签在线段中点附近
        apo_mid = (np.array(self.CENTER) + np.array(edge12_mid)) / 2
        apo_label = MathTex("r", color=self.C_APOTHEM, font_size=32).next_to(
            apo_mid, RIGHT, buff=0.12
        )
        apo_desc = Text("边心距", font="Noto Sans CJK SC", font_size=20,
                       color=self.C_APOTHEM).move_to(DOWN * 4.3)

        self.play(FadeOut(r_desc), run_time=0.2)
        self.play(Create(apothem_line), run_time=0.7)
        self.play(FadeIn(apo_label), FadeIn(apo_desc), run_time=0.4)
        self.wait(0.4)

        # ==== 4. 中心角 ====
        # 中心角：从中心到两相邻顶点连线形成的角
        # 用 V0 和 V1 两条半径展示中心角
        radius0 = Line(self.CENTER, self.hex_verts[0], color=self.C_ANGLE, stroke_width=2.5)
        radius1 = Line(self.CENTER, self.hex_verts[1], color=self.C_ANGLE, stroke_width=2.5)

        # 计算角度方向（确保弧画在正确位置）
        v0_rel = np.array(self.hex_verts[0]) - np.array(self.CENTER)
        v1_rel = np.array(self.hex_verts[1]) - np.array(self.CENTER)
        cross_z = v0_rel[0] * v1_rel[1] - v0_rel[1] * v1_rel[0]
        # cross_z > 0 → v0到v1是逆时针 → 使用默认 other_angle=False

        central_angle_arc = Angle(
            radius0, radius1,
            radius=0.5,
            color=self.C_ANGLE,
            stroke_width=2.5,
            other_angle=(cross_z < 0)
        )

        # 中心角标签
        angle_label = MathTex(r"60^\circ", color=self.C_ANGLE, font_size=26)
        # 放在两条半径角平分线方向上
        bisect_dir = (v0_rel / np.linalg.norm(v0_rel) + v1_rel / np.linalg.norm(v1_rel))
        bisect_dir = bisect_dir / np.linalg.norm(bisect_dir)
        angle_label.move_to(self.CENTER + bisect_dir * 0.9)

        angle_desc = Text("中心角", font="Noto Sans CJK SC", font_size=20,
                         color=self.C_ANGLE).move_to(DOWN * 4.8)

        self.play(FadeOut(apo_desc), run_time=0.2)
        self.play(Create(radius0), Create(radius1), run_time=0.6)
        self.play(Create(central_angle_arc), FadeIn(angle_label), run_time=0.6)
        self.play(FadeIn(angle_desc), run_time=0.3)

        # ==== 中心角公式 ====
        formula_label = Text("中心角 =", font="Noto Sans CJK SC",
                            font_size=28, color=self.C_FORMULA)
        formula_math = MathTex(r"\frac{360^\circ}{n}", font_size=36, color=self.C_HIGHLIGHT)
        formula_group = VGroup(formula_label, formula_math).arrange(RIGHT, buff=0.2)
        formula_group.move_to(DOWN * 4.0)

        self.play(FadeOut(angle_desc), run_time=0.2)
        self.play(Write(formula_group), run_time=0.8)

        # n=6 时的具体值
        formula_n6 = Text("正六边形: n=6  →", font="Noto Sans CJK SC",
                         font_size=22, color=self.C_TEXT)
        formula_val = MathTex(r"\frac{360^\circ}{6} = 60^\circ", font_size=28,
                             color=self.C_HIGHLIGHT)
        formula_n6_group = VGroup(formula_n6, formula_val).arrange(RIGHT, buff=0.15)
        formula_n6_group.move_to(DOWN * 5.0)

        self.play(FadeIn(formula_n6_group, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 清理 Scene 2
        self.play(
            FadeOut(sc_title),
            FadeOut(center_label),
            FadeOut(r_label),
            FadeOut(r_desc) if r_desc in self.mobjects else FadeOut(formula_group),
            FadeOut(formula_group),
            FadeOut(formula_n6_group),
            FadeOut(apo_label),
            FadeOut(central_angle_arc),
            FadeOut(angle_label),
            FadeOut(radius0),
            FadeOut(radius1),
            run_time=0.5
        )

        # 保存部分元素给下一场景
        self.center_dot_main = center_dot
        self.radius_line_main = radius_line
        self.apothem_line_main = apothem_line

    # ============================================================
    # Scene 3: 中心角探索 — 不同正多边形
    # ============================================================
    def scene_3_central_angle(self):
        sc_title = Text(
            "中心角随边数变化",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.C_TITLE
        ).move_to(UP * 5.8)

        self.play(Write(sc_title), run_time=0.6)

        # 先清理主图
        self.play(
            FadeOut(self.hex_poly_main),
            FadeOut(self.circ_main),
            FadeOut(self.center_dot_main),
            FadeOut(self.radius_line_main),
            FadeOut(self.apothem_line_main),
            run_time=0.5
        )

        # 公式框（保持显示）
        formula_box_label = Text("中心角 =", font="Noto Sans CJK SC",
                                font_size=28, color=self.C_TEXT)
        formula_box_math = MathTex(r"\frac{360^\circ}{n}", font_size=36, color=self.C_FORMULA)
        formula_box = VGroup(formula_box_label, formula_box_math).arrange(RIGHT, buff=0.2)
        formula_box.move_to(DOWN * 5.0)
        self.play(FadeIn(formula_box), run_time=0.4)

        # === 正三角形 ===
        tri_poly = Polygon(*self.tri_verts, color=self.C_POLYGON, stroke_width=3.5)
        tri_circ = Circle(radius=self.R, color=self.C_CIRCLE, stroke_width=2).move_to(self.CENTER)
        tri_center = Dot(self.CENTER, radius=0.1, color=self.C_CENTER)

        # 两条半径
        r0 = Line(self.CENTER, self.tri_verts[0], color=self.C_RADIUS, stroke_width=2.5)
        r1 = Line(self.CENTER, self.tri_verts[1], color=self.C_RADIUS, stroke_width=2.5)

        # 中心角弧（120°，大于90°，需检查方向）
        v0_rel = np.array(self.tri_verts[0]) - np.array(self.CENTER)
        v1_rel = np.array(self.tri_verts[1]) - np.array(self.CENTER)
        cross_z = v0_rel[0] * v1_rel[1] - v0_rel[1] * v1_rel[0]
        # 正三角形中心角120°，需确认方向
        tri_angle_arc = Angle(
            r0, r1,
            radius=0.55,
            color=self.C_ANGLE,
            stroke_width=2.5,
            other_angle=(cross_z < 0)
        )

        n3_info = Text("正三角形 (n=3)", font="Noto Sans CJK SC",
                      font_size=26, color=self.C_POLYGON).move_to(DOWN * 3.8)
        n3_angle = MathTex(r"120^\circ", font_size=36, color=self.C_HIGHLIGHT).move_to(DOWN * 4.4)

        self.play(
            Create(tri_poly), Create(tri_circ),
            FadeIn(tri_center), run_time=1.0
        )
        self.play(Create(r0), Create(r1), Create(tri_angle_arc), run_time=0.7)
        self.play(FadeIn(n3_info), Write(n3_angle), run_time=0.5)
        self.wait(0.8)

        # === 变换为正四边形 ===
        sq_poly = Polygon(*self.sq_verts, color=self.C_POLYGON, stroke_width=3.5)
        sq_circ = Circle(radius=self.R, color=self.C_CIRCLE, stroke_width=2).move_to(self.CENTER)

        r0_sq = Line(self.CENTER, self.sq_verts[0], color=self.C_RADIUS, stroke_width=2.5)
        r1_sq = Line(self.CENTER, self.sq_verts[1], color=self.C_RADIUS, stroke_width=2.5)

        v0_sq = np.array(self.sq_verts[0]) - np.array(self.CENTER)
        v1_sq = np.array(self.sq_verts[1]) - np.array(self.CENTER)
        cross_sq = v0_sq[0] * v1_sq[1] - v0_sq[1] * v1_sq[0]

        sq_angle_arc = Angle(
            r0_sq, r1_sq,
            radius=0.55,
            color=self.C_ANGLE,
            stroke_width=2.5,
            other_angle=(cross_sq < 0)
        )

        n4_info = Text("正四边形 (n=4)", font="Noto Sans CJK SC",
                      font_size=26, color=self.C_POLYGON).move_to(DOWN * 3.8)
        n4_angle = MathTex(r"90^\circ", font_size=36, color=self.C_HIGHLIGHT).move_to(DOWN * 4.4)

        self.play(
            Transform(tri_poly, sq_poly),
            Transform(tri_circ, sq_circ),
            Transform(r0, r0_sq),
            Transform(r1, r1_sq),
            Transform(tri_angle_arc, sq_angle_arc),
            run_time=1.2
        )
        self.play(
            Transform(n3_info, n4_info),
            Transform(n3_angle, n4_angle),
            run_time=0.5
        )
        self.wait(0.8)

        # === 变换为正六边形 ===
        hex_poly_new = Polygon(*self.hex_verts, color=self.C_POLYGON, stroke_width=3.5)
        hex_circ_new = Circle(radius=self.R, color=self.C_CIRCLE, stroke_width=2).move_to(self.CENTER)

        r0_hex = Line(self.CENTER, self.hex_verts[0], color=self.C_RADIUS, stroke_width=2.5)
        r1_hex = Line(self.CENTER, self.hex_verts[1], color=self.C_RADIUS, stroke_width=2.5)

        v0_hex = np.array(self.hex_verts[0]) - np.array(self.CENTER)
        v1_hex = np.array(self.hex_verts[1]) - np.array(self.CENTER)
        cross_hex = v0_hex[0] * v1_hex[1] - v0_hex[1] * v1_hex[0]

        hex_angle_arc = Angle(
            r0_hex, r1_hex,
            radius=0.55,
            color=self.C_ANGLE,
            stroke_width=2.5,
            other_angle=(cross_hex < 0)
        )

        n6_info = Text("正六边形 (n=6)", font="Noto Sans CJK SC",
                      font_size=26, color=self.C_POLYGON).move_to(DOWN * 3.8)
        n6_angle = MathTex(r"60^\circ", font_size=36, color=self.C_HIGHLIGHT).move_to(DOWN * 4.4)

        self.play(
            Transform(tri_poly, hex_poly_new),
            Transform(tri_circ, hex_circ_new),
            Transform(r0, r0_hex),
            Transform(r1, r1_hex),
            Transform(tri_angle_arc, hex_angle_arc),
            run_time=1.2
        )
        self.play(
            Transform(n3_info, n6_info),
            Transform(n3_angle, n6_angle),
            run_time=0.5
        )
        self.wait(0.6)

        # 小结
        summary_text = Text(
            "边数越多，中心角越小",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.C_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(summary_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(sc_title),
            FadeOut(tri_poly), FadeOut(tri_circ), FadeOut(tri_center),
            FadeOut(r0), FadeOut(r1), FadeOut(tri_angle_arc),
            FadeOut(n3_info), FadeOut(n3_angle),
            FadeOut(summary_text), FadeOut(formula_box),
            run_time=0.6
        )

        # 重建主图
        self.hex_poly_main = Polygon(*self.hex_verts, color=self.C_POLYGON, stroke_width=3.5)
        self.circ_main = Circle(radius=self.R, color=self.C_CIRCLE, stroke_width=2.5).move_to(self.CENTER)
        self.center_dot_main = Dot(self.CENTER, radius=0.1, color=self.C_CENTER)

        self.play(
            FadeIn(self.hex_poly_main),
            FadeIn(self.circ_main),
            FadeIn(self.center_dot_main),
            run_time=0.5
        )

    # ============================================================
    # Scene 4: 正六边形特殊性质（边长=半径）
    # ============================================================
    def scene_4_hexagon_special(self):
        sc_title = Text(
            "正六边形的特殊性质",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.C_TITLE
        ).move_to(UP * 5.8)

        self.play(Write(sc_title), run_time=0.6)

        # 高亮一条边（V0-V1）
        v0, v1 = self.hex_verts[0], self.hex_verts[1]
        edge_hl = Line(v0, v1, color=self.C_SIDE, stroke_width=6)
        side_label = MathTex("a", color=self.C_SIDE, font_size=34)
        side_mid = (np.array(v0) + np.array(v1)) / 2
        # 标签放在边的外侧
        edge_dir = np.array(v1) - np.array(v0)
        perp = np.array([-edge_dir[1], edge_dir[0], 0])
        perp_unit = perp / np.linalg.norm(perp)
        # 判断外侧（远离中心方向）
        to_mid = side_mid - np.array(self.CENTER)
        if np.dot(to_mid[:2], perp_unit[:2]) < 0:
            perp_unit = -perp_unit
        side_label.move_to(side_mid + perp_unit * 0.35)

        self.play(Create(edge_hl), run_time=0.7)
        self.play(FadeIn(side_label), run_time=0.4)

        # 高亮对应半径（V0到中心）
        radius_hl = Line(self.CENTER, v0, color=self.C_RADIUS, stroke_width=6)
        radius_label = MathTex("R", color=self.C_RADIUS, font_size=34)
        r_mid = (np.array(self.CENTER) + np.array(v0)) / 2
        radius_label.next_to(r_mid, LEFT, buff=0.15)

        self.play(Create(radius_hl), run_time=0.7)
        self.play(FadeIn(radius_label), run_time=0.4)

        # 两者同时闪烁表示相等
        self.play(
            Indicate(edge_hl, color=self.C_HIGHLIGHT, scale_factor=1.15),
            Indicate(radius_hl, color=self.C_HIGHLIGHT, scale_factor=1.15),
            run_time=0.8
        )
        self.wait(0.3)

        # 显示等式
        eq_text = Text("边长  =  外接圆半径", font="Noto Sans CJK SC",
                      font_size=28, color=self.C_TEXT).move_to(DOWN * 3.8)
        eq_math = MathTex("a = R", font_size=40, color=self.C_HIGHLIGHT).move_to(DOWN * 4.5)

        self.play(FadeIn(eq_text), run_time=0.5)
        self.play(Write(eq_math), run_time=0.7)
        self.wait(0.5)

        # 解释：因为中心角=60°，所以OV0V1是等边三角形
        reason_title = Text("原因：中心角 = 60°", font="Noto Sans CJK SC",
                           font_size=22, color=self.C_ANGLE).move_to(DOWN * 5.2)

        # 连接 V0-V1 的三角形
        triangle_ov = Polygon(
            self.CENTER, v0, v1,
            color=self.C_ANGLE,
            stroke_width=2,
            fill_opacity=0.15,
            fill_color=self.C_ANGLE
        )
        self.play(
            Create(triangle_ov),
            FadeIn(reason_title),
            run_time=0.8
        )

        reason_detail = Text(
            "△OAB是等边三角形！所以 OA=OB=AB",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.C_TEXT
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(reason_detail), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(sc_title),
            FadeOut(edge_hl), FadeOut(side_label),
            FadeOut(radius_hl), FadeOut(radius_label),
            FadeOut(eq_text), FadeOut(eq_math),
            FadeOut(triangle_ov),
            FadeOut(reason_title), FadeOut(reason_detail),
            run_time=0.6
        )

    # ============================================================
    # Scene 5: 面积公式推导
    # ============================================================
    def scene_5_area_formula(self):
        sc_title = Text(
            "正多边形面积公式",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.C_TITLE
        ).move_to(UP * 5.8)

        self.play(Write(sc_title), run_time=0.6)

        # === Step 1: 连接中心到各顶点，分割成6个三角形 ===
        dividing_lines = VGroup(*[
            Line(self.CENTER, self.hex_verts[k],
                 color=GRAY_B, stroke_width=1.5, stroke_opacity=0.7)
            for k in range(6)
        ])

        split_hint = Text("从中心连接各顶点，分成 6 个三角形",
                         font="Noto Sans CJK SC", font_size=22,
                         color=self.C_TEXT).move_to(DOWN * 3.8)

        self.play(Create(dividing_lines), run_time=1.0)
        self.play(FadeIn(split_hint), run_time=0.4)
        self.wait(0.5)

        # === Step 2: 高亮其中一个三角形 ===
        v0, v1 = self.hex_verts[0], self.hex_verts[1]
        triangle_hi = Polygon(
            self.CENTER, v0, v1,
            color=self.C_POLYGON,
            stroke_width=3,
            fill_opacity=0.35,
            fill_color=self.C_POLYGON
        )

        self.play(FadeOut(split_hint), run_time=0.2)
        self.play(Create(triangle_hi), run_time=0.6)

        # === Step 3: 标注底边 a 和高 r ===
        # 底边 a（V0-V1）
        edge_a = Line(v0, v1, color=self.C_SIDE, stroke_width=5)
        edge_dir = np.array(v1) - np.array(v0)
        perp = np.array([-edge_dir[1], edge_dir[0], 0])
        perp_unit = perp / np.linalg.norm(perp)
        to_mid = (np.array(v0) + np.array(v1)) / 2 - np.array(self.CENTER)
        if np.dot(to_mid[:2], perp_unit[:2]) < 0:
            perp_unit = -perp_unit
        a_mid = (np.array(v0) + np.array(v1)) / 2
        a_label = MathTex("a", color=self.C_SIDE, font_size=32).move_to(
            a_mid + perp_unit * 0.35
        )

        # 边心距 r（中心到边中点的垂线）
        # 边中点
        edge_mid = (np.array(v0) + np.array(v1)) / 2
        apo_line = DashedLine(
            self.CENTER, edge_mid,
            color=self.C_APOTHEM, stroke_width=3, dash_length=0.1
        )
        apo_mid = (np.array(self.CENTER) + edge_mid) / 2
        r_label = MathTex("r", color=self.C_APOTHEM, font_size=32).next_to(
            apo_mid, RIGHT, buff=0.12
        )

        self.play(
            Create(edge_a), FadeIn(a_label),
            Create(apo_line), FadeIn(r_label),
            run_time=0.8
        )

        # 标注垂直符号（r ⊥ 底边）
        # 计算垂足处的小方块
        right_mark = self._make_right_angle_mark(edge_mid, self.CENTER, v0, size=0.18)
        self.play(FadeIn(right_mark), run_time=0.3)
        self.wait(0.4)

        # === Step 4: 单个三角形面积 ===
        step1_label = Text("单个三角形面积 =", font="Noto Sans CJK SC",
                          font_size=24, color=self.C_TEXT)
        step1_math = MathTex(r"\frac{1}{2} \times a \times r",
                            font_size=30, color=self.C_FORMULA)
        step1 = VGroup(step1_label, step1_math).arrange(RIGHT, buff=0.15)
        step1.move_to(DOWN * 3.8)

        self.play(Write(step1), run_time=0.8)
        self.wait(0.5)

        # === Step 5: 共 n=6 个三角形 ===
        step2_label = Text("共 n=6 个三角形，总面积：", font="Noto Sans CJK SC",
                          font_size=22, color=self.C_TEXT).move_to(DOWN * 4.5)
        self.play(FadeIn(step2_label), run_time=0.5)

        # 其他三角形淡入填充
        other_triangles = VGroup(*[
            Polygon(
                self.CENTER, self.hex_verts[k], self.hex_verts[(k+1) % 6],
                color=self.C_POLYGON,
                stroke_width=1.5,
                fill_opacity=0.2,
                fill_color=self.C_POLYGON
            )
            for k in range(1, 6)
        ])
        self.play(FadeIn(other_triangles), run_time=0.7)
        self.wait(0.3)

        # === Step 6: 面积公式 ===
        formula_S = MathTex(
            r"S = n \times \frac{1}{2} \times a \times r",
            font_size=32, color=self.C_FORMULA
        ).move_to(DOWN * 5.1)

        self.play(Write(formula_S), run_time=0.8)
        self.wait(0.5)

        # === Step 7: 化简 → (1/2)×周长×r ===
        formula_S2 = MathTex(
            r"S = \frac{1}{2} \times (na) \times r",
            font_size=32, color=self.C_FORMULA
        ).move_to(DOWN * 5.1)

        formula_C = Text("（其中 na = 周长 C）", font="Noto Sans CJK SC",
                        font_size=20, color=self.C_TEXT).move_to(DOWN * 5.7)

        self.play(
            Transform(formula_S, formula_S2),
            FadeIn(formula_C),
            run_time=0.8
        )
        self.wait(0.4)

        # 最终公式框
        formula_final = MathTex(
            r"S = \frac{1}{2} \times C \times r",
            font_size=38, color=self.C_HIGHLIGHT
        ).move_to(DOWN * 5.1)

        formula_box_rect = SurroundingRectangle(
            formula_final, color=self.C_HIGHLIGHT, buff=0.15,
            stroke_width=2.5, corner_radius=0.1
        )

        self.play(
            Transform(formula_S, formula_final),
            FadeOut(formula_C),
            run_time=0.7
        )
        self.play(Create(formula_box_rect), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(sc_title),
            FadeOut(dividing_lines),
            FadeOut(triangle_hi), FadeOut(other_triangles),
            FadeOut(edge_a), FadeOut(a_label),
            FadeOut(apo_line), FadeOut(r_label),
            FadeOut(right_mark),
            FadeOut(step1), FadeOut(step2_label),
            FadeOut(formula_S), FadeOut(formula_box_rect),
            run_time=0.6
        )

    def _make_right_angle_mark(self, corner, p1, p2, size=0.18):
        """在 corner 处创建直角标记"""
        v1 = np.array(p1) - np.array(corner)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = np.array(p2) - np.array(corner)
        v2 = v2 / np.linalg.norm(v2) * size
        return Polygon(
            corner,
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=YELLOW,
            stroke_width=1.5,
            fill_opacity=0
        )

    # ============================================================
    # Scene 6: 总结 + 片尾
    # ============================================================
    def scene_6_summary(self):
        # 主图缩小移到上方
        self.play(
            self.hex_poly_main.animate.scale(0.55).move_to(UP * 4.5),
            self.circ_main.animate.scale(0.55).move_to(UP * 4.5),
            self.center_dot_main.animate.scale(0.55).move_to(UP * 4.5),
            run_time=0.8
        )

        sc_title = Text(
            "知识点总结",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.C_TITLE
        ).move_to(UP * 3.2)
        self.play(Write(sc_title), run_time=0.5)

        # === 知识卡片 ===
        def make_card(icon_color, title_str, formula_str, pos):
            dot_icon = Dot(ORIGIN, radius=0.14, color=icon_color, fill_opacity=1)
            title_t = Text(title_str, font="Noto Sans CJK SC", font_size=22, color=WHITE)
            math_t = MathTex(formula_str, font_size=26, color=icon_color)
            row = VGroup(dot_icon, title_t, math_t).arrange(RIGHT, buff=0.2)
            row.move_to(pos)
            return row

        card1 = make_card(
            self.C_ANGLE,
            "中心角",
            r"\frac{360^\circ}{n}",
            UP * 1.8
        )
        card2 = make_card(
            self.C_SIDE,
            "正六边形边长",
            r"a = R",
            UP * 0.8
        )
        card3_dot = Dot(ORIGIN, radius=0.14, color=self.C_APOTHEM, fill_opacity=1)
        card3_title = Text("面积公式", font="Noto Sans CJK SC", font_size=22, color=WHITE)
        card3_math = MathTex(r"S = \frac{1}{2} \times n \times a \times r",
                            font_size=24, color=self.C_APOTHEM)
        card3 = VGroup(card3_dot, card3_title, card3_math).arrange(RIGHT, buff=0.2)
        card3.move_to(DOWN * 0.2)

        card4_title = Text("等价：", font="Noto Sans CJK SC", font_size=22, color=GRAY_A)
        card4_math = MathTex(r"S = \frac{1}{2} \times C \times r",
                            font_size=24, color=GRAY_A)
        card4 = VGroup(card4_title, card4_math).arrange(RIGHT, buff=0.2)
        card4.move_to(DOWN * 1.0)

        for card in [card1, card2, card3, card4]:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.1)

        self.wait(1.0)

        # === 片尾 ===
        self.play(
            FadeOut(sc_title),
            FadeOut(card1), FadeOut(card2), FadeOut(card3), FadeOut(card4),
            self.hex_poly_main.animate.scale(1.8).move_to(UP * 1.5),
            self.circ_main.animate.scale(1.8).move_to(UP * 1.5),
            self.center_dot_main.animate.scale(1.8).move_to(UP * 1.5),
            run_time=0.8
        )

        # 旋转动画
        self.play(
            Rotate(self.hex_poly_main, angle=PI / 6, about_point=self.CENTER),
            run_time=1.0
        )

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 2.5)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.C_AUTHOR
        ).move_to(DOWN * 3.2)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_HIGHLIGHT
        ).move_to(DOWN * 4.2)

        self.play(
            FadeOut(self.author_bar),
            FadeIn(author_big, shift=UP * 0.3),
            run_time=0.6
        )
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(follow_text, scale=1.05), run_time=0.6)

        self.wait(2.0)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(self.hex_poly_main),
            FadeOut(self.circ_main),
            FadeOut(self.center_dot_main),
            run_time=1.0
        )


# ========================
# 渲染命令
# ========================
# 快速预览 (480p):
#   manim -pql regular_polygon_circle.py RegularPolygonAndCircle
#
# 高质量 (1080p):
#   manim -qh regular_polygon_circle.py RegularPolygonAndCircle
#
# 4K 生产版:
#   manim -qk regular_polygon_circle.py RegularPolygonAndCircle