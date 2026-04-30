"""
005_约分.py — 约分 教学动画

知识点: 把分数的分子和分母同时除以公因数，分数值不变，直到最简分数
年级: 五年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子: 12/18 能化简吗？
  2. 约分定义: 分子分母同时除以公因数
  3. 方法1 逐步约分: 12/18 ÷2→ 6/9 ÷3→ 2/3
  4. 方法2 一步到位: 12/18 ÷6→ 2/3 (用最大公因数)
  5. 最简分数: 分子分母只有公因数1
  6. 约分依据: 分数的基本性质
  7. 练习: 判断哪些是最简分数
  8. 片尾
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
COLOR_FRAC = "#3b82f6"       # 蓝色主分数
COLOR_STEP = "#22c55e"       # 绿色步骤
COLOR_GCD = "#a78bfa"        # 紫色最大公因数
COLOR_SIMPLE = "#10b981"     # 翠绿最简分数
COLOR_HL = "#fbbf24"         # 黄色高亮
COLOR_ACCENT = "#ef4444"     # 红色强调
COLOR_ORANGE = "#f59e0b"     # 橙色
COLOR_AUTHOR = "#6b7280"     # 灰色作者信息
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class ReducingFractionsLesson(Scene):
    """
    约分教学动画
    场景顺序:
      1. 开场钩子: 12/18 能化简吗？
      2. 约分定义: 分子分母同时除以公因数
      3. 方法1: 逐步约分 12/18 → 6/9 → 2/3
      4. 方法2: 用最大公因数一步到位
      5. 最简分数定义 + 约分依据
      6. 练习: 判断最简分数
      7. 总结公式框
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_step_by_step()
        self.scene_4_gcd_method()
        self.scene_5_simplest_and_basis()
        self.scene_6_practice()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '12/18 能化简吗？'"""

        # 作者信息 (顶部，贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "这个分数", font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "能化简吗？", font=FONT, font_size=50,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 主分数 12/18
        self.main_frac = MathTex(
            r"\frac{12}{18}",
            font_size=120, color=COLOR_FRAC
        ).move_to(UP * 1.5)
        self.play(FadeIn(self.main_frac, scale=0.4), run_time=0.8)

        # 问号
        q = Text("?", font=FONT, font_size=80, color=COLOR_HL, weight=BOLD)
        q.move_to(DOWN * 1.0)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(1.0)

        # 清理钩子
        self.play(FadeOut(VGroup(hook1, hook2, q, self.main_frac)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 2: 约分定义
    # ------------------------------------------------------------------

    def scene_2_definition(self):
        """约分定义: 分子分母同时除以公因数，分数值不变"""

        title = Text(
            "什么是约分？", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 定义框
        def_box = RoundedRectangle(
            width=7.8, height=3.6,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_FRAC, stroke_width=3
        ).move_to(UP * 2.2)
        self.play(FadeIn(def_box), run_time=0.3)

        # 定义文字逐行
        d1 = Text(
            "把分数的分子和分母", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 3.2)
        d2_a = Text(
            "同时除以公因数", font=FONT, font_size=30,
            color=COLOR_ACCENT, weight=BOLD
        )
        d2 = d2_a.move_to(UP * 2.3)
        d3 = Text(
            "分数的大小不变", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 1.4)

        self.play(Write(d1), run_time=0.6)
        self.play(Write(d2), run_time=0.6)
        self.play(Write(d3), run_time=0.5)
        self.wait(0.5)

        # 这个过程叫做——约分
        label = Text(
            "这个过程叫做——约分",
            font=FONT, font_size=34, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(label, shift=UP * 0.3), run_time=0.6)

        # 示意: 12/18 → 分子分母都除以公因数
        demo = MathTex(
            r"\frac{12}{18}",
            font_size=72, color=COLOR_FRAC
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(demo, scale=0.6), run_time=0.5)

        # 找公因数提示
        cf_text = Text(
            "12 和 18 的公因数: 1, 2, 3, 6",
            font=FONT, font_size=24, color=COLOR_GCD
        ).move_to(DOWN * 3.8)
        self.play(Write(cf_text), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, def_box, d1, d2, d3,
                label, demo, cf_text
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 方法1 — 逐步约分
    # ------------------------------------------------------------------

    def scene_3_step_by_step(self):
        """逐步约分: 12/18 ÷2→ 6/9 ÷3→ 2/3"""

        title = Text(
            "方法一：逐步约分", font=FONT, font_size=40,
            color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # ========== Step 1: 12/18 ÷ 2 = 6/9 ==========

        step1_label = Text(
            "第一步：找一个公因数 2",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.0)
        self.play(Write(step1_label), run_time=0.5)

        # 分数链 step 1
        f1 = MathTex(r"\frac{12}{18}", font_size=68, color=COLOR_FRAC)
        arrow1 = MathTex(r"\longrightarrow", font_size=48, color=COLOR_HL)
        f2 = MathTex(r"\frac{6}{9}", font_size=68, color=COLOR_STEP)

        chain1 = VGroup(f1, arrow1, f2).arrange(RIGHT, buff=0.6)
        chain1.move_to(UP * 2.0)

        self.play(FadeIn(f1), run_time=0.4)

        # 弧线标注: 分子 ÷2, 分母 ÷2
        div2_top = MathTex(r"\div 2", font_size=30, color=COLOR_ACCENT)
        arr_top1 = CurvedArrow(
            f1.get_top() + UP * 0.15 + LEFT * 0.1,
            f2.get_top() + UP * 0.15 + RIGHT * 0.1,
            color=COLOR_ACCENT, stroke_width=2.5, angle=-0.5
        )
        div2_top.next_to(arr_top1, UP, buff=0.08)

        div2_bot = MathTex(r"\div 2", font_size=30, color=COLOR_ACCENT)
        arr_bot1 = CurvedArrow(
            f1.get_bottom() + DOWN * 0.15 + LEFT * 0.1,
            f2.get_bottom() + DOWN * 0.15 + RIGHT * 0.1,
            color=COLOR_ACCENT, stroke_width=2.5, angle=0.5
        )
        div2_bot.next_to(arr_bot1, DOWN, buff=0.08)

        self.play(
            FadeIn(arrow1), FadeIn(f2),
            Create(arr_top1), FadeIn(div2_top),
            Create(arr_bot1), FadeIn(div2_bot),
            run_time=0.8
        )
        self.wait(0.8)

        # ========== Step 2: 6/9 ÷ 3 = 2/3 ==========

        step2_label = Text(
            "第二步：再找一个公因数 3",
            font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.0)
        self.play(
            FadeOut(step1_label),
            FadeIn(step2_label, shift=UP * 0.2),
            run_time=0.4
        )

        f2b = MathTex(r"\frac{6}{9}", font_size=68, color=COLOR_STEP)
        arrow2 = MathTex(r"\longrightarrow", font_size=48, color=COLOR_HL)
        f3 = MathTex(r"\frac{2}{3}", font_size=68, color=COLOR_HL)

        chain2 = VGroup(f2b, arrow2, f3).arrange(RIGHT, buff=0.6)
        chain2.move_to(DOWN * 1.0)

        self.play(FadeIn(f2b), run_time=0.3)

        # 弧线标注: 分子 ÷3, 分母 ÷3
        div3_top = MathTex(r"\div 3", font_size=30, color=COLOR_GCD)
        arr_top2 = CurvedArrow(
            f2b.get_top() + UP * 0.15 + LEFT * 0.1,
            f3.get_top() + UP * 0.15 + RIGHT * 0.1,
            color=COLOR_GCD, stroke_width=2.5, angle=-0.5
        )
        div3_top.next_to(arr_top2, UP, buff=0.08)

        div3_bot = MathTex(r"\div 3", font_size=30, color=COLOR_GCD)
        arr_bot2 = CurvedArrow(
            f2b.get_bottom() + DOWN * 0.15 + LEFT * 0.1,
            f3.get_bottom() + DOWN * 0.15 + RIGHT * 0.1,
            color=COLOR_GCD, stroke_width=2.5, angle=0.5
        )
        div3_bot.next_to(arr_bot2, DOWN, buff=0.08)

        self.play(
            FadeIn(arrow2), FadeIn(f3),
            Create(arr_top2), FadeIn(div3_top),
            Create(arr_bot2), FadeIn(div3_bot),
            run_time=0.8
        )
        self.wait(0.5)

        # 高亮最终结果
        result_box = SurroundingRectangle(
            f3, color=COLOR_HL, stroke_width=3, buff=0.15,
            corner_radius=0.12
        )
        self.play(Create(result_box), run_time=0.4)

        # 结论
        note = Text(
            "2 和 3 只有公因数 1，不能再约了！",
            font=FONT, font_size=24, color=COLOR_SIMPLE
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, step2_label,
                f1, arrow1, f2, arr_top1, div2_top, arr_bot1, div2_bot,
                f2b, arrow2, f3, arr_top2, div3_top, arr_bot2, div3_bot,
                result_box, note
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 方法2 — 用最大公因数一步到位
    # ------------------------------------------------------------------

    def scene_4_gcd_method(self):
        """直接用最大公因数约分: 12/18 ÷6→ 2/3"""

        title = Text(
            "方法二：用最大公因数", font=FONT, font_size=40,
            color=COLOR_GCD, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 找最大公因数
        gcd_q = Text(
            "12 和 18 的最大公因数是多少？",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 4.0)
        self.play(Write(gcd_q), run_time=0.6)

        # 列出因数
        factors_12 = Text(
            "12 的因数: 1, 2, 3, 4, 6, 12",
            font=FONT, font_size=22, color=COLOR_FRAC
        ).move_to(UP * 2.8)
        factors_18 = Text(
            "18 的因数: 1, 2, 3, 6, 9, 18",
            font=FONT, font_size=22, color=COLOR_STEP
        ).move_to(UP * 2.0)

        self.play(Write(factors_12), run_time=0.5)
        self.play(Write(factors_18), run_time=0.5)
        self.wait(0.5)

        # 最大公因数 = 6
        gcd_ans = Text(
            "最大公因数 = 6",
            font=FONT, font_size=36, color=COLOR_GCD, weight=BOLD
        ).move_to(UP * 0.8)
        self.play(FadeIn(gcd_ans, scale=0.7), run_time=0.5)
        self.wait(0.5)

        # 一步到位
        step_text = Text(
            "分子分母同时除以 6，一步到位！",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(Write(step_text), run_time=0.6)

        # 分数链
        f_orig = MathTex(r"\frac{12}{18}", font_size=72, color=COLOR_FRAC)
        arrow = MathTex(r"\longrightarrow", font_size=52, color=COLOR_HL)
        f_result = MathTex(r"\frac{2}{3}", font_size=72, color=COLOR_HL)

        chain = VGroup(f_orig, arrow, f_result).arrange(RIGHT, buff=0.8)
        chain.move_to(DOWN * 2.5)

        self.play(FadeIn(f_orig), run_time=0.4)

        # 弧线: ÷6
        div6_top = MathTex(r"\div 6", font_size=34, color=COLOR_GCD)
        arr_top = CurvedArrow(
            f_orig.get_top() + UP * 0.15 + LEFT * 0.1,
            f_result.get_top() + UP * 0.15 + RIGHT * 0.1,
            color=COLOR_GCD, stroke_width=3, angle=-0.5
        )
        div6_top.next_to(arr_top, UP, buff=0.08)

        div6_bot = MathTex(r"\div 6", font_size=34, color=COLOR_GCD)
        arr_bot = CurvedArrow(
            f_orig.get_bottom() + DOWN * 0.15 + LEFT * 0.1,
            f_result.get_bottom() + DOWN * 0.15 + RIGHT * 0.1,
            color=COLOR_GCD, stroke_width=3, angle=0.5
        )
        div6_bot.next_to(arr_bot, DOWN, buff=0.08)

        self.play(
            FadeIn(arrow), FadeIn(f_result),
            Create(arr_top), FadeIn(div6_top),
            Create(arr_bot), FadeIn(div6_bot),
            run_time=1.0
        )

        # 高亮
        result_box = SurroundingRectangle(
            f_result, color=COLOR_HL, stroke_width=3, buff=0.15,
            corner_radius=0.12
        )
        self.play(Create(result_box), run_time=0.4)

        # 小提示
        tip = Text(
            "用最大公因数约分更快！",
            font=FONT, font_size=26, color=COLOR_ACCENT
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, gcd_q, factors_12, factors_18,
                gcd_ans, step_text,
                f_orig, arrow, f_result,
                arr_top, div6_top, arr_bot, div6_bot,
                result_box, tip
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 最简分数 + 约分依据
    # ------------------------------------------------------------------

    def scene_5_simplest_and_basis(self):
        """最简分数定义 + 约分的依据是分数的基本性质"""

        title = Text(
            "最简分数", font=FONT, font_size=42,
            color=COLOR_SIMPLE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 定义框
        simp_box = RoundedRectangle(
            width=7.8, height=2.8,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_SIMPLE, stroke_width=3
        ).move_to(UP * 3.0)
        self.play(FadeIn(simp_box), run_time=0.3)

        s1 = Text(
            "分子和分母只有公因数 1",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 3.5)
        s2 = Text(
            "的分数，叫做最简分数",
            font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 2.7)

        self.play(Write(s1), run_time=0.6)
        self.play(Write(s2), run_time=0.5)
        self.wait(0.5)

        # 示例
        ex_yes = VGroup(
            MathTex(r"\frac{2}{3}", font_size=52, color=COLOR_SIMPLE),
            MathTex(r"\frac{1}{4}", font_size=52, color=COLOR_SIMPLE),
            MathTex(r"\frac{5}{7}", font_size=52, color=COLOR_SIMPLE),
        ).arrange(RIGHT, buff=1.0).move_to(UP * 1.0)

        check_marks = VGroup(*[
            MathTex(r"\checkmark", font_size=36, color=COLOR_SIMPLE).next_to(
                f, DOWN, buff=0.2
            )
            for f in ex_yes
        ])

        self.play(FadeIn(ex_yes), run_time=0.5)
        self.play(FadeIn(check_marks), run_time=0.4)
        self.wait(0.5)

        # 约分目标
        goal = Text(
            "约分的目标：化成最简分数",
            font=FONT, font_size=28, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(goal, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # ====== 约分的依据 ======
        basis_title = Text(
            "约分的依据", font=FONT, font_size=36,
            color=COLOR_ORANGE, weight=BOLD
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(basis_title, shift=UP * 0.3), run_time=0.5)

        # 分数基本性质公式
        basis_formula = MathTex(
            r"\frac{a}{b}",
            r"=",
            r"\frac{a \div c}{b \div c}",
            font_size=44
        ).move_to(DOWN * 3.5)
        basis_formula[0].set_color(WHITE)
        basis_formula[2].set_color(COLOR_ORANGE)

        cond = MathTex(r"(c \neq 0)", font_size=32, color=COLOR_ORANGE)
        cond.next_to(basis_formula, RIGHT, buff=0.3)

        self.play(Write(basis_formula), FadeIn(cond), run_time=0.8)

        basis_note = Text(
            "分数的基本性质",
            font=FONT, font_size=24, color=COLOR_ORANGE
        ).move_to(DOWN * 4.8)
        self.play(FadeIn(basis_note, shift=UP * 0.2), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, simp_box, s1, s2,
                ex_yes, check_marks, goal,
                basis_title, basis_formula, cond, basis_note
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 练习 — 判断最简分数
    # ------------------------------------------------------------------

    def scene_6_practice(self):
        """判断哪些是最简分数"""

        title = Text(
            "练一练", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        prompt = Text(
            "下面哪些是最简分数？",
            font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 4.2)
        self.play(Write(prompt), run_time=0.5)

        # 四个分数
        fracs_data = [
            (r"\frac{3}{5}", True),
            (r"\frac{4}{8}", False),
            (r"\frac{7}{9}", True),
            (r"\frac{6}{15}", False),
        ]

        frac_mobs = []
        y_positions = [UP * 2.2, UP * 0.4, DOWN * 1.4, DOWN * 3.2]

        for i, ((tex, is_simple), y_pos) in enumerate(
            zip(fracs_data, y_positions)
        ):
            frac = MathTex(tex, font_size=62, color=WHITE)
            frac.move_to(LEFT * 1.5 + y_pos)
            frac_mobs.append((frac, is_simple))
            self.play(FadeIn(frac, shift=RIGHT * 0.3), run_time=0.3)

        self.wait(0.8)

        # 逐个判断
        for frac, is_simple in frac_mobs:
            if is_simple:
                mark = MathTex(
                    r"\checkmark", font_size=48, color=COLOR_SIMPLE
                )
                label = Text(
                    "最简分数", font=FONT, font_size=22, color=COLOR_SIMPLE
                )
            else:
                mark = MathTex(
                    r"\times", font_size=48, color=COLOR_ACCENT
                )
                label = Text(
                    "还能约分", font=FONT, font_size=22, color=COLOR_ACCENT
                )
            mark.next_to(frac, RIGHT, buff=0.6)
            label.next_to(mark, RIGHT, buff=0.3)
            self.play(FadeIn(mark), FadeIn(label), run_time=0.4)
            self.wait(0.3)

        # 约分 4/8 的演示
        demo_text = Text(
            "例：", font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 5.2 + LEFT * 3.0)
        demo = MathTex(
            r"\frac{4}{8}", r"=", r"\frac{4 \div 4}{8 \div 4}",
            r"=", r"\frac{1}{2}",
            font_size=36
        ).next_to(demo_text, RIGHT, buff=0.2)
        demo[0].set_color(COLOR_ACCENT)
        demo[2].set_color(COLOR_GCD)
        demo[4].set_color(COLOR_SIMPLE)

        self.play(FadeIn(demo_text), Write(demo), run_time=0.8)
        self.wait(1.5)

        # 清理所有元素（保留 author_mob）
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.author_mob and isinstance(mob, VMobject)],
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 总结公式框
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        """总结约分方法和最简分数"""

        title = Text(
            "总结", font=FONT, font_size=42,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # ===== 约分公式框 =====
        box1 = RoundedRectangle(
            width=7.8, height=3.0,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 2.8)
        self.play(FadeIn(box1), run_time=0.3)

        box1_title = Text(
            "约分", font=FONT, font_size=28, color=GRAY_A
        ).move_to(UP * 3.9)
        self.play(Write(box1_title), run_time=0.3)

        # 逐步约分示例
        step_demo = MathTex(
            r"\frac{12}{18}",
            r"\xrightarrow{\div 2}",
            r"\frac{6}{9}",
            r"\xrightarrow{\div 3}",
            r"\frac{2}{3}",
            font_size=38
        ).move_to(UP * 3.0)
        step_demo[0].set_color(COLOR_FRAC)
        step_demo[2].set_color(COLOR_STEP)
        step_demo[4].set_color(COLOR_HL)
        self.play(Write(step_demo), run_time=0.8)

        # 一步到位示例
        gcd_demo = MathTex(
            r"\frac{12}{18}",
            r"\xrightarrow{\div 6}",
            r"\frac{2}{3}",
            font_size=38
        ).move_to(UP * 1.8)
        gcd_demo[0].set_color(COLOR_FRAC)
        gcd_demo[2].set_color(COLOR_HL)
        self.play(Write(gcd_demo), run_time=0.6)
        self.wait(0.5)

        # ===== 要点 =====
        points_data = [
            ("约分依据：分数的基本性质", COLOR_ORANGE),
            ("约分目标：化成最简分数", COLOR_SIMPLE),
            ("用最大公因数约分更快！", COLOR_GCD),
        ]

        points = VGroup()
        for i, (text, color) in enumerate(points_data):
            bullet = Text(
                text, font=FONT, font_size=24, color=color
            ).move_to(DOWN * (0.3 + i * 1.0))
            points.add(bullet)

        for p in points:
            self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(0.5)

        # 最简分数定义回顾
        simp_box = RoundedRectangle(
            width=7.0, height=1.6,
            corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_SIMPLE, stroke_width=2.5
        ).move_to(DOWN * 4.0)
        self.play(FadeIn(simp_box), run_time=0.3)

        simp_text = Text(
            "最简分数：分子分母只有公因数 1",
            font=FONT, font_size=24, color=COLOR_SIMPLE
        ).move_to(DOWN * 4.0)
        self.play(Write(simp_text), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, box1, box1_title,
                step_demo, gcd_demo,
                points, simp_box, simp_text
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        """作者信息放大 + 关注提示 + 装饰"""

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

        # 装饰: 6个小分数围绕旋转
        deco_colors = [
            COLOR_FRAC, COLOR_STEP, COLOR_GCD,
            COLOR_SIMPLE, COLOR_ACCENT, COLOR_HL
        ]
        deco_fracs = [
            r"\frac{12}{18}", r"\frac{6}{9}", r"\frac{2}{3}",
            r"\frac{3}{5}", r"\frac{1}{4}", r"\frac{a}{b}"
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
#   快速预览: manim -pql 005_约分.py ReducingFractionsLesson
#   高质量:   manim -qh  005_约分.py ReducingFractionsLesson
#   4K:       manim -qk  005_约分.py ReducingFractionsLesson
# ======================================================================
