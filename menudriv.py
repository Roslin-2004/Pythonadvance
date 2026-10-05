def file_read():
    file_name=input("enter file name:")
    f=open(file_name,"r")
    con=f.read()
    print(con)
def file_write():
    file_name=input("enter file name:")
    f = open(file_name, "w")
    con=input("enter content:")
    f.write(con)
    print("printed sucessfully.....")
def file_append():
    file_name=input("enter file name:")
    f = open(file_name, "a")
    con=input("enter content:")
    f.write(con)
    print("print sucessfully....")
def file_search():
    file_name=input("Enter file name: ")
    word=input("Enter word to search: ")
    f=open(file_name, "r")
    con=f.read()
    f.close()
    if word in con:
        print("Word found")
    else:
        print("Word not found")
def file_remove():
    file_name=input("enter file name:")
    import os
    os.remove(file_name)
    print("REMOVED")

while(1):
    print("menudrive--file operation")
    print("1.file read")
    print("2.file write")
    print("3.file append")
    print("4.file search")
    print("5.file remove")
    print("6.exit")

    ch=int(input("enter choice"))
    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_remove()
    elif ch==6:
        exit()