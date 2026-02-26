"""
平面的基本性质 - Space Plane Axioms Teaching Animation
高三数学第十四章：空间直线与平面
目标受众: 高三学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== 全局配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ===== 颜色配置 =====
BG_COLOR      = "#1a1a2e"
COLOR_ALPHA   = "#4FC3F7"    # 浅蓝 - 平面α
COLOR_BETA    = "#81C784"    # 浅绿 - 平面β
COLOR_LINE    = "#FFD54F"    # 金黄 - 直线
COLOR_POINT   = "#FF8A65"    # 橙红 - 点
COLOR_FORMULA = WHITE
COLOR_AXIOM   = "#CE93D8"    # 紫色 - 公理
COLOR_COND    = "#F06292"    # 粉红 - 条件
COLOR_GOLD    = "#FFD700"

FONT_CN       = "Noto Sans CJK SC"


def make_plane_polygon(center, width=5.5, height=1.8, skew=0.8, **kwargs):
    """创建表示平面的平行四边形（透视效果）"""
    cx, cy = center[0], center[1]
    # 四个顶点
    bl = np.array([cx - width/2,           cy - height/2, 0])
    br = np.array([cx + width/2,           cy - height/2, 0])
    tr = np.array([cx + width/2 + skew,    cy + height/2, 0])
    tl = np.array([cx - width/2 + skew,    cy + height/2, 0])
    return Polygon(bl, br, tr, tl, **kwargs)


class PlaneAxiomsScene(Scene):
    """平面的基本性质教学动画"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        # ===== 初始化几何数据 =====
        self.setup_geometry()

        # ===== 执行各场景 =====
        self.scene_1_opening()
        self.scene_2_plane_concept()
        self.scene_3_axiom1()
        self.scene_4_axiom2()
        self.scene_5_axiom3()
        self.scene_6_conditions()
        self.scene_7_outro()

    # ================================================================
    # 几何数据初始化与验证
    # ================================================================
    def setup_geometry(self):
        """统一初始化所有几何数据"""

        # ----- 主平面中心（主内容区中部偏上）-----
        self.plane_center = np.array([0, 1.0, 0])

        # ----- 公理1: 直线与平面 -----
        # 直线上两点在平面内
        self.axiom1_line_start = np.array([-2.5, 1.0, 0])
        self.axiom1_line_end   = np.array([ 2.5, 1.0, 0])
        self.axiom1_A = np.array([-1.2, 1.0, 0])
        self.axiom1_B = np.array([ 1.2, 1.0, 0])

        # ----- 公理2: 三点确定平面 -----
        # 不共线三点
        self.axiom2_A = np.array([-1.5, 0.0, 0])
        self.axiom2_B = np.array([ 1.8, 0.3, 0])
        self.axiom2_C = np.array([ 0.2, 2.0, 0])

        # 验证不共线
        area = 0.5 * abs(
            self.axiom2_A[0]*(self.axiom2_B[1]-self.axiom2_C[1]) +
            self.axiom2_B[0]*(self.axiom2_C[1]-self.axiom2_A[1]) +
            self.axiom2_C[0]*(self.axiom2_A[1]-self.axiom2_B[1])
        )
        assert area > 0.1, "三点共线！"

        # ----- 公理3: 两平面交线 -----
        # 平面α中心偏左上，平面β中心偏右下
        self.plane_alpha_center = np.array([-0.5, 1.8, 0])
        self.plane_beta_center  = np.array([ 0.5, 0.2, 0])

        # 交线（两平面公共直线）
        self.intersect_line_start = np.array([-2.2, 1.0, 0])
        self.intersect_line_end   = np.array([ 2.2, 1.0, 0])
        # 公共点P在交线中点
        self.intersect_P = (self.intersect_line_start + self.intersect_line_end) / 2

        print("✓ 几何数据初始化完成")

    # ================================================================
    # Scene 1: 开场钩子
    # ================================================================
    def scene_1_opening(self):
        # 作者信息（顶部，全程保留）
        self.author_info = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author_info, shift=DOWN*0.2), run_time=0.4)

        # 钩子标题
        hook = Text("三脚架为什么稳？", font=FONT_CN, font_size=44, color=COLOR_GOLD).move_to(UP * 5.5)
        self.play(Write(hook), run_time=0.8)

        # 显示三个点
        pts = [
            np.array([-1.5, 3.5, 0]),
            np.array([ 1.5, 3.5, 0]),
            np.array([ 0.0, 2.2, 0]),
        ]
        dots = VGroup(*[Dot(p, radius=0.12, color=COLOR_POINT) for p in pts])
        labels = VGroup(
            Text("A", font=FONT_CN, font_size=24, color=WHITE).next_to(dots[0], LEFT, buff=0.1),
            Text("B", font=FONT_CN, font_size=24, color=WHITE).next_to(dots[1], RIGHT, buff=0.1),
            Text("C", font=FONT_CN, font_size=24, color=WHITE).next_to(dots[2], DOWN, buff=0.1),
        )

        for d, l in zip(dots, labels):
            self.play(FadeIn(d, scale=0.5), Write(l), run_time=0.25)

        # 连三角形
        tri = Polygon(*pts[:3],
                      color=COLOR_ALPHA, fill_color=COLOR_ALPHA,
                      fill_opacity=0.18, stroke_width=2)
        self.play(Create(tri), run_time=0.7)

        answer = Text("三点确定唯一平面！", font=FONT_CN, font_size=32,
                      color=COLOR_COND).move_to(UP * 1.2)
        self.play(FadeIn(answer, shift=UP*0.3), run_time=0.5)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(hook), FadeOut(dots), FadeOut(labels),
            FadeOut(tri), FadeOut(answer),
            run_time=0.5
        )

    # ================================================================
    # Scene 2: 平面的概念
    # ================================================================
    def scene_2_plane_concept(self):
        title = Text("平面的概念", font=FONT_CN, font_size=40, color=COLOR_ALPHA).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 画平面α
        plane = make_plane_polygon(
            self.plane_center, width=5.5, height=1.8, skew=0.7,
            color=COLOR_ALPHA, fill_color=COLOR_ALPHA,
            fill_opacity=0.15, stroke_width=2.5
        )
        self.play(Create(plane), run_time=1.0)

        # α标签（右上角）
        alpha_label = MathTex(r"\alpha", color=COLOR_ALPHA, font_size=48).move_to(np.array([3.5, 2.2, 0]))
        self.play(Write(alpha_label), run_time=0.4)

        # 无限延展箭头（4个方向）
        arr_kwargs = dict(color=COLOR_ALPHA, stroke_width=2, tip_length=0.2,
                         max_tip_length_to_length_ratio=0.15)
        arrows = VGroup(
            Arrow(self.plane_center, self.plane_center + np.array([-2.8, -1.0, 0]), **arr_kwargs),
            Arrow(self.plane_center, self.plane_center + np.array([ 2.8,  1.0, 0]), **arr_kwargs),
            Arrow(self.plane_center, self.plane_center + np.array([-1.5,  0.9, 0]), **arr_kwargs),
            Arrow(self.plane_center, self.plane_center + np.array([ 1.5, -0.9, 0]), **arr_kwargs),
        )
        self.play(*[GrowArrow(a) for a in arrows], run_time=0.8)

        desc1 = Text("无限延展的平坦面", font=FONT_CN, font_size=28,
                     color=WHITE).move_to(DOWN * 2.5)
        self.play(FadeIn(desc1, shift=UP*0.2), run_time=0.5)
        self.wait(0.5)

        desc2 = Text("用希腊字母 α、β、γ 表示", font=FONT_CN, font_size=24,
                     color=GRAY_A).move_to(DOWN * 3.3)
        self.play(FadeIn(desc2), run_time=0.5)
        self.wait(0.8)

        # 清场，保留作者信息
        self.play(
            FadeOut(title), FadeOut(plane), FadeOut(alpha_label),
            FadeOut(arrows), FadeOut(desc1), FadeOut(desc2),
            run_time=0.5
        )

    # ================================================================
    # Scene 3: 公理1
    # ================================================================
    def scene_3_axiom1(self):
        # 标题
        title_num = Text("公理 1", font=FONT_CN, font_size=34, color=COLOR_AXIOM).move_to(UP * 6.2)
        title_desc = Text("直线与平面", font=FONT_CN, font_size=28, color=GRAY_A).move_to(UP * 5.6)
        self.play(Write(title_num), FadeIn(title_desc), run_time=0.7)

        # 平面α
        plane = make_plane_polygon(
            self.plane_center, width=5.5, height=1.8, skew=0.7,
            color=COLOR_ALPHA, fill_color=COLOR_ALPHA,
            fill_opacity=0.12, stroke_width=2
        )
        alpha_label = MathTex(r"\alpha", color=COLOR_ALPHA, font_size=42).move_to(np.array([3.3, 2.1, 0]))
        self.play(Create(plane), Write(alpha_label), run_time=0.8)

        # 直线l（先在平面外上方）
        line_off = np.array([0, 0.8, 0])  # 偏移量，使直线先在平面上方
        l_start_off = self.axiom1_line_start + line_off
        l_end_off   = self.axiom1_line_end   + line_off
        line_l = Line(l_start_off, l_end_off, color=COLOR_LINE, stroke_width=3)
        l_label = MathTex("l", color=COLOR_LINE, font_size=36).next_to(line_l, RIGHT, buff=0.15)

        self.play(Create(line_l), Write(l_label), run_time=0.7)

        # 直线上标记两点A, B
        dot_A = Dot(self.axiom1_A + line_off, radius=0.10, color=COLOR_POINT)
        dot_B = Dot(self.axiom1_B + line_off, radius=0.10, color=COLOR_POINT)
        lbl_A = Text("A", font=FONT_CN, font_size=22, color=WHITE).next_to(dot_A, UP, buff=0.08)
        lbl_B = Text("B", font=FONT_CN, font_size=22, color=WHITE).next_to(dot_B, UP, buff=0.08)

        self.play(FadeIn(dot_A), FadeIn(dot_B), Write(lbl_A), Write(lbl_B), run_time=0.5)

        # 条件说明
        cond = Text("设 A, B 在平面 α 内", font=FONT_CN, font_size=26,
                    color=COLOR_COND).move_to(DOWN * 2.8)
        self.play(FadeIn(cond, shift=UP*0.2), run_time=0.5)
        self.wait(0.4)

        # 直线整体移入平面
        self.play(
            line_l.animate.shift(-line_off),
            dot_A.animate.shift(-line_off),
            dot_B.animate.shift(-line_off),
            lbl_A.animate.shift(-line_off),
            lbl_B.animate.shift(-line_off),
            l_label.animate.shift(-line_off),
            run_time=1.0
        )

        # 结论
        conc = Text("则直线 l 上所有点都在 α 内", font=FONT_CN, font_size=24,
                    color=WHITE).move_to(DOWN * 3.6)
        self.play(FadeIn(conc), run_time=0.5)

        # 高亮直线
        self.play(
            line_l.animate.set_color(COLOR_COND).set_stroke(width=4),
            run_time=0.5
        )

        # 公式
        formula = MathTex(
            r"l \subset \alpha",
            color=COLOR_FORMULA, font_size=40
        ).move_to(DOWN * 4.8)
        self.play(Write(formula), run_time=0.6)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title_num), FadeOut(title_desc),
            FadeOut(plane), FadeOut(alpha_label),
            FadeOut(line_l), FadeOut(l_label),
            FadeOut(dot_A), FadeOut(dot_B),
            FadeOut(lbl_A), FadeOut(lbl_B),
            FadeOut(cond), FadeOut(conc), FadeOut(formula),
            run_time=0.5
        )

    # ================================================================
    # Scene 4: 公理2
    # ================================================================
    def scene_4_axiom2(self):
        title_num  = Text("公理 2", font=FONT_CN, font_size=34, color=COLOR_AXIOM).move_to(UP * 6.2)
        title_desc = Text("三点确定平面", font=FONT_CN, font_size=28, color=GRAY_A).move_to(UP * 5.6)
        self.play(Write(title_num), FadeIn(title_desc), run_time=0.7)

        # ---- 显示三个不共线的点 ----
        A = self.axiom2_A
        B = self.axiom2_B
        C = self.axiom2_C

        dot_A = Dot(A, radius=0.12, color=COLOR_POINT)
        dot_B = Dot(B, radius=0.12, color=COLOR_POINT)
        dot_C = Dot(C, radius=0.12, color=COLOR_POINT)
        lbl_A = Text("A", font=FONT_CN, font_size=24, color=WHITE).next_to(dot_A, LEFT, buff=0.12)
        lbl_B = Text("B", font=FONT_CN, font_size=24, color=WHITE).next_to(dot_B, RIGHT, buff=0.12)
        lbl_C = Text("C", font=FONT_CN, font_size=24, color=WHITE).next_to(dot_C, UP, buff=0.12)

        self.play(
            FadeIn(dot_A, scale=0.5), Write(lbl_A),
            FadeIn(dot_B, scale=0.5), Write(lbl_B),
            FadeIn(dot_C, scale=0.5), Write(lbl_C),
            run_time=0.7
        )

        # 不共线标注
        note_nc = Text("（三点不共线）", font=FONT_CN, font_size=22,
                       color=COLOR_COND).move_to(DOWN * 2.8)
        self.play(FadeIn(note_nc), run_time=0.4)
        self.wait(0.3)

        # 平面从三点展开（用缩放动画）
        plane = Polygon(
            np.array([-3.5, -0.3, 0]),
            np.array([ 3.5, -0.3, 0]),
            np.array([ 2.5,  2.5, 0]),
            np.array([-2.5,  2.5, 0]),
            color=COLOR_ALPHA, fill_color=COLOR_ALPHA,
            fill_opacity=0.13, stroke_width=2
        )
        alpha_lbl = MathTex(r"\alpha", color=COLOR_ALPHA, font_size=42).move_to(np.array([3.3, 2.8, 0]))

        self.play(GrowFromCenter(plane), run_time=1.0)
        self.play(Write(alpha_lbl), run_time=0.4)

        # 三点现在在平面上，做Flash
        self.play(
            Flash(dot_A, color=COLOR_COND, flash_radius=0.35),
            Flash(dot_B, color=COLOR_COND, flash_radius=0.35),
            Flash(dot_C, color=COLOR_COND, flash_radius=0.35),
            run_time=0.7
        )

        # 结论
        conc = Text("有且只有一个平面过 A、B、C", font=FONT_CN,
                    font_size=24, color=WHITE).move_to(DOWN * 3.7)
        self.play(FadeIn(conc, shift=UP*0.2), run_time=0.5)

        # 公式
        formula_top = Text("A, B, C 不共线", font=FONT_CN, font_size=22, color=GRAY_A)
        formula_bot = MathTex(r"\Rightarrow", r"\exists", r"! \, \alpha", r"\text{ contains A, B, C}",
                              font_size=34, color=COLOR_FORMULA)
        # 避免LaTeX中的中文
        formula_bot2 = MathTex(r"\Rightarrow \exists ! \; \alpha", font_size=38, color=COLOR_FORMULA)
        formula_text = Text("唯一平面 α 过 A, B, C", font=FONT_CN, font_size=26, color=COLOR_FORMULA)
        formula_group = VGroup(formula_bot2, formula_text).arrange(RIGHT, buff=0.3).move_to(DOWN * 5.0)
        self.play(Write(formula_group), run_time=0.7)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title_num), FadeOut(title_desc),
            FadeOut(dot_A), FadeOut(dot_B), FadeOut(dot_C),
            FadeOut(lbl_A), FadeOut(lbl_B), FadeOut(lbl_C),
            FadeOut(note_nc), FadeOut(plane), FadeOut(alpha_lbl),
            FadeOut(conc), FadeOut(formula_group),
            run_time=0.5
        )

    # ================================================================
    # Scene 5: 公理3
    # ================================================================
    def scene_5_axiom3(self):
        title_num  = Text("公理 3", font=FONT_CN, font_size=34, color=COLOR_AXIOM).move_to(UP * 6.2)
        title_desc = Text("两平面的交线", font=FONT_CN, font_size=28, color=GRAY_A).move_to(UP * 5.6)
        self.play(Write(title_num), FadeIn(title_desc), run_time=0.7)

        # 平面α（蓝色，偏左上）
        plane_alpha = Polygon(
            np.array([-4.0,  0.2, 0]),
            np.array([ 1.5,  0.2, 0]),
            np.array([ 2.5,  2.8, 0]),
            np.array([-3.0,  2.8, 0]),
            color=COLOR_ALPHA, fill_color=COLOR_ALPHA,
            fill_opacity=0.20, stroke_width=2.5
        )
        alpha_lbl = MathTex(r"\alpha", color=COLOR_ALPHA, font_size=42).move_to(np.array([-2.8, 3.0, 0]))

        # 平面β（绿色，偏右下）
        plane_beta = Polygon(
            np.array([-1.5, -0.6, 0]),
            np.array([ 4.0, -0.6, 0]),
            np.array([ 3.0,  2.2, 0]),
            np.array([-2.5,  2.2, 0]),
            color=COLOR_BETA, fill_color=COLOR_BETA,
            fill_opacity=0.18, stroke_width=2.5
        )
        beta_lbl = MathTex(r"\beta", color=COLOR_BETA, font_size=42).move_to(np.array([3.2, 2.4, 0]))

        # 先分别显示两平面
        self.play(Create(plane_alpha), Write(alpha_lbl), run_time=0.8)
        self.play(Create(plane_beta), Write(beta_lbl), run_time=0.8)
        self.wait(0.3)

        # 公共点P
        P = self.intersect_P
        dot_P = Dot(P, radius=0.13, color=COLOR_POINT)
        lbl_P = Text("P", font=FONT_CN, font_size=24, color=COLOR_POINT).next_to(dot_P, UP+RIGHT, buff=0.08)

        note_pt = Text("两平面有公共点 P", font=FONT_CN, font_size=26,
                       color=COLOR_COND).move_to(DOWN * 2.8)
        self.play(FadeIn(dot_P, scale=0.5), Write(lbl_P), run_time=0.4)
        self.play(Flash(dot_P, color=COLOR_COND, flash_radius=0.35), run_time=0.4)
        self.play(FadeIn(note_pt, shift=UP*0.2), run_time=0.4)
        self.wait(0.5)

        # 交线 l 出现
        intersect_line = Line(
            self.intersect_line_start,
            self.intersect_line_end,
            color=COLOR_LINE, stroke_width=4
        )
        l_lbl = MathTex("l", color=COLOR_LINE, font_size=38).next_to(intersect_line, RIGHT, buff=0.15)

        note_line = Text("则有且只有一条公共直线 l", font=FONT_CN,
                         font_size=24, color=WHITE).move_to(DOWN * 3.6)
        self.play(Create(intersect_line), Write(l_lbl), run_time=0.8)
        self.play(FadeIn(note_line), run_time=0.4)

        # 公式
        formula_line1 = MathTex(r"\alpha \cap \beta = \{P\}", font_size=34, color=GRAY_A)
        arrow_sym     = MathTex(r"\Rightarrow", font_size=34, color=WHITE)
        formula_line2 = MathTex(r"\alpha \cap \beta = l \; (P \in l)", font_size=34, color=COLOR_FORMULA)
        formula_group = VGroup(formula_line1, arrow_sym, formula_line2).arrange(RIGHT, buff=0.2)
        formula_group.move_to(DOWN * 5.0)
        self.play(Write(formula_group), run_time=1.0)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title_num), FadeOut(title_desc),
            FadeOut(plane_alpha), FadeOut(alpha_lbl),
            FadeOut(plane_beta), FadeOut(beta_lbl),
            FadeOut(dot_P), FadeOut(lbl_P),
            FadeOut(note_pt), FadeOut(note_line),
            FadeOut(intersect_line), FadeOut(l_lbl),
            FadeOut(formula_group),
            run_time=0.5
        )

    # ================================================================
    # Scene 6: 确定平面的条件
    # ================================================================
    def scene_6_conditions(self):
        title = Text("确定平面的四个条件", font=FONT_CN, font_size=34,
                     color=COLOR_GOLD).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        conditions = [
            ("① ", "不共线三点"),
            ("② ", "一直线和直线外一点"),
            ("③ ", "两条相交直线"),
            ("④ ", "两条平行直线"),
        ]
        colors = [COLOR_ALPHA, COLOR_BETA, COLOR_COND, COLOR_AXIOM]

        y_start = 4.0
        y_step  = 1.5
        items_group = VGroup()

        for i, ((num, desc), col) in enumerate(zip(conditions, colors)):
            num_text  = Text(num, font=FONT_CN, font_size=30, color=col)
            desc_text = Text(desc, font=FONT_CN, font_size=28, color=WHITE)
            row = VGroup(num_text, desc_text).arrange(RIGHT, buff=0.1)
            row.move_to(np.array([0, y_start - i * y_step, 0]))

            # 小图示（简单几何图）
            icon = self._make_condition_icon(i, col)
            icon.next_to(row, RIGHT, buff=0.4)

            items_group.add(VGroup(row, icon))
            self.play(FadeIn(row, shift=RIGHT*0.3), run_time=0.4)
            self.play(FadeIn(icon, scale=0.7), run_time=0.3)

        self.wait(1.0)

        # 记忆口诀
        mnemonic = Text("记口诀：不共线三点、直线加点外、", font=FONT_CN,
                        font_size=20, color=GRAY_A).move_to(DOWN * 4.2)
        mnemonic2 = Text("两交线或两平行线", font=FONT_CN,
                         font_size=20, color=GRAY_A).move_to(DOWN * 4.9)
        self.play(FadeIn(mnemonic), FadeIn(mnemonic2), run_time=0.6)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(title), FadeOut(items_group),
            FadeOut(mnemonic), FadeOut(mnemonic2),
            run_time=0.5
        )

    def _make_condition_icon(self, idx, color):
        """制作小图示"""
        if idx == 0:
            # 三点 + 三角形
            pts = [np.array([-0.3, -0.3, 0]), np.array([0.3, -0.3, 0]), np.array([0, 0.35, 0])]
            dots = VGroup(*[Dot(p, radius=0.06, color=color) for p in pts])
            lines = VGroup(
                Line(pts[0], pts[1], color=color, stroke_width=1.5),
                Line(pts[1], pts[2], color=color, stroke_width=1.5),
                Line(pts[2], pts[0], color=color, stroke_width=1.5),
            )
            return VGroup(lines, dots)
        elif idx == 1:
            # 一条线 + 一个点
            line = Line(np.array([-0.35, -0.1, 0]), np.array([0.35, -0.1, 0]),
                        color=color, stroke_width=2)
            dot  = Dot(np.array([0, 0.3, 0]), radius=0.07, color=color)
            return VGroup(line, dot)
        elif idx == 2:
            # 两交线（X形）
            l1 = Line(np.array([-0.35, -0.3, 0]), np.array([0.35, 0.3, 0]),
                      color=color, stroke_width=2)
            l2 = Line(np.array([-0.35, 0.3, 0]), np.array([0.35, -0.3, 0]),
                      color=color, stroke_width=2)
            return VGroup(l1, l2)
        else:
            # 两平行线
            l1 = Line(np.array([-0.35, 0.18, 0]), np.array([0.35, 0.18, 0]),
                      color=color, stroke_width=2)
            l2 = Line(np.array([-0.35, -0.18, 0]), np.array([0.35, -0.18, 0]),
                      color=color, stroke_width=2)
            return VGroup(l1, l2)

    # ================================================================
    # Scene 7: 片尾
    # ================================================================
    def scene_7_outro(self):
        # 作者信息放大居中
        author_big = Text("上海初高中数学直通车", font=FONT_CN,
                          font_size=38, color=WHITE).move_to(UP * 1.8)
        author_id  = Text("@emptyandcalm", font=FONT_CN,
                          font_size=28, color=GRAY_B).move_to(UP * 0.8)
        follow_txt = Text("关注我，获得更多数学技巧！", font=FONT_CN,
                          font_size=30, color=COLOR_GOLD).move_to(DOWN * 0.3)

        self.play(
            Transform(self.author_info, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP*0.2), run_time=0.4)
        self.play(FadeIn(follow_txt, scale=1.05), run_time=0.5)

        # 三条公理总结卡片
        summary_title = Text("三大公理", font=FONT_CN, font_size=28,
                             color=COLOR_AXIOM).move_to(DOWN * 2.0)
        s1 = Text("①  线上两点在面内 → 线在面内", font=FONT_CN, font_size=20, color=GRAY_A).move_to(DOWN * 2.9)
        s2 = Text("②  不共线三点确定唯一平面",        font=FONT_CN, font_size=20, color=GRAY_A).move_to(DOWN * 3.6)
        s3 = Text("③  两平面交点 → 唯一交线",         font=FONT_CN, font_size=20, color=GRAY_A).move_to(DOWN * 4.3)

        self.play(FadeIn(summary_title), run_time=0.4)
        for s in [s1, s2, s3]:
            self.play(FadeIn(s, shift=RIGHT*0.3), run_time=0.35)

        self.wait(1.5)

        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id), FadeOut(follow_txt),
            FadeOut(summary_title), FadeOut(s1), FadeOut(s2), FadeOut(s3),
            run_time=0.8
        )