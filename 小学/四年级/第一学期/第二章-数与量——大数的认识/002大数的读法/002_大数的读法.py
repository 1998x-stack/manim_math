"""
002_大数的读法.py — 大数的读法 教学动画

知识点: 大数的读法规则
  ① 从高位读起, 一级一级往下读
  ② 读亿级、万级时, 先按个级读法读, 再在后面加"亿"或"万"字
  ③ 每级末尾的0都不读, 其他数位有一个或连续几个0, 都只读一个零

年级: 四年级第一学期
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
COLOR_TITLE = "#fbbf24"        # 金黄色 标题
COLOR_LEVEL_YI = "#ef4444"     # 红色 亿级
COLOR_LEVEL_WAN = "#3b82f6"    # 蓝色 万级
COLOR_LEVEL_GE = "#22c55e"     # 绿色 个级
COLOR_ZERO = "#f97316"         # 橙色 零的读法规则
COLOR_HL = "#fbbf24"           # 黄色 高亮
COLOR_DIGIT = "#e2e8f0"        # 淡白 数字
COLOR_AUTHOR = "#6b7280"       # 灰色 作者信息
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class LargeNumberReadLesson(Scene):
    """
    大数的读法教学动画

    场景顺序:
      1. 开场钩子 - 会读这些大数吗?
      2. 数位表 - 数位与数级
      3. 读法规则一 - 从高位读起
      4. 读法规则二 - 亿级、万级读法
      5. 读法规则三 - 零的读法
      6. 例题一 - 3005000
      7. 例题二 - 200080009
      8. 知识总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_place_value_table()
        self.scene_3_rule_1()
        self.scene_4_rule_2()
        self.scene_5_rule_3()
        self.scene_6_example1()
        self.scene_7_example2()
        self.scene_8_summary()
        self.scene_9_outro()

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

    def make_title(self, text, color=COLOR_TITLE, font_size=36):
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(UP * 5.5)

    def make_subtitle(self, text, color=GRAY_A, font_size=24):
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(UP * 4.8)

    def make_rule_box(self, rule_text, detail_text, color, y_pos=2.0):
        """创建规则卡片"""
        rule_label = Text(rule_text, font=FONT, font_size=26, color=color)
        detail_label = Text(detail_text, font=FONT, font_size=20, color=GRAY_A)
        card = VGroup(rule_label, detail_label).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        card.move_to(UP * y_pos)
        return card

    def make_digit_row(self, digits, colors, font_size=48, spacing=0.85):
        """
        创建一行数字, 每位数字单独着色
        digits: list of str, e.g. ["2","0","0","0","8","0","0","0","9"]
        colors: list of Color
        """
        cells = VGroup()
        for d, c in zip(digits, colors):
            cell = Text(d, font=FONT, font_size=font_size, color=c)
            cells.add(cell)
        cells.arrange(RIGHT, buff=spacing - 0.5)
        return cells

    def make_place_name_row(self, names, colors, font_size=18, ref_group=None):
        """
        创建数位名称行, 对齐到 ref_group 的每个子元素
        """
        labels = VGroup()
        for i, (name, c) in enumerate(zip(names, colors)):
            lbl = Text(name, font=FONT, font_size=font_size, color=c)
            labels.add(lbl)
        if ref_group is not None:
            for lbl, ref in zip(labels, ref_group):
                lbl.move_to(ref.get_center() + DOWN * 0.65)
        else:
            labels.arrange(RIGHT, buff=0.15)
        return labels

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text("你会读这些大数吗?", font=FONT, font_size=40, color=COLOR_HL)
        hook.move_to(UP * 5.0)

        self.play(Write(hook), run_time=0.8)

        # 展示两个大数
        num1 = Text("3 005 000", font=FONT, font_size=52, color=COLOR_LEVEL_WAN)
        num1.move_to(UP * 3.0)
        num2 = Text("200 080 009", font=FONT, font_size=46, color=COLOR_LEVEL_YI)
        num2.move_to(UP * 1.5)

        self.play(FadeIn(num1, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(num2, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        # 难点提示
        sub = Text("别急! 三步搞定大数读法!", font=FONT, font_size=26, color=GRAY_A)
        sub.move_to(DOWN * 0.5)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(hook), FadeOut(num1), FadeOut(num2), FadeOut(sub),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 数位表 — 数位与数级
    # ------------------------------------------------------------------

    def scene_2_place_value_table(self):
        title = self.make_title("数位与数级")
        self.play(Write(title), run_time=0.6)

        # ===== 绘制数位表 =====
        # 数位名称 (从高到低)
        place_names = ["亿", "千万", "百万", "十万", "万", "千", "百", "十", "个"]
        place_colors = [
            COLOR_LEVEL_YI,
            COLOR_LEVEL_WAN, COLOR_LEVEL_WAN, COLOR_LEVEL_WAN, COLOR_LEVEL_WAN,
            COLOR_LEVEL_GE, COLOR_LEVEL_GE, COLOR_LEVEL_GE, COLOR_LEVEL_GE,
        ]

        # 数级分组标签
        level_labels = [
            ("亿级", COLOR_LEVEL_YI, 1),
            ("万级", COLOR_LEVEL_WAN, 4),
            ("个级", COLOR_LEVEL_GE, 4),
        ]

        # 表格行: 每个数位画一个格子
        # 格子宽0.78, 高0.6
        cell_w = 0.78
        cell_h = 0.6
        n_cols = len(place_names)
        table_width = cell_w * n_cols

        # 从屏幕中偏上一点居中
        table_center_x = 0.0
        table_center_y = 2.5

        # 每列 x 坐标 (左边为高位)
        col_xs = [table_center_x - table_width / 2 + cell_w * (i + 0.5) for i in range(n_cols)]

        # ---- 数位行标题格子 ----
        cells_top = VGroup()
        for i, (name, color) in enumerate(zip(place_names, place_colors)):
            rect = Rectangle(
                width=cell_w - 0.04, height=cell_h,
                color=color,
                stroke_width=1.5,
                fill_color=color,
                fill_opacity=0.12,
            ).move_to([col_xs[i], table_center_y, 0])
            lbl = Text(name, font=FONT, font_size=16, color=color)
            lbl.move_to([col_xs[i], table_center_y, 0])
            cells_top.add(VGroup(rect, lbl))

        self.play(FadeIn(cells_top, shift=DOWN * 0.3), run_time=0.8)

        # ---- 数级行 (上方括号/标签) ----
        level_group = VGroup()
        cursor = 0
        for level_name, lv_color, span in level_labels:
            x_left = col_xs[cursor]
            x_right = col_xs[cursor + span - 1]
            x_mid = (x_left + x_right) / 2
            y_bar = table_center_y + cell_h * 0.9

            # 括号横线
            brace_line = Line(
                [x_left - cell_w * 0.4, y_bar, 0],
                [x_right + cell_w * 0.4, y_bar, 0],
                color=lv_color, stroke_width=2,
            )
            # 标签
            lv_lbl = Text(level_name, font=FONT, font_size=22, color=lv_color)
            lv_lbl.move_to([x_mid, y_bar + 0.4, 0])

            level_group.add(VGroup(brace_line, lv_lbl))
            cursor += span

        self.play(FadeIn(level_group, shift=DOWN * 0.2), run_time=0.7)

        # ---- 数字行 (示意, 用9位数 200080009) ----
        demo_digits = ["2", "0", "0", "0", "8", "0", "0", "0", "9"]
        digit_colors = [
            COLOR_LEVEL_YI,
            COLOR_LEVEL_WAN, COLOR_LEVEL_WAN, COLOR_LEVEL_WAN, COLOR_LEVEL_WAN,
            COLOR_LEVEL_GE, COLOR_LEVEL_GE, COLOR_LEVEL_GE, COLOR_LEVEL_GE,
        ]
        digit_row = VGroup()
        for i, (d, dc) in enumerate(zip(demo_digits, digit_colors)):
            rect = Rectangle(
                width=cell_w - 0.04, height=cell_h,
                color=GRAY_B,
                stroke_width=1.5,
                fill_opacity=0,
            ).move_to([col_xs[i], table_center_y - cell_h, 0])
            lbl = Text(d, font=FONT, font_size=30, color=dc if d != "0" else GRAY_B)
            lbl.move_to([col_xs[i], table_center_y - cell_h, 0])
            digit_row.add(VGroup(rect, lbl))

        self.play(FadeIn(digit_row, shift=DOWN * 0.2), run_time=0.8)

        # 说明
        explain = Text(
            "每级包含4个数位, 亿级只有1个",
            font=FONT, font_size=20, color=GRAY_A,
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(cells_top), FadeOut(level_group),
            FadeOut(digit_row), FadeOut(explain),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 规则一 — 从高位读起
    # ------------------------------------------------------------------

    def scene_3_rule_1(self):
        title = self.make_title("读法规则", color=COLOR_HL)
        rule_num = Text("规则 ①", font=FONT, font_size=28, color=COLOR_HL)
        rule_num.move_to(UP * 4.8)

        self.play(Write(title), FadeIn(rule_num), run_time=0.6)

        rule_body = Text(
            "从高位读起, 一级一级往下读",
            font=FONT, font_size=26, color=WHITE,
        ).move_to(UP * 4.0)
        self.play(FadeIn(rule_body, shift=UP * 0.2), run_time=0.5)

        # 示意: 箭头从左(高位)到右(低位)
        num_row = Text("2  0  0  0  8  0  0  0  9", font=FONT, font_size=36, color=COLOR_DIGIT)
        num_row.move_to(UP * 2.0)
        self.play(FadeIn(num_row), run_time=0.5)

        arrow = Arrow(
            num_row.get_left() + LEFT * 0.3,
            num_row.get_right() + RIGHT * 0.3,
            color=COLOR_HL,
            stroke_width=4,
            buff=0.0,
            max_tip_length_to_length_ratio=0.12,
        )
        arrow.move_to(UP * 1.0)

        hi_label = Text("高位(亿)", font=FONT, font_size=20, color=COLOR_LEVEL_YI)
        hi_label.next_to(arrow, LEFT, buff=0.1)
        lo_label = Text("低位(个)", font=FONT, font_size=20, color=COLOR_LEVEL_GE)
        lo_label.next_to(arrow, RIGHT, buff=0.1)

        self.play(Create(arrow), FadeIn(hi_label), FadeIn(lo_label), run_time=0.8)

        explain = Text(
            "从最高的数位开始往右读",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(explain), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(rule_num), FadeOut(rule_body),
            FadeOut(num_row), FadeOut(arrow),
            FadeOut(hi_label), FadeOut(lo_label), FadeOut(explain),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 4: 规则二 — 亿级/万级读法
    # ------------------------------------------------------------------

    def scene_4_rule_2(self):
        title = self.make_title("读法规则", color=COLOR_HL)
        rule_num = Text("规则 ②", font=FONT, font_size=28, color=COLOR_HL)
        rule_num.move_to(UP * 4.8)

        self.play(Write(title), FadeIn(rule_num), run_time=0.6)

        rule_body = Text(
            "读亿级/万级时, 先按个级读法读,",
            font=FONT, font_size=22, color=WHITE,
        ).move_to(UP * 4.0)
        rule_body2 = Text(
            '再在后面加"亿"或"万"字',
            font=FONT, font_size=22, color=WHITE,
        ).move_to(UP * 3.4)
        self.play(FadeIn(rule_body, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(rule_body2, shift=UP * 0.2), run_time=0.4)

        # 数位格子示意 (简版, 9格)
        place_names = ["亿", "千万", "百万", "十万", "万", "千", "百", "十", "个"]
        place_colors = [
            COLOR_LEVEL_YI,
            COLOR_LEVEL_WAN, COLOR_LEVEL_WAN, COLOR_LEVEL_WAN, COLOR_LEVEL_WAN,
            COLOR_LEVEL_GE, COLOR_LEVEL_GE, COLOR_LEVEL_GE, COLOR_LEVEL_GE,
        ]
        demo_digits = ["2", "0", "0", "0", "8", "0", "0", "0", "9"]

        cell_w = 0.78
        cell_h = 0.55
        n_cols = 9
        table_width = cell_w * n_cols
        table_center_x = 0.0
        table_center_y = 1.6
        col_xs = [table_center_x - table_width / 2 + cell_w * (i + 0.5) for i in range(n_cols)]

        cells = VGroup()
        digit_labels = VGroup()
        for i, (name, color, d) in enumerate(zip(place_names, place_colors, demo_digits)):
            rect = Rectangle(
                width=cell_w - 0.04, height=cell_h,
                color=color, stroke_width=1.5,
                fill_color=color, fill_opacity=0.12,
            ).move_to([col_xs[i], table_center_y, 0])
            place_lbl = Text(name, font=FONT, font_size=14, color=color)
            place_lbl.move_to([col_xs[i], table_center_y, 0])

            digit_rect = Rectangle(
                width=cell_w - 0.04, height=cell_h,
                color=GRAY_B, stroke_width=1.5, fill_opacity=0,
            ).move_to([col_xs[i], table_center_y - cell_h, 0])
            digit_lbl = Text(d, font=FONT, font_size=26, color=color if d != "0" else GRAY_B)
            digit_lbl.move_to([col_xs[i], table_center_y - cell_h, 0])

            cells.add(VGroup(rect, place_lbl, digit_rect))
            digit_labels.add(digit_lbl)

        self.play(FadeIn(cells), FadeIn(digit_labels), run_time=0.6)

        # 亿级标注
        yi_brace_y = table_center_y + cell_h * 0.85
        yi_brace = Line(
            [col_xs[0] - cell_w * 0.4, yi_brace_y, 0],
            [col_xs[0] + cell_w * 0.4, yi_brace_y, 0],
            color=COLOR_LEVEL_YI, stroke_width=2,
        )
        yi_lbl = Text("亿级", font=FONT, font_size=20, color=COLOR_LEVEL_YI)
        yi_lbl.move_to([col_xs[0], yi_brace_y + 0.38, 0])

        # 万级标注
        wan_brace = Line(
            [col_xs[1] - cell_w * 0.4, yi_brace_y, 0],
            [col_xs[4] + cell_w * 0.4, yi_brace_y, 0],
            color=COLOR_LEVEL_WAN, stroke_width=2,
        )
        wan_lbl = Text("万级", font=FONT, font_size=20, color=COLOR_LEVEL_WAN)
        wan_lbl.move_to([col_xs[2], yi_brace_y + 0.38, 0])

        # 个级标注
        ge_brace = Line(
            [col_xs[5] - cell_w * 0.4, yi_brace_y, 0],
            [col_xs[8] + cell_w * 0.4, yi_brace_y, 0],
            color=COLOR_LEVEL_GE, stroke_width=2,
        )
        ge_lbl = Text("个级", font=FONT, font_size=20, color=COLOR_LEVEL_GE)
        ge_lbl.move_to([col_xs[6], yi_brace_y + 0.38, 0])

        self.play(
            FadeIn(yi_brace), FadeIn(yi_lbl),
            FadeIn(wan_brace), FadeIn(wan_lbl),
            FadeIn(ge_brace), FadeIn(ge_lbl),
            run_time=0.6,
        )

        # 读法步骤
        step1 = Text("亿级: 2 → 读作二, 加亿 = 二亿", font=FONT, font_size=20, color=COLOR_LEVEL_YI)
        step1.move_to(DOWN * 0.1)
        step2 = Text("万级: 0008 → 读作八万", font=FONT, font_size=20, color=COLOR_LEVEL_WAN)
        step2.move_to(DOWN * 0.8)
        step3 = Text("个级: 0009 → 读作零九", font=FONT, font_size=20, color=COLOR_LEVEL_GE)
        step3.move_to(DOWN * 1.5)

        # 高亮亿级
        self.play(Indicate(digit_labels[0], color=COLOR_LEVEL_YI, scale_factor=1.4), run_time=0.6)
        self.play(FadeIn(step1, shift=RIGHT * 0.3), run_time=0.5)

        # 高亮万级
        wan_group = VGroup(*[digit_labels[i] for i in range(1, 5)])
        self.play(Indicate(wan_group, color=COLOR_LEVEL_WAN, scale_factor=1.3), run_time=0.6)
        self.play(FadeIn(step2, shift=RIGHT * 0.3), run_time=0.5)

        # 高亮个级
        ge_group = VGroup(*[digit_labels[i] for i in range(5, 9)])
        self.play(Indicate(ge_group, color=COLOR_LEVEL_GE, scale_factor=1.3), run_time=0.6)
        self.play(FadeIn(step3, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(rule_num),
            FadeOut(rule_body), FadeOut(rule_body2),
            FadeOut(cells), FadeOut(digit_labels),
            FadeOut(yi_brace), FadeOut(yi_lbl),
            FadeOut(wan_brace), FadeOut(wan_lbl),
            FadeOut(ge_brace), FadeOut(ge_lbl),
            FadeOut(step1), FadeOut(step2), FadeOut(step3),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 5: 规则三 — 零的读法
    # ------------------------------------------------------------------

    def scene_5_rule_3(self):
        title = self.make_title("读法规则", color=COLOR_HL)
        rule_num = Text("规则 ③", font=FONT, font_size=28, color=COLOR_HL)
        rule_num.move_to(UP * 4.8)

        self.play(Write(title), FadeIn(rule_num), run_time=0.6)

        rule_body = Text("零的读法:", font=FONT, font_size=26, color=COLOR_ZERO)
        rule_body.move_to(UP * 4.0)
        self.play(FadeIn(rule_body), run_time=0.4)

        # 规则 A
        ruleA_title = Text("每级末尾的 0", font=FONT, font_size=23, color=WHITE)
        ruleA_body = Text("→ 不读", font=FONT, font_size=23, color=COLOR_ZERO)
        ruleA = VGroup(ruleA_title, ruleA_body).arrange(RIGHT, buff=0.2)
        ruleA.move_to(UP * 3.1)

        # 示意: 30050000 末尾两个0不读
        ex_a = VGroup(
            Text("30050000", font=FONT, font_size=38, color=COLOR_DIGIT),
        ).move_to(UP * 2.0)

        # 用不同颜色标记末尾0
        ex_a_parts = VGroup(
            Text("3005", font=FONT, font_size=38, color=COLOR_DIGIT),
            Text("0000", font=FONT, font_size=38, color=GRAY_B),
        ).arrange(RIGHT, buff=0.05).move_to(UP * 2.0)

        cross_line = Line(
            ex_a_parts[1].get_left() + LEFT * 0.05,
            ex_a_parts[1].get_right() + RIGHT * 0.05,
            color=COLOR_ZERO, stroke_width=3,
        )
        not_read_lbl = Text("末尾0不读", font=FONT, font_size=18, color=COLOR_ZERO)
        not_read_lbl.next_to(ex_a_parts[1], DOWN, buff=0.25)

        self.play(FadeIn(ruleA), run_time=0.5)
        self.play(FadeIn(ex_a_parts), run_time=0.5)
        self.play(Create(cross_line), FadeIn(not_read_lbl), run_time=0.6)
        self.wait(1.0)

        # 规则 B
        ruleB_title = Text("中间一个或连续多个 0", font=FONT, font_size=21, color=WHITE)
        ruleB_body = Text("→ 只读一个零", font=FONT, font_size=21, color=COLOR_ZERO)
        ruleB = VGroup(ruleB_title, ruleB_body).arrange(RIGHT, buff=0.2)
        ruleB.move_to(DOWN * 0.3)

        # 示意: 3005000 中间两个0只读一个
        ex_b_parts = VGroup(
            Text("3", font=FONT, font_size=38, color=COLOR_DIGIT),
            Text("00", font=FONT, font_size=38, color=GRAY_B),
            Text("5", font=FONT, font_size=38, color=COLOR_DIGIT),
            Text("000", font=FONT, font_size=38, color=GRAY_B),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 1.4)

        # 只读一个0
        one_zero_arrow = Arrow(
            ex_b_parts[1].get_bottom() + DOWN * 0.1,
            ex_b_parts[1].get_bottom() + DOWN * 0.6,
            color=COLOR_ZERO, stroke_width=3, buff=0.0,
            max_tip_length_to_length_ratio=0.2,
        )
        one_zero_lbl = Text("只读一个零", font=FONT, font_size=18, color=COLOR_ZERO)
        one_zero_lbl.next_to(one_zero_arrow, DOWN, buff=0.1)

        self.play(FadeIn(ruleB), run_time=0.5)
        self.play(FadeIn(ex_b_parts), run_time=0.5)
        self.play(Create(one_zero_arrow), FadeIn(one_zero_lbl), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(rule_num), FadeOut(rule_body),
            FadeOut(ruleA), FadeOut(ex_a_parts), FadeOut(cross_line), FadeOut(not_read_lbl),
            FadeOut(ruleB), FadeOut(ex_b_parts), FadeOut(one_zero_arrow), FadeOut(one_zero_lbl),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 6: 例题一 — 3005000 读作三百万五千
    # ------------------------------------------------------------------

    def scene_6_example1(self):
        title = Text("例题 ①", font=FONT, font_size=32, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 数字展示
        num_text = Text("3 005 000", font=FONT, font_size=56, color=COLOR_DIGIT)
        num_text.move_to(UP * 4.3)
        self.play(FadeIn(num_text, shift=DOWN * 0.3), run_time=0.6)

        # 数位表 (7格: 千万 百万 十万 万 千 百 十 个? 不, 3005000 是7位数)
        # 3 0 0 5 0 0 0
        # 位: 百万 十万 万 千 百 十 个
        place_names_7 = ["百万", "十万", "万", "千", "百", "十", "个"]
        place_colors_7 = [
            COLOR_LEVEL_WAN, COLOR_LEVEL_WAN, COLOR_LEVEL_WAN, COLOR_LEVEL_WAN,
            COLOR_LEVEL_GE, COLOR_LEVEL_GE, COLOR_LEVEL_GE,
        ]
        demo_d7 = ["3", "0", "0", "5", "0", "0", "0"]

        cell_w = 0.92
        cell_h = 0.55
        n7 = 7
        table_center_y = 3.0
        total_w7 = cell_w * n7
        col_xs7 = [-total_w7 / 2 + cell_w * (i + 0.5) for i in range(n7)]

        cells7 = VGroup()
        digit_labels7 = VGroup()
        for i, (name, color, d) in enumerate(zip(place_names_7, place_colors_7, demo_d7)):
            rect = Rectangle(
                width=cell_w - 0.04, height=cell_h,
                color=color, stroke_width=1.5,
                fill_color=color, fill_opacity=0.12,
            ).move_to([col_xs7[i], table_center_y, 0])
            place_lbl = Text(name, font=FONT, font_size=14, color=color)
            place_lbl.move_to([col_xs7[i], table_center_y, 0])

            digit_rect = Rectangle(
                width=cell_w - 0.04, height=cell_h,
                color=GRAY_B, stroke_width=1.5, fill_opacity=0,
            ).move_to([col_xs7[i], table_center_y - cell_h, 0])
            digit_lbl = Text(d, font=FONT, font_size=26, color=color if d != "0" else GRAY_B)
            digit_lbl.move_to([col_xs7[i], table_center_y - cell_h, 0])

            cells7.add(VGroup(rect, place_lbl, digit_rect))
            digit_labels7.add(digit_lbl)

        # 数级标注
        wan_brace_y = table_center_y + cell_h * 0.9
        wan_brace7 = Line(
            [col_xs7[0] - cell_w * 0.4, wan_brace_y, 0],
            [col_xs7[3] + cell_w * 0.4, wan_brace_y, 0],
            color=COLOR_LEVEL_WAN, stroke_width=2,
        )
        wan_lbl7 = Text("万级", font=FONT, font_size=18, color=COLOR_LEVEL_WAN)
        wan_lbl7.move_to([col_xs7[1], wan_brace_y + 0.35, 0])

        ge_brace7 = Line(
            [col_xs7[4] - cell_w * 0.4, wan_brace_y, 0],
            [col_xs7[6] + cell_w * 0.4, wan_brace_y, 0],
            color=COLOR_LEVEL_GE, stroke_width=2,
        )
        ge_lbl7 = Text("个级", font=FONT, font_size=18, color=COLOR_LEVEL_GE)
        ge_lbl7.move_to([col_xs7[5], wan_brace_y + 0.35, 0])

        self.play(FadeIn(cells7), FadeIn(digit_labels7), run_time=0.6)
        self.play(FadeIn(wan_brace7), FadeIn(wan_lbl7), FadeIn(ge_brace7), FadeIn(ge_lbl7), run_time=0.5)

        # Step-by-step 分析
        # Step 1: 万级 = 3005 → 三百零五万
        step_y = 1.0
        step1_box = RoundedRectangle(
            width=7.5, height=1.2, corner_radius=0.2,
            color=COLOR_LEVEL_WAN, stroke_width=1.5, fill_opacity=0.08,
        ).move_to(UP * step_y)
        step1_text = VGroup(
            Text("万级: 3005", font=FONT, font_size=22, color=COLOR_LEVEL_WAN),
            Text("→", font=FONT, font_size=22, color=GRAY_A),
            Text("三百零五", font=FONT, font_size=22, color=WHITE),
            Text("+", font=FONT, font_size=22, color=GRAY_A),
            Text("万", font=FONT, font_size=26, color=COLOR_LEVEL_WAN),
        ).arrange(RIGHT, buff=0.15).move_to(UP * step_y)

        # 高亮万级数字
        wan_digits_group = VGroup(*[digit_labels7[i] for i in range(4)])
        self.play(Indicate(wan_digits_group, color=COLOR_LEVEL_WAN, scale_factor=1.3), run_time=0.7)
        self.play(FadeIn(step1_box), FadeIn(step1_text), run_time=0.6)
        self.wait(0.8)

        # Step 2: 个级 = 000 → 末尾0不读
        step2_box = RoundedRectangle(
            width=7.5, height=1.2, corner_radius=0.2,
            color=COLOR_LEVEL_GE, stroke_width=1.5, fill_opacity=0.08,
        ).move_to(DOWN * 0.4)
        step2_text = VGroup(
            Text("个级: 000", font=FONT, font_size=22, color=COLOR_LEVEL_GE),
            Text("→", font=FONT, font_size=22, color=GRAY_A),
            Text("末尾0, 不读", font=FONT, font_size=22, color=COLOR_ZERO),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 0.4)

        ge_digits_group = VGroup(*[digit_labels7[i] for i in range(4, 7)])
        self.play(Indicate(ge_digits_group, color=COLOR_LEVEL_GE, scale_factor=1.3), run_time=0.7)
        self.play(FadeIn(step2_box), FadeIn(step2_text), run_time=0.6)
        self.wait(0.8)

        # 最终答案
        answer_box = RoundedRectangle(
            width=7.5, height=1.5, corner_radius=0.3,
            color=COLOR_HL, stroke_width=2, fill_opacity=0.1,
        ).move_to(DOWN * 2.0)
        answer_label = Text("读作:", font=FONT, font_size=22, color=GRAY_A)
        answer_value = Text("三百零五万", font=FONT, font_size=38, color=COLOR_HL)
        answer_row = VGroup(answer_label, answer_value).arrange(RIGHT, buff=0.2)
        answer_row.move_to(DOWN * 2.0)

        self.play(FadeIn(answer_box), Write(answer_row), run_time=0.8)
        self.play(Indicate(answer_value, color=COLOR_HL, scale_factor=1.1), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(num_text),
            FadeOut(cells7), FadeOut(digit_labels7),
            FadeOut(wan_brace7), FadeOut(wan_lbl7),
            FadeOut(ge_brace7), FadeOut(ge_lbl7),
            FadeOut(step1_box), FadeOut(step1_text),
            FadeOut(step2_box), FadeOut(step2_text),
            FadeOut(answer_box), FadeOut(answer_row),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 7: 例题二 — 200080009 读作二亿零八万零九
    # ------------------------------------------------------------------

    def scene_7_example2(self):
        title = Text("例题 ②", font=FONT, font_size=32, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 数字展示
        num_text = Text("200 080 009", font=FONT, font_size=50, color=COLOR_DIGIT)
        num_text.move_to(UP * 4.3)
        self.play(FadeIn(num_text, shift=DOWN * 0.3), run_time=0.6)

        # 数位表 (9格)
        place_names = ["亿", "千万", "百万", "十万", "万", "千", "百", "十", "个"]
        place_colors = [
            COLOR_LEVEL_YI,
            COLOR_LEVEL_WAN, COLOR_LEVEL_WAN, COLOR_LEVEL_WAN, COLOR_LEVEL_WAN,
            COLOR_LEVEL_GE, COLOR_LEVEL_GE, COLOR_LEVEL_GE, COLOR_LEVEL_GE,
        ]
        demo_digits = ["2", "0", "0", "0", "8", "0", "0", "0", "9"]

        cell_w = 0.78
        cell_h = 0.55
        n_cols = 9
        table_center_y = 2.9
        total_w = cell_w * n_cols
        col_xs = [-total_w / 2 + cell_w * (i + 0.5) for i in range(n_cols)]

        cells9 = VGroup()
        digit_labels9 = VGroup()
        for i, (name, color, d) in enumerate(zip(place_names, place_colors, demo_digits)):
            rect = Rectangle(
                width=cell_w - 0.04, height=cell_h,
                color=color, stroke_width=1.5,
                fill_color=color, fill_opacity=0.12,
            ).move_to([col_xs[i], table_center_y, 0])
            place_lbl = Text(name, font=FONT, font_size=13, color=color)
            place_lbl.move_to([col_xs[i], table_center_y, 0])

            digit_rect = Rectangle(
                width=cell_w - 0.04, height=cell_h,
                color=GRAY_B, stroke_width=1.5, fill_opacity=0,
            ).move_to([col_xs[i], table_center_y - cell_h, 0])
            digit_lbl = Text(d, font=FONT, font_size=24, color=color if d != "0" else GRAY_B)
            digit_lbl.move_to([col_xs[i], table_center_y - cell_h, 0])

            cells9.add(VGroup(rect, place_lbl, digit_rect))
            digit_labels9.add(digit_lbl)

        # 数级标注
        brace_y = table_center_y + cell_h * 0.9
        yi_brace = Line(
            [col_xs[0] - cell_w * 0.4, brace_y, 0],
            [col_xs[0] + cell_w * 0.4, brace_y, 0],
            color=COLOR_LEVEL_YI, stroke_width=2,
        )
        yi_lbl = Text("亿级", font=FONT, font_size=17, color=COLOR_LEVEL_YI)
        yi_lbl.move_to([col_xs[0], brace_y + 0.34, 0])

        wan_brace = Line(
            [col_xs[1] - cell_w * 0.4, brace_y, 0],
            [col_xs[4] + cell_w * 0.4, brace_y, 0],
            color=COLOR_LEVEL_WAN, stroke_width=2,
        )
        wan_lbl = Text("万级", font=FONT, font_size=17, color=COLOR_LEVEL_WAN)
        wan_lbl.move_to([(col_xs[1] + col_xs[4]) / 2, brace_y + 0.34, 0])

        ge_brace = Line(
            [col_xs[5] - cell_w * 0.4, brace_y, 0],
            [col_xs[8] + cell_w * 0.4, brace_y, 0],
            color=COLOR_LEVEL_GE, stroke_width=2,
        )
        ge_lbl = Text("个级", font=FONT, font_size=17, color=COLOR_LEVEL_GE)
        ge_lbl.move_to([(col_xs[5] + col_xs[8]) / 2, brace_y + 0.34, 0])

        self.play(FadeIn(cells9), FadeIn(digit_labels9), run_time=0.6)
        self.play(
            FadeIn(yi_brace), FadeIn(yi_lbl),
            FadeIn(wan_brace), FadeIn(wan_lbl),
            FadeIn(ge_brace), FadeIn(ge_lbl),
            run_time=0.5,
        )

        # 分步分析
        # Step 1: 亿级 = 2 → 二亿
        step1_box = RoundedRectangle(
            width=7.5, height=1.1, corner_radius=0.2,
            color=COLOR_LEVEL_YI, stroke_width=1.5, fill_opacity=0.08,
        ).move_to(UP * 1.4)
        step1_text = VGroup(
            Text("亿级: 2", font=FONT, font_size=20, color=COLOR_LEVEL_YI),
            Text("→", font=FONT, font_size=20, color=GRAY_A),
            Text("二 + 亿 = 二亿", font=FONT, font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 1.4)

        self.play(Indicate(digit_labels9[0], color=COLOR_LEVEL_YI, scale_factor=1.4), run_time=0.6)
        self.play(FadeIn(step1_box), FadeIn(step1_text), run_time=0.5)

        # Step 2: 万级 = 0008 → 八万, 且中间有0 → 零
        step2_box = RoundedRectangle(
            width=7.5, height=1.1, corner_radius=0.2,
            color=COLOR_LEVEL_WAN, stroke_width=1.5, fill_opacity=0.08,
        ).move_to(UP * 0.1)
        step2_text = VGroup(
            Text("万级: 0008", font=FONT, font_size=20, color=COLOR_LEVEL_WAN),
            Text("→", font=FONT, font_size=20, color=GRAY_A),
            Text("零八万", font=FONT, font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 0.1)

        wan_digits_group = VGroup(*[digit_labels9[i] for i in range(1, 5)])
        self.play(Indicate(wan_digits_group, color=COLOR_LEVEL_WAN, scale_factor=1.3), run_time=0.6)
        self.play(FadeIn(step2_box), FadeIn(step2_text), run_time=0.5)

        # Step 3: 个级 = 0009 → 零九
        step3_box = RoundedRectangle(
            width=7.5, height=1.1, corner_radius=0.2,
            color=COLOR_LEVEL_GE, stroke_width=1.5, fill_opacity=0.08,
        ).move_to(DOWN * 1.2)
        step3_text = VGroup(
            Text("个级: 0009", font=FONT, font_size=20, color=COLOR_LEVEL_GE),
            Text("→", font=FONT, font_size=20, color=GRAY_A),
            Text("零九", font=FONT, font_size=20, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.2)

        ge_digits_group = VGroup(*[digit_labels9[i] for i in range(5, 9)])
        self.play(Indicate(ge_digits_group, color=COLOR_LEVEL_GE, scale_factor=1.3), run_time=0.6)
        self.play(FadeIn(step3_box), FadeIn(step3_text), run_time=0.5)

        # 最终答案
        answer_box = RoundedRectangle(
            width=7.5, height=1.6, corner_radius=0.3,
            color=COLOR_HL, stroke_width=2, fill_opacity=0.1,
        ).move_to(DOWN * 2.7)
        answer_label = Text("读作:", font=FONT, font_size=22, color=GRAY_A)
        answer_value = Text("二亿零八万零九", font=FONT, font_size=34, color=COLOR_HL)
        answer_row = VGroup(answer_label, answer_value).arrange(RIGHT, buff=0.2)
        answer_row.move_to(DOWN * 2.7)

        self.play(FadeIn(answer_box), Write(answer_row), run_time=0.8)
        self.play(Indicate(answer_value, color=COLOR_HL, scale_factor=1.1), run_time=0.6)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(num_text),
            FadeOut(cells9), FadeOut(digit_labels9),
            FadeOut(yi_brace), FadeOut(yi_lbl),
            FadeOut(wan_brace), FadeOut(wan_lbl),
            FadeOut(ge_brace), FadeOut(ge_lbl),
            FadeOut(step1_box), FadeOut(step1_text),
            FadeOut(step2_box), FadeOut(step2_text),
            FadeOut(step3_box), FadeOut(step3_text),
            FadeOut(answer_box), FadeOut(answer_row),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 8: 知识总结
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        title = Text("知识总结", font=FONT, font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        card_bg = RoundedRectangle(
            width=7.8, height=10.5, corner_radius=0.35,
            color=WHITE, stroke_width=2,
            fill_color=WHITE, fill_opacity=0.04,
        ).move_to(UP * 0.0)
        self.play(FadeIn(card_bg), run_time=0.4)

        # 三条规则
        rule1_title = Text("① 从高位读起", font=FONT, font_size=26, color=COLOR_TITLE)
        rule1_body = Text("一级一级往下读", font=FONT, font_size=20, color=GRAY_A)
        rule1 = VGroup(rule1_title, rule1_body).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        rule1.move_to(UP * 3.5 + LEFT * 0.2)

        rule2_title = Text("② 亿级/万级读法", font=FONT, font_size=26, color=COLOR_LEVEL_WAN)
        rule2_body = Text('先按个级读, 再加"亿"或"万"字', font=FONT, font_size=20, color=GRAY_A)
        rule2 = VGroup(rule2_title, rule2_body).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        rule2.move_to(UP * 2.1 + LEFT * 0.2)

        rule3_title = Text("③ 零的读法", font=FONT, font_size=26, color=COLOR_ZERO)
        rule3_bodyA = Text("• 每级末尾的0: 不读", font=FONT, font_size=20, color=GRAY_A)
        rule3_bodyB = Text("• 中间一个或多个0: 只读一个零", font=FONT, font_size=20, color=GRAY_A)
        rule3 = VGroup(rule3_title, rule3_bodyA, rule3_bodyB).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        rule3.move_to(UP * 0.3 + LEFT * 0.2)

        self.play(FadeIn(rule1, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(rule2, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(rule3, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.3)

        # 分割线
        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1).move_to(DOWN * 1.4)
        self.play(Create(divider), run_time=0.4)

        # 例题回顾
        ex_title = Text("例题回顾", font=FONT, font_size=22, color=GRAY_A).move_to(DOWN * 1.9)
        ex1 = VGroup(
            Text("3 005 000", font=FONT, font_size=26, color=COLOR_LEVEL_WAN),
            Text("→", font=FONT, font_size=22, color=GRAY_A),
            Text("三百零五万", font=FONT, font_size=26, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.7)
        ex2 = VGroup(
            Text("200 080 009", font=FONT, font_size=24, color=COLOR_LEVEL_YI),
            Text("→", font=FONT, font_size=22, color=GRAY_A),
            Text("二亿零八万零九", font=FONT, font_size=24, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.6)

        self.play(FadeIn(ex_title), run_time=0.4)
        self.play(FadeIn(ex1, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(ex2, shift=RIGHT * 0.2), run_time=0.5)

        # 激励语
        cheer = Text("掌握规则, 再大的数也能读!", font=FONT, font_size=22, color=COLOR_ZERO)
        cheer.move_to(DOWN * 4.8)
        self.play(FadeIn(cheer, shift=UP * 0.2), run_time=0.5)

        self.wait(3.0)

        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(rule1), FadeOut(rule2), FadeOut(rule3),
            FadeOut(divider), FadeOut(ex_title),
            FadeOut(ex1), FadeOut(ex2), FadeOut(cheer),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(UP * 0.5)

        self.play(ReplacementTransform(self.author, author_big), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多数学知识!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 1.0)

        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 数字装饰
        decorations = VGroup()
        big_nums = ["亿", "万", "0", "1", "2"]
        num_positions = [
            UP * 3.5 + LEFT * 2.5,
            UP * 3.5 + RIGHT * 2.5,
            DOWN * 3.0 + LEFT * 2.0,
            DOWN * 3.0 + RIGHT * 2.0,
            DOWN * 3.0,
        ]
        num_colors = [COLOR_LEVEL_YI, COLOR_LEVEL_WAN, COLOR_ZERO, COLOR_LEVEL_GE, COLOR_HL]
        for txt, pos, col in zip(big_nums, num_positions, num_colors):
            dec = Text(txt, font=FONT, font_size=42, color=col, fill_opacity=0.5)
            dec.move_to(pos)
            decorations.add(dec)

        self.play(*[FadeIn(d, scale=0.5) for d in decorations], run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(decorations),
            run_time=1.0,
        )


# 运行命令:
# manim -pql 002_大数的读法.py LargeNumberReadLesson   # 快速预览
# manim -qm 002_大数的读法.py LargeNumberReadLesson    # 中等质量 (720p)
# manim -qh 002_大数的读法.py LargeNumberReadLesson    # 高质量 (1080p)
