"""
numbers_0_10.py - 认识数字0-10
一年级上册数学教学动画

内容: 认识数字0-10的形状和含义
目标观众: 一年级小学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== 全局配置 - TikTok竖屏 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ===== 颜色配置 =====
BG_COLOR = "#1a1a2e"
COLOR_ZERO = "#e74c3c"
COLOR_1_5 = "#3498db"
COLOR_6_10 = "#2ecc71"
COLOR_HIGHLIGHT = "#f1c40f"
COLOR_GRID_LINE = "#4a4a6a"
COLOR_DOT = "#f39c12"
COLOR_TEXT = WHITE
COLOR_DIM = "#888888"

FONT = "Noto Sans CJK SC"


def make_dot_array(n, dot_radius=0.16, spacing=0.45, color=COLOR_DOT):
    """
    生成n个圆点组成的阵列 VGroup
    最多每行5个，超过则换行
    """
    dots = VGroup()
    if n == 0:
        return dots
    
    cols = min(n, 5)
    rows = (n + cols - 1) // cols
    
    for i in range(n):
        row = i // cols
        col = i % cols
        current_row_count = min(cols, n - row * cols)
        
        x = (col - (current_row_count - 1) / 2.0) * spacing
        y = ((rows - 1) / 2.0 - row) * spacing
        
        dot = Circle(radius=dot_radius, fill_color=color, fill_opacity=1, stroke_width=0)
        dot.move_to(np.array([x, y, 0]))
        dots.add(dot)
    
    return dots


def make_grid_cell(cell_size=1.1, color=COLOR_GRID_LINE):
    """创建一个日字格（带十字中线）"""
    rect = Rectangle(width=cell_size, height=cell_size, color=color, stroke_width=2)
    # 横中线
    h_line = DashedLine(
        rect.get_left(), rect.get_right(),
        color=color, stroke_width=1, dash_length=0.05
    )
    # 竖中线
    v_line = DashedLine(
        rect.get_top(), rect.get_bottom(),
        color=color, stroke_width=1, dash_length=0.05
    )
    return VGroup(rect, h_line, v_line)


class Numbers0To10(Scene):
    """
    认识数字0-10 教学动画
    
    场景顺序:
    1. 开场钩子
    2. 认识0 - 特殊含义
    3. 数字1-5 + 点阵
    4. 数字6-10 + 点阵
    5. 数列0-10展示
    6. 日字格书写示范
    7. 片尾关注
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者标识（全程保留在顶部）
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_DIM
        ).move_to(UP * 7.3)

        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_zero()
        self.scene_3_one_to_five()
        self.scene_4_six_to_ten()
        self.scene_5_sequence()
        self.scene_6_writing()
        self.scene_7_outro()

    # ─────────────────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────────────────────
    def scene_1_opening(self):
        title = Text("数字大冒险！", font=FONT, font_size=52, color=COLOR_HIGHLIGHT)
        title.move_to(UP * 5.5)

        subtitle = Text("认识 0 到 10", font=FONT, font_size=36, color=COLOR_TEXT)
        subtitle.move_to(UP * 4.5)

        # 装饰性小数字（随机散落）
        deco_positions = [
            (-3.2, 2.0), (3.0, 2.5), (-3.5, 0.0),
            (3.2, 0.5), (-2.0, -1.5), (2.5, -2.0),
            (0.0, 0.5), (-1.2, 3.0), (1.5, 3.2),
        ]
        deco_nums = [str(i) for i in [0, 3, 7, 1, 5, 9, 2, 6, 8]]
        deco_colors = [COLOR_ZERO, COLOR_1_5, COLOR_6_10] * 3

        deco = VGroup()
        for i, ((x, y), num, col) in enumerate(zip(deco_positions, deco_nums, deco_colors)):
            t = Text(num, font=FONT, font_size=40, color=col, fill_opacity=0.5)
            t.move_to(np.array([x, y, 0]))
            deco.add(t)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)

        # 装饰数字依次飘入
        for t in deco:
            self.play(FadeIn(t, shift=DOWN * 0.3, scale=0.8), run_time=0.15)

        self.wait(0.8)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(deco),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────
    # Scene 2: 认识0
    # ─────────────────────────────────────────────────────────
    def scene_2_zero(self):
        # ---- 标题 ----
        section_title = Text("认识  0", font=FONT, font_size=40, color=COLOR_ZERO)
        section_title.move_to(UP * 6.0)
        self.play(Write(section_title), run_time=0.6)

        # ---- 大数字0 ----
        big_zero = Text("0", font=FONT, font_size=160, color=COLOR_ZERO)
        big_zero.move_to(UP * 3.0)
        self.play(GrowFromCenter(big_zero), run_time=0.8)

        # ---- 空盘子演示 ----
        plate = Ellipse(width=3.0, height=0.8, color=GRAY_B, stroke_width=3)
        plate.move_to(UP * 0.5)
        plate_label = Text("盘子里有苹果吗？", font=FONT, font_size=26, color=GRAY_A)
        plate_label.move_to(DOWN * 0.5)

        self.play(Create(plate), run_time=0.5)
        self.play(FadeIn(plate_label), run_time=0.4)
        self.wait(0.5)

        # 空盘子闪烁
        self.play(plate.animate.set_color(COLOR_ZERO), run_time=0.2)
        self.play(plate.animate.set_color(GRAY_B), run_time=0.2)
        self.play(plate.animate.set_color(COLOR_ZERO), run_time=0.2)
        self.play(plate.animate.set_color(GRAY_B), run_time=0.2)

        answer = Text("没有！0 个！", font=FONT, font_size=32, color=COLOR_HIGHLIGHT)
        answer.move_to(DOWN * 1.5)
        self.play(FadeIn(answer, scale=1.2), run_time=0.5)
        self.wait(0.8)

        # ---- 含义说明 ----
        meaning_1 = Text("0 表示 \"没有\"", font=FONT, font_size=28, color=COLOR_TEXT)
        meaning_1.move_to(DOWN * 3.0)
        self.play(Write(meaning_1), run_time=0.6)

        # ---- 尺子上的0 ----
        ruler_y = -4.5
        ruler_line = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_A, stroke_width=3)
        ruler_line.move_to(UP * ruler_y)

        # 刻度线
        ticks = VGroup()
        tick_labels = VGroup()
        for i in range(6):
            x = -3.5 + i * 7.0 / 5
            tick = Line(UP * 0.15, DOWN * 0.15, color=GRAY_A, stroke_width=2)
            tick.move_to(np.array([x, ruler_y, 0]))
            ticks.add(tick)

            num_str = str(i)
            col = COLOR_ZERO if i == 0 else GRAY_A
            lbl = Text(num_str, font=FONT, font_size=22, color=col)
            lbl.move_to(np.array([x, ruler_y - 0.4, 0]))
            tick_labels.add(lbl)

        self.play(Create(ruler_line), Create(ticks), run_time=0.5)
        self.play(Write(tick_labels), run_time=0.6)

        # 箭头指向0
        arrow = Arrow(
            start=np.array([-3.5, ruler_y - 1.0, 0]),
            end=np.array([-3.5, ruler_y - 0.25, 0]),
            color=COLOR_ZERO, buff=0.05, stroke_width=4,
            max_tip_length_to_length_ratio=0.3
        )
        start_label = Text("计数起点", font=FONT, font_size=22, color=COLOR_ZERO)
        start_label.move_to(np.array([-3.5, ruler_y - 1.4, 0]))

        self.play(GrowArrow(arrow), FadeIn(start_label), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(section_title),
            FadeOut(big_zero),
            FadeOut(plate),
            FadeOut(plate_label),
            FadeOut(answer),
            FadeOut(meaning_1),
            FadeOut(ruler_line),
            FadeOut(ticks),
            FadeOut(tick_labels),
            FadeOut(arrow),
            FadeOut(start_label),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────────────
    # Scene 3: 数字1-5
    # ─────────────────────────────────────────────────────────
    def scene_3_one_to_five(self):
        section_title = Text("认识  1 ~ 5", font=FONT, font_size=40, color=COLOR_1_5)
        section_title.move_to(UP * 6.0)
        self.play(Write(section_title), run_time=0.5)

        hint = Text("数字 = 点的数量", font=FONT, font_size=24, color=GRAY_A)
        hint.move_to(UP * 5.2)
        self.play(FadeIn(hint), run_time=0.3)

        current_num_text = None
        current_dots = None

        for n in range(1, 6):
            big_num = Text(str(n), font=FONT, font_size=150, color=COLOR_1_5)
            big_num.move_to(UP * 2.5)

            dots = make_dot_array(n, spacing=0.50, color=COLOR_DOT)
            dots.move_to(DOWN * 0.5)

            count_text = Text(f"{n}  个", font=FONT, font_size=30, color=COLOR_TEXT)
            count_text.move_to(DOWN * 2.2)

            if current_num_text is None:
                self.play(GrowFromCenter(big_num), run_time=0.5)
                self.play(
                    LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.2),
                    run_time=0.6
                )
                self.play(FadeIn(count_text), run_time=0.3)
            else:
                self.play(
                    Transform(current_num_text, big_num),
                    run_time=0.4
                )
                self.play(
                    FadeOut(current_dots),
                    run_time=0.2
                )
                self.play(
                    LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.15),
                    run_time=0.5
                )
                self.play(Transform(current_count, count_text), run_time=0.3)

            self.wait(0.6)

            if current_num_text is None:
                current_num_text = big_num
                current_count = count_text
            current_dots = dots

        # 汇总展示1-5
        self.play(
            FadeOut(current_num_text),
            FadeOut(current_dots),
            FadeOut(current_count),
            run_time=0.4
        )

        summary = VGroup()
        for n in range(1, 6):
            num_t = Text(str(n), font=FONT, font_size=60, color=COLOR_1_5)
            d = make_dot_array(n, dot_radius=0.10, spacing=0.28, color=COLOR_DOT)
            card = VGroup(num_t, d).arrange(DOWN, buff=0.3)
            summary.add(card)
        summary.arrange(RIGHT, buff=0.5)
        summary.move_to(UP * 1.5)

        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in summary], lag_ratio=0.15),
            run_time=1.0
        )
        self.wait(1.0)

        self.play(FadeOut(section_title), FadeOut(hint), FadeOut(summary), run_time=0.5)

    # ─────────────────────────────────────────────────────────
    # Scene 4: 数字6-10
    # ─────────────────────────────────────────────────────────
    def scene_4_six_to_ten(self):
        section_title = Text("认识  6 ~ 10", font=FONT, font_size=40, color=COLOR_6_10)
        section_title.move_to(UP * 6.0)
        self.play(Write(section_title), run_time=0.5)

        current_num_text = None
        current_dots = None
        current_count = None

        for n in range(6, 11):
            num_color = COLOR_HIGHLIGHT if n == 10 else COLOR_6_10
            big_num = Text(str(n), font=FONT, font_size=150, color=num_color)
            big_num.move_to(UP * 2.5)

            dots = make_dot_array(n, spacing=0.48, color=COLOR_DOT)
            dots.move_to(DOWN * 0.2)

            count_text = Text(f"{n}  个", font=FONT, font_size=30, color=COLOR_TEXT)
            count_text.move_to(DOWN * 2.3)

            if current_num_text is None:
                self.play(GrowFromCenter(big_num), run_time=0.5)
                self.play(
                    LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.15),
                    run_time=0.8
                )
                self.play(FadeIn(count_text), run_time=0.3)
            else:
                self.play(
                    Transform(current_num_text, big_num),
                    run_time=0.4
                )
                self.play(FadeOut(current_dots), run_time=0.2)
                self.play(
                    LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.12),
                    run_time=0.7
                )
                self.play(Transform(current_count, count_text), run_time=0.3)

            # 10特别处理：闪光效果
            if n == 10:
                self.play(Flash(current_num_text if current_num_text else big_num,
                                color=COLOR_HIGHLIGHT, flash_radius=1.2), run_time=0.5)
                special = Text("两位数！", font=FONT, font_size=32, color=COLOR_HIGHLIGHT)
                special.move_to(DOWN * 3.2)
                self.play(FadeIn(special, scale=1.2), run_time=0.4)
                self.wait(0.8)
                self.play(FadeOut(special), run_time=0.3)
            else:
                self.wait(0.5)

            if current_num_text is None:
                current_num_text = big_num
                current_count = count_text
            current_dots = dots

        self.play(
            FadeOut(current_num_text),
            FadeOut(current_dots),
            FadeOut(current_count),
            run_time=0.4
        )

        # 汇总展示6-10
        summary = VGroup()
        for n in range(6, 11):
            num_t = Text(str(n), font=FONT, font_size=55, color=COLOR_6_10)
            d = make_dot_array(n, dot_radius=0.08, spacing=0.24, color=COLOR_DOT)
            card = VGroup(num_t, d).arrange(DOWN, buff=0.25)
            summary.add(card)
        summary.arrange(RIGHT, buff=0.45)
        summary.move_to(UP * 1.0)

        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in summary], lag_ratio=0.15),
            run_time=1.0
        )
        self.wait(1.0)

        self.play(FadeOut(section_title), FadeOut(summary), run_time=0.5)

    # ─────────────────────────────────────────────────────────
    # Scene 5: 数列0-10展示
    # ─────────────────────────────────────────────────────────
    def scene_5_sequence(self):
        section_title = Text("数字序列", font=FONT, font_size=40, color=COLOR_TEXT)
        section_title.move_to(UP * 6.0)
        self.play(Write(section_title), run_time=0.5)

        # 数轴
        axis_y = UP * 0.5
        axis_line = Arrow(
            LEFT * 4.2, RIGHT * 4.2,
            color=GRAY_A, stroke_width=3,
            max_tip_length_to_length_ratio=0.04
        )
        axis_line.move_to(axis_y)
        self.play(Create(axis_line), run_time=0.6)

        # 0-10 各数字和刻度
        num_positions = []
        for i in range(11):
            x = -4.0 + i * 0.8
            num_positions.append(x)

        colors = (
            [COLOR_ZERO]
            + [COLOR_1_5] * 5
            + [COLOR_6_10] * 4
            + [COLOR_HIGHLIGHT]
        )

        tick_group = VGroup()
        num_group = VGroup()

        for i, (x, col) in enumerate(zip(num_positions, colors)):
            tick = Line(UP * 0.12, DOWN * 0.12, color=col, stroke_width=2)
            tick.move_to(np.array([x, 0.5, 0]))
            tick_group.add(tick)

            num_t = Text(str(i), font=FONT, font_size=30, color=col)
            num_t.move_to(np.array([x, 0.0, 0]))
            num_group.add(num_t)

        self.play(
            LaggedStart(*[Create(t) for t in tick_group], lag_ratio=0.08),
            run_time=0.8
        )
        self.play(
            LaggedStart(*[Write(n) for n in num_group], lag_ratio=0.08),
            run_time=0.9
        )

        # 箭头依次跳跃强调
        bounce_arrow = Arrow(
            np.array([num_positions[0], 1.3, 0]),
            np.array([num_positions[0], 0.85, 0]),
            color=COLOR_HIGHLIGHT, stroke_width=5,
            max_tip_length_to_length_ratio=0.4
        )
        self.play(GrowArrow(bounce_arrow), run_time=0.3)

        for i in range(1, 11):
            new_arrow = Arrow(
                np.array([num_positions[i], 1.3, 0]),
                np.array([num_positions[i], 0.85, 0]),
                color=COLOR_HIGHLIGHT, stroke_width=5,
                max_tip_length_to_length_ratio=0.4
            )
            self.play(Transform(bounce_arrow, new_arrow), run_time=0.18)
        self.play(FadeOut(bounce_arrow), run_time=0.2)

        # 小结
        summary_text = Text(
            "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10",
            font=FONT, font_size=24, color=COLOR_TEXT
        )
        summary_text.move_to(DOWN * 1.0)
        self.play(Write(summary_text), run_time=0.8)

        direction_text = Text("从小到大排列 →", font=FONT, font_size=24, color=GRAY_A)
        direction_text.move_to(DOWN * 2.0)
        self.play(FadeIn(direction_text), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(section_title),
            FadeOut(axis_line),
            FadeOut(tick_group),
            FadeOut(num_group),
            FadeOut(summary_text),
            FadeOut(direction_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────
    # Scene 6: 日字格书写示范
    # ─────────────────────────────────────────────────────────
    def scene_6_writing(self):
        section_title = Text("书写练习", font=FONT, font_size=40, color=COLOR_TEXT)
        section_title.move_to(UP * 6.0)
        self.play(Write(section_title), run_time=0.5)

        subtitle = Text("在日字格里写数字", font=FONT, font_size=26, color=GRAY_A)
        subtitle.move_to(UP * 5.2)
        self.play(FadeIn(subtitle), run_time=0.3)

        # 要演示的数字
        demo_nums = ["0", "1", "8"]
        demo_colors = [COLOR_ZERO, COLOR_1_5, COLOR_6_10]

        cell_size = 1.4
        # 三个日字格横向排列
        cells = VGroup()
        cell_centers = []
        for i in range(3):
            x = (i - 1) * (cell_size + 0.5)
            cell = make_grid_cell(cell_size=cell_size, color=COLOR_GRID_LINE)
            cell.move_to(np.array([x, 1.5, 0]))
            cells.add(cell)
            cell_centers.append(np.array([x, 1.5, 0]))

        self.play(Create(cells), run_time=0.8)

        # 在格子里依次写数字
        written_nums = VGroup()
        for i, (num_str, col, center) in enumerate(zip(demo_nums, demo_colors, cell_centers)):
            num_written = Text(num_str, font=FONT, font_size=int(cell_size * 55), color=col)
            num_written.move_to(center)
            self.play(Write(num_written), run_time=0.7)
            written_nums.add(num_written)
            self.wait(0.3)

        # 表扬
        bravo = Text("写得真棒！🎉", font=FONT, font_size=36, color=COLOR_HIGHLIGHT)
        bravo.move_to(DOWN * 0.5)
        self.play(FadeIn(bravo, scale=1.2), run_time=0.5)

        # 笔顺提示
        tip_title = Text("小提示:", font=FONT, font_size=24, color=COLOR_TEXT)
        tip_title.move_to(DOWN * 1.8)
        tip_body = Text("数字要写在格子中间，大小合适", font=FONT, font_size=22, color=GRAY_A)
        tip_body.move_to(DOWN * 2.5)

        self.play(FadeIn(tip_title), FadeIn(tip_body), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(section_title),
            FadeOut(subtitle),
            FadeOut(cells),
            FadeOut(written_nums),
            FadeOut(bravo),
            FadeOut(tip_title),
            FadeOut(tip_body),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────────────
    # Scene 7: 片尾
    # ─────────────────────────────────────────────────────────
    def scene_7_outro(self):
        # 作者名放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B
        ).move_to(UP * 1.0)

        self.play(
            Transform(self.author_bar, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.4)

        follow = Text(
            "关注我，学更多数学知识！",
            font=FONT, font_size=30, color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(follow, scale=1.1), run_time=0.5)

        # 0-10彩色数字环绕
        ring_radius = 3.0
        ring_nums = VGroup()
        n_ring = 11
        ring_colors = (
            [COLOR_ZERO]
            + [COLOR_1_5] * 5
            + [COLOR_6_10] * 4
            + [COLOR_HIGHLIGHT]
        )
        for i in range(n_ring):
            angle = 2 * np.pi * i / n_ring - np.pi / 2
            x = ring_radius * np.cos(angle)
            y = ring_radius * np.sin(angle) - 2.5
            t = Text(str(i), font=FONT, font_size=34, color=ring_colors[i])
            t.move_to(np.array([x, y, 0]))
            ring_nums.add(t)

        self.play(
            LaggedStart(*[GrowFromCenter(t) for t in ring_nums], lag_ratio=0.07),
            run_time=1.0
        )
        self.play(Rotate(ring_nums, angle=TAU / n_ring, about_point=np.array([0, -2.5, 0])),
                  run_time=1.5)

        self.wait(0.8)
        self.play(
            FadeOut(self.author_bar),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(ring_nums),
            run_time=1.0
        )


# ─────────────────────────────────────────────────────────
# 渲染命令:
# 快速预览: manim -pql numbers_0_10.py Numbers0To10
# 高清渲染: manim -qh numbers_0_10.py Numbers0To10
# ─────────────────────────────────────────────────────────