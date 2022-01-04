list=["creata","Audi","Ferrari","BMW","Innova","aston martin","mercedes","Maclaren"]

print("using simple formula : ")
try:
    i=0
    choice=int(input("Which number car you want to select : \n1.odd\n2.even\n"))
    if(choice==1):
            for item in list:
                if i%2!= 0:
                    print(f"I want to buy {item}")
                i+=1
    elif(choice==2):
            for item in list:
                if i%2== 0:
                    print(f"I want to buy {item}")
                i+=1

except Exception as e:
    print(e)
    print("INVALID input!")

print("\nusing enumerate function : ")
try:
    i=0
    choice=int(input("Which number car you want to select : \n1.odd\n2.even\n"))
    if(choice==1):
            for i,item in enumerate(list):
            #for i, item in enumerate(list, 1):    a starting index can be given in enumerate function
                if i%2!= 0:
                    print(f"I want to buy {item}")
    elif(choice==2):
        for i, item in enumerate(list):
            if i % 2 == 0:
                print(f"I want to buy {item}")
except Exception as e:
    print(e)
    print("INVALID input!")
