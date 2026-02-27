# TODO1: Processing Directories with Python files over 200 lines

## Bug Fixing Protocol
- If manim process fails due to code error (no MP4 generated):
  1. Check the error in the nohup log
  2. Read the Python code to identify the bug
  3. Fix the Python code
  4. Re-run the manim command
  5. Do NOT retry without fixing the code first

## Process Flow

# TODO1: Directories with Python files over 200 lines

## Overview
These directories have existing Python files exceeding 200 lines that need to be executed with Manim to generate MP4 files. 
For each directory:
1. Run the Python file(s) with Manim in the background using nohup
2. Monitor the output log for errors
- [ ] 4. 高中/高三/第二学期/第十七章-概率论初步/001随机事件与概率 - Processing (code fixed: interpolate_color issue)
4. Rerun until successful
5. Move the generated MP4 to the same directory
6. After completing this phase, read TODO2.md

## Directory Processing List

## Progress Tracking

- [x] 1. 初中/八年级/第一学期/第十九章-几何证明/001命题与证明 - Completed
- [x] 2. 高中/高三/第二学期/第十八章-基本统计方法/001总体与样本 - Completed
- [x] 3. 初中/八年级/第二学期/第二十章-一次函数/001一次函数的概念 - Completed (code fixed: removed Chinese chars from MathTex to fix LaTeX error)
- [x] 4. 高中/高三/第二学期/第十七章-概率论初步/001随机事件与概率 - Completed (code fixed: interpolate_color issue)
- [x] 5. 初中/六年级/第二学期/第八章-长方体的再认识/001长方体的基本元素 - Completed (code fixed: get_points issue)
- [x] 6. 高中/高二/第二学期/第十一章-坐标平面上的直线/001直线的倾斜角与斜率 - Completed (code fixed: replaced Chinese chars in MathTex to fix LaTeX error)
- [x] 7. 高中/高一/第二学期/第四章-幂函数、指数函数和对数函数（下）/001对数的概念与运算 - Completed
- [ ] 8. 高中/高三/第一学期/第十五章-简单几何体/002棱柱 - Processing
- [ ] 9. 高中/高一/第一学期/第二章-不等式/002一元二次不等式 - Processing (code fixed: fixed syntax error after replacing inline lambdas with class methods)
- [x] 10. 高中/高一/第二学期/第五章-三角比/002任意角的三角比 - Completed (code fixed: simplified rotation demo to avoid complex path/index errors)
- [ ] 11. 初中/九年级/第二学期/第二十八章-统计初步/002统计图表 - Processing (retry after LaTeX error)
- [ ] 12. 高中/高一/第一学期/第一章-集合与命题/002集合间的关系 - Processing
- [ ] 13. 高中/高三/第二学期/第十八章-基本统计方法/002抽样技术 - Processing
- [ ] 14. 初中/九年级/第二学期/第二十七章-圆与正多边形/002圆的确定
- [ ] 15. 初中/八年级/第一学期/第十九章-几何证明/002逆命题与逆定理
- [ ] 16. 高中/高二/第二学期/第十一章-坐标平面上的直线/002直线的方程
- [ ] 17. 高中/高一/第二学期/第四章-幂函数、指数函数和对数函数（下）/002反函数
- [ ] 18. 高中/高一/第一学期/第二章-不等式/003分式不等式
- [ ] 19. 高中/高三/第二学期/第十七章-概率论初步/003频率与概率
- [ ] 20. 高中/高三/第二学期/第十八章-基本统计方法/003频率分布与统计图表
- [ ] 21. 初中/八年级/第一学期/第十八章-正比例函数和反比例函数/003反比例函数
- [ ] 22. 高中/高一/第二学期/第四章-幂函数、指数函数和对数函数（下）/003对数函数
- [ ] 23. 高中/高三/第一学期/第十五章-简单几何体/004棱台
- [ ] 24. 高中/高一/第一学期/第二章-不等式/004含绝对值不等式
- [ ] 25. 高中/高一/第二学期/第五章-三角比/004两角和与差的三角函数
- [ ] 26. 高中/高二/第二学期/第十三章-复数/004复数的平方根与立方根
- [ ] 27. 初中/八年级/第二学期/第二十二章-四边形/004矩形的性质与判定
- [ ] 28. 高中/高三/第二学期/第十八章-基本统计方法/004数据的集中趋势
- [ ] 29. 初中/八年级/第一学期/第十八章-正比例函数和反比例函数/004待定系数法
- [ ] 30. 初中/八年级/第一学期/第十九章-几何证明/004线段垂直平分线的性质与判定

