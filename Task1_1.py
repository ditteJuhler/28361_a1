import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import timeit

# Rate constants
k1f = 1000 # L/h/mmol
k1b = 2E5 # 1/h
kr = 250 # 1/h

# Initial conditions
S0 = 1000 # mmol/L
E0 = 0.6 # mmol/L
ES0 = 0 # mmol/L
P0 = 0 # mmol/L

def model(t, y):
    S, E, ES, P = y

    dydt = np.zeros(len(y))
    dydt[0] = -k1f*S*E + k1b*ES
    dydt[1] = -k1f*S*E + k1b*ES + kr*ES
    dydt[2] = k1f*S*E - k1b * ES - kr*ES
    dydt[3] = kr*ES

    return dydt

# Define solving properties
y0 = [S0, E0, ES0, P0]
t_span = [0,20]

# Solve equations with timer
startBDF = timeit.default_timer()
ysolBDF = solve_ivp(model, t_span, y0, method='BDF')
stopBDF = timeit.default_timer()

startRK45 = timeit.default_timer()
ysolRK45 = solve_ivp(model, t_span, y0, method='BDF')
#ysolRK45 = solve_ivp(model, t_span, y0, method='RK45')
stopRK45 = timeit.default_timer()

print('Time BDF: ', stopBDF - startBDF)
print('Time RK45: ', stopRK45 - startRK45)  

# Plot ALL with both
fig, axes = plt.subplots(4, 1, figsize=(8, 10), sharex=True)
colors = ["#1f77b4", "#ff7f0e"]
labels = ["Substrate (S)", "Enzyme (E)", "Complex (ES)", "Product (P)"]

for i, ax in enumerate(axes):
    if i == 0:
        ax.plot(ysolRK45.t, ysolRK45.y[i, :], color=colors[0], linewidth=2, label='RK45')
        ax.plot(ysolBDF.t, ysolBDF.y[i, :], color=colors[1], marker = 'o', linestyle='', linewidth=2, label='BDF')
    if i != 0:
        ax.plot(ysolRK45.t, ysolRK45.y[i, :], color=colors[0], linewidth=2)
        ax.plot(ysolBDF.t, ysolBDF.y[i, :], color=colors[1], marker = 'o', linestyle='', linewidth=2)
    
    ax.set_title(labels[i], fontsize=14, fontweight="bold")
    ax.grid(True, linestyle="--", alpha=0.6)
    
    if i == 0:
        ax.legend()

axes[-1].set_xlabel("Time (s)", fontsize=12) 
fig.text(0.04, 0.5, 'Concentration [mmol/L]', va='center', rotation='vertical', fontsize=12)


plt.tight_layout()
plt.show()



