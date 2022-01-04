import random
computer_win=0
user_win=0
draw=0
times=0
l=["snake","water","gun"]
choice=random.choice(l)

try :
    while(times<10):
        l = ["snake", "water", "gun"]
        choice = random.choice(l)
        a = input("enter the option you want to choose : \n1.snake\n2.water\n3.gun\n")
        if(choice=="snake" and a=="snake"):
            print("DRAW")
            #print(f"computer choose {choice}")
            draw+=1
            times+=1
        elif(choice=="snake" and a=="gun"):
            print("YOU WIN")
            #print(f"computer choose {choice}")
            user_win+=1
            times += 1
        elif (choice == "snake" and a == "water"):
            print("COMPUTER WIN")
            #print(f"computer choose {choice}")
            computer_win += 1
            times += 1
        elif (choice == "water" and a == "snake"):
            print("YOU WIN")
            #print(f"computer choose {choice}")
            user_win += 1
            times += 1
        elif (choice == "water" and a == "gun"):
            print("COMPUTER WIN")
            #print(f"computer choose {choice}")
            computer_win += 1
            times += 1
        elif (choice == "water" and a == "water"):
            print("DRAW")
            #print(f"computer choose {choice}")
            draw+=1
            times += 1
        elif (choice == "gun" and a == "gun"):
            print("DRAW")
            #print(f"computer choose {choice}")
            draw += 1
            times += 1
        elif (choice == "gun" and a == "snake"):
            print("COMPUTER WIN")
            #print(f"computer choose {choice}")
            computer_win += 1
            times += 1
        elif (choice == "gun" and a == "water"):
            print("YOU WIN")
            #print(f"computer choose {choice}")
            user_win += 1
            times += 1
        print(f"computer choose : {choice}\n")

except Exception as e:
    print(e)
    print("Invalid choice!")

print(f"\nuser won {user_win} times")
print(f"computer won {computer_win} times")
print(f"Draws : {draw}")