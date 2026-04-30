"""
大数的比较与改写 - 四年级数学教学动画
内容: 比较大数大小的方法 + 将整万/整亿数改写成万/亿作单位的数
目标受众: 四年级小学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== 全局配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ===== 颜色配置 =====
COLOR_BG = "#1a1a2e"
COLOR_GOLD = "#f0c040"
COLOR_BLUE = "#4fc3f7"
COLOR_GREEN = "#81c784"
COLOR_RED = "#ef5350"
COLOR_PURPLE = "#ce93d8"
COLOR_ORANGE = "#ffb74d"
COLOR_GRAY = "#90a4ae"
COLOR_WHITE = "#ffffff"
COLOR_HIGHLIGHT = "#ffd54f"
COLOR_CARD_BG = "#16213e"
COLOR_ACCENT = "#0f3460"


class LargeNumberCompareLesson(Scene):
    """
    大数的比较与改写教学动画

    场景顺序:
    1. 开场钩子
    2. 比较方法一: 位数不同时，位数多的数大
    3. 比较方法二: 位数相同时，从最高位比起
    4. 改写成万作单位的数
    5. 改写成亿作单位的数
    6. 综合练习
    7. 片尾关注
    """

    def construct(self):
        self.camera.background_color = COLOR_BG

        # 作者品牌（全程保留）
        self.author_tag = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=COLOR_GRAY,
        ).move_to(UP * 7.0)
        self.add(self.author_tag)

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_compare_by_digits()
        self.scene_3_compare_same_digits()
        self.scene_4_rewrite_wan()
        self.scene_5_rewrite_yi()
        self.scene_6_practice()
        self.scene_7_outro()

    # ─────────────────────────────────────────
    # 辅助方法
    # ─────────────────────────────────────────

    def make_number_card(self, num_str, color=COLOR_BLUE, font_size=36):
        """创建数字卡片（圆角矩形背景 + 数字）"""
        num_text = Text(num_str, font="PingFang SC", font_size=font_size, color=color)
        bg = RoundedRectangle(
            corner_radius=0.2,
            width=num_text.width + 0.5,
            height=num_text.height + 0.3,
            fill_color=COLOR_CARD_BG,
            fill_opacity=1,
            stroke_color=color,
            stroke_width=2,
        )
        return VGroup(bg, num_text)

    def make_digit_boxes(self, num_str, colors=None):
        """
        将数字字符串拆成按位显示的方块组。
        colors: 长度与 num_str 对应的颜色列表，None 则全白。
        """
        boxes = VGroup()
        for i, ch in enumerate(num_str):
            c = colors[i] if colors else COLOR_WHITE
            txt = Text(ch, font="PingFang SC", font_size=32, color=c)
            box = Square(side_length=0.55, fill_color=COLOR_CARD_BG,
                         fill_opacity=1, stroke_color=c, stroke_width=1.5)
            boxes.add(VGroup(box, txt))
        boxes.arrange(RIGHT, buff=0.08)
        return boxes

    def section_title(self, text_str, color=COLOR_GOLD):
        """创建区块小标题"""
        return Text(text_str, font="PingFang SC", font_size=30, color=color)

    def body_text(self, text_str, font_size=24, color=COLOR_WHITE):
        return Text(text_str, font="PingFang SC", font_size=font_size, color=color)

    def highlight_box(self, mob, color=COLOR_HIGHLIGHT, buff=0.15):
        """在 mob 周围画高亮矩形"""
        rect = SurroundingRectangle(mob, color=color, buff=buff, stroke_width=2.5)
        return rect

    # ─────────────────────────────────────────
    # 场景 1: 开场钩子
    # ─────────────────────────────────────────

    def scene_1_opening(self):
        # 主标题
        title_line1 = Text(
            "大数的",
            font="PingFang SC",
            font_size=52,
            color=COLOR_GOLD,
        )
        title_line2 = Text(
            "比较与改写",
            font="PingFang SC",
            font_size=52,
            color=COLOR_GOLD,
        )
        title_group = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.2)
        title_group.move_to(UP * 5.0)

        # 钩子问题
        hook_q = Text(
            "你能比较下面哪个数更大吗？",
            font="PingFang SC",
            font_size=26,
            color=COLOR_WHITE,
        ).move_to(UP * 3.5)

        # 两个大数
        num_a = Text("9980000", font="PingFang SC", font_size=44, color=COLOR_BLUE)
        vs = Text("VS", font="PingFang SC", font_size=32, color=COLOR_GRAY)
        num_b = Text("10000000", font="PingFang SC", font_size=44, color=COLOR_ORANGE)
        nums_group = VGroup(num_a, vs, num_b).arrange(RIGHT, buff=0.5)
        nums_group.move_to(UP * 2.2)

        # 小提示
        hint = Text(
            "学完这节课你就会啦！",
            font="PingFang SC",
            font_size=24,
            color=COLOR_GREEN,
        ).move_to(UP * 0.8)

        # 动画
        self.play(Write(title_group), run_time=1.0)
        self.play(FadeIn(hook_q, shift=UP * 0.3), run_time=0.6)
        self.play(
            FadeIn(num_a, shift=RIGHT * 0.5),
            FadeIn(vs),
            FadeIn(num_b, shift=LEFT * 0.5),
            run_time=0.8,
        )
        self.play(Indicate(num_a, color=COLOR_BLUE, scale_factor=1.1), run_time=0.5)
        self.play(Indicate(num_b, color=COLOR_ORANGE, scale_factor=1.1), run_time=0.5)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(title_group),
            FadeOut(hook_q),
            FadeOut(nums_group),
            FadeOut(hint),
            run_time=0.6,
        )

    # ─────────────────────────────────────────
    # 场景 2: 比较方法一 —— 位数不同
    # ─────────────────────────────────────────

    def scene_2_compare_by_digits(self):
        # ── 标题 ──
        rule_title = Text(
            "比较大小 · 方法一",
            font="PingFang SC",
            font_size=34,
            color=COLOR_GOLD,
        ).move_to(UP * 6.2)

        rule_text = Text(
            "位数不同时，位数多的那个数更大",
            font="PingFang SC",
            font_size=24,
            color=COLOR_WHITE,
        ).move_to(UP * 5.4)

        self.play(Write(rule_title), run_time=0.7)
        self.play(FadeIn(rule_text, shift=DOWN * 0.2), run_time=0.5)

        # ── 示例数字 ──
        n_small = "9980000"   # 7位
        n_large = "10000000"  # 8位

        # 数字文本
        txt_a = Text(n_small, font="PingFang SC", font_size=40, color=COLOR_BLUE)
        txt_b = Text(n_large, font="PingFang SC", font_size=40, color=COLOR_ORANGE)

        txt_a.move_to(UP * 4.0)
        txt_b.move_to(UP * 2.8)

        self.play(FadeIn(txt_a, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(txt_b, shift=RIGHT * 0.3), run_time=0.5)

        # ── 计数位数（Brace 标注）──
        brace_a = Brace(txt_a, direction=DOWN, color=COLOR_BLUE)
        brace_a_lbl = Text("7位", font="PingFang SC", font_size=22, color=COLOR_BLUE)
        brace_a_lbl.next_to(brace_a, DOWN, buff=0.12)

        brace_b = Brace(txt_b, direction=DOWN, color=COLOR_ORANGE)
        brace_b_lbl = Text("8位", font="PingFang SC", font_size=22, color=COLOR_ORANGE)
        brace_b_lbl.next_to(brace_b, DOWN, buff=0.12)

        self.play(
            GrowFromCenter(brace_a), Write(brace_a_lbl), run_time=0.7
        )
        self.play(
            GrowFromCenter(brace_b), Write(brace_b_lbl), run_time=0.7
        )
        self.wait(0.5)

        # ── 结论箭头与符号 ──
        # 8位 > 7位 → 10000000 > 9980000
        arrow = Arrow(
            txt_b.get_right() + RIGHT * 0.1,
            txt_a.get_right() + RIGHT * 0.1,
            buff=0,
            color=COLOR_GREEN,
            stroke_width=3,
        )

        conclusion_line1 = Text(
            "8位 > 7位",
            font="PingFang SC",
            font_size=26,
            color=COLOR_GREEN,
        )
        conclusion_line2 = Text(
            "所以  10000000 > 9980000",
            font="PingFang SC",
            font_size=24,
            color=COLOR_GREEN,
        )
        conclusion = VGroup(conclusion_line1, conclusion_line2).arrange(DOWN, buff=0.2)
        conclusion.move_to(DOWN * 0.5)

        self.play(Create(arrow), run_time=0.6)
        self.play(Write(conclusion), run_time=0.8)
        self.wait(0.8)

        # 高亮最终结论
        rect = self.highlight_box(conclusion, color=COLOR_HIGHLIGHT)
        self.play(Create(rect), run_time=0.4)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(rule_title), FadeOut(rule_text),
            FadeOut(txt_a), FadeOut(txt_b),
            FadeOut(brace_a), FadeOut(brace_a_lbl),
            FadeOut(brace_b), FadeOut(brace_b_lbl),
            FadeOut(arrow), FadeOut(conclusion), FadeOut(rect),
            run_time=0.6,
        )

    # ─────────────────────────────────────────
    # 场景 3: 比较方法二 —— 位数相同时从最高位比
    # ─────────────────────────────────────────

    def scene_3_compare_same_digits(self):
        # ── 标题 ──
        rule_title = Text(
            "比较大小 · 方法二",
            font="PingFang SC",
            font_size=34,
            color=COLOR_GOLD,
        ).move_to(UP * 6.2)

        rule_text = Text(
            "位数相同时，从最高位开始逐位比较",
            font="PingFang SC",
            font_size=23,
            color=COLOR_WHITE,
        ).move_to(UP * 5.4)

        self.play(Write(rule_title), run_time=0.7)
        self.play(FadeIn(rule_text, shift=DOWN * 0.2), run_time=0.5)

        # ── 两个8位数 ──
        na = "31500000"
        nb = "28700000"

        # 逐位显示
        boxes_a = self.make_digit_boxes(na)
        boxes_b = self.make_digit_boxes(nb)

        boxes_a.move_to(UP * 4.2)
        boxes_b.move_to(UP * 3.0)

        # 位标题（亿千百十万千百十个）
        pos_labels_str = ["千", "百", "十", "万", "千", "百", "十", "个"]
        pos_label_group = VGroup()
        for lbl_str in pos_labels_str:
            lbl = Text(lbl_str, font="PingFang SC", font_size=14, color=COLOR_GRAY)
            pos_label_group.add(lbl)
        pos_label_group.arrange(RIGHT, buff=0.18)
        pos_label_group.move_to(UP * 4.85)

        self.play(FadeIn(pos_label_group), run_time=0.4)
        self.play(FadeIn(boxes_a), run_time=0.6)
        self.play(FadeIn(boxes_b), run_time=0.6)
        self.wait(0.3)

        # ── 逐位比较动画 ──
        # 第0位：3 vs 2  → 3 > 2，结论已出
        comparison_results = []
        for i in range(len(na)):
            d_a = int(na[i])
            d_b = int(nb[i])
            if d_a > d_b:
                comparison_results.append(("a_wins", i))
                break
            elif d_b > d_a:
                comparison_results.append(("b_wins", i))
                break
            else:
                comparison_results.append(("equal", i))

        step_texts = []
        for result, idx in comparison_results:
            box_a_i = boxes_a[idx]
            box_b_i = boxes_b[idx]

            # 高亮当前位
            hl_a = SurroundingRectangle(box_a_i, color=COLOR_HIGHLIGHT, buff=0.04, stroke_width=2.5)
            hl_b = SurroundingRectangle(box_b_i, color=COLOR_HIGHLIGHT, buff=0.04, stroke_width=2.5)

            self.play(Create(hl_a), Create(hl_b), run_time=0.4)

            step_note_str = f"最高位: {na[idx]} > {nb[idx]}"
            step_note = Text(
                step_note_str,
                font="PingFang SC",
                font_size=24,
                color=COLOR_GREEN,
            ).move_to(UP * 1.8)
            self.play(Write(step_note), run_time=0.5)
            step_texts.append((hl_a, hl_b, step_note))
            self.wait(0.5)

        # ── 结论 ──
        conclusion_str1 = f"最高位  3 > 2"
        conclusion_str2 = f"所以  31500000 > 28700000"
        c1 = Text(conclusion_str1, font="PingFang SC", font_size=25, color=COLOR_GREEN)
        c2 = Text(conclusion_str2, font="PingFang SC", font_size=23, color=COLOR_GREEN)
        conclusion = VGroup(c1, c2).arrange(DOWN, buff=0.2)
        conclusion.move_to(UP * 0.5)

        self.play(Write(conclusion), run_time=0.8)
        rect = self.highlight_box(conclusion, color=COLOR_HIGHLIGHT)
        self.play(Create(rect), run_time=0.4)
        self.wait(1.5)

        # 补充说明：继续往后比
        note = Text(
            "若最高位相同，则继续比下一位，以此类推",
            font="PingFang SC",
            font_size=21,
            color=COLOR_GRAY,
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 清场
        objs_to_remove = [rule_title, rule_text, boxes_a, boxes_b,
                          pos_label_group, conclusion, rect, note]
        for hl_a, hl_b, sn in step_texts:
            objs_to_remove += [hl_a, hl_b, sn]
        self.play(*[FadeOut(o) for o in objs_to_remove], run_time=0.6)

    # ─────────────────────────────────────────
    # 场景 4: 改写成"万"作单位
    # ─────────────────────────────────────────

    def scene_4_rewrite_wan(self):
        # ── 标题 ──
        sec_title = Text(
            "改写成「万」作单位",
            font="PingFang SC",
            font_size=34,
            color=COLOR_GOLD,
        ).move_to(UP * 6.2)

        key_rule = Text(
            "整万的数 ÷ 10000，再写上「万」字",
            font="PingFang SC",
            font_size=23,
            color=COLOR_WHITE,
        ).move_to(UP * 5.3)

        self.play(Write(sec_title), run_time=0.7)
        self.play(FadeIn(key_rule, shift=DOWN * 0.2), run_time=0.5)

        # ── 例题1: 250000 = 25万 ──
        eg1_label = Text(
            "例1:",
            font="PingFang SC",
            font_size=26,
            color=COLOR_GRAY,
        ).move_to(UP * 4.4 + LEFT * 3.2)

        num1 = Text("250000", font="PingFang SC", font_size=42, color=COLOR_BLUE)
        eq1 = Text("=", font="PingFang SC", font_size=42, color=COLOR_WHITE)
        result1 = Text("25万", font="PingFang SC", font_size=42, color=COLOR_GREEN)
        row1 = VGroup(num1, eq1, result1).arrange(RIGHT, buff=0.4)
        row1.move_to(UP * 3.8)

        self.play(FadeIn(eg1_label), FadeIn(num1), run_time=0.5)

        # 用大括号标注末尾4个0
        # 找到末尾4个0的位置范围
        brace_zeros = Brace(
            VGroup(*[
                Text(c, font="PingFang SC", font_size=42, color=COLOR_BLUE)
                for c in "0000"
            ]).arrange(RIGHT, buff=0.03).move_to(
                num1.get_right() + LEFT * (num1.width * 4 / 6) + DOWN * 0.05
            ),
            direction=DOWN, color=COLOR_RED
        )
        # 简化：用文字说明
        zeros_hint = Text(
            "末尾有4个0，去掉4个0",
            font="PingFang SC",
            font_size=22,
            color=COLOR_RED,
        ).next_to(row1, DOWN, buff=0.35)

        self.play(FadeIn(zeros_hint, shift=DOWN * 0.1), run_time=0.5)
        self.wait(0.3)

        self.play(
            FadeIn(eq1), FadeIn(result1), run_time=0.6
        )
        self.wait(0.4)

        # 验证：Indicate result
        self.play(Indicate(result1, color=COLOR_HIGHLIGHT, scale_factor=1.15), run_time=0.5)

        # ── 例题2: 3680000 = 368万 ──
        eg2_label = Text(
            "例2:",
            font="PingFang SC",
            font_size=26,
            color=COLOR_GRAY,
        ).move_to(UP * 2.5 + LEFT * 3.2)

        num2 = Text("3680000", font="PingFang SC", font_size=40, color=COLOR_BLUE)
        eq2 = Text("=", font="PingFang SC", font_size=40, color=COLOR_WHITE)
        result2 = Text("368万", font="PingFang SC", font_size=40, color=COLOR_GREEN)
        row2 = VGroup(num2, eq2, result2).arrange(RIGHT, buff=0.4)
        row2.move_to(UP * 2.0)

        zeros_hint2 = Text(
            "末尾有4个0，去掉4个0",
            font="PingFang SC",
            font_size=22,
            color=COLOR_RED,
        ).next_to(row2, DOWN, buff=0.3)

        self.play(FadeIn(eg2_label), FadeIn(num2), run_time=0.5)
        self.play(FadeIn(zeros_hint2, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(eq2), FadeIn(result2), run_time=0.5)
        self.play(Indicate(result2, color=COLOR_HIGHLIGHT, scale_factor=1.15), run_time=0.5)
        self.wait(0.5)

        # ── 关键公式总结卡 ──
        formula_bg = RoundedRectangle(
            corner_radius=0.25,
            width=7.5,
            height=1.1,
            fill_color="#0f3460",
            fill_opacity=1,
            stroke_color=COLOR_GOLD,
            stroke_width=2,
        ).move_to(DOWN * 0.6)

        formula_txt_l = Text("整万数", font="PingFang SC", font_size=26, color=COLOR_BLUE)
        formula_arrow_sym = Text("÷ 10000 →", font="PingFang SC", font_size=24, color=COLOR_WHITE)
        formula_txt_r = Text("数字 + 万", font="PingFang SC", font_size=26, color=COLOR_GREEN)
        formula_content = VGroup(formula_txt_l, formula_arrow_sym, formula_txt_r).arrange(RIGHT, buff=0.3)
        formula_content.move_to(formula_bg.get_center())

        self.play(FadeIn(formula_bg), run_time=0.4)
        self.play(Write(formula_content), run_time=0.7)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(sec_title), FadeOut(key_rule),
            FadeOut(eg1_label), FadeOut(row1), FadeOut(zeros_hint),
            FadeOut(eg2_label), FadeOut(row2), FadeOut(zeros_hint2),
            FadeOut(formula_bg), FadeOut(formula_content),
            run_time=0.6,
        )

    # ─────────────────────────────────────────
    # 场景 5: 改写成"亿"作单位
    # ─────────────────────────────────────────

    def scene_5_rewrite_yi(self):
        # ── 标题 ──
        sec_title = Text(
            "改写成「亿」作单位",
            font="PingFang SC",
            font_size=34,
            color=COLOR_GOLD,
        ).move_to(UP * 6.2)

        key_rule = Text(
            "整亿的数 ÷ 100000000，再写上「亿」字",
            font="PingFang SC",
            font_size=22,
            color=COLOR_WHITE,
        ).move_to(UP * 5.3)

        self.play(Write(sec_title), run_time=0.7)
        self.play(FadeIn(key_rule, shift=DOWN * 0.2), run_time=0.5)

        # ── 例题1: 500000000 = 5亿 ──
        eg1_label = Text(
            "例1:",
            font="PingFang SC",
            font_size=26,
            color=COLOR_GRAY,
        ).move_to(UP * 4.4 + LEFT * 3.5)

        num1 = Text("500000000", font="PingFang SC", font_size=36, color=COLOR_PURPLE)
        eq1 = Text("=", font="PingFang SC", font_size=36, color=COLOR_WHITE)
        result1 = Text("5亿", font="PingFang SC", font_size=36, color=COLOR_GREEN)
        row1 = VGroup(num1, eq1, result1).arrange(RIGHT, buff=0.35)
        row1.move_to(UP * 3.7)

        hint1 = Text(
            "末尾有8个0，去掉8个0",
            font="PingFang SC",
            font_size=22,
            color=COLOR_RED,
        ).next_to(row1, DOWN, buff=0.3)

        self.play(FadeIn(eg1_label), FadeIn(num1), run_time=0.5)
        self.play(FadeIn(hint1, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(eq1), FadeIn(result1), run_time=0.5)
        self.play(Indicate(result1, color=COLOR_HIGHLIGHT, scale_factor=1.2), run_time=0.5)

        # ── 例题2: 3000000000 = 30亿 ──
        eg2_label = Text(
            "例2:",
            font="PingFang SC",
            font_size=26,
            color=COLOR_GRAY,
        ).move_to(UP * 2.5 + LEFT * 3.5)

        num2 = Text("3000000000", font="PingFang SC", font_size=33, color=COLOR_PURPLE)
        eq2 = Text("=", font="PingFang SC", font_size=33, color=COLOR_WHITE)
        result2 = Text("30亿", font="PingFang SC", font_size=33, color=COLOR_GREEN)
        row2 = VGroup(num2, eq2, result2).arrange(RIGHT, buff=0.35)
        row2.move_to(UP * 2.0)

        hint2 = Text(
            "末尾有8个0，去掉8个0",
            font="PingFang SC",
            font_size=22,
            color=COLOR_RED,
        ).next_to(row2, DOWN, buff=0.3)

        self.play(FadeIn(eg2_label), FadeIn(num2), run_time=0.5)
        self.play(FadeIn(hint2, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(eq2), FadeIn(result2), run_time=0.5)
        self.play(Indicate(result2, color=COLOR_HIGHLIGHT, scale_factor=1.2), run_time=0.5)
        self.wait(0.5)

        # ── 关键公式总结卡 ──
        formula_bg = RoundedRectangle(
            corner_radius=0.25,
            width=7.5,
            height=1.1,
            fill_color="#0f3460",
            fill_opacity=1,
            stroke_color=COLOR_GOLD,
            stroke_width=2,
        ).move_to(DOWN * 0.8)

        formula_txt_l = Text("整亿数", font="PingFang SC", font_size=26, color=COLOR_PURPLE)
        formula_arrow_sym = Text("÷ 亿 →", font="PingFang SC", font_size=24, color=COLOR_WHITE)
        formula_txt_r = Text("数字 + 亿", font="PingFang SC", font_size=26, color=COLOR_GREEN)
        formula_content = VGroup(formula_txt_l, formula_arrow_sym, formula_txt_r).arrange(RIGHT, buff=0.3)
        formula_content.move_to(formula_bg.get_center())

        self.play(FadeIn(formula_bg), run_time=0.4)
        self.play(Write(formula_content), run_time=0.7)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(sec_title), FadeOut(key_rule),
            FadeOut(eg1_label), FadeOut(row1), FadeOut(hint1),
            FadeOut(eg2_label), FadeOut(row2), FadeOut(hint2),
            FadeOut(formula_bg), FadeOut(formula_content),
            run_time=0.6,
        )

    # ─────────────────────────────────────────
    # 场景 6: 综合练习
    # ─────────────────────────────────────────

    def scene_6_practice(self):
        # ── 标题 ──
        prac_title = Text(
            "综合练习",
            font="PingFang SC",
            font_size=38,
            color=COLOR_GOLD,
        ).move_to(UP * 6.2)

        self.play(Write(prac_title), run_time=0.6)

        # ── 练习 A: 比较大小填 > 或 < ──
        a_title = Text(
            "① 比一比，填 > 或 <",
            font="PingFang SC",
            font_size=26,
            color=COLOR_BLUE,
        ).move_to(UP * 5.2)
        self.play(FadeIn(a_title), run_time=0.4)

        # A1: 9000000  _  10000000
        q1_a = Text("9000000", font="PingFang SC", font_size=32, color=COLOR_BLUE)
        q1_blank = Text("  ?  ", font="PingFang SC", font_size=32, color=COLOR_GRAY)
        q1_b = Text("10000000", font="PingFang SC", font_size=32, color=COLOR_ORANGE)
        q1 = VGroup(q1_a, q1_blank, q1_b).arrange(RIGHT, buff=0.2)
        q1.move_to(UP * 4.3)

        self.play(FadeIn(q1), run_time=0.4)
        self.wait(0.5)

        # 答案揭示
        ans1 = Text("<", font="PingFang SC", font_size=36, color=COLOR_GREEN)
        ans1.move_to(q1_blank.get_center())
        self.play(Transform(q1_blank, ans1), run_time=0.5)
        reason1 = Text(
            "（7位 < 8位，所以 9000000 < 10000000）",
            font="PingFang SC",
            font_size=19,
            color=COLOR_GRAY,
        ).next_to(q1, DOWN, buff=0.2)
        self.play(FadeIn(reason1), run_time=0.4)
        self.wait(0.6)

        # A2: 56700000  _  56900000
        q2_a = Text("56700000", font="PingFang SC", font_size=30, color=COLOR_BLUE)
        q2_blank = Text("  ?  ", font="PingFang SC", font_size=30, color=COLOR_GRAY)
        q2_b = Text("56900000", font="PingFang SC", font_size=30, color=COLOR_ORANGE)
        q2 = VGroup(q2_a, q2_blank, q2_b).arrange(RIGHT, buff=0.2)
        q2.move_to(UP * 3.0)

        self.play(FadeIn(q2), run_time=0.4)
        self.wait(0.5)

        ans2 = Text("<", font="PingFang SC", font_size=34, color=COLOR_GREEN)
        ans2.move_to(q2_blank.get_center())
        self.play(Transform(q2_blank, ans2), run_time=0.5)
        reason2 = Text(
            "（位数同，千万位同=5，百万位 6 < 9）",
            font="PingFang SC",
            font_size=19,
            color=COLOR_GRAY,
        ).next_to(q2, DOWN, buff=0.2)
        self.play(FadeIn(reason2), run_time=0.4)
        self.wait(0.6)

        # ── 练习 B: 改写 ──
        b_title = Text(
            "② 改写成万或亿作单位",
            font="PingFang SC",
            font_size=26,
            color=COLOR_PURPLE,
        ).move_to(UP * 1.6)
        self.play(FadeIn(b_title), run_time=0.4)

        # B1: 60000000 = ? 万
        b1_q = Text("60000000 =", font="PingFang SC", font_size=30, color=COLOR_BLUE)
        b1_blank = Text("___", font="PingFang SC", font_size=30, color=COLOR_GRAY)
        b1_unit = Text("万", font="PingFang SC", font_size=30, color=COLOR_WHITE)
        b1_row = VGroup(b1_q, b1_blank, b1_unit).arrange(RIGHT, buff=0.2)
        b1_row.move_to(UP * 0.8)

        self.play(FadeIn(b1_row), run_time=0.4)
        self.wait(0.4)
        b1_ans = Text("6000", font="PingFang SC", font_size=30, color=COLOR_GREEN)
        b1_ans.move_to(b1_blank.get_center())
        self.play(Transform(b1_blank, b1_ans), run_time=0.4)
        self.wait(0.5)

        # B2: 2000000000 = ? 亿
        b2_q = Text("2000000000 =", font="PingFang SC", font_size=28, color=COLOR_PURPLE)
        b2_blank = Text("___", font="PingFang SC", font_size=28, color=COLOR_GRAY)
        b2_unit = Text("亿", font="PingFang SC", font_size=28, color=COLOR_WHITE)
        b2_row = VGroup(b2_q, b2_blank, b2_unit).arrange(RIGHT, buff=0.2)
        b2_row.move_to(DOWN * 0.3)

        self.play(FadeIn(b2_row), run_time=0.4)
        self.wait(0.4)
        b2_ans = Text("20", font="PingFang SC", font_size=28, color=COLOR_GREEN)
        b2_ans.move_to(b2_blank.get_center())
        self.play(Transform(b2_blank, b2_ans), run_time=0.4)
        self.wait(0.8)

        # ── 知识总结卡 ──
        summary_bg = RoundedRectangle(
            corner_radius=0.3,
            width=7.8,
            height=2.8,
            fill_color=COLOR_CARD_BG,
            fill_opacity=1,
            stroke_color=COLOR_GOLD,
            stroke_width=2,
        ).move_to(DOWN * 2.3)

        sum_title = Text("记住这两条规则！", font="PingFang SC",
                         font_size=26, color=COLOR_GOLD).move_to(DOWN * 1.4)
        sum_r1 = Text("① 位数多的数更大", font="PingFang SC",
                      font_size=22, color=COLOR_GREEN).move_to(DOWN * 2.0)
        sum_r2 = Text("② 位数同，从最高位逐位比", font="PingFang SC",
                      font_size=22, color=COLOR_GREEN).move_to(DOWN * 2.55)
        sum_r3 = Text("③ 整万整亿数可改写成万/亿作单位", font="PingFang SC",
                      font_size=20, color=COLOR_BLUE).move_to(DOWN * 3.1)

        self.play(FadeIn(summary_bg), run_time=0.4)
        self.play(Write(sum_title), run_time=0.5)
        self.play(FadeIn(sum_r1), FadeIn(sum_r2), FadeIn(sum_r3), run_time=0.7)
        self.wait(2.0)

        # 清场
        self.play(
            FadeOut(prac_title), FadeOut(a_title),
            FadeOut(q1), FadeOut(reason1),
            FadeOut(q2), FadeOut(reason2),
            FadeOut(b_title), FadeOut(b1_row), FadeOut(b2_row),
            FadeOut(summary_bg), FadeOut(sum_title),
            FadeOut(sum_r1), FadeOut(sum_r2), FadeOut(sum_r3),
            run_time=0.6,
        )

    # ─────────────────────────────────────────
    # 场景 7: 片尾关注
    # ─────────────────────────────────────────

    def scene_7_outro(self):
        # 大号作者名
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=COLOR_WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=COLOR_GRAY,
        ).move_to(UP * 0.7)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=COLOR_HIGHLIGHT,
        ).move_to(DOWN * 0.3)

        # 装饰星星
        stars = VGroup()
        for i in range(5):
            angle = i * TAU / 5 - TAU / 4
            pos = np.array([1.8 * np.cos(angle), 1.8 * np.sin(angle), 0])
            star = Star(n=5, outer_radius=0.25, inner_radius=0.12,
                        color=COLOR_GOLD, fill_opacity=0.9)
            star.move_to(follow_text.get_center() + pos + DOWN * 2.0)
            stars.add(star)

        self.play(
            Transform(self.author_tag, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.05), run_time=0.6)
        self.play(
            *[GrowFromCenter(s) for s in stars],
            run_time=0.7,
        )
        self.play(Rotate(stars, angle=TAU / 5, run_time=1.0))
        self.wait(1.5)

        self.play(
            FadeOut(self.author_tag),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(stars),
            run_time=0.8,
        )
