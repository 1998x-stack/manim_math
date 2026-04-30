"""
减法的初步认识 - 一年级上册数学动画
Subtraction Introduction - Grade 1 Math Animation

内容: 从5个苹果中拿走2个，还剩几个 → 引入减法公式
目标: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== TikTok 竖屏配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


FONT = "PingFang SC"

# ===== 颜色配置 =====
COLOR_BG        = "#1a1a2e"
COLOR_APPLE     = "#e74c3c"    # 苹果红
COLOR_APPLE_2   = "#c0392b"    # 深红（要被拿走的）
COLOR_GONE      = "#444455"    # 已拿走变灰
COLOR_MINUS     = "#f39c12"    # 减号橙色高亮
COLOR_RESULT    = "#2ecc71"    # 结果绿色
COLOR_BRACE     = "#3498db"    # 括号蓝
COLOR_LABEL     = "#f0e68c"    # 术语标注
COLOR_AUTHOR    = "#7f8c8d"

# ===== 布局常量 =====
AUTHOR_Y    = 7.0
TITLE_Y     = 5.5
APPLE_Y     = 2.8
EXPLAIN_Y   = 0.8
FORMULA_Y   = -0.8
BRACE_Y     = -2.2
GENERAL_Y   = -4.2
OUTRO_Y     = 0.0


class SubtractionIntro(Scene):
    """减法初步认识 - 一年级教学动画"""

    def construct(self):
        self.camera.background_color = COLOR_BG

        # 预计算苹果位置
        self.setup_layout()

        # 执行场景
        self.scene_0_opening()
        self.scene_1_show_apples()
        self.scene_2_take_away()
        self.scene_3_count_rest()
        self.scene_4_formula()
        self.scene_5_terms()
        self.scene_6_outro()

    # ─────────────────────────────
    def setup_layout(self):
        """预计算所有布局坐标"""
        # 5个苹果水平排列，圆心间距 1.0
        self.APPLE_R = 0.38
        self.APPLE_SPACING = 1.05
        self.apple_xs = [-2 * self.APPLE_SPACING + i * self.APPLE_SPACING for i in range(5)]
        # → [-2.1, -1.05, 0, 1.05, 2.1]
        self.apple_positions = [
            np.array([x, APPLE_Y, 0]) for x in self.apple_xs
        ]

    # ─────────────────────────────
    def make_apple(self, pos, color=None, label_num=None):
        """创建一个苹果圆形（带可选数字）"""
        c = color or COLOR_APPLE
        circle = Circle(
            radius=self.APPLE_R,
            fill_color=c,
            fill_opacity=0.95,
            stroke_color=WHITE,
            stroke_width=2,
        ).move_to(pos)

        group = VGroup(circle)

        if label_num is not None:
            num = Text(str(label_num), font=FONT, font_size=26, color=WHITE)
            num.move_to(pos)
            group.add(num)

        return group

    def make_apple_emoji(self, pos):
        """创建苹果图案（叶子+圆）"""
        body = Circle(
            radius=self.APPLE_R,
            fill_color=COLOR_APPLE,
            fill_opacity=0.95,
            stroke_color=WHITE,
            stroke_width=2,
        ).move_to(pos)
        # 小叶子用绿色小圆
        leaf = Circle(
            radius=0.10,
            fill_color="#27ae60",
            fill_opacity=1.0,
            stroke_width=0,
        ).move_to(pos + UP * (self.APPLE_R * 0.85) + RIGHT * 0.08)
        stem = Line(
            pos + UP * self.APPLE_R,
            pos + UP * (self.APPLE_R + 0.18),
            stroke_color="#8B4513",
            stroke_width=2,
        )
        return VGroup(body, leaf, stem)

    # ─────────────────────────────
    def scene_0_opening(self):
        """场景0：开场 + 钩子"""

        # 作者信息
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=20, color=COLOR_AUTHOR
        ).move_to(UP * AUTHOR_Y)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 主标题
        title = Text("减法的初步认识", font=FONT, font_size=44, color=GOLD)
        title.move_to(UP * TITLE_Y)
        self.play(Write(title), run_time=0.9)

        # 副标题
        subtitle = Text("从总数里去掉一部分", font=FONT, font_size=26, color=GRAY_A)
        subtitle.move_to(UP * 4.6)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)

        # 情境问题
        question = Text("树上有5个苹果🍎", font=FONT, font_size=30, color=WHITE)
        question.move_to(UP * 3.7)
        self.play(Write(question), run_time=0.7)

        self.wait(0.5)

        # 5个苹果逐个落下（带弹跳感）
        self.apples = VGroup()
        for i, pos in enumerate(self.apple_positions):
            apple = self.make_apple_emoji(pos)
            start_pos = pos + UP * 3
            apple.move_to(start_pos)
            self.add(apple)
            self.play(
                apple.animate.move_to(pos).set_rate_func(there_and_back_with_pause),
                run_time=0.28,
            )
            # 落下后轻微弹跳
            apple.move_to(pos)
            self.apples.add(apple)

        self.wait(0.6)

        # 清理标题
        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(question),
            run_time=0.5
        )

    # ─────────────────────────────
    def scene_1_show_apples(self):
        """场景1：展示5个苹果，标注总数"""

        # 大数字"5"在苹果下方
        total_label = Text("一共", font=FONT, font_size=28, color=GRAY_A)
        total_num = Text("5", font=FONT, font_size=56, color=YELLOW)
        total_unit = Text("个苹果", font=FONT, font_size=28, color=GRAY_A)
        total_row = VGroup(total_label, total_num, total_unit).arrange(RIGHT, buff=0.15)
        total_row.move_to(UP * EXPLAIN_Y)

        # 大括号标注 5 个苹果
        brace = Brace(self.apples, DOWN, color=COLOR_BRACE, buff=0.15)
        brace_label = Text("5个", font=FONT, font_size=24, color=COLOR_BRACE)
        brace.put_at_tip(brace_label, buff=0.1)

        self.play(GrowFromCenter(brace), FadeIn(brace_label), run_time=0.7)
        self.play(FadeIn(total_row, shift=UP * 0.3), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(brace), FadeOut(brace_label), FadeOut(total_row),
            run_time=0.4
        )

    # ─────────────────────────────
    def scene_2_take_away(self):
        """场景2：拿走2个苹果"""

        explain = Text("小鸟叼走了", font=FONT, font_size=30, color=WHITE)
        num_gone = Text("2", font=FONT, font_size=56, color=COLOR_MINUS)
        explain2 = Text("个", font=FONT, font_size=30, color=WHITE)
        row = VGroup(explain, num_gone, explain2).arrange(RIGHT, buff=0.1)
        row.move_to(UP * EXPLAIN_Y)

        self.play(Write(row), run_time=0.7)
        self.wait(0.3)

        # 前2个苹果变暗 + 划叉
        to_remove = [self.apples[0], self.apples[1]]
        crosses = VGroup()

        for apple in to_remove:
            # 变灰
            self.play(
                apple[0].animate.set_fill(COLOR_GONE, opacity=0.6).set_stroke(GRAY),
                run_time=0.3,
            )
            # 划叉
            pos = apple.get_center()
            r = self.APPLE_R * 0.9
            cross = VGroup(
                Line(pos + UL * r, pos + DR * r, color=RED, stroke_width=5),
                Line(pos + UR * r, pos + DL * r, color=RED, stroke_width=5),
            )
            self.play(Create(cross), run_time=0.35)
            crosses.add(cross)

        self.wait(0.5)

        # 拿走的苹果飞走
        for i, (apple, cross) in enumerate(zip(to_remove, crosses)):
            fly_dir = LEFT * 1.5 + UP * 2.5 if i == 0 else RIGHT * 0.5 + UP * 3.0
            self.play(
                apple.animate.shift(fly_dir).set_opacity(0),
                cross.animate.shift(fly_dir).set_opacity(0),
                run_time=0.45,
            )
            self.remove(apple, cross)

        self.wait(0.5)

        # 保存说明行，稍后清理
        self.play(FadeOut(row), run_time=0.3)

    # ─────────────────────────────
    def scene_3_count_rest(self):
        """场景3：数剩余3个苹果"""

        # 剩余3个苹果向中间靠拢
        remaining = self.apples[2:]  # 索引2,3,4
        new_positions = [
            np.array([-1.0 * self.APPLE_SPACING, APPLE_Y, 0]),
            np.array([0.0, APPLE_Y, 0]),
            np.array([1.0 * self.APPLE_SPACING, APPLE_Y, 0]),
        ]

        animations = []
        for apple, new_pos in zip(remaining, new_positions):
            animations.append(apple.animate.move_to(new_pos))
        self.play(*animations, run_time=0.6)

        # 高亮闪烁
        for apple in remaining:
            self.play(
                apple[0].animate.set_stroke(YELLOW, width=4),
                run_time=0.2
            )

        # 标注剩余
        brace2 = Brace(VGroup(*remaining), DOWN, color=COLOR_RESULT, buff=0.15)
        brace_label2 = Text("还剩3个", font=FONT, font_size=26, color=COLOR_RESULT)
        brace2.put_at_tip(brace_label2, buff=0.1)

        self.play(GrowFromCenter(brace2), FadeIn(brace_label2), run_time=0.7)

        # 大数字3
        result_big = Text("3", font=FONT, font_size=72, color=COLOR_RESULT)
        result_big.move_to(UP * EXPLAIN_Y)
        self.play(GrowFromCenter(result_big), run_time=0.6)
        self.play(Flash(result_big, color=COLOR_RESULT, flash_radius=0.6), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(brace2), FadeOut(brace_label2), FadeOut(result_big),
            *[apple[0].animate.set_stroke(WHITE, width=2) for apple in remaining],
            run_time=0.4
        )

        # 把剩余苹果移上去，给公式腾出空间
        self.remaining_apples = VGroup(*remaining)
        self.play(
            self.remaining_apples.animate.move_to(UP * 4.5).scale(0.7),
            run_time=0.5
        )

    # ─────────────────────────────
    def scene_4_formula(self):
        """场景4：逐步构建减法算式 5 - 2 = 3"""

        # 引导文字
        intro = Text("我们用算式来表示：", font=FONT, font_size=26, color=GRAY_A)
        intro.move_to(UP * 3.2)
        self.play(FadeIn(intro, shift=RIGHT * 0.3), run_time=0.5)

        # 公式逐步显示（各部分分别动画）
        num5 = MathTex("5", font_size=80, color=WHITE).move_to(UP * FORMULA_Y + LEFT * 2.4)
        minus = MathTex("-", font_size=80, color=COLOR_MINUS).move_to(UP * FORMULA_Y + LEFT * 0.8)
        num2 = MathTex("2", font_size=80, color=COLOR_MINUS).move_to(UP * FORMULA_Y + RIGHT * 0.6)
        eq = MathTex("=", font_size=80, color=WHITE).move_to(UP * FORMULA_Y + RIGHT * 2.0)
        num3 = MathTex("3", font_size=80, color=COLOR_RESULT).move_to(UP * FORMULA_Y + RIGHT * 3.4)

        self.play(GrowFromCenter(num5), run_time=0.5)
        self.wait(0.2)

        # 减号高亮
        self.play(GrowFromCenter(minus), run_time=0.4)
        self.play(Flash(minus, color=COLOR_MINUS, flash_radius=0.4), run_time=0.3)

        # 减号说明
        minus_label = Text("减号", font=FONT, font_size=24, color=COLOR_MINUS)
        minus_label.next_to(minus, DOWN, buff=0.4)
        minus_read = Text('读作"减"', font=FONT, font_size=22, color=GRAY_A)
        minus_read.next_to(minus_label, DOWN, buff=0.15)
        self.play(FadeIn(minus_label), FadeIn(minus_read), run_time=0.5)
        self.wait(0.8)
        self.play(FadeOut(minus_label), FadeOut(minus_read), run_time=0.3)

        self.play(GrowFromCenter(num2), run_time=0.5)
        self.wait(0.2)
        self.play(GrowFromCenter(eq), run_time=0.4)
        self.wait(0.2)
        self.play(GrowFromCenter(num3), run_time=0.5)
        self.play(Flash(num3, color=COLOR_RESULT, flash_radius=0.5), run_time=0.4)

        self.wait(1.0)
        self.play(FadeOut(intro), run_time=0.3)

        # 保存公式元素供下一场景使用
        self.f_num5 = num5
        self.f_minus = minus
        self.f_num2 = num2
        self.f_eq = eq
        self.f_num3 = num3

    # ─────────────────────────────
    def scene_5_terms(self):
        """场景5：术语讲解 - 被减数、减数、差"""

        formula_group = VGroup(
            self.f_num5, self.f_minus, self.f_num2, self.f_eq, self.f_num3
        )

        # 整体上移给术语腾位置
        self.play(
            formula_group.animate.move_to(UP * 1.5).scale(0.85),
            self.remaining_apples.animate.move_to(UP * 5.8).scale(0.6),
            run_time=0.5
        )

        # 重新获取位置（缩放后）
        pos5 = self.f_num5.get_center()
        pos2 = self.f_num2.get_center()
        pos3 = self.f_num3.get_center()

        # ── 被减数 ──
        arrow_5 = Arrow(
            pos5 + UP * 0.7, pos5 + UP * 0.15,
            color=COLOR_BRACE, stroke_width=3, max_tip_length_to_length_ratio=0.35
        )
        label_5 = Text("被减数", font=FONT, font_size=26, color=COLOR_BRACE)
        label_5.next_to(arrow_5, UP, buff=0.1)

        self.play(
            GrowArrow(arrow_5),
            FadeIn(label_5, shift=DOWN * 0.2),
            run_time=0.6
        )
        self.wait(0.5)

        # ── 减数 ──
        arrow_2 = Arrow(
            pos2 + UP * 0.7, pos2 + UP * 0.15,
            color=COLOR_MINUS, stroke_width=3, max_tip_length_to_length_ratio=0.35
        )
        label_2 = Text("减数", font=FONT, font_size=26, color=COLOR_MINUS)
        label_2.next_to(arrow_2, UP, buff=0.1)

        self.play(
            GrowArrow(arrow_2),
            FadeIn(label_2, shift=DOWN * 0.2),
            run_time=0.6
        )
        self.wait(0.5)

        # ── 差 ──
        arrow_3 = Arrow(
            pos3 + UP * 0.7, pos3 + UP * 0.15,
            color=COLOR_RESULT, stroke_width=3, max_tip_length_to_length_ratio=0.35
        )
        label_3 = Text("差", font=FONT, font_size=26, color=COLOR_RESULT)
        label_3.next_to(arrow_3, UP, buff=0.1)

        self.play(
            GrowArrow(arrow_3),
            FadeIn(label_3, shift=DOWN * 0.2),
            run_time=0.6
        )
        self.wait(0.8)

        # ── 通用公式行 ──
        bg_rect = RoundedRectangle(
            width=7.8, height=1.1,
            corner_radius=0.3,
            fill_color="#16213e",
            fill_opacity=0.9,
            stroke_color=GOLD,
            stroke_width=2,
        ).move_to(UP * GENERAL_Y)

        # 用 VGroup 拼接: 被减数 - 减数 = 差
        g_bjs = Text("被减数", font=FONT, font_size=28, color=COLOR_BRACE)
        g_minus = MathTex("-", font_size=36, color=COLOR_MINUS)
        g_js = Text("减数", font=FONT, font_size=28, color=COLOR_MINUS)
        g_eq = MathTex("=", font_size=36, color=WHITE)
        g_cha = Text("差", font=FONT, font_size=28, color=COLOR_RESULT)
        gen_formula = VGroup(g_bjs, g_minus, g_js, g_eq, g_cha).arrange(RIGHT, buff=0.25)
        gen_formula.move_to(UP * GENERAL_Y)

        self.play(FadeIn(bg_rect), run_time=0.3)
        self.play(Write(gen_formula), run_time=1.0)

        # 关键停留
        self.wait(2.0)

        # 清理标注
        self.play(
            FadeOut(arrow_5), FadeOut(label_5),
            FadeOut(arrow_2), FadeOut(label_2),
            FadeOut(arrow_3), FadeOut(label_3),
            run_time=0.4
        )

        # 整个公式+通用公式淡出，过渡到片尾
        self.play(
            FadeOut(formula_group),
            FadeOut(bg_rect), FadeOut(gen_formula),
            FadeOut(self.remaining_apples),
            run_time=0.6
        )

    # ─────────────────────────────
    def scene_6_outro(self):
        """场景6：片尾关注"""

        # 核心总结
        summary_1 = Text("记住减法口诀：", font=FONT, font_size=30, color=GOLD)
        summary_2_bjs = Text("被减数", font=FONT, font_size=28, color=COLOR_BRACE)
        summary_2_m = MathTex("-", font_size=36, color=COLOR_MINUS)
        summary_2_js = Text("减数", font=FONT, font_size=28, color=COLOR_MINUS)
        summary_2_eq = MathTex("=", font_size=36, color=WHITE)
        summary_2_cha = Text("差", font=FONT, font_size=28, color=COLOR_RESULT)
        summary_2 = VGroup(
            summary_2_bjs, summary_2_m, summary_2_js, summary_2_eq, summary_2_cha
        ).arrange(RIGHT, buff=0.2)

        summary_3 = Text(
            "去掉一部分，求还剩多少",
            font=FONT, font_size=24, color=GRAY_A
        )

        summary = VGroup(summary_1, summary_2, summary_3).arrange(DOWN, buff=0.35)
        summary.move_to(UP * 2.0)

        self.play(FadeIn(summary, shift=UP * 0.4), run_time=0.8)
        self.wait(0.8)

        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE
        ).move_to(DOWN * 1.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B
        ).move_to(DOWN * 2.0)

        self.play(
            self.author.animate.move_to(DOWN * 3.0).set_opacity(0),
            FadeIn(author_big, shift=UP * 0.3),
            run_time=0.5
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        # 关注引导
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=YELLOW
        ).move_to(DOWN * 3.2)

        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰：小苹果图标闪烁
        deco_apples = VGroup(*[
            Circle(radius=0.2, fill_color=COLOR_APPLE, fill_opacity=0.9, stroke_width=0)
            .move_to(follow.get_center() + 3.5 * np.array([np.cos(i * 2 * PI / 5), np.sin(i * 2 * PI / 5), 0]))
            for i in range(5)
        ])
        self.play(*[FadeIn(a, scale=0.5) for a in deco_apples], run_time=0.5)
        self.play(Rotate(deco_apples, angle=2 * PI, run_time=1.2, about_point=follow.get_center()))
        self.wait(0.8)

        self.play(
            FadeOut(summary),
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(deco_apples),
            run_time=1.0
        )


# ─────────────────────────────
# 渲染命令:
#   快速预览:  manim -pql subtraction_intro.py SubtractionIntro
#   高质量:    manim -qh  subtraction_intro.py SubtractionIntro
# ─────────────────────────────