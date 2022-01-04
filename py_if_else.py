age=int(input("enter the age : "))

if age in range(4,101):
    if(age>18):
        print("eligible to drive")
    elif(age==18):
        print("not decided")
    else:
        print("not eligible to drive ! underage")
else:
    print("enter valid age")
