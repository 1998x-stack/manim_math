"""
正方形的性质与判定 - Manim TikTok 竖屏教学动画
年级: 八年级第二学期 第二十二章 四边形
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
  manim -pql square_properties.py SquareProperties   # 快速预览
  manim -qh  square_properties.py SquareProperties   # 高质量
"""

from manim import *
import numpy as np

# ── 全局配置 TikTok 竖屏 ───────────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ── 颜色常量 ──────────────────────────────────────────────────────
BG_COLOR      = "#1a1a2e"
SQUARE_COLOR  = "#4fc3f7"   # 主正方形
DIAG_COLOR1   = "#ffd54f"   # 对角线AC
DIAG_COLOR2   = "#ff8a65"   # 对角线BD
RIGHT_MK_CLR  = "#a5d6a7"   # 直角标记
EQUAL_CLR     = "#ef9a9a"   # 等边标记
RECT_CLR      = "#80cbc4"   # 矩形
RHOMBUS_CLR   = "#ce93d8"   # 菱形
HL_COLOR      = "#ffeb3b"   # 高亮黄


# ══════════════════════════════════════════════════════════════════
class SquareProperties(Scene):
    """正方形的性质与判定 - 教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 初始化几何 ──
        self.setup_geometry()

        # ── 各场景 ──
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_property_sides_angles()
        self.scene_4_property_diagonals()
        self.scene_5_determine_rect()
        self.scene_6_determine_rhombus()
        self.scene_7_summary_outro()

    # ══════════════════════════════════════════════════════════════
    # 几何初始化
    # ══════════════════════════════════════════════════════════════
    def setup_geometry(self):
        """统一计算所有几何坐标，绝不臆想。"""
        self.SIDE = 2.5
        self.CENTER = np.array([0.0, 1.2, 0.0])
        half = self.SIDE / 2

        # 正方形四顶点  A=左下  B=右下  C=右上  D=左上
        self.sq_A = self.CENTER + np.array([-half, -half, 0])
        self.sq_B = self.CENTER + np.array([ half, -half, 0])
        self.sq_C = self.CENTER + np.array([ half,  half, 0])
        self.sq_D = self.CENTER + np.array([-half,  half, 0])

        # 对角线交点（正方形对称中心）
        self.sq_O = (self.sq_A + self.sq_C) / 2  # == CENTER

        # 对角线长
        self.diag_len = self.SIDE * np.sqrt(2)

        # ── 矩形（演示 Scene 5，长3 高1.5，中心同主正方形）
        rw, rh = 3.0, 1.5
        rc = self.CENTER.copy()
        self.rect_A = rc + np.array([-rw/2, -rh/2, 0])
        self.rect_B = rc + np.array([ rw/2, -rh/2, 0])
        self.rect_C = rc + np.array([ rw/2,  rh/2, 0])
        self.rect_D = rc + np.array([-rw/2,  rh/2, 0])

        # ── 菱形（演示 Scene 6，水平对角线2*1.5=3，垂直对角线2*1.0=2）
        rmc = self.CENTER.copy()
        self.rh_A = rmc + np.array([-1.5,  0.0, 0])  # 左
        self.rh_B = rmc + np.array([ 0.0, -1.0, 0])  # 下
        self.rh_C = rmc + np.array([ 1.5,  0.0, 0])  # 右
        self.rh_D = rmc + np.array([ 0.0,  1.0, 0])  # 上

        self._verify()

    def _verify(self):
        eps = 1e-6
        # 正方形四边等长
        sides = [
            np.linalg.norm(self.sq_B - self.sq_A),
            np.linalg.norm(self.sq_C - self.sq_B),
            np.linalg.norm(self.sq_D - self.sq_C),
            np.linalg.norm(self.sq_A - self.sq_D),
        ]
        assert all(abs(s - self.SIDE) < eps for s in sides), "正方形边长计算错误"

        # 对角线垂直
        d1 = self.sq_C - self.sq_A
        d2 = self.sq_D - self.sq_B
        assert abs(np.dot(d1[:2], d2[:2])) < eps, "对角线不垂直"

        # 对角线平分
        mid1 = (self.sq_A + self.sq_C) / 2
        mid2 = (self.sq_B + self.sq_D) / 2
        assert np.linalg.norm(mid1 - mid2) < eps, "对角线不互相平分"

        print("✓ 几何验证通过")

    # ══════════════════════════════════════════════════════════════
    # 辅助：直角标记小方块
    # ══════════════════════════════════════════════════════════════
    def _right_angle_mark(self, corner, p1, p2, size=0.2, color=RIGHT_MK_CLR):
        """在 corner 处创建正确方向的小直角方块标记"""
        v1 = p1 - corner
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = p2 - corner
        v2 = v2 / np.linalg.norm(v2) * size
        return Polygon(
            corner, corner + v1, corner + v1 + v2, corner + v2,
            color=color, stroke_width=2.0, fill_opacity=0
        )

    # ══════════════════════════════════════════════════════════════
    # 辅助：在线段中间添加等边刻度线
    # ══════════════════════════════════════════════════════════════
    def _tick_mark(self, p1, p2, n=1, size=0.18, color=EQUAL_CLR):
        """在线段中点附近画 n 条刻度线表示相等"""
        mid = (p1 + p2) / 2
        direction = p2 - p1
        direction = direction / np.linalg.norm(direction)
        perp = np.array([-direction[1], direction[0], 0])
        ticks = VGroup()
        gap = 0.12
        # 居中排列 n 条
        offsets = [(i - (n-1)/2) * gap for i in range(n)]
        for offset in offsets:
            center = mid + direction * offset
            tick = Line(center - perp * size/2, center + perp * size/2,
                        color=color, stroke_width=2.5)
            ticks.add(tick)
        return ticks

    # ══════════════════════════════════════════════════════════════
    # Scene 1: 开场钩子
    # ══════════════════════════════════════════════════════════════
    def scene_1_opening(self):
        # 作者信息
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font="PingFang SC", font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 大标题
        title = Text("正方形", font="PingFang SC",
                     font_size=64, color=HL_COLOR, weight=BOLD)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.9)

        # 正方形从中心生长
        sq = Square(side_length=self.SIDE, color=SQUARE_COLOR, stroke_width=4)
        sq.move_to(self.CENTER)
        self.play(Create(sq), run_time=1.2)

        # 顶点标签
        labels_data = [
            (self.sq_A, "A", DL),
            (self.sq_B, "B", DR),
            (self.sq_C, "C", UR),
            (self.sq_D, "D", UL),
        ]
        vertex_labels = VGroup()
        for pt, lbl, direction in labels_data:
            t = Text(lbl, font="PingFang SC", font_size=28, color=WHITE)
            t.next_to(pt, direction, buff=0.15)
            vertex_labels.add(t)
        self.play(FadeIn(vertex_labels), run_time=0.6)

        # 钩子文字
        hook = Text("你真的了解它的全部性质吗?",
                    font="PingFang SC", font_size=28, color=HL_COLOR)
        hook.move_to(DOWN * 4.5)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.6)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sq), FadeOut(vertex_labels),
            FadeOut(hook), run_time=0.5
        )
        # 保存主正方形供后续使用
        self.main_sq = Square(side_length=self.SIDE, color=SQUARE_COLOR, stroke_width=3)
        self.main_sq.move_to(self.CENTER)

    # ══════════════════════════════════════════════════════════════
    # Scene 2: 定义
    # ══════════════════════════════════════════════════════════════
    def scene_2_definition(self):
        scene_title = Text("正方形的定义", font="PingFang SC",
                           font_size=36, color=SQUARE_COLOR)
        scene_title.move_to(UP * 6.3)
        self.play(Write(scene_title), run_time=0.7)

        # 定义文字
        def_1 = Text("有一组邻边相等的矩形",
                     font="PingFang SC", font_size=26, color=RECT_CLR)
        def_arrow = Text("或", font="PingFang SC", font_size=26, color=WHITE)
        def_2 = Text("有一个直角的菱形",
                     font="PingFang SC", font_size=26, color=RHOMBUS_CLR)

        defs = VGroup(def_1, def_arrow, def_2).arrange(DOWN, buff=0.35)
        defs.move_to(UP * 4.6)
        self.play(FadeIn(def_1, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(def_arrow), run_time=0.3)
        self.play(FadeIn(def_2, shift=RIGHT * 0.3), run_time=0.5)

        # 正方形图形
        self.play(Create(self.main_sq), run_time=1.0)

        # 顶点
        vtx_labels = VGroup(
            Text("A", font="PingFang SC", font_size=24, color=WHITE).next_to(self.sq_A, DL, buff=0.12),
            Text("B", font="PingFang SC", font_size=24, color=WHITE).next_to(self.sq_B, DR, buff=0.12),
            Text("C", font="PingFang SC", font_size=24, color=WHITE).next_to(self.sq_C, UR, buff=0.12),
            Text("D", font="PingFang SC", font_size=24, color=WHITE).next_to(self.sq_D, UL, buff=0.12),
        )
        self.play(FadeIn(vtx_labels), run_time=0.4)
        self.vtx_labels = vtx_labels

        # 关键词：特殊平行四边形
        note = Text("— 最特殊的平行四边形 —",
                    font="PingFang SC", font_size=22, color=GRAY_A)
        note.move_to(DOWN * 3.5)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(FadeOut(scene_title), FadeOut(defs), FadeOut(note), run_time=0.5)

    # ══════════════════════════════════════════════════════════════
    # Scene 3: 性质1 — 四边相等 & 四角直角
    # ══════════════════════════════════════════════════════════════
    def scene_3_property_sides_angles(self):
        title = Text("性质一", font="PingFang SC",
                     font_size=36, color=HL_COLOR)
        title.move_to(UP * 6.3)
        self.play(Write(title), run_time=0.5)

        # 副标题
        sub = Text("四边相等，四角都是直角",
                   font="PingFang SC", font_size=26, color=WHITE)
        sub.move_to(UP * 5.5)
        self.play(FadeIn(sub), run_time=0.5)

        # 依次高亮四条边，加刻度线
        edges = [
            (self.sq_A, self.sq_B, "AB", DOWN),
            (self.sq_B, self.sq_C, "BC", RIGHT),
            (self.sq_C, self.sq_D, "CD", UP),
            (self.sq_D, self.sq_A, "DA", LEFT),
        ]
        tick_group = VGroup()
        for p1, p2, name, direction in edges:
            # 高亮边
            hl_line = Line(p1, p2, color=EQUAL_CLR, stroke_width=6)
            self.play(Create(hl_line), run_time=0.3)
            tick = self._tick_mark(p1, p2, n=1)
            tick_group.add(tick)
            self.play(FadeIn(tick), run_time=0.2)
            self.play(FadeOut(hl_line), run_time=0.2)

        # 公式: AB = BC = CD = DA
        eq_formula = MathTex(
            r"AB = BC = CD = DA",
            font_size=30, color=EQUAL_CLR
        )
        eq_formula.move_to(DOWN * 3.8)
        self.play(Write(eq_formula), run_time=0.8)

        self.wait(0.5)

        # 四个直角标记
        right_marks = VGroup(
            self._right_angle_mark(self.sq_A, self.sq_B, self.sq_D, size=0.22),
            self._right_angle_mark(self.sq_B, self.sq_C, self.sq_A, size=0.22),
            self._right_angle_mark(self.sq_C, self.sq_D, self.sq_B, size=0.22),
            self._right_angle_mark(self.sq_D, self.sq_A, self.sq_C, size=0.22),
        )
        self.play(FadeIn(right_marks), run_time=0.6)

        # 公式: ∠A = ∠B = ∠C = ∠D = 90°
        angle_formula = MathTex(
            r"\angle A = \angle B = \angle C = \angle D = 90^\circ",
            font_size=28, color=RIGHT_MK_CLR
        )
        angle_formula.move_to(DOWN * 4.8)
        self.play(Write(angle_formula), run_time=0.9)

        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(tick_group), FadeOut(eq_formula),
            FadeOut(right_marks), FadeOut(angle_formula),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════════════
    # Scene 4: 性质2 — 对角线
    # ══════════════════════════════════════════════════════════════
    def scene_4_property_diagonals(self):
        title = Text("性质二", font="PingFang SC",
                     font_size=36, color=HL_COLOR)
        title.move_to(UP * 6.3)
        self.play(Write(title), run_time=0.5)

        sub = Text("对角线相等且互相垂直平分",
                   font="PingFang SC", font_size=26, color=WHITE)
        sub.move_to(UP * 5.5)
        self.play(FadeIn(sub), run_time=0.5)

        # 画对角线 AC
        diag_AC = DashedLine(self.sq_A, self.sq_C,
                             color=DIAG_COLOR1, dash_length=0.15, stroke_width=2.5)
        lbl_AC = Text("AC", font="PingFang SC", font_size=20, color=DIAG_COLOR1)
        lbl_AC.next_to(diag_AC.get_center(), LEFT, buff=0.3)
        self.play(Create(diag_AC), FadeIn(lbl_AC), run_time=0.8)

        # 画对角线 BD
        diag_BD = DashedLine(self.sq_B, self.sq_D,
                             color=DIAG_COLOR2, dash_length=0.15, stroke_width=2.5)
        lbl_BD = Text("BD", font="PingFang SC", font_size=20, color=DIAG_COLOR2)
        lbl_BD.next_to(diag_BD.get_center(), RIGHT, buff=0.3)
        self.play(Create(diag_BD), FadeIn(lbl_BD), run_time=0.8)

        # 交点 O
        O_dot = Dot(self.sq_O, radius=0.1, color=WHITE)
        O_lbl = Text("O", font="PingFang SC", font_size=20, color=WHITE)
        O_lbl.next_to(O_dot, RIGHT, buff=0.15)
        self.play(FadeIn(O_dot), FadeIn(O_lbl), run_time=0.4)
        self.play(Flash(O_dot, color=HL_COLOR, flash_radius=0.3), run_time=0.5)

        # 中点刻度（分段等长）
        mid_ticks = VGroup(
            self._tick_mark(self.sq_A, self.sq_O, n=1, size=0.14, color=DIAG_COLOR1),
            self._tick_mark(self.sq_O, self.sq_C, n=1, size=0.14, color=DIAG_COLOR1),
            self._tick_mark(self.sq_B, self.sq_O, n=2, size=0.14, color=DIAG_COLOR2),
            self._tick_mark(self.sq_O, self.sq_D, n=2, size=0.14, color=DIAG_COLOR2),
        )
        self.play(FadeIn(mid_ticks), run_time=0.5)

        # 垂直标记
        right_o = self._right_angle_mark(
            self.sq_O,
            self.sq_A,      # 沿AC方向
            self.sq_B,      # 沿BD方向
            size=0.2, color=RIGHT_MK_CLR
        )
        self.play(FadeIn(right_o), run_time=0.4)

        # 公式
        f1 = MathTex(r"AC = BD", font_size=30, color=DIAG_COLOR1)
        f2 = MathTex(r"AC \perp BD", font_size=30, color=RIGHT_MK_CLR)
        f3 = MathTex(r"AO = CO,\ BO = DO", font_size=26, color=GRAY_A)
        formulas = VGroup(f1, f2, f3).arrange(DOWN, buff=0.3)
        formulas.move_to(DOWN * 4.5)
        self.play(Write(f1), run_time=0.5)
        self.play(Write(f2), run_time=0.5)
        self.play(Write(f3), run_time=0.5)

        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(diag_AC), FadeOut(diag_BD),
            FadeOut(lbl_AC), FadeOut(lbl_BD),
            FadeOut(O_dot), FadeOut(O_lbl),
            FadeOut(mid_ticks), FadeOut(right_o),
            FadeOut(formulas),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════════════
    # Scene 5: 判定1 — 矩形 + 邻边相等
    # ══════════════════════════════════════════════════════════════
    def scene_5_determine_rect(self):
        title = Text("判定方法一", font="PingFang SC",
                     font_size=34, color=HL_COLOR)
        title.move_to(UP * 6.3)
        self.play(Write(title), run_time=0.5)

        sub = Text("矩形 + 一组邻边相等 ⟹ 正方形",
                   font="PingFang SC", font_size=23, color=RECT_CLR)
        sub.move_to(UP * 5.5)
        self.play(FadeIn(sub), run_time=0.5)

        # ── 步骤1：展示矩形（非正方形）
        step1 = Text("第一步：有一个矩形",
                     font="PingFang SC", font_size=22, color=GRAY_A)
        step1.move_to(DOWN * 3.8)

        rect = Polygon(self.rect_A, self.rect_B, self.rect_C, self.rect_D,
                       color=RECT_CLR, stroke_width=3)
        # 四个直角标记
        rect_ra = VGroup(
            self._right_angle_mark(self.rect_A, self.rect_B, self.rect_D, size=0.22, color=RECT_CLR),
            self._right_angle_mark(self.rect_B, self.rect_C, self.rect_A, size=0.22, color=RECT_CLR),
            self._right_angle_mark(self.rect_C, self.rect_D, self.rect_B, size=0.22, color=RECT_CLR),
            self._right_angle_mark(self.rect_D, self.rect_A, self.rect_C, size=0.22, color=RECT_CLR),
        )

        self.play(Create(rect), run_time=1.0)
        self.play(FadeIn(rect_ra), FadeIn(step1), run_time=0.5)
        self.wait(0.5)

        # ── 步骤2：添加邻边相等条件
        step2 = Text("第二步：添加条件  AB = BC",
                     font="PingFang SC", font_size=22, color=EQUAL_CLR)
        step2.move_to(DOWN * 4.6)

        # 高亮 AB 和 BC
        hl_ab = Line(self.rect_A, self.rect_B, color=EQUAL_CLR, stroke_width=5)
        hl_bc = Line(self.rect_B, self.rect_C, color=EQUAL_CLR, stroke_width=5)
        tick_ab = self._tick_mark(self.rect_A, self.rect_B, n=1)
        tick_bc = self._tick_mark(self.rect_B, self.rect_C, n=1)

        self.play(
            Create(hl_ab), Create(hl_bc),
            FadeIn(tick_ab), FadeIn(tick_bc),
            FadeIn(step2),
            run_time=0.7
        )
        self.wait(0.8)

        # ── 步骤3：Transform 矩形 → 正方形
        step3 = Text("⟹  变成正方形！",
                     font="PingFang SC", font_size=26, color=HL_COLOR)
        step3.move_to(DOWN * 5.4)

        new_sq = self.main_sq.copy()
        self.play(
            Transform(rect, new_sq),
            FadeOut(hl_ab), FadeOut(hl_bc),
            FadeOut(tick_ab), FadeOut(tick_bc),
            FadeOut(rect_ra),
            FadeIn(step3),
            run_time=1.2
        )

        # 公式
        formula = VGroup(
            Text("矩形", font="PingFang SC", font_size=24, color=RECT_CLR),
            MathTex(r"+", font_size=28),
            Text("一组邻边相等", font="PingFang SC", font_size=24, color=EQUAL_CLR),
            MathTex(r"\Rightarrow", font_size=28, color=HL_COLOR),
            Text("正方形", font="PingFang SC", font_size=24, color=SQUARE_COLOR),
        ).arrange(RIGHT, buff=0.2)
        formula.move_to(DOWN * 3.5)

        self.play(
            FadeOut(step1), FadeOut(step2), FadeOut(step3),
            FadeIn(formula),
            run_time=0.6
        )
        self.wait(1.8)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(rect), FadeOut(formula),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════════════
    # Scene 6: 判定2 — 菱形 + 一个直角
    # ══════════════════════════════════════════════════════════════
    def scene_6_determine_rhombus(self):
        title = Text("判定方法二", font="PingFang SC",
                     font_size=34, color=HL_COLOR)
        title.move_to(UP * 6.3)
        self.play(Write(title), run_time=0.5)

        sub = Text("菱形 + 一个直角 ⟹ 正方形",
                   font="PingFang SC", font_size=24, color=RHOMBUS_CLR)
        sub.move_to(UP * 5.5)
        self.play(FadeIn(sub), run_time=0.5)

        # ── 步骤1：展示菱形
        step1 = Text("第一步：有一个菱形（四边相等）",
                     font="PingFang SC", font_size=22, color=GRAY_A)
        step1.move_to(DOWN * 3.8)

        rhombus = Polygon(self.rh_A, self.rh_B, self.rh_C, self.rh_D,
                          color=RHOMBUS_CLR, stroke_width=3)
        rh_ticks = VGroup(
            self._tick_mark(self.rh_A, self.rh_B, n=1, color=RHOMBUS_CLR),
            self._tick_mark(self.rh_B, self.rh_C, n=1, color=RHOMBUS_CLR),
            self._tick_mark(self.rh_C, self.rh_D, n=1, color=RHOMBUS_CLR),
            self._tick_mark(self.rh_D, self.rh_A, n=1, color=RHOMBUS_CLR),
        )

        self.play(Create(rhombus), run_time=1.0)
        self.play(FadeIn(rh_ticks), FadeIn(step1), run_time=0.5)
        self.wait(0.5)

        # ── 步骤2：在顶点 rh_A 处添加直角标记
        step2 = Text("第二步：其中一个角是直角",
                     font="PingFang SC", font_size=22, color=EQUAL_CLR)
        step2.move_to(DOWN * 4.6)

        # rh_A 角：相邻顶点是 rh_D（上）和 rh_B（下）
        rm_A = self._right_angle_mark(self.rh_A, self.rh_B, self.rh_D,
                                      size=0.22, color=RIGHT_MK_CLR)

        # 注意：rh_A 的角其实不是90°（菱形对角线不等），这里是"添加条件"，
        # 动画上用标记表示我们声称它是直角，然后变形为正方形
        self.play(FadeIn(rm_A), FadeIn(step2), run_time=0.6)
        self.wait(0.8)

        # ── 步骤3：变形为正方形
        step3 = Text("⟹  变成正方形！",
                     font="PingFang SC", font_size=26, color=HL_COLOR)
        step3.move_to(DOWN * 5.4)

        new_sq2 = self.main_sq.copy()
        self.play(
            Transform(rhombus, new_sq2),
            FadeOut(rh_ticks), FadeOut(rm_A),
            FadeIn(step3),
            run_time=1.2
        )

        # 公式
        formula2 = VGroup(
            Text("菱形", font="PingFang SC", font_size=24, color=RHOMBUS_CLR),
            MathTex(r"+", font_size=28),
            Text("一个直角", font="PingFang SC", font_size=24, color=EQUAL_CLR),
            MathTex(r"\Rightarrow", font_size=28, color=HL_COLOR),
            Text("正方形", font="PingFang SC", font_size=24, color=SQUARE_COLOR),
        ).arrange(RIGHT, buff=0.2)
        formula2.move_to(DOWN * 3.5)

        self.play(
            FadeOut(step1), FadeOut(step2), FadeOut(step3),
            FadeIn(formula2),
            run_time=0.6
        )
        self.wait(1.8)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(rhombus), FadeOut(formula2),
            run_time=0.5
        )

    # ══════════════════════════════════════════════════════════════
    # Scene 7: 总结 + 片尾
    # ══════════════════════════════════════════════════════════════
    def scene_7_summary_outro(self):
        # 大标题
        summary_title = Text("总结", font="PingFang SC",
                             font_size=40, color=HL_COLOR)
        summary_title.move_to(UP * 6.3)
        self.play(Write(summary_title), run_time=0.5)

        # 正方形图（小一点，移到上区）
        sq_small = Square(side_length=2.0, color=SQUARE_COLOR, stroke_width=3)
        sq_small.move_to(UP * 4.5)
        self.play(Create(sq_small), run_time=0.7)

        # 卡片式总结
        cards_data = [
            ("🔶  四边相等", r"AB=BC=CD=DA", EQUAL_CLR),
            ("🔷  四角直角", r"90^\circ", RIGHT_MK_CLR),
            ("🔸  对角线等且垂直平分", r"AC=BD,\ AC\perp BD", DIAG_COLOR1),
        ]

        card_y = [2.3, 1.1, -0.2]
        card_mobs = VGroup()

        for i, (text_str, math_str, clr) in enumerate(cards_data):
            bg = RoundedRectangle(corner_radius=0.2, width=7.5, height=0.75,
                                  fill_color="#16213e", fill_opacity=1,
                                  stroke_color=clr, stroke_width=2)
            bg.move_to(np.array([0, card_y[i], 0]))

            label = Text(text_str, font="PingFang SC",
                         font_size=22, color=clr)
            label.move_to(bg.get_center() + LEFT * 1.5)

            formula = MathTex(math_str, font_size=22, color=WHITE)
            formula.move_to(bg.get_center() + RIGHT * 2.0)

            card = VGroup(bg, label, formula)
            card_mobs.add(card)
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.4)

        # 判定方法
        det_title = Text("判定：", font="PingFang SC",
                         font_size=26, color=WHITE)
        det_title.move_to(DOWN * 1.5 + LEFT * 2.8)
        self.play(FadeIn(det_title), run_time=0.3)

        det_cards_data = [
            ("矩形 + 邻边相等", RECT_CLR),
            ("菱形 + 一个直角", RHOMBUS_CLR),
        ]
        det_y = [-2.4, -3.2]
        det_mobs = VGroup()
        for i, (txt, clr) in enumerate(det_cards_data):
            line = VGroup(
                Text("⟹  正方形", font="PingFang SC",
                     font_size=21, color=HL_COLOR),
            )
            lbl = Text(txt, font="PingFang SC", font_size=21, color=clr)
            row = VGroup(lbl, line).arrange(RIGHT, buff=0.4)
            row.move_to(np.array([0, det_y[i], 0]))
            det_mobs.add(row)
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.4)

        self.wait(1.5)

        # 片尾
        self.play(
            FadeOut(summary_title),
            FadeOut(sq_small),
            FadeOut(card_mobs),
            FadeOut(det_title),
            FadeOut(det_mobs),
            FadeOut(self.main_sq),
            FadeOut(self.vtx_labels),
            run_time=0.6
        )

        # 作者放大
        author_big = Text("上海初高中数学直通车",
                          font="PingFang SC", font_size=38,
                          color=WHITE, weight=BOLD)
        author_big.move_to(UP * 1.5)

        author_id = Text("@emptyandcalm",
                         font="PingFang SC", font_size=30, color=GRAY_B)
        author_id.move_to(UP * 0.5)

        follow = Text("关注我，获得更多数学技巧！",
                      font="PingFang SC", font_size=28, color=HL_COLOR)
        follow.move_to(DOWN * 0.8)

        self.play(
            Transform(self.author, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 装饰小正方形
        deco = VGroup(*[
            Square(side_length=0.35, color=SQUARE_COLOR,
                   fill_color=SQUARE_COLOR, fill_opacity=0.6,
                   stroke_width=0)
            .move_to(DOWN * 2.5 + LEFT * (1.5 - i * 0.75))
            for i in range(5)
        ])
        self.play(*[FadeIn(d, scale=0.3) for d in deco], run_time=0.5)
        self.play(Rotate(deco, angle=PI/4), run_time=0.8)

        self.wait(1.5)
        self.play(FadeOut(self.author), FadeOut(author_id),
                  FadeOut(follow), FadeOut(deco), run_time=0.8)
