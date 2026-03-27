"""
001_扇形统计图.py -- 扇形统计图 教学动画

知识点: 认识扇形统计图, 了解其特点, 计算百分比与圆心角, 从图中提取信息
年级: 六年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 圆代表整体, 扇形代表部分
  2. 百分比 -> 圆心角 = 360 x 百分比
  3. 各扇形圆心角之和 = 360
  4. 实例: 小明一天时间分配扇形统计图
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
COLOR_SLEEP = "#3b82f6"       # 蓝色 - 睡觉
COLOR_STUDY = "#22c55e"       # 绿色 - 学习
COLOR_PLAY = "#f59e0b"        # 橙色 - 活动
COLOR_EAT = "#ef4444"         # 红色 - 吃饭
COLOR_OTHER = "#8b5cf6"       # 紫色 - 其他
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_AUTHOR = "#6b7280"
COLOR_FORMULA = "#a78bfa"     # 浅紫色公式
FONT = "Noto Sans CJK SC"

# ======================================================================
# 数据: 小明一天时间分配
# ======================================================================
DATA_LABELS = ["睡觉", "学习", "活动", "吃饭", "其他"]
DATA_HOURS = [10, 6, 4, 2, 2]
DATA_TOTAL = sum(DATA_HOURS)                # 24
DATA_PCTS = [h / DATA_TOTAL for h in DATA_HOURS]
DATA_ANGLES_DEG = [p * 360 for p in DATA_PCTS]     # degrees
DATA_ANGLES_RAD = [p * TAU for p in DATA_PCTS]      # radians
DATA_COLORS = [COLOR_SLEEP, COLOR_STUDY, COLOR_PLAY, COLOR_EAT, COLOR_OTHER]


class PieChartLesson(Scene):
    """
    扇形统计图教学动画

    场景:
      1. 开场钩子
      2. 圆 = 整体, 扇形 = 部分
      3. 百分比与圆心角计算
      4. 动手绘制扇形统计图
      5. 从图中提取信息
      6. 总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_whole_and_part()
        self.scene_3_percent_to_angle()
        self.scene_4_build_pie_chart()
        self.scene_5_read_chart()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text(
            "一个圆, 就能讲清楚", font=FONT, font_size=36, color=WHITE
        ).move_to(UP * 5.0)
        hook2 = Text(
            "一天24小时怎么花的?", font=FONT, font_size=42, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.8)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)

        # 一个圆 + 问号
        circle_preview = Circle(
            radius=1.8, color=WHITE, stroke_width=3
        ).move_to(UP * 0.5)
        q_mark = MathTex(r"?", font_size=120, color=COLOR_HL).move_to(circle_preview.get_center())

        self.play(Create(circle_preview), run_time=0.8)
        self.play(FadeIn(q_mark, scale=0.5), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, circle_preview, q_mark)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 圆 = 整体, 扇形 = 部分
    # ------------------------------------------------------------------
    def scene_2_whole_and_part(self):
        title = Text(
            "扇形统计图的原理", font=FONT, font_size=36,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 完整圆 = 整体
        full_circle = Circle(
            radius=2.0, color=WHITE, stroke_width=3,
            fill_color=COLOR_SLEEP, fill_opacity=0.2
        ).move_to(UP * 1.5)

        lbl_whole = Text(
            "圆 = 整体 (100%)", font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 1.5)

        self.play(Create(full_circle), run_time=0.8)
        self.play(FadeIn(lbl_whole), run_time=0.5)
        self.wait(0.6)

        # 分成两部分
        angle_a = 120 * DEGREES
        sector_a = AnnularSector(
            inner_radius=0, outer_radius=2.0,
            angle=angle_a, start_angle=90 * DEGREES,
            color=COLOR_STUDY, fill_opacity=0.6, stroke_width=2
        ).move_to(UP * 1.5)

        sector_b = AnnularSector(
            inner_radius=0, outer_radius=2.0,
            angle=TAU - angle_a, start_angle=90 * DEGREES + angle_a,
            color=COLOR_PLAY, fill_opacity=0.6, stroke_width=2
        ).move_to(UP * 1.5)

        self.play(
            FadeOut(lbl_whole),
            FadeOut(full_circle),
            FadeIn(sector_a),
            FadeIn(sector_b),
            run_time=0.8
        )

        desc_a = Text("部分 A", font=FONT, font_size=22, color=COLOR_STUDY)
        desc_b = Text("部分 B", font=FONT, font_size=22, color=COLOR_PLAY)
        desc_a.move_to(UP * 2.5 + LEFT * 1.2)
        desc_b.move_to(UP * 0.5 + RIGHT * 1.2)
        self.play(FadeIn(desc_a), FadeIn(desc_b), run_time=0.4)

        key_point = Text(
            "扇形面积越大 = 占比越高",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(key_point, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(VGroup(title, sector_a, sector_b, desc_a, desc_b, key_point)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 3: 百分比 -> 圆心角
    # ------------------------------------------------------------------
    def scene_3_percent_to_angle(self):
        title = Text(
            "百分比与圆心角", font=FONT, font_size=36,
            color=COLOR_FORMULA, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 公式: 圆心角 = 360 x 百分比
        f_lbl = Text("圆心角 ", font=FONT, font_size=28, color=WHITE)
        f_eq = MathTex(r"= 360^\circ \times", font_size=36, color=WHITE)
        f_pct = Text(" 百分比", font=FONT, font_size=28, color=COLOR_HL)
        formula = VGroup(f_lbl, f_eq, f_pct).arrange(RIGHT, buff=0.1).move_to(UP * 3.5)

        self.play(Write(formula), run_time=0.8)
        self.wait(0.5)

        # 用"睡觉"做例子
        example_title = Text(
            "例: 小明一天睡觉10小时", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 2.2)
        self.play(Write(example_title), run_time=0.5)

        # 步骤1: 算百分比
        step1_lbl = Text("百分比 = ", font=FONT, font_size=24, color=WHITE)
        step1_frac = MathTex(r"\frac{10}{24}", font_size=36, color=COLOR_SLEEP)
        step1_approx = MathTex(r"\approx 41.7\%", font_size=36, color=COLOR_SLEEP)
        step1 = VGroup(step1_lbl, step1_frac, step1_approx).arrange(RIGHT, buff=0.15).move_to(UP * 0.8)

        self.play(Write(step1), run_time=0.8)
        self.wait(0.5)

        # 步骤2: 算圆心角
        step2_lbl = Text("圆心角 = ", font=FONT, font_size=24, color=WHITE)
        step2_calc = MathTex(r"360^\circ \times \frac{10}{24}", font_size=36, color=COLOR_SLEEP)
        step2_eq = MathTex(r"= 150^\circ", font_size=36, color=COLOR_HL)
        step2 = VGroup(step2_lbl, step2_calc, step2_eq).arrange(RIGHT, buff=0.15).move_to(DOWN * 0.5)

        self.play(Write(VGroup(step2_lbl, step2_calc)), run_time=0.8)
        self.wait(0.3)
        self.play(Write(step2_eq), run_time=0.5)

        # 强调结果
        self.play(Indicate(step2_eq, scale_factor=1.15, color=COLOR_HL), run_time=0.6)

        # 公式2: 各角之和 = 360
        sum_lbl = Text("所有圆心角之和", font=FONT, font_size=24, color=WHITE)
        sum_eq = MathTex(r"= 360^\circ", font_size=36, color=COLOR_HL)
        sum_formula = VGroup(sum_lbl, sum_eq).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.5)

        self.play(FadeIn(sum_formula, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(title, formula, example_title, step1, step2, sum_formula)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 动手绘制扇形统计图
    # ------------------------------------------------------------------
    def scene_4_build_pie_chart(self):
        title = Text(
            "绘制扇形统计图", font=FONT, font_size=36,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        subtitle = Text(
            "小明一天 24 小时时间分配", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 4.8)
        self.play(FadeIn(title, shift=DOWN * 0.3), FadeIn(subtitle), run_time=0.5)

        # 先展示数据表
        table_items = []
        for i, (label, hours) in enumerate(zip(DATA_LABELS, DATA_HOURS)):
            pct_str = f"{DATA_PCTS[i]*100:.1f}%"
            angle_str = f"{DATA_ANGLES_DEG[i]:.0f}"
            row_color = Dot(radius=0.12, color=DATA_COLORS[i])
            row_lbl = Text(label, font=FONT, font_size=20, color=WHITE)
            row_hrs = Text(f"{hours}h", font=FONT, font_size=20, color=GRAY_A)
            row_pct = Text(pct_str, font=FONT, font_size=20, color=GRAY_A)
            row_ang_val = MathTex(angle_str + r"^\circ", font_size=22, color=GRAY_A)
            row = VGroup(row_color, row_lbl, row_hrs, row_pct, row_ang_val).arrange(RIGHT, buff=0.35)
            table_items.append(row)

        table = VGroup(*table_items).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(UP * 2.5)

        for row in table:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.35)
        self.wait(0.6)

        # 移动表格到上方, 开始画饼图
        self.play(table.animate.scale(0.8).move_to(UP * 4.0), run_time=0.5)

        # 逐块绘制扇形
        pie_center = DOWN * 0.5
        pie_radius = 2.2
        sectors = []
        sector_labels = []
        current_angle = 90 * DEGREES    # 从12点位置开始

        for i in range(len(DATA_LABELS)):
            sector = AnnularSector(
                inner_radius=0,
                outer_radius=pie_radius,
                angle=DATA_ANGLES_RAD[i],
                start_angle=current_angle,
                color=DATA_COLORS[i],
                fill_opacity=0.75,
                stroke_color=WHITE,
                stroke_width=2
            ).shift(pie_center)

            # 标签位置: 扇形中心方向
            mid_angle = current_angle + DATA_ANGLES_RAD[i] / 2
            label_r = pie_radius * 0.6
            label_pos = pie_center + label_r * np.array([np.cos(mid_angle), np.sin(mid_angle), 0])

            pct_str = f"{DATA_PCTS[i]*100:.1f}%"
            lbl = Text(pct_str, font=FONT, font_size=20, color=WHITE, weight=BOLD)
            lbl.move_to(label_pos)

            sectors.append(sector)
            sector_labels.append(lbl)
            current_angle += DATA_ANGLES_RAD[i]

        # 一块一块地绘制
        for i, (sec, lbl) in enumerate(zip(sectors, sector_labels)):
            self.play(FadeIn(sec, shift=UP * 0.1), run_time=0.5)
            self.play(FadeIn(lbl), run_time=0.3)
            self.wait(0.15)

        # 外部类别标签
        outer_labels = []
        current_angle = 90 * DEGREES
        for i in range(len(DATA_LABELS)):
            mid_angle = current_angle + DATA_ANGLES_RAD[i] / 2
            outer_r = pie_radius + 0.5
            outer_pos = pie_center + outer_r * np.array([np.cos(mid_angle), np.sin(mid_angle), 0])

            cat_lbl = Text(DATA_LABELS[i], font=FONT, font_size=18, color=DATA_COLORS[i])
            cat_lbl.move_to(outer_pos)
            outer_labels.append(cat_lbl)
            current_angle += DATA_ANGLES_RAD[i]

        self.play(*[FadeIn(ol) for ol in outer_labels], run_time=0.5)
        self.wait(1.5)

        # 保存引用用于后续场景
        self.pie_sectors = VGroup(*sectors)
        self.pie_labels = VGroup(*sector_labels)
        self.pie_outer = VGroup(*outer_labels)
        self.pie_table = table

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            run_time=0.3
        )

    # ------------------------------------------------------------------
    # Scene 5: 从图中提取信息
    # ------------------------------------------------------------------
    def scene_5_read_chart(self):
        title = Text(
            "读懂扇形统计图", font=FONT, font_size=36,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 高亮"睡觉"扇形
        q1 = Text(
            "哪项活动占时最多?", font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 4.0)
        self.play(Write(q1), run_time=0.5)

        # 高亮最大扇形 (睡觉 index=0)
        self.play(
            self.pie_sectors[0].animate.set_fill(opacity=1.0),
            self.pie_sectors[0].animate.set_stroke(color=COLOR_HL, width=4),
            run_time=0.6
        )

        a1 = Text(
            "睡觉 -- 占 41.7%, 接近一半!", font=FONT, font_size=22, color=COLOR_SLEEP
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(a1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # 恢复
        self.play(
            self.pie_sectors[0].animate.set_fill(opacity=0.75),
            self.pie_sectors[0].animate.set_stroke(color=WHITE, width=2),
            FadeOut(q1), FadeOut(a1),
            run_time=0.4
        )

        # 问题2: 学习 + 活动
        q2 = Text(
            "学习和活动共占多少?", font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 4.0)
        self.play(Write(q2), run_time=0.5)

        self.play(
            self.pie_sectors[1].animate.set_fill(opacity=1.0),
            self.pie_sectors[2].animate.set_fill(opacity=1.0),
            run_time=0.5
        )

        calc_lbl = Text("25% + 16.7% = ", font=FONT, font_size=22, color=WHITE)
        calc_val = Text("41.7%", font=FONT, font_size=22, color=COLOR_HL, weight=BOLD)
        calc = VGroup(calc_lbl, calc_val).arrange(RIGHT, buff=0.1).move_to(DOWN * 5.0)
        self.play(FadeIn(calc), run_time=0.5)
        self.wait(0.8)

        # 恢复
        self.play(
            self.pie_sectors[1].animate.set_fill(opacity=0.75),
            self.pie_sectors[2].animate.set_fill(opacity=0.75),
            FadeOut(q2), FadeOut(calc),
            run_time=0.4
        )

        # 问题3: 验证总和
        q3 = Text(
            "所有百分比之和?", font=FONT, font_size=26, color=WHITE
        ).move_to(DOWN * 4.0)
        self.play(Write(q3), run_time=0.5)

        sum_line = MathTex(
            r"41.7\% + 25\% + 16.7\% + 8.3\% + 8.3\%",
            font_size=26, color=GRAY_A
        ).move_to(DOWN * 5.0)
        sum_eq = MathTex(r"= 100\%", font_size=30, color=COLOR_HL).move_to(DOWN * 5.8)

        self.play(Write(sum_line), run_time=0.8)
        self.play(Write(sum_eq), run_time=0.4)

        self.play(Indicate(sum_eq, scale_factor=1.15, color=COLOR_HL), run_time=0.5)
        self.wait(1.0)

        # 清理所有饼图相关元素
        self.play(
            FadeOut(title), FadeOut(q3), FadeOut(sum_line), FadeOut(sum_eq),
            FadeOut(self.pie_sectors), FadeOut(self.pie_labels),
            FadeOut(self.pie_outer), FadeOut(self.pie_table),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 总结
    # ------------------------------------------------------------------
    def scene_6_summary(self):
        box = RoundedRectangle(
            width=8.0, height=7.0,
            corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)

        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "扇形统计图要点", font=FONT,
            font_size=32, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.5)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            VGroup(
                Text("1.", font=FONT, font_size=22, color=COLOR_HL),
                Text(" 圆 = 整体(100%)", font=FONT, font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("2.", font=FONT, font_size=22, color=COLOR_HL),
                Text(" 扇形 = 各部分占比", font=FONT, font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("3.", font=FONT, font_size=22, color=COLOR_HL),
                Text(" 圆心角 = ", font=FONT, font_size=22, color=WHITE),
                MathTex(r"360^\circ \times", font_size=26, color=WHITE),
                Text("百分比", font=FONT, font_size=22, color=COLOR_HL),
            ).arrange(RIGHT, buff=0.08),
            VGroup(
                Text("4.", font=FONT, font_size=22, color=COLOR_HL),
                Text(" 所有百分比之和 = 100%", font=FONT, font_size=22, color=WHITE),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("5.", font=FONT, font_size=22, color=COLOR_HL),
                Text(" 所有圆心角之和 = ", font=FONT, font_size=22, color=WHITE),
                MathTex(r"360^\circ", font_size=26, color=COLOR_HL),
            ).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, buff=0.55, aligned_edge=LEFT).move_to(UP * 0.5)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.45)
            self.wait(0.25)

        tip = Text(
            "直观展示部分与整体的关系!",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(FadeOut(VGroup(box, sum_title, items, tip)), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------
    def scene_7_outro(self):
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

        follow = Text(
            "关注我, 获得更多数学技巧!",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 小饼图装饰
        mini_pie = VGroup()
        mini_center = DOWN * 3.0
        mini_r = 0.8
        cur = 90 * DEGREES
        for i in range(len(DATA_LABELS)):
            sec = AnnularSector(
                inner_radius=0, outer_radius=mini_r,
                angle=DATA_ANGLES_RAD[i], start_angle=cur,
                color=DATA_COLORS[i], fill_opacity=0.8,
                stroke_color=WHITE, stroke_width=1
            ).shift(mini_center)
            mini_pie.add(sec)
            cur += DATA_ANGLES_RAD[i]

        self.play(FadeIn(mini_pie, scale=0.5), run_time=0.6)
        self.play(Rotate(mini_pie, angle=TAU, run_time=2.0, rate_func=smooth))
        self.wait(0.5)

        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, mini_pie)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 001_扇形统计图.py PieChartLesson
#   中等质量:  manim -qm  001_扇形统计图.py PieChartLesson
#   高质量:    manim -qh  001_扇形统计图.py PieChartLesson
# ======================================================================
