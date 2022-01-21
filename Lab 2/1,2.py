#TASK 1 (ii)
class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class Mylist:
    def __init__(self, a):
        if len(a)==0:
            self.head= None
        else:
            self.head = Node(a[0], None)
            tail = self.head
            for i in range(1, len(a)):
                temp = Node(a[i], None)
                tail.next = temp
                tail = tail.next

    def showList(self):
        if self.head == None:
            print('Empty List')
        else:
            n = self.head
            while n is not None:
                print(n.element, end=' ')
                n = n.next
            print()



ll = Mylist([])
ll.showList()