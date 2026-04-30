"""
001_两位数除以一位数.py — 两位数除以一位数（竖式计算）教学动画

知识点:
  - 竖式除法算法: 从被除数最高位除起，商写在对应位上
  - 例1: 52 ÷ 4 = 13 (十位5÷4=1余1, 落下个位2得12, 12÷4=3)
  - 例2: 有余数: 57 ÷ 4 = 14…1
  - 例3: 商中间有0: 312 ÷ 3 = 104 (十位1<3, 商0占位)
年级: 三年级上册
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
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
COLOR_TITLE = "#fbbf24"       # 金黄色 标题
COLOR_DIVIDEND = "#60a5fa"    # 蓝色 被除数
COLOR_DIVISOR = "#34d399"     # 绿色 除数
COLOR_QUOTIENT = "#f87171"    # 红色 商
COLOR_REMAINDER = "#a78bfa"   # 紫色 余数
COLOR_SUBTRACT = "#fb923c"    # 橙色 减法
COLOR_CARRY = "#fbbf24"       # 黄色 下移数字
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_RULE = "#94a3b8"        # 灰色 竖式线
COLOR_AUTHOR = "#6b7280"      # 灰色作者信息
COLOR_STEP = "#e2e8f0"        # 浅灰步骤说明
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class TwoDigitDivideOneLesson(Scene):
    """
    两位数除以一位数（竖式计算）教学动画
    场景顺序:
      1. 开场钩子
      2. 竖式结构介绍
      3. 例1: 52 ÷ 4 = 13 (退位)
      4. 例2: 57 ÷ 4 = 14…1 (有余数)
      5. 例3: 312 ÷ 3 = 104 (商中间有0)
      6. 算法口诀总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        self.scene_1_opening()
        self.scene_2_structure()
        self.scene_3_example1()
        self.scene_4_example2()
        self.scene_5_example3()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_title(self, txt, color=COLOR_TITLE, font_size=34):
        return Text(txt, font=FONT, font_size=font_size, color=color).move_to(UP * 5.8)

    def make_step_text(self, txt, color=COLOR_STEP, font_size=22, y=-4.5):
        return Text(txt, font=FONT, font_size=font_size, color=color).move_to(UP * y)

    def make_division_bar(self, center, width=3.8, color=COLOR_RULE):
        """竖式横线"""
        return Line(
            center + LEFT * width / 2,
            center + RIGHT * width / 2,
            color=color,
            stroke_width=2.5,
        )

    def make_vertical_bar(self, top, bottom, color=COLOR_RULE):
        """竖式竖线"""
        return Line(top, bottom, color=color, stroke_width=2.5)

    # ------------------------------------------------------------------
    # 竖式绘制辅助
    # 竖式布局 (长除法符号):
    #       商
    #   ┌─────
    # 除数 │ 被除数
    #       ─────
    #       余数
    # ------------------------------------------------------------------

    def build_long_division_frame(self, divisor_str, dividend_str, center):
        """
        绘制空白竖式框架, 返回各元素和关键坐标字典
        center: 被除数中心位置
        """
        fs = 52  # 数字字体大小

        # 被除数
        dividend = Text(dividend_str, font=FONT, font_size=fs, color=COLOR_DIVIDEND)
        dividend.move_to(center)

        # 除数 (被除数左侧)
        divisor = Text(divisor_str, font=FONT, font_size=fs, color=COLOR_DIVISOR)
        divisor.next_to(dividend, LEFT, buff=0.55)

        # 横线 (除号横线, 在被除数下方稍高)
        # 这里用 "厂" 形: 竖线 + 横线
        bar_y = dividend.get_bottom()[1] - 0.15
        bar_left_x = divisor.get_left()[0] + 0.05
        bar_right_x = dividend.get_right()[0] + 0.2

        # 竖线: 从除数顶到横线位置(再高一些，到商的位置)
        quotient_y = dividend.get_top()[1] + 0.75
        vert_bar = Line(
            np.array([bar_left_x + 0.1, bar_y, 0]),
            np.array([bar_left_x + 0.1, quotient_y + 0.3, 0]),
            color=COLOR_RULE,
            stroke_width=2.5,
        )

        # 横线: 被除数下方
        horiz_bar = Line(
            np.array([bar_left_x + 0.1, bar_y, 0]),
            np.array([bar_right_x, bar_y, 0]),
            color=COLOR_RULE,
            stroke_width=2.5,
        )

        # 商位置: 横线上方, 对齐被除数
        quotient_center_y = quotient_y

        coords = {
            "dividend_center": dividend.get_center(),
            "divisor_center": divisor.get_center(),
            "bar_y": bar_y,
            "bar_left_x": bar_left_x + 0.1,
            "bar_right_x": bar_right_x,
            "quotient_y": quotient_center_y,
            "dividend_right_x": dividend.get_right()[0],
            "dividend_left_x": dividend.get_left()[0],
            "dividend_top_y": dividend.get_top()[1],
            "dividend_bottom_y": dividend.get_bottom()[1],
        }

        frame = VGroup(dividend, divisor, vert_bar, horiz_bar)
        return frame, coords, dividend, divisor

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        hook = Text(
            "52 ÷ 4 = ?",
            font=FONT, font_size=56, color=COLOR_HL,
        ).move_to(UP * 4.5)

        sub = Text(
            "如何用竖式来计算除法?",
            font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 3.6)

        self.play(Write(hook), run_time=0.9)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)

        # 三个关键词闪现
        kw1 = Text("从高位算起", font=FONT, font_size=28, color=COLOR_DIVIDEND).move_to(UP * 1.5)
        kw2 = Text("余数落下来", font=FONT, font_size=28, color=COLOR_CARRY).move_to(UP * 0.3)
        kw3 = Text("商写对位置", font=FONT, font_size=28, color=COLOR_QUOTIENT).move_to(DOWN * 0.9)

        for kw in [kw1, kw2, kw3]:
            self.play(FadeIn(kw, scale=0.8), run_time=0.35)

        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(sub),
            FadeOut(kw1), FadeOut(kw2), FadeOut(kw3),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 竖式结构介绍
    # ------------------------------------------------------------------

    def scene_2_structure(self):
        title = self.make_title("竖式的结构")
        self.play(Write(title), run_time=0.6)

        # 竖式示意图
        center = UP * 1.5

        # 商 (上方)
        lbl_quotient = Text("商", font=FONT, font_size=40, color=COLOR_QUOTIENT)
        lbl_quotient.move_to(center + UP * 1.0 + RIGHT * 0.5)

        # 横线
        horiz = Line(
            center + UP * 0.35 + LEFT * 1.8,
            center + UP * 0.35 + RIGHT * 1.8,
            color=COLOR_RULE, stroke_width=2.5,
        )

        # 竖线 ("厂" 形)
        vert = Line(
            center + UP * 1.5 + LEFT * 0.7,
            center + UP * 0.35 + LEFT * 0.7,
            color=COLOR_RULE, stroke_width=2.5,
        )

        # 除数 (竖线左侧)
        lbl_divisor = Text("除数", font=FONT, font_size=36, color=COLOR_DIVISOR)
        lbl_divisor.move_to(center + LEFT * 1.6)

        # 被除数 (竖线右侧)
        lbl_dividend = Text("被除数", font=FONT, font_size=36, color=COLOR_DIVIDEND)
        lbl_dividend.move_to(center + RIGHT * 0.7)

        self.play(
            Create(horiz), Create(vert),
            run_time=0.8,
        )
        self.play(
            FadeIn(lbl_quotient, shift=DOWN * 0.2),
            FadeIn(lbl_divisor, shift=RIGHT * 0.2),
            FadeIn(lbl_dividend, shift=LEFT * 0.2),
            run_time=0.6,
        )

        # 箭头标注
        arr_q = Arrow(
            lbl_quotient.get_bottom(), horiz.get_center() + UP * 0.15,
            color=COLOR_QUOTIENT, stroke_width=2, buff=0.05,
            max_tip_length_to_length_ratio=0.2,
        )

        # 说明文字
        explain = Text(
            "除数 ÷ 号 右边是被除数，上面写商",
            font=FONT, font_size=20, color=GRAY_A,
        ).move_to(DOWN * 2.5)

        step_rule = VGroup(
            Text("算法规则:", font=FONT, font_size=24, color=COLOR_HL),
        ).move_to(DOWN * 3.5)

        rule1 = Text("从最高位(左)开始除", font=FONT, font_size=20, color=COLOR_STEP)
        rule2 = Text("除到哪位, 商写那位上方", font=FONT, font_size=20, color=COLOR_STEP)
        rule3 = Text("余数与下一位合并再除", font=FONT, font_size=20, color=COLOR_STEP)
        rules = VGroup(rule1, rule2, rule3).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        rules.move_to(DOWN * 5.0)

        self.play(FadeIn(explain), FadeIn(step_rule), run_time=0.5)
        self.play(FadeIn(rules, shift=UP * 0.2), run_time=0.6)

        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(horiz), FadeOut(vert),
            FadeOut(lbl_quotient), FadeOut(lbl_divisor), FadeOut(lbl_dividend),
            FadeOut(explain), FadeOut(step_rule), FadeOut(rules),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 例1 — 52 ÷ 4 = 13
    # ------------------------------------------------------------------

    def scene_3_example1(self):
        title = self.make_title("例1:  52 ÷ 4 = ?", color=COLOR_TITLE)
        self.play(Write(title), run_time=0.6)

        # ---- 布局参数 ----
        # 竖式放在屏幕上半部分
        # 使用手动精确坐标, 基于9x16逻辑坐标
        # 竖式中心 y ~ 2.5
        div_center = np.array([1.0, 2.8, 0.0])   # 被除数 "52" 中心
        fs = 52   # 数字字号

        # ---- 被除数 "52" ----
        t52 = Text("52", font=FONT, font_size=fs, color=COLOR_DIVIDEND)
        t52.move_to(div_center)

        # ---- 除数 "4" ----
        t4 = Text("4", font=FONT, font_size=fs, color=COLOR_DIVISOR)
        t4.next_to(t52, LEFT, buff=0.6)

        # ---- 竖式线 ("厂") ----
        bar_y = t52.get_bottom()[1] - 0.15
        left_x = t4.get_left()[0] + 0.05
        right_x = t52.get_right()[0] + 0.25
        top_y = t52.get_top()[1] + 0.8

        vert_line = Line(
            np.array([left_x + 0.12, bar_y, 0]),
            np.array([left_x + 0.12, top_y, 0]),
            color=COLOR_RULE, stroke_width=2.5,
        )
        horiz_line = Line(
            np.array([left_x + 0.12, bar_y, 0]),
            np.array([right_x, bar_y, 0]),
            color=COLOR_RULE, stroke_width=2.5,
        )

        # ---- 商的位置 y ----
        quot_y = top_y - 0.5

        # 十位5所在x, 个位2所在x
        # "52": 十位约在左半部分, 个位在右半部分
        # 获取单字符位置: 字符宽度约 fs/100 * 0.6
        char_w = 0.45   # 估计每个数字字符宽度(逻辑单位)
        # "52"的左边 x:
        d_left = t52.get_left()[0]
        d_right = t52.get_right()[0]
        d_mid = (d_left + d_right) / 2.0

        # 十位x ≈ d_left + char_w/2
        x_tens = d_left + char_w * 0.55
        # 个位x ≈ d_right - char_w/2
        x_ones = d_right - char_w * 0.55

        # 商 "1" (十位上方)
        q1 = Text("1", font=FONT, font_size=fs, color=COLOR_QUOTIENT)
        q1.move_to(np.array([x_tens, quot_y, 0]))

        # 商 "3" (个位上方)
        q3 = Text("3", font=FONT, font_size=fs, color=COLOR_QUOTIENT)
        q3.move_to(np.array([x_ones, quot_y, 0]))

        # ---- 第一步减法: 5 - 4 = 1, 写在被除数下方 ----
        # 中间竖式减法区域: y ~ bar_y - 0.1
        subtract_y1 = bar_y - 0.5   # "4" (4×1) 的位置
        remainder_y1 = bar_y - 1.1  # 余数 "1" 位置
        bar2_y = bar_y - 1.35       # 第二横线

        # 4×1=4: 写在十位下方
        t_sub4 = Text("4", font=FONT, font_size=fs, color=COLOR_SUBTRACT)
        t_sub4.move_to(np.array([x_tens, subtract_y1, 0]))

        sub_bar = Line(
            np.array([left_x + 0.12, bar2_y, 0]),
            np.array([d_mid + 0.05, bar2_y, 0]),
            color=COLOR_RULE, stroke_width=2.0,
        )

        # 余数 "1" (十位余数)
        t_rem1 = Text("1", font=FONT, font_size=fs, color=COLOR_CARRY)
        t_rem1.move_to(np.array([x_tens, remainder_y1, 0]))

        # ---- 落下个位 "2": 余1和2合成12 ----
        # "2" (个位) 落下, 和余数 "1" 组成 "12"
        t_bring2 = Text("2", font=FONT, font_size=fs, color=COLOR_CARRY)
        # 12 出现在下方区域: "1" 在十位x, "2" 在个位x, y = remainder_y1
        t_bring2.move_to(np.array([x_ones, remainder_y1, 0]))

        # ---- 第二步减法: 12 - 12 = 0 ----
        subtract_y2 = remainder_y1 - 0.55
        bar3_y = remainder_y1 - 0.8
        remainder_y2 = remainder_y1 - 1.0

        # 4×3=12: 写在 "12" 下方
        t_sub12_1 = Text("1", font=FONT, font_size=fs, color=COLOR_SUBTRACT)
        t_sub12_1.move_to(np.array([x_tens, subtract_y2, 0]))
        t_sub12_2 = Text("2", font=FONT, font_size=fs, color=COLOR_SUBTRACT)
        t_sub12_2.move_to(np.array([x_ones, subtract_y2, 0]))

        sub_bar2 = Line(
            np.array([left_x + 0.12, bar3_y, 0]),
            np.array([d_right + 0.1, bar3_y, 0]),
            color=COLOR_RULE, stroke_width=2.0,
        )

        t_rem0 = Text("0", font=FONT, font_size=fs, color=COLOR_REMAINDER)
        t_rem0.move_to(np.array([x_ones, remainder_y2, 0]))

        # ---- 结论 ----
        answer_line = VGroup(
            Text("52 ÷ 4 = ", font=FONT, font_size=36, color=WHITE),
            Text("13", font=FONT, font_size=40, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.2)

        # ===== 动画序列 =====

        # 出现竖式框架
        self.play(
            FadeIn(t52), FadeIn(t4),
            Create(vert_line), Create(horiz_line),
            run_time=0.8,
        )

        # 步骤1: 十位 5 ÷ 4 = 1
        step1 = self.make_step_text("十位: 5 ÷ 4 = 1, 商1", y=-3.5)
        self.play(FadeIn(step1), run_time=0.4)
        self.play(Indicate(t52[0:1], color=COLOR_HL, scale_factor=1.3), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.3), run_time=0.5)
        self.wait(0.5)

        # 步骤2: 4×1=4, 5-4=1
        step2 = self.make_step_text("4×1=4, 5-4=1, 余数是1", y=-3.5)
        self.play(ReplacementTransform(step1, step2), run_time=0.4)
        self.play(FadeIn(t_sub4, shift=UP * 0.3), run_time=0.4)
        self.play(Create(sub_bar), run_time=0.3)
        self.play(FadeIn(t_rem1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 步骤3: 落下个位2, 得12
        step3 = self.make_step_text("余1十, 落下个位2 → 12", y=-3.5)
        self.play(ReplacementTransform(step2, step3), run_time=0.4)

        # 动画: "2" 从被除数位置落下
        t52_copy = Text("2", font=FONT, font_size=fs, color=COLOR_CARRY)
        t52_copy.move_to(np.array([x_ones, t52.get_center()[1], 0]))

        t_bring2_target = t_bring2.copy()
        self.play(FadeIn(t52_copy), run_time=0.3)
        self.play(
            t52_copy.animate.move_to(np.array([x_ones, remainder_y1, 0])),
            run_time=0.8, rate_func=smooth,
        )
        self.remove(t52_copy)
        self.add(t_bring2)
        self.wait(0.5)

        # 步骤4: 12 ÷ 4 = 3
        step4 = self.make_step_text("个位: 12 ÷ 4 = 3, 商3", y=-3.5)
        self.play(ReplacementTransform(step3, step4), run_time=0.4)
        self.play(Indicate(t_rem1, color=COLOR_HL), Indicate(t_bring2, color=COLOR_HL), run_time=0.5)
        self.play(FadeIn(q3, shift=DOWN * 0.3), run_time=0.5)
        self.wait(0.5)

        # 步骤5: 4×3=12, 12-12=0
        step5 = self.make_step_text("4×3=12, 12-12=0, 整除!", y=-3.5)
        self.play(ReplacementTransform(step4, step5), run_time=0.4)
        self.play(FadeIn(t_sub12_1, shift=UP * 0.2), FadeIn(t_sub12_2, shift=UP * 0.2), run_time=0.4)
        self.play(Create(sub_bar2), run_time=0.3)
        self.play(FadeIn(t_rem0, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # 结论
        self.play(FadeOut(step5), run_time=0.3)
        self.play(FadeIn(answer_line, shift=UP * 0.3), run_time=0.6)
        self.play(Indicate(q1, scale_factor=1.2), Indicate(q3, scale_factor=1.2), run_time=0.6)
        self.wait(1.5)

        # 清理
        all_scene3 = VGroup(
            title, t52, t4, vert_line, horiz_line,
            q1, q3, t_sub4, sub_bar, t_rem1,
            t_bring2, t_sub12_1, t_sub12_2, sub_bar2, t_rem0,
            answer_line,
        )
        self.play(FadeOut(all_scene3), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 4: 例2 — 57 ÷ 4 = 14…1 (有余数)
    # ------------------------------------------------------------------

    def scene_4_example2(self):
        title = self.make_title("例2:  57 ÷ 4 = ?", color=COLOR_TITLE)
        self.play(Write(title), run_time=0.6)

        # 布局参数
        div_center = np.array([1.0, 2.8, 0.0])
        fs = 52

        # 被除数 "57"
        t57 = Text("57", font=FONT, font_size=fs, color=COLOR_DIVIDEND)
        t57.move_to(div_center)

        # 除数 "4"
        t4 = Text("4", font=FONT, font_size=fs, color=COLOR_DIVISOR)
        t4.next_to(t57, LEFT, buff=0.6)

        # 竖式线
        bar_y = t57.get_bottom()[1] - 0.15
        left_x = t4.get_left()[0] + 0.05
        right_x = t57.get_right()[0] + 0.25
        top_y = t57.get_top()[1] + 0.8

        vert_line = Line(
            np.array([left_x + 0.12, bar_y, 0]),
            np.array([left_x + 0.12, top_y, 0]),
            color=COLOR_RULE, stroke_width=2.5,
        )
        horiz_line = Line(
            np.array([left_x + 0.12, bar_y, 0]),
            np.array([right_x, bar_y, 0]),
            color=COLOR_RULE, stroke_width=2.5,
        )

        quot_y = top_y - 0.5
        char_w = 0.45
        d_left = t57.get_left()[0]
        d_right = t57.get_right()[0]
        d_mid = (d_left + d_right) / 2.0
        x_tens = d_left + char_w * 0.55
        x_ones = d_right - char_w * 0.55

        # 商 "14"
        q1 = Text("1", font=FONT, font_size=fs, color=COLOR_QUOTIENT)
        q1.move_to(np.array([x_tens, quot_y, 0]))
        q4 = Text("4", font=FONT, font_size=fs, color=COLOR_QUOTIENT)
        q4.move_to(np.array([x_ones, quot_y, 0]))

        # 第一步减法: 5-4=1
        subtract_y1 = bar_y - 0.5
        bar2_y = bar_y - 1.35
        remainder_y1 = bar_y - 1.1

        t_sub4 = Text("4", font=FONT, font_size=fs, color=COLOR_SUBTRACT)
        t_sub4.move_to(np.array([x_tens, subtract_y1, 0]))

        sub_bar = Line(
            np.array([left_x + 0.12, bar2_y, 0]),
            np.array([d_mid + 0.05, bar2_y, 0]),
            color=COLOR_RULE, stroke_width=2.0,
        )

        t_rem1 = Text("1", font=FONT, font_size=fs, color=COLOR_CARRY)
        t_rem1.move_to(np.array([x_tens, remainder_y1, 0]))

        # 落下 "7"
        t_bring7 = Text("7", font=FONT, font_size=fs, color=COLOR_CARRY)
        t_bring7.move_to(np.array([x_ones, remainder_y1, 0]))

        # 第二步减法: 17 - 16 = 1
        subtract_y2 = remainder_y1 - 0.55
        bar3_y = remainder_y1 - 0.8
        remainder_y2 = remainder_y1 - 1.0

        t_sub16_1 = Text("1", font=FONT, font_size=fs, color=COLOR_SUBTRACT)
        t_sub16_1.move_to(np.array([x_tens, subtract_y2, 0]))
        t_sub16_2 = Text("6", font=FONT, font_size=fs, color=COLOR_SUBTRACT)
        t_sub16_2.move_to(np.array([x_ones, subtract_y2, 0]))

        sub_bar2 = Line(
            np.array([left_x + 0.12, bar3_y, 0]),
            np.array([d_right + 0.1, bar3_y, 0]),
            color=COLOR_RULE, stroke_width=2.0,
        )

        # 余数 "1"
        t_final_rem = Text("1", font=FONT, font_size=fs, color=COLOR_REMAINDER)
        t_final_rem.move_to(np.array([x_ones, remainder_y2, 0]))

        # 余数标注 "...1"
        remainder_label = VGroup(
            Text("余数:", font=FONT, font_size=26, color=COLOR_REMAINDER),
            Text("1", font=FONT, font_size=36, color=COLOR_REMAINDER),
        ).arrange(RIGHT, buff=0.1).move_to(np.array([x_ones + 0.8, remainder_y2, 0]))

        # 余数必须比除数小 的提示
        rem_rule = Text(
            "余数 1 < 除数 4  ✓",
            font=FONT, font_size=22, color=COLOR_REMAINDER,
        ).move_to(DOWN * 3.8)

        # 结论
        answer_line = VGroup(
            Text("57 ÷ 4 = ", font=FONT, font_size=36, color=WHITE),
            Text("14", font=FONT, font_size=40, color=COLOR_QUOTIENT),
            Text(" … ", font=FONT, font_size=36, color=WHITE),
            Text("1", font=FONT, font_size=40, color=COLOR_REMAINDER),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.2)

        # ===== 动画序列 =====

        self.play(FadeIn(t57), FadeIn(t4), Create(vert_line), Create(horiz_line), run_time=0.8)

        step1 = self.make_step_text("十位: 5 ÷ 4 = 1 商1", y=-3.5)
        self.play(FadeIn(step1), run_time=0.4)
        self.play(Indicate(t57[0:1], color=COLOR_HL, scale_factor=1.3), run_time=0.5)
        self.play(FadeIn(q1, shift=DOWN * 0.3), run_time=0.5)
        self.wait(0.4)

        step2 = self.make_step_text("4×1=4, 5-4=1, 余数1", y=-3.5)
        self.play(ReplacementTransform(step1, step2), run_time=0.4)
        self.play(FadeIn(t_sub4, shift=UP * 0.3), run_time=0.4)
        self.play(Create(sub_bar), run_time=0.3)
        self.play(FadeIn(t_rem1, shift=UP * 0.2), run_time=0.4)
        self.wait(0.4)

        step3 = self.make_step_text("余1十, 落下个位7 → 17", y=-3.5)
        self.play(ReplacementTransform(step2, step3), run_time=0.4)
        t57_copy = Text("7", font=FONT, font_size=fs, color=COLOR_CARRY)
        t57_copy.move_to(np.array([x_ones, t57.get_center()[1], 0]))
        self.play(FadeIn(t57_copy), run_time=0.3)
        self.play(t57_copy.animate.move_to(np.array([x_ones, remainder_y1, 0])), run_time=0.8, rate_func=smooth)
        self.remove(t57_copy)
        self.add(t_bring7)
        self.wait(0.4)

        step4 = self.make_step_text("个位: 17 ÷ 4 = 4 商4", y=-3.5)
        self.play(ReplacementTransform(step3, step4), run_time=0.4)
        self.play(FadeIn(q4, shift=DOWN * 0.3), run_time=0.5)
        self.wait(0.4)

        step5 = self.make_step_text("4×4=16, 17-16=1 有余数!", y=-3.5)
        self.play(ReplacementTransform(step4, step5), run_time=0.4)
        self.play(FadeIn(t_sub16_1, shift=UP * 0.2), FadeIn(t_sub16_2, shift=UP * 0.2), run_time=0.4)
        self.play(Create(sub_bar2), run_time=0.3)
        self.play(FadeIn(t_final_rem, shift=UP * 0.2), run_time=0.4)
        self.wait(0.4)

        # 余数规则
        self.play(FadeOut(step5), FadeIn(rem_rule), run_time=0.4)
        self.play(Indicate(t_final_rem, color=COLOR_REMAINDER, scale_factor=1.3), run_time=0.6)
        self.wait(0.5)

        self.play(FadeOut(rem_rule), run_time=0.3)
        self.play(FadeIn(answer_line, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        all_scene4 = VGroup(
            title, t57, t4, vert_line, horiz_line,
            q1, q4, t_sub4, sub_bar, t_rem1,
            t_bring7, t_sub16_1, t_sub16_2, sub_bar2, t_final_rem,
            answer_line,
        )
        self.play(FadeOut(all_scene4), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 5: 例3 — 312 ÷ 3 = 104 (商中间有0)
    # ------------------------------------------------------------------

    def scene_5_example3(self):
        title = self.make_title("例3:  312 ÷ 3 = ?", color=COLOR_TITLE)
        sub_title = Text(
            "⚠ 商中间有0",
            font=FONT, font_size=26, color=COLOR_REMAINDER,
        ).move_to(UP * 5.0)
        self.play(Write(title), FadeIn(sub_title), run_time=0.7)

        # 布局参数: 三位数
        div_center = np.array([1.2, 3.0, 0.0])
        fs = 44

        # 被除数 "312"
        t312 = Text("312", font=FONT, font_size=fs, color=COLOR_DIVIDEND)
        t312.move_to(div_center)

        # 除数 "3"
        t3 = Text("3", font=FONT, font_size=fs, color=COLOR_DIVISOR)
        t3.next_to(t312, LEFT, buff=0.55)

        # 竖式线
        bar_y = t312.get_bottom()[1] - 0.15
        left_x = t3.get_left()[0] + 0.05
        right_x = t312.get_right()[0] + 0.2
        top_y = t312.get_top()[1] + 0.7

        vert_line = Line(
            np.array([left_x + 0.12, bar_y, 0]),
            np.array([left_x + 0.12, top_y, 0]),
            color=COLOR_RULE, stroke_width=2.5,
        )
        horiz_line = Line(
            np.array([left_x + 0.12, bar_y, 0]),
            np.array([right_x, bar_y, 0]),
            color=COLOR_RULE, stroke_width=2.5,
        )

        quot_y = top_y - 0.45

        # "312": 三位数, 每位x坐标
        d_left = t312.get_left()[0]
        d_right = t312.get_right()[0]
        char_w = (d_right - d_left) / 3.0

        x_hundreds = d_left + char_w * 0.5    # 百位
        x_tens = d_left + char_w * 1.5        # 十位
        x_ones = d_left + char_w * 2.5        # 个位

        # 商 "1" (百位), "0" (十位), "4" (个位)
        q_h1 = Text("1", font=FONT, font_size=fs, color=COLOR_QUOTIENT)
        q_h1.move_to(np.array([x_hundreds, quot_y, 0]))

        q_0 = Text("0", font=FONT, font_size=fs, color=COLOR_REMAINDER)
        q_0.move_to(np.array([x_tens, quot_y, 0]))

        q_h4 = Text("4", font=FONT, font_size=fs, color=COLOR_QUOTIENT)
        q_h4.move_to(np.array([x_ones, quot_y, 0]))

        # 第一步: 3 ÷ 3 = 1
        sub_y1 = bar_y - 0.45
        bar2_y = bar_y - 1.2
        rem_y1 = bar_y - 1.0

        t_sub3 = Text("3", font=FONT, font_size=fs, color=COLOR_SUBTRACT)
        t_sub3.move_to(np.array([x_hundreds, sub_y1, 0]))

        sub_bar1 = Line(
            np.array([left_x + 0.12, bar2_y, 0]),
            np.array([x_hundreds + char_w * 0.5, bar2_y, 0]),
            color=COLOR_RULE, stroke_width=2.0,
        )

        t_rem0_1 = Text("0", font=FONT, font_size=fs, color=COLOR_CARRY)
        t_rem0_1.move_to(np.array([x_hundreds, rem_y1, 0]))

        # 落下十位 "1"
        t_bring1 = Text("1", font=FONT, font_size=fs, color=COLOR_CARRY)
        t_bring1.move_to(np.array([x_tens, rem_y1, 0]))

        # 关键: 1 < 3, 商0占位
        highlight_zero = Text(
            "1 < 3, 不够除! 商 0 占位",
            font=FONT, font_size=24, color=COLOR_REMAINDER,
        ).move_to(DOWN * 3.2)

        # 落下个位 "2"
        t_bring2 = Text("2", font=FONT, font_size=fs, color=COLOR_CARRY)
        t_bring2.move_to(np.array([x_ones, rem_y1, 0]))

        # "12" (下降后合并) — 十位1和个位2合成12
        # 实际: 竖式继续做 12 ÷ 3

        # 第二步: 12 ÷ 3 = 4
        sub_y2 = rem_y1 - 0.55
        bar3_y = rem_y1 - 0.8
        rem_y2 = rem_y1 - 1.0

        t_sub12_1 = Text("1", font=FONT, font_size=fs, color=COLOR_SUBTRACT)
        t_sub12_1.move_to(np.array([x_tens, sub_y2, 0]))
        t_sub12_2 = Text("2", font=FONT, font_size=fs, color=COLOR_SUBTRACT)
        t_sub12_2.move_to(np.array([x_ones, sub_y2, 0]))

        sub_bar2 = Line(
            np.array([left_x + 0.12, bar3_y, 0]),
            np.array([x_ones + char_w * 0.5, bar3_y, 0]),
            color=COLOR_RULE, stroke_width=2.0,
        )

        t_rem0_2 = Text("0", font=FONT, font_size=fs, color=COLOR_REMAINDER)
        t_rem0_2.move_to(np.array([x_ones, rem_y2, 0]))

        # 结论
        answer_line = VGroup(
            Text("312 ÷ 3 = ", font=FONT, font_size=34, color=WHITE),
            Text("104", font=FONT, font_size=40, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.2)

        # ===== 动画序列 =====

        self.play(FadeIn(t312), FadeIn(t3), Create(vert_line), Create(horiz_line), run_time=0.8)

        step1 = self.make_step_text("百位: 3 ÷ 3 = 1, 商1", y=-3.9)
        self.play(FadeIn(step1), run_time=0.4)
        self.play(FadeIn(q_h1, shift=DOWN * 0.3), run_time=0.5)
        self.wait(0.4)

        step2 = self.make_step_text("3×1=3, 3-3=0, 落下十位1", y=-3.9)
        self.play(ReplacementTransform(step1, step2), run_time=0.4)
        self.play(FadeIn(t_sub3, shift=UP * 0.3), run_time=0.4)
        self.play(Create(sub_bar1), run_time=0.3)
        self.play(FadeIn(t_rem0_1, shift=UP * 0.2), run_time=0.4)

        # 落下十位 "1"
        t312_digit1 = Text("1", font=FONT, font_size=fs, color=COLOR_CARRY)
        t312_digit1.move_to(np.array([x_tens, t312.get_center()[1], 0]))
        self.play(FadeIn(t312_digit1), run_time=0.3)
        self.play(t312_digit1.animate.move_to(np.array([x_tens, rem_y1, 0])), run_time=0.7, rate_func=smooth)
        self.remove(t312_digit1)
        self.add(t_bring1)
        self.wait(0.4)

        # 关键: 十位 1 < 3, 商0
        step3 = self.make_step_text("十位: 01 ÷ 3, 不够除!", y=-3.9)
        self.play(ReplacementTransform(step2, step3), run_time=0.4)
        self.play(FadeIn(highlight_zero, shift=UP * 0.2), run_time=0.5)
        self.play(Indicate(t_bring1, color=COLOR_REMAINDER, scale_factor=1.4), run_time=0.6)
        self.play(FadeIn(q_0, shift=DOWN * 0.3), run_time=0.6)
        self.wait(0.8)

        # 落下个位 "2"
        step4 = self.make_step_text("落下个位2, 合成12", y=-3.9)
        self.play(ReplacementTransform(step3, step4), FadeOut(highlight_zero), run_time=0.4)

        t312_digit2 = Text("2", font=FONT, font_size=fs, color=COLOR_CARRY)
        t312_digit2.move_to(np.array([x_ones, t312.get_center()[1], 0]))
        self.play(FadeIn(t312_digit2), run_time=0.3)
        self.play(t312_digit2.animate.move_to(np.array([x_ones, rem_y1, 0])), run_time=0.7, rate_func=smooth)
        self.remove(t312_digit2)
        self.add(t_bring2)
        self.wait(0.4)

        step5 = self.make_step_text("12 ÷ 3 = 4, 商4", y=-3.9)
        self.play(ReplacementTransform(step4, step5), run_time=0.4)
        self.play(FadeIn(q_h4, shift=DOWN * 0.3), run_time=0.5)
        self.wait(0.4)

        step6 = self.make_step_text("3×4=12, 12-12=0, 整除!", y=-3.9)
        self.play(ReplacementTransform(step5, step6), run_time=0.4)
        self.play(FadeIn(t_sub12_1, shift=UP * 0.2), FadeIn(t_sub12_2, shift=UP * 0.2), run_time=0.4)
        self.play(Create(sub_bar2), run_time=0.3)
        self.play(FadeIn(t_rem0_2, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        self.play(FadeOut(step6), run_time=0.3)

        # 高亮商中间的0
        zero_box = SurroundingRectangle(q_0, color=COLOR_REMAINDER, buff=0.08, stroke_width=2.5)
        zero_note = Text("0 是占位数, 不能省略!", font=FONT, font_size=22, color=COLOR_REMAINDER)
        zero_note.move_to(DOWN * 3.8)
        self.play(Create(zero_box), FadeIn(zero_note), run_time=0.6)
        self.play(Indicate(q_0, color=COLOR_REMAINDER, scale_factor=1.4), run_time=0.7)
        self.wait(0.8)

        self.play(FadeOut(zero_box), FadeOut(zero_note), run_time=0.3)
        self.play(FadeIn(answer_line, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        all_scene5 = VGroup(
            title, sub_title, t312, t3, vert_line, horiz_line,
            q_h1, q_0, q_h4,
            t_sub3, sub_bar1, t_rem0_1,
            t_bring1, t_bring2,
            t_sub12_1, t_sub12_2, sub_bar2, t_rem0_2,
            answer_line,
        )
        self.play(FadeOut(all_scene5), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 6: 算法口诀总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = self.make_title("竖式除法  口诀总结", color=COLOR_HL)
        self.play(Write(title), run_time=0.6)

        card_bg = RoundedRectangle(
            width=7.8, height=10.0,
            corner_radius=0.3,
            color=WHITE,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=0.05,
        ).move_to(UP * 0.0)
        self.play(FadeIn(card_bg), run_time=0.4)

        # 条目1
        item1_head = Text("① 从最高位开始除", font=FONT, font_size=26, color=COLOR_DIVIDEND)
        item1_body = Text(
            "被除数最高位开始, 除到哪位\n商就写在那位上面",
            font=FONT, font_size=20, color=GRAY_A,
        )
        item1 = VGroup(item1_head, item1_body).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item1.move_to(UP * 3.8 + LEFT * 0.2)

        self.play(FadeIn(item1, shift=RIGHT * 0.3), run_time=0.5)

        # 条目2
        item2_head = Text("② 余数落下合并再除", font=FONT, font_size=26, color=COLOR_CARRY)
        item2_body = Text(
            "每步的余数与下一位数字合并\n继续相除",
            font=FONT, font_size=20, color=GRAY_A,
        )
        item2 = VGroup(item2_head, item2_body).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item2.move_to(UP * 2.0 + LEFT * 0.2)

        self.play(FadeIn(item2, shift=RIGHT * 0.3), run_time=0.5)

        # 条目3
        item3_head = Text("③ 不够除要商0占位", font=FONT, font_size=26, color=COLOR_REMAINDER)
        item3_body = Text(
            "某位上不够商1时, 必须写0占位\n否则商的位数会出错!",
            font=FONT, font_size=20, color=GRAY_A,
        )
        item3 = VGroup(item3_head, item3_body).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item3.move_to(DOWN * 0.0 + LEFT * 0.2)

        self.play(FadeIn(item3, shift=RIGHT * 0.3), run_time=0.5)

        # 条目4
        item4_head = Text("④ 余数必须小于除数", font=FONT, font_size=26, color=COLOR_QUOTIENT)
        item4_body = Text(
            "每次相除后余数 < 除数\n否则说明商取小了",
            font=FONT, font_size=20, color=GRAY_A,
        )
        item4 = VGroup(item4_head, item4_body).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item4.move_to(DOWN * 2.1 + LEFT * 0.2)

        self.play(FadeIn(item4, shift=RIGHT * 0.3), run_time=0.5)

        # 例题回顾
        examples_recap = VGroup(
            Text("52÷4=13", font=FONT, font_size=22, color=COLOR_DIVIDEND),
            Text("57÷4=14…1", font=FONT, font_size=22, color=COLOR_CARRY),
            Text("312÷3=104", font=FONT, font_size=22, color=COLOR_REMAINDER),
        ).arrange(RIGHT, buff=0.5).move_to(DOWN * 4.2)

        self.play(FadeIn(examples_recap, shift=UP * 0.3), run_time=0.6)

        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(item1), FadeOut(item2), FadeOut(item3), FadeOut(item4),
            FadeOut(examples_recap),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(UP * 0.5)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多数学知识!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 1.0)

        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 三个例题装饰
        deco1 = VGroup(
            Text("52÷4", font=FONT, font_size=24, color=COLOR_DIVIDEND),
            Text("=13", font=FONT, font_size=24, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 3.0 + LEFT * 2.5)

        deco2 = VGroup(
            Text("57÷4", font=FONT, font_size=24, color=COLOR_DIVIDEND),
            Text("=14…1", font=FONT, font_size=24, color=COLOR_REMAINDER),
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 3.8)

        deco3 = VGroup(
            Text("312÷3", font=FONT, font_size=24, color=COLOR_DIVIDEND),
            Text("=104", font=FONT, font_size=24, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 3.0 + RIGHT * 2.5)

        self.play(
            FadeIn(deco1, scale=0.8),
            FadeIn(deco2, scale=0.8),
            FadeIn(deco3, scale=0.8),
            run_time=0.6,
        )
        self.wait(2.0)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco1), FadeOut(deco2), FadeOut(deco3),
            run_time=1.0,
        )


# 运行命令:
# manim -pql 001_两位数除以一位数.py TwoDigitDivideOneLesson   # 快速预览
# manim -qm  001_两位数除以一位数.py TwoDigitDivideOneLesson   # 中等质量
# manim -qh  001_两位数除以一位数.py TwoDigitDivideOneLesson   # 高质量
