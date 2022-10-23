import csv
from numpy import *
import pandas as pd

tokens = []
with open("attention/Beer_train/tokens.csv") as f:
    f_csv = csv.reader(f)
    heads = next(f_csv)
    for token in f_csv:
        tokens.append(token)
print(tokens)
extokens = ['COL', 'VAL', 'Beer', 'Name', 'Brew', 'Factory', 'Style', 'ABV']
attr = [i for i in range(1, 103)]
all_weight = []
j = 218
sep = tokens[j - 1].index("</s>") + 1
d = {}
df = pd.read_csv("attention/Beer_train/attention" + str(j) + ".csv", names=attr)
num = []
for i in range(1, 103):
    num.extend(pd.to_numeric(df[i]).tolist())
mean_value = mean(num)
std_value = std(num)
lenth = len(num)
for i in range(lenth):
    if num[i] > mean_value + 3 * std_value:
        """
        column = i // (102 * 144) + 1
        layer = (i % (102 * 144)) // (12 * 102) + 1
        head = ((i % (102 * 144)) % (12 * 102)) // 102 + 1
        row = ((i % (102 * 144)) % (12 * 102)) % 102 + 1
        """
        column = i // (102 * 144)
        row = ((i % (102 * 144)) % (12 * 102)) % 102
        if abs(row - column) > 2 and column != 0 and (
                row < sep and column > sep + 1 or row > sep + 1 and column < sep) and tokens[j - 1][row].isalpha() \
                and tokens[j - 1][column].isalpha() and (tokens[j - 1][row] not in extokens) \
                and (tokens[j - 1][column] not in extokens):
            if str(row + 1) + " " + str(column + 1) + ":" + tokens[j - 1][row] + " " + tokens[j - 1][column] in d:
                d[str(row + 1) + " " + str(column + 1) + ":" + tokens[j - 1][row] + " " + tokens[j - 1][
                    column]] += 1
            else:
                d[str(row + 1) + " " + str(column + 1) + ":" + tokens[j - 1][row] + " " + tokens[j - 1][column]] = 1
weight_distribution = sorted(d.items(), key=lambda x: -x[1])
all_weight.append(weight_distribution)
size = len(all_weight)
f = open("attention weight" + str(j) + ".csv", 'a', encoding='utf-8', newline="")
csv_writer = csv.writer(f)
for i in range(size):
    print(all_weight[i])
    csv_writer.writerow(all_weight[i])
