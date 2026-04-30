"""
等腰三角形的判定 - Manim教学动画
七年级数学 第十四章

内容: 等腰三角形的两种判定方法
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ====== 全局配置 TikTok竖屏 ======
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class IsoscelesTriangleDetermination(Scene):
    """
    等腰三角形判定教学动画

    场景顺序:
    1. 开场钩子
    2. 判定方法一：定义法（两边相等）
    3. 过渡：等边对等角回顾
    4. 判定方法二：等角对等边
    5. 例题练习
    6. 总结+片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_TRIANGLE = WHITE
        self.COLOR_EQUAL_SIDE = "#e74c3c"    # 红色 - 等边
        self.COLOR_EQUAL_ANGLE = "#3498db"   # 蓝色 - 等角
        self.COLOR_HIGHLIGHT = "#f1c40f"     # 金色 - 高亮
        self.COLOR_SUCCESS = "#2ecc71"       # 绿色 - 成功判定
        self.COLOR_AUX = "#95a5a6"           # 灰色 - 辅助

        # 初始化几何数据
        self.setup_geometry()

        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_method1_definition()
        self.scene_3_transition_property()
        self.scene_4_method2_equal_angles()
        self.scene_5_example()
        self.scene_6_summary_outro()

    def setup_geometry(self):
        """统一初始化所有几何数据"""
        self.SCALE = 1.2
        self.OFFSET = np.array([0, 1.0, 0])

        # 等腰三角形顶点 (A为顶角，位于顶部中央)
        A_raw = np.array([0, 2.5, 0])
        B_raw = np.array([-2.0, -0.5, 0])
        C_raw = np.array([2.0, -0.5, 0])

        self.A = A_raw * self.SCALE + self.OFFSET
        self.B = B_raw * self.SCALE + self.OFFSET
        self.C = C_raw * self.SCALE + self.OFFSET

        # 边长
        self.AB_len = np.linalg.norm(self.B - self.A)
        self.AC_len = np.linalg.norm(self.C - self.A)
        self.BC_len = np.linalg.norm(self.C - self.B)

        # 角度
        self.angle_A_val = self._angle_at(self.B, self.A, self.C)
        self.angle_B_val = self._angle_at(self.A, self.B, self.C)
        self.angle_C_val = self._angle_at(self.A, self.C, self.B)

        # 验证等腰性质
        assert abs(self.AB_len - self.AC_len) < 1e-6, "等腰三角形AB≠AC"
        assert abs(self.angle_B_val - self.angle_C_val) < 1e-6, "等腰三角形∠B≠∠C"

        print(f"✓ 等腰三角形验证通过: AB=AC={self.AB_len:.3f}, 角B=角C={np.degrees(self.angle_B_val):.1f}deg")

    def _angle_at(self, P1, vertex, P2):
        """计算∠P1-vertex-P2的角度（弧度）"""
        v1 = P1 - vertex
        v2 = P2 - vertex
        cos_a = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        return np.arccos(np.clip(cos_a, -1.0, 1.0))

    def _create_triangle(self, color=WHITE, stroke_width=3):
        """创建三角形多边形"""
        return Polygon(self.A, self.B, self.C,
                      color=color, stroke_width=stroke_width,
                      fill_opacity=0)

    def _create_tick_mark(self, P1, P2, n=1, color=RED, size=0.18):
        """在线段P1P2中点创建等长刻度标记（单/双/三刻线）"""
        mid = (P1 + P2) / 2
        direction = P2 - P1
        direction = direction / np.linalg.norm(direction)
        perp = np.array([-direction[1], direction[0], 0])

        marks = VGroup()
        offsets = []
        if n == 1:
            offsets = [0]
        elif n == 2:
            offsets = [-size * 0.25, size * 0.25]
        elif n == 3:
            offsets = [-size * 0.35, 0, size * 0.35]

        for offset in offsets:
            tick = Line(
                mid + offset * direction - perp * size / 2,
                mid + offset * direction + perp * size / 2,
                color=color, stroke_width=3
            )
            marks.add(tick)
        return marks

    def _create_angle_arc(self, vertex, P1, P2, radius=0.45, color=BLUE,
                          other_angle=False, label_text=None, label_scale=0.7):
        """创建角弧，使用叉积自动判断方向"""
        # 用叉积判断是否需要 other_angle
        v1 = P1 - vertex
        v2 = P2 - vertex
        cross_z = v1[0] * v2[1] - v1[1] * v2[0]

        # 如果外部指定了 other_angle，直接用；否则自动判断
        line1 = Line(vertex, P1)
        line2 = Line(vertex, P2)

        arc = Angle(line1, line2, radius=radius, color=color,
                    other_angle=other_angle, stroke_width=3)

        group = VGroup(arc)

        if label_text:
            # 角平分线方向放置标签
            v1_unit = v1 / np.linalg.norm(v1)
            v2_unit = v2 / np.linalg.norm(v2)
            bisector = v1_unit + v2_unit
            if np.linalg.norm(bisector) > 1e-6:
                bisector = bisector / np.linalg.norm(bisector)
            else:
                bisector = v1_unit

            label_pos = vertex + bisector * (radius + 0.3)
            label = MathTex(label_text, color=color).scale(label_scale)
            label.move_to(label_pos)
            group.add(label)

        return group

    # ============================================================
    # Scene 1: 开场钩子
    # ============================================================
    def scene_1_opening(self):
        """开场：引出问题"""
        # 作者信息（顶部）
        self.author_bar = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_AUX
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.4)

        # 章节标签
        chapter_tag = Text(
            "七年级 · 第十四章 · 三角形",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_AUX
        ).move_to(UP * 6.3)
        self.play(FadeIn(chapter_tag), run_time=0.4)

        # 主标题
        title = Text(
            "等腰三角形的判定",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.3)
        self.play(Write(title), run_time=0.8)

        # 问题钩子
        hook_q = Text(
            "怎样判断一个三角形",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 4.3)
        hook_q2 = Text(
            "是等腰三角形？",
            font="PingFang SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 3.7)

        self.play(FadeIn(hook_q), FadeIn(hook_q2), run_time=0.6)

        # 简单三角形展示
        triangle = self._create_triangle(color=self.COLOR_TRIANGLE)
        self.play(Create(triangle), run_time=1.0)

        # 两个问号强调
        q1 = Text("?", font_size=48, color=self.COLOR_HIGHLIGHT).move_to(
            (self.A + self.B) / 2 + LEFT * 0.4 + UP * 0.2)
        q2 = Text("?", font_size=48, color=self.COLOR_HIGHLIGHT).move_to(
            (self.A + self.C) / 2 + RIGHT * 0.4 + UP * 0.2)

        self.play(
            FadeIn(q1, scale=0.5),
            FadeIn(q2, scale=0.5),
            run_time=0.5
        )
        self.wait(0.8)

        # 清理开场元素
        self.play(
            FadeOut(chapter_tag),
            FadeOut(title),
            FadeOut(hook_q),
            FadeOut(hook_q2),
            FadeOut(q1),
            FadeOut(q2),
            FadeOut(triangle),
            run_time=0.5
        )

    # ============================================================
    # Scene 2: 判定方法一 - 定义法
    # ============================================================
    def scene_2_method1_definition(self):
        """判定方法一：两边相等 → 等腰三角形"""
        # 方法标题
        method_tag = Text(
            "判定方法一",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 6.3)

        method_name = Text(
            "定义法",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 5.6)

        self.play(
            FadeIn(method_tag, shift=DOWN * 0.2),
            FadeIn(method_name, shift=DOWN * 0.2),
            run_time=0.6
        )

        # 绘制三角形
        triangle = self._create_triangle()
        self.play(Create(triangle), run_time=0.8)

        # 顶点标签
        label_A = Text("A", font="PingFang SC", font_size=28, color=WHITE).next_to(self.A, UP, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=28, color=WHITE).next_to(self.B, DL, buff=0.15)
        label_C = Text("C", font="PingFang SC", font_size=28, color=WHITE).next_to(self.C, DR, buff=0.15)

        self.play(
            FadeIn(label_A),
            FadeIn(label_B),
            FadeIn(label_C),
            run_time=0.5
        )

        # 条件展示：AB = AC 高亮显示
        cond_text = Text(
            "已知条件：",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 3.5)

        cond_formula = MathTex(
            r"AB = AC",
            color=self.COLOR_EQUAL_SIDE,
            font_size=36
        ).next_to(cond_text, DOWN, buff=0.2)

        self.play(FadeIn(cond_text), run_time=0.4)
        self.play(Write(cond_formula), run_time=0.8)

        # 高亮AB边和AC边
        ab_line = Line(self.A, self.B, color=self.COLOR_EQUAL_SIDE, stroke_width=6)
        ac_line = Line(self.A, self.C, color=self.COLOR_EQUAL_SIDE, stroke_width=6)

        self.play(
            Create(ab_line),
            Create(ac_line),
            run_time=0.8
        )

        # 添加刻度标记（一刻线表示等长）
        tick_AB = self._create_tick_mark(self.A, self.B, n=1, color=self.COLOR_EQUAL_SIDE)
        tick_AC = self._create_tick_mark(self.A, self.C, n=1, color=self.COLOR_EQUAL_SIDE)

        self.play(
            FadeIn(tick_AB),
            FadeIn(tick_AC),
            run_time=0.5
        )
        self.wait(0.5)

        # 结论动画
        arrow_down = Arrow(UP * 0.3, DOWN * 0.3, color=self.COLOR_HIGHLIGHT,
                          buff=0).move_to(DOWN * 5.2)
        concl_text = Text(
            "∴ △ABC 是等腰三角形",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 6.0)

        self.play(FadeIn(arrow_down), run_time=0.3)
        self.play(Write(concl_text), run_time=0.8)

        # 闪光强调
        self.play(
            Flash(ab_line.get_center(), color=self.COLOR_EQUAL_SIDE, flash_radius=0.5),
            Flash(ac_line.get_center(), color=self.COLOR_EQUAL_SIDE, flash_radius=0.5),
            run_time=0.6
        )

        # 规则框
        rule_box = RoundedRectangle(
            width=8.0, height=1.2,
            corner_radius=0.3,
            color=self.COLOR_SUCCESS,
            fill_color="#0d2a1a",
            fill_opacity=0.8
        ).move_to(DOWN * 6.3)

        rule_text = Text(
            "有两边相等的三角形是等腰三角形",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 6.3)

        self.play(
            FadeOut(arrow_down),
            FadeOut(concl_text),
            FadeIn(rule_box),
            FadeIn(rule_text),
            run_time=0.6
        )
        self.wait(1.5)

        # 清理场景2
        self.play(
            FadeOut(method_tag),
            FadeOut(method_name),
            FadeOut(triangle),
            FadeOut(label_A), FadeOut(label_B), FadeOut(label_C),
            FadeOut(ab_line), FadeOut(ac_line),
            FadeOut(tick_AB), FadeOut(tick_AC),
            FadeOut(cond_text), FadeOut(cond_formula),
            FadeOut(rule_box), FadeOut(rule_text),
            run_time=0.6
        )

    # ============================================================
    # Scene 3: 过渡 - 等边对等角性质回顾
    # ============================================================
    def scene_3_transition_property(self):
        """回顾等腰三角形性质：等边对等角，引出逆定理"""
        # 过渡提示
        prop_title = Text(
            "回顾：等腰三角形的性质",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        self.play(FadeIn(prop_title), run_time=0.5)

        # 绘制三角形
        triangle = self._create_triangle()
        self.play(Create(triangle), run_time=0.7)

        # 标签
        label_A = Text("A", font="PingFang SC", font_size=28, color=WHITE).next_to(self.A, UP, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=28, color=WHITE).next_to(self.B, DL, buff=0.15)
        label_C = Text("C", font="PingFang SC", font_size=28, color=WHITE).next_to(self.C, DR, buff=0.15)
        self.play(FadeIn(label_A), FadeIn(label_B), FadeIn(label_C), run_time=0.4)

        # 高亮等边
        ab_line = Line(self.A, self.B, color=self.COLOR_EQUAL_SIDE, stroke_width=5)
        ac_line = Line(self.A, self.C, color=self.COLOR_EQUAL_SIDE, stroke_width=5)
        tick_AB = self._create_tick_mark(self.A, self.B, n=1, color=self.COLOR_EQUAL_SIDE)
        tick_AC = self._create_tick_mark(self.A, self.C, n=1, color=self.COLOR_EQUAL_SIDE)

        self.play(Create(ab_line), Create(ac_line), run_time=0.6)
        self.play(FadeIn(tick_AB), FadeIn(tick_AC), run_time=0.4)

        # 等边条件
        cond1 = MathTex(r"AB = AC", color=self.COLOR_EQUAL_SIDE, font_size=32).move_to(DOWN * 3.5)
        arrow_prop = MathTex(r"\Rightarrow", color=WHITE, font_size=32).next_to(cond1, RIGHT, buff=0.2)
        cond2 = MathTex(r"\angle B = \angle C", color=self.COLOR_EQUAL_ANGLE, font_size=32).next_to(arrow_prop, RIGHT, buff=0.2)

        self.play(Write(cond1), run_time=0.5)
        self.play(FadeIn(arrow_prop), run_time=0.3)

        # 角弧展示
        # ∠B: 验证脚本显示需要 other_angle=True
        arc_B = self._create_angle_arc(
            self.B, self.A, self.C,
            radius=0.5, color=self.COLOR_EQUAL_ANGLE,
            other_angle=True  # 叉积为负，顺时针，需要 other_angle=True
        )
        # ∠C: 叉积为正，逆时针，使用默认
        arc_C = self._create_angle_arc(
            self.C, self.A, self.B,
            radius=0.5, color=self.COLOR_EQUAL_ANGLE,
            other_angle=False
        )

        self.play(Create(arc_B), Create(arc_C), run_time=0.8)
        self.play(Write(cond2), run_time=0.5)
        self.wait(0.8)

        # 引出逆定理
        inverse_box = RoundedRectangle(
            width=8.0, height=1.0,
            corner_radius=0.3,
            color=self.COLOR_HIGHLIGHT,
            fill_color="#2a2a0d",
            fill_opacity=0.8
        ).move_to(DOWN * 5.5)

        inverse_text = Text(
            "那么，反过来呢？",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5.5)

        self.play(FadeIn(inverse_box), FadeIn(inverse_text), run_time=0.6)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(prop_title),
            FadeOut(triangle),
            FadeOut(label_A), FadeOut(label_B), FadeOut(label_C),
            FadeOut(ab_line), FadeOut(ac_line),
            FadeOut(tick_AB), FadeOut(tick_AC),
            FadeOut(cond1), FadeOut(arrow_prop), FadeOut(cond2),
            FadeOut(arc_B), FadeOut(arc_C),
            FadeOut(inverse_box), FadeOut(inverse_text),
            run_time=0.6
        )

    # ============================================================
    # Scene 4: 判定方法二 - 等角对等边
    # ============================================================
    def scene_4_method2_equal_angles(self):
        """判定方法二：两角相等 → 等腰三角形（逆定理）"""
        # 方法标题
        method_tag = Text(
            "判定方法二",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_EQUAL_ANGLE
        ).move_to(UP * 6.5)

        method_name = Text(
            "等角对等边",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_EQUAL_ANGLE
        ).move_to(UP * 5.8)

        self.play(
            FadeIn(method_tag, shift=DOWN * 0.2),
            FadeIn(method_name, shift=DOWN * 0.2),
            run_time=0.6
        )

        # 绘制三角形
        triangle = self._create_triangle()
        self.play(Create(triangle), run_time=0.8)

        # 顶点标签
        label_A = Text("A", font="PingFang SC", font_size=28, color=WHITE).next_to(self.A, UP, buff=0.15)
        label_B = Text("B", font="PingFang SC", font_size=28, color=WHITE).next_to(self.B, DL, buff=0.15)
        label_C = Text("C", font="PingFang SC", font_size=28, color=WHITE).next_to(self.C, DR, buff=0.15)
        self.play(FadeIn(label_A), FadeIn(label_B), FadeIn(label_C), run_time=0.4)

        # 已知条件：∠B = ∠C
        cond_text = Text(
            "已知条件：",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(DOWN * 3.5)

        cond_formula = MathTex(
            r"\angle B = \angle C",
            color=self.COLOR_EQUAL_ANGLE,
            font_size=36
        ).next_to(cond_text, DOWN, buff=0.2)

        self.play(FadeIn(cond_text), run_time=0.4)
        self.play(Write(cond_formula), run_time=0.8)

        # 绘制等角弧（相同颜色和大小表示相等）
        # ∠B: other_angle=True（来自验证）
        arc_B = Angle(
            Line(self.B, self.A),
            Line(self.B, self.C),
            radius=0.5,
            color=self.COLOR_EQUAL_ANGLE,
            stroke_width=3,
            other_angle=True
        )
        # 小双弧标记∠C
        arc_C = Angle(
            Line(self.C, self.A),
            Line(self.C, self.B),
            radius=0.5,
            color=self.COLOR_EQUAL_ANGLE,
            stroke_width=3,
            other_angle=False
        )
        # 双弧（稍大半径）表示相等
        arc_B2 = Angle(
            Line(self.B, self.A),
            Line(self.B, self.C),
            radius=0.62,
            color=self.COLOR_EQUAL_ANGLE,
            stroke_width=3,
            other_angle=True
        )
        arc_C2 = Angle(
            Line(self.C, self.A),
            Line(self.C, self.B),
            radius=0.62,
            color=self.COLOR_EQUAL_ANGLE,
            stroke_width=3,
            other_angle=False
        )

        angle_arcs = VGroup(arc_B, arc_C, arc_B2, arc_C2)
        self.play(Create(angle_arcs), run_time=1.0)

        # 角度标签
        angle_B_label = MathTex(r"\angle B", color=self.COLOR_EQUAL_ANGLE, font_size=28).next_to(
            self.B, UR, buff=0.6)
        angle_C_label = MathTex(r"\angle C", color=self.COLOR_EQUAL_ANGLE, font_size=28).next_to(
            self.C, UL, buff=0.6)
        self.play(FadeIn(angle_B_label), FadeIn(angle_C_label), run_time=0.5)
        self.wait(0.5)

        # 结论：揭示 AB = AC
        concl_arrow = Text("∴", font="PingFang SC", font_size=32,
                           color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.2)
        concl_formula = MathTex(r"AB = AC", color=self.COLOR_EQUAL_SIDE,
                                font_size=36).next_to(concl_arrow, RIGHT, buff=0.2)

        self.play(FadeIn(concl_arrow), Write(concl_formula), run_time=0.8)

        # 高亮等边
        ab_line = Line(self.A, self.B, color=self.COLOR_EQUAL_SIDE, stroke_width=6)
        ac_line = Line(self.A, self.C, color=self.COLOR_EQUAL_SIDE, stroke_width=6)
        tick_AB = self._create_tick_mark(self.A, self.B, n=1, color=self.COLOR_EQUAL_SIDE)
        tick_AC = self._create_tick_mark(self.A, self.C, n=1, color=self.COLOR_EQUAL_SIDE)

        self.play(Create(ab_line), Create(ac_line), run_time=0.8)
        self.play(FadeIn(tick_AB), FadeIn(tick_AC), run_time=0.4)

        # 三角形是等腰三角形
        concl_iso = Text("△ABC 是等腰三角形！",
                         font="PingFang SC", font_size=28,
                         color=self.COLOR_SUCCESS).move_to(DOWN * 6.2)
        self.play(Write(concl_iso), run_time=0.6)
        self.play(
            Flash(self.B, color=self.COLOR_EQUAL_ANGLE, flash_radius=0.4),
            Flash(self.C, color=self.COLOR_EQUAL_ANGLE, flash_radius=0.4),
            Flash(self.A, color=self.COLOR_EQUAL_SIDE, flash_radius=0.4),
            run_time=0.8
        )
        self.wait(1.5)

        # 规则框
        rule_box = RoundedRectangle(
            width=8.0, height=1.3,
            corner_radius=0.3,
            color=self.COLOR_EQUAL_ANGLE,
            fill_color="#0d1a2a",
            fill_opacity=0.8
        ).move_to(DOWN * 6.3)

        rule_text = Text(
            "若∠B=∠C，则AB=AC",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_EQUAL_ANGLE
        ).move_to(DOWN * 6.1)

        rule_text2 = Text(
            "（等角对等边）",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_AUX
        ).move_to(DOWN * 6.55)

        self.play(
            FadeOut(concl_arrow), FadeOut(concl_formula), FadeOut(concl_iso),
            FadeIn(rule_box),
            FadeIn(rule_text),
            FadeIn(rule_text2),
            run_time=0.6
        )
        self.wait(1.8)

        # 清理场景4
        self.play(
            FadeOut(method_tag), FadeOut(method_name),
            FadeOut(triangle),
            FadeOut(label_A), FadeOut(label_B), FadeOut(label_C),
            FadeOut(cond_text), FadeOut(cond_formula),
            FadeOut(angle_arcs),
            FadeOut(angle_B_label), FadeOut(angle_C_label),
            FadeOut(ab_line), FadeOut(ac_line),
            FadeOut(tick_AB), FadeOut(tick_AC),
            FadeOut(rule_box), FadeOut(rule_text), FadeOut(rule_text2),
            run_time=0.6
        )

    # ============================================================
    # Scene 5: 例题练习
    # ============================================================
    def scene_5_example(self):
        """例题：两种方法各一个例子"""
        ex_title = Text(
            "例题练习",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        self.play(FadeIn(ex_title), run_time=0.4)

        # ===== 例1：定义法 =====
        ex1_label = Text(
            "例1   已知 AB = AC = 5，BC = 6",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 5.7)

        ex1_q = Text(
            "△ABC 是等腰三角形吗？",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.1)

        self.play(FadeIn(ex1_label), FadeIn(ex1_q), run_time=0.6)

        # 小三角形（例1）
        A1 = np.array([0, 3.8, 0])
        B1 = np.array([-1.6, 2.0, 0])
        C1 = np.array([1.6, 2.0, 0])

        tri1 = Polygon(A1, B1, C1, color=WHITE, stroke_width=3)
        lA1 = Text("A", font="PingFang SC", font_size=22).next_to(A1, UP, buff=0.1)
        lB1 = Text("B", font="PingFang SC", font_size=22).next_to(B1, DL, buff=0.1)
        lC1 = Text("C", font="PingFang SC", font_size=22).next_to(C1, DR, buff=0.1)

        self.play(Create(tri1), FadeIn(lA1), FadeIn(lB1), FadeIn(lC1), run_time=0.6)

        # 边长标注
        ab1_label = MathTex(r"5", color=self.COLOR_EQUAL_SIDE, font_size=24).move_to(
            (A1 + B1) / 2 + LEFT * 0.3)
        ac1_label = MathTex(r"5", color=self.COLOR_EQUAL_SIDE, font_size=24).move_to(
            (A1 + C1) / 2 + RIGHT * 0.3)
        bc1_label = MathTex(r"6", color=WHITE, font_size=24).move_to(
            (B1 + C1) / 2 + DOWN * 0.3)

        # 等边高亮
        ab1_line = Line(A1, B1, color=self.COLOR_EQUAL_SIDE, stroke_width=5)
        ac1_line = Line(A1, C1, color=self.COLOR_EQUAL_SIDE, stroke_width=5)
        tick1 = self._create_tick_mark(A1, B1, n=1, color=self.COLOR_EQUAL_SIDE, size=0.15)
        tick2 = self._create_tick_mark(A1, C1, n=1, color=self.COLOR_EQUAL_SIDE, size=0.15)

        self.play(
            Create(ab1_line), Create(ac1_line),
            FadeIn(ab1_label), FadeIn(ac1_label), FadeIn(bc1_label),
            FadeIn(tick1), FadeIn(tick2),
            run_time=0.7
        )

        # 答案
        ans1 = Text(
            "✓  是！因为 AB = AC = 5（定义法）",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_SUCCESS
        ).move_to(DOWN * 0.5 + UP * 0.2)  # y ≈ 0.2

        self.play(FadeIn(ans1), run_time=0.5)
        self.wait(0.8)

        # 淡出例1
        self.play(
            FadeOut(ex1_label), FadeOut(ex1_q),
            FadeOut(tri1), FadeOut(lA1), FadeOut(lB1), FadeOut(lC1),
            FadeOut(ab1_line), FadeOut(ac1_line),
            FadeOut(ab1_label), FadeOut(ac1_label), FadeOut(bc1_label),
            FadeOut(tick1), FadeOut(tick2),
            FadeOut(ans1),
            run_time=0.5
        )

        # ===== 例2：等角对等边 =====
        ex2_label = Text(
            "例2   已知 ∠B = ∠C = 65 度",
            font="PingFang SC",
            font_size=24,
            color=WHITE
        ).move_to(UP * 5.7)

        ex2_q = Text(
            "△ABC 是等腰三角形吗？",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.1)

        self.play(FadeIn(ex2_label), FadeIn(ex2_q), run_time=0.6)

        # 小三角形（例2，等腰）
        A2 = np.array([0, 3.8, 0])
        B2 = np.array([-1.6, 2.0, 0])
        C2 = np.array([1.6, 2.0, 0])

        tri2 = Polygon(A2, B2, C2, color=WHITE, stroke_width=3)
        lA2 = Text("A", font="PingFang SC", font_size=22).next_to(A2, UP, buff=0.1)
        lB2 = Text("B", font="PingFang SC", font_size=22).next_to(B2, DL, buff=0.1)
        lC2 = Text("C", font="PingFang SC", font_size=22).next_to(C2, DR, buff=0.1)

        self.play(Create(tri2), FadeIn(lA2), FadeIn(lB2), FadeIn(lC2), run_time=0.6)

        # 角度标注
        angle_B2_label = MathTex(r"65^\circ", color=self.COLOR_EQUAL_ANGLE, font_size=22).move_to(
            B2 + np.array([0.45, 0.35, 0]))
        angle_C2_label = MathTex(r"65^\circ", color=self.COLOR_EQUAL_ANGLE, font_size=22).move_to(
            C2 + np.array([-0.45, 0.35, 0]))

        # 角弧（用Line来创建Angle）
        arc_B2_ex = Angle(
            Line(B2, A2),
            Line(B2, C2),
            radius=0.4,
            color=self.COLOR_EQUAL_ANGLE,
            stroke_width=3,
            other_angle=True  # B点同样需要 other_angle=True（对称三角形）
        )
        arc_C2_ex = Angle(
            Line(C2, A2),
            Line(C2, B2),
            radius=0.4,
            color=self.COLOR_EQUAL_ANGLE,
            stroke_width=3,
            other_angle=False
        )

        self.play(
            Create(arc_B2_ex), Create(arc_C2_ex),
            FadeIn(angle_B2_label), FadeIn(angle_C2_label),
            run_time=0.7
        )

        # 揭示等边
        ab2_line = Line(A2, B2, color=self.COLOR_EQUAL_SIDE, stroke_width=5)
        ac2_line = Line(A2, C2, color=self.COLOR_EQUAL_SIDE, stroke_width=5)
        tick_ab2 = self._create_tick_mark(A2, B2, n=1, color=self.COLOR_EQUAL_SIDE, size=0.15)
        tick_ac2 = self._create_tick_mark(A2, C2, n=1, color=self.COLOR_EQUAL_SIDE, size=0.15)

        self.play(Create(ab2_line), Create(ac2_line), run_time=0.7)
        self.play(FadeIn(tick_ab2), FadeIn(tick_ac2), run_time=0.4)

        # 答案
        ans2 = Text(
            "✓  是！因为 ∠B = ∠C（等角对等边）",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 0.2)

        self.play(FadeIn(ans2), run_time=0.5)
        self.play(
            Flash(B2, color=self.COLOR_EQUAL_ANGLE, flash_radius=0.3),
            Flash(C2, color=self.COLOR_EQUAL_ANGLE, flash_radius=0.3),
            run_time=0.6
        )
        self.wait(1.2)

        # 清理例2
        self.play(
            FadeOut(ex_title),
            FadeOut(ex2_label), FadeOut(ex2_q),
            FadeOut(tri2), FadeOut(lA2), FadeOut(lB2), FadeOut(lC2),
            FadeOut(arc_B2_ex), FadeOut(arc_C2_ex),
            FadeOut(angle_B2_label), FadeOut(angle_C2_label),
            FadeOut(ab2_line), FadeOut(ac2_line),
            FadeOut(tick_ab2), FadeOut(tick_ac2),
            FadeOut(ans2),
            run_time=0.6
        )

    # ============================================================
    # Scene 6: 总结 + 片尾
    # ============================================================
    def scene_6_summary_outro(self):
        """总结两种判定方法，引导关注"""
        # 总结标题
        summary_title = Text(
            "知识总结",
            font="PingFang SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.2)
        self.play(Write(summary_title), run_time=0.6)

        # 方法一卡片
        card1_bg = RoundedRectangle(
            width=7.5, height=2.2,
            corner_radius=0.3,
            color=self.COLOR_SUCCESS,
            fill_color="#0d2a1a",
            fill_opacity=0.9
        ).move_to(UP * 4.3)

        card1_num = Text("方法一", font="PingFang SC", font_size=22,
                         color=self.COLOR_SUCCESS).move_to(card1_bg.get_top() + DOWN * 0.35)
        card1_title = Text("定义法",
                           font="PingFang SC", font_size=30,
                           color=WHITE).move_to(UP * 4.3 + UP * 0.2)
        card1_content = Text(
            "两边相等 → 等腰三角形",
            font="PingFang SC", font_size=24,
            color=self.COLOR_SUCCESS
        ).move_to(UP * 4.3 + DOWN * 0.5)

        self.play(FadeIn(card1_bg), run_time=0.3)
        self.play(FadeIn(card1_num), FadeIn(card1_title), FadeIn(card1_content), run_time=0.6)

        # 方法二卡片
        card2_bg = RoundedRectangle(
            width=7.5, height=2.2,
            corner_radius=0.3,
            color=self.COLOR_EQUAL_ANGLE,
            fill_color="#0d1a2a",
            fill_opacity=0.9
        ).move_to(UP * 1.5)

        card2_num = Text("方法二", font="PingFang SC", font_size=22,
                         color=self.COLOR_EQUAL_ANGLE).move_to(card2_bg.get_top() + DOWN * 0.35)
        card2_title = Text("等角对等边",
                           font="PingFang SC", font_size=30,
                           color=WHITE).move_to(UP * 1.5 + UP * 0.2)
        card2_content = Text(
            "两角相等 → 等腰三角形",
            font="PingFang SC", font_size=24,
            color=self.COLOR_EQUAL_ANGLE
        ).move_to(UP * 1.5 + DOWN * 0.5)

        self.play(FadeIn(card2_bg), run_time=0.3)
        self.play(FadeIn(card2_num), FadeIn(card2_title), FadeIn(card2_content), run_time=0.6)

        # 核心公式
        formula_box = RoundedRectangle(
            width=7.5, height=1.4,
            corner_radius=0.3,
            color=self.COLOR_HIGHLIGHT,
            fill_color="#1a1a0d",
            fill_opacity=0.9
        ).move_to(DOWN * 1.3)

        formula = MathTex(
            r"\angle B = \angle C \Leftrightarrow AB = AC",
            color=self.COLOR_HIGHLIGHT,
            font_size=32
        ).move_to(DOWN * 1.3)

        self.play(FadeIn(formula_box), Write(formula), run_time=0.8)
        self.wait(1.0)

        # 片尾 - 作者信息放大
        self.play(
            FadeOut(summary_title),
            FadeOut(card1_bg), FadeOut(card1_num),
            FadeOut(card1_title), FadeOut(card1_content),
            FadeOut(card2_bg), FadeOut(card2_num),
            FadeOut(card2_title), FadeOut(card2_content),
            FadeOut(formula_box), FadeOut(formula),
            run_time=0.6
        )

        # 大作者信息
        outro_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=44,
            color=WHITE
        ).move_to(UP * 2.0)

        outro_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_AUX
        ).move_to(UP * 1.0)

        outro_cta = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)

        self.play(
            Transform(self.author_bar, outro_name),
            run_time=0.6
        )
        self.play(FadeIn(outro_id, shift=UP * 0.3), run_time=0.4)
        self.play(FadeIn(outro_cta, shift=UP * 0.2), run_time=0.5)

        # 装饰性等腰三角形
        deco_triangles = VGroup()
        for i in range(5):
            size = 0.25 + 0.1 * i
            tri = Polygon(
                np.array([0, size, 0]),
                np.array([-size, -size * 0.5, 0]),
                np.array([size, -size * 0.5, 0]),
                color=self.COLOR_HIGHLIGHT,
                fill_opacity=0.6
            ).move_to(
                np.array([
                    np.cos(i * 2 * np.pi / 5) * 2.5,
                    np.sin(i * 2 * np.pi / 5) * 1.0 - 2.5,
                    0
                ])
            )
            deco_triangles.add(tri)

        self.play(
            *[FadeIn(t, scale=0.3) for t in deco_triangles],
            run_time=0.7
        )
        self.play(Rotate(deco_triangles, angle=PI, run_time=1.2))
        self.wait(1.0)

        # 最终淡出
        self.play(
            FadeOut(self.author_bar),
            FadeOut(outro_id),
            FadeOut(outro_cta),
            FadeOut(deco_triangles),
            run_time=1.0
        )


# ====== 渲染命令 ======
# 快速预览: manim -pql isosceles_triangle.py IsoscelesTriangleDetermination
# 高质量:   manim -qh  isosceles_triangle.py IsoscelesTriangleDetermination