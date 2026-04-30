"""
三角形按角分类 - Triangle Classification by Angles
小学四年级数学教学动画

内容: 锐角三角形、直角三角形、钝角三角形的定义与识别
目标受众: 小学四年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ── 全局配置 TikTok 竖屏 ──────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ── 配色 ─────────────────────────────────────────────────────
C_BG         = "#1a1a2e"
C_ACUTE      = "#3498db"   # 锐角三角形 — 蓝
C_RIGHT      = "#2ecc71"   # 直角三角形 — 绿
C_OBTUSE     = "#e74c3c"   # 钝角三角形 — 红
C_ANGLE_ARC  = "#f1c40f"   # 角弧 — 黄
C_LABEL      = "#ecf0f1"
C_DIM        = "#7f8c8d"
C_HIGHLIGHT  = "#f39c12"


# ─────────────────────────────────────────────────────────────
class TriangleAngleClassifyLesson(Scene):
    """
    场景顺序:
      1. scene_1_opening        — 开场钩子
      2. scene_2_angle_review   — 角的类型复习
      3. scene_3_acute          — 锐角三角形
      4. scene_4_right          — 直角三角形
      5. scene_5_obtuse         — 钝角三角形
      6. scene_6_summary        — 三类汇总对比
      7. scene_7_warning        — 重要提醒（不能有两个直/钝角）
      8. scene_8_outro          — 片尾关注
    """

    # ── construct ────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = C_BG
        self._setup_geometry()

        self.scene_1_opening()
        self.scene_2_angle_review()
        self.scene_3_acute()
        self.scene_4_right()
        self.scene_5_obtuse()
        self.scene_6_summary()
        self.scene_7_warning()
        self.scene_8_outro()

    # ── geometry setup ────────────────────────────────────────
    def _setup_geometry(self):
        """预计算三类三角形的顶点（逻辑坐标）"""

        # ---- 锐角三角形 ----
        # 三角: A=(-1.4,-1)  B=(1.4,-1)  C=(0, 1.4)
        # 角A≈54°  角B≈54°  角C≈72°  — 全是锐角
        self.acute_A = np.array([-1.4, -1.0, 0])
        self.acute_B = np.array([ 1.4, -1.0, 0])
        self.acute_C = np.array([ 0.0,  1.4, 0])
        self._verify_all_acute(self.acute_A, self.acute_B, self.acute_C)

        # ---- 直角三角形 ----
        # 角B = 90°（B在原点，BA沿左，BC沿上）
        self.right_A = np.array([-2.2, -1.0, 0])
        self.right_B = np.array([-0.1, -1.0, 0])   # 直角顶点
        self.right_C = np.array([-0.1,  1.3, 0])
        self._verify_right_angle(self.right_A, self.right_B, self.right_C)

        # ---- 钝角三角形 ----
        # 角B钝角: A在左上，B在中，C在右下
        self.obtuse_A = np.array([-1.8,  0.8, 0])
        self.obtuse_B = np.array([ 0.0, -1.0, 0])   # 钝角顶点
        self.obtuse_C = np.array([ 2.0, -0.4, 0])
        self._verify_obtuse_at_B(self.obtuse_A, self.obtuse_B, self.obtuse_C)

    # ── helper: angle calc ───────────────────────────────────
    @staticmethod
    def _angle_at(P, vertex, Q):
        """顶点处∠PVQ 的弧度（0 ~ π）"""
        v1 = P - vertex
        v2 = Q - vertex
        cos_a = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-12)
        return np.arccos(np.clip(cos_a, -1.0, 1.0))

    def _verify_all_acute(self, A, B, C):
        angles = [
            self._angle_at(B, A, C),
            self._angle_at(A, B, C),
            self._angle_at(A, C, B),
        ]
        for a in angles:
            assert a < np.pi / 2 - 1e-6, f"锐角三角形验证失败: {np.degrees(a):.1f}°"
        print(f"✓ 锐角三角形: {[f'{np.degrees(a):.1f}°' for a in angles]}")

    def _verify_right_angle(self, A, B, C):
        angle_B = self._angle_at(A, B, C)
        assert abs(angle_B - np.pi / 2) < 1e-4, f"直角验证失败: {np.degrees(angle_B):.2f}°"
        print(f"✓ 直角三角形 ∠B = {np.degrees(angle_B):.1f}°")

    def _verify_obtuse_at_B(self, A, B, C):
        angle_B = self._angle_at(A, B, C)
        assert angle_B > np.pi / 2 + 1e-6, f"钝角验证失败: {np.degrees(angle_B):.1f}°"
        print(f"✓ 钝角三角形 ∠B = {np.degrees(angle_B):.1f}°")

    # ── helper: right-angle mark ─────────────────────────────
    def _right_angle_mark(self, corner, p1, p2, size=0.18, color=C_ANGLE_ARC):
        """在 corner 处绘制直角小方框"""
        u = (p1 - corner)
        u = u / np.linalg.norm(u) * size
        v = (p2 - corner)
        v = v / np.linalg.norm(v) * size
        square = Polygon(
            corner, corner + u, corner + u + v, corner + v,
            color=color, stroke_width=2.0, fill_opacity=0
        )
        return square

    # ── helper: angle arc ────────────────────────────────────
    def _make_angle_arc(self, p1, vertex, p2, radius=0.35, color=C_ANGLE_ARC):
        """
        在 vertex 处绘制从 p1 到 p2 方向的角弧。
        始终使用 Angle.from_three_points，自动选择正确的 other_angle。
        """
        v1 = p1 - vertex
        v2 = p2 - vertex
        # 叉积 z 分量：> 0 逆时针，< 0 顺时针
        cross_z = v1[0] * v2[1] - v1[1] * v2[0]
        arc = Angle.from_three_points(
            p1, vertex, p2,
            radius=radius,
            other_angle=(cross_z < 0),
            color=color,
        )
        return arc

    # ── helper: triangle + labels ────────────────────────────
    def _make_triangle(self, A, B, C, color=WHITE, stroke_width=3.0, fill_color=None, fill_opacity=0.0):
        poly = Polygon(A, B, C,
                       color=color,
                       stroke_width=stroke_width,
                       fill_color=fill_color or color,
                       fill_opacity=fill_opacity)
        return poly

    # ═════════════════════════════════════════════════════════
    # Scene 1 — 开场钩子
    # ═════════════════════════════════════════════════════════
    def scene_1_opening(self):
        # 品牌
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC", font_size=18, color=C_DIM
        ).move_to(UP * 7.0)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author = author  # 保留到结尾

        # 钩子问题
        hook_line1 = Text(
            "三角形有几种？",
            font="PingFang SC", font_size=52, color=C_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.2)
        hook_line2 = Text(
            "按角来分一分！",
            font="PingFang SC", font_size=38, color=C_LABEL
        ).move_to(UP * 4.2)

        self.play(Write(hook_line1), run_time=0.8)
        self.play(FadeIn(hook_line2, shift=UP * 0.3), run_time=0.5)
        self.wait(0.6)

        # 快速闪现三种三角形轮廓
        OFFSET = DOWN * 1.2
        s = 0.85

        tri_acute = self._make_triangle(
            self.acute_A * s + OFFSET,
            self.acute_B * s + OFFSET,
            self.acute_C * s + OFFSET,
            color=C_ACUTE
        )
        tri_right = self._make_triangle(
            self.right_A * s + OFFSET,
            self.right_B * s + OFFSET,
            self.right_C * s + OFFSET,
            color=C_RIGHT
        )
        tri_obtuse = self._make_triangle(
            self.obtuse_A * s + OFFSET,
            self.obtuse_B * s + OFFSET,
            self.obtuse_C * s + OFFSET,
            color=C_OBTUSE
        )

        preview = VGroup(tri_acute, tri_right, tri_obtuse)
        preview.arrange(RIGHT, buff=0.5).move_to(DOWN * 1.5)

        self.play(
            LaggedStart(
                Create(tri_acute), Create(tri_right), Create(tri_obtuse),
                lag_ratio=0.3
            ),
            run_time=1.2
        )

        # 三种名称
        lbl_a = Text("锐角", font="PingFang SC", font_size=26, color=C_ACUTE)
        lbl_r = Text("直角", font="PingFang SC", font_size=26, color=C_RIGHT)
        lbl_o = Text("钝角", font="PingFang SC", font_size=26, color=C_OBTUSE)

        lbl_a.next_to(tri_acute, DOWN, buff=0.15)
        lbl_r.next_to(tri_right, DOWN, buff=0.15)
        lbl_o.next_to(tri_obtuse, DOWN, buff=0.15)

        self.play(
            FadeIn(lbl_a), FadeIn(lbl_r), FadeIn(lbl_o),
            run_time=0.5
        )
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(hook_line1), FadeOut(hook_line2),
            FadeOut(preview), FadeOut(lbl_a), FadeOut(lbl_r), FadeOut(lbl_o),
            run_time=0.5
        )

    # ═════════════════════════════════════════════════════════
    # Scene 2 — 角的类型复习
    # ═════════════════════════════════════════════════════════
    def scene_2_angle_review(self):
        title = Text(
            "先来复习一下角",
            font="PingFang SC", font_size=40, color=C_HIGHLIGHT
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.7)

        # 三种角的示意 —— 用简单的射线对
        center_y = 2.0

        # ── 锐角 ──
        v_acute = np.array([-3.0, center_y, 0])
        p1_acute = v_acute + np.array([ 1.2, 0.0, 0])
        p2_acute = v_acute + np.array([ 0.6, 1.0, 0])
        ray1_a = Line(v_acute, p1_acute, color=C_ACUTE, stroke_width=3)
        ray2_a = Line(v_acute, p2_acute, color=C_ACUTE, stroke_width=3)
        arc_a = self._make_angle_arc(p1_acute, v_acute, p2_acute, radius=0.32, color=C_ACUTE)
        lbl_acute = Text("锐角", font="PingFang SC", font_size=26, color=C_ACUTE)
        lbl_acute.next_to(v_acute, DOWN, buff=0.8)
        sub_acute = Text("小于90°", font="PingFang SC", font_size=20, color=C_DIM)
        sub_acute.next_to(lbl_acute, DOWN, buff=0.1)

        # ── 直角 ──
        v_right = np.array([ 0.0, center_y, 0])
        p1_right = v_right + np.array([1.1, 0.0, 0])
        p2_right = v_right + np.array([0.0, 1.1, 0])
        ray1_r = Line(v_right, p1_right, color=C_RIGHT, stroke_width=3)
        ray2_r = Line(v_right, p2_right, color=C_RIGHT, stroke_width=3)
        mark_r = self._right_angle_mark(v_right, p1_right, p2_right, size=0.22, color=C_RIGHT)
        lbl_right = Text("直角", font="PingFang SC", font_size=26, color=C_RIGHT)
        lbl_right.next_to(v_right, DOWN, buff=0.8)
        sub_right = Text("等于90°", font="PingFang SC", font_size=20, color=C_DIM)
        sub_right.next_to(lbl_right, DOWN, buff=0.1)

        # ── 钝角 ──
        v_obtuse = np.array([ 3.0, center_y, 0])
        p1_obtuse = v_obtuse + np.array([ 1.2, 0.0, 0])
        p2_obtuse = v_obtuse + np.array([-0.8, 0.9, 0])
        ray1_o = Line(v_obtuse, p1_obtuse, color=C_OBTUSE, stroke_width=3)
        ray2_o = Line(v_obtuse, p2_obtuse, color=C_OBTUSE, stroke_width=3)
        arc_o = self._make_angle_arc(p1_obtuse, v_obtuse, p2_obtuse, radius=0.32, color=C_OBTUSE)
        lbl_obtuse = Text("钝角", font="PingFang SC", font_size=26, color=C_OBTUSE)
        lbl_obtuse.next_to(v_obtuse, DOWN, buff=0.8)
        sub_obtuse = Text("大于90°", font="PingFang SC", font_size=20, color=C_DIM)
        sub_obtuse.next_to(lbl_obtuse, DOWN, buff=0.1)

        # 动画
        self.play(
            Create(ray1_a), Create(ray2_a),
            Create(ray1_r), Create(ray2_r),
            Create(ray1_o), Create(ray2_o),
            run_time=0.8
        )
        self.play(
            Create(arc_a), Create(mark_r), Create(arc_o),
            run_time=0.6
        )
        self.play(
            FadeIn(lbl_acute), FadeIn(lbl_right), FadeIn(lbl_obtuse),
            FadeIn(sub_acute), FadeIn(sub_right), FadeIn(sub_obtuse),
            run_time=0.5
        )
        self.wait(1.2)

        review_group = VGroup(
            ray1_a, ray2_a, arc_a, lbl_acute, sub_acute,
            ray1_r, ray2_r, mark_r, lbl_right, sub_right,
            ray1_o, ray2_o, arc_o, lbl_obtuse, sub_obtuse,
        )

        # 分类提示
        classify_text = Text(
            "三角形的角也有这三种！",
            font="PingFang SC", font_size=34, color=C_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(classify_text, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(review_group), FadeOut(classify_text),
            run_time=0.5
        )

    # ═════════════════════════════════════════════════════════
    # Scene 3 — 锐角三角形
    # ═════════════════════════════════════════════════════════
    def scene_3_acute(self):
        # 标题
        sec_title = Text(
            "锐角三角形",
            font="PingFang SC", font_size=46, color=C_ACUTE, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(Write(sec_title), run_time=0.6)

        # 三角形
        SCALE = 1.25
        OFF = DOWN * 0.5
        A = self.acute_A * SCALE + OFF
        B = self.acute_B * SCALE + OFF
        C = self.acute_C * SCALE + OFF

        tri = self._make_triangle(A, B, C, color=C_ACUTE, fill_opacity=0.08, fill_color=C_ACUTE)
        self.play(Create(tri), run_time=1.0)

        # 顶点标签
        lA = Text("A", font="PingFang SC", font_size=24, color=C_LABEL).next_to(A, DL, buff=0.12)
        lB = Text("B", font="PingFang SC", font_size=24, color=C_LABEL).next_to(B, DR, buff=0.12)
        lC = Text("C", font="PingFang SC", font_size=24, color=C_LABEL).next_to(C, UP, buff=0.12)
        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.4)

        # 三个角弧 + 高亮逐一展示
        arc_A = self._make_angle_arc(B, A, C, radius=0.38, color=C_ANGLE_ARC)
        arc_B = self._make_angle_arc(A, B, C, radius=0.38, color=C_ANGLE_ARC)
        arc_C = self._make_angle_arc(A, C, B, radius=0.38, color=C_ANGLE_ARC)

        deg_A = int(round(np.degrees(self._angle_at(B, A, C))))
        deg_B = int(round(np.degrees(self._angle_at(A, B, C))))
        deg_C = int(round(np.degrees(self._angle_at(A, C, B))))

        def make_deg_label(vertex, direction, deg, color=C_ANGLE_ARC):
            t = Text(f"{deg}°", font="PingFang SC", font_size=22, color=color)
            t.next_to(vertex, direction, buff=0.5)
            return t

        deg_lbl_A = make_deg_label(A, LEFT,  deg_A)
        deg_lbl_B = make_deg_label(B, RIGHT*0.4 + DOWN, deg_B)
        deg_lbl_C = make_deg_label(C, RIGHT, deg_C)

        # 逐个展示
        for arc, lbl in [(arc_A, deg_lbl_A), (arc_B, deg_lbl_B), (arc_C, deg_lbl_C)]:
            self.play(Create(arc), FadeIn(lbl), run_time=0.5)
            self.wait(0.2)

        # 说明文字
        def_text = Text(
            "三个角都是锐角",
            font="PingFang SC", font_size=32, color=C_LABEL
        ).move_to(DOWN * 3.5)
        sub_text = Text(
            "（每个角都小于90°）",
            font="PingFang SC", font_size=24, color=C_DIM
        ).next_to(def_text, DOWN, buff=0.15)

        self.play(FadeIn(def_text), run_time=0.5)
        self.play(FadeIn(sub_text), run_time=0.4)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(sec_title), FadeOut(tri),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(arc_A), FadeOut(arc_B), FadeOut(arc_C),
            FadeOut(deg_lbl_A), FadeOut(deg_lbl_B), FadeOut(deg_lbl_C),
            FadeOut(def_text), FadeOut(sub_text),
            run_time=0.5
        )

    # ═════════════════════════════════════════════════════════
    # Scene 4 — 直角三角形
    # ═════════════════════════════════════════════════════════
    def scene_4_right(self):
        sec_title = Text(
            "直角三角形",
            font="PingFang SC", font_size=46, color=C_RIGHT, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(Write(sec_title), run_time=0.6)

        SCALE = 1.18
        OFF = DOWN * 0.6
        A = self.right_A * SCALE + OFF
        B = self.right_B * SCALE + OFF
        C = self.right_C * SCALE + OFF

        tri = self._make_triangle(A, B, C, color=C_RIGHT, fill_opacity=0.08, fill_color=C_RIGHT)
        self.play(Create(tri), run_time=1.0)

        lA = Text("A", font="PingFang SC", font_size=24, color=C_LABEL).next_to(A, LEFT, buff=0.12)
        lB = Text("B", font="PingFang SC", font_size=24, color=C_LABEL).next_to(B, DOWN+RIGHT*0.2, buff=0.12)
        lC = Text("C", font="PingFang SC", font_size=24, color=C_LABEL).next_to(C, RIGHT, buff=0.12)
        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.4)

        # 直角标记在 B
        mark_B = self._right_angle_mark(B, A, C, size=0.22, color=C_ANGLE_ARC)
        self.play(Create(mark_B), run_time=0.5)

        # 闪光强调直角
        self.play(Flash(B, color=C_ANGLE_ARC, flash_radius=0.45, num_lines=8), run_time=0.5)

        # 直角标注
        right_label = Text(
            "直角 90°",
            font="PingFang SC", font_size=24, color=C_ANGLE_ARC
        ).next_to(B, DOWN + LEFT*0.5, buff=0.45)
        self.play(FadeIn(right_label), run_time=0.4)

        # 另外两个锐角
        arc_A = self._make_angle_arc(B, A, C, radius=0.35, color=C_DIM)
        arc_C = self._make_angle_arc(A, C, B, radius=0.35, color=C_DIM)
        deg_A = int(round(np.degrees(self._angle_at(B, A, C))))
        deg_C = int(round(np.degrees(self._angle_at(A, C, B))))
        lbl_A = Text(f"{deg_A}°", font="PingFang SC", font_size=22, color=C_DIM)
        lbl_C = Text(f"{deg_C}°", font="PingFang SC", font_size=22, color=C_DIM)
        lbl_A.next_to(A, RIGHT + UP * 0.3, buff=0.45)
        lbl_C.next_to(C, LEFT + DOWN * 0.3, buff=0.45)

        self.play(
            Create(arc_A), Create(arc_C),
            FadeIn(lbl_A), FadeIn(lbl_C),
            run_time=0.6
        )

        # 说明
        def_text = Text(
            "有一个直角",
            font="PingFang SC", font_size=32, color=C_LABEL
        ).move_to(DOWN * 3.5)
        sub_text = Text(
            "另外两个角都是锐角",
            font="PingFang SC", font_size=24, color=C_DIM
        ).next_to(def_text, DOWN, buff=0.15)

        self.play(FadeIn(def_text), run_time=0.5)
        self.play(FadeIn(sub_text), run_time=0.4)

        # 斜边标注
        hyp_label = Text(
            "斜边（最长边）",
            font="PingFang SC", font_size=20, color=C_HIGHLIGHT
        )
        mid_AC = (A + C) / 2
        hyp_label.next_to(mid_AC, RIGHT, buff=0.1)
        hyp_line = Line(A, C, color=C_HIGHLIGHT, stroke_width=4)

        self.play(Create(hyp_line), FadeIn(hyp_label), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(sec_title), FadeOut(tri),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(mark_B), FadeOut(right_label),
            FadeOut(arc_A), FadeOut(arc_C),
            FadeOut(lbl_A), FadeOut(lbl_C),
            FadeOut(def_text), FadeOut(sub_text),
            FadeOut(hyp_line), FadeOut(hyp_label),
            run_time=0.5
        )

    # ═════════════════════════════════════════════════════════
    # Scene 5 — 钝角三角形
    # ═════════════════════════════════════════════════════════
    def scene_5_obtuse(self):
        sec_title = Text(
            "钝角三角形",
            font="PingFang SC", font_size=46, color=C_OBTUSE, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(Write(sec_title), run_time=0.6)

        SCALE = 1.1
        OFF = DOWN * 0.6
        A = self.obtuse_A * SCALE + OFF
        B = self.obtuse_B * SCALE + OFF
        C = self.obtuse_C * SCALE + OFF

        tri = self._make_triangle(A, B, C, color=C_OBTUSE, fill_opacity=0.08, fill_color=C_OBTUSE)
        self.play(Create(tri), run_time=1.0)

        lA = Text("A", font="PingFang SC", font_size=24, color=C_LABEL).next_to(A, UL, buff=0.12)
        lB = Text("B", font="PingFang SC", font_size=24, color=C_LABEL).next_to(B, DOWN, buff=0.12)
        lC = Text("C", font="PingFang SC", font_size=24, color=C_LABEL).next_to(C, RIGHT, buff=0.12)
        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.4)

        # 钝角弧在 B
        arc_B = self._make_angle_arc(A, B, C, radius=0.42, color=C_ANGLE_ARC)
        deg_B = int(round(np.degrees(self._angle_at(A, B, C))))
        lbl_B = Text(f"{deg_B}°", font="PingFang SC", font_size=24, color=C_ANGLE_ARC)
        lbl_B.next_to(B, UP * 0.6, buff=0.45)

        self.play(Create(arc_B), FadeIn(lbl_B), run_time=0.6)
        self.play(Flash(B, color=C_ANGLE_ARC, flash_radius=0.50, num_lines=8), run_time=0.5)

        obtuse_label = Text(
            "钝角 > 90°",
            font="PingFang SC", font_size=24, color=C_ANGLE_ARC
        ).next_to(lbl_B, UP, buff=0.1)
        self.play(FadeIn(obtuse_label), run_time=0.4)

        # 另两个锐角
        arc_A = self._make_angle_arc(B, A, C, radius=0.35, color=C_DIM)
        arc_C = self._make_angle_arc(A, C, B, radius=0.35, color=C_DIM)
        deg_A = int(round(np.degrees(self._angle_at(B, A, C))))
        deg_C = int(round(np.degrees(self._angle_at(A, C, B))))
        lbl_A2 = Text(f"{deg_A}°", font="PingFang SC", font_size=22, color=C_DIM)
        lbl_C2 = Text(f"{deg_C}°", font="PingFang SC", font_size=22, color=C_DIM)
        lbl_A2.next_to(A, RIGHT + DOWN * 0.2, buff=0.45)
        lbl_C2.next_to(C, LEFT + UP * 0.2, buff=0.45)

        self.play(
            Create(arc_A), Create(arc_C),
            FadeIn(lbl_A2), FadeIn(lbl_C2),
            run_time=0.6
        )

        def_text = Text(
            "有一个钝角",
            font="PingFang SC", font_size=32, color=C_LABEL
        ).move_to(DOWN * 3.5)
        sub_text = Text(
            "另外两个角都是锐角",
            font="PingFang SC", font_size=24, color=C_DIM
        ).next_to(def_text, DOWN, buff=0.15)

        self.play(FadeIn(def_text), run_time=0.5)
        self.play(FadeIn(sub_text), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(sec_title), FadeOut(tri),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(arc_B), FadeOut(lbl_B), FadeOut(obtuse_label),
            FadeOut(arc_A), FadeOut(arc_C),
            FadeOut(lbl_A2), FadeOut(lbl_C2),
            FadeOut(def_text), FadeOut(sub_text),
            run_time=0.5
        )

    # ═════════════════════════════════════════════════════════
    # Scene 6 — 三类汇总对比
    # ═════════════════════════════════════════════════════════
    def scene_6_summary(self):
        title = Text(
            "三类三角形总结",
            font="PingFang SC", font_size=40, color=C_HIGHLIGHT, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # ── 三个卡片排列 ──
        s = 0.72

        def make_card(A, B, C, tri_color, name, rule):
            tri = self._make_triangle(A * s, B * s, C * s,
                                      color=tri_color, fill_opacity=0.12, fill_color=tri_color)
            name_t = Text(name, font="PingFang SC", font_size=28, color=tri_color, weight=BOLD)
            rule_t = Text(rule, font="PingFang SC", font_size=20, color=C_DIM)
            card = VGroup(tri, name_t, rule_t).arrange(DOWN, buff=0.25)
            return card

        card_a = make_card(self.acute_A, self.acute_B, self.acute_C,
                           C_ACUTE, "锐角三角形", "3个锐角")
        card_r = make_card(self.right_A, self.right_B, self.right_C,
                           C_RIGHT, "直角三角形", "1个直角+2个锐角")
        card_o = make_card(self.obtuse_A, self.obtuse_B, self.obtuse_C,
                           C_OBTUSE, "钝角三角形", "1个钝角+2个锐角")

        all_cards = VGroup(card_a, card_r, card_o)
        all_cards.arrange(RIGHT, buff=0.6)
        all_cards.move_to(UP * 1.5)

        self.play(
            LaggedStart(
                FadeIn(card_a, shift=UP * 0.4),
                FadeIn(card_r, shift=UP * 0.4),
                FadeIn(card_o, shift=UP * 0.4),
                lag_ratio=0.3
            ),
            run_time=1.2
        )
        self.wait(0.5)

        # ── 表格式对比 ──
        # 行标题
        row_title = Text(
            "类型     角的情况",
            font="PingFang SC", font_size=22, color=C_LABEL
        ).move_to(DOWN * 1.5)

        rows = VGroup()
        data = [
            ("锐角三角形", "三个角全是锐角", C_ACUTE),
            ("直角三角形", "一个直角,两个锐角", C_RIGHT),
            ("钝角三角形", "一个钝角,两个锐角", C_OBTUSE),
        ]
        y_start = -2.3
        for i, (name, desc, color) in enumerate(data):
            n_t = Text(name, font="PingFang SC", font_size=22, color=color)
            d_t = Text(desc, font="PingFang SC", font_size=22, color=C_LABEL)
            row = VGroup(n_t, d_t).arrange(RIGHT, buff=0.6)
            row.move_to(UP * (y_start - i * 0.85))
            rows.add(row)

        self.play(FadeIn(row_title), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.3),
            run_time=1.0
        )
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(all_cards),
            FadeOut(row_title), FadeOut(rows),
            run_time=0.5
        )

    # ═════════════════════════════════════════════════════════
    # Scene 7 — 重要提醒
    # ═════════════════════════════════════════════════════════
    def scene_7_warning(self):
        warn_title = Text(
            "重要提醒！",
            font="PingFang SC", font_size=44, color=C_OBTUSE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(Write(warn_title), run_time=0.6)

        # 提醒1
        msg1_line1 = Text(
            "一个三角形",
            font="PingFang SC", font_size=32, color=C_LABEL
        )
        msg1_line2 = Text(
            "最多只有一个直角",
            font="PingFang SC", font_size=32, color=C_RIGHT, weight=BOLD
        )
        msg1_line3 = Text(
            "或一个钝角",
            font="PingFang SC", font_size=32, color=C_OBTUSE, weight=BOLD
        )
        msg1 = VGroup(msg1_line1, msg1_line2, msg1_line3).arrange(DOWN, buff=0.2)
        msg1.move_to(UP * 3.5)

        self.play(FadeIn(msg1, shift=UP * 0.3), run_time=0.7)
        self.wait(0.5)

        # 为什么：角度和 = 180°
        why_title = Text(
            "为什么？",
            font="PingFang SC", font_size=30, color=C_HIGHLIGHT
        ).move_to(UP * 1.8)
        self.play(FadeIn(why_title), run_time=0.4)

        why_formula = VGroup(
            Text("三角形三个角之和 = 180°",
                 font="PingFang SC", font_size=26, color=C_LABEL),
        ).move_to(UP * 1.0)
        self.play(FadeIn(why_formula), run_time=0.5)

        # 演示：若有两个直角
        demo_text = Text(
            "如果有两个直角：",
            font="PingFang SC", font_size=26, color=C_DIM
        ).move_to(UP * 0.1)

        eq_parts = VGroup(
            Text("90°", font="PingFang SC", font_size=28, color=C_RIGHT),
            Text("+", font="PingFang SC", font_size=28, color=C_LABEL),
            Text("90°", font="PingFang SC", font_size=28, color=C_RIGHT),
            Text("= 180°", font="PingFang SC", font_size=28, color=C_LABEL),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 0.7)

        cross = Text(
            "第三个角只能是0°，不是三角形！",
            font="PingFang SC", font_size=24, color=C_OBTUSE
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(demo_text), run_time=0.4)
        self.play(FadeIn(eq_parts), run_time=0.5)
        self.play(FadeIn(cross), run_time=0.5)
        self.wait(1.5)

        # 结论框
        concl = Text(
            "不可能有两个或三个直角/钝角！",
            font="PingFang SC", font_size=26, color=C_HIGHLIGHT, weight=BOLD
        ).move_to(DOWN * 2.8)
        border = SurroundingRectangle(concl, color=C_HIGHLIGHT, buff=0.18, stroke_width=2.5)
        self.play(FadeIn(concl), Create(border), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(warn_title), FadeOut(msg1), FadeOut(why_title),
            FadeOut(why_formula), FadeOut(demo_text), FadeOut(eq_parts),
            FadeOut(cross), FadeOut(concl), FadeOut(border),
            run_time=0.6
        )

    # ═════════════════════════════════════════════════════════
    # Scene 8 — 片尾关注
    # ═════════════════════════════════════════════════════════
    def scene_8_outro(self):
        # 三个彩色三角形装饰
        s = 0.55
        tri_a = self._make_triangle(
            self.acute_A * s, self.acute_B * s, self.acute_C * s,
            color=C_ACUTE, fill_color=C_ACUTE, fill_opacity=0.5
        ).shift(LEFT * 2.5 + UP * 0.5)
        tri_r = self._make_triangle(
            self.right_A * s, self.right_B * s, self.right_C * s,
            color=C_RIGHT, fill_color=C_RIGHT, fill_opacity=0.5
        ).shift(UP * 0.5)
        tri_o = self._make_triangle(
            self.obtuse_A * s, self.obtuse_B * s, self.obtuse_C * s,
            color=C_OBTUSE, fill_color=C_OBTUSE, fill_opacity=0.5
        ).shift(RIGHT * 2.5 + UP * 0.5)

        self.play(
            LaggedStart(
                GrowFromCenter(tri_a),
                GrowFromCenter(tri_r),
                GrowFromCenter(tri_o),
                lag_ratio=0.25
            ),
            run_time=0.9
        )

        author_large = Text(
            "上海初高中数学直通车",
            font="PingFang SC", font_size=38, color=WHITE
        ).move_to(DOWN * 1.0)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC", font_size=28, color=C_DIM
        ).next_to(author_large, DOWN, buff=0.2)

        follow = Text(
            "关注我，学更多数学技巧！",
            font="PingFang SC", font_size=30, color=C_HIGHLIGHT
        ).move_to(DOWN * 2.8)

        self.play(
            FadeIn(author_large, shift=UP * 0.3),
            FadeIn(author_id, shift=UP * 0.3),
            run_time=0.7
        )
        self.play(FadeIn(follow, scale=1.1), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(self.author),
            FadeOut(tri_a), FadeOut(tri_r), FadeOut(tri_o),
            FadeOut(author_large), FadeOut(author_id), FadeOut(follow),
            run_time=0.8
        )
        self.wait(0.3)


# ── 运行命令 ──────────────────────────────────────────────────
# manim -qm 003_三角形按角分类.py TriangleAngleClassifyLesson
