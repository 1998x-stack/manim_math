"""
006_小数加减法.py — 小数加减法 教学动画

知识点:
  - 算理: 相同计数单位相加减
  - 笔算方法: 小数点对齐 (相同数位对齐), 按整数加减法法则计算, 最后对齐小数点
  - 难点: 被减数小数位数少于减数时的补位 (如 3 - 1.25 = 3.00 - 1.25 = 1.75)

年级: 四年级第二学期
格式: TikTok 竖屏 (1080×1920)
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
BG_COLOR     = "#1a1a2e"
COLOR_TITLE  = "#fbbf24"   # 金黄 - 标题
COLOR_KEY    = "#3b82f6"   # 蓝色 - 关键词
COLOR_HL     = "#f59e0b"   # 橙黄 - 高亮
COLOR_ADD    = "#22c55e"   # 绿色 - 加法
COLOR_SUB    = "#ef4444"   # 红色 - 减法
COLOR_DOT    = "#a78bfa"   # 紫色 - 小数点
COLOR_FILL   = "#0f172a"   # 深色填充背景
COLOR_AUTHOR = "#6b7280"   # 灰色作者
COLOR_CARRY  = "#f97316"   # 橙色 - 进位/借位
FONT         = "Heiti SC"


# ======================================================================
# 主场景
# ======================================================================

class DecimalAddSubLesson(Scene):
    """
    小数加减法教学动画
    场景顺序:
      1. 开场钩子
      2. 算理 — 相同计数单位才能相加减
      3. 小数加法竖式 (0.73 + 1.54)
      4. 小数减法竖式 (2.85 - 1.32)
      5. 难点 — 补位 (3 - 1.25 = 3.00 - 1.25)
      6. 规律总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_data()

        self.scene_1_opening()
        self.scene_2_principle()
        self.scene_3_addition()
        self.scene_4_subtraction()
        self.scene_5_补位()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 数据初始化
    # ------------------------------------------------------------------

    def setup_data(self):
        """初始化所有布局参数"""
        # 竖式区域中心 Y 位置
        self.col_center_y = 1.0   # 竖式主体居中
        # 竖式列 X 坐标
        self.col_x = 0.0          # 竖式水平居中

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        """创建作者标识"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_vertical_box(self, width=6.5, height=5.5, center=ORIGIN):
        """创建竖式背景卡片"""
        box = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.25,
            color=WHITE,
            stroke_width=1.5,
            fill_color=COLOR_FILL,
            fill_opacity=0.6,
        ).move_to(center)
        return box

    def make_digit_row(self, digits_str, color=WHITE, font_size=52):
        """
        将字符串中的每个字符作为独立 MathTex 排列成一行。
        digits_str: 如 "0.73" 或 "+1.54"
        返回 VGroup，每个字符是独立 MathTex。
        """
        mobs = []
        for ch in digits_str:
            if ch == '.':
                m = MathTex(r".", font_size=font_size, color=COLOR_DOT)
            elif ch == '+':
                m = MathTex(r"+", font_size=font_size, color=COLOR_ADD)
            elif ch == '-':
                m = MathTex(r"-", font_size=font_size, color=COLOR_SUB)
            elif ch == ' ':
                m = MathTex(r"\phantom{0}", font_size=font_size, color=color)
            else:
                m = MathTex(ch, font_size=font_size, color=color)
            mobs.append(m)
        row = VGroup(*mobs).arrange(RIGHT, buff=0.05, aligned_edge=DOWN)
        return row

    def make_label(self, text, font_size=24, color=WHITE):
        return Text(text, font=FONT, font_size=font_size, color=color)

    def make_highlight_rect(self, mob, color=COLOR_HL, buff=0.08, opacity=0.25):
        """在 mob 周围画高亮矩形"""
        rect = SurroundingRectangle(mob, color=color, buff=buff, corner_radius=0.1)
        rect.set_fill(color=color, opacity=opacity)
        return rect

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "小数加减法",
            font=FONT,
            font_size=52,
            color=COLOR_TITLE,
        ).move_to(UP * 5.5)

        sub = Text(
            "一个对齐就能搞定!",
            font=FONT,
            font_size=28,
            color=GRAY_A,
        ).move_to(UP * 4.6)

        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 问题展示: 0.73 + 1.54 = ?
        q1 = VGroup(
            MathTex(r"0.73 + 1.54 = ?", font_size=44, color=COLOR_ADD),
        ).move_to(UP * 2.8)

        # 问题展示: 3 - 1.25 = ?
        q2 = VGroup(
            MathTex(r"3 - 1.25 = ?", font_size=44, color=COLOR_SUB),
        ).move_to(UP * 1.4)

        self.play(Write(q1), run_time=0.7)
        self.play(Write(q2), run_time=0.7)
        self.wait(1.0)

        # 箭头指向关键:小数点
        dot_hint = Text(
            "关键: 小数点对齐!",
            font=FONT,
            font_size=30,
            color=COLOR_DOT,
        ).move_to(DOWN * 0.2)

        arrow_hint = Arrow(
            dot_hint.get_top() + UP * 0.1,
            dot_hint.get_top() + UP * 0.5,
            color=COLOR_DOT,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2,
        )

        self.play(FadeIn(dot_hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(hook),
            FadeOut(sub),
            FadeOut(q1),
            FadeOut(q2),
            FadeOut(dot_hint),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 算理 — 相同计数单位才能相加减
    # ------------------------------------------------------------------

    def scene_2_principle(self):
        title = Text("为什么要小数点对齐?", font=FONT, font_size=34, color=WHITE)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        # 说明: 相同计数单位才能相加
        explain = Text(
            "相同计数单位的数才能相加减",
            font=FONT,
            font_size=24,
            color=GRAY_A,
        ).move_to(UP * 4.6)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)

        # 数位表
        # 列标题
        header_pos = UP * 3.5
        col_labels = ["个位", "十分位", "百分位"]
        col_colors = [COLOR_ADD, COLOR_KEY, COLOR_DOT]
        col_xs = [-2.5, 0.0, 2.5]

        header_group = VGroup()
        for lbl, cx, cc in zip(col_labels, col_xs, col_colors):
            t = Text(lbl, font=FONT, font_size=22, color=cc)
            t.move_to(header_pos + RIGHT * cx)
            header_group.add(t)

        self.play(FadeIn(header_group), run_time=0.5)

        # 分隔线
        sep_line = Line(
            LEFT * 4.0 + UP * 3.1, RIGHT * 4.0 + UP * 3.1,
            color=GRAY_C, stroke_width=1.5,
        )
        self.play(Create(sep_line), run_time=0.3)

        # 数字 0.73
        row1_vals = ["0", "7", "3"]
        row1_group = VGroup()
        row1_y = UP * 2.5
        for val, cx, cc in zip(row1_vals, col_xs, col_colors):
            t = MathTex(val, font_size=38, color=cc)
            t.move_to(row1_y + RIGHT * cx)
            row1_group.add(t)

        # 数字 1.54
        row2_vals = ["1", "5", "4"]
        row2_group = VGroup()
        row2_y = UP * 1.6
        for val, cx, cc in zip(row2_vals, col_xs, col_colors):
            t = MathTex(val, font_size=38, color=cc)
            t.move_to(row2_y + RIGHT * cx)
            row2_group.add(t)

        num1_label = Text("0.73", font=FONT, font_size=26, color=WHITE).move_to(row1_y + LEFT * 4.0)
        num2_label = Text("1.54", font=FONT, font_size=26, color=WHITE).move_to(row2_y + LEFT * 4.0)

        self.play(FadeIn(num1_label), FadeIn(row1_group), run_time=0.6)
        self.play(FadeIn(num2_label), FadeIn(row2_group), run_time=0.6)

        # 高亮同位数
        boxes = VGroup()
        for i, (cx, cc) in enumerate(zip(col_xs, col_colors)):
            rect = RoundedRectangle(
                width=1.4, height=1.8, corner_radius=0.1,
                color=cc, stroke_width=2,
                fill_color=cc, fill_opacity=0.1,
            )
            rect.move_to(UP * 2.05 + RIGHT * cx)
            boxes.add(rect)

        self.play(FadeIn(boxes), run_time=0.5)

        same_unit = Text(
            "相同数位对齐 = 相同计数单位相加减",
            font=FONT,
            font_size=21,
            color=COLOR_HL,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(same_unit, shift=UP * 0.2), run_time=0.5)

        key_rule = Text(
            "小数点对齐就保证了数位对齐!",
            font=FONT,
            font_size=24,
            color=COLOR_DOT,
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(key_rule, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(explain),
            FadeOut(header_group), FadeOut(sep_line),
            FadeOut(row1_group), FadeOut(row2_group),
            FadeOut(num1_label), FadeOut(num2_label),
            FadeOut(boxes),
            FadeOut(same_unit), FadeOut(key_rule),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 小数加法竖式 — 0.73 + 1.54
    # ------------------------------------------------------------------

    def scene_3_addition(self):
        title = Text("小数加法", font=FONT, font_size=36, color=COLOR_ADD)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        ex_line = VGroup(
            MathTex(r"0.73 + 1.54 = ?", font_size=40, color=WHITE),
        ).move_to(UP * 4.6)
        self.play(Write(ex_line), run_time=0.6)
        self.wait(0.4)

        # 竖式背景
        box = self.make_vertical_box(width=6.0, height=6.5, center=UP * 1.0)
        self.play(FadeIn(box), run_time=0.4)

        # 竖式布局参数
        row_top_y   = UP * 3.0
        row_mid_y   = UP * 2.0
        row_res_y   = UP * 0.9

        # 数字列 X 坐标 (从左: 个位, 小数点, 十分位, 百分位)
        # 格式: " 0 . 7 3"  and "+1 . 5 4"
        #         个  .  十  百
        xs_int  = -1.5    # 个位
        xs_dot  = -0.75   # 小数点
        xs_tenth = 0.0    # 十分位
        xs_hund  = 0.75   # 百分位

        # --- 第一行: 0.73 ---
        d_0   = MathTex(r"0", font_size=52, color=WHITE).move_to(row_top_y + RIGHT * xs_int)
        d_dot1 = MathTex(r".", font_size=52, color=COLOR_DOT).move_to(row_top_y + RIGHT * xs_dot)
        d_7   = MathTex(r"7", font_size=52, color=WHITE).move_to(row_top_y + RIGHT * xs_tenth)
        d_3   = MathTex(r"3", font_size=52, color=WHITE).move_to(row_top_y + RIGHT * xs_hund)
        row1 = VGroup(d_0, d_dot1, d_7, d_3)

        # --- 第二行: +1.54 ---
        d_plus = MathTex(r"+", font_size=52, color=COLOR_ADD).move_to(row_mid_y + LEFT * 2.5)
        d_1    = MathTex(r"1", font_size=52, color=WHITE).move_to(row_mid_y + RIGHT * xs_int)
        d_dot2 = MathTex(r".", font_size=52, color=COLOR_DOT).move_to(row_mid_y + RIGHT * xs_dot)
        d_5   = MathTex(r"5", font_size=52, color=WHITE).move_to(row_mid_y + RIGHT * xs_tenth)
        d_4   = MathTex(r"4", font_size=52, color=WHITE).move_to(row_mid_y + RIGHT * xs_hund)
        row2 = VGroup(d_plus, d_1, d_dot2, d_5, d_4)

        # 横线
        h_line = Line(
            LEFT * 2.8 + UP * 1.45, RIGHT * 1.4 + UP * 1.45,
            color=WHITE, stroke_width=2.5,
        )

        # --- 结果行 ---
        r_1   = MathTex(r"2", font_size=52, color=COLOR_ADD).move_to(row_res_y + RIGHT * xs_int)
        r_dot = MathTex(r".", font_size=52, color=COLOR_DOT).move_to(row_res_y + RIGHT * xs_dot)
        r_2   = MathTex(r"2", font_size=52, color=COLOR_ADD).move_to(row_res_y + RIGHT * xs_tenth)
        r_7   = MathTex(r"7", font_size=52, color=COLOR_ADD).move_to(row_res_y + RIGHT * xs_hund)
        row_res = VGroup(r_1, r_dot, r_2, r_7)

        # Step 1: 写出被加数和加数
        step_lbl = Text("第一步: 小数点对齐", font=FONT, font_size=24, color=COLOR_KEY)
        step_lbl.move_to(DOWN * 1.8)

        self.play(Write(row1), run_time=0.8)
        self.play(Write(row2), run_time=0.8)
        self.play(FadeIn(step_lbl, shift=UP * 0.2), run_time=0.4)

        # 高亮两个小数点
        hl_dot1 = self.make_highlight_rect(d_dot1, color=COLOR_DOT, buff=0.1, opacity=0.4)
        hl_dot2 = self.make_highlight_rect(d_dot2, color=COLOR_DOT, buff=0.1, opacity=0.4)
        self.play(FadeIn(hl_dot1), FadeIn(hl_dot2), run_time=0.4)
        self.wait(1.0)

        # 画竖向对齐线(穿过两个小数点)
        dot_align_line = DashedLine(
            UP * 3.5 + RIGHT * xs_dot, UP * 1.5 + RIGHT * xs_dot,
            color=COLOR_DOT, stroke_width=2, dash_length=0.12,
        )
        self.play(Create(dot_align_line), run_time=0.5)
        self.wait(0.5)

        # Step 2: 画横线
        step_lbl2 = Text("第二步: 按整数加减法计算", font=FONT, font_size=24, color=COLOR_KEY)
        step_lbl2.move_to(DOWN * 1.8)
        self.play(
            ReplacementTransform(step_lbl, step_lbl2),
            Create(h_line),
            run_time=0.6,
        )

        # 逐列计算: 百分位 3+4=7
        col_hund_hl = self.make_highlight_rect(
            VGroup(d_3, d_4), color=COLOR_HL, buff=0.15, opacity=0.2,
        )
        calc_hund = Text("3+4=7", font=FONT, font_size=22, color=COLOR_HL)
        calc_hund.move_to(DOWN * 2.8)
        self.play(FadeIn(col_hund_hl), FadeIn(calc_hund), run_time=0.4)
        self.play(Write(r_7), run_time=0.5)
        self.play(FadeOut(col_hund_hl), FadeOut(calc_hund), run_time=0.3)

        # 十分位 7+5=12, 写2进1
        col_tenth_hl = self.make_highlight_rect(
            VGroup(d_7, d_5), color=COLOR_HL, buff=0.15, opacity=0.2,
        )
        calc_tenth = Text("7+5=12, 写2进1", font=FONT, font_size=22, color=COLOR_HL)
        calc_tenth.move_to(DOWN * 2.8)
        carry_1 = MathTex(r"1", font_size=28, color=COLOR_CARRY)
        carry_1.move_to(UP * 3.5 + RIGHT * xs_int)   # 进位放在个位上方
        self.play(FadeIn(col_tenth_hl), FadeIn(calc_tenth), run_time=0.4)
        self.play(Write(r_2), FadeIn(carry_1), run_time=0.5)
        self.play(FadeOut(col_tenth_hl), FadeOut(calc_tenth), run_time=0.3)

        # 个位 0+1+1(进位)=2
        col_int_hl = self.make_highlight_rect(
            VGroup(d_0, d_1, carry_1), color=COLOR_HL, buff=0.15, opacity=0.2,
        )
        calc_int = Text("0+1+1(进位)=2", font=FONT, font_size=22, color=COLOR_HL)
        calc_int.move_to(DOWN * 2.8)
        self.play(FadeIn(col_int_hl), FadeIn(calc_int), run_time=0.4)
        self.play(Write(r_1), run_time=0.5)
        self.play(FadeOut(col_int_hl), FadeOut(calc_int), run_time=0.3)

        # Step 3: 对齐小数点
        step_lbl3 = Text("第三步: 对齐小数点", font=FONT, font_size=24, color=COLOR_KEY)
        step_lbl3.move_to(DOWN * 1.8)
        self.play(ReplacementTransform(step_lbl2, step_lbl3), run_time=0.4)

        # 在结果行写小数点并高亮
        self.play(Write(r_dot), run_time=0.4)
        hl_res_dot = self.make_highlight_rect(r_dot, color=COLOR_DOT, buff=0.12, opacity=0.5)
        self.play(FadeIn(hl_res_dot), run_time=0.3)
        self.wait(0.5)

        # 显示完整答案  0.73 + 1.54 = 2.27
        ans_line = VGroup(
            MathTex(r"0.73 + 1.54 = ", font_size=38, color=WHITE),
            MathTex(r"2.27", font_size=38, color=COLOR_ADD),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.2)

        self.play(FadeIn(ans_line, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(ex_line), FadeOut(box),
            FadeOut(row1), FadeOut(row2), FadeOut(h_line),
            FadeOut(row_res), FadeOut(carry_1),
            FadeOut(hl_dot1), FadeOut(hl_dot2),
            FadeOut(dot_align_line),
            FadeOut(step_lbl3), FadeOut(hl_res_dot),
            FadeOut(ans_line),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 4: 小数减法竖式 — 2.85 - 1.32
    # ------------------------------------------------------------------

    def scene_4_subtraction(self):
        title = Text("小数减法", font=FONT, font_size=36, color=COLOR_SUB)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        ex_line = MathTex(r"2.85 - 1.32 = ?", font_size=40, color=WHITE)
        ex_line.move_to(UP * 4.6)
        self.play(Write(ex_line), run_time=0.6)
        self.wait(0.4)

        # 竖式背景
        box = self.make_vertical_box(width=6.0, height=6.5, center=UP * 1.0)
        self.play(FadeIn(box), run_time=0.4)

        # 列X坐标
        xs_int   = -1.5
        xs_dot   = -0.75
        xs_tenth =  0.0
        xs_hund  =  0.75

        row_top_y = UP * 3.0
        row_mid_y = UP * 2.0
        row_res_y = UP * 0.9

        # --- 第一行: 2.85 (被减数) ---
        a_2   = MathTex(r"2", font_size=52, color=WHITE).move_to(row_top_y + RIGHT * xs_int)
        a_dot = MathTex(r".", font_size=52, color=COLOR_DOT).move_to(row_top_y + RIGHT * xs_dot)
        a_8   = MathTex(r"8", font_size=52, color=WHITE).move_to(row_top_y + RIGHT * xs_tenth)
        a_5   = MathTex(r"5", font_size=52, color=WHITE).move_to(row_top_y + RIGHT * xs_hund)
        row1 = VGroup(a_2, a_dot, a_8, a_5)

        # --- 第二行: -1.32 (减数) ---
        b_minus = MathTex(r"-", font_size=52, color=COLOR_SUB).move_to(row_mid_y + LEFT * 2.5)
        b_1     = MathTex(r"1", font_size=52, color=WHITE).move_to(row_mid_y + RIGHT * xs_int)
        b_dot   = MathTex(r".", font_size=52, color=COLOR_DOT).move_to(row_mid_y + RIGHT * xs_dot)
        b_3     = MathTex(r"3", font_size=52, color=WHITE).move_to(row_mid_y + RIGHT * xs_tenth)
        b_2     = MathTex(r"2", font_size=52, color=WHITE).move_to(row_mid_y + RIGHT * xs_hund)
        row2 = VGroup(b_minus, b_1, b_dot, b_3, b_2)

        h_line = Line(
            LEFT * 2.8 + UP * 1.45, RIGHT * 1.4 + UP * 1.45,
            color=WHITE, stroke_width=2.5,
        )

        # --- 结果: 1.53 ---
        r_1   = MathTex(r"1", font_size=52, color=COLOR_SUB).move_to(row_res_y + RIGHT * xs_int)
        r_dot = MathTex(r".", font_size=52, color=COLOR_DOT).move_to(row_res_y + RIGHT * xs_dot)
        r_5   = MathTex(r"5", font_size=52, color=COLOR_SUB).move_to(row_res_y + RIGHT * xs_tenth)
        r_3   = MathTex(r"3", font_size=52, color=COLOR_SUB).move_to(row_res_y + RIGHT * xs_hund)
        row_res = VGroup(r_1, r_dot, r_5, r_3)

        # Step 1: 写出被减数和减数, 小数点对齐
        step_lbl = Text("第一步: 小数点对齐", font=FONT, font_size=24, color=COLOR_KEY)
        step_lbl.move_to(DOWN * 1.8)

        self.play(Write(row1), run_time=0.8)
        self.play(Write(row2), run_time=0.8)
        self.play(FadeIn(step_lbl, shift=UP * 0.2), run_time=0.4)

        hl_dot1 = self.make_highlight_rect(a_dot, color=COLOR_DOT, buff=0.1, opacity=0.4)
        hl_dot2 = self.make_highlight_rect(b_dot, color=COLOR_DOT, buff=0.1, opacity=0.4)
        self.play(FadeIn(hl_dot1), FadeIn(hl_dot2), run_time=0.4)

        dot_align_line = DashedLine(
            UP * 3.5 + RIGHT * xs_dot, UP * 1.5 + RIGHT * xs_dot,
            color=COLOR_DOT, stroke_width=2, dash_length=0.12,
        )
        self.play(Create(dot_align_line), run_time=0.5)
        self.wait(0.5)

        # Step 2: 计算
        step_lbl2 = Text("第二步: 按整数减法计算", font=FONT, font_size=24, color=COLOR_KEY)
        step_lbl2.move_to(DOWN * 1.8)
        self.play(
            ReplacementTransform(step_lbl, step_lbl2),
            Create(h_line),
            run_time=0.6,
        )

        # 百分位 5-2=3
        col_hund_hl = self.make_highlight_rect(
            VGroup(a_5, b_2), color=COLOR_HL, buff=0.15, opacity=0.2,
        )
        calc_hund = Text("5-2=3", font=FONT, font_size=22, color=COLOR_HL)
        calc_hund.move_to(DOWN * 2.8)
        self.play(FadeIn(col_hund_hl), FadeIn(calc_hund), run_time=0.4)
        self.play(Write(r_3), run_time=0.5)
        self.play(FadeOut(col_hund_hl), FadeOut(calc_hund), run_time=0.3)

        # 十分位 8-3=5
        col_tenth_hl = self.make_highlight_rect(
            VGroup(a_8, b_3), color=COLOR_HL, buff=0.15, opacity=0.2,
        )
        calc_tenth = Text("8-3=5", font=FONT, font_size=22, color=COLOR_HL)
        calc_tenth.move_to(DOWN * 2.8)
        self.play(FadeIn(col_tenth_hl), FadeIn(calc_tenth), run_time=0.4)
        self.play(Write(r_5), run_time=0.5)
        self.play(FadeOut(col_tenth_hl), FadeOut(calc_tenth), run_time=0.3)

        # 个位 2-1=1
        col_int_hl = self.make_highlight_rect(
            VGroup(a_2, b_1), color=COLOR_HL, buff=0.15, opacity=0.2,
        )
        calc_int = Text("2-1=1", font=FONT, font_size=22, color=COLOR_HL)
        calc_int.move_to(DOWN * 2.8)
        self.play(FadeIn(col_int_hl), FadeIn(calc_int), run_time=0.4)
        self.play(Write(r_1), run_time=0.5)
        self.play(FadeOut(col_int_hl), FadeOut(calc_int), run_time=0.3)

        # Step 3: 对齐小数点
        step_lbl3 = Text("第三步: 对齐小数点", font=FONT, font_size=24, color=COLOR_KEY)
        step_lbl3.move_to(DOWN * 1.8)
        self.play(ReplacementTransform(step_lbl2, step_lbl3), run_time=0.4)
        self.play(Write(r_dot), run_time=0.4)
        hl_res_dot = self.make_highlight_rect(r_dot, color=COLOR_DOT, buff=0.12, opacity=0.5)
        self.play(FadeIn(hl_res_dot), run_time=0.3)
        self.wait(0.5)

        ans_line = VGroup(
            MathTex(r"2.85 - 1.32 = ", font_size=38, color=WHITE),
            MathTex(r"1.53", font_size=38, color=COLOR_SUB),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.2)
        self.play(FadeIn(ans_line, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(ex_line), FadeOut(box),
            FadeOut(row1), FadeOut(row2), FadeOut(h_line),
            FadeOut(row_res),
            FadeOut(hl_dot1), FadeOut(hl_dot2),
            FadeOut(dot_align_line),
            FadeOut(step_lbl3), FadeOut(hl_res_dot),
            FadeOut(ans_line),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 5: 难点 — 补位 (3 - 1.25 = 3.00 - 1.25 = 1.75)
    # ------------------------------------------------------------------

    def scene_5_补位(self):
        title = Text("难点: 位数不够怎么办?", font=FONT, font_size=32, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        ex_line = MathTex(r"3 - 1.25 = ?", font_size=44, color=WHITE)
        ex_line.move_to(UP * 4.6)
        self.play(Write(ex_line), run_time=0.6)

        # 疑问: 3 没有小数位, 怎么对齐?
        question = Text(
            "3没有小数位, 怎么对齐?",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 3.8)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 答案: 把 3 看作 3.00
        arrow_eq = MathTex(r"3 = 3.00", font_size=40, color=COLOR_DOT)
        arrow_eq.move_to(UP * 2.8)
        self.play(Write(arrow_eq), run_time=0.7)

        补位_explain = Text(
            "在整数末尾补零, 不改变大小!",
            font=FONT, font_size=22, color=COLOR_DOT,
        ).move_to(UP * 2.0)
        self.play(FadeIn(补位_explain, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理说明文字
        self.play(
            FadeOut(question), FadeOut(arrow_eq), FadeOut(补位_explain),
            run_time=0.4,
        )

        # 竖式背景
        box = self.make_vertical_box(width=6.5, height=7.0, center=UP * 0.5)
        self.play(FadeIn(box), run_time=0.4)

        # 列X坐标 (整数, 小数点, 十分位, 百分位)
        xs_int   = -1.8
        xs_dot   = -1.0
        xs_tenth =  -0.2
        xs_hund  =   0.6

        row_top_y = UP * 2.8
        row_mid_y = UP * 1.7
        row_res_y = UP * 0.5

        # --- 先写 3 (错误示例) ---
        wrong_3 = MathTex(r"3", font_size=52, color=WHITE)
        wrong_3.move_to(row_top_y + RIGHT * xs_int)
        wrong_label = Text("(被减数)", font=FONT, font_size=20, color=GRAY_B)
        wrong_label.move_to(row_top_y + LEFT * 3.2)

        b_minus2 = MathTex(r"-", font_size=52, color=COLOR_SUB).move_to(row_mid_y + LEFT * 3.0)
        b_1b     = MathTex(r"1", font_size=52, color=WHITE).move_to(row_mid_y + RIGHT * xs_int)
        b_dot2   = MathTex(r".", font_size=52, color=COLOR_DOT).move_to(row_mid_y + RIGHT * xs_dot)
        b_2b     = MathTex(r"2", font_size=52, color=WHITE).move_to(row_mid_y + RIGHT * xs_tenth)
        b_5b     = MathTex(r"5", font_size=52, color=WHITE).move_to(row_mid_y + RIGHT * xs_hund)
        row2b = VGroup(b_minus2, b_1b, b_dot2, b_2b, b_5b)

        self.play(FadeIn(wrong_3), FadeIn(wrong_label), run_time=0.5)
        self.play(Write(row2b), run_time=0.8)

        # 问号: 对不齐!
        q_mark = MathTex(r"?", font_size=40, color=COLOR_SUB)
        q_mark.move_to(row_top_y + RIGHT * xs_dot)
        self.play(Write(q_mark), run_time=0.4)
        self.wait(0.5)

        # 转换: 3 → 3.00
        step_hint = Text("把 3 写成 3.00", font=FONT, font_size=26, color=COLOR_HL)
        step_hint.move_to(DOWN * 2.0)
        self.play(FadeIn(step_hint, shift=UP * 0.2), run_time=0.4)

        # 把 wrong_3 和 q_mark 变成 3.00
        new_3    = MathTex(r"3", font_size=52, color=WHITE).move_to(row_top_y + RIGHT * xs_int)
        new_dot  = MathTex(r".", font_size=52, color=COLOR_DOT).move_to(row_top_y + RIGHT * xs_dot)
        new_0_t  = MathTex(r"0", font_size=52, color=COLOR_KEY).move_to(row_top_y + RIGHT * xs_tenth)
        new_0_h  = MathTex(r"0", font_size=52, color=COLOR_KEY).move_to(row_top_y + RIGHT * xs_hund)

        self.play(
            FadeOut(q_mark),
            Transform(wrong_3, new_3),
            run_time=0.3,
        )
        self.play(
            Write(new_dot),
            Write(new_0_t),
            Write(new_0_h),
            run_time=0.7,
        )

        # 高亮补的零
        hl_zeros = self.make_highlight_rect(
            VGroup(new_0_t, new_0_h), color=COLOR_KEY, buff=0.12, opacity=0.35,
        )
        self.play(FadeIn(hl_zeros), run_time=0.3)

        zeros_label = Text("补的零 (不改变大小)", font=FONT, font_size=20, color=COLOR_KEY)
        zeros_label.move_to(DOWN * 2.7)
        self.play(
            FadeOut(step_hint),
            FadeIn(zeros_label),
            run_time=0.4,
        )
        self.wait(0.8)

        # 画横线
        h_line2 = Line(
            LEFT * 3.2 + UP * 1.1, RIGHT * 1.4 + UP * 1.1,
            color=WHITE, stroke_width=2.5,
        )
        self.play(Create(h_line2), run_time=0.4)

        # 计算 3.00 - 1.25
        # 百分位: 0-5 不够减, 借位: 10-5=5
        borrow_t_label = Text("十分位借1", font=FONT, font_size=20, color=COLOR_CARRY)
        borrow_t_label.move_to(row_top_y + RIGHT * (xs_tenth + 0.5) + UP * 0.55)

        borrow_top = MathTex(r"10", font_size=28, color=COLOR_CARRY)
        borrow_top.move_to(row_top_y + RIGHT * xs_hund + UP * 0.55)

        self.play(
            FadeOut(zeros_label),
            FadeIn(borrow_top),
            FadeIn(borrow_t_label),
            run_time=0.4,
        )
        calc_h = Text("10-5=5", font=FONT, font_size=22, color=COLOR_HL)
        calc_h.move_to(DOWN * 2.5)
        self.play(FadeIn(calc_h), run_time=0.3)

        r_5_b = MathTex(r"5", font_size=52, color=COLOR_SUB).move_to(row_res_y + RIGHT * xs_hund)
        self.play(Write(r_5_b), run_time=0.4)
        self.play(FadeOut(borrow_top), FadeOut(borrow_t_label), FadeOut(calc_h), run_time=0.3)

        # 十分位: 0-1-1(借)-2 = 借位: 10-1-2=7  (0 借给了百分位 → 剩-1, 再从个位借1 → 10-1=9, 9-2=7)
        # Actually: tenths digit is 0 (from 3.00), minus 2 (tenths of 1.25), but we already borrowed 1 to hundredths
        # So tenths: 0 - 1(borrow to hundredths) - 2 = -3, borrow from ones: 10 - 1 - 2 = 7
        borrow_int_label = Text("个位借1", font=FONT, font_size=20, color=COLOR_CARRY)
        borrow_int_label.move_to(row_top_y + RIGHT * (xs_int + 0.4) + UP * 0.55)
        borrow_top2 = MathTex(r"10", font_size=28, color=COLOR_CARRY)
        borrow_top2.move_to(row_top_y + RIGHT * xs_tenth + UP * 0.55)

        self.play(FadeIn(borrow_top2), FadeIn(borrow_int_label), run_time=0.4)
        calc_t = Text("10-1-2=7", font=FONT, font_size=22, color=COLOR_HL)
        calc_t.move_to(DOWN * 2.5)
        self.play(FadeIn(calc_t), run_time=0.3)

        r_7_b = MathTex(r"7", font_size=52, color=COLOR_SUB).move_to(row_res_y + RIGHT * xs_tenth)
        self.play(Write(r_7_b), run_time=0.4)
        self.play(FadeOut(borrow_top2), FadeOut(borrow_int_label), FadeOut(calc_t), run_time=0.3)

        # 个位: 3-1-1(借位)=1
        calc_i = Text("3-1-1=1", font=FONT, font_size=22, color=COLOR_HL)
        calc_i.move_to(DOWN * 2.5)
        self.play(FadeIn(calc_i), run_time=0.3)
        r_1_b = MathTex(r"1", font_size=52, color=COLOR_SUB).move_to(row_res_y + RIGHT * xs_int)
        self.play(Write(r_1_b), run_time=0.4)
        self.play(FadeOut(calc_i), run_time=0.3)

        # 小数点
        r_dot_b = MathTex(r".", font_size=52, color=COLOR_DOT).move_to(row_res_y + RIGHT * xs_dot)
        self.play(Write(r_dot_b), run_time=0.4)

        # 答案
        ans_b = VGroup(
            MathTex(r"3 - 1.25 = ", font_size=38, color=WHITE),
            MathTex(r"1.75", font_size=38, color=COLOR_SUB),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.2)
        self.play(FadeIn(ans_b, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(ex_line), FadeOut(box),
            FadeOut(wrong_3), FadeOut(wrong_label),
            FadeOut(row2b), FadeOut(h_line2),
            FadeOut(new_dot), FadeOut(new_0_t), FadeOut(new_0_h),
            FadeOut(hl_zeros),
            FadeOut(r_5_b), FadeOut(r_7_b), FadeOut(r_1_b), FadeOut(r_dot_b),
            FadeOut(ans_b),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 6: 规律总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = Text("小数加减法小结", font=FONT, font_size=36, color=COLOR_TITLE)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 背景卡片
        card = RoundedRectangle(
            width=7.8, height=10.5,
            corner_radius=0.3,
            color=WHITE,
            stroke_width=1.5,
            fill_color=COLOR_FILL,
            fill_opacity=0.7,
        ).move_to(UP * 0.0)
        self.play(FadeIn(card), run_time=0.4)

        # 三步骤
        steps_data = [
            ("第一步", "小数点对齐", COLOR_ADD,  UP * 3.8),
            ("第二步", "按整数法则计算", COLOR_KEY, UP * 2.2),
            ("第三步", "对齐小数点", COLOR_DOT,  UP * 0.6),
        ]

        step_items = VGroup()
        for num, desc, color, pos in steps_data:
            num_t  = Text(num,  font=FONT, font_size=28, color=color)
            desc_t = Text(desc, font=FONT, font_size=24, color=WHITE)
            row = VGroup(num_t, desc_t).arrange(RIGHT, buff=0.4)
            row.move_to(pos)
            step_items.add(row)

        for item in step_items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        # 分隔线
        sep = Line(LEFT * 3.5 + DOWN * 0.9, RIGHT * 3.5 + DOWN * 0.9,
                   color=GRAY_C, stroke_width=1.5)
        self.play(Create(sep), run_time=0.3)

        # 难点提示
        key_note_title = Text("难点提示:", font=FONT, font_size=26, color=COLOR_HL)
        key_note_title.move_to(DOWN * 1.4 + LEFT * 2.0)
        self.play(FadeIn(key_note_title, shift=RIGHT * 0.3), run_time=0.4)

        key_note1 = VGroup(
            MathTex(r"3 - 1.25", font_size=30, color=WHITE),
            Text("→", font=FONT, font_size=26, color=COLOR_HL),
            MathTex(r"3.00 - 1.25", font_size=30, color=COLOR_KEY),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.2)
        self.play(FadeIn(key_note1, shift=RIGHT * 0.3), run_time=0.5)

        key_note2 = Text(
            "位数不足时在末尾补零",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 3.1)
        self.play(FadeIn(key_note2, shift=RIGHT * 0.3), run_time=0.4)

        # 核心口诀
        mantra_bg = RoundedRectangle(
            width=7.2, height=1.2,
            corner_radius=0.2,
            color=COLOR_HL,
            stroke_width=2,
            fill_color=COLOR_HL,
            fill_opacity=0.15,
        ).move_to(DOWN * 4.5)
        mantra = Text(
            "小数点对齐, 计算不出错!",
            font=FONT, font_size=26, color=COLOR_HL,
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(mantra_bg), FadeIn(mantra), run_time=0.5)

        self.wait(3.0)

        self.play(
            FadeOut(title), FadeOut(card),
            FadeOut(step_items), FadeOut(sep),
            FadeOut(key_note_title), FadeOut(key_note1), FadeOut(key_note2),
            FadeOut(mantra_bg), FadeOut(mantra),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE,
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
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 装饰: 几个小数点和计算符号
        deco_items = VGroup(
            MathTex(r"+", font_size=48, color=COLOR_ADD),
            MathTex(r"-", font_size=48, color=COLOR_SUB),
            MathTex(r".", font_size=56, color=COLOR_DOT),
            MathTex(r"=", font_size=48, color=COLOR_KEY),
        )
        deco_items.arrange(RIGHT, buff=0.6).move_to(DOWN * 2.5)
        self.play(
            *[FadeIn(d, scale=0.5) for d in deco_items],
            run_time=0.7,
        )

        # 公式展示
        formula_show = VGroup(
            MathTex(r"0.73 + 1.54 = 2.27", font_size=30, color=COLOR_ADD),
            MathTex(r"3 - 1.25 = 1.75", font_size=30, color=COLOR_SUB),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 4.2)
        self.play(FadeIn(formula_show, shift=UP * 0.2), run_time=0.6)

        self.wait(2.5)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco_items),
            FadeOut(formula_show),
            run_time=1.0,
        )


# 运行命令:
# manim -qm 006_小数加减法.py DecimalAddSubLesson
