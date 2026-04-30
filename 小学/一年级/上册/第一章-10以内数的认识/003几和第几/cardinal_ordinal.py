"""
cardinal_ordinal.py  ──  几 和 第几
一年级上册数学教学动画

内容: 区分基数（几）和序数（第几）
目标: TikTok 竖屏 1080×1920，约55秒
作者: 上海初高中数学直通车  @emptyandcalm
"""

from manim import *
import numpy as np

# ════════════════════════════════════════════════════════
# 全局配置
# ════════════════════════════════════════════════════════
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_width  = 9
config.frame_height = 16

BG_COLOR        = "#1a1a2e"
COLOR_CARDINAL  = "#3498db"   # 蓝  → 基数
COLOR_ORDINAL   = "#e74c3c"   # 红  → 序数
COLOR_ACTIVE    = "#f1c40f"   # 黄  → 高亮
COLOR_PASSIVE   = "#374151"   # 暗灰 → 非关注
COLOR_ARROW     = "#2ecc71"   # 绿  → 方向箭头
COLOR_DIM       = "#888899"
FONT            = "PingFang SC"

# 队列参数（与 verify_geometry.py 一致）
Q5_N, Q5_SP, Q5_CX, Q5_CY, Q5_R = 5, 1.4, 0.0, 2.0, 0.40
Q6_N, Q6_SP, Q6_CX, Q6_CY, Q6_R = 6, 1.3, 0.0, 2.0, 0.38
CARD_W = 3.5


# ════════════════════════════════════════════════════════
# 工具函数
# ════════════════════════════════════════════════════════
def row_positions(n, spacing, cx, cy):
    return [
        np.array([cx + (i - (n - 1) / 2.0) * spacing, cy, 0.0])
        for i in range(n)
    ]


def make_person_circle(pos, radius, label_str, fill_color, label_color=WHITE):
    """创建一个带编号的小人圆圈"""
    circle = Circle(
        radius=radius,
        fill_color=fill_color,
        fill_opacity=1,
        stroke_color=WHITE,
        stroke_width=2,
    ).move_to(pos)
    label = Text(label_str, font=FONT, font_size=int(radius * 90), color=label_color)
    label.move_to(pos)
    return VGroup(circle, label)


def make_queue(n, spacing, cx, cy, radius,
               fill_color=None, label_color=WHITE):
    """生成一排 n 个带编号小圆圈"""
    positions = row_positions(n, spacing, cx, cy)
    queue = VGroup()
    colors_cycle = [
        "#3b82f6", "#ef4444", "#22c55e",
        "#f59e0b", "#8b5cf6", "#ec4899",
    ]
    for i, pos in enumerate(positions):
        col = fill_color if fill_color else colors_cycle[i % len(colors_cycle)]
        person = make_person_circle(pos, radius, str(i + 1), col, label_color)
        queue.add(person)
    return queue


