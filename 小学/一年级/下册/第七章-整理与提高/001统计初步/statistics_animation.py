"""
一年级统计初步 - 象形统计图教学动画
Statistics Introduction for Grade 1 - Pictograph Teaching Animation

知识点: 用象形统计图整理数据，每格代表1人
目标: 会看图回答"谁最多/最少/一共多少"
格式: TikTok 竖屏 1080×1920
"""

from manim import *
import numpy as np

# ===== 全局配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ===== 颜色配置 =====
BG_COLOR = "#1a1a2e"
COLOR_APPLE = "#e74c3c"
COLOR_BANANA = "#f1c40f"
COLOR_ORANGE = "#e67e22"
COLOR_GRAPE = "#9b59b6"
COLOR_HIGHLIGHT = "#f9ca24"
COLOR_TABLE_BG = "#16213e"
COLOR_TABLE_LINE = "#0f3460"
COLOR_GRID_LINE = "#2d3561"

FRUIT_COLORS = [COLOR_APPLE, COLOR_BANANA, COLOR_ORANGE, COLOR_GRAPE]
FRUIT_NAMES = ["苹果", "香蕉", "橙子", "葡萄"]
FRUIT_DATA = [5, 3, 4, 6]

# ===== 图表布局参数（经过 verify_geometry.py 验证）=====
CHART_ORIGIN_X = -3.0
CHART_ORIGIN_Y = -3.5   # 图表底部 y（主内容区）
COL_WIDTH = 1.8
ROW_HEIGHT = 0.72
NUM_FRUITS = 4
MAX_COUNT = max(FRUIT_DATA)  # 6

AUTHOR_FONT = "PingFang SC"


def make_fruit_icon(color, size=0.28):
    """创建水果图标（用填充圆圈+颜色区分）"""
    circle = Circle(radius=size, fill_color=color, fill_opacity=1.0, stroke_width=2, stroke_color=WHITE)
    return circle


def make_star_icon(color, size=0.25):
    """创建☆图标代表1人（用五角星）"""
    star = Star(n=5, outer_radius=size, inner_radius=size * 0.4,
                fill_color=color, fill_opacity=1.0,
                stroke_width=1.5, stroke_color=WHITE)
    return star


