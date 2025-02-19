from Task1_2 import ysolRK45 as ysol2
import matplotlib.pyplot as plt
import numpy as np

# Define the analytical solution
def analytical_solution_S(c_S):
    return (20 / 3) - (267 * np.log(c_S / 1000) / 200) - (c_S / 150)

# Define the analytical solution for Product (P)
def analytical_solution_P(c_S):
    return 1000 - c_S

# Calculate the analytical solution for the same concentration range
t_analytical_S = analytical_solution_S(ysol2.y[0, :])
c_P_analytical = analytical_solution_P(ysol2.y[0, :])

# Plot the numerical and analytical solutions
fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)  # 2 rows, 1 column
colors = ["#2ca02c", "#1f77b4"]  # Green for analytical, blue for numerical
labels = ["Substrate (S)", "Product (P)"]

# Plot Substrate (S)
axes[0].plot(t_analytical_S, ysol2.y[0, :], color=colors[0], linewidth=2, label='Analytical Solution S')
axes[0].plot(ysol2.t, ysol2.y[0, :], color=colors[1], marker='o', linestyle='', linewidth=2, label='Numerical Solution S')
axes[0].set_ylabel("Concentration [mmol/L]", fontsize=12)
axes[0].set_title(labels[0], fontsize=14, fontweight="bold")
axes[0].grid(True, linestyle="--", alpha=0.6)
axes[0].legend()

# Plot Product (P)
axes[1].plot(t_analytical_S, c_P_analytical, color=colors[0], linewidth=2, label='Analytical Solution P')
axes[1].plot(ysol2.t, ysol2.y[1, :], color=colors[1], marker='o', linestyle='', linewidth=2, label='Numerical Solution P')
axes[1].set_ylabel("Concentration [mmol/L]", fontsize=12)
axes[1].set_title(labels[1], fontsize=14, fontweight="bold")
axes[1].grid(True, linestyle="--", alpha=0.6)
axes[1].legend()

axes[-1].set_xlabel("Time (s)", fontsize=12)  # X-axis label on last subplot

plt.tight_layout()
plt.show()