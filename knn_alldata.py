import time
from matplotlib.font_manager import FontProperties
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
print(time.strftime("%Y-%m-%d %H:%M:%S"))
CLStrain = []
labelstrain = []
data = "Cameras"
title = "Cameras"
origin_time = 116.605043
one = 0
with open("CLS_Roberta/" + data + "/CLStrain.txt", "r", encoding='utf-8') as f:
    for i in f.readlines():
        j = i.split("\t")
        labelstrain.append(int(j[1].split("\n")[0]))
        if int(j[1].split("\n")[0]) == 1:
            one += 1
        i = j[0].split(",")
        lenth = len(i)
        for index in range(lenth):
            i[index] = float(i[index])
        CLStrain.append(i)
CLS = []
print(one)
truelabels = []
oldpredicts = []
one = 0
with open("CLStest/" + data + ".txt", "r", encoding='utf-8') as f:
    for i in f.readlines():
        j = i.split("\t")
        truelabels.append(int(j[1].split("\n")[0]))
        if int(j[1].split("\n")[0]) == 1:
            one += 1
        i = j[0].split(",")
        lenth = len(i)
        for index in range(lenth):
            i[index] = float(i[index])
        CLS.append(i)
oldtruelabels = []
print(one)
with open("ditto_Roberta/" + data + "/test_result.txt", "r") as f:
    for i in f.readlines():
        i = i.split(" ")
        j = i[1].split("\n")
        oldpredicts.append(int(i[1]))
print(len(truelabels))
print(len(oldpredicts))
starttime = {}
knn_time = {}
predict = {}
x_axis_data = []
y_f1_score = []
y_precision_score = []
y_recall_score = []
y_f1_score2 = []
y_precision_score2 = []
y_recall_score2 = []
origin_f1_score = metrics.f1_score(truelabels, oldpredicts)
origin_precision_score = metrics.precision_score(truelabels, oldpredicts)
origin_recall_score = metrics.recall_score(truelabels, oldpredicts)
print("origin_f1_score:", origin_f1_score)
print("origin_precision_score:", origin_precision_score)
print("origin_recall_score:", origin_recall_score)
print("origin_time:", str(origin_time))
f1_score = {}
precision_score = {}
recall_score = {}
for k in range(2, 61):
    starttime[k] = time.time()
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(CLStrain, labelstrain)
    predict[k] = knn.predict(CLS)
    knn_time[k] = float(time.time() - starttime[k]) * 1000.0
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
plt.plot(x_axis_data, y_f1_score, 'bo--', alpha=0.5, linewidth=1, label='f1_score_knn')
plt.legend()
font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
plt.title(title, fontproperties=font1)
plt.xlabel('k', fontproperties=font1)
plt.ylabel('f1_score', fontproperties=font1)
plt.show()
plt.plot(x_axis_data, y_precision_score2, 'r.--', alpha=0.5, linewidth=1, label='precision_score_origin')
plt.plot(x_axis_data, y_precision_score, 'bo--', alpha=0.5, linewidth=1, label='precision_score_knn')
plt.legend()
plt.title(title, fontproperties=font1)
plt.xlabel('k', fontproperties=font1)
plt.ylabel('precision_score', fontproperties=font1)
plt.show()
plt.plot(x_axis_data, y_recall_score2, 'r.--', alpha=0.5, linewidth=1, label='recall_score_origin')
plt.plot(x_axis_data, y_recall_score, 'bo--', alpha=0.5, linewidth=1, label='recall_score_knn')
plt.legend()
plt.title(title, fontproperties=font1)
plt.xlabel('k', fontproperties=font1)
plt.ylabel('recall_score', fontproperties=font1)
plt.show()
print(knn_time)
y_f1_time = []
y_f1_time2 = []
for k in range(3, 61):
    y_f1_time.append(knn_time[k])
    y_f1_time2.append(origin_time)
plt.plot(x_axis_data, y_f1_time2, 'r.--', alpha=0.5, linewidth=1, label='time_origin')
plt.plot(x_axis_data, y_f1_time, 'bo--', alpha=0.5, linewidth=1, label='time_knn')
plt.legend()
plt.title(title, fontproperties=font1)
plt.xlabel('k', fontproperties=font1)
plt.ylabel('time(ms)', fontproperties=font1)
plt.show()
print(f1_score)
print(precision_score)
print(recall_score)