"""
除法的引入 - Division Introduction Animation
二年级上册 第二章 乘法、除法（一）

内容:
  1. 等分除 - 把12个苹果平均分给3个小朋友，每人几个？
  2. 包含除 - 12个苹果每3个装一袋，能装几袋？
  3. 认识除号"÷"，理解算式 被除数 ÷ 除数 = 商

目标受众: 二年级小学生
格式: TikTok竖屏 1080×1920
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ── 全局配置 ──────────────────────────────────────────
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# ── 颜色常量 ──────────────────────────────────────────
C_BG        = "#1a1a2e"
C_TITLE     = "#f9ca24"
C_APPLE     = "#e74c3c"
C_APPLE_HL  = "#ff6b6b"
C_PLATE     = "#3498db"
C_BAG       = "#9b59b6"
C_FORMULA   = "#2ecc71"
C_ARROW     = "#f39c12"
C_HINT      = "#ecf0f1"
C_DIM       = "#7f8c8d"
C_DIV_SIGN  = "#e67e22"


class DivisionIntroLesson(Scene):
    """
    除法的引入教学动画

    场景顺序:
      1. 开场钩子
      2. 问题引入：12个苹果
      3. 等分除演示
      4. 认识除号与算式
      5. 包含除演示
      6. 总结对比
      7. 片尾
    """

    # ──────────────────────────────────────────────────
    def construct(self):
        self.camera.background_color = C_BG

        # 品牌标识（常驻顶部）
        self.author_label = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color=C_DIM,
        ).move_to(UP * 7.0)
        self.add(self.author_label)

        # 运行各场景
        self.scene_opening()
        self.scene_equal_division()
        self.scene_division_symbol()
        self.scene_containing_division()
        self.scene_summary()
        self.scene_outro()

    # ══════════════════════════════════════════════════
    # 辅助：创建一个苹果图标（红色圆 + 叶子）
    # ══════════════════════════════════════════════════
    def make_apple(self, color=C_APPLE, radius=0.22):
        body = Circle(radius=radius, color=color,
                      fill_color=color, fill_opacity=1, stroke_width=0)
        # 叶子：小椭圆
        leaf = Ellipse(width=radius * 0.6, height=radius * 0.4,
                       color="#27ae60", fill_color="#27ae60",
                       fill_opacity=1, stroke_width=0)
        leaf.move_to(body.get_top() + UP * radius * 0.25 + LEFT * radius * 0.15)
        leaf.rotate(PI / 6)
        return VGroup(body, leaf)

    def make_apple_group(self, n, color=C_APPLE, radius=0.22,
                         cols=6, h_buff=0.62, v_buff=0.65):
        """排列 n 个苹果，按 cols 列网格"""
        apples = VGroup()
        for i in range(n):
            row = i // cols
            col = i % cols
            apple = self.make_apple(color=color, radius=radius)
            apple.move_to(RIGHT * col * h_buff + DOWN * row * v_buff)
            apples.add(apple)
        return apples

    # ══════════════════════════════════════════════════
    # 场景 1：开场钩子
    # ══════════════════════════════════════════════════
    def scene_opening(self):
        # 大标题
        title = Text("除法的引入", font="PingFang SC",
                     font_size=52, color=C_TITLE)
        title.move_to(UP * 5.5)

        hook = Text("12个苹果，怎么分？", font="PingFang SC",
                    font_size=36, color=WHITE)
        hook.move_to(UP * 4.3)

        # 12个苹果整体展示
        apples = self.make_apple_group(12, cols=6, h_buff=0.65, v_buff=0.7)
        apples.move_to(UP * 2.3)

        question_mark = Text("?", font="PingFang SC",
                             font_size=80, color=C_TITLE)
        question_mark.move_to(DOWN * 0.2)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(hook, shift=UP * 0.2), run_time=0.5)
        self.play(LaggedStart(
            *[GrowFromCenter(a) for a in apples],
            lag_ratio=0.07
        ), run_time=1.5)
        self.play(FadeIn(question_mark, scale=0.5), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(hook),
            FadeOut(question_mark), FadeOut(apples),
            run_time=0.5,
        )

    # ══════════════════════════════════════════════════
    # 场景 2：等分除演示
    # ══════════════════════════════════════════════════
    def scene_equal_division(self):
        # ── 标题 ──
        sec_title = Text("等分除", font="PingFang SC",
                         font_size=44, color=C_TITLE)
        sec_title.move_to(UP * 6.5)

        desc = Text("把12个苹果平均分给3个小朋友", font="PingFang SC",
                    font_size=28, color=C_HINT)
        desc.move_to(UP * 5.5)

        question = Text("每人分几个？", font="PingFang SC",
                        font_size=32, color=C_APPLE_HL)
        question.move_to(UP * 4.7)

        self.play(Write(sec_title), run_time=0.6)
        self.play(FadeIn(desc), FadeIn(question, shift=UP * 0.15), run_time=0.6)
        self.wait(0.4)

        # ── 12 个苹果（初始整齐排列）──
        apples = self.make_apple_group(12, cols=6, h_buff=0.65, v_buff=0.7)
        apples.move_to(UP * 3.0)

        self.play(LaggedStart(
            *[GrowFromCenter(a) for a in apples],
            lag_ratio=0.06
        ), run_time=1.2)
        self.wait(0.5)

        # ── 3 个盘子（代表3个小朋友）──
        plate_centers = [
            LEFT * 2.8 + DOWN * 0.5,
            ORIGIN  + DOWN * 0.5,
            RIGHT * 2.8 + DOWN * 0.5,
        ]
        plate_colors = ["#3498db", "#e67e22", "#2ecc71"]
        plates = VGroup()
        plate_labels = VGroup()
        for idx, (center, col) in enumerate(zip(plate_centers, plate_colors)):
            plate = Ellipse(width=1.8, height=0.6,
                            color=col, fill_color=col,
                            fill_opacity=0.25, stroke_width=3)
            plate.move_to(center)
            plates.add(plate)
            lbl = Text(f"小朋友{idx+1}", font="PingFang SC",
                       font_size=20, color=col)
            lbl.next_to(plate, DOWN, buff=0.12)
            plate_labels.add(lbl)

        self.play(
            LaggedStart(*[Create(p) for p in plates], lag_ratio=0.2),
            run_time=0.8,
        )
        self.play(
            LaggedStart(*[FadeIn(lb) for lb in plate_labels], lag_ratio=0.2),
            run_time=0.5,
        )
        self.wait(0.3)

        # ── 逐轮分配：每轮每个盘子各得 1 个苹果，共 4 轮 ──
        apple_positions_per_plate = [[], [], []]  # 每盘最终苹果位置
        # 预先计算每个苹果落点（每盘4个，2列2行）
        sub_offsets = [
            LEFT * 0.35 + UP * 0.12,
            RIGHT * 0.35 + UP * 0.12,
            LEFT * 0.35 + DOWN * 0.12,
            RIGHT * 0.35 + DOWN * 0.12,
        ]
        for p_idx, center in enumerate(plate_centers):
            for o in sub_offsets:
                apple_positions_per_plate[p_idx].append(center + o)

        apple_idx = 0
        for round_i in range(4):          # 4轮
            anims = []
            for plate_i in range(3):      # 3个盘子
                a = apples[apple_idx]
                target_pos = apple_positions_per_plate[plate_i][round_i]
                anims.append(a.animate.move_to(target_pos).scale(0.85))
                apple_idx += 1
            self.play(*anims, run_time=0.6)
            self.wait(0.15)

        # ── 标注每盘4个 ──
        count_labels = VGroup()
        for p_idx, center in enumerate(plate_centers):
            lbl = Text("4个", font="PingFang SC",
                       font_size=26, color=C_TITLE)
            lbl.move_to(center + UP * 0.5)
            count_labels.add(lbl)

        self.play(
            LaggedStart(*[FadeIn(lb, scale=1.2) for lb in count_labels],
                        lag_ratio=0.2),
            run_time=0.7,
        )
        self.wait(1.0)

        # ── 结论 ──
        conclusion = Text("每人分到 4 个！", font="PingFang SC",
                          font_size=34, color=C_FORMULA)
        conclusion.move_to(DOWN * 2.2)
        self.play(Write(conclusion), run_time=0.7)
        self.wait(1.2)

        # 淡出当前场景元素
        self.play(
            FadeOut(sec_title), FadeOut(desc), FadeOut(question),
            FadeOut(apples), FadeOut(plates), FadeOut(plate_labels),
            FadeOut(count_labels), FadeOut(conclusion),
            run_time=0.6,
        )

    # ══════════════════════════════════════════════════
    # 场景 3：认识除号与算式结构
    # ══════════════════════════════════════════════════
    def scene_division_symbol(self):
        # ── 标题 ──
        sec_title = Text("认识除号  ÷", font="PingFang SC",
                         font_size=44, color=C_TITLE)
        sec_title.move_to(UP * 6.5)
        self.play(Write(sec_title), run_time=0.6)

        # ── 除号放大展示 ──
        div_big = Text("÷", font="PingFang SC",
                       font_size=140, color=C_DIV_SIGN)
        div_big.move_to(UP * 4.0)
        self.play(GrowFromCenter(div_big), run_time=0.8)

        read_hint = Text("读作：除以", font="PingFang SC",
                         font_size=30, color=C_HINT)
        read_hint.next_to(div_big, DOWN, buff=0.3)
        self.play(FadeIn(read_hint), run_time=0.5)
        self.wait(0.8)

        # ── 算式结构图解 ──
        #   被除数  ÷  除数  =  商
        parts = VGroup(
            Text("被除数", font="PingFang SC", font_size=28, color=C_APPLE_HL),
            Text("÷",     font="PingFang SC", font_size=36, color=C_DIV_SIGN),
            Text("除数",   font="PingFang SC", font_size=28, color=C_PLATE),
            Text("=",     font="PingFang SC", font_size=36, color=WHITE),
            Text("商",    font="PingFang SC", font_size=28, color=C_FORMULA),
        )
        parts.arrange(RIGHT, buff=0.35)
        parts.move_to(UP * 2.0)
        self.play(
            FadeOut(div_big), FadeOut(read_hint),
            run_time=0.4,
        )
        self.play(
            LaggedStart(*[Write(p) for p in parts], lag_ratio=0.25),
            run_time=1.2,
        )
        self.wait(0.5)

        # ── 对应到具体算式 12 ÷ 3 = 4 ──
        formula_row = VGroup(
            Text("12", font="PingFang SC", font_size=48, color=C_APPLE_HL),
            Text("÷",  font="PingFang SC", font_size=48, color=C_DIV_SIGN),
            Text("3",  font="PingFang SC", font_size=48, color=C_PLATE),
            Text("=",  font="PingFang SC", font_size=48, color=WHITE),
            Text("4",  font="PingFang SC", font_size=48, color=C_FORMULA),
        )
        formula_row.arrange(RIGHT, buff=0.45)
        formula_row.move_to(UP * 0.5)

        # 对应箭头
        arrows = VGroup()
        for i, (part, fpart) in enumerate(zip(parts, formula_row)):
            arr = Arrow(
                start=part.get_bottom() + DOWN * 0.05,
                end=fpart.get_top() + UP * 0.05,
                buff=0.08,
                color=C_ARROW,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.3,
            )
            arrows.add(arr)

        self.play(
            LaggedStart(*[GrowArrow(arr) for arr in arrows], lag_ratio=0.15),
            run_time=0.8,
        )
        self.play(
            LaggedStart(*[Write(p) for p in formula_row], lag_ratio=0.2),
            run_time=1.0,
        )
        self.wait(1.5)

        # 高亮每个部分
        boxes = VGroup()
        colors = [C_APPLE_HL, C_DIV_SIGN, C_PLATE, WHITE, C_FORMULA]
        labels = ["被除数", "除以", "除数", "等于", "商（结果）"]
        for fpart, col, lbl_text in zip(formula_row, colors, labels):
            box = SurroundingRectangle(fpart, color=col, buff=0.1, stroke_width=2)
            boxes.add(box)

        for box, fpart, col, lbl_text in zip(boxes, formula_row, colors, labels):
            lbl = Text(lbl_text, font="PingFang SC",
                       font_size=20, color=col)
            lbl.next_to(fpart, DOWN, buff=1.0)
            self.play(Create(box), FadeIn(lbl), run_time=0.4)
            self.wait(0.3)
            self.play(FadeOut(box), FadeOut(lbl), run_time=0.2)

        self.wait(0.8)

        # 保留算式，清除其余
        self.play(
            FadeOut(sec_title), FadeOut(parts), FadeOut(arrows),
            run_time=0.5,
        )
        # 把算式移上去
        self.play(formula_row.animate.move_to(UP * 5.8), run_time=0.6)
        self.formula_row = formula_row

    # ══════════════════════════════════════════════════
    # 场景 4：包含除演示
    # ══════════════════════════════════════════════════
    def scene_containing_division(self):
        sec_title = Text("包含除", font="PingFang SC",
                         font_size=44, color=C_TITLE)
        sec_title.move_to(UP * 6.5)

        # 把已有公式往下移一点，给标题让位
        self.play(
            self.formula_row.animate.move_to(UP * 5.8),
            Write(sec_title),
            run_time=0.6,
        )

        desc = Text("12个苹果，每3个装一袋", font="PingFang SC",
                    font_size=28, color=C_HINT)
        desc.move_to(UP * 5.0)
        question2 = Text("能装几袋？", font="PingFang SC",
                         font_size=32, color=C_BAG)
        question2.move_to(UP * 4.3)
        self.play(FadeIn(desc), FadeIn(question2, shift=UP * 0.1), run_time=0.6)
        self.wait(0.4)

        # ── 12 个苹果横排 ──
        apples2 = self.make_apple_group(12, cols=12, h_buff=0.6, v_buff=0.7)
        apples2.move_to(UP * 3.1)
        self.play(LaggedStart(
            *[GrowFromCenter(a) for a in apples2],
            lag_ratio=0.06,
        ), run_time=1.0)
        self.wait(0.3)

        # ── 每3个用括号圈起来，依次装袋 ──
        bag_color = C_BAG
        bag_anims_list = []

        bag_group_positions = []  # 存储每袋中心
        brackets = VGroup()
        bag_labels = VGroup()
        bag_count = 4
        apples_per_bag = 3

        for bag_i in range(bag_count):
            group_apples = apples2[bag_i * apples_per_bag:(bag_i + 1) * apples_per_bag]
            brace = Brace(group_apples, direction=DOWN, color=bag_color, buff=0.08)
            b_lbl = Text(f"第{bag_i+1}袋", font="PingFang SC",
                         font_size=20, color=bag_color)
            b_lbl.next_to(brace, DOWN, buff=0.08)
            brackets.add(brace)
            bag_labels.add(b_lbl)
            bag_group_positions.append(group_apples.get_center())

        # 逐袋动画
        for bag_i in range(bag_count):
            self.play(
                Create(brackets[bag_i]),
                run_time=0.4,
            )
            self.play(
                FadeIn(bag_labels[bag_i]),
                run_time=0.3,
            )
            self.wait(0.2)

        self.wait(0.8)

        # ── 标注共4袋 ──
        result_text = Text("共装了 4 袋！", font="PingFang SC",
                           font_size=34, color=C_FORMULA)
        result_text.move_to(DOWN * 1.2)
        self.play(Write(result_text), run_time=0.7)
        self.wait(1.0)

        # ── 同样是 12 ÷ 3 = 4 ──
        same_formula = Text("同样是  12 ÷ 3 = 4", font="PingFang SC",
                            font_size=32, color=C_TITLE)
        same_formula.move_to(DOWN * 2.2)
        self.play(Write(same_formula), run_time=0.7)
        self.wait(1.5)

        # 清场
        self.play(
            FadeOut(sec_title), FadeOut(desc), FadeOut(question2),
            FadeOut(apples2), FadeOut(brackets), FadeOut(bag_labels),
            FadeOut(result_text), FadeOut(same_formula),
            run_time=0.6,
        )

    # ══════════════════════════════════════════════════
    # 场景 5：总结对比
    # ══════════════════════════════════════════════════
    def scene_summary(self):
        # 清掉悬浮算式
        self.play(FadeOut(self.formula_row), run_time=0.3)

        sec_title = Text("总结", font="PingFang SC",
                         font_size=44, color=C_TITLE)
        sec_title.move_to(UP * 6.5)
        self.play(Write(sec_title), run_time=0.5)

        # ── 两种除法对比卡片 ──
        # 等分除卡片
        card_bg1 = RoundedRectangle(
            corner_radius=0.3, width=7.8, height=2.8,
            color=C_PLATE, fill_color=C_PLATE, fill_opacity=0.12,
            stroke_width=2,
        )
        card_bg1.move_to(UP * 4.3)

        card1_type  = Text("等分除", font="PingFang SC",
                           font_size=32, color=C_PLATE)
        card1_type.move_to(card_bg1.get_top() + DOWN * 0.45)

        card1_desc  = Text("已知总数和份数，求每份数",
                           font="PingFang SC", font_size=24, color=C_HINT)
        card1_desc.next_to(card1_type, DOWN, buff=0.2)

        card1_ex    = Text("12个苹果平均分给3人 → 每人4个",
                           font="PingFang SC", font_size=22, color=C_APPLE_HL)
        card1_ex.next_to(card1_desc, DOWN, buff=0.18)

        card1 = VGroup(card_bg1, card1_type, card1_desc, card1_ex)

        # 包含除卡片
        card_bg2 = RoundedRectangle(
            corner_radius=0.3, width=7.8, height=2.8,
            color=C_BAG, fill_color=C_BAG, fill_opacity=0.12,
            stroke_width=2,
        )
        card_bg2.move_to(UP * 1.0)

        card2_type  = Text("包含除", font="PingFang SC",
                           font_size=32, color=C_BAG)
        card2_type.move_to(card_bg2.get_top() + DOWN * 0.45)

        card2_desc  = Text("已知总数和每份数，求份数",
                           font="PingFang SC", font_size=24, color=C_HINT)
        card2_desc.next_to(card2_type, DOWN, buff=0.2)

        card2_ex    = Text("12个苹果每3个一袋 → 共4袋",
                           font="PingFang SC", font_size=22, color=C_BAG)
        card2_ex.next_to(card2_desc, DOWN, buff=0.18)

        card2 = VGroup(card_bg2, card2_type, card2_desc, card2_ex)

        self.play(
            FadeIn(card1, shift=RIGHT * 0.3),
            run_time=0.7,
        )
        self.wait(0.3)
        self.play(
            FadeIn(card2, shift=RIGHT * 0.3),
            run_time=0.7,
        )
        self.wait(0.5)

        # ── 公式框 ──
        formula_box_bg = RoundedRectangle(
            corner_radius=0.3, width=7.8, height=1.8,
            color=C_TITLE, fill_color=C_TITLE, fill_opacity=0.12,
            stroke_width=2,
        )
        formula_box_bg.move_to(DOWN * 1.8)

        formula_label = Text("统一用除法算式表示：",
                             font="PingFang SC", font_size=24, color=C_HINT)
        formula_label.move_to(formula_box_bg.get_top() + DOWN * 0.4)

        formula_parts = VGroup(
            Text("12", font="PingFang SC", font_size=40, color=C_APPLE_HL),
            Text("÷",  font="PingFang SC", font_size=40, color=C_DIV_SIGN),
            Text("3",  font="PingFang SC", font_size=40, color=C_PLATE),
            Text("=",  font="PingFang SC", font_size=40, color=WHITE),
            Text("4",  font="PingFang SC", font_size=40, color=C_FORMULA),
        )
        formula_parts.arrange(RIGHT, buff=0.4)
        formula_parts.next_to(formula_label, DOWN, buff=0.15)

        formula_box = VGroup(formula_box_bg, formula_label, formula_parts)

        self.play(FadeIn(formula_box, shift=UP * 0.2), run_time=0.7)
        self.wait(1.0)

        # 名称卡片：被除数 除数 商
        term_row = VGroup(
            VGroup(
                Text("12", font="PingFang SC", font_size=28, color=C_APPLE_HL),
                Text("被除数", font="PingFang SC", font_size=20, color=C_DIM),
            ).arrange(DOWN, buff=0.08),
            VGroup(
                Text("3",  font="PingFang SC", font_size=28, color=C_PLATE),
                Text("除数", font="PingFang SC", font_size=20, color=C_DIM),
            ).arrange(DOWN, buff=0.08),
            VGroup(
                Text("4",  font="PingFang SC", font_size=28, color=C_FORMULA),
                Text("商",  font="PingFang SC", font_size=20, color=C_DIM),
            ).arrange(DOWN, buff=0.08),
        )
        term_row.arrange(RIGHT, buff=1.8)
        term_row.move_to(DOWN * 3.2)

        self.play(
            LaggedStart(*[FadeIn(t, shift=UP * 0.1) for t in term_row],
                        lag_ratio=0.25),
            run_time=0.8,
        )
        self.wait(2.0)

        # 清场
        self.play(
            FadeOut(sec_title),
            FadeOut(card1), FadeOut(card2),
            FadeOut(formula_box), FadeOut(term_row),
            run_time=0.7,
        )

    # ══════════════════════════════════════════════════
    # 场景 6：片尾
    # ══════════════════════════════════════════════════
    def scene_outro(self):
        # 大作者名
        outro_name = Text("上海初高中数学直通车",
                          font="PingFang SC",
                          font_size=42, color=WHITE)
        outro_name.move_to(UP * 2.0)

        outro_id = Text("@emptyandcalm",
                        font="PingFang SC",
                        font_size=32, color=C_DIM)
        outro_id.next_to(outro_name, DOWN, buff=0.3)

        follow = Text("关注我，获得更多数学技巧！",
                      font="PingFang SC",
                      font_size=30, color=C_TITLE)
        follow.move_to(DOWN * 0.2)

        # 小装饰：苹果散落
        deco_apples = VGroup(*[
            self.make_apple(radius=0.18).move_to(
                np.array([
                    3.0 * np.cos(i * TAU / 8),
                    3.0 * np.sin(i * TAU / 8),
                    0,
                ])
            )
            for i in range(8)
        ])
        deco_apples.move_to(DOWN * 2.5)

        self.play(
            Transform(self.author_label, outro_name),
            run_time=0.7,
        )
        self.play(FadeIn(outro_id, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(follow, scale=1.05), run_time=0.6)
        self.play(
            LaggedStart(*[GrowFromCenter(a) for a in deco_apples],
                        lag_ratio=0.1),
            run_time=0.8,
        )
        self.play(Rotate(deco_apples, angle=PI * 0.5, run_time=1.2))
        self.wait(1.5)

        self.play(
            FadeOut(self.author_label),
            FadeOut(outro_id),
            FadeOut(follow),
            FadeOut(deco_apples),
            run_time=0.8,
        )
