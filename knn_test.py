import time
from matplotlib.font_manager import FontProperties
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
data = "Watches"
title = "Watches"
print(time.strftime("%Y-%m-%d %H:%M:%S"))
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
CLS = []
labels = []
with open("CLS_Roberta/" + data + "/CLStest.txt", "r", encoding='utf-8') as f:
    for i in f.readlines():
        j = i.split("\t")
        labels.append(int(j[1].split("\n")[0]))
        i = j[0].split(",")
        lenth = len(i)
        for index in range(lenth):
            i[index] = float(i[index])
        CLS.append(i)
print(len(CLS[0]))
print(len(CLS))
truelabels = []
predicts = []
oldtruelabels = []
oldpredicts = []
starttime = {}
endtime = {}
knn_time = {}
with open("ditto_Roberta/" + data + "/test_result.txt", "r") as f:
    for i in f.readlines():
        i = i.split(" ")
        j = i[1].split("\n")
        oldtruelabels.append(int(i[0]))
        oldpredicts.append(int(j[0]))
        if int(i[0]) == int(j[0]):
            truelabels.append(int(i[0]))
            predicts.append(int(j[0]))
truelabels.extend(labels)
predict = {}
x_axis_data = []
y_f1_score = []
y_precision_score = []
y_recall_score = []
y_f1_score2 = []
y_precision_score2 = []
y_recall_score2 = []
print(len(oldtruelabels))
print(len(oldpredicts))
origin_f1_score = metrics.f1_score(oldtruelabels, oldpredicts)
origin_precision_score = metrics.precision_score(oldtruelabels, oldpredicts)
origin_recall_score = metrics.recall_score(oldtruelabels, oldpredicts)
print("origin_f1_score:", origin_f1_score)
print("origin_precision_score:", origin_precision_score)
print("origin_recall_score:", origin_recall_score)
f1_score = {}
precision_score = {}
recall_score = {}
for k in range(2, 100):
    predict[k] = []
    predict[k].extend(predicts)
    starttime[k] = time.time()
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(CLStrain, labelstrain)
    y_pred = knn.predict(CLS)
    endtime[k] = time.time()
    knn_time[k] = float(endtime[k] - starttime[k]) * 1000.0
    predict[k].extend(y_pred)
    if k > 2:
        x_axis_data.append(k)
        y_f1_score.append(metrics.f1_score(truelabels, predict[k]))
        y_f1_score2.append(origin_f1_score)
        y_precision_score.append(metrics.precision_score(truelabels, predict[k]))
        y_precision_score2.append(origin_precision_score)
        y_recall_score.append(metrics.recall_score(truelabels, predict[k]))
        y_recall_score2.append(origin_recall_score)
    f1_score[k] = metrics.f1_score(truelabels, predict[k])
    precision_score[k] = metrics.precision_score(truelabels, predict[k])
    recall_score[k] = metrics.recall_score(truelabels, predict[k])
    print(metrics.f1_score(truelabels, predict[k]))
plt.plot(x_axis_data, y_f1_score2, 'r.--', alpha=0.5, linewidth=1, label='f1_score_origin')
plt.plot(x_axis_data, y_f1_score, 'bo--', alpha=0.5, linewidth=1, label='f1_score_withknn')
plt.legend()
font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
plt.title(title, fontproperties=font1)
plt.xlabel('k', fontproperties=font1)
plt.ylabel('f1_score', fontproperties=font1)
plt.show()
plt.plot(x_axis_data, y_precision_score2, 'r.--', alpha=0.5, linewidth=1, label='precision_score_origin')
plt.plot(x_axis_data, y_precision_score, 'bo--', alpha=0.5, linewidth=1, label='precision_score_withknn')
plt.legend()
plt.title(title, fontproperties=font1)
plt.xlabel('k', fontproperties=font1)
plt.ylabel('precision_score', fontproperties=font1)
plt.show()
plt.plot(x_axis_data, y_recall_score2, 'r.--', alpha=0.5, linewidth=1, label='recall_score_origin')
plt.plot(x_axis_data, y_recall_score, 'bo--', alpha=0.5, linewidth=1, label='recall_score_withknn')
plt.legend()
plt.title(title, fontproperties=font1)
plt.xlabel('k', fontproperties=font1)
plt.ylabel('recall_score', fontproperties=font1)
plt.show()
print(knn_time)
y_f1_time = []
for k in range(3, 100):
    y_f1_time.append(knn_time[k])
plt.plot(x_axis_data, y_f1_time, 'r.--', alpha=0.5, linewidth=1)
plt.title(title, fontproperties=font1)
plt.xlabel('k', fontproperties=font1)
plt.ylabel('time(ms)', fontproperties=font1)
plt.show()
print(f1_score)
print(precision_score)
print(recall_score)
"""

print(y_pred)
print(labels)
lenth = len(labels)
acc = 0
error = 0
for i in range(lenth):
    if labels[i] == y_pred[i]:
        acc += 1
    else:
        error += 1
print(acc)
print(error)
"""