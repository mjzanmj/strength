import math

def structural_analysis():
    # 1. Inputs
    P = float(input("Enter Axial Force (kN): "))
    L = float(input("Enter Length of the member (m): "))
    d = float(input("Enter Diameter of the cross-section (mm): "))
    E = float(input("Enter Modulus of Elasticity (GPa): "))
    sigma_y = float(input("Enter Yield Strength (MPa): "))

    # 2. Calculations
    A = (math.pi / 4) * (d ** 2)                  # Cross-sectional Area in mm²
    sigma = (P * 1000.0) / A                       # Axial Stress in MPa
    epsilon = sigma / (E * 1000.0)                 # Axial Strain in mm/mm
    delta = (P * L) / (A * E)                      # Axial Deformation in mm

    # Display Results
    print("\n--- Results ---")
    print(f"Cross-sectional Area (A): {A:.2f} mm²")
    print(f"Axial Stress (sigma): {sigma:.2f} MPa")
    print(f"Axial Strain (epsilon): {epsilon:.6f} mm/mm")
    print(f"Axial Deformation (delta): {delta:.4f} mm")

    # 3. Warning Alarm (Logic Check)
    print("\n--- Status ---")
    if sigma > sigma_y:
        print("🚨 ALARM: YIELDING DETECTED! STRUCTURAL FAILURE IMMINENT! 🚨")
    else:
        print("✅ Structure is Safe.")

if __name__ == "__main__":
    structural_analysis()
