#1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
#
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.


# class Circle:
#     def __init__(self):
#         self.radius= radius
#     def getarea(self):
#         self.are=3.14*(self.radius**2)
#         print("Area:",self.are)
#     def getperi(self):
#         self.peri=(2*3.14)*self.radius
#         print("Perimeter:",self.peri)
# c=Circle()
# c.getarea()
# c.getperi()


# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.

#
# class Account:
#     def __init__(self):
#         self.acctnumber = input("Enter Account Number: ")
#         self.acctname = input("Enter Account Name: ")
#         self.balance = float(input("Enter Balance: "))
#     def withdraw(self):
#         amount = float(input("Enter Amount to Withdraw: "))
#         self.balance = self.balance-amount
#     def deposit(self):
#         amount = float(input("Enter Amount to Deposit: "))
#         self.balance = self.balance+amount
#     def showbalance(self):
#         print("Current Balance =",self.balance)
# a = Account()
# a.withdraw()
# a.showbalance()
# a.deposit()
# a.showbalance()
# b= Account()
# b.withdraw()
# b.showbalance()
# b.deposit()
# b.showbalance()
#
# l=[a,b]
# num=int(input("accno"))
# for i in l:
#     i

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        self.are = 3.14 * (self.radius ** 2)
        print("Area:", self.are)

    def getperi(self):
        self.peri = 2 * 3.14 * self.radius
        print("Perimeter:", self.peri)


c = Circle(5)
c.getarea()
c.getperi()