Now continuing with remaining items:

- [ ] 31. 初中/八年级/第二学期/第二十章-一次函数/004待定系数法求一次函数解析式
- [ ] 32. 初中/六年级/第二学期/第六章-一次方程（组）和一次不等式（组）/004一元一次不等式
- [ ] 33. 高中/高一/第二学期/第四章-幂函数、指数函数和对数函数（下）/004指数方程和对数方程
- [ ] 34. 初中/七年级/第二学期/第十二章-实数/005实数的运算
- [ ] 35. 高中/高一/第二学期/第六章-三角函数/005最简三角方程
- [ ] 36. 高中/高一/第二学期/第五章-三角比/005二倍角与半角公式
- [ ] 37. 高中/高二/第二学期/第十三章-复数/005实系数一元二次方程
- [ ] 38. 高中/高一/第一学期/第三章-函数的基本性质/005函数的奇偶性
- [ ] 39. 初中/八年级/第二学期/第二十二章-四边形/005菱形的性质与判定
- [ ] 40. 高中/高一/第一学期/第二章-不等式/005基本不等式（均值不等式）
- [ ] 41. 高中/高三/第二学期/第十七章-概率论初步/005条件概率与独立事件
- [ ] 42. 初中/八年级/第一学期/第十九章-几何证明/005角平分线的性质与判定
- [ ] 43. 初中/六年级/第二学期/第八章-长方体的再认识/005平面与平面的位置关系
- [ ] 44. 初中/八年级/第二学期/第二十章-一次函数/005一次函数与方程、不等式的关系
- [ ] 45. 高中/高一/第二学期/第五章-三角比/006正弦定理
- [ ] 46. 初中/七年级/第二学期/第十二章-实数/006分数指数幂
- [ ] 47. 高中/高一/第一学期/第二章-不等式/006不等式的证明
- [ ] 48. 高中/高三/第二学期/第十八章-基本统计方法/006统计估计
- [ ] 49. 高中/高一/第一学期/第三章-函数的基本性质/006函数的最值
- [ ] 50. 初中/八年级/第一学期/第十七章-一元二次方程/006根的判别式
- [ ] 51. 初中/六年级/第一学期/第二章-分数/007分数的乘法
- [ ] 52. 高中/高三/第二学期/第十八章-基本统计方法/007线性回归
- [ ] 53. 初中/八年级/第一学期/第十七章-一元二次方程/007根与系数的关系（韦达定理）
- [ ] 54. 高中/高三/第二学期/第十八章-基本统计方法/008统计案例分析
- [ ] 55. 高中/高二/第二学期/第十二章-圆锥曲线/008抛物线的几何性质
- [ ] 56. 初中/六年级/第二学期/第五章-有理数/009有理数的除法
- [ ] 57. 初中/六年级/第一学期/第二章-分数/009分数与小数的互化
- [ ] 58. 初中/六年级/第二学期/第五章-有理数/010有理数的乘方
- [ ] 59. 初中/八年级/第二学期/第二十二章-四边形/010向量的加法与减法
- [ ] 60. 初中/六年级/第二学期/第五章-有理数/011有理数混合运算
- [ ] 61. 初中/九年级/第二学期/第二十七章-圆与正多边形/011弧长与扇形面积

---

## Instructions
1. Read this file to see current progress
2. For each unchecked item, execute the appropriate manim command
3. Mark as [x] when completed
4. Continue until all are marked as completed
5. Then proceed to read and execute TODO2.md
- Command: `nohup manim -qh quadratic_inequality.py QuadraticInequality > nohup.log 2>&1 &`

### 10. 高中/高一/第二学期/第五章-三角比/002任意角的三角比
- Python file: any_angle_trigonometry.py (1067 lines)
- Command: `nohup manim -qh any_angle_trigonometry.py AnyAngleTrigonometry > nohup.log 2>&1 &`

### 11. 初中/九年级/第二学期/第二十八章-统计初步/002统计图表
- Python file: statistical_charts.py (912 lines)
- Command: `nohup manim -qh statistical_charts.py StatisticalCharts > nohup.log 2>&1 &`

### 12. 高中/高一/第一学期/第一章-集合与命题/002集合间的关系
- Python files: verify_sets.py (215 lines), set_relations.py (978 lines)
- Command: `nohup manim -qh set_relations.py SetRelations > nohup.log 2>&1 &`

