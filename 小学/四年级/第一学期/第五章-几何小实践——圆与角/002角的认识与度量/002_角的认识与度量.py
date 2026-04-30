"""
002_角的认识与度量.py — 角的认识与度量 教学动画

知识点:
  - 角的定义: 从一点引出两条射线所组成的图形
  - 角的组成: 顶点 + 两条边
  - 角的度量: 度 (°)，将圆分成360份，每份1度
  - 特殊角: 直角(90°), 平角(180°), 周角(360°)
  - 量角器的使用方法

年级: 四年级第一学期
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
BG_COLOR          = "#1a1a2e"
COLOR_ANGLE       = "#3b82f6"      # 蓝  — 角弧
COLOR_VERTEX      = "#f59e0b"      # 橙  — 顶点
COLOR_RAY         = "#22c55e"      # 绿  — 射线 / 边
COLOR_DEGREE      = "#f472b6"      # 粉  — 度数标注
COLOR_HL          = "#fbbf24"      # 黄  — 高亮
COLOR_CIRCLE      = "#a78bfa"      # 紫  — 圆
COLOR_PROTRACTOR  = "#06b6d4"      # 青  — 量角器
COLOR_AUTHOR      = "#6b7280"
FONT              = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class AngleMeasureLesson(Scene):
    """
    角的认识与度量教学动画
    场景顺序:
      1. 开场钩子
      2. 角的定义（从两条射线引出）
      3. 角的各部分名称（顶点、边）
      4. 角的度量单位——"度"的来源（圆360等份）
      5. 特殊角: 直角、平角、周角
      6. 量角器的使用方法
      7. 总结公式
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_angle_definition()
        self.scene_3_angle_parts()
        self.scene_4_degree_origin()
        self.scene_5_special_angles()
        self.scene_6_protractor()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标（NumPy 精确计算）"""

        # ===== 演示角（45°）=====
        self.demo_vertex  = np.array([0.0, 1.0, 0.0])
        self.RAY_LEN = 3.0
        demo_angle_deg = 45.0
        demo_angle_rad = np.radians(demo_angle_deg)

        # 第一条边: 水平向右
        self.demo_ray1_end = self.demo_vertex + self.RAY_LEN * np.array([1.0, 0.0, 0.0])
        # 第二条边: 逆时针旋转 demo_angle_deg
        self.demo_ray2_end = self.demo_vertex + self.RAY_LEN * np.array([
            np.cos(demo_angle_rad), np.sin(demo_angle_rad), 0.0
        ])

        # ===== 量角器场景（场景6）=====
        # 被测角顶点
        self.meas_vertex = np.array([0.0, -1.0, 0.0])
        meas_angle_deg = 50.0
        meas_angle_rad = np.radians(meas_angle_deg)
        self.meas_ray1_end = self.meas_vertex + 3.0 * np.array([1.0, 0.0, 0.0])
        self.meas_ray2_end = self.meas_vertex + 3.0 * np.array([
            np.cos(meas_angle_rad), np.sin(meas_angle_rad), 0.0
        ])

        # ===== 验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        eps = 1e-9
        # 验证 demo 射线长度
        r1 = np.linalg.norm(self.demo_ray1_end - self.demo_vertex)
        r2 = np.linalg.norm(self.demo_ray2_end - self.demo_vertex)
        assert abs(r1 - self.RAY_LEN) < eps, f"ray1 length error: {r1}"
        assert abs(r2 - self.RAY_LEN) < eps, f"ray2 length error: {r2}"

        # 验证演示角度
        v1 = self.demo_ray1_end - self.demo_vertex
        v2 = self.demo_ray2_end - self.demo_vertex
        cos_a = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_a = np.clip(cos_a, -1.0, 1.0)
        angle_deg = np.degrees(np.arccos(cos_a))
        assert abs(angle_deg - 45.0) < 1e-4, f"demo angle error: {angle_deg}"

    # ------------------------------------------------------------------
    # 辅助方法
    # ------------------------------------------------------------------

    def make_author_tag(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)

    def make_angle_arc(self, vertex, ray1_end, ray2_end, radius=0.5, color=COLOR_ANGLE):
        """安全创建角弧：根据叉积自动决定 other_angle 方向"""
        v1 = ray1_end - vertex
        v2 = ray2_end - vertex
        cross_z = v1[0] * v2[1] - v1[1] * v2[0]
        line1 = Line(vertex, ray1_end)
        line2 = Line(vertex, ray2_end)
        if cross_z >= 0:
            arc = Angle(line1, line2, radius=radius, other_angle=False, color=color)
        else:
            arc = Angle(line1, line2, radius=radius, other_angle=True, color=color)
        return arc

    def make_right_angle_mark(self, vertex, ray1_end, ray2_end, size=0.25):
        """创建直角小方块标记"""
        v1 = (ray1_end - vertex)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = (ray2_end - vertex)
        v2 = v2 / np.linalg.norm(v2) * size
        sq = Polygon(
            vertex, vertex + v1, vertex + v1 + v2, vertex + v2,
            color=COLOR_HL, stroke_width=2.0, fill_opacity=0
        )
        return sq

    # ------------------------------------------------------------------
    # 场景 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author_tag()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text("角是什么？怎么度量角？", font=FONT, font_size=36, color=COLOR_HL
                    ).move_to(UP * 5.5)
        self.play(Write(hook), run_time=0.8)

        sub = Text("四年级·角的认识与度量", font=FONT, font_size=26, color=GRAY_A
                   ).move_to(UP * 4.7)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # 用动画旋转的射线展示"角"
        vtx = np.array([0.0, 1.0, 0.0])
        ray_fixed = Line(vtx, vtx + 3.0 * RIGHT, color=COLOR_RAY, stroke_width=4)
        tracker = ValueTracker(0)
        ray_rotating = always_redraw(
            lambda: Line(
                vtx,
                vtx + 3.0 * np.array([
                    np.cos(tracker.get_value()),
                    np.sin(tracker.get_value()),
                    0.0
                ]),
                color=COLOR_ANGLE, stroke_width=4
            )
        )
        vtx_dot = Dot(vtx, color=COLOR_VERTEX, radius=0.12)

        self.play(Create(ray_fixed), FadeIn(vtx_dot), run_time=0.5)
        self.add(ray_rotating)
        self.play(tracker.animate.set_value(np.radians(60)), run_time=1.2)
        self.wait(0.3)

        self.play(
            FadeOut(hook), FadeOut(sub),
            FadeOut(ray_fixed), FadeOut(ray_rotating), FadeOut(vtx_dot),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 2: 角的定义
    # ------------------------------------------------------------------

    def scene_2_angle_definition(self):
        title = Text("角的定义", font=FONT, font_size=38, color=COLOR_HL
                     ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 说明文字
        line1 = Text("从一点引出两条射线，", font=FONT, font_size=26, color=WHITE
                     ).move_to(UP * 4.9)
        line2 = Text("所组成的图形叫做角。", font=FONT, font_size=26, color=WHITE
                     ).move_to(UP * 4.3)
        self.play(Write(line1), run_time=0.6)
        self.play(Write(line2), run_time=0.6)

        # 画顶点
        vtx = self.demo_vertex.copy()
        vtx_dot = Dot(vtx, color=COLOR_VERTEX, radius=0.14)
        self.play(FadeIn(vtx_dot, scale=0.5), run_time=0.4)

        # 从顶点引出第一条射线（带箭头）
        ray1 = Arrow(
            vtx, self.demo_ray1_end,
            color=COLOR_RAY, buff=0, stroke_width=5,
            max_tip_length_to_length_ratio=0.08
        )
        self.play(Create(ray1), run_time=0.7)

        # 从顶点引出第二条射线
        ray2 = Arrow(
            vtx, self.demo_ray2_end,
            color=COLOR_RAY, buff=0, stroke_width=5,
            max_tip_length_to_length_ratio=0.08
        )
        self.play(Create(ray2), run_time=0.7)

        # 角弧
        arc = self.make_angle_arc(
            vtx, self.demo_ray1_end, self.demo_ray2_end,
            radius=0.55, color=COLOR_ANGLE
        )
        self.play(Create(arc), run_time=0.5)

        # 角的符号 ∠
        angle_label = MathTex(r"\angle", color=COLOR_ANGLE, font_size=40
                              ).move_to(vtx + np.array([0.9, 0.3, 0.0]))
        self.play(Write(angle_label), run_time=0.4)

        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(line1), FadeOut(line2),
            FadeOut(vtx_dot), FadeOut(ray1), FadeOut(ray2),
            FadeOut(arc), FadeOut(angle_label),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 3: 角的各部分名称
    # ------------------------------------------------------------------

    def scene_3_angle_parts(self):
        title = Text("角的组成", font=FONT, font_size=38, color=COLOR_HL
                     ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        vtx = self.demo_vertex.copy()
        vtx_dot = Dot(vtx, color=COLOR_VERTEX, radius=0.14)

        ray1 = Line(vtx, self.demo_ray1_end, color=COLOR_RAY, stroke_width=5)
        ray2 = Line(vtx, self.demo_ray2_end, color=COLOR_RAY, stroke_width=5)
        arc = self.make_angle_arc(
            vtx, self.demo_ray1_end, self.demo_ray2_end,
            radius=0.55, color=COLOR_ANGLE
        )

        self.play(
            FadeIn(vtx_dot), Create(ray1), Create(ray2), Create(arc),
            run_time=0.8
        )

        # 顶点标注
        vtx_label = Text("顶点", font=FONT, font_size=26, color=COLOR_VERTEX
                         ).next_to(vtx_dot, DL, buff=0.15)
        vtx_arrow = Arrow(vtx_label.get_right() + RIGHT * 0.05, vtx, buff=0.15,
                          color=COLOR_VERTEX, stroke_width=2,
                          max_tip_length_to_length_ratio=0.15)
        self.play(Write(vtx_label), Create(vtx_arrow), run_time=0.6)
        self.wait(0.4)

        # 两条边标注
        mid_ray1 = (vtx + self.demo_ray1_end) / 2
        side1_label = Text("边", font=FONT, font_size=26, color=COLOR_RAY
                           ).next_to(mid_ray1, DOWN, buff=0.2)
        self.play(Write(side1_label), run_time=0.4)

        mid_ray2 = (vtx + self.demo_ray2_end) / 2
        side2_label = Text("边", font=FONT, font_size=26, color=COLOR_RAY
                           ).next_to(mid_ray2, UP + LEFT * 0.5, buff=0.15)
        self.play(Write(side2_label), run_time=0.4)

        # 总结文字
        summary = Text("顶点 + 两条边 = 角", font=FONT, font_size=28, color=COLOR_HL
                       ).move_to(DOWN * 3.5)
        self.play(FadeIn(summary, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(vtx_dot), FadeOut(ray1), FadeOut(ray2),
            FadeOut(arc), FadeOut(vtx_label), FadeOut(vtx_arrow),
            FadeOut(side1_label), FadeOut(side2_label), FadeOut(summary),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 4: 度的来源——圆等分360份
    # ------------------------------------------------------------------

    def scene_4_degree_origin(self):
        title = Text("角的度量单位——度", font=FONT, font_size=34, color=COLOR_HL
                     ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        explain = Text("把圆平均分成 360 份，", font=FONT, font_size=26, color=WHITE
                       ).move_to(UP * 5.0)
        explain2 = Text("其中 1 份所对的角是 1 度，记作 1°", font=FONT, font_size=24, color=WHITE
                        ).move_to(UP * 4.4)
        self.play(Write(explain), run_time=0.5)
        self.play(Write(explain2), run_time=0.6)

        # 画圆
        circle_center = np.array([0.0, 0.5, 0.0])
        circle_r = 2.2
        circle = Circle(radius=circle_r, color=COLOR_CIRCLE, stroke_width=3
                        ).move_to(circle_center)
        self.play(Create(circle), run_time=1.0)

        # 圆心点
        c_dot = Dot(circle_center, color=COLOR_VERTEX, radius=0.1)
        self.play(FadeIn(c_dot), run_time=0.3)

        # 画360等份刻度（每10度一条短线）
        tick_lines = VGroup()
        for deg in range(0, 360, 10):
            rad = np.radians(deg)
            outer = circle_center + circle_r * np.array([np.cos(rad), np.sin(rad), 0])
            inner = circle_center + (circle_r - 0.18) * np.array([np.cos(rad), np.sin(rad), 0])
            tick_lines.add(Line(inner, outer, stroke_width=1.2, color=COLOR_CIRCLE))

        self.play(Create(tick_lines), run_time=1.0)

        # 高亮其中一份（0° 到 1°）
        one_deg_rad = np.radians(1)
        one_deg_arc = Arc(
            radius=circle_r, start_angle=0, angle=one_deg_rad,
            arc_center=circle_center, color=COLOR_HL, stroke_width=6
        )
        self.play(Create(one_deg_arc), run_time=0.5)

        one_deg_label = MathTex(r"1^{\circ}", color=COLOR_HL, font_size=32
                                ).move_to(circle_center + (circle_r + 0.5) * np.array([
                                    np.cos(one_deg_rad / 2), np.sin(one_deg_rad / 2), 0
                                ]))
        self.play(Write(one_deg_label), run_time=0.4)

        # 展示 360° 一圈
        full_arc = Arc(
            radius=circle_r * 0.55, start_angle=0, angle=2 * np.pi,
            arc_center=circle_center, color=COLOR_DEGREE, stroke_width=4
        )
        full_label = MathTex(r"360^{\circ}", color=COLOR_DEGREE, font_size=36
                             ).move_to(circle_center + np.array([0.0, -0.55, 0.0]))
        self.play(Create(full_arc), Write(full_label), run_time=1.2)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(explain), FadeOut(explain2),
            FadeOut(circle), FadeOut(c_dot), FadeOut(tick_lines),
            FadeOut(one_deg_arc), FadeOut(one_deg_label),
            FadeOut(full_arc), FadeOut(full_label),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 5: 特殊角
    # ------------------------------------------------------------------

    def scene_5_special_angles(self):
        title = Text("特殊角", font=FONT, font_size=38, color=COLOR_HL
                     ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        # ---- 5a. 直角 90° ----
        sub_title = Text("直角 = 90°", font=FONT, font_size=30, color=COLOR_RAY
                         ).move_to(UP * 5.0)
        self.play(FadeIn(sub_title), run_time=0.4)

        vtx = np.array([0.0, 1.5, 0.0])
        r1_end = vtx + 3.0 * RIGHT
        r2_end = vtx + 3.0 * UP
        ray1 = Line(vtx, r1_end, color=WHITE, stroke_width=5)
        ray2 = Line(vtx, r2_end, color=WHITE, stroke_width=5)
        vtx_dot = Dot(vtx, color=COLOR_VERTEX, radius=0.12)
        sq_mark = self.make_right_angle_mark(vtx, r1_end, r2_end, size=0.3)

        self.play(Create(ray1), Create(ray2), FadeIn(vtx_dot), run_time=0.8)
        self.play(Create(sq_mark), run_time=0.4)

        deg_90 = MathTex(r"90^{\circ}", color=COLOR_DEGREE, font_size=40
                         ).move_to(vtx + np.array([0.7, 0.7, 0.0]))
        self.play(Write(deg_90), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(sub_title), FadeOut(ray1), FadeOut(ray2),
            FadeOut(vtx_dot), FadeOut(sq_mark), FadeOut(deg_90),
            run_time=0.4
        )

        # ---- 5b. 平角 180° ----
        sub_title2 = Text("平角 = 180°", font=FONT, font_size=30, color=COLOR_ANGLE
                          ).move_to(UP * 5.0)
        self.play(FadeIn(sub_title2), run_time=0.4)

        vtx2 = np.array([0.0, 1.5, 0.0])
        p_r1_end = vtx2 + 3.5 * RIGHT
        p_r2_end = vtx2 + 3.5 * LEFT
        p_ray1 = Line(vtx2, p_r1_end, color=WHITE, stroke_width=5)
        p_ray2 = Line(vtx2, p_r2_end, color=WHITE, stroke_width=5)
        p_vtx_dot = Dot(vtx2, color=COLOR_VERTEX, radius=0.12)

        # 半圆弧
        p_arc = Arc(
            radius=0.7, start_angle=0, angle=np.pi,
            arc_center=vtx2, color=COLOR_ANGLE, stroke_width=4
        )
        self.play(Create(p_ray1), Create(p_ray2), FadeIn(p_vtx_dot), run_time=0.7)
        self.play(Create(p_arc), run_time=0.5)

        deg_180 = MathTex(r"180^{\circ}", color=COLOR_DEGREE, font_size=40
                          ).move_to(vtx2 + np.array([0.0, 1.1, 0.0]))
        self.play(Write(deg_180), run_time=0.4)

        note_flat = Text("两条边在同一直线上", font=FONT, font_size=22, color=GRAY_A
                         ).move_to(DOWN * 3.5)
        self.play(FadeIn(note_flat), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(sub_title2), FadeOut(p_ray1), FadeOut(p_ray2),
            FadeOut(p_vtx_dot), FadeOut(p_arc), FadeOut(deg_180), FadeOut(note_flat),
            run_time=0.4
        )

        # ---- 5c. 周角 360° ----
        sub_title3 = Text("周角 = 360°", font=FONT, font_size=30, color=COLOR_CIRCLE
                          ).move_to(UP * 5.0)
        self.play(FadeIn(sub_title3), run_time=0.4)

        vtx3 = np.array([0.0, 1.5, 0.0])
        full_ray = Line(vtx3, vtx3 + 3.0 * RIGHT, color=WHITE, stroke_width=5)
        full_vtx_dot = Dot(vtx3, color=COLOR_VERTEX, radius=0.12)
        full_circle_arc = Arc(
            radius=0.8, start_angle=0, angle=2 * np.pi,
            arc_center=vtx3, color=COLOR_CIRCLE, stroke_width=4
        )
        self.play(Create(full_ray), FadeIn(full_vtx_dot), run_time=0.5)
        self.play(Create(full_circle_arc), run_time=0.8)

        deg_360 = MathTex(r"360^{\circ}", color=COLOR_DEGREE, font_size=40
                          ).move_to(vtx3 + np.array([1.5, 0.8, 0.0]))
        self.play(Write(deg_360), run_time=0.4)

        note_full = Text("旋转一圈回到原位", font=FONT, font_size=22, color=GRAY_A
                         ).move_to(DOWN * 3.5)
        self.play(FadeIn(note_full), run_time=0.4)
        self.wait(1.0)

        # 汇总公式
        formula_group = VGroup(
            Text("直角 = 90°",   font=FONT, font_size=24, color=COLOR_RAY),
            Text("平角 = 180°",  font=FONT, font_size=24, color=COLOR_ANGLE),
            Text("周角 = 360°",  font=FONT, font_size=24, color=COLOR_CIRCLE),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 4.8)
        self.play(
            FadeOut(sub_title3), FadeOut(full_ray), FadeOut(full_vtx_dot),
            FadeOut(full_circle_arc), FadeOut(deg_360), FadeOut(note_full),
            run_time=0.4
        )
        self.play(FadeIn(formula_group, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(title), FadeOut(formula_group), run_time=0.5)

    # ------------------------------------------------------------------
    # 场景 6: 量角器的使用
    # ------------------------------------------------------------------

    def scene_6_protractor(self):
        title = Text("用量角器量角", font=FONT, font_size=36, color=COLOR_HL
                     ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        # ---- 被量的角 ----
        vtx = self.meas_vertex.copy()
        vtx_dot = Dot(vtx, color=COLOR_VERTEX, radius=0.13)
        ray1 = Line(vtx, self.meas_ray1_end, color=WHITE, stroke_width=5)
        ray2 = Line(vtx, self.meas_ray2_end, color=WHITE, stroke_width=5)

        self.play(FadeIn(vtx_dot), Create(ray1), Create(ray2), run_time=0.8)

        # ---- 量角器（半圆形示意）----
        prot_r = 2.8
        prot_center = vtx.copy()   # 中心对准顶点

        # 半圆弧
        prot_arc = Arc(
            radius=prot_r, start_angle=0, angle=np.pi,
            arc_center=prot_center,
            color=COLOR_PROTRACTOR, stroke_width=3
        )
        # 量角器底边（直径）
        prot_base = Line(
            prot_center + prot_r * LEFT,
            prot_center + prot_r * RIGHT,
            color=COLOR_PROTRACTOR, stroke_width=3
        )

        # 刻度（0°~180°，每10°一条）
        tick_group = VGroup()
        label_group = VGroup()
        for deg in range(0, 181, 10):
            rad = np.radians(deg)
            outer_pt = prot_center + prot_r * np.array([np.cos(rad), np.sin(rad), 0])
            tick_len = 0.2 if deg % 30 == 0 else 0.1
            inner_pt = prot_center + (prot_r - tick_len) * np.array([np.cos(rad), np.sin(rad), 0])
            tick_group.add(Line(inner_pt, outer_pt,
                                stroke_width=1.5, color=COLOR_PROTRACTOR))
            # 仅标注 0, 90, 180
            if deg in (0, 90, 180):
                label_pt = prot_center + (prot_r + 0.38) * np.array([np.cos(rad), np.sin(rad), 0])
                lbl = MathTex(
                    rf"{deg}^\circ",
                    font_size=20, color=COLOR_PROTRACTOR
                ).move_to(label_pt)
                label_group.add(lbl)

        prot_group = VGroup(prot_arc, prot_base, tick_group, label_group)

        # 步骤提示
        step_text = Text("① 中心点对准顶点", font=FONT, font_size=24, color=WHITE
                         ).move_to(UP * 4.5)
        self.play(Write(step_text), run_time=0.5)
        self.play(FadeIn(prot_group), run_time=0.8)
        self.wait(0.6)

        step2_text = Text("② 0° 刻度线与一条边重合", font=FONT, font_size=24, color=WHITE
                          ).move_to(UP * 4.5)
        self.play(Transform(step_text, step2_text), run_time=0.4)
        zero_highlight = Line(
            prot_center, prot_center + prot_r * RIGHT,
            color=COLOR_HL, stroke_width=4
        )
        self.play(Create(zero_highlight), run_time=0.5)
        self.wait(0.6)

        step3_text = Text("③ 看另一条边对应的刻度", font=FONT, font_size=24, color=WHITE
                          ).move_to(UP * 4.5)
        self.play(Transform(step_text, step3_text), run_time=0.4)

        # 高亮第二条边交量角器弧的位置
        meas_angle_deg = 50.0
        meas_angle_rad = np.radians(meas_angle_deg)
        arc_pt = prot_center + prot_r * np.array([np.cos(meas_angle_rad), np.sin(meas_angle_rad), 0])

        read_line = DashedLine(
            self.meas_ray2_end, arc_pt,
            dash_length=0.12, color=COLOR_DEGREE, stroke_width=2
        )
        read_dot = Dot(arc_pt, color=COLOR_DEGREE, radius=0.1)
        self.play(Create(read_line), FadeIn(read_dot), run_time=0.6)

        # 读数标注
        read_label = MathTex(r"50^{\circ}", color=COLOR_DEGREE, font_size=42
                             ).move_to(vtx + np.array([0.85, 0.55, 0.0]))
        self.play(Write(read_label), run_time=0.5)

        result_text = Text("这个角是 50°", font=FONT, font_size=28, color=COLOR_HL
                           ).move_to(DOWN * 4.5)
        self.play(FadeIn(result_text, shift=UP * 0.2), run_time=0.5)
        self.wait(1.8)

        # 清理
        self.play(
            FadeOut(title), FadeOut(vtx_dot), FadeOut(ray1), FadeOut(ray2),
            FadeOut(prot_group), FadeOut(step_text), FadeOut(zero_highlight),
            FadeOut(read_line), FadeOut(read_dot), FadeOut(read_label),
            FadeOut(result_text),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 7: 总结公式
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        title = Text("知识总结", font=FONT, font_size=38, color=COLOR_HL
                     ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        items = [
            ("角 = 顶点 + 两条边",   WHITE),
            ("度量单位: 度 (°)",      COLOR_DEGREE),
            ("圆 360 等份，每份 1°",  COLOR_CIRCLE),
            ("直角 = 90°",            COLOR_RAY),
            ("平角 = 180°",           COLOR_ANGLE),
            ("周角 = 360°",           COLOR_CIRCLE),
        ]
        texts = VGroup(*[
            Text(txt, font=FONT, font_size=27, color=col)
            for txt, col in items
        ]).arrange(DOWN, buff=0.42, aligned_edge=LEFT).move_to(np.array([0.0, 0.8, 0.0]))

        for t in texts:
            self.play(FadeIn(t, shift=RIGHT * 0.3), run_time=0.25)

        # 量角器步骤小卡
        steps_title = Text("量角器三步法:", font=FONT, font_size=25, color=COLOR_PROTRACTOR
                           ).move_to(DOWN * 3.5)
        steps = VGroup(
            Text("① 中心 → 顶点",      font=FONT, font_size=22, color=GRAY_A),
            Text("② 0° 线 → 一条边",   font=FONT, font_size=22, color=GRAY_A),
            Text("③ 读另一条边的度数",  font=FONT, font_size=22, color=GRAY_A),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT).move_to(DOWN * 4.9)

        self.play(FadeIn(steps_title), run_time=0.4)
        self.play(FadeIn(steps, shift=UP * 0.2), run_time=0.5)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(texts),
            FadeOut(steps_title), FadeOut(steps),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=40, color=WHITE
                          ).move_to(UP * 1.5)
        author_id  = Text("@emptyandcalm", font=FONT, font_size=32, color=GRAY_B
                          ).move_to(UP * 0.6)
        follow_text = Text("关注我，学更多数学知识！", font=FONT, font_size=30,
                           color=COLOR_HL).move_to(DOWN * 0.4)

        self.play(Transform(self.author, author_big), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(follow_text, shift=UP * 0.2, scale=1.05), run_time=0.6)

        # 旋转角装饰
        deco_vtx = np.array([0.0, -2.2, 0.0])
        deco_r1 = Line(deco_vtx, deco_vtx + 1.8 * RIGHT, color=COLOR_RAY, stroke_width=4)
        deco_tracker = ValueTracker(0)
        deco_r2 = always_redraw(
            lambda: Line(
                deco_vtx,
                deco_vtx + 1.8 * np.array([
                    np.cos(deco_tracker.get_value()),
                    np.sin(deco_tracker.get_value()),
                    0
                ]),
                color=COLOR_ANGLE, stroke_width=4
            )
        )
        deco_dot = Dot(deco_vtx, color=COLOR_VERTEX, radius=0.12)
        self.play(Create(deco_r1), FadeIn(deco_dot), run_time=0.4)
        self.add(deco_r2)
        self.play(deco_tracker.animate.set_value(np.radians(180)), run_time=1.5,
                  rate_func=smooth)
        self.play(deco_tracker.animate.set_value(np.radians(360)), run_time=1.5,
                  rate_func=smooth)

        self.wait(0.5)

        self.play(
            FadeOut(self.author), FadeOut(author_id), FadeOut(follow_text),
            FadeOut(deco_r1), FadeOut(deco_r2), FadeOut(deco_dot),
            run_time=1.0
        )


# ======================================================================
# 渲染命令:
#   manim -qm 002_角的认识与度量.py AngleMeasureLesson
# ======================================================================
