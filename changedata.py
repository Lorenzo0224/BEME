# 交换属性顺序
def changeOrder(readFile="newtest.txt", writeFile="test2.txt"):
    g = open(writeFile, "w")
    with open(readFile, "r") as f:
        for i in f.readlines():
            i = i.split("\t")
            for index in range(2):
                j = i[index].split("COL")
                temp = j[3]
                j[3] = j[2]
                j[2] = j[1]
                j[1] = j[4]
                j[4] = temp
                i[index] = 'COL'.join(j)
            i = '\t'.join(i)
            g.writelines(i)
    g.close()


def changeOrder2(readFile="data/er_magellan/Structured/Watches/test2.txt", writeFile="data/er_magellan/Structured"
                                                                                     "/Watches/test.txt"):
    g = open(writeFile, "w")
    with open(readFile, "r") as f:
        for i in f.readlines():
            i = i.split("\t")
            for index in range(2):
                j = i[index].split("COL")
                temp1 = j[3]
                temp2 = j[2]
                temp3 = j[1]
                j[1] = temp1
                j[2] = temp2
                j[3] = temp3
                i[index] = 'COL'.join(j)
            i = '\t'.join(i)
            g.writelines(i)
    g.close()


# 读取Bert生成的CLS，可能会有一些小错误，adjustCLS调整
def extractCLS(modelFile="ditto_Roberta/", dataset="Beer/", dataSize=91):
    sum = 0
    with open(modelFile + dataset + "numpy.txt", "r", encoding='utf-8') as f:
        for i in f.readlines():
            sum += 1
    count = sum - dataSize * 128  # 768维的向量，每行6个数，共128行
    flag = 0
    g = open(modelFile + dataset + "numpy2.txt", "w")
    with open(modelFile + dataset + "numpy.txt", "r") as f:
        for i in f.readlines():
            flag += 1
            if flag > count:
                g.writelines(i)
    g.close()
    g = open(modelFile + dataset + "numpy.txt", "w")
    with open(modelFile + dataset + "numpy2.txt", "r") as f:
        for i in range(dataSize):
            s = ""
            for j in range(128):
                line = f.readline().split("\n")
                s += line[0]
            g.writelines(s + "\n")
    g.close()


# 调整提取的CLS
def adjustCLS(modelFile="ditto_Roberta/", dataset="Beer/"):
    g = open(modelFile + dataset + "numpy.txt", "w")
    s = ""
    with open(modelFile + dataset + "numpy1.txt", "r", encoding='utf-8') as f:
        for i in f.readlines():
            s = s + i.split("\n")[0]
    s = s.split("][")
    lenth = len(s)
    s[lenth - 1] = s[lenth - 1].split("]")[0]
    print(lenth)
    for i in range(lenth):
        g.writelines(s[i] + "\n")
    g.close()


# 保存错分样本的CLS Embedding
def save_errorCLS(modelFile="ditto_Roberta/", dataset="Walmart_Amazon", CLSfile="CLS_Roberta/"):
    count = 1
    entity = []
    with open(modelFile + dataset + "/test_result.txt", "r", encoding='utf-8') as f:
        for i in f.readlines():
            i = i.split(" ")
            j = i[1].split("\n")
            if i[0] != j[0]:
                entity.append(count)
            count += 1
    print(len(entity))
    entity.append("0")
    flag = 1
    index = 0
    g = open(CLSfile + dataset + "/CLStest.txt", "w")
    with open("CLStest/" + dataset + ".txt", "r", encoding='utf-8') as f:
        for line in f.readlines():
            if flag == entity[index]:
                index += 1
                g.writelines(line)
            flag += 1
    g.close()


# 判断是不是数字,例如-1.8909e-01是数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 为CLS向量标注label
def labelCLS(labelFile="Beer/test.txt", modelFile="ditto_Roberta/", dataset="Beer/"):
    label = []
    with open("data/er_magellan/Structured/" + labelFile, "r", encoding='utf-8') as f:
        for i in f.readlines():
            i = i.split("\t")
            label.append(i[2])
    print(len(label))
    count = 0
    g = open(modelFile + dataset + "CLStest.txt", "w")
    with open(modelFile + dataset + "numpy.txt", "r", encoding='utf-8') as f:
        for i in f.readlines():
            i = i.split("\n")
            s = i[0]
            s = s.split(" ")
            lenth = len(s)
            print(lenth)
            CLS = ""
            for j in range(lenth):
                if is_number(s[j]):
                    CLS = CLS + s[j] + ","
            g.writelines(CLS.strip(',').strip("\n") + "\t" + label[count])
            count += 1
    g.close()
    print(count)


# 处理匹配结果的output_small.jsonl，键值包括left，right，match，match_confidence
def deal_json():
    import json
    label = []
    with open('output/output_small.jsonl', 'r', encoding='utf8') as fp:
        for line in fp.readlines():
            js_l = json.loads(line)
            label.append(js_l["match"])
    h = open("test_result.txt", "w", encoding='utf-8')
    count = 0
    with open("data/er_magellan/Structured/Watches/test.txt", "r") as f:
        for i in f.readlines():
            j = i.split("\t")
            j = j[2].split("\n")
            h.writelines(j[0] + " " + str(label[count]) + "\n")
            count += 1
    h.close()


if __name__ == "__main__":
    save_errorCLS(modelFile="ditto_Roberta/", dataset="Watches", CLSfile="CLS_Roberta/")
