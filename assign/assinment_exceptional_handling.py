
#Q.1- Name and handle the exception occured in the following program:
'''a=3
if a<4:
    a=a/(a-3)
    print(a)#ZeroDivisionError
    '''

#handle
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)

except ZeroDivisionError:
    print("You can't divide by zero, you're silly")

'''
Q.2- Name and handle the exception occurred in the following program: 
l=[1,2,3]
print(l[3])
#IndexError
'''

l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("it cross index value")
finally:
    print("put value according to index")
'''
Q.3- What will be the output of the following code:
# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise  # To determine whether the exception was raised or not
#exception will raise
'''


'''Q.4- What will be the output of the following code:
 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


#first it gives -5.0 and then a/b result in 0
'''

'''Q.5- Write a program to show and handle following exceptions:
1. Import Error
2. Value Error
3. Index Error

'''
#ValueError
try:
    x = int(input("Enter a number "))
except ValueError as E:
    print("enter int value",E)
else:
    print(x)
#IndexError
lis = ['mote','chotu']
try:
    print(lis[5])
except IndexError as E:
    print("handle exception",E)
else:
    print(lis[5])

'''Q.6- Create a user-defined exception AgeTooSmallError()
that warns the user when they have entered age less than 18. The code must keep taking input till the user enters the appropriate age number(less than 18)
'''

class User_defided(Exception):
    pass
try:
    n = int(input("enter your valid age here "))
except ValueError:
    print("int value only")
    n = int(input("enter your valid age again "))
while (n <= 18):
    try:
        if (n < 18):
            raise User_defided
    except User_defided:
        print("enter age greater than 18")
        n = int(input("enter age again it shoud be greater then 18"))

print("Age is ",n)
