"""
三年级下册 两位数乘两位数（竖式计算）教学动画
23 × 14 = 322

知识点：
- 竖式乘法的算理（乘法分配律）
- 先用个位乘，积末位与个位对齐
- 再用十位乘，积末位与十位对齐
- 最后两个积相加

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


class TwoDigitMultiplyLesson(Scene):
    """
    两位数乘两位数（竖式计算）教学动画场景

    场景顺序:
    1. 开场钩子 - 引出问题 23 × 14
    2. 算理拆分 - 14 = 10 + 4，分配律直观演示
    3. 竖式搭建 - 对齐数位
    4. 第一步：个位4乘23，积92
    5. 第二步：十位1乘23（实为10×23=230），积末位与十位对齐
    6. 第三步：两积相加得322
    7. 总结步骤 + 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # ===== 配色方案 =====
        self.C_HIGHLIGHT = "#f1c40f"   # 黄色高亮
        self.C_ONES = "#e74c3c"        # 红色 - 个位相关
        self.C_TENS = "#3498db"        # 蓝色 - 十位相关
        self.C_RESULT = "#2ecc71"      # 绿色 - 结果
        self.C_AUX = "#95a5a6"         # 辅助灰色
        self.C_WHITE = WHITE

        # 作者信息 (顶部，始终保留)
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)

        self.add(self.author_info)

        # 执行各场景
        self.scene_opening()
        self.scene_distributive_law()
        self.scene_build_vertical()
        self.scene_step1_ones()
        self.scene_step2_tens()
        self.scene_step3_add()
        self.scene_summary()

    # ─────────────────────────────────────────
    # 场景 1: 开场钩子
    # ─────────────────────────────────────────
    def scene_opening(self):
        """场景1: 开场钩子"""

        hook = Text(
            "两位数 × 两位数怎么算？",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.C_HIGHLIGHT
        ).move_to(UP * 5.5)

        problem_text = Text(
            "23 × 14 = ?",
            font="Noto Sans CJK SC",
            font_size=60,
            color=self.C_WHITE
        ).move_to(UP * 3.5)

        subtitle = Text(
            "竖式计算，步步拆解！",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_AUX
        ).move_to(UP * 2.2)

        self.play(Write(hook), run_time=0.8)
        self.wait(0.3)
        self.play(Write(problem_text), run_time=1.0)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(hook),
            FadeOut(subtitle),
            run_time=0.4
        )
        # problem_text 保留，稍微上移，变小
        problem_small = Text(
            "23 × 14 = ?",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.C_HIGHLIGHT
        ).move_to(UP * 6.2)
        self.play(Transform(problem_text, problem_small), run_time=0.5)
        self.problem_label = problem_text

    # ─────────────────────────────────────────
    # 场景 2: 算理 - 乘法分配律拆分
    # ─────────────────────────────────────────
    def scene_distributive_law(self):
        """场景2: 14拆成10+4，分配律直观演示"""

        title = Text(
            "先理解算理",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.C_HIGHLIGHT
        ).move_to(UP * 5.2)

        self.play(Write(title), run_time=0.6)

        # 14 = 10 + 4
        split_label = Text(
            "把 14 拆成 10 + 4",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_WHITE
        ).move_to(UP * 4.0)

        self.play(FadeIn(split_label, shift=UP * 0.2), run_time=0.7)
        self.wait(0.5)

        # 展示分配律
        # 23 × 14
        line1_a = Text("23 × 14", font="Noto Sans CJK SC", font_size=40, color=self.C_WHITE)
        line1_eq = Text("=", font="Noto Sans CJK SC", font_size=40, color=self.C_AUX)
        line1_b = Text("23 × (10 + 4)", font="Noto Sans CJK SC", font_size=40, color=self.C_WHITE)
        row1 = VGroup(line1_a, line1_eq, line1_b).arrange(RIGHT, buff=0.3).move_to(UP * 2.5)

        self.play(FadeIn(row1), run_time=0.8)
        self.wait(0.5)

        # = 23×10 + 23×4  (分开两行更清晰)
        row2_eq = Text("=", font="Noto Sans CJK SC", font_size=40, color=self.C_AUX)
        row2_tens = Text("23 × 10", font="Noto Sans CJK SC", font_size=40, color=self.C_TENS)
        row2_plus = Text("+", font="Noto Sans CJK SC", font_size=40, color=self.C_AUX)
        row2_ones = Text("23 × 4", font="Noto Sans CJK SC", font_size=40, color=self.C_ONES)
        row2 = VGroup(row2_eq, row2_tens, row2_plus, row2_ones).arrange(RIGHT, buff=0.3).move_to(UP * 1.3)

        self.play(FadeIn(row2), run_time=0.8)
        self.wait(0.5)

        # = 230 + 92
        row3_eq = Text("=", font="Noto Sans CJK SC", font_size=40, color=self.C_AUX)
        row3_a = Text("230", font="Noto Sans CJK SC", font_size=40, color=self.C_TENS)
        row3_plus = Text("+", font="Noto Sans CJK SC", font_size=40, color=self.C_AUX)
        row3_b = Text("92", font="Noto Sans CJK SC", font_size=40, color=self.C_ONES)
        row3 = VGroup(row3_eq, row3_a, row3_plus, row3_b).arrange(RIGHT, buff=0.3).move_to(UP * 0.1)

        self.play(Write(row3), run_time=0.8)
        self.wait(0.5)

        # = 322
        row4_eq = Text("=", font="Noto Sans CJK SC", font_size=44, color=self.C_AUX)
        row4_ans = Text("322", font="Noto Sans CJK SC", font_size=44, color=self.C_RESULT)
        row4 = VGroup(row4_eq, row4_ans).arrange(RIGHT, buff=0.3).move_to(DOWN * 1.0)

        self.play(Write(row4), run_time=0.7)
        self.play(Indicate(row4_ans, color=self.C_RESULT, scale_factor=1.2), run_time=0.8)
        self.wait(1.5)

        key_note = Text(
            "竖式帮我们把这个过程整理得更清晰！",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.C_HIGHLIGHT
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(key_note, shift=UP * 0.2), run_time=0.7)
        self.wait(1.5)

        # 清理本场景
        self.play(
            FadeOut(title),
            FadeOut(split_label),
            FadeOut(row1),
            FadeOut(row2),
            FadeOut(row3),
            FadeOut(row4),
            FadeOut(key_note),
            run_time=0.5
        )

    # ─────────────────────────────────────────
    # 内部辅助：构建竖式框架
    # ─────────────────────────────────────────
    def _build_vertical_skeleton(self, center=ORIGIN):
        """
        构建 23×14 竖式骨架，返回各部件。
        布局（相对于center）：
          数位列间距 col_gap，行间距 row_gap
          顶行 23，第二行 ×14，横线，第三行留空（个位积），第四行留空（十位积），
          双横线，第五行（总和）
        """
        cx, cy, cz = center[0], center[1], center[2] if len(center) > 2 else 0

        col_gap = 1.1   # 数位列间距
        row_gap = 1.0   # 行间距

        fs = 52         # 主要数字字号

        # 列中心 x 坐标（百位、十位、个位）
        # 个位在右，十位中间，百位在左
        x_ones   = cx + 1.0 * col_gap
        x_tens   = cx + 0.0 * col_gap
        x_hunds  = cx - 1.0 * col_gap

        # 行 y 坐标
        y_top    = cy + 2.5 * row_gap   # 被乘数 23
        y_mult   = cy + 1.5 * row_gap   # 乘数 ×14
        # 横线1 at y = cy + row_gap
        y_par1   = cy + 0.5 * row_gap   # 第一部分积（个位积）92
        y_par2   = cy - 0.5 * row_gap   # 第二部分积（十位积）230，末尾在十位
        # 横线2 at y = cy - row_gap
        y_sum    = cy - 1.5 * row_gap   # 总和 322

        def mk(s, color=WHITE, font_size=None):
            return Text(s, font="Noto Sans CJK SC",
                        font_size=font_size or fs,
                        color=color)

        # 被乘数 23
        d_2 = mk("2").move_to([x_tens,  y_top, 0])
        d_3 = mk("3").move_to([x_ones,  y_top, 0])

        # 乘号 ×
        mul_sign = mk("×", font_size=44).move_to([x_hunds - 0.4, y_mult, 0])

        # 乘数 14
        d_1 = mk("1").move_to([x_tens,  y_mult, 0])
        d_4 = mk("4").move_to([x_ones,  y_mult, 0])

        # 横线1（乘数下方）
        hr1 = Line(
            [x_hunds - 0.5, cy + row_gap, 0],
            [x_ones  + 0.5, cy + row_gap, 0],
            color=WHITE, stroke_width=3
        )

        # 横线2（两积之间下方）
        hr2 = Line(
            [x_hunds - 0.5, cy - row_gap, 0],
            [x_ones  + 0.8, cy - row_gap, 0],   # 稍宽一点，容纳3位数
            color=WHITE, stroke_width=3
        )

        # 存储坐标供后续场景使用
        self.vf = {
            "x_ones":  x_ones,
            "x_tens":  x_tens,
            "x_hunds": x_hunds,
            "y_top":   y_top,
            "y_mult":  y_mult,
            "y_par1":  y_par1,
            "y_par2":  y_par2,
            "y_sum":   y_sum,
            "col_gap": col_gap,
            "fs":      fs,
            "hr1":     hr1,
            "hr2":     hr2,
            "center":  center,
            # 被乘数
            "d_2": d_2, "d_3": d_3,
            # 乘数
            "mul_sign": mul_sign, "d_1": d_1, "d_4": d_4,
        }

    # ─────────────────────────────────────────
    # 场景 3: 搭建竖式
    # ─────────────────────────────────────────
    def scene_build_vertical(self):
        """场景3: 搭建竖式框架，强调数位对齐"""

        center = UP * 1.5
        self._build_vertical_skeleton(center)
        vf = self.vf

        title = Text(
            "用竖式来计算",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.C_HIGHLIGHT
        ).move_to(UP * 5.5)

        self.play(Write(title), run_time=0.5)

        # 数位标签
        x_ones, x_tens, x_hunds = vf["x_ones"], vf["x_tens"], vf["x_hunds"]
        y_top = vf["y_top"]
        label_y = y_top + 0.8

        lbl_ones  = Text("个位", font="Noto Sans CJK SC", font_size=20, color=self.C_AUX).move_to([x_ones,  label_y, 0])
        lbl_tens  = Text("十位", font="Noto Sans CJK SC", font_size=20, color=self.C_AUX).move_to([x_tens,  label_y, 0])
        lbl_hunds = Text("百位", font="Noto Sans CJK SC", font_size=20, color=self.C_AUX).move_to([x_hunds, label_y, 0])

        # 写被乘数 23
        self.play(Write(vf["d_2"]), Write(vf["d_3"]), run_time=0.8)
        self.play(FadeIn(lbl_ones), FadeIn(lbl_tens), FadeIn(lbl_hunds), run_time=0.5)

        # 写乘号和乘数 14
        self.play(Write(vf["mul_sign"]), run_time=0.4)
        self.play(Write(vf["d_1"]), Write(vf["d_4"]), run_time=0.8)

        # 横线
        self.play(Create(vf["hr1"]), run_time=0.5)

        # 强调对齐
        align_note = Text(
            "相同数位要对齐！",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.C_HIGHLIGHT
        ).move_to(DOWN * 1.5)

        # 画垂直辅助线标示对齐
        col_lines = VGroup(
            DashedLine([x_ones,  label_y + 0.3, 0], [x_ones,  vf["y_mult"] - 0.4, 0],
                       color=self.C_AUX, dash_length=0.12, stroke_width=1.5),
            DashedLine([x_tens,  label_y + 0.3, 0], [x_tens,  vf["y_mult"] - 0.4, 0],
                       color=self.C_AUX, dash_length=0.12, stroke_width=1.5),
        )

        self.play(FadeIn(align_note, shift=UP * 0.2), Create(col_lines), run_time=0.8)
        self.wait(1.5)

        # 清理辅助元素
        self.play(FadeOut(align_note), FadeOut(col_lines), run_time=0.4)

        # 保存全局竖式对象（供后续场景使用）
        self._vf_title = title
        self._vf_labels = VGroup(lbl_ones, lbl_tens, lbl_hunds)

    # ─────────────────────────────────────────
    # 场景 4: 第一步 - 个位4乘23
    # ─────────────────────────────────────────
    def scene_step1_ones(self):
        """场景4: 用个位4乘23，积为92，末位与个位对齐"""
        vf = self.vf

        # 更新标题
        step_title = Text(
            "第一步：个位 4 × 23",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_ONES
        ).move_to(UP * 5.2)
        self.play(Transform(self._vf_title, step_title), run_time=0.4)

        # 高亮个位 4 和被乘数
        self.play(
            Indicate(vf["d_4"], color=self.C_ONES, scale_factor=1.3),
            Indicate(vf["d_2"], color=self.C_ONES, scale_factor=1.2),
            Indicate(vf["d_3"], color=self.C_ONES, scale_factor=1.2),
            run_time=0.8
        )

        # 计算框
        calc_box_bg = RoundedRectangle(
            width=5.5, height=2.2,
            corner_radius=0.25,
            fill_color="#16213e",
            fill_opacity=0.95,
            stroke_color=self.C_ONES,
            stroke_width=2
        ).move_to(DOWN * 2.8)

        calc_line1 = Text(
            "4 × 3 = 12  →  个位写 2，进 1",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_WHITE
        ).move_to(DOWN * 2.4)

        calc_line2 = Text(
            "4 × 2 = 8，加进位 1，得 9",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_WHITE
        ).move_to(DOWN * 3.1)

        calc_line3 = Text(
            "所以 4 × 23 = 92",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.C_ONES
        ).move_to(DOWN * 3.8)

        self.play(FadeIn(calc_box_bg), run_time=0.3)
        self.play(Write(calc_line1), run_time=1.0)
        self.wait(0.8)
        self.play(Write(calc_line2), run_time=1.0)
        self.wait(0.8)
        self.play(Write(calc_line3), run_time=0.8)
        self.wait(1.0)

        # 写进位1（在23十位上方）
        carry1 = Text("1", font="Noto Sans CJK SC", font_size=22, color=self.C_ONES)
        carry1.move_to([vf["x_tens"], vf["y_top"] + 0.55, 0])
        self.play(FadeIn(carry1, scale=0.5), run_time=0.4)

        # 写积 92
        # 个位 2 对齐个位列，十位 9 对齐十位列
        p1_ones = Text("2", font="Noto Sans CJK SC",
                       font_size=vf["fs"], color=self.C_ONES)
        p1_ones.move_to([vf["x_ones"], vf["y_par1"], 0])

        p1_tens = Text("9", font="Noto Sans CJK SC",
                       font_size=vf["fs"], color=self.C_ONES)
        p1_tens.move_to([vf["x_tens"], vf["y_par1"], 0])

        self.play(FadeIn(p1_ones, shift=DOWN * 0.3), run_time=0.5)
        self.play(FadeIn(p1_tens, shift=DOWN * 0.3), run_time=0.5)

        # 强调个位对齐
        align_arr = Arrow(
            start=[vf["x_ones"], vf["y_par1"] - 0.5, 0],
            end=[vf["x_ones"],   vf["y_par1"] + 0.5, 0],
            color=self.C_ONES, buff=0.05,
            max_tip_length_to_length_ratio=0.3
        )
        align_text = Text(
            "末位与个位对齐",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.C_ONES
        ).next_to(align_arr, RIGHT, buff=0.15)

        self.play(GrowArrow(align_arr), FadeIn(align_text), run_time=0.8)
        self.wait(2.0)

        # 清理辅助
        self.play(
            FadeOut(calc_box_bg),
            FadeOut(calc_line1),
            FadeOut(calc_line2),
            FadeOut(calc_line3),
            FadeOut(align_arr),
            FadeOut(align_text),
            run_time=0.4
        )

        # 保存积元素
        self._carry1  = carry1
        self._p1_ones = p1_ones
        self._p1_tens = p1_tens

    # ─────────────────────────────────────────
    # 场景 5: 第二步 - 十位1乘23（实为10×23=230）
    # ─────────────────────────────────────────
    def scene_step2_tens(self):
        """场景5: 用十位1（代表10）乘23，积230，末位与十位对齐"""
        vf = self.vf

        # 更新标题
        step_title = Text(
            "第二步：十位 1 × 23",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_TENS
        ).move_to(UP * 5.2)
        self.play(Transform(self._vf_title, step_title), run_time=0.4)

        # 高亮十位 1
        self.play(
            Indicate(vf["d_1"], color=self.C_TENS, scale_factor=1.3),
            run_time=0.8
        )

        # 关键提示：十位的1代表10
        key_hint = Text(
            "十位的 1 其实代表 10 ！",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.C_HIGHLIGHT
        ).move_to(DOWN * 0.8)
        self.play(FadeIn(key_hint, shift=UP * 0.2), run_time=0.7)
        self.wait(1.0)

        # 计算框
        calc_box_bg = RoundedRectangle(
            width=5.8, height=2.2,
            corner_radius=0.25,
            fill_color="#16213e",
            fill_opacity=0.95,
            stroke_color=self.C_TENS,
            stroke_width=2
        ).move_to(DOWN * 2.8)

        calc_line1 = Text(
            "1 × 3 = 3",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.C_WHITE
        ).move_to(DOWN * 2.4)

        calc_line2 = Text(
            "1 × 2 = 2",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.C_WHITE
        ).move_to(DOWN * 3.0)

        calc_line3 = Text(
            "所以 10 × 23 = 230",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.C_TENS
        ).move_to(DOWN * 3.8)

        self.play(FadeIn(calc_box_bg), run_time=0.3)
        self.play(Write(calc_line1), run_time=0.8)
        self.wait(0.5)
        self.play(Write(calc_line2), run_time=0.8)
        self.wait(0.5)
        self.play(Write(calc_line3), run_time=0.8)
        self.wait(1.0)

        # 写第二部分积 230
        # 百位2，十位3，个位0 → 0写在十位列（末位与十位对齐），3在百位列，2在百位左边
        # 末位(0)与十位对齐
        p2_ones_zero = Text("0", font="Noto Sans CJK SC",
                            font_size=vf["fs"], color=self.C_TENS)
        p2_ones_zero.move_to([vf["x_tens"], vf["y_par2"], 0])   # 末尾0与十位列对齐

        p2_mid_3 = Text("3", font="Noto Sans CJK SC",
                        font_size=vf["fs"], color=self.C_TENS)
        p2_mid_3.move_to([vf["x_hunds"], vf["y_par2"], 0])

        p2_high_2 = Text("2", font="Noto Sans CJK SC",
                         font_size=vf["fs"], color=self.C_TENS)
        p2_high_2.move_to([vf["x_hunds"] - vf["col_gap"], vf["y_par2"], 0])

        self.play(FadeIn(p2_ones_zero, shift=DOWN * 0.3), run_time=0.4)
        self.play(FadeIn(p2_mid_3,    shift=DOWN * 0.3), run_time=0.4)
        self.play(FadeIn(p2_high_2,   shift=DOWN * 0.3), run_time=0.4)

        # 清理 key_hint 和计算框
        self.play(FadeOut(key_hint), run_time=0.3)

        # 重点说明：末位为什么要与十位对齐
        why_box = RoundedRectangle(
            width=6.2, height=1.4,
            corner_radius=0.2,
            fill_color="#1a1a4e",
            fill_opacity=0.95,
            stroke_color=self.C_HIGHLIGHT,
            stroke_width=2
        ).move_to(DOWN * 0.8)

        why_text = Text(
            "末位与十位对齐\n因为我们乘的是十位（代表10）！",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.C_HIGHLIGHT
        ).move_to(DOWN * 0.8)

        self.play(FadeIn(why_box), Write(why_text), run_time=0.8)

        # 箭头指向末位0与十位的对应关系
        arr_why = Arrow(
            start=[vf["x_tens"], vf["y_par2"] - 0.5, 0],
            end=[vf["x_tens"],   vf["y_mult"]  - 0.4, 0],
            color=self.C_TENS, buff=0.05,
            max_tip_length_to_length_ratio=0.25
        )
        self.play(GrowArrow(arr_why), run_time=0.8)
        self.wait(2.5)

        # 清理
        self.play(
            FadeOut(calc_box_bg),
            FadeOut(calc_line1),
            FadeOut(calc_line2),
            FadeOut(calc_line3),
            FadeOut(why_box),
            FadeOut(why_text),
            FadeOut(arr_why),
            run_time=0.4
        )

        # 保存积元素
        self._p2_zero = p2_ones_zero
        self._p2_3    = p2_mid_3
        self._p2_2    = p2_high_2

    # ─────────────────────────────────────────
    # 场景 6: 第三步 - 两积相加
    # ─────────────────────────────────────────
    def scene_step3_add(self):
        """场景6: 92 + 230 = 322"""
        vf = self.vf

        # 更新标题
        step_title = Text(
            "第三步：两积相加",
            font="Noto Sans CJK SC",
            font_size=28,
            color=self.C_RESULT
        ).move_to(UP * 5.2)
        self.play(Transform(self._vf_title, step_title), run_time=0.4)

        # 画横线2
        self.play(Create(vf["hr2"]), run_time=0.5)

        # 高亮两个积
        self.play(
            Indicate(self._p1_tens, color=self.C_ONES, scale_factor=1.2),
            Indicate(self._p1_ones, color=self.C_ONES, scale_factor=1.2),
            Indicate(self._p2_2,    color=self.C_TENS, scale_factor=1.2),
            Indicate(self._p2_3,    color=self.C_TENS, scale_factor=1.2),
            Indicate(self._p2_zero, color=self.C_TENS, scale_factor=1.2),
            run_time=1.0
        )

        # 计算框：92 + 230
        calc_box = RoundedRectangle(
            width=5.5, height=1.5,
            corner_radius=0.2,
            fill_color="#16213e",
            fill_opacity=0.95,
            stroke_color=self.C_RESULT,
            stroke_width=2
        ).move_to(DOWN * 0.3)

        calc_txt = Text(
            "92 + 230 = 322",
            font="Noto Sans CJK SC",
            font_size=32,
            color=self.C_WHITE
        ).move_to(DOWN * 0.3)

        self.play(FadeIn(calc_box), Write(calc_txt), run_time=0.8)
        self.wait(0.8)

        # 写最终结果 322
        x_ones, x_tens, x_hunds = vf["x_ones"], vf["x_tens"], vf["x_hunds"]
        y_sum = vf["y_sum"]

        r_2_ones = Text("2", font="Noto Sans CJK SC",
                        font_size=vf["fs"], color=self.C_RESULT)
        r_2_ones.move_to([x_ones, y_sum, 0])

        r_2_tens = Text("2", font="Noto Sans CJK SC",
                        font_size=vf["fs"], color=self.C_RESULT)
        r_2_tens.move_to([x_tens, y_sum, 0])

        r_3_hunds = Text("3", font="Noto Sans CJK SC",
                         font_size=vf["fs"], color=self.C_RESULT)
        r_3_hunds.move_to([x_hunds, y_sum, 0])

        self.play(
            FadeIn(r_2_ones,  shift=DOWN * 0.3),
            FadeIn(r_2_tens,  shift=DOWN * 0.3),
            FadeIn(r_3_hunds, shift=DOWN * 0.3),
            run_time=0.6
        )

        result_group = VGroup(r_3_hunds, r_2_tens, r_2_ones)
        self.play(
            Indicate(result_group, color=self.C_RESULT, scale_factor=1.15),
            run_time=0.8
        )
        self.wait(0.5)

        # 更新题目标签
        answer_label = Text(
            "23 × 14 = 322",
            font="Noto Sans CJK SC",
            font_size=36,
            color=self.C_RESULT
        ).move_to(UP * 6.2)
        self.play(Transform(self.problem_label, answer_label), run_time=0.6)
        self.play(Indicate(self.problem_label, color=self.C_RESULT, scale_factor=1.1), run_time=0.6)
        self.wait(2.0)

        self.play(FadeOut(calc_box), FadeOut(calc_txt), run_time=0.4)

        # 保存结果元素
        self._result_group = result_group

    # ─────────────────────────────────────────
    # 场景 7: 总结 + 片尾
    # ─────────────────────────────────────────
    def scene_summary(self):
        """场景7: 总结步骤 + 片尾"""
        vf = self.vf

        # 竖式整体淡出（保留问题标签）
        all_vertical = VGroup(
            vf["d_2"], vf["d_3"],
            vf["mul_sign"], vf["d_1"], vf["d_4"],
            vf["hr1"], vf["hr2"],
            self._carry1,
            self._p1_ones, self._p1_tens,
            self._p2_zero, self._p2_3, self._p2_2,
            self._result_group,
            self._vf_labels,
        )

        self.play(FadeOut(all_vertical), FadeOut(self._vf_title), run_time=0.6)

        # 步骤总结卡片
        summary_title = Text(
            "竖式乘法 · 四步法",
            font="Noto Sans CJK SC",
            font_size=34,
            color=self.C_HIGHLIGHT
        ).move_to(UP * 4.5)

        steps = VGroup(
            Text("① 相同数位对齐写好竖式", font="Noto Sans CJK SC",
                 font_size=26, color=self.C_WHITE),
            Text("② 个位乘整个被乘数", font="Noto Sans CJK SC",
                 font_size=26, color=self.C_ONES),
            Text("   积的末位与个位对齐", font="Noto Sans CJK SC",
                 font_size=22, color=self.C_ONES),
            Text("③ 十位乘整个被乘数", font="Noto Sans CJK SC",
                 font_size=26, color=self.C_TENS),
            Text("   积的末位与十位对齐", font="Noto Sans CJK SC",
                 font_size=22, color=self.C_TENS),
            Text("④ 两个积相加得最终结果", font="Noto Sans CJK SC",
                 font_size=26, color=self.C_RESULT),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(UP * 1.5)

        self.play(FadeIn(summary_title, shift=DOWN * 0.3), run_time=0.6)
        self.wait(0.2)

        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.3), run_time=0.45)
            self.wait(0.25)

        self.wait(1.5)

        # 例题回顾
        example_box = RoundedRectangle(
            width=6.0, height=1.0,
            corner_radius=0.2,
            fill_color="#16213e",
            fill_opacity=0.9,
            stroke_color=self.C_HIGHLIGHT,
            stroke_width=2
        ).move_to(DOWN * 3.2)

        example_text = Text(
            "23 × 14 = 92 + 230 = 322 ✓",
            font="Noto Sans CJK SC",
            font_size=26,
            color=self.C_RESULT
        ).move_to(DOWN * 3.2)

        self.play(FadeIn(example_box), Write(example_text), run_time=0.8)
        self.wait(1.5)

        # 片尾 - 作者信息放大
        self.play(
            FadeOut(summary_title),
            FadeOut(steps),
            FadeOut(example_box),
            FadeOut(example_text),
            FadeOut(self.problem_label),
            run_time=0.6
        )

        author_large = VGroup(
            Text("上海初高中数学直通车", font="Noto Sans CJK SC",
                 font_size=38, color=self.C_WHITE),
            Text("@emptyandcalm", font="Noto Sans CJK SC",
                 font_size=30, color=self.C_AUX)
        ).arrange(DOWN, buff=0.4).move_to(UP * 1.5)

        self.play(Transform(self.author_info, author_large), run_time=0.8)

        follow_text = Text(
            "关注我，获得更多数学技巧！",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.C_HIGHLIGHT
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow_text, shift=UP * 0.3), run_time=0.6)
        self.wait(2.0)

        self.play(
            FadeOut(self.author_info),
            FadeOut(follow_text),
            run_time=1.0
        )


# 运行命令:
# manim -qm 001_两位数乘两位数.py TwoDigitMultiplyLesson
