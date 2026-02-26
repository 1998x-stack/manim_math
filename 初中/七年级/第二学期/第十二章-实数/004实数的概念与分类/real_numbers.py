"""
实数的概念与分类 - Manim 教学动画
年级: 七年级第二学期 第十二章
知识点: 实数的概念与分类
格式: TikTok 竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
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
# 颜色常量
# ============================================================
COLOR_BG          = "#1a1a2e"
COLOR_RATIONAL    = "#4fc3f7"   # 天蓝 - 有理数
COLOR_IRRATIONAL  = "#ff7043"   # 橙红 - 无理数
COLOR_INTEGER     = "#66bb6a"   # 绿色 - 整数
COLOR_FRACTION    = "#ffd54f"   # 金黄 - 分数
COLOR_ZERO        = "#ce93d8"   # 紫色 - 零
COLOR_NEGATIVE    = "#ef9a9a"   # 浅红 - 负数
COLOR_POSITIVE    = "#80cbc4"   # 青绿 - 正数
COLOR_AXIS        = "#b0bec5"   # 灰白 - 数轴
COLOR_AUTHOR      = "#78909c"
FONT = "Noto Sans CJK SC"


class RealNumbersConcept(Scene):
    """
    实数的概念与分类教学动画

    场景流程:
    1. 开场钩子 — π 是什么数？
    2. 数轴展示 — 实数与数轴的一一对应
    3. 分类树 — 实数 → 有理数 & 无理数
    4. 举例说明 — 各类实数举例
    5. 正负分类 — 第二种分类方式
    6. 总结 + 片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG
        self.scene_opening()
        self.scene_number_line()
        self.scene_classification_tree()
        self.scene_examples()
        self.scene_pos_neg_classification()
        self.scene_outro()

    # ============================================================
    # Scene 1: 开场钩子
    # ============================================================
    def scene_opening(self):
        # 作者信息
        author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=20, color=COLOR_AUTHOR
        ).move_to(UP * 7.3)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author_obj = author

        # 标题
        title = Text("实数的概念与分类", font=FONT, font_size=44, color=GOLD)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.8)

        # 钩子问题
        hook = Text("π 是有理数还是无理数？", font=FONT, font_size=32, color=WHITE)
        hook.move_to(UP * 4.8)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.6)

        # 展示一些数字
        nums_data = [
            (r"\frac{1}{2}", LEFT * 3.0 + UP * 3.2, COLOR_RATIONAL),
            (r"\sqrt{2}", LEFT * 1.2 + UP * 3.5, COLOR_IRRATIONAL),
            (r"\pi",     RIGHT * 0.8 + UP * 3.2, COLOR_IRRATIONAL),
            (r"-3",      RIGHT * 2.8 + UP * 3.5, COLOR_RATIONAL),
            (r"0",       LEFT * 0.2 + UP * 2.6, COLOR_ZERO),
            (r"0.333\ldots", LEFT * 2.5 + UP * 2.2, COLOR_RATIONAL),
        ]
        num_mobs = []
        for tex_str, pos, col in nums_data:
            m = MathTex(tex_str, font_size=36, color=col)
            m.move_to(pos)
            num_mobs.append(m)

        for m in num_mobs:
            self.play(FadeIn(m, scale=0.7), run_time=0.25)

        # 问号脉冲
        question = Text("它们分别属于哪类？", font=FONT, font_size=28, color=YELLOW)
        question.move_to(UP * 1.0)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清除
        fade_group = VGroup(*num_mobs, question, hook, title)
        self.play(FadeOut(fade_group), run_time=0.5)

    # ============================================================
    # Scene 2: 数轴与实数一一对应
    # ============================================================
    def scene_number_line(self):
        # 小标题
        sec_title = Text("实数与数轴", font=FONT, font_size=36, color=GOLD)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.6)

        # 创建数轴 — 放在屏幕中上部
        number_line = NumberLine(
            x_range=[-4, 4, 1],
            length=7.5,
            include_numbers=True,
            include_tip=True,
            numbers_to_exclude=[],
            color=COLOR_AXIS,
            tip_width=0.2,
            tip_height=0.2,
            font_size=28,
        )
        number_line.move_to(UP * 4.0)
        self.play(Create(number_line), run_time=1.2)
        self.number_line = number_line

        # 在数轴上标注各类数
        points_data = [
            (-3,      "-3",    DOWN,  COLOR_RATIONAL),
            (-1,      "-1",    DOWN,  COLOR_RATIONAL),
            (0,       "0",     DOWN,  COLOR_ZERO),
            (1,       "1",     DOWN,  COLOR_RATIONAL),
            (np.sqrt(2), r"\sqrt{2}", UP, COLOR_IRRATIONAL),
            (np.pi,   r"\pi",  UP,    COLOR_IRRATIONAL),
        ]

        dots_group = VGroup()
        labels_group = VGroup()

        explain = Text("每个实数对应数轴上唯一一点", font=FONT, font_size=26, color=WHITE)
        explain.move_to(UP * 2.2)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)

        for val, label_str, direction, color in points_data:
            x_pos = number_line.number_to_point(val)
            dot = Dot(x_pos, radius=0.1, color=color)
            label = MathTex(label_str, font_size=30, color=color)
            buff_val = 0.35 if direction[1] > 0 else 0.35
            label.next_to(dot, direction, buff=buff_val)

            self.play(
                FadeIn(dot, scale=0.5),
                FadeIn(label),
                run_time=0.4
            )
            dots_group.add(dot)
            labels_group.add(label)

        self.wait(0.5)

        # 有理数 vs 无理数 分组高亮
        rational_label = Text("有理数", font=FONT, font_size=22, color=COLOR_RATIONAL)
        rational_label.move_to(LEFT * 2.8 + UP * 0.8)
        irrational_label = Text("无理数", font=FONT, font_size=22, color=COLOR_IRRATIONAL)
        irrational_label.move_to(RIGHT * 2.5 + UP * 0.8)

        self.play(
            FadeIn(rational_label, shift=UP * 0.2),
            FadeIn(irrational_label, shift=UP * 0.2),
            run_time=0.5
        )

        # 关键结论
        conclusion = Text("实数与数轴上的点  一一对应", font=FONT, font_size=28, color=YELLOW)
        conclusion.move_to(DOWN * 0.2)
        underline = Line(
            conclusion.get_left() + DOWN * 0.1,
            conclusion.get_right() + DOWN * 0.1,
            color=YELLOW, stroke_width=2
        )
        self.play(Write(conclusion), Create(underline), run_time=0.8)
        self.wait(1.2)

        # 保留数轴，清除其他
        self.play(
            FadeOut(VGroup(sec_title, explain, dots_group, labels_group,
                           rational_label, irrational_label, conclusion, underline)),
            number_line.animate.scale(0.7).move_to(UP * 2.0),
            run_time=0.7
        )
        self.number_line_small = number_line

    # ============================================================
    # Scene 3: 分类树（核心）
    # ============================================================
    def scene_classification_tree(self):
        # 移走数轴
        self.play(FadeOut(self.number_line_small), run_time=0.4)

        sec_title = Text("实数的分类", font=FONT, font_size=38, color=GOLD)
        sec_title.move_to(UP * 7.0)
        self.play(Write(sec_title), run_time=0.5)

        # ── 构建分类树 ──
        # 节点位置（精确计算）
        pos_root    = np.array([0.0,  5.5, 0])
        pos_rat     = np.array([-2.8, 4.0, 0])
        pos_irrat   = np.array([ 2.8, 4.0, 0])
        pos_int     = np.array([-3.8, 2.5, 0])
        pos_frac    = np.array([-1.8, 2.5, 0])
        pos_neg_int = np.array([-4.2, 1.0, 0])
        pos_zero    = np.array([-3.2, 1.0, 0])
        pos_pos_int = np.array([-2.2, 1.0, 0])

        # 节点框
        def make_node(text_str, pos, color, font_size=26, width=1.8, height=0.55):
            box = RoundedRectangle(
                width=width, height=height,
                corner_radius=0.15,
                color=color, fill_color=color,
                fill_opacity=0.25, stroke_width=2
            )
            txt = Text(text_str, font=FONT, font_size=font_size, color=WHITE)
            grp = VGroup(box, txt)
            txt.move_to(box.get_center())
            grp.move_to(pos)
            return grp

        node_root  = make_node("实数  R",   pos_root,    GOLD,            font_size=30, width=2.4, height=0.65)
        node_rat   = make_node("有理数  Q", pos_rat,     COLOR_RATIONAL,  font_size=26, width=2.4, height=0.6)
        node_irrat = make_node("无理数",    pos_irrat,   COLOR_IRRATIONAL,font_size=26, width=2.4, height=0.6)
        node_int   = make_node("整数",      pos_int,     COLOR_INTEGER,   font_size=24, width=1.6, height=0.55)
        node_frac  = make_node("分数/小数", pos_frac,    COLOR_FRACTION,  font_size=22, width=1.8, height=0.55)
        node_neg   = make_node("负整数",    pos_neg_int, COLOR_NEGATIVE,  font_size=20, width=1.6, height=0.50)
        node_zero  = make_node("零",        pos_zero,    COLOR_ZERO,      font_size=24, width=0.9, height=0.50)
        node_pos   = make_node("正整数",    pos_pos_int, COLOR_POSITIVE,  font_size=20, width=1.6, height=0.50)

        # 连接线（从父节点底部到子节点顶部）
        def make_edge(parent_node, child_node, color=GRAY):
            start = parent_node.get_bottom()
            end   = child_node.get_top()
            return Line(start, end, color=color, stroke_width=2)

        edge_root_rat   = make_edge(node_root, node_rat,   COLOR_RATIONAL)
        edge_root_irrat = make_edge(node_root, node_irrat, COLOR_IRRATIONAL)
        edge_rat_int    = make_edge(node_rat,  node_int,   COLOR_INTEGER)
        edge_rat_frac   = make_edge(node_rat,  node_frac,  COLOR_FRACTION)
        edge_int_neg    = make_edge(node_int,  node_neg,   COLOR_NEGATIVE)
        edge_int_zero   = make_edge(node_int,  node_zero,  COLOR_ZERO)
        edge_int_pos    = make_edge(node_int,  node_pos,   COLOR_POSITIVE)

        # 无理数例子（右侧）
        irrat_examples = VGroup(
            MathTex(r"\sqrt{2},\ \sqrt{3},\ \pi,\ e", font_size=26, color=COLOR_IRRATIONAL)
        )
        irrat_examples.next_to(node_irrat, DOWN, buff=0.4)

        # ── 动画：逐层展示分类树 ──
        # 根节点
        self.play(FadeIn(node_root, scale=0.7), run_time=0.5)
        self.wait(0.3)

        # 第一层
        self.play(
            Create(edge_root_rat),
            Create(edge_root_irrat),
            run_time=0.5
        )
        self.play(
            FadeIn(node_rat, shift=DOWN * 0.3),
            FadeIn(node_irrat, shift=DOWN * 0.3),
            run_time=0.6
        )

        # 无理数举例
        self.play(FadeIn(irrat_examples, shift=DOWN * 0.2), run_time=0.5)
        self.wait(0.3)

        # 第二层 - 整数和分数
        self.play(
            Create(edge_rat_int),
            Create(edge_rat_frac),
            run_time=0.4
        )
        self.play(
            FadeIn(node_int, shift=DOWN * 0.3),
            FadeIn(node_frac, shift=DOWN * 0.3),
            run_time=0.6
        )

        # 分数举例
        frac_examples = MathTex(
            r"\frac{1}{2},\ -\frac{3}{4},\ 0.25,\ 0.\overline{3}",
            font_size=22, color=COLOR_FRACTION
        )
        frac_examples.next_to(node_frac, DOWN, buff=0.35)
        self.play(FadeIn(frac_examples, shift=DOWN * 0.2), run_time=0.4)

        # 第三层 - 整数的细分
        self.play(
            Create(edge_int_neg),
            Create(edge_int_zero),
            Create(edge_int_pos),
            run_time=0.5
        )
        self.play(
            FadeIn(node_neg, shift=DOWN * 0.2),
            FadeIn(node_zero, shift=DOWN * 0.2),
            FadeIn(node_pos, shift=DOWN * 0.2),
            run_time=0.6
        )

        # 举例
        neg_ex = MathTex(r"\ldots,-2,-1", font_size=20, color=COLOR_NEGATIVE)
        neg_ex.next_to(node_neg, DOWN, buff=0.2)
        pos_ex = MathTex(r"1,2,\ldots", font_size=20, color=COLOR_POSITIVE)
        pos_ex.next_to(node_pos, DOWN, buff=0.2)

        self.play(
            FadeIn(neg_ex),
            FadeIn(pos_ex),
            run_time=0.4
        )

        # 高亮 R = Q ∪ 无理数  — 避免MathTex含中文，使用Text
        formula_text = Text("R = 有理数 ∪ 无理数", font=FONT, font_size=26, color=YELLOW)
        formula_text.move_to(DOWN * 6.2)
        box_formula = SurroundingRectangle(formula_text, color=YELLOW, buff=0.15, corner_radius=0.1)

        self.play(
            FadeIn(formula_text),
            Create(box_formula),
            run_time=0.6
        )
        self.wait(2.0)

        # 收集所有树元素
        tree_group = VGroup(
            node_root, node_rat, node_irrat, node_int, node_frac,
            node_neg, node_zero, node_pos,
            edge_root_rat, edge_root_irrat, edge_rat_int, edge_rat_frac,
            edge_int_neg, edge_int_zero, edge_int_pos,
            irrat_examples, frac_examples, neg_ex, pos_ex,
            formula_text, box_formula
        )

        self.play(FadeOut(tree_group), FadeOut(sec_title), run_time=0.6)

    # ============================================================
    # Scene 4: 举例说明
    # ============================================================
    def scene_examples(self):
        sec_title = Text("各类实数举例", font=FONT, font_size=36, color=GOLD)
        sec_title.move_to(UP * 7.0)
        self.play(Write(sec_title), run_time=0.5)

        # 表格式展示
        rows = [
            ("有理数", [r"\frac{2}{3}", r"-5", r"0", r"1.5", r"0.\overline{6}"], COLOR_RATIONAL),
            ("无理数", [r"\sqrt{2}", r"\sqrt{5}", r"\pi", r"e", r"-\sqrt{3}"],   COLOR_IRRATIONAL),
        ]

        all_elements = VGroup()

        y_start = 5.0
        for i, (category, examples, color) in enumerate(rows):
            y = y_start - i * 3.2

            # 类别标签
            cat_text = Text(category, font=FONT, font_size=30, color=color)
            cat_box = RoundedRectangle(
                width=2.2, height=0.65, corner_radius=0.15,
                color=color, fill_color=color, fill_opacity=0.3, stroke_width=2
            )
            cat_box.move_to(LEFT * 3.5 + UP * y)
            cat_text.move_to(cat_box.get_center())

            self.play(FadeIn(cat_box), Write(cat_text), run_time=0.4)

            # 例子逐个出现
            ex_mobs = VGroup()
            x_positions = np.linspace(-1.5, 3.8, len(examples))
            for j, (ex_str, x) in enumerate(zip(examples, x_positions)):
                ex = MathTex(ex_str, font_size=32, color=color)
                ex.move_to(np.array([x, y, 0]))
                ex_mobs.add(ex)
                self.play(FadeIn(ex, scale=0.7), run_time=0.25)

            # 分隔线
            sep_line = Line(
                LEFT * 4.0 + UP * (y - 1.3),
                RIGHT * 4.0 + UP * (y - 1.3),
                color=GRAY, stroke_width=1, stroke_opacity=0.4
            )
            self.play(Create(sep_line), run_time=0.3)

            all_elements.add(cat_box, cat_text, ex_mobs, sep_line)

        # 关键提示
        tip1 = Text("有理数 = 能写成", font=FONT, font_size=24, color=COLOR_RATIONAL)
        tip1_frac = MathTex(r"\dfrac{p}{q}", font_size=28, color=COLOR_RATIONAL)
        tip1_end = Text("（p,q为整数，q≠0）", font=FONT, font_size=22, color=COLOR_RATIONAL)
        tip1_row = VGroup(tip1, tip1_frac, tip1_end).arrange(RIGHT, buff=0.15)
        tip1_row.move_to(DOWN * 1.0)

        tip2 = Text("无理数 = 无限不循环小数", font=FONT, font_size=24, color=COLOR_IRRATIONAL)
        tip2.move_to(DOWN * 2.0)

        self.play(FadeIn(tip1_row, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(tip2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(all_elements, tip1_row, tip2, sec_title)), run_time=0.5)

    # ============================================================
    # Scene 5: 正负分类
    # ============================================================
    def scene_pos_neg_classification(self):
        sec_title = Text("实数的另一种分类", font=FONT, font_size=34, color=GOLD)
        sec_title.move_to(UP * 7.0)
        self.play(Write(sec_title), run_time=0.5)

        subtitle = Text("按正负分类", font=FONT, font_size=28, color=WHITE)
        subtitle.move_to(UP * 6.0)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 三列展示
        col_data = [
            ("正实数", [r"1,\ 2,\ \frac{1}{3},\ \sqrt{2},\ \pi", r"\cdots"], COLOR_POSITIVE, LEFT * 2.8),
            ("零",     [r"0"],                                                   COLOR_ZERO,     ORIGIN),
            ("负实数", [r"-1,\ -\sqrt{3},\ -\pi", r"\cdots"],                  COLOR_NEGATIVE, RIGHT * 2.8),
        ]

        col_groups = VGroup()
        for label_str, examples, color, x_offset in col_data:
            box = RoundedRectangle(
                width=2.4, height=0.7, corner_radius=0.15,
                color=color, fill_color=color, fill_opacity=0.3, stroke_width=2
            )
            box.move_to(x_offset + UP * 4.5)
            label = Text(label_str, font=FONT, font_size=26, color=WHITE)
            label.move_to(box.get_center())

            ex_mobs = VGroup()
            for k, ex_str in enumerate(examples):
                ex = MathTex(ex_str, font_size=22, color=color)
                ex.move_to(x_offset + UP * (3.5 - k * 0.7))
                ex_mobs.add(ex)

            col_groups.add(VGroup(box, label, ex_mobs))

        for grp in col_groups:
            self.play(FadeIn(grp, shift=DOWN * 0.3), run_time=0.5)

        # 数轴上的正负
        number_line2 = NumberLine(
            x_range=[-4, 4, 1], length=7.5,
            include_numbers=True, include_tip=True,
            numbers_to_exclude=[],
            color=COLOR_AXIS, font_size=26,
            tip_width=0.2, tip_height=0.2,
        )
        number_line2.move_to(UP * 1.8)
        self.play(Create(number_line2), run_time=0.8)

        # 着色区域（正负）
        # 正数段：从0到右
        pos_region = Line(
            number_line2.number_to_point(0.05),
            number_line2.number_to_point(3.8),
            color=COLOR_POSITIVE, stroke_width=8, stroke_opacity=0.7
        )
        neg_region = Line(
            number_line2.number_to_point(-3.8),
            number_line2.number_to_point(-0.05),
            color=COLOR_NEGATIVE, stroke_width=8, stroke_opacity=0.7
        )
        zero_dot = Dot(number_line2.number_to_point(0), radius=0.14, color=COLOR_ZERO)

        self.play(
            Create(pos_region),
            Create(neg_region),
            FadeIn(zero_dot, scale=0.5),
            run_time=0.8
        )

        # 正负标签
        pos_lbl = Text("正实数", font=FONT, font_size=22, color=COLOR_POSITIVE)
        pos_lbl.next_to(pos_region, UP, buff=0.25)
        neg_lbl = Text("负实数", font=FONT, font_size=22, color=COLOR_NEGATIVE)
        neg_lbl.next_to(neg_region, UP, buff=0.25)

        self.play(FadeIn(pos_lbl), FadeIn(neg_lbl), run_time=0.4)

        # 总结公式
        summary = Text("实数 = 正实数 + 零 + 负实数", font=FONT, font_size=26, color=YELLOW)
        summary.move_to(DOWN * 4.5)
        box_s = SurroundingRectangle(summary, color=YELLOW, buff=0.2, corner_radius=0.1)
        self.play(FadeIn(summary), Create(box_s), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(sec_title, subtitle, col_groups, number_line2,
                           pos_region, neg_region, zero_dot,
                           pos_lbl, neg_lbl, summary, box_s)),
            run_time=0.6
        )

    # ============================================================
    # Scene 6: 总结 + 片尾
    # ============================================================
    def scene_outro(self):
        # 总结框
        summary_title = Text("📌 本节要点", font=FONT, font_size=34, color=GOLD)
        summary_title.move_to(UP * 6.5)
        self.play(Write(summary_title), run_time=0.5)

        points_data = [
            ("实数 = 有理数 + 无理数", COLOR_RATIONAL),
            ("有理数可写成 p/q 的形式", COLOR_RATIONAL),
            ("无理数是无限不循环小数", COLOR_IRRATIONAL),
            ("实数与数轴上的点一一对应", YELLOW),
            ("实数也可按正负分为三类", WHITE),
        ]

        point_mobs = VGroup()
        for i, (txt, color) in enumerate(points_data):
            bullet = Text(f"• {txt}", font=FONT, font_size=24, color=color)
            bullet.move_to(UP * (5.0 - i * 1.1))
            bullet.align_to(LEFT * 0.5, LEFT)
            point_mobs.add(bullet)

        for mob in point_mobs:
            self.play(FadeIn(mob, shift=RIGHT * 0.3), run_time=0.35)

        self.wait(1.5)

        # 片尾
        self.play(FadeOut(VGroup(summary_title, point_mobs)), run_time=0.5)

        # 作者放大
        author_big = Text("上海初高中数学直通车", font=FONT, font_size=40, color=WHITE)
        author_big.move_to(UP * 2.0)
        author_id  = Text("@emptyandcalm", font=FONT, font_size=30, color=COLOR_AUTHOR)
        author_id.move_to(UP * 1.0)

        self.play(
            Transform(self.author_obj, author_big),
            run_time=0.6
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text("关注我，获得更多数学技巧！", font=FONT, font_size=30, color=YELLOW)
        follow.move_to(DOWN * 0.5)
        self.play(FadeIn(follow, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 装饰小图标：小圆圈
        deco = VGroup(*[
            Circle(radius=0.18, fill_color=c, fill_opacity=0.9, stroke_width=0)
            .move_to(follow.get_center() + UP * 1.2 + RIGHT * (i - 2) * 1.0)
            for i, c in enumerate([
                COLOR_RATIONAL, COLOR_IRRATIONAL, COLOR_INTEGER,
                COLOR_FRACTION, COLOR_ZERO
            ])
        ])
        self.play(*[GrowFromCenter(d) for d in deco], run_time=0.6)

        labels_deco = VGroup(
            Text("有理", font=FONT, font_size=14, color=COLOR_RATIONAL).next_to(deco[0], DOWN, buff=0.08),
            Text("无理", font=FONT, font_size=14, color=COLOR_IRRATIONAL).next_to(deco[1], DOWN, buff=0.08),
            Text("整数", font=FONT, font_size=14, color=COLOR_INTEGER).next_to(deco[2], DOWN, buff=0.08),
            Text("分数", font=FONT, font_size=14, color=COLOR_FRACTION).next_to(deco[3], DOWN, buff=0.08),
            Text("零",   font=FONT, font_size=14, color=COLOR_ZERO).next_to(deco[4], DOWN, buff=0.08),
        )
        self.play(*[FadeIn(l) for l in labels_deco], run_time=0.4)

        self.wait(2.0)

        self.play(FadeOut(VGroup(self.author_obj, author_id, follow, deco, labels_deco)),
                  run_time=1.0)


# ============================================================
# 运行命令:
# manim -pql real_numbers.py RealNumbersConcept   # 快速预览
# manim -qh  real_numbers.py RealNumbersConcept   # 高质量
# ============================================================