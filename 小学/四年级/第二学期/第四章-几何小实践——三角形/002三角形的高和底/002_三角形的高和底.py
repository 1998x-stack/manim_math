"""
002_三角形的高和底.py — 三角形的高和底 教学动画

知识点: 三角形的高和底
  - 从三角形的一个顶点到它的对边作一条垂线
  - 顶点和垂足之间的线段叫做三角形的高
  - 这条对边叫做三角形的底
  - 每个三角形有三条高
  - 钝角三角形的钝角边上的高在形外（需延长底边）
年级: 四年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR      = "#1a1a2e"
COLOR_TRI     = "#3b82f6"   # 蓝色  三角形主体
COLOR_HEIGHT  = "#f59e0b"   # 橙色  高线
COLOR_BASE    = "#22c55e"   # 绿色  底边
COLOR_RA      = "#f472b6"   # 粉色  直角标记
COLOR_FOOT    = "#fb923c"   # 橙红  垂足
COLOR_HL      = "#fbbf24"   # 黄色  高亮
COLOR_AUTHOR  = "#6b7280"   # 灰色  作者信息
COLOR_DASH    = "#a78bfa"   # 紫色  辅助虚线
COLOR_OBTUSE  = "#ef4444"   # 红色  钝角三角形
FONT          = "PingFang SC"


def foot_of_perpendicular(point, line_start, line_end):
    """计算点到直线的垂足（精确公式）"""
    line_vec  = line_end - line_start
    point_vec = point - line_start
    t = np.dot(point_vec, line_vec) / np.dot(line_vec, line_vec)
    return line_start + t * line_vec


def make_right_angle_mark(corner, p1, p2, size=0.18, color=COLOR_RA):
    """在 corner 处创建直角小方块标记（p1、p2 是两条边上的方向点）"""
    v1 = (p1 - corner)
    v1 = v1 / np.linalg.norm(v1) * size
    v2 = (p2 - corner)
    v2 = v2 / np.linalg.norm(v2) * size
    return Polygon(
        corner,
        corner + v1,
        corner + v1 + v2,
        corner + v2,
        color=color,
        stroke_width=2,
        fill_opacity=0,
    )


# ======================================================================
# 主场景
# ======================================================================

class TriangleHeightBaseLesson(Scene):
    """
    三角形的高和底教学动画
    场景顺序:
      1. 开场钩子
      2. 高和底的定义（以锐角三角形 BC 边为底为例）
      3. 动态演示作高的步骤
      4. 三角形有三条高（锐角三角形）
      5. 钝角三角形的高（高在形外，需延长底边）
      6. 知识总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_draw_height_step_by_step()
        self.scene_4_three_heights()
        self.scene_5_obtuse_triangle()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标（精确计算，无臆想坐标）"""

        # ===== 主三角形（锐角三角形）顶点 =====
        # 放置在屏幕中部，设计为一个清晰的锐角三角形
        self.OFFSET = np.array([0.0, 0.8, 0.0])

        raw_A = np.array([-2.2, -1.4, 0.0])
        raw_B = np.array([ 2.0, -1.4, 0.0])
        raw_C = np.array([-0.4,  1.8, 0.0])

        self.A = raw_A + self.OFFSET
        self.B = raw_B + self.OFFSET
        self.C = raw_C + self.OFFSET

        # ===== 三条高的垂足（精确计算）=====
        # 高1: 从 C 到 AB 边的垂足 D
        self.D = foot_of_perpendicular(self.C, self.A, self.B)
        # 高2: 从 A 到 BC 边的垂足 E
        self.E = foot_of_perpendicular(self.A, self.B, self.C)
        # 高3: 从 B 到 CA 边的垂足 F
        self.F = foot_of_perpendicular(self.B, self.C, self.A)

        # ===== 验证锐角三角形（所有垂足都在边内部）=====
        self._verify_acute_triangle()

        # ===== 钝角三角形顶点 =====
        # 设计一个明显的钝角三角形，放置在较低位置
        self.OFFSET_OB = np.array([0.0, 0.5, 0.0])

        raw_P = np.array([-3.0, -1.2, 0.0])
        raw_Q = np.array([ 2.8, -1.2, 0.0])
        raw_R = np.array([-1.6,  1.5, 0.0])   # R 在 P 附近，使 ∠P 为钝角

        self.P = raw_P + self.OFFSET_OB
        self.Q = raw_Q + self.OFFSET_OB
        self.R = raw_R + self.OFFSET_OB

        # 钝角三角形：以 PQ 为底，从 R 作高，垂足 S 在 PQ 延长线上吗？
        # 检验角 P 是否为钝角
        angle_P = self._calc_angle(self.Q, self.P, self.R)

        # 垂足 S：从 R 到直线 PQ 的垂足
        self.S = foot_of_perpendicular(self.R, self.P, self.Q)

        # 如果 S 在 PQ 线段内，说明不是底边延长线上的高，需要调整
        # 对钝角三角形，我们展示从 Q 顶点到 PR 延长线的高
        # 垂足 T：从 Q 到直线 PR 的垂足（可能在 PR 延长线外）
        self.T = foot_of_perpendicular(self.Q, self.P, self.R)

        # 验证 T 是否在 PR 线段外（即需要延长 PR）
        PR_vec   = self.R - self.P
        PT_vec   = self.T - self.P
        t_param  = np.dot(PT_vec, PR_vec) / np.dot(PR_vec, PR_vec)
        self.T_outside = (t_param > 1.0 + 1e-6)  # T 在 R 之外

        if not self.T_outside:
            # 重新选定：确保钝角在 P，高从 Q 往 PR 方向的垂足在延长线外
            # 用 R 顶点作 PQ 边上的高，确保 S 在 PQ 之外
            # 重新设置让 ∠P 明显钝角
            raw_R2 = np.array([-2.2,  1.5, 0.0])
            self.R = raw_R2 + self.OFFSET_OB
            self.S = foot_of_perpendicular(self.R, self.P, self.Q)
            self.T = foot_of_perpendicular(self.Q, self.P, self.R)
            PT_vec = self.T - self.P
            t_param = np.dot(PT_vec, PR_vec) / np.dot(PR_vec, PR_vec)
            self.T_outside = (t_param > 1.0 + 1e-6)

        print(f"Geometry setup: T_outside={self.T_outside}, t_param={t_param:.3f}")
        print("Geometry setup complete.")

    def _calc_angle(self, p1, vertex, p2):
        """计算以 vertex 为顶点，p1-vertex-p2 的内角（弧度）"""
        v1 = p1 - vertex
        v2 = p2 - vertex
        cos_a = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_a = np.clip(cos_a, -1.0, 1.0)
        return np.arccos(cos_a)

    def _verify_acute_triangle(self):
        """验证主三角形是锐角三角形（所有垂足在边内）"""
        # 从 C 到 AB：t ∈ (0,1)
        AB_vec = self.B - self.A
        AD_vec = self.D - self.A
        t_D = np.dot(AD_vec, AB_vec) / np.dot(AB_vec, AB_vec)
        assert 0 < t_D < 1, f"垂足 D 不在 AB 内部: t={t_D:.3f}"

        BC_vec = self.C - self.B
        BE_vec = self.E - self.B
        t_E = np.dot(BE_vec, BC_vec) / np.dot(BC_vec, BC_vec)
        assert 0 < t_E < 1, f"垂足 E 不在 BC 内部: t={t_E:.3f}"

        CA_vec = self.A - self.C
        CF_vec = self.F - self.C
        t_F = np.dot(CF_vec, CA_vec) / np.dot(CA_vec, CA_vec)
        assert 0 < t_F < 1, f"垂足 F 不在 CA 内部: t={t_F:.3f}"

        print("Acute triangle verification passed.")

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_triangle(self, A, B, C, color=COLOR_TRI, stroke_width=4, fill_opacity=0.08):
        return Polygon(
            A, B, C,
            color=color,
            stroke_width=stroke_width,
            fill_color=color,
            fill_opacity=fill_opacity,
        )

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "你知道三角形的高怎么画吗?",
            font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(UP * 5.2)

        sub = Text(
            "今天学习三角形的高和底!",
            font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 4.3)

        self.play(Write(hook), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 预览三角形
        tri_preview = self.make_triangle(
            self.A, self.B, self.C,
            color=COLOR_TRI, stroke_width=5, fill_opacity=0.12,
        )
        self.play(Create(tri_preview), run_time=1.0)
        self.wait(0.6)

        # 预览一条高（从 C 到 AB）
        height_preview = DashedLine(
            self.C, self.D,
            color=COLOR_HEIGHT, stroke_width=3, dash_length=0.15,
        )
        self.play(Create(height_preview), run_time=0.8)
        self.wait(0.5)

        self.play(
            FadeOut(hook), FadeOut(sub),
            FadeOut(tri_preview), FadeOut(height_preview),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 高和底的定义
    # ------------------------------------------------------------------

    def scene_2_definition(self):
        title = Text(
            "什么是三角形的高和底?",
            font=FONT, font_size=32, color=COLOR_HL,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 画三角形（以 AB 为底边示例）
        tri = self.make_triangle(self.A, self.B, self.C)
        self.play(Create(tri), run_time=1.0)

        # 顶点标签
        lbl_A = Text("A", font=FONT, font_size=26, color=WHITE).next_to(self.A, DL, buff=0.15)
        lbl_B = Text("B", font=FONT, font_size=26, color=WHITE).next_to(self.B, DR, buff=0.15)
        lbl_C = Text("C", font=FONT, font_size=26, color=WHITE).next_to(self.C, UP, buff=0.15)
        self.play(FadeIn(lbl_A), FadeIn(lbl_B), FadeIn(lbl_C), run_time=0.5)

        self.wait(0.4)

        # 高亮底边 AB
        base_line = Line(self.A, self.B, color=COLOR_BASE, stroke_width=6)
        self.play(Create(base_line), run_time=0.6)

        base_label = Text(
            "底边 AB",
            font=FONT, font_size=24, color=COLOR_BASE,
        ).move_to((self.A + self.B) / 2 + DOWN * 0.45)
        self.play(FadeIn(base_label), run_time=0.4)

        hint_base = Text(
            "与高对应的那条边叫做底",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(hint_base), run_time=0.4)
        self.wait(0.6)

        # 画高线：从 C 到 AB 的垂线
        height_line = Line(self.C, self.D, color=COLOR_HEIGHT, stroke_width=5)
        self.play(Create(height_line), run_time=0.8)

        # 垂足点
        foot_dot = Dot(self.D, color=COLOR_FOOT, radius=0.1)
        self.play(FadeIn(foot_dot), run_time=0.3)

        foot_label = Text("D（垂足）", font=FONT, font_size=20, color=COLOR_FOOT)
        foot_label.next_to(self.D, DOWN, buff=0.2)
        self.play(FadeIn(foot_label), run_time=0.4)

        # 直角标记
        ra_mark = make_right_angle_mark(self.D, self.C, self.B, size=0.2, color=COLOR_RA)
        self.play(Create(ra_mark), run_time=0.4)

        # 高线标签
        height_mid = (self.C + self.D) / 2
        height_label = Text("高 CD", font=FONT, font_size=24, color=COLOR_HEIGHT)
        height_label.move_to(height_mid + LEFT * 0.8)
        self.play(FadeIn(height_label), run_time=0.4)

        self.play(FadeOut(hint_base), run_time=0.3)

        # 文字定义（分两行）
        def_line1 = Text(
            "从顶点 C 到对边 AB 的垂线段 CD",
            font=FONT, font_size=21, color=WHITE,
        )
        def_line2 = Text(
            "叫做三角形的高，AB 叫做底",
            font=FONT, font_size=21, color=COLOR_HEIGHT,
        )
        def_group = VGroup(def_line1, def_line2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        def_group.move_to(DOWN * 4.2)
        self.play(FadeIn(def_line1, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(def_line2, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(2.5)

        # 保存供下一场景用
        self._tri_main   = tri
        self._lbl_A      = lbl_A
        self._lbl_B      = lbl_B
        self._lbl_C      = lbl_C

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(base_line), FadeOut(base_label),
            FadeOut(height_line), FadeOut(height_label),
            FadeOut(foot_dot), FadeOut(foot_label),
            FadeOut(ra_mark), FadeOut(def_group),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 3: 逐步演示如何作高
    # ------------------------------------------------------------------

    def scene_3_draw_height_step_by_step(self):
        title = Text(
            "如何画三角形的高?",
            font=FONT, font_size=34, color=COLOR_HL,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 使用已有三角形
        tri = self._tri_main
        lbl_A, lbl_B, lbl_C = self._lbl_A, self._lbl_B, self._lbl_C

        # 步骤指示器
        step_bg = RoundedRectangle(
            width=7.5, height=1.0,
            corner_radius=0.25,
            fill_color="#16213e",
            fill_opacity=0.85,
            stroke_color=COLOR_TRI,
            stroke_width=1.5,
        ).move_to(DOWN * 3.6)

        step_text = Text(
            "第一步：确定底边",
            font=FONT, font_size=24, color=WHITE,
        ).move_to(step_bg.get_center())

        self.play(FadeIn(step_bg), Write(step_text), run_time=0.5)

        # 高亮底边 AB
        base_hl = Line(self.A, self.B, color=COLOR_BASE, stroke_width=7)
        self.play(Create(base_hl), run_time=0.6)
        base_tag = Text("底边 AB", font=FONT, font_size=22, color=COLOR_BASE)
        base_tag.move_to((self.A + self.B) / 2 + DOWN * 0.45)
        self.play(FadeIn(base_tag), run_time=0.4)
        self.wait(0.7)

        # 步骤二
        step_text2 = Text(
            "第二步：从对面顶点 C 向底边引垂线",
            font=FONT, font_size=21, color=WHITE,
        ).move_to(step_bg.get_center())
        self.play(ReplacementTransform(step_text, step_text2), run_time=0.4)

        # 高亮顶点 C
        ring_C = Circle(radius=0.22, color=COLOR_HEIGHT, stroke_width=3).move_to(self.C)
        self.play(Create(ring_C), run_time=0.4)
        self.wait(0.4)

        # 画垂线（动态创建）
        perp_line = Line(self.C, self.D, color=COLOR_HEIGHT, stroke_width=5)
        self.play(Create(perp_line), run_time=0.8)
        self.play(FadeOut(ring_C), run_time=0.3)

        # 步骤三
        step_text3 = Text(
            "第三步：标记垂足和直角",
            font=FONT, font_size=24, color=WHITE,
        ).move_to(step_bg.get_center())
        self.play(ReplacementTransform(step_text2, step_text3), run_time=0.4)

        foot_dot = Dot(self.D, color=COLOR_FOOT, radius=0.1)
        ra_mark  = make_right_angle_mark(self.D, self.C, self.B, size=0.2, color=COLOR_RA)
        self.play(FadeIn(foot_dot), Create(ra_mark), run_time=0.5)

        foot_lbl = Text("D", font=FONT, font_size=22, color=COLOR_FOOT).next_to(self.D, DOWN, buff=0.18)
        self.play(FadeIn(foot_lbl), run_time=0.3)
        self.wait(0.6)

        # 步骤四
        step_text4 = Text(
            "第四步：标注高 CD",
            font=FONT, font_size=24, color=WHITE,
        ).move_to(step_bg.get_center())
        self.play(ReplacementTransform(step_text3, step_text4), run_time=0.4)

        height_lbl = Text("高 CD", font=FONT, font_size=24, color=COLOR_HEIGHT)
        height_lbl.move_to((self.C + self.D) / 2 + LEFT * 0.85)
        self.play(FadeIn(height_lbl), run_time=0.4)

        # 关键要点：高 ⊥ 底
        key_box = RoundedRectangle(
            width=6.5, height=1.0,
            corner_radius=0.25,
            fill_color="#0f3460",
            fill_opacity=0.9,
            stroke_color=COLOR_HL,
            stroke_width=2,
        ).move_to(DOWN * 5.0)

        key_row = VGroup(
            Text("关键：高", font=FONT, font_size=24, color=WHITE),
            MathTex(r"\perp", font_size=32, color=COLOR_HL),
            Text("底（互相垂直）", font=FONT, font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(key_box.get_center())

        self.play(FadeIn(key_box), FadeIn(key_row), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(step_bg), FadeOut(step_text4),
            FadeOut(base_hl), FadeOut(base_tag),
            FadeOut(perp_line), FadeOut(foot_dot), FadeOut(foot_lbl),
            FadeOut(ra_mark), FadeOut(height_lbl),
            FadeOut(key_box), FadeOut(key_row),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 4: 三角形有三条高
    # ------------------------------------------------------------------

    def scene_4_three_heights(self):
        title = Text(
            "三角形有三条高!",
            font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        hint = Text(
            "每条边都可以作底，对应的高各有一条",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(UP * 4.6)
        self.play(FadeIn(hint), run_time=0.4)

        tri = self._tri_main
        lbl_A, lbl_B, lbl_C = self._lbl_A, self._lbl_B, self._lbl_C

        # ---------- 高 1：从 C 到 AB，底边 AB ----------
        tag1 = Text(
            "底边 AB → 高 CD",
            font=FONT, font_size=24, color=COLOR_BASE,
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(tag1), run_time=0.4)

        base1 = Line(self.A, self.B, color=COLOR_BASE, stroke_width=6)
        self.play(Create(base1), run_time=0.5)

        h1 = Line(self.C, self.D, color=COLOR_HEIGHT, stroke_width=5)
        fd1 = Dot(self.D, color=COLOR_FOOT, radius=0.09)
        ra1 = make_right_angle_mark(self.D, self.C, self.B, size=0.18, color=COLOR_RA)
        lbl_h1 = Text("高 CD", font=FONT, font_size=20, color=COLOR_HEIGHT)
        lbl_h1.move_to((self.C + self.D) / 2 + LEFT * 0.75)

        self.play(Create(h1), FadeIn(fd1), Create(ra1), run_time=0.8)
        self.play(FadeIn(lbl_h1), run_time=0.3)
        self.wait(1.2)

        self.play(
            FadeOut(base1), FadeOut(h1), FadeOut(fd1),
            FadeOut(ra1), FadeOut(lbl_h1), FadeOut(tag1),
            run_time=0.4,
        )

        # ---------- 高 2：从 A 到 BC，底边 BC ----------
        tag2 = Text(
            "底边 BC → 高 AE",
            font=FONT, font_size=24, color=COLOR_BASE,
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(tag2), run_time=0.4)

        base2 = Line(self.B, self.C, color=COLOR_BASE, stroke_width=6)
        self.play(Create(base2), run_time=0.5)

        h2 = Line(self.A, self.E, color=COLOR_HEIGHT, stroke_width=5)
        fd2 = Dot(self.E, color=COLOR_FOOT, radius=0.09)
        ra2 = make_right_angle_mark(self.E, self.A, self.C, size=0.18, color=COLOR_RA)
        mid_AE = (self.A + self.E) / 2
        # 方向放在右侧
        lbl_h2 = Text("高 AE", font=FONT, font_size=20, color=COLOR_HEIGHT)
        lbl_h2.move_to(mid_AE + RIGHT * 0.75)

        self.play(Create(h2), FadeIn(fd2), Create(ra2), run_time=0.8)
        self.play(FadeIn(lbl_h2), run_time=0.3)
        self.wait(1.2)

        self.play(
            FadeOut(base2), FadeOut(h2), FadeOut(fd2),
            FadeOut(ra2), FadeOut(lbl_h2), FadeOut(tag2),
            run_time=0.4,
        )

        # ---------- 高 3：从 B 到 CA，底边 CA ----------
        tag3 = Text(
            "底边 CA → 高 BF",
            font=FONT, font_size=24, color=COLOR_BASE,
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(tag3), run_time=0.4)

        base3 = Line(self.C, self.A, color=COLOR_BASE, stroke_width=6)
        self.play(Create(base3), run_time=0.5)

        h3 = Line(self.B, self.F, color=COLOR_HEIGHT, stroke_width=5)
        fd3 = Dot(self.F, color=COLOR_FOOT, radius=0.09)
        ra3 = make_right_angle_mark(self.F, self.B, self.A, size=0.18, color=COLOR_RA)
        mid_BF = (self.B + self.F) / 2
        lbl_h3 = Text("高 BF", font=FONT, font_size=20, color=COLOR_HEIGHT)
        lbl_h3.move_to(mid_BF + RIGHT * 0.75)

        self.play(Create(h3), FadeIn(fd3), Create(ra3), run_time=0.8)
        self.play(FadeIn(lbl_h3), run_time=0.3)
        self.wait(0.8)

        # 三条高都显示
        self.play(FadeOut(tag3), run_time=0.3)
        h1_copy = Line(self.C, self.D, color=COLOR_HEIGHT, stroke_width=4)
        h2_copy = Line(self.A, self.E, color=COLOR_HEIGHT, stroke_width=4)
        fd1c = Dot(self.D, color=COLOR_FOOT, radius=0.08)
        fd2c = Dot(self.E, color=COLOR_FOOT, radius=0.08)
        lbl_h1c = Text("CD", font=FONT, font_size=18, color=COLOR_HEIGHT)
        lbl_h1c.move_to((self.C + self.D) / 2 + LEFT * 0.6)
        lbl_h2c = Text("AE", font=FONT, font_size=18, color=COLOR_HEIGHT)
        lbl_h2c.move_to((self.A + self.E) / 2 + RIGHT * 0.6)

        self.play(
            Create(h1_copy), Create(h2_copy),
            FadeIn(fd1c), FadeIn(fd2c),
            FadeIn(lbl_h1c), FadeIn(lbl_h2c),
            run_time=0.7,
        )

        summary = Text(
            "一共有三条高！",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(summary, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(hint), FadeOut(summary),
            FadeOut(base3),
            FadeOut(h1_copy), FadeOut(h2_copy), FadeOut(h3),
            FadeOut(fd1c), FadeOut(fd2c), FadeOut(fd3),
            FadeOut(ra3),
            FadeOut(lbl_h1c), FadeOut(lbl_h2c), FadeOut(lbl_h3),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 5: 钝角三角形的高（高在形外）
    # ------------------------------------------------------------------

    def scene_5_obtuse_triangle(self):
        # 先淡出主三角形相关元素
        self.play(
            FadeOut(self._tri_main),
            FadeOut(self._lbl_A),
            FadeOut(self._lbl_B),
            FadeOut(self._lbl_C),
            run_time=0.5,
        )

        title = Text(
            "钝角三角形的高",
            font=FONT, font_size=36, color=COLOR_OBTUSE,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        hint = Text(
            "钝角三角形有的高在三角形外面！",
            font=FONT, font_size=24, color=COLOR_HL,
        ).move_to(UP * 4.6)
        self.play(FadeIn(hint), run_time=0.5)

        # 画钝角三角形 PQR（放在中部）
        # 将 P, Q, R 整体平移到合适位置
        shift_ob = np.array([0.0, 0.0, 0.0])
        P = self.P + shift_ob
        Q = self.Q + shift_ob
        R = self.R + shift_ob

        ob_tri = self.make_triangle(P, Q, R, color=COLOR_OBTUSE, fill_opacity=0.10)
        self.play(Create(ob_tri), run_time=1.0)

        lbl_P = Text("P", font=FONT, font_size=26, color=WHITE).next_to(P, DL, buff=0.15)
        lbl_Q = Text("Q", font=FONT, font_size=26, color=WHITE).next_to(Q, DR, buff=0.15)
        lbl_R = Text("R", font=FONT, font_size=26, color=WHITE).next_to(R, UP, buff=0.15)
        self.play(FadeIn(lbl_P), FadeIn(lbl_Q), FadeIn(lbl_R), run_time=0.4)

        # 标注 ∠P 是钝角
        angle_P_val = self._calc_angle(Q, P, R)
        angle_P_deg = np.degrees(angle_P_val)
        print(f"angle_P = {angle_P_deg:.1f}°")

        # 显示角度提示
        angle_hint = VGroup(
            Text("∠P = ", font=FONT, font_size=22, color=COLOR_OBTUSE),
            MathTex(f"{angle_P_deg:.0f}" + r"^\circ", font_size=28, color=COLOR_OBTUSE),
            Text("> 90° （钝角）", font=FONT, font_size=22, color=COLOR_OBTUSE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.5)
        self.play(FadeIn(angle_hint), run_time=0.5)
        self.wait(0.8)

        # ---------- 以 PQ 为底：高 RG 在形内 ----------
        case1_title = Text(
            "以 PQ 为底，高 RG 在三角形内",
            font=FONT, font_size=22, color=COLOR_BASE,
        ).move_to(DOWN * 4.5)
        self.play(FadeOut(angle_hint), FadeIn(case1_title), run_time=0.4)

        base_PQ = Line(P, Q, color=COLOR_BASE, stroke_width=6)
        self.play(Create(base_PQ), run_time=0.5)

        # 垂足 G：从 R 到 PQ 的垂足（在 PQ 内部，因为 ∠R < 90°）
        G = foot_of_perpendicular(R, P, Q)
        h_RG = Line(R, G, color=COLOR_HEIGHT, stroke_width=5)
        fd_G = Dot(G, color=COLOR_FOOT, radius=0.09)
        ra_G = make_right_angle_mark(G, R, Q, size=0.2, color=COLOR_RA)
        lbl_G = Text("G", font=FONT, font_size=22, color=COLOR_FOOT).next_to(G, DOWN, buff=0.18)
        lbl_hRG = Text("高 RG", font=FONT, font_size=20, color=COLOR_HEIGHT)
        lbl_hRG.move_to((R + G) / 2 + LEFT * 0.7)

        self.play(Create(h_RG), FadeIn(fd_G), Create(ra_G), run_time=0.8)
        self.play(FadeIn(lbl_G), FadeIn(lbl_hRG), run_time=0.3)
        self.wait(1.0)

        note_in = Text("高在三角形内部 ✓", font=FONT, font_size=22, color=COLOR_BASE)
        note_in.move_to(DOWN * 5.3)
        self.play(FadeIn(note_in), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(base_PQ), FadeOut(h_RG), FadeOut(fd_G),
            FadeOut(ra_G), FadeOut(lbl_G), FadeOut(lbl_hRG),
            FadeOut(case1_title), FadeOut(note_in),
            run_time=0.5,
        )

        # ---------- 以 PR 为底：高 QT 在形外，需要延长 PR ----------
        case2_title = Text(
            "以 PR 为底，高 QT 在三角形外！",
            font=FONT, font_size=22, color=COLOR_OBTUSE,
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(case2_title), run_time=0.4)

        base_PR = Line(P, R, color=COLOR_BASE, stroke_width=6)
        self.play(Create(base_PR), run_time=0.5)

        # 垂足 T：从 Q 到直线 PR 的垂足
        T = foot_of_perpendicular(Q, P, R)

        # 检查 T 是否在 PR 之外（在 P 侧之外）
        PR_vec = R - P
        PT_vec = T - P
        t_val  = np.dot(PT_vec, PR_vec) / np.dot(PR_vec, PR_vec)
        print(f"T on PR: t={t_val:.3f} (outside if <0 or >1)")

        # 延长底边 PR 到 T（虚线延长部分）
        if t_val < 0:
            # T 在 P 之外（∠P 是钝角，高从 Q 落在 P 的另一侧）
            extend_end = P  # 延长线从 T 到 P
            ext_line = DashedLine(T, P, color=COLOR_DASH, stroke_width=3, dash_length=0.12)
        else:
            # T 在 R 之外
            extend_end = R
            ext_line = DashedLine(R, T, color=COLOR_DASH, stroke_width=3, dash_length=0.12)

        self.play(Create(ext_line), run_time=0.7)

        extend_hint = Text(
            "需要将底边 PR 延长！",
            font=FONT, font_size=22, color=COLOR_DASH,
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(extend_hint), run_time=0.4)
        self.wait(0.5)

        # 高线 QT（在形外）
        h_QT = Line(Q, T, color=COLOR_HEIGHT, stroke_width=5)
        fd_T = Dot(T, color=COLOR_FOOT, radius=0.09)
        ra_T = make_right_angle_mark(T, Q, R, size=0.2, color=COLOR_RA)
        lbl_T = Text("T", font=FONT, font_size=22, color=COLOR_FOOT).next_to(T, DOWN, buff=0.18)
        lbl_hQT = Text("高 QT", font=FONT, font_size=20, color=COLOR_HEIGHT)
        mid_QT = (Q + T) / 2
        lbl_hQT.move_to(mid_QT + RIGHT * 0.7)

        self.play(Create(h_QT), FadeIn(fd_T), Create(ra_T), run_time=0.8)
        self.play(FadeIn(lbl_T), FadeIn(lbl_hQT), run_time=0.3)
        self.wait(0.8)

        # 关键结论
        key_text = Text(
            "高 QT 在三角形的外部！",
            font=FONT, font_size=24, color=COLOR_OBTUSE,
        ).move_to(DOWN * 5.3)
        self.play(FadeOut(extend_hint), FadeIn(key_text), run_time=0.5)

        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(hint),
            FadeOut(ob_tri), FadeOut(lbl_P), FadeOut(lbl_Q), FadeOut(lbl_R),
            FadeOut(base_PR), FadeOut(ext_line),
            FadeOut(h_QT), FadeOut(fd_T), FadeOut(ra_T),
            FadeOut(lbl_T), FadeOut(lbl_hQT),
            FadeOut(case2_title), FadeOut(key_text),
            run_time=0.7,
        )

    # ------------------------------------------------------------------
    # Scene 6: 知识总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = Text(
            "知识总结",
            font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 卡片背景
        card_bg = RoundedRectangle(
            width=7.8, height=11.5,
            corner_radius=0.4,
            color=WHITE,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=0.04,
        ).move_to(UP * 0.0)
        self.play(FadeIn(card_bg), run_time=0.4)

        # ---- 条目 1：定义 ----
        item1_title = Text("1. 三角形的高", font=FONT, font_size=26, color=COLOR_HEIGHT)
        item1_body  = VGroup(
            Text("从三角形一个顶点向对边作垂线，", font=FONT, font_size=20, color=GRAY_A),
            Text("顶点与垂足之间的线段叫做高。", font=FONT, font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        item1 = VGroup(item1_title, item1_body).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item1.move_to(UP * 4.2 + LEFT * 0.3)
        self.play(FadeIn(item1, shift=RIGHT * 0.3), run_time=0.5)

        # ---- 条目 2：底 ----
        item2_title = Text("2. 三角形的底", font=FONT, font_size=26, color=COLOR_BASE)
        item2_body  = Text(
            "与高对应的那条边叫做底。",
            font=FONT, font_size=20, color=GRAY_A,
        )
        item2 = VGroup(item2_title, item2_body).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item2.move_to(UP * 2.4 + LEFT * 0.3)
        self.play(FadeIn(item2, shift=RIGHT * 0.3), run_time=0.5)

        # ---- 条目 3：高⊥底 ----
        item3_title = Text("3. 高与底的关系", font=FONT, font_size=26, color=COLOR_RA)
        item3_body  = VGroup(
            Text("高", font=FONT, font_size=22, color=WHITE),
            MathTex(r"\perp", font_size=28, color=COLOR_HL),
            Text("底（高和底互相垂直）", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.12)
        item3 = VGroup(item3_title, item3_body).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item3.move_to(UP * 0.8 + LEFT * 0.3)
        self.play(FadeIn(item3, shift=RIGHT * 0.3), run_time=0.5)

        # ---- 条目 4：三条高 ----
        item4_title = Text("4. 每个三角形有三条高", font=FONT, font_size=26, color=COLOR_HL)
        item4_body  = Text(
            "三条边各可作底，对应三条高。",
            font=FONT, font_size=20, color=GRAY_A,
        )
        item4 = VGroup(item4_title, item4_body).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item4.move_to(DOWN * 0.9 + LEFT * 0.3)
        self.play(FadeIn(item4, shift=RIGHT * 0.3), run_time=0.5)

        # ---- 条目 5：钝角三角形 ----
        item5_title = Text("5. 钝角三角形的高", font=FONT, font_size=26, color=COLOR_OBTUSE)
        item5_body  = VGroup(
            Text("钝角所对底边上的高在形内，", font=FONT, font_size=20, color=GRAY_A),
            Text("钝角顶点的高需延长底边，高在形外。", font=FONT, font_size=20, color=COLOR_OBTUSE),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        item5 = VGroup(item5_title, item5_body).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item5.move_to(DOWN * 2.8 + LEFT * 0.3)
        self.play(FadeIn(item5, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(4.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(item1), FadeOut(item2), FadeOut(item3),
            FadeOut(item4), FadeOut(item5),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B,
        ).move_to(UP * 0.5)

        self.play(ReplacementTransform(self.author, author_big), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多几何知识!",
            font=FONT, font_size=30, color=COLOR_HL,
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 小三角形装饰
        deco_group = VGroup()
        for i in range(6):
            angle_val = i * PI / 3
            pos = DOWN * 3.0 + 2.2 * np.array([np.cos(angle_val), np.sin(angle_val), 0.0])
            mini_tri = Polygon(
                pos,
                pos + np.array([0.35, 0.0, 0.0]),
                pos + np.array([0.175, 0.30, 0.0]),
                color=COLOR_TRI,
                fill_opacity=0.75,
                stroke_width=0,
            )
            deco_group.add(mini_tri)

        self.play(*[FadeIn(d, scale=0.5) for d in deco_group], run_time=0.6)
        self.play(Rotate(deco_group, angle=PI, run_time=1.5))
        self.wait(1.0)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco_group),
            run_time=1.0,
        )


# ======================================================================
# 运行命令:
# manim -qm 002_三角形的高和底.py TriangleHeightBaseLesson   # 720p
# manim -qh 002_三角形的高和底.py TriangleHeightBaseLesson   # 1080p
# ======================================================================
