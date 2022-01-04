import random
n=int(input("Enter the size of list : "))
l=[]
print(f"Enter the {n} names : ")
for i in range(n):
    name=input()
    l.append(name)
print(l)

fname=[i.split(" ")[0] for i in l ]
lname=[i.split(" ")[1] for i in l ]
# print(fname)
# print(lname)

print("\nJumbled names : ")
for i in range(n):
    list=[]
    # a = fname[i] + " " + lname[random.randint(0,n-1)]
    a=fname[i] +" "+ lname[n-i-1]
    list.append(a)
    print(list)

