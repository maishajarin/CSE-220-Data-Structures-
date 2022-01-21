#SUMMER21 CSE220 Lab 7
#Assignment 07: Key Index Searching & Sorting, Hashing
#Task 1 on Key index Searching & Sorting
#2101125
class KeyIndex:
    def __init__(self, a):
        self.a = a
        minimum = 0
        maximum = 0

        for i in self.a:
            if i > maximum:
                maximum = i
            elif i < minimum:
                minimum = i

        if minimum < 0:
            minimum = minimum * (-1)

        for i in range(len(self.a)):
           self.a[i] = self.a[i]+minimum

        maximum = maximum+minimum

        self.k = [0]*(1+maximum)

        for i in range(len(self.a)):
            element = self.a[i]
            self.k[element] = self.k[element]+1

        for i in range(len(self.a)):
           self.a[i] = self.a[i]-minimum

    def search(self, val):
        minimum = 0
        maximum = 0

        for i in self.a:
            if i > maximum:
                maximum = i
            elif i < minimum:
                minimum = i

        if minimum < 0:
            minimum = minimum * (-1)

        val = val+minimum

        if self.k[val] != 0:
            return True
        else:
            return False

    def sort(self):
        minimum = 0
        maximum = 0
        s = [0]*len(self.a)
        index = 0

        for i in self.a:
            if i > maximum:
                maximum = i
            elif i < minimum:
                minimum = i

        if minimum < 0:
            minimum = minimum * (-1)

        for i in range(len(self.k)):
            if self.k[i] != 0:
                for j in range(self.k[i]):
                    s[index] = i-minimum
                    index += 1

        for i in range(len(s)):
            self.a[i] = s[i]

        return self.a


arr = [10,-1,-3,9,-4,5,20,-1,3]

b = KeyIndex(arr)
print(b.search(3))
print(b.sort())

#Task 2 on Hashing
class Hashing:
    def __init__(self, array):
        self.arr = array

    def hash_calculation(self):

        string_list = [0]*len(self.arr)

        for j in self.arr:
            sum = 0
            const = 0
            for i in j:
                if (ord(i) > 65 and ord(i) < 69) or (ord(i) > 69 and ord(i) < 73) or (ord(i) > 73 and ord(i) < 79) or (
                        ord(i) > 79 and ord(i) < 85) or (ord(i) > 85 and ord(i) < 91):
                    const += 1

                elif ord(i) > 47 and ord(i) < 58:
                    sum = sum + int(i)

            index = ((const * 24) + sum) % 9

            if string_list[index]==0:
                string_list[index] = j
            else:
                for k in range(index+1,len(string_list)):
                    if string_list[k] == 0:
                        string_list[k] = j
                        break
                else:
                    for l in range(index):
                        if str_list[l] == 0:
                            str_list[l] = j
                            break

        return string_list

a = ['ST189B832','ST189B832','ABCU123','ABC123','ABX','MA59']
b = Hashing(a)
print(b.hash_calculation())


