#Question no 1
def recursivelyselectionsort(s,a,b):
    l=len(s)

    if(a<l):
        minimum=a
        while(b<l):
            if s[b]<s[minimum]:
                minimum=b
            b+=1
        temp=s[a]
        s[a]=s[minimum]
        s[minimum]=temp

        recursivelyselectionsort(s,a+1,a+2)

s=[13,25,0,-4,7,-1,18,9,-6,21]
a=0
b=a+1
recursivelyselectionsort(s,a,b)
print('#Question no 1')
print(s)

#Question no 2
def recursivelyinsersionsort(s,a):
    l=len(s)
    if(a==l):
        return -1
    else:
        b=0
        minimum=a
        while b<a:

            if(s[a]<s[b]):
                temp=s[a]
                s[a]=s[b]
                s[b]=temp
            b+=1
        recursivelyinsersionsort(s,a+1)
a=1
s=[1,5,7,6,3,8,9,9]
recursivelyinsersionsort(s,a)
print('#Question no 2')
print(s)


#Question no 3

    def bubbleSort(self):
        temp1=self.head
        temp2=temp1.next
        c=0
        pred = temp1
        t=self.head
        length=0
        while(t!=None):
            length+=1
            t=t.next
        while(c!=length):
            temp1 = self.head
            temp2 = temp1.next
            while(temp2!=None):
                if(temp1.data>temp2.data):
                    if(temp1==self.head):
                        temp1.next=temp2.next
                        temp2.next=temp1

                        pred=temp2
                        self.head=temp2
                        t=temp2
                        temp2=temp1
                        temp1=t
                    else:
                        temp1.next = temp2.next
                        temp2.next = temp1
                        pred.next=temp2
                        pred=temp2
                        t = temp2
                        temp2 = temp1
                        temp1 = t
                temp1=temp1.next
                temp2=temp2.next
            c+=1
            pred=self.head

#Question no 4
    def selection_Sort_list(self):

        key=self.head
        temp=key.next

        t = self.head
        length = 0
        while (t != None):
            length += 1
            t = t.next
        c=0
        while(key.next!=None):
            min=key
            temp=key.next
            while(temp!=None):
                if(temp.data<min.data):
                    min=temp
                temp=temp.next
            a=key.data
            key.data=min.data
            min.data=a
            key=key.next

arr=[9,10,50,5,6,2,3,8]
l=len(arr)
link=MyList(arr)
link.bubbleSort()
print('#Task3')
link.showList()


arr=[1,4,2,4,6,8,5,3,2,4,6,7,54]
link=MyList(arr)
link.selection_Sort_list()
print('#Task 4')
link.showList()


#Question no 5
class Node:
    def _init_ (self, data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyList:
    def __init__(self,a):
        if isinstance(a,list):
            if(a!=None):

                self.head = Node(None)
                self.head.next=self.head
                self.head.prev=self.head
                tail = self.head

                for i in a:
                    n=Node(i)

                    tail.next=n
                    n.prev=tail
                    tail=tail.next
                    tail.next=self.head
                    self.head.prev=tail

    def showList(self):
        temp = self.head.next
        if (temp.data == None):
            print('Empty List')
        else:
            while (temp != self.head):
                print(temp.data)
                temp = temp.next

    def insertion_Sort_list(self):
        temp1=self.head.next
        temp2=temp1.next
        while(temp2!=self.head):
            temp1=temp2.prev
            while(temp1!=self.head):

                if(temp1.data>temp2.data):
                    t=temp1.data
                    temp1.data=temp2.data
                    temp2.data=t
                    temp2=temp2.prev

                temp1=temp1.prev
            temp2=temp2.next

arr=[9,5,6,2,3,8]
l=len(arr)
link=DoublyList(arr)
link.insertion_Sort_list()
print('#Task5')
link.showList()

#Question no 6
def binary_search_algorithm(a,l,r,n):
    b=int((l+r)/2)
    if(a[b]==n):
        print('Exists in the index '+str(b))
        return 0
    elif(a[b]<n):
        return binary_search_algorithm(a,b+1,len(a)-1,n)
    elif(a[b>n]):
        return binary_search_algorithm(a,0,b-1,n)



a=[10,30,50,70,80,90,110,130,140,150,220]
l=0
r=len(a)-1
n=90
print('#Question no 6')
binary_search_algorithm(a,l,r,n)

#Question no 7
def fibonacci_number(n):
    if(a[n-1])!=0:
        return a[n-1]
    elif(n==1 or n==2):
        f= 1

    elif(n>2):
        f=fibonacci_number(n-1)+fibonacci_number(n-2)

    a[n-1]=f
    return a[n-1]
n=8
a=[0]*n
print('#Question no 7')
print(fibonacci_number(n))

#Question no 7
def fibonacci_number(n):
    if(a[n-1])!=0:
        return a[n-1]
    elif(n==1 or n==2):
        f= 1

    elif(n>2):
        f=fibonacci_number(n-1)+fibonacci_number(n-2)

    a[n-1]=f
    return a[n-1]
n=8
a=[0]*n
print('#Question no 7')
print(fibonacci_number(n))
