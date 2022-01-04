import random
def game(a,b,c):
    trails1=0
    bl = True
    while bl:
        num = int(input(f"Guess the number between {a} and {b} : "))
        if num < a or num > b:
            print(f"Strictly Enter the number between the range {a} and {b}")
        elif num > c:
            print("Wrong guess! please guess a smaller number\n")
            trails1 += 1
        elif num < c:
            print("Wrong guess! please guess a greater number\n")
            trails1 += 1
        elif num == c:
            print("Correct guess")
            trails1 += 1
            print((f"Player 1 guessed in {trails1} trails\n"))
            return trails1
            bl = False

if __name__ == '__main__':
    a = int(input("Enter the lower bound of range : "))
    b = int(input("Enter the upper bound of range : "))
    c = random.randint(a, b)

    print(f"\nPlayer 1 guess the number : ")
    t1=game(a,b,c)

    print(f"\nPlayer 2 guess the number : ")
    t2 = game(a, b, c)

    if t1>t2:
        print(f"player 1 Trails = {t1}\nplayer 2 Trails = {t2}")
        print("player 2 Won")
    elif t1==t2:
        print("Draw")
    else:
        print(f"player 1 Trails = {t1}\nplayer 2 Trails = {t2}")
        print("Player 1 won")







