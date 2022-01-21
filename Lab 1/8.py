#Maisha Jarin
#id: 20101125
#Task 8:

def repetition(array):

    tempCount = []
    tempElement = []
    count = 1

    i = 0
    while (i <= len(array)):
        if i == len(array) -1:
            break

        count = 1
        j = i + 1
        while(j <= len(array)):
            if j == len(array):
                break

            if array[i] == array[j]:
                count = count+1
            j = j + 1

        if array[i] not in tempElement:
            tempElement.append(array[i])
            tempCount.append(count)
        i = i + 1

    temp3 = False
    #print(tempCount)
    #print(tempElement)

    for a in range(0,len(tempCount)):

        for b in range (a + 1, len(tempCount)):
            if (tempCount[a] == tempCount[b]) and (tempCount[a] != 1) :
                temp3 = True
                break



        if temp3 == True:
            break
    print(temp3)
    return temp3

repetition ([4,5,6,6,4,3,6,4])