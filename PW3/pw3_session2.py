import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("Heart_disease_cleveland_new.csv")

disease = df.loc[df["target"] == 1, "thalach"]
healthy = df.loc[df["target"] == 0, "thalach"]
print("n disease:", len(disease), " n healthy:", len(healthy))
print("mean disease: %.2f   mean healthy: %.2f" % (disease.mean(), healthy.mean()))

t, p_t = stats.ttest_ind(disease, healthy, equal_var=False)
print(f"Welch t-test:   t = {t:.2f}, p = {p_t:.3e}")

U, p_u = stats.mannwhitneyu(disease, healthy, alternative="two-sided")
print(f"Mann-Whitney:   U = {U:.0f}, p = {p_u:.3e}")

sp = np.sqrt(((len(disease) - 1) * disease.var(ddof=1) +
              (len(healthy) - 1) * healthy.var(ddof=1)) /
             (len(disease) + len(healthy) - 2))
print("Cohen's d = %.2f" % ((disease.mean() - healthy.mean()) / sp))

def mean_ci(x, conf=0.95):
    n = len(x)
    m = x.mean()
    sem = x.std(ddof=1) / np.sqrt(n)
    half = stats.t.ppf((1 + conf) / 2, n - 1) * sem
    return m, sem, half

names, means, halves = [], [], []
for name, g in [("Disease", disease), ("Healthy", healthy)]:
    m, sem, half = mean_ci(g)
    print(f"{name}: mean = {m:.1f}, SEM = {sem:.2f}, 95% CI = [{m-half:.1f}, {m+half:.1f}]")
    names.append(name); means.append(m); halves.append(half)

plt.figure(figsize=(5, 5))
plt.errorbar(names, means, yerr=halves, fmt="o", capsize=8, markersize=8)
plt.ylabel("thalach (max heart rate, bpm)")
plt.title("Mean thalach with 95% CI")
plt.xlim(-0.5, 1.5)
plt.savefig("thalach_means.png", dpi=150)
plt.show()

r, p_r = stats.pearsonr(df["age"], df["thalach"])
rho, p_s = stats.spearmanr(df["age"], df["thalach"])
print(f"Pearson r = {r:.3f} (p = {p_r:.2e});  Spearman rho = {rho:.3f} (p = {p_s:.2e})")

slope, intercept = np.polyfit(df["age"], df["thalach"], 1)
xs = np.linspace(df["age"].min(), df["age"].max(), 100)
plt.figure(figsize=(6, 5))
plt.scatter(df["age"], df["thalach"], alpha=0.6)
plt.plot(xs, slope * xs + intercept, color="red",
         label=f"fit: slope = {slope:.2f} bpm/year")
plt.xlabel("age (years)")
plt.ylabel("thalach (bpm)")
plt.legend()
plt.savefig("age_vs_thalach.png", dpi=150)
plt.show()