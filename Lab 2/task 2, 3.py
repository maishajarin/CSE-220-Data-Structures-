#TASK 2 (3)

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

    def isEmpty(self):
        if self.head == None:
            print(True)
        else:
            print(False)



ll = Mylist([])
ll.isEmpty()