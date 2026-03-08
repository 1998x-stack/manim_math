"""
认识克 - 二年级数学教学动画
Understanding Grams - 2nd Grade Math Teaching Animation

目标受众: 小学二年级学生
格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm

渲染命令:
  快速预览: manim -pql gram.py UnderstandGram
  高质量:   manim -qh  gram.py UnderstandGram
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


class UnderstandGram(Scene):
    """
    认识克 教学动画

    场景顺序:
      1. 开场钩子
      2. 认识克单位
      3. 一枚硬币 ≈ 1g
      4. 一粒花生米 ≈ 1g，并与硬币对比
      5. 用弹簧秤称量
      6. 克 vs 千克对比
      7. 知识总结 + 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # ── 配色 ──────────────────────────────
        self.C_TITLE     = GOLD
        self.C_COIN      = "#D4A017"      # 硬币金黄
        self.C_COIN_DARK = "#9A7010"      # 硬币边缘深色
        self.C_PEANUT    = "#C4813A"      # 花生棕
        self.C_PEANUT_D  = "#8B5A2B"      # 花生深棕
        self.C_GRAM      = "#80DEEA"      # 克单位颜色
        self.C_GREEN     = "#A5D6A7"
        self.C_HIGHLIGHT = "#FFD700"
        self.FONT        = "Noto Sans CJK SC"

        # ── 执行场景 ──────────────────────────
        self.scene_1_hook()
        self.scene_2_gram_definition()
        self.scene_3_coin()
        self.scene_4_peanut_compare()
        self.scene_5_spring_scale()
        self.scene_6_gram_vs_kg()
        self.scene_7_summary_outro()

    # ══════════════════════════════════════════
    # 工具函数
    # ══════════════════════════════════════════

    def _author_bar(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=self.FONT, font_size=20, color=GRAY_B
        ).move_to(UP * 7.2)

    def _make_coin(self, position=ORIGIN, radius=0.72, label="2分"):
        """金属硬币：双圆 + 文字"""
        outer = Circle(
            radius=radius,
            fill_color=self.C_COIN, fill_opacity=1.0,
            stroke_color=self.C_COIN_DARK, stroke_width=5
        )
        inner = Circle(
            radius=radius * 0.82,
            fill_color=self.C_COIN, fill_opacity=0,
            stroke_color=self.C_COIN_DARK, stroke_width=1.5
        )
        # 文字：分两行
        line1 = Text(label, font=self.FONT, font_size=int(radius * 52),
                     color="#3E2700", weight=BOLD)
        line1.move_to(outer.get_center())

        # 高光弧
        highlight = Arc(
            radius=radius * 0.7,
            start_angle=PI * 0.6, angle=PI * 0.55,
            stroke_color=WHITE, stroke_width=3, stroke_opacity=0.5
        )
        highlight.move_to(outer.get_center() + UP * radius * 0.1)

        coin = VGroup(outer, inner, highlight, line1)
        coin.move_to(position)
        return coin

    def _make_peanut(self, position=ORIGIN, scale=1.0):
        """花生米：椭圆 + 纹理线 + 茎点"""
        body = Ellipse(
            width=1.0 * scale, height=0.65 * scale,
            fill_color=self.C_PEANUT, fill_opacity=1.0,
            stroke_color=self.C_PEANUT_D, stroke_width=3
        )
        # 纹理横线（3条）
        lines = VGroup(*[
            Line(
                body.get_left() + RIGHT * 0.15 * scale + UP * dy * scale,
                body.get_right() + LEFT * 0.15 * scale + UP * dy * scale,
                stroke_color=self.C_PEANUT_D, stroke_width=1.2, stroke_opacity=0.6
            )
            for dy in [-0.12, 0.0, 0.12]
        ])
        # 两端小圆点
        dot_l = Dot(body.get_left() + RIGHT * 0.08 * scale,
                    radius=0.06 * scale, color=self.C_PEANUT_D)
        dot_r = Dot(body.get_right() + LEFT * 0.08 * scale,
                    radius=0.06 * scale, color=self.C_PEANUT_D)

        peanut = VGroup(body, lines, dot_l, dot_r)
        peanut.rotate(20 * DEGREES)
        peanut.move_to(position)
        return peanut

    def _make_spring_scale(self, position=ORIGIN, value_str="0", scale=1.0):
        """
        弹簧秤：刻度尺背景 + 刻度线 + 指针 + 钩子
        采用竖向布局
        """
        H = 3.6 * scale
        W = 1.5 * scale

        # 外壳
        body = RoundedRectangle(
            corner_radius=0.25 * scale, width=W, height=H,
            fill_color="#37474F", fill_opacity=1,
            stroke_color="#78909C", stroke_width=3
        )

        # 刻度背景（白色面板）
        panel = Rectangle(
            width=W * 0.65, height=H * 0.82,
            fill_color="#ECEFF1", fill_opacity=1, stroke_width=0
        )
        panel.move_to(body.get_center() + LEFT * W * 0.1)

        # 刻度线（5条主刻度：0, 1, 2, 3, 4g）
        tick_group = VGroup()
        panel_h = H * 0.82
        panel_top = panel.get_top()
        n_ticks = 5
        for i in range(n_ticks):
            frac = i / (n_ticks - 1)
            y = panel_top[1] - panel_h * frac
            x_left  = panel.get_left()[0]
            x_right = panel.get_right()[0]

            # 主刻度线
            tick = Line(
                [x_left, y, 0],
                [x_right - 0.1 * scale, y, 0],
                stroke_color="#37474F", stroke_width=2
            )
            tick_group.add(tick)

            # 刻度数字（克）
            num_val = n_ticks - 1 - i  # 0在底部，4在顶部
            num_label = Text(
                str(num_val), font=self.FONT,
                font_size=int(16 * scale), color="#212121"
            )
            num_label.move_to([x_right + 0.22 * scale, y, 0])
            tick_group.add(num_label)

        # 单位标签
        unit_label = Text("g", font=self.FONT,
                          font_size=int(18 * scale), color="#546E7A")
        unit_label.next_to(panel, RIGHT, buff=0.08 * scale)
        unit_label.shift(UP * panel_h * 0.4)

        # ── 指针位置计算 ──
        # value_str 是数字字符串，映射到刻度位置
        try:
            val = float(value_str)
        except ValueError:
            val = 0.0
        val_clamped = np.clip(val, 0, n_ticks - 1)
        frac_ptr = val_clamped / (n_ticks - 1)
        # 指针 y 坐标
        ptr_y = panel_top[1] - panel_h * frac_ptr
        ptr_x_left  = panel.get_left()[0] - 0.05 * scale
        ptr_x_right = panel.get_right()[0] + 0.05 * scale

        pointer = Line(
            [ptr_x_left, ptr_y, 0],
            [ptr_x_right, ptr_y, 0],
            stroke_color="#F44336", stroke_width=4
        )

        # 钩子（秤的下端）
        hook_top = np.array([body.get_center()[0], body.get_bottom()[1], 0])
        hook_line = Line(
            hook_top,
            hook_top + DOWN * 0.5 * scale,
            stroke_color="#78909C", stroke_width=3
        )
        hook_circle = Circle(
            radius=0.12 * scale,
            stroke_color="#78909C", stroke_width=3,
            fill_opacity=0
        )
        hook_circle.move_to(hook_line.get_end() + DOWN * 0.12 * scale)

        # 顶部挂环
        ring = Arc(
            radius=0.18 * scale,
            start_angle=0, angle=PI,
            stroke_color="#90A4AE", stroke_width=4
        )
        ring.move_to(body.get_top() + UP * 0.1 * scale)

        scale_grp = VGroup(body, panel, tick_group, unit_label,
                           pointer, hook_line, hook_circle, ring)
        scale_grp.move_to(position)
        return scale_grp

    def _result_box_gram(self, position=ORIGIN):
        """绿色结果框：约 1克"""
        box = RoundedRectangle(
            corner_radius=0.35, width=4.0, height=1.5,
            fill_color="#1B5E20", fill_opacity=0.85,
            stroke_color="#A5D6A7", stroke_width=3
        )
        box.move_to(position)
        row = VGroup(
            Text("约", font=self.FONT, font_size=40, color=WHITE),
            Text("1", font=self.FONT, font_size=64,
                 color=self.C_GRAM, weight=BOLD),
            Text("克", font=self.FONT, font_size=40, color=WHITE),
        ).arrange(RIGHT, buff=0.2)
        row.move_to(box.get_center())
        return VGroup(box, row)

    def _info_card(self, main_txt, sub_txt, bg_color, stroke_color, y_pos):
        bg = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=1.7,
            fill_color=bg_color, fill_opacity=0.65,
            stroke_color=stroke_color, stroke_width=2.5
        )
        bg.move_to(UP * y_pos)
        main = Text(main_txt, font=self.FONT, font_size=30,
                    color=WHITE, weight=BOLD)
        main.move_to(bg.get_center() + UP * 0.33)
        sub = Text(sub_txt, font=self.FONT, font_size=22, color=GRAY_A)
        sub.move_to(bg.get_center() + DOWN * 0.33)
        return VGroup(bg, main, sub)

    # ══════════════════════════════════════════
    # Scene 1: 开场钩子
    # ══════════════════════════════════════════

    def scene_1_hook(self):
        self.author_bar = self._author_bar()
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.4)

        hook1 = Text("1克", font=self.FONT, font_size=96,
                     color=self.C_TITLE, weight=BOLD)
        hook2 = Text("有多轻？", font=self.FONT, font_size=52, color=WHITE)
        VGroup(hook1, hook2).arrange(DOWN, buff=0.4).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.7)
        self.play(FadeIn(hook2, shift=UP * 0.3), run_time=0.5)

        # 硬币 + 花生米（带问号）
        coin   = self._make_coin(position=LEFT * 1.8 + UP * 1.3)
        peanut = self._make_peanut(position=RIGHT * 1.8 + UP * 1.3, scale=1.3)

        q1 = Text("?", font=self.FONT, font_size=52, color=YELLOW)
        q1.move_to(LEFT * 1.8 + UP * 2.5)
        q2 = Text("?", font=self.FONT, font_size=52, color=YELLOW)
        q2.move_to(RIGHT * 1.8 + UP * 2.5)

        self.play(GrowFromCenter(coin), GrowFromCenter(peanut), run_time=0.7)
        self.play(FadeIn(q1), FadeIn(q2), run_time=0.4)
        self.wait(1.2)

        self.play(
            FadeOut(hook1), FadeOut(hook2),
            FadeOut(coin), FadeOut(peanut),
            FadeOut(q1), FadeOut(q2),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 2: 认识克单位
    # ══════════════════════════════════════════

    def scene_2_gram_definition(self):
        title = Text("认识克", font=self.FONT, font_size=54,
                     color=self.C_TITLE, weight=BOLD)
        title.move_to(UP * 5.9)
        self.play(Write(title), run_time=0.7)

        # 大圆 + "g" 符号
        circle = Circle(
            radius=1.55,
            fill_color="#00695C", fill_opacity=0.88,
            stroke_color=self.C_GRAM, stroke_width=6
        )
        circle.move_to(UP * 3.8)

        g_text = Text("g", font=self.FONT, font_size=96,
                      color=WHITE, weight=BOLD)
        g_text.move_to(circle.get_center())

        self.play(GrowFromCenter(circle), run_time=0.6)
        self.play(Write(g_text), run_time=0.6)
        self.play(Flash(circle, color=self.C_GRAM, flash_radius=2.0), run_time=0.5)

        # 等号行
        arr = Arrow(UP * 2.0, UP * 1.4, color=GRAY_B,
                    stroke_width=3, max_tip_length_to_length_ratio=0.2)
        self.play(Create(arr), run_time=0.4)

        eq_row = VGroup(
            Text("克", font=self.FONT, font_size=40, color=YELLOW),
            Text("=", font=self.FONT, font_size=40, color=WHITE),
            Text("g", font=self.FONT, font_size=40,
                 color=self.C_GRAM, weight=BOLD),
        ).arrange(RIGHT, buff=0.35)
        eq_row.move_to(UP * 1.0)
        self.play(FadeIn(eq_row, shift=UP * 0.3), run_time=0.6)

        # 信息框
        info_bg = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=2.0,
            fill_color="#004D40", fill_opacity=0.5,
            stroke_color="#26A69A", stroke_width=2
        )
        info_bg.move_to(DOWN * 0.5)

        info1 = Text("克是计量较轻物品的单位", font=self.FONT,
                     font_size=28, color=WHITE)
        info2 = Text("比千克小得多！", font=self.FONT,
                     font_size=26, color=self.C_GRAM)
        VGroup(info1, info2).arrange(DOWN, buff=0.3).move_to(info_bg.get_center())

        self.play(FadeIn(info_bg), run_time=0.4)
        self.play(Write(info1), run_time=0.6)
        self.play(FadeIn(info2), run_time=0.5)
        self.wait(1.8)

        self.play(
            FadeOut(title), FadeOut(circle), FadeOut(g_text),
            FadeOut(arr), FadeOut(eq_row),
            FadeOut(info_bg), FadeOut(info1), FadeOut(info2),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 3: 一枚硬币 ≈ 1g
    # ══════════════════════════════════════════

    def scene_3_coin(self):
        title = Text("生活中的1克", font=self.FONT, font_size=48,
                     color=self.C_TITLE, weight=BOLD)
        title.move_to(UP * 5.9)
        sub = Text("一枚2分硬币", font=self.FONT, font_size=32, color=YELLOW)
        sub.move_to(UP * 5.0)

        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)

        # 硬币从顶部落下
        coin = self._make_coin(position=UP * 6.5)
        self.add(coin)
        self.play(
            coin.animate.move_to(UP * 3.5),
            rate_func=bounce,
            run_time=0.9
        )

        # 弹簧秤（初始0）
        spring_0 = self._make_spring_scale(
            position=UP * 0.6, value_str="0", scale=1.0
        )
        self.play(FadeIn(spring_0), run_time=0.5)

        # 硬币挂到秤钩上
        self.play(coin.animate.move_to(UP * 3.2).scale(0.9), run_time=0.5)

        # 指针变为"1g"
        spring_1 = self._make_spring_scale(
            position=UP * 0.6, value_str="1", scale=1.0
        )
        self.play(FadeOut(spring_0), FadeIn(spring_1), run_time=0.4)

        # 箭头 + 读数
        read_arr = Arrow(
            RIGHT * 1.5 + DOWN * 0.2,
            RIGHT * 0.9 + DOWN * 0.2,
            color=YELLOW, stroke_width=5,
            max_tip_length_to_length_ratio=0.25
        )
        read_lbl = VGroup(
            Text("读数：", font=self.FONT, font_size=28, color=YELLOW),
            Text("1", font=self.FONT, font_size=36,
                 color=self.C_GRAM, weight=BOLD),
            Text("g", font=self.FONT, font_size=28, color=YELLOW),
        ).arrange(RIGHT, buff=0.15)
        read_lbl.move_to(RIGHT * 2.3 + DOWN * 0.2)

        self.play(Create(read_arr), run_time=0.4)
        self.play(FadeIn(read_lbl, shift=LEFT * 0.2), run_time=0.5)

        # 说明框
        explain_bg = RoundedRectangle(
            corner_radius=0.3, width=7.0, height=2.0,
            fill_color="#1A237E", fill_opacity=0.5,
            stroke_color="#5C6BC0", stroke_width=2
        )
        explain_bg.move_to(DOWN * 2.8)
        e1 = Text("硬币很轻，只有1克哦！", font=self.FONT,
                  font_size=28, color=WHITE)
        e2 = Text("💡 捏一枚硬币，感受1克！", font=self.FONT,
                  font_size=24, color=GRAY_A)
        VGroup(e1, e2).arrange(DOWN, buff=0.3).move_to(explain_bg.get_center())

        self.play(FadeIn(explain_bg), run_time=0.4)
        self.play(Write(e1), run_time=0.5)
        self.play(FadeIn(e2), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(coin), FadeOut(spring_1),
            FadeOut(read_arr), FadeOut(read_lbl),
            FadeOut(explain_bg), FadeOut(e1), FadeOut(e2),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 4: 一粒花生米 ≈ 1g，与硬币对比
    # ══════════════════════════════════════════

    def scene_4_peanut_compare(self):
        title = Text("生活中的1克", font=self.FONT, font_size=48,
                     color=self.C_TITLE, weight=BOLD)
        title.move_to(UP * 5.9)
        sub = Text("一粒花生米", font=self.FONT, font_size=32, color=YELLOW)
        sub.move_to(UP * 5.0)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)

        # 花生米生长
        peanut = self._make_peanut(position=ORIGIN + UP * 3.2, scale=1.5)
        self.play(GrowFromCenter(peanut), run_time=0.7)
        self.play(Flash(peanut, color=YELLOW, flash_radius=1.3), run_time=0.5)

        # 移到左边，硬币出现在右边对比
        coin   = self._make_coin(position=ORIGIN + UP * 3.2)
        coin.set_opacity(0)  # 先隐藏

        self.play(
            peanut.animate.move_to(LEFT * 1.7 + UP * 3.2),
            run_time=0.5
        )
        coin.move_to(RIGHT * 1.7 + UP * 3.2)
        self.play(FadeIn(coin), run_time=0.4)

        # 两个标签
        lbl_peanut = Text("花生米", font=self.FONT, font_size=22, color=GRAY_A)
        lbl_peanut.move_to(LEFT * 1.7 + UP * 2.0)
        lbl_coin = Text("硬币", font=self.FONT, font_size=22, color=GRAY_A)
        lbl_coin.move_to(RIGHT * 1.7 + UP * 2.0)

        self.play(FadeIn(lbl_peanut), FadeIn(lbl_coin), run_time=0.4)

        # 对比符号
        vs = Text("VS", font=self.FONT, font_size=40,
                  color=WHITE, weight=BOLD)
        vs.move_to(UP * 3.2)
        self.play(FadeIn(vs), run_time=0.3)

        # 下箭头
        arr = Arrow(UP * 1.6, UP * 1.0, color=GOLD, stroke_width=4,
                    max_tip_length_to_length_ratio=0.25)
        self.play(Create(arr), run_time=0.4)

        # 结果框
        result = self._result_box_gram(position=UP * 0.3)
        self.play(GrowFromCenter(result), run_time=0.6)

        # 提示
        tip_bg = RoundedRectangle(
            corner_radius=0.3, width=7.0, height=1.3,
            fill_color="#311B92", fill_opacity=0.6,
            stroke_color="#7E57C2", stroke_width=2
        )
        tip_bg.move_to(DOWN * 1.3)
        tip_t = Text("它们都约重1克！", font=self.FONT,
                     font_size=28, color=WHITE)
        tip_t.move_to(tip_bg.get_center())

        self.play(FadeIn(tip_bg), FadeIn(tip_t), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(peanut), FadeOut(coin),
            FadeOut(lbl_peanut), FadeOut(lbl_coin), FadeOut(vs),
            FadeOut(arr), FadeOut(result),
            FadeOut(tip_bg), FadeOut(tip_t),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 5: 用弹簧秤称量
    # ══════════════════════════════════════════

    def scene_5_spring_scale(self):
        title = Text("用弹簧秤称量", font=self.FONT, font_size=48,
                     color=self.C_TITLE, weight=BOLD)
        title.move_to(UP * 5.9)
        self.play(Write(title), run_time=0.7)

        # 弹簧秤居中，稍大
        spring_0 = self._make_spring_scale(
            position=UP * 2.2, value_str="0", scale=1.2
        )
        self.play(GrowFromCenter(spring_0), run_time=0.8)

        # 花生米从右侧飞入，挂上钩子
        peanut = self._make_peanut(position=RIGHT * 3.5 + UP * 2.2, scale=1.2)
        self.play(GrowFromCenter(peanut), run_time=0.4)
        # 花生米移向钩子位置
        hook_pos = UP * 2.2 + DOWN * 2.2  # 秤钩大概位置
        self.play(peanut.animate.move_to(UP * 0.0 + DOWN * 0.2).scale(0.75),
                  run_time=0.7)

        # 秤变为1g
        spring_1 = self._make_spring_scale(
            position=UP * 2.2, value_str="1", scale=1.2
        )
        self.play(FadeOut(spring_0), FadeIn(spring_1), run_time=0.4)

        # 黄色箭头指向刻度 "1"
        # 刻度1在秤面板上 25% 处（从顶往下）
        # 秤中心 UP*2.2，面板高度约 3.6*1.2=4.32，顶端约 2.2+2.16=4.36
        # 1g 刻度 frac = 1/4 = 0.25 → y = 4.36 - 4.32*0.25 ≈ 3.28
        arr_start = np.array([1.6, 3.3, 0])
        arr_end   = np.array([0.5, 3.3, 0])
        read_arr = Arrow(arr_start, arr_end, color=YELLOW, stroke_width=5,
                         max_tip_length_to_length_ratio=0.25)
        self.play(Create(read_arr), run_time=0.4)

        # 读数标签
        read_lbl = VGroup(
            Text("读数：", font=self.FONT, font_size=26, color=YELLOW),
            Text("1", font=self.FONT, font_size=34,
                 color=self.C_GRAM, weight=BOLD),
            Text("g", font=self.FONT, font_size=26, color=YELLOW),
        ).arrange(RIGHT, buff=0.15)
        read_lbl.move_to(np.array([2.5, 3.3, 0]))
        self.play(FadeIn(read_lbl, shift=LEFT * 0.2), run_time=0.5)

        # 说明框
        explain_bg = RoundedRectangle(
            corner_radius=0.3, width=7.2, height=2.7,
            fill_color="#1A237E", fill_opacity=0.5,
            stroke_color="#5C6BC0", stroke_width=2
        )
        explain_bg.move_to(DOWN * 2.0)

        e1 = Text("📺 指针刻度 = 物品质量", font=self.FONT,
                  font_size=26, color=WHITE)
        e2_row = VGroup(
            Text("单位是", font=self.FONT, font_size=26, color=WHITE),
            Text("克", font=self.FONT, font_size=26,
                 color=self.C_GRAM, weight=BOLD),
            Text("(g)", font=self.FONT, font_size=26, color=self.C_GRAM),
        ).arrange(RIGHT, buff=0.18)
        e3 = Text("克 适合称较轻的物品", font=self.FONT,
                  font_size=26, color=GRAY_A)
        VGroup(e1, e2_row, e3).arrange(DOWN, buff=0.3).move_to(explain_bg.get_center())

        self.play(FadeIn(explain_bg), run_time=0.4)
        self.play(Write(e1), run_time=0.5)
        self.play(FadeIn(e2_row), run_time=0.5)
        self.play(Write(e3), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(peanut),
            FadeOut(spring_1), FadeOut(read_arr), FadeOut(read_lbl),
            FadeOut(explain_bg), FadeOut(e1), FadeOut(e2_row), FadeOut(e3),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 6: 克 vs 千克对比
    # ══════════════════════════════════════════

    def scene_6_gram_vs_kg(self):
        title = Text("克 vs 千克", font=self.FONT, font_size=48,
                     color=self.C_TITLE, weight=BOLD)
        title.move_to(UP * 5.9)
        self.play(Write(title), run_time=0.6)

        # ── 天平结构 ──────────────────────────
        # 支柱
        pole = Line(UP * 2.0, UP * 4.8, stroke_color="#78909C", stroke_width=6)
        base = Rectangle(
            width=2.0, height=0.35,
            fill_color="#455A64", fill_opacity=1,
            stroke_color="#78909C", stroke_width=2
        )
        base.move_to(UP * 2.0)

        # 横梁（稍微倾斜，右边重）
        beam_cx, beam_cy = 0.0, 4.65
        beam_half = 2.8
        tilt_rad = np.radians(10)
        left_pt  = np.array([
            beam_cx - beam_half * np.cos(tilt_rad),
            beam_cy - beam_half * np.sin(tilt_rad),
            0
        ])
        right_pt = np.array([
            beam_cx + beam_half * np.cos(tilt_rad),
            beam_cy + beam_half * np.sin(tilt_rad),
            0
        ])
        beam = Line(left_pt, right_pt, stroke_color="#90A4AE", stroke_width=5)

        # 中心铆钉
        pivot_dot = Dot(np.array([beam_cx, beam_cy, 0]),
                        radius=0.14, color="#CFD8DC")

        # 左盘吊线 + 盘（1克/硬币一侧）
        pan_left_top  = left_pt
        pan_left_bot  = pan_left_top + np.array([0, -1.3, 0])
        string_l = DashedLine(pan_left_top, pan_left_bot,
                              stroke_color="#90A4AE", dash_length=0.15)
        pan_l = Ellipse(
            width=1.3, height=0.28,
            fill_color="#546E7A", fill_opacity=1,
            stroke_color="#78909C", stroke_width=2
        )
        pan_l.move_to(pan_left_bot)

        # 右盘吊线 + 盘（1千克/水瓶一侧）
        pan_right_top = right_pt
        pan_right_bot = pan_right_top + np.array([0, -1.3, 0])
        string_r = DashedLine(pan_right_top, pan_right_bot,
                              stroke_color="#90A4AE", dash_length=0.15)
        pan_r = Ellipse(
            width=1.3, height=0.28,
            fill_color="#546E7A", fill_opacity=1,
            stroke_color="#78909C", stroke_width=2
        )
        pan_r.move_to(pan_right_bot)

        balance = VGroup(pole, base, beam, pivot_dot,
                         string_l, pan_l, string_r, pan_r)
        self.play(Create(balance), run_time=1.0)

        # 左盘：1枚硬币
        coin_sm = self._make_coin(position=pan_l.get_top() + UP * 0.4, radius=0.4)
        self.play(GrowFromCenter(coin_sm), run_time=0.5)

        # 右盘：简化水瓶堆（两个小矩形）
        b1 = RoundedRectangle(corner_radius=0.1, width=0.4, height=0.7,
                              fill_color="#29B6F6", fill_opacity=0.8,
                              stroke_color=WHITE, stroke_width=1.5)
        b2 = b1.copy()
        bottles = VGroup(b1, b2).arrange(RIGHT, buff=0.1)
        bottles.move_to(pan_r.get_top() + UP * 0.5)
        self.play(GrowFromCenter(bottles), run_time=0.5)

        # 标签
        lbl_l = Text("1克", font=self.FONT, font_size=24,
                     color=self.C_GRAM, weight=BOLD)
        lbl_l.move_to(pan_l.get_center() + DOWN * 0.6)
        lbl_r = Text("1千克", font=self.FONT, font_size=24,
                     color="#29B6F6", weight=BOLD)
        lbl_r.move_to(pan_r.get_center() + DOWN * 0.6)
        self.play(FadeIn(lbl_l), FadeIn(lbl_r), run_time=0.4)

        # 公式行
        formula_bg = RoundedRectangle(
            corner_radius=0.3, width=7.0, height=1.1,
            fill_color="#0D47A1", fill_opacity=0.55,
            stroke_color=BLUE_C, stroke_width=2
        )
        formula_bg.move_to(UP * 1.2)
        formula_row = VGroup(
            Text("1千克", font=self.FONT, font_size=34,
                 color="#29B6F6", weight=BOLD),
            Text("=", font=self.FONT, font_size=34, color=WHITE),
            Text("1000克", font=self.FONT, font_size=34,
                 color=self.C_GRAM, weight=BOLD),
        ).arrange(RIGHT, buff=0.3)
        formula_row.move_to(formula_bg.get_center())

        self.play(FadeIn(formula_bg), run_time=0.4)
        self.play(Write(formula_row), run_time=0.7)

        sub_note = Text("1000枚硬币 = 1千克", font=self.FONT,
                        font_size=26, color=GRAY_A)
        sub_note.move_to(UP * 0.2)
        self.play(FadeIn(sub_note), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(balance),
            FadeOut(coin_sm), FadeOut(bottles),
            FadeOut(lbl_l), FadeOut(lbl_r),
            FadeOut(formula_bg), FadeOut(formula_row), FadeOut(sub_note),
            run_time=0.5
        )

    # ══════════════════════════════════════════
    # Scene 7: 知识总结 + 片尾
    # ══════════════════════════════════════════

    def scene_7_summary_outro(self):
        title = Text("知识总结", font=self.FONT, font_size=54,
                     color=self.C_TITLE, weight=BOLD)
        title.move_to(UP * 6.5)
        self.play(Write(title), run_time=0.6)

        # 3 张卡片从左飞入
        cards_meta = [
            ("1克 = 1g",        "克的符号是 g",          "#1565C0", "#42A5F5", 4.5),
            ("硬币/花生 ≈ 1g",   "用于称轻小物品",        "#4E342E", "#A1887F", 2.5),
            ("克 < 千克",        "1000克 = 1千克",        "#4A148C", "#AB47BC", 0.5),
        ]

        cards = []
        for main, sub, bg, stroke, y in cards_meta:
            card = self._info_card(main, sub, bg, stroke, y)
            card.shift(LEFT * 11)
            cards.append(card)
            self.add(card)

        for card in cards:
            self.play(card.animate.shift(RIGHT * 11), run_time=0.5)
            self.wait(0.2)

        cheer = Text("掌握克，轻松生活！", font=self.FONT,
                     font_size=32, color=YELLOW)
        cheer.move_to(DOWN * 1.5)
        self.play(FadeIn(cheer, shift=UP * 0.3, scale=1.1), run_time=0.6)
        self.wait(1.5)

        # ── 片尾 ──────────────────────────────
        stars = VGroup(*[
            Star(
                n=5, outer_radius=0.32, inner_radius=0.14,
                fill_color=GOLD, fill_opacity=0.9, stroke_width=0
            ).move_to(3.0 * np.array([
                np.cos(i * 2 * PI / 8),
                np.sin(i * 2 * PI / 8),
                0
            ]))
            for i in range(8)
        ])

        self.play(
            FadeOut(title), FadeOut(cheer),
            *[FadeOut(c) for c in cards],
            run_time=0.5
        )

        self.play(
            LaggedStart(*[GrowFromCenter(s) for s in stars], lag_ratio=0.08),
            run_time=0.9
        )

        # 作者大字
        author_big = Text(
            "上海初高中数学直通车",
            font=self.FONT, font_size=40, color=WHITE, weight=BOLD
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font=self.FONT, font_size=30, color=GRAY_B
        ).move_to(UP * 1.1)

        self.play(Transform(self.author_bar, author_big), run_time=0.7)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

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