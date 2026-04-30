"""
001_整十整百数乘一位数.py — 整十、整百数乘一位数 教学动画

知识点: 整十、整百数乘一位数的口算方法
  - 算理: 利用表内乘法推算
  - 如: 20×3, 想2个十×3=6个十, 即60
  - 整十数: 20×3=60, 30×4=120 等
  - 整百数: 200×3=600, 300×4=1200 等
  - 规律: 末位0可以先不写, 最后补上
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
COLOR_PRIMARY = "#3b82f6"       # 蓝色 主色
COLOR_TENS = "#22c55e"          # 绿色 整十数
COLOR_HUNDREDS = "#f59e0b"      # 橙色 整百数
COLOR_HL = "#fbbf24"            # 黄色高亮
COLOR_RESULT = "#ef4444"        # 红色结果
COLOR_UNIT = "#a78bfa"          # 紫色 位值
COLOR_AUTHOR = "#6b7280"        # 灰色作者信息
COLOR_BOX = "#1e3a5f"           # 深蓝 背景框
FONT = "PingFang SC"


# ======================================================================
# 主场景
# ======================================================================

class RoundNumberMultiplyLesson(Scene):
    """
    整十、整百数乘一位数教学动画
    场景顺序:
      1. 开场钩子 - 引出问题
      2. 复习表内乘法 - 2×3=6
      3. 整十数乘一位数 - 20×3=60 (算理)
      4. 整十数乘一位数 - 多例练习
      5. 整百数乘一位数 - 200×3=600 (算理)
      6. 整百数乘一位数 - 多例练习
      7. 规律总结
      8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = self.make_author()

        self.scene_1_opening()
        self.scene_2_review_times_table()
        self.scene_3_tens_reasoning()
        self.scene_4_tens_practice()
        self.scene_5_hundreds_reasoning()
        self.scene_6_hundreds_practice()
        self.scene_7_summary()
        self.scene_8_outro()

    # ------------------------------------------------------------------
    # 工具方法
    # ------------------------------------------------------------------

    def make_author(self):
        """创建作者标识"""
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    def make_formula_row(self, left_text, right_text, color_left=WHITE, color_right=COLOR_HL, font_size=36):
        """创建 左文字 = 右文字 的公式行"""
        left = Text(left_text, font=FONT, font_size=font_size, color=color_left)
        eq = Text("=", font=FONT, font_size=font_size, color=WHITE)
        right = Text(right_text, font=FONT, font_size=font_size, color=color_right)
        return VGroup(left, eq, right).arrange(RIGHT, buff=0.2)

    def make_unit_box(self, number_str, unit_str, num_color=WHITE, unit_color=COLOR_UNIT, font_size=28):
        """创建 数字+单位 的组合框"""
        num = Text(number_str, font=FONT, font_size=font_size, color=num_color)
        unit = Text(unit_str, font=FONT, font_size=font_size - 4, color=unit_color)
        return VGroup(num, unit).arrange(RIGHT, buff=0.1)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        hook = Text(
            "20×3 等于多少?",
            font=FONT,
            font_size=44,
            color=COLOR_HL,
        ).move_to(UP * 5.0)

        self.play(Write(hook), run_time=0.8)

        # 展示问题
        formula_q = VGroup(
            Text("20", font=FONT, font_size=72, color=COLOR_TENS),
            Text("×", font=FONT, font_size=64, color=WHITE),
            Text("3", font=FONT, font_size=72, color=COLOR_PRIMARY),
            Text("= ?", font=FONT, font_size=64, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.3).move_to(UP * 2.5)

        self.play(FadeIn(formula_q, shift=UP * 0.3), run_time=0.8)
        self.wait(0.6)

        sub = Text(
            "用表内乘法就能算出来!",
            font=FONT,
            font_size=26,
            color=GRAY_A,
        ).move_to(UP * 0.8)

        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(hook),
            FadeOut(formula_q),
            FadeOut(sub),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 复习表内乘法
    # ------------------------------------------------------------------

    def scene_2_review_times_table(self):
        title = Text("先复习表内乘法", font=FONT, font_size=36, color=WHITE)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 展示 2×3=6
        core_formula = VGroup(
            Text("2", font=FONT, font_size=80, color=COLOR_TENS),
            Text("×", font=FONT, font_size=70, color=WHITE),
            Text("3", font=FONT, font_size=80, color=COLOR_PRIMARY),
            Text("=", font=FONT, font_size=70, color=WHITE),
            Text("6", font=FONT, font_size=80, color=COLOR_RESULT),
        ).arrange(RIGHT, buff=0.25).move_to(UP * 2.5)

        self.play(FadeIn(core_formula[0]), FadeIn(core_formula[1]), FadeIn(core_formula[2]), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(core_formula[3]), FadeIn(core_formula[4]), run_time=0.5)

        # 小圆点直观图: 2行 3列 = 6个
        dot_group = VGroup()
        rows = 2
        cols = 3
        dot_spacing = 0.55
        dot_start_x = -0.75
        dot_start_y = 0.3

        for r in range(rows):
            for c in range(cols):
                dot = Circle(
                    radius=0.18,
                    color=COLOR_TENS,
                    fill_color=COLOR_TENS,
                    fill_opacity=0.8,
                    stroke_width=2,
                ).move_to(
                    np.array([dot_start_x + c * dot_spacing, dot_start_y - r * dot_spacing, 0.0])
                )
                dot_group.add(dot)

        self.play(FadeIn(dot_group, shift=UP * 0.2), run_time=0.7)

        count_label = Text("2行3列 = 6个", font=FONT, font_size=24, color=GRAY_A)
        count_label.move_to(DOWN * 0.6)
        self.play(FadeIn(count_label), run_time=0.4)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(core_formula),
            FadeOut(dot_group),
            FadeOut(count_label),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 整十数乘一位数 算理推导 (20×3=60)
    # ------------------------------------------------------------------

    def scene_3_tens_reasoning(self):
        title = Text("整十数乘一位数", font=FONT, font_size=34, color=COLOR_TENS)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 例题
        example_label = Text("例: 20 × 3 = ?", font=FONT, font_size=32, color=WHITE)
        example_label.move_to(UP * 4.5)
        self.play(FadeIn(example_label), run_time=0.5)

        # Step 1: 20 = 2个十
        step1_title = Text("第一步: 把 20 看成 2个十", font=FONT, font_size=24, color=COLOR_HL)
        step1_title.move_to(UP * 3.4)
        self.play(FadeIn(step1_title), run_time=0.5)

        # 位值图: 2个十的方块
        tens_blocks = VGroup()
        block_w = 1.0
        block_h = 1.6
        gap = 0.25
        block_start_x = -1.1

        for i in range(2):
            block = Rectangle(
                width=block_w,
                height=block_h,
                color=COLOR_TENS,
                fill_color=COLOR_TENS,
                fill_opacity=0.3,
                stroke_width=3,
            ).move_to(np.array([block_start_x + i * (block_w + gap), 1.9, 0.0]))
            label_ten = Text("10", font=FONT, font_size=22, color=COLOR_TENS)
            label_ten.move_to(block.get_center())
            tens_blocks.add(VGroup(block, label_ten))

        brace_tens = Brace(tens_blocks, direction=DOWN, color=COLOR_HL)
        brace_label_tens = Text("2个十", font=FONT, font_size=22, color=COLOR_HL)
        brace_label_tens.next_to(brace_tens, DOWN, buff=0.15)

        self.play(FadeIn(tens_blocks, shift=UP * 0.3), run_time=0.7)
        self.play(Create(brace_tens), FadeIn(brace_label_tens), run_time=0.5)
        self.wait(0.5)

        # Step 2: 乘以3 → 变成3组
        step2_title = Text("第二步: 2个十 × 3 = 6个十", font=FONT, font_size=24, color=COLOR_HL)
        step2_title.move_to(UP * 3.4)
        self.play(ReplacementTransform(step1_title, step2_title), run_time=0.5)

        # 展示 3 组
        all_blocks = VGroup()
        group_colors = [COLOR_TENS, "#34d399", "#6ee7b7"]
        total_groups = 3
        total_w = total_groups * block_w + (total_groups - 1) * gap
        start_x = -total_w / 2 + block_w / 2

        for g in range(total_groups):
            col_color = group_colors[g % len(group_colors)]
            block = Rectangle(
                width=block_w,
                height=block_h,
                color=col_color,
                fill_color=col_color,
                fill_opacity=0.3,
                stroke_width=3,
            ).move_to(np.array([start_x + g * (block_w + gap), 1.9, 0.0]))
            label_ten = Text("10", font=FONT, font_size=22, color=col_color)
            label_ten.move_to(block.get_center())
            all_blocks.add(VGroup(block, label_ten))

        # 移出原来的2个, 换成3组
        self.play(
            FadeOut(tens_blocks),
            FadeOut(brace_tens),
            FadeOut(brace_label_tens),
            run_time=0.4,
        )
        self.play(FadeIn(all_blocks, shift=UP * 0.2), run_time=0.8)

        brace_all = Brace(all_blocks, direction=DOWN, color=COLOR_HL)
        brace_label_all = Text("6个十", font=FONT, font_size=22, color=COLOR_HL)
        brace_label_all.next_to(brace_all, DOWN, buff=0.15)

        self.play(Create(brace_all), FadeIn(brace_label_all), run_time=0.5)
        self.wait(0.5)

        # Step 3: 6个十 = 60
        step3_title = Text("第三步: 6个十 = 60", font=FONT, font_size=24, color=COLOR_HL)
        step3_title.move_to(UP * 3.4)
        self.play(ReplacementTransform(step2_title, step3_title), run_time=0.5)

        # 关键算式
        key_chain = VGroup(
            Text("2个十", font=FONT, font_size=28, color=COLOR_TENS),
            Text("× 3", font=FONT, font_size=28, color=COLOR_PRIMARY),
            Text("= 6个十", font=FONT, font_size=28, color=COLOR_RESULT),
            Text("= 60", font=FONT, font_size=28, color=COLOR_RESULT),
        ).arrange(RIGHT, buff=0.2).move_to(DOWN * 1.0)

        self.play(FadeIn(key_chain, shift=UP * 0.2), run_time=0.7)

        # 最终结论
        conclusion = VGroup(
            Text("所以", font=FONT, font_size=28, color=GRAY_A),
            Text("20 × 3 = 60", font=FONT, font_size=38, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 2.5)

        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.7)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(example_label),
            FadeOut(step3_title),
            FadeOut(all_blocks),
            FadeOut(brace_all),
            FadeOut(brace_label_all),
            FadeOut(key_chain),
            FadeOut(conclusion),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 4: 整十数练习 (多例)
    # ------------------------------------------------------------------

    def scene_4_tens_practice(self):
        title = Text("整十数乘一位数 — 练习", font=FONT, font_size=30, color=COLOR_TENS)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 技巧说明
        tip = VGroup(
            Text("技巧: 先算乘法, 再在末尾加0", font=FONT, font_size=22, color=GRAY_A),
        ).move_to(UP * 4.6)
        self.play(FadeIn(tip), run_time=0.5)

        # 三道例题: 依次出现, 分步展示
        examples = [
            ("20 × 3", "2 × 3 = 6", "60"),
            ("30 × 4", "3 × 4 = 12", "120"),
            ("50 × 6", "5 × 6 = 30", "300"),
        ]

        y_positions = [2.8, 0.8, -1.2]
        example_groups = []

        for i, (question, middle, answer) in enumerate(examples):
            y = y_positions[i]

            # 问题
            q_text = Text(question, font=FONT, font_size=32, color=WHITE)
            q_text.move_to(np.array([-2.5, y, 0.0]))

            # 想: 中间步骤
            think_label = Text("想:", font=FONT, font_size=22, color=GRAY_B)
            think_label.move_to(np.array([-0.2, y + 0.55, 0.0]))

            think_text = Text(middle, font=FONT, font_size=22, color=COLOR_TENS)
            think_text.move_to(np.array([0.8, y + 0.55, 0.0]))

            arrow = Text("→", font=FONT, font_size=28, color=COLOR_HL)
            arrow.move_to(np.array([0.3, y, 0.0]))

            # 结果
            result_text = Text(answer, font=FONT, font_size=36, color=COLOR_RESULT)
            result_text.move_to(np.array([1.8, y, 0.0]))

            grp = VGroup(q_text, think_label, think_text, arrow, result_text)
            example_groups.append(grp)

            # 依次动画
            self.play(FadeIn(q_text), run_time=0.4)
            self.play(FadeIn(think_label), FadeIn(think_text), run_time=0.4)
            self.play(FadeIn(arrow), FadeIn(result_text), run_time=0.4)
            self.wait(0.5)

        # 等待学生看
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(tip),
            *[FadeOut(g) for g in example_groups],
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 5: 整百数乘一位数 算理推导 (200×3=600)
    # ------------------------------------------------------------------

    def scene_5_hundreds_reasoning(self):
        title = Text("整百数乘一位数", font=FONT, font_size=34, color=COLOR_HUNDREDS)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 例题
        example_label = Text("例: 200 × 3 = ?", font=FONT, font_size=32, color=WHITE)
        example_label.move_to(UP * 4.5)
        self.play(FadeIn(example_label), run_time=0.5)

        # 类比推理展示
        analogy_title = Text("类比整十数, 思考过程:", font=FONT, font_size=24, color=COLOR_HL)
        analogy_title.move_to(UP * 3.4)
        self.play(FadeIn(analogy_title), run_time=0.5)

        # 对比链:  2×3=6  →  20×3=60  →  200×3=600
        compare_rows = [
            ("2 × 3", "=", "6", GRAY_A, GRAY_A, GRAY_B),
            ("20 × 3", "=", "60", COLOR_TENS, COLOR_TENS, COLOR_TENS),
            ("200 × 3", "=", "600", COLOR_HUNDREDS, COLOR_HUNDREDS, COLOR_RESULT),
        ]

        row_y = [2.3, 1.3, 0.3]
        row_items = []
        arrow_items = []

        for i, (left, eq, right, lc, ec, rc) in enumerate(compare_rows):
            left_t = Text(left, font=FONT, font_size=30, color=lc)
            eq_t = Text(eq, font=FONT, font_size=30, color=ec)
            right_t = Text(right, font=FONT, font_size=30, color=rc)
            row = VGroup(left_t, eq_t, right_t).arrange(RIGHT, buff=0.3)
            row.move_to(np.array([0.0, row_y[i], 0.0]))
            row_items.append(row)

        for i, row in enumerate(row_items):
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
            if i < len(row_items) - 1:
                # 下箭头
                arrow_down = Text("↓", font=FONT, font_size=24, color=COLOR_HL)
                arrow_down.move_to(np.array([2.8, (row_y[i] + row_y[i + 1]) / 2, 0.0]))
                self.play(FadeIn(arrow_down), run_time=0.3)
                arrow_items.append(arrow_down)
            self.wait(0.4)

        all_row_items = row_items + arrow_items

        # 规律说明
        rule_box_bg = RoundedRectangle(
            width=7.0,
            height=1.6,
            corner_radius=0.2,
            color=COLOR_HUNDREDS,
            stroke_width=2,
            fill_color=COLOR_BOX,
            fill_opacity=0.6,
        ).move_to(DOWN * 1.8)

        rule_text = VGroup(
            Text("2个百 × 3 = 6个百 = 600", font=FONT, font_size=24, color=COLOR_HL),
        ).move_to(DOWN * 1.8)

        self.play(FadeIn(rule_box_bg), run_time=0.4)
        self.play(FadeIn(rule_text), run_time=0.5)

        # 结论
        conclusion = VGroup(
            Text("所以", font=FONT, font_size=28, color=GRAY_A),
            Text("200 × 3 = 600", font=FONT, font_size=38, color=COLOR_HL),
        ).arrange(RIGHT, buff=0.3).move_to(DOWN * 3.2)

        self.play(FadeIn(conclusion, shift=UP * 0.3), run_time=0.7)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(example_label),
            FadeOut(analogy_title),
            *[FadeOut(r) for r in all_row_items],
            FadeOut(rule_box_bg),
            FadeOut(rule_text),
            FadeOut(conclusion),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 6: 整百数练习 (多例)
    # ------------------------------------------------------------------

    def scene_6_hundreds_practice(self):
        title = Text("整百数乘一位数 — 练习", font=FONT, font_size=30, color=COLOR_HUNDREDS)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.5)

        # 技巧说明
        tip = Text("技巧: 先算乘法, 再在末尾加两个0", font=FONT, font_size=22, color=GRAY_A)
        tip.move_to(UP * 4.6)
        self.play(FadeIn(tip), run_time=0.5)

        examples = [
            ("200 × 3", "2 × 3 = 6", "600"),
            ("300 × 4", "3 × 4 = 12", "1200"),
            ("400 × 5", "4 × 5 = 20", "2000"),
        ]

        y_positions = [2.8, 0.8, -1.2]
        example_groups = []

        for i, (question, middle, answer) in enumerate(examples):
            y = y_positions[i]

            q_text = Text(question, font=FONT, font_size=32, color=WHITE)
            q_text.move_to(np.array([-2.5, y, 0.0]))

            think_label = Text("想:", font=FONT, font_size=22, color=GRAY_B)
            think_label.move_to(np.array([-0.2, y + 0.55, 0.0]))

            think_text = Text(middle, font=FONT, font_size=22, color=COLOR_HUNDREDS)
            think_text.move_to(np.array([0.9, y + 0.55, 0.0]))

            arrow = Text("→", font=FONT, font_size=28, color=COLOR_HL)
            arrow.move_to(np.array([0.3, y, 0.0]))

            result_text = Text(answer, font=FONT, font_size=36, color=COLOR_RESULT)
            result_text.move_to(np.array([1.9, y, 0.0]))

            grp = VGroup(q_text, think_label, think_text, arrow, result_text)
            example_groups.append(grp)

            self.play(FadeIn(q_text), run_time=0.4)
            self.play(FadeIn(think_label), FadeIn(think_text), run_time=0.4)
            self.play(FadeIn(arrow), FadeIn(result_text), run_time=0.4)
            self.wait(0.5)

        self.wait(1.5)

        self.play(
            FadeOut(title),
            FadeOut(tip),
            *[FadeOut(g) for g in example_groups],
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 规律总结
    # ------------------------------------------------------------------

    def scene_7_summary(self):
        title = Text("口算规律总结", font=FONT, font_size=36, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 背景卡片
        card = RoundedRectangle(
            width=7.8,
            height=10.5,
            corner_radius=0.3,
            color=WHITE,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=0.04,
        ).move_to(UP * 0.2)
        self.play(FadeIn(card), run_time=0.4)

        # 条目 1: 整十数
        item1_head = Text("整十数 × 一位数", font=FONT, font_size=28, color=COLOR_TENS)
        item1_head.move_to(UP * 3.8 + LEFT * 0.5)

        item1_rule = VGroup(
            Text("先算: 2 × 3 = 6", font=FONT, font_size=22, color=GRAY_A),
            Text("再加0: 20 × 3 = 60", font=FONT, font_size=22, color=COLOR_TENS),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item1_rule.move_to(UP * 2.8 + LEFT * 0.3)

        self.play(FadeIn(item1_head, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(item1_rule, shift=RIGHT * 0.3), run_time=0.5)

        # 分割线
        divider1 = Line(
            np.array([-3.5, 1.8, 0.0]),
            np.array([3.5, 1.8, 0.0]),
            color=GRAY_B,
            stroke_width=1,
        )
        self.play(Create(divider1), run_time=0.3)

        # 条目 2: 整百数
        item2_head = Text("整百数 × 一位数", font=FONT, font_size=28, color=COLOR_HUNDREDS)
        item2_head.move_to(UP * 1.3 + LEFT * 0.5)

        item2_rule = VGroup(
            Text("先算: 2 × 3 = 6", font=FONT, font_size=22, color=GRAY_A),
            Text("再加00: 200 × 3 = 600", font=FONT, font_size=22, color=COLOR_HUNDREDS),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item2_rule.move_to(UP * 0.3 + LEFT * 0.3)

        self.play(FadeIn(item2_head, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(item2_rule, shift=RIGHT * 0.3), run_time=0.5)

        # 分割线
        divider2 = Line(
            np.array([-3.5, -0.7, 0.0]),
            np.array([3.5, -0.7, 0.0]),
            color=GRAY_B,
            stroke_width=1,
        )
        self.play(Create(divider2), run_time=0.3)

        # 条目 3: 核心口诀
        item3_head = Text("核心口诀", font=FONT, font_size=28, color=COLOR_HL)
        item3_head.move_to(DOWN * 1.1 + LEFT * 0.5)

        item3_body = VGroup(
            Text("有几个0, 末尾就加几个0", font=FONT, font_size=22, color=GRAY_A),
            Text("位值帮你快速口算!", font=FONT, font_size=24, color=COLOR_HL),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        item3_body.move_to(DOWN * 2.1 + LEFT * 0.3)

        self.play(FadeIn(item3_head, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(item3_body, shift=RIGHT * 0.3), run_time=0.5)

        # 对比框
        compare_bg = RoundedRectangle(
            width=7.0,
            height=1.6,
            corner_radius=0.2,
            color=COLOR_HL,
            stroke_width=2,
            fill_color=COLOR_BOX,
            fill_opacity=0.6,
        ).move_to(DOWN * 3.7)

        compare_formulas = VGroup(
            Text("20×3=60", font=FONT, font_size=26, color=COLOR_TENS),
            Text("200×3=600", font=FONT, font_size=26, color=COLOR_HUNDREDS),
        ).arrange(RIGHT, buff=0.8).move_to(DOWN * 3.7)

        self.play(FadeIn(compare_bg), run_time=0.3)
        self.play(FadeIn(compare_formulas, shift=UP * 0.2), run_time=0.5)

        self.wait(3.0)

        self.play(
            FadeOut(title),
            FadeOut(card),
            FadeOut(item1_head),
            FadeOut(item1_rule),
            FadeOut(divider1),
            FadeOut(item2_head),
            FadeOut(item2_rule),
            FadeOut(divider2),
            FadeOut(item3_head),
            FadeOut(item3_body),
            FadeOut(compare_bg),
            FadeOut(compare_formulas),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 8: 片尾
    # ------------------------------------------------------------------

    def scene_8_outro(self):
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT,
            font_size=38,
            color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT,
            font_size=28,
            color=GRAY_B,
        ).move_to(UP * 0.6)

        self.play(
            ReplacementTransform(self.author, author_big),
            run_time=0.8,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        follow = Text(
            "关注我, 学更多数学知识!",
            font=FONT,
            font_size=28,
            color=COLOR_HL,
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow, shift=UP * 0.2), run_time=0.6)

        # 装饰: 数字动画
        deco_formulas = VGroup(
            Text("20×3=60", font=FONT, font_size=22, color=COLOR_TENS),
            Text("200×4=800", font=FONT, font_size=22, color=COLOR_HUNDREDS),
            Text("30×5=150", font=FONT, font_size=22, color=COLOR_TENS),
        ).arrange(DOWN, buff=0.35).move_to(DOWN * 2.8)

        self.play(FadeIn(deco_formulas, shift=UP * 0.3), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(author_big),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco_formulas),
            run_time=1.0,
        )


# 运行命令:
# manim -pql 001_整十整百数乘一位数.py RoundNumberMultiplyLesson   # 快速预览
# manim -qm 001_整十整百数乘一位数.py RoundNumberMultiplyLesson    # 中等质量
# manim -qh 001_整十整百数乘一位数.py RoundNumberMultiplyLesson    # 高质量
