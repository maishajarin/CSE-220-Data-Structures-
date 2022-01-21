#TASK 3 (6)
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

    def rotate(self, position, k=1):
        tail = self.head
        if tail == None:
            print('Empty List')
            return
        elif tail.next == None:
            print(tail.element)
            return
        else:
            if position.lower() == 'left':
                for i in range(k):
                    prev = self.head
                    self.head = self.head.next
                    tail = self.head

                    while tail.next is not None:
                        tail = tail.next
                    tail.next = prev
                    prev.next = None
                return self.head

            elif position.lower() == 'right':
                for i in range(k):
                    tail = self.head
                    while tail.next.next is not None:
                        tail = tail.next
                    ct = tail.next
                    ct.next = self.head
                    self.head = ct
                    tail.next = None
                return self.head
ll = Mylist()
ll.rotate()