# ════════════════════════════════════════════════════════
# 主场景
# ════════════════════════════════════════════════════════
class CardinalOrdinal(Scene):

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 作者条（全程固定顶部）
        self.author_bar = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT, font_size=18, color=COLOR_DIM,
        ).move_to(UP * 7.3)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        self.scene_1_hook()
        self.scene_2_cardinal()
        self.scene_3_ordinal()
        self.scene_4_contrast()
        self.scene_5_race()
        self.scene_6_practice()
        self.scene_7_outro()

    # ──────────────────────────────────────────────────
    # Scene 1: 开场钩子
    # ──────────────────────────────────────────────────
    def scene_1_hook(self):
        hook = Text("你分得清吗？", font=FONT, font_size=52, color=COLOR_ACTIVE)
        hook.move_to(UP * 5.5)
        self.play(Write(hook), run_time=0.7)

        # 两个对比词
        card_a = Text("5个苹果", font=FONT, font_size=38, color=COLOR_CARDINAL)
        card_b = Text("第5个苹果", font=FONT, font_size=38, color=COLOR_ORDINAL)
        VGroup(card_a, card_b).arrange(DOWN, buff=0.8).move_to(UP * 3.5)

        self.play(FadeIn(card_a, shift=LEFT * 0.4), run_time=0.5)
        self.play(FadeIn(card_b, shift=RIGHT * 0.4), run_time=0.5)

        # 双向闪烁对比
        for _ in range(2):
            self.play(
                card_a.animate.scale(1.15).set_color(COLOR_ACTIVE),
                card_b.animate.scale(0.88),
                run_time=0.25,
            )
            self.play(
                card_a.animate.scale(1 / 1.15).set_color(COLOR_CARDINAL),
                card_b.animate.scale(1 / 0.88).set_color(COLOR_ACTIVE),
                run_time=0.25,
            )
            self.play(
                card_b.animate.set_color(COLOR_ORDINAL),
                run_time=0.15,
            )

        # 今天学
        today = Text("今天学：几  和  第几", font=FONT, font_size=34, color=WHITE)
        today.move_to(UP * 1.2)
        sep_l = Text("几", font=FONT, font_size=34, color=COLOR_CARDINAL)
        sep_r = Text("第几", font=FONT, font_size=34, color=COLOR_ORDINAL)
        # 直接用颜色替换重新构建
        today_group = VGroup(
            Text("今天学：", font=FONT, font_size=34, color=WHITE),
            sep_l,
            Text("  和  ", font=FONT, font_size=34, color=WHITE),
            sep_r,
        ).arrange(RIGHT, buff=0.0).move_to(UP * 1.2)

        self.play(FadeIn(today_group, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(hook), FadeOut(card_a), FadeOut(card_b),
            FadeOut(today_group),
            run_time=0.5,
        )

    # ──────────────────────────────────────────────────
    # Scene 2: 认识基数（几）
    # ──────────────────────────────────────────────────
    def scene_2_cardinal(self):
        # ── 标题
        title = Text("基数：几", font=FONT, font_size=44, color=COLOR_CARDINAL)
        title.move_to(UP * 6.0)
        sub = Text("表示有多少个", font=FONT, font_size=26, color=COLOR_DIM)
        sub.move_to(UP * 5.2)
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.3)

        # ── 5个苹果
        apple_pos = row_positions(Q5_N, Q5_SP, Q5_CX, Q5_CY)
        apple_colors = ["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#3498db"]
        apples = VGroup()
        for i, (pos, col) in enumerate(zip(apple_pos, apple_colors)):
            apple = Circle(
                radius=Q5_R,
                fill_color=col, fill_opacity=1,
                stroke_color=WHITE, stroke_width=2,
            ).move_to(pos)
            lbl = Text("🍎", font=FONT, font_size=28).move_to(pos)
            apples.add(VGroup(apple, lbl))

        # 苹果依次弹出
        for apple in apples:
            self.play(GrowFromCenter(apple), run_time=0.22)

        self.wait(0.3)

        # ── 大括号括住全部
        brace = Brace(apples, direction=DOWN, color=COLOR_CARDINAL)
        brace_lbl = Text("一共有几个？", font=FONT, font_size=28, color=COLOR_CARDINAL)
        brace_lbl.next_to(brace, DOWN, buff=0.2)
        self.play(GrowFromCenter(brace), FadeIn(brace_lbl), run_time=0.6)
        self.wait(0.4)

        # ── 逐个高亮计数
        count_labels = VGroup()
        for i, apple in enumerate(apples):
            num_lbl = Text(str(i + 1), font=FONT, font_size=22, color=COLOR_ACTIVE)
            num_lbl.next_to(apple, UP, buff=0.15)
            self.play(
                apple[0].animate.set_stroke(color=COLOR_ACTIVE, width=4),
                FadeIn(num_lbl, scale=1.2),
                run_time=0.22,
            )
            count_labels.add(num_lbl)

        # ── 答案
        answer = Text("5  个！", font=FONT, font_size=52, color=COLOR_CARDINAL)
        answer.move_to(DOWN * 1.5)
        self.play(FadeIn(answer, scale=1.2), run_time=0.5)
        self.wait(0.4)

        # ── 小结
        summary = VGroup(
            Text("基数", font=FONT, font_size=32, color=COLOR_CARDINAL),
            Text(" = 总数量", font=FONT, font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.0).move_to(DOWN * 3.0)
        self.play(Write(summary), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(apples), FadeOut(brace), FadeOut(brace_lbl),
            FadeOut(count_labels), FadeOut(answer), FadeOut(summary),
            run_time=0.5,
        )

    # ──────────────────────────────────────────────────
    # Scene 3: 认识序数（第几）
    # ──────────────────────────────────────────────────
    def scene_3_ordinal(self):
        title = Text("序数：第几", font=FONT, font_size=44, color=COLOR_ORDINAL)
        title.move_to(UP * 6.0)
        sub = Text("表示排在第几位", font=FONT, font_size=26, color=COLOR_DIM)
        sub.move_to(UP * 5.2)
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.3)

        # ── 5个小人队列（统一灰色，待高亮）
        positions = row_positions(Q5_N, Q5_SP, Q5_CX, Q5_CY)
        queue = make_queue(Q5_N, Q5_SP, Q5_CX, Q5_CY, Q5_R, fill_color=COLOR_PASSIVE)
        for person in queue:
            self.play(GrowFromCenter(person), run_time=0.20)

        # ── 从左数 箭头
        arrow_start = np.array([-4.0, Q5_CY - 0.9, 0])
        arrow_end   = np.array([ 4.0, Q5_CY - 0.9, 0])
        dir_arrow = Arrow(
            arrow_start, arrow_end,
            color=COLOR_ARROW, stroke_width=4,
            max_tip_length_to_length_ratio=0.05,
        )
        dir_label = Text("从左数 →", font=FONT, font_size=24, color=COLOR_ARROW)
        dir_label.next_to(dir_arrow, DOWN, buff=0.15)
        self.play(GrowArrow(dir_arrow), FadeIn(dir_label), run_time=0.5)
        self.wait(0.2)

        # ── 逐个扫描高亮（第1→第3）
        ordinal_labels = VGroup()
        for i in range(3):
            pos = positions[i]
            # 高亮当前圆
            circle = queue[i][0]
            self.play(
                circle.animate.set_fill(COLOR_ORDINAL).set_stroke(color=COLOR_ACTIVE, width=5),
                run_time=0.3,
            )
            lbl = Text(f"第{i+1}", font=FONT, font_size=22, color=COLOR_ACTIVE)
            lbl.next_to(queue[i], UP, buff=0.15)
            self.play(FadeIn(lbl, scale=1.2), run_time=0.2)
            ordinal_labels.add(lbl)
            if i < 2:
                self.wait(0.1)

        self.wait(0.3)

        # ── 第3个放大聚焦
        target = queue[2]
        spotlight = Circle(
            radius=Q5_R * 1.5,
            color=COLOR_ACTIVE, stroke_width=4, fill_opacity=0,
        ).move_to(positions[2])
        self.play(Create(spotlight), run_time=0.4)
        self.play(target.animate.scale(1.25), run_time=0.3)

        announce = Text("他排在第 3 位！", font=FONT, font_size=34, color=COLOR_ORDINAL)
        announce.move_to(DOWN * 1.5)
        self.play(Write(announce), run_time=0.6)
        self.wait(0.6)

        # ── 小结
        summary = VGroup(
            Text("序数", font=FONT, font_size=32, color=COLOR_ORDINAL),
            Text(" = 位置顺序", font=FONT, font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.0).move_to(DOWN * 3.0)
        self.play(Write(summary), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(queue), FadeOut(dir_arrow), FadeOut(dir_label),
            FadeOut(ordinal_labels), FadeOut(spotlight),
            FadeOut(announce), FadeOut(summary),
            run_time=0.5,
        )

    # ──────────────────────────────────────────────────
    # Scene 4: 基数 vs 序数 对比
    # ──────────────────────────────────────────────────
    def scene_4_contrast(self):
        # 中间同一排队列（稍小，居中）
        q_scale = 0.9
        r_small = Q5_R * q_scale
        sp_small = Q5_SP * q_scale
        positions = row_positions(Q5_N, sp_small, 0.0, 1.5)

        queue = VGroup()
        base_colors = ["#3b82f6", "#ef4444", "#22c55e", "#f59e0b", "#8b5cf6"]
        for i, pos in enumerate(positions):
            p = make_person_circle(pos, r_small, str(i + 1),
                                   base_colors[i])
            queue.add(p)

        title = Text("一起来比一比！", font=FONT, font_size=40, color=COLOR_ACTIVE)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        for p in queue:
            self.play(GrowFromCenter(p), run_time=0.18)

        self.wait(0.3)

        # ── 左侧：基数卡片
        card_left_bg = RoundedRectangle(
            width=3.5, height=5.5,
            corner_radius=0.3,
            fill_color="#0d2137", fill_opacity=1,
            stroke_color=COLOR_CARDINAL, stroke_width=3,
        ).move_to(np.array([-2.1, -2.2, 0]))

        lbl_cardinal = Text("几个？", font=FONT, font_size=30, color=COLOR_CARDINAL)
        lbl_cardinal.move_to(card_left_bg.get_top() + DOWN * 0.5)

        # 全部高亮括号
        mini_apples = VGroup()
        mini_pos = row_positions(5, 0.5, -2.1, -2.5)
        for i, pos in enumerate(mini_pos):
            c = Circle(radius=0.2, fill_color=base_colors[i],
                       fill_opacity=1, stroke_width=0).move_to(pos)
            mini_apples.add(c)

        mini_brace = Brace(mini_apples, direction=DOWN,
                           color=COLOR_CARDINAL, buff=0.1)
        mini_ans = Text("5个", font=FONT, font_size=30, color=COLOR_CARDINAL)
        mini_ans.next_to(mini_brace, DOWN, buff=0.15)

        # ── 右侧：序数卡片
        card_right_bg = RoundedRectangle(
            width=3.5, height=5.5,
            corner_radius=0.3,
            fill_color="#1f0d0d", fill_opacity=1,
            stroke_color=COLOR_ORDINAL, stroke_width=3,
        ).move_to(np.array([2.1, -2.2, 0]))

        lbl_ordinal = Text("第几个？", font=FONT, font_size=30, color=COLOR_ORDINAL)
        lbl_ordinal.move_to(card_right_bg.get_top() + DOWN * 0.5)

        # 第3个高亮
        mini_pos_r = row_positions(5, 0.5, 2.1, -2.5)
        mini_people = VGroup()
        for i, pos in enumerate(mini_pos_r):
            col = COLOR_ORDINAL if i == 2 else COLOR_PASSIVE
            c = Circle(radius=0.2, fill_color=col,
                       fill_opacity=1, stroke_width=0).move_to(pos)
            mini_people.add(c)

        mini_arrow = Arrow(
            mini_pos_r[2] + UP * 0.4,
            mini_pos_r[2] + UP * 0.15,
            color=COLOR_ACTIVE, stroke_width=3,
            max_tip_length_to_length_ratio=0.5,
        )
        mini_ans_r = Text("第3个", font=FONT, font_size=30, color=COLOR_ORDINAL)
        mini_ans_r.next_to(card_right_bg, DOWN, buff=0.15)

        # 动画：卡片从两侧滑入
        card_left_group = VGroup(card_left_bg, lbl_cardinal, mini_apples,
                                  mini_brace, mini_ans)
        card_right_group = VGroup(card_right_bg, lbl_ordinal, mini_people,
                                   mini_arrow, mini_ans_r)

        card_left_group.shift(LEFT * 6)
        card_right_group.shift(RIGHT * 6)

        self.play(
            card_left_group.animate.shift(RIGHT * 6),
            card_right_group.animate.shift(LEFT * 6),
            run_time=0.7,
        )

        # 闪烁对比
        self.play(
            Indicate(card_left_bg, scale_factor=1.05, color=COLOR_CARDINAL),
            run_time=0.5,
        )
        self.play(
            Indicate(card_right_bg, scale_factor=1.05, color=COLOR_ORDINAL),
            run_time=0.5,
        )
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(queue),
            FadeOut(card_left_group), FadeOut(card_right_group),
            run_time=0.5,
        )

    # ──────────────────────────────────────────────────
    # Scene 5: 比赛名次
    # ──────────────────────────────────────────────────
    def scene_5_race(self):
        title = Text("比赛名次", font=FONT, font_size=44, color=COLOR_ACTIVE)
        title.move_to(UP * 6.0)
        sub = Text("序数的生活应用", font=FONT, font_size=26, color=COLOR_DIM)
        sub.move_to(UP * 5.2)
        self.play(Write(title), FadeIn(sub), run_time=0.5)

        # 三个奖台圆形
        trophy_pos = row_positions(3, 2.2, 0.0, 2.5)
        trophy_cols = ["#f1c40f", "#c0c0c0", "#cd7f32"]  # 金银铜
        trophy_labels = ["第1名", "第2名", "第3名"]
        trophies = VGroup()

        for pos, col, lbl_str in zip(trophy_pos, trophy_cols, trophy_labels):
            circle = Circle(
                radius=0.55, fill_color=col, fill_opacity=1,
                stroke_color=WHITE, stroke_width=3,
            ).move_to(pos)
            star = Text("★", font=FONT, font_size=30, color=WHITE).move_to(pos)
            name = Text(lbl_str, font=FONT, font_size=24, color=col)
            name.next_to(circle, DOWN, buff=0.2)
            trophies.add(VGroup(circle, star, name))

        self.play(
            LaggedStart(*[GrowFromCenter(t) for t in trophies], lag_ratio=0.25),
            run_time=0.9,
        )

        # 第1名闪光
        self.play(
            Flash(trophies[0][0], color=COLOR_ACTIVE, flash_radius=0.9),
            run_time=0.5,
        )
        cheer = Text("第1名最棒！🏆", font=FONT, font_size=32, color=COLOR_ACTIVE)
        cheer.move_to(DOWN * 0.3)
        self.play(FadeIn(cheer, scale=1.15), run_time=0.4)
        self.wait(0.5)

        # 引出基数问题
        q = Text("他们共有几名选手？", font=FONT, font_size=30, color=WHITE)
        q.move_to(DOWN * 1.5)
        self.play(FadeIn(q), run_time=0.4)
        self.wait(0.5)

        brace = Brace(trophies, direction=DOWN, color=COLOR_CARDINAL)
        a = Text("共  3  名（基数）", font=FONT, font_size=30, color=COLOR_CARDINAL)
        a.next_to(brace, DOWN, buff=0.2)
        self.play(GrowFromCenter(brace), Write(a), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(sub),
            FadeOut(trophies), FadeOut(cheer),
            FadeOut(q), FadeOut(brace), FadeOut(a),
            run_time=0.5,
        )

    # ──────────────────────────────────────────────────
    # Scene 6: 互动练习
    # ──────────────────────────────────────────────────
    def scene_6_practice(self):
        title = Text("一起来练习！", font=FONT, font_size=44, color=COLOR_ACTIVE)
        title.move_to(UP * 6.0)
        self.play(Write(title), run_time=0.5)

        # 6只小动物
        animal_emojis = ["🐶", "🐱", "🐭", "🐰", "🦊", "🐻"]
        # 直接用彩色圆代替，避免emoji字体问题
        animal_colors = [
            "#e67e22", "#e74c3c", "#95a5a6",
            "#f1c40f", "#e67e22", "#8b4513",
        ]
        positions = row_positions(Q6_N, Q6_SP, Q6_CX, Q6_CY)
        animals = VGroup()
        for i, (pos, col) in enumerate(zip(positions, animal_colors)):
            circle = Circle(
                radius=Q6_R, fill_color=col, fill_opacity=1,
                stroke_color=WHITE, stroke_width=2,
            ).move_to(pos)
            num_lbl = Text(str(i + 1), font=FONT, font_size=22, color=WHITE)
            num_lbl.move_to(pos)
            animals.add(VGroup(circle, num_lbl))

        # 动物特殊标记（第4个=小猫，用特殊颜色）
        animals[3][0].set_fill(color="#e74c3c")
        cat_mark = Text("猫", font=FONT, font_size=18, color=WHITE)
        cat_mark.move_to(positions[3])
        animals[3][1].become(cat_mark)

        for a in animals:
            self.play(GrowFromCenter(a), run_time=0.18)
        self.wait(0.3)

        # ── 问题1：基数
        q1 = VGroup(
            Text("问：一共有", font=FONT, font_size=30, color=WHITE),
            Text("几只", font=FONT, font_size=30, color=COLOR_CARDINAL),
            Text("动物？", font=FONT, font_size=30, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 1.2)
        self.play(FadeIn(q1), run_time=0.4)

        # 全体高亮
        for a in animals:
            self.play(a[0].animate.set_stroke(color=COLOR_CARDINAL, width=5),
                      run_time=0.08)

        brace1 = Brace(animals, direction=DOWN, color=COLOR_CARDINAL)
        a1 = Text("6 只（基数）", font=FONT, font_size=30, color=COLOR_CARDINAL)
        a1.next_to(brace1, DOWN, buff=0.2)
        self.play(GrowFromCenter(brace1), Write(a1), run_time=0.6)
        self.wait(0.8)
        self.play(FadeOut(q1), FadeOut(brace1), FadeOut(a1), run_time=0.3)

        # 恢复描边
        for a in animals:
            self.play(a[0].animate.set_stroke(color=WHITE, width=2), run_time=0.05)

        # ── 问题2：序数
        q2 = VGroup(
            Text("问：小猫排在", font=FONT, font_size=30, color=WHITE),
            Text("第几位", font=FONT, font_size=30, color=COLOR_ORDINAL),
            Text("？", font=FONT, font_size=30, color=WHITE),
        ).arrange(RIGHT, buff=0.05).move_to(DOWN * 1.2)
        self.play(FadeIn(q2), run_time=0.4)

        # 聚焦第4个
        spotlight = Circle(
            radius=Q6_R * 1.6, color=COLOR_ORDINAL,
            stroke_width=5, fill_opacity=0,
        ).move_to(positions[3])
        self.play(Create(spotlight), run_time=0.4)
        self.play(animals[3].animate.scale(1.2), run_time=0.3)

        arrow = Arrow(
            positions[3] + UP * 1.0,
            positions[3] + UP * 0.5,
            color=COLOR_ORDINAL, stroke_width=5,
            max_tip_length_to_length_ratio=0.35,
        )
        self.play(GrowArrow(arrow), run_time=0.3)

        a2 = Text("第 4 位（序数）", font=FONT, font_size=30, color=COLOR_ORDINAL)
        a2.move_to(DOWN * 2.5)
        self.play(Write(a2), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(animals),
            FadeOut(q2), FadeOut(spotlight),
            FadeOut(arrow), FadeOut(a2),
            run_time=0.5,
        )

    # ──────────────────────────────────────────────────
    # Scene 7: 口诀总结 + 片尾
    # ──────────────────────────────────────────────────
    def scene_7_outro(self):
        # 口诀卡片
        card_bg = RoundedRectangle(
            width=7.5, height=3.8,
            corner_radius=0.4,
            fill_color="#0f1b2e", fill_opacity=1,
            stroke_color=COLOR_ACTIVE, stroke_width=3,
        ).move_to(UP * 3.5)

        line1 = VGroup(
            Text("几", font=FONT, font_size=36, color=COLOR_CARDINAL),
            Text(" →  有多少个（总数）", font=FONT, font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.0)

        line2 = VGroup(
            Text("第几", font=FONT, font_size=36, color=COLOR_ORDINAL),
            Text(" →  在哪里（位置）", font=FONT, font_size=32, color=WHITE),
        ).arrange(RIGHT, buff=0.0)

        VGroup(line1, line2).arrange(DOWN, buff=0.5).move_to(card_bg)

        self.play(Create(card_bg), run_time=0.5)
        self.play(Write(line1), run_time=0.6)
        self.play(Write(line2), run_time=0.6)
        self.wait(0.5)

        # 作者名放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=38, color=WHITE,
        ).move_to(UP * 1.0)
        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=COLOR_DIM,
        ).move_to(UP * 0.2)

        self.play(
            Transform(self.author_bar, author_big),
            run_time=0.6,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.4)

        follow = Text(
            "关注我，学更多数学！",
            font=FONT, font_size=30, color=COLOR_ACTIVE,
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(follow, scale=1.1), run_time=0.5)

        # 彩色数字装饰环
        deco = VGroup()
        ring_y = -3.2
        for i, col in enumerate([COLOR_CARDINAL, COLOR_ORDINAL, COLOR_ACTIVE,
                                   COLOR_ARROW, "#8b5cf6"]):
            x = (i - 2) * 1.5
            t = Text(f"第{i+1}", font=FONT, font_size=30, color=col)
            t.move_to(np.array([x, ring_y, 0]))
            deco.add(t)

        self.play(
            LaggedStart(*[FadeIn(d, scale=0.8) for d in deco], lag_ratio=0.1),
            run_time=0.7,
        )
        self.wait(1.0)

        self.play(
            FadeOut(self.author_bar),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(card_bg),
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(deco),
            run_time=1.0,
        )


# ════════════════════════════════════════════════════════
# 渲染命令:
#   快速预览: manim -pql cardinal_ordinal.py CardinalOrdinal
#   高清输出: manim -qh  cardinal_ordinal.py CardinalOrdinal
# ════════════════════════════════════════════════════════