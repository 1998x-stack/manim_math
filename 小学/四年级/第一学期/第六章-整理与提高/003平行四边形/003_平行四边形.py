"""
平行四边形 - 四年级几何教学动画
内容: 平行四边形的定义、底和高、对边相等、对角相等
目标观众: 小学四年级学生
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


class ParallelogramLesson(Scene):
    """
    平行四边形教学动画

    场景顺序:
    1. 开场 - 引入平行四边形
    2. 定义 - 两组对边分别平行
    3. 底和高 - 垂线定义
    4. 对边相等
    5. 对角相等
    6. 片尾总结
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色
        self.COLOR_SHAPE = "#4fc3f7"       # 浅蓝 - 主图形
        self.COLOR_PARALLEL = "#ffd54f"    # 黄 - 平行标记
        self.COLOR_HEIGHT = "#ef5350"      # 红 - 高线
        self.COLOR_EQUAL = "#66bb6a"       # 绿 - 相等标记
        self.COLOR_ANGLE = "#ce93d8"       # 紫 - 角度
        self.COLOR_AUXILIARY = "#90a4ae"   # 灰 - 辅助

        # 统一初始化几何数据
        self.setup_geometry()

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_height()
        self.scene_4_equal_sides()
        self.scene_5_equal_angles()
        self.scene_6_outro()

    # ──────────────────────────────────────────────
    # 几何初始化
    # ──────────────────────────────────────────────
    def setup_geometry(self):
        """统一初始化所有几何数据，场景共享"""
        # 平行四边形顶点（中心在原点附近）
        # A(左下) B(右下) C(右上) D(左上)
        # 向右倾斜，底边水平
        self.BASE_W = 3.0    # 底边宽
        self.SIDE_W = 1.2    # 侧边水平分量
        self.H = 1.8         # 高（垂直距离）
        self.CENTER = np.array([0.0, 0.5, 0.0])

        half_b = self.BASE_W / 2
        self.A = self.CENTER + np.array([-half_b, -self.H / 2, 0])
        self.B = self.CENTER + np.array([half_b, -self.H / 2, 0])
        self.C = self.CENTER + np.array([half_b + self.SIDE_W, self.H / 2, 0])
        self.D = self.CENTER + np.array([-half_b + self.SIDE_W, self.H / 2, 0])

        # 派生：垂足（从D向AB做垂线，垂足在AB延长线上）
        # AB是水平线，D在AB上方，垂足就是D正下方投影到AB所在直线
        self.foot_D = np.array([self.D[0], self.A[1], 0])
        # 从A向DC做垂线，垂足
        self.foot_A = np.array([self.A[0] - self.SIDE_W, self.D[1], 0])

        # 边长
        self.len_AB = np.linalg.norm(self.B - self.A)
        self.len_AD = np.linalg.norm(self.D - self.A)

        # 验证平行性（AB // DC, AD // BC）
        v_AB = self.B - self.A
        v_DC = self.C - self.D
        v_AD = self.D - self.A
        v_BC = self.C - self.B
        assert abs(np.cross(v_AB[:2], v_DC[:2])) < 1e-9, "AB not parallel to DC"
        assert abs(np.cross(v_AD[:2], v_BC[:2])) < 1e-9, "AD not parallel to BC"

        # 验证高
        foot = self._perpendicular_foot(self.D, self.A, self.B)
        computed_h = np.linalg.norm(self.D - foot)
        assert abs(computed_h - self.H) < 1e-9, f"Height mismatch: {computed_h} vs {self.H}"

    def _perpendicular_foot(self, point, line_start, line_end):
        """精确计算垂足"""
        lv = line_end - line_start
        pv = point - line_start
        t = np.dot(pv, lv) / np.dot(lv, lv)
        return line_start + t * lv

    # ──────────────────────────────────────────────
    # 辅助：创建平行四边形 Polygon
    # ──────────────────────────────────────────────
    def _make_parallelogram(self, color=None, stroke_width=3, fill_opacity=0.15):
        color = color or self.COLOR_SHAPE
        return Polygon(
            self.A, self.B, self.C, self.D,
            color=color,
            stroke_width=stroke_width,
            fill_color=color,
            fill_opacity=fill_opacity,
        )

    # ──────────────────────────────────────────────
    # 作者标识（始终在顶部）
    # ──────────────────────────────────────────────
    def _make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)

    # ──────────────────────────────────────────────
    # 平行符号（小箭头 > 标在边中点）
    # ──────────────────────────────────────────────
    def _parallel_tick(self, p1, p2, count=1, color=None, tick_len=0.18):
        """在线段 p1→p2 中点处绘制平行符号（1或2个箭头）"""
        color = color or self.COLOR_PARALLEL
        mid = (p1 + p2) / 2
        direction = (p2 - p1)
        direction = direction / np.linalg.norm(direction)
        perp = np.array([-direction[1], direction[0], 0])

        ticks = VGroup()
        offsets = [0] if count == 1 else [-0.12, 0.12]
        for off in offsets:
            pos = mid + perp * off
            # 用两条小线段组成 >
            p_back = pos - direction * tick_len * 0.6
            p_tip = pos + direction * tick_len * 0.4
            p_upper = pos + perp * tick_len * 0.4
            p_lower = pos - perp * tick_len * 0.4
            t1 = Line(p_back + perp * tick_len * 0.3, p_tip, color=color, stroke_width=2.5)
            t2 = Line(p_back - perp * tick_len * 0.3, p_tip, color=color, stroke_width=2.5)
            ticks.add(VGroup(t1, t2))
        return ticks

    # ──────────────────────────────────────────────
    # 相等符号（竖短线标在边中点）
    # ──────────────────────────────────────────────
    def _equal_tick(self, p1, p2, count=1, color=None, tick_len=0.22):
        color = color or self.COLOR_EQUAL
        mid = (p1 + p2) / 2
        direction = (p2 - p1)
        direction = direction / np.linalg.norm(direction)
        perp = np.array([-direction[1], direction[0], 0])

        ticks = VGroup()
        offsets = [0] if count == 1 else [-0.12, 0.12]
        for off in offsets:
            pos = mid + direction * off
            t = Line(pos - perp * tick_len / 2, pos + perp * tick_len / 2,
                     color=color, stroke_width=2.8)
            ticks.add(t)
        return ticks

    # ──────────────────────────────────────────────
    # Scene 1: 开场
    # ──────────────────────────────────────────────
    def scene_1_opening(self):
        author = self._make_author()
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author = author

        # 标题
        title = Text("平行四边形", font="Noto Sans CJK SC",
                     font_size=52, color=self.COLOR_SHAPE)
        title.move_to(UP * 5.8)

        hook = Text("你能找出它的秘密吗？", font="Noto Sans CJK SC",
                    font_size=30, color="#ffd54f")
        hook.move_to(UP * 4.9)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(hook, shift=UP * 0.2), run_time=0.5)

        # 绘制主图形
        pg = self._make_parallelogram()
        pg.move_to(ORIGIN + DOWN * 0.5)

        # 顶点标签
        label_A = Text("A", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        label_B = Text("B", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        label_C = Text("C", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        label_D = Text("D", font="Noto Sans CJK SC", font_size=24, color=WHITE)
        label_A.next_to(self.A + DOWN * 0.5, DL, buff=0.08)
        label_B.next_to(self.B + DOWN * 0.5, DR, buff=0.08)
        label_C.next_to(self.C + DOWN * 0.5, UR, buff=0.08)
        label_D.next_to(self.D + DOWN * 0.5, UL, buff=0.08)

        self.play(Create(pg), run_time=1.2)
        self.play(
            FadeIn(label_A), FadeIn(label_B),
            FadeIn(label_C), FadeIn(label_D),
            run_time=0.5
        )
        self.wait(0.8)

        self.play(
            FadeOut(hook),
            FadeOut(label_A), FadeOut(label_B),
            FadeOut(label_C), FadeOut(label_D),
            run_time=0.4
        )

        self.pg_main = pg
        self.title_main = title

    # ──────────────────────────────────────────────
    # Scene 2: 定义 — 两组对边分别平行
    # ──────────────────────────────────────────────
    def scene_2_definition(self):
        # 场景标题
        scene_title = Text("定义", font="Noto Sans CJK SC",
                           font_size=36, color=self.COLOR_PARALLEL)
        scene_title.move_to(UP * 4.8)
        self.play(Write(scene_title), run_time=0.6)

        # 定义文字第一行
        def_line1 = Text("两组对边分别平行的四边形",
                         font="Noto Sans CJK SC", font_size=26, color=WHITE)
        def_line2 = Text("叫做平行四边形",
                         font="Noto Sans CJK SC", font_size=26, color=self.COLOR_SHAPE)
        def_group = VGroup(def_line1, def_line2).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        def_group.move_to(UP * 3.8)

        self.play(Write(def_line1), run_time=0.7)
        self.play(Write(def_line2), run_time=0.5)
        self.wait(0.4)

        pg = self.pg_main

        # 高亮 AB（底边）
        ab_line = Line(self.A, self.B, color=self.COLOR_PARALLEL, stroke_width=5)
        dc_line = Line(self.D, self.C, color=self.COLOR_PARALLEL, stroke_width=5)

        self.play(Create(ab_line), run_time=0.5)
        self.play(Create(dc_line), run_time=0.5)

        # 平行符号 AB // DC
        tick_ab = self._parallel_tick(self.A, self.B, count=1)
        tick_dc = self._parallel_tick(self.D, self.C, count=1)
        self.play(FadeIn(tick_ab), FadeIn(tick_dc), run_time=0.4)

        label_parallel1 = Text("AB // DC", font="Noto Sans CJK SC",
                               font_size=26, color=self.COLOR_PARALLEL)
        label_parallel1.move_to(DOWN * 2.8)
        self.play(Write(label_parallel1), run_time=0.5)
        self.wait(0.6)

        # 高亮 AD // BC
        ad_line = Line(self.A, self.D, color="#ef9a9a", stroke_width=5)
        bc_line = Line(self.B, self.C, color="#ef9a9a", stroke_width=5)

        self.play(
            ab_line.animate.set_color(self.COLOR_SHAPE),
            dc_line.animate.set_color(self.COLOR_SHAPE),
            run_time=0.3
        )
        self.play(Create(ad_line), Create(bc_line), run_time=0.5)

        tick_ad = self._parallel_tick(self.A, self.D, count=2, color="#ef9a9a")
        tick_bc = self._parallel_tick(self.B, self.C, count=2, color="#ef9a9a")
        self.play(FadeIn(tick_ad), FadeIn(tick_bc), run_time=0.4)

        label_parallel2 = Text("AD // BC", font="Noto Sans CJK SC",
                               font_size=26, color="#ef9a9a")
        label_parallel2.next_to(label_parallel1, DOWN, buff=0.18)
        self.play(Write(label_parallel2), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(scene_title), FadeOut(def_group),
            FadeOut(ab_line), FadeOut(dc_line),
            FadeOut(ad_line), FadeOut(bc_line),
            FadeOut(tick_ab), FadeOut(tick_dc),
            FadeOut(tick_ad), FadeOut(tick_bc),
            FadeOut(label_parallel1), FadeOut(label_parallel2),
            run_time=0.5
        )

    # ──────────────────────────────────────────────
    # Scene 3: 底和高
    # ──────────────────────────────────────────────
    def scene_3_height(self):
        scene_title = Text("底 和 高", font="Noto Sans CJK SC",
                           font_size=38, color=self.COLOR_HEIGHT)
        scene_title.move_to(UP * 4.8)
        self.play(Write(scene_title), run_time=0.6)

        pg = self.pg_main

        # 底边标注
        ab_highlight = Line(self.A, self.B, color=self.COLOR_HEIGHT, stroke_width=5)
        self.play(Create(ab_highlight), run_time=0.5)

        label_base = Text("底", font="Noto Sans CJK SC",
                          font_size=28, color=self.COLOR_HEIGHT)
        mid_AB = (self.A + self.B) / 2
        label_base.next_to(mid_AB + DOWN * 0.5, DOWN, buff=0.1)
        self.play(FadeIn(label_base, shift=UP * 0.15), run_time=0.4)
        self.wait(0.4)

        # 高线：从D向AB做垂线
        # 垂足在 AB 所在直线上（可能在线段外）
        foot = self._perpendicular_foot(self.D, self.A, self.B)
        # foot = self.foot_D（水平线，AB是水平的）

        height_line = DashedLine(
            self.D, foot,
            color=self.COLOR_HEIGHT,
            stroke_width=3,
            dash_length=0.12,
        )
        self.play(Create(height_line), run_time=0.8)

        # 直角符号
        right_angle = self._right_angle_mark(foot, self.D, self.B, size=0.18)
        self.play(FadeIn(right_angle), run_time=0.3)

        # 高标注
        label_h = Text("高", font="Noto Sans CJK SC",
                        font_size=28, color=self.COLOR_HEIGHT)
        mid_height = (self.D + foot) / 2
        label_h.next_to(mid_height, RIGHT, buff=0.15)
        self.play(FadeIn(label_h, shift=LEFT * 0.15), run_time=0.4)

        # 解释文字
        explain1 = Text("从一条边上的点向对边作垂线",
                        font="Noto Sans CJK SC", font_size=22, color=WHITE)
        explain2 = Text("垂足之间的距离叫做高",
                        font="Noto Sans CJK SC", font_size=22, color=self.COLOR_HEIGHT)
        explains = VGroup(explain1, explain2).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        explains.move_to(DOWN * 3.2)

        self.play(Write(explain1), run_time=0.6)
        self.play(Write(explain2), run_time=0.5)
        self.wait(0.5)

        # 公式：高 ⊥ 底
        formula_row = VGroup(
            Text("高", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_HEIGHT),
            MathTex(r"\perp", font_size=36, color=WHITE),
            Text("底", font="Noto Sans CJK SC", font_size=28, color=self.COLOR_HEIGHT),
        ).arrange(RIGHT, buff=0.15)
        formula_row.move_to(DOWN * 4.2)

        self.play(FadeIn(formula_row, scale=1.1), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(ab_highlight),
            FadeOut(label_base),
            FadeOut(height_line),
            FadeOut(right_angle),
            FadeOut(label_h),
            FadeOut(explains),
            FadeOut(formula_row),
            run_time=0.5
        )

    def _right_angle_mark(self, corner, point1, point2, size=0.18, color=YELLOW):
        """在 corner 处绘制直角符号（小正方形）"""
        v1 = point1 - corner
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = point2 - corner
        v2 = v2 / np.linalg.norm(v2) * size

        square = Polygon(
            corner,
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=color,
            stroke_width=2.0,
            fill_opacity=0,
        )
        return square

    # ──────────────────────────────────────────────
    # Scene 4: 对边相等
    # ──────────────────────────────────────────────
    def scene_4_equal_sides(self):
        scene_title = Text("对边相等", font="Noto Sans CJK SC",
                           font_size=40, color=self.COLOR_EQUAL)
        scene_title.move_to(UP * 4.8)
        self.play(Write(scene_title), run_time=0.6)

        pg = self.pg_main

        # 高亮 AB 和 DC（对边1）
        ab_line = Line(self.A, self.B, color=self.COLOR_EQUAL, stroke_width=5)
        dc_line = Line(self.D, self.C, color=self.COLOR_EQUAL, stroke_width=5)

        self.play(Create(ab_line), Create(dc_line), run_time=0.6)

        tick_ab = self._equal_tick(self.A, self.B, count=1)
        tick_dc = self._equal_tick(self.D, self.C, count=1)
        self.play(FadeIn(tick_ab), FadeIn(tick_dc), run_time=0.4)

        label_eq1 = Text("AB = DC", font="Noto Sans CJK SC",
                         font_size=28, color=self.COLOR_EQUAL)
        label_eq1.move_to(DOWN * 2.8)
        self.play(Write(label_eq1), run_time=0.5)
        self.wait(0.7)

        # 高亮 AD 和 BC（对边2）
        ad_line = Line(self.A, self.D, color="#a5d6a7", stroke_width=5)
        bc_line = Line(self.B, self.C, color="#a5d6a7", stroke_width=5)

        self.play(
            ab_line.animate.set_color(self.COLOR_SHAPE),
            dc_line.animate.set_color(self.COLOR_SHAPE),
            run_time=0.3
        )
        self.play(Create(ad_line), Create(bc_line), run_time=0.6)

        tick_ad = self._equal_tick(self.A, self.D, count=2, color="#a5d6a7")
        tick_bc = self._equal_tick(self.B, self.C, count=2, color="#a5d6a7")
        self.play(FadeIn(tick_ad), FadeIn(tick_bc), run_time=0.4)

        label_eq2 = Text("AD = BC", font="Noto Sans CJK SC",
                         font_size=28, color="#a5d6a7")
        label_eq2.next_to(label_eq1, DOWN, buff=0.18)
        self.play(Write(label_eq2), run_time=0.5)
        self.wait(0.6)

        # 总结
        summary = Text("平行四边形对边相等！",
                       font="Noto Sans CJK SC", font_size=26, color=YELLOW)
        summary.next_to(label_eq2, DOWN, buff=0.3)
        self.play(FadeIn(summary, scale=1.1), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(ab_line), FadeOut(dc_line),
            FadeOut(ad_line), FadeOut(bc_line),
            FadeOut(tick_ab), FadeOut(tick_dc),
            FadeOut(tick_ad), FadeOut(tick_bc),
            FadeOut(label_eq1), FadeOut(label_eq2),
            FadeOut(summary),
            run_time=0.5
        )

    # ──────────────────────────────────────────────
    # Scene 5: 对角相等
    # ──────────────────────────────────────────────
    def scene_5_equal_angles(self):
        scene_title = Text("对角相等", font="Noto Sans CJK SC",
                           font_size=40, color=self.COLOR_ANGLE)
        scene_title.move_to(UP * 4.8)
        self.play(Write(scene_title), run_time=0.6)

        pg = self.pg_main

        # 角 A 和 角 C（对角）
        # 用 Arc 标注角 A
        arc_A = self._make_angle_arc(self.D, self.A, self.B,
                                     color=self.COLOR_ANGLE, radius=0.38)
        arc_C = self._make_angle_arc(self.B, self.C, self.D,
                                     color=self.COLOR_ANGLE, radius=0.38)

        self.play(Create(arc_A), Create(arc_C), run_time=0.7)

        label_A_text = Text("∠A", font="Noto Sans CJK SC",
                            font_size=22, color=self.COLOR_ANGLE)
        label_C_text = Text("∠C", font="Noto Sans CJK SC",
                            font_size=22, color=self.COLOR_ANGLE)
        label_A_text.move_to(self.A + np.array([0.05, -0.55, 0]))
        label_C_text.move_to(self.C + np.array([0.05, 0.55, 0]))

        self.play(FadeIn(label_A_text), FadeIn(label_C_text), run_time=0.4)

        eq_label1 = Text("∠A = ∠C", font="Noto Sans CJK SC",
                         font_size=28, color=self.COLOR_ANGLE)
        eq_label1.move_to(DOWN * 2.8)
        self.play(Write(eq_label1), run_time=0.5)
        self.wait(0.8)

        # 角 B 和 角 D（另一对对角）
        arc_B = self._make_angle_arc(self.A, self.B, self.C,
                                     color="#f48fb1", radius=0.38)
        arc_D = self._make_angle_arc(self.C, self.D, self.A,
                                     color="#f48fb1", radius=0.38)

        self.play(Create(arc_B), Create(arc_D), run_time=0.7)

        label_B_text = Text("∠B", font="Noto Sans CJK SC",
                            font_size=22, color="#f48fb1")
        label_D_text = Text("∠D", font="Noto Sans CJK SC",
                            font_size=22, color="#f48fb1")
        label_B_text.move_to(self.B + np.array([0.6, -0.4, 0]))
        label_D_text.move_to(self.D + np.array([-0.5, 0.45, 0]))

        self.play(FadeIn(label_B_text), FadeIn(label_D_text), run_time=0.4)

        eq_label2 = Text("∠B = ∠D", font="Noto Sans CJK SC",
                         font_size=28, color="#f48fb1")
        eq_label2.next_to(eq_label1, DOWN, buff=0.18)
        self.play(Write(eq_label2), run_time=0.5)
        self.wait(0.6)

        summary = Text("平行四边形对角相等！",
                       font="Noto Sans CJK SC", font_size=26, color=YELLOW)
        summary.next_to(eq_label2, DOWN, buff=0.3)
        self.play(FadeIn(summary, scale=1.1), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(arc_A), FadeOut(arc_C),
            FadeOut(arc_B), FadeOut(arc_D),
            FadeOut(label_A_text), FadeOut(label_C_text),
            FadeOut(label_B_text), FadeOut(label_D_text),
            FadeOut(eq_label1), FadeOut(eq_label2),
            FadeOut(summary),
            run_time=0.5
        )

    def _make_angle_arc(self, p1, vertex, p2, color=YELLOW, radius=0.4):
        """
        在 vertex 处绘制从 p1 到 p2 的角弧（正确方向）。
        使用 cross product 判断 other_angle。
        """
        v1 = p1 - vertex
        v2 = p2 - vertex
        line1 = Line(vertex, vertex + v1 / np.linalg.norm(v1))
        line2 = Line(vertex, vertex + v2 / np.linalg.norm(v2))

        cross_z = v1[0] * v2[1] - v1[1] * v2[0]
        other = cross_z < 0

        arc = Angle(line1, line2, radius=radius, other_angle=other,
                    color=color, stroke_width=2.5)
        return arc

    # ──────────────────────────────────────────────
    # Scene 6: 片尾总结
    # ──────────────────────────────────────────────
    def scene_6_outro(self):
        # 淡出主图形和标题
        self.play(
            FadeOut(self.pg_main),
            FadeOut(self.title_main),
            run_time=0.5
        )

        # 总结卡
        summary_title = Text("平行四边形的性质", font="Noto Sans CJK SC",
                             font_size=38, color=self.COLOR_SHAPE)
        summary_title.move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.7)

        props = [
            ("① 两组对边分别平行", self.COLOR_PARALLEL),
            ("② 对边相等（AB=DC，AD=BC）", self.COLOR_EQUAL),
            ("③ 对角相等（∠A=∠C，∠B=∠D）", self.COLOR_ANGLE),
            ("④ 高 ⊥ 底", self.COLOR_HEIGHT),
        ]

        items = VGroup()
        for text, color in props:
            item = Text(text, font="Noto Sans CJK SC", font_size=24, color=color)
            items.add(item)

        items.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        items.move_to(UP * 2.5)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.45)

        self.wait(0.5)

        # 小图形示范
        pg_small = self._make_parallelogram(fill_opacity=0.25)
        pg_small.scale(0.7).move_to(DOWN * 2.0)
        self.play(Create(pg_small), run_time=0.8)

        # 平行符号
        t_ab = self._parallel_tick(self.A * 0.7, self.B * 0.7, count=1)
        t_dc = self._parallel_tick(self.D * 0.7, self.C * 0.7, count=1)
        t_ad = self._parallel_tick(self.A * 0.7, self.D * 0.7, count=2, color="#ef9a9a")
        t_bc = self._parallel_tick(self.B * 0.7, self.C * 0.7, count=2, color="#ef9a9a")

        # 等边符号
        e_ab = self._equal_tick(self.A * 0.7, self.B * 0.7, count=1)
        e_dc = self._equal_tick(self.D * 0.7, self.C * 0.7, count=1)
        e_ad = self._equal_tick(self.A * 0.7, self.D * 0.7, count=2, color="#a5d6a7")
        e_bc = self._equal_tick(self.B * 0.7, self.C * 0.7, count=2, color="#a5d6a7")

        self.play(
            FadeIn(t_ab), FadeIn(t_dc),
            FadeIn(t_ad), FadeIn(t_bc),
            run_time=0.4
        )
        self.wait(0.3)
        self.play(
            FadeIn(e_ab), FadeIn(e_dc),
            FadeIn(e_ad), FadeIn(e_bc),
            run_time=0.4
        )
        self.wait(1.5)

        # 关注提示
        follow = Text("关注我，获得更多数学技巧！",
                      font="Noto Sans CJK SC", font_size=28, color=YELLOW)
        follow.move_to(DOWN * 4.2)
        self.play(FadeIn(follow, scale=1.05), run_time=0.6)

        # 作者大字
        author_big = Text("上海初高中数学直通车",
                          font="Noto Sans CJK SC", font_size=30, color=WHITE)
        author_id = Text("@emptyandcalm",
                         font="Noto Sans CJK SC", font_size=24, color="#6b7280")
        author_group = VGroup(author_big, author_id).arrange(DOWN, buff=0.1)
        author_group.move_to(DOWN * 5.5)

        self.play(FadeIn(author_group, shift=UP * 0.2), run_time=0.5)
        self.wait(2.5)

        self.play(
            FadeOut(summary_title), FadeOut(items),
            FadeOut(pg_small),
            FadeOut(t_ab), FadeOut(t_dc), FadeOut(t_ad), FadeOut(t_bc),
            FadeOut(e_ab), FadeOut(e_dc), FadeOut(e_ad), FadeOut(e_bc),
            FadeOut(follow), FadeOut(author_group),
            FadeOut(self.author),
            run_time=1.0
        )
