"""
加法表整理 - 20以内的进位加法
目标受众: 一年级小学生
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
COLOR_9ROW = "#e74c3c"
COLOR_8ROW = "#3498db"
COLOR_7ROW = "#2ecc71"
COLOR_6ROW = "#9b59b6"
COLOR_HIGHLIGHT = "#f1c40f"
COLOR_RESULT = "#ffffff"
COLOR_PATTERN = "#e67e22"
COLOR_GRAY = "#95a5a6"


class AdditionTableLesson(Scene):
    """
    20以内进位加法表整理教学动画

    场景顺序:
    1. 开场钩子
    2. 引入9加几
    3. 展示8加几
    4. 展示7加几和6加几
    5. 完整加法表
    6. 发现规律
    7. 片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG

        self.scene_1_opening()
        self.scene_2_nine_plus()
        self.scene_3_eight_plus()
        self.scene_4_seven_six_plus()
        self.scene_5_full_table()
        self.scene_6_pattern()
        self.scene_7_outro()

    # ─────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        # 作者信息
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280",
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 大标题
        title = Text(
            "加法表整理",
            font="PingFang SC",
            font_size=52,
            color=COLOR_TITLE,
        ).move_to(UP * 5.8)

        subtitle = Text(
            "20以内的进位加法",
            font="PingFang SC",
            font_size=30,
            color=COLOR_GRAY,
        ).move_to(UP * 4.9)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.5)

        # 钩子问题
        hook = Text(
            "你能快速算出这些吗？",
            font="PingFang SC",
            font_size=32,
            color=COLOR_HIGHLIGHT,
        ).move_to(UP * 3.5)

        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.5)

        # 三个待计算算式
        f1 = MathTex(r"9 + 5 = ?", font_size=44, color=COLOR_9ROW).move_to(UP * 2.3)
        f2 = MathTex(r"8 + 7 = ?", font_size=44, color=COLOR_8ROW).move_to(UP * 1.4)
        f3 = MathTex(r"7 + 6 = ?", font_size=44, color=COLOR_7ROW).move_to(UP * 0.5)

        self.play(Write(f1), run_time=0.35)
        self.play(Write(f2), run_time=0.35)
        self.play(Write(f3), run_time=0.35)
        self.wait(0.8)

        # 显示答案
        a1 = MathTex(r"9 + 5 = 14", font_size=44, color=COLOR_9ROW).move_to(UP * 2.3)
        a2 = MathTex(r"8 + 7 = 15", font_size=44, color=COLOR_8ROW).move_to(UP * 1.4)
        a3 = MathTex(r"7 + 6 = 13", font_size=44, color=COLOR_7ROW).move_to(UP * 0.5)

        self.play(ReplacementTransform(f1, a1), run_time=0.3)
        self.play(ReplacementTransform(f2, a2), run_time=0.3)
        self.play(ReplacementTransform(f3, a3), run_time=0.3)
        self.wait(0.6)

        # 清场
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hook),
            FadeOut(a1),
            FadeOut(a2),
            FadeOut(a3),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 2: 9加几
    # ─────────────────────────────────────────────
    def scene_2_nine_plus(self):
        row_title = Text(
            "9 加几",
            font="PingFang SC",
            font_size=44,
            color=COLOR_9ROW,
        ).move_to(UP * 6.0)

        self.play(Write(row_title), run_time=0.6)

        explain = Text(
            "用凑十法：先凑成 10，再加余数",
            font="PingFang SC",
            font_size=24,
            color=COLOR_GRAY,
        ).move_to(UP * 5.1)

        self.play(FadeIn(explain), run_time=0.5)

        nine_data = [
            ("9+2", "=11"),
            ("9+3", "=12"),
            ("9+4", "=13"),
            ("9+5", "=14"),
            ("9+6", "=15"),
            ("9+7", "=16"),
            ("9+8", "=17"),
            ("9+9", "=18"),
        ]

        cards = self._build_equation_cards(nine_data, COLOR_9ROW, center_y=3.2)

        for card in cards:
            self.play(FadeIn(card, scale=0.85), run_time=0.15)

        self.wait(0.5)

        pattern_box = self._make_pattern_box(
            "结果：11, 12, 13 … 18",
            "加数每增加1，结果也增加1！",
        )
        self.play(FadeIn(pattern_box, shift=UP * 0.3), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(row_title),
            FadeOut(explain),
            FadeOut(VGroup(*cards)),
            FadeOut(pattern_box),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 3: 8加几
    # ─────────────────────────────────────────────
    def scene_3_eight_plus(self):
        row_title = Text(
            "8 加几",
            font="PingFang SC",
            font_size=44,
            color=COLOR_8ROW,
        ).move_to(UP * 6.0)

        self.play(Write(row_title), run_time=0.6)

        eight_data = [
            ("8+3", "=11"),
            ("8+4", "=12"),
            ("8+5", "=13"),
            ("8+6", "=14"),
            ("8+7", "=15"),
            ("8+8", "=16"),
            ("8+9", "=17"),
        ]

        cards = self._build_equation_cards(eight_data, COLOR_8ROW, center_y=3.2)

        for card in cards:
            self.play(FadeIn(card, scale=0.85), run_time=0.17)

        self.wait(0.5)

        pattern_box = self._make_pattern_box(
            "结果：11, 12, 13 … 17",
            "8 的进位加法比 9 少一行",
        )
        self.play(FadeIn(pattern_box, shift=UP * 0.3), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(row_title),
            FadeOut(VGroup(*cards)),
            FadeOut(pattern_box),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 4: 7加几 + 6加几
    # ─────────────────────────────────────────────
    def scene_4_seven_six_plus(self):
        # --- 7加几 ---
        row_title_7 = Text(
            "7 加几",
            font="PingFang SC",
            font_size=44,
            color=COLOR_7ROW,
        ).move_to(UP * 6.0)

        self.play(Write(row_title_7), run_time=0.5)

        seven_data = [
            ("7+4", "=11"),
            ("7+5", "=12"),
            ("7+6", "=13"),
            ("7+7", "=14"),
            ("7+8", "=15"),
            ("7+9", "=16"),
        ]
        cards_7 = self._build_equation_cards(seven_data, COLOR_7ROW, center_y=3.2)
        for card in cards_7:
            self.play(FadeIn(card, scale=0.85), run_time=0.18)
        self.wait(0.8)

        # --- 切换到 6加几 ---
        row_title_6 = Text(
            "6 加几",
            font="PingFang SC",
            font_size=44,
            color=COLOR_6ROW,
        ).move_to(UP * 6.0)

        self.play(
            ReplacementTransform(row_title_7, row_title_6),
            FadeOut(VGroup(*cards_7)),
            run_time=0.4,
        )

        six_data = [
            ("6+5", "=11"),
            ("6+6", "=12"),
            ("6+7", "=13"),
            ("6+8", "=14"),
            ("6+9", "=15"),
        ]
        cards_6 = self._build_equation_cards(six_data, COLOR_6ROW, center_y=3.2)
        for card in cards_6:
            self.play(FadeIn(card, scale=0.85), run_time=0.2)
        self.wait(0.8)

        self.play(
            FadeOut(row_title_6),
            FadeOut(VGroup(*cards_6)),
            run_time=0.5,
        )

    # ─────────────────────────────────────────────
    # Scene 5: 完整加法表
    # ─────────────────────────────────────────────
    def scene_5_full_table(self):
        title = Text(
            "完整加法表",
            font="PingFang SC",
            font_size=40,
            color=COLOR_TITLE,
        ).move_to(UP * 6.5)

        self.play(Write(title), run_time=0.6)

        # 表格数据：(行标签, [(算式, 结果)...], 颜色)
        table_data = [
            ("9+", [("9+2","11"),("9+3","12"),("9+4","13"),("9+5","14"),
                    ("9+6","15"),("9+7","16"),("9+8","17"),("9+9","18")], COLOR_9ROW),
            ("8+", [("8+3","11"),("8+4","12"),("8+5","13"),("8+6","14"),
                    ("8+7","15"),("8+8","16"),("8+9","17")], COLOR_8ROW),
            ("7+", [("7+4","11"),("7+5","12"),("7+6","13"),
                    ("7+7","14"),("7+8","15"),("7+9","16")], COLOR_7ROW),
            ("6+", [("6+5","11"),("6+6","12"),("6+7","13"),
                    ("6+8","14"),("6+9","15")], COLOR_6ROW),
        ]

        row_start_y = 5.2
        row_gap = 2.0
        all_row_groups = []

        for row_idx, (prefix, pairs, color) in enumerate(table_data):
            y_pos = row_start_y - row_idx * row_gap

            # 行标签
            label = Text(
                prefix,
                font="PingFang SC",
                font_size=24,
                color=color,
            ).move_to(np.array([-4.0, y_pos, 0]))

            # 每行格子
            n = len(pairs)
            total_w = 7.5
            cell_w = total_w / n
            x_start = -3.6 + cell_w * 0.5

            cells = VGroup()
            for j, (expr, res) in enumerate(pairs):
                x = x_start + j * cell_w

                bg = RoundedRectangle(
                    width=cell_w * 0.87,
                    height=1.7,
                    corner_radius=0.14,
                    color=color,
                    fill_opacity=0.18,
                    stroke_width=1.5,
                ).move_to(np.array([x, y_pos, 0]))

                eq_tex = MathTex(
                    expr,
                    font_size=22,
                    color=color,
                ).move_to(np.array([x, y_pos + 0.38, 0]))

                res_tex = MathTex(
                    "=" + res,
                    font_size=24,
                    color=COLOR_RESULT,
                ).move_to(np.array([x, y_pos - 0.38, 0]))

                cells.add(VGroup(bg, eq_tex, res_tex))

            row_group = VGroup(label, cells)
            all_row_groups.append(row_group)

        # 逐行显示
        for rg in all_row_groups:
            label = rg[0]
            cells = rg[1]
            self.play(FadeIn(label), run_time=0.2)
            for cell in cells:
                self.play(FadeIn(cell, scale=0.88), run_time=0.07)
            self.wait(0.05)

        self.wait(1.2)

        # 保存用于下一场景
        self.table_title = title
        self.all_row_groups = all_row_groups

    # ─────────────────────────────────────────────
    # Scene 6: 发现规律
    # ─────────────────────────────────────────────
    def scene_6_pattern(self):
        pattern_title = Text(
            "发现规律",
            font="PingFang SC",
            font_size=36,
            color=COLOR_PATTERN,
        ).move_to(UP * 6.5)

        self.play(
            ReplacementTransform(self.table_title, pattern_title),
            run_time=0.5,
        )

        # 规律①：每行都从11开始
        rule_1 = Text(
            "规律①：每行结果都从 11 开始",
            font="PingFang SC",
            font_size=24,
            color=COLOR_HIGHLIGHT,
        ).move_to(DOWN * 2.4)

        self.play(FadeIn(rule_1, shift=UP * 0.3), run_time=0.5)

        # 高亮每行第一格
        highlight_rects = []
        for rg in self.all_row_groups:
            cells = rg[1]
            if len(cells) > 0:
                hl = SurroundingRectangle(
                    cells[0],
                    color=COLOR_HIGHLIGHT,
                    buff=0.06,
                    stroke_width=3,
                )
                highlight_rects.append(hl)

        self.play(*[Create(hl) for hl in highlight_rects], run_time=0.5)
        self.wait(1.0)
        self.play(*[FadeOut(hl) for hl in highlight_rects], run_time=0.3)

        # 规律②：加数增大，结果增大
        rule_2 = Text(
            "规律②：加数每增加1，结果增加1",
            font="PingFang SC",
            font_size=24,
            color=COLOR_HIGHLIGHT,
        ).move_to(DOWN * 3.2)

        self.play(FadeIn(rule_2, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # 规律③：行数越来越少
        rule_3 = Text(
            "规律③：加数越小，算式越少",
            font="PingFang SC",
            font_size=24,
            color=COLOR_HIGHLIGHT,
        ).move_to(DOWN * 4.0)

        self.play(FadeIn(rule_3, shift=UP * 0.3), run_time=0.5)

        # 逐行 Indicate
        for rg in self.all_row_groups:
            cells = rg[1]
            self.play(Indicate(cells, color=COLOR_PATTERN, scale_factor=1.04), run_time=0.45)

        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(pattern_title),
            FadeOut(rule_1),
            FadeOut(rule_2),
            FadeOut(rule_3),
            *[FadeOut(rg) for rg in self.all_row_groups],
            run_time=0.6,
        )

    # ─────────────────────────────────────────────
    # Scene 7: 片尾
    # ─────────────────────────────────────────────
    def scene_7_outro(self):
        summary_title = Text(
            "记住这些加法口诀",
            font="PingFang SC",
            font_size=36,
            color=COLOR_TITLE,
        ).move_to(UP * 3.8)

        self.play(Write(summary_title), run_time=0.7)

        # 关键算式展示
        key_pairs = [
            ("9+2=11", COLOR_9ROW),
            ("8+3=11", COLOR_8ROW),
            ("7+4=11", COLOR_7ROW),
            ("6+5=11", COLOR_6ROW),
            ("9+9=18", COLOR_9ROW),
        ]

        formula_mobs = VGroup()
        for expr, color in key_pairs:
            formula_mobs.add(MathTex(expr, font_size=40, color=color))

        formula_mobs.arrange(DOWN, buff=0.38).move_to(UP * 1.5)

        for f in formula_mobs:
            self.play(FadeIn(f, scale=0.9), run_time=0.2)

        self.wait(0.6)

        # 鼓励语
        encourage = Text(
            "多练习，越来越快！",
            font="PingFang SC",
            font_size=32,
            color=COLOR_HIGHLIGHT,
        ).move_to(DOWN * 2.2)

        self.play(FadeIn(encourage, shift=UP * 0.3), run_time=0.5)

        follow_text = Text(
            "关注我，获得更多数学技巧!",
            font="PingFang SC",
            font_size=26,
            color=COLOR_GRAY,
        ).move_to(DOWN * 3.2)

        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)

        # 作者信息
        author_big = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=22,
            color="#6b7280",
        ).move_to(DOWN * 4.4)

        self.play(Transform(self.author, author_big), run_time=0.6)
        self.wait(2.0)

        # 全场淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(formula_mobs),
            FadeOut(encourage),
            FadeOut(follow_text),
            FadeOut(self.author),
            run_time=0.8,
        )

    # ─────────────────────────────────────────────
    # 辅助函数
    # ─────────────────────────────────────────────
    def _build_equation_cards(self, data, color, center_y=3.0):
        """
        构建一行等式卡片列表
        data: list of (expr_str, result_str)  e.g. ("9+2", "=11")
        """
        n = len(data)
        total_width = 8.2
        cell_w = total_width / n
        x_start = -4.1 + cell_w * 0.5

        cards = []
        for i, (expr, result) in enumerate(data):
            x = x_start + i * cell_w

            bg = RoundedRectangle(
                width=cell_w * 0.88,
                height=1.75,
                corner_radius=0.15,
                color=color,
                fill_opacity=0.18,
                stroke_width=1.8,
            ).move_to(np.array([x, center_y, 0]))

            eq_tex = MathTex(
                expr,
                font_size=26,
                color=color,
            ).move_to(np.array([x, center_y + 0.40, 0]))

            res_tex = MathTex(
                result,
                font_size=30,
                color=COLOR_RESULT,
            ).move_to(np.array([x, center_y - 0.42, 0]))

            cards.append(VGroup(bg, eq_tex, res_tex))

        return cards

    def _make_pattern_box(self, line1_str, line2_str):
        """构建规律提示框"""
        line1 = Text(
            line1_str,
            font="PingFang SC",
            font_size=24,
            color=COLOR_HIGHLIGHT,
        )
        line2 = Text(
            line2_str,
            font="PingFang SC",
            font_size=20,
            color=COLOR_GRAY,
        )
        content = VGroup(line1, line2).arrange(DOWN, buff=0.22)

        box = SurroundingRectangle(
            content,
            color=COLOR_PATTERN,
            fill_color=COLOR_BG,
            fill_opacity=0.85,
            buff=0.28,
            stroke_width=2,
        )

        group = VGroup(box, content)
        group.move_to(DOWN * 3.8)
        return group
