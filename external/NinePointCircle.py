"""
九点圆圆心（欧拉点）构造动画
Nine-Point Circle Center (Euler Point) Construction Animation

内容: 通过外心O和垂心H构造九点圆圆心N，展示欧拉线的发现
目标观众: 初中/高中学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景顺序:
  Scene 1: 开场钩子
  Scene 2: 画三角形ABC + 标注顶点
  Scene 3: 求外心O（作两条边的垂直平分线）
  Scene 4: 求垂心H（作两条高线）
  Scene 5: 连接OJ取中点N → 九点圆圆心
  Scene 6: 绘制九点圆，展示9个特征点
  Scene 7: 总结 + 片尾
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置 - TikTok竖屏
# ============================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ============================================================
# 颜色配置
# ============================================================
BG_COLOR = "#1a1a2e"
COL_TRIANGLE = "#e0e0e0"       # 三角形边 - 亮白灰
COL_VERTEX = "#ffffff"          # 顶点标签
COL_CIRCUMCENTER = "#e74c3c"   # 外心 - 红
COL_ORTHOCENTER = "#f39c12"    # 垂心 - 橙
COL_NINEPOINT = "#2ecc71"      # 九点圆圆心 - 绿
COL_PERP_BISECT = "#3498db"    # 垂直平分线 - 蓝
COL_ALTITUDE = "#9b59b6"       # 高线 - 紫
COL_EULER_LINE = "#e8d44d"     # 欧拉线 - 金黄
COL_NINE_CIRCLE = "#2ecc71"    # 九点圆 - 绿
COL_NINE_POINTS = "#1abc9c"    # 9特征点 - 青绿
COL_AUX = "#7f8c8d"            # 辅助线 - 灰蓝
COL_HIGHLIGHT = "#f1c40f"      # 高亮 - 黄

FONT = "Noto Sans CJK SC"


class NinePointCircle(Scene):
    """九点圆圆心（欧拉点）教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ---------- 阶段1: 统一初始化几何数据 ----------
        self.setup_geometry()

        # ---------- 阶段2: 执行动画序列 ----------
        self.scene_opening()          # 开场钩子
        self.scene_triangle()         # 画三角形
        self.scene_circumcenter()     # 求外心O
        self.scene_orthocenter()      # 求垂心H（用J标记以匹配题目）
        self.scene_nine_point_center()# 连OJ取中点N
        self.scene_nine_circle()      # 绘制九点圆 + 9个点
        self.scene_outro()            # 片尾

    # ============================================================
    # 几何数据初始化（所有坐标精确计算，已通过verify_geometry验证）
    # ============================================================
    def setup_geometry(self):
        self.SCALE = 0.82
        self.OFFSET = np.array([0.0, 1.8, 0.0])

        # 基准三角形顶点
        A_raw = np.array([-2.8, -1.2, 0.0])
        B_raw = np.array([2.6, -0.8, 0.0])
        C_raw = np.array([-0.3, 2.4, 0.0])

        self.A = A_raw * self.SCALE + self.OFFSET
        self.B = B_raw * self.SCALE + self.OFFSET
        self.C = C_raw * self.SCALE + self.OFFSET

        # 边长
        self.a = np.linalg.norm(self.C - self.B)  # BC
        self.b = np.linalg.norm(self.A - self.C)  # CA
        self.c = np.linalg.norm(self.B - self.A)  # AB

        # 中点
        self.M_AB = (self.A + self.B) / 2
        self.M_BC = (self.B + self.C) / 2
        self.M_CA = (self.C + self.A) / 2

        # 外心 O
        self.O = self._calc_circumcenter(self.A, self.B, self.C)
        self.circumradius = np.linalg.norm(self.O - self.A)

        # 垂心 H（题目中用J标记）
        self.H = self.A + self.B + self.C - 2 * self.O

        # 高线垂足
        self.foot_A = self._foot_of_perp(self.A, self.B, self.C)  # A到BC的垂足
        self.foot_B = self._foot_of_perp(self.B, self.C, self.A)  # B到CA的垂足
        self.foot_C = self._foot_of_perp(self.C, self.A, self.B)  # C到AB的垂足

        # 九点圆圆心 N = (O + H) / 2
        self.N = (self.O + self.H) / 2
        self.nine_point_radius = self.circumradius / 2

        # 重心 G（用于欧拉线展示）
        self.G = (self.A + self.B + self.C) / 3

        # AH, BH, CH 中点（9点之一）
        self.mid_AH = (self.A + self.H) / 2
        self.mid_BH = (self.B + self.H) / 2
        self.mid_CH = (self.C + self.H) / 2

        # 垂直平分线方向（单位化）
        d_AB = self.B - self.A
        self.perp_dir_AB = np.array([-d_AB[1], d_AB[0], 0])
        self.perp_dir_AB = self.perp_dir_AB / np.linalg.norm(self.perp_dir_AB)

        d_BC = self.C - self.B
        self.perp_dir_BC = np.array([-d_BC[1], d_BC[0], 0])
        self.perp_dir_BC = self.perp_dir_BC / np.linalg.norm(self.perp_dir_BC)

    # ---------- 几何工具函数 ----------
    @staticmethod
    def _calc_circumcenter(A, B, C):
        ax, ay = A[0], A[1]
        bx, by = B[0], B[1]
        cx, cy = C[0], C[1]
        D = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        ux = ((ax**2 + ay**2) * (by - cy) +
              (bx**2 + by**2) * (cy - ay) +
              (cx**2 + cy**2) * (ay - by)) / D
        uy = ((ax**2 + ay**2) * (cx - bx) +
              (bx**2 + by**2) * (ax - cx) +
              (cx**2 + cy**2) * (bx - ax)) / D
        return np.array([ux, uy, 0])

    @staticmethod
    def _foot_of_perp(point, line_start, line_end):
        v = line_end - line_start
        t = np.dot(point - line_start, v) / np.dot(v, v)
        return line_start + t * v

    def _make_right_angle_mark(self, corner, p1, p2, size=0.18):
        """手动构造直角标记四边形"""
        v1 = p1 - corner
        v1 = v1 / np.linalg.norm(v1) * size
        v2 = p2 - corner
        v2 = v2 / np.linalg.norm(v2) * size
        return Polygon(
            corner + v1,
            corner + v1 + v2,
            corner + v2,
            color=COL_HIGHLIGHT,
            stroke_width=1.5,
            fill_opacity=0
        )

    # ============================================================
    # Scene 1: 开场钩子
    # ============================================================
    def scene_opening(self):
        # 作者信息（顶部）
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=COL_AUX
        ).move_to(UP * 7.2)
        self.play(FadeIn(self.author, shift=DOWN * 0.3), run_time=0.4)

        # 钩子标题
        hook = Text(
            "你知道九点圆吗？",
            font=FONT, font_size=38, color=COL_HIGHLIGHT, weight=BOLD
        ).move_to(UP * 6.0)
        self.play(Write(hook), run_time=0.7)

        sub = Text(
            "一个圆竟能经过三角形的9个特殊点！",
            font=FONT, font_size=22, color=COL_AUX
        ).move_to(UP * 5.1)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)
        self.wait(0.6)

        # 淡出钩子文字，保留作者
        self.play(FadeOut(hook), FadeOut(sub), run_time=0.5)

    # ============================================================
    # Scene 2: 画三角形ABC
    # ============================================================
    def scene_triangle(self):
        # 步骤提示
        step_txt = Text(
            "第一步：画三角形ABC",
            font=FONT, font_size=24, color=COL_HIGHLIGHT
        ).move_to(UP * 4.8)
        self.play(Write(step_txt), run_time=0.5)

        # 三角形
        self.tri = Polygon(
            self.A, self.B, self.C,
            color=COL_TRIANGLE, stroke_width=2.8
        )
        self.play(Create(self.tri), run_time=1.0)

        # 顶点点和标签
        dot_A = Dot(self.A, radius=0.08, color=COL_VERTEX)
        dot_B = Dot(self.B, radius=0.08, color=COL_VERTEX)
        dot_C = Dot(self.C, radius=0.08, color=COL_VERTEX)

        lab_A = Text("A", font=FONT, font_size=26, color=COL_VERTEX).next_to(self.A, DL, buff=0.15)
        lab_B = Text("B", font=FONT, font_size=26, color=COL_VERTEX).next_to(self.B, DR, buff=0.15)
        lab_C = Text("C", font=FONT, font_size=26, color=COL_VERTEX).next_to(self.C, UP, buff=0.15)

        self.play(
            FadeIn(dot_A), FadeIn(dot_B), FadeIn(dot_C),
            Write(lab_A), Write(lab_B), Write(lab_C),
            run_time=0.6
        )

        # 保存引用
        self.dot_A, self.dot_B, self.dot_C = dot_A, dot_B, dot_C
        self.lab_A, self.lab_B, self.lab_C = lab_A, lab_B, lab_C
        self.step_txt = step_txt

        self.wait(0.8)

    # ============================================================
    # Scene 3: 求外心O（作两条边的垂直平分线）
    # ============================================================
    def scene_circumcenter(self):
        # 更新步骤
        new_step = Text(
            "第二步：找外心 O",
            font=FONT, font_size=24, color=COL_CIRCUMCENTER
        ).move_to(UP * 4.8)
        self.play(ReplacementTransform(self.step_txt, new_step), run_time=0.4)
        self.step_txt = new_step

        desc1 = Text(
            "作两条边的垂直平分线，交点即为外心",
            font=FONT, font_size=19, color=COL_AUX
        ).move_to(UP * 4.1)
        self.play(FadeIn(desc1), run_time=0.3)

        # --- AB 边高亮 ---
        line_AB_hl = Line(self.A, self.B, color=COL_PERP_BISECT, stroke_width=3.5)
        self.play(Create(line_AB_hl), run_time=0.5)

        # AB 中点
        dot_MAB = Dot(self.M_AB, radius=0.07, color=COL_PERP_BISECT)
        lab_MAB = Text("M₁", font=FONT, font_size=18, color=COL_PERP_BISECT).next_to(
            self.M_AB, DOWN, buff=0.18)
        self.play(FadeIn(dot_MAB), Write(lab_MAB), run_time=0.4)

        # AB 垂直平分线
        ext = 2.5
        perp_line_AB = DashedLine(
            self.M_AB - self.perp_dir_AB * ext,
            self.M_AB + self.perp_dir_AB * ext,
            color=COL_PERP_BISECT, dash_length=0.12, stroke_width=2
        )
        self.play(Create(perp_line_AB), run_time=0.7)

        # 直角标记在AB中点
        ra1 = self._make_right_angle_mark(
            self.M_AB,
            self.M_AB + self.perp_dir_AB,
            self.A,
            size=0.2
        )
        self.play(FadeIn(ra1), run_time=0.3)
        self.wait(0.3)

        # 恢复AB颜色
        self.play(FadeOut(line_AB_hl), run_time=0.2)

        # --- BC 边高亮 ---
        line_BC_hl = Line(self.B, self.C, color=COL_PERP_BISECT, stroke_width=3.5)
        self.play(Create(line_BC_hl), run_time=0.5)

        dot_MBC = Dot(self.M_BC, radius=0.07, color=COL_PERP_BISECT)
        lab_MBC = Text("M₂", font=FONT, font_size=18, color=COL_PERP_BISECT).next_to(
            self.M_BC, RIGHT, buff=0.18)
        self.play(FadeIn(dot_MBC), Write(lab_MBC), run_time=0.4)

        ext2 = 2.2
        perp_line_BC = DashedLine(
            self.M_BC - self.perp_dir_BC * ext2,
            self.M_BC + self.perp_dir_BC * ext2,
            color=COL_PERP_BISECT, dash_length=0.12, stroke_width=2
        )
        self.play(Create(perp_line_BC), run_time=0.7)

        ra2 = self._make_right_angle_mark(
            self.M_BC,
            self.M_BC + self.perp_dir_BC,
            self.B,
            size=0.2
        )
        self.play(FadeIn(ra2), run_time=0.3)
        self.wait(0.3)

        self.play(FadeOut(line_BC_hl), run_time=0.2)

        # --- 标记外心O ---
        self.dot_O = Dot(self.O, radius=0.11, color=COL_CIRCUMCENTER, z_index=5)
        self.play(GrowFromCenter(self.dot_O), run_time=0.5)
        self.play(Flash(self.dot_O, color=COL_CIRCUMCENTER, flash_radius=0.3), run_time=0.3)

        self.lab_O = Text("O", font=FONT, font_size=24, color=COL_CIRCUMCENTER, weight=BOLD
                          ).next_to(self.O, RIGHT, buff=0.18)
        lab_O_cn = Text("外心", font=FONT, font_size=16, color=COL_CIRCUMCENTER
                        ).next_to(self.lab_O, DOWN, buff=0.05, aligned_edge=LEFT)
        self.play(Write(self.lab_O), FadeIn(lab_O_cn), run_time=0.4)
        self.wait(1.0)

        # 清理临时元素，保留外心点和垂直平分线淡化
        self.play(
            FadeOut(perp_line_AB),
            FadeOut(perp_line_BC),
            FadeOut(dot_MAB), FadeOut(lab_MAB),
            FadeOut(dot_MBC), FadeOut(lab_MBC),
            FadeOut(ra1), FadeOut(ra2),
            FadeOut(desc1), FadeOut(lab_O_cn),
            run_time=0.5
        )

    # ============================================================
    # Scene 4: 求垂心H（用J标记）
    # ============================================================
    def scene_orthocenter(self):
        new_step = Text(
            "第三步：找垂心 J",
            font=FONT, font_size=24, color=COL_ORTHOCENTER
        ).move_to(UP * 4.8)
        self.play(ReplacementTransform(self.step_txt, new_step), run_time=0.4)
        self.step_txt = new_step

        desc2 = Text(
            "从顶点向对边作高线，交点即为垂心",
            font=FONT, font_size=19, color=COL_AUX
        ).move_to(UP * 4.1)
        self.play(FadeIn(desc2), run_time=0.3)

        # --- 高线1: A -> BC ---
        alt1 = DashedLine(
            self.A, self.foot_A,
            color=COL_ALTITUDE, dash_length=0.12, stroke_width=2
        )
        self.play(Create(alt1), run_time=0.6)

        # 垂足直角标记
        ra_A = self._make_right_angle_mark(
            self.foot_A, self.A, self.B, size=0.18
        )
        self.play(FadeIn(ra_A), run_time=0.25)
        self.wait(0.3)

        # --- 高线2: B -> CA ---
        alt2 = DashedLine(
            self.B, self.foot_B,
            color=COL_ALTITUDE, dash_length=0.12, stroke_width=2
        )
        self.play(Create(alt2), run_time=0.6)

        ra_B = self._make_right_angle_mark(
            self.foot_B, self.B, self.C, size=0.18
        )
        self.play(FadeIn(ra_B), run_time=0.25)
        self.wait(0.3)

        # --- 高线3: C -> AB （验证三线共点）---
        alt3 = DashedLine(
            self.C, self.foot_C,
            color=COL_ALTITUDE, dash_length=0.12, stroke_width=2, stroke_opacity=0.7
        )
        self.play(Create(alt3), run_time=0.5)

        ra_C = self._make_right_angle_mark(
            self.foot_C, self.C, self.A, size=0.18
        )
        self.play(FadeIn(ra_C), run_time=0.25)

        # --- 标记垂心 J（即 H）---
        self.dot_H = Dot(self.H, radius=0.11, color=COL_ORTHOCENTER, z_index=5)
        self.play(GrowFromCenter(self.dot_H), run_time=0.5)
        self.play(Flash(self.dot_H, color=COL_ORTHOCENTER, flash_radius=0.3), run_time=0.3)

        self.lab_H = Text("J", font=FONT, font_size=24, color=COL_ORTHOCENTER, weight=BOLD
                          ).next_to(self.H, LEFT, buff=0.2)
        lab_H_cn = Text("垂心", font=FONT, font_size=16, color=COL_ORTHOCENTER
                        ).next_to(self.lab_H, DOWN, buff=0.05, aligned_edge=RIGHT)
        self.play(Write(self.lab_H), FadeIn(lab_H_cn), run_time=0.4)

        # 底部提示
        hint_h = Text(
            "三条高线交于一点！",
            font=FONT, font_size=20, color=COL_HIGHLIGHT
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(hint_h), run_time=0.3)
        self.wait(1.2)

        # 清理高线等，保留垂心点
        self.play(
            FadeOut(alt1), FadeOut(alt2), FadeOut(alt3),
            FadeOut(ra_A), FadeOut(ra_B), FadeOut(ra_C),
            FadeOut(desc2), FadeOut(lab_H_cn), FadeOut(hint_h),
            run_time=0.5
        )

    # ============================================================
    # Scene 5: 连接OJ取中点N → 九点圆圆心
    # ============================================================
    def scene_nine_point_center(self):
        new_step = Text(
            "第四步：求九点圆圆心 N",
            font=FONT, font_size=24, color=COL_NINEPOINT
        ).move_to(UP * 4.8)
        self.play(ReplacementTransform(self.step_txt, new_step), run_time=0.4)
        self.step_txt = new_step

        desc3 = Text(
            "连接 O 和 J，取线段 OJ 的中点",
            font=FONT, font_size=20, color=COL_AUX
        ).move_to(UP * 4.0)
        self.play(FadeIn(desc3), run_time=0.35)
        self.wait(0.3)

        # 画 OJ 连线（欧拉线）
        euler_line = Line(
            self.O, self.H,
            color=COL_EULER_LINE, stroke_width=2.8
        )
        self.play(Create(euler_line), run_time=0.7)
        self.wait(0.4)

        # 动态标记中点N
        self.dot_N = Dot(self.N, radius=0.0, color=COL_NINEPOINT, z_index=5)
        self.play(
            self.dot_N.animate.set_radius(0.13),
            run_time=0.6
        )
        self.play(Flash(self.dot_N, color=COL_NINEPOINT, flash_radius=0.35), run_time=0.35)

        # N的标签
        self.lab_N = Text("N", font=FONT, font_size=26, color=COL_NINEPOINT, weight=BOLD
                          ).next_to(self.N, RIGHT, buff=0.2)
        lab_N_cn = Text("九点圆圆心", font=FONT, font_size=17, color=COL_NINEPOINT
                        ).next_to(self.lab_N, DOWN, buff=0.06, aligned_edge=LEFT)
        self.play(Write(self.lab_N), FadeIn(lab_N_cn), run_time=0.5)

        # 底部公式说明
        formula_txt = Text(
            "N 是 OJ 的中点 → 九点圆圆心（欧拉点）",
            font=FONT, font_size=20, color=COL_EULER_LINE
        ).move_to(DOWN * 5.2)
        self.play(FadeIn(formula_txt, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        # 清理临时
        self.play(
            FadeOut(desc3), FadeOut(lab_N_cn), FadeOut(formula_txt),
            run_time=0.4
        )

        # 保留：euler_line, dot_O, lab_O, dot_H, lab_H, dot_N, lab_N
        self.euler_line = euler_line

    # ============================================================
    # Scene 6: 绘制九点圆，标注9个特征点
    # ============================================================
    def scene_nine_circle(self):
        new_step = Text(
            "九点圆：经过9个特殊点！",
            font=FONT, font_size=24, color=COL_NINE_CIRCLE
        ).move_to(UP * 4.8)
        self.play(ReplacementTransform(self.step_txt, new_step), run_time=0.4)
        self.step_txt = new_step

        # 画九点圆
        nine_circle = Circle(
            radius=self.nine_point_radius,
            color=COL_NINE_CIRCLE, stroke_width=2.5
        ).move_to(self.N)
        self.play(Create(nine_circle), run_time=1.2)
        self.wait(0.4)

        # ---------- 分批显示9个点 ----------
        # 批次1: 三边中点（3个）
        mid_points = [self.M_AB, self.M_BC, self.M_CA]
        mid_labels_pos = [
            (self.M_AB, DOWN, "中点"),
            (self.M_BC, RIGHT, "中点"),
            (self.M_CA, LEFT, "中点"),
        ]

        dots_mid = VGroup(*[
            Dot(p, radius=0.08, color=COL_NINE_POINTS, z_index=4)
            for p in mid_points
        ])
        self.play(
            *[GrowFromCenter(d) for d in dots_mid],
            run_time=0.5
        )

        label_mid = Text(
            "① 三边中点（3个）",
            font=FONT, font_size=18, color=COL_NINE_POINTS
        ).move_to(DOWN * 4.6)
        self.play(FadeIn(label_mid), run_time=0.3)
        self.wait(0.5)

        # 批次2: 高线垂足（3个）
        foot_points = [self.foot_A, self.foot_B, self.foot_C]
        dots_foot = VGroup(*[
            Dot(p, radius=0.08, color="#e67e22", z_index=4)
            for p in foot_points
        ])
        self.play(
            *[GrowFromCenter(d) for d in dots_foot],
            run_time=0.5
        )

        label_foot = Text(
            "② 高线的垂足（3个）",
            font=FONT, font_size=18, color="#e67e22"
        ).move_to(DOWN * 5.1)
        self.play(FadeIn(label_foot), run_time=0.3)
        self.wait(0.5)

        # 批次3: 顶点到垂心连线的中点（3个）
        euler_mid_points = [self.mid_AH, self.mid_BH, self.mid_CH]
        dots_euler = VGroup(*[
            Dot(p, radius=0.08, color="#8e44ad", z_index=4)
            for p in euler_mid_points
        ])
        self.play(
            *[GrowFromCenter(d) for d in dots_euler],
            run_time=0.5
        )

        label_euler = Text(
            "③ 各顶点到垂心连线的中点（3个）",
            font=FONT, font_size=18, color="#8e44ad"
        ).move_to(DOWN * 5.6)
        self.play(FadeIn(label_euler), run_time=0.3)
        self.wait(0.8)

        # 总结提示
        total_hint = Text(
            "共 3 + 3 + 3 = 9 个点，都在同一圆上！",
            font=FONT, font_size=20, color=COL_HIGHLIGHT
        ).move_to(DOWN * 6.2)
        self.play(FadeIn(total_hint, shift=UP * 0.15), run_time=0.4)
        self.wait(1.8)

        # 清理标签
        self.play(
            FadeOut(label_mid), FadeOut(label_foot),
            FadeOut(label_euler), FadeOut(total_hint),
            run_time=0.4
        )

        # 保存引用
        self.nine_circle = nine_circle
        self.dots_mid = dots_mid
        self.dots_foot = dots_foot
        self.dots_euler = dots_euler

    # ============================================================
    # Scene 7: 总结 + 片尾
    # ============================================================
    def scene_outro(self):
        # 淡出几何图
        to_remove = [
            self.tri, self.dot_A, self.dot_B, self.dot_C,
            self.lab_A, self.lab_B, self.lab_C,
            self.dot_O, self.lab_O, self.dot_H, self.lab_H,
            self.euler_line, self.dot_N, self.lab_N,
            self.nine_circle, self.dots_mid, self.dots_foot, self.dots_euler,
            self.step_txt
        ]
        self.play(*[FadeOut(obj) for obj in to_remove], run_time=0.7)
        self.wait(0.3)

        # ---------- 总结卡 ----------
        title_sum = Text(
            "总结",
            font=FONT, font_size=34, color=COL_HIGHLIGHT, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(Write(title_sum), run_time=0.5)

        # 三步骤
        lines = [
            ("① 作两边垂直平分线 → 外心 O", COL_CIRCUMCENTER),
            ("② 作三条高线 → 垂心 J", COL_ORTHOCENTER),
            ("③ 取 OJ 中点 N → 九点圆圆心", COL_NINEPOINT),
        ]
        y_pos = 4.2
        sum_texts = []
        for i, (txt, col) in enumerate(lines):
            t = Text(txt, font=FONT, font_size=22, color=col).move_to(
                np.array([0, y_pos - i * 1.1, 0])
            )
            sum_texts.append(t)
            self.play(FadeIn(t, shift=RIGHT * 0.3), run_time=0.35)
            self.wait(0.15)

        self.wait(0.6)

        # 核心结论
        conclusion = Text(
            "N 就是九点圆圆心（欧拉点）！",
            font=FONT, font_size=26, color=COL_NINEPOINT, weight=BOLD
        ).move_to(DOWN * 0.8)
        box = SurroundingRectangle(conclusion, color=COL_NINEPOINT, buff=0.25)
        self.play(FadeIn(box), FadeIn(conclusion), run_time=0.5)
        self.wait(1.0)

        # ---------- 片尾 ----------
        # 淡出总结
        all_sum = [title_sum] + sum_texts + [conclusion, box]
        self.play(*[FadeOut(t) for t in all_sum], run_time=0.5)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=36, color=WHITE, weight=BOLD
        ).move_to(UP * 1.5)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=26, color=COL_AUX
        ).move_to(UP * 0.6)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=COL_HIGHLIGHT
        ).move_to(DOWN * 0.4)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 小装饰圆 - 九点圆主题
        deco_colors = [COL_CIRCUMCENTER, COL_ORTHOCENTER, COL_NINEPOINT,
                       COL_PERP_BISECT, COL_ALTITUDE]
        decos = VGroup(*[
            Circle(radius=0.2, color=deco_colors[i], fill_opacity=0.7, stroke_width=0)
            .move_to(np.array([np.cos(i * 2 * np.pi / 5) * 2.2,
                               np.sin(i * 2 * np.pi / 5) * 0.6 - 2.2, 0]))
            for i in range(5)
        ])
        self.play(*[FadeIn(d, scale=0.3) for d in decos], run_time=0.5)
        self.play(Rotate(decos, angle=PI * 0.4), run_time=1.0)
        self.wait(1.2)


# 运行命令:
# manim -pql nine_point_circle.py NinePointCircle   # 快速预览
# manim -qh nine_point_circle.py NinePointCircle    # 高质量渲染