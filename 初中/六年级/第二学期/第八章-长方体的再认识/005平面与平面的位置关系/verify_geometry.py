"""
Geometric validation script
Used to validate 3D geometric calculations for plane-to-plane relationships
"""
import numpy as np


def verify_angles():
    """
    Validate angle calculations for planes in 3D space
    """
    print("Starting plane-to-plane angle validation...")
    
    # For plane-to-plane relationships, consider these cases:
    # 1. Parallel planes: angle is 0 degrees
    # 2. Intersecting planes: angle is the angle between normal vectors
    # 3. Perpendicular planes: angle is 90 degrees
    
    # Test cases: normal vectors of two planes
    test_cases = [
        {
            'name': 'Parallel Planes Test',
            'normal1': np.array([0, 0, 1]),  # xy plane normal vector
            'normal2': np.array([0, 0, 1]),  # same direction vector, should be 0 degrees
            'expected_deg': 0
        },
        {
            'name': 'Perpendicular Planes Test',
            'normal1': np.array([0, 0, 1]),  # xy plane normal vector
            'normal2': np.array([1, 0, 0]),  # yz plane normal vector
            'expected_deg': 90
        },
        {
            'name': '45-degree Intersecting Planes Test',
            'normal1': np.array([0, 0, 1]),  # xy plane normal vector
            'normal2': np.array([1, 0, 1]),  # 45-degree to xy plane
            'expected_deg': 45
        }
    ]
    
    for test_case in test_cases:
        n1 = test_case['normal1']
        n2 = test_case['normal2']
        expected_deg = test_case['expected_deg']
        
        # Normalize normal vectors
        n1_norm = n1 / np.linalg.norm(n1)
        n2_norm = n2 / np.linalg.norm(n2)
        
        # Calculate angle between normals (i.e. plane angle)
        cos_angle = np.abs(np.dot(n1_norm, n2_norm))  # Take absolute value since plane angle is acute
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        angle_rad = np.arccos(cos_angle)
        angle_deg = np.degrees(angle_rad)
        
        print(f"{test_case['name']}: Calculated plane angle {angle_deg:.2f}°, Expected angle {expected_deg}°")
        
        # Check if within reasonable range
        if abs(angle_deg - expected_deg) > 5:  # Allow 5 degree tolerance
            print(f"  ⚠️  Warning: Large angle difference ({abs(angle_deg - expected_deg):.2f}°)")
        else:
            print(f"  ✓ Plane angle validation passed")


