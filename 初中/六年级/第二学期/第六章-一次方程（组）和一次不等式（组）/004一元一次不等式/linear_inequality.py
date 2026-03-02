"""
一元一次不等式 - Linear Inequality in One Variable
六年级数学教学动画

内容: 定义、三条性质（含翻转警告）、解法、数轴表示
目标观众: 六年级学生
格式: TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ============================================================
# 全局配置
# ============================================================
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ============================================================
# 颜色常量
# ============================================================
BG_COLOR   = "#1a1a2e"
COLOR_X    = "#e74c3c"    # 红色  - 未知数
COLOR_POS  = "#3498db"    # 蓝色  - 正数乘除（不变）
COLOR_NEG  = "#e67e22"    # 橙色  - 负数乘除
COLOR_OK   = "#2ecc71"    # 绿色  - 不等号不变
COLOR_FLIP = "#e74c3c"    # 红色  - 不等号翻转
COLOR_CARD = "#16213e"    # 深蓝  - 卡片背景
COLOR_NUM  = "#95a5a6"    # 灰色  - 数轴
COLOR_SOL  = "#3498db"    # 蓝色  - 解集
FONT       = "Noto Sans CJK SC"


# ============================================================
# 辅助：带圆角背景的卡片
# ============================================================
def card_bg(mob, fill=COLOR_CARD, stroke=WHITE, buff=0.22, r=0.14):
    return SurroundingRectangle(
        mob, fill_color=fill, fill_opacity=0.88,
        stroke_color=stroke, stroke_width=2,
        buff=buff, corner_radius=r
    )


# ============================================================
# 主场景
# ============================================================
class LinearInequality(Scene):
    """
    一元一次不等式教学动画

    场景:
      1. 开场钩子
      2. 不等式 vs 等式
      3. 一元一次不等式定义
      4. 性质一：加减（不变）
      5. 性质二：乘除正数（不变）
      6. 性质三：乘除负数（翻转！）⭐
      7. 解不等式示例 + 数轴
      8. 总结
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=GRAY_B
        ).move_to(UP * 7.3)
        self.add(self.author)

        self.scene_hook()
        self.scene_inequality_intro()
        self.scene_definition()
        self.scene_prop1_add()
        self.scene_prop2_mul_pos()
        self.scene_prop3_mul_neg()
        self.scene_solve_example()
        self.scene_summary()
        self.scene_outro()

    # ----------------------------------------------------------
    # Scene 1: 开场钩子
    # ----------------------------------------------------------
    def scene_hook(self):
        hook = Text(
            "不等式里藏着一个大秘密…",
            font=FONT, font_size=33, color=YELLOW
        ).move_to(UP * 5.8)

        # 提问
        q1 = Text("已知 x > 3", font=FONT, font_size=30, color=WHITE).move_to(UP * 4.5)
        q2 = VGroup(
            Text("两边同乘", font=FONT, font_size=30, color=WHITE),
            MathTex(r"(-1)", font_size=38, color=COLOR_NEG),
            Text("会怎样？", font=FONT, font_size=30, color=WHITE),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.6)

        # 假设学生可能犯的错误 vs 正确答案
        wrong_ans = VGroup(
            Text("以为：", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"-x > -3", font_size=38, color=GRAY_A),
            MathTex(r"\times", font_size=30, color=COLOR_FLIP),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 2.4)

        right_ans = VGroup(
            Text("正确：", font=FONT, font_size=24, color=COLOR_OK),
            MathTex(r"-x < -3", font_size=38, color=COLOR_OK),
            MathTex(r"\checkmark", font_size=30, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 1.5)

        exclaim = Text(
            "不等号方向变了！",
            font=FONT, font_size=30, color=COLOR_FLIP
        ).move_to(UP * 0.4)
        exclaim_bg = card_bg(exclaim, fill="#3a0000", stroke=COLOR_FLIP, buff=0.18)

        self.play(Write(hook), run_time=0.7)
        self.play(FadeIn(q1, shift=UP * 0.2), FadeIn(q2, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(wrong_ans), run_time=0.5)
        self.play(FadeIn(right_ans), run_time=0.5)
        self.play(Create(exclaim_bg), Write(exclaim), run_time=0.6)
        self.play(Indicate(exclaim, scale_factor=1.08, color=YELLOW), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(hook), FadeOut(q1), FadeOut(q2),
            FadeOut(wrong_ans), FadeOut(right_ans),
            FadeOut(exclaim_bg), FadeOut(exclaim),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 2: 不等式 vs 等式
    # ----------------------------------------------------------
    def scene_inequality_intro(self):
        title = Text("不等式 vs 等式", font=FONT, font_size=34, color=GOLD).move_to(UP * 6.2)

        # 等式行
        row_eq = VGroup(
            Text("等式：", font=FONT, font_size=26, color=GRAY_A),
            MathTex(r"a = b", font_size=46),
            Text("（左边 = 右边）", font=FONT, font_size=22, color=GRAY_A),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 5.0)

        # 不等式行
        row_ineq = VGroup(
            Text("不等式：", font=FONT, font_size=26, color=WHITE),
            MathTex(r"a > b", font_size=40, color=COLOR_X),
            Text("或", font=FONT, font_size=28, color=GRAY_A),
            MathTex(r"a < b", font_size=40, color=COLOR_X),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 3.9)

        # 不等号图鉴
        ineq_title = Text("不等号一览", font=FONT, font_size=24, color=GOLD).move_to(UP * 2.8)
        signs = VGroup(
            VGroup(MathTex(r">", font_size=48, color=COLOR_OK),
                   Text("大于", font=FONT, font_size=20, color=GRAY_A)).arrange(DOWN, buff=0.1),
            VGroup(MathTex(r"<", font_size=48, color=COLOR_OK),
                   Text("小于", font=FONT, font_size=20, color=GRAY_A)).arrange(DOWN, buff=0.1),
            VGroup(MathTex(r"\geq", font_size=48, color=COLOR_POS),
                   Text("大于等于", font=FONT, font_size=18, color=GRAY_A)).arrange(DOWN, buff=0.1),
            VGroup(MathTex(r"\leq", font_size=48, color=COLOR_POS),
                   Text("小于等于", font=FONT, font_size=18, color=GRAY_A)).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=0.7).move_to(UP * 1.7)
        signs_bg = card_bg(signs, fill="#0d1f3a", stroke=COLOR_POS, buff=0.28)

        key = Text(
            "不等式中含有不等号，两边大小关系不同",
            font=FONT, font_size=22, color=GRAY_A
        ).move_to(UP * 0.3)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(row_eq), run_time=0.5)
        self.play(FadeIn(row_ineq), run_time=0.5)
        self.play(FadeIn(ineq_title), Create(signs_bg), FadeIn(signs), run_time=0.7)
        self.play(FadeIn(key), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(row_eq), FadeOut(row_ineq),
            FadeOut(ineq_title), FadeOut(signs_bg), FadeOut(signs),
            FadeOut(key),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 3: 定义
    # ----------------------------------------------------------
    def scene_definition(self):
        title = Text("一元一次不等式", font=FONT, font_size=38, color=GOLD).move_to(UP * 6.3)
        uline = Line(
            title.get_left() + DOWN * 0.05,
            title.get_right() + DOWN * 0.05,
            color=GOLD, stroke_width=2
        )

        self.play(Write(title), Create(uline), run_time=0.6)

        # --- 要素一 ---
        tag1  = Text("「一元」", font=FONT, font_size=28, color=COLOR_X).move_to(UP * 5.1 + LEFT * 1.6)
        desc1 = Text("只含一个未知数", font=FONT, font_size=24, color=WHITE).move_to(UP * 5.1 + RIGHT * 1.2)
        sep1  = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_D, stroke_width=1).move_to(UP * 4.5)

        self.play(FadeIn(tag1, shift=RIGHT * 0.3), FadeIn(desc1), run_time=0.5)
        self.play(Create(sep1), run_time=0.3)

        # --- 要素二 ---
        tag2  = Text("「一次」", font=FONT, font_size=28, color=COLOR_POS).move_to(UP * 3.9 + LEFT * 1.6)
        desc2 = Text("未知数的次数是 1", font=FONT, font_size=24, color=WHITE).move_to(UP * 3.9 + RIGHT * 1.2)
        sep2  = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_D, stroke_width=1).move_to(UP * 3.3)

        self.play(FadeIn(tag2, shift=RIGHT * 0.3), FadeIn(desc2), run_time=0.5)
        self.play(Create(sep2), run_time=0.3)

        # --- 要素三 ---
        tag3  = Text("「不等式」", font=FONT, font_size=28, color=COLOR_NEG).move_to(UP * 2.7 + LEFT * 1.6)
        desc3 = Text("含有不等号", font=FONT, font_size=24, color=WHITE).move_to(UP * 2.7 + RIGHT * 1.2)

        self.play(FadeIn(tag3, shift=RIGHT * 0.3), FadeIn(desc3), run_time=0.5)
        self.wait(0.4)

        # --- 标准形式 ---
        std_label = Text("标准形式：", font=FONT, font_size=24, color=GRAY_A).move_to(UP * 1.6 + LEFT * 1.2)
        std_form  = MathTex(
            r"ax + b > 0 \quad (a \neq 0)",
            font_size=38
        ).move_to(UP * 1.6 + RIGHT * 1.0)
        std_form[0][0].set_color(COLOR_POS)   # a
        std_form[0][1].set_color(COLOR_X)      # x
        std_form[0][3].set_color(COLOR_NEG)    # b

        # --- 例子 ---
        examples = VGroup(
            MathTex(r"2x - 3 > 0", font_size=34, color=GRAY_A),
            MathTex(r"x + 1 < 5", font_size=34, color=GRAY_A),
            MathTex(r"-x \geq 2", font_size=34, color=GRAY_A),
        ).arrange(RIGHT, buff=0.6).move_to(UP * 0.4)
        examples[0][0][0].set_color(COLOR_X)
        examples[1][0][0].set_color(COLOR_X)
        examples[2][0][1].set_color(COLOR_X)

        ex_label = Text("举例：", font=FONT, font_size=22, color=GRAY_A).next_to(examples, LEFT, buff=0.3)
        ex_bg = card_bg(examples, fill="#0a1628", stroke=COLOR_POS, buff=0.22)

        self.play(FadeIn(std_label), Write(std_form), run_time=0.7)
        self.play(Create(ex_bg), FadeIn(ex_label), FadeIn(examples), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(uline),
            FadeOut(tag1), FadeOut(desc1), FadeOut(sep1),
            FadeOut(tag2), FadeOut(desc2), FadeOut(sep2),
            FadeOut(tag3), FadeOut(desc3),
            FadeOut(std_label), FadeOut(std_form),
            FadeOut(ex_bg), FadeOut(ex_label), FadeOut(examples),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 4: 性质一 — 加减（不等号不变）
    # ----------------------------------------------------------
    def scene_prop1_add(self):
        title = Text("性质一：加减法", font=FONT, font_size=32, color=COLOR_OK).move_to(UP * 6.3)
        sub   = Text("两边同加减同一个数，不等号不变", font=FONT, font_size=22, color=GRAY_A).move_to(UP * 5.6)

        self.play(Write(title), FadeIn(sub), run_time=0.6)

        # 初始不等式
        init_ineq = MathTex(r"a > b", font_size=56).move_to(UP * 4.5)
        self.play(Write(init_ineq), run_time=0.5)
        self.wait(0.3)

        # ---- 加法 ----
        add_label = VGroup(
            Text("两边同加", font=FONT, font_size=24, color=WHITE),
            MathTex(r"c", font_size=32, color=COLOR_POS),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.5)
        add_arrow = MathTex(r"\Downarrow", font_size=38, color=COLOR_POS).move_to(UP * 2.9)
        add_result = MathTex(r"a+{{c}} > b+{{c}}", font_size=52).move_to(UP * 2.2)
        add_result.set_color_by_tex("c", COLOR_POS)

        add_ok = VGroup(
            MathTex(r"\checkmark", font_size=36, color=COLOR_OK),
            Text("不等号方向不变", font=FONT, font_size=24, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 1.3)
        add_ok_bg = card_bg(add_ok, fill="#001a08", stroke=COLOR_OK, buff=0.18)

        self.play(FadeIn(add_label), FadeIn(add_arrow), run_time=0.4)
        self.play(Write(add_result), run_time=0.6)
        self.play(Create(add_ok_bg), FadeIn(add_ok), run_time=0.5)
        self.wait(0.5)

        # ---- 减法 ----
        sep = Line(LEFT * 3.6, RIGHT * 3.6, color=GRAY_D, stroke_width=1.2).move_to(UP * 0.5)
        self.play(Create(sep), run_time=0.3)

        sub_label = VGroup(
            Text("两边同减", font=FONT, font_size=24, color=WHITE),
            MathTex(r"c", font_size=32, color=COLOR_POS),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 0.2)
        sub_arrow  = MathTex(r"\Downarrow", font_size=38, color=COLOR_POS).move_to(DOWN * 0.8)
        sub_result = MathTex(r"a-{{c}} > b-{{c}}", font_size=52).move_to(DOWN * 1.5)
        sub_result.set_color_by_tex("c", COLOR_POS)

        sub_ok = VGroup(
            MathTex(r"\checkmark", font_size=36, color=COLOR_OK),
            Text("不等号方向不变", font=FONT, font_size=24, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 2.5)
        sub_ok_bg = card_bg(sub_ok, fill="#001a08", stroke=COLOR_OK, buff=0.18)

        self.play(FadeIn(sub_label), FadeIn(sub_arrow), run_time=0.4)
        self.play(Write(sub_result), run_time=0.6)
        self.play(Create(sub_ok_bg), FadeIn(sub_ok), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(init_ineq),
            FadeOut(add_label), FadeOut(add_arrow), FadeOut(add_result),
            FadeOut(add_ok_bg), FadeOut(add_ok),
            FadeOut(sep),
            FadeOut(sub_label), FadeOut(sub_arrow), FadeOut(sub_result),
            FadeOut(sub_ok_bg), FadeOut(sub_ok),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 5: 性质二 — 乘除正数（不等号不变）
    # ----------------------------------------------------------
    def scene_prop2_mul_pos(self):
        title = Text("性质二：乘除正数", font=FONT, font_size=32, color=COLOR_POS).move_to(UP * 6.3)
        sub   = Text("两边同乘除正数，不等号不变", font=FONT, font_size=22, color=GRAY_A).move_to(UP * 5.6)

        self.play(Write(title), FadeIn(sub), run_time=0.5)

        init = MathTex(r"a > b", font_size=56).move_to(UP * 4.6)
        cond = VGroup(
            Text("其中", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"c > 0", font_size=36, color=COLOR_POS),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 3.8)

        self.play(Write(init), FadeIn(cond), run_time=0.6)

        arrow = MathTex(r"\Downarrow", font_size=42, color=COLOR_POS).move_to(UP * 3.0)
        op_label = VGroup(
            Text("两边", font=FONT, font_size=24, color=WHITE),
            MathTex(r"\times c", font_size=34, color=COLOR_POS),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 2.3)

        result = MathTex(r"ac > bc", font_size=58).move_to(UP * 1.3)
        result[0][0].set_color(COLOR_POS)
        result[0][2].set_color(COLOR_POS)

        ok = VGroup(
            MathTex(r"\checkmark", font_size=40, color=COLOR_OK),
            Text("不等号方向不变", font=FONT, font_size=26, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 0.1)
        ok_bg = card_bg(ok, fill="#001a08", stroke=COLOR_OK, buff=0.22)

        # 数字演示
        demo = VGroup(
            Text("例：3 > 2，×3 后 →", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"9 > 6 \;\checkmark", font_size=36, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 1.0)

        self.play(FadeIn(arrow), FadeIn(op_label), run_time=0.4)
        self.play(Write(result), run_time=0.6)
        self.play(Create(ok_bg), FadeIn(ok), run_time=0.5)
        self.play(FadeIn(demo), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(init), FadeOut(cond),
            FadeOut(arrow), FadeOut(op_label), FadeOut(result),
            FadeOut(ok_bg), FadeOut(ok), FadeOut(demo),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 6: 性质三 — 乘除负数（不等号翻转！）⭐
    # ----------------------------------------------------------
    def scene_prop3_mul_neg(self):
        title = Text("性质三：乘除负数", font=FONT, font_size=32, color=COLOR_NEG).move_to(UP * 6.3)
        sub   = VGroup(
            Text("两边同乘除负数，不等号", font=FONT, font_size=22, color=WHITE),
            Text("方向要改变！", font=FONT, font_size=22, color=COLOR_FLIP),
        ).arrange(RIGHT, buff=0.1).move_to(UP * 5.6)

        self.play(Write(title), FadeIn(sub), run_time=0.5)

        init = MathTex(r"a > b", font_size=56).move_to(UP * 4.7)
        cond = VGroup(
            Text("其中", font=FONT, font_size=24, color=GRAY_A),
            MathTex(r"c < 0", font_size=36, color=COLOR_NEG),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 4.0)

        self.play(Write(init), FadeIn(cond), run_time=0.6)
        self.wait(0.3)

        arrow = MathTex(r"\Downarrow", font_size=42, color=COLOR_NEG).move_to(UP * 3.2)
        op_label = VGroup(
            Text("两边", font=FONT, font_size=24, color=WHITE),
            MathTex(r"\times c \;(c<0)", font_size=32, color=COLOR_NEG),
        ).arrange(RIGHT, buff=0.2).move_to(UP * 2.5)

        self.play(FadeIn(arrow), FadeIn(op_label), run_time=0.4)

        # 不等号翻转动画
        result_before = MathTex(r"ac \,>\, bc", font_size=58, color=GRAY_B).move_to(UP * 1.5)
        cross = MathTex(r"\times", font_size=36, color=COLOR_FLIP).next_to(result_before, RIGHT, buff=0.2)

        result_after = MathTex(r"ac \,<\, bc", font_size=58).move_to(UP * 1.5)
        result_after[0][2].set_color(COLOR_FLIP)
        result_after[0][0].set_color(COLOR_NEG)
        result_after[0][4].set_color(COLOR_NEG)

        self.play(Write(result_before), FadeIn(cross), run_time=0.5)
        self.wait(0.3)
        self.play(
            FadeOut(result_before), FadeOut(cross),
            run_time=0.3
        )
        self.play(Write(result_after), run_time=0.6)

        # 翻转警告
        warn_bg = RoundedRectangle(
            width=6.5, height=0.85, corner_radius=0.18,
            fill_color="#4a0000", fill_opacity=0.8,
            stroke_color=COLOR_FLIP, stroke_width=3
        ).move_to(UP * 0.3)
        warn_txt = Text(
            "⚠  不等号方向必须改变！",
            font=FONT, font_size=26, color="#ff6b6b"
        ).move_to(UP * 0.3)
        self.play(Create(warn_bg), Write(warn_txt), run_time=0.6)
        self.play(Indicate(warn_txt, scale_factor=1.1, color=YELLOW), run_time=0.5)

        # ---- 数字验证（最有说服力）----
        sep = Line(LEFT * 3.6, RIGHT * 3.6, color=GRAY_D, stroke_width=1.2).move_to(DOWN * 0.5)
        self.play(Create(sep), run_time=0.3)

        demo_title = Text("数字验证：", font=FONT, font_size=24, color=GOLD).move_to(DOWN * 1.1 + LEFT * 1.5)

        # 3 > 2, ×(-1) → -3 < -2
        demo_start = MathTex(r"3 > 2", font_size=42).move_to(DOWN * 1.8 + LEFT * 1.5)
        demo_op    = VGroup(
            Text("×(-1)", font=FONT, font_size=28, color=COLOR_NEG),
            MathTex(r"\Rightarrow", font_size=32, color=COLOR_NEG),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.8 + RIGHT * 0.5)
        demo_end   = MathTex(r"-3 < -2", font_size=42, color=COLOR_FLIP).move_to(DOWN * 1.8 + RIGHT * 2.4)

        # 6 > 4, ÷(-2) → -3 < -2
        demo2_start = MathTex(r"6 > 4", font_size=38, color=GRAY_A).move_to(DOWN * 2.7 + LEFT * 1.5)
        demo2_op    = VGroup(
            Text("÷(-2)", font=FONT, font_size=26, color=COLOR_NEG),
            MathTex(r"\Rightarrow", font_size=28, color=COLOR_NEG),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.7 + RIGHT * 0.5)
        demo2_end   = MathTex(r"-3 < -2", font_size=38, color=COLOR_FLIP).move_to(DOWN * 2.7 + RIGHT * 2.4)

        self.play(FadeIn(demo_title), run_time=0.3)
        self.play(Write(demo_start), FadeIn(demo_op), Write(demo_end), run_time=0.8)
        self.play(Write(demo2_start), FadeIn(demo2_op), Write(demo2_end), run_time=0.7)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(sub), FadeOut(init), FadeOut(cond),
            FadeOut(arrow), FadeOut(op_label), FadeOut(result_after),
            FadeOut(warn_bg), FadeOut(warn_txt),
            FadeOut(sep), FadeOut(demo_title),
            FadeOut(demo_start), FadeOut(demo_op), FadeOut(demo_end),
            FadeOut(demo2_start), FadeOut(demo2_op), FadeOut(demo2_end),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # Scene 7: 解不等式 + 数轴
    # ----------------------------------------------------------
    def scene_solve_example(self):
        title = Text("解一元一次不等式", font=FONT, font_size=32, color=GOLD).move_to(UP * 6.3)
        self.play(Write(title), run_time=0.5)

        # 题目
        prob_label = Text("解：", font=FONT, font_size=26, color=GRAY_A).move_to(UP * 5.5 + LEFT * 2.8)
        prob_eq = MathTex(r"2x - 6 > 0", font_size=50).move_to(UP * 5.5 + RIGHT * 0.5)
        prob_eq[0][0].set_color(COLOR_POS)
        prob_eq[0][1].set_color(COLOR_X)

        self.play(FadeIn(prob_label), Write(prob_eq), run_time=0.6)
        self.wait(0.3)

        # Step 1: 两边 +6
        step1_note = VGroup(
            Text("两边", font=FONT, font_size=22, color=WHITE),
            MathTex(r"+6", font_size=28, color=COLOR_POS),
            Text("（性质一）", font=FONT, font_size=20, color=GRAY_A),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 4.3)
        step1_arrow = MathTex(r"\Downarrow", font_size=34, color=COLOR_POS).move_to(UP * 3.7)
        step1_eq = MathTex(r"2x > 6", font_size=50).move_to(UP * 3.1)
        step1_eq[0][0].set_color(COLOR_POS)
        step1_eq[0][1].set_color(COLOR_X)

        self.play(FadeIn(step1_note), FadeIn(step1_arrow), run_time=0.4)
        self.play(Write(step1_eq), run_time=0.5)

        # Step 2: 两边 ÷2 (正数，不变)
        step2_note = VGroup(
            Text("两边", font=FONT, font_size=22, color=WHITE),
            MathTex(r"\div 2", font_size=28, color=COLOR_POS),
            Text("（正数，不等号不变）", font=FONT, font_size=20, color=COLOR_OK),
        ).arrange(RIGHT, buff=0.15).move_to(UP * 2.2)
        step2_arrow = MathTex(r"\Downarrow", font_size=34, color=COLOR_OK).move_to(UP * 1.6)
        step2_eq = MathTex(r"x > 3", font_size=58, color=COLOR_OK).move_to(UP * 0.9)
        step2_eq[0][0].set_color(COLOR_X)
        step2_box = SurroundingRectangle(step2_eq, color=COLOR_OK, buff=0.2, corner_radius=0.12)

        self.play(FadeIn(step2_note), FadeIn(step2_arrow), run_time=0.4)
        self.play(Write(step2_eq), Create(step2_box), run_time=0.6)
        self.wait(0.5)

        # ---- 数轴表示 ----
        nl_label = Text("数轴表示解集：", font=FONT, font_size=24, color=GOLD).move_to(DOWN * 0.3)
        self.play(FadeIn(nl_label), run_time=0.4)

        # 数轴：x_range 精确计算
        # 显示区间 [-1, 7]，数轴中心在 (0, -1.5)
        # 数轴长度 = 7单位 逻辑坐标 → 显示宽度 = 7.0（frame宽=9，留边距）
        NL_CENTER_Y = -1.5
        NL_LEFT_X   = -3.5
        NL_RIGHT_X  =  3.5
        NL_RANGE_MIN = -1
        NL_RANGE_MAX =  7

        # 每逻辑单位对应的像素单位
        display_len  = NL_RIGHT_X - NL_LEFT_X   # = 7.0
        logical_len  = NL_RANGE_MAX - NL_RANGE_MIN  # = 8
        scale        = display_len / logical_len     # = 0.875

        def to_display(x_val):
            """逻辑 x → 显示坐标"""
            return NL_LEFT_X + (x_val - NL_RANGE_MIN) * scale

        # 轴线
        axis_line = Line(
            np.array([NL_LEFT_X, NL_CENTER_Y, 0]),
            np.array([NL_RIGHT_X + 0.3, NL_CENTER_Y, 0]),
            color=COLOR_NUM, stroke_width=2.5
        )
        axis_arrow = Arrow(
            np.array([NL_RIGHT_X, NL_CENTER_Y, 0]),
            np.array([NL_RIGHT_X + 0.4, NL_CENTER_Y, 0]),
            color=COLOR_NUM, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.6
        )

        # 刻度和标签（0,1,2,3,4,5,6）
        ticks = VGroup()
        tick_labels = VGroup()
        for v in range(0, 7):
            xd = to_display(v)
            tick = Line(
                np.array([xd, NL_CENTER_Y - 0.12, 0]),
                np.array([xd, NL_CENTER_Y + 0.12, 0]),
                color=COLOR_NUM, stroke_width=2
            )
            lbl_color = YELLOW if v == 3 else GRAY_A
            lbl = MathTex(str(v), font_size=20, color=lbl_color).move_to(
                np.array([xd, NL_CENTER_Y - 0.38, 0])
            )
            ticks.add(tick)
            tick_labels.add(lbl)

        # x = 3 的位置（精确计算）
        x3_display = to_display(3)   # = -3.5 + (3 - (-1)) * 0.875 = -3.5 + 3.5 = 0.0
        x3_pos = np.array([x3_display, NL_CENTER_Y, 0])

        # 空心点（x > 3，不含3）
        open_dot = Circle(
            radius=0.14, color=COLOR_SOL,
            fill_color=BG_COLOR, fill_opacity=1.0,
            stroke_width=3
        ).move_to(x3_pos)

        # 解集射线：从 x=3 向右
        ray_end_x = NL_RIGHT_X + 0.05
        solution_ray = Line(
            x3_pos,
            np.array([ray_end_x, NL_CENTER_Y, 0]),
            color=COLOR_SOL, stroke_width=5
        )
        ray_arrow = Arrow(
            np.array([ray_end_x - 0.3, NL_CENTER_Y, 0]),
            np.array([ray_end_x + 0.1, NL_CENTER_Y, 0]),
            color=COLOR_SOL, stroke_width=4,
            max_tip_length_to_length_ratio=0.5
        )

        # "x > 3" 标签
        sol_label = MathTex(r"x > 3", font_size=32, color=COLOR_SOL).move_to(
            np.array([x3_display + 1.0, NL_CENTER_Y - 0.75, 0])
        )

        self.play(Create(axis_line), GrowArrow(axis_arrow), run_time=0.5)
        self.play(FadeIn(ticks), FadeIn(tick_labels), run_time=0.4)
        self.play(Create(open_dot), run_time=0.4)
        self.play(Create(solution_ray), GrowArrow(ray_arrow), run_time=0.6)
        self.play(FadeIn(sol_label), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(prob_label), FadeOut(prob_eq),
            FadeOut(step1_note), FadeOut(step1_arrow), FadeOut(step1_eq),
            FadeOut(step2_note), FadeOut(step2_arrow),
            FadeOut(step2_eq), FadeOut(step2_box), FadeOut(nl_label),
            FadeOut(axis_line), FadeOut(axis_arrow),
            FadeOut(ticks), FadeOut(tick_labels),
            FadeOut(open_dot), FadeOut(solution_ray),
            FadeOut(ray_arrow), FadeOut(sol_label),
            run_time=0.6
        )

    # ----------------------------------------------------------
    # Scene 8: 总结
    # ----------------------------------------------------------
    def scene_summary(self):
        title = Text("三条性质 · 核心口诀", font=FONT, font_size=30, color=GOLD).move_to(UP * 6.5)
        self.play(Write(title), run_time=0.5)

        # 卡片1：性质一
        c1_t = Text("加减法", font=FONT, font_size=24, color=COLOR_OK).move_to(UP * 5.6)
        c1_f = MathTex(r"a>b \Rightarrow a \pm c \,>\, b \pm c", font_size=34).move_to(UP * 5.0)
        c1_note = Text("不等号不变 ✓", font=FONT, font_size=20, color=COLOR_OK).move_to(UP * 4.5)
        c1_group = VGroup(c1_t, c1_f, c1_note)
        c1_bg = card_bg(c1_group, fill="#001a08", stroke=COLOR_OK, buff=0.22)

        # 卡片2：性质二
        c2_t = Text("乘除正数", font=FONT, font_size=24, color=COLOR_POS).move_to(UP * 3.3)
        c2_f = MathTex(r"a>b,\,c>0 \Rightarrow ac > bc", font_size=32).move_to(UP * 2.7)
        c2_note = Text("不等号不变 ✓", font=FONT, font_size=20, color=COLOR_OK).move_to(UP * 2.2)
        c2_group = VGroup(c2_t, c2_f, c2_note)
        c2_bg = card_bg(c2_group, fill="#001020", stroke=COLOR_POS, buff=0.22)

        # 卡片3：性质三（最重要）
        c3_t = Text("乘除负数", font=FONT, font_size=24, color=COLOR_FLIP).move_to(UP * 1.0)
        c3_f = MathTex(r"a>b,\,c<0 \Rightarrow ac < bc", font_size=32).move_to(UP * 0.4)
        c3_note = Text("⚠  不等号翻转！", font=FONT, font_size=22, color=COLOR_FLIP).move_to(DOWN * 0.2)
        c3_group = VGroup(c3_t, c3_f, c3_note)
        c3_bg = card_bg(c3_group, fill="#3a0000", stroke=COLOR_FLIP, buff=0.22)

        # 口诀
        slogan = Text(
            "加减不变 · 乘正不变 · 乘负要翻",
            font=FONT, font_size=24, color=YELLOW
        ).move_to(DOWN * 1.4)
        slogan_bg = card_bg(slogan, fill="#1a1400", stroke=YELLOW, buff=0.2)

        self.play(Create(c1_bg), Write(c1_t), Write(c1_f), FadeIn(c1_note), run_time=0.7)
        self.play(Create(c2_bg), Write(c2_t), Write(c2_f), FadeIn(c2_note), run_time=0.7)
        self.play(Create(c3_bg), Write(c3_t), Write(c3_f), Write(c3_note), run_time=0.8)
        self.play(Indicate(c3_note, scale_factor=1.1, color=YELLOW), run_time=0.5)
        self.play(Create(slogan_bg), Write(slogan), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(c1_bg), FadeOut(c1_t), FadeOut(c1_f), FadeOut(c1_note),
            FadeOut(c2_bg), FadeOut(c2_t), FadeOut(c2_f), FadeOut(c2_note),
            FadeOut(c3_bg), FadeOut(c3_t), FadeOut(c3_f), FadeOut(c3_note),
            FadeOut(slogan_bg), FadeOut(slogan),
            run_time=0.6
        )

    # ----------------------------------------------------------
    # Scene 9: 片尾
    # ----------------------------------------------------------
    def scene_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=36, color=WHITE
        ).move_to(UP * 2.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=26, color=GRAY_B
        ).move_to(UP * 1.1)
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=28, color=YELLOW
        ).move_to(DOWN * 0.2)

        # 装饰：三条性质缩略
        decos = VGroup(
            MathTex(r"a \pm c \;>\; b \pm c", font_size=22, color=COLOR_OK),
            MathTex(r"ac > bc \;(c>0)", font_size=22, color=COLOR_POS),
            MathTex(r"ac < bc \;(c<0)", font_size=22, color=COLOR_FLIP),
        ).arrange(DOWN, buff=0.35).set_opacity(0.6).move_to(DOWN * 2.0)

        self.play(Transform(self.author, author_big), run_time=0.6)
        self.play(FadeIn(author_id), run_time=0.4)
        self.play(FadeIn(follow, scale=1.05), run_time=0.5)
        self.play(FadeIn(decos), run_time=0.5)
        self.play(
            Indicate(decos[2], scale_factor=1.2, color=YELLOW),
            run_time=0.7
        )
        self.wait(1.5)

        self.play(
            FadeOut(self.author), FadeOut(author_id),
            FadeOut(follow), FadeOut(decos),
            run_time=0.8
        )

# manim -pql linear_inequality.py LinearInequality   # 快速预览
# manim -qh  linear_inequality.py LinearInequality   # 高质量输出