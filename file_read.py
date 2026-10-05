# f=open("k.txt","r")
# # con=f.read()
# con=f.readlines()
# print(con)
# f.close()

# write a pro to read  a text file and display the no.of lines in a file
# f=open("k.txt","r")
# # con=f.read()
# con=len(f.readlines())
# print(con)
# f.close()
# display  the number of words in a file
# f=open("k.txt","r")
# con=f.read()
# s=con.split()
# print(len(s))
# f.close()
#update the second line in a file
# f=open("k.txt","r")
# con=f.readlines()
# con[1]="c++\n"
# f=open("k.txt","w")
# f.writelines(con)
# f.close()

#write a program to display the last 5 lines in a file
# f=open("k.txt","r")
# con=f.readlines()
# s=con[-5:]
# print(s)
# #program to search a particular word in a file
# a=input("enter a word")
# f=open("k.txt","r")
# con=f.read()
# if a in con:
#     print("word found")
# else:
#     print("not found")

#find the number of letters,digits,and spaces in a file
# f=open("k.txt","r")
# con=f.read()
# l=0
# s=0
# d=0
# for i in con:
#     if i.isalpha():
#         l=l+1
#     elif i.isdigit():
#         d=d+1
#     elif i.isspace():
#         s=s+1
# print("letter",l)
# print("digit",d)
# print("space",s)



#reverse the lines in a file
# f=open("k.txt","r")
# con=f.readlines()
# s=con[::-1]
# f=open("k.txt","w")
# con=f.writelines(s)
# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed the exam.
# f=open("totalstudents.txt","w")
# total=['kiran\n','ajal\n','roslin\n','anju\n','raman\n','mongly\n']
# f.writelines(total)
# f.close()
# f=open("passedstudents.txt","w")
# passed=['kiran\n','ajal\n','roslin\n']
# f.writelines(passed)
# f.close()
# f=open("failedstudents.txt","w")
# for i in total:
#     if i not in passed:
#         f.write(i)
# f.close()



# or

# f1=open("totalstudents.txt","r")
# l1=f1.readlines()
#
# f2=open("passedstudents.txt","r")
# l2=f2.readlines()
#
# f3=open("failedstudents.txt","w")
# for i in l1:
#     if i not in l2:
#         f3.write(i)

# Write a Python program to:
# Read the names from both files.
# Find the students who did not pass.
# Write their names to a new file named failed_students.txt, one name per line.






# Two files, swiggy.txt and zomato.txt, contain the names of food items ordered from each platform.
# Write a Python program to read words from swiggy.txt and zomato.txt, combine them, and count how many times each word appears. Store the result in a dictionary and print it


#
# f=open("swiggy.txt","w")
# swiggy = ["burger", "chickenpop", "pizza", "donut", "burger"]
# f.writelines(swiggy)
# f.close()
# f=open("zomato.txt","w")
# zomato = ["burger", "pizza", "donut", "maggie"]
# f.writelines(zomato)
# f.close()
#items= swiggy+zomato
# d = {}
# for i in items:
#     count=0
#     for j in items:
#         if i==j:
#             count=count+1
#     d[i]=count
#
# print(d)

# or
# f1=open("swiggy.txt","r")
# s1=f1.read().split()
#
# f2=open("zomato.txt","r")
# l2=f2.read().split()
#
#d={}
# for i in item:
#     d[i]=item.count(i)
# print(d)


# A file marks.txt contains the names and marks of students as shown below:
# Anu 80
# Rahul 65
# Meera 90
# Arun 70
#
#
# Write a Python program to read the file and write the names of students who scored more than 75 marks into a file named names.txt

f=open("marks.txt","w")
total=["Anu 80\n", "Rahul 65", "Meera 90", "Arun 70",]
f.writelines(total)
f.close()

g=open("names.txt","w")
for i in total:
    s=i.split()
    name = s[0]
    mark = int(s[1])
    if mark > 75:
        g.write(name+"\n")
g.close()







# f=open("p.txt","r")
# s=f.read()
# f1=open("kt.txt","a+")
# f1.write(s)
#
# f1=open("kt.txt","a+")
# f1.write("py")
# s=f1.read()
# print(s)

# f1=open("kt.txt","a+")
# print("current pos:",f1.tell())
# f1.write("python")
# print("current pos:",f1.tell())
# f1.seek(0)
# print("current pos:",f1.tell())
# s=f1.read()
# print("content",s)
# print(s)












