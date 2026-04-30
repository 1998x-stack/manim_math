"""
复数的平方根与立方根 - Manim 教学动画
高二数学 第十三章 复数

关键验证结论（来自 verify_roots.py）：
  · √(-4) = ±2i  ✓
  · w²=3+4i → w=2+i 或 w=-2-i  ✓
  · 1的三个立方根相邻角度=120°，全部为 CCW（other_angle=False）✓
  · 所有边界 ✓

渲染命令：
  manim -pql complex_roots.py ComplexRoots   # 快速预览
  manim -qh  complex_roots.py ComplexRoots   # 高质量
"""

from manim import *
import numpy as np

# ────────────────────────────────────────
# TikTok 竖屏配置
# ────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ────────────────────────────────────────
# 颜色常量
# ────────────────────────────────────────
BG_COLOR    = "#1a1a2e"
COL_GOLD    = "#f39c12"
COL_GREEN   = "#2ecc71"
COL_BLUE    = "#3498db"
COL_RED     = "#e74c3c"
COL_PURPLE  = "#9b59b6"
COL_TEAL    = "#1abc9c"
COL_GRAY    = "#7f8c8d"
COL_GRAY_L  = "#95a5a6"
COL_YELLOW = "#ffff00"

FONT = "PingFang SC"

# 经验证的精确坐标
# 复平面中心 = (0, 1.5)，UNIT_R = 2.0
UNIT_R = 2.0
PLANE_CENTER = np.array([0.0, 1.5, 0.0])

def cube_root_point(k):
    """1 的第 k 个立方根坐标（在复平面视觉空间，带 PLANE_CENTER 偏移）"""
    angle = 2 * np.pi * k / 3
    local = np.array([UNIT_R * np.cos(angle), UNIT_R * np.sin(angle), 0.0])
    return local + PLANE_CENTER


