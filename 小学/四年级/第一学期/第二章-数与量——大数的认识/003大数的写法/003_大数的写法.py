"""
003_大数的写法.py — 大数的写法 教学动画

知识点: 大数的写法规则
  ① 从高位写起, 先写亿级, 再写万级, 最后写个级
  ② 哪一位上一个单位也没有, 就在那一位上写 0 占位

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
BG_COLOR     = "#1a1a2e"
COLOR_TITLE  = "#fbbf24"       # 金黄 标题
COLOR_YI     = "#ef4444"       # 红色 亿级
COLOR_WAN    = "#3b82f6"       # 蓝色 万级
COLOR_GE     = "#22c55e"       # 绿色 个级
COLOR_ZERO   = "#f97316"       # 橙色 零占位
COLOR_HL     = "#fbbf24"       # 黄色 高亮
COLOR_DIGIT  = "#e2e8f0"       # 淡白 数字
COLOR_AUTHOR = "#6b7280"       # 灰色 作者
FONT         = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class LargeNumberWriteLesson(Scene):
    """
    大数的写法教学动画

    场景顺序:
      1. 开场钩子 — 你会写这些大数吗?
      2. 数位表 — 亿级/万级/个级
      3. 写法规则一 — 从高位写起
      4. 写法规则二 — 0 占位
      5. 例题一 — 二千五百万 → 25000000
      6. 例题二 — 三亿零五十万 → 305000000
      7. 易错提示 — 连续 0 的占位
      8. 知识总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_place_value_table()
        self.scene_3_rule_1()
        self.scene_4_rule_2()
        self.scene_5_example1()
        self.scene_6_example2()
        self.scene_7_pitfall()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_title(self, text, color=COLOR_TITLE, font_size=36):
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(UP * 5.5)

    def _build_place_table(
        self,
        place_names, place_colors, digits,
        cell_w=0.78, cell_h=0.55,
        table_center_y=2.5,
        place_font=14, digit_font=26,
    ):
        """
        构建数位格子表，返回 (cells_vg, digit_labels_vg, col_xs)
        cells_vg   : 包含上方数位格子（名称行 + 数字行矩形）的 VGroup
        digit_labels_vg : 仅数字文字的 VGroup（用于 Indicate）
        col_xs     : 每列中心 x 坐标列表
        """
        n = len(place_names)
        total_w = cell_w * n
        col_xs = [-total_w / 2 + cell_w * (i + 0.5) for i in range(n)]

        cells_vg = VGroup()
        digit_labels_vg = VGroup()

        for i, (name, color, d) in enumerate(zip(place_names, place_colors, digits)):
            # 数位名称格
            rect_top = Rectangle(
                width=cell_w - 0.04, height=cell_h,
                color=color, stroke_width=1.5,
                fill_color=color, fill_opacity=0.12,
            ).move_to([col_xs[i], table_center_y, 0])
            lbl_top = Text(name, font=FONT, font_size=place_font, color=color)
            lbl_top.move_to([col_xs[i], table_center_y, 0])

            # 数字格
            rect_bot = Rectangle(
                width=cell_w - 0.04, height=cell_h,
                color=GRAY_B, stroke_width=1.5, fill_opacity=0,
            ).move_to([col_xs[i], table_center_y - cell_h, 0])
            lbl_bot = Text(
                d, font=FONT, font_size=digit_font,
                color=(COLOR_ZERO if d == "0" else color),
            )
            lbl_bot.move_to([col_xs[i], table_center_y - cell_h, 0])

            cells_vg.add(VGroup(rect_top, lbl_top, rect_bot))
            digit_labels_vg.add(lbl_bot)

        return cells_vg, digit_labels_vg, col_xs

    def _build_level_braces(self, col_xs, brace_y, cell_w, levels):
        """
        levels: list of (level_name, color, start_idx, end_idx)
        返回 VGroup
        """
        grp = VGroup()
        for name, color, s, e in levels:
            line = Line(
                [col_xs[s] - cell_w * 0.4, brace_y, 0],
                [col_xs[e] + cell_w * 0.4, brace_y, 0],
                color=color, stroke_width=2,
            )
            mid_x = (col_xs[s] + col_xs[e]) / 2
            lbl = Text(name, font=FONT, font_size=18, color=color)
            lbl.move_to([mid_x, brace_y + 0.38, 0])
            grp.add(VGroup(line, lbl))
        return grp

    def _step_box(self, text_parts, color, y_pos, box_w=7.5, box_h=1.15):
        """创建一个分析步骤卡片，text_parts 为 (txt, color) 列表"""
        box = RoundedRectangle(
            width=box_w, height=box_h, corner_radius=0.2,
            color=color, stroke_width=1.5, fill_opacity=0.08,
        ).move_to(UP * y_pos)
        labels = VGroup()
        for txt, c in text_parts:
            labels.add(Text(txt, font=FONT, font_size=20, color=c))
        labels.arrange(RIGHT, buff=0.15).move_to(UP * y_pos)
        return box, labels

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text("你会写这些大数吗?", font=FONT, font_size=40, color=COLOR_HL)
        hook.move_to(UP * 5.0)
        self.play(Write(hook), run_time=0.7)

        # 汉字形式展示
        ch1 = Text("二千五百万", font=FONT, font_size=44, color=COLOR_WAN)
        ch1.move_to(UP * 3.2)
        ch2 = Text("三亿零五十万", font=FONT, font_size=40, color=COLOR_YI)
        ch2.move_to(UP * 1.8)

        self.play(FadeIn(ch1, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(ch2, shift=UP * 0.3), run_time=0.6)
        self.wait(0.5)

        # 问号 → 数字形式（淡入）
        arrow1 = Text("→ ?", font=FONT, font_size=36, color=GRAY_A).next_to(ch1, RIGHT, buff=0.3)
        arrow2 = Text("→ ?", font=FONT, font_size=36, color=GRAY_A).next_to(ch2, RIGHT, buff=0.3)
        self.play(FadeIn(arrow1), FadeIn(arrow2), run_time=0.5)
        self.wait(0.5)

        # 提示
        tip = Text("掌握两条规则, 轻松搞定!", font=FONT, font_size=26, color=GRAY_A)
        tip.move_to(DOWN * 0.5)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(hook), FadeOut(ch1), FadeOut(ch2),
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(tip),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 数位表
    # ------------------------------------------------------------------

    def scene_2_place_value_table(self):
        title = self.make_title("数位与数级")
        self.play(Write(title), run_time=0.6)

        place_names  = ["亿", "千万", "百万", "十万", "万", "千", "百", "十", "个"]
        place_colors = [
            COLOR_YI,
            COLOR_WAN, COLOR_WAN, COLOR_WAN, COLOR_WAN,
            COLOR_GE,  COLOR_GE,  COLOR_GE,  COLOR_GE,
        ]
        # 示意数字: 305000000 = 三亿零五十万
        demo_digits = ["3", "0", "5", "0", "0", "0", "0", "0", "0"]

        cells, dlabels, col_xs = self._build_place_table(
            place_names, place_colors, demo_digits,
            cell_w=0.78, cell_h=0.58,
            table_center_y=2.5,
            place_font=14, digit_font=26,
        )

        self.play(FadeIn(cells, shift=DOWN * 0.3), run_time=0.8)
        self.play(FadeIn(dlabels, shift=DOWN * 0.2), run_time=0.5)

        # 数级标注
        brace_y = 2.5 + 0.58 * 0.9
        level_braces = self._build_level_braces(
            col_xs, brace_y, 0.78,
            [
                ("亿级", COLOR_YI,  0, 0),
                ("万级", COLOR_WAN, 1, 4),
                ("个级", COLOR_GE,  5, 8),
            ],
        )
        self.play(FadeIn(level_braces, shift=DOWN * 0.2), run_time=0.7)

        # 写法顺序箭头: 从左到右
        arr_start = [col_xs[0] - 0.3, 2.5 - 0.58 - 0.55, 0]
        arr_end   = [col_xs[8] + 0.3, 2.5 - 0.58 - 0.55, 0]
        order_arrow = Arrow(
            arr_start, arr_end,
            color=COLOR_HL, stroke_width=3, buff=0.0,
            max_tip_length_to_length_ratio=0.1,
        )
        order_label = Text("从高位(亿)写到低位(个)", font=FONT, font_size=20, color=COLOR_HL)
        order_label.next_to(order_arrow, DOWN, buff=0.18)

        self.play(Create(order_arrow), run_time=0.6)
        self.play(FadeIn(order_label), run_time=0.4)
        self.wait(2.0)

        # 解释: 0 占位高亮
        zero_note = Text("0 占位: 该位没有单位就写 0", font=FONT, font_size=22, color=COLOR_ZERO)
        zero_note.move_to(DOWN * 0.5)
        # 高亮所有 0
        zero_labels = VGroup(*[dlabels[i] for i in range(9) if demo_digits[i] == "0"])
        self.play(Indicate(zero_labels, color=COLOR_ZERO, scale_factor=1.35), run_time=0.8)
        self.play(FadeIn(zero_note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(cells), FadeOut(dlabels),
            FadeOut(level_braces), FadeOut(order_arrow),
            FadeOut(order_label), FadeOut(zero_note),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 写法规则一 — 从高位写起
    # ------------------------------------------------------------------

    def scene_3_rule_1(self):
        title = self.make_title("写法规则", color=COLOR_HL)
        rule_num = Text("规则 ①", font=FONT, font_size=28, color=COLOR_HL)
        rule_num.move_to(UP * 4.8)
        self.play(Write(title), FadeIn(rule_num), run_time=0.6)

        rule_body = Text(
            "从高位写起",
            font=FONT, font_size=32, color=WHITE,
        ).move_to(UP * 3.9)
        rule_detail = Text(
            "先写亿级 → 再写万级 → 最后写个级",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(UP * 3.1)
        self.play(FadeIn(rule_body, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(rule_detail, shift=UP * 0.2), run_time=0.5)

        # 三级流程图
        box_yi  = RoundedRectangle(width=2.0, height=0.85, corner_radius=0.18,
                                   color=COLOR_YI, stroke_width=2, fill_opacity=0.15)
        lbl_yi  = Text("亿级", font=FONT, font_size=26, color=COLOR_YI)
        grp_yi  = VGroup(box_yi, lbl_yi).move_to(UP * 1.8 + LEFT * 2.8)

        arr1 = Arrow(LEFT * 0.3, RIGHT * 0.3, color=GRAY_A, stroke_width=3, buff=0.0,
                     max_tip_length_to_length_ratio=0.3).move_to(UP * 1.8 + LEFT * 1.2)

        box_wan = RoundedRectangle(width=2.0, height=0.85, corner_radius=0.18,
                                   color=COLOR_WAN, stroke_width=2, fill_opacity=0.15)
        lbl_wan = Text("万级", font=FONT, font_size=26, color=COLOR_WAN)
        grp_wan = VGroup(box_wan, lbl_wan).move_to(UP * 1.8)

        arr2 = Arrow(LEFT * 0.3, RIGHT * 0.3, color=GRAY_A, stroke_width=3, buff=0.0,
                     max_tip_length_to_length_ratio=0.3).move_to(UP * 1.8 + RIGHT * 1.2)

        box_ge  = RoundedRectangle(width=2.0, height=0.85, corner_radius=0.18,
                                   color=COLOR_GE, stroke_width=2, fill_opacity=0.15)
        lbl_ge  = Text("个级", font=FONT, font_size=26, color=COLOR_GE)
        grp_ge  = VGroup(box_ge, lbl_ge).move_to(UP * 1.8 + RIGHT * 2.8)

        self.play(FadeIn(grp_yi, scale=0.8), run_time=0.4)
        self.play(Create(arr1), FadeIn(grp_wan, scale=0.8), run_time=0.4)
        self.play(Create(arr2), FadeIn(grp_ge, scale=0.8), run_time=0.4)

        # 示例: 三亿零五十万 — 展示写法顺序
        ex_label = Text("例: 三亿零五十万", font=FONT, font_size=26, color=COLOR_DIGIT)
        ex_label.move_to(UP * 0.4)
        self.play(FadeIn(ex_label), run_time=0.4)

        # 分步写出
        step_yi  = Text("3________", font=FONT, font_size=30, color=COLOR_YI)
        step_yi.move_to(DOWN * 0.5)
        step_wan = Text("05______", font=FONT, font_size=30, color=COLOR_WAN)
        step_wan.next_to(step_yi, RIGHT, buff=0.05)
        step_ge  = Text("0000", font=FONT, font_size=30, color=COLOR_GE)
        step_ge.next_to(step_wan, RIGHT, buff=0.05)

        note_yi  = Text("← 亿级: 3", font=FONT, font_size=18, color=COLOR_YI).next_to(step_yi, DOWN, buff=0.15)
        note_wan = Text("← 万级: 0500", font=FONT, font_size=18, color=COLOR_WAN).next_to(step_wan, DOWN, buff=0.15)
        note_ge  = Text("← 个级: 0000", font=FONT, font_size=18, color=COLOR_GE).next_to(step_ge, DOWN, buff=0.15)

        # 整体居中
        full_row = VGroup(step_yi, step_wan, step_ge).arrange(RIGHT, buff=0.0)
        full_row.move_to(DOWN * 0.5)
        note_row = VGroup(note_yi, note_wan, note_ge)
        for note, ref in zip(note_row, full_row):
            note.next_to(ref, DOWN, buff=0.15)

        self.play(Write(step_yi), FadeIn(note_yi), run_time=0.6)
        self.play(Write(step_wan), FadeIn(note_wan), run_time=0.6)
        self.play(Write(step_ge), FadeIn(note_ge), run_time=0.6)

        # 最终结果
        result = Text("→  305000000", font=FONT, font_size=32, color=COLOR_HL)
        result.move_to(DOWN * 2.2)
        self.play(FadeIn(result, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(rule_num), FadeOut(rule_body), FadeOut(rule_detail),
            FadeOut(grp_yi), FadeOut(arr1), FadeOut(grp_wan), FadeOut(arr2), FadeOut(grp_ge),
            FadeOut(ex_label), FadeOut(full_row), FadeOut(note_row), FadeOut(result),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 4: 写法规则二 — 0 占位
    # ------------------------------------------------------------------

    def scene_4_rule_2(self):
        title = self.make_title("写法规则", color=COLOR_HL)
        rule_num = Text("规则 ②", font=FONT, font_size=28, color=COLOR_HL)
        rule_num.move_to(UP * 4.8)
        self.play(Write(title), FadeIn(rule_num), run_time=0.6)

        rule_body = Text(
            "哪一位上没有单位, 就写 0 占位",
            font=FONT, font_size=26, color=WHITE,
        ).move_to(UP * 3.9)
        self.play(FadeIn(rule_body, shift=UP * 0.2), run_time=0.5)

        # 对比示例: 二千五百万 (无 0 占位的错误 vs 正确)
        ex_label = Text("以 二千五百万 为例:", font=FONT, font_size=24, color=GRAY_A)
        ex_label.move_to(UP * 2.8)
        self.play(FadeIn(ex_label), run_time=0.4)

        # 错误写法
        wrong_title = Text("错误写法:", font=FONT, font_size=22, color="#ef4444")
        wrong_title.move_to(UP * 2.0 + LEFT * 2.0)
        wrong_num = Text("2500", font=FONT, font_size=36, color="#ef4444")
        wrong_num.move_to(UP * 1.2 + LEFT * 2.0)
        cross = Cross(wrong_num, color="#ef4444", stroke_width=5)

        # 正确写法
        right_title = Text("正确写法:", font=FONT, font_size=22, color=COLOR_GE)
        right_title.move_to(UP * 2.0 + RIGHT * 2.0)
        right_num = Text("25000000", font=FONT, font_size=36, color=COLOR_GE)
        right_num.move_to(UP * 1.2 + RIGHT * 2.0)
        check = Text("✓", font=FONT, font_size=40, color=COLOR_GE)
        check.next_to(right_num, RIGHT, buff=0.2)

        self.play(FadeIn(wrong_title), FadeIn(right_title), run_time=0.4)
        self.play(FadeIn(wrong_num), FadeIn(right_num), run_time=0.5)
        self.play(Create(cross), FadeIn(check), run_time=0.6)

        # 解释: 个级 (万 以下) 全部没有单位 → 全写 0
        explain = VGroup(
            Text("二千五百万: 亿级 → 无, 万级 → 2500,", font=FONT, font_size=20, color=GRAY_A),
            Text("个级 (千、百、十、个) → 全部没有 → 写 0000", font=FONT, font_size=20, color=COLOR_ZERO),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        explain.move_to(DOWN * 0.4)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.6)
        self.wait(0.8)

        # 数位格展示: 0 0 2 5 0 0 0 0 0 (9位, 从亿位开始)
        # 二千五百万 = 25,000,000 → 亿位=0, 千万=2, 百万=5, 十万=0, 万=0, ...
        # 实际上 25,000,000 是 8位数, 没有亿位
        # place_names: 千万 百万 十万 万 千 百 十 个 (8位)
        place_names8  = ["千万", "百万", "十万", "万", "千", "百", "十", "个"]
        place_colors8 = [COLOR_WAN]*4 + [COLOR_GE]*4
        digits8       = ["2", "5", "0", "0", "0", "0", "0", "0"]

        cells8, dlabels8, col_xs8 = self._build_place_table(
            place_names8, place_colors8, digits8,
            cell_w=0.82, cell_h=0.55,
            table_center_y=-1.8,
            place_font=14, digit_font=26,
        )

        brace_y8 = -1.8 + 0.55 * 0.9
        braces8 = self._build_level_braces(
            col_xs8, brace_y8, 0.82,
            [("万级", COLOR_WAN, 0, 3), ("个级", COLOR_GE, 4, 7)],
        )

        self.play(FadeIn(cells8, shift=DOWN * 0.2), FadeIn(dlabels8), run_time=0.7)
        self.play(FadeIn(braces8), run_time=0.4)

        # 高亮 0 位
        zero_grp = VGroup(*[dlabels8[i] for i in range(8) if digits8[i] == "0"])
        self.play(Indicate(zero_grp, color=COLOR_ZERO, scale_factor=1.4), run_time=0.8)

        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(rule_num), FadeOut(rule_body),
            FadeOut(ex_label),
            FadeOut(wrong_title), FadeOut(wrong_num), FadeOut(cross),
            FadeOut(right_title), FadeOut(right_num), FadeOut(check),
            FadeOut(explain), FadeOut(cells8), FadeOut(dlabels8), FadeOut(braces8),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 5: 例题一 — 二千五百万 → 25000000
    # ------------------------------------------------------------------

    def scene_5_example1(self):
        title = Text("例题 ①", font=FONT, font_size=32, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        question = Text("二千五百万  写作:", font=FONT, font_size=34, color=COLOR_DIGIT)
        question.move_to(UP * 4.5)
        self.play(FadeIn(question, shift=DOWN * 0.3), run_time=0.5)

        # 数位表 (8格: 千万~个)
        place_names  = ["千万", "百万", "十万", "万", "千", "百", "十", "个"]
        place_colors = [COLOR_WAN]*4 + [COLOR_GE]*4
        digits       = ["?", "?", "?", "?", "?", "?", "?", "?"]

        cells, dlabels, col_xs = self._build_place_table(
            place_names, place_colors, digits,
            cell_w=0.82, cell_h=0.58,
            table_center_y=3.2,
            place_font=14, digit_font=28,
        )
        brace_y = 3.2 + 0.58 * 0.9
        braces = self._build_level_braces(
            col_xs, brace_y, 0.82,
            [("万级", COLOR_WAN, 0, 3), ("个级", COLOR_GE, 4, 7)],
        )

        # 先显示空表
        self.play(FadeIn(cells), FadeIn(dlabels), FadeIn(braces), run_time=0.7)
        self.wait(0.3)

        # Step 1: 分析万级 "二千五百" → 2500
        box1, lbl1 = self._step_box(
            [("万级: 二千五百", COLOR_WAN), ("→", GRAY_A), ("2500", COLOR_WAN)],
            COLOR_WAN, y_pos=2.0,
        )
        self.play(
            Indicate(VGroup(*[cells[i] for i in range(4)]), color=COLOR_WAN, scale_factor=1.1),
            run_time=0.6,
        )
        self.play(FadeIn(box1), FadeIn(lbl1), run_time=0.5)

        # 填写万级数字
        filled_wan = VGroup()
        wan_digits = ["2", "5", "0", "0"]
        for i, d in enumerate(wan_digits):
            lbl = Text(d, font=FONT, font_size=28, color=COLOR_WAN if d != "0" else COLOR_ZERO)
            lbl.move_to(dlabels[i].get_center())
            filled_wan.add(lbl)
        self.play(
            FadeOut(VGroup(*[dlabels[i] for i in range(4)])),
            FadeIn(filled_wan),
            run_time=0.5,
        )
        self.wait(0.4)

        # Step 2: 分析个级 — 千百十个全没有 → 0000
        box2, lbl2 = self._step_box(
            [("个级: 千百十个均无", COLOR_GE), ("→", GRAY_A), ("0000", COLOR_ZERO)],
            COLOR_GE, y_pos=0.7,
        )
        self.play(
            Indicate(VGroup(*[cells[i] for i in range(4, 8)]), color=COLOR_GE, scale_factor=1.1),
            run_time=0.6,
        )
        self.play(FadeIn(box2), FadeIn(lbl2), run_time=0.5)

        # 填写个级数字 (全 0)
        filled_ge = VGroup()
        for i in range(4, 8):
            lbl = Text("0", font=FONT, font_size=28, color=COLOR_ZERO)
            lbl.move_to(dlabels[i].get_center())
            filled_ge.add(lbl)
        self.play(
            FadeOut(VGroup(*[dlabels[i] for i in range(4, 8)])),
            FadeIn(filled_ge),
            run_time=0.5,
        )
        self.wait(0.4)

        # 答案框
        ans_box = RoundedRectangle(
            width=7.5, height=1.6, corner_radius=0.3,
            color=COLOR_HL, stroke_width=2, fill_opacity=0.1,
        ).move_to(DOWN * 1.0)
        ans_row = VGroup(
            Text("写作:", font=FONT, font_size=24, color=GRAY_A),
            Text("25000000", font=FONT, font_size=42, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.0)

        self.play(FadeIn(ans_box), Write(ans_row), run_time=0.7)
        self.play(Indicate(ans_row[1], color=COLOR_HL, scale_factor=1.08), run_time=0.6)

        # 数位分组提示
        group_hint = Text("= 2500  0000", font=FONT, font_size=28, color=COLOR_DIGIT)
        group_hint.move_to(DOWN * 2.3)
        hint_note = Text("(每四位一组)", font=FONT, font_size=20, color=GRAY_A)
        hint_note.next_to(group_hint, DOWN, buff=0.12)
        self.play(FadeIn(group_hint), FadeIn(hint_note), run_time=0.5)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(question),
            FadeOut(cells), FadeOut(dlabels), FadeOut(braces),
            FadeOut(filled_wan), FadeOut(filled_ge),
            FadeOut(box1), FadeOut(lbl1),
            FadeOut(box2), FadeOut(lbl2),
            FadeOut(ans_box), FadeOut(ans_row),
            FadeOut(group_hint), FadeOut(hint_note),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 6: 例题二 — 三亿零五十万 → 305000000
    # ------------------------------------------------------------------

    def scene_6_example2(self):
        title = Text("例题 ②", font=FONT, font_size=32, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        question = Text("三亿零五十万  写作:", font=FONT, font_size=32, color=COLOR_DIGIT)
        question.move_to(UP * 4.5)
        self.play(FadeIn(question, shift=DOWN * 0.3), run_time=0.5)

        # 数位表 (9格: 亿~个)
        place_names  = ["亿", "千万", "百万", "十万", "万", "千", "百", "十", "个"]
        place_colors = [COLOR_YI] + [COLOR_WAN]*4 + [COLOR_GE]*4
        digits_q     = ["?", "?", "?", "?", "?", "?", "?", "?", "?"]

        cells, dlabels, col_xs = self._build_place_table(
            place_names, place_colors, digits_q,
            cell_w=0.78, cell_h=0.55,
            table_center_y=3.2,
            place_font=13, digit_font=26,
        )
        brace_y = 3.2 + 0.55 * 0.9
        braces = self._build_level_braces(
            col_xs, brace_y, 0.78,
            [("亿级", COLOR_YI, 0, 0), ("万级", COLOR_WAN, 1, 4), ("个级", COLOR_GE, 5, 8)],
        )

        self.play(FadeIn(cells), FadeIn(dlabels), FadeIn(braces), run_time=0.7)
        self.wait(0.3)

        # Step 1: 亿级 "三亿" → 3
        box1, lbl1 = self._step_box(
            [("亿级: 三亿", COLOR_YI), ("→", GRAY_A), ("3", COLOR_YI)],
            COLOR_YI, y_pos=2.0,
        )
        self.play(Indicate(cells[0], color=COLOR_YI, scale_factor=1.2), run_time=0.6)
        self.play(FadeIn(box1), FadeIn(lbl1), run_time=0.5)

        f_yi = Text("3", font=FONT, font_size=26, color=COLOR_YI)
        f_yi.move_to(dlabels[0].get_center())
        self.play(FadeOut(dlabels[0]), FadeIn(f_yi), run_time=0.4)
        self.wait(0.3)

        # Step 2: 万级 "零五十万" → 0050
        # 三亿零五十万: 万级 = 0050 (千万=0, 百万=0, 十万=5, 万=0)
        box2, lbl2 = self._step_box(
            [("万级: 零五十万", COLOR_WAN), ("→", GRAY_A), ("0050", COLOR_WAN)],
            COLOR_WAN, y_pos=0.7,
        )
        wan_cells = VGroup(*[cells[i] for i in range(1, 5)])
        self.play(Indicate(wan_cells, color=COLOR_WAN, scale_factor=1.1), run_time=0.6)
        self.play(FadeIn(box2), FadeIn(lbl2), run_time=0.5)

        wan_fill_digits = ["0", "0", "5", "0"]
        f_wan = VGroup()
        for i, d in enumerate(wan_fill_digits):
            lbl = Text(d, font=FONT, font_size=26,
                       color=COLOR_WAN if d != "0" else COLOR_ZERO)
            lbl.move_to(dlabels[i + 1].get_center())
            f_wan.add(lbl)
        self.play(
            FadeOut(VGroup(*[dlabels[i] for i in range(1, 5)])),
            FadeIn(f_wan),
            run_time=0.5,
        )
        self.wait(0.3)

        # Step 3: 个级 — 全无 → 0000
        box3, lbl3 = self._step_box(
            [("个级: 全无", COLOR_GE), ("→", GRAY_A), ("0000", COLOR_ZERO)],
            COLOR_GE, y_pos=-0.6,
        )
        ge_cells = VGroup(*[cells[i] for i in range(5, 9)])
        self.play(Indicate(ge_cells, color=COLOR_GE, scale_factor=1.1), run_time=0.6)
        self.play(FadeIn(box3), FadeIn(lbl3), run_time=0.5)

        f_ge = VGroup()
        for i in range(5, 9):
            lbl = Text("0", font=FONT, font_size=26, color=COLOR_ZERO)
            lbl.move_to(dlabels[i].get_center())
            f_ge.add(lbl)
        self.play(
            FadeOut(VGroup(*[dlabels[i] for i in range(5, 9)])),
            FadeIn(f_ge),
            run_time=0.5,
        )
        self.wait(0.4)

        # 答案框
        ans_box = RoundedRectangle(
            width=7.5, height=1.6, corner_radius=0.3,
            color=COLOR_HL, stroke_width=2, fill_opacity=0.1,
        ).move_to(DOWN * 2.1)
        ans_row = VGroup(
            Text("写作:", font=FONT, font_size=22, color=GRAY_A),
            Text("305000000", font=FONT, font_size=40, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.1)

        self.play(FadeIn(ans_box), Write(ans_row), run_time=0.7)
        self.play(Indicate(ans_row[1], color=COLOR_HL, scale_factor=1.08), run_time=0.6)

        group_hint = Text("= 3  0500  0000", font=FONT, font_size=26, color=COLOR_DIGIT)
        group_hint.move_to(DOWN * 3.3)
        self.play(FadeIn(group_hint), run_time=0.4)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(question),
            FadeOut(cells), FadeOut(dlabels), FadeOut(braces),
            FadeOut(f_yi), FadeOut(f_wan), FadeOut(f_ge),
            FadeOut(box1), FadeOut(lbl1),
            FadeOut(box2), FadeOut(lbl2),
            FadeOut(box3), FadeOut(lbl3),
            FadeOut(ans_box), FadeOut(ans_row),
            FadeOut(group_hint),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 7: 易错提示 — 连续 0 的占位
    # ------------------------------------------------------------------

    def scene_7_pitfall(self):
        title = Text("易错提示", font=FONT, font_size=36, color="#f97316").move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        warn = Text("注意: 中间的每个 0 都要写!", font=FONT, font_size=28, color=COLOR_ZERO)
        warn.move_to(UP * 4.5)
        self.play(FadeIn(warn, shift=UP * 0.2), run_time=0.5)

        # 例: 三亿零五百 → 300000500
        # 亿=3, 千万=0, 百万=0, 十万=0, 万=0, 千=5, 百=0, 十=0, 个=0
        # 汉字: 三亿零五百
        ex_ch = Text("三亿零五百", font=FONT, font_size=34, color=COLOR_DIGIT)
        ex_ch.move_to(UP * 3.5)
        self.play(FadeIn(ex_ch), run_time=0.4)

        # 数位表
        place_names  = ["亿", "千万", "百万", "十万", "万", "千", "百", "十", "个"]
        place_colors = [COLOR_YI] + [COLOR_WAN]*4 + [COLOR_GE]*4
        digits_p     = ["3", "0", "0", "0", "0", "5", "0", "0", "0"]

        cells, dlabels, col_xs = self._build_place_table(
            place_names, place_colors, digits_p,
            cell_w=0.78, cell_h=0.55,
            table_center_y=2.3,
            place_font=13, digit_font=26,
        )
        brace_y = 2.3 + 0.55 * 0.9
        braces = self._build_level_braces(
            col_xs, brace_y, 0.78,
            [("亿级", COLOR_YI, 0, 0), ("万级", COLOR_WAN, 1, 4), ("个级", COLOR_GE, 5, 8)],
        )
        self.play(FadeIn(cells), FadeIn(dlabels), FadeIn(braces), run_time=0.7)

        # 高亮中间的 0
        mid_zeros = VGroup(*[dlabels[i] for i in [1, 2, 3, 4, 6, 7, 8]])
        self.play(Indicate(mid_zeros, color=COLOR_ZERO, scale_factor=1.45), run_time=0.9)

        # 错误 vs 正确
        wrong_row = VGroup(
            Text("错误:", font=FONT, font_size=22, color="#ef4444"),
            Text("35", font=FONT, font_size=32, color="#ef4444"),
            Cross(Text("35", font=FONT, font_size=32)).set_color("#ef4444"),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.3)
        # 简化: 直接文字
        wrong_lbl = VGroup(
            Text("错误: 漏写中间 0 → ", font=FONT, font_size=22, color="#ef4444"),
            Text("35 (错!)", font=FONT, font_size=28, color="#ef4444"),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 0.5)

        right_lbl = VGroup(
            Text("正确: 每 0 都写 → ", font=FONT, font_size=22, color=COLOR_GE),
            Text("300000500", font=FONT, font_size=28, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.5)

        self.play(FadeIn(wrong_lbl, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(right_lbl, shift=RIGHT * 0.3), run_time=0.5)

        remind = Text(
            "口诀: 该位没有就写 0, 一个都不能少!",
            font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(DOWN * 2.8)
        self.play(FadeIn(remind, shift=UP * 0.2), run_time=0.5)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(warn), FadeOut(ex_ch),
            FadeOut(cells), FadeOut(dlabels), FadeOut(braces),
            FadeOut(wrong_lbl), FadeOut(right_lbl), FadeOut(remind),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 8: 知识总结
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        title = Text("知识总结", font=FONT, font_size=36, color=COLOR_HL).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        card_bg = RoundedRectangle(
            width=7.8, height=10.0, corner_radius=0.35,
            color=WHITE, stroke_width=2,
            fill_color=WHITE, fill_opacity=0.04,
        ).move_to(UP * 0.2)
        self.play(FadeIn(card_bg), run_time=0.4)

        # 写法规则
        r1_title = Text("① 从高位写起", font=FONT, font_size=28, color=COLOR_TITLE)
        r1_body  = Text("先亿级 → 再万级 → 最后个级", font=FONT, font_size=21, color=GRAY_A)
        rule1 = VGroup(r1_title, r1_body).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        rule1.move_to(UP * 3.8 + LEFT * 0.2)

        r2_title = Text("② 0 占位", font=FONT, font_size=28, color=COLOR_ZERO)
        r2_body  = Text("该位没有单位 → 写 0 占位", font=FONT, font_size=21, color=GRAY_A)
        r2_body2 = Text("每个缺的位都要写 0, 一个不能少", font=FONT, font_size=21, color=GRAY_A)
        rule2 = VGroup(r2_title, r2_body, r2_body2).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        rule2.move_to(UP * 2.3 + LEFT * 0.2)

        self.play(FadeIn(rule1, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(rule2, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.4)

        # 分割线
        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1)
        divider.move_to(UP * 0.9)
        self.play(Create(divider), run_time=0.4)

        # 例题回顾
        ex_title = Text("例题回顾", font=FONT, font_size=22, color=GRAY_A).move_to(UP * 0.3)

        ex1 = VGroup(
            Text("二千五百万", font=FONT, font_size=24, color=COLOR_WAN),
            Text("→", font=FONT, font_size=22, color=GRAY_A),
            Text("25000000", font=FONT, font_size=28, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.6)

        ex2 = VGroup(
            Text("三亿零五十万", font=FONT, font_size=24, color=COLOR_YI),
            Text("→", font=FONT, font_size=22, color=GRAY_A),
            Text("305000000", font=FONT, font_size=28, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.6)

        self.play(FadeIn(ex_title), run_time=0.4)
        self.play(FadeIn(ex1, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(ex2, shift=RIGHT * 0.2), run_time=0.5)

        # 口诀
        divider2 = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1)
        divider2.move_to(DOWN * 2.5)
        self.play(Create(divider2), run_time=0.3)

        mnemonic = VGroup(
            Text("口诀", font=FONT, font_size=22, color=COLOR_HL),
            Text("高位起, 级级写;", font=FONT, font_size=22, color=WHITE),
            Text("位上没有写个 0!", font=FONT, font_size=22, color=COLOR_ZERO),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        mnemonic.move_to(DOWN * 3.7)

        self.play(FadeIn(mnemonic, shift=UP * 0.2), run_time=0.6)

        cheer = Text(
            "掌握规则, 再大的数也会写!",
            font=FONT, font_size=22, color=COLOR_GE,
        ).move_to(DOWN * 5.3)
        self.play(FadeIn(cheer, shift=UP * 0.2), run_time=0.5)

        self.wait(3.0)

        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(rule1), FadeOut(rule2),
            FadeOut(divider), FadeOut(ex_title),
            FadeOut(ex1), FadeOut(ex2),
            FadeOut(divider2), FadeOut(mnemonic), FadeOut(cheer),
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

        # 装饰数字
        deco_items = ["亿", "万", "0", "25", "305"]
        deco_positions = [
            UP * 3.5 + LEFT * 2.5,
            UP * 3.5 + RIGHT * 2.5,
            DOWN * 3.0 + LEFT * 2.0,
            DOWN * 3.0 + RIGHT * 2.0,
            DOWN * 3.0,
        ]
        deco_colors = [COLOR_YI, COLOR_WAN, COLOR_ZERO, COLOR_GE, COLOR_HL]
        decorations = VGroup()
        for txt, pos, col in zip(deco_items, deco_positions, deco_colors):
            dec = Text(txt, font=FONT, font_size=40, color=col)
            dec.set_opacity(0.55)
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
# manim -qm 003_大数的写法.py LargeNumberWriteLesson   # 中等质量 720p
# manim -qh 003_大数的写法.py LargeNumberWriteLesson   # 高质量 1080p
