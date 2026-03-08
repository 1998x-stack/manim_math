"""
认识千克 - 二年级数学教学动画
Understanding Kilograms - 2nd Grade Math Teaching Animation

目标受众: 小学二年级学生
格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
  快速预览: manim -pql kilogram.py UnderstandKilogram
  高质量:   manim -qh  kilogram.py UnderstandKilogram
"""

from manim import *
import numpy as np

# ──────────────────────────────────────────────
# 全局配置 - TikTok 竖屏
# ──────────────────────────────────────────────
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16


class UnderstandKilogram(Scene):
    """
    认识千克 教学动画

    场景顺序:
      1. 开场钩子
      2. 认识千克单位
      3. 两瓶矿泉水 ≈ 1kg
      4. 四个苹果 ≈ 1kg
      5. 用电子秤称量
      6. 知识总结
      7. 片尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # ── 配色方案 ──────────────────────────
        self.C_TITLE     = GOLD
        self.C_HIGHLIGHT = "#FFD700"
        self.C_WATER     = "#29B6F6"
        self.C_APPLE     = "#E53935"
        self.C_KG        = "#A5D6A7"
        self.C_SCALE     = "#546E7A"
        self.C_TEXT      = WHITE
        self.C_GRAY      = GRAY_A
        self.FONT        = "Noto Sans CJK SC"

        # ── 执行场景序列 ──────────────────────
        self.scene_1_hook()
        self.scene_2_kg_definition()
        self.scene_3_water_bottles()
        self.scene_4_apples()
        self.scene_5_scale()
        self.scene_6_summary()
        self.scene_7_outro()

    # ══════════════════════════════════════════
    # 工具函数
    # ══════════════════════════════════════════

    def _author_bar(self):
        """顶部作者信息条"""
        bar = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT, font_size=20, color=GRAY_B
        ).move_to(UP * 7.2)
        return bar

    def _make_water_bottle(self, position=ORIGIN, color=None):
        """创建矿泉水瓶（基础图形拼合）"""
        if color is None:
            color = self.C_WATER

        body = RoundedRectangle(
            corner_radius=0.22, width=0.85, height=1.6,
            fill_color=color, fill_opacity=0.75,
            stroke_color=WHITE, stroke_width=2.5
        )
        neck = Rectangle(
            width=0.42, height=0.38,
            fill_color=color, fill_opacity=0.85,
            stroke_color=WHITE, stroke_width=2
        )
        neck.next_to(body, UP, buff=0)
        cap = Rectangle(
            width=0.48, height=0.22,
            fill_color="#BDBDBD", fill_opacity=1,
            stroke_color=WHITE, stroke_width=1.5
        )
        cap.next_to(neck, UP, buff=0)

        # 水位线
        water_fill = Rectangle(
            width=0.72, height=1.1,
            fill_color=color, fill_opacity=0.4,
            stroke_width=0
        )
        water_fill.move_to(body.get_center() + DOWN * 0.15)

        label = Text("500ml", font=self.FONT, font_size=15, color=WHITE)
        label.move_to(body.get_center())

        bottle = VGroup(body, water_fill, neck, cap, label)
        bottle.move_to(position)
        return bottle

    def _make_apple(self, position=ORIGIN, color=None):
        """创建苹果（Circle + 茎 + 叶）"""
        if color is None:
            color = self.C_APPLE

        body = Circle(
            radius=0.48,
            fill_color=color, fill_opacity=0.92,
            stroke_color=WHITE, stroke_width=2
        )
        # 顶部凹陷
        dent = Circle(
            radius=0.1, fill_color=color, fill_opacity=1, stroke_width=0
        )
        dent.move_to(body.get_top() + DOWN * 0.05)

        stem = Line(
            body.get_top() + DOWN * 0.02,
            body.get_top() + UP * 0.28,
            stroke_color="#5D4037", stroke_width=4
        )
        leaf = Ellipse(
            width=0.35, height=0.18,
            fill_color="#4CAF50", fill_opacity=1, stroke_width=0
        )
        leaf.move_to(stem.get_end() + RIGHT * 0.18 + DOWN * 0.06)
        leaf.rotate(PI / 5)

        apple = VGroup(body, dent, stem, leaf)
        apple.move_to(position)
        return apple

    def _make_electronic_scale(self, value_str="0", position=ORIGIN):
        """创建电子秤"""
        # 主机体
        body = RoundedRectangle(
            corner_radius=0.3, width=3.8, height=2.6,
            fill_color="#263238", fill_opacity=1,
            stroke_color="#546E7A", stroke_width=3
        )
        # 显示屏
        screen = RoundedRectangle(
            corner_radius=0.15, width=2.8, height=1.1,
            fill_color="#1B5E20", fill_opacity=1,
            stroke_color="#A5D6A7", stroke_width=2.5
        )
        screen.move_to(body.get_center() + UP * 0.4)

        # 数字
        num = Text(value_str, font=self.FONT, font_size=52, color="#A5D6A7", weight=BOLD)
        num.move_to(screen.get_center() + LEFT * 0.5)

        # 单位
        unit = Text("kg", font=self.FONT, font_size=28, color="#66BB6A")
        unit.move_to(screen.get_center() + RIGHT * 0.75)

        # 平台面板
        platform = Rectangle(
            width=3.5, height=0.22,
            fill_color="#455A64", fill_opacity=1,
            stroke_color="#78909C", stroke_width=2
        )
        platform.next_to(body, DOWN, buff=-0.25)

        # 标签
        label = Text("电子秤", font=self.FONT, font_size=20, color=GRAY_A)
        label.move_to(body.get_center() + DOWN * 0.72)

        # 按钮装饰
        btn1 = Circle(radius=0.12, fill_color="#37474F", fill_opacity=1,
                      stroke_color="#78909C", stroke_width=1)
        btn2 = Circle(radius=0.12, fill_color="#37474F", fill_opacity=1,
                      stroke_color="#78909C", stroke_width=1)
        btn1.move_to(body.get_center() + LEFT * 0.4 + DOWN * 0.75)
        btn2.move_to(body.get_center() + RIGHT * 0.4 + DOWN * 0.75)

        scale = VGroup(body, screen, num, unit, platform, label, btn1, btn2)
        scale.move_to(position)
        return scale

    def _result_box(self, position=ORIGIN):
        """创建 ≈1千克 结果框"""
        box = RoundedRectangle(
            corner_radius=0.35, width=4.2, height=1.5,
            fill_color="#1B5E20", fill_opacity=0.85,
            stroke_color="#A5D6A7", stroke_width=3
        )
        box.move_to(position)

        content = VGroup(
            Text("≈", font=self.FONT, font_size=48, color=WHITE),
            Text("1", font=self.FONT, font_size=64, color=self.C_KG, weight=BOLD),
            Text("千克", font=self.FONT, font_size=40, color=WHITE),
        ).arrange(RIGHT, buff=0.25)
        content.move_to(box.get_center())

        return VGroup(box, content)

    def _info_card(self, main, sub, bg_color, stroke_color, y_pos):
        """创建总结卡片"""
        bg = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=1.7,
            fill_color=bg_color, fill_opacity=0.65,
            stroke_color=stroke_color, stroke_width=2.5
        )
        bg.move_to(UP * y_pos)

        main_t = Text(main, font=self.FONT, font_size=30, color=WHITE, weight=BOLD)
        main_t.move_to(bg.get_center() + UP * 0.33)

        sub_t = Text(sub, font=self.FONT, font_size=22, color=GRAY_A)
        sub_t.move_to(bg.get_center() + DOWN * 0.33)

        return VGroup(bg, main_t, sub_t)

    # ══════════════════════════════════════════
    # Scene 1: 开场钩子
    # ══════════════════════════════════════════

    def scene_1_hook(self):
        # 作者信息
        self.author_bar = self._author_bar()
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.4)

        # 钩子文字
        hook1 = Text("1千克", font=self.FONT, font_size=88,
                     color=self.C_TITLE, weight=BOLD)
        hook2 = Text("到底有多重？", font=self.FONT, font_size=50, color=WHITE)
        hook_grp = VGroup(hook1, hook2).arrange(DOWN, buff=0.4)
        hook_grp.move_to(UP * 4.2)

        self.play(Write(hook1), run_time=0.8)
        self.play(FadeIn(hook2, shift=UP * 0.3), run_time=0.6)

        # 演示物品
        bottle = self._make_water_bottle(position=LEFT * 1.7 + UP * 1.2)
        apple  = self._make_apple(position=RIGHT * 1.7 + UP * 1.2)

        q_marks = VGroup(
            Text("?", font=self.FONT, font_size=44, color=YELLOW).move_to(LEFT * 1.7 + UP * 2.8),
            Text("?", font=self.FONT, font_size=44, color=YELLOW).move_to(RIGHT * 1.7 + UP * 2.8),
        )

        self.play(GrowFromCenter(bottle), GrowFromCenter(apple), run_time=0.7)
        self.play(FadeIn(q_marks), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(bottle), FadeOut(apple), FadeOut(q_marks),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 2: 认识千克单位
    # ══════════════════════════════════════════

    def scene_2_kg_definition(self):
        title = Text("认识千克", font=self.FONT, font_size=54,
                     color=self.C_TITLE, weight=BOLD)
        title.move_to(UP * 5.9)
        self.play(Write(title), run_time=0.7)

        # KG 大图标
        circle = Circle(
            radius=1.55,
            fill_color="#1565C0", fill_opacity=0.88,
            stroke_color=GOLD, stroke_width=6
        )
        circle.move_to(UP * 3.5)

        kg_text = Text("kg", font=self.FONT, font_size=84, color=WHITE, weight=BOLD)
        kg_text.move_to(circle.get_center())

        self.play(GrowFromCenter(circle), run_time=0.6)
        self.play(Write(kg_text), run_time=0.6)
        self.play(Flash(circle, color=GOLD, flash_radius=2.0), run_time=0.5)

        # 等号说明
        arr = Arrow(UP * 1.7, UP * 1.1, color=GRAY_B, stroke_width=3, max_tip_length_to_length_ratio=0.2)
        self.play(Create(arr), run_time=0.4)

        eq_row = VGroup(
            Text("千克", font=self.FONT, font_size=38, color=YELLOW),
            Text("=", font=self.FONT, font_size=38, color=WHITE),
            Text("kg", font=self.FONT, font_size=38, color=self.C_KG, weight=BOLD),
        ).arrange(RIGHT, buff=0.35)
        eq_row.move_to(UP * 0.7)
        self.play(FadeIn(eq_row, shift=UP * 0.3), run_time=0.6)

        # 信息框
        info_bg = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=1.8,
            fill_color="#0D47A1", fill_opacity=0.45,
            stroke_color=BLUE_C, stroke_width=2
        )
        info_bg.move_to(DOWN * 0.7)

        info1 = Text("千克是计量质量的单位", font=self.FONT,
                     font_size=30, color=WHITE)
        info2 = Text('也叫做"公斤"', font=self.FONT,
                     font_size=26, color=GRAY_A)
        VGroup(info1, info2).arrange(DOWN, buff=0.25).move_to(info_bg.get_center())

        self.play(FadeIn(info_bg), run_time=0.4)
        self.play(Write(info1), run_time=0.6)
        self.play(FadeIn(info2), run_time=0.5)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(circle), FadeOut(kg_text),
            FadeOut(arr), FadeOut(eq_row),
            FadeOut(info_bg), FadeOut(info1), FadeOut(info2),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 3: 两瓶矿泉水 ≈ 1kg
    # ══════════════════════════════════════════

    def scene_3_water_bottles(self):
        title = Text("生活中的1千克", font=self.FONT, font_size=48,
                     color=self.C_TITLE, weight=BOLD)
        title.move_to(UP * 5.9)
        sub = Text("两瓶500毫升矿泉水", font=self.FONT, font_size=32, color=YELLOW)
        sub.move_to(UP * 5.0)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)

        # 两瓶水
        b1 = self._make_water_bottle(position=LEFT * 1.4 + UP * 2.6, color="#29B6F6")
        b2 = self._make_water_bottle(position=RIGHT * 1.4 + UP * 2.6, color="#0288D1")

        self.play(GrowFromCenter(b1), run_time=0.5)
        self.play(GrowFromCenter(b2), run_time=0.5)

        plus = Text("+", font=self.FONT, font_size=56, color=WHITE)
        plus.move_to(UP * 2.6)
        self.play(FadeIn(plus), run_time=0.3)

        # 下箭头
        arr = Arrow(UP * 0.9, UP * 0.15, color=GOLD, stroke_width=4,
                    max_tip_length_to_length_ratio=0.25)
        self.play(Create(arr), run_time=0.4)

        # 结果框
        result = self._result_box(position=DOWN * 0.7)
        self.play(GrowFromCenter(result), run_time=0.6)
        self.wait(0.3)

        # 计算过程
        calc = Text("2 × 500ml = 1000ml ≈ 1kg", font=self.FONT,
                    font_size=24, color=GRAY_A)
        calc.move_to(DOWN * 2.0)
        self.play(FadeIn(calc), run_time=0.5)

        # 提示框
        tip_bg = RoundedRectangle(
            corner_radius=0.3, width=7.0, height=1.3,
            fill_color="#311B92", fill_opacity=0.6,
            stroke_color="#7E57C2", stroke_width=2
        )
        tip_bg.move_to(DOWN * 3.3)
        tip_t = Text("💡 拿一拿，感受1千克的重量！",
                     font=self.FONT, font_size=24, color=WHITE)
        tip_t.move_to(tip_bg.get_center())

        self.play(FadeIn(tip_bg), FadeIn(tip_t), run_time=0.6)
        self.wait(2.2)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(b1), FadeOut(b2), FadeOut(plus),
            FadeOut(arr), FadeOut(result),
            FadeOut(calc), FadeOut(tip_bg), FadeOut(tip_t),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 4: 四个苹果 ≈ 1kg
    # ══════════════════════════════════════════

    def scene_4_apples(self):
        title = Text("生活中的1千克", font=self.FONT, font_size=48,
                     color=self.C_TITLE, weight=BOLD)
        title.move_to(UP * 5.9)
        sub = Text("大约4个苹果的重量", font=self.FONT, font_size=32, color=YELLOW)
        sub.move_to(UP * 5.0)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)

        # 4 个苹果位置（2×2 格）
        positions = [
            LEFT * 1.4 + UP * 3.1,
            RIGHT * 1.4 + UP * 3.1,
            LEFT * 1.4 + UP * 1.4,
            RIGHT * 1.4 + UP * 1.4,
        ]
        colors = ["#E53935", "#C62828", "#D32F2F", "#B71C1C"]

        apples = [self._make_apple(pos, col) for pos, col in zip(positions, colors)]

        # 编号标签
        nums = [
            Text(str(i + 1), font=self.FONT, font_size=22, color=YELLOW)
            .move_to(pos + DOWN * 0.62)
            for i, pos in enumerate(positions)
        ]

        for apple, num in zip(apples, nums):
            self.play(GrowFromCenter(apple), run_time=0.4)
            self.play(FadeIn(num), run_time=0.2)

        # 下箭头
        arr = Arrow(UP * 0.55, DOWN * 0.15, color=GOLD, stroke_width=4,
                    max_tip_length_to_length_ratio=0.25)
        self.play(Create(arr), run_time=0.4)

        # 结果框
        result = self._result_box(position=DOWN * 0.85)
        self.play(GrowFromCenter(result), run_time=0.6)

        sub2 = Text("每个苹果约 250克", font=self.FONT, font_size=26, color=GRAY_A)
        sub2.move_to(DOWN * 2.2)
        self.play(FadeIn(sub2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(sub),
            *[FadeOut(a) for a in apples],
            *[FadeOut(n) for n in nums],
            FadeOut(arr), FadeOut(result), FadeOut(sub2),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 5: 用电子秤称量
    # ══════════════════════════════════════════

    def scene_5_scale(self):
        title = Text("用电子秤称量", font=self.FONT, font_size=48,
                     color=self.C_TITLE, weight=BOLD)
        title.move_to(UP * 5.9)
        self.play(Write(title), run_time=0.7)

        # 电子秤（初始显示 0）
        scale0 = self._make_electronic_scale(value_str="0", position=UP * 2.2)
        self.play(GrowFromCenter(scale0), run_time=0.8)

        # 水瓶出现，然后移到秤面
        bottle = self._make_water_bottle(position=UP * 5.5, color="#29B6F6")
        self.play(GrowFromCenter(bottle), run_time=0.5)
        # 下移到秤面
        self.play(bottle.animate.move_to(UP * 4.0), run_time=0.7)

        # 秤数字变为 1
        scale1 = self._make_electronic_scale(value_str="1", position=UP * 2.2)
        self.play(FadeOut(scale0), FadeIn(scale1), run_time=0.5)

        # 指示箭头 + 读数说明
        arr = Arrow(UP * 0.3, UP * 1.2, color=YELLOW, stroke_width=4,
                    max_tip_length_to_length_ratio=0.2)
        read_lbl = VGroup(
            Text("读数：", font=self.FONT, font_size=30, color=YELLOW),
            Text("1", font=self.FONT, font_size=36, color=self.C_KG, weight=BOLD),
            Text("kg", font=self.FONT, font_size=30, color=YELLOW),
        ).arrange(RIGHT, buff=0.2)
        read_lbl.move_to(DOWN * 0.2)

        self.play(Create(arr), run_time=0.4)
        self.play(FadeIn(read_lbl, shift=UP * 0.2), run_time=0.5)

        # 三行说明
        explain_bg = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=2.7,
            fill_color="#1A237E", fill_opacity=0.5,
            stroke_color="#5C6BC0", stroke_width=2
        )
        explain_bg.move_to(DOWN * 2.7)

        e1 = Text("📺 屏幕数字 = 物品质量", font=self.FONT, font_size=26, color=WHITE)
        e2 = VGroup(
            Text("单位是", font=self.FONT, font_size=26, color=WHITE),
            Text("千克", font=self.FONT, font_size=26, color=self.C_KG, weight=BOLD),
            Text("(kg)", font=self.FONT, font_size=26, color=self.C_KG),
        ).arrange(RIGHT, buff=0.2)
        e3 = Text("数字越大，物品越重", font=self.FONT, font_size=26, color=GRAY_A)
        VGroup(e1, e2, e3).arrange(DOWN, buff=0.3).move_to(explain_bg.get_center())

        self.play(FadeIn(explain_bg), run_time=0.4)
        self.play(Write(e1), run_time=0.5)
        self.play(FadeIn(e2), run_time=0.5)
        self.play(Write(e3), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(bottle),
            FadeOut(scale1), FadeOut(arr), FadeOut(read_lbl),
            FadeOut(explain_bg), FadeOut(e1), FadeOut(e2), FadeOut(e3),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 6: 知识总结
    # ══════════════════════════════════════════

    def scene_6_summary(self):
        title = Text("知识总结", font=self.FONT, font_size=54,
                     color=self.C_TITLE, weight=BOLD)
        title.move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 4 张卡片：颜色、文字、Y坐标
        cards_meta = [
            ("1千克 = 1kg",       "千克的符号是 kg",      "#1565C0", "#42A5F5",  4.5),
            ("2瓶矿泉水 ≈ 1kg",   "两瓶500ml水的重量",    "#1B5E20", "#66BB6A",  2.5),
            ("4个苹果 ≈ 1kg",     "每个苹果约250克",      "#B71C1C", "#EF5350",  0.5),
            ("电子秤读千克数",      "屏幕数字就是质量(kg)", "#4A148C", "#AB47BC", -1.5),
        ]

        cards = []
        for main, sub, bg, stroke, y in cards_meta:
            card = self._info_card(main, sub, bg, stroke, y)
            # 初始从左侧飞入
            card.shift(LEFT * 11)
            cards.append(card)
            self.add(card)

        for card in cards:
            self.play(card.animate.shift(RIGHT * 11), run_time=0.5)
            self.wait(0.25)

        # 底部鼓励语
        cheer = Text("掌握千克，轻松生活！", font=self.FONT,
                     font_size=32, color=YELLOW)
        cheer.move_to(DOWN * 3.2)
        self.play(FadeIn(cheer, shift=UP * 0.3, scale=1.1), run_time=0.6)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(cheer),
            *[FadeOut(c) for c in cards],
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 7: 片尾关注
    # ══════════════════════════════════════════

    def scene_7_outro(self):
        # 星星装饰（8颗）
        stars = VGroup(*[
            Star(
                n=5, outer_radius=0.35, inner_radius=0.16,
                fill_color=GOLD, fill_opacity=0.9, stroke_width=0
            ).move_to(3.0 * np.array([
                np.cos(i * 2 * PI / 8),
                np.sin(i * 2 * PI / 8),
                0
            ]))
            for i in range(8)
        ])

        self.play(
            LaggedStart(*[GrowFromCenter(s) for s in stars], lag_ratio=0.08),
            run_time=0.9
        )

        # 作者名放大
        author_big = Text(
            "上海初高中数学直通车",
            font=self.FONT, font_size=40, color=WHITE, weight=BOLD
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font=self.FONT, font_size=30, color=GRAY_B
        ).move_to(UP * 1.2)

        self.play(
            Transform(self.author_bar, author_big),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注文字
        follow = Text(
            "关注我，获得更多数学技巧！",
            font=self.FONT, font_size=30, color=GOLD
        ).move_to(DOWN * 0.2)

        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)
        self.play(Rotate(stars, angle=TAU, run_time=2.0))
        self.wait(0.5)

        self.play(
            FadeOut(self.author_bar),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(stars),
            run_time=0.8
        )