class StatisticsAnimation(Scene):
    """一年级统计初步 - 象形统计图"""

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者信息（贯穿全程）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=AUTHOR_FONT,
            font_size=18,
            color=GRAY_B
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # 执行各场景
        self.scene_1_hook()
        self.scene_2_raw_data()
        self.scene_3_table()
        self.scene_4_pictograph()
        self.scene_5_questions()
        self.scene_6_outro()

    # ─────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────
    def scene_1_hook(self):
        # 主标题
        title = Text(
            "你最喜欢\n哪种水果？",
            font=AUTHOR_FONT,
            font_size=52,
            color=COLOR_HIGHLIGHT,
            line_spacing=1.3
        ).move_to(UP * 5.2)

        self.play(Write(title), run_time=1.0)
        self.wait(0.3)

        # 四个水果图标弹出
        icons_group = VGroup()
        icon_positions = [
            np.array([-2.8, 2.8, 0]),
            np.array([-0.9, 2.8, 0]),
            np.array([0.9, 2.8, 0]),
            np.array([2.8, 2.8, 0]),
        ]
        labels_group = VGroup()

        for i, (name, color, pos) in enumerate(zip(FRUIT_NAMES, FRUIT_COLORS, icon_positions)):
            icon = make_fruit_icon(color, size=0.55)
            icon.move_to(pos)
            label = Text(name, font=AUTHOR_FONT, font_size=22, color=color)
            label.next_to(icon, DOWN, buff=0.15)
            icons_group.add(icon)
            labels_group.add(label)
            self.play(
                FadeIn(icon, scale=0.3),
                FadeIn(label),
                run_time=0.35
            )

        self.wait(0.6)

        # 引出统计
        call_text = Text(
            "让我们来统计一下！",
            font=AUTHOR_FONT,
            font_size=36,
            color=WHITE
        ).move_to(UP * 1.5)

        self.play(FadeIn(call_text, shift=UP * 0.4, scale=1.1), run_time=0.6)
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(title),
            FadeOut(icons_group),
            FadeOut(labels_group),
            FadeOut(call_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # Scene 2: 展示原始数据（小圆点代表每个学生）
    # ─────────────────────────────────────────────
    def scene_2_raw_data(self):
        title = Text(
            "班级调查结果",
            font=AUTHOR_FONT,
            font_size=38,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 6.3)

        self.play(Write(title), run_time=0.6)

        # 每行展示水果名 + 对应数量的小圆点
        row_y_start = 4.0
        row_gap = 1.3
        all_dots = VGroup()
        all_fruit_labels = VGroup()

        for i, (name, color, count) in enumerate(zip(FRUIT_NAMES, FRUIT_COLORS, FRUIT_DATA)):
            row_y = row_y_start - i * row_gap

            # 水果标签
            fruit_icon = make_fruit_icon(color, size=0.3)
            fruit_icon.move_to(np.array([-3.8, row_y, 0]))
            fruit_label = Text(name, font=AUTHOR_FONT, font_size=26, color=color)
            fruit_label.next_to(fruit_icon, RIGHT, buff=0.2)

            self.play(FadeIn(fruit_icon), FadeIn(fruit_label), run_time=0.3)
            all_fruit_labels.add(fruit_icon, fruit_label)

            # 小圆点（每个代表1个学生）
            dot_start_x = -1.8
            dot_spacing = 0.65
            row_dots = VGroup()
            for j in range(count):
                dot = Dot(
                    point=np.array([dot_start_x + j * dot_spacing, row_y, 0]),
                    radius=0.2,
                    color=color,
                    fill_opacity=0.9
                )
                row_dots.add(dot)
                all_dots.add(dot)

            self.play(
                LaggedStart(*[FadeIn(d, scale=0.4) for d in row_dots], lag_ratio=0.15),
                run_time=0.6
            )

        self.wait(0.5)

        # 感叹：好乱！
        messy_text = Text(
            "好乱啊，怎么数清楚呢？",
            font=AUTHOR_FONT,
            font_size=30,
            color=YELLOW
        ).move_to(DOWN * 3.0)

        self.play(FadeIn(messy_text, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        # 提示
        hint_text = Text(
            "用统计表整理一下！",
            font=AUTHOR_FONT,
            font_size=32,
            color=GREEN
        ).move_to(DOWN * 4.5)

        self.play(FadeIn(hint_text, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(title),
            FadeOut(all_dots),
            FadeOut(all_fruit_labels),
            FadeOut(messy_text),
            FadeOut(hint_text),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # Scene 3: 建立统计表
    # ─────────────────────────────────────────────
    def scene_3_table(self):
        title = Text(
            "统计表",
            font=AUTHOR_FONT,
            font_size=40,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 6.3)

        self.play(Write(title), run_time=0.5)

        # 表格参数
        # 2行（表头+数据）+ 1列标题 + 4列水果 + 1列合计
        # 用 Rectangle 手工绘制

        table_x_start = -3.8
        table_y_start = 4.5
        col_w = [1.5, 1.3, 1.3, 1.3, 1.3, 1.4]   # 宽度：项目列 + 4水果 + 合计
        row_h = [0.85, 0.85, 0.85]                  # 高度：3行（名称/人数/合计）

        num_cols = len(col_w)
        num_rows = len(row_h)

        # 计算各列 x 中心
        col_x_centers = []
        x = table_x_start
        for w in col_w:
            col_x_centers.append(x + w / 2)
            x += w

        # 计算各行 y 中心
        row_y_centers = []
        y = table_y_start
        for h in row_h:
            row_y_centers.append(y - h / 2)
            y -= h

        total_width = sum(col_w)
        total_height = sum(row_h)

        # 绘制表格框
        table_cells = VGroup()
        for row in range(num_rows):
            for col in range(num_cols):
                cell_x = table_x_start + sum(col_w[:col]) + col_w[col] / 2
                cell_y = table_y_start - sum(row_h[:row]) - row_h[row] / 2
                cell = Rectangle(
                    width=col_w[col],
                    height=row_h[row],
                    color=COLOR_TABLE_LINE,
                    stroke_width=2,
                    fill_color=COLOR_TABLE_BG,
                    fill_opacity=1.0
                ).move_to(np.array([cell_x, cell_y, 0]))
                table_cells.add(cell)

        self.play(Create(table_cells), run_time=0.8)

        # 填入表头（第一行）
        # 第一格：空白（项目）
        header_label = Text("项目", font=AUTHOR_FONT, font_size=22, color=GRAY_A)
        header_label.move_to(np.array([col_x_centers[0], row_y_centers[0], 0]))

        fruit_headers = VGroup()
        for i, (name, color) in enumerate(zip(FRUIT_NAMES, FRUIT_COLORS)):
            icon = make_fruit_icon(color, size=0.22)
            label = Text(name, font=AUTHOR_FONT, font_size=20, color=color)
            group = VGroup(icon, label).arrange(DOWN, buff=0.05)
            group.move_to(np.array([col_x_centers[i + 1], row_y_centers[0], 0]))
            fruit_headers.add(group)

        total_header = Text("合计", font=AUTHOR_FONT, font_size=22, color=WHITE)
        total_header.move_to(np.array([col_x_centers[5], row_y_centers[0], 0]))

        self.play(
            FadeIn(header_label),
            LaggedStart(*[FadeIn(h) for h in fruit_headers], lag_ratio=0.15),
            FadeIn(total_header),
            run_time=0.8
        )

        # 填入行标签（第二行第一格）
        row_label_count = Text("人数", font=AUTHOR_FONT, font_size=22, color=GRAY_A)
        row_label_count.move_to(np.array([col_x_centers[0], row_y_centers[1], 0]))
        self.play(FadeIn(row_label_count), run_time=0.3)

        # 逐个填入数字（第二行）
        data_numbers = VGroup()
        for i, (count, color) in enumerate(zip(FRUIT_DATA, FRUIT_COLORS)):
            num_text = Text(str(count), font=AUTHOR_FONT, font_size=32, color=color)
            num_text.move_to(np.array([col_x_centers[i + 1], row_y_centers[1], 0]))
            data_numbers.add(num_text)

            # 高亮格子
            highlight_cell = Rectangle(
                width=col_w[i + 1],
                height=row_h[1],
                color=color,
                stroke_width=3,
                fill_color=color,
                fill_opacity=0.2
            ).move_to(np.array([col_x_centers[i + 1], row_y_centers[1], 0]))

            self.play(
                FadeIn(highlight_cell, scale=0.5),
                FadeIn(num_text, scale=0.5),
                run_time=0.4
            )
            self.play(FadeOut(highlight_cell), run_time=0.2)

        # 合计行（第三行）
        total_label = Text("合计", font=AUTHOR_FONT, font_size=22, color=GRAY_A)
        total_label.move_to(np.array([col_x_centers[0], row_y_centers[2], 0]))

        total_num = Text(str(sum(FRUIT_DATA)), font=AUTHOR_FONT, font_size=34, color=COLOR_HIGHLIGHT)
        total_num.move_to(np.array([col_x_centers[5], row_y_centers[2], 0]))

        # 合计行等号动画
        formula_parts = []
        x_pos = -2.6
        formula_y = row_y_centers[2]
        for i, count in enumerate(FRUIT_DATA):
            t = Text(str(count), font=AUTHOR_FONT, font_size=22, color=FRUIT_COLORS[i])
            t.move_to(np.array([x_pos, formula_y, 0]))
            formula_parts.append(t)
            x_pos += 0.55
            if i < len(FRUIT_DATA) - 1:
                plus = Text("+", font=AUTHOR_FONT, font_size=22, color=WHITE)
                plus.move_to(np.array([x_pos, formula_y, 0]))
                formula_parts.append(plus)
                x_pos += 0.5

        eq = Text("=", font=AUTHOR_FONT, font_size=22, color=WHITE).move_to(np.array([x_pos, formula_y, 0]))
        formula_parts.append(eq)

        self.play(
            FadeIn(total_label),
            LaggedStart(*[FadeIn(p) for p in formula_parts], lag_ratio=0.08),
            run_time=1.0
        )

        # 总数弹出
        self.play(FadeIn(total_num, scale=0.3), run_time=0.5)
        self.play(Flash(total_num, color=COLOR_HIGHLIGHT, flash_radius=0.5), run_time=0.4)

        self.wait(1.2)

        # 提示
        next_hint = Text(
            "用象形图看更直观！",
            font=AUTHOR_FONT,
            font_size=30,
            color=GREEN
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(next_hint, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(title),
            FadeOut(table_cells),
            FadeOut(header_label),
            FadeOut(fruit_headers),
            FadeOut(total_header),
            FadeOut(row_label_count),
            FadeOut(data_numbers),
            FadeOut(total_label),
            FadeOut(total_num),
            FadeOut(next_hint),
            *[FadeOut(p) for p in formula_parts],
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # Scene 4: 象形统计图（核心场景）
    # ─────────────────────────────────────────────
    def scene_4_pictograph(self):
        title = Text(
            "象形统计图",
            font=AUTHOR_FONT,
            font_size=40,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 6.3)

        subtitle = Text(
            "每个 ★ 代表 1 人",
            font=AUTHOR_FONT,
            font_size=28,
            color=YELLOW
        ).move_to(UP * 5.4)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle, shift=DOWN * 0.2), run_time=0.4)

        # ── 绘制坐标网格 ──
        # 图表布局（已由 verify_geometry.py 验证）
        origin_x = CHART_ORIGIN_X   # -3.0
        origin_y = CHART_ORIGIN_Y   # -3.5
        col_w = COL_WIDTH            # 1.8
        row_h = ROW_HEIGHT           # 0.72

        # 网格线（横向）
        max_rows = MAX_COUNT + 1     # 7条横线
        grid_lines = VGroup()

        for row in range(max_rows + 1):
            y = origin_y + row * row_h
            line = Line(
                start=np.array([origin_x - 0.1, y, 0]),
                end=np.array([origin_x + NUM_FRUITS * col_w + 0.1, y, 0]),
                stroke_width=1.5,
                color=COLOR_GRID_LINE
            )
            grid_lines.add(line)

        # 网格线（纵向）
        for col in range(NUM_FRUITS + 1):
            x = origin_x + col * col_w
            line = Line(
                start=np.array([x, origin_y, 0]),
                end=np.array([x, origin_y + MAX_COUNT * row_h + 0.1, 0]),
                stroke_width=1.5,
                color=COLOR_GRID_LINE
            )
            grid_lines.add(line)

        self.play(Create(grid_lines), run_time=0.8)

        # ── Y 轴刻度 (1~6) ──
        y_labels = VGroup()
        for row in range(1, MAX_COUNT + 1):
            y_pos = origin_y + (row - 0.5) * row_h
            num = Text(str(row), font=AUTHOR_FONT, font_size=20, color=GRAY_B)
            num.move_to(np.array([origin_x - 0.4, y_pos, 0]))
            y_labels.add(num)
        self.play(FadeIn(y_labels), run_time=0.4)

        # ── X 轴水果标签 ──
        x_axis_labels = VGroup()
        for col, (name, color) in enumerate(zip(FRUIT_NAMES, FRUIT_COLORS)):
            col_center_x = origin_x + col * col_w + col_w / 2
            icon = make_fruit_icon(color, size=0.25)
            icon.move_to(np.array([col_center_x, origin_y - 0.45, 0]))
            lbl = Text(name, font=AUTHOR_FONT, font_size=22, color=color)
            lbl.next_to(icon, DOWN, buff=0.1)
            x_axis_labels.add(icon, lbl)

        self.play(FadeIn(x_axis_labels), run_time=0.5)

        # ── 逐列填入 ★ ──
        self.all_stars = VGroup()
        column_star_groups = []

        for col, (count, color) in enumerate(zip(FRUIT_DATA, FRUIT_COLORS)):
            col_center_x = origin_x + col * col_w + col_w / 2
            col_stars = VGroup()

            # 列名高亮提示
            col_label_temp = Text(
                FRUIT_NAMES[col],
                font=AUTHOR_FONT,
                font_size=28,
                color=color
            ).move_to(np.array([0, -5.2, 0]))

            count_label_temp = VGroup(
                Text(FRUIT_NAMES[col], font=AUTHOR_FONT, font_size=26, color=color),
                Text(" : ", font=AUTHOR_FONT, font_size=26, color=WHITE),
                Text(str(count), font=AUTHOR_FONT, font_size=32, color=color),
                Text(" 人", font=AUTHOR_FONT, font_size=26, color=WHITE),
            ).arrange(RIGHT, buff=0.05).move_to(np.array([0, -5.5, 0]))

            self.play(FadeIn(count_label_temp, shift=UP * 0.2), run_time=0.3)

            for row in range(count):
                star_y = origin_y + row * row_h + row_h / 2
                star = make_star_icon(color, size=0.25)
                star.move_to(np.array([col_center_x, star_y, 0]))
                col_stars.add(star)
                self.all_stars.add(star)

                self.play(
                    FadeIn(star, scale=0.3, rate_func=rush_from),
                    run_time=0.18
                )

            column_star_groups.append(col_stars)
            self.play(FadeOut(count_label_temp), run_time=0.2)

        self.wait(1.5)

        # 保留图表，进入问答场景
        self.chart_elements = VGroup(
            title, subtitle, grid_lines, y_labels, x_axis_labels, self.all_stars
        )
        self.column_star_groups = column_star_groups
        self.chart_origin = np.array([origin_x, origin_y, 0])
        self.chart_col_w = col_w
        self.chart_row_h = row_h

    # ─────────────────────────────────────────────
    # Scene 5: 三个问题
    # ─────────────────────────────────────────────
    def scene_5_questions(self):
        # 问题1: 谁最多？
        q1 = Text("❓ 谁最多？", font=AUTHOR_FONT, font_size=34, color=YELLOW)
        q1.move_to(np.array([0, -5.0, 0]))
        self.play(FadeIn(q1, shift=UP * 0.3), run_time=0.4)

        # 高亮葡萄列（第3列，index=3）
        grape_stars = self.column_star_groups[3]
        self.play(
            *[star.animate.set_color(YELLOW).scale(1.3) for star in grape_stars],
            run_time=0.6
        )

        a1_group = VGroup(
            Text("葡萄最多！", font=AUTHOR_FONT, font_size=30, color=COLOR_GRAPE),
            Text("有 6 人", font=AUTHOR_FONT, font_size=30, color=YELLOW),
        ).arrange(RIGHT, buff=0.2).move_to(np.array([0, -6.0, 0]))

        self.play(FadeIn(a1_group, scale=1.1), run_time=0.5)
        self.wait(1.0)

        # 恢复颜色
        self.play(
            *[star.animate.set_color(COLOR_GRAPE).scale(1/1.3) for star in grape_stars],
            FadeOut(q1),
            FadeOut(a1_group),
            run_time=0.4
        )

        # 问题2: 谁最少？
        q2 = Text("❓ 谁最少？", font=AUTHOR_FONT, font_size=34, color=YELLOW)
        q2.move_to(np.array([0, -5.0, 0]))
        self.play(FadeIn(q2, shift=UP * 0.3), run_time=0.4)

        banana_stars = self.column_star_groups[1]
        self.play(
            *[star.animate.set_color(YELLOW).scale(1.3) for star in banana_stars],
            run_time=0.6
        )

        a2_group = VGroup(
            Text("香蕉最少！", font=AUTHOR_FONT, font_size=30, color=COLOR_BANANA),
            Text("有 3 人", font=AUTHOR_FONT, font_size=30, color=YELLOW),
        ).arrange(RIGHT, buff=0.2).move_to(np.array([0, -6.0, 0]))

        self.play(FadeIn(a2_group, scale=1.1), run_time=0.5)
        self.wait(1.0)

        self.play(
            *[star.animate.set_color(COLOR_BANANA).scale(1/1.3) for star in banana_stars],
            FadeOut(q2),
            FadeOut(a2_group),
            run_time=0.4
        )

        # 问题3: 一共多少人？
        q3 = Text("❓ 一共多少人？", font=AUTHOR_FONT, font_size=34, color=YELLOW)
        q3.move_to(np.array([0, -4.8, 0]))
        self.play(FadeIn(q3, shift=UP * 0.3), run_time=0.4)

        # 所有列依次高亮
        for col_stars, color in zip(self.column_star_groups, FRUIT_COLORS):
            self.play(
                *[star.animate.set_color(YELLOW) for star in col_stars],
                run_time=0.25
            )

        formula_line = VGroup(
            Text("5+3+4+6", font=AUTHOR_FONT, font_size=28, color=WHITE),
            Text("=", font=AUTHOR_FONT, font_size=28, color=WHITE),
            Text("18", font=AUTHOR_FONT, font_size=36, color=COLOR_HIGHLIGHT),
            Text("人", font=AUTHOR_FONT, font_size=28, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(np.array([0, -5.8, 0]))

        self.play(Write(formula_line), run_time=0.8)
        self.play(Flash(formula_line[2], color=COLOR_HIGHLIGHT, flash_radius=0.6), run_time=0.4)
        self.wait(1.2)

        # 清场
        self.play(
            FadeOut(q3),
            FadeOut(formula_line),
            FadeOut(self.chart_elements),
            run_time=0.7
        )

    # ─────────────────────────────────────────────
    # Scene 6: 总结片尾
    # ─────────────────────────────────────────────
    def scene_6_outro(self):
        # 知识要点卡片
        summary_title = Text(
            "今天学会了！",
            font=AUTHOR_FONT,
            font_size=44,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)

        self.play(FadeIn(summary_title, scale=1.2), run_time=0.6)

        # 三要点
        points = [
            ("📊 统计表", "整理数据，清晰明了", COLOR_TABLE_LINE),
            ("★ 象形图", "每格=1，直观对比", YELLOW),
            ("🔍 读图", "最多、最少、合计", GREEN),
        ]

        point_cards = VGroup()
        for i, (icon_text, desc, color) in enumerate(points):
            bg = RoundedRectangle(
                corner_radius=0.3,
                width=7.0,
                height=1.0,
                fill_color=color,
                fill_opacity=0.15,
                stroke_color=color,
                stroke_width=2
            )
            icon_part = Text(icon_text, font=AUTHOR_FONT, font_size=26, color=color)
            desc_part = Text(desc, font=AUTHOR_FONT, font_size=22, color=WHITE)
            content = VGroup(icon_part, desc_part).arrange(RIGHT, buff=0.4)
            card = VGroup(bg, content)
            content.move_to(bg.get_center())
            point_cards.add(card)

        point_cards.arrange(DOWN, buff=0.4)
        point_cards.move_to(UP * 1.8)

        for card in point_cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.4)

        self.wait(0.5)

        # 作者大字
        author_name = Text(
            "上海初高中数学直通车",
            font=AUTHOR_FONT,
            font_size=36,
            color=WHITE
        ).move_to(DOWN * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font=AUTHOR_FONT,
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 3.0)

        follow_text = Text(
            "关注我，学更多小学数学！",
            font=AUTHOR_FONT,
            font_size=30,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 4.2)

        self.play(
            Transform(self.author, author_name),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(follow_text, scale=1.1), run_time=0.5)

        # 小星星装饰
        deco_stars = VGroup(*[
            Star(n=5, outer_radius=0.25, inner_radius=0.1,
                 fill_color=FRUIT_COLORS[i % 4], fill_opacity=0.9,
                 stroke_width=0)
            .move_to(np.array([
                2.8 * np.cos(i * TAU / 6),
                -5.5 + 0.6 * np.sin(i * TAU / 6),
                0
            ]))
            for i in range(6)
        ])

        self.play(
            LaggedStart(*[FadeIn(s, scale=0.3) for s in deco_stars], lag_ratio=0.1),
            run_time=0.6
        )
        self.play(Rotate(deco_stars, angle=TAU, run_time=2.0, rate_func=linear))

        self.wait(1.0)

        # 最终淡出
        self.play(
            FadeOut(summary_title),
            FadeOut(point_cards),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_stars),
            FadeOut(self.author),
            run_time=1.0
        )


# ─────────────────────────────────────────────
# 渲染命令:
#   快速预览: manim -pql statistics_animation.py StatisticsAnimation
#   高质量:   manim -qh  statistics_animation.py StatisticsAnimation
# ─────────────────────────────────────────────