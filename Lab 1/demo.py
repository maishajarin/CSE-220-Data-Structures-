def shiftLeft(source, k):
    i = 0
    temp=0
    y=k

    while len(source)>k:

        temp= source[i]

        source[i] = source[k]
        source[k]= temp

        i = i + 1
        k = k + 1
        if k>len(source):
            k=k-y



    #while len(source)>i:
        #source[i] = 0

        #i = i + 1


a = [10,20,30,40,50,60]

shiftLeft(a, 4)

print(a)