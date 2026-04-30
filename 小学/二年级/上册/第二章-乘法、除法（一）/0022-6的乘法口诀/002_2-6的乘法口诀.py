"""
2-6的乘法口诀 - 二年级数学教学动画
学习顺序：2、5、4、3、6的乘法口诀
目标观众：二年级小学生
格式：TikTok竖屏 (1080×1920)
作者：上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# 全局配置 - TikTok竖屏尺寸
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


# 颜色配置
COLOR_BG = "#1a1a2e"
COLOR_TWO = "#e74c3c"      # 红色 - 2的口诀
COLOR_FIVE = "#3498db"     # 蓝色 - 5的口诀
COLOR_FOUR = "#2ecc71"     # 绿色 - 4的口诀
COLOR_THREE = "#f39c12"    # 橙色 - 3的口诀
COLOR_SIX = "#9b59b6"      # 紫色 - 6的口诀
COLOR_HIGHLIGHT = YELLOW
COLOR_CARD_BG = "#16213e"


class MultiplicationTableLesson(Scene):
    """
    2-6乘法口诀教学动画

    场景顺序：
    1. 开场 - 钩子问题
    2. 2的乘法口诀
    3. 5的乘法口诀
    4. 4的乘法口诀
    5. 3的乘法口诀
    6. 6的乘法口诀（难点）
    7. 总结回顾
    8. 片尾
    """

    def construct(self):
        self.camera.background_color = COLOR_BG

        # 作者信息 (顶部，贯穿全程)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)

        # 执行各场景
        self.scene_opening()
        self.scene_two_table()
        self.scene_five_table()
        self.scene_four_table()
        self.scene_three_table()
        self.scene_six_table()
        self.scene_summary()
        self.scene_outro()

    # ─────────────────────────────────────────────
    # 辅助：创建口诀卡片（单行）
    # ─────────────────────────────────────────────
    def make_chant_card(self, chant_text, equation_text, color, width=7.5, height=0.85):
        """创建一张口诀卡片：左边口诀，右边算式"""
        bg = RoundedRectangle(
            width=width, height=height,
            corner_radius=0.15,
            fill_color=COLOR_CARD_BG,
            fill_opacity=1,
            stroke_color=color,
            stroke_width=2
        )
        left_accent = Rectangle(
            width=0.18, height=height,
            fill_color=color, fill_opacity=1,
            stroke_width=0
        ).align_to(bg, LEFT)

        chant = Text(
            chant_text,
            font="PingFang SC",
            font_size=26,
            color=WHITE
        ).next_to(left_accent, RIGHT, buff=0.25)

        eq = Text(
            equation_text,
            font="PingFang SC",
            font_size=22,
            color=color
        ).align_to(bg, RIGHT).shift(LEFT * 0.3)

        card = VGroup(bg, left_accent, chant, eq)
        return card

    # ─────────────────────────────────────────────
    # 辅助：创建点阵（rows × cols）
    # ─────────────────────────────────────────────
    def make_dot_array(self, rows, cols, color, dot_radius=0.12, gap=0.32):
        """创建 rows 行 cols 列的点阵"""
        group = VGroup()
        for r in range(rows):
            for c in range(cols):
                d = Dot(radius=dot_radius, color=color, fill_opacity=0.9)
                d.move_to(RIGHT * c * gap + DOWN * r * gap)
                group.add(d)
        return group

    # ─────────────────────────────────────────────
    # 场景 1：开场
    # ─────────────────────────────────────────────
    def scene_opening(self):
        title = Text(
            "2-6 的乘法口诀",
            font="PingFang SC",
            font_size=52,
            color=GOLD
        ).move_to(UP * 5.8)

        subtitle = Text(
            "背熟口诀，计算更快！",
            font="PingFang SC",
            font_size=30,
            color=GRAY_A
        ).move_to(UP * 4.9)

        hook = Text(
            "你能背出六六三十六吗？",
            font="PingFang SC",
            font_size=28,
            color=COLOR_HIGHLIGHT
        ).move_to(UP * 3.8)

        # 五组颜色圆圈代表 2-6 数字
        circles = VGroup()
        nums = ["2", "5", "4", "3", "6"]
        colors = [COLOR_TWO, COLOR_FIVE, COLOR_FOUR, COLOR_THREE, COLOR_SIX]
        for i, (n, c) in enumerate(zip(nums, colors)):
            circ = Circle(radius=0.45, color=c, fill_color=c, fill_opacity=0.85)
            label = Text(n, font="PingFang SC", font_size=28, color=WHITE)
            label.move_to(circ.get_center())
            circles.add(VGroup(circ, label))
        circles.arrange(RIGHT, buff=0.45).move_to(UP * 2.2)

        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.4)
        self.play(FadeIn(hook, shift=UP * 0.3), run_time=0.5)

        self.play(
            LaggedStart(*[GrowFromCenter(c) for c in circles], lag_ratio=0.15),
            run_time=1.0
        )
        self.wait(1.0)

        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(hook),
            FadeOut(circles),
            run_time=0.5
        )

    # ─────────────────────────────────────────────
    # 场景 2：2 的乘法口诀
    # ─────────────────────────────────────────────
    def scene_two_table(self):
        color = COLOR_TWO
        header = Text("2 的乘法口诀", font="PingFang SC",
                      font_size=40, color=color).move_to(UP * 6.2)
        tip = Text("规律：结果都是偶数", font="PingFang SC",
                   font_size=22, color=GRAY_A).move_to(UP * 5.4)

        self.play(Write(header), run_time=0.6)
        self.play(FadeIn(tip), run_time=0.3)

        chants = [
            ("一二得二",   "1×2=2"),
            ("二二得四",   "2×2=4"),
            ("三二得六",   "3×2=6"),
            ("四二得八",   "4×2=8"),
            ("五二得十",   "5×2=10"),
            ("六二十二",   "6×2=12"),
        ]

        cards = VGroup()
        for i, (chant, eq) in enumerate(chants):
            card = self.make_chant_card(chant, eq, color)
            card.move_to(UP * (4.4 - i * 1.0))
            cards.add(card)

        # 先展示点阵说明 2 的含义
        dot_demo = self.make_dot_array(2, 2, color).scale(0.9).move_to(RIGHT * 2.5 + UP * 3.5)
        demo_label = Text("2×2=4", font="PingFang SC", font_size=22, color=color)
        demo_label.next_to(dot_demo, DOWN, buff=0.2)

        self.play(Create(dot_demo), FadeIn(demo_label), run_time=0.8)
        self.wait(0.5)
        self.play(FadeOut(dot_demo), FadeOut(demo_label), run_time=0.3)

        # 逐张呈现卡片
        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.15)

        # 高亮 "二二得四"
        self.play(Indicate(cards[1], color=COLOR_HIGHLIGHT, scale_factor=1.05), run_time=0.6)
        self.wait(1.2)

        self.play(FadeOut(header), FadeOut(tip), FadeOut(cards), run_time=0.5)

    # ─────────────────────────────────────────────
    # 场景 3：5 的乘法口诀
    # ─────────────────────────────────────────────
    def scene_five_table(self):
        color = COLOR_FIVE
        header = Text("5 的乘法口诀", font="PingFang SC",
                      font_size=40, color=color).move_to(UP * 6.2)
        tip = Text("规律：结果末尾是 0 或 5", font="PingFang SC",
                   font_size=22, color=GRAY_A).move_to(UP * 5.4)

        self.play(Write(header), run_time=0.6)
        self.play(FadeIn(tip), run_time=0.3)

        chants = [
            ("一五得五",   "1×5=5"),
            ("二五一十",   "2×5=10"),
            ("三五十五",   "3×5=15"),
            ("四五二十",   "4×5=20"),
            ("五五二十五", "5×5=25"),
            ("六五三十",   "6×5=30"),
        ]

        cards = VGroup()
        for i, (chant, eq) in enumerate(chants):
            card = self.make_chant_card(chant, eq, color)
            card.move_to(UP * (4.4 - i * 1.0))
            cards.add(card)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.15)

        # 高亮 "五五二十五"
        self.play(Indicate(cards[4], color=COLOR_HIGHLIGHT, scale_factor=1.05), run_time=0.6)

        # 展示末尾规律
        pattern = Text("5, 10, 15, 20, 25, 30 …", font="PingFang SC",
                       font_size=24, color=COLOR_HIGHLIGHT).move_to(DOWN * 4.5)
        self.play(FadeIn(pattern, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(header), FadeOut(tip), FadeOut(cards), FadeOut(pattern), run_time=0.5)

    # ─────────────────────────────────────────────
    # 场景 4：4 的乘法口诀
    # ─────────────────────────────────────────────
    def scene_four_table(self):
        color = COLOR_FOUR
        header = Text("4 的乘法口诀", font="PingFang SC",
                      font_size=40, color=color).move_to(UP * 6.2)
        tip = Text("重点：四六二十四", font="PingFang SC",
                   font_size=22, color=GRAY_A).move_to(UP * 5.4)

        self.play(Write(header), run_time=0.6)
        self.play(FadeIn(tip), run_time=0.3)

        chants = [
            ("一四得四",   "1×4=4"),
            ("二四得八",   "2×4=8"),
            ("三四十二",   "3×4=12"),
            ("四四十六",   "4×4=16"),
            ("五四二十",   "5×4=20"),
            ("六四二十四", "6×4=24"),
        ]

        cards = VGroup()
        for i, (chant, eq) in enumerate(chants):
            card = self.make_chant_card(chant, eq, color)
            card.move_to(UP * (4.4 - i * 1.0))
            cards.add(card)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.15)

        # 高亮 "六四二十四"
        self.play(Indicate(cards[5], color=COLOR_HIGHLIGHT, scale_factor=1.05), run_time=0.6)

        # 点阵演示 4×4
        dot_demo = self.make_dot_array(4, 4, color, dot_radius=0.10, gap=0.28)
        dot_demo.scale(0.85).move_to(LEFT * 2.8 + DOWN * 3.8)
        dot_label = Text("4×4=16", font="PingFang SC", font_size=22, color=color)
        dot_label.next_to(dot_demo, DOWN, buff=0.18)
        self.play(Create(dot_demo), FadeIn(dot_label), run_time=0.8)
        self.wait(1.2)

        self.play(FadeOut(header), FadeOut(tip), FadeOut(cards),
                  FadeOut(dot_demo), FadeOut(dot_label), run_time=0.5)

    # ─────────────────────────────────────────────
    # 场景 5：3 的乘法口诀
    # ─────────────────────────────────────────────
    def scene_three_table(self):
        color = COLOR_THREE
        header = Text("3 的乘法口诀", font="PingFang SC",
                      font_size=40, color=color).move_to(UP * 6.2)
        tip = Text("重点：三六十八", font="PingFang SC",
                   font_size=22, color=GRAY_A).move_to(UP * 5.4)

        self.play(Write(header), run_time=0.6)
        self.play(FadeIn(tip), run_time=0.3)

        chants = [
            ("一三得三",   "1×3=3"),
            ("二三得六",   "2×3=6"),
            ("三三得九",   "3×3=9"),
            ("四三十二",   "4×3=12"),
            ("五三十五",   "5×3=15"),
            ("六三十八",   "6×3=18"),
        ]

        cards = VGroup()
        for i, (chant, eq) in enumerate(chants):
            card = self.make_chant_card(chant, eq, color)
            card.move_to(UP * (4.4 - i * 1.0))
            cards.add(card)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.15)

        # 高亮 "六三十八"（三六十八等价）
        self.play(Indicate(cards[5], color=COLOR_HIGHLIGHT, scale_factor=1.05), run_time=0.6)

        # 口诀关联说明
        note = Text("三六十八 = 六三十八", font="PingFang SC",
                    font_size=24, color=COLOR_HIGHLIGHT).move_to(DOWN * 4.5)
        self.play(FadeIn(note, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(header), FadeOut(tip), FadeOut(cards), FadeOut(note), run_time=0.5)

    # ─────────────────────────────────────────────
    # 场景 6：6 的乘法口诀（难点）
    # ─────────────────────────────────────────────
    def scene_six_table(self):
        color = COLOR_SIX
        header = Text("6 的乘法口诀", font="PingFang SC",
                      font_size=40, color=color).move_to(UP * 6.2)
        hard_label = Text("★ 难点", font="PingFang SC",
                          font_size=22, color=RED).next_to(header, RIGHT, buff=0.3)
        tip = Text("逆背挑战：几六二十四？→ 四六二十四", font="PingFang SC",
                   font_size=20, color=GRAY_A).move_to(UP * 5.4)

        self.play(Write(header), FadeIn(hard_label), run_time=0.7)
        self.play(FadeIn(tip), run_time=0.3)

        chants = [
            ("一六得六",   "1×6=6"),
            ("二六十二",   "2×6=12"),
            ("三六十八",   "3×6=18"),
            ("四六二十四", "4×6=24"),
            ("五六三十",   "5×6=30"),
            ("六六三十六", "6×6=36"),
        ]

        cards = VGroup()
        for i, (chant, eq) in enumerate(chants):
            card = self.make_chant_card(chant, eq, color)
            card.move_to(UP * (4.4 - i * 1.0))
            cards.add(card)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.4)
            self.wait(0.15)

        # 依次高亮关键口诀
        key_indices = [3, 5]   # 四六二十四, 六六三十六
        for idx in key_indices:
            self.play(Indicate(cards[idx], color=COLOR_HIGHLIGHT, scale_factor=1.06), run_time=0.7)
            self.wait(0.3)

        # 逆背互动提示
        question = Text("几 × 6 = 36 ？", font="PingFang SC",
                        font_size=30, color=COLOR_HIGHLIGHT).move_to(DOWN * 4.2)
        answer = Text("→ 6！（六六三十六）", font="PingFang SC",
                      font_size=26, color=WHITE).move_to(DOWN * 5.0)

        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.5)
        self.wait(1.0)
        self.play(FadeIn(answer, shift=UP * 0.3), run_time=0.5)
        self.wait(1.5)

        # 点阵演示 6×6
        dot_demo = self.make_dot_array(6, 6, color, dot_radius=0.09, gap=0.26)
        dot_demo.scale(0.75).move_to(LEFT * 2.8 + DOWN * 4.5)
        dot_label = Text("6×6=36", font="PingFang SC", font_size=22, color=color)
        dot_label.next_to(dot_demo, DOWN, buff=0.15)
        self.play(Create(dot_demo), FadeIn(dot_label), run_time=1.0)
        self.wait(1.0)

        self.play(
            FadeOut(header), FadeOut(hard_label), FadeOut(tip),
            FadeOut(cards), FadeOut(question), FadeOut(answer),
            FadeOut(dot_demo), FadeOut(dot_label),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # 场景 7：总结回顾
    # ─────────────────────────────────────────────
    def scene_summary(self):
        title = Text("核心口诀总回顾", font="PingFang SC",
                     font_size=38, color=GOLD).move_to(UP * 6.3)
        self.play(Write(title), run_time=0.7)

        # 精选 5 条重要口诀（题目中点名的）
        key_chants = [
            ("二二得四",   "2×2=4",   COLOR_TWO),
            ("五五二十五", "5×5=25",  COLOR_FIVE),
            ("四六二十四", "4×6=24",  COLOR_FOUR),
            ("三六十八",   "3×6=18",  COLOR_THREE),
            ("六六三十六", "6×6=36",  COLOR_SIX),
        ]

        summary_cards = VGroup()
        for i, (chant, eq, color) in enumerate(key_chants):
            card = self.make_chant_card(chant, eq, color, width=7.2, height=0.88)
            card.move_to(UP * (4.5 - i * 1.1))
            summary_cards.add(card)

        self.play(
            LaggedStart(*[FadeIn(c, shift=LEFT * 0.4) for c in summary_cards],
                        lag_ratio=0.18),
            run_time=1.2
        )
        self.wait(0.5)

        # 逐一闪烁
        for card in summary_cards:
            self.play(Indicate(card, scale_factor=1.04), run_time=0.4)

        # 逆背提示条幅
        banner = RoundedRectangle(
            width=7.5, height=0.9,
            corner_radius=0.2,
            fill_color="#2d1b69", fill_opacity=1,
            stroke_color=GOLD, stroke_width=2.5
        ).move_to(DOWN * 4.2)
        banner_text = Text(
            "记正背，也要练逆背！",
            font="PingFang SC",
            font_size=26,
            color=GOLD
        ).move_to(banner.get_center())
        self.play(FadeIn(banner), FadeIn(banner_text), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(summary_cards),
            FadeOut(banner), FadeOut(banner_text),
            run_time=0.6
        )

    # ─────────────────────────────────────────────
    # 场景 8：片尾
    # ─────────────────────────────────────────────
    def scene_outro(self):
        author_name = Text(
            "上海初高中数学直通车",
            font="PingFang SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.8)

        author_id = Text(
            "@emptyandcalm",
            font="PingFang SC",
            font_size=30,
            color=GRAY_B
        ).move_to(UP * 0.8)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.3)

        self.play(Write(author_name), run_time=0.8)
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.08), run_time=0.6)

        # 五彩小圆圈装饰
        deco_colors = [COLOR_TWO, COLOR_FIVE, COLOR_FOUR, COLOR_THREE, COLOR_SIX, GOLD]
        decorations = VGroup(*[
            Circle(radius=0.22, color=deco_colors[i % len(deco_colors)],
                   fill_color=deco_colors[i % len(deco_colors)], fill_opacity=0.85)
            .move_to(follow_text.get_center() +
                     2.3 * np.array([np.cos(i * TAU / 6), np.sin(i * TAU / 6), 0]))
            for i in range(6)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in decorations], lag_ratio=0.1),
            run_time=0.7
        )
        self.play(Rotate(decorations, angle=PI, run_time=1.5))

        # 关键口诀快闪
        flash_chants = ["二二得四", "五五二十五", "六六三十六"]
        flash_colors = [COLOR_TWO, COLOR_FIVE, COLOR_SIX]
        for chant, col in zip(flash_chants, flash_colors):
            ft = Text(chant, font="PingFang SC", font_size=32, color=col)
            ft.move_to(DOWN * 3.0)
            self.play(FadeIn(ft, scale=1.2), run_time=0.35)
            self.wait(0.25)
            self.play(FadeOut(ft), run_time=0.2)

        self.wait(1.5)
        self.play(
            FadeOut(self.author_info),
            FadeOut(author_name),
            FadeOut(author_id),
            FadeOut(follow_text),
            FadeOut(decorations),
            run_time=1.0
        )


if __name__ == "__main__":
    # manim -qm 002_2-6的乘法口诀.py MultiplicationTableLesson
    pass
