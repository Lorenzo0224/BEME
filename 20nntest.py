import json
import time
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
data = "Beer"
predict = []
confidence = []
with open("ditto_Roberta/" + data + "_output_small.jsonl", 'r', encoding='utf8') as fp:
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
CLStest = [] = []
labelstest = []
with open("CLS_Roberta/" + data + "/CLStest.txt", "r", encoding='utf-8') as f:
    for i in f.readlines():
        j = i.split("\t")
        labelstest.append(int(j[1].split("\n")[0]))
        i = j[0].split(",")
        lenth = len(i)
        for index in range(lenth):
            i[index] = float(i[index])
        CLStest.append(i)
knn = KNeighborsClassifier(n_neighbors=20)
knn.fit(CLStrain, labelstrain)
a = knn.kneighbors(X=CLStest, n_neighbors=5, return_distance=True)
print(a)  # 错分样本和它对应的训练集中的5个近似样本
y_pred = knn.predict(CLStest)
print(y_pred)
y_f1_score = format(metrics.f1_score(labelstest, y_pred), '.4f')
y_precision_score = format(metrics.precision_score(labelstest, y_pred), '.4f')
y_recall_score = format(metrics.recall_score(labelstest, y_pred), '.4f')
print(y_precision_score)
print(y_recall_score)
print(y_f1_score)