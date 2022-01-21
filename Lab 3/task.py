class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None


class DoublyList:
    def __init__(self, a):
        if isinstance(a, list):
            if len(a) == 0:
                self.head = None
            else:
                self.head = Node(None)
                self.head.next = self.head
                self.head.prev = self.head
                tail = self.head
                for i in range(0, len(a)):
                    temp = Node(a[i])
                    tail.next = temp
                    temp.prev = tail
                    tail = tail.next
                    tail.next = self.head
                    self.head.prev = tail

    def showList(self):
        tempVal = self.head.next
        if tempVal == self.head:
            print("Empty List")
        else:
            while tempVal is not self.head:
                print(tempVal.element)
                tempVal = tempVal.next

    def insert(self, newElement):

        tempVal = Node(newElement)
        tail = self.head.prev
        tail.next = tempVal
        tempVal.prev= tail
        tail = tail.next
        tail.next = self.head
        self.head.prev = tail

    def remove(self, index):
        tail = self.head.next
        tempVal = self.head.next
        c = 0
        while tempVal.next is not self.head:
            c = c + 1
            tempVal = tempVal.next

        if (index < 0) or (index > c):
            raise Exception("Invalid index")
        rmv = None
        if index == 0:
            tail = self.head

        else:
            for i in range(index - 1):
                tail = tail.next
        rmv = tail.next
        tail.next = rmv.next
        rmv.next.prev = tail
        rmv.next = None
        rmv.prev = None
        return rmv.element

    def removeKey(self, deleteKey):
        tail = self.head.next
        newkey = None
        if tail is None:
            return self.head
        else:
            while (tail != self.head) and (tail.element != deleteKey):
                newkey = tail
                tail = tail.next
            if newkey is None:
                k = self.head.next
                self.head.next = k.next
                k.next.prev = self.head
                k.next = None
                k.prev = None
            else:
                newkey.next = tail.next
                tail.next.prev = newkey
                tail.next = None
                tail.prev = None
        return tail.element

ll= [1,5,3,9,7]
ll = DoublyList(ll)
ll.showList()
ll.insert(7)
ll.remove(2)
ll.removeKey(2)
