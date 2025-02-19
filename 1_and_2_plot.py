from Task1_1 import ysolBDF as ysol1
from Task1_2 import ysolBDF as ysol2

import matplotlib.pyplot as plt

ysol1.y = ysol1.y[[0, 3], :]

# Plot only Substrate (S) and Product (P) for both ysol1 and ysol2
fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)  # 2 rows, 1 column
colors = ["#2ca02c", "#1f77b4"]  # Soothing color palette for S and P
labels = ["Substrate (S)", "Product (P)"]

# Plot ysol1 and ysol2 together
for i, ax in enumerate(axes):
    ax.plot(ysol1.t, ysol1.y[i, :], color=colors[0], linewidth=2, label=f'Task1_1 {labels[i]}')
    ax.plot(ysol2.t, ysol2.y[i, :], color=colors[1], marker='o', linestyle = '', linewidth=2, label=f'Task1_2 {labels[i]}')
    ax.set_ylabel("Concentration [mmol/L]", fontsize=12)
    ax.set_title(labels[i], fontsize=14, fontweight="bold")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend()

axes[-1].set_xlabel("Time (s)", fontsize=12)  # X-axis label on last subplot

plt.tight_layout()
plt.show()
