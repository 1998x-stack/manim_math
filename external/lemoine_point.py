"""
来莫恩点 (Lemoine Point / Symmedian Point) 教学动画
Lemoine Point Animation - Triangle Geometry

内容: 类似中线的定义、构造、来莫恩点的存在性、核心性质
目标观众: 高中数学学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景安排:
  Scene 1: 开场 + 钩子
  Scene 2: 回顾中线与重心
  Scene 3: 角平分线与等角共轭的铺垫
  Scene 4: 类似中线的构造（反射中线）
  Scene 5: 来莫恩点 — 三线共点
  Scene 6: 核心性质：比例分割与面积比
  Scene 7: 核心性质：到三边距离平方和最小
  Scene 8: 片尾 + 关注
"""

from manim import *
import numpy as np


# ====================================================================
# 全局配置 — TikTok 竖屏
# ====================================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ====================================================================
# 几何计算工具库
# ====================================================================
class GC:
    """Geometry Calculator — 所有点必须经此计算"""

    @staticmethod
    def midpoint(P1, P2):
        return (P1 + P2) / 2

    @staticmethod
    def unit(v):
        n = np.linalg.norm(v)
        return v / n if n > 1e-15 else v

    @staticmethod
    def foot(point, L1, L2):
        """垂足"""
        d = L2 - L1
        t = np.dot(point - L1, d) / np.dot(d, d)
        return L1 + t * d

    @staticmethod
    def line_intersect(P1, D1, P2, D2):
        """两直线交点"""
        A = np.array([[D1[0], -D2[0]], [D1[1], -D2[1]]])
        b = np.array([P2[0] - P1[0], P2[1] - P1[1]])
        det = np.linalg.det(A)
        if abs(det) < 1e-12:
            return None
        params = np.linalg.solve(A, b)
        return np.array([P1[0] + params[0] * D1[0], P1[1] + params[0] * D1[1], 0])

    @staticmethod
    def reflect_vector(v, axis):
        """将向量 v 关于 axis 方向做反射"""
        ax = GC.unit(axis)
        return 2 * np.dot(v, ax) * ax - v

    @staticmethod
    def dist_to_line(P, L1, L2):
        d = L2 - L1
        n = np.array([-d[1], d[0], 0])
        n = n / np.linalg.norm(n)
        return abs(np.dot(P - L1, n))

    @staticmethod
    def tri_area(P1, P2, P3):
        return 0.5 * abs(
            P1[0] * (P2[1] - P3[1])
            + P2[0] * (P3[1] - P1[1])
            + P3[0] * (P1[1] - P2[1])
        )


