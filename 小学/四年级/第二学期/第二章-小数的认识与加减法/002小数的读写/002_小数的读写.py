"""
002_小数的读写.py — 小数的读写 教学动画

知识点: 小数的读写法则
年级: 四年级第二学期
格式: TikTok 竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm

核心内容:
  1. 开场钩子 — 30.05 怎么读？
  2. 读法规则 — 整数部分、小数点、小数部分
  3. 例1读 — 30.05 → 三十点零五
  4. 写法规则 — 听声音写数
  5. 例2写 — 一百点零零八 → 100.008
  6. 要点总结
  7. 片尾
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
COLOR_INT     = "#3b82f6"   # 蓝 — 整数部分
COLOR_DOT     = "#f59e0b"   # 橙 — 小数点
COLOR_DEC     = "#22c55e"   # 绿 — 小数部分
COLOR_HL      = "#fbbf24"   # 黄 — 高亮
COLOR_RULE    = "#a78bfa"   # 紫 — 规则框
COLOR_WARN    = "#ef4444"   # 红 — 警示
COLOR_AUTHOR  = "#6b7280"
FONT          = "Noto Sans CJK SC"


class DecimalReadWriteLesson(Scene):
    """
    小数的读写教学动画
    场景:
      1. 开场钩子
      2. 读法规则
      3. 例1：30.05 的读法
      4. 写法规则
      5. 例2：一百点零零八 的写法
      6. 要点总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.scene_1_opening()
        self.scene_2_read_rule()
        self.scene_3_read_example()
        self.scene_4_write_rule()
        self.scene_5_write_example()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 辅助：带颜色分区的小数数字组
    # ------------------------------------------------------------------

    def make_decimal_number(self, int_str, dec_str, font_size=52):
        """
        构建一个整数部分(蓝)·小数点(橙)·小数部分(绿) 的 VGroup。
        返回 (group, int_part, dot_part, dec_part)
        """
        int_tex  = MathTex(int_str,  font_size=font_size, color=COLOR_INT)
        dot_tex  = MathTex(r".",     font_size=font_size, color=COLOR_DOT)
        dec_tex  = MathTex(dec_str,  font_size=font_size, color=COLOR_DEC)
        group = VGroup(int_tex, dot_tex, dec_tex).arrange(RIGHT, buff=0.05)
        return group, int_tex, dot_tex, dec_tex

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
            "小数的读写", font=FONT, font_size=52, color=WHITE, weight=BOLD
        ).move_to(UP * 5.5)
        hook2 = Text(
            "你会读这个数吗？", font=FONT, font_size=36, color=COLOR_HL
        ).move_to(UP * 4.3)

        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.6)

        # 展示问题数字 30.05
        num_group, _, _, _ = self.make_decimal_number("30", "05", font_size=60)
        num_group.move_to(UP * 1.8)
        self.play(FadeIn(num_group, scale=0.5), run_time=0.8)

        q_mark = Text("= ?", font=FONT, font_size=44, color=COLOR_HL).next_to(num_group, RIGHT, buff=0.3)
        self.play(FadeIn(q_mark, shift=LEFT * 0.2), run_time=0.5)
        self.wait(0.8)

        self.play(FadeOut(VGroup(hook1, hook2, num_group, q_mark)), run_time=0.4)

    # ------------------------------------------------------------------
    # Scene 2: 读法规则
    # ------------------------------------------------------------------

    def scene_2_read_rule(self):
        title = Text(
            "读法规则", font=FONT, font_size=38,
            color=COLOR_RULE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 示意数字
        num_group, int_part, dot_part, dec_part = self.make_decimal_number("30", "05", font_size=54)
        num_group.move_to(UP * 4.0)
        self.play(FadeIn(num_group), run_time=0.6)

        # --- 规则1：整数部分 ---
        rule1_title = Text(
            "① 整数部分", font=FONT, font_size=28, color=COLOR_INT, weight=BOLD
        ).move_to(UP * 2.6)
        rule1_body = Text(
            "按整数读法读", font=FONT, font_size=24, color=GRAY_A
        ).move_to(UP * 2.0)

        arrow1 = Arrow(
            start=rule1_title.get_top() + UP * 0.1,
            end=int_part.get_bottom() + DOWN * 0.15,
            color=COLOR_INT, stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )

        self.play(
            FadeIn(rule1_title),
            FadeIn(rule1_body),
            GrowArrow(arrow1),
            int_part.animate.set_color(COLOR_INT),
            run_time=0.7
        )

        read_int = Text(
            "30 → 三十", font=FONT, font_size=26, color=COLOR_INT
        ).move_to(UP * 1.3)
        self.play(Write(read_int), run_time=0.5)
        self.wait(0.5)

        # --- 规则2：小数点 ---
        rule2_title = Text(
            "② 小数点", font=FONT, font_size=28, color=COLOR_DOT, weight=BOLD
        ).move_to(UP * 0.3)
        rule2_body = Text(
            '读作"点"', font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 0.3)

        arrow2 = Arrow(
            start=rule2_title.get_top() + UP * 0.05,
            end=dot_part.get_bottom() + DOWN * 0.15,
            color=COLOR_DOT, stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )

        self.play(
            FadeIn(rule2_title),
            FadeIn(rule2_body),
            GrowArrow(arrow2),
            dot_part.animate.set_color(COLOR_DOT),
            run_time=0.7
        )

        read_dot = Text(
            "· → 点", font=FONT, font_size=26, color=COLOR_DOT
        ).move_to(DOWN * 1.0)
        self.play(Write(read_dot), run_time=0.5)
        self.wait(0.5)

        # --- 规则3：小数部分 ---
        rule3_title = Text(
            "③ 小数部分", font=FONT, font_size=28, color=COLOR_DEC, weight=BOLD
        ).move_to(DOWN * 2.0)
        rule3_body = Text(
            "依次读每一位数字", font=FONT, font_size=24, color=GRAY_A
        ).move_to(DOWN * 2.6)

        arrow3 = Arrow(
            start=rule3_title.get_top() + UP * 0.05,
            end=dec_part.get_bottom() + DOWN * 0.15,
            color=COLOR_DEC, stroke_width=2,
            max_tip_length_to_length_ratio=0.15
        )

        self.play(
            FadeIn(rule3_title),
            FadeIn(rule3_body),
            GrowArrow(arrow3),
            dec_part.animate.set_color(COLOR_DEC),
            run_time=0.7
        )

        read_dec = Text(
            "0, 5 → 零五", font=FONT, font_size=26, color=COLOR_DEC
        ).move_to(DOWN * 3.4)
        self.play(Write(read_dec), run_time=0.5)
        self.wait(0.4)

        warn = Text(
            "注意：0 也要读出来！", font=FONT, font_size=24,
            color=COLOR_WARN, weight=BOLD
        ).move_to(DOWN * 4.3)
        self.play(FadeIn(warn, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            title, num_group,
            rule1_title, rule1_body, arrow1, read_int,
            rule2_title, rule2_body, arrow2, read_dot,
            rule3_title, rule3_body, arrow3, read_dec,
            warn
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 3: 例题1 — 读 30.05
    # ------------------------------------------------------------------

    def scene_3_read_example(self):
        title = Text(
            "例题：读出下面的数", font=FONT, font_size=34,
            color=COLOR_INT, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 数字展示
        num_group, int_part, dot_part, dec_part = self.make_decimal_number("30", "05", font_size=62)
        num_group.move_to(UP * 4.0)
        self.play(FadeIn(num_group), run_time=0.6)

        # ---- 拆解读法动画 ----
        sep1 = VGroup(
            Text("整数部分", font=FONT, font_size=24, color=COLOR_INT),
            Text("30", font=FONT, font_size=28, color=COLOR_INT),
            Text("→ 三十", font=FONT, font_size=28, color=COLOR_INT),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 2.5)

        self.play(
            Indicate(int_part, color=COLOR_INT, scale_factor=1.2),
            run_time=0.6
        )
        self.play(FadeIn(sep1, shift=UP * 0.2), run_time=0.5)

        sep2 = VGroup(
            Text("小数点", font=FONT, font_size=24, color=COLOR_DOT),
            Text("·", font=FONT, font_size=28, color=COLOR_DOT),
            Text("→ 点", font=FONT, font_size=28, color=COLOR_DOT),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 1.5)

        self.play(
            Indicate(dot_part, color=COLOR_DOT, scale_factor=1.4),
            run_time=0.6
        )
        self.play(FadeIn(sep2, shift=UP * 0.2), run_time=0.5)

        sep3_line1 = VGroup(
            Text("小数部分", font=FONT, font_size=24, color=COLOR_DEC),
            Text("0, 5", font=FONT, font_size=28, color=COLOR_DEC),
        ).arrange(RIGHT, buff=0.25)
        sep3_line2 = VGroup(
            Text("→ 依次读：", font=FONT, font_size=24, color=COLOR_DEC),
            Text("零、五", font=FONT, font_size=28, color=COLOR_DEC),
        ).arrange(RIGHT, buff=0.1)
        sep3 = VGroup(sep3_line1, sep3_line2).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        sep3.move_to(UP * 0.4)

        self.play(
            Indicate(dec_part, color=COLOR_DEC, scale_factor=1.2),
            run_time=0.6
        )
        self.play(FadeIn(sep3, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 分隔线
        hline = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1.5)
        hline.move_to(DOWN * 0.7)
        self.play(Create(hline), run_time=0.3)

        # 最终读法
        result_label = Text("读作：", font=FONT, font_size=26, color=GRAY_A)
        result_text  = Text("三十点零五", font=FONT, font_size=44, color=COLOR_HL, weight=BOLD)
        result = VGroup(result_label, result_text).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.7)

        self.play(FadeIn(result, shift=UP * 0.3, scale=0.9), run_time=0.7)
        self.play(Indicate(result_text, scale_factor=1.05, color=COLOR_HL), run_time=0.5)
        self.wait(1.8)

        self.play(FadeOut(VGroup(
            title, num_group,
            sep1, sep2, sep3, hline, result
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 4: 写法规则
    # ------------------------------------------------------------------

    def scene_4_write_rule(self):
        title = Text(
            "写法规则", font=FONT, font_size=38,
            color=COLOR_RULE, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        desc = Text(
            "听到一个数，怎么写出来？", font=FONT, font_size=26, color=GRAY_A
        ).move_to(UP * 4.4)
        self.play(Write(desc), run_time=0.5)

        # 三条规则卡片
        rules = VGroup(
            self._make_rule_card(
                "① 整数部分",
                "按整数写法写",
                COLOR_INT
            ),
            self._make_rule_card(
                "② 小数点",
                "写在个位右下角",
                COLOR_DOT
            ),
            self._make_rule_card(
                "③ 小数部分",
                "依次写每一位数字\n（0也要写）",
                COLOR_DEC
            ),
        ).arrange(DOWN, buff=0.45).move_to(UP * 1.0)

        for card in rules:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.2)

        # 示例
        eg_label = Text("例：一百点零零八", font=FONT, font_size=28, color=COLOR_HL)
        eg_arrow = MathTex(r"\Rightarrow", font_size=36, color=GRAY_A)
        eg_val   = MathTex(r"100.008", font_size=38, color=COLOR_HL)
        eg = VGroup(eg_label, eg_arrow, eg_val).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.2)
        self.play(FadeIn(eg, shift=UP * 0.2), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(VGroup(title, desc, rules, eg)), run_time=0.5)

    def _make_rule_card(self, title_str, body_str, color):
        """创建规则小卡片"""
        box = RoundedRectangle(
            width=7.5, height=1.15 if "\n" not in body_str else 1.45,
            corner_radius=0.2,
            fill_color="#0f172a", fill_opacity=0.9,
            stroke_color=color, stroke_width=2
        )
        title_t = Text(title_str, font=FONT, font_size=22, color=color, weight=BOLD)
        body_t  = Text(body_str,  font=FONT, font_size=20, color=GRAY_A)
        inner = VGroup(title_t, body_t).arrange(RIGHT, buff=0.3)
        inner.move_to(box.get_center())
        return VGroup(box, inner)

    # ------------------------------------------------------------------
    # Scene 5: 例题2 — 写 100.008
    # ------------------------------------------------------------------

    def scene_5_write_example(self):
        title = Text(
            "例题：写出下面的数", font=FONT, font_size=34,
            color=COLOR_DEC, weight=BOLD
        ).move_to(UP * 5.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        # 听到的读音
        hear_label = Text("听到：", font=FONT, font_size=26, color=GRAY_A)
        hear_text  = Text("一百点零零八", font=FONT, font_size=36, color=COLOR_HL, weight=BOLD)
        hear = VGroup(hear_label, hear_text).arrange(RIGHT, buff=0.2).move_to(UP * 4.2)
        self.play(FadeIn(hear, shift=DOWN * 0.1), run_time=0.6)

        # 逐步分析
        # Step 1: 整数部分
        s1_title = Text("第一步：整数部分", font=FONT, font_size=26, color=COLOR_INT, weight=BOLD)
        s1_body  = VGroup(
            Text("一百", font=FONT, font_size=26, color=COLOR_INT),
            MathTex(r"\rightarrow", font_size=28, color=GRAY_A),
            MathTex(r"100", font_size=32, color=COLOR_INT),
        ).arrange(RIGHT, buff=0.2)
        s1 = VGroup(s1_title, s1_body).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        s1.move_to(UP * 2.8)

        self.play(FadeIn(s1, shift=UP * 0.2), run_time=0.6)
        self.wait(0.4)

        # Step 2: 小数点
        s2_title = Text("第二步：小数点", font=FONT, font_size=26, color=COLOR_DOT, weight=BOLD)
        s2_body  = VGroup(
            Text("点", font=FONT, font_size=26, color=COLOR_DOT),
            MathTex(r"\rightarrow", font_size=28, color=GRAY_A),
            MathTex(r".", font_size=32, color=COLOR_DOT),
            Text("（写在100右下角）", font=FONT, font_size=20, color=GRAY_B),
        ).arrange(RIGHT, buff=0.15)
        s2 = VGroup(s2_title, s2_body).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        s2.move_to(UP * 1.5)

        self.play(FadeIn(s2, shift=UP * 0.2), run_time=0.6)
        self.wait(0.4)

        # Step 3: 小数部分
        s3_title = Text("第三步：小数部分", font=FONT, font_size=26, color=COLOR_DEC, weight=BOLD)
        s3_body  = VGroup(
            Text("零、零、八", font=FONT, font_size=26, color=COLOR_DEC),
            MathTex(r"\rightarrow", font_size=28, color=GRAY_A),
            MathTex(r"008", font_size=32, color=COLOR_DEC),
        ).arrange(RIGHT, buff=0.2)
        s3_note = Text("0 不能省略！", font=FONT, font_size=22, color=COLOR_WARN)
        s3 = VGroup(s3_title, s3_body, s3_note).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        s3.move_to(DOWN * 0.4)

        self.play(FadeIn(s3, shift=UP * 0.2), run_time=0.6)
        self.wait(0.4)

        # 分隔线
        hline = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY_B, stroke_width=1.5)
        hline.move_to(DOWN * 2.1)
        self.play(Create(hline), run_time=0.3)

        # 最终结果
        write_label = Text("写作：", font=FONT, font_size=26, color=GRAY_A)
        write_val   = MathTex(r"100.008", font_size=52, color=COLOR_HL)
        write_result = VGroup(write_label, write_val).arrange(RIGHT, buff=0.2).move_to(DOWN * 3.0)
        self.play(FadeIn(write_result, scale=0.9, shift=UP * 0.3), run_time=0.7)
        self.play(Indicate(write_val, scale_factor=1.05, color=COLOR_HL), run_time=0.5)

        # 用颜色标注各部分
        int_box = SurroundingRectangle(
            write_val[0][0:3], color=COLOR_INT, buff=0.04, stroke_width=2
        )
        dot_box = SurroundingRectangle(
            write_val[0][3], color=COLOR_DOT, buff=0.04, stroke_width=2
        )
        dec_box = SurroundingRectangle(
            write_val[0][4:7], color=COLOR_DEC, buff=0.04, stroke_width=2
        )
        self.play(Create(int_box), Create(dot_box), Create(dec_box), run_time=0.6)
        self.wait(1.8)

        self.play(FadeOut(VGroup(
            title, hear, s1, s2, s3, hline, write_result, int_box, dot_box, dec_box
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 6: 要点总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        box = RoundedRectangle(
            width=8.2, height=10.0,
            corner_radius=0.35,
            fill_color="#0f172a", fill_opacity=0.96,
            stroke_color=COLOR_HL, stroke_width=3
        ).move_to(UP * 0.5)
        self.play(FadeIn(box), run_time=0.3)

        sum_title = Text(
            "读写法要点总结", font=FONT,
            font_size=32, color=COLOR_HL, weight=BOLD
        ).move_to(UP * 5.0)
        self.play(Write(sum_title), run_time=0.5)

        # 读法部分
        read_head = Text(
            "【读法】", font=FONT, font_size=26, color=COLOR_INT, weight=BOLD
        ).move_to(UP * 3.8)
        self.play(FadeIn(read_head, shift=RIGHT * 0.2), run_time=0.4)

        read_items = VGroup(
            Text("① 整数部分按整数读法读", font=FONT, font_size=22, color=WHITE),
            Text('② 小数点读作"点"', font=FONT, font_size=22, color=WHITE),
            Text("③ 小数部分依次读每一位", font=FONT, font_size=22, color=WHITE),
            Text("   （包括 0，不能跳过）", font=FONT, font_size=20, color=GRAY_B),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(UP * 2.5)

        for item in read_items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.35)
            self.wait(0.15)

        div_line = Line(LEFT * 3.8, RIGHT * 3.8, color=GRAY_B, stroke_width=1)
        div_line.move_to(UP * 1.1)
        self.play(Create(div_line), run_time=0.3)

        # 写法部分
        write_head = Text(
            "【写法】", font=FONT, font_size=26, color=COLOR_DEC, weight=BOLD
        ).move_to(UP * 0.5)
        self.play(FadeIn(write_head, shift=RIGHT * 0.2), run_time=0.4)

        write_items = VGroup(
            Text("① 整数部分按整数写法写", font=FONT, font_size=22, color=WHITE),
            Text("② 小数点写在个位右下角", font=FONT, font_size=22, color=WHITE),
            Text("③ 小数部分依次写每一位", font=FONT, font_size=22, color=WHITE),
            Text("   （0 不能漏写）", font=FONT, font_size=20, color=GRAY_B),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN * 0.8)

        for item in write_items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.35)
            self.wait(0.15)

        # 两个典型例子
        eg1 = VGroup(
            MathTex(r"30.05", font_size=32, color=COLOR_HL),
            Text(" 读作 三十点零五", font=FONT, font_size=22, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1)

        eg2 = VGroup(
            Text("一百点零零八 写作 ", font=FONT, font_size=22, color=COLOR_HL),
            MathTex(r"100.008", font_size=32, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.1)

        examples = VGroup(eg1, eg2).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        examples.move_to(DOWN * 2.8)
        self.play(FadeIn(examples, shift=UP * 0.2), run_time=0.7)
        self.wait(2.5)

        self.play(FadeOut(VGroup(
            box, sum_title,
            read_head, read_items, div_line,
            write_head, write_items, examples
        )), run_time=0.5)

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
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
#   快速预览:  manim -pql 002_小数的读写.py DecimalReadWriteLesson
#   中等质量:  manim -qm  002_小数的读写.py DecimalReadWriteLesson
#   高质量:    manim -qh  002_小数的读写.py DecimalReadWriteLesson
# ======================================================================
