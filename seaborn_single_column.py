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
entity_tokens = [tokens[7][i] for i in range(102)]  # entity
token = [tokens[7][71]]  # entity, index
attr = [i for i in range(1, 103)]
df = pd.read_csv("attention/Beer/attention8.csv", names=attr)  # 实体对2
attention = np.zeros((1, 102))
for j in range(1, 103):
    # attention[0][j-1] = df[j][102*12*11+9*102+71]  # index 12layer10head
    attention[0][j - 1] = df[j][102 * 12 * 10 + 10 * 102 + 71]  # index
df = pd.DataFrame(attention, columns=entity_tokens, index=token)
print(df)
hm = sns.heatmap(df, cmap="Oranges", cbar=False, square=True, xticklabels=True)
plt.show()
