"""
三位数除以一位数 - 三年级上册第四章
知识点：480÷4=120，竖式除法，商末尾有0
目标观众：小学三年级学生
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


class ThreeDigitDivideOneLesson(Scene):
    """
    三位数除以一位数教学动画

    场景顺序：
    1. 开场钩子 - 引出问题 480÷4=?
    2. 回顾两位数除法 - 迁移思路
    3. 竖式书写 - 搭建框架
    4. 百位计算 4÷4=1
    5. 十位计算 8÷4=2
    6. 个位计算 0÷4=0 (重点：商末尾0)
    7. 总结验证
    8. 片尾
    """

    def construct(self):
        self.camera.background_color = "#1a1a2e"

        # 配色
        self.C_TITLE = "#ffd700"       # 金色 - 标题
        self.C_STEP = "#4fc3f7"        # 蓝色 - 步骤标题
        self.C_HIGHLIGHT = "#ff6b6b"   # 红色 - 高亮
        self.C_GREEN = "#69db7c"       # 绿色 - 正确答案
        self.C_ORANGE = "#ffa94d"      # 橙色 - 强调
        self.C_GRAY = "#b0b3b8"        # 灰色 - 说明文字
        self.C_WHITE = WHITE
        self.C_YELLOW = YELLOW

        # 执行动画
        self.scene_1_opening()
        self.scene_2_review()
        self.scene_3_setup_division()
        self.scene_4_hundreds()
        self.scene_5_tens()
        self.scene_6_ones()
        self.scene_7_summary()
        self.scene_8_outro()

    # ─────────────────────────────────────────
    # 场景1：开场钩子
    # ─────────────────────────────────────────
    def scene_1_opening(self):
        # 作者品牌（顶部）
        author = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="PingFang SC",
            font_size=18,
            color="#6b7280"
        ).move_to(UP * 7.0)
        self.play(FadeIn(author, shift=DOWN * 0.2), run_time=0.4)
        self.author = author

        # 钩子标题
        hook_line1 = Text(
            "你会算吗？",
            font="PingFang SC",
            font_size=52,
            color=self.C_TITLE
        ).move_to(UP * 5.5)

        self.play(Write(hook_line1), run_time=0.7)

        # 主问题
        question = MathTex(
            r"480 \div 4 = \, ?",
            font_size=90,
            color=self.C_WHITE
        ).move_to(UP * 3.8)
        self.play(Write(question), run_time=1.0)
        self.wait(0.5)

        # 副标题
        sub = Text(
            "三位数除以一位数",
            font="PingFang SC",
            font_size=34,
            color=self.C_STEP
        ).move_to(UP * 2.6)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.5)
        self.wait(0.8)

        # 特别提示：商末尾有0
        tip_bg = RoundedRectangle(
            width=7.0, height=1.2,
            corner_radius=0.3,
            color="#2d3561",
            fill_color="#2d3561",
            fill_opacity=0.9,
            stroke_width=2
        ).move_to(UP * 1.2)
        tip_text = Text(
            "注意：商末尾有0！",
            font="PingFang SC",
            font_size=30,
            color=self.C_ORANGE
        ).move_to(UP * 1.2)
        self.play(FadeIn(tip_bg), Write(tip_text), run_time=0.7)
        self.wait(1.0)

        # 清理，保留 author
        self.play(
            FadeOut(hook_line1),
            FadeOut(question),
            FadeOut(sub),
            FadeOut(tip_bg),
            FadeOut(tip_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────
    # 场景2：回顾两位数除法，迁移思路
    # ─────────────────────────────────────────
    def scene_2_review(self):
        title = Text(
            "先回顾：两位数除以一位数",
            font="PingFang SC",
            font_size=30,
            color=self.C_STEP
        ).move_to(UP * 6.0)
        self.play(Write(title), run_time=0.6)

        # 展示 84÷4=21 竖式作为对比
        review_label = Text(
            "例：84 ÷ 4 = 21",
            font="PingFang SC",
            font_size=36,
            color=self.C_WHITE
        ).move_to(UP * 4.8)
        self.play(Write(review_label), run_time=0.7)

        # 步骤
        step_tens = Text(
            "十位：8 ÷ 4 = 2",
            font="PingFang SC",
            font_size=28,
            color=self.C_GREEN
        ).move_to(UP * 3.5)
        step_ones = Text(
            "个位：4 ÷ 4 = 1",
            font="PingFang SC",
            font_size=28,
            color=self.C_GREEN
        ).move_to(UP * 2.8)
        self.play(FadeIn(step_tens, shift=RIGHT * 0.3), run_time=0.5)
        self.play(FadeIn(step_ones, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(0.5)

        # 过渡提示
        arrow_text = Text(
            "同样的方法，用于三位数！",
            font="PingFang SC",
            font_size=26,
            color=self.C_ORANGE
        ).move_to(UP * 1.8)
        self.play(FadeIn(arrow_text, shift=UP * 0.2), run_time=0.5)
        self.wait(0.8)

        self.play(
            FadeOut(title),
            FadeOut(review_label),
            FadeOut(step_tens),
            FadeOut(step_ones),
            FadeOut(arrow_text),
            run_time=0.5
        )

    # ─────────────────────────────────────────
    # 辅助：构建竖式元素
    # ─────────────────────────────────────────
    def build_division_frame(self, center_y=1.5):
        """
        创建 480÷4 的竖式框架（不含商）
        竖式布局：
                ┌──────────
           4  ) 4   8   0
        """
        cx = 0.0
        cy = center_y

        # 被除数各位数字
        d0 = MathTex(r"4", font_size=64, color=self.C_WHITE).move_to([cx - 1.1, cy, 0])
        d1 = MathTex(r"8", font_size=64, color=self.C_WHITE).move_to([cx + 0.1, cy, 0])
        d2 = MathTex(r"0", font_size=64, color=self.C_WHITE).move_to([cx + 1.2, cy, 0])

        # 除数
        divisor = MathTex(r"4", font_size=64, color=self.C_WHITE).move_to([cx - 2.5, cy, 0])

        # 竖线（除数右侧向下）
        v_line = Line(
            start=[cx - 1.85, cy + 0.7, 0],
            end=[cx - 1.85, cy - 0.55, 0],
            color=self.C_WHITE,
            stroke_width=3
        )
        # 横线（被除数顶部）
        h_line = Line(
            start=[cx - 1.85, cy + 0.7, 0],
            end=[cx + 1.8, cy + 0.7, 0],
            color=self.C_WHITE,
            stroke_width=3
        )

        return {
            "divisor": divisor,
            "d0": d0, "d1": d1, "d2": d2,
            "v_line": v_line,
            "h_line": h_line,
            "cx": cx, "cy": cy
        }

    # ─────────────────────────────────────────
    # 场景3：搭建竖式框架
    # ─────────────────────────────────────────
    def scene_3_setup_division(self):
        title = Text(
            "用竖式来计算 480 ÷ 4",
            font="PingFang SC",
            font_size=32,
            color=self.C_TITLE
        ).move_to(UP * 6.2)
        self.play(Write(title), run_time=0.6)
        self.div_title = title

        # 说明文字
        explain = Text(
            "从最高位（百位）开始，一位一位地除",
            font="PingFang SC",
            font_size=24,
            color=self.C_GRAY
        ).move_to(UP * 5.3)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(explain), run_time=0.3)

        # 构建竖式
        frame = self.build_division_frame(center_y=1.5)
        self.frame = frame

        # 显示除数
        self.play(Write(frame["divisor"]), run_time=0.4)
        # 显示竖线和横线
        self.play(
            Create(frame["v_line"]),
            Create(frame["h_line"]),
            run_time=0.5
        )
        # 显示被除数
        self.play(
            Write(frame["d0"]),
            Write(frame["d1"]),
            Write(frame["d2"]),
            run_time=0.7
        )
        self.wait(0.5)

        # 商位置提示
        quot_hint = Text(
            "商写在横线上方",
            font="PingFang SC",
            font_size=22,
            color=self.C_GRAY
        ).move_to(UP * 3.0)
        self.play(FadeIn(quot_hint), run_time=0.4)
        self.wait(0.5)
        self.play(FadeOut(quot_hint), run_time=0.3)

    # ─────────────────────────────────────────
    # 场景4：百位 4÷4=1
    # ─────────────────────────────────────────
    def scene_4_hundreds(self):
        frame = self.frame
        cx, cy = frame["cx"], frame["cy"]

        # 步骤标题
        step_title = Text(
            "第一步：算百位",
            font="PingFang SC",
            font_size=32,
            color=self.C_STEP
        ).move_to(UP * 5.2)
        self.play(Write(step_title), run_time=0.5)

        # 高亮百位数字
        highlight_rect = SurroundingRectangle(
            frame["d0"], color=self.C_YELLOW, buff=0.12, stroke_width=3
        )
        self.play(Create(highlight_rect), run_time=0.4)

        # 问题文字
        q_label = Text(
            "百位：",
            font="PingFang SC",
            font_size=30,
            color=self.C_WHITE
        )
        q_formula = MathTex(r"4 \div 4 = 1", font_size=46, color=self.C_GREEN)
        question_grp = VGroup(q_label, q_formula).arrange(RIGHT, buff=0.15)
        question_grp.move_to(UP * 4.1)
        self.play(Write(q_label), run_time=0.4)
        self.play(Write(q_formula), run_time=0.6)
        self.wait(0.4)

        # 商 "1" 写在横线上方
        quot_1 = MathTex(r"1", font_size=64, color=self.C_GREEN).move_to(
            [frame["d0"].get_x(), cy + 1.15, 0]
        )
        self.play(Write(quot_1), run_time=0.5)
        self.quot_1 = quot_1

        # 减法说明
        sub_explain = Text(
            "4 - 4 = 0，余0，继续看下一位",
            font="PingFang SC",
            font_size=24,
            color=self.C_GRAY
        ).move_to(UP * 3.0)
        self.play(FadeIn(sub_explain, shift=UP * 0.2), run_time=0.5)
        self.wait(0.7)

        self.play(FadeOut(sub_explain), run_time=0.3)
        self.play(
            FadeOut(highlight_rect),
            FadeOut(question_grp),
            FadeOut(step_title),
            run_time=0.4
        )

    # ─────────────────────────────────────────
    # 场景5：十位 8÷4=2
    # ─────────────────────────────────────────
    def scene_5_tens(self):
        frame = self.frame
        cx, cy = frame["cx"], frame["cy"]

        step_title = Text(
            "第二步：算十位",
            font="PingFang SC",
            font_size=32,
            color=self.C_STEP
        ).move_to(UP * 5.2)
        self.play(Write(step_title), run_time=0.5)

        # 高亮十位数字
        highlight_rect = SurroundingRectangle(
            frame["d1"], color=self.C_YELLOW, buff=0.12, stroke_width=3
        )
        self.play(Create(highlight_rect), run_time=0.4)

        q_label = Text(
            "十位：",
            font="PingFang SC",
            font_size=30,
            color=self.C_WHITE
        )
        q_formula = MathTex(r"8 \div 4 = 2", font_size=46, color=self.C_GREEN)
        question_grp = VGroup(q_label, q_formula).arrange(RIGHT, buff=0.15)
        question_grp.move_to(UP * 4.1)
        self.play(Write(q_label), run_time=0.4)
        self.play(Write(q_formula), run_time=0.6)
        self.wait(0.4)

        # 商 "2" 写上
        quot_2 = MathTex(r"2", font_size=64, color=self.C_GREEN).move_to(
            [frame["d1"].get_x(), cy + 1.15, 0]
        )
        self.play(Write(quot_2), run_time=0.5)
        self.quot_2 = quot_2

        sub_explain = Text(
            "8 - 8 = 0，余0，继续看下一位",
            font="PingFang SC",
            font_size=24,
            color=self.C_GRAY
        ).move_to(UP * 3.0)
        self.play(FadeIn(sub_explain, shift=UP * 0.2), run_time=0.5)
        self.wait(0.7)

        self.play(FadeOut(sub_explain), run_time=0.3)
        self.play(
            FadeOut(highlight_rect),
            FadeOut(question_grp),
            FadeOut(step_title),
            run_time=0.4
        )

    # ─────────────────────────────────────────
    # 场景6：个位 0÷4=0（重点！商末尾有0）
    # ─────────────────────────────────────────
    def scene_6_ones(self):
        frame = self.frame
        cx, cy = frame["cx"], frame["cy"]

        step_title = Text(
            "第三步：算个位（重点！）",
            font="PingFang SC",
            font_size=32,
            color=self.C_HIGHLIGHT
        ).move_to(UP * 5.2)
        self.play(Write(step_title), run_time=0.5)

        # 高亮个位数字 "0"
        highlight_rect = SurroundingRectangle(
            frame["d2"], color=self.C_HIGHLIGHT, buff=0.12, stroke_width=3
        )
        self.play(
            Create(highlight_rect),
            Indicate(frame["d2"], color=self.C_HIGHLIGHT),
            run_time=0.6
        )

        q_label = Text(
            "个位：",
            font="PingFang SC",
            font_size=30,
            color=self.C_WHITE
        )
        q_formula = MathTex(r"0 \div 4 = 0", font_size=46, color=self.C_ORANGE)
        question_grp = VGroup(q_label, q_formula).arrange(RIGHT, buff=0.15)
        question_grp.move_to(UP * 4.1)
        self.play(Write(q_label), run_time=0.4)
        self.play(Write(q_formula), run_time=0.6)
        self.wait(0.4)

        # 强调：0除以任何数等于0
        emphasis_bg = RoundedRectangle(
            width=7.2, height=1.3,
            corner_radius=0.25,
            color=self.C_HIGHLIGHT,
            fill_color="#3d1a1a",
            fill_opacity=0.85,
            stroke_width=2.5
        ).move_to(UP * 3.1)
        emphasis_text = Text(
            "0 除以任何数都等于 0！",
            font="PingFang SC",
            font_size=28,
            color=self.C_ORANGE
        ).move_to(UP * 3.1)
        self.play(FadeIn(emphasis_bg), Write(emphasis_text), run_time=0.7)
        self.wait(0.4)

        # 重要警告：商末尾不能省略
        warn_bg = RoundedRectangle(
            width=7.4, height=1.6,
            corner_radius=0.25,
            color=self.C_YELLOW,
            fill_color="#3d3500",
            fill_opacity=0.85,
            stroke_width=2.5
        ).move_to(UP * 1.9)
        warn_text1 = Text(
            "商末尾的 0 不能省略！",
            font="PingFang SC",
            font_size=28,
            color=self.C_YELLOW
        ).move_to(UP * 2.05)
        warn_text2 = Text(
            "120  不等于  12",
            font="PingFang SC",
            font_size=26,
            color=self.C_HIGHLIGHT
        ).move_to(UP * 1.65)
        self.play(FadeIn(warn_bg), Write(warn_text1), run_time=0.6)
        self.play(Write(warn_text2), run_time=0.5)
        self.wait(1.0)

        # 商 "0" 写上
        quot_0 = MathTex(r"0", font_size=64, color=self.C_ORANGE).move_to(
            [frame["d2"].get_x(), cy + 1.15, 0]
        )
        self.play(
            Indicate(frame["d2"], color=self.C_ORANGE, scale_factor=1.3),
            run_time=0.4
        )
        self.play(Write(quot_0), run_time=0.5)
        self.play(Flash(quot_0, color=self.C_ORANGE, flash_radius=0.5), run_time=0.5)
        self.quot_0 = quot_0
        self.wait(0.8)

        self.play(
            FadeOut(highlight_rect),
            FadeOut(question_grp),
            FadeOut(step_title),
            FadeOut(emphasis_bg),
            FadeOut(emphasis_text),
            FadeOut(warn_bg),
            FadeOut(warn_text1),
            FadeOut(warn_text2),
            run_time=0.5
        )

    # ─────────────────────────────────────────
    # 场景7：总结与验证
    # ─────────────────────────────────────────
    def scene_7_summary(self):
        frame = self.frame
        cx, cy = frame["cx"], frame["cy"]

        # 高亮整个商
        quot_group = VGroup(self.quot_1, self.quot_2, self.quot_0)

        title = Text(
            "结果：",
            font="PingFang SC",
            font_size=34,
            color=self.C_TITLE
        ).move_to(UP * 5.2)
        self.play(Write(title), run_time=0.4)

        self.play(
            Indicate(quot_group, color=self.C_GREEN, scale_factor=1.15),
            run_time=0.7
        )

        # 答案展示框
        answer_box_bg = RoundedRectangle(
            width=7.5, height=1.6,
            corner_radius=0.3,
            color=self.C_GREEN,
            fill_color="#0a2d1a",
            fill_opacity=0.9,
            stroke_width=3
        ).move_to(UP * 4.1)
        answer_text = MathTex(
            r"480 \div 4 = 120",
            font_size=58,
            color=self.C_GREEN
        ).move_to(UP * 4.1)
        self.play(FadeIn(answer_box_bg), Write(answer_text), run_time=0.8)
        self.wait(0.5)

        # 步骤回顾背景框
        step_bg = RoundedRectangle(
            width=7.8, height=4.0,
            corner_radius=0.3,
            color="#2a2a4a",
            fill_color="#16163a",
            fill_opacity=0.95,
            stroke_width=2
        ).move_to(UP * 1.3)
        self.play(FadeIn(step_bg), run_time=0.4)

        review_title = Text(
            "计算步骤回顾",
            font="PingFang SC",
            font_size=28,
            color=self.C_STEP
        ).move_to(UP * 2.8)
        self.play(Write(review_title), run_time=0.4)

        # 三行步骤
        steps_data = [
            ("百位：", r"4 \div 4 = 1", self.C_GREEN),
            ("十位：", r"8 \div 4 = 2", self.C_GREEN),
            ("个位：", r"0 \div 4 = 0", self.C_ORANGE),
        ]
        y_positions = [2.05, 1.2, 0.35]
        row_mobjects = []

        for (label_str, formula_str, color), ypos in zip(steps_data, y_positions):
            label_t = Text(
                label_str,
                font="PingFang SC",
                font_size=28,
                color=self.C_WHITE
            )
            formula_t = MathTex(formula_str, font_size=38, color=color)
            row = VGroup(label_t, formula_t).arrange(RIGHT, buff=0.2)
            row.move_to([0, ypos, 0])
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.4)
            row_mobjects.append(row)

        # 商末尾0强调
        zero_warn = Text(
            "商末尾的 0 绝对不能丢！",
            font="PingFang SC",
            font_size=26,
            color=self.C_HIGHLIGHT
        ).move_to(UP * -0.5)
        zero_box = SurroundingRectangle(
            zero_warn, color=self.C_HIGHLIGHT, buff=0.15, stroke_width=2.5
        )
        self.play(Write(zero_warn), Create(zero_box), run_time=0.6)
        self.wait(1.2)

        # 乘法验算
        verify_label = Text(
            "用乘法验算：",
            font="PingFang SC",
            font_size=28,
            color=self.C_STEP
        ).move_to(UP * -1.5)
        self.play(Write(verify_label), run_time=0.4)

        verify_formula = MathTex(
            r"120 \times 4 = 480 \checkmark",
            font_size=48,
            color=self.C_GREEN
        ).move_to(UP * -2.3)
        self.play(Write(verify_formula), run_time=0.7)
        self.play(
            Indicate(verify_formula, color=self.C_GREEN, scale_factor=1.08),
            run_time=0.5
        )
        self.wait(1.5)

        # 清除竖式和本场景所有元素
        self.play(
            FadeOut(VGroup(
                frame["divisor"], frame["d0"], frame["d1"], frame["d2"],
                frame["v_line"], frame["h_line"],
                self.quot_1, self.quot_2, self.quot_0
            )),
            FadeOut(title),
            FadeOut(answer_box_bg),
            FadeOut(answer_text),
            FadeOut(step_bg),
            FadeOut(review_title),
            FadeOut(zero_warn),
            FadeOut(zero_box),
            FadeOut(verify_label),
            FadeOut(verify_formula),
            *[FadeOut(r) for r in row_mobjects],
            run_time=0.6
        )

    # ─────────────────────────────────────────
    # 场景8：片尾
    # ─────────────────────────────────────────
    def scene_8_outro(self):
        # 大标题
        outro_title = Text(
            "三位数除以一位数",
            font="PingFang SC",
            font_size=44,
            color=self.C_TITLE
        ).move_to(UP * 2.5)
        self.play(Write(outro_title), run_time=0.7)

        # 核心口诀
        tips = [
            "从最高位开始，逐位相除",
            "余数与下一位合并继续除",
            "商末尾的 0 不能省略！",
        ]
        tip_objects = []
        tip_y = [1.4, 0.7, 0.0]
        for i, (tip, ypos) in enumerate(zip(tips, tip_y)):
            col = self.C_GREEN if i < 2 else self.C_ORANGE
            t = Text(
                f"• {tip}",
                font="PingFang SC",
                font_size=26,
                color=col
            ).move_to([0, ypos, 0])
            tip_objects.append(t)
        for t in tip_objects:
            self.play(FadeIn(t, shift=RIGHT * 0.3), run_time=0.4)
        self.wait(0.5)

        # 大答案
        big_answer = MathTex(
            r"480 \div 4 = 120",
            font_size=70,
            color=self.C_GREEN
        ).move_to(UP * -1.5)
        self.play(Write(big_answer), run_time=0.8)
        self.play(
            Flash(big_answer, color=self.C_GREEN, flash_radius=1.0, num_lines=10),
            run_time=0.7
        )
        self.wait(0.5)

        # 关注提示
        follow = Text(
            "关注我，获得更多数学技巧！",
            font="PingFang SC",
            font_size=28,
            color=self.C_YELLOW
        ).move_to(UP * -3.0)
        self.play(FadeIn(follow, shift=UP * 0.3), run_time=0.5)

        # 作者信息移至底部
        self.play(
            self.author.animate.move_to(UP * -4.0).set_color(self.C_GRAY),
            run_time=0.5
        )
        self.wait(2.0)
