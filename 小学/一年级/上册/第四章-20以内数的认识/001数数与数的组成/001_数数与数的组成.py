"""
数数与数的组成 - Counting and Number Composition
一年级上册 第四章：20以内数的认识

内容: 从1数到20，两个两个数，10个一是1个十，位值制启蒙
目标观众: 一年级小学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CountingNumberComposition(Scene):
    """
    数数与数的组成教学动画

    场景顺序:
    1. 开场 - 引出数数主题
    2. 从1数到20 - 数字逐一出现
    3. 两个两个数 - 偶数序列
    4. 10个一是1个十 - 核心概念
    5. 认识计数器 - 十位和个位
    6. 数的组成示例 - 11, 15
    7. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_ONES = "#3498db"       # 蓝色 - 个位/个
        self.COLOR_TENS = "#e74c3c"       # 红色 - 十位/十
        self.COLOR_HIGHLIGHT = "#f1c40f"  # 黄色 - 高亮
        self.COLOR_GREEN = "#2ecc71"      # 绿色
        self.COLOR_SUBTITLE = "#95a5a6"   # 灰色 - 副标题

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_count_to_20()
        self.scene_3_count_by_twos()
        self.scene_4_ten_ones_make_one_ten()
        self.scene_5_place_value_counter()
        self.scene_6_number_composition()
        self.scene_7_outro()

    # ------------------------------------------------------------------ #
    #  场景 1: 开场
    # ------------------------------------------------------------------ #
    def scene_1_opening(self):
        # 作者信息
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author), run_time=0.4)

        # 章节标签
        chapter = Text(
            "一年级上册 · 第四章",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_SUBTITLE
        ).move_to(UP * 5.8)

        # 主标题
        title = Text(
            "数数与数的组成",
            font="PingFang SC",
            font_size=52,
            color=WHITE
        ).move_to(UP * 4.8)

        # 副标题
        subtitle = Text(
            "20以内数的认识",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 3.9)

        self.play(FadeIn(chapter), run_time=0.4)
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.5)

        # 展示 1~20 的大数字
        nums_row1 = VGroup(*[
            Text(str(n), font="PingFang SC", font_size=38,
                 color=self.COLOR_ONES if n % 2 == 0 else WHITE)
            for n in range(1, 11)
        ]).arrange(RIGHT, buff=0.25).move_to(UP * 2.5)

        nums_row2 = VGroup(*[
            Text(str(n), font="PingFang SC", font_size=38,
                 color=self.COLOR_ONES if n % 2 == 0 else WHITE)
            for n in range(11, 21)
        ]).arrange(RIGHT, buff=0.18).move_to(UP * 1.7)

        self.play(
            LaggedStart(*[FadeIn(n, shift=UP * 0.2) for n in nums_row1],
                        lag_ratio=0.08),
            run_time=1.2
        )
        self.play(
            LaggedStart(*[FadeIn(n, shift=UP * 0.2) for n in nums_row2],
                        lag_ratio=0.08),
            run_time=1.2
        )

        hook = Text(
            "你会从1数到20吗？",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.2)

        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(chapter), FadeOut(title), FadeOut(subtitle),
            FadeOut(nums_row1), FadeOut(nums_row2), FadeOut(hook),
            run_time=0.5
        )

    # ------------------------------------------------------------------ #
    #  场景 2: 从 1 数到 20
    # ------------------------------------------------------------------ #
    def scene_2_count_to_20(self):
        sec_title = Text(
            "从1数到20",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.0)

        self.play(Write(sec_title), run_time=0.6)

        # 4列 × 5行排列20个数字格
        cols, rows = 4, 5
        cell_w, cell_h = 1.7, 1.3
        start_x = -(cols - 1) * cell_w / 2
        start_y = 3.5

        cells = VGroup()
        num_texts = VGroup()

        for i in range(20):
            row = i // cols
            col = i % cols
            x = start_x + col * cell_w
            y = start_y - row * cell_h

            rect = RoundedRectangle(
                width=1.4, height=1.0,
                corner_radius=0.15,
                color="#2c3e50",
                fill_color="#2c3e50",
                fill_opacity=0.8,
                stroke_width=1.5
            ).move_to([x, y, 0])

            if (i + 1) == 10 or (i + 1) == 20:
                txt_color = self.COLOR_HIGHLIGHT
            elif (i + 1) % 2 == 0:
                txt_color = self.COLOR_ONES
            else:
                txt_color = WHITE

            num = Text(
                str(i + 1),
                font="PingFang SC",
                font_size=36,
                color=txt_color
            ).move_to([x, y, 0])

            cells.add(rect)
            num_texts.add(num)

        # 逐个显示
        for i in range(19):
            self.play(
                FadeIn(cells[i]),
                FadeIn(num_texts[i]),
                run_time=0.18
            )
        # 最后一个 20
        self.play(
            FadeIn(cells[19]),
            FadeIn(num_texts[19]),
            run_time=0.35
        )

        self.wait(0.5)

        # 高亮 10
        self.play(
            cells[9].animate.set_stroke(color=self.COLOR_TENS, width=3),
            num_texts[9].animate.scale(1.3),
            run_time=0.5
        )

        ten_label = Text(
            "到了10！满十进一！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_TENS
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(ten_label), run_time=0.4)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(sec_title), FadeOut(cells), FadeOut(num_texts),
            FadeOut(ten_label),
            run_time=0.5
        )

    # ------------------------------------------------------------------ #
    #  场景 3: 两个两个数
    # ------------------------------------------------------------------ #
    def scene_3_count_by_twos(self):
        sec_title = Text(
            "两个两个地数",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.0)

        self.play(Write(sec_title), run_time=0.6)

        hint = Text(
            "2, 4, 6, 8, 10, 12, 14, 16, 18, 20",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_SUBTITLE
        ).move_to(UP * 5.0)
        self.play(FadeIn(hint), run_time=0.4)

        # 10组，每组2个圆点
        dot_radius = 0.22
        dot_gap = 0.58
        group_gap = 1.1
        cols_per_row = 5

        dots_groups = VGroup()
        labels = VGroup()

        for g in range(10):
            row = g // cols_per_row
            col = g % cols_per_row

            gx = -2.8 + col * group_gap
            gy = 3.2 - row * 2.5

            d1 = Circle(
                radius=dot_radius,
                fill_color=self.COLOR_ONES,
                fill_opacity=1,
                stroke_width=0
            ).move_to([gx, gy, 0])
            d2 = Circle(
                radius=dot_radius,
                fill_color=self.COLOR_ONES,
                fill_opacity=1,
                stroke_width=0
            ).move_to([gx + dot_gap, gy, 0])

            brace_line = Line(
                [gx - dot_radius, gy - dot_radius - 0.1, 0],
                [gx + dot_gap + dot_radius, gy - dot_radius - 0.1, 0],
                color=self.COLOR_HIGHLIGHT,
                stroke_width=2
            )

            label_num = (g + 1) * 2
            lbl = Text(
                str(label_num),
                font="PingFang SC",
                font_size=28,
                color=self.COLOR_HIGHLIGHT
            ).move_to([gx + dot_gap / 2, gy - 0.65, 0])

            grp = VGroup(d1, d2, brace_line)
            dots_groups.add(grp)
            labels.add(lbl)

        for i in range(10):
            self.play(
                FadeIn(dots_groups[i]),
                FadeIn(labels[i]),
                run_time=0.28
            )

        self.wait(1.0)

        conclusion = Text(
            "两个两个数，全是偶数！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_GREEN
        ).move_to(DOWN * 6.0)
        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(sec_title), FadeOut(hint),
            FadeOut(dots_groups), FadeOut(labels), FadeOut(conclusion),
            run_time=0.5
        )

    # ------------------------------------------------------------------ #
    #  场景 4: 10个一 = 1个十
    # ------------------------------------------------------------------ #
    def scene_4_ten_ones_make_one_ten(self):
        sec_title = Text(
            "10个一是1个十",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        self.play(Write(sec_title), run_time=0.6)

        # 10个小方块（代表"个"）
        unit_size = 0.52
        gap = 0.62
        ones_group = VGroup()
        start_x = -9 * gap / 2

        for i in range(10):
            sq = Square(
                side_length=unit_size,
                fill_color=self.COLOR_ONES,
                fill_opacity=0.85,
                stroke_color=WHITE,
                stroke_width=2
            ).move_to([start_x + i * gap, 3.2, 0])

            num_t = Text(
                "1",
                font="PingFang SC",
                font_size=22,
                color=WHITE
            ).move_to(sq.get_center())

            ones_group.add(VGroup(sq, num_t))

        ones_label = Text(
            "10个一",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_ONES
        ).move_to(UP * 2.2)

        for sq in ones_group:
            self.play(FadeIn(sq), run_time=0.12)

        self.play(FadeIn(ones_label), run_time=0.4)
        self.wait(0.5)

        # 等号
        equals_text = Text(
            "=",
            font="PingFang SC",
            font_size=50,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.0)
        self.play(Write(equals_text), run_time=0.3)

        # 大的"十"方块
        ten_sq = Square(
            side_length=1.4,
            fill_color=self.COLOR_TENS,
            fill_opacity=0.9,
            stroke_color=WHITE,
            stroke_width=3
        ).move_to(UP * -0.5)

        ten_label_inside = Text(
            "10",
            font="PingFang SC",
            font_size=42,
            color=WHITE
        ).move_to(ten_sq.get_center())

        ten_caption = Text(
            "1个十",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_TENS
        ).move_to(DOWN * 1.7)

        # 动画：10个小方块汇聚 → 一个大方块
        self.play(
            *[sq.animate.move_to(ten_sq.get_center()).scale(0) for sq in ones_group],
            run_time=1.0
        )
        self.play(
            GrowFromCenter(ten_sq),
            FadeIn(ten_label_inside),
            run_time=0.6
        )
        self.play(FadeIn(ten_caption), run_time=0.4)

        # 核心公式
        formula_line = VGroup(
            Text("10个一", font="PingFang SC", font_size=34, color=self.COLOR_ONES),
            Text(" = ", font="PingFang SC", font_size=34, color=WHITE),
            Text("1个十", font="PingFang SC", font_size=34, color=self.COLOR_TENS),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.0)

        self.play(FadeIn(formula_line, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(sec_title), FadeOut(ones_label), FadeOut(equals_text),
            FadeOut(ten_sq), FadeOut(ten_label_inside),
            FadeOut(ten_caption), FadeOut(formula_line),
            run_time=0.5
        )

    # ------------------------------------------------------------------ #
    #  场景 5: 认识计数器（十位和个位）
    # ------------------------------------------------------------------ #
    def scene_5_place_value_counter(self):
        sec_title = Text(
            "认识计数器",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        self.play(Write(sec_title), run_time=0.6)

        # 计数器框架
        col_gap = 2.8
        col_tens_x = -col_gap / 2
        col_ones_x = col_gap / 2
        top_y = 5.0
        bottom_y = -0.5

        divider = Line([0, top_y, 0], [0, bottom_y, 0], color="#4a5568", stroke_width=2)
        top_bar = Line(
            [col_tens_x - 1.0, top_y, 0],
            [col_ones_x + 1.0, top_y, 0],
            color="#718096", stroke_width=3
        )

        tens_title = Text(
            "十位",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_TENS
        ).move_to([col_tens_x, top_y + 0.7, 0])

        ones_title = Text(
            "个位",
            font="PingFang SC",
            font_size=34,
            color=self.COLOR_ONES
        ).move_to([col_ones_x, top_y + 0.7, 0])

        self.play(
            Create(divider), Create(top_bar),
            FadeIn(tens_title), FadeIn(ones_title),
            run_time=0.6
        )

        # 表示数字 13：十位1珠，个位3珠
        num_tens = 1
        num_ones = 3
        bead_r = 0.28
        bead_spacing = 0.75
        bead_start_y = top_y - 0.7

        tens_beads = VGroup()
        for i in range(num_tens):
            b = Circle(
                radius=bead_r,
                fill_color=self.COLOR_TENS,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=2
            ).move_to([col_tens_x, bead_start_y - i * bead_spacing, 0])
            tens_beads.add(b)

        ones_beads = VGroup()
        for i in range(num_ones):
            b = Circle(
                radius=bead_r,
                fill_color=self.COLOR_ONES,
                fill_opacity=1,
                stroke_color=WHITE,
                stroke_width=2
            ).move_to([col_ones_x, bead_start_y - i * bead_spacing, 0])
            ones_beads.add(b)

        for bead in tens_beads:
            self.play(FadeIn(bead, shift=DOWN * 0.3), run_time=0.3)
        for bead in ones_beads:
            self.play(FadeIn(bead, shift=DOWN * 0.3), run_time=0.2)

        # 数字解读
        reading_line = VGroup(
            Text("13", font="PingFang SC", font_size=52, color=WHITE),
            Text("=", font="PingFang SC", font_size=40, color=WHITE),
            Text("1个十", font="PingFang SC", font_size=34, color=self.COLOR_TENS),
            Text("+", font="PingFang SC", font_size=34, color=WHITE),
            Text("3个一", font="PingFang SC", font_size=34, color=self.COLOR_ONES),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.8)

        self.play(FadeIn(reading_line, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(sec_title), FadeOut(divider), FadeOut(top_bar),
            FadeOut(tens_title), FadeOut(ones_title),
            FadeOut(tens_beads), FadeOut(ones_beads),
            FadeOut(reading_line),
            run_time=0.5
        )

    # ------------------------------------------------------------------ #
    #  场景 6: 数的组成示例 (11, 15)
    # ------------------------------------------------------------------ #
    def scene_6_number_composition(self):
        sec_title = Text(
            "数的组成",
            font="PingFang SC",
            font_size=44,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)
        self.play(Write(sec_title), run_time=0.5)

        examples = [
            (11, 1, 1),
            (15, 1, 5),
        ]

        for num, tens, ones in examples:
            self._show_number_composition(num, tens, ones)

        # 清掉标题
        self.play(FadeOut(sec_title), run_time=0.4)

    def _show_number_composition(self, number, tens_count, ones_count):
        """展示一个数的组成"""
        # 大数字
        big_num = Text(
            str(number),
            font="PingFang SC",
            font_size=100,
            color=WHITE
        ).move_to(UP * 5.0)

        self.play(FadeIn(big_num, shift=UP * 0.4), run_time=0.5)

        # "十"方块
        ten_boxes = VGroup()
        for i in range(tens_count):
            sq = Square(
                side_length=1.2,
                fill_color=self.COLOR_TENS,
                fill_opacity=0.9,
                stroke_color=WHITE,
                stroke_width=2.5
            )
            t = Text("10", font="PingFang SC", font_size=28, color=WHITE)
            t.move_to(sq.get_center())
            ten_boxes.add(VGroup(sq, t))

        # "一"方块
        one_boxes = VGroup()
        for i in range(ones_count):
            sq = Square(
                side_length=0.7,
                fill_color=self.COLOR_ONES,
                fill_opacity=0.85,
                stroke_color=WHITE,
                stroke_width=1.5
            )
            t = Text("1", font="PingFang SC", font_size=20, color=WHITE)
            t.move_to(sq.get_center())
            one_boxes.add(VGroup(sq, t))

        # 布局：十方块 + 个方块横排
        all_boxes = VGroup(*list(ten_boxes) + list(one_boxes)).arrange(RIGHT, buff=0.35)
        all_boxes.move_to(UP * 3.0)

        for box in all_boxes:
            self.play(GrowFromCenter(box), run_time=0.35)

        # 箭头标注
        arrow_tens = Arrow(
            start=ten_boxes[0].get_bottom() + DOWN * 0.05,
            end=ten_boxes[0].get_bottom() + DOWN * 0.8,
            color=self.COLOR_TENS,
            buff=0.05,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25
        )
        label_tens = Text(
            f"{tens_count}个十",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_TENS
        ).next_to(arrow_tens, DOWN, buff=0.1)

        arrow_ones = Arrow(
            start=one_boxes[-1].get_bottom() + DOWN * 0.05,
            end=one_boxes[-1].get_bottom() + DOWN * 0.8,
            color=self.COLOR_ONES,
            buff=0.05,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25
        )
        label_ones = Text(
            f"{ones_count}个一",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_ONES
        ).next_to(arrow_ones, DOWN, buff=0.1)

        self.play(
            Create(arrow_tens), FadeIn(label_tens),
            Create(arrow_ones), FadeIn(label_ones),
            run_time=0.5
        )

        # 公式行
        formula = VGroup(
            Text(str(number), font="PingFang SC", font_size=44, color=WHITE),
            Text("=", font="PingFang SC", font_size=38, color=WHITE),
            Text(f"{tens_count}个十", font="PingFang SC", font_size=34, color=self.COLOR_TENS),
            Text("+", font="PingFang SC", font_size=34, color=WHITE),
            Text(f"{ones_count}个一", font="PingFang SC", font_size=34, color=self.COLOR_ONES),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 0.5)

        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.6)

        # 位值框
        place_content = VGroup(
            Text("十位", font="PingFang SC", font_size=26, color=self.COLOR_TENS),
            Text(":", font="PingFang SC", font_size=26, color=WHITE),
            Text(str(tens_count), font="PingFang SC", font_size=36, color=self.COLOR_TENS),
            Text("  个位", font="PingFang SC", font_size=26, color=self.COLOR_ONES),
            Text(":", font="PingFang SC", font_size=26, color=WHITE),
            Text(str(ones_count), font="PingFang SC", font_size=36, color=self.COLOR_ONES),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 1.8)

        box_bg = RoundedRectangle(
            width=place_content.width + 0.5,
            height=place_content.height + 0.35,
            corner_radius=0.2,
            fill_color="#1e3a5f",
            fill_opacity=0.9,
            stroke_color=self.COLOR_ONES,
            stroke_width=2
        ).move_to(place_content.get_center())

        self.play(FadeIn(box_bg), FadeIn(place_content), run_time=0.5)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(big_num), FadeOut(all_boxes),
            FadeOut(arrow_tens), FadeOut(label_tens),
            FadeOut(arrow_ones), FadeOut(label_ones),
            FadeOut(formula), FadeOut(place_content), FadeOut(box_bg),
            run_time=0.5
        )

    # ------------------------------------------------------------------ #
    #  场景 7: 片尾
    # ------------------------------------------------------------------ #
    def scene_7_outro(self):
        summary_title = Text(
            "今天学了什么？",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        self.play(Write(summary_title), run_time=0.6)

        points_data = [
            ("1 → 20", "从1数到20，从20数到1"),
            ("2, 4, 6…", "两个两个地数"),
            ("10个一=1个十", "满十进一，位值制"),
            ("十位 + 个位", "数的组成"),
        ]

        point_items = VGroup()
        for key, desc in points_data:
            dot = Circle(
                radius=0.12,
                fill_color=self.COLOR_HIGHLIGHT,
                fill_opacity=1,
                stroke_width=0
            )
            key_t = Text(key, font="PingFang SC", font_size=26, color=self.COLOR_HIGHLIGHT)
            desc_t = Text(desc, font="PingFang SC", font_size=20, color=self.COLOR_SUBTITLE)
            row = VGroup(dot, key_t, desc_t).arrange(RIGHT, buff=0.25)
            point_items.add(row)

        point_items.arrange(DOWN, buff=0.55, aligned_edge=LEFT).move_to(UP * 2.5)

        for item in point_items:
            self.play(FadeIn(item, shift=RIGHT * 0.4), run_time=0.4)
            self.wait(0.15)

        self.wait(0.8)

        # 作者放大 + 关注提示
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 2.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SUBTITLE
        ).move_to(DOWN * 3.3)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.3)

        self.play(Transform(self.author, author_big), run_time=0.6)
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)

        # 装饰性数字环绕
        deco_nums = VGroup(*[
            Text(
                str(n),
                font="PingFang SC",
                font_size=20,
                color=self.COLOR_ONES if n % 2 == 0 else self.COLOR_TENS
            ).move_to(
                follow_text.get_center() +
                2.5 * np.array([
                    np.cos(n * 2 * PI / 10 - PI / 2),
                    np.sin(n * 2 * PI / 10 - PI / 2),
                    0
                ])
            )
            for n in range(1, 11)
        ])

        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in deco_nums], lag_ratio=0.1),
            run_time=1.0
        )
        self.wait(1.5)

        self.play(
            FadeOut(summary_title), FadeOut(point_items),
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow_text), FadeOut(deco_nums),
            run_time=1.0
        )
