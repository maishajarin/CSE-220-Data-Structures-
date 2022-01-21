#TASK 3 (4)

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

    def sort(self):
        tail = self.head
        l = []
        while tail is not None:
            l.append(tail.element)
            tail = tail.next
        l.sort()
        head = None
        tail = None
        for i in l:
            n = Node(i, None)
            if head == None:
                head = n
                tail = n
            else:
                tail.next = n
                tail = tail.next
        self.head = head
ll = Mylist()
ll.sort()