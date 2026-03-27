"""
003_锐角和钝角.py — 锐角和钝角 教学动画

知识点: 锐角比直角小，钝角比直角大。用三角尺的直角作为标准对角进行分类。
年级: 二年级上册
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

几何核心:
  直角: 90度角，两射线从顶点出发互相垂直
  锐角: 小于 90 度的角 (示例 45 度)
  钝角: 大于 90 度的角 (示例 120 度)
  角度比较: 锐角 < 直角 < 钝角
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
BG_COLOR = "#1a1a2e"
COLOR_RIGHT = "#22c55e"      # 绿色 - 直角
COLOR_ACUTE = "#3b82f6"      # 蓝色 - 锐角
COLOR_OBTUSE = "#ef4444"     # 红色 - 钝角
COLOR_RAY = "#e2e8f0"        # 浅灰 - 射线
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
COLOR_RULER = "#f59e0b"      # 橙色 - 三角尺
FONT = "Heiti SC"


# ======================================================================
# 主场景
# ======================================================================

class AcuteAndObtuseAngleLesson(Scene):
    """
    锐角和钝角教学动画
    场景顺序:
      1. 开场钩子
      2. 复习直角
      3. 认识锐角
      4. 认识钝角
      5. 三种角比较
      6. 用三角尺分类练习
      7. 公式总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_right_angle_review()
        self.scene_3_acute_angle()
        self.scene_4_obtuse_angle()
        self.scene_5_comparison()
        self.scene_6_ruler_classify()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标"""

        # ===== 射线公用长度 =====
        self.RAY_LEN = 2.8

        # ===== 直角 (90 度) =====
        self.right_vertex = np.array([0.0, 0.0, 0.0])
        self.right_angle_deg = 90.0
        self.right_ray1_end = self.right_vertex + self.RAY_LEN * np.array([1.0, 0.0, 0.0])
        self.right_ray2_end = self.right_vertex + self.RAY_LEN * np.array([0.0, 1.0, 0.0])

        # ===== 锐角 (45 度) =====
        self.acute_vertex = np.array([0.0, 0.0, 0.0])
        self.acute_angle_deg = 45.0
        self.acute_angle_rad = np.radians(self.acute_angle_deg)
        self.acute_ray1_end = self.acute_vertex + self.RAY_LEN * np.array([1.0, 0.0, 0.0])
        self.acute_ray2_end = self.acute_vertex + self.RAY_LEN * np.array([
            np.cos(self.acute_angle_rad),
            np.sin(self.acute_angle_rad),
            0.0
        ])

        # ===== 钝角 (120 度) =====
        self.obtuse_vertex = np.array([0.0, 0.0, 0.0])
        self.obtuse_angle_deg = 120.0
        self.obtuse_angle_rad = np.radians(self.obtuse_angle_deg)
        self.obtuse_ray1_end = self.obtuse_vertex + self.RAY_LEN * np.array([1.0, 0.0, 0.0])
        self.obtuse_ray2_end = self.obtuse_vertex + self.RAY_LEN * np.array([
            np.cos(self.obtuse_angle_rad),
            np.sin(self.obtuse_angle_rad),
            0.0
        ])

        # ===== 验证角度 =====
        self._verify_angles()

    def _verify_angles(self):
        """验证角度计算的正确性"""
        eps = 1e-6

        # 直角验证
        v1 = self.right_ray1_end - self.right_vertex
        v2 = self.right_ray2_end - self.right_vertex
        dot = np.dot(v1[:2], v2[:2])
        assert abs(dot) < eps, f"Right angle dot product should be 0, got {dot}"

        # 锐角验证
        v1 = self.acute_ray1_end - self.acute_vertex
        v2 = self.acute_ray2_end - self.acute_vertex
        cos_a = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        angle_check = np.degrees(np.arccos(np.clip(cos_a, -1, 1)))
        assert abs(angle_check - self.acute_angle_deg) < eps, \
            f"Acute angle should be {self.acute_angle_deg}, got {angle_check}"

        # 钝角验证
        v1 = self.obtuse_ray1_end - self.obtuse_vertex
        v2 = self.obtuse_ray2_end - self.obtuse_vertex
        cos_a = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        angle_check = np.degrees(np.arccos(np.clip(cos_a, -1, 1)))
        assert abs(angle_check - self.obtuse_angle_deg) < eps, \
            f"Obtuse angle should be {self.obtuse_angle_deg}, got {angle_check}"

        print("Geometry verification passed")

    # ------------------------------------------------------------------
    # Helper: 创建角的图形组
    # ------------------------------------------------------------------

    def _make_angle_group(self, vertex, ray1_end, ray2_end, angle_deg,
                          color, arc_radius=0.7, offset=ORIGIN,
                          show_elbow=False, label_text=None):
        """
        创建一个角的完整图形组: 两条射线 + 角弧 + 可选标签
        vertex, ray1_end, ray2_end 为局部坐标, offset 为场景位移
        """
        v = vertex + offset
        r1 = ray1_end + offset
        r2 = ray2_end + offset

        ray1 = Line(v, r1, color=COLOR_RAY, stroke_width=3)
        ray2 = Line(v, r2, color=COLOR_RAY, stroke_width=3)

        vertex_dot = Dot(v, radius=0.06, color=WHITE)

        if show_elbow:
            # 直角标记
            elbow_size = 0.35
            dir1 = (r1 - v) / np.linalg.norm(r1 - v) * elbow_size
            dir2 = (r2 - v) / np.linalg.norm(r2 - v) * elbow_size
            elbow = Polygon(
                v + dir1,
                v + dir1 + dir2,
                v + dir2,
                color=color,
                stroke_width=2.5,
                fill_opacity=0.0,
            )
            arc_mob = elbow
        else:
            # 角弧
            line1 = Line(v, r1)
            line2 = Line(v, r2)
            # 确定角弧方向
            vec1 = r1 - v
            vec2 = r2 - v
            cross_z = vec1[0] * vec2[1] - vec1[1] * vec2[0]
            arc_mob = Angle(
                line1, line2,
                radius=arc_radius,
                other_angle=(cross_z < 0),
                color=color,
                stroke_width=3,
            )

        parts = [ray1, ray2, vertex_dot, arc_mob]

        if label_text is not None:
            # 放在角弧中间位置
            angle_rad = np.radians(angle_deg)
            mid_angle = angle_rad / 2
            label_r = arc_radius + 0.35
            label_pos = v + label_r * np.array([np.cos(mid_angle), np.sin(mid_angle), 0])
            label = MathTex(label_text, font_size=26, color=color).move_to(label_pos)
            parts.append(label)

        group = VGroup(*parts)
        return group

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.author = author

        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "你能分辨这些角吗?",
            font=FONT, font_size=38, color=COLOR_HL
        ).move_to(UP * 5.5)

        self.play(Write(hook), run_time=0.8)

        # 展示三个不同大小的角 (小预览)
        preview_offset_y = UP * 2.0
        scale = 0.55

        # 锐角预览
        a_v = np.array([0, 0, 0])
        a_r1 = a_v + 2.0 * np.array([1, 0, 0])
        a_r2 = a_v + 2.0 * np.array([np.cos(np.radians(45)), np.sin(np.radians(45)), 0])
        acute_preview = self._make_angle_group(
            a_v, a_r1, a_r2, 45, COLOR_ACUTE, arc_radius=0.5
        ).scale(scale).move_to(LEFT * 3.0 + preview_offset_y)

        # 直角预览
        r_v = np.array([0, 0, 0])
        r_r1 = r_v + 2.0 * RIGHT
        r_r2 = r_v + 2.0 * UP
        right_preview = self._make_angle_group(
            r_v, r_r1, r_r2, 90, COLOR_RIGHT, show_elbow=True
        ).scale(scale).move_to(preview_offset_y)

        # 钝角预览
        o_v = np.array([0, 0, 0])
        o_r1 = o_v + 2.0 * np.array([1, 0, 0])
        o_r2 = o_v + 2.0 * np.array([np.cos(np.radians(120)), np.sin(np.radians(120)), 0])
        obtuse_preview = self._make_angle_group(
            o_v, o_r1, o_r2, 120, COLOR_OBTUSE, arc_radius=0.5
        ).scale(scale).move_to(RIGHT * 3.0 + preview_offset_y)

        q_acute = Text("?", font=FONT, font_size=30, color=COLOR_ACUTE).next_to(acute_preview, DOWN, buff=0.4)
        q_right = Text("?", font=FONT, font_size=30, color=COLOR_RIGHT).next_to(right_preview, DOWN, buff=0.4)
        q_obtuse = Text("?", font=FONT, font_size=30, color=COLOR_OBTUSE).next_to(obtuse_preview, DOWN, buff=0.4)

        self.play(
            FadeIn(acute_preview, scale=0.8),
            FadeIn(right_preview, scale=0.8),
            FadeIn(obtuse_preview, scale=0.8),
            run_time=1.0
        )
        self.play(FadeIn(q_acute), FadeIn(q_right), FadeIn(q_obtuse), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(hook), FadeOut(acute_preview), FadeOut(right_preview),
            FadeOut(obtuse_preview), FadeOut(q_acute), FadeOut(q_right), FadeOut(q_obtuse),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 2: 复习直角
    # ------------------------------------------------------------------

    def scene_2_right_angle_review(self):
        title = Text("复习: 直角", font=FONT, font_size=34, color=COLOR_RIGHT).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        offset = UP * 1.5
        angle_group = self._make_angle_group(
            self.right_vertex, self.right_ray1_end, self.right_ray2_end,
            90, COLOR_RIGHT, show_elbow=True, offset=offset
        )

        self.play(Create(angle_group), run_time=1.0)

        # 标注 90 度
        label_90 = MathTex(r"90^\circ", font_size=32, color=COLOR_RIGHT).move_to(
            self.right_vertex + offset + np.array([0.7, 0.7, 0])
        )
        self.play(Write(label_90), run_time=0.5)

        # 说明文字
        desc = Text(
            "直角 = 90度",
            font=FONT, font_size=28, color=WHITE
        ).move_to(DOWN * 2.0)

        desc2 = Text(
            "三角尺上有一个直角",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 3.0)

        self.play(FadeIn(desc), run_time=0.5)
        self.play(FadeIn(desc2), run_time=0.5)
        self.wait(1.5)

        # 画三角尺简图
        ruler_v = np.array([-1.0, -5.0, 0.0])
        ruler_pts = [
            ruler_v,
            ruler_v + np.array([3.0, 0.0, 0.0]),
            ruler_v + np.array([0.0, 2.5, 0.0]),
        ]
        ruler = Polygon(
            *ruler_pts,
            color=COLOR_RULER, fill_opacity=0.15, stroke_width=2.5
        )
        # 直角标记在 ruler_v
        rb_size = 0.3
        ruler_elbow = Polygon(
            ruler_v + rb_size * RIGHT,
            ruler_v + rb_size * RIGHT + rb_size * UP,
            ruler_v + rb_size * UP,
            color=COLOR_RIGHT, stroke_width=2, fill_opacity=0
        )
        ruler_label = Text("三角尺", font=FONT, font_size=20, color=COLOR_RULER).next_to(ruler, DOWN, buff=0.3)

        self.play(Create(ruler), FadeIn(ruler_elbow), FadeIn(ruler_label), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(angle_group), FadeOut(label_90),
            FadeOut(desc), FadeOut(desc2),
            FadeOut(ruler), FadeOut(ruler_elbow), FadeOut(ruler_label),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 3: 认识锐角
    # ------------------------------------------------------------------

    def scene_3_acute_angle(self):
        title = Text("锐角", font=FONT, font_size=38, color=COLOR_ACUTE).move_to(UP * 5.5)
        subtitle = Text(
            "比直角小的角",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 4.7)

        self.play(Write(title), FadeIn(subtitle), run_time=0.7)

        offset = UP * 1.5

        # 先画直角 (虚线参考)
        ref_ray1 = DashedLine(
            self.acute_vertex + offset,
            self.acute_vertex + offset + self.RAY_LEN * RIGHT,
            color=GRAY_B, dash_length=0.12, stroke_width=2
        )
        ref_ray2 = DashedLine(
            self.acute_vertex + offset,
            self.acute_vertex + offset + self.RAY_LEN * UP,
            color=GRAY_B, dash_length=0.12, stroke_width=2
        )
        ref_label = MathTex(r"90^\circ", font_size=22, color=GRAY_B).move_to(
            self.acute_vertex + offset + np.array([0.6, 0.6, 0])
        )

        self.play(Create(ref_ray1), Create(ref_ray2), FadeIn(ref_label), run_time=0.5)

        # 画锐角
        angle_group = self._make_angle_group(
            self.acute_vertex, self.acute_ray1_end, self.acute_ray2_end,
            self.acute_angle_deg, COLOR_ACUTE, arc_radius=0.65,
            offset=offset, label_text=r"45^\circ"
        )

        self.play(Create(angle_group), run_time=1.0)

        # 指示: 比直角小
        arrow_note = Text(
            "角的开口比直角小",
            font=FONT, font_size=24, color=COLOR_ACUTE
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(arrow_note, shift=UP * 0.2), run_time=0.5)

        # 公式
        formula_parts = VGroup(
            Text("锐角", font=FONT, font_size=28, color=COLOR_ACUTE),
            MathTex(r"< 90^\circ", font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.0)

        self.play(Write(formula_parts), run_time=0.6)

        # 再展示一个锐角 60 度
        acute2_angle_rad = np.radians(60)
        a2_ray2 = self.acute_vertex + self.RAY_LEN * np.array([
            np.cos(acute2_angle_rad), np.sin(acute2_angle_rad), 0
        ])
        angle_group2 = self._make_angle_group(
            self.acute_vertex, self.acute_ray1_end, a2_ray2,
            60, COLOR_ACUTE, arc_radius=0.65,
            offset=DOWN * 5.0 + LEFT * 0.5,
            label_text=r"60^\circ"
        )

        also_text = Text(
            "60度也是锐角", font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 5.0 + RIGHT * 2.5)

        self.play(Create(angle_group2), FadeIn(also_text), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(ref_ray1), FadeOut(ref_ray2),
            FadeOut(ref_label), FadeOut(angle_group), FadeOut(arrow_note),
            FadeOut(formula_parts), FadeOut(angle_group2), FadeOut(also_text),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 4: 认识钝角
    # ------------------------------------------------------------------

    def scene_4_obtuse_angle(self):
        title = Text("钝角", font=FONT, font_size=38, color=COLOR_OBTUSE).move_to(UP * 5.5)
        subtitle = Text(
            "比直角大的角",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 4.7)

        self.play(Write(title), FadeIn(subtitle), run_time=0.7)

        offset = UP * 1.5

        # 直角参考 (虚线)
        ref_ray1 = DashedLine(
            self.obtuse_vertex + offset,
            self.obtuse_vertex + offset + self.RAY_LEN * RIGHT,
            color=GRAY_B, dash_length=0.12, stroke_width=2
        )
        ref_ray2 = DashedLine(
            self.obtuse_vertex + offset,
            self.obtuse_vertex + offset + self.RAY_LEN * UP,
            color=GRAY_B, dash_length=0.12, stroke_width=2
        )
        ref_label = MathTex(r"90^\circ", font_size=22, color=GRAY_B).move_to(
            self.obtuse_vertex + offset + np.array([0.6, 0.6, 0])
        )

        self.play(Create(ref_ray1), Create(ref_ray2), FadeIn(ref_label), run_time=0.5)

        # 画钝角
        angle_group = self._make_angle_group(
            self.obtuse_vertex, self.obtuse_ray1_end, self.obtuse_ray2_end,
            self.obtuse_angle_deg, COLOR_OBTUSE, arc_radius=0.65,
            offset=offset, label_text=r"120^\circ"
        )

        self.play(Create(angle_group), run_time=1.0)

        # 指示
        arrow_note = Text(
            "角的开口比直角大",
            font=FONT, font_size=24, color=COLOR_OBTUSE
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(arrow_note, shift=UP * 0.2), run_time=0.5)

        # 公式
        formula_parts = VGroup(
            Text("钝角", font=FONT, font_size=28, color=COLOR_OBTUSE),
            MathTex(r"> 90^\circ", font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.0)

        self.play(Write(formula_parts), run_time=0.6)

        # 另一个钝角 150 度
        obtuse2_angle_rad = np.radians(150)
        o2_ray2 = self.obtuse_vertex + self.RAY_LEN * np.array([
            np.cos(obtuse2_angle_rad), np.sin(obtuse2_angle_rad), 0
        ])
        angle_group2 = self._make_angle_group(
            self.obtuse_vertex, self.obtuse_ray1_end, o2_ray2,
            150, COLOR_OBTUSE, arc_radius=0.65,
            offset=DOWN * 5.0 + LEFT * 0.5,
            label_text=r"150^\circ"
        )

        also_text = Text(
            "150度也是钝角", font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 5.0 + RIGHT * 2.5)

        self.play(Create(angle_group2), FadeIn(also_text), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(ref_ray1), FadeOut(ref_ray2),
            FadeOut(ref_label), FadeOut(angle_group), FadeOut(arrow_note),
            FadeOut(formula_parts), FadeOut(angle_group2), FadeOut(also_text),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 5: 三种角的比较
    # ------------------------------------------------------------------

    def scene_5_comparison(self):
        title = Text("三种角的比较", font=FONT, font_size=34, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 三个角并排
        scale = 0.48

        # 锐角
        a_v = np.array([0, 0, 0])
        a_r1 = a_v + 2.5 * RIGHT
        a_r2 = a_v + 2.5 * np.array([np.cos(np.radians(45)), np.sin(np.radians(45)), 0])
        acute_g = self._make_angle_group(
            a_v, a_r1, a_r2, 45, COLOR_ACUTE, arc_radius=0.6,
            label_text=r"45^\circ"
        ).scale(scale).move_to(LEFT * 2.8 + UP * 3.0)
        acute_name = Text("锐角", font=FONT, font_size=24, color=COLOR_ACUTE).next_to(acute_g, DOWN, buff=0.5)

        # 直角
        r_v = np.array([0, 0, 0])
        r_r1 = r_v + 2.5 * RIGHT
        r_r2 = r_v + 2.5 * UP
        right_g = self._make_angle_group(
            r_v, r_r1, r_r2, 90, COLOR_RIGHT, show_elbow=True
        ).scale(scale).move_to(UP * 3.0)
        right_name = Text("直角", font=FONT, font_size=24, color=COLOR_RIGHT).next_to(right_g, DOWN, buff=0.5)

        # 钝角
        o_v = np.array([0, 0, 0])
        o_r1 = o_v + 2.5 * RIGHT
        o_r2 = o_v + 2.5 * np.array([np.cos(np.radians(120)), np.sin(np.radians(120)), 0])
        obtuse_g = self._make_angle_group(
            o_v, o_r1, o_r2, 120, COLOR_OBTUSE, arc_radius=0.6,
            label_text=r"120^\circ"
        ).scale(scale).move_to(RIGHT * 2.8 + UP * 3.0)
        obtuse_name = Text("钝角", font=FONT, font_size=24, color=COLOR_OBTUSE).next_to(obtuse_g, DOWN, buff=0.5)

        self.play(
            FadeIn(acute_g), FadeIn(right_g), FadeIn(obtuse_g),
            run_time=0.8
        )
        self.play(
            FadeIn(acute_name), FadeIn(right_name), FadeIn(obtuse_name),
            run_time=0.5
        )

        # 不等式链
        ineq = VGroup(
            Text("锐角", font=FONT, font_size=28, color=COLOR_ACUTE),
            MathTex(r"<", font_size=32, color=WHITE),
            Text("直角", font=FONT, font_size=28, color=COLOR_RIGHT),
            MathTex(r"<", font_size=32, color=WHITE),
            Text("钝角", font=FONT, font_size=28, color=COLOR_OBTUSE),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 0.5)

        self.play(Write(ineq), run_time=1.0)

        # 数字版
        ineq2 = VGroup(
            MathTex(r"0^\circ", font_size=28, color=COLOR_ACUTE),
            MathTex(r"<", font_size=28, color=WHITE),
            Text("锐角", font=FONT, font_size=24, color=COLOR_ACUTE),
            MathTex(r"< 90^\circ <", font_size=28, color=WHITE),
            Text("钝角", font=FONT, font_size=24, color=COLOR_OBTUSE),
            MathTex(r"< 180^\circ", font_size=28, color=COLOR_OBTUSE),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.0)

        self.play(FadeIn(ineq2, shift=UP * 0.2), run_time=0.8)

        # 记忆口诀
        tip = Text(
            "口诀: 锐角尖尖小, 钝角胖胖大",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 4.0)

        self.play(FadeIn(tip), run_time=0.5)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(acute_g), FadeOut(right_g), FadeOut(obtuse_g),
            FadeOut(acute_name), FadeOut(right_name), FadeOut(obtuse_name),
            FadeOut(ineq), FadeOut(ineq2), FadeOut(tip),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 6: 用三角尺分类
    # ------------------------------------------------------------------

    def scene_6_ruler_classify(self):
        title = Text(
            "动手试一试", font=FONT, font_size=34, color=COLOR_HL
        ).move_to(UP * 5.5)

        subtitle = Text(
            "用三角尺的直角来比一比",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.7)

        self.play(Write(title), FadeIn(subtitle), run_time=0.7)

        # 创建三角尺 (简化)
        ruler_center = UP * 1.5 + LEFT * 2.5
        ruler_scale = 0.9
        ruler_pts = [
            ruler_center,
            ruler_center + ruler_scale * 2.5 * RIGHT,
            ruler_center + ruler_scale * 2.0 * UP,
        ]
        ruler = Polygon(
            *ruler_pts,
            color=COLOR_RULER, fill_opacity=0.12, stroke_width=2.5
        )
        rb_size = 0.3 * ruler_scale
        ruler_elbow = Polygon(
            ruler_center + rb_size * RIGHT,
            ruler_center + rb_size * RIGHT + rb_size * UP,
            ruler_center + rb_size * UP,
            color=COLOR_RIGHT, stroke_width=2, fill_opacity=0
        )
        ruler_group = VGroup(ruler, ruler_elbow)

        self.play(FadeIn(ruler_group), run_time=0.5)

        # 测试角1: 锐角 50度
        test1_center = UP * 1.5 + RIGHT * 1.5
        t1_rad = np.radians(50)
        t1_r1 = test1_center + 1.8 * RIGHT
        t1_r2 = test1_center + 1.8 * np.array([np.cos(t1_rad), np.sin(t1_rad), 0])
        test1 = self._make_angle_group(
            np.array([0, 0, 0]),
            1.8 * RIGHT,
            1.8 * np.array([np.cos(t1_rad), np.sin(t1_rad), 0]),
            50, COLOR_ACUTE, arc_radius=0.5,
            offset=test1_center,
        )

        self.play(Create(test1), run_time=0.8)

        # 移动三角尺对比
        self.play(
            ruler_group.animate.move_to(test1_center + LEFT * 0.3 + DOWN * 0.15),
            run_time=0.8
        )

        result1 = Text(
            "比直角小 -> 锐角!",
            font=FONT, font_size=24, color=COLOR_ACUTE
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(result1), run_time=0.5)
        self.wait(1.0)

        # 清理第一轮
        self.play(FadeOut(test1), FadeOut(result1), run_time=0.4)

        # 测试角2: 钝角 130度
        test2_center = UP * 1.5 + RIGHT * 1.0
        t2_rad = np.radians(130)
        test2 = self._make_angle_group(
            np.array([0, 0, 0]),
            1.8 * RIGHT,
            1.8 * np.array([np.cos(t2_rad), np.sin(t2_rad), 0]),
            130, COLOR_OBTUSE, arc_radius=0.5,
            offset=test2_center,
        )

        self.play(Create(test2), run_time=0.8)

        # 移动三角尺对比
        self.play(
            ruler_group.animate.move_to(test2_center + LEFT * 0.3 + DOWN * 0.15),
            run_time=0.8
        )

        result2 = Text(
            "比直角大 -> 钝角!",
            font=FONT, font_size=24, color=COLOR_OBTUSE
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(result2), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(ruler_group),
            FadeOut(test2), FadeOut(result2),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 7: 总结
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        title = Text(
            "总结", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 三个卡片
        card_y_start = UP * 3.5
        card_spacing = 2.8

        # 锐角卡片
        acute_card = self._make_summary_card(
            "锐角", r"< 90^\circ", COLOR_ACUTE,
            "比直角小的角", 45
        ).move_to(card_y_start)

        # 直角卡片
        right_card = self._make_summary_card(
            "直角", r"= 90^\circ", COLOR_RIGHT,
            "标准角", 90, is_right=True
        ).move_to(card_y_start + DOWN * card_spacing)

        # 钝角卡片
        obtuse_card = self._make_summary_card(
            "钝角", r"> 90^\circ", COLOR_OBTUSE,
            "比直角大的角", 120
        ).move_to(card_y_start + DOWN * card_spacing * 2)

        self.play(FadeIn(acute_card, shift=RIGHT * 0.5), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(right_card, shift=RIGHT * 0.5), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(obtuse_card, shift=RIGHT * 0.5), run_time=0.6)

        # 核心不等式
        core = VGroup(
            Text("锐角", font=FONT, font_size=30, color=COLOR_ACUTE),
            MathTex(r"<", font_size=34, color=WHITE),
            Text("直角", font=FONT, font_size=30, color=COLOR_RIGHT),
            MathTex(r"<", font_size=34, color=WHITE),
            Text("钝角", font=FONT, font_size=30, color=COLOR_OBTUSE),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 4.5)

        box = SurroundingRectangle(core, color=COLOR_HL, buff=0.3, corner_radius=0.15, stroke_width=2)

        self.play(Write(core), Create(box), run_time=0.8)

        tip = Text(
            "用三角尺比一比就知道了!",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 6.0)
        self.play(FadeIn(tip), run_time=0.4)

        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(acute_card), FadeOut(right_card),
            FadeOut(obtuse_card), FadeOut(core), FadeOut(box), FadeOut(tip),
            run_time=0.6
        )

    def _make_summary_card(self, name, formula_str, color, desc, angle_deg, is_right=False):
        """创建总结卡片: 小角图 + 名称 + 公式 + 描述"""
        # 小角图
        scale = 0.3
        v = np.array([0, 0, 0])
        r1 = v + 2.0 * RIGHT
        angle_rad = np.radians(angle_deg)
        r2 = v + 2.0 * np.array([np.cos(angle_rad), np.sin(angle_rad), 0])
        angle_icon = self._make_angle_group(
            v, r1, r2, angle_deg, color,
            arc_radius=0.6, show_elbow=is_right
        ).scale(scale)

        name_text = Text(name, font=FONT, font_size=28, color=color)
        formula = MathTex(formula_str, font_size=26, color=WHITE)
        desc_text = Text(desc, font=FONT, font_size=20, color=GRAY_A)

        row1 = VGroup(angle_icon, name_text, formula).arrange(RIGHT, buff=0.4)
        card = VGroup(row1, desc_text).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        bg = RoundedRectangle(
            width=card.width + 0.8,
            height=card.height + 0.5,
            corner_radius=0.15,
            color=color,
            fill_opacity=0.08,
            stroke_width=1.5,
        ).move_to(card.get_center())

        return VGroup(bg, card)

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=36, color=WHITE
        ).move_to(UP * 1.0)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B
        ).move_to(UP * 0.0)

        self.play(
            Transform(self.author, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 获得更多数学技巧!",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.6)

        # 三个小角装饰
        deco_angles = VGroup()
        for i, (deg, clr) in enumerate([(45, COLOR_ACUTE), (90, COLOR_RIGHT), (120, COLOR_OBTUSE)]):
            v = np.array([0, 0, 0])
            r1 = v + 1.5 * RIGHT
            rad = np.radians(deg)
            r2 = v + 1.5 * np.array([np.cos(rad), np.sin(rad), 0])
            g = self._make_angle_group(
                v, r1, r2, deg, clr, arc_radius=0.4, show_elbow=(deg == 90)
            ).scale(0.3).move_to(DOWN * 3.5 + (i - 1) * RIGHT * 2.5)
            deco_angles.add(g)

        self.play(*[FadeIn(d, scale=0.5) for d in deco_angles], run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco_angles),
            run_time=1.0
        )
