"""
combination_animation.py - 组合与组合数 教学动画
高三数学第十六章 排列组合与二项式定理

# 快速预览
manim -pql combination_animation.py CombinationLesson

# 高质量输出
manim -qh combination_animation.py CombinationLesson

内容: 组合定义、组合数公式、对称性、帕斯卡三角形、求和公式
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ======================== 全局配置 ========================
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ======================== 颜色常量 ========================
BG_COLOR     = "#1a1a2e"
COLOR_TITLE  = "#e8d5b7"
COLOR_HL     = "#f6c90e"       # 黄色高亮
COLOR_FORMULA= "#4ecdc4"       # 青色公式
COLOR_RED    = "#ff6b6b"       # 红色强调
COLOR_BLUE   = "#45b7d1"       # 蓝色
COLOR_GREEN  = "#96ceb4"       # 绿色
COLOR_ORANGE = "#f4a261"       # 橙色
COLOR_PURPLE = "#c084fc"       # 紫色
COLOR_GRAY   = "#a0a0b0"

# 学生颜色
STUDENT_COLORS = ["#ff6b6b", "#45b7d1", "#96ceb4", "#f6c90e", "#c084fc"]

FONT_CN = "Noto Sans CJK SC"


class CombinationLesson(Scene):
    """
    组合与组合数 - 完整教学动画
    7个场景, 约65秒
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 全程显示的作者标识
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN, font_size=18, color=COLOR_GRAY
        ).move_to(UP * 7.0)
        self.add(self.author_bar)

        # 执行各场景
        self.scene1_hook()
        self.scene2_concept()
        self.scene3_formula()
        self.scene4_symmetry()
        self.scene5_pascal()
        self.scene6_sum()
        self.scene7_outro()

    # ===================== Scene 1: 开场钩子 =====================
    def scene1_hook(self):
        """开场：提出问题，展示5名学生"""

        # 标题
        title = Text("班级选拔赛", font=FONT_CN, font_size=44, color=COLOR_HL
                     ).move_to(UP * 6.0)

        question = Text("从5名同学中，选3人参赛",
                        font=FONT_CN, font_size=32, color=WHITE
                        ).move_to(UP * 5.1)

        sub = Text("共有几种选法？",
                   font=FONT_CN, font_size=36, color=COLOR_RED
                   ).move_to(UP * 4.3)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(question, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)

        # 5 个学生圆圈
        labels = ["A", "B", "C", "D", "E"]
        positions = [np.array([-3.0 + i * 1.5, 2.2, 0]) for i in range(5)]
        circles = VGroup()
        for i, (pos, label, col) in enumerate(zip(positions, labels, STUDENT_COLORS)):
            c = Circle(radius=0.42, color=col, fill_opacity=0.85,
                       stroke_width=3).move_to(pos)
            t = Text(label, font=FONT_CN, font_size=26,
                     color=WHITE, weight=BOLD).move_to(pos)
            circles.add(VGroup(c, t))

        for circle in circles:
            self.play(GrowFromCenter(circle), run_time=0.18)

        # 高亮选中的 A、B、C
        self.wait(0.3)
        selected_idx = [0, 1, 2]
        for i in selected_idx:
            self.play(
                circles[i][0].animate.set_stroke(width=5, color=COLOR_HL),
                run_time=0.2
            )

        # 闪烁选中的3个
        self.play(
            *[Indicate(circles[i], scale_factor=1.15, color=COLOR_HL)
              for i in selected_idx],
            run_time=0.7
        )

        # 问号闪现
        qmark = Text("?", font=FONT_CN, font_size=80, color=COLOR_HL
                     ).move_to(DOWN * 0.5)
        self.play(GrowFromCenter(qmark), run_time=0.4)
        self.wait(1.0)

        # 清场
        self.play(
            FadeOut(VGroup(title, question, sub, circles, qmark)),
            run_time=0.5
        )

    # ===================== Scene 2: 组合概念 =====================
    def scene2_concept(self):
        """引入组合概念：顺序无关"""

        title = Text("什么是组合？",
                     font=FONT_CN, font_size=40, color=COLOR_HL
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 排列对比：ABC / BAC / CAB 是"不同排列"
        perm_label = Text("排列（考虑顺序）",
                          font=FONT_CN, font_size=24, color=COLOR_ORANGE
                          ).move_to(UP * 5.1)
        self.play(FadeIn(perm_label), run_time=0.4)

        perms = ["ABC", "BAC", "CAB"]
        perm_texts = VGroup(*[
            Text(p, font=FONT_CN, font_size=32, color=COLOR_ORANGE)
            for p in perms
        ]).arrange(RIGHT, buff=0.8).move_to(UP * 4.0)

        self.play(
            LaggedStart(*[FadeIn(t, shift=DOWN * 0.2)
                          for t in perm_texts], lag_ratio=0.3),
            run_time=0.8
        )

        # 标注"3种不同排列"
        diff_note = Text("→ 3 种不同排列",
                         font=FONT_CN, font_size=22, color=COLOR_ORANGE
                         ).next_to(perm_texts, DOWN, buff=0.2)
        self.play(FadeIn(diff_note), run_time=0.3)
        self.wait(0.5)

        # 分隔线
        sep = Line(LEFT * 3.5, RIGHT * 3.5, color=COLOR_GRAY, stroke_width=1
                   ).move_to(UP * 2.9)
        self.play(Create(sep), run_time=0.3)

        # 组合视角：ABC = BAC = CAB 是"同一组合"
        comb_label = Text("组合（不考虑顺序）",
                          font=FONT_CN, font_size=24, color=COLOR_BLUE
                          ).move_to(UP * 2.4)
        self.play(FadeIn(comb_label), run_time=0.4)

        comb_texts = VGroup(*[
            Text(p, font=FONT_CN, font_size=32, color=COLOR_BLUE)
            for p in perms
        ]).arrange(RIGHT, buff=0.8).move_to(UP * 1.5)
        self.play(
            LaggedStart(*[FadeIn(t, shift=DOWN * 0.2)
                          for t in comb_texts], lag_ratio=0.3),
            run_time=0.7
        )

        # 画等号连线
        eq1 = Text("=", font=FONT_CN, font_size=32, color=COLOR_HL
                   ).move_to(comb_texts[0].get_center() + RIGHT * 1.0 + UP * 0)
        eq2 = Text("=", font=FONT_CN, font_size=32, color=COLOR_HL
                   ).move_to(comb_texts[1].get_center() + RIGHT * 1.0 + UP * 0)

        same_note = Text("→ 同一种组合  {A,B,C}",
                         font=FONT_CN, font_size=22, color=COLOR_BLUE
                         ).next_to(comb_texts, DOWN, buff=0.2)
        self.play(
            FadeIn(same_note),
            run_time=0.4
        )
        self.wait(0.5)

        # 定义框
        def_box = RoundedRectangle(
            width=7.5, height=1.8, corner_radius=0.25,
            color=COLOR_FORMULA, stroke_width=2, fill_opacity=0.1,
            fill_color=COLOR_FORMULA
        ).move_to(DOWN * 0.2)

        def_text1 = Text("从 n 个不同元素中取出 m 个元素",
                         font=FONT_CN, font_size=22, color=WHITE
                         ).move_to(DOWN * 0 + UP * 0.3)
        def_text2 = Text("不考虑顺序，组成一组",
                         font=FONT_CN, font_size=22, color=WHITE
                         ).move_to(DOWN * 0.5)

        key = Text("核心：只看取哪些，不看顺序！",
                   font=FONT_CN, font_size=26, color=COLOR_HL
                   ).move_to(DOWN * 1.5)

        self.play(FadeIn(def_box), run_time=0.3)
        self.play(Write(def_text1), Write(def_text2), run_time=0.8)
        self.play(FadeIn(key, shift=UP * 0.2), run_time=0.4)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(VGroup(
                title, perm_label, perm_texts, diff_note, sep,
                comb_label, comb_texts, same_note,
                def_box, def_text1, def_text2, key
            )),
            run_time=0.5
        )

    # ===================== Scene 3: 组合数公式 =====================
    def scene3_formula(self):
        """推导组合数公式 C(n,m) = n!/[m!(n-m)!]"""

        title = Text("组合数公式",
                     font=FONT_CN, font_size=40, color=COLOR_HL
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 逻辑推导：排列 ÷ 重复计算次数 = 组合
        step0 = Text("从排列到组合的推导：",
                     font=FONT_CN, font_size=24, color=COLOR_GRAY
                     ).move_to(UP * 5.2)
        self.play(FadeIn(step0), run_time=0.4)

        # 排列数关系
        logic_text = Text("m个元素的排列 = 同一组合 × m! 种排法",
                          font=FONT_CN, font_size=22, color=COLOR_ORANGE
                          ).move_to(UP * 4.3)
        self.play(Write(logic_text), run_time=0.7)

        # 公式1: A(n,m) = C(n,m) × m!
        f1 = MathTex(
            r"A(n,m) = C(n,m) \times m!",
            font_size=34, color=WHITE
        ).move_to(UP * 3.2)
        self.play(Write(f1), run_time=0.7)

        # 变形
        arrow = Text("↓  两边除以 m!",
                     font=FONT_CN, font_size=22, color=COLOR_GRAY
                     ).move_to(UP * 2.5)
        self.play(FadeIn(arrow), run_time=0.3)

        # 公式2: C(n,m) = A(n,m) / m!
        f2 = MathTex(
            r"C(n,m) = \frac{A(n,m)}{m!}",
            font_size=38, color=COLOR_FORMULA
        ).move_to(UP * 1.5)
        self.play(Write(f2), run_time=0.8)
        self.wait(0.5)

        # 展开 A(n,m)
        arrow2 = Text("展开 A(n,m) = n!/(n-m)!  →",
                      font=FONT_CN, font_size=20, color=COLOR_GRAY
                      ).move_to(UP * 0.5)
        self.play(FadeIn(arrow2), run_time=0.3)

        # 完整公式框
        formula_box = RoundedRectangle(
            width=7.0, height=1.3, corner_radius=0.2,
            color=COLOR_HL, stroke_width=2.5, fill_opacity=0.08,
            fill_color=COLOR_HL
        ).move_to(DOWN * 0.5)

        f3 = MathTex(
            r"C(n,m) = \frac{n!}{m! \cdot (n-m)!}",
            font_size=40, color=COLOR_HL
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(formula_box), Write(f3), run_time=0.9)
        self.play(Indicate(f3, scale_factor=1.05), run_time=0.5)
        self.wait(0.8)

        # 示例计算 C(5,3)
        example_title = Text("例：C(5,3) = ?",
                             font=FONT_CN, font_size=28, color=COLOR_GREEN
                             ).move_to(DOWN * 1.8)
        self.play(FadeIn(example_title), run_time=0.4)

        calc1 = MathTex(
            r"C(5,3) = \frac{5!}{3! \cdot 2!}",
            font_size=32, color=WHITE
        ).move_to(DOWN * 2.7)
        self.play(Write(calc1), run_time=0.7)

        calc2 = MathTex(
            r"= \frac{120}{6 \times 2} = \frac{120}{12}",
            font_size=32, color=WHITE
        ).move_to(DOWN * 3.7)
        self.play(Write(calc2), run_time=0.7)

        # 结果高亮
        result_box = RoundedRectangle(
            width=4.0, height=0.9, corner_radius=0.2,
            color=COLOR_RED, stroke_width=2.5, fill_opacity=0.15,
            fill_color=COLOR_RED
        ).move_to(DOWN * 4.8)

        result_num = MathTex(r"= 10", font_size=38, color=COLOR_RED)
        result_unit = Text("种", font=FONT_CN, font_size=34, color=COLOR_RED)
        result = VGroup(result_num, result_unit).arrange(RIGHT, buff=0.15).move_to(DOWN * 4.8)

        self.play(FadeIn(result_box), Write(result), run_time=0.7)
        self.play(Flash(result, color=COLOR_HL, flash_radius=0.5), run_time=0.5)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(VGroup(
                title, step0, logic_text, f1, arrow, f2, arrow2,
                formula_box, f3, example_title, calc1, calc2,
                result_box, result
            )),
            run_time=0.5
        )

    # ===================== Scene 4: 对称性 =====================
    def scene4_symmetry(self):
        """C(n,m) = C(n,n-m) 对称性直觉解释"""

        title = Text("组合数的对称性",
                     font=FONT_CN, font_size=38, color=COLOR_HL
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 直觉动画：5个圆，选3个 ↔ 排除2个
        intro = Text("选 3 个  ↔  排除 2 个",
                     font=FONT_CN, font_size=28, color=WHITE
                     ).move_to(UP * 5.1)
        self.play(FadeIn(intro), run_time=0.4)

        # 第一行：选中的3个（高亮）
        row1_label = Text("选中：",
                          font=FONT_CN, font_size=22, color=COLOR_GREEN
                          ).move_to(UP * 4.0 + LEFT * 3.0)

        labels = ["A", "B", "C", "D", "E"]
        row1_circles = VGroup()
        for i, (label, col) in enumerate(zip(labels, STUDENT_COLORS)):
            alpha = 0.9 if i < 3 else 0.2
            pos = np.array([-1.5 + i * 0.9, 0, 0]) + UP * 4.0
            c = Circle(radius=0.35, color=col, fill_opacity=alpha,
                       stroke_width=3).move_to(pos)
            t = Text(label, font=FONT_CN, font_size=20,
                     color=WHITE).move_to(pos)
            row1_circles.add(VGroup(c, t))

        self.play(FadeIn(row1_label), run_time=0.3)
        for circ in row1_circles:
            self.play(GrowFromCenter(circ), run_time=0.15)

        # 大括号标注
        brace_sel = Brace(
            VGroup(*[row1_circles[i] for i in range(3)]),
            direction=DOWN, color=COLOR_GREEN
        )
        sel_text = Text("3 个选中",
                        font=FONT_CN, font_size=18, color=COLOR_GREEN
                        ).next_to(brace_sel, DOWN, buff=0.05)
        self.play(FadeIn(brace_sel), FadeIn(sel_text), run_time=0.4)

        brace_not = Brace(
            VGroup(*[row1_circles[i] for i in range(3, 5)]),
            direction=DOWN, color=COLOR_RED
        )
        not_text = Text("2 个未选",
                        font=FONT_CN, font_size=18, color=COLOR_RED
                        ).next_to(brace_not, DOWN, buff=0.05)
        self.play(FadeIn(brace_not), FadeIn(not_text), run_time=0.4)

        self.wait(0.5)

        # 翻转逻辑：选中2个（原来未选的），排除3个
        logic_arrow = Text("反过来想：选 2 个留下  =  排除 3 个",
                           font=FONT_CN, font_size=22, color=COLOR_ORANGE
                           ).move_to(UP * 2.2)
        self.play(FadeIn(logic_arrow), run_time=0.5)

        # 结论 C(5,3) = C(5,2)
        eq_box = RoundedRectangle(
            width=6.0, height=0.9, corner_radius=0.2,
            color=COLOR_BLUE, stroke_width=2, fill_opacity=0.1,
            fill_color=COLOR_BLUE
        ).move_to(UP * 1.0)

        eq = MathTex(
            r"C(5,3) = C(5,2) = 10",
            font_size=36, color=COLOR_BLUE
        ).move_to(UP * 1.0)

        self.play(FadeIn(eq_box), Write(eq), run_time=0.7)
        self.wait(0.5)

        # 通用公式
        gen_box = RoundedRectangle(
            width=7.0, height=1.2, corner_radius=0.2,
            color=COLOR_HL, stroke_width=2.5, fill_opacity=0.08,
            fill_color=COLOR_HL
        ).move_to(DOWN * 0.3)

        gen = MathTex(
            r"C(n,m) = C(n, n-m)",
            font_size=38, color=COLOR_HL
        ).move_to(DOWN * 0.3)

        self.play(FadeIn(gen_box), Write(gen), run_time=0.8)
        self.play(Indicate(gen, scale_factor=1.05), run_time=0.5)

        # 用途提示
        tip = Text("可以把 m > n/2 的组合变小，方便计算！",
                   font=FONT_CN, font_size=22, color=COLOR_GRAY
                   ).move_to(DOWN * 1.7)
        self.play(FadeIn(tip), run_time=0.4)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(VGroup(
                title, intro, row1_label, row1_circles,
                brace_sel, sel_text, brace_not, not_text,
                logic_arrow, eq_box, eq, gen_box, gen, tip
            )),
            run_time=0.5
        )

    # ===================== Scene 5: 帕斯卡三角形 =====================
    def scene5_pascal(self):
        """帕斯卡三角形与递推公式"""

        title = Text("帕斯卡三角形",
                     font=FONT_CN, font_size=40, color=COLOR_HL
                     ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        subtitle = Text("每个数 = 正上方两数之和",
                        font=FONT_CN, font_size=24, color=COLOR_GRAY
                        ).move_to(UP * 5.7)
        self.play(FadeIn(subtitle), run_time=0.4)

        # 帕斯卡三角形数据
        pascal = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
        ]

        ROW_H = 0.72
        COL_W = 0.85
        ORIGIN_Y = 4.3   # 第0行的 y 坐标
        OFFSET_Y = -1.2  # 向下偏移用于居中

        # 构建三角形 Mobject 矩阵
        all_cells = []
        for row_idx, row in enumerate(pascal):
            row_cells = []
            for col_idx, val in enumerate(row):
                x = (col_idx - (len(row) - 1) / 2) * COL_W
                y = ORIGIN_Y + OFFSET_Y - row_idx * ROW_H

                num_text = Text(
                    str(val), font=FONT_CN,
                    font_size=26 if val < 10 else 22,
                    color=WHITE
                ).move_to(np.array([x, y, 0]))
                row_cells.append(num_text)
            all_cells.append(row_cells)

        # 逐行淡入
        for row_idx, row_cells in enumerate(all_cells):
            row_group = VGroup(*row_cells)
            delay = row_idx * 0.2
            self.play(
                LaggedStart(*[FadeIn(c, shift=DOWN * 0.15) for c in row_cells],
                             lag_ratio=0.12),
                run_time=0.5
            )

        self.wait(0.5)

        # 高亮 C(4,2)=6，及其来源 C(3,1)=3, C(3,2)=3
        # 第4行（row_idx=4）第2列（0-indexed: col=2）→ 值=6
        # 第3行（row_idx=3）第1列（col=1）→ 值=3
        # 第3行（row_idx=3）第2列（col=2）→ 值=3

        cell_62 = all_cells[4][2]   # C(4,2)=6
        cell_31 = all_cells[3][1]   # C(3,1)=3
        cell_32 = all_cells[3][2]   # C(3,2)=3

        # 为三个单元格画高亮框
        hl_62 = SurroundingRectangle(cell_62, color=COLOR_HL, buff=0.12)
        hl_31 = SurroundingRectangle(cell_31, color=COLOR_BLUE, buff=0.12)
        hl_32 = SurroundingRectangle(cell_32, color=COLOR_GREEN, buff=0.12)

        self.play(Create(hl_31), Create(hl_32), run_time=0.4)
        self.play(Create(hl_62), run_time=0.3)

        # 画两条箭头
        arr1 = Arrow(
            cell_31.get_center(), cell_62.get_center(),
            buff=0.2, color=COLOR_BLUE, stroke_width=2,
            max_tip_length_to_length_ratio=0.2
        )
        arr2 = Arrow(
            cell_32.get_center(), cell_62.get_center(),
            buff=0.2, color=COLOR_GREEN, stroke_width=2,
            max_tip_length_to_length_ratio=0.2
        )
        self.play(Create(arr1), Create(arr2), run_time=0.6)

        # 标注方程
        eq_note = MathTex(
            r"3 + 3 = 6",
            font_size=32, color=COLOR_HL
        ).move_to(DOWN * 1.8)
        self.play(Write(eq_note), run_time=0.6)

        pascal_eq = MathTex(
            r"C(3,1) + C(3,2) = C(4,2)",
            font_size=28, color=COLOR_GRAY
        ).move_to(DOWN * 2.7)
        self.play(Write(pascal_eq), run_time=0.7)

        self.wait(0.8)

        # 通用递推公式
        formula_box = RoundedRectangle(
            width=7.8, height=1.3, corner_radius=0.2,
            color=COLOR_FORMULA, stroke_width=2.5, fill_opacity=0.1,
            fill_color=COLOR_FORMULA
        ).move_to(DOWN * 4.0)

        formula = MathTex(
            r"C(n,m) = C(n-1,m-1) + C(n-1,m)",
            font_size=28, color=COLOR_FORMULA
        ).move_to(DOWN * 4.0)

        self.play(FadeIn(formula_box), Write(formula), run_time=0.9)

        tip = Text("记住帕斯卡三角形，快速查组合数！",
                   font=FONT_CN, font_size=22, color=COLOR_ORANGE
                   ).move_to(DOWN * 5.3)
        self.play(FadeIn(tip), run_time=0.4)
        self.wait(1.5)

        # 清场
        all_triangle = VGroup(*[c for row in all_cells for c in row])
        self.play(
            FadeOut(VGroup(
                title, subtitle, all_triangle,
                hl_62, hl_31, hl_32, arr1, arr2,
                eq_note, pascal_eq, formula_box, formula, tip
            )),
            run_time=0.5
        )

    # ===================== Scene 6: 求和公式 =====================
    def scene6_sum(self):
        """∑C(n,k) = 2^n 的直观理解"""

        title = Text("组合数求和公式",
                     font=FONT_CN, font_size=38, color=COLOR_HL
                     ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        idea = Text("每个元素：选 或 不选，共 2 种",
                    font=FONT_CN, font_size=26, color=WHITE
                    ).move_to(UP * 5.2)
        self.play(FadeIn(idea), run_time=0.5)

        # 以 n=3 (ABC) 演示
        eg_label = Text("以 n = 3（元素 A、B、C）为例：",
                        font=FONT_CN, font_size=22, color=COLOR_GRAY
                        ).move_to(UP * 4.3)
        self.play(FadeIn(eg_label), run_time=0.3)

        # 列出所有 2^3=8 个子集
        subsets = [
            ("∅（0个）", "C(3,0)=1", "#888"),
            ("A  B  C（各1个）", "C(3,1)=3", COLOR_BLUE),
            ("AB AC BC（各2个）", "C(3,2)=3", COLOR_GREEN),
            ("ABC（3个）", "C(3,3)=1", COLOR_ORANGE),
        ]

        row_group = VGroup()
        for i, (desc, cnt, col) in enumerate(subsets):
            y = 3.2 - i * 0.95
            desc_t = Text(desc, font=FONT_CN, font_size=20, color=col
                          ).move_to(np.array([-1.0, y, 0]))
            cnt_t = Text(cnt, font=FONT_CN, font_size=20, color=col
                         ).move_to(np.array([2.6, y, 0]))
            row_group.add(VGroup(desc_t, cnt_t))

        for row in row_group:
            self.play(FadeIn(row, shift=LEFT * 0.2), run_time=0.3)

        self.wait(0.5)

        # 求和
        sum_eq1 = MathTex(
            r"C(3,0) + C(3,1) + C(3,2) + C(3,3)",
            font_size=26, color=WHITE
        ).move_to(DOWN * 0.8)
        self.play(Write(sum_eq1), run_time=0.7)

        sum_eq2 = MathTex(
            r"= 1 + 3 + 3 + 1 = 8 = 2^3",
            font_size=30, color=COLOR_HL
        ).move_to(DOWN * 1.8)
        self.play(Write(sum_eq2), run_time=0.7)

        # 通用公式框
        gen_box = RoundedRectangle(
            width=7.5, height=1.3, corner_radius=0.2,
            color=COLOR_PURPLE, stroke_width=2.5, fill_opacity=0.1,
            fill_color=COLOR_PURPLE
        ).move_to(DOWN * 3.2)

        gen = MathTex(
            r"C(n,0) + C(n,1) + \cdots + C(n,n) = 2^n",
            font_size=28, color=COLOR_PURPLE
        ).move_to(DOWN * 3.2)

        self.play(FadeIn(gen_box), Write(gen), run_time=0.9)
        self.play(Indicate(gen, scale_factor=1.04), run_time=0.5)

        note = Text("所有子集的个数 = 2^n",
                    font=FONT_CN, font_size=22, color=COLOR_ORANGE
                    ).move_to(DOWN * 4.5)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(VGroup(
                title, idea, eg_label, row_group,
                sum_eq1, sum_eq2, gen_box, gen, note
            )),
            run_time=0.5
        )

    # ===================== Scene 7: 片尾 =====================
    def scene7_outro(self):
        """总结公式卡片 + 关注引导"""

        title = Text("组合数公式总结",
                     font=FONT_CN, font_size=36, color=COLOR_HL
                     ).move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 公式卡片
        cards_data = [
            (r"C(n,m) = \frac{n!}{m!(n-m)!}", "定义公式", COLOR_FORMULA),
            (r"C(n,m) = C(n,n-m)", "对称性", COLOR_BLUE),
            (r"C(n,m) = C(n-1,m-1)+C(n-1,m)", "递推公式", COLOR_GREEN),
            (r"\sum_{k=0}^{n} C(n,k) = 2^n", "求和公式", COLOR_PURPLE),
        ]

        card_group = VGroup()
        for i, (formula_str, label_str, col) in enumerate(cards_data):
            y = 4.0 - i * 1.6

            box = RoundedRectangle(
                width=7.5, height=1.3, corner_radius=0.2,
                color=col, stroke_width=1.5, fill_opacity=0.08,
                fill_color=col
            ).move_to(np.array([0, y, 0]))

            label = Text(label_str, font=FONT_CN, font_size=18, color=col
                         ).move_to(np.array([-2.5, y + 0.3, 0]))

            f = MathTex(formula_str, font_size=24, color=WHITE
                        ).move_to(np.array([0.5, y - 0.1, 0]))

            card_group.add(VGroup(box, label, f))

        for card in card_group:
            self.play(FadeIn(card, shift=LEFT * 0.3), run_time=0.4)

        self.wait(0.8)

        # 作者信息放大
        self.play(FadeOut(title), run_time=0.3)

        author_big = Text(
            "上海初高中数学直通车",
            font=FONT_CN, font_size=42, color=WHITE
        ).move_to(DOWN * 3.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT_CN, font_size=30, color=COLOR_GRAY
        ).move_to(DOWN * 4.5)

        cta = Text(
            "关注我，获得更多数学技巧！",
            font=FONT_CN, font_size=28, color=COLOR_HL
        ).move_to(DOWN * 5.6)

        self.play(FadeIn(author_big, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(cta, scale=1.1), run_time=0.5)

        # 装饰：小星星/闪光
        sparkles = VGroup()
        for angle in np.linspace(0, 2 * np.pi, 6, endpoint=False):
            pos = np.array([np.cos(angle) * 2.0, -5.6 + np.sin(angle) * 0.5, 0])
            star = Star(5, outer_radius=0.18, inner_radius=0.08,
                        color=COLOR_HL, fill_opacity=0.9)
            star.move_to(pos)
            sparkles.add(star)

        self.play(
            LaggedStart(*[GrowFromCenter(s) for s in sparkles], lag_ratio=0.1),
            run_time=0.5
        )
        self.play(Rotate(sparkles, angle=PI, run_time=1.0))
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(card_group, author_big, author_id, cta, sparkles)),
            run_time=0.8
        )