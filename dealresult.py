import json
import time
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

data = "Watches"
title = "Watches"
threshold = 0.5
time_ditto = format(849.931002 + 173.016310, '.0f')
print(time_ditto)
predict = []
confidence = []
with open("ditto_Roberta/" + title + "_output_small.jsonl", 'r', encoding='utf8') as fp:
    for line in fp.readlines():
        js_l = json.loads(line)
        predict.append(js_l["match"])
        confidence.append(js_l["match_confidence"])
CLStrain = []
labelstrain = []
with open("CLS_Roberta/" + data + "/CLStrain.txt", "r", encoding='utf-8') as f:
    for i in f.readlines():
        j = i.split("\t")
        labelstrain.append(int(j[1].split("\n")[0]))
        i = j[0].split(",")
        lenth = len(i)
        for index in range(lenth):
            i[index] = float(i[index])
        CLStrain.append(i)
CLStest = []
labelstest = []
with open("CLStest/" + data + ".txt", "r", encoding='utf-8') as f:
    for i in f.readlines():
        j = i.split("\t")
        labelstest.append(int(j[1].split("\n")[0]))
        i = j[0].split(",")
        lenth = len(i)
        for index in range(lenth):
            i[index] = float(i[index])
        CLStest.append(i)
predicts = {}
y_f1_score = [threshold]
y_precision_score = [threshold]
y_recall_score = [threshold]
knn_time = [threshold]
size = len(confidence)
labels = []
truelabel = []
for i in range(size):
    if confidence[i] > threshold:
        truelabel.append(labelstest[i])
    else:
        labels.append(labelstest[i])
truelabel.extend(labels)
origin_f1_score = metrics.f1_score(labelstest, predict)
origin_precision_score = metrics.precision_score(labelstest, predict)
origin_recall_score = metrics.recall_score(labelstest, predict)
print("P=", format(origin_precision_score, '.4f'))
print("R=", round(origin_recall_score, 4))
print("F1=", format(origin_f1_score, '.4f'))
for k in range(2, 51):
    predicts[k] = []
    CLS = []
    starttime = time.time()
    for i in range(size):
        if confidence[i] > threshold:
            predicts[k].append(predict[i])
        else:
            CLS.append(CLStest[i])
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(CLStrain, labelstrain)
    y_pred = knn.predict(CLS)
    endtime = time.time()
    predicts[k].extend(y_pred)
    if k > 2:
        knn_time.append(format(float(endtime - starttime) * 1000.0, '.0f'))
        y_f1_score.append(format(metrics.f1_score(truelabel, predicts[k]), '.4f'))
        y_precision_score.append(format(metrics.precision_score(truelabel, predicts[k]), '.4f'))
        y_recall_score.append(format(metrics.recall_score(truelabel, predicts[k]), '.4f'))
print(y_precision_score)
print(y_recall_score)
print(y_f1_score)
print(knn_time)
f = open("knn(confidence)/" + data + "/precision.csv", 'a', encoding='utf-8', newline="")
csv_writer = csv.writer(f)
if threshold == 0.5:
    a = ["threshold\k"]
    for i in range(3, 51):
        a.append(i)
    csv_writer.writerow(a)
csv_writer.writerow(y_precision_score)
f.close()
f = open("knn(confidence)/" + data + "/recall.csv", 'a', encoding='utf-8', newline="")
csv_writer = csv.writer(f)
if threshold == 0.5:
    a = ["threshold\k"]
    for i in range(3, 51):
        a.append(i)
    csv_writer.writerow(a)
csv_writer.writerow(y_precision_score)
f.close()
f = open("knn(confidence)/" + data + "/f1.csv", 'a', encoding='utf-8', newline="")
csv_writer = csv.writer(f)
if threshold == 0.5:
    a = ["threshold\k"]
    for i in range(3, 51):
        a.append(i)
    csv_writer.writerow(a)
csv_writer.writerow(y_f1_score)
f.close()
f = open("knn(confidence)/" + data + "/time.csv", 'a', encoding='utf-8', newline="")
csv_writer = csv.writer(f)
if threshold == 0.5:
    a = ["threshold\k"]
    for i in range(3, 51):
        a.append(i)
    csv_writer.writerow(a)
csv_writer.writerow(knn_time)
f.close()
f = open("knn(confidence)/" + data + "/time.csv", 'a', encoding='utf-8', newline="")
csv_writer = csv.writer(f)
if threshold == 0.5:
    a = ["threshold\k"]
    for i in range(3, 51):
        a.append(i)
    csv_writer.writerow(a)
csv_writer.writerow(knn_time)
f.close()
