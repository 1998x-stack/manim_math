"""
004_常见的数量关系.py — 常见的数量关系 教学动画

知识点: 两个核心数量关系
  - 单价 × 数量 = 总价
  - 速度 × 时间 = 路程 (s = vt)
  - 逆向求解: 已知总价和单价求数量，已知路程和速度求时间

年级: 四年级第一学期 第三章
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
COLOR_TITLE   = "#fbbf24"   # 金黄色 — 标题
COLOR_PRICE   = "#3b82f6"   # 蓝色   — 单价/总价关系
COLOR_SPEED   = "#22c55e"   # 绿色   — 速度/路程关系
COLOR_REVERSE = "#f59e0b"   # 橙色   — 逆向运算高亮
COLOR_RESULT  = "#a78bfa"   # 紫色   — 最终结果
COLOR_AUTHOR  = "#6b7280"   # 灰色   — 作者信息
COLOR_BG_CARD = "#16213e"   # 深蓝   — 卡片背景
COLOR_ACCENT  = "#ef4444"   # 红色   — 强调
FONT = "Noto Sans CJK SC"


# ======================================================================
# 主场景
# ======================================================================

class QuantityRelationLesson(Scene):
    """
    常见的数量关系教学动画
    场景顺序:
      1. 开场钩子
      2. 单价 × 数量 = 总价
      3. 总价例题演示
      4. 逆向求解 (总价求数量)
      5. 速度 × 时间 = 路程
      6. 路程例题演示
      7. 逆向求解 (路程求时间)
      8. 总结双公式
      9. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者标识（全程保留在顶部）
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_AUTHOR
        ).move_to(UP * 7.0)
        self.add(self.author_label)

        self.scene_1_opening()
        self.scene_2_price_formula()
        self.scene_3_price_example()
        self.scene_4_price_reverse()
        self.scene_5_speed_formula()
        self.scene_6_speed_example()
        self.scene_7_speed_reverse()
        self.scene_8_summary()
        self.scene_9_outro()

    # ------------------------------------------------------------------
    # 场景 1 — 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        """开场: 抛出生活问题，引起兴趣"""

        hook_line1 = Text("买东西怎么算总价？", font=FONT, font_size=34, color=WHITE)
        hook_line2 = Text("行驶多远怎么知道？", font=FONT, font_size=34, color=COLOR_TITLE)
        hook = VGroup(hook_line1, hook_line2).arrange(DOWN, buff=0.2)
        hook.move_to(UP * 5.5)

        self.play(FadeIn(hook, shift=DOWN * 0.3), run_time=0.7)
        self.wait(0.3)

        # 展示两个生活场景图标
        # 购物场景
        shop_icon_bg = RoundedRectangle(
            width=3.6, height=2.2,
            corner_radius=0.3,
            fill_color=COLOR_BG_CARD, fill_opacity=1,
            stroke_color=COLOR_PRICE, stroke_width=2
        ).move_to(UP * 3.2 + LEFT * 2.1)

        shop_symbol = Text("🛒", font_size=52).move_to(shop_icon_bg.get_center() + UP * 0.35)
        shop_label = Text("购物场景", font=FONT, font_size=22, color=COLOR_PRICE)
        shop_label.move_to(shop_icon_bg.get_center() + DOWN * 0.55)

        # 行驶场景
        drive_icon_bg = RoundedRectangle(
            width=3.6, height=2.2,
            corner_radius=0.3,
            fill_color=COLOR_BG_CARD, fill_opacity=1,
            stroke_color=COLOR_SPEED, stroke_width=2
        ).move_to(UP * 3.2 + RIGHT * 2.1)

        drive_symbol = Text("🚗", font_size=52).move_to(drive_icon_bg.get_center() + UP * 0.35)
        drive_label = Text("行驶场景", font=FONT, font_size=22, color=COLOR_SPEED)
        drive_label.move_to(drive_icon_bg.get_center() + DOWN * 0.55)

        self.play(
            FadeIn(shop_icon_bg), FadeIn(shop_symbol), FadeIn(shop_label),
            FadeIn(drive_icon_bg), FadeIn(drive_symbol), FadeIn(drive_label),
            run_time=0.8
        )
        self.wait(0.5)

        # 今天学习提示
        hint_bg = RoundedRectangle(
            width=7.5, height=1.2,
            corner_radius=0.25,
            fill_color=COLOR_BG_CARD, fill_opacity=0.9,
            stroke_color=COLOR_TITLE, stroke_width=2
        ).move_to(UP * 1.5)

        hint = Text(
            "今天学习两个数量关系公式！",
            font=FONT, font_size=28, color=COLOR_TITLE
        ).move_to(hint_bg.get_center())

        self.play(FadeIn(hint_bg), FadeIn(hint, shift=UP * 0.2), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(hook), FadeOut(shop_icon_bg), FadeOut(shop_symbol),
            FadeOut(shop_label), FadeOut(drive_icon_bg), FadeOut(drive_symbol),
            FadeOut(drive_label), FadeOut(hint_bg), FadeOut(hint),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 2 — 单价 × 数量 = 总价
    # ------------------------------------------------------------------

    def scene_2_price_formula(self):
        """展示单价 × 数量 = 总价公式及含义"""

        section_title = Text(
            "公式一：单价 × 数量 = 总价",
            font=FONT, font_size=32, color=COLOR_PRICE
        ).move_to(UP * 6.3)
        self.play(Write(section_title), run_time=0.8)

        # 生活情境图示：苹果
        # 用矩形模拟苹果价格标签
        apple_bg = RoundedRectangle(
            width=5.5, height=1.8,
            corner_radius=0.3,
            fill_color="#0f2027", fill_opacity=1,
            stroke_color=COLOR_PRICE, stroke_width=2
        ).move_to(UP * 4.8)

        apple_text1 = Text("苹果", font=FONT, font_size=28, color=WHITE)
        apple_price  = Text("每个 3 元", font=FONT, font_size=26, color=COLOR_PRICE)
        apple_row = VGroup(apple_text1, apple_price).arrange(RIGHT, buff=0.5)
        apple_row.move_to(apple_bg.get_center())

        self.play(FadeIn(apple_bg), FadeIn(apple_row), run_time=0.6)

        # 用方块图示表示数量
        qty_label = Text("买了 5 个", font=FONT, font_size=26, color=WHITE).move_to(UP * 3.5)
        self.play(FadeIn(qty_label), run_time=0.4)

        # 5 个苹果图标
        apples = VGroup()
        for i in range(5):
            apple_box = RoundedRectangle(
                width=0.9, height=0.9,
                corner_radius=0.15,
                fill_color="#ef4444", fill_opacity=0.85,
                stroke_color="#dc2626", stroke_width=1.5
            )
            apple_box.move_to(UP * 2.7 + LEFT * 1.8 + RIGHT * i * 1.1)
            apples.add(apple_box)

        self.play(LaggedStart(*[FadeIn(a, scale=0.5) for a in apples], lag_ratio=0.15), run_time=1.0)
        self.wait(0.4)

        # 显示计算过程
        calc_text = Text("单价 × 数量 = 总价", font=FONT, font_size=30, color=COLOR_PRICE)
        calc_text.move_to(UP * 1.6)
        self.play(Write(calc_text), run_time=0.7)

        # 不在MathTex中用中文，改用VGroup拼合
        calc_math = MathTex(r"3 \times 5 = 15", font_size=44, color=COLOR_PRICE)
        calc_unit = Text("（元）", font=FONT, font_size=34, color=COLOR_PRICE)
        calc_row = VGroup(calc_math, calc_unit).arrange(RIGHT, buff=0.15)
        calc_row.move_to(UP * 0.7)

        self.play(Write(calc_math), FadeIn(calc_unit), run_time=0.8)
        self.wait(0.5)

        # 公式框
        formula_bg = RoundedRectangle(
            width=7.6, height=1.3,
            corner_radius=0.3,
            fill_color="#0a192f", fill_opacity=1,
            stroke_color=COLOR_PRICE, stroke_width=2.5
        ).move_to(DOWN * 0.5)

        formula_label = Text("单价", font=FONT, font_size=32, color=COLOR_PRICE)
        formula_times = MathTex(r"\times", font_size=36, color=WHITE)
        formula_qty   = Text("数量", font=FONT, font_size=32, color=COLOR_PRICE)
        formula_eq    = MathTex(r"=", font_size=36, color=WHITE)
        formula_total = Text("总价", font=FONT, font_size=32, color=COLOR_ACCENT)
        formula_items = VGroup(
            formula_label, formula_times, formula_qty,
            formula_eq, formula_total
        ).arrange(RIGHT, buff=0.25)
        formula_items.move_to(formula_bg.get_center())

        self.play(FadeIn(formula_bg), run_time=0.3)
        self.play(Write(formula_items), run_time=0.8)
        self.wait(0.5)

        # 反向推导说明
        reverse_text1 = Text("总价 ÷ 单价 = 数量", font=FONT, font_size=24, color=COLOR_REVERSE)
        reverse_text2 = Text("总价 ÷ 数量 = 单价", font=FONT, font_size=24, color=COLOR_REVERSE)
        reverses = VGroup(reverse_text1, reverse_text2).arrange(DOWN, buff=0.2)
        reverses.move_to(DOWN * 1.9)

        self.play(FadeIn(reverses, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(section_title), FadeOut(apple_bg), FadeOut(apple_row),
            FadeOut(qty_label), FadeOut(apples),
            FadeOut(calc_text), FadeOut(calc_row),
            FadeOut(formula_bg), FadeOut(formula_items),
            FadeOut(reverses),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 3 — 总价例题演示
    # ------------------------------------------------------------------

    def scene_3_price_example(self):
        """例题1: 已知单价和数量求总价"""

        eg_title = Text("例题 1", font=FONT, font_size=32, color=COLOR_TITLE).move_to(UP * 6.5)
        self.play(Write(eg_title), run_time=0.5)

        # 题目背景卡片
        problem_bg = RoundedRectangle(
            width=7.8, height=2.8,
            corner_radius=0.3,
            fill_color=COLOR_BG_CARD, fill_opacity=1,
            stroke_color=COLOR_PRICE, stroke_width=2
        ).move_to(UP * 5.0)

        prob_line1 = Text("每本练习册 4 元，", font=FONT, font_size=26, color=WHITE)
        prob_line2 = Text("买了 12 本。", font=FONT, font_size=26, color=WHITE)
        prob_line3 = Text("一共花了多少钱？", font=FONT, font_size=26, color=COLOR_PRICE)
        problem_text = VGroup(prob_line1, prob_line2, prob_line3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problem_text.move_to(problem_bg.get_center())

        self.play(FadeIn(problem_bg), run_time=0.3)
        self.play(Write(problem_text), run_time=0.9)
        self.wait(0.6)

        # 列出已知信息
        known_title = Text("已知：", font=FONT, font_size=26, color=COLOR_TITLE).move_to(UP * 3.0 + LEFT * 2.8)
        known1 = Text("单价 = 4 元", font=FONT, font_size=24, color=COLOR_PRICE).move_to(UP * 2.4 + LEFT * 1.8)
        known2 = Text("数量 = 12 本", font=FONT, font_size=24, color=COLOR_PRICE).move_to(UP * 1.8 + LEFT * 1.7)
        unknown_title = Text("求：总价 = ？", font=FONT, font_size=26, color=COLOR_ACCENT).move_to(UP * 1.2 + LEFT * 1.8)

        self.play(
            FadeIn(known_title), FadeIn(known1), FadeIn(known2),
            FadeIn(unknown_title),
            run_time=0.7
        )
        self.wait(0.4)

        # 解题过程
        solve_label = Text("解：单价 × 数量 = 总价", font=FONT, font_size=26, color=WHITE).move_to(UP * 0.4)
        solve_math = MathTex(r"4 \times 12 = 48", font_size=46, color=COLOR_PRICE).move_to(DOWN * 0.5)

        self.play(FadeIn(solve_label), run_time=0.4)
        self.play(Write(solve_math), run_time=0.8)
        self.wait(0.4)

        # 结果框
        result_bg = RoundedRectangle(
            width=6.5, height=1.2,
            corner_radius=0.3,
            fill_color="#0a192f", fill_opacity=1,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(DOWN * 1.8)

        ans_text = Text("答：一共花了 48 元", font=FONT, font_size=28, color=COLOR_RESULT)
        ans_text.move_to(result_bg.get_center())

        self.play(FadeIn(result_bg), run_time=0.3)
        self.play(FadeIn(ans_text, shift=UP * 0.2), run_time=0.6)
        self.wait(1.8)

        self.play(
            FadeOut(eg_title), FadeOut(problem_bg), FadeOut(problem_text),
            FadeOut(known_title), FadeOut(known1), FadeOut(known2),
            FadeOut(unknown_title), FadeOut(solve_label), FadeOut(solve_math),
            FadeOut(result_bg), FadeOut(ans_text),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 4 — 逆向求解: 总价求数量
    # ------------------------------------------------------------------

    def scene_4_price_reverse(self):
        """例题2: 已知总价和单价，求数量（逆向）"""

        eg_title = Text("例题 2（逆向）", font=FONT, font_size=32, color=COLOR_TITLE).move_to(UP * 6.5)
        self.play(Write(eg_title), run_time=0.5)

        # 题目卡片
        problem_bg = RoundedRectangle(
            width=7.8, height=2.8,
            corner_radius=0.3,
            fill_color=COLOR_BG_CARD, fill_opacity=1,
            stroke_color=COLOR_REVERSE, stroke_width=2
        ).move_to(UP * 5.0)

        prob_line1 = Text("每支钢笔 6 元，", font=FONT, font_size=26, color=WHITE)
        prob_line2 = Text("一共花了 72 元。", font=FONT, font_size=26, color=WHITE)
        prob_line3 = Text("买了多少支钢笔？", font=FONT, font_size=26, color=COLOR_REVERSE)
        problem_text = VGroup(prob_line1, prob_line2, prob_line3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problem_text.move_to(problem_bg.get_center())

        self.play(FadeIn(problem_bg), run_time=0.3)
        self.play(Write(problem_text), run_time=0.9)
        self.wait(0.6)

        # 逆向思维框
        reverse_tip_bg = RoundedRectangle(
            width=7.4, height=1.0,
            corner_radius=0.2,
            fill_color="#1a0a2e", fill_opacity=1,
            stroke_color=COLOR_REVERSE, stroke_width=2
        ).move_to(UP * 3.0)
        reverse_tip = Text("逆向思维：总价 ÷ 单价 = 数量", font=FONT, font_size=24, color=COLOR_REVERSE)
        reverse_tip.move_to(reverse_tip_bg.get_center())
        self.play(FadeIn(reverse_tip_bg), FadeIn(reverse_tip), run_time=0.5)
        self.wait(0.4)

        # 已知信息
        known1 = Text("总价 = 72 元", font=FONT, font_size=24, color=WHITE).move_to(UP * 2.1 + LEFT * 1.5)
        known2 = Text("单价 = 6 元", font=FONT, font_size=24, color=WHITE).move_to(UP * 1.5 + LEFT * 1.6)
        self.play(FadeIn(known1), FadeIn(known2), run_time=0.5)

        solve_label = Text("解：总价 ÷ 单价 = 数量", font=FONT, font_size=26, color=WHITE).move_to(UP * 0.7)
        solve_math = MathTex(r"72 \div 6 = 12", font_size=46, color=COLOR_REVERSE).move_to(DOWN * 0.3)

        self.play(FadeIn(solve_label), run_time=0.4)
        self.play(Write(solve_math), run_time=0.8)
        self.wait(0.4)

        # 结果框
        result_bg = RoundedRectangle(
            width=6.5, height=1.2,
            corner_radius=0.3,
            fill_color="#0a192f", fill_opacity=1,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(DOWN * 1.6)
        ans_text = Text("答：买了 12 支钢笔", font=FONT, font_size=28, color=COLOR_RESULT)
        ans_text.move_to(result_bg.get_center())

        self.play(FadeIn(result_bg), run_time=0.3)
        self.play(FadeIn(ans_text, shift=UP * 0.2), run_time=0.6)
        self.wait(1.8)

        self.play(
            FadeOut(eg_title), FadeOut(problem_bg), FadeOut(problem_text),
            FadeOut(reverse_tip_bg), FadeOut(reverse_tip),
            FadeOut(known1), FadeOut(known2),
            FadeOut(solve_label), FadeOut(solve_math),
            FadeOut(result_bg), FadeOut(ans_text),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 5 — 速度 × 时间 = 路程
    # ------------------------------------------------------------------

    def scene_5_speed_formula(self):
        """展示速度 × 时间 = 路程公式"""

        section_title = Text(
            "公式二：速度 × 时间 = 路程",
            font=FONT, font_size=32, color=COLOR_SPEED
        ).move_to(UP * 6.3)
        self.play(Write(section_title), run_time=0.8)

        # 路线示意图
        road_bg = RoundedRectangle(
            width=7.6, height=1.4,
            corner_radius=0.25,
            fill_color="#0a2010", fill_opacity=1,
            stroke_color=COLOR_SPEED, stroke_width=2
        ).move_to(UP * 5.0)

        # 起点 → 箭头 → 终点
        start_label = Text("出发", font=FONT, font_size=22, color=WHITE)
        road_arrow  = Arrow(LEFT * 1.5, RIGHT * 1.5, color=COLOR_SPEED, stroke_width=4,
                            max_tip_length_to_length_ratio=0.15)
        end_label   = Text("到达", font=FONT, font_size=22, color=WHITE)
        road_row = VGroup(start_label, road_arrow, end_label).arrange(RIGHT, buff=0.3)
        road_row.move_to(road_bg.get_center())

        self.play(FadeIn(road_bg), FadeIn(road_row), run_time=0.6)
        self.wait(0.3)

        # 三要素说明
        elements_title = Text("三个关键量：", font=FONT, font_size=28, color=COLOR_TITLE).move_to(UP * 3.8)
        self.play(FadeIn(elements_title), run_time=0.4)

        # 速度
        v_icon = Circle(radius=0.35, fill_color=COLOR_SPEED, fill_opacity=1, stroke_width=0)
        v_sym  = Text("v", font=FONT, font_size=28, color=WHITE, weight=BOLD).move_to(v_icon.get_center())
        v_icon_group = VGroup(v_icon, v_sym)
        v_desc = Text("速度（每小时多远）", font=FONT, font_size=22, color=WHITE)
        v_row = VGroup(v_icon_group, v_desc).arrange(RIGHT, buff=0.3).move_to(UP * 2.9 + LEFT * 0.5)

        # 时间
        t_icon = Circle(radius=0.35, fill_color="#f59e0b", fill_opacity=1, stroke_width=0)
        t_sym  = Text("t", font=FONT, font_size=28, color=WHITE, weight=BOLD).move_to(t_icon.get_center())
        t_icon_group = VGroup(t_icon, t_sym)
        t_desc = Text("时间（走了多少小时）", font=FONT, font_size=22, color=WHITE)
        t_row = VGroup(t_icon_group, t_desc).arrange(RIGHT, buff=0.3).move_to(UP * 2.0 + LEFT * 0.4)

        # 路程
        s_icon = Circle(radius=0.35, fill_color=COLOR_ACCENT, fill_opacity=1, stroke_width=0)
        s_sym  = Text("s", font=FONT, font_size=28, color=WHITE, weight=BOLD).move_to(s_icon.get_center())
        s_icon_group = VGroup(s_icon, s_sym)
        s_desc = Text("路程（一共走了多远）", font=FONT, font_size=22, color=WHITE)
        s_row = VGroup(s_icon_group, s_desc).arrange(RIGHT, buff=0.3).move_to(UP * 1.1 + LEFT * 0.4)

        self.play(FadeIn(v_row, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(t_row, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(s_row, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)

        # 核心公式框
        formula_bg = RoundedRectangle(
            width=7.8, height=2.2,
            corner_radius=0.3,
            fill_color="#0a192f", fill_opacity=1,
            stroke_color=COLOR_SPEED, stroke_width=2.5
        ).move_to(DOWN * 0.8)

        formula_chinese_row = VGroup(
            Text("速度", font=FONT, font_size=30, color=COLOR_SPEED),
            MathTex(r"\times", font_size=34, color=WHITE),
            Text("时间", font=FONT, font_size=30, color=COLOR_SPEED),
            MathTex(r"=", font_size=34, color=WHITE),
            Text("路程", font=FONT, font_size=30, color=COLOR_ACCENT),
        ).arrange(RIGHT, buff=0.2)
        formula_chinese_row.move_to(formula_bg.get_center() + UP * 0.4)

        formula_letter_row = VGroup(
            MathTex(r"s = v \times t", font_size=40, color=COLOR_SPEED),
        )
        formula_letter_row.move_to(formula_bg.get_center() + DOWN * 0.4)

        self.play(FadeIn(formula_bg), run_time=0.3)
        self.play(Write(formula_chinese_row), run_time=0.8)
        self.play(Write(formula_letter_row), run_time=0.6)
        self.wait(0.5)

        # 逆向公式说明
        reverse_row = VGroup(
            Text("路程 ÷ 速度 = 时间", font=FONT, font_size=22, color=COLOR_REVERSE),
        ).move_to(DOWN * 2.2)
        self.play(FadeIn(reverse_row, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(section_title), FadeOut(road_bg), FadeOut(road_row),
            FadeOut(elements_title), FadeOut(v_row), FadeOut(t_row), FadeOut(s_row),
            FadeOut(formula_bg), FadeOut(formula_chinese_row), FadeOut(formula_letter_row),
            FadeOut(reverse_row),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 6 — 路程例题演示
    # ------------------------------------------------------------------

    def scene_6_speed_example(self):
        """例题3: 已知速度和时间求路程"""

        eg_title = Text("例题 3", font=FONT, font_size=32, color=COLOR_TITLE).move_to(UP * 6.5)
        self.play(Write(eg_title), run_time=0.5)

        # 题目卡片
        problem_bg = RoundedRectangle(
            width=7.8, height=2.8,
            corner_radius=0.3,
            fill_color=COLOR_BG_CARD, fill_opacity=1,
            stroke_color=COLOR_SPEED, stroke_width=2
        ).move_to(UP * 5.0)

        prob_line1 = Text("一辆汽车每小时行驶 120 千米，", font=FONT, font_size=24, color=WHITE)
        prob_line2 = Text("行驶了 3 小时。", font=FONT, font_size=24, color=WHITE)
        prob_line3 = Text("一共走了多少千米？", font=FONT, font_size=24, color=COLOR_SPEED)
        problem_text = VGroup(prob_line1, prob_line2, prob_line3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problem_text.move_to(problem_bg.get_center())

        self.play(FadeIn(problem_bg), run_time=0.3)
        self.play(Write(problem_text), run_time=0.9)
        self.wait(0.6)

        # 路线动画：车辆沿路行驶
        road_line = Line(LEFT * 3.2, RIGHT * 3.2, color=GRAY_C, stroke_width=3).move_to(UP * 3.2)
        car_dot = Dot(road_line.get_start(), color=COLOR_SPEED, radius=0.18)
        car_label = Text("出发", font=FONT, font_size=18, color=WHITE)
        car_label.next_to(car_dot, UP, buff=0.15)

        self.play(FadeIn(road_line), FadeIn(car_dot), FadeIn(car_label), run_time=0.4)

        # 三个时间段标记
        time_marks = VGroup()
        for i in range(4):
            mark = Line(UP * 0.15, DOWN * 0.15, color=GRAY_B, stroke_width=2)
            mark.move_to(road_line.get_start() + RIGHT * i * 2.13)
            time_label = Text(f"{i}h", font=FONT, font_size=16, color=GRAY_B)
            time_label.next_to(mark, DOWN, buff=0.1)
            time_marks.add(mark, time_label)
        self.play(FadeIn(time_marks), run_time=0.4)

        # 动车动画
        end_dot = Dot(road_line.get_end(), color=COLOR_ACCENT, radius=0.18)
        self.play(
            car_dot.animate.move_to(road_line.get_end()),
            car_label.animate.move_to(road_line.get_end() + UP * 0.33),
            run_time=1.2, rate_func=linear
        )
        self.play(
            car_label.animate.become(
                Text("到达", font=FONT, font_size=18, color=COLOR_SPEED).move_to(road_line.get_end() + UP * 0.33)
            ),
            run_time=0.3
        )
        self.wait(0.3)

        # 已知信息
        known1 = Text("速度 = 120 千米/时", font=FONT, font_size=24, color=WHITE).move_to(UP * 2.2 + LEFT * 1.0)
        known2 = Text("时间 = 3 小时", font=FONT, font_size=24, color=WHITE).move_to(UP * 1.6 + LEFT * 1.6)
        self.play(FadeIn(known1), FadeIn(known2), run_time=0.5)

        # 解题
        solve_label = Text("解：速度 × 时间 = 路程", font=FONT, font_size=26, color=WHITE).move_to(UP * 0.8)
        solve_math = MathTex(r"120 \times 3 = 360", font_size=44, color=COLOR_SPEED).move_to(UP * 0.0)

        self.play(FadeIn(solve_label), run_time=0.4)
        self.play(Write(solve_math), run_time=0.8)
        self.wait(0.4)

        # 结果框
        result_bg = RoundedRectangle(
            width=7.0, height=1.2,
            corner_radius=0.3,
            fill_color="#0a192f", fill_opacity=1,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(DOWN * 1.3)
        ans_text = Text("答：一共走了 360 千米", font=FONT, font_size=28, color=COLOR_RESULT)
        ans_text.move_to(result_bg.get_center())

        self.play(FadeIn(result_bg), run_time=0.3)
        self.play(FadeIn(ans_text, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(eg_title), FadeOut(problem_bg), FadeOut(problem_text),
            FadeOut(road_line), FadeOut(car_dot), FadeOut(car_label),
            FadeOut(time_marks),
            FadeOut(known1), FadeOut(known2),
            FadeOut(solve_label), FadeOut(solve_math),
            FadeOut(result_bg), FadeOut(ans_text),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 7 — 逆向求解: 路程求时间
    # ------------------------------------------------------------------

    def scene_7_speed_reverse(self):
        """例题4: 已知路程和速度，求时间（逆向）"""

        eg_title = Text("例题 4（逆向）", font=FONT, font_size=32, color=COLOR_TITLE).move_to(UP * 6.5)
        self.play(Write(eg_title), run_time=0.5)

        problem_bg = RoundedRectangle(
            width=7.8, height=2.8,
            corner_radius=0.3,
            fill_color=COLOR_BG_CARD, fill_opacity=1,
            stroke_color=COLOR_REVERSE, stroke_width=2
        ).move_to(UP * 5.0)

        prob_line1 = Text("从甲城到乙城，路程为 480 千米，", font=FONT, font_size=23, color=WHITE)
        prob_line2 = Text("列车速度为 160 千米/时。", font=FONT, font_size=23, color=WHITE)
        prob_line3 = Text("需要走几小时？", font=FONT, font_size=23, color=COLOR_REVERSE)
        problem_text = VGroup(prob_line1, prob_line2, prob_line3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problem_text.move_to(problem_bg.get_center())

        self.play(FadeIn(problem_bg), run_time=0.3)
        self.play(Write(problem_text), run_time=0.9)
        self.wait(0.6)

        # 逆向思维提示
        reverse_tip_bg = RoundedRectangle(
            width=7.4, height=1.0,
            corner_radius=0.2,
            fill_color="#1a0a2e", fill_opacity=1,
            stroke_color=COLOR_REVERSE, stroke_width=2
        ).move_to(UP * 3.0)
        reverse_tip = Text("逆向思维：路程 ÷ 速度 = 时间", font=FONT, font_size=24, color=COLOR_REVERSE)
        reverse_tip.move_to(reverse_tip_bg.get_center())
        self.play(FadeIn(reverse_tip_bg), FadeIn(reverse_tip), run_time=0.5)
        self.wait(0.4)

        # 已知信息
        known1 = Text("路程 = 480 千米", font=FONT, font_size=24, color=WHITE).move_to(UP * 2.1 + LEFT * 1.3)
        known2 = Text("速度 = 160 千米/时", font=FONT, font_size=24, color=WHITE).move_to(UP * 1.5 + LEFT * 1.2)
        self.play(FadeIn(known1), FadeIn(known2), run_time=0.5)

        solve_label = Text("解：路程 ÷ 速度 = 时间", font=FONT, font_size=26, color=WHITE).move_to(UP * 0.7)
        solve_math = MathTex(r"480 \div 160 = 3", font_size=44, color=COLOR_REVERSE).move_to(DOWN * 0.2)

        self.play(FadeIn(solve_label), run_time=0.4)
        self.play(Write(solve_math), run_time=0.8)
        self.wait(0.4)

        # 结果框
        result_bg = RoundedRectangle(
            width=6.5, height=1.2,
            corner_radius=0.3,
            fill_color="#0a192f", fill_opacity=1,
            stroke_color=COLOR_RESULT, stroke_width=2.5
        ).move_to(DOWN * 1.6)
        ans_text = Text("答：需要 3 小时", font=FONT, font_size=28, color=COLOR_RESULT)
        ans_text.move_to(result_bg.get_center())

        self.play(FadeIn(result_bg), run_time=0.3)
        self.play(FadeIn(ans_text, shift=UP * 0.2), run_time=0.6)
        self.wait(1.8)

        self.play(
            FadeOut(eg_title), FadeOut(problem_bg), FadeOut(problem_text),
            FadeOut(reverse_tip_bg), FadeOut(reverse_tip),
            FadeOut(known1), FadeOut(known2),
            FadeOut(solve_label), FadeOut(solve_math),
            FadeOut(result_bg), FadeOut(ans_text),
            run_time=0.5
        )

    # ------------------------------------------------------------------
    # 场景 8 — 总结双公式
    # ------------------------------------------------------------------

    def scene_8_summary(self):
        """总结两大数量关系"""

        sum_title = Text("公式总结", font=FONT, font_size=38, color=COLOR_TITLE)
        sum_title.move_to(UP * 6.4)
        self.play(Write(sum_title), run_time=0.6)

        # ---- 公式一卡片 ----
        card1_bg = RoundedRectangle(
            width=7.8, height=3.0,
            corner_radius=0.3,
            fill_color=COLOR_BG_CARD, fill_opacity=1,
            stroke_color=COLOR_PRICE, stroke_width=2.5
        ).move_to(UP * 4.4)

        c1_tag = Text("购物场景", font=FONT, font_size=22, color=COLOR_PRICE)
        c1_tag.move_to(card1_bg.get_top() + DOWN * 0.4 + LEFT * 2.5)

        c1_main = VGroup(
            Text("单价", font=FONT, font_size=30, color=COLOR_PRICE),
            MathTex(r"\times", font_size=34, color=WHITE),
            Text("数量", font=FONT, font_size=30, color=COLOR_PRICE),
            MathTex(r"=", font_size=34, color=WHITE),
            Text("总价", font=FONT, font_size=30, color=COLOR_ACCENT),
        ).arrange(RIGHT, buff=0.2)
        c1_main.move_to(card1_bg.get_center() + UP * 0.35)

        c1_reverse1 = Text("总价 ÷ 单价 = 数量", font=FONT, font_size=20, color=COLOR_REVERSE)
        c1_reverse2 = Text("总价 ÷ 数量 = 单价", font=FONT, font_size=20, color=COLOR_REVERSE)
        c1_reverses = VGroup(c1_reverse1, c1_reverse2).arrange(RIGHT, buff=0.5)
        c1_reverses.move_to(card1_bg.get_center() + DOWN * 0.65)

        card1 = VGroup(card1_bg, c1_tag, c1_main, c1_reverses)
        self.play(FadeIn(card1, shift=RIGHT * 0.4), run_time=0.6)
        self.wait(0.6)

        # ---- 公式二卡片 ----
        card2_bg = RoundedRectangle(
            width=7.8, height=3.0,
            corner_radius=0.3,
            fill_color=COLOR_BG_CARD, fill_opacity=1,
            stroke_color=COLOR_SPEED, stroke_width=2.5
        ).move_to(UP * 1.0)

        c2_tag = Text("行驶场景", font=FONT, font_size=22, color=COLOR_SPEED)
        c2_tag.move_to(card2_bg.get_top() + DOWN * 0.4 + LEFT * 2.5)

        c2_main = VGroup(
            Text("速度", font=FONT, font_size=30, color=COLOR_SPEED),
            MathTex(r"\times", font_size=34, color=WHITE),
            Text("时间", font=FONT, font_size=30, color=COLOR_SPEED),
            MathTex(r"=", font_size=34, color=WHITE),
            Text("路程", font=FONT, font_size=30, color=COLOR_ACCENT),
        ).arrange(RIGHT, buff=0.2)
        c2_main.move_to(card2_bg.get_center() + UP * 0.35)

        c2_letter = MathTex(r"s = v \times t", font_size=32, color=COLOR_SPEED)
        c2_letter.move_to(card2_bg.get_center() + DOWN * 0.15)

        c2_reverse = Text("路程 ÷ 速度 = 时间", font=FONT, font_size=20, color=COLOR_REVERSE)
        c2_reverse.move_to(card2_bg.get_center() + DOWN * 0.8)

        card2 = VGroup(card2_bg, c2_tag, c2_main, c2_letter, c2_reverse)
        self.play(FadeIn(card2, shift=RIGHT * 0.4), run_time=0.6)
        self.wait(0.6)

        # ---- 记忆口诀 ----
        rhyme_bg = RoundedRectangle(
            width=7.8, height=1.8,
            corner_radius=0.3,
            fill_color="#0a0a1e", fill_opacity=1,
            stroke_color=COLOR_TITLE, stroke_width=2.5
        ).move_to(DOWN * 2.0)

        rhyme_line1 = Text("单价乘数量得总价，", font=FONT, font_size=26, color=COLOR_TITLE)
        rhyme_line2 = Text("速度乘时间是路程！", font=FONT, font_size=26, color=COLOR_TITLE)
        rhyme = VGroup(rhyme_line1, rhyme_line2).arrange(DOWN, buff=0.2)
        rhyme.move_to(rhyme_bg.get_center())

        self.play(FadeIn(rhyme_bg), Write(rhyme), run_time=0.8)
        self.wait(2.5)

        self.play(
            FadeOut(sum_title), FadeOut(card1), FadeOut(card2),
            FadeOut(rhyme_bg), FadeOut(rhyme),
            run_time=0.6
        )

    # ------------------------------------------------------------------
    # 场景 9 — 片尾
    # ------------------------------------------------------------------

    def scene_9_outro(self):
        """片尾: 作者信息 + 关注提示"""

        channel = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=42, color=WHITE
        ).move_to(UP * 2.2)

        handle = Text(
            "@emptyandcalm",
            font=FONT, font_size=32, color=GRAY_B
        ).move_to(UP * 1.2)

        self.play(
            FadeOut(self.author_label),
            FadeIn(channel, shift=DOWN * 0.3),
            run_time=0.7
        )
        self.play(FadeIn(handle, shift=DOWN * 0.2), run_time=0.5)

        follow = Text(
            "关注我，获得更多数学技巧！",
            font=FONT, font_size=30, color=COLOR_TITLE
        ).move_to(UP * 0.0)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 装饰：两个公式符号飘动
        deco1 = VGroup(
            Text("单价", font=FONT, font_size=22, color=COLOR_PRICE),
            MathTex(r"\times", font_size=28, color=WHITE),
            Text("数量", font=FONT, font_size=22, color=COLOR_PRICE),
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 1.5 + LEFT * 1.5)

        deco2 = MathTex(r"s = vt", font_size=36, color=COLOR_SPEED).move_to(DOWN * 1.5 + RIGHT * 1.8)

        self.play(FadeIn(deco1, scale=0.5), FadeIn(deco2, scale=0.5), run_time=0.6)

        # 图标行
        icons = VGroup(
            Circle(radius=0.25, fill_color=COLOR_PRICE, fill_opacity=0.9, stroke_width=0),
            Circle(radius=0.25, fill_color=COLOR_SPEED, fill_opacity=0.9, stroke_width=0),
            Circle(radius=0.25, fill_color=COLOR_REVERSE, fill_opacity=0.9, stroke_width=0),
            Circle(radius=0.25, fill_color=COLOR_RESULT, fill_opacity=0.9, stroke_width=0),
        ).arrange(RIGHT, buff=0.4).move_to(DOWN * 2.8)

        self.play(*[FadeIn(ic, scale=0.5) for ic in icons], run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(channel), FadeOut(handle),
            FadeOut(follow), FadeOut(deco1), FadeOut(deco2),
            FadeOut(icons),
            run_time=0.8
        )
