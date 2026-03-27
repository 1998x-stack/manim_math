"""
003_圆的面积.py — 圆的面积 教学动画

知识点: 通过'剪拼法'将圆等分成若干个小扇形，拼成近似长方形，推导 S = pi*r^2
年级: 六年级第一学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

几何核心:
  圆: 半径 r, 圆心 O
  剪拼法: 将圆等分为 N 个扇形，交替排列拼成近似长方形
  近似长方形: 长 = 半周长 = pi*r, 宽 = r
  面积推导: S = pi*r * r = pi*r^2
  极限思想: 分割越细 (N越大), 越接近长方形
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
COLOR_CIRCLE = "#3b82f6"       # 蓝色圆
COLOR_SECTOR_A = "#ef4444"     # 红色扇形 (奇数)
COLOR_SECTOR_B = "#3b82f6"     # 蓝色扇形 (偶数)
COLOR_RECT = "#22c55e"         # 绿色长方形
COLOR_RADIUS = "#a78bfa"       # 紫色半径
COLOR_CIRCUM = "#f59e0b"       # 橙色周长
COLOR_HL = "#fbbf24"           # 黄色高亮
COLOR_AUTHOR = "#6b7280"       # 灰色作者信息
COLOR_FORMULA_BG = "#0f172a"   # 暗色公式背景
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class CircleAreaLesson(Scene):
    """
    圆的面积教学动画
    场景顺序:
      1. 开场钩子
      2. 认识圆的半径和周长
      3. 剪拼法 - 将圆切成扇形
      4. 拼成近似长方形 (少量分割)
      5. 极限思想 - 分割越细越接近长方形
      6. 推导面积公式
      7. 公式总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_radius_circumference()
        self.scene_3_cut_into_sectors()
        self.scene_4_rearrange()
        self.scene_5_limit_idea()
        self.scene_6_derive_formula()
        self.scene_7_formula_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """统一初始化所有几何参数"""

        # ===== 圆的基本参数 =====
        self.radius = 1.8
        self.circle_center = np.array([0.0, 2.0, 0.0])

        # ===== 扇形分割参数 =====
        self.num_sectors_demo = 8       # 初始演示用 8 等分
        self.num_sectors_fine = 24      # 精细分割用 24 等分

        # ===== 近似长方形参数 =====
        # 长 = pi * r (半周长)
        self.rect_length = np.pi * self.radius
        # 宽 = r
        self.rect_width = self.radius

        # ===== 验证 =====
        self._verify_geometry()

    def _verify_geometry(self):
        eps = 1e-9
        # 圆面积 = pi * r^2
        area_circle = np.pi * self.radius ** 2
        # 长方形面积 = 长 x 宽 = pi*r * r = pi*r^2
        area_rect = self.rect_length * self.rect_width
        assert abs(area_circle - area_rect) < eps, \
            f"面积不等: 圆={area_circle}, 长方形={area_rect}"
        print(f"  r = {self.radius}")
        print(f"  rect_length (pi*r) = {self.rect_length:.4f}")
        print(f"  rect_width (r) = {self.radius}")
        print(f"  area = {area_circle:.4f}")

    # ------------------------------------------------------------------
    # 辅助函数
    # ------------------------------------------------------------------

    def _create_circle(self, fill_opacity=0.3, **kw):
        """创建主圆"""
        return Circle(
            radius=self.radius,
            color=COLOR_CIRCLE,
            fill_color=COLOR_CIRCLE,
            fill_opacity=fill_opacity,
            stroke_width=3,
            **kw
        ).move_to(self.circle_center)

    def _create_sectors(self, n, center, radius, fill_opacity=0.7):
        """
        创建 n 个扇形，交替红蓝颜色
        返回 VGroup
        """
        sectors = VGroup()
        angle_per_sector = TAU / n
        for i in range(n):
            color = COLOR_SECTOR_A if i % 2 == 0 else COLOR_SECTOR_B
            sector = Sector(
                radius=radius,
                start_angle=i * angle_per_sector,
                angle=angle_per_sector,
                color=color,
                fill_color=color,
                fill_opacity=fill_opacity,
                stroke_width=1.5,
                stroke_color=WHITE,
                arc_center=center,
            )
            sectors.add(sector)
        return sectors

    def _create_rearranged_sectors(self, n, target_center, radius, scale=1.0):
        """
        创建拼合后的扇形排列 (近似长方形)
        偶数扇形朝上，奇数扇形朝下交替排列

        返回 VGroup of sectors in rearranged positions
        """
        sectors = VGroup()
        angle_per_sector = TAU / n
        # 每个扇形的弦宽 (近似) = 2 * r * sin(pi/n)
        chord_width = 2 * radius * np.sin(np.pi / n)

        half_n = n // 2
        # Total width of the rearranged shape
        total_width = half_n * chord_width
        start_x = target_center[0] - total_width / 2 + chord_width / 2

        for i in range(n):
            color = COLOR_SECTOR_A if i % 2 == 0 else COLOR_SECTOR_B
            sector = Sector(
                radius=radius * scale,
                start_angle=-angle_per_sector / 2,
                angle=angle_per_sector,
                color=color,
                fill_color=color,
                fill_opacity=0.7,
                stroke_width=1.5,
                stroke_color=WHITE,
                arc_center=ORIGIN,
            )

            # Position: alternate up and down
            col_index = i // 2
            x_pos = start_x + col_index * chord_width

            if i % 2 == 0:
                # Even sectors: point up, arc at bottom
                sector.rotate(PI / 2, about_point=ORIGIN)
                sector.move_to(np.array([
                    x_pos * scale,
                    target_center[1] - radius * scale / 2,
                    0
                ]), aligned_edge=DOWN)
            else:
                # Odd sectors: point down, arc at top
                sector.rotate(-PI / 2, about_point=ORIGIN)
                sector.move_to(np.array([
                    x_pos * scale,
                    target_center[1] + radius * scale / 2,
                    0
                ]), aligned_edge=UP)

            sectors.add(sector)
        return sectors

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '圆的面积怎么算？'"""

        # 作者信息 (顶部)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "圆的面积", font=FONT, font_size=48, color=WHITE
        ).move_to(UP * 5.5)
        hook2 = Text(
            "怎么算？", font=FONT, font_size=52, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.4)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 显示圆
        self.main_circle = self._create_circle()
        self.play(Create(self.main_circle), run_time=1.2)

        # 问号
        q = Text("?", font=FONT, font_size=72, color=COLOR_HL, weight=BOLD)
        q.move_to(self.circle_center)
        self.play(FadeIn(q, scale=0.4), run_time=0.4)
        self.wait(0.8)

        # 清理钩子，保留圆
        self.play(FadeOut(VGroup(hook1, hook2, q)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 认识半径和周长
    # ------------------------------------------------------------------

    def scene_2_radius_circumference(self):
        """标注半径 r 和周长 C = 2*pi*r"""

        title = Text(
            "认识圆的要素", font=FONT, font_size=36, color=WHITE
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 圆心
        center_dot = Dot(self.circle_center, color=WHITE, radius=0.06)
        center_label = Text(
            "O", font=FONT, font_size=22, color=WHITE
        ).next_to(center_dot, DL, buff=0.1)
        self.play(FadeIn(center_dot), FadeIn(center_label), run_time=0.4)

        # 半径线段
        radius_end = self.circle_center + RIGHT * self.radius
        radius_line = Line(
            self.circle_center, radius_end,
            color=COLOR_RADIUS, stroke_width=4
        )
        r_label = MathTex("r", font_size=32, color=COLOR_RADIUS).next_to(
            radius_line, DOWN, buff=0.15
        )

        step1 = Text(
            "半径 r", font=FONT, font_size=28, color=COLOR_RADIUS
        ).move_to(DOWN * 3.0)
        self.play(Create(radius_line), FadeIn(r_label), FadeIn(step1), run_time=0.8)
        self.wait(0.5)

        # 周长
        circumference = Circle(
            radius=self.radius, color=COLOR_CIRCUM, stroke_width=4
        ).move_to(self.circle_center)

        circ_formula = VGroup(
            Text("周长 C = ", font=FONT, font_size=26, color=COLOR_CIRCUM),
            MathTex(r"2\pi r", font_size=34, color=COLOR_CIRCUM)
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 4.0)

        half_circ_formula = VGroup(
            Text("半周长 = ", font=FONT, font_size=26, color=COLOR_CIRCUM),
            MathTex(r"\pi r", font_size=34, color=COLOR_CIRCUM)
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 5.0)

        self.play(
            FadeOut(step1),
            Create(circumference),
            run_time=1.0
        )
        self.play(FadeIn(circ_formula), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(half_circ_formula), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, center_dot, center_label,
                radius_line, r_label, circumference,
                circ_formula, half_circ_formula
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 剪拼法 - 将圆切成扇形
    # ------------------------------------------------------------------

    def scene_3_cut_into_sectors(self):
        """将圆等分成 8 个扇形"""

        title = Text(
            "剪拼法", font=FONT, font_size=44, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        step1 = Text(
            "把圆等分成小扇形", font=FONT, font_size=28, color=WHITE
        ).move_to(DOWN * 3.5)
        self.play(Write(step1), run_time=0.5)

        # Draw division lines on the circle
        n = self.num_sectors_demo  # 8
        division_lines = VGroup()
        for i in range(n):
            angle = i * TAU / n
            end_point = self.circle_center + self.radius * np.array([
                np.cos(angle), np.sin(angle), 0
            ])
            line = Line(
                self.circle_center, end_point,
                color=WHITE, stroke_width=1.5
            )
            division_lines.add(line)

        self.play(Create(division_lines), run_time=1.0)
        self.wait(0.3)

        # Color the sectors
        sectors = self._create_sectors(n, self.circle_center, self.radius)

        step2 = Text(
            "交替涂上红色和蓝色", font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 3.5)
        self.play(
            FadeOut(step1),
            FadeIn(step2, shift=UP * 0.2),
            run_time=0.4
        )
        self.play(
            FadeOut(self.main_circle),
            FadeOut(division_lines),
            FadeIn(sectors),
            run_time=0.8
        )
        self.wait(0.5)

        # Save for next scene
        self.sectors = sectors
        self.title_cut = title
        self.step_cut = step2

    # ------------------------------------------------------------------
    # Scene 4: 拼成近似长方形
    # ------------------------------------------------------------------

    def scene_4_rearrange(self):
        """将扇形交替排列拼成近似长方形"""

        step3 = Text(
            "交替排列，拼成近似长方形",
            font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 3.5)
        self.play(
            FadeOut(self.step_cut),
            FadeIn(step3, shift=UP * 0.2),
            run_time=0.4
        )

        # Create the rearranged sectors
        n = self.num_sectors_demo
        rearrange_center = np.array([0.0, 1.5, 0.0])
        rearranged = self._create_rearranged_sectors(
            n, rearrange_center, self.radius, scale=1.0
        )

        # Animate: transform sectors to rearranged positions
        self.play(
            Transform(self.sectors, rearranged),
            run_time=2.5,
            rate_func=smooth
        )
        self.wait(0.5)

        # Label the approximate rectangle
        # Show the "wavy" top and bottom
        note1 = Text(
            "上下边还是弧形的...", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(note1, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # Save references
        self.step_rearrange = step3
        self.note_wavy = note1

    # ------------------------------------------------------------------
    # Scene 5: 极限思想
    # ------------------------------------------------------------------

    def scene_5_limit_idea(self):
        """分割越细，越接近长方形"""

        step4 = Text(
            "分得越细，越接近长方形！",
            font=FONT, font_size=28, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.5)
        self.play(
            FadeOut(self.step_rearrange),
            FadeOut(self.note_wavy),
            FadeIn(step4, shift=UP * 0.2),
            run_time=0.5
        )

        rearrange_center = np.array([0.0, 1.5, 0.0])

        # Progressively refine: 8 -> 16 -> 24
        for n_sectors in [16, 24]:
            rearranged_new = self._create_rearranged_sectors(
                n_sectors, rearrange_center, self.radius, scale=1.0
            )
            count_label = VGroup(
                MathTex(f"n = {n_sectors}", font_size=28, color=WHITE),
                Text(" 等分", font=FONT, font_size=22, color=GRAY_A)
            ).arrange(RIGHT, buff=0.08).move_to(DOWN * 4.5)

            self.play(
                Transform(self.sectors, rearranged_new),
                FadeIn(count_label),
                run_time=1.5
            )
            self.wait(0.8)
            if n_sectors < 24:
                self.play(FadeOut(count_label), run_time=0.3)

        # Final note about limit
        limit_note = Text(
            "当 n 趋向无穷大...", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 5.5)
        limit_note2 = Text(
            "就变成了长方形！", font=FONT, font_size=28, color=COLOR_RECT, weight=BOLD
        ).move_to(DOWN * 6.3)
        self.play(FadeIn(limit_note, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(limit_note2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # Clean up
        self.play(
            FadeOut(VGroup(
                self.title_cut, step4, count_label,
                limit_note, limit_note2, self.sectors
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 推导面积公式
    # ------------------------------------------------------------------

    def scene_6_derive_formula(self):
        """从近似长方形推导圆面积公式"""

        title = Text(
            "推导面积公式", font=FONT, font_size=36, color=WHITE
        ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # Draw the approximate rectangle explicitly
        rect_center = np.array([0.0, 2.5, 0.0])
        rect_half_w = self.rect_length / 2  # pi*r / 2
        rect_half_h = self.rect_width / 2   # r / 2

        # Scale to fit screen: pi*1.8 ~ 5.65, too wide for 9-width frame
        display_scale = 0.65
        rw = rect_half_w * display_scale
        rh = rect_half_h * display_scale

        rect_bl = rect_center + np.array([-rw, -rh, 0])
        rect_br = rect_center + np.array([rw, -rh, 0])
        rect_tr = rect_center + np.array([rw, rh, 0])
        rect_tl = rect_center + np.array([-rw, rh, 0])

        rect = Polygon(
            rect_bl, rect_br, rect_tr, rect_tl,
            color=COLOR_RECT, fill_color=COLOR_RECT,
            fill_opacity=0.35, stroke_width=3
        )

        self.play(FadeIn(rect), run_time=0.8)

        # Label: length = pi*r (top)
        length_brace = Brace(rect, DOWN, buff=0.15, color=COLOR_CIRCUM)
        length_label = VGroup(
            Text("长 = ", font=FONT, font_size=22, color=COLOR_CIRCUM),
            MathTex(r"\pi r", font_size=30, color=COLOR_CIRCUM)
        ).arrange(RIGHT, buff=0.05)
        length_label.next_to(length_brace, DOWN, buff=0.1)

        self.play(FadeIn(length_brace), FadeIn(length_label), run_time=0.6)

        # Label: width = r (right side)
        width_brace = Brace(rect, RIGHT, buff=0.15, color=COLOR_RADIUS)
        width_label = VGroup(
            Text("宽 = ", font=FONT, font_size=22, color=COLOR_RADIUS),
            MathTex(r"r", font_size=30, color=COLOR_RADIUS)
        ).arrange(RIGHT, buff=0.05)
        width_label.next_to(width_brace, RIGHT, buff=0.1)

        self.play(FadeIn(width_brace), FadeIn(width_label), run_time=0.6)
        self.wait(0.5)

        # Explain the relationship
        explain_origin = Text(
            "长来自半周长，宽来自半径",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(explain_origin, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # Step-by-step derivation
        eq1_lhs = Text("长方形面积", font=FONT, font_size=24, color=COLOR_RECT)
        eq1_eq = Text(" = ", font=FONT, font_size=24, color=WHITE)
        eq1_rhs = VGroup(
            Text("长", font=FONT, font_size=24, color=COLOR_CIRCUM),
            MathTex(r"\times", font_size=28, color=WHITE),
            Text("宽", font=FONT, font_size=24, color=COLOR_RADIUS),
        ).arrange(RIGHT, buff=0.08)
        eq1 = VGroup(eq1_lhs, eq1_eq, eq1_rhs).arrange(RIGHT, buff=0.08)
        eq1.move_to(DOWN * 2.5)

        self.play(FadeIn(eq1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # Substitution
        eq2 = VGroup(
            Text(" = ", font=FONT, font_size=26, color=WHITE),
            MathTex(r"\pi r", font_size=34, color=COLOR_CIRCUM),
            MathTex(r"\times", font_size=28, color=WHITE),
            MathTex(r"r", font_size=34, color=COLOR_RADIUS),
        ).arrange(RIGHT, buff=0.1)
        eq2.move_to(DOWN * 3.5)

        self.play(FadeIn(eq2, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # Result
        eq3 = VGroup(
            Text(" = ", font=FONT, font_size=26, color=WHITE),
            MathTex(r"\pi r^2", font_size=40, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1)
        eq3.move_to(DOWN * 4.5)

        self.play(FadeIn(eq3, shift=UP * 0.2), run_time=0.6)

        # Key conclusion
        conclude = VGroup(
            Text("圆的面积", font=FONT, font_size=28, color=COLOR_CIRCLE),
            Text(" = ", font=FONT, font_size=28, color=WHITE),
            Text("长方形面积", font=FONT, font_size=28, color=COLOR_RECT),
        ).arrange(RIGHT, buff=0.08).move_to(DOWN * 5.8)

        self.play(FadeIn(conclude, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        # Clean up
        self.play(
            FadeOut(VGroup(
                title, rect, length_brace, length_label,
                width_brace, width_label, explain_origin,
                eq1, eq2, eq3, conclude
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 公式总结
    # ------------------------------------------------------------------

    def scene_7_formula_summary(self):
        """大字公式总结 + 关键要点"""

        # Redraw circle with labels
        circle = self._create_circle(fill_opacity=0.3)
        center_dot = Dot(self.circle_center, color=WHITE, radius=0.06)

        radius_end = self.circle_center + RIGHT * self.radius
        radius_line = Line(
            self.circle_center, radius_end,
            color=COLOR_RADIUS, stroke_width=4
        )
        r_label = MathTex("r", font_size=32, color=COLOR_RADIUS).next_to(
            radius_line, DOWN, buff=0.15
        )

        self.play(
            FadeIn(circle), FadeIn(center_dot),
            Create(radius_line), FadeIn(r_label),
            run_time=0.8
        )
        self.wait(0.3)

        # Formula box
        formula_box = RoundedRectangle(
            width=7.8, height=3.2,
            corner_radius=0.3,
            fill_color=COLOR_FORMULA_BG, fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 4.5)

        formula_title = Text(
            "圆的面积公式", font=FONT, font_size=26, color=GRAY_A
        ).move_to(DOWN * 3.2)

        # Main formula: S = pi * r^2
        formula_lhs = Text("S = ", font=FONT, font_size=48, color=WHITE)
        formula_rhs = MathTex(
            r"\pi r^2", font_size=60, color=COLOR_HL
        )
        formula_main = VGroup(formula_lhs, formula_rhs).arrange(RIGHT, buff=0.15)
        formula_main.move_to(DOWN * 4.3)

        # Chinese explanation below formula
        formula_explain = VGroup(
            Text("圆面积 = ", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"\pi", font_size=30, color=COLOR_CIRCUM),
            MathTex(r"\times", font_size=24, color=GRAY_A),
            Text(" 半径", font=FONT, font_size=24, color=COLOR_RADIUS),
            MathTex(r"\times", font_size=24, color=GRAY_A),
            Text(" 半径", font=FONT, font_size=24, color=COLOR_RADIUS),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 5.5)

        self.play(FadeIn(formula_box), run_time=0.3)
        self.play(Write(formula_title), run_time=0.4)
        self.play(Write(formula_main), run_time=1.0)

        # Highlight box around formula
        hl_box = SurroundingRectangle(
            formula_rhs, color=COLOR_SECTOR_A, stroke_width=2.5,
            buff=0.15, corner_radius=0.1
        )
        self.play(Create(hl_box), run_time=0.4)
        self.play(FadeIn(formula_explain, shift=UP * 0.2), run_time=0.5)

        # Key reminder
        reminder = Text(
            "r  是半径，别忘了要平方哦！",
            font=FONT, font_size=22, color=COLOR_HL
        ).move_to(DOWN * 6.5)
        self.play(FadeIn(reminder, shift=UP * 0.2), run_time=0.5)
        self.wait(2.5)

        # Clean up
        self.play(
            FadeOut(VGroup(
                circle, center_dot, radius_line, r_label,
                formula_box, formula_title, formula_main,
                hl_box, formula_explain, reminder
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        """作者信息 + 关注提示"""

        # Author big
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=30, color=GRAY_A
        ).move_to(UP * 1.0)

        self.play(Transform(self.author_mob, author_big), run_time=0.6)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # Follow prompt
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # Decorative: small circles
        colors = [COLOR_CIRCLE, COLOR_SECTOR_A, COLOR_SECTOR_B,
                  COLOR_RECT, COLOR_CIRCUM, COLOR_RADIUS]
        mini_circles = VGroup(*[
            Circle(
                radius=0.25, fill_color=c, fill_opacity=0.9,
                stroke_color=c, stroke_width=1
            ).move_to(
                DOWN * 2.8 + np.array([
                    np.cos(i * PI / 3) * 2.2,
                    np.sin(i * PI / 3) * 0.7,
                    0.0
                ])
            )
            for i, c in enumerate(colors)
        ])
        self.play(*[FadeIn(s, scale=0.3) for s in mini_circles], run_time=0.5)
        self.play(Rotate(mini_circles, angle=2 * PI / 3, run_time=1.2, rate_func=smooth))
        self.wait(0.8)

        # Fade out all
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini_circles)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 003_圆的面积.py CircleAreaLesson
#   中等质量:  manim -qm  003_圆的面积.py CircleAreaLesson
#   高质量:    manim -qh  003_圆的面积.py CircleAreaLesson
# ======================================================================
