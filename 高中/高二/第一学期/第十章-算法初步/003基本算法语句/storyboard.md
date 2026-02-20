# 基本算法语句 - 教学动画分镜脚本

## 元信息
- **目标时长:** 60-65 秒
- **场景数量:** 8 个
- **难度等级:** 高二
- **关键概念:** 赋值、输入、输出、条件、循环语句

## 配色方案
```python
COLOR_PRIMARY = "#3498db"       # 蓝色 - 主要概念
COLOR_SECONDARY = "#e74c3c"     # 红色 - 重要标记
COLOR_HIGHLIGHT = YELLOW        # 黄色 - 高亮
COLOR_AUXILIARY = GRAY_B        # 灰色 - 辅助线
COLOR_SUCCESS = "#2ecc71"       # 绿色 - 成功/输出
BACKGROUND = "#1a1a2e"          # 深色背景

# 语句类型颜色
COLOR_ASSIGNMENT = "#3498db"    # 蓝色 - 赋值语句
COLOR_INPUT = "#2ecc71"         # 绿色 - 输入语句
COLOR_OUTPUT = "#2ecc71"        # 绿色 - 输出语句
COLOR_CONDITION = "#f39c12"     # 橙色 - 条件语句
COLOR_LOOP = "#9b59b6"          # 紫色 - 循环语句

# 代码高亮颜色
COLOR_CODE_BG = "#2c3e50"       # 代码背景
COLOR_CODE_TEXT = WHITE         # 代码文字
COLOR_CODE_KEYWORD = "#e74c3c"  # 关键字（IF, FOR等）
COLOR_CODE_VARIABLE = "#3498db" # 变量
COLOR_CODE_NUMBER = "#f39c12"   # 数字
```

## 布局计算
```python
# TikTok 竖屏坐标系
SAFE_X = 4.0  # x ∈ [-4, +4]
SAFE_Y_TOP = 7.0  # y ∈ [-7, +7]

# 功能区域
AUTHOR_Y = 7.0          # 作者信息
TITLE_Y = 6.0           # 标题区
CODE_Y = 2.0            # 代码显示区
VARIABLE_Y = -2.0       # 变量/内存区
EXPLANATION_Y = -5.0    # 说明文字区
```

## 元素尺寸标准
```python
# 代码框尺寸
CODE_WIDTH = 7.0
CODE_HEIGHT = 4.0

# 变量框尺寸
VAR_BOX_WIDTH = 2.5
VAR_BOX_HEIGHT = 1.0

# 文字大小
FONT_TITLE = 36
FONT_SUBTITLE = 28
FONT_BODY = 22
FONT_CODE = 20
FONT_LABEL = 18
FONT_SMALL = 16
```

---

## Scene 1: 开场钩子
**时长:** 4 秒  
**目的:** 引出基本算法语句的概念

### 元素布局
```
y=+7: 作者信息（常驻）
y=+6: 钩子问题 "如何让计算机执行算法?"
y=+2: 代码片段闪现
      x = 5
      IF x > 0 THEN
      FOR i = 1 TO 10
y=-4: 引导文字 "答案: 基本算法语句"
```

### 动画序列
| 时间 | 动作 | 持续时间 |
|------|------|---------|
| 0.0s | 作者信息淡入 | 0.3s |
| 0.3s | 钩子问题书写 | 0.8s |
| 1.1s | 代码片段逐行淡入 | 1.2s |
| 2.3s | 引导文字淡入 | 0.5s |
| 2.8s | 理解停顿 | 1.2s |

---

## Scene 2: 基本算法语句定义
**时长:** 5 秒  
**目的:** 给出基本算法语句的定义

### 元素布局
```
y=+6: 标题 "基本算法语句"
y=+3: 定义框
      "用特定语法描述算法步骤的代码语句
       是编写程序的基础"
y=-2: 五种语句图标
      [=] [IN] [OUT] [IF] [LOOP]
```

### 动画序列
| 时间 | 动作 | 持续时间 |
|------|------|---------|
| 4.0s | 标题书写 | 0.6s |
| 4.6s | 定义框淡入 | 0.8s |
| 5.4s | 五种语句图标依次出现 | 1.0s |
| 6.4s | 理解停顿 | 2.0s |

---

## Scene 3: 五种语句介绍
**时长:** 3 秒  
**目的:** 引出五种语句

### 元素布局
```
y=+6: "五种基本算法语句"
y=+2: 五个图标
      ① 赋值  ② 输入  ③ 输出  ④ 条件  ⑤ 循环
y=-3: "让我们逐个学习"
```

---

## Scene 4: 五种语句详解
**总时长:** 25 秒（每个5秒）  
**目的:** 详细讲解每种语句

