#1-count length of tuple

tupl = ("Neha", "Mote", "chotu","Nitu")
print(" The Length of tuple is: ",len(tupl))

#2-Find largest and smallest elements of a tuples. 
tu = (2,4,6,7,8,5)
print("maximum element in tuple is : ",max(tu))
print("minimum element in tuple is : ",min(tu))
#Write a program to find the product of all elements of a tuple.
tup = (1,2,3,4,5,6)
a = 1
for i in tup:
    a=a*i
print("Product of all elements in tuple is: ",a)


'''# 3-Create two set using user defined values. 
Calculate difference between two sets.
Compare two sets.
Print the result of intersection of two sets.'''
s1 = set()
s2 = set()
for i in range(3):
    a = input('Enter elements for set 1: ')
    s1.add(a)

for j in range(5):
    a = input('\nEnter elements for set 2: ')
    s2.add(a)

print('Set one is: ',s1)
print('Set two is: ',s2)

d = s2 - s1
print("difference between two sets",d)

print(s2.difference(s1))#compare
m = set({0,2,2,3,1})
n = set({0,2,2,3,1})
print(m ^ n)
print(m == n)

p = set({3,4,5,6,7,})
print(m == p)      
print(m ^ p)
s = s1 & s2
print("Intersection of s1,s2",s)

print(s1.intersection(s2))



'''1- Create a dictionary to store name and marks of 10 students by user input. '''
a = {}
for i in range(2):
    Name = input("Enter the name of the student :")
    Marks = int(input("Enter the marks:"))
    a[Name] = Marks
    print("The new dictionary is ",a)

'''2-Sort the dictionary created in previous question according to marks.'''

b = tuple([(v,k) for k,v in a.items()])
c = sorted(b)
d = dict(c)
print("dictionary sorted according to marks..")
print(d)


#3- Count the number of occurrence of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary.


a = {}
for i in 'MISSISSIPPI':
    b = a.keys()
    if i in b:
        a[i]=a[i] + 1
    else:
        a[i] = 1
print("\n\noccurrence of each letter in word MISSISSIPPI",a)




