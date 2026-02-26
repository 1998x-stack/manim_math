"""
Simple test to verify the animation code can be imported and instantiated
"""
try:
    from final_parallel_determination import ParallelLineDetermination
    print("✓ Successfully imported ParallelLineDetermination class")
    
    # Try to instantiate the scene (without rendering)
    scene = ParallelLineDetermination()
    print("✓ Successfully instantiated the scene")
    
    print("\nTo render the animation, run:")
    print("manim -pql final_parallel_determination.py ParallelLineDetermination")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
except Exception as e:
    print(f"✗ Error: {e}")

# Also test the geometry verification functions
try:
    from verify_geometry import verify_angles, grep_MathTex, verify_boundaries
    print("\n✓ Successfully imported verification functions")
    
    # Run basic tests
    verify_angles()
    grep_MathTex()
    verify_boundaries()
    print("✓ All verification functions ran successfully")
    
except ImportError as e:
    print(f"✗ Could not import verification functions: {e}")
except Exception as e:
    print(f"✗ Error in verification functions: {e}")