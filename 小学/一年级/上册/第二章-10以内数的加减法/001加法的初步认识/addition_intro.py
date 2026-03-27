"""
addition_intro.py  ──  加法的初步认识
一年级上册·第二章·10以内数的加减法

内容: 加法含义（合并求总）、加号、2+1=3、加数+加数=和
目标: TikTok 竖屏 1080×1920，约55秒
作者: 上海初高中数学直通车  @emptyandcalm
"""

from manim import *
import numpy as np

# ═══════════════════════════════════════════════════════
# 全局配置
# ═══════════════════════════════════════════════════════
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

BG_COLOR  = "#1a1a2e"
C_PLUS    = "#f1c40f"   # 黄  → 加号 +
C_LEFT    = "#3498db"   # 蓝  → 左加数（2）
C_RIGHT   = "#e74c3c"   # 红  → 右加数（1）
C_SUM     = "#2ecc71"   # 绿  → 和（3）
C_ACTIVE  = "#f97316"   # 橙  → 动作高亮
C_DIM     = "#888899"
FONT      = "Noto Sans CJK SC"

# 布局常量（与 verify_addition.py 一致）
LEFT_CX, LEFT_CY, LEFT_SP, LEFT_R    = -2.5, 2.5, 1.0, 0.42
RIGHT_CX, RIGHT_CY, RIGHT_R          =  2.5, 2.5, 0.42
MERGE_CX, MERGE_CY, MERGE_SP, MERGE_R =  0.0, 2.5, 1.0, 0.42

BALLOON_COLORS = ["#60a5fa","#818cf8","#f472b6","#34d399","#fbbf24"]


def row_centers(n, cx, cy, sp):
    return [np.array([cx + (i-(n-1)/2.0)*sp, cy, 0.0]) for i in range(n)]


def make_balloon(pos, r, color, label=""):
    """气球：圆 + 小尾巴 + 可选数字"""
    body = Circle(radius=r, fill_color=color, fill_opacity=1,
                  stroke_color=WHITE, stroke_width=2).move_to(pos)
    # 小尾巴
    tail = Line(pos + DOWN * r, pos + DOWN * (r + 0.25),
                color=color, stroke_width=2)
    grp = VGroup(body, tail)
    if label:
        lbl = Text(label, font=FONT, font_size=int(r*80), color=WHITE)
        lbl.move_to(pos)
        grp.add(lbl)
    return grp


