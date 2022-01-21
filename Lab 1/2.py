
#Maisha Jarin
#id: 20101125
#Task 2:

def rotateLeft(source, k):
    b = [0]*(len(source))


    for i in range(len(source)):
        b[i-k] = source[i]
    #    i += 1
    j= 0
    while j < k:
        b[j] = source[j-k]
        j += 1
    print(b)



a = [10,20,30,40,50,60]

rotateLeft(a, 3)
