# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name,self.age)
# p=Person("anju",23)
# p.display()
#
# class Person:
#     def __init__(self):
#         self.name =input("name:")
#         self.age =input("age:")
#
#     def show(self):
#         print(self.name, self.age)
#
#
# p = Person()
# p.show()
# class Employee:
#     def __init__(self):
#         self.empid= input("id:")
#         self.name =input("name:")
#         self.age =input("age:")
#         self.salary= input("salary:")
#         self.designation= input("designation:")
#         self.place= input("place:")
#
#     def getsalary(self):
#         return self.salary
#     def display(self):
#         print(self.empid)
#
#
# e =Employee()
# print(e.getsalary())
# e.display()
#
# class Student:
#     def __init__(self):
#         self.rollno= input("id:")
#         self.name =input("name:")
#         self.clas=input("class:")
#         self.mark1= int(input(("mark1:")))
#         self.mark2= int(input(("mark2:")))
#         self.mark3= int(input(("mark3:")))
#
#     def calculate(self):
#         self.total=self.mark1+self.mark2+self.mark3
#         self.ave=(self.total/3)
#         print("total of",self.name,self.total,self.ave)
#     def showdetails(self):
#         print(self.name,self.rollno,self.clas)
#
#
# s=Student()
# s.calculate()
# s.showdetails()
from datetime import datetime


#define a class book with the following description:
#datamembers
#bookname,bookid,authorid,authorname,price,booktitle
#membermethods
#getauthorid (),getauthorname(),getbooktitile(),getprice(),setauthorname(),setbooktitile(),setprice(),


#
# class Book:
#     def __init__(self):
#         self.bookid = input("Enter Book ID: ")
#         self.bookname = input("Enter Book Name: ")
#         self.authorid = input("Enter Author ID: ")
#         self.authorname = input("Enter Author Name: ")
#         self.booktitle = input("Enter Book Title: ")
#         self.price = float(input("Enter Price: "))
#     def getauthorid(self):
#         print("Author ID:", self.authorid)
#     def getauthorname(self):
#         print("Author Name:", self.authorname)
#     def getbooktitle(self):
#         print("Book Title:", self.booktitle)
#     def getprice(self):
#         print("Price:", self.price)
#     def setauthorname(self):
#         self.authorname = input("Enter New Author Name: ")
#         self.getauthorname()
#     def setbooktitle(self):
#         self.booktitle = input("Enter New Book Title: ")
#         self.getbooktitle()
#     def setprice(self):
#         self.price = float(input("Enter New Price: "))
#         self.getprice()
# b=Book()
# b.setauthorname()
# b.setbooktitle()
# b.setprice()
# print("\nAfter Updating")
# b.getauthorname()
# b.getbooktitle()
# b.getprice()






#write a menu drive python program for a banking
# craete account
#withdraw money
#deposit money
#display balance
#exit
#store account details in alist andvsearch account using account number
# display "account not fount " if the account does not exit
# class Account:
#     def __init__(self):
#         self.acctnumber = input("Enter Account Number: ")
#         self.acctname = input("Enter Account Name: ")
#         self.balance = float(input("Enter Balance: "))
#     def withdraw(self):
#         amount = float(input("Enter Amount to Withdraw: "))
#         self.balance = self.balance-amount
#         self.showbalance()
#     def deposit(self):
#         amount = float(input("Enter Amount to Deposit: "))
#         self.balance = self.balance+amount
#         self.showbalance()
#     def showbalance(self):
#         print("Current Balance =",self.balance)
# l=[]
# while(1):
#     print("menudrive--")
#     print("1.create account")
#     print("2.withdraw money")
#     print("3.deposit money")
#     print("4.display balance")
#     print("5.exit")
#     ch=int(input("enter choice:"))
#
#     if ch==1:
#         a=Account()
#         l.append(a)
#     elif ch==2:
#         num=input("acc no:")
#         for i in l:
#             if i.acctnumber==num:
#                 i.withdraw()
#                 break
#         else:
#             print("acc not found")
#
#     elif ch==3:
#         num = input("acc no:")
#         for i in l:
#             if i.acctnumber == num:
#                 i.deposit()
#                 break
#         else:
#             print("acc not found")
#
#     elif ch==4:
#         num = input("acc no:")
#         for i in l:
#             if i.acctnumber == num:
#                 i.showbalance()
#                 break
#         else:
#             print("acc not found")
#
#
#     elif ch==5:
#         exit()


