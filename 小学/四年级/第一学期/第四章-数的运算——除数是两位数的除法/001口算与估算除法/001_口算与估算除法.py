"""
001_口算与估算除法.py — 口算与估算除法 教学动画

知识点: 将除数和被除数看作整十数进行估算
  - 把被除数近似为接近的整十数
  - 把除数近似为接近的整十数
  - 得到估算结果, 确定商的大致范围
  - 例: 382 ÷ 19 ≈ 380 ÷ 20 = 19

年级: 四年级第一学期
格式: TikTok 竖屏 (1080×1920)
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
BG_COLOR      = "#1a1a2e"
COLOR_DIVIDEND = "#3b82f6"   # 蓝色  被除数
COLOR_DIVISOR  = "#f59e0b"   # 橙色  除数
COLOR_RESULT   = "#22c55e"   # 绿色  商
COLOR_ARROW    = "#a78bfa"   # 紫色  箭头 / 变换
COLOR_HL       = "#fbbf24"   # 黄色  高亮
COLOR_GRAY_TXT = "#9ca3af"   # 灰色  辅助文字
COLOR_AUTHOR   = "#6b7280"   # 灰色  作者信息
FONT           = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class MentalEstimateDivLesson(Scene):
    """
    口算与估算除法 教学动画

    场景顺序:
      1. 开场钩子  — 引出问题 382÷19 怎么估算?
      2. 口算规则  — 整十数除以整十数
      3. 估算步骤  — 被除数近似 → 除数近似 → 得到结果
      4. 动态演示  — 数轴上可视化 382 → 380, 19 → 20
      5. 验证理解  — 再举两个例子
      6. 规律总结  — 估算口诀
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_mental_div_rules()
        self.scene_3_estimate_steps()
        self.scene_4_number_line_demo()
        self.scene_5_more_examples()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 几何初始化
    # ------------------------------------------------------------------

    def setup_geometry(self):
        """初始化数轴参数及常用数值"""
        # 数轴范围和缩放
        self.NL_X_MIN = 0
        self.NL_X_MAX = 400
        self.NL_SCALE = 0.016          # 每单位对应的逻辑宽度
        self.NL_ORIGIN_X = -3.2       # 数轴左端 x 坐标
        self.NL_Y = 1.0               # 数轴 y 坐标

        # 主例题: 382 ÷ 19
        self.dividend_exact = 382
        self.divisor_exact  = 19
        self.dividend_round = 380
        self.divisor_round  = 20
        self.quotient       = self.dividend_round // self.divisor_round  # 19

    def _num_to_x(self, n):
        """将数值映射到数轴上的 x 坐标"""
        return self.NL_ORIGIN_X + (n - self.NL_X_MIN) * self.NL_SCALE * (6.4 / (self.NL_X_MAX - self.NL_X_MIN) / self.NL_SCALE)

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        """作者标识"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_title_bar(self, text, color=WHITE, font_size=34):
        """顶部标题条"""
        return Text(text, font=FONT, font_size=font_size, color=color).move_to(UP * 5.5)

    def make_step_label(self, text, pos=DOWN * 4.5):
        """步骤说明文字"""
        return Text(text, font=FONT, font_size=22, color=COLOR_GRAY_TXT).move_to(pos)

    def create_division_display(self, dividend, divisor, approx=False, y_pos=2.0):
        """
        生成除法算式组合 (纯 MathTex + Text 拼合, 避免中文进入 MathTex)
        approx=True: 显示 ≈ 号
        """
        sym = r"\approx" if approx else r"\div"
        formula = MathTex(
            str(dividend), r"\div", str(divisor),
            font_size=52,
        )
        formula.move_to(UP * y_pos)
        # 着色
        formula[0].set_color(COLOR_DIVIDEND)
        formula[2].set_color(COLOR_DIVISOR)
        return formula

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.author = self.make_author()
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook_line1 = Text(
            "除数是两位数,",
            font=FONT, font_size=38, color=COLOR_HL,
        ).move_to(UP * 5.0)

        hook_line2 = Text(
            "算之前先估一估!",
            font=FONT, font_size=38, color=COLOR_HL,
        ).move_to(UP * 4.2)

        self.play(Write(hook_line1), run_time=0.7)
        self.play(Write(hook_line2), run_time=0.7)

        # 主题算式亮相
        main_formula = MathTex(
            r"382 \div 19 = \; ?",
            font_size=58, color=WHITE,
        ).move_to(UP * 2.5)
        main_formula[0][0:3].set_color(COLOR_DIVIDEND)
        main_formula[0][4:6].set_color(COLOR_DIVISOR)

        self.play(Write(main_formula), run_time=1.0)
        self.wait(0.6)

        sub = Text(
            "不用精确计算, 先估算出大概范围!",
            font=FONT, font_size=22, color=COLOR_GRAY_TXT,
        ).move_to(UP * 1.2)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(hook_line1), FadeOut(hook_line2),
            FadeOut(main_formula), FadeOut(sub),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 口算整十数除法规则
    # ------------------------------------------------------------------

    def scene_2_mental_div_rules(self):
        title = self.make_title_bar("整十数的口算", color=COLOR_HL)
        self.play(Write(title), run_time=0.5)

        intro = Text(
            "先看整十数怎么口算:",
            font=FONT, font_size=24, color=WHITE,
        ).move_to(UP * 4.5)
        self.play(FadeIn(intro), run_time=0.4)

        # 三道整十数例题
        examples = [
            (r"60 \div 20 = 3",   r"60",  r"20", r"3"),
            (r"120 \div 40 = 3",  r"120", r"40", r"3"),
            (r"180 \div 60 = 3",  r"180", r"60", r"3"),
        ]

        positions = [UP * 3.0, UP * 1.5, UP * 0.0]
        example_mobs = []

        for i, (full, dnd, dsr, q) in enumerate(examples):
            f = MathTex(full, font_size=42)
            # 着色 token 0 = 被除数, token 2 = 除数, token 4 = 商
            f[0][0:len(dnd)].set_color(COLOR_DIVIDEND)
            f[0][len(dnd)+1:len(dnd)+1+len(dsr)].set_color(COLOR_DIVISOR)
            f[0][-len(q):].set_color(COLOR_RESULT)
            f.move_to(positions[i])
            example_mobs.append(f)
            self.play(Write(f), run_time=0.6)
            self.wait(0.3)

        # 规律说明
        tip_title = Text("口算技巧:", font=FONT, font_size=24, color=COLOR_HL).move_to(DOWN * 1.8)
        tip_body = Text(
            "把整十数末尾的 0 消掉, 再口算",
            font=FONT, font_size=20, color=COLOR_GRAY_TXT,
        ).move_to(DOWN * 2.5)

        # 示例: 60÷20 → 6÷2=3
        arrow_tex = MathTex(
            r"60 \div 20 \;\Rightarrow\; 6 \div 2 = 3",
            font_size=34, color=WHITE,
        ).move_to(DOWN * 3.5)
        arrow_tex[0][0:2].set_color(COLOR_DIVIDEND)
        arrow_tex[0][3:5].set_color(COLOR_DIVISOR)
        arrow_tex[0][-1].set_color(COLOR_RESULT)

        self.play(FadeIn(tip_title), FadeIn(tip_body), run_time=0.5)
        self.play(Write(arrow_tex), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(intro),
            *[FadeOut(e) for e in example_mobs],
            FadeOut(tip_title), FadeOut(tip_body),
            FadeOut(arrow_tex),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 估算步骤  382 ÷ 19
    # ------------------------------------------------------------------

    def scene_3_estimate_steps(self):
        title = self.make_title_bar("估算步骤", color=COLOR_ARROW)
        self.play(Write(title), run_time=0.5)

        # 原题
        original = MathTex(
            r"382 \div 19",
            font_size=54, color=WHITE,
        ).move_to(UP * 4.3)
        original[0][0:3].set_color(COLOR_DIVIDEND)
        original[0][4:6].set_color(COLOR_DIVISOR)
        self.play(Write(original), run_time=0.7)

        # 步骤框架
        step1_label = Text("第一步", font=FONT, font_size=26, color=COLOR_HL).move_to(UP * 3.0 + LEFT * 2.8)
        step1_desc = Text(
            "把被除数近似为整十数",
            font=FONT, font_size=22, color=COLOR_GRAY_TXT,
        ).move_to(UP * 3.0 + RIGHT * 0.8)

        self.play(FadeIn(step1_label), FadeIn(step1_desc), run_time=0.5)

        # 382 → 380
        dividend_transform = VGroup(
            MathTex(r"382", font_size=48, color=COLOR_DIVIDEND).move_to(UP * 2.0 + LEFT * 1.5),
            MathTex(r"\rightarrow", font_size=44, color=COLOR_ARROW).move_to(UP * 2.0),
            MathTex(r"380", font_size=48, color=COLOR_DIVIDEND).move_to(UP * 2.0 + RIGHT * 1.5),
        )
        note_dnd = Text(
            "(四舍五入到整十)",
            font=FONT, font_size=18, color=COLOR_GRAY_TXT,
        ).move_to(UP * 1.3)

        self.play(
            Write(dividend_transform[0]),
            Write(dividend_transform[1]),
            Write(dividend_transform[2]),
            run_time=0.8,
        )
        self.play(FadeIn(note_dnd), run_time=0.4)

        # 高亮 380
        self.play(
            Indicate(dividend_transform[2], color=COLOR_HL, scale_factor=1.2),
            run_time=0.6,
        )
        self.wait(0.5)

        # 步骤2
        step2_label = Text("第二步", font=FONT, font_size=26, color=COLOR_HL).move_to(UP * 0.3 + LEFT * 2.8)
        step2_desc = Text(
            "把除数近似为整十数",
            font=FONT, font_size=22, color=COLOR_GRAY_TXT,
        ).move_to(UP * 0.3 + RIGHT * 0.7)

        self.play(FadeIn(step2_label), FadeIn(step2_desc), run_time=0.5)

        # 19 → 20
        divisor_transform = VGroup(
            MathTex(r"19", font_size=48, color=COLOR_DIVISOR).move_to(DOWN * 0.7 + LEFT * 1.5),
            MathTex(r"\rightarrow", font_size=44, color=COLOR_ARROW).move_to(DOWN * 0.7),
            MathTex(r"20", font_size=48, color=COLOR_DIVISOR).move_to(DOWN * 0.7 + RIGHT * 1.5),
        )
        note_dsr = Text(
            "(四舍五入到整十)",
            font=FONT, font_size=18, color=COLOR_GRAY_TXT,
        ).move_to(DOWN * 1.4)

        self.play(
            Write(divisor_transform[0]),
            Write(divisor_transform[1]),
            Write(divisor_transform[2]),
            run_time=0.8,
        )
        self.play(FadeIn(note_dsr), run_time=0.4)
        self.play(
            Indicate(divisor_transform[2], color=COLOR_HL, scale_factor=1.2),
            run_time=0.6,
        )
        self.wait(0.5)

        # 步骤3
        step3_label = Text("第三步", font=FONT, font_size=26, color=COLOR_HL).move_to(DOWN * 2.4 + LEFT * 2.8)
        step3_desc = Text(
            "口算估算结果",
            font=FONT, font_size=22, color=COLOR_GRAY_TXT,
        ).move_to(DOWN * 2.4 + RIGHT * 0.3)

        self.play(FadeIn(step3_label), FadeIn(step3_desc), run_time=0.5)

        # 380 ÷ 20 = 19
        result_formula = MathTex(
            r"380 \div 20 = 19",
            font_size=48, color=WHITE,
        ).move_to(DOWN * 3.4)
        result_formula[0][0:3].set_color(COLOR_DIVIDEND)
        result_formula[0][4:6].set_color(COLOR_DIVISOR)
        result_formula[0][7:9].set_color(COLOR_RESULT)

        self.play(Write(result_formula), run_time=0.8)

        # 最终完整估算式
        full_estimate = MathTex(
            r"382 \div 19 \approx 380 \div 20 = 19",
            font_size=36, color=WHITE,
        ).move_to(DOWN * 5.0)
        full_estimate[0][0:3].set_color(COLOR_DIVIDEND)
        full_estimate[0][4:6].set_color(COLOR_DIVISOR)
        full_estimate[0][7:10].set_color(COLOR_DIVIDEND)
        full_estimate[0][11:13].set_color(COLOR_DIVISOR)
        full_estimate[0][14:16].set_color(COLOR_RESULT)

        self.play(Write(full_estimate), run_time=1.0)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(original),
            FadeOut(step1_label), FadeOut(step1_desc),
            FadeOut(dividend_transform), FadeOut(note_dnd),
            FadeOut(step2_label), FadeOut(step2_desc),
            FadeOut(divisor_transform), FadeOut(note_dsr),
            FadeOut(step3_label), FadeOut(step3_desc),
            FadeOut(result_formula), FadeOut(full_estimate),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 4: 数轴可视化  382→380, 19→20
    # ------------------------------------------------------------------

    def scene_4_number_line_demo(self):
        title = self.make_title_bar("数轴上看近似", color=COLOR_HL)
        self.play(Write(title), run_time=0.5)

        intro = Text(
            "四舍五入到最近的整十数",
            font=FONT, font_size=24, color=COLOR_GRAY_TXT,
        ).move_to(UP * 4.6)
        self.play(FadeIn(intro), run_time=0.4)

        # ---- 被除数数轴  370~390 ----
        nl1_label = Text("被除数 近似", font=FONT, font_size=22, color=COLOR_DIVIDEND).move_to(UP * 3.8)
        self.play(FadeIn(nl1_label), run_time=0.3)

        nl1 = NumberLine(
            x_range=[370, 395, 10],
            length=7.0,
            include_numbers=True,
            numbers_to_include=[370, 380, 390],
            font_size=24,
            color=WHITE,
            tick_size=0.1,
        ).move_to(UP * 3.0)

        self.play(Create(nl1), run_time=0.7)

        # 382 的点
        x_382 = nl1.n2p(382)
        dot_382 = Dot(x_382, color=COLOR_DIVIDEND, radius=0.12)
        label_382 = MathTex(r"382", font_size=30, color=COLOR_DIVIDEND).next_to(dot_382, UP, buff=0.2)
        self.play(FadeIn(dot_382), Write(label_382), run_time=0.5)

        # 380 的点
        x_380 = nl1.n2p(380)
        dot_380 = Dot(x_380, color=COLOR_HL, radius=0.12)
        label_380 = MathTex(r"380", font_size=30, color=COLOR_HL).next_to(dot_380, DOWN, buff=0.25)
        self.play(FadeIn(dot_380), Write(label_380), run_time=0.5)

        # 箭头: 382 → 380
        arr1 = CurvedArrow(
            dot_382.get_center(),
            dot_380.get_center(),
            angle=-0.6,
            color=COLOR_ARROW,
            stroke_width=3,
        )
        self.play(Create(arr1), run_time=0.6)
        near_text_1 = Text("近似!", font=FONT, font_size=20, color=COLOR_ARROW).move_to(UP * 2.35 + LEFT * 0.3)
        self.play(FadeIn(near_text_1), run_time=0.3)
        self.wait(0.5)

        # ---- 除数数轴  10~30 ----
        nl2_label = Text("除数 近似", font=FONT, font_size=22, color=COLOR_DIVISOR).move_to(UP * 1.3)
        self.play(FadeIn(nl2_label), run_time=0.3)

        nl2 = NumberLine(
            x_range=[10, 32, 10],
            length=7.0,
            include_numbers=True,
            numbers_to_include=[10, 20, 30],
            font_size=24,
            color=WHITE,
            tick_size=0.1,
        ).move_to(UP * 0.5)

        self.play(Create(nl2), run_time=0.7)

        # 19 的点
        x_19 = nl2.n2p(19)
        dot_19 = Dot(x_19, color=COLOR_DIVISOR, radius=0.12)
        label_19 = MathTex(r"19", font_size=30, color=COLOR_DIVISOR).next_to(dot_19, UP, buff=0.2)
        self.play(FadeIn(dot_19), Write(label_19), run_time=0.5)

        # 20 的点
        x_20 = nl2.n2p(20)
        dot_20 = Dot(x_20, color=COLOR_HL, radius=0.12)
        label_20 = MathTex(r"20", font_size=30, color=COLOR_HL).next_to(dot_20, DOWN, buff=0.25)
        self.play(FadeIn(dot_20), Write(label_20), run_time=0.5)

        # 箭头: 19 → 20
        arr2 = CurvedArrow(
            dot_19.get_center(),
            dot_20.get_center(),
            angle=-0.6,
            color=COLOR_ARROW,
            stroke_width=3,
        )
        self.play(Create(arr2), run_time=0.6)
        near_text_2 = Text("近似!", font=FONT, font_size=20, color=COLOR_ARROW).move_to(DOWN * 0.2 + RIGHT * 0.5)
        self.play(FadeIn(near_text_2), run_time=0.3)
        self.wait(0.5)

        # 结论框
        conclusion_bg = RoundedRectangle(
            width=7.5, height=1.6,
            corner_radius=0.3,
            color=COLOR_RESULT,
            stroke_width=2,
            fill_color=COLOR_RESULT,
            fill_opacity=0.1,
        ).move_to(DOWN * 2.2)

        conc_line1 = VGroup(
            MathTex(r"382 \div 19", font_size=34, color=WHITE),
            MathTex(r"\approx", font_size=34, color=COLOR_ARROW),
            MathTex(r"380 \div 20 = 19", font_size=34, color=COLOR_RESULT),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 2.0)
        conc_line1[0][0][0:3].set_color(COLOR_DIVIDEND)
        conc_line1[0][0][4:6].set_color(COLOR_DIVISOR)
        conc_line1[2][0][0:3].set_color(COLOR_DIVIDEND)
        conc_line1[2][0][4:6].set_color(COLOR_DIVISOR)
        conc_line1[2][0][7:9].set_color(COLOR_RESULT)

        conc_line2 = Text(
            "商大约是 19",
            font=FONT, font_size=26, color=COLOR_RESULT,
        ).move_to(DOWN * 2.8)

        self.play(FadeIn(conclusion_bg), run_time=0.4)
        self.play(Write(conc_line1), run_time=0.8)
        self.play(FadeIn(conc_line2, shift=UP * 0.2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(intro),
            FadeOut(nl1_label), FadeOut(nl1),
            FadeOut(dot_382), FadeOut(label_382),
            FadeOut(dot_380), FadeOut(label_380),
            FadeOut(arr1), FadeOut(near_text_1),
            FadeOut(nl2_label), FadeOut(nl2),
            FadeOut(dot_19), FadeOut(label_19),
            FadeOut(dot_20), FadeOut(label_20),
            FadeOut(arr2), FadeOut(near_text_2),
            FadeOut(conclusion_bg),
            FadeOut(conc_line1), FadeOut(conc_line2),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 5: 再举两个例子
    # ------------------------------------------------------------------

    def scene_5_more_examples(self):
        title = self.make_title_bar("再练一练!", color=COLOR_HL)
        self.play(Write(title), run_time=0.5)

        # ---- 例2: 245 ÷ 32 ----
        ex2_q = Text("例题 2", font=FONT, font_size=26, color=COLOR_ARROW).move_to(UP * 4.5)
        self.play(FadeIn(ex2_q), run_time=0.3)

        ex2_orig = MathTex(r"245 \div 32", font_size=48, color=WHITE).move_to(UP * 3.7)
        ex2_orig[0][0:3].set_color(COLOR_DIVIDEND)
        ex2_orig[0][4:6].set_color(COLOR_DIVISOR)
        self.play(Write(ex2_orig), run_time=0.6)

        # 步骤
        ex2_step1 = VGroup(
            MathTex(r"245 \approx 240", font_size=38, color=COLOR_DIVIDEND),
        ).move_to(UP * 2.7)
        ex2_step2 = VGroup(
            MathTex(r"32 \approx 30", font_size=38, color=COLOR_DIVISOR),
        ).move_to(UP * 1.9)
        ex2_step3 = MathTex(
            r"240 \div 30 = 8",
            font_size=44, color=WHITE,
        ).move_to(UP * 1.0)
        ex2_step3[0][0:3].set_color(COLOR_DIVIDEND)
        ex2_step3[0][4:6].set_color(COLOR_DIVISOR)
        ex2_step3[0][7].set_color(COLOR_RESULT)

        ex2_full = MathTex(
            r"245 \div 32 \approx 240 \div 30 = 8",
            font_size=34, color=WHITE,
        ).move_to(UP * 0.0)
        ex2_full[0][0:3].set_color(COLOR_DIVIDEND)
        ex2_full[0][4:6].set_color(COLOR_DIVISOR)
        ex2_full[0][7:10].set_color(COLOR_DIVIDEND)
        ex2_full[0][11:13].set_color(COLOR_DIVISOR)
        ex2_full[0][14].set_color(COLOR_RESULT)

        self.play(FadeIn(ex2_step1), run_time=0.5)
        self.play(FadeIn(ex2_step2), run_time=0.5)
        self.play(Write(ex2_step3), run_time=0.6)
        self.play(Write(ex2_full), run_time=0.7)

        result2 = Text("商大约是 8", font=FONT, font_size=28, color=COLOR_RESULT).move_to(DOWN * 0.9)
        self.play(FadeIn(result2, shift=UP * 0.2), run_time=0.4)
        self.wait(1.2)

        # 分割线
        sep = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_B, stroke_width=1).move_to(DOWN * 1.6)
        self.play(Create(sep), run_time=0.3)

        # ---- 例3: 563 ÷ 78 ----
        ex3_q = Text("例题 3", font=FONT, font_size=26, color=COLOR_ARROW).move_to(DOWN * 2.2)
        self.play(FadeIn(ex3_q), run_time=0.3)

        ex3_orig = MathTex(r"563 \div 78", font_size=48, color=WHITE).move_to(DOWN * 3.0)
        ex3_orig[0][0:3].set_color(COLOR_DIVIDEND)
        ex3_orig[0][4:6].set_color(COLOR_DIVISOR)
        self.play(Write(ex3_orig), run_time=0.6)

        ex3_full = MathTex(
            r"563 \div 78 \approx 560 \div 80 = 7",
            font_size=32, color=WHITE,
        ).move_to(DOWN * 4.0)
        ex3_full[0][0:3].set_color(COLOR_DIVIDEND)
        ex3_full[0][4:6].set_color(COLOR_DIVISOR)
        ex3_full[0][7:10].set_color(COLOR_DIVIDEND)
        ex3_full[0][11:13].set_color(COLOR_DIVISOR)
        ex3_full[0][14].set_color(COLOR_RESULT)

        self.play(Write(ex3_full), run_time=0.8)

        result3 = Text("商大约是 7", font=FONT, font_size=26, color=COLOR_RESULT).move_to(DOWN * 5.0)
        self.play(FadeIn(result3, shift=UP * 0.2), run_time=0.4)
        self.wait(2.0)

        self.play(
            FadeOut(title),
            FadeOut(ex2_q), FadeOut(ex2_orig),
            FadeOut(ex2_step1), FadeOut(ex2_step2),
            FadeOut(ex2_step3), FadeOut(ex2_full), FadeOut(result2),
            FadeOut(sep),
            FadeOut(ex3_q), FadeOut(ex3_orig),
            FadeOut(ex3_full), FadeOut(result3),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 6: 规律总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = self.make_title_bar("估算口诀", color=COLOR_HL)
        self.play(Write(title), run_time=0.5)

        # 总结卡片背景
        card_bg = RoundedRectangle(
            width=7.8, height=10.0,
            corner_radius=0.3,
            color=WHITE,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=0.05,
        ).move_to(DOWN * 0.5)
        self.play(FadeIn(card_bg), run_time=0.4)

        # --- 条目 1: 被除数近似 ---
        item1_title = Text(
            "1. 被除数近似为整十数",
            font=FONT, font_size=25, color=COLOR_DIVIDEND,
        )
        item1_ex = MathTex(
            r"382 \rightarrow 380",
            font_size=34, color=COLOR_DIVIDEND,
        )
        item1_ex[0][0:3].set_color(COLOR_DIVIDEND)
        item1_ex[0][-3:].set_color(COLOR_HL)
        item1 = VGroup(item1_title, item1_ex).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item1.move_to(UP * 3.2 + LEFT * 0.2)
        self.play(FadeIn(item1, shift=RIGHT * 0.3), run_time=0.5)

        # --- 条目 2: 除数近似 ---
        item2_title = Text(
            "2. 除数近似为整十数",
            font=FONT, font_size=25, color=COLOR_DIVISOR,
        )
        item2_ex = MathTex(
            r"19 \rightarrow 20",
            font_size=34, color=COLOR_DIVISOR,
        )
        item2_ex[0][0:2].set_color(COLOR_DIVISOR)
        item2_ex[0][-2:].set_color(COLOR_HL)
        item2 = VGroup(item2_title, item2_ex).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item2.move_to(UP * 1.6 + LEFT * 0.2)
        self.play(FadeIn(item2, shift=RIGHT * 0.3), run_time=0.5)

        # --- 条目 3: 口算结果 ---
        item3_title = Text(
            "3. 整十数口算得商",
            font=FONT, font_size=25, color=COLOR_RESULT,
        )
        item3_ex = MathTex(
            r"380 \div 20 = 19",
            font_size=34, color=WHITE,
        )
        item3_ex[0][0:3].set_color(COLOR_DIVIDEND)
        item3_ex[0][4:6].set_color(COLOR_DIVISOR)
        item3_ex[0][7:9].set_color(COLOR_RESULT)
        item3 = VGroup(item3_title, item3_ex).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item3.move_to(DOWN * 0.2 + LEFT * 0.2)
        self.play(FadeIn(item3, shift=RIGHT * 0.3), run_time=0.5)

        # --- 条目 4: 用途 ---
        item4_title = Text(
            "4. 估算帮助试商",
            font=FONT, font_size=25, color=COLOR_ARROW,
        )
        item4_body = Text(
            "确定商是几位数、大概是多少",
            font=FONT, font_size=20, color=COLOR_GRAY_TXT,
        )
        item4 = VGroup(item4_title, item4_body).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        item4.move_to(DOWN * 2.0 + LEFT * 0.2)
        self.play(FadeIn(item4, shift=RIGHT * 0.3), run_time=0.5)

        # 核心公式回顾
        core_formula = MathTex(
            r"382 \div 19 \approx 380 \div 20 = 19",
            font_size=30, color=WHITE,
        ).move_to(DOWN * 3.8)
        core_formula[0][0:3].set_color(COLOR_DIVIDEND)
        core_formula[0][4:6].set_color(COLOR_DIVISOR)
        core_formula[0][7:10].set_color(COLOR_DIVIDEND)
        core_formula[0][11:13].set_color(COLOR_DIVISOR)
        core_formula[0][14:16].set_color(COLOR_RESULT)

        self.play(Write(core_formula), run_time=0.8)

        # 强调重点
        hl_text = Text(
            "估算是笔算试商的基础!",
            font=FONT, font_size=26, color=COLOR_HL,
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(hl_text, shift=UP * 0.2), run_time=0.5)

        self.wait(3.0)

        self.play(
            FadeOut(title), FadeOut(card_bg),
            FadeOut(item1), FadeOut(item2),
            FadeOut(item3), FadeOut(item4),
            FadeOut(core_formula), FadeOut(hl_text),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B,
        ).move_to(UP * 0.5)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多数学技巧!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.5)

        # 装饰: 三个除法算式小卡片
        card_data = [
            (r"382 \div 19 \approx 19", COLOR_DIVIDEND),
            (r"245 \div 32 \approx 8",  COLOR_DIVISOR),
            (r"563 \div 78 \approx 7",  COLOR_RESULT),
        ]
        cards = VGroup()
        for tex, clr in card_data:
            m = MathTex(tex, font_size=24, color=clr)
            cards.add(m)
        cards.arrange(DOWN, buff=0.45).move_to(DOWN * 3.2)

        self.play(*[FadeIn(c, shift=RIGHT * 0.3) for c in cards], run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(author_big), FadeOut(author_id),
            FadeOut(follow), FadeOut(cards),
            run_time=1.0,
        )


# 运行命令:
# manim -qm 001_口算与估算除法.py MentalEstimateDivLesson   # 中等质量
# manim -qh 001_口算与估算除法.py MentalEstimateDivLesson   # 高质量
