# Q.1- Take 10 integers from user and print it on screen

for i in range(10):
    a = int(input("Enter a number: "))
    print(a)



# Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
#while(True):
#    print(a)



# Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

lis = []
sq = []
n = int(input("Enter the no. of elements in list: "))
for j in range(n):
    a = int(input("Enter the elements of list: "))
    lis.append(a)
for n in lis:
    sq.append(n*n)

print("original list: ",lis)
print("square list: ",sq)



#Q.4- From a list containing ints, strings and floats, make three lists to store them separately

lis = [1,2,3.5,4.6,'neha','rahman']
i = []
f = []
s = []
for n in lis:
    if (type(n) == int):
        i.append(n)
    elif (type(n) == float):
        f.append(n)
    else:
        s.append(n)

print("List of Integer: ", i)
print("List of Floats: ", f)
print("List of Strings: ", s)




# Q.5- Using range(1,101), make a list containing even and odd numbers.

a = []
b = []

for i in range(1,101):
    if i%2 == 0:
        a.append(i)
    else:
        b.append(i)

print("Even List ",a)
print("Odd List ", b)





# Q.6- Print the following patterns:
print("The pattern is")
for i in range(1,5):
    print(i*'*')




# Q.7- Create a user defined dictionary and get keys corresponding to the value using for loop.

a = {}
e = int(input('Enter the no. of items in dictionary: '))
for f in range(e):
    x = int(input('Enter a number: '))
    y = int(input('Enter age: '))
    a[x] = y
print(a)

print("value:key ")
for i in a:
    print(a[i],":",i)





'''Q.8- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found.
Iterate over list using for loop.'''


a = []
for i in range(10):
    x = int(input("Enter the elements of list: "))
    a.append(x)
print("previous list",a)
y = int(input("Enter the element to be removed: "))

a = [n for n in a if n != y]

print("Removed " , y , li)
