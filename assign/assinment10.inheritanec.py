''' Q.1- Create a class Animal as a base class and define method animal_attribute.
Create another class Tiger which is inheriting Animal and access the base class method.
class animal:'''
class Animal:   
    def animal_atr(self,legs,ears):  
      print("ANmal attribute")
      self.legs = legs
      self.ears = ears
class tiger(Animal):
    def __init__(self):
        print("The animal is tiger")
obj = tiger()
# Q.2- What will be the output of following code.

#print("A B\nA B")


'''Q.3- Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details.
Create another class Mission which extends the class Cop. Define method add_mission _details.
select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.'''

class Cop():
    def add(self):
        self.name = input(("enter name:"))
        self.age = int(input("enter the age:"))
        self.work = int(input("enter the work experience in years:"))
        self.designation = input("enter the designation:")
    def display(self):
        print("name of this cop: %s\nage of this cop: %d\nwork_experience: %d\ndesignation: %s" % (self.name, self.age, self.work, self.designation))
    def update(self):
        self.name = input(("enter new name:"))
        self.age = int(input("enter the new age:"))
        self.work = int(input("enter the new work experience in years:"))
        self.designation = input("enter the new designation:")
class Mission(Cop):
    m_name = ''
    m_duration = ''
    m_place = ''
    def mission_details(self):
        m_name = input("Enter the mission name:")
        m_duration = int(input("Enter mission duration in months: "))
        m_place = input("Enter country for mission: ")
obj = Mission()
print("Add data")
obj.add()
print("\nshowing added data......")
obj.display()
print("\ntime to update data.....")
obj.update()
print("\nupdated data below")
obj.display()


''' Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area.
Create class rectangle and square which inherits shape and access the method Area.'''
class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return (self.length * self.breadth)
class rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
class square(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
a = rectangle(10, 9)
print("area of rectangle:", a.area())
b = square(10, 10)
print("area of square:", b.area())
