#TASK 3 (2)

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

    def find_element(self, value):
        flag = False
        tail = self.head
        while tail is not None:
            if tail.element == value:
                flag = True
            tail = tail.next
        print(flag)
ll = Mylist()
ll.find_element()