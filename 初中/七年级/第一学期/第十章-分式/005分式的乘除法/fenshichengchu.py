""" 
分式乘除法 - 七年级数学教学动画
TikTok竖屏格式 (1080×1920)

内容: 分式的乘法和除法运算
目标: 七年级第一学期学生
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
BG_COLOR = "#1a1a2e"
COLOR_NUMERATOR = "#4fc3f7"     # 浅蓝 - 分子
COLOR_DENOMINATOR = "#ef9a9a"   # 浅红 - 分母
COLOR_CANCEL = "#a5d6a7"        # 浅绿 - 约分高亮
COLOR_RESULT = GOLD             # 金色 - 结果
COLOR_TITLE = "#ce93d8"         # 浅紫 - 标题
COLOR_STEP = "#80cbc4"          # 绿松石 - 步骤说明
COLOR_KEY = YELLOW              # 黄色 - 关键词
FONT_CN = "Noto Sans CJK SC"    # 中文字体


class FenshiChengChu(Scene):
    """
    分式乘除法教学动画

    场景顺序:
    1. 开场钩子
    2. 乘法法则
    3. 乘法例题步骤
    4. 除法法则
    5. 除法例题步骤
    6. 总结
    7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR

        # 统一初始化
        self.setup_layout()

        # 执行场景
        self.scene_1_opening()
        self.scene_2_multiply_rule()
        self.scene_3_multiply_example()
        self.scene_4_divide_rule()
        self.scene_5_divide_example()
        self.scene_6_summary()
        self.scene_7_outro()

    # =========================================================
    # 布局初始化
    # =========================================================
    def setup_layout(self):
        """定义关键y坐标参考位置"""
        self.Y_AUTHOR = 7.2       # 作者栏
        self.Y_TITLE = 5.8        # 场景标题
        self.Y_STEP_LABEL = 5.0   # 步骤标签
        self.Y_FORMULA_1 = 3.8    # 公式第1行
        self.Y_FORMULA_2 = 2.5    # 公式第2行
        self.Y_FORMULA_3 = 1.2    # 公式第3行
        self.Y_FORMULA_4 = -0.1   # 公式第4行
        self.Y_EXPLAIN = -3.0     # 底部说明文字
        self.Y_CAPTION = -4.5     # 底部字幕

        # 创建持久化作者信息
        self.author_bar = self._make_author_bar()

    def _make_author_bar(self):
        author = Text(
            "上海初高中数学直通车  @emptyandcalm",
            font=FONT_CN,
            font_size=18,
            color=GRAY_B
        ).move_to(UP * self.Y_AUTHOR)
        return author

    # =========================================================
    # 辅助函数
    # =========================================================
    def cn(self, text, size=24, color=WHITE, **kwargs):
        """创建中文文字"""
        return Text(text, font=FONT_CN, font_size=size, color=color, **kwargs)

    def scene_title(self, text, color=COLOR_TITLE):
        """场景标题"""
        return self.cn(text, size=36, color=color).move_to(UP * self.Y_TITLE)

    def step_label(self, text, color=COLOR_STEP):
        """步骤说明标签"""
        label = self.cn(text, size=22, color=color)
        label.move_to(UP * self.Y_STEP_LABEL)
        return label

    def caption(self, text, color=GRAY_A):
        """底部说明"""
        return self.cn(text, size=20, color=color).move_to(UP * self.Y_CAPTION)

    def highlight_box(self, mobject, color=YELLOW, buff=0.15):
        """给公式加高亮框"""
        return SurroundingRectangle(mobject, color=color, buff=buff, corner_radius=0.1)

    # =========================================================
    # Scene 1: 开场钩子
    # =========================================================
    def scene_1_opening(self):
        """钩子场景：引出分式乘除法"""

        # 作者信息
        self.play(FadeIn(self.author_bar, shift=DOWN * 0.2), run_time=0.4)

        # 主标题
        main_title = self.cn("分式乘除法", size=52, color=COLOR_TITLE)
        main_title.move_to(UP * 5.5)

        # 挑战文字
        challenge = self.cn("化简下面这个式子，你会吗？", size=26, color=GRAY_A)
        challenge.move_to(UP * 4.5)

        self.play(Write(main_title), run_time=0.8)
        self.play(FadeIn(challenge, shift=UP * 0.3), run_time=0.4)

        # 钩子算式
        hook_formula = MathTex(
            r"\frac{x^2-4}{x+3} \times \frac{x^2+6x+9}{x+2}",
            font_size=40,
            color=WHITE
        ).move_to(UP * 3.0)

        hook_box = SurroundingRectangle(
            hook_formula, color=COLOR_TITLE, buff=0.3, corner_radius=0.15
        )

        self.play(Write(hook_formula), run_time=1.2)
        self.play(Create(hook_box), run_time=0.5)

        # 答案揭示提示
        hint = self.cn("= (x-2)(x+3)  这是怎么算出来的？", size=22, color=COLOR_KEY)
        hint.move_to(UP * 1.8)
        self.play(FadeIn(hint, shift=UP * 0.3), run_time=0.6)
        self.wait(0.8)

        # 清理，进入法则
        self.play(
            FadeOut(main_title),
            FadeOut(challenge),
            FadeOut(hook_formula),
            FadeOut(hook_box),
            FadeOut(hint),
            run_time=0.5
        )

    # =========================================================
    # Scene 2: 乘法法则
    # =========================================================
    def scene_2_multiply_rule(self):
        """展示分式乘法公式"""

        title = self.scene_title("✦ 分式乘法法则 ✦")
        self.play(Write(title), run_time=0.6)

        # 核心公式
        rule_label = self.cn("分子乘分子，分母乘分母", size=26, color=COLOR_KEY)
        rule_label.move_to(UP * 4.8)
        self.play(FadeIn(rule_label, shift=UP * 0.2), run_time=0.5)

        # 乘法公式
        mul_formula = MathTex(
            r"\frac{A}{B} \times \frac{C}{D} = \frac{A \cdot C}{B \cdot D}",
            font_size=46,
            color=WHITE
        ).move_to(UP * 3.0)

        self.play(Write(mul_formula), run_time=1.0)
        self.wait(0.5)

        # 分子箭头标注
        num_arrow = Arrow(
            start=mul_formula.get_top() + UP * 0.1,
            end=mul_formula.get_top() + UP * 0.8,
            color=COLOR_NUMERATOR,
            buff=0,
            max_stroke_width_to_length_ratio=4
        )
        
        # 分子标注
        num_label = self.cn("↑ 分子×分子 ↑", size=22, color=COLOR_NUMERATOR)
        num_label.next_to(mul_formula, UP, buff=0.25)
        
        self.play(
            Create(num_arrow),
            FadeIn(num_label, shift=DOWN * 0.2),
            run_time=0.7
        )

        # 分母箭头标注
        den_arrow = Arrow(
            start=mul_formula.get_bottom() + DOWN * 0.1,
            end=mul_formula.get_bottom() + DOWN * 0.8,
            color=COLOR_DENOMINATOR,
            buff=0,
            max_stroke_width_to_length_ratio=4
        )
        
        # 分母标注
        den_label = self.cn("↓ 分母×分母 ↓", size=22, color=COLOR_DENOMINATOR)
        den_label.next_to(mul_formula, DOWN, buff=0.25)
        
        self.play(
            Create(den_arrow),
            FadeIn(den_label),
            run_time=0.8
        )

        self.wait(1.0)

        # 步骤提示
        steps_box_content = VGroup(
            self.cn("①先因式分解", size=22, color=WHITE),
            self.cn("②再约分化简", size=22, color=COLOR_CANCEL),
            self.cn("③结果为最简分式", size=22, color=COLOR_RESULT),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        steps_bg = RoundedRectangle(
            width=5.5, height=steps_box_content.height + 0.6,
            corner_radius=0.2,
            fill_color="#1e2a4a",
            fill_opacity=0.9,
            stroke_color=COLOR_STEP,
            stroke_width=1.5
        )

        steps_group = VGroup(steps_bg, steps_box_content)
        steps_box_content.move_to(steps_bg.get_center())
        steps_group.move_to(UP * 0.5)

        self.play(FadeIn(steps_bg), Write(steps_box_content), run_time=0.8)
        self.wait(1.0)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(rule_label),
            FadeOut(mul_formula),
            FadeOut(num_arrow),
            FadeOut(num_label),
            FadeOut(den_arrow),
            FadeOut(den_label),
            FadeOut(steps_group),
            run_time=0.5
        )

    # =========================================================
    # Scene 3: 乘法例题
    # =========================================================
    def scene_3_multiply_example(self):
        """乘法例题步步解析"""

        title = self.scene_title("例题1：乘法")
        self.play(Write(title), run_time=0.5)

        # ---- 原式 ----
        lbl_original = self.cn("原式", size=22, color=COLOR_STEP)
        lbl_original.move_to(UP * 5.0)
        self.play(FadeIn(lbl_original), run_time=0.3)

        f_original = MathTex(
            r"\frac{x^2-4}{x+3} \times \frac{x^2+6x+9}{x+2}",
            font_size=38,
            color=WHITE
        ).move_to(UP * 4.0)

        self.play(Write(f_original), run_time=0.9)
        self.wait(0.4)

        # ---- 步骤1：因式分解 ----
        lbl_step1 = self.cn("第①步：因式分解", size=22, color=COLOR_STEP)
        lbl_step1.move_to(UP * 5.0)

        f_step1 = MathTex(
            r"= \frac{(x+2)(x-2)}{x+3} \times \frac{(x+3)^2}{x+2}",
            font_size=34,
            color=WHITE
        ).move_to(UP * 2.8)

        # 注释：x²-4 = (x+2)(x-2)
        note1 = self.cn("x²-4 = (x+2)(x-2)", size=18, color=COLOR_NUMERATOR)
        note2 = self.cn("x²+6x+9 = (x+3)²", size=18, color=COLOR_NUMERATOR)
        notes = VGroup(note1, note2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        notes.move_to(UP * 1.3)

        self.play(
            Transform(lbl_original, lbl_step1),
            run_time=0.3
        )
        self.play(Write(f_step1), run_time=0.9)
        self.play(FadeIn(notes, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        # ---- 步骤2：约分 ----
        lbl_step2 = self.cn("第②步：约分", size=22, color=COLOR_CANCEL)
        lbl_step2.move_to(UP * 5.0)

        # 显示完整展开后再约分
        f_expanded = MathTex(
            r"= \frac{(x+2)(x-2)(x+3)^2}{(x+3)(x+2)}",
            font_size=34,
            color=WHITE
        ).move_to(UP * 0.2)

        self.play(
            Transform(lbl_original, lbl_step2),
            FadeOut(notes),
            run_time=0.3
        )
        self.play(Write(f_expanded), run_time=0.8)
        self.wait(0.5)

        # 高亮可约分的因子
        # 用颜色标记 (x+2) 和 (x+3)
        f_cancel = MathTex(
            r"= \frac{(x+2)(x-2)(x+3)^2}{(x+3)(x+2)}",
            font_size=34,
            color=WHITE
        ).move_to(UP * 0.2)
        # Highlight the terms that cancel
        f_cancel.set_color_by_tex("(x+2)", COLOR_CANCEL)
        f_cancel.set_color_by_tex("(x+3)", COLOR_CANCEL)

        cancel_note = self.cn("消去公因式 (x+2) 和 (x+3)", size=20, color=COLOR_CANCEL)
        cancel_note.move_to(UP * -1.0)

        self.play(
            Transform(f_expanded, f_cancel),
            FadeIn(cancel_note),
            run_time=0.8
        )
        self.wait(0.8)

        # ---- 步骤3：结果 ----
        lbl_step3 = self.cn("第③步：结果", size=22, color=COLOR_RESULT)
        lbl_step3.move_to(UP * 5.0)

        f_result = MathTex(
            r"= (x-2)(x+3)",
            font_size=44,
            color=COLOR_RESULT
        ).move_to(UP * -2.2)

        result_box = self.highlight_box(f_result, color=GOLD, buff=0.2)

        self.play(
            Transform(lbl_original, lbl_step3),
            run_time=0.3
        )
        self.play(Write(f_result), run_time=0.6)
        self.play(Create(result_box), run_time=0.4)
        self.play(Flash(f_result, color=GOLD, flash_radius=1.5), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(lbl_original),
            FadeOut(f_original),
            FadeOut(f_step1),
            FadeOut(f_expanded),
            FadeOut(cancel_note),
            FadeOut(f_result),
            FadeOut(result_box),
            run_time=0.5
        )

    # =========================================================
    # Scene 4: 除法法则
    # =========================================================
    def scene_4_divide_rule(self):
        """除法转乘法的核心规则"""

        title = self.scene_title("✦ 分式除法法则 ✦")
        self.play(Write(title), run_time=0.6)

        # 核心要点
        key_text = self.cn("除以一个分式 = 乘以它的倒数！", size=26, color=COLOR_KEY)
        key_text.move_to(UP * 4.8)
        self.play(Write(key_text), run_time=0.7)

        # 除法公式 - 分两步展示
        div_lhs = MathTex(
            r"\frac{A}{B} \div \frac{C}{D}",
            font_size=46,
            color=WHITE
        ).move_to(UP * 3.2 + LEFT * 2.0)

        div_arrow = Arrow(
            start=div_lhs.get_right() + RIGHT * 0.2,
            end=div_lhs.get_right() + RIGHT * 1.8,
            color=COLOR_KEY,
            buff=0
        )
        div_arrow_label = self.cn("翻转", size=20, color=COLOR_KEY)
        div_arrow_label.next_to(div_arrow, UP, buff=0.1)

        div_rhs = MathTex(
            r"\frac{A}{B} \times \frac{D}{C}",
            font_size=46,
            color=WHITE
        ).move_to(UP * 3.2 + RIGHT * 2.0)

        self.play(Write(div_lhs), run_time=0.8)
        self.play(
            GrowArrow(div_arrow),
            FadeIn(div_arrow_label),
            run_time=0.5
        )
        self.play(Write(div_rhs), run_time=0.8)

        # 强调"翻转"
        flip_box = self.highlight_box(div_rhs, color=YELLOW)
        self.play(Create(flip_box), run_time=0.4)

        # 标注 C/D → D/C
        note_cd = MathTex(r"\frac{C}{D}", font_size=28, color=COLOR_DENOMINATOR)
        note_cd.move_to(UP * 2.0 + LEFT * 1.0)
        note_dc = MathTex(r"\longrightarrow \frac{D}{C}", font_size=28, color=COLOR_NUMERATOR)
        note_dc.next_to(note_cd, RIGHT, buff=0.3)
        flip_note = VGroup(note_cd, note_dc)

        flip_desc = self.cn("除数取倒数（分子分母互换）", size=20, color=GRAY_A)
        flip_desc.move_to(UP * 1.2)

        self.play(FadeIn(flip_note), FadeIn(flip_desc), run_time=0.5)

        # 完整公式
        full_rule = MathTex(
            r"\frac{A}{B} \div \frac{C}{D} = \frac{A}{B} \times \frac{D}{C} = \frac{AD}{BC}",
            font_size=36,
            color=WHITE
        ).move_to(UP * -0.5)

        rule_bg = SurroundingRectangle(
            full_rule, color=COLOR_KEY, buff=0.2, corner_radius=0.12
        )

        self.play(Write(full_rule), run_time=1.0)
        self.play(Create(rule_bg), run_time=0.4)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(key_text),
            FadeOut(div_lhs),
            FadeOut(div_arrow),
            FadeOut(div_arrow_label),
            FadeOut(div_rhs),
            FadeOut(flip_box),
            FadeOut(flip_note),
            FadeOut(flip_desc),
            FadeOut(full_rule),
            FadeOut(rule_bg),
            run_time=0.5
        )

    # =========================================================
    # Scene 5: 除法例题
    # =========================================================
    def scene_5_divide_example(self):
        """除法例题步步解析"""

        title = self.scene_title("例题2：除法")
        self.play(Write(title), run_time=0.5)

        # ---- 原式 ----
        lbl = self.cn("原式", size=22, color=COLOR_STEP)
        lbl.move_to(UP * 5.0)
        self.play(FadeIn(lbl), run_time=0.3)

        f_original = MathTex(
            r"\frac{a^2-1}{a^2} \div \frac{a+1}{a}",
            font_size=40,
            color=WHITE
        ).move_to(UP * 4.0)

        self.play(Write(f_original), run_time=0.8)
        self.wait(0.3)

        # ---- 步骤1：除法变乘法 ----
        lbl_s1 = self.cn("第①步：除法变乘法", size=22, color=COLOR_STEP)
        lbl_s1.move_to(UP * 5.0)

        f_step1 = MathTex(
            r"= \frac{a^2-1}{a^2} \times \frac{a}{a+1}",
            font_size=38,
            color=WHITE
        ).move_to(UP * 2.8)

        # 标注倒数
        flip_annotation = self.cn("倒数：a+1/a  →  a/a+1", size=19, color=COLOR_KEY)
        flip_annotation.move_to(UP * 1.9)

        self.play(Transform(lbl, lbl_s1), run_time=0.3)
        self.play(Write(f_step1), run_time=0.8)
        self.play(FadeIn(flip_annotation, shift=UP * 0.2), run_time=0.4)
        self.wait(0.6)

        # ---- 步骤2：因式分解 ----
        lbl_s2 = self.cn("第②步：因式分解", size=22, color=COLOR_STEP)
        lbl_s2.move_to(UP * 5.0)

        f_step2 = MathTex(
            r"= \frac{(a+1)(a-1)}{a^2} \times \frac{a}{a+1}",
            font_size=35,
            color=WHITE
        ).move_to(UP * 1.0)

        note_factor = self.cn("a²-1 = (a+1)(a-1)", size=18, color=COLOR_NUMERATOR)
        note_factor.move_to(UP * 0.0)

        self.play(
            Transform(lbl, lbl_s2),
            FadeOut(flip_annotation),
            run_time=0.3
        )
        self.play(Write(f_step2), run_time=0.8)
        self.play(FadeIn(note_factor, shift=UP * 0.2), run_time=0.4)
        self.wait(0.5)

        # ---- 步骤3：约分 ----
        lbl_s3 = self.cn("第③步：约分", size=22, color=COLOR_CANCEL)
        lbl_s3.move_to(UP * 5.0)

        # 展示完整连乘（a²=a·a）
        f_cancel = MathTex(
            r"= \frac{(a+1)(a-1)}{a \cdot a} \times \frac{a}{(a+1)}",
            font_size=33,
            color=WHITE
        ).move_to(UP * -1.2)
        # Highlight the terms that cancel
        f_cancel.set_color_by_tex("(a+1)", COLOR_CANCEL)
        f_cancel.set_color_by_tex("a", COLOR_CANCEL)

        cancel_hint = self.cn("消去公因式 (a+1) 和 a", size=20, color=COLOR_CANCEL)
        cancel_hint.move_to(UP * -2.3)

        self.play(
            Transform(lbl, lbl_s3),
            FadeOut(note_factor),
            run_time=0.3
        )
        self.play(Write(f_cancel), run_time=0.8)
        self.play(FadeIn(cancel_hint), run_time=0.4)
        self.wait(0.8)

        # ---- 步骤4：结果 ----
        lbl_s4 = self.cn("第④步：结果", size=22, color=COLOR_RESULT)
        lbl_s4.move_to(UP * 5.0)

        f_result = MathTex(
            r"= \frac{a-1}{a}",
            font_size=52,
            color=COLOR_RESULT
        ).move_to(UP * -3.8)

        result_box = self.highlight_box(f_result, color=GOLD, buff=0.25)

        self.play(
            Transform(lbl, lbl_s4),
            FadeOut(cancel_hint),
            run_time=0.3
        )
        self.play(Write(f_result), run_time=0.6)
        self.play(Create(result_box), run_time=0.4)
        self.play(Flash(f_result, color=GOLD, flash_radius=1.2), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(lbl),
            FadeOut(f_original),
            FadeOut(f_step1),
            FadeOut(f_step2),
            FadeOut(f_cancel),
            FadeOut(f_result),
            FadeOut(result_box),
            run_time=0.5
        )

    # =========================================================
    # Scene 6: 总结
    # =========================================================
    def scene_6_summary(self):
        """三步法总结"""

        title = self.scene_title("✦ 解题三步法 ✦", color=GOLD)
        self.play(Write(title), run_time=0.5)

        # 三步总结卡
        steps = [
            ("①", "因式分解", "分子分母分别分解", COLOR_NUMERATOR),
            ("②", "约分化简", "消去公因式", COLOR_CANCEL),
            ("③", "写出结果", "最简分式形式", COLOR_RESULT),
        ]

        step_groups = VGroup()
        for num, name, desc, color in steps:
            num_text = self.cn(num, size=30, color=color)
            name_text = self.cn(name, size=26, color=WHITE)
            desc_text = self.cn(desc, size=20, color=GRAY_A)
            row = VGroup(num_text, name_text, desc_text).arrange(RIGHT, buff=0.4)
            bg = RoundedRectangle(
                width=7.5, height=0.9,
                corner_radius=0.15,
                fill_color="#1e2a4a",
                fill_opacity=0.9,
                stroke_color=color,
                stroke_width=1.5
            )
            row.move_to(bg.get_center())
            step_groups.add(VGroup(bg, row))

        step_groups.arrange(DOWN, buff=0.35)
        step_groups.move_to(UP * 3.0)

        for sg in step_groups:
            self.play(FadeIn(sg, shift=RIGHT * 0.5), run_time=0.4)

        # 除法额外提示
        div_tip_bg = RoundedRectangle(
            width=7.5, height=1.1,
            corner_radius=0.15,
            fill_color="#2a1e3a",
            fill_opacity=0.9,
            stroke_color=COLOR_KEY,
            stroke_width=2
        ).move_to(UP * 0.5)

        div_tip = self.cn("除法：先取倒数变乘法，再按乘法三步做", size=21, color=COLOR_KEY)
        div_tip.move_to(div_tip_bg.get_center())

        self.play(FadeIn(div_tip_bg), Write(div_tip), run_time=0.6)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title),
            FadeOut(step_groups),
            FadeOut(div_tip_bg),
            FadeOut(div_tip),
            run_time=0.5
        )

    # =========================================================
    # Scene 7: 片尾
    # =========================================================
    def scene_7_outro(self):
        """片尾关注引导"""

        # 作者信息放大
        big_name = self.cn("上海初高中数学直通车", size=40, color=WHITE)
        big_name.move_to(UP * 2.0)

        big_id = self.cn("@emptyandcalm", size=30, color=GRAY_B)
        big_id.move_to(UP * 1.0)

        self.play(
            Transform(self.author_bar, big_name),
            run_time=0.6
        )
        self.play(FadeIn(big_id, shift=UP * 0.3), run_time=0.4)

        # 关注 CTA
        cta = self.cn("关注我，获得更多数学技巧！", size=28, color=COLOR_KEY)
        cta.move_to(UP * -0.2)
        self.play(FadeIn(cta, scale=1.05), run_time=0.5)

        # 数学符号装饰
        decorations = VGroup()
        symbols = [r"\frac{A}{B}", r"\times", r"\div", r"="]  # Removed \cancel{x}
        positions = [
            LEFT * 3.0 + DOWN * 1.8,
            LEFT * 1.5 + DOWN * 2.2,
            ORIGIN + DOWN * 1.8,
            RIGHT * 1.5 + DOWN * 2.2,
        ]
        colors = [COLOR_NUMERATOR, WHITE, COLOR_DENOMINATOR, GOLD]

        for sym, pos, col in zip(symbols, positions, colors):
            d = MathTex(sym, font_size=28, color=col).move_to(pos)
            decorations.add(d)

        self.play(
            *[FadeIn(d, scale=0.5) for d in decorations],
            run_time=0.7
        )
        self.wait(1.5)

        self.play(
            FadeOut(self.author_bar),
            FadeOut(big_id),
            FadeOut(cta),
            FadeOut(decorations),
            run_time=0.8
        )


# ========== 渲染命令 ==========
# 预览: manim -pql fenshichengchu.py FenshiChengChu
# 高质量: manim -qh fenshichengchu.py FenshiChengChu