"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3     # decay constant, given

# 1. Read CSV into arrays t and observed
t, observed = np.loadtxt(
    "decay_observed.csv",
    delimiter=",",
    skiprows=1,
    unpack=True
)

# 2. First observed value is N0, then build analytical curve
NO = observed[0]
analytical = NO * np.exp(-LAMBDA * t)

# 3. Make 1x2 subplot with shared x and y axes
fig, axes = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

# Left: scatter of observed
axes[0].scatter(t, observed)
axes[0].set_title("Observed")
axes[0].set_xlabel("t")
axes[0].set_ylabel("N")

# Right: line of analytical
axes[1].plot(t, analytical)
axes[1].set_title("Analytical")
axes[1].set_xlabel("t")
axes[1].set_ylabel("N")

fig.tight_layout()

# 4. Save figure
fig.savefig("figure.png")
