"""
002_平行与垂直.py — 平行与垂直 教学动画

知识点: 平行与垂直
  - 同一平面内，不相交的两条直线叫做平行线，记作 AB∥CD
  - 两条直线相交成直角(90°)，就说这两条直线互相垂直
  - 其中一条直线是另一条直线的垂线，交点叫垂足

年级: 四年级第一学期 第六章整理与提高
格式: TikTok 竖屏 (1080×1920)
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
BG_COLOR       = "#1a1a2e"
COLOR_PARALLEL = "#3b82f6"   # 蓝色 — 平行线
COLOR_PERP     = "#22c55e"   # 绿色 — 垂直
COLOR_HL       = "#fbbf24"   # 黄色 高亮
COLOR_AUX      = "#94a3b8"   # 灰蓝 辅助线
COLOR_AUTHOR   = "#6b7280"   # 灰色 作者信息
COLOR_NOTE     = "#f87171"   # 红色 标注
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class ParallelPerpendicularLesson(Scene):
    """
    平行与垂直教学动画
    场景顺序:
      1. 开场钩子
      2. 同一平面内两条直线的位置关系
      3. 平行线的定义
      4. 平行线的记法 AB∥CD
      5. 垂直的定义
      6. 垂足与垂线
      7. 符号记法 AB⊥CD
      8. 知识总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_two_lines_relation()
        self.scene_3_parallel_definition()
        self.scene_4_parallel_notation()
        self.scene_5_perpendicular_definition()
        self.scene_6_foot_and_perpline()
        self.scene_7_perp_notation()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标（精确计算，不使用臆想数值）"""

        # ===== 平行线对 =====
        # 两条水平平行线，间距 1.8 单位
        self.PAR_Y1 =  1.2   # 上方平行线 y 坐标
        self.PAR_Y2 = -0.6   # 下方平行线 y 坐标
        self.PAR_HALF_LEN = 3.2   # 半长

        self.par_A1 = np.array([-self.PAR_HALF_LEN, self.PAR_Y1, 0.0])
        self.par_B1 = np.array([ self.PAR_HALF_LEN, self.PAR_Y1, 0.0])
        self.par_A2 = np.array([-self.PAR_HALF_LEN, self.PAR_Y2, 0.0])
        self.par_B2 = np.array([ self.PAR_HALF_LEN, self.PAR_Y2, 0.0])

        # ===== 垂直线对 =====
        # 水平线 + 竖直线，交于原点附近
        self.PERP_CENTER = np.array([0.0, 0.5, 0.0])
        self.PERP_HALF_LEN = 2.8

        # 水平线
        self.perp_H_start = self.PERP_CENTER + self.PERP_HALF_LEN * LEFT
        self.perp_H_end   = self.PERP_CENTER + self.PERP_HALF_LEN * RIGHT

        # 竖直线 (垂直于水平线)
        self.perp_V_start = self.PERP_CENTER + self.PERP_HALF_LEN * DOWN
        self.perp_V_end   = self.PERP_CENTER + self.PERP_HALF_LEN * UP

        # 垂足 = 两线交点 = PERP_CENTER
        self.foot = self.PERP_CENTER.copy()

        # ===== 斜交线（用于对比：相交但不垂直）=====
        # 方向向量 (3, 1) 和 (−1, 2)，叉积非零且点积非零
        angle_deg = 55.0  # 斜线角度（度）
        self.INTERSECT_CENTER = np.array([0.0, 0.5, 0.0])
        self.INTERSECT_LEN = 2.6

        theta = np.radians(angle_deg)
        dir_slant1 = np.array([np.cos(theta), np.sin(theta), 0.0])
        dir_slant2 = np.array([np.cos(theta + np.radians(90)), np.sin(theta + np.radians(90)), 0.0])
        # 改成一条水平线和一条斜线（非直角）
        dir_h   = np.array([1.0, 0.0, 0.0])
        theta2  = np.radians(55.0)
        dir_obl = np.array([np.cos(theta2), np.sin(theta2), 0.0])

        self.oblique_H_start = self.INTERSECT_CENTER - self.INTERSECT_LEN * dir_h
        self.oblique_H_end   = self.INTERSECT_CENTER + self.INTERSECT_LEN * dir_h
        self.oblique_L_start = self.INTERSECT_CENTER - self.INTERSECT_LEN * dir_obl
        self.oblique_L_end   = self.INTERSECT_CENTER + self.INTERSECT_LEN * dir_obl

        # ===== 验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何关系"""
        eps = 1e-10

        # 验证平行线方向一致（叉积为0）
        v1 = self.par_B1 - self.par_A1
        v2 = self.par_B2 - self.par_A2
        cross = v1[0] * v2[1] - v1[1] * v2[0]
        assert abs(cross) < eps, f"平行线不平行: cross={cross}"

        # 验证平行线确实不重合（y 坐标不同）
        assert abs(self.PAR_Y1 - self.PAR_Y2) > eps, "平行线重合!"

        # 验证垂直线正交（点积为0）
        vH = self.perp_H_end - self.perp_H_start
        vV = self.perp_V_end - self.perp_V_start
        dot = np.dot(vH[:2], vV[:2])
        assert abs(dot) < eps, f"垂直线不垂直: dot={dot}"

        print("Geometry verification passed.")

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def create_right_angle_mark(self, corner, p1, p2, size=0.3, color=WHITE, stroke_width=2.5):
        """创建直角小方块标记"""
        v1 = (p1 - corner)
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = (p2 - corner)
        v2 = v2 / np.linalg.norm(v2) * size
        mark = Polygon(
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=color,
            stroke_width=stroke_width,
            fill_opacity=0,
        )
        return mark

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "平行？垂直？",
            font=FONT, font_size=52, color=COLOR_HL,
        ).move_to(UP * 5.0)

        sub = Text(
            "两条直线之间有什么关系?",
            font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 4.0)

        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 快速闪现两种情形（平行 vs 垂直）
        # 平行示意
        par_quick_1 = Line(
            np.array([-3.0, 1.5, 0.0]), np.array([3.0, 1.5, 0.0]),
            color=COLOR_PARALLEL, stroke_width=5,
        )
        par_quick_2 = Line(
            np.array([-3.0, -0.5, 0.0]), np.array([3.0, -0.5, 0.0]),
            color=COLOR_PARALLEL, stroke_width=5,
        )
        # 垂直示意
        perp_quick_h = Line(
            np.array([-2.5, -3.5, 0.0]), np.array([2.5, -3.5, 0.0]),
            color=COLOR_PERP, stroke_width=5,
        )
        perp_quick_v = Line(
            np.array([0.0, -5.5, 0.0]), np.array([0.0, -1.5, 0.0]),
            color=COLOR_PERP, stroke_width=5,
        )

        par_label = Text("平行", font=FONT, font_size=28, color=COLOR_PARALLEL).move_to(UP * 0.3)
        perp_label = Text("垂直", font=FONT, font_size=28, color=COLOR_PERP).move_to(DOWN * 4.5 + RIGHT * 2.3)

        self.play(
            Create(par_quick_1), Create(par_quick_2), run_time=0.6,
        )
        self.play(FadeIn(par_label), run_time=0.3)

        self.play(
            Create(perp_quick_h), Create(perp_quick_v), run_time=0.6,
        )
        self.play(FadeIn(perp_label), run_time=0.3)

        self.wait(0.8)

        self.play(
            FadeOut(hook), FadeOut(sub),
            FadeOut(par_quick_1), FadeOut(par_quick_2), FadeOut(par_label),
            FadeOut(perp_quick_h), FadeOut(perp_quick_v), FadeOut(perp_label),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 同一平面内两条直线的位置关系
    # ------------------------------------------------------------------

    def scene_2_two_lines_relation(self):
        title = Text(
            "同一平面内两条直线",
            font=FONT, font_size=32, color=WHITE,
        ).move_to(UP * 5.5)

        subtitle = Text(
            "只有两种位置关系",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.8)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.4)

        # ---------- 情形 A：不相交（平行）----------
        case_a_label = Text("情形 A：不相交", font=FONT, font_size=26, color=COLOR_PARALLEL)
        case_a_label.move_to(UP * 3.8)
        self.play(FadeIn(case_a_label), run_time=0.4)

        line_a1 = Line(
            np.array([-3.0, 2.8, 0.0]), np.array([3.0, 2.8, 0.0]),
            color=COLOR_PARALLEL, stroke_width=4,
        )
        line_a2 = Line(
            np.array([-3.0, 1.5, 0.0]), np.array([3.0, 1.5, 0.0]),
            color=COLOR_PARALLEL, stroke_width=4,
        )
        self.play(Create(line_a1), Create(line_a2), run_time=0.8)

        # 用带箭头的虚线表示永远不相交
        no_meet_arrow = DashedLine(
            np.array([3.2, 2.8, 0.0]), np.array([4.0, 2.8, 0.0]),
            color=COLOR_AUX, dash_length=0.12,
        )
        no_meet_arrow2 = DashedLine(
            np.array([3.2, 1.5, 0.0]), np.array([4.0, 1.5, 0.0]),
            color=COLOR_AUX, dash_length=0.12,
        )
        self.play(Create(no_meet_arrow), Create(no_meet_arrow2), run_time=0.4)

        par_note = Text("永远不相交", font=FONT, font_size=20, color=COLOR_HL).move_to(UP * 0.8)
        self.play(FadeIn(par_note), run_time=0.4)
        self.wait(0.8)

        # ---------- 情形 B：相交 ----------
        case_b_label = Text("情形 B：相交", font=FONT, font_size=26, color=COLOR_NOTE)
        case_b_label.move_to(DOWN * 0.2)
        self.play(FadeIn(case_b_label), run_time=0.4)

        # 一条水平线，一条斜线，相交
        intersect_h = Line(
            np.array([-3.0, -1.5, 0.0]), np.array([3.0, -1.5, 0.0]),
            color=COLOR_NOTE, stroke_width=4,
        )
        angle_rad = np.radians(55)
        dir_obl = np.array([np.cos(angle_rad), np.sin(angle_rad), 0.0])
        cross_pt = np.array([0.0, -1.5, 0.0])
        intersect_l = Line(
            cross_pt - 2.5 * dir_obl, cross_pt + 2.5 * dir_obl,
            color=COLOR_NOTE, stroke_width=4,
        )
        cross_dot = Dot(cross_pt, color=COLOR_HL, radius=0.10)

        self.play(Create(intersect_h), Create(intersect_l), run_time=0.8)
        self.play(FadeIn(cross_dot), run_time=0.3)

        inter_note = Text("有交点", font=FONT, font_size=20, color=COLOR_HL).move_to(DOWN * 2.8)
        self.play(FadeIn(inter_note), run_time=0.4)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(case_a_label), FadeOut(line_a1), FadeOut(line_a2),
            FadeOut(no_meet_arrow), FadeOut(no_meet_arrow2), FadeOut(par_note),
            FadeOut(case_b_label), FadeOut(intersect_h), FadeOut(intersect_l),
            FadeOut(cross_dot), FadeOut(inter_note),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 平行线的定义
    # ------------------------------------------------------------------

    def scene_3_parallel_definition(self):
        title = Text("平行线", font=FONT, font_size=40, color=COLOR_PARALLEL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        definition_line1 = Text(
            "在同一平面内，", font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 4.7)
        definition_line2 = VGroup(
            Text("不相交", font=FONT, font_size=28, color=COLOR_HL),
            Text("的两条直线", font=FONT, font_size=26, color=GRAY_A),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 4.0)
        definition_line3 = Text(
            "叫做平行线",
            font=FONT, font_size=28, color=COLOR_PARALLEL,
        ).move_to(UP * 3.3)

        self.play(FadeIn(definition_line1), run_time=0.4)
        self.play(FadeIn(definition_line2), run_time=0.4)
        self.play(FadeIn(definition_line3), run_time=0.4)

        # 画两条平行线
        line1 = Line(self.par_A1, self.par_B1, color=COLOR_PARALLEL, stroke_width=5)
        line2 = Line(self.par_A2, self.par_B2, color=COLOR_PARALLEL, stroke_width=5)

        # 点 A, B on line1; C, D on line2
        dot_A = Dot(self.par_A1 + 0.8 * RIGHT, color=COLOR_PARALLEL, radius=0.08)
        dot_B = Dot(self.par_B1 - 0.8 * RIGHT, color=COLOR_PARALLEL, radius=0.08)
        dot_C = Dot(self.par_A2 + 0.8 * RIGHT, color=COLOR_PARALLEL, radius=0.08)
        dot_D = Dot(self.par_B2 - 0.8 * RIGHT, color=COLOR_PARALLEL, radius=0.08)

        label_A = Text("A", font=FONT, font_size=24, color=WHITE).next_to(dot_A, UP, buff=0.1)
        label_B = Text("B", font=FONT, font_size=24, color=WHITE).next_to(dot_B, UP, buff=0.1)
        label_C = Text("C", font=FONT, font_size=24, color=WHITE).next_to(dot_C, DOWN, buff=0.1)
        label_D = Text("D", font=FONT, font_size=24, color=WHITE).next_to(dot_D, DOWN, buff=0.1)

        self.play(Create(line1), Create(line2), run_time=1.0)
        self.play(
            FadeIn(dot_A), FadeIn(dot_B), FadeIn(dot_C), FadeIn(dot_D),
            run_time=0.4,
        )
        self.play(
            Write(label_A), Write(label_B), Write(label_C), Write(label_D),
            run_time=0.5,
        )

        # 箭头方向标记（平行线常用双箭头标记）
        arrow_1 = Arrow(
            self.par_A1 + 0.5 * RIGHT, self.par_B1 - 0.5 * RIGHT,
            color=COLOR_PARALLEL, buff=0, stroke_width=2,
            max_tip_length_to_length_ratio=0.08,
        )
        arrow_2 = Arrow(
            self.par_A2 + 0.5 * RIGHT, self.par_B2 - 0.5 * RIGHT,
            color=COLOR_PARALLEL, buff=0, stroke_width=2,
            max_tip_length_to_length_ratio=0.08,
        )
        self.play(Create(arrow_1), Create(arrow_2), run_time=0.5)

        # 强调：无论延长多远都不相交
        dashed_ext1 = DashedLine(
            self.par_B1, self.par_B1 + 1.5 * RIGHT,
            color=COLOR_AUX, dash_length=0.12,
        )
        dashed_ext2 = DashedLine(
            self.par_B2, self.par_B2 + 1.5 * RIGHT,
            color=COLOR_AUX, dash_length=0.12,
        )
        self.play(Create(dashed_ext1), Create(dashed_ext2), run_time=0.5)

        note = Text(
            "无论延长多远，永远不相交",
            font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.8)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition_line1), FadeOut(definition_line2), FadeOut(definition_line3),
            FadeOut(line1), FadeOut(line2),
            FadeOut(dot_A), FadeOut(dot_B), FadeOut(dot_C), FadeOut(dot_D),
            FadeOut(label_A), FadeOut(label_B), FadeOut(label_C), FadeOut(label_D),
            FadeOut(arrow_1), FadeOut(arrow_2),
            FadeOut(dashed_ext1), FadeOut(dashed_ext2),
            FadeOut(note),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 4: 平行线的记法
    # ------------------------------------------------------------------

    def scene_4_parallel_notation(self):
        title = Text("平行线的记法", font=FONT, font_size=36, color=COLOR_PARALLEL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 画带标签的平行线
        line1 = Line(self.par_A1, self.par_B1, color=COLOR_PARALLEL, stroke_width=5)
        line2 = Line(self.par_A2, self.par_B2, color=COLOR_PARALLEL, stroke_width=5)

        pA = self.par_A1 + 0.6 * RIGHT
        pB = self.par_B1 - 0.6 * RIGHT
        pC = self.par_A2 + 0.6 * RIGHT
        pD = self.par_B2 - 0.6 * RIGHT

        dot_A = Dot(pA, color=COLOR_PARALLEL, radius=0.08)
        dot_B = Dot(pB, color=COLOR_PARALLEL, radius=0.08)
        dot_C = Dot(pC, color=COLOR_PARALLEL, radius=0.08)
        dot_D = Dot(pD, color=COLOR_PARALLEL, radius=0.08)

        lA = Text("A", font=FONT, font_size=22, color=WHITE).next_to(dot_A, UP, buff=0.12)
        lB = Text("B", font=FONT, font_size=22, color=WHITE).next_to(dot_B, UP, buff=0.12)
        lC = Text("C", font=FONT, font_size=22, color=WHITE).next_to(dot_C, DOWN, buff=0.12)
        lD = Text("D", font=FONT, font_size=22, color=WHITE).next_to(dot_D, DOWN, buff=0.12)

        self.play(Create(line1), Create(line2), run_time=0.8)
        self.play(
            FadeIn(dot_A), FadeIn(dot_B), FadeIn(dot_C), FadeIn(dot_D),
            Write(lA), Write(lB), Write(lC), Write(lD),
            run_time=0.6,
        )

        # 记法
        notation_label = Text("我们记作：", font=FONT, font_size=26, color=GRAY_A)
        notation_formula = MathTex(r"AB \parallel CD", font_size=48, color=COLOR_HL)
        notation_group = VGroup(notation_label, notation_formula).arrange(RIGHT, buff=0.25)
        notation_group.move_to(DOWN * 0.8)

        self.play(FadeIn(notation_label), run_time=0.4)
        self.play(Write(notation_formula), run_time=0.8)

        # 读法
        read_label = Text("读作：AB 平行于 CD", font=FONT, font_size=24, color=COLOR_AUX)
        read_label.move_to(DOWN * 2.0)
        self.play(FadeIn(read_label, shift=UP * 0.2), run_time=0.5)

        # 强调平行符号
        highlight_sym = SurroundingRectangle(notation_formula[0][2], color=COLOR_HL, buff=0.1)
        sym_label = Text("平行符号 ∥", font=FONT, font_size=22, color=COLOR_HL)
        sym_label.next_to(highlight_sym, DOWN, buff=0.25)
        self.play(Create(highlight_sym), FadeIn(sym_label), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line1), FadeOut(line2),
            FadeOut(dot_A), FadeOut(dot_B), FadeOut(dot_C), FadeOut(dot_D),
            FadeOut(lA), FadeOut(lB), FadeOut(lC), FadeOut(lD),
            FadeOut(notation_group),
            FadeOut(read_label),
            FadeOut(highlight_sym), FadeOut(sym_label),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 5: 垂直的定义
    # ------------------------------------------------------------------

    def scene_5_perpendicular_definition(self):
        title = Text("垂直", font=FONT, font_size=40, color=COLOR_PERP)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        definition_line1 = Text(
            "两条直线相交，", font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 4.7)

        definition_line2 = VGroup(
            Text("交成", font=FONT, font_size=26, color=GRAY_A),
            Text("直角(90°)", font=FONT, font_size=28, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 4.0)

        definition_line3 = Text(
            "就说这两条直线互相垂直",
            font=FONT, font_size=26, color=COLOR_PERP,
        ).move_to(UP * 3.3)

        self.play(FadeIn(definition_line1), run_time=0.4)
        self.play(FadeIn(definition_line2), run_time=0.4)
        self.play(FadeIn(definition_line3), run_time=0.4)

        # 先画斜交（非垂直）
        cross_pt = np.array([0.0, 0.8, 0.0])
        theta = np.radians(55)
        d_obl = np.array([np.cos(theta), np.sin(theta), 0.0])
        d_h   = np.array([1.0, 0.0, 0.0])
        L = 2.4

        line_h = Line(cross_pt - L * d_h,   cross_pt + L * d_h,   color=GRAY_B, stroke_width=4)
        line_s = Line(cross_pt - L * d_obl, cross_pt + L * d_obl, color=GRAY_B, stroke_width=4)
        dot_inter = Dot(cross_pt, color=COLOR_HL, radius=0.09)

        # 夹角弧
        # 叉积分量: d_h x d_obl = 1*sin(theta) - 0*cos(theta) > 0 → 逆时针
        line_obj_h = Line(cross_pt, cross_pt + L * d_h)
        line_obj_s = Line(cross_pt, cross_pt + L * d_obl)
        arc_oblique = Angle(line_obj_h, line_obj_s, radius=0.55, color=GRAY_B, other_angle=False)

        q_mark = MathTex(r"?", font_size=36, color=GRAY_B).move_to(cross_pt + np.array([0.35, 0.35, 0.0]))

        self.play(Create(line_h), Create(line_s), FadeIn(dot_inter), run_time=0.8)
        self.play(Create(arc_oblique), FadeIn(q_mark), run_time=0.4)

        not_perp = Text("不是直角，不是垂直", font=FONT, font_size=22, color=GRAY_B).move_to(DOWN * 0.8)
        self.play(FadeIn(not_perp), run_time=0.4)
        self.wait(0.8)

        # 变换成垂直
        target_h = Line(self.perp_H_start, self.perp_H_end, color=COLOR_PERP, stroke_width=5)
        target_v = Line(self.perp_V_start, self.perp_V_end, color=COLOR_PERP, stroke_width=5)

        self.play(
            FadeOut(line_h), FadeOut(line_s),
            FadeOut(arc_oblique), FadeOut(q_mark), FadeOut(not_perp),
            FadeOut(dot_inter),
            run_time=0.4,
        )
        self.play(Create(target_h), Create(target_v), run_time=0.8)

        foot_dot = Dot(self.foot, color=COLOR_HL, radius=0.10)
        self.play(FadeIn(foot_dot), run_time=0.3)

        # 直角标记
        right_mark = self.create_right_angle_mark(
            self.foot,
            self.foot + RIGHT,
            self.foot + UP,
            size=0.3, color=COLOR_PERP, stroke_width=3,
        )
        self.play(Create(right_mark), run_time=0.5)

        # 90° 标注
        degree_lbl = MathTex(r"90^\circ", font_size=36, color=COLOR_HL)
        degree_lbl.move_to(self.foot + np.array([0.65, 0.55, 0.0]))
        self.play(Write(degree_lbl), run_time=0.5)

        perp_result = Text("是直角，互相垂直！", font=FONT, font_size=26, color=COLOR_PERP)
        perp_result.move_to(DOWN * 1.8)
        self.play(FadeIn(perp_result, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(definition_line1), FadeOut(definition_line2), FadeOut(definition_line3),
            FadeOut(target_h), FadeOut(target_v), FadeOut(foot_dot),
            FadeOut(right_mark), FadeOut(degree_lbl), FadeOut(perp_result),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 6: 垂足与垂线
    # ------------------------------------------------------------------

    def scene_6_foot_and_perpline(self):
        title = Text("垂线 与 垂足", font=FONT, font_size=36, color=COLOR_PERP)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 画水平线（主线）
        base_start = np.array([-3.5, 1.0, 0.0])
        base_end   = np.array([ 3.5, 1.0, 0.0])
        base_line = Line(base_start, base_end, color=COLOR_PARALLEL, stroke_width=5)
        self.play(Create(base_line), run_time=0.6)

        # 垂足位置
        foot_pt = np.array([0.0, 1.0, 0.0])
        foot_dot = Dot(foot_pt, color=COLOR_HL, radius=0.10)

        # 垂线（从下方到上方穿过垂足）
        perp_top  = foot_pt + 2.8 * UP
        perp_bot  = foot_pt + 1.5 * DOWN
        perp_line = Line(perp_bot, perp_top, color=COLOR_PERP, stroke_width=5)

        self.play(Create(perp_line), run_time=0.8)
        self.play(FadeIn(foot_dot), run_time=0.3)

        # 直角标记
        right_mk = self.create_right_angle_mark(
            foot_pt,
            foot_pt + RIGHT,
            foot_pt + UP,
            size=0.28, color=COLOR_PERP, stroke_width=3,
        )
        self.play(Create(right_mk), run_time=0.4)

        # 标注: 垂线
        perp_arrow = Arrow(
            perp_top + np.array([1.2, 0.2, 0.0]),
            perp_top + np.array([0.2, 0.1, 0.0]),
            color=COLOR_PERP, buff=0.05, stroke_width=2,
            max_tip_length_to_length_ratio=0.18,
        )
        perp_line_label = Text("垂线", font=FONT, font_size=26, color=COLOR_PERP)
        perp_line_label.move_to(perp_top + np.array([2.0, 0.2, 0.0]))
        self.play(Create(perp_arrow), FadeIn(perp_line_label), run_time=0.5)

        # 标注: 垂足
        foot_arrow = Arrow(
            foot_pt + np.array([1.5, -0.8, 0.0]),
            foot_pt + np.array([0.15, -0.15, 0.0]),
            color=COLOR_HL, buff=0.05, stroke_width=2,
            max_tip_length_to_length_ratio=0.18,
        )
        foot_label = Text("垂足", font=FONT, font_size=26, color=COLOR_HL)
        foot_label.move_to(foot_pt + np.array([2.1, -0.85, 0.0]))
        self.play(Create(foot_arrow), FadeIn(foot_label), run_time=0.5)

        # 解释文字
        explain1 = Text("垂线：与另一条直线垂直的直线", font=FONT, font_size=22, color=GRAY_A)
        explain1.move_to(DOWN * 2.0)
        explain2 = Text("垂足：两条垂直直线的交点", font=FONT, font_size=22, color=GRAY_A)
        explain2.move_to(DOWN * 2.9)

        self.play(FadeIn(explain1, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(explain2, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(base_line), FadeOut(perp_line), FadeOut(foot_dot),
            FadeOut(right_mk),
            FadeOut(perp_arrow), FadeOut(perp_line_label),
            FadeOut(foot_arrow), FadeOut(foot_label),
            FadeOut(explain1), FadeOut(explain2),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 7: 垂直记法
    # ------------------------------------------------------------------

    def scene_7_perp_notation(self):
        title = Text("垂直的记法", font=FONT, font_size=36, color=COLOR_PERP)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 画垂直两线并标注 A B C D
        # 水平线: A--B，竖直线 C--D，交点 O
        h_start = np.array([-3.0, 1.2, 0.0])
        h_end   = np.array([ 3.0, 1.2, 0.0])
        v_start = np.array([ 0.0, -0.8, 0.0])
        v_end   = np.array([ 0.0,  3.2, 0.0])
        O_pt    = np.array([ 0.0,  1.2, 0.0])   # 交点

        line_AB = Line(h_start, h_end, color=COLOR_PERP, stroke_width=5)
        line_CD = Line(v_start, v_end, color=COLOR_PERP, stroke_width=5)
        dot_O   = Dot(O_pt, color=COLOR_HL, radius=0.09)

        self.play(Create(line_AB), Create(line_CD), FadeIn(dot_O), run_time=0.8)

        # 直角标记
        right_mk = self.create_right_angle_mark(
            O_pt, O_pt + RIGHT, O_pt + UP,
            size=0.28, color=COLOR_PERP, stroke_width=3,
        )
        self.play(Create(right_mk), run_time=0.4)

        # 标注点
        pA = h_start + 0.5 * RIGHT
        pB = h_end   - 0.5 * RIGHT
        pC = v_start + 0.5 * UP
        pD = v_end   - 0.5 * UP

        dots = VGroup(
            Dot(pA, color=COLOR_PERP, radius=0.07),
            Dot(pB, color=COLOR_PERP, radius=0.07),
            Dot(pC, color=COLOR_PERP, radius=0.07),
            Dot(pD, color=COLOR_PERP, radius=0.07),
        )
        lA = Text("A", font=FONT, font_size=22, color=WHITE).next_to(dots[0], DOWN, buff=0.12)
        lB = Text("B", font=FONT, font_size=22, color=WHITE).next_to(dots[1], DOWN, buff=0.12)
        lC = Text("C", font=FONT, font_size=22, color=WHITE).next_to(dots[2], LEFT, buff=0.12)
        lD = Text("D", font=FONT, font_size=22, color=WHITE).next_to(dots[3], LEFT, buff=0.12)
        lO = Text("O", font=FONT, font_size=22, color=COLOR_HL).next_to(dot_O, DR, buff=0.08)

        self.play(FadeIn(dots), Write(lA), Write(lB), Write(lC), Write(lD), Write(lO), run_time=0.6)

        # 记法
        notation_intro = Text("我们记作：", font=FONT, font_size=26, color=GRAY_A)
        notation_formula = MathTex(r"AB \perp CD", font_size=48, color=COLOR_HL)
        notation_row = VGroup(notation_intro, notation_formula).arrange(RIGHT, buff=0.2)
        notation_row.move_to(DOWN * 1.2)

        self.play(FadeIn(notation_intro), run_time=0.3)
        self.play(Write(notation_formula), run_time=0.8)

        # 读法
        read_txt = Text("读作：AB 垂直于 CD", font=FONT, font_size=24, color=COLOR_AUX)
        read_txt.move_to(DOWN * 2.3)
        self.play(FadeIn(read_txt, shift=UP * 0.2), run_time=0.5)

        # 垂足说明
        foot_txt = VGroup(
            Text("交点", font=FONT, font_size=22, color=GRAY_A),
            Text("O", font=FONT, font_size=22, color=COLOR_HL),
            Text("叫做", font=FONT, font_size=22, color=GRAY_A),
            Text("垂足", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.2)
        self.play(FadeIn(foot_txt), run_time=0.5)

        # 强调 ⊥ 符号
        box = SurroundingRectangle(notation_formula[0][2], color=COLOR_HL, buff=0.08)
        sym_note = Text("垂直符号 ⊥", font=FONT, font_size=22, color=COLOR_HL).next_to(box, DOWN, buff=0.2)
        self.play(Create(box), FadeIn(sym_note), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line_AB), FadeOut(line_CD), FadeOut(dot_O),
            FadeOut(right_mk), FadeOut(dots),
            FadeOut(lA), FadeOut(lB), FadeOut(lC), FadeOut(lD), FadeOut(lO),
            FadeOut(notation_row), FadeOut(read_txt), FadeOut(foot_txt),
            FadeOut(box), FadeOut(sym_note),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 8: 知识总结
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        title = Text("知识总结", font=FONT, font_size=36, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 卡片背景
        card = RoundedRectangle(
            width=7.8, height=10.5,
            corner_radius=0.4,
            color=WHITE,
            stroke_width=1.5,
            fill_color=WHITE,
            fill_opacity=0.05,
        ).move_to(UP * 0.1)
        self.play(FadeIn(card), run_time=0.4)

        # --- 条目 1: 平行线 ---
        t1 = Text("1. 平行线", font=FONT, font_size=28, color=COLOR_PARALLEL).move_to(UP * 4.0 + LEFT * 1.0)
        b1 = Text(
            "同一平面内，不相交的两条直线",
            font=FONT, font_size=20, color=GRAY_A,
        ).move_to(UP * 3.3 + LEFT * 0.0)
        # 小示意线
        mini_l1 = Line(np.array([-3.5, 2.6, 0.0]), np.array([-0.2, 2.6, 0.0]),
                       color=COLOR_PARALLEL, stroke_width=3)
        mini_l2 = Line(np.array([-3.5, 2.1, 0.0]), np.array([-0.2, 2.1, 0.0]),
                       color=COLOR_PARALLEL, stroke_width=3)
        self.play(FadeIn(t1), FadeIn(b1), Create(mini_l1), Create(mini_l2), run_time=0.6)

        # 记法
        r1_intro = Text("记作：", font=FONT, font_size=22, color=GRAY_A).move_to(UP * 1.5 + LEFT * 2.2)
        r1_form  = MathTex(r"AB \parallel CD", font_size=36, color=COLOR_HL).next_to(r1_intro, RIGHT, buff=0.2)
        self.play(FadeIn(r1_intro), Write(r1_form), run_time=0.5)

        # --- 条目 2: 垂直 ---
        t2 = Text("2. 垂直", font=FONT, font_size=28, color=COLOR_PERP).move_to(UP * 0.5 + LEFT * 1.5)
        b2_line1 = Text(
            "两直线相交成直角(90°)",
            font=FONT, font_size=20, color=GRAY_A,
        ).move_to(DOWN * 0.2)
        b2_line2 = Text(
            "这两条直线互相垂直",
            font=FONT, font_size=20, color=GRAY_A,
        ).move_to(DOWN * 0.7)

        # 小直角示意
        mini_foot = np.array([-2.8, -1.5, 0.0])
        mini_h = Line(mini_foot + 0.8 * LEFT, mini_foot + 0.8 * RIGHT,
                      color=COLOR_PERP, stroke_width=3)
        mini_v = Line(mini_foot + 0.6 * DOWN, mini_foot + 0.8 * UP,
                      color=COLOR_PERP, stroke_width=3)
        mini_mk = self.create_right_angle_mark(
            mini_foot, mini_foot + RIGHT, mini_foot + UP,
            size=0.18, color=COLOR_PERP, stroke_width=2,
        )
        self.play(FadeIn(t2), FadeIn(b2_line1), FadeIn(b2_line2), run_time=0.5)
        self.play(Create(mini_h), Create(mini_v), Create(mini_mk), run_time=0.5)

        r2_intro = Text("记作：", font=FONT, font_size=22, color=GRAY_A).move_to(DOWN * 2.0 + LEFT * 2.2)
        r2_form  = MathTex(r"AB \perp CD", font_size=36, color=COLOR_HL).next_to(r2_intro, RIGHT, buff=0.2)
        self.play(FadeIn(r2_intro), Write(r2_form), run_time=0.5)

        # --- 条目 3: 垂足 ---
        t3 = Text("3. 垂足：两垂直直线的交点", font=FONT, font_size=24, color=COLOR_HL)
        t3.move_to(DOWN * 3.2)
        self.play(FadeIn(t3, shift=RIGHT * 0.2), run_time=0.4)

        # 公式汇总行
        formula_row = VGroup(
            MathTex(r"AB \parallel CD", font_size=30, color=COLOR_PARALLEL),
            Text("  |  ", font=FONT, font_size=26, color=GRAY_B),
            MathTex(r"AB \perp CD", font_size=30, color=COLOR_PERP),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.5)
        self.play(FadeIn(formula_row), run_time=0.5)

        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(card),
            FadeOut(t1), FadeOut(b1), FadeOut(mini_l1), FadeOut(mini_l2),
            FadeOut(r1_intro), FadeOut(r1_form),
            FadeOut(t2), FadeOut(b2_line1), FadeOut(b2_line2),
            FadeOut(mini_h), FadeOut(mini_v), FadeOut(mini_mk),
            FadeOut(r2_intro), FadeOut(r2_form),
            FadeOut(t3), FadeOut(formula_row),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE,
        ).move_to(UP * 1.5)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(UP * 0.5)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我，学更多数学知识！",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 装饰：平行线 + 垂直线交替出现
        deco = VGroup()
        for i in range(3):
            yy = -2.5 - i * 1.0
            dl1 = Line(np.array([-3.5, yy, 0.0]), np.array([-0.5, yy, 0.0]),
                       color=COLOR_PARALLEL, stroke_width=3)
            dl2 = Line(np.array([-3.5, yy - 0.45, 0.0]), np.array([-0.5, yy - 0.45, 0.0]),
                       color=COLOR_PARALLEL, stroke_width=3)
            deco.add(dl1, dl2)

        perp_deco_h = Line(np.array([0.5, -2.5, 0.0]), np.array([3.5, -2.5, 0.0]),
                           color=COLOR_PERP, stroke_width=3)
        perp_deco_v = Line(np.array([2.0, -4.0, 0.0]), np.array([2.0, -1.0, 0.0]),
                           color=COLOR_PERP, stroke_width=3)
        perp_deco_mk = self.create_right_angle_mark(
            np.array([2.0, -2.5, 0.0]),
            np.array([2.0, -2.5, 0.0]) + RIGHT,
            np.array([2.0, -2.5, 0.0]) + UP,
            size=0.18, color=COLOR_PERP, stroke_width=2,
        )

        self.play(
            *[FadeIn(d, scale=0.8) for d in deco],
            Create(perp_deco_h), Create(perp_deco_v),
            run_time=0.7,
        )
        self.play(Create(perp_deco_mk), run_time=0.3)
        self.wait(2.0)

        # 淡出
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco),
            FadeOut(perp_deco_h), FadeOut(perp_deco_v), FadeOut(perp_deco_mk),
            run_time=1.0,
        )


# 运行命令:
# manim -pql 002_平行与垂直.py ParallelPerpendicularLesson   # 快速预览
# manim -qm  002_平行与垂直.py ParallelPerpendicularLesson   # 中等质量 (720p)
# manim -qh  002_平行与垂直.py ParallelPerpendicularLesson   # 高质量 (1080p)
