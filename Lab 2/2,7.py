#TASK 2 (7)

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


def remove(self, deletekey):
    tail = self.head
    new = None
    while tail is not None and tail.element is not deletekey:
        new = tail
        tail = tail.next
    new.next = tail.next
    return self.head
ll = Mylist()
ll.remove()
