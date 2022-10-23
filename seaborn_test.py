import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
e = ""
heads = [str(i) for i in range(1, 13)]
layers = [str(i) for i in range(1, 13)]
attr = [i for i in range(1, 103)]
df = pd.read_csv("attention/Beer/attention8.csv", names=attr)  # 实体对
attention = np.zeros((12, 12))
for layer in range(12):
    for head in range(12):
        attention[layer][head] = df[22][102*12*layer+102*head+71]  # index
"""
weight_sum = attention.sum()
for layer in range(12):
    for head in range(12):
        attention[layer][head] = attention[layer][head]/weight_sum
"""
df = pd.DataFrame(attention, columns=heads, index=layers)
print(df)
hm = sns.heatmap(df, cmap="YlOrRd", annot=True, square=True)
# hm = sns.heatmap(df, cmap="YlOrRd", square=True)
plt.show()
