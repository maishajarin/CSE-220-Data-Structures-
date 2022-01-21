# id_20101125
# 1a
def factorial(n):  # In this case, factorial is the name of a function.
    if n == 0:
        return 1

    return n * factorial(n - 1)


# Driver Code
number = 8;
print("Factorial of", number, "is",
      factorial(number), ".")


# id_20101125
# 1b
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 0:
        return 0
    # Second Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# Driver Program
number = 25;
print("Fibonacci of", number, "is",
      Fibonacci(number), ".")


# id_20101125
# 1c
def arrayelemnents(array):
    if len(array) > 1:
        a = array[0]
    else:
        return array[0]
    array = array[1:]
    return f'{a}, {arrayelemnents(array)}'


lst = [1, 3, 4, 5, 6, 7, 2]
print(arrayelemnents(lst))


# id_20101125
# 1d
def power(a, b):
    if (b == 0):
        return 1
    return a * power(a, b - 1)


# Driver Code
a = 2;
b = 3
print("powerN(", a, ",", b, ")→", power(a, b), ".")


# id_20101125
# 2a
def find(decimalnumber):  # In this case, find is the name of a function.
    if decimalnumber == 0:
        return 0
    else:
        return (decimalnumber % 2 + 10 *
                find(int(decimalnumber // 2)))


# Driver Code
decimalnumber = 2
print("The binary number of the decimal", decimalnumber, "is",
      find(decimalnumber), ".")


# id_20101125
# 2b
def add(n):  # n is Node #add is the function to all the elements
    if n is None:
        return 0
    else:
        return n.element + add(n.next)


# id_20101125
# 2c
def reverseprinting(n):  # n is Node #everseprinting is the function for reversed order
    if n is None:
        return
    else:
        reverseprinting(n.next)
        print(n.element)


# id_20101125
# 3
def hocBuilder(height):
    # base case for height=0
    if (height == 0):
        return 0
    # if it is the top of the building then cards will be 8
    if (height == 1):
        return 8

    # if it is not the top of the building then for each level 5 cards will be added
    return hocBuilder(height - 1) + 5


# taking input from the user
n = int(input("Enter the height:"))

# calling the function for the required height and printing its value
print(hocBuilder(n))


# id_20101125
# 5a
def printrecursionpattern(n):
    if (n > 0):
        printrecursionpattern(n - 1)
        print(n, end=" ")


def pattern1(n):
    if (n > 1):
        pattern1(n - 1)
    printrecursionpattern(n)
    print()


pattern1(5)


# id_20101125
# 5b
def printrecursionspace(space):
    if (space == 0):
        return;
    print(" ", end=" ")
    printrecursionspace(space - 1)


def print_number(num):
    if (num > 0):
        print_number(num - 1)
        print(num, end=" ")


def pattern2(n, num):
    if (n == 0):
        return
    printrecursionspace(n - 1)
    print_number(num - n + 1)
    print()
    pattern2(n - 1, num)


pattern2(5, 5)


# id_20101125
# 6
class FinalQ:
    def print(self, array, idx):
        if (idx < len(array)):
            profit = self.calcProfit(array[idx])
            print(str(idx + 1) + ". Investment: " + str(array[idx]) + "; Profit: " + str(profit))
            self.print(array, idx + 1)

    def calcProfit(self, investment):
        if investment <= 25000:
            return 0.0
        else:
            val = investment - 100000
            val = val / 100
            val = val + val + val + val + val + val + val + val
            return val + 3375.0


# Tester
array = [25000, 100000, 250000, 350000]
f = FinalQ()
f.print(array, 0)