'''Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.'''
import math
class Circle():
    def __init__(self,radius):
        self.radius = radius

    def getArea(self):
        return (math.pi * self.radius**2)

    def getCircumference(self):
        return (2 * math.pi * self.radius)


rad = float(input("Enter radius of circle: "))
x = Circle(rad)
y = x.getArea()
print("Area of circle is: ", y)
n = x.getCircumference()
print("Perimeter of circle is: ", n)



''' Create a Student class and initialize it with name and roll number. Make methods to :Display - It should display all informations of the student.'''
class Student():
    name = ''
    roll = 0
    def __init__(self):
        name = input("Enter name of student: ")
        self.name = name
        roll = int(input("Enter roll number of student:"))
        self.roll= roll
    def display(self):
        print("name of student is: ",self.name)
        print("Roll no: ",self.roll)
        

obj = Student()
obj.display()



'''.3- Create a Temprature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.'''




class Temprature():
  def  convertFahrenhiet(self,celsius):
      return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
      return (farenhiet-32)*(5/9)


a = Temprature()
celsius = float((input("Enter temperature in celcius: ")))
b = a.convertFahrenhiet(celsius)
print("The temperature in farenhiet is: ",b, " degree farenhiet")


c = float((input("Enter temperature in farenhiet: ")))
d = a.convertCelsius(c)
print("The temperature in celsius is: ",d, " degree celsius")




'''Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
Make methods to 
1. Display-Display the details.
2. Update- Update the movie details.'''
class MovieDetails():
    def __init__(self,movie_name,artist_name,release_year,ratings):
        self.movie_name = movie_name
        self.artist_name = artist_name
        self.release_year = release_year
        self.ratings = ratings
    def display(self):
        print("Name of movie: ",self.movie_name)
        print("Name of artist of movie: ",self.artist_name)
        print("Name of movie: ",self.release_year)
        print("Name of movie: ",self.ratings)
    def update_details(self):
        self.movie_name = input("Enter new movie name: ")
        self. artist_name = input("Enter new artist's name: ")
        self.release_year = int(input("Enter release year: "))
        self.ratings = int(input("Enter ratings out of 10: "))
movie = input("Enter movie name: ")
artist = input("Enter artist's name: ")
year = int(input("Enter release year: "))
rating = int(input("Enter ratings out of 10: "))
obj = MovieDetails(movie,artist,year,rating)
obj.display()
obj.update_details()
obj.display()


'''Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
1. Display expenditure and savings 
2. Calculate total salary
3. Display salary
'''

class Expenditure():
    def __init__(self,expenditure,savings):
        self.expenditure = expenditure
        self.savings = savings

    def display(self):
        print("Expenditure = ", self.expenditure)
        print("Savings = ",self.savings)

    def total_salary(self):
        return (self.expenditure + self.savings)

    def display_salary(self):
        self.s = self.total_salary()
        print("Total salary : ", self.s)

x = int(input("enter total expenditure: "))
y = int(input("Enter total savings: "))

obj = Expenditure(x,y)
obj.display()
obj.display_salary()



