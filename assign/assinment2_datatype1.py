#1-Create alist
x = []
for i in range(0,2):
        a = input()
        x.append(a)

#2-add into list

x = x + ['google','apple','microsoft','tesla']
print(x)
#3-Count the number of time an object occurs in a list. 
for element in x:
	print(element + " occurs " + str(a.count(element)) + " times ")
# create list
a = [90,4,8,4,7,9]
a.sort()
print(a)
'''Given are two one-dimensional arrays A and B which are sorted in ascending order
. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order.
[List] '''
a = [1,2,3,4] 
b = [8,7,6,4]
c = a + b
print("List after merging a and b : " +str(c))
c.sort()
print("Sorted list after merging a and b : " + str(c))
#6-Implement a stack and queue using lists.
stack = ["Neha", "Mote", "chotu","Nitu"]
stack.append("Shubham")
stack.append("ABC")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
#Queue
from collections import deque
queue = deque(["Neha", "Mote", "chotu","Nitu"])
queue.append("Shubham")
print(queue)
queue.append(9)
print(queue)
queue.popleft()
queue.popleft()
print(queue)
#Count even and odd numbers in that list.
lis = [4,5,8,9,9,6,1,2]
print(lis)
even = 0
odd= 0
for i in lis:
    if(i%2==0):
        even = even + 1
    else:
        odd = odd + 1
print("the no of odd even count = " +str(even))
print(" the no of odd count is " + str(odd))

