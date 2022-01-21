#Maisha Jarin
#id: 20101125
#Task 6:

def array(n):
    temp = [''] * n * n
    a = 0
    i = 0

    while i < n:
        j = 0
        while j < n - (i + 1):
            temp[a] = 0
            a = a + 1
            j = j + 1

        b = i + 1

        while b > 0:
            temp[a] = b
            b = b - 1
            a = a + 1
        i = i + 1

    print(temp)


array(2)
