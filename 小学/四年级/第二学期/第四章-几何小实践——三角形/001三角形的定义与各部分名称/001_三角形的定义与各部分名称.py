"""
001_三角形的定义与各部分名称.py — 三角形的定义与各部分名称 教学动画

知识点: 三角形的定义与各部分名称
  - 定义: 由三条线段围成的图形(每相邻两条线段的端点相连)叫做三角形
  - 各部分: 三条边、三个角、三个顶点
  - 符号: △ 表示三角形，如 △ABC
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
BG_COLOR      = "#1a1a2e"
COLOR_TRI     = "#3b82f6"   # 蓝色  三角形主体
COLOR_VERTEX  = "#f59e0b"   # 橙色  顶点
COLOR_SIDE    = "#22c55e"   # 绿色  边
COLOR_ANGLE   = "#f472b6"   # 粉色  角
COLOR_HL      = "#fbbf24"   # 黄色  高亮
COLOR_AUTHOR  = "#6b7280"   # 灰色  作者信息
COLOR_SYMBOL  = "#a78bfa"   # 紫色  符号
FONT          = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class TriangleDefinitionLesson(Scene):
    """
    三角形的定义与各部分名称教学动画
    场景顺序:
      1. 开场钩子 — 三条线段能围成什么?
      2. 演示三角形的形成 — 逐步连接三点
      3. 三角形的定义
      4. 顶点 — 三个顶点 A、B、C
      5. 边   — 三条边 AB、BC、CA
      6. 角   — 三个角 ∠A、∠B、∠C
      7. 三角形符号 △ABC
      8. 知识总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_forming_triangle()
        self.scene_3_definition()
        self.scene_4_vertices()
        self.scene_5_sides()
        self.scene_6_angles()
        self.scene_7_symbol()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何坐标（精确计算，无臆想坐标）"""

        # ===== 主三角形顶点 =====
        # 设计一个清晰、美观的三角形，放置在屏幕中部
        self.SCALE  = 1.0
        self.OFFSET = np.array([0.0, 0.5, 0.0])

        # 原始坐标（无缩放无偏移）
        raw_A = np.array([-2.2, -1.6, 0.0])
        raw_B = np.array([ 2.2, -1.6, 0.0])
        raw_C = np.array([ 0.0,  2.0, 0.0])

        self.A = raw_A * self.SCALE + self.OFFSET
        self.B = raw_B * self.SCALE + self.OFFSET
        self.C = raw_C * self.SCALE + self.OFFSET

        # ===== 派生点（精确计算）=====
        self.centroid = (self.A + self.B + self.C) / 3

        # ===== 边长（精确计算）=====
        self.len_AB = np.linalg.norm(self.B - self.A)
        self.len_BC = np.linalg.norm(self.C - self.B)
        self.len_CA = np.linalg.norm(self.A - self.C)

        # ===== 角度（精确计算，弧度）=====
        self.angle_A = self._calc_angle(self.B, self.A, self.C)
        self.angle_B = self._calc_angle(self.A, self.B, self.C)
        self.angle_C = self._calc_angle(self.A, self.C, self.B)

        # ===== 验证 =====
        self._verify_geometry()

    def _calc_angle(self, P1, vertex, P2):
        """计算以 vertex 为顶点，P1-vertex-P2 的内角（弧度）"""
        v1 = P1 - vertex
        v2 = P2 - vertex
        cos_a = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_a = np.clip(cos_a, -1.0, 1.0)
        return np.arccos(cos_a)

    def _verify_geometry(self):
        """验证几何关系"""
        # 内角和应为 π
        angle_sum = self.angle_A + self.angle_B + self.angle_C
        assert abs(angle_sum - np.pi) < 1e-8, (
            f"内角和错误: {np.degrees(angle_sum):.4f}° ≠ 180°"
        )
        # 所有点在竖屏安全区内
        for pt, name in [(self.A, "A"), (self.B, "B"), (self.C, "C")]:
            assert abs(pt[0]) < 4.0, f"点{name} x 超界: {pt[0]}"
            assert abs(pt[1]) < 7.5, f"点{name} y 超界: {pt[1]}"
        print("Geometry verification passed.")

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        """创建作者标识"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_triangle(self, color=COLOR_TRI, stroke_width=4, fill_opacity=0.08):
        """创建主三角形 Polygon"""
        return Polygon(
            self.A, self.B, self.C,
            color=color,
            stroke_width=stroke_width,
            fill_color=color,
            fill_opacity=fill_opacity,
        )

    def make_vertex_dot(self, point, color=COLOR_VERTEX, radius=0.10):
        return Dot(point, color=color, radius=radius)

    def make_angle_arc(self, vertex, p1, p2, radius=0.45, color=COLOR_ANGLE):
        """在 vertex 处画从 p1 侧到 p2 侧的角弧（使用 from_three_points）"""
        # 计算叉积判断逆/顺时针
        v1 = p1 - vertex
        v2 = p2 - vertex
        cross_z = v1[0] * v2[1] - v1[1] * v2[0]
        return Angle.from_three_points(
            p1, vertex, p2,
            radius=radius,
            color=color,
            other_angle=(cross_z < 0),
        )

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者标识
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "三条线段能围成什么?",
            font=FONT, font_size=40, color=COLOR_HL,
        ).move_to(UP * 5.2)

        sub = Text(
            "今天认识一个最基本的几何图形!",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.4)

        self.play(Write(hook), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 快速展示三角形轮廓
        tri_preview = self.make_triangle(
            color=COLOR_TRI, stroke_width=5, fill_opacity=0.12
        ).move_to(DOWN * 0.5)

        self.play(Create(tri_preview), run_time=1.2)
        self.wait(0.6)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(sub), FadeOut(tri_preview),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 三角形的形成
    # ------------------------------------------------------------------

    def scene_2_forming_triangle(self):
        title = Text(
            "三条线段如何围成三角形?",
            font=FONT, font_size=32, color=WHITE,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 先画三个点
        dot_A = self.make_vertex_dot(self.A)
        dot_B = self.make_vertex_dot(self.B)
        dot_C = self.make_vertex_dot(self.C)

        label_A = Text("A", font=FONT, font_size=28, color=COLOR_VERTEX).next_to(self.A, DL, buff=0.2)
        label_B = Text("B", font=FONT, font_size=28, color=COLOR_VERTEX).next_to(self.B, DR, buff=0.2)
        label_C = Text("C", font=FONT, font_size=28, color=COLOR_VERTEX).next_to(self.C, UP, buff=0.2)

        self.play(
            FadeIn(dot_A), FadeIn(dot_B), FadeIn(dot_C),
            FadeIn(label_A), FadeIn(label_B), FadeIn(label_C),
            run_time=0.8,
        )

        hint = Text(
            "先定三个点",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(hint), run_time=0.4)
        self.wait(0.6)

        # 依次连接三条线段
        line_AB = Line(self.A, self.B, color=COLOR_SIDE, stroke_width=4)
        line_BC = Line(self.B, self.C, color=COLOR_SIDE, stroke_width=4)
        line_CA = Line(self.C, self.A, color=COLOR_SIDE, stroke_width=4)

        hint2 = Text(
            "相邻两点连线段",
            font=FONT, font_size=24, color=COLOR_SIDE,
        ).move_to(DOWN * 4.5)
        self.play(ReplacementTransform(hint, hint2), run_time=0.3)

        self.play(Create(line_AB), run_time=0.7)
        self.play(Create(line_BC), run_time=0.7)
        self.play(Create(line_CA), run_time=0.7)

        hint3 = Text(
            "三条线段首尾相连, 三角形形成!",
            font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(DOWN * 4.5)
        self.play(ReplacementTransform(hint2, hint3), run_time=0.4)

        # 填充
        tri_fill = self.make_triangle(fill_opacity=0.15, stroke_width=0)
        self.play(FadeIn(tri_fill), run_time=0.5)
        self.wait(1.5)

        # 清理 (保留三角形和顶点标签到下一场景)
        self.play(
            FadeOut(title), FadeOut(hint3), FadeOut(tri_fill),
            run_time=0.5,
        )
        # 保存供后续场景使用
        self._dots   = VGroup(dot_A, dot_B, dot_C)
        self._labels = VGroup(label_A, label_B, label_C)
        self._lines  = VGroup(line_AB, line_BC, line_CA)

    # ------------------------------------------------------------------
    # Scene 3: 三角形的定义
    # ------------------------------------------------------------------

    def scene_3_definition(self):
        title = Text(
            "三角形的定义",
            font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 定义文字（分两行）
        def_line1 = Text(
            "由三条线段围成的图形,",
            font=FONT, font_size=26, color=WHITE,
        )
        def_line2 = Text(
            "叫做三角形。",
            font=FONT, font_size=26, color=COLOR_TRI,
        )
        def_group = VGroup(def_line1, def_line2).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        def_group.move_to(DOWN * 3.6)

        # 补充说明
        note = Text(
            "（每相邻两条线段的端点相连）",
            font=FONT, font_size=20, color=GRAY_A,
        ).next_to(def_group, DOWN, buff=0.3)

        self.play(FadeIn(def_line1, shift=RIGHT * 0.3), run_time=0.6)
        self.play(FadeIn(def_line2, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(note), run_time=0.5)

        # 闪亮三条线段
        self.play(
            self._lines.animate.set_color(COLOR_HL),
            run_time=0.5,
        )
        self.play(
            self._lines.animate.set_color(COLOR_SIDE),
            run_time=0.5,
        )
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(def_group), FadeOut(note),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 4: 三个顶点
    # ------------------------------------------------------------------

    def scene_4_vertices(self):
        title = Text(
            "三个顶点",
            font=FONT, font_size=36, color=COLOR_VERTEX,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        explain = Text(
            "三条线段的端点叫做顶点",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(explain), run_time=0.5)

        # 逐一高亮三个顶点
        dot_A, dot_B, dot_C = self._dots
        label_A, label_B, label_C = self._labels

        # 顶点 A
        ring_A = Circle(radius=0.25, color=COLOR_VERTEX, stroke_width=3).move_to(self.A)
        v_label_A = Text("顶点 A", font=FONT, font_size=22, color=COLOR_VERTEX)
        v_label_A.move_to(self.A + np.array([-1.4, -0.5, 0.0]))

        self.play(
            dot_A.animate.set_color(COLOR_HL).scale(1.5),
            Create(ring_A),
            FadeIn(v_label_A),
            run_time=0.7,
        )
        self.wait(0.4)

        # 顶点 B
        ring_B = Circle(radius=0.25, color=COLOR_VERTEX, stroke_width=3).move_to(self.B)
        v_label_B = Text("顶点 B", font=FONT, font_size=22, color=COLOR_VERTEX)
        v_label_B.move_to(self.B + np.array([1.4, -0.5, 0.0]))

        self.play(
            dot_B.animate.set_color(COLOR_HL).scale(1.5),
            Create(ring_B),
            FadeIn(v_label_B),
            run_time=0.7,
        )
        self.wait(0.4)

        # 顶点 C
        ring_C = Circle(radius=0.25, color=COLOR_VERTEX, stroke_width=3).move_to(self.C)
        v_label_C = Text("顶点 C", font=FONT, font_size=22, color=COLOR_VERTEX)
        v_label_C.move_to(self.C + np.array([1.2, 0.2, 0.0]))

        self.play(
            dot_C.animate.set_color(COLOR_HL).scale(1.5),
            Create(ring_C),
            FadeIn(v_label_C),
            run_time=0.7,
        )
        self.wait(0.4)

        # 总结标注
        summary_v = Text(
            "共 3 个顶点",
            font=FONT, font_size=26, color=COLOR_HL,
        ).move_to(DOWN * 4.8)
        self.play(FadeIn(summary_v, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 还原点颜色
        self.play(
            dot_A.animate.set_color(COLOR_VERTEX).scale(1/1.5),
            dot_B.animate.set_color(COLOR_VERTEX).scale(1/1.5),
            dot_C.animate.set_color(COLOR_VERTEX).scale(1/1.5),
            FadeOut(ring_A), FadeOut(ring_B), FadeOut(ring_C),
            FadeOut(v_label_A), FadeOut(v_label_B), FadeOut(v_label_C),
            FadeOut(title), FadeOut(explain), FadeOut(summary_v),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 5: 三条边
    # ------------------------------------------------------------------

    def scene_5_sides(self):
        title = Text(
            "三条边",
            font=FONT, font_size=36, color=COLOR_SIDE,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        explain = Text(
            "连接两个顶点的线段叫做边",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(explain), run_time=0.5)

        line_AB, line_BC, line_CA = self._lines

        # 边 AB
        side_label_AB = Text("边 AB", font=FONT, font_size=22, color=COLOR_SIDE)
        side_label_AB.move_to((self.A + self.B) / 2 + DOWN * 0.4)

        self.play(
            line_AB.animate.set_color(COLOR_HL).set_stroke(width=7),
            FadeIn(side_label_AB),
            run_time=0.7,
        )
        self.wait(0.4)
        self.play(
            line_AB.animate.set_color(COLOR_SIDE).set_stroke(width=4),
            run_time=0.3,
        )

        # 边 BC
        mid_BC = (self.B + self.C) / 2
        side_label_BC = Text("边 BC", font=FONT, font_size=22, color=COLOR_SIDE)
        side_label_BC.move_to(mid_BC + RIGHT * 0.9)

        self.play(
            line_BC.animate.set_color(COLOR_HL).set_stroke(width=7),
            FadeIn(side_label_BC),
            run_time=0.7,
        )
        self.wait(0.4)
        self.play(
            line_BC.animate.set_color(COLOR_SIDE).set_stroke(width=4),
            run_time=0.3,
        )

        # 边 CA
        mid_CA = (self.C + self.A) / 2
        side_label_CA = Text("边 CA", font=FONT, font_size=22, color=COLOR_SIDE)
        side_label_CA.move_to(mid_CA + LEFT * 0.9)

        self.play(
            line_CA.animate.set_color(COLOR_HL).set_stroke(width=7),
            FadeIn(side_label_CA),
            run_time=0.7,
        )
        self.wait(0.4)
        self.play(
            line_CA.animate.set_color(COLOR_SIDE).set_stroke(width=4),
            run_time=0.3,
        )

        # 总结
        summary_s = Text(
            "共 3 条边",
            font=FONT, font_size=26, color=COLOR_HL,
        ).move_to(DOWN * 4.8)
        self.play(FadeIn(summary_s, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(explain), FadeOut(summary_s),
            FadeOut(side_label_AB), FadeOut(side_label_BC), FadeOut(side_label_CA),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 6: 三个角
    # ------------------------------------------------------------------

    def scene_6_angles(self):
        title = Text(
            "三个角",
            font=FONT, font_size=36, color=COLOR_ANGLE,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        explain = Text(
            "相邻两条边之间的夹角叫做角",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(DOWN * 3.8)
        self.play(FadeIn(explain), run_time=0.5)

        # 角 A (∠BAC)
        arc_A = self.make_angle_arc(self.A, self.B, self.C, radius=0.5)
        angle_label_A = Text("∠A", font=FONT, font_size=22, color=COLOR_ANGLE)
        # 放在角弧中间偏内一点
        bisect_A_dir = (
            (self.B - self.A) / np.linalg.norm(self.B - self.A)
            + (self.C - self.A) / np.linalg.norm(self.C - self.A)
        )
        bisect_A_dir /= np.linalg.norm(bisect_A_dir)
        angle_label_A.move_to(self.A + bisect_A_dir * 0.9)

        self.play(Create(arc_A), FadeIn(angle_label_A), run_time=0.7)
        self.wait(0.4)

        # 角 B (∠ABC)
        arc_B = self.make_angle_arc(self.B, self.A, self.C, radius=0.5)
        angle_label_B = Text("∠B", font=FONT, font_size=22, color=COLOR_ANGLE)
        bisect_B_dir = (
            (self.A - self.B) / np.linalg.norm(self.A - self.B)
            + (self.C - self.B) / np.linalg.norm(self.C - self.B)
        )
        bisect_B_dir /= np.linalg.norm(bisect_B_dir)
        angle_label_B.move_to(self.B + bisect_B_dir * 0.9)

        self.play(Create(arc_B), FadeIn(angle_label_B), run_time=0.7)
        self.wait(0.4)

        # 角 C (∠ACB)
        arc_C = self.make_angle_arc(self.C, self.A, self.B, radius=0.5)
        angle_label_C = Text("∠C", font=FONT, font_size=22, color=COLOR_ANGLE)
        bisect_C_dir = (
            (self.A - self.C) / np.linalg.norm(self.A - self.C)
            + (self.B - self.C) / np.linalg.norm(self.B - self.C)
        )
        bisect_C_dir /= np.linalg.norm(bisect_C_dir)
        angle_label_C.move_to(self.C + bisect_C_dir * 0.9)

        self.play(Create(arc_C), FadeIn(angle_label_C), run_time=0.7)
        self.wait(0.4)

        # 总结
        summary_a = Text(
            "共 3 个角",
            font=FONT, font_size=26, color=COLOR_HL,
        ).move_to(DOWN * 4.8)
        self.play(FadeIn(summary_a, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(explain), FadeOut(summary_a),
            FadeOut(arc_A), FadeOut(arc_B), FadeOut(arc_C),
            FadeOut(angle_label_A), FadeOut(angle_label_B), FadeOut(angle_label_C),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 三角形符号 △ABC
    # ------------------------------------------------------------------

    def scene_7_symbol(self):
        title = Text(
            "三角形的符号表示",
            font=FONT, font_size=34, color=COLOR_SYMBOL,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 符号 △ 介绍
        sym_intro = VGroup(
            Text("三角形用符号", font=FONT, font_size=26, color=WHITE),
            MathTex(r"\triangle", font_size=48, color=COLOR_SYMBOL),
            Text("表示", font=FONT, font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.5)

        self.play(FadeIn(sym_intro, shift=UP * 0.3), run_time=0.7)
        self.wait(0.8)

        # △ABC 示例
        sym_abc = VGroup(
            MathTex(r"\triangle", font_size=52, color=COLOR_SYMBOL),
            Text("ABC", font=FONT, font_size=48, color=COLOR_VERTEX),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 4.8)

        self.play(Write(sym_abc), run_time=0.8)

        # 箭头指向三顶点
        dot_A, dot_B, dot_C = self._dots
        label_A, label_B, label_C = self._labels

        # 高亮顶点 A B C 与符号对应
        self.play(
            dot_A.animate.set_color(COLOR_HL).scale(1.4),
            label_A.animate.set_color(COLOR_HL),
            run_time=0.5,
        )
        self.wait(0.3)
        self.play(
            dot_A.animate.set_color(COLOR_VERTEX).scale(1/1.4),
            label_A.animate.set_color(COLOR_VERTEX),
            dot_B.animate.set_color(COLOR_HL).scale(1.4),
            label_B.animate.set_color(COLOR_HL),
            run_time=0.5,
        )
        self.wait(0.3)
        self.play(
            dot_B.animate.set_color(COLOR_VERTEX).scale(1/1.4),
            label_B.animate.set_color(COLOR_VERTEX),
            dot_C.animate.set_color(COLOR_HL).scale(1.4),
            label_C.animate.set_color(COLOR_HL),
            run_time=0.5,
        )
        self.wait(0.3)
        self.play(
            dot_C.animate.set_color(COLOR_VERTEX).scale(1/1.4),
            label_C.animate.set_color(COLOR_VERTEX),
            run_time=0.4,
        )

        note_sym = Text(
            "读作: 三角形 ABC",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(DOWN * 6.0)
        self.play(FadeIn(note_sym), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sym_intro), FadeOut(sym_abc),
            FadeOut(note_sym),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 8: 知识总结
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        # 先淡出三角形和顶点
        self.play(
            FadeOut(self._dots),
            FadeOut(self._labels),
            FadeOut(self._lines),
            run_time=0.5,
        )

        title = Text(
            "知识总结",
            font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 总结卡片背景
        card_bg = RoundedRectangle(
            width=7.8, height=10.5,
            corner_radius=0.4,
            color=WHITE,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=0.05,
        ).move_to(UP * 0.5)
        self.play(FadeIn(card_bg), run_time=0.4)

        # 条目 1: 定义
        item1_title = Text("1. 三角形的定义", font=FONT, font_size=26, color=COLOR_TRI)
        item1_body = VGroup(
            Text("由三条线段围成的图形,", font=FONT, font_size=20, color=GRAY_A),
            Text("叫做三角形。", font=FONT, font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        item1 = VGroup(item1_title, item1_body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        item1.move_to(UP * 3.8 + LEFT * 0.2)
        self.play(FadeIn(item1, shift=RIGHT * 0.3), run_time=0.5)

        # 条目 2: 顶点
        item2_title = Text("2. 三个顶点", font=FONT, font_size=26, color=COLOR_VERTEX)
        item2_body = VGroup(
            Text("A、B、C 三个顶点", font=FONT, font_size=20, color=GRAY_A),
        )
        item2 = VGroup(item2_title, item2_body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        item2.move_to(UP * 2.2 + LEFT * 0.2)
        self.play(FadeIn(item2, shift=RIGHT * 0.3), run_time=0.5)

        # 条目 3: 边
        item3_title = Text("3. 三条边", font=FONT, font_size=26, color=COLOR_SIDE)
        item3_body = VGroup(
            Text("AB、BC、CA 三条边", font=FONT, font_size=20, color=GRAY_A),
        )
        item3 = VGroup(item3_title, item3_body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        item3.move_to(UP * 0.8 + LEFT * 0.2)
        self.play(FadeIn(item3, shift=RIGHT * 0.3), run_time=0.5)

        # 条目 4: 角
        item4_title = Text("4. 三个角", font=FONT, font_size=26, color=COLOR_ANGLE)
        item4_body = VGroup(
            Text("∠A、∠B、∠C 三个角", font=FONT, font_size=20, color=GRAY_A),
        )
        item4 = VGroup(item4_title, item4_body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        item4.move_to(DOWN * 0.6 + LEFT * 0.2)
        self.play(FadeIn(item4, shift=RIGHT * 0.3), run_time=0.5)

        # 条目 5: 符号
        item5_title = Text("5. 符号表示", font=FONT, font_size=26, color=COLOR_SYMBOL)
        item5_body = VGroup(
            MathTex(r"\triangle", font_size=36, color=COLOR_SYMBOL),
            Text("ABC  读作: 三角形ABC", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(RIGHT, buff=0.15)
        item5 = VGroup(item5_title, item5_body).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        item5.move_to(DOWN * 2.0 + LEFT * 0.2)
        self.play(FadeIn(item5, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(3.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(item1), FadeOut(item2), FadeOut(item3),
            FadeOut(item4), FadeOut(item5),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        # 放大作者信息
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
            "关注我, 学更多数学知识!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 三角形装饰
        deco_group = VGroup()
        for i in range(6):
            angle_val = i * PI / 3
            pos = DOWN * 3.0 + 2.2 * np.array([np.cos(angle_val), np.sin(angle_val), 0.0])
            mini_tri = Polygon(
                pos,
                pos + np.array([0.35, 0.0, 0.0]),
                pos + np.array([0.175, 0.3, 0.0]),
                color=COLOR_TRI,
                fill_opacity=0.7,
                stroke_width=0,
            )
            deco_group.add(mini_tri)

        self.play(*[FadeIn(d, scale=0.5) for d in deco_group], run_time=0.6)
        self.play(Rotate(deco_group, angle=PI, run_time=1.5))
        self.wait(1.2)

        # 全部淡出
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco_group),
            run_time=1.0,
        )


# 运行命令:
# manim -pql 001_三角形的定义与各部分名称.py TriangleDefinitionLesson   # 快速预览
# manim -qm  001_三角形的定义与各部分名称.py TriangleDefinitionLesson   # 中等质量 720p
# manim -qh  001_三角形的定义与各部分名称.py TriangleDefinitionLesson   # 高质量 1080p
