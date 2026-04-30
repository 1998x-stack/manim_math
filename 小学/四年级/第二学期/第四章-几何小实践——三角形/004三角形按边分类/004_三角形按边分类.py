"""
004_三角形按边分类.py — 三角形按边分类 教学动画

知识点: 按边分类
  - 不等边三角形: 三条边都不相等
  - 等腰三角形: 两条边相等，相等的两边叫腰，另一边叫底
  - 等边三角形/正三角形: 三条边都相等，每个角都是60°
  - 等边三角形是特殊的等腰三角形

年级: 四年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR         = "#1a1a2e"
COLOR_SCALENE    = "#f97316"   # 橙色 — 不等边三角形
COLOR_ISOSCELES  = "#3b82f6"   # 蓝色 — 等腰三角形
COLOR_EQUILATERAL= "#22c55e"   # 绿色 — 等边三角形
COLOR_WAIST      = "#facc15"   # 黄色 — 腰
COLOR_BASE       = "#f472b6"   # 粉色 — 底
COLOR_AUTHOR     = "#6b7280"   # 灰色
COLOR_HL         = "#fbbf24"   # 高亮黄
FONT             = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class TriangleSideClassifyLesson(Scene):
    """
    三角形按边分类 教学动画
    场景顺序:
      1. 开场钩子
      2. 不等边三角形
      3. 等腰三角形 — 腰和底
      4. 等边三角形 — 60°角
      5. 等边三角形是特殊等腰三角形
      6. 总结分类图
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_scalene()
        self.scene_3_isosceles()
        self.scene_4_equilateral()
        self.scene_5_relationship()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有三角形顶点坐标（精确计算）"""

        # ===== 不等边三角形 (三边都不相等) =====
        # 设计成三边明显不同长：约 2.4, 3.2, 1.8
        self.SC_A = np.array([-1.6,  -0.9, 0.0])
        self.SC_B = np.array([ 1.6,  -0.9, 0.0])
        self.SC_C = np.array([-0.2,   1.5, 0.0])

        sc_ab = np.linalg.norm(self.SC_B - self.SC_A)
        sc_bc = np.linalg.norm(self.SC_C - self.SC_B)
        sc_ca = np.linalg.norm(self.SC_A - self.SC_C)
        assert abs(sc_ab - sc_bc) > 0.05, "不等边三角形AB≈BC"
        assert abs(sc_bc - sc_ca) > 0.05, "不等边三角形BC≈CA"
        assert abs(sc_ca - sc_ab) > 0.05, "不等边三角形CA≈AB"

        self.SC_AB = sc_ab
        self.SC_BC = sc_bc
        self.SC_CA = sc_ca

        # ===== 等腰三角形 (AB=AC，底边 BC) =====
        # 腰长 = 2.2，底长 = 2.6
        waist = 2.2
        base  = 2.6
        # A 在正上方，BC 水平
        half_base = base / 2
        height_iso = np.sqrt(waist**2 - half_base**2)

        self.ISO_B = np.array([-half_base, -0.9, 0.0])
        self.ISO_C = np.array([ half_base, -0.9, 0.0])
        self.ISO_A = np.array([0.0, -0.9 + height_iso, 0.0])

        self.ISO_AB = np.linalg.norm(self.ISO_B - self.ISO_A)
        self.ISO_AC = np.linalg.norm(self.ISO_C - self.ISO_A)
        self.ISO_BC = np.linalg.norm(self.ISO_C - self.ISO_B)

        eps = 1e-6
        assert abs(self.ISO_AB - self.ISO_AC) < eps, "等腰三角形腰不等"
        assert abs(self.ISO_AB - waist)         < eps, "等腰三角形腰长错"
        assert abs(self.ISO_BC - base)          < eps, "等腰三角形底长错"

        # ===== 等边三角形 (三边相等，每角60°) =====
        side = 2.8
        half = side / 2
        height_eq = side * np.sqrt(3) / 2

        self.EQ_A = np.array([0.0,   -0.9 + height_eq * 2/3, 0.0])
        self.EQ_B = np.array([-half, -0.9 - height_eq / 3,   0.0])
        self.EQ_C = np.array([ half, -0.9 - height_eq / 3,   0.0])

        self.EQ_AB = np.linalg.norm(self.EQ_B - self.EQ_A)
        self.EQ_BC = np.linalg.norm(self.EQ_C - self.EQ_B)
        self.EQ_CA = np.linalg.norm(self.EQ_A - self.EQ_C)

        assert abs(self.EQ_AB - side) < eps, "等边三角形AB边长错"
        assert abs(self.EQ_BC - side) < eps, "等边三角形BC边长错"
        assert abs(self.EQ_CA - side) < eps, "等边三角形CA边长错"

        # 验证60°角
        angle_A = self._angle_at(self.EQ_B, self.EQ_A, self.EQ_C)
        angle_B = self._angle_at(self.EQ_A, self.EQ_B, self.EQ_C)
        angle_C = self._angle_at(self.EQ_A, self.EQ_C, self.EQ_B)
        assert abs(np.degrees(angle_A) - 60.0) < 0.01, "等边三角形A角错"
        assert abs(np.degrees(angle_B) - 60.0) < 0.01, "等边三角形B角错"
        assert abs(np.degrees(angle_C) - 60.0) < 0.01, "等边三角形C角错"

    def _angle_at(self, P1, vertex, P2):
        """计算顶点vertex处的角度（弧度）"""
        v1 = P1 - vertex
        v2 = P2 - vertex
        cos_val = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.arccos(np.clip(cos_val, -1.0, 1.0))

    def _tick_mark(self, P, Q, n=1, color=WHITE, size=0.18):
        """在线段PQ中点处画n条刻度线（表示等长）"""
        mid = (P + Q) / 2
        direction = Q - P
        length = np.linalg.norm(direction)
        unit = direction / length
        perp = np.array([-unit[1], unit[0], 0.0])
        marks = VGroup()
        offsets = [(i - (n - 1) / 2) * 0.13 for i in range(n)]
        for offset in offsets:
            pt = mid + offset * unit
            tick = Line(pt - perp * size/2, pt + perp * size/2, color=color, stroke_width=3)
            marks.add(tick)
        return marks

    # ------------------------------------------------------------------
    # 场景 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者信息（固定在顶部）
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.add(self.author_label)

        # 大标题
        title = Text("三角形", font=FONT, font_size=52, color=WHITE)
        title.move_to(UP * 5.2)

        subtitle = Text("按边分类", font=FONT, font_size=40, color=COLOR_HL)
        subtitle.next_to(title, DOWN, buff=0.3)

        # 三个小三角形并排展示（钩子）
        tri_s = Polygon(self.SC_A, self.SC_B, self.SC_C,
                        color=COLOR_SCALENE, stroke_width=3).scale(0.38).move_to(LEFT * 2.5 + DOWN * 0.5)
        tri_i = Polygon(self.ISO_A, self.ISO_B, self.ISO_C,
                        color=COLOR_ISOSCELES, stroke_width=3).scale(0.38).move_to(ORIGIN + DOWN * 0.5)
        tri_e = Polygon(self.EQ_A, self.EQ_B, self.EQ_C,
                        color=COLOR_EQUILATERAL, stroke_width=3).scale(0.38).move_to(RIGHT * 2.5 + DOWN * 0.5)

        q_text = Text("它们有什么不同？", font=FONT, font_size=28, color=COLOR_HL)
        q_text.move_to(DOWN * 2.5)

        self.play(FadeIn(self.author_label), run_time=0.3)
        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.play(
            LaggedStart(
                Create(tri_s), Create(tri_i), Create(tri_e),
                lag_ratio=0.3
            ),
            run_time=1.0
        )
        self.play(FadeIn(q_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(tri_s), FadeOut(tri_i), FadeOut(tri_e),
            FadeOut(q_text),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 2: 不等边三角形
    # ------------------------------------------------------------------

    def scene_2_scalene(self):
        # 标题
        title = Text("不等边三角形", font=FONT, font_size=38, color=COLOR_SCALENE)
        title.move_to(UP * 5.5)

        # 三角形（偏上方）
        tri = Polygon(self.SC_A, self.SC_B, self.SC_C,
                      color=COLOR_SCALENE, stroke_width=3)
        tri.move_to(UP * 1.5)

        self.play(Write(title), run_time=0.6)
        self.play(Create(tri), run_time=0.9)

        # 顶点标签
        verts = tri.get_vertices()
        A_pt, B_pt, C_pt = verts[0], verts[1], verts[2]

        lA = Text("A", font=FONT, font_size=22, color=WHITE).next_to(A_pt + np.array([-0.15, 0, 0]), UL, buff=0.08)
        lB = Text("B", font=FONT, font_size=22, color=WHITE).next_to(B_pt + np.array([ 0.15, 0, 0]), UR, buff=0.08)
        lC = Text("C", font=FONT, font_size=22, color=WHITE).next_to(C_pt, UP, buff=0.1)

        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.4)

        # 逐边高亮并标注长度
        def highlight_edge(P, Q, label_str, color_e, direction):
            edge = Line(P, Q, color=color_e, stroke_width=5)
            lbl = Text(label_str, font=FONT, font_size=20, color=color_e)
            lbl.next_to((P + Q) / 2, direction, buff=0.18)
            return edge, lbl

        # 计算屏幕坐标下的边长（tri已经move_to，需要用实际顶点）
        len_AB = round(np.linalg.norm(B_pt - A_pt), 1)
        len_BC = round(np.linalg.norm(C_pt - B_pt), 1)
        len_CA = round(np.linalg.norm(A_pt - C_pt), 1)

        edge_ab, lbl_ab = highlight_edge(A_pt, B_pt, f"AB", "#ef4444", DOWN)
        edge_bc, lbl_bc = highlight_edge(B_pt, C_pt, f"BC", "#a78bfa", RIGHT)
        edge_ca, lbl_ca = highlight_edge(C_pt, A_pt, f"CA", "#38bdf8", LEFT)

        self.play(Create(edge_ab), FadeIn(lbl_ab), run_time=0.5)
        self.play(Create(edge_bc), FadeIn(lbl_bc), run_time=0.5)
        self.play(Create(edge_ca), FadeIn(lbl_ca), run_time=0.5)

        self.wait(0.5)

        # 核心说明
        def_text = Text("三条边长度各不相同", font=FONT, font_size=26, color=WHITE)
        def_text.move_to(DOWN * 1.5)

        formula = VGroup(
            Text("a", font=FONT, font_size=26, color="#ef4444"),
            Text(" ≠ ", font=FONT, font_size=26, color=WHITE),
            Text("b", font=FONT, font_size=26, color="#a78bfa"),
            Text(" ≠ ", font=FONT, font_size=26, color=WHITE),
            Text("c", font=FONT, font_size=26, color="#38bdf8"),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 2.5)

        self.play(FadeIn(def_text, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(formula), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(tri),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(edge_ab), FadeOut(lbl_ab),
            FadeOut(edge_bc), FadeOut(lbl_bc),
            FadeOut(edge_ca), FadeOut(lbl_ca),
            FadeOut(def_text), FadeOut(formula),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 3: 等腰三角形 — 腰和底
    # ------------------------------------------------------------------

    def scene_3_isosceles(self):
        # 标题
        title = Text("等腰三角形", font=FONT, font_size=38, color=COLOR_ISOSCELES)
        title.move_to(UP * 5.5)

        # 三角形
        tri = Polygon(self.ISO_A, self.ISO_B, self.ISO_C,
                      color=COLOR_ISOSCELES, stroke_width=3)
        tri.move_to(UP * 1.6)

        self.play(Write(title), run_time=0.6)
        self.play(Create(tri), run_time=0.9)

        verts = tri.get_vertices()
        A_pt, B_pt, C_pt = verts[0], verts[1], verts[2]

        lA = Text("A", font=FONT, font_size=22, color=WHITE).next_to(A_pt, UP, buff=0.1)
        lB = Text("B", font=FONT, font_size=22, color=WHITE).next_to(B_pt, DL, buff=0.08)
        lC = Text("C", font=FONT, font_size=22, color=WHITE).next_to(C_pt, DR, buff=0.08)

        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.4)

        # 腰 AB 和 AC（等长）
        waist_ab = Line(A_pt, B_pt, color=COLOR_WAIST, stroke_width=5)
        waist_ac = Line(A_pt, C_pt, color=COLOR_WAIST, stroke_width=5)

        tick_ab = self._tick_mark(A_pt, B_pt, n=2, color=COLOR_WAIST)
        tick_ac = self._tick_mark(A_pt, C_pt, n=2, color=COLOR_WAIST)

        waist_label = Text("腰", font=FONT, font_size=24, color=COLOR_WAIST)
        waist_label.move_to(DOWN * 1.4)

        waist_eq = VGroup(
            Text("AB = AC", font=FONT, font_size=24, color=COLOR_WAIST)
        ).move_to(DOWN * 2.0)

        self.play(
            Create(waist_ab), Create(waist_ac),
            run_time=0.6
        )
        self.play(
            FadeIn(tick_ab), FadeIn(tick_ac),
            run_time=0.4
        )
        self.play(FadeIn(waist_label), run_time=0.4)
        self.play(FadeIn(waist_eq), run_time=0.5)
        self.wait(0.8)

        # 底边 BC
        base_line = Line(B_pt, C_pt, color=COLOR_BASE, stroke_width=5)
        base_label = Text("底", font=FONT, font_size=24, color=COLOR_BASE)
        base_label.next_to((B_pt + C_pt) / 2, DOWN, buff=0.25)

        self.play(Create(base_line), run_time=0.5)
        self.play(FadeIn(base_label), run_time=0.4)
        self.wait(0.5)

        # 说明文字
        explain = Text(
            "两腰相等，另一边叫底边",
            font=FONT, font_size=24, color=WHITE
        ).move_to(DOWN * 3.2)

        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(tri),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(waist_ab), FadeOut(waist_ac),
            FadeOut(tick_ab), FadeOut(tick_ac),
            FadeOut(waist_label), FadeOut(waist_eq),
            FadeOut(base_line), FadeOut(base_label),
            FadeOut(explain),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 4: 等边三角形 — 三边相等 + 60°
    # ------------------------------------------------------------------

    def scene_4_equilateral(self):
        # 标题
        title = Text("等边三角形", font=FONT, font_size=38, color=COLOR_EQUILATERAL)
        subtitle_also = Text("（正三角形）", font=FONT, font_size=26, color="#86efac")
        VGroup(title, subtitle_also).arrange(RIGHT, buff=0.2).move_to(UP * 5.5)

        # 三角形
        tri = Polygon(self.EQ_A, self.EQ_B, self.EQ_C,
                      color=COLOR_EQUILATERAL, stroke_width=3,
                      fill_color=COLOR_EQUILATERAL, fill_opacity=0.08)
        tri.move_to(UP * 1.5)

        self.play(Write(title), FadeIn(subtitle_also), run_time=0.6)
        self.play(Create(tri), run_time=0.9)

        verts = tri.get_vertices()
        A_pt, B_pt, C_pt = verts[0], verts[1], verts[2]

        lA = Text("A", font=FONT, font_size=22, color=WHITE).next_to(A_pt, UP, buff=0.1)
        lB = Text("B", font=FONT, font_size=22, color=WHITE).next_to(B_pt, DL, buff=0.08)
        lC = Text("C", font=FONT, font_size=22, color=WHITE).next_to(C_pt, DR, buff=0.08)

        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.4)

        # 三条边都加刻度线（各1条）
        tick_ab = self._tick_mark(A_pt, B_pt, n=1, color=COLOR_EQUILATERAL)
        tick_bc = self._tick_mark(B_pt, C_pt, n=1, color=COLOR_EQUILATERAL)
        tick_ca = self._tick_mark(C_pt, A_pt, n=1, color=COLOR_EQUILATERAL)

        self.play(
            FadeIn(tick_ab), FadeIn(tick_bc), FadeIn(tick_ca),
            run_time=0.5
        )

        eq_formula = Text("AB = BC = CA", font=FONT, font_size=26, color=COLOR_EQUILATERAL)
        eq_formula.move_to(DOWN * 1.5)

        self.play(FadeIn(eq_formula), run_time=0.5)
        self.wait(0.6)

        # 三个角都是60° — 用Angle.from_three_points
        def make_angle_arc(P1, vertex, P2, color_a, radius=0.42):
            """绘制顶角弧（from_three_points方式，确保方向正确）"""
            v1 = P1 - vertex
            v2 = P2 - vertex
            cross_z = v1[0] * v2[1] - v1[1] * v2[0]
            arc = Angle.from_three_points(
                P1, vertex, P2,
                radius=radius,
                color=color_a,
                other_angle=(cross_z < 0)
            )
            return arc

        arc_A = make_angle_arc(B_pt, A_pt, C_pt, COLOR_HL, radius=0.38)
        arc_B = make_angle_arc(A_pt, B_pt, C_pt, COLOR_HL, radius=0.38)
        arc_C = make_angle_arc(A_pt, C_pt, B_pt, COLOR_HL, radius=0.38)

        self.play(
            Create(arc_A), Create(arc_B), Create(arc_C),
            run_time=0.7
        )

        # 标注 60°
        deg_A = MathTex(r"60^\circ", color=COLOR_HL, font_size=22)
        deg_B = MathTex(r"60^\circ", color=COLOR_HL, font_size=22)
        deg_C = MathTex(r"60^\circ", color=COLOR_HL, font_size=22)

        deg_A.move_to(A_pt + np.array([0, -0.65, 0]))
        deg_B.move_to(B_pt + np.array([ 0.55, 0.3, 0]))
        deg_C.move_to(C_pt + np.array([-0.55, 0.3, 0]))

        self.play(FadeIn(deg_A), FadeIn(deg_B), FadeIn(deg_C), run_time=0.5)

        angle_explain = Text(
            "三个内角都是 60°",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 2.5)

        self.play(FadeIn(angle_explain), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(subtitle_also), FadeOut(tri),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(tick_ab), FadeOut(tick_bc), FadeOut(tick_ca),
            FadeOut(eq_formula),
            FadeOut(arc_A), FadeOut(arc_B), FadeOut(arc_C),
            FadeOut(deg_A), FadeOut(deg_B), FadeOut(deg_C),
            FadeOut(angle_explain),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 5: 等边三角形是特殊的等腰三角形
    # ------------------------------------------------------------------

    def scene_5_relationship(self):
        # 标题
        title = Text("等边三角形", font=FONT, font_size=34, color=COLOR_EQUILATERAL)
        title.move_to(UP * 5.8)

        is_special = VGroup(
            Text("是", font=FONT, font_size=28, color=WHITE),
            Text("特殊的", font=FONT, font_size=28, color=COLOR_HL),
            Text("等腰三角形", font=FONT, font_size=28, color=COLOR_ISOSCELES),
        ).arrange(RIGHT, buff=0.12).move_to(UP * 5.0)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(is_special), run_time=0.5)

        # 大圆：等腰三角形
        big_circle = Circle(radius=2.4, color=COLOR_ISOSCELES, stroke_width=3)
        big_circle.move_to(UP * 1.5 + RIGHT * 0.2)

        iso_label = Text("等腰三角形", font=FONT, font_size=22, color=COLOR_ISOSCELES)
        iso_label.move_to(big_circle.get_top() + DOWN * 0.35)

        # 小圆：等边三角形（套在大圆内偏右上）
        small_circle = Circle(radius=1.1, color=COLOR_EQUILATERAL, stroke_width=3,
                              fill_color=COLOR_EQUILATERAL, fill_opacity=0.15)
        small_circle.move_to(UP * 1.7 + RIGHT * 0.5)

        eq_label = Text("等边\n三角形", font=FONT, font_size=20, color=COLOR_EQUILATERAL)
        eq_label.move_to(small_circle.get_center())

        self.play(Create(big_circle), FadeIn(iso_label), run_time=0.8)
        self.play(Create(small_circle), FadeIn(eq_label), run_time=0.7)

        # ⊂ 符号说明
        subset_line = VGroup(
            Text("等边三角形", font=FONT, font_size=24, color=COLOR_EQUILATERAL),
            MathTex(r"\subset", color=WHITE, font_size=36),
            Text("等腰三角形", font=FONT, font_size=24, color=COLOR_ISOSCELES),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.5)

        self.play(FadeIn(subset_line), run_time=0.6)

        explain = Text(
            "等边三角形两腰相等，还多了：\n三边全相等、每角都60°",
            font=FONT, font_size=22, color=WHITE,
            line_spacing=1.3
        ).move_to(DOWN * 4.0)

        self.play(FadeIn(explain), run_time=0.6)
        self.wait(2.2)

        self.play(
            FadeOut(title), FadeOut(is_special),
            FadeOut(big_circle), FadeOut(iso_label),
            FadeOut(small_circle), FadeOut(eq_label),
            FadeOut(subset_line), FadeOut(explain),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 6: 总结分类图
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        # 顶部标题
        sum_title = Text("按边分类总结", font=FONT, font_size=36, color=COLOR_HL)
        sum_title.move_to(UP * 6.0)
        self.play(Write(sum_title), run_time=0.6)

        # 三列：不等边 / 等腰 / 等边
        col_y = UP * 3.8
        x_scalene    = -3.2
        x_isosceles  =  0.0
        x_equilateral=  3.2

        # ---- 不等边 ----
        sc_tri = Polygon(self.SC_A, self.SC_B, self.SC_C,
                         color=COLOR_SCALENE, stroke_width=2.5
                         ).scale(0.30).move_to(np.array([x_scalene, 3.0, 0]))

        sc_name = Text("不等边", font=FONT, font_size=22, color=COLOR_SCALENE)
        sc_name.next_to(sc_tri, DOWN, buff=0.18)

        sc_desc = Text("三边各不同", font=FONT, font_size=18, color=GRAY_A)
        sc_desc.next_to(sc_name, DOWN, buff=0.12)

        # ---- 等腰 ----
        iso_tri = Polygon(self.ISO_A, self.ISO_B, self.ISO_C,
                          color=COLOR_ISOSCELES, stroke_width=2.5
                          ).scale(0.30).move_to(np.array([x_isosceles, 3.0, 0]))
        # 腰刻度
        iso_verts = iso_tri.get_vertices()
        iso_tA, iso_tB, iso_tC = iso_verts[0], iso_verts[1], iso_verts[2]
        iso_tick_ab = self._tick_mark(iso_tA, iso_tB, n=2, color=COLOR_WAIST, size=0.10)
        iso_tick_ac = self._tick_mark(iso_tA, iso_tC, n=2, color=COLOR_WAIST, size=0.10)

        iso_name = Text("等腰", font=FONT, font_size=22, color=COLOR_ISOSCELES)
        iso_name.next_to(iso_tri, DOWN, buff=0.18)

        iso_desc = Text("两腰相等", font=FONT, font_size=18, color=GRAY_A)
        iso_desc.next_to(iso_name, DOWN, buff=0.12)

        # ---- 等边 ----
        eq_tri = Polygon(self.EQ_A, self.EQ_B, self.EQ_C,
                         color=COLOR_EQUILATERAL, stroke_width=2.5,
                         fill_color=COLOR_EQUILATERAL, fill_opacity=0.1
                         ).scale(0.30).move_to(np.array([x_equilateral, 3.0, 0]))
        eq_verts = eq_tri.get_vertices()
        eq_tA, eq_tB, eq_tC = eq_verts[0], eq_verts[1], eq_verts[2]
        eq_tick_ab = self._tick_mark(eq_tA, eq_tB, n=1, color=COLOR_EQUILATERAL, size=0.10)
        eq_tick_bc = self._tick_mark(eq_tB, eq_tC, n=1, color=COLOR_EQUILATERAL, size=0.10)
        eq_tick_ca = self._tick_mark(eq_tC, eq_tA, n=1, color=COLOR_EQUILATERAL, size=0.10)

        eq_name = Text("等边", font=FONT, font_size=22, color=COLOR_EQUILATERAL)
        eq_name.next_to(eq_tri, DOWN, buff=0.18)

        eq_desc = Text("三边全相等", font=FONT, font_size=18, color=GRAY_A)
        eq_desc.next_to(eq_name, DOWN, buff=0.12)

        # 动画出现
        self.play(
            LaggedStart(
                AnimationGroup(Create(sc_tri), FadeIn(sc_name), FadeIn(sc_desc)),
                AnimationGroup(
                    Create(iso_tri), FadeIn(iso_tick_ab), FadeIn(iso_tick_ac),
                    FadeIn(iso_name), FadeIn(iso_desc)
                ),
                AnimationGroup(
                    Create(eq_tri),
                    FadeIn(eq_tick_ab), FadeIn(eq_tick_bc), FadeIn(eq_tick_ca),
                    FadeIn(eq_name), FadeIn(eq_desc)
                ),
                lag_ratio=0.35
            ),
            run_time=1.4
        )

        self.wait(0.6)

        # 分割线
        divider = Line(LEFT * 4.0, RIGHT * 4.0, color=GRAY_B, stroke_width=1.5)
        divider.move_to(UP * 1.6)
        self.play(Create(divider), run_time=0.4)

        # 要点卡片
        key_items = [
            ("不等边三角形", "a ≠ b ≠ c", COLOR_SCALENE),
            ("等腰三角形",   "两腰相等，有腰和底", COLOR_ISOSCELES),
            ("等边三角形",   "a = b = c，角 = 60°", COLOR_EQUILATERAL),
        ]

        cards = VGroup()
        for i, (name, desc, color) in enumerate(key_items):
            dot = Dot(radius=0.1, color=color)
            name_t = Text(name, font=FONT, font_size=21, color=color)
            desc_t = Text(desc, font=FONT, font_size=18, color=GRAY_A)
            row = VGroup(dot, name_t, desc_t).arrange(RIGHT, buff=0.2)
            row.move_to(np.array([0, 0.8 - i * 1.0, 0]))
            cards.add(row)

        self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.3) for c in cards], lag_ratio=0.25), run_time=1.0)
        self.wait(0.5)

        # 等边是特殊等腰
        special_note = VGroup(
            Text("等边三角形", font=FONT, font_size=22, color=COLOR_EQUILATERAL),
            MathTex(r"\subset", color=WHITE, font_size=30),
            Text("等腰三角形", font=FONT, font_size=22, color=COLOR_ISOSCELES),
            Text("（特殊情况）", font=FONT, font_size=20, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.12).move_to(DOWN * 2.3)

        self.play(FadeIn(special_note, shift=UP * 0.2), run_time=0.6)

        # 口诀
        slogan = Text(
            "按边分三类，腰底要分清！",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 3.5)

        self.play(Write(slogan), run_time=0.8)
        self.wait(2.5)

        self.play(
            FadeOut(sum_title),
            FadeOut(sc_tri), FadeOut(sc_name), FadeOut(sc_desc),
            FadeOut(iso_tri), FadeOut(iso_tick_ab), FadeOut(iso_tick_ac),
            FadeOut(iso_name), FadeOut(iso_desc),
            FadeOut(eq_tri),
            FadeOut(eq_tick_ab), FadeOut(eq_tick_bc), FadeOut(eq_tick_ca),
            FadeOut(eq_name), FadeOut(eq_desc),
            FadeOut(divider),
            FadeOut(cards),
            FadeOut(special_note),
            FadeOut(slogan),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        channel = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE
        ).move_to(UP * 1.5)

        handle = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=COLOR_AUTHOR
        ).next_to(channel, DOWN, buff=0.3)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 0.8)

        # 小装饰三角形
        def small_tri(color, pos):
            pts_local = np.array([
                [0.0,  0.3, 0],
                [-0.26, -0.15, 0],
                [ 0.26, -0.15, 0],
            ])
            return Polygon(*pts_local, color=color,
                           fill_color=color, fill_opacity=0.85,
                           stroke_width=1.5).move_to(pos)

        deco = VGroup(
            small_tri(COLOR_SCALENE,     DOWN * 2.8 + LEFT  * 2.0),
            small_tri(COLOR_ISOSCELES,   DOWN * 2.8),
            small_tri(COLOR_EQUILATERAL, DOWN * 2.8 + RIGHT * 2.0),
        )

        # 片尾动画
        self.play(
            Transform(
                self.author_label,
                channel
            ),
            run_time=0.7
        )
        self.play(FadeIn(handle, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(follow_text, scale=1.05), run_time=0.6)
        self.play(
            LaggedStart(*[GrowFromCenter(t) for t in deco], lag_ratio=0.3),
            run_time=0.8
        )
        self.wait(2.0)

        self.play(
            FadeOut(self.author_label),
            FadeOut(handle),
            FadeOut(follow_text),
            FadeOut(deco),
            run_time=0.8
        )