# ═══════════════════════════════════════════════════════
class AdditionIntro(Scene):

    def construct(self):
        self.camera.background_color = BG_COLOR

        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=C_DIM,
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        self.scene_1_hook()
        self.scene_2_story()
        self.scene_3_plus_sign()
        self.scene_4_formula()
        self.scene_5_more_examples()
        self.scene_6_terms()
        self.scene_7_outro()

    # ─────────────────────────────────────────
    # Scene 1: 开场钩子
    # ─────────────────────────────────────────
    def scene_1_hook(self):
        title = Text("加法的初步认识", font=FONT, font_size=46, color=C_PLUS)
        title.move_to(UP * 5.6)
        sub = Text("把两部分合起来！", font=FONT, font_size=34, color=WHITE)
        sub.move_to(UP * 4.7)
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # 大号加号从中心生长
        plus_big = MathTex(r"+", font_size=160, color=C_PLUS)
        plus_big.move_to(UP * 2.5)
        self.play(GrowFromCenter(plus_big), run_time=0.7)
        self.play(Flash(plus_big, color=C_PLUS, flash_radius=1.5), run_time=0.4)
        self.wait(0.4)

        self.play(FadeOut(title), FadeOut(sub), FadeOut(plus_big), run_time=0.5)

    # ─────────────────────────────────────────
    # Scene 2: 气球故事
    # ─────────────────────────────────────────
    def scene_2_story(self):
        sec_title = Text("气球的故事", font=FONT, font_size=42, color=C_ACTIVE)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.4)

        # ── 左手2个气球
        story_l = Text("左手有  2  个气球", font=FONT, font_size=28, color=C_LEFT)
        story_l.move_to(UP * 5.1)
        self.play(FadeIn(story_l), run_time=0.3)

        lc = row_centers(2, LEFT_CX, LEFT_CY, LEFT_SP)
        left_balloons = VGroup(*[
            make_balloon(p, LEFT_R, BALLOON_COLORS[i]) for i, p in enumerate(lc)
        ])
        for b in left_balloons:
            self.play(GrowFromCenter(b), run_time=0.25)

        # 左侧数量标注
        lbl_2 = Text("2", font=FONT, font_size=50, color=C_LEFT)
        lbl_2.next_to(left_balloons, DOWN, buff=0.3)
        self.play(FadeIn(lbl_2), run_time=0.3)
        self.wait(0.3)

        # ── 右手1个气球
        story_r = Text("右手有  1  个气球", font=FONT, font_size=28, color=C_RIGHT)
        story_r.move_to(UP * 5.1)
        self.play(Transform(story_l, story_r), run_time=0.3)

        rc = row_centers(1, RIGHT_CX, RIGHT_CY, 0)
        right_balloon = VGroup(make_balloon(rc[0], RIGHT_R, BALLOON_COLORS[2]))
        self.play(GrowFromCenter(right_balloon), run_time=0.3)

        lbl_1 = Text("1", font=FONT, font_size=50, color=C_RIGHT)
        lbl_1.next_to(right_balloon, DOWN, buff=0.3)
        self.play(FadeIn(lbl_1), run_time=0.3)
        self.wait(0.4)

        # ── 合起来
        question = Text("合起来有几个？", font=FONT, font_size=32, color=WHITE)
        question.move_to(UP * 5.1)
        self.play(Transform(story_l, question), run_time=0.3)

        # 气球向中心移动
        mc = row_centers(3, MERGE_CX, MERGE_CY, MERGE_SP)
        self.play(
            left_balloons[0].animate.move_to(mc[0]),
            left_balloons[1].animate.move_to(mc[1]),
            right_balloon[0].animate.move_to(mc[2]),
            run_time=0.8,
        )

        # 合并后整体变绿
        merged = VGroup(left_balloons[0][0], left_balloons[1][0], right_balloon[0][0])
        self.play(
            *[c.animate.set_fill(C_SUM) for c in merged],
            run_time=0.4,
        )
        self.play(
            Flash(VGroup(left_balloons, right_balloon),
                  color=C_SUM, flash_radius=2.0),
            run_time=0.4,
        )

        # 合并后标注3
        lbl_3 = Text("3  个！", font=FONT, font_size=50, color=C_SUM)
        lbl_3.move_to(DOWN * 0.8)
        self.play(FadeIn(lbl_3, scale=1.2), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(sec_title), FadeOut(story_l),
            FadeOut(left_balloons), FadeOut(right_balloon),
            FadeOut(lbl_2), FadeOut(lbl_1), FadeOut(lbl_3),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 3: 认识加号
    # ─────────────────────────────────────────
    def scene_3_plus_sign(self):
        sec_title = Text("认识加号  +", font=FONT, font_size=42, color=C_PLUS)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.4)

        plus = MathTex(r"+", font_size=130, color=C_PLUS)
        plus.move_to(UP * 3.5)
        self.play(GrowFromCenter(plus), run_time=0.6)

        # 含义标注
        meaning_1 = Text("表示：把两部分", font=FONT, font_size=30, color=WHITE)
        meaning_2 = Text("合并", font=FONT, font_size=30, color=C_PLUS)
        meaning_3 = Text("在一起", font=FONT, font_size=30, color=WHITE)
        meaning = VGroup(meaning_1, meaning_2, meaning_3).arrange(RIGHT, buff=0.1)
        meaning.move_to(UP * 1.5)
        self.play(FadeIn(meaning), run_time=0.5)

        meaning_b = Text("求一共有多少", font=FONT, font_size=30, color=C_ACTIVE)
        meaning_b.move_to(UP * 0.7)
        self.play(FadeIn(meaning_b), run_time=0.4)

        # 可视化：两个小球靠近
        ball_l = Circle(radius=0.35, fill_color=C_LEFT, fill_opacity=1,
                        stroke_width=0).move_to(LEFT * 3.0 + DOWN * 1.2)
        ball_r = Circle(radius=0.35, fill_color=C_RIGHT, fill_opacity=1,
                        stroke_width=0).move_to(RIGHT * 3.0 + DOWN * 1.2)
        plus_small = MathTex(r"+", font_size=50, color=C_PLUS).move_to(DOWN * 1.2)

        self.play(FadeIn(ball_l), FadeIn(plus_small), FadeIn(ball_r), run_time=0.4)

        # 靠拢
        self.play(
            ball_l.animate.move_to(LEFT * 0.4 + DOWN * 1.2),
            ball_r.animate.move_to(RIGHT * 0.4 + DOWN * 1.2),
            plus_small.animate.set_color(C_ACTIVE).scale(1.3),
            run_time=0.7,
        )
        self.wait(0.8)

        self.play(
            FadeOut(sec_title), FadeOut(plus), FadeOut(meaning), FadeOut(meaning_b),
            FadeOut(ball_l), FadeOut(plus_small), FadeOut(ball_r),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 4: 公式 2+1=3
    # ─────────────────────────────────────────
    def scene_4_formula(self):
        sec_title = Text("写出算式", font=FONT, font_size=42, color=WHITE)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.4)

        # 左2气球
        lc = row_centers(2, LEFT_CX, LEFT_CY, LEFT_SP)
        left_b = VGroup(*[
            make_balloon(p, LEFT_R, BALLOON_COLORS[i]) for i, p in enumerate(lc)
        ])
        for b in left_b:
            self.play(GrowFromCenter(b), run_time=0.2)

        # 加号大幅飞入
        plus = MathTex(r"+", font_size=80, color=C_PLUS).move_to(UP * 2.5)
        self.play(GrowFromCenter(plus), run_time=0.35)

        # 右1气球
        rc = row_centers(1, RIGHT_CX, RIGHT_CY, 0)
        right_b = VGroup(make_balloon(rc[0], RIGHT_R, BALLOON_COLORS[2]))
        self.play(GrowFromCenter(right_b), run_time=0.2)

        self.wait(0.3)

        # 大算式逐步显示
        formula = MathTex(r"2 + 1 = 3", font_size=80, color=WHITE)
        formula[0][0].set_color(C_LEFT)
        formula[0][1].set_color(C_PLUS)
        formula[0][2].set_color(C_RIGHT)
        formula[0][4].set_color(C_SUM)
        formula.move_to(DOWN * 1.0)

        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula[0][4], scale_factor=1.5, color=C_SUM), run_time=0.5)

        # 读法
        reading = VGroup(
            Text("读作：", font=FONT, font_size=26, color=C_DIM),
            Text("2加1等于3", font=FONT, font_size=28, color=WHITE),
        ).arrange(RIGHT, buff=0.1).move_to(DOWN * 2.5)
        self.play(FadeIn(reading), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(sec_title), FadeOut(left_b), FadeOut(plus), FadeOut(right_b),
            FadeOut(formula), FadeOut(reading),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 5: 更多示例
    # ─────────────────────────────────────────
    def scene_5_more_examples(self):
        sec_title = Text("再来几个！", font=FONT, font_size=42, color=C_ACTIVE)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.4)

        examples = [
            (1, 2, 3, r"1 + 2 = 3"),
            (3, 1, 4, r"3 + 1 = 4"),
            (2, 2, 4, r"2 + 2 = 4"),
        ]

        y_positions = [4.8, 3.3, 1.8]

        all_items = VGroup()
        for i, ((a, b, c, formula_str), y) in enumerate(zip(examples, y_positions)):
            # 小圆点组
            dots_a = VGroup(*[
                Circle(radius=0.22, fill_color=C_LEFT, fill_opacity=1, stroke_width=0
                       ).move_to(np.array([-3.5 + j*0.55, y, 0]))
                for j in range(a)
            ])
            dots_b = VGroup(*[
                Circle(radius=0.22, fill_color=C_RIGHT, fill_opacity=1, stroke_width=0
                       ).move_to(np.array([0.5 + j*0.55, y, 0]))
                for j in range(b)
            ])
            plus_s = MathTex(r"+", font_size=36, color=C_PLUS).move_to(
                np.array([-1.0, y, 0])
            )
            formula = MathTex(formula_str, font_size=40, color=WHITE)
            formula[0][0].set_color(C_LEFT)
            formula[0][1].set_color(C_PLUS)
            formula[0][2].set_color(C_RIGHT)
            formula[0][4].set_color(C_SUM)
            formula.move_to(np.array([2.8, y, 0]))

            row = VGroup(dots_a, plus_s, dots_b, formula)
            all_items.add(row)

            self.play(
                LaggedStart(*[GrowFromCenter(d) for d in [*dots_a, *dots_b]],
                            lag_ratio=0.1),
                FadeIn(plus_s),
                run_time=0.4,
            )
            self.play(Write(formula), run_time=0.35)
            self.play(Indicate(formula[0][4], color=C_SUM, scale_factor=1.3),
                      run_time=0.25)

        self.wait(0.8)
        self.play(FadeOut(sec_title), FadeOut(all_items), run_time=0.5)

    # ─────────────────────────────────────────
    # Scene 6: 术语：加数 + 加数 = 和
    # ─────────────────────────────────────────
    def scene_6_terms(self):
        sec_title = Text("记住这三个词！", font=FONT, font_size=40, color=C_ACTIVE)
        sec_title.move_to(UP * 6.0)
        self.play(Write(sec_title), run_time=0.4)

        # 公式行
        formula = MathTex(r"2 + 1 = 3", font_size=80, color=WHITE)
        formula[0][0].set_color(C_LEFT)
        formula[0][1].set_color(C_PLUS)
        formula[0][2].set_color(C_RIGHT)
        formula[0][4].set_color(C_SUM)
        formula.move_to(UP * 4.0)
        self.play(Write(formula), run_time=0.6)

        # 标注三个术语（Brace 向上，避免 270° 问题）
        # 加数1
        b1 = Brace(formula[0][0], direction=DOWN, color=C_LEFT)
        l1 = Text("加数", font=FONT, font_size=26, color=C_LEFT)
        l1.next_to(b1, DOWN, buff=0.1)
        self.play(GrowFromCenter(b1), FadeIn(l1), run_time=0.4)

        # 加号
        b2 = Brace(formula[0][1], direction=DOWN, color=C_PLUS)
        l2 = Text("加号", font=FONT, font_size=26, color=C_PLUS)
        l2.next_to(b2, DOWN, buff=0.1)
        self.play(GrowFromCenter(b2), FadeIn(l2), run_time=0.4)

        # 加数2
        b3 = Brace(formula[0][2], direction=DOWN, color=C_RIGHT)
        l3 = Text("加数", font=FONT, font_size=26, color=C_RIGHT)
        l3.next_to(b3, DOWN, buff=0.1)
        self.play(GrowFromCenter(b3), FadeIn(l3), run_time=0.4)

        # 和
        b4 = Brace(formula[0][4], direction=DOWN, color=C_SUM)
        l4 = Text("和", font=FONT, font_size=26, color=C_SUM)
        l4.next_to(b4, DOWN, buff=0.1)
        self.play(GrowFromCenter(b4), FadeIn(l4), run_time=0.4)

        self.wait(0.4)

        # 术语总结卡片
        card = RoundedRectangle(
            width=7.2, height=2.8, corner_radius=0.35,
            fill_color="#0f1b2e", fill_opacity=1,
            stroke_color=C_ACTIVE, stroke_width=3,
        ).move_to(DOWN * 1.5)

        summary = VGroup(
            VGroup(
                Text("加数", font=FONT, font_size=30, color=C_LEFT),
                Text(" + ", font=FONT, font_size=30, color=C_PLUS),
                Text("加数", font=FONT, font_size=30, color=C_RIGHT),
                Text(" = ", font=FONT, font_size=30, color=WHITE),
                Text("和", font=FONT, font_size=30, color=C_SUM),
            ).arrange(RIGHT, buff=0.05),
        ).move_to(card)

        self.play(Create(card), run_time=0.3)
        self.play(FadeIn(summary[0]), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(sec_title), FadeOut(formula),
            FadeOut(b1), FadeOut(l1), FadeOut(b2), FadeOut(l2),
            FadeOut(b3), FadeOut(l3), FadeOut(b4), FadeOut(l4),
            FadeOut(card), FadeOut(summary),
            run_time=0.5,
        )

    # ─────────────────────────────────────────
    # Scene 7: 片尾
    # ─────────────────────────────────────────
    def scene_7_outro(self):
        card = RoundedRectangle(
            width=7.5, height=4.0, corner_radius=0.4,
            fill_color="#0f1b2e", fill_opacity=1,
            stroke_color=C_PLUS, stroke_width=3,
        ).move_to(UP * 4.2)

        card_title = Text("加法的意义", font=FONT, font_size=32, color=C_PLUS)
        card_title.next_to(card, UP, buff=-0.55)

        lines = VGroup(
            VGroup(
                Text("把两部分", font=FONT, font_size=28, color=WHITE),
                Text("合并", font=FONT, font_size=28, color=C_PLUS),
                Text("起来", font=FONT, font_size=28, color=WHITE),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                Text("求", font=FONT, font_size=28, color=WHITE),
                Text("一共", font=FONT, font_size=28, color=C_SUM),
                Text("有多少", font=FONT, font_size=28, color=WHITE),
            ).arrange(RIGHT, buff=0.05),
            MathTex(r"2 + 1 = 3", font_size=56, color=WHITE),
        )
        lines[2][0][0].set_color(C_LEFT)
        lines[2][0][1].set_color(C_PLUS)
        lines[2][0][2].set_color(C_RIGHT)
        lines[2][0][4].set_color(C_SUM)
        lines.arrange(DOWN, buff=0.4).move_to(card)

        self.play(Create(card), FadeIn(card_title), run_time=0.4)
        for line in lines:
            self.play(FadeIn(line, shift=RIGHT * 0.3), run_time=0.35)
        self.wait(0.4)

        author_big = Text("上海初高中数学直通车",
                          font=FONT, font_size=34, color=WHITE).move_to(UP * 0.6)
        author_id  = Text("@emptyandcalm",
                          font=FONT, font_size=26, color=C_DIM).move_to(DOWN * 0.1)
        follow     = Text("关注我，学更多数学！",
                          font=FONT, font_size=28, color=C_PLUS).move_to(DOWN * 1.0)

        self.play(Transform(self.author_bar, author_big), run_time=0.5)
        self.play(FadeIn(author_id), FadeIn(follow, scale=1.1), run_time=0.5)

        # 气球装饰
        deco = VGroup(*[
            make_balloon(
                np.array([(i-2)*1.4, -2.8, 0]),
                0.28,
                BALLOON_COLORS[i % len(BALLOON_COLORS)],
            )
            for i in range(5)
        ])
        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in deco], lag_ratio=0.1),
            run_time=0.7,
        )
        self.wait(1.2)

        self.play(
            FadeOut(self.author_bar), FadeOut(author_id), FadeOut(follow),
            FadeOut(card), FadeOut(card_title), FadeOut(lines),
            FadeOut(deco),
            run_time=1.0,
        )


# ═══════════════════════════════════════════════════════
# manim -pql addition_intro.py AdditionIntro
# manim -qh  addition_intro.py AdditionIntro
# ═══════════════════════════════════════════════════════