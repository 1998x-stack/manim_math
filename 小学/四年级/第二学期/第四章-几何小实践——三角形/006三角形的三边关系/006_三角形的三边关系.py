"""
三角形的三边关系 - Triangle Side Relationship Animation
使用 Manim 创建的小学四年级几何教学视频

内容: 三角形任意两边之和大于第三边；判断三条线段能否构成三角形；已知两边求第三边范围
目标观众: 小学四年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class TriangleSideRelationLesson(Scene):
    """
    三角形三边关系教学动画

    场景顺序:
    1. 开场钩子 - 提问能否围成三角形
    2. 核心定理 - 两边之和大于第三边
    3. 动手演示 - 用三根棍子演示
    4. 判断练习 - 三组数据判断
    5. 三边范围 - 已知两边求第三边范围
    6. 片尾总结
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色方案
        self.COLOR_PRIMARY = "#4fc3f7"      # 亮蓝 - 主色
        self.COLOR_SUCCESS = "#66bb6a"      # 绿色 - 成功/能构成
        self.COLOR_DANGER = "#ef5350"       # 红色 - 失败/不能构成
        self.COLOR_HIGHLIGHT = "#ffd54f"    # 金黄 - 高亮
        self.COLOR_FORMULA = "#ce93d8"      # 紫色 - 公式
        self.COLOR_TRIANGLE = "#80deea"     # 青色 - 三角形
        self.COLOR_SIDE_A = "#ff8a65"       # 橙色 - 边a
        self.COLOR_SIDE_B = "#aed581"       # 浅绿 - 边b
        self.COLOR_SIDE_C = "#ba68c8"       # 紫色 - 边c

        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_theorem()
        self.scene_3_demo()
        self.scene_4_practice()
        self.scene_5_range()
        self.scene_6_outro()

    # =========================================================
    # 场景1：开场钩子
    # =========================================================
    def scene_1_opening(self):
        """开场：用问题吸引注意力"""
        # 作者信息
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.add(author)

        # 钩子标题
        hook_line1 = Text(
            "3根棍子",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(UP * 5.0)

        hook_line2 = Text(
            "一定能围成三角形吗？",
            font="PingFang SC",
            font_size=34,
            color=WHITE
        ).move_to(UP * 4.0)

        self.play(Write(hook_line1), run_time=0.8)
        self.play(FadeIn(hook_line2, shift=UP * 0.3), run_time=0.6)
        self.wait(0.5)

        # 展示三根棍子（三条线段）
        # 棍子1：长度3（短）
        stick1_start = np.array([-3.2, 2.0, 0])
        stick1_end = np.array([-0.7, 2.0, 0])
        stick1 = Line(stick1_start, stick1_end,
                      color=self.COLOR_SIDE_A, stroke_width=10)
        label1 = Text("3 cm", font="PingFang SC",
                      font_size=22, color=self.COLOR_SIDE_A)
        label1.next_to(stick1, DOWN, buff=0.15)

        # 棍子2：长度3（短）
        stick2_start = np.array([-0.5, 2.0, 0])
        stick2_end = np.array([2.0, 2.0, 0])
        stick2 = Line(stick2_start, stick2_end,
                      color=self.COLOR_SIDE_B, stroke_width=10)
        label2 = Text("3 cm", font="PingFang SC",
                      font_size=22, color=self.COLOR_SIDE_B)
        label2.next_to(stick2, DOWN, buff=0.15)

        # 棍子3：长度8（长）
        stick3_start = np.array([-3.5, 0.8, 0])
        stick3_end = np.array([3.5, 0.8, 0])
        stick3 = Line(stick3_start, stick3_end,
                      color=self.COLOR_SIDE_C, stroke_width=10)
        label3 = Text("8 cm", font="PingFang SC",
                      font_size=22, color=self.COLOR_SIDE_C)
        label3.next_to(stick3, DOWN, buff=0.15)

        self.play(
            Create(stick1), Create(stick2), Create(stick3),
            run_time=1.0
        )
        self.play(
            FadeIn(label1), FadeIn(label2), FadeIn(label3),
            run_time=0.5
        )
        self.wait(0.5)

        # 问号
        question = Text("???", font="PingFang SC",
                        font_size=60, color=self.COLOR_HIGHLIGHT)
        question.move_to(np.array([0, -0.5, 0]))
        self.play(FadeIn(question, scale=0.5), run_time=0.5)
        self.wait(0.8)

        # 清场
        self.play(
            FadeOut(hook_line1), FadeOut(hook_line2),
            FadeOut(stick1), FadeOut(stick2), FadeOut(stick3),
            FadeOut(label1), FadeOut(label2), FadeOut(label3),
            FadeOut(question),
            run_time=0.5
        )

    # =========================================================
    # 场景2：核心定理
    # =========================================================
    def scene_2_theorem(self):
        """展示三角形三边关系定理"""
        # 标题
        title = Text(
            "三角形三边关系",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.7)

        # 画一个标准三角形（坐标精确计算）
        A = np.array([-2.2, 3.5, 0])
        B = np.array([2.2, 3.5, 0])
        C = np.array([0.0, 6.0, 0])

        tri = Polygon(A, B, C, color=self.COLOR_TRIANGLE, stroke_width=3)
        tri.set_fill(self.COLOR_TRIANGLE, opacity=0.15)

        # 顶点标签
        lA = Text("A", font="PingFang SC", font_size=26, color=WHITE)
        lA.next_to(A, DL, buff=0.1)
        lB = Text("B", font="PingFang SC", font_size=26, color=WHITE)
        lB.next_to(B, DR, buff=0.1)
        lC = Text("C", font="PingFang SC", font_size=26, color=WHITE)
        lC.next_to(C, UP, buff=0.1)

        self.play(Create(tri), run_time=1.0)
        self.play(FadeIn(lA), FadeIn(lB), FadeIn(lC), run_time=0.4)

        # 边标签
        mid_AB = (A + B) / 2
        mid_BC = (B + C) / 2
        mid_CA = (C + A) / 2

        edge_c = Text("c (AB)", font="PingFang SC",
                      font_size=20, color=self.COLOR_SIDE_C)
        edge_c.move_to(mid_AB + DOWN * 0.35)
        edge_a = Text("a (BC)", font="PingFang SC",
                      font_size=20, color=self.COLOR_SIDE_A)
        edge_a.move_to(mid_BC + RIGHT * 0.5)
        edge_b = Text("b (CA)", font="PingFang SC",
                      font_size=20, color=self.COLOR_SIDE_B)
        edge_b.move_to(mid_CA + LEFT * 0.5)

        self.play(FadeIn(edge_c), FadeIn(edge_a), FadeIn(edge_b), run_time=0.5)
        self.wait(0.3)

        # 三个不等式（用MathTex，纯数学符号）
        formula1 = MathTex(r"a + b > c", font_size=36, color=self.COLOR_FORMULA)
        formula2 = MathTex(r"a + c > b", font_size=36, color=self.COLOR_FORMULA)
        formula3 = MathTex(r"b + c > a", font_size=36, color=self.COLOR_FORMULA)

        formulas = VGroup(formula1, formula2, formula3).arrange(DOWN, buff=0.35)
        formulas.move_to(np.array([0, 1.2, 0]))

        box = SurroundingRectangle(formulas, color=self.COLOR_FORMULA,
                                   buff=0.25, corner_radius=0)
        box.set_fill("#1a1a2e", opacity=0.8)

        self.play(FadeIn(box), run_time=0.3)
        self.play(Write(formula1), run_time=0.6)
        self.play(Write(formula2), run_time=0.6)
        self.play(Write(formula3), run_time=0.6)
        self.wait(0.4)

        # 核心结论
        conclusion_p1 = Text("任意两边之和", font="PingFang SC",
                              font_size=30, color=self.COLOR_HIGHLIGHT, weight=BOLD)
        conclusion_p2 = Text("大于第三边", font="PingFang SC",
                              font_size=30, color=self.COLOR_HIGHLIGHT, weight=BOLD)
        conclusion = VGroup(conclusion_p1, conclusion_p2).arrange(RIGHT, buff=0.1)
        conclusion.move_to(np.array([0, -0.5, 0]))

        self.play(FadeIn(conclusion, scale=1.05), run_time=0.7)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title), FadeOut(tri),
            FadeOut(lA), FadeOut(lB), FadeOut(lC),
            FadeOut(edge_a), FadeOut(edge_b), FadeOut(edge_c),
            FadeOut(box),
            FadeOut(formula1), FadeOut(formula2), FadeOut(formula3),
            FadeOut(conclusion),
            run_time=0.6
        )

    # =========================================================
    # 场景3：动手演示
    # =========================================================
    def scene_3_demo(self):
        """用线段演示能/不能构成三角形"""
        title = Text(
            "动手验证",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # --- 情形1：能构成三角形 3, 4, 5 ---
        case1_label = Text(
            "情形① 3 cm、4 cm、5 cm",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 5.5)
        self.play(FadeIn(case1_label), run_time=0.4)

        # 展示三条线段（水平排列）
        y_sticks = 4.5
        # 3cm -> 2.4单位
        s1_start = np.array([-4.0, y_sticks, 0])
        s1_end = np.array([-1.6, y_sticks, 0])
        s1 = Line(s1_start, s1_end, color=self.COLOR_SIDE_A, stroke_width=9)
        t1 = Text("3", font="PingFang SC", font_size=20, color=self.COLOR_SIDE_A)
        t1.next_to(s1, UP, buff=0.1)

        # 4cm -> 3.2单位
        s2_start = np.array([-1.3, y_sticks, 0])
        s2_end = np.array([1.9, y_sticks, 0])
        s2 = Line(s2_start, s2_end, color=self.COLOR_SIDE_B, stroke_width=9)
        t2 = Text("4", font="PingFang SC", font_size=20, color=self.COLOR_SIDE_B)
        t2.next_to(s2, UP, buff=0.1)

        # 5cm -> 4.0单位
        s3_start = np.array([2.2, y_sticks, 0])
        s3_end = np.array([2.2 + 3.2, y_sticks, 0])
        s3 = Line(s3_start, s3_end, color=self.COLOR_SIDE_C, stroke_width=9)
        t3 = Text("5", font="PingFang SC", font_size=20, color=self.COLOR_SIDE_C)
        t3.next_to(s3, UP, buff=0.1)

        self.play(Create(s1), Create(s2), Create(s3), run_time=0.7)
        self.play(FadeIn(t1), FadeIn(t2), FadeIn(t3), run_time=0.4)

        # 验证不等式（3+4=7>5）
        check1 = Text("3 + 4 = 7 > 5  ✓", font="PingFang SC",
                      font_size=22, color=self.COLOR_SUCCESS)
        check1.move_to(np.array([0, 3.5, 0]))
        check2 = Text("3 + 5 = 8 > 4  ✓", font="PingFang SC",
                      font_size=22, color=self.COLOR_SUCCESS)
        check2.move_to(np.array([0, 2.9, 0]))
        check3 = Text("4 + 5 = 9 > 3  ✓", font="PingFang SC",
                      font_size=22, color=self.COLOR_SUCCESS)
        check3.move_to(np.array([0, 2.3, 0]))

        self.play(Write(check1), run_time=0.5)
        self.play(Write(check2), run_time=0.5)
        self.play(Write(check3), run_time=0.5)

        # 画出三角形
        # 3-4-5 直角三角形，精确坐标
        scale_tri = 0.7
        tri_A = np.array([-1.5, 1.2, 0])
        tri_B = np.array([-1.5 + 4 * scale_tri, 1.2, 0])
        tri_C = np.array([-1.5, 1.2 + 3 * scale_tri, 0])

        good_tri = Polygon(tri_A, tri_B, tri_C,
                           color=self.COLOR_SUCCESS, stroke_width=3)
        good_tri.set_fill(self.COLOR_SUCCESS, opacity=0.2)

        result1 = Text("能构成三角形！", font="PingFang SC",
                       font_size=28, color=self.COLOR_SUCCESS, weight=BOLD)
        result1.move_to(np.array([0, -0.2, 0]))

        self.play(Create(good_tri), run_time=1.0)
        self.play(FadeIn(result1, scale=1.1), run_time=0.5)
        self.wait(1.0)

        # 清理情形1
        self.play(
            FadeOut(case1_label),
            FadeOut(s1), FadeOut(s2), FadeOut(s3),
            FadeOut(t1), FadeOut(t2), FadeOut(t3),
            FadeOut(check1), FadeOut(check2), FadeOut(check3),
            FadeOut(good_tri), FadeOut(result1),
            run_time=0.5
        )

        # --- 情形2：不能构成三角形 3, 3, 8 ---
        case2_label = Text(
            "情形② 3 cm、3 cm、8 cm",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 5.5)
        self.play(FadeIn(case2_label), run_time=0.4)

        # 8cm 底边（约6.4单位长，但场景最宽约9，用5.6单位）
        open_A = np.array([-2.8, 3.8, 0])
        open_B = np.array([2.8, 3.8, 0])

        side_c_demo = Line(open_A, open_B, color=self.COLOR_SIDE_C, stroke_width=9)
        tc_label = Text("8", font="PingFang SC",
                        font_size=20, color=self.COLOR_SIDE_C)
        tc_label.next_to(side_c_demo, DOWN, buff=0.12)

        self.play(Create(side_c_demo), FadeIn(tc_label), run_time=0.5)

        # 两条3cm棍从两端出发，各2.4单位，向上倾斜
        gap_A_end = open_A + np.array([2.4, 1.6, 0])
        gap_B_end = open_B + np.array([-2.4, 1.6, 0])

        side_a_demo = Line(open_A, gap_A_end, color=self.COLOR_SIDE_A, stroke_width=9)
        side_b_demo = Line(open_B, gap_B_end, color=self.COLOR_SIDE_B, stroke_width=9)

        ta_label = Text("3", font="PingFang SC",
                        font_size=20, color=self.COLOR_SIDE_A)
        ta_label.next_to(side_a_demo.get_center(), LEFT, buff=0.1)
        tb_label = Text("3", font="PingFang SC",
                        font_size=20, color=self.COLOR_SIDE_B)
        tb_label.next_to(side_b_demo.get_center(), RIGHT, buff=0.1)

        self.play(Create(side_a_demo), Create(side_b_demo), run_time=0.7)
        self.play(FadeIn(ta_label), FadeIn(tb_label), run_time=0.3)

        # 缺口（两端点之间的空隙）
        gap_line = DashedLine(gap_A_end, gap_B_end,
                              color=self.COLOR_DANGER,
                              dash_length=0.15, stroke_width=4)
        gap_mid = (gap_A_end + gap_B_end) / 2
        gap_label = Text("合不拢！", font="PingFang SC",
                         font_size=22, color=self.COLOR_DANGER, weight=BOLD)
        gap_label.move_to(gap_mid + UP * 0.4)

        self.play(Create(gap_line), FadeIn(gap_label), run_time=0.5)

        # 验算失败
        fail_check = Text("3 + 3 = 6 < 8  ✗", font="PingFang SC",
                          font_size=26, color=self.COLOR_DANGER, weight=BOLD)
        fail_check.move_to(np.array([0, 1.8, 0]))
        self.play(Write(fail_check), run_time=0.6)

        result2 = Text("不能构成三角形！", font="PingFang SC",
                       font_size=28, color=self.COLOR_DANGER, weight=BOLD)
        result2.move_to(np.array([0, 0.8, 0]))
        self.play(FadeIn(result2, scale=1.1), run_time=0.5)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title), FadeOut(case2_label),
            FadeOut(side_c_demo), FadeOut(tc_label),
            FadeOut(side_a_demo), FadeOut(side_b_demo),
            FadeOut(ta_label), FadeOut(tb_label),
            FadeOut(gap_line), FadeOut(gap_label),
            FadeOut(fail_check), FadeOut(result2),
            run_time=0.6
        )

    # =========================================================
    # 场景4：判断练习
    # =========================================================
    def scene_4_practice(self):
        """三组数据让学生判断"""
        title = Text(
            "判断练习",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6.5)

        subtitle = Text(
            "哪组能围成三角形？",
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).move_to(UP * 5.6)

        self.play(Write(title), FadeIn(subtitle), run_time=0.6)

        # 技巧提示
        tip = Text(
            "只需验证：最小两边之和 > 最长边",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.7)
        self.play(FadeIn(tip, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 练习数据
        cases = [
            ("① 2, 4, 7", "2+4=6 < 7", False),
            ("② 5, 6, 8", "5+6=11 > 8", True),
            ("③ 3, 3, 3", "3+3=6 > 3", True),
        ]

        y_positions = [3.5, 1.8, 0.1]
        case_texts = []
        answer_items = []

        for i, (case_str, check_str, can_form) in enumerate(cases):
            y = y_positions[i]
            case_text = Text(
                case_str,
                font="PingFang SC",
                font_size=28,
                color=WHITE
            ).move_to(np.array([-1.0, y, 0]))
            case_texts.append(case_text)
            self.play(FadeIn(case_text, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        self.wait(0.6)

        # 逐一揭示答案
        for i, (case_str, check_str, can_form) in enumerate(cases):
            y = y_positions[i]
            color = self.COLOR_SUCCESS if can_form else self.COLOR_DANGER

            check = Text(
                check_str,
                font="PingFang SC",
                font_size=21,
                color=color
            ).move_to(np.array([0.2, y - 0.6, 0]))

            symbol = "✓" if can_form else "✗"
            result_sym = Text(
                symbol,
                font="PingFang SC",
                font_size=32,
                color=color,
                weight=BOLD
            ).move_to(np.array([3.2, y, 0]))

            self.play(FadeIn(check, shift=UP * 0.2), run_time=0.4)
            self.play(FadeIn(result_sym, scale=1.2), run_time=0.3)
            self.wait(0.4)
            answer_items.extend([check, result_sym])

        self.wait(1.0)

        # 清场
        all_objs = [title, subtitle, tip] + case_texts + answer_items
        self.play(*[FadeOut(obj) for obj in all_objs], run_time=0.6)

    # =========================================================
    # 场景5：第三边的范围
    # =========================================================
    def scene_5_range(self):
        """已知两边求第三边的取值范围"""
        title = Text(
            "第三边的范围",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 题目
        prob1 = Text("已知两边分别为", font="PingFang SC",
                     font_size=27, color=WHITE)
        prob2 = Text("3 cm  和  5 cm", font="PingFang SC",
                     font_size=32, color=self.COLOR_HIGHLIGHT, weight=BOLD)
        prob3 = Text("第三边  c  的范围是？", font="PingFang SC",
                     font_size=27, color=WHITE)
        problem = VGroup(prob1, prob2, prob3).arrange(DOWN, buff=0.2)
        problem.move_to(UP * 4.8)

        self.play(FadeIn(problem, shift=UP * 0.3), run_time=0.7)
        self.wait(0.5)

        # 推导步骤
        step_title = Text(
            "根据三边关系，c 必须满足：",
            font="PingFang SC",
            font_size=24,
            color=GRAY_A
        ).move_to(UP * 3.4)
        self.play(FadeIn(step_title), run_time=0.4)

        # 条件①
        cond1_a = Text("条件①：3 + c > 5", font="PingFang SC",
                       font_size=24, color=self.COLOR_SIDE_A)
        cond1_arr = Text("→", font="PingFang SC", font_size=24, color=WHITE)
        cond1_b = Text("c > 2", font="PingFang SC",
                       font_size=24, color=self.COLOR_HIGHLIGHT, weight=BOLD)
        cond1 = VGroup(cond1_a, cond1_arr, cond1_b).arrange(RIGHT, buff=0.2)
        cond1.move_to(UP * 2.5)
        self.play(FadeIn(cond1, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.3)

        # 条件②（恒成立）
        cond2_a = Text("条件②：5 + c > 3", font="PingFang SC",
                       font_size=24, color=self.COLOR_SIDE_B)
        cond2_arr = Text("→", font="PingFang SC", font_size=24, color=WHITE)
        cond2_b = Text("恒成立", font="PingFang SC",
                       font_size=22, color=GRAY_B)
        cond2 = VGroup(cond2_a, cond2_arr, cond2_b).arrange(RIGHT, buff=0.2)
        cond2.move_to(UP * 1.7)
        self.play(FadeIn(cond2, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.3)

        # 条件③
        cond3_a = Text("条件③：3 + 5 > c", font="PingFang SC",
                       font_size=24, color=self.COLOR_SIDE_C)
        cond3_arr = Text("→", font="PingFang SC", font_size=24, color=WHITE)
        cond3_b = Text("c < 8", font="PingFang SC",
                       font_size=24, color=self.COLOR_HIGHLIGHT, weight=BOLD)
        cond3 = VGroup(cond3_a, cond3_arr, cond3_b).arrange(RIGHT, buff=0.2)
        cond3.move_to(UP * 0.9)
        self.play(FadeIn(cond3, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.4)

        # 最终结论框
        concl_lead = Text("综合得：", font="PingFang SC",
                          font_size=26, color=WHITE)
        concl_formula = MathTex(r"2 < c < 8", font_size=44, color=self.COLOR_HIGHLIGHT)
        concl_unit = Text("（单位：cm）", font="PingFang SC",
                          font_size=20, color=GRAY_B)
        conclusion = VGroup(concl_lead, concl_formula, concl_unit).arrange(RIGHT, buff=0.2)
        conclusion.move_to(np.array([0, -0.3, 0]))

        concl_box = SurroundingRectangle(conclusion, color=self.COLOR_HIGHLIGHT,
                                         buff=0.3, corner_radius=0)
        concl_box.set_fill("#2d1b4e", opacity=0.7)

        self.play(FadeIn(concl_box), run_time=0.3)
        self.play(FadeIn(conclusion, scale=1.05), run_time=0.7)
        self.wait(0.5)

        # 数轴可视化
        # 数轴从0到10，x_min_axis为左端点位置
        x_min_axis = -3.5
        x_scale = 0.7   # 每1个cm数值 = 0.7逻辑单位
        axis_y = -1.8

        axis = Line(np.array([x_min_axis, axis_y, 0]),
                    np.array([x_min_axis + 10.5 * x_scale, axis_y, 0]),
                    color=GRAY_A, stroke_width=2)
        arrow_right = Arrow(np.array([x_min_axis + 10.0 * x_scale, axis_y, 0]),
                            np.array([x_min_axis + 10.5 * x_scale, axis_y, 0]),
                            color=GRAY_A, buff=0,
                            stroke_width=2,
                            max_tip_length_to_length_ratio=0.4)

        # 刻度 0,2,4,6,8,10
        tick_vals = [0, 2, 4, 6, 8, 10]
        ticks = VGroup()
        tick_labels = VGroup()
        for v in tick_vals:
            xp = x_min_axis + v * x_scale
            tick = Line(np.array([xp, axis_y - 0.12, 0]),
                        np.array([xp, axis_y + 0.12, 0]),
                        color=GRAY_A, stroke_width=1.5)
            ticks.add(tick)
            tlbl = Text(str(v), font="PingFang SC",
                        font_size=16, color=GRAY_B)
            tlbl.move_to(np.array([xp, axis_y - 0.38, 0]))
            tick_labels.add(tlbl)

        self.play(Create(axis), Create(ticks), FadeIn(tick_labels), run_time=0.5)

        # 高亮区间 (2, 8)（开区间，用空心圆端点）
        x2 = x_min_axis + 2 * x_scale
        x8 = x_min_axis + 8 * x_scale

        valid_range = Line(np.array([x2, axis_y, 0]),
                           np.array([x8, axis_y, 0]),
                           color=self.COLOR_SUCCESS, stroke_width=10)

        dot2 = Circle(radius=0.13, color=self.COLOR_SUCCESS, stroke_width=2)
        dot2.set_fill("#1a1a2e", opacity=1)
        dot2.move_to(np.array([x2, axis_y, 0]))

        dot8 = Circle(radius=0.13, color=self.COLOR_SUCCESS, stroke_width=2)
        dot8.set_fill("#1a1a2e", opacity=1)
        dot8.move_to(np.array([x8, axis_y, 0]))

        range_label = Text("c 的有效范围", font="PingFang SC",
                           font_size=18, color=self.COLOR_SUCCESS)
        range_label.move_to(np.array([(x2 + x8) / 2, axis_y + 0.45, 0]))

        self.play(Create(valid_range), run_time=0.7)
        self.play(FadeIn(dot2), FadeIn(dot8), run_time=0.3)
        self.play(FadeIn(range_label), run_time=0.3)
        self.wait(1.5)

        # 口诀
        rule_text = Text(
            "口诀：两差 < 第三边 < 两和",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_FORMULA
        ).move_to(np.array([0, -3.5, 0]))
        rule_box = SurroundingRectangle(rule_text, color=self.COLOR_FORMULA, buff=0.2)
        self.play(FadeIn(rule_box), Write(rule_text), run_time=0.7)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title), FadeOut(problem), FadeOut(step_title),
            FadeOut(cond1), FadeOut(cond2), FadeOut(cond3),
            FadeOut(concl_box), FadeOut(conclusion),
            FadeOut(axis), FadeOut(ticks), FadeOut(tick_labels),
            FadeOut(valid_range), FadeOut(dot2), FadeOut(dot8),
            FadeOut(range_label), FadeOut(rule_text), FadeOut(rule_box),
            run_time=0.6
        )

    # =========================================================
    # 场景6：片尾总结
    # =========================================================
    def scene_6_outro(self):
        """总结知识点并引导关注"""
        summary_title = Text(
            "本节重点回顾",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_PRIMARY,
            weight=BOLD
        ).move_to(UP * 5.5)
        self.play(Write(summary_title), run_time=0.6)

        # 三张知识点卡片
        points = [
            ("①", "三边关系定理", "任意两边之和 > 第三边"),
            ("②", "快速判断法", "最小两边之和 > 最长边"),
            ("③", "第三边范围", "两边之差 < 第三边 < 两边之和"),
        ]

        y_start = 4.0
        card_objects = []
        for i, (num, pt_title, pt_content) in enumerate(points):
            y = y_start - i * 2.1

            num_text = Text(num, font="PingFang SC",
                            font_size=30, color=self.COLOR_HIGHLIGHT, weight=BOLD)
            title_text = Text(pt_title, font="PingFang SC",
                              font_size=26, color=WHITE, weight=BOLD)
            content_text = Text(pt_content, font="PingFang SC",
                                font_size=21, color=GRAY_A)

            row = VGroup(num_text, title_text).arrange(RIGHT, buff=0.2)
            card = VGroup(row, content_text).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
            card.move_to(np.array([0.2, y, 0]))

            card_bg = SurroundingRectangle(card, color="#334155", buff=0.22, corner_radius=0)
            card_bg.set_fill("#0f172a", opacity=0.7)

            self.play(FadeIn(card_bg), FadeIn(card, shift=RIGHT * 0.3), run_time=0.5)
            card_objects.extend([card_bg, card])
            self.wait(0.2)

        self.wait(1.0)

        # 作者信息
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=32,
            color=WHITE,
            weight=BOLD
        ).move_to(np.array([0, -3.5, 0]))

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=26,
            color=GRAY_B
        ).move_to(np.array([0, -4.3, 0]))

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(np.array([0, -5.3, 0]))

        self.play(FadeIn(author_big, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(follow_text, scale=1.05), run_time=0.5)

        # 小三角形装饰
        deco_tris = VGroup()
        for i in range(5):
            angle_offset = i * 2 * PI / 5
            pos = np.array([
                3.2 * np.cos(angle_offset),
                -6.5 + 0.5 * np.sin(angle_offset),
                0
            ])
            tri_deco = Triangle(color=self.COLOR_TRIANGLE, fill_opacity=0.6)
            tri_deco.scale(0.18)
            tri_deco.move_to(pos)
            deco_tris.add(tri_deco)

        self.play(*[FadeIn(t, scale=0.5) for t in deco_tris], run_time=0.5)
        self.wait(2.0)

        # 全部淡出
        all_out = card_objects + [
            summary_title, author_big, author_id, follow_text, deco_tris
        ]
        self.play(*[FadeOut(obj) for obj in all_out], run_time=1.0)
        self.wait(0.5)
