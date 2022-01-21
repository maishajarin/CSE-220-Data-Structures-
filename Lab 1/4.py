#Maisha Jarin
#id: 20101125
#Task 4:


def removeAll(source, size, element):
    i = 0
    while i < size:
        if source[i] == element:
            source[i] = 0
            shitfLeft(source, size, i)
            size -= 1
            if source[i] == element:
                i -= 1
        i += 1
    print(source)


def shitfLeft(l, size, idx):
    while size > idx:
        l[idx] = l[idx + 1]
        idx += 1

    l[size - 1] = 0


source = [10, 2, 30, 2, 50, 2, 2, 60, 0, 0]
removeAll(source, 8, 2)
