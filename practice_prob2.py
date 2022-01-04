try:
    n=int(input("Enter the number of apples you got : "))
    min=int(input("Enter the minimum number for range : "))
    max=int(input("Enter the maximum number for range : "))

    for i in range(min,max+1):
        if n%i==0:
            if min == max:
                print(f"Its not a range and min:{min} and max:{max} are equal")
            print(f"{i} is a divisor of {n}")

        else:
            if min==max:
                print(f"Its not a range and min:{min} and max:{max} are equal")
            print(f"{i} is not a divisor of {n}")

except Exception as e:
    print("INVALID INPUT!",e)



