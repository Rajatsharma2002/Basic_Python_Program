a=24
guess=9
while(guess!=0):
    num=int(input("\nenter the number to guess : "))
    guess=guess-1
    if(num>a):
        print("\nnumber entered is greater")
        print("guesses left = ",guess)
    elif(num==a):
        print("\nyou guessed the correct number")
        print("guesses left after getting the correct guess = ",guess)
        break
    else:
        print("\nnumber entered is lesser")
        print("guesses left = ", guess)

if(guess==0):
    print("you reached the limit of guess")
    print("game over")