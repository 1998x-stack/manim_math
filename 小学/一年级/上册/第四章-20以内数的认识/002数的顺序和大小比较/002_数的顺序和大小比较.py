"""
数的顺序和大小比较 - Number Order and Comparison Animation
一年级上册 第四章 20以内数的认识

内容: 利用数轴认识20以内数的顺序，会比较两个数的大小
目标观众: 小学一年级学生
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


class NumberOrderComparison(Scene):
    """
    数的顺序和大小比较教学动画

    场景顺序:
    1. 开场介绍
    2. 数轴认识数的顺序
    3. 比较 12 > 10
    4. 比较 15 < 18
    5. 比较 13 = 13
    6. 规律总结
    7. 片尾关注
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_PRIMARY = "#4fc3f7"     # 浅蓝 - 主色
        self.COLOR_SECONDARY = "#81c784"   # 绿色 - 辅助
        self.COLOR_HIGHLIGHT = "#ffd54f"   # 黄色 - 高亮
        self.COLOR_GREATER = "#ef5350"     # 红色 - 大
        self.COLOR_LESS = "#42a5f5"        # 蓝色 - 小
        self.COLOR_EQUAL = "#66bb6a"       # 绿色 - 相等
        self.COLOR_NUMBERLINE = "#b0bec5"  # 灰色 - 数轴

        # 执行各场景
        self.scene_1_opening()
        self.scene_2_number_line()
        self.scene_3_greater_than()
        self.scene_4_less_than()
        self.scene_5_equal()
        self.scene_6_summary()
        self.scene_7_outro()

    # ===================== 场景1: 开场 =====================
    def scene_1_opening(self):
        """开场：钩子问题 + 标题"""
        # 作者信息
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Heiti SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.author = author
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子问题
        hook = Text(
            "12 和 15，谁更大？",
            font="Heiti SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 4.5)

        self.play(Write(hook), run_time=0.8)
        self.wait(0.5)

        # 副标题
        subtitle = Text(
            "数的顺序和大小比较",
            font="Heiti SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 3.5)

        grade_label = Text(
            "一年级 · 20以内数的认识",
            font="Heiti SC",
            font_size=22,
            color="#90a4ae"
        ).move_to(UP * 2.8)

        self.play(FadeIn(subtitle), run_time=0.5)
        self.play(FadeIn(grade_label), run_time=0.4)
        self.wait(0.8)

        # 展示三个关键符号
        symbols_label = Text(
            "今天学习三个符号：",
            font="Heiti SC",
            font_size=24,
            color="#cfd8dc"
        ).move_to(UP * 1.5)

        sym_greater = MathTex(r">", font_size=72, color=self.COLOR_GREATER)
        sym_less = MathTex(r"<", font_size=72, color=self.COLOR_LESS)
        sym_equal = MathTex(r"=", font_size=72, color=self.COLOR_EQUAL)

        symbols_row = VGroup(sym_greater, sym_less, sym_equal).arrange(RIGHT, buff=1.2)
        symbols_row.move_to(UP * 0.3)

        lbl_greater = Text("大于", font="Heiti SC", font_size=22, color=self.COLOR_GREATER)
        lbl_less = Text("小于", font="Heiti SC", font_size=22, color=self.COLOR_LESS)
        lbl_equal = Text("等于", font="Heiti SC", font_size=22, color=self.COLOR_EQUAL)

        labels_row = VGroup(lbl_greater, lbl_less, lbl_equal).arrange(RIGHT, buff=1.2)
        labels_row.move_to(DOWN * 0.7)
        # Align labels below their symbols
        for i in range(3):
            labels_row[i].set_x(symbols_row[i].get_x())

        self.play(FadeIn(symbols_label), run_time=0.4)
        self.play(
            Write(sym_greater),
            Write(sym_less),
            Write(sym_equal),
            run_time=0.8
        )
        self.play(
            FadeIn(lbl_greater),
            FadeIn(lbl_less),
            FadeIn(lbl_equal),
            run_time=0.5
        )
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(subtitle),
            FadeOut(grade_label),
            FadeOut(symbols_label),
            FadeOut(sym_greater),
            FadeOut(sym_less),
            FadeOut(sym_equal),
            FadeOut(lbl_greater),
            FadeOut(lbl_less),
            FadeOut(lbl_equal),
            run_time=0.5
        )

    # ===================== 场景2: 数轴认识顺序 =====================
    def scene_2_number_line(self):
        """展示数轴，认识0-20数的顺序"""

        title = Text(
            "数轴上的数的顺序",
            font="Heiti SC",
            font_size=34,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.0)

        self.play(Write(title), run_time=0.6)

        # 创建数轴 (0 到 20，水平，居中)
        # 数轴范围：从0到20，每格间距 0.37 (总宽约7.5)
        nl_start = np.array([-3.7, 2.0, 0])
        nl_end   = np.array([ 3.7, 2.0, 0])
        step = (nl_end[0] - nl_start[0]) / 20.0  # 每单位步长

        # 主数轴箭头
        nl_arrow = Arrow(
            nl_start + LEFT * 0.1,
            nl_end + RIGHT * 0.3,
            color=self.COLOR_NUMBERLINE,
            stroke_width=3,
            buff=0
        )

        self.play(Create(nl_arrow), run_time=0.8)

        # 刻度和数字标签
        ticks = VGroup()
        tick_labels = VGroup()

        for i in range(0, 21):
            x = nl_start[0] + i * step
            y = nl_start[1]

            tick_height = 0.18 if i % 5 == 0 else 0.10
            tick = Line(
                np.array([x, y - tick_height / 2, 0]),
                np.array([x, y + tick_height / 2, 0]),
                color=self.COLOR_NUMBERLINE,
                stroke_width=2
            )
            ticks.add(tick)

            # 只标0,5,10,15,20的数字，避免拥挤
            if i % 5 == 0:
                lbl = Text(
                    str(i),
                    font="Heiti SC",
                    font_size=20,
                    color=WHITE
                ).move_to(np.array([x, y - 0.45, 0]))
                tick_labels.add(lbl)

        self.play(Create(ticks), run_time=0.6)
        self.play(Write(tick_labels), run_time=0.5)

        # 说明文字：数轴特点
        explain1 = Text(
            "从左到右，数越来越大",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.7)

        self.play(FadeIn(explain1, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 用箭头指示方向
        direction_arrow = Arrow(
            np.array([-2.5, 0.1, 0]),
            np.array([2.5, 0.1, 0]),
            color=self.COLOR_HIGHLIGHT,
            buff=0,
            stroke_width=4
        )

        self.play(Create(direction_arrow), run_time=0.6)
        self.wait(0.4)

        # 点亮几个数字节点
        highlight_nums = [5, 10, 15, 20]
        highlight_dots = VGroup()
        for n in highlight_nums:
            x = nl_start[0] + n * step
            d = Dot(np.array([x, nl_start[1], 0]), radius=0.10, color=self.COLOR_HIGHLIGHT)
            highlight_dots.add(d)

        self.play(
            *[GrowFromCenter(d) for d in highlight_dots],
            run_time=0.6
        )
        self.wait(0.6)

        explain2 = Text(
            "右边的数 > 左边的数",
            font="Heiti SC",
            font_size=26,
            color=self.COLOR_SECONDARY
        ).move_to(DOWN * 0.4)

        self.play(FadeIn(explain2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.2)

        # 保存数轴信息供后续场景使用
        self.nl_start = nl_start
        self.nl_step = step
        self.nl_y = nl_start[1]
        self.nl_group = VGroup(nl_arrow, ticks, tick_labels)

        # 清理说明文字
        self.play(
            FadeOut(title),
            FadeOut(explain1),
            FadeOut(direction_arrow),
            FadeOut(highlight_dots),
            FadeOut(explain2),
            run_time=0.5
        )
        # 数轴缩小移到上方
        self.play(
            self.nl_group.animate.move_to(UP * 3.5).scale(0.85),
            run_time=0.8
        )

    # ===================== 辅助：在数轴上标记一个数 =====================
    def mark_number_on_nl(self, number, color, label_offset=None):
        """在缩放后的数轴上标记一个数并返回VGroup和位置"""
        if label_offset is None:
            label_offset = DOWN * 0.5
        # 数轴 scale(0.85) 且 move_to(UP*3.5)
        # 原始中心 x=0, y=2 => 缩放后 center = (0, 3.5)
        # 原始点 (x_orig, 2) => 缩放后 ((x_orig-0)*0.85 + 0, (2-2)*0.85 + 3.5)
        scale = 0.85
        x_orig = self.nl_start[0] + number * self.nl_step
        y_orig = self.nl_y
        x_new = x_orig * scale
        y_new = (y_orig - 2.0) * scale + 3.5

        pos = np.array([x_new, y_new, 0])
        dot = Dot(pos, radius=0.13, color=color)
        lbl = Text(str(number), font="Heiti SC", font_size=26, color=color)
        lbl.move_to(pos + np.array([0, -0.5 * scale, 0]))
        return VGroup(dot, lbl), pos

    # ===================== 场景3: 12 > 10 =====================
    def scene_3_greater_than(self):
        """演示 12 > 10"""

        title = Text(
            "比较 12 和 10",
            font="Heiti SC",
            font_size=34,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.0)

        self.play(Write(title), run_time=0.5)

        # 在数轴上标记 10 和 12
        mark10, pos10 = self.mark_number_on_nl(10, self.COLOR_LESS)
        mark12, pos12 = self.mark_number_on_nl(12, self.COLOR_GREATER)

        self.play(GrowFromCenter(mark10[0]), Write(mark10[1]), run_time=0.5)
        self.play(GrowFromCenter(mark12[0]), Write(mark12[1]), run_time=0.5)
        self.wait(0.3)

        # 箭头指示谁在右边
        cmp_arrow = Arrow(
            pos10 + UP * 0.35,
            pos12 + UP * 0.35,
            color=self.COLOR_HIGHLIGHT,
            buff=0.05,
            stroke_width=4
        )
        right_label = Text(
            "12 在 10 的右边",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.8)

        self.play(Create(cmp_arrow), run_time=0.5)
        self.play(FadeIn(right_label, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # 写出结论
        conclusion_lhs = Text("12", font="Heiti SC", font_size=64, color=self.COLOR_GREATER)
        conclusion_sym = MathTex(r">", font_size=72, color=WHITE)
        conclusion_rhs = Text("10", font="Heiti SC", font_size=64, color=self.COLOR_LESS)

        conclusion = VGroup(conclusion_lhs, conclusion_sym, conclusion_rhs)
        conclusion.arrange(RIGHT, buff=0.35)
        conclusion.move_to(UP * 0.5)

        self.play(
            Write(conclusion_lhs),
            Write(conclusion_sym),
            Write(conclusion_rhs),
            run_time=0.8
        )

        # 读法
        read_text = Text(
            "读作：十二  大于  十",
            font="Heiti SC",
            font_size=26,
            color="#cfd8dc"
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(read_text), run_time=0.5)

        # 强调大于号
        self.play(Indicate(conclusion_sym, color=self.COLOR_HIGHLIGHT, scale_factor=1.5), run_time=0.6)
        self.wait(1.0)

        # 小提示：开口朝大数
        tip_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.5,
            height=1.1,
            color=self.COLOR_GREATER,
            fill_opacity=0.15,
            stroke_width=2
        ).move_to(DOWN * 1.8)

        tip_text = Text(
            "记忆口诀：开口朝大数！",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(tip_box.get_center())

        self.play(Create(tip_box), FadeIn(tip_text), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(mark10),
            FadeOut(mark12),
            FadeOut(cmp_arrow),
            FadeOut(right_label),
            FadeOut(conclusion),
            FadeOut(read_text),
            FadeOut(tip_box),
            FadeOut(tip_text),
            run_time=0.5
        )

    # ===================== 场景4: 15 < 18 =====================
    def scene_4_less_than(self):
        """演示 15 < 18"""

        title = Text(
            "比较 15 和 18",
            font="Heiti SC",
            font_size=34,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.0)

        self.play(Write(title), run_time=0.5)

        # 在数轴上标记 15 和 18
        mark15, pos15 = self.mark_number_on_nl(15, self.COLOR_LESS)
        mark18, pos18 = self.mark_number_on_nl(18, self.COLOR_GREATER)

        self.play(GrowFromCenter(mark15[0]), Write(mark15[1]), run_time=0.5)
        self.play(GrowFromCenter(mark18[0]), Write(mark18[1]), run_time=0.5)
        self.wait(0.3)

        # 箭头指示（从18指向15，说明15在左边）
        cmp_arrow = Arrow(
            pos18 + UP * 0.35,
            pos15 + UP * 0.35,
            color=self.COLOR_HIGHLIGHT,
            buff=0.05,
            stroke_width=4
        )
        left_label = Text(
            "15 在 18 的左边",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.8)

        self.play(Create(cmp_arrow), run_time=0.5)
        self.play(FadeIn(left_label, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # 写出结论
        conclusion_lhs = Text("15", font="Heiti SC", font_size=64, color=self.COLOR_LESS)
        conclusion_sym = MathTex(r"<", font_size=72, color=WHITE)
        conclusion_rhs = Text("18", font="Heiti SC", font_size=64, color=self.COLOR_GREATER)

        conclusion = VGroup(conclusion_lhs, conclusion_sym, conclusion_rhs)
        conclusion.arrange(RIGHT, buff=0.35)
        conclusion.move_to(UP * 0.5)

        self.play(
            Write(conclusion_lhs),
            Write(conclusion_sym),
            Write(conclusion_rhs),
            run_time=0.8
        )

        # 读法
        read_text = Text(
            "读作：十五  小于  十八",
            font="Heiti SC",
            font_size=26,
            color="#cfd8dc"
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(read_text), run_time=0.5)
        self.play(Indicate(conclusion_sym, color=self.COLOR_HIGHLIGHT, scale_factor=1.5), run_time=0.6)
        self.wait(1.0)

        # 提示：小于号开口朝右（大数方向）
        tip_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.5,
            height=1.1,
            color=self.COLOR_LESS,
            fill_opacity=0.15,
            stroke_width=2
        ).move_to(DOWN * 1.8)

        tip_text = Text(
            "开口朝大数 18，所以用 <",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(tip_box.get_center())

        self.play(Create(tip_box), FadeIn(tip_text), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(mark15),
            FadeOut(mark18),
            FadeOut(cmp_arrow),
            FadeOut(left_label),
            FadeOut(conclusion),
            FadeOut(read_text),
            FadeOut(tip_box),
            FadeOut(tip_text),
            run_time=0.5
        )

    # ===================== 场景5: 13 = 13 =====================
    def scene_5_equal(self):
        """演示 13 = 13"""

        title = Text(
            "比较 13 和 13",
            font="Heiti SC",
            font_size=34,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 6.0)

        self.play(Write(title), run_time=0.5)

        # 在数轴上标记 13（两个相同的数在同一点）
        mark13, pos13 = self.mark_number_on_nl(13, self.COLOR_EQUAL)

        self.play(GrowFromCenter(mark13[0]), Write(mark13[1]), run_time=0.5)
        self.wait(0.3)

        # 两个数指向同一个位置
        same_label = Text(
            "两个数在同一个位置！",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 1.8)

        self.play(FadeIn(same_label, shift=UP * 0.2), run_time=0.4)
        self.wait(0.3)

        # 写出结论
        conclusion_lhs = Text("13", font="Heiti SC", font_size=64, color=self.COLOR_EQUAL)
        conclusion_sym = MathTex(r"=", font_size=72, color=WHITE)
        conclusion_rhs = Text("13", font="Heiti SC", font_size=64, color=self.COLOR_EQUAL)

        conclusion = VGroup(conclusion_lhs, conclusion_sym, conclusion_rhs)
        conclusion.arrange(RIGHT, buff=0.35)
        conclusion.move_to(UP * 0.5)

        self.play(
            Write(conclusion_lhs),
            Write(conclusion_sym),
            Write(conclusion_rhs),
            run_time=0.8
        )

        # 读法
        read_text = Text(
            "读作：十三  等于  十三",
            font="Heiti SC",
            font_size=26,
            color="#cfd8dc"
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(read_text), run_time=0.5)
        self.play(Indicate(conclusion_sym, color=self.COLOR_HIGHLIGHT, scale_factor=1.5), run_time=0.6)
        self.wait(1.0)

        # 提示：相同的数用等号
        tip_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.5,
            height=1.1,
            color=self.COLOR_EQUAL,
            fill_opacity=0.15,
            stroke_width=2
        ).move_to(DOWN * 1.8)

        tip_text = Text(
            "相同的数用 = 连接",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(tip_box.get_center())

        self.play(Create(tip_box), FadeIn(tip_text), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(mark13),
            FadeOut(same_label),
            FadeOut(conclusion),
            FadeOut(read_text),
            FadeOut(tip_box),
            FadeOut(tip_text),
            run_time=0.5
        )

        # 淡出数轴
        self.play(FadeOut(self.nl_group), run_time=0.5)

    # ===================== 场景6: 规律总结 =====================
    def scene_6_summary(self):
        """总结三个例子和规律"""

        title = Text(
            "总结",
            font="Heiti SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6.5)

        self.play(Write(title), run_time=0.5)

        # 三条例题回顾
        ex1_lhs = Text("12", font="Heiti SC", font_size=52, color=self.COLOR_GREATER)
        ex1_sym = MathTex(r">", font_size=60, color=WHITE)
        ex1_rhs = Text("10", font="Heiti SC", font_size=52, color=self.COLOR_LESS)
        ex1 = VGroup(ex1_lhs, ex1_sym, ex1_rhs).arrange(RIGHT, buff=0.3)

        ex2_lhs = Text("15", font="Heiti SC", font_size=52, color=self.COLOR_LESS)
        ex2_sym = MathTex(r"<", font_size=60, color=WHITE)
        ex2_rhs = Text("18", font="Heiti SC", font_size=52, color=self.COLOR_GREATER)
        ex2 = VGroup(ex2_lhs, ex2_sym, ex2_rhs).arrange(RIGHT, buff=0.3)

        ex3_lhs = Text("13", font="Heiti SC", font_size=52, color=self.COLOR_EQUAL)
        ex3_sym = MathTex(r"=", font_size=60, color=WHITE)
        ex3_rhs = Text("13", font="Heiti SC", font_size=52, color=self.COLOR_EQUAL)
        ex3 = VGroup(ex3_lhs, ex3_sym, ex3_rhs).arrange(RIGHT, buff=0.3)

        all_ex = VGroup(ex1, ex2, ex3).arrange(DOWN, buff=0.6)
        all_ex.move_to(UP * 3.8)

        self.play(FadeIn(ex1, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(ex2, shift=RIGHT * 0.3), run_time=0.4)
        self.play(FadeIn(ex3, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(0.5)

        # 分割线
        divider = Line(
            np.array([-4.0, 1.5, 0]),
            np.array([4.0, 1.5, 0]),
            color="#37474f",
            stroke_width=2
        )
        self.play(Create(divider), run_time=0.4)

        # 规律卡片标题
        rule_title = Text(
            "比大小的方法",
            font="Heiti SC",
            font_size=30,
            color=self.COLOR_PRIMARY
        ).move_to(UP * 1.0)

        self.play(Write(rule_title), run_time=0.5)

        # 规律1：数轴右边的数大
        rule1_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.8,
            height=0.85,
            color=self.COLOR_GREATER,
            fill_opacity=0.12,
            stroke_width=1.5
        ).move_to(UP * 0.1)

        rule1_text = Text(
            "数轴上，右边的数 > 左边的数",
            font="Heiti SC",
            font_size=22,
            color=WHITE
        ).move_to(rule1_box.get_center())

        self.play(Create(rule1_box), FadeIn(rule1_text), run_time=0.5)

        # 规律2：开口朝大数
        rule2_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.8,
            height=0.85,
            color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.12,
            stroke_width=1.5
        ).move_to(DOWN * 0.85)

        rule2_text = Text(
            "开口朝大数：大嘴巴张向大数",
            font="Heiti SC",
            font_size=22,
            color=WHITE
        ).move_to(rule2_box.get_center())

        self.play(Create(rule2_box), FadeIn(rule2_text), run_time=0.5)

        # 规律3：相同用等号
        rule3_box = RoundedRectangle(
            corner_radius=0.2,
            width=7.8,
            height=0.85,
            color=self.COLOR_EQUAL,
            fill_opacity=0.12,
            stroke_width=1.5
        ).move_to(DOWN * 1.8)

        rule3_text = Text(
            "两个数相同，用 = 连接",
            font="Heiti SC",
            font_size=22,
            color=WHITE
        ).move_to(rule3_box.get_center())

        self.play(Create(rule3_box), FadeIn(rule3_text), run_time=0.5)
        self.wait(1.5)

        # 口诀小节
        slogan_box = RoundedRectangle(
            corner_radius=0.3,
            width=7.8,
            height=1.6,
            color=self.COLOR_HIGHLIGHT,
            fill_opacity=0.2,
            stroke_width=2
        ).move_to(DOWN * 3.2)

        slogan_line1 = Text(
            "口诀：大嘴张向大数吃，",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 2.9)

        slogan_line2 = Text(
            "右大左小要记牢！",
            font="Heiti SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 3.5)

        self.play(Create(slogan_box), run_time=0.4)
        self.play(Write(slogan_line1), run_time=0.5)
        self.play(Write(slogan_line2), run_time=0.5)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(all_ex),
            FadeOut(divider),
            FadeOut(rule_title),
            FadeOut(rule1_box),
            FadeOut(rule1_text),
            FadeOut(rule2_box),
            FadeOut(rule2_text),
            FadeOut(rule3_box),
            FadeOut(rule3_text),
            FadeOut(slogan_box),
            FadeOut(slogan_line1),
            FadeOut(slogan_line2),
            run_time=0.6
        )

    # ===================== 场景7: 片尾 =====================
    def scene_7_outro(self):
        """片尾：关注信息"""

        # 作者名字放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Heiti SC",
            font_size=38,
            color=WHITE
        ).move_to(UP * 2.0)

        author_id = Text(
            "@emptyandcalm",
            font="Heiti SC",
            font_size=28,
            color="#90a4ae"
        ).move_to(UP * 1.2)

        self.play(
            Transform(self.author, author_name),
            run_time=0.7
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        # 关注口号
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Heiti SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 0.1)

        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.5)

        # 三个符号装饰
        deco_greater = MathTex(r">", font_size=80, color=self.COLOR_GREATER).move_to(DOWN * 1.2 + LEFT * 2.0)
        deco_less = MathTex(r"<", font_size=80, color=self.COLOR_LESS).move_to(DOWN * 1.2)
        deco_equal = MathTex(r"=", font_size=80, color=self.COLOR_EQUAL).move_to(DOWN * 1.2 + RIGHT * 2.0)

        self.play(
            GrowFromCenter(deco_greater),
            GrowFromCenter(deco_less),
            GrowFromCenter(deco_equal),
            run_time=0.7
        )

        # 闪烁动画
        self.play(
            Indicate(deco_greater, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            Indicate(deco_less, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            Indicate(deco_equal, color=self.COLOR_HIGHLIGHT, scale_factor=1.3),
            run_time=0.8
        )
        self.wait(1.2)

        # 全部淡出
        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(deco_greater),
            FadeOut(deco_less),
            FadeOut(deco_equal),
            run_time=1.0
        )
