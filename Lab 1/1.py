
#Maisha Jarin
#id: 20101125
#Task 1:

def shiftLeft(source, k):
    i = 0

    while len(source) > k:
        source[i] = source[k]

        i = i + 1
        k = k + 1



    while len(source)>i:
        source[i] = 0

        i = i + 1


a = [10,20,30,40,50,60]

shiftLeft(a, 4)

print(a)
