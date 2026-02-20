"""
实系数一元二次方程 - 复数根 Manim 教学动画
高二数学 | 第十三章 | 复数

渲染命令:
  manim -pql complex_quadratic.py ComplexQuadratic   # 快速预览
  manim -qh  complex_quadratic.py ComplexQuadratic   # 高质量
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────────
# 全局配置 — TikTok 竖屏 1080×1920
# ─────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─────────────────────────────────────────────
# 颜色常量
# ─────────────────────────────────────────────
BG_COLOR      = "#1a1a2e"
COL_GOLD      = "#f39c12"
COL_GREEN     = "#2ecc71"
COL_BLUE      = "#3498db"
COL_RED       = "#e74c3c"
COL_PURPLE    = "#9b59b6"
COL_GRAY      = "#95a5a6"
COL_WHITE     = WHITE
COL_YELLOW    = YELLOW

FONT = "Noto Sans CJK SC"

# ─────────────────────────────────────────────
# 主场景
# ─────────────────────────────────────────────
class ComplexQuadratic(Scene):
    """
    实系数一元二次方程 ax²+bx+c=0 的复数根教学动画
    场景顺序：
      0. 开场 Hook
      1. 判别式 Δ 引入
      2. Δ > 0  两实根（绿色抛物线）
      3. Δ = 0  重根  （蓝色抛物线）
      4. Δ < 0  复根  （红色抛物线）
      5. 复数根公式推导
      6. 韦达定理（复数域）
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者信息（全程保留）
        self.author_mob = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=COL_GRAY
        ).move_to(UP * 7.3)
        self.add(self.author_mob)

        self.scene_0_hook()
        self.scene_1_discriminant()
        self.scene_2_two_real_roots()
        self.scene_3_double_root()
        self.scene_4_no_real_root()
        self.scene_5_complex_formula()
        self.scene_6_vieta()
        self.scene_7_outro()

    # ══════════════════════════════════════════
    # Scene 0: 开场 Hook
    # ══════════════════════════════════════════
    def scene_0_hook(self):
        title = Text("一元二次方程", font=FONT, font_size=44, color=COL_GOLD)
        title.move_to(UP * 5.8)

        subtitle = Text("当判别式 Δ < 0 时，根去哪了？",
                        font=FONT, font_size=26, color=COL_WHITE)
        subtitle.move_to(UP * 4.9)

        eq = MathTex(r"ax^2 + bx + c = 0 \quad (a \neq 0)",
                     font_size=32, color=COL_WHITE)
        eq.move_to(UP * 3.9)

        question = Text("数轴上找不到？", font=FONT, font_size=30, color=COL_YELLOW)
        question.move_to(UP * 3.0)

        arrow = Text("↓ 答案在复数域！", font=FONT, font_size=26, color=COL_PURPLE)
        arrow.move_to(UP * 2.3)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.play(Write(eq), run_time=0.8)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(arrow, shift=UP * 0.2), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(subtitle),
            FadeOut(question),
            FadeOut(arrow),
            run_time=0.4
        )
        # title 和 eq 继续保留，稍后清理
        self.hook_title = title
        self.hook_eq = eq

    # ══════════════════════════════════════════
    # Scene 1: 判别式 Δ
    # ══════════════════════════════════════════
    def scene_1_discriminant(self):
        # 清理 hook
        self.play(
            FadeOut(self.hook_title),
            FadeOut(self.hook_eq),
            run_time=0.4
        )

        # 判别式标题
        delta_title = Text("判别式", font=FONT, font_size=38, color=COL_GOLD)
        delta_title.move_to(UP * 6.2)

        delta_formula = MathTex(r"\Delta = b^2 - 4ac", font_size=40, color=COL_WHITE)
        delta_formula.move_to(UP * 5.3)

        self.play(Write(delta_title), run_time=0.6)
        self.play(Write(delta_formula), run_time=0.7)

        # 三种情形
        cond_data = [
            (r"\Delta > 0", "两个不等实根", COL_GREEN,  UP * 4.1),
            (r"\Delta = 0", "两个相等实根（重根）", COL_BLUE,   UP * 3.1),
            (r"\Delta < 0", "两个共轭虚根", COL_RED,    UP * 2.1),
        ]

        cond_mobs = []
        for tex, cn_text, col, pos in cond_data:
            tex_mob = MathTex(tex, font_size=32, color=col)
            cn_mob  = Text(cn_text, font=FONT, font_size=22, color=col)
            row = VGroup(tex_mob, cn_mob).arrange(RIGHT, buff=0.4)
            row.move_to(pos)
            self.play(FadeIn(row, shift=UP * 0.15), run_time=0.5)
            self.wait(0.3)
            cond_mobs.append(row)

        self.wait(1.0)

        self.play(
            FadeOut(delta_title),
            FadeOut(delta_formula),
            *[FadeOut(m) for m in cond_mobs],
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # 辅助：创建坐标系（复用）
    # ══════════════════════════════════════════
    def _make_axes(self):
        axes = Axes(
            x_range=[-0.5, 4.5, 1],
            y_range=[-0.5, 5.5, 1],
            x_length=7.0,
            y_length=5.0,
            axis_config={
                "include_numbers": False,
                "include_tip": True,
                "tip_length": 0.2,
                "color": COL_GRAY,
            }
        )
        axes.move_to(UP * 1.8)
        # 轴标签
        x_label = MathTex("x", font_size=22, color=COL_GRAY).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        y_label = MathTex("y", font_size=22, color=COL_GRAY).next_to(axes.y_axis.get_end(), UP, buff=0.1)
        return axes, x_label, y_label

    # ══════════════════════════════════════════
    # Scene 2: Δ > 0 两实根
    # ══════════════════════════════════════════
    def scene_2_two_real_roots(self):
        # 场景标题
        sc_title = Text("Δ > 0  两个不等实根", font=FONT, font_size=32, color=COL_GREEN)
        sc_title.move_to(UP * 6.3)
        self.play(Write(sc_title), run_time=0.6)

        # 方程标注
        # f(x) = x^2 - 3x + 2 = (x-1)(x-2), roots: 1, 2; Δ=1>0
        eq_label = MathTex(r"f(x) = x^2 - 3x + 2", font_size=28, color=COL_GREEN)
        eq_label.move_to(UP * 5.5)
        delta_label = MathTex(r"\Delta = 1 > 0", font_size=26, color=COL_YELLOW)
        delta_label.move_to(UP * 4.85)

        self.play(Write(eq_label), run_time=0.6)
        self.play(Write(delta_label), run_time=0.5)

        # 坐标系
        axes, xl, yl = self._make_axes()
        self.play(Create(axes), FadeIn(xl), FadeIn(yl), run_time=0.7)

        # 抛物线
        parabola = axes.plot(
            lambda x: x**2 - 3*x + 2,
            x_range=[0.0, 3.0],
            color=COL_GREEN,
            stroke_width=3
        )
        self.play(Create(parabola), run_time=1.0)

        # 两个根: x=1, x=2
        r1 = axes.c2p(1, 0)
        r2 = axes.c2p(2, 0)

        dot1 = Dot(r1, color=COL_YELLOW, radius=0.1)
        dot2 = Dot(r2, color=COL_YELLOW, radius=0.1)
        dline1 = DashedLine(r1, axes.c2p(1, 0.01),
                            color=COL_YELLOW, dash_length=0.08)  # 极短，仅高亮
        dline1 = DashedLine(axes.c2p(1, 2.0), r1,
                            color=COL_YELLOW, dash_length=0.08)
        dline2 = DashedLine(axes.c2p(2, 0.0), axes.c2p(2, 0.0),
                            color=COL_YELLOW, dash_length=0.08)

        lbl1 = MathTex(r"x_1=1", font_size=22, color=COL_YELLOW).next_to(dot1, DOWN+LEFT, buff=0.12)
        lbl2 = MathTex(r"x_2=2", font_size=22, color=COL_YELLOW).next_to(dot2, DOWN+RIGHT, buff=0.12)

        self.play(FadeIn(dot1, scale=0.5), FadeIn(dot2, scale=0.5), run_time=0.5)
        self.play(Write(lbl1), Write(lbl2), run_time=0.5)

        # 求根公式
        formula = MathTex(r"x = \frac{-b \pm \sqrt{\Delta}}{2a}",
                          font_size=30, color=COL_WHITE)
        formula.move_to(DOWN * 3.2)
        self.play(Write(formula), run_time=0.7)

        # 韦达定理简示
        vieta_hint = MathTex(r"x_1 + x_2 = 3 = \frac{3}{1},\quad x_1 x_2 = 2",
                             font_size=24, color=COL_GRAY)
        vieta_hint.move_to(DOWN * 4.2)
        self.play(FadeIn(vieta_hint, shift=UP * 0.1), run_time=0.5)

        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(sc_title), FadeOut(eq_label), FadeOut(delta_label),
            FadeOut(parabola), FadeOut(dot1), FadeOut(dot2),
            FadeOut(lbl1), FadeOut(lbl2),
            FadeOut(formula), FadeOut(vieta_hint),
            run_time=0.5
        )
        self.axes_base = axes
        self.xl_base = xl
        self.yl_base = yl

    # ══════════════════════════════════════════
    # Scene 3: Δ = 0 重根
    # ══════════════════════════════════════════
    def scene_3_double_root(self):
        sc_title = Text("Δ = 0  两个相等的实根", font=FONT, font_size=32, color=COL_BLUE)
        sc_title.move_to(UP * 6.3)
        self.play(Write(sc_title), run_time=0.6)

        eq_label = MathTex(r"f(x) = x^2 - 2x + 1", font_size=28, color=COL_BLUE)
        eq_label.move_to(UP * 5.5)
        delta_label = MathTex(r"\Delta = 0", font_size=26, color=COL_YELLOW)
        delta_label.move_to(UP * 4.85)

        self.play(Write(eq_label), Write(delta_label), run_time=0.6)

        axes, xl, yl = self._make_axes()
        self.play(Create(axes), FadeIn(xl), FadeIn(yl), run_time=0.5)

        parabola = axes.plot(
            lambda x: x**2 - 2*x + 1,
            x_range=[0.0, 2.5],
            color=COL_BLUE,
            stroke_width=3
        )
        self.play(Create(parabola), run_time=0.9)

        # 重根 x=1
        r0 = axes.c2p(1, 0)
        dot0 = Dot(r0, color=COL_YELLOW, radius=0.12)
        # 中文不能放 MathTex，拆分
        lbl0a = MathTex(r"x_0 = 1", font_size=24, color=COL_YELLOW)
        lbl0b = Text("（重根）", font=FONT, font_size=20, color=COL_YELLOW)
        lbl0g = VGroup(lbl0a, lbl0b).arrange(RIGHT, buff=0.15)
        lbl0g.next_to(dot0, DOWN + LEFT, buff=0.2)

        formula0 = MathTex(r"x_1 = x_2 = -\frac{b}{2a} = 1",
                           font_size=28, color=COL_WHITE)
        formula0.move_to(DOWN * 3.5)

        self.play(FadeIn(dot0, scale=0.5), run_time=0.4)
        self.play(Write(lbl0g), run_time=0.5)
        self.play(Write(formula0), run_time=0.7)

        # 切线说明
        tangent_hint = Text("抛物线与 x 轴相切", font=FONT, font_size=22, color=COL_GRAY)
        tangent_hint.move_to(DOWN * 4.6)
        self.play(FadeIn(tangent_hint), run_time=0.4)

        self.wait(1.2)

        self.play(
            FadeOut(sc_title), FadeOut(eq_label), FadeOut(delta_label),
            FadeOut(parabola), FadeOut(dot0), FadeOut(lbl0g),
            FadeOut(formula0), FadeOut(tangent_hint),
            run_time=0.5
        )
        self.play(FadeOut(axes), FadeOut(xl), FadeOut(yl), run_time=0.3)

    # ══════════════════════════════════════════
    # Scene 4: Δ < 0 无实根
    # ══════════════════════════════════════════
    def scene_4_no_real_root(self):
        sc_title = Text("Δ < 0  无实数根！", font=FONT, font_size=32, color=COL_RED)
        sc_title.move_to(UP * 6.3)
        self.play(Write(sc_title), run_time=0.6)

        eq_label = MathTex(r"f(x) = x^2 - 2x + 5", font_size=28, color=COL_RED)
        eq_label.move_to(UP * 5.5)
        delta_label = MathTex(r"\Delta = -16 < 0", font_size=26, color=COL_YELLOW)
        delta_label.move_to(UP * 4.85)

        self.play(Write(eq_label), Write(delta_label), run_time=0.6)

        # 坐标系（y轴从-0.5到9）
        axes = Axes(
            x_range=[-0.5, 4.5, 1],
            y_range=[-0.5, 9.5, 1],
            x_length=7.0,
            y_length=5.0,
            axis_config={"include_tip": True, "tip_length": 0.2, "color": COL_GRAY}
        )
        axes.move_to(UP * 1.8)
        xl = MathTex("x", font_size=22, color=COL_GRAY).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1)
        yl = MathTex("y", font_size=22, color=COL_GRAY).next_to(axes.y_axis.get_end(), UP, buff=0.1)
        self.play(Create(axes), FadeIn(xl), FadeIn(yl), run_time=0.6)

        parabola = axes.plot(
            lambda x: x**2 - 2*x + 5,
            x_range=[0.0, 3.0],
            color=COL_RED,
            stroke_width=3
        )
        self.play(Create(parabola), run_time=0.9)

        # 标注顶点（1, 4）最低点，不触 x 轴
        vertex_pt = axes.c2p(1, 4)
        vertex_dot = Dot(vertex_pt, color=COL_YELLOW, radius=0.08)
        vertex_lbl = MathTex(r"(1,4)", font_size=20, color=COL_YELLOW).next_to(vertex_dot, RIGHT, buff=0.1)
        self.play(FadeIn(vertex_dot), Write(vertex_lbl), run_time=0.5)

        # X 号说明无实根
        cross_text = Text("✗ 与 x 轴无交点", font=FONT, font_size=26, color=COL_RED)
        cross_text.move_to(DOWN * 3.0)
        self.play(FadeIn(cross_text, shift=UP * 0.2), run_time=0.5)

        hint_text = Text("→ 在复数范围寻找根", font=FONT, font_size=26, color=COL_PURPLE)
        hint_text.move_to(DOWN * 4.0)
        self.play(FadeIn(hint_text, shift=UP * 0.2), run_time=0.5)

        self.wait(1.5)

        self.play(
            FadeOut(sc_title), FadeOut(eq_label), FadeOut(delta_label),
            FadeOut(parabola), FadeOut(axes), FadeOut(xl), FadeOut(yl),
            FadeOut(vertex_dot), FadeOut(vertex_lbl),
            FadeOut(cross_text), FadeOut(hint_text),
            run_time=0.6
        )

    # ══════════════════════════════════════════
    # Scene 5: 复数根公式推导
    # ══════════════════════════════════════════
    def scene_5_complex_formula(self):
        sc_title = Text("复数根推导", font=FONT, font_size=36, color=COL_PURPLE)
        sc_title.move_to(UP * 6.3)
        self.play(Write(sc_title), run_time=0.6)

        # 起始：求根公式
        step_labels = [
            Text("求根公式：", font=FONT, font_size=22, color=COL_GRAY),
            Text("当 Δ < 0，令 Δ = -|Δ|：", font=FONT, font_size=22, color=COL_GRAY),
            Text("利用虚数单位 i：", font=FONT, font_size=22, color=COL_GRAY),
            Text("代入得：", font=FONT, font_size=22, color=COL_GRAY),
        ]
        step_formulas = [
            MathTex(r"x = \frac{-b \pm \sqrt{\Delta}}{2a}", font_size=34),
            MathTex(r"x = \frac{-b \pm \sqrt{-|\Delta|}}{2a}", font_size=34),
            MathTex(r"\sqrt{-|\Delta|} = i\sqrt{|\Delta|}", font_size=34, color=COL_PURPLE),
            MathTex(r"x = \frac{-b \pm i\sqrt{|\Delta|}}{2a}", font_size=34, color=COL_PURPLE),
        ]

        y_start = 5.4
        all_mobs = []
        for i, (lbl, fml) in enumerate(zip(step_labels, step_formulas)):
            y = y_start - i * 1.6
            lbl.move_to(LEFT * 1.5 + UP * y)
            fml.next_to(lbl, DOWN, buff=0.15, aligned_edge=LEFT)
            fml.shift(RIGHT * 0.3)
            group = VGroup(lbl, fml)
            all_mobs.append(group)
            self.play(FadeIn(lbl, shift=RIGHT * 0.15), run_time=0.4)
            self.play(Write(fml), run_time=0.7)
            if i < 3:
                self.wait(0.5)

        self.wait(1.8)

        # 结论框
        conclusion_text = Text("共轭虚根成对出现！", font=FONT, font_size=26, color=COL_YELLOW)
        conclusion_text.move_to(DOWN * 5.3)
        self.play(FadeIn(conclusion_text, scale=1.1), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(sc_title),
            *[FadeOut(m) for m in all_mobs],
            FadeOut(conclusion_text),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 6: 韦达定理（复数域）
    # ══════════════════════════════════════════
    def scene_6_vieta(self):
        sc_title = Text("韦达定理（复数域同样成立）",
                        font=FONT, font_size=28, color=COL_GOLD)
        sc_title.move_to(UP * 6.3)
        self.play(Write(sc_title), run_time=0.7)

        # 韦达定理
        vieta_title = Text("韦达定理：", font=FONT, font_size=28, color=COL_WHITE)
        vieta_title.move_to(UP * 5.5)

        vieta1 = MathTex(r"x_1 + x_2 = -\frac{b}{a}", font_size=34, color=COL_GREEN)
        vieta1.move_to(UP * 4.7)

        vieta2 = MathTex(r"x_1 \cdot x_2 = \frac{c}{a}", font_size=34, color=COL_GREEN)
        vieta2.move_to(UP * 3.9)

        self.play(FadeIn(vieta_title), run_time=0.4)
        self.play(Write(vieta1), run_time=0.6)
        self.play(Write(vieta2), run_time=0.6)

        # 分割线
        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=COL_GRAY, stroke_width=1.5)
        divider.move_to(UP * 3.3)
        self.play(Create(divider), run_time=0.3)

        # 验证示例：x² - 2x + 5 = 0，根为 1±2i
        example_lbl = Text("验证：x² - 2x + 5 = 0", font=FONT, font_size=22, color=COL_GRAY)
        example_lbl.move_to(UP * 2.8)
        roots_lbl = MathTex(r"x_1 = 1+2i, \quad x_2 = 1-2i", font_size=26, color=COL_WHITE)
        roots_lbl.move_to(UP * 2.1)

        check1 = MathTex(r"x_1 + x_2 = 2 = -\frac{-2}{1} \checkmark",
                         font_size=24, color=COL_GREEN)
        check1.move_to(UP * 1.3)
        check2 = MathTex(r"x_1 x_2 = (1+2i)(1-2i) = 1+4 = 5 = \frac{5}{1} \checkmark",
                         font_size=22, color=COL_GREEN)
        check2.move_to(UP * 0.5)

        self.play(FadeIn(example_lbl, shift=UP * 0.1), run_time=0.4)
        self.play(Write(roots_lbl), run_time=0.6)
        self.wait(0.3)
        self.play(Write(check1), run_time=0.6)
        self.play(Write(check2), run_time=0.8)
        self.wait(1.5)

        # 任何实系数多项式：虚根成共轭对
        conjugate_text = Text(
            "实系数方程的虚根必成共轭对出现",
            font=FONT, font_size=22, color=COL_PURPLE
        )
        conjugate_text.move_to(DOWN * 0.5)
        self.play(FadeIn(conjugate_text, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(sc_title), FadeOut(vieta_title),
            FadeOut(vieta1), FadeOut(vieta2), FadeOut(divider),
            FadeOut(example_lbl), FadeOut(roots_lbl),
            FadeOut(check1), FadeOut(check2), FadeOut(conjugate_text),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 7: 片尾
    # ══════════════════════════════════════════
    def scene_7_outro(self):
        # 作者大名
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=COL_WHITE
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=COL_GRAY
        ).move_to(UP * 1.1)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=COL_YELLOW
        ).move_to(UP * 0.0)

        # 三条总结要点
        summary_data = [
            ("Δ > 0", "两不等实根", COL_GREEN),
            ("Δ = 0", "两相等实根", COL_BLUE),
            ("Δ < 0", "两共轭虚根", COL_RED),
        ]
        rows = VGroup()
        for tex, cn, col in summary_data:
            t1 = MathTex(tex, font_size=26, color=col)
            t2 = Text(cn, font=FONT, font_size=20, color=col)
            row = VGroup(t1, t2).arrange(RIGHT, buff=0.4)
            rows.add(row)
        rows.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        rows.move_to(DOWN * 2.0)

        self.play(
            Transform(self.author_mob, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow_text, shift=UP * 0.15), run_time=0.5)

        self.play(FadeIn(rows, shift=UP * 0.2), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(self.author_mob),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(rows),
            run_time=0.8
        )