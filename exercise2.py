a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
c=input("enter the operation(multiply,divide,add,subtract) to perform :")
if(a==45 and b==3 and c=="multiply"):
    print(a,"*",b,"= 555")

elif(a==56 and b==9 and c=="add"):
    print(a,"+",b,"= 77")

elif(a==56 and b==6 and c=="divide"):
    print(a,"/",b,"= 4")

elif (c == "divide"):
    print(a / b)
elif (c == "multiply"):
    print(a * b)
elif (c == "add"):
    print(a + b)
else:
    print(a - b)