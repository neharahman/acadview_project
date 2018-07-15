#Q.1- Create a function to calculate the area of a circle by taking radius from user.
import math
def circle_area(r):
    return math.pi * r**2
radius = float(input("Enter radius of circle: "))
circle_area = circle_area(radius)
print("Area of circle is:", circle_area)




'''Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the
 perfect numbers between 1 and 1000.
[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number.'''

def perfect(a):
    su = 0
    for i in range(1, a):
        if (a % i == 0):
            su = su + i

    if (a == su):
        print(' the number is perfect')
    else:
        print(' the number is not perfect')

x = int(input("Enter the no. to be checked for perfect or not: "))
perfect(x)

'''Q.3- Print multiplication table of 12 using recursion.'''
def Multiplication(a,i=1):
    if i>10:
        print("need 1 to 10 numbers only")
    else:
        print(a, ' X ' , i ,' = ',  a*i)
        return Multiplication(a,i+1)
mu = int(input("Enter the no. to print 12 table "))
Multiplication(mu)

#6 Write a function to find factorial of a number but also store the factorials calculated in a dictionary

fact = {1:11,1:22}

def factorial(num):
    if num in fact.keys():
        return fact[num]
    else:
        a = num*factorial(num-1)
        fact[num] = a
        return a

p = int(input("Enter the no. to calculate factorial : "))
print(factorial(p))
print(fact)



#5Write a function to calculate power of a number raised to other ( a^b ) using recursion

def power_of_num(n: int , m: int)->int:
        if (m == 1):
            return (n)
        if (m != 1):
            return (n * power_of_num(n, m - 1))

base = int(input("Enter base: "))
exp = int(input("Enter exponent value: "))
print('Result of ',base,'^',exp ,'is:', power_of_num(base, exp))





