import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df2 = pd.read_csv("chemicals_cancer.csv")
print(df2.shape)
print(df2.columns.tolist())
print(df2.head())