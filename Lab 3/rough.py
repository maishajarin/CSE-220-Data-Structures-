def insert(self, newElement, index=None):
    s = 0
    tempVal = self.head.next
    while tempVal is not self.head:
        if tempVal.data == newElement:
            print('The key already exists')
            pass
        tempVal = tempVal.next
        s = s + 1

    if index is None:
        n = Node(newElement, None, None)
        n.prev = self.head.prev
        self.head.prev.next = n
        n.next = self.head
        self.head.prev = n
    else:
        if self.head.next != None:
            if (index > s) or (0 > index):
                print('invalid Index')
                pass
            else:
                x = 0
                n = Node(newElement, None, None)
                if index == 0:
                    n.next = self.head.next
                    self.head.next.prev = n
                    self.head.next = n
                    n.prev = self.head
                else:
                    tempVal = self.head.next
                    while tempVal is not self.head:
                        if x == index - 1:
                            n.next = tempVal.next
                            tempVal.next.prev = n
                            tempVal.next = n
                            n.prev = tempVal
                            break
                        x = x + 1
                        tempVal = tempVal.next
