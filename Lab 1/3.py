#Maisha Jarin
#id: 20101125
#Task 3:

def remove(source, size, idx):
    l = [0] * (len(source))

    for i in range(len(source)):
        if source[i] > source[idx] or source[i] < source[idx]:
            l[i] = source[i]
            i += 1
    while size > idx:
        l[idx] = l[idx + 1]
        idx += 1

    l[size - 1] = 0

    print(l)


source = [10, 20, 30, 40, 50, 0, 0]
remove(source, 5, 2)
