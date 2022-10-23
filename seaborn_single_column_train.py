import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import csv
tokens = []
with open("attention/Beer_train/tokens.csv") as f:
    f_csv = csv.reader(f)
    heads = next(f_csv)
    for token in f_csv:
        tokens.append(token)
entity_tokens = [tokens[217][i] for i in range(102)]  # entity token
token = [tokens[217][28]]  # token
attr = [i for i in range(1, 103)]
df = pd.read_csv("attention/Beer_train/attention218.csv", names=attr)  # 实体对
attention = np.zeros((1, 102))
for j in range(1, 103):
    attention[0][j-1] = df[j][102*12*3+8*102+28]  # index(3)
    # attention[0][j - 1] = df[j][102 * 12 * 6 + 19]
df = pd.DataFrame(attention, columns=entity_tokens, index=token)
print(df["Pale"])
hm = sns.heatmap(df, cmap="Oranges", cbar=False, square=True, xticklabels=True)
plt.show()
