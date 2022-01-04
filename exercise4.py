a=int(input("enter the number of rows : "))
b=int(input("enter a boolean value(1,0) : "))
c=bool(b)

# if c==True:
#     for i in range(1,a+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif c==False:
#     for i in range(a,0,-1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()

if c==True:
    for i in range(1,a+1):
            print("*"*i)
elif c==False:
    for i in range(a,0,-1):
            print("*"*i)