#=======single level==============

# class Person:
#     def __init__(self):
#         self.name=input("enter a name")
#         self.age=int(input("age:"))
#     def showdetails(self):
#         print("name:",self.name,"age",self.age,)
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.roll=int(input("Rollno:"))
#     def studentdetails(self):
#         super().showdetails()
#         print(self.age)
# s=Student()
# s.studentdetails()
#
#
# class Company:
#     def __init__(self):
#         self.name=input("enter a companyname")
#     def showdetails(self):
#         print("name:",self.name,)
# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.id =input("id")
#         self.des=input("designation:")
#         self.salary = int(input("salary:"))
#     def getsalary(self):
#         print("salary:",self.salary)
#     def employeedetails(self):
#         super().showdetails()
#         print("emid",self.id,"designation",self.des,"salary",self.salary)
# c=Employee()
# c.employeedetails()
# c.getsalary()
#
#
# class Hospital:
#     def __init__(self):
#         self.Hname=input("Hname:")
#         self.loc=input("Location:")
#     def showdetails(self):
#         print("Hospital name:",self.Hname,"Location:",self.loc)
# class Department:
#     def __init__(self):
#         self.Dname=input("Dname:")
#         self.doc=input("Doc name:")
#     def showdepatdetails(self):
#         print("Department name:",self.Dname,"Doc name:",self.doc)
# class Patient(Hospital,Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#         self.pname =input("pname:")
#         self.age=input("Age:")
#         self.id = int(input("id:"))
#         self.gender =input("gender:")
#         self.place= input("place:")
#         self.admndate =input("admission date:")
#     def setdischarge(self):
#         self.discharge=input("Discharge date:")
#     def fullsummary(self):
#         print("PATIENT DETAILS")
#         print("---------------")
#         print("Name:",self.pname)
#         print("Age:",self.age)
#         print("ID:",self.id)
#         print("Gender:",self.gender)
#         print("Place:",self.place)
#         print("Admission date:",self.admndate)
#         print("Discharge Date:",self.discharge)
#         if self.discharge=="":
#             print("not discharged")
#         else:
#             print("self.discharge",self.discharge)
#     def dischargedetail(self):
#         print("PATIENT DISCHARGE DETAILS")
#         print("-------------------------")
#         print("Name:", self.pname)
#         print("Department name:", self.Dname)
#         print("Doc name:", self.doc)
#         print("ID:", self.id)
#         print("Place:", self.place)
#         print("Admission date:", self.admndate)
#         print("Discharge Date:", self.discharge)
#
#
# p=Patient()
# p.fullsummary()
# p.setdischarge()
# p.dischargedetail()



# try:
#     n1=int(input("num"))
#     n2=int(input("num"))
#     r=n1/n2

# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
# import math
# try:
#     n=int(input("Enter a number: "))
#     print("Factorial =",math.factorial(n))
# except ValueError:
#     print("ValueError")

# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# try:
#     while(1):
#         a=int(input("Enter First Number: "))
#         b=int(input("Enter Second Number: "))
#         print("1.Addition")
#         print("2.Subtraction")
#         print("3.Multiplication")
#         print("4.Division")
#         ch = int(input("Enter Choice: "))
#         if ch==1:
#             print("Answer =", a+b)
#         elif ch==2:
#             print("Answer =", a-b)
#         elif ch==3:
#             print("Answer =", a*b)
#         elif ch==4:
#             print("Answer =", a/b)
#         else:
#             print("Invalid Choice")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ValueError:
#     print("ValueError")
# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
# try:
#     f=open("k.txt", "r")
#     print("yes file here",f.read())
#     f.close()
# except FileNotFoundError:
#     print("FileNotFoundError")



