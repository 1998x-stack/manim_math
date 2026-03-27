"""
位置的表示方法(数对) - Coordinate Pair Lesson
四年级第二学期 第五章整理与提高
用数对确定位置，初步接触直角坐标系思想

格式: TikTok竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# TikTok 竖屏配置
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class CoordinatePairLesson(Scene):
    """
    数对教学动画
    场景顺序:
    1. 开场钩子
    2. 认识行与列
    3. 数对的写法
    4. 在格子里标点
    5. 读出数对
    6. 关键规则强调
    7. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.C_GRID = "#334155"
        self.C_ROW = "#3b82f6"       # 蓝色 - 行
        self.C_COL = "#f59e0b"       # 橙色 - 列
        self.C_DOT = "#ef4444"       # 红色 - 点
        self.C_PAIR = "#10b981"      # 绿色 - 数对
        self.C_HIGHLIGHT = "#fbbf24"
        self.C_TEXT = "#e2e8f0"

        # 网格参数（主内容区域居中）
        self.GRID_COLS = 6
        self.GRID_ROWS = 5
        self.CELL = 0.95             # 格子大小
        self.GRID_ORIGIN = np.array([-2.5, -1.2, 0])  # 左下角

        self.scene_1_opening()
        self.scene_2_grid_intro()
        self.scene_3_pair_notation()
        self.scene_4_mark_points()
        self.scene_5_read_pairs()
        self.scene_6_key_rule()
        self.scene_7_outro()

    # ─────────────────────────────────────────────
    # 辅助：网格坐标 -> Manim坐标
    # ─────────────────────────────────────────────
    def grid_pos(self, col, row):
        """col: 1-indexed, row: 1-indexed (bottom=1). 返回格子中心。"""
        x = self.GRID_ORIGIN[0] + (col - 0.5) * self.CELL
        y = self.GRID_ORIGIN[1] + (row - 0.5) * self.CELL
        return np.array([x, y, 0])

    def build_grid(self):
        """构建基础网格 VGroup"""
        lines = VGroup()
        # 竖线
        for c in range(self.GRID_COLS + 1):
            x = self.GRID_ORIGIN[0] + c * self.CELL
            y0 = self.GRID_ORIGIN[1]
            y1 = y0 + self.GRID_ROWS * self.CELL
            lines.add(Line(
                np.array([x, y0, 0]), np.array([x, y1, 0]),
                color=self.C_GRID, stroke_width=1.5
            ))
        # 横线
        for r in range(self.GRID_ROWS + 1):
            y = self.GRID_ORIGIN[1] + r * self.CELL
            x0 = self.GRID_ORIGIN[0]
            x1 = x0 + self.GRID_COLS * self.CELL
            lines.add(Line(
                np.array([x0, y, 0]), np.array([x1, y, 0]),
                color=self.C_GRID, stroke_width=1.5
            ))
        return lines

    def col_labels(self):
        """底部列标签 1-6"""
        labels = VGroup()
        for i in range(1, self.GRID_COLS + 1):
            x = self.GRID_ORIGIN[0] + (i - 0.5) * self.CELL
            y = self.GRID_ORIGIN[1] - 0.48
            lbl = Text(str(i), font="Noto Sans CJK SC", font_size=22, color=self.C_COL)
            lbl.move_to(np.array([x, y, 0]))
            labels.add(lbl)
        return labels

    def row_labels(self):
        """左侧行标签 1-5（从下往上）"""
        labels = VGroup()
        for i in range(1, self.GRID_ROWS + 1):
            x = self.GRID_ORIGIN[0] - 0.48
            y = self.GRID_ORIGIN[1] + (i - 0.5) * self.CELL
            lbl = Text(str(i), font="Noto Sans CJK SC", font_size=22, color=self.C_ROW)
            lbl.move_to(np.array([x, y, 0]))
            labels.add(lbl)
        return labels

    # ─────────────────────────────────────────────
    # 场景 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_1_opening(self):
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(author)
        self.author = author

        title = Text(
            "如何用数字表示位置?",
            font="Noto Sans CJK SC",
            font_size=40,
            color=self.C_HIGHLIGHT
        ).move_to(UP * 5.8)

        subtitle = Text(
            "数对的秘密",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.C_TEXT
        ).move_to(UP * 5.0)

        self.play(Write(title), run_time=0.9)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)

        # 钩子示例框
        hook_bg = Rectangle(
            width=5.0, height=1.5,
            color=self.C_PAIR,
            fill_color="#071a12",
            fill_opacity=0.9,
            stroke_width=2
        ).move_to(UP * 3.6)

        hook_t1 = Text("班级座位", font="Noto Sans CJK SC",
                       font_size=22, color=self.C_TEXT).move_to(UP * 3.95)
        hook_t2 = Text("第3列  第2行", font="Noto Sans CJK SC",
                       font_size=28, color=self.C_HIGHLIGHT).move_to(UP * 3.4)

        self.play(FadeIn(hook_bg), run_time=0.3)
        self.play(FadeIn(hook_t1), FadeIn(hook_t2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(hook_bg), FadeOut(hook_t1), FadeOut(hook_t2),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # 场景 2: 认识行与列
    # ─────────────────────────────────────────────
    def scene_2_grid_intro(self):
        title = Text("认识行和列", font="Noto Sans CJK SC",
                     font_size=36, color=self.C_HIGHLIGHT).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.7)

        # 建立网格
        grid = self.build_grid()
        self.play(Create(grid), run_time=1.0)

        # ── 列说明（左侧箭头）
        col_arrow_x = self.GRID_ORIGIN[0] - 0.85
        col_arrow_y_top = self.GRID_ORIGIN[1] + self.GRID_ROWS * self.CELL
        col_arrow_y_bot = self.GRID_ORIGIN[1]

        col_arrow = Arrow(
            start=np.array([col_arrow_x, col_arrow_y_top, 0]),
            end=np.array([col_arrow_x, col_arrow_y_bot, 0]),
            color=self.C_COL, stroke_width=3,
            max_tip_length_to_length_ratio=0.1
        )
        col_label = Text("列", font="Noto Sans CJK SC",
                         font_size=28, color=self.C_COL).move_to(
            np.array([col_arrow_x - 0.38, (col_arrow_y_top + col_arrow_y_bot) / 2, 0])
        )
        col_tip = Text("从左到右\n第1列、第2列…", font="Noto Sans CJK SC",
                       font_size=20, color=self.C_COL).move_to(UP * 3.4)

        self.play(Create(col_arrow), Write(col_label), run_time=0.6)
        self.play(FadeIn(col_tip), run_time=0.5)

        c_labels = self.col_labels()
        self.play(FadeIn(c_labels), run_time=0.4)
        self.wait(0.8)

        # ── 行说明（底部箭头）
        row_arrow_y = self.GRID_ORIGIN[1] - 0.85
        row_arrow_x_left = self.GRID_ORIGIN[0]
        row_arrow_x_right = self.GRID_ORIGIN[0] + self.GRID_COLS * self.CELL

        row_arrow = Arrow(
            start=np.array([row_arrow_x_left, row_arrow_y, 0]),
            end=np.array([row_arrow_x_right, row_arrow_y, 0]),
            color=self.C_ROW, stroke_width=3,
            max_tip_length_to_length_ratio=0.08
        )
        row_label = Text("行", font="Noto Sans CJK SC",
                         font_size=28, color=self.C_ROW).move_to(
            np.array([(row_arrow_x_left + row_arrow_x_right) / 2, row_arrow_y - 0.4, 0])
        )
        row_tip = Text("从下到上\n第1行、第2行…", font="Noto Sans CJK SC",
                       font_size=20, color=self.C_ROW).move_to(DOWN * 3.2)

        self.play(FadeOut(col_tip), run_time=0.3)
        self.play(Create(row_arrow), Write(row_label), run_time=0.6)
        self.play(FadeIn(row_tip), run_time=0.5)

        r_labels = self.row_labels()
        self.play(FadeIn(r_labels), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title),
            FadeOut(col_arrow), FadeOut(col_label),
            FadeOut(row_arrow), FadeOut(row_label),
            FadeOut(row_tip),
            run_time=0.5
        )

        # 保留 grid, 标签
        self.grid = grid
        self.c_labels = c_labels
        self.r_labels = r_labels

    # ─────────────────────────────────────────────
    # 场景 3: 数对的写法
    # ─────────────────────────────────────────────
    def scene_3_pair_notation(self):
        title = Text("数对怎么写?", font="Noto Sans CJK SC",
                     font_size=36, color=self.C_HIGHLIGHT).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 公式框
        rule_bg = Rectangle(
            width=5.5, height=1.7,
            color=self.C_PAIR,
            fill_color="#071a12",
            fill_opacity=0.85,
            stroke_width=2
        ).move_to(UP * 4.55)

        rule_line1 = Text("(列, 行)", font="Noto Sans CJK SC",
                          font_size=36, color=self.C_PAIR).move_to(UP * 4.8)
        rule_line2 = Text("列 在 前，行 在 后", font="Noto Sans CJK SC",
                          font_size=22, color=self.C_TEXT).move_to(UP * 4.25)

        self.play(FadeIn(rule_bg), run_time=0.3)
        self.play(Write(rule_line1), run_time=0.6)
        self.play(FadeIn(rule_line2), run_time=0.4)

        example_title = Text("例：第3列第2行", font="Noto Sans CJK SC",
                             font_size=26, color=self.C_TEXT).move_to(UP * 3.35)
        self.play(FadeIn(example_title), run_time=0.4)

        # 高亮第3列（矩形）
        col3_rect = Rectangle(
            width=self.CELL,
            height=self.GRID_ROWS * self.CELL,
            color=self.C_COL,
            fill_color=self.C_COL,
            fill_opacity=0.18,
            stroke_width=0
        ).move_to(np.array([
            self.GRID_ORIGIN[0] + (3 - 0.5) * self.CELL,
            self.GRID_ORIGIN[1] + self.GRID_ROWS * self.CELL / 2,
            0
        ]))
        col3_tip = Text("第3列", font="Noto Sans CJK SC",
                        font_size=22, color=self.C_COL).move_to(np.array([
            self.GRID_ORIGIN[0] + 2.5 * self.CELL,
            self.GRID_ORIGIN[1] + self.GRID_ROWS * self.CELL + 0.42,
            0
        ]))

        self.play(FadeIn(col3_rect), FadeIn(col3_tip), run_time=0.5)
        self.wait(0.4)

        # 高亮第2行（矩形）
        row2_rect = Rectangle(
            width=self.GRID_COLS * self.CELL,
            height=self.CELL,
            color=self.C_ROW,
            fill_color=self.C_ROW,
            fill_opacity=0.18,
            stroke_width=0
        ).move_to(np.array([
            self.GRID_ORIGIN[0] + self.GRID_COLS * self.CELL / 2,
            self.GRID_ORIGIN[1] + (2 - 0.5) * self.CELL,
            0
        ]))
        row2_tip = Text("第2行", font="Noto Sans CJK SC",
                        font_size=22, color=self.C_ROW).move_to(np.array([
            self.GRID_ORIGIN[0] - 0.92,
            self.GRID_ORIGIN[1] + 1.5 * self.CELL,
            0
        ]))

        self.play(FadeIn(row2_rect), FadeIn(row2_tip), run_time=0.5)
        self.wait(0.4)

        # 交叉点
        dot_32 = Dot(self.grid_pos(3, 2), radius=0.18, color=self.C_DOT)
        self.play(FadeIn(dot_32, scale=0.5), run_time=0.4)
        self.play(Flash(dot_32, color=self.C_DOT, flash_radius=0.35), run_time=0.4)

        # 数对
        pair_text = Text("数对：(3, 2)", font="Noto Sans CJK SC",
                         font_size=32, color=self.C_PAIR).move_to(DOWN * 3.2)
        self.play(Write(pair_text), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(example_title),
            FadeOut(col3_rect), FadeOut(col3_tip),
            FadeOut(row2_rect), FadeOut(row2_tip),
            FadeOut(pair_text),
            FadeOut(rule_bg), FadeOut(rule_line1), FadeOut(rule_line2),
            run_time=0.5
        )

        self.dot_32 = dot_32  # 保留红点

    # ─────────────────────────────────────────────
    # 场景 4: 在格子里标多个点
    # ─────────────────────────────────────────────
    def scene_4_mark_points(self):
        title = Text("在格子里找位置", font="Noto Sans CJK SC",
                     font_size=36, color=self.C_HIGHLIGHT).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 要标注的点 (col, row, label_str, color)
        points_data = [
            (3, 2, "(3, 2)", self.C_DOT),
            (1, 4, "(1, 4)", "#a78bfa"),
            (5, 1, "(5, 1)", "#34d399"),
            (4, 5, "(4, 5)", "#fb923c"),
            (6, 3, "(6, 3)", "#60a5fa"),
        ]

        dot_objs = [self.dot_32]
        label_objs = []

        # (3,2) 的标签
        lbl_32 = Text("(3, 2)", font="Noto Sans CJK SC",
                      font_size=19, color=self.C_DOT).next_to(self.dot_32, UR, buff=0.1)
        self.play(FadeIn(lbl_32), run_time=0.3)
        label_objs.append(lbl_32)

        # 其余点
        for idx, (col, row, lbl_str, col_color) in enumerate(points_data[1:], start=1):
            pos = self.grid_pos(col, row)
            dot = Dot(pos, radius=0.15, color=col_color)
            direction = UR if col <= 4 else UL
            lbl = Text(lbl_str, font="Noto Sans CJK SC",
                       font_size=19, color=col_color).next_to(dot, direction, buff=0.10)
            self.play(FadeIn(dot, scale=0.5), FadeIn(lbl), run_time=0.4)
            dot_objs.append(dot)
            label_objs.append(lbl)
            self.wait(0.25)

        self.wait(1.2)

        self.play(
            FadeOut(title),
            *[FadeOut(d) for d in dot_objs],
            *[FadeOut(l) for l in label_objs],
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # 场景 5: 读出数对（交互式演示）
    # ─────────────────────────────────────────────
    def scene_5_read_pairs(self):
        title = Text("读出这个点的数对", font="Noto Sans CJK SC",
                     font_size=36, color=self.C_HIGHLIGHT).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.6)

        # 放置目标点 (4, 3)
        target_col, target_row = 4, 3
        target_pos = self.grid_pos(target_col, target_row)
        target_dot = Dot(target_pos, radius=0.22, color=self.C_DOT)

        self.play(FadeIn(target_dot, scale=0.5), run_time=0.5)
        self.play(Flash(target_dot, color=self.C_HIGHLIGHT, flash_radius=0.42), run_time=0.5)

        question = Text("这个点是第几列第几行?", font="Noto Sans CJK SC",
                        font_size=26, color=self.C_TEXT).move_to(DOWN * 3.0)
        self.play(FadeIn(question), run_time=0.5)
        self.wait(0.8)

        # 步骤1: 找列
        step1 = Text("第一步: 数列 (左→右)", font="Noto Sans CJK SC",
                     font_size=24, color=self.C_COL).move_to(DOWN * 3.0)
        self.play(ReplacementTransform(question, step1), run_time=0.4)

        # 竖线从左边扫过
        init_x = self.GRID_ORIGIN[0]
        scan_v = DashedLine(
            np.array([init_x, self.GRID_ORIGIN[1] + self.GRID_ROWS * self.CELL + 0.2, 0]),
            np.array([init_x, self.GRID_ORIGIN[1] - 0.2, 0]),
            color=self.C_COL, dash_length=0.12, stroke_width=3
        )
        self.play(Create(scan_v), run_time=0.3)

        target_x = self.GRID_ORIGIN[0] + (target_col - 0.5) * self.CELL
        self.play(
            scan_v.animate.shift(RIGHT * (target_x - init_x)),
            run_time=0.7, rate_func=smooth
        )

        col_mark = Text("第4列", font="Noto Sans CJK SC",
                        font_size=26, color=self.C_COL).move_to(np.array([
            target_x,
            self.GRID_ORIGIN[1] + self.GRID_ROWS * self.CELL + 0.5,
            0
        ]))
        self.play(FadeIn(col_mark), run_time=0.4)
        self.wait(0.5)

        # 步骤2: 找行
        step2 = Text("第二步: 数行 (下→上)", font="Noto Sans CJK SC",
                     font_size=24, color=self.C_ROW).move_to(DOWN * 3.0)
        self.play(ReplacementTransform(step1, step2), run_time=0.4)

        init_y = self.GRID_ORIGIN[1]
        scan_h = DashedLine(
            np.array([self.GRID_ORIGIN[0] - 0.2, init_y, 0]),
            np.array([self.GRID_ORIGIN[0] + self.GRID_COLS * self.CELL + 0.2, init_y, 0]),
            color=self.C_ROW, dash_length=0.12, stroke_width=3
        )
        self.play(Create(scan_h), run_time=0.3)

        target_y = self.GRID_ORIGIN[1] + (target_row - 0.5) * self.CELL
        self.play(
            scan_h.animate.shift(UP * (target_y - init_y)),
            run_time=0.7, rate_func=smooth
        )

        row_mark = Text("第3行", font="Noto Sans CJK SC",
                        font_size=26, color=self.C_ROW).move_to(np.array([
            self.GRID_ORIGIN[0] - 1.05, target_y, 0
        ]))
        self.play(FadeIn(row_mark), run_time=0.4)
        self.wait(0.5)

        self.play(FadeOut(step2), run_time=0.3)

        result = Text("数对是：(4, 3)", font="Noto Sans CJK SC",
                      font_size=34, color=self.C_PAIR).move_to(DOWN * 3.2)
        self.play(Write(result), run_time=0.7)
        self.play(Indicate(target_dot, scale_factor=1.5, color=self.C_PAIR), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(target_dot),
            FadeOut(scan_v), FadeOut(scan_h),
            FadeOut(col_mark), FadeOut(row_mark),
            FadeOut(result),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # 场景 6: 关键规则强调
    # ─────────────────────────────────────────────
    def scene_6_key_rule(self):
        # 清理网格
        self.play(
            FadeOut(self.grid),
            FadeOut(self.c_labels),
            FadeOut(self.r_labels),
            run_time=0.4
        )

        title = Text("记住这个规则！", font="Noto Sans CJK SC",
                     font_size=40, color=self.C_HIGHLIGHT).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        # 主规则卡片
        main_bg = Rectangle(
            width=7.0, height=4.0,
            color=self.C_PAIR,
            fill_color="#071a12",
            fill_opacity=0.9,
            stroke_width=2.5
        ).move_to(UP * 2.6)

        rule_big = Text("(列, 行)", font="Noto Sans CJK SC",
                        font_size=56, color=self.C_PAIR).move_to(UP * 3.3)

        col_note = Text("列 在 前", font="Noto Sans CJK SC",
                        font_size=30, color=self.C_COL).move_to(UP * 2.4)
        row_note = Text("行 在 后", font="Noto Sans CJK SC",
                        font_size=30, color=self.C_ROW).move_to(UP * 1.9)
        bracket_note = Text("括号括起来，逗号隔开", font="Noto Sans CJK SC",
                            font_size=22, color=self.C_TEXT).move_to(UP * 1.35)

        self.play(FadeIn(main_bg), run_time=0.3)
        self.play(Write(rule_big), run_time=0.7)
        self.play(FadeIn(col_note), run_time=0.4)
        self.play(FadeIn(row_note), run_time=0.4)
        self.play(FadeIn(bracket_note), run_time=0.4)

        # 例子
        ex1 = Text("(3, 2) → 第3列  第2行", font="Noto Sans CJK SC",
                   font_size=26, color=self.C_TEXT).move_to(UP * 0.1)
        ex2 = Text("(1, 5) → 第1列  第5行", font="Noto Sans CJK SC",
                   font_size=26, color=self.C_TEXT).move_to(DOWN * 0.6)
        ex3 = Text("(6, 3) → 第6列  第3行", font="Noto Sans CJK SC",
                   font_size=26, color=self.C_TEXT).move_to(DOWN * 1.3)

        self.play(FadeIn(ex1), run_time=0.4)
        self.play(FadeIn(ex2), run_time=0.4)
        self.play(FadeIn(ex3), run_time=0.4)
        self.wait(0.5)

        # 警示框
        warn_bg = Rectangle(
            width=6.8, height=1.4,
            color="#ef4444",
            fill_color="#1a0505",
            fill_opacity=0.85,
            stroke_width=2
        ).move_to(DOWN * 2.8)

        warn_text = Text("注意：列在前，行在后", font="Noto Sans CJK SC",
                         font_size=28, color="#ef4444").move_to(DOWN * 2.8)

        self.play(FadeIn(warn_bg), run_time=0.3)
        self.play(Write(warn_text), run_time=0.5)

        for _ in range(2):
            self.play(warn_text.animate.set_color(self.C_HIGHLIGHT), run_time=0.25)
            self.play(warn_text.animate.set_color("#ef4444"), run_time=0.25)

        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(main_bg),
            FadeOut(rule_big), FadeOut(col_note), FadeOut(row_note), FadeOut(bracket_note),
            FadeOut(ex1), FadeOut(ex2), FadeOut(ex3),
            FadeOut(warn_bg), FadeOut(warn_text),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # 场景 7: 片尾
    # ─────────────────────────────────────────────
    def scene_7_outro(self):
        summary = Text("数对 = (列, 行)", font="Noto Sans CJK SC",
                       font_size=48, color=self.C_PAIR).move_to(UP * 2.5)
        sub1 = Text("列 在 前", font="Noto Sans CJK SC",
                    font_size=30, color=self.C_COL).move_to(UP * 1.45)
        sub2 = Text("行 在 后", font="Noto Sans CJK SC",
                    font_size=30, color=self.C_ROW).move_to(UP * 0.75)

        self.play(Write(summary), run_time=0.8)
        self.play(FadeIn(sub1), FadeIn(sub2), run_time=0.5)
        self.wait(0.5)

        author_big = Text("上海初高中数学直通车", font="Noto Sans CJK SC",
                          font_size=34, color=WHITE).move_to(DOWN * 0.8)
        author_id = Text("@emptyandcalm", font="Noto Sans CJK SC",
                         font_size=28, color="#6b7280").move_to(DOWN * 1.6)
        follow = Text("关注我，学更多数学技巧！", font="Noto Sans CJK SC",
                      font_size=30, color=self.C_HIGHLIGHT).move_to(DOWN * 2.7)

        self.play(FadeIn(author_big), run_time=0.5)
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 装饰点环绕
        num_dots = 8
        orbit_center = DOWN * 5.0
        orbit_r = 2.6
        dot_colors = [self.C_COL, self.C_ROW, self.C_DOT, self.C_PAIR,
                      self.C_HIGHLIGHT, self.C_COL, self.C_ROW, self.C_PAIR]

        dec_dots = VGroup(*[
            Dot(
                np.array([
                    orbit_r * np.cos(i * TAU / num_dots),
                    orbit_r * np.sin(i * TAU / num_dots),
                    0
                ]) + orbit_center,
                radius=0.12,
                color=dot_colors[i]
            )
            for i in range(num_dots)
        ])

        self.play(*[FadeIn(d, scale=0.3) for d in dec_dots], run_time=0.6)
        self.play(Rotate(dec_dots, angle=TAU, about_point=orbit_center), run_time=2.0)
        self.wait(1.0)
