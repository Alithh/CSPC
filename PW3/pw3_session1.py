import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("Heart_disease_cleveland_new.csv")
print("shape:", df.shape)
print(df.head())
print("columns:", df.columns.tolist())
print("missing values:\n", df.isna().sum())
print("target counts:\n", df["target"].value_counts())

cont = df[["age", "chol", "trestbps", "thalach"]]
print(cont.describe())

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.ravel(), cont.columns):
    ax.hist(cont[col], bins=20, density=True, edgecolor="black", alpha=0.7)
    ax.set_title(col)
    ax.set_xlabel(col)
    ax.set_ylabel("density")
plt.tight_layout()
plt.savefig("distributions.png", dpi=150)
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
print(f"{'var':10s} {'skew':>7s} {'ex.kurt':>8s} {'Shapiro W':>10s} {'p':>10s}")
for ax, col in zip(axes.ravel(), cont.columns):
    x = cont[col]
    stats.probplot(x, dist="norm", plot=ax)
    ax.set_title(f"Q-Q plot: {col}")
    W, p = stats.shapiro(x)
    print(f"{col:10s} {stats.skew(x):7.2f} {stats.kurtosis(x):8.2f} {W:10.3f} {p:10.4f}")
plt.tight_layout()
plt.savefig("qqplots.png", dpi=150)
plt.show()