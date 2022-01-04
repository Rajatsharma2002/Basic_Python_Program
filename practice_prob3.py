a=int(input("Enter size of list : "))
lis=[]
for i in range(a):
    l = input("Enter the list of food calories : ")
    lis.append(l)

x=lis.copy()
y=lis.copy()

lis.reverse()
print(f"reverse of list using inbuilt method {lis}")


a=x[::-1]
print(f"reverse of a string using slicing {a}")

def swap(a,b):
    temp=a
    a=b
    b=temp
    return a

z=[]
for i in range(len(lis)):
    rev=swap(y[i],y[len(lis)-i-1])
    z.append(rev)
print(f"reverse of list using swapping {z}")

if lis==a==z:
    print("ALL three methods give same result")



