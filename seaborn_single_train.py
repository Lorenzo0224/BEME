import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import csv
"""
tokens = []
with open("attention/Beer_train/tokens.csv") as f:
    f_csv = csv.reader(f)
    heads = next(f_csv)
    for token in f_csv:
        tokens.append(token)
"""
entity_tokens = [str(i) for i in range(102)]
attr = [i for i in range(1, 103)]
df = pd.read_csv("attention/Beer_train/attention218.csv", names=attr)  # 实体对
attention = np.zeros((102, 102))
for i in range(102):
    for j in range(1, 103):
        attention[i][j-1] = df[j][102*12*3+102*8+i]  # index
        # attention[i][j - 1] = df[j][102 * 12 * 6 + i]
df = pd.DataFrame(attention, columns=entity_tokens, index=entity_tokens)
hm = sns.heatmap(df, cmap="Oranges")
plt.show()
