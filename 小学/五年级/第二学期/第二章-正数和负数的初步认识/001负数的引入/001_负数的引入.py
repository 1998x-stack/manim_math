"""
001_负数的引入.py — 负数的引入 教学动画

知识点: 从温度、海拔、收支等现实情境引入负数
        正数前 + 可省略, 负数前 - 不能省略
        0 既不是正数, 也不是负数
年级: 五年级第二学期
格式: TikTok 竖屏 (1080x1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ======================================================================
# TikTok 竖屏配置
# ======================================================================
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

# ======================================================================
# 颜色常量
# ======================================================================
BG_COLOR     = "#1a1a2e"
COLOR_POS    = "#22c55e"   # 绿色 — 正数 / 正面
COLOR_NEG    = "#3b82f6"   # 蓝色 — 负数 / 负面
COLOR_ZERO   = "#f59e0b"   # 橙色 — 0 / 分界
COLOR_HL     = "#fbbf24"   # 黄色高亮
COLOR_RED    = "#ef4444"   # 红色强调
COLOR_PURPLE = "#a78bfa"   # 紫色装饰
COLOR_AUTHOR = "#6b7280"   # 灰色作者
FONT         = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class NegativeNumberLesson(Scene):
    """
    负数的引入 — 教学动画
    Scene 1: 开场钩子
    Scene 2: 温度情境 — 温度计可视化
    Scene 3: 海拔情境 — 海平面图
    Scene 4: 收支情境 — 盈亏可视化
    Scene 5: 正号省略 / 负号不可省略
    Scene 6: 0 是分界点
    Scene 7: 数轴总结
    Scene 8: 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_temperature()
        self.scene_3_altitude()
        self.scene_4_finance()
        self.scene_5_sign_rules()
        self.scene_6_zero_divider()
        self.scene_7_number_line_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """钩子: '比0还小的数？'"""

        # 作者信息 (顶部, 贯穿全程)
        self.author_mob = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_mob, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text(
            "负数", font=FONT, font_size=52,
            color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "比0还小的数？", font=FONT, font_size=36,
            color=COLOR_HL
        ).move_to(UP * 4.3)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.8)

        # 显示几个负数弹出
        neg_nums = VGroup(
            MathTex(r"-1", font_size=48, color=COLOR_NEG),
            MathTex(r"-5", font_size=48, color=COLOR_NEG),
            MathTex(r"-100", font_size=48, color=COLOR_NEG),
        )
        neg_nums[0].move_to(LEFT * 2.5 + UP * 2.0)
        neg_nums[1].move_to(UP * 2.0)
        neg_nums[2].move_to(RIGHT * 2.5 + UP * 2.0)

        self.play(
            *[FadeIn(n, scale=0.3) for n in neg_nums],
            run_time=0.6
        )
        self.play(
            *[Indicate(n, scale_factor=1.2, color=COLOR_HL) for n in neg_nums],
            run_time=0.5
        )
        self.wait(0.6)

        # 问题引导
        question = Text(
            "它们在生活中有什么用？",
            font=FONT, font_size=30, color=WHITE
        ).move_to(UP * 0.5)
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(VGroup(hook1, hook2, neg_nums, question)),
            run_time=0.4
        )

    # ------------------------------------------------------------------
    # Scene 2: 温度情境 — 温度计可视化
    # ------------------------------------------------------------------

    def scene_2_temperature(self):
        """温度计: 零上 vs 零下, -5℃ 表示零下5度"""

        title = Text(
            "情境一: 温度", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # === 温度计 ===
        # 外框
        therm_body = RoundedRectangle(
            width=1.2, height=7.0, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=WHITE, stroke_width=2
        ).move_to(LEFT * 2.5 + DOWN * 0.5)

        # 底部圆球
        therm_bulb = Circle(
            radius=0.55, fill_color=COLOR_RED, fill_opacity=0.9,
            stroke_color=WHITE, stroke_width=2
        ).move_to(LEFT * 2.5 + DOWN * 4.3)

        self.play(FadeIn(therm_body), FadeIn(therm_bulb), run_time=0.5)

        # 刻度线和标签 (从 -10 到 10, 间隔 5)
        therm_center_x = -2.5
        therm_bottom_y = -3.7
        therm_top_y = 2.8
        scale_marks = VGroup()
        scale_labels = VGroup()

        tick_values = [-10, -5, 0, 5, 10]
        for val in tick_values:
            frac = (val + 10) / 20.0
            y = therm_bottom_y + frac * (therm_top_y - therm_bottom_y)
            # tick mark
            tick = Line(
                start=np.array([therm_center_x - 0.45, y, 0]),
                end=np.array([therm_center_x + 0.45, y, 0]),
                color=WHITE if val != 0 else COLOR_ZERO,
                stroke_width=2 if val != 0 else 3
            )
            scale_marks.add(tick)
            # label
            lbl_color = COLOR_POS if val > 0 else (COLOR_NEG if val < 0 else COLOR_ZERO)
            lbl = MathTex(
                str(val), font_size=24, color=lbl_color
            ).next_to(tick, LEFT, buff=0.15)
            scale_labels.add(lbl)

        self.play(
            *[Create(m) for m in scale_marks],
            *[FadeIn(l) for l in scale_labels],
            run_time=0.8
        )

        # === 0°C 标记线 ===
        zero_y = therm_bottom_y + 0.5 * (therm_top_y - therm_bottom_y)
        zero_line = DashedLine(
            start=np.array([therm_center_x - 1.5, zero_y, 0]),
            end=np.array([therm_center_x + 1.5, zero_y, 0]),
            color=COLOR_ZERO, stroke_width=2, dash_length=0.1
        )
        zero_label = VGroup(
            MathTex(r"0", font_size=28, color=COLOR_ZERO),
            Text("℃", font=FONT, font_size=22, color=COLOR_ZERO)
        ).arrange(RIGHT, buff=0.05).next_to(zero_line, RIGHT, buff=0.2)

        self.play(Create(zero_line), FadeIn(zero_label), run_time=0.5)

        # === 零上零下标注 ===
        above_text = Text(
            "零上", font=FONT, font_size=24, color=COLOR_POS
        ).move_to(np.array([therm_center_x + 2.2, zero_y + 1.5, 0]))
        below_text = Text(
            "零下", font=FONT, font_size=24, color=COLOR_NEG
        ).move_to(np.array([therm_center_x + 2.2, zero_y - 1.5, 0]))
        above_arrow = Arrow(
            start=np.array([therm_center_x + 2.2, zero_y + 0.7, 0]),
            end=np.array([therm_center_x + 2.2, zero_y + 2.2, 0]),
            color=COLOR_POS, stroke_width=3, buff=0.05,
            max_tip_length_to_length_ratio=0.2
        )
        below_arrow = Arrow(
            start=np.array([therm_center_x + 2.2, zero_y - 0.7, 0]),
            end=np.array([therm_center_x + 2.2, zero_y - 2.2, 0]),
            color=COLOR_NEG, stroke_width=3, buff=0.05,
            max_tip_length_to_length_ratio=0.2
        )

        self.play(
            FadeIn(above_text), Create(above_arrow),
            FadeIn(below_text), Create(below_arrow),
            run_time=0.6
        )
        self.wait(0.4)

        # === 水银柱动画: 先升到 +5 ===
        def get_mercury(val):
            frac = (val + 10) / 20.0
            y_top = therm_bottom_y + frac * (therm_top_y - therm_bottom_y)
            h = y_top - therm_bottom_y
            if h < 0.1:
                h = 0.1
            bar = RoundedRectangle(
                width=0.6, height=h, corner_radius=0.1,
                fill_color=COLOR_RED, fill_opacity=0.8,
                stroke_width=0
            )
            bar.move_to(np.array([therm_center_x, therm_bottom_y + h / 2, 0]))
            return bar

        mercury = get_mercury(5)
        self.play(FadeIn(mercury), run_time=0.6)

        # +5℃ 标签
        pos_temp = VGroup(
            MathTex(r"+5", font_size=40, color=COLOR_POS),
            Text("℃", font=FONT, font_size=30, color=COLOR_POS)
        ).arrange(RIGHT, buff=0.05).move_to(RIGHT * 2.5 + UP * 2.5)

        pos_explain = Text(
            "零上5度 → 正数", font=FONT, font_size=26, color=COLOR_POS
        ).move_to(RIGHT * 2.5 + UP * 1.7)

        self.play(FadeIn(pos_temp, scale=1.1), run_time=0.5)
        self.play(FadeIn(pos_explain, shift=UP * 0.2), run_time=0.5)
        self.wait(0.6)

        # 水银降到 -5
        mercury_neg = get_mercury(-5)
        self.play(
            Transform(mercury, mercury_neg),
            run_time=1.2, rate_func=smooth
        )

        # -5℃ 标签
        neg_temp = VGroup(
            MathTex(r"-5", font_size=40, color=COLOR_NEG),
            Text("℃", font=FONT, font_size=30, color=COLOR_NEG)
        ).arrange(RIGHT, buff=0.05).move_to(RIGHT * 2.5 + DOWN * 1.5)

        neg_explain = Text(
            "零下5度 → 负数", font=FONT, font_size=26, color=COLOR_NEG
        ).move_to(RIGHT * 2.5 + DOWN * 2.3)

        self.play(FadeIn(neg_temp, scale=1.1), run_time=0.5)
        self.play(FadeIn(neg_explain, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 关键结论
        conclusion1 = VGroup(
            MathTex(r"-5", font_size=34, color=COLOR_NEG),
            Text("℃ 表示零下", font=FONT, font_size=28, color=WHITE),
            MathTex(r"5", font_size=34, color=COLOR_NEG),
            Text("℃", font=FONT, font_size=28, color=WHITE),
        ).arrange(RIGHT, buff=0.06).move_to(DOWN * 5.0)

        box1 = SurroundingRectangle(
            conclusion1, color=COLOR_NEG, stroke_width=2,
            buff=0.18, corner_radius=0.12
        )
        self.play(FadeIn(conclusion1), Create(box1), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, therm_body, therm_bulb,
                scale_marks, scale_labels,
                zero_line, zero_label,
                above_text, below_text, above_arrow, below_arrow,
                mercury, pos_temp, pos_explain,
                neg_temp, neg_explain,
                conclusion1, box1
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 3: 海拔情境 — 海平面图
    # ------------------------------------------------------------------

    def scene_3_altitude(self):
        """海平面图: 高于海平面 → 正, 低于海平面 → 负"""

        title = Text(
            "情境二: 海拔", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # === 海平面线 ===
        sea_y = 0.0
        sea_line = Line(
            start=np.array([-4.0, sea_y, 0]),
            end=np.array([4.0, sea_y, 0]),
            color=COLOR_ZERO, stroke_width=3
        )
        sea_label = Text(
            "海平面 (0m)", font=FONT, font_size=24, color=COLOR_ZERO
        ).next_to(sea_line, RIGHT, buff=0.2)

        # 水面波纹效果
        wave_points = []
        for x_val in np.linspace(-4.0, 4.0, 40):
            y_val = sea_y + 0.08 * np.sin(x_val * 3)
            wave_points.append(np.array([x_val, y_val, 0]))

        wave = VMobject(color="#38bdf8", stroke_width=2, stroke_opacity=0.5)
        wave.set_points_smoothly(wave_points)

        self.play(Create(sea_line), FadeIn(sea_label), Create(wave), run_time=0.7)

        # === 山 (高于海平面) ===
        mountain = Polygon(
            np.array([-3.0, sea_y, 0]),
            np.array([-1.5, 3.5, 0]),
            np.array([0.0, sea_y, 0]),
            fill_color="#4ade80", fill_opacity=0.35,
            stroke_color=COLOR_POS, stroke_width=2
        )
        mountain_label = Text(
            "珠穆朗玛峰", font=FONT, font_size=22, color=COLOR_POS
        ).move_to(np.array([-1.5, 2.5, 0]))

        height_label = VGroup(
            Text("海拔 ", font=FONT, font_size=24, color=COLOR_POS),
            MathTex(r"+8848", font_size=28, color=COLOR_POS),
            Text(" m", font=FONT, font_size=24, color=COLOR_POS)
        ).arrange(RIGHT, buff=0.05).move_to(np.array([-1.5, 4.2, 0]))

        up_arrow = Arrow(
            start=np.array([-1.5, sea_y + 0.2, 0]),
            end=np.array([-1.5, 3.3, 0]),
            color=COLOR_POS, stroke_width=3, buff=0.05,
            max_tip_length_to_length_ratio=0.12
        )

        self.play(FadeIn(mountain), run_time=0.5)
        self.play(
            FadeIn(mountain_label), Create(up_arrow),
            FadeIn(height_label),
            run_time=0.7
        )
        self.wait(0.5)

        # === 海沟 (低于海平面) ===
        trench = Polygon(
            np.array([1.0, sea_y, 0]),
            np.array([2.5, -3.5, 0]),
            np.array([4.0, sea_y, 0]),
            fill_color="#60a5fa", fill_opacity=0.35,
            stroke_color=COLOR_NEG, stroke_width=2
        )
        # 给海沟上面覆盖一层水色
        water_fill = Polygon(
            np.array([1.0, sea_y, 0]),
            np.array([4.0, sea_y, 0]),
            np.array([4.0, -3.5, 0]),
            np.array([1.0, -3.5, 0]),
            fill_color="#1e40af", fill_opacity=0.3,
            stroke_width=0
        )
        trench_label = Text(
            "吐鲁番盆地", font=FONT, font_size=22, color=COLOR_NEG
        ).move_to(np.array([2.5, -2.0, 0]))

        depth_label = VGroup(
            Text("海拔 ", font=FONT, font_size=24, color=COLOR_NEG),
            MathTex(r"-155", font_size=28, color=COLOR_NEG),
            Text(" m", font=FONT, font_size=24, color=COLOR_NEG)
        ).arrange(RIGHT, buff=0.05).move_to(np.array([2.5, -4.2, 0]))

        down_arrow = Arrow(
            start=np.array([2.5, sea_y - 0.2, 0]),
            end=np.array([2.5, -3.3, 0]),
            color=COLOR_NEG, stroke_width=3, buff=0.05,
            max_tip_length_to_length_ratio=0.12
        )

        self.play(FadeIn(water_fill), FadeIn(trench), run_time=0.5)
        self.play(
            FadeIn(trench_label), Create(down_arrow),
            FadeIn(depth_label),
            run_time=0.7
        )
        self.wait(0.5)

        # 关键结论
        conclusion2 = VGroup(
            MathTex(r"-155", font_size=32, color=COLOR_NEG),
            Text(" m 表示低于海平面 ", font=FONT, font_size=26, color=WHITE),
            MathTex(r"155", font_size=32, color=COLOR_NEG),
            Text(" m", font=FONT, font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 5.5)

        box2 = SurroundingRectangle(
            conclusion2, color=COLOR_NEG, stroke_width=2,
            buff=0.18, corner_radius=0.12
        )
        self.play(FadeIn(conclusion2), Create(box2), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, sea_line, sea_label, wave,
                mountain, mountain_label, height_label, up_arrow,
                water_fill, trench, trench_label, depth_label, down_arrow,
                conclusion2, box2
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 4: 收支情境 — 盈亏可视化
    # ------------------------------------------------------------------

    def scene_4_finance(self):
        """盈利 → 正数, 亏损 → 负数"""

        title = Text(
            "情境三: 收支", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # === 钱包图标 (简化为矩形) ===
        wallet = RoundedRectangle(
            width=3.5, height=2.0, corner_radius=0.25,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=COLOR_HL, stroke_width=2
        ).move_to(UP * 3.0)
        wallet_label = Text(
            "小明的零花钱", font=FONT, font_size=28, color=WHITE
        ).move_to(UP * 3.0)
        self.play(FadeIn(wallet), Write(wallet_label), run_time=0.6)

        # === 盈利场景 ===
        profit_box = RoundedRectangle(
            width=3.5, height=2.8, corner_radius=0.2,
            fill_color="#052e16", fill_opacity=0.6,
            stroke_color=COLOR_POS, stroke_width=2
        ).move_to(LEFT * 2.3 + DOWN * 0.2)

        profit_title = Text(
            "收入", font=FONT, font_size=30, color=COLOR_POS, weight=BOLD
        ).move_to(LEFT * 2.3 + UP * 0.8)

        profit_icon = Text(
            "+", font=FONT, font_size=60, color=COLOR_POS, weight=BOLD
        ).move_to(LEFT * 2.3 + DOWN * 0.1)

        profit_amount = VGroup(
            MathTex(r"+200", font_size=36, color=COLOR_POS),
            Text(" 元", font=FONT, font_size=28, color=COLOR_POS)
        ).arrange(RIGHT, buff=0.05).move_to(LEFT * 2.3 + DOWN * 0.9)

        profit_explain = Text(
            "赚了200元", font=FONT, font_size=22, color=COLOR_POS
        ).move_to(LEFT * 2.3 + DOWN * 1.5)

        self.play(FadeIn(profit_box), run_time=0.3)
        self.play(
            Write(profit_title), FadeIn(profit_icon, scale=0.5),
            run_time=0.5
        )
        self.play(FadeIn(profit_amount), FadeIn(profit_explain), run_time=0.5)
        self.wait(0.3)

        # === 亏损场景 ===
        loss_box = RoundedRectangle(
            width=3.5, height=2.8, corner_radius=0.2,
            fill_color="#1e1b4b", fill_opacity=0.6,
            stroke_color=COLOR_NEG, stroke_width=2
        ).move_to(RIGHT * 2.3 + DOWN * 0.2)

        loss_title = Text(
            "支出", font=FONT, font_size=30, color=COLOR_NEG, weight=BOLD
        ).move_to(RIGHT * 2.3 + UP * 0.8)

        loss_icon = Text(
            "-", font=FONT, font_size=60, color=COLOR_NEG, weight=BOLD
        ).move_to(RIGHT * 2.3 + DOWN * 0.1)

        loss_amount = VGroup(
            MathTex(r"-100", font_size=36, color=COLOR_NEG),
            Text(" 元", font=FONT, font_size=28, color=COLOR_NEG)
        ).arrange(RIGHT, buff=0.05).move_to(RIGHT * 2.3 + DOWN * 0.9)

        loss_explain = Text(
            "亏了100元", font=FONT, font_size=22, color=COLOR_NEG
        ).move_to(RIGHT * 2.3 + DOWN * 1.5)

        self.play(FadeIn(loss_box), run_time=0.3)
        self.play(
            Write(loss_title), FadeIn(loss_icon, scale=0.5),
            run_time=0.5
        )
        self.play(FadeIn(loss_amount), FadeIn(loss_explain), run_time=0.5)
        self.wait(0.5)

        # === VS 标志 ===
        vs_text = Text(
            "VS", font=FONT, font_size=36, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 0.2)
        self.play(FadeIn(vs_text, scale=0.5), run_time=0.4)

        # 关键结论
        conclusion3 = VGroup(
            MathTex(r"-100", font_size=32, color=COLOR_NEG),
            Text(" 表示亏损 ", font=FONT, font_size=26, color=WHITE),
            MathTex(r"100", font_size=32, color=COLOR_NEG),
            Text(" 元", font=FONT, font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 3.5)

        box3 = SurroundingRectangle(
            conclusion3, color=COLOR_NEG, stroke_width=2,
            buff=0.18, corner_radius=0.12
        )
        self.play(FadeIn(conclusion3), Create(box3), run_time=0.6)
        self.wait(0.5)

        # 总结: 正负数表示意义相反的量
        summary_text = Text(
            "正数和负数表示意义相反的量！",
            font=FONT, font_size=30, color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 5.0)
        self.play(FadeIn(summary_text, shift=UP * 0.3), run_time=0.6)
        self.play(Indicate(summary_text, color=COLOR_HL), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, wallet, wallet_label,
                profit_box, profit_title, profit_icon,
                profit_amount, profit_explain,
                loss_box, loss_title, loss_icon,
                loss_amount, loss_explain,
                vs_text, conclusion3, box3, summary_text
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 5: 正号省略 / 负号不可省略
    # ------------------------------------------------------------------

    def scene_5_sign_rules(self):
        """正数的+可以省略, 负数的-不能省略"""

        title = Text(
            "书写规则", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # === 规则一: 正号可省略 ===
        rule1_box = RoundedRectangle(
            width=7.5, height=3.0, corner_radius=0.25,
            fill_color="#052e16", fill_opacity=0.5,
            stroke_color=COLOR_POS, stroke_width=2
        ).move_to(UP * 2.5)

        rule1_title = Text(
            "规则一: 正数", font=FONT, font_size=30,
            color=COLOR_POS, weight=BOLD
        ).move_to(UP * 3.5)

        # +5 = 5
        plus5 = MathTex(r"+5", font_size=56, color=COLOR_POS).move_to(LEFT * 2.0 + UP * 2.3)
        equals1 = MathTex(r"=", font_size=44, color=WHITE).move_to(UP * 2.3)
        five = MathTex(r"5", font_size=56, color=COLOR_POS).move_to(RIGHT * 2.0 + UP * 2.3)

        # 划掉 + 号的效果
        cross_line = Line(
            start=plus5.get_left() + LEFT * 0.05 + UP * 0.15,
            end=plus5.get_left() + RIGHT * 0.4 + DOWN * 0.15,
            color=COLOR_RED, stroke_width=4
        )

        rule1_note = Text(
            "正号 \"+\" 可以省略不写",
            font=FONT, font_size=24, color=COLOR_POS
        ).move_to(UP * 1.5)

        self.play(FadeIn(rule1_box), Write(rule1_title), run_time=0.5)
        self.play(Write(plus5), run_time=0.4)
        self.play(Create(cross_line), run_time=0.4)
        self.play(Write(equals1), Write(five), run_time=0.5)
        self.play(FadeIn(rule1_note, shift=UP * 0.2), run_time=0.4)
        self.wait(0.6)

        # === 规则二: 负号不可省略 ===
        rule2_box = RoundedRectangle(
            width=7.5, height=3.0, corner_radius=0.25,
            fill_color="#1e1b4b", fill_opacity=0.5,
            stroke_color=COLOR_NEG, stroke_width=2
        ).move_to(DOWN * 1.5)

        rule2_title = Text(
            "规则二: 负数", font=FONT, font_size=30,
            color=COLOR_NEG, weight=BOLD
        ).move_to(DOWN * 0.5)

        neg5 = MathTex(r"-5", font_size=56, color=COLOR_NEG).move_to(DOWN * 1.7)

        # 负号上方强调框
        neg_sign_rect = SurroundingRectangle(
            neg5[0][0],  # 只框住负号
            color=COLOR_RED, stroke_width=3,
            buff=0.1, corner_radius=0.08
        )

        rule2_note = Text(
            "负号 \"-\" 不能省略！",
            font=FONT, font_size=24, color=COLOR_RED, weight=BOLD
        ).move_to(DOWN * 2.6)

        self.play(FadeIn(rule2_box), Write(rule2_title), run_time=0.5)
        self.play(Write(neg5), run_time=0.4)
        self.play(Create(neg_sign_rect), run_time=0.4)
        self.play(
            FadeIn(rule2_note, shift=UP * 0.2),
            run_time=0.5
        )
        self.play(
            Indicate(neg_sign_rect, scale_factor=1.15, color=COLOR_RED),
            run_time=0.5
        )
        self.wait(0.4)

        # 错误示范
        wrong = VGroup(
            MathTex(r"5", font_size=40, color=GRAY_B),
            Text(" ← 这是正数5, 不是负数!", font=FONT, font_size=22, color=COLOR_RED),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 3.8)

        self.play(FadeIn(wrong, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title,
                rule1_box, rule1_title, plus5, equals1, five,
                cross_line, rule1_note,
                rule2_box, rule2_title, neg5, neg_sign_rect,
                rule2_note, wrong
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 6: 0 是分界点
    # ------------------------------------------------------------------

    def scene_6_zero_divider(self):
        """0 既不是正数, 也不是负数, 是分界点"""

        title = Text(
            "0 的特殊地位", font=FONT, font_size=40,
            color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # === 大大的 0 ===
        big_zero = MathTex(
            r"0", font_size=120, color=COLOR_ZERO
        ).move_to(UP * 3.0)
        zero_glow = Circle(
            radius=1.2, color=COLOR_ZERO, stroke_width=3,
            fill_color=COLOR_ZERO, fill_opacity=0.1
        ).move_to(UP * 3.0)

        self.play(FadeIn(zero_glow), Write(big_zero), run_time=0.7)
        self.play(
            Indicate(big_zero, scale_factor=1.15, color=COLOR_ZERO),
            run_time=0.5
        )

        # === 三条性质 ===
        prop1 = Text(
            "0 不是正数", font=FONT, font_size=30, color=COLOR_POS
        ).move_to(UP * 0.8)
        cross1 = Line(
            prop1.get_left() + LEFT * 0.1,
            prop1.get_right() + RIGHT * 0.1,
            color=COLOR_RED, stroke_width=3
        )

        prop2 = Text(
            "0 不是负数", font=FONT, font_size=30, color=COLOR_NEG
        ).move_to(DOWN * 0.2)
        cross2 = Line(
            prop2.get_left() + LEFT * 0.1,
            prop2.get_right() + RIGHT * 0.1,
            color=COLOR_RED, stroke_width=3
        )

        prop3 = Text(
            "0 是正数和负数的分界点",
            font=FONT, font_size=32, color=COLOR_ZERO, weight=BOLD
        ).move_to(DOWN * 1.5)

        self.play(Write(prop1), run_time=0.5)
        self.play(Create(cross1), run_time=0.3)
        self.wait(0.3)

        self.play(Write(prop2), run_time=0.5)
        self.play(Create(cross2), run_time=0.3)
        self.wait(0.3)

        self.play(Write(prop3), run_time=0.7)
        self.play(Indicate(prop3, color=COLOR_ZERO), run_time=0.5)
        self.wait(0.4)

        # === 分界图示 (简化数轴) ===
        divider_line = Line(
            start=np.array([-3.5, -3.5, 0]),
            end=np.array([3.5, -3.5, 0]),
            color=WHITE, stroke_width=2
        )
        zero_dot = Dot(
            point=np.array([0, -3.5, 0]),
            radius=0.15, color=COLOR_ZERO
        )
        zero_lbl = MathTex(
            r"0", font_size=30, color=COLOR_ZERO
        ).next_to(zero_dot, DOWN, buff=0.15)

        # 负数区域
        neg_region = RoundedRectangle(
            width=3.2, height=0.8, corner_radius=0.15,
            fill_color=COLOR_NEG, fill_opacity=0.2,
            stroke_color=COLOR_NEG, stroke_width=1.5
        ).move_to(np.array([-1.85, -3.5, 0]))
        neg_text = Text(
            "负数", font=FONT, font_size=22, color=COLOR_NEG
        ).move_to(np.array([-1.85, -4.4, 0]))

        # 正数区域
        pos_region = RoundedRectangle(
            width=3.2, height=0.8, corner_radius=0.15,
            fill_color=COLOR_POS, fill_opacity=0.2,
            stroke_color=COLOR_POS, stroke_width=1.5
        ).move_to(np.array([1.85, -3.5, 0]))
        pos_text = Text(
            "正数", font=FONT, font_size=22, color=COLOR_POS
        ).move_to(np.array([1.85, -4.4, 0]))

        self.play(
            Create(divider_line), FadeIn(zero_dot),
            FadeIn(zero_lbl),
            run_time=0.5
        )
        self.play(
            FadeIn(neg_region), FadeIn(neg_text),
            FadeIn(pos_region), FadeIn(pos_text),
            run_time=0.6
        )

        # 0不属于任何一边的箭头
        left_arr = Arrow(
            start=np.array([0, -4.8, 0]),
            end=np.array([-1.0, -4.8, 0]),
            color=COLOR_NEG, stroke_width=2, buff=0.05,
            max_tip_length_to_length_ratio=0.25
        )
        right_arr = Arrow(
            start=np.array([0, -4.8, 0]),
            end=np.array([1.0, -4.8, 0]),
            color=COLOR_POS, stroke_width=2, buff=0.05,
            max_tip_length_to_length_ratio=0.25
        )
        divider_note = Text(
            "分界", font=FONT, font_size=20, color=COLOR_ZERO
        ).move_to(np.array([0, -5.2, 0]))

        self.play(
            Create(left_arr), Create(right_arr),
            FadeIn(divider_note),
            run_time=0.5
        )
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, big_zero, zero_glow,
                prop1, cross1, prop2, cross2, prop3,
                divider_line, zero_dot, zero_lbl,
                neg_region, neg_text, pos_region, pos_text,
                left_arr, right_arr, divider_note
            )),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # Scene 7: 数轴总结
    # ------------------------------------------------------------------

    def scene_7_number_line_summary(self):
        """用完整数轴总结所有知识点"""

        title = Text(
            "总结: 数轴上的正数和负数",
            font=FONT, font_size=36, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # === 数轴 ===
        number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=8,
            color=WHITE,
            include_numbers=False,
            include_tip=True,
            tip_length=0.2,
            stroke_width=2.5
        ).move_to(UP * 3.0)

        self.play(Create(number_line), run_time=0.8)

        # 逐个标数字
        num_mobs = VGroup()
        dot_mobs = VGroup()
        for i in range(-5, 6):
            pos = number_line.n2p(i)
            dot = Dot(pos, radius=0.08, color=WHITE)
            if i < 0:
                color = COLOR_NEG
            elif i > 0:
                color = COLOR_POS
            else:
                color = COLOR_ZERO
            lbl = MathTex(str(i), font_size=26, color=color)
            lbl.next_to(dot, DOWN, buff=0.2)
            num_mobs.add(lbl)
            dot_mobs.add(dot)

        self.play(
            *[FadeIn(d) for d in dot_mobs],
            run_time=0.5
        )
        self.play(
            *[FadeIn(n, shift=UP * 0.1) for n in num_mobs],
            run_time=0.6
        )
        self.wait(0.3)

        # === 标注三个区域 ===
        neg_brace = Brace(
            VGroup(dot_mobs[0], dot_mobs[4]),  # -5 to -1
            direction=UP, color=COLOR_NEG
        )
        neg_brace_lbl = Text(
            "负数", font=FONT, font_size=26, color=COLOR_NEG
        ).next_to(neg_brace, UP, buff=0.1)

        pos_brace = Brace(
            VGroup(dot_mobs[6], dot_mobs[10]),  # 1 to 5
            direction=UP, color=COLOR_POS
        )
        pos_brace_lbl = Text(
            "正数", font=FONT, font_size=26, color=COLOR_POS
        ).next_to(pos_brace, UP, buff=0.1)

        zero_circle = Circle(
            radius=0.25, color=COLOR_ZERO, stroke_width=3
        ).move_to(number_line.n2p(0))
        zero_note = Text(
            "分界点", font=FONT, font_size=20, color=COLOR_ZERO
        ).next_to(zero_circle, UP, buff=0.35)

        self.play(
            FadeIn(neg_brace), FadeIn(neg_brace_lbl),
            FadeIn(pos_brace), FadeIn(pos_brace_lbl),
            run_time=0.6
        )
        self.play(Create(zero_circle), FadeIn(zero_note), run_time=0.5)
        self.wait(0.5)

        # === 知识总结框 ===
        summary_box = RoundedRectangle(
            width=8.0, height=6.5, corner_radius=0.3,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(summary_box), run_time=0.3)

        summary_title = Text(
            "本课要点", font=FONT, font_size=32,
            color=COLOR_HL, weight=BOLD
        ).move_to(DOWN * 0.2)
        self.play(Write(summary_title), run_time=0.4)

        # 四条总结
        points = [
            ("1.", "负数用来表示与正数意义相反的量", COLOR_NEG),
            ("2.", "正数前的\"+\"可以省略", COLOR_POS),
            ("3.", "负数前的\"-\"不能省略", COLOR_RED),
            ("4.", "0既不是正数, 也不是负数", COLOR_ZERO),
        ]

        point_mobs = VGroup()
        for idx, (num, text, color) in enumerate(points):
            num_mob = Text(
                num, font=FONT, font_size=26, color=color, weight=BOLD
            )
            text_mob = Text(
                text, font=FONT, font_size=24, color=WHITE
            )
            row = VGroup(num_mob, text_mob).arrange(RIGHT, buff=0.15)
            row.move_to(DOWN * (0.9 + idx * 0.9))
            point_mobs.add(row)

        for p in point_mobs:
            self.play(FadeIn(p, shift=LEFT * 0.3), run_time=0.5)
            self.wait(0.2)

        # 强调框
        emphasis_rect = SurroundingRectangle(
            point_mobs, color=COLOR_HL, stroke_width=2,
            buff=0.2, corner_radius=0.12
        )
        self.play(Create(emphasis_rect), run_time=0.4)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(VGroup(
                title, number_line, num_mobs, dot_mobs,
                neg_brace, neg_brace_lbl,
                pos_brace, pos_brace_lbl,
                zero_circle, zero_note,
                summary_box, summary_title,
                point_mobs, emphasis_rect
            )),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        """作者信息放大 + 关注提示"""

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

        # 装饰: 正负数交替飘动
        deco_nums = VGroup()
        deco_values = ["-3", "+2", "-7", "+4", "-1", "+6"]
        deco_colors = [COLOR_NEG, COLOR_POS, COLOR_NEG, COLOR_POS, COLOR_NEG, COLOR_POS]
        for i, (val, c) in enumerate(zip(deco_values, deco_colors)):
            angle = i * PI / 3
            m = MathTex(val, font_size=32, color=c)
            m.move_to(
                DOWN * 2.8 + np.array([
                    np.cos(angle) * 2.5,
                    np.sin(angle) * 1.0,
                    0.0
                ])
            )
            m.set_opacity(0.7)
            deco_nums.add(m)

        self.play(*[FadeIn(n, scale=0.3) for n in deco_nums], run_time=0.5)
        self.play(
            Rotate(deco_nums, angle=2 * PI / 3, run_time=1.2, rate_func=smooth)
        )
        self.wait(0.8)

        self.play(
            FadeOut(VGroup(self.author_mob, author_id, follow, deco_nums)),
            run_time=0.8
        )


# ======================================================================
# 渲染命令:
#   快速预览: manim -pql 001_负数的引入.py NegativeNumberLesson
#   高质量:   manim -qh  001_负数的引入.py NegativeNumberLesson
#   4K:       manim -qk  001_负数的引入.py NegativeNumberLesson
# ======================================================================
