import csv
import json
from sklearn import metrics

data = "Beer"
title = "Beer"
threshold = [0, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
predict = []
confidence = []
with open("ditto_Roberta/" + title + "_output_small.jsonl", 'r', encoding='utf8') as fp:
    for line in fp.readlines():
        js_l = json.loads(line)
        predict.append(js_l["match"])
        confidence.append(js_l["match_confidence"])
size = len(threshold)
predicts = {}
labels = {}
for i in range(size):
    predicts[i] = []
    labels[i] = []
label = []
with open("CLStest/" + data + ".txt", "r", encoding='utf-8') as f:
    for i in f.readlines():
        j = i.split("\t")
        label.append(int(j[1].split("\n")[0]))
lenth = len(confidence)
for i in range(lenth):
    for j in range(size - 1):
        if threshold[j] <= confidence[i] < threshold[j + 1]:
            labels[j].append(label[i])
            predicts[j].append(predict[i])
result = []
for i in range(size - 1):
    print(labels[i])
    print(predicts[i])
    if len(labels[i]) != 0:
        result.append(metrics.f1_score(labels[i], predicts[i]))
    else:
        result.append(0)
"""
f = open("result(confidence).csv", 'a', encoding='utf-8', newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(result)
f.close()
"""