def remove( source, size, idx):
    l = []


    for i in range(len(source)):
        if source[i] > source[idx] or source[i] < source[idx]:
            l=i
    for i in range(len(source)-len(l)):
        l.append(0)
    print(l)


source = [10,20,30,40,50,0,0]
remove(source, 5,2)