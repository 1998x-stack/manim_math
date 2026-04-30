"""
003_正推与逆推.py — 正推与逆推 教学动画

知识点: 用计算盒(流程图)学习正推和逆推
  - 正推: 已知输入求输出, 按照运算顺序从左到右计算
  - 逆推: 已知输出求输入, 使用逆运算从右到左倒推
  - 培养可逆思维, 为解方程做准备

年级: 四年级上册
格式: TikTok 竖屏 (1080x1920)
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
BG_COLOR    = "#1a1a2e"
COLOR_FWD   = "#3b82f6"   # 蓝色  正推
COLOR_REV   = "#ef4444"   # 红色  逆推
COLOR_BOX   = "#1e3a5f"   # 深蓝  计算盒背景
COLOR_HL    = "#fbbf24"   # 黄色  高亮
COLOR_NUM   = "#22c55e"   # 绿色  数字
COLOR_OP    = "#f59e0b"   # 橙色  运算符
COLOR_ARROW_FWD = "#60a5fa"  # 正推箭头
COLOR_ARROW_REV = "#f87171"  # 逆推箭头
COLOR_AUTHOR = "#6b7280"
FONT = "PingFang SC"


# ======================================================================
# 工具函数
# ======================================================================

def make_box(label_text, width=2.2, height=1.0, box_color=COLOR_BOX,
             border_color=COLOR_FWD, font_size=26):
    """创建一个带文字标签的计算盒"""
    rect = Rectangle(
        width=width,
        height=height,
        color=border_color,
        fill_color=box_color,
        fill_opacity=1.0,
        stroke_width=2.5,
    )
    label = Text(label_text, font=FONT, font_size=font_size, color=WHITE)
    return VGroup(rect, label)


def make_oval(label_text, width=1.8, height=0.9, border_color=COLOR_NUM, font_size=30):
    """创建椭圆形输入/输出节点"""
    ellipse = Ellipse(
        width=width,
        height=height,
        color=border_color,
        fill_color="#0f2027",
        fill_opacity=1.0,
        stroke_width=2.5,
    )
    label = Text(label_text, font=FONT, font_size=font_size, color=border_color)
    return VGroup(ellipse, label)


# ======================================================================
# 主场景
# ======================================================================

class ForwardReverseLesson(Scene):
    """
    正推与逆推教学动画
    场景顺序:
      1. 开场钩子 — 神秘数字机器
      2. 正推 — 已知输入求输出 (例题1)
      3. 多步正推 — 两步计算盒 (例题2)
      4. 逆推概念引入
      5. 逆推 — 已知输出求输入 (例题)
      6. 正逆对比总结
      7. 片尾
    """

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.author = self._make_author()

        self.scene_1_opening()
        self.scene_2_forward_single()
        self.scene_3_forward_multi()
        self.scene_4_reverse_intro()
        self.scene_5_reverse_solve()
        self.scene_6_summary()
        self.scene_7_outro()

    # ------------------------------------------------------------------
    # 作者标识
    # ------------------------------------------------------------------

    def _make_author(self):
        return Text(
            "上海初高中数学直通车 @emptyandcalm",
            font=FONT,
            font_size=18,
            color=COLOR_AUTHOR,
        ).move_to(UP * 7.0)

    # ------------------------------------------------------------------
    # Scene 1: 开场钩子
    # ------------------------------------------------------------------

    def scene_1_opening(self):
        self.play(FadeIn(self.author, shift=DOWN * 0.2), run_time=0.4)

        # 钩子标题
        hook = Text("神秘的数字机器", font=FONT, font_size=44, color=COLOR_HL)
        hook.move_to(UP * 5.2)

        sub = Text("放进去一个数, 会变成什么?", font=FONT, font_size=26, color=GRAY_A)
        sub.move_to(UP * 4.4)

        self.play(Write(hook), run_time=0.8)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)

        # 画一个"机器"示意图
        machine = Rectangle(
            width=3.0, height=2.2,
            color=COLOR_FWD,
            fill_color="#0d1b2a",
            fill_opacity=1.0,
            stroke_width=3,
        ).move_to(UP * 1.5)

        gear_label = Text("×3", font=FONT, font_size=50, color=COLOR_OP)
        gear_label.move_to(UP * 1.5)

        # 输入箭头和数字
        arr_in = Arrow(
            start=LEFT * 3.5 + UP * 1.5,
            end=LEFT * 1.5 + UP * 1.5,
            color=COLOR_ARROW_FWD, buff=0, stroke_width=5,
        )
        num_in = Text("4", font=FONT, font_size=46, color=COLOR_NUM)
        num_in.move_to(LEFT * 4.2 + UP * 1.5)

        # 输出箭头和问号
        arr_out = Arrow(
            start=RIGHT * 1.5 + UP * 1.5,
            end=RIGHT * 3.5 + UP * 1.5,
            color=COLOR_ARROW_FWD, buff=0, stroke_width=5,
        )
        question = Text("?", font=FONT, font_size=52, color=COLOR_HL)
        question.move_to(RIGHT * 4.2 + UP * 1.5)

        self.play(FadeIn(machine), FadeIn(gear_label), run_time=0.6)
        self.play(FadeIn(num_in), Create(arr_in), run_time=0.5)
        self.play(Create(arr_out), FadeIn(question), run_time=0.5)
        self.wait(0.5)

        # 答案揭示
        answer = Text("12", font=FONT, font_size=46, color=COLOR_NUM)
        answer.move_to(RIGHT * 4.2 + UP * 1.5)
        self.play(ReplacementTransform(question, answer), run_time=0.5)
        self.wait(0.3)

        # 悬念: 逆向呢?
        reverse_q = Text("那反过来, 输出是12, 输入是多少?",
                         font=FONT, font_size=22, color=COLOR_REV)
        reverse_q.move_to(DOWN * 1.0)
        self.play(FadeIn(reverse_q, shift=UP * 0.3), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(hook), FadeOut(sub),
            FadeOut(machine), FadeOut(gear_label),
            FadeOut(num_in), FadeOut(arr_in),
            FadeOut(arr_out), FadeOut(answer),
            FadeOut(reverse_q),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 2: 正推 — 单步计算盒
    # ------------------------------------------------------------------

    def scene_2_forward_single(self):
        title = Text("正推 — 按顺序计算", font=FONT, font_size=36, color=COLOR_FWD)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 说明文字
        desc = Text("已知输入, 求输出", font=FONT, font_size=24, color=GRAY_A)
        desc.move_to(UP * 4.7)
        self.play(FadeIn(desc), run_time=0.4)

        # ---- 计算盒流程图 ----
        # 输入节点
        input_node = make_oval("8", border_color=COLOR_NUM, font_size=38)
        input_node.move_to(LEFT * 3.5 + UP * 2.5)

        # 运算盒
        op_box = make_box("×4", border_color=COLOR_FWD, font_size=32)
        op_box.move_to(UP * 2.5)

        # 输出节点 (问号)
        output_node = make_oval("?", border_color=COLOR_HL, font_size=38)
        output_node.move_to(RIGHT * 3.5 + UP * 2.5)

        # 箭头
        arr1 = Arrow(
            start=input_node.get_right(),
            end=op_box.get_left(),
            color=COLOR_ARROW_FWD, buff=0.1, stroke_width=4,
        )
        arr2 = Arrow(
            start=op_box.get_right(),
            end=output_node.get_left(),
            color=COLOR_ARROW_FWD, buff=0.1, stroke_width=4,
        )

        # 标签
        lbl_input = Text("输入", font=FONT, font_size=20, color=GRAY_B)
        lbl_input.next_to(input_node, DOWN, buff=0.2)
        lbl_output = Text("输出", font=FONT, font_size=20, color=GRAY_B)
        lbl_output.next_to(output_node, DOWN, buff=0.2)

        self.play(FadeIn(input_node), FadeIn(lbl_input), run_time=0.5)
        self.play(Create(arr1), run_time=0.4)
        self.play(FadeIn(op_box), run_time=0.5)
        self.play(Create(arr2), run_time=0.4)
        self.play(FadeIn(output_node), FadeIn(lbl_output), run_time=0.5)
        self.wait(0.5)

        # 计算步骤
        step_text = Text("8 × 4 = ?", font=FONT, font_size=30, color=WHITE)
        step_text.move_to(UP * 0.8)
        self.play(Write(step_text), run_time=0.6)
        self.wait(0.4)

        calc = Text("8 × 4 = 32", font=FONT, font_size=30, color=COLOR_NUM)
        calc.move_to(UP * 0.8)
        self.play(ReplacementTransform(step_text, calc), run_time=0.5)

        # 更新输出节点
        output_answer = make_oval("32", border_color=COLOR_NUM, font_size=38)
        output_answer.move_to(RIGHT * 3.5 + UP * 2.5)
        self.play(ReplacementTransform(output_node, output_answer), run_time=0.5)
        self.wait(0.3)

        # 正推方向指示
        fwd_label = Text("正推方向 →", font=FONT, font_size=22, color=COLOR_FWD)
        fwd_label.move_to(DOWN * 0.5)
        self.play(FadeIn(fwd_label, shift=RIGHT * 0.3), run_time=0.5)
        self.wait(1.2)

        # 清理
        self.play(
            FadeOut(title), FadeOut(desc),
            FadeOut(input_node), FadeOut(lbl_input),
            FadeOut(op_box), FadeOut(output_answer), FadeOut(lbl_output),
            FadeOut(arr1), FadeOut(arr2),
            FadeOut(calc), FadeOut(fwd_label),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 3: 多步正推
    # ------------------------------------------------------------------

    def scene_3_forward_multi(self):
        title = Text("多步正推", font=FONT, font_size=36, color=COLOR_FWD)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 例题: 输入5, 先×3再+6, 求输出
        example = Text("输入 5,  先 ×3,  再 +6,  输出=?",
                       font=FONT, font_size=24, color=GRAY_A)
        example.move_to(UP * 4.6)
        self.play(FadeIn(example), run_time=0.5)
        self.wait(0.3)

        # ---- 三节点流程图 ----
        y_row = 3.0

        # 节点位置
        pos_in  = LEFT * 3.5 + UP * y_row
        pos_op1 = LEFT * 1.0 + UP * y_row
        pos_op2 = RIGHT * 1.5 + UP * y_row
        pos_out = RIGHT * 3.8 + UP * y_row

        node_in  = make_oval("5",  border_color=COLOR_NUM, font_size=36)
        node_in.move_to(pos_in)

        box1 = make_box("×3", width=1.9, height=0.85, border_color=COLOR_FWD, font_size=30)
        box1.move_to(pos_op1)

        box2 = make_box("+6", width=1.9, height=0.85, border_color=COLOR_FWD, font_size=30)
        box2.move_to(pos_op2)

        node_out = make_oval("?", border_color=COLOR_HL, font_size=36)
        node_out.move_to(pos_out)

        arr_a = Arrow(node_in.get_right(),  box1.get_left(),  color=COLOR_ARROW_FWD, buff=0.08, stroke_width=4)
        arr_b = Arrow(box1.get_right(),     box2.get_left(),  color=COLOR_ARROW_FWD, buff=0.08, stroke_width=4)
        arr_c = Arrow(box2.get_right(),     node_out.get_left(), color=COLOR_ARROW_FWD, buff=0.08, stroke_width=4)

        # 展示流程图
        self.play(FadeIn(node_in), run_time=0.4)
        self.play(Create(arr_a), FadeIn(box1), run_time=0.5)
        self.play(Create(arr_b), FadeIn(box2), run_time=0.5)
        self.play(Create(arr_c), FadeIn(node_out), run_time=0.5)
        self.wait(0.5)

        # 步骤1: 5×3
        step1_label = Text("第一步:", font=FONT, font_size=24, color=COLOR_FWD)
        step1_label.move_to(LEFT * 2.0 + UP * 1.2)
        step1_calc = Text("5 × 3 = 15", font=FONT, font_size=28, color=WHITE)
        step1_calc.next_to(step1_label, RIGHT, buff=0.3)

        self.play(
            box1[0].animate.set_color(COLOR_HL),
            FadeIn(step1_label), Write(step1_calc),
            run_time=0.7,
        )

        # 中间结果节点
        mid_node = make_oval("15", border_color=COLOR_NUM, font_size=32, width=1.6, height=0.8)
        mid_node.move_to(pos_op1 + DOWN * 1.6)
        arr_mid = Arrow(box1.get_bottom(), mid_node.get_top(), color=COLOR_NUM, buff=0.08, stroke_width=3)
        self.play(Create(arr_mid), FadeIn(mid_node), run_time=0.5)
        self.wait(0.4)

        # 步骤2: 15+6
        step2_label = Text("第二步:", font=FONT, font_size=24, color=COLOR_FWD)
        step2_label.move_to(LEFT * 2.0 + UP * 0.3)
        step2_calc = Text("15 + 6 = 21", font=FONT, font_size=28, color=WHITE)
        step2_calc.next_to(step2_label, RIGHT, buff=0.3)

        self.play(
            box1[0].animate.set_color(COLOR_FWD),
            box2[0].animate.set_color(COLOR_HL),
            FadeIn(step2_label), Write(step2_calc),
            run_time=0.7,
        )

        # 输出答案
        node_out_ans = make_oval("21", border_color=COLOR_NUM, font_size=36)
        node_out_ans.move_to(pos_out)
        self.play(
            ReplacementTransform(node_out, node_out_ans),
            box2[0].animate.set_color(COLOR_FWD),
            run_time=0.5,
        )
        self.wait(1.0)

        # 正推提示
        summary_fwd = Text("正推: 从左到右, 依次计算", font=FONT, font_size=24, color=COLOR_FWD)
        summary_fwd.move_to(DOWN * 2.0)
        self.play(FadeIn(summary_fwd, shift=UP * 0.2), run_time=0.5)
        self.wait(1.5)

        # 清理
        self.play(
            FadeOut(title), FadeOut(example),
            FadeOut(node_in), FadeOut(box1), FadeOut(box2),
            FadeOut(node_out_ans),
            FadeOut(arr_a), FadeOut(arr_b), FadeOut(arr_c),
            FadeOut(step1_label), FadeOut(step1_calc),
            FadeOut(step2_label), FadeOut(step2_calc),
            FadeOut(mid_node), FadeOut(arr_mid),
            FadeOut(summary_fwd),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 4: 逆推概念引入
    # ------------------------------------------------------------------

    def scene_4_reverse_intro(self):
        title = Text("逆推 — 反向倒推", font=FONT, font_size=36, color=COLOR_REV)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        desc = Text("已知输出, 求输入", font=FONT, font_size=24, color=GRAY_A)
        desc.move_to(UP * 4.7)
        self.play(FadeIn(desc), run_time=0.4)
        self.wait(0.3)

        # 正运算 vs 逆运算 对照表
        table_title = Text("关键: 用逆运算!", font=FONT, font_size=28, color=COLOR_HL)
        table_title.move_to(UP * 3.5)
        self.play(FadeIn(table_title), run_time=0.5)

        # 运算对
        pairs = [
            ("+", "加法", "-", "减法"),
            ("-", "减法", "+", "加法"),
            ("×", "乘法", "÷", "除法"),
            ("÷", "除法", "×", "乘法"),
        ]

        row_y = [2.5, 1.6, 0.7, -0.2]
        pair_group = VGroup()

        for i, (op1, name1, op2, name2) in enumerate(pairs):
            y = row_y[i]

            op1_t = Text(op1,    font=FONT, font_size=30, color=COLOR_FWD)
            nm1_t = Text(name1,  font=FONT, font_size=24, color=GRAY_A)
            arrow_t = Text("←→", font=FONT, font_size=22, color=COLOR_HL)
            op2_t = Text(op2,    font=FONT, font_size=30, color=COLOR_REV)
            nm2_t = Text(name2,  font=FONT, font_size=24, color=GRAY_A)

            row = VGroup(op1_t, nm1_t, arrow_t, op2_t, nm2_t)
            row.arrange(RIGHT, buff=0.3)
            row.move_to(UP * y)
            pair_group.add(row)

            self.play(FadeIn(row, shift=LEFT * 0.2), run_time=0.35)

        self.wait(1.5)

        # 强调: 逆运算是关键
        key_text = Text("逆推 = 用逆运算从右往左推", font=FONT, font_size=26, color=COLOR_REV)
        key_text.move_to(DOWN * 1.5)
        self.play(FadeIn(key_text, scale=1.1), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(title), FadeOut(desc),
            FadeOut(table_title), FadeOut(pair_group), FadeOut(key_text),
            run_time=0.5,
        )

    # ------------------------------------------------------------------
    # Scene 5: 逆推解题
    # ------------------------------------------------------------------

    def scene_5_reverse_solve(self):
        title = Text("逆推例题", font=FONT, font_size=36, color=COLOR_REV)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.6)

        # 例题说明
        problem = Text("输出是 21,  运算: ×3 再 +6,  输入=?",
                       font=FONT, font_size=22, color=GRAY_A)
        problem.move_to(UP * 4.7)
        self.play(FadeIn(problem), run_time=0.5)
        self.wait(0.3)

        # 正推方向流程图 (作为参考, 灰显)
        y_row = 3.6
        pos_in  = LEFT * 3.5 + UP * y_row
        pos_op1 = LEFT * 1.0 + UP * y_row
        pos_op2 = RIGHT * 1.5 + UP * y_row
        pos_out = RIGHT * 3.8 + UP * y_row

        node_in  = make_oval("?", border_color=GRAY_B, font_size=34)
        node_in.move_to(pos_in)

        box1 = make_box("×3", width=1.9, height=0.85,
                        border_color=GRAY_B, box_color="#111827", font_size=28)
        box1.move_to(pos_op1)

        box2 = make_box("+6", width=1.9, height=0.85,
                        border_color=GRAY_B, box_color="#111827", font_size=28)
        box2.move_to(pos_op2)

        node_out = make_oval("21", border_color=COLOR_NUM, font_size=34)
        node_out.move_to(pos_out)

        arr_fwd1 = Arrow(node_in.get_right(),  box1.get_left(),
                         color=GRAY_B, buff=0.08, stroke_width=3)
        arr_fwd2 = Arrow(box1.get_right(),     box2.get_left(),
                         color=GRAY_B, buff=0.08, stroke_width=3)
        arr_fwd3 = Arrow(box2.get_right(),     node_out.get_left(),
                         color=GRAY_B, buff=0.08, stroke_width=3)

        lbl_fwd = Text("正推方向 →", font=FONT, font_size=18, color=GRAY_B)
        lbl_fwd.move_to(UP * (y_row - 0.8))

        self.play(
            FadeIn(node_in), FadeIn(box1), FadeIn(box2), FadeIn(node_out),
            Create(arr_fwd1), Create(arr_fwd2), Create(arr_fwd3),
            FadeIn(lbl_fwd),
            run_time=0.8,
        )
        self.wait(0.4)

        # ---------- 逆推箭头 (从右往左, 下方) ----------
        y_rev = y_row - 1.7

        # 逆运算盒 (对应 +6 的逆运算: -6)
        rbox2 = make_box("-6", width=1.9, height=0.85,
                         border_color=COLOR_REV, box_color="#2d0c0c", font_size=28)
        rbox2.move_to(pos_op2 + DOWN * 1.7)

        # 逆运算盒 (对应 ×3 的逆运算: ÷3)
        rbox1 = make_box("÷3", width=1.9, height=0.85,
                         border_color=COLOR_REV, box_color="#2d0c0c", font_size=28)
        rbox1.move_to(pos_op1 + DOWN * 1.7)

        # 中间值节点
        mid_rev = make_oval("15", border_color=COLOR_NUM, font_size=32, width=1.6, height=0.78)
        mid_rev.move_to(pos_in + DOWN * 1.7)

        # 逆推从输出出发
        r_start = node_out.get_bottom() + DOWN * 0.1
        r_arr0 = Arrow(
            r_start,
            rbox2.get_top(),
            color=COLOR_ARROW_REV, buff=0.08, stroke_width=4,
        )

        r_arr1 = Arrow(
            rbox2.get_left(),
            rbox1.get_right(),
            color=COLOR_ARROW_REV, buff=0.08, stroke_width=4,
        )

        r_arr2 = Arrow(
            rbox1.get_left(),
            mid_rev.get_right(),
            color=COLOR_ARROW_REV, buff=0.08, stroke_width=4,
        )

        lbl_rev = Text("逆推方向 ←", font=FONT, font_size=18, color=COLOR_REV)
        lbl_rev.move_to(UP * (y_rev - 0.6))

        self.play(
            FadeIn(lbl_rev), Create(r_arr0),
            run_time=0.5,
        )

        # 步骤1: 21-6=15
        step1 = Text("第一步 (逆): 21 - 6 = 15", font=FONT, font_size=24, color=WHITE)
        step1.move_to(DOWN * 0.5)
        self.play(FadeIn(rbox2), Write(step1), run_time=0.6)
        self.play(Create(r_arr1), FadeIn(mid_rev), run_time=0.5)
        self.wait(0.5)

        # 步骤2: 15÷3=5
        step2 = Text("第二步 (逆): 15 ÷ 3 = 5", font=FONT, font_size=24, color=WHITE)
        step2.move_to(DOWN * 1.2)
        self.play(FadeIn(rbox1), Write(step2), run_time=0.6)

        # 答案
        answer_node = make_oval("5", border_color=COLOR_NUM, font_size=36)
        answer_node.move_to(pos_in + DOWN * 1.7)
        self.play(Create(r_arr2), ReplacementTransform(mid_rev, answer_node), run_time=0.5)
        self.wait(0.5)

        # 验证
        verify = Text("验算: 5 × 3 + 6 = 21  ✓", font=FONT, font_size=24, color=COLOR_NUM)
        verify.move_to(DOWN * 2.2)
        self.play(FadeIn(verify, scale=1.05), run_time=0.6)
        self.wait(1.8)

        # 更新 node_in 显示答案
        answer_top = make_oval("5", border_color=COLOR_NUM, font_size=34)
        answer_top.move_to(pos_in)
        self.play(ReplacementTransform(node_in, answer_top), run_time=0.5)
        self.wait(0.8)

        # 清理
        self.play(
            FadeOut(title), FadeOut(problem),
            FadeOut(answer_top), FadeOut(box1), FadeOut(box2), FadeOut(node_out),
            FadeOut(arr_fwd1), FadeOut(arr_fwd2), FadeOut(arr_fwd3),
            FadeOut(lbl_fwd), FadeOut(lbl_rev),
            FadeOut(rbox1), FadeOut(rbox2),
            FadeOut(r_arr0), FadeOut(r_arr1), FadeOut(r_arr2),
            FadeOut(answer_node), FadeOut(step1), FadeOut(step2), FadeOut(verify),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 6: 正逆对比总结
    # ------------------------------------------------------------------

    def scene_6_summary(self):
        title = Text("正推 vs 逆推", font=FONT, font_size=38, color=COLOR_HL)
        title.move_to(UP * 5.5)
        self.play(Write(title), run_time=0.7)

        # 正推卡片
        fwd_bg = Rectangle(
            width=3.8, height=4.5,
            color=COLOR_FWD,
            fill_color="#0d1b35",
            fill_opacity=1.0,
            stroke_width=2.5,
        ).move_to(LEFT * 2.2 + UP * 1.5)

        fwd_head = Text("正推", font=FONT, font_size=32, color=COLOR_FWD)
        fwd_head.move_to(LEFT * 2.2 + UP * 3.5)

        fwd_arrow = Text("→", font=FONT, font_size=40, color=COLOR_ARROW_FWD)
        fwd_arrow.move_to(LEFT * 2.2 + UP * 2.7)

        fwd_l1 = Text("已知: 输入", font=FONT, font_size=22, color=GRAY_A)
        fwd_l1.move_to(LEFT * 2.2 + UP * 2.0)

        fwd_l2 = Text("求: 输出", font=FONT, font_size=22, color=GRAY_A)
        fwd_l2.move_to(LEFT * 2.2 + UP * 1.4)

        fwd_l3 = Text("方法:", font=FONT, font_size=20, color=WHITE)
        fwd_l3.move_to(LEFT * 2.2 + UP * 0.7)
        fwd_l4 = Text("依次正向运算", font=FONT, font_size=20, color=GRAY_A)
        fwd_l4.move_to(LEFT * 2.2 + UP * 0.1)

        fwd_example = Text("5 →×3→ 15\n  →+6→ 21", font=FONT, font_size=19, color=COLOR_NUM)
        fwd_example.move_to(LEFT * 2.2 + DOWN * 0.75)

        fwd_card = VGroup(fwd_bg, fwd_head, fwd_arrow,
                          fwd_l1, fwd_l2, fwd_l3, fwd_l4, fwd_example)

        # 逆推卡片
        rev_bg = Rectangle(
            width=3.8, height=4.5,
            color=COLOR_REV,
            fill_color="#2d0c0c",
            fill_opacity=1.0,
            stroke_width=2.5,
        ).move_to(RIGHT * 2.2 + UP * 1.5)

        rev_head = Text("逆推", font=FONT, font_size=32, color=COLOR_REV)
        rev_head.move_to(RIGHT * 2.2 + UP * 3.5)

        rev_arrow = Text("←", font=FONT, font_size=40, color=COLOR_ARROW_REV)
        rev_arrow.move_to(RIGHT * 2.2 + UP * 2.7)

        rev_l1 = Text("已知: 输出", font=FONT, font_size=22, color=GRAY_A)
        rev_l1.move_to(RIGHT * 2.2 + UP * 2.0)

        rev_l2 = Text("求: 输入", font=FONT, font_size=22, color=GRAY_A)
        rev_l2.move_to(RIGHT * 2.2 + UP * 1.4)

        rev_l3 = Text("方法:", font=FONT, font_size=20, color=WHITE)
        rev_l3.move_to(RIGHT * 2.2 + UP * 0.7)
        rev_l4 = Text("逆向用逆运算", font=FONT, font_size=20, color=GRAY_A)
        rev_l4.move_to(RIGHT * 2.2 + UP * 0.1)

        rev_example = Text("21 →-6→ 15\n   →÷3→  5", font=FONT, font_size=19, color=COLOR_NUM)
        rev_example.move_to(RIGHT * 2.2 + DOWN * 0.75)

        rev_card = VGroup(rev_bg, rev_head, rev_arrow,
                          rev_l1, rev_l2, rev_l3, rev_l4, rev_example)

        self.play(FadeIn(fwd_card, shift=RIGHT * 0.3), run_time=0.7)
        self.play(FadeIn(rev_card, shift=LEFT * 0.3), run_time=0.7)
        self.wait(0.5)

        # 逆运算对照小表
        table_y = -2.8
        table_bg = Rectangle(
            width=7.5, height=1.4,
            color=COLOR_HL,
            fill_color="#1e1a00",
            fill_opacity=1.0,
            stroke_width=2,
        ).move_to(DOWN * 3.2)

        table_text = Text(
            "+  ↔  -          ×  ↔  ÷",
            font=FONT, font_size=26, color=COLOR_HL,
        ).move_to(DOWN * 3.0)

        table_sub = Text("(互为逆运算)", font=FONT, font_size=20, color=GRAY_A)
        table_sub.move_to(DOWN * 3.6)

        self.play(FadeIn(table_bg), Write(table_text), run_time=0.6)
        self.play(FadeIn(table_sub), run_time=0.4)

        # 口诀
        mantra = Text(
            "正推顺序走, 逆推反向绕,\n逆运算是关键, 检验别忘掉!",
            font=FONT, font_size=22, color=WHITE,
            line_spacing=1.3,
        )
        mantra.move_to(DOWN * 5.2)
        self.play(FadeIn(mantra, shift=UP * 0.2), run_time=0.7)
        self.wait(2.5)

        self.play(
            FadeOut(title), FadeOut(fwd_card), FadeOut(rev_card),
            FadeOut(table_bg), FadeOut(table_text), FadeOut(table_sub),
            FadeOut(mantra),
            run_time=0.6,
        )

    # ------------------------------------------------------------------
    # Scene 7: 片尾
    # ------------------------------------------------------------------

    def scene_7_outro(self):
        # 作者信息放大
        author_big = Text(
            "上海初高中数学直通车",
            font=FONT, font_size=36, color=WHITE,
        ).move_to(UP * 1.5)

        author_id = Text(
            "@emptyandcalm",
            font=FONT, font_size=28, color=GRAY_B,
        ).move_to(UP * 0.6)

        self.play(
            Transform(self.author, author_big),
            run_time=0.7,
        )
        self.play(FadeIn(author_id, shift=UP * 0.2), run_time=0.5)

        # 关注提示
        follow = Text(
            "关注我, 获得更多数学技巧!",
            font=FONT, font_size=28, color=COLOR_HL,
        ).move_to(DOWN * 0.5)

        self.play(FadeIn(follow, shift=UP * 0.2, scale=1.05), run_time=0.6)

        # 装饰: 双向箭头动画
        deco_fwd = Arrow(LEFT * 2 + DOWN * 2.2, RIGHT * 2 + DOWN * 2.2,
                         color=COLOR_ARROW_FWD, stroke_width=5, buff=0)
        deco_rev = Arrow(RIGHT * 2 + DOWN * 3.0, LEFT * 2 + DOWN * 3.0,
                         color=COLOR_ARROW_REV, stroke_width=5, buff=0)

        lbl_fwd = Text("正推 →", font=FONT, font_size=22, color=COLOR_FWD)
        lbl_fwd.next_to(deco_fwd, UP, buff=0.15)
        lbl_rev = Text("← 逆推", font=FONT, font_size=22, color=COLOR_REV)
        lbl_rev.next_to(deco_rev, DOWN, buff=0.15)

        self.play(
            Create(deco_fwd), FadeIn(lbl_fwd),
            run_time=0.5,
        )
        self.play(
            Create(deco_rev), FadeIn(lbl_rev),
            run_time=0.5,
        )

        self.wait(2.0)

        self.play(
            FadeOut(self.author),
            FadeOut(author_id),
            FadeOut(follow),
            FadeOut(deco_fwd), FadeOut(lbl_fwd),
            FadeOut(deco_rev), FadeOut(lbl_rev),
            run_time=1.0,
        )
