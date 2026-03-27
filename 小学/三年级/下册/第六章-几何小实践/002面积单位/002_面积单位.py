"""
002_面积单位.py — 面积单位 教学动画

知识点: 认识平方厘米、平方分米、平方米
  - 1 cm²: 边长1厘米的正方形的面积
  - 1 dm²: 边长1分米的正方形的面积
  - 1 m²:  边长1米的正方形的面积
  - 生活联系: 找生活中接近各面积单位的物体

年级: 三年级下册 第六章
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
BG_COLOR    = "#1a1a2e"
COLOR_CM    = "#3b82f6"   # 蓝色 — 平方厘米
COLOR_DM    = "#22c55e"   # 绿色 — 平方分米
COLOR_M     = "#f59e0b"   # 橙色 — 平方米
COLOR_HL    = "#fbbf24"   # 黄色高亮
COLOR_LIFE  = "#a78bfa"   # 紫色 生活联系
COLOR_AUTHOR = "#6b7280"  # 灰色作者信息
FONT = "Hiragino Sans GB"


# ======================================================================
# 主场景
# ======================================================================

class AreaUnitLesson(Scene):
    """
    面积单位教学动画
    场景顺序:
      1. 开场钩子 — 面积单位是什么?
      2. 平方厘米 (cm²) — 定义 + 直观演示
      3. 生活中的平方厘米
      4. 平方分米 (dm²) — 定义 + 直观演示
      5. 生活中的平方分米
      6. 平方米 (m²) — 定义 + 直观演示
      7. 生活中的平方米
      8. 三者对比总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_sq_centimeter()
        self.scene_3_life_cm()
        self.scene_4_sq_decimeter()
        self.scene_5_life_dm()
        self.scene_6_sq_meter()
        self.scene_7_life_m()
        self.scene_8_comparison()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化尺寸参数"""
        # 展示用的正方形视觉尺寸 (逻辑单位, 与实际长度单位无关)
        self.sq_cm_size  = 1.8   # cm² 正方形边长 (屏幕单位)
        self.sq_dm_size  = 3.0   # dm² 正方形边长 (屏幕单位)
        self.sq_m_size   = 5.5   # m²  正方形边长 (屏幕单位)

        # 标准正方形网格 (cm² 演示用 5x5 格)
        self.grid_n = 5
        self.grid_cell = self.sq_cm_size / self.grid_n

        print("Geometry setup complete")

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        """创建作者标识"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_square_with_label(self, size, color, center, label_str,
                                formula_parts=None, fill_opacity=0.18):
        """
        创建带标注的正方形
        label_str: 中文标签 (Text)
        formula_parts: list of (type, content) — ('text', ...) or ('math', ...)
        """
        sq = Square(
            side_length=size,
            color=color,
            stroke_width=4,
            fill_color=color,
            fill_opacity=fill_opacity,
        ).move_to(center)
        return sq

    def make_grid_inside(self, sq_center, sq_size, n, color):
        """在正方形内画 n×n 网格线"""
        lines = VGroup()
        half = sq_size / 2
        cell = sq_size / n

        # 垂直线
        for i in range(1, n):
            x = sq_center[0] - half + i * cell
            lines.add(
                Line(
                    np.array([x, sq_center[1] - half, 0]),
                    np.array([x, sq_center[1] + half, 0]),
                    color=color, stroke_width=1.5, stroke_opacity=0.5,
                )
            )
        # 水平线
        for i in range(1, n):
            y = sq_center[1] - half + i * cell
            lines.add(
                Line(
                    np.array([sq_center[0] - half, y, 0]),
                    np.array([sq_center[0] + half, y, 0]),
                    color=color, stroke_width=1.5, stroke_opacity=0.5,
                )
            )
        return lines

    def make_side_brace(self, sq, direction, label_parts, color):
        """
        在正方形一侧画大括号+标注
        direction: LEFT or RIGHT or UP or DOWN
        label_parts: list of mobjects to arrange RIGHT
        """
        brace = Brace(sq, direction=direction, buff=0.12, color=color)
        label_group = VGroup(*label_parts).arrange(RIGHT, buff=0.08)
        brace.put_at_tip(label_group, buff=0.18)
        return VGroup(brace, label_group)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "你知道面积单位有哪些吗?",
            font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(UP * 5.2)

        sub = Text(
            "cm²、dm²、m²，今天全搞懂!",
            font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 4.3)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 三个面积单位符号快速亮相
        labels = VGroup(
            MathTex(r"1\,\text{cm}^2", font_size=52, color=COLOR_CM),
            MathTex(r"1\,\text{dm}^2", font_size=52, color=COLOR_DM),
            MathTex(r"1\,\text{m}^2",  font_size=52, color=COLOR_M),
        ).arrange(DOWN, buff=0.6).move_to(UP * 1.0)

        for lbl in labels:
            self.play(FadeIn(lbl, scale=0.7), run_time=0.4)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(hook), FadeOut(sub), FadeOut(labels),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 平方厘米 (cm²)
    # ------------------------------------------------------------------

    def scene_2_sq_centimeter(self):
        title = Text("平方厘米", font=FONT, font_size=40, color=COLOR_CM)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 副标题
        sub = Text(
            "边长是 1 厘米的正方形",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.6)
        self.play(FadeIn(sub), run_time=0.4)

        # 主正方形
        sq_center = np.array([0.0, 1.5, 0.0])
        sq = Square(
            side_length=self.sq_cm_size,
            color=COLOR_CM, stroke_width=5,
            fill_color=COLOR_CM, fill_opacity=0.2,
        ).move_to(sq_center)

        self.play(Create(sq), run_time=1.0)

        # 网格 (5×5)
        grid = self.make_grid_inside(sq_center, self.sq_cm_size, 5, COLOR_CM)
        self.play(Create(grid), run_time=0.6)

        # 左侧大括号 + "1 cm"
        brace_left = Brace(sq, direction=LEFT, buff=0.12, color=COLOR_CM)
        label_left = VGroup(
            MathTex(r"1", font_size=28, color=COLOR_CM),
            Text("厘米", font=FONT, font_size=22, color=COLOR_CM),
        ).arrange(RIGHT, buff=0.06)
        brace_left.put_at_tip(label_left, buff=0.18)
        brace_group_left = VGroup(brace_left, label_left)

        # 底侧大括号 + "1 cm"
        brace_bot = Brace(sq, direction=DOWN, buff=0.12, color=COLOR_CM)
        label_bot = VGroup(
            MathTex(r"1", font_size=28, color=COLOR_CM),
            Text("厘米", font=FONT, font_size=22, color=COLOR_CM),
        ).arrange(RIGHT, buff=0.06)
        brace_bot.put_at_tip(label_bot, buff=0.18)
        brace_group_bot = VGroup(brace_bot, label_bot)

        self.play(
            Create(brace_group_left),
            Create(brace_group_bot),
            run_time=0.7,
        )

        # 面积公式
        formula = VGroup(
            Text("面积", font=FONT, font_size=28, color=WHITE),
            MathTex(r"=", font_size=30, color=WHITE),
            MathTex(r"1\,\mathrm{cm}^2", font_size=34, color=COLOR_CM),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.2)

        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.6)

        # 全名标注
        full_name = VGroup(
            Text("1 平方厘米", font=FONT, font_size=26, color=COLOR_CM),
        ).move_to(DOWN * 4.2)
        self.play(FadeIn(full_name), run_time=0.4)

        # 高亮闪烁
        self.play(Indicate(sq, color=COLOR_HL, scale_factor=1.06), run_time=0.8)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(sq), FadeOut(grid),
            FadeOut(brace_group_left), FadeOut(brace_group_bot),
            FadeOut(formula), FadeOut(full_name),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 生活中的平方厘米
    # ------------------------------------------------------------------

    def scene_3_life_cm(self):
        title = Text("生活中的平方厘米", font=FONT, font_size=36, color=COLOR_CM)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        tip = Text(
            "大约有多大?",
            font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 4.7)
        self.play(FadeIn(tip), run_time=0.4)

        # 指甲盖示意 — 圆角正方形近似
        nail_center = np.array([-2.2, 2.5, 0.0])
        nail = RoundedRectangle(
            width=1.2, height=1.4,
            corner_radius=0.3,
            color=COLOR_LIFE, stroke_width=3,
            fill_color=COLOR_LIFE, fill_opacity=0.2,
        ).move_to(nail_center)
        nail_label = Text("大拇指\n指甲盖", font=FONT, font_size=20, color=WHITE)
        nail_label.next_to(nail, DOWN, buff=0.25)

        # 纽扣示意 — 小正方形
        button_center = np.array([2.2, 2.5, 0.0])
        button = Square(
            side_length=1.2,
            color=COLOR_LIFE, stroke_width=3,
            fill_color=COLOR_LIFE, fill_opacity=0.2,
        ).move_to(button_center)
        # 纽扣四个小圆孔
        holes = VGroup(*[
            Circle(radius=0.1, color=COLOR_LIFE, stroke_width=2)
            .move_to(button_center + np.array([dx * 0.25, dy * 0.25, 0]))
            for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]
        ])
        button_label = Text("普通\n纽扣", font=FONT, font_size=20, color=WHITE)
        button_label.next_to(button, DOWN, buff=0.25)

        # 小正方形 (1cm²) 演示
        demo_sq = Square(
            side_length=self.sq_cm_size * 0.8,
            color=COLOR_CM, stroke_width=4,
            fill_color=COLOR_CM, fill_opacity=0.25,
        ).move_to(np.array([0.0, 0.2, 0.0]))

        demo_label = VGroup(
            MathTex(r"1\,\mathrm{cm}^2", font_size=32, color=COLOR_CM),
        ).next_to(demo_sq, RIGHT, buff=0.3)

        # 文字说明
        explain = Text(
            "边长 1 厘米的正方形\n面积约等于大拇指指甲盖",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 2.8)

        self.play(FadeIn(nail, scale=0.8), FadeIn(button, scale=0.8), run_time=0.6)
        self.play(
            Create(holes),
            FadeIn(nail_label), FadeIn(button_label),
            run_time=0.5,
        )
        self.play(Create(demo_sq), FadeIn(demo_label), run_time=0.7)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(tip),
            FadeOut(nail), FadeOut(button), FadeOut(holes),
            FadeOut(nail_label), FadeOut(button_label),
            FadeOut(demo_sq), FadeOut(demo_label), FadeOut(explain),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 4: 平方分米 (dm²)
    # ------------------------------------------------------------------

    def scene_4_sq_decimeter(self):
        title = Text("平方分米", font=FONT, font_size=40, color=COLOR_DM)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        sub = Text(
            "边长是 1 分米的正方形",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.6)
        self.play(FadeIn(sub), run_time=0.4)

        # 主正方形
        sq_center = np.array([0.0, 1.2, 0.0])
        sq = Square(
            side_length=self.sq_dm_size,
            color=COLOR_DM, stroke_width=5,
            fill_color=COLOR_DM, fill_opacity=0.18,
        ).move_to(sq_center)
        self.play(Create(sq), run_time=1.0)

        # 网格 (10×10, 模拟 10cm × 10cm)
        grid = self.make_grid_inside(sq_center, self.sq_dm_size, 10, COLOR_DM)
        self.play(Create(grid), run_time=0.6)

        # 边长标注
        brace_left = Brace(sq, direction=LEFT, buff=0.12, color=COLOR_DM)
        label_left = VGroup(
            MathTex(r"1", font_size=28, color=COLOR_DM),
            Text("分米", font=FONT, font_size=22, color=COLOR_DM),
        ).arrange(RIGHT, buff=0.06)
        brace_left.put_at_tip(label_left, buff=0.18)

        brace_bot = Brace(sq, direction=DOWN, buff=0.12, color=COLOR_DM)
        label_bot = VGroup(
            MathTex(r"1", font_size=28, color=COLOR_DM),
            Text("分米", font=FONT, font_size=22, color=COLOR_DM),
        ).arrange(RIGHT, buff=0.06)
        brace_bot.put_at_tip(label_bot, buff=0.18)

        brace_left_g = VGroup(brace_left, label_left)
        brace_bot_g  = VGroup(brace_bot, label_bot)

        self.play(Create(brace_left_g), Create(brace_bot_g), run_time=0.7)

        # 面积公式
        formula = VGroup(
            Text("面积", font=FONT, font_size=28, color=WHITE),
            MathTex(r"=", font_size=30, color=WHITE),
            MathTex(r"1\,\mathrm{dm}^2", font_size=34, color=COLOR_DM),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.5)

        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.6)

        full_name = Text("1 平方分米", font=FONT, font_size=26, color=COLOR_DM)
        full_name.move_to(DOWN * 4.5)
        self.play(FadeIn(full_name), run_time=0.4)

        self.play(Indicate(sq, color=COLOR_HL, scale_factor=1.04), run_time=0.8)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(sq), FadeOut(grid),
            FadeOut(brace_left_g), FadeOut(brace_bot_g),
            FadeOut(formula), FadeOut(full_name),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 5: 生活中的平方分米
    # ------------------------------------------------------------------

    def scene_5_life_dm(self):
        title = Text("生活中的平方分米", font=FONT, font_size=36, color=COLOR_DM)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        tip = Text(
            "大约有多大?",
            font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 4.7)
        self.play(FadeIn(tip), run_time=0.4)

        # 平板 / 书本封面示意
        book_center = np.array([-2.0, 2.2, 0.0])
        book = Rectangle(
            width=2.0, height=2.5,
            color=COLOR_LIFE, stroke_width=3,
            fill_color=COLOR_LIFE, fill_opacity=0.15,
        ).move_to(book_center)
        book_lines = VGroup(
            Line(book_center + LEFT * 0.9 + UP * 0.5,
                 book_center + RIGHT * 0.9 + UP * 0.5,
                 color=COLOR_LIFE, stroke_width=1.5, stroke_opacity=0.5),
            Line(book_center + LEFT * 0.9 + UP * 0.0,
                 book_center + RIGHT * 0.9 + UP * 0.0,
                 color=COLOR_LIFE, stroke_width=1.5, stroke_opacity=0.5),
            Line(book_center + LEFT * 0.9 + DOWN * 0.5,
                 book_center + RIGHT * 0.9 + DOWN * 0.5,
                 color=COLOR_LIFE, stroke_width=1.5, stroke_opacity=0.5),
        )
        book_label = Text("课本封面", font=FONT, font_size=20, color=WHITE)
        book_label.next_to(book, DOWN, buff=0.25)

        # 瓷砖小方格示意
        tile_center = np.array([2.2, 2.2, 0.0])
        tile = Square(
            side_length=2.2,
            color=COLOR_LIFE, stroke_width=3,
            fill_color=COLOR_LIFE, fill_opacity=0.15,
        ).move_to(tile_center)
        tile_grid = self.make_grid_inside(tile_center, 2.2, 4, COLOR_LIFE)
        tile_label = Text("地板砖\n(小块)", font=FONT, font_size=20, color=WHITE)
        tile_label.next_to(tile, DOWN, buff=0.25)

        # dm² 演示正方形
        dm_sq = Square(
            side_length=2.4,
            color=COLOR_DM, stroke_width=4,
            fill_color=COLOR_DM, fill_opacity=0.22,
        ).move_to(np.array([0.0, -0.8, 0.0]))
        dm_label = MathTex(r"1\,\mathrm{dm}^2", font_size=32, color=COLOR_DM)
        dm_label.next_to(dm_sq, RIGHT, buff=0.3)

        explain = Text(
            "边长 1 分米的正方形\n大约是课本封面的大小",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 3.5)

        self.play(
            FadeIn(book, scale=0.8), FadeIn(tile, scale=0.8),
            run_time=0.6,
        )
        self.play(
            Create(book_lines), Create(tile_grid),
            FadeIn(book_label), FadeIn(tile_label),
            run_time=0.5,
        )
        self.play(Create(dm_sq), FadeIn(dm_label), run_time=0.7)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(tip),
            FadeOut(book), FadeOut(book_lines), FadeOut(book_label),
            FadeOut(tile), FadeOut(tile_grid), FadeOut(tile_label),
            FadeOut(dm_sq), FadeOut(dm_label), FadeOut(explain),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 6: 平方米 (m²)
    # ------------------------------------------------------------------

    def scene_6_sq_meter(self):
        title = Text("平方米", font=FONT, font_size=40, color=COLOR_M)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        sub = Text(
            "边长是 1 米的正方形",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.6)
        self.play(FadeIn(sub), run_time=0.4)

        # 主正方形 — 较大, 居中偏上
        sq_size = 4.2
        sq_center = np.array([0.0, 1.3, 0.0])
        sq = Square(
            side_length=sq_size,
            color=COLOR_M, stroke_width=5,
            fill_color=COLOR_M, fill_opacity=0.15,
        ).move_to(sq_center)
        self.play(Create(sq), run_time=1.0)

        # 粗网格 (模拟 dm 格, 10×10)
        grid = self.make_grid_inside(sq_center, sq_size, 10, COLOR_M)
        self.play(Create(grid), run_time=0.7)

        # 边长标注 (仅左侧, 避免超出边界)
        brace_left = Brace(sq, direction=LEFT, buff=0.1, color=COLOR_M)
        label_left = VGroup(
            MathTex(r"1", font_size=26, color=COLOR_M),
            Text("米", font=FONT, font_size=22, color=COLOR_M),
        ).arrange(RIGHT, buff=0.06)
        brace_left.put_at_tip(label_left, buff=0.15)
        brace_g = VGroup(brace_left, label_left)
        self.play(Create(brace_g), run_time=0.6)

        # 底部标注
        brace_bot = Brace(sq, direction=DOWN, buff=0.1, color=COLOR_M)
        label_bot = VGroup(
            MathTex(r"1", font_size=26, color=COLOR_M),
            Text("米", font=FONT, font_size=22, color=COLOR_M),
        ).arrange(RIGHT, buff=0.06)
        brace_bot.put_at_tip(label_bot, buff=0.15)
        brace_bot_g = VGroup(brace_bot, label_bot)
        self.play(Create(brace_bot_g), run_time=0.6)

        # 面积公式
        formula = VGroup(
            Text("面积", font=FONT, font_size=28, color=WHITE),
            MathTex(r"=", font_size=30, color=WHITE),
            MathTex(r"1\,\mathrm{m}^2", font_size=34, color=COLOR_M),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.0)
        self.play(FadeIn(formula, shift=UP * 0.3), run_time=0.6)

        full_name = Text("1 平方米", font=FONT, font_size=26, color=COLOR_M)
        full_name.move_to(DOWN * 5.0)
        self.play(FadeIn(full_name), run_time=0.4)

        self.play(Indicate(sq, color=COLOR_HL, scale_factor=1.03), run_time=0.8)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(sq), FadeOut(grid),
            FadeOut(brace_g), FadeOut(brace_bot_g),
            FadeOut(formula), FadeOut(full_name),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 7: 生活中的平方米
    # ------------------------------------------------------------------

    def scene_7_life_m(self):
        title = Text("生活中的平方米", font=FONT, font_size=36, color=COLOR_M)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        tip = Text(
            "大约有多大?",
            font=FONT, font_size=26, color=GRAY_A,
        ).move_to(UP * 4.7)
        self.play(FadeIn(tip), run_time=0.4)

        # 门 示意
        door_bl = np.array([-3.5, -0.5, 0.0])
        door_w, door_h = 2.0, 3.5
        door = VGroup(
            Line(door_bl, door_bl + np.array([door_w, 0, 0]),
                 color=COLOR_LIFE, stroke_width=3),
            Line(door_bl + np.array([door_w, 0, 0]),
                 door_bl + np.array([door_w, door_h, 0]),
                 color=COLOR_LIFE, stroke_width=3),
            Line(door_bl + np.array([door_w, door_h, 0]),
                 door_bl + np.array([0, door_h, 0]),
                 color=COLOR_LIFE, stroke_width=3),
            Line(door_bl + np.array([0, door_h, 0]),
                 door_bl,
                 color=COLOR_LIFE, stroke_width=3),
        )
        door_knob = Circle(radius=0.1, color=COLOR_LIFE, stroke_width=2)
        door_knob.move_to(door_bl + np.array([door_w - 0.3, door_h / 2, 0]))
        door_label = Text("普通门\n(约2m²)", font=FONT, font_size=20, color=WHITE)
        door_label.move_to(door_bl + np.array([door_w / 2, -0.6, 0]))

        # m² 示意正方形 (右侧)
        m_sq_center = np.array([2.5, 2.0, 0.0])
        m_sq = Square(
            side_length=3.0,
            color=COLOR_M, stroke_width=4,
            fill_color=COLOR_M, fill_opacity=0.2,
        ).move_to(m_sq_center)
        m_label = MathTex(r"1\,\mathrm{m}^2", font_size=30, color=COLOR_M)
        m_label.move_to(m_sq_center)

        explain = Text(
            "1平方米\n大约是一扇门一半的大小",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 4.5)

        self.play(Create(door), FadeIn(door_knob), run_time=0.8)
        self.play(FadeIn(door_label), run_time=0.4)
        self.play(Create(m_sq), FadeIn(m_label), run_time=0.7)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(tip),
            FadeOut(door), FadeOut(door_knob), FadeOut(door_label),
            FadeOut(m_sq), FadeOut(m_label), FadeOut(explain),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 8: 三者对比总结
    # ------------------------------------------------------------------

    def scene_8_comparison(self):
        title = Text("面积单位对比", font=FONT, font_size=38, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # --- cm² ---
        cm_sq = Square(
            side_length=0.8,
            color=COLOR_CM, stroke_width=3,
            fill_color=COLOR_CM, fill_opacity=0.3,
        )
        cm_label_name = Text("平方厘米", font=FONT, font_size=22, color=COLOR_CM)
        cm_label_sym  = MathTex(r"1\,\mathrm{cm}^2", font_size=24, color=COLOR_CM)
        cm_label_side = VGroup(
            Text("边长:", font=FONT, font_size=18, color=GRAY_A),
            Text("1 厘米", font=FONT, font_size=18, color=COLOR_CM),
        ).arrange(RIGHT, buff=0.1)
        cm_col = VGroup(cm_sq, cm_label_name, cm_label_sym, cm_label_side).arrange(
            DOWN, buff=0.2, aligned_edge=ORIGIN
        )

        # --- dm² ---
        dm_sq = Square(
            side_length=1.6,
            color=COLOR_DM, stroke_width=3,
            fill_color=COLOR_DM, fill_opacity=0.3,
        )
        dm_label_name = Text("平方分米", font=FONT, font_size=22, color=COLOR_DM)
        dm_label_sym  = MathTex(r"1\,\mathrm{dm}^2", font_size=24, color=COLOR_DM)
        dm_label_side = VGroup(
            Text("边长:", font=FONT, font_size=18, color=GRAY_A),
            Text("1 分米", font=FONT, font_size=18, color=COLOR_DM),
        ).arrange(RIGHT, buff=0.1)
        dm_col = VGroup(dm_sq, dm_label_name, dm_label_sym, dm_label_side).arrange(
            DOWN, buff=0.2, aligned_edge=ORIGIN
        )

        # --- m² ---
        m_sq = Square(
            side_length=2.4,
            color=COLOR_M, stroke_width=3,
            fill_color=COLOR_M, fill_opacity=0.3,
        )
        m_label_name = Text("平方米", font=FONT, font_size=22, color=COLOR_M)
        m_label_sym  = MathTex(r"1\,\mathrm{m}^2", font_size=24, color=COLOR_M)
        m_label_side = VGroup(
            Text("边长:", font=FONT, font_size=18, color=GRAY_A),
            Text("1 米", font=FONT, font_size=18, color=COLOR_M),
        ).arrange(RIGHT, buff=0.1)
        m_col = VGroup(m_sq, m_label_name, m_label_sym, m_label_side).arrange(
            DOWN, buff=0.2, aligned_edge=ORIGIN
        )

        # 水平排列三列
        compare_group = VGroup(cm_col, dm_col, m_col).arrange(
            RIGHT, buff=0.5, aligned_edge=DOWN
        ).move_to(UP * 1.0)

        # 依次出现
        self.play(FadeIn(cm_col, shift=UP * 0.3), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(dm_col, shift=UP * 0.3), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(m_col, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)

        # 闪烁强调
        self.play(
            Indicate(cm_sq, color=COLOR_CM, scale_factor=1.1),
            Indicate(dm_sq, color=COLOR_DM, scale_factor=1.1),
            Indicate(m_sq,  color=COLOR_M,  scale_factor=1.1),
            run_time=1.0,
        )

        # 底部总结公式
        formula_group = VGroup(
            VGroup(
                MathTex(r"1\,\mathrm{cm}^2", font_size=26, color=COLOR_CM),
                MathTex(r"<", font_size=26, color=WHITE),
                MathTex(r"1\,\mathrm{dm}^2", font_size=26, color=COLOR_DM),
                MathTex(r"<", font_size=26, color=WHITE),
                MathTex(r"1\,\mathrm{m}^2",  font_size=26, color=COLOR_M),
            ).arrange(RIGHT, buff=0.18),
        ).move_to(DOWN * 3.8)

        self.play(FadeIn(formula_group, shift=UP * 0.3), run_time=0.6)

        # 小是大概几个对比
        ratio_text = VGroup(
            Text("1 dm² = 100 cm²", font=FONT, font_size=20, color=GRAY_A),
            Text("1 m² = 100 dm²", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 5.0)

        self.play(FadeIn(ratio_text, shift=UP * 0.2), run_time=0.5)
        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(compare_group),
            FadeOut(formula_group), FadeOut(ratio_text),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 9: 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        # 知识小结卡片
        card_bg = RoundedRectangle(
            width=7.5, height=8.5,
            corner_radius=0.3,
            color=WHITE, stroke_width=2,
            fill_color=WHITE, fill_opacity=0.05,
        ).move_to(UP * 2.0)
        self.play(FadeIn(card_bg), run_time=0.4)

        summary_title = Text("知识总结", font=FONT, font_size=32, color=COLOR_HL)
        summary_title.move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.5)

        # 三条总结
        row1 = VGroup(
            Text("▶ 平方厘米", font=FONT, font_size=24, color=COLOR_CM),
            VGroup(
                MathTex(r"(\mathrm{cm}^2)", font_size=22, color=COLOR_CM),
                Text(": 边长 1 cm 的正方形", font=FONT, font_size=20, color=GRAY_A),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.2)

        row2 = VGroup(
            Text("▶ 平方分米", font=FONT, font_size=24, color=COLOR_DM),
            VGroup(
                MathTex(r"(\mathrm{dm}^2)", font_size=22, color=COLOR_DM),
                Text(": 边长 1 dm 的正方形", font=FONT, font_size=20, color=GRAY_A),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.2)

        row3 = VGroup(
            Text("▶ 平方米", font=FONT, font_size=24, color=COLOR_M),
            VGroup(
                MathTex(r"(\mathrm{m}^2)", font_size=22, color=COLOR_M),
                Text(": 边长 1 m 的正方形", font=FONT, font_size=20, color=GRAY_A),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.2)

        rows = VGroup(row1, row2, row3).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        rows.move_to(UP * 2.3)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.2)

        self.wait(1.0)

        # 过渡到作者信息
        self.play(FadeOut(card_bg), FadeOut(summary_title), FadeOut(rows), run_time=0.5)

        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE,
        ).move_to(UP * 1.0)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(ORIGIN)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 获得更多数学技巧!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 小正方形装饰
        decorations = VGroup()
        colors = [COLOR_CM, COLOR_DM, COLOR_M, COLOR_CM, COLOR_DM, COLOR_M]
        sizes  = [0.3, 0.45, 0.6, 0.3, 0.45, 0.6]
        for i in range(6):
            angle_val = i * PI / 3
            pos = DOWN * 3.5 + 2.2 * np.array([np.cos(angle_val), np.sin(angle_val), 0.0])
            deco = Square(
                side_length=sizes[i],
                color=colors[i], stroke_width=2,
                fill_color=colors[i], fill_opacity=0.4,
            ).move_to(pos)
            decorations.add(deco)

        self.play(*[FadeIn(d, scale=0.5) for d in decorations], run_time=0.6)
        self.play(Rotate(decorations, angle=PI, run_time=1.5))
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(decorations),
            run_time=1.0,
        )


# 运行命令:
# manim -pql 002_面积单位.py AreaUnitLesson   # 快速预览
# manim -qm  002_面积单位.py AreaUnitLesson   # 中等质量 (720p)
# manim -qh  002_面积单位.py AreaUnitLesson   # 高质量 (1080p)
