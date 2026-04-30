"""
二次函数的概念 — Quadratic Function Concept
九年级 第二十六章 数学教学动画

内容:
  Scene 1  开场钩子
  Scene 2  回顾一次函数 (引导)
  Scene 3  认识二次函数 — 一般式 y = ax²+bx+c
  Scene 4  图像观察 — 标准抛物线 y = x²
  Scene 5  顶点式 y = a(x-h)²+k
  Scene 6  交点式 y = a(x-x₁)(x-x₂)
  Scene 7  三种形式对比
  Scene 8  关键要点总结
  Scene 9  片尾 + 关注

目标观众  : 九年级学生
格式      : TikTok 竖屏 1080×1920
作者      : 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ──────────────────────────────────────────────
# 全局配置 — TikTok 竖屏
# ──────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9      # 逻辑宽
config.frame_height = 16     # 逻辑高

# ──────────────────────────────────────────────
# 色彩 & 字体常量
# ──────────────────────────────────────────────
BG_COLOR       = "#1a1a2e"
C_PRIMARY      = "#e94560"   # 红粉 — 主抛物线
C_SECONDARY    = "#0f3460"   # 深蓝
C_ACCENT       = "#e94560"
C_GOLD         = "#f5a623"
C_GREEN        = "#2ecc71"
C_BLUE         = "#3498db"
C_PURPLE       = "#9b59b6"
C_AXIS         = "#555555"
C_GRID         = "#333344"
C_TEXT         = WHITE
C_SUBTEXT      = GRAY_A
C_LABEL        = YELLOW

FONT = "PingFang SC"

# 字体规范
FS_TITLE    = 38
FS_SUB      = 26
FS_BODY     = 22
FS_SMALL    = 18
FS_FORMULA  = 30
FS_AUTHOR   = 20


class QuadraticFunctionIntro(Scene):
    """
    九年级 — 二次函数的概念
    """

    # ═══════════════════════════════════════════
    # 构建入口
    # ═══════════════════════════════════════════
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 预计算几何 ──
        self.setup_geometry()

        # ── 场景序列 ──
        self.scene_opening()
        self.scene_linear_recap()
        self.scene_general_form()
        self.scene_standard_parabola()
        self.scene_vertex_form()
        self.scene_intercept_form()
        self.scene_three_forms_compare()
        self.scene_key_points()
        self.scene_outro()

    # ═══════════════════════════════════════════
    # 几何预计算（仅 numpy，无 manim 包）
    # ═══════════════════════════════════════════
    def setup_geometry(self):
        # 坐标轴数据范围 — 经 verify_geometry.py 验证
        self.AX_X = [-3, 3, 1]
        self.AX_Y = [-2.5, 5, 1]
        self.AX_X_LEN = 7.0
        self.AX_Y_LEN = 7.0
        self.AX_CENTER = UP * 0.5   # axes.move_to 目标

        # 五条抛物线定义
        # 曲线 x 范围限制在 [-2.5, 2.5]，避免顶端溢出
        self.CURVE_X = [-2.5, 2.5]

        # — 函数定义 —
        # 1) 标准     y = x²
        self.f_std     = lambda x: x**2
        # 2) 右移     y = (x-1)²       vertex (1, 0)
        self.f_shift   = lambda x: (x - 1)**2
        # 3) 顶点式   y = (x-1)² - 1   vertex (1,-1)   roots 0,2
        self.f_vtx     = lambda x: (x - 1)**2 - 1
        # 4) 拉伸     y = 2(x-1)² - 1  vertex (1,-1)   steeper
        self.f_stretch = lambda x: 2*(x - 1)**2 - 1
        # 5) 交点式   y = (x+1)(x-2)   roots -1,2      vertex (0.5,-2.25)
        self.f_inter   = lambda x: (x + 1)*(x - 2)

        # — 关键点缓存 —
        self.vtx_std     = np.array([0.0,  0.0])
        self.vtx_shift   = np.array([1.0,  0.0])
        self.vtx_vtx     = np.array([1.0, -1.0])
        self.roots_vtx   = np.array([0.0, 2.0])        # x=0, x=2
        self.vtx_inter   = np.array([0.5, -2.25])
        self.roots_inter = np.array([-1.0, 2.0])       # x=-1, x=2
        self.yint_inter  = np.array([0.0, -2.0])       # y-截距

    # ── 创建带样式的坐标轴 ──
    def make_axes(self):
        axes = Axes(
            x_range=self.AX_X,
            y_range=self.AX_Y,
            x_length=self.AX_X_LEN,
            y_length=self.AX_Y_LEN,
            axis_config={
                "color": C_SUBTEXT,
                "stroke_width": 1.5,
                "include_ticks": True,
                "tick_size": 0.08,
            },
        )
        axes.move_to(self.AX_CENTER)
        # 轴标签
        x_lab = axes.get_axis_labels(
            x_label=MathTex("x", color=C_SUBTEXT, font_size=20),
            y_label=MathTex("y", color=C_SUBTEXT, font_size=20),
        )
        return axes, x_lab

    # ── 辅助：作者条 ──
    def make_author_bar(self):
        return Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=FS_AUTHOR, color=GRAY_B,
        ).move_to(UP * 7.2)

    # ═══════════════════════════════════════════
    # Scene 1 — 开场钩子
    # ═══════════════════════════════════════════
    def scene_opening(self):
        # 作者条
        author = self.make_author_bar()
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author_bar = author   # 保留

        # 钩子文字
        hook = Text(
            "一个函数，只需换一个字母，\n就能画出漂亮的抛物线？",
            font=FONT, font_size=FS_SUB, color=C_GOLD,
            line_spacing=1.4,
        ).move_to(UP * 4.5)

        self.play(Write(hook), run_time=1.2)

        # 快速闪一条抛物线
        axes, x_lab = self.make_axes()
        axes.move_to(DOWN * 1.5)
        curve = axes.plot(self.f_std, x_range=self.CURVE_X, color=C_PRIMARY, stroke_width=3)
        self.play(Create(axes), run_time=0.6)
        self.play(Create(curve), run_time=1.0)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(axes),
            FadeOut(curve),
            FadeOut(x_lab) if x_lab else [],
            run_time=0.5,
        )

    # ═══════════════════════════════════════════
    # Scene 2 — 回顾一次函数
    # ═══════════════════════════════════════════
    def scene_linear_recap(self):
        title = Text("回顾：一次函数", font=FONT, font_size=FS_TITLE, color=C_BLUE).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 公式
        eq_lin = MathTex(r"y = kx + b \quad (k \neq 0)", font_size=FS_FORMULA, color=WHITE)
        eq_lin.move_to(UP * 5.2)
        self.play(Write(eq_lin), run_time=0.7)

        # 画一次函数图像
        axes, x_lab = self.make_axes()
        axes.move_to(UP * 1.0)
        self.play(Create(axes), run_time=0.6)

        line_graph = axes.plot(lambda x: 0.8 * x + 0.5, x_range=[-2.8, 2.8], color=C_BLUE, stroke_width=3)
        self.play(Create(line_graph), run_time=0.8)

        # 标注
        note = Text("图像是一条直线", font=FONT, font_size=FS_BODY, color=C_SUBTEXT).move_to(DOWN * 3.0)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)

        # 过渡文字
        transition = Text(
            "那如果把 x 变成 x² 呢？",
            font=FONT, font_size=FS_SUB, color=C_GOLD,
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(transition, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(title), FadeOut(eq_lin),
            FadeOut(axes), FadeOut(line_graph),
            FadeOut(note), FadeOut(transition),
            run_time=0.5,
        )

    # ═══════════════════════════════════════════
    # Scene 3 — 一般式定义
    # ═══════════════════════════════════════════
    def scene_general_form(self):
        title = Text("二次函数 — 一般式", font=FONT, font_size=FS_TITLE, color=C_PRIMARY).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 核心公式
        eq = MathTex(
            r"y = ", "ax^2", r" + ", "bx", r" + ", "c",
            font_size=FS_FORMULA + 4, color=WHITE,
        )
        eq[1].set_color(C_PRIMARY)   # ax²  红
        eq[3].set_color(C_BLUE)      # bx   蓝
        eq[5].set_color(C_GREEN)     # c    绿
        eq.move_to(UP * 5.0)
        self.play(Write(eq), run_time=0.9)

        # 条件标注
        cond = MathTex(r"(a \neq 0)", font_size=FS_BODY, color=C_GOLD)
        cond.next_to(eq, RIGHT, buff=0.3)
        self.play(FadeIn(cond), run_time=0.3)
        self.wait(0.5)

        # 逐项说明卡片
        cards_data = [
            (r"a", "二次项系数",  C_PRIMARY,  UP * 3.5),
            (r"b", "一次项系数",  C_BLUE,     UP * 2.5),
            (r"c", "常数项",      C_GREEN,    UP * 1.5),
        ]
        cards = []
        for sym, desc, col, pos in cards_data:
            sym_tex = MathTex(sym, font_size=FS_SUB + 2, color=col)#, weight=BOLD)
            desc_text = Text(desc, font=FONT, font_size=FS_SMALL, color=C_SUBTEXT)
            grp = VGroup(sym_tex, desc_text).arrange(RIGHT, buff=0.25)
            grp.move_to(pos + LEFT * 1.5)
            cards.append(grp)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.35)

        self.wait(0.6)

        # 重点提示
        highlight = Text(
            "关键条件：a ≠ 0",
            font=FONT, font_size=FS_BODY, color=C_GOLD,
        ).move_to(DOWN * 0.8)
        box = RoundedRectangle(
            width=4.5, height=0.8, corner_radius=0.15,
            color=C_GOLD, fill_opacity=0.08, stroke_width=1.5,
        ).move_to(highlight.get_center())
        self.play(Create(box), FadeIn(highlight), run_time=0.5)
        self.wait(1.0)

        # 自变量范围
        domain = Text(
            "自变量 x 的取值范围：全体实数",
            font=FONT, font_size=FS_SMALL, color=C_SUBTEXT,
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(domain), run_time=0.4)
        self.wait(0.8)

        # 清理
        all_items = [title, eq, cond] + cards + [box, highlight, domain]
        self.play(*[FadeOut(m) for m in all_items], run_time=0.5)

    # ═══════════════════════════════════════════
    # Scene 4 — 标准抛物线 y = x²
    # ═══════════════════════════════════════════
    def scene_standard_parabola(self):
        title = Text("标准抛物线", font=FONT, font_size=FS_TITLE, color=C_PRIMARY).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        eq = MathTex(r"y = x^2", font_size=FS_FORMULA, color=WHITE).move_to(UP * 5.5)
        self.play(Write(eq), run_time=0.5)

        # 坐标轴
        axes, x_lab = self.make_axes()
        axes.move_to(UP * 1.0)
        self.play(Create(axes), run_time=0.5)

        # 逐点描绘 — ValueTracker 动态绘制
        t = ValueTracker(self.CURVE_X[0])
        curve = always_redraw(
            lambda: axes.plot(self.f_std, x_range=[self.CURVE_X[0], t.get_value()], color=C_PRIMARY, stroke_width=3)
        )
        dot = always_redraw(
            lambda: Dot(axes.c2p(t.get_value(), self.f_std(t.get_value())), color=C_GOLD, radius=0.08)
        )
        self.add(curve, dot)
        self.play(t.animate.set_value(self.CURVE_X[1]), run_time=2.0, rate_func=linear)
        self.remove(dot)   # 动态点画完后移除

        # 标记顶点
        vtx_dot = Dot(axes.c2p(0, 0), color=C_GOLD, radius=0.1)
        vtx_label = Text("顶点 (0,0)", font=FONT, font_size=FS_SMALL, color=C_GOLD)
        vtx_label.next_to(vtx_dot, DL, buff=0.25)
        self.play(FadeIn(vtx_dot), FadeIn(vtx_label), run_time=0.4)

        # 对称轴
        sym_axis = DashedLine(
            axes.c2p(0, -2.5), axes.c2p(0, 5),
            color=C_PURPLE, stroke_width=1.5, dash_length=0.12,
        )
        sym_label = Text("对称轴 x=0", font=FONT, font_size=FS_SMALL, color=C_PURPLE)
        sym_label.next_to(axes.c2p(0, 4.5), RIGHT, buff=0.15)
        self.play(Create(sym_axis), FadeIn(sym_label), run_time=0.5)
        self.wait(0.6)

        # 开口向上标注
        note = Text("开口向上 (a=1>0)", font=FONT, font_size=FS_BODY, color=C_SUBTEXT).move_to(DOWN * 3.2)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(eq),
            FadeOut(axes), FadeOut(curve),
            FadeOut(vtx_dot), FadeOut(vtx_label),
            FadeOut(sym_axis), FadeOut(sym_label),
            FadeOut(note),
            run_time=0.5,
        )

    # ═══════════════════════════════════════════
    # Scene 5 — 顶点式
    # ═══════════════════════════════════════════
    def scene_vertex_form(self):
        title = Text("顶点式", font=FONT, font_size=FS_TITLE, color=C_BLUE).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        eq_vtx = MathTex(r"y = a(x - h)^2 + k", font_size=FS_FORMULA, color=WHITE).move_to(UP * 5.5)
        self.play(Write(eq_vtx), run_time=0.6)

        # 意义标注
        meaning = Text("顶点坐标为 (h, k)", font=FONT, font_size=FS_BODY, color=C_GOLD).move_to(UP * 4.6)
        self.play(FadeIn(meaning), run_time=0.3)

        # 坐标轴
        axes, x_lab = self.make_axes()
        axes.move_to(UP * 0.8)
        self.play(Create(axes), run_time=0.5)

        # 先画标准抛物线（灰色参考）
        ref_curve = axes.plot(self.f_std, x_range=self.CURVE_X, color=GRAY_B, stroke_width=1.5)
        self.play(Create(ref_curve), run_time=0.6)
        ref_label = Text("y = x²", font=FONT, font_size=FS_SMALL, color=GRAY_B)
        ref_label.next_to(axes.c2p(2.0, self.f_std(2.0)), UR, buff=0.1)
        self.play(FadeIn(ref_label), run_time=0.3)

        # 画 y=(x-1)²  — 右移示例  (左端限 -1.9 避免溢出屏幕)
        curve_shift = axes.plot(self.f_shift, x_range=[-1.9, 2.8], color=C_BLUE, stroke_width=2.5)
        self.play(Create(curve_shift), run_time=0.7)
        shift_label = Text("y=(x−1)²", font=FONT, font_size=FS_SMALL, color=C_BLUE)
        shift_label.next_to(axes.c2p(2.3, self.f_shift(2.3)), UR, buff=0.05)
        self.play(FadeIn(shift_label), run_time=0.3)

        # 顶点标记
        vtx1 = Dot(axes.c2p(1, 0), color=C_BLUE, radius=0.09)
        vtx1_lab = Text("(1, 0)", font=FONT, font_size=FS_SMALL, color=C_BLUE)
        vtx1_lab.next_to(vtx1, DR, buff=0.15)
        self.play(FadeIn(vtx1), FadeIn(vtx1_lab), run_time=0.3)
        self.wait(0.5)

        # 画 y=(x-1)²-1  — 再下移  (左端限 -2.0 避免溢出)
        curve_vtx = axes.plot(self.f_vtx, x_range=[-2.0, 2.8], color=C_PRIMARY, stroke_width=2.8)
        self.play(Create(curve_vtx), run_time=0.7)
        vtx_label2 = Text("y=(x−1)²−1", font=FONT, font_size=FS_SMALL, color=C_PRIMARY)
        vtx_label2.next_to(axes.c2p(-1.5, self.f_vtx(-1.5)), UL, buff=0.1)
        self.play(FadeIn(vtx_label2), run_time=0.3)

        # 新顶点
        vtx2 = Dot(axes.c2p(1, -1), color=C_PRIMARY, radius=0.09)
        vtx2_lab = Text("(1, −1)", font=FONT, font_size=FS_SMALL, color=C_PRIMARY)
        vtx2_lab.next_to(vtx2, DR, buff=0.15)
        self.play(FadeIn(vtx2), FadeIn(vtx2_lab), run_time=0.3)
        self.wait(0.7)

        # 说明框
        note = Text(
            "h 控制左右平移\nk 控制上下平移",
            font=FONT, font_size=FS_SMALL, color=C_SUBTEXT, line_spacing=1.3,
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.0)

        # 清理
        all_elems = [
            title, eq_vtx, meaning,
            axes, ref_curve, ref_label,
            curve_shift, shift_label, vtx1, vtx1_lab,
            curve_vtx, vtx_label2, vtx2, vtx2_lab,
            note,
        ]
        self.play(*[FadeOut(m) for m in all_elems], run_time=0.5)

    # ═══════════════════════════════════════════
    # Scene 6 — 交点式
    # ═══════════════════════════════════════════
    def scene_intercept_form(self):
        title = Text("交点式", font=FONT, font_size=FS_TITLE, color=C_GREEN).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        eq_int = MathTex(
            r"y = a(x - x_1)(x - x_2)",
            font_size=FS_FORMULA, color=WHITE,
        ).move_to(UP * 5.5)
        self.play(Write(eq_int), run_time=0.6)

        meaning = Text("x₁, x₂ 是与 x 轴的交点", font=FONT, font_size=FS_BODY, color=C_GOLD).move_to(UP * 4.6)
        self.play(FadeIn(meaning), run_time=0.3)

        # 坐标轴
        axes, x_lab = self.make_axes()
        axes.move_to(UP * 0.8)
        self.play(Create(axes), run_time=0.5)

        # 画 y = (x+1)(x-2)
        curve = axes.plot(self.f_inter, x_range=[-2.2, 2.8], color=C_GREEN, stroke_width=3)
        self.play(Create(curve), run_time=0.9)

        # 标记两个根
        r_left  = Dot(axes.c2p(-1, 0), color=C_GOLD, radius=0.1)
        r_right = Dot(axes.c2p(2, 0),  color=C_GOLD, radius=0.1)
        lab_l   = MathTex(r"x_1=-1", font_size=FS_SMALL, color=C_GOLD)
        lab_l.next_to(r_left, UL, buff=0.15)
        lab_r   = MathTex(r"x_2=2", font_size=FS_SMALL, color=C_GOLD)
        lab_r.next_to(r_right, UR, buff=0.15)
        self.play(FadeIn(r_left), FadeIn(r_right), run_time=0.3)
        self.play(FadeIn(lab_l), FadeIn(lab_r), run_time=0.3)

        # 标记顶点
        vtx = Dot(axes.c2p(0.5, -2.25), color=C_PRIMARY, radius=0.09)
        vtx_lab = Text("顶点 (0.5, −2.25)", font=FONT, font_size=FS_SMALL, color=C_PRIMARY)
        vtx_lab.next_to(vtx, DR, buff=0.2)
        self.play(FadeIn(vtx), FadeIn(vtx_lab), run_time=0.4)

        # y 截距
        yi_dot = Dot(axes.c2p(0, -2), color=C_BLUE, radius=0.08)
        yi_lab = MathTex(r"c=-2", font_size=FS_SMALL, color=C_BLUE)
        yi_lab.next_to(yi_dot, LEFT, buff=0.2)
        self.play(FadeIn(yi_dot), FadeIn(yi_lab), run_time=0.3)
        self.wait(0.5)

        # 展开验证
        expand = MathTex(
            r"(x+1)(x-2) = x^2 - x - 2",
            font_size=FS_BODY, color=C_SUBTEXT,
        ).move_to(DOWN * 3.2)
        self.play(Write(expand), run_time=0.6)
        self.wait(1.0)

        # 清理
        all_elems = [
            title, eq_int, meaning,
            axes, curve,
            r_left, r_right, lab_l, lab_r,
            vtx, vtx_lab,
            yi_dot, yi_lab,
            expand,
        ]
        self.play(*[FadeOut(m) for m in all_elems], run_time=0.5)

    # ═══════════════════════════════════════════
    # Scene 7 — 三种形式对比
    # ═══════════════════════════════════════════
    def scene_three_forms_compare(self):
        title = Text("三种形式对比", font=FONT, font_size=FS_TITLE, color=C_GOLD).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # 三行公式卡
        row_data = [
            (r"y = ax^2 + bx + c",          "一般式",   C_PRIMARY,  UP * 5.2),
            (r"y = a(x - h)^2 + k",         "顶点式",   C_BLUE,     UP * 4.2),
            (r"y = a(x - x_1)(x - x_2)",    "交点式",   C_GREEN,    UP * 3.2),
        ]

        rows = []
        for formula_str, name, col, pos in row_data:
            name_text = Text(name, font=FONT, font_size=FS_BODY, color=col, weight=BOLD)
            formula   = MathTex(formula_str, font_size=FS_BODY, color=WHITE)
            row = VGroup(name_text, formula).arrange(RIGHT, buff=0.4)
            row.move_to(pos)
            rows.append(row)

        for row in rows:
            self.play(FadeIn(row, shift=LEFT * 0.4), run_time=0.4)
            self.wait(0.15)

        self.wait(0.5)

        # 特殊能力标注
        abilities = [
            ("→ 知道系数 a,b,c", C_PRIMARY,   DOWN * 0.2),
            ("→ 直接知道顶点坐标", C_BLUE,     DOWN * 1.0),
            ("→ 直接知道与x轴交点", C_GREEN,   DOWN * 1.8),
        ]
        abil_objs = []
        for txt, col, pos in abilities:
            t = Text(txt, font=FONT, font_size=FS_SMALL, color=col)
            t.move_to(pos)
            abil_objs.append(t)
            self.play(FadeIn(t, shift=UP * 0.2), run_time=0.35)

        self.wait(0.5)

        # 共通条件
        common = Text("三种形式都要求 a ≠ 0", font=FONT, font_size=FS_BODY, color=C_GOLD).move_to(DOWN * 3.2)
        box = RoundedRectangle(
            width=5.2, height=0.7, corner_radius=0.15,
            color=C_GOLD, fill_opacity=0.1, stroke_width=1.5,
        ).move_to(common.get_center())
        self.play(Create(box), FadeIn(common), run_time=0.5)
        self.wait(1.2)

        # 清理
        all_elems = [title] + rows + abil_objs + [common, box]
        self.play(*[FadeOut(m) for m in all_elems], run_time=0.5)

    # ═══════════════════════════════════════════
    # Scene 8 — 关键要点
    # ═══════════════════════════════════════════
    def scene_key_points(self):
        title = Text("记住这些", font=FONT, font_size=FS_TITLE, color=C_GOLD).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        points = [
            ("① 二次项系数 a ≠ 0 是本质要求",       C_PRIMARY),
            ("② 图像是抛物线，不是直线",            C_BLUE),
            ("③ a > 0 开口向上，a < 0 开口向下",    C_GREEN),
            ("④ 顶点是抛物线的最高/最低点",         C_PURPLE),
            ("⑤ 抛物线关于对称轴左右对称",          C_GOLD),
        ]

        objs = []
        y_start = 5.0
        for i, (text, col) in enumerate(points):
            t = Text(text, font=FONT, font_size=FS_BODY, color=col)
            t.move_to(np.array([0, y_start - i * 1.1, 0]))
            objs.append(t)
            self.play(FadeIn(t, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        self.wait(1.2)

        # 清理
        self.play(FadeOut(title), *[FadeOut(o) for o in objs], run_time=0.5)

    # ═══════════════════════════════════════════
    # Scene 9 — 片尾
    # ═══════════════════════════════════════════
    def scene_outro(self):
        # 作者大字
        name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE,
        ).move_to(UP * 2.0)
        aid = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B,
        ).move_to(UP * 1.0)

        self.play(
            Transform(self.author_bar, name),
            run_time=0.8,
        )
        self.play(FadeIn(aid, shift=UP * 0.3), run_time=0.4)

        # 关注文字
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=FS_SUB, color=C_GOLD,
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 小抛物线装饰
        deco_axes = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-0.3, 1.5, 1],
            x_length=1.2, y_length=1.0,
            axis_config={"stroke_width": 0, "include_ticks": False},
        )
        deco_curve = deco_axes.plot(lambda x: x**2, x_range=[-1.2, 1.2], color=C_PRIMARY, stroke_width=2)
        deco = VGroup(deco_axes, deco_curve)
        deco.move_to(DOWN * 2.5)
        self.play(Create(deco), run_time=0.6)

        self.wait(2.0)

        # 淡出
        self.play(
            FadeOut(name), FadeOut(aid),
            FadeOut(follow), FadeOut(deco),
            run_time=1.0,
        )