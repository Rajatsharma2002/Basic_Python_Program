def getdate():
    import datetime
    return datetime.datetime.now()

def func():
    info=int(input("enter the option you wnat to choose :\n1.LOCK\n2.RETRIEVE\n"))
    if(info==1):
        a=int(input("choose the following by entering there number \n1.Harry\n2.Rohan\n3.Rajat\n"))
        if(a==1):
            num=int(input("which do you want to lock \n1.Food\n2.Exercise\n"))
            if(num==1):
                f=open("Harry_food.txt","a")
                food=input("enter things harry has eaten :\n")
                dt= str(getdate())
                f.write(dt+" : ")
                f.write(food+"\n")
                f.close()
            else:
                f = open("Harry_exercise.txt", "a")
                exercise = input("enter the workoutplan of harry :\n")
                dt = str(getdate())
                f.write(dt)
                f.write(exercise+"\n")
                f.close()
        elif(a==2):
            num = int(input("which do you want to lock \n1.Food\n2.Exercise\n"))
            if (num == 1):
                f = open("Rohan_food.txt", "a")
                food = input("enter things Rajat has eaten :\n")
                dt = str(getdate())
                f.write(dt)
                f.write(food+"\n")
                f.close()
            else:
                f = open("Rohan_exercise.txt", "a")
                exercise = input("enter the workoutplan of Rohan :\n")
                dt = str(getdate())
                f.write(dt)
                f.write( exercise+"\n")
                f.close()
        elif(a==3):
            num = int(input("which do you want to lock \n1.Food\n2.Exercise\n"))
            if (num == 1):
                f = open("Rajat_food.txt", "a")
                food = input("enter things Rajat has eaten :\n")
                dt = str(getdate())
                f.write(dt)
                f.write(food+"\n")
                f.close()
            elif(a==3):
                f = open("Rajat_exercise.txt", "a")
                exercise = input("enter the workoutplan of Rajat :\n")
                dt = str(getdate())
                f.write(dt+" : ")
                f.write(exercise+"\n")
                f.close()
        else:
            print("ERROR! enter a valid option!")
    elif(info==2):
        a = int(input("choose the following by entering there number \n1.Harry\n2.Rohan\n3.Rajat\n"))
        if (a == 1):
            num = int(input("which data do you want to retrieve \n1.Food\n2.Exercise\n"))
            if (num == 1):
                f = open("Harry_food.txt", "rt")
                content=f.read()
                print(content)
                f.close()
            else:
                f = open("Harry_exercise.txt", "rt")
                content = f.read()
                print(content)
                f.close()
        elif (a == 2):
            num = int(input("which data do you want to retrieve \n1.Food\n2.Exercise\n"))
            if (num == 1):
                f = open("Rohan_food.txt", "rt")
                content=f.read()
                print(content)
                f.close()
            else:
                f = open("Rohan_exercise.txt", "rt")
                content = f.read()
                print(content)
                f.close()

        elif (a == 3):
            num = int(input("which data do you want to retrieve \n1.Food\n2.Exercise\n"))
            if (num == 1):
                f = open("Rajat_food.txt", "rt")
                content=f.read()
                print(content)
                f.close()
            else:
                f = open("Rajat_exercise.txt", "rt")
                content = f.read()
                print(content)
                f.close()
        else:
            print("ERROR! enter a valid option!")
    else:
        print("ERROR! enter a valid option!")
func()