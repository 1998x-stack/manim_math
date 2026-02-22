"""
一元一次不等式组 - Manim 教学动画
六年级 第二学期 第六章

内容: 一元一次不等式组的概念与口诀
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
  manim -pql inequality_system.py InequalitySystem   # 快速预览
  manim -qh inequality_system.py InequalitySystem    # 高质量
"""

from manim import *
import numpy as np


# ============================================================
# 全局配置 - TikTok 竖屏
# ============================================================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ============================================================
# 颜色配置
# ============================================================
BG_COLOR = "#1a1a2e"
COLOR_INEQ1 = "#e74c3c"      # 红色 - 不等式1 (x > a)
COLOR_INEQ2 = "#3498db"      # 蓝色 - 不等式2 (x < b)
COLOR_SOLUTION = "#2ecc71"   # 绿色 - 解集区域
COLOR_HIGHLIGHT = YELLOW
COLOR_CARD_BG = "#16213e"
COLOR_ACCENT = "#f39c12"     # 橙色 - 强调
FONT = "Noto Sans CJK SC"


def make_number_line(x_range=(-2, 8), unit=0.5, y_pos=0, color=WHITE):
    """
    创建数轴
    x_range: (min, max) 数值范围
    unit: 每单位对应的逻辑长度
    y_pos: 数轴的y坐标
    """
    x_min, x_max = x_range
    line_left = x_min * unit
    line_right = x_max * unit

    # 主轴线
    axis = Arrow(
        start=np.array([line_left - 0.2, y_pos, 0]),
        end=np.array([line_right + 0.3, y_pos, 0]),
        color=color,
        stroke_width=2.5,
        max_tip_length_to_length_ratio=0.08,
        buff=0
    )

    # 刻度和标签
    ticks = VGroup()
    labels = VGroup()

    for i in range(x_min, x_max + 1):
        x_logical = i * unit
        tick = Line(
            start=np.array([x_logical, y_pos - 0.1, 0]),
            end=np.array([x_logical, y_pos + 0.1, 0]),
            color=color,
            stroke_width=1.5
        )
        ticks.add(tick)

        # 只标注整数（-2到8但只标几个关键点）
        if i % 2 == 0 or i in (-1, 1, 3, 5, 7):
            label = MathTex(str(i), color=color, font_size=18)
            label.move_to(np.array([x_logical, y_pos - 0.35, 0]))
            labels.add(label)

    return VGroup(axis, ticks, labels)


def make_solution_ray_right(start_val, unit=0.5, y_pos=0, open_end=True, color=COLOR_INEQ1, extend=3.5):
    """
    创建向右射线（x > a 或 x >= a 的解集）
    open_end=True: 空心点（不含端点）
    """
    x_start = start_val * unit

    ray = Arrow(
        start=np.array([x_start, y_pos, 0]),
        end=np.array([x_start + extend, y_pos, 0]),
        color=color,
        stroke_width=5,
        max_tip_length_to_length_ratio=0.12,
        buff=0
    )

    if open_end:
        dot = Circle(radius=0.1, color=color, stroke_width=3)
        dot.move_to(np.array([x_start, y_pos, 0]))
        dot.set_fill(BG_COLOR, opacity=1)
    else:
        dot = Dot(np.array([x_start, y_pos, 0]), color=color, radius=0.1)

    return VGroup(ray, dot)


def make_solution_ray_left(end_val, unit=0.5, y_pos=0, open_end=True, color=COLOR_INEQ2, extend=3.5):
    """
    创建向左射线（x < a 或 x <= a 的解集）
    """
    x_end = end_val * unit

    ray = Arrow(
        start=np.array([x_end, y_pos, 0]),
        end=np.array([x_end - extend, y_pos, 0]),
        color=color,
        stroke_width=5,
        max_tip_length_to_length_ratio=0.12,
        buff=0
    )

    if open_end:
        dot = Circle(radius=0.1, color=color, stroke_width=3)
        dot.move_to(np.array([x_end, y_pos, 0]))
        dot.set_fill(BG_COLOR, opacity=1)
    else:
        dot = Dot(np.array([x_end, y_pos, 0]), color=color, radius=0.1)

    return VGroup(ray, dot)


def make_solution_segment(a_val, b_val, unit=0.5, y_pos=0, color=COLOR_SOLUTION):
    """
    创建有界解集线段 a < x < b
    """
    x_a = a_val * unit
    x_b = b_val * unit

    segment = Line(
        start=np.array([x_a, y_pos, 0]),
        end=np.array([x_b, y_pos, 0]),
        color=color,
        stroke_width=8
    )

    dot_a = Circle(radius=0.1, color=color, stroke_width=3)
    dot_a.move_to(np.array([x_a, y_pos, 0]))
    dot_a.set_fill(BG_COLOR, opacity=1)

    dot_b = Circle(radius=0.1, color=color, stroke_width=3)
    dot_b.move_to(np.array([x_b, y_pos, 0]))
    dot_b.set_fill(BG_COLOR, opacity=1)

    return VGroup(segment, dot_a, dot_b)


