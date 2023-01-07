#Number of trees
N = 18895

#Import coordinates about trees from file
data1 = []
with open("107_26.txt") as f:
    for line in f:
        data1.append([int(x) for x in line.split()])

data = sorted(data1)

#iterating over the coordinates of the planted trees
#recording every two tree planting sites,
#between which there are exactly 13 places
i = 0
j = 0
data13 = []
k = 0
h = 0
while (k != N-1):
    while (data[i + h][j] == data[i + h + 1][j]):
        if (data[i + h + 1][1] - data[i + h][1] - 1 == 13):
            data13.append(data[i + h])
            data13.append(data[i + h + 1])
        i += 1
        k += 1
    h += 1
    k += 1

#Output the free place for tree as in the task
print("Ответ: ряд: ", data13[-1][0], ", Место: ", data13[-2][1]+1)