### 13. 高中/高三/第二学期/第十八章-基本统计方法/002抽样技术
- Python file: sampling_techniques_animation.py (644 lines)
- Command: `nohup manim -qh sampling_techniques_animation.py SamplingTechniquesAnimation > nohup.log 2>&1 &`

### 14. 初中/九年级/第二学期/第二十七章-圆与正多边形/002圆的确定
- Python file: circle_determination.py (797 lines)
- Command: `nohup manim -qh circle_determination.py CircleDetermination > nohup.log 2>&1 &`

### 15. 初中/八年级/第一学期/第十九章-几何证明/002逆命题与逆定理
- Python file: inverse_propositions.py (880 lines)
- Command: `nohup manim -qh inverse_propositions.py InversePropositions > nohup.log 2>&1 &`

### 16. 高中/高二/第二学期/第十一章-坐标平面上的直线/002直线的方程
- Python file: line_equations.py (632 lines)
- Command: `nohup manim -qh line_equations.py LineEquations > nohup.log 2>&1 &`

### 17. 高中/高一/第二学期/第四章-幂函数、指数函数和对数函数（下）/002反函数
- Python file: inverse_functions.py (908 lines)
- Command: `nohup manim -qh inverse_functions.py InverseFunctions > nohup.log 2>&1 &`

### 18. 高中/高一/第一学期/第二章-不等式/003分式不等式
- Python files: fractional_inequalities.py (564 lines), verify_geometry.py (172 lines)
- Command: `nohup manim -qh fractional_inequalities.py FractionalInequalities > nohup.log 2>&1 &`

### 19. 高中/高三/第二学期/第十七章-概率论初步/003频率与概率
- Python file: freq_prob_animation.py (722 lines)
- Command: `nohup manim -qh freq_prob_animation.py FreqProbAnimation > nohup.log 2>&1 &`

### 20. 高中/高三/第二学期/第十八章-基本统计方法/003频率分布与统计图表
- Python file: freq_dist_animation.py (753 lines)
- Command: `nohup manim -qh freq_dist_animation.py FreqDistAnimation > nohup.log 2>&1 &`

### 21. 初中/八年级/第一学期/第十八章-正比例函数和反比例函数/003反比例函数
- Python file: inverse_proportion.py (372 lines)
- Command: `nohup manim -qh inverse_proportion.py InverseProportion > nohup.log 2>&1 &`

### 22. 高中/高一/第二学期/第四章-幂函数、指数函数和对数函数（下）/003对数函数
- Python file: logarithm_function.py (657 lines)
- Command: `nohup manim -qh logarithm_function.py LogarithmFunction > nohup.log 2>&1 &`

### 23. 高中/高三/第一学期/第十五章-简单几何体/004棱台
- Python file: frustum_lesson.py (703 lines)
- Command: `nohup manim -qh frustum_lesson.py FrustumLesson > nohup.log 2>&1 &`

### 24. 高中/高一/第一学期/第二章-不等式/004含绝对值不等式
- Python files: absolute_value_inequalities.py (523 lines), verify_geometry.py (331 lines), AbsoluteValueInequalitiesAnimation.py (527 lines), AbsoluteValueInequalities.py (519 lines)
- Command: `nohup manim -qh AbsoluteValueInequalitiesAnimation.py AbsoluteValueInequalitiesAnimation > nohup.log 2>&1 &`

### 25. 高中/高一/第二学期/第五章-三角比/004两角和与差的三角函数
- Python file: sum_difference_angles.py (863 lines)
- Command: `nohup manim -qh sum_difference_angles.py SumDifferenceAngles > nohup.log 2>&1 &`

### 26. 高中/高二/第二学期/第十三章-复数/004复数的平方根与立方根
- Python file: complex_roots.py (552 lines)
- Command: `nohup manim -qh complex_roots.py ComplexRoots > nohup.log 2>&1 &`

### 27. 初中/八年级/第二学期/第二十二章-四边形/004矩形的性质与判定
- Python file: rectangle_properties.py (456 lines)
- Command: `nohup manim -qh rectangle_properties.py RectangleProperties > nohup.log 2>&1 &`

### 28. 高中/高三/第二学期/第十八章-基本统计方法/004数据的集中趋势
- Python file: central_tendency_animation.py (795 lines)
- Command: `nohup manim -qh central_tendency_animation.py CentralTendencyAnimation > nohup.log 2>&1 &`

