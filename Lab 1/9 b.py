#Maisha Jarin
#id: 20101125
#Circular Array Task:2

def intersection(a, b, aSize, bSize, aStart, bStart):
    leanA = [0] * aSize
    leanB = [0] * bSize

    i = 0
    while (i < aSize):
        leanA[i] = a[(aStart + i) % len(a)]
        i = i + 1

    i = 0
    while (i < bSize):
        leanB[i] = b[(bStart + i) % len(b)]
        i = i + 1

    output = []
    for i in leanA:
        for j in leanB:
            if i == j:
                output.append(i)
    return output


a = [40, 50, 0, 0, 0, 10, 20, 30]
start_1 = 5
size_1 = 5
b = [10, 20, 5, 0, 0, 0, 0, 0, 5, 40, 15, 25]
start_2 = 8
size_2 = 7
output = intersection(a, b, size_1, size_2, start_1, start_2)
print(*output)
