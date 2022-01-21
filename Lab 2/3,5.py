#TASK 3 (5)

class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next


class Mylist:
    def __init__(self, a):
        self.head = Node(a[0], None)
        tail = self.head
        for i in range(1, len(a)):
            temp = Node(a[i], None)
            tail.next = temp
            tail = tail.next

    def sum(self):
        s = 0
        tail = self.head
        while tail is not None:
            s += tail.element
            tail = tail.next
        print(s)
ll = Mylist()
ll.sum()
