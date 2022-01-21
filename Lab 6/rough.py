#Sort a singly linked sequential list using bubble sort algorithm.

class Node:
    def init(self, Value = None, next = None):
        self.Value = Value
        self.next = next


class Linkedlist:
    def init(self):
        self.head = None


    def push(self, value):

        node = Node(value)
        node.next = self.head
        self.head = node



    def bubble_sort(self):
        temp2 = None

        while self.head.next != temp2:
            a = self.head

            while a.next != temp2:
                b = a.next

                if a.Value > b.Value:
                    b.Value, a.Value = a.Value, b.Value
                a = a.next

            temp2 = a


    def showlist(self):
        temp = self.head

        while temp != None:
            print(temp.Value, end=" -> ")
            temp = temp.next

        print("\b\b\b\b")


#Testing

test = Linkedlist()

arr = [525,2442,4820,10]

for i in arr:
    test.push(i)

print("Not Sorted:", end=" ")
test.showlist()

test.bubble_sort()

print("Sorted:", end=" ")
test.showlist()