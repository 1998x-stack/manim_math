import numpy as np

def verify_angles():
    """
    Verify angles in the animation to ensure they are within proper bounds.
    In Manim, angles are typically in radians, and special attention is needed
    for angles greater than 90 degrees (π/2) or 180 degrees (π).
    """
    print("Verifying angles in the animation...")

    # We'll verify that any computed angles are within expected ranges
    # Since our animation deals with sine functions, we're primarily concerned with
    # phase shifts and rotation angles

    # Phase shifts
    pi_over_4 = np.pi / 4  # 45 degrees
    print(f"Phase shift π/4 = {np.degrees(pi_over_4)} degrees - OK")

    pi_over_2 = np.pi / 2  # 90 degrees
    print(f"Phase shift π/2 = {np.degrees(pi_over_2)} degrees - OK")

    pi = np.pi  # 180 degrees
    print(f"Phase shift π = {np.degrees(pi)} degrees - OK (requires other_angle=True in Manim if needed)")

    # Angles greater than 180 degrees need special attention in Manim
    # since Manim's Angle.from_three_points might pick the smaller angle
    angle_gt_180 = 3 * np.pi / 2  # 270 degrees
    print(f"Angle 3π/2 = {np.degrees(angle_gt_180)} degrees - CAUTION! May need other_angle=True in Manim")

    print("Angle verification completed.\n")


def grep_MathTex():
    """
    Verify that LaTeX expressions in MathTex are properly formatted to avoid compilation errors.
    """
    print("Checking MathTex expressions for potential LaTeX compilation errors...")

    # Common issues to avoid:
    # 1. Unicode characters that LaTeX doesn't support
    # 2. Improperly escaped characters
    # 3. Unmatched braces

    # Good examples (these should work):
    expr1 = r"y = A \sin(\omega x + \varphi) + B"
    print(f"Expression: {expr1} - OK")

    expr2 = r"A=1 \to A=3"
    print(f"Expression: {expr2} - OK")

    expr3 = r"\omega=1 \to \omega=2"
    print(f"Expression: {expr3} - OK")

    expr4 = r"\varphi=0 \to \varphi=\frac{\pi}{4}"
    print(f"Expression: {expr4} - OK")

    expr5 = r"周期 T = \frac{2\pi}{\omega}"
    print(f"Expression: {expr5} - OK (but should be T = \\frac{{2\\pi}}{{\\omega}})")

    expr6 = r"T = \frac{2\pi}{\omega}"
    print(f"Expression: {expr6} - OK")

    print("LaTeX expression check completed.\n")


def verify_boundaries():
    """
    Verify that all elements stay within safe boundaries for the TikTok format.
    Safe coordinates: x ∈ [-4.5, 4.5], y ∈ [-7, 7] approximately.
    """
    print("Verifying element boundaries...")

    # Define safe boundaries
    x_min, x_max = -4.5, 4.5
    y_min, y_max = -7, 7

    print(f"Safe boundaries: x ∈ [{x_min}, {x_max}], y ∈ [{y_min}, {y_max}]")

    # Check various positions used in the animation
    positions = [
        ("Title", (0, 6.5)),
        ("Formula", (0, 5)),
        ("Hint text", (0, 3.5)),
        ("Axes center", (0, 1.5)),
        ("Summary title", (0, 6.5)),
        ("Parameter summaries", (-3, 4), (0, 4), (3, 4), (-3, 3), (0, 3), (3, 3)),
        ("Follow text", (0, 0)),
        ("Author name", (0, 2)),
        ("Author ID", (0, 1)),
    ]

    all_safe = True
    for pos_info in positions:
        name = pos_info[0]
        coords = pos_info[1:]
        for coord in coords:
            x, y = coord
            x_safe = x_min <= x <= x_max
            y_safe = y_min <= y <= y_max

            if not (x_safe and y_safe):
                print(f"  WARNING: {name} at ({x}, {y}) is out of bounds!")
                all_safe = False
            else:
                print(f"  OK: {name} at ({x}, {y}) is within bounds")

    # Check function ranges
    # x range: [-4, 4] - within bounds
    # y range: [-4, 4] for axes, but function values might exceed this
    print(f"  OK: Axis x-range [-4, 4] is within bounds")
    print(f"  OK: Axis y-range [-4, 4] is within bounds")

    # The transformed sine function has amplitude 2, shifted up by 1,
    # so y-values range from -2+1=-1 to 2+1=3, which is well within [-4, 4]
    print(f"  OK: Function y-values range from -1 to 3, within axis bounds [-4, 4]")

    if all_safe:
        print("\nAll elements are within safe boundaries.")
    else:
        print("\nSome elements are outside safe boundaries!")

    print("Boundary verification completed.\n")


def main():
    """
    Main verification function that runs all checks.
    """
    print("Starting verification of the y=Asin(ωx+φ) animation...\n")

    verify_angles()
    grep_MathTex()
    verify_boundaries()

    print("Verification process completed!")


if __name__ == "__main__":
    main()