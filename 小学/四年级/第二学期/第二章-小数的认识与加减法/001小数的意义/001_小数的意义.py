"""
小数的意义 - Decimal Meaning Animation
使用 Manim 创建的小学四年级数学教学视频

内容: 从分数角度理解小数，小数点、数位与计数单位
目标观众: 四年级小学生
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


class DecimalMeaningLesson(Scene):
    """
    小数的意义教学动画

    场景顺序:
    1. 开场钩子
    2. 分数 → 小数 概念引入
    3. 1/10 = 0.1 演示
    4. 3/100 = 0.03 演示
    5. 25/100 = 0.25 演示
    6. 数位表 (十分位、百分位、千分位)
    7. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色
        self.C_TITLE     = "#f9ca24"   # 金黄 - 标题
        self.C_FRAC      = "#6ab04c"   # 绿色 - 分数
        self.C_DEC       = "#e74c3c"   # 红色 - 小数
        self.C_ARROW     = "#f0932b"   # 橙色 - 箭头
        self.C_UNIT      = "#48dbfb"   # 青色 - 计数单位
        self.C_GRID      = "#7f8c8d"   # 灰色 - 网格
        self.C_HIGHLIGHT = YELLOW
        self.C_TEXT      = WHITE
        self.C_SUB       = "#b2bec3"   # 浅灰 - 辅助文字

        self.scene_1_opening()
        self.scene_2_fraction_to_decimal()
        self.scene_3_tenth()
        self.scene_4_hundredth()
        self.scene_5_twentyfive_hundredths()
        self.scene_6_place_value_table()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 辅助：作者标识
    # ------------------------------------------------------------------
    def _author_tag(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)

    # ------------------------------------------------------------------
    # 场景 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        author = self._author_tag()
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        q1 = Text("你知道", font="PingFang SC", font_size=40, color=self.C_TEXT)
        q2 = Text("0.1 是怎么来的吗?", font="PingFang SC",
                  font_size=40, color=self.C_HIGHLIGHT)
        hook = VGroup(q1, q2).arrange(DOWN, buff=0.3).move_to(UP * 4.5)

        self.play(Write(q1), run_time=0.6)
        self.play(Write(q2), run_time=0.7)
        self.wait(0.5)

        # 大标题
        title = Text("小数的意义", font="PingFang SC",
                     font_size=52, color=self.C_TITLE)
        title.move_to(UP * 2.5)

        sub = Text("分数 → 小数", font="PingFang SC",
                   font_size=30, color=self.C_SUB)
        sub.next_to(title, DOWN, buff=0.4)

        self.play(FadeIn(title, scale=0.9), run_time=0.8)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(0.8)

        # 清场，保留作者标识
        self.play(FadeOut(hook), FadeOut(title), FadeOut(sub), run_time=0.5)
        self.author = author

    # ------------------------------------------------------------------
    # 场景 2: 分数 → 小数 概念引入
    # ------------------------------------------------------------------
    def scene_2_fraction_to_decimal(self):
        # 标题
        title = Text("分母是 10、100、1000…",
                     font="PingFang SC", font_size=32, color=self.C_TITLE)
        title.move_to(UP * 5.8)

        subtitle = Text("的分数可以写成小数",
                        font="PingFang SC", font_size=28, color=self.C_SUB)
        subtitle.next_to(title, DOWN, buff=0.25)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(subtitle), run_time=0.5)

        # 三个例子
        examples_data = [
            (r"\frac{1}{10}",   r"= 0.1"),
            (r"\frac{3}{100}",  r"= 0.03"),
            (r"\frac{25}{100}", r"= 0.25"),
        ]

        rows = VGroup()
        for frac_tex, eq_str in examples_data:
            frac = MathTex(frac_tex, font_size=40, color=self.C_FRAC)
            eq   = MathTex(eq_str,   font_size=40, color=self.C_DEC)
            row  = VGroup(frac, eq).arrange(RIGHT, buff=0.5)
            rows.add(row)

        rows.arrange(DOWN, buff=0.6).move_to(UP * 3.0)

        for row in rows:
            self.play(FadeIn(row[0], shift=RIGHT * 0.3), run_time=0.5)
            self.play(Write(row[1]), run_time=0.5)
            self.wait(0.3)

        # 关键说明
        note = Text("小数是十进制分数的另一种写法",
                    font="PingFang SC", font_size=24, color=self.C_HIGHLIGHT)
        note.move_to(UP * 0.8)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.6)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(rows), FadeOut(note),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # 辅助：绘制 N 格方块网格，高亮 k 格
    # ------------------------------------------------------------------
    def _make_grid_strip(self, n, k, center, width=5.5, height=1.0,
                         fill_color="#e74c3c", grid_color="#7f8c8d"):
        """返回 (全部格子VGroup, 高亮格子VGroup)"""
        cell_w = width / n
        rects = VGroup()
        highlighted = VGroup()

        for i in range(n):
            x_mid = center[0] - width / 2 + i * cell_w + cell_w / 2
            y_mid = center[1]

            rect = Rectangle(
                width=cell_w, height=height,
                fill_opacity=0,
                stroke_color=grid_color,
                stroke_width=1.5,
            ).move_to(np.array([x_mid, y_mid, 0]))

            if i < k:
                rect.set_fill(fill_color, opacity=0.7)
                highlighted.add(rect)

            rects.add(rect)

        return rects, highlighted

    # ------------------------------------------------------------------
    # 场景 3: 1/10 = 0.1
    # ------------------------------------------------------------------
    def scene_3_tenth(self):
        title = Text("十分之一 = 0.1",
                     font="PingFang SC", font_size=38, color=self.C_TITLE)
        title.move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        explain = Text("把 1 平均分成 10 份，取其中 1 份",
                       font="PingFang SC", font_size=24, color=self.C_SUB)
        explain.move_to(UP * 4.9)
        self.play(FadeIn(explain), run_time=0.5)

        # 网格条 (10格，1格高亮)
        strip_center = np.array([0, 3.5, 0])
        strip, hl = self._make_grid_strip(
            10, 1, strip_center, width=5.6, height=0.9,
            fill_color=self.C_DEC, grid_color=self.C_GRID,
        )

        # 先画空格（高亮格初始透明）
        for r in hl:
            r.set_fill(self.C_DEC, opacity=0)

        self.play(Create(strip), run_time=0.8)
        self.wait(0.2)

        self.add(*hl)
        self.play(
            *[r.animate.set_fill(self.C_DEC, opacity=0.75) for r in hl],
            run_time=0.6,
        )

        # 标注"1份"
        brace_hl = Brace(hl, direction=UP, color=self.C_HIGHLIGHT)
        brace_label = Text("1 份", font="PingFang SC", font_size=22,
                           color=self.C_HIGHLIGHT).next_to(brace_hl, UP, buff=0.15)
        self.play(FadeIn(brace_hl), FadeIn(brace_label), run_time=0.5)
        self.wait(0.3)

        # 分数 → 小数
        frac = MathTex(r"\frac{1}{10}", font_size=64, color=self.C_FRAC)
        frac.move_to(LEFT * 1.8 + UP * 1.6)

        arrow = Arrow(frac.get_right(), frac.get_right() + RIGHT * 1.5,
                      color=self.C_ARROW, buff=0.1)

        dec = MathTex(r"0.1", font_size=64, color=self.C_DEC)
        dec.next_to(arrow, RIGHT, buff=0.15)

        self.play(FadeIn(frac, shift=UP * 0.3), run_time=0.6)
        self.wait(0.3)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(Write(dec), run_time=0.5)
        self.wait(0.4)

        # 说明：十分位
        note1 = Text("小数点后第一位", font="PingFang SC",
                     font_size=24, color=self.C_UNIT)
        note2 = Text("叫做「十分位」", font="PingFang SC",
                     font_size=24, color=self.C_UNIT)
        notes = VGroup(note1, note2).arrange(DOWN, buff=0.2).move_to(DOWN * 0.2)
        self.play(FadeIn(notes, shift=UP * 0.2), run_time=0.6)

        # 圈住"1"（0.1 中的 1）
        box = SurroundingRectangle(dec[0][-1], color=self.C_UNIT, buff=0.06)
        self.play(Create(box), run_time=0.5)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title), FadeOut(explain),
            FadeOut(strip), *[FadeOut(r) for r in hl],
            FadeOut(brace_hl), FadeOut(brace_label),
            FadeOut(frac), FadeOut(arrow), FadeOut(dec),
            FadeOut(notes), FadeOut(box),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # 场景 4: 3/100 = 0.03
    # ------------------------------------------------------------------
    def scene_4_hundredth(self):
        title = Text("百分之三 = 0.03",
                     font="PingFang SC", font_size=38, color=self.C_TITLE)
        title.move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        explain = Text("把 1 平均分成 100 份，取其中 3 份",
                       font="PingFang SC", font_size=24, color=self.C_SUB)
        explain.move_to(UP * 4.9)
        self.play(FadeIn(explain), run_time=0.5)

        # 10×10 方格代表 100 份
        grid_center = np.array([0, 3.2, 0])
        grid_size   = 4.0
        cell        = grid_size / 10

        all_cells     = VGroup()
        colored_cells = []

        for row in range(10):
            for col in range(10):
                x   = grid_center[0] - grid_size / 2 + col * cell + cell / 2
                y   = grid_center[1] + grid_size / 2 - row * cell - cell / 2
                idx = row * 10 + col
                rect = Rectangle(
                    width=cell, height=cell,
                    fill_opacity=0,
                    stroke_color=self.C_GRID,
                    stroke_width=1.0,
                ).move_to(np.array([x, y, 0]))
                all_cells.add(rect)
                if idx < 3:
                    colored_cells.append(rect)

        self.play(Create(all_cells), run_time=1.0)
        self.wait(0.2)

        for r in colored_cells:
            r.set_fill(self.C_DEC, opacity=0)
        self.add(*colored_cells)
        self.play(
            *[r.animate.set_fill(self.C_DEC, opacity=0.85) for r in colored_cells],
            run_time=0.6,
        )

        # 标注
        colored_group = VGroup(*colored_cells)
        brace_hl = Brace(colored_group, direction=RIGHT, color=self.C_HIGHLIGHT)
        brace_label = Text("3 份", font="PingFang SC", font_size=20,
                           color=self.C_HIGHLIGHT).next_to(brace_hl, RIGHT, buff=0.12)
        self.play(FadeIn(brace_hl), FadeIn(brace_label), run_time=0.5)
        self.wait(0.3)

        # 公式
        frac  = MathTex(r"\frac{3}{100}", font_size=56, color=self.C_FRAC)
        frac.move_to(LEFT * 2.0 + UP * 0.4)
        arrow = Arrow(frac.get_right(), frac.get_right() + RIGHT * 1.3,
                      color=self.C_ARROW, buff=0.1)
        dec   = MathTex(r"0.03", font_size=56, color=self.C_DEC)
        dec.next_to(arrow, RIGHT, buff=0.15)

        self.play(FadeIn(frac, shift=UP * 0.3), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.4)
        self.play(Write(dec), run_time=0.5)
        self.wait(0.4)

        # 说明
        note = Text("小数点后第二位叫「百分位」",
                    font="PingFang SC", font_size=24, color=self.C_UNIT)
        note.move_to(DOWN * 1.0)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.6)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(title), FadeOut(explain),
            FadeOut(all_cells), *[FadeOut(r) for r in colored_cells],
            FadeOut(brace_hl), FadeOut(brace_label),
            FadeOut(frac), FadeOut(arrow), FadeOut(dec),
            FadeOut(note),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # 场景 5: 25/100 = 0.25
    # ------------------------------------------------------------------
    def scene_5_twentyfive_hundredths(self):
        title = Text("百分之二十五 = 0.25",
                     font="PingFang SC", font_size=34, color=self.C_TITLE)
        title.move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        explain = Text("把 1 平均分成 100 份，取其中 25 份",
                       font="PingFang SC", font_size=23, color=self.C_SUB)
        explain.move_to(UP * 4.9)
        self.play(FadeIn(explain), run_time=0.5)

        # 10×10 方格
        grid_center = np.array([0, 3.1, 0])
        grid_size   = 4.0
        cell        = grid_size / 10

        all_cells     = VGroup()
        colored_cells = []

        for row in range(10):
            for col in range(10):
                x   = grid_center[0] - grid_size / 2 + col * cell + cell / 2
                y   = grid_center[1] + grid_size / 2 - row * cell - cell / 2
                idx = row * 10 + col
                rect = Rectangle(
                    width=cell, height=cell,
                    fill_opacity=0,
                    stroke_color=self.C_GRID,
                    stroke_width=1.0,
                ).move_to(np.array([x, y, 0]))
                all_cells.add(rect)
                if idx < 25:
                    colored_cells.append(rect)

        self.play(Create(all_cells), run_time=0.9)

        for r in colored_cells:
            r.set_fill(self.C_FRAC, opacity=0)
        self.add(*colored_cells)
        self.play(
            *[r.animate.set_fill(self.C_FRAC, opacity=0.82) for r in colored_cells],
            run_time=0.7,
        )

        # 分数与小数
        frac  = MathTex(r"\frac{25}{100}", font_size=52, color=self.C_FRAC)
        frac.move_to(LEFT * 2.0 + UP * 0.4)
        arrow = Arrow(frac.get_right(), frac.get_right() + RIGHT * 1.3,
                      color=self.C_ARROW, buff=0.1)
        dec   = MathTex(r"0.25", font_size=52, color=self.C_DEC)
        dec.next_to(arrow, RIGHT, buff=0.15)

        self.play(FadeIn(frac), GrowArrow(arrow), run_time=0.6)
        self.play(Write(dec), run_time=0.5)
        self.wait(0.4)

        # 解析每一位
        hint = Text("2 在十分位，5 在百分位",
                    font="PingFang SC", font_size=24, color=self.C_UNIT)
        hint.move_to(DOWN * 0.9)
        self.play(FadeIn(hint, shift=UP * 0.2), run_time=0.6)

        # 分别圈出 2 和 5
        box2 = SurroundingRectangle(dec[0][-2], color=self.C_UNIT, buff=0.06)
        box5 = SurroundingRectangle(dec[0][-1], color=self.C_DEC,  buff=0.06)
        self.play(Create(box2), run_time=0.4)
        self.play(Create(box5), run_time=0.4)
        self.wait(1.4)

        # 清场
        self.play(
            FadeOut(title), FadeOut(explain),
            FadeOut(all_cells), *[FadeOut(r) for r in colored_cells],
            FadeOut(frac), FadeOut(arrow), FadeOut(dec),
            FadeOut(hint), FadeOut(box2), FadeOut(box5),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # 场景 6: 数位表 (整数部分 / 小数部分)
    # ------------------------------------------------------------------
    def scene_6_place_value_table(self):
        title = Text("小数的数位",
                     font="PingFang SC", font_size=42, color=self.C_TITLE)
        title.move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # ---- 表格参数 ----
        col_labels = ["百", "十", "个", ".", "十分位", "百分位", "千分位"]
        col_colors = [
            self.C_TEXT, self.C_TEXT, self.C_TEXT,
            self.C_DEC,
            self.C_UNIT, self.C_UNIT, self.C_UNIT,
        ]
        # 示例数字行 (6.375)
        digit_row = ["", "", "6", ".", "3", "7", "5"]

        n_cols  = len(col_labels)
        col_w   = 1.05
        row_h   = 0.85
        table_x = 0.0
        table_y = 4.5   # 顶部 y 坐标

        total_w = col_w * n_cols
        total_h = row_h * 2

        # 外框
        outer = Rectangle(
            width=total_w, height=total_h,
            stroke_color=self.C_TEXT, stroke_width=2, fill_opacity=0,
        ).move_to(np.array([table_x, table_y - total_h / 2, 0]))
        self.play(Create(outer), run_time=0.5)

        # 列线
        v_lines = VGroup()
        for i in range(1, n_cols):
            x = table_x - total_w / 2 + i * col_w
            v_lines.add(Line(
                [x, table_y, 0], [x, table_y - total_h, 0],
                stroke_color=self.C_GRID, stroke_width=1.5,
            ))

        # 水平中线
        mid_y  = table_y - row_h
        h_line = Line(
            [table_x - total_w / 2, mid_y, 0],
            [table_x + total_w / 2, mid_y, 0],
            stroke_color=self.C_GRID, stroke_width=1.5,
        )

        self.play(Create(v_lines), Create(h_line), run_time=0.5)

        # 表头文字
        header_texts = VGroup()
        for i, (label, col_c) in enumerate(zip(col_labels, col_colors)):
            x = table_x - total_w / 2 + i * col_w + col_w / 2
            y = table_y - row_h / 2
            if label == ".":
                t = MathTex(r"\cdot", font_size=36, color=col_c)
            else:
                t = Text(label, font="PingFang SC", font_size=18, color=col_c)
            t.move_to(np.array([x, y, 0]))
            header_texts.add(t)

        self.play(FadeIn(header_texts), run_time=0.6)

        # 数字行
        digit_texts = VGroup()
        for i, (d, col_c) in enumerate(zip(digit_row, col_colors)):
            x = table_x - total_w / 2 + i * col_w + col_w / 2
            y = table_y - row_h - row_h / 2
            if d == ".":
                t = MathTex(r"\boldsymbol{\cdot}", font_size=48, color=self.C_DEC)
            elif d == "":
                t = Text("", font="PingFang SC", font_size=28)
            else:
                color = self.C_TEXT if i < 3 else self.C_UNIT
                t = MathTex(d, font_size=34, color=color)
            t.move_to(np.array([x, y, 0]))
            digit_texts.add(t)

        self.play(FadeIn(digit_texts), run_time=0.6)
        self.wait(0.5)

        # 整数部分大括号
        int_start_x = table_x - total_w / 2
        int_end_x   = table_x - total_w / 2 + 3 * col_w
        brace_int = BraceBetweenPoints(
            [int_start_x, table_y - total_h - 0.05, 0],
            [int_end_x,   table_y - total_h - 0.05, 0],
            direction=DOWN, color=self.C_TEXT,
        )
        label_int = Text("整数部分", font="PingFang SC",
                         font_size=20, color=self.C_TEXT).next_to(brace_int, DOWN, buff=0.12)

        # 小数部分大括号
        dec_start_x = table_x - total_w / 2 + 4 * col_w
        dec_end_x   = table_x + total_w / 2
        brace_dec = BraceBetweenPoints(
            [dec_start_x, table_y - total_h - 0.05, 0],
            [dec_end_x,   table_y - total_h - 0.05, 0],
            direction=DOWN, color=self.C_UNIT,
        )
        label_dec = Text("小数部分", font="PingFang SC",
                         font_size=20, color=self.C_UNIT).next_to(brace_dec, DOWN, buff=0.12)

        self.play(
            FadeIn(brace_int), FadeIn(label_int),
            FadeIn(brace_dec), FadeIn(label_dec),
            run_time=0.7,
        )
        self.wait(0.6)

        # 小数点高亮列背景
        dot_col_center_x = table_x - total_w / 2 + 3 * col_w + col_w / 2
        dot_highlight = Rectangle(
            width=col_w, height=total_h,
            fill_color=self.C_DEC, fill_opacity=0.12,
            stroke_opacity=0,
        ).move_to(np.array([dot_col_center_x, table_y - total_h / 2, 0]))
        self.play(FadeIn(dot_highlight), run_time=0.4)

        # 小数点说明箭头
        dot_note = Text("小数点", font="PingFang SC",
                        font_size=22, color=self.C_DEC)
        dot_note.move_to(np.array([dot_col_center_x + 1.8, table_y - total_h - 0.5, 0]))
        arr_to_dot = Arrow(
            dot_note.get_top(),
            digit_texts[3].get_bottom() + DOWN * 0.05,
            color=self.C_DEC, buff=0.08, stroke_width=2,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(FadeIn(dot_note), GrowArrow(arr_to_dot), run_time=0.6)
        self.wait(0.5)

        # ---- 计数单位说明 ----
        units_title = Text("每个数位的计数单位",
                           font="PingFang SC", font_size=26, color=self.C_HIGHLIGHT)
        units_title.move_to(DOWN * 1.5)
        self.play(Write(units_title), run_time=0.5)

        unit_data = [
            ("十分位", r"\frac{1}{10}",    r"= 0.1"),
            ("百分位", r"\frac{1}{100}",   r"= 0.01"),
            ("千分位", r"\frac{1}{1000}",  r"= 0.001"),
        ]

        unit_rows = VGroup()
        for name, frac_str, dec_str in unit_data:
            name_t = Text(name, font="PingFang SC",
                          font_size=22, color=self.C_UNIT)
            frac_t = MathTex(frac_str, font_size=26, color=self.C_FRAC)
            eq_t   = MathTex(r"=", font_size=26, color=self.C_TEXT)
            dec_t  = MathTex(dec_str[2:], font_size=26, color=self.C_DEC)
            row    = VGroup(name_t, frac_t, eq_t, dec_t).arrange(RIGHT, buff=0.28)
            unit_rows.add(row)

        unit_rows.arrange(DOWN, buff=0.35).next_to(units_title, DOWN, buff=0.35)

        for row in unit_rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.2)

        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title),
            FadeOut(outer), FadeOut(v_lines), FadeOut(h_line),
            FadeOut(header_texts), FadeOut(digit_texts),
            FadeOut(brace_int), FadeOut(label_int),
            FadeOut(brace_dec), FadeOut(label_dec),
            FadeOut(dot_highlight), FadeOut(dot_note), FadeOut(arr_to_dot),
            FadeOut(units_title), FadeOut(unit_rows),
            run_time=0.7,
        )

    # ------------------------------------------------------------------
    # 场景 7: 片尾
    # ------------------------------------------------------------------
    def scene_7_outro(self):
        summary_title = Text("小结",
                             font="PingFang SC", font_size=44, color=self.C_TITLE)
        summary_title.move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.5)

        points = [
            "分母是 10、100、1000… 的分数",
            "可以写成小数",
            "小数点左边是整数部分",
            "小数点右边是小数部分",
            "十分位的计数单位是 0.1",
            "百分位的计数单位是 0.01",
            "千分位的计数单位是 0.001",
        ]
        point_items = VGroup()
        for p in points:
            bullet = Text("• " + p, font="PingFang SC",
                          font_size=25, color=self.C_TEXT)
            point_items.add(bullet)

        point_items.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        point_items.move_to(UP * 2.5)

        for item in point_items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.32)
        self.wait(0.8)

        # 作者信息
        author_big = Text("上海初高中数学直通车", font="PingFang SC",
                          font_size=36, color=WHITE)
        author_id  = Text("@emptyandcalm", font="PingFang SC",
                          font_size=28, color=self.C_SUB)
        author_group = VGroup(author_big, author_id).arrange(DOWN, buff=0.25)
        author_group.move_to(DOWN * 3.5)

        follow = Text("关注我，学更多数学知识！", font="PingFang SC",
                      font_size=28, color=self.C_HIGHLIGHT)
        follow.next_to(author_group, DOWN, buff=0.4)

        self.play(FadeIn(author_big), FadeIn(author_id), run_time=0.6)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)
        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(summary_title), FadeOut(point_items),
            FadeOut(author_group), FadeOut(follow),
            FadeOut(self.author),
            run_time=0.8,
        )
