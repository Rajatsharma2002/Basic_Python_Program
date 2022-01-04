a=int(input("Enter number of items you want to add in list : "))
input_str=input("Enter the list of items : ")
l=input_str.split()
c=int(input("What type of comprehension you want to make \n1.List comprehension\n2.Dict comprehension\n3.set comprehension\n4.Generator\n"))
if c==1:
        list=[i for i in l]
        print(list)
elif c==2:
        dict={i:f"item {i}" for i in l}
        print(dict)
elif c==3:
        set={i for i in l}
        print(set)
elif c==4:
    gen=(i for i in l)
    print(type(gen))
    for i in gen:
        print(i)

