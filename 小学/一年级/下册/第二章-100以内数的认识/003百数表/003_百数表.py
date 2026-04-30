"""
百数表 - 一年级数学教学动画
利用百数表探索规律：横着看（十位相同）、竖着看（个位相同）、斜着看
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


# 颜色配置
COLOR_BG = "#1a1a2e"
COLOR_TITLE = "#f39c12"
COLOR_ROW_HIGHLIGHT = "#e74c3c"
COLOR_COL_HIGHLIGHT = "#3498db"
COLOR_DIAG_HIGHLIGHT = "#2ecc71"
COLOR_CELL_DEFAULT = "#16213e"
COLOR_CELL_BORDER = "#0f3460"
COLOR_TEXT_NORMAL = "#e0e0e0"
COLOR_TEXT_HIGHLIGHT = "#ffffff"
COLOR_ACCENT = "#9b59b6"
COLOR_GOLD = "#f1c40f"


class HundredChartLesson(Scene):
    """
    百数表教学动画
    场景顺序:
    1. 开场 - 引出百数表
    2. 建立百数表
    3. 横行规律（十位相同）
    4. 竖列规律（个位相同）
    5. 斜线规律
    6. 总结与片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG

        # 作者信息（常驻顶部）
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(self.author_label)

        self.scene_1_opening()
        self.scene_2_build_chart()
        self.scene_3_row_pattern()
        self.scene_4_col_pattern()
        self.scene_5_diagonal_pattern()
        self.scene_6_outro()

    # ─────────────────────────────────────────────
    # 辅助：生成格子和数字
    # ─────────────────────────────────────────────
    def make_chart(self, cell_size=0.72):
        """
        生成10×10百数表，返回 (cells_group, numbers_group, cell_matrix, num_matrix)
        cell_matrix[row][col] 是对应的 Square 对象
        num_matrix[row][col] 是对应的 Text 对象
        以 ORIGIN 为整体中心
        """
        cell_matrix = []
        num_matrix = []
        cells_group = VGroup()
        numbers_group = VGroup()

        grid_width = cell_size * 10
        grid_height = cell_size * 10
        # 左上角格子中心坐标
        x0 = -grid_width / 2 + cell_size / 2
        y0 = grid_height / 2 - cell_size / 2

        for row in range(10):
            row_cells = []
            row_nums = []
            for col in range(10):
                num = row * 10 + col + 1
                cx = x0 + col * cell_size
                cy = y0 - row * cell_size

                cell = Square(
                    side_length=cell_size,
                    fill_color=COLOR_CELL_DEFAULT,
                    fill_opacity=0.9,
                    stroke_color=COLOR_CELL_BORDER,
                    stroke_width=1.5
                ).move_to([cx, cy, 0])

                label = Text(
                    str(num),
                    font="PingFang SC",
                    font_size=22,
                    color=COLOR_TEXT_NORMAL
                ).move_to([cx, cy, 0])

                row_cells.append(cell)
                row_nums.append(label)
                cells_group.add(cell)
                numbers_group.add(label)
            cell_matrix.append(row_cells)
            num_matrix.append(row_nums)

        return cells_group, numbers_group, cell_matrix, num_matrix

    def highlight_cells(self, cm, nm, positions, color):
        """高亮指定格子列表 positions=[(row,col),...]，返回动画列表"""
        anims = []
        for (r, c) in positions:
            anims.append(cm[r][c].animate.set_fill(color, opacity=0.85))
            anims.append(nm[r][c].animate.set_color(COLOR_TEXT_HIGHLIGHT))
        return anims

    def reset_cells(self, cm, nm, positions):
        """重置格子颜色"""
        anims = []
        for (r, c) in positions:
            anims.append(cm[r][c].animate.set_fill(COLOR_CELL_DEFAULT, opacity=0.9))
            anims.append(nm[r][c].animate.set_color(COLOR_TEXT_NORMAL))
        return anims

    # ─────────────────────────────────────────────
    # 场景1：开场
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        title = Text(
            "百数表",
            font="PingFang SC",
            font_size=72,
            color=COLOR_TITLE,
            weight=BOLD
        ).move_to(UP * 5.5)

        subtitle = Text(
            "1 到 100，藏着什么秘密？",
            font="PingFang SC",
            font_size=32,
            color=COLOR_TEXT_NORMAL
        ).move_to(UP * 4.3)

        # 装饰数字
        sample_data = [
            ("1",   UP * 2.8 + LEFT * 3.2,  BLUE_B),
            ("10",  UP * 2.8 + LEFT * 1.0,  BLUE_C),
            ("25",  UP * 2.8 + RIGHT * 1.2, TEAL_B),
            ("50",  UP * 2.8 + RIGHT * 3.2, TEAL_C),
            ("37",  UP * 1.2 + LEFT * 3.2,  GREEN_B),
            ("61",  UP * 1.2 + LEFT * 1.0,  GREEN_C),
            ("88",  UP * 1.2 + RIGHT * 1.2, PURPLE_B),
            ("100", UP * 1.2 + RIGHT * 3.2, PURPLE_C),
        ]
        deco_nums = VGroup()
        for txt, pos, col in sample_data:
            t = Text(
                txt,
                font="PingFang SC",
                font_size=36,
                color=col
            ).move_to(pos)
            deco_nums.add(t)

        hook = Text(
            "找规律，数学不再难！",
            font="PingFang SC",
            font_size=30,
            color=COLOR_GOLD
        ).move_to(DOWN * 1.5)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(n, scale=0.6) for n in deco_nums], lag_ratio=0.1),
            run_time=1.2
        )
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(deco_nums),
            FadeOut(hook),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # 场景2：建立百数表
    # ─────────────────────────────────────────────
    def scene_2_build_chart(self):
        title = Text(
            "百数表",
            font="PingFang SC",
            font_size=40,
            color=COLOR_TITLE
        ).move_to(UP * 6.8)

        subtitle = Text(
            "把 1～100 排成 10 行 × 10 列",
            font="PingFang SC",
            font_size=26,
            color=COLOR_TEXT_NORMAL
        ).move_to(UP * 6.0)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 构建百数表，放在屏幕中间偏下
        cells, nums, cm, nm = self.make_chart(cell_size=0.72)
        chart_group = VGroup(cells, nums).move_to(UP * 0.3)

        # 逐行出现
        for row in range(10):
            self.play(
                LaggedStart(
                    *[FadeIn(VGroup(cm[row][c], nm[row][c]), scale=0.8) for c in range(10)],
                    lag_ratio=0.05
                ),
                run_time=0.38
            )

        self.wait(0.8)

        row_label = Text(
            "→ 每行10个数",
            font="PingFang SC",
            font_size=24,
            color=COLOR_ROW_HIGHLIGHT
        ).move_to(DOWN * 5.8)
        col_label = Text(
            "↓ 共10行",
            font="PingFang SC",
            font_size=24,
            color=COLOR_COL_HIGHLIGHT
        ).move_to(DOWN * 6.5)

        self.play(FadeIn(row_label, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(col_label, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(1.0)

        self.play(FadeOut(row_label), FadeOut(col_label), FadeOut(subtitle), run_time=0.4)

        # 保存给后续场景使用
        self.chart_title = title
        self.chart_cells = cells
        self.chart_nums = nums
        self.cm = cm
        self.nm = nm
        self.chart_group = chart_group

    # ─────────────────────────────────────────────
    # 场景3：横行规律（十位相同）
    # ─────────────────────────────────────────────
    def scene_3_row_pattern(self):
        cm = self.cm
        nm = self.nm

        scene_title = Text(
            "横着看 →",
            font="PingFang SC",
            font_size=36,
            color=COLOR_ROW_HIGHLIGHT
        ).move_to(UP * 6.2)

        desc = Text(
            "同一行：十位数字相同！",
            font="PingFang SC",
            font_size=26,
            color=COLOR_TEXT_NORMAL
        ).move_to(UP * 5.5)

        self.play(
            ReplacementTransform(self.chart_title, scene_title),
            run_time=0.5
        )
        self.chart_title = scene_title
        self.play(FadeIn(desc), run_time=0.4)

        # 依次扫过几行，展示十位数字相同
        row_tips = [
            (0, "1, 2, 3 ... 10  十位是 0（或空）"),
            (1, "11, 12, 13 ... 20  十位都是 1"),
            (3, "31, 32, 33 ... 40  十位都是 3"),
            (6, "61, 62, 63 ... 70  十位都是 6"),
        ]

        for row_idx, tip_text in row_tips:
            positions = [(row_idx, c) for c in range(10)]
            anims = self.highlight_cells(cm, nm, positions, COLOR_ROW_HIGHLIGHT)
            self.play(*anims, run_time=0.35)

            tip = Text(
                tip_text,
                font="PingFang SC",
                font_size=21,
                color=COLOR_GOLD
            ).move_to(DOWN * 5.8)

            self.play(FadeIn(tip), run_time=0.3)
            self.wait(0.5)
            self.play(FadeOut(tip), run_time=0.2)

            reset_anims = self.reset_cells(cm, nm, positions)
            self.play(*reset_anims, run_time=0.25)

        # 慢速重点展示第5行（41-50）
        row_idx = 4
        positions = [(row_idx, c) for c in range(10)]
        anims = self.highlight_cells(cm, nm, positions, COLOR_ROW_HIGHLIGHT)
        self.play(*anims, run_time=0.4)

        row_tip_big = Text(
            "41, 42, 43 ... 50  十位都是 4",
            font="PingFang SC",
            font_size=24,
            color=COLOR_GOLD
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(row_tip_big), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(row_tip_big), FadeOut(desc), run_time=0.3)
        reset_anims = self.reset_cells(cm, nm, positions)
        self.play(*reset_anims, run_time=0.3)

    # ─────────────────────────────────────────────
    # 场景4：竖列规律（个位相同）
    # ─────────────────────────────────────────────
    def scene_4_col_pattern(self):
        cm = self.cm
        nm = self.nm

        scene_title = Text(
            "竖着看 ↓",
            font="PingFang SC",
            font_size=36,
            color=COLOR_COL_HIGHLIGHT
        ).move_to(UP * 6.2)

        desc = Text(
            "同一列：个位数字相同！",
            font="PingFang SC",
            font_size=26,
            color=COLOR_TEXT_NORMAL
        ).move_to(UP * 5.5)

        self.play(
            ReplacementTransform(self.chart_title, scene_title),
            run_time=0.5
        )
        self.chart_title = scene_title
        self.play(FadeIn(desc), run_time=0.4)

        # 依次高亮几列
        col_tips = [
            (0, "1, 11, 21, 31 ...  个位都是 1"),
            (2, "3, 13, 23, 33 ...  个位都是 3"),
            (4, "5, 15, 25, 35 ...  个位都是 5"),
            (6, "7, 17, 27, 37 ...  个位都是 7"),
            (9, "10, 20, 30, 40 ...  个位都是 0"),
        ]

        for col_idx, tip_text in col_tips:
            positions = [(r, col_idx) for r in range(10)]
            anims = self.highlight_cells(cm, nm, positions, COLOR_COL_HIGHLIGHT)
            self.play(*anims, run_time=0.35)

            tip = Text(
                tip_text,
                font="PingFang SC",
                font_size=21,
                color=COLOR_GOLD
            ).move_to(DOWN * 5.8)

            self.play(FadeIn(tip), run_time=0.3)
            self.wait(0.5)
            self.play(FadeOut(tip), run_time=0.2)

            reset_anims = self.reset_cells(cm, nm, positions)
            self.play(*reset_anims, run_time=0.25)

        # 重点高亮个位是2的列
        col_idx = 1
        positions = [(r, col_idx) for r in range(10)]
        anims = self.highlight_cells(cm, nm, positions, COLOR_COL_HIGHLIGHT)
        self.play(*anims, run_time=0.4)

        col_tip_big = Text(
            "2, 12, 22, 32, 42 ...  个位都是 2",
            font="PingFang SC",
            font_size=24,
            color=COLOR_GOLD
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(col_tip_big), run_time=0.4)
        self.wait(1.5)

        self.play(FadeOut(col_tip_big), FadeOut(desc), run_time=0.3)
        reset_anims = self.reset_cells(cm, nm, positions)
        self.play(*reset_anims, run_time=0.3)

    # ─────────────────────────────────────────────
    # 场景5：斜线规律 + 总结
    # ─────────────────────────────────────────────
    def scene_5_diagonal_pattern(self):
        cm = self.cm
        nm = self.nm

        scene_title = Text(
            "斜着看 ↘",
            font="PingFang SC",
            font_size=36,
            color=COLOR_DIAG_HIGHLIGHT
        ).move_to(UP * 6.2)

        desc = Text(
            "斜线上：每个数差 11！",
            font="PingFang SC",
            font_size=26,
            color=COLOR_TEXT_NORMAL
        ).move_to(UP * 5.5)

        self.play(
            ReplacementTransform(self.chart_title, scene_title),
            run_time=0.5
        )
        self.chart_title = scene_title
        self.play(FadeIn(desc), run_time=0.4)

        # 主对角线：1,12,23,34,45,56,67,78,89,100
        diag_main = [(i, i) for i in range(10)]
        anims = self.highlight_cells(cm, nm, diag_main, COLOR_DIAG_HIGHLIGHT)
        self.play(*anims, run_time=0.5)

        main_tip = Text(
            "1 → 12 → 23 → ... → 100  每次 +11",
            font="PingFang SC",
            font_size=22,
            color=COLOR_GOLD
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(main_tip), run_time=0.4)
        self.wait(1.5)
        self.play(FadeOut(main_tip), run_time=0.3)
        reset_anims = self.reset_cells(cm, nm, diag_main)
        self.play(*reset_anims, run_time=0.3)

        # 另一条斜线：2,13,24,35,46,57,68,79,90
        diag_2 = [(i, (i + 1) % 10) for i in range(9)]  # col=i+1, 只到第9行第0列
        # 实际: (0,1)→2, (1,2)→13, ..., (8,9)→90
        anims = self.highlight_cells(cm, nm, diag_2, COLOR_ACCENT)
        self.play(*anims, run_time=0.45)

        tip2 = Text(
            "2 → 13 → 24 → ... → 90  也差 11！",
            font="PingFang SC",
            font_size=22,
            color=COLOR_GOLD
        ).move_to(DOWN * 5.8)
        self.play(FadeIn(tip2), run_time=0.4)
        self.wait(1.2)
        self.play(FadeOut(tip2), FadeOut(desc), run_time=0.3)
        reset_anims = self.reset_cells(cm, nm, diag_2)
        self.play(*reset_anims, run_time=0.3)

        # ── 总结规律卡片 ──
        self.play(FadeOut(self.chart_title), run_time=0.3)

        rule_title = Text(
            "百数表的规律",
            font="PingFang SC",
            font_size=38,
            color=COLOR_TITLE
        ).move_to(UP * 6.5)

        self.play(Write(rule_title), run_time=0.6)
        self.chart_title = rule_title

        cards = VGroup(
            self._make_rule_card("→ 横着看", "同一行，十位相同", COLOR_ROW_HIGHLIGHT),
            self._make_rule_card("↓ 竖着看", "同一列，个位相同", COLOR_COL_HIGHLIGHT),
            self._make_rule_card("↘ 斜着看", "斜线上，每次 +11", COLOR_DIAG_HIGHLIGHT),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 5.2)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.4)
            self.wait(0.3)

        self.wait(1.5)
        self.play(FadeOut(cards), run_time=0.4)

    def _make_rule_card(self, arrow_text, detail_text, color):
        arrow = Text(
            arrow_text,
            font="PingFang SC",
            font_size=26,
            color=color
        )
        detail = Text(
            detail_text,
            font="PingFang SC",
            font_size=22,
            color=COLOR_TEXT_NORMAL
        )
        inner = VGroup(arrow, detail).arrange(RIGHT, buff=0.4)
        bg = SurroundingRectangle(
            inner,
            color=color,
            fill_color=COLOR_CELL_DEFAULT,
            fill_opacity=0.6,
            buff=0.2,
            stroke_width=1.5
        )
        return VGroup(bg, inner)

    # ─────────────────────────────────────────────
    # 场景6：片尾
    # ─────────────────────────────────────────────
    def scene_6_outro(self):
        # 淡出图表
        self.play(
            FadeOut(self.chart_cells),
            FadeOut(self.chart_nums),
            FadeOut(self.chart_title),
            run_time=0.6
        )

        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color="#6b7280"
        ).move_to(UP * 1.0)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=COLOR_GOLD
        ).move_to(DOWN * 0.2)

        summary = Text(
            "百数表：横同十位，竖同个位，斜差11",
            font="PingFang SC",
            font_size=22,
            color=COLOR_TEXT_NORMAL
        ).move_to(DOWN * 1.5)

        self.play(
            FadeOut(self.author_label),
            FadeIn(author_big, shift=DOWN * 0.3),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow_text, scale=1.05), run_time=0.5)
        self.play(FadeIn(summary, shift=UP * 0.2), run_time=0.4)

        # 小装饰：数字气泡
        bubble_data = [
            ("11", LEFT * 2.5 + DOWN * 3.2, COLOR_ROW_HIGHLIGHT),
            ("22", LEFT * 0.8 + DOWN * 3.8, COLOR_COL_HIGHLIGHT),
            ("33", RIGHT * 1.0 + DOWN * 3.2, COLOR_DIAG_HIGHLIGHT),
            ("44", RIGHT * 2.8 + DOWN * 3.8, COLOR_ACCENT),
            ("55", ORIGIN + DOWN * 4.5,       COLOR_GOLD),
        ]
        bubbles = VGroup()
        for txt, pos, col in bubble_data:
            circle = Circle(radius=0.35, fill_color=col, fill_opacity=0.7, stroke_width=0)
            label = Text(txt, font="PingFang SC", font_size=22, color=WHITE)
            bubble = VGroup(circle, label).move_to(pos)
            bubbles.add(bubble)

        self.play(
            LaggedStart(*[GrowFromCenter(b) for b in bubbles], lag_ratio=0.15),
            run_time=1.0
        )
        self.wait(1.5)

        self.play(
            FadeOut(author_big),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(summary),
            FadeOut(bubbles),
            run_time=0.8
        )
