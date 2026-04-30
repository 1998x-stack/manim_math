"""
实数的运算 - Manim 教学动画
七年级第二学期 第十二章
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ── 颜色常量 ──────────────────────────────────────
COLOR_BG       = "#1a1a2e"
COLOR_ADD      = "#4fc3f7"   # 天蓝  — 加法
COLOR_MUL      = "#66bb6a"   # 绿    — 乘法
COLOR_SIMP     = "#ffd54f"   # 金黄  — 化简
COLOR_ABS      = "#ce93d8"   # 紫    — 绝对值
COLOR_LAW      = "#ff7043"   # 橙红  — 运算律
COLOR_RESULT   = "#80cbc4"   # 青绿  — 结果
COLOR_FORMULA  = "#ffd54f"
COLOR_AUTHOR   = "#78909c"
FONT = "PingFang SC"


class RealNumberOperations(Scene):
    """
    场景顺序:
    1. 开场钩子   — 实数运算不神秘
    2. 加减运算   — 同类项合并（含无理数）
    3. 乘除运算   — √a × √b = √(ab)
    4. 化简运算   — √8 = 2√2 等
    5. 绝对值     — |a| 的计算
    6. 运算律汇总
    7. 综合例题
    8. 总结+片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG
        self.scene_opening()
        self.scene_add_sub()
        self.scene_mul_div()
        self.scene_simplify()
        self.scene_abs_value()
        self.scene_laws()
        self.scene_combined()
        self.scene_outro()

    # ══════════════════════════════════════════════
    # 工具：创建带标题的公式卡片
    # ══════════════════════════════════════════════
    def make_card(self, title_str, formula_str, color, pos,
                  card_w=7.5, card_h=1.1):
        box = RoundedRectangle(
            width=card_w, height=card_h, corner_radius=0.14,
            color=color, fill_color=color, fill_opacity=0.15, stroke_width=2
        ).move_to(pos)
        title = Text(title_str, font=FONT, font_size=22, color=color)
        formula = MathTex(formula_str, font_size=32, color=WHITE)
        grp = VGroup(title, formula).arrange(RIGHT, buff=0.4)
        grp.move_to(pos)
        return VGroup(box, grp)

    # ══════════════════════════════════════════════
    # Scene 1  开场钩子
    # ══════════════════════════════════════════════
    def scene_opening(self):
        author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=20, color=COLOR_AUTHOR
        ).move_to(UP * 7.3)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author_obj = author

        title = Text("实数的运算", font=FONT, font_size=50, color=GOLD)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.7)

        # 展示几个运算表达式飞入
        exprs = [
            (r"\sqrt{2} + 3\sqrt{2}",          LEFT*2.8 + UP*4.8,  COLOR_ADD),
            (r"\sqrt{2} \times \sqrt{3}",       RIGHT*1.5 + UP*4.8, COLOR_MUL),
            (r"\sqrt{8} = 2\sqrt{2}",           LEFT*2.5 + UP*3.8,  COLOR_SIMP),
            (r"|-\sqrt{3}| = \sqrt{3}",         RIGHT*1.8 + UP*3.8, COLOR_ABS),
        ]
        mobs = []
        for tex, pos, col in exprs:
            m = MathTex(tex, font_size=34, color=col).move_to(pos)
            mobs.append(m)
            self.play(FadeIn(m, scale=0.7), run_time=0.3)

        hook = Text("有理数的运算法则对实数同样适用！",
                    font=FONT, font_size=26, color=YELLOW)
        hook.move_to(UP * 2.6)
        box_h = SurroundingRectangle(hook, color=YELLOW, buff=0.18, corner_radius=0.1)
        self.play(FadeIn(hook), Create(box_h), run_time=0.6)
        self.wait(0.8)

        self.play(FadeOut(VGroup(title, *mobs, hook, box_h)), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 2  加减运算
    # ══════════════════════════════════════════════
    def scene_add_sub(self):
        sec = Text("加减运算", font=FONT, font_size=38, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        rule = Text("合并同类项（根号相同才能合并）",
                    font=FONT, font_size=26, color=COLOR_ADD)
        rule.move_to(UP * 6.0)
        self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.4)

        # 例1: 3√2 + 5√2 = 8√2
        steps_1 = [
            (r"3\sqrt{2} + 5\sqrt{2}", UP * 4.8),
            (r"= (3+5)\sqrt{2}",        UP * 3.8),
            (r"= 8\sqrt{2}",            UP * 3.8),
        ]
        self._play_steps(steps_1, COLOR_ADD, label="例1")

        # 例2: √3 + √2（不能合并）
        ex2_title = Text("例2", font=FONT, font_size=22, color=GRAY_A)
        ex2_title.move_to(LEFT * 3.5 + UP * 2.5)
        eq2 = MathTex(r"\sqrt{3} + \sqrt{2}", font_size=36, color=WHITE)
        eq2.move_to(UP * 2.5)
        self.play(FadeIn(ex2_title), Write(eq2), run_time=0.4)

        note2_part1 = MathTex(r"\sqrt{3}", font_size=30, color=COLOR_ADD)
        note2_and   = Text("和", font=FONT, font_size=24, color=WHITE)
        note2_part2 = MathTex(r"\sqrt{2}", font_size=30, color=COLOR_MUL)
        note2_end   = Text("是不同类项，不能合并", font=FONT, font_size=24, color=WHITE)
        note2 = VGroup(note2_part1, note2_and, note2_part2, note2_end).arrange(RIGHT, buff=0.12)
        note2.move_to(UP * 1.6)
        self.play(FadeIn(note2, shift=UP * 0.2), run_time=0.5)

        # 例3: 2√3 - 5√3 + √3
        ex3_title = Text("例3", font=FONT, font_size=22, color=GRAY_A)
        ex3_title.move_to(LEFT * 3.5 + UP * 0.5)
        step3a = MathTex(r"2\sqrt{3} - 5\sqrt{3} + \sqrt{3}", font_size=34, color=WHITE)
        step3a.move_to(UP * 0.5)
        step3b = MathTex(r"= (2 - 5 + 1)\sqrt{3} = -2\sqrt{3}", font_size=34,
                          color=COLOR_RESULT)
        step3b.move_to(DOWN * 0.4)
        self.play(FadeIn(ex3_title), Write(step3a), run_time=0.4)
        self.play(Write(step3b), run_time=0.6)

        tip = Text("关键：根号内相同才是同类项",
                   font=FONT, font_size=24, color=YELLOW)
        tip.move_to(DOWN * 1.5)
        box_tip = SurroundingRectangle(tip, color=YELLOW, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(tip), Create(box_tip), run_time=0.4)
        self.wait(1.2)

        # 构建要移除的对象列表
        mobjs_to_remove = [sec, rule, ex2_title, eq2, note2,
                          ex3_title, step3a, step3b, tip, box_tip]
        # 添加其他不在排除列表中的对象
        excluded = (sec, rule, ex2_title, eq2, note2,
                   ex3_title, step3a, step3b, tip, box_tip)
        additional_mobjs = [m for m in self.mobjects
                           if m is not self.author_obj and m not in excluded]
        mobjs_to_remove.extend(additional_mobjs)
        
        if mobjs_to_remove:
            self.play(FadeOut(Group(*mobjs_to_remove)), run_time=0.5)

    def _play_steps(self, steps, color, label="例1"):
        lbl = Text(label, font=FONT, font_size=22, color=GRAY_A)
        lbl.move_to(LEFT * 3.5 + steps[0][1])
        self.play(FadeIn(lbl), run_time=0.2)

        prev = None
        for i, (tex, pos) in enumerate(steps):
            mob = MathTex(tex, font_size=36, color=WHITE if i < len(steps)-1 else color)
            mob.move_to(pos)
            if prev is None:
                self.play(Write(mob), run_time=0.5)
            elif i == len(steps) - 1:
                self.play(ReplacementTransform(prev, mob), run_time=0.6)
            else:
                self.play(Write(mob), run_time=0.5)
            prev = mob

    # ══════════════════════════════════════════════
    # Scene 3  乘除运算
    # ══════════════════════════════════════════════
    def scene_mul_div(self):
        # 清屏
        # 清屏
        mobjs_to_fade = [m for m in self.mobjects if m is not self.author_obj]
        if mobjs_to_fade:
            self.play(*[FadeOut(m) for m in mobjs_to_fade], run_time=0.3)

        sec = Text("乘除运算", font=FONT, font_size=38, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        # 核心公式
        rule_box = RoundedRectangle(
            width=7.8, height=1.5, corner_radius=0.15,
            color=COLOR_MUL, fill_color=COLOR_MUL, fill_opacity=0.15, stroke_width=2
        ).move_to(UP * 5.8)
        rule_1 = MathTex(r"\sqrt{a} \times \sqrt{b} = \sqrt{ab}", font_size=34, color=COLOR_MUL)
        rule_sep = Text("  |  ", font=FONT, font_size=28, color=GRAY)
        rule_2 = MathTex(
            r"\frac{\sqrt{a} }{\sqrt{b} } = \sqrt{ \frac{a}{b} }",
            font_size=34,
            color=COLOR_MUL
        )
        rule_row = VGroup(rule_1, rule_sep, rule_2).arrange(RIGHT, buff=0.3)
        rule_row.move_to(rule_box.get_center())
        cond = Text("(a≥0, b>0)", font=FONT, font_size=20, color=GRAY_A)
        cond.next_to(rule_box, DOWN, buff=0.1)

        self.play(Create(rule_box), Write(rule_row), run_time=0.7)
        self.play(FadeIn(cond), run_time=0.3)

        # 例1: √2 × √3 = √6
        examples = [
            # (左式, 右式, 过程色)
            (r"\sqrt{2} \times \sqrt{3}",
            r"= \sqrt{2 \times 3} = \sqrt{6}",
            COLOR_MUL),
            (r"\sqrt{3} \times \sqrt{3}",
            r"= \sqrt{9} = 3",
            COLOR_RESULT),
            (r"\frac{\sqrt{12} }{\sqrt{3} }",  # Added spaces between braces
            r"= \sqrt{\frac{12}{3}} = \sqrt{4} = 2",
            COLOR_MUL),
            (r"2\sqrt{5} \times 3\sqrt{5}",
            r"= 6 \times 5 = 30",
            COLOR_RESULT),
        ]

        all_ex = VGroup()
        for i, (lhs, rhs, col) in enumerate(examples):
            y = 4.0 - i * 1.0
            lhs_m = MathTex(lhs, font_size=30, color=WHITE)
            lhs_m.move_to(LEFT * 1.8 + UP * y)
            arr = Arrow(lhs_m.get_right() + RIGHT * 0.1,
                        lhs_m.get_right() + RIGHT * 0.5,
                        color=GRAY, buff=0.02, stroke_width=2,
                        max_tip_length_to_length_ratio=0.4)
            rhs_m = MathTex(rhs, font_size=30, color=col)
            rhs_m.next_to(arr, RIGHT, buff=0.1)
            self.play(Write(lhs_m), run_time=0.3)
            self.play(Create(arr), Write(rhs_m), run_time=0.4)
            all_ex.add(lhs_m, arr, rhs_m)

        self.wait(1.2)
        self.play(FadeOut(Group(sec, rule_box, rule_row, cond, all_ex)), run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 4  化简运算
    # ══════════════════════════════════════════════
    def scene_simplify(self):
        sec = Text("化简根式", font=FONT, font_size=38, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        tip = Text("把被开方数中的完全平方数提取出来",
                   font=FONT, font_size=24, color=COLOR_SIMP)
        tip.move_to(UP * 6.1)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.4)

        # √8 = 2√2 详细推导
        deriv_title = Text("推导", font=FONT, font_size=22, color=GRAY_A)
        deriv_title.move_to(LEFT * 3.6 + UP * 5.0)
        self.play(FadeIn(deriv_title), run_time=0.2)

        steps = [
            (r"\sqrt{8}",                    WHITE),
            (r"= \sqrt{4 \times 2}",          WHITE),
            (r"= \sqrt{4} \times \sqrt{2}",   WHITE),
            (r"= 2\sqrt{2}",                  COLOR_SIMP),
        ]
        y = 5.0
        prev = None
        for i, (tex, col) in enumerate(steps):
            m = MathTex(tex, font_size=40, color=col)
            m.move_to(UP * y)
            if prev is None:
                self.play(Write(m), run_time=0.4)
            else:
                down = MathTex(tex, font_size=40, color=col).move_to(UP * (y - 0.9 * i))
                self.play(Write(down), run_time=0.4)
                m = down
            prev = m

        # 更多例子
        simplify_examples = [
            (r"\sqrt{12} = 2\sqrt{3}",    r"\sqrt{4 \times 3}"),
            (r"\sqrt{18} = 3\sqrt{2}",    r"\sqrt{9 \times 2}"),
            (r"\sqrt{50} = 5\sqrt{2}",    r"\sqrt{25 \times 2}"),
            (r"\sqrt{75} = 5\sqrt{3}",    r"\sqrt{25 \times 3}"),
        ]

        all_s = VGroup()
        for i, (result, process) in enumerate(simplify_examples):
            y = 1.5 - i * 0.95
            res_m = MathTex(result, font_size=30, color=COLOR_SIMP)
            res_m.move_to(LEFT * 0.8 + UP * y)
            proc_m = MathTex(process, font_size=26, color=GRAY_A)
            proc_m.next_to(res_m, RIGHT, buff=0.4)
            self.play(Write(res_m), FadeIn(proc_m, shift=LEFT*0.1), run_time=0.4)
            all_s.add(res_m, proc_m)

        rule_box = RoundedRectangle(
            width=7.5, height=0.75, corner_radius=0.12,
            color=COLOR_SIMP, fill_color=COLOR_SIMP, fill_opacity=0.15, stroke_width=1.5
        ).move_to(DOWN * 2.5)
        rule_t1 = MathTex(r"\sqrt{a^2 b} = a\sqrt{b}", font_size=32, color=COLOR_SIMP)
        rule_t1.move_to(rule_box.get_center())
        self.play(Create(rule_box), Write(rule_t1), run_time=0.5)
        self.wait(1.2)

        mobjs_to_fade = [m for m in self.mobjects if m is not self.author_obj]
        if mobjs_to_fade:
            self.play(*[FadeOut(m) for m in mobjs_to_fade], run_time=0.4)

    # ══════════════════════════════════════════════
    # Scene 5  绝对值运算
    # ══════════════════════════════════════════════
    def scene_abs_value(self):
        sec = Text("绝对值运算", font=FONT, font_size=38, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        # 定义
        defn_box = RoundedRectangle(
            width=7.8, height=2.2, corner_radius=0.15,
            color=COLOR_ABS, fill_color=COLOR_ABS, fill_opacity=0.12, stroke_width=2
        ).move_to(UP * 5.5)
        defn_tex = MathTex(
            r"|a| = \begin{cases} a & (a > 0) \\ 0 & (a = 0) \\ -a & (a < 0) \end{cases}",
            font_size=32, color=WHITE
        )
        defn_tex.move_to(defn_box.get_center())
        self.play(Create(defn_box), Write(defn_tex), run_time=0.8)

        # 例题
        abs_examples = [
            # (题干MathTex, 答案MathTex)
            (r"|\sqrt{2} - 1|",      r"= \sqrt{2} - 1",    r"(\sqrt{2} > 1)"),
            (r"|3 - \sqrt{10}|",     r"= \sqrt{10} - 3",   r"(\sqrt{10} > 3)"),
            (r"|-\sqrt{5}|",         r"= \sqrt{5}",         r""),
            (r"|2 - \sqrt{5}|",      r"= \sqrt{5} - 2",    r"(\sqrt{5} > 2)"),
        ]

        all_abs = VGroup()
        for i, (prob, ans, note) in enumerate(abs_examples):
            y = 3.5 - i * 1.0
            prob_m = MathTex(prob, font_size=30, color=WHITE)
            prob_m.move_to(LEFT * 2.0 + UP * y)
            ans_m = MathTex(ans, font_size=30, color=COLOR_ABS)
            ans_m.next_to(prob_m, RIGHT, buff=0.2)
            mobs = [prob_m, ans_m]
            if note:
                note_m = MathTex(note, font_size=22, color=GRAY_A)
                note_m.next_to(ans_m, RIGHT, buff=0.2)
                mobs.append(note_m)
            self.play(*[Write(m) for m in mobs], run_time=0.45)
            all_abs.add(*mobs)

        # 常用不等式提示
        cmp = Text("常用大小比较", font=FONT, font_size=22, color=YELLOW)
        cmp.move_to(DOWN * 1.2)
        cmp_vals = MathTex(
            r"\sqrt{2} \approx 1.414,\quad \sqrt{3} \approx 1.732,\quad \sqrt{5} \approx 2.236",
            font_size=26, color=YELLOW
        )
        cmp_vals.move_to(DOWN * 2.0)
        self.play(FadeIn(cmp), Write(cmp_vals), run_time=0.5)
        self.wait(1.3)

        mobjs_to_fade = [m for m in self.mobjects if m is not self.author_obj]
        if mobjs_to_fade:
            self.play(*[FadeOut(m) for m in mobjs_to_fade], run_time=0.4)

    # ══════════════════════════════════════════════
    # Scene 6  运算律汇总
    # ══════════════════════════════════════════════
    def scene_laws(self):
        sec = Text("实数运算律（与有理数相同）",
                   font=FONT, font_size=32, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        laws = [
            # (名称, 公式)
            ("加法交换律",  r"a + b = b + a"),
            ("加法结合律",  r"(a+b)+c = a+(b+c)"),
            ("乘法交换律",  r"a \times b = b \times a"),
            ("乘法结合律",  r"(ab)c = a(bc)"),
            ("分配律",      r"a(b+c) = ab + ac"),
        ]

        law_colors = [COLOR_ADD, COLOR_ADD, COLOR_MUL, COLOR_MUL, COLOR_LAW]
        all_laws = VGroup()
        for i, ((name, formula), col) in enumerate(zip(laws, law_colors)):
            y = 5.8 - i * 1.05
            name_t = Text(name, font=FONT, font_size=24, color=col)
            name_t.move_to(LEFT * 2.8 + UP * y)
            sep = Text("：", font=FONT, font_size=24, color=GRAY)
            sep.next_to(name_t, RIGHT, buff=0.05)
            formula_m = MathTex(formula, font_size=30, color=WHITE)
            formula_m.next_to(sep, RIGHT, buff=0.1)
            row = VGroup(name_t, sep, formula_m)
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.4)
            all_laws.add(row)

        # 无理数参与例子
        eg_title = Text("无理数也满足运算律", font=FONT, font_size=26, color=YELLOW)
        eg_title.move_to(DOWN * 0.2)
        self.play(FadeIn(eg_title, shift=UP * 0.2), run_time=0.4)

        eg = MathTex(
            r"\sqrt{2}(\sqrt{3} + \sqrt{2}) = \sqrt{6} + 2",
            font_size=32, color=COLOR_LAW
        )
        eg.move_to(DOWN * 1.2)
        box_eg = SurroundingRectangle(eg, color=COLOR_LAW, buff=0.15, corner_radius=0.1)
        self.play(Write(eg), Create(box_eg), run_time=0.6)
        self.wait(1.2)

        mobjs_to_fade = [m for m in self.mobjects if m is not self.author_obj]
        if mobjs_to_fade:
            self.play(*[FadeOut(m) for m in mobjs_to_fade], run_time=0.4)

    # ══════════════════════════════════════════════
    # Scene 7  综合例题
    # ══════════════════════════════════════════════
    def scene_combined(self):
        sec = Text("综合例题", font=FONT, font_size=38, color=GOLD)
        sec.move_to(UP * 7.0)
        self.play(Write(sec), run_time=0.5)

        # 题目
        prob_label = Text("计算：", font=FONT, font_size=26, color=GRAY_A)
        prob_label.move_to(LEFT * 3.2 + UP * 6.1)
        prob = MathTex(
            r"(\sqrt{3} + \sqrt{2})(\sqrt{3} - \sqrt{2})",
            font_size=36, color=WHITE
        )
        prob.move_to(UP * 6.1)
        self.play(FadeIn(prob_label), Write(prob), run_time=0.5)

        # 逐步展开
        step_data = [
            (r"= (\sqrt{3})^2 - (\sqrt{2})^2", "平方差公式"),
            (r"= 3 - 2",                         ""),
            (r"= 1",                              ""),
        ]
        y = 5.0
        prev_mob = prob
        step_mobs = []
        for tex, hint in step_data:
            y -= 1.0
            step_m = MathTex(tex, font_size=36,
                              color=COLOR_RESULT if tex == r"= 1" else WHITE)
            step_m.move_to(UP * y)
            if hint:
                hint_t = Text(hint, font=FONT, font_size=20, color=GRAY_A)
                hint_t.next_to(step_m, RIGHT, buff=0.3)
                self.play(Write(step_m), FadeIn(hint_t, shift=LEFT*0.1), run_time=0.5)
                step_mobs.extend([step_m, hint_t])
            else:
                self.play(Write(step_m), run_time=0.4)
                step_mobs.append(step_m)

        # 高亮结果
        result_box = SurroundingRectangle(
            step_mobs[-1], color=COLOR_RESULT, buff=0.2, corner_radius=0.1
        )
        self.play(Create(result_box), run_time=0.4)
        self.play(Flash(step_mobs[-1], color=COLOR_RESULT, flash_radius=0.4), run_time=0.4)

        # 第二道题
        prob2_label = Text("计算：", font=FONT, font_size=26, color=GRAY_A)
        prob2_label.move_to(LEFT * 3.2 + UP * 1.5)
        prob2 = MathTex(
            r"\sqrt{2} \times \sqrt{8} + \sqrt{3} \times \sqrt{3}",
            font_size=32, color=WHITE
        )
        prob2.move_to(UP * 1.5)
        self.play(FadeIn(prob2_label), Write(prob2), run_time=0.5)

        step2a = MathTex(r"= \sqrt{16} + 3", font_size=32, color=WHITE)
        step2a.move_to(UP * 0.5)
        step2b = MathTex(r"= 4 + 3 = 7", font_size=36, color=COLOR_RESULT)
        step2b.move_to(DOWN * 0.4)
        self.play(Write(step2a), run_time=0.4)
        self.play(Write(step2b), run_time=0.4)
        box2 = SurroundingRectangle(step2b, color=COLOR_RESULT, buff=0.2, corner_radius=0.1)
        self.play(Create(box2), run_time=0.3)

        self.wait(1.5)
        mobjs_to_fade = [m for m in self.mobjects if m is not self.author_obj]
        if mobjs_to_fade:
            self.play(*[FadeOut(m) for m in mobjs_to_fade], run_time=0.5)

    # ══════════════════════════════════════════════
    # Scene 8  总结+片尾
    # ══════════════════════════════════════════════
    def scene_outro(self):
        sum_title = Text("本节要点", font=FONT, font_size=36, color=GOLD)
        sum_title.move_to(UP * 7.0)
        self.play(Write(sum_title), run_time=0.4)

        # 每条: ("math"/"text"/"mixed", 内容, 颜色)
        points = [
            ("text",  "有理数运算律对实数完全适用",          COLOR_LAW),
            ("math",  r"\sqrt{a}\cdot\sqrt{b}=\sqrt{ab}",   COLOR_MUL),
            ("math",  r"\sqrt{a^2 b}=a\sqrt{b}",            COLOR_SIMP),
            ("mixed", (r"\sqrt{a}\pm\sqrt{b}", "：根号内不同，不能合并"),   COLOR_ADD),
            ("math",  r"|a| \geq 0",                         COLOR_ABS),
        ]

        point_mobs = VGroup()
        for i, (kind, content, col) in enumerate(points):
            y = 5.8 - i * 1.1
            if kind == "math":
                mob = MathTex(content, font_size=30, color=col)
            elif kind == "mixed":
                m_p = MathTex(content[0], font_size=30, color=col)
                t_p = Text(content[1], font=FONT, font_size=22, color=col)
                mob = VGroup(m_p, t_p).arrange(RIGHT, buff=0.12)
            else:
                mob = Text(content, font=FONT, font_size=24, color=col)
            mob.move_to(UP * y + RIGHT * 0.4)
            mob.align_to(LEFT * 0.3, LEFT)
            dot = Dot(radius=0.07, color=col).next_to(mob, LEFT, buff=0.2)
            grp = VGroup(dot, mob)
            point_mobs.add(grp)
            self.play(FadeIn(grp, shift=RIGHT * 0.2), run_time=0.35)

        self.wait(1.5)
        self.play(FadeOut(VGroup(sum_title, point_mobs)), run_time=0.5)

        # 片尾
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=40, color=WHITE)
        author_big.move_to(UP * 2.0)
        author_id = Text("@emptyandcalm", font=FONT, font_size=30, color=COLOR_AUTHOR)
        author_id.next_to(author_big, DOWN, buff=0.3)
        self.play(Transform(self.author_obj, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text("关注我，获得更多数学技巧！", font=FONT, font_size=30, color=YELLOW)
        follow.move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        finale = MathTex(
            r"\sqrt{2} \times \sqrt{3} = \sqrt{6}",
            font_size=42, color=COLOR_MUL
        )
        finale.move_to(DOWN * 2.2)
        self.play(Write(finale), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(Group(
            self.author_obj, author_id, follow, finale
        )), run_time=0.8)


# 渲染:
#   manim -pql real_number_ops.py RealNumberOperations
#   manim -qh  real_number_ops.py RealNumberOperations