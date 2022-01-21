#TASK 3 (3)
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

    def reverse(self):
        newHead = None
        n = self.head

        while n is not None:
            nextNode = n.next

            n.next = newHead

            newHead = n

            n = nextNode
        self.head = newHead
        return self.head
ll = Mylist()
ll.reverse()