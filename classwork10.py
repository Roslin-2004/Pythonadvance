

# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.
#
# class Student:
#     def __init__(self):
#         self.name = input("name: ")
#         self.rollno =input("rollno: ")
#         self.mark = int(input("mark: "))
#     def update(self):
#         self.mark=int(input("update mark: "))
#
#     def display(self):
#         print("rollno:",self.rollno)
#         print("Name:",self.name)
#         print("mark:",self.mark)
# l=[]
# while(1):
#     print("menudrive--")
#     print("1.Student")
#     print("2.Update Marks")
#     print("3.Display All Student Details")
#     print("4.Search Student by Roll Number")
#     print("5.Delete Student")
#     print("6.exit")
#     ch=int(input("enter choice:"))
#
#     if ch==1:
#         s=Student()
#         l.append(s)
#     elif ch==2:
#         roll=input("rollno:")
#         for i in l:
#             if i.rollno==roll:
#                 i.update()
#                 break
#         else:
#             print("student not found")
#
#     elif ch==3:
#         for i in l:
#             i.display()
#
#
#     elif ch==4:
#         roll=input("Enter Roll No: ")
#         for i in l:
#             if i.rollno == roll:
#                 i.display()
#                 break
#         else:
#             print("Student not found")
#     elif ch==5:
#         roll=input("Enter Roll No: ")
#         for i in l:
#             if i.rollno ==roll:
#                 l.remove(i)
#                 print("Student deleted")
#                 break
#         else:
#             print("Student not found")
#
#     elif ch==5:
#         exit()
