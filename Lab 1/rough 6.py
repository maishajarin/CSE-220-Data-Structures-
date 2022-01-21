def series(n):
    array = [''] * n * n
    l = 0
    for i in range(n):
        for j in range(n - (i + 1)):
            array[l] = 0
            l += 1
        k = i + 1
        while k > 0:
            array[l] = k
            k -= 1
            l += 1
    print(array)
    return array


series(2)
