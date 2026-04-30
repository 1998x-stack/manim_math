"""
001_两位数除以一位数_竖式计算.py — 两位数除以一位数（竖式计算）教学动画

知识点:
  - 从被除数的最高位除起，除到哪一位，商就写在哪一位的上面
  - 如果哪一位上不够商1，就在那一位上商0
  - 每次除得的余数必须比除数小
  - 例1: 52 ÷ 4 = 13（十位5÷4=1余1，余下1个十与个位2合成12，12÷4=3）
  - 例2: 57 ÷ 4 = 14...1（有余数的情况）

年级: 三年级上册
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
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
COLOR_TITLE = "#fbbf24"         # 黄色标题
COLOR_HL = "#fbbf24"            # 黄色高亮
COLOR_BLUE = "#3b82f6"          # 蓝色
COLOR_GREEN = "#22c55e"         # 绿色
COLOR_ORANGE = "#f59e0b"        # 橙色
COLOR_RED = "#ef4444"           # 红色
COLOR_PURPLE = "#a78bfa"        # 紫色
COLOR_PINK = "#f472b6"          # 粉色
COLOR_CYAN = "#38bdf8"          # 天蓝色
COLOR_AUTHOR = "#6b7280"        # 灰色作者信息
FONT = "PingFang SC"


# ======================================================================
# 辅助函数: 构建竖式除法布局
# ======================================================================
def build_long_division(
    divisor, dividend_tens, dividend_ones,
    origin=ORIGIN,
    num_size=40,
    spacing_x=0.8,
    spacing_y=0.9,
):
    """
    构建竖式除法的基本骨架（除数、被除数、除法符号线）。
    返回一个字典，包含所有 Mobject 和关键位置坐标。

    布局:
           ___________
      d  )  T    O
    """
    ox, oy = origin[0], origin[1]

    # 被除数十位、个位
    tens_pos = np.array([ox, oy, 0])
    ones_pos = np.array([ox + spacing_x, oy, 0])

    dividend_t = MathTex(str(dividend_tens), font_size=num_size, color=WHITE)
    dividend_t.move_to(tens_pos)
    dividend_o = MathTex(str(dividend_ones), font_size=num_size, color=WHITE)
    dividend_o.move_to(ones_pos)

    # 除数
    divisor_pos = np.array([ox - spacing_x * 1.5, oy, 0])
    divisor_mob = MathTex(str(divisor), font_size=num_size, color=WHITE)
    divisor_mob.move_to(divisor_pos)

    # 除法括号: 竖线 + 横线
    bracket_v = Line(
        start=np.array([ox - spacing_x * 0.7, oy + spacing_y * 0.55, 0]),
        end=np.array([ox - spacing_x * 0.7, oy - spacing_y * 0.55, 0]),
        color=WHITE, stroke_width=3,
    )
    bracket_h = Line(
        start=np.array([ox - spacing_x * 0.7, oy + spacing_y * 0.55, 0]),
        end=np.array([ox + spacing_x * 1.6, oy + spacing_y * 0.55, 0]),
        color=WHITE, stroke_width=3,
    )

    # 商的位置 (十位上方、个位上方)
    quotient_tens_pos = np.array([ox, oy + spacing_y * 1.2, 0])
    quotient_ones_pos = np.array([ox + spacing_x, oy + spacing_y * 1.2, 0])

    return {
        "divisor": divisor_mob,
        "dividend_tens": dividend_t,
        "dividend_ones": dividend_o,
        "bracket_v": bracket_v,
        "bracket_h": bracket_h,
        "divisor_pos": divisor_pos,
        "tens_pos": tens_pos,
        "ones_pos": ones_pos,
        "quotient_tens_pos": quotient_tens_pos,
        "quotient_ones_pos": quotient_ones_pos,
        "origin": origin,
        "spacing_x": spacing_x,
        "spacing_y": spacing_y,
        "num_size": num_size,
    }


# ======================================================================
# 主场景
# ======================================================================
class LongDivisionLesson(Scene):
    """
    两位数除以一位数（竖式计算）教学动画

    场景顺序:
      1. 开场钩子 — "52 ÷ 4 = ?" 引发思考
      2. 竖式格式介绍 — 认识除法竖式的各部分
      3. 例1: 52÷4=13 逐步演算
      4. 例2: 57÷4=14...1 有余数的逐步演算
      5. 三条核心法则总结
      6. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_format_intro()
        self.scene_3_example_52div4()
        self.scene_4_example_57div4()
        self.scene_5_rules_summary()
        self.scene_6_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------
    def scene_1_opening(self):
        # 作者信息
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 大标题
        title = Text(
            "两位数除以一位数", font=FONT, font_size=36, color=WHITE,
        ).move_to(UP * 5.2)
        subtitle = Text(
            "竖式计算", font=FONT, font_size=32, color=COLOR_TITLE,
        ).move_to(UP * 4.3)

        self.play(Write(title), run_time=0.7)
        self.play(Write(subtitle), run_time=0.6)
        self.wait(0.4)

        # 钩子问题
        hook_q = MathTex(
            r"52 \div 4 = \;?", font_size=56, color=COLOR_CYAN,
        ).move_to(UP * 2.0)

        question_box = SurroundingRectangle(
            hook_q, color=COLOR_CYAN, buff=0.4, corner_radius=0.2,
        )

        self.play(Write(hook_q), run_time=0.8)
        self.play(Create(question_box), run_time=0.5)
        self.wait(0.3)

        # 思考提示
        think = Text(
            "你能用竖式算出来吗?", font=FONT, font_size=26, color=COLOR_HL,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(think, shift=UP * 0.3), run_time=0.6)
        self.wait(0.5)

        # 除法的直观展示: 52个球分成4组
        dots_group = VGroup()
        for i in range(52):
            row = i // 13
            col = i % 13
            dot = Dot(radius=0.08, color=COLOR_BLUE, fill_opacity=0.7)
            dot.move_to(np.array([
                -3.0 + col * 0.5,
                -2.5 - row * 0.5,
                0
            ]))
            dots_group.add(dot)

        total_label = Text(
            "52个", font=FONT, font_size=22, color=COLOR_BLUE,
        ).next_to(dots_group, LEFT, buff=0.3)

        self.play(FadeIn(dots_group, lag_ratio=0.01), FadeIn(total_label), run_time=1.0)
        self.wait(0.3)

        divide_hint = Text(
            "平均分成4份，每份多少?", font=FONT, font_size=22, color=COLOR_ORANGE,
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(divide_hint), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(hook_q), FadeOut(question_box),
            FadeOut(think), FadeOut(dots_group),
            FadeOut(total_label), FadeOut(divide_hint),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 2: 竖式格式介绍
    # ------------------------------------------------------------------
    def scene_2_format_intro(self):
        title = Text(
            "认识除法竖式", font=FONT, font_size=36, color=COLOR_TITLE,
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 构建示意竖式 (用 ? 代替具体数字)
        origin = np.array([0, 2.5, 0])
        sp_x, sp_y = 0.9, 1.0
        num_sz = 44

        # 除数
        divisor = MathTex("4", font_size=num_sz, color=COLOR_ORANGE)
        divisor.move_to(origin + LEFT * sp_x * 1.5)

        # 被除数
        d_tens = MathTex("5", font_size=num_sz, color=COLOR_BLUE)
        d_tens.move_to(origin)
        d_ones = MathTex("2", font_size=num_sz, color=COLOR_BLUE)
        d_ones.move_to(origin + RIGHT * sp_x)

        # 括号
        bv = Line(
            start=origin + LEFT * sp_x * 0.7 + UP * sp_y * 0.55,
            end=origin + LEFT * sp_x * 0.7 + DOWN * sp_y * 0.55,
            color=WHITE, stroke_width=3,
        )
        bh = Line(
            start=origin + LEFT * sp_x * 0.7 + UP * sp_y * 0.55,
            end=origin + RIGHT * sp_x * 1.7 + UP * sp_y * 0.55,
            color=WHITE, stroke_width=3,
        )

        # 商的位置 (用 ? 占位)
        q_tens = MathTex("?", font_size=num_sz, color=COLOR_GREEN)
        q_tens.move_to(origin + UP * sp_y * 1.2)
        q_ones = MathTex("?", font_size=num_sz, color=COLOR_GREEN)
        q_ones.move_to(origin + RIGHT * sp_x + UP * sp_y * 1.2)

        # 逐步展示各部分
        # 先画括号
        self.play(Create(bv), Create(bh), run_time=0.6)

        # 除数
        label_divisor = Text(
            "除数", font=FONT, font_size=20, color=COLOR_ORANGE,
        ).next_to(divisor, LEFT, buff=0.3)
        self.play(Write(divisor), FadeIn(label_divisor), run_time=0.6)

        # 被除数
        label_dividend = Text(
            "被除数", font=FONT, font_size=20, color=COLOR_BLUE,
        ).next_to(d_ones, RIGHT, buff=0.3)
        self.play(Write(d_tens), Write(d_ones), FadeIn(label_dividend), run_time=0.6)

        # 商
        label_quotient = Text(
            "商", font=FONT, font_size=20, color=COLOR_GREEN,
        ).next_to(q_ones, RIGHT, buff=0.3)
        self.play(Write(q_tens), Write(q_ones), FadeIn(label_quotient), run_time=0.6)
        self.wait(0.5)

        # 说明文字
        explain_items = [
            ("从最高位除起", COLOR_CYAN),
            ("商写在对应位的上面", COLOR_GREEN),
            ("余数必须比除数小", COLOR_RED),
        ]

        explains = []
        for i, (text, color) in enumerate(explain_items):
            bullet = Text(
                text, font=FONT, font_size=22, color=color,
            ).move_to(DOWN * (1.0 + i * 1.0))

            icon = MathTex(
                r"\bullet", font_size=24, color=color,
            ).next_to(bullet, LEFT, buff=0.2)

            grp = VGroup(icon, bullet)
            explains.append(grp)
            self.play(FadeIn(grp, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.2)

        self.wait(0.5)

        # 指示箭头: 从高位到低位
        arrow = Arrow(
            start=d_tens.get_top() + UP * 0.2 + LEFT * 0.3,
            end=d_ones.get_top() + UP * 0.2 + RIGHT * 0.3,
            color=COLOR_HL, buff=0.1, stroke_width=3,
        )
        arrow_label = Text(
            "从左到右", font=FONT, font_size=18, color=COLOR_HL,
        ).next_to(arrow, UP, buff=0.15)

        self.play(Create(arrow), FadeIn(arrow_label), run_time=0.6)
        self.wait(1.0)

        # 清理
        all_mobs = VGroup(
            title, divisor, d_tens, d_ones, bv, bh,
            q_tens, q_ones,
            label_divisor, label_dividend, label_quotient,
            arrow, arrow_label, *explains,
        )
        self.play(FadeOut(all_mobs), run_time=0.6)

    # ------------------------------------------------------------------
    # Scene 3: 52 ÷ 4 = 13 逐步竖式演算
    # ------------------------------------------------------------------
    def scene_3_example_52div4(self):
        title = Text(
            "例1: 52 ÷ 4", font=FONT, font_size=36, color=COLOR_TITLE,
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # --- 竖式参数 ---
        origin = np.array([0.0, 3.5, 0])
        sp_x = 0.9
        sp_y = 1.0
        num_sz = 44

        # 被除数十位、个位位置
        tens_x = origin[0]
        ones_x = origin[0] + sp_x

        # 位置辅助
        def pos(x, y_offset):
            return np.array([x, origin[1] + y_offset, 0])

        # ====== Step 0: 画竖式骨架 ======
        divisor = MathTex("4", font_size=num_sz, color=COLOR_ORANGE)
        divisor.move_to(pos(tens_x - sp_x * 1.5, 0))

        d_tens = MathTex("5", font_size=num_sz, color=WHITE)
        d_tens.move_to(pos(tens_x, 0))
        d_ones = MathTex("2", font_size=num_sz, color=WHITE)
        d_ones.move_to(pos(ones_x, 0))

        bv = Line(
            start=pos(tens_x - sp_x * 0.7, sp_y * 0.55),
            end=pos(tens_x - sp_x * 0.7, -sp_y * 0.55),
            color=WHITE, stroke_width=3,
        )
        bh = Line(
            start=pos(tens_x - sp_x * 0.7, sp_y * 0.55),
            end=pos(ones_x + sp_x * 0.7, sp_y * 0.55),
            color=WHITE, stroke_width=3,
        )

        self.play(
            Write(divisor), Write(d_tens), Write(d_ones),
            Create(bv), Create(bh),
            run_time=0.8,
        )
        self.wait(0.3)

        # ====== Step 1: 看十位 5÷4 ======
        step1_label = Text(
            "第1步: 看十位", font=FONT, font_size=24, color=COLOR_CYAN,
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(step1_label), run_time=0.4)

        # 高亮十位的5
        hl_tens = SurroundingRectangle(d_tens, color=COLOR_HL, buff=0.12)
        self.play(Create(hl_tens), run_time=0.4)

        step1_calc = VGroup(
            Text("5 ", font=FONT, font_size=22, color=WHITE),
            MathTex(r"\div", font_size=22, color=WHITE),
            Text(" 4 ", font=FONT, font_size=22, color=COLOR_ORANGE),
            MathTex(r"=", font_size=22, color=WHITE),
            Text(" 1", font=FONT, font_size=22, color=COLOR_GREEN),
            Text(" ...... ", font=FONT, font_size=22, color=WHITE),
            Text("1", font=FONT, font_size=22, color=COLOR_RED),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.0)
        self.play(FadeIn(step1_calc), run_time=0.6)
        self.wait(0.3)

        step1_explain = Text(
            "商1写在十位上方", font=FONT, font_size=20, color=COLOR_GREEN,
        ).move_to(DOWN * 3.0)
        self.play(FadeIn(step1_explain), run_time=0.4)

        # 写商的十位: 1
        q_tens = MathTex("1", font_size=num_sz, color=COLOR_GREEN)
        q_tens.move_to(pos(tens_x, sp_y * 1.2))
        self.play(Write(q_tens), run_time=0.5)
        self.wait(0.3)

        # 写 4×1=4 在十位下方
        sub_4 = MathTex("4", font_size=num_sz, color=COLOR_PURPLE)
        sub_4.move_to(pos(tens_x, -sp_y * 1.0))
        sub_line_1 = Line(
            start=pos(tens_x - sp_x * 0.5, -sp_y * 1.5),
            end=pos(ones_x + sp_x * 0.5, -sp_y * 1.5),
            color=WHITE, stroke_width=2,
        )

        step1_sub = Text(
            "4 x 1 = 4, 写在下面", font=FONT, font_size=20, color=COLOR_PURPLE,
        ).move_to(DOWN * 4.0)
        self.play(Write(sub_4), FadeIn(step1_sub), run_time=0.5)
        self.play(Create(sub_line_1), run_time=0.3)

        # 5-4=1 余数
        remainder_1 = MathTex("1", font_size=num_sz, color=COLOR_RED)
        remainder_1.move_to(pos(tens_x, -sp_y * 2.0))

        step1_rem = Text(
            "5 - 4 = 1, 余1", font=FONT, font_size=20, color=COLOR_RED,
        ).move_to(DOWN * 5.0)
        self.play(Write(remainder_1), FadeIn(step1_rem), run_time=0.5)
        self.wait(0.5)

        # 清理说明文字
        self.play(
            FadeOut(step1_label), FadeOut(step1_calc),
            FadeOut(step1_explain), FadeOut(step1_sub),
            FadeOut(step1_rem), FadeOut(hl_tens),
            run_time=0.4,
        )

        # ====== Step 2: 落下个位，组成12 ======
        step2_label = Text(
            "第2步: 落下个位", font=FONT, font_size=24, color=COLOR_CYAN,
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(step2_label), run_time=0.4)

        # 落下动画: 个位2移到余数旁边
        bring_down_2 = MathTex("2", font_size=num_sz, color=COLOR_PINK)
        bring_down_2.move_to(pos(ones_x, -sp_y * 2.0))

        # 画落下箭头
        drop_arrow = Arrow(
            start=d_ones.get_bottom() + DOWN * 0.1,
            end=bring_down_2.get_top() + UP * 0.1,
            color=COLOR_PINK, stroke_width=2, buff=0.05,
        )

        step2_explain = Text(
            "余下1个十和个位2合成12", font=FONT, font_size=20, color=COLOR_PINK,
        ).move_to(DOWN * 2.5)

        self.play(Create(drop_arrow), run_time=0.4)
        self.play(Write(bring_down_2), FadeIn(step2_explain), run_time=0.5)

        # 高亮12
        hl_12 = SurroundingRectangle(
            VGroup(remainder_1, bring_down_2), color=COLOR_HL, buff=0.1,
        )
        self.play(Create(hl_12), run_time=0.4)
        self.wait(0.3)

        step2_calc = VGroup(
            Text("12 ", font=FONT, font_size=22, color=WHITE),
            MathTex(r"\div", font_size=22, color=WHITE),
            Text(" 4 ", font=FONT, font_size=22, color=COLOR_ORANGE),
            MathTex(r"=", font_size=22, color=WHITE),
            Text(" 3", font=FONT, font_size=22, color=COLOR_GREEN),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.5)
        self.play(FadeIn(step2_calc), run_time=0.5)

        step2_qexplain = Text(
            "商3写在个位上方", font=FONT, font_size=20, color=COLOR_GREEN,
        ).move_to(DOWN * 4.5)
        self.play(FadeIn(step2_qexplain), run_time=0.4)

        # 写商的个位: 3
        q_ones = MathTex("3", font_size=num_sz, color=COLOR_GREEN)
        q_ones.move_to(pos(ones_x, sp_y * 1.2))
        self.play(Write(q_ones), run_time=0.5)

        # 4×3=12, 写在下面
        sub_12 = MathTex("12", font_size=num_sz, color=COLOR_PURPLE)
        sub_12.move_to(pos((tens_x + ones_x) / 2, -sp_y * 3.0))
        sub_line_2 = Line(
            start=pos(tens_x - sp_x * 0.5, -sp_y * 3.5),
            end=pos(ones_x + sp_x * 0.5, -sp_y * 3.5),
            color=WHITE, stroke_width=2,
        )

        self.play(Write(sub_12), Create(sub_line_2), run_time=0.5)

        # 余数0
        remainder_0 = MathTex("0", font_size=num_sz, color=COLOR_GREEN)
        remainder_0.move_to(pos(ones_x, -sp_y * 4.0))

        step2_done = Text(
            "12 - 12 = 0, 整除!", font=FONT, font_size=20, color=COLOR_GREEN,
        ).move_to(DOWN * 5.5)
        self.play(Write(remainder_0), FadeIn(step2_done), run_time=0.5)
        self.wait(0.5)

        # 清理说明文字
        self.play(
            FadeOut(step2_label), FadeOut(step2_explain),
            FadeOut(step2_calc), FadeOut(step2_qexplain),
            FadeOut(step2_done), FadeOut(hl_12), FadeOut(drop_arrow),
            run_time=0.4,
        )

        # ====== 结论 ======
        result_box = RoundedRectangle(
            width=7, height=1.4, corner_radius=0.2,
            color=COLOR_GREEN, stroke_width=3, fill_opacity=0.1,
        ).move_to(DOWN * 3.0)

        result_text = MathTex(
            r"52 \div 4 = 13", font_size=48, color=COLOR_GREEN,
        ).move_to(result_box.get_center())

        self.play(FadeIn(result_box), Write(result_text), run_time=0.8)
        self.wait(0.5)

        check_text = Text(
            "验算: 13 x 4 = 52", font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 4.5)
        check_mark = MathTex(r"\checkmark", font_size=36, color=COLOR_GREEN)
        check_mark.next_to(check_text, RIGHT, buff=0.3)
        self.play(FadeIn(check_text), FadeIn(check_mark), run_time=0.5)
        self.wait(1.5)

        # 清理全部
        all_div = VGroup(
            title, divisor, d_tens, d_ones, bv, bh,
            q_tens, q_ones, sub_4, sub_line_1,
            remainder_1, bring_down_2, sub_12, sub_line_2,
            remainder_0, result_box, result_text,
            check_text, check_mark,
        )
        self.play(FadeOut(all_div), run_time=0.6)

    # ------------------------------------------------------------------
    # Scene 4: 57 ÷ 4 = 14...1 有余数的逐步竖式演算
    # ------------------------------------------------------------------
    def scene_4_example_57div4(self):
        title = Text(
            "例2: 57 ÷ 4 (有余数)", font=FONT, font_size=36, color=COLOR_TITLE,
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        intro = Text(
            "不是每次都能整除哦!", font=FONT, font_size=24, color=COLOR_PINK,
        ).move_to(UP * 5.0)
        self.play(FadeIn(intro, shift=UP * 0.2), run_time=0.5)
        self.wait(0.3)

        # --- 竖式参数 ---
        origin = np.array([0.0, 3.0, 0])
        sp_x = 0.9
        sp_y = 1.0
        num_sz = 44

        tens_x = origin[0]
        ones_x = origin[0] + sp_x

        def pos(x, y_offset):
            return np.array([x, origin[1] + y_offset, 0])

        # ====== Step 0: 画竖式骨架 ======
        divisor = MathTex("4", font_size=num_sz, color=COLOR_ORANGE)
        divisor.move_to(pos(tens_x - sp_x * 1.5, 0))

        d_tens = MathTex("5", font_size=num_sz, color=WHITE)
        d_tens.move_to(pos(tens_x, 0))
        d_ones = MathTex("7", font_size=num_sz, color=WHITE)
        d_ones.move_to(pos(ones_x, 0))

        bv = Line(
            start=pos(tens_x - sp_x * 0.7, sp_y * 0.55),
            end=pos(tens_x - sp_x * 0.7, -sp_y * 0.55),
            color=WHITE, stroke_width=3,
        )
        bh = Line(
            start=pos(tens_x - sp_x * 0.7, sp_y * 0.55),
            end=pos(ones_x + sp_x * 0.7, sp_y * 0.55),
            color=WHITE, stroke_width=3,
        )

        self.play(
            Write(divisor), Write(d_tens), Write(d_ones),
            Create(bv), Create(bh),
            run_time=0.8,
        )
        self.wait(0.3)

        # ====== Step 1: 十位 5÷4=1...1 ======
        step1_label = Text(
            "第1步: 十位 5÷4", font=FONT, font_size=24, color=COLOR_CYAN,
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(step1_label), run_time=0.4)

        hl_tens = SurroundingRectangle(d_tens, color=COLOR_HL, buff=0.12)
        self.play(Create(hl_tens), run_time=0.3)

        step1_calc = VGroup(
            Text("5 ", font=FONT, font_size=22, color=WHITE),
            MathTex(r"\div", font_size=22, color=WHITE),
            Text(" 4 ", font=FONT, font_size=22, color=COLOR_ORANGE),
            MathTex(r"=", font_size=22, color=WHITE),
            Text(" 1", font=FONT, font_size=22, color=COLOR_GREEN),
            Text(" ...... ", font=FONT, font_size=22, color=WHITE),
            Text("1", font=FONT, font_size=22, color=COLOR_RED),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.5)
        self.play(FadeIn(step1_calc), run_time=0.5)

        # 商1
        q_tens = MathTex("1", font_size=num_sz, color=COLOR_GREEN)
        q_tens.move_to(pos(tens_x, sp_y * 1.2))
        self.play(Write(q_tens), run_time=0.5)

        # 4×1=4
        sub_4 = MathTex("4", font_size=num_sz, color=COLOR_PURPLE)
        sub_4.move_to(pos(tens_x, -sp_y * 1.0))
        sub_line_1 = Line(
            start=pos(tens_x - sp_x * 0.5, -sp_y * 1.5),
            end=pos(ones_x + sp_x * 0.5, -sp_y * 1.5),
            color=WHITE, stroke_width=2,
        )
        self.play(Write(sub_4), Create(sub_line_1), run_time=0.5)

        # 余1
        remainder_1 = MathTex("1", font_size=num_sz, color=COLOR_RED)
        remainder_1.move_to(pos(tens_x, -sp_y * 2.0))
        self.play(Write(remainder_1), run_time=0.4)
        self.wait(0.3)

        self.play(
            FadeOut(step1_label), FadeOut(step1_calc), FadeOut(hl_tens),
            run_time=0.4,
        )

        # ====== Step 2: 落下个位7，组成17 ======
        step2_label = Text(
            "第2步: 落下个位7，组成17", font=FONT, font_size=24, color=COLOR_CYAN,
        ).move_to(DOWN * 1.5)
        self.play(FadeIn(step2_label), run_time=0.4)

        bring_down_7 = MathTex("7", font_size=num_sz, color=COLOR_PINK)
        bring_down_7.move_to(pos(ones_x, -sp_y * 2.0))

        drop_arrow = Arrow(
            start=d_ones.get_bottom() + DOWN * 0.1,
            end=bring_down_7.get_top() + UP * 0.1,
            color=COLOR_PINK, stroke_width=2, buff=0.05,
        )

        self.play(Create(drop_arrow), Write(bring_down_7), run_time=0.5)

        hl_17 = SurroundingRectangle(
            VGroup(remainder_1, bring_down_7), color=COLOR_HL, buff=0.1,
        )
        self.play(Create(hl_17), run_time=0.3)

        step2_calc = VGroup(
            Text("17 ", font=FONT, font_size=22, color=WHITE),
            MathTex(r"\div", font_size=22, color=WHITE),
            Text(" 4 ", font=FONT, font_size=22, color=COLOR_ORANGE),
            MathTex(r"=", font_size=22, color=WHITE),
            Text(" 4", font=FONT, font_size=22, color=COLOR_GREEN),
            Text(" ...... ", font=FONT, font_size=22, color=WHITE),
            Text("1", font=FONT, font_size=22, color=COLOR_RED),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.5)
        self.play(FadeIn(step2_calc), run_time=0.5)

        # 商4
        q_ones = MathTex("4", font_size=num_sz, color=COLOR_GREEN)
        q_ones.move_to(pos(ones_x, sp_y * 1.2))
        self.play(Write(q_ones), run_time=0.5)

        # 4×4=16
        sub_16 = MathTex("16", font_size=num_sz, color=COLOR_PURPLE)
        sub_16.move_to(pos((tens_x + ones_x) / 2, -sp_y * 3.0))
        sub_line_2 = Line(
            start=pos(tens_x - sp_x * 0.5, -sp_y * 3.5),
            end=pos(ones_x + sp_x * 0.5, -sp_y * 3.5),
            color=WHITE, stroke_width=2,
        )
        self.play(Write(sub_16), Create(sub_line_2), run_time=0.5)

        # 余数1!
        final_remainder = MathTex("1", font_size=num_sz, color=COLOR_RED)
        final_remainder.move_to(pos(ones_x, -sp_y * 4.0))

        step2_rem = Text(
            "17 - 16 = 1, 还剩1!", font=FONT, font_size=20, color=COLOR_RED,
        ).move_to(DOWN * 3.5)
        self.play(Write(final_remainder), FadeIn(step2_rem), run_time=0.5)
        self.wait(0.3)

        # 余数检查
        rem_check = Text(
            "余数 1 < 除数 4", font=FONT, font_size=20, color=COLOR_GREEN,
        ).move_to(DOWN * 4.5)
        check_mark = MathTex(r"\checkmark", font_size=28, color=COLOR_GREEN)
        check_mark.next_to(rem_check, RIGHT, buff=0.2)
        self.play(FadeIn(rem_check), FadeIn(check_mark), run_time=0.5)
        self.wait(0.3)

        self.play(
            FadeOut(step2_label), FadeOut(step2_calc),
            FadeOut(step2_rem), FadeOut(hl_17), FadeOut(drop_arrow),
            FadeOut(rem_check), FadeOut(check_mark),
            run_time=0.4,
        )

        # ====== 结论 ======
        result_box = RoundedRectangle(
            width=7.5, height=1.6, corner_radius=0.2,
            color=COLOR_ORANGE, stroke_width=3, fill_opacity=0.1,
        ).move_to(DOWN * 3.0)

        result_line = VGroup(
            MathTex(r"57 \div 4 = 14", font_size=44, color=COLOR_GREEN),
            MathTex(r"\cdots\cdots", font_size=44, color=WHITE),
            MathTex(r"1", font_size=44, color=COLOR_RED),
        ).arrange(RIGHT, buff=0.15).move_to(result_box.get_center())

        self.play(FadeIn(result_box), Write(result_line), run_time=0.8)
        self.wait(0.3)

        # 验算
        verify = Text(
            "验算: 14 x 4 + 1 = 57", font=FONT, font_size=22, color=GRAY_A,
        ).move_to(DOWN * 4.5)
        verify_mark = MathTex(r"\checkmark", font_size=28, color=COLOR_GREEN)
        verify_mark.next_to(verify, RIGHT, buff=0.3)
        self.play(FadeIn(verify), FadeIn(verify_mark), run_time=0.5)

        # 余数书写格式提示
        format_hint = Text(
            "余数用 ...... 表示", font=FONT, font_size=20, color=COLOR_HL,
        ).move_to(DOWN * 5.5)
        self.play(FadeIn(format_hint), run_time=0.4)
        self.wait(1.5)

        # 清理全部
        all_div = VGroup(
            title, intro, divisor, d_tens, d_ones, bv, bh,
            q_tens, q_ones, sub_4, sub_line_1,
            remainder_1, bring_down_7, sub_16, sub_line_2,
            final_remainder, result_box, result_line,
            verify, verify_mark, format_hint,
        )
        self.play(FadeOut(all_div), run_time=0.6)

    # ------------------------------------------------------------------
    # Scene 5: 三条核心法则总结
    # ------------------------------------------------------------------
    def scene_5_rules_summary(self):
        title = Text(
            "三条法则", font=FONT, font_size=36, color=COLOR_TITLE,
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        subtitle = Text(
            "竖式除法必须记住!", font=FONT, font_size=24, color=COLOR_HL,
        ).move_to(UP * 5.0)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)

        # 法则1
        rule1_icon_bg = Circle(
            radius=0.35, color=COLOR_CYAN, fill_opacity=0.9, stroke_width=0,
        ).move_to(UP * 3.5 + LEFT * 3.2)
        rule1_icon = Text(
            "1", font=FONT, font_size=24, color=WHITE,
        ).move_to(rule1_icon_bg.get_center())

        rule1_box = RoundedRectangle(
            width=7.5, height=2.2, corner_radius=0.2,
            color=COLOR_CYAN, stroke_width=2, fill_opacity=0.06,
        ).move_to(UP * 3.3)

        rule1_title = Text(
            "从最高位除起", font=FONT, font_size=26, color=COLOR_CYAN,
        ).move_to(rule1_box.get_center() + UP * 0.4)
        rule1_detail = Text(
            "除到哪一位，商就写在", font=FONT, font_size=20, color=GRAY_A,
        ).move_to(rule1_box.get_center() + DOWN * 0.1)
        rule1_detail2 = Text(
            "那一位的上面", font=FONT, font_size=20, color=GRAY_A,
        ).move_to(rule1_box.get_center() + DOWN * 0.5)

        rule1 = VGroup(rule1_box, rule1_icon_bg, rule1_icon,
                        rule1_title, rule1_detail, rule1_detail2)
        self.play(FadeIn(rule1, shift=RIGHT * 0.5), run_time=0.7)
        self.wait(0.5)

        # 法则2
        rule2_icon_bg = Circle(
            radius=0.35, color=COLOR_ORANGE, fill_opacity=0.9, stroke_width=0,
        ).move_to(UP * 0.7 + LEFT * 3.2)
        rule2_icon = Text(
            "2", font=FONT, font_size=24, color=WHITE,
        ).move_to(rule2_icon_bg.get_center())

        rule2_box = RoundedRectangle(
            width=7.5, height=2.2, corner_radius=0.2,
            color=COLOR_ORANGE, stroke_width=2, fill_opacity=0.06,
        ).move_to(UP * 0.5)

        rule2_title = Text(
            "不够商1就商0", font=FONT, font_size=26, color=COLOR_ORANGE,
        ).move_to(rule2_box.get_center() + UP * 0.4)
        rule2_detail = Text(
            "如果哪一位上不够商1，", font=FONT, font_size=20, color=GRAY_A,
        ).move_to(rule2_box.get_center() + DOWN * 0.1)
        rule2_detail2 = Text(
            "就在那一位上商0占位", font=FONT, font_size=20, color=GRAY_A,
        ).move_to(rule2_box.get_center() + DOWN * 0.5)

        rule2 = VGroup(rule2_box, rule2_icon_bg, rule2_icon,
                        rule2_title, rule2_detail, rule2_detail2)
        self.play(FadeIn(rule2, shift=RIGHT * 0.5), run_time=0.7)
        self.wait(0.5)

        # 法则3
        rule3_icon_bg = Circle(
            radius=0.35, color=COLOR_RED, fill_opacity=0.9, stroke_width=0,
        ).move_to(DOWN * 2.1 + LEFT * 3.2)
        rule3_icon = Text(
            "3", font=FONT, font_size=24, color=WHITE,
        ).move_to(rule3_icon_bg.get_center())

        rule3_box = RoundedRectangle(
            width=7.5, height=2.2, corner_radius=0.2,
            color=COLOR_RED, stroke_width=2, fill_opacity=0.06,
        ).move_to(DOWN * 2.3)

        rule3_title = Text(
            "余数 < 除数", font=FONT, font_size=26, color=COLOR_RED,
        ).move_to(rule3_box.get_center() + UP * 0.4)
        rule3_detail = Text(
            "每次除得的余数", font=FONT, font_size=20, color=GRAY_A,
        ).move_to(rule3_box.get_center() + DOWN * 0.1)
        rule3_detail2 = Text(
            "必须比除数小", font=FONT, font_size=20, color=GRAY_A,
        ).move_to(rule3_box.get_center() + DOWN * 0.5)

        rule3 = VGroup(rule3_box, rule3_icon_bg, rule3_icon,
                        rule3_title, rule3_detail, rule3_detail2)
        self.play(FadeIn(rule3, shift=RIGHT * 0.5), run_time=0.7)
        self.wait(0.5)

        # 底部: 对比两个例子
        compare_title = Text(
            "两个例子对比", font=FONT, font_size=22, color=COLOR_HL,
        ).move_to(DOWN * 4.3)
        self.play(FadeIn(compare_title), run_time=0.4)

        ex1 = VGroup(
            MathTex(r"52 \div 4 = 13", font_size=30, color=COLOR_GREEN),
            Text("整除", font=FONT, font_size=18, color=COLOR_GREEN),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 5.3 + LEFT * 2)

        ex2 = VGroup(
            MathTex(r"57 \div 4 = 14", font_size=30, color=COLOR_ORANGE),
            MathTex(r"\cdots 1", font_size=30, color=COLOR_RED),
            Text("有余数", font=FONT, font_size=18, color=COLOR_RED),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 5.3 + RIGHT * 2)

        # scale if too wide
        compare_line = VGroup(ex1, ex2)
        if compare_line.width > 8.0:
            compare_line.scale(8.0 / compare_line.width)

        self.play(FadeIn(ex1), FadeIn(ex2), run_time=0.6)
        self.wait(2.0)

        # 高亮闪烁
        for rule in [rule1, rule2, rule3]:
            self.play(
                Indicate(rule, color=COLOR_HL, scale_factor=1.03),
                run_time=0.4,
            )

        self.wait(1.0)

        # 清理
        all_mobs = VGroup(
            title, subtitle,
            rule1, rule2, rule3,
            compare_title, ex1, ex2,
        )
        self.play(FadeOut(all_mobs), run_time=0.6)

    # ------------------------------------------------------------------
    # Scene 6: 片尾
    # ------------------------------------------------------------------
    def scene_6_outro(self):
        # 大作者名
        author_name = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=40, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B,
        ).move_to(UP * 0.5)

        self.play(
            Transform(self.author_mob, author_name),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        follow_text = Text(
            "关注我, 获得更多数学技巧!",
            font=FONT, font_size=30, color=COLOR_HL,
        ).move_to(DOWN * 1.0)
        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)

        # 小结公式
        final_formula = VGroup(
            MathTex(r"52 \div 4 = 13", font_size=32, color=COLOR_GREEN),
            MathTex(r"57 \div 4 = 14 \cdots 1", font_size=32, color=COLOR_ORANGE),
        ).arrange(DOWN, buff=0.5).move_to(DOWN * 3.0)

        self.play(FadeIn(final_formula, shift=UP * 0.3), run_time=0.6)
        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(self.author_mob),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(final_formula),
            run_time=1.0,
        )
