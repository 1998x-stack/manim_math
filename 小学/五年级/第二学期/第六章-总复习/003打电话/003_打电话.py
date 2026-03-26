"""
003_打电话.py — 打电话 教学动画

知识点: 倍增策略通知多人，树形结构，最优方案
年级: 五年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 问题: 老师要通知15个学生，每分钟打1个电话
  2. 逐个打: 15分钟(低效)
  3. 倍增策略: 接到通知的人同时打电话
  4. 树形展示: 1→2→4→8→16，4分钟搞定
  5. 规律: n人需要 ⌈log₂(n+1)⌉ 分钟
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
COLOR_TEACHER = "#ef4444"     # 红色老师
COLOR_STUDENT = "#3b82f6"     # 蓝色学生
COLOR_ACTIVE = "#22c55e"      # 绿色已通知
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_STEP = "#a78bfa"        # 紫色步骤
COLOR_SLOW = "#6b7280"        # 灰色低效
COLOR_AUTHOR = "#6b7280"
FONT = "Noto Sans CJK SC"


class PhoneCallLesson(Scene):
    """
    打电话教学动画
    场景:
      1. 开场钩子
      2. 逐个打(低效方案)
      3. 倍增策略
      4. 树形展示
      5. 规律总结
      6. 总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.scene_1_opening()
        self.scene_2_slow_method()
        self.scene_3_doubling_strategy()
        self.scene_4_tree_demo()
        self.scene_5_pattern()
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
            "打电话", font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "怎样最快通知所有人？", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 4.3)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(VGroup(hook1, hook2)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 逐个打(低效方案)
    # ------------------------------------------------------------------
    def scene_2_slow_method(self):
        title = Text(
            "方案一：逐个通知", font=FONT, font_size=36,
            color=COLOR_SLOW, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 问题描述
        problem = Text(
            "老师要通知15个学生", font=FONT, font_size=26, color=WHITE
        ).move_to(UP * 4.0)
        rule = Text(
            "每分钟只能打1个电话", font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 3.3)
        self.play(Write(problem), run_time=0.5)
        self.play(Write(rule), run_time=0.4)

        # 老师圆点
        teacher = Dot(UP * 1.5, radius=0.2, color=COLOR_TEACHER)
        teacher_label = Text("老师", font=FONT, font_size=18, color=COLOR_TEACHER).next_to(teacher, UP, buff=0.15)
        self.play(FadeIn(teacher), FadeIn(teacher_label), run_time=0.4)

        # 15个学生排一排(简化展示5个+省略号)
        students = VGroup()
        for i in range(5):
            dot = Dot(
                DOWN * 0.5 + LEFT * 3.0 + RIGHT * i * 1.5,
                radius=0.15, color=COLOR_STUDENT
            )
            students.add(dot)
        dots_text = Text("...", font=FONT, font_size=30, color=COLOR_STUDENT).move_to(DOWN * 0.5 + RIGHT * 3.0)
        self.play(FadeIn(students), FadeIn(dots_text), run_time=0.4)

        # 逐个连线
        for i in range(3):
            arrow = Arrow(
                teacher.get_center(), students[i].get_center(),
                buff=0.25, color=COLOR_SLOW, stroke_width=2, max_tip_length_to_length_ratio=0.15
            )
            minute = Text(
                f"第{i+1}分钟", font=FONT, font_size=16, color=COLOR_SLOW
            ).next_to(arrow, RIGHT, buff=0.1)
            self.play(Create(arrow), FadeIn(minute), run_time=0.3)

        # 结论
        slow_result = Text(
            "需要 15 分钟！太慢了！",
            font=FONT, font_size=28, color=COLOR_SLOW, weight=BOLD
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(slow_result, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 3: 倍增策略
    # ------------------------------------------------------------------
    def scene_3_doubling_strategy(self):
        title = Text(
            "方案二：倍增策略", font=FONT, font_size=36,
            color=COLOR_ACTIVE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        idea = Text(
            "核心：接到通知的人也同时打电话！",
            font=FONT, font_size=24, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.0)
        self.play(Write(idea), run_time=0.6)

        # 每分钟的人数变化
        minutes_data = [
            ("第0分钟", "1人知道(老师)", COLOR_TEACHER),
            ("第1分钟", "1+1 = 2人知道", COLOR_ACTIVE),
            ("第2分钟", "2+2 = 4人知道", COLOR_ACTIVE),
            ("第3分钟", "4+4 = 8人知道", COLOR_ACTIVE),
            ("第4分钟", "8+8 = 16人知道", COLOR_HL),
        ]

        rows = VGroup()
        for min_str, count_str, color in minutes_data:
            min_t = Text(min_str, font=FONT, font_size=22, color=GRAY_A)
            arrow = MathTex(r"\rightarrow", font_size=22, color=GRAY_A)
            count_t = Text(count_str, font=FONT, font_size=22, color=color)
            row = VGroup(min_t, arrow, count_t).arrange(RIGHT, buff=0.2)
            rows.add(row)

        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 1.0)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.3)

        result = Text(
            "16 > 15，只需 4 分钟！",
            font=FONT, font_size=28, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.0)
        result_box = SurroundingRectangle(result, color=COLOR_HL, buff=0.15, corner_radius=0.1)
        self.play(FadeIn(result, shift=UP * 0.2), Create(result_box), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 4: 树形展示
    # ------------------------------------------------------------------
    def scene_4_tree_demo(self):
        title = Text(
            "树形图", font=FONT, font_size=36,
            color=COLOR_STEP, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 简化树形: 老师 → 2人 → 4人 → 8人
        # Level 0: 老师
        root = Dot(UP * 3.5, radius=0.18, color=COLOR_TEACHER)
        root_label = Text("老师", font=FONT, font_size=16, color=COLOR_TEACHER).next_to(root, UP, buff=0.1)
        self.play(FadeIn(root), FadeIn(root_label), run_time=0.4)

        # Level 1: 2 nodes
        l1_positions = [UP * 2.0 + LEFT * 2.0, UP * 2.0 + RIGHT * 2.0]
        l1_dots = VGroup()
        l1_lines = VGroup()
        for pos in l1_positions:
            dot = Dot(pos, radius=0.15, color=COLOR_ACTIVE)
            line = Line(root.get_center(), pos, color=COLOR_ACTIVE, stroke_width=2)
            l1_dots.add(dot)
            l1_lines.add(line)

        min1_label = Text("第1分钟", font=FONT, font_size=16, color=COLOR_HL).move_to(UP * 2.0 + RIGHT * 3.8)
        self.play(Create(l1_lines), FadeIn(l1_dots), FadeIn(min1_label), run_time=0.5)

        # Level 2: 4 nodes
        l2_positions = [
            UP * 0.5 + LEFT * 3.0, UP * 0.5 + LEFT * 1.0,
            UP * 0.5 + RIGHT * 1.0, UP * 0.5 + RIGHT * 3.0
        ]
        l2_dots = VGroup()
        l2_lines = VGroup()
        for i, pos in enumerate(l2_positions):
            parent = l1_positions[i // 2]
            dot = Dot(pos, radius=0.15, color=COLOR_ACTIVE)
            line = Line(parent, pos, color=COLOR_ACTIVE, stroke_width=2)
            l2_dots.add(dot)
            l2_lines.add(line)

        min2_label = Text("第2分钟", font=FONT, font_size=16, color=COLOR_HL).move_to(UP * 0.5 + RIGHT * 3.8)
        self.play(Create(l2_lines), FadeIn(l2_dots), FadeIn(min2_label), run_time=0.5)

        # Level 3: 8 nodes (simplified as 8 small dots)
        l3_dots = VGroup()
        l3_lines = VGroup()
        for i in range(8):
            x = -3.5 + i * 1.0
            pos = np.array([x, -1.2, 0])
            parent = l2_positions[i // 2]
            dot = Dot(pos, radius=0.12, color=COLOR_ACTIVE)
            line = Line(parent, pos, color=COLOR_ACTIVE, stroke_width=1.5)
            l3_dots.add(dot)
            l3_lines.add(line)

        min3_label = Text("第3分钟", font=FONT, font_size=16, color=COLOR_HL).move_to(DOWN * 1.2 + RIGHT * 3.8)
        self.play(Create(l3_lines), FadeIn(l3_dots), FadeIn(min3_label), run_time=0.5)

        # 第4分钟说明
        min4_text = Text(
            "第4分钟：再翻倍 → 16人",
            font=FONT, font_size=24, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(min4_text, shift=UP * 0.2), run_time=0.5)

        # 倍增公式
        formula = VGroup(
            MathTex(r"1 \rightarrow 2 \rightarrow 4 \rightarrow 8 \rightarrow 16", font_size=34, color=COLOR_ACTIVE),
            MathTex(r"2^0, 2^1, 2^2, 2^3, 2^4", font_size=30, color=GRAY_A),
        ).arrange(DOWN, buff=0.2).move_to(DOWN * 4.5)
        self.play(FadeIn(formula, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 5: 规律总结
    # ------------------------------------------------------------------
    def scene_5_pattern(self):
        title = Text(
            "规律", font=FONT, font_size=38,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 表格数据
        header_min = Text("分钟数", font=FONT, font_size=22, color=COLOR_HL)
        header_total = Text("已知道的人数", font=FONT, font_size=22, color=COLOR_HL)
        header = VGroup(header_min, header_total).arrange(RIGHT, buff=2.0).move_to(UP * 3.8)
        sep = Line(LEFT * 4, RIGHT * 4, color=GRAY, stroke_width=1).move_to(UP * 3.3)
        self.play(FadeIn(header), Create(sep), run_time=0.4)

        data = [
            ("1", "2"),
            ("2", "4"),
            ("3", "8"),
            ("4", "16"),
            ("n", "2^n"),
        ]

        rows = VGroup()
        for i, (minutes, total) in enumerate(data):
            if minutes == "n":
                min_t = MathTex(r"n", font_size=28, color=COLOR_STEP)
                total_t = MathTex(r"2^n", font_size=28, color=COLOR_ACTIVE)
            else:
                min_t = Text(minutes, font=FONT, font_size=24, color=WHITE)
                total_t = Text(total, font=FONT, font_size=24, color=COLOR_ACTIVE)
            row = VGroup(min_t, total_t).arrange(RIGHT, buff=3.0).move_to(UP * (2.5 - i * 0.8))
            rows.add(row)
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.3)

        # 结论公式
        conclusion = VGroup(
            Text("要通知 n 个人：", font=FONT, font_size=24, color=WHITE),
            Text("找最小的 t 使得", font=FONT, font_size=22, color=GRAY_A),
            MathTex(r"2^t \geq n + 1", font_size=36, color=COLOR_HL),
        ).arrange(DOWN, buff=0.3).move_to(DOWN * 2.5)
        self.play(FadeIn(conclusion, shift=UP * 0.2), run_time=0.6)

        example = Text(
            "15人：2的4次方=16 > 15+1=16，需4分钟",
            font=FONT, font_size=20, color=COLOR_HL
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(example), run_time=0.4)
        self.wait(2.0)

        self.play(FadeOut(self.mobjects_without_author()), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 6: 总结
    # ------------------------------------------------------------------
    def scene_6_summary(self):
        box = RoundedRectangle(
            width=8.0, height=7.0, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.3)
        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "打电话问题", font=FONT,
            font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 3.2)
        self.play(Write(sum_title), run_time=0.5)

        items = VGroup(
            Text("1. 逐个打太慢：需要n分钟", font=FONT, font_size=22, color=COLOR_SLOW),
            Text("2. 倍增策略：已知的人同时打电话", font=FONT, font_size=22, color=COLOR_ACTIVE),
            Text("3. 每分钟人数翻倍：1→2→4→8→16", font=FONT, font_size=22, color=WHITE),
            Text("4. 15人只需4分钟！", font=FONT, font_size=22, color=COLOR_HL),
            Text("5. 关键：让所有人都行动起来", font=FONT, font_size=22, color=COLOR_STEP),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 0.3)

        for item in items:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        tip = Text(
            "团队协作，效率翻倍！",
            font=FONT, font_size=24, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 3.0)
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
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_HL
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)
        self.wait(1.5)
        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow)),
            run_time=0.8
        )

    # ------------------------------------------------------------------
    # Helper
    # ------------------------------------------------------------------
    def mobjects_without_author(self):
        return VGroup(*[m for m in self.mobjects if m is not self.author_mob and isinstance(m, VMobject)])


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 003_打电话.py PhoneCallLesson
#   高质量:    manim -qh  003_打电话.py PhoneCallLesson
#   4K:        manim -qk  003_打电话.py PhoneCallLesson
# ======================================================================
