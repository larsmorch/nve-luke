import numpy as np
import matplotlib.pyplot as plt


def beam_centered_udl_numeric_deflection_mm_kN(w_kN_per_m, a_mm, L_mm, E_Pa, I_mm4, npts=4001):
    """
    Simply supported beam with centered partial UDL, using:
      length      : mm
      force       : kN
      moment      : kN·m (returned)
      deflection  : mm (returned)

    Inputs:
      w_kN_per_m  : kN/m   (UDL intensity over length a, centered)
      a_mm, L_mm  : mm
      E_Pa        : Pa (N/m^2)
      I_mm4       : mm^4
    """
    if not (0 < a_mm <= L_mm):
        raise ValueError("a_mm must satisfy 0 < a_mm <= L_mm")

    # --- Unit conversions to a consistent internal system (N, mm) ---
    # E in Pa = N/m^2 -> N/mm^2
    E_N_per_mm2 = E_Pa / 1e6
    I = I_mm4  # mm^4
    EI = E_N_per_mm2 * I  # N*mm^2

    # w: kN/m -> N/mm (1 kN=1000 N, 1 m=1000 mm => numerically same)
    w = w_kN_per_m  # N/mm

    # Geometry
    x1 = 0.5 * (L_mm - a_mm)
    x2 = 0.5 * (L_mm + a_mm)

    x = np.linspace(0.0, L_mm, npts)
    dx = x[1] - x[0]

    # Reactions (symmetry) in N
    RA = RB = 0.5 * w * a_mm  # N

    # Shear V(x) in N
    V = np.full_like(x, RA)
    in_load = (x >= x1) & (x <= x2)
    right_of_load = (x > x2)

    V[in_load] = RA - w * (x[in_load] - x1)
    V[right_of_load] = RA - w * a_mm  # = -RB

    # Moment M(x) in N*mm
    M = np.empty_like(x)
    left = x < x1
    M[left] = RA * x[left]
    M[in_load] = RA * x[in_load] - 0.5 * w * (x[in_load] - x1) ** 2
    M[right_of_load] = RB * (L_mm - x[right_of_load])  # ensures M(L)=0

    # Curvature kappa = y'' = M/(E I)  -> 1/mm
    kappa = M / EI

    # Integrate twice (trapezoidal) -> slope (rad), deflection (mm)
    theta = np.zeros_like(x)
    theta[1:] = np.cumsum(0.5 * (kappa[:-1] + kappa[1:]) * dx)

    y = np.zeros_like(x)
    y[1:] = np.cumsum(0.5 * (theta[:-1] + theta[1:]) * dx)

    # Enforce y(0)=0 and y(L)=0 exactly by removing end-to-end line
    y = y - (y[0] + (y[-1] - y[0]) * (x / L_mm))

    # --- Convert outputs to requested designations ---
    V_kN = V / 1e3                # kN
    M_kNm = (M / 1e6)             # N*mm -> kN*m (1 kN*m = 1e6 N*mm)
    y_mm = y                      # mm

    return x, V_kN, M_kNm, y_mm, (RA / 1e3, RB / 1e3, x1, x2)


def plot_diagrams_mm_kN(x_mm, V_kN, M_kNm, y_mm, L_mm, x1, x2):
    fig, axs = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

    def mark_load(ax):
        ax.axvspan(x1, x2, color="k", alpha=0.08)
        ax.axhline(0, color="k", lw=0.8)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, L_mm)

    axs[0].plot(x_mm, V_kN, lw=2)
    mark_load(axs[0])
    axs[0].set_ylabel("Shear V [kN]")

    axs[1].plot(x_mm, M_kNm, lw=2)
    mark_load(axs[1])
    axs[1].set_ylabel("Moment M [kN·m]")

    axs[2].plot(x_mm, y_mm, lw=2)
    mark_load(axs[2])
    axs[2].set_ylabel("Deflection y [mm] (up +)")
    axs[2].set_xlabel("x [mm]")

    xm = L_mm / 2
    ym = np.interp(xm, x_mm, y_mm)
    axs[2].plot([xm], [ym], "o")
    axs[2].annotate(f"y(L/2) = {ym:.3f} mm", (xm, ym),
                    textcoords="offset points", xytext=(10, 10))

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # ---- Inputs in requested designations ----
    w = 10.0            # kN/m  (partial UDL intensity)
    a = 4000.0          # mm (loaded length, centered)
    L = 10000.0         # mm
    E = 210e9           # Pa
    I = 5.517e8         # mm^4

    x, V_kN, M_kNm, y_mm, (RA_kN, RB_kN, x1, x2) = beam_centered_udl_numeric_deflection_mm_kN(w, a, L, E, I)

    print(f"RA = {RA_kN:.6g} kN, RB = {RB_kN:.6g} kN")
    print(f"y(0)   = {y_mm[0]:.6e} mm")
    print(f"y(L)   = {y_mm[-1]:.6e} mm")
    print(f"y(L/2) = {np.interp(L/2, x, y_mm):.6f} mm (up +)")

    iV = np.argmax(np.abs(V_kN))
    iM = np.argmax(np.abs(M_kNm))
    print(f"Max |V| = {abs(V_kN[iV]):.6g} kN at x = {x[iV]:.4g} mm (V = {V_kN[iV]:.6g} kN)")
    print(f"Max |M| = {abs(M_kNm[iM]):.6g} kN·m at x = {x[iM]:.4g} mm (M = {M_kNm[iM]:.6g} kN·m)")

    plot_diagrams_mm_kN(x, V_kN, M_kNm, y_mm, L, x1, x2)