"""
001_分数的再认识.py — 分数的再认识 教学动画

知识点:
  - 单位"1"可以是一个物体 (一个圆、一个苹果、一条线段)
  - 单位"1"也可以是多个物体组成的整体 (一堆苹果的1/4)
  - 分数 = 把"整体"平均分若干份, 取其中的几份
  - 分子、分母的含义深化

年级: 三年级下册
格式: TikTok 竖屏 (1080×1920)
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
BG_COLOR = "#1a1a2e"
COLOR_PRIMARY   = "#3b82f6"   # 蓝色 - 主色
COLOR_ACCENT    = "#f59e0b"   # 橙色 - 强调
COLOR_GREEN     = "#22c55e"   # 绿色 - 已选部分
COLOR_RED       = "#ef4444"   # 红色 - 对比
COLOR_PURPLE    = "#a78bfa"   # 紫色 - 分数标注
COLOR_HL        = "#fbbf24"   # 黄色 - 高亮
COLOR_UNIT1     = "#06b6d4"   # 青色 - 单位"1"
COLOR_AUTHOR    = "#6b7280"   # 灰色 - 作者
FONT            = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class FractionRevisitLesson(Scene):
    """
    分数的再认识教学动画

    场景顺序:
      1. 开场钩子 - 什么是分数的"整体"?
      2. 回顾 - 把一个物体平均分
      3. 深化 - 把一组物体当作整体
      4. 对比 - 同样是1/4, 整体不同, 结果不同
      5. 分数意义总结
      6. 例题练习
      7. 知识总结卡片
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_single_object()
        self.scene_3_group_as_whole()
        self.scene_4_comparison()
        self.scene_5_fraction_meaning()
        self.scene_6_practice()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化几何坐标和尺寸常量"""

        # 圆形分割参数
        self.circle_radius = 1.5
        self.circle_center = np.array([0.0, 2.0, 0.0])

        # 苹果网格参数 (4行×2列 = 8个苹果)
        self.apple_radius = 0.3
        self.apple_cols = 4
        self.apple_rows = 2
        self.apple_spacing_x = 0.9
        self.apple_spacing_y = 0.9

        # 线段参数
        self.seg_start = np.array([-3.5, 2.0, 0.0])
        self.seg_end   = np.array([ 3.5, 2.0, 0.0])

        # 验证
        self._verify_geometry()

    def _verify_geometry(self):
        """验证几何参数"""
        # 苹果格子总数应能整除演示的分母
        total_apples = self.apple_cols * self.apple_rows
        assert total_apples % 4 == 0, f"苹果总数 {total_apples} 无法被4整除"
        print("Geometry verification passed. Total apples:", total_apples)

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

    def make_apple(self, center, color=COLOR_GREEN, fill_opacity=0.85):
        """创建一个苹果图标 (圆形代替)"""
        body = Circle(
            radius=self.apple_radius,
            color=color,
            fill_color=color,
            fill_opacity=fill_opacity,
            stroke_width=2,
        ).move_to(center)
        stem = Line(
            center + UP * self.apple_radius,
            center + UP * (self.apple_radius + 0.15),
            color=COLOR_ACCENT,
            stroke_width=3,
        )
        leaf = Arc(
            radius=0.12,
            start_angle=0,
            angle=PI,
            color=COLOR_GREEN,
            stroke_width=2,
        ).move_to(center + UP * (self.apple_radius + 0.08) + RIGHT * 0.1)
        return VGroup(body, stem, leaf)

    def make_apple_grid(self, center=ORIGIN, rows=2, cols=4,
                        sx=0.9, sy=0.9, color=COLOR_GREEN):
        """创建苹果网格"""
        grid = VGroup()
        total_w = (cols - 1) * sx
        total_h = (rows - 1) * sy
        for r in range(rows):
            for c in range(cols):
                x = center[0] - total_w / 2 + c * sx
                y = center[1] + total_h / 2 - r * sy
                apple = self.make_apple(np.array([x, y, 0.0]), color=color)
                grid.add(apple)
        return grid

    def make_fraction(self, numerator_str, denominator_str, font_size=40, color=WHITE):
        """创建分数显示 (数字 + 横线 + 数字)"""
        num = Text(numerator_str, font=FONT, font_size=font_size, color=color)
        bar = Line(LEFT * 0.4, RIGHT * 0.4, color=color, stroke_width=3)
        den = Text(denominator_str, font=FONT, font_size=font_size, color=color)
        frac = VGroup(num, bar, den).arrange(DOWN, buff=0.08)
        return frac

    def make_dividing_lines_circle(self, center, radius, n, color=WHITE):
        """在圆内画n等分线"""
        lines = VGroup()
        for i in range(n):
            angle = i * TAU / n
            end_pt = center + radius * np.array([np.cos(angle), np.sin(angle), 0.0])
            line = Line(center, end_pt, color=color, stroke_width=2)
            lines.add(line)
        return lines

    def make_pie_sector(self, center, radius, start_frac, end_frac,
                        color=COLOR_GREEN, fill_opacity=0.8):
        """创建扇形 (start_frac, end_frac 均为 [0,1] 比例)"""
        start_angle = PI / 2 - start_frac * TAU
        arc_angle   = -(end_frac - start_frac) * TAU
        sector = Sector(
            radius=radius,
            start_angle=start_angle,
            angle=arc_angle,
            color=color,
            fill_color=color,
            fill_opacity=fill_opacity,
            stroke_width=0,
        )
        sector.move_to(center)
        return sector

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "1/4 一定是这么多吗?",
            font=FONT, font_size=38, color=COLOR_HL,
        ).move_to(UP * 5.5)

        self.play(Write(hook), run_time=0.8)
        self.wait(0.3)

        # 快速展示两个"1/4"的对比场景
        # 左: 一个圆分成4份取1份
        circle_left = Circle(
            radius=1.0, color=COLOR_PRIMARY,
            fill_color=BG_COLOR, fill_opacity=1,
            stroke_width=3,
        ).move_to(LEFT * 2.2 + UP * 2.8)

        sector_left = self.make_pie_sector(
            LEFT * 2.2 + UP * 2.8, 1.0, 0, 0.25,
            color=COLOR_GREEN, fill_opacity=0.85,
        )

        frac_left = self.make_fraction("1", "4", font_size=32, color=COLOR_GREEN)
        frac_left.move_to(LEFT * 2.2 + UP * 1.4)

        # 右: 8个苹果取2个(1/4)
        apple_mini_group = VGroup()
        mini_positions = [
            RIGHT * 0.5 + UP * 3.2, RIGHT * 1.2 + UP * 3.2, RIGHT * 1.9 + UP * 3.2, RIGHT * 2.6 + UP * 3.2,
            RIGHT * 0.5 + UP * 2.4, RIGHT * 1.2 + UP * 2.4, RIGHT * 1.9 + UP * 2.4, RIGHT * 2.6 + UP * 2.4,
        ]
        for i, pos in enumerate(mini_positions):
            c = COLOR_GREEN if i < 2 else GRAY_B
            apple_mini = Circle(
                radius=0.25, color=c, fill_color=c,
                fill_opacity=0.85, stroke_width=1.5,
            ).move_to(pos)
            apple_mini_group.add(apple_mini)

        frac_right = self.make_fraction("1", "4", font_size=32, color=COLOR_GREEN)
        frac_right.move_to(RIGHT * 1.55 + UP * 1.4)

        self.play(
            Create(circle_left),
            run_time=0.5,
        )
        self.play(
            FadeIn(sector_left, scale=0.5),
            run_time=0.5,
        )
        self.play(
            FadeIn(apple_mini_group, lag_ratio=0.05),
            run_time=0.6,
        )

        self.play(
            FadeIn(frac_left, shift=UP * 0.2),
            FadeIn(frac_right, shift=UP * 0.2),
            run_time=0.5,
        )

        # 两者之间画不等号
        neq = Text("≠", font=FONT, font_size=36, color=COLOR_RED).move_to(UP * 2.8)
        self.play(FadeIn(neq), run_time=0.4)

        sub_hook = Text(
            "整体不同, 1/4的大小也不同!",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(UP * 0.5)
        self.play(FadeIn(sub_hook, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(circle_left), FadeOut(sector_left),
            FadeOut(apple_mini_group),
            FadeOut(frac_left), FadeOut(frac_right),
            FadeOut(neq), FadeOut(sub_hook),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 把一个物体平均分 (单位"1" = 单个)
    # ------------------------------------------------------------------

    def scene_2_single_object(self):
        title = Text(
            "单位\"1\" = 一个物体",
            font=FONT, font_size=34, color=COLOR_UNIT1,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        subtitle = Text(
            "把一个圆平均分成4份",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.7)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 画圆
        center = np.array([0.0, 2.0, 0.0])
        radius = 2.0
        circle = Circle(
            radius=radius, color=COLOR_PRIMARY,
            fill_color="#0f2547", fill_opacity=1,
            stroke_width=4,
        ).move_to(center)
        self.play(Create(circle), run_time=0.8)

        # 单位"1"标注
        unit1_label = Text("整体 (单位\"1\")", font=FONT, font_size=22, color=COLOR_UNIT1)
        unit1_label.next_to(circle, DOWN, buff=0.3)
        unit1_box = SurroundingRectangle(
            circle,
            color=COLOR_UNIT1,
            stroke_width=2.5,
            corner_radius=0.1,
            buff=0.15,
        )
        self.play(Create(unit1_box), FadeIn(unit1_label), run_time=0.6)
        self.wait(0.8)

        # 画4等分线
        div_lines = VGroup()
        for i in range(4):
            angle = i * PI / 2  # 0, 90, 180, 270度
            end = center + radius * np.array([np.cos(angle), np.sin(angle), 0.0])
            dl = DashedLine(
                center, end,
                color=WHITE, dash_length=0.15, stroke_width=2,
            )
            div_lines.add(dl)

        self.play(Create(div_lines), run_time=0.8)

        split_text = Text(
            "平均分成4份, 每份是 1/4",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(split_text), run_time=0.4)
        self.wait(0.6)

        # 填色第1份 (右上扇形)
        sector_highlight = self.make_pie_sector(
            center, radius, 0, 0.25,
            color=COLOR_GREEN, fill_opacity=0.85,
        )
        self.play(FadeIn(sector_highlight), run_time=0.6)

        # 分数标注
        frac_label = VGroup(
            Text("取出其中", font=FONT, font_size=22, color=GRAY_A),
            self.make_fraction("1", "4", font_size=36, color=COLOR_GREEN),
        ).arrange(RIGHT, buff=0.25).move_to(DOWN * 4.5)

        self.play(FadeIn(frac_label, shift=UP * 0.2), run_time=0.6)

        # 指示箭头
        arrow_to_sector = Arrow(
            frac_label.get_top() + UP * 0.1,
            center + np.array([0.8, 0.8, 0.0]),
            color=COLOR_GREEN,
            stroke_width=2.5,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(Create(arrow_to_sector), run_time=0.5)

        # 高亮闪烁
        self.play(
            Indicate(sector_highlight, color=COLOR_HL, scale_factor=1.05),
            run_time=0.8,
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(circle), FadeOut(unit1_box), FadeOut(unit1_label),
            FadeOut(div_lines), FadeOut(sector_highlight),
            FadeOut(split_text), FadeOut(frac_label), FadeOut(arrow_to_sector),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 3: 把一组物体当作整体
    # ------------------------------------------------------------------

    def scene_3_group_as_whole(self):
        title = Text(
            "单位\"1\" 也可以是一组物体!",
            font=FONT, font_size=30, color=COLOR_UNIT1,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        subtitle = Text(
            "把8个苹果看作一个整体",
            font=FONT, font_size=24, color=GRAY_A,
        ).move_to(UP * 4.7)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 8个苹果网格 (2行4列)
        grid_center = np.array([0.0, 2.0, 0.0])
        apples = self.make_apple_grid(
            center=grid_center, rows=2, cols=4,
            sx=1.0, sy=1.0, color=GRAY_C,
        )
        self.play(FadeIn(apples, lag_ratio=0.06), run_time=1.2)

        # 单位"1"框
        unit1_box = SurroundingRectangle(
            apples,
            color=COLOR_UNIT1,
            stroke_width=2.5,
            corner_radius=0.2,
            buff=0.2,
        )
        unit1_label = Text("整体 (单位\"1\")", font=FONT, font_size=22, color=COLOR_UNIT1)
        unit1_label.next_to(unit1_box, DOWN, buff=0.2)

        self.play(Create(unit1_box), FadeIn(unit1_label), run_time=0.6)
        self.wait(0.5)

        # 平均分成4组 (每组2个)
        group_explain = Text(
            "平均分成4组, 每组2个苹果",
            font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(group_explain), run_time=0.4)

        # 画竖线分隔4组
        group_lines = VGroup()
        top_y = grid_center[1] + 0.7
        bot_y = grid_center[1] - 0.7
        xs = [-1.5, -0.5, 0.5]   # 3条竖线把4列分开
        for x in xs:
            gl = DashedLine(
                np.array([x, top_y, 0.0]),
                np.array([x, bot_y, 0.0]),
                color=COLOR_ACCENT,
                dash_length=0.12,
                stroke_width=2.5,
            )
            group_lines.add(gl)

        self.play(Create(group_lines), run_time=0.6)
        self.wait(0.6)

        # 高亮第一组 (左边2个苹果)
        highlight_group = VGroup()
        for i, apple in enumerate(apples):
            col = i % 4
            if col == 0:
                highlight_group.add(apple)

        # 将第一组苹果变绿色
        self.play(
            *[apple[0].animate.set_fill(COLOR_GREEN).set_color(COLOR_GREEN)
              for apple in highlight_group],
            run_time=0.6,
        )

        # 分数标注
        frac_group = VGroup(
            Text("取出", font=FONT, font_size=22, color=GRAY_A),
            self.make_fraction("1", "4", font_size=36, color=COLOR_GREEN),
            Text("就是2个苹果", font=FONT, font_size=22, color=GRAY_A),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 4.2)

        self.play(FadeIn(frac_group, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(apples), FadeOut(unit1_box), FadeOut(unit1_label),
            FadeOut(group_explain), FadeOut(group_lines),
            FadeOut(frac_group),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 4: 对比 - 整体不同, 1/4不同
    # ------------------------------------------------------------------

    def scene_4_comparison(self):
        title = Text(
            "整体不同, 分数的量不同!",
            font=FONT, font_size=30, color=COLOR_HL,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        # ---- 左侧: 1个苹果的1/4 ----
        left_center = np.array([-2.2, 2.5, 0.0])

        big_apple_body = Circle(
            radius=0.9, color=COLOR_GREEN,
            fill_color=COLOR_GREEN, fill_opacity=0.2,
            stroke_width=3,
        ).move_to(left_center)
        # 扇形填色 1/4
        big_sector = self.make_pie_sector(
            left_center, 0.9, 0, 0.25,
            color=COLOR_GREEN, fill_opacity=0.9,
        )

        left_label = Text("1个苹果", font=FONT, font_size=20, color=GRAY_A)
        left_label.next_to(big_apple_body, UP, buff=0.3)

        left_frac = self.make_fraction("1", "4", font_size=32, color=COLOR_GREEN)
        left_frac.next_to(big_apple_body, DOWN, buff=0.4)

        # ---- 右侧: 8个苹果的1/4 ----
        right_center = np.array([2.2, 2.5, 0.0])

        small_apples = VGroup()
        positions_8 = [
            np.array([1.4, 3.1, 0.0]), np.array([2.0, 3.1, 0.0]),
            np.array([2.6, 3.1, 0.0]), np.array([3.2, 3.1, 0.0]),
            np.array([1.4, 2.4, 0.0]), np.array([2.0, 2.4, 0.0]),
            np.array([2.6, 2.4, 0.0]), np.array([3.2, 2.4, 0.0]),
        ]
        for i, pos in enumerate(positions_8):
            c = COLOR_GREEN if i < 2 else GRAY_C
            a = Circle(
                radius=0.22, color=c,
                fill_color=c, fill_opacity=0.85,
                stroke_width=1.5,
            ).move_to(pos)
            small_apples.add(a)

        right_label = Text("8个苹果", font=FONT, font_size=20, color=GRAY_A)
        right_label.move_to(right_center + UP * 0.95)

        right_frac = self.make_fraction("1", "4", font_size=32, color=COLOR_GREEN)
        right_frac.move_to(right_center + DOWN * 1.05)

        # 中间分隔线
        sep_line = DashedLine(
            np.array([0.0, 5.2, 0.0]),
            np.array([0.0, 0.5, 0.0]),
            color=GRAY_B, dash_length=0.15, stroke_width=1.5,
        )

        self.play(
            Create(sep_line),
            FadeIn(left_label), FadeIn(right_label),
            run_time=0.5,
        )
        self.play(
            Create(big_apple_body), FadeIn(big_sector),
            FadeIn(small_apples, lag_ratio=0.05),
            run_time=0.8,
        )
        self.play(
            FadeIn(left_frac, shift=UP * 0.2),
            FadeIn(right_frac, shift=UP * 0.2),
            run_time=0.6,
        )
        self.wait(0.5)

        # 展示结果不一样
        left_result = Text("= 苹果的1/4份", font=FONT, font_size=18, color=COLOR_GREEN)
        left_result.next_to(left_frac, DOWN, buff=0.3)

        right_result = Text("= 2个苹果", font=FONT, font_size=18, color=COLOR_GREEN)
        right_result.next_to(right_frac, DOWN, buff=0.3)

        self.play(
            FadeIn(left_result, shift=UP * 0.15),
            FadeIn(right_result, shift=UP * 0.15),
            run_time=0.6,
        )
        self.wait(0.5)

        # 关键结论
        conclusion = VGroup(
            Text("整体越大,", font=FONT, font_size=26, color=COLOR_HL),
            Text("对应的分数就越大!", font=FONT, font_size=26, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.8)

        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.6)

        # 指出关键
        key_box = SurroundingRectangle(
            conclusion, color=COLOR_HL, stroke_width=2.5, corner_radius=0.2,
        )
        self.play(Create(key_box), run_time=0.5)

        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(sep_line),
            FadeOut(left_label), FadeOut(right_label),
            FadeOut(big_apple_body), FadeOut(big_sector),
            FadeOut(small_apples),
            FadeOut(left_frac), FadeOut(right_frac),
            FadeOut(left_result), FadeOut(right_result),
            FadeOut(conclusion), FadeOut(key_box),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 5: 分数的意义 (分子分母的含义)
    # ------------------------------------------------------------------

    def scene_5_fraction_meaning(self):
        title = Text(
            "分数的意义",
            font=FONT, font_size=36, color=COLOR_PRIMARY,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 画一个大分数
        big_num = Text("3", font=FONT, font_size=70, color=COLOR_GREEN)
        big_bar = Line(LEFT * 1.2, RIGHT * 1.2, color=WHITE, stroke_width=4)
        big_den = Text("4", font=FONT, font_size=70, color=COLOR_ACCENT)
        big_frac = VGroup(big_num, big_bar, big_den).arrange(DOWN, buff=0.15)
        big_frac.move_to(UP * 3.0)

        self.play(FadeIn(big_frac, scale=0.7), run_time=0.8)
        self.wait(0.3)

        # 分母标注
        den_arrow = Arrow(
            big_den.get_right() + RIGHT * 0.15,
            big_den.get_right() + RIGHT * 1.8,
            color=COLOR_ACCENT,
            stroke_width=2.5,
            buff=0.05,
            max_tip_length_to_length_ratio=0.2,
        )
        den_label = VGroup(
            Text("分母", font=FONT, font_size=22, color=COLOR_ACCENT),
            Text("把整体平均分成", font=FONT, font_size=18, color=GRAY_A),
            Text("4 份", font=FONT, font_size=20, color=COLOR_ACCENT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        den_label.next_to(den_arrow, RIGHT, buff=0.1)

        self.play(Create(den_arrow), FadeIn(den_label), run_time=0.6)
        self.wait(0.6)

        # 分子标注
        num_arrow = Arrow(
            big_num.get_right() + RIGHT * 0.15,
            big_num.get_right() + RIGHT * 1.8,
            color=COLOR_GREEN,
            stroke_width=2.5,
            buff=0.05,
            max_tip_length_to_length_ratio=0.2,
        )
        num_label = VGroup(
            Text("分子", font=FONT, font_size=22, color=COLOR_GREEN),
            Text("取其中的", font=FONT, font_size=18, color=GRAY_A),
            Text("3 份", font=FONT, font_size=20, color=COLOR_GREEN),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        num_label.next_to(num_arrow, RIGHT, buff=0.1)

        self.play(Create(num_arrow), FadeIn(num_label), run_time=0.6)
        self.wait(0.6)

        # 可视化 3/4: 4个等份矩形取3个
        rect_center = np.array([0.0, -1.5, 0.0])
        rect_w, rect_h = 1.2, 0.9
        rects = VGroup()
        for i in range(4):
            x = rect_center[0] - 1.8 + i * (rect_w + 0.1)
            fill_c = COLOR_GREEN if i < 3 else GRAY_D
            r = Rectangle(
                width=rect_w, height=rect_h,
                color=WHITE, stroke_width=2.5,
                fill_color=fill_c, fill_opacity=0.85,
            ).move_to(np.array([x, rect_center[1], 0.0]))
            rects.add(r)

        rects_label = VGroup(
            Text("4等份中取3份", font=FONT, font_size=22, color=GRAY_A),
            Text("= 整体的 3/4", font=FONT, font_size=22, color=COLOR_GREEN),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.0)

        self.play(FadeIn(rects, lag_ratio=0.1), run_time=0.8)
        self.play(FadeIn(rects_label, shift=UP * 0.2), run_time=0.5)

        # 高亮前3个
        self.play(
            *[Indicate(rects[i], color=COLOR_HL, scale_factor=1.08) for i in range(3)],
            run_time=0.8,
        )
        self.wait(1.5)

        # 核心口诀
        key_text = VGroup(
            Text("把整体平均分成若干份,", font=FONT, font_size=20, color=GRAY_A),
            Text("取其中一份或几份,", font=FONT, font_size=20, color=GRAY_A),
            Text("就是整体的几分之几", font=FONT, font_size=20, color=COLOR_HL),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).move_to(DOWN * 4.8)

        self.play(FadeIn(key_text, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(big_frac),
            FadeOut(den_arrow), FadeOut(den_label),
            FadeOut(num_arrow), FadeOut(num_label),
            FadeOut(rects), FadeOut(rects_label),
            FadeOut(key_text),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 6: 例题练习
    # ------------------------------------------------------------------

    def scene_6_practice(self):
        title = Text(
            "来做一道题!",
            font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 题目
        q_line1 = Text(
            "12个草莓, 把它们看作一个整体,",
            font=FONT, font_size=22, color=WHITE,
        )
        q_line2 = VGroup(
            Text("它的", font=FONT, font_size=22, color=WHITE),
            self.make_fraction("1", "3", font_size=28, color=COLOR_ACCENT),
            Text("是多少个?", font=FONT, font_size=22, color=WHITE),
        ).arrange(RIGHT, buff=0.15)
        question = VGroup(q_line1, q_line2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        question.move_to(UP * 4.2)

        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.6)
        self.wait(0.5)

        # 画12个草莓 (3行4列)
        berry_center = np.array([0.0, 1.8, 0.0])
        berries = VGroup()
        berry_positions = []
        rows, cols = 3, 4
        for r in range(rows):
            for c in range(cols):
                x = berry_center[0] - 1.5 + c * 1.0
                y = berry_center[1] + 1.0 - r * 1.0
                berry_positions.append(np.array([x, y, 0.0]))
                b = Circle(
                    radius=0.28, color=COLOR_RED,
                    fill_color=COLOR_RED, fill_opacity=0.85,
                    stroke_width=2,
                ).move_to(np.array([x, y, 0.0]))
                berries.add(b)

        self.play(FadeIn(berries, lag_ratio=0.04), run_time=1.0)

        # 框选整体
        whole_box = SurroundingRectangle(
            berries, color=COLOR_UNIT1,
            stroke_width=2.5, corner_radius=0.2, buff=0.2,
        )
        whole_label = Text("整体12个", font=FONT, font_size=20, color=COLOR_UNIT1)
        whole_label.next_to(whole_box, DOWN, buff=0.2)

        self.play(Create(whole_box), FadeIn(whole_label), run_time=0.5)
        self.wait(0.5)

        # 分成3组
        step1 = Text(
            "第一步: 平均分成3组, 每组4个",
            font=FONT, font_size=20, color=GRAY_A,
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(step1), run_time=0.4)

        # 画2条竖线分3列
        div1 = DashedLine(
            np.array([-0.5, 2.6, 0.0]),
            np.array([-0.5, 0.8, 0.0]),
            color=COLOR_ACCENT, dash_length=0.12, stroke_width=2.5,
        )
        div2 = DashedLine(
            np.array([0.5, 2.6, 0.0]),
            np.array([0.5, 0.8, 0.0]),
            color=COLOR_ACCENT, dash_length=0.12, stroke_width=2.5,
        )
        self.play(Create(div1), Create(div2), run_time=0.5)
        self.wait(0.5)

        # 第二步: 取第一组 (前4个草莓)
        step2 = Text(
            "第二步: 取其中1组 = 4个",
            font=FONT, font_size=20, color=COLOR_GREEN,
        ).move_to(DOWN * 4.3)
        self.play(FadeIn(step2), run_time=0.4)

        # 高亮第一组 (col=0 的4个)
        for i, b in enumerate(berries):
            if i % 4 == 0:
                self.play(
                    b.animate.set_fill(COLOR_GREEN).set_color(COLOR_GREEN),
                    run_time=0.15,
                )

        # 答案
        answer = VGroup(
            Text("答:", font=FONT, font_size=26, color=WHITE),
            self.make_fraction("1", "3", font_size=32, color=COLOR_ACCENT),
            Text("是", font=FONT, font_size=26, color=WHITE),
            Text("4", font=FONT, font_size=32, color=COLOR_GREEN),
            Text("个草莓", font=FONT, font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 5.3)

        self.play(FadeIn(answer, shift=UP * 0.2), run_time=0.6)

        # 高亮答案
        answer_box = SurroundingRectangle(
            answer, color=COLOR_GREEN, stroke_width=2.5, corner_radius=0.2,
        )
        self.play(Create(answer_box), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(question),
            FadeOut(berries), FadeOut(whole_box), FadeOut(whole_label),
            FadeOut(step1), FadeOut(div1), FadeOut(div2),
            FadeOut(step2), FadeOut(answer), FadeOut(answer_box),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 知识总结卡片
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        title = Text(
            "知识总结",
            font=FONT, font_size=36, color=COLOR_HL,
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 卡片背景
        card = RoundedRectangle(
            width=7.8, height=9.5,
            corner_radius=0.4,
            color=WHITE, stroke_width=2,
            fill_color="#0d1b3e", fill_opacity=1,
        ).move_to(UP * 0.2)
        self.play(FadeIn(card), run_time=0.4)

        # 条目1
        item1_t = Text("1. 单位\"1\" 是整体", font=FONT, font_size=26, color=COLOR_UNIT1)
        item1_b = VGroup(
            Text("可以是一个物体 (一个圆, 一条线段...)", font=FONT, font_size=18, color=GRAY_A),
            Text("也可以是多个物体的集合", font=FONT, font_size=18, color=GRAY_A),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        item1 = VGroup(item1_t, item1_b).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        item1.move_to(UP * 3.5 + LEFT * 0.2)
        self.play(FadeIn(item1, shift=RIGHT * 0.3), run_time=0.5)

        # 分隔线
        sep1 = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_D, stroke_width=1).move_to(UP * 2.2)
        self.play(Create(sep1), run_time=0.3)

        # 条目2
        item2_t = Text("2. 分数的意义", font=FONT, font_size=26, color=COLOR_PRIMARY)
        item2_b = VGroup(
            Text("把整体平均分成若干份,", font=FONT, font_size=18, color=GRAY_A),
            Text("取其中的几份就是几分之几", font=FONT, font_size=18, color=COLOR_PRIMARY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        item2 = VGroup(item2_t, item2_b).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        item2.move_to(UP * 1.4 + LEFT * 0.2)
        self.play(FadeIn(item2, shift=RIGHT * 0.3), run_time=0.5)

        # 分隔线
        sep2 = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_D, stroke_width=1).move_to(UP * 0.3)
        self.play(Create(sep2), run_time=0.3)

        # 条目3
        item3_t = Text("3. 整体不同, 分数的量不同", font=FONT, font_size=24, color=COLOR_HL)
        # 小示意图
        ex_left = VGroup(
            Circle(radius=0.35, color=COLOR_GREEN, fill_color=COLOR_GREEN, fill_opacity=0.3, stroke_width=2),
            Text("1个苹果的1/4", font=FONT, font_size=14, color=GRAY_A),
        ).arrange(RIGHT, buff=0.2)

        ex_right = VGroup(
            *[Circle(radius=0.18,
                     color=(COLOR_GREEN if i < 2 else GRAY_C),
                     fill_color=(COLOR_GREEN if i < 2 else GRAY_C),
                     fill_opacity=0.85, stroke_width=1.5).shift(i * 0.42 * RIGHT)
              for i in range(8)],
        )
        ex_right_label = Text("8个苹果的1/4 = 2个", font=FONT, font_size=14, color=GRAY_A)
        ex_right_group = VGroup(ex_right, ex_right_label).arrange(RIGHT, buff=0.2)

        neq_sym = Text("≠", font=FONT, font_size=28, color=COLOR_RED)

        item3_b = VGroup(ex_left, neq_sym, ex_right_group).arrange(RIGHT, buff=0.25)
        item3 = VGroup(item3_t, item3_b).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item3.move_to(DOWN * 1.3 + LEFT * 0.2)
        self.play(FadeIn(item3, shift=RIGHT * 0.3), run_time=0.6)

        # 分隔线
        sep3 = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_D, stroke_width=1).move_to(DOWN * 2.4)
        self.play(Create(sep3), run_time=0.3)

        # 条目4
        item4_t = Text("4. 分子和分母", font=FONT, font_size=26, color=COLOR_PURPLE)
        item4_b = VGroup(
            VGroup(
                Text("分母:", font=FONT, font_size=18, color=COLOR_ACCENT),
                Text("整体被平均分的份数", font=FONT, font_size=18, color=GRAY_A),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("分子:", font=FONT, font_size=18, color=COLOR_GREEN),
                Text("取了其中的份数", font=FONT, font_size=18, color=GRAY_A),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        item4 = VGroup(item4_t, item4_b).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        item4.move_to(DOWN * 3.5 + LEFT * 0.2)
        self.play(FadeIn(item4, shift=RIGHT * 0.3), run_time=0.5)

        self.wait(3.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(card),
            FadeOut(item1), FadeOut(sep1),
            FadeOut(item2), FadeOut(sep2),
            FadeOut(item3), FadeOut(sep3),
            FadeOut(item4),
            run_time=0.7,
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        # 放大作者信息
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_B,
        ).move_to(UP * 0.5)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多数学知识!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 装饰: 分数圆盘
        deco_circles = VGroup()
        fractions = [(1, 2), (1, 3), (3, 4), (2, 5)]
        deco_positions = [
            DOWN * 2.8 + LEFT * 2.8,
            DOWN * 2.8 + LEFT * 0.9,
            DOWN * 2.8 + RIGHT * 0.9,
            DOWN * 2.8 + RIGHT * 2.8,
        ]
        colors = [COLOR_GREEN, COLOR_PRIMARY, COLOR_ACCENT, COLOR_PURPLE]
        for (n, d), pos, c in zip(fractions, deco_positions, colors):
            bg_c = Circle(
                radius=0.55, color=c,
                fill_color="#0f172a", fill_opacity=1,
                stroke_width=2.5,
            ).move_to(pos)
            sect = self.make_pie_sector(pos, 0.55, 0, n / d, color=c, fill_opacity=0.8)
            deco_circles.add(VGroup(bg_c, sect))

        self.play(
            *[FadeIn(d, scale=0.5) for d in deco_circles],
            run_time=0.7,
        )

        # 分数标注
        deco_labels = VGroup()
        label_strs = ["1/2", "1/3", "3/4", "2/5"]
        for i, (pos, s) in enumerate(zip(deco_positions, label_strs)):
            lbl = Text(s, font=FONT, font_size=16, color=colors[i])
            lbl.next_to(deco_circles[i], DOWN, buff=0.15)
            deco_labels.add(lbl)

        self.play(FadeIn(deco_labels), run_time=0.4)
        self.wait(2.0)

        # 全部淡出
        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco_circles), FadeOut(deco_labels),
            run_time=1.0,
        )


# ======================================================================
# 运行命令:
# manim -pql 001_分数的再认识.py FractionRevisitLesson   # 快速预览
# manim -qm  001_分数的再认识.py FractionRevisitLesson   # 中等质量
# manim -qh  001_分数的再认识.py FractionRevisitLesson   # 高质量
# ======================================================================
