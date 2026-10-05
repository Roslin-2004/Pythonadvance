# 54321
# 5432
# 543
# 54
# 5
# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()

#write a program to find a max number in a list
# l=[23,78,45,70,12,56]
# maxi=l[0]
# for i in l:
#     if i>maxi:
#         maxi=i
#     else:
#         maxi=maxi
# print(maxi)


#nth term fibbino
n=int(input("Enter the value of n: "))
a=0
b=1
for i in range(n-1):
    a,b=b,a+b
print(b)

#or
n=int(input("Enter the value of n: "))
a=0
b=1
if n==1:
    print(a)
elif n==2:
    print(b)
else:
   for i in range(3, n + 1):
       a, b = b, a + b
   print(b)