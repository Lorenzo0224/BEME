import csv

from numpy import *
import pandas as pd

attr = [i for i in range(1, 103)]
all_mean_value = []
all_std_value = []
d = {}
for j in [22, 131, 213, 218]:
    df = pd.read_csv("attention/Beer_train/attention" + str(j) + ".csv", names=attr)
    num = []
    for i in range(1, 103):
        num.extend(pd.to_numeric(df[i]).tolist())
    mean_value = mean(num)
    std_value = std(num)
    all_mean_value.append(mean_value)
    all_std_value.append(std_value)
print(all_mean_value)
print(all_std_value)
f = open("miu&sigma.csv", 'w', encoding='utf-8', newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(all_mean_value)
csv_writer.writerow(all_std_value)
f.close()
