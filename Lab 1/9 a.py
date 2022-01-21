#Maisha Jarin
#id: 20101125
#Circular Array Task:1

def palcheck(array, size, start):
    palindrom = []
    i = 0
    while (i < size):
        palindrom.append(array[start])
        start += 1
        if (len(array) ==start):
            start = 0
        i += 1

    l = 0
    k = size - 1
    while (l <= k):
        if (palindrom[l] != palindrom[k]):
            return 0
        l += 1
        k -= 1
    return 1


array = [20, 10, 0, 0, 0, 10, 20, 30]
start = 5
size = 5
print(True if palcheck(array, size, start) else False)