class InequalitySystem(Scene):
    """
    一元一次不等式组教学动画

    场景顺序:
    1. 开场钩子
    2. 概念定义
    3. 数轴可视化
    4. 口诀四法 (核心)
    5. 例题演示
    6. 片尾关注
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 数轴单位长度（每数值单位对应的逻辑坐标长度）
        self.UNIT = 0.5

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_definition()
        self.scene_3_number_line_visual()
        self.scene_4_four_rules()
        self.scene_5_example()
        self.scene_6_outro()

    # ============================================================
    # Scene 1: 开场钩子
    # ============================================================
    def scene_1_opening(self):
        # 作者信息（顶部常驻）
        self.author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT,
            font_size=18,
            color=GRAY_B
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # 标题
        title = Text(
            "一元一次不等式组",
            font=FONT,
            font_size=44,
            color=WHITE,
            weight=BOLD
        ).move_to(UP * 5.5)

        subtitle = Text(
            "四句口诀轻松解题！",
            font=FONT,
            font_size=30,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)

        # 不等式组示例
        brace_group = self.make_system_display(
            r"x > 1",
            r"x < 4",
            pos=UP * 2.5,
            color1=COLOR_INEQ1,
            color2=COLOR_INEQ2
        )

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(brace_group, shift=UP * 0.5, scale=0.9), run_time=0.8)

        # 问号：这个怎么解？
        question = Text(
            "这个不等式组怎么解？",
            font=FONT,
            font_size=28,
            color=COLOR_ACCENT
        ).move_to(UP * 0.5)

        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(brace_group),
            FadeOut(question),
            run_time=0.5
        )

    # ============================================================
    # Scene 2: 概念定义
    # ============================================================
    def scene_2_definition(self):
        # 章节标题
        sec_title = Text(
            "什么是一元一次不等式组？",
            font=FONT,
            font_size=32,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 5.5)

        self.play(Write(sec_title), run_time=0.7)

        # 定义卡片背景
        card = RoundedRectangle(
            width=7.5, height=3.0,
            corner_radius=0.3,
            fill_color=COLOR_CARD_BG,
            fill_opacity=1,
            stroke_color=COLOR_INEQ1,
            stroke_width=2
        ).move_to(UP * 3.5)

        def_text = Text(
            "由几个含有同一未知数的\n一元一次不等式组成的不等式组",
            font=FONT,
            font_size=24,
            color=WHITE
        ).move_to(UP * 3.5)

        self.play(FadeIn(card), Write(def_text), run_time=1.0)

        # 示例：展示不等式组
        example_title = Text(
            "例如：",
            font=FONT,
            font_size=26,
            color=GRAY_A
        ).move_to(UP * 1.8)

        system = self.make_system_display(
            r"x > 2",
            r"x < 5",
            pos=UP * 0.7,
            color1=COLOR_INEQ1,
            color2=COLOR_INEQ2,
            scale=1.3
        )

        self.play(FadeIn(example_title), run_time=0.4)
        self.play(FadeIn(system, shift=UP * 0.3), run_time=0.7)

        # 解集说明
        sol_label = Text(
            "解集 = 各不等式解集的",
            font=FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 0.8)

        sol_highlight = Text(
            "公共部分（交集）",
            font=FONT,
            font_size=28,
            color=COLOR_SOLUTION,
            weight=BOLD
        ).move_to(DOWN * 1.6)

        self.play(FadeIn(sol_label), run_time=0.5)
        self.play(FadeIn(sol_highlight, scale=1.1), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(sec_title),
            FadeOut(card),
            FadeOut(def_text),
            FadeOut(example_title),
            FadeOut(system),
            FadeOut(sol_label),
            FadeOut(sol_highlight),
            run_time=0.5
        )

    # ============================================================
    # Scene 3: 数轴可视化
    # ============================================================
    def scene_3_number_line_visual(self):
        sec_title = Text(
            "用数轴表示解集",
            font=FONT,
            font_size=34,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 6.0)

        self.play(Write(sec_title), run_time=0.6)

        # 不等式组展示
        system = self.make_system_display(
            r"x > 2",
            r"x < 5",
            pos=UP * 4.8,
            color1=COLOR_INEQ1,
            color2=COLOR_INEQ2,
            scale=1.1
        )
        self.play(FadeIn(system), run_time=0.5)

        # ---- 数轴1：x > 2 ----
        label1 = Text(
            "不等式①  x > 2  的解集：",
            font=FONT,
            font_size=22,
            color=COLOR_INEQ1
        ).move_to(UP * 3.3)

        # 数轴（仅显示0-7范围，单位0.5）
        nl1 = make_number_line(x_range=(0, 7), unit=self.UNIT, y_pos=0, color=GRAY_A)
        nl1.move_to(UP * 2.5)

        self.play(FadeIn(label1), run_time=0.4)
        self.play(Create(nl1), run_time=0.7)

        # x > 2 的射线（从2向右）
        # 在数轴坐标系中：x=2 对应逻辑坐标 (2*0.5 - 3.5, 0) = (-2.5, 0)???
        # 需要计算数轴中心偏移
        # nl1 居中在0，所以数轴的数值0 对应逻辑坐标0（因为我们move_to了UP*2.5）
        # 数值i 对应的x逻辑坐标 = (i - 3.5) * 0.5  （居中在3.5处）
        # 实际上：数轴从0到7，中心在3.5，所以：
        # x_logical_in_nl = (val - 3.5) * self.UNIT
        # 但我们需要在nl1的移动后的坐标系中计算

        # 简单方法：数值0在数轴最左，每单位0.5
        # nl1总宽度 = 7 * 0.5 = 3.5，左端偏移 = -3.5/2 = -1.75
        # 所以数值 v 对应的x坐标 = v * 0.5 - 1.75 (相对于中心)
        # 绝对位置: y=2.5（已经move_to）

        def val_to_x(val, nl_center_x=0.0, x_min=0, unit=0.5):
            """将数值转换为数轴上的逻辑x坐标"""
            # x_min的逻辑坐标 = nl_center_x - (x_max - x_min)/2 * unit
            # = nl_center_x - (7-0)/2 * 0.5 = nl_center_x - 1.75
            x_min_logical = nl_center_x - (7 - 0) / 2 * unit
            return x_min_logical + (val - x_min) * unit

        y1 = 2.5  # 数轴1的y坐标
        x2 = val_to_x(2)  # x=2对应的逻辑x坐标

        ray1 = Arrow(
            start=np.array([x2, y1, 0]),
            end=np.array([x2 + 2.0, y1, 0]),
            color=COLOR_INEQ1,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.12,
            buff=0
        )
        dot1 = Circle(radius=0.1, color=COLOR_INEQ1, stroke_width=3)
        dot1.move_to(np.array([x2, y1, 0]))
        dot1.set_fill(BG_COLOR, opacity=1)

        self.play(Create(dot1), run_time=0.3)
        self.play(Create(ray1), run_time=0.6)

        # ---- 数轴2：x < 5 ----
        label2 = Text(
            "不等式②  x < 5  的解集：",
            font=FONT,
            font_size=22,
            color=COLOR_INEQ2
        ).move_to(UP * 0.8)

        nl2 = make_number_line(x_range=(0, 7), unit=self.UNIT, y_pos=0, color=GRAY_A)
        nl2.move_to(UP * 0.0)

        self.play(FadeIn(label2), run_time=0.4)
        self.play(Create(nl2), run_time=0.7)

        y2 = 0.0
        x5 = val_to_x(5)  # x=5对应的逻辑x坐标

        ray2 = Arrow(
            start=np.array([x5, y2, 0]),
            end=np.array([x5 - 2.5, y2, 0]),
            color=COLOR_INEQ2,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.12,
            buff=0
        )
        dot2 = Circle(radius=0.1, color=COLOR_INEQ2, stroke_width=3)
        dot2.move_to(np.array([x5, y2, 0]))
        dot2.set_fill(BG_COLOR, opacity=1)

        self.play(Create(dot2), run_time=0.3)
        self.play(Create(ray2), run_time=0.6)
        self.wait(0.5)

        # ---- 数轴3：公共部分（解集） ----
        label3 = Text(
            "两者的公共部分（解集）：",
            font=FONT,
            font_size=22,
            color=COLOR_SOLUTION
        ).move_to(DOWN * 1.7)

        nl3 = make_number_line(x_range=(0, 7), unit=self.UNIT, y_pos=0, color=GRAY_A)
        nl3.move_to(DOWN * 2.5)

        self.play(FadeIn(label3), run_time=0.4)
        self.play(Create(nl3), run_time=0.6)

        y3 = -2.5
        x2_on3 = val_to_x(2)
        x5_on3 = val_to_x(5)

        # 解集区间线段
        seg = Line(
            start=np.array([x2_on3, y3, 0]),
            end=np.array([x5_on3, y3, 0]),
            color=COLOR_SOLUTION,
            stroke_width=8
        )
        seg_dot_a = Circle(radius=0.1, color=COLOR_SOLUTION, stroke_width=3)
        seg_dot_a.move_to(np.array([x2_on3, y3, 0]))
        seg_dot_a.set_fill(BG_COLOR, opacity=1)
        seg_dot_b = Circle(radius=0.1, color=COLOR_SOLUTION, stroke_width=3)
        seg_dot_b.move_to(np.array([x5_on3, y3, 0]))
        seg_dot_b.set_fill(BG_COLOR, opacity=1)

        self.play(Create(seg_dot_a), Create(seg_dot_b), run_time=0.4)
        self.play(Create(seg), run_time=0.8)

        # 解集公式
        sol_formula = MathTex(
            r"2 < x < 5",
            color=COLOR_SOLUTION,
            font_size=40
        ).move_to(DOWN * 4.0)

        self.play(Write(sol_formula), run_time=0.7)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(sec_title),
            FadeOut(system),
            FadeOut(label1), FadeOut(nl1), FadeOut(ray1), FadeOut(dot1),
            FadeOut(label2), FadeOut(nl2), FadeOut(ray2), FadeOut(dot2),
            FadeOut(label3), FadeOut(nl3), FadeOut(seg), FadeOut(seg_dot_a), FadeOut(seg_dot_b),
            FadeOut(sol_formula),
            run_time=0.6
        )

    # ============================================================
    # Scene 4: 口诀四法（核心）
    # ============================================================
    def scene_4_four_rules(self):
        sec_title = Text(
            "四句口诀速记法",
            font=FONT,
            font_size=36,
            color=COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)

        self.play(Write(sec_title), run_time=0.6)

        # ---- 口诀1: 同大取大 ----
        self.show_rule_1()

        # ---- 口诀2: 同小取小 ----
        self.show_rule_2()

        # ---- 口诀3: 大小小大中间找 ----
        self.show_rule_3()

        # ---- 口诀4: 大大小小找不到 ----
        self.show_rule_4()

        # 清理标题
        self.play(FadeOut(sec_title), run_time=0.3)

    def show_rule_1(self):
        """口诀1：同大取大 - x > a 且 x > b (a < b) => x > b"""
        # 口诀标题
        rule_title = self.make_rule_card("① 同大取大", COLOR_INEQ1)
        rule_title.move_to(UP * 5.3)

        ineq_display = self.make_system_display(
            r"x > 1",
            r"x > 3",
            pos=UP * 3.8,
            color1=COLOR_INEQ1,
            color2=COLOR_INEQ1,
            scale=1.0
        )

        self.play(FadeIn(rule_title), FadeIn(ineq_display), run_time=0.5)

        # 两条数轴
        nl1, nl2 = self._make_two_number_lines()

        self.play(Create(nl1), Create(nl2), run_time=0.6)

        # 数轴上画解集
        y1, y2 = 2.2, 0.5
        x1_pos = self._val_to_x(1)
        x3_pos = self._val_to_x(3)

        ray1 = self._make_right_arrow(x1_pos, y1, COLOR_INEQ1)
        ray2 = self._make_right_arrow(x3_pos, y2, COLOR_INEQ1)

        self.play(Create(ray1), run_time=0.5)
        self.play(Create(ray2), run_time=0.5)

        # 解集：取更大的（x > 3）
        result_line = make_number_line(x_range=(0, 7), unit=self.UNIT, y_pos=0, color=GRAY_A)
        result_line.move_to(DOWN * 1.2)
        self.play(Create(result_line), run_time=0.4)

        y3 = -1.2
        x3_on3 = self._val_to_x(3)
        ray3 = self._make_right_arrow(x3_on3, y3, COLOR_SOLUTION, stroke_width=8)
        self.play(Create(ray3), run_time=0.6)

        result_formula = MathTex(r"x > 3", color=COLOR_SOLUTION, font_size=38)
        result_formula.move_to(DOWN * 2.5)
        self.play(Write(result_formula), run_time=0.5)

        explain = Text(
            "取较大的那个！",
            font=FONT,
            font_size=26,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(explain, scale=1.1), run_time=0.4)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(rule_title), FadeOut(ineq_display),
            FadeOut(nl1), FadeOut(nl2),
            FadeOut(ray1), FadeOut(ray2),
            FadeOut(result_line), FadeOut(ray3),
            FadeOut(result_formula), FadeOut(explain),
            run_time=0.4
        )

    def show_rule_2(self):
        """口诀2：同小取小 - x < a 且 x < b (a < b) => x < a"""
        rule_title = self.make_rule_card("② 同小取小", COLOR_INEQ2)
        rule_title.move_to(UP * 5.3)

        ineq_display = self.make_system_display(
            r"x < 6",
            r"x < 4",
            pos=UP * 3.8,
            color1=COLOR_INEQ2,
            color2=COLOR_INEQ2,
            scale=1.0
        )

        self.play(FadeIn(rule_title), FadeIn(ineq_display), run_time=0.5)

        nl1, nl2 = self._make_two_number_lines()
        self.play(Create(nl1), Create(nl2), run_time=0.6)

        y1, y2 = 2.2, 0.5
        x6_pos = self._val_to_x(6)
        x4_pos = self._val_to_x(4)

        ray1 = self._make_left_arrow(x6_pos, y1, COLOR_INEQ2)
        ray2 = self._make_left_arrow(x4_pos, y2, COLOR_INEQ2)

        self.play(Create(ray1), run_time=0.5)
        self.play(Create(ray2), run_time=0.5)

        # 解集：取更小的（x < 4）
        result_line = make_number_line(x_range=(0, 7), unit=self.UNIT, y_pos=0, color=GRAY_A)
        result_line.move_to(DOWN * 1.2)
        self.play(Create(result_line), run_time=0.4)

        y3 = -1.2
        x4_on3 = self._val_to_x(4)
        ray3 = self._make_left_arrow(x4_on3, y3, COLOR_SOLUTION, stroke_width=8)
        self.play(Create(ray3), run_time=0.6)

        result_formula = MathTex(r"x < 4", color=COLOR_SOLUTION, font_size=38)
        result_formula.move_to(DOWN * 2.5)
        self.play(Write(result_formula), run_time=0.5)

        explain = Text(
            "取较小的那个！",
            font=FONT,
            font_size=26,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(explain, scale=1.1), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(rule_title), FadeOut(ineq_display),
            FadeOut(nl1), FadeOut(nl2),
            FadeOut(ray1), FadeOut(ray2),
            FadeOut(result_line), FadeOut(ray3),
            FadeOut(result_formula), FadeOut(explain),
            run_time=0.4
        )

    def show_rule_3(self):
        """口诀3：大小小大中间找 - x > a 且 x < b (a < b) => a < x < b"""
        rule_title = self.make_rule_card("③ 大小小大中间找", COLOR_SOLUTION)
        rule_title.move_to(UP * 5.3)

        ineq_display = self.make_system_display(
            r"x > 2",
            r"x < 5",
            pos=UP * 3.8,
            color1=COLOR_INEQ1,
            color2=COLOR_INEQ2,
            scale=1.0
        )

        self.play(FadeIn(rule_title), FadeIn(ineq_display), run_time=0.5)

        nl1, nl2 = self._make_two_number_lines()
        self.play(Create(nl1), Create(nl2), run_time=0.6)

        y1, y2 = 2.2, 0.5
        x2_pos = self._val_to_x(2)
        x5_pos = self._val_to_x(5)

        ray1 = self._make_right_arrow(x2_pos, y1, COLOR_INEQ1)
        ray2 = self._make_left_arrow(x5_pos, y2, COLOR_INEQ2)

        self.play(Create(ray1), run_time=0.5)
        self.play(Create(ray2), run_time=0.5)

        # 解集：中间部分 2 < x < 5
        result_line = make_number_line(x_range=(0, 7), unit=self.UNIT, y_pos=0, color=GRAY_A)
        result_line.move_to(DOWN * 1.2)
        self.play(Create(result_line), run_time=0.4)

        y3 = -1.2
        x2_on3 = self._val_to_x(2)
        x5_on3 = self._val_to_x(5)

        seg = Line(
            start=np.array([x2_on3, y3, 0]),
            end=np.array([x5_on3, y3, 0]),
            color=COLOR_SOLUTION,
            stroke_width=8
        )
        sdot_a = Circle(radius=0.1, color=COLOR_SOLUTION, stroke_width=3)
        sdot_a.move_to(np.array([x2_on3, y3, 0]))
        sdot_a.set_fill(BG_COLOR, opacity=1)
        sdot_b = Circle(radius=0.1, color=COLOR_SOLUTION, stroke_width=3)
        sdot_b.move_to(np.array([x5_on3, y3, 0]))
        sdot_b.set_fill(BG_COLOR, opacity=1)

        self.play(Create(sdot_a), Create(sdot_b), run_time=0.3)
        self.play(Create(seg), run_time=0.7)

        result_formula = MathTex(r"2 < x < 5", color=COLOR_SOLUTION, font_size=38)
        result_formula.move_to(DOWN * 2.5)
        self.play(Write(result_formula), run_time=0.5)

        explain = Text(
            "中间那段！（注意a < b时才有解）",
            font=FONT,
            font_size=22,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)
        self.play(FadeIn(explain, scale=1.1), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(rule_title), FadeOut(ineq_display),
            FadeOut(nl1), FadeOut(nl2),
            FadeOut(ray1), FadeOut(ray2),
            FadeOut(result_line), FadeOut(seg), FadeOut(sdot_a), FadeOut(sdot_b),
            FadeOut(result_formula), FadeOut(explain),
            run_time=0.4
        )

    def show_rule_4(self):
        """口诀4：大大小小找不到 - x > b 且 x < a (b > a) => 无解"""
        rule_title = self.make_rule_card("④ 大大小小找不到", "#e74c3c")
        rule_title.move_to(UP * 5.3)

        ineq_display = self.make_system_display(
            r"x > 5",
            r"x < 2",
            pos=UP * 3.8,
            color1=COLOR_INEQ1,
            color2=COLOR_INEQ2,
            scale=1.0
        )

        self.play(FadeIn(rule_title), FadeIn(ineq_display), run_time=0.5)

        nl1, nl2 = self._make_two_number_lines()
        self.play(Create(nl1), Create(nl2), run_time=0.6)

        y1, y2 = 2.2, 0.5
        x5_pos = self._val_to_x(5)
        x2_pos = self._val_to_x(2)

        ray1 = self._make_right_arrow(x5_pos, y1, COLOR_INEQ1)
        ray2 = self._make_left_arrow(x2_pos, y2, COLOR_INEQ2)

        self.play(Create(ray1), run_time=0.5)
        self.play(Create(ray2), run_time=0.5)

        # 无解！显示X
        no_solution = Text(
            "❌ 无解！",
            font=FONT,
            font_size=48,
            color="#e74c3c"
        ).move_to(DOWN * 1.2)

        explain = Text(
            "两个射线方向相反且不重叠",
            font=FONT,
            font_size=24,
            color=GRAY_A
        ).move_to(DOWN * 2.4)

        explain2 = Text(
            "没有公共部分 → 无解",
            font=FONT,
            font_size=26,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.4)

        self.play(FadeIn(no_solution, scale=1.3), run_time=0.6)
        self.play(FadeIn(explain), FadeIn(explain2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(rule_title), FadeOut(ineq_display),
            FadeOut(nl1), FadeOut(nl2),
            FadeOut(ray1), FadeOut(ray2),
            FadeOut(no_solution), FadeOut(explain), FadeOut(explain2),
            run_time=0.4
        )

    # ============================================================
    # Scene 5: 口诀总结 + 例题
    # ============================================================
    def scene_5_example(self):
        # 口诀汇总卡片
        summary_title = Text(
            "四句口诀总结",
            font=FONT,
            font_size=34,
            color=COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)

        self.play(Write(summary_title), run_time=0.5)

        # 四个口诀
        rules = [
            ("同大取大", "x>a与x>b → x>max(a,b)", COLOR_INEQ1),
            ("同小取小", "x<a与x<b → x<min(a,b)", COLOR_INEQ2),
            ("大小小大中间找", "x>a与x<b(a<b) → a<x<b", COLOR_SOLUTION),
            ("大大小小找不到", "x>b与x<a(b>a) → 无解", "#e74c3c"),
        ]

        rule_cards = VGroup()
        for i, (rule, desc, color) in enumerate(rules):
            card = self._make_summary_card(rule, desc, color)
            card.move_to(np.array([0, 4.5 - i * 2.2, 0]))
            rule_cards.add(card)

        for card in rule_cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.35)

        self.wait(2.0)

        # 清理口诀，展示例题
        self.play(
            FadeOut(summary_title),
            FadeOut(rule_cards),
            run_time=0.5
        )

        # 例题
        ex_title = Text(
            "例题",
            font=FONT,
            font_size=36,
            color=COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 6.5)

        self.play(Write(ex_title), run_time=0.4)

        # 题目
        problem_card = RoundedRectangle(
            width=7.5, height=2.5,
            corner_radius=0.3,
            fill_color=COLOR_CARD_BG,
            fill_opacity=1,
            stroke_color=COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(UP * 4.8)

        problem_text = Text(
            "解不等式组：",
            font=FONT,
            font_size=26,
            color=WHITE
        ).move_to(UP * 5.3)

        problem_sys = self.make_system_display(
            r"x > 1",
            r"x < 4",
            pos=UP * 4.3,
            color1=COLOR_INEQ1,
            color2=COLOR_INEQ2,
            scale=1.1
        )

        self.play(FadeIn(problem_card), Write(problem_text), FadeIn(problem_sys), run_time=0.8)

        # 解题步骤
        step1_text = Text(
            "Step 1：分别在数轴上表示各解集",
            font=FONT,
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 2.8)
        self.play(FadeIn(step1_text), run_time=0.4)

        # 数轴演示
        nl_ex = make_number_line(x_range=(0, 6), unit=0.65, y_pos=0, color=GRAY_A)
        nl_ex.move_to(UP * 2.0)
        self.play(Create(nl_ex), run_time=0.5)

        # 计算数值到x坐标的映射（0到6范围，单位0.65，数轴居中）
        def val_to_x_ex(val):
            center_x = 0.0
            x_min, x_max = 0, 6
            x_min_logical = center_x - (x_max - x_min) / 2 * 0.65
            return x_min_logical + (val - x_min) * 0.65

        y_ex = 2.0
        x1_ex = val_to_x_ex(1)
        x4_ex = val_to_x_ex(4)

        # x > 1 的射线
        ray_ex1 = Arrow(
            start=np.array([x1_ex, y_ex + 0.25, 0]),
            end=np.array([x1_ex + 1.8, y_ex + 0.25, 0]),
            color=COLOR_INEQ1,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.12,
            buff=0
        )
        dot_ex1 = Circle(radius=0.09, color=COLOR_INEQ1, stroke_width=3)
        dot_ex1.move_to(np.array([x1_ex, y_ex + 0.25, 0]))
        dot_ex1.set_fill(BG_COLOR, opacity=1)

        # x < 4 的射线
        ray_ex2 = Arrow(
            start=np.array([x4_ex, y_ex - 0.25, 0]),
            end=np.array([x4_ex - 2.2, y_ex - 0.25, 0]),
            color=COLOR_INEQ2,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.12,
            buff=0
        )
        dot_ex2 = Circle(radius=0.09, color=COLOR_INEQ2, stroke_width=3)
        dot_ex2.move_to(np.array([x4_ex, y_ex - 0.25, 0]))
        dot_ex2.set_fill(BG_COLOR, opacity=1)

        self.play(Create(dot_ex1), Create(ray_ex1), run_time=0.5)
        self.play(Create(dot_ex2), Create(ray_ex2), run_time=0.5)

        step2_text = Text(
            "Step 2：找公共部分（大小小大中间找）",
            font=FONT,
            font_size=22,
            color=GRAY_A
        ).move_to(UP * 0.8)
        self.play(FadeIn(step2_text), run_time=0.4)

        # 解集线段
        seg_ex = Line(
            start=np.array([x1_ex, y_ex, 0]),
            end=np.array([x4_ex, y_ex, 0]),
            color=COLOR_SOLUTION,
            stroke_width=10
        )
        sdot_a_ex = Circle(radius=0.1, color=COLOR_SOLUTION, stroke_width=3)
        sdot_a_ex.move_to(np.array([x1_ex, y_ex, 0]))
        sdot_a_ex.set_fill(BG_COLOR, opacity=1)
        sdot_b_ex = Circle(radius=0.1, color=COLOR_SOLUTION, stroke_width=3)
        sdot_b_ex.move_to(np.array([x4_ex, y_ex, 0]))
        sdot_b_ex.set_fill(BG_COLOR, opacity=1)

        self.play(Create(sdot_a_ex), Create(sdot_b_ex), run_time=0.3)
        self.play(Create(seg_ex), run_time=0.7)

        # 最终答案
        answer_box = RoundedRectangle(
            width=6, height=1.5,
            corner_radius=0.3,
            fill_color=COLOR_SOLUTION,
            fill_opacity=0.2,
            stroke_color=COLOR_SOLUTION,
            stroke_width=3
        ).move_to(DOWN * 1.0)

        answer_label = Text("解集：", font=FONT, font_size=30, color=COLOR_SOLUTION)
        answer_formula = MathTex(r"1 < x < 4", color=COLOR_SOLUTION, font_size=36)
        answer = VGroup(answer_label, answer_formula).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.0)

        self.play(FadeIn(answer_box), Write(answer), run_time=0.8)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(ex_title),
            FadeOut(problem_card), FadeOut(problem_text), FadeOut(problem_sys),
            FadeOut(step1_text), FadeOut(nl_ex),
            FadeOut(ray_ex1), FadeOut(dot_ex1),
            FadeOut(ray_ex2), FadeOut(dot_ex2),
            FadeOut(step2_text),
            FadeOut(seg_ex), FadeOut(sdot_a_ex), FadeOut(sdot_b_ex),
            FadeOut(answer_box), FadeOut(answer),
            run_time=0.5
        )

    # ============================================================
    # Scene 6: 片尾
    # ============================================================
    def scene_6_outro(self):
        # 口诀最终展示
        motto_bg = RoundedRectangle(
            width=7.5, height=4.0,
            corner_radius=0.4,
            fill_color=COLOR_CARD_BG,
            fill_opacity=1,
            stroke_color=COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(UP * 3.0)

        motto_title = Text(
            "牢记口诀",
            font=FONT,
            font_size=30,
            color=COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 4.3)

        mottos = VGroup(
            Text("同大取大", font=FONT, font_size=26, color=COLOR_INEQ1),
            Text("同小取小", font=FONT, font_size=26, color=COLOR_INEQ2),
            Text("大小小大中间找", font=FONT, font_size=26, color=COLOR_SOLUTION),
            Text("大大小小找不到", font=FONT, font_size=26, color="#e74c3c"),
        ).arrange(DOWN, buff=0.35).move_to(UP * 2.8)

        self.play(FadeIn(motto_bg), Write(motto_title), run_time=0.5)
        for m in mottos:
            self.play(FadeIn(m, shift=RIGHT * 0.3), run_time=0.3)

        self.wait(1.0)

        # 作者信息放大居中
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT,
            font_size=36,
            color=WHITE,
            weight=BOLD
        ).move_to(DOWN * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT,
            font_size=28,
            color=GRAY_B
        ).move_to(DOWN * 2.4)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font=FONT,
            font_size=28,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)

        self.play(
            FadeIn(author_big, shift=UP * 0.3),
            FadeIn(author_id, shift=UP * 0.3),
            run_time=0.6
        )
        self.play(
            FadeIn(follow_text, scale=1.1),
            run_time=0.5
        )
        self.wait(2.0)

        # 淡出
        self.play(
            FadeOut(motto_bg), FadeOut(motto_title), FadeOut(mottos),
            FadeOut(author_big), FadeOut(author_id), FadeOut(follow_text),
            FadeOut(self.author),
            run_time=1.0
        )

    # ============================================================
    # 辅助方法
    # ============================================================
    def make_system_display(self, ineq1_str, ineq2_str, pos, color1, color2, scale=1.0):
        """创建不等式组显示（带大括号）"""
        ineq1 = MathTex(ineq1_str, color=color1, font_size=int(36 * scale))
        ineq2 = MathTex(ineq2_str, color=color2, font_size=int(36 * scale))

        # 竖排
        group = VGroup(ineq1, ineq2).arrange(DOWN, buff=0.3 * scale, aligned_edge=LEFT)

        # 左大括号
        brace = MathTex(r"\left\{", font_size=int(60 * scale), color=WHITE)
        brace.next_to(group, LEFT, buff=0.1 * scale)

        result = VGroup(brace, group).move_to(pos)
        return result

    def make_rule_card(self, text, color):
        """创建口诀标题卡片"""
        bg = RoundedRectangle(
            width=7.0, height=0.8,
            corner_radius=0.2,
            fill_color=color,
            fill_opacity=0.25,
            stroke_color=color,
            stroke_width=2
        )
        label = Text(text, font=FONT, font_size=28, color=color, weight=BOLD)
        return VGroup(bg, label)

    def _make_summary_card(self, rule, desc, color):
        """创建口诀汇总卡片"""
        bg = RoundedRectangle(
            width=7.5, height=1.8,
            corner_radius=0.25,
            fill_color=COLOR_CARD_BG,
            fill_opacity=1,
            stroke_color=color,
            stroke_width=2
        )
        rule_text = Text(rule, font=FONT, font_size=26, color=color, weight=BOLD)
        desc_text = Text(desc, font=FONT, font_size=18, color=GRAY_A)
        content = VGroup(rule_text, desc_text).arrange(DOWN, buff=0.2)
        return VGroup(bg, content)

    def _make_two_number_lines(self):
        """创建两条数轴（上下排列用于口诀展示）"""
        nl1 = make_number_line(x_range=(0, 7), unit=self.UNIT, y_pos=0, color=GRAY_A)
        nl1.move_to(UP * 2.2)
        nl2 = make_number_line(x_range=(0, 7), unit=self.UNIT, y_pos=0, color=GRAY_A)
        nl2.move_to(UP * 0.5)
        return nl1, nl2

    def _val_to_x(self, val, x_min=0, x_max=7):
        """将数轴数值转换为逻辑x坐标（居中，0-7范围）"""
        center_x = 0.0
        x_min_logical = center_x - (x_max - x_min) / 2 * self.UNIT
        return x_min_logical + (val - x_min) * self.UNIT

    def _make_right_arrow(self, x_start, y, color, extend=1.8, stroke_width=5):
        """创建向右的箭头+空心圆（表示 x > a）"""
        arrow = Arrow(
            start=np.array([x_start, y, 0]),
            end=np.array([x_start + extend, y, 0]),
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=0.12,
            buff=0
        )
        dot = Circle(radius=0.09, color=color, stroke_width=3)
        dot.move_to(np.array([x_start, y, 0]))
        dot.set_fill(BG_COLOR, opacity=1)
        return VGroup(arrow, dot)

    def _make_left_arrow(self, x_end, y, color, extend=1.8, stroke_width=5):
        """创建向左的箭头+空心圆（表示 x < a）"""
        arrow = Arrow(
            start=np.array([x_end, y, 0]),
            end=np.array([x_end - extend, y, 0]),
            color=color,
            stroke_width=stroke_width,
            max_tip_length_to_length_ratio=0.12,
            buff=0
        )
        dot = Circle(radius=0.09, color=color, stroke_width=3)
        dot.move_to(np.array([x_end, y, 0]))
        dot.set_fill(BG_COLOR, opacity=1)
        return VGroup(arrow, dot)