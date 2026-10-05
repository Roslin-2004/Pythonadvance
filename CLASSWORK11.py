#.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()
# class Movie:
#     def __init__(self):
#         self.name=input("Enter movie name:")
#         self.year=input("Enter year:")
#         self.language=input("Enter language:")
#         self.director=input("Enter director name:")
#         self.rating=int(input("Enter rating:"))
#     def display_details(self):
#         print("Movie name:",self.name)
#         print("Year:",self.year)
#         print("Language:",self.language)
#         print("Director:",self.director)
#         print("Rating:",self.rating)
#     def setupdate_rating(self):
#         self.update_rating=input("Enter rating:")
# a=Movie()
# a.display_details()
# a.setupdate_rating()
# a.display_details()


# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.
# class Vehicle:
#     def __init__(self):
#         self.brand=input("Enter brand name:")
#         self.model=input("Enter model name:")
#         self.color=input("Enter the color:")
#         self.year=int(input("Enter year:"))
#     def display(self):
#         print("Brand:",self.brand)
#         print("Model:",self.model)
#         print("Colour:",self.color)
#         print("Year:",self.year)
# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.mileage=input("Enter mileage:")
#     def display(self):
#         super().display()
#         print("Mileage:",self.mileage)
# class Bike(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.cc=input("Enter cc:")
#     def display(self):
#         super().display()
#         print("CC:",self.cc)
#
# c=Car()
# c.display()
# b=Bike()
# b.display()


#3. Create an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.
# from abc import ABC,abstractmethod
# class Employee(ABC):
#
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
# class FullTimeEmployee(Employee):
#     def __init__(self):
#         self.salary=int(input("Enter monthly salary:"))
#     def calculate_salary(self):
#         print("Salary:",self.salary)
#
# class PartTimeEmployee(Employee):
#     def __init__(self):
#         self.hourly_salary=int(input("Enter hourly salary:"))
#         self.hours_worked=int(input("Enter hours worked:"))
#     def calculate_salary(self):
#         print("Salary:",self.hourly_salary * self.hours_worked)
#
# f=FullTimeEmployee()
# f.calculate_salary()
# p=PartTimeEmployee()
# p.calculate_salary()

#4. create an abstract class Shape with abstract methods get_area() and get_perimeter()
# create two subclasses
#  -Rectangle
#  -Square
#
#  -Each class should calculate area() and perimeter() differently.
# from abc import ABC,abstractmethod
# class Shape(ABC):
#
#     @abstractmethod
#     def getarea(self):
#         pass
#
#     @abstractmethod
#     def getperimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self):
#         self.length=int(input("Enter the length:"))
#         self.breadth=int(input("Enter the breadth:"))
#     def getarea(self):
#         print("Area:",self.length * self.breadth)
#
#     def getperimeter(self):
#         print("Perimeter:",2 * (self.length + self.breadth))
#
#
# r=Rectangle()
# r.getarea()
# r.getperimeter()
#
# class Square(Shape):
#     def __init__(self):
#         self.side=int(input("Enter side:"))
#     def getarea(self):
#         print("Area:",self.side * self.side)
#
#     def getperimeter(self):
#         print("Perimeter:",4 * (self.side))
#
# s=Square()
# s.getarea()
# s.getperimeter()

# 5.Create a Python program using Object-Oriented Programming (OOP) that includes the following:
# • Class: Course
# Attributes:
# course_name
# instructor
# duration
# Methods:
# show_course() → to display course details
# • Subclass: Student (inherits from Course)
# Additional attributes:
# name
# roll_no
# marks
# Methods:
# show_student() → to display student details along with course details
# get_result() → return "Pass" if marks ≥ 50, otherwise "Fail"
# Create at least one object of the Student class
# Display all details and result

# class Course():
#     def __init__(self):
#         self.course_name=input("Enter course name:")
#         self.instructor=input("Enter instructor name:")
#         self.duration=input("Enter course duration:")
#     def show_course(self):
#         print("Course name:",self.course_name)
#         print("Instructor:",self.instructor)
#         print("Duration:",self.duration)
#
# class Student(Course):
#     def __init__(self):
#         super().__init__()
#         self.name=input("Enter student name:")
#         self.rollno=input("Enter rollno:")
#         self.marks=int(input("Enter marks:"))
#     def show_student(self):
#         print("Student name:",self.name)
#         print("Rollno:",self.rollno)
#         print("Marks:",self.marks)
#         self.show_course()
#     def get_result(self):
#         if self.marks>=50:
#             print("Pass")
#         else:
#             print("Fail")
#
# s=Student()
# s.show_student()
# s.get_result()


# 6.Create a Python program using Object-Oriented Programming (OOP) that includes a class called Employee with attributes
# such as id, name, age, designation, experience (in years), and salary.
# The class should include methods to display employee details and update the designation.
# It should also include a method to check promotion eligibility where an employee is eligible for promotion if experience is 5 years or more and age is above 30;
# otherwise, the employee is not eligible.
# Create at least one object of the Employee class, assign values directly, and display all the details along with the promotion eligibility result.
# class Employee:
#     def __init__(self):
#         self.id=input("Enter Employee id:")
#         self.name=input("Enter Employee name:")
#         self.age=int(input("Enter age:"))
#         self.designation=input("Enter designation:")
#         self.experience=int(input("Enter experience in years:"))
#         self.salary=int(input("Enter salary:"))
#     def display_details(self):
#         print("Employee id:",self.id)
#         print("Employee name:",self.name)
#         print("Employee age:",self.age)
#         print("Deaignation:",self.designation)
#         print("Experience:",self.experience)
#         print("Salary:",self.salary)
#     def update_designation(self):
#         self.new_designation=input("Enter updated designation:")
#         print("New designation:",self.new_designation)
#     def check_promotion(self):
#         if(self.experience>=5 and self.age>30):
#             print("Eligible for promotion")
#         else:
#             print("Not eligible for promotion")
#
# e=Employee()
# e.display_details()
# e.update_designation()
# e.check_promotion()