class ComplexRoots(Scene):
    """
    复数的平方根与立方根教学动画
    Scene 0: 开场 Hook
    Scene 1: 负数平方根 √(-a)=±√a·i
    Scene 2: 一般复数平方根（设 w=x+yi）
    Scene 3: 立方根与 De Moivre 公式
    Scene 4: 1的三个立方根 — 复平面可视化
    Scene 5: ω 的重要性质
    Scene 6: 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.author_mob = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=COL_GRAY_L
        ).move_to(UP * 7.0)
        self.add(self.author_mob)

        self.scene_0_hook()
        self.scene_1_sqrt_negative()
        self.scene_2_general_sqrt()
        self.scene_3_cube_root_formula()
        self.scene_4_cube_roots_visual()
        self.scene_5_omega_properties()
        self.scene_6_outro()

    # ══════════════════════════════════════════
    # 辅助工具
    # ══════════════════════════════════════════
    def _section_title(self, text, color=COL_GOLD):
        mob = Text(text, font=FONT, font_size=34, color=color)
        mob.move_to(UP * 6.3)
        return mob

    def _fade_all(self, *mobs, run_time=0.5):
        self.play(*[FadeOut(m) for m in mobs], run_time=run_time)

    # ══════════════════════════════════════════
    # Scene 0: 开场 Hook
    # ══════════════════════════════════════════
    def scene_0_hook(self):
        title = Text("复数的根", font=FONT, font_size=52, color=COL_GOLD)
        title.move_to(UP * 5.8)

        question_text = Text("虚数居然可以开根？", font=FONT, font_size=30, color=WHITE)
        question_text.move_to(UP * 4.9)

        # 问题：√(-4) = ?
        mystery = MathTex(r"\sqrt{-4} = \;?", font_size=52, color=COL_YELLOW)
        mystery.move_to(UP * 3.7)

        # 答案揭示
        answer = MathTex(r"\sqrt{-4} = \pm 2i", font_size=48, color=COL_GREEN)
        answer.move_to(UP * 2.7)

        hint = Text("→ 答案藏在复数域！", font=FONT, font_size=26, color=COL_PURPLE)
        hint.move_to(UP * 1.9)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(question_text, shift=UP * 0.15), run_time=0.5)
        self.play(Write(mystery), run_time=0.8)
        self.wait(0.6)
        self.play(
            TransformMatchingShapes(mystery.copy(), answer),
            run_time=0.9
        )
        self.play(FadeIn(hint, shift=UP * 0.15), run_time=0.4)
        self.wait(1.0)

        self._fade_all(title, question_text, mystery, answer, hint)

    # ══════════════════════════════════════════
    # Scene 1: 负数平方根
    # ══════════════════════════════════════════
    def scene_1_sqrt_negative(self):
        sc_title = self._section_title("负数的平方根", COL_BLUE)
        self.play(Write(sc_title), run_time=0.5)

        # 从实数类比
        analogy_label = Text("类比实数：", font=FONT, font_size=24, color=COL_GRAY_L)
        analogy_label.move_to(UP * 5.5)
        real_sqrt = MathTex(r"\sqrt{4} = \pm 2", font_size=36, color=WHITE)
        real_sqrt.move_to(UP * 4.8)

        self.play(FadeIn(analogy_label), Write(real_sqrt), run_time=0.6)

        # 延伸到负数
        arrow_down = Text("↓ 扩展到负数", font=FONT, font_size=22, color=COL_GRAY_L)
        arrow_down.move_to(UP * 4.0)
        neg_sqrt = MathTex(r"\sqrt{-4} = \pm 2i", font_size=36, color=COL_BLUE)
        neg_sqrt.move_to(UP * 3.3)
        self.play(FadeIn(arrow_down), Write(neg_sqrt), run_time=0.7)

        # 通项公式
        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=COL_GRAY, stroke_width=1.5)
        divider.move_to(UP * 2.7)
        self.play(Create(divider), run_time=0.3)

        rule_label = Text("一般规律：", font=FONT, font_size=24, color=COL_GRAY_L)
        rule_label.move_to(UP * 2.2)
        rule = MathTex(
            r"\sqrt{-a} = \pm\sqrt{a}\,i \quad (a > 0)",
            font_size=34, color=COL_TEAL
        )
        rule.move_to(UP * 1.5)
        self.play(FadeIn(rule_label), Write(rule), run_time=0.8)

        # 验证动画
        verify_label = Text("验证：", font=FONT, font_size=22, color=COL_GRAY_L)
        verify_label.move_to(UP * 0.6)
        verify = MathTex(
            r"(2i)^2 = 4 \cdot i^2 = 4 \times (-1) = -4 \;\checkmark",
            font_size=28, color=COL_GREEN
        )
        verify.move_to(UP * 0.0)
        self.play(FadeIn(verify_label), Write(verify), run_time=0.8)

        # 负号 i²=-1 高亮
        i2_box = SurroundingRectangle(verify, color=COL_YELLOW, buff=0.1)
        self.play(Create(i2_box), run_time=0.4)
        self.wait(1.5)

        self._fade_all(
            sc_title, analogy_label, real_sqrt, arrow_down, neg_sqrt,
            divider, rule_label, rule, verify_label, verify, i2_box
        )

    # ══════════════════════════════════════════
    # Scene 2: 一般复数平方根（设 w=x+yi）
    # ══════════════════════════════════════════
    def scene_2_general_sqrt(self):
        sc_title = self._section_title("一般复数的平方根", COL_PURPLE)
        self.play(Write(sc_title), run_time=0.5)

        # 例题
        problem_lbl = Text("例：求 w² = 3+4i 的平方根", font=FONT, font_size=26, color=WHITE)
        problem_lbl.move_to(UP * 5.5)
        self.play(FadeIn(problem_lbl), run_time=0.5)

        # 步骤展示
        steps = [
            (Text("设",   font=FONT, font_size=22, color=COL_GRAY_L),
             MathTex(r"w = x + yi \quad (x,y \in \mathbb{R})",     font_size=28)),
            (Text("展开", font=FONT, font_size=22, color=COL_GRAY_L),
             MathTex(r"(x+yi)^2 = x^2 - y^2 + 2xyi",              font_size=28)),
            (Text("实部", font=FONT, font_size=22, color=COL_GRAY_L),
             MathTex(r"x^2 - y^2 = 3",                             font_size=30, color=COL_BLUE)),
            (Text("虚部", font=FONT, font_size=22, color=COL_GRAY_L),
             MathTex(r"2xy = 4 \;\Rightarrow\; xy = 2",            font_size=30, color=COL_BLUE)),
            (Text("解方程组", font=FONT, font_size=22, color=COL_GRAY_L),
             MathTex(r"x = \pm 2,\; y = \pm 1",                    font_size=30, color=COL_GREEN)),
        ]

        y_pos = 4.7
        step_mobs = []
        for lbl_mob, fml_mob in steps:
            lbl_mob.move_to(LEFT * 3.2 + UP * y_pos)
            fml_mob.next_to(lbl_mob, RIGHT, buff=0.25)
            self.play(FadeIn(lbl_mob), Write(fml_mob), run_time=0.55)
            self.wait(0.2)
            step_mobs.extend([lbl_mob, fml_mob])
            y_pos -= 1.05

        # 答案框
        answer_lbl = Text("答：", font=FONT, font_size=24, color=COL_GOLD)
        answer_lbl.move_to(LEFT * 2.8 + UP * (y_pos + 0.2))
        answer = MathTex(r"w = 2+i \quad \text{or} \quad w = -(2+i)",
                         font_size=28, color=COL_GOLD)
        answer.next_to(answer_lbl, RIGHT, buff=0.2)
        answer_box = SurroundingRectangle(VGroup(answer_lbl, answer),
                                          color=COL_GOLD, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(answer_lbl), Write(answer), Create(answer_box), run_time=0.7)

        # 规律：两根互为相反数
        note = Text("规律：两根互为相反数（± 对）", font=FONT, font_size=22, color=COL_TEAL)
        note.move_to(DOWN * 4.5)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.4)
        self.wait(1.5)

        self._fade_all(
            sc_title, problem_lbl, *step_mobs,
            answer_lbl, answer, answer_box, note
        )

    # ══════════════════════════════════════════
    # Scene 3: 立方根 De Moivre 公式
    # ══════════════════════════════════════════
    def scene_3_cube_root_formula(self):
        sc_title = self._section_title("复数的立方根", COL_RED)
        self.play(Write(sc_title), run_time=0.5)

        # 三角形式前置
        tri_lbl = Text("三角形式：", font=FONT, font_size=24, color=COL_GRAY_L)
        tri_lbl.move_to(UP * 5.5)
        tri_form = MathTex(
            r"z = r(\cos\theta + i\sin\theta)",
            font_size=32, color=WHITE
        )
        tri_form.move_to(UP * 4.8)
        self.play(FadeIn(tri_lbl), Write(tri_form), run_time=0.7)

        # 立方根公式
        cube_lbl = Text("立方根公式（棣莫弗）：", font=FONT, font_size=24, color=COL_GRAY_L)
        cube_lbl.move_to(UP * 3.8)
        cube_form = MathTex(
            r"w = \sqrt[3]{r}\left[\cos\frac{\theta+2k\pi}{3}"
            r"+i\sin\frac{\theta+2k\pi}{3}\right]",
            font_size=28, color=COL_RED
        )
        cube_form.move_to(UP * 3.0)
        self.play(FadeIn(cube_lbl), Write(cube_form), run_time=1.0)

        k_text = MathTex(r"k = 0,\; 1,\; 2", font_size=34, color=COL_YELLOW)
        k_text.move_to(UP * 2.0)
        self.play(Write(k_text), run_time=0.5)

        # 关键：共有3个立方根
        three_roots_text = Text("→ 任意复数有 3 个立方根", font=FONT, font_size=26, color=COL_GREEN)
        three_roots_text.move_to(UP * 1.1)
        self.play(FadeIn(three_roots_text, shift=UP * 0.1), run_time=0.5)

        # 在复平面中等间隔分布
        dist_text = Text("在复平面中等间隔 120° 分布", font=FONT, font_size=24, color=COL_TEAL)
        dist_text.move_to(UP * 0.3)
        self.play(FadeIn(dist_text, shift=UP * 0.1), run_time=0.4)

        self.wait(1.5)
        self._fade_all(
            sc_title, tri_lbl, tri_form,
            cube_lbl, cube_form, k_text,
            three_roots_text, dist_text
        )

    # ══════════════════════════════════════════
    # Scene 4: 1的三个立方根 — 复平面可视化
    # ══════════════════════════════════════════
    def scene_4_cube_roots_visual(self):
        sc_title = self._section_title("1 的三个立方根", COL_GOLD)
        self.play(Write(sc_title), run_time=0.5)

        # 方程标注
        eq_label = MathTex(r"w^3 = 1 \;\Rightarrow\; w = \sqrt[3]{1}",
                           font_size=30, color=WHITE)
        eq_label.move_to(UP * 5.6)
        self.play(Write(eq_label), run_time=0.6)

        # ── 复平面轴 ──────────────────────────
        plane_center = PLANE_CENTER   # (0, 1.5, 0)

        x_axis = Arrow(
            plane_center + LEFT * 3.0,
            plane_center + RIGHT * 3.0,
            buff=0, color=COL_GRAY, stroke_width=2,
            tip_length=0.18
        )
        y_axis = Arrow(
            plane_center + DOWN * 2.8,
            plane_center + UP * 2.8,
            buff=0, color=COL_GRAY, stroke_width=2,
            tip_length=0.18
        )
        x_lbl = Text("实轴", font=FONT, font_size=18, color=COL_GRAY)
        x_lbl.next_to(x_axis.get_end(), RIGHT, buff=0.1)
        y_lbl = Text("虚轴", font=FONT, font_size=18, color=COL_GRAY)
        y_lbl.next_to(y_axis.get_end(), UP, buff=0.1)

        self.play(Create(x_axis), Create(y_axis), run_time=0.5)
        self.play(FadeIn(x_lbl), FadeIn(y_lbl), run_time=0.3)

        # ── 单位圆 ────────────────────────────
        unit_circle = Circle(
            radius=UNIT_R, color=COL_GRAY_L,
            stroke_width=1.5, stroke_opacity=0.6
        )
        unit_circle.move_to(plane_center)
        self.play(Create(unit_circle), run_time=0.8)

        # ── 三个根的坐标（经 verify_roots.py 验证）────
        #  k=0: (0, 1.5)     → 标签: 1
        #  k=1: (-1, 3.232)  → 标签: ω
        #  k=2: (-1, -0.232) → 标签: ω²
        P0 = cube_root_point(0)
        P1 = cube_root_point(1)
        P2 = cube_root_point(2)

        ROOT_COLORS = [COL_GREEN, COL_BLUE, COL_RED]
        root_pts    = [P0, P1, P2]
        root_labels_tex = [
            MathTex(r"1",       font_size=28, color=COL_GREEN),
            MathTex(r"\omega",  font_size=28, color=COL_BLUE),
            MathTex(r"\omega^2",font_size=28, color=COL_RED),
        ]
        label_dirs = [RIGHT * 0.45 + UP * 0.0,
                      LEFT  * 0.45 + UP * 0.25,
                      LEFT  * 0.45 + DOWN * 0.25]

        dots   = []
        vecs   = []
        labels = []

        for pt, col, lbl_tex, ldir in zip(
                root_pts, ROOT_COLORS, root_labels_tex, label_dirs):
            vec = Arrow(
                plane_center, pt,
                buff=0, color=col,
                stroke_width=3, tip_length=0.20
            )
            dot = Dot(pt, color=col, radius=0.12)
            lbl_tex.move_to(pt + ldir)
            vecs.append(vec)
            dots.append(dot)
            labels.append(lbl_tex)

        # 逐一展示三个根
        for vec, dot, lbl in zip(vecs, dots, labels):
            self.play(GrowArrow(vec), run_time=0.6)
            self.play(FadeIn(dot, scale=0.5), Write(lbl), run_time=0.4)
            self.wait(0.2)

        # ── 120° 弧（全部 CCW，other_angle=False，经验证）──────
        # 使用 Arc 对象直接指定起始角和跨度，在 plane_center 处
        arc_params = [
            (0,                  2*np.pi/3, COL_GREEN),   # 0→120°
            (2*np.pi/3,          2*np.pi/3, COL_BLUE),    # 120→240°
            (4*np.pi/3,          2*np.pi/3, COL_RED),     # 240→360°
        ]
        arc_mobs = []
        for start_a, span_a, col in arc_params:
            arc = Arc(
                radius=UNIT_R * 0.55,
                start_angle=start_a,
                angle=span_a,
                color=col,
                stroke_width=2.5
            )
            arc.move_to(plane_center)
            arc_mobs.append(arc)

        arc_label_mobs = []
        for i, arc in enumerate(arc_mobs):
            self.play(Create(arc), run_time=0.5)
            mid_angle = arc_params[i][0] + arc_params[i][1] / 2
            mid_pt = plane_center + np.array([
                UNIT_R * 0.55 * 1.45 * np.cos(mid_angle),
                UNIT_R * 0.55 * 1.45 * np.sin(mid_angle),
                0.0
            ])
            deg_lbl = MathTex(r"120^\circ", font_size=22, color=COL_YELLOW)
            deg_lbl.move_to(mid_pt)
            arc_label_mobs.append(deg_lbl)
            self.play(Write(deg_lbl), run_time=0.35)

        # 等间隔说明
        equal_text = Text("等间隔 120° 分布在单位圆上！",
                          font=FONT, font_size=24, color=COL_YELLOW)
        equal_text.move_to(DOWN * 3.8)
        self.play(FadeIn(equal_text, shift=UP * 0.1), run_time=0.5)
        self.wait(1.8)

        self._fade_all(
            sc_title, eq_label,
            x_axis, y_axis, x_lbl, y_lbl,
            unit_circle,
            *vecs, *dots, *labels,
            *arc_mobs, *arc_label_mobs,
            equal_text
        )

    # ══════════════════════════════════════════
    # Scene 5: ω 的重要性质
    # ══════════════════════════════════════════
    def scene_5_omega_properties(self):
        sc_title = self._section_title("ω 的重要性质", COL_TEAL)
        self.play(Write(sc_title), run_time=0.5)

        omega_def_lbl = Text("其中 ω 定义为：", font=FONT, font_size=24, color=COL_GRAY_L)
        omega_def_lbl.move_to(UP * 5.5)
        omega_def = MathTex(
            r"\omega = -\frac{1}{2}+\frac{\sqrt{3}}{2}i",
            font_size=34, color=COL_BLUE
        )
        omega_def.move_to(UP * 4.7)
        self.play(FadeIn(omega_def_lbl), Write(omega_def), run_time=0.7)

        # 三条性质
        props = [
            (r"\omega^3 = 1",           COL_GREEN,  UP * 3.7, "3次幂等于1"),
            (r"1 + \omega + \omega^2 = 0", COL_YELLOW, UP * 2.8, "三根之和为零"),
            (r"\omega^2 = \overline{\omega}", COL_RED, UP * 1.9, "ω²是ω的共轭"),
        ]
        prop_mobs = []
        note_mobs = []
        for tex, col, pos, note_str in props:
            fml = MathTex(tex, font_size=36, color=col)
            fml.move_to(pos)
            note = Text(note_str, font=FONT, font_size=20, color=COL_GRAY_L)
            note.next_to(fml, RIGHT, buff=0.4)
            self.play(Write(fml), run_time=0.6)
            self.play(FadeIn(note), run_time=0.3)
            self.wait(0.4)
            prop_mobs.append(fml)
            note_mobs.append(note)

        # 几何直觉
        geo_text = Text(
            "几何直觉：正三角形的三个顶点",
            font=FONT, font_size=22, color=COL_TEAL
        )
        geo_text.move_to(UP * 0.8)
        self.play(FadeIn(geo_text, shift=UP * 0.1), run_time=0.4)

        # 小型示意三角形
        tri_center = DOWN * 0.3
        tri_pts = [
            tri_center + np.array([0.8, 0, 0]),
            tri_center + np.array([-0.4, 0.693, 0]),
            tri_center + np.array([-0.4, -0.693, 0]),
        ]
        tri_poly = Polygon(*tri_pts, color=COL_GOLD, stroke_width=2.5)
        tri_dots = VGroup(*[Dot(p, radius=0.08, color=COL_GOLD) for p in tri_pts])
        self.play(Create(tri_poly), FadeIn(tri_dots), run_time=0.7)
        self.wait(1.5)

        self._fade_all(
            sc_title, omega_def_lbl, omega_def,
            *prop_mobs, *note_mobs,
            geo_text, tri_poly, tri_dots
        )

    # ══════════════════════════════════════════
    # Scene 6: 片尾
    # ══════════════════════════════════════════
    def scene_6_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE
        ).move_to(UP * 2.5)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=COL_GRAY_L
        ).move_to(UP * 1.7)
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=COL_YELLOW
        ).move_to(UP * 0.7)

        # ✅ 修复：summary_items 全部拆成 VGroup(MathTex, Text)，不再传 Unicode 进 MathTex
        summary_items = [
            (r"\sqrt{-a} = \pm\sqrt{a}\,i",  "负数的平方根", COL_BLUE),
            (r"w = x + yi",                   "一般复数平方根", COL_PURPLE),
            (r"\omega,\; \omega^2,\; 1",      "1的三个立方根", COL_RED),
        ]
        rows = VGroup()
        for tex_str, cn_str, col in summary_items:
            t1 = MathTex(tex_str, font_size=24, color=col)
            t2 = Text(cn_str, font=FONT, font_size=18, color=col)
            row = VGroup(t1, t2).arrange(RIGHT, buff=0.35)
            rows.add(row)
        rows.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        rows.move_to(DOWN * 2.0)

        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow_text, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(rows, shift=UP * 0.2), run_time=0.7)

        deco_circle = Circle(
            radius=0.6, color=COL_GOLD,
            stroke_width=2, fill_opacity=0
        ).move_to(DOWN * 4.5)
        deco_pts = [
            deco_circle.get_center() + 0.6 * np.array([np.cos(2*np.pi*k/3),
                                                        np.sin(2*np.pi*k/3), 0])
            for k in range(3)
        ]
        deco_dots = VGroup(*[
            Dot(p, radius=0.07, color=c)
            for p, c in zip(deco_pts, [COL_GREEN, COL_BLUE, COL_RED])
        ])
        deco_poly = Polygon(*deco_pts, color=COL_GOLD, stroke_width=1.5, fill_opacity=0.1)

        self.play(Create(deco_circle), Create(deco_poly), FadeIn(deco_dots), run_time=0.7)
        self.wait(1.8)

        self._fade_all(
            self.author_mob, author_id, follow_text,
            rows, deco_circle, deco_poly, deco_dots
        )