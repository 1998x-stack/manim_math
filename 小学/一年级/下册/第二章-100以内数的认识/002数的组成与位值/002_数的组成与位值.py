"""
数的组成与位值 - Number Composition and Place Value
一年级下册 第二章 100以内数的认识

内容: 几个十和几个一，数位（百位、十位、个位），位值概念
目标受众: 一年级学生
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


class NumberCompositionPlaceValue(Scene):
    """
    数的组成与位值教学动画

    场景顺序:
    1. 开场 - 引出问题
    2. 认识23 - 用十块和个块展示
    3. 认识32 - 对比展示
    4. 计数器 - 数位概念
    5. 位值深化 - 同一数字不同位置
    6. 总结
    7. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 颜色配置
        self.COLOR_TEN = "#e74c3c"        # 红色 - 十位/十块
        self.COLOR_ONE = "#3498db"        # 蓝色 - 个位/个块
        self.COLOR_HIGHLIGHT = "#f1c40f"  # 黄色 - 高亮
        self.COLOR_TITLE = "#ecf0f1"      # 白色 - 标题
        self.COLOR_SUBTITLE = "#bdc3c7"   # 灰色 - 副标题
        self.COLOR_BG_CARD = "#16213e"    # 深蓝 - 卡片背景

        # 作者标识
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)

        self.play(FadeIn(self.author_info), run_time=0.3)

        self.scene_1_opening()
        self.scene_2_number_23()
        self.scene_3_number_32()
        self.scene_4_place_value_table()
        self.scene_5_place_value_insight()
        self.scene_6_summary()
        self.scene_7_outro()

    # ─────────────────────────────────────────────────────────────────────
    # 辅助函数
    # ─────────────────────────────────────────────────────────────────────

    def make_ten_block(self, position, color=None):
        """创建一个'十块'（竖条，由10个小方格组成）"""
        if color is None:
            color = self.COLOR_TEN
        block = VGroup()
        for i in range(10):
            cell = Square(
                side_length=0.18,
                stroke_width=1.5,
                stroke_color=color,
                fill_color=color,
                fill_opacity=0.6
            )
            cell.move_to(position + DOWN * i * 0.18)
            block.add(cell)
        return block

    def make_one_block(self, position, color=None):
        """创建一个'个块'（小正方形）"""
        if color is None:
            color = self.COLOR_ONE
        cell = Square(
            side_length=0.28,
            stroke_width=1.5,
            stroke_color=color,
            fill_color=color,
            fill_opacity=0.6
        )
        cell.move_to(position)
        return cell

    # ─────────────────────────────────────────────────────────────────────
    # Scene 1: 开场
    # ─────────────────────────────────────────────────────────────────────

    def scene_1_opening(self):
        # 大标题
        title = Text(
            "数的组成与位值",
            font="PingFang SC",
            font_size=52,
            color=self.COLOR_TITLE,
            weight=BOLD
        )
        title.move_to(UP * 5.5)

        # 问题钩子
        hook_line1 = Text(
            "23 和 32",
            font="PingFang SC",
            font_size=80,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        )
        hook_line1.move_to(UP * 3.5)

        hook_line2 = Text(
            "看起来像，意思却不同？",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_SUBTITLE
        )
        hook_line2.move_to(UP * 2.3)

        # 装饰性背景数字
        deco_left = Text(
            "2",
            font="PingFang SC",
            font_size=160,
            color="#1e2a3a"
        ).move_to([-2.5, 0.0, 0])

        deco_right = Text(
            "3",
            font="PingFang SC",
            font_size=160,
            color="#1e2a3a"
        ).move_to([2.5, 0.0, 0])

        # 动画
        self.play(FadeIn(deco_left), FadeIn(deco_right), run_time=0.4)
        self.play(Write(title), run_time=0.7)
        self.play(GrowFromCenter(hook_line1), run_time=0.8)
        self.play(FadeIn(hook_line2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(hook_line1),
            FadeOut(hook_line2),
            FadeOut(deco_left),
            FadeOut(deco_right),
            run_time=0.5
        )

    # ─────────────────────────────────────────────────────────────────────
    # Scene 2: 认识23 = 2个十 + 3个一
    # ─────────────────────────────────────────────────────────────────────

    def scene_2_number_23(self):
        # 场景标题
        scene_title = Text(
            "认识数字 23",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_TITLE
        )
        scene_title.move_to(UP * 5.8)
        self.play(FadeIn(scene_title), run_time=0.4)

        # 大数字 23
        num_23 = Text(
            "23",
            font="PingFang SC",
            font_size=120,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        )
        num_23.move_to(UP * 4.3)
        self.play(GrowFromCenter(num_23), run_time=0.7)
        self.wait(0.3)

        # ---- 展示 2个十块 ----
        ten_label = Text(
            "2 个十",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_TEN,
            weight=BOLD
        )
        ten_label.move_to(UP * 2.8)
        self.play(FadeIn(ten_label), run_time=0.4)

        # 2个十块，左侧区域
        ten_blocks = VGroup()
        for i in range(2):
            blk = self.make_ten_block(
                np.array([-2.2 + i * 0.55, 1.3, 0])
            )
            ten_blocks.add(blk)

        self.play(FadeIn(ten_blocks), run_time=0.8)

        ten_value_txt = Text(
            "= 20",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_TEN
        )
        ten_value_txt.move_to([-1.65, 0.05, 0])
        self.play(Write(ten_value_txt), run_time=0.5)
        self.wait(0.4)

        # ---- 展示 3个一块 ----
        one_label = Text(
            "3 个一",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_ONE,
            weight=BOLD
        )
        one_label.move_to([2.0, 2.8, 0])
        self.play(FadeIn(one_label), run_time=0.4)

        one_blocks = VGroup()
        one_positions = [
            np.array([1.5, 1.3, 0]),
            np.array([1.9, 1.3, 0]),
            np.array([2.3, 1.3, 0]),
        ]
        for pos in one_positions:
            blk = self.make_one_block(pos)
            one_blocks.add(blk)

        self.play(FadeIn(one_blocks), run_time=0.6)

        one_value_txt = Text(
            "= 3",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_ONE
        )
        one_value_txt.move_to([2.0, 0.05, 0])
        self.play(Write(one_value_txt), run_time=0.5)
        self.wait(0.4)

        # ---- 合并公式 ----
        formula_parts = VGroup(
            Text("23", font="PingFang SC",
                 font_size=36, color=self.COLOR_HIGHLIGHT, weight=BOLD),
            Text("=", font="PingFang SC",
                 font_size=36, color=WHITE),
            Text("2", font="PingFang SC",
                 font_size=36, color=self.COLOR_TEN, weight=BOLD),
            Text("个十", font="PingFang SC",
                 font_size=36, color=self.COLOR_TEN),
            Text("+", font="PingFang SC",
                 font_size=36, color=WHITE),
            Text("3", font="PingFang SC",
                 font_size=36, color=self.COLOR_ONE, weight=BOLD),
            Text("个一", font="PingFang SC",
                 font_size=36, color=self.COLOR_ONE),
        ).arrange(RIGHT, buff=0.12)
        formula_parts.move_to(DOWN * 1.5)

        self.play(FadeIn(formula_parts, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        # 强调：数字"2"在十位
        arrow_ten = Arrow(
            start=np.array([-0.5, 3.6, 0]),
            end=ten_label.get_right() + LEFT * 0.1,
            color=self.COLOR_TEN,
            buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )
        self.play(GrowArrow(arrow_ten), run_time=0.5)
        self.play(
            Indicate(num_23[0], color=self.COLOR_TEN, scale_factor=1.4),
            run_time=0.7
        )
        self.wait(0.5)
        self.play(FadeOut(arrow_ten), run_time=0.3)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(num_23),
            FadeOut(ten_label),
            FadeOut(ten_blocks),
            FadeOut(ten_value_txt),
            FadeOut(one_label),
            FadeOut(one_blocks),
            FadeOut(one_value_txt),
            FadeOut(formula_parts),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────────────────────────
    # Scene 3: 认识32 对比展示
    # ─────────────────────────────────────────────────────────────────────

    def scene_3_number_32(self):
        scene_title = Text(
            "再看数字 32",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_TITLE
        )
        scene_title.move_to(UP * 5.8)
        self.play(FadeIn(scene_title), run_time=0.4)

        # 大数字32
        COLOR_32 = "#e67e22"
        num_32 = Text(
            "32",
            font="PingFang SC",
            font_size=120,
            color=COLOR_32,
            weight=BOLD
        )
        num_32.move_to(UP * 4.3)
        self.play(GrowFromCenter(num_32), run_time=0.7)
        self.wait(0.3)

        # ---- 3个十块 ----
        ten_label = Text(
            "3 个十",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_TEN,
            weight=BOLD
        )
        ten_label.move_to(UP * 2.8)
        self.play(FadeIn(ten_label), run_time=0.3)

        ten_blocks = VGroup()
        for i in range(3):
            blk = self.make_ten_block(
                np.array([-2.7 + i * 0.55, 1.3, 0])
            )
            ten_blocks.add(blk)

        self.play(FadeIn(ten_blocks), run_time=0.8)

        ten_value_txt = Text(
            "= 30",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_TEN
        )
        ten_value_txt.move_to([-1.4, 0.05, 0])
        self.play(Write(ten_value_txt), run_time=0.5)
        self.wait(0.3)

        # ---- 2个一块 ----
        one_label = Text(
            "2 个一",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_ONE,
            weight=BOLD
        )
        one_label.move_to([2.0, 2.8, 0])
        self.play(FadeIn(one_label), run_time=0.3)

        one_blocks = VGroup()
        one_positions = [
            np.array([1.7, 1.3, 0]),
            np.array([2.1, 1.3, 0]),
        ]
        for pos in one_positions:
            blk = self.make_one_block(pos)
            one_blocks.add(blk)
        self.play(FadeIn(one_blocks), run_time=0.5)

        one_value_txt = Text(
            "= 2",
            font="PingFang SC",
            font_size=32,
            color=self.COLOR_ONE
        )
        one_value_txt.move_to([2.0, 0.05, 0])
        self.play(Write(one_value_txt), run_time=0.5)
        self.wait(0.4)

        # 合并公式
        formula_32 = VGroup(
            Text("32", font="PingFang SC",
                 font_size=36, color=COLOR_32, weight=BOLD),
            Text("=", font="PingFang SC",
                 font_size=36, color=WHITE),
            Text("3", font="PingFang SC",
                 font_size=36, color=self.COLOR_TEN, weight=BOLD),
            Text("个十", font="PingFang SC",
                 font_size=36, color=self.COLOR_TEN),
            Text("+", font="PingFang SC",
                 font_size=36, color=WHITE),
            Text("2", font="PingFang SC",
                 font_size=36, color=self.COLOR_ONE, weight=BOLD),
            Text("个一", font="PingFang SC",
                 font_size=36, color=self.COLOR_ONE),
        ).arrange(RIGHT, buff=0.12)
        formula_32.move_to(DOWN * 1.5)

        self.play(FadeIn(formula_32, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        # ---- 关键对比提示 ----
        compare_bg = RoundedRectangle(
            corner_radius=0.25,
            width=7.5,
            height=1.4,
            fill_color=self.COLOR_BG_CARD,
            fill_opacity=0.95,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(DOWN * 3.3)

        compare_txt = Text(
            "23 ≠ 32    位置决定大小！",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 3.3)

        self.play(FadeIn(compare_bg), Write(compare_txt), run_time=0.7)
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(num_32),
            FadeOut(ten_label),
            FadeOut(ten_blocks),
            FadeOut(ten_value_txt),
            FadeOut(one_label),
            FadeOut(one_blocks),
            FadeOut(one_value_txt),
            FadeOut(formula_32),
            FadeOut(compare_bg),
            FadeOut(compare_txt),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────────────────────────
    # Scene 4: 数位表格
    # ─────────────────────────────────────────────────────────────────────

    def scene_4_place_value_table(self):
        scene_title = Text(
            "认识数位",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_TITLE
        )
        scene_title.move_to(UP * 5.8)
        self.play(FadeIn(scene_title), run_time=0.4)

        # ---- 数位表格（百位 | 十位 | 个位）----
        table_center_y = 4.0
        table_w = 7.0
        table_h = 2.2

        table_bg = RoundedRectangle(
            corner_radius=0.2,
            width=table_w,
            height=table_h,
            fill_color=self.COLOR_BG_CARD,
            fill_opacity=0.95,
            stroke_color="#444466",
            stroke_width=2
        ).move_to([0.0, table_center_y, 0])

        self.play(FadeIn(table_bg), run_time=0.3)

        # 列的x坐标（三列等分）
        col_w = table_w / 3.0
        col_xs = [
            -col_w,   # 百位
            0.0,      # 十位
            col_w     # 个位
        ]

        # 水平分隔线
        h_div_y = table_center_y + 0.55
        h_divider = Line(
            [-table_w / 2, h_div_y, 0],
            [table_w / 2, h_div_y, 0],
            stroke_color="#444466",
            stroke_width=2
        )

        # 竖直分隔线
        v_div1 = Line(
            [-col_w / 2, table_center_y + 1.1, 0],
            [-col_w / 2, table_center_y - 1.1, 0],
            stroke_color="#444466",
            stroke_width=2
        )
        v_div2 = Line(
            [col_w / 2, table_center_y + 1.1, 0],
            [col_w / 2, table_center_y - 1.1, 0],
            stroke_color="#444466",
            stroke_width=2
        )

        self.play(
            Create(h_divider),
            Create(v_div1),
            Create(v_div2),
            run_time=0.4
        )

        # 列标题行
        title_y = table_center_y + 0.82
        bai_title = Text("百位", font="PingFang SC",
                         font_size=28, color=WHITE)
        bai_title.move_to([col_xs[0], title_y, 0])

        shi_title = Text("十位", font="PingFang SC",
                         font_size=28, color=self.COLOR_TEN)
        shi_title.move_to([col_xs[1], title_y, 0])

        ge_title = Text("个位", font="PingFang SC",
                        font_size=28, color=self.COLOR_ONE)
        ge_title.move_to([col_xs[2], title_y, 0])

        self.play(
            Write(bai_title),
            Write(shi_title),
            Write(ge_title),
            run_time=0.5
        )

        # 数字行的y坐标
        digit_y = table_center_y - 0.38

        # ---- 填入数字 23 ----
        hint_23 = Text(
            "把 23 填入表格",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_SUBTITLE
        )
        hint_23.move_to(UP * 2.8)
        self.play(FadeIn(hint_23), run_time=0.3)

        digit_shi = Text("2", font="PingFang SC",
                         font_size=48, color=self.COLOR_TEN, weight=BOLD)
        digit_shi.move_to([col_xs[1], digit_y, 0])

        digit_ge = Text("3", font="PingFang SC",
                        font_size=48, color=self.COLOR_ONE, weight=BOLD)
        digit_ge.move_to([col_xs[2], digit_y, 0])

        self.play(
            GrowFromCenter(digit_shi),
            GrowFromCenter(digit_ge),
            run_time=0.7
        )
        self.wait(0.4)

        # 说明
        explain_shi = VGroup(
            Text("十位上的", font="PingFang SC",
                 font_size=24, color=self.COLOR_SUBTITLE),
            Text("2", font="PingFang SC",
                 font_size=28, color=self.COLOR_TEN, weight=BOLD),
            Text("= 2个十 = 20",
                 font="PingFang SC",
                 font_size=24, color=self.COLOR_TEN),
        ).arrange(RIGHT, buff=0.1)
        explain_shi.move_to(UP * 1.9)

        explain_ge = VGroup(
            Text("个位上的", font="PingFang SC",
                 font_size=24, color=self.COLOR_SUBTITLE),
            Text("3", font="PingFang SC",
                 font_size=28, color=self.COLOR_ONE, weight=BOLD),
            Text("= 3个一 = 3",
                 font="PingFang SC",
                 font_size=24, color=self.COLOR_ONE),
        ).arrange(RIGHT, buff=0.1)
        explain_ge.move_to(UP * 1.1)

        # 箭头
        arrow_shi = Arrow(
            start=digit_shi.get_bottom(),
            end=explain_shi.get_top(),
            color=self.COLOR_TEN,
            buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )
        arrow_ge = Arrow(
            start=digit_ge.get_bottom(),
            end=explain_ge.get_top(),
            color=self.COLOR_ONE,
            buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )

        self.play(GrowArrow(arrow_shi), GrowArrow(arrow_ge), run_time=0.5)
        self.play(
            FadeIn(explain_shi, shift=UP * 0.1),
            FadeIn(explain_ge, shift=UP * 0.1),
            run_time=0.6
        )
        self.wait(1.8)

        # 清除数字 → 换成 32
        self.play(
            FadeOut(hint_23),
            FadeOut(digit_shi),
            FadeOut(digit_ge),
            FadeOut(arrow_shi),
            FadeOut(arrow_ge),
            FadeOut(explain_shi),
            FadeOut(explain_ge),
            run_time=0.5
        )

        # ---- 填入数字 32 ----
        hint_32 = Text(
            "把 32 填入表格",
            font="PingFang SC",
            font_size=26,
            color=self.COLOR_SUBTITLE
        )
        hint_32.move_to(UP * 2.8)
        self.play(FadeIn(hint_32), run_time=0.3)

        digit_shi_32 = Text("3", font="PingFang SC",
                            font_size=48, color=self.COLOR_TEN, weight=BOLD)
        digit_shi_32.move_to([col_xs[1], digit_y, 0])

        digit_ge_32 = Text("2", font="PingFang SC",
                           font_size=48, color=self.COLOR_ONE, weight=BOLD)
        digit_ge_32.move_to([col_xs[2], digit_y, 0])

        self.play(
            GrowFromCenter(digit_shi_32),
            GrowFromCenter(digit_ge_32),
            run_time=0.7
        )
        self.wait(0.3)

        explain_shi2 = VGroup(
            Text("十位上的", font="PingFang SC",
                 font_size=24, color=self.COLOR_SUBTITLE),
            Text("3", font="PingFang SC",
                 font_size=28, color=self.COLOR_TEN, weight=BOLD),
            Text("= 3个十 = 30",
                 font="PingFang SC",
                 font_size=24, color=self.COLOR_TEN),
        ).arrange(RIGHT, buff=0.1)
        explain_shi2.move_to(UP * 1.9)

        explain_ge2 = VGroup(
            Text("个位上的", font="PingFang SC",
                 font_size=24, color=self.COLOR_SUBTITLE),
            Text("2", font="PingFang SC",
                 font_size=28, color=self.COLOR_ONE, weight=BOLD),
            Text("= 2个一 = 2",
                 font="PingFang SC",
                 font_size=24, color=self.COLOR_ONE),
        ).arrange(RIGHT, buff=0.1)
        explain_ge2.move_to(UP * 1.1)

        arrow_shi2 = Arrow(
            start=digit_shi_32.get_bottom(),
            end=explain_shi2.get_top(),
            color=self.COLOR_TEN,
            buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )
        arrow_ge2 = Arrow(
            start=digit_ge_32.get_bottom(),
            end=explain_ge2.get_top(),
            color=self.COLOR_ONE,
            buff=0.1,
            max_tip_length_to_length_ratio=0.2
        )

        self.play(GrowArrow(arrow_shi2), GrowArrow(arrow_ge2), run_time=0.5)
        self.play(
            FadeIn(explain_shi2, shift=UP * 0.1),
            FadeIn(explain_ge2, shift=UP * 0.1),
            run_time=0.6
        )
        self.wait(1.8)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(table_bg),
            FadeOut(h_divider),
            FadeOut(v_div1),
            FadeOut(v_div2),
            FadeOut(bai_title),
            FadeOut(shi_title),
            FadeOut(ge_title),
            FadeOut(hint_32),
            FadeOut(digit_shi_32),
            FadeOut(digit_ge_32),
            FadeOut(arrow_shi2),
            FadeOut(arrow_ge2),
            FadeOut(explain_shi2),
            FadeOut(explain_ge2),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────────────────────────
    # Scene 5: 位值深化 - 同一数字不同位置值不同
    # ─────────────────────────────────────────────────────────────────────

    def scene_5_place_value_insight(self):
        scene_title = Text(
            "位值的秘密",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_TITLE
        )
        scene_title.move_to(UP * 5.8)
        self.play(FadeIn(scene_title), run_time=0.4)

        # 核心问题
        question = VGroup(
            Text("数字", font="PingFang SC",
                 font_size=30, color=self.COLOR_SUBTITLE),
            Text("2", font="PingFang SC",
                 font_size=44, color=self.COLOR_HIGHLIGHT, weight=BOLD),
            Text("在不同位置，代表不同的数！",
                 font="PingFang SC",
                 font_size=30, color=self.COLOR_SUBTITLE),
        ).arrange(RIGHT, buff=0.15)
        question.move_to(UP * 4.8)
        self.play(FadeIn(question), run_time=0.5)

        # ---- 左卡片：23中的2 ----
        card_left_bg = RoundedRectangle(
            corner_radius=0.25,
            width=3.4,
            height=4.2,
            fill_color=self.COLOR_BG_CARD,
            fill_opacity=0.95,
            stroke_color=self.COLOR_TEN,
            stroke_width=2.5
        ).move_to([-2.0, 2.0, 0])

        card_left_title = Text(
            "数字 23 中的 2",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        ).move_to([-2.0, 3.75, 0])

        # 突出的 "2" 和灰色的 "3"
        num23_2 = Text("2", font="PingFang SC",
                       font_size=80, color=self.COLOR_TEN, weight=BOLD)
        num23_2.move_to([-2.35, 3.1, 0])
        num23_3 = Text("3", font="PingFang SC",
                       font_size=80, color="#3a3a4a")
        num23_3.move_to([-1.6, 3.1, 0])

        card_left_pos = Text(
            "2 在 十位",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_TEN,
            weight=BOLD
        ).move_to([-2.0, 2.2, 0])

        card_left_eq = Text(
            "= 2个十",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_TEN
        ).move_to([-2.0, 1.7, 0])

        card_left_val = Text(
            "= 20",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_TEN,
            weight=BOLD
        ).move_to([-2.0, 1.1, 0])

        # 迷你十块（2个）
        mini_tens = VGroup()
        for i in range(2):
            blk = self.make_ten_block(
                np.array([-2.5 + i * 0.42, 0.35, 0])
            )
            mini_tens.add(blk)

        self.play(FadeIn(card_left_bg), run_time=0.3)
        self.play(
            FadeIn(card_left_title),
            FadeIn(num23_2),
            FadeIn(num23_3),
            run_time=0.5
        )
        self.play(
            FadeIn(card_left_pos),
            FadeIn(card_left_eq),
            FadeIn(card_left_val),
            FadeIn(mini_tens),
            run_time=0.6
        )

        # ---- 右卡片：32中的2 ----
        card_right_bg = RoundedRectangle(
            corner_radius=0.25,
            width=3.4,
            height=4.2,
            fill_color=self.COLOR_BG_CARD,
            fill_opacity=0.95,
            stroke_color=self.COLOR_ONE,
            stroke_width=2.5
        ).move_to([2.0, 2.0, 0])

        card_right_title = Text(
            "数字 32 中的 2",
            font="PingFang SC",
            font_size=20,
            color=WHITE
        ).move_to([2.0, 3.75, 0])

        num32_3 = Text("3", font="PingFang SC",
                       font_size=80, color="#3a3a4a")
        num32_3.move_to([1.55, 3.1, 0])
        num32_2 = Text("2", font="PingFang SC",
                       font_size=80, color=self.COLOR_ONE, weight=BOLD)
        num32_2.move_to([2.3, 3.1, 0])

        card_right_pos = Text(
            "2 在 个位",
            font="PingFang SC",
            font_size=24,
            color=self.COLOR_ONE,
            weight=BOLD
        ).move_to([2.0, 2.2, 0])

        card_right_eq = Text(
            "= 2个一",
            font="PingFang SC",
            font_size=22,
            color=self.COLOR_ONE
        ).move_to([2.0, 1.7, 0])

        card_right_val = Text(
            "= 2",
            font="PingFang SC",
            font_size=36,
            color=self.COLOR_ONE,
            weight=BOLD
        ).move_to([2.0, 1.1, 0])

        # 迷你一块（2个）
        mini_ones = VGroup()
        for i in range(2):
            blk = self.make_one_block(
                np.array([1.7 + i * 0.42, 0.35, 0])
            )
            blk.scale(1.2)
            mini_ones.add(blk)

        self.play(FadeIn(card_right_bg), run_time=0.3)
        self.play(
            FadeIn(card_right_title),
            FadeIn(num32_3),
            FadeIn(num32_2),
            run_time=0.5
        )
        self.play(
            FadeIn(card_right_pos),
            FadeIn(card_right_eq),
            FadeIn(card_right_val),
            FadeIn(mini_ones),
            run_time=0.6
        )
        self.wait(0.5)

        # VS 对比
        vs_text = Text(
            "VS",
            font="PingFang SC",
            font_size=40,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        )
        vs_text.move_to([0.0, 2.0, 0])
        self.play(GrowFromCenter(vs_text), run_time=0.4)

        # 大小对比
        comparison = VGroup(
            Text("20", font="PingFang SC",
                 font_size=44, color=self.COLOR_TEN, weight=BOLD),
            Text("≠", font="PingFang SC",
                 font_size=38, color=WHITE),
            Text("2", font="PingFang SC",
                 font_size=44, color=self.COLOR_ONE, weight=BOLD),
        ).arrange(RIGHT, buff=0.2)
        comparison.move_to(DOWN * 0.5)
        self.play(FadeIn(comparison, shift=UP * 0.2), run_time=0.6)

        # 结论框
        conclusion_bg = RoundedRectangle(
            corner_radius=0.2,
            width=7.5,
            height=1.2,
            fill_color=self.COLOR_BG_CARD,
            fill_opacity=0.95,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(DOWN * 1.9)

        conclusion_txt = VGroup(
            Text("同样是", font="PingFang SC",
                 font_size=26, color=self.COLOR_SUBTITLE),
            Text("2", font="PingFang SC",
                 font_size=32, color=self.COLOR_HIGHLIGHT, weight=BOLD),
            Text("，位置不同，值相差 10 倍！",
                 font="PingFang SC",
                 font_size=26, color=self.COLOR_SUBTITLE),
        ).arrange(RIGHT, buff=0.1)
        conclusion_txt.move_to(DOWN * 1.9)

        self.play(FadeIn(conclusion_bg), run_time=0.3)
        self.play(FadeIn(conclusion_txt, shift=UP * 0.1), run_time=0.6)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(question),
            FadeOut(card_left_bg),
            FadeOut(card_left_title),
            FadeOut(num23_2),
            FadeOut(num23_3),
            FadeOut(card_left_pos),
            FadeOut(card_left_eq),
            FadeOut(card_left_val),
            FadeOut(mini_tens),
            FadeOut(card_right_bg),
            FadeOut(card_right_title),
            FadeOut(num32_3),
            FadeOut(num32_2),
            FadeOut(card_right_pos),
            FadeOut(card_right_eq),
            FadeOut(card_right_val),
            FadeOut(mini_ones),
            FadeOut(vs_text),
            FadeOut(comparison),
            FadeOut(conclusion_bg),
            FadeOut(conclusion_txt),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────────────────────────
    # Scene 6: 总结
    # ─────────────────────────────────────────────────────────────────────

    def scene_6_summary(self):
        scene_title = Text(
            "今天学了什么？",
            font="PingFang SC",
            font_size=38,
            color=self.COLOR_TITLE
        )
        scene_title.move_to(UP * 5.8)
        self.play(FadeIn(scene_title), run_time=0.4)

        # 要点卡片数据
        points_data = [
            (
                "①",
                "几个十和几个一",
                "23 = 2个十 + 3个一",
                self.COLOR_TEN,
                UP * 4.3
            ),
            (
                "②",
                "认识数位",
                "百位  十位  个位",
                self.COLOR_ONE,
                UP * 2.9
            ),
            (
                "③",
                "位值不同，大小不同",
                "十位的2=20，个位的2=2",
                self.COLOR_HIGHLIGHT,
                UP * 1.5
            ),
        ]

        all_cards = VGroup()
        for num_str, title_str, desc_str, clr, pos in points_data:
            card_bg = RoundedRectangle(
                corner_radius=0.2,
                width=7.5,
                height=1.1,
                fill_color=self.COLOR_BG_CARD,
                fill_opacity=0.95,
                stroke_color=clr,
                stroke_width=2
            ).move_to(pos)

            num_t = Text(num_str, font="PingFang SC",
                         font_size=28, color=clr, weight=BOLD)
            num_t.move_to(pos + LEFT * 3.2)

            title_t = Text(title_str, font="PingFang SC",
                           font_size=24, color=WHITE)
            title_t.move_to(pos + UP * 0.18 + LEFT * 0.5)

            desc_t = Text(desc_str, font="PingFang SC",
                          font_size=18, color="#999999")
            desc_t.move_to(pos + DOWN * 0.2 + LEFT * 0.5)

            card_group = VGroup(card_bg, num_t, title_t, desc_t)
            all_cards.add(card_group)

        for card in all_cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.3)

        # ---- 练习题 ----
        practice_bg = RoundedRectangle(
            corner_radius=0.2,
            width=7.5,
            height=2.6,
            fill_color="#0a0a1a",
            fill_opacity=0.95,
            stroke_color=self.COLOR_HIGHLIGHT,
            stroke_width=2
        ).move_to(DOWN * 1.5)

        practice_title = Text(
            "小练习",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        ).move_to(DOWN * 0.6)

        practice_q1 = VGroup(
            Text("45 = ", font="PingFang SC",
                 font_size=26, color=WHITE),
            Text("(  )", font="PingFang SC",
                 font_size=26, color=self.COLOR_TEN),
            Text("个十 + ", font="PingFang SC",
                 font_size=26, color=WHITE),
            Text("(  )", font="PingFang SC",
                 font_size=26, color=self.COLOR_ONE),
            Text("个一", font="PingFang SC",
                 font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.08)
        practice_q1.move_to(DOWN * 1.4)

        practice_q2 = VGroup(
            Text("7个十 + 8个一 =", font="PingFang SC",
                 font_size=26, color=WHITE),
            Text("(    )", font="PingFang SC",
                 font_size=26, color=self.COLOR_HIGHLIGHT),
        ).arrange(RIGHT, buff=0.15)
        practice_q2.move_to(DOWN * 2.2)

        self.play(
            FadeIn(practice_bg),
            FadeIn(practice_title),
            FadeIn(practice_q1),
            FadeIn(practice_q2),
            run_time=0.7
        )
        self.wait(1.0)

        # 答案揭示
        ans1_new = VGroup(
            Text("45 = ", font="PingFang SC",
                 font_size=26, color=WHITE),
            Text("4", font="PingFang SC",
                 font_size=30, color=self.COLOR_TEN, weight=BOLD),
            Text("个十 + ", font="PingFang SC",
                 font_size=26, color=WHITE),
            Text("5", font="PingFang SC",
                 font_size=30, color=self.COLOR_ONE, weight=BOLD),
            Text("个一", font="PingFang SC",
                 font_size=26, color=WHITE),
        ).arrange(RIGHT, buff=0.08)
        ans1_new.move_to(DOWN * 1.4)

        ans2_new = VGroup(
            Text("7个十 + 8个一 =", font="PingFang SC",
                 font_size=26, color=WHITE),
            Text("78", font="PingFang SC",
                 font_size=34, color=self.COLOR_HIGHLIGHT, weight=BOLD),
        ).arrange(RIGHT, buff=0.15)
        ans2_new.move_to(DOWN * 2.2)

        self.play(
            ReplacementTransform(practice_q1, ans1_new),
            run_time=0.6
        )
        self.wait(0.3)
        self.play(
            ReplacementTransform(practice_q2, ans2_new),
            run_time=0.6
        )
        self.wait(2.0)

        # 清理
        self.play(
            FadeOut(scene_title),
            FadeOut(all_cards),
            FadeOut(practice_bg),
            FadeOut(practice_title),
            FadeOut(ans1_new),
            FadeOut(ans2_new),
            run_time=0.6
        )

    # ─────────────────────────────────────────────────────────────────────
    # Scene 7: 片尾
    # ─────────────────────────────────────────────────────────────────────

    def scene_7_outro(self):
        # 作者名放大
        author_big = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        )
        author_big.move_to(UP * 2.5)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=28,
            color=self.COLOR_SUBTITLE
        )
        author_id.move_to(UP * 1.6)

        self.play(
            Transform(self.author_info, author_big),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        # 关注引导
        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT,
            weight=BOLD
        )
        follow_text.move_to(UP * 0.4)
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.05), run_time=0.6)

        # 知识点回顾
        recap_lines = [
            ("23 = 2个十 + 3个一", self.COLOR_TEN, DOWN * 0.8),
            ("32 = 3个十 + 2个一", "#e67e22", DOWN * 1.5),
            ("位置决定值的大小！", self.COLOR_HIGHLIGHT, DOWN * 2.3),
        ]
        recap_group = VGroup()
        for txt, clr, pos in recap_lines:
            t = Text(txt, font="PingFang SC",
                     font_size=24, color=clr)
            t.move_to(pos)
            recap_group.add(t)

        self.play(FadeIn(recap_group), run_time=0.6)

        # 数位标签装饰
        badge_data = [
            ("百位", WHITE, -2.3),
            ("十位", self.COLOR_TEN, 0.0),
            ("个位", self.COLOR_ONE, 2.3),
        ]
        deco = VGroup()
        for label_str, clr, x_pos in badge_data:
            badge_bg = RoundedRectangle(
                corner_radius=0.15,
                width=1.6,
                height=0.6,
                fill_color=self.COLOR_BG_CARD,
                fill_opacity=0.9,
                stroke_color=clr,
                stroke_width=2
            )
            badge_txt = Text(label_str, font="PingFang SC",
                             font_size=22, color=clr)
            badge = VGroup(badge_bg, badge_txt)
            badge.move_to([x_pos, -3.2, 0])
            deco.add(badge)

        self.play(FadeIn(deco), run_time=0.5)
        self.wait(2.5)

        # 全部淡出
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(recap_group),
            FadeOut(deco),
            run_time=1.0
        )
        self.wait(0.5)
