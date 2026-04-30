"""
有关0的加减法 - Manim 教学动画
一年级上册 · 第二章 · 10以内数的加减法

知识点:
  - a + 0 = a  （加上0，还得这个数）
  - a - 0 = a  （减去0，还得这个数）
  - a - a = 0  （两个相同的数相减等于0）

格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ===== 全局配置 =====
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


class ZeroAddSubtract(Scene):
    """有关0的加减法教学动画"""

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色主题
        self.C_APPLE = "#e74c3c"
        self.C_ZERO_BOX = "#7f8c8d"
        self.C_RESULT = "#2ecc71"
        self.C_FORMULA = "#f1c40f"
        self.C_RULE = "#3498db"
        self.C_HIGHLIGHT = "#e67e22"
        self.C_TITLE = "#ecf0f1"

        # 苹果参数
        self.APPLE_R = 0.35
        self.APPLE_SPACING = 0.9

        # 执行场景
        self.scene_1_hook()
        self.scene_2_plus_zero()
        self.scene_3_minus_zero()
        self.scene_4_minus_self()
        self.scene_5_summary()
        self.scene_6_outro()

    # ==========================================
    # 工具函数
    # ==========================================

    def make_apples(self, n, y=0.0, color=None, fill_opacity=0.9):
        """创建 n 个苹果圆圈，水平居中排列"""
        if color is None:
            color = self.C_APPLE
        r = self.APPLE_R
        sp = self.APPLE_SPACING
        total_w = (n - 1) * sp + 2 * r
        x_start = -total_w / 2 + r
        group = VGroup()
        for i in range(n):
            x = x_start + i * sp
            circle = Circle(
                radius=r,
                color=color,
                fill_color=color,
                fill_opacity=fill_opacity,
                stroke_width=2,
            ).move_to(np.array([x, y, 0]))
            group.add(circle)
        return group

    def make_empty_plate(self, y=0.0):
        """创建空盘子（虚线圆圈）代表0个"""
        plate = DashedVMobject(
            Circle(radius=self.APPLE_R * 1.3, color=self.C_ZERO_BOX, stroke_width=2),
            num_dashes=12,
        ).move_to(np.array([0, y, 0]))
        return plate

    def make_zero_label(self, y=0.0):
        """在空盘子下方标注'0'"""
        zero = MathTex(r"0", color=self.C_ZERO_BOX, font_size=32).move_to(
            np.array([0, y - self.APPLE_R * 1.3 - 0.3, 0])
        )
        return zero

    def make_formula_row(self, left_text, mid_tex, right_text, y=-2.5, font_size=44):
        """
        构建公式行: Text + MathTex 混排
        left_text: 左侧中文 (Text)
        mid_tex: 中间 LaTeX (MathTex)
        right_text: 右侧中文 (Text) 或 None
        """
        parts = []
        if left_text:
            parts.append(
                Text(left_text, font="PingFang SC", font_size=font_size, color=self.C_FORMULA)
            )
        parts.append(
            MathTex(mid_tex, color=self.C_FORMULA, font_size=font_size)
        )
        if right_text:
            parts.append(
                Text(right_text, font="PingFang SC", font_size=font_size, color=self.C_FORMULA)
            )
        row = VGroup(*parts).arrange(RIGHT, buff=0.15)
        row.move_to(np.array([0, y, 0]))
        return row

    def make_rule_text(self, line1, line2=None, y=-4.5):
        """创建规律说明文字（两行）"""
        t1 = Text(line1, font="PingFang SC", font_size=26, color=self.C_RULE)
        group = VGroup(t1)
        if line2:
            t2 = Text(line2, font="PingFang SC", font_size=26, color=self.C_RULE)
            group.add(t2)
        group.arrange(DOWN, buff=0.2)
        group.move_to(np.array([0, y, 0]))
        return group

    def make_scene_title(self, text, y=5.5):
        """创建场景标题"""
        return Text(
            text,
            font="PingFang SC",
            font_size=38,
            color=self.C_TITLE,
        ).move_to(np.array([0, y, 0]))

    # ==========================================
    # Scene 1: 开场钩子
    # ==========================================

    def scene_1_hook(self):
        # 作者信息（全程显示）
        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=20,
            color=GRAY_B,
        ).move_to(UP * 7)
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.3)

        # 钩子大问题
        question_zh = Text(
            "5个苹果", font="PingFang SC", font_size=52, color=self.C_APPLE
        )
        question_op = MathTex(r"+\ 0\ =\ ?", color=self.C_FORMULA, font_size=52)
        hook = VGroup(question_zh, question_op).arrange(RIGHT, buff=0.2)
        hook.move_to(UP * 4.5)

        self.play(Write(hook), run_time=1.2)

        # 动画：5个苹果闪现
        demo_apples = self.make_apples(5, y=2.5)
        self.play(
            LaggedStart(*[GrowFromCenter(a) for a in demo_apples], lag_ratio=0.15),
            run_time=1.2,
        )

        # 问号脉动
        q_mark = MathTex(r"?", color=YELLOW, font_size=120).move_to(ORIGIN)
        self.play(FadeIn(q_mark, scale=0.5), run_time=0.5)
        self.play(q_mark.animate.scale(1.3), run_time=0.3)
        self.play(q_mark.animate.scale(1 / 1.3), run_time=0.3)
        self.wait(0.5)

        # 清场
        self.play(
            FadeOut(hook),
            FadeOut(demo_apples),
            FadeOut(q_mark),
            run_time=0.5,
        )

    # ==========================================
    # Scene 2: a + 0 = a
    # ==========================================

    def scene_2_plus_zero(self):
        # 标题
        title = self.make_scene_title("加上 0")
        self.play(Write(title), run_time=0.6)

        # 第一行：5个苹果
        label_left = Text(
            "盘子里有", font="PingFang SC", font_size=28, color=GRAY_A
        ).move_to(np.array([-2.2, 4.2, 0]))
        count_left = MathTex(r"5", color=self.C_APPLE, font_size=36).next_to(
            label_left, RIGHT, buff=0.15
        )
        label_left2 = Text(
            "个苹果", font="PingFang SC", font_size=28, color=GRAY_A
        ).next_to(count_left, RIGHT, buff=0.15)
        row_label = VGroup(label_left, count_left, label_left2)
        self.play(FadeIn(row_label), run_time=0.5)

        apples = self.make_apples(5, y=2.8)
        self.play(
            LaggedStart(*[GrowFromCenter(a) for a in apples], lag_ratio=0.18),
            run_time=1.0,
        )

        # 加号
        plus_sign = MathTex(r"+", color=WHITE, font_size=60).move_to(np.array([0, 1.2, 0]))
        self.play(Write(plus_sign), run_time=0.4)

        # 第二行：空盘子（0个）
        label_right = Text(
            "又加了", font="PingFang SC", font_size=28, color=GRAY_A
        ).move_to(np.array([-2.5, 0.4, 0]))
        count_zero = MathTex(r"0", color=self.C_ZERO_BOX, font_size=36).next_to(
            label_right, RIGHT, buff=0.15
        )
        label_right2 = Text(
            "个苹果", font="PingFang SC", font_size=28, color=GRAY_A
        ).next_to(count_zero, RIGHT, buff=0.15)
        row_label2 = VGroup(label_right, count_zero, label_right2)
        self.play(FadeIn(row_label2), run_time=0.5)

        # 空盘子动画
        empty_plate = self.make_empty_plate(y=-0.5)
        empty_text = Text(
            "空空的~", font="PingFang SC", font_size=22, color=self.C_ZERO_BOX
        ).move_to(np.array([0, -1.0, 0]))
        self.play(Create(empty_plate), run_time=0.8)
        self.play(FadeIn(empty_text), run_time=0.4)
        self.wait(0.5)

        # 等号后：结果5个苹果
        equals_sign = MathTex(r"=", color=WHITE, font_size=60).move_to(np.array([0, -2.0, 0]))
        self.play(Write(equals_sign), run_time=0.4)
        self.play(FadeOut(empty_text), run_time=0.2)

        # 结果苹果行
        result_apples = self.make_apples(5, y=-2.9, color=self.C_RESULT)
        self.play(
            LaggedStart(*[GrowFromCenter(a) for a in result_apples], lag_ratio=0.15),
            run_time=1.0,
        )

        # 公式
        formula = MathTex(r"5 + 0 = 5", color=self.C_FORMULA, font_size=48).move_to(
            np.array([0, -4.0, 0])
        )
        self.play(Write(formula), run_time=0.8)

        # 高亮5不变
        self.play(Indicate(result_apples, color=YELLOW, scale_factor=1.1), run_time=0.8)

        # 规律文字
        rule = self.make_rule_text("加上 0，还得原来的数！", y=-5.3)
        self.play(FadeIn(rule, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(title), FadeOut(row_label), FadeOut(apples),
            FadeOut(plus_sign), FadeOut(row_label2), FadeOut(empty_plate),
            FadeOut(equals_sign), FadeOut(result_apples), FadeOut(formula),
            FadeOut(rule),
            run_time=0.6,
        )

    # ==========================================
    # Scene 3: a - 0 = a
    # ==========================================

    def scene_3_minus_zero(self):
        title = self.make_scene_title("减去 0")
        self.play(Write(title), run_time=0.6)

        # 说明文字
        desc = Text(
            "盘子里有5个苹果",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A,
        ).move_to(np.array([0, 4.3, 0]))
        self.play(FadeIn(desc), run_time=0.4)

        apples = self.make_apples(5, y=2.8)
        self.play(
            LaggedStart(*[GrowFromCenter(a) for a in apples], lag_ratio=0.18),
            run_time=1.0,
        )

        # 减去0
        minus_sign = MathTex(r"-", color=WHITE, font_size=60).move_to(np.array([0, 1.3, 0]))
        self.play(Write(minus_sign), run_time=0.4)

        desc2 = Text(
            "拿走了 0 个（什么都没拿）",
            font="PingFang SC",
            font_size=26,
            color=GRAY_A,
        ).move_to(np.array([0, 0.4, 0]))
        self.play(FadeIn(desc2), run_time=0.5)

        empty_plate = self.make_empty_plate(y=-0.6)
        self.play(Create(empty_plate), run_time=0.8)

        # 强调"什么都没少"
        nothing_text = Text(
            "苹果没有减少！",
            font="PingFang SC",
            font_size=30,
            color=YELLOW,
        ).move_to(np.array([0, -1.5, 0]))
        self.play(FadeIn(nothing_text, scale=0.8), run_time=0.5)

        # 等号 + 结果
        equals_sign = MathTex(r"=", color=WHITE, font_size=60).move_to(np.array([0, -2.3, 0]))
        self.play(Write(equals_sign), run_time=0.4)
        self.play(FadeOut(nothing_text), run_time=0.2)

        result_apples = self.make_apples(5, y=-3.1, color=self.C_RESULT)
        self.play(
            LaggedStart(*[GrowFromCenter(a) for a in result_apples], lag_ratio=0.15),
            run_time=1.0,
        )

        formula = MathTex(r"5 - 0 = 5", color=self.C_FORMULA, font_size=48).move_to(
            np.array([0, -4.0, 0])
        )
        self.play(Write(formula), run_time=0.8)

        rule = self.make_rule_text("减去 0，还得原来的数！", y=-5.3)
        self.play(FadeIn(rule, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(desc), FadeOut(apples),
            FadeOut(minus_sign), FadeOut(desc2), FadeOut(empty_plate),
            FadeOut(equals_sign), FadeOut(result_apples), FadeOut(formula),
            FadeOut(rule),
            run_time=0.6,
        )

    # ==========================================
    # Scene 4: a - a = 0
    # ==========================================

    def scene_4_minus_self(self):
        title = self.make_scene_title("全部拿走")
        self.play(Write(title), run_time=0.6)

        desc = Text(
            "盘子里有5个苹果",
            font="PingFang SC",
            font_size=28,
            color=GRAY_A,
        ).move_to(np.array([0, 4.3, 0]))
        self.play(FadeIn(desc), run_time=0.4)

        apples = self.make_apples(5, y=2.8)
        self.play(
            LaggedStart(*[GrowFromCenter(a) for a in apples], lag_ratio=0.18),
            run_time=1.0,
        )

        minus_sign = MathTex(r"-", color=WHITE, font_size=60).move_to(np.array([0, 1.3, 0]))
        self.play(Write(minus_sign), run_time=0.4)

        desc2 = Text(
            "拿走了全部 5 个！",
            font="PingFang SC",
            font_size=28,
            color=self.C_HIGHLIGHT,
        ).move_to(np.array([0, 0.5, 0]))
        self.play(FadeIn(desc2), run_time=0.5)

        # 被减的苹果（深色）
        sub_apples = self.make_apples(5, y=-0.5, color="#c0392b", fill_opacity=0.5)
        self.play(
            LaggedStart(*[GrowFromCenter(a) for a in sub_apples], lag_ratio=0.15),
            run_time=0.8,
        )

        # 动画：苹果消失
        crosses = VGroup(
            *[
                Cross(stroke_color=RED, stroke_width=3).move_to(a.get_center()).scale(0.6)
                for a in sub_apples
            ]
        )
        self.play(
            LaggedStart(*[Create(c) for c in crosses], lag_ratio=0.1),
            run_time=0.8,
        )
        self.play(
            FadeOut(sub_apples),
            FadeOut(crosses),
            apples.animate.set_opacity(0.2),
            run_time=0.8,
        )

        # 等号 + 结果0
        equals_sign = MathTex(r"=", color=WHITE, font_size=60).move_to(np.array([0, -1.8, 0]))
        self.play(Write(equals_sign), run_time=0.4)

        empty_result = self.make_empty_plate(y=-2.9)
        zero_label = MathTex(r"0", color=self.C_RESULT, font_size=80).move_to(
            np.array([0, -2.9, 0])
        )
        self.play(Create(empty_result), run_time=0.6)
        self.play(Write(zero_label), run_time=0.5)
        self.play(Flash(zero_label, color=YELLOW, flash_radius=0.6), run_time=0.5)

        formula = MathTex(r"5 - 5 = 0", color=self.C_FORMULA, font_size=48).move_to(
            np.array([0, -4.0, 0])
        )
        self.play(Write(formula), run_time=0.8)

        rule = self.make_rule_text("相同的数相减，等于 0！", y=-5.3)
        self.play(FadeIn(rule, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(desc), FadeOut(apples),
            FadeOut(minus_sign), FadeOut(desc2), FadeOut(empty_result),
            FadeOut(zero_label), FadeOut(equals_sign), FadeOut(formula),
            FadeOut(rule),
            run_time=0.6,
        )

    # ==========================================
    # Scene 5: 规律总结
    # ==========================================

    def scene_5_summary(self):
        title = Text(
            "三条规律，记住了吗？",
            font="PingFang SC",
            font_size=34,
            color=YELLOW,
        ).move_to(UP * 5.8)
        self.play(Write(title), run_time=0.8)

        # 卡片1: a+0=a
        def make_card(rule_text, formula_tex, example_tex, color, y):
            bg = RoundedRectangle(
                corner_radius=0.2,
                width=7.5,
                height=1.6,
                fill_color=color,
                fill_opacity=0.15,
                stroke_color=color,
                stroke_width=2,
            ).move_to(np.array([0, y, 0]))
            rule = Text(
                rule_text, font="PingFang SC", font_size=26, color=color
            ).move_to(np.array([-1.8, y + 0.3, 0]))
            formula = MathTex(formula_tex, color=WHITE, font_size=34).move_to(
                np.array([1.5, y + 0.3, 0])
            )
            example = MathTex(example_tex, color=GRAY_A, font_size=24).move_to(
                np.array([0, y - 0.35, 0])
            )
            return VGroup(bg, rule, formula, example)

        card1 = make_card(
            "加0不变", r"a + 0 = a", r"5+0=5,\ \ 3+0=3",
            self.C_RESULT, 3.5
        )
        card2 = make_card(
            "减0不变", r"a - 0 = a", r"5-0=5,\ \ 7-0=7",
            self.C_RULE, 1.5
        )
        card3 = make_card(
            "自减为零", r"a - a = 0", r"5-5=0,\ \ 8-8=0",
            self.C_HIGHLIGHT, -0.5
        )

        for card in [card1, card2, card3]:
            self.play(FadeIn(card, shift=RIGHT * 0.4), run_time=0.6)
            self.wait(0.3)

        # 总结口诀
        slogan_1 = Text(
            "加0或减0，", font="PingFang SC", font_size=30, color=WHITE
        )
        slogan_2 = Text(
            "原来是几就是几！", font="PingFang SC", font_size=30, color=YELLOW
        )
        slogan = VGroup(slogan_1, slogan_2).arrange(RIGHT, buff=0.1)
        slogan.move_to(np.array([0, -2.3, 0]))

        slogan_3 = Text(
            "相同数相减，结果是零！",
            font="PingFang SC",
            font_size=30,
            color=self.C_HIGHLIGHT,
        ).move_to(np.array([0, -3.3, 0]))

        self.play(FadeIn(slogan, shift=UP * 0.3), run_time=0.6)
        self.play(FadeIn(slogan_3, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(card1), FadeOut(card2), FadeOut(card3),
            FadeOut(slogan), FadeOut(slogan_3),
            run_time=0.6,
        )

    # ==========================================
    # Scene 6: 片尾
    # ==========================================

    def scene_6_outro(self):
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE,
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=GRAY_B,
        ).move_to(UP * 1.0)

        self.play(
            Transform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=self.C_FORMULA,
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)

        # 装饰：三个公式快闪
        mini_formulas = VGroup(
            MathTex(r"a+0=a", color=self.C_RESULT, font_size=28),
            MathTex(r"a-0=a", color=self.C_RULE, font_size=28),
            MathTex(r"a-a=0", color=self.C_HIGHLIGHT, font_size=28),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 2.2)

        self.play(
            LaggedStart(*[FadeIn(f, scale=0.8) for f in mini_formulas], lag_ratio=0.3),
            run_time=1.0,
        )
        self.wait(1.0)

        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(mini_formulas),
            run_time=1.0,
        )


# ===== 运行命令 =====
# 快速预览:  manim -pql zero_addition_subtraction.py ZeroAddSubtract
# 高质量:    manim -qh  zero_addition_subtraction.py ZeroAddSubtract
# 4K生产:    manim -qk  zero_addition_subtraction.py ZeroAddSubtract