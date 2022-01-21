#TASK 3 (1)
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

    def evenNumbers(self):
        tail = self.head

        while tail is not None:
            if tail.element % 2 == 0:
                print(tail.element, end='->')
            tail = tail.next
        print()
ll = Mylist()
ll.evenNumbers()