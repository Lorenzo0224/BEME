import itertools

orders = list(itertools.permutations([1, 2, 3], 3))
size = len(orders)
count = 0
for i in range(size):
    print(orders[count])
    g = open("data/er_magellan/Structured/Amazon-Google/test.txt", "w")
    with open("data/er_magellan/Structured/Amazon-Google/newtest.txt", "r") as f:
        for i in f.readlines():
            i = i.split("\t")
            for index in range(2):
                j = i[index].split("COL")
                temp1 = j[orders[count][0]]
                temp2 = j[orders[count][1]]
                temp3 = j[orders[count][2]]
                j[1] = temp1
                j[2] = temp2
                j[3] = temp3
                i[index] = 'COL'.join(j)
            i = '\t'.join(i)
            g.writelines(i)
    g.close()
    count += 1