### 4.1 赋值语句 (Assignment)
```
y=+6: "① 赋值语句"
y=+2: 代码框
      x = 3
      y = x + 5
y=0:  内存/变量可视化
      ┌───────┐     ┌───────┐
      │ x: 3  │     │ y: 8  │
      └───────┘     └───────┘
y=-4: "将值赋给变量，存储在内存中"
```

**动画流程:**
1. 显示代码 `x = 3`
2. 动画：数字 3 "流入" x 的内存框
3. 显示代码 `y = x + 5`
4. 动画：从 x 取值，计算 3+5=8，流入 y
5. 说明文字

**时长:** 5s（演示2s + 停顿1.5s + 过渡0.5s）

### 4.2 输入语句 (Input)
```
y=+6: "② 输入语句 INPUT"
y=+2: 代码框
      INPUT x
y=0:  输入可视化
      键盘 → [输入框: 10] → [x: 10]
y=-4: "从外部读取数据到变量"
```

**动画流程:**
1. 显示代码 `INPUT x`
2. 动画：键盘图标出现
3. 数字 10 出现在输入框
4. 数字 10 "流入" x 的内存框
5. 说明文字

**时长:** 5s

### 4.3 输出语句 (Output)
```
y=+6: "③ 输出语句 PRINT"
y=+2: 代码框
      x = 100
      PRINT x
y=0:  输出可视化
      [x: 100] → [输出框: 100] → 屏幕
y=-4: "将变量值输出到屏幕"
```

**动画流程:**
1. 显示代码 `x = 100` 和 `PRINT x`
2. x 被赋值为 100
3. 动画：数字 100 从 x 的内存框"流出"
4. 出现在输出框，然后显示在屏幕
5. 说明文字

**时长:** 5s

### 4.4 条件语句 (Conditional)
```
y=+6: "④ 条件语句 IF-THEN-ELSE"
y=+2: 代码框
      x = 5
      IF x > 0 THEN
          y = 1
      ELSE
          y = -1
      END IF
y=-1: 执行路径高亮
      x=5 → 判断 x>0? → 是 → y=1
y=-4: "根据条件执行不同代码"
```

**动画流程:**
1. 显示完整代码
2. x 被赋值为 5
3. 判断框高亮：x > 0? → 是（绿色）
4. THEN 分支高亮
5. y 被赋值为 1
6. 说明文字

**时长:** 5s

### 4.5 循环语句 (Loop)
```
y=+6: "⑤ 循环语句 FOR"
y=+2: 代码框
      sum = 0
      FOR i = 1 TO 3
          sum = sum + i
      NEXT i
y=-1: 执行过程可视化
      i=1: sum=0+1=1
      i=2: sum=1+2=3
      i=3: sum=3+3=6
y=-4: "重复执行指定次数"
```

**动画流程:**
1. 显示完整代码
2. sum 初始化为 0
3. 循环开始，i=1 高亮
4. 执行 sum=sum+i，显示计算过程
5. i=2, i=3 快速演示
6. 最终结果 sum=6
7. 说明文字

**时长:** 5s

---

## Scene 5: 综合示例 - 求和程序
**时长:** 10 秒  
**目的:** 展示多种语句的组合使用

### 程序示例
```
INPUT n
sum = 0
FOR i = 1 TO n
    sum = sum + i
NEXT i
PRINT sum
```

### 元素布局
```
y=+6: "综合示例：求和程序"
y=+2: 代码框（左侧）
y=+2: 变量追踪（右侧）
      n: 5
      sum: 0 → 1 → 3 → 6 → 10 → 15
      i: 1 → 2 → 3 → 4 → 5
y=-4: 逐步执行演示
```

### 动画流程
| 步骤 | 代码高亮 | 变量状态 | 持续时间 |
|------|----------|---------|---------|
| 1 | INPUT n | n = 5 | 1.0s |
| 2 | sum = 0 | sum = 0 | 0.5s |
| 3 | FOR i = 1 | i = 1 | 0.5s |
| 4 | sum = sum + i | sum = 1 | 0.8s |
| 5 | i = 2 | i = 2, sum = 3 | 0.6s |
| 6 | i = 3 | i = 3, sum = 6 | 0.6s |
| 7 | 快速演示 | i = 4,5 | 1.0s |
| 8 | PRINT sum | 输出: 15 | 1.0s |
| 9 | 理解停顿 | - | 2.0s |

---

## Scene 6: 五种语句回顾
**时长:** 5 秒  
**目的:** 总结五种语句

### 元素布局
```
y=+6: "五种基本算法语句"
y=+3: ① 赋值语句  x = 表达式
y=+1: ② 输入语句  INPUT 变量
y=-1: ③ 输出语句  PRINT 变量
y=-3: ④ 条件语句  IF...THEN...ELSE
y=-5: ⑤ 循环语句  FOR / WHILE
```

