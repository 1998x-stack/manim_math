"""
解一元一次方程 - Solving Linear Equations Step by Step
六年级数学教学动画

例题: (x+2)/3 - (x-1)/2 = 1
验证: x=1 时 (1+2)/3 - (1-1)/2 = 1 - 0 = 1 ✓

目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置 - TikTok 竖屏
# ============================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ============================================================
# 颜色常量
# ============================================================
BG_COLOR    = "#1a1a2e"
COLOR_X     = "#e74c3c"    # 红色  — 未知数 x
COLOR_STEP  = "#3498db"    # 蓝色  — 步骤
COLOR_OP    = "#f39c12"    # 橙色  — 操作
COLOR_OK    = "#2ecc71"    # 绿色  — 正确
COLOR_MOVED = "#9b59b6"    # 紫色  — 移项
COLOR_CARD  = "#16213e"    # 深蓝  — 卡片
FONT        = "PingFang SC"

# ============================================================
# 全局字体大小
# ============================================================
FS_TITLE  = 32   # 场景标题
FS_STEP   = 26   # 步骤说明
FS_EQ     = 44   # 方程主体
FS_EQ_SM  = 36   # 较小方程
FS_ANNOT  = 22   # 注释
FS_BODY   = 24   # 正文


# ============================================================
# 辅助：创建步骤编号徽章
# ============================================================
def step_badge(number, label_cn, color=COLOR_STEP):
    """返回 VGroup: 圆形编号 + 文字说明"""
    circle = Circle(radius=0.32, fill_color=color, fill_opacity=1,
                    stroke_width=0)
    num = Text(str(number), font=FONT, font_size=22,
               color=WHITE).move_to(circle.get_center())
    badge = VGroup(circle, num)
    label = Text(label_cn, font=FONT, font_size=FS_STEP, color=color)
    return VGroup(badge, label).arrange(RIGHT, buff=0.25)


def make_card(mob, stroke_color=WHITE, fill_color=COLOR_CARD,
              buff=0.22, radius=0.15):
    return SurroundingRectangle(
        mob,
        fill_color=fill_color,
        fill_opacity=0.85,
        stroke_color=stroke_color,
        stroke_width=2.5,
        buff=buff,
        corner_radius=radius
    )


# ============================================================
# 主场景
# ============================================================
class SolveLinearEquation(Scene):

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 顶部作者信息（全程保留）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.add(self.author)

        self.scene_hook()
        self.scene_roadmap()
        self.scene_step1_clear_fractions()
        self.scene_step2_expand_brackets()
        self.scene_step3_transpose()
        self.scene_step4_combine()
        self.scene_step5_coeff_to_one()
        self.scene_verify()
        self.scene_summary()
        self.scene_outro()

    # ----------------------------------------------------------
    # Scene 1: 开场钩子
    # ----------------------------------------------------------
    def scene_hook(self):
        hook = Text(
            "这道方程，你会解吗？",
            font=FONT, font_size=34, color=YELLOW
        ).move_to(UP * 5.9)

        # 原方程
        eq_orig = MathTex(
            r"\frac{x+2}{3} - \frac{x-1}{2} = 1",
            font_size=FS_EQ + 4
        ).move_to(UP * 4.2)
        eq_orig.set_color_by_tex("x", COLOR_X)

        tag_line = VGroup(
            Text("看起来很难？", font=FONT, font_size=26, color=GRAY_A),
            Text("其实只需", font=FONT, font_size=26, color=WHITE),
            Text("5 步", font=FONT, font_size=28, color=COLOR_OK),
            Text("就能搞定！", font=FONT, font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.18).move_to(UP * 2.8)

        self.play(Write(hook), run_time=0.7)
        self.play(Write(eq_orig), run_time=1.0)
        self.play(FadeIn(tag_line, shift=UP * 0.2), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(hook), FadeOut(tag_line),
            run_time=0.4
        )
        # 原方程缩小移到顶部，全程跟随
        self.eq_orig_top = MathTex(
            r"\frac{x+2}{3} - \frac{x-1}{2} = 1",
            font_size=28, color=GRAY_B
        ).move_to(UP * 6.4)

        self.play(
            ReplacementTransform(eq_orig, self.eq_orig_top),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 2: 5步路线图
    # ----------------------------------------------------------
    def scene_roadmap(self):
        title = Text("解方程的 5 个步骤", font=FONT,
                     font_size=FS_TITLE, color=GOLD).move_to(UP * 5.5)

        steps_data = [
            ("①", "去分母", COLOR_STEP),
            ("②", "去括号", "#1abc9c"),
            ("③", "移项",   COLOR_MOVED),
            ("④", "合并同类项", COLOR_OP),
            ("⑤", "系数化为 1", COLOR_OK),
        ]
        y_start = 4.2
        cards = []
        for i, (num, label, col) in enumerate(steps_data):
            badge = step_badge(num, label, color=col)
            badge.move_to(UP * (y_start - i * 1.1))
            bg = make_card(badge, stroke_color=col,
                           fill_color=COLOR_CARD, buff=0.18)
            cards.append(VGroup(bg, badge))

        self.play(Write(title), run_time=0.5)
        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.3)
        self.wait(1.0)

        self.play(
            FadeOut(title),
            *[FadeOut(c) for c in cards],
            run_time=0.5
        )

    # ----------------------------------------------------------
    # 内部：步骤标题条
    # ----------------------------------------------------------
    def _show_step_banner(self, num_str, label_cn, color):
        banner = step_badge(num_str, label_cn, color=color)
        banner.move_to(UP * 5.7)
        self.play(FadeIn(banner, shift=DOWN * 0.2), run_time=0.4)
        return banner

    # ----------------------------------------------------------
    # Scene 3: 步骤① 去分母
    # ----------------------------------------------------------
    def scene_step1_clear_fractions(self):
        banner = self._show_step_banner("①", "去分母", COLOR_STEP)

        # 显示原方程
        eq0 = MathTex(
            r"\frac{x+2}{3} - \frac{x-1}{2} = 1",
            font_size=FS_EQ
        ).move_to(UP * 4.3)

        # 高亮分母
        denom_note = VGroup(
            Text("分母有 3 和 2", font=FONT, font_size=FS_ANNOT, color=COLOR_OP),
        ).move_to(UP * 3.3)

        lcm_text = VGroup(
            Text("最小公倍数", font=FONT, font_size=FS_ANNOT, color=WHITE),
            MathTex(r"\text{LCM}(3,2) = 6", font_size=FS_ANNOT + 4, color=COLOR_OP),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.6)

        op_note = VGroup(
            Text("两边同乘 6", font=FONT, font_size=FS_STEP, color=COLOR_OP),
        ).move_to(UP * 1.8)

        down_arr = MathTex(r"\Downarrow", font_size=36,
                           color=COLOR_STEP).move_to(UP * 1.0)

        # 结果：去掉分母
        eq1 = MathTex(
            r"2(x+2) - 3(x-1) = 6",
            font_size=FS_EQ
        ).move_to(UP * 0.1)

        eq1_bg = make_card(eq1, stroke_color=COLOR_STEP)

        self.play(Write(eq0), run_time=0.8)
        self.play(FadeIn(denom_note), run_time=0.4)
        self.play(FadeIn(lcm_text), run_time=0.5)
        self.play(FadeIn(op_note), run_time=0.4)
        self.play(FadeIn(down_arr), run_time=0.3)
        self.play(Write(eq1), Create(eq1_bg), run_time=0.8)

        # 解释：6÷3=2, 6÷2=3
        annot = VGroup(
            Text("6 ÷ 3 = 2，所以 (x+2) 系数为 2", font=FONT,
                 font_size=19, color=GRAY_A),
            Text("6 ÷ 2 = 3，所以 (x-1) 系数为 3", font=FONT,
                 font_size=19, color=GRAY_A),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 1.1)

        self.play(FadeIn(annot), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(banner), FadeOut(eq0), FadeOut(denom_note),
            FadeOut(lcm_text), FadeOut(op_note), FadeOut(down_arr),
            FadeOut(eq1_bg), FadeOut(annot),
            run_time=0.4
        )
        # eq1 移到顶部作为"当前进度"
        self.current_eq = eq1
        self._park_eq(eq1, label="去分母后")

    def _park_eq(self, eq, label=""):
        """将方程缩小停放在进度区 (y≈-0.5)，不做动画"""
        pass  # 我们直接在各场景顶部重建"当前状态"

    # ----------------------------------------------------------
    # Scene 4: 步骤② 去括号
    # ----------------------------------------------------------
    def scene_step2_expand_brackets(self):
        banner = self._show_step_banner("②", "去括号", "#1abc9c")

        # 上方显示上一步结果
        prev = MathTex(
            r"2(x+2) - 3(x-1) = 6",
            font_size=FS_EQ_SM, color=GRAY_A
        ).move_to(UP * 4.5)

        self.play(Write(prev), run_time=0.6)

        # 展开过程
        expand_title = Text(
            "按乘法分配律展开括号",
            font=FONT, font_size=FS_ANNOT, color=COLOR_OP
        ).move_to(UP * 3.6)

        # 展开 2(x+2)
        exp1_lhs = MathTex(
            r"2(x+2) = 2x + 4",
            font_size=FS_EQ_SM, color=WHITE
        ).move_to(UP * 2.7)
        exp1_lhs[0][0].set_color(COLOR_OP)   # 系数 2

        # 展开 -3(x-1)，注意负号
        exp2_rhs = MathTex(
            r"-3(x-1) = -3x + 3",
            font_size=FS_EQ_SM, color=WHITE
        ).move_to(UP * 1.8)
        exp2_rhs[0][1].set_color(COLOR_OP)   # 系数 -3

        warn = VGroup(
            Text("⚠", font=FONT, font_size=22, color=YELLOW),
            Text("负号 × 负号 = 正号", font=FONT,
                 font_size=20, color=YELLOW),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.1)

        down_arr = MathTex(r"\Downarrow", font_size=36,
                           color="#1abc9c").move_to(UP * 0.4)

        # 结果
        eq2 = MathTex(
            r"2x + 4 - 3x + 3 = 6",
            font_size=FS_EQ
        ).move_to(DOWN * 0.5)
        eq2_bg = make_card(eq2, stroke_color="#1abc9c")

        self.play(FadeIn(expand_title), run_time=0.4)
        self.play(Write(exp1_lhs), run_time=0.6)
        self.play(Write(exp2_rhs), run_time=0.6)
        self.play(FadeIn(warn), run_time=0.4)
        self.play(FadeIn(down_arr), run_time=0.3)
        self.play(Write(eq2), Create(eq2_bg), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(banner), FadeOut(prev), FadeOut(expand_title),
            FadeOut(exp1_lhs), FadeOut(exp2_rhs),
            FadeOut(warn), FadeOut(down_arr), FadeOut(eq2_bg),
            run_time=0.4
        )
        self.eq2 = eq2

    # ----------------------------------------------------------
    # Scene 5: 步骤③ 移项
    # ----------------------------------------------------------
    def scene_step3_transpose(self):
        banner = self._show_step_banner("③", "移项", COLOR_MOVED)

        prev = MathTex(
            r"2x + 4 - 3x + 3 = 6",
            font_size=FS_EQ_SM, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(ReplacementTransform(self.eq2, prev), run_time=0.5)

        rule = VGroup(
            Text("含 x 的项", font=FONT, font_size=FS_ANNOT, color=COLOR_X),
            Text("→ 左边", font=FONT, font_size=FS_ANNOT, color=COLOR_X),
            Text("    常数项", font=FONT, font_size=FS_ANNOT, color=COLOR_OP),
            Text("→ 右边", font=FONT, font_size=FS_ANNOT, color=COLOR_OP),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.6)

        # 标注：4 和 3 移到右边（变号）
        move_note = VGroup(
            Text("移项要变号：", font=FONT, font_size=FS_ANNOT, color=COLOR_MOVED),
            MathTex(r"+4 \rightarrow -4", font_size=FS_ANNOT + 2, color=COLOR_MOVED),
            Text("，", font=FONT, font_size=FS_ANNOT, color=WHITE),
            MathTex(r"+3 \rightarrow -3", font_size=FS_ANNOT + 2, color=COLOR_MOVED),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 2.8)

        down_arr = MathTex(r"\Downarrow", font_size=36,
                           color=COLOR_MOVED).move_to(UP * 2.0)

        # 移项后
        eq3 = MathTex(
            r"2x - 3x = 6 - 4 - 3",
            font_size=FS_EQ
        ).move_to(UP * 1.1)
        # 着色 x 项 & 常数项
        eq3[0][0:2].set_color(COLOR_X)   # 2x
        eq3[0][3:5].set_color(COLOR_X)   # -3x
        eq3[0][6].set_color(COLOR_OP)    # 6
        eq3[0][8].set_color(COLOR_MOVED) # 4（已变号）
        eq3[0][10].set_color(COLOR_MOVED)# 3（已变号）

        eq3_bg = make_card(eq3, stroke_color=COLOR_MOVED)

        self.play(FadeIn(rule), run_time=0.5)
        self.play(FadeIn(move_note), run_time=0.5)
        self.play(FadeIn(down_arr), run_time=0.3)
        self.play(Write(eq3), Create(eq3_bg), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(banner), FadeOut(prev), FadeOut(rule),
            FadeOut(move_note), FadeOut(down_arr), FadeOut(eq3_bg),
            run_time=0.4
        )
        self.eq3 = eq3

    # ----------------------------------------------------------
    # Scene 6: 步骤④ 合并同类项
    # ----------------------------------------------------------
    def scene_step4_combine(self):
        banner = self._show_step_banner("④", "合并同类项", COLOR_OP)

        prev = MathTex(
            r"2x - 3x = 6 - 4 - 3",
            font_size=FS_EQ_SM, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(ReplacementTransform(self.eq3, prev), run_time=0.5)

        # 合并 x 项
        combine_x = VGroup(
            MathTex(r"2x - 3x", font_size=36, color=COLOR_X),
            MathTex(r"= -x", font_size=36, color=COLOR_X),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 3.5)

        # 合并常数项
        combine_c = VGroup(
            MathTex(r"6 - 4 - 3", font_size=36, color=COLOR_OP),
            MathTex(r"= -1", font_size=36, color=COLOR_OP),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.7)

        down_arr = MathTex(r"\Downarrow", font_size=36,
                           color=COLOR_OP).move_to(UP * 1.9)

        eq4 = MathTex(r"-x = -1", font_size=FS_EQ + 8).move_to(UP * 0.9)
        eq4[0][0:2].set_color(COLOR_X)
        eq4[0][3:5].set_color(COLOR_OP)
        eq4_bg = make_card(eq4, stroke_color=COLOR_OP)

        self.play(FadeIn(combine_x), run_time=0.5)
        self.play(FadeIn(combine_c), run_time=0.5)
        self.play(FadeIn(down_arr), run_time=0.3)
        self.play(Write(eq4), Create(eq4_bg), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(banner), FadeOut(prev),
            FadeOut(combine_x), FadeOut(combine_c),
            FadeOut(down_arr), FadeOut(eq4_bg),
            run_time=0.4
        )
        self.eq4 = eq4

    # ----------------------------------------------------------
    # Scene 7: 步骤⑤ 系数化为 1
    # ----------------------------------------------------------
    def scene_step5_coeff_to_one(self):
        banner = self._show_step_banner("⑤", "系数化为 1", COLOR_OK)

        prev = MathTex(
            r"-x = -1", font_size=FS_EQ_SM, color=GRAY_A
        ).move_to(UP * 4.5)
        self.play(ReplacementTransform(self.eq4, prev), run_time=0.5)

        op_note = VGroup(
            Text("两边除以 x 的系数 (−1)", font=FONT,
                 font_size=FS_ANNOT, color=COLOR_OK),
        ).move_to(UP * 3.6)

        # 展示运算
        div_show = MathTex(
            r"\frac{-x}{-1} = \frac{-1}{-1}",
            font_size=40
        ).move_to(UP * 2.7)

        down_arr = MathTex(r"\Downarrow", font_size=36,
                           color=COLOR_OK).move_to(UP * 1.8)

        # 最终答案
        eq_final = MathTex(r"x = 1", font_size=72, color=COLOR_OK).move_to(UP * 0.7)
        eq_final_bg = make_card(eq_final, stroke_color=COLOR_OK,
                                fill_color="#001a08", buff=0.3)

        check_mark = Text("✓", font=FONT, font_size=52,
                          color=COLOR_OK).next_to(eq_final, RIGHT, buff=0.3)

        self.play(FadeIn(op_note), run_time=0.4)
        self.play(Write(div_show), run_time=0.6)
        self.play(FadeIn(down_arr), run_time=0.3)
        self.play(Create(eq_final_bg), Write(eq_final), run_time=0.8)
        self.play(
            FadeIn(check_mark, scale=0.5),
            Flash(eq_final, color=COLOR_OK, flash_radius=0.8),
            run_time=0.7
        )
        self.wait(1.5)

        self.play(
            FadeOut(banner), FadeOut(prev), FadeOut(op_note),
            FadeOut(div_show), FadeOut(down_arr),
            FadeOut(eq_final_bg), FadeOut(check_mark),
            run_time=0.4
        )
        self.eq_final = eq_final

    # ----------------------------------------------------------
    # Scene 8: 代入验证
    # ----------------------------------------------------------
    def scene_verify(self):
        title = Text("代入验证", font=FONT, font_size=FS_TITLE,
                     color=GOLD).move_to(UP * 5.7)

        # 展示最终答案
        ans = MathTex(r"x = 1", font_size=FS_EQ, color=COLOR_OK)
        ans_bg = make_card(ans, stroke_color=COLOR_OK,
                           fill_color="#001a08")
        VGroup(ans_bg, ans).move_to(UP * 4.7)

        # 代入左边
        lhs_label = Text("代入左边：", font=FONT, font_size=FS_ANNOT,
                         color=GRAY_A).move_to(UP * 3.8 + LEFT * 1.0)

        lhs_calc = MathTex(
            r"\frac{1+2}{3} - \frac{1-1}{2}",
            font_size=FS_EQ_SM
        ).move_to(UP * 3.0)

        step_a = MathTex(
            r"= \frac{3}{3} - \frac{0}{2}",
            font_size=FS_EQ_SM
        ).move_to(UP * 2.2)

        step_b = MathTex(
            r"= 1 - 0 = 1",
            font_size=FS_EQ_SM, color=COLOR_OK
        ).move_to(UP * 1.4)

        # 等于右边
        equal_rhs = VGroup(
            Text("左边 = 右边 = 1", font=FONT,
                 font_size=FS_STEP, color=COLOR_OK),
            Text("验证正确！", font=FONT, font_size=FS_STEP, color=YELLOW),
        ).arrange(RIGHT, buff=0.4).move_to(UP * 0.4)
        eq_rhs_bg = make_card(equal_rhs, stroke_color=COLOR_OK,
                              fill_color="#001a08")

        self.play(Write(title), run_time=0.5)
        self.play(
            ReplacementTransform(self.eq_final, ans),
            Create(ans_bg),
            run_time=0.5
        )
        self.play(FadeIn(lhs_label), run_time=0.3)
        self.play(Write(lhs_calc), run_time=0.7)
        self.play(Write(step_a), run_time=0.6)
        self.play(Write(step_b), run_time=0.5)
        self.play(Create(eq_rhs_bg), FadeIn(equal_rhs), run_time=0.6)
        self.play(Indicate(equal_rhs, scale_factor=1.05, color=YELLOW),
                  run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(ans_bg), FadeOut(ans),
            FadeOut(lhs_label), FadeOut(lhs_calc),
            FadeOut(step_a), FadeOut(step_b),
            FadeOut(eq_rhs_bg), FadeOut(equal_rhs),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 9: 总结
    # ----------------------------------------------------------
    def scene_summary(self):
        title = Text("解一元一次方程 · 5步法", font=FONT,
                     font_size=28, color=GOLD).move_to(UP * 6.3)

        steps_data = [
            ("①", "去分母", "两边乘最小公倍数",    COLOR_STEP),
            ("②", "去括号", "用乘法分配律展开",    "#1abc9c"),
            ("③", "移项",   "含x项左，常数项右",   COLOR_MOVED),
            ("④", "合并",   "合并同类项",           COLOR_OP),
            ("⑤", "化系数", "÷x的系数 → x=…",    COLOR_OK),
        ]

        y_top = 5.3
        cards = []
        for i, (num, short, detail, col) in enumerate(steps_data):
            row = VGroup(
                Text(num, font=FONT, font_size=24, color=col),
                Text(short, font=FONT, font_size=22, color=WHITE),
                Text(detail, font=FONT, font_size=18, color=GRAY_A),
            ).arrange(RIGHT, buff=0.3)
            row.move_to(UP * (y_top - i * 1.1))
            bg = make_card(row, stroke_color=col, buff=0.16)
            cards.append(VGroup(bg, row))

        self.play(Write(title), run_time=0.5)
        for c in cards:
            self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.25)

        # 例题答案
        ans_row = VGroup(
            Text("例题答案：", font=FONT, font_size=22, color=GRAY_A),
            MathTex(r"x = 1", font_size=34, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 1.0)
        ans_bg = make_card(ans_row, stroke_color=COLOR_OK,
                           fill_color="#001a08")

        self.play(Create(ans_bg), FadeIn(ans_row), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(ans_bg), FadeOut(ans_row),
            *[FadeOut(c) for c in cards],
            run_time=0.6
        )

    # ----------------------------------------------------------
    # Scene 10: 片尾
    # ----------------------------------------------------------
    def scene_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=36, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=26, color=GRAY_B
        ).move_to(UP * 1.1)
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=YELLOW
        ).move_to(DOWN * 0.2)

        # 5步编号装饰
        deco = VGroup(*[
            Text(s, font=FONT, font_size=22,
                 color=c).set_opacity(0.55)
            for s, c in [
                ("①去分母", COLOR_STEP),
                ("②去括号", "#1abc9c"),
                ("③移项",   COLOR_MOVED),
                ("④合并",   COLOR_OP),
                ("⑤化系数", COLOR_OK),
            ]
        ]).arrange(DOWN, buff=0.28).move_to(DOWN * 2.3)

        self.play(Transform(self.author, author_big), run_time=0.6)
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(follow, scale=1.05), run_time=0.5)
        self.play(FadeIn(deco), run_time=0.5)
        self.play(
            *[Indicate(d, scale_factor=1.1) for d in deco],
            run_time=0.8
        )
        self.wait(1.5)

        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco),
            run_time=0.8
        )

# manim -pql solve_linear_equation.py SolveLinearEquation   # 快速预览
# manim -qh  solve_linear_equation.py SolveLinearEquation   # 高质量输出