"""
椭圆焦点反射性质 - Ellipse Focal Reflection Property
使用 Manim 创建的数学/物理教学视频

内容: 从椭圆一个焦点发出的光，经椭圆反射后必经过另一个焦点（费马原理）
目标观众: 高中生
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


class EllipseFocalReflection(Scene):
    """
    椭圆焦点反射性质教学动画场景
    
    场景顺序:
    1. 开场钩子 - 多条光线汇聚演示
    2. 椭圆定义 - 到两焦点距离之和恒定
    3. 反射定律 - 入射角=反射角
    4. 几何证明 - 椭圆切线性质
    5. 费马原理 - 物理角度理解
    6. 应用与片尾
    """
    
    def construct(self):
        # 设置背景色
        self.camera.background_color = "#1a1a2e"
        
        # 配色方案
        self.COLOR_ELLIPSE = "#3498db"        # 蓝色 - 椭圆
        self.COLOR_FOCUS = "#e74c3c"          # 红色 - 焦点
        self.COLOR_LIGHT_PATH = "#f39c12"     # 橙色 - 光线
        self.COLOR_TANGENT = "#2ecc71"        # 绿色 - 切线
        self.COLOR_NORMAL = "#9b59b6"         # 紫色 - 法线
        self.COLOR_AUXILIARY = GRAY_B         # 灰色 - 辅助
        self.COLOR_HIGHLIGHT = YELLOW         # 黄色 - 高亮
        
        # 字体大小
        self.FONT_TITLE = 36
        self.FONT_SUBTITLE = 28
        self.FONT_BODY = 22
        self.FONT_SMALL = 18
        
        # 初始化几何数据
        self.setup_geometry()
        
        # 执行动画序列
        self.scene_1_opening()
        self.scene_2_ellipse_definition()
        self.scene_3_reflection_law()
        self.scene_4_geometric_proof()
        self.scene_5_fermat_principle()
        self.scene_6_applications_outro()
    
    def setup_geometry(self):
        """初始化椭圆和所有几何元素"""
        # 椭圆参数
        self.a = 3.0  # 半长轴
        self.b = 2.0  # 半短轴
        self.c = np.sqrt(self.a**2 - self.b**2)  # 焦距
        
        # 缩放和偏移
        self.SCALE = 0.85
        self.OFFSET = UP * 1.5
        
        # 应用缩放
        self.a_scaled = self.a * self.SCALE
        self.b_scaled = self.b * self.SCALE
        self.c_scaled = self.c * self.SCALE
        
        # 焦点坐标
        self.F1 = np.array([-self.c_scaled, 0, 0]) + self.OFFSET
        self.F2 = np.array([self.c_scaled, 0, 0]) + self.OFFSET
        
        # 选择反射点（参数角度60°）
        self.t_param = np.radians(60)
        self.P = self.point_on_ellipse(self.t_param)
        
        # 计算切线和法线方向
        self.tangent_dir = self.tangent_direction(self.t_param)
        self.normal_dir = self.normal_direction(self.t_param)
        
        # 验证几何计算
        self.verify_geometry()
    
    def point_on_ellipse(self, t):
        """椭圆参数方程上的点"""
        x = self.a_scaled * np.cos(t)
        y = self.b_scaled * np.sin(t)
        return np.array([x, y, 0]) + self.OFFSET
    
    def tangent_direction(self, t):
        """椭圆在参数t处的切线方向"""
        dx = -self.a_scaled * np.sin(t)
        dy = self.b_scaled * np.cos(t)
        tangent = np.array([dx, dy, 0])
        return tangent / np.linalg.norm(tangent)
    
    def normal_direction(self, t):
        """椭圆在参数t处的外法线方向"""
        nx = self.b_scaled * np.cos(t)
        ny = self.a_scaled * np.sin(t)
        normal = np.array([nx, ny, 0])
        return normal / np.linalg.norm(normal)
    
    def verify_geometry(self):
        """验证几何计算的正确性"""
        epsilon = 1e-6
        
        # 验证点P在椭圆上
        P_centered = self.P - self.OFFSET
        ellipse_check = (P_centered[0]**2 / self.a_scaled**2 + 
                        P_centered[1]**2 / self.b_scaled**2)
        assert abs(ellipse_check - 1.0) < epsilon, "P不在椭圆上"
        
        # 验证焦点距离和
        dist_sum = (np.linalg.norm(self.P - self.F1) + 
                   np.linalg.norm(self.F2 - self.P))
        expected_sum = 2 * self.a_scaled
        assert abs(dist_sum - expected_sum) < epsilon, "焦点距离和错误"
        
        # 验证切线垂直于法线
        dot_product = np.dot(self.tangent_dir, self.normal_dir)
        assert abs(dot_product) < epsilon, "切线不垂直于法线"
        
        print("✓ 椭圆反射几何验证通过")
    
    def scene_1_opening(self):
        """场景1: 开场钩子 (0-5秒)"""
        # 作者信息（顶部）
        self.author_info = Text(
            "上海初高中数学直通车 @emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_B
        ).move_to(UP * 7)
        
        self.play(FadeIn(self.author_info, shift=DOWN * 0.2), run_time=0.3)
        
        # 钩子问题
        hook_text = Text(
            "为什么椭圆镜面\n能汇聚光线?",
            font="Noto Sans CJK SC",
            font_size=42,
            color=self.COLOR_HIGHLIGHT
        ).move_to(UP * 6)
        
        self.play(Write(hook_text), run_time=0.8)
        self.wait(0.3)
        
        # 创建椭圆
        self.ellipse = Ellipse(
            width=2 * self.a_scaled,
            height=2 * self.b_scaled,
            color=self.COLOR_ELLIPSE,
            stroke_width=3
        ).move_to(self.OFFSET)
        
        self.play(Create(self.ellipse), run_time=1.0)
        
        # 焦点
        f1_dot = Dot(self.F1, color=self.COLOR_FOCUS, radius=0.08)
        f2_dot = Dot(self.F2, color=self.COLOR_FOCUS, radius=0.08)
        f1_label = Text("F₁", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_FOCUS).next_to(f1_dot, DOWN, buff=0.1)
        f2_label = Text("F₂", font="Noto Sans CJK SC", font_size=22, color=self.COLOR_FOCUS).next_to(f2_dot, DOWN, buff=0.1)
        
        self.play(
            FadeIn(f1_dot, scale=0.5),
            FadeIn(f2_dot, scale=0.5),
            run_time=0.3
        )
        self.play(
            Flash(f1_dot, color=self.COLOR_FOCUS, flash_radius=0.3),
            Flash(f2_dot, color=self.COLOR_FOCUS, flash_radius=0.3),
            run_time=0.4
        )
        self.play(FadeIn(f1_label), FadeIn(f2_label), run_time=0.3)
        
        # 多条光线演示（从F1发出，在不同点反射到F2）
        light_paths = VGroup()
        test_angles = [30, 45, 60, 75, 105, 120, 135, 150]
        
        for angle in test_angles:
            t = np.radians(angle)
            P_temp = self.point_on_ellipse(t)
            
            ray_in = Line(self.F1, P_temp, color=self.COLOR_LIGHT_PATH, stroke_width=2)
            ray_out = Line(P_temp, self.F2, color=self.COLOR_LIGHT_PATH, stroke_width=2)
            
            light_paths.add(ray_in, ray_out)
        
        self.play(
            LaggedStart(*[Create(ray) for ray in light_paths], lag_ratio=0.1),
            run_time=1.5
        )
        self.wait(0.6)
        
        # 清理
        self.play(
            FadeOut(hook_text),
            FadeOut(light_paths),
            run_time=0.5
        )
        
        # 保留元素
        self.f1_dot = f1_dot
        self.f2_dot = f2_dot
        self.f1_label = f1_label
        self.f2_label = f2_label
    
    def scene_2_ellipse_definition(self):
        """场景2: 椭圆定义 (5-12秒)"""
        # 标题
        title = Text(
            "椭圆的定义",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 在椭圆上添加一个动点P
        p_dot = Dot(self.P, color=WHITE, radius=0.08)
        p_label = Text("P", font="Noto Sans CJK SC", font_size=22, color=WHITE).next_to(p_dot, UR, buff=0.1)
        
        self.play(FadeIn(p_dot, scale=0.5), FadeIn(p_label), run_time=0.3)
        
        # 连线PF1和PF2
        line_pf1 = Line(self.P, self.F1, color=self.COLOR_AUXILIARY, stroke_width=2)
        line_pf2 = Line(self.P, self.F2, color=self.COLOR_AUXILIARY, stroke_width=2)
        
        self.play(Create(line_pf1), run_time=0.5)
        self.play(Create(line_pf2), run_time=0.5)
        
        # 距离标注
        dist_f1p = np.linalg.norm(self.P - self.F1)
        dist_pf2 = np.linalg.norm(self.F2 - self.P)
        
        # 公式
        formula = MathTex(
            r"|PF_1| + |PF_2| = 2a",
            font_size=self.FONT_BODY
        ).move_to(DOWN * 4.5)
        formula.set_color_by_tex("常数", self.COLOR_HIGHLIGHT)
        
        self.play(Write(formula), run_time=0.8)
        self.wait(0.4)
        
        # 让P沿椭圆移动
        def update_p(mob, alpha):
            # 从60度移动到300度
            t = np.radians(60 + alpha * 240)
            new_pos = self.point_on_ellipse(t)
            mob.move_to(new_pos)
        
        def update_label(mob):
            mob.next_to(p_dot, UR, buff=0.1)
        
        def update_line_pf1(mob):
            mob.put_start_and_end_on(p_dot.get_center(), self.F1)
        
        def update_line_pf2(mob):
            mob.put_start_and_end_on(p_dot.get_center(), self.F2)
        
        p_label.add_updater(update_label)
        line_pf1.add_updater(update_line_pf1)
        line_pf2.add_updater(update_line_pf2)
        
        self.play(
            UpdateFromAlphaFunc(p_dot, update_p),
            run_time=2.5,
            rate_func=smooth
        )
        
        # 移除updater
        p_label.remove_updater(update_label)
        line_pf1.remove_updater(update_line_pf1)
        line_pf2.remove_updater(update_line_pf2)
        
        # 强调公式
        self.play(Indicate(formula, color=self.COLOR_HIGHLIGHT), run_time=0.6)
        self.wait(0.7)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line_pf1),
            FadeOut(line_pf2),
            FadeOut(formula),
            run_time=0.5
        )
        
        # 保留P点
        self.p_dot = p_dot
        self.p_label = p_label
        
        # P回到原位置
        self.play(p_dot.animate.move_to(self.P), run_time=0.4)
        p_label.next_to(p_dot, UR, buff=0.1)
    
    def scene_3_reflection_law(self):
        """场景3: 反射定律 (12-20秒)"""
        # 标题
        title = Text(
            "反射定律",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 绘制切线
        tangent_length = 2.5
        tangent_start = self.P - self.tangent_dir * tangent_length
        tangent_end = self.P + self.tangent_dir * tangent_length
        
        tangent_line = Line(
            tangent_start,
            tangent_end,
            color=self.COLOR_TANGENT,
            stroke_width=2
        )
        
        tangent_label = Text(
            "切线",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_TANGENT
        ).next_to(tangent_end, RIGHT, buff=0.15)
        
        self.play(Create(tangent_line), FadeIn(tangent_label), run_time=0.6)
        
        # 绘制法线
        normal_length = 1.8
        normal_start = self.P
        normal_end = self.P + self.normal_dir * normal_length
        
        normal_line = DashedLine(
            normal_start,
            normal_end,
            color=self.COLOR_NORMAL,
            stroke_width=2,
            dash_length=0.1
        )
        
        normal_label = Text(
            "法线",
            font="Noto Sans CJK SC",
            font_size=self.FONT_SMALL,
            color=self.COLOR_NORMAL
        ).next_to(normal_end, UP, buff=0.1)
        
        self.play(Create(normal_line), FadeIn(normal_label), run_time=0.6)
        
        # 入射光线（从F1到P）
        incident_ray = Arrow(
            self.F1,
            self.P,
            color=self.COLOR_LIGHT_PATH,
            stroke_width=3,
            buff=0.08,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(Create(incident_ray), run_time=0.7)
        
        # 反射光线（从P到F2）
        reflected_ray = Arrow(
            self.P,
            self.F2,
            color=self.COLOR_LIGHT_PATH,
            stroke_width=3,
            buff=0.08,
            max_tip_length_to_length_ratio=0.15
        )
        
        self.play(Create(reflected_ray), run_time=0.7)
        
        # 标注角度
        # 入射角
        incident_dir = self.P - self.F1
        incident_dir_norm = incident_dir / np.linalg.norm(incident_dir)
        
        # 使用Angle类创建角度标记
        # 创建临时线段用于Angle
        temp_line_incident = Line(self.P, self.P - incident_dir_norm * 0.8)
        temp_line_normal = Line(self.P, self.P + self.normal_dir * 0.8)
        
        angle_in_arc = Angle(
            temp_line_incident,
            temp_line_normal,
            radius=0.4,
            color=self.COLOR_HIGHLIGHT,
            other_angle=False
        )
        
        angle_in_label = MathTex(r"\theta_1", font_size=20, color=self.COLOR_HIGHLIGHT)
        # 角平分线方向放置标签
        bisector_in = incident_dir_norm + self.normal_dir
        bisector_in = bisector_in / np.linalg.norm(bisector_in)
        angle_in_label.move_to(self.P + bisector_in * 0.6)
        
        self.play(Create(angle_in_arc), FadeIn(angle_in_label), run_time=0.5)
        
        # 反射角
        reflected_dir = self.F2 - self.P
        reflected_dir_norm = reflected_dir / np.linalg.norm(reflected_dir)
        
        temp_line_reflected = Line(self.P, self.P + reflected_dir_norm * 0.8)
        
        angle_out_arc = Angle(
            temp_line_normal,
            temp_line_reflected,
            radius=0.4,
            color=self.COLOR_HIGHLIGHT,
            other_angle=False
        )
        
        angle_out_label = MathTex(r"\theta_2", font_size=20, color=self.COLOR_HIGHLIGHT)
        bisector_out = reflected_dir_norm + self.normal_dir
        bisector_out = bisector_out / np.linalg.norm(bisector_out)
        angle_out_label.move_to(self.P + bisector_out * 0.6)
        
        self.play(Create(angle_out_arc), FadeIn(angle_out_label), run_time=0.5)
        
        # 反射定律公式
        law_formula = MathTex(
            r"\theta_1 = \theta_2",
            font_size=self.FONT_SUBTITLE,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 5)
        
        self.play(Write(law_formula), run_time=0.8)
        
        # 角度闪烁验证
        self.play(
            Flash(angle_in_arc, color=self.COLOR_HIGHLIGHT),
            Flash(angle_out_arc, color=self.COLOR_HIGHLIGHT),
            run_time=0.6
        )
        self.wait(0.5)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(law_formula),
            run_time=0.5
        )
        
        # 保留元素供下一场景使用
        self.tangent_line = tangent_line
        self.tangent_label = tangent_label
        self.normal_line = normal_line
        self.normal_label = normal_label
        self.incident_ray = incident_ray
        self.reflected_ray = reflected_ray
        self.angle_in_arc = angle_in_arc
        self.angle_in_label = angle_in_label
        self.angle_out_arc = angle_out_arc
        self.angle_out_label = angle_out_label
    
    def scene_4_geometric_proof(self):
        """场景4: 几何证明 (20-35秒)"""
        # 标题
        title = Text(
            "为什么反射必过另一焦点?",
            font="Noto Sans CJK SC",
            font_size=32,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)
        
        # 说明文字1
        explain_1 = Text(
            "观察PF₁与切线的夹角",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain_1), run_time=0.8)
        
        # 绘制PF1连线
        line_pf1 = Line(self.P, self.F1, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.play(Create(line_pf1), run_time=0.5)
        
        # 标注α角（PF1与切线的夹角）
        dir_pf1 = self.F1 - self.P
        dir_pf1_norm = dir_pf1 / np.linalg.norm(dir_pf1)
        
        temp_line_pf1 = Line(self.P, self.P + dir_pf1_norm * 0.6)
        temp_line_tangent = Line(self.P, self.P + self.tangent_dir * 0.6)
        
        angle_alpha = Angle(
            temp_line_pf1,
            temp_line_tangent,
            radius=0.35,
            color=BLUE,
            other_angle=False
        )
        
        alpha_label = MathTex(r"\alpha", font_size=22, color=BLUE)
        alpha_label.move_to(self.P + (dir_pf1_norm + self.tangent_dir) / np.linalg.norm(dir_pf1_norm + self.tangent_dir) * 0.55)
        
        self.play(Create(angle_alpha), FadeIn(alpha_label), run_time=0.6)
        self.wait(0.4)
        
        # 说明文字2
        self.play(FadeOut(explain_1), run_time=0.3)
        explain_2 = Text(
            "观察PF₂与切线的夹角",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A
        ).move_to(DOWN * 4)
        
        self.play(FadeIn(explain_2), run_time=0.8)
        
        # 绘制PF2连线
        line_pf2 = Line(self.P, self.F2, color=self.COLOR_AUXILIARY, stroke_width=2)
        self.play(Create(line_pf2), run_time=0.5)
        
        # 标注β角（PF2与切线的夹角）
        dir_pf2 = self.F2 - self.P
        dir_pf2_norm = dir_pf2 / np.linalg.norm(dir_pf2)
        
        temp_line_pf2 = Line(self.P, self.P + dir_pf2_norm * 0.6)
        
        angle_beta = Angle(
            temp_line_tangent,
            temp_line_pf2,
            radius=0.35,
            color=RED,
            other_angle=False
        )
        
        beta_label = MathTex(r"\beta", font_size=22, color=RED)
        beta_label.move_to(self.P + (dir_pf2_norm + self.tangent_dir) / np.linalg.norm(dir_pf2_norm + self.tangent_dir) * 0.55)
        
        self.play(Create(angle_beta), FadeIn(beta_label), run_time=0.6)
        self.wait(0.4)
        
        # 椭圆切线性质
        self.play(FadeOut(explain_2), run_time=0.3)
        property_text = Text(
            "椭圆切线性质:\n∠(PF₁,切线) = ∠(PF₂,切线)",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A,
            line_spacing=0.8
        ).move_to(DOWN * 4.5)
        
        self.play(Write(property_text), run_time=1.0)
        
        # 高亮α = β
        equal_formula = MathTex(r"\alpha = \beta", font_size=28, color=self.COLOR_HIGHLIGHT).move_to(DOWN * 5.8)
        self.play(
            Flash(angle_alpha, color=BLUE),
            Flash(angle_beta, color=RED),
            Write(equal_formula),
            run_time=0.8
        )
        self.wait(0.4)
        
        # 推导
        derivation = VGroup(
            Text("因为 α = β", font="Noto Sans CJK SC", font_size=18, color=GRAY_A),
            Text("且 切线⊥法线", font="Noto Sans CJK SC", font_size=18, color=GRAY_A),
            Text("所以 θ₁ = θ₂", font="Noto Sans CJK SC", font_size=18, color=self.COLOR_HIGHLIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(DOWN * 6.5)
        
        self.play(FadeIn(derivation, shift=UP * 0.3), run_time=1.5)
        
        # 箭头指向结论
        conclusion = Text(
            "反射光线必定经过F₂!",
            font="Noto Sans CJK SC",
            font_size=24,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 7.5)
        
        arrow = Arrow(derivation.get_bottom(), conclusion.get_top(), color=self.COLOR_HIGHLIGHT, stroke_width=2, buff=0.1)
        
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(Write(conclusion), run_time=1.2)
        
        self.wait(1.6)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(line_pf1),
            FadeOut(line_pf2),
            FadeOut(angle_alpha),
            FadeOut(angle_beta),
            FadeOut(alpha_label),
            FadeOut(beta_label),
            FadeOut(property_text),
            FadeOut(equal_formula),
            FadeOut(derivation),
            FadeOut(arrow),
            FadeOut(conclusion),
            run_time=0.6
        )
    
    def scene_5_fermat_principle(self):
        """场景5: 费马原理 (35-50秒)"""
        # 标题
        title = Text(
            "费马原理",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)
        
        # 费马原理说明
        fermat_text = Text(
            "光沿所有可能路径中\n的稳定路径传播",
            font="Noto Sans CJK SC",
            font_size=self.FONT_BODY,
            color=GRAY_A,
            line_spacing=0.9
        ).move_to(UP * 4.5)
        
        self.play(FadeIn(fermat_text), run_time=1.0)
        
        # 绘制多条可能路径（从F1经椭圆上不同点到F2）
        path_group = VGroup()
        test_angles = [30, 45, 60, 75, 105, 120, 135, 150]
        length_labels = VGroup()
        
        for i, angle in enumerate(test_angles):
            t = np.radians(angle)
            P_temp = self.point_on_ellipse(t)
            
            ray_in = Line(self.F1, P_temp, color=GRAY_B, stroke_width=1.5, stroke_opacity=0.6)
            ray_out = Line(P_temp, self.F2, color=GRAY_B, stroke_width=1.5, stroke_opacity=0.6)
            
            path_group.add(ray_in, ray_out)
            
            # 计算路径长度
            length = np.linalg.norm(P_temp - self.F1) + np.linalg.norm(self.F2 - P_temp)
        
        self.play(
            LaggedStart(*[Create(path) for path in path_group], lag_ratio=0.08),
            run_time=1.5
        )
        
        # 标注：所有路径长度相同
        equal_lengths_text = Text(
            "所有路径: |PF₁| + |PF₂| = 2a",
            font="Noto Sans CJK SC",
            font_size=20,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 4)
        
        self.play(Write(equal_lengths_text), run_time=0.8)
        
        # 高亮当前反射路径
        highlight_in = self.incident_ray.copy().set_color(self.COLOR_HIGHLIGHT).set_stroke_width(4)
        highlight_out = self.reflected_ray.copy().set_color(self.COLOR_HIGHLIGHT).set_stroke_width(4)
        
        self.play(
            Create(highlight_in),
            Create(highlight_out),
            run_time=0.5
        )
        
        # 说明：唯一稳定路径
        stable_text = Text(
            "满足反射定律的路径\n是唯一的稳定路径",
            font="Noto Sans CJK SC",
            font_size=20,
            color=GRAY_A,
            line_spacing=0.9
        ).move_to(DOWN * 5)
        
        self.play(FadeIn(stable_text), run_time=1.0)
        
        # 其他路径淡化
        self.play(
            path_group.animate.set_opacity(0.2),
            run_time=0.6
        )
        
        # 结论
        conclusion = Text(
            "光线在椭圆镜面上的反射\n总是经过两个焦点!",
            font="Noto Sans CJK SC",
            font_size=22,
            color=self.COLOR_HIGHLIGHT,
            line_spacing=0.9
        ).move_to(DOWN * 6.5)
        
        self.play(Write(conclusion), run_time=1.2)
        self.wait(2.0)
        
        # 清理
        self.play(
            FadeOut(title),
            FadeOut(fermat_text),
            FadeOut(path_group),
            FadeOut(equal_lengths_text),
            FadeOut(highlight_in),
            FadeOut(highlight_out),
            FadeOut(stable_text),
            FadeOut(conclusion),
            FadeOut(self.tangent_line),
            FadeOut(self.tangent_label),
            FadeOut(self.normal_line),
            FadeOut(self.normal_label),
            FadeOut(self.angle_in_arc),
            FadeOut(self.angle_in_label),
            FadeOut(self.angle_out_arc),
            FadeOut(self.angle_out_label),
            FadeOut(self.incident_ray),
            FadeOut(self.reflected_ray),
            FadeOut(self.p_dot),
            FadeOut(self.p_label),
            run_time=0.8
        )
    
    def scene_6_applications_outro(self):
        """场景6: 应用与片尾 (50-65秒)"""
        # 标题
        title = Text(
            "实际应用",
            font="Noto Sans CJK SC",
            font_size=self.FONT_TITLE,
            color=WHITE
        ).move_to(UP * 5.5)
        
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.5)
        
        # 多束光线汇聚演示
        light_beams = VGroup()
        for angle in range(20, 160, 15):
            t = np.radians(angle)
            P_temp = self.point_on_ellipse(t)
            
            beam_in = Arrow(
                self.F1, P_temp,
                color=self.COLOR_LIGHT_PATH,
                stroke_width=2,
                buff=0.05,
                max_tip_length_to_length_ratio=0.1
            )
            beam_out = Arrow(
                P_temp, self.F2,
                color=self.COLOR_LIGHT_PATH,
                stroke_width=2,
                buff=0.05,
                max_tip_length_to_length_ratio=0.1
            )
            
            light_beams.add(beam_in, beam_out)
        
        self.play(
            LaggedStart(*[Create(beam) for beam in light_beams], lag_ratio=0.05),
            run_time=2.0
        )
        
        # 应用场景文字
        app_1 = Text(
            "1. 医疗碎石 - 椭圆反射聚焦",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 3.5)
        
        app_2 = Text(
            "2. 耳语廊 - 声波传播",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 4.5)
        
        app_3 = Text(
            "3. 天文望远镜 - 光学系统",
            font="Noto Sans CJK SC",
            font_size=22,
            color=GRAY_A
        ).move_to(DOWN * 5.5)
        
        self.play(FadeIn(app_1), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(app_2), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(app_3), run_time=0.6)
        self.wait(0.6)
        
        # 清理所有图形
        self.play(
            FadeOut(title),
            FadeOut(self.ellipse),
            FadeOut(self.f1_dot),
            FadeOut(self.f2_dot),
            FadeOut(self.f1_label),
            FadeOut(self.f2_label),
            FadeOut(light_beams),
            FadeOut(app_1),
            FadeOut(app_2),
            FadeOut(app_3),
            run_time=0.8
        )
        
        # 作者信息放大
        author_name = Text(
            "上海初高中数学直通车",
            font="Noto Sans CJK SC",
            font_size=40,
            color=WHITE
        ).move_to(UP * 1.5)
        
        author_id = Text(
            "@emptyandcalm",
            font="Noto Sans CJK SC",
            font_size=32,
            color=GRAY_B
        ).move_to(UP * 0.5)
        
        self.play(
            Transform(self.author_info, author_name),
            run_time=0.8
        )
        self.play(FadeIn(author_id, shift=UP * 0.3), run_time=0.5)
        
        # 关注提示
        follow_text = Text(
            "关注我, 学更多数学技巧!",
            font="Noto Sans CJK SC",
            font_size=30,
            color=self.COLOR_HIGHLIGHT
        ).move_to(DOWN * 0.5)
        
        self.play(FadeIn(follow_text, shift=UP * 0.3, scale=1.1), run_time=0.6)
        
        # 装饰 - 小椭圆图标
        ellipse_icons = VGroup()
        for i in range(5):
            icon = Ellipse(
                width=0.6, height=0.4,
                color=self.COLOR_ELLIPSE,
                fill_opacity=0.6,
                stroke_width=1
            ).move_to(follow_text.get_center() + 2.5 * np.array([np.cos(i * 2*PI/5), np.sin(i * 2*PI/5), 0]))
            ellipse_icons.add(icon)
        ellipse_icons.move_to(DOWN * 2.5)
        
        self.play(
            *[FadeIn(icon, scale=0.5) for icon in ellipse_icons],
            run_time=0.8
        )
        
        # 旋转装饰
        self.play(
            Rotate(ellipse_icons, angle=PI, run_time=1.5)
        )
        
        self.wait(2.7)


# 运行命令:
# manim -pql ellipse_reflection.py EllipseFocalReflection  # 快速预览
# manim -qh ellipse_reflection.py EllipseFocalReflection   # 高质量 1080p
# manim -qk ellipse_reflection.py EllipseFocalReflection   # 4K质量