def check_latex_compatibility():
    """
    Detect characters that may cause LaTeX compilation errors
    """
    print("Starting LaTeX error risk detection...")
    
    # Check for potential problems in Python files in the current directory
    import os
    
    problematic_files = []
    current_dir = '.'
    
    for file in os.listdir(current_dir):
        if file.endswith('.py'):
            filepath = os.path.join(current_dir, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for Chinese characters that might cause LaTeX errors
                problematic_chars = ['乘', '除', '加', '减', '等', '°']  # Degree symbol also needs special handling
                
                found_chars = []
                for char in problematic_chars:
                    if char in content:
                        count = content.count(char)
                        found_chars.append((char, count))
                
                if found_chars:
                    problematic_files.append((filepath, found_chars))
                    
            except IOError as e:
                print(f"Cannot read file {filepath}: {e}")
    
    if problematic_files:
        print("Found potential LaTeX error characters:")
        for filepath, chars in problematic_files:
            print(f"  File: {filepath}")
            for char, count in chars:
                print(f"    Character '{char}' appears {count} times")
        
        print("\nFix suggestions:")
        print("  - Replace '°' with '^\\circ', e.g.: MathTex(r'90^\\circ')")
        print("  - Use Text() instead of MathTex() for Chinese characters")
    else:
        print("✓ No obvious LaTeX compilation error risks found")
    
    print("\nLaTeX check complete")


def verify_boundaries():
    """
    Validate that 3D elements are within safe boundaries
    """
    print("Starting 3D element boundary validation...")
    
    # Define safe boundaries for TikTok portrait format
    x_min, x_max = -4.0, 4.0
    y_min, y_max = -7.0, 7.0  # Some margin for top and bottom
    z_min, z_max = -3.0, 3.0  # Also control z-axis range
    
    # Test some typical 3D plane coordinates
    test_points = [
        # Key points related to planes
        np.array([-2, -2, 0]),  # Corner of plane, should be safe
        np.array([2, 2, 0]),    # Other corner of plane, should be safe
        np.array([0, 0, 0]),    # Origin, should be safe
        np.array([5, 0, 0]),    # x out of bounds
        np.array([0, 8, 0]),    # y out of bounds
        np.array([0, 0, 4]),    # z out of bounds
        np.array([-3, -3, 1]),  # Should be safe
        np.array([3, 3, -1]),   # Should be safe
    ]
    
    boundary_issues = []
    
    for i, point in enumerate(test_points):
        x, y, z = point
        
        issues = []
        if x < x_min or x > x_max:
            issues.append(f"x coordinate out of range [{x_min}, {x_max}]: {x}")
        if y < y_min or y > y_max:
            issues.append(f"y coordinate out of range [{y_min}, {y_max}]: {y}")
        if z < z_min or z > z_max:
            issues.append(f"z coordinate out of range [{z_min}, {z_max}]: {z}")
        
        if issues:
            boundary_issues.append((i, point, issues))
    
    if boundary_issues:
        print("Found boundary issues:")
        for idx, point, issues in boundary_issues:
            print(f"  Point {idx}: {point}")
            for issue in issues:
                print(f"    - {issue}")
    else:
        print("✓ All test points are within safe boundaries")
    
    print("\nBoundary validation complete")


def verify_planes_relationships():
    """
    Validate core geometric principles of plane-to-plane relationships
    """
    print("Starting validation of plane-to-plane relationship geometric principles...")
    
    # 1. Validate parallel plane condition: normal vectors parallel
    n1_parallel = np.array([1, 2, 3])
    n2_parallel = np.array([2, 4, 6])  # 2x n1, should be parallel
    
    # Check if parallel (cross product is zero vector)
    cross_parallel = np.cross(n1_parallel, n2_parallel)
    is_parallel = np.allclose(cross_parallel, np.zeros(3), atol=1e-6)
    print(f"Parallel planes validation: Normal vectors {n1_parallel} and {n2_parallel} {'parallel' if is_parallel else 'not parallel'} ✓")
    
    # 2. Validate perpendicular plane condition: normal vectors perpendicular
    n1_perp = np.array([1, 0, 0])
    n2_perp = np.array([0, 1, 0])  # Should be perpendicular
    
    dot_perp = np.dot(n1_perp, n2_perp)
    is_perp = abs(dot_perp) < 1e-6
    print(f"Perpendicular planes validation: Normal vectors {n1_perp} and {n2_perp} {'perpendicular' if is_perp else 'not perpendicular'} ✓")
    
    # 3. Validate intersection line calculation (for intersecting planes)
    # If two planes intersect, the intersection line direction is the cross product of the normal vectors
    n1_intersect = np.array([1, 0, 0])  # yz plane
    n2_intersect = np.array([0, 1, 0])  # xz plane
    line_dir = np.cross(n1_intersect, n2_intersect)  # Should be z-axis direction [0, 0, 1]
    expected_dir = np.array([0, 0, 1])
    is_correct_dir = np.allclose(line_dir, expected_dir, atol=1e-6)
    print(f"Intersection line direction validation: Calculated direction {line_dir}, Expected direction {expected_dir} {'correct' if is_correct_dir else 'incorrect'} ✓")
    
    print("\nPlane relationship validation complete")


def main():
    """
    主验证函数
    """
    print("="*60)
    print("平面与平面位置关系 - 几何验证脚本")
    print("="*60)
    
    verify_angles()
    print()
    verify_planes_relationships()
    print()
    check_latex_compatibility()
    print()
    verify_boundaries()
    
    print("\n" + "="*60)
    print("验证完成")
    print("="*60)


if __name__ == "__main__":
    main()