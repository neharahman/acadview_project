
import time

# Q.1- What is Time Tuple?

print(" A tuple is a sequence of immutable Python objects.")
print ("Tuples are sequences, just like lists. The differences between tuples and lists are,")
print ("the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.")
print("Creating a tuple is as simple as putting different comma-separated values.")





# Q.2- Write a program to get formatted time.

print("\nFormatteed time: ")
n = time.ctime()
print(n)


# Q.3- Extract month from the time.
print("\n\nthe month is: ",n[1:2])

# Q.4- Extract day from the time.
print("the day is: ",time.ctime()[1:3])

# Q.5- Extract date (ex : 11 in 11/01/2021) from the time.
import datetime
x = datetime.datetime.now()
print("\n\n")
print(d.strftime("%d/%m/%Y"))
print("Date in d: ", x.day)

# Q.6- Write a program to print time using localtime method.
localtime = time.asctime( time.localtime(time.time()) )
print ("\n\nLocal current time :", localtime)

# Q.7- Find the factorial of a number input by user using math package functions. Q.8- Find the GCD of a number input
import math
a = int(input("\n\nenter the no. to calculate it's factorial: "))
print(math.factorial(a))


# Q.8- Find the GCD of a number input by user using math package functions.
x =  int(input("\n\nenter the 1st no. to calculate gcd : "))
y = int(input("enter the 2nd no. to calculate gcd : "))
print('GCD of ',x ,' and ', y, ' is ', math.gcd(x,y))



# Q.9- Use OS package and do the following tasks:
# 1. Get current working directory.
# 2. Get the user environment.

import os
print("\n\ncuurent working directory: \n",os.getcwd())


print("\n\nUSER ENV: \n: ", os.environ['HOME'])

print("\n\nEnvornment variables: \n: ", os.environ)
