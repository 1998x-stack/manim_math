"""
003_分数应用题.py — 分数应用题 教学动画

知识点: 分数乘除法应用题三大类型
  核心关系: 单位'1'的量 × 分率 = 对应量
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景:
  1. 开场钩子 — 核心关系式亮出
  2. 三大类型总览
  3. 类型1: 求一个数的几分之几是多少 (乘法)
  4. 类型2: 已知几分之几，求整体 (除法)
  5. 类型3: 求一个数是另一个数的几分之几 (除法)
  6. 总结公式框
  7. 片尾
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
BG_COLOR    = "#1a1a2e"
COLOR_TYPE1 = "#3b82f6"   # 蓝 — 类型1 (乘法)
COLOR_TYPE2 = "#f59e0b"   # 橙 — 类型2 (除法求整体)
COLOR_TYPE3 = "#22c55e"   # 绿 — 类型3 (除法求分率)
COLOR_HL    = "#fbbf24"   # 黄 高亮
COLOR_UNIT1 = "#a78bfa"   # 紫 单位1
COLOR_FRAC  = "#f472b6"   # 粉 分率
COLOR_CORR  = "#34d399"   # 青 对应量
COLOR_AUTHOR = "#6b7280"  # 灰作者
FONT        = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class FractionWordProblemLesson(Scene):
    """
    分数应用题教学动画
    场景顺序:
      1. 开场钩子
      2. 三大类型总览
      3. 类型1 例题 (乘法)
      4. 类型2 例题 (除法 — 求整体)
      5. 类型3 例题 (除法 — 求分率)
      6. 总结公式框
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_overview()
        self.scene_3_type1()
        self.scene_4_type2()
        self.scene_5_type3()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 工具: 绘制条形图 (用于可视化分率)
    # ------------------------------------------------------------------

    def make_bar(self, n_parts, filled, fill_color, center, bar_width=6.0, bar_height=0.9):
        """返回 VGroup: n 等份条形，前 filled 份高亮"""
        part_w = bar_width / n_parts
        parts = VGroup()
        for i in range(n_parts):
            color = fill_color if i < filled else "#334155"
            rect = Rectangle(
                width=part_w - 0.05, height=bar_height,
                fill_color=color, fill_opacity=0.85,
                stroke_color=WHITE, stroke_width=1.5
            )
            rect.move_to(
                center
                + LEFT * (bar_width / 2 - part_w / 2)
                + RIGHT * i * part_w
            )
            parts.add(rect)
        return parts

    # ------------------------------------------------------------------
    # 工具: 彩色角括号标签
    # ------------------------------------------------------------------

    def make_brace_label(self, bar, text_str, direction, color, font_size=22):
        brace = Brace(bar, direction=direction, color=color, buff=0.08)
        label = Text(text_str, font=FONT, font_size=font_size, color=color)
        brace.put_at_tip(label, buff=0.12)
        return VGroup(brace, label)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 作者信息 (贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 标题
        hook1 = Text(
            "分数应用题", font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.6)
        hook2 = Text(
            "掌握一个公式，搞定三类题！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(UP * 4.6)

        self.play(Write(hook1), run_time=0.7)
        self.play(FadeIn(hook2, shift=UP * 0.2), run_time=0.5)

        # 核心关系式框
        core_bg = RoundedRectangle(
            width=7.8, height=2.8, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2.5
        ).move_to(UP * 1.8)

        core_title = Text("核心关系式", font=FONT, font_size=26, color=COLOR_HL)

        # 行1: 单位'1'的量 × 分率 = 对应量
        r1_a = Text("单位", font=FONT, font_size=24, color=COLOR_UNIT1)
        r1_b = Text("'1'", font=FONT, font_size=24, color=COLOR_UNIT1)
        r1_c = Text("的量", font=FONT, font_size=24, color=COLOR_UNIT1)
        r1_op = MathTex(r"\times", font_size=28, color=WHITE)
        r1_d = Text("分率", font=FONT, font_size=24, color=COLOR_FRAC)
        r1_eq = MathTex(r"=", font_size=28, color=WHITE)
        r1_e = Text("对应量", font=FONT, font_size=24, color=COLOR_CORR)
        row1 = VGroup(r1_a, r1_b, r1_c, r1_op, r1_d, r1_eq, r1_e).arrange(RIGHT, buff=0.1)

        core_content = VGroup(core_title, row1).arrange(DOWN, buff=0.4)
        core_content.move_to(core_bg.get_center())

        self.play(FadeIn(core_bg), run_time=0.4)
        self.play(Write(core_content), run_time=1.0)
        self.wait(1.2)

        # 清理
        self.play(FadeOut(VGroup(hook1, hook2, core_bg, core_content)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 2: 三大类型总览
    # ------------------------------------------------------------------

    def scene_2_overview(self):
        title = Text(
            "三大基本类型", font=FONT, font_size=44, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        cards = []
        data = [
            (COLOR_TYPE1, "①", "乘法",  "已知单位'1'和分率\n求对应量"),
            (COLOR_TYPE2, "②", "除法①", "已知对应量和分率\n求单位'1'"),
            (COLOR_TYPE3, "③", "除法②", "已知两个量\n求分率"),
        ]
        y_positions = [3.8, 1.6, -0.6]

        for (color, num_str, op_str, desc_str), y in zip(data, y_positions):
            card_bg = RoundedRectangle(
                width=7.6, height=1.7, corner_radius=0.25,
                fill_color="#1e293b", fill_opacity=0.9,
                stroke_color=color, stroke_width=2
            ).move_to(UP * y)

            num_text = Text(num_str, font=FONT, font_size=36, color=color, weight=BOLD)
            op_text = Text(op_str, font=FONT, font_size=28, color=WHITE, weight=BOLD)
            desc_text = Text(desc_str, font=FONT, font_size=20, color=GRAY_A)

            content = VGroup(
                VGroup(num_text, op_text).arrange(RIGHT, buff=0.25),
                desc_text
            ).arrange(DOWN, buff=0.18)
            content.move_to(card_bg.get_center())

            card = VGroup(card_bg, content)
            cards.append(card)
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.4)

        self.wait(1.5)

        # 公式提示
        formula_hint_bg = RoundedRectangle(
            width=7.6, height=1.0, corner_radius=0.2,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=1.5
        ).move_to(DOWN * 2.8)

        hint_a = Text("单位", font=FONT, font_size=20, color=COLOR_UNIT1)
        hint_b = Text("'1'", font=FONT, font_size=20, color=COLOR_UNIT1)
        hint_c = Text("的量", font=FONT, font_size=20, color=COLOR_UNIT1)
        hint_x = MathTex(r"\times", font_size=22, color=WHITE)
        hint_d = Text("分率", font=FONT, font_size=20, color=COLOR_FRAC)
        hint_eq = MathTex(r"=", font_size=22, color=WHITE)
        hint_e = Text("对应量", font=FONT, font_size=20, color=COLOR_CORR)
        formula_row = VGroup(hint_a, hint_b, hint_c, hint_x, hint_d, hint_eq, hint_e).arrange(RIGHT, buff=0.1)
        formula_row.move_to(formula_hint_bg.get_center())

        self.play(FadeIn(formula_hint_bg), Write(formula_row), run_time=0.6)
        self.wait(1.0)

        self.play(FadeOut(VGroup(*cards, formula_hint_bg, formula_row, title)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 3: 类型1 — 乘法 (求一个数的几分之几是多少)
    # ------------------------------------------------------------------

    def scene_3_type1(self):
        color = COLOR_TYPE1

        # 标题
        type_label = Text(
            "① 求一个数的几分之几是多少",
            font=FONT, font_size=32, color=color, weight=BOLD
        ).move_to(UP * 5.8)
        op_label = Text("→ 用乘法", font=FONT, font_size=26, color=WHITE).next_to(type_label, DOWN, buff=0.2)
        self.play(Write(type_label), FadeIn(op_label, shift=UP * 0.2), run_time=0.6)

        # 例题文字
        line1 = Text("学校图书馆共有图书 600 本，", font=FONT, font_size=26, color=WHITE)
        line2_left = Text("其中科普书占图书总数的", font=FONT, font_size=26, color=WHITE)
        frac_t = MathTex(r"\frac{3}{5}", font_size=32, color=color)
        line2_end = Text("，科普书有多少本？", font=FONT, font_size=26, color=WHITE)
        line2 = VGroup(line2_left, frac_t, line2_end).arrange(RIGHT, buff=0.1)
        prob_group = VGroup(line1, line2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        prob_group.move_to(UP * 4.3)
        self.play(FadeIn(prob_group, shift=DOWN * 0.2), run_time=0.7)

        # 可视化: 条形图 — 600本分成5等份，取3份
        bar_center = np.array([0.0, 2.5, 0.0])
        bar = self.make_bar(5, 3, color, bar_center)
        self.play(Create(bar), run_time=0.7)

        # 标注 "单位1" 与 "3/5"
        brace_all = self.make_brace_label(bar, "600本 (单位'1')", DOWN, COLOR_UNIT1, font_size=21)
        self.play(FadeIn(brace_all), run_time=0.5)

        brace_filled = self.make_brace_label(
            VGroup(*[bar[i] for i in range(3)]),
            "科普书 (3/5)", UP, color, font_size=21
        )
        self.play(FadeIn(brace_filled), run_time=0.5)
        self.wait(0.5)

        # 分析
        analysis_title = Text("分析：", font=FONT, font_size=26, color=COLOR_HL, weight=BOLD).move_to(UP * 0.9 + LEFT * 3.2)
        self.play(FadeIn(analysis_title), run_time=0.3)

        # 找单位'1'
        step_a1 = Text("单位", font=FONT, font_size=24, color=COLOR_UNIT1)
        step_a2 = Text("'1'", font=FONT, font_size=24, color=COLOR_UNIT1)
        step_a3 = Text("= 图书总数 = 600本", font=FONT, font_size=24, color=WHITE)
        step_a = VGroup(step_a1, step_a2, step_a3).arrange(RIGHT, buff=0.08)
        step_a.next_to(analysis_title, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(FadeIn(step_a, shift=RIGHT * 0.2), run_time=0.4)

        # 分率
        step_b1 = Text("分率 =", font=FONT, font_size=24, color=COLOR_FRAC)
        step_b2 = MathTex(r"\frac{3}{5}", font_size=32, color=COLOR_FRAC)
        step_b = VGroup(step_b1, step_b2).arrange(RIGHT, buff=0.15)
        step_b.next_to(step_a, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(FadeIn(step_b, shift=RIGHT * 0.2), run_time=0.4)

        self.wait(0.4)

        # 解题
        sol_title = Text("解：", font=FONT, font_size=26, color=COLOR_HL, weight=BOLD)
        sol_title.next_to(step_b, DOWN, buff=0.35, aligned_edge=LEFT)
        self.play(FadeIn(sol_title), run_time=0.3)

        sol_line_a1 = Text("科普书 =", font=FONT, font_size=24, color=WHITE)
        sol_line_a2 = Text("单位", font=FONT, font_size=24, color=COLOR_UNIT1)
        sol_line_a3 = Text("'1'", font=FONT, font_size=24, color=COLOR_UNIT1)
        sol_line_a4 = Text("的量", font=FONT, font_size=24, color=COLOR_UNIT1)
        sol_line_a5 = MathTex(r"\times", font_size=24, color=WHITE)
        sol_line_a6 = Text("分率", font=FONT, font_size=24, color=COLOR_FRAC)
        sol_line_a = VGroup(sol_line_a1, sol_line_a2, sol_line_a3, sol_line_a4, sol_line_a5, sol_line_a6).arrange(RIGHT, buff=0.08)
        sol_line_a.next_to(sol_title, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(FadeIn(sol_line_a, shift=RIGHT * 0.2), run_time=0.5)

        sol_line_b = MathTex(r"= 600 \times \frac{3}{5}", font_size=40)
        sol_line_b.next_to(sol_line_a, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(sol_line_b), run_time=0.5)

        sol_line_c_math = MathTex(r"= 360", font_size=40)
        sol_line_c_unit = Text("（本）", font=FONT, font_size=28, color=WHITE)
        sol_line_c = VGroup(sol_line_c_math, sol_line_c_unit).arrange(RIGHT, buff=0.15)
        sol_line_c_math.set_color(COLOR_TYPE3)
        sol_line_c.next_to(sol_line_b, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(sol_line_c), run_time=0.5)

        # 答案框
        ans_box = SurroundingRectangle(sol_line_c, color=COLOR_HL, buff=0.15, corner_radius=0.12)
        self.play(Create(ans_box), run_time=0.4)

        ans_text = Text("答：科普书有 360 本。", font=FONT, font_size=24, color=COLOR_TYPE3)
        ans_text.next_to(ans_box, DOWN, buff=0.25)
        self.play(FadeIn(ans_text, shift=UP * 0.2), run_time=0.4)

        self.wait(1.8)
        self.play(FadeOut(VGroup(
            type_label, op_label, prob_group, bar, brace_all, brace_filled,
            analysis_title, step_a, step_b, sol_title, sol_line_a,
            sol_line_b, sol_line_c, ans_box, ans_text
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 4: 类型2 — 除法 (已知几分之几是多少，求整体)
    # ------------------------------------------------------------------

    def scene_4_type2(self):
        color = COLOR_TYPE2

        type_label = Text(
            "② 已知几分之几，求整体",
            font=FONT, font_size=32, color=color, weight=BOLD
        ).move_to(UP * 5.8)
        op_label = Text("→ 用除法", font=FONT, font_size=26, color=WHITE).next_to(type_label, DOWN, buff=0.2)
        self.play(Write(type_label), FadeIn(op_label, shift=UP * 0.2), run_time=0.6)

        # 例题
        line1 = Text("小明读一本书，已读了全书的", font=FONT, font_size=26, color=WHITE)
        frac_t = MathTex(r"\frac{2}{5}", font_size=32, color=color)
        line1_end = Text("，", font=FONT, font_size=26, color=WHITE)
        row1 = VGroup(line1, frac_t, line1_end).arrange(RIGHT, buff=0.1)
        line2 = Text("已读了 48 页。这本书共有多少页？", font=FONT, font_size=26, color=WHITE)
        prob_group = VGroup(row1, line2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        prob_group.move_to(UP * 4.4)
        self.play(FadeIn(prob_group, shift=DOWN * 0.2), run_time=0.7)

        # 可视化: 条形图 — 5份，填2份(已读)
        bar_center = np.array([0.0, 2.6, 0.0])
        bar = self.make_bar(5, 2, color, bar_center)
        self.play(Create(bar), run_time=0.7)

        brace_filled = self.make_brace_label(
            VGroup(*[bar[i] for i in range(2)]),
            "已读 48页 (2/5)", UP, color, font_size=21
        )
        brace_all = self.make_brace_label(bar, "全书 = 单位'1' = ?", DOWN, COLOR_UNIT1, font_size=21)
        self.play(FadeIn(brace_filled), FadeIn(brace_all), run_time=0.5)
        self.wait(0.5)

        # 分析
        analysis_title = Text("分析：", font=FONT, font_size=26, color=COLOR_HL, weight=BOLD).move_to(UP * 0.9 + LEFT * 3.2)
        self.play(FadeIn(analysis_title), run_time=0.3)

        step_a1 = Text("单位", font=FONT, font_size=24, color=COLOR_UNIT1)
        step_a2 = Text("'1'", font=FONT, font_size=24, color=COLOR_UNIT1)
        step_a3 = Text("= 全书总页数 = 未知", font=FONT, font_size=24, color=WHITE)
        step_a = VGroup(step_a1, step_a2, step_a3).arrange(RIGHT, buff=0.08)
        step_a.next_to(analysis_title, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(FadeIn(step_a, shift=RIGHT * 0.2), run_time=0.4)

        step_b1 = Text("分率 =", font=FONT, font_size=24, color=COLOR_FRAC)
        step_b2 = MathTex(r"\frac{2}{5}", font_size=32, color=COLOR_FRAC)
        step_b3 = Text("，对应量 = 48页", font=FONT, font_size=24, color=COLOR_CORR)
        step_b = VGroup(step_b1, step_b2, step_b3).arrange(RIGHT, buff=0.12)
        step_b.next_to(step_a, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(FadeIn(step_b, shift=RIGHT * 0.2), run_time=0.4)

        # 关系推导
        derive1_a = Text("单位", font=FONT, font_size=22, color=COLOR_UNIT1)
        derive1_b = Text("'1'", font=FONT, font_size=22, color=COLOR_UNIT1)
        derive1_c = Text("的量 =", font=FONT, font_size=22, color=COLOR_UNIT1)
        derive1_d = Text("对应量", font=FONT, font_size=22, color=COLOR_CORR)
        derive1_e = MathTex(r"\div", font_size=22, color=WHITE)
        derive1_f = Text("分率", font=FONT, font_size=22, color=COLOR_FRAC)
        derive1 = VGroup(derive1_a, derive1_b, derive1_c, derive1_d, derive1_e, derive1_f).arrange(RIGHT, buff=0.08)
        derive1.next_to(step_b, DOWN, buff=0.28, aligned_edge=LEFT)
        self.play(FadeIn(derive1, shift=RIGHT * 0.2), run_time=0.4)

        sol_title = Text("解：", font=FONT, font_size=26, color=COLOR_HL, weight=BOLD)
        sol_title.next_to(derive1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(sol_title), run_time=0.3)

        sol_b = MathTex(r"= 48 \div \frac{2}{5}", font_size=40)
        sol_b.next_to(sol_title, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(sol_b), run_time=0.5)

        sol_c_math = MathTex(r"= 48 \times \frac{5}{2} = 120", font_size=38)
        sol_c_unit = Text("（页）", font=FONT, font_size=26, color=WHITE)
        sol_c = VGroup(sol_c_math, sol_c_unit).arrange(RIGHT, buff=0.15)
        sol_c_math.set_color(COLOR_TYPE3)
        sol_c.next_to(sol_b, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(sol_c), run_time=0.5)

        ans_box = SurroundingRectangle(sol_c, color=COLOR_HL, buff=0.15, corner_radius=0.12)
        self.play(Create(ans_box), run_time=0.4)

        ans_text = Text("答：这本书共有 120 页。", font=FONT, font_size=24, color=COLOR_TYPE3)
        ans_text.next_to(ans_box, DOWN, buff=0.25)
        self.play(FadeIn(ans_text, shift=UP * 0.2), run_time=0.4)

        self.wait(1.8)
        self.play(FadeOut(VGroup(
            type_label, op_label, prob_group, bar, brace_filled, brace_all,
            analysis_title, step_a, step_b, derive1, sol_title, sol_b,
            sol_c, ans_box, ans_text
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 5: 类型3 — 求一个数是另一个数的几分之几 (除法)
    # ------------------------------------------------------------------

    def scene_5_type3(self):
        color = COLOR_TYPE3

        type_label = Text(
            "③ 求一个数是另一个数的几分之几",
            font=FONT, font_size=30, color=color, weight=BOLD
        ).move_to(UP * 5.8)
        op_label = Text("→ 用除法", font=FONT, font_size=26, color=WHITE).next_to(type_label, DOWN, buff=0.2)
        self.play(Write(type_label), FadeIn(op_label, shift=UP * 0.2), run_time=0.6)

        # 例题
        line1 = Text("班级有男生 24 人，女生 30 人。", font=FONT, font_size=26, color=WHITE)
        line2 = Text("男生人数是女生人数的几分之几？", font=FONT, font_size=26, color=WHITE)
        prob_group = VGroup(line1, line2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        prob_group.move_to(UP * 4.5)
        self.play(FadeIn(prob_group, shift=DOWN * 0.2), run_time=0.7)

        # 可视化: 两条条形图对比 (对齐左端)
        bar_w_female = 6.0
        bar_w_male   = 6.0 * 24.0 / 30.0   # = 4.8
        bar_h = 0.75

        left_edge_x = -3.0  # 左端 x 坐标

        rect_female = Rectangle(
            width=bar_w_female, height=bar_h,
            fill_color="#475569", fill_opacity=0.85,
            stroke_color=WHITE, stroke_width=1.5
        )
        rect_female.move_to(
            np.array([left_edge_x + bar_w_female / 2, 3.0, 0.0])
        )

        rect_male = Rectangle(
            width=bar_w_male, height=bar_h,
            fill_color=color, fill_opacity=0.85,
            stroke_color=WHITE, stroke_width=1.5
        )
        rect_male.move_to(
            np.array([left_edge_x + bar_w_male / 2, 1.95, 0.0])
        )

        label_female = Text("女生 30人", font=FONT, font_size=20, color=GRAY_A)
        label_female.next_to(rect_female, LEFT, buff=0.18)
        label_male = Text("男生 24人", font=FONT, font_size=20, color=color)
        label_male.next_to(rect_male, LEFT, buff=0.18)

        self.play(Create(rect_female), FadeIn(label_female), run_time=0.5)
        self.play(Create(rect_male), FadeIn(label_male), run_time=0.5)

        # 分析
        analysis_title = Text("分析：", font=FONT, font_size=26, color=COLOR_HL, weight=BOLD).move_to(UP * 0.85 + LEFT * 3.2)
        self.play(FadeIn(analysis_title), run_time=0.3)

        step_a1 = Text("单位", font=FONT, font_size=24, color=COLOR_UNIT1)
        step_a2 = Text("'1'", font=FONT, font_size=24, color=COLOR_UNIT1)
        step_a3 = Text("= 女生人数 = 30人", font=FONT, font_size=24, color=WHITE)
        step_a = VGroup(step_a1, step_a2, step_a3).arrange(RIGHT, buff=0.08)
        step_a.next_to(analysis_title, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(FadeIn(step_a, shift=RIGHT * 0.2), run_time=0.4)

        step_b = Text("对应量 = 男生人数 = 24人", font=FONT, font_size=24, color=COLOR_CORR)
        step_b.next_to(step_a, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(FadeIn(step_b, shift=RIGHT * 0.2), run_time=0.4)

        # 关系推导
        derive_a = Text("分率 =", font=FONT, font_size=22, color=COLOR_FRAC)
        derive_b = Text("对应量", font=FONT, font_size=22, color=COLOR_CORR)
        derive_c = MathTex(r"\div", font_size=22, color=WHITE)
        derive_d = Text("单位", font=FONT, font_size=22, color=COLOR_UNIT1)
        derive_e = Text("'1'", font=FONT, font_size=22, color=COLOR_UNIT1)
        derive_f = Text("的量", font=FONT, font_size=22, color=COLOR_UNIT1)
        derive = VGroup(derive_a, derive_b, derive_c, derive_d, derive_e, derive_f).arrange(RIGHT, buff=0.08)
        derive.next_to(step_b, DOWN, buff=0.28, aligned_edge=LEFT)
        self.play(FadeIn(derive, shift=RIGHT * 0.2), run_time=0.4)

        sol_title = Text("解：", font=FONT, font_size=26, color=COLOR_HL, weight=BOLD)
        sol_title.next_to(derive, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(sol_title), run_time=0.3)

        sol_b = MathTex(r"24 \div 30 = \frac{24}{30} = \frac{4}{5}", font_size=40)
        sol_b.next_to(sol_title, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(sol_b), run_time=0.6)

        ans_box = SurroundingRectangle(sol_b, color=COLOR_HL, buff=0.15, corner_radius=0.12)
        self.play(Create(ans_box), run_time=0.4)

        ans_text = Text("答：男生人数是女生人数的五分之四。", font=FONT, font_size=23, color=color)
        ans_text.next_to(ans_box, DOWN, buff=0.25)
        self.play(FadeIn(ans_text, shift=UP * 0.2), run_time=0.4)

        self.wait(1.8)
        self.play(FadeOut(VGroup(
            type_label, op_label, prob_group,
            rect_female, label_female, rect_male, label_male,
            analysis_title, step_a, step_b, derive, sol_title, sol_b,
            ans_box, ans_text
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 6: 总结公式框
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = Text(
            "总结", font=FONT, font_size=48, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.5)

        # 核心公式大卡片
        core_bg = RoundedRectangle(
            width=8.0, height=2.0, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=2.5
        ).move_to(UP * 4.3)

        core_title = Text("核心关系式", font=FONT, font_size=26, color=COLOR_HL, weight=BOLD)

        ra = Text("单位", font=FONT, font_size=26, color=COLOR_UNIT1, weight=BOLD)
        rb = Text("'1'", font=FONT, font_size=26, color=COLOR_UNIT1, weight=BOLD)
        rc = Text("的量", font=FONT, font_size=26, color=COLOR_UNIT1, weight=BOLD)
        rx = MathTex(r"\times", font_size=30, color=WHITE)
        rd = Text("分率", font=FONT, font_size=26, color=COLOR_FRAC, weight=BOLD)
        req = MathTex(r"=", font_size=30, color=WHITE)
        re = Text("对应量", font=FONT, font_size=26, color=COLOR_CORR, weight=BOLD)
        core_row = VGroup(ra, rb, rc, rx, rd, req, re).arrange(RIGHT, buff=0.12)

        core_content = VGroup(core_title, core_row).arrange(DOWN, buff=0.35)
        core_content.move_to(core_bg.get_center())
        self.play(FadeIn(core_bg), Write(core_content), run_time=0.8)

        # 三类变形卡片
        types_data = [
            (COLOR_TYPE1, "① 求对应量",    "单位'1'的量 × 分率",   "→ 乘法"),
            (COLOR_TYPE2, "② 求单位'1'",   "对应量 ÷ 分率",        "→ 除法"),
            (COLOR_TYPE3, "③ 求分率",      "对应量 ÷ 单位'1'的量", "→ 除法"),
        ]
        y_positions = [2.5, 1.2, -0.1]

        type_cards = []
        for (c, label_str, formula_str, op_str), y in zip(types_data, y_positions):
            card_bg = RoundedRectangle(
                width=8.0, height=0.95, corner_radius=0.2,
                fill_color="#1e293b", fill_opacity=0.9,
                stroke_color=c, stroke_width=1.8
            ).move_to(UP * y)

            label = Text(label_str, font=FONT, font_size=22, color=c, weight=BOLD)
            formula = Text(formula_str, font=FONT, font_size=20, color=WHITE)
            op = Text(op_str, font=FONT, font_size=20, color=GRAY_A)
            row = VGroup(label, formula, op).arrange(RIGHT, buff=0.3)
            row.move_to(card_bg.get_center())

            card = VGroup(card_bg, row)
            type_cards.append(card)
            self.play(FadeIn(card, shift=LEFT * 0.3), run_time=0.35)

        self.wait(0.6)

        # 口诀框
        mnemonic_bg = RoundedRectangle(
            width=8.0, height=2.2, corner_radius=0.3,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2
        ).move_to(DOWN * 1.8)

        mnemonic_title = Text("记忆口诀", font=FONT, font_size=24, color=COLOR_HL, weight=BOLD)
        mnemonic_line1 = Text("找单位'1'：看\"占\"\"是\"后面的那个量", font=FONT, font_size=20, color=WHITE)
        mnemonic_line2 = Text("知整求部分 → 乘法", font=FONT, font_size=20, color=COLOR_TYPE1)
        mnemonic_line3 = Text("知部分求整 → 除法", font=FONT, font_size=20, color=COLOR_TYPE2)
        mnemonic_content = VGroup(
            mnemonic_title, mnemonic_line1, mnemonic_line2, mnemonic_line3
        ).arrange(DOWN, buff=0.2)
        mnemonic_content.move_to(mnemonic_bg.get_center())

        self.play(FadeIn(mnemonic_bg), Write(mnemonic_content), run_time=0.8)
        self.wait(2.0)

        self.play(FadeOut(VGroup(
            title, core_bg, core_content, *type_cards, mnemonic_bg, mnemonic_content
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        # 作者放大
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE, weight=BOLD
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=COLOR_AUTHOR
        ).move_to(UP * 1.0)

        self.play(Transform(self.author_mob, author_name), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=32, color=COLOR_HL
        ).move_to(ORIGIN)
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 装饰: 三个彩色卡片滑入
        deco_data = [
            (COLOR_TYPE1, "已知整体和分率 → 整体 × 分率 = 部分"),
            (COLOR_TYPE2, "已知部分和分率 → 部分 ÷ 分率 = 整体"),
            (COLOR_TYPE3, "已知部分和整体 → 部分 ÷ 整体 = 分率"),
        ]
        deco_cards = VGroup()
        for i, (c, txt) in enumerate(deco_data):
            bg = RoundedRectangle(
                width=7.8, height=0.8, corner_radius=0.18,
                fill_color="#1e293b", fill_opacity=0.85,
                stroke_color=c, stroke_width=1.5
            )
            txt_mob = Text(txt, font=FONT, font_size=18, color=c)
            txt_mob.move_to(bg.get_center())
            deco_cards.add(VGroup(bg, txt_mob))

        deco_cards.arrange(DOWN, buff=0.22)
        deco_cards.move_to(DOWN * 2.8)

        for card in deco_cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.3)

        self.wait(2.0)

        self.play(FadeOut(VGroup(
            self.author_mob, author_id, follow_text, deco_cards
        )), run_time=1.0)
