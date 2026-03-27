"""
004_小数的大小比较.py — 小数的大小比较 教学动画

知识点: 先比较整数部分，整数部分大的数就大；
        如果整数部分相同，再依次比较十分位、百分位……
        哪一位上的数大，这个小数就大。
年级: 四年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

场景:
  1. 开场钩子
  2. 比较规则说明
  3. 示例1 — 整数部分不同（3.14 vs 4.5）
  4. 示例2 — 整数相同，比十分位（3.14 vs 3.2）
  5. 示例3 — 多位比较（0.356 vs 0.359）
  6. 数轴直觉展示
  7. 规律总结
  8. 片尾
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
COLOR_HL     = "#fbbf24"   # 黄色高亮
COLOR_GT     = "#22c55e"   # 绿色 — 较大的数
COLOR_LT     = "#ef4444"   # 红色 — 较小的数
COLOR_DOT    = "#f59e0b"   # 橙色 — 小数点
COLOR_STEP   = "#60a5fa"   # 蓝色 — 步骤
COLOR_RULE   = "#a78bfa"   # 紫色 — 规律
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


# ======================================================================
# 辅助函数
# ======================================================================

def make_decimal_chars(number_str: str, dot_color=COLOR_DOT,
                       digit_color=WHITE, font_size=52,
                       highlight_index=None, highlight_color=COLOR_HL):
    """
    将数字字符串拆成单个字符，返回 VGroup（方便逐位高亮）。
    highlight_index: 整数索引，对应 number_str 中某位置的字符高亮。
    """
    chars = []
    for i, ch in enumerate(number_str):
        if ch == ".":
            color = dot_color
        elif highlight_index is not None and i == highlight_index:
            color = highlight_color
        else:
            color = digit_color
        t = Text(ch, font=FONT, font_size=font_size, color=color, weight=BOLD)
        chars.append(t)
    group = VGroup(*chars).arrange(RIGHT, buff=0.04)
    return group


def make_place_value_table(number_str: str, y_center=0.0, x_center=0.0,
                           cell_w=1.0, font_size=28):
    """
    为给定小数字符串生成数位表 (VGroup)。
    返回 (table_group, header_group, value_group) 三个 VGroup。
    """
    # 解析整数部分与小数部分
    if "." in number_str:
        int_part, dec_part = number_str.split(".")
    else:
        int_part, dec_part = number_str, ""

    # 根据数位决定列标题
    int_len = len(int_part)
    dec_len = len(dec_part)

    unit_names_int = ["千位", "百位", "十位", "个位"]
    unit_names_dec = ["十分位", "百分位", "千分位"]

    headers = unit_names_int[-int_len:] + unit_names_dec[:dec_len]
    values  = list(int_part) + list(dec_part)

    cols = len(headers)
    total_w = cols * cell_w + 0.1
    x_start = x_center - total_w / 2 + cell_w / 2

    header_mobs = VGroup()
    value_mobs  = VGroup()
    line_mobs   = VGroup()

    for i, (h, v) in enumerate(zip(headers, values)):
        x = x_start + i * cell_w
        h_txt = Text(h, font=FONT, font_size=font_size - 6, color=GRAY_A).move_to(
            [x, y_center + 0.4, 0]
        )
        v_txt = Text(v, font=FONT, font_size=font_size + 4, color=WHITE, weight=BOLD).move_to(
            [x, y_center - 0.3, 0]
        )
        header_mobs.add(h_txt)
        value_mobs.add(v_txt)

    # 分隔线
    sep_line = Line(
        [x_center - total_w / 2, y_center + 0.05, 0],
        [x_center + total_w / 2, y_center + 0.05, 0],
        color=GRAY_B, stroke_width=1.5
    )
    line_mobs.add(sep_line)

    # 小数点竖线
    if "." in number_str:
        dot_x = x_start + (int_len - 0.5) * cell_w
        dot_line = DashedLine(
            [dot_x, y_center + 0.65, 0],
            [dot_x, y_center - 0.65, 0],
            color=COLOR_DOT, stroke_width=1.5, dash_length=0.08
        )
        line_mobs.add(dot_line)

    table_group = VGroup(header_mobs, value_mobs, line_mobs)
    return table_group, header_mobs, value_mobs


# ======================================================================
# 主场景
# ======================================================================

class DecimalCompareLesson(Scene):
    """
    小数的大小比较 教学动画
    场景:
      1. 开场钩子
      2. 比较规则
      3. 示例1 — 整数部分不同
      4. 示例2 — 整数相同比十分位 (3.14 vs 3.2)
      5. 示例3 — 多位比较 (0.356 vs 0.359)
      6. 数轴直觉
      7. 规律总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_rules()
        self.scene_3_example_int_diff()
        self.scene_4_example_same_int()
        self.scene_5_example_deep()
        self.scene_6_number_line()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "3.14 和 3.2 哪个大？",
            font=FONT, font_size=44, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(Write(hook), run_time=0.7)

        # 显示两个数
        num_a = make_decimal_chars("3.14", font_size=72).move_to(UP * 3.5 + LEFT * 2.0)
        vs    = Text("vs", font=FONT, font_size=36, color=GRAY_A).move_to(UP * 3.5)
        num_b = make_decimal_chars("3.2",  font_size=72).move_to(UP * 3.5 + RIGHT * 2.2)

        self.play(FadeIn(num_a, scale=0.8), run_time=0.5)
        self.play(FadeIn(vs),               run_time=0.3)
        self.play(FadeIn(num_b, scale=0.8), run_time=0.5)
        self.wait(0.5)

        # 表情引发思考
        think = Text(
            "很多同学以为 3.14 更大\n（因为 14 > 2）",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 1.2)
        self.play(FadeIn(think, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        wrong_mark = Text("✗ 错！", font=FONT, font_size=40, color=COLOR_LT).move_to(DOWN * 0.3)
        self.play(FadeIn(wrong_mark, scale=1.2), run_time=0.5)
        self.wait(0.5)

        correct = Text(
            "其实 3.14 < 3.2",
            font=FONT, font_size=36, color=COLOR_GT
        ).move_to(DOWN * 1.3)
        self.play(Write(correct), run_time=0.6)
        self.wait(1.0)

        explain_hint = Text(
            "为什么？学完就懂了！",
            font=FONT, font_size=28, color=COLOR_STEP
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(explain_hint, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(VGroup(hook, num_a, vs, num_b, think, wrong_mark, correct, explain_hint)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 2: 比较规则
    # ------------------------------------------------------------------

    def scene_2_rules(self):
        title = Text(
            "比较规则", font=FONT, font_size=40, color=COLOR_RULE, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 规则步骤
        rules = [
            ("第一步", "比较整数部分",        "整数部分大的数更大"),
            ("第二步", "整数相同，比十分位",  "十分位上数字大的更大"),
            ("第三步", "仍然相同，比百分位",  "依次往后比……"),
        ]

        rule_mobs = VGroup()
        y_positions = [3.8, 2.2, 0.6]
        for (step, rule, desc), y in zip(rules, y_positions):
            step_txt = Text(step, font=FONT, font_size=24, color=COLOR_STEP, weight=BOLD)
            rule_txt = Text(rule, font=FONT, font_size=26, color=WHITE)
            desc_txt = Text(desc, font=FONT, font_size=20, color=GRAY_A)

            row = VGroup(step_txt, rule_txt).arrange(RIGHT, buff=0.3)
            block = VGroup(row, desc_txt).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
            block.move_to(UP * y + LEFT * 0.5)

            # 序号圆圈
            circ = Circle(radius=0.28, color=COLOR_STEP, fill_color=COLOR_STEP,
                          fill_opacity=1, stroke_width=0)
            num_lbl = Text(str(rules.index((step, rule, desc)) + 1),
                           font=FONT, font_size=20, color=BG_COLOR, weight=BOLD)
            num_lbl.move_to(circ.get_center())
            bullet = VGroup(circ, num_lbl).move_to(UP * y + LEFT * 3.8)

            group = VGroup(bullet, block)
            rule_mobs.add(group)

            self.play(FadeIn(bullet, scale=0.5), FadeIn(block, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        # 关键提示
        key_bg = RoundedRectangle(
            width=7.5, height=1.4,
            corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=2
        ).move_to(DOWN * 1.6)
        key_txt = Text(
            "从高位开始，逐位比较，\n先分出大小就停下！",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(key_bg.get_center())
        self.play(FadeIn(key_bg), Write(key_txt), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, rule_mobs, key_bg, key_txt)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 示例1 — 整数部分不同（3.5 vs 4.2）
    # ------------------------------------------------------------------

    def scene_3_example_int_diff(self):
        title = Text(
            "情况1：整数部分不同", font=FONT, font_size=34,
            color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 展示两个数
        label_a = Text("甲：", font=FONT, font_size=28, color=GRAY_A).move_to(UP * 4.4 + LEFT * 3.2)
        num_a   = make_decimal_chars("3.5", font_size=56).next_to(label_a, RIGHT, buff=0.2)
        label_b = Text("乙：", font=FONT, font_size=28, color=GRAY_A).move_to(UP * 3.2 + LEFT * 3.2)
        num_b   = make_decimal_chars("4.2", font_size=56).next_to(label_b, RIGHT, buff=0.2)

        self.play(FadeIn(label_a), FadeIn(num_a), run_time=0.5)
        self.play(FadeIn(label_b), FadeIn(num_b), run_time=0.5)
        self.wait(0.4)

        # 步骤1: 看整数部分
        step1 = Text(
            "第一步：比整数部分", font=FONT, font_size=28, color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 1.8)
        self.play(FadeIn(step1, shift=UP * 0.2), run_time=0.4)

        # 高亮整数位
        int_box_a = SurroundingRectangle(num_a[0], color=COLOR_HL, buff=0.1, stroke_width=3)
        int_box_b = SurroundingRectangle(num_b[0], color=COLOR_HL, buff=0.1, stroke_width=3)
        self.play(Create(int_box_a), Create(int_box_b), run_time=0.5)

        int_cmp = Text(
            "3 < 4", font=FONT, font_size=32, color=COLOR_HL
        ).move_to(UP * 0.6)
        self.play(FadeIn(int_cmp, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # 结论
        concl_bg = RoundedRectangle(
            width=6.5, height=1.2, corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_GT, stroke_width=2
        ).move_to(DOWN * 0.8)
        concl_txt = VGroup(
            Text("整数部分 3 < 4", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"\Rightarrow", font_size=28, color=COLOR_GT),
            Text("3.5 < 4.2", font=FONT, font_size=28, color=COLOR_GT, weight=BOLD)
        ).arrange(RIGHT, buff=0.2).move_to(concl_bg.get_center())
        self.play(FadeIn(concl_bg), FadeIn(concl_txt), run_time=0.5)

        # 不需要看小数位
        note = Text(
            "整数部分已分出大小，不需要再看小数位！",
            font=FONT, font_size=20, color=COLOR_HL
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, label_a, num_a, label_b, num_b,
                step1, int_box_a, int_box_b, int_cmp,
                concl_bg, concl_txt, note
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 示例2 — 整数相同比十分位（3.14 vs 3.2）
    # ------------------------------------------------------------------

    def scene_4_example_same_int(self):
        title = Text(
            "情况2：整数相同，比十分位",
            font=FONT, font_size=30, color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 回到钩子问题
        subtitle = Text(
            "回到开场问题：3.14 vs 3.2",
            font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 5.0)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 数位表
        table_a, hdr_a, val_a = make_place_value_table(
            "3.14", y_center=3.2, x_center=-0.3, cell_w=1.15, font_size=26
        )
        table_b, hdr_b, val_b = make_place_value_table(
            "3.20", y_center=1.2, x_center=-0.3, cell_w=1.15, font_size=26
        )

        label_a = Text("3.14", font=FONT, font_size=32, color=WHITE, weight=BOLD).move_to(UP * 3.8 + LEFT * 3.5)
        label_b = Text("3.20", font=FONT, font_size=32, color=WHITE, weight=BOLD).move_to(UP * 1.8 + LEFT * 3.5)

        # 3.20 注释
        note_eq = Text("(3.2 = 3.20)", font=FONT, font_size=18, color=GRAY_A).next_to(label_b, RIGHT, buff=0.2)

        self.play(
            FadeIn(label_a), FadeIn(table_a),
            FadeIn(label_b), FadeIn(table_b), FadeIn(note_eq),
            run_time=0.6
        )
        self.wait(0.5)

        # 步骤1: 整数位
        step1 = Text("第一步：比个位", font=FONT, font_size=26, color=COLOR_STEP, weight=BOLD
                     ).move_to(DOWN * 0.2)
        self.play(FadeIn(step1), run_time=0.4)

        # 高亮个位（索引0: 个位）
        box_int_a = SurroundingRectangle(val_a[0], color=COLOR_HL, buff=0.1, stroke_width=3)
        box_int_b = SurroundingRectangle(val_b[0], color=COLOR_HL, buff=0.1, stroke_width=3)
        self.play(Create(box_int_a), Create(box_int_b), run_time=0.5)

        same_int = Text("个位: 3 = 3，相同！", font=FONT, font_size=24, color=COLOR_HL
                        ).move_to(DOWN * 1.0)
        self.play(FadeIn(same_int), run_time=0.4)
        self.wait(0.5)

        # 步骤2: 十分位
        step2 = Text("第二步：比十分位", font=FONT, font_size=26, color=COLOR_STEP, weight=BOLD
                     ).move_to(DOWN * 2.0)
        self.play(
            FadeOut(VGroup(box_int_a, box_int_b, same_int)),
            FadeIn(step2),
            run_time=0.4
        )

        # 十分位高亮（索引1）
        box_dec_a = SurroundingRectangle(val_a[1], color=COLOR_HL, buff=0.1, stroke_width=3)
        box_dec_b = SurroundingRectangle(val_b[1], color=COLOR_HL, buff=0.1, stroke_width=3)
        self.play(Create(box_dec_a), Create(box_dec_b), run_time=0.5)

        dec_cmp = VGroup(
            Text("十分位：1 < 2", font=FONT, font_size=26, color=COLOR_HL),
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(dec_cmp), run_time=0.4)
        self.wait(0.5)

        # 结论
        concl_bg = RoundedRectangle(
            width=7.0, height=1.4, corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_GT, stroke_width=2
        ).move_to(DOWN * 4.5)
        concl_row = VGroup(
            Text("十分位 1 < 2", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"\Rightarrow", font_size=28, color=COLOR_GT),
            Text("3.14 < 3.2", font=FONT, font_size=30, color=COLOR_GT, weight=BOLD)
        ).arrange(RIGHT, buff=0.2).move_to(concl_bg.get_center())
        self.play(FadeIn(concl_bg), FadeIn(concl_row), run_time=0.5)
        self.wait(1.8)

        self.play(
            FadeOut(VGroup(
                title, subtitle,
                label_a, table_a, label_b, table_b, note_eq,
                step1, step2, box_dec_a, box_dec_b, dec_cmp,
                concl_bg, concl_row
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 示例3 — 多位比较（0.356 vs 0.359）
    # ------------------------------------------------------------------

    def scene_5_example_deep(self):
        title = Text(
            "情况3：需要比到千分位",
            font=FONT, font_size=32, color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 两个数
        num_a_str = "0.356"
        num_b_str = "0.359"

        disp_a = make_decimal_chars(num_a_str, font_size=60).move_to(UP * 4.3 + LEFT * 1.5)
        disp_b = make_decimal_chars(num_b_str, font_size=60).move_to(UP * 2.9 + LEFT * 1.5)

        la = Text("甲：", font=FONT, font_size=28, color=GRAY_A).next_to(disp_a, LEFT, buff=0.3)
        lb = Text("乙：", font=FONT, font_size=28, color=GRAY_A).next_to(disp_b, LEFT, buff=0.3)

        self.play(FadeIn(la), FadeIn(disp_a), FadeIn(lb), FadeIn(disp_b), run_time=0.6)
        self.wait(0.4)

        # 对齐数位说明
        align_note = Text(
            "小数点对齐，从高位逐位比较：",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(UP * 1.8)
        self.play(FadeIn(align_note), run_time=0.4)

        # 步骤标注
        steps = [
            # (描述, 位置y, 结果, 是否最终)
            ("个位：0 = 0，继续", 0.8, "相同", False),
            ("十分位：3 = 3，继续", -0.2, "相同", False),
            ("百分位：5 = 5，继续", -1.2, "相同", False),
            ("千分位：6 < 9，分出大小！", -2.2, "6 < 9", True),
        ]

        step_mobs = VGroup()
        # indices in "0.356": 0='0' 1='.' 2='3' 3='5' 4='6'
        # indices in "0.359": 0='0' 1='.' 2='3' 3='5' 4='9'
        highlight_pairs = [
            (1, 1),   # 个位: index 0 in both (after dot stripped)
            (2, 2),   # 十分位
            (3, 3),   # 百分位
            (4, 4),   # 千分位
        ]
        colors_step = [GRAY_A, GRAY_A, GRAY_A, COLOR_HL]

        for i, ((desc, y, result, is_final), (idx_a, idx_b)) in enumerate(
                zip(steps, highlight_pairs)):
            # 高亮对应字符
            c = COLOR_HL if is_final else GRAY_B
            box_a = SurroundingRectangle(disp_a[idx_a], color=c, buff=0.08, stroke_width=2.5)
            box_b = SurroundingRectangle(disp_b[idx_b], color=c, buff=0.08, stroke_width=2.5)
            step_txt = Text(desc, font=FONT, font_size=22,
                            color=COLOR_HL if is_final else GRAY_A).move_to(UP * y + LEFT * 0.3)
            self.play(Create(box_a), Create(box_b), FadeIn(step_txt), run_time=0.4)
            if is_final:
                self.wait(0.6)
            else:
                self.wait(0.3)
            step_mobs.add(box_a, box_b, step_txt)

        # 结论
        concl_bg = RoundedRectangle(
            width=7.0, height=1.4, corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_GT, stroke_width=2
        ).move_to(DOWN * 3.5)
        concl_row = VGroup(
            Text("千分位 6 < 9", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"\Rightarrow", font_size=28, color=COLOR_GT),
            Text("0.356 < 0.359", font=FONT, font_size=28, color=COLOR_GT, weight=BOLD)
        ).arrange(RIGHT, buff=0.2).move_to(concl_bg.get_center())
        self.play(FadeIn(concl_bg), FadeIn(concl_row), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                title, la, disp_a, lb, disp_b, align_note, step_mobs, concl_bg, concl_row
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 数轴直觉
    # ------------------------------------------------------------------

    def scene_6_number_line(self):
        title = Text(
            "用数轴感受大小", font=FONT, font_size=36, color=COLOR_RULE, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        subtitle = Text(
            "数轴上越靠右，数越大",
            font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 4.9)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 数轴
        nl = NumberLine(
            x_range=[2.8, 3.6, 0.2],
            length=7.5,
            include_numbers=False,
            include_tip=True,
            color=WHITE,
            stroke_width=2,
        ).move_to(UP * 3.0)

        self.play(Create(nl), run_time=0.8)

        # 手动标注刻度标签
        tick_vals = [2.8, 3.0, 3.2, 3.4, 3.6]
        tick_labels = VGroup()
        for v in tick_vals:
            lbl = Text(f"{v:.1f}", font=FONT, font_size=20, color=GRAY_A)
            lbl.move_to(nl.n2p(v) + DOWN * 0.45)
            tick_labels.add(lbl)
        self.play(FadeIn(tick_labels), run_time=0.4)

        # 标注 3.14 和 3.2
        pos_314 = nl.n2p(3.14)
        pos_32  = nl.n2p(3.2)

        dot_314 = Dot(pos_314, radius=0.12, color=COLOR_LT)
        dot_32  = Dot(pos_32,  radius=0.12, color=COLOR_GT)

        lbl_314 = Text("3.14", font=FONT, font_size=24, color=COLOR_LT, weight=BOLD)
        lbl_314.move_to(pos_314 + UP * 0.6)
        arr_314 = Arrow(lbl_314.get_bottom(), pos_314 + UP * 0.12,
                        buff=0.05, color=COLOR_LT, stroke_width=2,
                        max_tip_length_to_length_ratio=0.25)

        lbl_32 = Text("3.2", font=FONT, font_size=24, color=COLOR_GT, weight=BOLD)
        lbl_32.move_to(pos_32 + DOWN * 0.7)
        arr_32 = Arrow(lbl_32.get_top(), pos_32 + DOWN * 0.12,
                       buff=0.05, color=COLOR_GT, stroke_width=2,
                       max_tip_length_to_length_ratio=0.25)

        self.play(FadeIn(dot_314, scale=0.5), FadeIn(lbl_314), Create(arr_314), run_time=0.5)
        self.play(FadeIn(dot_32,  scale=0.5), FadeIn(lbl_32),  Create(arr_32),  run_time=0.5)
        self.wait(0.4)

        # 比较箭头
        cmp_arrow = Arrow(
            pos_314, pos_32,
            buff=0.15, color=COLOR_HL, stroke_width=3,
            max_tip_length_to_length_ratio=0.2
        ).shift(UP * 0.25)
        cmp_lbl = Text("3.14 在左边 → 更小", font=FONT, font_size=22, color=COLOR_HL).move_to(
            UP * 1.8
        )
        self.play(Create(cmp_arrow), run_time=0.5)
        self.play(FadeIn(cmp_lbl), run_time=0.4)
        self.wait(0.5)

        # 结论
        concl = Text(
            "3.14 < 3.2",
            font=FONT, font_size=40, color=COLOR_GT, weight=BOLD
        ).move_to(UP * 0.8)
        self.play(FadeIn(concl, scale=1.1), run_time=0.5)
        self.wait(1.5)

        # 再标一个示例 0.356 vs 0.359（用更精细数轴）
        self.play(
            FadeOut(VGroup(
                nl, tick_labels, dot_314, dot_32,
                lbl_314, arr_314, lbl_32, arr_32,
                cmp_arrow, cmp_lbl, concl, subtitle
            )),
            run_time=0.4
        )

        subtitle2 = Text(
            "0.356 与 0.359 的位置：", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.9)
        self.play(FadeIn(subtitle2), run_time=0.3)

        nl2 = NumberLine(
            x_range=[0.35, 0.36, 0.002],
            length=7.5,
            include_numbers=False,
            include_tip=True,
            color=WHITE,
            stroke_width=2,
        ).move_to(UP * 3.0)
        self.play(Create(nl2), run_time=0.6)

        tick_vals2 = [0.350, 0.352, 0.354, 0.356, 0.358, 0.360]
        tick_labels2 = VGroup()
        for v in tick_vals2:
            lbl = Text(f"{v:.3f}", font=FONT, font_size=17, color=GRAY_A)
            lbl.move_to(nl2.n2p(v) + DOWN * 0.5)
            tick_labels2.add(lbl)
        self.play(FadeIn(tick_labels2), run_time=0.4)

        pos_a = nl2.n2p(0.356)
        pos_b = nl2.n2p(0.359)

        dot_a = Dot(pos_a, radius=0.12, color=COLOR_LT)
        dot_b = Dot(pos_b, radius=0.12, color=COLOR_GT)

        lbl_a = Text("0.356", font=FONT, font_size=22, color=COLOR_LT, weight=BOLD)
        lbl_a.move_to(pos_a + UP * 0.65)
        lbl_b = Text("0.359", font=FONT, font_size=22, color=COLOR_GT, weight=BOLD)
        lbl_b.move_to(pos_b + DOWN * 0.75)

        self.play(FadeIn(dot_a, scale=0.5), FadeIn(lbl_a), run_time=0.4)
        self.play(FadeIn(dot_b, scale=0.5), FadeIn(lbl_b), run_time=0.4)

        concl2 = Text(
            "0.356 < 0.359",
            font=FONT, font_size=38, color=COLOR_GT, weight=BOLD
        ).move_to(UP * 1.0)
        self.play(FadeIn(concl2, scale=1.1), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, subtitle2, nl2, tick_labels2,
                dot_a, dot_b, lbl_a, lbl_b, concl2
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 规律总结
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        sum_title = Text(
            "比较方法总结", font=FONT, font_size=40, color=COLOR_RULE, weight=BOLD
        ).move_to(UP * 5.8)
        self.play(FadeIn(sum_title, shift=DOWN * 0.3), run_time=0.5)

        # 流程图风格展示
        flow_items = [
            ("① 比整数部分",   "整数大的数就更大",           COLOR_STEP),
            ("② 整数相同",      "继续比十分位",               GRAY_A),
            ("③ 十分位相同",    "继续比百分位",               GRAY_A),
            ("④ 依次比较…",    "哪位数字大，这个小数就大",    COLOR_HL),
        ]

        flow_mobs = VGroup()
        y_start = 4.5
        y_step  = 1.35

        for i, (step, desc, col) in enumerate(flow_items):
            y = y_start - i * y_step
            step_t = Text(step, font=FONT, font_size=26, color=col, weight=BOLD)
            desc_t = Text(desc, font=FONT, font_size=22, color=GRAY_A)
            row = VGroup(step_t, desc_t).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
            row.move_to(UP * y + LEFT * 0.3)

            # 连接箭头
            if i > 0:
                prev_y = y_start - (i - 1) * y_step
                arr = Arrow(
                    [0.0, prev_y - 0.55, 0],
                    [0.0, y + 0.45, 0],
                    buff=0, color=GRAY_B, stroke_width=2,
                    max_tip_length_to_length_ratio=0.3
                )
                self.play(Create(arr), run_time=0.3)
                flow_mobs.add(arr)

            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.4)
            flow_mobs.add(row)
            self.wait(0.2)

        # 核心口诀
        rhyme_bg = RoundedRectangle(
            width=7.8, height=2.2, corner_radius=0.25,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_RULE, stroke_width=2.5
        ).move_to(DOWN * 3.8)
        rhyme_lines = VGroup(
            Text("比较小数大小口诀：", font=FONT, font_size=22, color=COLOR_RULE),
            Text("先看整数部分，大的就更大；", font=FONT, font_size=22, color=WHITE),
            Text("整数相同再看小数，", font=FONT, font_size=22, color=WHITE),
            Text("从高位比起，分出大小停！", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(DOWN, buff=0.22).move_to(rhyme_bg.get_center())
        self.play(FadeIn(rhyme_bg), run_time=0.3)
        for line in rhyme_lines:
            self.play(Write(line), run_time=0.45)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(sum_title, flow_mobs, rhyme_bg, rhyme_lines)),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.5)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_A
        ).move_to(UP * 1.5)

        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(UP * 0.3)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰：三个小数比较展示
        dec_pairs = VGroup(
            VGroup(
                Text("1.5", font=FONT, font_size=30, color=COLOR_LT, weight=BOLD),
                Text("<", font=FONT, font_size=30, color=COLOR_HL),
                Text("2.3", font=FONT, font_size=30, color=COLOR_GT, weight=BOLD),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("3.14", font=FONT, font_size=30, color=COLOR_LT, weight=BOLD),
                Text("<", font=FONT, font_size=30, color=COLOR_HL),
                Text("3.2", font=FONT, font_size=30, color=COLOR_GT, weight=BOLD),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("0.356", font=FONT, font_size=30, color=COLOR_LT, weight=BOLD),
                Text("<", font=FONT, font_size=30, color=COLOR_HL),
                Text("0.359", font=FONT, font_size=30, color=COLOR_GT, weight=BOLD),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 1.8)

        for pair in dec_pairs:
            self.play(FadeIn(pair, shift=UP * 0.2), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, dec_pairs)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 004_小数的大小比较.py DecimalCompareLesson
#   中等质量:  manim -qm  004_小数的大小比较.py DecimalCompareLesson
#   高质量:    manim -qh  004_小数的大小比较.py DecimalCompareLesson
# ======================================================================
