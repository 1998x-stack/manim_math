#!/bin/bash

# Script to run manim animations in batches of 3 every 3 minutes.
# Ensure this script is executable (chmod +x script.sh) and run from the parent directory
# that contains all the listed subdirectories.

# Arrays containing the data for each item (index 0 corresponds to item 10)
dirs=(
    "高中/高一/第二学期/第五章-三角比/002任意角的三角比"
    "初中/九年级/第二学期/第二十八章-统计初步/002统计图表"
    "高中/高一/第一学期/第一章-集合与命题/002集合间的关系"
    "高中/高三/第二学期/第十八章-基本统计方法/002抽样技术"
    "初中/九年级/第二学期/第二十七章-圆与正多边形/002圆的确定"
    "初中/八年级/第一学期/第十九章-几何证明/002逆命题与逆定理"
    "高中/高二/第二学期/第十一章-坐标平面上的直线/002直线的方程"
    "高中/高一/第二学期/第四章-幂函数、指数函数和对数函数（下）/002反函数"
    "高中/高一/第一学期/第二章-不等式/003分式不等式"
    "高中/高三/第二学期/第十七章-概率论初步/003频率与概率"
    "高中/高三/第二学期/第十八章-基本统计方法/003频率分布与统计图表"
    "初中/八年级/第一学期/第十八章-正比例函数和反比例函数/003反比例函数"
    "高中/高一/第二学期/第四章-幂函数、指数函数和对数函数（下）/003对数函数"
    "高中/高三/第一学期/第十五章-简单几何体/004棱台"
    "高中/高一/第一学期/第二章-不等式/004含绝对值不等式"
    "高中/高一/第二学期/第五章-三角比/004两角和与差的三角函数"
    "高中/高二/第二学期/第十三章-复数/004复数的平方根与立方根"
    "初中/八年级/第二学期/第二十二章-四边形/004矩形的性质与判定"
    "高中/高三/第二学期/第十八章-基本统计方法/004数据的集中趋势"
    "初中/八年级/第一学期/第十八章-正比例函数和反比例函数/004待定系数法"
    "初中/八年级/第一学期/第十九章-几何证明/004线段垂直平分线的性质与判定"
    "初中/八年级/第二学期/第二十章-一次函数/004待定系数法求一次函数解析式"
    "初中/六年级/第二学期/第六章-一次方程（组）和一次不等式（组）/004一元一次不等式"
    "高中/高一/第二学期/第四章-幂函数、指数函数和对数函数（下）/004指数方程和对数方程"
    "初中/七年级/第二学期/第十二章-实数/005实数的运算"
    "高中/高一/第二学期/第六章-三角函数/005最简三角方程"
    "高中/高一/第二学期/第五章-三角比/005二倍角与半角公式"
    "高中/高二/第二学期/第十三章-复数/005实系数一元二次方程"
    "高中/高一/第一学期/第三章-函数的基本性质/005函数的奇偶性"
    "初中/八年级/第二学期/第二十二章-四边形/005菱形的性质与判定"
    "高中/高一/第一学期/第二章-不等式/005基本不等式（均值不等式）"
    "高中/高三/第二学期/第十七章-概率论初步/005条件概率与独立事件"
    "初中/八年级/第一学期/第十九章-几何证明/005角平分线的性质与判定"
    "初中/六年级/第二学期/第八章-长方体的再认识/005平面与平面的位置关系"
    "初中/八年级/第二学期/第二十章-一次函数/005一次函数与方程、不等式的关系"
    "高中/高一/第二学期/第五章-三角比/006正弦定理"
    "初中/七年级/第二学期/第十二章-实数/006分数指数幂"
    "高中/高一/第一学期/第二章-不等式/006不等式的证明"
    "高中/高三/第二学期/第十八章-基本统计方法/006统计估计"
    "高中/高一/第一学期/第三章-函数的基本性质/006函数的最值"
    "初中/八年级/第一学期/第十七章-一元二次方程/006根的判别式"
    "初中/六年级/第一学期/第二章-分数/007分数的乘法"
    "高中/高三/第二学期/第十八章-基本统计方法/007线性回归"
    "初中/八年级/第一学期/第十七章-一元二次方程/007根与系数的关系（韦达定理）"
    "高中/高三/第二学期/第十八章-基本统计方法/008统计案例分析"
    "高中/高二/第二学期/第十二章-圆锥曲线/008抛物线的几何性质"
    "初中/六年级/第二学期/第五章-有理数/009有理数的除法"
    "初中/六年级/第一学期/第二章-分数/009分数与小数的互化"
    "初中/六年级/第二学期/第五章-有理数/010有理数的乘方"
    "初中/八年级/第二学期/第二十二章-四边形/010向量的加法与减法"
    "初中/六年级/第二学期/第五章-有理数/011有理数混合运算"
    "初中/九年级/第二学期/第二十七章-圆与正多边形/011弧长与扇形面积"
)

