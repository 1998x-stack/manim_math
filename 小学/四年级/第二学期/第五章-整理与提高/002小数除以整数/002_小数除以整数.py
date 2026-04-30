"""
小数除以整数 - Decimal Division by Integer
小学四年级 第二学期 第五章-整理与提高

内容:
- 算理：将小数除法转化为整数除法
- 商的小数点要与被除数的小数点对齐
- 以 6.8 ÷ 4 = 1.7 为例展示完整竖式计算
- 补0继续除的规则

格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ==================== 全局配置 ====================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class DecimalDivideIntegerLesson(Scene):
    """
    小数除以整数教学动画

    场景顺序:
    1. 开场钩子
    2. 核心算理：转化为整数除法
    3. 竖式演示：6.8 ÷ 4 逐步计算
    4. 关键规则：小数点对齐
    5. 进阶示例：余数补0继续除
    6. 总结口诀
    7. 片尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_TITLE = "#f0c040"
        self.COLOR_PRIMARY = "#4fc3f7"
        self.COLOR_ACCENT = "#ff7043"
        self.COLOR_GREEN = "#66bb6a"
        self.COLOR_PURPLE = "#ce93d8"
        self.COLOR_HIGHLIGHT = "#ffeb3b"
        self.COLOR_AUXILIARY = "#90a4ae"
        self.COLOR_DECIMAL_PT = "#ff5252"

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_core_principle()
        self.scene_3_long_division()
        self.scene_4_decimal_point_rule()
        self.scene_5_add_zero()
        self.scene_6_summary()
        self.scene_7_outro()

    # ==================== 场景 1：开场钩子 ====================
    def scene_1_opening(self):
        """开场：抛出问题，吸引注意力"""

        # 作者信息（顶部固定）
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_label, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook_line1 = Text(
            "6.8 ÷ 4 = ?",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_TITLE,
        ).move_to(UP * 4.5)

        hook_line2 = Text(
            "小数怎么除整数？",
            font="PingFang SC",
            font_size=34,
            color=WHITE,
        ).move_to(UP * 3.3)

        self.play(Write(hook_line1), run_time=0.8)
        self.play(FadeIn(hook_line2, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # 章节标题
        chapter = Text(
            "小数除以整数",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_PRIMARY,
        ).move_to(UP * 1.8)

        subtitle = Text(
            "四年级 · 第五章",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_AUXILIARY,
        ).move_to(UP * 1.0)

        self.play(
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            run_time=0.4,
        )
        self.play(Write(chapter), run_time=0.7)
        self.play(FadeIn(subtitle), run_time=0.4)
        self.wait(0.8)

        # 三条核心规则预告
        rules_title = Text(
            "今天学习三个关键点:",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.5)

        rule1 = Text(
            "① 按整数除法计算",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 1.5)

        rule2 = Text(
            "② 小数点与被除数对齐",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 2.4)

        rule3 = Text(
            "③ 余数后补0继续除",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_PURPLE,
        ).move_to(DOWN * 3.3)

        self.play(FadeIn(rules_title, shift=UP * 0.2), run_time=0.4)
        for rule in [rule1, rule2, rule3]:
            self.play(FadeIn(rule, shift=LEFT * 0.3), run_time=0.4)
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(chapter),
            FadeOut(subtitle),
            FadeOut(rules_title),
            FadeOut(rule1),
            FadeOut(rule2),
            FadeOut(rule3),
            run_time=0.5,
        )

    # ==================== 场景 2：核心算理 ====================
    def scene_2_core_principle(self):
        """算理：小数除以整数 = 整数除法"""

        section_title = Text(
            "算理：转化为整数除法",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_TITLE,
        ).move_to(UP * 6.0)
        self.play(Write(section_title), run_time=0.6)

        # 思路说明
        idea = Text(
            "把 6.8 看成 68 个 0.1",
            font="PingFang SC",
            font_size=30,
            color=WHITE,
        ).move_to(UP * 4.8)
        self.play(FadeIn(idea, shift=UP * 0.3), run_time=0.5)

        # 可视化：68个小方块代表6.8
        # 用两排格子：第一排6个（代表6），第二排8个（代表0.8）
        cell_size = 0.38
        cell_gap = 0.04
        cell_step = cell_size + cell_gap

        # 整数部分（6）：蓝色方块
        int_cells = VGroup()
        for i in range(6):
            rect = Square(
                side_length=cell_size,
                color=self.COLOR_PRIMARY,
                fill_color=self.COLOR_PRIMARY,
                fill_opacity=0.7,
                stroke_width=1.5,
            )
            rect.move_to(
                np.array([-2.5 + i * cell_step, 2.6, 0])
            )
            int_cells.add(rect)

        # 小数部分（0.8）：橙色方块（更小以区分）
        dec_cells = VGroup()
        for i in range(8):
            rect = Square(
                side_length=cell_size,
                color=self.COLOR_ACCENT,
                fill_color=self.COLOR_ACCENT,
                fill_opacity=0.7,
                stroke_width=1.5,
            )
            rect.move_to(
                np.array([-2.5 + i * cell_step, 2.0, 0])
            )
            dec_cells.add(rect)

        int_label = Text(
            "6（个）",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_PRIMARY,
        ).move_to(np.array([2.5, 2.6, 0]))

        dec_label = Text(
            "8（个0.1）",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_ACCENT,
        ).move_to(np.array([2.6, 2.0, 0]))

        self.play(Create(int_cells), run_time=0.6)
        self.play(Write(int_label), run_time=0.3)
        self.play(Create(dec_cells), run_time=0.6)
        self.play(Write(dec_label), run_time=0.3)

        total_label = Text(
            "合计：68 个 0.1",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 1.0)
        self.play(FadeIn(total_label, shift=UP * 0.2), run_time=0.5)

        # 分组：每4个一组
        divide_text = Text(
            "÷ 4：每份 17 个 0.1",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_GREEN,
        ).move_to(UP * 0.2)
        self.play(FadeIn(divide_text, shift=UP * 0.2), run_time=0.5)

        result_text = Text(
            "17 × 0.1 = 1.7",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.8)
        self.play(Write(result_text), run_time=0.6)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(section_title),
            FadeOut(idea),
            FadeOut(int_cells),
            FadeOut(dec_cells),
            FadeOut(int_label),
            FadeOut(dec_label),
            FadeOut(total_label),
            FadeOut(divide_text),
            FadeOut(result_text),
            run_time=0.5,
        )

    # ==================== 场景 3：竖式计算演示 ====================
    def scene_3_long_division(self):
        """逐步展示 6.8 ÷ 4 的竖式计算"""

        section_title = Text(
            "竖式计算：6.8 ÷ 4",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(section_title), run_time=0.6)

        # -------- 竖式框架 --------
        # 布局说明：
        # 竖式符号 "4 )" 放在左边，被除数 "6.8" 放在右边上方
        # 横线下面写商

        # 竖式整体居中，y 范围大约 [1.5, 5.0]
        # 竖式符号坐标系
        div_x = -0.8   # 除号"|"的 x
        num_x_start = -0.2  # 被除数数字起始 x

        # 除数标签
        divisor_text = Text(
            "4",
            font="PingFang SC",
            font_size=52,
            color=WHITE,
        ).move_to(np.array([-2.2, 3.8, 0]))

        # 竖式符号（反括号样式）
        # 右括号形状用两段线表示
        bracket_v = Line(
            start=np.array([div_x, 4.6, 0]),
            end=np.array([div_x, 2.9, 0]),
            color=WHITE,
            stroke_width=3,
        )
        bracket_h = Line(
            start=np.array([div_x, 4.6, 0]),
            end=np.array([3.2, 4.6, 0]),
            color=WHITE,
            stroke_width=3,
        )

        # 被除数 "6.8"
        dividend_6 = Text(
            "6",
            font="PingFang SC",
            font_size=52,
            color=WHITE,
        ).move_to(np.array([0.5, 3.8, 0]))

        # 小数点（红色高亮）
        dividend_dot = Text(
            ".",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_DECIMAL_PT,
        ).move_to(np.array([1.05, 3.6, 0]))

        dividend_8 = Text(
            "8",
            font="PingFang SC",
            font_size=52,
            color=WHITE,
        ).move_to(np.array([1.65, 3.8, 0]))

        self.play(
            FadeIn(divisor_text),
            Create(bracket_v),
            Create(bracket_h),
            run_time=0.6,
        )
        self.play(
            FadeIn(dividend_6),
            FadeIn(dividend_dot),
            FadeIn(dividend_8),
            run_time=0.5,
        )

        step_hint = Text(
            "第一步：先算整数部分 6 ÷ 4",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(step_hint, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # -------- Step 1: 6 ÷ 4 = 1，余 2 --------
        # 商的第一位 "1"
        quotient_1 = Text(
            "1",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_GREEN,
        ).move_to(np.array([0.5, 5.2, 0]))

        arrow_q1 = Arrow(
            start=np.array([0.5, 4.9, 0]),
            end=np.array([0.5, 5.0, 0]),
            buff=0,
            color=self.COLOR_GREEN,
            max_tip_length_to_length_ratio=0.5,
        )

        self.play(FadeIn(quotient_1, shift=DOWN * 0.3), run_time=0.4)

        # 乘法：1 × 4 = 4
        mult_line1 = Text(
            "1 × 4 = 4",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_AUXILIARY,
        ).move_to(np.array([3.5, 3.8, 0]))
        self.play(FadeIn(mult_line1), run_time=0.3)

        # 写出"4"在被除数下方，并画横线
        sub_4 = Text(
            "4",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_AUXILIARY,
        ).move_to(np.array([0.5, 2.9, 0]))

        line1 = Line(
            start=np.array([-0.0, 2.5, 0]),
            end=np.array([1.3, 2.5, 0]),
            color=WHITE,
            stroke_width=2,
        )

        self.play(FadeIn(sub_4), Create(line1), run_time=0.4)

        # 余数 2
        remainder_2 = Text(
            "2",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_ACCENT,
        ).move_to(np.array([0.5, 1.8, 0]))

        remainder_hint = Text(
            "余 2",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_ACCENT,
        ).move_to(np.array([3.5, 1.8, 0]))

        self.play(
            FadeOut(step_hint),
            FadeIn(remainder_2),
            FadeIn(remainder_hint),
            run_time=0.4,
        )
        self.wait(0.6)

        # -------- Step 2: 对齐小数点 --------
        step2_hint = Text(
            "第二步：商的小数点对齐被除数小数点",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(step2_hint, shift=UP * 0.2), run_time=0.5)

        # 商的小数点（红色大号）
        quotient_dot = Text(
            ".",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_DECIMAL_PT,
        ).move_to(np.array([1.05, 5.0, 0]))

        # 对齐虚线
        align_line = DashedLine(
            start=np.array([1.05, 5.2, 0]),
            end=np.array([1.05, 3.4, 0]),
            color=self.COLOR_DECIMAL_PT,
            dash_length=0.15,
            stroke_width=2,
        )

        self.play(Create(align_line), run_time=0.5)
        self.play(FadeIn(quotient_dot, scale=1.5), run_time=0.4)

        # 强调动画：小数点闪烁
        self.play(
            dividend_dot.animate.set_color(self.COLOR_HIGHLIGHT).scale(1.3),
            quotient_dot.animate.set_color(self.COLOR_HIGHLIGHT).scale(1.3),
            run_time=0.4,
        )
        self.play(
            dividend_dot.animate.set_color(self.COLOR_DECIMAL_PT).scale(1 / 1.3),
            quotient_dot.animate.set_color(self.COLOR_DECIMAL_PT).scale(1 / 1.3),
            run_time=0.4,
        )
        self.wait(0.5)

        # -------- Step 3: 落下 8，继续除 --------
        # 把 8 拉下来
        step3_hint = Text(
            "第三步：落下 8，算 28 ÷ 4",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 0.5)
        self.play(FadeOut(step2_hint), FadeIn(step3_hint), run_time=0.4)

        # 显示"2" "8"组合（余数2+落下的8=28）
        drop_8 = Text(
            "8",
            font="PingFang SC",
            font_size=52,
            color=WHITE,
        ).move_to(np.array([1.65, 1.8, 0]))

        # 箭头从被除数的8下移
        drop_arrow = Arrow(
            start=np.array([1.65, 3.2, 0]),
            end=np.array([1.65, 2.2, 0]),
            buff=0,
            color=self.COLOR_GREEN,
            max_tip_length_to_length_ratio=0.3,
            stroke_width=3,
        )

        self.play(Create(drop_arrow), run_time=0.4)
        self.play(FadeIn(drop_8, shift=DOWN * 0.5), run_time=0.4)
        self.play(FadeOut(drop_arrow), run_time=0.2)

        # 28 ÷ 4 = 7
        div28_hint = Text(
            "28 ÷ 4 = 7",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_AUXILIARY,
        ).move_to(np.array([3.5, 1.0, 0]))
        self.play(FadeIn(div28_hint), run_time=0.3)

        quotient_7 = Text(
            "7",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_GREEN,
        ).move_to(np.array([1.65, 5.2, 0]))

        self.play(FadeIn(quotient_7, shift=DOWN * 0.3), run_time=0.4)

        # 乘：7 × 4 = 28
        sub_28_line = Line(
            start=np.array([0.3, 0.8, 0]),
            end=np.array([2.4, 0.8, 0]),
            color=WHITE,
            stroke_width=2,
        )
        sub_28_2 = Text(
            "2",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_AUXILIARY,
        ).move_to(np.array([0.9, 0.1, 0]))
        sub_28_8 = Text(
            "8",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_AUXILIARY,
        ).move_to(np.array([1.65, 0.1, 0]))

        self.play(
            Create(sub_28_line),
            FadeIn(sub_28_2),
            FadeIn(sub_28_8),
            run_time=0.4,
        )

        # 余数 0
        remainder_0 = Text(
            "0",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_GREEN,
        ).move_to(np.array([1.65, -0.8, 0]))

        self.play(FadeIn(remainder_0), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(step3_hint), run_time=0.3)

        # -------- 最终答案框 --------
        answer_box_bg = SurroundingRectangle(
            VGroup(quotient_1, quotient_dot, quotient_7),
            color=self.COLOR_HIGHLIGHT,
            buff=0.2,
            corner_radius=0,
            stroke_width=3,
        )
        answer_text = Text(
            "所以：6.8 ÷ 4 = 1.7",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 2.2)

        self.play(Create(answer_box_bg), run_time=0.5)
        self.play(Write(answer_text), run_time=0.6)
        self.wait(1.5)

        # 清场
        self.play(
            *[
                FadeOut(obj)
                for obj in [
                    section_title,
                    divisor_text,
                    bracket_v,
                    bracket_h,
                    dividend_6,
                    dividend_dot,
                    dividend_8,
                    quotient_1,
                    quotient_dot,
                    quotient_7,
                    sub_4,
                    line1,
                    remainder_2,
                    remainder_hint,
                    align_line,
                    mult_line1,
                    drop_8,
                    div28_hint,
                    sub_28_line,
                    sub_28_2,
                    sub_28_8,
                    remainder_0,
                    answer_box_bg,
                    answer_text,
                ]
            ],
            run_time=0.6,
        )

    # ==================== 场景 4：小数点对齐规则 ====================
    def scene_4_decimal_point_rule(self):
        """强调：商的小数点必须与被除数的小数点对齐"""

        section_title = Text(
            "核心规则：小数点对齐",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(section_title), run_time=0.6)

        rule_box = Text(
            "商的小数点要与被除数的小数点对齐",
            font="PingFang SC",
            font_size=26,
            color=WHITE,
        ).move_to(UP * 5.3)

        rule_rect = SurroundingRectangle(
            rule_box,
            color=self.COLOR_ACCENT,
            buff=0.2,
            stroke_width=2,
        )

        self.play(
            FadeIn(rule_box, shift=DOWN * 0.2),
            Create(rule_rect),
            run_time=0.6,
        )

        # 对比示意图：正确 vs 错误
        # --- 正确示例 ---
        correct_label = Text(
            "正确",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_GREEN,
        ).move_to(np.array([-1.8, 3.8, 0]))

        # 竖式（简化）
        correct_dividend = Text(
            "6.8",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
        ).move_to(np.array([-1.8, 3.0, 0]))

        correct_quotient = Text(
            "1.7",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_GREEN,
        ).move_to(np.array([-1.8, 4.5, 0]))

        # 对齐线
        correct_align = DashedLine(
            start=np.array([-1.6, 4.7, 0]),
            end=np.array([-1.6, 2.7, 0]),
            color=self.COLOR_GREEN,
            dash_length=0.12,
            stroke_width=2,
        )

        correct_check = Text(
            "✓",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_GREEN,
        ).move_to(np.array([-0.2, 3.7, 0]))

        # --- 错误示例 ---
        wrong_label = Text(
            "错误",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_ACCENT,
        ).move_to(np.array([2.2, 3.8, 0]))

        wrong_dividend = Text(
            "6.8",
            font="PingFang SC",
            font_size=36,
            color=WHITE,
        ).move_to(np.array([2.2, 3.0, 0]))

        # 错误商（小数点位移）
        wrong_quotient = Text(
            "17.",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_ACCENT,
        ).move_to(np.array([2.2, 4.5, 0]))

        wrong_cross = Text(
            "✗",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_ACCENT,
        ).move_to(np.array([3.5, 3.7, 0]))

        # 分割线
        divider = Line(
            start=np.array([0.2, 2.2, 0]),
            end=np.array([0.2, 5.0, 0]),
            color=self.COLOR_AUXILIARY,
            stroke_width=1.5,
        )

        self.play(
            FadeIn(correct_label),
            FadeIn(wrong_label),
            Create(divider),
            run_time=0.4,
        )
        self.play(
            FadeIn(correct_dividend),
            FadeIn(wrong_dividend),
            run_time=0.4,
        )
        self.play(
            FadeIn(correct_quotient),
            FadeIn(wrong_quotient),
            run_time=0.4,
        )
        self.play(Create(correct_align), run_time=0.4)
        self.play(
            FadeIn(correct_check),
            FadeIn(wrong_cross),
            run_time=0.4,
        )
        self.wait(1.2)

        # 口诀强调
        mnemonic = Text(
            "口诀：小数点上下对齐",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(UP * 1.0)

        self.play(Write(mnemonic), run_time=0.6)
        self.wait(1.0)

        # 补充说明
        note1 = Text(
            "整数部分不够除时，",
            font="PingFang SC",
            font_size=24,
            color=WHITE,
        ).move_to(UP * 0.0)
        note2 = Text(
            "在个位（整数位）写 0",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_PURPLE,
        ).move_to(DOWN * 0.7)

        # 示例：0.8 ÷ 4 商的个位要写0
        example_title = Text(
            "例：0.8 ÷ 4",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_AUXILIARY,
        ).move_to(DOWN * 1.8)
        example_result = Text(
            "商 = 0.2（个位写0！）",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_PURPLE,
        ).move_to(DOWN * 2.6)

        self.play(FadeIn(note1), FadeIn(note2), run_time=0.5)
        self.play(FadeIn(example_title), run_time=0.4)
        self.play(Write(example_result), run_time=0.5)
        self.wait(1.2)

        # 清场
        self.play(
            *[
                FadeOut(obj)
                for obj in [
                    section_title,
                    rule_box,
                    rule_rect,
                    correct_label,
                    wrong_label,
                    correct_dividend,
                    wrong_dividend,
                    correct_quotient,
                    wrong_quotient,
                    correct_align,
                    correct_check,
                    wrong_cross,
                    divider,
                    mnemonic,
                    note1,
                    note2,
                    example_title,
                    example_result,
                ]
            ],
            run_time=0.5,
        )

    # ==================== 场景 5：余数补0 ====================
    def scene_5_add_zero(self):
        """进阶规则：余数后面补0继续除"""

        section_title = Text(
            "进阶：余数补0继续除",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(section_title), run_time=0.6)

        # 例：2.5 ÷ 4
        example_intro = Text(
            "例题：2.5 ÷ 4 = ?",
            font="PingFang SC",
            font_size=34,
            color=WHITE,
        ).move_to(UP * 5.4)
        self.play(FadeIn(example_intro, shift=UP * 0.2), run_time=0.5)

        # 竖式
        div_x2 = -0.8
        divisor2 = Text(
            "4",
            font="PingFang SC",
            font_size=48,
            color=WHITE,
        ).move_to(np.array([-2.2, 3.5, 0]))

        bracket_v2 = Line(
            start=np.array([div_x2, 4.3, 0]),
            end=np.array([div_x2, 2.6, 0]),
            color=WHITE,
            stroke_width=3,
        )
        bracket_h2 = Line(
            start=np.array([div_x2, 4.3, 0]),
            end=np.array([3.0, 4.3, 0]),
            color=WHITE,
            stroke_width=3,
        )

        dividend2_2 = Text(
            "2",
            font="PingFang SC",
            font_size=48,
            color=WHITE,
        ).move_to(np.array([0.3, 3.5, 0]))

        dividend2_dot = Text(
            ".",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_DECIMAL_PT,
        ).move_to(np.array([0.75, 3.3, 0]))

        dividend2_5 = Text(
            "5",
            font="PingFang SC",
            font_size=48,
            color=WHITE,
        ).move_to(np.array([1.3, 3.5, 0]))

        self.play(
            FadeIn(divisor2),
            Create(bracket_v2),
            Create(bracket_h2),
            run_time=0.5,
        )
        self.play(
            FadeIn(dividend2_2),
            FadeIn(dividend2_dot),
            FadeIn(dividend2_5),
            run_time=0.4,
        )

        # Step A: 2 ÷ 4，不够除，商0
        stepA = Text(
            "2 ÷ 4：不够！个位商 0",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(stepA, shift=UP * 0.2), run_time=0.5)

        quot2_0 = Text(
            "0",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_PURPLE,
        ).move_to(np.array([0.3, 4.8, 0]))

        quot2_dot = Text(
            ".",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_DECIMAL_PT,
        ).move_to(np.array([0.75, 4.6, 0]))

        # 对齐线
        align2 = DashedLine(
            start=np.array([0.75, 4.85, 0]),
            end=np.array([0.75, 3.1, 0]),
            color=self.COLOR_DECIMAL_PT,
            dash_length=0.12,
            stroke_width=2,
        )

        self.play(FadeIn(quot2_0, shift=DOWN * 0.2), run_time=0.4)
        self.play(Create(align2), run_time=0.3)
        self.play(FadeIn(quot2_dot, scale=1.5), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(stepA), run_time=0.3)

        # Step B: 落下5，25 ÷ 4 = 6，余1
        stepB = Text(
            "落下 5，算 25 ÷ 4 = 6，余 1",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(stepB), run_time=0.4)

        quot2_6 = Text(
            "6",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_GREEN,
        ).move_to(np.array([1.3, 4.8, 0]))

        self.play(FadeIn(quot2_6, shift=DOWN * 0.2), run_time=0.4)

        # 减法：25 - 24 = 1
        sub2_2 = Text("2", font="PingFang SC", font_size=48, color=self.COLOR_AUXILIARY).move_to(np.array([0.5, 2.4, 0]))
        sub2_4 = Text("4", font="PingFang SC", font_size=48, color=self.COLOR_AUXILIARY).move_to(np.array([1.3, 2.4, 0]))
        line2 = Line(start=np.array([0.1, 2.0, 0]), end=np.array([1.9, 2.0, 0]), color=WHITE, stroke_width=2)
        rem2_1 = Text("1", font="PingFang SC", font_size=48, color=self.COLOR_ACCENT).move_to(np.array([1.3, 1.4, 0]))

        self.play(FadeIn(sub2_2), FadeIn(sub2_4), Create(line2), run_time=0.4)
        self.play(FadeIn(rem2_1), run_time=0.3)
        self.wait(0.4)
        self.play(FadeOut(stepB), run_time=0.3)

        # Step C: 补0！关键步骤
        stepC = Text(
            "余数不为0！在余数后面补 0",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(stepC, shift=UP * 0.2), run_time=0.5)

        # 补0动画
        add_zero = Text(
            "0",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(np.array([2.1, 1.4, 0]))

        zero_circle = Circle(
            radius=0.4,
            color=self.COLOR_HIGHLIGHT,
            stroke_width=3,
        ).move_to(np.array([2.1, 1.4, 0]))

        self.play(
            FadeIn(add_zero, scale=0.3),
            Create(zero_circle),
            run_time=0.5,
        )
        self.wait(0.5)
        self.play(FadeOut(zero_circle), run_time=0.3)

        # 10 ÷ 4 = 2，余 2，继续补0
        step_10 = Text(
            "10 ÷ 4 = 2，余 2，继续补 0",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 1.5)
        self.play(FadeOut(stepC), FadeIn(step_10), run_time=0.4)

        quot2_2 = Text(
            "2",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_GREEN,
        ).move_to(np.array([2.1, 4.8, 0]))
        self.play(FadeIn(quot2_2, shift=DOWN * 0.2), run_time=0.4)

        step_25 = Text(
            "20 ÷ 4 = 5，整除！",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 2.3)
        self.play(FadeOut(step_10), FadeIn(step_25), run_time=0.4)

        quot2_5 = Text(
            "5",
            font="PingFang SC",
            font_size=48,
            color=self.COLOR_GREEN,
        ).move_to(np.array([2.8, 4.8, 0]))
        self.play(FadeIn(quot2_5, shift=DOWN * 0.2), run_time=0.4)
        self.wait(0.6)
        self.play(FadeOut(step_25), run_time=0.3)

        # 答案
        ans2 = Text(
            "2.5 ÷ 4 = 0.625",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 3.0)
        ans2_box = SurroundingRectangle(
            ans2, color=self.COLOR_HIGHLIGHT, buff=0.2, stroke_width=2
        )
        self.play(Write(ans2), Create(ans2_box), run_time=0.6)
        self.wait(1.2)

        # 补0规则总结
        zero_rule = Text(
            "规则：余数后补0，继续除，直到余数为0",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_PURPLE,
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(zero_rule, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清场
        self.play(
            *[
                FadeOut(obj)
                for obj in [
                    section_title,
                    example_intro,
                    divisor2,
                    bracket_v2,
                    bracket_h2,
                    dividend2_2,
                    dividend2_dot,
                    dividend2_5,
                    quot2_0,
                    quot2_dot,
                    quot2_6,
                    quot2_2,
                    quot2_5,
                    align2,
                    sub2_2,
                    sub2_4,
                    line2,
                    rem2_1,
                    add_zero,
                    ans2,
                    ans2_box,
                    zero_rule,
                ]
            ],
            run_time=0.6,
        )

    # ==================== 场景 6：总结口诀 ====================
    def scene_6_summary(self):
        """三步口诀总结"""

        section_title = Text(
            "三步口诀总结",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_TITLE,
        ).move_to(UP * 6.5)
        self.play(Write(section_title), run_time=0.6)

        # 大框口诀卡片
        card_texts = [
            ("第一步", "按整数除法逐位去除", self.COLOR_GREEN),
            ("第二步", "商的小数点对准被除数小数点", self.COLOR_ACCENT),
            ("第三步", "余数后补0，继续除到整除", self.COLOR_PURPLE),
        ]

        cards = VGroup()
        for i, (step, content, color) in enumerate(card_texts):
            y_pos = 4.0 - i * 2.2

            # 背景色块
            bg = Rectangle(
                width=7.5,
                height=1.7,
                fill_color=color,
                fill_opacity=0.15,
                stroke_color=color,
                stroke_width=2,
            ).move_to(np.array([0, y_pos, 0]))

            step_text = Text(
                step,
                font="PingFang SC",
                font_size=28,
                color=color,
            ).move_to(np.array([-2.5, y_pos + 0.2, 0]))

            content_text = Text(
                content,
                font="PingFang SC",
                font_size=22,
                color=WHITE,
            ).move_to(np.array([0.8, y_pos - 0.2, 0]))

            card_group = VGroup(bg, step_text, content_text)
            cards.add(card_group)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        # 公式展示
        formula_line1 = Text(
            "记住：",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(np.array([-2.5, -2.8, 0]))

        formula_line2 = Text(
            "小数 ÷ 整数 = 小数",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(np.array([1.2, -2.8, 0]))

        key_formula = MathTex(
            r"6.8 \div 4 = 1.7",
            font_size=40,
            color=self.COLOR_GREEN,
        ).move_to(np.array([0, -4.0, 0]))

        self.play(
            FadeIn(formula_line1),
            FadeIn(formula_line2),
            run_time=0.5,
        )
        self.play(Write(key_formula), run_time=0.6)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(section_title),
            FadeOut(cards),
            FadeOut(formula_line1),
            FadeOut(formula_line2),
            FadeOut(key_formula),
            run_time=0.6,
        )

    # ==================== 场景 7：片尾关注 ====================
    def scene_7_outro(self):
        """片尾：作者信息 + 关注提示"""

        # 作者名放大居中
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE,
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_AUXILIARY,
        ).move_to(UP * 1.0)

        self.play(
            self.author_label.animate.move_to(UP * 2.0).set_color(WHITE).scale(40 / 18),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注提示
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 装饰：三个小数点图标
        dots_deco = VGroup(
            *[
                Dot(radius=0.15, color=self.COLOR_DECIMAL_PT, fill_opacity=0.9).move_to(
                    np.array([-1.5 + i * 1.5, -2.0, 0])
                )
                for i in range(3)
            ]
        )
        self.play(
            *[FadeIn(d, scale=0.3) for d in dots_deco],
            run_time=0.5,
        )

        # 复习卡：快速展示三步
        review_bg = Rectangle(
            width=7.0,
            height=3.5,
            fill_color="#16213e",
            fill_opacity=0.95,
            stroke_color=self.COLOR_PRIMARY,
            stroke_width=2,
        ).move_to(DOWN * 4.0)

        review_title = Text(
            "小数除以整数 — 三步法",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_PRIMARY,
        ).move_to(DOWN * 2.7)

        review_r1 = Text(
            "① 按整数除法计算",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_GREEN,
        ).move_to(DOWN * 3.4)

        review_r2 = Text(
            "② 小数点对齐被除数小数点",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_ACCENT,
        ).move_to(DOWN * 4.1)

        review_r3 = Text(
            "③ 余数后补0继续除",
            font="PingFang SC",
            font_size=20,
            color=self.COLOR_PURPLE,
        ).move_to(DOWN * 4.8)

        self.play(FadeIn(review_bg), run_time=0.4)
        self.play(
            FadeIn(review_title),
            FadeIn(review_r1),
            FadeIn(review_r2),
            FadeIn(review_r3),
            run_time=0.6,
        )

        self.wait(2.0)

        # 最终淡出
        self.play(
            FadeOut(self.author_label),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(dots_deco),
            FadeOut(review_bg),
            FadeOut(review_title),
            FadeOut(review_r1),
            FadeOut(review_r2),
            FadeOut(review_r3),
            run_time=1.0,
        )
        self.wait(0.5)