# ====================================================================
# 主场景
# ====================================================================
class LemoinePoint(Scene):
    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # ---- 色板 ----
        self.C_TRI = "#c8d6e5"          # 三角形边
        self.C_MEDIAN = "#55efc4"       # 中线 — 绿
        self.C_BISECTOR = "#74b9ff"     # 角平分线 — 蓝
        self.C_SYMMEDIAN = "#fd79a8"    # 类似中线 — 粉红
        self.C_LEMOINE = "#fdcb6e"      # 来莫恩点 — 金
        self.C_AUX = "#636e72"          # 辅助线灰
        self.C_LABEL = "#dfe6e9"        # 白标签
        self.C_HIGHLIGHT = YELLOW
        self.C_CENTROID = "#55efc4"     # 重心绿

        # 初始化所有几何
        self.setup_geometry()

        # 场景序列
        self.scene_opening()
        self.scene_median_centroid()
        self.scene_bisector_intro()
        self.scene_symmedian_construction()
        self.scene_lemoine_concurrence()
        self.scene_properties_ratio()
        self.scene_properties_minsum()
        self.scene_outro()

    # ================================================================
    # 几何初始化（统一，仅调用一次）
    # ================================================================
    def setup_geometry(self):
        # --- 基准顶点 ---
        self.A = np.array([-2.8, -0.4, 0.0])
        self.B = np.array([2.4, -0.7, 0.0])
        self.C = np.array([0.2, 3.6, 0.0])

        # --- 边长 ---
        self.a = np.linalg.norm(self.C - self.B)   # BC
        self.b = np.linalg.norm(self.A - self.C)   # CA
        self.c = np.linalg.norm(self.B - self.A)   # AB
        self.a2 = self.a ** 2
        self.b2 = self.b ** 2
        self.c2 = self.c ** 2

        # --- 中点 ---
        self.M_BC = GC.midpoint(self.B, self.C)
        self.M_CA = GC.midpoint(self.C, self.A)
        self.M_AB = GC.midpoint(self.A, self.B)

        # --- 重心 ---
        self.G = (self.A + self.B + self.C) / 3

        # --- 角平分线方向 (从顶点出发) ---
        self.bis_A_dir = GC.unit(self.B - self.A) + GC.unit(self.C - self.A)
        self.bis_B_dir = GC.unit(self.A - self.B) + GC.unit(self.C - self.B)
        self.bis_C_dir = GC.unit(self.A - self.C) + GC.unit(self.B - self.C)

        # --- 角平分线交对边交点 (用于画线段) ---
        # D on BC: BD/DC = c/b
        self.D_bisA = self.B + (self.c / (self.b + self.c)) * (self.C - self.B)

        # --- 中线方向 ---
        self.med_A_dir = self.M_BC - self.A
        self.med_B_dir = self.M_CA - self.B
        self.med_C_dir = self.M_AB - self.C

        # --- 类似中线的反射方向 ---
        self.sym_A_dir = GC.reflect_vector(GC.unit(self.med_A_dir), self.bis_A_dir)
        self.sym_B_dir = GC.reflect_vector(GC.unit(self.med_B_dir), self.bis_B_dir)
        self.sym_C_dir = GC.reflect_vector(GC.unit(self.med_C_dir), self.bis_C_dir)

        # --- 类似中线交对边的点 K_a, K_b, K_c ---
        # BK_a : CK_a = c^2 : b^2
        self.K_a = self.B + (self.c2 / (self.b2 + self.c2)) * (self.C - self.B)
        # CK_b : AK_b = a^2 : c^2
        self.K_b = self.C + (self.a2 / (self.a2 + self.c2)) * (self.A - self.C)
        # AK_c : BK_c = b^2 : a^2
        self.K_c = self.A + (self.b2 / (self.a2 + self.b2)) * (self.B - self.A)

        # --- 来莫恩点 K (重心坐标 a^2 : b^2 : c^2) ---
        self.K = (self.a2 * self.A + self.b2 * self.B + self.c2 * self.C) / (self.a2 + self.b2 + self.c2)

        # --- 面积 ---
        self.area_ABC = GC.tri_area(self.A, self.B, self.C)

        # --- 到三边距离 ---
        self.K_da = GC.dist_to_line(self.K, self.B, self.C)
        self.K_db = GC.dist_to_line(self.K, self.C, self.A)
        self.K_dc = GC.dist_to_line(self.K, self.A, self.B)

        print("✓ Geometry setup complete")
        print(f"  K = ({self.K[0]:.4f}, {self.K[1]:.4f})")
        print(f"  G = ({self.G[0]:.4f}, {self.G[1]:.4f})")

    # ================================================================
    # 辅助：创建三角形 Polygon
    # ================================================================
    def make_triangle(self, color=None, sw=2.5):
        return Polygon(self.A, self.B, self.C,
                       color=color or self.C_TRI, stroke_width=sw, fill_opacity=0)

    # ================================================================
    # 辅助：作者信息
    # ================================================================
    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC", font_size=18, color=self.C_AUX
        ).move_to(np.array([0, 7.2, 0]))

    # ================================================================
    # 辅助：底部说明文字
    # ================================================================
    def make_bottom_text(self, txt, color=None, y=-5.2, size=22):
        return Text(txt, font="Noto Sans CJK SC", font_size=size,
                    color=color or self.C_LABEL).move_to(np.array([0, y, 0]))

    # ================================================================
    # 辅助：顶点标签组
    # ================================================================
    def make_vertex_labels(self):
        offsets = {
            'A': np.array([-0.35, -0.25, 0]),
            'B': np.array([0.3, -0.25, 0]),
            'C': np.array([0.0, 0.3, 0]),
        }
        labels = VGroup()
        for name, pt in [('A', self.A), ('B', self.B), ('C', self.C)]:
            lbl = Text(name, font="Noto Sans CJK SC", font_size=24,
                       color=self.C_LABEL, weight=BOLD)
            lbl.move_to(pt + offsets[name])
            labels.add(lbl)
        return labels

    # ================================================================
    # Scene 1: 开场
    # ================================================================
    def scene_opening(self):
        author = self.make_author()
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author_mob = author

        # 钩子标题
        title = Text("来莫恩点", font="Noto Sans CJK SC",
                     font_size=52, color=self.C_LEMOINE, weight=BOLD
                     ).move_to(np.array([0, 5.8, 0]))
        sub = Text("三角形中最优美的秘密点", font="Noto Sans CJK SC",
                   font_size=26, color=self.C_AUX
                   ).move_to(np.array([0, 5.0, 0]))

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.4)

        # 画三角形
        tri = self.make_triangle(sw=3)
        self.play(Create(tri), run_time=0.8)

        # 快速闪烁来莫恩点
        k_dot = Dot(self.K, radius=0.12, color=self.C_LEMOINE, z_index=5)
        self.play(FadeIn(k_dot, scale=0.3), run_time=0.3)
        self.play(Flash(k_dot, color=self.C_LEMOINE, flash_radius=0.4), run_time=0.3)

        # 钩子提问
        hook = Text("你知道这个点有什么神奇性质吗？",
                    font="Noto Sans CJK SC", font_size=24,
                    color=self.C_HIGHLIGHT
                    ).move_to(np.array([0, -5.5, 0]))
        self.play(FadeIn(hook, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 清除（保留作者）
        self.play(FadeOut(title), FadeOut(sub), FadeOut(hook),
                  FadeOut(k_dot), FadeOut(tri), run_time=0.5)

    # ================================================================
    # Scene 2: 回顾中线与重心
    # ================================================================
    def scene_median_centroid(self):
        # 标题
        title = Text("第一步：回顾中线与重心",
                     font="Noto Sans CJK SC", font_size=30,
                     color=self.C_MEDIAN).move_to(np.array([0, 5.8, 0]))
        self.play(Write(title), run_time=0.5)

        # 三角形
        tri = self.make_triangle()
        vlabels = self.make_vertex_labels()
        self.play(Create(tri), run_time=0.6)
        self.play(FadeIn(vlabels), run_time=0.3)

        # 中点标记
        m_dots = VGroup(
            Dot(self.M_BC, radius=0.07, color=self.C_MEDIAN),
            Dot(self.M_CA, radius=0.07, color=self.C_MEDIAN),
            Dot(self.M_AB, radius=0.07, color=self.C_MEDIAN),
        )
        m_labels = VGroup(
            Text("$M_a$", font="Noto Sans CJK SC", font_size=18, color=self.C_MEDIAN
                 ).move_to(self.M_BC + np.array([0.25, 0.15, 0])),
            Text("$M_b$", font="Noto Sans CJK SC", font_size=18, color=self.C_MEDIAN
                 ).move_to(self.M_CA + np.array([-0.32, 0.12, 0])),
            Text("$M_c$", font="Noto Sans CJK SC", font_size=18, color=self.C_MEDIAN
                 ).move_to(self.M_AB + np.array([0.0, -0.28, 0])),
        )

        # 逐条画中线
        medians = [
            Line(self.A, self.M_BC, color=self.C_MEDIAN, stroke_width=2),
            Line(self.B, self.M_CA, color=self.C_MEDIAN, stroke_width=2),
            Line(self.C, self.M_AB, color=self.C_MEDIAN, stroke_width=2),
        ]

        self.play(FadeIn(m_dots), run_time=0.3)
        self.play(FadeIn(m_labels), run_time=0.3)

        for med in medians:
            self.play(Create(med), run_time=0.5)

        # 重心
        g_dot = Dot(self.G, radius=0.12, color=self.C_CENTROID, z_index=5)
        g_label = Text("G（重心）", font="Noto Sans CJK SC", font_size=20,
                       color=self.C_CENTROID
                       ).move_to(self.G + np.array([0.55, -0.28, 0]))
        self.play(FadeIn(g_dot, scale=0.3), run_time=0.3)
        self.play(Flash(g_dot, color=self.C_CENTROID, flash_radius=0.3), run_time=0.3)
        self.play(FadeIn(g_label), run_time=0.3)

        # 说明
        explain = self.make_bottom_text("中线：连接顶点与对边中点\n重心：三条中线的交点", y=-5.0, size=22)
        self.play(FadeIn(explain), run_time=0.4)
        self.wait(1.5)

        # 清除
        to_remove = [title, tri, vlabels, m_dots, m_labels, g_dot, g_label, explain] + medians
        self.play(*[FadeOut(m) for m in to_remove], run_time=0.5)

    # ================================================================
    # Scene 3: 角平分线铺垫
    # ================================================================
    def scene_bisector_intro(self):
        title = Text("第二步：角平分线的回顾",
                     font="Noto Sans CJK SC", font_size=30,
                     color=self.C_BISECTOR).move_to(np.array([0, 5.8, 0]))
        self.play(Write(title), run_time=0.5)

        tri = self.make_triangle()
        vlabels = self.make_vertex_labels()
        self.play(Create(tri), run_time=0.5)
        self.play(FadeIn(vlabels), run_time=0.3)

        # 角A的平分线 A -> D
        bis_line = Line(self.A, self.D_bisA, color=self.C_BISECTOR,
                        stroke_width=2, )
        self.play(Create(bis_line), run_time=0.6)

        # 角弧示意（简单画两段弧来暗示等分）
        # 用小弧线从AB方向到平分线、平分线到AC方向
        r_arc = 0.7
        # 角A处：向量 AB 和 AC 的角度
        ang_AB = np.arctan2((self.B - self.A)[1], (self.B - self.A)[0])
        ang_AC = np.arctan2((self.C - self.A)[1], (self.C - self.A)[0])
        ang_bis = np.arctan2(self.bis_A_dir[1], self.bis_A_dir[0])

        # 两段弧
        arc1 = Arc(radius=r_arc, start_angle=ang_AB, angle=ang_bis - ang_AB,
                   color=self.C_BISECTOR, stroke_width=1.5).move_to(self.A)
        arc2 = Arc(radius=r_arc, start_angle=ang_bis, angle=ang_AC - ang_bis,
                   color=self.C_BISECTOR, stroke_width=1.5).move_to(self.A)

        # 等号标记
        alpha_label = Text("α", font="Noto Sans CJK SC", font_size=18, color=self.C_BISECTOR)
        mid_ang1 = (ang_AB + ang_bis) / 2
        alpha_label.move_to(self.A + 0.95 * np.array([np.cos(mid_ang1), np.sin(mid_ang1), 0]))

        alpha_label2 = Text("α", font="Noto Sans CJK SC", font_size=18, color=self.C_BISECTOR)
        mid_ang2 = (ang_bis + ang_AC) / 2
        alpha_label2.move_to(self.A + 0.95 * np.array([np.cos(mid_ang2), np.sin(mid_ang2), 0]))

        self.play(Create(arc1), Create(arc2), run_time=0.5)
        self.play(FadeIn(alpha_label), FadeIn(alpha_label2), run_time=0.3)

        explain = self.make_bottom_text("角平分线：将顶角平分为两个相等的角", y=-5.0)
        self.play(FadeIn(explain), run_time=0.4)
        self.wait(1.5)

        # 清除
        to_rem = [title, tri, vlabels, bis_line, arc1, arc2, alpha_label, alpha_label2, explain]
        self.play(*[FadeOut(m) for m in to_rem], run_time=0.5)

    # ================================================================
    # Scene 4: 类似中线的构造
    # ================================================================
    def scene_symmedian_construction(self):
        title = Text("第三步：类似中线的构造",
                     font="Noto Sans CJK SC", font_size=30,
                     color=self.C_SYMMEDIAN).move_to(np.array([0, 5.8, 0]))
        sub = Text("中线关于角平分线的对称线",
                   font="Noto Sans CJK SC", font_size=22,
                   color=self.C_AUX).move_to(np.array([0, 5.1, 0]))

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.3)

        tri = self.make_triangle()
        vlabels = self.make_vertex_labels()
        self.play(Create(tri), run_time=0.5)
        self.play(FadeIn(vlabels), run_time=0.3)

        # --- Step 1: 画从A出发的中线 ---
        med_A = Line(self.A, self.M_BC, color=self.C_MEDIAN, stroke_width=2.5)
        m_dot = Dot(self.M_BC, radius=0.07, color=self.C_MEDIAN)
        m_lbl = Text("$M_a$", font="Noto Sans CJK SC", font_size=18, color=self.C_MEDIAN
                     ).move_to(self.M_BC + np.array([0.22, 0.15, 0]))

        self.play(Create(med_A), FadeIn(m_dot), run_time=0.5)
        self.play(FadeIn(m_lbl), run_time=0.3)

        step1_txt = self.make_bottom_text("① 画中线 $AM_a$", y=-4.8, size=22,
                                          color=self.C_MEDIAN)
        self.play(FadeIn(step1_txt), run_time=0.3)
        self.wait(0.6)

        # --- Step 2: 画角平分线 ---
        bis_A = Line(self.A, self.D_bisA, color=self.C_BISECTOR,
                     stroke_width=2, )
        self.play(FadeOut(step1_txt), run_time=0.2)

        step2_txt = self.make_bottom_text("② 画角 A 的平分线", y=-4.8, size=22,
                                          color=self.C_BISECTOR)
        self.play(Create(bis_A), FadeIn(step2_txt), run_time=0.6)
        self.wait(0.6)

        # --- Step 3: 画类似中线（反射）---
        # 类似中线从 A 到 K_a
        sym_A = Line(self.A, self.K_a, color=self.C_SYMMEDIAN, stroke_width=3)
        ka_dot = Dot(self.K_a, radius=0.08, color=self.C_SYMMEDIAN)
        ka_lbl = Text("$K_a$", font="Noto Sans CJK SC", font_size=18,
                       color=self.C_SYMMEDIAN
                       ).move_to(self.K_a + np.array([0.22, 0.12, 0]))

        self.play(FadeOut(step2_txt), run_time=0.2)
        step3_txt = self.make_bottom_text("③ 将中线关于角平分线反射\n   → 得到类似中线（粉红色）",
                                          y=-5.0, size=21, color=self.C_SYMMEDIAN)
        self.play(Create(sym_A), FadeIn(ka_dot), FadeIn(ka_lbl),
                  FadeIn(step3_txt), run_time=0.8)
        self.wait(1.0)

        # --- Step 4: 标注比例 BK_a : CK_a = c² : b² ---
        self.play(FadeOut(step3_txt), run_time=0.2)

        ratio_txt = Text(
            "$BK_a : CK_a = AB^2 : AC^2 = c^2 : b^2$",
            font="Noto Sans CJK SC", font_size=20, color=self.C_LEMOINE
        ).move_to(np.array([0, -4.8, 0]))
        self.play(FadeIn(ratio_txt), run_time=0.5)
        self.wait(1.2)

        # 清除
        to_rem = [title, sub, tri, vlabels, med_A, m_dot, m_lbl,
                  bis_A, sym_A, ka_dot, ka_lbl, ratio_txt]
        self.play(*[FadeOut(m) for m in to_rem], run_time=0.5)

    # ================================================================
    # Scene 5: 来莫恩点 — 三线共点
    # ================================================================
    def scene_lemoine_concurrence(self):
        title = Text("第四步：来莫恩点 — 三线共点",
                     font="Noto Sans CJK SC", font_size=30,
                     color=self.C_LEMOINE).move_to(np.array([0, 5.8, 0]))
        self.play(Write(title), run_time=0.5)

        tri = self.make_triangle()
        vlabels = self.make_vertex_labels()
        self.play(Create(tri), run_time=0.5)
        self.play(FadeIn(vlabels), run_time=0.3)

        # 逐条画三条类似中线
        sym_lines = [
            Line(self.A, self.K_a, color=self.C_SYMMEDIAN, stroke_width=2.5),
            Line(self.B, self.K_b, color=self.C_SYMMEDIAN, stroke_width=2.5),
            Line(self.C, self.K_c, color=self.C_SYMMEDIAN, stroke_width=2.5),
        ]
        ka_dots = [
            Dot(self.K_a, radius=0.07, color=self.C_SYMMEDIAN),
            Dot(self.K_b, radius=0.07, color=self.C_SYMMEDIAN),
            Dot(self.K_c, radius=0.07, color=self.C_SYMMEDIAN),
        ]
        ka_labels = [
            Text("$K_a$", font="Noto Sans CJK SC", font_size=17, color=self.C_SYMMEDIAN
                 ).move_to(self.K_a + np.array([0.25, 0.1, 0])),
            Text("$K_b$", font="Noto Sans CJK SC", font_size=17, color=self.C_SYMMEDIAN
                 ).move_to(self.K_b + np.array([-0.3, 0.1, 0])),
            Text("$K_c$", font="Noto Sans CJK SC", font_size=17, color=self.C_SYMMEDIAN
                 ).move_to(self.K_c + np.array([0.0, -0.28, 0])),
        ]

        for i in range(3):
            self.play(Create(sym_lines[i]), FadeIn(ka_dots[i]), FadeIn(ka_labels[i]),
                      run_time=0.6)
            self.wait(0.2)

        # 来莫恩点
        k_dot = Dot(self.K, radius=0.14, color=self.C_LEMOINE, z_index=5)
        k_label = Text("K（来莫恩点）", font="Noto Sans CJK SC", font_size=20,
                       color=self.C_LEMOINE, weight=BOLD
                       ).move_to(self.K + np.array([0.7, -0.35, 0]))

        self.play(FadeIn(k_dot, scale=0.3), run_time=0.4)
        self.play(Flash(k_dot, color=self.C_LEMOINE, flash_radius=0.5), run_time=0.4)
        self.play(FadeIn(k_label), run_time=0.3)

        explain = self.make_bottom_text("三条类似中线交于一点\n来莫恩点 = 重心的等角共轭点", y=-5.0, size=21)
        self.play(FadeIn(explain), run_time=0.4)
        self.wait(2.0)

        # 清除
        all_mobs = [title, tri, vlabels, k_dot, k_label, explain] + sym_lines + ka_dots + ka_labels
        self.play(*[FadeOut(m) for m in all_mobs], run_time=0.5)

    # ================================================================
    # Scene 6: 性质 — 比例与面积
    # ================================================================
    def scene_properties_ratio(self):
        title = Text("性质一：比例与面积",
                     font="Noto Sans CJK SC", font_size=30,
                     color=self.C_LEMOINE).move_to(np.array([0, 5.8, 0]))
        self.play(Write(title), run_time=0.5)

        tri = self.make_triangle()
        vlabels = self.make_vertex_labels()
        self.play(Create(tri), run_time=0.5)
        self.play(FadeIn(vlabels), run_time=0.3)

        # 来莫恩点
        k_dot = Dot(self.K, radius=0.11, color=self.C_LEMOINE, z_index=5)
        self.play(FadeIn(k_dot), run_time=0.3)

        # 连接 K 与三顶点（分割三角形）
        klines = VGroup(
            Line(self.K, self.A, color=self.C_AUX, stroke_width=1.5, ),
            Line(self.K, self.B, color=self.C_AUX, stroke_width=1.5, ),
            Line(self.K, self.C, color=self.C_AUX, stroke_width=1.5, ),
        )
        self.play(Create(klines), run_time=0.6)

        # 三个子三角形轻微染色
        tri_KBC = Polygon(self.K, self.B, self.C, fill_opacity=0.15,
                          fill_color="#e17055", stroke_width=0, color="#e17055")
        tri_KCA = Polygon(self.K, self.C, self.A, fill_opacity=0.15,
                          fill_color="#0984e3", stroke_width=0, color="#0984e3")
        tri_KAB = Polygon(self.K, self.A, self.B, fill_opacity=0.15,
                          fill_color="#6c5ce7", stroke_width=0, color="#6c5ce7")

        self.play(FadeIn(tri_KBC), FadeIn(tri_KCA), FadeIn(tri_KAB), run_time=0.5)

        # 面积标签
        center_KBC = (self.K + self.B + self.C) / 3
        center_KCA = (self.K + self.C + self.A) / 3
        center_KAB = (self.K + self.A + self.B) / 3

        s_kbc = Text("$S_1$", font="Noto Sans CJK SC", font_size=20, color="#e17055"
                     ).move_to(center_KBC)
        s_kca = Text("$S_2$", font="Noto Sans CJK SC", font_size=20, color="#0984e3"
                     ).move_to(center_KCA)
        s_kab = Text("$S_3$", font="Noto Sans CJK SC", font_size=20, color="#6c5ce7"
                     ).move_to(center_KAB)

        self.play(FadeIn(s_kbc), FadeIn(s_kca), FadeIn(s_kab), run_time=0.4)
        self.wait(0.5)

        # 公式
        formula = MathTex(
            r"\frac{S_1}{a^2} = \frac{S_2}{b^2} = \frac{S_3}{c^2}",
            font_size=28, color=self.C_LEMOINE
        ).move_to(np.array([0, -4.6, 0]))
        self.play(Write(formula), run_time=0.7)

        explain = self.make_bottom_text("来莫恩点将三角形分成的三个小三角形\n面积与对边长度的平方成正比", y=-5.8, size=19)
        self.play(FadeIn(explain), run_time=0.4)
        self.wait(2.0)

        # 清除
        all_mobs = [title, tri, vlabels, k_dot, klines,
                    tri_KBC, tri_KCA, tri_KAB, s_kbc, s_kca, s_kab, formula, explain]
        self.play(*[FadeOut(m) for m in all_mobs], run_time=0.5)

    # ================================================================
    # Scene 7: 性质 — 距离平方和最小
    # ================================================================
    def scene_properties_minsum(self):
        title = Text("性质二：距离平方和最小",
                     font="Noto Sans CJK SC", font_size=30,
                     color=self.C_LEMOINE).move_to(np.array([0, 5.8, 0]))
        sub = Text("来莫恩点是到三边距离平方和最小的点",
                   font="Noto Sans CJK SC", font_size=21,
                   color=self.C_AUX).move_to(np.array([0, 5.1, 0]))
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.3)

        tri = self.make_triangle()
        vlabels = self.make_vertex_labels()
        self.play(Create(tri), run_time=0.5)
        self.play(FadeIn(vlabels), run_time=0.3)

        # 来莫恩点
        k_dot = Dot(self.K, radius=0.11, color=self.C_LEMOINE, z_index=5)
        k_lbl = Text("K", font="Noto Sans CJK SC", font_size=20,
                     color=self.C_LEMOINE, weight=BOLD
                     ).move_to(self.K + np.array([0.2, 0.18, 0]))
        self.play(FadeIn(k_dot), FadeIn(k_lbl), run_time=0.3)

        # 从K到三边作垂线
        foot_BC = GC.foot(self.K, self.B, self.C)
        foot_CA = GC.foot(self.K, self.C, self.A)
        foot_AB = GC.foot(self.K, self.A, self.B)

        perp_lines = VGroup(
            Line(self.K, foot_BC, color="#e17055", stroke_width=2, ),
            Line(self.K, foot_CA, color="#0984e3", stroke_width=2, ),
            Line(self.K, foot_AB, color="#6c5ce7", stroke_width=2, ),
        )
        foot_dots = VGroup(
            Dot(foot_BC, radius=0.06, color="#e17055"),
            Dot(foot_CA, radius=0.06, color="#0984e3"),
            Dot(foot_AB, radius=0.06, color="#6c5ce7"),
        )

        self.play(Create(perp_lines), FadeIn(foot_dots), run_time=0.7)

        # 距离标签
        mid_pBC = (self.K + foot_BC) / 2
        mid_pCA = (self.K + foot_CA) / 2
        mid_pAB = (self.K + foot_AB) / 2

        d_labels = VGroup(
            Text("$d_a$", font="Noto Sans CJK SC", font_size=18, color="#e17055"
                 ).move_to(mid_pBC + np.array([0.2, -0.05, 0])),
            Text("$d_b$", font="Noto Sans CJK SC", font_size=18, color="#0984e3"
                 ).move_to(mid_pCA + np.array([-0.25, 0.0, 0])),
            Text("$d_c$", font="Noto Sans CJK SC", font_size=18, color="#6c5ce7"
                 ).move_to(mid_pAB + np.array([0.0, -0.22, 0])),
        )
        self.play(FadeIn(d_labels), run_time=0.4)
        self.wait(0.5)

        # 公式（中文与数学分开）
        formula_math = MathTex(
            r"d_a^2 + d_b^2 + d_c^2",
            font_size=24, color=self.C_LEMOINE
        )
        formula_txt = Text("取最小值", font="Noto Sans CJK SC", font_size=22,
                           color=self.C_LEMOINE)
        formula = VGroup(formula_math, formula_txt).arrange(RIGHT, buff=0.2)
        formula.move_to(np.array([0, -4.5, 0]))
        self.play(Write(formula), run_time=0.6)

        # 三线坐标比例
        trilinear = MathTex(
            r"d_a : d_b : d_c = a : b : c",
            font_size=22, color="#dfe6e9"
        ).move_to(np.array([0, -5.3, 0]))
        self.play(FadeIn(trilinear), run_time=0.4)
        self.wait(2.0)

        # 清除
        all_mobs = [title, sub, tri, vlabels, k_dot, k_lbl,
                    perp_lines, foot_dots, d_labels, formula, trilinear]
        self.play(*[FadeOut(m) for m in all_mobs], run_time=0.5)

    # ================================================================
    # Scene 8: 片尾
    # ================================================================
    def scene_outro(self):
        # 渐大作者名
        name = Text("上海初高中数学直通车",
                    font="Noto Sans CJK SC", font_size=38,
                    color=WHITE, weight=BOLD).move_to(np.array([0, 2.0, 0]))
        handle = Text("@emptyandcalm",
                      font="Noto Sans CJK SC", font_size=26,
                      color=self.C_AUX).move_to(np.array([0, 1.2, 0]))

        self.play(FadeOut(self.author_mob), run_time=0.3)
        self.play(FadeIn(name), run_time=0.5)
        self.play(FadeIn(handle), run_time=0.4)

        follow = Text("关注我，学更多数学技巧！",
                      font="Noto Sans CJK SC", font_size=28,
                      color=self.C_HIGHLIGHT).move_to(np.array([0, 0.0, 0]))
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 小装饰：金色星星点
        stars = VGroup(*[
            Dot(radius=0.08, color=GOLD, fill_opacity=0.9).move_to(
                np.array([1.8 * np.cos(i * PI / 3 + 0.3),
                          -1.8 + 1.8 * np.sin(i * PI / 3 + 0.3), 0])
            )
            for i in range(6)
        ])
        self.play(*[FadeIn(s, scale=0.3) for s in stars], run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(name), FadeOut(handle), FadeOut(follow),
                  FadeOut(stars), run_time=0.8)


# ====================================================================
# 运行指令
# ====================================================================
# 预览: manim -pql lemoine_point.py LemoinePoint
# 高画质: manim -qh lemoine_point.py LemoinePoint