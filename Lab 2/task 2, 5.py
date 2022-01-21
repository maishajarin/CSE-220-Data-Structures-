#TASK 2 (5)

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

    def insert(self, newElement):
        n = self.head

        while n is not None:
            if n.next is not None:
                if n.element is newElement:
                    print("already exists")
                    return
            else:
                if n.element is newElement:
                    print("already exists")
                    return
                else:
                    temp = Node(newElement, None)
                    n.next = temp
                    return
            n= n.next

    def showList(self):
        if self.head == None:
            pass
        else:
            n = self.head
            while n is not None:
                print(n.element, end=' ')
                n = n.next
            print()
ll = Mylist([1,2,3])
ll.insert(3)
ll.showList()


