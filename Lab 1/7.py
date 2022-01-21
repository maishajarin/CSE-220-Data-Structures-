#Maisha Jarin
#id: 20101125
#Task 7:

def bunch(array):
    temp = 0
    maxBunch = 0

    i = 0
    while i in range(len(array)):
        if i == len(array)-1:
            break

        if array[i] == array[i + 1]:
            temp = temp + 1
        else:
            temp = 0

        if temp > maxBunch:
            maxBunch = temp
        i = i + 1

    maxBunch = maxBunch + 1
    print(maxBunch)
    return maxBunch


bunch([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1])
