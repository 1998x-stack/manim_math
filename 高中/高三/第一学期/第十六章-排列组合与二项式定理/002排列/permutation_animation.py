"""
排列 Permutation - 高三数学教学动画

# 快速预览 (480p)
manim -pql permutation_animation.py PermutationLesson

# 高质量输出 (1080p, 适合发布)
manim -qh permutation_animation.py PermutationLesson

格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
知识点: 排列, 排列数公式, 全排列, 阶乘
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────────────────────────
# 全局配置
# ─────────────────────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ─────────────────────────────────────────────────────────────
# 颜色方案
# ─────────────────────────────────────────────────────────────
BG_COLOR       = "#1a1a2e"
COLOR_TITLE    = "#e2b96a"      # 金黄
COLOR_SLOT     = "#2563eb"      # 蓝色槽位
COLOR_SLOT_HL  = "#f59e0b"      # 高亮槽位
COLOR_ARROW    = "#34d399"      # 绿色箭头
COLOR_FORMULA  = "#f472b6"      # 粉色公式
COLOR_EXPLAIN  = "#94a3b8"      # 灰蓝说明
COLOR_HL       = "#facc15"      # 黄色高亮
COLOR_PERSON   = ["#ef4444", "#3b82f6", "#a855f7",
                  "#22c55e", "#f97316"]  # 5种人物颜色
FONT = "PingFang SC"

# ─────────────────────────────────────────────────────────────
# 辅助函数
# ─────────────────────────────────────────────────────────────
def zh(text, size=28, color=WHITE, **kw):
    """创建中文 Text 对象"""
    return Text(text, font=FONT, font_size=size, color=color, **kw)

def make_slot_box(label="?", label_color=WHITE, width=1.5, height=1.5):
    """创建一个槽位框 (矩形 + 中心标签)"""
    rect = Rectangle(
        width=width, height=height,
        color=COLOR_SLOT,
        stroke_width=3,
        fill_color=COLOR_SLOT,
        fill_opacity=0.15
    )
    txt = zh(label, size=36, color=label_color)
    return VGroup(rect, txt)

def make_numbered_slot(n_choices, width=1.5, height=1.5):
    """创建带数字的槽位 (显示可选数量)"""
    rect = Rectangle(
        width=width, height=height,
        color=COLOR_SLOT_HL,
        stroke_width=3,
        fill_color=COLOR_SLOT_HL,
        fill_opacity=0.2
    )
    txt = zh(str(n_choices), size=44, color=COLOR_SLOT_HL)
    return VGroup(rect, txt)

def author_watermark():
    """作者水印 (顶部)"""
    return zh("上海初高中数学直通车 @emptyandcalm",
              size=18, color=COLOR_EXPLAIN).move_to(UP * 7.3)

# ─────────────────────────────────────────────────────────────
# 主场景
# ─────────────────────────────────────────────────────────────
class PermutationLesson(Scene):
    """
    排列知识点教学动画
    场景顺序:
      S1  开场钩子 — 3人站队问题
      S2  分步计数 — 乘法原理可视化
      S3  引入符号 — A(n,m) 的写法
      S4  公式推导 — A(n,m)=n!/(n-m)!
      S5  全排列   — A(n,n)=n!
      S6  特殊值   — 0!=1, A(n,0)=1
      S7  例题练习 — A(5,3)=60
      S8  汇总口诀
      S9  片尾     — 作者信息
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 持久水印
        self.watermark = author_watermark()
        self.add(self.watermark)

        self.s1_hook()
        self.s2_counting()
        self.s3_notation()
        self.s4_formula()
        self.s5_full_permutation()
        self.s6_special_cases()
        self.s7_example()
        self.s8_summary()
        self.s9_outro()

    # ──────────────────────────────────────────────────────────
    # S1  开场钩子
    # ──────────────────────────────────────────────────────────
    def s1_hook(self):
        title = zh("排  列", size=54, color=COLOR_TITLE).move_to(UP * 6.2)
        sub   = zh("Permutation", size=28, color=COLOR_EXPLAIN).move_to(UP * 5.4)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(0.3)

        # 钩子问题
        q1 = zh("甲、乙、丙 3位同学", size=30, color=WHITE).move_to(UP * 4.2)
        q2 = zh("站成一排", size=36, color=COLOR_HL).move_to(UP * 3.5)
        q3 = zh("共有多少种站法？", size=30, color=WHITE).move_to(UP * 2.8)

        self.play(FadeIn(q1, shift=RIGHT * 0.3), run_time=0.5)
        self.play(Write(q2), run_time=0.5)
        self.play(FadeIn(q3, shift=LEFT * 0.3), run_time=0.5)

        # 3个人物圆圈
        names = ["甲", "乙", "丙"]
        people = VGroup()
        for i, (name, col) in enumerate(zip(names, COLOR_PERSON)):
            circ = Circle(radius=0.45, fill_color=col,
                          fill_opacity=0.85, stroke_width=0)
            label = zh(name, size=26, color=WHITE)
            p = VGroup(circ, label).move_to(
                np.array([(i - 1) * 1.5, 1.4, 0])
            )
            people.add(p)

        self.play(LaggedStart(*[GrowFromCenter(p) for p in people],
                               lag_ratio=0.25, run_time=1.0))
        self.wait(0.4)

        question_mark = zh("= ?", size=48, color=COLOR_FORMULA).move_to(RIGHT * 1.8 + DOWN * 0.2)
        self.play(Write(question_mark), run_time=0.4)
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(q1), FadeOut(q2), FadeOut(q3),
            FadeOut(people), FadeOut(question_mark),
            FadeOut(title), FadeOut(sub),
            run_time=0.5
        )

    # ──────────────────────────────────────────────────────────
    # S2  分步计数 — 乘法原理
    # ──────────────────────────────────────────────────────────
    def s2_counting(self):
        title = zh("分步计数法", size=40, color=COLOR_TITLE).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 3个槽位
        slot_y   = 2.5
        n_slots  = 3
        sw, sh   = 1.5, 1.5
        spacing  = 0.4
        total_w  = n_slots * sw + (n_slots - 1) * spacing
        xs = [-total_w/2 + i * (sw + spacing) + sw/2 for i in range(n_slots)]

        pos_labels = ["第一位", "第二位", "第三位"]
        choices    = [3, 2, 1]

        slots = VGroup()
        for i in range(n_slots):
            s = make_slot_box("?", width=sw, height=sh)
            s.move_to(np.array([xs[i], slot_y, 0]))
            slots.add(s)

        pos_texts = VGroup()
        for i, lbl in enumerate(pos_labels):
            t = zh(lbl, size=20, color=COLOR_EXPLAIN)
            t.move_to(np.array([xs[i], slot_y - sh/2 - 0.35, 0]))
            pos_texts.add(t)

        self.play(LaggedStart(*[Create(s) for s in slots],
                               lag_ratio=0.2, run_time=0.8))
        self.play(LaggedStart(*[FadeIn(t) for t in pos_texts],
                               lag_ratio=0.15, run_time=0.5))
        self.wait(0.3)

        # 逐步填入选择数量
        explain_texts = [
            "第一位：3人可选",
            "第二位：剩 2 人",
            "第三位：剩 1 人",
        ]
        explain_y = 1.0

        filled_slots = VGroup()
        explain_box  = None

        for i in range(n_slots):
            # 替换 ? 为数字
            new_s = make_numbered_slot(choices[i], width=sw, height=sh)
            new_s.move_to(np.array([xs[i], slot_y, 0]))
            filled_slots.add(new_s)

            exp = zh(explain_texts[i], size=24, color=COLOR_HL).move_to(
                np.array([0, explain_y, 0])
            )

            if explain_box is not None:
                self.play(FadeOut(explain_box), run_time=0.2)
            self.play(
                Transform(slots[i], new_s),
                FadeIn(exp, shift=UP * 0.2),
                run_time=0.6
            )
            explain_box = exp
            self.wait(0.4)

        self.play(FadeOut(explain_box), run_time=0.3)

        # 乘法
        mult_row = MathTex(
            r"3 \times 2 \times 1 = 6",
            font_size=44,
            color=COLOR_FORMULA
        ).move_to(np.array([0, -0.2, 0]))

        self.play(Write(mult_row), run_time=0.8)

        result = zh("共 6 种站法！", size=34, color=COLOR_HL).move_to(
            np.array([0, -1.2, 0])
        )
        self.play(FadeIn(result, scale=1.1), run_time=0.5)
        self.wait(1.2)

        # 清场 (保留槽位结构用于过渡)
        self.play(
            FadeOut(title),
            FadeOut(slots),
            FadeOut(pos_texts),
            FadeOut(mult_row),
            FadeOut(result),
            run_time=0.5
        )

    # ──────────────────────────────────────────────────────────
    # S3  引入符号 A(n,m)
    # ──────────────────────────────────────────────────────────
    def s3_notation(self):
        title = zh("排列数符号", size=40, color=COLOR_TITLE).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # 定义文字
        def_line1 = zh("从 n 个不同元素中", size=28, color=WHITE).move_to(UP * 5.2)
        def_line2 = zh("取出 m 个，按顺序排成一列", size=28, color=WHITE).move_to(UP * 4.5)
        def_line3 = zh("叫做从 n 个中取 m 个的", size=26, color=COLOR_EXPLAIN).move_to(UP * 3.7)
        def_line4 = zh("排  列", size=36, color=COLOR_HL).move_to(UP * 3.0)

        self.play(FadeIn(def_line1), run_time=0.4)
        self.play(FadeIn(def_line2), run_time=0.4)
        self.wait(0.3)
        self.play(FadeIn(def_line3), FadeIn(def_line4), run_time=0.5)
        self.wait(0.5)

        # 符号展示
        notation = MathTex(
            r"A", r"_n", r"^m",
            font_size=80,
            color=COLOR_FORMULA
        ).move_to(UP * 1.5)

        # 标注 n 和 m
        brace_n = Brace(notation[1], DOWN, color=COLOR_EXPLAIN, buff=0.05)
        label_n = zh("元素总数", size=20, color=COLOR_EXPLAIN).next_to(brace_n, DOWN, buff=0.1)

        brace_m = Brace(notation[2], UP, color=COLOR_ARROW, buff=0.05)
        label_m = zh("取出的个数", size=20, color=COLOR_ARROW).next_to(brace_m, UP, buff=0.1)

        self.play(Write(notation), run_time=0.8)
        self.wait(0.3)
        self.play(GrowFromCenter(brace_n), FadeIn(label_n), run_time=0.5)
        self.play(GrowFromCenter(brace_m), FadeIn(label_m), run_time=0.5)
        self.wait(0.4)

        # 约束条件
        constraint = MathTex(
            r"(\ m \leq n,\ m,n \in \mathbb{N}^*\ )",
            font_size=30,
            color=COLOR_EXPLAIN
        ).move_to(UP * 0.0)

        self.play(FadeIn(constraint), run_time=0.4)


        # 避免MathTex含中文，改用VGroup
        ex_left  = zh("3人全站 = ", size=30, color=WHITE)
        ex_mid   = MathTex(r"A_3^3", font_size=38, color=COLOR_FORMULA)
        ex_right = zh("= 6", size=30, color=COLOR_HL)
        ex_group = VGroup(ex_left, ex_mid, ex_right).arrange(RIGHT, buff=0.15)
        ex_group.move_to(DOWN * 1.2)

        self.play(FadeIn(ex_group, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(title), FadeOut(def_line1), FadeOut(def_line2),
            FadeOut(def_line3), FadeOut(def_line4),
            FadeOut(notation), FadeOut(brace_n), FadeOut(label_n),
            FadeOut(brace_m), FadeOut(label_m),
            FadeOut(constraint), FadeOut(ex_group),
            run_time=0.5
        )

    # ──────────────────────────────────────────────────────────
    # S4  公式推导 A(n,m) = n!/(n-m)!
    # ──────────────────────────────────────────────────────────
    def s4_formula(self):
        title = zh("排列公式推导", size=40, color=COLOR_TITLE).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # 展示 m 个槽位 (n个取m个)
        explain = zh("从 n 个中取 m 个排列", size=26, color=COLOR_EXPLAIN).move_to(UP * 5.5)
        self.play(FadeIn(explain), run_time=0.4)

        # 槽位展示 (抽象，用省略号)
        slot_y = 4.0
        sw, sh = 1.1, 1.1

        slot_data = [
            ("n",   COLOR_SLOT_HL),
            ("n{-}1", COLOR_SLOT_HL),
            (r"\cdots", COLOR_EXPLAIN),
            ("n{-}m{+}1", COLOR_SLOT_HL),
        ]

        positions = [-3.0, -1.1, 0.6, 2.2]

        slot_group = VGroup()
        for i, ((txt, col), px) in enumerate(zip(slot_data, positions)):
            rect = Rectangle(width=sw, height=sh,
                             color=col, stroke_width=2.5,
                             fill_color=col, fill_opacity=0.12)
            label = MathTex(txt, font_size=28, color=col)
            grp = VGroup(rect, label).move_to(np.array([px, slot_y, 0]))
            slot_group.add(grp)

        # 位序标签
        pos_labels = ["第1位", "第2位", "", "第m位"]
        plabel_grp = VGroup()
        for i, (lbl, px) in enumerate(zip(pos_labels, positions)):
            if lbl:
                t = zh(lbl, size=17, color=COLOR_EXPLAIN)
                t.move_to(np.array([px, slot_y - sh/2 - 0.3, 0]))
                plabel_grp.add(t)

        self.play(LaggedStart(*[Create(s) for s in slot_group],
                               lag_ratio=0.15, run_time=0.8))
        self.play(FadeIn(plabel_grp), run_time=0.3)
        self.wait(0.4)

        # 选择数量说明
        choice_texts = [
            (r"n\ \text{种}", -3.0, 2.7),
            (r"(n-1)\ \text{种}", -1.1, 2.7),
            (r"(n-m+1)\ \text{种}", 2.2, 2.7),
        ]

        choice_grp = VGroup()
        for tex, px, py in choice_texts:
            # 中文"种"改为Text
            if "种" in tex:
                # 分开处理
                num_part = tex.replace(r"\ \text{种}", "")
                num_label = MathTex(num_part, font_size=22, color=COLOR_ARROW)
                cn_label  = zh("种", size=20, color=COLOR_ARROW)
                combo = VGroup(num_label, cn_label).arrange(RIGHT, buff=0.05)
                combo.move_to(np.array([px, py, 0]))
                choice_grp.add(combo)
            else:
                t = MathTex(tex, font_size=22, color=COLOR_ARROW)
                t.move_to(np.array([px, py, 0]))
                choice_grp.add(t)

        self.play(LaggedStart(*[FadeIn(c, shift=UP*0.15) for c in choice_grp],
                               lag_ratio=0.2, run_time=0.7))
        self.wait(0.4)

        # 乘法原理
        mult_explain = zh("乘法原理 → 各位数量相乘", size=24, color=COLOR_EXPLAIN).move_to(UP * 1.8)
        self.play(FadeIn(mult_explain), run_time=0.4)

        step1 = MathTex(
            r"A_n^m = n \cdot (n-1) \cdot (n-2) \cdots (n-m+1)",
            font_size=30,
            color=COLOR_FORMULA
        ).move_to(UP * 0.8)
        self.play(Write(step1), run_time=1.0)
        self.wait(0.5)

        # 分子分母化简
        step2_title = zh("分子分母同乘 (n-m)! →", size=22, color=COLOR_EXPLAIN).move_to(UP * -0.2)
        self.play(FadeIn(step2_title), run_time=0.4)

        step2 = MathTex(
            r"A_n^m = \dfrac{n!}{(n-m)!}",
            font_size=44,
            color=COLOR_FORMULA
        ).move_to(DOWN * 1.0)

        self.play(Write(step2), run_time=0.9)

        # 框起核心公式
        box = SurroundingRectangle(step2, color=COLOR_HL, buff=0.18,
                                   corner_radius=0.1, stroke_width=3)
        self.play(Create(box), run_time=0.5)

        key_tip = zh("★ 核心公式", size=22, color=COLOR_HL).next_to(box, DOWN, buff=0.2)
        self.play(FadeIn(key_tip), run_time=0.3)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title), FadeOut(explain),
            FadeOut(slot_group), FadeOut(plabel_grp),
            FadeOut(choice_grp), FadeOut(mult_explain),
            FadeOut(step1), FadeOut(step2_title),
            FadeOut(step2), FadeOut(box), FadeOut(key_tip),
            run_time=0.6
        )

    # ──────────────────────────────────────────────────────────
    # S5  全排列 A(n,n) = n!
    # ──────────────────────────────────────────────────────────
    def s5_full_permutation(self):
        title = zh("全 排 列", size=44, color=COLOR_TITLE).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        def_text = zh("n 个元素全部取出排成一列", size=28, color=WHITE).move_to(UP * 5.5)
        self.play(FadeIn(def_text), run_time=0.4)

        # 公式
        formula = MathTex(
            r"A_n^n = \dfrac{n!}{(n-n)!} = \dfrac{n!}{0!} = \dfrac{n!}{1} = n!",
            font_size=34,
            color=COLOR_FORMULA
        ).move_to(UP * 4.0)
        self.play(Write(formula), run_time=1.2)
        self.wait(0.5)

        # 结论框
        conclusion = MathTex(
            r"A_n^n = n!",
            font_size=56,
            color=COLOR_HL
        ).move_to(UP * 2.5)
        c_box = SurroundingRectangle(conclusion, color=COLOR_HL,
                                     buff=0.2, corner_radius=0.12,
                                     stroke_width=3)
        self.play(Write(conclusion), run_time=0.6)
        self.play(Create(c_box), run_time=0.4)

        # 展开n! 例子
        expand_title = zh("阶乘展开示意", size=24, color=COLOR_EXPLAIN).move_to(UP * 1.3)
        self.play(FadeIn(expand_title), run_time=0.3)

        expand = MathTex(
            r"n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1",
            font_size=28,
            color=WHITE
        ).move_to(UP * 0.5)
        self.play(Write(expand), run_time=0.8)

        # 具体例子
        examples_data = [
            (r"3! = 3 \times 2 \times 1 = 6",   UP * -0.5),
            (r"4! = 4 \times 3 \times 2 \times 1 = 24", UP * -1.4),
            (r"5! = 120",                          UP * -2.3),
        ]
        for tex, pos in examples_data:
            e = MathTex(tex, font_size=32, color=COLOR_ARROW).move_to(pos)
            self.play(FadeIn(e, shift=RIGHT * 0.2), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(def_text), FadeOut(formula),
            FadeOut(conclusion), FadeOut(c_box),
            FadeOut(expand_title), FadeOut(expand),
            *[FadeOut(mob) for mob in self.mobjects if mob not in [self.watermark]],
            run_time=0.6
        )

    # ──────────────────────────────────────────────────────────
    # S6  特殊值：0! = 1, A(n,0) = 1
    # ──────────────────────────────────────────────────────────
    def s6_special_cases(self):
        title = zh("特殊规定", size=40, color=COLOR_TITLE).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # 0! = 1
        zero_fact_title = zh("规定：", size=28, color=WHITE).move_to(UP * 5.5)
        self.play(FadeIn(zero_fact_title), run_time=0.3)

        zero_fact = MathTex(r"0! = 1", font_size=64, color=COLOR_FORMULA).move_to(UP * 4.5)
        self.play(Write(zero_fact), run_time=0.6)

        why_box = RoundedRectangle(
            width=6.5, height=1.6,
            corner_radius=0.2,
            color=COLOR_EXPLAIN,
            fill_color=COLOR_EXPLAIN,
            fill_opacity=0.08,
            stroke_width=1.5
        ).move_to(UP * 3.2)

        why1 = zh("为什么？", size=22, color=COLOR_EXPLAIN).move_to(UP * 3.55)
        why2 = MathTex(
            r"A_n^n = \frac{n!}{0!} = n! \Rightarrow 0! = 1",
            font_size=26,
            color=COLOR_EXPLAIN
        ).move_to(UP * 2.9)

        self.play(Create(why_box), FadeIn(why1), Write(why2), run_time=0.8)
        self.wait(0.6)

        # A(n,0) = 1
        a_n0 = MathTex(
            r"A_n^0 = \frac{n!}{n!} = 1",
            font_size=44,
            color=COLOR_ARROW
        ).move_to(UP * 1.7)

        a_n0_explain = zh("从n个中取0个，只有「不取」1种", size=22, color=COLOR_EXPLAIN)
        a_n0_explain.move_to(UP * 1.0)

        self.play(Write(a_n0), run_time=0.6)
        self.play(FadeIn(a_n0_explain), run_time=0.4)

        # A(n,1) = n
        a_n1 = MathTex(r"A_n^1 = n", font_size=44, color=COLOR_ARROW).move_to(UP * 0.0)
        a_n1_explain = zh("从n个中取1个，有n种选法", size=22, color=COLOR_EXPLAIN).move_to(DOWN * 0.7)

        self.play(Write(a_n1), run_time=0.5)
        self.play(FadeIn(a_n1_explain), run_time=0.4)
        self.wait(1.2)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not self.watermark],
            run_time=0.5
        )

    # ──────────────────────────────────────────────────────────
    # S7  例题 A(5,3) = 60
    # ──────────────────────────────────────────────────────────
    def s7_example(self):
        title = zh("例题练习", size=40, color=COLOR_TITLE).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        problem = zh("从 5 人中选 3 人排成一排，有多少种排法？", size=26, color=WHITE)
        problem.move_to(UP * 5.5)
        self.play(FadeIn(problem), run_time=0.5)

        # Step1: 写出符号
        step1_label = zh("第一步：写出排列数符号", size=24, color=COLOR_EXPLAIN).move_to(UP * 4.4)
        step1_expr  = MathTex(r"A_5^3", font_size=60, color=COLOR_FORMULA).move_to(UP * 3.5)

        self.play(FadeIn(step1_label), run_time=0.3)
        self.play(Write(step1_expr), run_time=0.5)
        self.wait(0.3)

        # Step2: 代入公式
        step2_label = zh("第二步：代入公式", size=24, color=COLOR_EXPLAIN).move_to(UP * 2.5)
        step2_expr = MathTex(
            r"A_5^3 = \frac{5!}{(5-3)!} = \frac{5!}{2!}",
            font_size=36, color=COLOR_FORMULA
        ).move_to(UP * 1.6)

        self.play(FadeIn(step2_label), run_time=0.3)
        self.play(Write(step2_expr), run_time=0.7)
        self.wait(0.4)

        # Step3: 展开计算
        step3_label = zh("第三步：展开计算", size=24, color=COLOR_EXPLAIN).move_to(UP * 0.5)
        step3_expr = MathTex(
            r"= \frac{5 \times 4 \times 3 \times 2 \times 1}{2 \times 1}",
            font_size=34, color=COLOR_FORMULA
        ).move_to(DOWN * 0.4)

        self.play(FadeIn(step3_label), run_time=0.3)
        self.play(Write(step3_expr), run_time=0.7)
        self.wait(0.3)

        # Step4: 简化
        step4_expr = MathTex(
            r"= 5 \times 4 \times 3 = 60",
            font_size=40, color=COLOR_HL
        ).move_to(DOWN * 1.5)

        self.play(Write(step4_expr), run_time=0.6)

        # 结果框
        result_box = SurroundingRectangle(step4_expr, color=COLOR_HL,
                                          buff=0.15, corner_radius=0.1,
                                          stroke_width=3)
        self.play(Create(result_box), run_time=0.4)
        self.play(Flash(step4_expr, color=COLOR_HL, flash_radius=0.6), run_time=0.5)

        tip = zh("技巧：直接乘连续 m 个因数", size=22, color=COLOR_EXPLAIN).move_to(DOWN * 2.8)
        tip2 = MathTex(
            r"A_n^m = n(n-1)(n-2)\cdots(n-m+1)",
            font_size=26, color=COLOR_EXPLAIN
        ).move_to(DOWN * 3.7)

        self.play(FadeIn(tip), run_time=0.3)
        self.play(Write(tip2), run_time=0.6)
        self.wait(1.5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not self.watermark],
            run_time=0.5
        )

    # ──────────────────────────────────────────────────────────
    # S8  汇总口诀
    # ──────────────────────────────────────────────────────────
    def s8_summary(self):
        title = zh("排列公式汇总", size=40, color=COLOR_TITLE).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        summary_data = [
            (r"A_n^m = \dfrac{n!}{(n-m)!}",
             "核心公式", UP * 5.2),
            (r"A_n^m = n(n-1)\cdots(n-m+1)",
             "乘积写法", UP * 3.8),
            (r"A_n^n = n!",
             "全排列", UP * 2.5),
            (r"A_n^0 = 1",
             "取0个", UP * 1.4),
            (r"0! = 1",
             "特殊规定", UP * 0.3),
        ]

        for tex, label_str, pos in summary_data:
            row_formula = MathTex(tex, font_size=34, color=COLOR_FORMULA)
            row_label   = zh(label_str, size=22, color=COLOR_EXPLAIN)
            row = VGroup(row_formula, row_label).arrange(RIGHT, buff=0.4)
            row.move_to(pos)
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.4)

        # 口诀
        slogan_box = RoundedRectangle(
            width=7.0, height=1.2,
            corner_radius=0.2,
            color=COLOR_HL,
            fill_color=COLOR_HL,
            fill_opacity=0.1,
            stroke_width=2
        ).move_to(DOWN * 1.4)
        slogan = zh("顺序有关 → 用排列！", size=30, color=COLOR_HL).move_to(DOWN * 1.4)

        self.play(Create(slogan_box), Write(slogan), run_time=0.7)
        self.wait(2.0)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob is not self.watermark],
            run_time=0.6
        )

    # ──────────────────────────────────────────────────────────
    # S9  片尾
    # ──────────────────────────────────────────────────────────
    def s9_outro(self):
        author_big = zh("上海初高中数学直通车", size=38, color=WHITE).move_to(UP * 2.0)
        author_id  = zh("@emptyandcalm", size=28, color=COLOR_EXPLAIN).move_to(UP * 1.1)

        self.play(
            Transform(self.watermark, author_big),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = zh("关注我，获得更多数学技巧！", size=28, color=COLOR_HL).move_to(DOWN * 0.2)
        self.play(FadeIn(follow, scale=1.08), run_time=0.5)

        # 装饰：公式雨
        decorations = VGroup()
        formulas = [r"A_n^m", r"n!", r"A_n^n", r"0!=1", r"A_n^0"]
        positions = [
            [-3.0, -2.0], [-1.2, -2.8], [0.6, -2.3],
            [2.5, -1.8], [-2.0, -3.5],
        ]
        for tex, (x, y) in zip(formulas, positions):
            d = MathTex(tex, font_size=24, color=COLOR_FORMULA, fill_opacity=0.5)
            d.move_to(np.array([x, y, 0]))
            decorations.add(d)

        self.play(LaggedStart(*[FadeIn(d, scale=0.6) for d in decorations],
                               lag_ratio=0.15, run_time=0.8))

        self.wait(1.5)
        self.play(FadeOut(decorations), run_time=0.5)
        self.wait(0.5)