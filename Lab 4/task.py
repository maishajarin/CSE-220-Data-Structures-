#task 1
def result(exp):
    k = 0
    stk = []
    str_llist = []
    number = -1
    for item in exp:
        if item == '{' or item == '(' or item == '[':
            stk.append(item)
            k += 1
            str_llist.append(k)
            number = -1
        elif item == ')':
            last = '('
            if len(stk) == 0 or stk[len(stk)-1] != last:
                k += 1
                if len(stk) == 0:
                    print('The expression is NOT correct')
                    print(f'Error at character # {k}. "{item}"- not opened')
                    return
                else:
                    print('The expression is NOT correct')
                    print(
                        f'Error at character # {str_llist.pop()}. "{stk[len(stk) -1]}"- not closed')
                    return
            else:
                stk.pop()
                str_llist.pop()
                k += 1

        elif item == '}':
            last = '{'
            if len(stk) == 0 or stk[len(stk) - 1] != last:
                k += 1
                if len(stk) == 0:
                    print('The expression is NOT correct')
                    print(f'Error at character # {k}. "{item}"- not opened')
                    return
                else:
                    print('The expression is NOT correct')
                    print(
                        f'Error at character # {str_llist.pop()}. "{stk[len(stk) -1]}"- not closed')
                    return

            else:
                stk.pop()
                k += 1

        elif item == ']':
            last = '['
            if len(stk) == 0 or stk[len(stk) - 1] != last:
                k += 1
                if len(stk) == 0:
                    print('The expression is NOT correct')
                    print(f'Error at character # {k}. "{item}"- not opened')
                    return
                else:
                    print('The expression is NOT correct')
                    print(
                        f'Error at character # {str_llist.pop()}. "{stk[len(stk) -1]}"- not closed')
                    return
            else:
                stk.pop()
                k += 1

        else:
            if item.isnumeric() and number == -1:
                k += 1
                number = item
            elif item.isnumeric() and number != -1:
                pass
            else:
                number = -1
                k += 1

    print('The expression is correct')


exp = input()
result(exp)

#task 2


class node:
    def __init__(self, data=None):
        self.data = data
        self.address = None
        self.previous = None


class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = node()
        self.k = 0
        self.number = -1
        self.total = 0
        self.llist = []

    def append(self, element):
        new_node = node(element)
        current = self.head
        if current.address is None:
            current.address = new_node
            current = current.address
            self.tail = current
            current.previous = self.head

        else:
            while current.address is not None:
                current = current.address
            temp = current
            current.address = new_node
            current = current.address
            current.previous = temp
            self.tail = current
        self.k += 1
        self.number = -1
        self.total += 1
        self.llist.append(self.k)

    def traverse(self, item, main):
        if self.total == 0 or self.tail.data != item:
            self.k += 1
            if self.total == 0:
                print('The expression is NOT correct')
                print(f'Error at character # {self.k}. "{main}"- not opened')
                return
            else:
                print('The expression is NOT correct')
                print(
                    f'Error at character # {self.llist.pop()}. "{self.tail.data}"- not closed')
                return
        else:
            current = self.tail
            self.tail = current.previous
            current.address = None
            current.previous = None
            self.tail.address = None
            self.total -= 1
            self.k += 1
            self.llist.pop()
        return self.number

    def extra(self, item):
        self.k += 1
        self.number = 0
        return self.number

    def extra1(self, item):
        self.number = -1
        self.k += 1
        return self.number
    def final_check(self):
        if self.total != 0:
            print('The expression is NOT correct')
            print(f'Error at character # {self.llist.pop()}. "{self.tail.data}"- not closed')
        else:
            print('The expression is correct')

output = -1
exp = input()
result = linked_list()
for item in exp:
    if item == '{' or item == '(' or item == '[':
        result.append(item)
    elif item == ')':
        last = '('
        output = result.traverse(last, item)
        if output == None:
            break

    elif item == '}':
        last = '{'
        output = result.traverse(last, item)
        if output == None:
            break
    elif item == ']':
        last = '['
        output = result.traverse(last, item)
        if output == None:
            break
    else:
        if item.isnumeric() and output == -1:
            output = result.extra(output)

        elif item.isnumeric() and output != -1:
            pass
        else:
            output = result.extra1(output)

if output != None:
    result.final_check()
else:
    pass