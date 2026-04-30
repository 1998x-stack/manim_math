"""
总体与样本 - Population and Sample Statistics Animation
高三数学 第十八章 基本统计方法
TikTok竖屏 (1080×1920)
作者: 上海初高中数学直通车 @emptyandcalm
"""

from manim import *
import numpy as np

# ========== 全局配置 ==========
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

# ========== 颜色配置 ==========
BG_COLOR     = "#1a1a2e"
COLOR_POP    = "#e74c3c"   # 红 - 总体
COLOR_SAMPLE = "#3498db"   # 蓝 - 样本
COLOR_IND    = "#f39c12"   # 橙 - 个体
COLOR_ACCENT = "#2ecc71"   # 绿 - 强调
COLOR_GOLD   = GOLD
COLOR_GRAY   = GRAY_B
FONT         = "PingFang SC"


class PopulationSample(Scene):
    """
    场景顺序:
    1. 开场钩子
    2. 总体 & 个体定义
    3. 样本 & 抽样过程
    4. 样本容量
    5. 简单随机抽样
    6. 样本均值公式
    7. 核心思想
    8. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.setup_geometry()

        self.scene_1_opening()
        self.scene_2_population()
        self.scene_3_sampling()
        self.scene_4_sample_size()
        self.scene_5_random_sampling()
        self.scene_6_formula()
        self.scene_7_core_idea()
        self.scene_8_outro()

    # ----------------------------------------------------------
    # 几何数据初始化
    # ----------------------------------------------------------
    def setup_geometry(self):
        # 总体大圆
        self.POP_CENTER   = np.array([0.0, 2.0, 0.0])
        self.POP_RADIUS   = 2.5

        # 20个个体点 (均匀分布在圆内)
        self.N_IND = 20
        self.ind_positions = []
        rng = np.random.default_rng(42)
        for i in range(self.N_IND):
            angle = 2 * np.pi * i / self.N_IND + 0.1
            r = (0.4 + 0.55 * (i % 3) / 2.0) * (self.POP_RADIUS - 0.3)
            x = self.POP_CENTER[0] + r * np.cos(angle)
            y = self.POP_CENTER[1] + r * np.sin(angle)
            self.ind_positions.append(np.array([x, y, 0.0]))

        # 样本椭圆
        self.SAMPLE_CENTER = np.array([0.0, -3.5, 0.0])
        self.SAMPLE_W = 2.2
        self.SAMPLE_H = 1.3

        # 被抽中的6个样本索引
        self.sample_indices = [0, 3, 7, 11, 15, 18]

    # ----------------------------------------------------------
    # 辅助: 创建 Text
    # ----------------------------------------------------------
    def T(self, text, size=28, color=WHITE, **kwargs):
        return Text(text, font=FONT, font_size=size, color=color, **kwargs)

    # ----------------------------------------------------------
    # 场景 1: 开场钩子
    # ----------------------------------------------------------
    def scene_1_opening(self):
        # 作者标识
        self.author_bar = self.T("上海初高中数学直通车 @emptyandcalm",
                                  size=18, color=COLOR_GRAY).move_to(UP * 7.2)
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.3)

        # 钩子问题
        hook = self.T("全国有多少近视学生?", size=40, color=COLOR_GOLD)
        hook.move_to(UP * 5.5)

        sub = self.T("不可能全部调查!", size=28, color=COLOR_GRAY)
        sub.move_to(UP * 4.6)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.4)

        # 画一个代表"全国学生"的大圆
        pop_circle = Circle(radius=self.POP_RADIUS, color=COLOR_POP, stroke_width=3)
        pop_circle.move_to(self.POP_CENTER)

        # 圆内散点代表个体
        dots = VGroup(*[
            Dot(pos, radius=0.07, color=COLOR_IND, fill_opacity=0.8)
            for pos in self.ind_positions
        ])

        self.play(Create(pop_circle), run_time=0.8)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.3) for d in dots],
                        lag_ratio=0.05),
            run_time=1.0
        )

        # 问号文字在圆上
        q = self.T("?", size=80, color=COLOR_POP).move_to(self.POP_CENTER)
        self.play(FadeIn(q, scale=0.5), run_time=0.4)
        self.wait(0.5)

        self.play(
            FadeOut(hook), FadeOut(sub), FadeOut(q),
            FadeOut(pop_circle), FadeOut(dots),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # 场景 2: 总体 & 个体定义
    # ----------------------------------------------------------
    def scene_2_population(self):
        title = self.T("总体 与 个体", size=42, color=COLOR_GOLD)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 大圆 = 总体
        pop_circle = Circle(radius=self.POP_RADIUS, color=COLOR_POP,
                            stroke_width=3, fill_opacity=0.08, fill_color=COLOR_POP)
        pop_circle.move_to(self.POP_CENTER)

        pop_label = self.T("总体", size=32, color=COLOR_POP)
        pop_label.move_to(self.POP_CENTER + UP * (self.POP_RADIUS + 0.4))

        self.play(Create(pop_circle), FadeIn(pop_label), run_time=0.8)

        # 定义框
        def_pop = self.T("考察对象的全体", size=24, color=WHITE)
        def_pop.move_to(UP * 4.6)
        self.play(FadeIn(def_pop), run_time=0.4)
        self.wait(0.3)

        # 逐个显示个体点
        dots = VGroup()
        for i, pos in enumerate(self.ind_positions):
            d = Dot(pos, radius=0.10, color=COLOR_IND, fill_opacity=0.9)
            dots.add(d)

        self.play(
            LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.04),
            run_time=1.2
        )

        # 高亮一个个体并标注
        ind_dot = dots[5]
        self.play(ind_dot.animate.set_color(YELLOW).scale(2.0), run_time=0.4)

        ind_arrow = Arrow(
            self.ind_positions[5] + RIGHT * 0.3 + DOWN * 0.1,
            self.ind_positions[5] + RIGHT * 1.4 + DOWN * 0.4,
            buff=0,
            color=YELLOW,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.25
        )
        ind_label = self.T("个体", size=24, color=YELLOW)
        ind_label.next_to(ind_arrow.get_end(), RIGHT, buff=0.1)

        self.play(GrowArrow(ind_arrow), FadeIn(ind_label), run_time=0.5)

        def_ind = self.T("总体中每一个考察对象", size=22, color=YELLOW)
        def_ind.move_to(DOWN * 1.0)
        self.play(FadeIn(def_ind), run_time=0.4)

        self.wait(1.2)

        # 保存引用，清理文字但保留圆和点
        self.pop_circle = pop_circle
        self.pop_dots = dots
        self.pop_label_obj = pop_label

        self.play(
            FadeOut(title), FadeOut(def_pop),
            FadeOut(ind_arrow), FadeOut(ind_label),
            FadeOut(def_ind),
            run_time=0.5
        )
        # 恢复高亮点
        self.play(ind_dot.animate.set_color(COLOR_IND).scale(0.5), run_time=0.2)

    # ----------------------------------------------------------
    # 场景 3: 样本 & 抽样过程
    # ----------------------------------------------------------
    def scene_3_sampling(self):
        title = self.T("样本 与 抽样", size=42, color=COLOR_GOLD)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 样本椭圆
        sample_ellipse = Ellipse(
            width=self.SAMPLE_W * 2,
            height=self.SAMPLE_H * 2,
            color=COLOR_SAMPLE,
            stroke_width=3,
            fill_opacity=0.10,
            fill_color=COLOR_SAMPLE
        ).move_to(self.SAMPLE_CENTER)

        sample_label = self.T("样本", size=32, color=COLOR_SAMPLE)
        sample_label.move_to(self.SAMPLE_CENTER + UP * (self.SAMPLE_H + 0.35))

        self.play(Create(sample_ellipse), FadeIn(sample_label), run_time=0.8)

        def_sample = self.T("从总体中抽取的一部分个体", size=22, color=WHITE)
        def_sample.move_to(DOWN * 5.8)
        self.play(FadeIn(def_sample), run_time=0.4)

        # 箭头: 总体 → 样本 (弯曲)
        sample_arrow = CurvedArrow(
            self.POP_CENTER + DOWN * (self.POP_RADIUS + 0.1),
            self.SAMPLE_CENTER + UP * (self.SAMPLE_H + 0.1),
            angle=-TAU / 8,
            color=COLOR_ACCENT,
            stroke_width=3
        )
        arrow_label = self.T("抽样", size=24, color=COLOR_ACCENT)
        arrow_label.next_to(sample_arrow.get_center(), RIGHT, buff=0.15)

        self.play(Create(sample_arrow), FadeIn(arrow_label), run_time=0.8)

        # 逐个将被抽中的点"飞"到样本椭圆中
        sample_dots = VGroup()
        
        # 计算样本椭圆内的目标位置
        target_positions = []
        for k, idx in enumerate(self.sample_indices):
            angle_t = 2 * np.pi * k / len(self.sample_indices)
            r = 0.55
            tx = self.SAMPLE_CENTER[0] + r * self.SAMPLE_W * np.cos(angle_t)
            ty = self.SAMPLE_CENTER[1] + r * self.SAMPLE_H * np.sin(angle_t)
            target_positions.append(np.array([tx, ty, 0.0]))

        for k, idx in enumerate(self.sample_indices):
            src_dot = self.pop_dots[idx]
            # 创建副本点
            flying = Dot(src_dot.get_center(), radius=0.10,
                         color=COLOR_SAMPLE, fill_opacity=1.0)
            self.play(
                src_dot.animate.set_color(COLOR_SAMPLE),
                run_time=0.15
            )
            self.play(
                flying.animate.move_to(target_positions[k]).scale(0.9),
                run_time=0.35
            )
            sample_dots.add(flying)

        self.wait(0.8)

        # 保存引用
        self.sample_ellipse = sample_ellipse
        self.sample_label_obj = sample_label
        self.sample_dots = sample_dots
        self.sample_arrow = sample_arrow
        self.sample_arrow_label = arrow_label

        self.play(FadeOut(title), FadeOut(def_sample), run_time=0.4)

    # ----------------------------------------------------------
    # 场景 4: 样本容量
    # ----------------------------------------------------------
    def scene_4_sample_size(self):
        title = self.T("样本容量", size=42, color=COLOR_GOLD)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 在样本中逐个标号
        n = len(self.sample_indices)
        num_labels = VGroup()
        for i, dot in enumerate(self.sample_dots):
            lbl = self.T(str(i + 1), size=16, color=WHITE)
            lbl.next_to(dot, UP, buff=0.05)
            num_labels.add(lbl)

        self.play(
            LaggedStart(*[FadeIn(l) for l in num_labels], lag_ratio=0.1),
            run_time=0.8
        )

        # 大字显示 n = 6
        n_display = VGroup(
            self.T("样本容量 ", size=28, color=WHITE),
            MathTex(r"n = 6", font_size=48, color=COLOR_SAMPLE)
        ).arrange(RIGHT, buff=0.15).move_to(DOWN * 5.5)

        self.play(FadeIn(n_display), run_time=0.5)

        # 注释
        note = self.T("样本中个体的数目", size=22, color=COLOR_GRAY)
        note.move_to(DOWN * 6.4)
        self.play(FadeIn(note), run_time=0.3)

        self.wait(1.0)

        self.play(
            FadeOut(title), FadeOut(num_labels),
            FadeOut(n_display), FadeOut(note),
            run_time=0.4
        )

    # ----------------------------------------------------------
    # 场景 5: 简单随机抽样
    # ----------------------------------------------------------
    def scene_5_random_sampling(self):
        title = self.T("简单随机抽样", size=40, color=COLOR_GOLD)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)

        # 核心定义
        def1 = self.T("每个个体被抽到的概率相等", size=26, color=WHITE)
        def1.move_to(DOWN * 5.0)
        self.play(FadeIn(def1), run_time=0.5)

        # 高亮总体中所有点: 依次闪烁表示"等概率"
        for i in range(3):
            self.play(
                self.pop_dots.animate.set_color(YELLOW),
                run_time=0.3
            )
            self.play(
                self.pop_dots.animate.set_color(COLOR_IND),
                run_time=0.3
            )

        # 两种方法
        methods_bg = RoundedRectangle(
            width=7.5, height=2.2,
            corner_radius=0.2,
            fill_color="#16213e", fill_opacity=0.9,
            stroke_color=COLOR_ACCENT, stroke_width=1.5
        ).move_to(DOWN * 3.5)

        method1 = self.T("① 抽签法", size=26, color=COLOR_ACCENT)
        method1.move_to(DOWN * 3.1)

        method2 = self.T("② 随机数表法", size=26, color=COLOR_ACCENT)
        method2.move_to(DOWN * 4.1)

        self.play(FadeIn(methods_bg), run_time=0.3)
        self.play(Write(method1), run_time=0.5)
        self.play(Write(method2), run_time=0.5)

        self.wait(1.0)

        # 强调: 独立性 & 代表性
        rep_text = self.T("代表性 + 独立性 → 推断有效!", size=22, color=YELLOW)
        rep_text.move_to(DOWN * 5.6)
        self.play(FadeIn(rep_text, shift=UP * 0.2), run_time=0.5)

        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(def1),
            FadeOut(methods_bg), FadeOut(method1),
            FadeOut(method2), FadeOut(rep_text),
            run_time=0.4
        )

    # ----------------------------------------------------------
    # 场景 6: 样本均值公式
    # ----------------------------------------------------------
    def scene_6_formula(self):
        title = self.T("样本均值", size=42, color=COLOR_GOLD)
        title.move_to(UP * 6.2)
        self.play(Write(title), run_time=0.5)

        # 渐入数据示例
        data_label = self.T("样本数据:", size=24, color=WHITE)
        data_label.move_to(DOWN * 1.2)
        data_vals = MathTex(
            r"x_1,\ x_2,\ x_3,\ \ldots,\ x_n",
            font_size=38, color=COLOR_SAMPLE
        )
        data_vals.move_to(DOWN * 2.0)

        self.play(FadeIn(data_label), run_time=0.3)
        self.play(Write(data_vals), run_time=0.7)

        # 均值公式
        formula_label = self.T("样本均值公式:", size=24, color=WHITE)
        formula_label.move_to(DOWN * 3.2)

        formula = MathTex(
            r"\bar{x} = \frac{x_1 + x_2 + \cdots + x_n}{n}",
            font_size=44, color=COLOR_SAMPLE
        )
        formula.move_to(DOWN * 4.2)

        self.play(FadeIn(formula_label), run_time=0.3)
        self.play(Write(formula), run_time=1.0)

        # 强调分母 n
        try:
            n_part = formula.get_part_by_tex("n")
            n_rect = SurroundingRectangle(n_part, color=YELLOW, buff=0.05)
        except:
            # 如果获取特定部分失败，环绕整个公式
            n_rect = SurroundingRectangle(formula, color=YELLOW, buff=0.1)
        n_note = self.T("样本容量", size=20, color=YELLOW)
        n_note.next_to(n_rect, DOWN, buff=0.1)
        self.play(Create(n_rect), FadeIn(n_note), run_time=0.5)

        # 总体均值
        pop_formula_label = self.T("总体均值:", size=24, color=WHITE)
        pop_formula_label.move_to(DOWN * 5.4)
        pop_formula = MathTex(r"\mu = E(X)", font_size=38, color=COLOR_POP)
        pop_formula.move_to(DOWN * 6.2)

        self.play(FadeIn(pop_formula_label), run_time=0.3)
        self.play(Write(pop_formula), run_time=0.6)

        self.wait(1.2)

        self.play(
            FadeOut(title), FadeOut(data_label), FadeOut(data_vals),
            FadeOut(formula_label), FadeOut(formula),
            FadeOut(n_rect), FadeOut(n_note),
            FadeOut(pop_formula_label), FadeOut(pop_formula),
            run_time=0.5
        )

    # ----------------------------------------------------------
    # 场景 7: 核心思想
    # ----------------------------------------------------------
    def scene_7_core_idea(self):
        # 清理前面保留的元素
        self.play(
            FadeOut(self.pop_circle),
            FadeOut(self.pop_dots),
            FadeOut(self.pop_label_obj),
            FadeOut(self.sample_ellipse),
            FadeOut(self.sample_label_obj),
            FadeOut(self.sample_dots),
            FadeOut(self.sample_arrow),
            FadeOut(self.sample_arrow_label),
            run_time=0.6
        )

        title = self.T("统计学核心思想", size=40, color=COLOR_GOLD)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 流程图: 总体 → 抽样 → 样本 → 推断 → 总体
        pop_box = self.make_box("总体", COLOR_POP, UP * 3.0)
        sample_box = self.make_box("样本", COLOR_SAMPLE, UP * 0.5)
        conclusion_box = self.make_box("推断结论", COLOR_ACCENT, DOWN * 2.0)

        self.play(FadeIn(pop_box), run_time=0.4)
        self.play(FadeIn(sample_box), run_time=0.4)
        self.play(FadeIn(conclusion_box), run_time=0.4)

        # 向下箭头: 总体 → 抽样 → 样本
        arr1 = Arrow(pop_box.get_bottom(), sample_box.get_top(),
                     buff=0.1, color=COLOR_ACCENT, stroke_width=3)
        lbl1 = self.T("随机抽样", size=20, color=COLOR_ACCENT)
        lbl1.next_to(arr1, RIGHT, buff=0.15)

        arr2 = Arrow(sample_box.get_bottom(), conclusion_box.get_top(),
                     buff=0.1, color=COLOR_ACCENT, stroke_width=3)
        lbl2 = self.T("统计分析", size=20, color=COLOR_ACCENT)
        lbl2.next_to(arr2, RIGHT, buff=0.15)

        self.play(GrowArrow(arr1), FadeIn(lbl1), run_time=0.5)
        self.play(GrowArrow(arr2), FadeIn(lbl2), run_time=0.5)

        # 推断回总体的弧形箭头 (左侧)
        arr3 = CurvedArrow(
            conclusion_box.get_left() + LEFT * 0.1,
            pop_box.get_left() + LEFT * 0.1,
            angle=TAU / 5,
            color=YELLOW,
            stroke_width=2.5
        )
        lbl3 = self.T("推断总体", size=20, color=YELLOW)
        lbl3.next_to(arr3.get_center(), LEFT, buff=0.1)

        self.play(Create(arr3), FadeIn(lbl3), run_time=0.8)

        # 核心公式框
        core_text = self.T("用样本推断总体", size=34, color=YELLOW)
        core_text.move_to(DOWN * 4.5)
        underline = Underline(core_text, color=YELLOW)
        self.play(Write(core_text), Create(underline), run_time=0.7)

        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(pop_box), FadeOut(sample_box),
            FadeOut(conclusion_box), FadeOut(arr1), FadeOut(lbl1),
            FadeOut(arr2), FadeOut(lbl2), FadeOut(arr3), FadeOut(lbl3),
            FadeOut(core_text), FadeOut(underline),
            run_time=0.6
        )

    def make_box(self, text, color, position):
        rect = RoundedRectangle(
            width=3.8, height=0.9,
            corner_radius=0.2,
            fill_color=color, fill_opacity=0.15,
            stroke_color=color, stroke_width=2.5
        )
        label = self.T(text, size=28, color=color)
        group = VGroup(rect, label)
        label.move_to(rect.get_center())
        group.move_to(position)
        return group

    # ----------------------------------------------------------
    # 场景 8: 片尾
    # ----------------------------------------------------------
    def scene_8_outro(self):
        # 作者信息放大
        author_big = self.T("上海初高中数学直通车", size=40, color=WHITE)
        author_big.move_to(UP * 2.0)

        author_id = self.T("@emptyandcalm", size=30, color=COLOR_GRAY)
        author_id.move_to(UP * 1.0)

        self.play(
            Transform(self.author_bar, author_big),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)

        # 关注文字
        follow = self.T("关注我，获得更多数学技巧!", size=30, color=COLOR_GOLD)
        follow.move_to(DOWN * 0.2)
        self.play(FadeIn(follow, scale=1.1), run_time=0.6)

        # 总结卡片
        summary_items = [
            ("总体", "考察对象的全体", COLOR_POP),
            ("个体", "总体中的每个成员", COLOR_IND),
            ("样本", "从总体抽取的部分", COLOR_SAMPLE),
            ("样本容量", "样本中个体数目 n", COLOR_ACCENT),
        ]
        cards = VGroup()
        for i, (term, desc, col) in enumerate(summary_items):
            card_bg = RoundedRectangle(
                width=7.0, height=0.75,
                corner_radius=0.15,
                fill_color=col, fill_opacity=0.12,
                stroke_color=col, stroke_width=1.2
            )
            t1 = self.T(term, size=22, color=col)
            t2 = self.T(f" — {desc}", size=18, color=WHITE)
            row = VGroup(t1, t2).arrange(RIGHT, buff=0.1)
            row.move_to(card_bg.get_center())
            cards.add(VGroup(card_bg, row))

        cards.arrange(DOWN, buff=0.15)
        cards.move_to(DOWN * 3.5)

        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.2), run_time=0.25)

        self.wait(1.5)

        # 全部淡出
        self.play(
            FadeOut(self.author_bar),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(cards),
            run_time=1.0
        )

# # 快速预览 (480p)
# manim -pql population_sample_animation.py PopulationSample

# # 高质量 (1080p)
# manim -qh population_sample_animation.py PopulationSample