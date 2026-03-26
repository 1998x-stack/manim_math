"""
004_分数的基本性质.py — 分数的基本性质 教学动画

知识点: a/b = (a×c)/(b×c) = (a÷c)/(b÷c)，其中 c≠0
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 引入: 1/2 = 2/4 = 3/6，分数大小相同但写法不同
  2. 视觉展示: 用矩形展示 1/2, 2/4, 3/6 涂色部分相等
  3. 性质: 分子分母同乘或同除一个不为0的数，分数大小不变
  4. 公式: a/b = (a×c)/(b×c) = (a÷c)/(b÷c), c≠0
  5. 例题: 把 2/3 变成分母是12的分数 → 8/12
  6. 应用: 约分和通分的基础
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
BG_COLOR = "#1a1a2e"
COLOR_FRAC = "#3b82f6"       # 蓝色分数/涂色区
COLOR_FRAC2 = "#22c55e"      # 绿色第二分数
COLOR_FRAC3 = "#a78bfa"      # 紫色第三分数
COLOR_GRID = "#94a3b8"       # 灰色网格线
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_ACCENT = "#ef4444"     # 红色强调
COLOR_FORMULA = "#f59e0b"    # 橙色公式
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class FractionPropertyLesson(Scene):
    """
    分数的基本性质教学动画
    场景顺序:
      1. 开场钩子: 一块蛋糕切不同刀数，得到的大小一样吗？
      2. 视觉等价: 用矩形展示 1/2 = 2/4 = 3/6
      3. 发现规律: 分子分母的变化关系
      4. 性质公式: 分数的基本性质 + 公式
      5. 例题应用: 2/3 → ?/12
      6. 总结: 约分通分的基础
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_visual_equivalence()
        self.scene_3_discover_pattern()
        self.scene_4_property_formula()
        self.scene_5_example()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 辅助: 创建带网格的分数矩形
    # ------------------------------------------------------------------

    def _fraction_rect(self, total_parts, shaded_parts, color,
                       width=3.0, height=1.6):
        """
        创建一个矩形，分成 total_parts 等份，涂色 shaded_parts 份。
        返回 VGroup(outline, grid_lines, shaded_region)
        """
        outline = Rectangle(
            width=width, height=height,
            stroke_color=WHITE, stroke_width=2.5,
            fill_opacity=0
        )

        part_w = width / total_parts
        grid_lines = VGroup()
        for i in range(1, total_parts):
            line = Line(
                outline.get_left() + RIGHT * part_w * i + UP * height / 2,
                outline.get_left() + RIGHT * part_w * i + DOWN * height / 2,
                stroke_color=COLOR_GRID, stroke_width=1.5
            )
            grid_lines.add(line)

        shaded = Rectangle(
            width=part_w * shaded_parts, height=height,
            stroke_width=0,
            fill_color=color, fill_opacity=0.45
        )
        shaded.align_to(outline, LEFT)

        return VGroup(outline, grid_lines, shaded)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '这三个分数，大小一样吗？'"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "这三个分数", font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "大小一样吗？", font=FONT, font_size=50,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 展示三个分数
        f1 = MathTex(r"\frac{1}{2}", font_size=72, color=COLOR_FRAC)
        f2 = MathTex(r"\frac{2}{4}", font_size=72, color=COLOR_FRAC2)
        f3 = MathTex(r"\frac{3}{6}", font_size=72, color=COLOR_FRAC3)
        fracs = VGroup(f1, f2, f3).arrange(RIGHT, buff=1.2).move_to(UP * 1.5)

        for f in [f1, f2, f3]:
            self.play(FadeIn(f, scale=0.5), run_time=0.5)

        # 问号
        q = Text("= ?", font=FONT, font_size=68, color=COLOR_HL, weight=BOLD)
        q.move_to(DOWN * 0.5)
        self.play(FadeIn(q, scale=0.4), run_time=0.5)
        self.wait(1.2)

        # 清理钩子
        self.play(FadeOut(VGroup(hook1, hook2, fracs, q)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 2: 视觉等价 — 矩形涂色展示
    # ------------------------------------------------------------------

    def scene_2_visual_equivalence(self):
        """用矩形展示 1/2 = 2/4 = 3/6，涂色部分相等"""

        title = Text(
            "用图形来比较", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        rect_w = 5.0
        rect_h = 1.2

        # ----- 1/2 -----
        r1 = self._fraction_rect(2, 1, COLOR_FRAC, width=rect_w, height=rect_h)
        r1.move_to(UP * 3.0)
        lbl1 = MathTex(r"\frac{1}{2}", font_size=52, color=COLOR_FRAC)
        lbl1.next_to(r1, LEFT, buff=0.5)

        self.play(Create(r1[0]), run_time=0.4)
        self.play(Create(r1[1]), run_time=0.3)
        self.play(FadeIn(r1[2]), FadeIn(lbl1), run_time=0.5)
        self.wait(0.3)

        # ----- 2/4 -----
        r2 = self._fraction_rect(4, 2, COLOR_FRAC2, width=rect_w, height=rect_h)
        r2.move_to(UP * 0.8)
        lbl2 = MathTex(r"\frac{2}{4}", font_size=52, color=COLOR_FRAC2)
        lbl2.next_to(r2, LEFT, buff=0.5)

        self.play(Create(r2[0]), run_time=0.4)
        self.play(Create(r2[1]), run_time=0.3)
        self.play(FadeIn(r2[2]), FadeIn(lbl2), run_time=0.5)
        self.wait(0.3)

        # ----- 3/6 -----
        r3 = self._fraction_rect(6, 3, COLOR_FRAC3, width=rect_w, height=rect_h)
        r3.move_to(DOWN * 1.4)
        lbl3 = MathTex(r"\frac{3}{6}", font_size=52, color=COLOR_FRAC3)
        lbl3.next_to(r3, LEFT, buff=0.5)

        self.play(Create(r3[0]), run_time=0.4)
        self.play(Create(r3[1]), run_time=0.3)
        self.play(FadeIn(r3[2]), FadeIn(lbl3), run_time=0.5)
        self.wait(0.5)

        # 强调涂色面积相同
        note = Text(
            "涂色部分大小完全相同！",
            font=FONT, font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(note, shift=UP * 0.3), run_time=0.5)

        # 等号连接
        eq_tex = MathTex(
            r"\frac{1}{2}", r"=", r"\frac{2}{4}", r"=", r"\frac{3}{6}",
            font_size=52, color=WHITE
        ).move_to(DOWN * 5.0)
        eq_tex[0].set_color(COLOR_FRAC)
        eq_tex[2].set_color(COLOR_FRAC2)
        eq_tex[4].set_color(COLOR_FRAC3)

        self.play(Write(eq_tex), run_time=0.8)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, r1, lbl1, r2, lbl2, r3, lbl3, note, eq_tex
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 发现规律 — 分子分母的变化
    # ------------------------------------------------------------------

    def scene_3_discover_pattern(self):
        """观察 1/2 → 2/4 → 3/6，发现分子分母同乘关系"""

        title = Text(
            "发现规律", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 三个分数排列
        f1 = MathTex(r"\frac{1}{2}", font_size=68, color=WHITE)
        arrow1 = MathTex(r"\longrightarrow", font_size=48, color=COLOR_HL)
        f2 = MathTex(r"\frac{2}{4}", font_size=68, color=WHITE)
        arrow2 = MathTex(r"\longrightarrow", font_size=48, color=COLOR_HL)
        f3 = MathTex(r"\frac{3}{6}", font_size=68, color=WHITE)

        chain = VGroup(f1, arrow1, f2, arrow2, f3).arrange(RIGHT, buff=0.5)
        chain.move_to(UP * 3.0)

        self.play(FadeIn(chain), run_time=0.6)
        self.wait(0.5)

        # 标注: 1/2 → 2/4 分子分母同乘2
        multiply_top1 = MathTex(r"\times 2", font_size=32, color=COLOR_ACCENT)
        multiply_top1.next_to(f1, UP, buff=0.6)
        arr_top1 = CurvedArrow(
            f1.get_top() + UP * 0.15,
            f2.get_top() + UP * 0.15,
            color=COLOR_ACCENT, stroke_width=2.5, angle=-0.5
        )
        multiply_bot1 = MathTex(r"\times 2", font_size=32, color=COLOR_ACCENT)
        multiply_bot1.next_to(f1, DOWN, buff=0.6)
        arr_bot1 = CurvedArrow(
            f1.get_bottom() + DOWN * 0.15,
            f2.get_bottom() + DOWN * 0.15,
            color=COLOR_ACCENT, stroke_width=2.5, angle=0.5
        )

        note1_top = Text(
            "分子 ×2", font=FONT, font_size=24, color=COLOR_ACCENT
        ).next_to(arr_top1, UP, buff=0.1)
        note1_bot = Text(
            "分母 ×2", font=FONT, font_size=24, color=COLOR_ACCENT
        ).next_to(arr_bot1, DOWN, buff=0.1)

        self.play(
            Create(arr_top1), FadeIn(note1_top),
            Create(arr_bot1), FadeIn(note1_bot),
            run_time=0.8
        )
        self.wait(0.8)

        # 标注: 2/4 → 3/6 不是乘关系，换一种方式
        # 其实 1/2 → 3/6 是 ×3
        # 清除第一组标注
        self.play(
            FadeOut(VGroup(arr_top1, note1_top, arr_bot1, note1_bot)),
            run_time=0.3
        )

        # 改为展示 1/2 → 3/6 分子分母同乘3
        arr_top2 = CurvedArrow(
            f1.get_top() + UP * 0.15,
            f3.get_top() + UP * 0.15,
            color=COLOR_FRAC2, stroke_width=2.5, angle=-0.4
        )
        arr_bot2 = CurvedArrow(
            f1.get_bottom() + DOWN * 0.15,
            f3.get_bottom() + DOWN * 0.15,
            color=COLOR_FRAC2, stroke_width=2.5, angle=0.4
        )
        note2_top = Text(
            "分子 ×3", font=FONT, font_size=24, color=COLOR_FRAC2
        ).next_to(arr_top2, UP, buff=0.1)
        note2_bot = Text(
            "分母 ×3", font=FONT, font_size=24, color=COLOR_FRAC2
        ).next_to(arr_bot2, DOWN, buff=0.1)

        self.play(
            Create(arr_top2), FadeIn(note2_top),
            Create(arr_bot2), FadeIn(note2_bot),
            run_time=0.8
        )
        self.wait(0.8)

        # 关键发现
        key_text = Text(
            "分子和分母同时乘相同的数",
            font=FONT, font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 1.5)
        key_text2 = Text(
            "分数的大小不变！",
            font=FONT, font_size=34, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 2.5)

        self.play(Write(key_text), run_time=0.6)
        self.play(Write(key_text2), run_time=0.6)
        self.wait(1.5)

        # 那反过来呢？ 6/6 → 1/2 除以相同的数也可以
        reverse = Text(
            "反过来，同时除以相同的数也可以！",
            font=FONT, font_size=26, color=COLOR_FRAC3
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(reverse, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, chain,
                arr_top2, note2_top, arr_bot2, note2_bot,
                key_text, key_text2, reverse
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 分数基本性质公式
    # ------------------------------------------------------------------

    def scene_4_property_formula(self):
        """展示分数基本性质的完整公式"""

        title = Text(
            "分数的基本性质", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 性质文字
        prop_line1 = Text(
            "分数的分子和分母", font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 3.8)
        prop_line2_a = Text(
            "同时乘", font=FONT, font_size=30, color=COLOR_ACCENT
        )
        prop_line2_b = Text(
            "（或", font=FONT, font_size=30, color=WHITE
        )
        prop_line2_c = Text(
            "同时除以", font=FONT, font_size=30, color=COLOR_FRAC2
        )
        prop_line2_d = Text(
            "）", font=FONT, font_size=30, color=WHITE
        )
        prop_line2 = VGroup(
            prop_line2_a, prop_line2_b, prop_line2_c, prop_line2_d
        ).arrange(RIGHT, buff=0.05).move_to(UP * 2.9)

        prop_line3 = Text(
            "一个不为0的数，分数大小不变",
            font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 2.0)

        self.play(Write(prop_line1), run_time=0.6)
        self.play(Write(prop_line2), run_time=0.7)
        self.play(Write(prop_line3), run_time=0.6)
        self.wait(0.8)

        # 公式框
        formula_box = RoundedRectangle(
            width=7.8, height=3.2,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 1.0)

        self.play(FadeIn(formula_box), run_time=0.3)

        # 核心公式
        formula = MathTex(
            r"\frac{a}{b}",
            r"=",
            r"\frac{a \times c}{b \times c}",
            r"=",
            r"\frac{a \div c}{b \div c}",
            font_size=46
        ).move_to(DOWN * 0.6)
        formula[0].set_color(WHITE)
        formula[2].set_color(COLOR_ACCENT)
        formula[4].set_color(COLOR_FRAC2)

        self.play(Write(formula), run_time=1.2)
        self.wait(0.5)

        # c ≠ 0 条件
        condition = MathTex(
            r"(c \neq 0)",
            font_size=38, color=COLOR_FORMULA
        ).move_to(DOWN * 1.8)
        self.play(FadeIn(condition, shift=UP * 0.2), run_time=0.5)

        # 强调 c ≠ 0
        cond_note = Text(
            "注意: c 不能为 0 !",
            font=FONT, font_size=24, color=COLOR_ACCENT
        ).move_to(DOWN * 2.6)
        self.play(FadeIn(cond_note, shift=UP * 0.2), run_time=0.4)

        # 闪烁强调公式
        self.play(
            Indicate(formula, scale_factor=1.05, color=COLOR_HL),
            run_time=0.6
        )
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, prop_line1, prop_line2, prop_line3,
                formula_box, formula, condition, cond_note
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 例题应用
    # ------------------------------------------------------------------

    def scene_5_example(self):
        """例题: 把 2/3 变成分母为 12 的分数"""

        title = Text(
            "例题", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 题目
        q_line1 = Text(
            "把", font=FONT, font_size=32, color=WHITE
        )
        q_frac = MathTex(r"\frac{2}{3}", font_size=52, color=COLOR_FRAC)
        q_line2 = Text(
            "变成分母是 12 的分数", font=FONT, font_size=32, color=WHITE
        )
        question = VGroup(q_line1, q_frac, q_line2).arrange(
            RIGHT, buff=0.2
        ).move_to(UP * 3.8)

        self.play(Write(question), run_time=0.8)
        self.wait(0.8)

        # 思路: 分母 3 → 12，乘了几？
        think1 = Text(
            "思路：分母 3 → 12", font=FONT, font_size=28, color=COLOR_FRAC2
        ).move_to(UP * 2.2)
        self.play(Write(think1), run_time=0.5)

        think2_a = Text(
            "3 × ", font=FONT, font_size=28, color=WHITE
        )
        think2_b = Text(
            "?", font=FONT, font_size=34, color=COLOR_HL, weight=BOLD
        )
        think2_c = Text(
            " = 12", font=FONT, font_size=28, color=WHITE
        )
        think2 = VGroup(think2_a, think2_b, think2_c).arrange(
            RIGHT, buff=0.08
        ).move_to(UP * 1.2)
        self.play(FadeIn(think2), run_time=0.4)
        self.wait(0.5)

        # 答案: ×4
        answer_mult = Text(
            "3 × 4 = 12，所以 c = 4",
            font=FONT, font_size=28, color=COLOR_HL
        ).move_to(UP * 0.2)
        self.play(
            FadeOut(think2),
            FadeIn(answer_mult, shift=UP * 0.2),
            run_time=0.5
        )
        self.wait(0.5)

        # 分子分母同时 ×4
        step_label = Text(
            "分子和分母同时 ×4",
            font=FONT, font_size=28, color=COLOR_ACCENT
        ).move_to(DOWN * 0.8)
        self.play(Write(step_label), run_time=0.5)

        # 计算过程
        calc = MathTex(
            r"\frac{2}{3}",
            r"=",
            r"\frac{2 \times 4}{3 \times 4}",
            r"=",
            r"\frac{8}{12}",
            font_size=50
        ).move_to(DOWN * 2.3)
        calc[0].set_color(COLOR_FRAC)
        calc[2].set_color(COLOR_ACCENT)
        calc[4].set_color(COLOR_HL)

        self.play(Write(calc[0:2]), run_time=0.4)
        self.play(Write(calc[2:4]), run_time=0.6)
        self.play(Write(calc[4]), run_time=0.5)

        # 高亮答案
        ans_box = SurroundingRectangle(
            calc[4], color=COLOR_HL, stroke_width=3, buff=0.15,
            corner_radius=0.1
        )
        self.play(Create(ans_box), run_time=0.4)

        ans_text = Text(
            "答案:", font=FONT, font_size=28, color=WHITE
        )
        ans_val = MathTex(r"\frac{2}{3} = \frac{8}{12}",
                          font_size=44, color=COLOR_HL)
        ans_group = VGroup(ans_text, ans_val).arrange(
            RIGHT, buff=0.2
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(ans_group, shift=UP * 0.3), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, question, think1, answer_mult,
                step_label, calc, ans_box, ans_group
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 总结 — 约分通分的基础
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        """总结分数基本性质及其应用"""

        title = Text(
            "总结", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 公式框
        formula_box = RoundedRectangle(
            width=7.8, height=2.8,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 2.8)

        formula_title = Text(
            "分数的基本性质", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 3.8)

        formula = MathTex(
            r"\frac{a}{b} = \frac{a \times c}{b \times c}"
            r"= \frac{a \div c}{b \div c}",
            font_size=40, color=COLOR_HL
        ).move_to(UP * 2.8)

        cond = MathTex(r"(c \neq 0)", font_size=34, color=COLOR_FORMULA)
        cond.move_to(UP * 1.8)

        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(formula_title), run_time=0.4)
        self.play(Write(formula), run_time=0.9)
        self.play(FadeIn(cond), run_time=0.3)
        self.wait(0.5)

        # 应用方向
        app_title = Text(
            "这个性质是", font=FONT, font_size=30, color=WHITE
        ).move_to(DOWN * 0.2)
        self.play(Write(app_title), run_time=0.4)

        # 约分
        app1_icon = MathTex(
            r"\frac{4}{8} \to \frac{1}{2}",
            font_size=40, color=COLOR_FRAC2
        ).move_to(DOWN * 1.8 + LEFT * 2.0)
        app1_label = Text(
            "约分", font=FONT, font_size=32, color=COLOR_FRAC2, weight=BOLD
        ).next_to(app1_icon, DOWN, buff=0.3)
        app1_desc = Text(
            "（同除）", font=FONT, font_size=22, color=COLOR_FRAC2
        ).next_to(app1_label, DOWN, buff=0.1)

        # 通分
        app2_icon = MathTex(
            r"\frac{1}{3} \to \frac{4}{12}",
            font_size=40, color=COLOR_FRAC3
        ).move_to(DOWN * 1.8 + RIGHT * 2.0)
        app2_label = Text(
            "通分", font=FONT, font_size=32, color=COLOR_FRAC3, weight=BOLD
        ).next_to(app2_icon, DOWN, buff=0.3)
        app2_desc = Text(
            "（同乘）", font=FONT, font_size=22, color=COLOR_FRAC3
        ).next_to(app2_label, DOWN, buff=0.1)

        # 中间 "的基础"
        basis_text = Text(
            "的基础！", font=FONT, font_size=30, color=WHITE
        ).move_to(DOWN * 4.5)

        # 约分和通分标签
        yf_text = Text(
            "约分", font=FONT, font_size=34, color=COLOR_FRAC2, weight=BOLD
        )
        tf_text = Text(
            "和", font=FONT, font_size=30, color=WHITE
        )
        tf_text2 = Text(
            "通分", font=FONT, font_size=34, color=COLOR_FRAC3, weight=BOLD
        )
        basis_line = VGroup(yf_text, tf_text, tf_text2).arrange(
            RIGHT, buff=0.15
        ).move_to(DOWN * 3.8)

        self.play(
            FadeIn(app1_icon, shift=UP * 0.2),
            FadeIn(app2_icon, shift=UP * 0.2),
            run_time=0.6
        )
        self.play(
            FadeIn(app1_label), FadeIn(app1_desc),
            FadeIn(app2_label), FadeIn(app2_desc),
            run_time=0.5
        )
        self.play(
            FadeIn(basis_line, shift=UP * 0.2),
            FadeIn(basis_text, shift=UP * 0.2),
            run_time=0.6
        )
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, formula_box, formula_title, formula, cond,
                app_title,
                app1_icon, app1_label, app1_desc,
                app2_icon, app2_label, app2_desc,
                basis_line, basis_text
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        """作者信息放大 + 关注提示"""

        # 作者名放大居中
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_A
        ).move_to(UP * 1.0)

        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰: 6个小分数围绕
        deco_colors = [
            COLOR_FRAC, COLOR_FRAC2, COLOR_FRAC3,
            COLOR_ACCENT, COLOR_FORMULA, COLOR_HL
        ]
        deco_fracs = [
            r"\frac{1}{2}", r"\frac{2}{4}", r"\frac{3}{6}",
            r"\frac{2}{3}", r"\frac{8}{12}", r"\frac{a}{b}"
        ]
        mini = VGroup(*[
            MathTex(f, font_size=30, color=c).move_to(
                DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.5,
                    np.sin(i * PI / 3) * 0.8,
                    0.0
                ])
            )
            for i, (f, c) in enumerate(zip(deco_fracs, deco_colors))
        ])
        self.play(*[FadeIn(t, scale=0.3) for t in mini], run_time=0.5)
        self.play(
            Rotate(mini, angle=2 * PI / 3, run_time=1.2, rate_func=smooth)
        )
        self.wait(0.8)

        # 全部淡出
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览: manim -pql 004_分数的基本性质.py FractionPropertyLesson
#   高质量:   manim -qh  004_分数的基本性质.py FractionPropertyLesson
#   4K:       manim -qk  004_分数的基本性质.py FractionPropertyLesson
# ======================================================================
