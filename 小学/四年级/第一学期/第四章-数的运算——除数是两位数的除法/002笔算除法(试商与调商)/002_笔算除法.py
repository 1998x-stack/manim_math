"""
002_笔算除法.py — 笔算除法（试商与调商）教学动画

知识点: 除数是两位数的笔算除法——试商与调商
  - 四舍五入法试商：将除数看作最接近的整十数
  - 灵活试商：除数个位是 4/5/6 时可能需要调商
  - 同头无除商 8、9 技巧
  - 竖式演示：写商 → 乘 → 减 → 验余数

年级: 四年级第一学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR       = "#1a1a2e"
COLOR_DIVIDEND = "#3b82f6"   # 蓝  被除数
COLOR_DIVISOR  = "#f59e0b"   # 橙  除数
COLOR_QUOTIENT = "#22c55e"   # 绿  商
COLOR_REMAIN   = "#f87171"   # 红  余数
COLOR_ARROW    = "#a78bfa"   # 紫  箭头/变换
COLOR_HL       = "#fbbf24"   # 黄  高亮
COLOR_GRAY_TXT = "#9ca3af"   # 灰  辅助文字
COLOR_AUTHOR   = "#6b7280"   # 灰  作者
COLOR_STEP     = "#38bdf8"   # 青  步骤标题
FONT           = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class WrittenDivisionLesson(Scene):
    """
    笔算除法（试商与调商）教学动画

    场景顺序:
      1. 开场钩子     — 抛出问题 952 ÷ 34
      2. 试商方法     — 四舍五入法：34 → 30，看商几
      3. 竖式演示     — 一步步写竖式（试商 3，偏小 → 调大为 4）
      4. 调商规则     — "余数≥除数→调大，乘积>被除数→调小"
      5. 再练一练     — 例题 672 ÷ 21（整除，无需调商）
      6. 同头无除     — 技巧：被除数前几位与除数"同头"时商 8、9
      7. 规律总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_trial_quotient()
        self.scene_3_long_division()
        self.scene_4_adjust_rules()
        self.scene_5_more_examples()
        self.scene_6_same_head_trick()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """初始化常用数值"""
        # 主例题 952 ÷ 34
        self.eg1_dividend = 952
        self.eg1_divisor  = 34
        self.eg1_quotient = 28
        self.eg1_remain   = 0

        # 第二例题 672 ÷ 21
        self.eg2_dividend = 672
        self.eg2_divisor  = 21
        self.eg2_quotient = 32
        self.eg2_remain   = 0

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_title(self, text, color=COLOR_HL, font_size=32):
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(UP * 5.8)

    def make_step_text(self, text, pos, color=COLOR_GRAY_TXT, font_size=22):
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(pos)

    def make_rounded_rect(self, width, height, pos, color=WHITE, fill_opacity=0.07):
        """带圆角的背景矩形"""
        return RoundedRectangle(
            width=width, height=height,
            corner_radius=0.3,
            color=color, stroke_width=1.5,
            fill_color=color, fill_opacity=fill_opacity,
        ).move_to(pos)

    # ------------------------------------------------------------------
    # 竖式绘图助手
    # ------------------------------------------------------------------

    def build_long_division(
        self,
        dividend_str,
        divisor_str,
        quotient_str,
        partial_products,   # list of (subtracted_str, remainder_str, bring_down_str or "")
        center=ORIGIN,
        scale=1.0,
    ):
        """
        绘制竖式的各层元素，返回 VGroup.
        只用 MathTex 显示数字，文字说明用 Text 单独处理。

        layout (logical units, scale=1):
          ┌──────────────────────────────┐
          │  divisor ) dividend  quotient│
          │            ─────────         │
          │            partial0          │
          │          ─ ─ ─ ─ ─          │
          │            rem0 ↓bringdown  │
          │            ...               │
          └──────────────────────────────┘
        """
        group = VGroup()

        # 字体大小
        fs = int(44 * scale)

        # 除数和被除数，第一行
        divisor_tex  = MathTex(divisor_str,  font_size=fs, color=COLOR_DIVISOR)
        dividend_tex = MathTex(dividend_str, font_size=fs, color=COLOR_DIVIDEND)
        quotient_tex = MathTex(quotient_str, font_size=fs, color=COLOR_QUOTIENT)

        # 布局参考 x 原点
        ox, oy, _ = center

        # 宽度估算
        div_w  = len(divisor_str)  * 0.30 * scale
        dnd_w  = len(dividend_str) * 0.30 * scale

        # 位置
        divisor_tex.move_to([ox - dnd_w * 0.5 - 0.25 * scale, oy, 0])
        dividend_tex.move_to([ox + div_w * 0.5 * 0.5,         oy, 0])

        # ） 符号
        paren_x = ox - dnd_w * 0.5 + 0.12 * scale
        paren   = MathTex(r"\big)", font_size=fs + 6, color=WHITE)
        paren.move_to([paren_x, oy, 0])

        # 商放在被除数右上
        quotient_tex.move_to([ox + dnd_w * 0.4 + 0.55 * scale, oy + 0.55 * scale, 0])

        group.add(divisor_tex, dividend_tex, paren, quotient_tex)

        # 第一条横线（在被除数下方）
        line_y   = oy - 0.45 * scale
        line_x0  = ox - 0.05 * scale
        line_x1  = ox + dnd_w * 0.55 + 0.3 * scale
        h_line1  = Line([line_x0, line_y, 0], [line_x1, line_y, 0],
                        color=WHITE, stroke_width=2)
        group.add(h_line1)

        # 各层减法
        current_y = line_y - 0.55 * scale
        for i, (sub_str, rem_str, bring_str) in enumerate(partial_products):
            sub_tex = MathTex(sub_str, font_size=int(36 * scale), color=COLOR_ARROW)
            sub_tex.move_to([line_x1 - 0.25 * scale - len(sub_str) * 0.12 * scale,
                             current_y, 0])
            group.add(sub_tex)

            current_y -= 0.50 * scale

            # 减法线
            sub_line = Line(
                [line_x0, current_y, 0],
                [line_x1, current_y, 0],
                color=WHITE, stroke_width=1.5,
            )
            group.add(sub_line)
            current_y -= 0.48 * scale

            # 余数（+ bring down）
            rem_full = rem_str + bring_str
            rem_color = COLOR_REMAIN if i == len(partial_products) - 1 else COLOR_DIVIDEND
            rem_tex = MathTex(rem_full, font_size=int(36 * scale), color=rem_color)
            rem_tex.move_to([line_x1 - 0.25 * scale - len(rem_full) * 0.12 * scale,
                             current_y, 0])
            group.add(rem_tex)

            current_y -= 0.55 * scale

        return group

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text("笔算除法,", font=FONT, font_size=42, color=COLOR_HL).move_to(UP * 5.2)
        hook2 = Text("你会试商吗?", font=FONT, font_size=42, color=COLOR_HL).move_to(UP * 4.4)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.6)

        # 主算式
        main = MathTex(r"952 \div 34 = \;?", font_size=58, color=WHITE).move_to(UP * 2.8)
        main[0][0:3].set_color(COLOR_DIVIDEND)
        main[0][4:6].set_color(COLOR_DIVISOR)
        self.play(Write(main), run_time=0.9)
        self.wait(0.5)

        sub = Text("先估商, 再笔算!", font=FONT, font_size=24, color=COLOR_GRAY_TXT).move_to(UP * 1.6)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)
        self.wait(1.2)

        self.play(FadeOut(hook1), FadeOut(hook2), FadeOut(main), FadeOut(sub), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 2: 试商方法 — 四舍五入法
    # ------------------------------------------------------------------

    def scene_2_trial_quotient(self):
        title = self.make_title("第一步：试商", color=COLOR_STEP)
        self.play(Write(title), run_time=0.5)

        # 原题回顾
        orig = MathTex(r"952 \div 34", font_size=50, color=WHITE).move_to(UP * 4.6)
        orig[0][0:3].set_color(COLOR_DIVIDEND)
        orig[0][4:6].set_color(COLOR_DIVISOR)
        self.play(Write(orig), run_time=0.6)

        # 说明文字
        desc = Text("把除数 34 看作整十数来试商", font=FONT, font_size=22, color=COLOR_GRAY_TXT).move_to(UP * 3.7)
        self.play(FadeIn(desc), run_time=0.4)

        # 34 → 30
        row1 = VGroup(
            MathTex(r"34", font_size=48, color=COLOR_DIVISOR),
            MathTex(r"\rightarrow", font_size=44, color=COLOR_ARROW),
            MathTex(r"30", font_size=48, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.4).move_to(UP * 2.8)
        note1 = Text("（个位 4 < 5，四舍，看作 30）", font=FONT, font_size=19, color=COLOR_GRAY_TXT).move_to(UP * 2.1)
        self.play(FadeIn(row1), run_time=0.5)
        self.play(FadeIn(note1), run_time=0.4)

        # 商的位数判断
        sep1 = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1).move_to(UP * 1.55)
        self.play(Create(sep1), run_time=0.3)

        desc2 = Text("判断商的最高位在哪里？", font=FONT, font_size=22, color=COLOR_GRAY_TXT).move_to(UP * 1.0)
        self.play(FadeIn(desc2), run_time=0.4)

        # 9 ÷ 3 = 3 → 商是两位数，最高位在十位
        trial1 = MathTex(r"9 \div 3 = 3", font_size=42, color=WHITE).move_to(UP * 0.2)
        trial1[0][0].set_color(COLOR_DIVIDEND)
        trial1[0][2].set_color(COLOR_DIVISOR)
        trial1[0][4].set_color(COLOR_QUOTIENT)
        self.play(Write(trial1), run_time=0.6)

        hint1 = Text("95 ÷ 30，商约 3 → 试商 2 or 3", font=FONT, font_size=20, color=COLOR_GRAY_TXT).move_to(DOWN * 0.6)
        self.play(FadeIn(hint1), run_time=0.4)
        self.wait(0.4)

        # 试商框
        box_bg = self.make_rounded_rect(6.5, 1.4, DOWN * 1.7, color=COLOR_QUOTIENT, fill_opacity=0.12)
        trial_hint = Text("试商时：用被除数前几位 ÷ 整十除数", font=FONT, font_size=20, color=COLOR_QUOTIENT).move_to(DOWN * 1.7)
        self.play(FadeIn(box_bg), FadeIn(trial_hint), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(orig), FadeOut(desc),
            FadeOut(row1), FadeOut(note1),
            FadeOut(sep1), FadeOut(desc2),
            FadeOut(trial1), FadeOut(hint1),
            FadeOut(box_bg), FadeOut(trial_hint),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 竖式演示 952 ÷ 34 = 28（含调商）
    # ------------------------------------------------------------------

    def scene_3_long_division(self):
        title = self.make_title("竖式笔算：952 ÷ 34", color=COLOR_STEP)
        self.play(Write(title), run_time=0.5)

        # ---- 第一步：确定商的最高位 ----
        step_label = Text("Step 1  确定商的十位", font=FONT, font_size=22, color=COLOR_HL).move_to(UP * 4.8)
        self.play(FadeIn(step_label), run_time=0.4)

        # 被除数、除数显示
        dividend_tex = MathTex(r"952", font_size=52, color=COLOR_DIVIDEND).move_to(UP * 3.8)
        divisor_tex  = MathTex(r"34",  font_size=52, color=COLOR_DIVISOR).move_to(UP * 3.8 + LEFT * 2.2)
        div_sign     = MathTex(r"\div", font_size=46, color=WHITE).move_to(UP * 3.8 + LEFT * 1.2)
        self.play(Write(divisor_tex), Write(div_sign), Write(dividend_tex), run_time=0.7)

        # 95 ÷ 34 ≈ 95 ÷ 30，试商 3
        trial_row = VGroup(
            MathTex(r"95 \div 30", font_size=40, color=WHITE),
            MathTex(r"\approx", font_size=36, color=COLOR_ARROW),
            MathTex(r"3", font_size=40, color=COLOR_QUOTIENT),
            Text("（试商 3）", font=FONT, font_size=20, color=COLOR_GRAY_TXT),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 2.8)
        trial_row[0][0][0:2].set_color(COLOR_DIVIDEND)
        trial_row[0][0][3:5].set_color(COLOR_DIVISOR)
        self.play(FadeIn(trial_row), run_time=0.6)
        self.wait(0.4)

        # 验证：3 × 34 = 102 > 95，调商为 2
        verify1 = VGroup(
            MathTex(r"3 \times 34 = 102", font_size=38, color=WHITE),
        ).move_to(UP * 2.0)
        verify1[0][0].set_color(COLOR_QUOTIENT)
        verify1[0][2:4].set_color(COLOR_DIVISOR)
        verify1[0][5:8].set_color(COLOR_REMAIN)
        self.play(Write(verify1), run_time=0.6)

        too_big = Text("102 > 95，乘积太大！→ 调小商为 2", font=FONT, font_size=20, color=COLOR_REMAIN).move_to(UP * 1.3)
        self.play(FadeIn(too_big), run_time=0.4)

        verify2 = VGroup(
            MathTex(r"2 \times 34 = 68", font_size=38, color=WHITE),
        ).move_to(UP * 0.5)
        verify2[0][0].set_color(COLOR_QUOTIENT)
        verify2[0][2:4].set_color(COLOR_DIVISOR)
        verify2[0][5:7].set_color(COLOR_QUOTIENT)
        self.play(Write(verify2), run_time=0.5)

        ok1 = Text("95 - 68 = 27  < 34  ✓  商十位为 2", font=FONT, font_size=20, color=COLOR_QUOTIENT).move_to(DOWN * 0.2)
        self.play(FadeIn(ok1), run_time=0.4)
        self.wait(0.8)

        # 清屏，进入竖式
        self.play(
            FadeOut(step_label), FadeOut(dividend_tex), FadeOut(divisor_tex),
            FadeOut(div_sign), FadeOut(trial_row),
            FadeOut(verify1), FadeOut(too_big), FadeOut(verify2), FadeOut(ok1),
            run_time=0.5,
        )

        # ---- 竖式：逐步显示 ----
        step2_label = Text("Step 2  写竖式，逐步计算", font=FONT, font_size=22, color=COLOR_HL).move_to(UP * 4.8)
        self.play(FadeIn(step2_label), run_time=0.4)

        center = np.array([0.5, 2.2, 0])
        fs = 40

        # 除数
        divisor_v = MathTex(r"34", font_size=fs, color=COLOR_DIVISOR).move_to(center + LEFT * 1.9)
        # 被除数
        dividend_v = MathTex(r"952", font_size=fs, color=COLOR_DIVIDEND).move_to(center)
        # 括号 ）
        paren_v = MathTex(r"\big)", font_size=fs + 4, color=WHITE).move_to(center + LEFT * 0.85)

        self.play(Write(divisor_v), Write(paren_v), Write(dividend_v), run_time=0.7)
        self.wait(0.3)

        # 商：十位 2
        quotient_2 = MathTex(r"2", font_size=fs, color=COLOR_QUOTIENT)
        quotient_2.move_to(center + RIGHT * 0.30 + UP * 0.55)
        self.play(FadeIn(quotient_2, shift=DOWN * 0.2), run_time=0.5)

        # 第一条横线
        line_y1 = center[1] - 0.48
        h_line1 = Line(
            [center[0] - 0.6, line_y1, 0],
            [center[0] + 1.05, line_y1, 0],
            color=WHITE, stroke_width=2,
        )
        self.play(Create(h_line1), run_time=0.4)

        # 2 × 34 = 68，减法
        sub1_tex = MathTex(r"68", font_size=36, color=COLOR_ARROW).move_to(
            [center[0] + 0.45, line_y1 - 0.42, 0])
        note_sub1 = Text("← 2×34", font=FONT, font_size=18, color=COLOR_GRAY_TXT).move_to(
            [center[0] - 0.82, line_y1 - 0.42, 0])
        self.play(Write(sub1_tex), FadeIn(note_sub1), run_time=0.5)

        # 减法横线
        line_y2 = line_y1 - 0.88
        h_line2 = Line(
            [center[0] - 0.6, line_y2, 0],
            [center[0] + 1.05, line_y2, 0],
            color=WHITE, stroke_width=1.5,
        )
        self.play(Create(h_line2), run_time=0.3)

        # 余数 27 带下一位 2 → 272
        rem1_tex = MathTex(r"272", font_size=36, color=COLOR_DIVIDEND).move_to(
            [center[0] + 0.4, line_y2 - 0.42, 0])
        note_rem1 = Text("← 95-68=27，带下 2", font=FONT, font_size=18, color=COLOR_GRAY_TXT).move_to(
            [center[0] - 1.05, line_y2 - 0.42, 0])
        self.play(Write(rem1_tex), FadeIn(note_rem1), run_time=0.5)
        self.wait(0.4)

        # 商个位：272 ÷ 34，试商 8
        quotient_8 = MathTex(r"8", font_size=fs, color=COLOR_QUOTIENT)
        quotient_8.move_to(center + RIGHT * 0.80 + UP * 0.55)
        self.play(FadeIn(quotient_8, shift=DOWN * 0.2), run_time=0.5)

        # 验证：8 × 34 = 272
        note_8 = Text("8×34=272  ✓", font=FONT, font_size=18, color=COLOR_QUOTIENT).move_to(
            [center[0] - 1.1, line_y2 - 0.42 - 0.55, 0])

        # 减法
        line_y3 = line_y2 - 0.88
        sub2_tex = MathTex(r"272", font_size=36, color=COLOR_ARROW).move_to(
            [center[0] + 0.4, line_y3 - 0.38, 0])
        h_line3 = Line(
            [center[0] - 0.6, line_y3, 0],
            [center[0] + 1.05, line_y3, 0],
            color=WHITE, stroke_width=1.5,
        )
        self.play(FadeIn(note_8), Create(h_line3), Write(sub2_tex), run_time=0.5)

        # 余数 0
        line_y4 = line_y3 - 0.75
        rem2_tex = MathTex(r"0", font_size=36, color=COLOR_REMAIN).move_to(
            [center[0] + 0.95, line_y4, 0])
        self.play(Write(rem2_tex), run_time=0.4)

        # 最终商框
        final_box = self.make_rounded_rect(4.5, 0.9, UP * 5.3 + RIGHT * 0.8, color=COLOR_QUOTIENT, fill_opacity=0.15)
        final_ans = VGroup(
            MathTex(r"952 \div 34 =", font_size=34, color=WHITE),
            MathTex(r"28", font_size=38, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 5.3 + RIGHT * 0.8)
        final_ans[0][0][0:3].set_color(COLOR_DIVIDEND)
        final_ans[0][0][4:6].set_color(COLOR_DIVISOR)
        self.play(FadeIn(final_box), Write(final_ans), run_time=0.8)
        self.wait(2.5)

        self.play(
            FadeOut(step2_label),
            FadeOut(divisor_v), FadeOut(paren_v), FadeOut(dividend_v),
            FadeOut(quotient_2), FadeOut(quotient_8),
            FadeOut(h_line1), FadeOut(h_line2), FadeOut(h_line3),
            FadeOut(sub1_tex), FadeOut(note_sub1),
            FadeOut(rem1_tex), FadeOut(note_rem1),
            FadeOut(sub2_tex), FadeOut(rem2_tex),
            FadeOut(note_8),
            FadeOut(final_box), FadeOut(final_ans),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 4: 调商规则
    # ------------------------------------------------------------------

    def scene_4_adjust_rules(self):
        title = self.make_title("调商规则", color=COLOR_STEP)
        self.play(Write(title), run_time=0.5)

        card_bg = self.make_rounded_rect(7.8, 9.5, DOWN * 0.8, color=WHITE, fill_opacity=0.06)
        self.play(FadeIn(card_bg), run_time=0.4)

        # 规则 1：乘积太大 → 调小
        r1_title = Text("规则 1：试商偏大 → 调小", font=FONT, font_size=25, color=COLOR_REMAIN).move_to(UP * 3.2)
        r1_cond  = Text("试商×除数 > 被除数前几位", font=FONT, font_size=20, color=COLOR_GRAY_TXT).move_to(UP * 2.55)
        r1_act   = Text("→ 把商减小 1", font=FONT, font_size=22, color=COLOR_REMAIN).move_to(UP * 2.0)
        # Avoid Chinese in MathTex — use VGroup with separate Text
        r1_ex = VGroup(
            MathTex(r"3 \times 34 = 102 > 95", font_size=30, color=WHITE),
            Text("→ 调商为 2", font=FONT, font_size=22, color=COLOR_REMAIN),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1.3)
        r1_ex[0][0][0].set_color(COLOR_QUOTIENT)
        r1_ex[0][0][2:4].set_color(COLOR_DIVISOR)

        self.play(FadeIn(r1_title), run_time=0.4)
        self.play(FadeIn(r1_cond), run_time=0.3)
        self.play(FadeIn(r1_act),  run_time=0.3)
        self.play(FadeIn(r1_ex),   run_time=0.5)
        self.wait(0.5)

        # 分割线
        sep = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1).move_to(UP * 0.6)
        self.play(Create(sep), run_time=0.3)

        # 规则 2：余数太大 → 调大
        r2_title = Text("规则 2：试商偏小 → 调大", font=FONT, font_size=25, color=COLOR_QUOTIENT).move_to(ORIGIN)
        r2_cond  = Text("余数 ≥ 除数", font=FONT, font_size=22, color=COLOR_GRAY_TXT).move_to(DOWN * 0.65)
        r2_act   = Text("→ 把商加大 1", font=FONT, font_size=22, color=COLOR_QUOTIENT).move_to(DOWN * 1.25)
        r2_ex = VGroup(
            MathTex(r"45 - 34 = 11 \geq 34", font_size=28, color=WHITE),
            Text("→ 调大商", font=FONT, font_size=21, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 1.95)
        r2_ex[0][0][0:2].set_color(COLOR_DIVIDEND)
        r2_ex[0][0][3:5].set_color(COLOR_DIVISOR)

        self.play(FadeIn(r2_title), run_time=0.4)
        self.play(FadeIn(r2_cond), run_time=0.3)
        self.play(FadeIn(r2_act),  run_time=0.3)
        self.play(FadeIn(r2_ex),   run_time=0.5)
        self.wait(0.5)

        # 核心口诀框
        rule_box = self.make_rounded_rect(7.0, 1.5, DOWN * 3.5, color=COLOR_HL, fill_opacity=0.15)
        rule_text1 = Text("余数 ≥ 除数 → 商偏小，调大", font=FONT, font_size=21, color=COLOR_HL).move_to(DOWN * 3.2)
        rule_text2 = Text("乘积 > 部分被除数 → 商偏大，调小", font=FONT, font_size=21, color=COLOR_HL).move_to(DOWN * 3.8)
        self.play(FadeIn(rule_box), FadeIn(rule_text1), FadeIn(rule_text2), run_time=0.6)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(r1_title), FadeOut(r1_cond), FadeOut(r1_act), FadeOut(r1_ex),
            FadeOut(sep),
            FadeOut(r2_title), FadeOut(r2_cond), FadeOut(r2_act), FadeOut(r2_ex),
            FadeOut(rule_box), FadeOut(rule_text1), FadeOut(rule_text2),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 5: 再练一练 — 672 ÷ 21 = 32
    # ------------------------------------------------------------------

    def scene_5_more_examples(self):
        title = self.make_title("再练一练！", color=COLOR_HL)
        self.play(Write(title), run_time=0.5)

        ex2_label = Text("例题：672 ÷ 21 = ?", font=FONT, font_size=26, color=COLOR_ARROW).move_to(UP * 4.8)
        self.play(FadeIn(ex2_label), run_time=0.4)

        # 试商过程
        trial_desc = Text("21 ≈ 20，67 ÷ 20，试商 3", font=FONT, font_size=22, color=COLOR_GRAY_TXT).move_to(UP * 4.0)
        self.play(FadeIn(trial_desc), run_time=0.4)

        verify_3 = VGroup(
            MathTex(r"3 \times 21 = 63", font_size=38, color=WHITE),
            Text("✓", font=FONT, font_size=28, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 3.2)
        verify_3[0][0][0].set_color(COLOR_QUOTIENT)
        verify_3[0][0][2:4].set_color(COLOR_DIVISOR)
        verify_3[0][0][5:7].set_color(COLOR_QUOTIENT)
        self.play(Write(verify_3), run_time=0.5)

        rem_1 = VGroup(
            MathTex(r"67 - 63 = 4", font_size=36, color=WHITE),
            Text("< 21  余数合法", font=FONT, font_size=20, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 2.5)
        rem_1[0][0][0:2].set_color(COLOR_DIVIDEND)
        rem_1[0][0][3:5].set_color(COLOR_ARROW)
        self.play(FadeIn(rem_1), run_time=0.5)

        # 带下位
        bring_down = Text("带下个位 2 → 42", font=FONT, font_size=22, color=COLOR_DIVIDEND).move_to(UP * 1.8)
        self.play(FadeIn(bring_down), run_time=0.4)

        trial2 = VGroup(
            MathTex(r"42 \div 20", font_size=36, color=WHITE),
            Text("试商 2", font=FONT, font_size=20, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1.1)
        trial2[0][0][0:2].set_color(COLOR_DIVIDEND)
        trial2[0][0][3:5].set_color(COLOR_DIVISOR)
        self.play(FadeIn(trial2), run_time=0.4)

        verify_2 = VGroup(
            MathTex(r"2 \times 21 = 42", font_size=36, color=WHITE),
            Text("✓", font=FONT, font_size=24, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 0.4)
        verify_2[0][0][0].set_color(COLOR_QUOTIENT)
        verify_2[0][0][2:4].set_color(COLOR_DIVISOR)
        verify_2[0][0][5:7].set_color(COLOR_QUOTIENT)
        self.play(Write(verify_2), run_time=0.5)

        rem_2 = VGroup(
            MathTex(r"42 - 42 = 0", font_size=36, color=COLOR_REMAIN),
        ).move_to(DOWN * 0.3)
        rem_2[0][0][0:2].set_color(COLOR_DIVIDEND)
        rem_2[0][0][3:5].set_color(COLOR_ARROW)
        self.play(FadeIn(rem_2), run_time=0.4)

        # 答案框
        ans_box = self.make_rounded_rect(5.5, 1.0, DOWN * 1.4, color=COLOR_QUOTIENT, fill_opacity=0.15)
        ans_tex = VGroup(
            MathTex(r"672 \div 21 =", font_size=36, color=WHITE),
            MathTex(r"32", font_size=40, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.4)
        ans_tex[0][0][0:3].set_color(COLOR_DIVIDEND)
        ans_tex[0][0][4:6].set_color(COLOR_DIVISOR)
        self.play(FadeIn(ans_box), Write(ans_tex), run_time=0.7)

        # 无需调商说明
        no_adj = Text("整除！无需调商，一次到位", font=FONT, font_size=20, color=COLOR_GRAY_TXT).move_to(DOWN * 2.4)
        self.play(FadeIn(no_adj, shift=UP * 0.2), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(ex2_label), FadeOut(trial_desc),
            FadeOut(verify_3), FadeOut(rem_1), FadeOut(bring_down),
            FadeOut(trial2), FadeOut(verify_2), FadeOut(rem_2),
            FadeOut(ans_box), FadeOut(ans_tex), FadeOut(no_adj),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 6: 同头无除商 8、9
    # ------------------------------------------------------------------

    def scene_6_same_head_trick(self):
        title = self.make_title("技巧：同头无除商 8、9", color=COLOR_STEP)
        self.play(Write(title), run_time=0.5)

        # 解释"同头"
        explain = Text(
            "被除数前几位 与 除数 最高位相同",
            font=FONT, font_size=22, color=COLOR_GRAY_TXT,
        ).move_to(UP * 4.9)
        self.play(FadeIn(explain), run_time=0.4)

        line0 = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1).move_to(UP * 4.3)
        self.play(Create(line0), run_time=0.3)

        # 例：88 ÷ 22 —— 同头，直接试商 4?
        ex_title = Text("例：88 ÷ 22", font=FONT, font_size=26, color=COLOR_ARROW).move_to(UP * 3.7)
        self.play(FadeIn(ex_title), run_time=0.4)

        ex_step1 = Text("88 和 22 都以 2 开头（同头）", font=FONT, font_size=20, color=COLOR_GRAY_TXT).move_to(UP * 3.0)
        self.play(FadeIn(ex_step1), run_time=0.4)

        ex_rule = VGroup(
            Text("同头无除 →", font=FONT, font_size=22, color=COLOR_HL),
            Text("商 4（直接试商接近整数倍）", font=FONT, font_size=20, color=COLOR_GRAY_TXT),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 2.3)
        self.play(FadeIn(ex_rule), run_time=0.5)

        # 验证
        verify_88 = VGroup(
            MathTex(r"4 \times 22 = 88", font_size=40, color=WHITE),
            Text("✓", font=FONT, font_size=28, color=COLOR_QUOTIENT),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1.5)
        verify_88[0][0][0].set_color(COLOR_QUOTIENT)
        verify_88[0][0][2:4].set_color(COLOR_DIVISOR)
        verify_88[0][0][5:7].set_color(COLOR_DIVIDEND)
        self.play(Write(verify_88), run_time=0.6)

        ans_88 = VGroup(
            MathTex(r"88 \div 22 = 4", font_size=40, color=WHITE),
        ).move_to(UP * 0.7)
        ans_88[0][0][0:2].set_color(COLOR_DIVIDEND)
        ans_88[0][0][3:5].set_color(COLOR_DIVISOR)
        ans_88[0][0][6].set_color(COLOR_QUOTIENT)
        self.play(Write(ans_88), run_time=0.5)
        self.wait(0.4)

        sep2 = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1).move_to(ORIGIN)
        self.play(Create(sep2), run_time=0.3)

        # 例2：78 ÷ 26 —— 同头，商 3
        ex2_title = Text("例：78 ÷ 26", font=FONT, font_size=26, color=COLOR_ARROW).move_to(DOWN * 0.6)
        self.play(FadeIn(ex2_title), run_time=0.4)

        ex2_rule = Text("7 和 2 不同头…但 78 ÷ 26 ≈ 78 ÷ 30，试 2", font=FONT, font_size=19, color=COLOR_GRAY_TXT).move_to(DOWN * 1.35)
        self.play(FadeIn(ex2_rule), run_time=0.4)

        # 实际演示：同头技巧示例
        trick_box = self.make_rounded_rect(7.6, 3.2, DOWN * 3.3, color=COLOR_HL, fill_opacity=0.10)
        trick_t = Text("同头无除商 8、9  口诀", font=FONT, font_size=23, color=COLOR_HL).move_to(DOWN * 2.3)
        trick_b1 = Text("被除数前几位 ÷ 除数，商≥8 时", font=FONT, font_size=19, color=COLOR_GRAY_TXT).move_to(DOWN * 2.95)
        trick_b2 = Text("先试商 8，若余数≥除数再改为 9", font=FONT, font_size=19, color=COLOR_GRAY_TXT).move_to(DOWN * 3.55)
        trick_b3 = Text("（两者最高位相近时常出现）", font=FONT, font_size=18, color=COLOR_GRAY_TXT).move_to(DOWN * 4.15)
        self.play(FadeIn(trick_box), FadeIn(trick_t), FadeIn(trick_b1), FadeIn(trick_b2), FadeIn(trick_b3), run_time=0.7)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(explain), FadeOut(line0),
            FadeOut(ex_title), FadeOut(ex_step1), FadeOut(ex_rule),
            FadeOut(verify_88), FadeOut(ans_88),
            FadeOut(sep2), FadeOut(ex2_title), FadeOut(ex2_rule),
            FadeOut(trick_box), FadeOut(trick_t),
            FadeOut(trick_b1), FadeOut(trick_b2), FadeOut(trick_b3),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 规律总结
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        title = self.make_title("总结：试商与调商", color=COLOR_HL)
        self.play(Write(title), run_time=0.5)

        card_bg = self.make_rounded_rect(7.8, 10.5, DOWN * 0.5, color=WHITE, fill_opacity=0.05)
        self.play(FadeIn(card_bg), run_time=0.4)

        items = [
            ("1. 试商", "把除数四舍五入为整十数，\n用被除数前几位 ÷ 整十数", COLOR_STEP),
            ("2. 调大商", "余数 ≥ 除数 → 商加 1", COLOR_QUOTIENT),
            ("3. 调小商", "乘积 > 被除数前几位 → 商减 1", COLOR_REMAIN),
            ("4. 同头技巧", "最高位相同 → 先试商 8 或 9", COLOR_HL),
            ("5. 验余数", "每次余数必须 < 除数", COLOR_ARROW),
        ]

        y_start = UP * 3.5
        step_y   = 1.7

        for i, (label, body, color) in enumerate(items):
            y = y_start - i * step_y * 0.95
            label_t = Text(label, font=FONT, font_size=24, color=color).move_to(y + LEFT * 1.5)
            body_t  = Text(body,  font=FONT, font_size=19, color=COLOR_GRAY_TXT).move_to(y + RIGHT * 0.9)
            self.play(FadeIn(label_t, shift=RIGHT * 0.2), FadeIn(body_t, shift=RIGHT * 0.2), run_time=0.4)
            if i < len(items) - 1:
                self.wait(0.15)

        # 核心例题回顾
        core = VGroup(
            MathTex(r"952 \div 34 = 28", font_size=36, color=WHITE),
        ).move_to(DOWN * 5.2)
        core[0][0][0:3].set_color(COLOR_DIVIDEND)
        core[0][0][4:6].set_color(COLOR_DIVISOR)
        core[0][0][7:9].set_color(COLOR_QUOTIENT)
        self.play(Write(core), run_time=0.7)

        hl = Text("掌握试商调商，笔算不犯愁！", font=FONT, font_size=22, color=COLOR_HL).move_to(DOWN * 6.2)
        self.play(FadeIn(hl, shift=UP * 0.2), run_time=0.5)
        self.wait(3.0)

        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(core), FadeOut(hl),
            run_time=0.5,
        )
        # fade out all remaining text mobjects (items)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not self.author], run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B,
        ).move_to(UP * 0.6)

        self.play(ReplacementTransform(self.author, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我，学更多数学技巧！",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 0.6)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 装饰：三道例题小卡片
        card_data = [
            (r"952 \div 34 = 28", COLOR_DIVIDEND),
            (r"672 \div 21 = 32", COLOR_DIVISOR),
            (r"88 \div 22 = 4",   COLOR_QUOTIENT),
        ]
        cards = VGroup()
        for tex, clr in card_data:
            m = MathTex(tex, font_size=26, color=clr)
            cards.add(m)
        cards.arrange(DOWN, buff=0.45).move_to(DOWN * 3.0)
        for card in cards:
            card[0][0:3].set_color(COLOR_DIVIDEND)

        self.play(*[FadeIn(c, shift=RIGHT * 0.3) for c in cards], run_time=0.8)
        self.wait(2.5)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(cards),
            run_time=1.0,
        )


# 运行命令:
# manim -qm 002_笔算除法.py WrittenDivisionLesson
# manim -qh 002_笔算除法.py WrittenDivisionLesson