### 29. 初中/八年级/第一学期/第十八章-正比例函数和反比例函数/004待定系数法
- Python file: undetermined_coeff.py (396 lines)
- Command: `nohup manim -qh undetermined_coeff.py UndeterminedCoeff > nohup.log 2>&1 &`

### 30. 初中/八年级/第一学期/第十九章-几何证明/004线段垂直平分线的性质与判定
- Python file: perpendicular_bisector.py (693 lines)
- Command: `nohup manim -qh perpendicular_bisector.py PerpendicularBisector > nohup.log 2>&1 &`

### 31. 初中/八年级/第二学期/第二十章-一次函数/004待定系数法求一次函数解析式
- Python file: linear_function_undetermined_coefficients.py (812 lines)
- Command: `nohup manim -qh linear_function_undetermined_coefficients.py LinearFunctionUndeterminedCoefficients > nohup.log 2>&1 &`

### 32. 初中/六年级/第二学期/第六章-一次方程（组）和一次不等式（组）/004一元一次不等式
- Python file: linear_inequality.py (718 lines)
- Command: `nohup manim -qh linear_inequality.py LinearInequality > nohup.log 2>&1 &`

### 33. 高中/高一/第二学期/第四章-幂函数、指数函数和对数函数（下）/004指数方程和对数方程
- Python file: exponential_logarithmic.py (773 lines)
- Command: `nohup manim -qh exponential_logarithmic.py ExponentialLogarithmic > nohup.log 2>&1 &`

### 34. 初中/七年级/第二学期/第十二章-实数/005实数的运算
- Python file: real_number_ops.py (567 lines)
- Command: `nohup manim -qh real_number_ops.py RealNumberOps > nohup.log 2>&1 &`

### 35. 高中/高一/第二学期/第六章-三角函数/005最简三角方程
- Python file: simplest_trig_equations.py (786 lines)
- Command: `nohup manim -qh simplest_trig_equations.py SimplestTrigEquations > nohup.log 2>&1 &`

### 36. 高中/高一/第二学期/第五章-三角比/005二倍角与半角公式
- Python file: double_angle_formulas.py (839 lines)
- Command: `nohup manim -qh double_angle_formulas.py DoubleAngleFormulas > nohup.log 2>&1 &`

### 37. 高中/高二/第二学期/第十三章-复数/005实系数一元二次方程
- Python file: complex_quadratic.py (541 lines)
- Command: `nohup manim -qh complex_quadratic.py ComplexQuadratic > nohup.log 2>&1 &`

### 38. 高中/高一/第一学期/第三章-函数的基本性质/005函数的奇偶性
- Python file: function_parity.py (1177 lines)
- Command: `nohup manim -qh function_parity.py FunctionParity > nohup.log 2>&1 &`

### 39. 初中/八年级/第二学期/第二十二章-四边形/005菱形的性质与判定
- Python file: rhombus_properties.py (528 lines)
- Command: `nohup manim -qh rhombus_properties.py RhombusProperties > nohup.log 2>&1 &`

### 40. 高中/高一/第一学期/第二章-不等式/005基本不等式（均值不等式）
- Python files: 005_基本不等式（均值不等式）.py (514 lines), verify_geometry.py (313 lines)
- Command: `nohup manim -qh 005_基本不等式（均值不等式）.py BasicInequality > nohup.log 2>&1 &`

### 41. 高中/高三/第二学期/第十七章-概率论初步/005条件概率与独立事件
- Python file: cond_prob_animation.py (705 lines)
- Command: `nohup manim -qh cond_prob_animation.py CondProbAnimation > nohup.log 2>&1 &`

### 42. 初中/八年级/第一学期/第十九章-几何证明/005角平分线的性质与判定
- Python file: angle_bisector.py (702 lines)
- Command: `nohup manim -qh angle_bisector.py AngleBisector > nohup.log 2>&1 &`

### 43. 初中/六年级/第二学期/第八章-长方体的再认识/005平面与平面的位置关系
- Python files: verify_geometry.py (223 lines), 005_平面与平面的位置关系.py (130 lines)
- Command: `nohup manim -qh verify_geometry.py VerifyGeometry > nohup.log 2>&1 &`

### 44. 初中/八年级/第二学期/第二十章-一次函数/005一次函数与方程、不等式的关系
- Python file: linear_function_equation_inequality.py (756 lines)
- Command: `nohup manim -qh linear_function_equation_inequality.py LinearFunctionEquationInequality > nohup.log 2>&1 &`

