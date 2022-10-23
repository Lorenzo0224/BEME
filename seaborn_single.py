import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import csv
tokens = []
with open("attention/Beer/attention tokens.csv") as f:
    f_csv = csv.reader(f)
    heads = next(f_csv)
    for token in f_csv:
        tokens.append(token)
# entity_tokens = [tokens[1][i] for i in range(102)]
entity_tokens = [str(i+1) for i in range(102)]
attr = [i for i in range(1, 103)]
df = pd.read_csv("attention/Beer/attention8.csv", names=attr)  # 实体对2
attention = np.zeros((102, 102))
for i in range(102):
    for j in range(1, 103):
        attention[i][j-1] = df[j][102*12*11+102*9+i]  # index
df = pd.DataFrame(attention, columns=entity_tokens, index=entity_tokens)
# hm = sns.heatmap(df, cmap="Oranges", xticklabels=True, yticklabels=True)
hm = sns.heatmap(df, cmap="Oranges", square=True)
plt.show()
