#TASK 2 (6)

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


def insert(self, newElement, index):
    inserted_value = Node(newElement, None)
    if index is None:
        if self.head is None:
            self.head = inserted_value
        else:
            tail = self.head
            while tail.next is not None:
                tail = tail.next
            tail.next = inserted_value
    elif index == 0:
        inserted_value.next = self.head
        self.head = inserted_value
    else:
        newTail = self.head
        for i in range(index - 1):
            newTail = newTail.next
        previous = newTail
        inserted_value.next = previous.next
        previous.next = inserted_value
    return self.head

ll = Mylist()
ll.insert()