### 45. 高中/高一/第二学期/第五章-三角比/006正弦定理
- Python file: 006_正弦定理.py (715 lines)
- Command: `nohup manim -qh 006_正弦定理.py SineTheorem > nohup.log 2>&1 &`

### 46. 初中/七年级/第二学期/第十二章-实数/006分数指数幂
- Python file: frac_exponent.py (592 lines)
- Command: `nohup manim -qh frac_exponent.py FracExponent > nohup.log 2>&1 &`

### 47. 高中/高一/第一学期/第二章-不等式/006不等式的证明
- Python files: verify_geometry.py (304 lines), InequalityProofsAnimation.py (521 lines)
- Command: `nohup manim -qh InequalityProofsAnimation.py InequalityProofsAnimation > nohup.log 2>&1 &`

### 48. 高中/高三/第二学期/第十八章-基本统计方法/006统计估计
- Python file: stat_estimation.py (668 lines)
- Command: `nohup manim -qh stat_estimation.py StatEstimation > nohup.log 2>&1 &`

### 49. 高中/高一/第一学期/第三章-函数的基本性质/006函数的最值
- Python file: function_max_min.py (661 lines)
- Command: `nohup manim -qh function_max_min.py FunctionMaxMin > nohup.log 2>&1 &`

### 50. 初中/八年级/第一学期/第十七章-一元二次方程/006根的判别式
- Python file: quadratic_discriminant.py (951 lines)
- Command: `nohup manim -qh quadratic_discriminant.py QuadraticDiscriminant > nohup.log 2>&1 &`

### 51. 初中/六年级/第一学期/第二章-分数/007分数的乘法
- Python file: fraction_multiplication.py (945 lines)
- Command: `nohup manim -qh fraction_multiplication.py FractionMultiplication > nohup.log 2>&1 &`

### 52. 高中/高三/第二学期/第十八章-基本统计方法/007线性回归
- Python file: linear_regression.py (636 lines)
- Command: `nohup manim -qh linear_regression.py LinearRegression > nohup.log 2>&1 &`

### 53. 初中/八年级/第一学期/第十七章-一元二次方程/007根与系数的关系（韦达定理）
- Python file: vieta_formulas.py (742 lines)
- Command: `nohup manim -qh vieta_formulas.py VietaFormulas > nohup.log 2>&1 &`

### 54. 高中/高三/第二学期/第十八章-基本统计方法/008统计案例分析
- Python file: chi_square.py (792 lines)
- Command: `nohup manim -qh chi_square.py ChiSquare > nohup.log 2>&1 &`

### 55. 高中/高二/第二学期/第十二章-圆锥曲线/008抛物线的几何性质
- Python file: parabola_properties.py (910 lines)
- Command: `nohup manim -qh parabola_properties.py ParabolaProperties > nohup.log 2>&1 &`

### 56. 初中/六年级/第二学期/第五章-有理数/009有理数的除法
- Python file: rational_division.py (844 lines)
- Command: `nohup manim -qh rational_division.py RationalDivision > nohup.log 2>&1 &`

### 57. 初中/六年级/第一学期/第二章-分数/009分数与小数的互化
- Python file: fraction_decimal.py (965 lines)
- Command: `nohup manim -qh fraction_decimal.py FractionDecimal > nohup.log 2>&1 &`

### 58. 初中/六年级/第二学期/第五章-有理数/010有理数的乘方
- Python file: power_of_numbers.py (756 lines)
- Command: `nohup manim -qh power_of_numbers.py PowerOfNumbers > nohup.log 2>&1 &`

### 59. 初中/八年级/第二学期/第二十二章-四边形/010向量的加法与减法
- Python file: vector_addition_subtraction.py (989 lines)
- Command: `nohup manim -qh vector_addition_subtraction.py VectorAdditionSubtraction > nohup.log 2>&1 &`

### 60. 初中/六年级/第二学期/第五章-有理数/011有理数混合运算
- Python file: rational_number_mixed_operations.py (950 lines)
- Command: `nohup manim -qh rational_number_mixed_operations.py RationalNumberMixedOperations > nohup.log 2>&1 &`

### 61. 初中/九年级/第二学期/第二十七章-圆与正多边形/011弧长与扇形面积
- Python file: arc_length_sector_area.py (1068 lines)
- Command: `nohup manim -qh arc_length_sector_area.py ArcLengthSectorArea > nohup.log 2>&1 &`

---

## Next Steps
After completing all items in this list, proceed to read and follow the instructions in TODO2.md.