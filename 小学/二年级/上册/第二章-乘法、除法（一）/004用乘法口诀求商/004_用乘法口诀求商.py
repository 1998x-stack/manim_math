"""
004_用乘法口诀求商.py — 用乘法口诀求商 教学动画

知识点: 核心方法：想'几乘除数等于被除数'，建立乘除法之间的逆运算关系
年级: 二年级上册
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 乘法与除法的关系（逆运算引入）
  2. 例题1: 24 ÷ 4 = ? → 想"四(六)二十四" → 商是6
  3. 例题2: 18 ÷ 3 = ? → 想"三(六)十八" → 商是6
  4. 例题3: 30 ÷ 5 = ? → 想"五(六)三十" → 商是6
  5. 方法总结 + 小练习
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
COLOR_DIVIDEND = "#3b82f6"    # 蓝色 被除数
COLOR_DIVISOR = "#22c55e"     # 绿色 除数
COLOR_QUOTIENT = "#f59e0b"    # 橙色 商
COLOR_HL = "#fbbf24"          # 黄色高亮
COLOR_WARN = "#ef4444"        # 红色
COLOR_RULE = "#a78bfa"        # 紫色规则
COLOR_MULT = "#f472b6"        # 粉色 乘法口诀
COLOR_AUTHOR = "#6b7280"
COLOR_CARD = "#0f172a"
FONT = "Noto Sans CJK SC"


class MultiplicationTableDivisionLesson(Scene):
    """
    用乘法口诀求商 教学动画
    场景:
      1. 开场钩子
      2. 乘除法关系（逆运算）
      3. 例题1: 24 / 4 = 6
      4. 例题2: 18 / 3 = 6
      5. 例题3: 30 / 5 = 6
      6. 方法总结
      7. 小练习
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_inverse()
        self.scene_3_example_1()
        self.scene_4_example_2()
        self.scene_5_example_3()
        self.scene_6_summary()
        self.scene_7_practice()
        self.scene_8_outro()

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
            "用乘法口诀求商", font=FONT, font_size=48,
            color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)

        hook2 = Text(
            "除法也能用口诀？", font=FONT, font_size=36,
            color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.7)
        self.play(Write(hook2), run_time=0.6)

        # 展示一个除法问号
        problem = MathTex(
            r"24 \div 4 = \;?",
            font_size=52, color=COLOR_DIVIDEND
        ).move_to(UP * 1.5)
        self.play(FadeIn(problem, scale=0.6), run_time=0.8)

        # 思考泡泡
        think = Text(
            "想一想，怎么算？", font=FONT, font_size=28,
            color=GRAY_A
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(think, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(hook1, hook2, problem, think)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 2: 乘除法逆运算关系
    # ------------------------------------------------------------------
    def scene_2_inverse(self):
        title = Text(
            "乘法和除法是好朋友", font=FONT, font_size=34,
            color=COLOR_RULE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 乘法算式
        mult_label = Text(
            "乘法：", font=FONT, font_size=26, color=COLOR_MULT
        )
        mult_eq = MathTex(
            r"4 \times 6 = 24", font_size=42, color=WHITE
        )
        mult_group = VGroup(mult_label, mult_eq).arrange(
            RIGHT, buff=0.3
        ).move_to(UP * 3.5)
        self.play(Write(mult_group), run_time=0.8)
        self.wait(0.3)

        # 箭头：从乘法到除法
        arrow = Arrow(
            start=UP * 2.7, end=UP * 1.8,
            color=COLOR_HL, stroke_width=4, buff=0.1
        )
        arrow_text = Text(
            "反过来", font=FONT, font_size=22, color=COLOR_HL
        ).next_to(arrow, RIGHT, buff=0.2)
        self.play(
            GrowArrow(arrow), FadeIn(arrow_text),
            run_time=0.6
        )

        # 除法算式
        div_label = Text(
            "除法：", font=FONT, font_size=26, color=COLOR_DIVIDEND
        )
        div_eq = MathTex(
            r"24 \div 4 = 6", font_size=42, color=WHITE
        )
        div_group = VGroup(div_label, div_eq).arrange(
            RIGHT, buff=0.3
        ).move_to(UP * 1.0)
        self.play(Write(div_group), run_time=0.8)
        self.wait(0.3)

        # 关键说明
        key = Text(
            "知道乘法，就能算除法！", font=FONT, font_size=28,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 0.8)
        self.play(Write(key), run_time=0.6)

        # 图解：苹果分组
        desc = Text(
            "24个苹果，每4个一组，分几组？", font=FONT,
            font_size=22, color=GRAY_A
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(desc, shift=UP * 0.2), run_time=0.5)

        # 苹果网格 6 列 x 4 行
        apple_grid = VGroup()
        colors_6 = [
            "#ef4444", "#f97316", "#eab308",
            "#22c55e", "#3b82f6", "#8b5cf6"
        ]
        for col in range(6):
            col_group = VGroup()
            for row in range(4):
                dot = Dot(
                    radius=0.12,
                    color=colors_6[col],
                    fill_opacity=0.9
                )
                dot.move_to(
                    np.array([
                        (col - 2.5) * 0.6,
                        -3.5 + row * 0.5,
                        0
                    ])
                )
                col_group.add(dot)
            apple_grid.add(col_group)

        for col_group in apple_grid:
            self.play(FadeIn(col_group, shift=UP * 0.1), run_time=0.15)
        self.wait(0.3)

        # 圈出每一列（每组4个）
        rects = VGroup()
        for col in range(6):
            rect = RoundedRectangle(
                width=0.5, height=2.2,
                corner_radius=0.15,
                stroke_color=colors_6[col],
                stroke_width=2,
                fill_opacity=0.08,
                fill_color=colors_6[col]
            ).move_to(
                np.array([(col - 2.5) * 0.6, -3.25, 0])
            )
            rects.add(rect)

        self.play(FadeIn(rects), run_time=0.5)

        count_text = Text(
            "6 组！", font=FONT, font_size=30,
            color=COLOR_QUOTIENT, weight=BOLD
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(count_text, scale=1.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, mult_group, arrow, arrow_text,
                div_group, key, desc, apple_grid,
                rects, count_text
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 例题1 — 24 / 4 = 6
    # ------------------------------------------------------------------
    def scene_3_example_1(self):
        title = Text(
            "例题一", font=FONT, font_size=36,
            color=COLOR_DIVIDEND, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 除法算式
        problem = MathTex(
            r"24 \div 4 = \;?",
            font_size=48, color=WHITE
        ).move_to(UP * 3.8)
        self.play(Write(problem), run_time=0.7)

        # 第一步：找被除数和除数
        step1_text = Text(
            "第一步：找被除数和除数",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(UP * 2.5)
        self.play(Write(step1_text), run_time=0.5)

        # 标注被除数和除数
        brace_dividend = Brace(
            problem[0][:2], DOWN, buff=0.15, color=COLOR_DIVIDEND
        )
        label_dividend = Text(
            "被除数", font=FONT, font_size=18, color=COLOR_DIVIDEND
        ).next_to(brace_dividend, DOWN, buff=0.1)

        brace_divisor = Brace(
            problem[0][3], DOWN, buff=0.15, color=COLOR_DIVISOR
        )
        label_divisor = Text(
            "除数", font=FONT, font_size=18, color=COLOR_DIVISOR
        ).next_to(brace_divisor, DOWN, buff=0.1)

        self.play(
            FadeIn(brace_dividend), FadeIn(label_dividend),
            FadeIn(brace_divisor), FadeIn(label_divisor),
            run_time=0.6
        )
        self.wait(0.3)

        # 第二步：想口诀
        step2_text = Text(
            "第二步：想口诀",
            font=FONT, font_size=24, color=COLOR_HL
        ).move_to(UP * 0.5)
        self.play(
            Write(step2_text),
            FadeOut(VGroup(
                brace_dividend, label_dividend,
                brace_divisor, label_divisor
            )),
            run_time=0.5
        )

        # 思考框
        think_box = RoundedRectangle(
            width=7.5, height=2.8,
            corner_radius=0.25,
            fill_color="#1e293b", fill_opacity=0.95,
            stroke_color=COLOR_MULT, stroke_width=2
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(think_box), run_time=0.3)

        think_label = Text(
            "想：", font=FONT, font_size=28, color=COLOR_MULT
        ).move_to(think_box.get_top() + DOWN * 0.5 + LEFT * 2.5)

        # "几 x 4 = 24 ?"
        think_q = VGroup(
            MathTex(r"?", font_size=40, color=COLOR_QUOTIENT),
            MathTex(r"\times", font_size=34, color=WHITE),
            MathTex(r"4", font_size=40, color=COLOR_DIVISOR),
            MathTex(r"=", font_size=34, color=WHITE),
            MathTex(r"24", font_size=40, color=COLOR_DIVIDEND),
        ).arrange(RIGHT, buff=0.2).move_to(
            think_box.get_center() + UP * 0.1
        )

        self.play(FadeIn(think_label), run_time=0.3)
        self.play(Write(think_q), run_time=0.8)
        self.wait(0.5)

        # 口诀闪现
        rhyme = Text(
            "四六二十四", font=FONT, font_size=36,
            color=COLOR_MULT, weight=BOLD
        ).move_to(think_box.get_bottom() + UP * 0.6)
        self.play(FadeIn(rhyme, scale=1.3), run_time=0.6)
        self.play(
            Indicate(rhyme, scale_factor=1.1, color=COLOR_MULT),
            run_time=0.5
        )
        self.wait(0.3)

        # 第三步：得出答案
        step3_text = Text(
            "第三步：商就是 6 ！",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(DOWN * 3.8)
        self.play(Write(step3_text), run_time=0.5)

        # 最终答案
        answer = MathTex(
            r"24 \div 4 = 6",
            font_size=48, color=COLOR_HL
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(answer, shift=UP * 0.2), run_time=0.6)
        self.play(
            Indicate(answer, scale_factor=1.05, color=COLOR_HL),
            run_time=0.5
        )
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, problem, step1_text, step2_text,
                think_box, think_label, think_q, rhyme,
                step3_text, answer
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 4: 例题2 — 18 / 3 = 6
    # ------------------------------------------------------------------
    def scene_4_example_2(self):
        title = Text(
            "例题二", font=FONT, font_size=36,
            color=COLOR_DIVISOR, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        problem = MathTex(
            r"18 \div 3 = \;?",
            font_size=48, color=WHITE
        ).move_to(UP * 3.8)
        self.play(Write(problem), run_time=0.7)

        # 想口诀
        step_text = Text(
            "想口诀：几乘3等于18？",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 2.3)
        self.play(Write(step_text), run_time=0.6)

        # 思考过程
        think_box = RoundedRectangle(
            width=7.5, height=2.5,
            corner_radius=0.25,
            fill_color="#1e293b", fill_opacity=0.95,
            stroke_color=COLOR_MULT, stroke_width=2
        ).move_to(UP * 0.3)
        self.play(FadeIn(think_box), run_time=0.3)

        think_q = VGroup(
            MathTex(r"?", font_size=40, color=COLOR_QUOTIENT),
            MathTex(r"\times", font_size=34, color=WHITE),
            MathTex(r"3", font_size=40, color=COLOR_DIVISOR),
            MathTex(r"=", font_size=34, color=WHITE),
            MathTex(r"18", font_size=40, color=COLOR_DIVIDEND),
        ).arrange(RIGHT, buff=0.2).move_to(
            think_box.get_center() + UP * 0.3
        )
        self.play(Write(think_q), run_time=0.7)

        # 口诀
        rhyme = Text(
            "三六十八", font=FONT, font_size=36,
            color=COLOR_MULT, weight=BOLD
        ).move_to(think_box.get_center() + DOWN * 0.5)
        self.play(FadeIn(rhyme, scale=1.3), run_time=0.6)
        self.play(
            Indicate(rhyme, scale_factor=1.1, color=COLOR_MULT),
            run_time=0.5
        )
        self.wait(0.3)

        # 答案
        answer = MathTex(
            r"18 \div 3 = 6",
            font_size=48, color=COLOR_HL
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(answer, shift=UP * 0.2), run_time=0.6)
        self.play(
            Indicate(answer, scale_factor=1.05, color=COLOR_HL),
            run_time=0.5
        )
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(
                title, problem, step_text,
                think_box, think_q, rhyme, answer
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 5: 例题3 — 30 / 5 = 6
    # ------------------------------------------------------------------
    def scene_5_example_3(self):
        title = Text(
            "例题三", font=FONT, font_size=36,
            color=COLOR_QUOTIENT, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        problem = MathTex(
            r"30 \div 5 = \;?",
            font_size=48, color=WHITE
        ).move_to(UP * 3.8)
        self.play(Write(problem), run_time=0.7)

        step_text = Text(
            "想口诀：几乘5等于30？",
            font=FONT, font_size=26, color=COLOR_HL
        ).move_to(UP * 2.3)
        self.play(Write(step_text), run_time=0.6)

        # 思考过程
        think_box = RoundedRectangle(
            width=7.5, height=2.5,
            corner_radius=0.25,
            fill_color="#1e293b", fill_opacity=0.95,
            stroke_color=COLOR_MULT, stroke_width=2
        ).move_to(UP * 0.3)
        self.play(FadeIn(think_box), run_time=0.3)

        think_q = VGroup(
            MathTex(r"?", font_size=40, color=COLOR_QUOTIENT),
            MathTex(r"\times", font_size=34, color=WHITE),
            MathTex(r"5", font_size=40, color=COLOR_DIVISOR),
            MathTex(r"=", font_size=34, color=WHITE),
            MathTex(r"30", font_size=40, color=COLOR_DIVIDEND),
        ).arrange(RIGHT, buff=0.2).move_to(
            think_box.get_center() + UP * 0.3
        )
        self.play(Write(think_q), run_time=0.7)

        rhyme = Text(
            "五六三十", font=FONT, font_size=36,
            color=COLOR_MULT, weight=BOLD
        ).move_to(think_box.get_center() + DOWN * 0.5)
        self.play(FadeIn(rhyme, scale=1.3), run_time=0.6)
        self.play(
            Indicate(rhyme, scale_factor=1.1, color=COLOR_MULT),
            run_time=0.5
        )
        self.wait(0.3)

        answer = MathTex(
            r"30 \div 5 = 6",
            font_size=48, color=COLOR_HL
        ).move_to(DOWN * 2.0)
        self.play(FadeIn(answer, shift=UP * 0.2), run_time=0.6)
        self.play(
            Indicate(answer, scale_factor=1.05, color=COLOR_HL),
            run_time=0.5
        )
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(
                title, problem, step_text,
                think_box, think_q, rhyme, answer
            )),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 6: 方法总结
    # ------------------------------------------------------------------
    def scene_6_summary(self):
        box = RoundedRectangle(
            width=8.0, height=8.5,
            corner_radius=0.3,
            fill_color=COLOR_CARD, fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)
        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "用乘法口诀求商", font=FONT,
            font_size=32, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 4.2)
        self.play(Write(sum_title), run_time=0.5)

        subtitle = Text(
            "三步法", font=FONT,
            font_size=26, color=COLOR_RULE
        ).move_to(UP * 3.4)
        self.play(FadeIn(subtitle), run_time=0.3)

        # 三步
        steps = VGroup(
            Text(
                "1. 看：被除数和除数是多少",
                font=FONT, font_size=22, color=WHITE
            ),
            Text(
                "2. 想：几乘除数等于被除数",
                font=FONT, font_size=22, color=WHITE
            ),
            Text(
                "3. 答：那个几就是商",
                font=FONT, font_size=22, color=WHITE
            ),
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to(UP * 1.8)

        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.2)

        # 关键口诀
        key_box = RoundedRectangle(
            width=7.0, height=1.5,
            corner_radius=0.2,
            fill_color="#312e81", fill_opacity=0.8,
            stroke_color=COLOR_MULT, stroke_width=2
        ).move_to(DOWN * 0.3)
        self.play(FadeIn(key_box), run_time=0.3)

        key_text = Text(
            "口诀是乘法和除法的桥梁！",
            font=FONT, font_size=26, color=COLOR_MULT, weight=BOLD
        ).move_to(key_box.get_center())
        self.play(Write(key_text), run_time=0.6)

        # 示例对照
        example_title = Text(
            "乘除对照：", font=FONT, font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 1.8 + LEFT * 2.0)
        self.play(FadeIn(example_title), run_time=0.3)

        # 乘法 -> 除法 对照
        pair1 = VGroup(
            MathTex(r"4 \times 6 = 24", font_size=28, color=COLOR_MULT),
            MathTex(r"\Leftrightarrow", font_size=24, color=COLOR_HL),
            MathTex(r"24 \div 4 = 6", font_size=28, color=COLOR_DIVIDEND),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.6)

        pair2 = VGroup(
            MathTex(r"3 \times 6 = 18", font_size=28, color=COLOR_MULT),
            MathTex(r"\Leftrightarrow", font_size=24, color=COLOR_HL),
            MathTex(r"18 \div 3 = 6", font_size=28, color=COLOR_DIVIDEND),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.4)

        self.play(FadeIn(pair1), run_time=0.5)
        self.play(FadeIn(pair2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                box, sum_title, subtitle, steps,
                key_box, key_text, example_title,
                pair1, pair2
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 小练习
    # ------------------------------------------------------------------
    def scene_7_practice(self):
        title = Text(
            "试一试！", font=FONT, font_size=38,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 练习题目
        problems = [
            (r"12 \div 2 = \;?", "二六十二", r"12 \div 2 = 6"),
            (r"20 \div 4 = \;?", "四五二十", r"20 \div 4 = 5"),
            (r"15 \div 3 = \;?", "三五十五", r"15 \div 3 = 5"),
        ]

        y_positions = [UP * 3.5, UP * 0.8, DOWN * 1.9]

        all_elements = VGroup()

        for i, (prob_tex, rhyme_str, ans_tex) in enumerate(problems):
            y = y_positions[i]

            # 题号
            num_label = Text(
                f"{i + 1}.", font=FONT, font_size=26,
                color=GRAY_A
            ).move_to(y + LEFT * 3.5)
            all_elements.add(num_label)

            # 题目
            prob = MathTex(prob_tex, font_size=40, color=WHITE)
            prob.move_to(y)
            all_elements.add(prob)

            self.play(FadeIn(num_label), Write(prob), run_time=0.6)
            self.wait(0.5)

            # 想口诀
            rhyme = Text(
                rhyme_str, font=FONT, font_size=28,
                color=COLOR_MULT
            ).move_to(y + DOWN * 0.8)
            all_elements.add(rhyme)
            self.play(FadeIn(rhyme, scale=1.2), run_time=0.5)

            # 答案
            ans = MathTex(ans_tex, font_size=40, color=COLOR_HL)
            ans.move_to(y + DOWN * 1.6)
            all_elements.add(ans)
            self.play(
                FadeIn(ans, shift=UP * 0.2), run_time=0.5
            )
            self.wait(0.3)

        # 鼓励
        cheer = Text(
            "你答对了吗？", font=FONT, font_size=32,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 5.5)
        all_elements.add(cheer)
        self.play(FadeIn(cheer, scale=1.1), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, all_elements)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------
    def scene_8_outro(self):
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


# ======================================================================
# 渲染命令:
#   快速预览:  manim -pql 004_用乘法口诀求商.py MultiplicationTableDivisionLesson
#   中等质量:  manim -qm  004_用乘法口诀求商.py MultiplicationTableDivisionLesson
#   高质量:    manim -qh  004_用乘法口诀求商.py MultiplicationTableDivisionLesson
# ======================================================================
