"""
002_两位数除两三位数.py — 两位数除两、三位数（试商）教学动画

知识点: 试商法、调商策略、竖式除法
  - 核心: 四舍五入试商法
  - 步骤: 从被除数最高位开始, 先看前两位; 不够除则看前三位
  - 商写在被除数相应位上; 余数必须小于除数
  - 调商: 初商 → 试乘 → 积太大调小 / 积太小调大
  - 例题: 96 ÷ 32 = 3 (直接整除); 78 ÷ 26 = 3 (调商示例)
年级: 三年级下册
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
BG_COLOR     = "#1a1a2e"
COLOR_TITLE  = "#fbbf24"   # 金色 标题
COLOR_HL     = "#f59e0b"   # 橙色 高亮
COLOR_STEP   = "#3b82f6"   # 蓝色 步骤标题
COLOR_OK     = "#22c55e"   # 绿色 正确/结论
COLOR_ERR    = "#ef4444"   # 红色 错误/调商
COLOR_GUESS  = "#a78bfa"   # 紫色 试商数字
COLOR_AUX    = "#94a3b8"   # 灰蓝 辅助文字
COLOR_AUTHOR = "#6b7280"   # 灰色 作者
FONT         = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class TwoDigitDivisionLesson(Scene):
    """
    两位数除两、三位数（试商）教学动画
    场景顺序:
      1. 开场钩子
      2. 试商思路 — 四舍五入
      3. 例题1: 96 ÷ 32 = 3 (竖式 + 验证)
      4. 调商演示 — 积太大调小商
      5. 例题2: 78 ÷ 26 (试商→调商完整流程)
      6. 知识总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 持久存在的作者标识
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        self.scene_1_opening()
        self.scene_2_shishang_idea()
        self.scene_3_example1()
        self.scene_4_adjust_demo()
        self.scene_5_example2()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_title(self, text, color=COLOR_STEP, font_size=34):
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(UP * 5.8)

    def make_subtitle(self, text, color=COLOR_AUX, font_size=22):
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(UP * 5.0)

    def make_explanation(self, text, y=-4.5, color=COLOR_AUX, font_size=22):
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(UP * y)

    def build_division_box(
        self,
        dividend,        # str, e.g. "96"
        divisor,         # str, e.g. "32"
        quotient,        # str (may be partial/blank), e.g. "3"
        remainder,       # str, e.g. "0"   (empty string = don't show)
        product,         # str, e.g. "96"  (empty = don't show)
        center=ORIGIN,
        scale=1.0,
    ):
        """
        构建标准竖式除法图形，返回 VGroup 及各关键元素的引用字典。

        布局 (竖式):
                  quotient
             ___________
        divisor ) dividend
                  product
                ---------
                  remainder
        """
        fs_large  = int(48 * scale)
        fs_medium = int(38 * scale)
        sw        = 3.0 * scale         # stroke_width

        # 除数
        t_divisor  = Text(divisor,  font=FONT, font_size=fs_large, color=WHITE)
        # 被除数
        t_dividend = Text(dividend, font=FONT, font_size=fs_large, color=WHITE)
        # 商 (顶部)
        t_quotient = Text(quotient if quotient else " ", font=FONT, font_size=fs_large, color=COLOR_OK)

        # 竖式符号: 竖线 + 横线
        # 先排列被除数和除数让位置确定
        inner = VGroup(t_divisor, t_dividend).arrange(RIGHT, buff=0.45)
        inner.move_to(center)

        # 竖式横线 (盖住被除数部分)
        line_top_start_x = t_dividend.get_left()[0] - 0.1
        line_top_end_x   = t_dividend.get_right()[0] + 0.15
        line_top_y       = t_dividend.get_top()[1] + 0.18

        top_line = Line(
            [line_top_start_x, line_top_y, 0],
            [line_top_end_x,   line_top_y, 0],
            stroke_width=sw, color=WHITE,
        )

        # 竖式竖线
        vert_line_x = t_dividend.get_left()[0] - 0.08
        vert_line = Line(
            [vert_line_x, line_top_y,                    0],
            [vert_line_x, t_dividend.get_bottom()[1] - 0.1, 0],
            stroke_width=sw, color=WHITE,
        )

        # 商放到横线上方
        t_quotient.move_to([
            t_dividend.get_center()[0],
            line_top_y + t_quotient.height / 2 + 0.12,
            0
        ])

        group_dict = {
            "divisor":  t_divisor,
            "dividend": t_dividend,
            "quotient": t_quotient,
            "top_line": top_line,
            "vert_line": vert_line,
        }

        elements = [t_divisor, t_dividend, t_quotient, top_line, vert_line]

        # 乘积 (减法行)
        if product:
            t_product = Text(product, font=FONT, font_size=fs_medium, color=COLOR_GUESS)
            product_y = t_dividend.get_bottom()[1] - 0.55
            t_product.move_to([t_dividend.get_center()[0], product_y, 0])

            # 减法横线
            sub_line_y = product_y - t_product.height / 2 - 0.18
            sub_line = Line(
                [line_top_start_x, sub_line_y, 0],
                [line_top_end_x,   sub_line_y, 0],
                stroke_width=sw * 0.8, color=WHITE,
            )

            group_dict["product"]  = t_product
            group_dict["sub_line"] = sub_line
            elements += [t_product, sub_line]

        # 余数
        if remainder:
            rem_ref_y = (
                group_dict["sub_line"].get_bottom()[1] - 0.55
                if "sub_line" in group_dict
                else t_dividend.get_bottom()[1] - 1.1
            )
            t_remainder = Text(remainder, font=FONT, font_size=fs_medium, color=COLOR_HL)
            t_remainder.move_to([t_dividend.get_center()[0], rem_ref_y, 0])
            group_dict["remainder"] = t_remainder
            elements.append(t_remainder)

        return VGroup(*elements), group_dict

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        # 大钩子问题
        hook = Text(
            "96 ÷ 32 = ?",
            font=FONT, font_size=52, color=COLOR_TITLE,
        ).move_to(UP * 4.5)

        hook_sub = Text(
            "两位数除法怎么算?",
            font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 3.5)

        self.play(Write(hook), run_time=0.9)
        self.play(FadeIn(hook_sub, shift=UP * 0.2), run_time=0.5)

        # 困惑表情 — 三个问号
        q_marks = VGroup(
            MathTex(r"?", font_size=80, color=COLOR_GUESS).move_to(LEFT * 2.0 + UP * 1.2),
            MathTex(r"?", font_size=60, color=COLOR_GUESS).move_to(ORIGIN + UP * 1.0),
            MathTex(r"?", font_size=80, color=COLOR_GUESS).move_to(RIGHT * 2.0 + UP * 1.2),
        )
        self.play(*[GrowFromCenter(q) for q in q_marks], run_time=0.7)
        self.wait(0.8)

        # 引出方法
        method_text = Text(
            "学会试商法, 轻松搞定!",
            font=FONT, font_size=28, color=COLOR_OK,
        ).move_to(DOWN * 1.0)

        self.play(
            FadeOut(q_marks),
            FadeIn(method_text, shift=UP * 0.3),
            run_time=0.6,
        )
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(hook_sub), FadeOut(method_text),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 试商思路 — 四舍五入
    # ------------------------------------------------------------------

    def scene_2_shishang_idea(self):
        title = self.make_title("试商的方法", color=COLOR_TITLE, font_size=38)
        self.play(Write(title), run_time=0.6)

        # 核心思路说明
        idea_box_bg = RoundedRectangle(
            width=7.8, height=2.6,
            corner_radius=0.3,
            color=COLOR_STEP,
            stroke_width=2,
            fill_color=COLOR_STEP,
            fill_opacity=0.1,
        ).move_to(UP * 3.5)

        idea_line1 = Text(
            "把除数四舍五入成整十数",
            font=FONT, font_size=24, color=WHITE,
        ).move_to(UP * 4.0)

        idea_line2 = VGroup(
            Text("再用这个整十数去试商", font=FONT, font_size=24, color=WHITE),
        ).move_to(UP * 3.3)

        idea_line3 = Text(
            "最后验证并调商", font=FONT, font_size=22, color=COLOR_AUX,
        ).move_to(UP * 2.7)

        self.play(FadeIn(idea_box_bg), run_time=0.4)
        self.play(FadeIn(idea_line1, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(idea_line2, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(idea_line3, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(0.5)

        # 具体示例: 32 → 30
        arrow_label = VGroup(
            Text("例: 除数", font=FONT, font_size=26, color=COLOR_AUX),
            MathTex(r"32", font_size=36, color=WHITE),
            Text("四舍五入得", font=FONT, font_size=26, color=COLOR_AUX),
            MathTex(r"30", font_size=36, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.4)

        arrow_down = Arrow(
            UP * 1.05, UP * 0.45,
            color=COLOR_HL, stroke_width=4,
            max_tip_length_to_length_ratio=0.25,
        )

        rounding_text = VGroup(
            Text("个位是", font=FONT, font_size=24, color=COLOR_AUX),
            MathTex(r"2", font_size=32, color=COLOR_GUESS),
            Text("< 5, 舍去", font=FONT, font_size=24, color=COLOR_AUX),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 0.0)

        trial_text = VGroup(
            Text("用", font=FONT, font_size=26, color=COLOR_AUX),
            MathTex(r"96 \div 30 \approx 3", font_size=34, color=COLOR_HL),
            Text("来试商", font=FONT, font_size=26, color=COLOR_AUX),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.0)

        self.play(FadeIn(arrow_label, shift=UP * 0.2), run_time=0.6)
        self.play(GrowArrow(arrow_down), run_time=0.4)
        self.play(FadeIn(rounding_text), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(trial_text, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 三步骤框
        steps_bg = RoundedRectangle(
            width=7.8, height=3.4,
            corner_radius=0.3,
            color=COLOR_AUX,
            stroke_width=1.5,
            fill_color=WHITE,
            fill_opacity=0.04,
        ).move_to(DOWN * 3.2)

        step_a = VGroup(
            Text("(1)", font=FONT, font_size=24, color=COLOR_HL),
            Text("四舍五入除数为整十数", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.2)

        step_b = VGroup(
            Text("(2)", font=FONT, font_size=24, color=COLOR_HL),
            Text("用整十数试商得初商", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.2)

        step_c = VGroup(
            Text("(3)", font=FONT, font_size=24, color=COLOR_HL),
            Text("验证 (余数 < 除数), 必要时调商", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.2)

        steps = VGroup(step_a, step_b, step_c).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        steps.move_to(DOWN * 3.2)

        self.play(FadeIn(steps_bg), run_time=0.3)
        for s in steps:
            self.play(FadeIn(s, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(idea_box_bg),
            FadeOut(idea_line1), FadeOut(idea_line2), FadeOut(idea_line3),
            FadeOut(arrow_label), FadeOut(arrow_down),
            FadeOut(rounding_text), FadeOut(trial_text),
            FadeOut(steps_bg), FadeOut(steps),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 例题1 — 96 ÷ 32 = 3 竖式演示
    # ------------------------------------------------------------------

    def scene_3_example1(self):
        title = self.make_title("例题: 96 ÷ 32", color=COLOR_TITLE, font_size=36)
        self.play(Write(title), run_time=0.6)

        # ---- Step 0: 展示题目 ----
        prob_display = VGroup(
            MathTex(r"96 \div 32 = ?", font_size=52, color=WHITE),
        ).move_to(UP * 4.5)
        self.play(FadeIn(prob_display, shift=DOWN * 0.2), run_time=0.6)

        # ---- Step 1: 试商 ----
        step1_label = Text("第一步: 四舍五入试商", font=FONT, font_size=26, color=COLOR_STEP)
        step1_label.move_to(UP * 3.4)
        self.play(FadeIn(step1_label, shift=RIGHT * 0.3), run_time=0.5)

        trial_row = VGroup(
            MathTex(r"32 \approx 30", font_size=36, color=COLOR_HL),
        ).move_to(UP * 2.5)

        self.play(Write(trial_row), run_time=0.6)

        trial_calc = VGroup(
            MathTex(r"96 \div 30 \approx 3", font_size=36, color=COLOR_GUESS),
        ).move_to(UP * 1.7)

        trial_note = Text("初商 3", font=FONT, font_size=24, color=COLOR_GUESS)
        trial_note.move_to(UP * 1.0)

        self.play(Write(trial_calc), run_time=0.6)
        self.play(FadeIn(trial_note, shift=UP * 0.2), run_time=0.4)
        self.wait(0.8)

        # ---- Step 2: 验证 ----
        step2_label = Text("第二步: 验证", font=FONT, font_size=26, color=COLOR_STEP)
        step2_label.move_to(UP * 0.2)
        self.play(FadeIn(step2_label, shift=RIGHT * 0.3), run_time=0.4)

        verify_row = VGroup(
            MathTex(r"32 \times 3 = 96", font_size=36, color=WHITE),
        ).move_to(DOWN * 0.6)

        ok_text = Text("恰好整除, 商正确!", font=FONT, font_size=24, color=COLOR_OK)
        ok_text.move_to(DOWN * 1.4)

        self.play(Write(verify_row), run_time=0.6)
        self.play(FadeIn(ok_text, scale=1.1), run_time=0.5)
        self.wait(0.6)

        # ---- 清理顶部, 显示竖式 ----
        self.play(
            FadeOut(prob_display), FadeOut(step1_label),
            FadeOut(trial_row), FadeOut(trial_calc),
            FadeOut(trial_note), FadeOut(step2_label),
            FadeOut(verify_row), FadeOut(ok_text),
            FadeOut(title),
            run_time=0.5,
        )

        # ---- 竖式动画 ----
        vshang_title = self.make_title("竖式计算过程", color=COLOR_STEP, font_size=34)
        self.play(Write(vshang_title), run_time=0.5)

        # 初始: 只有除数和被除数
        base_group, base_dict = self.build_division_box(
            dividend="96", divisor="32",
            quotient="", remainder="", product="",
            center=UP * 2.5, scale=1.1,
        )

        self.play(
            FadeIn(base_dict["divisor"]),
            FadeIn(base_dict["dividend"]),
            Create(base_dict["top_line"]),
            Create(base_dict["vert_line"]),
            run_time=0.8,
        )
        self.wait(0.4)

        # 写商
        quotient_text = Text("3", font=FONT, font_size=int(48 * 1.1), color=COLOR_OK)
        quotient_text.move_to(base_dict["quotient"].get_center())
        self.play(Write(quotient_text), run_time=0.6)

        # 标注箭头说明 "商写在哪一位"
        arrow_explain = Text(
            "商写在个位上面",
            font=FONT, font_size=22, color=COLOR_AUX,
        ).move_to(RIGHT * 2.5 + UP * 3.8)
        arrow_to_q = Arrow(
            arrow_explain.get_left() + LEFT * 0.1,
            quotient_text.get_right() + RIGHT * 0.05,
            color=COLOR_AUX, stroke_width=2,
            max_tip_length_to_length_ratio=0.2, buff=0.1,
        )
        self.play(FadeIn(arrow_explain), GrowArrow(arrow_to_q), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(arrow_explain), FadeOut(arrow_to_q), run_time=0.3)

        # 写乘积
        product_text = Text("96", font=FONT, font_size=int(38 * 1.1), color=COLOR_GUESS)
        div_center_x = base_dict["dividend"].get_center()[0]
        product_y = base_dict["dividend"].get_bottom()[1] - 0.6
        product_text.move_to([div_center_x, product_y, 0])

        prod_note = VGroup(
            MathTex(r"32 \times 3 = 96", font_size=28, color=COLOR_GUESS),
        ).move_to(DOWN * 0.5)

        self.play(Write(prod_note), run_time=0.5)
        self.play(Write(product_text), run_time=0.5)

        # 减法横线
        lx0 = base_dict["dividend"].get_left()[0] - 0.1
        lx1 = base_dict["dividend"].get_right()[0] + 0.15
        sub_y = product_y - product_text.height / 2 - 0.2
        sub_line = Line([lx0, sub_y, 0], [lx1, sub_y, 0], stroke_width=3 * 1.1, color=WHITE)
        self.play(Create(sub_line), run_time=0.4)

        # 余数 0
        remainder_text = Text("0", font=FONT, font_size=int(38 * 1.1), color=COLOR_HL)
        remainder_text.move_to([div_center_x, sub_y - 0.55, 0])
        self.play(Write(remainder_text), run_time=0.4)

        # 余数标注
        rem_note = Text("余数为 0, 整除!", font=FONT, font_size=22, color=COLOR_OK)
        rem_note.move_to(DOWN * 2.8)
        self.play(FadeIn(rem_note, scale=1.1), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(prod_note), run_time=0.3)

        # 最终答案
        final_ans = VGroup(
            MathTex(r"96 \div 32 = ", font_size=40, color=WHITE),
            MathTex(r"3", font_size=48, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 4.0)

        self.play(FadeIn(final_ans, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(vshang_title),
            FadeOut(base_dict["divisor"]), FadeOut(base_dict["dividend"]),
            FadeOut(base_dict["top_line"]), FadeOut(base_dict["vert_line"]),
            FadeOut(quotient_text), FadeOut(product_text),
            FadeOut(sub_line), FadeOut(remainder_text),
            FadeOut(rem_note), FadeOut(final_ans),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 4: 调商演示 — 积太大, 调小商
    # ------------------------------------------------------------------

    def scene_4_adjust_demo(self):
        title = self.make_title("调商: 初商不对怎么办?", color=COLOR_TITLE, font_size=32)
        self.play(Write(title), run_time=0.6)

        intro = Text(
            "有时初商需要调整",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 5.0)
        self.play(FadeIn(intro), run_time=0.4)

        # ---------- 情况 A: 积太大, 调小 ----------
        case_a_title = Text("情况(1): 积太大, 调小商", font=FONT, font_size=26, color=COLOR_ERR)
        case_a_title.move_to(UP * 4.0)
        self.play(FadeIn(case_a_title, shift=RIGHT * 0.3), run_time=0.5)

        # 示例: 假设用 80÷25, 25→30, 80÷30≈2 (初商2), 但 25×2=50 不对
        # 更直观: 用 78÷26, 26→30, 78÷30≈2 (初商2), 26×2=52, 78-52=26≥26 → 偏小
        # 反向演示: 某数 ÷ 34, 34→30, 初商 = 4, 34×4=136 > 被除数 → 调小
        # 用 130 ÷ 34:  34→30, 130÷30≈4; 34×4=136 > 130 → 商偏大, 调为 3

        example_a = VGroup(
            Text("例:", font=FONT, font_size=26, color=COLOR_AUX),
            MathTex(r"130 \div 34", font_size=38, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.0)

        self.play(FadeIn(example_a), run_time=0.5)

        # 试商步骤
        trial_a1 = VGroup(
            MathTex(r"34 \approx 30", font_size=32, color=COLOR_HL),
        ).move_to(UP * 2.2)

        trial_a2 = VGroup(
            MathTex(r"130 \div 30 \approx 4", font_size=32, color=COLOR_GUESS),
            Text("(初商 4)", font=FONT, font_size=22, color=COLOR_GUESS),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 1.5)

        self.play(Write(trial_a1), run_time=0.5)
        self.play(Write(trial_a2), run_time=0.5)
        self.wait(0.4)

        # 验证: 积太大
        verify_a = VGroup(
            MathTex(r"34 \times 4 = 136", font_size=32, color=WHITE),
        ).move_to(UP * 0.7)

        big_warn = VGroup(
            MathTex(r"136 > 130", font_size=30, color=COLOR_ERR),
            Text("积比被除数大!", font=FONT, font_size=22, color=COLOR_ERR),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 0.0)

        self.play(Write(verify_a), run_time=0.5)
        self.play(FadeIn(big_warn, scale=1.05), run_time=0.5)

        # 调商
        cross_4 = Cross(
            MathTex(r"4", font_size=38, color=COLOR_GUESS).move_to(trial_a2[0].get_right() + LEFT * 1.5 + UP * 0.0),
            stroke_color=COLOR_ERR, stroke_width=4,
        )
        self.play(Create(cross_4), run_time=0.4)

        adjust_arrow = Arrow(
            UP * (-0.7), DOWN * 0.5,
            color=COLOR_OK, stroke_width=4,
            max_tip_length_to_length_ratio=0.2,
        ).move_to(DOWN * 0.8 + LEFT * 1.5)

        adjust_text = VGroup(
            Text("调小商, 改为 ", font=FONT, font_size=24, color=COLOR_OK),
            MathTex(r"3", font_size=38, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.6)

        verify_a2 = VGroup(
            MathTex(r"34 \times 3 = 102", font_size=32, color=WHITE),
        ).move_to(DOWN * 2.4)

        rem_a = VGroup(
            MathTex(r"130 - 102 = 28 < 34", font_size=28, color=COLOR_OK),
        ).move_to(DOWN * 3.1)

        ok_a = Text("余数 < 除数, 商正确!", font=FONT, font_size=22, color=COLOR_OK)
        ok_a.move_to(DOWN * 3.8)

        self.play(FadeIn(adjust_text, shift=UP * 0.2), run_time=0.4)
        self.play(Write(verify_a2), run_time=0.5)
        self.play(Write(rem_a), run_time=0.5)
        self.play(FadeIn(ok_a, scale=1.05), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(intro), FadeOut(case_a_title),
            FadeOut(example_a), FadeOut(trial_a1), FadeOut(trial_a2),
            FadeOut(verify_a), FadeOut(big_warn), FadeOut(cross_4),
            FadeOut(adjust_text),
            FadeOut(verify_a2), FadeOut(rem_a), FadeOut(ok_a),
            run_time=0.5,
        )

        # ---------- 情况 B: 积太小, 调大 ----------
        title_b = self.make_title("情况(2): 余数>=除数, 调大商", color=COLOR_TITLE, font_size=30)
        self.play(Write(title_b), run_time=0.5)

        case_b_intro = VGroup(
            Text("如果余数 >= 除数,", font=FONT, font_size=24, color=WHITE),
        ).move_to(UP * 5.0)

        case_b_sub = Text(
            "说明商偏小, 需要调大 +1",
            font=FONT, font_size=24, color=COLOR_OK,
        ).move_to(UP * 4.3)

        self.play(FadeIn(case_b_intro), FadeIn(case_b_sub), run_time=0.5)

        # 示例
        example_b = VGroup(
            Text("例:", font=FONT, font_size=26, color=COLOR_AUX),
            MathTex(r"78 \div 26", font_size=38, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.3)
        self.play(FadeIn(example_b), run_time=0.5)

        trial_b = VGroup(
            MathTex(r"26 \approx 30,\quad 78 \div 30 \approx 2", font_size=30, color=COLOR_GUESS),
            Text("(初商 2)", font=FONT, font_size=20, color=COLOR_GUESS),
        ).arrange(DOWN, buff=0.15).move_to(UP * 2.3)

        self.play(Write(trial_b), run_time=0.6)

        verify_b = VGroup(
            MathTex(r"26 \times 2 = 52", font_size=30, color=WHITE),
        ).move_to(UP * 1.4)

        rem_b_wrong = VGroup(
            MathTex(r"78 - 52 = 26 \geq 26", font_size=28, color=COLOR_ERR),
            Text("余数 >= 除数!", font=FONT, font_size=22, color=COLOR_ERR),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 0.6)

        self.play(Write(verify_b), run_time=0.5)
        self.play(FadeIn(rem_b_wrong, scale=1.05), run_time=0.5)
        self.wait(0.4)

        adjust_b = VGroup(
            Text("调大商, 改为 ", font=FONT, font_size=24, color=COLOR_OK),
            MathTex(r"3", font_size=38, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 0.3)

        verify_b2 = VGroup(
            MathTex(r"26 \times 3 = 78", font_size=30, color=WHITE),
        ).move_to(DOWN * 1.1)

        rem_b_ok = VGroup(
            MathTex(r"78 - 78 = 0", font_size=28, color=COLOR_OK),
            Text("整除!", font=FONT, font_size=22, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.9)

        self.play(FadeIn(adjust_b, shift=UP * 0.2), run_time=0.4)
        self.play(Write(verify_b2), run_time=0.5)
        self.play(FadeIn(rem_b_ok, scale=1.05), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title_b), FadeOut(case_b_intro), FadeOut(case_b_sub),
            FadeOut(example_b), FadeOut(trial_b), FadeOut(verify_b),
            FadeOut(rem_b_wrong), FadeOut(adjust_b),
            FadeOut(verify_b2), FadeOut(rem_b_ok),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 5: 例题2 — 78 ÷ 26 完整竖式（含调商）
    # ------------------------------------------------------------------

    def scene_5_example2(self):
        title = self.make_title("完整竖式: 78 ÷ 26", color=COLOR_TITLE, font_size=36)
        self.play(Write(title), run_time=0.6)

        # 题目
        prob = VGroup(
            MathTex(r"78 \div 26 = ?", font_size=48, color=WHITE),
        ).move_to(UP * 5.0)
        self.play(FadeIn(prob, shift=DOWN * 0.2), run_time=0.5)

        # ---- 试商 ----
        trial_label = Text("(1) 试商", font=FONT, font_size=26, color=COLOR_STEP).move_to(UP * 4.0)
        self.play(FadeIn(trial_label, shift=RIGHT * 0.3), run_time=0.4)

        trial_line = VGroup(
            MathTex(r"26 \approx 30,\quad 78 \div 30 \approx 2", font_size=32, color=COLOR_GUESS),
        ).move_to(UP * 3.2)
        self.play(Write(trial_line), run_time=0.6)
        self.wait(0.4)

        # ---- 竖式: 初商 2 ----
        vgroup_2, vdict_2 = self.build_division_box(
            dividend="78", divisor="26",
            quotient="2", remainder="", product="",
            center=UP * 1.5, scale=1.0,
        )

        self.play(
            FadeIn(vdict_2["divisor"]),
            FadeIn(vdict_2["dividend"]),
            Create(vdict_2["top_line"]),
            Create(vdict_2["vert_line"]),
            run_time=0.6,
        )
        self.play(Write(vdict_2["quotient"]), run_time=0.5)

        # 验证: 26×2=52
        prod_label2 = Text("(2) 验证: 26x2=52", font=FONT, font_size=24, color=COLOR_AUX)
        prod_label2.move_to(UP * 0.3)
        self.play(FadeIn(prod_label2, shift=RIGHT * 0.2), run_time=0.4)

        # 乘积行
        div_cx = vdict_2["dividend"].get_center()[0]
        prod_y2 = vdict_2["dividend"].get_bottom()[1] - 0.55
        prod_text2 = Text("52", font=FONT, font_size=38, color=COLOR_GUESS)
        prod_text2.move_to([div_cx, prod_y2, 0])
        self.play(Write(prod_text2), run_time=0.4)

        sub_y2 = prod_y2 - prod_text2.height / 2 - 0.18
        lx0 = vdict_2["dividend"].get_left()[0] - 0.1
        lx1 = vdict_2["dividend"].get_right()[0] + 0.15
        sub_line2 = Line([lx0, sub_y2, 0], [lx1, sub_y2, 0], stroke_width=3, color=WHITE)
        self.play(Create(sub_line2), run_time=0.3)

        rem2 = Text("26", font=FONT, font_size=38, color=COLOR_ERR)
        rem2.move_to([div_cx, sub_y2 - 0.55, 0])
        self.play(Write(rem2), run_time=0.4)

        # 错误提示
        err_box = RoundedRectangle(
            width=5.5, height=0.9,
            corner_radius=0.2,
            color=COLOR_ERR,
            stroke_width=2,
            fill_color=COLOR_ERR,
            fill_opacity=0.1,
        ).move_to(DOWN * 2.5)
        err_msg = VGroup(
            MathTex(r"26 \geq 26", font_size=28, color=COLOR_ERR),
            Text("余数 >= 除数, 商偏小!", font=FONT, font_size=20, color=COLOR_ERR),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.5)

        self.play(FadeIn(err_box), FadeIn(err_msg), run_time=0.5)
        self.wait(0.8)

        # ---- 调商: 2 → 3 ----
        # 划掉 2
        cross_q2 = Cross(vdict_2["quotient"], stroke_color=COLOR_ERR, stroke_width=5)
        self.play(Create(cross_q2), run_time=0.4)

        adjust_hint = VGroup(
            Text("调大商, 改为 ", font=FONT, font_size=24, color=COLOR_OK),
            MathTex(r"3", font_size=40, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.5)

        self.play(FadeIn(adjust_hint, shift=UP * 0.2), run_time=0.4)
        self.wait(0.4)

        # 清掉旧竖式部分, 写新商
        new_quotient = Text("3", font=FONT, font_size=48, color=COLOR_OK)
        new_quotient.move_to(vdict_2["quotient"].get_center())

        # 新乘积 26×3=78
        new_prod = Text("78", font=FONT, font_size=38, color=COLOR_GUESS)
        new_prod.move_to(prod_text2.get_center())

        # 新余数 0
        new_rem = Text("0", font=FONT, font_size=38, color=COLOR_OK)
        new_rem.move_to(rem2.get_center())

        self.play(
            FadeOut(vdict_2["quotient"]), FadeOut(cross_q2),
            FadeOut(prod_text2), FadeOut(rem2),
            FadeOut(err_box), FadeOut(err_msg),
            FadeOut(adjust_hint),
            run_time=0.4,
        )

        self.play(Write(new_quotient), run_time=0.5)

        prod_note3 = VGroup(
            MathTex(r"26 \times 3 = 78", font_size=28, color=COLOR_GUESS),
        ).move_to(RIGHT * 3.0 + UP * 0.3)

        self.play(FadeIn(prod_note3), Write(new_prod), run_time=0.5)
        self.play(Write(new_rem), run_time=0.4)

        ok_msg = VGroup(
            MathTex(r"0 < 26", font_size=28, color=COLOR_OK),
            Text("余数 < 除数, 商正确!", font=FONT, font_size=20, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.3)

        self.play(FadeIn(ok_msg, scale=1.05), run_time=0.5)
        self.wait(0.5)

        # 最终答案
        final = VGroup(
            MathTex(r"78 \div 26 = ", font_size=40, color=WHITE),
            MathTex(r"3", font_size=48, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.8)

        self.play(FadeIn(final, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(prob),
            FadeOut(trial_label), FadeOut(trial_line),
            FadeOut(prod_label2), FadeOut(prod_note3),
            FadeOut(vdict_2["divisor"]), FadeOut(vdict_2["dividend"]),
            FadeOut(vdict_2["top_line"]), FadeOut(vdict_2["vert_line"]),
            FadeOut(new_quotient), FadeOut(new_prod),
            FadeOut(sub_line2), FadeOut(new_rem),
            FadeOut(ok_msg), FadeOut(final),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 6: 知识总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = self.make_title("知识总结", color=COLOR_TITLE, font_size=38)
        self.play(Write(title), run_time=0.6)

        # 总结背景
        card_bg = RoundedRectangle(
            width=7.8, height=10.5,
            corner_radius=0.35,
            color=COLOR_STEP,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=0.04,
        ).move_to(UP * 0.5)
        self.play(FadeIn(card_bg), run_time=0.4)

        # 条目
        def make_item(num_str, body_text, desc_text, icon_color):
            num_t = Text(num_str, font=FONT, font_size=26, color=icon_color)
            body_t = Text(body_text, font=FONT, font_size=24, color=WHITE)
            desc_t = Text(desc_text, font=FONT, font_size=19, color=COLOR_AUX)
            top_row = VGroup(num_t, body_t).arrange(RIGHT, buff=0.2)
            return VGroup(top_row, desc_t).arrange(DOWN, buff=0.12, aligned_edge=LEFT)

        item1 = make_item(
            "(1)", "试商: 四舍五入除数为整十数",
            "再用整十数估算出初商",
            COLOR_HL,
        )
        item2 = make_item(
            "(2)", "验证: 初商 x 除数",
            "观察积与被除数的大小关系",
            COLOR_HL,
        )
        item3 = make_item(
            "(3)", "调商规则:",
            "积 > 被除数, 商偏大, 减 1",
            COLOR_ERR,
        )
        item3_sub = Text(
            "余数 >= 除数, 商偏小, 加 1",
            font=FONT, font_size=19, color=COLOR_OK,
        )
        item4 = make_item(
            "(4)", "余数必须 < 除数",
            "否则商还需继续调整",
            COLOR_OK,
        )

        summary_items = VGroup(item1, item2, item3, item3_sub, item4)
        summary_items.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary_items.move_to(UP * 0.5)

        for it in [item1, item2, item3, item3_sub, item4]:
            self.play(FadeIn(it, shift=RIGHT * 0.3), run_time=0.45)

        # 口诀
        rhyme_bg = RoundedRectangle(
            width=7.4, height=1.8,
            corner_radius=0.25,
            color=COLOR_TITLE,
            stroke_width=2,
            fill_color=COLOR_TITLE,
            fill_opacity=0.12,
        ).move_to(DOWN * 4.5)

        rhyme = VGroup(
            Text("口诀: 四舍五入来试商,", font=FONT, font_size=21, color=COLOR_TITLE),
            Text("大了减一小了加, 余数要比除数小!", font=FONT, font_size=21, color=COLOR_TITLE),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 4.5)

        self.play(FadeIn(rhyme_bg), FadeIn(rhyme, shift=UP * 0.2), run_time=0.6)
        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(summary_items), FadeOut(rhyme_bg), FadeOut(rhyme),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        # 放大作者信息
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

        follow_text = Text(
            "关注我, 学更多小学数学!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 0.8)

        self.play(FadeIn(follow_text, shift=UP * 0.2), run_time=0.6)

        # 装饰: 六个数字围绕
        deco_nums = VGroup(*[
            MathTex(str(n), font_size=36, color=COLOR_GUESS)
            .move_to(DOWN * 3.0 + 2.2 * np.array([np.cos(i * PI / 3), np.sin(i * PI / 3), 0.0]))
            for i, n in enumerate([9, 6, 3, 2, 7, 8])
        ])
        deco_div = VGroup(*[
            MathTex(r"\div", font_size=28, color=COLOR_AUX)
            .move_to(DOWN * 3.0 + 1.1 * np.array([np.cos((i + 0.5) * PI / 3), np.sin((i + 0.5) * PI / 3), 0.0]))
            for i in range(6)
        ])

        self.play(
            *[GrowFromCenter(n) for n in deco_nums],
            *[FadeIn(d) for d in deco_div],
            run_time=0.8,
        )
        self.play(Rotate(VGroup(deco_nums, deco_div), angle=PI, run_time=1.5))

        # 最终正确答案闪烁
        ans_box = VGroup(
            MathTex(r"96 \div 32 = 3", font_size=38, color=COLOR_OK),
            MathTex(r"78 \div 26 = 3", font_size=38, color=COLOR_OK),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 5.5)

        self.play(FadeIn(ans_box, shift=UP * 0.3), run_time=0.7)
        self.play(Indicate(ans_box, color=COLOR_HL, scale_factor=1.08), run_time=0.6)
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_nums), FadeOut(deco_div),
            FadeOut(ans_box),
            run_time=1.0,
        )


# 运行命令:
# manim -pql 002_两位数除两三位数.py TwoDigitDivisionLesson   # 快速预览
# manim -qm  002_两位数除两三位数.py TwoDigitDivisionLesson   # 中等质量
# manim -qh  002_两位数除两三位数.py TwoDigitDivisionLesson   # 高质量
