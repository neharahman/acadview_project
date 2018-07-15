#1- Take an input year from user and decide whether it is a leap year or not.

a = int(input("Enter year: "))
if (a%4 == 0 and a%100 != 0 or a%400 == 0):
    print(" The year is leap year",a)
else:
    print(" Enterded Year is not a leap year",a)




#2- Take length and breadth input from user and check whether the dimensions are of square or rectangle. 

l = int(input("\n\nEnter length of figure to check whether the dimensions are of square or rectangle: "))
b = int(input("Enter breadth of figure: "))

if(l == b):
    print("This is a square")
else:
    print("This is a rectangle")


#Take the input age of 3 people and determine oldest and youngest among them.

a = int(input("Enter age of first person: "))
b = int(input("Enter age of 2nd person: "))
c = int(input("Enter age of 3rd person: "))
li = [a, b, c]
print("the oldest among these is person   ",max(li))
print("the youngest among these is person ", min(li))


'''4- Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored,
which is stored in the integer variable points(your input). points can only take on positive integer values up to 200. 
If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name.
If there's no prize, the message should state "Sorry! No prize this time.'''


prize = ['candy','corn flakes','t-shirt','bag']
points = int(input("Enetr points: "))
if(points>=1 and points<=200):
    if( points in range(1,50)):
        print("Congratulations! You have won a %s !" %(prize[0]))
    elif(points in range(50,150)):
        print("Congratulations! You have won a %s !" %(prize[1]))
    elif(points  in range(150,180)):
        print("Congratulations! You have won a %s !" %(prize[2]))
    elif (points in range(180,201)):
        print("Congratulations! You have won a %s !" %(prize[3]))
    else:
          print("Sorry! No prize this time")
else:
         print("Wrong Input")



'''5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity Suppose, one unit will cost 100.
Judge and print total cost for user. '''

a =int(input("enter the number of items: "))
b = a*100
if b>1000:
    q=b-0.1*b
    print("Total cost:",q)
else:
    print("Total cost:",b)

