#TASK 2 (1)
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

    def print(self):
        n = self.head
        while n is not None:
            if n.next is not None:
                print(n.element, end=", ")

            else:
                print(n.element)
            n = n.next


ll = Mylist([1, 2, 3, 4])
ll.print()
