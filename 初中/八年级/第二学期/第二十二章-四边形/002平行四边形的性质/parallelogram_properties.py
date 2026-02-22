"""
平行四边形的性质 - 八年级数学教学动画
Parallelogram Properties - Grade 8 Math Teaching Animation

内容: 平行四边形的三大性质
目标观众: 八年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ParallelogramProperties(Scene):
    """
    平行四边形性质教学动画

    场景顺序:
    1. 开场介绍
    2. 性质① 对边平行且相等
    3. 性质② 对角相等，邻角互补
    4. 性质③ 对角线互相平分
    5. 总结
    6. 片尾关注
    """

    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PARA = "#4fc3f7"          # 蓝色 - 平行四边形主体
        self.COLOR_DIAG = "#ffd54f"          # 黄色 - 对角线
        self.COLOR_EQUAL_SIDE_H = "#a5d6a7"  # 绿色 - 相等水平边
        self.COLOR_EQUAL_SIDE_S = "#80cbc4"  # 青绿 - 相等斜边
        self.COLOR_ANGLE_A = "#ef9a9a"       # 红色 - ∠A∠C（对角）
        self.COLOR_ANGLE_B = "#ce93d8"       # 紫色 - ∠B∠D（对角）
        self.COLOR_MIDPOINT = "#ffb74d"      # 橙色 - 中点/交点
        self.COLOR_HIGHLIGHT = YELLOW

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_parallel_equal_sides()
        self.scene_3_angles()
        self.scene_4_diagonals()
        self.scene_5_summary()
        self.scene_6_outro()

    # =========================================================
    # 几何初始化
    # =========================================================
    def setup_geometry(self):
        """统一初始化所有几何元素坐标"""
        # 平行四边形 ABCD 顶点（精确保证平行关系）
        # AB ∥ CD（水平方向），AD ∥ BC（斜方向）
        # 主体放在屏幕中部略偏上，留出底部文字区域

        OFFSET = UP * 1.2

        # 顶点定义（保证 AB∥CD, AD∥BC）
        # A, B 在下方；D, C 在上方
        # AB 方向向量 [4, 0]，AD 方向向量 [1, 2.4]
        self.A = np.array([-2.5, -1.2, 0]) + OFFSET
        self.B = np.array([1.5, -1.2, 0]) + OFFSET
        self.C = np.array([2.5, 1.2, 0]) + OFFSET
        self.D = np.array([-1.5, 1.2, 0]) + OFFSET

        # 精确计算对角线交点（两对角线中点重合，即互相平分）
        self.O = (self.A + self.C) / 2  # = (B + D) / 2

        # 边向量（用于验证）
        self.vec_AB = self.B - self.A   # [4, 0, 0]
        self.vec_DC = self.C - self.D   # [4, 0, 0] ← 与 AB 相同
        self.vec_AD = self.D - self.A   # [1, 2.4, 0]
        self.vec_BC = self.C - self.B   # [1, 2.4, 0] ← 与 AD 相同

        # 边长
        self.len_AB = np.linalg.norm(self.vec_AB)  # = 4.0
        self.len_AD = np.linalg.norm(self.vec_AD)  # ≈ 2.6

        # 角度值（用于 Manim Angle 参数）
        # 经过验证：∠A = ∠C ≈ 67.4°，∠B = ∠D ≈ 112.6°
        # 所有角度叉积为负（顺时针），需要 other_angle=True

    # =========================================================
    # 辅助方法
    # =========================================================
    def make_parallelogram(self, color=None, stroke_width=3, fill_opacity=0.08):
        """创建平行四边形对象"""
        if color is None:
            color = self.COLOR_PARA
        return Polygon(
            self.A, self.B, self.C, self.D,
            color=color,
            stroke_width=stroke_width,
            fill_color=color,
            fill_opacity=fill_opacity
        )

    def make_vertex_labels(self):
        """创建顶点标签 A, B, C, D"""
        label_A = MathTex("A", color=WHITE, font_size=32).next_to(
            self.A, DL, buff=0.12
        )
        label_B = MathTex("B", color=WHITE, font_size=32).next_to(
            self.B, DR, buff=0.12
        )
        label_C = MathTex("C", color=WHITE, font_size=32).next_to(
            self.C, UR, buff=0.12
        )
        label_D = MathTex("D", color=WHITE, font_size=32).next_to(
            self.D, UL, buff=0.12
        )
        return VGroup(label_A, label_B, label_C, label_D)

    def make_angle_arc(self, vertex, p1, p2, color, radius=0.45, other_angle=True):
        """
        创建角弧
        vertex: 顶点
        p1, p2: 角的两条边上的点（从 p1 到顶点到 p2）
        other_angle=True 因为验证结果显示所有角叉积为负
        """
        line1 = Line(vertex, p1)
        line2 = Line(vertex, p2)
        return Angle(
            line1, line2,
            radius=radius,
            color=color,
            stroke_width=2.5,
            other_angle=other_angle
        )

    def make_tick_mark(self, p1, p2, n_ticks=1, color=WHITE, tick_size=0.18):
        """在线段中点处创建刻度标记（表示相等）"""
        mid = (p1 + p2) / 2
        direction = p2 - p1
        direction_norm = direction / np.linalg.norm(direction)
        perp = np.array([-direction_norm[1], direction_norm[0], 0])

        marks = VGroup()
        spacing = tick_size * 0.4
        offsets = np.linspace(-(n_ticks - 1) * spacing / 2, (n_ticks - 1) * spacing / 2, n_ticks)

        for offset in offsets:
            start_pt = mid + offset * direction_norm - perp * tick_size / 2
            end_pt = mid + offset * direction_norm + perp * tick_size / 2
            marks.add(Line(start_pt, end_pt, color=color, stroke_width=2.5))

        return marks

    def make_parallel_arrow(self, p1, p2, color=WHITE, n_arrows=1):
        """在线段中点处创建平行箭头标记"""
        mid = (p1 + p2) / 2
        direction = p2 - p1
        direction_norm = direction / np.linalg.norm(direction)

        marks = VGroup()
        spacing = 0.2
        offsets = np.linspace(-(n_arrows - 1) * spacing / 2, (n_arrows - 1) * spacing / 2, n_arrows)

        for offset in offsets:
            pos = mid + offset * direction_norm
            arrow = Arrow(
                pos - direction_norm * 0.12,
                pos + direction_norm * 0.12,
                buff=0,
                color=color,
                stroke_width=2,
                tip_length=0.12,
                max_stroke_width_to_length_ratio=50
            )
            marks.add(arrow)
        return marks

    def make_section_title(self, text_str, color=YELLOW, y_pos=5.8):
        """创建场景标题"""
        return Text(
            text_str,
            font="Noto Sans CJK SC",
            font_size=34,
            color=color
        ).move_to(UP * y_pos)

    def make_formula_text(self, formula_str, y_pos, color=WHITE):
        """创建公式（MathTex）"""
        return MathTex(formula_str, color=color, font_size=30).move_to(UP * y_pos)

    def make_chinese_text(self, text_str, y_pos, color=GRAY_A, font_size=22):
        """创建中文说明文字"""
        return Text(
            text_str,
            font="Noto Sans CJK SC",
            font_size=font_size,
            color=color
        ).move_to(UP * y_pos)

    # =========================================================
    # Scene 1: 开场
    # =========================================================
    def scene_1_opening(self):
        """场景1: 开场钩子"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7.3)

        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 章节标签
        chapter_tag = Text(
            "八年级 · 第二十二章",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_B
        ).move_to(UP * 6.8)

        self.play(FadeIn(chapter_tag, shift=DOWN * 0.1), run_time=0.3)

        # 主标题
        main_title = Text(
            "平行四边形的性质",
            font="Noto Sans CJK SC",
            font_size=44,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 6.1)

        self.play(Write(main_title), run_time=0.9)

        # 三大性质提示
        hint = Text(
            "3个核心性质，掌握解题利器！",
            font="Noto Sans CJK SC",
            font_size=25,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.3)

        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)

        # 创建并展示平行四边形
        self.para = self.make_parallelogram()
        self.vertex_labels = self.make_vertex_labels()

        self.play(Create(self.para), run_time=1.0)
        self.play(Write(self.vertex_labels), run_time=0.6)
        self.wait(0.8)

        # 清除标题文字，保留图形
        self.play(
            FadeOut(main_title),
            FadeOut(hint),
            FadeOut(chapter_tag),
            run_time=0.5
        )

    # =========================================================
    # Scene 2: 性质① 对边平行且相等
    # =========================================================
    def scene_2_parallel_equal_sides(self):
        """场景2: 性质① 对边平行且相等"""

        # 标题
        title = self.make_section_title("性质①  对边平行且相等", color=self.COLOR_EQUAL_SIDE_H)
        self.play(Write(title), run_time=0.7)

        # --- Step 1: 高亮 AB 和 CD（水平对边）---
        explain_1 = self.make_chinese_text("AB 和 CD 是一对对边", y_pos=-4.2)
        self.play(FadeIn(explain_1), run_time=0.4)

        # 高亮两条水平边
        line_AB = Line(self.A, self.B, color=self.COLOR_EQUAL_SIDE_H, stroke_width=5)
        line_CD = Line(self.C, self.D, color=self.COLOR_EQUAL_SIDE_H, stroke_width=5)

        self.play(Create(line_AB), Create(line_CD), run_time=0.7)

        # 平行符号（箭头）
        arrow_AB = self.make_parallel_arrow(self.A, self.B, color=self.COLOR_EQUAL_SIDE_H)
        arrow_CD = self.make_parallel_arrow(self.D, self.C, color=self.COLOR_EQUAL_SIDE_H)

        self.play(FadeIn(arrow_AB), FadeIn(arrow_CD), run_time=0.4)

        # 相等刻度
        tick_AB = self.make_tick_mark(self.A, self.B, n_ticks=1, color=self.COLOR_EQUAL_SIDE_H)
        tick_CD = self.make_tick_mark(self.D, self.C, n_ticks=1, color=self.COLOR_EQUAL_SIDE_H)

        self.play(FadeIn(tick_AB), FadeIn(tick_CD), run_time=0.4)
        self.play(FadeOut(explain_1), run_time=0.3)

        # 公式
        formula_1 = self.make_formula_text(
            r"AB \parallel CD \quad \text{and} \quad AB = CD",
            y_pos=-4.2,
            color=self.COLOR_EQUAL_SIDE_H
        )
        # 注意：\text{且} 可能有问题，改用两行
        formula_1a = MathTex(
            r"AB \parallel CD",
            color=self.COLOR_EQUAL_SIDE_H,
            font_size=30
        ).move_to(UP * -4.0)
        formula_1b = MathTex(
            r"AB = CD",
            color=self.COLOR_EQUAL_SIDE_H,
            font_size=30
        ).move_to(UP * -4.6)

        self.play(Write(formula_1a), Write(formula_1b), run_time=0.6)
        self.wait(0.7)

        # --- Step 2: 高亮 AD 和 BC（斜边对边）---
        line_AD = Line(self.A, self.D, color=self.COLOR_EQUAL_SIDE_S, stroke_width=5)
        line_BC = Line(self.B, self.C, color=self.COLOR_EQUAL_SIDE_S, stroke_width=5)

        self.play(
            line_AB.animate.set_color(self.COLOR_PARA).set_stroke(width=3),
            line_CD.animate.set_color(self.COLOR_PARA).set_stroke(width=3),
            FadeOut(formula_1a),
            FadeOut(formula_1b),
            run_time=0.5
        )

        self.play(Create(line_AD), Create(line_BC), run_time=0.7)

        # 双箭头（平行标记）
        arrow_AD = self.make_parallel_arrow(self.A, self.D, color=self.COLOR_EQUAL_SIDE_S, n_arrows=2)
        arrow_BC = self.make_parallel_arrow(self.B, self.C, color=self.COLOR_EQUAL_SIDE_S, n_arrows=2)

        self.play(FadeIn(arrow_AD), FadeIn(arrow_BC), run_time=0.4)

        # 双刻度（相等标记）
        tick_AD = self.make_tick_mark(self.A, self.D, n_ticks=2, color=self.COLOR_EQUAL_SIDE_S)
        tick_BC = self.make_tick_mark(self.B, self.C, n_ticks=2, color=self.COLOR_EQUAL_SIDE_S)

        self.play(FadeIn(tick_AD), FadeIn(tick_BC), run_time=0.4)

        formula_2a = MathTex(
            r"AD \parallel BC",
            color=self.COLOR_EQUAL_SIDE_S,
            font_size=30
        ).move_to(UP * -4.0)
        formula_2b = MathTex(
            r"AD = BC",
            color=self.COLOR_EQUAL_SIDE_S,
            font_size=30
        ).move_to(UP * -4.6)

        self.play(Write(formula_2a), Write(formula_2b), run_time=0.6)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line_AB), FadeOut(line_CD),
            FadeOut(line_AD), FadeOut(line_BC),
            FadeOut(arrow_AB), FadeOut(arrow_CD),
            FadeOut(arrow_AD), FadeOut(arrow_BC),
            FadeOut(tick_AB), FadeOut(tick_CD),
            FadeOut(tick_AD), FadeOut(tick_BC),
            FadeOut(formula_2a), FadeOut(formula_2b),
            run_time=0.5
        )

    # =========================================================
    # Scene 3: 性质② 对角相等，邻角互补
    # =========================================================
    def scene_3_angles(self):
        """场景3: 性质② 对角相等，邻角互补"""

        title = self.make_section_title("性质②  对角相等，邻角互补", color=self.COLOR_ANGLE_A)
        self.play(Write(title), run_time=0.7)

        # --- Step 1: 展示 ∠A 和 ∠C（对角相等）---
        explain_a = self.make_chinese_text("∠A 和 ∠C 是对角", y_pos=-4.2)
        self.play(FadeIn(explain_a), run_time=0.4)

        # ∠A 的角弧（顶点A，从D侧到B侧）
        # 验证：所有角 other_angle=True
        arc_A = self.make_angle_arc(
            self.A, self.D, self.B,
            color=self.COLOR_ANGLE_A,
            radius=0.45,
            other_angle=True
        )
        arc_A.set_fill(self.COLOR_ANGLE_A, opacity=0.2)

        # ∠C 的角弧（顶点C，从B侧到D侧）
        arc_C = self.make_angle_arc(
            self.C, self.B, self.D,
            color=self.COLOR_ANGLE_A,
            radius=0.45,
            other_angle=True
        )
        arc_C.set_fill(self.COLOR_ANGLE_A, opacity=0.2)

        self.play(Create(arc_A), Create(arc_C), run_time=0.8)
        self.play(FadeOut(explain_a), run_time=0.3)

        # 闪烁强调相等
        self.play(
            arc_A.animate.set_color(self.COLOR_HIGHLIGHT),
            arc_C.animate.set_color(self.COLOR_HIGHLIGHT),
            run_time=0.3
        )
        self.play(
            arc_A.animate.set_color(self.COLOR_ANGLE_A),
            arc_C.animate.set_color(self.COLOR_ANGLE_A),
            run_time=0.3
        )

        formula_ac = MathTex(
            r"\angle A = \angle C",
            color=self.COLOR_ANGLE_A,
            font_size=34
        ).move_to(UP * -4.2)
        self.play(Write(formula_ac), run_time=0.5)
        self.wait(0.6)

        # --- Step 2: 展示 ∠B 和 ∠D（对角相等）---
        explain_b = self.make_chinese_text("∠B 和 ∠D 是对角", y_pos=-4.8)
        self.play(FadeIn(explain_b), run_time=0.3)

        # ∠B 的角弧（顶点B，从A侧到C侧）
        arc_B = self.make_angle_arc(
            self.B, self.A, self.C,
            color=self.COLOR_ANGLE_B,
            radius=0.45,
            other_angle=True
        )
        arc_B.set_fill(self.COLOR_ANGLE_B, opacity=0.2)

        # ∠D 的角弧（顶点D，从C侧到A侧）
        arc_D = self.make_angle_arc(
            self.D, self.C, self.A,
            color=self.COLOR_ANGLE_B,
            radius=0.45,
            other_angle=True
        )
        arc_D.set_fill(self.COLOR_ANGLE_B, opacity=0.2)

        self.play(Create(arc_B), Create(arc_D), run_time=0.8)
        self.play(FadeOut(explain_b), run_time=0.3)

        formula_bd = MathTex(
            r"\angle B = \angle D",
            color=self.COLOR_ANGLE_B,
            font_size=34
        ).move_to(UP * -4.8)
        self.play(Write(formula_bd), run_time=0.5)
        self.wait(0.6)

        # --- Step 3: 邻角互补 ∠A + ∠B = 180° ---
        explain_supp = self.make_chinese_text(
            "∠A 和 ∠B 是邻角，它们互补！",
            y_pos=-4.2,
            color=self.COLOR_HIGHLIGHT
        )
        self.play(
            FadeOut(formula_ac),
            FadeOut(formula_bd),
            run_time=0.3
        )
        self.play(FadeIn(explain_supp), run_time=0.4)

        # 高亮 ∠A 和 ∠B
        self.play(
            arc_A.animate.set_color(self.COLOR_ANGLE_A).set_stroke(width=3),
            arc_B.animate.set_color(self.COLOR_ANGLE_B).set_stroke(width=3),
            arc_C.animate.set_opacity(0.3),
            arc_D.animate.set_opacity(0.3),
            run_time=0.5
        )

        formula_supp = MathTex(
            r"\angle A + \angle B = 180^{\circ}",
            color=self.COLOR_HIGHLIGHT,
            font_size=34
        ).move_to(UP * -4.8)
        self.play(FadeOut(explain_supp), run_time=0.3)
        self.play(Write(formula_supp), run_time=0.7)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(arc_A), FadeOut(arc_B),
            FadeOut(arc_C), FadeOut(arc_D),
            FadeOut(formula_supp),
            run_time=0.5
        )

    # =========================================================
    # Scene 4: 性质③ 对角线互相平分
    # =========================================================
    def scene_4_diagonals(self):
        """场景4: 性质③ 对角线互相平分"""

        title = self.make_section_title("性质③  对角线互相平分", color=self.COLOR_DIAG)
        self.play(Write(title), run_time=0.7)

        # 绘制对角线 AC 和 BD
        diag_AC = DashedLine(
            self.A, self.C,
            color=self.COLOR_DIAG,
            dash_length=0.15,
            stroke_width=2.5
        )
        diag_BD = DashedLine(
            self.B, self.D,
            color=self.COLOR_DIAG,
            dash_length=0.15,
            stroke_width=2.5
        )

        explain_diag = self.make_chinese_text("连接两条对角线", y_pos=-4.2)
        self.play(FadeIn(explain_diag), run_time=0.3)

        self.play(Create(diag_AC), run_time=0.7)
        self.play(Create(diag_BD), run_time=0.7)
        self.play(FadeOut(explain_diag), run_time=0.3)

        # 交点 O 出现
        O_dot = Dot(self.O, radius=0.12, color=self.COLOR_MIDPOINT)
        O_label = MathTex("O", color=self.COLOR_MIDPOINT, font_size=30).next_to(
            self.O, UR, buff=0.15
        )

        self.play(FadeIn(O_dot, scale=0.3), run_time=0.4)
        self.play(Flash(O_dot, color=self.COLOR_MIDPOINT, flash_radius=0.35), run_time=0.4)
        self.play(Write(O_label), run_time=0.4)

        # --- Step 1: OA = OC ---
        explain_oa = self.make_chinese_text("对角线 AC 被 O 平分", y_pos=-4.2)
        self.play(FadeIn(explain_oa), run_time=0.4)

        # 高亮 OA 和 OC 段
        seg_OA = Line(self.O, self.A, color=self.COLOR_ANGLE_A, stroke_width=5)
        seg_OC = Line(self.O, self.C, color=self.COLOR_ANGLE_A, stroke_width=5)

        self.play(Create(seg_OA), Create(seg_OC), run_time=0.6)

        # 等号刻度
        tick_OA = self.make_tick_mark(self.O, self.A, n_ticks=1, color=self.COLOR_ANGLE_A)
        tick_OC = self.make_tick_mark(self.O, self.C, n_ticks=1, color=self.COLOR_ANGLE_A)
        self.play(FadeIn(tick_OA), FadeIn(tick_OC), run_time=0.4)
        self.play(FadeOut(explain_oa), run_time=0.3)

        formula_oa = MathTex(
            r"OA = OC",
            color=self.COLOR_ANGLE_A,
            font_size=34
        ).move_to(UP * -4.2)
        self.play(Write(formula_oa), run_time=0.5)
        self.wait(0.5)

        # --- Step 2: OB = OD ---
        explain_ob = self.make_chinese_text("对角线 BD 被 O 平分", y_pos=-4.8)
        self.play(FadeIn(explain_ob), run_time=0.4)

        seg_OB = Line(self.O, self.B, color=self.COLOR_ANGLE_B, stroke_width=5)
        seg_OD = Line(self.O, self.D, color=self.COLOR_ANGLE_B, stroke_width=5)

        self.play(Create(seg_OB), Create(seg_OD), run_time=0.6)

        tick_OB = self.make_tick_mark(self.O, self.B, n_ticks=2, color=self.COLOR_ANGLE_B)
        tick_OD = self.make_tick_mark(self.O, self.D, n_ticks=2, color=self.COLOR_ANGLE_B)
        self.play(FadeIn(tick_OB), FadeIn(tick_OD), run_time=0.4)
        self.play(FadeOut(explain_ob), run_time=0.3)

        formula_ob = MathTex(
            r"OB = OD",
            color=self.COLOR_ANGLE_B,
            font_size=34
        ).move_to(UP * -4.8)
        self.play(Write(formula_ob), run_time=0.5)
        self.wait(1.2)

        # 保存这些元素（总结场景用）
        self.diag_AC = diag_AC
        self.diag_BD = diag_BD
        self.O_dot = O_dot
        self.O_label = O_label

        # 清理文字和分段线，保留对角线和O
        self.play(
            FadeOut(title),
            FadeOut(seg_OA), FadeOut(seg_OC),
            FadeOut(seg_OB), FadeOut(seg_OD),
            FadeOut(tick_OA), FadeOut(tick_OC),
            FadeOut(tick_OB), FadeOut(tick_OD),
            FadeOut(formula_oa), FadeOut(formula_ob),
            run_time=0.5
        )

    # =========================================================
    # Scene 5: 总结
    # =========================================================
    def scene_5_summary(self):
        """场景5: 三大性质汇总"""

        summary_title = Text(
            "三大性质 · 总结",
            font="Noto Sans CJK SC",
            font_size=38,
            color=GOLD,
            weight=BOLD
        ).move_to(UP * 6.1)

        self.play(Write(summary_title), run_time=0.6)

        # 将图形移动缩小到上方
        target_para = self.make_parallelogram(stroke_width=2, fill_opacity=0.05)
        target_para.scale(0.65).move_to(UP * 4.5)

        self.play(
            Transform(self.para, target_para),
            FadeOut(self.vertex_labels),
            FadeOut(self.diag_AC),
            FadeOut(self.diag_BD),
            FadeOut(self.O_dot),
            FadeOut(self.O_label),
            run_time=0.8
        )

        # 三大性质卡片
        card_data = [
            {
                "num": "①",
                "title": "对边平行且相等",
                "formula1": r"AB \parallel CD,\; AB = CD",
                "formula2": r"AD \parallel BC,\; AD = BC",
                "color": self.COLOR_EQUAL_SIDE_H,
                "y": 2.8
            },
            {
                "num": "②",
                "title": "对角相等，邻角互补",
                "formula1": r"\angle A = \angle C,\; \angle B = \angle D",
                "formula2": r"\angle A + \angle B = 180^{\circ}",
                "color": self.COLOR_ANGLE_A,
                "y": 0.5
            },
            {
                "num": "③",
                "title": "对角线互相平分",
                "formula1": r"OA = OC",
                "formula2": r"OB = OD",
                "color": self.COLOR_DIAG,
                "y": -1.8
            },
        ]

        cards = []
        for data in card_data:
            # 编号 + 标题
            num_text = Text(
                data["num"],
                font="Noto Sans CJK SC",
                font_size=28,
                color=data["color"],
                weight=BOLD
            )
            title_text = Text(
                data["title"],
                font="Noto Sans CJK SC",
                font_size=24,
                color=data["color"]
            )
            header = VGroup(num_text, title_text).arrange(RIGHT, buff=0.2)
            header.move_to(RIGHT * 0 + UP * data["y"])

            # 公式
            f1 = MathTex(data["formula1"], color=WHITE, font_size=24)
            f2 = MathTex(data["formula2"], color=WHITE, font_size=24)
            formulas = VGroup(f1, f2).arrange(DOWN, buff=0.12)
            formulas.next_to(header, DOWN, buff=0.15)

            # 背景框
            bg = RoundedRectangle(
                corner_radius=0.2,
                width=7.8,
                height=1.65,
                color=data["color"],
                fill_opacity=0.08,
                stroke_width=1.5
            ).move_to(UP * (data["y"] - 0.18))

            card = VGroup(bg, header, formulas)
            cards.append(card)

        # 依次显示卡片
        for card in cards:
            self.play(
                FadeIn(card, shift=RIGHT * 0.3),
                run_time=0.6
            )
            self.wait(0.3)

        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(summary_title),
            FadeOut(self.para),
            *[FadeOut(c) for c in cards],
            run_time=0.6
        )

    # =========================================================
    # Scene 6: 片尾
    # =========================================================
    def scene_6_outro(self):
        """场景6: 片尾 - 关注引导"""

        # 背景装饰：小平行四边形
        deco_paras = VGroup()
        positions = [UP * 4 + LEFT * 3, UP * 2 + RIGHT * 3.5, DOWN * 1 + LEFT * 3.5,
                     DOWN * 3.5 + RIGHT * 3, UP * 5.5 + RIGHT * 2]
        colors = [self.COLOR_EQUAL_SIDE_H, self.COLOR_ANGLE_A, self.COLOR_DIAG,
                  self.COLOR_ANGLE_B, self.COLOR_MIDPOINT]

        for pos, col in zip(positions, colors):
            mini = Polygon(
                np.array([-0.4, -0.15, 0]),
                np.array([0.3, -0.15, 0]),
                np.array([0.4, 0.15, 0]),
                np.array([-0.3, 0.15, 0]),
                color=col,
                fill_opacity=0.3,
                stroke_width=1.5
            ).move_to(pos)
            deco_paras.add(mini)

        self.play(
            *[FadeIn(d, scale=0.5) for d in deco_paras],
            run_time=0.6
        )

        # 作者名（放大居中）
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=38,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=28,
            color=GRAY_B
        ).move_to(UP * 0.6)

        self.play(
            Transform(self.author_info, author_name),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        # 关注引导
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 三大性质小标语
        tagline = Text(
            "对边平行相等 · 对角相等邻角补 · 对角线平分",
            font="Noto Sans CJK SC",
            font_size=18,
            color=GRAY_B
        ).move_to(DOWN * 1.8)

        self.play(FadeIn(tagline), run_time=0.5)

        # 装饰性动画
        self.play(Rotate(deco_paras, angle=PI / 6, run_time=1.2))

        self.wait(1.0)

        # 最终淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(tagline),
            FadeOut(deco_paras),
            run_time=1.0
        )


# =============================================
# 运行命令:
# 快速预览: manim -pql parallelogram_properties.py ParallelogramProperties
# 高质量:   manim -qh  parallelogram_properties.py ParallelogramProperties
# =============================================