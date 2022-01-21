#Maisha Jarin
#id: 20101125
#Task 5:

def split(array):
    a = 0
    b = 0
    result= "false"
    for i in range(len(array)):
        a += array[i]
        for j in range(i + 1, len(array)):
            b += array[j]
        if a == b:
            result = "true"
        else: pass
        b = 0
    print(result)
    return result
split([1, 1, 1, 2, 1])
