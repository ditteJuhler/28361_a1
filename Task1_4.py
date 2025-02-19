from Task1_1 import ysolBDF
import numpy as np
import matplotlib.pyplot as plt


def lambda1(S, E):
    return(-500*(E+S)-100125+125*np.sqrt(16*E**2+(32*S+6392)*E+16*(S+200.25)**2))
def lambda2(S, E):
    return(-500*(E+S)-100125-125*np.sqrt(16*E**2+(32*S+6392)*E+16*(S+200.25)**2))

S = ysolBDF.y[0, :]
E = ysolBDF.y[1, :]

# Calculate lambda1 and lambda2
lambda1_values = abs(lambda1(S, E))
lambda2_values = abs(lambda2(S, E))
ratio = abs(lambda2(S, E)/lambda1(S, E))


# Plot lambda1 and lambda2
fig, ax = plt.subplots(figsize=(8, 6))
colors = ["#1f77b4", "#d62728", "#2ca02c"]  # Blue for lambda1, red for lambda2

ax.plot(ysolBDF.t, lambda1_values, color=colors[0], linewidth=2, label='lambda1')
ax.plot(ysolBDF.t, lambda2_values, color=colors[1], linewidth=2, label='lambda2')
ax.plot(ysolBDF.t, ratio, color=colors[2], linewidth=2, label='Ratio')
ax.set_xlabel("Time (s)", fontsize=12)
ax.set_ylabel("Lambda values", fontsize=12)
ax.set_title("Lambda1 and Lambda2 over Time with the ratio", fontsize=14, fontweight="bold")
ax.set_yscale('log')
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend()

plt.tight_layout()
plt.show()