python_files=(
    "any_angle_trigonometry.py"
    "statistical_charts.py"
    "set_relations.py"
    "sampling_techniques_animation.py"
    "circle_determination.py"
    "inverse_propositions.py"
    "line_equations.py"
    "inverse_functions.py"
    "fractional_inequalities.py"
    "freq_prob_animation.py"
    "freq_dist_animation.py"
    "inverse_proportion.py"
    "logarithm_function.py"
    "frustum_lesson.py"
    "AbsoluteValueInequalitiesAnimation.py"
    "sum_difference_angles.py"
    "complex_roots.py"
    "rectangle_properties.py"
    "central_tendency_animation.py"
    "undetermined_coeff.py"
    "perpendicular_bisector.py"
    "linear_function_undetermined_coefficients.py"
    "linear_inequality.py"
    "exponential_logarithmic.py"
    "real_number_ops.py"
    "simplest_trig_equations.py"
    "double_angle_formulas.py"
    "complex_quadratic.py"
    "function_parity.py"
    "rhombus_properties.py"
    "005_基本不等式（均值不等式）.py"
    "cond_prob_animation.py"
    "angle_bisector.py"
    "verify_geometry.py"
    "linear_function_equation_inequality.py"
    "006_正弦定理.py"
    "frac_exponent.py"
    "InequalityProofsAnimation.py"
    "stat_estimation.py"
    "function_max_min.py"
    "quadratic_discriminant.py"
    "fraction_multiplication.py"
    "linear_regression.py"
    "vieta_formulas.py"
    "chi_square.py"
    "parabola_properties.py"
    "rational_division.py"
    "fraction_decimal.py"
    "power_of_numbers.py"
    "vector_addition_subtraction.py"
    "rational_number_mixed_operations.py"
    "arc_length_sector_area.py"
)

scene_names=(
    "AnyAngleTrigonometry"
    "StatisticalCharts"
    "SetRelations"
    "SamplingTechniquesAnimation"
    "CircleDetermination"
    "InversePropositions"
    "LineEquations"
    "InverseFunctions"
    "FractionalInequalities"
    "FreqProbAnimation"
    "FreqDistAnimation"
    "InverseProportion"
    "LogarithmFunction"
    "FrustumLesson"
    "AbsoluteValueInequalitiesAnimation"
    "SumDifferenceAngles"
    "ComplexRoots"
    "RectangleProperties"
    "CentralTendencyAnimation"
    "UndeterminedCoeff"
    "PerpendicularBisector"
    "LinearFunctionUndeterminedCoefficients"
    "LinearInequality"
    "ExponentialLogarithmic"
    "RealNumberOps"
    "SimplestTrigEquations"
    "DoubleAngleFormulas"
    "ComplexQuadratic"
    "FunctionParity"
    "RhombusProperties"
    "BasicInequality"
    "CondProbAnimation"
    "AngleBisector"
    "VerifyGeometry"
    "LinearFunctionEquationInequality"
    "SineTheorem"
    "FracExponent"
    "InequalityProofsAnimation"
    "StatEstimation"
    "FunctionMaxMin"
    "QuadraticDiscriminant"
    "FractionMultiplication"
    "LinearRegression"
    "VietaFormulas"
    "ChiSquare"
    "ParabolaProperties"
    "RationalDivision"
    "FractionDecimal"
    "PowerOfNumbers"
    "VectorAdditionSubtraction"
    "RationalNumberMixedOperations"
    "ArcLengthSectorArea"
)

# Check that arrays have the same length
if [ ${#dirs[@]} -ne ${#python_files[@]} ] || [ ${#dirs[@]} -ne ${#scene_names[@]} ]; then
    echo "Error: Array lengths do not match."
    exit 1
fi

total=${#dirs[@]}
echo "Starting processing of $total items in batches of 3, with 3-minute pauses."

for (( i=0; i<total; i++ )); do
    # After every 3 jobs (except the first batch), sleep for 3 minutes
    if [ $i -ne 0 ] && [ $((i % 3)) -eq 0 ]; then
        echo "Completed batch $((i/3)). Sleeping for 3 minutes (180 seconds)..."
        sleep 180
    fi

    dir="${dirs[i]}"
    pyfile="${python_files[i]}"
    scene="${scene_names[i]}"

    echo "[$((i+1))/$total] Launching in directory: $dir"
    echo "        Command: nohup manim -qh $pyfile $scene > nohup.log 2>&1 &"

    # Change to the directory and run the command
    # Use a subshell to avoid changing the working directory of the main script
    (
        if cd "$dir"; then
            nohup manim -qh "$pyfile" "$scene" > nohup.log 2>&1 &
            echo "        Launched PID $!"
        else
            echo "        ERROR: Could not cd into $dir" >&2
        fi
    ) &
    # The subshell itself is backgrounded so the loop continues immediately
    # This ensures all 3 jobs are launched without waiting for cd to finish,
    # but that's fine because cd is fast.
done

echo "All jobs have been scheduled. They will run in the background."
echo "Check individual nohup.log files in each directory for output."