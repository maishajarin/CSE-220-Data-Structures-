#Maisha Jarin
#id: 20101125
#Circular Array Task:3

import random

def leftRotate(l,n):
    lst=[0]*n
    lst[n-1]=l[0]
    for i in range(1,n):
        lst[i-1]=l[i]
    return lst


lst=["Mim","Sadia","Aysha","Jannat ","Zamila","Rahima","Maisha"]
length=len(lst)
while length!=1:
    x = random.randint(0, 3)
    lst=leftRotate(lst,length)
    if x==1:
        a=length//2
        for i in range(length):
            if i>a:
                lst[i-1]=lst[i]
        lst[length-1]=0
        length=length-1
        print(lst)

print(lst[0])