### 动画序列
| 时间 | 动作 | 持续时间 |
|------|------|---------|
| 47.0s | 标题出现 | 0.6s |
| 47.6s | 五种语句依次淡入 | 2.0s |
| 49.6s | 整体闪烁 | 0.8s |
| 50.4s | 理解停顿 | 1.5s |

---

## Scene 7: 片尾关注
**时长:** 4 秒  
**目的:** 引导关注

### 元素布局
```
y=+2: 作者信息放大
y=-1: "关注我，学更多编程技巧!"
周围: 代码符号装饰（{} [] () 旋转）
```

---

## 元素生命周期追踪

| 元素 | 创建场景 | 销毁场景 | 备注 |
|------|---------|---------|------|
| author_info | Scene 1 | Scene 7 | 常驻顶部 |
| hook_question | Scene 1 | Scene 1 | 仅开场 |
| definition_box | Scene 2 | Scene 2 | 定义展示 |
| statement_demos | Scene 4 | Scene 4 | 每种语句独立 |
| comprehensive_example | Scene 5 | Scene 5 | 综合示例 |
| summary_list | Scene 6 | Scene 6 | 总结回顾 |

---

## 计时预算

| 类别 | 时长 | 百分比 |
|------|------|--------|
| 开场钩子 | 4s | 6% |
| 基本语句定义 | 5s | 8% |
| 五种语句介绍 | 3s | 5% |
| 五种语句详解 | 25s | 40% |
| 综合示例 | 10s | 16% |
| 五种语句回顾 | 5s | 8% |
| 片尾关注 | 4s | 6% |
| **总计** | **~62s** | **100%** |

---

## 验证清单

### 实施前检查
- [x] 代码使用 Text() 而非 MathTex()（避免中英混合）
- [x] 场景时长合理（60-65秒）
- [x] 元素布局在安全边界内
- [x] 颜色方案一致
- [x] 动画节奏：难点2-3秒停顿

### 技术约束
- [ ] 代码显示使用等宽字体（Courier New）
- [ ] 关键字使用特殊颜色高亮
- [ ] 变量框使用矩形 + 文字
- [ ] 箭头表示数据流动
- [ ] 执行流程用高亮表示

### 特殊注意
- **代码高亮:** 需要手动实现，不能依赖语法高亮库
- **变量可视化:** 使用矩形框 + 文字标签
- **数据流动:** 使用箭头 + Transform 动画
- **执行追踪:** 逐行代码高亮 + 变量值更新

---

## 调试策略

1. **快速预览:** `manim -pql algorithm_statements.py AlgorithmStatements`
2. **检查边界:** 验证所有元素在 [-4, 4] × [-7, 7] 范围内
3. **测试节奏:** 确保关键概念有2秒以上停顿
4. **代码显示:** 确认代码字体和颜色正确
5. **变量框对齐:** 使用 arrange() 保证整齐

---

## 实施备注

**不涉及复杂几何的原因:**
- 本动画为代码语句演示，主要是文字和框的布局
- 无需精确几何计算
- 主要使用矩形、文字、箭头等基本元素

**verify_geometry.py 简化版:**
```python
# 检查内容:
# 1. 元素边界是否超出安全范围
# 2. 是否有中文出现在 MathTex 中（代码中可能有变量名）
# 3. 代码框位置是否合理
# 4. 变量框布局是否整齐
```

**关键技术点:**
```python
# 代码显示 - 使用等宽字体
code = Text("x = 3", font="Courier New", font_size=20)

# 变量框
var_box = Rectangle(width=2.5, height=1.0, color=COLOR_PRIMARY)
var_label = Text("x", font="Courier New", font_size=18)
var_value = Text("3", font="Courier New", font_size=18)
var_group = VGroup(var_box, var_label, var_value)

# 数据流动动画
arrow = Arrow(start, end, buff=0.2, color=COLOR_SUCCESS)
self.play(
    Create(arrow),
    value.animate.move_to(target_pos),
    run_time=0.8
)

# 代码高亮（改变颜色）
self.play(code_line.animate.set_color(COLOR_HIGHLIGHT), run_time=0.3)
```

**代码格式示例:**
```python
# 使用 Text() 创建代码，手动换行
code_lines = VGroup(
    Text("INPUT n", font="Courier New", font_size=18),
    Text("sum = 0", font="Courier New", font_size=18),
    Text("FOR i = 1 TO n", font="Courier New", font_size=18),
    Text("    sum = sum + i", font="Courier New", font_size=18),
    Text("NEXT i", font="Courier New", font_size=18),
    Text("PRINT sum", font="Courier New", font_size=18)
).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
```